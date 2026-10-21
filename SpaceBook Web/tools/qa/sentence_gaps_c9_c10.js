'use strict';
/* Sentence-translation gaps for the Class 9 + 10 page books (check 5) — dev only.
 *   node tools/qa/sentence_gaps_c9_c10.js --cache <books.json> [--out <file>]
 * For every English sentence of a text block (p, h, ul items, q, box...) it asks whether a translation line exists for Urdu, Pashto and
 * Arabic: from the block itself (parallel ur / ps field) or from the stored sentence shards js/sent_data_N.js (key = SBSentKey.key).
 * Prints per-book counts and writes the sentences with no stored line (and no parallel line) to --out as TSV: book, pdf page, text. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..');
const K = require(path.join(ROOT, 'js', 'sb_sentkey.js'));
const args = process.argv.slice(2);
const opt = k => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : null; };
const data = JSON.parse(fs.readFileSync(opt('--cache'), 'utf8'));
const store = {};
for (let i = 0; i < 16; i++) { const w = {}; vm.runInNewContext(fs.readFileSync(path.join(ROOT, 'js', `sent_data_${i}.js`), 'utf8'), { window: w }); Object.assign(store, w['SB_SENT_' + i].d); }
const col = { ur: 1, ps: 2, ar: 3 };
const has = (key, lang) => { const v = store[key]; if (!v) return false; const p = v.split('\t'); return !!(p[col[lang]] && p[col[lang]] !== '-'); };
const clean = t => String(t).replace(/\$[^$]*\$/g, ' ').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
const out = [], rep = {};
function walkBlocks(blocks, bk, pg) {
  for (const b of blocks || []) {
    if (!b || typeof b !== 'object') continue;
    if (b.t === 'page') { pg.v = b.pdf; continue; }
    if (typeof b.en === 'string' && !['m', 'eq', 'svg'].includes(b.t)) {
      const txt = clean(b.en);
      if (/[A-Za-z]{3}/.test(txt) && !/^[^A-Za-z]*$/.test(txt)) {
        const hasUr = typeof b.ur === 'string' && b.ur.trim(), hasPs = typeof b.ps === 'string' && b.ps.trim();
        for (const s of K.split(txt)) {
          const key = K.key(s); if (!key) continue;
          const r = rep[bk] = rep[bk] || { sent: 0, ur: 0, ps: 0, ar: 0, none: 0 };
          r.sent++;
          const u = hasUr || has(key, 'ur'), p = hasPs || has(key, 'ps'), a = has(key, 'ar');
          if (u) r.ur++; if (p) r.ps++; if (a) r.ar++;
          if (!u || !p || !a) { r.none++; out.push(`${bk}\t${pg.v}\t${s}`); }
        }
      }
    }
    for (const k of ['blocks', 'parts', 'items', 'rows']) if (b[k] && typeof b[k] === 'object') walkBlocks(Array.isArray(b[k]) ? b[k] : [b[k]], bk, pg);
    if (b.title && typeof b.title === 'object' && typeof b.title.en === 'string') walkBlocks([{ t: 'h', en: b.title.en }], bk, pg);
  }
}
for (const cls of ['c9', 'c10']) for (const sub in data[cls]) {
  const bk = cls + '/' + sub, pg = { v: 0 }, d = data[cls][sub];
  walkBlocks(d.book.frontMatter, bk, pg);
  (d.units || []).forEach(u => (u.sections || []).forEach(s => walkBlocks(s.blocks, bk, pg)));
  walkBlocks(d.book.backMatter, bk, pg);
}
const pad = (s, n) => String(s).padEnd(n);
console.log(pad('book', 14), pad('sentences', 10), pad('ur%', 6), pad('ps%', 6), pad('ar%', 6), 'incomplete');
let T = { sent: 0, ur: 0, ps: 0, ar: 0, none: 0 };
for (const k in rep) { const r = rep[k]; for (const x in T) T[x] += r[x]; console.log(pad(k, 14), pad(r.sent, 10), pad((100 * r.ur / r.sent).toFixed(0), 6), pad((100 * r.ps / r.sent).toFixed(0), 6), pad((100 * r.ar / r.sent).toFixed(0), 6), r.none); }
console.log(pad('TOTAL', 14), pad(T.sent, 10), pad((100 * T.ur / T.sent).toFixed(0), 6), pad((100 * T.ps / T.sent).toFixed(0), 6), pad((100 * T.ar / T.sent).toFixed(0), 6), T.none);
if (opt('--out')) fs.writeFileSync(opt('--out'), out.join('\n'));
