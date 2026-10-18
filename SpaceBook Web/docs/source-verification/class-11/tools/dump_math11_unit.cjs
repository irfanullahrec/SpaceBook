// Prints every exercise leaf of a Class 11 Maths unit with its printed answer-key text (if any).
// usage: node tools/dump_math11_unit.cjs <unit> [exerciseId]
const fs=require('fs'),path=require('path'),vm=require('vm');
const app=path.resolve(__dirname,'../../../..');
const ctx={window:{}};vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(app,'js/math_11_data.js'),'utf8')+'\nthis.units=MATH_11_DATA;this.book=MATH_11_BOOK;',ctx);
const [unitNo,only]=[Number(process.argv[2]),process.argv[3]];
const unit=ctx.units.find(u=>u.number===unitNo);
const key=ctx.book.answers||{};
const keyFor=(ex,q,p)=>{const k=[`${ex}|${q}|${p}`,`${ex}|${q}|`,`${ex}|${q}`].find(x=>key[x]!==undefined);return k?JSON.stringify(key[k]).slice(0,300):'';};
for(const ex of unit.exercises){
  if(only&&ex.id!==only)continue;
  console.log(`\n######## Exercise ${ex.id} (p.${ex.printed})`);
  const walk=bs=>(bs||[]).forEach(b=>{
    if(b.t==='q'){
      console.log(`[${b.no}] ${b.en}`);
      for(const o of (b.parts&&b.parts.length?b.parts:[]))console.log(`   (${o.no}) ${o.en}${keyFor(ex.id,b.no,o.no)?'   KEY: '+keyFor(ex.id,b.no,o.no):''}`);
      if(!(b.parts&&b.parts.length)&&keyFor(ex.id,b.no,''))console.log('   KEY: '+keyFor(ex.id,b.no,''));
    } else if(b.en&&b.t!=='q') console.log(`   ~ ${String(b.en).slice(0,160)}`);
    if(b.blocks)walk(b.blocks);
  });
  walk(ex.blocks);
}
console.log('\nKEY sample keys: '+Object.keys(key).filter(k=>k.startsWith(String(unitNo)+'.')||k.startsWith('Review '+unitNo)).slice(0,8).join(' , '));
