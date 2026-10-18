const fs = require('fs');
const src = fs.readFileSync('js/english_12_data.js', 'utf8');
const fn = new Function(src.replace(/if \(typeof DATA[^\n]*/g, '').replace(/if \(typeof window[^\n]*/g, '') + '\nreturn ENGLISH_12_DATA;');
const data = fn();

// Unit 4: Truck Art
const u4 = data[3];
console.log('=== Unit 4: Truck Art ===');
console.log('Sections:', u4.sections.length);
u4.sections.forEach((s,i) => {
    console.log(`Section ${i}: ${s.heading} (${s.paras.length} paras)`);
    s.paras.forEach((p,j) => console.log(`  Para${j}: ${p.substring(0,150)}`));
});
console.log('Comp Qs:', u4.exercise.comprehension.length);

console.log('\n=== Unit 6: If ===');
const u6 = data[5];
u6.sections.forEach((s,i) => {
    console.log(`Section ${i}: ${s.heading}`);
    s.paras.forEach((p,j) => console.log(`  Para${j}: ${p.substring(0,200)}`));
});

console.log('\n=== Unit 9: The Toys ===');
const u9 = data[8];
u9.sections.forEach((s,i) => {
    console.log(`Section ${i}: ${s.heading}`);
    s.paras.forEach((p,j) => console.log(`  Para${j}: ${p.substring(0,200)}`));
});

console.log('\n=== Unit 12: All Worlds a Stage ===');
const u12 = data[11];
u12.sections.forEach((s,i) => {
    console.log(`Section ${i}: ${s.heading}`);
    s.paras.forEach((p,j) => console.log(`  Para${j}: ${p.substring(0,200)}`));
});
