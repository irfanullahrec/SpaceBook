// Class 11 Maths solutions: how many animate, KaTeX check of every row.  node tools/qa/m11_vr.js [orig]
global.window = global;
const path = require('path'), fs = require('fs'), vm = require('vm');
const eng = process.argv[2] === 'orig' ? './bak/vr_auto.orig.js' : '../../js/vr_auto.js';
require(eng); const S = global.SBVR || require(eng);
const katex = require('../../assets/vendor/katex/katex.min.js');
const w = {}; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../../js/math_11_solutions.js'), 'utf8'), { window: w });
const D = w.MATH_11_SOLUTIONS; let ok = 0, rows = 0, bad = 0, n = 0;
for (const [k, v] of Object.entries(D)) {
  n++; const st = (v.steps || []).map(s => ({ text: s.en, m: s.m || '' })); const r = (S.autoSpec || global.SBVR.autoSpec)(st, { q: '' });
  if (!r.spec) continue; ok++;
  for (const rw of r.spec.rows) for (const t of Object.values(rw.tex || {})) if (t) { rows++; try { katex.renderToString(t, { throwOnError: true, strict: 'ignore', trust: true }); } catch (e) { bad++; if (bad < 6) console.log('BAD', k, t.slice(0, 80), e.message.slice(0, 50)); } }
}
console.log({ solutions: n, animatable: ok, rows, katexBad: bad });
