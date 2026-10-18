// This checks bookkeeping and rendering inputs, not word-for-word source accuracy.
// Source fidelity still requires visual inspection of the JPG/PDF pages.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const root = path.resolve(__dirname, '..');
const ledger = JSON.parse(fs.readFileSync(path.join(root, 'docs/source-verification/math12.json'), 'utf8'));
const sourceDir = path.resolve(root, '../Books/12th/12th Maths/JPG');
const images = fs.readdirSync(sourceDir).filter(name => /\.jpg$/i.test(name)).sort();
assert.deepEqual(ledger.pages.map(page => page.jpg), images, 'Every supplied JPG must appear once, in source order');
assert.equal(ledger.sourceCount, images.length);
const context = vm.createContext({});
vm.runInContext(fs.readFileSync(path.join(root, 'js/math_12_data.js'), 'utf8'), context);
const chapters = JSON.parse(vm.runInContext('JSON.stringify(MATH_12_DATA)', context));
const pages = [...chapters.flatMap(chapter => chapter.sourcePages || []), ...chapters.flatMap(chapter => chapter.sourceAnswerPages || []).sort((a,b)=>a.page-b.page), ...chapters.flatMap(chapter => chapter.sourceBackMatterPages || [])];
assert.equal(new Set(pages.map(page => page.file)).size, pages.length, 'Duplicate source pages');
const reviewedPrintedPages = pages.filter(page => typeof page.page === 'number').map(page => page.page);
assert.deepEqual(reviewedPrintedPages, [...Array.from({length:141}, (_, index) => index + 1),158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349], 'A reviewed printed page was skipped');
for (const page of pages) {
  const entry = ledger.pages.find(entry => entry.jpg === page.file);
  assert(entry, `Untracked source ${page.file}`);
  assert.equal(entry.textStatus, page.textStatus || (page.page===33 ? 'partial_source_legibility' : page.sourceDefects && page.sourceDefects.length ? 'partial_source_clipping' : 'visually_verified'));
  for (const block of page.blocks || []) {
    if (block.type === 'figure') {
      assert(block.alt && block.caption, 'Figure must retain caption and accessible description');
      assert(fs.existsSync(path.join(root, block.src)), `Missing figure ${block.src}`);
    }
  }
}
for (const section of chapters[0].sections.slice(0, 2)) {
  const numberedResults = section.sourceBlocks.filter(block => block.type === 'command' && block.number != null);
  assert.deepEqual(numberedResults.map(block => block.number), Array.from({length:10}, (_, index) => index + 1), `Missing or unordered commands in ${section.id}`);
  assert(section.sourceReferences.length && section.theory, 'Reviewed text must remain searchable and traceable');
}
assert.equal(chapters.length, 12, 'Unreviewed units must remain intact');
assert(chapters[0].sections[3].theory.includes('1.4'), 'Unreviewed matrices content was removed');
assert.equal(chapters[0].sections[3].unreviewedTheory, '', 'Completed matrix source text must replace the old incomplete transcription');
assert.equal(chapters[0].sections[3].sourceBlocks.filter(block => block.type === 'matrix').length, 27);
assert(chapters[0].sections[3].sourceBlocks.some(block => block.type === 'clarification'), 'Original errors require a separate clarification');
assert(chapters[0].sections[3].theory.includes('Transport of a matrix'), 'Printed heading was silently corrected');
assert(chapters[1].sourcePages[0].objectives.length === 8 && chapters[1].sourcePages[0].sourceDefects.length, 'Unit 2 objectives and their source clipping must be tracked');
assert.equal(chapters[1].sections[0].unreviewedTheory, '', 'Reviewed modulus text must replace incomplete OCR');
assert.equal(chapters[1].sections[1].unreviewedTheory, '', 'Reviewed composition text must replace incomplete OCR');
assert(chapters[1].sections[0].theory.includes('f(x) = |3x − 4|') && chapters[1].sections[0].theory.includes('f(x) = |3x + 4|'), 'Original problem/solution mismatch must remain visible');
assert.equal(chapters[1].workedExamples.slice(0,7).filter(example => example.progressiveSolution && example.solutionOrigin).length, 7);
assert.deepEqual(chapters[1].workedExamples.slice(0,8).map(example => example.num), ['1','2','3','4','5','6','7','8'], 'Missing examples must be restored in source order');
assert.equal(new Set(chapters[1].workedExamples.map(example => example.id)).size, chapters[1].workedExamples.length, 'Restored examples must not reuse existing IDs');
assert.equal(chapters[1].sections[2].unreviewedTheory, '', 'Reviewed exercises must leave the inverse lesson body');
const exercise21 = chapters[1].exercises[0];
assert.equal(exercise21.pageStart,31); assert.equal(exercise21.pageEnd,31);
assert.equal(exercise21.problems[0].sourceQuestionBlocks.length,6);
assert.equal(exercise21.problems[4].sourceQuestionBlocks.length,2);
assert(exercise21.problems.every(problem => problem.progressiveSolution && problem.solutionOrigin && problem.steps.length>1));
assert(exercise21.problems[2].solution.includes('ℝ ∖ {1}') && exercise21.problems[2].solution.includes('ℝ ∖ {−1}'), 'Rational composition domains were lost after cancellation');
assert(exercise21.problems[4].solutionStatus.startsWith('partial'), 'Unverified project endpoints must remain flagged');
const transcendental=chapters[1].sections[3];
assert(transcendental.theory.includes('a_{n-1}x^{n-1}'), 'General polynomial indices were lost');
assert(transcendental.theory.includes('\\frac{8t^3+5t-9}{t^4+1}'), 'Rational example exponents were lost');
assert.equal(transcendental.sourceBlocks.find(block=>block.type==='dataTable').rows.length,4);
assert.equal(transcendental.sourceBlocks.filter(block=>block.type==='dataTable')[1].rows.length,7);
assert(transcendental.theory.includes('\\frac{a^x}{b^x}=a^{x-y}'), 'Printed quotient law was silently corrected');
const population=chapters[1].workedExamples.find(example=>example.num==='8');
assert(population.progressiveSolution && population.answer.includes('100') && population.sourceClarification.includes('99.97'));
assert.deepEqual([1,3,4].map(time=>Math.round(25*Math.exp(1.386*time))),[100,1599,6392], 'Growth-model rounding is incorrect');
assert(transcendental.theory.includes('99.97') && transcendental.theory.includes('uses b = 2'), 'Printed result or disclosed graph base missing');
assert.equal(transcendental.sourceBlocks.filter(block=>block.type==='diagram').length,3);
const logRulesPage=pages.find(page=>page.page===35);
assert.equal(logRulesPage.blocks.find(block=>block.type==='list').items.length,8);
assert(logRulesPage.blocks.some(block=>block.result && block.result.includes('4998n')), 'Example 11 source denominator missing');
assert.equal(Math.log10(2).toFixed(4),'0.3010'); assert.equal(Math.log(3).toFixed(4),'1.0986');
assert(chapters[1].workedExamples.filter(example=>['9','10'].includes(example.num)).every(example=>example.progressiveSolution && example.solutionOrigin));
assert(chapters[1].workedExamples.find(example=>example.num==='11').progressiveSolution);
assert.equal((-1.43*Math.log(9500/2499000)).toFixed(4),'7.9685');
assert.equal((-1.43*Math.log(1/4998)).toFixed(4),'12.1790');
assert(transcendental.theory.includes('\\cosh^2x-\\sinh^2x=1') && transcendental.theory.includes('e^{x^3}'), 'Hyperbolic identity or nested explicit-function exponent missing');
assert.deepEqual(chapters[0].sections[0].sourceReferences.map(reference => reference.page), [1,2,3,4,5,6], 'Introduction references unrelated pages');
const graphics = chapters[0].sections[2];
assert.deepEqual(graphics.sourceBlocks.filter(block => block.type === 'diagram').map(block => block.caption), ['Figure 1.11','Figure 1.12','Figure 1.13','Figure 1.14','Figure 1.15','Figure 1.17']);
assert(graphics.theory.includes('Plot employs an adaptive plotting scheme'), 'Printed plotting reminder missing');
assert(graphics.theory.includes('discount = t'), 'Printed syntax was silently corrected');
assert(graphics.theory.includes('such that created by'), 'Paragraph split over pages 12 and 13 was not rejoined');
assert(chapters[0].workedExamples[4].problem.includes('x=\\sin(t)') && chapters[0].workedExamples[4].sourceClarification, 'Original variable error and educational clarification must remain distinct');
assert(chapters[0].workedExamples.every(example => example.progressiveSolution && example.solutionOrigin), 'Reviewed examples need distinct progressive learning solutions');
if (ledger.bookStatus === 'complete') assert(ledger.pages.every(page => page.pageComplete), 'Incomplete pages cannot support book completion');

