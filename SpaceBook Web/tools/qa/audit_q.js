'use strict';
// node tools/qa/audit_q.js [--json out.json] : Class 11/12 question/answer/junk audit over js/*_11_*, *_12_* data files
const fs=require('fs'),path=require('path'),vm=require('vm');
const ROOT=path.resolve(__dirname,'..','..');
const files=fs.readdirSync(path.join(ROOT,'js')).filter(f=>/^(?!sent_data)(.*(_11_|_12_|11_|12_|math11|math12|class1[12]).*)\.js$/.test(f)&&!/translat|study_views|recovery|answer_repairs|reader|^sb_|^vr_/.test(f));
const QK=['question','q','prompt','stem','problem'], AK=['answer','ans','correct','correctAnswer','key','solution','steps','answerKey'];
const out={};
const junk=/[\uFFFD]|\?\?\?|(.)\1{9,}|\bl{3,}\b/;
for(const f of files){
 const code=fs.readFileSync(path.join(ROOT,'js',f),'utf8').replace(/^(const|let) /gm,'var ');
 const win={};const ctx=vm.createContext({window:win,self:win,document:{},console:{log(){},warn(){},error(){}},localStorage:{},navigator:{},setTimeout(){},addEventListener(){}});
 try{vm.runInContext(code,ctx,{timeout:30000});}catch(e){}
 const r={q:0,noAns:0,mcq:0,mcqNoKey:0,junk:0,emptyStr:0,ex:[]};const seen=new Set();
 const walk=(o,d)=>{if(!o||typeof o!=='object'||seen.has(o)||d>16)return;seen.add(o);
  if(!Array.isArray(o)){
   const qk=QK.find(k=>typeof o[k]==='string'&&o[k].trim().length>3);
   const opts=o.options||o.choices||o.opts;
   if(qk){r.q++;
     const has=AK.some(k=>o[k]!==undefined&&o[k]!==null&&String(typeof o[k]==='object'?JSON.stringify(o[k]):o[k]).trim()!==''&&o[k]!==false);
     if(Array.isArray(opts)&&opts.length>=2){r.mcq++;const kk=['answer','ans','correct','correctIndex','key','correctAnswer'].some(k=>o[k]!==undefined&&o[k]!==''&&o[k]!==null);if(!kk){r.mcqNoKey++;if(r.ex.length<6)r.ex.push('MCQ:'+o[qk].slice(0,70));}}
     else if(!has){r.noAns++;if(r.ex.length<6)r.ex.push('NOANS:'+o[qk].slice(0,70));}
   }
   for(const k of Object.keys(o)){const v=o[k];if(typeof v==='string'){if(junk.test(v)&&!/^(svg|d|path|fill)/.test(k)&&!/^<svg/.test(v)){r.junk++;}}}
  }
  for(const k of Object.keys(o))walk(o[k],d+1);};
 for(const k of Object.keys(ctx))walk(ctx[k],0);for(const k of Object.keys(win))walk(win[k],0);
 if(r.q||r.junk)out[f]=r;
}
console.log('file'.padEnd(38),'q','noAns','mcq','mcqNoKey','junk');
for(const [f,r] of Object.entries(out))console.log(f.padEnd(38),r.q,r.noAns,r.mcq,r.mcqNoKey,r.junk,(r.ex.length?'  e.g. '+r.ex[0]:''));
const ji=process.argv.indexOf('--json');if(ji>0)fs.writeFileSync(process.argv[ji+1],JSON.stringify(out,null,1));
