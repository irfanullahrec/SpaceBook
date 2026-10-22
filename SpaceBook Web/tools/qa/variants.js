'use strict';
/* Finds English sentences that occur in more than one spelling/punctuation inside one data file
 * (the same page text is stored several times, so a typo fixed in one copy shows up as a variant).
 *   node tools/qa/variants.js js/english_12_data.js */
const fs = require('fs');
const t = fs.readFileSync(process.argv[2], 'utf8');
const strs = [...t.matchAll(/"((?:[^"\\]|\\.)*)"/g)].map(m => m[1]
  .replace(/\\n/g, ' ').replace(/&#x27;/g, "'").replace(/&amp;/g, '&')
  .replace(/\\u([0-9a-f]{4})/gi, (a, h) => String.fromCharCode(parseInt(h, 16))));
const sents = new Map();
for (const s of strs) {
  if (!/[A-Za-z]{3}/.test(s) || /[؀-ۿ]/.test(s)) continue;
  for (const p of s.split(/(?<=[.?!])\s+/)) {
    if (p.length < 25) continue;
    const k = p.toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
    if (!sents.has(k)) sents.set(k, new Map());
    const m = sents.get(k);
    m.set(p, (m.get(p) || 0) + 1);
  }
}
let n = 0;
for (const [, m] of sents) {
  if (m.size > 1) { n++; console.log([...m].map(([p, c]) => c + 'x ' + p.slice(0, 220)).join('\n  ') + '\n'); }
}
console.error('groups', n);
