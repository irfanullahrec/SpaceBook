'use strict';
/* Every exercise of a Mathematics unit shows its questions in the Android app's reader (no empty page); the question bank of Statistics (Classes 11-12)
 * is a page each; and the pages stay open in a long reading session, one chapter after the other in the same WebView.
 * The website's Exercises tab (js/sb_exercise_tabs.js) shows one exercise at a time under a bar of tabs and hides the other cards; the app turns the
 * pages itself (assets/reader_bridge.js, assets/reader_mobile.css), so every card must be shown when it is the page on screen. The test puts the app's
 * own two files on the website in a phone-sized Chrome (html.sbapp, the way the app's WebView does), opens the Exercises tab of Unit 3 and turns through
 * every page with SBApp.go(n).
 *     node --max-old-space-size=6144 tests/parity/app_exercise_pages.js [--app "<folder of the app repo>"]
 * Without the app folder it says SKIP. Dev-only. */
const fs = require('fs'), path = require('path');
const { serve, launch } = require('../baseline/lib');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const APP = path.resolve(args.includes('--app') ? args[args.indexOf('--app') + 1] : path.join(ROOT, '..', 'SpaceBook App'));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets') + path.sep;
if (!fs.existsSync(ASSETS + 'reader_bridge.js')) { console.log('SKIP  the app folder is not here (' + ASSETS + ')'); process.exit(0); }

