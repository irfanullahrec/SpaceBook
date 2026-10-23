'use strict';
/* Builds the question bank of "Create Test": content/testbank/index.json and one shard per class, content/testbank/cls<N>.json.
 *     node --max-old-space-size=8192 tools/tests/build_test_bank.js [--check] [--from leaves.json] [--report]
 * What goes in: every question or part of every exercise of every book (CLSn_BOOKS: Classes 1 to 10 and 12), as the reader shows it, with its answer where
 * the project has one (a solution record, the printed key, an answer written by us), arranged by subject, chapter and topic (the book's section the
 * item sits in); the keyed MCQs of the Tests Preps bank (js/test_prep_bank.js) that the books do not already give, for the subjects and classes whose
 * questions do not live in the books (Class 11 and the older Class 9 to 12 data) - they belong to the whole subject; and "meaning" MCQs made from the
 * word list printed with a lesson (the word, and what the book says it means). Nothing is invented: an item is a question of the books, an MCQ of the
 * project's own bank, or a word of a lesson with its printed meaning.
 * Kinds (y): mcq (one right option; marks itself), tf (true or false), fill (fill in the blank), short, long, task (an activity: write, draw, match,
 * read aloud; the paper can carry it, the test cannot mark it). A, the answer, is the option number for mcq, 0 true / 1 false for tf, else text.
 * --check fails when the files are stale. Dev-only, never shipped. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const ROOT = path.resolve(__dirname, '..', '..');
process.chdir(ROOT);
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const OUT = path.join(ROOT, 'content', 'testbank');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');

// what the files depend on: the book data (hashes in the lazy manifest), the readers that resolve answers, the catalog, the Tests Preps bank, and this builder
const lf = f => fs.readFileSync(path.join(ROOT, f), 'utf8').replace(/\r\n/g, '\n');
function inputsHash() {
  const man = JSON.parse(lf('content/lazy_manifest.json')), h = [];
  for (const f of man.files) { h.push(f.src + ':' + f.sha256); for (const a of (f.also || []).concat(f.after || [])) h.push(a.src + ':' + a.sha256); }
  for (const f of ['js/answers_extra.js', 'js/math6_reader.js', 'js/sb_mcq.js', 'content/app_catalog.json', 'js/test_prep_bank.js', 'tools/tests/build_test_bank.js', 'tools/tests/extract_leaves.js']) h.push(f + ':' + sha(lf(f)));
  return sha(h.filter(s => !s.startsWith('js/fills_data.js:')).sort().join('\n'));   // fills_data.js is made after the manifest it is listed in; nothing here depends on it
}
if (args.includes('--check')) {          // fast: the files carry the hash of what they were made from, no book is loaded
  const ixFile = path.join(OUT, 'index.json');
  if (!fs.existsSync(ixFile)) { console.log('STALE  content/testbank does not exist (node tools/tests/build_test_bank.js)'); process.exit(1); }
  const have = JSON.parse(fs.readFileSync(ixFile, 'utf8'));
  const now = inputsHash();
  if (have.source !== now) { console.log('STALE  content/testbank is older than the book data or the readers (node tools/tests/build_test_bank.js)'); process.exit(1); }
  let bad = 0;
  for (const [n, c] of Object.entries(have.classes)) { const p = path.join(OUT, c.file); if (!fs.existsSync(p) || sha(fs.readFileSync(p)).slice(0, 12) !== c.h) { console.log('STALE  content/testbank/' + c.file + ' does not match its hash'); bad++; } }
  if (bad) process.exit(1);
  console.log('fresh  testbank  (' + Object.values(have.classes).reduce((a, c) => a + c.n, 0) + ' questions)');
  process.exit(0);
}

// ── 1. what the books hold ───────────────────────────────────────────────
let raw;
if (opt('--from')) raw = JSON.parse(fs.readFileSync(opt('--from'), 'utf8'));
else {
  const { load } = require('../lib/app_sandbox');
  const extract = require('./extract_leaves');
  const app = load({ page: process.env.SB_PAGE || 'index.html', quiet: true });
  raw = JSON.parse(app.run('JSON.stringify((' + extract.toString() + ')())', 600000));
}
const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));

// subject id of each book, and the chapters the sidebar lists for it
const subjOf = {};
for (const c of catalog.classes) for (const s of c.subjects) {
  const o0 = (s.chapters[0] || {}).o || '';
  const m = /selectSubjectChapter\('(\w+)',\s*\d+,\s*'(cls\d+)'\)/.exec(o0) || (/selectMathChapter\(/.test(o0) && /-math$/.test(s.id) ? [null, 'math', c.id] : null);
  if (m) subjOf[m[2].replace('cls', '') + ':' + m[1]] = { id: s.id, name: s.name, chapters: s.chapters.map(ch => ch.t), cls: +c.id.replace('cls', ''), ur: s.ur || '' };
}

// ── 2. kinds ────────────────────────────────────────────────────────────
const ARABIC = /[؀-ۿ]/;
const T_MCQ = /choose|correct (option|answer)|select|tick|mcq|encircle|circle the correct|درست جواب|صحیح جواب|انتخاب|منتخب/i;
const T_TF = /true or false|true\/false|true.*false|✓.*✗|✗.*✓|درست.*غلط|صحیح.*غلط|درست بیان|درست جملے|سم.*ناسم|سم یا ناسم/i;
const T_FILL = /fill in|fill the|blanks?|missing (letters?|words?)|خالی جگہ|خالي ځای|ډک کړئ|ډک کړه|complete the sentence/i;
const T_SHORT = /short|brief|مختصر|لنډ/i;
const T_LONG = /long|in detail|detailed|constructed|structured|descriptive|essay|تفصیل|تفصيل|تشریح|لوی|وضاحت/i;
const T_TASK = /draw|colou?r|paste|trace|join the dots|match|circle|underline|label|cut out|read aloud|read and say|say the|ملائیں|رنگ|ڈرائنگ|لکیر|ملاوئ/i;
const FIG = /\b(figure|fig\.|diagram|picture|pictures|graph|map|chart|photo)\b|\bshown\b|given (table|figure|diagram|graph)|following (figure|picture|diagram|table|graph)|شکل|تصویر|جدول|نقشہ|انځور|نقشه/i;
const CALC_HEAD = /\b(solve|calculate|simplify|evaluate|convert|compute|work out|expand|factori[sz]e|prove|verify|add|subtract|multiply|divide|find the (value|sum|product|difference|square|cube|area|volume|perimeter|mean|median|mode)|find x|find y)\b|حل کریں|معلوم کریں|حساب|ضرب|تقسیم|جمع کریں|تفریق/i;
const LANG_HEAD = /grammar|tense|\bnouns?\b|pronoun|\bverbs?\b|adjective|adverb|plural|singular|article|preposition|conjunction|punctuat|direct|indirect|voice|phrase|clause|gerund|participle|question tag|conditional|synonym|antonym|opposite|homophone|homonym|spell|meaning|vocabulary|rewrite|rearrange|convert|change|use (the |each )?(given )?(words?|phrases?)?.{0,30}(in|to make|to form)|make sentences|قواعد|جملہ|جملے|فعل|اسم|صفت|ضمیر|مترادف|متضاد|الفاظ|معنی|واحد|جمع|مذکر|مؤنث|ګرامر|جمله|مترادف|پهٔ جمع|په جمع/i;
const PLACEHOLDER = /^(solution|model answer|sample answer|see the unit text|see the lesson|see (the )?(unit|lesson|text|chapter|page)\b.{0,40}|agent answer|answer|نمونے کا جواب|حل|جواب)\s*[.:]?$/i;
const QWORD = /^(what|who|whom|whose|when|where|why|how|which|name|define|state|give|list|explain|describe|discuss|compare|differentiate|distinguish|is|are|was|were|do|does|did|can|could|will|would|has|have|should)\b|^(کیا|کیوں|کون|کب|کہاں|کس|کیسے|کتنے|کتنی|کتنا|کیونکر|څه|څوک|ولې|چېرته|کله|څنګه|کوم|څو)\b|[?؟]\s*$|[?؟]\s*\(?[ivx]*\)?\s*$/i;
const TRUE_RX = /^(✓|✔|✔️|true|t|correct|right|yes|صحیح|درست|سم|ہاں)[.۔]?\b/i;
const FALSE_RX = /^(✗|✘|×|x|false|f|wrong|incorrect|no|غلط|ناسم|نہیں)[.۔]?\b/i;
// the books mark a word with <u>, <b> or **: the reader draws ** as bold and escapes tags, so tags become ** (a question that says "the underlined word" keeps its word) and other tags go
const clean = s => String(s == null ? '' : s).replace(/<(u|b|strong)>([\s\S]*?)<\/\1>/gi, '**$2**').replace(/<br\s*\/?>/gi, ' ').replace(/<\/?[a-z][^>]*>/gi, '').replace(/\s+/g, ' ').trim();
const norm = s => clean(s).toLowerCase().replace(/\$/g, '').replace(/[^\p{L}\p{N}]+/gu, '');
const DEFAULT_MARKS = { mcq: 1, tf: 1, fill: 1, num: 2, lang: 1, short: 3, long: 6, task: 2 };

function kindOf(l) {
  const text = clean(l.q[0]), head = clean(l.head) + ' ' + clean(l.instr), ans = clean(l.a);
  if (l.o) return l.cor >= 0 ? 'mcq' : null;                                      // an MCQ without a key can neither be marked nor printed with its answer
  if (T_TF.test(head)) return TRUE_RX.test(ans) || FALSE_RX.test(ans) ? 'tf' : (text.length >= 12 && !/[?؟]$/.test(text) ? 'task' : null);
  if (FIG.test(text) || FIG.test(head)) return 'task';
  if (T_TASK.test(head) && !T_FILL.test(head)) return 'task';
  if (T_FILL.test(head) || /_{2,}|…{1,}|\.{4,}|ـ{3,}/.test(text)) return 'fill';
  if (CALC_HEAD.test(head) && /[0-9]|\$/.test(text) && !/[?؟]$/.test(text) && text.length < 220) return 'num';
  if (l.lang && LANG_HEAD.test(head) && !/[?؟]\s*$/.test(text) && text.length < 260) return 'lang';
  if (T_LONG.test(head) || ans.length > 450 || /^(explain|describe|discuss|compare|differentiate|distinguish|derive|prove|state and|how does|why do|why does|what happens|write (a|an|about)|تفصیل|بیان کریں|لکھیں)/i.test(text)) return T_SHORT.test(head) && ans.length <= 450 && !T_LONG.test(head) ? 'short' : 'long';
  if (T_SHORT.test(head) || QWORD.test(text)) return 'short';
  if (T_MCQ.test(head)) return 'task';
  if (CALC_HEAD.test(text) && /\$|[×÷=+−]/.test(text)) return 'num';
  if (/answer|write|explain|describe|discuss|define|state|give|name|list|جواب|ځواب|لکھیں|ولیکئ/i.test(head)) return 'short';
  return 'task';
}

// ── 3. items ────────────────────────────────────────────────────────────
const books = new Map(raw.books.map(b => [b.id, b]));
const items = [];                      // {b, subject, ...}
const stat = { leaves: raw.leaves.length, dropped: 0, byKind: {}, noAnswer: 0, unmapped: new Set() };
for (const l of raw.leaves) {
  const book = books.get(l.b), sj = subjOf[l.b.replace('cls', '')];
  if (!sj) { stat.unmapped.add(l.b); continue; }
  l.a = PLACEHOLDER.test(clean(l.a)) ? '' : l.a;
  l.lang = /-(eng|urdu|pashto|arabic)$/.test(sj.id);
  const k = kindOf(l);
  const text = clean(l.o ? l.stem : l.q[0]);
  if (!k || text.length < 4) { stat.dropped++; continue; }
  const it = { s: sj.id, c: book.cls, u: l.u, p: l.p, y: k, q: text };
  if (l.q[1]) it.q2 = clean(l.o ? l.q[1].replace(/\s*[a-d][.)]\s.*$/s, '') : l.q[1]);
  if (l.q[2]) it.q3 = clean(l.o ? l.q[2].replace(/\s*[a-d][.)]\s.*$/s, '') : l.q[2]);
  if (!it.q2) delete it.q2; if (!it.q3) delete it.q3;
  if (k === 'mcq') { it.o = l.o.map(clean); it.a = l.cor; }
  else if (k === 'tf') it.a = TRUE_RX.test(clean(l.a)) ? 0 : 1;
  else if (!l.wl) {
    // a solution record keeps its answer in "answer" and the working in its steps; a lead-in such as "Solution:" means the answer is in the steps
    let a = clean(l.a), e = clean(l.st);
    if (!a && e) { a = e; e = ''; }
    else if (/:\s*$/.test(a) && e) { a = a + ' ' + e; e = ''; }
    if (a) it.a = a.slice(0, 1400);
    if (e) it.e = e.slice(0, 900);
  } /* else only a printed line for the whole question: not an answer to this part */
  if (k !== 'mcq' && k !== 'tf' && it.a === undefined) stat.noAnswer++;
  const expl = (k === 'mcq' || k === 'tf') ? clean(l.st).slice(0, 700) : '';
  if (expl) it.e = expl;
  const instr = clean(l.instr || l.head).slice(0, 160);
  if (instr && instr !== text) it.h = instr;
  if (l.pg != null && l.pg !== '') it.pg = l.pg;
  if (l.ex) it.x = l.ex;
  items.push(it);
  stat.byKind[k] = (stat.byKind[k] || 0) + 1;
}

