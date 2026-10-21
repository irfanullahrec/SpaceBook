// doubles every backslash after a marker in a JS file (used once to repair js/sol_m12_calc.js)
const fs = require('fs');
const [file, marker] = process.argv.slice(2);
const s = fs.readFileSync(file, 'utf8');
const i = s.indexOf(marker);
if (i < 0) throw new Error('marker not found');
const head = s.slice(0, i), tail = s.slice(i);
if (tail.includes('\\\\')) throw new Error('region already has doubled backslashes');
fs.writeFileSync(file, head + tail.split('\\').join('\\\\'));
console.log('fixed', (tail.match(/\\/g) || []).length);
