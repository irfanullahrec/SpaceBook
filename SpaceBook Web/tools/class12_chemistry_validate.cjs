// Focused non-browser checks for Chemistry source records and existing reading paths.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const context={};vm.createContext(context);
vm.runInContext(fs.readFileSync('js/chem_12_data.js','utf8'),context);
const chapter=vm.runInContext('CHEM_12_DATA[0]',context);
const chapters=vm.runInContext('CHEM_12_DATA',context);
assert.equal(new Set(chapter.sections.map(s=>s.id)).size,chapter.sections.length);
assert.equal(chapter.sections[0].id,'chem12-cover');
const repaired=chapters.flatMap(ch=>ch.sections.filter(s=>s.sourceClass12Chemistry));
const sourceTable=id=>repaired.flatMap(s=>s.sourceBlocks||[]).find(b=>b.id===id);
assert.deepEqual(Array.from(sourceTable('chem12-table-13-3').rows[0]).slice(1),['186','160','143','118','114','104','99','188']);
assert.deepEqual(Array.from(sourceTable('chem12-table-13-4').rows[0]).slice(1),['495','737','577','786','1011','1000','1251','1520']);
assert.equal(sourceTable('chem12-table-13-6-thermal').rows[1][8],'−486');
assert.equal(sourceTable('chem12-contents-table').rows[0][2],'1');
assert.equal(sourceTable('chem12-contents-table').rows[1][2],'46');
assert.equal(sourceTable('chem12-contents-table').rows[13][2],'386');
assert.equal(sourceTable('chem12-table-13-1').rows.length,8);
if(sourceTable('chem12-table-13-23')){
 assert.deepEqual(Array.from(sourceTable('chem12-table-13-23').rows[0]).slice(1),['3550 (Diamond)','1410','937','232','328']);
 assert.deepEqual(Array.from(sourceTable('chem12-table-13-23').rows[1]).slice(1),['4827','2355','2830','2260','1744']);
 assert(chapter.sections.find(s=>s.id==='13.15').theory.includes('Na₂[Be(OH)₄](aq)'));
}
if(chapter.sections.find(s=>s.id==='13.17').sourceClass12Chemistry){
 if(chapter.sections.find(s=>s.id==='13.18').sourceClass12Chemistry){
  assert(chapter.sections.find(s=>s.id==='13.18').theory.startsWith('ii. The Structure of Silicon dioxide'));
  assert(chapter.sections.find(s=>s.id==='13.19').theory.startsWith('Halogens in the uncombined state'));
  assert.equal(sourceTable('chem12-table-13-24').rows[0][2],'[He] 2s, 2p⁵');
 }else assert(chapter.sections.find(s=>s.id==='13.18').theory.startsWith('ii.\nThe Structure of Silicon dioxide'));
 assert(chapter.sections.find(s=>s.id==='13.17').theory.includes('Pb²⁺(aq) + 2Cl⁻(aq)'));
 assert.equal(chapter.sections.find(s=>s.id==='13.17').sourceBlocks.length,4);
 assert.equal((sourceTable('chem12-figure-13-7').svg.match(/r="2"/g)||[]).length,8);
}
if(sourceTable('chem12-table-13-17')){
 assert.deepEqual(Array.from(sourceTable('chem12-table-13-17').rows[0]).slice(1),['Crimson red','Golden yellow','Lilac','Red-violet','Blue-violet']);
 assert.equal(sourceTable('chem12-table-13-18').rows.length,6);
 assert.deepEqual(Array.from(sourceTable('chem12-table-13-19').rows[0]).slice(1),['112','150','197','215','217']);
 assert.deepEqual(Array.from(sourceTable('chem12-table-13-20').rows[0]).slice(1),['899.5','737.7','589.8','549.5','502.6']);
 assert(chapter.sections.find(s=>s.id==='13.11').theory.includes('4NO₂(g)'));
}
assert(chapter.definitions[0].def.includes('and VIIIA.'));
assert(!chapter.definitions[0].def.includes('&#'));
assert(!chapter.formulas.some(f=>f.formula==='AH=1476kJ.mol1'||f.formula==='H0-5=0'));
assert(chapter.formulas.some(f=>f.formula.includes('Mg²⁺')&&f.formula.includes('1476 kJ.mol⁻¹')));
assert.equal(new Set(chapter.formulas.filter(f=>f.id).map(f=>f.id)).size,chapter.formulas.filter(f=>f.id).length);
assert.equal(chapter.sections.find(s=>s.id==='13.1').paras.length,22);
assert(!sourceTable('chem12-figure-13-1').svg.includes('>7p<'));
assert(chapter.sections.find(s=>s.id==='13.2').theory.includes('1476 kJ.mol⁻¹'));
assert(!chapter.sections.find(s=>s.id==='13.3').theory.includes('1476'));
if(chapter.sections.find(s=>s.id==='13.7').sourceClass12Chemistry){
 if(chapter.sections.find(s=>s.id==='13.8').sourceClass12Chemistry){
  if(chapter.sections.find(s=>s.id==='13.9').sourceClass12Chemistry){
   if(chapter.sections.find(s=>s.id==='13.10').sourceClass12Chemistry){
    if(chapter.sections.find(s=>s.id==='13.11').sourceClass12Chemistry){
     if(chapter.sections.find(s=>s.id==='13.12').sourceClass12Chemistry){
      if(chapter.sections.find(s=>s.id==='13.13').sourceClass12Chemistry){
       if(chapter.sections.find(s=>s.id==='13.14').sourceClass12Chemistry)assert(chapter.sections.find(s=>s.id==='13.15').theory.startsWith('13.3.6.1 Why is Beryllium Chloride'));
       else assert(chapter.sections.find(s=>s.id==='13.14').theory.startsWith('Ba2+\nBa(OH)2(8)'));
      }
      else assert(chapter.sections.find(s=>s.id==='13.13').theory.startsWith('Table 13.21 Trend in Electronegativity'));
     }
     else assert(chapter.sections.find(s=>s.id==='13.12').theory.startsWith('The smaller the positive ion'));
    }
    else assert(chapter.sections.find(s=>s.id==='13.11').theory.startsWith('2Na+ Cla\n'));
   }
   else assert(chapter.sections.find(s=>s.id==='13.10').theory.startsWith('13.2.3\nReactions with Oxygen'));
  }
  else assert(chapter.sections.find(s=>s.id==='13.9').theory.startsWith('37Rb\n'));
 }
 else assert(chapter.sections.find(s=>s.id==='13.8').theory.startsWith('PC130\n+3H2O'));
}else assert(chapter.sections.find(s=>s.id==='13.7').theory.startsWith('Dichlorine heptoxide (C207) reacts directly'));
const app=fs.readFileSync('js/app.js','utf8');
const getParas=app.slice(app.indexOf('function getScienceSectionParagraphsWithTranslations('),app.indexOf('function switchScienceLessonSubTab('));
const layout=app.slice(app.indexOf('function renderScienceSourceLayout('),app.indexOf('function renderClass9PhysicsFrontMatterBlocks('));
const calls=[];
const sanitize=x=>String(x??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const c={sanitize,renderInteractiveParagraphHtml:(en,ur,ps,id,aligned)=>{assert(en&&ur&&ps&&aligned);calls.push({en,ur,ps});return '<span>'+sanitize(en)+'</span>';}};
vm.createContext(c);vm.runInContext(getParas+layout,c);
for(const s of repaired){
 assert(s.paras.every(p=>p.text&&p.urdu&&p.pashto&&!/<\/?(?:svg|p|div)\b/.test(p.text)));
 assert.equal(s.sourceLayout.flatMap(b=>b.indices||[]).length,s.paras.length);
 const owner=chapters.find(ch=>ch.sections.includes(s));
 const p=c.getScienceSectionParagraphsWithTranslations(s,owner,'chem');
 for(const lang of ['en','ur','ps']){
  const out=c.renderScienceSourceLayout(s,p,lang,0);assert(out.length>20);assert(!out.includes('undefined'));
  assert.equal((out.match(/<table\b/g)||[]).length,s.sourceLayout.filter(b=>b.type==='sourceDataTable').length);
 }
}
// Exercise the real hover controller with a small in-memory DOM substitute.
const hover=app.slice(app.indexOf('let hoverTooltipEl = null;'),app.indexOf('function hideWordHoverTooltip('));
let tooltip;
const h={state:{selectedClass:'cls12',activeSubject:'chem',selectedSubjChapter:0},CHEM_12_DATA:[chapter],DATA:{},sanitize,
 window:{innerWidth:900},document:{body:{appendChild(){}},createElement(){tooltip={style:{},getBoundingClientRect:()=>({width:200,height:80})};return tooltip;}}};
vm.createContext(h);vm.runInContext(hover,h);
for(const word of ['electronegativity','radius','magnesium']){
 h.showWordHoverTooltip({dataset:{word},getBoundingClientRect:()=>({left:100,top:200,bottom:220,width:30})});
 assert(tooltip.innerHTML.includes(chapter.sourceWordMeanings[word].u));
 assert(tooltip.innerHTML.includes(chapter.sourceWordMeanings[word].p));
}
h.state.selectedClass='cls9';h.DATA.chemChapters=[{sourceWordMeanings:{radius:{u:'نصف قطر',p:'شعاع'}}}];
h.showWordHoverTooltip({dataset:{word:'radius'},getBoundingClientRect:()=>({left:100,top:200,bottom:220,width:30})});
assert(tooltip.innerHTML.includes('نصف قطر'));
h.state.selectedClass='cls12';h.CHEM_12_DATA=chapters;
for(const [number,words] of [[14,['ligand','titration']],[15,['organic','catenation','biotechnology']]]){
 const index=chapters.findIndex(ch=>ch.number===number);h.state.selectedSubjChapter=index;
 if(!chapters[index].sections.some(s=>s.sourceClass12Chemistry))continue;
 for(const word of words){
  const meaning=chapters[index].sourceWordMeanings[word];assert(meaning?.u&&meaning?.p);
  h.showWordHoverTooltip({dataset:{word},getBoundingClientRect:()=>({left:100,top:200,bottom:220,width:30})});
  assert(tooltip.innerHTML.includes(meaning.u)&&tooltip.innerHTML.includes(meaning.p));
 }
}
const transition=chapters.find(ch=>ch.number===14),organic=chapters.find(ch=>ch.number===15);
const sourceBlock=(owner,id)=>owner.sections.flatMap(s=>s.sourceBlocks||[]).find(b=>b.id===id);
if(sourceBlock(organic,'chem12-table15-2')){
 const rows=sourceBlock(organic,'chem12-table15-2').rows;
 assert.equal(rows.length,10);assert.deepEqual(Array.from(rows[0]),['1','CH₄','Methane','CH₄']);
 assert.equal(rows[9][1],'C₁₀H₂₂');assert.equal(rows[9][3],'CH₃'+'CH₂'.repeat(8)+'CH₃');
 assert.equal(sourceBlock(organic,'chem12-table15-1-first').rows.length+sourceBlock(organic,'chem12-table15-1-continuation').rows.length,14);
 assert.equal(sourceBlock(transition,'chem12-p60-complex-names').rows.length,9);
 assert.equal(sourceBlock(transition,'chem12-table-14-6').rows.length,14);
 const exercise=transition.sections.find(s=>s.id==='chem12-u14-exercise');
 assert.equal(exercise.paras.filter(p=>/^[abcd]\. /.test(p.text)).length,60);
 assert.equal(exercise.paras.filter(p=>/^\d+\. /.test(p.text)).length,19);
 assert(transition.sections.find(s=>s.id==='14.11').theory.includes('Cr₂(SO₄)₃.18H₂O'));
}
const report={savedUtc:new Date().toISOString(),repairedSectionIds:repaired.map(s=>s.id),alignedParagraphs:repaired.reduce((n,s)=>n+s.paras.length,0),cachedVocabularyWords:Object.keys(chapter.sourceWordMeanings).length,
 passed:['JavaScript evaluation','unique source identities','source table values from inspected scans','source contents page references','learning-outcome count','magnesium equation boundary','formula/definition views synchronized','pending-page continuation preserved','explicit aligned paragraphs','three-language layouts and tables','real Chemistry XII hover controller','existing Class9 hover behavior preserved'],
 scope:'Focused code/source-value checks; no browser used. Whole-page visual comparison and full-book verification remain separate.'};
fs.writeFileSync('docs/source-verification/class-12/chemistry-code-validation.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
