// OCR is only a locator. This word-overlap report helps find omissions; visual source review remains required.
const fs = require('fs');
const vm = require('vm');
const path = require('path');
const root = 'D:/SpaceBook/SpaceBook Web/';
const ocrDir = process.argv[2];
if (!ocrDir) throw new Error('Usage: node compare_chemistry_ocr_to_code.cjs <OCR batch directory>');
const ctx = vm.createContext({});
vm.runInContext(fs.readFileSync(path.join(root, 'js/chem_11_data.js'), 'utf8') + ';globalThis.chemData=CHEM_11_DATA', ctx);
const pages = new Map();
function add(page, value) {
  if (!pages.has(page)) pages.set(page, []);
  if (value) pages.get(page).push(String(value));
}
for (const chapter of ctx.chemData) for (const sec of chapter.sections) {
  const page = sec.source.pdfPage;
  add(page, [sec.title, sec.headingUrdu, sec.headingPashto].join(' '));
  for (const p of sec.paras || []) add(page, p.original);
  if (sec.table) {
    add(page, sec.table.caption);
    for (const row of sec.table.rows) for (const cell of row) add(page, cell.en);
    for (const h of sec.table.headers) add(page, h.en);
  }
}
const normalize = value => value.toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim().split(/\s+/).filter(Boolean);
const report = [];
for (const [page, sourceParts] of [...pages].sort((a,b)=>a[0]-b[0])) {
  const file = path.join(ocrDir, `p${String(page).padStart(3,'0')}.txt`);
  if (!fs.existsSync(file)) { report.push({page,status:'OCR pending'}); continue; }
  const words = normalize(fs.readFileSync(file,'utf8'));
  const codeWords = new Set(normalize(sourceParts.join(' ')));
  const hits = words.filter(word => codeWords.has(word));
  const uniqueMissing = [...new Set(words.filter(word => !codeWords.has(word)))];
  report.push({page,ocrWords:words.length,matchedOccurrences:hits.length,wordOverlap:words.length ? +(hits.length/words.length).toFixed(3) : 1,unmatchedOcrWords:uniqueMissing.slice(0,60)});
}
const output = path.join(ocrDir, 'chemistry-source-code-overlap.json');
fs.writeFileSync(output, JSON.stringify(report,null,2));
console.log(`pages=${report.length}; saved=${output}`);
for (const r of report) console.log(`p${r.page}: ${r.status || `${(r.wordOverlap*100).toFixed(1)}% OCR token overlap; ${r.ocrWords} words`}`);