assert.deepEqual(chapters[1].workedExamples.slice(0,24).map(e=>e.num), Array.from({length:24},(_,i)=>String(i+1)));
assert(chapters[1].workedExamples.filter(e=>['12','13'].includes(e.num)).every(e=>e.progressiveSolution && e.sourceReferences[0].pageStart===37));
assert(chapters[1].sections[4].sourceBlocks.some(b=>b.caption==='Figure 2.10'));
assert.equal(chapters[1].sections[4].unreviewedTheory,'');

assert.equal(chapters[1].sections[4].sourceBlocks.filter(b=>b.type==='diagram').length,21);
assert(chapters[1].workedExamples.find(e=>e.num==='14').sourceReferences[0].pageStart===38);

assert(chapters[1].workedExamples.filter(e=>Number(e.num)>=15&&Number(e.num)<=17).every(e=>e.progressiveSolution&&e.sourceReferences[0].pageStart===39));
assert(chapters[1].sections[4].sourceReferences.some(r=>r.page===39));

const conicPage=pages.find(p=>p.page===40);
assert.equal(conicPage.blocks.find(b=>b.type==='dataTable').headers.length,14);
assert.equal(conicPage.blocks.filter(b=>b.type==='clarification').length,2);
assert(chapters[1].workedExamples.filter(e=>Number(e.num)>=18&&Number(e.num)<=20).every(e=>e.progressiveSolution&&e.sourceReferences[0].pageStart===40));
assert(chapters[1].workedExamples.find(e=>e.num==='19').answer.includes('(±4, 0)'));
assert(chapters[1].workedExamples.find(e=>e.num==='20').diagram.sidewaysParabola.coefficient===3/16);

const compound=chapters[1].workedExamples.find(e=>e.num==='22');
assert.deepEqual(compound.diagram.openPoints,[[-2,5],[2,4]]);
assert.deepEqual(compound.diagram.closedPoints,[[-2,0],[2,1]]);
assert(compound.answer.includes('[0, 4) ∪ (5, ∞)'));
assert.equal(chapters[1].workedExamples.find(e=>e.num==='21').sourceReferences[0].pageStart,41);
assert.equal(pages.find(p=>p.page===41).blocks.find(b=>b.type==='dataTable').headers.length,10);

const maplePage=pages.find(p=>p.page===42);
assert.deepEqual(maplePage.blocks.filter(b=>b.type==='diagram').map(b=>b.caption),['Figure 2.21','Figure 2.22','Figure 2.23','Figure 2.24']);
assert(maplePage.sourceNotes[0].includes('continues'));
assert(maplePage.blocks.some(b=>b.type==='command'&&b.text&&b.text.includes('x = 0..−4')));

const mapleExample=chapters[1].workedExamples.find(e=>e.num==='23');
assert(mapleExample.progressiveSolution);
assert.equal(mapleExample.sourceReferences[0].pageStart,42);assert.equal(mapleExample.sourceReferences[0].pageEnd,43);
assert.equal(mapleExample.diagram.hyperbola,true);
assert(!chapters[1].sections[4].unreviewedTheory.includes('Example 23'));
assert.equal(chapters[1].sections[5].unreviewedTheory,'');
assert(pages.find(p=>p.page===43).sourceNotes[0].includes('verified across pages 43–44'));

const ex22=chapters[1].exercises[1];assert.equal(ex22.problems.length,8);assert.equal(ex22.pageStart,44);
assert(ex22.problems.slice(0,3).every(p=>p.progressiveSolution&&p.answerKeyReference.printedPage===327));
assert(ex22.problems.every(p=>p.solution&&p.answer&&p.progressiveSolution&&p.solutionStatus==='worked and checked'));
assert.deepEqual([0,800,1600,5000].map(t=>(100*Math.exp(-.00043*t)).toFixed(2)),['100.00','70.89','50.26','11.65']);
assert.equal(chapters[1].workedExamples.find(e=>e.num==='24').sourceReferences[0].pageEnd,44);

assert.equal(chapters[1].workedExamples.filter(e=>e.num==='24').length,2);
assert(chapters[1].workedExamples.slice(0,24).every(e=>e.progressiveSolution));

