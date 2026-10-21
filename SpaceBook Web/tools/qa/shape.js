'use strict';
// node tools/qa/shape.js <file.js> : print key frequency of objects reachable from a data file's globals
const fs=require('fs'),path=require('path'),vm=require('vm');
const f=path.resolve(process.argv[2]);
const code=fs.readFileSync(f,'utf8').replace(/^(const|let) /gm,'var ');
const win={};
const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
try{vm.runInContext(code,ctx,{timeout:20000});}catch(e){console.log('ERR',e.message);}
const freq={};const seen=new Set();let n=0;
const walk=(o,d,p)=>{if(!o||typeof o!=='object'||seen.has(o)||d>14)return;seen.add(o);n++;
 if(!Array.isArray(o)){const k=Object.keys(o).sort().join(',');if(k.length<200){freq[k]=(freq[k]||0)+1;}}
 for(const k of Object.keys(o))walk(o[k],d+1);};
for(const k of Object.keys(ctx))walk(ctx[k],0);
for(const k of Object.keys(win))walk(win[k],0);
console.log('globals',Object.keys(ctx).slice(0,20),Object.keys(win).slice(0,20));
Object.entries(freq).sort((a,b)=>b[1]-a[1]).slice(0,25).forEach(([k,v])=>console.log(v,k));