// the questions of a subject that the books do not hold (Class 11, the older Class 9 to 12 data): the keyed MCQs of the Tests Preps bank
const bank = (() => { const w = {}; new Function('window', fs.readFileSync(path.join(ROOT, 'js', 'test_prep_bank.js'), 'utf8'))(w); return w.SB_MCQ_BANK; })();
const have = new Set(items.filter(i => i.y === 'mcq').map(i => i.s + '#' + norm(i.q)));
const subjectsWithBooks = new Set(items.map(i => i.s));
let legacy = 0;
for (const m of bank.mcqs) {
  if (have.has(m.s + '#' + norm(m.q))) continue;
  const cls = +m.s.match(/^cls(\d+)/)[1];
  const it = { s: m.s, c: cls, u: -1, p: -1, y: m.tf ? 'tf' : 'mcq', q: clean(m.q) };
  if (m.tf) it.a = m.a; else { it.o = m.o.map(clean); it.a = m.a; }
  if (m.e) it.e = m.e;
  if (m.qu) it.q2 = m.qu; if (m.qp) it.q3 = m.qp;
  items.push(it); legacy++;
}

// "meaning" MCQs from the word list printed with a book: the word, and what the book says it means (Urdu for the English books, English for the Urdu books)
let meanings = 0;
for (const b of raw.books) {
  const sj = subjOf[b.id.replace('cls', '')]; if (!sj || !b.words || b.words.length < 8) continue;
  const lang = b.langs[0] === 'en' ? 'Urdu' : 'English';
  const list = b.words.filter(w => w[1] && String(w[1]).length <= 70 && clean(w[0]).length <= 40);
  const seenW = new Set();
  list.forEach((w, i) => {
    const word = clean(w[0]), right = clean(w[1]);
    if (!word || !right || seenW.has(norm(word))) return; seenW.add(norm(word));
    const pool = list.filter((x, j) => j !== i && norm(x[1]) !== norm(right));
    const opts = [right]; let k = (i * 7 + 3) % pool.length, tries = 0;
    while (opts.length < 4 && tries++ < pool.length) { const d = clean(pool[k % pool.length][1]); if (!opts.some(o => norm(o) === norm(d))) opts.push(d); k += 5; }
    if (opts.length < 4) return;
    const at = (i * 5 + 1) % 4; opts.splice(at, 0, opts.shift());       // the right option moves to a fixed but varied place
    items.push({ s: sj.id, c: b.cls, u: -1, p: -1, y: 'mcq', q: 'What is the meaning of “' + word + '” in ' + lang + '?', o: opts, a: at, h: 'Meaning of words' });
    meanings++;
  });
}