assert.equal(ex22.problems[2].solutionBlocks.filter(b=>b.type==='diagram').length,4);
assert.deepEqual(ex22.problems.slice(2).map(p=>p.solutionBlocks.filter(b=>b.type==='diagram').length),[4,5,2,7,4,7]);
assert.equal(ex22.problems[5].solutionBlocks[5].diagram.logarithm.power,2);
assert.equal(ex22.problems[5].solutionBlocks[6].diagram.logarithm.inputFactor,2);
assert.equal(ex22.problems[4].solutionBlocks[1].diagram.ellipse.clockwise,true);
assert.equal(ex22.problems[6].solutionBlocks[3].diagram.ellipse.b,Math.sqrt(6));
assert(Math.abs(2*Math.log(20)-5.991464547)<1e-8);
assert(ex22.problems[3].sourceClarification.includes('(18, 6.4)'));
assert(ex22.problems[5].sourceClarification.includes('opposite exercise parts'));
assert(!ex22.problems[7].answerKeyReference);
assert.equal(chapters[1].sections[5].sourceBlocks.filter(b=>b.type==='diagram').length,9);
const sequencePage=pages.find(p=>p.page===47);
assert(sequencePage.blocks.some(b=>b.result&&b.result.includes('\\approx')));
const sequencePoints=sequencePage.blocks.find(b=>b.type==='diagram').diagram.points;
assert.equal(sequencePoints.length,25);
sequencePoints.forEach(([n,value],i)=>{assert.equal(n,i+1);assert.equal(value,(n+2)/n**2);});
const sequenceLimitPage=pages.find(p=>p.page===48);
assert(chapters[1].sourcePages.every(p=>p.title==='FUNCTIONS AND LIMITS'));
assert.equal(sequenceLimitPage.blocks.filter(b=>b.type==='dataTable').length,2);
const sequenceMarks=sequenceLimitPage.blocks.find(b=>b.type==='diagram').diagram.points;
assert.equal(sequenceMarks.length,8);
sequenceMarks.forEach((point,i)=>assert.equal(point.x,8*(i+1)/(i+4)));
assert(sequenceLimitPage.blocks.some(b=>b.text&&b.text.includes('n+1')));
assert(chapters[1].workedExamples.find(e=>e.num==='27').answer.includes('+∞'));
assert(chapters[1].workedExamples.find(e=>e.num==='27').steps.some(s=>s.includes('2k + 1')));
assert.equal(chapters[1].workedExamples.find(e=>e.num==='27').sourceReferences[0].pageEnd,49);
assert(pages.find(p=>p.page===49).blocks.some(b=>b.text&&b.text.includes('\\delta\\to0')));
assert(pages.find(p=>p.page===49).blocks.some(b=>b.type==='clarification'&&b.text.includes('δ > 0')));
assert.deepEqual(chapters[1].workedExamples.filter(e=>Number(e.num)>=28&&Number(e.num)<=31).map(e=>e.answer),['9.','−12.','16.','−6/7.']);
assert.equal(chapters[1].workedExamples.find(e=>e.num==='29').sourceReferences[0].pageEnd,50);
const importantLimits=chapters[1].sections[6];
assert.equal(importantLimits.title,'2.7 Important Limits');
assert.deepEqual(importantLimits.sourceReferences.map(r=>r.page),[51,52,53,54,55]);
assert.equal(importantLimits.unreviewedTheory,'');
const eTable=pages.find(p=>p.page===52).blocks.find(b=>b.type==='dataTable');
assert.equal(eTable.rows.length,7);
assert.deepEqual(eTable.rows.map(row=>row[0]),['1','10','100','1000','10000','100000','1000000']);
assert(pages.find(p=>p.page===52).blocks.some(b=>b.result&&b.result.includes('x\\to-\\infty')));
assert(pages.find(p=>p.page===51).blocks.some(b=>b.type==='clarification'&&b.text.includes('right-hand limit')));
assert(pages.find(p=>p.page===52).blocks.some(b=>b.type==='clarification'&&b.text.includes('a = 1')));
const proofPage=pages.find(p=>p.page===53);
assert(proofPage.blocks.some(b=>b.type==='clarification'&&b.text.includes('a = 0')));
assert(proofPage.blocks.some(b=>b.type==='clarification'&&b.text.includes('n = 0')));
assert(proofPage.blocks.some(b=>b.result&&b.result.includes('\\log_e a=\\ln a')));
const sinePage=pages.find(p=>p.page===54);
const sineAngle=sinePage.blocks.find(b=>b.type==='diagram').diagram.angleRad;
assert(sineAngle>0&&sineAngle<Math.PI/2);
assert(Math.sin(sineAngle)<sineAngle&&sineAngle<Math.tan(sineAngle));
assert(sinePage.blocks.some(b=>b.result&&b.result.includes('1<x<')));
assert(sinePage.blocks.some(b=>b.type==='clarification'&&b.text.includes('from the left')));
assert.equal(chapters[1].workedExamples.find(e=>e.num==='32').answer,'1/4.');
const mapleLimitPage=pages.find(p=>p.page===55);
assert.equal(mapleLimitPage.blocks.filter(b=>b.type==='command'&&b.prompt).length,7);
assert(mapleLimitPage.blocks.some(b=>b.result==='−10'));
assert(mapleLimitPage.blocks.some(b=>b.result==='−54'));
assert.equal(chapters[1].workedExamples.find(e=>e.num==='33').answer,'2.');
assert.equal(chapters[1].workedExamples.find(e=>e.num==='34').answer,'(a) 0; (b) 0.');
assert.equal(chapters[1].workedExamples.find(e=>e.num==='35').answer,'(a) 10; (b) −54; (c) 3a².');
const ex23=chapters[1].exercises[2];
assert.equal(ex23.pageStart,56);assert.equal(ex23.pageEnd,56);assert.equal(ex23.problems.length,7);
assert(ex23.problems.every(p=>p.progressiveSolution&&p.steps.length>=3));
assert(ex23.problems.slice(0,6).every(p=>p.solutionStatus==='worked and checked'));
assert(ex23.problems[6].solutionStatus.startsWith('partial'));
assert.equal(ex23.problems[6].sourceQuestionBlocks.length,2);
assert(ex23.problems[3].question.includes('x\\to16'));
assert(ex23.problems[3].answer.includes('5200'));
assert(ex23.problems[5].answer.includes('(f) e²; (g) e⁻¹'));
assert(ex23.problems[5].steps[4].includes('=\\ln(1-u)/u'));
const continuity=chapters[1].sections[7];
assert.deepEqual(continuity.sourceReferences.map(r=>r.page),[57,58,59]);
assert.equal(continuity.unreviewedTheory,'');
const continuityExample=chapters[1].workedExamples.find(e=>e.num==='36');
assert(continuityExample.problem.includes('x\\to5'));
assert(continuityExample.answer.includes('= 11'));
assert(continuityExample.answer.includes('12 has no two-sided limit'));
assert.deepEqual(continuityExample.solutionBlocks[0].diagram.openPoints,[[12,4],[14,14]]);
assert.deepEqual(continuityExample.sourceQuestionBlocks[0].rows.map(r=>r[0]),['\\(3x+4\\)','\\(16-x\\)','\\(x\\)']);
assert.equal(chapters[1].workedExamples.find(e=>e.id==='we-2-source-24-intervals').sourceReferences[0].pageStart,45);
assert.deepEqual(chapters[1].workedExamples.find(e=>e.num==='25').sourceQuestionBlocks.map(b=>[b.diagram.leftClosed,b.diagram.rightClosed]),[[false,false],[true,true],[undefined,true]]);


assert(chapters[1].workedExamples.find(e=>e.num==='37').problem.includes('x^3-2x^2'));
assert(chapters[1].workedExamples.find(e=>e.num==='38').answer.includes('removable hole'));

const postage=chapters[1].workedExamples.find(e=>e.num==='39');
assert.deepEqual(postage.solutionBlocks[0].diagram.closedPoints,[[1,.32],[2,.55],[3,.78],[4,1.01],[5,1.24]]);
assert(chapters[1].workedExamples.find(e=>e.num==='40').steps[1].includes('default interval is open'));

