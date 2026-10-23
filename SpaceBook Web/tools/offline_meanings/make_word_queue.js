'use strict';
/* Which (word, language) pairs still have no meaning on the device?  Writes D:/lexsrc/mt/queue.json = [[word, freq, "ur,ps,ar"], ...] most frequent first.
 *   node tools/offline_meanings/make_word_queue.js <envocab.json> <out.json> [minFreq] */
const fs = require('fs');
global.window = {};
eval(fs.readFileSync(__dirname + '/../../js/lexicon_data.js', 'utf8'));
const voc = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const minF = +(process.argv[4] || 3);
const have = { ur: new Set(), ps: new Set(), ar: new Set() };
for (const r of window.SB_LEXICON_V1.rows) for (const p of r[0].split(/[،,]/)) {
  const k = p.replace(/\(.*?\)/g, '').trim().toLowerCase(); if (!/^[a-z'-]+$/.test(k)) continue;
  if (r[1]) have.ur.add(k); if (r[2]) have.ps.add(k); if (r[3]) have.ar.add(k);
}
const NOISE = /^(scan|pdf|ul|kptbb|svg|rs|int|fig|obscured|unresolved|watermark|eq|ye|ms|ac|cout|html|abc|src|cos|sin|tan)$/;
const q = [];
for (const [w, f] of voc) {
  if (f < minF || NOISE.test(w) || !/^[a-z][a-z'-]*$/.test(w) || w.length < 2 && w !== 'a') continue;
  const need = ['ur', 'ps', 'ar'].filter(l => !have[l].has(w));
  if (need.length) q.push([w, f, need.join(',')]);
}
fs.writeFileSync(process.argv[3], JSON.stringify(q));
console.log('queue', q.length, 'pairs', q.reduce((a, x) => a + x[2].split(',').length, 0));
