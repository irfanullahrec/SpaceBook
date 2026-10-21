'use strict';
/* Words of Class 11 and 12 books that have no meaning on the device, most frequent first.
 *   node --max-old-space-size=3072 tools/qa/missing_words_1112.js [N] > list
 * Prints "word<TAB>occurrences<TAB>missing targets" for English; uses the same lookup as the hover card (SBOfflineLookup). */
const fs = require('fs'), path = require('path');
const { load, ROOT } = require('../lib/app_sandbox');
const W = {}; new Function('window', fs.readFileSync(path.join(ROOT, 'js', 'word_stats_words.js'), 'utf8'))(W);
const D = W.SB_WORD_STATS_WORDS;
const LANG = process.argv[3] || 'en', N = +process.argv[2] || 600;
const words = D.words[LANG].split('\n'), freq = D.freq[LANG].split(',').map(x => parseInt(x, 36));
const set = new Set();
for (const sc of Object.keys(D.scopes)) if (/^cls1[12]($|-)/.test(sc) && D.scopes[sc][LANG]) { let p = -1; for (const part of D.scopes[sc][LANG].split(',')) { p += parseInt(part, 36); set.add(p); } }
const app = load({ page: 'lazy.html', quiet: true });
const T = ['en', 'ur', 'ps', 'ar'].filter(x => x !== LANG);
const idx = [...set].filter(i => words[i].length > 1 && /^[\p{L}][\p{L}'-]*$/u.test(words[i]));
const res = JSON.parse(app.run(`(() => { const w = ${JSON.stringify(idx.map(i => words[i]))}, T = ${JSON.stringify(T)}; return JSON.stringify(w.map(x => T.map(t => { try { return SBOfflineLookup(x, '${LANG}', t) ? 1 : 0; } catch (e) { return 0; } }))); })()`));
const rows = idx.map((i, k) => ({ w: words[i], f: freq[i], miss: T.filter((t, j) => !res[k][j]) })).filter(r => r.miss.length).sort((a, b) => b.f - a.f);
console.error('class 11/12 words', idx.length, 'with a gap', rows.length);
rows.slice(0, N).forEach(r => console.log(r.w + '\t' + r.f + '\t' + r.miss.join(',')));
