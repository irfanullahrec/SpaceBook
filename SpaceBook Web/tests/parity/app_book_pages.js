'use strict';
/* A Class 11-12 page book (Pakistan Studies, HPE, Civics, ...) in the Android app's reader: the Lessons tab turns through printed pages (one card each,
 * its printed number once), the Solved Exercises tab shows the book's own exercise with an Ans on every question, and an Ans opens its answer.
 * The test puts the app's own two files on the website in a phone-sized Chrome (html.sbapp, the way the app's WebView does):
 *     node --max-old-space-size=6144 tests/parity/app_book_pages.js [--app "<folder of the app repo>"] [--shots <folder>] [--site bundled]
 * --site bundled serves the website copy the app ships (app/src/main/assets/site) instead of this folder, which tells whether the app was synced.
 * Without the app folder it says SKIP. Dev-only. */
const fs = require('fs'), path = require('path'), http = require('http');
const { serve, launch } = require('../baseline/lib');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const APP = path.resolve(opt('--app') || path.join(ROOT, '..', 'SpaceBook App'));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets') + path.sep;
if (!fs.existsSync(ASSETS + 'reader_bridge.js')) { console.log('SKIP  the app folder is not here (' + ASSETS + ')'); process.exit(0); }
const SHOTS = opt('--shots');
const bundled = opt('--site') === 'bundled';

