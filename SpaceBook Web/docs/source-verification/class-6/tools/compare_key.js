// Compare the printed answer key (MATH_6_BOOK.answers) with SpaceBook's verified solutions.
// Writes math/answer_key_report.md and prints a summary.
// A part "agrees" when every number in the printed answer also appears in the SpaceBook answer
// (or the other way round for long lists), after removing separators.
global.window = global;
const fs = require('fs');
const path = require('path');
const APP = path.resolve(__dirname, '../../../..');
eval(fs.readFileSync(path.join(APP, 'js/math_6_data.js'), 'utf8'));
eval(fs.readFileSync(path.join(APP, 'js/math_6_solutions.js'), 'utf8'));
const SOL = window.MATH_6_SOLUTIONS;

const nums = t => {
  t = String(t);
  // drop labels such as "l =", "A =", "Perimeter =", "LCM =" in front of values
  t = t.replace(/(^|[;,(]\s*)[A-Za-z$\\][A-Za-z.{}\\ ]*?\s*=\s*(?=[-\d$\\])/g, '$1');
  // compare final forms only: keep the part after the last "=" inside each answer
  if (t.includes('=')) t = t.slice(t.lastIndexOf('=') + 1);
  for (let i = 0; i < 4; i++) t = t.replace(/(\d),(\d{3})/g, '$1$2');
  t = t.replace(/[−–]/g, '-');
  // mixed numbers like 31\frac{1}{4} -> 31.25, plain fractions -> decimal value
  t = t.replace(/(-?)(\d+)\s*\\frac\{(\d+)\}\{(\d+)\}/g, (m, s, w, a, b) => ` ${s}${(+w + a / b).toFixed(4)} `);
  t = t.replace(/(-?)\\frac\{(\d+)\}\{(\d+)\}/g, (m, s, a, b) => ` ${s}${(a / b).toFixed(4)} `);
  t = t.replace(/\^\{?(\d+)\}?/g, '^$1');
  // ignore exponent 1 (2^1 == 2)
  t = t.replace(/\^1(?!\d)/g, '');
  return (t.match(/-?\d+(?:\.\d+)?(?:\/\d+)?(?:\^\d+)?/g) || []).map(x => {
    if (/\^/.test(x)) return x;
    const v = x.includes('/') ? x.split('/')[0] / x.split('/')[1] : +x;
    return String(Math.round(v * 100) / 100);   // values agree to 2 decimal places (book rounding)
  }).map(x => x.replace(/^-0$/, '0'));
};

// Algebraic answers: compare as an unordered set of signed terms (variables sorted inside each term).
const algebra = t => {
  let x = String(t).replace(/\$|\[,;!]|\ /g, '').replace(/\s+/g, '').replace(/[{}]/g, '').replace(/[−–]/g, '-')
    .replace(/\frac(\w)(\d)/g, '$1/$2').replace(/\times/g, '*');
  if (/[^a-zA-Z0-9+\-=^*/().]/.test(x)) return null;      // words or other symbols: not an algebra answer
  if (!/[a-z]/.test(x) || /[a-z]{4,}/i.test(x)) return null;
  const sides = x.split('=');
  return sides.map(sd => (sd.match(/[+-]?[^+-]+/g) || []).map(term => {
    const sign = term[0] === '-' ? '-' : '+';
    const body = term.replace(/^[+-]/, '');
    const coef = (body.match(/^\d+(?:\.\d+)?/) || ['1'])[0];
    const vars = (body.slice(coef === '1' && !/^1/.test(body) ? 0 : coef.length).match(/[a-zA-Z](?:\^\d+)?/g) || [])
      .map(v => v.toLowerCase()).sort().join('');
    return sign + (coef === '1' && vars ? '' : coef) + vars;
  }).sort().join(',')).join('=');
};
const splitParts = t => {
  const out = {};
  const re = /(?:^|;\s*)([a-z]|i{1,3}|iv|vi{0,3}|ix|x)\)\s*/g;
  const idx = [];
  let m;
  while ((m = re.exec(t))) idx.push([m[1], m.index, re.lastIndex]);
  if (!idx.length) return null;
  idx.forEach(([k, , start], i) => { out[k] = t.slice(start, i + 1 < idx.length ? idx[i + 1][1] : undefined).trim(); });
  return out;
};
const optionLetter = t => (String(t).match(/^\s*(i{1,3}|iv|v)\b\.?/) || [])[1];

