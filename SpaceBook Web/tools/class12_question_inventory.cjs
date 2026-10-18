/* Evaluates active Class12 records without changing any subject data. */
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'..');
const names={phys:'PHYS',chem:'CHEM',stat:'STAT',english:'ENGLISH',urdu:'URDU',biology:'BIOLOGY',pakstudy:'PAKSTUDY',computer:'COMPUTER',civics:'CIVICS',economics:'ECONOMICS',hpe:'HPE',islamiat_ikhtiari:'ISLAMIAT_IKHTIARI',islamic_history:'ISLAMIC_HISTORY',quran:'QURAN'};
const report={checkedUtc:new Date().toISOString(),scope:'Active schema inventory; answer presence is not correctness verification.',subjects:{}};
for(const [name,prefix] of Object.entries(names)){
 const file='js/'+name+'_12_data.js',text=fs.readFileSync(path.join(root,file),'utf8');
 const binding=(text.match(/(?:const|var|let)\s+([A-Z_0-9]+_12_DATA)\s*=/)||[])[1]||prefix+'_12_DATA';
 const sb={console,DATA:{}};sb.window=sb;vm.createContext(sb);
 try{
  vm.runInContext(text+'\nthis.result='+binding+';',sb,{filename:file,timeout:20000});
  report.subjects[name]={file,binding,chapters:sb.result.map(ch=>{
   const sections=ch.sections||ch.topics||[];
   const result={number:ch.number||ch.num,title:ch.title||ch.name,keys:Object.keys(ch),sections:sections.length,
    sourceSections:sections.filter(s=>s.sourceLayout||s.sourceBlocks).length,
    answerSections:sections.filter(s=>/answer|solution|solved|حل|ځواب/i.test(s.title||'')).map(s=>({id:s.id,title:s.title,paras:s.paras?.length,blocks:s.sourceBlocks?.length})),
    fields:{}};
   for(const key of ['exercise','textbookExercise','exercises','slos','sloBank','sloQuestions','sloMcqs','sloSq','sloLq','numericals','longQuestions']){
    const field=ch[key];if(!field)continue;
    result.fields[key]=Array.isArray(field)?{count:field.length,sample:field.slice(0,1)}:Object.fromEntries(Object.entries(field).map(([k,v])=>[k,Array.isArray(v)?{count:v.length,sample:v.slice(0,1)}:v]));
   }
   return result;
  })};
 }catch(error){report.subjects[name]={file,error:error.message};}
}
fs.writeFileSync(path.join(root,'docs/source-verification/class-12/question-inventory.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(Object.fromEntries(Object.entries(report.subjects).map(([name,s])=>[name,s.error||{chapters:s.chapters.length,answerSections:s.chapters.reduce((n,c)=>n+c.answerSections.length,0),fields:[...new Set(s.chapters.flatMap(c=>Object.keys(c.fields)))]}]))));
