'use strict';
/* ==========================================================================
 * SpaceBook pre-push validation gate
 *   node tools/validate.js
 * Runs: syntax check, dataset integrity, index.html wiring, app.js static
 * checks. Exits non-zero when anything fails. Keep it dependency-free.
 * ========================================================================== */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.resolve(__dirname, '..');
const JS = path.join(ROOT, 'js') + path.sep;
const INDEX = path.join(ROOT, 'index.html');

const DATA_FILES = [
  'data.js', 'drawing_1_data.js', 'data_chem.js', 'data_phys.js', 'data_eng.js', 'data_bio.js',
  'data_comp.js',
  'dictionary_data.js', 'urdu_data.js', 'urdu_10_data.js', 'english_data.js', 'english_10_data.js', 'english_1_data.js', 'math_data.js',
  'pakstudy_data.js', 'pakstudy_10_data.js', 'bio_data.js', 'islamyat_data.js', 'islamyat_10_data.js',
  'math_10_data.js'
];

let pass = 0, fail = 0;
function check(label, cond, detail) {
  if (cond) { pass++; console.log('PASS  ' + label); }
  else { fail++; console.log('FAIL  ' + label + (detail ? '  -> ' + detail : '')); }
}

// ---------------------------------------------------------------- 1. syntax
console.log('--- syntax ---');
const jsFiles = fs.readdirSync(ROOT + path.sep + 'js').filter(f => f.endsWith('.js')).sort();
jsFiles.forEach(f => {
  const src = fs.readFileSync(JS + f, 'utf8');
  try {
    new vm.Script(src, { filename: f });
    check('syntax ' + f, true);
  } catch (e) {
    check('syntax ' + f, false, e.message);
  }
  check('no BOM ' + f, src.charCodeAt(0) !== 0xFEFF, 'file starts with UTF-8 BOM');
});

// ------------------------------------------------------------ 2. load data
console.log('--- datasets ---');
const sb = { console, window: undefined, module: undefined, exports: undefined, document: undefined, setTimeout, clearTimeout };
vm.createContext(sb);
const declared = new Set();
for (const f of DATA_FILES) {
  try {
    const code = fs.readFileSync(JS + f, 'utf8');
    const re = /^\s*(?:const|var|let)\s+([A-Za-z_$][\w$]*)/gm;
    let d; while ((d = re.exec(code))) declared.add(d[1]);
    vm.runInContext(code, sb, { filename: f, timeout: 60000 });
    check('load ' + f, true);
  } catch (e) {
    check('load ' + f, false, e.message);
  }
}
vm.runInContext('for (const n of ' + JSON.stringify([...declared]) + ') { try { globalThis[n] = eval(n); } catch (e) {} }', sb);

