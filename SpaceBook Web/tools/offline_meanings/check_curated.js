'use strict';
/* Lists the lines of docs/lexicon/curated/*.txt that make_lexicon.js will skip (not 4 fields, bad English word, English letters left in a meaning).
 *   node tools/offline_meanings/check_curated.js */
const fs = require('fs'), path = require('path');
const dir = path.join(__dirname, '..', '..', 'docs', 'lexicon', 'curated');
let n = 0, bad = 0; const seen = new Map();
for (const f of fs.readdirSync(dir).filter(f => /\.txt$/.test(f)).sort()) {
  fs.readFileSync(path.join(dir, f), 'utf8').split('\n').forEach((line, i) => {
    line = line.replace(/\r$/, ''); if (!line.trim()) return; n++;
    const p = line.split('|'); let why = '';
    if (p.length !== 4) why = 'fields=' + p.length;
    else if (!/^[a-z][a-z' -]*$/.test(p[0].trim())) why = 'bad word';
    else if (!p.slice(1).some(v => v.trim())) why = 'no meaning';
    else if (p.slice(1).some(v => /[A-Za-z]{3,}/.test(v.replace(/\([^)]*\)/g, '')))) why = 'Latin in meaning';
    else if (seen.has(p[0])) why = 'repeated in ' + seen.get(p[0]);
    if (!seen.has(p[0])) seen.set(p[0], f + ':' + (i + 1));
    if (why) { bad++; console.log(f + ':' + (i + 1) + ' ' + why + ' | ' + line.slice(0, 70)); }
  });
}
console.log(n + ' lines, ' + bad + ' to fix, ' + seen.size + ' distinct words');