let pass = 0, fail = 0;
const check = (l, ok, d) => { if (ok) { pass++; console.log('PASS  ' + l); } else { fail++; console.log('FAIL  ' + l + (d !== undefined ? '  -> ' + JSON.stringify(d).slice(0, 500) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));
const catalog = JSON.parse(fs.readFileSync(ASSETS + 'app_catalog.json', 'utf8'));

// [class, subject, chapter index, a page number that must be on a page of the Lessons tab, the least number of Ans buttons of the exercise]
const BOOKS = [
  ['cls12', 'cls12-pak', 1, 21, 25],
  ['cls12', 'cls12-hpe', 1, 3, 5],
  ['cls12', 'cls12-civics', 1, 12, 20],
  ['cls12', 'cls12-quran', 1, 8, 15],
  ['cls12', 'cls12-islhist', 1, 8, 5],
  ['cls12', 'cls12-islopt', 1, 50, 20],
  ['cls12', 'cls12-econ', 1, 10, 20]
];
const only = opt('--only');

(async () => {
  let base, server;
  if (bundled) {
    const site = ASSETS + 'site';
    server = http.createServer((req, res) => {
      let p = decodeURIComponent(req.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
      const f = path.join(site, p);
      fs.readFile(f, (e, b) => { if (e) { res.writeHead(404); return res.end(); } res.writeHead(200, { 'Content-Type': { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.png': 'image/png' }[path.extname(f)] || 'application/octet-stream' }); res.end(b); });
    });
    await new Promise(r => server.listen(0, '127.0.0.1', r));
    base = 'http://127.0.0.1:' + server.address().port + '/';
  } else { const s = await serve(0); server = s.server; base = s.url; }
  const browser = await launch();
  const ctx = await browser.newContext({ viewport: { width: 411, height: 900 }, hasTouch: true, isMobile: true, userAgent: 'Mozilla/5.0 (Linux; Android 14; Pixel) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36' });
  const errors = [];
  const prepare = async page => {
    for (let attempt = 0; attempt < 3; attempt++) {
      await page.goto(base + (process.env.SB_PAGE || (bundled ? 'index.html' : 'index.html')), { waitUntil: 'domcontentloaded', timeout: 180000 });
      for (let k = 0; k < 4; k++) {
        try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(3000); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded */ }
      }
      await page.evaluate(() => document.documentElement.classList.add('sbapp'));
      await page.addStyleTag({ content: fs.readFileSync(ASSETS + 'reader_mobile.css', 'utf8') });
      await page.addScriptTag({ content: fs.readFileSync(ASSETS + 'reader_bridge.js', 'utf8') });
      if (await page.waitForFunction(() => window.SBApp && typeof window.SBApp.open === 'function', null, { timeout: 20000 }).then(() => true, () => false)) return true;
    }
    return false;
  };
  for (const [classId, subjectId, chIdx, pageNo, minAns] of BOOKS) {
    if (only && !subjectId.includes(only)) continue;
    const subj = catalog.classes.find(c => c.id === classId).subjects.find(s => s.id === subjectId);
    const chapter = subj.chapters[chIdx];
    const tag = `${subjectId} "${chapter.t.slice(0, 24)}"`;
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    if (!await prepare(page)) { check(tag + ': the bridge runs', false); await page.close(); continue; }
    await page.evaluate(([c, s, call]) => window.SBApp.open(c, s, call, 0, ''), [classId, subjectId, chapter.o]);
    await sleep(4500);
    const st = await page.evaluate(() => window.SBApp.state());
    const les = await page.evaluate(() => {
      const cards = [...document.querySelectorAll('#subjTabContent .sb-pgcard, #subjTabContent .math-accordion-card')];
      return { bk: document.querySelectorAll('#subjTabContent .bk-page').length, cards: cards.length, labels: cards.map(c => (c.querySelector('.math-badge') || {}).textContent || '').filter(Boolean).slice(0, 5), text: (document.getElementById('subjTabContent') || {}).innerText.length };
    });
    // the Lessons tab is the website's own printed pages (.bk-page), one at a time; an older build drew one card per page (.sb-pgcard)
    check(`${tag}: the Lessons tab turns through printed pages`, st.pages >= 2 && (les.bk >= 2 || les.cards >= 2), { st, les });
    const hasPage = await page.evaluate(n => { const nos = [...document.querySelectorAll('#subjTabContent .bk-no')].map(x => x.textContent.trim()); if (nos.length) return nos.includes(String(n)); const all = [...document.querySelectorAll('#subjTabContent .sb-pgcard, #subjTabContent .math-accordion-card')]; return all.some(c => new RegExp('(^|\\D)' + n + '(\\D|$)').test((c.querySelector('.math-badge') || c).textContent.slice(0, 40))); }, pageNo);
    if (!subjectId.includes('islhist') && chIdx > 0) check(`${tag}: page ${pageNo} is a card of its own`, hasPage);
    if (SHOTS) { fs.mkdirSync(SHOTS, { recursive: true }); await page.screenshot({ path: path.join(SHOTS, subjectId + '_lesson.png') }); }
    // the exercise
    const exTab = ['حل شدہ مشقیں', 'Solved Exercises', 'Exercises'];
    let ok = false;
    for (const t of exTab) { await page.evaluate(w => window.SBApp.clickTab(w), t); await sleep(2500); const n = await page.evaluate(() => document.querySelectorAll('#subjTabContent .sb-ans').length); if (n) { ok = true; break; } }
    const n = await page.evaluate(() => document.querySelectorAll('#subjTabContent .sb-ans').length);
    check(`${tag}: the exercise tab has the book's questions with an Ans on each (${n})`, n >= minAns, n);
    if (n) {
      // open every page of the tab until an Ans button is on screen, click it, read the answer
      let shown = null;
      const total = (await page.evaluate(() => window.SBApp.state())).pages;
      for (let p = 0; p < total && !shown; p++) {
        await page.evaluate(i => window.SBApp.go(i), p); await sleep(500);
        shown = await page.evaluate(() => {
          const b = [...document.querySelectorAll('#subjTabContent .sb-ans')].find(x => { const r = x.getBoundingClientRect(); return r.width > 0 && r.height > 0 && x.offsetParent !== null; });
          if (!b) return null;
          b.scrollIntoView({ block: 'center' }); b.click(); return true;
        });
      }
      await sleep(1200);
      const ans = await page.evaluate(() => { const m = [...document.querySelectorAll('.sb-solve')].find(x => !x.hidden && x.getBoundingClientRect().width > 0); return m ? m.innerText.replace(/\s+/g, ' ').trim().slice(0, 160) : ''; });
      check(`${tag}: tapping Ans shows the answer`, ans.length > 8, ans);
      if (SHOTS) await page.screenshot({ path: path.join(SHOTS, subjectId + '_answer.png') });
    }
    await page.close();
  }
  check('no script error on the pages', errors.length === 0, errors.slice(0, 3));
  console.log(`\n${pass} passed, ${fail} failed`);
  await browser.close(); server.close();
  process.exit(fail ? 1 : 0);
})();