let pass = 0, fail = 0;
const check = (l, ok, d) => { if (ok) { pass++; console.log('PASS  ' + l); } else { fail++; console.log('FAIL  ' + l + (d !== undefined ? '  -> ' + JSON.stringify(d).slice(0, 600) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));
const catalog = JSON.parse(fs.readFileSync(ASSETS + 'app_catalog.json', 'utf8'));

// [class, subject, chapter index (2 = Unit 3), tab words, the exercise a student reported as empty, how many pages the tab has at least]
const BOOKS = [
  ['cls6', 'cls6-math', 2, 'Exercises', 'ex-3.7', 9],        // Exercise 3.7 and every exercise but the first were empty
  ['cls5', 'cls5-math', 2, 'Exercises', 'Review Exercise 3', 3],
  ['cls8', 'cls8-math', 2, 'Exercises', 'ex-3.5', 7],
  ['cls11', 'cls11-stat', 2, 'Solved Exercises', 'class12-stat-exercise-0', 10],   // the question bank's cards are pages 2.. of the tab: their box was hidden with the bank's heading
];

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 411, height: 900 }, hasTouch: true, isMobile: true, userAgent: 'Mozilla/5.0 (Linux; Android 14; Pixel) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36' });
  const errors = [];
  // The website as the app's WebView shows it: html.sbapp, the app's stylesheet and bridge. The lazy page may reload itself once after it first looks
  // ready (the bridge is then gone), so the whole load is tried again until the bridge answers.
  const prepare = async page => {
    for (let attempt = 0; attempt < 3; attempt++) {
      await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
      for (let k = 0; k < 4; k++) {
        try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(3000); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded: wait again */ }
      }
      await page.evaluate(() => document.documentElement.classList.add('sbapp'));
      await page.addStyleTag({ content: fs.readFileSync(ASSETS + 'reader_mobile.css', 'utf8') });
      await page.addScriptTag({ content: fs.readFileSync(ASSETS + 'reader_bridge.js', 'utf8') });
      if (await page.waitForFunction(() => window.SBApp && typeof window.SBApp.open === 'function', null, { timeout: 20000 }).then(() => true, () => false)) return true;
    }
    return false;
  };
  for (const [classId, subjectId, chIdx, tab, named, minPages] of BOOKS) {
    const chapter = catalog.classes.find(c => c.id === classId).subjects.find(s => s.id === subjectId).chapters[chIdx];
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    check(`${classId}: the app's bridge is running on the page`, await prepare(page));
    await page.evaluate(([c, s, call]) => window.SBApp.open(c, s, call, 0, ''), [classId, subjectId, chapter.o]);
    await sleep(4000);
    await page.evaluate(t => window.SBApp.clickTab(t), tab); await sleep(3000);
    const st = await page.evaluate(() => window.SBApp.state());
    check(`${classId} ${chapter.t.split(' ').slice(0, 2).join(' ')}: the ${tab} tab has its exercises as pages`, st.mode === 'cards' && st.pages >= minPages, st);
    const empty = [];
    let sawNamed = false;
    for (let n = 0; n < st.pages; n++) {
      await page.evaluate(i => window.SBApp.go(i), n); await sleep(350);
      const r = await page.evaluate(() => {
        const u = document.querySelector('.sbapp-page-on');
        if (!u) return null;
        const b = u.getBoundingClientRect();
        return { id: u.id || '', h: Math.round(b.height), text: (u.innerText || '').replace(/\s+/g, ' ').trim().length, shown: getComputedStyle(u).display !== 'none' };
      });
      if (!r || !r.shown || r.h < 120 || r.text < 60) empty.push({ n, r });
      if (r && r.id.endsWith(named)) sawNamed = true;
    }
    check(`${classId}: no exercise page is empty (${st.pages} pages turned)`, empty.length === 0, empty.slice(0, 4));
    check(`${classId}: the exercise that was reported empty (${named}) is a page and shows its questions`, sawNamed && !empty.some(e => e.r && e.r.id.endsWith(named)));
    await page.close();
  }
  // A long reading session: the WebView is kept from chapter to chapter. The bridge opens a collapsed page by clicking its heading; that click
  // used to be taken for a tap on a sentence (a click made by code sits at (0, 0)), swallowed, and every Board SLO / MCQ page of the later
  // chapters stayed a 30 px heading. Chapter 1 is read tab by tab, then chapter 2's MCQ tab must show every page open.
  {
    const maths9 = catalog.classes.find(c => c.id === 'cls9').subjects.find(s => s.id === 'cls9-math').chapters;
    const page = await ctx.newPage();                              // its own page errors belong to the website, not to this check
    check('reading session: the app\'s bridge is running on the page', await prepare(page));
    const stable = async () => {                                    // the tab may still be building its cards: wait until the page count stops changing
      let st = await page.evaluate(() => window.SBApp.state()), same = 0;
      for (let w = 0; w < 16 && same < 2; w++) { await sleep(500); const s2 = await page.evaluate(() => window.SBApp.state()); same = s2.pages === st.pages ? same + 1 : 0; st = s2; }
      return st;
    };
    const open = async i => { await page.evaluate(([c, s, call]) => window.SBApp.open(c, s, call, 0, ''), ['cls9', 'cls9-math', maths9[i].o]); await sleep(4000); };
    await open(0);
    // every tab of chapter 1, the last ones (Formulas & Summary, Word Stats) too: what the page is left showing there decides whether the bug shows
    for (const tab of await page.evaluate(() => window.SBApp.tabs())) { await page.evaluate(t => window.SBApp.clickTab(t), tab); await sleep(900); const st = await stable(); for (let n = 0; n < Math.min(st.pages, 6); n++) { await page.evaluate(i => window.SBApp.go(i), n); await sleep(150); } }
    await open(1);
    await page.evaluate(() => window.SBApp.clickTab('Board SLO')); await sleep(900);
    const st = await stable();
    const closed = [];
    for (let n = 0; n < st.pages; n++) {
      await page.evaluate(i => window.SBApp.go(i), n); await sleep(150);
      const r = await page.evaluate(() => { const u = document.querySelector('.sbapp-page-on'); return u ? { id: u.id, closed: u.classList.contains('sb-topic-closed'), h: Math.round(u.getBoundingClientRect().height) } : null; });
      if (!r || r.closed || r.h < 100) closed.push({ n, r });
    }
    check(`reading session: chapter 2's MCQ tab has its pages (${st.pages})`, st.mode === 'cards' && st.pages >= 20, st);
    check(`reading session: no MCQ page of chapter 2 stays collapsed (${st.pages} pages turned)`, closed.length === 0, closed.slice(0, 3));
    await page.close();
  }
  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log(`\n${pass} passed, ${fail} failed  (app exercise pages)`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
