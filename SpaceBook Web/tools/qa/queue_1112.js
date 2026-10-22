'use strict';
/* Queue of the English sentences of Class 11/12 books that have no translation from the book itself, most frequent first, for
 * tools/offline_meanings/mt_sentences.py (local NLLB model, nothing leaves the machine).
 *   node tools/qa/queue_1112.js <sent_all.json from tools/word_stats/dump_sentences.js> <out queue.json> [min occurrences] */
const fs = require('fs');
const rows = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const MIN = +process.argv[4] || 1;
const JUNK = /\.pdf|Books\/|unresolved|corrected|source|scan|printed|transcri|SpaceBook|KPTBB|owner|ballpoint|retained|preserved|illegible|cut edge|watermark|page \d|PDF/i;
const BAD = /[=<>_{}|^~\\]/;
const f = rows.filter(r => r.c.some(k => /^cls1[12]$/.test(k)) && r.t !== r.n && r.n >= MIN).filter(r => {
  const s = r.s, w = s.split(' ').length;
  if (w < 3 || w > 40 || s.length > 300 || JUNK.test(s) || BAD.test(s)) return false;
  const l = (s.match(/[A-Za-z]/g) || []).length;
  return l / s.length >= 0.75;
});
f.sort((a, b) => b.n - a.n);
fs.writeFileSync(process.argv[3], JSON.stringify(f.map(x => x.s)));
console.log(f.length, 'sentences; occurrences covered', f.reduce((a, x) => a + x.n, 0));
