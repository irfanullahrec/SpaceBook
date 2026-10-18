const fs=require('fs'),path=require('path'),vm=require('vm');
const app=path.resolve(__dirname,'../../../..');
const ctx={window:{}};vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(app,'js/math_11_data.js'),'utf8')+'\nthis.units=MATH_11_DATA;this.book=MATH_11_BOOK;',ctx);
vm.runInContext(fs.readFileSync(path.join(app,'js/math_11_solutions.js'),'utf8'),ctx);
const report={reviewed:ctx.book.reviewedPdfPages,total:ctx.book.totalPdfPages,sourceAnswers:Object.keys(ctx.book.answers||{}),solutions:Object.keys(ctx.window.MATH_11_SOLUTIONS||{}).length,units:[]};
for(const ch of ctx.units){
 const r={number:ch.number,title:ch.title,sections:ch.sections.length,exercises:[],questions:0,parts:0,solved:0};
 for(const ex of ch.exercises){const qs=[];const walk=bs=>(bs||[]).forEach(b=>{if(b.t==='q'){qs.push(b);r.questions++;r.parts+=(b.parts||[]).length;r.solved+=Number(!!b.solId)+(b.parts||[]).filter(p=>p.solId).length;}if(b.blocks)walk(b.blocks);});walk(ex.blocks);r.exercises.push({id:ex.id,printed:ex.printed,questions:qs.length});}
 report.units.push(r);
}
console.log(JSON.stringify(report,null,2));
if(process.argv.includes('--unit1'))for(const ex of ctx.units[0].exercises)console.log(JSON.stringify(ex,null,2));
