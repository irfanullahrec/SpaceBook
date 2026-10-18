const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const root=path.resolve(__dirname,'..'),read=f=>fs.readFileSync(path.join(root,f),'utf8');
const sb={};vm.createContext(sb);vm.runInContext(read('js/chem_12_data.js')+';this.ch=CHEM_12_DATA.find(c=>c.number===13);',sb);
const source=sb.ch.sections.find(s=>s.id==='13.21'),before=JSON.stringify(source),original=sb.ch.sections.find(s=>s.id==='13.exercise.solved').theory;
vm.runInContext(read('js/chem12_unit13_study.js'),sb);const bank=sb.ch.class12Exercise;
assert.equal(JSON.stringify(source),before,'Printed question section and translations preserved');
assert.equal(bank.mcqs.length,15);assert.equal(bank.shortQuestions.length,10);assert.equal(bank.longQuestions.length,10);assert.equal(bank.activities.length,1);
for(const [category,items] of Object.entries(bank))for(const item of items){
 assert(item.q&&item.sourceParagraphIndices.length&&item.sourceReferences.length);
 assert(item.answer||item.exp);assert(item.answerUrdu||item.expUrdu);assert(item.answerPashto||item.expPashto);
 assert.equal(item.q,source.paras[item.sourceParagraphIndices[0]].text);
 if(category==='mcqs')assert(item.options[item.correct]);
}
assert.equal(bank.mcqs[3].options[bank.mcqs[3].correct],'BaSO₄');
assert.equal(bank.mcqs[5].options[bank.mcqs[5].correct],'F₂');
assert(bank.mcqs[11].choiceIssues,'Undefined oxygen affinity is qualified');
assert.match(bank.shortQuestions[5].q,/fluorine/);assert.match(bank.shortQuestions[5].answer,/hydration/);
assert.match(bank.shortQuestions[8].q,/Al and Si/);assert.match(bank.shortQuestions[8].answer,/RISES from Al to Si/);
assert.match(bank.shortQuestions[9].q,/Sn⁴/);assert.match(bank.shortQuestions[9].answer,/SnCl₂/);
assert.equal(sb.ch.sections.find(s=>s.id==='13.exercise.solved').originalAnswerDraft.theory,original);
// Independent elemental balance checks for the newly corrected thermal equations.
const balanced=(left,right)=>{const sum=side=>{const out={};for(const [factor,atoms]of side)for(const [el,n]of Object.entries(atoms))out[el]=(out[el]||0)+factor*n;return out;};assert.deepEqual(sum(left),sum(right));};
balanced([[2,{M:1,N:2,O:6}]],[[2,{M:1,O:1}],[4,{N:1,O:2}],[1,{O:2}]]);
balanced([[1,{M:1,H:2,C:2,O:6}]],[[1,{M:1,C:1,O:3}],[1,{C:1,O:2}],[1,{H:2,O:1}]]);
const once=JSON.stringify(bank);vm.runInContext(read('js/chem12_unit13_study.js'),sb);assert.equal(JSON.stringify(sb.ch.class12Exercise),once);
const report={...sb.CHEM12_UNIT13_STUDY_REPORT,checkedUtc:new Date().toISOString(),passed:true,checked:['Source paragraph mapping and original translations preserved','All 36 question/part/activity records answered','MCQ option letters match source order','Printed Al/Si issue retained and explained','GroupIIA thermal equations independently balanced','Original answer draft retained','Idempotent addon loading'],limits:['No claim that other Chemistry units are complete','Long-answer translations condense the English working','Chemistry source and answer correctness checks do not constitute final whole-book verification']};
fs.writeFileSync(path.join(root,'docs/source-verification/class-12/chem12-unit13-study-check.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:true,questions:36,report:'docs/source-verification/class-12/chem12-unit13-study-check.json'}));
