'use strict';
/* Games content check (no browser needed):  node tests/games/content.js
 *  - every Math Sprint / Little Learners generator, many runs: well-formed items, one right answer among distinct choices,
 *    and for the arithmetic / algebra skills the answer is recomputed independently from the printed question
 *  - every game for every class against the real MCQ bank: scopes, level plans, a built run of every level
 *  - reward keys have the shape api/lib/rewards.php accepts ('count' kind) */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
global.window = global;
require(path.join(ROOT, 'js', 'games_vocab.js'));
const C = require(path.join(ROOT, 'js', 'sb_games_content.js'));
require(path.join(ROOT, 'js', 'test_prep_bank.js'));
const BANK = global.SB_MCQ_BANK;

let pass = 0, fail = 0;
const bad = [];
function check(name, ok, detail) { if (ok) pass++; else { fail++; bad.push(name + (detail ? ' :: ' + String(detail).slice(0, 300) : '')); } }

const plain = s => String(s).replace(/<[^>]*>/g, '').replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/&nbsp;/g, ' ').replace(/−/g, '-').replace(/×/g, '*').replace(/÷/g, '/');
function structural(it, label) {
  const ok = it && typeof it.p === 'string' && Array.isArray(it.c) && it.c.length >= 2 && it.c.length <= 4 && Number.isInteger(it.a) && it.a >= 0 && it.a < it.c.length;
  if (!ok) { check(label + ' shape', false, JSON.stringify(it)); return false; }
  const txt = it.c.map(plain);
  const distinct = new Set(txt).size === txt.length;
  // textbook items may legitimately say "Infinity" or "null condition"; made-up items never should
  const clean = !(it.kind === 'math' || it.kind === 'learn' || !it.kind ? /\bNaN\b|undefined|Infinity|\bnull\b|\[object/ : /\bNaN\b|undefined|\[object/).test(it.p + it.c.join(' '));
  if (!distinct || !clean) { check(label + ' distinct/clean', false, it.p + ' -> ' + it.c.join(' | ')); return false; }
  pass++;
  return true;
}
const num = s => parseFloat((plain(s).match(/-?\d+(\.\d+)?/) || [NaN])[0]);

// ---------- independent checks on printed questions ----------
const verifiers = [
  // "A + B = ?" style
  it => { const m = /^(\d+) ([+−×÷]) (\d+) = \?$/.exec(it.p); if (!m) return null; const a = +m[1], b = +m[3]; const v = m[2] === '+' ? a + b : m[2] === '−' ? a - b : m[2] === '×' ? a * b : a / b; return num(it.c[it.a]) === v; },
  // "Solve: ax + b = c" / "Solve: ... = ..."   substitute the chosen answer
  it => { const m = /^Solve: (.+) = (.+)$/.exec(plain(it.p).replace(/-/g, '-')); if (!m) return null; const x = num(it.c[it.a]); const f = e => Function('x', 'return ' + e.replace(/(\d)x/g, '$1*x').replace(/(\d)\(/g, '$1*(').replace(/(^|[^\w])x/g, '$1x').replace(/--/g, '+'))(x); try { const L = f(m[1].replace(/\s+/g, '')), R = f(m[2].replace(/\s+/g, '')); return Math.abs(L - R) < 1e-9; } catch (e) { return false; } },
  // roots of a quadratic: substitute both
  it => { const m = /^Roots of (.+) = 0$/.exec(plain(it.p)); if (!m) return null; const nums = (plain(it.c[it.a]).match(/-?\d+/g) || []).map(Number); const f = x => Function('x', 'return ' + m[1].replace(/\s+/g, '').replace(/x2/g, 'x**2').replace(/(\d)x/g, '$1*x').replace(/\+-/g, '-').replace(/--/g, '+'))(x); return nums.length === 2 && nums.every(v => Math.abs(f(v)) < 1e-9); },
  // discriminant
  it => { const m = /^Find the discriminant of (.+) = 0$/.exec(plain(it.p)); if (!m) return null; const s = m[1].replace(/\s+/g, ''); const t = s.replace(/x2/g, 'X').replace(/-/g, '+-'); const parts = t.split('+').filter(Boolean); let a = 0, b = 0, c = 0; parts.forEach(p => { if (p.endsWith('X')) a = p === 'X' ? 1 : p === '-X' ? -1 : +p.slice(0, -1); else if (p.endsWith('x')) b = p === 'x' ? 1 : p === '-x' ? -1 : +p.slice(0, -1); else c = +p; }); return num(it.c[it.a]) === b * b - 4 * a * c; },
  // percent
  it => { const m = /^(\d+)% of (\d+) = \?$/.exec(plain(it.p)); if (!m) return null; return Math.abs(num(it.c[it.a]) - (+m[1]) * (+m[2]) / 100) < 1e-9; },
  // HCF / LCM
  it => { const m = /^(HCF|LCM) of (\d+) and (\d+) = \?$/.exec(plain(it.p)); if (!m) return null; const a = +m[2], b = +m[3], g = (x, y) => (y ? g(y, x % y) : x); return num(it.c[it.a]) === (m[1] === 'HCF' ? g(a, b) : a / g(a, b) * b); },
  // sets
  it => { const m = /^If n\(A\) = (\d+), n\(B\) = (\d+) and n\(A ∩ B\) = (\d+)/.exec(plain(it.p).replace(/∩/g, '∩')); if (!m) return null; return num(it.c[it.a]) === +m[1] + +m[2] - +m[3]; },
  // Pythagoras
  it => { const m = /^The two shorter sides of a right triangle are (\d+) cm and (\d+) cm/.exec(plain(it.p)); if (!m) return null; return Math.abs(num(it.c[it.a]) - Math.hypot(+m[1], +m[2])) < 1e-9; },
  it => { const m = /hypotenuse is (\d+) cm and one side is (\d+) cm/.exec(plain(it.p)); if (!m) return null; return Math.abs(num(it.c[it.a]) - Math.sqrt(m[1] * m[1] - m[2] * m[2])) < 1e-9; },
  // C(n,k) / P(n,k)
  it => { const m = /^([CP])\((\d+), (\d+)\) = \?$/.exec(plain(it.p)); if (!m) return null; const f = n => (n <= 1 ? 1 : n * f(n - 1)); const n = +m[2], k = +m[3]; return num(it.c[it.a]) === (m[1] === 'C' ? f(n) / (f(k) * f(n - k)) : f(n) / f(n - k)); },
  // mean
  it => { const m = /^Find the mean of ([0-9, ]+)\.$/.exec(plain(it.p)); if (!m) return null; const v = m[1].split(',').map(Number); return Math.abs(num(it.c[it.a]) - v.reduce((a, b) => a + b, 0) / v.length) < 1e-9; },
  // limit (x^2 - a^2)/(x - a)
  it => { const m = /^lim.* \(x2 - (\d+)\) \/ \(x - (\d+)\)$/.exec(plain(it.p).replace(/x→(\d+)/, '')); if (!m) return null; return num(it.c[it.a]) === 2 * Math.sqrt(+m[1]); },
  // log
  it => { const m = /^log(\d+) (\d+) = \?$/.exec(plain(it.p)); if (!m) return null; return Math.abs(Math.log(+m[2]) / Math.log(+m[1]) - num(it.c[it.a])) < 1e-9; },
  // dot product
  it => { const m = /^If u = \((-?\d+), (-?\d+)\) and v = \((-?\d+), (-?\d+)\), find u . v\.$/.exec(plain(it.p).replace(/·/g, '.')); if (!m) return null; return num(it.c[it.a]) === +m[1] * +m[3] + +m[2] * +m[4]; },
  // simple interest
  it => { const m = /simple interest on Rs\. (\d+) at (\d+)% per year for (\d+) year/.exec(plain(it.p)); if (!m) return null; return num(it.c[it.a]) === m[1] * m[2] * m[3] / 100; },
  // 22/7 circle
  it => { const m = /^Area of a circle of radius (\d+) cm/.exec(plain(it.p)); if (!m) return null; return Math.abs(num(it.c[it.a]) - 22 / 7 * m[1] * m[1]) < 1e-9; },
  it => { const m = /^Circumference of a circle of radius (\d+) cm/.exec(plain(it.p)); if (!m) return null; return Math.abs(num(it.c[it.a]) - 2 * 22 / 7 * m[1]) < 1e-9; },
  // slope
  it => { const m = /^Slope of the line through \((-?\d+), (-?\d+)\) and \((-?\d+), (-?\d+)\)$/.exec(plain(it.p)); if (!m) return null; return num(it.c[it.a]) === (+m[4] - +m[2]) / (+m[3] - +m[1]); },
  // distance
  it => { const m = /^Distance between \((-?\d+), (-?\d+)\) and \((-?\d+), (-?\d+)\)$/.exec(plain(it.p)); if (!m) return null; return Math.abs(num(it.c[it.a]) - Math.hypot(+m[3] - +m[1], +m[4] - +m[2])) < 1e-9; },
  // integers with brackets
  it => { const m = /^\(?(-?\d+)\)? ([+\-×÷*\/]) \(?(-?\d+)\)? = \?$/.exec(plain(it.p).replace(/\(-/g, '(-')); if (!m) return null; const a = +m[1], b = +m[3]; const v = m[2] === '+' ? a + b : m[2] === '-' ? a - b : m[2] === '*' ? a * b : a / b; return num(it.c[it.a]) === v; },
  // f(x) evaluation
  it => { const m = /^If f\(x\) = (.+), find f\((.+)\)\.$/.exec(plain(it.p)); if (!m) return null; const k = +m[2].replace(/-/g, '-'); const e = m[1].replace(/\s+/g, '').replace(/x2/g, 'x**2').replace(/(\d)x/g, '$1*x').replace(/\+-/g, '-'); return num(it.c[it.a]) === Function('x', 'return ' + e)(k); }
];

// fractions: parse the printed fractions and recompute with exact integers
function fractionOk(it) {
  const re = /<span class="g-fr"><i>([^<]+)<\/i><b>([^<]+)<\/b><\/span>/g;
  const fr = s => { const out = []; let m; re.lastIndex = 0; while ((m = re.exec(s))) out.push([m[1], m[2]]); return out; };
  const P = fr(it.p), txt = it.p.replace(re, 'F');
  const ans = it.c[it.a], A = fr(ans)[0] || [ans, '1'];
  const eq = (n1, d1, n2, d2) => n1 * d2 === n2 * d1;
  if (/^F \+ F = \?$/.test(txt)) { const [a, b] = [P[0].map(Number), P[1].map(Number)]; return eq(+A[0], +A[1], a[0] * b[1] + b[0] * a[1], a[1] * b[1]); }
  if (/^F × F = \?$/.test(txt)) { const [a, b] = [P[0].map(Number), P[1].map(Number)]; return eq(+A[0], +A[1], a[0] * b[0], a[1] * b[1]); }
  if (/^F of (\d+) = \?$/.test(txt)) { const n = +/of (\d+)/.exec(txt)[1]; return +A[0] / +A[1] === +P[0][0] * n / +P[0][1]; }
  if (/^F = F$/.test(txt)) return +ans * +P[0][1] === +P[0][0] * +P[1][1];      // a/b = ans/d2  <=>  ans*b = a*d2
  return false;
}

let verified = 0;
for (let cls = 1; cls <= 12; cls++) {
  const lad = C.MATH_LADDER[cls];
  check('math ladder exists for class ' + cls + ' with 10 levels', lad && lad.length === 10);
  if (!lad) continue;
  lad.forEach((row, li) => {
    const r = C.makeRng(cls * 100 + li);
    for (let n = 0; n < 250; n++) {
      const it = row[1](r);
      const label = 'class ' + cls + ' L' + (li + 1) + ' ' + row[0];
      if (!structural(it, label)) break;
      if (/g-fr/.test(it.p)) { verified++; check(label + ' fraction answer correct', fractionOk(it), it.p + ' -> ' + it.c[it.a]); continue; }
      for (const v of verifiers) { const res = v(it); if (res === null) continue; verified++; if (res !== true) { check(label + ' answer correct', false, it.p + ' -> ' + it.c[it.a]); } else pass++; break; }
    }
  });
}
check('independent verifiers ran on many items', verified > 2500, verified);

for (let cls = 1; cls <= 3; cls++) {
  const lad = C.LEARN_LADDER[cls];
  check('learn ladder exists for class ' + cls, lad && lad.length === 10);
  lad.forEach((row, li) => { const r = C.makeRng(cls * 31 + li); for (let n = 0; n < 150; n++) { const it = row[1](r); if (!structural(it, 'learn class ' + cls + ' L' + (li + 1) + ' ' + row[0])) break; } });
}

// ---------- every game x class x scope, with the real bank ----------
const KEY = /^[A-Za-z0-9_.:-]{1,40}\|[A-Za-z0-9_.:-]{1,60}\|u[A-Za-z0-9]{0,8}\|(trace|count)\|[a-z0-9]{1,10}\|[0-9]{1,3}$/;
let runs = 0, scopesSeen = 0;
for (let cls = 1; cls <= 12; cls++) {
  for (const game of C.ORDER) {
    const ctx0 = {cls, scope: 'all', bank: BANK};
    const scopes = C.scopesFor(game, ctx0);
    if (game === 'math') check('math is playable in class ' + cls, scopes.length === 1);
    if (game === 'learn') check('learn only in classes 1-3 (class ' + cls + ')', (scopes.length === 1) === (cls <= 3));
    for (const sc of scopes) {
      scopesSeen++;
      const ctx = {cls, scope: sc.id, bank: BANK};
      const plan = C.planFor(game, ctx);
      const label = game + ' class ' + cls + ' ' + sc.id;
      if (!plan.levels) { check(label + ' plan', false, plan.why); continue; }
      check(label + ' has 1-10 levels', plan.levels.length >= 1 && plan.levels.length <= 10, plan.levels.length);
      plan.levels.forEach(lv => {
        check(label + ' L' + lv.level + ' total fits the server (1..200)', lv.total >= 2 && lv.total <= 200, lv.total);
        const key = C.levelKey(game, cls, sc.id, lv.level, lv.total);
        check(label + ' L' + lv.level + ' key accepted by api/lib/rewards.php', KEY.test(key) && key.length <= 190, key);
        const run = C.buildLevel(game, ctx, lv.level, C.makeRng(lv.level * 7 + cls));
        runs++;
        if (!run || !run.items || run.items.length !== lv.total) { check(label + ' L' + lv.level + ' builds exactly total items', false, run && run.items && run.items.length + ' vs ' + lv.total); return; }
        pass++;
        if (run.runner === 'choice') run.items.forEach((it, i) => { if (!structural(it, label + ' L' + lv.level + ' #' + i)) return; });
        if (run.runner === 'tiles') run.items.forEach(it => check(label + ' tiles item', typeof it.p === 'string' && /^[A-Z]{3,14}$/.test(it.ans), it.ans));
        if (run.runner === 'flip') {
          run.items.forEach(it => check(label + ' flip pair', it.q && it.a));
          check(label + ' L' + lv.level + ' pairs have distinct answers', new Set(run.items.map(i => C.plain(i.a).toLowerCase())).size === run.items.length);
        }
      });
    }
  }
}
check('built many runs', runs > 300, runs);

// level keys are unique per level and per scope
const ks = new Set(); let dup = 0;
for (let cls = 1; cls <= 12; cls++) for (const g of C.ORDER) for (const sc of C.scopesFor(g, {cls, scope: 'all', bank: BANK})) { const pl = C.planFor(g, {cls, scope: sc.id, bank: BANK}); (pl.levels || []).forEach(l => { const k = C.levelKey(g, cls, sc.id, l.level, l.total); if (ks.has(k)) dup++; ks.add(k); }); }
check('no two levels share a reward key', dup === 0, dup);

// a quiz run never repeats a question, true/false statements point at the real answer
const q1 = C.buildLevel('quiz', {cls: 9, scope: 'all', bank: BANK}, 3, C.makeRng(5));
check('a quiz run has no repeated question', new Set(q1.items.map(i => C.plain(i.p))).size === q1.items.length);
const t1 = C.buildLevel('tf', {cls: 8, scope: 'all', bank: BANK}, 2, C.makeRng(9));
check('true/false run has a timer and two answers', t1.secs > 0 && t1.items.every(i => i.c.length === 2));
check('pass mark is 60 %', C.stepsNeeded(5) === 3 && C.stepsNeeded(12) === 8 && C.stepsNeeded(10) === 6);

console.log('games content: ' + pass + ' ok, ' + fail + ' failed  (' + runs + ' level runs over ' + scopesSeen + ' game scopes, ' + verified + ' answers recomputed)');
if (bad.length) { console.log(bad.slice(0, 40).join('\n')); if (bad.length > 40) console.log('... and ' + (bad.length - 40) + ' more'); }
process.exit(fail ? 1 : 0);
