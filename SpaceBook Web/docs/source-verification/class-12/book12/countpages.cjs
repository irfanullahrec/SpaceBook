const k = process.argv[2]; const d = require('../' + k + '/dump.json');
const per = {};
for (const ch of d) for (const s of ch.sections) {
  const r = (s.refs || [{}])[0]; const rr = r && typeof r === 'object' ? r : {};
  if (rr.pdfPage == null) continue;
  const o = (per[rr.pdfPage] = per[rr.pdfPage] || { pages: new Set(), unl: 0, secs: 0 });
  o.secs++; const pp = (rr.printedPages || []).filter(x => x != null); pp.forEach(p => o.pages.add(p)); if (!pp.length) o.unl++;
}
let need = 0; const ks = Object.keys(per).map(Number).sort((a, b) => a - b);
for (const k of ks) need += per[k].pages.size + (per[k].unl ? 1 : 0);
console.log(k, 'pdfs with sections', ks.length, 'pages needed', need, 'min printed', Math.min(...Object.values(per).flatMap(o => [...o.pages])), 'max', Math.max(...Object.values(per).flatMap(o => [...o.pages])));
