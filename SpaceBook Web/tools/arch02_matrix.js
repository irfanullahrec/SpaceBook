'use strict';
/* ARCH-02 matrix test: which book a subject opens must depend on the class and subject, never on what was selected before.
 *   node --max-old-space-size=8192 tools/arch02_matrix.js [--page lazy.html]
 * Opens every subject of every class and records the (subject key, class) pairs the app asks getSubjectChapterList for.
 * For each pair it fetches the chapter list with state.selectedClass set to the class itself (the reference), then with
 * every other class id, '' and null, and fails when the list differs. Before the fix, getSubjectChapterList('eng', 'cls9')
 * returned the Class 7 book while state.selectedClass was 'cls7'. Exit 1 on any difference. Dev-only. */
const { load, ROOT } = require('./lib/app_sandbox');
const args = process.argv.slice(2);
const page = args.includes('--page') ? args[args.indexOf('--page') + 1] : 'index.html';
const app = load({ page, quiet: true });

const subjects = app.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id })))');
const classIds = app.run('DATA.classes.map(c => c.id)');
// the app's own calls: wrap getSubjectChapterList for the duration of the opening loop
const pairs = app.run(`(() => {
  const seen = new Set(), orig = getSubjectChapterList, subj = ${JSON.stringify(subjects)};
  getSubjectChapterList = function (key, classId) { if (classId) seen.add(key + '|' + classId); return orig.apply(this, arguments); };
  let errors = 0;
  for (const s of subj) { try { openSubject(s.classId, s.id); } catch (e) { errors++; } }
  getSubjectChapterList = orig;
  return { pairs: [...seen], errors };
})()`);
// a short fingerprint of a chapter list: its length and every chapter's identifying fields
const FP = `const fp = list => { const a = Array.isArray(list) ? list : []; return a.length + ':' + a.map(c => [c && (c.id || c.number || c.num || ''), c && (c.title || c.name || '')].join('~').slice(0, 60)).join('|'); };`;
const result = app.run(`(() => {
  ${FP}
  const classIds = ${JSON.stringify(classIds)}, others = classIds.concat(['', null]);
  const fails = []; let calls = 0;
  for (const p of ${JSON.stringify(pairs.pairs)}) {
    const [key, cls] = p.split('|');
    state.selectedClass = cls;
    const ref = fp(getSubjectChapterList(key, cls));
    for (const x of others) {
      state.selectedClass = x; calls++;
      const got = fp(getSubjectChapterList(key, cls));
      if (got !== ref) fails.push(key + ' ' + cls + ' while state.selectedClass=' + JSON.stringify(x) + ': ' + got.split(':')[0] + ' chapters instead of ' + ref.split(':')[0]);
    }
  }
  return { fails, calls };
})()`);
console.log(`ARCH-02 matrix (${page}): ${pairs.pairs.length} subject/class pairs x ${classIds.length + 2} selected-class values = ${result.calls} lookups, ${pairs.errors} open errors, ${result.fails.length} differences`);
result.fails.slice(0, 40).forEach(f => console.log('  ' + f));
if (result.fails.length > 40) console.log(`  ... and ${result.fails.length - 40} more`);
process.exit(result.fails.length || pairs.errors ? 1 : 0);
