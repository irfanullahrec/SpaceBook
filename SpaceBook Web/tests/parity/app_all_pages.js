'use strict';
/* Every book of Classes 1-12 in the Android app's reader, page by page. The app's own two files (reader_mobile.css, reader_bridge.js) are put on the
 * website in a phone-sized Chrome (html.sbapp, the way the app's WebView does); every chapter of every subject in assets/app_catalog.json is opened
 * the way the app opens it (SBApp.open) and its Lessons tab and Exercises tab are turned page by page (SBApp.go). A page is reported when
 *   - the tab has no pages at all (chapter opens empty / not paged),
 *   - a page is empty (under 120 px tall or under 40 characters of text), or
 *   - the page number is shown twice on one page (a "Page 7" chip and the footer circle, or two chips).
 * Run:  node --max-old-space-size=4096 tests/parity/app_all_pages.js [--classes 1,12] [--only <subject id part>] [--site web|bundled]
 *           [--exercises] [--out report.json] [--app "<app repo>"]
 * --site bundled serves the website copy the app ships (what the phone shows); the default serves this folder. Dev-only, takes long (a whole class
 * is minutes, all twelve are hours); each finished chapter is appended to the --out file as one JSON line. */
const fs = require('fs'), path = require('path'), http = require('http');
const { serve, launch } = require('../baseline/lib');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const APP = path.resolve(opt('--app') || path.join(ROOT, '..', 'SpaceBook App'));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets') + path.sep;
if (!fs.existsSync(ASSETS + 'reader_bridge.js')) { console.log('SKIP  the app folder is not here (' + ASSETS + ')'); process.exit(0); }
const classes = (opt('--classes') || '1,2,3,4,5,6,7,8,9,10,11,12').split(',').map(x => 'cls' + x.trim());
const only = opt('--only');
const bundled = opt('--site') === 'bundled';
const withEx = args.includes('--exercises');
const out = opt('--out');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const catalog = JSON.parse(fs.readFileSync(ASSETS + 'app_catalog.json', 'utf8'));