// the topic of a question: the lesson section of its chapter that shares the most (rare) words with it; none when the match is weak
const STOP = new Set('the and for with are was were been that this these those its not can may will shall has have had does did their they them you your our his her than then there such from which what who whom how why when where also into out all any each one two'.split(' '));
const tok = t => [...new Set((clean(t).toLowerCase().match(/[\p{L}\p{N}]{3,}/gu) || []).filter(w => !STOP.has(w)))];
const NOT_TOPIC = /outcome|key points|summary|review|exercise|glossary|reference|revision|intro(duction)? to this/i;
const topicsOf = {};                     // subject -> unit -> [{t, words:Set}]
for (const b of raw.books) {
  const sj = subjOf[b.id.replace('cls', '')]; if (!sj) continue;
  const df = new Map(); let nDocs = 0;
  const per = b.units.map(u => u.secs.map((sec, si) => ({ si, t: sec.t, ok: !sec.ex && !NOT_TOPIC.test(sec.t) && !NOT_TOPIC.test(sec.id) && sec.text.length > 80, w: new Set(tok(sec.text)) })).filter(x => x.ok));
  per.forEach(list => list.forEach(x => { nDocs++; x.w.forEach(w => df.set(w, (df.get(w) || 0) + 1)); }));
  const idf = w => Math.log(1 + nDocs / (df.get(w) || 1));
  topicsOf[sj.id] = { per, idf };
}
let topicHits = 0;
for (const it of items) {
  if (it.u < 0 || !topicsOf[it.s]) continue;
  const { per, idf } = topicsOf[it.s], list = per[it.u] || [];
  if (list.length < 2) { it.p = list.length === 1 ? 0 : -1; continue; }
  const words = tok(it.q + ' ' + (it.o || []).join(' ') + ' ' + (typeof it.a === 'string' ? it.a : '') + ' ' + (it.e || ''));
  const total = words.reduce((a, w) => a + idf(w), 0);
  let best = -1, bestScore = 0, hits = 0;
  list.forEach((tp, i) => { let sc = 0, n = 0; for (const w of words) if (tp.w.has(w)) { sc += idf(w); n++; } if (sc > bestScore) { bestScore = sc; best = i; hits = n; } });
  it.p = best >= 0 && hits >= 2 && bestScore / (total || 1) >= 0.3 ? best : -1;
  if (it.p >= 0) topicHits++;
}

