'use strict';
/* HTML snapshot baseline (no browser). For every class x subject x chapter x tab, renders the tab in the app
 * sandbox and stores the tab labels in order plus a hash of the rendered HTML (whitespace-normalised).
 *   node --max-old-space-size=8192 tools/snapshot_html.js [--out tests/baseline/html-2026-10-19] [--only cls9,cls12-phy]
 *   node tools/snapshot_html.js --compare <dirA> <dirB>      lists every chapter/tab whose labels or hash differ
 * This checks generated markup, not layout, fonts or what add-on scripts do to the live DOM afterwards: it
 * complements, and does not replace, the Playwright baseline (tests/baseline/run.js). Dev-only. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { ROOT } = require('./lib/app_sandbox');
const args = process.argv.slice(2);
const opt = k => { const i = args.indexOf('--' + k); return i < 0 ? null : args[i + 1]; };
const sha = s => crypto.createHash('sha256').update(s).digest('hex').slice(0, 16);

if (args[0] === '--compare') {
  const [A, B] = [path.resolve(args[1]), path.resolve(args[2])];
  let files = 0, tabs = 0, diffs = [];
  for (const c of fs.readdirSync(A)) {
    if (!fs.statSync(path.join(A, c)).isDirectory()) continue;
    for (const f of fs.readdirSync(path.join(A, c))) {
      const a = JSON.parse(fs.readFileSync(path.join(A, c, f), 'utf8'));
      const pb = path.join(B, c, f);
      if (!fs.existsSync(pb)) { diffs.push(`${c}/${f}: missing in B`); continue; }
      const b = JSON.parse(fs.readFileSync(pb, 'utf8'));
      files++;
      a.chapters.forEach((ch, i) => {
        const o = b.chapters[i];
        if (!o) return diffs.push(`${c}/${f} ch${i}: missing in B`);
        if (ch.tabLabels.join('|') !== o.tabLabels.join('|')) diffs.push(`${c}/${f} ch${i}: tab labels differ`);
        ch.tabs.forEach((t, j) => { tabs++; if (!o.tabs[j] || o.tabs[j].hash !== t.hash) diffs.push(`${c}/${f} ch${i} tab ${t.id}: html differs`); });
      });
    }
  }
  console.log(`compared ${files} subjects, ${tabs} tab renders: ${diffs.length} differences (${(100 * (1 - diffs.length / Math.max(tabs, 1))).toFixed(2)} % identical)`);
  diffs.slice(0, 60).forEach(d => console.log('  ' + d));
  process.exit(diffs.length ? 1 : 0);
}

const { load } = require('./lib/app_sandbox');
const OUT = path.resolve(ROOT, opt('out') || path.join('tests', 'baseline', 'html-' + new Date().toISOString().slice(0, 10)));
const ONLY = opt('only') ? opt('only').split(',') : null;
const app = load();
const subjects = app.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name })))')
  .filter(s => !ONLY || ONLY.includes(s.classId) || ONLY.includes(s.id));
let nCh = 0, nTab = 0, nErr = 0;
const t0 = Date.now();
for (const s of subjects) {
  const rec = { classId: s.classId, subjectId: s.id, name: s.name, errors: [], chapters: [] };
  const step = code => { try { return app.run(code, 120000); } catch (e) { rec.errors.push(e.message.slice(0, 200)); } };
  step(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`);
  const chs = step(String.raw`(() => { const seen = new Set(), out = [];
    for (const m of $('dashboard-body').innerHTML.matchAll(/onclick="(select\w*(?:Chapter|Unit|Lesson|Page)\([^"]*)"/g)) if (!seen.has(m[1])) { seen.add(m[1]); out.push(m[1]); }
    return out; })()`) || [];
  chs.forEach((oc, i) => {
    step(`state.activeSubjTab = null; ${oc.replace(/&#39;|&quot;/g, "'")}`);
    const tabOcs = step(String.raw`[...new Set([...document.getElementById('subjectTopicArea').innerHTML.matchAll(/onclick="(switchSubjectTab\([^"]*)"/g)].map(m => m[1]))]`) || [];
    const labels = step(String.raw`[...document.getElementById('subjectTopicArea').innerHTML.matchAll(/data-tab="([^"]+)"[^>]*>([\s\S]*?)<\/button>/g)].map(m => m[2].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim())`) || [];
    const ch = { idx: i, tabLabels: labels, tabs: [] };
    for (const t of tabOcs) {
      step(t.replace(/&#39;|&quot;/g, "'"));
      const html = step(`document.getElementById('subjTabContent').innerHTML`) || '';
      ch.tabs.push({ id: (t.match(/'[^']*',\s*'([^']+)'/) || [])[1] || t, len: html.length, hash: sha(html.replace(/sbq(\d+)_[a-z0-9]{4}/g, 'sbq$1_ID').replace(/\s+/g, ' ')) }); // sb_mcq ids are random per render
      nTab++;
    }
    rec.chapters.push(ch); nCh++;
  });
  nErr += rec.errors.length;
  fs.mkdirSync(path.join(OUT, s.classId), { recursive: true });
  fs.writeFileSync(path.join(OUT, s.classId, s.id + '.json'), JSON.stringify(rec) + '\n');
}
console.log(`snapshot ${path.relative(ROOT, OUT)}: ${subjects.length} subjects, ${nCh} chapters, ${nTab} tab renders, ${nErr} step errors, ${((Date.now() - t0) / 60000).toFixed(1)} min`);
