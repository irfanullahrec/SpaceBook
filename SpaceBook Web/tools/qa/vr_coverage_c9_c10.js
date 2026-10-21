'use strict';
/* Animated-solution coverage for Class 9 + 10 Maths (check 6) — dev only.
 *   node tools/qa/vr_coverage_c9_c10.js [--list]
 * For every exercise problem and worked example of MATH_DATA (Class 9) and MATH_10_DATA (Class 10): does it get a board?
 *   animatable = the written steps give at least one equation chain (SBVR.autoSpec) or a hand-written pack (SBVR.sol.find) exists.
 * Items with neither are the ones that keep the plain, static solution. Prints per class / per unit and, with --list, every missing item. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..');
global.window = global;
const cw = console.warn; console.warn = () => { };
require(path.join(ROOT, 'js', 'vr_viz.js')); require(path.join(ROOT, 'js', 'vr_auto.js'));
fs.readdirSync(path.join(ROOT, 'js')).filter(f => /^sol_.*\.js$/.test(f)).sort((a, b) => (/^sol_m\d/.test(a) ? 1 : 0) - (/^sol_m\d/.test(b) ? 1 : 0) || a.localeCompare(b)).forEach(f => require(path.join(ROOT, 'js', f)));
console.warn = cw;
const NS = global.SBVR;
const LIST = process.argv.includes('--list');
function load(file, name) {
  const ctx = vm.createContext({ window: {}, document: {}, console: { log() { }, warn() { }, error() { } }, localStorage: {}, navigator: {} });
  vm.runInContext(fs.readFileSync(path.join(ROOT, 'js', file), 'utf8').replace(/^(const|let) /gm, 'var '), ctx, { timeout: 60000 });
  return ctx[name];
}
const stepsOf = p => Array.isArray(p.steps) && p.steps.length ? p.steps.map(s => typeof s === 'string' ? s : (s.en || s.text || '')) : String(p.solution || '').split(/\n+/).filter(Boolean);
function check(q, steps) {
  const pk = NS.sol.find(q);
  if (pk) { const r = NS.autoSpec(pk.steps, { board: pk.board, question: q, maxSteps: 80 }); return r.spec ? 'pack' : 'pack-nospec'; }
  const r = NS.autoSpec(steps, { question: q, maxSteps: 80 });
  return r.spec ? 'auto' : 'none';
}
const out = {};
for (const [label, file, name] of [['Class 9', 'math_data.js', 'MATH_DATA'], ['Class 10', 'math_10_data.js', 'MATH_10_DATA']]) {
  const data = load(file, name);
  const c = out[label] = { items: 0, pack: 0, auto: 0, none: 0, perUnit: {} , missing: [] };
  data.forEach(u => {
    const row = c.perUnit[u.number] = c.perUnit[u.number] || { items: 0, none: 0 };
    const visit = (q, steps, tag) => {
      if (!q) return;
      c.items++; row.items++;
      const r = check(q, steps);
      if (r === 'pack' || r === 'pack-nospec') c.pack++; else if (r === 'auto') c.auto++; else { c.none++; row.none++; c.missing.push(`U${u.number} ${tag}: ${String(q).replace(/\s+/g, ' ').slice(0, 80)}`); }
    };
    (u.exercises || []).forEach(ex => (ex.problems || []).forEach(p => visit(p.question, stepsOf(p), 'Ex ' + (ex.exercise || ex.id || '') + ' ' + (p.qNo || ''))));
    (u.workedExamples || []).forEach(w => visit(w.question || w.problem || w.title, stepsOf(w), 'Example ' + (w.number || w.no || '')));
  });
  console.log(`${label}: ${c.items} items | pack ${c.pack} | auto-animatable ${c.auto} | no animation ${c.none}`);
  console.log('  by unit (none/items): ' + Object.entries(c.perUnit).map(([k, v]) => `${k}:${v.none}/${v.items}`).join('  '));
  if (LIST) c.missing.forEach(m => console.log('   ', m));
}
