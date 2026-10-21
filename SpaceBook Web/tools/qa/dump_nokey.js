const fs=require('fs'),path=require('path'),vm=require('vm');
const f=path.resolve(process.argv[2]);
const code=fs.readFileSync(f,'utf8').replace(/^(const|let) /gm,'var ');
const win={};const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
try{vm.runInContext(code,ctx,{timeout:30000});}catch(e){}
const seen=new Set();
const walk=(o,d)=>{if(!o||typeof o!=='object'||seen.has(o)||d>16)return;seen.add(o);
 if(!Array.isArray(o)&&o.solutionOrigin==='not_provided_in_textbook'&&Array.isArray(o.options)&&o.answer===undefined&&o.correct===undefined)console.log(o.id+' | '+o.question.replace(/\n/g,' ')+' || '+o.options.join(' ## '));
 for(const k of Object.keys(o))walk(o[k],d+1);};
for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);
