// Most frequent sentence shapes spoken by the Animated solution (digits and maths replaced by #), for the Urdu phrase table.
const fs=require('fs'),path=require('path'),vm=require('vm');
const dir=path.join(__dirname,'..','..','js');global.window=global;
const NS=require(path.join(dir,'vr_auto.js'));const SB=global.SBVR||NS.SBVR||NS;
try{require(path.join(dir,'vr_arith.js'));}catch(e){}
const cnt=new Map();
const norm=s=>String(s).replace(/<[^>]+>/g,' ').replace(/\$[^$]*\$/g,'#').replace(/[-+−×÷=\/\d.,()\[\]{}^√]+/g,'#').replace(/\s+/g,' ').trim();
for(const f of fs.readdirSync(dir).filter(x=>/^(math_(6|7|8|11|12)_.*|math_5_solutions)\.js$/.test(x)||/^sol_.*\.js$/.test(x))){
  const code=fs.readFileSync(path.join(dir,f),'utf8').replace(/^(const|let) /gm,'var ');const win={};
  const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
  try{vm.runInContext(code,ctx,{timeout:60000});}catch(e){}
  const seen=new Set();let n=0;
  const walk=(o,d)=>{if(!o||typeof o!=='object'||seen.has(o)||d>12||n>4000)return;seen.add(o);
    if(Array.isArray(o.steps)&&o.steps.length&&o.steps.every(s=>typeof s==='string')){n++;
      try{const r=(SB.arithSpec&&SB.arithSpec(o.steps.map(t=>({text:t,m:''})),{q:'',given:''}))||SB.autoSpec(o.steps,{q:'',given:''}).spec;
        if(r)r.steps.forEach(s=>[s.title,s.html].forEach(t=>t&&String(t).split(/(?<=[.!?:])\s+/).forEach(x=>{const k=norm(x);if(k&&k.length>3)cnt.set(k,(cnt.get(k)||0)+1);})));}catch(e){}}
    for(const k of Object.keys(o))walk(o[k],d+1);};
  for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);
}
[...cnt.entries()].sort((a,b)=>b[1]-a[1]).slice(0,+process.argv[2]||80).forEach(([k,v])=>console.log(v+'\t'+k));
