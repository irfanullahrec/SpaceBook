// Class 11/12 Maths items that do not animate: no chain from autoSpec and no hand pack. node tools/qa/unanimated.js [kw-regex] [limit]
const fs=require('fs'),path=require('path'),vm=require('vm');
const ROOT=path.resolve(__dirname,'..','..'),dir=path.join(ROOT,'js');
global.window=global;const NS=require(path.join(dir,'vr_auto.js'));
const SB=global.SBVR||NS.SBVR||NS;
for(const f of ['sol_m12_hand.js','sol_m12_flag.js','sol_m12_calc.js']){try{require(path.join(dir,f));}catch(e){}}
const kw=new RegExp(process.argv[2]||'derivat|differenti|integra|limit|sin|cos|tan|trig|∫|lim|d/dx|dy',"i");const LIM=+process.argv[3]||40;
const rawQ=s=>String(s||'').replace(/\s+/g,' ').trim();
const out=[];const G={};let tot=0,anim=0,pack=0;
function visit(o,file){if(!o||typeof o!=='object')return;
 const q=rawQ(o.question||o.problem||o.title);
 let steps=Array.isArray(o.steps)&&o.steps.every(s=>typeof s==='string')?o.steps:(typeof o.solution==='string'&&o.solution.includes('\n')?o.solution.split(/\n+/).map(x=>x.trim()).filter(Boolean):(typeof o.solution==='string'&&o.solution.length>3?[o.solution]:null));
 if(q&&steps){tot++;const hasPack=SB.sol&&SB.sol.find(q);const key=file+'|'+(o.id||q.slice(0,40));const r=hasPack?{spec:1}:SB.autoSpec(steps,{q:''});(G[key]=G[key]||[]).push({file,id:o.id||o.qNo,q,steps,ok:!!r.spec,pack:!!hasPack});}
}
for(const [f,g] of [['math_12_data.js','MATH_12_DATA'],['math_11_solutions.js',null],['math_11_data.js','MATH_11_DATA']]){
 const code=fs.readFileSync(path.join(dir,f),'utf8').replace(/^(const|let) /gm,'var ');const win={};
 const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
 try{vm.runInContext(code,ctx,{timeout:60000});}catch(e){}
 const seen=new Set();const walk=(o,d)=>{if(!o||typeof o!=='object'||seen.has(o)||d>14)return;seen.add(o);if(!Array.isArray(o))visit(o,f);for(const k of Object.keys(o))walk(o[k],d+1);};
 for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);}
for(const v of Object.values(G)){tot++;if(v.some(x=>x.pack))pack++;else if(v.some(x=>x.ok))anim++;else out.push(v.sort((a,b)=>b.steps.join('').length-a.steps.join('').length)[0]);}
console.log({tot,anim,pack,not:out.length});
const sel=out.filter(x=>kw.test(x.q+' '+x.steps.join(' ')));console.log('matching keyword',sel.length, JSON.stringify(out.reduce((a,x)=>(a[x.file]=(a[x.file]||0)+1,a),{})));
sel.slice(0,LIM).forEach(x=>console.log('\n['+x.file+' '+x.id+'] '+x.q.slice(0,200)+'\n   -> '+x.steps.join(' | ').slice(0,260)));
