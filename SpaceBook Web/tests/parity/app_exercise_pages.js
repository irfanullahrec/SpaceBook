'use strict';
/* Every exercise of a Mathematics unit shows its questions in the Android app's reader (no empty page).
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
];

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 411, height: 900 }, hasTouch: true, isMobile: true, userAgent: 'Mozilla/5.0 (Linux; Android 14; Pixel) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36' });
  const errors = [];
  for (const [classId, subjectId, chIdx, tab, named, minPages] of BOOKS) {
    const chapter = catalog.classes.find(c => c.id === classId).subjects.find(s => s.id === subjectId).chapters[chIdx];
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
    for (let k = 0; k < 4; k++) {
      try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(3000); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded: wait again */ }
    }
    await page.evaluate(() => document.documentElement.classList.add('sbapp'));
    await page.addStyleTag({ content: fs.readFileSync(ASSETS + 'reader_mobile.css', 'utf8') });
    await page.addScriptTag({ content: fs.readFileSync(ASSETS + 'reader_bridge.js', 'utf8') });
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
  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log(`\n${pass} passed, ${fail} failed  (app exercise pages)`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
