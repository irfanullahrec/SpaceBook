'use strict';
/* HTML snapshot baseline (no browser). For every class x subject x chapter x tab, renders the tab in the app
 * sandbox and stores the tab labels in order plus a hash of the rendered HTML (whitespace-normalised).
 *   node --max-old-space-size=8192 tools/snapshot_html.js [--out tests/baseline/html-2026-10-20] [--only cls9,cls12-phy]
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
const app = load({ page: opt('page') || 'index.html' });          // --page lazy.html: the lazy-loading page (tools/build/make_lazy.js)
const subjects = app.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name })))')
  .filter(s => !ONLY || ONLY.includes(s.classId) || ONLY.includes(s.id));
if (args.includes('--reverse')) subjects.reverse();                  // order-dependence check: subjects in the opposite order
let nCh = 0, nTab = 0, nErr = 0;
const t0 = Date.now();
// Three kinds of view (tools/build/measure_lazy.js lists them): the generic reader (130 subjects), the Maths view
// (selectMathChapter, 5 subjects) and pages without chapters (12 pre-school subjects, captured once as 'landing').
// The content element is blanked before every tab renders, so a leftover from the previous subject can never be hashed.
const VIEWS = {
  generic: { area: 'subjectTopicArea', content: 'subjTabContent', chapter: 'select\\w*(?:Chapter|Unit|Lesson|Page)', tab: 'switchSubjectTab',
    tabId: oc => (oc.match(/'[^']*',\s*'([^']+)'/) || [])[1], reset: 'state.activeSubjTab = null; ' },
  math: { area: 'mathTopicArea', content: 'mathTabContent', chapter: 'selectMathChapter', tab: 'switchMathTab', tabId: oc => (oc.match(/\('([^']+)'/) || [])[1], reset: '' },
};
const unesc = oc => oc.replace(/&#39;|&quot;/g, "'");
// The app remembers the last sub-selection (question category, lesson sub-tab, exercise number...) in `state` and the next subject
// inherits it (finding ARCH-02, docs/PHASE3_LAZY_LOADING.md). Each render starts from the values `state` had at load, so a snapshot
// depends only on subject + chapter + tab, never on what was opened before. tools/stateleak.js (kept in the notes) lists these keys.
const STICKY = ['activeSubjLessonSubTab', 'activeSubjWordsSubTab', 'activeSubjExCat', 'activeMathSloCategory', 'activeMathEx', 'class12ExerciseCategory', 'class12StudyCategory'];
const STICKY_INIT = JSON.parse(app.run(`JSON.stringify(${JSON.stringify(STICKY)}.map(k => [k, state[k]]))`));
const RESET = STICKY_INIT.map(([k, v]) => v === undefined ? `delete state[${JSON.stringify(k)}];` : `state[${JSON.stringify(k)}] = ${JSON.stringify(v)};`).join(' ');
for (const s of subjects) {
  const rec = { classId: s.classId, subjectId: s.id, name: s.name, errors: [], chapters: [] };
  const step = code => { try { return app.run(code, 120000); } catch (e) { rec.errors.push(e.message.slice(0, 200)); } };
  step(RESET); step(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`);
  const body = step(`document.getElementById('dashboard-body').innerHTML`) || '';
  const V = body.includes('id="mathTopicArea"') ? VIEWS.math : VIEWS.generic;
  const chs = [...new Set([...body.matchAll(new RegExp('onclick="(' + V.chapter + '\\([^"]*)"', 'g'))].map(m => m[1]))];
  // three kinds of id legitimately vary: sb_mcq ids are a render counter plus random letters; the ids inside Maths diagrams (clipPath,
  // marker, title/aria-labelledby: `m5-eg12-8hz3esv0clipA`) carry a random part per render, so they are renamed in order of first
  // appearance (the id graph is still compared); the "auto" answer ids carry the class of whichever page first opened a book that two
  // classes share (Class 10 Islamiat is the Class 9 book): both pages then use the same stored ids
  const figIds = html => { const m = new Map(); for (const x of html.matchAll(/\bid="(m[a-z]*\d*-[^"]+)"/g)) if (!m.has(x[1])) m.set(x[1], 'fig' + m.size); return m.size ? html.replace(/m[a-z]*\d*-[A-Za-z0-9-]+/g, t => m.get(t) || t) : html; };
  const norm = html => sha(figIds(html).replace(/sbq\d+_[a-z0-9]{4}/g, 'sbqN_ID').replace(/cls\d+-([a-z0-9]+)-auto-/g, 'clsN-$1-auto-').replace(/\s+/g, ' '));
  if (!chs.length) {
    rec.chapters.push({ idx: -1, tabLabels: [], tabs: [{ id: 'landing', len: body.length, hash: norm(body) }] });
    nCh++; nTab++;
  }
  chs.forEach((oc, i) => {
    step(RESET); step(`${V.reset}${unesc(oc)}`);
    const area = step(`document.getElementById('${V.area}').innerHTML`) || '';
    const tabOcs = [...new Set([...area.matchAll(new RegExp('onclick="(' + V.tab + '\\([^"]*)"', 'g'))].map(m => m[1]))];
    const labels = [...area.matchAll(new RegExp('<button[^>]*onclick="' + V.tab + '\\([^"]*"[^>]*>([\\s\\S]*?)<\\/button>', 'g'))].map(m => m[1].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim());
    const ch = { idx: i, tabLabels: labels, tabs: [] };
    for (const t of tabOcs) {
      step(RESET); step(`document.getElementById('${V.content}').innerHTML = ''`);
      step(unesc(t));
      const html = step(`document.getElementById('${V.content}').innerHTML`) || '';
      ch.tabs.push({ id: V.tabId(t) || t, len: html.length, hash: norm(html) });
      nTab++;
    }
    rec.chapters.push(ch); nCh++;
  });
  nErr += rec.errors.length;
  fs.mkdirSync(path.join(OUT, s.classId), { recursive: true });
  fs.writeFileSync(path.join(OUT, s.classId, s.id + '.json'), JSON.stringify(rec) + '\n');
}
console.log(`snapshot ${path.relative(ROOT, OUT)}: ${subjects.length} subjects, ${nCh} chapters, ${nTab} tab renders, ${nErr} step errors, ${((Date.now() - t0) / 60000).toFixed(1)} min`);
if (app.sb.SBLazy) { const st = app.sb.SBLazy.stats(); console.log(`lazy files loaded by the end: ${st.loaded} of ${st.files} (${(st.bytesLoaded / 1e6).toFixed(0)} of ${(st.bytesTotal / 1e6).toFixed(0)} MB)`); }
