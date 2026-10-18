#!/usr/bin/env node
/* ======================================================================
 *  build_word_stats.js — project-wide vocabulary index for "Project Stats"
 *
 *  Loads every book data file in js/ inside an isolated vm context, walks
 *  all string values (skipping ids, paths, styles, figures and other
 *  metadata keys), strips HTML / LaTeX / numbers / equations and splits
 *  the text into words of four languages:
 *      en  — Latin-script words (lower-cased)
 *      ur  — Urdu        ps — Pashto        ar — Arabic
 *  Arabic-script words are normalised (NFKC, harakat / tatweel / Quranic
 *  marks removed) and classified by their own distinctive letters, then by
 *  the language of the sentence they appear in.
 *
 *  Output (both lazy-loaded by js/word_stats.js, so they work on file://):
 *    js/word_stats_summary.js  — counts per project / class / subject
 *    js/word_stats_words.js    — word lists (frequency order) + per-scope
 *                                membership (delta-encoded base-36 indices)
 *
 *  Run:  node tools/word_stats/build_word_stats.js
 * ====================================================================== */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.resolve(__dirname, '..', '..');
const JS = path.join(ROOT, 'js');

// ── subject catalogue from data.js ────────────────────────────────────────
function loadCatalogue() {
  const ctx = { console };
  ctx.window = ctx;
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(JS, 'data.js'), 'utf8') + ';this.__D=DATA;', ctx, { timeout: 20000 });
  return ctx.__D;
}

// ── file → class / subject ────────────────────────────────────────────────
const SKIP_FILES = new Set([
  'app.js', 'auth.js', 'data.js', 'dictionary_data.js', 'universal_translate.js', 'continue_learning.js',
  'reader_tools.js', 'structure_harmonizer.js', 'primary_page_learning.js', 'primary_page_art.js',
  'math_primary_visuals.js', 'english_10_source_review.js', 'word_stats.js', 'word_stats_summary.js',
  'word_stats_words.js'
]);
const LEGACY = {
  'bio_data.js': 'cls9-bio', 'english_data.js': 'cls9-eng', 'math_data.js': 'cls9-math',
  'urdu_data.js': 'cls9-urdu', 'islamyat_data.js': 'cls9-isl', 'pakstudy_data.js': 'cls9-pakstudy',
  'data_comp.js': 'cls9-comp', 'english_1_pages.js': 'cls1-eng', 'math_3_book_text.js': 'cls3-math'
};
// files that put several classes into DATA.<key>
const DATA_KEY_FILES = { 'data_chem.js': 'chem', 'data_phys.js': 'phy', 'data_bio.js': 'bio', 'data_eng.js': 'eng' };
const PREFIX = [
  ['social_studies_um', 'sstum'], ['social_studies', 'sst'], ['general_science', 'sci'],
  ['islamiat_ikhtiari', 'islopt'], ['islamic_history', 'islhist'], ['mutalia_quran', 'quran'],
  ['islamyat', 'isl'], ['islamiat', 'isl'], ['isl', 'isl'], ['ikhtiari', 'ikhtiari'], ['ishist', 'ishist'],
  ['english', 'eng'], ['eng', 'eng'], ['urdu', 'urdu'], ['math', 'math'], ['gk', 'gk'], ['nazira', 'nazira'],
  ['pashto', 'pashto'], ['drawing', 'drawing'], ['computer', 'comp'], ['cs', 'cs'], ['geography', 'geo'],
  ['history', 'hist'], ['hpe', 'hpe'], ['arabic', 'arabic'], ['mq', 'mq'], ['quran', 'quran'],
  ['pakstudy', 'pakstudy'], ['civics', 'civics'], ['economics', 'econ'], ['stat', 'stat'],
  ['chemistry', 'chem'], ['chem', 'chem'], ['physics', 'phy'], ['phys', 'phy'], ['biology', 'bio'], ['bio', 'bio']
];
const ALIASES = { 'cls12-pakstudy': 'cls12-pak', 'cls12-comp': 'cls12-comp', 'cls11-comp': 'cls11-cs' };

function subjectForFile(file, subjects) {
  if (LEGACY[file]) return LEGACY[file];
  const m = file.match(/^([a-z_]+?)_(\d{1,2})(?:_|\.)/);
  if (!m) return null;
  const [, stem, num] = m;
  const pre = PREFIX.find(([p]) => stem === p);
  if (!pre) return null;
  let id = 'cls' + num + '-' + pre[1];
  id = ALIASES[id] || id;
  const list = (subjects['cls' + num] || []).map(s => s.id);
  return list.includes(id) ? id : null;
}