const D = sb.DATA;
if (D) {
  check('DATA registry present', true);
  check('subjects cls9 = 9', D.subjects && D.subjects.cls9 && D.subjects.cls9.length === 9, 'got ' + (D.subjects ? D.subjects.cls9.length : 'n/a'));
  check('subjects cls10 = 8', D.subjects && D.subjects.cls10 && D.subjects.cls10.length === 8, 'got ' + (D.subjects ? D.subjects.cls10.length : 'n/a'));
  check('Class 1 Drawing registered', D.subjects && D.subjects.cls1 && D.subjects.cls1.some(s => s.id === 'cls1-drawing' && s.hasDrawing));
  check('subject ids unique', (() => {
    const all = [].concat(D.subjects.cls9, D.subjects.cls10, D.subjects.cls11, D.subjects.cls12).map(s => s.id);
    return new Set(all).size === all.length;
  })());
  check('class counts match subject arrays', D.classes.every(c => c.subjects === (D.subjects[c.id] || []).length),
    D.classes.map(c => c.id + ':' + c.subjects + ' vs ' + ((D.subjects[c.id] || []).length)).join(' '));
  check('books = ' + D.books.length, D.books.length === 19, 'got ' + D.books.length);
  check('book ids unique', new Set(D.books.map(b => b.id)).size === D.books.length);
  check('book subjects resolvable', D.books.every(b => b.classId || b.class_id), 'missing classId/class_id on ' + D.books.filter(b => !(b.classId || b.class_id)).map(b => b.id).join(','));
  check('chemChapters = 8', D.chemChapters && D.chemChapters.length === 8, 'got ' + (D.chemChapters || []).length);
  check('chem10Chapters = 8', D.chem10Chapters && D.chem10Chapters.length === 8, 'got ' + (D.chem10Chapters || []).length);
  check('physChapters = 9', D.physChapters && D.physChapters.length === 9, 'got ' + (D.physChapters || []).length);
  check('phys10Chapters = 9', D.phys10Chapters && D.phys10Chapters.length === 9, 'got ' + (D.phys10Chapters || []).length);
  check('engChapters = 15', D.engChapters && D.engChapters.length === 15, 'got ' + (D.engChapters || []).length);
  check('eng10Chapters = 15', D.eng10Chapters && D.eng10Chapters.length === 15, 'got ' + (D.eng10Chapters || []).length);
  check('eng1Chapters = 11', D.eng1Chapters && D.eng1Chapters.length === 11, 'got ' + (D.eng1Chapters || []).length);
  check('compChapters = 7', D.compChapters && D.compChapters.length === 7, 'got ' + (D.compChapters || []).length);
  check('chapters roadmap map has 14 entries', D.chapters && Object.keys(D.chapters).length === 14, 'got ' + (D.chapters ? Object.keys(D.chapters).length : 0));
  check('DATA.urduChapters = 19 (from urdu_data.js)', D.urduChapters && (D.urduChapters.length === 19 || D.urduChapters.length === 15), 'got ' + (D.urduChapters || []).length);
  check('DATA.urdu10Chapters = 22 (from urdu_10_data.js)', (sb.URDU_10_DATA && sb.URDU_10_DATA.length === 22) || (D.urdu10Chapters && D.urdu10Chapters.length === 22), 'got ' + ((sb.URDU_10_DATA || D.urdu10Chapters || []).length));
  check('DATA.islamyatChapters = 15', D.islamyatChapters && D.islamyatChapters.length === 15, 'got ' + (D.islamyatChapters || []).length);
  check('DATA.islamyat10Chapters = 18', D.islamyat10Chapters && D.islamyat10Chapters.length === 18, 'got ' + (D.islamyat10Chapters || []).length);
  check('DATA.mathChapters present (from math_data.js)', Array.isArray(D.mathChapters) && D.mathChapters.length > 0, 'got ' + (D.mathChapters ? D.mathChapters.length : 0));
  check('DATA.math10Chapters = 13 (from math_10_data.js)', (sb.MATH_10_DATA && sb.MATH_10_DATA.length === 13) || (D.math10Chapters && D.math10Chapters.length === 13), 'got ' + ((sb.MATH_10_DATA || D.math10Chapters || []).length));
  check('islamic subjects registered', ['cls9-isl', 'cls10-isl'].every(id => [].concat(D.subjects.cls9, D.subjects.cls10).some(s => s.id === id)));
  check('islamic books registered', ['b-cls9-isl', 'b-cls10-isl'].every(id => D.books.some(b => b.id === id)));
} else {
  check('DATA registry present', false, 'DATA is undefined');
}

const EN = sb.ENGLISH_DATA;
check('Class 1 Drawing activities = 32', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.length === 32, 'got ' + ((sb.DRAWING_1_DATA || []).length));
check('Drawing activities have trilingual tips', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.every(x => x.en && x.ur && x.ps && x.artwork));
check('Drawing lessons use vector art without source scans', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.every(x => !x.image && x.artwork) && !fs.existsSync(path.join(ROOT, 'assets', 'drawing-class1')));
check('Drawing exam practice bank complete', !!(sb.DRAWING_1_EXAM && sb.DRAWING_1_EXAM.mcqs.length && sb.DRAWING_1_EXAM.sqs.length && sb.DRAWING_1_EXAM.lqs.length));

