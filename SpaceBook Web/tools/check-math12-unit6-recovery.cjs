const fs=require('node:fs');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const read=file=>fs.readFileSync(path.join(root,file),'utf8');
const context=vm.createContext({
  console,window:{},
  sanitize:value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])),
  renderMathDiagram:()=>{throw new Error('Unexpected diagram in recovered pages');}
});
vm.runInContext(read('js/math_12_data.js'),context);
const original=vm.runInContext('JSON.stringify(MATH_12_DATA[5].sourcePages)',context);
vm.runInContext(read('js/math12_unit6_source_recovery.js'),context);
vm.runInContext(read('js/math12_unit6_exercise61_recovery.js'),context);
const unit=vm.runInContext('MATH_12_DATA[5]',context);
assert.equal(JSON.stringify(unit.sourcePages.filter(page=>page.page>=158)),original,'Supplied source pages changed');
assert.deepEqual(Array.from(unit.sourcePages.slice(0,16),page=>page.page),Array.from({length:16},(_,i)=>142+i));
assert.equal(unit.sourceGap,null);
for(let n=1;n<=8;n++){
  const e=unit.workedExamples.find(item=>item.id==='we-6-source-'+n);
  assert(e?.problem&&e?.answer&&e?.steps?.length,'Incomplete recovered example '+n);
}
const challenge=unit.exercises.find(item=>item.id==='ex-6-recovered-substitution-challenges');
assert.equal(challenge.problems.length,5);
assert(challenge.problems.every(p=>p.question&&p.answer&&p.solution));
const exercise=unit.exercises.find(item=>item.id==='ex-6-5');
assert.equal(exercise.problems.length,8);
assert(exercise.problems.every(p=>p.question&&p.answer&&p.solution));
const app=read('js/app.js');
const start=app.indexOf('function renderMathSourceBlocks(');
const end=app.indexOf('function renderMathSourceOpening(',start);
assert(start>=0&&end>start);
vm.runInContext(app.slice(start,end),context);
vm.runInContext(read('js/math12_translation_reader.js'),context);
const sections=unit.sections.filter(s=>['sec-6-1','sec-6-2','sec-6-3'].includes(s.id));
const renderResults=[];
for(const section of sections){
  context.recoveredBlocks=section.sourceBlocks;
  const html=vm.runInContext('renderMathSourceBlocks(recoveredBlocks)',context);
  assert(!html.includes('undefined'));
  const translated=section.sourceBlocks.filter(block=>block.sentenceTranslations);
  for(const block of translated){
    assert(block.sentenceTranslations.every(p=>p.en&&p.ur&&p.ps));
  }
  assert.equal((html.match(/<p lang="ur"/g)||[]).length,translated.length);
  assert.equal((html.match(/<p lang="ps"/g)||[]).length,translated.length);
  renderResults.push({section:section.id,blocks:section.sourceBlocks.length,translatedPassages:translated.length,renderedCharacters:html.length});
}
const sourceCount=unit.sourcePages.length;
const exampleCount=unit.workedExamples.length;
vm.runInContext(read('js/math12_unit6_source_recovery.js'),context);
assert.equal(unit.sourcePages.length,sourceCount,'Source addon is not idempotent');
assert.equal(unit.workedExamples.length,exampleCount,'Examples duplicated on repeated execution');
const report={
  date:new Date().toISOString(),passed:true,
  recoveredPages:16,sourcePagesPreserved:20,recoveredExamples:8,
  exercise61Groups:exercise.problems.length,exercise61Subparts:28,answeredChallenges:5,
  renderResults,
  limitations:'Focused runtime/HTML checks only; final browser verification and complete translation of worked solutions are separate.'
};
fs.writeFileSync(path.join(root,'docs/source-verification/class-12/math12-unit6-recovery-render-checks.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
