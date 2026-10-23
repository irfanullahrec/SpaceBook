'use strict';
/* Every hand-written solution pack: builds its spec and renders every written row with KaTeX (throwOnError); lists the failures.   node tools/vr/validate_packs.js */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
global.window = global;
const katex = require(path.join(ROOT, 'assets', 'vendor', 'katex', 'katex.min.js'));
const cw = console.warn; console.warn = () => {};
require(path.join(ROOT, 'js', 'vr_viz.js')); require(path.join(ROOT, 'js', 'vr_auto.js'));
fs.readdirSync(path.join(ROOT, 'js')).filter(f => /^sol_.*\.js$/.test(f)).sort((a, b) => (/^sol_m\d/.test(a) ? 1 : 0) - (/^sol_m\d/.test(b) ? 1 : 0) || a.localeCompare(b)).forEach(f => require(path.join(ROOT, 'js', f)));
console.warn = cw;
const NS = global.SBVR, packs = NS.sol.all(); let bad = 0, rows = 0, noSpec = 0; const msgs = [];
const render = t => katex.renderToString(t, { trust: true, throwOnError: true, strict: 'ignore', output: 'html' });
packs.forEach(p => {
  const r = NS.autoSpec(p.steps, { board: p.board, question: p.q, maxSteps: 80 }); if (!r.spec) { noSpec++; msgs.push('NO-SPEC ' + p.q.slice(0, 70)); return; }
  r.spec.rows.forEach(row => { Object.values(row.tex || {}).forEach(t => { if (!t) return; rows++; try { render(t); } catch (e) { bad++; if (msgs.length < 25) msgs.push('TEX ' + p.q.slice(0, 50) + ' :: ' + t.slice(0, 80) + ' :: ' + String(e.message).slice(0, 80)); } }); });
});
console.log('packs', packs.length, '| rows rendered', rows, '| tex errors', bad, '| without spec', noSpec); msgs.forEach(m => console.log('  ', m));
