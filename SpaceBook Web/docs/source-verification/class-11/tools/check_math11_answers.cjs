const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const app=path.resolve(__dirname,'../../../..');
const katex=require(path.join(app,'assets/vendor/katex/katex.min.js'));
const context={console,katex,state:{selectedClass:'cls11',activeMathSloCategory:'mcqs'}};
context.window=context;
vm.createContext(context);
for(const name of ['math_11_data.js','math_11_solutions.js','lesson_math_reader.js','math11_reader.js'])
 vm.runInContext(fs.readFileSync(path.join(app,'js',name),'utf8'),context,{filename:name});
const unitNo=Number(process.argv[2]||1);
const expected={1:{leaves:85,mcqs:7},2:{leaves:72,mcqs:6},3:{leaves:78,mcqs:8}}[unitNo];
assert(expected,'No independently reviewed coverage count for this unit');
const unit=context.MATH_11_DATA.find(x=>x.number===unitNo), reader=context.MATH11_READER;
const authored=JSON.parse(fs.readFileSync(path.join(__dirname,'../math/authored-solutions.json'),'utf8'));
const seen=new Set();let formulas=0,leaves=0;
function renderCheck(tex){try{katex.renderToString(tex,{throwOnError:true,strict:'ignore'});}catch(e){throw new Error(e.message+'\nFormula: '+tex);}}
function checkMath(value){for(const p of context.SpaceBookLessonMath.mathParts(value||''))if(p.latex!==undefined){renderCheck(p.latex);formulas++;}}
const walk=bs=>(bs||[]).forEach(q=>{
 if(q.t==='q')for(const owner of q.parts.length?q.parts:[q]){
  leaves++; assert(owner.authoredAnswer&&owner.solId,'missing answer '+q.no+' '+owner.no);
  const sol=context.MATH_11_SOLUTIONS[owner.solId];assert(sol&&sol.steps.length,'missing steps');
  assert(!seen.has(owner.answerKey),'duplicate answer key');seen.add(owner.answerKey);
  assert.strictEqual(owner.authoredAnswer.en,authored[owner.answerKey].answer);
  checkMath(sol.answer);
  for(const step of sol.steps){for(const lang of ['en','ur','ps']){assert(step[lang]);checkMath(step[lang]);}assert(/[\u0600-\u06ff]/.test(step.ur)&&/[\u0600-\u06ff]/.test(step.ps),'native translation');if(step.m){renderCheck(step.m);formulas++;}}
 }
 if(q.blocks)walk(q.blocks);
});
unit.exercises.forEach(ex=>walk(ex.blocks));
assert.strictEqual(leaves,expected.leaves);assert.strictEqual(seen.size,expected.leaves);
const html=reader.exercises(unit),lesson=reader.lesson(unit);
for(const key of seen){const needle='data-answer-key="'+key+'"';assert.strictEqual(html.split(needle).length-1,1,'exercise answer visibility '+key);assert.strictEqual(lesson.split(needle).length-1,1,'lesson answer visibility '+key);}
assert(html.includes('SpaceBook answer:')&&!html.includes('Textbook answer:'),'authored provenance');
assert(!html.includes('(i))'),'source numbering');
assert(!/katex-error|<img|<iframe|<embed/.test(html),'math and coded content');
assert(lesson.includes('data-w='),'interactive word meanings');
const bank=context.getMath11QuestionBank(unit);assert.strictEqual(bank.mcqs.length,expected.mcqs);
for(const cat of ['mcqs','lqs','sqs']){context.state.activeMathSloCategory=cat;const out=reader.slos(unit);assert(out.includes('category-sub-tabs-bar'));assert(!out.includes('order (dimension)'),'no Class 9 matrix fallback');assert(!out.includes('katex-error'));}
assert(context.MATH_11_BOOK.complete===false,'whole book remains incomplete');
assert(Object.keys(context.MATH_11_WORDS).length>=90);
const controller=fs.readFileSync(path.join(app,'js/app.js'),'utf8');
assert(controller.includes("if (state.selectedClass === 'cls11') return typeof window.getMath11QuestionBank"),'scoped question bank route');
assert(controller.includes("classId === 'cls9' || classId === 'cls11'"),'no null PDF link for Class 11');
const sourceScans=[...new Set([...seen].flatMap(key=>authored[key].sourceCheckedPdfPages))].sort((a,b)=>a-b);
const report={date:'2026-10-18',unit:unitNo,answeredLeaves:leaves,mcqs:bank.mcqs.length,checkedMathExpressions:formulas,wordMeanings:Object.keys(context.MATH_11_WORDS).length,sourcePagesRepresented:context.MATH_11_BOOK.reviewedPdfPages,totalSourcePages:432,wholeBookComplete:false,sourceScans,scope:'Exercise answers: source scan comparison, symbolic arithmetic checks in authoring scripts, native-language steps, direct reader HTML and category routing; no browser tests.'};
fs.writeFileSync(path.join(__dirname,'../math/unit'+unitNo+'-answer-review.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
