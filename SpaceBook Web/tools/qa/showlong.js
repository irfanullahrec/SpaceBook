// longest stored version of each id: node tools/qa/showlong.js id1 id2 ...
const fs=require('fs'),path=require('path'),vm=require('vm');
const ids=process.argv.slice(2);const dir=path.resolve(__dirname,'..','..','js');
const code=fs.readFileSync(path.join(dir,'math_12_data.js'),'utf8').replace(/^(const|let) /gm,'var ');const win={};
const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
try{vm.runInContext(code,ctx,{timeout:60000});}catch(e){}
const best={};const seen=new Set();
const walk=(o,d)=>{if(!o||typeof o!=='object'||seen.has(o)||d>14)return;seen.add(o);if(!Array.isArray(o)&&ids.includes(o.id)){const L=(o.question||'').length+(o.solution||'').length;if(!best[o.id]||L>best[o.id].L)best[o.id]={L,o};}for(const k of Object.keys(o))walk(o[k],d+1);};
for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);
for(const id of ids)if(best[id])console.log('### '+id+'\nQ: '+best[id].o.question+'\nS: '+(best[id].o.solution||(best[id].o.steps||[]).join('\n')));else console.log('### '+id+' NOT FOUND');
