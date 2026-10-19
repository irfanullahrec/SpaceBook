'use strict';
/* What does the lazy page load? At start-up, and for each subject opened on its own (fresh page per subject is too slow,
 * so loaded files are attributed to the first subject that needed them).   node tools/build/measure_lazy.js [--startup-only] */
const { load } = require('../lib/app_sandbox');
const t0 = Date.now();
const app = load({ page: 'lazy.html', quiet: true });
const st = app.sb.SBLazy.stats();
console.log(`lazy page ready in ${Date.now() - t0} ms: ${app.srcs.length} scripts executed; lazy files loaded during start-up: ${st.loaded} of ${st.files} (${(st.bytesLoaded / 1e6).toFixed(1)} of ${(st.bytesTotal / 1e6).toFixed(0)} MB)`);
st.log.forEach(l => console.log('   at start-up: ' + l.src + ' ' + (l.bytes / 1e6).toFixed(1) + ' MB' + (l.by ? '   <- touched by ' + l.by : '')));
if (process.argv.includes('--startup-only')) process.exit(0);
const subjects = app.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id })))');
let seen = st.loaded;
const rows = [];
for (const s of subjects) {
  try { app.run(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`, 60000); } catch (e) { rows.push([s.id, 'ERROR ' + e.message.slice(0, 60)]); continue; }
  const now = app.sb.SBLazy.stats();
  const fresh = now.log.slice(seen); seen = now.loaded;
  rows.push([s.id, fresh.map(l => l.src.replace('js/', '') + ' ' + (l.bytes / 1e6).toFixed(1) + 'MB').join(', ') || '(nothing new)']);
}
rows.forEach(r => console.log(r[0].padEnd(22) + r[1]));
const end = app.sb.SBLazy.stats();
console.log(`after opening all ${subjects.length} subjects: ${end.loaded} of ${end.files} files loaded (${(end.bytesLoaded / 1e6).toFixed(0)} MB)`);
