// prints, per PDF scan of a book's reviewed data, its printed-page labels and section ids (to line the scans up with the JPG files)
const d = require('../' + process.argv[2] + '/dump.json');
const per = {};
for (const ch of d) for (const s of ch.sections) {
  const r = (s.refs || [{}])[0]; const rr = r && typeof r === 'object' ? r : {};
  const k = rr.pdfPage; if (k == null) continue;
  (per[k] = per[k] || { pages: [], secs: [] });
  per[k].pages.push(...(rr.printedPages || []).filter(x => x != null)); per[k].secs.push(s.id.replace(/^[a-z0-9]+-/, ''));
}
const ks = Object.keys(per).map(Number).sort((a, b) => a - b);
let prev = 0, out = [];
for (const k of ks) { if (k !== prev + 1) out.push('   -- gap: PDF ' + (prev + 1) + (k - prev > 2 ? '..' + (k - 1) : '') + ' has no section'); out.push(`PDF ${k}: p ${[...new Set(per[k].pages)].join(',') || '-'}  [${per[k].secs.length} sec] ${per[k].secs.slice(0, 2).join(' ')}`); prev = k; }
console.log(out.join('\n'));
