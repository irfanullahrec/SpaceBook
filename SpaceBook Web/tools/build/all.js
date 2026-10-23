'use strict';
/* One command for every derived file of the app (Phase 3).
 *   node --max-old-space-size=8192 tools/build/all.js           regenerate everything
 *   node --max-old-space-size=8192 tools/build/all.js --check    change nothing; exit 1 when a committed output is stale (CI)
 *   node tools/build/all.js --list                               what is generated, from what, with which command
 *   node tools/build/all.js --only lazy,word-stats               a subset (names from --list)
 * A step regenerates its outputs from the book data in js/. In --check mode the generator really runs (they are deterministic apart from
 * a generation date, which is ignored), the result is compared with the committed file, and the committed file is put back, so a
 * stale output is reported and the working tree is left as it was.
 * Run it before every commit that touches book data or the script list of index.html, and from a clean checkout before a release:
 * generated files describe the committed data, not whatever else is lying in the working tree. */
const fs = require('fs'), path = require('path'), { spawnSync } = require('child_process');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const CHECK = args.includes('--check');
const only = args.includes('--only') ? args[args.indexOf('--only') + 1].split(',') : null;

const node = (...a) => ({ cmd: process.execPath, args: ['--max-old-space-size=8192', ...a] });
const STEPS = [
  { id: 'word-stats', what: 'word counts per project, class and subject (My Stats / Project Stats)',
    outputs: ['js/word_stats_summary.js', 'js/word_stats_words.js'], touches: ['tools/word_stats/last_build_report.txt'], run: node('tools/word_stats/build_word_stats.js') },
  { id: 'mcq-bank', what: 'one MCQ bank from all books (Tests Preps) and the list of questions that still need an answer key',
    outputs: ['js/test_prep_bank.js', 'docs/test_prep_review/no_key.csv'], touches: ['tools/test_prep/last_bank_report.txt'], run: node('tools/test_prep/build_mcq_bank.js') },
  { id: 'study-index', what: 'chapter and question counts per subject (Study Plan)',
    outputs: ['js/study_plan_index.js'], touches: ['tools/study_plan/last_build_report.txt'], run: node('tools/study_plan/build_study_index.js') },
  { id: 'lexicon', what: 'offline word meanings of all books in one file (Lexicon v1: hover and selection lookups, no book is loaded)',
    outputs: ['js/lexicon_data.js'], run: node('tools/build/make_lexicon.js') },
  // last: lazy.html carries the content hash of every script, including the generated ones above
  { id: 'lazy', what: 'lazy page and its manifest (client-side lazy loading of the book files)',
    outputs: ['lazy.html', 'content/lazy_manifest.json'], run: node('tools/build/make_lazy.js'), checkNative: node('tools/build/make_lazy.js', '--check') },
  // after the lazy page (the book data it hashes), before the offline map (which lists each subject's search files)
  { id: 'search', what: 'search index per subject (header search finds words inside the books, offline)',
    outputs: ['content/search/index.json'], run: node('tools/build/make_search.js'), checkNative: node('tools/build/make_search.js', '--check') },
  // after the search index (it reads the chapter calls from it): what the Android app lists, so the app and the website cannot disagree about classes, subjects and chapters
  { id: 'app-catalog', what: 'classes, subjects and chapters the Android app lists, with the call that opens each chapter (assets/app_catalog.json in the app)',
    outputs: ['content/app_catalog.json'], run: node('tools/build/make_app_catalog.js'), checkNative: node('tools/build/make_app_catalog.js', '--check') },
  // after the catalog (chapters of each subject): the questions of every book for "Create Test", one file per class (the check compares the hash of the inputs, no book is loaded)
  { id: 'testbank', what: 'questions of all books by subject, chapter and topic, with answers (Create Test)',
    outputs: ['content/testbank/index.json'], run: node('tools/tests/build_test_bank.js'), checkNative: node('tools/tests/build_test_bank.js', '--check') },
  // after the lazy page: it lists what each subject loads and the shell of the service worker (both carry content hashes of the files above)
  { id: 'offline', what: 'what each subject needs offline, and the service worker version (Download for offline, sw.js)',
    outputs: ['content/offline_map.json', 'content/sw_version.js'], run: node('tools/build/make_offline.js'), checkNative: node('tools/build/make_offline.js', '--check') },
];

if (args.includes('--list')) {
  STEPS.forEach(s => console.log(s.id.padEnd(12) + s.outputs.join(', ').padEnd(60) + ' <- ' + path.relative(ROOT, s.run.args[1]) + '\n' + ' '.repeat(12) + s.what));
  process.exit(0);
}

// the generation date is the only thing that changes between two runs on the same data
const norm = text => text.replace(/\r\n/g, '\n').replace(/"generated":"[0-9T:.\-Z]+"/g, '"generated":"-"');
const read = f => (fs.existsSync(path.join(ROOT, f)) ? fs.readFileSync(path.join(ROOT, f), 'utf8') : null);
const exec = c => spawnSync(c.cmd, c.args, { cwd: ROOT, encoding: 'utf8', maxBuffer: 1 << 28 });
const tail = r => String(r.stdout || '').split('\n').filter(Boolean).slice(-2).join(' | ').slice(0, 200) + (r.stderr ? ' ' + String(r.stderr).split('\n').filter(Boolean).slice(-2).join(' | ').slice(0, 300) : '');

let stale = 0, failed = 0;
for (const step of STEPS.filter(s => !only || only.includes(s.id))) {
  const t0 = Date.now();
  if (CHECK && step.checkNative) {
    const r = exec(step.checkNative);
    const ok = r.status === 0;
    console.log((ok ? 'fresh  ' : 'STALE  ') + step.id.padEnd(12) + (ok ? '' : tail(r)) + `  (${((Date.now() - t0) / 1000).toFixed(0)} s)`);
    if (!ok) stale++;
    continue;
  }
  const files = step.outputs.concat(step.touches || []);
  const before = Object.fromEntries(files.map(f => [f, read(f)]));
  const r = exec(step.run);
  if (r.status !== 0) {
    files.forEach(f => { if (before[f] !== null) fs.writeFileSync(path.join(ROOT, f), before[f]); });   // a crashed generator must not leave half a file
    console.log('FAILED ' + step.id.padEnd(12) + tail(r));
    failed++;
    continue;
  }
  const changed = step.outputs.filter(f => before[f] === null || norm(before[f]) !== norm(read(f)));
  if (CHECK) {
    files.forEach(f => { if (before[f] !== null) fs.writeFileSync(path.join(ROOT, f), before[f]); });     // leave the working tree as it was
    console.log((changed.length ? 'STALE  ' : 'fresh  ') + step.id.padEnd(12) + (changed.length ? changed.join(', ') + ' differ from what the book data produces' : '') + `  (${((Date.now() - t0) / 1000).toFixed(0)} s)`);
    if (changed.length) stale++;
  } else {
    console.log((changed.length ? 'wrote  ' : 'same   ') + step.id.padEnd(12) + (changed.length ? changed.join(', ') : '') + `  (${((Date.now() - t0) / 1000).toFixed(0)} s)`);
  }
}
if (CHECK && stale) console.log(`\n${stale} derived output(s) are stale: run  node --max-old-space-size=8192 tools/build/all.js  and commit the result.`);
if (failed) console.log(`\n${failed} step(s) failed.`);
process.exit(stale || failed ? 1 : 0);
