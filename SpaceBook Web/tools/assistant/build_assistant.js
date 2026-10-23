'use strict';
/* Builds the passages the offline tutor ("Ask SpaceBook") answers from: content/assistant/index.json and one file per class, content/assistant/cls<N>.json.
 *     node --max-old-space-size=8192 tools/assistant/build_assistant.js [--check] [--from paras.json]
 * Every book of Classes 1 to 10 and 12 is cut into passages of about 420 characters (tools/assistant/extract_paras.js), each with the chapter it belongs to and
 * the heading it sits under. Class 11 and the older Class 9 to 12 subjects whose text does not live in these books are reached through the search index
 * (content/search/), which the tutor reads in the page. Together with the question bank (content/testbank/: the books' own questions with their answers),
 * that is everything the tutor knows: it adds no text of its own.
 * File: {v, cls, subjects: {id: {name, chapters: [{t, o}]}}, s: [subject id ...], p: [[subject no., chapter, heading, text] ...]}.
 * --check compares the hash of the inputs (the book data, this builder) and fails when the files are older. Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const ROOT = path.resolve(__dirname, '..', '..');
process.chdir(ROOT);
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const OUT = path.join(ROOT, 'content', 'assistant');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const lf = f => fs.readFileSync(path.join(ROOT, f), 'utf8').replace(/\r\n/g, '\n');

function inputsHash() {
  const man = JSON.parse(lf('content/lazy_manifest.json')), h = [];
  for (const f of man.files) { h.push(f.src + ':' + f.sha256); for (const a of (f.also || []).concat(f.after || [])) h.push(a.src + ':' + a.sha256); }
  for (const f of ['content/app_catalog.json', 'tools/assistant/build_assistant.js', 'tools/assistant/extract_paras.js', 'js/math6_reader.js']) h.push(f + ':' + sha(lf(f)));
  return sha(h.sort().join('\n'));
}
if (args.includes('--check')) {
  const f = path.join(OUT, 'index.json');
  if (!fs.existsSync(f)) { console.log('STALE  content/assistant does not exist (node tools/assistant/build_assistant.js)'); process.exit(1); }
  const have = JSON.parse(fs.readFileSync(f, 'utf8'));
  if (have.source !== inputsHash()) { console.log('STALE  content/assistant is older than the book data (node tools/assistant/build_assistant.js)'); process.exit(1); }
  let bad = 0;
  for (const c of Object.values(have.classes)) { const p = path.join(OUT, c.file); if (!fs.existsSync(p) || sha(fs.readFileSync(p)).slice(0, 12) !== c.h) { console.log('STALE  content/assistant/' + c.file + ' does not match its hash'); bad++; } }
  if (bad) process.exit(1);
  console.log('fresh  assistant  (' + Object.values(have.classes).reduce((a, c) => a + c.n, 0) + ' passages)');
  process.exit(0);
}

let raw;
if (opt('--from')) raw = JSON.parse(fs.readFileSync(opt('--from'), 'utf8'));
else {
  const { load } = require('../lib/app_sandbox');
  const extract = require('./extract_paras');
  raw = JSON.parse(load({ page: process.env.SB_PAGE || 'index.html', quiet: true }).run('JSON.stringify((' + extract.toString() + ')())', 900000));
}
const catalog = JSON.parse(lf('content/app_catalog.json'));
const subjOf = {};
for (const c of catalog.classes) for (const s of c.subjects) {
  const o0 = (s.chapters[0] || {}).o || '';
  const m = /selectSubjectChapter\('(\w+)',\s*\d+,\s*'(cls\d+)'\)/.exec(o0) || (/selectMathChapter\(/.test(o0) && /-math$/.test(s.id) ? [null, 'math', c.id] : null);
  if (m) subjOf[m[2].replace('cls', '') + ':' + m[1]] = { id: s.id, name: s.name, ur: s.ur || '', chapters: s.chapters.map(ch => ({ t: String(ch.t).replace(/\s+/g, ' ').slice(0, 90), o: ch.o })) };
}
const norm = s => String(s).toLowerCase().replace(/[^\p{L}\p{N}]+/gu, '');
const byClass = {};
let total = 0, unmapped = [];
for (const b of raw) {
  const sj = subjOf[b.id.replace('cls', '')];
  if (!sj) { unmapped.push(b.id); continue; }
  const shard = byClass[b.cls] = byClass[b.cls] || { subjects: {}, s: [], p: [] };
  if (!shard.subjects[sj.id]) { shard.subjects[sj.id] = { name: sj.name, ur: sj.ur, langs: b.langs, chapters: sj.chapters }; shard.s.push(sj.id); }
  const si = shard.s.indexOf(sj.id);
  b.units.forEach((paras, u) => {
    const seen = new Set();
    for (const [h, t] of paras) { const k = norm(t); if (!k || seen.has(k)) continue; seen.add(k); shard.p.push([si, u, h, t]); total++; }
  });
}
const index = { schema: 'spacebook.assistant/1', source: inputsHash(), classes: {}, subjects: {} };
const files = new Map();
for (const c of Object.keys(byClass).sort((a, b) => a - b)) {
  const sh = byClass[c];
  const text = JSON.stringify({ v: 1, cls: +c, subjects: sh.subjects, s: sh.s, p: sh.p }) + '\n';
  files.set('cls' + c + '.json', text);
  index.classes[c] = { file: 'cls' + c + '.json', h: sha(text).slice(0, 12), bytes: Buffer.byteLength(text), n: sh.p.length };
  sh.s.forEach(id => { index.subjects[id] = { cls: +c, name: sh.subjects[id].name }; });
}
files.set('index.json', JSON.stringify(index) + '\n');
fs.mkdirSync(OUT, { recursive: true });
for (const f of fs.readdirSync(OUT)) if (!files.has(f)) fs.unlinkSync(path.join(OUT, f));
for (const [f, text] of files) fs.writeFileSync(path.join(OUT, f), text);
console.log('wrote content/assistant: ' + total + ' passages in ' + Object.keys(byClass).length + ' class files, ' + (Array.from(files.values()).reduce((a, t) => a + Buffer.byteLength(t), 0) / 1048576).toFixed(1) + ' MB' + (unmapped.length ? ' | books without a subject id: ' + unmapped.join(', ') : ''));
