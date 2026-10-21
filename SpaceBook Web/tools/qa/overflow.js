'use strict';
/* Class 11/12 layout check: sideways overflow at 1280 / 768 / 375 px for every subject; chapters = first, middle, last (or --all).
 *   node tools/qa/overflow.js [--out file.json] [--only cls11,cls12-phy] [--all]
 * Page overflow = documentElement.scrollWidth > viewport; "wide" = elements whose box leaves the viewport and that are not inside a scroll container. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, "..", ".."); const { serve, launch } = require(path.join(ROOT, "tests", "baseline", "lib"));
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf('--' + k); return i < 0 ? d : (args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true); };
const ONLY = opt('only', 'cls11,cls12').split(',');
const ALL = !!opt('all', false);
const OUT = path.resolve(opt('out', path.join(ROOT, 'docs', 'qa_overflow.json')));
const WIDTHS = [[1280, 800], [768, 1024], [375, 812]];
const SETTLE = `window.__s=(q=150,m=4000)=>new Promise(r=>{let l=performance.now();const t=l;const mo=new MutationObserver(()=>{l=performance.now()});mo.observe(document.body,{subtree:true,childList:true,characterData:true,attributes:true});(function k(){const n=performance.now();if(n-l>=q||n-t>=m){mo.disconnect();r(1)}else setTimeout(k,25)})()})`;
const MEASURE = () => {
  const vw = document.documentElement.clientWidth, body = document.getElementById('dashboard-body') || document.body;
  const page = document.documentElement.scrollWidth - vw;
  const wide = [];
  for (const e of body.querySelectorAll('*')) {
    if (!(e.offsetWidth || e.offsetHeight)) continue;
    const r = e.getBoundingClientRect();
    if (r.width < 2 || r.right <= vw + 2) continue;
    let p = e.parentElement, inScroll = false;
    while (p && p !== document.body) { const o = getComputedStyle(p).overflowX; if ((o === 'auto' || o === 'scroll' || o === 'hidden') && p.getBoundingClientRect().right <= vw + 2) { inScroll = true; break; } p = p.parentElement; }
    if (inScroll) continue;
    if (wide.length < 4) wide.push(e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).slice(0, 2).join('.') : '') + ' +' + Math.round(r.right - vw));
  }
  // elements that scroll sideways inside the page (tables / pre / svg wrappers)
  let scrollers = 0;
  for (const e of body.querySelectorAll('*')) if ((e.offsetWidth) && e.scrollWidth > e.clientWidth + 2 && ['auto', 'scroll'].includes(getComputedStyle(e).overflowX)) scrollers++;
  return { vw, page, wide, scrollers };
};
(async () => {
  const { server, url } = await serve(); const browser = await launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  await page.goto(url + 'lazy.html', { waitUntil: 'domcontentloaded', timeout: 600000 });
  await page.waitForFunction(() => typeof openSubject === 'function' && typeof DATA !== 'undefined', null, { timeout: 600000 });
  await page.waitForTimeout(5000); // the page reloads once when the service worker takes control
  await page.waitForFunction(() => typeof openSubject === 'function' && typeof DATA !== 'undefined', null, { timeout: 600000 });
  await page.evaluate(SETTLE); await page.evaluate(() => window.__s(300, 15000));
  const subjects = (await page.evaluate(() => DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name }))))).filter(s => ONLY.some(o => s.classId === o || s.id === o || s.classId + '-' + s.id === o));
  console.log(subjects.length, 'subjects');
  const res = [];
  for (const s of subjects) {
    const rec = { classId: s.classId, id: s.id, name: s.name, checks: 0, bad: [] };
    try {
      await page.setViewportSize({ width: 1280, height: 800 });
      await page.evaluate(([c, i]) => { window.scrollTo(0, 0); openSubject(c, i); }, [s.classId, s.id]); await page.evaluate(() => window.__s());
      const chapters = await page.evaluate(() => { const b = document.getElementById('dashboard-body'); const seen = new Set(), out = []; for (const e of b.querySelectorAll('[onclick]')) { const oc = e.getAttribute('onclick'); if (!/select\w*(Chapter|Unit|Lesson|Page)\s*\(/.test(oc) || seen.has(oc)) continue; seen.add(oc); out.push({ oc, label: e.innerText.replace(/\s+/g, ' ').trim().slice(0, 50) }); } return out; });
      rec.chapters = chapters.length;
      const idx = ALL ? chapters.map((_, i) => i) : [...new Set([0, Math.floor((chapters.length - 1) / 2), chapters.length - 1])].filter(i => i >= 0);
      const targets = idx.length ? idx : [-1];
      for (const i of targets) {
        if (i >= 0) { await page.setViewportSize({ width: 1280, height: 800 }); await page.evaluate(oc => { new Function(oc).call(document.body); }, chapters[i].oc).catch(() => { }); await page.evaluate(() => window.__s()); }
        const tabs = await page.evaluate(() => [...document.querySelectorAll('#dashboard-body [data-tab]')].map((e, k) => ({ k, id: e.getAttribute('data-tab'), vis: !!(e.offsetWidth || e.offsetHeight) })).filter(t => t.vis));
        for (const t of (tabs.length ? tabs : [null])) {
          if (t) { await page.setViewportSize({ width: 1280, height: 800 }); await page.evaluate(sel => { const el = document.querySelectorAll('#dashboard-body [data-tab]')[sel.k]; if (el && el.getAttribute('data-tab') === sel.id) el.click(); }, t); await page.evaluate(() => window.__s()); }
          for (const [w, h] of WIDTHS) {
            await page.setViewportSize({ width: w, height: h }); await page.evaluate(() => window.__s(100, 1500));
            const m = await page.evaluate(MEASURE); rec.checks++;
            if (m.page > 2 || m.wide.length) rec.bad.push({ ch: i >= 0 ? chapters[i].label : '(landing)', tab: t ? t.id : '-', w, page: m.page, wide: m.wide });
          }
        }
      }
    } catch (e) { rec.fatal = String(e.message).slice(0, 200); }
    console.log(s.classId, s.id, rec.chapters, 'checks', rec.checks, 'bad', rec.bad.length, rec.fatal || '');
    res.push(rec); fs.writeFileSync(OUT, JSON.stringify(res, null, 1));
  }
  await browser.close(); server.close();
})().catch(e => { console.error(e); process.exit(2); });
