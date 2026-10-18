const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'..'),app=path.resolve(root,'../../..');
const katex=require(path.join(app,'assets/vendor/katex/katex.min.js'));
const c={console,katex,state:{selectedClass:'cls11',activeMathSloCategory:'mcqs'}};c.window=c;vm.createContext(c);
for(const f of ['math_11_data.js','math_11_solutions.js','lesson_math_reader.js','math11_reader.js'])vm.runInContext(fs.readFileSync(path.join(app,'js',f),'utf8'),c);
const first=Number(process.argv[2]||192),last=Number(process.argv[3]||196);
assert((first===192&&last===196)||(first===197&&last===201)||(first===202&&last===206),'Unreviewed batch');
const unit=c.MATH_11_DATA.find(u=>u.number===6);
const exercises=unit.exercises.filter(e=>(first===192?['6.4']:first===202?['6.5','Review 6']:[]).includes(e.id));
const qs=exercises.flatMap(e=>e.blocks.filter(b=>b.t==='q'));
if(first===192)assert.deepStrictEqual(Array.from(qs,q=>q.parts.length),[5,2,4,6,2,5,10]);
let expressions=0,pairs=0,currentPage=0;const svgs=[],pages=new Set(),missingWords=new Set();
function math(tex){try{katex.renderToString(tex,{throwOnError:true,strict:'ignore'});expressions++;}catch(e){throw new Error(e.message+'\n'+tex);}}
function text(str){for(const part of c.SpaceBookLessonMath.mathParts(str||''))if(part.latex!==undefined)math(part.latex);}
function paired(rec){
 if(!rec||!rec.en)return;
 assert(rec.ur&&rec.ps,'Missing paired translation: '+rec.en);
 for(const lang of ['en','ur','ps'])text(rec[lang]);
 const prose=c.SpaceBookLessonMath.mathParts(rec.en).filter(p=>p.latex===undefined).map(p=>p.text).join(' ');
 if(/[A-Za-z]{2}/.test(prose)){assert(/[\u0600-\u06ff]/.test(rec.ur)&&/[\u0600-\u06ff]/.test(rec.ps),'Missing native text');}
 for(const word of prose.toLowerCase().match(/[a-z]+(?:'[a-z]+)?/g)||[]){
  if(word.length>1&&!/^(i|ii|iii|iv|v|vi|vii|viii|ix|x)$/.test(word)&&!c.MATH_11_WORDS[word])missingWords.add(word);
 }
 pairs++;
}
function walk(bs){for(const b of bs){
 if(b.t==='page'){currentPage=b.pdf;if(currentPage>=first+1&&currentPage<=last+1)pages.add(currentPage);}
 if(currentPage>=first+1&&currentPage<=last+1){
  if(b.en)paired(b);if(b.cap)paired(b.cap);if(b.title&&typeof b.title==='object')paired(b.title);
  if(b.tex)math(b.tex);for(const p of b.parts||[])paired(p);for(const item of b.items||[])paired(item);
  if(b.svg){svgs.push(b.svg);assert(!/<image|<script|<foreignObject/.test(b.svg));}
 }
 if(b.blocks)walk(b.blocks);
}}
for(const u of c.MATH_11_DATA)for(const s of u.sections)walk(s.blocks);
assert.strictEqual(pages.size,5);assert.strictEqual(svgs.length,first===197?0:3);
assert.strictEqual(missingWords.size,0,'Missing word meanings: '+[...missingWords].join(', '));
let answers=0;
for(const q of qs)for(const p of q.parts.length?q.parts:[q]){
 assert(p.authoredAnswer&&p.solId);const sol=c.MATH_11_SOLUTIONS[p.solId];
 text(sol.answer);for(const s of sol.steps){paired(s);if(s.m)math(s.m);}
 answers++;
}
assert.strictEqual(answers,first===192?34:first===202?41:0);
const html=exercises.map(e=>c.MATH11_READER.blocks(e.blocks,{showAnswers:true})).join('');
for(const q of qs)for(const p of q.parts.length?q.parts:[q])assert(html.includes('data-answer-key="'+p.answerKey+'"'));
assert(!html.includes('katex-error'));
const ledger=JSON.parse(fs.readFileSync(path.join(root,'math/ledger.json'),'utf8'));
for(const p of ledger.filter(p=>p.pdfPage>=first+1&&p.pdfPage<=last+1))assert.strictEqual(p.untranslated.length,0);
const ocrComparison=[];
for(let index=first;index<=last;index++){
 const src=fs.readFileSync(path.join(root,'math/pages/p'+index+'.txt'),'utf8');
 const english=src.split('\n').filter(l=>/^(p |q |qp |example |svg |box |slo |@sec |#)/.test(l)).map(l=>l.split(' || ')[0].replace(/\$[^$]+\$/g,' ')).join(' ').toLowerCase();
 const ocr=fs.readFileSync(path.join(root,'math/ocr/p'+index+'.txt'),'utf8').toLowerCase();
 const terms=new Set(ocr.match(/[a-z]{4,}/g)||[]);
 const matched=[...terms].filter(w=>english.includes(w));
 ocrComparison.push({scan:index+1,ocrWordTypes:terms.size,matched:matched.length,unmatched:[...terms].filter(w=>!english.includes(w)),note:'OCR comparison supplements visual source review; it is not an automatic verification decision.'});
}
if(first===197){
 assert.strictEqual(Array.from({length:50},(_,i)=>i+1).filter(n=>n%6===0||n%8===0).length,12);
 let diceCount=0;for(let a=1;a<=6;a++)for(let b=1;b<=6;b++)if(a+b===7||a+b===11)diceCount++;
 assert.strictEqual(diceCount,8);assert.strictEqual(2**6-1,63);
 assert.strictEqual([1,3,5].filter(n=>[2,3,5].includes(n)).length,2);
 assert.strictEqual(3*2/(10*9),1/15);assert.strictEqual(3*7/(10*9),7/30);
 assert(fs.readFileSync(path.join(root,'math/pages/p201.txt'),'utf8').includes('\\dfrac7{30}'));
}
if(first===202){
 assert.strictEqual(c.getMath11QuestionBank(unit).mcqs.length,10);
 assert.strictEqual(c.MATH_11_DATA.find(u=>u.number===7).slos.length,9);
 assert.strictEqual(1000n**4n,1000000000000n);
 assert(fs.readFileSync(path.join(root,'math/pages/p206.txt'),'utf8').includes('\\frac{n(n+1)(2n+1)}2'));
 assert(fs.readFileSync(path.join(root,'math/pages/p206.txt'),'utf8').includes('\\dfrac{n(n+1)(2n+1)}6'));
}
const sourceIssues=Array.from({length:5},(_,i)=>({scan:first+i+1,text:fs.readFileSync(path.join(root,'math/pages/p'+(first+i)+'.txt'),'utf8')})).flatMap(p=>p.text.split('\n').filter(l=>l.startsWith('@issue ')).map(l=>({scan:p.scan,issue:l.slice(7)})));
const report={checkedAt:new Date().toISOString(),sourceScans:Array.from({length:5},(_,i)=>first+i+1),printedPages:Array.from({length:5},(_,i)=>first+i),answeredLeaves:answers,nativeLanguagePairs:pairs,mathExpressions:expressions,codedSourceFigures:svgs.length,wordMeanings:Object.keys(c.MATH_11_WORDS).length,sourceIssues,workedExamplesArithmeticallyChecked:first===197?[22,23,24,25,26]:first===202?[27]:[],ocrComparison,wholeBookComplete:false,browserTests:false};
fs.writeFileSync(path.join(root,'math/probability-'+first+'-'+last+'-review.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,ocrComparison:ocrComparison.map(x=>({scan:x.scan,matched:x.matched,ocrWordTypes:x.ocrWordTypes}))}));
