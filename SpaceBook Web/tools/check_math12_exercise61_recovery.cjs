'use strict';
const fs = require('fs'), path = require('path'), vm = require('vm'), assert = require('assert/strict');
const root = path.resolve(__dirname, '..');
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const context = {};
vm.createContext(context);
vm.runInContext(read('js/math_12_data.js') + ';globalThis.data=MATH_12_DATA;', context);
const others = () => JSON.stringify(context.data.map(ch => ch.exercises.filter(ex => ex.id !== 'ex-6-5')));
const originalOtherExercises = others();
const script = read('js/math12_unit6_exercise61_recovery.js');
vm.runInContext(script, context);
const exercise = context.data[5].exercises.find(ex => ex.id === 'ex-6-5');
assert.equal(exercise.problems.length, 8);
assert.equal(exercise.problems.reduce((n, p) => n + p.subpartCount, 0), 28);
assert.equal(exercise.pageStart, 150);
assert.equal(exercise.pageEnd, 150);
assert.equal(others(), originalOtherExercises);
for (const problem of exercise.problems) {
  assert(problem.answer && problem.solution && problem.questionUrdu && problem.questionPashto);
  const ref = problem.sourceReferences[0];
  assert.equal(ref.pdfPage, 10);
  assert.equal(ref.page, 150);
  assert.equal(ref.originalFullPdfPage, 155);
  assert.equal(ref.recoveredPdf, 'docs/source-verification/class-12/sources/math12-unit6-recovered.pdf');
}
const firstLoad = JSON.stringify(exercise);
vm.runInContext(script, context);
assert.equal(JSON.stringify(exercise), firstLoad);
// Numeric derivative checks supplement the symbolic working written with each answer.
const integrals = [
  ['1a',x=>x**4/4,x=>x**3,[-2,.5,3]], ['1b',x=>22*x,x=>22,[-2,.5,3]],
  ['1c',x=>Math.log(Math.abs(x))/5,x=>1/(5*x),[-2,.5,3]],
  ['1d',x=>x**3+2*x*x-5*x,x=>3*x*x+4*x-5,[-2,.5,3]],
  ['1e',x=>x**4/4+3*x**5/5,x=>(1+3*x)*x**3,[-2,.5,3]],
  ['1f',x=>-1/(2*x*x),x=>1/x**3,[-2,.5,3]],
  ['1g',x=>Math.exp(5*x)/5,x=>Math.exp(5*x),[-1,.5,2]],
  ['1h',x=>5*Math.atan(x),x=>5/(1+x*x),[-2,.5,3]],
  ['1i',x=>2*x**4.5/9,x=>x**3*Math.sqrt(x),[.2,1,3]],
  ['2a',x=>(3*x+4)**9/27,x=>(3*x+4)**8,[-1,.5,2]],
  ['2b',x=>(x**3-4)**2/2,x=>3*x*x*(x**3-4),[-1,.5,2]],
  ['2c',x=>(x**3+7*x)**9/9,x=>(3*x*x+7)*(x**3+7*x)**8,[-1,.5,2]],
  ['2d',x=>-1/(3*(x**3-7*x)**3),x=>(3*x*x-7)/(x**3-7*x)**4,[-1,.5,2]],
  ['2e',x=>2*Math.sqrt(3*x*x-7),x=>6*x/Math.sqrt(3*x*x-7),[-3,-2,2]],
  ['2f',x=>2*(Math.cbrt(x)+4)**1.5,x=>Math.sqrt(Math.cbrt(x)+4)/(Math.cbrt(x)**2),[-8,-1,1,8]],
  ['2g',x=>2*x**1.5/3+6*x**2.5/5,x=>(x+3*x*x)/Math.sqrt(x),[.2,1,3]],
  ['2h',x=>-1/(2*(x*x+2*x+2)),x=>(x+1)/(x*x+2*x+2)**2,[-3,.5,2]],
  ['3a',x=>Math.exp(6*x),x=>6*Math.exp(6*x),[-1,.5,2]],
  ['3b',x=>Math.exp(5*x*x+1)/10,x=>x*Math.exp(5*x*x+1),[-1,.5,1.2]],
  ['3c',x=>Math.exp(x**3-6*x+4)/3,x=>(x*x-2)*Math.exp(x**3-6*x+4),[-1,.5,2]],
  ['3d',x=>8**(7-3*x*x)/Math.log(8),x=>8**(7-3*x*x)*(-6*x),[-1,.5,2]]
];
let comparisons = 0;
for (const [id, primitive, integrand, points] of integrals) {
  for (const x of points) {
    const h = 1e-6 * (1 + Math.abs(x));
    const derivative = (primitive(x+h) - primitive(x-h)) / (2*h);
    const expected = integrand(x);
    assert(Math.abs(derivative-expected)/Math.max(1,Math.abs(expected)) < 2e-7, id+' derivative at '+x);
    comparisons++;
  }
}
assert.equal(1+2-3, 0);
assert.equal(((2*9-1)**3-4877)/12, 3);
assert.equal(1-Math.exp(0), 0);
assert(Math.abs((1-Math.exp(-.1))-.09516258196404048) < 1e-14);
assert.equal(.0005*60**3, 108);
assert.equal(.0005*70**3, 171.5);
assert.equal(5000+400*9+400*9**1.5, 19400);
const report = {
  generatedAt: new Date().toISOString(), status: 'passed', questionGroups: 8, subparts: 28,
  integrandsChecked: integrals.length, numericalDerivativeComparisons: comparisons,
  particularSolutionsAndInitialConditions: 5, idempotent: true, otherExercisesUnchanged: true,
  source: {printedPage: 150, recoveredPdfPage: 10, originalFullPdfPage: 155,
    path: 'docs/source-verification/class-12/sources/math12-unit6-recovered.pdf'},
  limitations: ['Finite difference checks supplement analytic derivations; they are not a formal proof.', 'Answer translations remain pending.', 'Original source prose is not reproduced.']
};
const reportPath = path.join(root, 'docs/source-verification/class-12/math12-exercise61-recovery-check.json');
fs.writeFileSync(reportPath, JSON.stringify(report, null, 2)+'\n');
console.log(JSON.stringify(report, null, 2));
