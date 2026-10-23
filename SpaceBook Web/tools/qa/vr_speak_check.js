// Which spoken sentences of the Animated solution have no board-made Urdu phrase? node tools/qa/vr_speak_check.js [n]
const fs=require('fs'),path=require('path'),vm=require('vm');
const dir=path.join(__dirname,'..','..','js');global.window=global;
const NS=require(path.join(dir,'vr_auto.js'));try{require(path.join(dir,'vr_arith.js'));}catch(e){}
const SB=global.SBVR||NS;
const src=fs.readFileSync(path.join(dir,'vr_engine.js'),'utf8');
const plainSrc=/const plain = x => ([^\n]*);\n/.exec(src)[1];
const plain=eval('x=>'+plainSrc.replace(/;$/,''));
const urSrc=src.slice(src.indexOf('urWords(s) {'),src.indexOf('hasVoice(l)'));
const eng={}; new Function('eng',"class X{"+urSrc.replace(/hasUrduVoice[\s\S]*$/,'')+"}; eng.X=X;")(eng);
const urPhrase=s=>new eng.X().urPhrase(s);
const miss=new Map();let tot=0;
const code=fs.readFileSync(path.join(dir,'math_7_solutions.js'),'utf8').replace(/^(const|let) /gm,'var ');const win={};
const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
try{vm.runInContext(code,ctx,{timeout:60000});}catch(e){}
const seen=new Set();let n=0;const LIM=+process.argv[2]||300;
const walk=(o,d)=>{if(!o||typeof o!=='object'||seen.has(o)||d>12||n>LIM)return;seen.add(o);
  if(Array.isArray(o.steps)&&o.steps.length&&o.steps.every(s=>s&&typeof s==='object'&&typeof s.en==='string')){n++;
    const tx=o.steps.map(t=>({text:t.en,m:t.m?String(t.m):''}));let r=null;try{r=(SB.arithSpec&&SB.arithSpec(tx,{q:'',given:''}))||SB.autoSpec(tx,{q:'',given:''}).spec;}catch(e){}
    if(r)r.steps.forEach(st=>{const t=[plain(st.title),plain(st.html)].filter(Boolean).join('. ').replace(/Textbook:.*$/i,'').trim();
      t.split(/(?<=[.!?])\s+/).filter(Boolean).forEach(s=>{tot++;if(!urPhrase(s)){miss.set(s,(miss.get(s)||0)+1);}});});}
  for(const k of Object.keys(o))walk(o[k],d+1);};
for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);
console.log('sentences',tot,'without own Urdu',[...miss.values()].reduce((a,b)=>a+b,0));
[...miss.entries()].sort((a,b)=>b[1]-a[1]).slice(0,40).forEach(([k,v])=>console.log(v+'\t'+k));
if(process.argv[3]){process.argv.slice(3).forEach(s=>console.log(JSON.stringify(s),'=>',urPhrase(s)));}