const ex24=chapters[1].exercises[3].problems;
assert.equal(ex24.length,8);
assert(ex24.every(p=>p.progressiveSolution&&p.steps.length>=3));
assert(ex24[6].question.includes('x^3+2.7'));
assert(ex24[6].answer.includes('false'));
assert.deepEqual(ex24[5].solutionBlocks[0].diagram.openPoints,[[20000,1500]]);
const review2=chapters[1].exercises[4].problems;
assert.equal(review2.length,15);
assert(review2.every(p=>p.progressiveSolution&&p.sourceQuestionBlocks[0].items.length===4));
assert(review2[0].question.includes('(x+3)^3'));
assert(review2[13].question.includes("f'(0)"));
assert.equal(review2[13].answer,'Option (b)');
assert(review2[13].sourceClarification.includes('printed answer key selects (a)'));
assert(review2[2].sourceClarification.includes('identical'));
assert.equal(chapters[1].sourceSummaryReferences[0].page,62);
assert(chapters[1].sourceSummaryBlocks.some(b=>b.type==='figure'&&b.alt.includes('Steinhaus')));
assert(chapters[1].sourceSummaryBlocks.some(b=>b.type==='clarification'&&b.text.includes('one-to-one')));
assert.equal(chapters[1].sourceSummaryBlocks.find(b=>b.type==='list').items.length,3);
assert.equal(chapters[2].sourcePages[0].page,63);
assert.equal(chapters[2].sourcePages[0].objectives.length,7);
assert(chapters[2].sourcePages[0].objectives[0][1][6].includes('q\\ne0'));
assert(chapters[2].sourcePages[0].objectives[6][1].some(item=>item.includes('MAPLE command diff')));
assert.equal(chapters[2].sourcePages[1].page,64);
assert.deepEqual(chapters[2].sourcePages[1].blocks.find(b=>b.type==='dataTable').rows,[['Distance','0','24','54','88','120']]);
assert.equal(chapters[2].sections[0].unreviewedTheory,'');
assert(chapters[2].sections[0].sourceBlocks.some(b=>b.type==='clarification'&&b.text.includes('−34')));
const source66=chapters[2].sourcePages.find(p=>p.page===66);
assert.equal(source66.blocks.filter(b=>b.type==='diagram').length,2);
assert.deepEqual(source66.blocks.find(b=>b.type==='dataTable').rows.map(r=>r[4]),['2.5','2.0','1.5','1.3']);
assert(chapters[2].workedExamples.find(e=>e.num==='2').progressiveSolution);
assert.equal(chapters[2].workedExamples.find(e=>e.num==='2').sourceReferences[0].pageEnd,66);
const source67=chapters[2].sourcePages.find(p=>p.page===67);
assert(source67.blocks.some(b=>b.diagram&&b.diagram.tangent));
assert.deepEqual(source67.blocks.find(b=>b.type==='dataTable').headers,['Mathematician','Newton','Leibniz','Euler','Lagrange']);
assert(chapters[2].workedExamples.find(e=>e.num==='3').progressiveSolution);
assert(chapters[2].workedExamples.find(e=>e.num==='4').progressiveSolution);
assert(chapters[2].workedExamples.find(e=>e.num==='4').answer.includes('6x-9'));
assert(chapters[2].sourcePages.find(p=>p.page===68).blocks.some(b=>b.type==='clarification'&&b.text.includes('vertical tangent')));
const source69=chapters[2].sourcePages.find(p=>p.page===69);
assert.equal(source69.blocks.filter(b=>b.type==='clarification').length,2);
assert(source69.blocks.some(b=>b.result&&b.result.includes('binom')));
assert(source69.sourceNotes.some(note=>note.includes('negative integer')));
const exercise31=chapters[2].exercises[0].problems;
assert.equal(exercise31.length,8);
assert(exercise31.every(p=>p.progressiveSolution&&p.steps.length>=3));
assert(exercise31[0].question.includes('2t³'));
assert(exercise31[1].answer.includes('1/7'));
assert.equal(exercise31[6].solutionBlocks.length,2);
assert.equal(chapters[2].sections[1].sourceReferences[0].page,71);
assert(chapters[2].workedExamples.find(e=>e.num==='6').answer.includes('3.330'));
assert.equal(chapters[2].sections[1].sourceReferences.length,5);
assert(chapters[2].workedExamples.find(e=>e.num==='7').answer.includes('6x-3'));
assert(chapters[2].sourcePages.find(p=>p.page===72).blocks.some(b=>b.text&&b.text.includes('continues on printed page 73')));
const source73=chapters[2].sourcePages.find(p=>p.page===73);
assert(source73.blocks.some(b=>b.type==='clarification'&&b.text.includes('incorrectly uses')));
assert.equal(source73.blocks.filter(b=>b.type==='command').length,14);
assert(source73.blocks.some(b=>b.type==='clarification'&&b.text.includes('stays nonzero')));
assert(chapters[2].workedExamples.find(e=>e.num==='8').steps.length===8);
assert(chapters[2].workedExamples.find(e=>e.num==='8').answer.includes('-2x^2-12x-60'));
assert.equal(chapters[2].workedExamples.filter(e=>e.num==='7').length,1);
assert.equal(chapters[2].unreviewedDuplicateExamples.length,1);
assert(chapters[2].workedExamples.find(e=>e.num==='9').answer.includes('million dollars'));
assert.equal(chapters[2].sections[2].sourceReferences[0].page,75);
const exercise32=chapters[2].exercises[1].problems;
assert.equal(exercise32.length,6);
assert(exercise32.every(p=>p.progressiveSolution&&p.steps.length>=4));
assert(exercise32[5].answer.includes('L^2-36'));
assert(chapters[2].sourcePages.find(p=>p.page===76).blocks.some(b=>b.diagram&&b.diagram.type==='source-ladder-rates'));
const derivativePairs=[
 [x=>(x*x-2)*(3*x+1),x=>9*x*x+2*x-6],
 [x=>(7*x**4+2*x)*(x*x-4),x=>42*x**5-112*x**3+6*x*x-8],
 [x=>(2*x-3)*(Math.sqrt(x)-1),x=>3*Math.sqrt(x)-2-3/(2*Math.sqrt(x))],
 [x=>(-3*Math.sqrt(x)+6)*(4*Math.sqrt(x)-2),x=>15/Math.sqrt(x)-12],
 [x=>(3*x-5)/(x-4),x=>-7/(x-4)**2],
 [x=>(-x*x+6*x)/(4*x**3+1),x=>(4*x**4-48*x**3-2*x+6)/(4*x**3+1)**2],
 [x=>(5*x+6)/Math.sqrt(x),x=>(5*x-6)/(2*x*Math.sqrt(x))],
 [p=>(2*p+3)*(4*p-1)/(3*p+2),p=>(24*p*p+32*p+29)/(3*p+2)**2],
 [x=>2*x/(x-2),x=>-4/(x-2)**2]
];
for(const [f,d] of derivativePairs)for(const x of [1.3,2.7,5.2]){const h=1e-5;const estimate=(f(x+h)-f(x-h))/(2*h);assert(Math.abs(estimate-d(x))<1e-5*Math.max(1,Math.abs(d(x))),'Independent numerical derivative check');}
assert.equal(chapters[2].sections[3].sourceReferences.length,5);
assert(chapters[2].workedExamples.find(e=>e.num==='11').answer.includes('93.75'));
assert(chapters[2].sourcePages.find(p=>p.page===77).blocks.some(b=>b.type==='clarification'&&b.text.includes('q(0)')));
assert(chapters[2].sourcePages.find(p=>p.page===78).blocks.some(b=>b.type==='clarification'&&b.text.includes('nonzero finite derivative')));
for(const [f,d] of [[x=>(4*x-3)**3,x=>12*(4*x-3)**2],[x=>Math.sqrt(15*x*x+1),x=>15*x/Math.sqrt(15*x*x+1)],[t=>8000*(30-6*t)/(32-6*t),t=>-96000/(32-6*t)**2]])for(const x of [.2,1.3,2.7]){const h=1e-5;assert(Math.abs((f(x+h)-f(x-h))/(2*h)-d(x))<1e-5*Math.max(1,Math.abs(d(x))));}
assert.equal(16000/32**2*(-6),-93.75);
assert(chapters[2].workedExamples.find(e=>e.num==='12').answer.includes('x ≠ 3/4'));
assert(chapters[2].workedExamples.find(e=>e.num==='13').answer.includes('176x'));
assert(chapters[2].workedExamples.find(e=>e.num==='14').answer.includes('3-2xy'));
for(const [f,d] of [[x=>(11*x*x-7)**8,x=>176*x*(11*x*x-7)**7],[x=>Math.sqrt(2*x**3+11),x=>3*x*x/Math.sqrt(2*x**3+11)]])for(const x of [-1,.2,1.3]){const h=1e-5;assert(Math.abs((f(x+h)-f(x-h))/(2*h)-d(x))<1e-5*Math.max(1,Math.abs(d(x))));}
function implicit14Root(x,initial){let y=initial;for(let i=0;i<10;i++)y-=(x*x*y+2*y**3-3*x-2*y)/(x*x+6*y*y-2);return y;}
for(const y of [-1,0,1]){const h=1e-5;const estimate=(implicit14Root(h,y)-implicit14Root(-h,y))/(2*h);assert(Math.abs(estimate-3/(6*y*y-2))<1e-7);}
assert(chapters[2].sourcePages.find(p=>p.page===80).blocks.some(b=>b.type==='clarification'&&b.text.includes('a = 0')));
const ex33=chapters[2].exercises[2].problems;assert.equal(ex33.length,9);assert(ex33.every(p=>p.progressiveSolution&&p.steps.length>=5));assert(ex33[2].sourceClarification.includes('12t²/a'));assert(!ex33[4].sourceClarification);assert(ex33[3].answer.includes('4222.8'));assert.equal(chapters[2].sections[4].sourceReferences[0].page,82);
assert.equal(5**2+4**2,5*5+4*4);assert.equal((5-2*5)/(2*4-4),-1.25);
const ex33DerivativePairs=[
 [x=>4*(x**3-4*x+2)**5,x=>20*(x**3-4*x+2)**4*(3*x*x-4)],
 [x=>(4*x-x**3)**11/5,x=>11/5*(4*x-x**3)**10*(4-3*x*x)],
 [t=>Math.cbrt(1-3*t*t),t=>-2*t/Math.cbrt(1-3*t*t)**2],
 [t=>1/(3*t+1)**7,t=>-21/(3*t+1)**8],
 [x=>(2*x-5)**3*(5*x-7),x=>(2*x-5)**2*(40*x-67)],
 [x=>(x+2)**2/(x-1),x=>(x*x-2*x-8)/(x-1)**2],
 [x=>((2*x-5)/(x-4))**4,x=>-12*(2*x-5)**3/(x-4)**5],
 [x=>x*Math.sqrt(2*x*x+11),x=>(4*x*x+11)/Math.sqrt(2*x*x+11)],
 [x=>(x*x+1)**(-1/3),x=>-2*x/(3*(x*x+1)**(4/3))],
 [x=>x*x/(x+2),x=>(x*x+4*x)/(x+2)**2],
 [x=>1/(5-x),x=>1/(5-x)**2],
 [x=>(x+2)/(x-1),x=>-3/(x-1)**2]
];for(const [f,d] of ex33DerivativePairs)for(const x of [.2,1.3,2.7]){const h=1e-6,estimate=(f(x+h)-f(x-h))/(2*h);assert(Math.abs(estimate-d(x))<1e-5*Math.max(1,Math.abs(d(x))));}
for(const t of [.3,1.2,2.3]){const h=1e-6,x=q=>6*q*q+2,y=q=>6*q**4+9;assert(Math.abs((y(t+h)-y(t-h))/(x(t+h)-x(t-h))-2*t*t)<1e-7);}
const productionCost=t=>{const q=t*t+100*t;return .2*q*q+q+900;};assert(Math.abs((productionCost(1.000001)-productionCost(.999999))/.000002-4222.8)<1e-5);
const ex34=chapters[2].exercises[3].problems;
assert.equal(ex34.length,5);assert(ex34.every(p=>p.progressiveSolution&&p.steps.length>=7));
assert(ex34[1].sourceClarification.includes('squared argument'));
assert(ex34[2].sourceClarification.includes('incorrect plus'));
assert(chapters[2].workedExamples.find(e=>e.num==='18').answer.includes('|x|'));
assert.equal(chapters[2].sections[4].sourceReferences.at(-1).page,90);
assert.equal(chapters[2].sections[4].unreviewedTheory,'');
const sec=x=>1/Math.cos(x),csc=x=>1/Math.sin(x),cot=x=>1/Math.tan(x);
const trigChecks=[
 [x=>(x*x+x)*Math.sin(x),x=>(2*x+1)*Math.sin(x)+(x*x+x)*Math.cos(x)],
 [x=>(1+Math.sin(x))/(2-Math.cos(x)),x=>(2*Math.cos(x)-Math.sin(x)-1)/(2-Math.cos(x))**2],
 [x=>sec(x)*Math.tan(x),x=>sec(x)**3+sec(x)*Math.tan(x)**2],
 [x=>(x*x+Math.tan(x))/(3*x+2*Math.tan(x)),x=>(3*x*x+(4*x-3)*Math.tan(x)+x*(3-2*x)*sec(x)**2)/(3*x+2*Math.tan(x))**2],
 [x=>Math.acos((x*x-1)/(x*x+1)),x=>-2*x/(Math.abs(x)*(1+x*x))],
 [x=>Math.sin(2*x),x=>2*Math.cos(2*x)],
 [x=>cot(3*x),x=>-3*csc(3*x)**2],
 [x=>Math.cos(3*x)+Math.tan(3*x),x=>3*(sec(3*x)**2-Math.sin(3*x))],
 [x=>cot(x)**2,x=>-2*cot(x)*csc(x)**2],
 [x=>Math.tan(Math.sqrt(x)),x=>sec(Math.sqrt(x))**2/(2*Math.sqrt(x))],
 [x=>Math.sin(x)**3,x=>3*Math.sin(x)**2*Math.cos(x)],
 [x=>x*x*cot(3*x),x=>2*x*cot(3*x)-3*x*x*csc(3*x)**2],
 [x=>(Math.sin(2*x)+cot(3*x))**2,x=>2*(Math.sin(2*x)+cot(3*x))*(2*Math.cos(2*x)-3*csc(3*x)**2)],
 [x=>4*csc(2*x),x=>-8*csc(2*x)*cot(2*x)],
 [x=>2*Math.tan((x+3)**2),x=>4*(x+3)*sec((x+3)**2)**2],
 [x=>Math.sqrt(Math.tan(x))/Math.cos(Math.sqrt(x)),x=>(Math.sqrt(x)*Math.cos(Math.sqrt(x))*sec(x)**2+Math.tan(x)*Math.sin(Math.sqrt(x)))/(2*Math.sqrt(x)*Math.sqrt(Math.tan(x))*Math.cos(Math.sqrt(x))**2)],
 [x=>(1+Math.tan(2*x))/csc(3*x),x=>2*sec(2*x)**2*Math.sin(3*x)+3*(1+Math.tan(2*x))*Math.cos(3*x)],
 [x=>Math.asin(1/Math.sqrt(1+x*x)),x=>-x/(Math.abs(x)*(1+x*x))],
 [x=>Math.atan((x+1)/(x-1))/x,x=>-1/(x*(x*x+1))-Math.atan((x+1)/(x-1))/(x*x)]
];
for(const [f,d] of trigChecks)for(const x of [.2,.4,1.2]){const h=1e-6,n=(f(x+h)-f(x-h))/(2*h),expected=d(x);assert(Math.abs(n-expected)<1e-4*Math.max(1,Math.abs(expected)),'Trig independent derivative mismatch at '+x);}
for(const x of [-.3,-2])for(const [f,d] of [trigChecks[4],trigChecks[17]]){const h=1e-6;assert(Math.abs((f(x+h)-f(x-h))/(2*h)-d(x))<1e-5,'Negative branch lost');}
assert.equal(chapters[2].sections[5].unreviewedTheory,'');
assert(chapters[2].workedExamples.find(e=>e.num==='19').sourceClarification.includes('1/ln u'));
assert.equal(chapters[2].workedExamples.find(e=>e.num==='20').steps.length,8);
const expChecks=[
 [x=>7**(4-3*x**5),x=>-15*x**4*7**(4-3*x**5)*Math.log(7),[.1,.3,.7]],
 [x=>Math.log10(Math.sqrt(x*x-7*x))+x**3,x=>(2*x-7)/(2*(x*x-7*x)*Math.log(10))+3*x*x,[-2,8,10]],
 [x=>Math.log(Math.exp(2*x)+Math.exp(-2*x)),x=>2*(Math.exp(2*x)-Math.exp(-2*x))/(Math.exp(2*x)+Math.exp(-2*x)),[-1,0,1]],
 [x=>Math.exp(2*x)/Math.log(x),x=>Math.exp(2*x)*(2*x*Math.log(x)-1)/(x*Math.log(x)**2),[.2,2,3]],
 [x=>Math.log(x*(x*x-3)**2/Math.sqrt(x*x-4)),x=>4*(x**4-5*x*x+3)/(x*(x*x-3)*(x*x-4)),[2.5,3,5]],
 [x=>x**Math.sin(x),x=>x**Math.sin(x)*(Math.cos(x)*Math.log(x)+Math.sin(x)/x),[.2,1,3]]
];
for(const [f,d,points] of expChecks)for(const x of points){const h=1e-6,n=(f(x+h)-f(x-h))/(2*h),expected=d(x);assert(Math.abs(n-expected)<1e-5*Math.max(1,Math.abs(expected)),'Exponential independent derivative mismatch');}
assert.equal(chapters[2].workedExamples.filter(e=>e.progressiveSolution&&e.solutionOrigin).length,23);
assert.equal(chapters[2].sections[7].id,'sec-3-8');assert.equal(chapters[2].sections[6].unreviewedTheory,'');
assert.deepEqual(chapters[2].exercises.map(e=>e.problems.length),[8,6,9,5,7,1,10]);
assert.deepEqual(chapters[2].exercises.slice(0,5).map(e=>e.title),['Exercise 3.1','Exercise 3.2','Exercise 3.3','Exercise 3.4','Exercise 3.5']);
assert.equal(chapters[2].sourceSummaryReferences[0].page,100);
assert(chapters[2].exercises[4].problems[2].sourceClarification.includes('no real domain'));
assert(chapters[2].exercises[6].problems[5].answer.includes('also (a)'));
assert(chapters[2].exercises[6].problems[6].answer.includes('also (d)'));
const closingChecks=[
 [x=>Math.cosh(2*x*x-1),x=>4*x*Math.sinh(2*x*x-1),[.1,.8,1.2]],
 [x=>1/Math.cosh((1-x)/(1+x)),x=>2*Math.tanh((1-x)/(1+x))/((1+x)**2*Math.cosh((1-x)/(1+x))),[-2,.2,1.2]],
 [x=>Math.asinh(x**3),x=>3*x*x/Math.sqrt(1+x**6),[-2,0,2]],
 [x=>Math.asinh(x)/Math.acosh(x),x=>1/(Math.sqrt(x*x+1)*Math.acosh(x))-Math.asinh(x)/(Math.sqrt(x*x-1)*Math.acosh(x)**2),[1.2,2,3]],
 [x=>11**(3-4*x**3),x=>-12*x*x*11**(3-4*x**3)*Math.log(11),[.1,.4,.7]],
 [x=>x**5*Math.exp(1/x),x=>(5*x**4-x**3)*Math.exp(1/x),[-2,.7,2]],
 [x=>Math.exp(2*x)/(Math.exp(-2*x)+1),x=>2*(Math.exp(2*x)+2)/(Math.exp(-2*x)+1)**2,[-1,0,1]],
 [x=>Math.log(Math.exp(2*x)-Math.exp(-2*x)),x=>2/Math.tanh(2*x),[.2,.7,2]],
 [x=>(Math.exp(2*x)-Math.exp(-2*x))/(Math.exp(2*x)+Math.exp(-2*x)),x=>2/Math.cosh(2*x)**2,[-1,0,1]],
 [x=>x**3*Math.log(Math.sqrt(x)),x=>x*x*(1+3*Math.log(x))/2,[.2,1,3]],
 [x=>x*x*Math.sqrt(Math.log(x)),x=>x*(4*Math.log(x)+1)/(2*Math.sqrt(Math.log(x))),[1.2,2,3]],
 [x=>Math.log(Math.sqrt((x*x+1)/(x*x-1))),x=>2*x/(1-x**4),[-2,1.2,3]],
 [x=>Math.log(Math.abs(x-Math.sqrt(x*x+1))),x=>-1/Math.sqrt(x*x+1),[-2,0,2]],
 [x=>Math.exp(-2*x)*Math.cos(2*x),x=>-2*Math.exp(-2*x)*(Math.cos(2*x)+Math.sin(2*x)),[-1,0,1]],
 [x=>x*x*Math.exp(Math.sin(x)),x=>x*Math.exp(Math.sin(x))*(x*Math.cos(x)+2),[-1,0,1]],
 [x=>Math.asinh(Math.cos(x)),x=>-Math.sin(x)/Math.sqrt(1+Math.cos(x)**2),[-1,0,1]],
 [x=>Math.atanh(x/2),x=>2/(4-x*x),[-1,0,1]],
 [x=>Math.log(1/Math.tanh(x)),x=>-2/Math.sinh(2*x),[.2,.7,2]],
 [x=>x*Math.acosh(x)-Math.sqrt(x*x-1),x=>Math.acosh(x),[1.2,2,3]],
 [x=>(x**4+2*x+16)/(x**3+3*x-2),x=>(4*x**3+2)/(x**3+3*x-2)-(x**4+2*x+16)*(3*x*x+3)/(x**3+3*x-2)**2,[-2,.2,2]],
 [x=>x**3+Math.sin(x)**2+Math.acos(x),x=>3*x*x+2*Math.sin(x)*Math.cos(x)-1/Math.sqrt(1-x*x),[-.7,0,.7]],
 [x=>x*x*Math.cosh(x)+Math.asinh(x),x=>2*x*Math.cosh(x)+x*x*Math.sinh(x)+1/Math.sqrt(1+x*x),[-1,0,1]]
];
for(const [f,d,points] of closingChecks)for(const x of points){const h=1e-6,n=(f(x+h)-f(x-h))/(2*h),expected=d(x);assert(Math.abs(n-expected)<1e-5*Math.max(1,Math.abs(expected)),'Closing Unit 3 derivative mismatch at '+x);}
assert(Math.abs(5000*2**10*2*Math.log(2)-7097827.1289338395)<1e-7);
assert(Math.abs(4*Math.PI*3**2-36*Math.PI)<1e-12);
const higher=chapters[3];assert.equal(higher.sourcePages.length,29);assert.equal(higher.sourcePages[0].objectives.length,4);assert.equal(higher.sections[0].unreviewedTheory,'');
for(let n=1;n<=31;n++){const e=higher.workedExamples.find(e=>e.num===String(n));assert(e.progressiveSolution&&e.steps.length>=7,'Unit 4 example incomplete '+n);assert.equal(higher.workedExamples.filter(e=>e.num===String(n)).length,1);}
assert(higher.workedExamples.find(e=>e.num==='5').sourceClarification.includes('chain factor'));
assert(higher.sourcePages.find(p=>p.page===108).blocks.filter(b=>b.type==='command'&&b.text&&b.text.startsWith('diff')).length===3);
for(const t of [-2,-.5,.5,2]){const h=1e-6,first=t=>(3*t+4)/2;assert(Math.abs((first(t+h)-first(t-h))/(2*h)/(2*t)-3/(4*t))<1e-8);}
// Check corrected implicit derivative against the curve parametrized by y.
for(const y of [.2,.5,.8]){const x=y=>(Math.acos(y)+y)/(2*y),h=1e-5,x1=(x(y+h)-x(y-h))/(2*h),x2=(x(y+h)-2*x(y)+x(y-h))/(h*h),s=Math.sqrt(1-y*y),A=1-2*x(y)-1/s,expected=8*y/A**2+4*y**3/(s**3*A**3);assert(Math.abs(-x2/x1**3-expected)<1e-5,'Implicit second derivative mismatch');}
assert.equal(15120*6**5,117573120);assert.equal(120*4**5,122880);assert.equal(24*4**5,24576);
assert.deepEqual(higher.exercises.slice(0,2).map(e=>e.problems.length),[8,8]);
assert(higher.exercises[1].problems[6].sourceClarification.includes('singular'));
for(const x of [-.4,.1,.3]){const h=1e-6,U=Math.sqrt(1/Math.cos(2*x)),T=Math.tan(2*x),second=x=>Math.sqrt(1/Math.cos(2*x))*(2+3*Math.tan(2*x)**2),n=(second(x+h)-second(x-h))/(2*h);assert(Math.abs(n-U*(14*T+15*T**3))<1e-5);}
for(const t of [-.5,.2,1,2]){const h=1e-6,a=2,slope=t=>t*(2-t**3)/(1-2*t**3),xp=3*a*(1-2*t**3)/(1+t**3)**2,n=(slope(t+h)-slope(t-h))/(2*h)/xp,expected=2*(1+t**3)**4/(3*a*(1-2*t**3)**3);assert(Math.abs(n-expected)<1e-5);}
for(const sign of [-1,1]){const x=(4+sign*Math.sqrt(91))/15,y=(-128+sign*43*Math.sqrt(91))/675;assert(Math.abs(y-(5*x**3-4*x*x))<1e-12);assert(Math.abs(15*x*x-8*x-5)<1e-12);}
assert(Math.abs(Math.atan(6/41)-.14531001063570212)<1e-15);
assert.equal(higher.exercises[2].problems.length,10);assert.equal(higher.exercises[3].problems.length,10);assert(higher.sourceSummaryBlocks.some(b=>b.type==='figure'));assert(higher.exercises[3].problems[7].answer.includes('also b'));
for(const x of [-2,0,1,3,5]){const derivative=6*(x+2)*(x-1);assert.equal(Math.sign(derivative)||0,x<-2||x>1?1:x===-2||x===1?0:-1);}
assert(Math.abs((8000/Math.sqrt(800)+10*Math.sqrt(800))-400*Math.SQRT2)<1e-10);
assert(Math.abs((450/Math.sqrt(150)+3*Math.sqrt(150))-30*Math.sqrt(6))<1e-10);
assert.equal(80+108*6-6**3,512);assert.equal(-(10**3)+9*10**2+120*10-400,700);


