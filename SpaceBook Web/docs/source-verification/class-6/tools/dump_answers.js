// Usage: node tools/dump_answers.js UNIT  -> prints exercise/question/part SpaceBook answers
global.window = global;
const fs = require('fs');
eval(fs.readFileSync(__dirname + '/../../../../js/math_6_data.js', 'utf8'));
eval(fs.readFileSync(__dirname + '/../../../../js/math_6_solutions.js', 'utf8'));
const SOL = window.MATH_6_SOLUTIONS;
const u = MATH_6_DATA[+process.argv[2] - 1];
for (const ex of u.exercises) {
  for (const b of ex.blocks) {
    if (b.t !== 'q') continue;
    const items = b.parts && b.parts.length ? b.parts : [b];
    const s = items.map(p => (p.no ? p.no + ') ' : '') + (p.solId ? SOL[p.solId].answer : '—')).join('; ');
    console.log(`${ex.id} | ${b.no} | ${s}`.slice(0, 260));
  }
}
