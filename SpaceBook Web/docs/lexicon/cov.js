// coverage check: which top ur/ps/ar words have no offline entry yet
global.window = global; require('../../js/word_stats_words.js');
const fs = require('fs'), vm = require('vm');
const c = {window: {}}; vm.createContext(c); vm.runInContext(fs.readFileSync(__dirname + '/../../js/dictionary_data.js', 'utf8') + ';this.D=ENG_URDU_DICT;', c);
const norm = s => String(s).replace(/[\u064B-\u065F\u0670\u0640\u06E1]/g, '').replace(/ي/g, 'ی').replace(/ك/g, 'ک').replace(/ہ|ۀ|ة/g, 'ه').replace(/[^\p{L}\s]/gu, '').trim().toLowerCase();
const have = {en: new Set(), ur: new Set(), ps: new Set(), ar: new Set()};
const idx = (l, v) => String(v || '').split(/[،,;\/]|\(|\)/).forEach(x => { x = norm(x); if (x) have[l].add(x); });
for (const k in c.D) { idx('en', k); idx('ur', c.D[k].u); idx('ps', c.D[k].p); }
for (const f of fs.readdirSync(__dirname).filter(f => /^(en|ur|ps|ar)\d+\.txt$/.test(f)))
  for (const line of fs.readFileSync(__dirname + '/' + f, 'utf8').split('\n')) { const p = line.split('|'); if (p.length < 4) continue; ['en', 'ur', 'ps', 'ar'].forEach((l, i) => idx(l, p[i])); }
const L = process.argv[2], N = +process.argv[3] || 600;
const W = SB_WORD_STATS_WORDS.words[L].split('\n').slice(0, N).filter(w => w.length > 1);
const miss = W.filter(w => !have[L].has(norm(w)));
console.log(L, 'top', N, 'missing', miss.length); console.log(miss.join(' '));