const vector=chapters[4];assert.equal(vector.sourcePages.length,12);assert.equal(vector.sourcePages[0].objectives.length,4);assert.equal(vector.sections[0].unreviewedTheory,'');assert.equal(vector.sections[1].unreviewedTheory,'');for(let i=1;i<=5;i++){const ex=vector.workedExamples.find(e=>Number(e.num)===i);assert(ex&&ex.progressiveSolution&&ex.steps.length>=7);}assert(vector.sourcePages.find(p=>p.page===133).blocks.some(b=>b.type==='figure'));

assert.equal(vector.exercises.find(e=>e.title==='Exercise 5.1').problems.length,4);

for(let i=8;i<=12;i++)assert(vector.workedExamples.find(e=>Number(e.num)===i).steps.length>=7);assert(vector.workedExamples.find(e=>e.num==='12').answer.includes('3.003962967'));

assert.equal(vector.exercises.find(e=>e.title==='Exercise 5.2').problems.length,5);assert(vector.workedExamples.find(e=>e.num==='13').steps.length>=7);

assert.equal(vector.exercises.find(e=>e.title==='Review Exercise 5').problems.length,10);assert(vector.sourceSummaryBlocks.filter(b=>b.type==='figure').length===2);

const integration=chapters[5];assert.equal(integration.sourcePages.length,20);assert.equal(integration.sourceGap.pageStart,142);assert.equal(integration.sourceGap.pageEnd,157);for(const num of ['9','10'])assert(integration.workedExamples.find(e=>e.num===num).steps.length>=7);

