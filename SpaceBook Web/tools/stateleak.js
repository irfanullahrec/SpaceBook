'use strict';
/* Which keys of the app's `state` object change while subjects are opened and their first chapters rendered, i.e. which
 * selections one subject leaves behind for the next (finding ARCH-02, docs/PHASE3_LAZY_LOADING.md).
 *   node --max-old-space-size=8192 tools/stateleak.js [--reverse] [--only=cls12,cls10-math]
 * tools/snapshot_html.js resets the sticky keys this lists before each render. Dev-only. */
const { load } = require(process.cwd() + '/tools/lib/app_sandbox');
const app = load({ page: 'index.html', quiet: true });
const snap = () => app.run(`(() => { const o = {}; for (const k of Object.keys(state)) { const v = state[k]; const t = typeof v; if (v === null || t === 'string' || t === 'number' || t === 'boolean' || t === 'undefined') o[k] = v; else o[k] = '[' + t + (Array.isArray(v) ? ':' + v.length : '') + ']'; } return JSON.stringify(o); })()`);
const init = JSON.parse(snap());
console.log('initial primitive keys:', Object.keys(init).length);
const changed = {};
const subjects = app.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id })))');
const rev = process.argv.includes('--reverse'); if (rev) subjects.reverse();
const only = (process.argv.find(a => a.startsWith('--only=')) || '').slice(7).split(',').filter(Boolean);
for (const s of subjects) {
  if (only.length && !only.includes(s.id) && !only.includes(s.classId)) continue;
  const step = code => { try { return app.run(code, 120000); } catch (e) { return null; } };
  step(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`);
  const chs = step(String.raw`(() => { const seen = new Set(), out = []; for (const m of document.getElementById('dashboard-body').innerHTML.matchAll(/onclick="((?:select\w*(?:Chapter|Unit|Lesson|Page))\([^"]*)"/g)) if (!seen.has(m[1])) { seen.add(m[1]); out.push(m[1]); } return out; })()`) || [];
  chs.slice(0, 3).forEach(oc => {
    step(`state.activeSubjTab = null; ${oc.replace(/&#39;|&quot;/g, "'")}`);
    const tabs = step(String.raw`[...new Set([...document.getElementById('subjectTopicArea').innerHTML.matchAll(/onclick="(switchSubjectTab\([^"]*)"/g)].map(m => m[1]))]`) || [];
    for (const t of tabs) step(t.replace(/&#39;|&quot;/g, "'"));
  });
  const now = JSON.parse(snap());
  for (const k of Object.keys(now)) if (now[k] !== init[k]) (changed[k] = changed[k] || new Set()).add(String(now[k]).slice(0, 40));
  for (const k of Object.keys(init)) if (!(k in now)) (changed[k] = changed[k] || new Set()).add('<deleted>');
}
for (const k of Object.keys(changed)) console.log(k.padEnd(34), 'init=' + String(init[k]).slice(0, 30).padEnd(32), '→', [...changed[k]].slice(0, 5).join(' | '), changed[k].size > 5 ? '… (' + changed[k].size + ' values)' : '');
