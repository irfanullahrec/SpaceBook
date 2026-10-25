'use strict';
/* Every kind of "Ans" / "جواب" of Classes 1-12, in the Android app's reader (phone-sized Chrome, the app's own reader_mobile.css and reader_bridge.js
 * put on the website, the way the app's WebView does) or on a wide screen. For each chapter a handful of Ans buttons of the Lessons and the Exercises tab
 * are pressed (the first, the last, evenly spread ones, and up to three whose question has a dash) and what happened is classified:
 *     filled  the answer was written into the dash of the question (js/sb_solve.js)
 *     box     a small answer box opened under the question
 *     modal   a maths solution opened the answer window
 *     none    nothing opened                         <- a problem
 * Problems reported: nothing opened, an empty box, a dash of the question still empty after a plain answer opened, a window for an answer without steps,
 * a window or box that stays open after the second press, a script error.
 *     node --max-old-space-size=3072 tests/parity/ans_everywhere.js [--classes 1,12] [--only <subject id part>] [--every 3] [--max 8]
 *          [--wide] [--out report.jsonl] [--app "<app repo>"]
 * --every N looks at the first two chapters, the last, and every Nth of each subject (1 = all). Dev-only, takes long (a class is minutes to an hour). */
const fs = require('fs'), path = require('path');
const { serve, launch } = require('../baseline/lib');

