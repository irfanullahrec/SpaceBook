'use strict';
/* Word-meaning gaps for the Class 9 + 10 page books (check 4) — dev only.
 *   node --max-old-space-size=8192 tools/qa/word_gaps_c9_c10.js --cache <books.json> [--out <dir>]
 * Takes every word of every English / Urdu / Pashto text field of CLS9_BOOKS and CLS10_BOOKS (text outside $..$ maths), asks the device
 * lexicon (SBOfflineLookup, the same call the hover card makes) for a meaning in each other language and writes, per source language,
 * the words that have none, most frequent first (<out>/gaps_<lang>_<target>.txt) plus a summary table. */
const fs = require('fs'), path = require('path');
const { load } = require('../lib/app_sandbox');
const args = process.argv.slice(2);
const opt = k => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : null; };
const data = JSON.parse(fs.readFileSync(opt('--cache'), 'utf8'));
const outDir = opt('--out') || '.';
const LANGS = ['en', 'ur', 'ps'];
const freq = { en: new Map(), ur: new Map(), ps: new Map() }, perBook = {};
const PS = /[\u067c\u0681\u0685\u0689\u0693\u0696\u069a\u06ab\u06bc\u06d0\u06cd]/;
function add(text, bookKey) {
  const t = String(text).replace(/\$[^$]*\$/g, ' ').replace(/<[^>]+>/g, ' ');
  const toks = t.match(/[A-Za-z][A-Za-z'’-]*|[\u0600-\u06ff]+/g) || [];
  for (const w of toks) {
    const lang = /^[A-Za-z]/.test(w) ? 'en' : 'ur';   // Urdu/Pashto/Arabic script is classified per word below
    const L = lang === 'en' ? 'en' : (PS.test(w) ? 'ps' : 'ur');
    const k = lang === 'en' ? w.toLowerCase().replace(/^['’-]+|['’-]+$/g, '') : w;
    if (!k || (lang === 'en' && k.length < 2)) continue;
    freq[L].set(k, (freq[L].get(k) || 0) + 1);
    (perBook[bookKey] = perBook[bookKey] || { en: new Map(), ur: new Map(), ps: new Map() })[L].set(k, 1);
  }
}
function walk(o, bk) {
  if (typeof o === 'string') return;
  if (Array.isArray(o)) return o.forEach(x => walk(x, bk));
  if (o && typeof o === 'object') {
    for (const k of ['en', 'ur', 'ps', 'text']) if (typeof o[k] === 'string' && o.t !== 'svg') add(o[k], bk);
    for (const k in o) if (typeof o[k] === 'object') walk(o[k], bk);
  }
}
for (const cls of ['c9', 'c10']) for (const sub in data[cls]) { walk(data[cls][sub].units, cls + '/' + sub); walk(data[cls][sub].book, cls + '/' + sub); }
const app = load({ page: 'index.html', quiet: true });
const have = {};
for (const src of LANGS) {
  const words = [...freq[src].keys()];
  have[src] = {};
  for (const tgt of ['en', 'ur', 'ps', 'ar']) {
    if (tgt === src) continue;
    const res = JSON.parse(app.run(`(() => { const w = ${JSON.stringify(words)}; const o = new Array(w.length); for (let i = 0; i < w.length; i++) { let r = ''; try { r = SBOfflineLookup(w[i], '${src}', '${tgt}'); } catch (e) { r = ''; } o[i] = r ? 1 : 0; } return JSON.stringify(o); })()`, 900000));
    have[src][tgt] = new Map(words.map((w, i) => [w, res[i]]));
  }
}
const lines = ['source->target   types(hit/all)   tokens covered'];
for (const src of LANGS) for (const tgt in have[src]) {
  let n = 0, k = 0, tn = 0, tk = 0; const miss = [];
  for (const [w, c] of freq[src]) { n++; tn += c; if (have[src][tgt].get(w)) { k++; tk += c; } else miss.push([w, c]); }
  miss.sort((a, b) => b[1] - a[1]);
  lines.push(`${src}->${tgt}   ${k}/${n} (${(100 * k / n).toFixed(1)}%)   ${(100 * tk / tn).toFixed(1)}%`);
  fs.writeFileSync(path.join(outDir, `gaps_${src}_${tgt}.txt`), miss.map(x => x[0] + '\t' + x[1]).join('\n'));
}
console.log(lines.join('\n'));
