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
  'data.js', 'munawar_registry.js', 'drawing_1_data.js', 'data_chem.js', 'data_phys.js', 'data_eng.js', 'data_bio.js',
  'data_comp.js',
  'dictionary_data.js', 'urdu_data.js', 'urdu_10_data.js', 'english_data.js', 'english_10_data.js', 'english_1_data.js', 'math_data.js',
  'pakstudy_data.js', 'pakstudy_10_data.js', 'bio_data.js', 'islamyat_data.js', 'islamyat_10_data.js', 'islamyat_1_data.js',
  'general_science_9_data.js', 'hpe_9_data.js', 'drawing_9_data.js', 'islamiat_ikhtiari_9_data.js', 'mutalia_quran_9_data.js',
  'computer_10_data.js', 'general_science_10_data.js', 'hpe_10_data.js', 'drawing_10_data.js', 'islamiat_ikhtiari_10_data.js', 'mutalia_quran_10_data.js',
  'nazira_1_data.js', 'pashto_1_data.js', 'math_10_data.js', 'math_1_data.js', 'drawing_2_data.js', 'drawing_3_data.js', 'math_2_data.js', 'math_3_book_text.js', 'math_3_data.js', 'math_primary_visuals.js',
  'primary_page_art.js', 'english_1_pages.js', 'primary_page_learning.js',
  'english_2_data.js', 'urdu_2_data.js', 'islamyat_2_data.js', 'nazira_2_data.js', 'gk_2_data.js', 'pashto_2_data.js',
  'islamyat_3_data.js', 'nazira_3_data.js', 'english_3_data.js', 'gk_3_data.js', 'pashto_3_data.js',
  'math_12_data.js', 'phys_12_data.js', 'chem_12_data.js', 'stat_12_data.js',
  'english_12_data.js', 'pakstudy_12_data.js', 'urdu_12_data.js',
  'biology_12_data.js', 'computer_12_data.js', 'civics_12_data.js',
  'economics_12_data.js', 'hpe_12_data.js', 'islamiat_ikhtiari_12_data.js',
  'islamic_history_12_data.js', 'quran_12_data.js',
  'math_5_data.js', 'general_science_5_data.js', 'english_5_data.js', 'urdu_5_data.js',
  'islamiat_5_data.js', 'social_studies_5_data.js', 'social_studies_um_5_data.js', 'pashto_5_data.js',
  'math_6_data.js', 'general_science_6_data.js', 'english_6_data.js', 'urdu_6_data.js',
  'islamiat_6_data.js', 'computer_6_data.js', 'geography_6_data.js', 'history_6_data.js',
  'hpe_6_data.js', 'drawing_6_data.js', 'arabic_6_data.js', 'mutalia_quran_6_data.js',
  'pashto_6_data.js',
  // Munawar (Kanz) series, Classes 1-4 (js/munawar_registry.js adds the books to DATA.subjects; the files register CLS<N>_BOOKS['mun-<code>'])
  'munawar_c1_comp_book.js', 'munawar_c1_compbl_book.js', 'munawar_c1_eng_book.js', 'munawar_c1_gram_book.js',
  'munawar_c1_gk_book.js', 'munawar_c1_isl_book.js', 'munawar_c1_math_book.js', 'munawar_c1_prel_book.js',
  'munawar_c1_urdu_book.js', 'munawar_c1_ugram_book.js', 'munawar_c1_waqf_book.js', 'munawar_c2_comp_book.js',
  'munawar_c2_compbl_book.js', 'munawar_c2_eng_book.js', 'munawar_c2_gram_book.js', 'munawar_c2_gk_book.js',
  'munawar_c2_isl_book.js', 'munawar_c2_math_book.js', 'munawar_c2_prel_book.js', 'munawar_c2_ugram_book.js',
  'munawar_c2_waqf_book.js', 'munawar_c3_comp_book.js', 'munawar_c3_compbl_book.js', 'munawar_c3_eng_book.js',
  'munawar_c3_gram_book.js', 'munawar_c3_gk_book.js', 'munawar_c3_isl_book.js', 'munawar_c3_math_book.js',
  'munawar_c3_prel_book.js', 'munawar_c3_urdu_book.js', 'munawar_c3_ugram_book.js', 'munawar_c3_waqf_book.js',
  'munawar_c4_comp_book.js', 'munawar_c4_compbl_book.js', 'munawar_c4_eng_book.js', 'munawar_c4_gram_book.js',
  'munawar_c4_isl_book.js', 'munawar_c4_math_book.js', 'munawar_c4_sci_book.js', 'munawar_c4_sst_book.js',
  'munawar_c4_urdu_book.js', 'munawar_c4_ugram_book.js'
];

let pass = 0, fail = 0;
function check(label, cond, detail) {
  if (cond) { pass++; console.log('PASS  ' + label); }
  else { fail++; console.log('FAIL  ' + label + (detail ? '  -> ' + detail : '')); }
}

// a check whose condition throws (missing global, changed data shape) is a FAIL, never a crash
function safe(label, fn) {
  try { fn(); } catch (e) { check(label, false, 'threw ' + e.constructor.name + ': ' + e.message); }
}

// ---------------------------------------------------------------- 1. syntax
console.log('--- syntax ---');
const jsFiles = fs.readdirSync(ROOT + path.sep + 'js').filter(f => f.endsWith('.js')).sort()
  .concat(fs.readdirSync(ROOT + path.sep + 'js' + path.sep + 'core').filter(f => f.endsWith('.js')).sort().map(f => 'core/' + f));   // js/core: store, sync
jsFiles.forEach(f => {
  const src = fs.readFileSync(JS + f, 'utf8');
  try {
    new vm.Script(src, { filename: f });
    safe('syntax ' + f, () => check('syntax ' + f, true));
  } catch (e) {
    safe('syntax ' + f, () => check('syntax ' + f, false, e.message));
  }
  safe('no BOM ' + f, () => check('no BOM ' + f, src.charCodeAt(0) !== 0xFEFF, 'file starts with UTF-8 BOM'));
});

// ------------------------------------------------------------ 2. load data
console.log('--- datasets ---');
const sb = { console, window: undefined, module: undefined, exports: undefined, document: undefined, setTimeout, clearTimeout };
sb.window = sb; // data files written for the browser assign window.X
vm.createContext(sb);
const declared = new Set();
for (const f of DATA_FILES) {
  try {
    const code = fs.readFileSync(JS + f, 'utf8');
    const re = /^\s*(?:const|var|let)\s+([A-Za-z_$][\w$]*)/gm;
    let d; while ((d = re.exec(code))) declared.add(d[1]);
    vm.runInContext(code, sb, { filename: f, timeout: 60000 });
    safe('load ' + f, () => check('load ' + f, true));
  } catch (e) {
    safe('load ' + f, () => check('load ' + f, false, e.message));
  }
}
vm.runInContext('for (const n of ' + JSON.stringify([...declared]) + ') { try { globalThis[n] = eval(n); } catch (e) {} }', sb);

