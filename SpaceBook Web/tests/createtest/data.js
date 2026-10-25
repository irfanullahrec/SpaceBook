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
// the Mathematics books of Classes 5, 6, 7, 8 and 11 are not CLSn_BOOKS (MATH_n_DATA): tools/tests/extract_leaves.js walks them with a stricter rule
const MATHS = ['cls5-math', 'cls6-math', 'cls7-math', 'cls8-math', 'cls11-math'], mathItems = {}, mathBadRef = [];
for (const [c, info] of Object.entries(ix.classes)) {
  const text = fs.readFileSync(path.join(DIR, info.file));
  if (crypto.createHash('sha256').update(text).digest('hex').slice(0, 12) !== info.h) hashBad++;
  const j = JSON.parse(text.toString('utf8'));
  const ids = new Set();
  for (const it of j.items) {
    total++;
    if (ids.has(it.i)) dupIds++; ids.add(it.i);
    if (!KINDS.has(it.y)) badKind++;
    if (!it.q || (it.q.length < 3 && !(it.h && it.h.length >= 8))) noText++;      // a short operand ("68") is a question under its instruction ("Find all the factors of the following numbers.")
    if (it.y === 'mcq') { if (!Array.isArray(it.o) || it.o.length < 3 || it.o.length > 5 || !Number.isInteger(it.a) || it.a < 0 || it.a >= it.o.length || new Set(it.o).size !== it.o.length) badOpts++; }
    else if (it.y === 'tf') { if (it.a !== 0 && it.a !== 1) badTf++; }
    const sj = j.subjects[it.s];
    if (!sj || (it.u >= 0 && (it.u >= sj.units || !sj.chapters[it.u])) || (it.p >= 0 && !(sj.topics[it.u] || [])[it.p])) badRef++;
    perSubject[it.s] = (perSubject[it.s] || 0) + 1;
    if (MATHS.includes(it.s)) { (mathItems[it.s] = mathItems[it.s] || []).push(it); if (/\\_|[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(it.q + ' ' + (it.h || '') + ' ' + String(it.a) + ' ' + (it.e || '')) || it.u < 0) mathBadRef.push([it.s, it.i]); }
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
check('the Mathematics books of Classes 5, 6, 7, 8 and 11 are in the bank, with at least 500 questions each, written and multiple choice', MATHS.every(id => (mathItems[id] || []).length >= 500 && mathItems[id].some(i => i.y === 'mcq') && mathItems[id].some(i => i.y === 'num') && mathItems[id].some(i => i.y === 'short')), MATHS.map(id => [id, (mathItems[id] || []).length]));
check('every one of their questions belongs to a chapter, and has plain text (no \_ escapes, no control characters)', mathBadRef.length === 0, mathBadRef.slice(0, 5));
{
  // the chapter number of a question is the book's: chapter u of the bank is the catalog's chapter u, which starts with the unit number u + 1
  const bad = [];
  for (const [c] of Object.entries(ix.classes)) {
    const j = JSON.parse(fs.readFileSync(path.join(DIR, ix.classes[c].file), 'utf8'));
    for (const id of MATHS) { const sj = j.subjects[id]; if (sj) sj.chapters.forEach((t, u) => { if (!String(t).startsWith((u + 1) + ' ')) bad.push([id, u, t]); }); }
  }
  check('chapter u of those books in the bank is unit u + 1 of the book (the catalog order the Study Plan uses)', bad.length === 0 && MATHS.every(id => Object.keys(perSubject).includes(id)), bad.slice(0, 5));
}
console.log('question bank tests: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
