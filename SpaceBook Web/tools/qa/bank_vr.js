'use strict';
// Class 12 bank worked answers: how many numerical-looking items animate (autoSpec) and which do not
const fs=require('fs'),path=require('path'),vm=require('vm');
const ROOT=path.resolve(__dirname,'..','..'),dir=path.join(ROOT,'js');
const {autoSpec}=require(path.join(dir,'vr_auto.js'));
const show=process.argv[2];const fails=[];const tot={};
for(const f of fs.readdirSync(dir).filter(f=>/12_exercise_banks\.js$/.test(f)&&f!=='class12_exercise_banks.js')){
 let reg={};const ctx=vm.createContext({window:{},console,registerClass12ExerciseBanks:(n,o)=>{reg[n]=o;}});
 try{vm.runInContext(fs.readFileSync(path.join(dir,f),'utf8'),ctx);}catch(e){}
 for(const [name,units] of Object.entries(reg)){const t=tot[name]=tot[name]||{items:0,numeric:0,anim:0};
  for(const [u,v] of Object.entries(units)){const it=v.items||{};
   for(const k of Object.keys(it)){for(const [i,m] of (it[k]||[]).entries()){const s=(m.s||[]).map(x=>typeof x==='string'?x:x.text||'');if(!s.length)continue;t.items++;
    const txt=s.join(' ');const numeric=(txt.match(/=/g)||[]).length>=2&&/\d/.test(txt);if(!numeric)continue;t.numeric++;
    const r=autoSpec(s,{q:''});if(r.spec)t.anim++;else fails.push({name,u,k,i,why:r.why,s});}}}}}
console.log(JSON.stringify(tot));
if(show){fails.filter(x=>x.name===show).slice(0,+process.argv[3]||8).forEach(x=>console.log(x.name,x.u,x.k,x.i,x.why,'\n   ',x.s.join('\n    ').slice(0,500)));}
