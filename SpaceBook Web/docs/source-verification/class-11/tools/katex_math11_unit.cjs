// Renders every formula in the authored answers/steps of the given exercises with KaTeX (throwOnError).
// usage: node tools/katex_math11_unit.cjs <exercise-id-prefix>...   e.g.  12. "Review 12"
const fs=require('fs'),path=require('path'),vm=require('vm');
const app=path.resolve(__dirname,'../../../..');
const katex=require(path.join(app,'assets/vendor/katex/katex.min.js'));
const ctx={console,katex,window:{}};ctx.window=ctx;vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(app,'js/lesson_math_reader.js'),'utf8'),ctx);
const authored=JSON.parse(fs.readFileSync(path.join(__dirname,'../math/authored-solutions.json'),'utf8'));
const prefixes=process.argv.slice(2);
let n=0,bad=0,svgs=0;
const tryTex=(tex,where)=>{try{katex.renderToString(tex,{throwOnError:true,strict:'ignore'});n++;}catch(e){bad++;console.log('BAD',where,'::',e.message.slice(0,120),'::',tex.slice(0,140));}};
const texts=v=>{for(const p of ctx.SpaceBookLessonMath.mathParts(v||''))if(p.latex!==undefined)tryTex(p.latex,cur);};
let cur='';
for(const [k,v] of Object.entries(authored)){
  if(!prefixes.some(p=>k.startsWith(p)))continue;
  cur=k;['answer','answerUr','answerPs'].forEach(f=>texts(v[f]));
  for(const s of v.steps||[]){['en','ur','ps'].forEach(f=>texts(s[f]));if(s.m)tryTex(s.m,k+' m');if(s.svg){svgs++;if(!/^<svg[\s\S]*<\/svg>$/.test(s.svg))console.log('BAD SVG',k);}}
}
console.log(`formulas ok ${n}, bad ${bad}, svg ${svgs}`);
