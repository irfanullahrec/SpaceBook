'use strict';
/* Lists English sentences of a data file that differ locally from the book's Word (OCR) text.
 * A sentence is flagged when most of its word 4-grams occur in the Word text but some do not
 * (so the sentence is in the book and a word differs). Each hit is either an OCR slip in the Word
 * file or a real difference in the data; only these need a look at the scan.
 *   node tools/qa/vs_word.js js/english_12_data.js word.txt */
const fs = require('fs');
const toks = s => s.toLowerCase().replace(/<[^>]*>/g, ' ').replace(/&[a-z#0-9]+;/g, ' ').split(/[^a-z0-9]+/).filter(Boolean);
const wt = toks(fs.readFileSync(process.argv[3], 'utf8'));
const grams = new Set(); for (let i = 0; i + 4 <= wt.length; i++) grams.add(wt.slice(i, i + 4).join(' '));
const t = fs.readFileSync(process.argv[2], 'utf8');
const strs = [...t.matchAll(/"((?:[^"\\]|\\.)*)"/g)].map(m => m[1]
  .replace(/\\n/g, ' ').replace(/\\"/g, '"').replace(/\\u([0-9a-f]{4})/gi, (a, h) => String.fromCharCode(parseInt(h, 16))));
const seen = new Set(); let flagged = 0, tot = 0;
for (const s of strs) {
  if (/[؀-ۿ]/.test(s) || !/[A-Za-z]{4}/.test(s) || s.length < 40) continue;
  const tk = toks(s); if (tk.length < 8) continue;
  const key = tk.join(' '); if (seen.has(key)) continue; seen.add(key); tot++;
  const miss = []; let have = 0, n = 0;
  for (let i = 0; i + 4 <= tk.length; i++) { n++; const g = tk.slice(i, i + 4).join(' '); if (grams.has(g)) have++; else miss.push(g); }
  if (have / n >= 0.6 && miss.length) { flagged++; console.log(miss.slice(0, 3).join(' | ') + '   <<  ' + s.replace(/<[^>]*>/g, ' ').slice(0, 120)); }
}
console.error('strings', tot, 'flagged', flagged);