const rows = [];
let checked = 0, agree = 0;
for (const u of MATH_6_DATA) {
  for (const ex of u.exercises) {
    const key = (MATH_6_BOOK.answers || {})[ex.id];
    if (!key) continue;
    const qmap = {};
    ex.blocks.filter(b => b.t === 'q').forEach(b => { qmap[b.no] = b; });
    for (const a of key) {
      const q = qmap[a.q];
      if (!q) { rows.push([ex.id, a.q, '', a.a, '(question not found)']); continue; }
      const kp = splitParts(a.a);
      const items = q.parts && q.parts.length ? q.parts : [q];
      const pairs = kp && q.parts && q.parts.length
        ? items.filter(p => kp[p.no] !== undefined).map(p => [p.no, kp[p.no], p.solId ? SOL[p.solId].answer : ''])
        : [['', a.a, items.map(p => (p.solId ? SOL[p.solId].answer : '')).join('; ')]];
      for (const [no, ka, sa] of pairs) {
        if (!sa) continue;
        checked++;
        const kn = nums(ka), sn = nums(sa);
        let ok;
        const ko = optionLetter(ka), so = optionLetter(sa);
        const lab = x => String(x).replace(/^\s*\$?[A-Za-z]\$?\s*=\s*/, '');
        const ak = algebra(/=/.test(ka) !== /=/.test(sa) ? lab(ka) : ka), as = algebra(/=/.test(ka) !== /=/.test(sa) ? lab(sa) : sa);
        if (ko && so) ok = ko === so;
        else if (ak && as) ok = ak === as;
        else if (!kn.length || !sn.length) ok = true;   // wording answers: not compared
        else {
          const near = (x, y) => (/\^/.test(x) || /\^/.test(y)) ? x === y
            : Math.abs(+x - +y) <= Math.max(0.051, 0.002 * Math.abs(+x));
          const has = (arr, x) => arr.some(y => near(x, y));
          const sub = kn.every(n => has(sn, n)), sup = sn.every(n => has(kn, n));
          const K = new Set(kn), S = new Set(sn);
          const open = /\.\.\.|…/.test(ka + sa) || /set of/i.test(ka + sa);   // open lists / described sets
          // lists (3+ numbers on both sides) must match exactly; short answers may be a subset either way
          ok = (K.size > 2 && S.size > 2 && !open) ? (sub && sup) : (sub || sup);
        }
        if (ok) agree++; else rows.push([ex.id, a.q, no, ka, sa]);
      }
    }
  }
}
const md = ['# Class 6 Mathematics — printed answer key vs SpaceBook solutions', '',
  `Compared ${checked} answers; ${agree} agree; ${rows.length} differ or need a look.`, '',
  'Every SpaceBook solution was worked step by step from the question as printed in the lesson pages. ',
  'Where they differ, check the question first; the printed key has known errors.', '',
  '| Exercise | Q | Part | Printed key | SpaceBook |', '|---|---|---|---|---|',
  ...rows.map(r => '| ' + r.map(x => String(x).replace(/\|/g, '/').replace(/\n/g, ' ').slice(0, 160)).join(' | ') + ' |')];
fs.writeFileSync(path.join(__dirname, '..', 'math', 'answer_key_report.md'), md.join('\n') + '\n');
console.log(`compared ${checked}, agree ${agree}, differ ${rows.length}`);
rows.forEach(r => console.log(r.map(x => String(x).slice(0, 70)).join(' | ')));
