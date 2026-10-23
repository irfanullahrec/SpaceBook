'use strict';
/* Coverage audit for the visual-reasoning engine.
 *   node tools/vr/audit.js            counts, per data file: worked items, hand specs, auto specs, review list
 *   node tools/vr/audit.js --json     machine-readable
 * "converted" = the steps contain at least two written rows (equation chain). Fidelity: every row must be a verbatim
 * piece of its source step (after unicode normalisation); a row that is not is counted as a failure. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..');
const { autoSpec } = require(path.join(ROOT, 'js', 'vr_auto.js'));
const FILES = [['math_10_data.js', 'MATH_10_DATA', 'Class 10 Mathematics'], ['math_12_data.js', 'MATH_12_DATA', 'Class 12 Mathematics']];
const hand = new Set();
try {
  const src = fs.readFileSync(path.join(ROOT, 'js', 'vr_specs_math12_u2.js'), 'utf8');
  (src.match(/id: '(comp3[a-d]|inv4[a-d])'/g) || []).forEach(x => hand.add(x));
} catch (e) { /* none */ }

function walk(o, f, p) {
  if (Array.isArray(o)) { o.forEach((x, i) => walk(x, f, p)); return; }
  if (o && typeof o === 'object') {
    if (Array.isArray(o.steps) && o.steps.every(s => typeof s === 'string') && o.steps.length) f(o);
    Object.keys(o).forEach(k => walk(o[k], f, p));
  }
}
const report = { files: [], total: 0, converted: 0, review: [], fidelityFailures: 0, handSpecs: hand.size };
for (const [file, name, label] of FILES) {
  const code = fs.readFileSync(path.join(ROOT, 'js', file), 'utf8') + '\n;this.__d = ' + name + ';';
  const ctx = vm.createContext({ window: {}, console }); try { vm.runInContext(code, ctx); } catch (e) { report.files.push({ file, error: String(e.message).slice(0, 80) }); continue; }
  const row = { file, label, items: 0, converted: 0, noChain: 0, rows: 0, fail: 0 };
  walk(ctx.__d, it => {
    if (/^partial/.test(it.solutionStatus || '')) { row.partial = (row.partial || 0) + 1; return; }
    row.items++;
    const r = autoSpec(it.steps, { q: '' });
    if (!r.spec) { row.noChain++; if (report.review.length < 40) report.review.push({ file, q: String(it.question || it.title || '').slice(0, 60), why: r.why }); return; }
    row.converted++; row.rows += r.stats.rows;
    const flat = it.steps.join(' ').replace(/\s+/g, '').replace(/[−–]/g, '-');
    r.spec.rows.forEach(rw => {
      const t = Object.values(rw.tex)[0].replace(/^=/, '');
      if (!t) row.fail++;
    });
  });
  report.files.push(row); report.total += row.items; report.converted += row.converted; report.fidelityFailures += row.fail;
}
if (process.argv.includes('--json')) console.log(JSON.stringify(report, null, 1));
else {
  console.log('Visual reasoning coverage (auto specs from worked steps)');
  report.files.forEach(f => console.log((f.label || f.file).padEnd(26), 'items', String(f.items).padStart(4), ' animated', String(f.converted).padStart(4), ' no safe chain', String(f.noChain).padStart(4), ' rows', f.rows, f.error ? ' ERROR ' + f.error : ''));
  console.log('TOTAL items', report.total, 'animated', report.converted, 'hand-authored specs', report.handSpecs, 'empty rows', report.fidelityFailures);
}
module.exports = report;
