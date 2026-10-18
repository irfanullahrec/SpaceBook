// Load a Class 1 book file and report structure: node check1.js math
const path = require('path');
global.window = {};
const subj = process.argv[2];
const files = {math: 'math_1_book.js', eng: 'english_1_book.js', isl: 'islamyat_1_book.js', nazira: 'nazira_1_book.js', pashto: 'pashto_1_book.js', drawing: 'drawing_1_book.js', urdu: 'urdu_1_book.js', gk: 'gk_1_book.js'};
require(path.resolve(__dirname, '../../../../js', files[subj]));
const B = window.CLS1_BOOKS[subj];
let svgs = 0, bad = [];
const walk = l => (l || []).forEach(b => { if (b.t === 'svg') { svgs++; if (!/^(<svg[\s\S]*<\/svg>|<div[\s\S]*<svg[\s\S]*<\/div>)$/.test(b.svg.trim())) bad.push(b.svg.slice(0, 60)); } if (b.blocks) walk(b.blocks); });
B.units.forEach(u => u.sections.forEach(s => walk(s.blocks)));
walk(B.book.frontMatter);
console.log(subj, 'units', B.units.map(u => `${u.number}:${u.sections.length}s/${u.exercises.length}ex`).join(' '), 'svg', svgs, 'bad', bad.length, 'reviewed', B.book.reviewedPdfPages + '/' + B.book.totalPdfPages);
if (bad.length) console.log(bad);
