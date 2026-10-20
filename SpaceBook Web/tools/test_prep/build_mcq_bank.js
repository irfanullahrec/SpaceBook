#!/usr/bin/env node
/* ======================================================================
 *  build_mcq_bank.js — one MCQ bank for "Tests Preps", built from the books
 *
 *  Every book data file in js/ is evaluated in an isolated vm context (the
 *  same loader as tools/word_stats). Two kinds of MCQ are collected:
 *    1. structured objects  { q|question, opts|options, ans|answer|correct, exp|explanation }
 *    2. book-reader blocks  { t:'q', en:'Stem? a. … b. … c. … d. …', solId } whose
 *       solution carries  answer: 'd. Cellulose'
 *  Each MCQ is tagged with class, subject and a category (english, maths,
 *  biology …). Difficulty follows the class: 1 (Class 1–3) … 5 (Class 11–12).
 *  Template filler (the same distractor set repeated on many questions) and
 *  duplicates are dropped.
 *
 *  Output: js/test_prep_bank.js  (lazy-loaded by js/test_prep.js)
 *          tools/test_prep/last_bank_report.txt
 *
 *  Run:  node --max-old-space-size=8192 tools/test_prep/build_mcq_bank.js
 * ====================================================================== */
'use strict';
const fs = require('fs');
const path = require('path');
const W = require('../word_stats/build_word_stats.js');

// ── subject → category ────────────────────────────────────────────────────
const CATEGORY = [
  [/-(eng)$/, 'english'], [/-(urdu)$/, 'urdu'], [/-(pashto)$/, 'pashto'], [/-(arabic)$/, 'arabic'],
  [/-(math)$/, 'maths'], [/-(phy)$/, 'physics'], [/-(chem)$/, 'chemistry'], [/-(bio)$/, 'biology'],
  [/-(sci|gk)$/, 'science'], [/-(comp|cs)$/, 'computer'], [/-(stat)$/, 'statistics'],
  [/-(isl)$/, 'islamiat'], [/-(quran|mq|nazira)$/, 'quran'], [/-(islopt|ikhtiari|islhist|ishist)$/, 'islamic-studies'],
  [/-(pakstudy|pak)$/, 'pakstudies'], [/-(sst|sstum|geo|hist|civics)$/, 'social'], [/-(econ)$/, 'economics'],
  [/-(hpe)$/, 'hpe'], [/-(drawing)$/, 'drawing']
];
const categoryOf = sid => { for (const [rx, c] of CATEGORY) if (rx.test(sid)) return c; return null; };
const levelOf = cls => cls <= 3 ? 1 : cls <= 5 ? 2 : cls <= 8 ? 3 : cls <= 10 ? 4 : 5;

// ── text helpers ──────────────────────────────────────────────────────────
const clean = s => String(s == null ? '' : s).replace(/\*\*(.+?)\*\*/g, '$1')
  .replace(/<br\s*\/?>/gi, ' ').replace(/<\/?(b|strong|i|em|u|sup|sub|span|small)[^>]*>/gi, m => /sup|sub/i.test(m) ? m : '')
  .replace(/<(?!\/?(sup|sub)\b)[^>]+>/gi, ' ').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();
const optText = o => typeof o === 'string' ? o : (o && (o.en || o.text || o.t || o.ur || '')) || '';
const OPT_PREFIX = /^\s*(\(?[a-dA-D]\)|[a-dA-D][.)]|\((الف|ب|ج|د)\)|(الف|ب|ج|د)[.)۔-])\s*/;
const stripOpt = s => clean(s).replace(OPT_PREFIX, '').trim();
const URDU_LETTER = { 'الف': 0, 'ا': 0, 'ب': 1, 'ج': 2, 'د': 3 };
const norm = s => stripOpt(s).toLowerCase().replace(/[^\p{L}\p{N}]+/gu, '');

function resolveAnswer(raw, opts) {
  if (raw == null || raw === '') return -1;
  if (typeof raw === 'number' && Number.isInteger(raw)) return raw >= 0 && raw < opts.length ? raw : -1;
  const s = String(raw).trim();
  if (/^\d+$/.test(s)) { const n = +s; return n < opts.length ? n : -1; }
  let m = s.match(/^\(?([a-dA-D])\)?(?:[.)\s]|$)/);
  if (m) return 'abcd'.indexOf(m[1].toLowerCase());
  m = s.match(/^\(?(الف|ب|ج|د)\)?(?:[.)\s۔]|$)/);
  if (m) return URDU_LETTER[m[1]];
  const n = norm(s);
  const hit = opts.findIndex(o => norm(o) === n);
  if (hit >= 0) return hit;
  const part = opts.findIndex(o => norm(o) && (n.includes(norm(o)) || norm(o).includes(n)));
  return part;
}

