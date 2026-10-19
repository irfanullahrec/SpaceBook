'use strict';
/* Browser baseline: for every class x subject x chapter x visible main tab, records the tab labels in order, a
 * hash of the rendered text, console errors and render time; screenshots of the first, middle and last chapter
 * at 1280x800 and 375x812.
 *
 *   node tests/baseline/run.js [--out tests/baseline/2026-10-19] [--only cls9,cls12-phy] [--subset] [--workers 1]
 *        [--no-shots]
 *   --subset  first chapter of each subject only (CI gate)
 * Output: <out>/<classId>/<subjectId>.json, <out>/summary.json, <out>/shots/*.png (screenshots are gitignored).
 * Compare two runs with tests/baseline/compare.js. Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { serve, launch, ROOT } = require('./lib');

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf('--' + k); return i < 0 ? d : (args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true); };
const today = new Date().toISOString().slice(0, 10);
const OUT = path.resolve(ROOT, opt('out', path.join('tests', 'baseline', today)));
const ONLY = opt('only', '') ? String(opt('only')).split(',') : null;
const SUBSET = !!opt('subset', false);
const SHOTS = !opt('no-shots', false) && !SUBSET;
const WORKERS = +opt('workers', 1); // each page holds ~0.7 GB of app heap: more workers need more RAM
const sha = s => crypto.createHash('sha256').update(s).digest('hex').slice(0, 16);

// runs in the page: wait until the DOM has been quiet for `quiet` ms (MutationObservers in add-ons post-process
// asynchronously), at most `max` ms
const SETTLE = `window.__sbSettle = (quiet = 150, max = 4000) => new Promise(res => {
  let last = performance.now(); const t0 = last;
  const mo = new MutationObserver(() => { last = performance.now(); });
  mo.observe(document.body, { subtree: true, childList: true, characterData: true, attributes: true });
  (function tick() {
    const now = performance.now();
    if (now - last >= quiet || now - t0 >= max) { mo.disconnect(); res(Math.round(now - t0)); }
    else setTimeout(tick, 25);
  })();
});`;

async function openApp(browser, url) {
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  page.__errors = [];
  page.on('pageerror', e => page.__errors.push('pageerror: ' + e.message.slice(0, 300)));
  page.on('console', m => { if (m.type() === 'error') page.__errors.push('console: ' + m.text().slice(0, 300)); });
  // 'load' also waits for media; the app is usable once its scripts have run
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 600000 });
  await page.waitForFunction(() => typeof openSubject === 'function' && window.DATA, null, { timeout: 600000 });
  await page.evaluate(SETTLE);
  await page.evaluate(() => window.__sbSettle(300, 15000));
  return page;
}

const takeErrors = page => page.__errors.splice(0);

async function textOf(page) {
  return page.evaluate(() => {
    const b = document.getElementById('dashboard-body');
    return b ? b.innerText.replace(/\s+/g, ' ').trim() : '';
  });
}

async function shot(page, file) {
  if (!SHOTS) return;
  fs.mkdirSync(path.dirname(file), { recursive: true });
  for (const [w, h, tag] of [[1280, 800, 'desktop'], [375, 812, 'mobile']]) {
    await page.setViewportSize({ width: w, height: h });
    await page.evaluate(() => window.__sbSettle(100, 1500));
    await page.screenshot({ path: file.replace(/\.png$/, '.' + tag + '.png') });
  }
  await page.setViewportSize({ width: 1280, height: 800 });
}

async function runSubject(page, classId, subj) {
  const rec = { classId, subjectId: subj.id, name: subj.name, chapters: [], errors: [] };
  const t0 = Date.now();
  await page.evaluate(([c, s]) => { window.scrollTo(0, 0); openSubject(c, s); }, [classId, subj.id]).catch(e => rec.errors.push('openSubject: ' + e.message.slice(0, 300)));
  rec.openMs = (Date.now() - t0) + await page.evaluate(() => window.__sbSettle());
  rec.errors.push(...takeErrors(page));
  // chapter buttons: distinct onclick handlers that select a chapter/unit/lesson
  const chapters = await page.evaluate(() => {
    const b = document.getElementById('dashboard-body'); if (!b) return [];
    const seen = new Set(), out = [];
    for (const e of b.querySelectorAll('[onclick]')) {
      const oc = e.getAttribute('onclick');
      if (!/select\w*(Chapter|Unit|Lesson|Page)\s*\(/.test(oc) || seen.has(oc)) continue;
      seen.add(oc); out.push({ onclick: oc, label: e.innerText.replace(/\s+/g, ' ').trim().slice(0, 80) });
    }
    return out;
  });
  rec.chapterCount = chapters.length;
  const picks = SUBSET ? [0] : chapters.map((_, i) => i);
  const shotIdx = new Set([0, Math.floor((chapters.length - 1) / 2), chapters.length - 1]);
  if (!chapters.length) {
    rec.landing = { hash: sha(await textOf(page)), tabs: await mainTabs(page) };
    await shot(page, path.join(OUT, 'shots', classId, subj.id + '.landing.png'));
  }
  for (const i of picks) {
    const ch = chapters[i]; if (!ch) continue;
    const c = { idx: i, label: ch.label, tabs: [] };
    const t1 = Date.now();
    await page.evaluate(oc => { new Function(oc).call(document.body); }, ch.onclick).catch(e => c.error = e.message.slice(0, 300));
    c.ms = (Date.now() - t1) + await page.evaluate(() => window.__sbSettle());
    c.errors = takeErrors(page);
    const tabs = await mainTabs(page);
    c.tabLabels = tabs.map(t => t.label);
    if (shotIdx.has(i)) await shot(page, path.join(OUT, 'shots', classId, subj.id + '.ch' + String(i).padStart(2, '0') + '.png'));
    for (const t of tabs) {
      const t2 = Date.now();
      const clicked = await page.evaluate(sel => {
        const el = document.querySelectorAll('#dashboard-body [data-tab]')[sel.i];
        if (!el || el.getAttribute('data-tab') !== sel.id) return false;
        el.click(); return true;
      }, t).catch(() => false);
      const settle = await page.evaluate(() => window.__sbSettle());
      const text = await textOf(page);
      c.tabs.push({ id: t.id, label: t.label, clicked, ms: (Date.now() - t2), settleMs: settle, len: text.length, hash: sha(text), errors: takeErrors(page) });
    }
    rec.chapters.push(c);
  }
  return rec;
}

function mainTabs(page) {
  return page.evaluate(() => [...document.querySelectorAll('#dashboard-body [data-tab]')]
    .map((e, i) => ({ i, id: e.getAttribute('data-tab'), label: e.innerText.replace(/\s+/g, ' ').trim().slice(0, 60), visible: !!(e.offsetWidth || e.offsetHeight) }))
    .filter(t => t.visible));
}

(async () => {
  const { server, url } = await serve();
  const browser = await launch();
  const probe = await openApp(browser, url);
  const subjects = await probe.evaluate(() => DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name }))));
  await probe.close();
  const todo = subjects.filter(s => !ONLY || ONLY.includes(s.classId) || ONLY.includes(s.id));
  console.log('baseline -> ' + path.relative(ROOT, OUT) + ': ' + todo.length + ' subjects, ' + WORKERS + ' workers' + (SUBSET ? ', subset' : ''));
  fs.mkdirSync(OUT, { recursive: true });
  const results = [], started = Date.now();
  let next = 0;
  async function worker(w) {
    let page = await openApp(browser, url);
    while (next < todo.length) {
      const s = todo[next++];
      let rec;
      try { rec = await runSubject(page, s.classId, s); }
      catch (e) {
        rec = { classId: s.classId, subjectId: s.id, name: s.name, fatal: e.message.slice(0, 500) };
        await page.close().catch(() => { }); page = await openApp(browser, url); // fresh page after a crash
      }
      fs.mkdirSync(path.join(OUT, s.classId), { recursive: true });
      fs.writeFileSync(path.join(OUT, s.classId, s.id + '.json'), JSON.stringify(rec, null, 1) + '\n');
      const nt = (rec.chapters || []).reduce((n, c) => n + c.tabs.length, 0);
      const ne = (rec.errors || []).length + (rec.chapters || []).reduce((n, c) => n + (c.errors || []).length + c.tabs.reduce((m, t) => m + t.errors.length, 0), 0);
      results.push({ classId: s.classId, subjectId: s.id, chapters: rec.chapterCount || 0, tabRenders: nt, errors: ne, openMs: rec.openMs, fatal: rec.fatal });
      console.log(`[w${w}] ${results.length}/${todo.length} ${s.classId}/${s.id}: ${rec.chapterCount || 0} ch, ${nt} tab renders, ${ne} errors, open ${rec.openMs} ms${rec.fatal ? ' FATAL ' + rec.fatal : ''}`);
    }
    await page.close();
  }
  // stagger the workers: several pages parsing 358 MB of scripts at once starve each other
  await Promise.all(Array.from({ length: Math.min(WORKERS, todo.length) }, (_, i) => new Promise(r => setTimeout(r, i * 45000)).then(() => worker(i + 1))));
  results.sort((a, b) => (a.classId + a.subjectId).localeCompare(b.classId + b.subjectId));
  const summary = { generated: new Date().toISOString(), subset: SUBSET, minutes: +((Date.now() - started) / 60000).toFixed(1), subjects: results.length,
    chapters: results.reduce((n, r) => n + r.chapters, 0), tabRenders: results.reduce((n, r) => n + r.tabRenders, 0),
    errors: results.reduce((n, r) => n + r.errors, 0), fatal: results.filter(r => r.fatal).length, results };
  fs.writeFileSync(path.join(OUT, 'summary.json'), JSON.stringify(summary, null, 1) + '\n');
  console.log(`done in ${summary.minutes} min: ${summary.subjects} subjects, ${summary.chapters} chapters, ${summary.tabRenders} tab renders, ${summary.errors} errors, ${summary.fatal} fatal`);
  await browser.close(); server.close();
  process.exit(summary.fatal ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
