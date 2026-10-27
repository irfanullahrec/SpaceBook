'use strict';
/* The MCQs that have an answer but whose answer matches no option ("open MCQs" of docs/launch/EXERCISE_COVERAGE.md), one line each, so that they can be corrected.
 *   node --max-old-space-size=6144 tools/launch/open_mcqs.js [--book cls9:chem] [--none] [--json out.json]
 * Same extraction as tools/launch/exercise_coverage.js. Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const opt = n => (args.includes(n) ? args[args.indexOf(n) + 1] : null);
const { load } = require('../lib/app_sandbox');
const extract = require('../tests/extract_leaves');
const app = load({ page: process.env.SB_PAGE || 'lazy.html', quiet: true });
for (const n of [5, 6, 7, 8, 11]) app.run(fs.readFileSync(path.join(ROOT, 'js', 'math_' + n + '_solutions.js'), 'utf8'));
const raw = JSON.parse(app.run('JSON.stringify((' + extract.toString() + ')())', 900000));
const only = opt('--book');
const has = L => (L.a && String(L.a).trim()) || (L.st && String(L.st).trim());
const NONE = args.includes('--none');          // the questions without any answer instead (leaves of the books that tools/audit/answers_audit.js does not cover)
const rows = raw.leaves.filter(L => (!only || L.b === only) && (NONE ? !has(L) && !L.head : L.o && has(L) && L.cor < 0 && !L.wl));
if (opt('--json')) fs.writeFileSync(path.resolve(opt('--json')), JSON.stringify(rows));
if (rows[0]) console.error('fields: ' + Object.keys(rows[0]).join(', '));
for (const L of rows) console.log(`${L.b} u${L.u} p${L.pg} ${String(L.ex || '').slice(0, 20)} | ${String(L.q || L.t || '').replace(/\s+/g, ' ').slice(0, 110)} || A: ${String(L.a || L.st).replace(/\s+/g, ' ').slice(0, 70)}`);
console.error(rows.length + ' open MCQs');
