'use strict';
/* Orders the book's English sentences by how useful a stored translation is, for tools/offline_meanings/mt_sentences.py.
 *   node tools/offline_meanings/make_sentence_queue.js <sent.json from tools/word_stats/dump_sentences.js> <out.json> */
const fs = require('fs');
const ALL = process.argv.includes('--all');                              // --all: also the sentences whose Urdu and Pashto the book already has (for the Arabic pass)
const MAXCLS = +((process.argv.find(a => a.startsWith('--max-class=')) || '').split('=')[1] || 12);
const rows = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const META = /native review|authored solution|learning enhancement|learning answer|retained as printed|printed answer|draft:|source comparison|worked and checked|section headings given|cut edge|textbook prints|textbook question|transcrib|obscured|printed page|unresolved|watermark|scan\b|pdf\b|page \d|complete worked answers|source (page|image)|unclear|not reconstructed|illegible|cropped|faded|JPG|printed p\./i;
const clsNum = c => +String(c).replace('cls', '');
const out = [];
for (const r of rows) {
  const s = r.s, w = s.split(' ').length;
  if (r.t === r.n && !ALL) continue;                                             // every place it occurs already carries a real Urdu and Pashto translation from the book
  if (w < 3 || w > 45 || s.length > 330 || META.test(s)) continue;
  const letters = (s.match(/[A-Za-z]/g) || []).length;
  if (letters / s.length < 0.72) continue;
  if (/[=<>_{}\|^~]/.test(s) || /\b\d+\.\d+\.\d+\b/.test(s)) continue;
  if (!/[A-Za-z]{3}/.test(s) || /^[(\[]?[a-z0-9]{1,3}[)\].]/.test(s) && w < 5) continue;
  const lo = Math.min(...r.c.map(clsNum));
  if (lo > MAXCLS) continue;
  out.push({ s, n: r.n, lo, w });
}
// youngest class first; inside a class the sentences read most often (and the ordinary prose of 6-25 words) first
out.sort((a, b) => a.lo - b.lo || (Math.abs(a.w - 14) - Math.abs(b.w - 14)) * 0.02 - (a.n - b.n) * 0.5 || (a.s < b.s ? -1 : 1));
fs.writeFileSync(process.argv[3], JSON.stringify(out.map(x => x.s)));
const by = {}; out.forEach(x => by[x.lo] = (by[x.lo] || 0) + 1);
console.log('queue', out.length, JSON.stringify(by));
