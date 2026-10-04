const fs = require('fs');
const vm = require('vm');

const path = require('path');
const DIR = path.resolve(__dirname, '../js') + path.sep;
const files = ['data.js', 'drawing_1_data.js', 'drawing_2_data.js', 'data_chem.js', 'data_phys.js', 'data_eng.js', 'data_bio.js', 'data_comp.js', 'dictionary_data.js', 'urdu_data.js', 'urdu_10_data.js', 'english_data.js', 'english_10_data.js', 'english_1_data.js', 'math_data.js', 'pakstudy_data.js', 'pakstudy_10_data.js', 'bio_data.js', 'islamyat_data.js', 'islamyat_10_data.js', 'islamyat_1_data.js', 'nazira_1_data.js', 'pashto_1_data.js', 'math_10_data.js', 'math_1_data.js', 'math_2_data.js', 'english_2_data.js', 'urdu_2_data.js', 'islamyat_2_data.js', 'nazira_2_data.js', 'gk_2_data.js', 'pashto_2_data.js'];

function makeEl(id) {
  const style = {};
  const el = {
    _id: id, innerHTML: '', textContent: '', value: '', className: '', title: '', src: '', href: '',
    style: new Proxy(style, { get: (t, k) => (k in t ? t[k] : ''), set: (t, k, v) => { t[k] = v; return true; } }),
    classList: { add() { }, remove() { }, toggle() { }, contains() { return false; } },
    dataset: {}, children: [], scrollHeight: 100, scrollTop: 0, offsetHeight: 100, checked: false, disabled: false,
    addEventListener() { }, removeEventListener() { }, appendChild() { }, insertBefore() { }, removeChild() { }, remove() { },
    setAttribute() { }, getAttribute() { return null; }, removeAttribute() { }, focus() { }, click() { }, blur() { },
    querySelector() { return makeEl(); }, querySelectorAll() { return []; }, closest() { return null; },
    getBoundingClientRect() { return { top: 0, left: 0, right: 0, bottom: 0, width: 0, height: 0 }; },
    contains() { return false; }, cloneNode() { return makeEl(); }, matches() { return false; }
  };
  return el;
}
const registry = {};
const NodeFilter = {
  SHOW_TEXT: 4,
  FILTER_ACCEPT: 1,
  FILTER_REJECT: 2,
  FILTER_SKIP: 3
};
const documentStub = {
  getElementById(id) { if (!registry[id]) registry[id] = makeEl(id); return registry[id]; },
  querySelector() { return makeEl(); },
  querySelectorAll() { return []; },
  createElement() { return makeEl(); },
  createTreeWalker() { return { nextNode: () => null }; },
  addEventListener() { }, removeEventListener() { },
  body: makeEl('body'), documentElement: makeEl('html'), head: makeEl('head'),
  location: { href: 'http://localhost/', search: '', hash: '' }
};
const windowStub = {
  document: documentStub, location: documentStub.location,
  localStorage: { getItem: () => null, setItem() { }, removeItem() { } },
  sessionStorage: { getItem: () => null, setItem() { } },
  open() { }, addEventListener() { }, removeEventListener() { },
  requestAnimationFrame() { return 0; }, matchMedia: () => ({ matches: false, addEventListener() { } }),
  navigator: { userAgent: 'smoke' }, innerWidth: 1400, innerHeight: 900,
  NodeFilter
};
windowStub.window = windowStub;