// "Stem? a. one b. two c. three d. four"  or "(a) … (b) …"
const UR_SEQ = ['الف', 'ب', 'ج', 'د'];
function splitInline(text) {
  const t = clean(text);
  const rx = /(?:^|\s)(?:\(?([a-d])[.)]|\((الف|ب|ج|د)\))\s+/g;
  const marks = [];
  let m;
  while ((m = rx.exec(t))) {
    const letter = m[1] || 'abcd'[UR_SEQ.indexOf(m[2])];
    marks.push({ letter, at: m.index + (/^\s/.test(m[0]) ? 1 : 0), end: rx.lastIndex });
  }
  // find a run a, b, c(, d) in order
  for (let i = 0; i < marks.length; i++) {
    if (marks[i].letter !== 'a') continue;
    const run = [marks[i]];
    for (let j = i + 1; j < marks.length && run.length < 4; j++) {
      if (marks[j].letter === 'abcd'[run.length]) run.push(marks[j]);
    }
    if (run.length < 3) continue;
    const stem = t.slice(0, run[0].at).trim();
    const opts = run.map((r, k) => t.slice(r.end, k + 1 < run.length ? run[k + 1].at : t.length).trim());
    if (stem.length < 6 || opts.some(o => !o || o.length > 160)) continue;
    return { stem, opts };
  }
  return null;
}

// ── collectors ────────────────────────────────────────────────────────────
const Q_KEYS = ['q', 'question', 'stem', 'qText', 'prompt', 'statement'];
const O_KEYS = ['opts', 'options', 'choices'];
const A_KEYS = ['ans', 'correct', 'answer', 'correctIndex', 'answerIndex', 'key', 'right'];
const E_KEYS = ['exp', 'explanation', 'expl', 'reason', 'rationale'];

function structured(o, wantNoKey) {
  const qk = Q_KEYS.find(k => typeof o[k] === 'string' && o[k].trim());
  const ok = O_KEYS.find(k => Array.isArray(o[k]) && o[k].length >= 3 && o[k].length <= 5);
  if (!qk || !ok) return null;
  const opts = o[ok].map(x => stripOpt(optText(x)));
  if (opts.some(x => !x)) return null;
  let a = -1;
  for (const k of A_KEYS) { if (o[k] != null) { a = resolveAnswer(o[k], o[ok].map(optText)); if (a >= 0) break; } }
  if (a < 0) return wantNoKey ? { q: clean(o[qk]).replace(/^\(?[ivx]+[.)]\s+/i, ''), o: opts, nokey: true } : null;      // a real question with no answer key: for the review queue, never in the bank
  const ek = E_KEYS.find(k => typeof o[k] === 'string' && o[k].trim());
  return {
    q: clean(o[qk]).replace(/^\(?[ivx]+[.)]\s+/i, ''), o: opts, a,
    e: ek ? clean(o[ek]) : '',
    qu: typeof o.qUrdu === 'string' ? clean(o.qUrdu) : '',
    qp: typeof o.qPashto === 'string' ? clean(o.qPashto) : ''
  };
}

function collect(value, sols, out, nokey) {
  const seen = new Set();
  (function walk(v) {
    if (!v || typeof v !== 'object' || seen.has(v)) return;
    seen.add(v);
    if (!Array.isArray(v)) {
      const s = structured(v, !!nokey);
      if (s && s.nokey) { nokey.push(s); return; }
      if (s) { out.push(s); return; }
      const sol = v.solId && sols[v.solId];
      if (sol && sol.answer != null && (typeof v.en === 'string' || typeof v.ur === 'string')) {
        const item = fromBookBlock(v, sol);
        if (item) { out.push(item); return; }
      }
    }
    for (const k of Object.keys(v)) { let x; try { x = v[k]; } catch (e) { continue; } walk(x); }
  })(value);
}

