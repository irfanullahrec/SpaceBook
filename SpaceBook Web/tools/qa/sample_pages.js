'use strict';
/* Pick random paragraphs (with their scan page) from Class 11/12 data files for a visual proofreading sample.
 *   node tools/qa/sample_pages.js <data file> [count] [seed]
 * Prints the paragraph, the pdfPage and the sourcePdf recorded with it (the JPG of that page is in Books/<class>/<book>/JPG). */
const fs = require('fs'), path = require('path'), vm = require('vm');
const f = path.resolve(__dirname, '..', '..', 'js', process.argv[2]);
const n = +process.argv[3] || 3; let seed = +process.argv[4] || 7;
const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
const code = fs.readFileSync(f, 'utf8').replace(/^(const|let) /gm, 'var ');
const win = {}; const ctx = vm.createContext({ window: win, self: win, document: {}, console: { log() { }, warn() { }, error() { } }, localStorage: {}, navigator: {}, setTimeout() { }, addEventListener() { } });
try { vm.runInContext(code, ctx, { timeout: 60000 }); } catch (e) { }
const cand = []; const seen = new Set();
const walk = (o, d, ref) => {
  if (!o || typeof o !== 'object' || seen.has(o) || d > 16) return; seen.add(o);
  const r = o.sourceReferences && o.sourceReferences[0] || (o.pdfPage ? o : null) || ref;
  if (!Array.isArray(o)) for (const k of ['en', 'text', 'english', 'p']) if (typeof o[k] === 'string' && o[k].length > 150 && o[k].length < 700 && r && r.pdfPage && !/[؀-ۿ]/.test(o[k]) && !/^</.test(o[k])) cand.push({ t: o[k], pdf: r.pdfPage, printed: r.printedPage, src: r.sourcePdf || r.jpg || '' });
  for (const k of Object.keys(o)) walk(o[k], d + 1, r);
};
for (const k of Object.keys(ctx)) walk(ctx[k], 0, null); for (const k of Object.keys(win)) walk(win[k], 0, null);
console.log(path.basename(f), 'candidates', cand.length);
for (let i = 0; i < n && cand.length; i++) { const c = cand.splice(Math.floor(rnd() * cand.length), 1)[0]; console.log('\n[pdf ' + c.pdf + ' printed ' + c.printed + '] ' + c.src + '\n' + c.t.replace(/\n+/g, ' ¶ ')); }
