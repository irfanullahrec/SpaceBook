// every bank/data item that animated with the original vr_auto must still animate (and with identical row count) now
const fs=require('fs'),path=require('path'),vm=require('vm');
const dir=path.resolve(__dirname,'..','..','js');
const O=require('./bak/vr_auto.orig.js'),N=require(path.join(dir,'vr_auto.js'));
let lost=0,gain=0,same=0,rowdiff=0;
for(const f of fs.readdirSync(dir).filter(f=>/12_exercise_banks\.js$/.test(f)&&f!=='class12_exercise_banks.js')){
 let reg={};const ctx=vm.createContext({window:{},console,registerClass12ExerciseBanks:(n,o)=>{reg[n]=o;}});vm.runInContext(fs.readFileSync(path.join(dir,f),'utf8'),ctx);
 for(const units of Object.values(reg))for(const v of Object.values(units))for(const arr of Object.values(v.items||{}))for(const m of arr||[]){const s=(m.s||[]).map(x=>typeof x==='string'?x:x.text||'');if(!s.length)continue;
  const a=O.autoSpec(s,{q:''}),b=N.autoSpec(s,{q:''});
  if(a.spec&&!b.spec){lost++;console.log('LOST',s[0].slice(0,80));}else if(!a.spec&&b.spec)gain++;else if(a.spec){same++;if(a.stats.rows!==b.stats.rows)rowdiff++;}}}
console.log({lost,gain,same,rowdiff});
if(process.argv[2]==='-v'){
for(const f of fs.readdirSync(dir).filter(f=>/12_exercise_banks\.js$/.test(f)&&f!=='class12_exercise_banks.js')){
 let reg={};const ctx=vm.createContext({window:{},console,registerClass12ExerciseBanks:(n,o)=>{reg[n]=o;}});vm.runInContext(fs.readFileSync(path.join(dir,f),'utf8'),ctx);
 for(const units of Object.values(reg))for(const v of Object.values(units))for(const arr of Object.values(v.items||{}))for(const m of arr||[]){const s=(m.s||[]).map(x=>typeof x==='string'?x:x.text||'');if(!s.length)continue;
  const a=O.autoSpec(s,{q:''}),b=N.autoSpec(s,{q:''});
  if((a.spec&&!b.spec)||(a.spec&&b.spec&&a.stats.rows!==b.stats.rows)){console.log('---',a.stats&&a.stats.rows,b.stats&&b.stats.rows);console.log(s.join('\n').slice(0,420));
   console.log(JSON.stringify(a.spec.rows.map(x=>Object.values(x.tex)[0])).slice(0,300));console.log(b.spec?JSON.stringify(b.spec.rows.map(x=>Object.values(x.tex)[0])).slice(0,300):'NONE');}}}}
