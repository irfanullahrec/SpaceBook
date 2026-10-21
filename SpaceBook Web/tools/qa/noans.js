const fs=require('fs'),path=require('path'),vm=require('vm');
const f=path.resolve(process.argv[2]);
const code=fs.readFileSync(f,'utf8').replace(/^(const|let) /gm,'var ');
const win={};const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
try{vm.runInContext(code,ctx,{timeout:30000});}catch(e){}
const seen=new Set();const AK=['answer','ans','correct','solution','steps','answerKey','correctAnswer'];
const walk=(o,d)=>{if(!o||typeof o!=='object'||seen.has(o)||d>16)return;seen.add(o);
 if(!Array.isArray(o)&&typeof o.question==='string'&&o.question.length>3&&!AK.some(k=>o[k]!==undefined&&o[k]!==null&&String(typeof o[k]==='object'?JSON.stringify(o[k]):o[k]).trim()!==''))console.log((o.id||o.qNo||'?')+' | '+o.question.replace(/\n/g,' ').slice(0,200));
 for(const k of Object.keys(o))walk(o[k],d+1);};
for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);
