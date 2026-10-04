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
  'pakstudy_data.js', 'pakstudy_10_data.js', 'bio_data.js', 'islamyat_data.js', 'islamyat_10_data.js', 'islamyat_1_data.js',
  'nazira_1_data.js', 'pashto_1_data.js', 'math_10_data.js', 'math_1_data.js', 'drawing_2_data.js', 'drawing_3_data.js', 'math_2_data.js',
  'english_2_data.js', 'urdu_2_data.js', 'islamyat_2_data.js', 'nazira_2_data.js', 'gk_2_data.js', 'pashto_2_data.js',
  'islamyat_3_data.js', 'nazira_3_data.js'
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
  check('books = ' + D.books.length, D.books.length === 22, 'got ' + D.books.length);
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
  check('DATA.islamyat1Chapters = 10', (sb.ISLAMYAT_1_DATA && sb.ISLAMYAT_1_DATA.length === 10) || (D.islamyat1Chapters && D.islamyat1Chapters.length === 10), 'got ' + ((sb.ISLAMYAT_1_DATA || D.islamyat1Chapters || []).length));
  check('DATA.nazira1Chapters = 17', (sb.NAZIRA_1_DATA && sb.NAZIRA_1_DATA.length === 17) || (D.nazira1Chapters && D.nazira1Chapters.length === 17), 'got ' + ((sb.NAZIRA_1_DATA || D.nazira1Chapters || []).length));
  check('DATA.eng2Chapters = 12', (sb.ENGLISH_2_DATA && sb.ENGLISH_2_DATA.length === 12) || (D.eng2Chapters && D.eng2Chapters.length === 12), 'got ' + ((sb.ENGLISH_2_DATA || D.eng2Chapters || []).length));
  check('DATA.urdu2Chapters = 22', (sb.URDU_2_DATA && sb.URDU_2_DATA.length === 22) || (D.urdu2Chapters && D.urdu2Chapters.length === 22), 'got ' + ((sb.URDU_2_DATA || D.urdu2Chapters || []).length));
  check('DATA.islamyat2Chapters = 11', (sb.ISLAMYAT_2_DATA && sb.ISLAMYAT_2_DATA.length === 11) || (D.islamyat2Chapters && D.islamyat2Chapters.length === 11), 'got ' + ((sb.ISLAMYAT_2_DATA || D.islamyat2Chapters || []).length));
  check('DATA.nazira2Chapters = 15', (sb.NAZIRA_2_DATA && sb.NAZIRA_2_DATA.length === 15) || (D.nazira2Chapters && D.nazira2Chapters.length === 15), 'got ' + ((sb.NAZIRA_2_DATA || D.nazira2Chapters || []).length));
  check('DATA.gk2Chapters = 16', (sb.GK_2_DATA && sb.GK_2_DATA.length === 16) || (D.gk2Chapters && D.gk2Chapters.length === 16), 'got ' + ((sb.GK_2_DATA || D.gk2Chapters || []).length));
  check('DATA.pashto2Chapters = 28', (sb.PASHTO_2_DATA && sb.PASHTO_2_DATA.length === 28) || (D.pashto2Chapters && D.pashto2Chapters.length === 28), 'got ' + ((sb.PASHTO_2_DATA || D.pashto2Chapters || []).length));
  check('DATA.islamyat3Chapters = 18', (sb.ISLAMYAT_3_DATA && sb.ISLAMYAT_3_DATA.length === 18) || (D.islamyat3Chapters && D.islamyat3Chapters.length === 18), 'got ' + ((sb.ISLAMYAT_3_DATA || D.islamyat3Chapters || []).length));
  check('DATA.nazira3Chapters = 16', (sb.NAZIRA_3_DATA && sb.NAZIRA_3_DATA.length === 16) || (D.nazira3Chapters && D.nazira3Chapters.length === 16), 'got ' + ((sb.NAZIRA_3_DATA || D.nazira3Chapters || []).length));
  check('DATA.mathChapters present (from math_data.js)', Array.isArray(D.mathChapters) && D.mathChapters.length > 0, 'got ' + (D.mathChapters ? D.mathChapters.length : 0));
  check('DATA.math10Chapters = 13 (from math_10_data.js)', (sb.MATH_10_DATA && sb.MATH_10_DATA.length === 13) || (D.math10Chapters && D.math10Chapters.length === 13), 'got ' + ((sb.MATH_10_DATA || D.math10Chapters || []).length));
  check('islamic subjects registered', ['cls9-isl', 'cls10-isl', 'cls1-isl', 'cls1-nazira', 'cls2-isl', 'cls2-nazira', 'cls3-isl', 'cls3-nazira'].every(id => [].concat(D.subjects.cls9, D.subjects.cls10, D.subjects.cls1, D.subjects.cls2, D.subjects.cls3).some(s => s.id === id)));
  check('islamic books registered', ['b-cls9-isl', 'b-cls10-isl', 'b-cls1-isl', 'b-cls1-nazira'].every(id => D.books.some(b => b.id === id)));
} else {
  check('DATA registry present', false, 'DATA is undefined');
}

