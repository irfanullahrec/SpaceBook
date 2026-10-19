'use strict';
/* Proof that lazy loading changes nothing the student sees: renders every chapter and tab of every subject on the eager page
 * (index.html) and on the lazy page (lazy.html) in the same run, and compares tab labels and a hash of the rendered HTML.
 *   node --max-old-space-size=8192 tools/build/lazy_parity.js [--reverse]
 * Exit 1 on any difference. --reverse renders the subjects in the opposite order on both pages (the app itself leaks state
 * between subjects, so each order is compared with itself, never with the other). Takes about 4 minutes. */
const { spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const snap = path.join(ROOT, 'tools', 'snapshot_html.js');
const extra = process.argv.includes('--reverse') ? ['--reverse'] : [];
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sb_lazy_parity_'));
const run = (args, label) => {
  const r = spawnSync(process.execPath, ['--max-old-space-size=8192', snap, ...args], { cwd: ROOT, encoding: 'utf8', maxBuffer: 1 << 28 });
  const last = String(r.stdout).split('\n').filter(l => /^(snapshot|lazy files|compared)/.test(l));
  console.log(label + ': ' + (last.join(' | ') || String(r.stderr).slice(0, 300)));
  return r;
};
const e = run(['--out', path.join(tmp, 'eager')].concat(extra), 'eager page');
const l = run(['--page', 'lazy.html', '--out', path.join(tmp, 'lazy')].concat(extra), 'lazy page ');
const c = run(['--compare', path.join(tmp, 'eager'), path.join(tmp, 'lazy')], 'comparison');
if (c.status !== 0) { String(c.stdout).split('\n').slice(1, 25).forEach(x => console.log(x)); }
fs.rmSync(tmp, { recursive: true, force: true });
console.log(c.status === 0 && e.status === 0 && l.status === 0 ? 'lazy parity: IDENTICAL' : 'lazy parity: DIFFERENT');
process.exit(c.status === 0 && e.status === 0 && l.status === 0 ? 0 : 1);
