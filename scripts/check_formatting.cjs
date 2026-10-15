// Run after quarto render, serving _site on port 8765. Requires Playwright.
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');

(async () => {
  const root = path.resolve(__dirname, '..');
  const sources = fs.readdirSync(root, {recursive: true})
    .filter(file => file.endsWith('.qmd') && !file.split(path.sep).some(part => part.startsWith('.') || part === '_site'));
  const browser = await chromium.launch({headless: true, ...(process.env.BROWSER_EXECUTABLE ? {executablePath: process.env.BROWSER_EXECUTABLE} : {})});
  const page = await browser.newPage();
  // Structure checks do not need remote equation/diagram rendering.
  await page.route('**/*', route => new URL(route.request().url()).hostname === '127.0.0.1' ? route.continue() : route.abort());
  let dropdowns = 0;
  try {
    for (const source of sources.sort()) {
      const response = await page.goto('http://127.0.0.1:8765/' + source.replace(/\.qmd$/, '.html'), {waitUntil: 'domcontentloaded'});
      assert.equal(response.status(), 200, source);
      const result = await page.locator('main').evaluate(main => {
        const errors = [];
        const details = [...main.querySelectorAll('details')];
        const callouts = [...main.querySelectorAll('.callout-collapse')];
        for (const detail of details) {
          const body = detail.cloneNode(true);
          body.querySelector('summary')?.remove();
          if (body.textContent.trim().length < 10) errors.push('Empty dropdown: ' + detail.textContent.trim());
          if (detail.open) errors.push('Dropdown starts expanded: ' + detail.querySelector('summary')?.textContent);
        }
        for (const callout of callouts) {
          if (callout.textContent.trim().length < 10) errors.push('Empty collapsible callout');
          if (callout.classList.contains('show')) errors.push('Callout starts expanded');
        }
        for (const paragraph of main.querySelectorAll('p')) {
          const copy = paragraph.cloneNode(true);
          copy.querySelectorAll('.math, code, mjx-container').forEach(node => node.replaceWith('MATH'));
          const text = copy.textContent;
          if (/(?:^|\n)\s*(?:[-*]|\d+[.)])\s/.test(text) || /\$\$|^\s*:::/m.test(text)) {
            errors.push('Exposed Markdown: ' + text.trim().slice(0, 180));
          }
        }
        return {errors, dropdowns: details.length + callouts.length};
      });
      assert.deepEqual(result.errors, [], source);
      const sourceText = fs.readFileSync(path.join(root, source), 'utf8');
      const expected = (sourceText.match(/<details(?:\s|>)/g) || []).length
        + (sourceText.match(/^ *:{3,}.*collapse="true"/gm) || []).length;
      assert.equal(result.dropdowns, expected, source + ': every source dropdown must render');
      dropdowns += result.dropdowns;
    }
    await page.unroute('**/*');
    // Exercise both native hint dropdowns and Quarto solution callouts on desktop/mobile.
    for (const width of [1440, 390]) {
      await page.setViewportSize({width, height: 900});
      await page.goto('http://127.0.0.1:8765/chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.html');
      await page.evaluate(async () => { if (window.MathJax?.startup?.promise) await Promise.race([window.MathJax.startup.promise, new Promise(resolve => setTimeout(resolve, 10000))]); });
      const hint = page.locator('main details').first();
      await hint.locator('summary').click();
      assert(await hint.evaluate(node => node.open));
      await hint.locator('summary').click();
      assert(!(await hint.evaluate(node => node.open)));
      const solution = page.locator('main .callout').filter({has: page.locator('.callout-title-container', {hasText: 'Complete Derivation'})}).first();
      const toggle = solution.locator('[data-bs-toggle="collapse"]');
      const heading = solution.locator('#reduction-from-exact-maximum-degree-to-bounded-maximum-degree > h4');
      assert.equal(await heading.isVisible(), false);
      await toggle.click();
      await heading.waitFor({state: 'visible'});
      await heading.scrollIntoViewIfNeeded();
      await page.screenshot({path: `/tmp/icpc-format-solution-${width}.png`});
      await toggle.click();
      await heading.waitFor({state: 'hidden'});
    }
    console.log(`${sources.length} pages; ${dropdowns} dropdowns; list syntax, solution containment, and desktop/mobile toggles passed`);
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
