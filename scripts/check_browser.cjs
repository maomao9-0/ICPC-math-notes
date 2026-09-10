// Optional integration check: requires Playwright and its Chromium browser.
// Serve _site locally, then run NODE_PATH=<playwright-package-dir> node this-file.
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');

(async () => {
  const root = path.resolve(__dirname, '..');
  const sources = fs.readdirSync(root).filter(x => x.endsWith('.qmd'));
  for (const dir of fs.readdirSync(root).filter(x => /^\d\d-/.test(x))) {
    for (const file of fs.readdirSync(path.join(root, dir)).filter(x => x.endsWith('.qmd'))) {
      sources.push(dir + '/' + file);
    }
  }
  const browser = await chromium.launch({headless: true});
  const results = [];
  const page = await browser.newPage();
  for (const width of [1440, 390]) {
    await page.setViewportSize({width, height: 900});
    for (const source of sources.sort()) {
      const errors = [];
      const errorListener = e => errors.push(e.message);
      page.on('pageerror', errorListener);
      const response = await page.goto('http://127.0.0.1:8765/' + source.replace(/\.qmd$/, '.html'), {waitUntil: 'networkidle'});
      await page.evaluate(async () => { if (window.MathJax?.startup?.promise) await window.MathJax.startup.promise; });
      const details = await page.evaluate(() => ({
        overflow: document.documentElement.scrollWidth > window.innerWidth + 2,
        mathErrors: Array.from(document.querySelectorAll('mjx-merror,[data-mjx-error]')).map(x => x.textContent),
        title: document.querySelector('h1')?.textContent,
        typesetMath: document.querySelectorAll('mjx-container').length,
        main: !!document.querySelector('main'),
        toc: !!document.querySelector('#TOC'),
      }));
      results.push({source, width, status: response.status(), errors, ...details});
      page.off('pageerror', errorListener);
    }
  }
  for (const [source, width, name] of [
    ['00-prerequisite-audit/chapter.html', 1440, 'foundations-desktop'],
    ['03-advanced-sieves/chapter.html', 390, 'sieves-mobile'],
    ['16-set-power-series/chapter.html', 390, 'set-series-mobile'],
    ['index.html', 1440, 'index-desktop']
  ]) {
    await page.setViewportSize({width, height: 900});
    await page.goto('http://127.0.0.1:8765/' + source, {waitUntil:'networkidle'});
    await page.screenshot({path: '/tmp/icpc-' + name + '.png'});
  }
  await browser.close();
  console.log(JSON.stringify(results, null, 2));
  const failed = results.some(x => x.status !== 200 || x.errors.length || x.mathErrors.length || x.overflow || !x.main || !x.title);
  process.exitCode = failed ? 1 : 0;
})().catch(error => { console.error(error); process.exitCode = 1; });
