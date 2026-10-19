'use strict';
/* Content integrity in the app code (Phase 6): answer keys, placeholder media, generated practice. Runs in the app sandbox.
 *   node --max-old-space-size=8192 tests/content/integrity.js        exits 1 on any failure */
const { load } = require('../../tools/lib/app_sandbox');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

const app = load({ page: 'lazy.html', quiet: true });
const run = c => app.run(c, 120000);
const J = c => JSON.parse(run('JSON.stringify(' + c + ')'));

// ---- sbMcqKey: the one place that decides which option is the key
check('correct: 2 is option C', J("sbMcqKey({ options: ['a','b','c','d'], correct: 2 })") === 2);
check('correctIndex wins over the others', J("sbMcqKey({ options: ['a','b','c','d'], correctIndex: 3, correct: 1, ans: 0 })") === 3);
check('ans: 1', J("sbMcqKey({ options: ['a','b','c','d'], ans: 1 })") === 1);
check('a letter works, either case', J("[sbMcqKey({ options: ['a','b','c','d'], answer: 'b' }), sbMcqKey({ options: ['a','b','c','d'], answer: 'D' })]").join() === '1,3');
check('the answer given as the option text works', J("sbMcqKey({ options: ['x','y','z','w'], answer: 'z' })") === 2);
check('a numeric string works', J("sbMcqKey({ options: ['a','b','c','d'], correct: '2' })") === 2);
check('no key gives null, never option A', J("sbMcqKey({ options: ['a','b','c','d'], q: 'Q' })") === null);
check('a key outside the options gives null', J("sbMcqKey({ options: ['a','b'], correct: 3 })") === null);
check('nonsense gives null', J("[sbMcqKey(null), sbMcqKey(undefined), sbMcqKey('x'), sbMcqKey({ correct: -1, options: ['a','b'] })]").every(v => v === null));
check('index 0 is a real key', J("sbMcqKey({ options: ['a','b','c','d'], correct: 0 })") === 0);

// ---- Papers reads the key the item has: Class 2 Urdu / Class 9 Islamiat were 100 % option A
const dist = id => { const cls = id.split('-')[0]; const list = J(`getCurriculumQuestionsForCategory('${cls}', '${id}', 'mcqs').map(q => q.ans)`); const d = [0, 0, 0, 0]; list.forEach(a => { if (a !== null) d[a]++; }); return { n: list.length, d }; };
for (const id of ['cls2-urdu', 'cls9-isl', 'cls10-chem', 'cls9-pakstudy']) {
  const r = dist(id), top = Math.max(...r.d) / Math.max(1, r.d.reduce((a, b) => a + b, 0));
  check(id + ': the paper pool keeps the keys of its source (not 100 % A)', r.n > 0 && top < 0.95, JSON.stringify(r));
}
// every question the pool returns with a key has it inside its options; a question with no key has null
{
  const bad = J("(() => { const out = []; for (const [c, id] of [['cls9','cls9-isl'], ['cls2','cls2-urdu'], ['cls10','cls10-eng'], ['cls6','cls6-comp']]) for (const q of getCurriculumQuestionsForCategory(c, id, 'mcqs')) if (q.ans !== null && !(Number.isInteger(q.ans) && q.ans >= 0 && q.ans < (q.opts || []).length)) out.push(id + ':' + q.ans); return out; })()");
  check('no paper MCQ has a key outside its options', bad.length === 0, bad.slice(0, 5).join(','));
}

