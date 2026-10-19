'use strict';
/* Mutation test of the offline layer: each line breaks sw.js or js/core/offline.js in a known way and the named test must then fail; the file is always restored.
 *   node tests/offline/mutate.js        (about 30 s; exit 1 when a mutation is not caught) */
const fs = require('fs'), cp = require('child_process'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const M = [
  ['sw.js', "await caches.delete(SHELL);", "/* no delete */", 'tests/offline/sw.js', 'failed install leaves a shell cache'],
  ['sw.js', "if (!hadShell) await self.skipWaiting();", "await self.skipWaiting();", 'tests/offline/sw.js', 'update takes over by itself'],
  ['sw.js', "if (k.startsWith('sb-shell-') && k !== SHELL) await caches.delete(k);", "await caches.delete(k);", 'tests/offline/sw.js', 'activate wipes content cache'],
  ['sw.js', "if (url.pathname.startsWith(apiPath)) return;", "", 'tests/offline/sw.js', 'API gets cached'],
  ['sw.js', "if (url.origin !== scope.origin) return;", "", 'tests/offline/sw.js', 'cross origin handled'],
  ['sw.js', "if (shellUrls.has(url.href)) { event.respondWith(fromShell(req)); return; }", "", 'tests/offline/sw.js', 'shell files not served from shell'],
  ['js/core/offline.js', "if (!(await sha256Matches(bytes, f.sha256, /\\.(js|json|css)$/.test(src)))) throw", "if (false) throw", 'tests/offline/offline.js', 'integrity check skipped'],
  ['js/core/offline.js', "if (!keepFiles.has(src) && await content.delete(", "if (await content.delete(", 'tests/offline/offline.js', 'remove ignores sharing'],
  ['js/core/offline.js', "todo.bytes * 1.1 > u.quota - u.usage", "false", 'tests/offline/offline.js', 'quota pre-check skipped'],
];
let bad = 0;
for (const [file, from, to, test, name] of M) {
  const full = path.join(ROOT, file), orig = fs.readFileSync(full, 'utf8');
  if (!orig.includes(from)) { console.log('SKIP (anchor not found) ' + name); bad++; continue; }
  fs.writeFileSync(full, orig.replace(from, to));
  let out;
  try { out = cp.spawnSync(process.execPath, [test], { cwd: ROOT, encoding: 'utf8', timeout: 120000 }); } finally { fs.writeFileSync(full, orig); }
  const caught = out.status !== 0;
  console.log((caught ? 'caught   ' : 'MISSED   ') + name);
  if (!caught) bad++;
}
console.log(bad ? bad + ' mutation(s) not caught' : 'all mutations caught');
process.exit(bad ? 1 : 0);
