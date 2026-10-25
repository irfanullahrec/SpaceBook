'use strict';
/* js/sb_mastery.js without a page: the rounds of a check (mistakes only, until a whole round is right), the record kept, and which questions belong to
 * which task of a plan.     node tests/mastery/engine.js
 * Dev-only, never shipped. */
const M = require('../../js/sb_mastery.js');
const { createRun, shuffleOptions, usable } = M.engine;
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 300) : '')); } };
const rng = seed => { let a = seed | 0; return () => { a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; };
const mcq = (id, a) => ({ id, y: 'mcq', q: 'Question ' + id, o: ['one', 'two', 'three', 'four'], a: a == null ? 1 : a });
const written = id => ({ id, y: 'short', q: 'Explain ' + id, a: 'Because ' + id });

// ---- 1. the rounds: five questions, two missed, one of those missed again
{
  const items = ['a', 'b', 'c', 'd', 'e'].map(id => mcq(id));
  const run = createRun(items, { rng: rng(7) });
  const plan = [new Set(['a', 'b']), new Set(['a']), new Set()];            // who is answered wrongly in round 1, 2, 3
  const asked = [], phases = [run.phase];
  let guard = 0;
  while (run.phase !== 'passed' && guard++ < 50) {
    if (run.phase === 'roundEnd') { phases.push('roundEnd'); run.retry(); phases.push(run.phase); continue; }
    const round = run.round, ids = [];
    while (run.phase === 'ask' && run.round === round) {
      const it = run.current(); ids.push(it.id);
      run.answer(!plan[round - 1].has(it.id));
      run.next();
    }
    asked.push(ids);
  }
  phases.push(run.phase);
  check('round 1 asks all five questions', asked[0].length === 5 && new Set(asked[0]).size === 5, asked[0]);
  check('round 2 asks only the two that were wrong', asked[1].length === 2 && new Set(asked[1]).has('a') && new Set(asked[1]).has('b'), asked[1]);
  check('round 3 asks only the one that was wrong again', asked[2].length === 1 && asked[2][0] === 'a', asked[2]);
  check('the check is passed only after a round with no mistake', run.phase === 'passed' && asked.length === 3, [run.phase, asked.length]);
  check('phases go ask -> round end -> ask -> round end -> ask -> passed', phases.join('>') === 'ask>roundEnd>ask>roundEnd>ask>passed', phases);
  const rec = run.record();
  check('the record: 3 rounds, 5 questions, 3 right first time, 2 put right, 3 wrong answers in all',
    rec.mode === 'check' && rec.rounds === 3 && rec.asked === 5 && rec.first === 3 && rec.fixed === 2 && rec.wrong === 3, rec);
  check('the record names the questions that were missed', rec.missed.slice().sort().join() === 'a,b' && rec.auto === 5 && rec.self === 0, rec);
}
// ---- 2. a perfect first round
{
  const run = createRun([mcq('x'), mcq('y'), written('z')], { rng: rng(3) });
  while (run.phase === 'ask') { run.answer(true); run.next(); }
  const rec = run.record();
  check('all right at once: passed in one round, nothing to fix', run.phase === 'passed' && rec.rounds === 1 && rec.first === 3 && rec.fixed === 0 && rec.wrong === 0, rec);
  check('written questions are counted as self-marked', rec.auto === 2 && rec.self === 1, rec);
}
// ---- 3. the rules of the machine
{
  const run = createRun([mcq('p'), mcq('q')], { rng: rng(1) });
  check('next() before an answer does nothing', run.next() === 'ask' && run.position === 0);
  check('the first answer counts', run.answer(false) === true);
  check('a second answer to the same question is ignored', run.answer(true) === false);
  run.next();
  run.answer(true); run.next();
  check('a round with a mistake ends in "roundEnd", the mistake is listed', run.phase === 'roundEnd' && run.mistakes().length === 1, run.phase);
  check('retry() starts a round of the mistakes only', run.retry() === true && run.round === 2 && run.total === 1);
  check('retry() outside a round end does nothing', run.retry() === false);
  run.answer(true); run.next();
  check('the last mistake put right passes the check', run.phase === 'passed');
}

// ---- 4. questions
{
  check('an MCQ needs 2+ options and a valid key', usable(mcq('m')) && !usable({ y: 'mcq', q: 'x', o: ['a'], a: 0 }) && !usable({ y: 'mcq', q: 'x', o: ['a', 'b'], a: 5 }) && !usable({ y: 'mcq', q: 'x', o: ['a', 'b'] }));
  check('true/false needs 0 or 1', usable({ y: 'tf', q: 'x', a: 0 }) && usable({ y: 'tf', q: 'x', a: 1 }) && !usable({ y: 'tf', q: 'x', a: 2 }));
  check('a written question needs the book\'s answer', usable(written('w')) && !usable({ y: 'short', q: 'x' }) && !usable({ y: 'short', q: 'x', a: '  ' }) && !usable({ y: 'short', q: '', a: 'y' }));
  const it = { y: 'mcq', q: 'q', o: ['alpha', 'beta', 'gamma', 'delta'], a: 2 };
  let ok = true;
  for (let s = 1; s < 40; s++) { const v = shuffleOptions(it, rng(s)); if (v.o[v.a] !== 'gamma' || v.o.slice().sort().join() !== it.o.slice().sort().join()) ok = false; }
  check('shuffled options keep the right answer on the right text', ok);
  const keep = { y: 'mcq', q: 'q', o: ['red', 'blue', 'all of the above', 'none'], a: 2 };
  check('"all of the above" questions keep their order', shuffleOptions(keep, rng(5)).o.join() === keep.o.join());
}

// ---- 5. which questions belong to which task
const SUBJ = 'cls6-sci';
const topics = ['Cells', 'Tissues', 'Organs', 'Systems', 'Habitats'];
const mk = (n, y, p, extra) => Array.from({ length: n }, (_, i) => Object.assign({ s: SUBJ, c: 6, u: 2, p, y, i: y + p + '_' + i, q: y + ' ' + p + ' ' + i + '?' }, y === 'mcq' ? { o: ['a', 'b', 'c', 'd'], a: i % 4 } : y === 'tf' ? { a: i % 2 } : { a: 'answer ' + i }, extra || {}));
const shard = { subjects: { [SUBJ]: { name: 'Science', topics: { 2: topics } } }, items: [] };
topics.forEach((_, p) => { shard.items.push(...mk(4, 'mcq', p), ...mk(2, 'tf', p), ...mk(2, 'short', p)); });
shard.items.push(...mk(3, 'mcq', -1), ...mk(2, 'long', -1));
shard.items.push({ s: SUBJ, c: 6, u: 3, p: -1, y: 'mcq', i: 'other', q: 'another chapter', o: ['a', 'b'], a: 0 });   // chapter 3: never mixed in
const T = (cat, a, b) => ({ s: SUBJ, ch: 2, cat, a, b, n: b - a + 1 });
{
  const r = M.pick(shard, { read: 10 }, T('read', 1, 2));
  check('lesson parts 1-2 of 10 (five topics) ask about the first topic only', r.items.length >= 4 && r.items.every(it => it.p === 0) && r.scope === 'part' && !r.fallback, r.items.map(i => i.p));
  check('those questions are marked by the page (MCQ / true-false)', r.items.every(it => it.y === 'mcq' || it.y === 'tf'));
  check('each question carries its topic\'s name', r.items.every(it => it.topic === 'Cells'), r.items.map(i => i.topic));
  const r2 = M.pick(shard, { read: 10 }, T('read', 9, 10));
  check('lesson parts 9-10 of 10 ask about the last topic', r2.items.length >= 4 && r2.items.every(it => it.p === 4), r2.items.map(i => i.p));
  const r3 = M.pick(shard, { read: 10 }, T('read', 1, 10));
  const topicsSeen = new Set(r3.items.map(i => i.p));
  check('reading the whole chapter asks at most 10 questions, taken from every topic in turn', r3.items.length === 10 && topicsSeen.size === 5, [r3.items.length, [...topicsSeen]]);
  check('no question of another chapter is ever asked', [r, r2, r3].every(x => x.items.every(it => it.u === 2)));
}
{
  const thin = { subjects: shard.subjects, items: shard.items.filter(it => it.p !== 0).concat(shard.items.filter(it => it.p === 0 && it.y === 'mcq').slice(0, 1)) };   // one question left about the first topic
  const r = M.pick(thin, { read: 10 }, T('read', 1, 2));
  check('when the first topic has too few questions the chapter\'s own are used, and the check says so', r.fallback === true && r.scope === 'chapter' && r.items.length >= 3, [r.scope, r.items.length]);
}
{
  // MCQ tasks partition the chapter's MCQs: 5 tasks of 5 over 23 MCQs in the book, nothing asked twice, nothing left out
  const total = shard.items.filter(it => it.u === 2 && it.y === 'mcq').length;      // 20 + 3 = 23
  const got = [];
  for (let a = 1; a <= 21; a += 5) got.push(M.pick(shard, { mcq: 25 }, T('mcq', a, Math.min(25, a + 4))).items.map(i => i.i));
  const flat = got.flat();
  check('MCQ tasks 1-5, 6-10 ... cover the chapter\'s MCQs without overlap', new Set(flat).size === flat.length && flat.length === total, [flat.length, new Set(flat).size, total]);
  check('each MCQ task asks MCQs only', got.flat().every(id => /^mcq/.test(id)));
  const first = M.pick(shard, { mcq: 23 }, T('mcq', 1, 5));
  check('MCQs 1-5 of 23 are the first five MCQs of the chapter, in book order', first.items.length === 5 && first.items.map(i => i.i).join() === shard.items.filter(it => it.u === 2 && it.y === 'mcq').slice(0, 5).map(i => i.i).join());
  const fewer = { subjects: shard.subjects, items: shard.items.filter(it => it.y !== 'mcq' || it.p === 0) };               // the book holds 4 MCQs, the plan counted 20
  const a1 = M.pick(fewer, { mcq: 20 }, T('mcq', 1, 10)).items.map(i => i.i), a2 = M.pick(fewer, { mcq: 20 }, T('mcq', 11, 20)).items.map(i => i.i);
  check('when the plan counted more MCQs than the book holds, the tasks share what exists', a1.length >= 1 && a2.length >= 1 && a1.filter(x => a2.includes(x)).length === 0 && a1.length + a2.length === 4, [a1, a2]);
}
{
  const sq = M.pick(shard, { sq: 10 }, T('sq', 1, 5));
  check('short-question tasks ask the book\'s short questions (written, self-marked)', sq.items.length > 0 && sq.items.every(it => it.y === 'short') && !sq.fallback);
  const noLong = { subjects: shard.subjects, items: shard.items.filter(it => it.y !== 'long') };
  const lq = M.pick(noLong, { lq: 2 }, T('lq', 1, 2));
  check('with no long questions in the book the check falls back to the chapter, MCQs first, and says so', lq.fallback === true && lq.items.length >= 2 && lq.items.every(it => it.y === 'mcq' || it.y === 'tf'), [lq.fallback, lq.items.map(i => i.y)]);
  const none = M.pick(shard, { mcq: 3 }, { s: SUBJ, ch: 9, cat: 'mcq', a: 1, b: 3, n: 3 });
  check('a chapter with no question at all has no check (the plan lets the student mark it)', none.items.length === 0 && none.scope === 'none');
}
{
  const bad = { subjects: shard.subjects, items: [{ s: SUBJ, c: 6, u: 2, p: 0, y: 'mcq', i: 'bad1', q: 'no key', o: ['a', 'b'] }, { s: SUBJ, c: 6, u: 2, p: 0, y: 'short', i: 'bad2', q: 'no answer' }] };
  check('questions without a key or an answer are never asked', M.pick(bad, { read: 1 }, T('read', 1, 1)).items.length === 0);
  const big = { subjects: shard.subjects, items: Array.from({ length: 80 }, (_, i) => ({ s: SUBJ, c: 6, u: 2, p: -1, y: 'mcq', i: 'big' + i, q: 'q' + i, o: ['a', 'b'], a: 0 })) };
  const r = M.pick(big, { mcq: 80 }, T('mcq', 1, 80));
  check('a check never has more than ' + M.config.MAX_Q + ' questions (spread over the range)', r.items.length === M.config.MAX_Q, r.items.length);
}

console.log('---\nmastery engine: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
