'use strict';
/* Groups the English strings of a data file by the scan page they are recorded against.
 *   node tools/qa/page_text.js <js/data file> <out.json> [pdfPage-key]
 * Every string inherits the nearest ancestor that carries sourceReferences[0].pdfPage / pdfPage / pdf (block "page" markers are
 * followed in document order for books that mark pages with {t:"page", pdf:N}). Output: { "<pdfPage>": ["string", ...] }. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const f = path.resolve(__dirname, '..', '..', 'js', process.argv[2].replace(/^js[\\/]/, ''));
const out = path.resolve(process.argv[3]);
const URDU = process.argv.includes('--urdu');   // collect Arabic-script strings (Urdu-source books) instead of English ones
const code = fs.readFileSync(f, 'utf8').replace(/^(const|let) /gm, 'var ');
const win = {}; const ctx = vm.createContext({ window: win, self: win, document: {}, console: { log() { }, warn() { }, error() { } }, localStorage: {}, navigator: {}, setTimeout() { }, addEventListener() { } });
try { vm.runInContext(code, ctx, { timeout: 120000 }); } catch (e) { /* partial */ }
const SKIPKEY = /^(svg|svgUrdu|svgPashto|diagramSvg|diagramSvgUrdu|diagramSvgPashto|tex|latex|m|code|formula|d|path|html|src|id|sourcePdf|jpg|stroke|fill|solution|steps|explanation|answer|sol|a|s|n|translations|ur|ps|urdu|pashto|titleUrdu|titlePashto|qUrdu|qPashto|questionUrdu|questionPashto|optionsUrdu|optionsPashto)$/;
const pages = {}; const seen = new Set(); let cur = null;
const put = (pg, s) => { if (!pg) return; for (const q of [].concat(pg).slice(0, 4)) (pages[q] = pages[q] || []).push(s); };
const refOf = o => (o.sourceReferences && o.sourceReferences[0] && o.sourceReferences[0].pdfPage) || (Array.isArray(o.sourcePdfPages) && o.sourcePdfPages.length ? o.sourcePdfPages : null) || o.pdfPage || null;
function walk(o, key, d, pg) {
  if (d > 18) return;
  if (typeof o === 'string') { if (URDU ? (o.length >= 8 && !/^(id|sourcePdf|jpg|svg|tex|latex|code|path|d)$/.test(key) && !/^</.test(o) && (o.match(/[؀-ۿ]/g) || []).length >= 6) : (o.length >= 12 && !SKIPKEY.test(key) && !/^</.test(o) && /[A-Za-z]{3,}/.test(o))) put(pg || cur, o); return; }
  if (!o || typeof o !== 'object' || seen.has(o)) return; seen.add(o);
  if (!Array.isArray(o)) {
    if (o.t === 'page' && o.pdf) cur = o.pdf;
    const mp = o.pdfPage || o.pdf;   // a page marker object ({pdfPage, printedPage, ...} with no long text): following siblings belong to that page
    if (typeof mp === 'number' && Object.keys(o).length <= 8 && !Object.values(o).some(v => (typeof v === 'string' && v.length >= 40) || (v && typeof v === 'object'))) cur = mp;
    const r = refOf(o); if (r) pg = r;
  }
  for (const k of Object.keys(o)) walk(o[k], k, d + 1, pg);
}
for (const k of Object.keys(ctx)) walk(ctx[k], k, 0, null); for (const k of Object.keys(win)) walk(win[k], k, 0, null);
fs.writeFileSync(out, JSON.stringify(pages));
console.log(path.basename(f), 'pages with text:', Object.keys(pages).length, 'strings:', Object.values(pages).reduce((a, b) => a + b.length, 0));