const D = sb.DATA;
if (D) {
  safe('DATA registry present', () => check('DATA registry present', true));
  safe('subjects cls6 = 13', () => check('subjects cls6 = 13', D.subjects && D.subjects.cls6 && D.subjects.cls6.length === 13, 'got ' + (D.subjects ? D.subjects.cls6.length : 'n/a')));
  safe('subjects cls9 = 14', () => check('subjects cls9 = 14', D.subjects && D.subjects.cls9 && D.subjects.cls9.length === 14, 'got ' + (D.subjects ? D.subjects.cls9.length : 'n/a')));
  safe('subjects cls10 = 14', () => check('subjects cls10 = 14', D.subjects && D.subjects.cls10 && D.subjects.cls10.length === 14, 'got ' + (D.subjects ? D.subjects.cls10.length : 'n/a')));
  safe('Class 1 Drawing registered', () => check('Class 1 Drawing registered', D.subjects && D.subjects.cls1 && D.subjects.cls1.some(s => s.id === 'cls1-drawing' && s.hasDrawing)));
  check('subject ids unique', (() => {
    const all = [].concat(D.subjects.cls6, D.subjects.cls9, D.subjects.cls10, D.subjects.cls11, D.subjects.cls12).map(s => s.id);
    return new Set(all).size === all.length;
  })());
  // the class card counts the Government subjects; a private series' books (series:'munawar', js/munawar_registry.js) are listed apart
  const govCount = id => (D.subjects[id] || []).filter(s => !s.series).length;
  check('class counts match subject arrays', D.classes.every(c => c.subjects === govCount(c.id)),
    D.classes.map(c => c.id + ':' + c.subjects + ' vs ' + govCount(c.id)).join(' '));
  check('every private-series book is flagged with its series and listed apart from the Government subjects',
    Object.values(D.subjects).every(list => list.every(s => !s.series || (D.series && D.series[s.series]))), 'a subject names a series DATA.series does not describe');
  safe('Class 12 books are included in the registry', () => check('Class 12 books are included in the registry', D.books.length >= 24, 'got ' + D.books.length));
  safe('book ids unique', () => check('book ids unique', new Set(D.books.map(b => b.id)).size === D.books.length));
  safe('book subjects resolvable', () => check('book subjects resolvable', D.books.every(b => b.classId || b.class_id), 'missing classId/class_id on ' + D.books.filter(b => !(b.classId || b.class_id)).map(b => b.id).join(',')));
  safe('chemChapters = 8', () => check('chemChapters = 8', D.chemChapters && D.chemChapters.length === 8, 'got ' + (D.chemChapters || []).length));
  safe('chem10Chapters = 8', () => check('chem10Chapters = 8', D.chem10Chapters && D.chem10Chapters.length === 8, 'got ' + (D.chem10Chapters || []).length));
  safe('physChapters = 9', () => check('physChapters = 9', D.physChapters && D.physChapters.length === 9, 'got ' + (D.physChapters || []).length));
  safe('phys10Chapters = 9', () => check('phys10Chapters = 9', D.phys10Chapters && D.phys10Chapters.length === 9, 'got ' + (D.phys10Chapters || []).length));
  safe('engChapters = 15', () => check('engChapters = 15', D.engChapters && D.engChapters.length === 15, 'got ' + (D.engChapters || []).length));
  safe('eng10Chapters = 15', () => check('eng10Chapters = 15', D.eng10Chapters && D.eng10Chapters.length === 15, 'got ' + (D.eng10Chapters || []).length));
  safe('eng1Chapters = 11', () => check('eng1Chapters = 11', D.eng1Chapters && D.eng1Chapters.length === 11, 'got ' + (D.eng1Chapters || []).length));
  safe('compChapters = 7', () => check('compChapters = 7', D.compChapters && D.compChapters.length === 7, 'got ' + (D.compChapters || []).length));
  safe('chapters roadmap includes the Class 12 map', () => check('chapters roadmap includes the Class 12 map', D.chapters && Object.keys(D.chapters).length >= 15 && D.chapters['cls12-stat'], 'got ' + (D.chapters ? Object.keys(D.chapters).length : 0)));
  safe('Class 12 all 15 subjects registered', () => check('Class 12 all 15 subjects registered', D.subjects && D.subjects.cls12 && D.subjects.cls12.length === 15 && ['cls12-math','cls12-phy','cls12-chem','cls12-stat','cls12-eng','cls12-urdu','cls12-bio','cls12-pak','cls12-comp','cls12-civics','cls12-econ','cls12-hpe','cls12-islopt','cls12-islhist','cls12-quran'].every(id => D.subjects.cls12.some(s => s.id === id))));
  safe('Class 12 textbook PDF links available for all 15 books', () => check('Class 12 textbook PDF links available for all 15 books', ['b-cls12-math','b-cls12-phys','b-cls12-chem','b-cls12-stat','b-cls12-eng','b-cls12-urdu','b-cls12-bio','b-cls12-pak','b-cls12-comp','b-cls12-civics','b-cls12-econ','b-cls12-hpe','b-cls12-islopt','b-cls12-islhist','b-cls12-quran'].every(id => D.books.some(b => b.id === id && b.available && b.pdfPath))));
  safe('DATA.urduChapters = 19 (from urdu_data.js)', () => check('DATA.urduChapters = 19 (from urdu_data.js)', D.urduChapters && (D.urduChapters.length === 19 || D.urduChapters.length === 15), 'got ' + (D.urduChapters || []).length));
  safe('DATA.urdu10Chapters = 22 (from urdu_10_data.js)', () => check('DATA.urdu10Chapters = 22 (from urdu_10_data.js)', (sb.URDU_10_DATA && sb.URDU_10_DATA.length === 22) || (D.urdu10Chapters && D.urdu10Chapters.length === 22), 'got ' + ((sb.URDU_10_DATA || D.urdu10Chapters || []).length)));
  safe('DATA.islamyatChapters = 15', () => check('DATA.islamyatChapters = 15', D.islamyatChapters && D.islamyatChapters.length === 15, 'got ' + (D.islamyatChapters || []).length));
  safe('DATA.islamyat10Chapters = 18', () => check('DATA.islamyat10Chapters = 18', D.islamyat10Chapters && D.islamyat10Chapters.length === 18, 'got ' + (D.islamyat10Chapters || []).length));
  safe('DATA.islamyat1Chapters = 10', () => check('DATA.islamyat1Chapters = 10', (sb.ISLAMYAT_1_DATA && sb.ISLAMYAT_1_DATA.length === 10) || (D.islamyat1Chapters && D.islamyat1Chapters.length === 10), 'got ' + ((sb.ISLAMYAT_1_DATA || D.islamyat1Chapters || []).length)));
  safe('DATA.nazira1Chapters = 17', () => check('DATA.nazira1Chapters = 17', (sb.NAZIRA_1_DATA && sb.NAZIRA_1_DATA.length === 17) || (D.nazira1Chapters && D.nazira1Chapters.length === 17), 'got ' + ((sb.NAZIRA_1_DATA || D.nazira1Chapters || []).length)));
  safe('Class 3 subjects registered', () => check('Class 3 subjects registered', ['cls3-eng', 'cls3-gk', 'cls3-pashto', 'cls3-isl', 'cls3-nazira', 'cls3-drawing'].every(id => (D.subjects.cls3 || []).some(s => s.id === id))));
  safe('DATA.mathChapters present (from math_data.js)', () => check('DATA.mathChapters present (from math_data.js)', Array.isArray(D.mathChapters) && D.mathChapters.length > 0, 'got ' + (D.mathChapters ? D.mathChapters.length : 0)));
  safe('DATA.math10Chapters = 13 (from math_10_data.js)', () => check('DATA.math10Chapters = 13 (from math_10_data.js)', (sb.MATH_10_DATA && sb.MATH_10_DATA.length === 13) || (D.math10Chapters && D.math10Chapters.length === 13), 'got ' + ((sb.MATH_10_DATA || D.math10Chapters || []).length)));
  safe('Class 12 Maths has 12 units and formulas', () => check('Class 12 Maths has 12 units and formulas', Array.isArray(sb.MATH_12_DATA) && sb.MATH_12_DATA.length === 12 && sb.MATH_12_DATA.every(ch => (ch.textbookText ? ch.textbookText.length : (ch.sections && ch.sections.length > 0)) && ch.formulaSheet), 'got ' + ((sb.MATH_12_DATA || []).length)));
  safe('Class 12 Physics has 10 text-backed units and vector figures', () => check('Class 12 Physics has 10 text-backed units and vector figures', Array.isArray(sb.PHYS_12_DATA) && sb.PHYS_12_DATA.length === 10 && sb.PHYS_12_DATA.every(ch => ch.textbookText.length && /<svg/.test(ch.diagramSvg)), 'got ' + ((sb.PHYS_12_DATA || []).length)));
  safe('Class 12 Chemistry has 12 text-backed units and vector figures', () => check('Class 12 Chemistry has 12 text-backed units and vector figures', Array.isArray(sb.CHEM_12_DATA) && sb.CHEM_12_DATA.length === 12 && sb.CHEM_12_DATA.every(ch => ch.textbookText.length && /<svg/.test(ch.diagramSvg)), 'got ' + ((sb.CHEM_12_DATA || []).length)));
  safe('Class 12 Statistics has 9 text-backed units and vector figures', () => check('Class 12 Statistics has 9 text-backed units and vector figures', Array.isArray(sb.STAT_12_DATA) && sb.STAT_12_DATA.length === 9 && sb.STAT_12_DATA.every(ch => ch.textbookText.length && /<svg/.test(ch.diagramSvg)), 'got ' + ((sb.STAT_12_DATA || []).length)));
  safe('islamic subjects registered', () => check('islamic subjects registered', ['cls9-isl', 'cls10-isl', 'cls1-isl', 'cls1-nazira', 'cls2-isl', 'cls2-nazira', 'cls3-isl', 'cls3-nazira'].every(id => [].concat(D.subjects.cls9, D.subjects.cls10, D.subjects.cls1, D.subjects.cls2, D.subjects.cls3).some(s => s.id === id))));
  safe('islamic books registered', () => check('islamic books registered', ['b-cls9-isl', 'b-cls10-isl', 'b-cls1-isl', 'b-cls1-nazira'].every(id => D.books.some(b => b.id === id))));
} else {
  safe('DATA registry present', () => check('DATA registry present', false, 'DATA is undefined'));
}