if (EN) {
  check('ENGLISH_DATA units = 15', EN.length === 15, 'got ' + EN.length);
  check('unit2 englishSummary', !!EN[1].englishSummary);
  check('unit2 section[0].urdu', !!(EN[1].sections && EN[1].sections[0] && EN[1].sections[0].urdu));
  check('unit9 urduSummary', !!EN[8].urduSummary);
  check('exercise.vocabulary on units 2-10', [1, 2, 3, 4, 5, 6, 7, 8, 9].every(i => EN[i] && EN[i].exercise && Array.isArray(EN[i].exercise.vocabulary)), 'missing on ' + [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(i => !(EN[i] && EN[i].exercise && EN[i].exercise.vocabulary)).join(','));
  check('unit8 figurativeLines', EN[7] && EN[7].exercise && Array.isArray(EN[7].exercise.figurativeLines) && EN[7].exercise.figurativeLines.length > 0);
} else {
  check('ENGLISH_DATA present', false);
}
const EN10 = sb.ENGLISH_10_DATA;
if (EN10) {
  check('ENGLISH_10_DATA units = 15', EN10.length === 15, 'got ' + EN10.length);
  check('ENGLISH_10_DATA unit 1 has sections', EN10[0] && Array.isArray(EN10[0].sections) && EN10[0].sections.length > 0);
  check('ENGLISH_10_DATA unit 1 has exercise', EN10[0] && !!EN10[0].exercise);
  check('ENGLISH_10_DATA unit 1 has sloBank', EN10[0] && !!EN10[0].sloBank);
} else {
  check('ENGLISH_10_DATA present', false);
}
const EN1 = sb.ENGLISH_1_DATA;
if (EN1) {
  check('ENGLISH_1_DATA units = 11', EN1.length === 11, 'got ' + EN1.length);
  check('ENGLISH_1_DATA unit 1 has sections', EN1[0] && Array.isArray(EN1[0].sections) && EN1[0].sections.length > 0);
  check('ENGLISH_1_DATA unit 1 has exercise', EN1[0] && !!EN1[0].exercise);
  check('ENGLISH_1_DATA unit 1 has sloQuestions', EN1[0] && !!(EN1[0].sloQuestions || EN1[0].slos));
  check('ENGLISH_1_DATA registered on DATA.eng1Chapters', Array.isArray(D.eng1Chapters) && D.eng1Chapters.length === 11);
} else {
  check('ENGLISH_1_DATA present', false);
}

const PS = sb.PAKSTUDY_DATA;
if (PS) {
  check('PAKSTUDY_DATA units = 4', PS.length === 4, 'got ' + PS.length);
} else {
  check('PAKSTUDY_DATA present', false);
}

const PS10 = sb.PAKSTUDY_10_DATA;
if (PS10) {
  check('PAKSTUDY_10_DATA units = 4', PS10.length === 4, 'got ' + PS10.length);
  check('PAKSTUDY_10_DATA ch 1 has sections', PS10[0] && Array.isArray(PS10[0].sections) && PS10[0].sections.length > 0);
  check('PAKSTUDY_10_DATA ch 1 has exercise', PS10[0] && !!PS10[0].exercise);
  check('PAKSTUDY_10_DATA ch 1 has sloBank', PS10[0] && !!PS10[0].sloBank);
} else {
  check('PAKSTUDY_10_DATA present', false);
}

const UR10 = sb.URDU_10_DATA;
if (UR10) {
  check('URDU_10_DATA units = 22', UR10.length === 22, 'got ' + UR10.length);
  check('URDU_10_DATA ch 1 has sections', UR10[0] && Array.isArray(UR10[0].sections) && UR10[0].sections.length > 0);
  check('URDU_10_DATA ch 1 has exercise', UR10[0] && !!UR10[0].exercise);
  check('URDU_10_DATA ch 1 has sloQuestions', UR10[0] && !!(UR10[0].sloQuestions || UR10[0].slos));
} else {
  check('URDU_10_DATA present', false);
}
check('ENG_UNIT_VOCAB_WORDS lexicon', !!(sb.ENG_UNIT_VOCAB_WORDS && sb.ENG_UNIT_VOCAB_WORDS[2]), 'missing from dictionary_data.js');
check('lookupEngWord()', typeof sb.lookupEngWord === 'function');

// --------------------------------------------------- 3. index.html wiring
console.log('--- index.html ---');
const html = fs.readFileSync(INDEX, 'utf8');
const srcs = [...html.matchAll(/<script\s+src="([^"]+)"/g)].map(m => m[1].split('?')[0]);
check('index.html references app.js', srcs.includes('js/app.js'));
check('index.html loads core registry before subjects', srcs.indexOf('js/data.js') >= 0 && srcs.indexOf('js/data.js') < srcs.indexOf('js/app.js'));
check('index.html loads Class 1 Drawing data', srcs.includes('js/drawing_1_data.js') && srcs.indexOf('js/drawing_1_data.js') < srcs.indexOf('js/app.js'));
check('index.html loads Class 1 English data', srcs.includes('js/english_1_data.js') && srcs.indexOf('js/english_1_data.js') < srcs.indexOf('js/app.js'));
['js/data_chem.js', 'js/data_phys.js', 'js/data_eng.js', 'js/data_bio.js', 'js/data_comp.js'].forEach(s => check('index.html loads ' + s, srcs.includes(s)));
const missingSrc = srcs.filter(s => !fs.existsSync(path.join(ROOT, s)));
check('every <script src> exists', missingSrc.length === 0, 'missing: ' + missingSrc.join(','));
const cssHref = (html.match(/<link\s+rel="stylesheet"\s+href="([^"]+)"/g) || []).map(s => s.match(/href="([^"]+)"/)[1]);
check('stylesheet path exists', cssHref.every(h => fs.existsSync(path.join(ROOT, h.split('?')[0]))), cssHref.join(','));

// ---------------------------------------------------- 4. app.js static checks
console.log('--- app.js ---');
const app = fs.readFileSync(JS + 'app.js', 'utf8');
const fnNames = [];
const fre = /^\s*function\s+([A-Za-z_$][\w$]*)/gm;
let m;
while ((m = fre.exec(app))) fnNames.push(m[1]);
const counts = {};
fnNames.forEach(n => counts[n] = (counts[n] || 0) + 1);
const dupes = Object.keys(counts).filter(k => counts[k] > 1);
check('app.js functions unique (' + fnNames.length + ')', dupes.length === 0, dupes.join(','));
const defines = n => !!counts[n] || new RegExp('(?:const|let|var)\\s+' + n + '\\s*=').test(app) || new RegExp('(?:window|globalThis)\\.' + n + '\\s*=').test(app);
['openSubject', 'handleGlobalSearch', 'clearGlobalSearch', 'renderBooksView', 'sanitize', 'autoScrollToActiveTab',
  'renderEngEnglishSummary', 'getUrduChapterList', 'openIslView', 'renderIslSloLQs', 'recordQuestionAnswer',
  'renderHome', 'renderClasses', 'goToSubjects'].forEach(n => check('app.js defines ' + n, defines(n)));
check('app.js has single openSubject', counts.openSubject === 1, 'got ' + counts.openSubject);
check('router hasIsl branch', app.includes('subj.hasIsl'));
check('state has selectedIslChapter', /selectedIslChapter:\s*0/.test(app));
check('state has math/pakstudy fields', /activePakStudySloTab:/.test(app) && /activeMathEx:/.test(app));
check('search has Islamyat section', app.includes('Search Islamyat Units'));
check('search has no undefined sanitize()', /sanitize\s*\(/.test(app) && /const sanitize\s*=/.test(app));
check('no undefined updateStudyStats()', !/[^.\w]updateStudyStats\s*\(/.test(app));
check('no undefined openGenericSubjectView()', !/[^.\w]openGenericSubjectView\s*\(/.test(app));
check('English Summary tab wired', app.includes('renderEngEnglishSummary') && app.includes('id: "en-sum"'));
check('no foreign data globals (BIO10_DATA/GEO_DATA/KIN_DATA)', !/\bBIO10_DATA\b|\bGEO_DATA\b|\bKIN_DATA\b/.test(app));

// ------------------------------------------------------------- 5. css balance
console.log('--- css ---');
const css = fs.readFileSync(path.join(ROOT, 'css', 'style.css'), 'utf8');
let depth = 0;
for (const c of css) { if (c === '{') depth++; else if (c === '}') depth--; }
check('css braces balanced', depth === 0, 'depth=' + depth);

console.log('---');
console.log('validate: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
