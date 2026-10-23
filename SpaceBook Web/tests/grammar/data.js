'use strict';
/* Grammar Stats (content/grammar/) checked as data:  node tests/grammar/data.js
 * Every file parses and has the hash its index entry says; the numbers of the index are the contents of the files; topics are known, in levels 1 to 5, and
 * unique; every lesson points to a subject and chapter that exist; every practice MCQ has a right option inside its options; the four languages are there
 * with their honest sizes (English most, Arabic least). Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const DIR = path.resolve(__dirname, '..', '..', 'content', 'grammar');
let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const ix = JSON.parse(fs.readFileSync(path.join(DIR, 'index.json'), 'utf8'));
check('the index has the four languages', ['en', 'ur', 'ps', 'ar'].every(l => ix.langs[l]), Object.keys(ix.langs));
const EVENTS = new Set(['h', 'p', 'ul', 'tbl', 'box']);
for (const [lang, L] of Object.entries(ix.langs)) {
  const buf = fs.readFileSync(path.join(DIR, L.file));
  check(lang + ': the file has the hash the index says', crypto.createHash('sha256').update(buf).digest('hex').slice(0, 12) === L.h);
  const F = JSON.parse(buf.toString('utf8'));
  const ids = F.topics.map(t => t.id);
  check(lang + ': topic ids are unique and match the index', new Set(ids).size === ids.length && ids.join() === L.topics.map(t => t.id).join(), [ids.length, L.topics.length]);
  check(lang + ': every topic is in a level from 1 to 5', F.topics.every(t => t.lvl >= 1 && t.lvl <= 5 && t.name && t.group));
  let lessons = 0, items = 0, bad = 0, badMcq = 0, badEv = 0;
  for (const t of F.topics) {
    for (const x of t.lessons) {
      lessons++;
      const sj = F.subjects[x.s];
      if (!sj || !sj.chapters[x.u] || !/^select(Subject|Math)Chapter\(/.test(sj.chapters[x.u].o) || !(x.c >= 1 && x.c <= 12) || !x.ev.length) bad++;
      if (!x.ev.every(e => EVENTS.has(e.k))) badEv++;
    }
    for (const it of t.items) {
      items++;
      const sj = F.subjects[it.s];
      if (!sj || !sj.chapters[it.u] || !it.q || !it.q[0]) bad++;
      if (it.o && (!Number.isInteger(it.a) || it.a < 0 || it.a >= it.o.length || new Set(it.o).size !== it.o.length)) badMcq++;
    }
    const r = L.topics.find(x => x.id === t.id);
    if (r.lessons !== t.lessons.length) bad++;
  }
  check(lang + ': every lesson and question points to a real subject and chapter', bad === 0, bad);
  check(lang + ': every lesson holds only known kinds of text', badEv === 0, badEv);
  check(lang + ': every practice MCQ has a right option among different options', badMcq === 0, badMcq);
  check(lang + ': the index totals are the contents (' + lessons + ' lessons)', L.total.lessons === lessons && L.total.topics === F.topics.length, [L.total, lessons, items]);
  check(lang + ': at most 40 practice questions per topic and class', F.topics.every(t => { const m = {}; t.items.forEach(i => { m[i.c] = (m[i.c] || 0) + 1; }); return Object.values(m).every(n => n <= 40); }));
}
check('English has the most grammar: 30+ topics, 200+ lessons, 2,000+ practice questions', ix.langs.en.total.topics >= 30 && ix.langs.en.total.lessons >= 200 && ix.langs.en.total.exercises >= 2000, ix.langs.en.total);
check('Urdu and Pashto have 10+ topics and 400+ practice questions each', ix.langs.ur.total.topics >= 10 && ix.langs.ps.total.topics >= 8 && ix.langs.ur.total.exercises >= 400 && ix.langs.ps.total.exercises >= 400, [ix.langs.ur.total, ix.langs.ps.total]);
check('Arabic is small and says so (the books are reading lessons)', ix.langs.ar.total.topics >= 1 && ix.langs.ar.total.lessons < 50, ix.langs.ar.total);
check('English runs from level 1 to level 4 or more', [1, 2, 3, 4].every(n => ix.langs.en.topics.some(t => t.lvl === n)));
console.log('grammar data tests: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
