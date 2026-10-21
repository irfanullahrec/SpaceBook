const fs=require('fs'),path=require('path'),vm=require('vm');
const f=path.resolve(process.argv[2]),n=+process.argv[3]||3,pat=process.argv[4]||'question';
const code=fs.readFileSync(f,'utf8').replace(/^(const|let) /gm,'var ');
const win={};const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
try{vm.runInContext(code,ctx,{timeout:30000});}catch(e){}
const seen=new Set();let c=0;const skip=+process.argv[5]||0;
const walk=(o,d)=>{if(c>=n||!o||typeof o!=='object'||seen.has(o)||d>16)return;seen.add(o);
 if(!Array.isArray(o)&&typeof o[pat]==='string'&&o[pat].length>3){if(c++>=0&&c>skip)console.log(JSON.stringify(o).slice(0,700));}
 for(const k of Object.keys(o))walk(o[k],d+1);};
for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);
