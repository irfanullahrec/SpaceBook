'use strict';
/* Chapter-by-chapter exercise completeness and answer coverage of every book that holds its exercises as data.
 *   node --max-old-space-size=6144 tools/launch/exercise_coverage.js [--from leaves.json] [--check] [--write-baseline]
 *
 * What it reads: the same records the Create Test bank is made of (tools/tests/extract_leaves.js: every question, and every part of a question, that a
 * student can be asked, with the answer exactly as the Ans button shows it), for every CLSn_BOOKS book and the five Mathematics books of Classes
 * 5, 6, 7, 8 and 11. It does NOT read the scans: that every printed question is present is the page-by-page work of docs/source-verification
 * (see docs/launch/COVERAGE_MANIFEST.md for the page side). What it can prove is the shape: no chapter that has an exercise lost its questions
 * (the baseline), every question has an answer, an MCQ's answer names one of its options, no two sources of an answer disagree.
 *
 * Per chapter: exercises (distinct exercise blocks the questions sit in), questions (leaves) and where each answer comes from. The counts come from
 * tools/audit/answers_audit.js (run here with --json) for every CLSn_BOOKS book, because that audit asks the reader itself whether an Ans button has an
 * answer to show; the Mathematics books of Classes 5, 6, 7, 8 and 11 are not CLSn_BOOKS and are counted from the leaf records:
 *   ans      the question or part has an answer record of its own (a worked solution or a stated answer)
 *   viaQ     no record of its own, the question it belongs to has one (one Ans button for the whole question)
 *   key      the book's own printed answer key has a line for exactly this part
 *   written  an answer written for the project (js/answers_extra.js), not printed in the book
 *   whole    only the printed line of the whole question exists (shown whole, not guessed per part)
 *   none     no answer anywhere
 *   head     a group heading ("Short Questions"): no answer by design, not counted as a question
 * plus MCQs whose answer cannot be matched to an option (mcqOpen) and MCQs where the solution and the printed key name different options (clash).
 * Output: docs/launch/EXERCISE_COVERAGE.json, EXERCISE_COVERAGE.md, exercise_coverage.csv (all three are generated; do not edit by hand).
 * --check fails when a chapter has fewer questions than in the committed baseline (an omission), more unanswered questions, more open MCQs or more clashes.
 * Dev-only, never deployed. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
process.chdir(ROOT);
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const OUT = path.join(ROOT, 'docs', 'launch');
const BASE = path.join(OUT, 'exercise_coverage_baseline.json');

const MATH_SOLUTIONS = [5, 6, 7, 8, 11].map(n => 'js/math_' + n + '_solutions.js');
let raw;
if (opt('--from')) raw = JSON.parse(fs.readFileSync(opt('--from'), 'utf8'));
else {
  const { load } = require('../lib/app_sandbox');
  const extract = require('../tests/extract_leaves');
  const app = load({ page: process.env.SB_PAGE || 'lazy.html', quiet: true });
  for (const f of MATH_SOLUTIONS) app.run(fs.readFileSync(path.join(ROOT, f), 'utf8'));
  raw = JSON.parse(app.run('JSON.stringify((' + extract.toString() + ')())', 900000));
}
const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));
const subjectName = {};
const chapterTitles = {};
for (const c of catalog.classes) for (const s of c.subjects) { subjectName[s.id] = s.name; chapterTitles[s.id] = s.chapters.map(x => x.t); }

// book id "cls9:phy" -> subject id; the catalog's ids are cls<N>-<suffix> and a few keys differ
const ALIAS = { 'cls9:phys': 'cls9-phy', 'cls10:phys': 'cls10-phy', 'cls11:phys': 'cls11-phy', 'cls12:phys': 'cls12-phy', 'cls12:pakstudy': 'cls12-pak', 'cls11:comp': 'cls11-cs',
  'cls11:islhist': 'cls11-ishist', 'cls11:islopt': 'cls11-ikhtiari', 'cls11:quran': 'cls11-mq', 'cls11:islc': 'cls11-isl' };
const subjectOf = id => {
  if (ALIAS[id]) return ALIAS[id];
  const [c, k] = id.split(':'); const want = c + '-' + k;
  if (subjectName[want]) return want;
  return null;
};

const books = {};
for (const bk of raw.books) {
  const sid = subjectOf(bk.id) || bk.id;
  books[bk.id] = { book: bk.id, subject: sid, name: subjectName[sid] || bk.title || bk.id, cls: bk.cls, listed: !!subjectName[sid],
    chapters: bk.units.map((u, i) => ({ n: i, number: u.n, title: u.title, exSections: u.secs.filter(s => s.ex).length, sections: u.secs.length, exercises: new Set(), pages: [],
      q: 0, ans: 0, viaQ: 0, key: 0, written: 0, whole: 0, none: 0, head: 0, mcq: 0, mcqOpen: 0, clash: 0, fig: 0 })) };
}
// the audit (the reader's own answer lookup) decides what counts as answered in the CLSn_BOOKS books
let audit = [];
if (opt('--audit')) audit = JSON.parse(fs.readFileSync(opt('--audit'), 'utf8'));
else {
  const tmp = path.join(require('os').tmpdir(), 'sb_audit_' + process.pid + '.json');
  require('child_process').execFileSync(process.execPath, ['--max-old-space-size=6144', path.join(ROOT, 'tools', 'audit', 'answers_audit.js'), '--json', tmp], { stdio: 'ignore', maxBuffer: 1 << 28 });
  audit = JSON.parse(fs.readFileSync(tmp, 'utf8')); fs.unlinkSync(tmp);
}
const audited = new Set();
for (const a of audit) {
  const B = books[a.id]; if (!B) continue;
  audited.add(a.id);
  for (const [u, c] of Object.entries(a.byUnit || {})) {
    const ch = B.chapters[+u]; if (!ch) continue;
    ch.q = c.leaves - c.head; ch.head = c.head; ch.ans = c.ans; ch.viaQ = c.viaQ; ch.key = c.key; ch.written = c.extra; ch.whole = c.whole; ch.none = c.none + c.dangling;
  }
}
for (const L of raw.leaves) {
  const B = books[L.b]; if (!B) continue;
  const ch = B.chapters[L.u]; if (!ch) continue;
  if (L.ex) ch.exercises.add(L.ex);
  if (L.pg != null && L.pg !== '') ch.pages.push(+L.pg || L.pg);
  const has = !!(L.a && String(L.a).trim()) || !!(L.st && String(L.st).trim());
  if (!audited.has(L.b)) {
    ch.q++;
    if (!has) ch.none++; else if (L.src === 'key') ch.key++; else if (L.src === 'extra') ch.written++; else ch.ans++;
  }
  if (L.o) { ch.mcq++; if (has && L.cor < 0 && !L.wl) ch.mcqOpen++; }
  if (L.clash) ch.clash++;
  if (L.fig) ch.fig++;
}

const rows = [];       // one per chapter
const bookRows = [];   // one per book
const ZERO = () => ({ q: 0, ans: 0, viaQ: 0, key: 0, written: 0, whole: 0, none: 0, head: 0, mcq: 0, mcqOpen: 0, clash: 0, fig: 0 });
for (const B of Object.values(books)) {
  const tot = ZERO(); let exCh = 0, emptyEx = 0;
  for (const ch of B.chapters) {
    const nums = ch.pages.filter(x => typeof x === 'number');
    const row = { book: B.book, subject: B.subject, cls: B.cls, n: ch.n, number: ch.number, title: ch.title,
      printed: nums.length ? [Math.min(...nums), Math.max(...nums)] : null,
      exerciseSections: ch.exSections, exercises: [...ch.exercises].sort(), q: ch.q, ans: ch.ans, viaQ: ch.viaQ, key: ch.key, written: ch.written, whole: ch.whole, none: ch.none, head: ch.head,
      mcq: ch.mcq, mcqOpen: ch.mcqOpen, clash: ch.clash, fig: ch.fig };
    row.state = ch.exSections === 0 && ch.q === 0 ? 'no-exercise' : (ch.q === 0 ? 'EXERCISE-WITHOUT-QUESTIONS' : (ch.none ? 'unanswered' : (ch.whole || ch.mcqOpen || ch.clash ? 'check-answers' : 'complete')));
    rows.push(row);
    for (const k of Object.keys(tot)) tot[k] += ch[k] || 0;
    if (ch.exSections || ch.q) exCh++;
    if (ch.exSections && !ch.q) emptyEx++;
  }
  bookRows.push(Object.assign({ book: B.book, subject: B.subject, name: B.name, cls: B.cls, listed: B.listed, method: audited.has(B.book) ? 'audit' : 'leaves', chapters: B.chapters.length, chaptersWithExercise: exCh, exerciseChaptersWithoutQuestions: emptyEx }, tot));
}
// subjects of the catalog that no book with questions covers
const covered = new Set(bookRows.filter(b => b.q).map(b => b.subject));
const uncovered = [];
for (const c of catalog.classes) for (const s of c.subjects) if (!covered.has(s.id)) uncovered.push({ subject: s.id, name: s.name, cls: +c.id.replace('cls', ''), chapters: s.chapters.length, exerciseItemsListed: s.chapters.reduce((n, x) => n + (x.n || 0), 0), inRegistry: bookRows.some(b => b.subject === s.id) });
const unlisted = bookRows.filter(b => !b.listed).map(b => b.book);

const result = { schema: 'spacebook.exercise-coverage/2', books: bookRows, chapters: rows, subjectsWithoutQuestions: uncovered, booksNotInCatalog: unlisted };
const sum = k => bookRows.reduce((n, b) => n + b[k], 0);
const totals = { books: bookRows.filter(b => b.q).length, chapters: rows.filter(r => r.q || r.exerciseSections).length, questions: sum('q'), ans: sum('ans'), viaQ: sum('viaQ'), key: sum('key'), written: sum('written'), whole: sum('whole'), none: sum('none'), heads: sum('head'),
  mcq: sum('mcq'), mcqOpen: sum('mcqOpen'), clash: sum('clash'),
  chaptersExerciseWithoutQuestions: rows.filter(r => r.state === 'EXERCISE-WITHOUT-QUESTIONS').length, chaptersUnanswered: rows.filter(r => r.state === 'unanswered').length };
result.totals = totals;

if (args.includes('--check')) {
  if (!fs.existsSync(BASE)) { console.error('no baseline: run with --write-baseline'); process.exit(1); }
  const base = JSON.parse(fs.readFileSync(BASE, 'utf8'));
  const bad = [];
  const was = new Map(base.chapters.map(r => [r.book + '#' + r.n, r]));
  for (const r of rows) {
    const b = was.get(r.book + '#' + r.n);
    if (!b) continue;
    if (r.q < b.q) bad.push(`${r.book} ch${r.n} "${r.title}": ${r.q} questions, baseline ${b.q} (omission)`);
    if (r.none > b.none) bad.push(`${r.book} ch${r.n}: ${r.none} unanswered, baseline ${b.none}`);
    if (r.mcqOpen > b.mcqOpen) bad.push(`${r.book} ch${r.n}: ${r.mcqOpen} MCQs whose answer matches no option, baseline ${b.mcqOpen}`);
    if (r.clash > b.clash) bad.push(`${r.book} ch${r.n}: ${r.clash} answer clashes, baseline ${b.clash}`);
  }
  const now = new Set(rows.map(r => r.book + '#' + r.n));
  for (const k of was.keys()) if (!now.has(k)) bad.push('chapter ' + k + ' is gone');
  if (bad.length) { console.error(bad.slice(0, 40).join('\n')); console.error(bad.length + ' regression(s) against docs/launch/exercise_coverage_baseline.json'); process.exit(1); }
  console.log('exercise coverage: no chapter lost questions or gained unanswered ones (' + totals.questions + ' questions in ' + totals.chapters + ' chapters, ' + totals.none + ' still unanswered)');
  process.exit(0);
}

fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, 'EXERCISE_COVERAGE.json'), JSON.stringify(result) + '\n');
const csv = ['class,subject,book,chapter_no,chapter,printed_from,printed_to,exercise_blocks,questions,own_answer,via_question,printed_key,written,whole_line_only,unanswered,headings,mcq,mcq_open,clash,state'];
const q = s => '"' + String(s == null ? '' : s).replace(/"/g, '""') + '"';
for (const r of rows) csv.push([r.cls, r.subject, r.book, r.number == null ? r.n + 1 : r.number, q(r.title), r.printed ? r.printed[0] : '', r.printed ? r.printed[1] : '', r.exercises.length, r.q, r.ans, r.viaQ, r.key, r.written, r.whole, r.none, r.head, r.mcq, r.mcqOpen, r.clash, r.state].join(','));
fs.writeFileSync(path.join(OUT, 'exercise_coverage.csv'), csv.join('\n') + '\n');

const md = [];
md.push('# Exercise completeness and answer coverage, chapter by chapter');
md.push('');
md.push('Generated by `tools/launch/exercise_coverage.js` from the books as the app holds them. **Do not edit by hand.** The per-chapter table is `exercise_coverage.csv` (one row per chapter); `EXERCISE_COVERAGE.json` has the same data for tools.');
md.push('');
md.push('What this proves and what it does not: it proves that every question the app holds has an answer (or is named below), that an MCQ answer names one of its options, and that no chapter loses questions in the future (`--check`). It does **not** prove that the questions equal the printed ones: that is the page-by-page work of `docs/source-verification/`, sampled and disclosed in `VERIFICATION_REPORT.md`.');
md.push('');
md.push('Answer columns: **own** = a record of its own (worked solution or stated answer); **via question** = the question it belongs to has one Ans for all its parts; **key** = the book\'s printed answer key; **written** = written for the project (`js/answers_extra.js`), not printed in the book; **whole line** = only the printed line of the whole question exists; **none** = nothing to show.');
md.push('');
md.push('## Totals');
md.push('');
md.push('| Books with questions | Chapters with an exercise | Questions (and parts) | Own answer | Via question | Printed key | Written | Whole line only | **No answer** | MCQs | MCQ answer matches no option | Answer clashes |');
md.push('|---|---|---|---|---|---|---|---|---|---|---|---|');
md.push(`| ${totals.books} | ${totals.chapters} | ${totals.questions} | ${totals.ans} | ${totals.viaQ} | ${totals.key} | ${totals.written} | ${totals.whole} | **${totals.none}** | ${totals.mcq} | ${totals.mcqOpen} | ${totals.clash} |`);
md.push('');
md.push(`Chapters whose exercise block holds no question: **${totals.chaptersExerciseWithoutQuestions}**. Chapters with at least one unanswered question: **${totals.chaptersUnanswered}**.`);
md.push('');
md.push('## Subjects without questions held as data (need their own check)');
md.push('');
if (!uncovered.length) md.push('None: every subject of the catalog holds its questions as data.');
else {
  md.push('These subjects have no question records in the registries this report reads (their exercises, if any, are in older card-per-scan data or in exercise banks), so it cannot count them. The last columns say what the catalog lists as exercise items and whether the book exists in the registry.');
  md.push('');
  md.push('| Class | Subject | Chapters | Exercise items in the catalog | In the book registry |');
  md.push('|---|---|---|---|---|');
  for (const u of uncovered) md.push(`| ${u.cls} | ${u.name} (\`${u.subject}\`) | ${u.chapters} | ${u.exerciseItemsListed} | ${u.inRegistry ? 'yes, with no questions' : 'no'} |`);
}
md.push('');
md.push('## By book');
md.push('');
md.push('| Class | Subject | Chapters | With exercise | Questions | Own | Via question | Key | Written | Whole line | **No answer** | MCQs | Open MCQs | Clashes |');
md.push('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|');
for (const b of bookRows.filter(x => x.q).sort((a, c) => a.cls - c.cls || a.subject.localeCompare(c.subject))) {
  md.push(`| ${b.cls} | ${b.name} (\`${b.book}\`) | ${b.chapters} | ${b.chaptersWithExercise} | ${b.q} | ${b.ans} | ${b.viaQ} | ${b.key} | ${b.written} | ${b.whole} | ${b.none ? '**' + b.none + '**' : 0} | ${b.mcq} | ${b.mcqOpen} | ${b.clash} |`);
}
md.push('');
md.push('## Chapters that need attention');
md.push('');
const attn = rows.filter(r => r.state !== 'complete' && r.state !== 'no-exercise');
if (!attn.length) md.push('None.');
else {
  md.push(`${attn.length} chapters. (The same rows, with every chapter, are in \`exercise_coverage.csv\`.)`);
  md.push('');
  md.push('| Class | Book | Chapter | Printed pages | Exercise sections | Questions | No answer | Whole line | Open MCQs | Clashes | State |');
  md.push('|---|---|---|---|---|---|---|---|---|---|---|');
  for (const r of attn.sort((a, c) => a.cls - c.cls || a.book.localeCompare(c.book) || a.n - c.n)) {
    md.push(`| ${r.cls} | \`${r.book}\` | ${r.number == null ? r.n + 1 : r.number}. ${String(r.title).replace(/\|/g, '/').slice(0, 60)} | ${r.printed ? r.printed[0] + '-' + r.printed[1] : ''} | ${r.exerciseSections} | ${r.q} | ${r.none} | ${r.whole} | ${r.mcqOpen} | ${r.clash} | ${r.state} |`);
  }
}
md.push('');
fs.writeFileSync(path.join(OUT, 'EXERCISE_COVERAGE.md'), md.join('\n'));
if (args.includes('--write-baseline')) {
  fs.writeFileSync(BASE, JSON.stringify({ schema: 'spacebook.exercise-coverage-baseline/2', chapters: rows.map(r => ({ book: r.book, n: r.n, q: r.q, none: r.none, mcqOpen: r.mcqOpen, clash: r.clash })) }) + '\n');
  console.log('baseline written');
}
console.log(`exercise coverage: ${totals.books} books, ${totals.chapters} chapters, ${totals.questions} questions: ${totals.ans} own answer, ${totals.viaQ} via question, ${totals.key} printed key, ${totals.written} written, ${totals.whole} whole line, ${totals.none} UNANSWERED; ${totals.mcqOpen} open MCQs, ${totals.clash} clashes; ${totals.chaptersExerciseWithoutQuestions} exercise chapters without questions; ${uncovered.length} subjects without question data`);
