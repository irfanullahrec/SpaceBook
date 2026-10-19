'use strict';
/* The generated lexicon (js/lexicon_data.js) must give the same answers as reading every book at the first lookup, and must not load any book.
 *   node --max-old-space-size=8192 tests/lexicon/equivalence.js */
const { load } = require('../../tools/lib/app_sandbox');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

// A: as shipped (rows). B: the same page with the rows removed, so the runtime falls back to scanning every book (the old behaviour).
const A = load({ page: 'lazy.html', quiet: true });
const before = A.sb.SBLazy.stats();
A.run("SBOfflineLookup('water', 'en', 'ur')");
const after = A.sb.SBLazy.stats();
const allowed = /lexicon_data\.js|dictionary_data\.js/;      // the generated rows and the English-Urdu dictionary the lookup also reads
check('the first lookup loads the lexicon and the dictionary, no book', before.loaded === 0 && after.loaded >= 1 && after.log.every(l => allowed.test(l.src)), after.loaded + ' files: ' + after.log.map(l => l.src).join(','));
const rows = JSON.parse(A.run('JSON.stringify(SB_LEXICON_V1.rows)'));
check('the first lookup loads under 2 MB (was 150 MB)', after.bytesLoaded < 2e6, (after.bytesLoaded / 1e6).toFixed(1) + ' MB');

const B = load({ page: 'lazy.html', quiet: true });
B.run('window.SB_LEXICON_V1 = undefined');
// a deterministic sample: every 7th row, every field, as the word to look up, in every direction
const words = { en: [], ur: [], ps: [], ar: [] };
rows.forEach((r, i) => { if (i % 7 === 0) ['en', 'ur', 'ps', 'ar'].forEach((l, k) => { const w = String(r[k] || '').split(/[،,]/)[0].replace(/\(.*?\)/g, '').trim(); if (w && w.split(' ').length <= 3) words[l].push(w); }); });
const probes = [];
for (const src of ['en', 'ur', 'ps', 'ar']) for (const tgt of ['en', 'ur', 'ps', 'ar']) if (src !== tgt) for (const w of words[src].slice(0, 400)) probes.push([w, src, tgt]);
probes.push(['water', 'en', 'ur'], ['unknownwordxyz', 'en', 'ur'], ['', 'en', 'ur']);
const q = JSON.stringify(probes);
const code = `JSON.stringify(${q}.map(p => SBOfflineLookup(p[0], p[1], p[2])))`;
const a = JSON.parse(A.run(code, 600000)), b = JSON.parse(B.run(code, 600000));
let diff = 0, firstDiff = null, answered = 0;
a.forEach((x, i) => { if (x) answered++; if (x !== b[i]) { diff++; if (!firstDiff) firstDiff = JSON.stringify(probes[i]) + ' -> ' + x + ' | ' + b[i]; } });
check('the generated lexicon answers like the book scan on ' + probes.length + ' probes (' + answered + ' answered)', diff === 0, diff + ' differ, first: ' + firstDiff);
check('the probes are not trivially empty', answered > probes.length * 0.5, answered + ' of ' + probes.length);
const s = JSON.parse(A.run("JSON.stringify(SBLazy.stats().log.map(l => l.src))"));
check('after thousands of lookups still no book is loaded', s.length <= 2 && s.every(f => allowed.test(f)), s.join(','));

console.log(`lexicon tests: ${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
