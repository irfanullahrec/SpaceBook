'use strict';
/* The generated lexicon (js/lexicon_data.js) is read at the first lookup, loads no book, keeps every language in its own column, and the
 * lookups built on it behave (base forms, both directions, no English in a Urdu/Pashto/Arabic answer).
 *   node --max-old-space-size=8192 tests/lexicon/equivalence.js
 * (Before 2026-10-21 this test compared the rows with a scan of every book; the rows are now normalised by script and joined per English
 *  word, on purpose, so they no longer equal that scan. Lexicon v1 rows: tools/build/make_lexicon.js + tools/offline_meanings/normalize.js.) */
const { load } = require('../../tools/lib/app_sandbox');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

const A = load({ page: 'lazy.html', quiet: true });
const before = A.sb.SBLazy.stats();
A.run("SBOfflineLookup('water', 'en', 'ur')");
const after = A.sb.SBLazy.stats();
const allowed = /lexicon_data\.js|dictionary_data\.js/;
check('the first lookup loads the lexicon and the dictionary, no book', before.loaded === 0 && after.loaded >= 1 && after.log.every(l => allowed.test(l.src)), after.loaded + ' files: ' + after.log.map(l => l.src).join(','));
check('the first lookup loads under 5 MB (was 150 MB)', after.bytesLoaded < 5e6, (after.bytesLoaded / 1e6).toFixed(1) + ' MB');

// every column holds its own script
const rows = JSON.parse(A.run('JSON.stringify(SB_LEXICON_V1.rows)'));
const arab = s => (String(s).replace(/\([^)]*\)/g, '').match(/[؀-ۿ]/g) || []).length;
const latin = s => (String(s).replace(/\([^)]*\)/g, '').match(/[A-Za-z]/g) || []).length;
let badCol = 0, first = '';
rows.forEach(r => [1, 2, 3].forEach(k => { if (r[k] && (latin(r[k]) >= 3 && latin(r[k]) > arab(r[k]) || arab(r[k]) === 0)) { badCol++; if (!first) first = JSON.stringify(r); } }));
check('no Urdu, Pashto or Arabic column holds English text', badCol === 0, badCol + ' rows, first ' + first);
check('the lexicon is not tiny', rows.length > 9000, rows.length + ' rows');

// both directions and base forms
const look = (w, s, t) => A.run(`SBOfflineLookup(${JSON.stringify(w)}, '${s}', '${t}')`);
const must = [
  ['water', 'en', 'ur'], ['running', 'en', 'ur'], ['children', 'en', 'ps'], ['studies', 'en', 'ar'], ['hydrogens', 'en', 'ur'], ['built', 'en', 'ps'],
  ['triangle', 'en', 'ar'], ['interval', 'en', 'ur'], ['never', 'en', 'ps'], ['respect', 'en', 'ar'],
  ['خوش نُمائی', 'ur', 'en'], ['ښکلا', 'ps', 'en']
];
must.forEach(([w, s, t]) => { const r = look(w, s, t); check('"' + w + '" (' + s + ' -> ' + t + ') has a meaning', !!r, JSON.stringify(r)); });
const bad = [['unknownwordxyz', 'en', 'ur'], ['', 'en', 'ur']];
bad.forEach(([w, s, t]) => check('"' + w + '" has no invented meaning', !look(w, s, t)));
const r1 = look('running', 'en', 'ur');
check('a meaning is in Arabic script, never English', arab(r1) > 0 && latin(r1) < 3, r1);

// the sandbox's own check that the lookup still loads no book after many lookups
const s = JSON.parse(A.run("JSON.stringify(SBLazy.stats().log.map(l => l.src))"));
check('after the lookups still no book is loaded', s.length <= 2 && s.every(f => allowed.test(f)), s.join(','));

console.log(`lexicon tests: ${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
