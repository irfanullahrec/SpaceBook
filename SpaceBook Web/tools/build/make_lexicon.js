'use strict';
/* Lexicon v1 (Phase 7 foundation): the offline word meanings of the whole app in ONE generated file, built at build time.
 *   node --max-old-space-size=8192 tools/build/make_lexicon.js [--check]
 * Before, js/universal_translate.js built its offline lexicon at the first word lookup by reading the word list of every book
 * (CLSn_BOOKS[x].words), which on the lazy page loaded 106 files / 150 MB and took ~10 s. This script reads the same sources in the
 * same order, once, and writes js/lexicon_data.js (window.SB_LEXICON_V1 = {rows: [[en, ur, ps, ar], ...]}); the runtime then adds the
 * rows in that order, so the merged lexicon is the same. Exact duplicate rows are dropped (adding one twice changes nothing).
 * Sources, in order: docs/lexicon/curated/*.txt (hand-written), SB_OFFLINE_LEXICON, the word lists of every book (Classes 1-11) and of the Maths readers, ENG_URDU_DICT.
 * Not in this file: any online or machine translation. Dev-only; the output is committed and checked by tools/build/all.js. */
const fs = require('fs'), path = require('path');
const { load, ROOT } = require('../lib/app_sandbox');
const OUT = path.join(ROOT, 'js', 'lexicon_data.js');
const CHECK = process.argv.includes('--check');

