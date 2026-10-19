'use strict';
/* Inventory of the scripts index.html loads: size, top-level names declared, window.X assignments, whether the file only
 * declares data. Output: console summary + tests/contract/script_inventory.json.   node tools/build/inventory.js */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
const srcs = [...html.matchAll(/<script\b[^>]*\bsrc="([^"]+)"/g)].map(m => m[1].split('?')[0]);
const out = [];
for (const s of srcs) {
  const f = path.join(ROOT, s);
  if (!fs.existsSync(f)) { out.push({ src: s, missing: true }); continue; }
  const code = fs.readFileSync(f, 'utf8');
  const decl = new Set(), win = new Set(), assigns = new Set();
  let m;
  const re = /^(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=/gm; while ((m = re.exec(code))) decl.add(m[1]);
  const re2 = /\b(?:window|globalThis)\.([A-Za-z_$][\w$]*)\s*=(?!=)/g; while ((m = re2.exec(code))) win.add(m[1]);
  const re3 = /^(?:Object\.assign\(\s*(?:window\.)?([A-Z_][A-Z0-9_]*)|(?:window\.)?([A-Z][A-Z0-9_]+)\.[A-Za-z_$][\w$]*\s*=)/gm; while ((m = re3.exec(code))) assigns.add(m[1] || m[2]);
  const fn = (code.match(/^function\s+[A-Za-z_$]/gm) || []).length;
  out.push({ src: s, bytes: Buffer.byteLength(code), declares: [...decl], windowSets: [...win], mutates: [...assigns], functions: fn });
}
fs.mkdirSync(path.join(ROOT, 'tests', 'contract'), { recursive: true });
fs.writeFileSync(path.join(ROOT, 'tests', 'contract', 'script_inventory.json'), JSON.stringify(out, null, 1) + '\n');
const total = out.reduce((n, o) => n + (o.bytes || 0), 0);
const big = out.filter(o => o.bytes > 200000).sort((a, b) => b.bytes - a.bytes);
console.log(out.length + ' scripts, ' + (total / 1e6).toFixed(1) + ' MB');
const dataLike = out.filter(o => o.bytes && o.functions === 0 && (o.declares.length || o.windowSets.length || o.mutates.length));
console.log('data-like (no functions, declares/sets/mutates globals): ' + dataLike.length + ' files, ' + (dataLike.reduce((n, o) => n + o.bytes, 0) / 1e6).toFixed(1) + ' MB');
console.log('largest:'); big.slice(0, 12).forEach(o => console.log('  ' + (o.bytes / 1e6).toFixed(1).padStart(6) + ' MB  ' + o.src + '  fns=' + o.functions));