// ── 4. subjects, chapters, shards ───────────────────────────────────────
const subjects = {};
for (const c of catalog.classes) for (const s of c.subjects) subjects[s.id] = { cls: +c.id.replace('cls', ''), name: s.name, ur: s.ur || '', chapters: s.chapters.map(ch => ({ t: ch.t, o: ch.o })), n: 0 };
for (const b of raw.books) {
  const sj = subjOf[b.id.replace('cls', '')]; if (!sj) continue;
  subjects[sj.id].langs = b.langs;
  subjects[sj.id].units = b.units.length;
  subjects[sj.id].topics = topicsOf[sj.id].per.map(list => list.map(x => x.t));
}
const id = it => crypto.createHash('sha1').update(it.s + '|' + it.u + '|' + it.y + '|' + it.q + '|' + (it.o || []).join('|')).digest('base64url').slice(0, 8);
const seen = new Set(); const finalItems = [];
// a multiple-choice question whose options repeat (two "8,888") has two right answers: it is left out and listed for the owner to correct in the book
const repeated = [];
for (const it of items) {
  const key =it.s + '#' + it.y + '#' + norm(it.q) + '#' + (it.o ? it.o.map(norm).sort().join('|') : '');
  if (seen.has(key)) continue; seen.add(key);
  if (it.y === 'mcq' && (it.o.length < 3 || it.o.length > 5 || new Set(it.o.map(norm)).size !== it.o.length)) { repeated.push([it.s, it.c, it.u, it.q, it.o.join(' | ')]); continue; }
  it.i = id(it); finalItems.push(it);
}
finalItems.sort((a, b) => a.c - b.c || (a.s < b.s ? -1 : a.s > b.s ? 1 : 0) || a.u - b.u || a.p - b.p);
const shards = {};
for (const it of finalItems) (shards[it.c] = shards[it.c] || []).push(it);
const index = { schema: 'spacebook.testbank/1', source: inputsHash(), kinds: Object.keys(DEFAULT_MARKS), marks: DEFAULT_MARKS, classes: {}, subjects: {} };
const files = new Map();
for (const [c, list] of Object.entries(shards)) {
  const subj = {};
  for (const it of list) { const sj = subjects[it.s]; (subj[it.s] = subj[it.s] || { name: sj.name, ur: sj.ur, langs: sj.langs || ['en', 'ur', 'ps'], chapters: sj.chapters.map(ch => ch.t), topics: sj.topics || [], units: sj.units }); }
  const text = JSON.stringify({ v: 1, cls: +c, subjects: subj, items: list }) + '\n';
  files.set('cls' + c + '.json', text);
  index.classes[c] = { file: 'cls' + c + '.json', h: sha(text).slice(0, 12), bytes: Buffer.byteLength(text), n: list.length };
}
for (const it of finalItems) {
  const S = index.subjects[it.s] = index.subjects[it.s] || { cls: it.c, name: subjects[it.s].name, ur: subjects[it.s].ur, chapters: {}, whole: {}, n: {} };
  const bucket = it.u >= 0 ? (S.chapters[it.u] = S.chapters[it.u] || {}) : S.whole;
  bucket[it.y] = (bucket[it.y] || 0) + 1;
  S.n[it.y] = (S.n[it.y] || 0) + 1;
}
const names = Object.keys(index.subjects); index.subjects = Object.fromEntries(names.sort().map(k => [k, index.subjects[k]]));
files.set('index.json', JSON.stringify(index) + '\n');

