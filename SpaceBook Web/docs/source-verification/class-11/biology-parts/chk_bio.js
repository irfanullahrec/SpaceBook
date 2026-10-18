const fs = require('fs'), vm = require('vm'), path = require('path');
const src = fs.readFileSync(path.join(__dirname, 'bio_11_data.MASTER.js'), 'utf8');
const ctx = vm.createContext({ console });
vm.runInContext(src + '\n;this.__D = BIO_11_DATA; this.__R = renderBiology11Tab;', ctx);
const data = ctx.__D, render = ctx.__R;
const issues = [];
const ids = new Map();
let nSec = 0, nPara = 0;
const note = (m) => issues.push(m);
const seen = (id, where) => { if (!id) return; if (ids.has(id)) note(`duplicate id ${id} (${where} / ${ids.get(id)})`); else ids.set(id, where); };
const rawMarkup = /<\/?[a-zA-Z][^>]*>|&[a-z]+;|\[object|undefined|NaN/;
for (const ch of data) {
  for (const sec of ch.sections || []) {
    nSec++;
    seen(sec.id, 'section');
    if (!sec.source || !sec.source.scan) note(`section ${sec.id} lacks source.scan`);
    for (const p of sec.paras || []) {
      nPara++;
      seen(p.id, 'para ' + sec.id);
      if (!p.original || !p.urdu || !p.pashto) note(`missing translation ${p.id}`);
      for (const k of ['original', 'urdu', 'pashto']) if (rawMarkup.test(String(p[k] || ''))) note(`raw markup ${p.id}.${k}`);
    }
    for (const f of sec.figures || []) { seen(f.id, 'figure ' + sec.id); if (!f.svg || !/^<svg/.test(f.svg.trim())) note(`figure ${f.id} lacks svg`); if (/data:image|<img/i.test(f.svg || '')) note(`raster in ${f.id}`); }
    for (const t of sec.tables || []) seen(t.id, 'table ' + sec.id);
    const known = new Set([...(sec.paras || []).map(p => p.id)]);
    for (const fl of sec.flow || []) {
      if (fl.type === 'paragraphs') for (const id of fl.ids) if (!known.has(id)) note(`flow id ${id} missing in ${sec.id}`);
      if (fl.type === 'figure' && !(sec.figures || [])[fl.index]) note(`flow figure ${fl.index} missing in ${sec.id}`);
      if (fl.type === 'table' && !(sec.tables || [])[fl.index]) note(`flow table ${fl.index} missing in ${sec.id}`);
    }
  }
  for (const tab of ['lesson', 'concepts', 'exercise', 'slos', 'formulas']) {
    try { const h = render(ch, tab); if (/undefined|\[object|NaN/.test(h)) note(`render ${ch.id}/${tab} contains undefined/[object]`); }
    catch (e) { note(`render ${ch.id}/${tab} threw ${e.message}`); }
  }
}
console.log(issues.slice(0, 40).join('\n'));
console.log(`sections ${nSec} paras ${nPara} issues ${issues.length}`);
