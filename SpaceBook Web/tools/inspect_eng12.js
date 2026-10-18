const fs = require('fs');
let src = fs.readFileSync('js/english_12_data.js', 'utf8');
// Replace the module footer so we can eval safely
src = src.replace(/if \(typeof DATA[^\n]*/g, '').replace(/if \(typeof window[^\n]*/g, '');
// eval in global scope
const fn = new Function(src + '\nreturn ENGLISH_12_DATA;');
const data = fn();
const u1 = data[0];
console.log('=== UNIT 1 ===');
console.log('Title:', u1.title);
console.log('Sections:', u1.sections.length);
console.log('Para count sec0:', u1.sections[0].paras.length);
console.log('First para (300):', u1.sections[0].paras[0] ? u1.sections[0].paras[0].substring(0,300) : 'EMPTY');
console.log('Comp Qs:', u1.exercise.comprehension.length);
if(u1.exercise.comprehension[0]) console.log('Comp Q1:', u1.exercise.comprehension[0].question.substring(0,200));
console.log('Summary:', u1.englishSummary.substring(0,300));
console.log('');
const u5 = data[4];
console.log('=== UNIT 5: The Last Leaf ===');
console.log('Sections:', u5.sections.length, 'ParaCount:', u5.sections.reduce((a,s)=>a+s.paras.length,0));
console.log('First para:', u5.sections[0].paras[0] ? u5.sections[0].paras[0].substring(0,300) : 'EMPTY');
console.log('');
console.log('Total units:', data.length);