const TRUE_RX = /^(✓|✔|✔️|true|t|correct|right|yes|صحیح|درست|سم|ہاں)[.۔]?$/i;
const FALSE_RX = /^(✗|✘|×|x|false|f|wrong|incorrect|no|غلط|ناسم|نہیں)[.۔]?$/i;
const isArabicScript = s => /[؀-ۿ]/.test(s) && !/[A-Za-z]{3}/.test(s);
// a book-reader question block (or one of its parts) whose solution holds the answer
function fromBookBlock(v, sol) {
  const texts = ['en', 'ur', 'ps'].map(k => typeof v[k] === 'string' ? v[k] : '');
  const steps = (sol.steps || []).map(st => clean(st && (st.en || st.ur))).filter(x => x && !/^(agent answer|نمونے کا جواب|p\. ?\d+)\.?$/i.test(x)).join(' ');
  for (const t of texts) {
    if (!t) continue;
    const sp = splitInline(t);
    if (!sp) continue;
    const a = resolveAnswer(sol.answer, sp.opts);
    if (a < 0) continue;
    const q = sp.stem.replace(/^\(?[ivx]+[.)]\s+/i, '');
    const others = texts.filter(x => x && x !== t).map(clean);
    return {
      q, o: sp.opts, a, e: steps,
      qu: others.find(x => isArabicScript(x) && /[ٹڈڑںھہے]/.test(x)) || '',
      qp: others.find(x => isArabicScript(x) && /[ټځڅډړږښګڼېۍ]/.test(x)) || ''
    };
  }
  // true / false statements (tick ✓ the correct and cross ✗ the wrong)
  const ans = clean(sol.answer);
  const tf = TRUE_RX.test(ans) ? 0 : FALSE_RX.test(ans) ? 1 : -1;
  const stmt = clean(texts[0] || texts[1]);
  if (tf >= 0 && stmt.length >= 12 && !/\?$/.test(stmt) && !splitInline(stmt)) {
    return { q: stmt.replace(/^\(?[ivx]+[.)]\s+/i, ''), o: ['True', 'False'], a: tf, e: steps, tf: 1,
      qu: isArabicScript(clean(texts[1])) ? clean(texts[1]) : '', qp: isArabicScript(clean(texts[2])) ? clean(texts[2]) : '' };
  }
  return null;
}

function findSolutions(globals) {
  const sols = {};
  for (const [k, v] of Object.entries(globals)) {
    if (!/SOLUTIONS/i.test(k) || !v || typeof v !== 'object') continue;
    for (const [id, s] of Object.entries(v)) if (s && typeof s === 'object') {
      if (s.answer) sols[id] = s;
      else for (const [id2, s2] of Object.entries(s)) if (s2 && typeof s2 === 'object' && s2.answer) sols[id2] = s2;
    }
  }
  return sols;
}