const EN = sb.ENGLISH_DATA;
check('Class 1 Drawing activities = 32', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.length === 32, 'got ' + ((sb.DRAWING_1_DATA || []).length));
check('Class 1 Maths units = 6', Array.isArray(sb.MATH_1_DATA) && sb.MATH_1_DATA.length === 6, 'got ' + ((sb.MATH_1_DATA || []).length));
check('Class 2 Drawing has 32 vector activities and trilingual tips', Array.isArray(sb.DRAWING_2_DATA) && sb.DRAWING_2_DATA.length === 32 && sb.DRAWING_2_DATA.every((x,i) => x.number === i + 1 && x.en && x.ur && x.ps && sb.DRAWING_2_ART[x.artwork]));
check('Class 3 Drawing has 32 vector activities and trilingual tips', Array.isArray(sb.DRAWING_3_DATA) && sb.DRAWING_3_DATA.length === 32 && sb.DRAWING_3_DATA.every((x,i) => x.number === i + 1 && x.en && x.ur && x.ps && sb.DRAWING_3_ART[x.artwork]));
check('Class 3 Drawing has trilingual exam questions and answers', !!(sb.DRAWING_3_EXAM && sb.DRAWING_3_EXAM.mcqs.every(q => q.options.length === 4 && q.optionsUr.length === 4 && q.optionsPs.length === 4 && q.qUr && q.qPs) && sb.DRAWING_3_EXAM.sqs.every(q => q.qUr && q.qPs && q.aUr && q.aPs) && sb.DRAWING_3_EXAM.lqs.every(q => q.qUr && q.qPs && q.aUr && q.aPs)));
check('Class 3 Drawing is registered in its subject list', sb.DATA.subjects.cls3.some(s => s.id === 'cls3-drawing' && s.hasDrawing));
check('Class 2 Drawing has trilingual exam practice', !!(sb.DRAWING_2_EXAM && sb.DRAWING_2_EXAM.mcqs.every(q => q.options.length === 4 && q.optionsUr.length === 4 && q.optionsPs.length === 4 && q.qUr && q.qPs) && sb.DRAWING_2_EXAM.sqs.every(q => q.qUr && q.qPs && q.aUr && q.aPs) && sb.DRAWING_2_EXAM.lqs.every(q => q.qUr && q.qPs && q.aUr && q.aPs)));
check('Class 2 Maths units = 6', Array.isArray(sb.MATH_2_DATA) && sb.MATH_2_DATA.length === 6, 'got ' + ((sb.MATH_2_DATA || []).length));
check('Class 2 Maths units have lessons, worked examples, solved exercises and three question banks', Array.isArray(sb.MATH_2_DATA) && sb.MATH_2_DATA.every(ch => ch.sections.length && ch.workedExamples.length && ch.exercises.length && ch.slos.mcqs.length && ch.slos.shortQuestions.length && ch.slos.longQuestions.length));
check('Class 2 Drawing vectors and questions remain a lightweight content dataset', !!(sb.DRAWING_2_DATA && JSON.stringify(sb.DRAWING_2_DATA).length < 40000 && JSON.stringify(sb.DRAWING_2_ART).length < 18000));
check('Class 3 Drawing vectors and questions remain lightweight', !!(sb.DRAWING_3_DATA && JSON.stringify(sb.DRAWING_3_DATA).length < 30000 && JSON.stringify(sb.DRAWING_3_ART).length < 30000));
check('Class 1 Maths units have lessons, examples, solved exercises and exam questions', Array.isArray(sb.MATH_1_DATA) && sb.MATH_1_DATA.every(ch => ch.sections.length && ch.workedExamples.length && ch.exercises.length && ch.slos.mcqs.length && ch.slos.shortQuestions.length && ch.slos.longQuestions.length));
check('Class 1 Maths lessons have topic-matched Urdu text and rules', Array.isArray(sb.MATH_1_DATA) && sb.MATH_1_DATA.every(ch => ch.sections.every(sec => sec.theoryUrdu && sec.rulesUrdu && sec.rulesUrdu.length === sec.rules.length)));
check('Drawing activities have trilingual tips', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.every(x => x.en && x.ur && x.ps && x.artwork));
check('Drawing lessons use vector art without source scans', Array.isArray(sb.DRAWING_1_DATA) && sb.DRAWING_1_DATA.every(x => !x.image && x.artwork) && !fs.existsSync(path.join(ROOT, 'assets', 'drawing-class1')));
check('Drawing exam practice bank complete', !!(sb.DRAWING_1_EXAM && sb.DRAWING_1_EXAM.mcqs.length && sb.DRAWING_1_EXAM.sqs.length && sb.DRAWING_1_EXAM.lqs.length));
check('Drawing MCQs have four trilingual options', !!(sb.DRAWING_1_EXAM && sb.DRAWING_1_EXAM.mcqs.every(q => q.options.length === 4 && q.optionsUr.length === 4 && q.optionsPs.length === 4 && q.qUr && q.qPs)));
check('Drawing SQs and LQs have trilingual questions and answers', !!(sb.DRAWING_1_EXAM && [...sb.DRAWING_1_EXAM.sqs, ...sb.DRAWING_1_EXAM.lqs].every(q => q.qUr && q.qPs && q.aUr && q.aPs)));

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

