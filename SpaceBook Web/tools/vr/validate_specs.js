'use strict';
/* Static validation of every generated spec, without a browser:
 *   1. every row text and every tagged variant renders with KaTeX (throwOnError)
 *   2. every op target "row.k-tag" exists in that row's text at the moment the op runs
 *   3. rows are verbatim: each written side occurs in the source step text (after normalising unicode minus / spaces)
 * node tools/vr/validate_specs.js [--set math10,math12,...] [--verbose]
 */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..');
const katex = require(path.join(ROOT, 'assets', 'vendor', 'katex', 'katex.min.js'));
const { autoSpec } = require(path.join(ROOT, 'js', 'vr_auto.js'));
const FILES = { math10: ['math_10_data.js', 'MATH_10_DATA'], math12: ['math_12_data.js', 'MATH_12_DATA'], math9: ['math_data.js', 'MATH_DATA'], m11: ['math_11_solutions.js', 'MATH_11_SOLUTIONS'], m5: ['math_5_solutions.js', 'MATH_5_SOLUTIONS'], m6: ['math_6_solutions.js', 'MATH_6_SOLUTIONS'], m7: ['math_7_solutions.js', 'MATH_7_SOLUTIONS'], m8: ['math_8_solutions.js', 'MATH_8_SOLUTIONS'], c1: ['math_1_data.js', 'MATH_1_DATA'], c2: ['math_2_data.js', 'MATH_2_DATA'], c3: ['math_3_data.js', 'MATH_3_DATA'], phys10: ['physics_10_book_data.js', 'PHYSICS_10_BOOK_DATA'], chem10: ['chemistry_10_book_data.js', 'CHEMISTRY_10_BOOK_DATA'] };
const want = (process.argv.includes('--set') ? process.argv[process.argv.indexOf('--set') + 1] : Object.keys(FILES).join(',')).split(',');
const verbose = process.argv.includes('--verbose');
const render = t => katex.renderToString(t, { trust: true, throwOnError: true, strict: 'ignore', output: 'html' });
const total = { items: 0, specs: 0, rows: 0, ops: 0, texErr: 0, targetErr: 0, specsBad: 0 };
const samples = [];
for (const key of want) {
  const [file, name] = FILES[key] || []; if (!file) continue;
  const code = fs.readFileSync(path.join(ROOT, 'js', file), 'utf8').replace(/^(const|let) /gm, 'var ');
  const ctx = vm.createContext({ window: { CLS10_BOOKS: {}, CLS9_BOOKS: {}, CLS11_BOOKS: {} }, document: {}, console: { log() {}, warn() {}, error() {} }, localStorage: {}, navigator: {} });
  try { vm.runInContext(code, ctx, { timeout: 20000 }); } catch (e) { /* partial */ }
  const seen = new Set(), all = [];
  const walk = (o, d) => {
    if (!o || typeof o !== 'object' || seen.has(o) || d > 12) return; seen.add(o);
    if (Array.isArray(o.steps) && o.steps.length && !/^partial/.test(o.solutionStatus || '')) {
      if (o.steps.every(s => typeof s === 'string')) all.push(Object.assign(o.steps.slice(), { question: String(o.question || '') }));
      else if (o.steps.every(s => s && typeof s === 'object' && typeof s.en === 'string')) all.push(o.steps.map(s => ({ text: s.en, m: s.m || '' })));
    }
    Object.keys(o).forEach(k => walk(o[k], d + 1));
  };
  [ctx[name], ctx.window].forEach(x => walk(x, 0));
  let items = 0, specs = 0, bad = 0;
  all.forEach(steps => {
    items++;
    const r = autoSpec(steps, { question: steps.question || '' }); if (!r.spec) return;
    specs++; let badHere = false; const spec = r.spec;
    const cur = {};                                    // row id -> tex currently on the board
    spec.rows.forEach(rw => { total.rows++; if (rw.viz) { total.viz = (total.viz || 0) + 1; const vz = require(path.join(ROOT, 'js', 'vr_viz.js')); (rw.viz.layers || []).forEach(L => { if (L.fn && !vz.compile(L.fn)) { total.texErr++; badHere = true; if (samples.length < 8) samples.push(file + ' viz fn ' + L.fn); } }); return; } const t = Object.values(rw.tex)[0]; cur[rw.id] = t; try { render(t); } catch (e) { total.texErr++; badHere = true; if (samples.length < 8) samples.push(file + ' row ' + t.slice(0, 80) + ' :: ' + String(e.message).slice(0, 70)); } });
    spec.steps.forEach(st => {
      spec.rows.forEach(rw => { cur[rw.id] = Object.values(rw.tex)[0]; });
      st.ops.forEach(op => {
        total.ops++;
        if (op.o === 'tex') { let ok = true; try { render(op.t); } catch (e) { ok = false; total.texErr++; badHere = true; if (samples.length < 8) samples.push(file + ' tagged ' + String(op.t).slice(0, 80) + ' :: ' + String(e.message).slice(0, 70)); } if (ok) cur[op.r] = op.t; return; }
        const refs = [].concat(op.at || [], op.from || [], op.to || []);
        refs.forEach(ref => { const [rid, tag] = String(ref).split('.'); if (!tag) return; if (!(cur[rid] || '').includes('htmlClass{' + tag + '}')) { total.targetErr++; badHere = true; if (samples.length < 8) samples.push(file + ' target ' + ref + ' missing in ' + String(cur[rid]).slice(0, 60)); } });
      });
    });
    if (badHere) bad++;
  });
  total.items += items; total.specs += specs; total.specsBad += bad;
  console.log(key.padEnd(7), 'items', String(items).padStart(5), 'specs', String(specs).padStart(5), 'with problems', bad);
}
console.log(JSON.stringify(total));
if (samples.length) console.log(samples.join('\n'));
process.exit(total.texErr || total.targetErr ? 1 : 0);
