'use strict';
/* The question bank of "Create Test" (content/testbank/), checked as data:  node tests/createtest/data.js
 * Every file parses and carries the hash the index says; every MCQ has its options and one right answer inside them; true or false has 0 or 1; the ids
 * are unique inside a class; every subject, chapter and topic an item points to exists; the counts of the index are the counts of the files.
 * Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const DIR = path.resolve(__dirname, '..', '..', 'content', 'testbank');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 400) : '')); } };
const ix = JSON.parse(fs.readFileSync(path.join(DIR, 'index.json'), 'utf8'));
check('the index lists classes and kinds', ix.schema === 'spacebook.testbank/1' && Object.keys(ix.classes).length >= 10 && ix.kinds.includes('mcq') && ix.kinds.includes('long'), Object.keys(ix.classes));
const KINDS = new Set(ix.kinds);
let total = 0, badOpts = 0, badTf = 0, badKind = 0, badRef = 0, dupIds = 0, hashBad = 0, noText = 0;
const seen = {}, perSubject = {}, perChapter = {};
for (const [c, info] of Object.entries(ix.classes)) {
  const text = fs.readFileSync(path.join(DIR, info.file));
  if (crypto.createHash('sha256').update(text).digest('hex').slice(0, 12) !== info.h) hashBad++;
  const j = JSON.parse(text.toString('utf8'));
  const ids = new Set();
  for (const it of j.items) {
    total++;
    if (ids.has(it.i)) dupIds++; ids.add(it.i);
    if (!KINDS.has(it.y)) badKind++;
    if (!it.q || it.q.length < 3) noText++;
    if (it.y === 'mcq') { if (!Array.isArray(it.o) || it.o.length < 3 || it.o.length > 5 || !Number.isInteger(it.a) || it.a < 0 || it.a >= it.o.length || new Set(it.o).size !== it.o.length) badOpts++; }
    else if (it.y === 'tf') { if (it.a !== 0 && it.a !== 1) badTf++; }
    const sj = j.subjects[it.s];
    if (!sj || (it.u >= 0 && (it.u >= sj.units || !sj.chapters[it.u])) || (it.p >= 0 && !(sj.topics[it.u] || [])[it.p])) badRef++;
    perSubject[it.s] = (perSubject[it.s] || 0) + 1;
    if (it.u >= 0) { const k = it.s + '|' + it.u; perChapter[k] = (perChapter[k] || 0) + 1; }
  }
  check('class ' + c + ': the file holds as many questions as the index says', j.items.length === info.n, [j.items.length, info.n]);
}
check('every file has the hash its index entry says', hashBad === 0, hashBad);
check('every kind is one the index knows', badKind === 0, badKind);
check('every MCQ has 3 to 5 different options and a right answer among them', badOpts === 0, badOpts);
check('every true / false question has the answer 0 or 1', badTf === 0, badTf);
check('every question has text', noText === 0, noText);
check('question ids are unique inside a class', dupIds === 0, dupIds);
check('every subject, chapter and topic a question points to exists', badRef === 0, badRef);
const idxTotal = Object.values(ix.subjects).reduce((a, s) => a + Object.values(s.n).reduce((x, y) => x + y, 0), 0);
check('the subject counts of the index add up to the questions of the files', idxTotal === total, [idxTotal, total]);
check('the chapter counts of the index are those of the files', Object.entries(ix.subjects).every(([id, s]) => Object.entries(s.chapters).every(([u, k]) => Object.values(k).reduce((a, b) => a + b, 0) === perChapter[id + '|' + u])));
check('there are at least 30,000 questions, in at least 90 subjects', total >= 30000 && Object.keys(perSubject).length >= 90, [total, Object.keys(perSubject).length]);
console.log('question bank tests: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
