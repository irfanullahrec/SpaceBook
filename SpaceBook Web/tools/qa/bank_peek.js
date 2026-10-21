const fs=require('fs'),path=require('path'),vm=require('vm');
const [f,name,want]=process.argv.slice(2);
let reg={};const ctx=vm.createContext({window:{},console,registerClass12ExerciseBanks:(n,o)=>{reg[n]=o;}});
vm.runInContext(fs.readFileSync('js/'+f,'utf8'),ctx);
let c=0;
for(const [u,v] of Object.entries(reg[name])){const it=v.items||{};
 if(want==='mcqNoC'){(it.mcqs||[]).forEach((m,i)=>{if(m.c==null||m.c<0)console.log(u,i,JSON.stringify(m).slice(0,400));});continue;}
 for(const k of Object.keys(it)){ if(k===want||want==='*'){ (it[k]||[]).forEach((m,i)=>{const s=m.s||m.a||[];if(!s.length&&c++<4)console.log(u,k,i,JSON.stringify(m).slice(0,500));});}}}
