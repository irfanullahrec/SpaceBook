'use strict';
/* Builds the stored sentence translations: js/sent_data_0.js ... js/sent_data_15.js  (read by js/universal_translate.js through js/sb_sentkey.js).
 *   node tools/offline_meanings/build_sentences.js [dir with the machine-translation .jsonl files = D:/lexsrc/mt]
 * Sources, first one wins:
 *   docs/lexicon/curated_sentences/*.txt   hand-written:  english|urdu|pashto|arabic            quality 'c'
 *   <mt dir>/sentences_mt*.jsonl            computer translation (tools/offline_meanings/mt_sentences.py), checked here   quality 'm'
 * A computer translation that fails a basic check (empty, not in Arabic script, a copy of the English, far too short or long, a repeated
 * loop) is dropped: a sentence without a stored translation falls back to the word-by-word meaning, which is shown as such.
 * Each shard: window.SB_SENT_<n> = { v: 1, d: { <key>: "<q>\t<urdu>\t<pashto>\t<arabic>" } }  with q = c or m per language ('cmm'). */
const fs = require('fs'), path = require('path');
const K = require('../../js/sb_sentkey.js');
const ROOT = path.resolve(__dirname, '..', '..');
const ARGS = process.argv.slice(2).filter(a => !a.startsWith('--'));
const CURATED_ONLY = process.argv.includes('--curated-only');          // leave out every computer-made translation (licence of the model: see docs/OFFLINE_MEANINGS.md)
const MT = ARGS[0] || 'D:/lexsrc/mt';
const arabicLetters = s => (String(s).match(/[\u0600-\u06FF]/g) || []).length;
const latinLetters = s => (String(s).replace(/\([^)]*\)/g, '').match(/[A-Za-z]/g) || []).length;

function sane(src, out, lang) {
  if (!out) return false;
  const t = out.trim();
  if (!t || arabicLetters(t) < Math.min(3, src.replace(/[^A-Za-z]/g, '').length)) return false;
  // maths, units and names may stay in Latin letters; a translation that is mostly Latin is a copy
  if (latinLetters(t) > arabicLetters(t) * 0.6 + 6) return false;
  const ratio = t.length / Math.max(1, src.length);
  if (src.length > 25 && (ratio < 0.25 || ratio > 4)) return false;
  const words = t.split(/\s+/);
  if (words.length >= 8) {                                              // a repeated 3-word run is the model looping
    const seen = new Map();
    for (let i = 0; i + 2 < words.length; i++) { const g = words.slice(i, i + 3).join(' '); seen.set(g, (seen.get(g) || 0) + 1); if (seen.get(g) >= 3) return false; }
  }
  return true;
}

const entries = new Map();        // key -> { src, ur, ps, ar, q:{ur,ps,ar} }
const put = (src, lang, text, q) => {
  const key = K.key(src); if (!key) return;
  let e = entries.get(key); if (!e) entries.set(key, e = { src, ur: '', ps: '', ar: '', q: {} });
  if (!e[lang] || (q === 'c' && e.q[lang] !== 'c')) { e[lang] = text; e.q[lang] = q; }   // hand-written text replaces a computer one; the first computer text is kept
};
// what earlier runs stored is the base (the machine-translation files are not part of the repository), so each run only adds
const had = 0;
for (let i = 0; i < K.SHARDS; i++) {
  const f = path.join(ROOT, 'js', 'sent_data_' + i + '.js');
  if (!fs.existsSync(f)) continue;
  const w = {}; new Function('window', fs.readFileSync(f, 'utf8'))(w);
  for (const [key, v] of Object.entries(w['SB_SENT_' + i].d || {})) {
    const p = v.replace(/\s*\u2047\s*/g, '"').split('\t'), e = { src: '', ur: p[1] || '', ps: p[2] || '', ar: p[3] || '', q: {} };
    ['ur', 'ps', 'ar'].forEach((l, k) => { if (p[k + 1]) e.q[l] = (p[0] || '')[k] === 'c' ? 'c' : 'm'; });
    entries.set(key, e);
  }
}
const base = entries.size;
let cur = 0, mt = 0, dropped = 0;
const curDir = path.join(ROOT, 'docs', 'lexicon', 'curated_sentences');
if (fs.existsSync(curDir)) for (const f of fs.readdirSync(curDir).filter(f => /\.txt$/.test(f)).sort()) {
  fs.readFileSync(path.join(curDir, f), 'utf8').split('\n').forEach((line, i) => {
    line = line.replace(/\r$/, ''); if (!line.trim()) return;
    const p = line.split('|');
    if (p.length !== 4) { console.log('skip ' + f + ':' + (i + 1) + ' needs 4 fields'); return; }
    ['ur', 'ps', 'ar'].forEach((l, k) => { if (p[k + 1].trim()) { put(p[0].trim(), l, p[k + 1].trim(), 'c'); cur++; } });
  });
}
if (!CURATED_ONLY && fs.existsSync(MT)) for (const f of fs.readdirSync(MT).filter(f => /^sentences_mt.*\.jsonl$/.test(f)).sort()) {
  for (const line of fs.readFileSync(path.join(MT, f), 'utf8').split('\n')) {
    if (!line.trim()) continue;
    let r; try { r = JSON.parse(line); } catch (e) { continue; }
    // the model has no curly quotes: it writes U+2047 for them
    ['ur', 'ps', 'ar'].forEach(l => { if (r[l] === undefined) return; const t = r[l].replace(/\s*⁇\s*/g, '"').trim(); if (sane(r.s, t, l)) { put(r.s, l, t, 'm'); mt++; } else dropped++; });
  }
}

const shards = Array.from({ length: K.SHARDS }, () => ({}));
let n = 0;
for (const [key, e] of entries) {
  if (!e.ur && !e.ps && !e.ar) continue;
  const q = ['ur', 'ps', 'ar'].map(l => e[l] ? (e.q[l] || 'm') : '-').join('');
  shards[K.shard(key)][key] = q + '\t' + e.ur + '\t' + e.ps + '\t' + e.ar; n++;
}
shards.forEach((d, i) => fs.writeFileSync(path.join(ROOT, 'js', 'sent_data_' + i + '.js'),
  '/* GENERATED by tools/offline_meanings/build_sentences.js: do not edit. Stored sentence translations, key = SBSentKey.key(English), value = quality letters (c = hand-written, m = computer-made, - = none), Urdu, Pashto, Arabic. */\n' +
  'window.SB_SENT_' + i + ' = ' + JSON.stringify({ v: 1, d }) + ';\n'));
const size = shards.reduce((s, d, i) => s + fs.statSync(path.join(ROOT, 'js', 'sent_data_' + i + '.js')).size, 0);
console.log('sentences', n, '(' + base + ' kept from earlier runs)', '| hand-written lines', cur, '| computer lines kept', mt, 'dropped', dropped, '|', (size / 1e6).toFixed(2), 'MB in', K.SHARDS, 'files');