const app = load({ page: 'lazy.html', quiet: true });
const rowsJson = app.run(`(() => {
  const rows = [], seen = new Set();
  const s = v => (v ? String(v) : '');          // exactly what the runtime did: String(rec[l] || '')
  const add = (en, ur, ps, ar, hint) => {
    const r = [s(en), s(ur), s(ps), s(ar), hint || ''];
    const k = r.join('\\u0001');
    if (seen.has(k)) return;
    seen.add(k); rows.push(r);
  };
  try { String(window.SB_OFFLINE_LEXICON || '').split('\\n').forEach(r => { const p = r.split('|'); if (p.length === 4) add(p[0], p[1], p[2], p[3]); }); } catch (e) { /* none */ }
  ['CLS1_BOOKS', 'CLS2_BOOKS', 'CLS3_BOOKS', 'CLS4_BOOKS', 'CLS5_BOOKS', 'CLS6_BOOKS', 'CLS7_BOOKS', 'CLS8_BOOKS', 'CLS9_BOOKS', 'CLS10_BOOKS', 'CLASS11_BOOKS'].forEach(n => {
    const lib = window[n] || {};
    Object.keys(lib).forEach(k => { const w = lib[k] && lib[k].words || {}; Object.keys(w).forEach(en => { const m = w[en] || []; add(en, m[0], m[1], '', /^(arabic|quran|nazira)$/.test(k) ? 'ar' : k === 'pashto' ? 'ps' : 'ur'); }); });
  });
  ['MATH_5_WORDS', 'MATH_6_WORDS', 'MATH_7_WORDS', 'MATH_8_WORDS', 'MATH_11_WORDS'].forEach(n => {
    let w = null; try { w = window[n] || eval(n); } catch (e) { w = null; }
    if (w) Object.keys(w).forEach(en => { const m = w[en] || []; add(en, m[0], m[1], ''); });
  });
  if (typeof ENG_URDU_DICT !== 'undefined') Object.keys(ENG_URDU_DICT).forEach(en => {
    const e = ENG_URDU_DICT[en]; if (!e) return;
    const u = e.u && e.u !== 'اردو معنی' && !/^اردو معنی/.test(e.u) ? e.u : '';
    if (u || e.p) add(en, u, e.p || '', '');
  });
  return JSON.stringify(rows);
})()`, 600000);
// Every row goes into the right language column by the script of each field (tools/offline_meanings/normalize.js)
const { normalizeRow, script } = require('../offline_meanings/normalize');
const rows = []; { const seen = new Set();
  // hand-written meanings (docs/lexicon/curated/*.txt, english|urdu|pashto|arabic per line) are the first and most general source
  const curDir = path.join(ROOT, 'docs', 'lexicon', 'curated'), cur = [];
  if (fs.existsSync(curDir)) for (const f of fs.readdirSync(curDir).filter(f => /\.txt$/.test(f)).sort())
    for (const line of fs.readFileSync(path.join(curDir, f), 'utf8').split('\n')) {
      const p = line.replace(/\r$/, "").split("|");
      if (p.length !== 4 || !/^[a-z][a-z' -]*$/.test(p[0].trim().toLowerCase())) continue;
      if (p.slice(1).some(v => /[A-Za-z]{3,}/.test(v.replace(/\([^)]*\)/g, '')))) continue;   // a target meaning in English letters: unfinished line
      cur.push([p[0].trim().toLowerCase(), p[1].trim(), p[2].trim(), p[3].trim(), 'ur']);
    }
  for (const r of cur.concat(JSON.parse(rowsJson))) {
    const n = normalizeRow(r, r[4]);
    if (!n || !(n.en || n.ur || n.ps || n.ar)) continue;
    if (n.en && !(n.ur || n.ps || n.ar)) continue;                         // an English word with no meaning in any language is not an entry
    const row = [n.en, n.ur, n.ps, n.ar], k = row.join('\u0001');
    if (seen.has(k)) continue; seen.add(k); rows.push(row);
  } }
// One row per English word: the meanings that different books gave (a book's word list, the dictionary) are joined, first source first,
// so the hover card shows "موسم، رُت" instead of whichever row happened to come first.
{ const byKey = new Map(), merged = [], overflow = [];
  const pieces = v => String(v || '').split(/[،,]\s*/).map(x => x.trim()).filter(Boolean);
  for (const r of rows) {
    const key = r[0] && /^[A-Za-z][A-Za-z' -]*$/.test(r[0]) ? r[0].toLowerCase() : '';
    if (!key) { merged.push(r); continue; }
    const cur = byKey.get(key);
    if (!cur) { const c = [r[0], pieces(r[1]), pieces(r[2]), pieces(r[3])]; byKey.set(key, c); merged.push(c); continue; }
    for (let k = 1; k <= 3; k++) for (const p of pieces(r[k])) {
      if (cur[k].includes(p)) continue;
      if (cur[k].length < 4) cur[k].push(p);
      else { const o = ['', '', '', '']; o[0] = r[0]; o[k] = p; overflow.push(o); }          // a fifth meaning stays findable (its own row), it is just not listed in the card
    }
  }
  rows.length = 0;
  for (const r of merged) rows.push(Array.isArray(r[1]) ? [r[0], r[1].join('، '), r[2].join('، '), r[3].join('، ')] : r);
  overflow.forEach(o => rows.push(o));
}
// Words of Urdu, Pashto and Arabic with their English meaning, from open sources fetched once at build time (docs/lexicon/sources/):
//   quran_words.json  word-by-word English and Urdu meanings of every word of the Qur'an (api.quran.com, tools/offline_meanings/fetch_quran_words.py)
//   native_ur.tsv / native_ps.tsv / native_ar.tsv   word <TAB> English meaning, from Wiktionary (CC BY-SA 4.0; tools/offline_meanings/extract_kaikki_native.py)
// One row per word, so every spelling of a word stays findable; they come after the book rows and the hand-written rows.
{
  const dir = path.join(ROOT, 'docs', 'lexicon', 'sources'), add = [];
  const have = new Set(rows.map(r => r.join('\u0001')));
  const q = path.join(dir, 'quran_words.json');
  if (fs.existsSync(q)) {
    const Q = JSON.parse(fs.readFileSync(q, 'utf8'));
    const top = o => Object.entries(o || {}).sort((a, b) => b[1] - a[1] || (a[0] < b[0] ? -1 : 1)).slice(0, 2).map(x => x[0]).join(', ');
    for (const w of Object.keys(Q).sort()) {
      const en = top(Q[w].en).replace(/[<>]/g, ''), ur = top(Q[w].ur);
      if (en || ur) add.push([en.length > 70 ? en.slice(0, 70) : en, ur, '', w, 'ar']);
    }
  }
  for (const [lang, col] of [['ur', 1], ['ps', 2], ['ar', 3]]) {
    const f = path.join(dir, 'native_' + lang + '.tsv');
    if (!fs.existsSync(f)) continue;
    for (const line of fs.readFileSync(f, 'utf8').split('\n')) {
      const t = line.replace(/\r$/, '').split('\t');
      if (t.length < 2 || !t[0] || !t[1]) continue;
      const r = ['', '', '', '', lang]; r[0] = t[1]; r[col] = t[0]; add.push(r);
    }
  }
  // hand-written meanings of Urdu / Pashto / Arabic words (docs/lexicon/curated_native/*.txt):  word|lang(ur,ps,ar)|english|meaning in another language (optional)|(optional)
  const natDir = path.join(ROOT, 'docs', 'lexicon', 'curated_native'), mine = [];
  if (fs.existsSync(natDir)) for (const f of fs.readdirSync(natDir).filter(f => /\.txt$/.test(f)).sort())
    for (const line of fs.readFileSync(path.join(natDir, f), 'utf8').split('\n')) {
      const t = line.replace(/\r$/, '').split('|');
      if (t.length < 3 || !t[0].trim() || !/^(ur|ps|ar)$/.test(t[1].trim()) || !t[2].trim()) continue;
      const col = { ur: 1, ps: 2, ar: 3 }[t[1].trim()], r = ['', '', '', '', t[1].trim()];
      r[0] = t[2].trim(); r[col] = t[0].trim();
      for (const extra of t.slice(3)) {                                  // a meaning in another language: its own letters say which (Pashto / Urdu / Arabic), else the first free column
        const v = extra.trim(); if (!v) continue;
        const sc = script(v), COL = { ur: 1, ps: 2, ar: 3 };
        const l = { P: 'ps', U: 'ur', R: 'ar' }[sc] || ['ur', 'ps', 'ar'].find(x => x !== t[1].trim() && !r[COL[x]]);
        if (l && l !== t[1].trim() && !r[COL[l]]) r[COL[l]] = v;
      }
      mine.push(r);
    }
  add.unshift(...mine);                                                    // hand-written rows come before the open-source ones
  let kept = 0;
  for (const r of add) {
    const n = normalizeRow(r, r[4]);
    if (!n || !(n.en && (n.ur || n.ps || n.ar))) continue;
    const row = [n.en, n.ur, n.ps, n.ar], k = row.join('\u0001');
    if (have.has(k)) continue; have.add(k); rows.push(row); kept++;
  }
  if (add.length) console.log('open-source word rows: ' + kept + ' kept of ' + add.length);
}
// Last guard: no Urdu, Pashto or Arabic column may carry English letters (a stray Latin word typed into a book's gloss)
for (let i = rows.length - 1; i >= 0; i--) {
  const r = rows[i];
  for (let k = 1; k <= 3; k++) if (r[k] && /[A-Za-z]{2,}/.test(r[k].replace(/\([^)]*\)/g, ''))) {
    r[k] = r[k].split(/[،,]\s*/).filter(p => !/[A-Za-z]{2,}/.test(p.replace(/\([^)]*\)/g, ''))).join('، ');
  }
  if (!r[1] && !r[2] && !r[3] && r[0]) rows.splice(i, 1);
}
const text = '/* GENERATED by tools/build/make_lexicon.js from the book word lists, ENG_URDU_DICT and SB_OFFLINE_LEXICON: do not edit. Rows: [English, Urdu, Pashto, Arabic], each in its own column. */\n' +
  'window.SB_LEXICON_V1 = {v: 1, rows: ' + JSON.stringify(rows) + '};\n';
if (CHECK) {
  const now = fs.existsSync(OUT) ? fs.readFileSync(OUT, 'utf8').replace(/\r\n/g, '\n') : '';
  if (now !== text) { console.log('STALE js/lexicon_data.js (' + rows.length + ' rows would be written): run node --max-old-space-size=8192 tools/build/make_lexicon.js'); process.exit(1); }
  console.log('lexicon is up to date (' + rows.length + ' rows)');
} else {
  fs.writeFileSync(OUT, text);
  const withAr = rows.filter(r => r[3]).length, withUr = rows.filter(r => r[1]).length, withPs = rows.filter(r => r[2]).length;
  console.log('wrote js/lexicon_data.js: ' + rows.length + ' rows (' + (Buffer.byteLength(text) / 1e6).toFixed(2) + ' MB); with Urdu ' + withUr + ', Pashto ' + withPs + ', Arabic ' + withAr);
}