// ── main ──────────────────────────────────────────────────────────────────
function main() {
  const D = W.loadCatalogue();
  const subjName = {};
  for (const [cid, list] of Object.entries(D.subjects)) for (const s of list) subjName[s.id] = s.name;
  const files = fs.readdirSync(W.JS).filter(f => f.endsWith('.js') && !W.SKIP_FILES.has(f) && !/reader\.js$/.test(f) &&
    !/^test_prep/.test(f)).sort();
  const all = [];
  const unkeyedAll = [];
  const report = [];
  for (const file of files) {
    const sid = W.subjectForFile(file, D.subjects);
    const keyed = W.DATA_KEY_FILES[file];
    if (!sid && !keyed) continue;
    let ev;
    try { ev = W.evaluate(file); } catch (e) { report.push('FAIL ' + file + ' ' + e.message); continue; }
    const sols = findSolutions(ev.globals);
    const groups = keyed
      ? Object.entries(ev.data).map(([k, v]) => [(/10/.test(k) ? 'cls10' : 'cls9') + '-' + keyed, v])
      : [[sid, [ev.globals, ev.data]]];
    for (const [gsid, value] of groups) {
      const found = [], nokey = [];
      collect(value, sols, found, nokey);
      const cls = +gsid.match(/^cls(\d+)/)[1];
      for (const m of found) Object.assign(m, { s: gsid, c: cls, l: levelOf(cls), k: categoryOf(gsid) });
      for (const m of nokey) Object.assign(m, { s: gsid, c: cls, f: file });
      all.push(...found.filter(m => m.k));
      unkeyedAll.push(...nokey);
      report.push(`${String(found.length).padStart(5)}  ${file} -> ${gsid}`);
    }
  }

  // template filler: the same distractors reused on many different questions
  const distractorSig = m => m.o.filter((_, i) => i !== m.a).map(norm).sort().join('|');
  const sigCount = new Map();
  for (const m of all) { const s = distractorSig(m); sigCount.set(s, (sigCount.get(s) || 0) + 1); }
  const FILLER = /completely contrary meaning|irrelevant concept|unrelated phenomenon|none of these are related/i;
  // stems that are instructions or meta questions, not questions from the lesson
  const BAD_STEM = /textbook unit does this topic belong|which unit (of the textbook|does this)|[✓✗✔✘]|نشان لگائیں|tick|encircle|choose the correct|درست جواب منتخب/i;
  const kept = [];
  const seenQ = new Set();
  let filler = 0, dup = 0, bad = 0;
  for (const m of all) {
    if (m.o.some(x => FILLER.test(x)) || (!m.tf && sigCount.get(distractorSig(m)) >= 4)) { filler++; continue; }
    if (BAD_STEM.test(m.q) || (m.tf && /_{2,}|…|\.{3}|⇨/.test(m.q))) { bad++; continue; }
    if (m.q.length < 5 || m.o.length < (m.tf ? 2 : 3) || new Set(m.o.map(norm)).size !== m.o.length) { bad++; continue; }
    const key = norm(m.q) + '#' + m.o.map(norm).sort().join('|');
    if (seenQ.has(key)) { dup++; continue; }
    seenQ.add(key);
    kept.push(m);
  }
  // stable id from content
  const hash = s => { let h = 2166136261; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return (h >>> 0).toString(36); };
  kept.sort((x, y) => x.c - y.c || (x.s < y.s ? -1 : x.s > y.s ? 1 : 0));
  const subjects = {};
  const rows = kept.map(m => {
    subjects[m.s] = subjects[m.s] || { name: subjName[m.s] || m.s, cls: m.c, cat: m.k, n: 0 };
    subjects[m.s].n++;
    const r = { i: hash(m.s + '|' + m.q + '|' + m.o.join('|')), s: m.s, q: m.q, o: m.o, a: m.a };
    if (m.e && m.e.length > 3) r.e = m.e.slice(0, 600);
    if (m.tf) r.tf = 1;
    if (m.qu && m.qu !== m.q) r.qu = m.qu;
    if (m.qp && m.qp !== m.q) r.qp = m.qp;
    return r;
  });
  const counts = {};
  for (const m of kept) {
    counts[m.k] = counts[m.k] || { n: 0, byLevel: [0, 0, 0, 0, 0, 0] };
    counts[m.k].n++; counts[m.k].byLevel[m.l]++;
  }
  // ---- review queue: what the bank leaves out for want of a key, and the subjects whose keys cluster on one position
  const queueDir = path.join(W.JS, '..', 'docs', 'test_prep_review');
  fs.mkdirSync(queueDir, { recursive: true });
  const csv = v => '"' + String(v).replace(/"/g, '""') + '"';
  const seenNoKey = new Set();
  const keyedStems = new Set(all.map(m => norm(m.q)));                        // the same question with a key in another file needs no review
  const queue = unkeyedAll.filter(m => { if (keyedStems.has(norm(m.q))) return false; const k = m.s + '#' + norm(m.q) + '#' + m.o.map(norm).sort().join('|'); if (seenNoKey.has(k)) return false; seenNoKey.add(k); return true; })
    .sort((x, y) => x.c - y.c || (x.s < y.s ? -1 : x.s > y.s ? 1 : 0) || (x.q < y.q ? -1 : 1));
  fs.writeFileSync(path.join(queueDir, 'no_key.csv'), ['subject,class,source file,question,options (A | B | C | D)'].concat(
    queue.map(m => [m.s, m.c, m.f, m.q.slice(0, 200), m.o.join(' | ')].map(csv).join(','))).join('\n') + '\n');
  const skew = [];
  for (const [sid, info] of Object.entries(subjects)) {
    const pos = [0, 0, 0, 0, 0];
    for (const m of kept) if (m.s === sid && !m.tf && m.a < 5) pos[m.a]++;
    const n = pos.reduce((x, y) => x + y, 0);
    if (n >= 20 && Math.max(...pos) / n >= 0.8) skew.push(`${sid} (${n} MCQs, ${(100 * Math.max(...pos) / n).toFixed(0)} % on option ${'ABCDE'[pos.indexOf(Math.max(...pos))]})`);
  }
  const noKeyBySubject = {};
  for (const m of queue) noKeyBySubject[m.s] = (noKeyBySubject[m.s] || 0) + 1;
  const header = '/* Generated by tools/test_prep/build_mcq_bank.js from the book data — do not edit by hand. */\n';
  fs.writeFileSync(path.join(W.JS, 'test_prep_bank.js'), header + 'window.SB_MCQ_BANK = ' + JSON.stringify({
    generated: new Date().toISOString().slice(0, 10), subjects, counts, mcqs: rows
  }) + ';\n');
  report.unshift(`kept ${kept.length} of ${all.length} (filler ${filler}, duplicates ${dup}, malformed ${bad}); review queue: ${queue.length} questions without a key (docs/test_prep_review/no_key.csv), ${skew.length} subjects with >= 80 % of the keys on one option`,
    'without a key, by subject: ' + Object.entries(noKeyBySubject).sort((a, b) => b[1] - a[1]).slice(0, 25).map(([k, v]) => k + ' ' + v).join(', '),
    'skewed: ' + (skew.join('; ') || 'none'),
    'by category: ' + Object.entries(counts).map(([k, v]) => `${k} ${v.n} [L1-5 ${v.byLevel.slice(1).join('/')}]`).join(', '), '');
  fs.writeFileSync(path.join(__dirname, 'last_bank_report.txt'), report.join('\n') + '\n');
  console.log(report.slice(0, 2).join('\n'));
}

main();
