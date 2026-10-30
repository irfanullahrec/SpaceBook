'use strict';
/* No blank page in any book (owner, 2026-10-29: "there are some blank pages in each subject, please do not keep a blank page").
 * In a real Chrome at a wide width (the open book: facing pages) it opens chapters of every subject of the app catalog (content/app_catalog.json: the same call the app uses
 * for each chapter) on the Lesson tab and on the Exercise tab and counts, in the pages drawn by js/sb_book_spread.js:
 *   - a blank half: a page drawn beside an empty one (class bk-blank)
 *   - an empty page: a page with nothing on it but its number
 * Both must be zero. A page whose partner is not in the book is drawn on its own (class bk-lone), which is fine and is reported as a count.
 *     node --max-old-space-size=3072 tests/launch/blank_pages.js [--sample N] [--all] [--only cls11-eng,cls9-bio] [--from cls10-chem]
 * Default: the first, a middle and the last chapter of every subject (--sample 3); --all: every chapter (about 1,850; an hour). Dev-only, never deployed. */
const fs = require('fs'), path = require('path');
const { serve, launch, ROOT } = require('../baseline/lib');
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const ALL = args.includes('--all'), ONLY = opt('--only') ? opt('--only').split(',') : null, FROM = opt('--from') || '';
const SAMPLE = +(opt('--sample') || 3);
const sleep = ms => new Promise(r => setTimeout(r, ms));
let pass = 0, fail = 0;
const check = (n, ok, d) => { if (ok) pass++; else { fail++; console.log('FAIL  ' + n + (d !== undefined ? '  -> ' + JSON.stringify(d).slice(0, 300) : '')); } };

(async () => {
  const cat = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));
  let picks = [];
  for (const c of cat.classes) for (const s of c.subjects) {
    const n = s.chapters.length; if (!n) continue;
    const idx = ALL ? s.chapters.map((_, i) => i) : [...new Set([0, Math.floor(n / 2), n - 1].slice(0, Math.max(1, SAMPLE)))];
    picks.push({ cls: c.id, id: s.id, name: s.name, chapters: idx.map(i => ({ i, call: s.chapters[i].o, title: s.chapters[i].t })) });
  }
  if (ONLY) picks = picks.filter(p => ONLY.includes(p.id));
  if (FROM) { const k = picks.findIndex(p => p.id === FROM); if (k >= 0) picks = picks.slice(k); }
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [], unmeasured = [];            // page script errors; chapters that could not be measured (a timeout or a crash of the page)
  let ctx = null, page = null;
  async function fresh() {
    if (ctx) { try { await ctx.close(); } catch (e) { /* gone */ } }
    ctx = await browser.newContext({ viewport: { width: 1366, height: 800 } });
    page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message.slice(0, 120)));
    if (process.env.SB_OLD_SPREAD) await page.route(/sb_book_spread.js/, r => r.fulfill({ path: process.env.SB_OLD_SPREAD, contentType: 'text/javascript' }));   // prove the check sees the old fault: SB_OLD_SPREAD=<an older copy of js/sb_book_spread.js>
    await page.goto(url + 'lazy.html', { waitUntil: 'domcontentloaded', timeout: 180000 });
    await page.waitForFunction(() => window.SBSpread6 && typeof openSubject === 'function' && typeof renderHome === 'function', null, { timeout: 120000 });
    await sleep(2500);
  }
  await fresh();
  const within = (ms, p) => Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error('timeout ' + ms + ' ms')), ms))]);
  const measure = () => page.evaluate(() => {
    const wraps = [...document.querySelectorAll('#subjTabContent .bk-wrap, #mathTabContent .bk-wrap')];
    let blank = 0, empty = 0, lone = 0;
    wraps.forEach(w => {
      if (w.classList.contains('bk-lone')) lone++;
      w.querySelectorAll('.bk-page').forEach(p => {
        if (p.classList.contains('bk-blank')) blank++;
        else if ((p.textContent || '').replace(/\s+/g, ' ').trim().length < 6 && !p.querySelector('svg,img,canvas,table')) empty++;
      });
    });
    return { spreads: wraps.length, blank, empty, lone };
  });
  let viewed = 0, total = 0;
  for (const p of picks) {
    for (const ch of p.chapters) {
      total++;
      try {
        await within(+(process.env.BP_TIMEOUT || 60000), (async () => {
          await page.evaluate(([c, s]) => { openSubject(c, s); }, [p.cls, p.id]); await sleep(1200);
          await page.evaluate(call => { (0, eval)(call); }, ch.call); await sleep(1800);
          for (const tab of ['lesson', 'exercise']) {
            await page.evaluate(t => { const b = [...document.querySelectorAll('.math-nav-tabs button, .math-top-tab, .math-tab-btn')].find(x => (x.dataset && x.dataset.tab === t) || new RegExp('^\\W*' + t, 'i').test((x.textContent || '').trim())); if (b) b.click(); }, tab);
            await sleep(1500);
            const m = await measure();
            if (m.spreads) viewed++;
            check(p.id + ' ch ' + (ch.i + 1) + ' ' + tab + ': no blank page', m.blank === 0 && m.empty === 0, Object.assign({ title: ch.title }, m));
          }
        })());
      } catch (e) { unmeasured.push({ id: p.id, ch: ch.i + 1, why: String(e.message).slice(0, 70) }); try { await fresh(); } catch (e2) { /* the next one reports */ } }
    }
  }
  await browser.close(); server.close();
  console.log('blank pages: ' + total + ' chapters of ' + picks.length + ' subjects, ' + viewed + ' tab views drawn as an open book; ' + pass + ' ok, ' + fail + ' with a blank page; ' + unmeasured.length + ' chapters could not be measured; ' + [...new Set(errors)].length + ' different page script errors');
  if (unmeasured.length) { console.log('UNMEASURED  ' + unmeasured.map(u => u.id + ' ch ' + u.ch + ' (' + u.why + ')').join('; ')); console.log('RERUN  --only ' + [...new Set(unmeasured.map(u => u.id))].join(',')); }
  [...new Set(errors)].slice(0, 8).forEach(e => console.log('PAGE ERROR  ' + e));
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('crashed ' + (e && e.stack || e)); process.exit(2); });