assert.equal(integration.exercises.find(e=>e.title==='Exercise 6.2').problems.length,3);

assert.equal(integration.exercises.find(e=>e.title==='Exercise 6.3').problems.length,4);

assert.equal(integration.sourcePages.filter(p=>p.page>=166&&p.page<=168).flatMap(p=>p.blocks).filter(b=>b.type==='diagram').length,5);

assert.equal(integration.exercises.find(e=>e.id==='ex-6-integral-property-challenges').problems.length,4);

for(const n of ['20','21'])assert.equal(integration.workedExamples.filter(e=>e.num===n).length,1);assert.equal(ledger.pages.find(p=>p.jpg==='091_page_2.jpg').duplicateOf,'075_page_2.jpg');

assert.equal(integration.exercises.find(e=>e.title==='Exercise 6.4').problems.length,6);assert.equal(integration.exercises.find(e=>e.title==='Exercise 6.4').problems[3].sourceQuestionBlocks.length,4);

assert.equal(integration.exercises.find(e=>e.title==='Review Exercise 6').problems.length,10);assert(integration.sourceSummaryBlocks.length>12);assert.equal(integration.sections[2].title,'6.3 Integration by Substitution');

const straight=chapters[6];assert.equal(straight.sourcePages.length,35);assert.equal(straight.sourcePages[0].objectives.length,9);
for(let n=1;n<=30;n++){const matches=straight.workedExamples.filter(e=>Number(e.num)===n);assert.equal(matches.length,1,'Reviewed example must occur once: '+n);const e=matches[0];assert.equal(e.problem,e.question,'Reviewed source question must be displayed');assert(e.steps.length>=6&&e.progressiveSolution&&e.answer&&e.sourceReferences.length);}
for(const [title,count] of [['Exercise 7.1',5],['Exercise 7.2',8],['Exercise 7.3',8],['Project — Home and School Midpoint',1]])assert.equal(straight.exercises.find(e=>e.title===title).problems.length,count);
assert.equal(straight.exercises.find(e=>e.title==='Exercise 7.2').problems[0].sourceQuestionBlocks.length,3);
assert(straight.workedExamples.find(e=>e.num==='23').answer.includes('x+8y−25'));assert(straight.workedExamples.find(e=>e.num==='24').answer.includes('34x+8y−99'));

