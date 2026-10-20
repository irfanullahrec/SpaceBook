'use strict';
/* Heap used after opening one subject on the lazy page, in a fresh process each time (Phase 11, docs/PERFORMANCE.md).
 *   node --expose-gc --max-old-space-size=8192 tools/perf_heap.js cls9-bio cls12-chem ...   (a subject id each; none = a built-in sample)
 * heapUsed after a forced collection, minus the heap of the page right after load. Node's heap is not a phone's: the numbers show the order of
 * magnitude and which subjects are heavy, not the memory a browser will use (which also holds the DOM, layout and the compositor). Dev-only. */
const { spawnSync } = require('child_process');
if (process.env.SB_PERF_CHILD) {
  const { load } = require('./lib/app_sandbox');
  const [classId, id] = [process.env.SB_PERF_CHILD.split('-')[0], process.env.SB_PERF_CHILD];
  const app = load({ page: 'lazy.html', quiet: true });
  global.gc(); const base = process.memoryUsage().heapUsed;
  const t = Date.now();
  app.run(`openSubject(${JSON.stringify(classId)}, ${JSON.stringify(id)})`, 120000);
  const body = app.run("document.getElementById('dashboard-body').innerHTML");
  const first = (body.match(/onclick="(select\w*(?:Chapter|Unit|Lesson|Page)\([^"]*)"/) || [])[1];
  if (first) app.run(first.replace(/&#39;|&quot;/g, "'"), 120000);
  global.gc();
  const st = app.sb.SBLazy.stats();
  console.log(JSON.stringify({ id, baseMB: base / 1048576, afterMB: process.memoryUsage().heapUsed / 1048576, files: st.loaded, loadedMB: st.bytesLoaded / 1048576, ms: Date.now() - t }));
  process.exit(0);
}
const ids = process.argv.slice(2).length ? process.argv.slice(2) : ['cls1-eng', 'cls5-math', 'cls9-bio', 'cls9-math', 'cls10-phy', 'cls11-phy', 'cls12-math', 'cls12-chem', 'cls12-phy', 'cls12-econ'];
console.log('subject          source MB   heap before -> after (MB)   +MB   first open ms');
for (const id of ids) {
  const r = spawnSync(process.execPath, ['--expose-gc', '--max-old-space-size=8192', __filename], { env: Object.assign({}, process.env, { SB_PERF_CHILD: id }), encoding: 'utf8', cwd: __dirname });
  const line = String(r.stdout).split('\n').filter(l => l.startsWith('{')).pop();
  if (!line) { console.log(id.padEnd(16), 'failed', String(r.stderr).slice(-120)); continue; }
  const j = JSON.parse(line);
  console.log(id.padEnd(16), j.loadedMB.toFixed(1).padStart(8), '   ', j.baseMB.toFixed(0).padStart(6), '->', j.afterMB.toFixed(0).padStart(5), '       ', (j.afterMB - j.baseMB).toFixed(0).padStart(4), '  ', String(j.ms).padStart(6));
}
