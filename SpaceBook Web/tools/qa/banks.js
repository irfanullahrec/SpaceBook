'use strict';
// Class 12 exercise-bank coverage: items, MCQs without correct index, items without worked steps/answers
const fs=require('fs'),path=require('path'),vm=require('vm');
const dir=path.resolve(__dirname,'..','..','js');
const out={};
for(const f of fs.readdirSync(dir).filter(f=>/12_exercise_banks\.js$/.test(f)&&f!=='class12_exercise_banks.js')){
 let reg={};const ctx=vm.createContext({window:{},console,registerClass12ExerciseBanks:(n,o)=>{reg[n]=o;}});
 try{vm.runInContext(fs.readFileSync(path.join(dir,f),'utf8'),ctx);}catch(e){console.log(f,'ERR',e.message.slice(0,80));}
 for(const [name,units] of Object.entries(reg)){
  const r={units:0,mcq:0,mcqNoC:0,mcqNoS:0,short:0,long:0,numeric:0,noSteps:0,steps2:0};
  for(const [u,v] of Object.entries(units)){r.units++;const it=v.items||{};
   for(const m of it.mcqs||[]){r.mcq++;if(m.c==null||m.c<0)r.mcqNoC++;if(!(m.s&&m.s.length))r.mcqNoS++;}
   for(const k of Object.keys(it)){if(k==='mcqs')continue;for(const m of it[k]||[]){ if(/short/i.test(k))r.short++;else if(/long/i.test(k))r.long++;else r.numeric++;
     const s=m.s||m.a||[];if(!(s.length))r.noSteps++;else if(s.length>=2)r.steps2++;}}}
  out[name]=r;}
}
console.log(JSON.stringify(out,null,0).replace(/},/g,'},\n'));
