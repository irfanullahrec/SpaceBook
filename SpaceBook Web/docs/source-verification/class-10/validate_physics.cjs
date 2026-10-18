const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const path = require('path');
const root = path.resolve(__dirname, '../../..');
const dataFile = path.join(root, 'js/physics_10_source_data.js');
const originalChapter = {num: 10, sections: [{code: 'legacy', text: 'retained'}],topics:[{num:'10.1',title:'legacy',summary:{en:'legacy'}}]};
const context = {DATA: {phys10Chapters: [originalChapter, {num: 11}], physChapters: [{num: 1, untouched: true}]}};
vm.createContext(context);
vm.runInContext(fs.readFileSync(dataFile, 'utf8'), context);
const snapshot = JSON.stringify(context.DATA);
vm.runInContext(fs.readFileSync(dataFile, 'utf8'), context);
assert.equal(JSON.stringify(context.DATA), snapshot, 'Repeated loads must not duplicate pages');
assert.equal(originalChapter.sections[0].text, 'retained');
assert.equal(JSON.stringify(context.DATA.physChapters), '[{"num":1,"untouched":true}]');
assert.equal(JSON.stringify(context.DATA.phys10Chapters[1]), '{"num":11}');
const pages = originalChapter.sourceFrontMatter;
assert.equal(new Set(pages.map(p => p.id)).size, pages.length);
for (const [i, page] of pages.entries()) {
  assert.equal(page.source.pdfPage, i + 1);
  if (page.table) for (const row of page.table.rows) {
    assert.equal(row.en.length, 3);
    assert.equal(row.ur.length, 3);
    assert.equal(row.ps.length, 3);
    assert.equal(row.en[2], row.ur[2]);
    assert.equal(row.en[2], row.ps[2]);
  }
  for (const para of page.paras) {
    assert(para.text && para.urdu && para.pashto, 'All paragraphs must have three aligned language fields');
    assert(!/<(?:p|img|svg|image)\b|data:image|\.png|\.jpg/i.test(para.text));
    assert.notEqual(para.text, para.urdu);
    assert.notEqual(para.text, para.pashto);
  }
}
const app = fs.readFileSync(path.join(root, 'js/app.js'), 'utf8');
const start = app.indexOf('function renderClass10PhysicsFrontMatter(');
const end = app.indexOf('function renderScienceLessonSubContent(', start);
assert(start !== -1 && end > start);
const escape = text => String(text).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
context.sanitize = escape;
context.state = {selectedClass:'cls10'};
context.renderInteractiveParagraphHtml = (text, urdu, pashto, id, aligned) => {
  assert(urdu && pashto && aligned);
  return `<span id="${id}">${escape(text)}</span>`;
};
vm.runInContext(app.slice(start, end), context);
const output = context.renderClass10PhysicsFrontMatter(originalChapter);
assert(output.includes('Academic Year 2025-26'));
assert(output.includes('dir="rtl" lang="ur"'));
assert(output.includes('dir="rtl" lang="ps"'));
assert.equal(originalChapter.slos.length,13);
assert(output.includes('<msqrt><mfrac>'));
assert(output.includes('phys10-shock-title'));
assert(output.includes('<ul>'));
assert(output.includes('data-en="solve problems by using the formula'));
const sectionOutput = context.renderPhysics10SourceSection(originalChapter.topics[0],'en',0);
assert(sectionOutput.includes('(10.1)'));
assert(sectionOutput.includes('<strong>A. Cycle/Vibration:</strong>'));
assert(sectionOutput.includes('s⁻¹'));
assert(!sectionOutput.includes('legacy'));
assert(output.includes('Many objects vibrate or oscillate-an object'));
assert.equal(originalChapter.workedExamples.length,6);
assert.equal(originalChapter.sourceAssignments.length,6);
assert.equal(originalChapter.workedExamples[0].answerOrigin,'textbook');
assert(!Object.hasOwn(originalChapter.sourceAssignments[0],'answer'));
assert(sectionOutput.includes('Figure 10.1 - Terminologies of Oscillatory Motion'));
assert(sectionOutput.includes('EXAMPLE 10.1: FREQUENCY OF OSCILLATION'));
assert(sectionOutput.includes('0.5 Hz'));
assert(sectionOutput.indexOf('phys10-motion-caption') < sectionOutput.indexOf('E. Displacement:'));
assert(sectionOutput.includes('x₀'));
assert(context.renderClass10PhysicsWorkedExamples(originalChapter).includes('<mfrac>'));
assert(!/<img\b|<image\b|<iframe\b|data:image/i.test(output));
context.state.selectedClass = 'cls9';
assert.equal(context.renderClass10PhysicsFrontMatter(originalChapter), '');
const index = fs.readFileSync(path.join(root,'index.html'),'utf8');
assert(index.indexOf('js/data_phys.js') < index.indexOf('js/physics_10_source_data.js'));
assert(index.indexOf('js/physics_10_source_data.js') < index.indexOf('js/app.js'));
console.log(`Passed: ${pages.length} sequential front-matter pages; paired translations, stable IDs, idempotent loading, class scope, renderer output, no raster content, script order.`);
