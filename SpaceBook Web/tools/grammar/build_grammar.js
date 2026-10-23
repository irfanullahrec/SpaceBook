'use strict';
/* Builds "Grammar Stats": content/grammar/index.json (the numbers for every topic of every language) and one file per language (content/grammar/<en|ur|ps|ar>.json:
 * the lessons and the practice questions of every topic, from the first classes to the last).
 *     node --max-old-space-size=8192 tools/grammar/build_grammar.js [--check] [--from leaves.json]
 * What goes in: the English, Urdu, Pashto and Arabic books of Classes 1 to 12 (CLSn_BOOKS). A lesson is the teaching text of the books (a Teaching Point
 * box, the rule under a heading, a table of forms with its examples) that is about one topic of tools/grammar/topics.js; a practice question is an exercise
 * question whose heading, exercise name or instruction is about that topic, with its answer where the project has one. A topic is recognised by its words
 * in those headings; a lesson or question that matches no topic is not counted (so a number is never inflated by guessing). Nothing is invented.
 * --check compares the hash of the inputs (the book data, the topics, this builder) and fails when the files are older. Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const ROOT = path.resolve(__dirname, '..', '..');
process.chdir(ROOT);
const TOPICS = require('./topics');
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const OUT = path.join(ROOT, 'content', 'grammar');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const lf = f => fs.readFileSync(path.join(ROOT, f), 'utf8').replace(/\r\n/g, '\n');
const LANGKEY = { eng: 'en', urdu: 'ur', pashto: 'ps', arabic: 'ar' };
const LANGNAME = { en: 'English', ur: 'Urdu', ps: 'Pashto', ar: 'Arabic' };
const LANGNATIVE = { en: 'English', ur: 'اردو', ps: 'پښتو', ar: 'العربية' };

function inputsHash() {
  const man = JSON.parse(lf('content/lazy_manifest.json')), h = [];
  for (const f of man.files) { h.push(f.src + ':' + f.sha256); for (const a of (f.also || []).concat(f.after || [])) h.push(a.src + ':' + a.sha256); }
  for (const f of ['content/app_catalog.json', 'tools/grammar/topics.js', 'tools/grammar/build_grammar.js', 'tools/tests/extract_leaves.js']) h.push(f + ':' + sha(lf(f)));
  return sha(h.filter(s => !s.startsWith('js/fills_data.js:')).sort().join('\n'));   // fills_data.js is made after the manifest it is listed in; nothing here depends on it
}
if (args.includes('--check')) {
  const f = path.join(OUT, 'index.json');
  if (!fs.existsSync(f)) { console.log('STALE  content/grammar does not exist (node tools/grammar/build_grammar.js)'); process.exit(1); }
  const have = JSON.parse(fs.readFileSync(f, 'utf8'));
  if (have.source !== inputsHash()) { console.log('STALE  content/grammar is older than the book data or the topics (node tools/grammar/build_grammar.js)'); process.exit(1); }
  let bad = 0;
  for (const [l, v] of Object.entries(have.langs)) { const p = path.join(OUT, v.file); if (!fs.existsSync(p) || sha(fs.readFileSync(p)).slice(0, 12) !== v.h) { console.log('STALE  content/grammar/' + v.file + ' does not match its hash'); bad++; } }
  if (bad) process.exit(1);
  console.log('fresh  grammar  (' + Object.values(have.langs).map(v => v.topics.length + ' topics').join(', ') + ')');
  process.exit(0);
}

let raw;
if (opt('--from')) raw = JSON.parse(fs.readFileSync(opt('--from'), 'utf8'));
else {
  const { load } = require('../lib/app_sandbox');
  const extract = require('../tests/extract_leaves');
  raw = JSON.parse(load({ page: process.env.SB_PAGE || 'index.html', quiet: true }).run('JSON.stringify((' + extract.toString() + ')())', 600000));
}
const catalog = JSON.parse(lf('content/app_catalog.json'));
const subjOf = {};
for (const c of catalog.classes) for (const s of c.subjects) {
  const o0 = (s.chapters[0] || {}).o || '';
  const m = /selectSubjectChapter\('(\w+)',\s*\d+,\s*'(cls\d+)'\)/.exec(o0);
  if (m) subjOf[m[2].replace('cls', '') + ':' + m[1]] = { id: s.id, name: s.name, chapters: s.chapters.map(ch => ({ t: ch.t, o: ch.o })) };
}

// the books mark a word with <u>, <b> or **: the reader draws ** as bold and escapes tags, so tags become ** and other tags go
const clean = s => String(s == null ? '' : s).replace(/<(u|b|strong)>([\s\S]*?)<\/\1>/gi, '**$2**').replace(/<br\s*\/?>/gi, ' ').replace(/<\/?[a-z][^>]*>/gi, '').replace(/\s+/g, ' ').trim();
const topicOf = (lang, label) => { const L = TOPICS.LANGS[lang]; const t = clean(label); if (!t) return null; for (const tp of L) if (tp.rx.test(t)) return tp; return null; };
const PLACEHOLDER = /^(solution|model answer|sample answer|see the unit text|agent answer|answer|نمونے کا جواب|حل|جواب)\s*[.:]?$/i;
// a reading lesson's word list and glossary are not grammar lessons: these topics count practice questions only
const NO_LESSON = new Set(['vocabulary', 'ur-lugat', 'ps-meaning']);
const byLang = {};
for (const l of Object.keys(TOPICS.LANGS)) byLang[l] = new Map(TOPICS.LANGS[l].map(t => [t.id, { t, lessons: [], items: [], cls: {} }]));
const bump = (rec, cls, k) => { const c = rec.cls[cls] = rec.cls[cls] || { l: 0, e: 0 }; c[k]++; };

// ── lessons ────────────────────────────────────────────────────────────
let cards = 0, items = 0, leavesSeen = 0;
for (const b of raw.books) {
  const key = b.id.split(':')[1], lang = LANGKEY[key]; if (!lang) continue;
  const sj = subjOf[b.id.replace('cls', '')]; if (!sj) continue;
  b.units.forEach((u, ui) => u.secs.forEach(sec => {
    if (!sec.flat || !sec.flat.length) return;
    if (/glossary|meanings? of words|new words|word list|vocabulary list|فرہنگ|لغت|لغات|مشکل الفاظ|ټکي او معنې/i.test(sec.t)) return;      // a word list is not a lesson
    const secTopic = topicOf(lang, sec.t);
    let buf = [], cur = null;
    const flush = tp => {
      const evs = buf; buf = [];
      if (!tp || NO_LESSON.has(tp.id)) return;
      const chars = evs.reduce((a, e) => a + (e.k === 'p' ? clean(e.t[0]).length : e.k === 'ul' ? e.t.join(' ').length : e.k === 'tbl' ? e.rows.flat().join(' ').length : 0), 0);
      if (chars < 50) return;
      const rec = byLang[lang].get(tp.id);
      const tidy = e => e.k === 'ul' ? Object.assign({}, e, { t: e.t.map(clean) }) : e.k === 'tbl' ? Object.assign({}, e, { rows: e.rows.map(r => r.map(clean)) }) : Array.isArray(e.t) ? Object.assign({}, e, { t: e.t.map(clean) }) : e;
      const keep = evs.filter(e => e.k === 'h' || e.k === 'p' || e.k === 'ul' || e.k === 'tbl' || e.k === 'box').slice(0, 16).map(tidy);
      rec.lessons.push({ c: b.cls, s: sj.id, u: ui, ut: u.title.slice(0, 80), st: sec.t.slice(0, 80), ev: keep });
      bump(rec, b.cls, 'l'); cards++;
    };
    for (const ev of sec.flat) {
      if (ev.k === 'ex') { const t = topicOf(lang, ev.id); flush(t || cur || secTopic); if (t) cur = t; continue; }
      if (ev.k === 'h' || ev.k === 'box') {
        const t = topicOf(lang, ev.t.join(' '));
        if (t && (!cur || cur.id !== t.id)) { flush(cur || secTopic); cur = t; }
      }
      buf.push(ev);
    }
    flush(cur || secTopic);
  }));
}

// ── practice questions ─────────────────────────────────────────────────
const byBook = new Map(raw.books.map(b => [b.id, b]));
for (const l of raw.leaves) {
  const key = l.b.split(':')[1], lang = LANGKEY[key]; if (!lang) continue;
  const sj = subjOf[l.b.replace('cls', '')]; if (!sj) continue;
  leavesSeen++;
  const tp = topicOf(lang, [l.ex, l.head, l.instr].map(clean).join(' ')); if (!tp) continue;
  const rec = byLang[lang].get(tp.id), cls = byBook.get(l.b).cls;
  const text = clean(l.o ? l.stem : l.q[0]); if (text.length < 2) continue;
  const it = { c: cls, s: sj.id, u: l.u, h: clean(l.instr || l.head).slice(0, 200), q: [text, clean(l.q[1]).slice(0, 400), clean(l.q[2]).slice(0, 400)] };
  if (l.o && l.cor >= 0) { it.o = l.o.map(clean); it.a = l.cor; if (new Set(it.o).size !== it.o.length || it.o.length < 3 || it.o.length > 5) continue; }      // repeated options: two right answers, left out (docs/test_bank_review/repeated_options.csv lists them)
  else { const a = clean(l.a); if (a && !PLACEHOLDER.test(a) && !l.wl) it.t = (/:\s*$/.test(a) && l.st ? a + ' ' + clean(l.st) : a).slice(0, 500); else if (!a && l.st && !l.wl) it.t = clean(l.st).slice(0, 500); }
  if (l.pg != null && l.pg !== '') it.pg = l.pg;
  rec.items.push(it); bump(rec, cls, 'e'); items++;
}
// at most 40 practice questions per topic and class, those with an answer first, spread over the books
for (const m of Object.values(byLang)) for (const rec of m.values()) {
  const byC = {};
  rec.items.forEach(i => (byC[i.c] = byC[i.c] || []).push(i));
  rec.items = [];
  for (const c of Object.keys(byC).sort((a, b) => a - b)) {
    const list = byC[c].sort((a, b) => (b.o || b.t ? 1 : 0) - (a.o || a.t ? 1 : 0));
    rec.items.push(...list.slice(0, 40));
  }
}

// ── files ──────────────────────────────────────────────────────────────
const index = { schema: 'spacebook.grammar/1', source: inputsHash(), levels: { 1: 'Classes 1 and 2: the first steps', 2: 'Classes 3 to 5: easy', 3: 'Classes 6 to 8: medium', 4: 'Classes 9 and 10: harder', 5: 'Classes 11 and 12: the hardest' }, langs: {} };
const files = new Map();
for (const lang of Object.keys(byLang)) {
  const recs = [...byLang[lang].values()].filter(r => r.lessons.length || r.items.length);
  const used = new Set(); recs.forEach(r => { r.lessons.forEach(x => used.add(x.s)); r.items.forEach(x => used.add(x.s)); });
  const subjects = {};
  for (const sj of Object.values(subjOf)) if (used.has(sj.id)) subjects[sj.id] = { name: sj.name, chapters: sj.chapters };
  const topics = recs.map(r => ({ id: r.t.id, name: r.t.name, native: r.t.native, lvl: r.t.lvl, group: r.t.group, lessons: r.lessons, items: r.items }));
  const text = JSON.stringify({ v: 1, lang, subjects, topics }) + '\n';
  files.set(lang + '.json', text);
  const total = { topics: recs.length, lessons: recs.reduce((a, r) => a + r.lessons.length, 0), exercises: recs.reduce((a, r) => a + Object.values(r.cls).reduce((x, c) => x + c.e, 0), 0) };
  index.langs[lang] = { name: LANGNAME[lang], native: LANGNATIVE[lang], file: lang + '.json', h: sha(text).slice(0, 12), bytes: Buffer.byteLength(text), total,
    topics: recs.map(r => ({ id: r.t.id, name: r.t.name, native: r.t.native, lvl: r.t.lvl, group: r.t.group, cls: r.cls, lessons: r.lessons.length, exercises: Object.values(r.cls).reduce((x, c) => x + c.e, 0) })) };
}
files.set('index.json', JSON.stringify(index) + '\n');
fs.mkdirSync(OUT, { recursive: true });
for (const f of fs.readdirSync(OUT)) if (!files.has(f)) fs.unlinkSync(path.join(OUT, f));
for (const [f, text] of files) fs.writeFileSync(path.join(OUT, f), text);
console.log('wrote content/grammar: ' + cards + ' lessons, ' + items + ' practice questions (of ' + leavesSeen + ' exercise questions in the language books), ' + (Array.from(files.values()).reduce((a, t) => a + Buffer.byteLength(t), 0) / 1048576).toFixed(2) + ' MB');
for (const [l, v] of Object.entries(index.langs)) console.log('  ' + l + ': ' + v.total.topics + ' topics, ' + v.total.lessons + ' lessons, ' + v.total.exercises + ' exercises');