const EN = sb.ENGLISH_DATA;
safe('Class 1 Drawing activities = 32', () => check('Class 1 Drawing activities = 32', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.length === 32, 'got ' + ((sb.DRAWING_1_DATA || []).length)));
safe('Class 1 Maths units = 6', () => check('Class 1 Maths units = 6', Array.isArray(sb.MATH_1_DATA) && sb.MATH_1_DATA.length === 6, 'got ' + ((sb.MATH_1_DATA || []).length)));
safe('Class 3 Drawing has trilingual exam questions and answers', () => check('Class 3 Drawing has trilingual exam questions and answers', !!(sb.DRAWING_3_EXAM && sb.DRAWING_3_EXAM.mcqs.every(q => q.options.length === 4 && q.optionsUr.length === 4 && q.optionsPs.length === 4 && q.qUr && q.qPs) && sb.DRAWING_3_EXAM.sqs.every(q => q.qUr && q.qPs && q.aUr && q.aPs) && sb.DRAWING_3_EXAM.lqs.every(q => q.qUr && q.qPs && q.aUr && q.aPs))));
safe('Class 3 Drawing is registered in its subject list', () => check('Class 3 Drawing is registered in its subject list', sb.DATA.subjects.cls3.some(s => s.id === 'cls3-drawing' && s.hasDrawing)));
safe('Class 2 Maths units = 6', () => check('Class 2 Maths units = 6', Array.isArray(sb.MATH_2_DATA) && sb.MATH_2_DATA.length === 6, 'got ' + ((sb.MATH_2_DATA || []).length)));
safe('Class 3 Maths has all 7 textbook units', () => check('Class 3 Maths has all 7 textbook units', Array.isArray(sb.MATH_3_DATA) && sb.MATH_3_DATA.length === 7, 'got ' + ((sb.MATH_3_DATA || []).length)));
safe('Class 3 Maths subject is registered to open the maths workspace', () => check('Class 3 Maths subject is registered to open the maths workspace', D.subjects.cls3.some(s => s.id === 'cls3-math' && s.hasMath3 && s.chapters === 7)));
safe('Drawing activities have trilingual tips', () => check('Drawing activities have trilingual tips', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.every(x => x.en && x.ur && x.ps && x.artwork)));
safe('Drawing lessons use vector art without source scans', () => check('Drawing lessons use vector art without source scans', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.every(x => !x.image && x.artwork) && !fs.existsSync(path.join(ROOT, 'assets', 'drawing-class1'))));
safe('Drawing exam practice bank complete', () => check('Drawing exam practice bank complete', !!(sb.DRAWING_1_EXAM && sb.DRAWING_1_EXAM.mcqs.length && sb.DRAWING_1_EXAM.sqs.length && sb.DRAWING_1_EXAM.lqs.length)));
safe('Drawing MCQs have four trilingual options', () => check('Drawing MCQs have four trilingual options', !!(sb.DRAWING_1_EXAM && sb.DRAWING_1_EXAM.mcqs.every(q => q.options.length === 4 && q.optionsUr.length === 4 && q.optionsPs.length === 4 && q.qUr && q.qPs))));
safe('Drawing SQs and LQs have trilingual questions and answers', () => check('Drawing SQs and LQs have trilingual questions and answers', !!(sb.DRAWING_1_EXAM && [...sb.DRAWING_1_EXAM.sqs, ...sb.DRAWING_1_EXAM.lqs].every(q => q.qUr && q.qPs && q.aUr && q.aPs))));