// ---- the paper prints "key not available" for a missing key and never invents A
{
  const src = require('fs').readFileSync(require('path').join(__dirname, '..', '..', 'js', 'app.js'), 'utf8');
  check('the paper key note handles a missing key', /m\.ans == null \? '💡 Key not available/.test(src));
  check('the OMR sheet does not fill a bubble without a key', /m && m\.ans != null \? m\.ans : -1/.test(src));
  check('no paper collector defaults a missing key to option A', !/ans: [^\n]*\|\| 0,/.test(src.slice(src.indexOf('function getCurriculumQuestionsForCategory'), src.indexOf('function getCurriculumQuestionsForCategory') + 40000)));
}

// ---- placeholder media
{
  const html = run(`renderIslVideo({ title: 'Surah', video: { title: 'Class 9 Islamyat', url: 'https://www.youtube.com/embed/dQw4w9WgXcQ', duration: '24:15', instructor: 'KPK Board Islamic Studies Specialist' } })`);
  check('the placeholder video id is not embedded', !/<iframe/.test(html) && !/dQw4w9WgXcQ/.test(html) && /no video lecture/i.test(html));
  const none = run(`renderIslVideo({ title: 'Surah' })`);
  check('a chapter with no video says so (no iframe, no invented lecture)', !/<iframe/.test(none) && /no video lecture/i.test(none));
  const real = run(`renderIslVideo({ title: 'Surah', video: { title: 'Real lecture', url: 'https://www.youtube-nocookie.com/embed/abc123XYZ_-', duration: '10:00', instructor: 'A. Teacher' } })`);
  check('a real embed still renders', /<iframe src="https:\/\/www\.youtube-nocookie\.com\/embed\/abc123XYZ_-"/.test(real) && /Real lecture/.test(real));
  const topic = run(`renderMathTopicSubContent({ id: '1.2', title: 'T' }, { number: 1, title: 'U', sections: [{ id: '1.2', title: 'T' }] }, 'video', 0)`);
  check('the Maths topic video tab has no fake player', !/1080p|Click to Play|18:45/.test(topic) && /no video lecture/i.test(topic));
  const src = require('fs').readFileSync(require('path').join(__dirname, '..', '..', 'js', 'app.js'), 'utf8');
  check('the Maths topic tab bar no longer offers a Video tab', !/data-subtab="video"/.test(src));
}

// ---- generated practice: visible until the owner approves, gone with the flag, authored items untouched
{
  const base = J(`(() => { const u = getMathChapterList('cls9')[0]; const a = getTopicSpecificSLOs(u.sections[0], u), b = getTopicSpecificSLOs(u.sections[1], u); return { authored: a.mcqs.length, authoredGenerated: a.mcqs.filter(x => x.generated).length, second: b.mcqs.length, secondGenerated: b.mcqs.filter(x => x.generated).length }; })()`);
  check('section 1.1 is authored (4 MCQs, none marked generated)', base.authored === 4 && base.authoredGenerated === 0, JSON.stringify(base));
  check('other sections are marked generated and still shown by default', base.second > 0 && base.secondGenerated === base.second, JSON.stringify(base));
  run(`window.SB_FLAGS = { hideGeneratedSlo: true }`);
  const hidden = J(`(() => { const u = getMathChapterList('cls9')[0]; const a = getTopicSpecificSLOs(u.sections[0], u), b = getTopicSpecificSLOs(u.sections[1], u); return { a: a.mcqs.length, b: b.mcqs.length + b.shortQuestions.length + b.longQuestions.length }; })()`);
  check('with the flag, generated items are gone and the authored ones stay', hidden.a === 4 && hidden.b === 0, JSON.stringify(hidden));
  const note = run(`renderTopicSloInnerContent(getMathChapterList('cls9')[0].sections[1], getMathChapterList('cls9')[0], 'mcqs')`);
  check('with the flag, the tab says practice is being prepared', /being prepared/.test(note));
  const pool = J(`getCurriculumQuestionsForCategory('cls9', 'cls9-math', 'mcqs').length`);
  run(`window.SB_FLAGS = {}`);
  const pool0 = J(`getCurriculumQuestionsForCategory('cls9', 'cls9-math', 'mcqs').length`);
  check('with the flag, Papers no longer offers generated Maths MCQs', pool < pool0, pool + ' vs ' + pool0);
}

// ---- the paper pool: no fabricated key, generated items marked
{
  const keys = J("(() => { const out = { revNull: 0, revOther: 0 }; for (const [c, id] of [['cls8','cls8-math'], ['cls10','cls10-math'], ['cls7','cls7-math']]) for (const q of getCurriculumQuestionsForCategory(c, id, 'mcqs')) if (q.exp && /Textbook Review Exercise/.test(q.exp)) { if (q.ans === null) out.revNull++; else out.revOther++; } return out; })()");
  check('review-exercise MCQs parsed from text have no key (null), never A', keys.revOther === 0, JSON.stringify(keys));
  const eng = J("(() => { const l = getCurriculumQuestionsForCategory('cls9', 'cls9-eng', 'mcqs'); return { n: l.length, gen: l.filter(q => q.generated).length }; })()");
  check('the one-template-per-unit English thematic MCQs are marked generated', eng.gen > 0, JSON.stringify(eng));
  run('window.SB_FLAGS = { hideGeneratedSlo: true }');
  const eng2 = J("getCurriculumQuestionsForCategory('cls9', 'cls9-eng', 'mcqs').length");
  run('window.SB_FLAGS = {}');
  check('the owner switch removes them from the paper pool', eng2 === eng.n - eng.gen, eng2 + ' vs ' + (eng.n - eng.gen));
}

// ---- PDFs: no button that leads nowhere
{
  check('sbPdf gives nothing for a path that is not packaged', run("[sbPdf('assets/books/Class-9-Biology-KPK.pdf'), sbPdf('file:///D:/x.pdf'), sbPdf(null)].join('|')") === '||');
  const html = run(`(() => { state.selectedClass = 'cls9'; openSubject('cls9', 'cls9-bio'); return document.getElementById('dashboard-body').innerHTML + (document.getElementById('dash-sub') ? document.getElementById('dash-sub').innerHTML : ''); })()`);
  check('a Class 9 subject page offers no PDF link', !/\.pdf/.test(html), (html.match(/[^"']*\.pdf/) || [''])[0]);
  const lib = run(`(() => { renderBooksView('cls9'); return document.getElementById('dashboard-body').innerHTML + (document.getElementById('page-content') ? document.getElementById('page-content').innerHTML : ''); })()`);
  check('the books library offers no dead PDF button (Read Online / Download)', !/Read Online|Download \(/.test(lib) && !/High-Resolution PDF/.test(lib));
  const all = J(`DATA.classes.map(c => { const l = DATA.subjects[c.id] || []; if (l[0]) openSubject(c.id, l[0].id); return document.getElementById('dashboard-body').innerHTML + (document.getElementById('page-content') ? document.getElementById('page-content').innerHTML : ''); }).filter(h => /href=.[^'" ]*[.]pdf/.test(h)).length`);
  check('no first subject of any class links to a PDF', all === 0, String(all));
}

console.log(`content integrity tests: ${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
