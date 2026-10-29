'use strict';
/* Government / Private / Series in a real browser (the installed Chrome through Playwright), on the lazy page:
 *     node --max-old-space-size=4096 tests/private/browser.js [--out <folder for screenshots>]
 * Clicks Class 1-8 and 9, goes through the two modals, opens the Munawar grid of each class and a Munawar book, and comes back.
 * Dev-only, never shipped. */
const fs = require('fs'), os = require('os'), path = require('path');
const { serve, launch } = require('../baseline/lib');

const args = process.argv.slice(2);
const OUT = path.resolve(args.includes('--out') ? args[args.indexOf('--out') + 1] : path.join(os.tmpdir(), 'sb_private_shots'));
fs.mkdirSync(OUT, { recursive: true });
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 1100, height: 800 } });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|ERR_|Failed to load resource|net::|api\//.test(m.text())) errors.push('console: ' + m.text()); });
  const shot = async name => { try { await page.screenshot({ path: path.join(OUT, name + '.png') }); } catch (e) { /* page busy */ } };

  await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
  await page.waitForFunction(() => window.SBPrivate && typeof openSubject === 'function' && typeof renderClasses === 'function', null, { timeout: 120000 });
  await page.evaluate(() => renderClasses());
  await sleep(500);

  const cards = await page.evaluate(() => document.querySelectorAll('.class-jewel-card').length);
  check('the class page lists the classes', cards >= 12, cards);

  // a click on Class 1 asks Government or Private
  await page.click('.class-jewel-card[aria-label="Open Class 1"]');
  await page.waitForSelector('.sbp-dialog');
  const first = await page.evaluate(() => ({
    title: document.querySelector('#sbpTitle').textContent, eyebrow: document.querySelector('.sbp-eyebrow').textContent,
    cards: [...document.querySelectorAll('.sbp-card')].map(c => c.querySelector('.sbp-card-name').textContent),
    gov: [...document.querySelectorAll('.sbp-gov .sbp-stat b')].map(b => b.textContent),
    priv: [...document.querySelectorAll('.sbp-priv .sbp-stat b')].map(b => b.textContent),
    modal: document.querySelector('.sbp-dialog').getAttribute('aria-modal'), focused: document.activeElement.className,
    gov8: DATA.subjects.cls1.filter(s => !s.series).length, priv11: DATA.subjects.cls1.filter(s => s.series).length,
  }));
  await shot('01-boards');
  check('Class 1 opens a modal with the two cards "Government Books" and "Private Books"', first.cards.join('|') === 'Government Books|Private Books' && first.modal === 'true' && /Class 1/.test(first.eyebrow), first);
  check('the Government card counts the Government books, the Private card the series and the Munawar books', first.gov[0] === String(first.gov8) && first.priv[0] === '1' && first.priv[1] === String(first.priv11), first);
  check('focus moves into the dialog', /sbp-card|sbp-close/.test(first.focused), first.focused);

  // Escape closes it and gives the focus back
  await page.keyboard.press('Escape');
  await sleep(200);
  check('Escape closes the modal', await page.evaluate(() => !document.querySelector('.sbp-overlay')));

  // Government: the board's books only
  await page.click('.class-jewel-card[aria-label="Open Class 1"]');
  await page.waitForSelector('.sbp-dialog');
  await page.click('.sbp-gov');
  await sleep(700);
  const gov = await page.evaluate(() => ({ covers: [...document.querySelectorAll('.cls1-cover-img')].map(i => i.getAttribute('src')), bar: !!document.querySelector('.sbp-bar'), series: SBPrivate.current('cls1') }));
  check('Government shows the 8 board books, no Munawar cover and no series bar', gov.covers.length === 8 && !gov.covers.some(s => /Munawar/.test(s)) && !gov.bar && gov.series === '', gov);

  // Private -> series -> Munawar, class by class
  const expect = { cls1: 11, cls2: 10, cls3: 11, cls4: 10 };
  for (const cls of Object.keys(expect)) {
    await page.evaluate(c => { SBPrivate.entry(c); }, cls);
    await page.waitForSelector('.sbp-priv');
    await page.click('.sbp-priv');
    await page.waitForSelector('.sbp-munawar');
    if (cls === 'cls1') {
      const s = await page.evaluate(() => ({ title: document.querySelector('#sbpTitle').textContent, name: document.querySelector('.sbp-munawar .sbp-card-name').textContent, back: !!document.querySelector('.sbp-back'), books: document.querySelector('.sbp-munawar .sbp-stat b').textContent, chips: document.querySelectorAll('.sbp-munawar .sbp-chip').length }));
      await shot('02-series');
      check('Private asks for the series: one card, "Munawar", with its books and their names', s.title === 'Choose a series' && s.name === 'Munawar' && s.back && s.books === '11' && s.chips === 11, s);
      await page.click('.sbp-back');
      await page.waitForSelector('.sbp-gov');
      check('"Government or Private" goes back to the first modal', true);
      await page.click('.sbp-priv');
      await page.waitForSelector('.sbp-munawar');
    }
    await page.click('.sbp-munawar');
    await sleep(700);
    const g = await page.evaluate(() => ({ covers: [...document.querySelectorAll('.cls1-cover-img')].map(i => i.getAttribute('src')), bar: (document.querySelector('.sbp-bar') || {}).textContent }));
    if (cls === 'cls1') await shot('03-munawar-class1');
    check(cls + ': the Munawar grid shows ' + expect[cls] + ' Munawar covers and the series bar', g.covers.length === expect[cls] && g.covers.every(s => /covers\/Munawar\/mun?/.test(s) || /Munawar\/cls\d-mun-/.test(s)) && /Munawar/.test(g.bar || ''), g);
  }

  // Classes 5-8 have no Munawar books yet: a notice, not a blank page
  for (const cls of ['cls5', 'cls8']) {
    await page.evaluate(c => { SBPrivate.entry(c); }, cls);
    await page.waitForSelector('.sbp-priv');
    await page.click('.sbp-priv');
    await page.click('.sbp-munawar');
    await sleep(400);
    const e = await page.evaluate(() => (document.querySelector('.sbp-empty h2') || {}).textContent);
    check(cls + ': Munawar says its books are coming', /coming/.test(e || ''), e);
  }

  // Class 9 does not ask
  await page.evaluate(() => SBPrivate.entry('cls9'));
  await sleep(500);
  check('Class 9 goes straight to its subjects, without a modal', await page.evaluate(() => !document.querySelector('.sbp-overlay') && state.selectedClass === 'cls9' && state.activeView === 'subjects'));

  // a Munawar book opens in the Government reader, and Back returns to the Munawar grid
  await page.evaluate(() => { SBPrivate.entry('cls1'); });
  await page.waitForSelector('.sbp-priv'); await page.click('.sbp-priv'); await page.click('.sbp-munawar'); await sleep(600);
  await page.click('button[aria-label="Kanz Mathematics"]');
  await page.waitForFunction(() => document.getElementById('subjTabContent') && /Whole Numbers/.test(document.getElementById('subjTabContent').innerText), null, { timeout: 60000 });
  await sleep(800);
  const book = await page.evaluate(() => ({
    key: state.activeSubject, units: document.querySelectorAll('.math-ch-sidebar .math-ch-btn, .math-ch-sidebar [onclick*="selectSubjectChapter"]').length,
    text: document.getElementById('subjTabContent').innerText, pages: document.querySelectorAll('#subjTabContent .m6-page, #subjTabContent .book-spread, #subjTabContent [data-page]').length,
  }));
  await shot('04-book');
  check('Class 1 Munawar Mathematics opens in the reader with its chapters and its transcribed pages', book.key === 'mun-math' && /Numbers 1-9/.test(book.text) && /Contents/.test(book.text), { key: book.key, units: book.units });
  const back = await page.evaluate(async () => { handleGlobalNavBack(); await new Promise(r => setTimeout(r, 600)); return { series: SBPrivate.current('cls1'), bar: !!document.querySelector('.sbp-bar'), covers: document.querySelectorAll('.cls1-cover-img').length }; });
  check('Back from the book returns to the Munawar grid, not to the Government books', back.series === 'munawar' && back.bar && back.covers === 11, back);
  const gov2 = await page.evaluate(async () => { openSubject('cls1', 'cls1-math'); await new Promise(r => setTimeout(r, 1200)); const s = SBPrivate.current('cls1'); goToSubjects('cls1'); await new Promise(r => setTimeout(r, 500)); return { s, series: SBPrivate.current('cls1'), covers: document.querySelectorAll('.cls1-cover-img').length }; });
  check('opening a Government book makes Back return to the Government books', gov2.s === '' && gov2.series === '' && gov2.covers === 8, gov2);

  check('no page errors', errors.length === 0, errors.slice(0, 4));
  await browser.close(); server.close();
  console.log(`\n${pass} passed, ${fail} failed; screenshots in ${OUT}`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