const ISL1 = sb.ISLAMYAT_1_DATA;
if (ISL1) {
  check('ISLAMYAT_1_DATA units = 10', ISL1.length === 10, 'got ' + ISL1.length);
  check('ISLAMYAT_1_DATA unit 1 has sections', ISL1[0] && Array.isArray(ISL1[0].sections) && ISL1[0].sections.length > 0);
  check('ISLAMYAT_1_DATA unit 1 has exercise', ISL1[0] && !!ISL1[0].exercise);
  check('ISLAMYAT_1_DATA unit 1 has sloQuestions', ISL1[0] && !!(ISL1[0].sloQuestions || ISL1[0].slos));
  check('ISLAMYAT_1_DATA registered on DATA.islamyat1Chapters', Array.isArray(D.islamyat1Chapters) && D.islamyat1Chapters.length === 10);
} else {
  check('ISLAMYAT_1_DATA present', false);
}

const NAZ1 = sb.NAZIRA_1_DATA;
if (NAZ1) {
  check('NAZIRA_1_DATA lessons = 17', NAZ1.length === 17, 'got ' + NAZ1.length);
  check('NAZIRA_1_DATA lesson 1 has sections', NAZ1[0] && Array.isArray(NAZ1[0].sections) && NAZ1[0].sections.length > 0);
  check('NAZIRA_1_DATA lesson 1 has exercise', NAZ1[0] && !!NAZ1[0].exercise);
  check('NAZIRA_1_DATA lesson 1 has sloQuestions', NAZ1[0] && !!(NAZ1[0].sloQuestions || NAZ1[0].slos));
  check('NAZIRA_1_DATA registered on DATA.nazira1Chapters', Array.isArray(D.nazira1Chapters) && D.nazira1Chapters.length === 17);
} else {
  check('NAZIRA_1_DATA present', false);
}

