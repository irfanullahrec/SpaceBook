'use strict';
/* Which questions have a hand-written solution pack, are the packs consistent with the book's answers, and which problems still have none?
 *   node tools/vr/check_packs.js [unit]      (Class 10 Maths; prints warnings from the pack builders)
 */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..');
global.window = global;
const warns = []; const cw = console.warn; console.warn = m => { warns.push(String(m)); };
require(path.join(ROOT, 'js', 'vr_viz.js')); require(path.join(ROOT, 'js', 'vr_auto.js'));
const packFiles = fs.readdirSync(path.join(ROOT, 'js')).filter(f => /^sol_.*\.js$/.test(f)).sort((a, b) => (/^sol_m\d/.test(a) ? 1 : 0) - (/^sol_m\d/.test(b) ? 1 : 0) || a.localeCompare(b));
packFiles.forEach(f => require(path.join(ROOT, 'js', f)));
console.warn = cw;
const NS = global.SBVR; const packs = NS.sol.all();
console.log('pack files:', packFiles.join(', '), '| packs:', packs.length);
warns.forEach(w => console.log('  WARN', w));
const ctx = vm.createContext({ window: {}, document: {}, console: { log() {}, warn() {}, error() {} }, localStorage: {}, navigator: {} });
vm.runInContext(fs.readFileSync(path.join(ROOT, 'js', 'math_10_data.js'), 'utf8').replace(/^(const|let) /gm, 'var '), ctx, { timeout: 60000 });
const only = process.argv[2] ? +process.argv[2] : null; let tot = 0, hit = 0; const miss = [];
ctx.MATH_10_DATA.forEach(u => { if (only && u.number !== only) return; (u.exercises || []).forEach(ex => (ex.problems || []).forEach(p => {
  if (Array.isArray(p.steps) && p.steps.length) return; tot++;
  const pk = NS.sol.find(p.question); if (pk) { hit++; const r = NS.autoSpec(pk.steps, { board: pk.board, question: p.question, maxSteps: 80 }); if (!r.spec) miss.push('NO-SPEC ' + u.number + ' ' + ex.exercise + ' ' + p.num + ' ' + JSON.stringify(Object.keys(r)) + ' ' + (r.why||r.reason||r.error||'')); } else miss.push('u' + u.number + ' ex' + ex.exercise + ' ' + p.num + ': ' + String(p.question).slice(0, 70).replace(/\n/g, ' '));
})); });
console.log('Class 10 problems without steps:', tot, '| with a pack:', hit, '| still missing:', tot - hit);
miss.filter(m => /^NO-SPEC/.test(m)).forEach(m => console.log('  ', m)); miss.filter(m => !/^NO-SPEC/.test(m)).slice(0, +(process.env.SHOW || 40)).forEach(m => console.log('  ', m));
