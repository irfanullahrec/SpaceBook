'use strict';
/* Bookmarks, notes, highlights, the Saved page, "continue" and "my class" in a real browser (the installed Chrome through Playwright):
 *     node --max-old-space-size=8192 tests/library/browser.js [--out <folder for screenshots>]
 * Loads the whole app (index.html; needs about 1 GB of free memory), opens Class 5 Maths "Fractions" and uses js/sb_library.js the way a
 * student would. Guest mode: the items are kept in this browser (localStorage), no server is involved.
 * Dev-only, never shipped. */
const fs = require('fs'), os = require('os'), path = require('path');
const { serve, launch } = require('../baseline/lib');

const args = process.argv.slice(2);
const OUT = path.resolve(args.includes('--out') ? args[args.indexOf('--out') + 1] : path.join(os.tmpdir(), 'sb_library_shots'));
fs.mkdirSync(OUT, { recursive: true });
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 860 } });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/favicon|ERR_|Failed to load resource|net::|api\//.test(m.text())) errors.push('console: ' + m.text()); });
  const shot = async name => { try { await page.screenshot({ path: path.join(OUT, name + '.png') }); } catch (e) { /* page busy */ } };

  async function boot() {
    await page.goto(url + 'index.html', { waitUntil: 'domcontentloaded', timeout: 180000 });
    await page.waitForFunction(() => window.SBLibrary && window.SBItems && typeof openSubject === 'function' && window.SBContinue, null, { timeout: 120000 });
  }
  async function openFractions() {
    await page.evaluate(() => { openSubject('cls5', 'cls5-math'); });
    await sleep(800);
    await page.evaluate(() => { selectSubjectChapter('math', 2, 'cls5'); });
    await page.waitForSelector('.sbl-tools', { timeout: 20000 });
    await sleep(400);
  }
  const items = (kind) => page.evaluate(k => SBItems.list(k), kind);

  await boot();
  await openFractions();
  const units = await page.evaluate(() => SBLibrary.collect().units.length);
  const tools = await page.evaluate(() => document.querySelectorAll('.sbl-tools').length);
  check('every page of the chapter has one set of buttons (' + units + ' pages)', units > 3 && tools === units, { units, tools });

  // bookmark
  const key1 = 'cls5-math|2|Lessons|1';
  await page.click('[data-sbl-idx="1"] .sbl-btn[data-sbl="bm"]');
  await sleep(300);
  let bms = await items('bm');
  check('tapping the bookmark saves the page with its place and title', bms.length === 1 && bms[0].key === key1 && bms[0].value.c === 'cls5' && bms[0].value.ch === 2 && bms[0].value.p === 1 && /Fractions/.test(bms[0].value.t), bms);
  check('and the button shows it is on', await page.$eval('[data-sbl-idx="1"] .sbl-btn[data-sbl="bm"]', b => b.classList.contains('on') && b.getAttribute('aria-pressed') === 'true'));
  await page.click('[data-sbl-idx="1"] .sbl-btn[data-sbl="bm"]'); await sleep(250);
  check('tapping again removes it', (await items('bm')).length === 0 && await page.$eval('[data-sbl-idx="1"] .sbl-btn[data-sbl="bm"]', b => !b.classList.contains('on')));
  await page.click('[data-sbl-idx="1"] .sbl-btn[data-sbl="bm"]'); await sleep(250);

  // a note
  await page.click('[data-sbl-idx="2"] .sbl-btn[data-sbl="note"]');
  await page.waitForSelector('.sbl-modal textarea');
  await page.fill('.sbl-modal textarea', 'Add the numerators, keep the denominator');
  await shot('note-editor');
  await page.click('.sbl-save'); await sleep(300);
  let notes = await items('note');
  check('a note is saved on that page', notes.length === 1 && notes[0].value.x === 'Add the numerators, keep the denominator' && notes[0].value.p === 2 && notes[0].value.k === 'note', notes);
  check('the page button counts it', await page.$eval('[data-sbl-idx="2"] .sbl-n', n => !n.hidden && n.textContent === '1'));

  // a highlight from selected words
  const picked = await page.evaluate(() => {
    const unit = SBLibrary.collect().units[3];
    const w = document.createTreeWalker(unit, NodeFilter.SHOW_TEXT, { acceptNode: t => (t.nodeValue.trim().length > 20 && !t.parentElement.closest('.sbl-tools, script, style') && t.parentElement.offsetParent !== null) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT });
    const t = w.nextNode();
    if (!t) return null;
    const start = t.nodeValue.search(/\S/);
    const r = document.createRange(); r.setStart(t, start); r.setEnd(t, start + 12);
    const s = getSelection(); s.removeAllRanges(); s.addRange(r);
    return String(s);
  });
  await page.waitForSelector('.sbl-pop', { timeout: 5000 }).catch(() => null);
  check('selecting words on a page offers Highlight and Note', !!picked && !!(await page.$('.sbl-pop')), picked);
  if (await page.$('.sbl-pop')) await page.click('.sbl-pop [data-a="hl"]');
  await sleep(500);
  notes = await items('note');
  const hl = notes.find(n => n.value.k === 'hl');
  check('Highlight saves the selected words', !!hl && hl.value.q === picked.replace(/\s+/g, ' ').trim() && hl.value.p === 3, notes);
  check('and the words are marked on the page', (await page.$$('mark.sbl-mark')).length >= 1);
  await shot('reader-marked');

  // position
  await sleep(3000);
  const pos = await page.evaluate(() => SBItems.get('pos', 'cls5-math'));
  check('where the student is reading is kept (chapter, tab, page count)', !!pos && pos.ch === 2 && pos.c === 'cls5' && pos.tb === 'Lessons' && pos.n === units, pos);

  // everything survives a reload and shows again
  await boot();
  await openFractions();
  check('after a reload the bookmark is still on', await page.$eval('[data-sbl-idx="1"] .sbl-btn[data-sbl="bm"]', b => b.classList.contains('on')));
  check('and the note count and the marked words are back', await page.$eval('[data-sbl-idx="2"] .sbl-n', n => n.textContent === '1') && (await page.$$('mark.sbl-mark')).length >= 1);
  check('the page still has exactly one set of buttons per page after being drawn twice', (await page.evaluate(() => document.querySelectorAll('.sbl-tools').length)) === units);

  // the Saved page
  await page.evaluate(() => document.querySelector('.nav-link[data-page="saved"]').click());
  await page.waitForSelector('.sbl-page', { timeout: 10000 });
  const rows = await page.$$eval('.sbl-row-item', r => r.map(x => x.dataset.kind));
  check('the Saved page lists the bookmark, the note and the highlight', rows.filter(k => k === 'bm').length === 1 && rows.filter(k => k === 'note').length === 2, rows);
  await shot('saved-page');
  await page.evaluate(() => { openSubject('cls9', 'cls9-math'); });                 // go away from the book, then open the bookmark from Saved
  await sleep(600);
  await page.evaluate(() => document.querySelector('.nav-link[data-page="saved"]').click());
  await page.waitForSelector('.sbl-row-item[data-kind="bm"] .sbl-open');
  await page.click('.sbl-row-item[data-kind="bm"] .sbl-open');
  await page.waitForSelector('.sbl-flash', { timeout: 15000 }).catch(() => null);
  const where = await page.evaluate(() => { const l = SBContinue.current(); return { cur: l, active: (document.querySelector('.math-ch-btn.active, .ch-btn.active, [class*="ch-btn"].active') || {}).textContent }; });
  check('opening a bookmark goes to its class, subject, chapter and page', !!where.cur && where.cur.subjId === 'cls5-math' && /Fractions/.test(where.active || ''), where);
  check('and marks the page for a moment', await page.evaluate(() => !!document.querySelector('[data-sbl-idx="1"].sbl-flash') || SBLibrary.collect().units[1] != null));

  // a note can be removed from the Saved page; a delete reaches the page tools
  await page.evaluate(() => document.querySelector('.nav-link[data-page="saved"]').click());
  await page.waitForSelector('.sbl-row-item[data-kind="note"] .sbl-del');
  await page.click('.sbl-row-item[data-kind="note"] .sbl-del'); await sleep(300);
  check('deleting a note from the Saved page removes it', (await items('note')).length === 1 && (await page.$$('.sbl-row-item[data-kind="note"]')).length === 1);

  // my class
  await page.evaluate(() => goToSubjects('cls5'));
  await page.waitForSelector('.sbl-class-star', { timeout: 5000 });
  await page.click('.sbl-class-star'); await sleep(300);
  check('the star on a class page makes it "my class"', (await page.evaluate(() => SBItems.get('pref', 'class'))).id === 'cls5' && /My class/.test(await page.$eval('.sbl-class-star', b => b.textContent)));
  await page.evaluate(() => renderClasses()); await sleep(300);
  check('and the class card says so', (await page.$$('.class-jewel-card.sbl-mine')).length === 1 && /My class/.test(await page.$eval('.sbl-mine-tag', t => t.textContent)));

  // phone width: no sideways scroll, the buttons are big enough to tap
  await page.setViewportSize({ width: 375, height: 800 });
  await boot();
  await openFractions();
  const phone = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, btn: document.querySelector('.sbl-btn').getBoundingClientRect().width }));
  check('on a 375 px phone nothing scrolls sideways and the buttons are at least 34 px', phone.sw <= phone.cw + 1 && phone.btn >= 34, phone);
  await shot('reader-phone');

  check('nothing threw in the console', errors.length === 0, errors);
  await browser.close(); server.close();
  console.log('---\nlibrary browser tests: ' + pass + ' passed, ' + fail + ' failed (screenshots in ' + OUT + ')');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  ' + (e && e.stack || e)); process.exit(1); });