// ── value walker ──────────────────────────────────────────────────────────
const SKIP_KEY = /^(id|ids|.*Id|.*Ids|uid|key|keys|ref|refs|slug|type|kind|status|layout|align|dir|lang|style|styles|css|class|cls|className|color|colour|colors|bg|background|icon|emoji|src|img|image|images|imgs|pic|photo|file|files|path|paths|href|url|urls|link|links|pdf|scan|scans|svg|fig|figs|figure|figures|art|draw|audio|video|videos|youtube|font|tag|tags|template|html_class|width|height|w|h|x|y|cx|cy|r|d|points|viewBox|fill|stroke|transform|shape|formula|latex|tex|katex|math|equation|equations|expr|expression|code|regex|pattern|version|v|hash|checksum|source|sourceFile|sourcePages|page_ref|pageRef|scanRef|anchor|badge|badgeClass|headerColor|grid|cells|position|pos)$/;

function walk(value, onText, key, seen) {
  if (value == null) return;
  const t = typeof value;
  if (t === 'string') { onText(value); return; }
  if (t !== 'object') return;
  if (seen.has(value)) return;
  seen.add(value);
  if (Array.isArray(value)) { for (const v of value) walk(v, onText, key, seen); return; }
  for (const k of Object.keys(value)) {
    if (SKIP_KEY.test(k)) continue;
    let v;
    try { v = value[k]; } catch (e) { continue; }
    walk(v, onText, k, seen);
  }
}

