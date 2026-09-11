// Optional browser smoke tests; same setup as check_browser.cjs.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({viewport: {width: 390, height: 900}});
  await page.goto('http://127.0.0.1:8765/00-foundations/chapter.html', {waitUntil: 'networkidle'});
  await page.getByRole('button', {name: 'Toggle sidebar navigation'}).click();
  assert.equal(await page.getByRole('button', {name: 'Toggle sidebar navigation'}).getAttribute('aria-expanded'), 'true');
  await page.getByRole('button', {name: 'Toggle sidebar navigation'}).click();
  await page.getByRole('button', {name: 'Search', exact: true}).click();
  const search = page.locator('input.aa-Input');
  await search.fill('Hensel');
  await page.waitForSelector('.aa-Item');
  assert.match(await page.locator('.aa-Panel').innerText(), /Hensel|Modular/i);
  await page.keyboard.press('Escape');
  const toggle = page.locator('.callout [data-bs-toggle="collapse"]').first();
  await toggle.scrollIntoViewIfNeeded();
  await toggle.focus();
  await page.keyboard.press('Enter');
  assert.equal(await toggle.getAttribute('aria-expanded'), 'true');
  await page.waitForSelector('.callout-collapse.show');
  await page.keyboard.press(' ');
  await page.waitForSelector('.callout-collapse.show', {state: 'hidden'});
  assert.equal(await toggle.getAttribute('aria-expanded'), 'false');
  await page.keyboard.press('Enter');
  await page.setViewportSize({width: 1440, height: 900});
  await page.locator('.quarto-color-scheme-toggle').first().click();
  assert(await page.locator('body').evaluate(e => e.classList.contains('quarto-dark')));
  const colors = await page.evaluate(() => ({
    text: getComputedStyle(document.body).color,
    background: getComputedStyle(document.body).backgroundColor,
    search: getComputedStyle(document.querySelector('.aa-DetachedSearchButtonIcon svg')).fill,
  }));
  function luminance(color) {
    const rgb = color.match(/[\d.]+/g).slice(0,3).map(Number).map(x => x / 255);
    return rgb.map(x => x <= 0.04045 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4)
      .reduce((total, x, i) => total + x * [0.2126,0.7152,0.0722][i], 0);
  }
  const background = luminance(colors.background);
  const contrast = color => (Math.max(luminance(color), background)+0.05)/(Math.min(luminance(color), background)+0.05);
  assert(contrast(colors.text) >= 4.5);
  assert(contrast(colors.search) >= 3);
  await page.screenshot({path: '/tmp/icpc-dark-solutions.png'});
  const next = page.locator('.page-navigation .nav-page-next a');
  assert(await next.count());
  await next.click();
  assert.match(page.url(), /NOTATION\.html/);
  console.log('Mobile navigation, search, Enter/Space solution activation, dark text/icon contrast, dark mode, and next-page navigation passed');
  await browser.close();
})().catch(error => {console.error(error); process.exit(1);});
