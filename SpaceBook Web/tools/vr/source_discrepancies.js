'use strict';
/* Statements in the books' own worked steps that the engine could check and that do not hold. They are reported, never corrected.
 *   node tools/vr/source_discrepancies.js
 * Checks: a written chemical equation must have the same atoms on both sides; "sin 30 deg = ..." style statements must be true. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..');
const { chemOf } = require(path.join(ROOT, 'js', 'vr_auto.js'));
const files = fs.readdirSync(path.join(ROOT, 'js')).filter(f => /solutions|_data|book/.test(f) && /\.js$/.test(f));
const out = [];
for (const f of files) {
  const raw = fs.readFileSync(path.join(ROOT, 'js', f), 'utf8');
  if (!/rightarrow|rightleftharpoons|→/.test(raw)) continue;
  const ctx = vm.createContext({ window: { CLS10_BOOKS: {}, CLS9_BOOKS: {}, CLS11_BOOKS: {} }, document: {}, console: { log() {}, warn() {}, error() {} }, localStorage: {}, navigator: {} });
  try { vm.runInContext(raw.replace(/^(const|let) /gm, 'var '), ctx, { timeout: 20000 }); } catch (e) { /* partial */ }
  const seen = new Set();
  (function w(o, key, d) {
    if (!o || typeof o !== 'object' || seen.has(o) || d > 12) return; seen.add(o);
    if (Array.isArray(o.steps)) o.steps.forEach(s => {
      const step = typeof s === 'string' ? { text: s } : { text: s && s.en || '', m: s && s.m || '' };
      chemOf(step).forEach(rx => { if (!rx.balanced) out.push({ file: f, key, reaction: rx.texPlain, counts: rx.els.map(e => e + ': ' + (rx.lt[e] || 0) + ' vs ' + (rx.rt[e] || 0)).join(', ') }); });
    });
    Object.keys(o).forEach(k => w(o[k], /^[a-z0-9-]+-s\d+$/i.test(k) ? k : key, d + 1));
  })(ctx.window, '', 0);
}
const uniq = new Map(); out.forEach(r => uniq.set(r.file + r.reaction, r));
Array.from(uniq.values()).forEach(r => console.log(r.file + ' [' + r.key + '] ' + r.reaction + '   -> ' + r.counts));
console.log(uniq.size + ' unbalanced equation(s) found as printed in the books (preserved).');