// ── text → words ──────────────────────────────────────────────────────────
const RX_PS = /[ټځڅډړږښګڼۍېۉ]/;
const RX_UR = /[ٹڈڑںھہۂےۓ]/;
const RX_AR_ONLY = /[ةكىإأ]/;    // ة ك ى إ أ (أ/إ are rare in Urdu & Pashto spelling)
const RX_HARAKAT = /[ً-ٰٟ]/g;
const AR_LETTERS = 'ء-غف-يٱ-ۓەۮۯۺ-ۿݐ-ݿ';
const RX_AR_WORD = new RegExp('[' + AR_LETTERS + '\\u064B-\\u065F\\u0670\\u0640\\u06D6-\\u06ED\\u200C]+', 'g');
const RX_LAT_WORD = /[A-Za-z]+(?:['’][A-Za-z]+)*/g;
const RX_ROMAN = /^[ivx]{2,}$/;

function cleanText(s) {
  if (!s || s.length < 2) return '';
  if (/^data:|^https?:\/\/\S+$|^[\w./\\-]+\.(png|jpe?g|gif|svg|webp|pdf|js|json|css|html|mp4|mp3|jfif)$/i.test(s)) return '';
  // ids / codes without spaces such as "u1-s2", "cls9-math", "ex_3_1"
  if (!/\s/.test(s) && /[\d_\/\\.:=#]/.test(s) && /[A-Za-z]/.test(s) && !/[؀-ۿ]/.test(s)) return '';
  let t = s;
  t = t.replace(/<(script|style|svg|math)\b[\s\S]*?<\/\1>/gi, ' ');
  t = t.replace(/<[^>]*>/g, ' ');
  t = t.replace(/&[a-z]+;|&#\d+;|&#x[0-9a-f]+;/gi, ' ');
  t = t.replace(/\$\$[\s\S]*?\$\$/g, ' ').replace(/\$[^$\n]{0,400}\$/g, ' ');
  t = t.replace(/\\\([\s\S]*?\\\)/g, ' ').replace(/\\\[[\s\S]*?\\\]/g, ' ');
  t = t.replace(/\\[A-Za-z]+(\{[^{}]*\})*/g, ' ');
  t = t.replace(/https?:\/\/\S+|www\.\S+/g, ' ');
  t = t.replace(/\S+@\S+\.\S+/g, ' ');
  // tokens that mix letters with digits/operators are equations or codes: x2, 3x, a+b=c, H2O
  t = t.replace(/\S*[A-Za-z]\S*[0-9=+^*\/<>_{}|]\S*|\S*[0-9=+^*\/<>_{}|]\S*[A-Za-z]\S*/g, m => /\s/.test(m) ? m : ' ');
  return t;
}

function sentenceLang(t) {
  const ps = (t.match(/[ټځڅډړږښګڼۍېۉ]/g) || []).length * 3;
  const ur = (t.match(/[ٹڈڑںھہۂےۓ]/g) || []).length * 2;
  const ar = (t.match(/[ةكىإأ]/g) || []).length * 2 + ((t.match(RX_HARAKAT) || []).length > 6 ? 4 : 0);
  const best = Math.max(ps, ur, ar);
  if (best === 0) return null;
  if (best === ps) return 'ps';
  if (best === ur) return 'ur';
  return 'ar';
}

function normArabic(w) {
  return w.normalize('NFKC')
    .replace(/[ً-ٰٟـۖ-ۭ‌]/g, '')
    .replace(/[ٱ]/g, 'ا');
}

function tokenize(text, fileLang, add) {
  const t = cleanText(text);
  if (!t) return;
  let m;
  RX_LAT_WORD.lastIndex = 0;
  while ((m = RX_LAT_WORD.exec(t))) {
    const raw = m[0];
    if (raw.length === 1 && !/^[aAI]$/.test(raw)) continue;
    if (/[a-z][A-Z]/.test(raw)) continue; // camelCase identifiers
    const w = raw.toLowerCase().replace(/’/g, "'");
    if (RX_ROMAN.test(w)) continue;
    if (w.includes("'")) {
      // primes and labels such as a'b, a'b'c'd, x'y are notation, not words (keep don't, o'clock, i'm, it's)
      const parts = w.split("'");
      if (parts[0].length === 1 && !/^[oiy]$/.test(parts[0])) continue;
      if (parts.slice(1).some(p => p.length === 1 && !/^[sdmt]$/.test(p))) continue;
    }
    add('en', w);
  }
  if (!/[؀-ۿﭐ-﻿]/.test(t)) return;
  const tn = t.normalize('NFKC');
  const ctxLang = sentenceLang(tn) || fileLang;
  RX_AR_WORD.lastIndex = 0;
  while ((m = RX_AR_WORD.exec(tn))) {
    const raw = m[0];
    const w = normArabic(raw);
    if (!w || w.length < 1) continue;
    if (w.length === 1 && !/[وبکہءیاﻭ]/.test(w)) continue;
    let lang;
    if (RX_PS.test(w)) lang = 'ps';
    else if (RX_UR.test(w)) lang = 'ur';
    else if (RX_AR_ONLY.test(w)) lang = 'ar';
    else if ((raw.match(RX_HARAKAT) || []).length >= 2 && ctxLang !== 'ps') lang = 'ar';
    else lang = ctxLang;
    add(lang, w);
  }
}

// subjects written mainly in one Arabic-script language
function fileLangFor(subjId) {
  if (!subjId) return 'ur';
  if (/-pashto$/.test(subjId)) return 'ps';
  if (/-(arabic|nazira)$/.test(subjId)) return 'ar';
  return 'ur';
}

// ── file evaluation ───────────────────────────────────────────────────────
// files that extend chapters created by another file
const DEPENDS = { 'chemistry_10_source_data.js': 'data_chem.js', 'physics_10_source_data.js': 'data_phys.js' };

function evaluate(file) {
  const dep = DEPENDS[file] ? fs.readFileSync(path.join(JS, DEPENDS[file]), 'utf8') + '\n;\n' : '';
  const src = dep + fs.readFileSync(path.join(JS, file), 'utf8');
  const dataObj = {};
  const ctx = { console: { log() {}, warn() {}, error() {}, info() {} }, DATA: dataObj, setTimeout() {}, clearTimeout() {} };
  ctx.window = ctx; ctx.self = ctx; ctx.globalThis = ctx;
  ctx.document = { addEventListener() {}, querySelector() { return null; }, querySelectorAll() { return []; }, getElementById() { return null; }, createElement() { return { style: {}, setAttribute() {}, appendChild() {} }; }, head: { appendChild() {} }, body: { appendChild() {} } };
  ctx.addEventListener = () => {};
  vm.createContext(ctx);
  const before = new Set(Object.getOwnPropertyNames(ctx));
  const names = new Set();
  for (const mm of src.matchAll(/^(?:const|let|var)\s+([A-Za-z_$][\w$]*)/gm)) names.add(mm[1]);
  const exportExpr = '\n;this.__ws = {' + [...names].map(n => `${JSON.stringify(n)}: (typeof ${n} !== 'undefined' ? ${n} : undefined)`).join(',') + '};';
  vm.runInContext(src + exportExpr, ctx, { timeout: 120000, filename: file });
  const out = { globals: {}, data: dataObj };
  for (const k of Object.getOwnPropertyNames(ctx)) {
    if (before.has(k) || k === '__ws') continue;
    out.globals[k] = ctx[k];
  }
  Object.assign(out.globals, ctx.__ws || {});
  return out;
}

// ── main ──────────────────────────────────────────────────────────────────
function main() {
  const D = loadCatalogue();
  const subjects = D.subjects;
  const classOf = id => id.split('-')[0];

  const LANGS = ['en', 'ur', 'ps', 'ar'];
  const freq = { en: new Map(), ur: new Map(), ps: new Map(), ar: new Map() };
  const scopeSets = new Map(); // subjId -> {en:Set,...}
  const setsFor = sid => {
    if (!scopeSets.has(sid)) scopeSets.set(sid, { en: new Set(), ur: new Set(), ps: new Set(), ar: new Set() });
    return scopeSets.get(sid);
  };
  const feed = (sid, value) => {
    const sets = setsFor(sid);
    const fl = fileLangFor(sid);
    walk(value, txt => tokenize(txt, fl, (lang, w) => {
      freq[lang].set(w, (freq[lang].get(w) || 0) + 1);
      sets[lang].add(w);
    }), '', new Set());
  };

  const files = fs.readdirSync(JS).filter(f => f.endsWith('.js') && !SKIP_FILES.has(f) && !/reader\.js$/.test(f)).sort();
  const report = [];
  for (const file of files) {
    let sid = subjectForFile(file, subjects);
    const keyed = DATA_KEY_FILES[file];
    if (!sid && !keyed) { report.push('SKIP (no subject) ' + file); continue; }
    let ev;
    try { ev = evaluate(file); } catch (e) { report.push('FAIL ' + file + ': ' + String(e && e.message || e).slice(0, 160)); continue; }
    if (keyed) {
      for (const [k, v] of Object.entries(ev.data)) {
        const cls = /10/.test(k) ? 'cls10' : 'cls9';
        feed(cls + '-' + keyed, v);
        report.push('ok   ' + file + ' DATA.' + k + ' -> ' + cls + '-' + keyed);
      }
      continue;
    }
    const vals = [...Object.values(ev.globals), ev.data];
    feed(sid, vals);
    report.push('ok   ' + file + ' -> ' + sid + ' (' + Object.keys(ev.globals).join(',') + (Object.keys(ev.data).length ? ' DATA.' + Object.keys(ev.data).join(',DATA.') : '') + ')');
  }

  // global word order: frequency desc, then alphabetical
  const words = {}, index = {};
  for (const L of LANGS) {
    words[L] = [...freq[L].entries()].sort((a, b) => b[1] - a[1] || (a[0] < b[0] ? -1 : 1));
    index[L] = new Map(words[L].map(([w], i) => [w, i]));
  }
  const enc = arr => { let prev = -1; return arr.map(i => { const d = i - prev; prev = i; return d.toString(36); }).join(','); };
  const scopeEntry = setsMap => {
    const o = {};
    for (const L of LANGS) o[L] = enc([...setsMap[L]].map(w => index[L].get(w)).sort((a, b) => a - b));
    return o;
  };
  const counts = setsMap => {
    const c = {};
    for (const L of LANGS) c[L] = setsMap[L].size;
    c.all = LANGS.reduce((s, L) => s + c[L], 0);
    return c;
  };

  // class scopes = union of subject scopes
  const classSets = new Map();
  for (const [sid, sets] of scopeSets) {
    const cid = classOf(sid);
    if (!classSets.has(cid)) classSets.set(cid, { en: new Set(), ur: new Set(), ps: new Set(), ar: new Set() });
    const cs = classSets.get(cid);
    for (const L of LANGS) for (const w of sets[L]) cs[L].add(w);
  }

  const summary = { generated: new Date().toISOString().slice(0, 10), project: {}, classes: {}, subjects: {} };
  summary.project = {};
  for (const L of LANGS) summary.project[L] = words[L].length;
  summary.project.all = LANGS.reduce((s, L) => s + summary.project[L], 0);
  for (const [cid, sets] of classSets) summary.classes[cid] = counts(sets);
  for (const [sid, sets] of scopeSets) summary.subjects[sid] = counts(sets);

  const wordsOut = { words: {}, freq: {}, scopes: {} };
  for (const L of LANGS) {
    wordsOut.words[L] = words[L].map(([w]) => w).join('\n');
    wordsOut.freq[L] = words[L].map(([, n]) => n.toString(36)).join(',');
  }
  for (const [cid, sets] of classSets) wordsOut.scopes[cid] = scopeEntry(sets);
  for (const [sid, sets] of scopeSets) wordsOut.scopes[sid] = scopeEntry(sets);

  const header = '/* Generated by tools/word_stats/build_word_stats.js — do not edit by hand. */\n';
  fs.writeFileSync(path.join(JS, 'word_stats_summary.js'), header + 'window.SB_WORD_STATS_SUMMARY = ' + JSON.stringify(summary) + ';\n');
  fs.writeFileSync(path.join(JS, 'word_stats_words.js'), header + 'window.SB_WORD_STATS_WORDS = ' + JSON.stringify(wordsOut) + ';\n');
  fs.writeFileSync(path.join(__dirname, 'last_build_report.txt'), report.join('\n') + '\n');
  console.log(report.filter(l => !l.startsWith('ok')).join('\n'));
  console.log('project', JSON.stringify(summary.project));
  for (const [cid, c] of Object.entries(summary.classes)) console.log(cid, JSON.stringify(c));
}

if (require.main === module) main();
module.exports = { loadCatalogue, subjectForFile, evaluate, SKIP_FILES, DATA_KEY_FILES, JS };
