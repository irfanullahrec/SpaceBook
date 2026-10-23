'use strict';
/* node tools/vr/validate_arith.js [--v] [--set 5,6,7,8,11]
 * Runs the two accumulating-board narrators (js/vr_arith.js) over every book solution of Classes 5-8 and 11 and checks, without a browser:
 *   - how many solutions each one takes over, and that the board has MORE steps than the book's own list
 *   - every row text, every tagged variant ("tex" op) and every $...$ in a step's explanation renders with KaTeX (throwOnError)
 *   - every op names a row that exists by then, and every .k-tag target is present in that row's text when the op runs
 *   - the last row written is the one marked final, and no step writes the same row twice
 */
const fs = require('fs');
const path = require('path');
const ROOT = path.join(__dirname, '..', '..');
const katex = require(path.join(ROOT, 'assets', 'vendor', 'katex', 'katex.min.js'));
require(path.join(ROOT, 'js', 'vr_auto.js'));                 // SBVR.diff (the rows narrator uses it)
const A = require(path.join(ROOT, 'js', 'vr_arith.js'));
const verbose = process.argv.includes('--v');
const sets = (process.argv.includes('--set') ? process.argv[process.argv.indexOf('--set') + 1] : '5,6,7,8,11').split(',').map(Number);
const render = t => katex.renderToString(t, { trust: true, throwOnError: true, strict: 'ignore', output: 'html' });

const stat = { arith: { n: 0, steps: 0, book: 0 }, rows: { n: 0, steps: 0, book: 0 } };
const skipped = [], issues = [];
const bad = (id, msg) => { if (issues.length < 60) issues.push(id + ' ' + msg); };

function check(id, spec, bookLen, kind) {
  const ids = new Map(spec.rows.map(r => [r.id, r]));
  if (ids.size !== spec.rows.length) bad(id, 'duplicate row id');
  spec.rows.forEach(r => { Object.keys(r.tex).forEach(k => { try { render(r.tex[k]); } catch (e) { bad(id, 'row ' + r.id + ' ' + String(e.message).slice(0, 80)); } }); });
  const written = new Set();
  spec.steps.forEach((s, i) => {
    (String(s.html).match(/\$([^$]+)\$/g) || []).forEach(m => { try { render(m.slice(1, -1)); } catch (e) { bad(id, 'step ' + i + ' html ' + m.slice(0, 50) + ' ' + String(e.message).slice(0, 50)); } });
    const cur = {};
    spec.rows.forEach(r => { cur[r.id] = r.tex[Object.keys(r.tex).map(Number).sort((a, b) => a - b)[0]]; });
    // the board at the start of step i shows the row texts as of the end of the previous step (plain)
    spec.rows.forEach(r => { const ks = Object.keys(r.tex).map(Number).filter(k => k < i); if (ks.length) cur[r.id] = r.tex[Math.max.apply(null, ks)]; });
    const needRow = (rid, what) => { const r = ids.get(rid); if (!r) { bad(id, 'step ' + i + ' ' + what + ' unknown row ' + rid); return null; } if (r.first > i) bad(id, 'step ' + i + ' ' + what + ' row ' + rid + ' that starts at ' + r.first); return r; };
    let wrote = 0;
    (s.ops || []).forEach(op => {
      if (op.o === 'tex') { needRow(op.r, 'tex'); try { render(op.t); } catch (e) { bad(id, 'step ' + i + ' tagged ' + String(op.t).slice(0, 60) + ' ' + String(e.message).slice(0, 50)); } cur[op.r] = op.t; return; }
      if (op.o === 'write') { needRow(op.r, 'write'); if (written.has(op.r)) bad(id, 'row ' + op.r + ' written twice'); written.add(op.r); wrote++; return; }
      [].concat(op.at || [], op.from || [], op.to || []).forEach(ref => {
        const [rid, tag] = String(ref).split('.'); if (!tag) return; needRow(rid, op.o);
        if (!String(cur[rid] || '').includes('htmlClass{' + tag + '}')) bad(id, 'step ' + i + ' ' + op.o + ' target ' + ref + ' not in ' + String(cur[rid]).slice(0, 50));
      });
    });
    if (!wrote && (s.ops || []).filter(o => o.o !== 'wait').length < 2) bad(id, 'step ' + i + ' does nothing visible (' + kind + ')');
  });
  const fin = spec.rows.filter(r => r.final);
  if (fin.length !== 1 || fin[0] !== spec.rows.filter(r => /^s\d+$|^b\d+$/.test(r.id)).pop()) bad(id, 'final row is not the last state row');
  if (spec.steps.length <= bookLen) bad(id, 'not more steps than the book: ' + spec.steps.length + ' vs ' + bookLen);
}

