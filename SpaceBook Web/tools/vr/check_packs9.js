'use strict';
/* Class 9 Maths: which problems with a short / chain-less solution have a hand-written pack?   node tools/vr/check_packs9.js [unit]
 * "short" = the stored solution is under 90 characters or has no equation sign (the same test used when the gaps were audited). */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..');
global.window = global;
const warns = []; const cw = console.warn; console.warn = m => { warns.push(String(m)); };
require(path.join(ROOT, 'js', 'vr_viz.js')); require(path.join(ROOT, 'js', 'vr_auto.js'));
fs.readdirSync(path.join(ROOT, 'js')).filter(f => /^sol_.*\.js$/.test(f)).sort((a, b) => (/^sol_m\d/.test(a) ? 1 : 0) - (/^sol_m\d/.test(b) ? 1 : 0) || a.localeCompare(b)).forEach(f => require(path.join(ROOT, 'js', f)));
console.warn = cw; warns.forEach(w => console.log('  WARN', w));
const NS = global.SBVR, ctx = vm.createContext({ window: {}, document: {}, console: { log() {}, warn() {}, error() {} }, localStorage: {}, navigator: {} });
vm.runInContext(fs.readFileSync(path.join(ROOT, 'js', 'math_data.js'), 'utf8').replace(/^(const|let) /gm, 'var '), ctx, { timeout: 60000 });
const only = process.argv[2] ? +process.argv[2] : null; let tot = 0, hit = 0; const miss = [];
const short = p => { const s = String(p.solution || ''); return s.replace(/\s+/g, ' ').length < 90 || !(/[=⟹⇒→]/.test(s)); };
ctx.MATH_DATA.forEach(u => { if (only && u.number !== only) return; (u.exercises || []).forEach(ex => (ex.problems || []).forEach(p => {
  if (!short(p)) return; tot++; const pk = NS.sol.find(p.question);
  if (pk) { hit++; const r = NS.autoSpec(pk.steps, { board: pk.board, question: p.question, maxSteps: 80 }); if (!r.spec) miss.push('NO-SPEC ' + u.number + ' ' + ex.exercise + ' ' + p.qNo); }
  else miss.push('u' + u.number + ' ' + ex.exercise + ' ' + p.qNo + ': ' + String(p.question).slice(0, 70).replace(/\n/g, ' '));
})); });
console.log('Class 9 short-solution problems:', tot, '| with a pack:', hit, '| without:', tot - hit);
miss.slice(0, +(process.env.SHOW || 60)).forEach(m => console.log('  ', m));