{
  fs.mkdirSync(OUT, { recursive: true });
  const reviewDir = path.join(ROOT, 'docs', 'test_bank_review');
  fs.mkdirSync(reviewDir, { recursive: true });
  const csv = v => '"' + String(v).replace(/"/g, '""') + '"';
  fs.writeFileSync(path.join(reviewDir, 'repeated_options.csv'), ['subject,class,chapter number,question,options'].concat(repeated.map(r => [r[0], r[1], r[2] + 1, r[3].slice(0, 200), r[4]].map(csv).join(','))).join('\n') + '\n');
  for (const f of fs.readdirSync(OUT)) if (!files.has(f)) fs.unlinkSync(path.join(OUT, f));
  for (const [f, text] of files) fs.writeFileSync(path.join(OUT, f), text);
  console.log('wrote content/testbank: ' + finalItems.length + ' questions in ' + names.length + ' subjects, ' + (Array.from(files.values()).reduce((a, t) => a + Buffer.byteLength(t), 0) / 1048576).toFixed(1) + ' MB');
}
{
  const k = {}; finalItems.forEach(i => { k[i.y] = (k[i.y] || 0) + 1; });
  console.log('by kind:', JSON.stringify(k), '| topic found for', topicHits, '| word-meaning MCQs', meanings, '| leaves read', stat.leaves, '| dropped', stat.dropped, '| from the Tests Preps bank', legacy, '| without an answer', stat.noAnswer);
  if (stat.unmapped.size) console.log('books without a subject id in the catalog:', [...stat.unmapped].join(', '));
  const bad = []; for (const b of raw.books) { const sj = subjOf[b.id.replace('cls', '')]; if (sj && sj.chapters.length !== b.units.length) bad.push(b.id + ' (' + b.units.length + ' units, ' + sj.chapters.length + ' chapters)'); }
  if (bad.length) console.log('chapter list differs from the unit list: ' + bad.join(', '));
}