let total = 0;
for (const n of sets) {
  const f = path.join(ROOT, 'js', 'math_' + n + '_solutions.js');
  if (!fs.existsSync(f)) continue;
  let S;
  try { S = new Function('window', fs.readFileSync(f, 'utf8') + ';return window.MATH_' + n + '_SOLUTIONS')({}); } catch (e) { console.log('cannot load', f, e.message); continue; }
  for (const key of Object.keys(S || {})) {
    const st = (S[key] && S[key].steps) || [];
    if (!st.length) continue;
    total++;
    const id = n + ':' + key, rows = st.map(x => ({ text: x.en || '', m: x.m || '' }));
    let kind = 'arith', spec = null;
    try { spec = A.arithSpec(rows, {}); if (!spec) { kind = 'rows'; spec = A.rowsSpec(rows, {}); } } catch (e) { bad(id, kind + ' threw ' + e.message); continue; }
    if (!spec) { skipped.push(id); continue; }
    stat[kind].n++; stat[kind].steps += spec.steps.length; stat[kind].book += st.length;
    check(id, spec, st.length, kind);
    if (verbose && stat[kind].n <= 2) console.log(id, kind, st.length, '->', spec.steps.length, '\n  ' + spec.steps.map(s => s.html.replace(/<[^>]+>/g, '')).join('\n  '));
  }
}
/* --fuzz N: N random questions (fractions, mixed numbers, decimals, negative numbers, powers, every bracket type) through the same checks.
   A question the narrator declines (too big, a non-terminating decimal) is fine; a question it takes must pass every check and every line must be true. */
if (process.argv.includes('--fuzz')) {
  const N = +process.argv[process.argv.indexOf('--fuzz') + 1] || 2000;
  let s = 12345; const rand = () => { s |= 0; s = s + 0x6D2B79F5 | 0; let t = Math.imul(s ^ s >>> 15, 1 | s); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  const pick = a => a[Math.floor(rand() * a.length)], int = (lo, hi) => lo + Math.floor(rand() * (hi - lo + 1));
  const atom = mode => {
    let t;
    if (mode === 'dec') t = rand() < 0.4 ? String(int(1, 30)) : int(0, 30) + '.' + pick(['5', '25', '75', '4', '08', '125', '6', '35']);
    else { const r = rand(); t = r < 0.4 ? String(int(1, 25)) : r < 0.8 ? '\\frac{' + int(1, 9) + '}{' + int(2, 9) + '}' : int(1, 9) + '\\frac{' + int(1, 5) + '}{' + int(2, 7) + '}'; }
    if (rand() < 0.22) t = '(-' + t + ')';
    if (mode === 'frac' && /^\(?-?\d+\)?$/.test(t) && rand() < 0.12) t = (/^\(/.test(t) ? t : '(' + t + ')') + '^{' + int(2, 3) + '}';
    return t;
  };
  const expr = (mode, depth) => {
    const nOps = int(1, 3), parts = [];
    for (let i = 0; i <= nOps; i++) { parts.push(depth > 0 && rand() < 0.35 ? group(mode, depth - 1) : atom(mode)); if (i < nOps) parts.push(pick([' + ', ' - ', ' \\times ', ' \\div '])); }
    return parts.join('');
  };
  const group = (mode, depth) => { const br = pick([['(', ')'], ['[', ']'], ['\\{', '\\}'], ['\\overline{', '}']]); return br[0] + ' ' + expr(mode, depth) + ' ' + br[1]; };
  const fz = { made: 0, taken: 0, mode: { frac: 0, dec: 0 }, steps: 0, lines: 0 };
  for (let k = 0; k < N; k++) {
    const mode = rand() < 0.35 ? 'dec' : 'frac', q = expr(mode, 2), root = A.parse(q); fz.made++;
    if (!root) { if (q.length < 200) bad('fuzz ' + q, 'generator made something the parser refuses'); continue; }
    const v = A.val(root); if (!v) continue;
    const fin = mode === 'dec' ? A.fmt(v) : (v.d === 1 ? String(v.n) : (v.n < 0 ? '-' : '') + '\\frac{' + Math.abs(v.n) + '}{' + v.d + '}');
    if (fin === null) continue;
    let spec = null;
    try { spec = A.arithSpec([{ text: '', m: q + ' = ' + fin }], {}); } catch (e) { bad('fuzz ' + q, 'threw ' + e.message); continue; }
    if (!spec) continue;
    fz.taken++; fz.mode[mode]++; fz.steps += spec.steps.length;
    check('fuzz ' + q, spec, 1, 'fuzz');
  }
  console.log('fuzz: made', fz.made, '| narrated', fz.taken, '(frac ' + fz.mode.frac + ', dec ' + fz.mode.dec + ') | board steps', fz.steps);
}
console.log('solutions with steps:', total, '| left to the older presentation:', skipped.length);
for (const k of ['arith', 'rows']) console.log(k.padEnd(6), 'solutions', String(stat[k].n).padStart(4), '| book steps', String(stat[k].book).padStart(5), '-> board steps', String(stat[k].steps).padStart(5), '(x' + (stat[k].steps / Math.max(1, stat[k].book)).toFixed(2) + ')');
if (issues.length) { console.log('ISSUES', issues.length); issues.forEach(x => console.log(' ', x)); process.exitCode = 1; } else console.log('no issues');
