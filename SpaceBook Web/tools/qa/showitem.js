const fs=require('fs'),path=require('path'),vm=require('vm');
const ids=process.argv.slice(2);const dir=path.resolve(__dirname,'..','..','js');
const code=fs.readFileSync(path.join(dir,'math_12_data.js'),'utf8').replace(/^(const|let) /gm,'var ');const win={};
const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
try{vm.runInContext(code,ctx,{timeout:60000});}catch(e){}
const seen=new Set();const walk=(o,d)=>{if(!o||typeof o!=='object'||seen.has(o)||d>14)return;seen.add(o);if(!Array.isArray(o)&&ids.includes(o.id))console.log(JSON.stringify({id:o.id,q:o.question,sol:o.solution,steps:o.steps},null,1));for(const k of Object.keys(o))walk(o[k],d+1);};
for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);
