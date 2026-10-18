'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const crypto = require('crypto');
const root = path.resolve(__dirname, '..');
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8');
const context = {};
vm.createContext(context);
vm.runInContext(read('js/math_12_data.js') + ';globalThis.data = MATH_12_DATA;', context);
const all = () => context.data.flatMap(chapter => (chapter.exercises || []).flatMap(exercise => exercise.problems || []));
const before = all().map(problem => ({id: problem.id, question: problem.question, sourceReferences: JSON.stringify(problem.sourceReferences)}));
const count = before.length;
const sourceGap = JSON.stringify(context.data[5].sourceGap);
const repair = read('js/math12_answer_repairs.js');
vm.runInContext(repair, context);
const find = id => all().find(problem => problem.id === id);
assert.equal(all().length, count, 'Question count must not change.');
before.forEach(record => {
  const problem = find(record.id);
  assert(problem, 'Question remains present: ' + record.id);
  assert.equal(problem.question, record.question, 'Printed question preserved: ' + record.id);
  assert.equal(JSON.stringify(problem.sourceReferences), record.sourceReferences, 'Source references preserved: ' + record.id);
});
assert.equal(JSON.stringify(context.data[5].sourceGap), sourceGap, 'Unit 6 source gap must remain intact.');
for (const id of context.MATH12_ANSWER_REPAIRS.questionIds) {
  const problem = find(id);
  assert(problem.answer && problem.steps.length >= 4 && problem.solution, id + ' has a substantive worked answer.');
  assert.equal(problem.solution, problem.steps.join('\n'), id + ' answer and progressive steps stay aligned.');
}
assert.match(find('ex-2-3-project').answer, /absolute-value.*Quadratic/);
assert.match(find('ex-2-3-project').sourceStatus, /unreadable/);
assert.match(find('ex-2-1-q5').sourceStatus, /unresolved/);
assert.match(find('ex-2-1-q5').solution, /chosen for demonstration/);
assert.match(find('ex-10-1-q2').solution, /6e\^\(−x\)/);
assert.equal(find('ex-10-1-q2').sourceQuestionBlocks[0].src, 'assets/math12/ode290-q2c-source-review.jpg');
assert(fs.existsSync(path.join(root, find('ex-10-1-q2').sourceQuestionBlocks[0].src)));
assert.equal(find('ex-12-2-q5').sourceStatus, 'under_specified_source_problem');
assert.match(find('ex-12-2-q5').solution, /no Maple execution/);
const n = 10, h = 2 / n, f = x => Math.exp(-x);
let trapezoid = (f(0) + f(2)) / 2;
let simpson = f(0) + f(2);
for (let i = 1; i < n; i++) {
  trapezoid += f(i * h);
  simpson += (i % 2 ? 4 : 2) * f(i * h);
}
trapezoid *= h;
simpson *= h / 3;
const exact = 1 - Math.exp(-2);
assert(Math.abs(trapezoid - 0.8675450128) < 5e-11);
assert(Math.abs(simpson - 0.8646723662) < 5e-11);
assert(Math.abs((trapezoid - exact) - 0.0028802961) < 5e-11);
assert(Math.abs((simpson - exact) - 0.0000076495) < 5e-11);
for (const x of [-2, 0, 1, 3]) {
  const c = 5;
  assert(Math.abs((1 - x - c) * Math.exp(-x) + (x + c) * Math.exp(-x) - Math.exp(-x)) < 1e-12);
  const residual = Math.exp(x) + Math.exp(-x) - 3 * (Math.exp(x) - Math.exp(-x)) + 2 * (Math.exp(x) + Math.exp(-x));
  assert(Math.abs(residual - 6 * Math.exp(-x)) < 1e-12);
}
const firstLoad = JSON.stringify(context.MATH12_ANSWER_REPAIRS.questionIds.map(find));
vm.runInContext(repair, context);
assert.equal(JSON.stringify(context.MATH12_ANSWER_REPAIRS.questionIds.map(find)), firstLoad, 'Repair loading is idempotent.');
const report = {
  generatedAt: new Date().toISOString(),
  scope: 'Four Class 12 Mathematics source-limited exercise answers; no question wording, source references, chapter structure or source-gap status changed.',
  status: 'focused_checks_passed_with_unresolved_source_defects',
  activeExerciseQuestionGroups: count,
  answerRepairsSha256: crypto.createHash('sha256').update(repair).digest('hex'),
  checks: ['Dataset evaluates with the repair layer', 'All printed question strings and source references preserved', 'No question added or removed', 'Progressive answers align with steps', 'Supplemental quadrature values independently recomputed', 'Conditional differential-equation residuals checked', 'Correct Q2(c) crop exists', 'Source-gap status preserved', 'Repeated loading is idempotent'],
  records: [
    {id: 'ex-2-1-q5', outcome: 'Improved symbolic domain answer and explicitly supplemental worked example. Numerical photographed endpoints remain unresolved.', inspected: ['JPG/020_page_1.jpg', 'assets/math12/ex21-project-landscape.jpg', 'assets/math12/ex21-project-car.jpg'], sourceComplete: false},
    {id: 'ex-2-3-project', outcome: 'Requested classifications answered: inverted absolute-value and quadratic. Exact first-model coefficients remain source-unreadable; no coefficients invented.', inspected: ['JPG/032_page_2.jpg', 'assets/math12/exercise-2-3-project-i.jpg'], requestedClassificationComplete: true, exactSourceModelRecovered: false},
    {id: 'ex-10-1-q2', outcome: 'Existing valid conditional algebra retained. Wrong Q2(d) crop replaced in active answer with isolated Q2(c) source crop. Printed RHS exponent remains unresolved.', inspected: ['JPG/149_page_2.jpg', 'PDF/Math Book for 12 class KPTBB.pdf: physical page 149'], newCrop: {path: 'assets/math12/ode290-q2c-source-review.jpg', sourcePdfPage: 149, pdfPointRect: [474, 201, 576, 222], scale: 4}, sourceComplete: false},
    {id: 'ex-12-2-q5', outcome: 'Added general quadrature formulas, explicit partition convention, worked sum details and errors. The original prompt omits the integrand and partition; no unique original numerical answer can be asserted.', inspected: ['JPG/166_page_1.jpg'], sourceComplete: false, sample: {integrand: 'exp(-x)', bounds: [0, 2], subintervals: n, trapezoid, simpson, exact}}
  ],
  unit6SourceSearch: {
    printedPages: [142, 157],
    status: 'unavailable_in_supplied_formats',
    existingAudit: 'docs/source-verification/math12.json',
    currentLocalInventory: {jpg: 357, pdf: 6, docx: 5},
    searched: 'D:/SpaceBook/Books, including ignored files, for Class 12 Mathematics PDF and Word alternatives',
    result: 'Only the already documented full PDF, five split PDFs and five Word files were found. Existing audit records the same missing span in those source formats. No alternate source was recovered.',
    allSuppliedFilesReaudited: false,
    sourceGapChanged: false
  },
  finalBrowserCheck: 'Owned by integrating task; not performed by this focused data repair check.'
};
const reportPath = path.join(root, 'docs/source-verification/class-12/math12-answer-repairs.json');
fs.writeFileSync(reportPath, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({status: report.status, questionGroups: count, repairedQuestions: report.records.length, unresolvedSourceAnswers: 3, report: path.relative(root, reportPath)}, null, 2));
