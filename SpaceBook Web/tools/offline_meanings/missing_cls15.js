'use strict';
/* English words of Classes 1-5 that still have no Urdu / Pashto / Arabic meaning (most frequent first).
 *   node tools/offline_meanings/missing_cls15.js [--top 80] [--json out.json]   */
const fs = require('fs'), path = require('path');
global.window = {};
const ROOT = path.join(__dirname, '..', '..');
eval(fs.readFileSync(path.join(ROOT, 'js', 'lexicon_data.js'), 'utf8'));
eval(fs.readFileSync(path.join(ROOT, 'js', 'word_stats_words.js'), 'utf8'));
const W = window.SB_WORD_STATS_WORDS;
const words = W.words.en.split('\n');
const freq = W.freq.en.split(',').map(x => parseInt(x, 36));
const have = { ur: new Set(), ps: new Set(), ar: new Set() };
for (const r of window.SB_LEXICON_V1.rows) for (const p of r[0].split(/[،,]/)) {
  const k = p.replace(/\(.*?\)/g, '').trim().toLowerCase(); if (!/^[a-z'-]+$/.test(k)) continue;
  if (r[1]) have.ur.add(k); if (r[2]) have.ps.add(k); if (r[3]) have.ar.add(k);
}
const CL = (process.argv.includes('--classes') ? process.argv[process.argv.indexOf('--classes') + 1].split(',').map(Number) : [1, 2, 3, 4, 5]);
const sc = CL.map(c => W.scopes['cls' + c].en.split(',').map(x => parseInt(x, 36) || 0));
const f15 = i => sc.reduce((a, s) => a + (s[i] || 0), 0);      // occurrences in Classes 1-5 only
const inScope = i => f15(i) > 0;
const stems = w => [w, w.replace(/ies$/, 'y'), w.replace(/(es|s)$/, ''), w.replace(/ed$/, ''), w.replace(/ed$/, 'e'), w.replace(/ing$/, ''), w.replace(/ing$/, 'e'), w.replace(/(.)ing$/, '$1'), w.replace(/ly$/, '')];
const out = [];
words.forEach((w, i) => {
  if (!/^[a-z][a-z'-]*$/.test(w) || w.length < 2 || !inScope(i)) return;
  const need = ['ur', 'ps', 'ar'].filter(l => !stems(w).some(x => have[l].has(x)));
  if (need.length) out.push([w, f15(i), need.join(',')]);
});
out.sort((a, b) => b[1] - a[1]);
const top = +(process.argv.includes('--top') ? process.argv[process.argv.indexOf('--top') + 1] : 60);
console.log('Class 1-5 English words without a meaning in at least one language:', out.length, '| with no Urdu meaning:', out.filter(x => /ur/.test(x[2])).length);
console.log(out.slice(0, top).map(x => x[0] + ':' + x[1]).join(' '));
if (process.argv.includes('--json')) fs.writeFileSync(process.argv[process.argv.indexOf('--json') + 1], JSON.stringify(out));
