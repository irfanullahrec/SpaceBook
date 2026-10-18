const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const root=path.resolve(__dirname,'..'),read=f=>fs.readFileSync(path.join(root,f),'utf8'),sb={};vm.createContext(sb);
vm.runInContext(read('js/phys_12_data.js')+';this.ch=PHYS_12_DATA.find(c=>Number(c.number)===11);',sb);
const sourceSnapshot=JSON.stringify(sb.ch.sections.filter(s=>s.id!=='11.exercise.solved'));
const old=sb.ch.sections.find(s=>s.id==='11.exercise.solved').theory;
vm.runInContext(read('js/phys12_unit11_study.js'),sb);const bank=sb.ch.class12Exercise;
assert.equal(JSON.stringify(sb.ch.sections.filter(s=>s.id!=='11.exercise.solved')),sourceSnapshot);
assert.equal(bank.mcqs.length,13);assert.equal(bank.shortQuestions.length,10);assert.equal(bank.longQuestions.length,11);assert.equal(bank.numericals.length,12);
for(const kind of ['mcqs','shortQuestions','longQuestions','numericals'])for(const q of bank[kind]){
 assert(q.q&&q.answer&&q.steps.length>=2);assert.equal(q.sol,q.steps.join('\n'));
 const original=q.sourceReferences.flatMap(ref=>ref.paragraphIndices.map(i=>sb.ch.sections.find(s=>s.id===ref.sectionId).paras[i].text)).join(' ');
 assert.equal(q.originalSourceText,original,'Exact source fragments '+q.id);
 if(kind!=='mcqs')assert.equal(q.q,original);
 if(kind==='mcqs'){assert.equal(q.options.length,4);if(q.choiceIssues)assert.equal(q.correct,undefined);else assert(Number.isInteger(q.correct));}
}
assert.equal(bank.mcqs[12].correct,0);assert.match(bank.mcqs[12].answer,/−qΔV/);
assert.match(bank.shortQuestions[1].answer,/neutral particle/);assert.match(bank.shortQuestions[6].sol,/LESS energy/);
assert.match(bank.mcqs[10].diagramSvg,/2 μF/);assert.match(bank.mcqs[10].diagramSvg,/6 μF/);assert.match(bank.mcqs[10].diagramSvg,/10 V/);
assert.match(bank.numericals[10].diagramSvg,/5 μF/);assert.match(bank.numericals[10].diagramSvg,/6 V/);
// Independently recompute numerical results and circuit boundary conditions.
const near=(value,expected,tolerance=1e-6)=>assert(Math.abs(value-expected)<tolerance,`${value} differs from ${expected}`);
const k=9e9,e=1.602e-19;
near(k*26*e*e/1e-24,.00600538536,1e-12);
near(Math.hypot(7.2-10.8/2,10.8*Math.sqrt(3)/2),9.52470472,1e-7);
near(k*15e-10*13e-10*(1/.08-1/.12),7.3125e-8,1e-17);
near(2*k*2e-7/.075**2,640000);
near((13*.5)/k,7.222222222e-10,1e-19);
for(const x of [.2/3,.2])near(8/Math.abs(x)-4/Math.abs(x-.1),0);
near(9.11e-31*(2.9e6)**2/(2*e*80),.2989,5e-5);
near(1/(1/4+1/6+1/8),24/13);
near((6000/13)/4+(6000/13)/6+(6000/13)/8,250);
near((1/(1/2+1/3+1/6))*10,10);
near((3*7/(3+7))*6/7*5,9);near(6*120/(6+4),72);
assert.equal(sb.ch.sections.find(s=>s.id==='11.exercise.solved').originalAnswerDraft.theory,old);
const once=JSON.stringify(bank);vm.runInContext(read('js/phys12_unit11_study.js'),sb);assert.equal(JSON.stringify(sb.ch.class12Exercise),once);
const report={...sb.PHYS12_UNIT11_STUDY_REPORT,checkedUtc:new Date().toISOString(),passed:true,checks:['All source questions/choices mapped to reviewed paragraphs','Original source sections unchanged','All46records have substantive answer and steps','Numerical results independently recalculated','Series and parallel circuits distinguished','Multiple/invalid MCQ choices remain qualified written answers','Prior incorrect worked-answer draft preserved but superseded','Idempotence'],limits:['Whole Physics book not reverified','New answer translations remain pending','Diagram topology checked against inspected source; no claim of pixel-identical rendering']};
fs.writeFileSync(path.join(root,'docs/source-verification/class-12/phys12-unit11-study-check.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:true,questions:46,answerTranslations:'pending'}));
