'use strict';
/* Builds content/app_catalog.json: the list of classes, subjects and chapters the Android app shows natively
 * (and the call that opens each chapter inside the web reader). Read from files that are already generated:
 *   js/study_plan_index.js        classes -> subjects (name, Urdu name, emoji) -> chapters (title, counts)
 *   content/search/index.json     subject id -> chapters with `o`, the onclick call of the chapter's own button
 * Output (deterministic, no timestamp):
 *   {schema: 'spacebook.app-catalog/1', classes: [{id, name, subjects: [{id, name, ur, emoji, chapters: [{t, o, n}]}]}]}
 *   t = chapter title, o = the call that opens it once openSubject(classId, subjectId) has run ('' if unknown),
 *   n = number of exercise items (study index `c.ex`) so the app can show a size hint.
 * Run after tools/build/all.js:   node tools/build/make_app_catalog.js [--check]
 * --check exits 1 when the committed file is stale. Dev-only (not deployed). */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.join(__dirname, '..', '..');
const CHECK = process.argv.includes('--check');

const sandbox = { window: {} };
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'js', 'study_plan_index.js'), 'utf8'), sandbox);
const study = sandbox.window.SB_STUDY_INDEX;
const search = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'search', 'index.json'), 'utf8'));
if (!study || !Array.isArray(study.classes)) throw new Error('study_plan_index.js has no classes');

const classes = study.classes.map(c => ({
  id: c.id,
  name: c.name,
  subjects: c.subjects.map(s => {
    const found = (search.subjects[s.id] && search.subjects[s.id].c) || [];
    const byTitle = new Map(found.map(x => [x.t, x.o]));
    return {
      id: s.id,
      name: s.name,
      ur: s.ur || '',
      emoji: s.emoji || '📘',
      chapters: s.chapters.map((ch, i) => ({
        t: ch.t,
        o: byTitle.get(ch.t) || (found[i] && found[i].o) || '',
        n: (ch.c && ch.c.ex) || 0,
      })),
    };
  }),
}));

const out = JSON.stringify({ schema: 'spacebook.app-catalog/1', classes }) + '\n';
const file = path.join(ROOT, 'content', 'app_catalog.json');
if (CHECK) {
  const have = fs.existsSync(file) ? fs.readFileSync(file, 'utf8') : '';
  if (have !== out) { console.error('content/app_catalog.json is stale: run node tools/build/make_app_catalog.js'); process.exit(1); }
  console.log('app_catalog.json is fresh');
} else {
  fs.writeFileSync(file, out);
  const subj = classes.reduce((n, c) => n + c.subjects.length, 0);
  const chap = classes.reduce((n, c) => n + c.subjects.reduce((m, s) => m + s.chapters.length, 0), 0);
  const noCall = classes.reduce((n, c) => n + c.subjects.reduce((m, s) => m + s.chapters.filter(x => !x.o).length, 0), 0);
  console.log(`app_catalog.json: ${classes.length} classes, ${subj} subjects, ${chap} chapters (${noCall} without an open-call), ${(out.length / 1024).toFixed(0)} KB`);
}
