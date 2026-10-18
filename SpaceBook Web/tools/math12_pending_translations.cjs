// List untranslated passage originals in Class 12 Maths sections (same attach rules as the unit translation files).
const fs=require('fs'),vm=require('vm'),path=require('path');
const root=path.resolve(__dirname,'..');
const ctx={console,Map,Set,Object,Array,JSON,Math,Number,String,RegExp,Error};ctx.window=ctx;ctx.globalThis=ctx;ctx.document={addEventListener(){},querySelector(){return null},querySelectorAll(){return []},createElement(){return {style:{},setAttribute(){},appendChild(){}}},head:{appendChild(){}},getElementById(){return null}};
ctx.sanitize=s=>String(s);ctx.renderMathSourceBlocks=()=>'';
vm.createContext(ctx);
const files=['math_12_data.js','math12_unit6_source_recovery.js','math12_translation_completions.js','math12_unit2_translations.js','math12_unit5_translations.js','math12_unit3_translations.js','math12_unit7_translations.js','math12_unit11_translations.js','math12_unit4_translations.js','math12_unit10_translations.js','math12_unit8_translations.js','math12_unit12_translations.js','math12_unit6_translations.js','math12_unit9_translations.js'];
for(const f of files){try{vm.runInContext(fs.readFileSync(path.join(root,'js',f),'utf8').replace(/^const (MATH_12_DATA|MATH12_SENTENCE_TRANSLATIONS)\b/m,'var $1'),ctx,{filename:f});}catch(e){console.error('load',f,e.message);}}
const D=vm.runInContext('typeof MATH_12_DATA!=="undefined"?MATH_12_DATA:null',ctx), T=vm.runInContext('typeof MATH12_SENTENCE_TRANSLATIONS!=="undefined"?MATH12_SENTENCE_TRANSLATIONS:null',ctx);
if(!D||!T){console.error('globals missing',!!D,!!T);process.exit(1);}
const ids=process.argv.slice(2);
const out={};
const ok=rows=>Array.isArray(rows)&&rows.length&&rows.every(r=>r.en&&r.ur&&r.ps);
for(const ch of D)for(const s of ch.sections||[]){
 if(!ids.includes(s.id))continue;
 const miss=[];const seen=new Set();
 const need=(t,existing)=>{if(!t||ok(existing)||ok(T[t])||seen.has(t))return;seen.add(t);miss.push(t);};
 for(const b of s.sourceBlocks||[]){
  if(['heading','paragraph','clarification'].includes(b.type))need(b.text,b.sentenceTranslations);
  if(b.caption)need(b.caption,b.captionSentenceTranslations);
  if(b.alt)need(b.alt,b.altSentenceTranslations);
  if(b.type==='list')(b.items||[]).forEach((it,i)=>{if(typeof it==='string')need(it,(b.itemSentenceTranslations||[])[i]);});
  if(Array.isArray(b.headers))b.headers.forEach((it,i)=>{if(typeof it==='string'&&/[A-Za-z]{2,}/.test(it.replace(/\\([\s\S]*?\\)/g,'')))need(it,(b.headerSentenceTranslations||[])[i]);});
  if(Array.isArray(b.rows))b.rows.forEach((row,r)=>Array.isArray(row)&&row.forEach((it,i)=>{if(typeof it==='string'&&/[A-Za-z]{2,}/.test(it.replace(/\\([\s\S]*?\\)/g,'')))need(it,((b.cellSentenceTranslations||[])[r]||[])[i]);}));
 }
 out[s.id]={title:s.title,unreviewedTheory:(s.unreviewedTheory||'').length,missing:miss};
}
fs.writeFileSync(path.join(root,'tmp/m12/pending.json'),JSON.stringify(out,null,1));
for(const [k,v] of Object.entries(out))console.log(k,v.title,'missing',v.missing.length,'chars',v.missing.join('').length,'unreviewed',v.unreviewedTheory);
