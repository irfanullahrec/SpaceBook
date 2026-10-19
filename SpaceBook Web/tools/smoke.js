'use strict';
/* Smoke test: loads the whole app exactly as index.html does (tools/lib/app_sandbox.js) and drives it
 * through its public functions.   node tools/smoke.js   (exit 1 on any failure) */
const vm = require('vm');
const { load } = require('./lib/app_sandbox');
const app = load({ page: process.env.SB_PAGE || 'index.html' });     // SB_PAGE=lazy.html runs every check against the lazy-loading page
const sb = app.sb;
if (app.loadFails.length) { console.log('FAIL  every index.html script loads -> ' + app.loadFails.join(' | ')); process.exitCode = 1; }

let fails = 0;
function run(label, src) {
  // each test runs in its own block so its const/let names do not collide with the next test
  try { vm.runInContext('{' + src + '\n}', sb, { timeout: 120000 }); console.log('PASS  ' + label); }
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
run("CLASS 1 Maths has six units", `if (getMathChapterList('cls1').length !== 6) throw new Error('Class 1 Maths unit list incomplete');`);
run("CLASS 1 Maths Urdu lessons match the topic", `const c=getMathChapterList('cls1')[0]; const u=renderMathTopicSubContent(c.sections[0],c,'urdu',0); if (!/چیزوں کو ایک ایک کرکے گنیں/.test(u) || /قالب/.test(u)) throw new Error('Class 1 Urdu lesson text is missing or inherited from another grade');`);
run("CLASS 2 Mathematics wrong MCQ shows red choice and green answer", `switchMathSloCategory('mcqs'); const m2card=document.getElementById('math-mcq-0'); const m2buttons=[0,1,2,3].map(()=>({style:{},innerHTML:'Option',disabled:false})); m2card.querySelectorAll=()=>m2buttons; selectMathMcqOption(0,0,false,'Try again.',1); if (m2buttons[0].style.background!=='#fee2e2' || m2buttons[1].style.background!=='#dcfce7') throw new Error('Class 2 wrong answer feedback missing');`);
run("CLASS 2 Maths worked examples include vector diagrams", `state.selectedClass='cls2'; for (const ch of MATH_2_DATA) { const html=renderMathExamples(ch); const count=(html.match(/<figure class="math-diagram/g)||[]).length; if(count<(ch.workedExamples||[]).length) throw new Error('Class 2 worked example diagrams missing in '+ch.title); }`);
// ---------------------------------------------------------------- rebuilt books (Classes 1-10, CLSn_BOOKS)
// Every page-reviewed book opens through the real reader: the chapter list has one button per unit, and the
// first and last units render every tab they offer with non-empty content.
const BOOK_NOT_COMPLETE = ['cls1.gk', 'cls1.urdu', 'cls3.urdu', 'cls8.drawing'];
run("REBUILT BOOKS open with every unit and every tab rendering", `
  const problems = [], seen = [];
  const NOT_COMPLETE = ${JSON.stringify(BOOK_NOT_COMPLETE)};
  for (let n = 1; n <= 10; n++) {
    const B = window['CLS' + n + '_BOOKS'] || {}, cls = 'cls' + n;
    for (const key of Object.keys(B)) {
      if (NOT_COMPLETE.includes(cls + '.' + key)) continue;
      const units = B[key].units || [];
      const subj = (DATA.subjects[cls] || []).find(s => {
        openSubject(cls, s.id);
        return new RegExp("selectSubjectChapter\\\\('" + key + "',").test($('dashboard-body').innerHTML);
      });
      if (!subj) { problems.push(cls + '.' + key + ': no registered subject opens it'); continue; }
      openSubject(cls, subj.id);
      const body = $('dashboard-body').innerHTML;
      // at least every rebuilt unit; a few legacy books (Class 10 Physics/Chemistry) add earlier units around it
      if (!body.includes('subj-ch-btn-' + (units.length - 1) + '"'))
        problems.push(cls + '.' + key + ': chapter list shows fewer than ' + units.length + ' units');
      for (const i of [...new Set([0, units.length - 1])]) {
        state.activeSubjTab = null;
        selectSubjectChapter(key, i, cls);
        const tabs = [...new Set([...$('subjectTopicArea').innerHTML.matchAll(/data-tab="([^"]+)"/g)].map(m => m[1]))];
        if (!tabs.length) problems.push(cls + '.' + key + ' unit ' + (i + 1) + ': no tabs');
        for (const t of tabs) {
          switchSubjectTab(key, t, i, cls);
          if (!$('subjTabContent').innerHTML.trim()) problems.push(cls + '.' + key + ' unit ' + (i + 1) + ' tab ' + t + ': empty');
        }
      }
      seen.push(cls + '.' + key);
    }
  }
  if (seen.length < 80) problems.push('only ' + seen.length + ' books checked');
  if (problems.length) throw new Error(problems.length + ' problems: ' + problems.slice(0, 12).join(' | '));
  globalThis.__rebuiltChecked = seen.length;
`);
console.log('      rebuilt books checked: ' + vm.runInContext('globalThis.__rebuiltChecked || 0', sb));

// ------------------------------------------------- Class 12 page-reviewed books (front-matter "source" entries count)
for (const [subjId, key, units, sources] of [
  ['cls12-eng', 'eng', 19, 1], ['cls12-urdu', 'urdu', 22, 13], ['cls12-pak', 'pak', 11, 1], ['cls12-comp', 'comp', 9, 2],
  ['cls12-civics', 'civics', 8, 2], ['cls12-econ', 'econ', 13, 2], ['cls12-hpe', 'hpe', 6, 3], ['cls12-islopt', 'islopt', 6, 2],
  ['cls12-islhist', 'islhist', 6, 37], ['cls12-quran', 'quran', 8, 18],
]) {
  run(`CLASS 12 ${subjId} opens ${units} units (+${sources} source pages) and renders first/last tabs`, `
    openSubject('cls12', '${subjId}');
    const key = (($('dashboard-body').innerHTML.match(/selectSubjectChapter\\('([a-z0-9_]+)',/) || [])[1]);
    if (!key) throw new Error('no chapter list');
    const list = getSubjectChapterList(key, 'cls12');
    const nUnits = list.filter(c => c.type !== 'source').length, nSrc = list.length - nUnits;
    if (nUnits !== ${units} || nSrc !== ${sources}) throw new Error('got ' + nUnits + ' units + ' + nSrc + ' source pages');
    for (const i of [0, list.length - 1]) {
      state.activeSubjTab = null;
      selectSubjectChapter(key, i, 'cls12');
      const tabs = [...new Set([...$('subjectTopicArea').innerHTML.matchAll(/data-tab="([^"]+)"/g)].map(m => m[1]))];
      for (const t of tabs) { switchSubjectTab(key, t, i, 'cls12'); if (!$('subjTabContent').innerHTML.trim()) throw new Error('entry ' + i + ' tab ' + t + ' empty'); }
    }
  `);
}

run("CLASS 3 lists every registered subject", `goToSubjects('cls3'); const h=$('dashboard-body').innerHTML; const miss=DATA.subjects.cls3.filter(s=>!h.includes(s.name)).map(s=>s.name); if (miss.length) throw new Error('missing: '+miss.join(', '));`);
run("CLASS 4 lists its uploaded books instead of the not-uploaded notice", `goToSubjects('cls4'); const h=$('dashboard-body').innerHTML; if (/Subjects Not Uploaded Yet/.test(h) || !/English/.test(h) || !/Mathematics/.test(h)) throw new Error('Class 4 subject list not shown');`);


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
run("CLASS 9 openSubject cls9 sci", `openSubject("cls9","cls9-sci")`);
run("CLASS 9 openSubject cls9 hpe", `openSubject("cls9","cls9-hpe")`);
run("CLASS 9 openSubject cls9 drawing", `openSubject("cls9","cls9-drawing")`);
run("CLASS 9 openSubject cls9 islopt", `openSubject("cls9","cls9-islopt")`);
run("CLASS 9 openSubject cls9 quran", `openSubject("cls9","cls9-quran")`);
run("CLASS 10 openSubject cls10 eng", `openSubject("cls10","cls10-eng")`);
run("CLASS 10 selectSubjectChapter eng 14", `selectSubjectChapter('eng', 14, 'cls10')`);
run("CLASS 10 openSubject cls10 pakstudy", `openSubject("cls10","cls10-pakstudy")`);
run("CLASS 10 selectSubjectChapter pakstudy 3", `selectSubjectChapter('pakstudy', 3, 'cls10')`);
run("CLASS 10 openSubject cls10 urdu", `openSubject("cls10","cls10-urdu")`);
run("CLASS 10 selectSubjectChapter urdu 0", `selectSubjectChapter('urdu', 0, 'cls10')`);
run("CLASS 10 openSubject cls10 chem", `openSubject("cls10","cls10-chem")`);
run("CLASS 10 openSubject cls10 phy", `openSubject("cls10","cls10-phy")`);
run("CLASS 10 openSubject cls10 bio", `openSubject("cls10","cls10-bio")`);
run("CLASS 10 openSubject cls10 comp", `openSubject("cls10","cls10-comp")`);
run("CLASS 10 openSubject cls10 sci", `openSubject("cls10","cls10-sci")`);
run("CLASS 10 openSubject cls10 hpe", `openSubject("cls10","cls10-hpe")`);
run("CLASS 10 openSubject cls10 drawing", `openSubject("cls10","cls10-drawing")`);
run("CLASS 10 openSubject cls10 islopt", `openSubject("cls10","cls10-islopt")`);
run("CLASS 10 openSubject cls10 quran", `openSubject("cls10","cls10-quran")`);
run("CLASS 10 goToSubjects cls10", `goToSubjects('cls10')`);
run("CLASS 10 renderBooksView cls10", `renderBooksView('cls10')`);
run("CLASS 1 goToSubjects lists Drawing", `goToSubjects('cls1'); if (!/Drawing/.test($('dashboard-body').innerHTML)) throw new Error('Drawing subject card missing');`);
run("CLASS 2 subjects are reachable and list Maths and Drawing", `goToSubjects('cls2'); if (!/Mathematics/.test($('dashboard-body').innerHTML) || !/Drawing/.test($('dashboard-body').innerHTML) || /Subjects Not Uploaded Yet/.test($('dashboard-body').innerHTML)) throw new Error('Class 2 subjects are still behind the upload gate');`);
run("CLASS 3 subjects are reachable and list Islamyat and Nazira", `goToSubjects('cls3'); if (!/Islamyat|اسلامیات/.test($('dashboard-body').innerHTML) || !/Nazira|ناظرہ قرآن/.test($('dashboard-body').innerHTML) || /Subjects Not Uploaded Yet/.test($('dashboard-body').innerHTML)) throw new Error('Class 3 subjects missing or behind upload gate');`);
run("CLASS 3 Maths lessons show native vector figures", `switchMathTab('lesson'); const c3Lesson=$('mathTabContent').innerHTML; if (!/<svg/.test(c3Lesson) || /\.jpg|\.png/.test(c3Lesson)) throw new Error('Class 3 Maths figures are missing or depend on page images');`);
run("CLASS 12 goToSubjects lists the four completed books", `goToSubjects('cls12'); const h12=$('dashboard-body').innerHTML+$('page-content').innerHTML; if (!/Mathematics/.test(h12) || !/Physics/.test(h12) || !/Chemistry/.test(h12) || !/Statistics/.test(h12) || /Subjects Not Uploaded Yet/.test(h12)) throw new Error('Class 12 subjects are still gated or missing');`);
run("CLASS 12 Maths opens its source units and formula sheet", `openSubject('cls12','cls12-math'); if (getMathChapterList('cls12').length!==12 || !/Introduction to Symbolic/.test($('mathTopicArea').innerHTML)) throw new Error('Class 12 Maths route or units missing'); switchMathTab('formulas'); if (!$('mathTabContent').innerHTML) throw new Error('Class 12 Math formula tab is empty'); switchMathTab('textbook'); if (!/Complete Book Text/.test($('mathTabContent').innerHTML)) throw new Error('Class 12 Math source text tab missing');`);
run("CLASS 12 Physics complete text, practice and figures", `openSubject('cls12','cls12-phy'); if (getSubjectChapterList('phys','cls12').length!==10) throw new Error('Physics unit list missing'); switchSubjectTab('phys','lesson',0,'cls12'); if (!/<svg/.test($('subjTabContent').innerHTML)) throw new Error('Physics vector figure missing'); switchSubjectTab('phys','slos',0,'cls12'); if (!/MCQs|Short Questions|Long Questions/.test($('subjTabContent').innerHTML)) throw new Error('Physics practice bank missing'); switchSubjectTab('phys','booktext',0,'cls12'); if (!/Complete Book Text/.test($('subjTabContent').innerHTML)) throw new Error('Physics transcription missing');`);
run("CLASS 12 Chemistry and Statistics open their textbook units", `openSubject('cls12','cls12-chem'); if (getSubjectChapterList('chem','cls12').length!==12) throw new Error('Chemistry unit list missing'); openSubject('cls12','cls12-stat'); if (getSubjectChapterList('stat','cls12').length!==9) throw new Error('Statistics unit list missing'); state.activeScienceLessonSubTab='translations'; switchSubjectTab('stat','lesson',0,'cls12'); if (!/<svg/.test($('subjTabContent').innerHTML)) throw new Error('Statistics chart missing'); switchSubjectTab('stat','formulas',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Statistics summary empty');`);

run("CLASS 12 Biology opens 14 units", `openSubject('cls12','cls12-bio'); if (getSubjectChapterList('bio','cls12').length!==14) throw new Error('Biology 12 units missing'); switchSubjectTab('bio','lesson',0,'cls12'); if (!$('subjTabContent').innerHTML) throw new Error('Bio 12 lesson empty'); selectSubjectChapter('bio',13,'cls12');`);

run("CLASS 1 Activities omit lesson heading and caption", `state.activeDrawingTab='activities'; renderDrawingView(); const body=$('dashboard-body').innerHTML; if (!/<svg/.test(body) || !/drawing-trace/.test(body) || !/English/.test(body) || !/پښتو/.test(body) || /CLASS 1 · CREATIVE ARTS & DRAWING|Workbook activity 1 · Page 1|<figcaption/.test(body) || /\.jpg|\.png/.test(body)) throw new Error('Activity view still has removed text or is missing vector tips');`);
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

run("CLASS 3 openSubject cls3-isl", `openSubject('cls3','cls3-isl')`);
run("CLASS 3 selectSubjectChapter isl 0", `selectSubjectChapter('isl', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab isl lesson", `switchSubjectTab('isl', 'lesson', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab isl exercise", `switchSubjectTab('isl', 'exercise', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab isl slos", `switchSubjectTab('isl', 'slos', 0, 'cls3')`);
run("CLASS 3 selectSubjectChapter isl 17 (Unit 18)", `selectSubjectChapter('isl', 17, 'cls3')`);

run("CLASS 3 openSubject cls3-nazira", `openSubject('cls3','cls3-nazira')`);
run("CLASS 3 selectSubjectChapter nazira 0", `selectSubjectChapter('nazira', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab nazira lesson", `switchSubjectTab('nazira', 'lesson', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab nazira exercise", `switchSubjectTab('nazira', 'exercise', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab nazira slos", `switchSubjectTab('nazira', 'slos', 0, 'cls3')`);
run("CLASS 3 selectSubjectChapter nazira 15 (Lesson 16)", `selectSubjectChapter('nazira', 15, 'cls3')`);

run("CLASS 3 openSubject cls3-eng", `openSubject('cls3','cls3-eng')`);
run("CLASS 3 selectSubjectChapter eng 0", `selectSubjectChapter('eng', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab eng lesson", `switchSubjectTab('eng', 'lesson', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab eng exercise", `switchSubjectTab('eng', 'exercise', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab eng slos", `switchSubjectTab('eng', 'slos', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab eng words", `switchSubjectTab('eng', 'words', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab eng grammar", `switchSubjectTab('eng', 'grammar', 0, 'cls3')`);
run("CLASS 3 selectSubjectChapter eng 10 (Unit 11)", `selectSubjectChapter('eng', 10, 'cls3')`);

run("CLASS 3 openSubject cls3-gk", `openSubject('cls3','cls3-gk')`);
run("CLASS 3 selectSubjectChapter gk 0", `selectSubjectChapter('gk', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab gk lesson", `switchSubjectTab('gk', 'lesson', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab gk exercise", `switchSubjectTab('gk', 'exercise', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab gk slos", `switchSubjectTab('gk', 'slos', 0, 'cls3')`);
run("CLASS 3 selectSubjectChapter gk 15 (Chapter 16)", `selectSubjectChapter('gk', 15, 'cls3')`);

run("CLASS 3 openSubject cls3-pashto", `openSubject('cls3','cls3-pashto')`);
run("CLASS 3 selectSubjectChapter pashto 0", `selectSubjectChapter('pashto', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab pashto lesson", `switchSubjectTab('pashto', 'lesson', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab pashto exercise", `switchSubjectTab('pashto', 'exercise', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab pashto slos", `switchSubjectTab('pashto', 'slos', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab pashto words", `switchSubjectTab('pashto', 'words', 0, 'cls3')`);
run("CLASS 3 switchSubjectTab pashto grammar", `switchSubjectTab('pashto', 'grammar', 0, 'cls3')`);
run("CLASS 3 selectSubjectChapter pashto 32 (Lesson 33)", `selectSubjectChapter('pashto', 32, 'cls3')`);

run("CLASS 5 goToSubjects cls5", `goToSubjects('cls5'); const h5 = $('dashboard-body').innerHTML; if (!/General Science/.test(h5) || !/Social Studies/.test(h5)) throw new Error('Class 5 subjects cards missing');`);
run("CLASS 5 openSubject cls5 math", `openSubject('cls5','cls5-math'); if (getMathChapterList('cls5').length !== 9) throw new Error('Class 5 Math unit count mismatch');`);
run("CLASS 5 openSubject cls5 sci", `openSubject('cls5','cls5-sci'); selectSubjectChapter('sci', 0, 'cls5'); switchSubjectTab('sci', 'exercise', 0, 'cls5');`);
run("CLASS 5 openSubject cls5 eng", `openSubject('cls5','cls5-eng'); selectSubjectChapter('eng', 0, 'cls5'); switchSubjectTab('eng', 'exercise', 0, 'cls5');`);
run("CLASS 5 openSubject cls5 urdu", `openSubject('cls5','cls5-urdu'); selectSubjectChapter('urdu', 0, 'cls5'); switchSubjectTab('urdu', 'exercise', 0, 'cls5');`);
run("CLASS 5 openSubject cls5 isl", `openSubject('cls5','cls5-isl'); selectSubjectChapter('isl', 0, 'cls5'); switchSubjectTab('isl', 'exercise', 0, 'cls5');`);
run("CLASS 5 openSubject cls5 sst", `openSubject('cls5','cls5-sst'); selectSubjectChapter('sst', 0, 'cls5'); switchSubjectTab('sst', 'exercise', 0, 'cls5');`);
run("CLASS 5 openSubject cls5 sstum", `openSubject('cls5','cls5-sstum'); selectSubjectChapter('sstum', 0, 'cls5'); switchSubjectTab('sstum', 'exercise', 0, 'cls5');`);
run("CLASS 5 openSubject cls5 pashto", `openSubject('cls5','cls5-pashto'); selectSubjectChapter('pashto', 0, 'cls5'); switchSubjectTab('pashto', 'exercise', 0, 'cls5');`);

run("CLASS 6 goToSubjects cls6", `goToSubjects('cls6'); const h6 = $('dashboard-body').innerHTML; if (!/General Science/.test(h6) || !/Computer/.test(h6)) throw new Error('Class 6 subjects cards missing');`);
run("CLASS 6 openSubject cls6 math", `openSubject('cls6','cls6-math'); if (getMathChapterList('cls6').length !== 11) throw new Error('Class 6 Math unit count mismatch');`);
run("CLASS 6 openSubject cls6 sci", `openSubject('cls6','cls6-sci'); selectSubjectChapter('sci', 0, 'cls6'); switchSubjectTab('sci', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 eng", `openSubject('cls6','cls6-eng'); selectSubjectChapter('eng', 0, 'cls6'); switchSubjectTab('eng', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 urdu", `openSubject('cls6','cls6-urdu'); selectSubjectChapter('urdu', 0, 'cls6'); switchSubjectTab('urdu', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 isl", `openSubject('cls6','cls6-isl'); selectSubjectChapter('isl', 0, 'cls6'); switchSubjectTab('isl', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 comp", `openSubject('cls6','cls6-comp'); selectSubjectChapter('comp', 0, 'cls6'); switchSubjectTab('comp', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 geo", `openSubject('cls6','cls6-geo'); selectSubjectChapter('geo', 0, 'cls6'); switchSubjectTab('geo', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 hist", `openSubject('cls6','cls6-hist'); selectSubjectChapter('hist', 0, 'cls6'); switchSubjectTab('hist', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 hpe", `openSubject('cls6','cls6-hpe'); selectSubjectChapter('hpe', 0, 'cls6'); switchSubjectTab('hpe', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 drawing", `openSubject('cls6','cls6-drawing'); selectSubjectChapter('drawing', 0, 'cls6'); switchSubjectTab('drawing', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 arabic", `openSubject('cls6','cls6-arabic'); selectSubjectChapter('arabic', 0, 'cls6'); switchSubjectTab('arabic', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 quran", `openSubject('cls6','cls6-quran'); selectSubjectChapter('quran', 0, 'cls6'); switchSubjectTab('quran', 'exercise', 0, 'cls6');`);
run("CLASS 6 openSubject cls6 pashto", `openSubject('cls6','cls6-pashto'); selectSubjectChapter('pashto', 0, 'cls6'); switchSubjectTab('pashto', 'exercise', 0, 'cls6');`);

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
run('SOURCE REVISION Class 12 Maths opening text and unaffected lessons', `
  openSubject('cls12','cls12-math');
  switchMathTab('lesson');
  const opening = $('mathTabContent').innerHTML;
  if (!opening.includes('Leading Books Publishers') || !opening.includes('Table of Contents') || !opening.includes('By the end of this unit')) throw new Error('Reviewed opening pages missing from lesson route');
  if (!opening.includes('multi-paradigm programming language') || !opening.includes('1.1.2')) throw new Error('Reviewed lesson or following unreviewed subsection was lost');
  if (!opening.includes('Figure 1.9') || !opening.includes('1.275862069') || !opening.includes('\\\\frac{37}{29}')) throw new Error('Source commands, exact fraction, or late figure missing');
  if (opening.includes('right edge cropped in source')) throw new Error('Resolved clipping still appears in lesson');
  if (!opening.includes('1.3.2')) throw new Error('Unreviewed graphics subsections lost');
  switchMathTab('examples');
  if (!$('mathTabContent').innerHTML.includes('SpaceBook learning enhancement')) throw new Error('Added solutions are not distinguished from original textbook');
  selectMathChapter(1);
  switchMathTab('lesson');
  if ($('mathTabContent').innerHTML.includes('Leading Books Publishers')) throw new Error('Front matter repeated in unrelated unit');
`);
console.log('state after tests = activeSubject=' + vm.runInContext('state.activeSubject', sb) + ' selectedIslChapter=' + vm.runInContext('state.selectedIslChapter', sb));
console.log("smoke: " + fails + " failed");
process.exit(fails || process.exitCode ? 1 : 0);