const sb = vm.createContext({
  console, window: windowStub, document: documentStub, NodeFilter,
  localStorage: windowStub.localStorage, sessionStorage: windowStub.sessionStorage,
  navigator: windowStub.navigator, location: documentStub.location,
  setTimeout, clearTimeout, setInterval, clearInterval,
  requestAnimationFrame: windowStub.requestAnimationFrame,
  getComputedStyle: () => ({ getPropertyValue: () => '' }),
  module: undefined, exports: undefined
});
const declared = new Set();
for (const f of files) {
  const code = fs.readFileSync(DIR + f, 'utf8');
  const re = /^\s*(?:const|var|let)\s+([A-Za-z_$][\w$]*)/gm;
  let d; while ((d = re.exec(code))) declared.add(d[1]);
  vm.runInContext(code, sb, { filename: f, timeout: 60000 });
}
vm.runInContext('for (const n of ' + JSON.stringify([...declared]) + ') { try { globalThis[n] = eval(n); } catch (e) {} }', sb);
// app.js declares functions / let state -> hoist those too
{
  const code = fs.readFileSync(DIR + 'app.js', 'utf8');
  const names = new Set();
  const re = /^\s*(?:function\s+([A-Za-z_$][\w$]*)|(?:const|let|var)\s+([A-Za-z_$][\w$]*))/gm;
  let m; while ((m = re.exec(code))) names.add(m[1] || m[2]);
  vm.runInContext(code, sb, { filename: 'app.js', timeout: 60000 });
  vm.runInContext('for (const n of ' + JSON.stringify([...names]) + ') { try { globalThis[n] = eval(n); } catch (e) {} }', sb);
}

let fails = 0;
function run(label, src) {
  try { vm.runInContext(src, sb, { timeout: 20000 }); console.log('PASS  ' + label); }
  catch (e) { fails++; console.log('FAIL  ' + label + ' -> ' + (e && e.message)); }
}