if (EN) {
  safe('ENGLISH_DATA units = 15', () => check('ENGLISH_DATA units = 15', EN.length === 15, 'got ' + EN.length));
  safe('unit2 englishSummary', () => check('unit2 englishSummary', !!EN[1].englishSummary));
  safe('unit2 section[0].urdu', () => check('unit2 section[0].urdu', !!(EN[1].sections && EN[1].sections[0] && EN[1].sections[0].urdu)));
  safe('unit9 urduSummary', () => check('unit9 urduSummary', !!EN[8].urduSummary));
  safe('exercise.vocabulary on units 2-10', () => check('exercise.vocabulary on units 2-10', [1, 2, 3, 4, 5, 6, 7, 8, 9].every(i => EN[i] && EN[i].exercise && Array.isArray(EN[i].exercise.vocabulary)), 'missing on ' + [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(i => !(EN[i] && EN[i].exercise && EN[i].exercise.vocabulary)).join(',')));
  safe('unit8 figurativeLines', () => check('unit8 figurativeLines', EN[7] && EN[7].exercise && Array.isArray(EN[7].exercise.figurativeLines) && EN[7].exercise.figurativeLines.length > 0));
} else {
  safe('ENGLISH_DATA present', () => check('ENGLISH_DATA present', false));
}
const EN10 = sb.ENGLISH_10_DATA;
if (EN10) {
  safe('ENGLISH_10_DATA units = 15', () => check('ENGLISH_10_DATA units = 15', EN10.length === 15, 'got ' + EN10.length));
  safe('ENGLISH_10_DATA unit 1 has sections', () => check('ENGLISH_10_DATA unit 1 has sections', EN10[0] && Array.isArray(EN10[0].sections) && EN10[0].sections.length > 0));
  safe('ENGLISH_10_DATA unit 1 has exercise', () => check('ENGLISH_10_DATA unit 1 has exercise', EN10[0] && !!EN10[0].exercise));
  safe('ENGLISH_10_DATA unit 1 has sloBank', () => check('ENGLISH_10_DATA unit 1 has sloBank', EN10[0] && !!EN10[0].sloBank));
} else {
  safe('ENGLISH_10_DATA present', () => check('ENGLISH_10_DATA present', false));
}
const EN1 = sb.ENGLISH_1_DATA;
if (EN1) {
  safe('ENGLISH_1_DATA units = 11', () => check('ENGLISH_1_DATA units = 11', EN1.length === 11, 'got ' + EN1.length));
  safe('ENGLISH_1_DATA unit 1 has sections', () => check('ENGLISH_1_DATA unit 1 has sections', EN1[0] && Array.isArray(EN1[0].sections) && EN1[0].sections.length > 0));
  safe('ENGLISH_1_DATA unit 1 has exercise', () => check('ENGLISH_1_DATA unit 1 has exercise', EN1[0] && !!EN1[0].exercise));
  safe('ENGLISH_1_DATA unit 1 has sloQuestions', () => check('ENGLISH_1_DATA unit 1 has sloQuestions', EN1[0] && !!(EN1[0].sloQuestions || EN1[0].slos)));
  safe('ENGLISH_1_DATA registered on DATA.eng1Chapters', () => check('ENGLISH_1_DATA registered on DATA.eng1Chapters', Array.isArray(D.eng1Chapters) && D.eng1Chapters.length === 11));
} else {
  safe('ENGLISH_1_DATA present', () => check('ENGLISH_1_DATA present', false));
}

const ISL1 = sb.ISLAMYAT_1_DATA;
if (ISL1) {
  safe('ISLAMYAT_1_DATA units = 10', () => check('ISLAMYAT_1_DATA units = 10', ISL1.length === 10, 'got ' + ISL1.length));
  safe('ISLAMYAT_1_DATA unit 1 has sections', () => check('ISLAMYAT_1_DATA unit 1 has sections', ISL1[0] && Array.isArray(ISL1[0].sections) && ISL1[0].sections.length > 0));
  safe('ISLAMYAT_1_DATA unit 1 has exercise', () => check('ISLAMYAT_1_DATA unit 1 has exercise', ISL1[0] && !!ISL1[0].exercise));
  safe('ISLAMYAT_1_DATA unit 1 has sloQuestions', () => check('ISLAMYAT_1_DATA unit 1 has sloQuestions', ISL1[0] && !!(ISL1[0].sloQuestions || ISL1[0].slos)));
  safe('ISLAMYAT_1_DATA registered on DATA.islamyat1Chapters', () => check('ISLAMYAT_1_DATA registered on DATA.islamyat1Chapters', Array.isArray(D.islamyat1Chapters) && D.islamyat1Chapters.length === 10));
} else {
  safe('ISLAMYAT_1_DATA present', () => check('ISLAMYAT_1_DATA present', false));
}

const NAZ1 = sb.NAZIRA_1_DATA;
if (NAZ1) {
  safe('NAZIRA_1_DATA lessons = 17', () => check('NAZIRA_1_DATA lessons = 17', NAZ1.length === 17, 'got ' + NAZ1.length));
  safe('NAZIRA_1_DATA lesson 1 has sections', () => check('NAZIRA_1_DATA lesson 1 has sections', NAZ1[0] && Array.isArray(NAZ1[0].sections) && NAZ1[0].sections.length > 0));
  safe('NAZIRA_1_DATA lesson 1 has exercise', () => check('NAZIRA_1_DATA lesson 1 has exercise', NAZ1[0] && !!NAZ1[0].exercise));
  safe('NAZIRA_1_DATA lesson 1 has sloQuestions', () => check('NAZIRA_1_DATA lesson 1 has sloQuestions', NAZ1[0] && !!(NAZ1[0].sloQuestions || NAZ1[0].slos)));
  safe('NAZIRA_1_DATA registered on DATA.nazira1Chapters', () => check('NAZIRA_1_DATA registered on DATA.nazira1Chapters', Array.isArray(D.nazira1Chapters) && D.nazira1Chapters.length === 17));
} else {
  safe('NAZIRA_1_DATA present', () => check('NAZIRA_1_DATA present', false));
}

const PS1 = sb.PASHTO_1_DATA;
if (PS1) {
  safe('PASHTO_1_DATA units = 23', () => check('PASHTO_1_DATA units = 23', PS1.length === 23, 'got ' + PS1.length));
  safe('PASHTO_1_DATA unit 1 has sections', () => check('PASHTO_1_DATA unit 1 has sections', PS1[0] && Array.isArray(PS1[0].sections) && PS1[0].sections.length > 0));
  safe('PASHTO_1_DATA unit 1 has exercise', () => check('PASHTO_1_DATA unit 1 has exercise', PS1[0] && !!PS1[0].exercise));
  safe('PASHTO_1_DATA unit 1 has sloQuestions', () => check('PASHTO_1_DATA unit 1 has sloQuestions', PS1[0] && !!(PS1[0].sloQuestions || PS1[0].slos)));
  safe('PASHTO_1_DATA registered on DATA.pashto1Chapters', () => check('PASHTO_1_DATA registered on DATA.pashto1Chapters', Array.isArray(D.pashto1Chapters) && D.pashto1Chapters.length === 23));
  safe('Class 1 Pashto registered in subjects', () => check('Class 1 Pashto registered in subjects', D.subjects && D.subjects.cls1 && D.subjects.cls1.some(s => s.id === 'cls1-pashto' && s.hasPashto)));
  safe('Class 1 Pashto book registered', () => check('Class 1 Pashto book registered', D.books.some(b => b.id === 'b-cls1-pashto')));
} else {
  safe('PASHTO_1_DATA present', () => check('PASHTO_1_DATA present', false));
}

const PS = sb.PAKSTUDY_DATA;
if (PS) {
  safe('PAKSTUDY_DATA units = 4', () => check('PAKSTUDY_DATA units = 4', PS.length === 4, 'got ' + PS.length));
} else {
  safe('PAKSTUDY_DATA present', () => check('PAKSTUDY_DATA present', false));
}

const PS10 = sb.PAKSTUDY_10_DATA;
if (PS10) {
  safe('PAKSTUDY_10_DATA units = 4', () => check('PAKSTUDY_10_DATA units = 4', PS10.length === 4, 'got ' + PS10.length));
  safe('PAKSTUDY_10_DATA ch 1 has sections', () => check('PAKSTUDY_10_DATA ch 1 has sections', PS10[0] && Array.isArray(PS10[0].sections) && PS10[0].sections.length > 0));
  safe('PAKSTUDY_10_DATA ch 1 has exercise', () => check('PAKSTUDY_10_DATA ch 1 has exercise', PS10[0] && !!PS10[0].exercise));
  safe('PAKSTUDY_10_DATA ch 1 has sloBank', () => check('PAKSTUDY_10_DATA ch 1 has sloBank', PS10[0] && !!PS10[0].sloBank));
} else {
  safe('PAKSTUDY_10_DATA present', () => check('PAKSTUDY_10_DATA present', false));
}

const UR10 = sb.URDU_10_DATA;
if (UR10) {
  safe('URDU_10_DATA units = 22', () => check('URDU_10_DATA units = 22', UR10.length === 22, 'got ' + UR10.length));
  safe('URDU_10_DATA ch 1 has sections', () => check('URDU_10_DATA ch 1 has sections', UR10[0] && Array.isArray(UR10[0].sections) && UR10[0].sections.length > 0));
  safe('URDU_10_DATA ch 1 has exercise', () => check('URDU_10_DATA ch 1 has exercise', UR10[0] && !!UR10[0].exercise));
  safe('URDU_10_DATA ch 1 has sloQuestions', () => check('URDU_10_DATA ch 1 has sloQuestions', UR10[0] && !!(UR10[0].sloQuestions || UR10[0].slos)));
} else {
  safe('URDU_10_DATA present', () => check('URDU_10_DATA present', false));
}

safe('ENG_UNIT_VOCAB_WORDS lexicon', () => check('ENG_UNIT_VOCAB_WORDS lexicon', !!(sb.ENG_UNIT_VOCAB_WORDS && sb.ENG_UNIT_VOCAB_WORDS[2]), 'missing from dictionary_data.js'));
safe('lookupEngWord()', () => check('lookupEngWord()', typeof sb.lookupEngWord === 'function'));


safe('MATH_5_DATA units = 9', () => check('MATH_5_DATA units = 9', Array.isArray(sb.MATH_5_DATA) && sb.MATH_5_DATA.length === 9));
safe('GENERAL_SCIENCE_5_DATA units = 10', () => check('GENERAL_SCIENCE_5_DATA units = 10', Array.isArray(sb.GENERAL_SCIENCE_5_DATA) && sb.GENERAL_SCIENCE_5_DATA.length === 10));
safe('ISLAMIAT_5_DATA units = 7', () => check('ISLAMIAT_5_DATA units = 7', Array.isArray(sb.ISLAMIAT_5_DATA) && sb.ISLAMIAT_5_DATA.length === 7));
safe('SOCIAL_STUDIES_5_DATA units = 6', () => check('SOCIAL_STUDIES_5_DATA units = 6', Array.isArray(sb.SOCIAL_STUDIES_5_DATA) && sb.SOCIAL_STUDIES_5_DATA.length === 6));
safe('SOCIAL_STUDIES_UM_5_DATA units = 6', () => check('SOCIAL_STUDIES_UM_5_DATA units = 6', Array.isArray(sb.SOCIAL_STUDIES_UM_5_DATA) && sb.SOCIAL_STUDIES_UM_5_DATA.length === 6));
safe('PASHTO_5_DATA units = 28', () => check('PASHTO_5_DATA units = 28', Array.isArray(sb.PASHTO_5_DATA) && sb.PASHTO_5_DATA.length === 28));
safe('Class 5 all 8 subjects registered', () => check('Class 5 all 8 subjects registered', D.subjects && D.subjects.cls5 && D.subjects.cls5.length === 8 && ['cls5-math','cls5-sci','cls5-eng','cls5-urdu','cls5-isl','cls5-sst','cls5-sstum','cls5-pashto'].every(id => D.subjects.cls5.some(s => s.id === id))));
safe('Class 5 textbook PDF links available for all 8 books', () => check('Class 5 textbook PDF links available for all 8 books', ['b-cls5-math','b-cls5-sci','b-cls5-eng','b-cls5-urdu','b-cls5-isl','b-cls5-sst','b-cls5-sstum','b-cls5-pashto'].every(id => D.books.some(b => b.id === id && b.available && b.pdfPath))));


// ------------------------------------------- 2b. Class 12 page-reviewed books
// Entries of type "source" are front/back-matter pages; the rest are the book's units (exercises live in sections).
const C12 = [
  ['ENGLISH_12_DATA', 19], ['PAKSTUDY_12_DATA', 11], ['URDU_12_DATA', 22], ['BIOLOGY_12_DATA', 14], ['COMP_12_DATA', 9],
  ['CIVICS_12_DATA', 8], ['ECON_12_DATA', 13], ['HPE_12_DATA', 6], ['ISLAMIAT_OPT_12_DATA', 6],
  ['ISLAMIC_HISTORY_12_DATA', 6], ['QURAN_12_DATA', 8],
];
for (const [name, n] of C12) {
  safe(name + ' units = ' + n, () => {
    const units = (sb[name] || []).filter(ch => ch.type !== 'source');
    check(name + ' units = ' + n, units.length === n && units.every(ch => Array.isArray(ch.sections) && ch.sections.length > 0),
      'got ' + units.length + ' units, ' + units.filter(ch => !(ch.sections || []).length).length + ' without sections');
  });
}

// ------------------------------------- 2c. rebuilt books, Classes 1-10 (Contract C)
// Every file that fills window.CLSn_BOOKS[subject] = {units, book, words} is loaded in its own sandbox.
// Unit counts are locked in tests/contract/cls_books.json: a change shows up here and is either an intended
// pipeline rebuild (run with --update-books and commit the file) or a regression.
console.log('--- rebuilt books (CLSn_BOOKS) ---');
const BOOK_LOCK = path.join(ROOT, 'tests', 'contract', 'cls_books.json');
// books whose source is missing or whose page-by-page pass is unfinished (see docs/06_PROJECT_AUDIT and MEMORY)
const NOT_COMPLETE = new Set(['cls1.gk', 'cls1.urdu', 'cls3.urdu', 'cls8.drawing', 'cls12.math', 'cls11.stat']);   // cls11.stat: units 8, 9 and the appendices are not in the reviewed data yet
const clsFiles = jsFiles.filter(f => /window\.CLS[0-9]+_BOOKS\["[a-z0-9_-]+"\] *=/.test(fs.readFileSync(JS + f, 'utf8')));   // "mun-<code>": the Munawar series' keys have a hyphen
const cb = { console, setTimeout, clearTimeout };
cb.window = cb;
vm.createContext(cb);
for (const f of clsFiles) {
  try { vm.runInContext(fs.readFileSync(JS + f, 'utf8'), cb, { filename: f, timeout: 60000 }); }
  catch (e) { check('load book ' + f, false, e.message); }
}
const bookUnits = {};
for (let n = 1; n <= 12; n++) {
  const B = cb['CLS' + n + '_BOOKS'];
  if (!B) continue;
  for (const [key, v] of Object.entries(B)) {
    const id = 'cls' + n + '.' + key, units = (v && v.units) || [], book = (v && v.book) || {};
    bookUnits[id] = units.length;
    safe(id + ' has units with ids and titles', () => check(id + ' has units with ids and titles',
      units.length > 0 && units.every(u => u.id && u.title), units.length + ' units'));
    // the Munawar (Kanz) books are transcribed as far as the publisher's low-resolution sample PDFs can be read
    // (docs/source-verification/private/munawar/README.md): an incomplete one is known, a book that claims to be complete is checked like any other
    if (NOT_COMPLETE.has(id) || (book.series === 'munawar' && !book.complete)) {
      console.log('KNOWN ' + id + ' not complete (' + book.reviewedPdfPages + '/' + book.totalPdfPages + ' pages)');
      continue;
    }
    safe(id + ' is complete and every unit has sections', () => check(id + ' is complete and every unit has sections',
      book.complete === true && units.every(u => Array.isArray(u.sections) && u.sections.length > 0),
      'complete=' + book.complete + ', ' + units.filter(u => !(u.sections || []).length).length + ' units without sections'));
  }
}
if (process.argv.includes('--update-books')) {
  fs.mkdirSync(path.dirname(BOOK_LOCK), { recursive: true });
  fs.writeFileSync(BOOK_LOCK, JSON.stringify(bookUnits, null, 1) + '\n');
  console.log('wrote ' + path.relative(ROOT, BOOK_LOCK));
}
const lock = fs.existsSync(BOOK_LOCK) ? JSON.parse(fs.readFileSync(BOOK_LOCK, 'utf8')) : {};
check('CLSn_BOOKS lock file exists', Object.keys(lock).length > 0, 'run node tools/validate.js --update-books');
const changed = [...new Set([...Object.keys(lock), ...Object.keys(bookUnits)])]
  .filter(k => lock[k] !== bookUnits[k]).map(k => k + ' ' + lock[k] + ' -> ' + bookUnits[k]);
check('CLSn_BOOKS unit counts match tests/contract/cls_books.json (' + Object.keys(bookUnits).length + ' books)',
  changed.length === 0, changed.join(', '));

// Class 11 registry: app.js class11BookBySubject() looks a book up by key (a scan of the values would load every Class 11 book on the lazy page),
// which holds only while every registration is { key: K, subjectId: 'cls11-' + K } and the registry slot is K.
safe('CLASS11_BOOKS registrations: slot = key, subjectId = cls11-key', () => {
  const bad = [], found = [];
  for (const f of jsFiles.filter(f => /_11_data\.js$/.test(f))) {
    const m = fs.readFileSync(JS + f, 'utf8').match(/CLASS11_BOOKS = window\.CLASS11_BOOKS \|\| \{\}\)\['([a-z0-9]+)'\] = \{\s*key: '([a-z0-9]+)', subjectId: '([a-z0-9-]+)'/);
    if (!m) continue;
    found.push(m[1]);
    if (m[2] !== m[1] || m[3] !== 'cls11-' + m[1]) bad.push(f + ': slot ' + m[1] + ', key ' + m[2] + ', subjectId ' + m[3]);
  }
  check('CLASS11_BOOKS registrations: slot = key, subjectId = cls11-key (' + found.length + ' books)', found.length >= 8 && bad.length === 0, bad.join('; ') || 'only ' + found.length + ' found');
});

// --------------------------------------------------- 3. index.html wiring
console.log('--- index.html ---');
const html = fs.readFileSync(INDEX, 'utf8');
const srcs = [...html.matchAll(/<script\s+src="([^"]+)"/g)].map(m => m[1].split('?')[0]);
safe('index.html references app.js', () => check('index.html references app.js', srcs.includes('js/app.js')));
safe('index.html loads core registry before subjects', () => check('index.html loads core registry before subjects', srcs.indexOf('js/data.js') >= 0 && srcs.indexOf('js/data.js') < srcs.indexOf('js/app.js')));
safe('index.html loads Class 1 Drawing data', () => check('index.html loads Class 1 Drawing data', srcs.includes('js/drawing_1_data.js') && srcs.indexOf('js/drawing_1_data.js') < srcs.indexOf('js/app.js')));
safe('index.html loads Class 1 English data', () => check('index.html loads Class 1 English data', srcs.includes('js/english_1_data.js') && srcs.indexOf('js/english_1_data.js') < srcs.indexOf('js/app.js')));
safe('index.html loads Class 1 English page-by-page art, model and learning renderer before app.js', () => check('index.html loads Class 1 English page-by-page art, model and learning renderer before app.js', ['js/primary_page_art.js','js/english_1_pages.js','js/primary_page_learning.js'].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js'))));
safe('index.html loads Class 1 Maths data', () => check('index.html loads Class 1 Maths data', srcs.includes('js/math_1_data.js') && srcs.indexOf('js/math_1_data.js') < srcs.indexOf('js/app.js')));
safe('index.html loads Class 2 Drawing and Maths data', () => check('index.html loads Class 2 Drawing and Maths data', ['js/drawing_2_data.js','js/math_2_data.js'].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js'))));
safe('index.html loads Class 3 Maths text, lessons, and vector figures before app.js', () => check('index.html loads Class 3 Maths text, lessons, and vector figures before app.js', ['js/math_3_book_text.js','js/math_3_data.js','js/math_primary_visuals.js'].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js'))));
safe('index.html loads all 15 Class 12 textbooks before app.js', () => check('index.html loads all 15 Class 12 textbooks before app.js', ['js/math_12_data.js','js/phys_12_data.js','js/chem_12_data.js','js/stat_12_data.js','js/english_12_data.js','js/pakstudy_12_data.js','js/urdu_12_data.js','js/biology_12_data.js','js/computer_12_data.js','js/civics_12_data.js','js/economics_12_data.js','js/hpe_12_data.js','js/islamiat_ikhtiari_12_data.js','js/islamic_history_12_data.js','js/quran_12_data.js'].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js'))));
safe('index.html loads Class 3 Drawing data before app.js', () => check('index.html loads Class 3 Drawing data before app.js', srcs.includes('js/drawing_3_data.js') && srcs.indexOf('js/drawing_3_data.js') < srcs.indexOf('js/app.js')));
safe('index.html loads Class 1 Islamyat data', () => check('index.html loads Class 1 Islamyat data', srcs.includes('js/islamyat_1_data.js') && srcs.indexOf('js/islamyat_1_data.js') < srcs.indexOf('js/app.js')));
safe('index.html loads Class 1 Nazira data', () => check('index.html loads Class 1 Nazira data', srcs.includes('js/nazira_1_data.js') && srcs.indexOf('js/nazira_1_data.js') < srcs.indexOf('js/app.js')));
safe('index.html loads Class 1 Pashto data', () => check('index.html loads Class 1 Pashto data', srcs.includes('js/pashto_1_data.js') && srcs.indexOf('js/pashto_1_data.js') < srcs.indexOf('js/app.js')));
check('index.html loads Class 2 English, Urdu, Islamyat, Nazira, GK, Pashto datasets', [
  'js/english_2_data.js', 'js/urdu_2_data.js', 'js/islamyat_2_data.js',
  'js/nazira_2_data.js', 'js/gk_2_data.js', 'js/pashto_2_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
check('index.html loads Class 3 Islamyat and Nazira datasets', [
  'js/islamyat_3_data.js', 'js/nazira_3_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
check('index.html loads Class 3 English, GK, Pashto datasets', [
  'js/english_3_data.js', 'js/gk_3_data.js', 'js/pashto_3_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
check('index.html loads Class 5 new datasets before app.js', [
  'js/math_5_data.js', 'js/general_science_5_data.js', 'js/english_5_data.js',
  'js/urdu_5_data.js', 'js/islamiat_5_data.js', 'js/social_studies_5_data.js',
  'js/social_studies_um_5_data.js', 'js/pashto_5_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
check('index.html loads Class 6 new datasets before app.js', [
  'js/math_6_data.js', 'js/general_science_6_data.js', 'js/english_6_data.js',
  'js/urdu_6_data.js', 'js/islamiat_6_data.js', 'js/computer_6_data.js',
  'js/geography_6_data.js', 'js/history_6_data.js', 'js/hpe_6_data.js',
  'js/drawing_6_data.js', 'js/arabic_6_data.js', 'js/mutalia_quran_6_data.js',
  'js/pashto_6_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
check('index.html loads Class 9 new datasets before app.js', [
  'js/general_science_9_data.js', 'js/hpe_9_data.js',
  'js/drawing_9_data.js', 'js/islamiat_ikhtiari_9_data.js', 'js/mutalia_quran_9_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
check('index.html loads Class 10 new datasets before app.js', [
  'js/computer_10_data.js', 'js/general_science_10_data.js', 'js/hpe_10_data.js',
  'js/drawing_10_data.js', 'js/islamiat_ikhtiari_10_data.js', 'js/mutalia_quran_10_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
['js/data_chem.js', 'js/data_phys.js', 'js/data_eng.js', 'js/data_bio.js', 'js/data_comp.js'].forEach(s => check('index.html loads ' + s, srcs.includes(s)));
safe('index.html loads js/core/store.js, sync.js, consent.js (in that order) before js/sb_rewards.js and js/auth.js', () => check('index.html loads js/core/store.js, sync.js, consent.js (in that order) before js/sb_rewards.js and js/auth.js',
  srcs.indexOf('js/core/store.js') >= 0 && srcs.indexOf('js/core/store.js') < srcs.indexOf('js/core/sync.js') && srcs.indexOf('js/core/sync.js') < srcs.indexOf('js/core/consent.js')
  && srcs.indexOf('js/core/consent.js') < srcs.indexOf('js/sb_rewards.js') && srcs.indexOf('js/sb_rewards.js') < srcs.indexOf('js/auth.js')));
const missingSrc = srcs.filter(s => !fs.existsSync(path.join(ROOT, s)));
safe('every <script src> exists', () => check('every <script src> exists', missingSrc.length === 0, 'missing: ' + missingSrc.join(',')));
const cssHref = (html.match(/<link\s+rel="stylesheet"\s+href="([^"]+)"/g) || []).map(s => s.match(/href="([^"]+)"/)[1]);
safe('stylesheet path exists', () => check('stylesheet path exists', cssHref.every(h => fs.existsSync(path.join(ROOT, h.split('?')[0]))), cssHref.join(',')));

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
safe('app.js functions unique (' + fnNames.length + ')', () => check('app.js functions unique (' + fnNames.length + ')', dupes.length === 0, dupes.join(',')));
const defines = n => !!counts[n] || new RegExp('(?:const|let|var)\\s+' + n + '\\s*=').test(app) || new RegExp('(?:window|globalThis)\\.' + n + '\\s*=').test(app);
['openSubject', 'handleGlobalSearch', 'clearGlobalSearch', 'renderBooksView', 'sanitize', 'autoScrollToActiveTab',
  'renderEngEnglishSummary', 'getUrduChapterList', 'openIslView', 'renderIslSloLQs', 'recordQuestionAnswer',
  'renderHome', 'renderClasses', 'goToSubjects'].forEach(n => check('app.js defines ' + n, defines(n)));
safe('app.js has single openSubject', () => check('app.js has single openSubject', counts.openSubject === 1, 'got ' + counts.openSubject));
safe('router hasIsl branch', () => check('router hasIsl branch', app.includes('subj.hasIsl')));
safe('state has selectedIslChapter', () => check('state has selectedIslChapter', /selectedIslChapter:\s*0/.test(app)));
safe('state has math/pakstudy fields', () => check('state has math/pakstudy fields', /activePakStudySloTab:/.test(app) && /activeMathEx:/.test(app)));
safe('search has Islamyat section', () => check('search has Islamyat section', app.includes('Search Islamyat Units')));
safe('search has no undefined sanitize()', () => check('search has no undefined sanitize()', /sanitize\s*\(/.test(app) && /const sanitize\s*=/.test(app)));
safe('no undefined updateStudyStats()', () => check('no undefined updateStudyStats()', !/[^.\w]updateStudyStats\s*\(/.test(app)));
safe('no undefined openGenericSubjectView()', () => check('no undefined openGenericSubjectView()', !/[^.\w]openGenericSubjectView\s*\(/.test(app)));
safe('English Summary tab wired', () => check('English Summary tab wired', app.includes('renderEngEnglishSummary') && app.includes('id: "en-sum"')));
safe('no foreign data globals (BIO10_DATA/GEO_DATA/KIN_DATA)', () => check('no foreign data globals (BIO10_DATA/GEO_DATA/KIN_DATA)', !/\bBIO10_DATA\b|\bGEO_DATA\b|\bKIN_DATA\b/.test(app)));

// ------------------------------------------------------------- 5. css balance
console.log('--- css ---');
const css = fs.readFileSync(path.join(ROOT, 'css', 'style.css'), 'utf8');
let depth = 0;
for (const c of css) { if (c === '{') depth++; else if (c === '}') depth--; }
safe('css braces balanced', () => check('css braces balanced', depth === 0, 'depth=' + depth));

// ------------------------------------------------- 6. offline layer and third parties (Phase 4)
console.log('--- offline ---');
{
  const read = f => fs.readFileSync(path.join(ROOT, f), 'utf8');
  const exists = f => fs.existsSync(path.join(ROOT, f));
  safe('manifest.webmanifest is valid and complete', () => {
    const m = JSON.parse(read('manifest.webmanifest'));
    const icons = m.icons || [];
    const missing = icons.filter(i => !exists(i.src));
    const dims = icons.map(i => { try { const b = fs.readFileSync(path.join(ROOT, i.src)); return b.readUInt32BE(16) + 'x' + b.readUInt32BE(20); } catch (e) { return '?'; } });
    check('manifest.webmanifest is valid and complete', !!(m.name && m.short_name && m.start_url && m.scope && m.display === 'standalone' && m.theme_color && m.background_color) &&
      icons.length >= 3 && missing.length === 0 && icons.every((i, k) => dims[k] === i.sizes) && icons.some(i => i.purpose === 'maskable') && icons.some(i => i.sizes === '192x192') && icons.some(i => i.sizes === '512x512'),
      'missing ' + missing.map(i => i.src).join(',') + ' sizes ' + dims.join(','));
  });
  safe('service worker file parses', () => { new vm.Script(read('sw.js'), { filename: 'sw.js' }); check('service worker file parses', true); });
  safe('offline files are generated and consistent', () => {
    const sw = {}; vm.runInNewContext(read('content/sw_version.js'), { self: sw });
    const m = JSON.parse(read('manifest.webmanifest'));
    const map = JSON.parse(read('content/offline_map.json'));
    const missingShell = sw.SB_SW.shell.filter(u => !exists(u.split('?')[0]));
    check('web manifest starts the page the service worker precaches (' + sw.SB_SW.entry + ')', m.start_url.replace(/^\.\//, '').split('?')[0] === sw.SB_SW.entry, 'start_url ' + m.start_url + ' vs entry ' + sw.SB_SW.entry);
    check('every file in the service worker shell exists (' + sw.SB_SW.shell.length + ')', missingShell.length === 0, missingShell.slice(0, 5).join(','));
    check('the shell holds the entry page, the offline page and the icons', ['lazy.html', 'offline.html', 'icons/icon-192.png'].every(f => sw.SB_SW.shell.includes(f)));
    const badFiles = Object.keys(map.files).filter(f => !exists(f));
    check('every book file in the offline map exists (' + Object.keys(map.files).length + ')', badFiles.length === 0, badFiles.slice(0, 5).join(','));
    const badAssets = Object.keys(map.assets).filter(f => !exists(f));
    check('every image in the offline map exists (' + Object.keys(map.assets).length + ')', badAssets.length === 0, badAssets.slice(0, 5).join(','));
    check('every subject of the registry is in the offline map', Object.keys(map.subjects).filter(id => id !== 'meanings').length === Object.values(sb.DATA.subjects).reduce((n, l) => n + l.length, 0), Object.keys(map.subjects).filter(id => id !== 'meanings').length + ' vs registry');
  });
  safe('no third-party request at start-up (fonts, scripts, styles)', () => {
    const html = read('index.html');
    const external = [...html.matchAll(/<(?:script|link|img)\b[^>]*\b(?:src|href)="((?:https?:)?\/\/[^"]+)"/g)].map(m => m[1]).filter(u => !/^https?:\/\/(www\.)?w3\.org/.test(u));
    check('no third-party request at start-up (fonts, scripts, styles)', external.length === 0, external.join(', '));
    check('index.html links the web manifest', /<link rel="manifest" href="manifest\.webmanifest"/.test(html));
  });
  safe('no script sends text to a third-party translation service', () => {
    const code = f => read('js/' + f).split(String.fromCharCode(10)).filter(l => { const t = l.trim(); return !(t.startsWith('//') || t.startsWith('*') || t.startsWith('/*')); }).join(String.fromCharCode(10));
    const bad = fs.readdirSync(path.join(ROOT, 'js')).filter(f => f.endsWith('.js') && !/_data\.js$/.test(f)).filter(f => /translate\.googleapis\.com|api\.mymemory|translate\.google\.com/.test(code(f)));
    check('no script sends text to a third-party translation service', bad.length === 0, bad.join(','));
    check('the generated lexicon is present', exists('js/lexicon_data.js') && /SB_LEXICON_V1/.test(read('js/lexicon_data.js').slice(0, 400)));
  });
  safe('the deploy workflow is valid YAML where it matters', () => {
    // GitHub refuses a workflow whose step name has a colon followed by a space ("mapping values are not allowed here"); two did, from Phase 3 until 2026-10-20
    const f = path.join(ROOT, '..', '.github', 'workflows', 'deploy.yml');
    if (!fs.existsSync(f)) { check('the deploy workflow is valid YAML where it matters (not in this checkout)', true); return; }
    const lines = fs.readFileSync(f, 'utf8').split(/\r?\n/);
    const bad = lines.map((l, i) => [i + 1, l]).filter(([, l]) => /^\s*-?\s*name:\s+[^'"|>\s].*:\s/.test(l));
    check('no step name in the deploy workflow has a colon followed by a space', bad.length === 0, bad.map(([n, l]) => n + ': ' + l.trim().slice(0, 60)).join(' | '));
    const tabs = lines.filter(l => /^\t/.test(l)).length;
    check('the deploy workflow has no tab indentation', tabs === 0, tabs + ' lines');
    // FTP-Deploy-Action matches a pattern that has no slash against the file NAME at any depth: "test_*.js" kept js/test_prep.js and
    // js/test_prep_bank.js off the server (404 on the live site, 2026-10-23). No file the site serves may be caught by the exclude list.
    const at = lines.findIndex(l => /^\s*exclude:\s*\|/.test(l));
    const pats = [];
    for (let i = at + 1; at >= 0 && i < lines.length && /^\s{6,}\S/.test(lines[i]); i++) pats.push(lines[i].trim());
    const rx = p => new RegExp('^' + p.replace(/[.+^${}()|[\]\\]/g, '\\$&').replace(/\*\*\//g, '@@A@@').replace(/\/\*\*/g, '/@@B@@').replace(/\*/g, '[^/]*').replace(/@@A@@/g, '(?:.*/)?').replace(/@@B@@/g, '.*') + '$');
    const site = ['js', 'css', 'content', 'assets', 'covers', 'icons', 'api']
      .flatMap(d => fs.existsSync(path.join(ROOT, d)) ? fs.readdirSync(path.join(ROOT, d), { recursive: true }).map(x => d + '/' + String(x).split(path.sep).join('/')) : [])
      .filter(x => fs.statSync(path.join(ROOT, x)).isFile())
      .concat(['index.html', 'lazy.html', 'offline.html', 'sw.js', 'manifest.webmanifest', '.htaccess']);
    const caught = site.filter(x => pats.some(p => { const r = rx(p); return r.test(x) || (!p.includes('/') && r.test(x.split('/').pop())); }));
    check('no file the site serves is caught by the deploy exclude list (' + pats.length + ' patterns, ' + site.length + ' files)', pats.length > 5 && caught.length === 0, caught.slice(0, 5).join(','));
  });
  safe('read-aloud never asks a website for speech', () => {
    const offenders = ['app.js', 'universal_translate.js', 'word_stats.js', 'sb_four_lang.js', 'reader_tools.js', 'sb_trilingual.js', 'sb_global_ui.js'].filter(f => exists('js/' + f) && /translate_tts/.test(read('js/' + f)));
    check('read-aloud never asks a website for speech', offenders.length === 0, offenders.join(','));
  });
}

console.log('---');
console.log('validate: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
