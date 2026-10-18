// Focused, non-browser checks for freshly reviewed Class 12 Physics records.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const root = path.resolve(__dirname, '..');
const context = {
  state: {selectedClass:'cls12'},
  sanitize: value => String(value).replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;'),
  // Unrelated class front-matter widgets are outside this Class 12 check.
  renderClass9PhysicsFrontMatter: () => '',
  renderClass10PhysicsFrontMatter: () => '',
  renderClass10PhysicsWorkedExamples: () => '',
  renderClass9PhysicsWorkedExamples: () => '',
};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root, 'assets/vendor/katex/katex.min.js'), 'utf8'), context);
vm.runInContext(fs.readFileSync(path.join(root, 'js/phys_12_data.js'), 'utf8')
  + ';globalThis.ch = PHYS_12_DATA[0];globalThis.allPhysicsChapters=PHYS_12_DATA;', context);
const app = fs.readFileSync(path.join(root, 'js/app.js'), 'utf8');
for (const name of ['splitSentenceText', 'renderInteractiveParagraphHtml',
  'getScienceSectionParagraphsWithTranslations', 'renderScienceSourceLayout', 'renderScienceLessonSubContent']) {
  const source = app.match(new RegExp('function ' + name + '\\([^]*?\\n\\}'));
  assert(source, name);
  vm.runInContext(source[0], context);
}
vm.runInContext(fs.readFileSync(path.join(root, 'js/lesson_math_reader.js'), 'utf8'), context);
const progress = JSON.parse(fs.readFileSync(path.join(root, 'docs/source-verification/class-12/progress.json'), 'utf8'));
const ids = progress.pages.flatMap(page => page.recordIds);
let count = 0;
for (const id of ids) {
  const chapter = context.allPhysicsChapters.find(item => item.sections.some(section => section.id === id));
  assert(chapter, id + ' assigned to a physics unit');
  const matches = chapter.sections.filter(section => section.id === id);
  assert.equal(matches.length, 1, id + ' unique active section');
  const section = matches[0];
  const topic = chapter.topics.find(item => item.id === id);
  assert.equal(JSON.stringify(section), JSON.stringify(topic), id + ' topic synchronized');
  const paras = context.getScienceSectionParagraphsWithTranslations(section, chapter, 'phys');
  const indices = section.sourceLayout.flatMap(block => block.indices || []).sort((a, b) => a - b);
  assert.equal(JSON.stringify(indices), JSON.stringify(paras.map((_, index) => index)), id + ' every paragraph once');
  assert(!/<img\b|<image\b|data:image|\.png|\.jpg|\.webp/i.test(section.content + section.diagramSvg), id + ' no source raster');
  for (const paragraph of paras) {
    assert(paragraph.text && paragraph.urdu && paragraph.pashto, id + ' aligned translations');
    assert(!/<\/?(?:p|b|strong|svg|figure)\b/.test(paragraph.text), id + ' plain prose');
    count++;
  }
  const output = context.renderScienceSourceLayout(section, paras, 'en', ids.indexOf(id), chapter);
  assert(!/&lt;\/?(?:p|b|strong|svg|figure)\b/.test(output), id + ' markup not exposed');
  if (section.paras.some(para => /\\\(/.test(para.text))) {
    for (const lang of ['en', 'ur', 'ps']) {
      const html = context.renderScienceSourceLayout(section, paras, lang, ids.indexOf(id), chapter);
      assert(html.includes('class="katex"'), id + ' formatted equation in ' + lang);
      assert(!html.includes('katex-error'), id + ' valid equation in ' + lang);
      assert(!html.includes('SPACEBOOKPHYSICS'), id + ' no leaked equation token');
    }
  }
}
const quote = context.ch.sections.find(section => section.id === 'phys12-front-quotation');
assert.equal(quote.paras[0].originalLanguage, 'ur');
assert.equal(quote.paras[0].originalText, quote.paras[0].urdu);
assert(/[A-Za-z]/.test(quote.paras[0].english));
// Render only the reviewed records: unreviewed legacy prose is outside the audit.
const reviewedChapter = {...context.ch, sections: context.ch.sections.filter(section => ids.includes(section.id))};
const output = context.renderScienceLessonSubContent('phys', reviewedChapter, 'translations');
assert(output.includes(quote.sourceOriginalLabel));
assert(output.includes(quote.sourceUrduLabel));
const svgIds = [...output.matchAll(/\bid="(phys12[^"]+)"/g)].map(match => match[1]);
assert.equal(new Set(svgIds).size, svgIds.length, 'Unique SVG IDs in simultaneous language panels');
for (const chapter of context.allPhysicsChapters) {
  const localIds=ids.filter(id=>chapter.sections.some(section=>section.id===id));
  if (!localIds.length || chapter.num===11) continue;
  const reviewed={...chapter,sections:chapter.sections.filter(section=>localIds.includes(section.id))};
  const translated=context.renderScienceLessonSubContent('phys',reviewed,'translations');
  assert(!translated.includes('katex-error'),`Unit ${chapter.num} translation panels format equations`);
  assert(!/<img\b|<image\b/.test(translated),`Unit ${chapter.num} reviewed sections contain no source raster`);
}
const summary = app.match(/function renderScienceOrHumanitiesSummaryTab\([^]*?\n\}/);
assert(summary);
const sourceFormulas=app.match(/function renderClass12PhysicsSourceFormulas\([^]*?\n\}/);
assert(sourceFormulas);
vm.runInContext(sourceFormulas[0],context);
vm.runInContext(summary[0],context);
const summaryHtml=context.renderScienceOrHumanitiesSummaryTab('phys',context.ch);
assert(summaryHtml.includes('class="katex"'),'Audited formula cards formatted');
assert(!summaryHtml.includes('katex-error'),'Formula cards contain valid notation');
assert.equal(new Set(context.ch.formulas.map(item=>item.id)).size,context.ch.formulas.length,'Formula cards have stable unique IDs');
const definitions=app.match(/function renderScienceConceptsTab\([^]*?\n\}/);
assert(definitions);
const examples=app.match(/function renderClass12PhysicsWorkedExamples\([^]*?\n\}/);
assert(examples);
vm.runInContext(examples[0],context);
vm.runInContext(definitions[0],context);
const definitionHtml=context.renderScienceConceptsTab('phys',context.ch);
assert(definitionHtml.includes('class="katex"'),'Definition notation formatted');
assert(!definitionHtml.includes('katex-error'),'Definition notation valid');
assert.equal((definitionHtml.match(/class="physics-source-worked-example"/g)||[]).length,6,'Six reviewed worked examples accessible through concepts');
const lessons=app.match(/function renderScienceOrHumanitiesLessons\([^]*?\n\}/);
assert(lessons);
vm.runInContext(lessons[0],context);
const lessonHtml=context.renderScienceOrHumanitiesLessons('phys',{...context.ch,topics:reviewedChapter.sections});
assert(lessonHtml.includes('class="katex"'),'Main lesson equations formatted');
assert(!/<img\b|<image\b/.test(lessonHtml),'Main reviewed lessons contain coded visuals');
for (const chapter of context.allPhysicsChapters) {
  const localIds=ids.filter(id=>chapter.sections.some(section=>section.id===id));
  if (!localIds.length || chapter.num===11) continue;
  const selected={...chapter,topics:chapter.sections.filter(section=>localIds.includes(section.id))};
  const unitLessons=context.renderScienceOrHumanitiesLessons('phys',selected);
  assert(!unitLessons.includes('katex-error'),`Unit ${chapter.num} lesson equations render`);
  assert(!/<img\b|<image\b/.test(unitLessons),`Unit ${chapter.num} reviewed lessons contain no source raster`);
}
const exerciseHelper=app.match(/function renderClass12PhysicsSourceExercises\([^]*?\n\}/);
assert(exerciseHelper);
vm.runInContext(exerciseHelper[0],context);
const exerciseHtml=context.renderClass12PhysicsSourceExercises(context.ch);
assert.equal((exerciseHtml.match(/class="physics-source-exercise"/g)||[]).length,5,'Three reviewed assignments, quiz and project accessible');
assert(exerciseHtml.includes('What are the basic differences between laser printer and photocopier?'),'Source quiz question included');
assert(exerciseHtml.includes('class="katex"'),'Assignment notation formatted');
assert(!exerciseHtml.includes('katex-error'),'Assignment notation valid');
const fidelityPath = path.join(root, 'docs/source-verification/class-12/physics-fidelity-review.json');
if (fs.existsSync(fidelityPath)) {
  const fidelity = JSON.parse(fs.readFileSync(fidelityPath, 'utf8'));
  for (const [page, pageReference] of Object.entries(fidelity.pages)) for (const reference of [pageReference,...(pageReference.additionalRecords || [])]) {
    const chapter = context.allPhysicsChapters.find(ch => ch.sections.some(sec => sec.id === reference.recordId));
    const section = chapter.sections.find(sec => sec.id === reference.recordId);
    assert.deepEqual(JSON.parse(JSON.stringify(section.paras.map(p => p.originalText))), reference.paragraphs, `PDF${page}: saved source transcription agrees with active original text`);
    assert.deepEqual(JSON.parse(JSON.stringify(section.paras.map(p => p.text))), reference.paragraphs, `PDF${page}: lesson text agrees with source transcription`);
    assert(section.sourceClass12Physics, `PDF${page}: source-renderer opt-in`);
    const figures = section.sourceBlocks.filter(block => block.type === 'figure');
    const paras = context.getScienceSectionParagraphsWithTranslations(section, chapter, 'phys');
    for (const lang of ['en','ur','ps']) {
      const rendered = context.renderScienceSourceLayout(section, paras, lang, `fidelity-${page}`);
      assert.equal((rendered.match(/<svg\b[^>]*\brole="img"/g)||[]).length, figures.length, `PDF${page}: every labelled source figure renders in ${lang}, excluding equation glyphs`);
      for (const figure of figures) {
        const markup = lang === 'en' ? figure.svg : lang === 'ur' ? figure.svgUrdu : figure.svgPashto;
        const label = markup.match(/aria-label="[^"]*"/);
        assert(label && rendered.includes(label[0]), `PDF${page}: source figure ${figure.id} and its ${lang} description reach the lesson`);
      }
      assert(!/<img\b|<image\b|data:image|katex-error|SPACEBOOKPHYSICS/.test(rendered), `PDF${page}: clean source output in ${lang}`);
      if (reference.paragraphs.some(text => text.includes('\\('))) assert(rendered.includes('class="katex"'), `PDF${page}: notation formatted in ${lang}`);
    }
    const sourceHtml = context.renderScienceSourceLayout(section, paras, 'en', `fidelity-original-${page}`);
    for (const paragraph of section.paras.filter(p=>p.sourceLanguage==='ur')) {
      assert.equal(paragraph.text, paragraph.originalText, `PDF${page}: Urdu original remains visible`);
      assert.equal(paragraph.urdu, paragraph.originalText, `PDF${page}: Urdu field preserves original`);
      assert(sourceHtml.includes('data-en="'+context.sanitize(paragraph.english)+'"'), `PDF${page}: English meaning available for the Urdu source`);
      assert(sourceHtml.includes('dir="rtl"'), `PDF${page}: Urdu original reads right to left`);
    }
    const mainLesson = context.renderScienceOrHumanitiesLessons('phys', {...chapter,topics:[section]});
    assert.equal((mainLesson.match(/<svg\b[^>]*\brole="img"/g)||[]).length, figures.length, `PDF${page}: labelled source figures reach main lessons`);
    assert(mainLesson.includes('data-ur='), `PDF${page}: interactive aligned translations reach main lessons`);
    for (const sourceExercise of chapter.exercises.filter(item => item.sourceSectionId === section.id)) {
      const exercisesHtml = context.renderClass12PhysicsSourceExercises({...chapter,exercises:[sourceExercise]});
      assert(exercisesHtml.includes('data-ur='), `PDF${page}: exercise tab uses paired source paragraphs`);
      assert(!exercisesHtml.includes('katex-error'), `PDF${page}: exercise notation valid`);
      for (const index of sourceExercise.sourceIndices) {
        assert(exercisesHtml.includes('data-ur="'+context.sanitize(section.paras[index].urdu)+'"'), `PDF${page}: source paragraph${index} retains its complete paired translation in the exercise view`);
      }
    }
    for (const example of chapter.workedExamples.filter(item => item.sourceSectionId === section.id || item.sourceParts?.some(part => part.sectionId === section.id))) {
      const examplesHtml = context.renderClass12PhysicsWorkedExamples({...chapter,workedExamples:[example]});
      const sourceIndices = example.sourceParts?.find(part => part.sectionId === section.id)?.indices || example.sourceIndices;
      for (const index of sourceIndices) {
        const translations = section.sourceTableRows?.[index] ? section.paras[index].urdu.split(' — ') : [section.paras[index].urdu];
        for (const translation of translations.filter(Boolean)) assert(examplesHtml.includes('data-ur="'+context.sanitize(translation)+'"'), `PDF${page}: complete worked-example source step${index}, including each table cell, reaches concepts`);
      }
      assert(!examplesHtml.includes('katex-error'), `PDF${page}: worked-example notation valid`);
    }
  }
}
console.log(`PASS: ${ids.length} records; ${count} aligned paragraphs; structural checks and saved fidelity-reference comparisons passed. This check does not certify unreviewed source text.`);