const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const APP = path.resolve(opt('--app', path.join(ROOT, '..', 'SpaceBook App')));
const ASSETS = path.join(APP, 'app', 'src', 'main', 'assets') + path.sep;
const wide = args.includes('--wide');
if (!wide && !fs.existsSync(ASSETS + 'reader_bridge.js')) { console.log('SKIP  the app folder is not here (' + ASSETS + ')'); process.exit(0); }
const classes = opt('--classes', '1,2,3,4,5,6,7,8,9,10,11,12').split(',').map(x => 'cls' + x.trim());
const only = opt('--only', null), every = +opt('--every', 3), MAX = +opt('--max', 8), out = opt('--out', null);
const sleep = ms => new Promise(r => setTimeout(r, ms));
const catalog = JSON.parse(fs.readFileSync(ASSETS + 'app_catalog.json', 'utf8'));

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const css = wide ? '' : fs.readFileSync(ASSETS + 'reader_mobile.css', 'utf8'), bridge = wide ? '' : fs.readFileSync(ASSETS + 'reader_bridge.js', 'utf8');
  let errors = [];
  const newPage = async () => {
    const ctx = await browser.newContext(wide ? { viewport: { width: 1360, height: 900 } }
      : { viewport: { width: 411, height: 900 }, hasTouch: true, isMobile: true, userAgent: 'Mozilla/5.0 (Linux; Android 14; Pixel) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36' });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(String(e.message).slice(0, 140)));
    for (let attempt = 0; attempt < 3; attempt++) {
      await page.goto(url + 'index.html', { waitUntil: 'domcontentloaded', timeout: 180000 });
      for (let k = 0; k < 4; k++) {
        try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 }); await sleep(2500); if (await page.evaluate(() => typeof openSubject === 'function')) break; } catch (e) { /* reloaded */ }
      }
      if (wide) return { ctx, page };
      await page.evaluate(() => { document.documentElement.classList.add('sbapp'); window.SBHost = { onReady() { }, onState() { }, onAction() { } }; });
      await page.addStyleTag({ content: css });
      await page.addScriptTag({ content: bridge });
      if (await page.waitForFunction(() => window.SBApp && typeof window.SBApp.open === 'function', null, { timeout: 20000 }).then(() => true, () => false)) return { ctx, page };
    }
    return null;
  };
  const selectTab = async (page, id) => {
    const on = await page.evaluate(i => { const b = document.querySelector('.math-nav-tabs [data-tab="' + i + '"], .math-top-tab[data-tab="' + i + '"], .math-tab-btn[data-tab="' + i + '"]'); if (!b) return 'none'; if (b.classList.contains('active')) return 'already'; b.click(); return 'clicked'; }, id);
    if (on === 'clicked') await sleep(wide ? 2200 : 1500);
    return on;
  };
  // press some of the Ans buttons of the open tab and say what each did
  const probe = (page, max) => page.evaluate(async max => {
    const BL = /_{3,}|\.{4,}|…+|-{3,}|[—–]{2,}/;
    const root = document.getElementById('subjTabContent') || document.getElementById('mathTabContent') || document.body;
    const all = [...root.querySelectorAll('.sb-ans')];
    const hostOf = b => b.closest('[class~="m6-s"]') || b.parentElement;
    const ownText = b => { const c = hostOf(b).cloneNode(true); c.querySelectorAll('button,.sb-solve,[class*="-tr"],.sbs-fill').forEach(n => n.remove()); return c.textContent; };
    // the first, the last, evenly spread ones, and up to three with a dash
    const pick = new Set([0, all.length - 1]);
    for (let i = 1; i < max - 3 && all.length > 1; i++) pick.add(Math.round(i * (all.length - 1) / (max - 3)));
    let d = 0; all.forEach((b, i) => { if (d < 3 && BL.test(ownText(b))) { pick.add(i); d++; } });
    const wait = ms => new Promise(r => setTimeout(r, ms));
    const res = { ans: all.length, tested: 0, kinds: { filled: 0, box: 0, modal: 0, none: 0 }, problems: [] };
    for (const i of [...pick].filter(i => i >= 0 && i < all.length).sort((a, b) => a - b)) {
      const b = all[i]; if (!b.isConnected) continue;
      const dashBefore = BL.test(ownText(b));
      b.click(); await wait(350);
      res.tested++;
      const modal = document.querySelector('.bk-modal');
      const fills = (b._fills || []).length;
      const panel = b._panel && b._panel.classList && b._panel.classList.contains('sb-solve') ? b._panel : null;   // the button is moved next to the speaker icon; its panel stays where it was
      const boxOpen = panel && !panel.hidden && panel.classList.contains('sbs-inline');
      const txt = boxOpen ? (panel.textContent || '').replace(/\s+/g, ' ').trim() : '';
      let kind = 'none';
      if (modal) kind = 'modal'; else if (fills) kind = 'filled'; else if (boxOpen) kind = 'box';
      res.kinds[kind]++;
      const where = (ownText(b) || '').replace(/\s+/g, ' ').trim().slice(0, 50);
      if (kind === 'none') res.problems.push({ i, why: 'nothing opened', where });
      if (kind === 'box' && txt.length < 3) res.problems.push({ i, why: 'empty box', where });
      if (kind === 'box' && dashBefore && !BL.test('')) res.problems.push({ i, why: 'dash left empty (answer shown below)', where });
      if (kind === 'modal' && !modal.querySelector('.sbs-step')) res.problems.push({ i, why: 'window without steps', where });
      if (kind === 'filled' && BL.test(ownText(b))) res.problems.push({ i, why: 'a dash of the question is still empty', where });
      // press again / close, and see that everything is closed
      if (modal) { const x = modal.querySelector('.bk-modal-x'); if (x) x.click(); } else b.click();
      await wait(250);
      if (document.querySelector('.bk-modal')) res.problems.push({ i, why: 'window stays open', where });
      else if (kind !== 'none' && b.getAttribute('aria-expanded') === 'true') res.problems.push({ i, why: 'button stays open', where });
      else if (kind === 'filled' && document.querySelectorAll('.sbs-fill').length) { document.querySelectorAll('.sbs-fill').forEach(s => s.replaceWith(document.createTextNode(s.dataset.blank || '____'))); res.problems.push({ i, why: 'dash not restored', where }); }
    }
    return res;
  }, max);

  let total = 0, bad = 0, ansTotal = 0;
  const tot = { filled: 0, box: 0, modal: 0, none: 0 };
  for (const cl of catalog.classes) {
    if (!classes.includes(cl.id)) continue;
    for (const s of cl.subjects) {
      if (only && !s.id.includes(only)) continue;
      const pg = await newPage();
      if (!pg) { console.log(JSON.stringify({ cls: cl.id, subject: s.id, error: 'page did not start' })); continue; }
      const n = s.chapters.length;
      for (let ci = 0; ci < n; ci++) {
        if (!(ci < 2 || ci === n - 1 || ci % every === 0)) continue;
        const rec = { cls: cl.id, subject: s.id, chapter: ci, title: String(s.chapters[ci].t || '').slice(0, 40), tabs: {} };
        errors = [];
        try {
          if (wide) {
            await pg.page.evaluate(([c, id]) => window.openSubject(c, id), [cl.id, s.id]); await sleep(1800);
            await pg.page.evaluate(call => { (0, eval)(call); }, s.chapters[ci].o); await sleep(3000);
          } else {
            const before = await pg.page.evaluate(() => (window.SBApp.state() || {}).title);
            await pg.page.evaluate(([c, sid, call]) => window.SBApp.open(c, sid, call, 0, 'Lessons'), [cl.id, s.id, s.chapters[ci].o]);
            for (let k = 0; k < 20; k++) { await sleep(450); const st = await pg.page.evaluate(() => window.SBApp.state()); if (st && st.ready && (st.mode === 'cards' || st.mode === 'book') && st.pages >= 1 && (st.title !== before || ci === 0) && k >= 2) break; }
          }
          // every tab of the chapter (the books name them differently: lesson, exercise, practice, summary ...); the open one first
          const tabs = await pg.page.evaluate(() => { const seen = []; document.querySelectorAll('.math-nav-tabs [data-tab], .math-top-tab[data-tab], .math-tab-btn[data-tab]').forEach(b => { if (b.dataset.tab && !seen.includes(b.dataset.tab) && b.getBoundingClientRect().width > 0) seen.push(b.dataset.tab); }); return seen; });
          if (!tabs.length) { rec.tabs.page = await probe(pg.page, MAX); }
          for (const tab of tabs.slice(0, 8)) {
            await selectTab(pg.page, tab);
            await sleep(500);
            rec.tabs[tab] = await probe(pg.page, MAX);
          }
        } catch (e) { rec.error = String(e.message).slice(0, 140); }
        rec.errors = errors.slice(0, 3);
        total++;
        let probs = (rec.error ? 1 : 0) + rec.errors.length;
        for (const t of Object.values(rec.tabs)) { probs += t.problems.length; ansTotal += t.tested; for (const k of Object.keys(tot)) tot[k] += t.kinds[k]; }
        if (probs) bad++;
        const sum = Object.entries(rec.tabs).map(([k, t]) => `${k}:${t.tested}/${t.ans}`).join(' ');
        const firstProb = Object.values(rec.tabs).flatMap(t => t.problems)[0];
        console.log((probs ? 'PROBLEM ' : 'ok      ') + cl.id + ' ' + s.id + ' ch' + ci + ' ' + sum + (probs ? '  ' + JSON.stringify(firstProb || rec.error || rec.errors[0]) : ''));
        if (out) fs.appendFileSync(out, JSON.stringify(rec) + '\n');
      }
      await pg.ctx.close();
    }
  }
  console.log(`\n${total} chapters, ${bad} with a problem; ${ansTotal} Ans pressed: ${JSON.stringify(tot)}`);
  await browser.close(); server.close();
})().catch(e => { console.error(e); process.exit(1); });
