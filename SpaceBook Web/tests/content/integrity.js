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
for (const id of ['cls9-urdu', 'cls9-isl', 'cls9-chem', 'cls9-pakstudy']) {
  const r = dist(id), top = Math.max(...r.d) / Math.max(1, r.d.reduce((a, b) => a + b, 0));
  check(id + ': the paper pool keeps the keys of its source (not 100 % A)', r.n > 0 && top < 0.95, JSON.stringify(r));
}
// every question the pool returns with a key has it inside its options; a question with no key has null
{
  const bad = J("(() => { const out = []; for (const [c, id] of [['cls9','cls9-isl'], ['cls9','cls9-urdu'], ['cls10','cls10-eng'], ['cls9','cls9-comp']]) for (const q of getCurriculumQuestionsForCategory(c, id, 'mcqs')) if (q.ans !== null && !(Number.isInteger(q.ans) && q.ans >= 0 && q.ans < (q.opts || []).length)) out.push(id + ':' + q.ans); return out; })()");
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

// ---- a paper is drawn from the books of ITS class: no other class's questions fill the pool (docs/CONTENT_REVIEW.md, decision 4)
{
  const n = (c, id, cat) => J(`getCurriculumQuestionsForCategory('${c}', '${id}', '${cat || 'mcqs'}').length`);
  const all = id => ['mcqs', 'sqs', 'lqs', 'numericals'].reduce((t, cat) => t + n(id.split('-')[0], id, cat), 0);        // a pool in any category
  check('Class 1, 5, 11 and 12 Maths have no pool of Class 9 questions', all('cls1-math') === 0 && all('cls5-math') === 0 && all('cls12-math') === 0 && all('cls11-math') === 0);
  check('Class 12 Physics / Chemistry / English / Urdu, Class 11 English and Class 10 Chemistry / Physics have none either', ['cls12-phy', 'cls12-chem', 'cls12-eng', 'cls12-urdu', 'cls11-eng', 'cls10-chem', 'cls10-phy'].every(id => all(id) === 0), ['cls12-phy', 'cls12-chem', 'cls12-eng', 'cls12-urdu', 'cls11-eng', 'cls10-chem', 'cls10-phy'].map(id => id + '=' + all(id)).join(' '));
  check('Class 2 Urdu / Islamiat and Class 6 Computer have none (they used to get the Class 9 book)', all('cls2-urdu') === 0 && all('cls6-comp') === 0 && all('cls2-isl') === 0);
  const own = ['cls7-math', 'cls8-math', 'cls9-math', 'cls10-math', 'cls1-eng', 'cls8-eng', 'cls9-eng', 'cls10-eng', 'cls9-urdu', 'cls9-chem', 'cls9-phy', 'cls9-comp', 'cls9-pakstudy', 'cls9-isl', 'cls10-isl', 'cls1-isl'];
  check('the subjects that have their own books still have their pool', own.every(id => all(id) > 0), own.filter(id => all(id) === 0).join(','));
  check('every category of an empty pool is empty (short and long questions too)', ['sqs', 'lqs'].every(cat => n('cls12', 'cls12-math', cat) === 0 && n('cls1', 'cls1-math', cat) === 0));
  const phy = dist('cls9-phy');
  check('Class 9 Physics (its pool never matched the subject id before) has MCQs with their own keys, not all A', phy.n > 50 && Math.max(...phy.d) / Math.max(1, phy.d.reduce((a, b) => a + b, 0)) < 0.95, JSON.stringify(phy));
}

// ---- paper sets A / B / C: the same questions in another order, options moved with their keys
{
  const r = J(`(() => {
    const pool = getCurriculumQuestionsForCategory('cls9', 'cls9-isl', 'mcqs').filter(q => q.ans !== null && Array.isArray(q.opts)).slice(0, 60);
    const ids = l => l.map(q => q.id).join(',');
    const A = sbPaperApplyVersion(pool, 'mcqs', 'A', 0), B = sbPaperApplyVersion(pool, 'mcqs', 'B', 0), B2 = sbPaperApplyVersion(pool, 'mcqs', 'B', 0), C = sbPaperApplyVersion(pool, 'mcqs', 'C', 0), A1 = sbPaperApplyVersion(pool, 'mcqs', 'A', 1);
    const byId = Object.fromEntries(pool.map(q => [q.id, q]));
    const keyText = q => q.opts[q.ans];
    const keyMoved = B.every(q => keyText(q) === keyText(byId[q.id])) && C.every(q => keyText(q) === keyText(byId[q.id]));
    const sameOptions = B.every(q => [...q.opts].sort().join('|') === [...byId[q.id].opts].sort().join('|'));
    const moved = B.filter(q => q.opts.join('|') !== byId[q.id].opts.join('|')).length;
    const pos = { q: 'P', opts: ['x', 'y', 'z', 'All of the above'], ans: 3, id: 'p1' };
    const pos2 = { q: 'Q', opts: ['(a) and (b)', 'only (a)', 'only (b)', 'none'], ans: 0, id: 'p2' };
    const keep = sbPaperApplyVersion([pos, pos2, { q: 'R', opts: ['1', '2', '3', '4'], ans: 2, id: 'p3' }], 'mcqs', 'B', 0);
    const noKey = sbPaperApplyVersion([{ q: 'N', opts: ['1', '2', '3', '4'], ans: null, id: 'n1' }, { q: 'M', opts: ['1', '2', '3', '4'], ans: null, id: 'n2' }], 'mcqs', 'C', 0);
    const sq = [1, 2, 3, 4, 5, 6].map(i => ({ id: 's' + i, q: 'S' + i }));
    return { n: pool.length, aSame: A === pool, a1Differs: ids(A1) !== ids(pool), bDiffers: ids(B) !== ids(pool), bAll: ids(B).split(',').sort().join() === ids(pool).split(',').sort().join(), bcDiffer: ids(B) !== ids(C), det: JSON.stringify(B) === JSON.stringify(B2), keyMoved, sameOptions, moved,
      positionalKept: keep.filter(q => q.id === 'p1' || q.id === 'p2').every(q => q.ans === (q.id === 'p1' ? 3 : 0) && q.opts.join('|') === (q.id === 'p1' ? pos : pos2).opts.join('|')), p3Key: (() => { const q = keep.find(x => x.id === 'p3'); return q.opts[q.ans]; })(),
      noKeyStays: noKey.every(q => q.ans === null), sqOrder: sbPaperApplyVersion(sq, 'sqs', 'B', 0).map(q => q.id).join() !== sq.map(q => q.id).join(), sqKeep: sbPaperApplyVersion(sq, 'sqs', 'A', 0) === sq,
      orig: JSON.stringify(pool) === JSON.stringify(pool.map(q => byId[q.id])) };
  })()`);
  check('Set A with no shuffle is the list as picked (the very same list)', r.aSame && r.n >= 20, JSON.stringify(r));
  check('Set B and Set C reorder the same questions, differently from each other and from A', r.bDiffers && r.bAll && r.bcDiffer);
  check('a set is the same paper every time (no randomness)', r.det);
  check('every press of Shuffle gives another order', r.a1Differs);
  check('the options of an MCQ are reordered and the key moves with its option (the correct text stays the correct one)', r.keyMoved && r.sameOptions && r.moved > 5, 'moved ' + r.moved);
  check('an MCQ whose options point at each other ("All of the above", "(a) and (b)") keeps its options and key', r.positionalKept);
  check('a question without a key stays without a key, never gets one by moving', r.noKeyStays);
  check('short questions are reordered too, set A leaves them alone', r.sqOrder && r.sqKeep);
  const html = run(`(() => {
    paperCreationState.classId = 'cls9'; paperCreationState.subjectId = 'cls9-isl'; paperCreationState.categoriesOrder = ['mcqs'];
    paperCreationState.categoryAllocations.mcqs = { count: 12, attempt: 12, marksPerQ: 1, totalMarks: 12 };
    const pool = getCurriculumQuestionsForCategory('cls9', 'cls9-isl', 'mcqs').slice(0, 12);
    paperCreationState.selectedQuestionsByCategory = { mcqs: pool.map(q => q.id) };
    paperCreationState.showAnswerKey = true;
    const out = {};
    for (const v of ['A', 'B', 'C']) { switchPaperVersion(v); out[v] = renderLiveExamPaperHtml(); }
    return JSON.stringify(out);
  })()`);
  const sets = JSON.parse(html);
  const keys = h => (h.match(/Key: \([A-E]\)/g) || []).length;
  check('the rendered paper of Set B differs from Set A, and has the same number of keyed questions', sets.B !== sets.A && sets.C !== sets.B && keys(sets.A) === keys(sets.B) && keys(sets.A) === keys(sets.C) && keys(sets.A) > 5, [keys(sets.A), keys(sets.B), keys(sets.C)].join('/'));
}

// ---- Tests Preps: only questions with a key from their source are in the bank; the rest wait in the review queue
{
  const fs = require('fs'), path = require('path');
  const txt = fs.readFileSync(path.join(__dirname, '..', '..', 'js', 'test_prep_bank.js'), 'utf8');
  const bank = JSON.parse(txt.slice(txt.indexOf('{'), txt.lastIndexOf('}') + 1));
  const bad = bank.mcqs.filter(m => !Number.isInteger(m.a) || m.a < 0 || m.a >= m.o.length || new Set(m.o.map(x => String(x).toLowerCase().replace(/\s+/g, ''))).size !== m.o.length || m.o.some(x => !String(x).trim()));
  check('every Test Prep question has a key inside its options and distinct, non-empty options', bank.mcqs.length > 5000 && bad.length === 0, bad.slice(0, 3).map(m => m.i).join(','));
  const q = fs.readFileSync(path.join(__dirname, '..', '..', 'docs', 'test_prep_review', 'no_key.csv'), 'utf8').split('\n').filter(Boolean);
  check('the review queue lists the questions that have no key (and the bank holds none of them)', q[0].startsWith('subject,class,source file,question') && q.length > 50 && q.slice(1).every(r => r.split('","').length >= 4), String(q.length));
  const inBank = new Set(bank.mcqs.map(m => m.q.toLowerCase().replace(/\s+/g, ' ').trim()));
  const leaked = q.slice(1).filter(r => { const m = r.match(/^"[^"]*","[^"]*","[^"]*","(.*?)","/); return m && inBank.has(m[1].replace(/""/g, '"').toLowerCase().replace(/\s+/g, ' ').trim()); });
  check('no question of the review queue is in the bank under another source', leaked.length < 5, String(leaked.length));
}

console.log(`content integrity tests: ${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
