'use strict';
/* For every data-like script of index.html: run it alone in an empty vm context and report what it defines
 * (top-level names with their kind, CLSn_BOOKS keys, other window.X sets) or why it cannot run alone.
 *   node tools/build/probe_files.js            writes tests/contract/file_probe.json */
const fs = require('fs'), vm = require('vm'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const inv = require('../../tests/contract/script_inventory.json');
const kind = v => Array.isArray(v) ? 'array' : v === null ? 'null' : typeof v === 'object' ? 'object' : typeof v;
const res = [];
for (const o of inv) {
  if (!o.bytes || o.functions !== 0 || !(o.declares.length || o.windowSets.length || o.mutates.length)) continue;
  const code = fs.readFileSync(path.join(ROOT, o.src), 'utf8');
  const ctx = vm.createContext({ console: { log() {}, warn() {}, error() {} }, setTimeout() {}, clearTimeout() {} });
  vm.runInContext('globalThis.window = globalThis; globalThis.self = globalThis;', ctx);
  const before = new Set(Object.keys(ctx));
  const names = o.declares.slice();
  // top-level const/let/var become window properties so they can be listed
  const tx = code.replace(/^(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=/gm, 'globalThis.$1 =');
  const r = { src: o.src, bytes: o.bytes };
  try {
    vm.runInContext(tx, ctx, { timeout: 60000, filename: o.src });
    r.ok = true;
    r.defines = Object.keys(ctx).filter(k => !before.has(k)).map(k => ({ name: k, kind: kind(ctx[k]) }));
    r.containerKeys = {};
    for (const k of Object.keys(ctx)) if (/^CLS\d+_BOOKS$/.test(k) && ctx[k] && typeof ctx[k] === 'object') r.containerKeys[k] = Object.keys(ctx[k]);
  } catch (e) { r.ok = false; r.error = String(e && e.message).slice(0, 120); }
  res.push(r);
}
fs.writeFileSync(path.join(ROOT, 'tests', 'contract', 'file_probe.json'), JSON.stringify(res, null, 1) + '\n');
const ok = res.filter(r => r.ok), bad = res.filter(r => !r.ok);
console.log('probed', res.length, 'data-like files:', ok.length, 'run alone,', bad.length, 'need other scripts');
console.log('run-alone size', (ok.reduce((n, r) => n + r.bytes, 0) / 1e6).toFixed(1), 'MB; need-others size', (bad.reduce((n, r) => n + r.bytes, 0) / 1e6).toFixed(1), 'MB');
bad.slice(0, 20).forEach(r => console.log('  needs others:', r.src, '-', r.error));
