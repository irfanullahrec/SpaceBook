'use strict';
/* CPU-only performance report for the budgets of Phase 11 (docs/PERFORMANCE.md), measured in the app sandbox on the lazy page.
 *   node --max-old-space-size=8192 tools/perf_report.js [--json out.json] [--only cls9,cls12-phy]
 * What it measures, for every subject: opening it cold (the first open also loads its book files), selecting every chapter, and switching
 * to every tab; for each, the milliseconds spent in the app's own code and the size of the HTML it produced. It does NOT measure what a
 * browser spends on style, layout, paint or the network: those need a real device (Lighthouse, Chrome's CPU throttling). A number from here
 * is a floor for a desktop, not a promise for a phone. Dev-only. */
const fs = require('fs'), path = require('path');
const { load, ROOT } = require('./lib/app_sandbox');
const args = process.argv.slice(2);
const opt = k => { const i = args.indexOf('--' + k); return i < 0 ? null : args[i + 1]; };
const ONLY = opt('only') ? opt('only').split(',') : null;

const t00 = process.hrtime.bigint();
const app = load({ page: 'lazy.html', quiet: true });
const loadMs = Number(process.hrtime.bigint() - t00) / 1e6;
const heapAtLoad = process.memoryUsage().heapUsed / 1048576;
const subjects = app.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name })))')
  .filter(s => !ONLY || ONLY.includes(s.classId) || ONLY.includes(s.id));

const VIEWS = {
  generic: { area: 'subjectTopicArea', content: 'subjTabContent', chapter: 'select\\w*(?:Chapter|Unit|Lesson|Page)', tab: 'switchSubjectTab', reset: 'state.activeSubjTab = null; ' },
  math: { area: 'mathTopicArea', content: 'mathTabContent', chapter: 'selectMathChapter', tab: 'switchMathTab', reset: '' },
};
const unesc = oc => oc.replace(/&#39;|&quot;/g, "'");
const now = () => Number(process.hrtime.bigint()) / 1e6;
const open = [], chapter = [], tab = [];            // {ms, kb, where}

for (const s of subjects) {
  const step = code => { try { return app.run(code, 120000); } catch (e) { return null; } };
  const t0 = now();
  step(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`);
  const body = step(`document.getElementById('dashboard-body').innerHTML`) || '';
  open.push({ ms: now() - t0, kb: body.length / 1024, where: s.id });
  const V = body.includes('id="mathTopicArea"') ? VIEWS.math : VIEWS.generic;
  const chs = [...new Set([...body.matchAll(new RegExp('onclick="(' + V.chapter + '\\([^"]*)"', 'g'))].map(m => m[1]))];
  chs.forEach((oc, i) => {
    const t1 = now();
    step(`${V.reset}${unesc(oc)}`);
    const dt = now() - t1;
    const area = step(`document.getElementById('${V.area}').innerHTML`) || '';
    chapter.push({ ms: dt, kb: area.length / 1024, where: `${s.id} ch${i}` });
    const tabOcs = [...new Set([...area.matchAll(new RegExp('onclick="(' + V.tab + '\\([^"]*)"', 'g'))].map(m => m[1]))];
    for (const t of tabOcs) {
      step(`document.getElementById('${V.content}').innerHTML = ''`);
      const t2 = now();
      step(unesc(t));
      const d2 = now() - t2;
      const html = step(`document.getElementById('${V.content}').innerHTML`) || '';
      tab.push({ ms: d2, kb: html.length / 1024, where: `${s.id} ch${i} ${(t.match(/'([a-z0-9-]+)'/g) || []).slice(0, 2).join(' ').replace(/'/g, '')}` });
    }
  });
}

const pct = (list, p, key = 'ms') => { const a = list.map(x => x[key]).sort((x, y) => x - y); return a.length ? a[Math.min(a.length - 1, Math.floor(a.length * p))] : 0; };
const f = (n, d = 0) => n.toFixed(d);
const row = (name, list) => `${name.padEnd(22)} n=${String(list.length).padStart(5)}  ms p50 ${f(pct(list, 0.5), 1).padStart(7)}  p95 ${f(pct(list, 0.95), 1).padStart(7)}  max ${f(Math.max(0, ...list.map(x => x.ms)), 0).padStart(6)}   html KB p50 ${f(pct(list, 0.5, 'kb')).padStart(5)}  p95 ${f(pct(list, 0.95, 'kb')).padStart(6)}  max ${f(Math.max(0, ...list.map(x => x.kb))).padStart(6)}`;
const out = [];
out.push(`page ready (lazy.html, sandbox): ${f(loadMs)} ms, heap ${f(heapAtLoad)} MB`);
out.push(row('open a subject (cold)', open));
out.push(row('select a chapter', chapter));
out.push(row('switch to a tab', tab));
const over = (list, kb) => list.filter(x => x.kb > kb).length;
out.push(`tabs over 500 KB: ${over(tab, 500)}, over 2 MB: ${over(tab, 2048)}, over 5 MB: ${over(tab, 5120)}; chapters over 300 ms: ${chapter.filter(x => x.ms > 300).length}; tabs over 150 ms: ${tab.filter(x => x.ms > 150).length}, over 600 ms: ${tab.filter(x => x.ms > 600).length}`);
out.push('heaviest tabs by HTML:');
tab.slice().sort((a, b) => b.kb - a.kb).slice(0, 12).forEach(x => out.push(`  ${f(x.kb / 1024, 1).padStart(6)} MB ${f(x.ms).padStart(6)} ms  ${x.where}`));
out.push('slowest tabs:');
tab.slice().sort((a, b) => b.ms - a.ms).slice(0, 8).forEach(x => out.push(`  ${f(x.ms).padStart(6)} ms ${f(x.kb / 1024, 1).padStart(6)} MB  ${x.where}`));
out.push('slowest chapters:');
chapter.slice().sort((a, b) => b.ms - a.ms).slice(0, 5).forEach(x => out.push(`  ${f(x.ms).padStart(6)} ms  ${x.where}`));
out.push('slowest cold opens:');
open.slice().sort((a, b) => b.ms - a.ms).slice(0, 5).forEach(x => out.push(`  ${f(x.ms).padStart(6)} ms  ${x.where}`));
if (app.sb.SBLazy) { const st = app.sb.SBLazy.stats(); out.push(`lazy files loaded by the end: ${st.loaded} of ${st.files}`); }
console.log(out.join('\n'));
if (opt('json')) fs.writeFileSync(path.resolve(ROOT, opt('json')), JSON.stringify({ loadMs, heapAtLoad, open, chapter, tab }));
