const fs=require('fs'),path=require('path');
const W=require('../word_stats/build_word_stats.js');
const D=W.loadCatalogue();
const files=fs.readdirSync(W.JS).filter(f=>f.endsWith('.js')&&!W.SKIP_FILES.has(f)&&!/reader\.js$/.test(f)).sort();
const shapes={},perFile={};
function isMcq(o){ if(!o||typeof o!=='object'||Array.isArray(o))return null;
  const keys=Object.keys(o); const arrK=keys.find(k=>Array.isArray(o[k])&&o[k].length>=3&&o[k].length<=6&&o[k].every(x=>typeof x==='string'||(x&&typeof x==='object'&&typeof (x.text||x.en||x.t)==='string')));
  if(!arrK)return null; const qK=keys.find(k=>/^(q|question|stem|text|qText|prompt|statement|qEn|en)$/i.test(k)&&typeof o[k]==='string');
  const aK=keys.find(k=>/^(ans|answer|correct|key|correctIndex|answerIndex|a|right)$/i.test(k));
  if(!qK||!aK)return null; return keys.sort().join(',');}
function walk(v,cb,seen){ if(!v||typeof v!=='object'||seen.has(v))return; seen.add(v); const s=isMcq(v); if(s){cb(s,v);} for(const k in v){try{walk(v[k],cb,seen)}catch(e){}}}
for(const f of files){ let ev; try{ev=W.evaluate(f)}catch(e){continue}
  walk([ev.globals,ev.data],(s,o)=>{shapes[s]=shapes[s]||{n:0,ex:o,f};shapes[s].n++;perFile[f]=(perFile[f]||0)+1;},new Set());}
const sorted=Object.entries(shapes).sort((a,b)=>b[1].n-a[1].n);
for(const [s,{n,ex,f}] of sorted.slice(0,25)) console.log(n,f,s,'\n   ',JSON.stringify(ex).slice(0,300));
console.log(Object.values(perFile).reduce((a,b)=>a+b,0)); console.log(JSON.stringify(perFile));