(async () => {
  let base, server;
  if (bundled) {
    const site = ASSETS + 'site';
    const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.png': 'image/png' };
    server = http.createServer((req, res) => {
      let p = decodeURIComponent(req.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
      const f = path.join(site, p);
      fs.readFile(f, (e, b) => { if (e) { res.writeHead(404); return res.end(); } res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' }); res.end(b); });
    });
    await new Promise(r => server.listen(0, '127.0.0.1', r));
    base = 'http://127.0.0.1:' + server.address().port + '/';
  } else { const s = await serve(0); server = s.server; base = s.url; }
  const browser = await launch();
  const css = fs.readFileSync(ASSETS + 'reader_mobile.css', 'utf8'), bridge = fs.readFileSync(ASSETS + 'reader_bridge.js', 'utf8');
  const newPage = async () => {
    const ctx = await browser.newContext({ viewport: { width: 411, height: 900 }, hasTouch: true, isMobile: true, userAgent: 'Mozilla/5.0 (Linux; Android 14; Pixel) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36' });
    const page = await ctx.newPage();
    for (let attempt = 0; attempt < 3; attempt++) {
      await page.goto(base + (process.env.SB_PAGE || 'index.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
      for (let k = 0; k < 4; k++) {
        try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(2500); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded */ }
      }
      await page.evaluate(() => document.documentElement.classList.add('sbapp'));
      await page.addStyleTag({ content: css });
      await page.addScriptTag({ content: bridge });
      if (await page.waitForFunction(() => window.SBApp && typeof window.SBApp.open === 'function', null, { timeout: 20000 }).then(() => true, () => false)) return { ctx, page };
    }
    return null;
  };
  // what the page on screen is: size, text, and how many times a page number is printed on it
  const measure = () => {
    const u = document.querySelector('.sbapp-page-on') || ((window.SBApp.state() || {}).mode === 'flow' ? document.getElementById('subjTabContent') || document.getElementById('mathTabContent') : null);   // a tab with one card is read as it is
    if (!u) return null;
    const r = u.getBoundingClientRect();
    const txt = (u.innerText || '').replace(/\s+/g, ' ').trim();
    const heads = [...u.querySelectorAll('.math-badge, .bk-no, .sb-pn')].filter(e => e.getBoundingClientRect().width > 0 && getComputedStyle(e).display !== 'none').map(e => e.textContent.trim()).filter(t => /^(Page|Pages|Scan|PDF|p\.|صفحہ|پاڼه)?\s*[\dIVXivx–-]+$/.test(t));
    return { h: Math.round(r.height), text: txt.length, labels: heads, head: txt.slice(0, 60) };
  };
  // the tab strip's buttons carry data-tab (lesson, exercise ...): the same on every book, whatever language its label is in
  const selectTab = async (page, id) => {
    const on = await page.evaluate(i => { const b = document.querySelector('.math-nav-tabs [data-tab="' + i + '"], .math-top-tab[data-tab="' + i + '"], .math-tab-btn[data-tab="' + i + '"]'); if (!b) return 'none'; if (b.classList.contains('active')) return 'already'; b.click(); return 'clicked'; }, id);
    if (on === 'clicked') await sleep(1800);
    return on;
  };
  // a heavy chapter is drawn, then its cards are wrapped into page cards a moment later: wait until the page count stops changing
  const settle = async page => {
    let last = -1, same = 0;
    for (let k = 0; k < 20 && same < 2; k++) { await sleep(600); const n = await page.evaluate(() => window.SBApp.state().pages); same = n === last ? same + 1 : 0; last = n; }
  };
  const turn = async page => {
    await settle(page);
    const st = await page.evaluate(() => window.SBApp.state());
    const issues = [];
    let blank = 0;
    for (let n = 0; n < st.pages; n++) {
      await page.evaluate(i => window.SBApp.go(i), n);
      let m = await page.evaluate(measure);
      // a collapsed card is opened by the bridge a moment after the page is turned (it clicks the card's heading): look again before calling it empty
      if (!m || m.h < 120 || m.text < 40) { await sleep(500); m = await page.evaluate(measure); }
      if (!m) { issues.push({ n, why: 'no page on screen' }); continue; }
      if (m.h < 120 || m.text < 40) { blank++; issues.push({ n, why: 'empty', h: m.h, text: m.text, head: m.head }); }
      if (m.labels.length > 1) issues.push({ n, why: 'page number shown more than once', labels: m.labels });
    }
    return { pages: st.pages, mode: st.mode, issues };
  };
  let total = 0, bad = 0;
  for (const cl of catalog.classes) {
    if (!classes.includes(cl.id)) continue;
    for (const s of cl.subjects) {
      if (only && !s.id.includes(only)) continue;
      let pg = await newPage();
      if (!pg) { console.log(JSON.stringify({ cls: cl.id, subject: s.id, error: 'bridge did not start' })); continue; }
      for (let ci = 0; ci < s.chapters.length; ci++) {
        const ch = s.chapters[ci];
        const rec = { cls: cl.id, subject: s.id, chapter: ci, title: String(ch.t || '').slice(0, 40) };
        try {
          const before = await pg.page.evaluate(() => (window.SBApp.state() || {}).title);
          await pg.page.evaluate(([c, sid, call]) => window.SBApp.open(c, sid, call, 0, 'Lessons'), [cl.id, s.id, ch.o]);
          // wait for the chapter to be on screen as pages (cards / book); a chapter that never pages is given 12 s, then measured as it is
          let st = null;
          for (let k = 0; k < 24; k++) { await sleep(500); st = await pg.page.evaluate(() => window.SBApp.state()); if (st && st.ready && (st.mode === 'cards' || st.mode === 'book') && st.pages >= 1 && (st.title !== before || ci === 0) && k >= 2) break; }
          if (await selectTab(pg.page, 'lesson') === 'clicked') { for (let k = 0; k < 10; k++) { await sleep(400); st = await pg.page.evaluate(() => window.SBApp.state()); if (st.mode === 'cards' || st.mode === 'book') break; } }
          await sleep(300);
          rec.lesson = await turn(pg.page);
          if (withEx) {
            rec.hasExerciseTab = await selectTab(pg.page, 'exercise');
            rec.exercise = await turn(pg.page);
            rec.exercise.ans = await pg.page.evaluate(() => document.querySelectorAll('#subjTabContent .sb-ans').length);
          }
        } catch (e) { rec.error = String(e.message).slice(0, 120); }
        total++;
        const probs = (rec.lesson ? rec.lesson.issues.length : 0) + (rec.exercise ? rec.exercise.issues.length : 0) + (rec.error ? 1 : 0) + (rec.lesson && rec.lesson.pages < 1 ? 1 : 0);
        if (probs) bad++;
        console.log((probs ? 'PROBLEM ' : 'ok      ') + cl.id + ' ' + s.id + ' ch' + ci + ' pages ' + (rec.lesson ? rec.lesson.pages + '/' + rec.lesson.mode : '-') + (rec.exercise ? ' ex ' + rec.exercise.pages + ' ans ' + rec.exercise.ans : '') + (probs ? '  ' + JSON.stringify((rec.lesson && rec.lesson.issues.slice(0, 2)) || rec.error) : ''));
        if (out) fs.appendFileSync(out, JSON.stringify(rec) + '\n');
      }
      await pg.ctx.close();
    }
  }
  console.log(`\n${total} chapters, ${bad} with a problem`);
  await browser.close(); server.close();
})();
