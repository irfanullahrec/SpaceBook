'use strict';
const fs = require('fs');
const W = require('../word_stats/build_word_stats.js');
const { JS, subjectForFile, evaluate, SKIP_FILES, DATA_KEY_FILES } = W;
const D = W.loadCatalogue();
const keys = {};
const files = fs.readdirSync(JS).filter(f => f.endsWith('.js') && !SKIP_FILES.has(f) && !/reader\.js$/.test(f)).sort();
function walk(v, seen, f) {
  if (!v || typeof v !== 'object' || seen.has(v)) return; seen.add(v);
  if (Array.isArray(v)) { v.forEach(x => walk(x, seen, f)); return; }
  const ks = Object.keys(v);
  const hasTr = ks.some(k => /^(ur|ps|ar|urdu|pashto|tr|translation|translations)$/i.test(k));
  for (const k of ks) { let x; try { x = v[k]; } catch (e) { continue; } if (hasTr && typeof x === 'string') { const kk = k; (keys[kk] = keys[kk] || { n: 0, f: new Set() }).n++; keys[kk].f.add(f); } walk(x, seen, f); }
}
for (const file of files) {
  const sid = subjectForFile(file, D.subjects), keyed = DATA_KEY_FILES[file];
  if (!sid && !keyed) continue;
  let ev; try { ev = evaluate(file); } catch (e) { continue; }
  walk([Object.values(ev.globals), ev.data], new Set(), file);
}
console.log(Object.entries(keys).sort((a, b) => b[1].n - a[1].n).slice(0, 40).map(([k, v]) => k + ' ' + v.n + ' ' + [...v.f].slice(0, 3).join(',')).join('\n'));
