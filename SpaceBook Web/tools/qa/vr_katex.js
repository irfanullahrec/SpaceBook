// every row of every auto spec (Class 12 banks + Maths 10/12 data) must render with KaTeX (throwOnError)
const fs=require('fs'),path=require('path'),vm=require('vm');
const ROOT=path.resolve(__dirname,'..','..'),dir=path.join(ROOT,'js');
const katex=require(path.join(ROOT,'assets','vendor','katex','katex.min.js'));
const {autoSpec}=require(path.join(dir,'vr_auto.js'));
let rows=0,bad=0,items=0;
const chk=s=>{const r=autoSpec(s,{q:''});if(!r.spec)return;items++;for(const rw of r.spec.rows){for(const t of Object.values(rw.tex||{})){if(!t)continue;rows++;try{katex.renderToString(t,{throwOnError:true,strict:'ignore',trust:true});}catch(e){bad++;if(bad<8)console.log('BAD',t.slice(0,80),e.message.slice(0,60));}}}};
for(const f of fs.readdirSync(dir).filter(f=>/12_exercise_banks\.js$/.test(f)&&f!=='class12_exercise_banks.js')){
 let reg={};const ctx=vm.createContext({window:{},console,registerClass12ExerciseBanks:(n,o)=>{reg[n]=o;}});vm.runInContext(fs.readFileSync(path.join(dir,f),'utf8'),ctx);
 for(const units of Object.values(reg))for(const v of Object.values(units))for(const arr of Object.values(v.items||{}))for(const m of arr||[]){const s=(m.s||[]).map(x=>typeof x==='string'?x:x.text||'');if(s.length)chk(s);}}
console.log({items,rows,bad});
