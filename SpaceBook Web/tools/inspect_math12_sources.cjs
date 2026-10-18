const fs=require('fs'),vm=require('vm');const s={};vm.createContext(s);vm.runInContext(fs.readFileSync('js/math_12_data.js','utf8')+';this.data=MATH_12_DATA;',s);
const ids=process.argv.slice(2);
for(const ch of s.data)for(const ex of ch.exercises||[])for(const q of ex.problems||[])if(ids.includes(q.id))console.log(JSON.stringify({id:q.id,question:q.question,answer:q.answer,steps:q.steps,refs:q.sourceReferences,blocks:q.sourceQuestionBlocks}));
