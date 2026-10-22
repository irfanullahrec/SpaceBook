const fs=require('fs'),vm=require('vm');
const katex=require('../assets/vendor/katex/katex.min.js');
for(const cls of [7,8]){
  const ctx={window:{}};vm.runInNewContext(fs.readFileSync(`js/math_${cls}_solutions.js`,'utf8'),ctx);
  const S=ctx.window['MATH_'+cls+'_SOLUTIONS'];let n=0,steps=0,empty=0,bad=[];
  for(const k in S){n++;const e=S[k];if(!e.steps||!e.steps.length)empty++;
    for(const st of e.steps||[]){steps++;if(st.m){try{katex.renderToString(st.m,{throwOnError:true,strict:'ignore'})}catch(x){bad.push(k+': '+st.m.slice(0,70)+' -> '+String(x.message).slice(0,70))}}
      for(const l of['en','ur','ps'])if(!st[l])bad.push(k+' missing '+l)}}
  console.log(cls,{n,steps,empty,bad:bad.length});bad.slice(0,15).forEach(b=>console.log('  ',b));
}