const PS1 = sb.PASHTO_1_DATA;
if (PS1) {
  check('PASHTO_1_DATA units = 23', PS1.length === 23, 'got ' + PS1.length);
  check('PASHTO_1_DATA unit 1 has sections', PS1[0] && Array.isArray(PS1[0].sections) && PS1[0].sections.length > 0);
  check('PASHTO_1_DATA unit 1 has exercise', PS1[0] && !!PS1[0].exercise);
  check('PASHTO_1_DATA unit 1 has sloQuestions', PS1[0] && !!(PS1[0].sloQuestions || PS1[0].slos));
  check('PASHTO_1_DATA registered on DATA.pashto1Chapters', Array.isArray(D.pashto1Chapters) && D.pashto1Chapters.length === 23);
  check('Class 1 Pashto registered in subjects', D.subjects && D.subjects.cls1 && D.subjects.cls1.some(s => s.id === 'cls1-pashto' && s.hasPashto));
  check('Class 1 Pashto book registered', D.books.some(b => b.id === 'b-cls1-pashto'));
} else {
  check('PASHTO_1_DATA present', false);
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

const EN2 = sb.ENGLISH_2_DATA;
if (EN2) {
  check('ENGLISH_2_DATA units = 12', EN2.length === 12, 'got ' + EN2.length);
  check('ENGLISH_2_DATA unit 1 has sections', EN2[0] && Array.isArray(EN2[0].sections) && EN2[0].sections.length > 0);
  check('ENGLISH_2_DATA unit 1 has exercise', EN2[0] && !!EN2[0].exercise);
  check('ENGLISH_2_DATA registered on DATA.eng2Chapters', Array.isArray(D.eng2Chapters) && D.eng2Chapters.length === 12);
} else {
  check('ENGLISH_2_DATA present', false);
}

const UR2 = sb.URDU_2_DATA;
if (UR2) {
  check('URDU_2_DATA units = 22', UR2.length === 22, 'got ' + UR2.length);
  check('URDU_2_DATA ch 1 has sections', UR2[0] && Array.isArray(UR2[0].sections) && UR2[0].sections.length > 0);
  check('URDU_2_DATA ch 1 has exercise', UR2[0] && !!UR2[0].exercise);
  check('URDU_2_DATA registered on DATA.urdu2Chapters', Array.isArray(D.urdu2Chapters) && D.urdu2Chapters.length === 22);
} else {
  check('URDU_2_DATA present', false);
}

const ISL2 = sb.ISLAMYAT_2_DATA;
if (ISL2) {
  check('ISLAMYAT_2_DATA units = 11', ISL2.length === 11, 'got ' + ISL2.length);
  check('ISLAMYAT_2_DATA unit 1 has sections', ISL2[0] && Array.isArray(ISL2[0].sections) && ISL2[0].sections.length > 0);
  check('ISLAMYAT_2_DATA registered on DATA.islamyat2Chapters', Array.isArray(D.islamyat2Chapters) && D.islamyat2Chapters.length === 11);
} else {
  check('ISLAMYAT_2_DATA present', false);
}

const NAZ2 = sb.NAZIRA_2_DATA;
if (NAZ2) {
  check('NAZIRA_2_DATA lessons = 15', NAZ2.length === 15, 'got ' + NAZ2.length);
  check('NAZIRA_2_DATA lesson 1 has sections', NAZ2[0] && Array.isArray(NAZ2[0].sections) && NAZ2[0].sections.length > 0);
  check('NAZIRA_2_DATA registered on DATA.nazira2Chapters', Array.isArray(D.nazira2Chapters) && D.nazira2Chapters.length === 15);
} else {
  check('NAZIRA_2_DATA present', false);
}

const GK2 = sb.GK_2_DATA;
if (GK2) {
  check('GK_2_DATA chapters = 16', GK2.length === 16, 'got ' + GK2.length);
  check('GK_2_DATA chapter 1 has sections', GK2[0] && Array.isArray(GK2[0].sections) && GK2[0].sections.length > 0);
  check('GK_2_DATA registered on DATA.gk2Chapters', Array.isArray(D.gk2Chapters) && D.gk2Chapters.length === 16);
} else {
  check('GK_2_DATA present', false);
}

const PS2 = sb.PASHTO_2_DATA;
if (PS2) {
  check('PASHTO_2_DATA units = 28', PS2.length === 28, 'got ' + PS2.length);
  check('PASHTO_2_DATA unit 1 has sections', PS2[0] && Array.isArray(PS2[0].sections) && PS2[0].sections.length > 0);
  check('PASHTO_2_DATA registered on DATA.pashto2Chapters', Array.isArray(D.pashto2Chapters) && D.pashto2Chapters.length === 28);
} else {
  check('PASHTO_2_DATA present', false);
}

const ISL3 = sb.ISLAMYAT_3_DATA;
if (ISL3) {
  check('ISLAMYAT_3_DATA units = 18', ISL3.length === 18, 'got ' + ISL3.length);
  check('ISLAMYAT_3_DATA unit 1 has sections', ISL3[0] && Array.isArray(ISL3[0].sections) && ISL3[0].sections.length > 0);
  check('ISLAMYAT_3_DATA registered on DATA.islamyat3Chapters', Array.isArray(D.islamyat3Chapters) && D.islamyat3Chapters.length === 18);
} else {
  check('ISLAMYAT_3_DATA present', false);
}

const NAZ3 = sb.NAZIRA_3_DATA;
if (NAZ3) {
  check('NAZIRA_3_DATA lessons = 16', NAZ3.length === 16, 'got ' + NAZ3.length);
  check('NAZIRA_3_DATA lesson 1 has sections', NAZ3[0] && Array.isArray(NAZ3[0].sections) && NAZ3[0].sections.length > 0);
  check('NAZIRA_3_DATA registered on DATA.nazira3Chapters', Array.isArray(D.nazira3Chapters) && D.nazira3Chapters.length === 16);
} else {
  check('NAZIRA_3_DATA present', false);
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
check('index.html loads Class 1 Maths data', srcs.includes('js/math_1_data.js') && srcs.indexOf('js/math_1_data.js') < srcs.indexOf('js/app.js'));
check('index.html loads Class 2 Drawing and Maths data', ['js/drawing_2_data.js','js/math_2_data.js'].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
check('index.html loads Class 3 Drawing data before app.js', srcs.includes('js/drawing_3_data.js') && srcs.indexOf('js/drawing_3_data.js') < srcs.indexOf('js/app.js'));
check('index.html loads Class 1 Islamyat data', srcs.includes('js/islamyat_1_data.js') && srcs.indexOf('js/islamyat_1_data.js') < srcs.indexOf('js/app.js'));
check('index.html loads Class 1 Nazira data', srcs.includes('js/nazira_1_data.js') && srcs.indexOf('js/nazira_1_data.js') < srcs.indexOf('js/app.js'));
check('index.html loads Class 1 Pashto data', srcs.includes('js/pashto_1_data.js') && srcs.indexOf('js/pashto_1_data.js') < srcs.indexOf('js/app.js'));
check('index.html loads Class 2 English, Urdu, Islamyat, Nazira, GK, Pashto datasets', [
  'js/english_2_data.js', 'js/urdu_2_data.js', 'js/islamyat_2_data.js',
  'js/nazira_2_data.js', 'js/gk_2_data.js', 'js/pashto_2_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
check('index.html loads Class 3 Islamyat and Nazira datasets', [
  'js/islamyat_3_data.js', 'js/nazira_3_data.js'
].every(f => srcs.includes(f) && srcs.indexOf(f) < srcs.indexOf('js/app.js')));
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