assert.equal(straight.exercises.find(e=>e.title==='Exercise 7.4').problems.length,8);
assert(straight.exercises.find(e=>e.title==='Exercise 7.4').problems[1].answer.includes('not concurrent'));
assert.equal(straight.exercises.find(e=>e.title==='Review Exercise 7').problems.length,10);
assert(straight.sourceSummaryBlocks.length>20);
assert.equal(chapters[7].sourcePages.length,28);
assert.equal(chapters[7].sourceObjectives.flatMap(g=>g[1]).length,21);
for(let n=1;n<=19;n++){const es=chapters[7].workedExamples.filter(e=>Number(e.num)===n);assert.equal(es.length,1);assert(es[0].problem===es[0].question&&es[0].steps.length>=6&&es[0].progressiveSolution);}
assert.equal(chapters[7].exercises.find(e=>e.title==='Exercise 8.1').problems.length,8);
assert.equal(chapters[7].exercises.find(e=>e.title==='Exercise 8.2').problems.length,12);
assert.equal(chapters[7].exercises.find(e=>e.title==='Exercise 8.3').problems.length,6);
assert.equal(chapters[7].exercises.find(e=>e.title==='Review Exercise 8').problems.length,10);
assert(chapters[7].sourceSummaryBlocks.length>20);
assert.equal(chapters[8].sourcePages.length,45);
assert.equal(chapters[8].sourceObjectives.length,4);
for(let n=1;n<=31;n++){const es=chapters[8].workedExamples.filter(e=>Number(e.num)===n);assert.equal(es.length,1);assert(es[0].problem===es[0].question&&es[0].steps.length>=6&&es[0].progressiveSolution);}
assert.equal(chapters[8].exercises.find(e=>e.title==='Exercise 9.1').problems.length,10);
assert.equal(chapters[8].exercises.find(e=>e.title==='Exercise 9.2').problems.length,7);
assert.equal(chapters[8].exercises.find(e=>e.title==='Exercise 9.3').problems.length,9);
assert.equal(chapters[8].exercises.find(e=>e.title==='Exercise 9.4').problems.length,4);assert.equal(chapters[8].exercises.length,4);assert(chapters[8].sourceSummaryBlocks.length>50);
assert.equal(chapters[9].sourcePages.length,14);assert.equal(chapters[9].sourceObjectives.length,4);
for(let n=1;n<=12;n++){const es=chapters[9].workedExamples.filter(e=>Number(e.num)===n);assert.equal(es.length,1);assert(es[0].problem===es[0].question&&es[0].steps.length>=6&&es[0].progressiveSolution);}
assert.equal(chapters[9].exercises.find(e=>e.title==='Exercise 10.1').problems.length,5);
assert.equal(chapters[9].exercises.find(e=>e.title==='Exercise 10.2').problems.length,11);
assert.equal(chapters[9].exercises.find(e=>e.title==='Review Exercise 10').problems.length,7);assert(chapters[9].sourceSummaryBlocks.length>15);
assert.equal(chapters[10].sourcePages.length,9);assert.equal(chapters[10].sourceObjectives.length,2);assert.equal(chapters[10].workedExamples[0].problem,chapters[10].workedExamples[0].question);
assert.equal(chapters[10].exercises.find(e=>e.title==='Exercise 11.1').problems.length,6);
for(let n=1;n<=8;n++){const e=chapters[10].workedExamples.find(e=>Number(e.num)===n);assert(e.problem===e.question&&e.steps.length>=6&&e.progressiveSolution);}
assert.equal(chapters[10].exercises.find(e=>e.title==='Exercise 11.2').problems.length,6);assert.equal(chapters[10].exercises.find(e=>e.title==='Review Exercise 11').problems.length,9);assert(chapters[10].sourceSummaryBlocks.length>10);
assert.equal(chapters[11].sourcePages.length,17);assert.equal(chapters[11].sourceObjectives.length,2);
for(let n=1;n<=7;n++){const e=chapters[11].workedExamples.find(e=>Number(e.num)===n);assert(e.problem===e.question&&e.steps.length>=6&&e.progressiveSolution);}
assert.equal(chapters[11].exercises.find(e=>e.title==='Exercise 12.1').problems.length,7);
assert.equal(chapters[11].exercises.find(e=>e.title==='Exercise 12.2').problems.length,5);assert(chapters[11].exercises.find(e=>e.title==='Exercise 12.2').problems[4].solutionStatus.startsWith('partial:'));
assert.equal(chapters[11].exercises.find(e=>e.title==='Review Exercise 12').problems.length,10);assert.equal(chapters[11].exercises.find(e=>e.title==='Project').problems.length,2);assert.equal(chapters[11].exercises.length,4);assert(chapters[11].sourceSummaryBlocks.length>10);
console.log(JSON.stringify({ trackedJpgs: images.length, reviewedSourcePages: pages.length, reviewedPrintedPages:reviewedPrintedPages.length, bookStatus:ledger.bookStatus, result:'passed' }));
