// Statistics XII source-record checks (no browser): data evaluation, aligned paragraphs, layout/table integrity,
// KaTeX rendering of every inline/display formula in all three languages, and SVG tag balance.
const fs = require('fs'), vm = require('vm'), path = require('path');
const root = path.resolve(__dirname, '..');
const ctx = {window: {}, console};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root, 'assets/vendor/katex/katex.min.js'), 'utf8'), ctx);
vm.runInContext(fs.readFileSync(path.join(root, 'js/stat_12_data.js'), 'utf8') + ';this.D=STAT_12_DATA;', ctx);
const katex = ctx.katex || ctx.window.katex;
const D = ctx.D, errors = [], ids = new Set();
const mathPattern = /\$\$([\s\S]*?)\$\$|(?<!\\)\$([^$\n]+)\$/g;
let sections = 0, paragraphs = 0, formulas = 0, tables = 0, visuals = 0;
const only = process.argv[2] ? Number(process.argv[2]) : null;
for (const unit of D) for (const s of unit.sections) {
  if (!s.sourceClass12Statistics) continue;
  const pdf = s.sourceReferences?.[0]?.pdfPage;
  if (only && pdf !== only) continue;
  sections++;
  const where = `unit ${unit.number} ${s.id} (PDF ${pdf})`;
  if (ids.has(s.id)) errors.push(`${where}: duplicate id`); ids.add(s.id);
  s.paras.forEach((p, i) => {
    paragraphs++;
    for (const k of ['text', 'urdu', 'pashto']) {
      if (!String(p[k] || '').trim()) errors.push(`${where} para ${i}: empty ${k}`);
      for (const m of String(p[k] || '').matchAll(mathPattern)) {
        formulas++;
        if (/[؀-ۿ]/.test(m[1] ?? m[2])) errors.push(`${where} para ${i} ${k}: Arabic-script text inside math`);
        try { katex.renderToString(m[1] ?? m[2], {throwOnError: true, strict: 'ignore', displayMode: m[1] !== undefined}); }
        catch (e) { errors.push(`${where} para ${i} ${k}: KaTeX ${e.message.slice(0, 140)} :: ${(m[1] ?? m[2]).slice(0, 80)}`); }
      }
      if ((String(p[k]).replace(/\$\$[\s\S]*?\$\$/g, '').match(/(?<!\\)\$/g) || []).length % 2) errors.push(`${where} para ${i} ${k}: unbalanced $`);
    }
  });
  const used = new Set();
  for (const b of s.sourceLayout) {
    for (const i of b.indices || []) { if (i >= s.paras.length) errors.push(`${where}: layout index ${i} out of range`); used.add(i); }
    if (b.type === 'sourceDataTable') {
      tables++;
      const t = s.sourceBlocks.find(x => x.id === b.tableId);
      if (!t) { errors.push(`${where}: missing table ${b.tableId}`); continue; }
      const width = (t.headers || []).length;
      for (const tr of [t, ...(t.translations || [])]) {
        if (!t.noHeader && tr.headers?.length !== width) errors.push(`${where} ${t.id}: header width mismatch (${tr.language || 'en'})`);
        if (tr.rows.length !== t.rows.length) errors.push(`${where} ${t.id}: row count mismatch (${tr.language || 'en'})`);
        tr.rows.forEach((r, ri) => { if (!t.ragged && width && r.length !== width) errors.push(`${where} ${t.id} row ${ri}: ${r.length} cells vs ${width}`);
          r.forEach(c => { for (const m of String(c).matchAll(mathPattern)) { formulas++; try { katex.renderToString(m[1] ?? m[2], {throwOnError: true, strict: 'ignore'}); } catch (e) { errors.push(`${where} ${t.id}: KaTeX ${e.message.slice(0, 100)}`); } } }); });
      }
    }
    if (b.type === 'visual' || b.type === 'visualParagraph') {
      visuals++;
      const v = s.sourceBlocks.find(x => x.id === b.blockId);
      if (!v) { errors.push(`${where}: missing visual ${b.blockId}`); continue; }
      for (const k of ['svg', 'svgUrdu', 'svgPashto']) {
        const svg = v[k] || '';
        if (!/^<svg\b[\s\S]*<\/svg>$/.test(svg.trim())) { errors.push(`${where} ${v.id} ${k}: not an svg`); continue; }
        const stack = [];
        for (const m of svg.matchAll(/<(\/?)([a-zA-Z][\w:-]*)([^>]*?)(\/?)>/g)) {
          if (m[4] === '/') continue;
          if (m[1]) { if (stack.pop() !== m[2]) { errors.push(`${where} ${v.id} ${k}: unbalanced </${m[2]}>`); break; } }
          else stack.push(m[2]);
        }
        if (stack.length) errors.push(`${where} ${v.id} ${k}: unclosed ${stack.join(',')}`);
        if (/<image\b|data:image|\.png|\.jpe?g|\.webp/i.test(svg)) errors.push(`${where} ${v.id}: raster content`);
      }
    }
  }
  s.paras.forEach((_, i) => { if (!used.has(i)) errors.push(`${where}: para ${i} not in layout`); });
}
const summary = {sections, paragraphs, formulas, tables, visuals, errors: errors.length};
console.log(JSON.stringify(summary));
errors.slice(0, 60).forEach(e => console.log(' -', e));
process.exitCode = errors.length ? 1 : 0;