run("openSubject cls9 isl", `openSubject("cls9","cls9-isl")`);
run("selectIslChapter(3)", `selectIslChapter(3)`);
run("switchIslTab('exercise')", `switchIslTab('exercise')`);
run("switchIslTab('slos')", `switchIslTab('slos')`);
run("switchIslSloTab('slo-sq')", `switchIslSloTab('slo-sq')`);
run("switchIslSloTab('slo-lq')", `switchIslSloTab('slo-lq')`);
run("switchIslTab('ps-trans')", `switchIslTab('ps-trans')`);
run("switchIslTab('video')", `switchIslTab('video')`);
run("switchIslTab('pages')", `switchIslTab('pages')`);
run("selectIslChapter(14)", `selectIslChapter(14)`);
run("openSubject cls10 isl", `openSubject("cls10","cls10-isl")`);
run("selectIslChapter(17)", `selectIslChapter(17)`);
run("openSubject cls10 math", `openSubject("cls10","cls10-math")`);
run("selectMathChapter(0)", `selectMathChapter(0)`);
run("switchMathTab('lesson')", `switchMathTab('lesson')`);
run("switchMathTab('examples')", `switchMathTab('examples')`);
run("switchMathTab('exercises')", `switchMathTab('exercises')`);
run("switchMathTab('slos')", `switchMathTab('slos')`);
run("switchMathTab('formulas')", `switchMathTab('formulas')`);
run("selectMathChapter(12)", `selectMathChapter(12)`);
run("CLASS 1 openSubject mathematics", `openSubject('cls1','cls1-math'); if (!/Whole Numbers/.test($('mathTopicArea').innerHTML)) throw new Error('Class 1 Maths Unit 1 missing');`);
run("CLASS 1 Maths has six units", `if (getMathChapterList('cls1').length !== 6) throw new Error('Class 1 Maths unit list incomplete');`);
run("CLASS 1 Maths lessons render", `switchMathTab('lesson'); if (!/Counting and Number Names/.test($('mathTabContent').innerHTML)) throw new Error('lesson content missing');`);
run("CLASS 1 Maths Urdu lessons match the topic", `const c=getMathChapterList('cls1')[0]; const u=renderMathTopicSubContent(c.sections[0],c,'urdu',0); if (!/چیزوں کو ایک ایک کرکے گنیں/.test(u) || /قالب/.test(u)) throw new Error('Class 1 Urdu lesson text is missing or inherited from another grade');`);
run("CLASS 1 Maths worked examples render", `switchMathTab('examples'); if (!/Counting and Place Value/.test($('mathTabContent').innerHTML)) throw new Error('worked examples missing');`);
run("CLASS 1 Maths solved exercises render", `switchMathTab('exercises'); if (!/Ex 1.1/.test($('mathTabContent').innerHTML)) throw new Error('solved exercise navigation missing');`);
run("CLASS 1 Maths exam bank uses its own MCQs", `switchMathTab('slos'); if (!/What number comes after 59/.test($('mathTabContent').innerHTML)) throw new Error('Class 1 exam MCQs missing');`);
run("CLASS 1 Maths MCQ answer feedback renders", `switchMathSloCategory('mcqs'); selectMathMcqOption(0, 1, true, 'Count one more than 59: the answer is 60.'); if (!/math-mcq/.test($('mathSloContentArea').innerHTML)) throw new Error('MCQ feedback controls missing');`);
run("CLASS 1 Maths summary renders", `switchMathTab('formulas'); if (!/Place value/.test($('mathTabContent').innerHTML)) throw new Error('revision summary missing');`);
run("CLASS 2 Drawing opens with Exam Practice", `openSubject('cls2','cls2-drawing'); if (state.selectedClass!=='cls2' || !/Join the dots and colour the shapes/.test($('dashboard-body').innerHTML) || !/MCQs/.test($('dashboard-body').innerHTML)) throw new Error('Class 2 Drawing view or practice missing');`);
run("CLASS 2 Drawing has 32 trilingual vector activities", `state.activeDrawingTab='activities'; renderDrawingView(); if (DRAWING_2_DATA.length!==32 || !/پښتو/.test($('dashboard-body').innerHTML) || !/<svg/.test($('dashboard-body').innerHTML)) throw new Error('Class 2 Drawing activities missing');`);
run("CLASS 2 Drawing answer feedback works", `state.activeDrawingTab='practice'; answerDrawingMcq(0,2); if (!/is-correct/.test($('dashboard-body').innerHTML) || !/Correct! Well done./.test($('dashboard-body').innerHTML)) throw new Error('Class 2 MCQ feedback missing');`);
run("CLASS 2 Drawing SQ and LQ answers expand in three languages", `state.activeDrawingTab='practice'; selectDrawingExamTab('sqs'); if (!/Name three tools/.test($('dashboard-body').innerHTML)) throw new Error('Class 2 SQ bank missing'); selectDrawingExamTab('lqs'); if (!/paper-folding models/.test($('dashboard-body').innerHTML)) throw new Error('Class 2 LQ bank missing');`);
run("CLASS 2 Mathematics opens six workbook units", `openSubject('cls2','cls2-math'); if (getMathChapterList('cls2').length!==6 || !/Whole Numbers/.test($('mathTopicArea').innerHTML)) throw new Error('Class 2 Maths did not open');`);
run("CLASS 2 Mathematics addition lessons and Urdu render", `selectMathChapter(1); switchMathTab('lesson'); const m2chapter=getMathChapterList('cls2')[1]; const m2urdu=renderMathTopicSubContent(m2chapter.sections[0],m2chapter,'urdu',0); if (!/Addition of Three-Digit Numbers/.test($('mathTabContent').innerHTML) || !/اکائیوں/.test(m2urdu)) throw new Error('Class 2 Maths lesson or Urdu translation missing');`);
run("CLASS 2 Mathematics solved exercises render", `selectMathChapter(1); switchMathTab('exercises'); if (!/Ex 2.1/.test($('mathTabContent').innerHTML)) throw new Error('Class 2 Maths exercise missing');`);
run("CLASS 2 Mathematics board bank uses Class 2 questions", `selectMathChapter(0); switchMathTab('slos'); if (!/What is the value of 5 in 352/.test($('mathTabContent').innerHTML)) throw new Error('Class 2 exam bank missing');`);
run("CLASS 2 Mathematics wrong MCQ shows red choice and green answer", `switchMathSloCategory('mcqs'); const m2card=document.getElementById('math-mcq-0'); const m2buttons=[0,1,2,3].map(()=>({style:{},innerHTML:'Option',disabled:false})); m2card.querySelectorAll=()=>m2buttons; selectMathMcqOption(0,0,false,'Try again.',1); if (m2buttons[0].style.background!=='#fee2e2' || m2buttons[1].style.background!=='#dcfce7') throw new Error('Class 2 wrong answer feedback missing');`);
run("CLASS 2 Mathematics formulas render", `selectMathChapter(3); switchMathTab('formulas'); if (!/1 m/.test($('mathTabContent').innerHTML)) throw new Error('Class 2 measurement summary missing');`);
run("showWordMeaning", `showWordMeaning(document.createElement("span"))`);
run("REGRESSION openSubject cls9 eng", `openSubject("cls9","cls9-eng")`);
run("REGRESSION selectEngChapter(2)", `selectEngChapter(2)`);
run("REGRESSION switchEngTab('reading')", `switchEngTab('reading')`);
run("REGRESSION openSubject cls9 urdu", `openSubject("cls9","cls9-urdu")`);
run("REGRESSION selectUrduChapter(1)", `selectUrduChapter(1)`);
run("REGRESSION openSubject cls9 chem", `openSubject("cls9","cls9-chem")`);
run("REGRESSION selectChemChapter(1)", `selectChemChapter(1)`);
run("REGRESSION openSubject cls9 bio", `openSubject("cls9","cls9-bio")`);
run("REGRESSION openSubject cls9 math", `openSubject("cls9","cls9-math")`);
run("REGRESSION openSubject cls9 pakstudy", `openSubject("cls9","cls9-pakstudy")`);
run("REGRESSION openSubject cls9 comp", `openSubject("cls9","cls9-comp")`);
run("REGRESSION comp switchSubjectTab('concepts')", `switchSubjectTab('comp', 'concepts', 0, 'cls9')`);
run("REGRESSION comp switchSubjectTab('exercise')", `switchSubjectTab('comp', 'exercise', 0, 'cls9')`);
run("REGRESSION comp switchSubjectTab('slos')", `switchSubjectTab('comp', 'slos', 0, 'cls9')`);
run("REGRESSION comp switchSubjectTab('formulas')", `switchSubjectTab('comp', 'formulas', 0, 'cls9')`);
run("REGRESSION comp selectSubjectChapter(1)", `selectSubjectChapter('comp', 1, 'cls9')`);
run("CLASS 10 openSubject cls10 eng", `openSubject("cls10","cls10-eng")`);
run("CLASS 10 selectSubjectChapter eng 14", `selectSubjectChapter('eng', 14, 'cls10')`);
run("CLASS 10 openSubject cls10 pakstudy", `openSubject("cls10","cls10-pakstudy")`);
run("CLASS 10 selectSubjectChapter pakstudy 3", `selectSubjectChapter('pakstudy', 3, 'cls10')`);
run("CLASS 10 openSubject cls10 urdu", `openSubject("cls10","cls10-urdu")`);
run("CLASS 10 selectSubjectChapter urdu 0", `selectSubjectChapter('urdu', 0, 'cls10')`);
run("CLASS 10 openSubject cls10 chem", `openSubject("cls10","cls10-chem")`);
run("CLASS 10 openSubject cls10 phy", `openSubject("cls10","cls10-phy")`);
run("CLASS 10 openSubject cls10 bio", `openSubject("cls10","cls10-bio")`);
run("CLASS 10 goToSubjects cls10", `goToSubjects('cls10')`);
run("CLASS 10 renderBooksView cls10", `renderBooksView('cls10')`);
run("CLASS 1 goToSubjects lists Drawing", `goToSubjects('cls1'); if (!/Drawing/.test($('dashboard-body').innerHTML)) throw new Error('Drawing subject card missing');`);
run("CLASS 2 subjects are reachable and list Maths and Drawing", `goToSubjects('cls2'); if (!/Mathematics/.test($('dashboard-body').innerHTML) || !/Drawing/.test($('dashboard-body').innerHTML) || /Subjects Not Uploaded Yet/.test($('dashboard-body').innerHTML)) throw new Error('Class 2 subjects are still behind the upload gate');`);
run("CLASS 3 retains the not-uploaded notice", `goToSubjects('cls3'); if (!/Subjects Not Uploaded Yet/.test($('dashboard-body').innerHTML)) throw new Error('Not-uploaded gate changed for Class 3');`);
run("CLASS 1 opens with expanded Exam Practice", `openSubject('cls1','cls1-drawing'); if (state.activeDrawingTab!=='practice' || state.activeDrawingExamTab!=='mcqs' || !/drawing-practice-tabs/.test($('dashboard-body').innerHTML) || !/drawing-option/.test($('dashboard-body').innerHTML) || /Drawing Exam Practice|CLASS 1 · REVISION|Practice questions based on the workbook activities/.test($('dashboard-body').innerHTML)) throw new Error('expanded Exam Practice or compact layout missing');`);
run("CLASS 1 Activities omit lesson heading and caption", `state.activeDrawingTab='activities'; renderDrawingView(); const body=$('dashboard-body').innerHTML; if (!/<svg/.test(body) || !/drawing-trace/.test(body) || !/English/.test(body) || !/پښتو/.test(body) || /CLASS 1 · CREATIVE ARTS & DRAWING|Workbook activity 1 · Page 1|<figcaption/.test(body) || /\.jpg|\.png/.test(body)) throw new Error('Activity view still has removed text or is missing vector tips');`);
run("CLASS 1 Drawing selects activity 32", `selectDrawingPage(31); if (!/Making a cat face/.test($('dashboard-body').innerHTML) || !/Folded cat face/.test($('dashboard-body').innerHTML)) throw new Error('final activity missing');`);
run("CLASS 1 Exam Practice shows MCQs without duplicate heading", `state.activeDrawingTab='practice'; state.activeDrawingExamTab='mcqs'; state.drawingMcqAnswers={}; renderDrawingView(); if (!/MCQs/.test($('dashboard-body').innerHTML) || /Drawing Exam Practice|CLASS 1 · REVISION|Practice questions based on the workbook activities/.test($('dashboard-body').innerHTML)) throw new Error('exam tabs or compact practice panel missing');`);
run("CLASS 1 MCQ wrong answer shows red cross and correct green option", `answerDrawingMcq(0,1); const html=$('dashboard-body').innerHTML; if (!/is-wrong/.test(html) || !/is-correct/.test(html) || !/✕/.test(html) || !/✓/.test(html) || !/نمبروں کی ترتیب/.test(html)) throw new Error('MCQ answer feedback or translations missing');`);
run("CLASS 1 MCQ correct answer shows green", `answerDrawingMcq(0,0); if (!/Correct! Well done./.test($('dashboard-body').innerHTML)) throw new Error('correct response missing');`);
run("CLASS 1 SQ tab reveals multilingual answer on question line", `selectDrawingExamTab('sqs'); globalThis.__drawingHtml=$('dashboard-body').innerHTML; if (!/SQ 1/.test(globalThis.__drawingHtml) || !/نقطے ملانے/.test(globalThis.__drawingHtml) || !/Suggested answer/.test(globalThis.__drawingHtml)) throw new Error('multilingual SQ tab missing');`);
run("CLASS 1 LQ tab reveals Pashto answer on question line", `selectDrawingExamTab('lqs'); globalThis.__drawingHtml=$('dashboard-body').innerHTML; if (!/LQ 1/.test(globalThis.__drawingHtml) || !/نښلولو سره د حیوان/.test(globalThis.__drawingHtml) || !/پښتو/.test(globalThis.__drawingHtml)) throw new Error('multilingual LQ tab missing'); state.activeDrawingTab='activities';`);
run("CLASS 1 goToSubjects lists English", `goToSubjects('cls1'); if (!/English/.test($('dashboard-body').innerHTML)) throw new Error('English subject card missing for Class 1');`);
run("CLASS 1 openSubject cls1-eng", `openSubject('cls1','cls1-eng')`);
run("CLASS 1 selectSubjectChapter eng 0", `selectSubjectChapter('eng', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab eng lesson", `switchSubjectTab('eng', 'lesson', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab eng exercise", `switchSubjectTab('eng', 'exercise', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab eng slos", `switchSubjectTab('eng', 'slos', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab eng words", `switchSubjectTab('eng', 'words', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab eng grammar", `switchSubjectTab('eng', 'grammar', 0, 'cls1')`);
run("CLASS 1 selectSubjectChapter eng 10 (Unit 11)", `selectSubjectChapter('eng', 10, 'cls1')`);
run("CLASS 1 goToSubjects lists Islamyat", `goToSubjects('cls1'); if (!/Islamyat|اسلامیات/.test($('dashboard-body').innerHTML)) throw new Error('Islamyat subject card missing for Class 1');`);
run("CLASS 1 goToSubjects lists Nazira", `goToSubjects('cls1'); if (!/Nazira|ناظرہ/.test($('dashboard-body').innerHTML)) throw new Error('Nazira subject card missing for Class 1');`);
run("CLASS 1 openSubject cls1-isl", `openSubject('cls1','cls1-isl')`);
run("CLASS 1 selectSubjectChapter isl 0", `selectSubjectChapter('isl', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab isl lesson", `switchSubjectTab('isl', 'lesson', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab isl concepts", `switchSubjectTab('isl', 'concepts', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab isl exercise", `switchSubjectTab('isl', 'exercise', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab isl slos", `switchSubjectTab('isl', 'slos', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab isl formulas", `switchSubjectTab('isl', 'formulas', 0, 'cls1')`);
run("CLASS 1 selectSubjectChapter isl 9 (Unit 10)", `selectSubjectChapter('isl', 9, 'cls1')`);
run("CLASS 1 openSubject cls1-nazira", `openSubject('cls1','cls1-nazira')`);
run("CLASS 1 selectSubjectChapter nazira 0", `selectSubjectChapter('nazira', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab nazira lesson", `switchSubjectTab('nazira', 'lesson', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab nazira concepts", `switchSubjectTab('nazira', 'concepts', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab nazira exercise", `switchSubjectTab('nazira', 'exercise', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab nazira slos", `switchSubjectTab('nazira', 'slos', 0, 'cls1')`);
run("CLASS 1 selectSubjectChapter nazira 16 (Surahs)", `selectSubjectChapter('nazira', 16, 'cls1')`);
run("CLASS 1 goToSubjects lists Pashto", `goToSubjects('cls1'); if (!/Pashto|پښتو/.test($('dashboard-body').innerHTML)) throw new Error('Pashto subject card missing for Class 1');`);
run("CLASS 1 openSubject cls1-pashto", `openSubject('cls1','cls1-pashto')`);
run("CLASS 1 selectSubjectChapter pashto 0", `selectSubjectChapter('pashto', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab pashto lesson", `switchSubjectTab('pashto', 'lesson', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab pashto exercise", `switchSubjectTab('pashto', 'exercise', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab pashto slos", `switchSubjectTab('pashto', 'slos', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab pashto words", `switchSubjectTab('pashto', 'words', 0, 'cls1')`);
run("CLASS 1 switchSubjectTab pashto grammar", `switchSubjectTab('pashto', 'grammar', 0, 'cls1')`);
run("CLASS 1 selectSubjectChapter pashto 22 (Unit 23)", `selectSubjectChapter('pashto', 22, 'cls1')`);

// ---- Class 2 Subject Port Verification ----
run("CLASS 2 goToSubjects lists all 8 subjects", `goToSubjects('cls2'); const c2Html = $('dashboard-body').innerHTML; if (!/English/.test(c2Html) || !/Urdu|اردو/.test(c2Html) || !/Mathematics/.test(c2Html) || !/General Knowledge|واقفیتِ عامہ/.test(c2Html) || !/Islamyat|اسلامیات/.test(c2Html) || !/Nazira|ناظرہ/.test(c2Html) || !/Pashto|پښتو/.test(c2Html) || !/Drawing/.test(c2Html)) throw new Error('Class 2 missing subject cards: ' + c2Html);`);
run("CLASS 2 openSubject cls2-eng", `openSubject('cls2','cls2-eng')`);
run("CLASS 2 selectSubjectChapter eng 0", `selectSubjectChapter('eng', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab eng lesson", `switchSubjectTab('eng', 'lesson', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab eng exercise", `switchSubjectTab('eng', 'exercise', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab eng slos", `switchSubjectTab('eng', 'slos', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab eng words", `switchSubjectTab('eng', 'words', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab eng grammar", `switchSubjectTab('eng', 'grammar', 0, 'cls2')`);
run("CLASS 2 selectSubjectChapter eng 11 (Unit 12)", `selectSubjectChapter('eng', 11, 'cls2')`);

run("CLASS 2 openSubject cls2-urdu", `openSubject('cls2','cls2-urdu')`);
run("CLASS 2 selectSubjectChapter urdu 0", `selectSubjectChapter('urdu', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab urdu lesson", `switchSubjectTab('urdu', 'lesson', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab urdu exercise", `switchSubjectTab('urdu', 'exercise', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab urdu slos", `switchSubjectTab('urdu', 'slos', 0, 'cls2')`);
run("CLASS 2 selectSubjectChapter urdu 21 (Lesson 22)", `selectSubjectChapter('urdu', 21, 'cls2')`);

run("CLASS 2 openSubject cls2-isl", `openSubject('cls2','cls2-isl')`);
run("CLASS 2 selectSubjectChapter isl 0", `selectSubjectChapter('isl', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab isl lesson", `switchSubjectTab('isl', 'lesson', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab isl exercise", `switchSubjectTab('isl', 'exercise', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab isl slos", `switchSubjectTab('isl', 'slos', 0, 'cls2')`);
run("CLASS 2 selectSubjectChapter isl 10 (Unit 11)", `selectSubjectChapter('isl', 10, 'cls2')`);

run("CLASS 2 openSubject cls2-nazira", `openSubject('cls2','cls2-nazira')`);
run("CLASS 2 selectSubjectChapter nazira 0", `selectSubjectChapter('nazira', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab nazira lesson", `switchSubjectTab('nazira', 'lesson', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab nazira exercise", `switchSubjectTab('nazira', 'exercise', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab nazira slos", `switchSubjectTab('nazira', 'slos', 0, 'cls2')`);
run("CLASS 2 selectSubjectChapter nazira 14 (Lesson 15)", `selectSubjectChapter('nazira', 14, 'cls2')`);

run("CLASS 2 openSubject cls2-gk", `openSubject('cls2','cls2-gk')`);
run("CLASS 2 selectSubjectChapter gk 0", `selectSubjectChapter('gk', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab gk lesson", `switchSubjectTab('gk', 'lesson', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab gk exercise", `switchSubjectTab('gk', 'exercise', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab gk slos", `switchSubjectTab('gk', 'slos', 0, 'cls2')`);
run("CLASS 2 selectSubjectChapter gk 15 (Chapter 16)", `selectSubjectChapter('gk', 15, 'cls2')`);

run("CLASS 2 openSubject cls2-pashto", `openSubject('cls2','cls2-pashto')`);
run("CLASS 2 selectSubjectChapter pashto 0", `selectSubjectChapter('pashto', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab pashto lesson", `switchSubjectTab('pashto', 'lesson', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab pashto exercise", `switchSubjectTab('pashto', 'exercise', 0, 'cls2')`);
run("CLASS 2 switchSubjectTab pashto slos", `switchSubjectTab('pashto', 'slos', 0, 'cls2')`);
run("CLASS 2 selectSubjectChapter pashto 27 (Lesson 28)", `selectSubjectChapter('pashto', 27, 'cls2')`);

run("REGRESSION renderClasses", `renderClasses()`);
run("REGRESSION handleGlobalSearch('islam')", `handleGlobalSearch("islam")`);
run("REGRESSION handleGlobalSearch('daffodils')", `handleGlobalSearch("daffodils")`);
run("REGRESSION handleGlobalSearch('iqbal')", `handleGlobalSearch("iqbal")`);

// ---- Phase 2: Maaz feature ports (vocab / summaries / stats / helpers) ----
run("PORT ENG_UNIT_VOCAB_WORDS loaded", `if (typeof ENG_UNIT_VOCAB_WORDS === 'undefined' || !ENG_UNIT_VOCAB_WORDS[2]) throw new Error('vocab lexicon missing');`);
run("PORT lookupEngWord loaded", `if (typeof lookupEngWord !== 'function') throw new Error('lookupEngWord missing');`);
run("PORT autoScrollToActiveTab defined", `if (typeof autoScrollToActiveTab !== 'function') throw new Error('missing');`);
run("PORT getUrduChapterList length", `if (getUrduChapterList().length !== 19 && getUrduChapterList().length !== 15) throw new Error('got ' + getUrduChapterList().length);`);
run("PORT eng tabs include English Summary", `openSubject("cls9","cls9-eng"); if (!/English Summary/.test($("engTabsBar").innerHTML)) throw new Error('en-sum tab missing');`);
run("PORT switchEngTab('vocab') renders", `switchEngTab('vocab', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('en-sum') renders", `switchEngTab('en-sum', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('lesson') renders", `switchEngTab('lesson', 0); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('urdu-trans') renders", `switchEngTab('urdu-trans', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('pashto-trans') renders", `switchEngTab('pashto-trans', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('video') renders", `switchEngTab('video', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('urdu-sum') renders", `switchEngTab('urdu-sum', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('pashto-sum') renders", `switchEngTab('pashto-sum', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('slos') renders", `switchEngTab('slos', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT switchEngTab('exercise') renders", `switchEngTab('exercise', 1); if (!$("engTabContent").innerHTML) throw new Error('empty');`);
run("PORT figurativeLines (unit 8)", `selectEngChapter(7); switchEngTab('exercise', 7); if (!/Figurative/.test($("engTabContent").innerHTML)) throw new Error('figurative block missing');`);
run("PORT renderHome()", `renderHome()`);
run("PORT renderBooksView()", `renderBooksView()`);
run("PORT goToSubjects('cls9')", `goToSubjects('cls9')`);
run("PORT goToSubjects cls9 lists Islamyat", `goToSubjects('cls9'); const h = (($("dashboard-body").innerHTML || '') + ($("page-content").innerHTML || '')); if (!/Islamyat/i.test(h)) throw new Error('isl subject not listed');`);
run("PORT handleGlobalSearch('chemistry')", `handleGlobalSearch("chemistry")`);
run("PORT handleGlobalSearch('solved')", `handleGlobalSearch("solved")`);
run("PORT handleGlobalSearch no-results path (sanitize)", `handleGlobalSearch("zzzznotfoundqqq"); if (!/No results found/.test($("searchResultsDropdown").innerHTML)) throw new Error('no-results block missing');`);
run("PORT checkPakStudySloMcq records stats", `openSubject("cls9","cls9-pakstudy"); switchPakStudySloTab('slo-mcqs'); globalThis.__saved = null; localStorage.setItem = (k, v) => { globalThis.__saved = v; }; checkPakStudySloMcq(0, 'a', 'b', encodeURIComponent('because')); if (!globalThis.__saved) throw new Error('stats not saved');`);
console.log('state after tests = activeSubject=' + vm.runInContext('state.activeSubject', sb) + ' selectedIslChapter=' + vm.runInContext('state.selectedIslChapter', sb));
process.exit(fails ? 1 : 0);
