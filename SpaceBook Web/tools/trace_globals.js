'use strict';
/* Global-access tracer (dev only). For every class x subject it opens the subject in the app sandbox, selects the
 * first, middle and last chapter and renders every tab, and records which data globals (DATA, ENGLISH_9_DATA,
 * CLS2_BOOKS, ...) were read. Output: tests/trace/<classId>/<subjectId>.json and tests/trace/index.json.
 * Use the files to compute a subject's "neighbours" (subjects sharing a global) before changing shared data.
 * Only data globals are traced; function calls are not (functions cannot be wrapped from outside).
 *   node --max-old-space-size=8192 tools/trace_globals.js [--only cls9,cls12-phy] */
const fs = require('fs'), path = require('path');
const { load, ROOT } = require('./lib/app_sandbox');
const args = process.argv.slice(2);
const oi = args.indexOf('--only');
const ONLY = oi < 0 ? null : args[oi + 1].split(',');
const OUT = path.join(ROOT, 'tests', 'trace');

const app = load({ trace: true });
if (app.loadFails.length) { console.log('load failures: ' + app.loadFails.length); process.exitCode = 1; }
const subjects = app.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name })))');
const todo = subjects.filter(s => !ONLY || ONLY.includes(s.classId) || ONLY.includes(s.id));
const index = {}, byGlobal = {};
let errors = 0;
for (const s of todo) {
  app.reads.clear();
  const rec = { classId: s.classId, subjectId: s.id, name: s.name, chapters: 0, tabsRendered: 0, errors: [] };
  const step = code => { try { return app.run(code, 60000); } catch (e) { rec.errors.push(e.message.slice(0, 200)); } };
  step(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`);
  const chs = step(String.raw`(() => { const seen = new Set(), out = [];
    for (const m of $('dashboard-body').innerHTML.matchAll(/onclick="(select\w*(?:Chapter|Unit|Lesson|Page)\([^"]*)"/g)) if (!seen.has(m[1])) { seen.add(m[1]); out.push(m[1]); }
    return out; })()`) || [];
  rec.chapters = chs.length;
  const picks = [...new Set([0, Math.floor((chs.length - 1) / 2), chs.length - 1])].filter(i => i >= 0 && chs[i]);
  for (const i of picks) {
    step(`state.activeSubjTab = null; ${chs[i].replace(/&#39;|&quot;/g, "'")}`);
    const tabs = step(String.raw`[...new Set([...document.getElementById('subjectTopicArea').innerHTML.matchAll(/onclick="(switchSubjectTab\([^"]*)"/g)].map(m => m[1]))]`) || [];
    for (const t of tabs) { step(t.replace(/&#39;|&quot;/g, "'")); rec.tabsRendered++; }
  }
  rec.globals = [...app.reads].sort();
  index[s.classId + '/' + s.id] = rec.globals;
  rec.globals.forEach(g => (byGlobal[g] = byGlobal[g] || []).push(s.classId + '/' + s.id));
  errors += rec.errors.length;
  fs.mkdirSync(path.join(OUT, s.classId), { recursive: true });
  fs.writeFileSync(path.join(OUT, s.classId, s.id + '.json'), JSON.stringify(rec, null, 1) + '\n');
  console.log(`${s.classId}/${s.id}: ${rec.chapters} ch, ${rec.tabsRendered} tabs, ${rec.globals.length} globals${rec.errors.length ? ', ' + rec.errors.length + ' errors' : ''}`);
}
if (!ONLY) {
  fs.writeFileSync(path.join(OUT, 'index.json'), JSON.stringify({ subjects: index, globalsToSubjects: Object.fromEntries(Object.entries(byGlobal).sort()) }, null, 1) + '\n');
  const unread = app.run("Object.keys(globalThis).filter(k => /^[A-Z][A-Z0-9_]{2,}$/.test(k) && /_(DATA|BOOKS|BOOK|TEXT)$|^CLS[0-9]+_/.test(k))").filter(k => !byGlobal[k]);
  fs.writeFileSync(path.join(OUT, 'never_read.json'), JSON.stringify(unread, null, 1) + '\n');
  console.log('book/data globals never read by any traced subject: ' + unread.length + ' (tests/trace/never_read.json)');
}
console.log(`traced ${todo.length} subjects, ${errors} step errors`);
