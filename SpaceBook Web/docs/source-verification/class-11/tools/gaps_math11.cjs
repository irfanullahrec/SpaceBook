// Lists every exercise question / part of Class 11 Maths that has no step-by-step solution.
// usage: node tools/gaps_math11.cjs [unit...]   (no args = summary for all units)
const fs=require('fs'),path=require('path'),vm=require('vm');
const app=path.resolve(__dirname,'../../../..');
const ctx={window:{}};vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(app,'js/math_11_data.js'),'utf8')+'\nthis.units=MATH_11_DATA;',ctx);
vm.runInContext(fs.readFileSync(path.join(app,'js/math_11_solutions.js'),'utf8'),ctx);
const sols=ctx.window.MATH_11_SOLUTIONS||{};
const authored=JSON.parse(fs.readFileSync(path.join(__dirname,'../math/authored-solutions.json'),'utf8'));
const want=process.argv.slice(2).map(Number);
for(const u of ctx.units){
  let leaves=0,ok=0;const miss=[];
  for(const ex of u.exercises){
    const walk=bs=>(bs||[]).forEach(b=>{
      if(b.t==='q')for(const o of (b.parts&&b.parts.length?b.parts:[b])){
        leaves++;const key=`${ex.id}|${b.no}|${o===b?'':o.no}`;
        const steps=(o.solId&&sols[o.solId]&&sols[o.solId].steps)||(authored[key]&&authored[key].steps)||[];
        if(steps.length)ok++;else miss.push(key);
      }
      if(b.blocks)walk(b.blocks);
    });
    walk(ex.blocks);
  }
  console.log(`Unit ${u.number} ${u.title}: ${ok}/${leaves} with steps`);
  if(want.includes(u.number))console.log('  missing: '+miss.join('  '));
}
