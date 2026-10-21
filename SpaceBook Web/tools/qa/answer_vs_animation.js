'use strict';
/* Compare every Class 9 / 10 Maths answer of the page books (printed key + derived) with the working that the animation shows (check 6).
 *   node tools/qa/answer_vs_animation.js <books.json cache from audit_c9_c10.js> [--list]
 * Animation source: a hand-written pack found by question text (SBVR.sol.find), else the older stored solution of the same exercise and question number
 * when its question text overlaps (>= 60 % of the words and the same numbers; the older data is a different edition for some questions). Rule: each number of the answer must occur in the numbers of the working (fractions and
 * decimals normalised); an answer with no numbers is compared by its key words. Prints counts and the disagreements. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..');
global.window = global;
const cw = console.warn; console.warn = () => { };
require(path.join(ROOT, 'js', 'vr_viz.js')); require(path.join(ROOT, 'js', 'vr_auto.js'));
fs.readdirSync(path.join(ROOT, 'js')).filter(f => /^sol_.*\.js$/.test(f)).sort((a, b) => (/^sol_m\d/.test(a) ? 1 : 0) - (/^sol_m\d/.test(b) ? 1 : 0) || a.localeCompare(b)).forEach(f => require(path.join(ROOT, 'js', f)));
console.warn = cw;
const NS = global.SBVR, LIST = process.argv.includes('--list');
const books = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
function load(file, name) {
  const ctx = vm.createContext({ window: {}, document: {}, console: { log() { }, warn() { }, error() { } }, localStorage: {}, navigator: {} });
  vm.runInContext(fs.readFileSync(path.join(ROOT, 'js', file), 'utf8').replace(/^(const|let) /gm, 'var '), ctx, { timeout: 60000 });
  return ctx[name];
}
const norm = e => { e = String(e); const m = e.match(/Review[- ]*(?:Exercise )?(\d+)/); return m ? 'R' + m[1] : e.replace(/ \(continued\)/, ''); };
const legacy = { c9: {}, c10: {} };
load('math_data.js', 'MATH_DATA').forEach(u => (u.exercises || []).forEach(e => (e.problems || []).forEach(p => { legacy.c9[norm(e.exercise) + '#' + String(p.qNo).replace(/\D/g, '')] = p; })));
load('math_10_data.js', 'MATH_10_DATA').forEach(u => (u.exercises || []).forEach(e => (e.problems || []).forEach(p => { legacy.c10[norm(e.exercise) + '#' + String(p.num).replace(/\D/g, '')] = p; })));
const strip = s => String(s || '').replace(/\$/g, ' ').replace(/\\(?:dfrac|frac)\{([^{}]*)\}\{([^{}]*)\}/g, '($1/$2)').replace(/\\[a-zA-Z]+/g, ' ').replace(/[{}]/g, ' ');
const nums = s => { const out = new Set(); strip(s).replace(/(\d+)\s*\/\s*(\d+)/g, (m, a, b) => { out.add(String(+(a / b).toFixed(3))); return ' '; }).replace(/\d+(?:\.\d+)?/g, m => { out.add(String(+(+m).toFixed(3))); }); return out; };
const words = s => new Set(strip(s).toLowerCase().match(/[a-z]{4,}/g) || []);
const text = o => JSON.stringify(o).replace(/\\\\/g, '\\');
const res = { items: 0, withWork: 0, agree: 0, disagree: [], noWork: 0 };
for (const cls of ['c9', 'c10']) {
  const bk = books[cls].math, ans = bk.book.answers || {}, qs = {};
  (function visit(b, ex) {
    if (Array.isArray(b)) return b.forEach(x => visit(x, ex));
    if (!b || typeof b !== 'object') return;
    if (b.t === 'exercise') ex = b.id;
    if (b.t === 'q' && ex) { const allp = [b.en].concat((b.parts || []).map(p => p.en)).join(' '); qs[norm(ex) + '#' + b.no] = allp; }
    for (const k of ['sections', 'blocks', 'parts']) if (b[k] && typeof b[k] === 'object') visit(b[k], ex);
  })(bk.units, null);
  for (const id in ans) for (const a of ans[id]) {
    const key = norm(id) + '#' + a.q; const qt = qs[key]; res.items++;
    let work = null, src = '';
    const pk = qt && NS.sol.find(qt);
    if (pk) { work = text(pk.steps); src = 'pack'; }
    else {
      const lp = legacy[cls][key];
      if (lp && qt) { const wq = words(qt), wl = words(lp.question); let hit = 0; wq.forEach(w => { if (wl.has(w)) hit++; }); const nq = nums(qt), nl = nums(lp.question); let nh = 0; nq.forEach(n => { if (nl.has(n)) nh++; }); const sameNums = nq.size === 0 ? true : nh / Math.max(nq.size, nl.size) >= 0.8;
      if (wq.size && hit / wq.size >= 0.6 && sameNums) { work = (lp.finalAnswer || '') + ' ' + (lp.solution || '') + ' ' + text(lp.steps || []); src = 'legacy'; } }
    }
    if (!work) { res.noWork++; continue; }
    res.withWork++;
    const an = nums(a.a), wn = nums(work);
    let missing = [...an].filter(n => !wn.has(n));
    if (!an.size) { const aw = words(a.a), ww = words(work); missing = [...aw].filter(w => !ww.has(w)); if (missing.length <= aw.size / 2) missing = []; }
    if (missing.length === 0 || (an.size >= 6 && missing.length / an.size < 0.2)) res.agree++;
    else res.disagree.push(`${cls} ${id} Q${a.q} [${src}] answer ${String(a.a).replace(/\s+/g, ' ').slice(0, 70)} | not in working: ${missing.slice(0, 6).join(',')}`);
  }
}
console.log(`answers ${res.items} | with an animation/working to compare ${res.withWork} | agree ${res.agree} | disagree ${res.disagree.length} | no working found ${res.noWork}`);
if (LIST) res.disagree.forEach(x => console.log('  ', x));
