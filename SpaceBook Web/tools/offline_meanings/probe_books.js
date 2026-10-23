const { load } = require('../lib/app_sandbox');
const app = load({ page: 'lazy.html', quiet: true });
const out = app.run(`(() => { const o = {};
 ['CLS1_BOOKS','CLS2_BOOKS','CLS3_BOOKS','CLS4_BOOKS','CLS5_BOOKS','CLS6_BOOKS','CLS7_BOOKS','CLS8_BOOKS','CLS9_BOOKS','CLS10_BOOKS','CLASS11_BOOKS'].forEach(n => { const lib = window[n] || {};
  Object.keys(lib).forEach(k => { const w = lib[k] && lib[k].words; if (!w) return; const ks = Object.keys(w); o[n + '.' + k] = [ks.length, ks.slice(0, 2).map(x => x + ' => ' + JSON.stringify(w[x]))]; }); });
 return JSON.stringify(o); })()`, 600000);
const o = JSON.parse(out);
for (const k of Object.keys(o)) console.log(k, o[k][0], o[k][1].join(' ; ').slice(0, 150));
