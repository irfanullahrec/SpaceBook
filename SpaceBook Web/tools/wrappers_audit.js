'use strict';
/* Which scripts replace a function that another script defined (wrapping it)? Found by watching every global function while the page's
 * scripts run in order: after each script, a global function whose identity changed was replaced by that script.
 *   node --max-old-space-size=8192 tools/wrappers_audit.js [--page lazy.html] [--check]
 * Replacements made through SBHooks (js/core/hooks.js) are listed separately: they are the intended way. --check exits 1 when any script
 * still replaces a global function itself (the Phase 5 acceptance criterion: no global function is wrapped by another file). Dev-only. */
const { load } = require('./lib/app_sandbox');
const args = process.argv.slice(2);
const page = args.includes('--page') ? args[args.indexOf('--page') + 1] : 'index.html';
const owner = {};                         // global function name -> script that defined it first
const replaced = [];                      // { name, by, previous }
let before = new Map();
const snapshot = sb => { const m = new Map(); for (const k of Object.getOwnPropertyNames(sb)) { let v; try { v = sb[k]; } catch (e) { continue; } if (typeof v === 'function' && !/^[A-Z]/.test(k) || (typeof v === 'function' && /^[A-Z][a-z]/.test(k) && !/^(Object|Array|String|Number|Boolean|Date|RegExp|Error|Promise|Map|Set|Symbol|Function|Proxy|Reflect|JSON|Math)$/.test(k))) m.set(k, v); } return m; };
const app = load({ page, quiet: true, onScript: (src, sb) => {
  const now = snapshot(sb);
  for (const [k, v] of now) {
    if (!before.has(k)) { owner[k] = src; continue; }
    if (before.get(k) !== v) replaced.push({ name: k, by: src, via: v.__sbHooked ? 'hooks' : 'assign' });
  }
  before = now;
} });
const hookList = app.sb.SBHooks ? app.sb.SBHooks.list() : {};
const hooked = new Set(Object.keys(hookList));
const byName = {};
replaced.forEach(r => { (byName[r.name] = byName[r.name] || []).push(r.by.replace(/^js\//, '')); });
console.log('functions replaced by a later script: ' + Object.keys(byName).length + ' (' + replaced.length + ' replacements)');
Object.keys(byName).sort((a, b) => byName[b].length - byName[a].length).forEach(n => console.log('  ' + n.padEnd(34) + byName[n].length + '  ' + byName[n].join(', ') + (hookList[n] ? '   [hooked: ' + hookList[n].join(', ') + ']' : '')));
if (Object.keys(hookList).length) { console.log('registered with SBHooks:'); Object.entries(hookList).forEach(([n, ids]) => console.log('  ' + n.padEnd(34) + ids.length + '  ' + ids.join(', '))); }
if (args.includes('--check')) {
  const bad = replaced.filter(r => r.via !== 'hooks');
  console.log(bad.length ? 'FAIL: ' + bad.length + ' replacement(s) outside SBHooks' : 'ok: every replacement goes through SBHooks');
  process.exit(bad.length ? 1 : 0);
}
