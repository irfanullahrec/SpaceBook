'use strict';
/* Lint of the stored sentence translations (js/sent_data_*.js): quality letters and obvious defects in the Urdu / Pashto / Arabic text.
 *   node tools/qa/sent_lint.js [--show N]
 * Entry = "qqq<TAB>urdu<TAB>pashto<TAB>arabic", q: c hand-written, m computer-made, - none. Defects: a language missing, Latin letters left in the
 * translation (other than a few symbols), text in the wrong script, a translation that is only digits/punctuation, or a very odd length ratio. */
const fs = require('fs'), path = require('path');
const dir = path.resolve(__dirname, '..', '..', 'js');
const show = +(process.argv[process.argv.indexOf('--show') + 1]) || 0;
const stat = { entries: 0, q: { c: 0, m: 0, none: 0 }, missing: [0, 0, 0], latin: [0, 0, 0], script: [0, 0, 0], ratio: [0, 0, 0], total3c: 0 };
const ex = [];
const AR = /[؀-ۿ]/, LAT = /[A-Za-z]{3,}/;
for (const f of fs.readdirSync(dir).filter(f => /^sent_data_\d+\.js$/.test(f))) {
  const win = {}; new Function('window', fs.readFileSync(path.join(dir, f), 'utf8'))(win);
  const D = Object.values(win)[0].d;
  for (const [k, v] of Object.entries(D)) {
    const p = v.split('\t'); const q = p[0]; stat.entries++;
    if (q === 'ccc') stat.total3c++;
    for (let i = 0; i < 3; i++) {
      const ch = q[i], t = (p[i + 1] || '').trim();
      if (ch === 'c') stat.q.c++; else if (ch === 'm') stat.q.m++; else stat.q.none++;
      if (!t) { stat.missing[i]++; continue; }
      const t2 = t.replace(/^≈\s*/, '').replace(/\$[^$]*\$|\([^)]*\)/g, '');
      if (LAT.test(t2)) { stat.latin[i]++; if (ex.length < 3000) ex.push(['latin' + i, k, t.slice(0, 80)]); }
      if (!AR.test(t)) { stat.script[i]++; if (ex.length < 3000) ex.push(['script' + i, k, t.slice(0, 80)]); }
    }
  }
}
console.log(JSON.stringify(stat));
if (show) for (const kind of ['latin0', 'latin1', 'latin2', 'script0', 'script1', 'script2']) { const L = ex.filter(e => e[0] === kind); console.log('--', kind, L.length); L.slice(0, show).forEach(e => console.log('  ', e[1], e[2])); }
