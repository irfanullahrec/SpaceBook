'use strict';
/* Content lints (Phase 6): what a student or a printed paper could be shown that is not real, sourced content.
 *   node --max-old-space-size=8192 tools/content_lint.js            print the report
 *   node tools/content_lint.js --write-baseline                      record the current numbers in tests/contract/content_lint.json
 *   node tools/content_lint.js --check                               exit 1 when a number got worse than the baseline (CI)
 * It reads the same question pool the Papers module uses (getCurriculumQuestionsForCategory, MCQs) for every subject, plus the
 * generated "Board SLO" items and placeholder media. The numbers are the removal/review lists the owner approves
 * (docs/CONTENT_REVIEW.md); the baseline only stops them getting worse, it does not say they are fine. Dev-only. */
const fs = require('fs'), path = require('path');
const { load, ROOT } = require('./lib/app_sandbox');
const args = process.argv.slice(2);
const BASE = path.join(ROOT, 'tests', 'contract', 'content_lint.json');
const app = load({ page: 'lazy.html', quiet: true });
const run = (c, t) => app.run(c, t || 120000);

const subjects = run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name })))');
const norm = s => String(s || '').replace(/<[^>]+>/g, ' ').replace(/[^\p{L}\p{N}]+/gu, ' ').trim().toLowerCase();

// ---- 1. Papers MCQ pool per subject: keys, skew, duplicate stems
const bank = {};
let total = 0, noKey = 0, skewedSubjects = [], dupTotal = 0;
for (const s of subjects) {
  let list;
  try { list = JSON.parse(run(`JSON.stringify(getCurriculumQuestionsForCategory(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)}, 'mcqs').map(q => ({ a: q.ans, q: q.q, n: (q.opts || []).length })))`)); } catch (e) { continue; }
  if (!list.length) continue;
  const dist = [0, 0, 0, 0, 0];
  list.forEach(q => { if (q.a === null || q.a === undefined) dist[4]++; else dist[Math.min(q.a, 3)]++; });
  const keyed = list.length - dist[4];
  const top = keyed ? Math.max(...dist.slice(0, 4)) / keyed : 0;
  const seen = new Map(); let dup = 0;
  list.forEach(q => { const k = norm(q.q); if (seen.has(k)) dup++; else seen.set(k, 1); });
  bank[s.id] = { mcqs: list.length, noKey: dist[4], skewPct: Math.round(top * 100), dupStems: dup };
  total += list.length; noKey += dist[4]; dupTotal += dup;
  if (keyed >= 20 && top >= 0.8) skewedSubjects.push(s.id);
}

// ---- 2. generated Board SLO items (Class 9-style Maths topics): per unit count by kind
const generated = { sections: 0, mcqs: 0, shortQuestions: 0, longQuestions: 0 };
const genByClass = {};
for (const cls of ['cls9', 'cls10']) {                              // the classes whose Maths topics show these items in the Board SLO tab (Classes 11 and 12 have their own banks)
  const r = run(`(() => { const out = { sections: 0, mcqs: 0, shortQuestions: 0, longQuestions: 0 }; const list = getMathChapterList(${JSON.stringify(cls)}) || []; for (const u of list) for (const sec of (u.sections || [])) { const d = getTopicSpecificSLOs(sec, u); const g = k => (d[k] || []).filter(x => x.generated).length; const n = g('mcqs') + g('shortQuestions') + g('longQuestions'); if (n) { out.sections++; out.mcqs += g('mcqs'); out.shortQuestions += g('shortQuestions'); out.longQuestions += g('longQuestions'); } } return JSON.stringify(out); })()`);
  genByClass[cls] = JSON.parse(r);
}
Object.values(genByClass).forEach(g => { for (const k of Object.keys(generated)) generated[k] += g[k]; });

// ---- 3. placeholder media in data
const placeholder = JSON.parse(run(`(() => { const rows = []; const book = ISLAMYAT_DATA || []; for (const ch of book) if (ch.video && !sbRealVideo(ch.video)) rows.push(ch.title || ch.id); return JSON.stringify(rows); })()`));

const metrics = {
  paperMcqs: total, paperMcqsWithoutKey: noKey, paperSubjectsSkewedOver80: skewedSubjects.length, paperDuplicateStems: dupTotal,
  generatedSloItems: generated.mcqs + generated.shortQuestions + generated.longQuestions, generatedSloSections: generated.sections,
  placeholderVideoChapters: placeholder.length,
};

if (args.includes('--write-baseline')) {
  fs.mkdirSync(path.dirname(BASE), { recursive: true });
  fs.writeFileSync(BASE, JSON.stringify({ note: 'Content lint numbers (tools/content_lint.js). The gate stops them getting worse; it does not say they are acceptable: see docs/CONTENT_REVIEW.md.', metrics }, null, 1) + '\n');
  console.log('wrote ' + path.relative(ROOT, BASE));
}

if (!args.includes('--check')) {
  console.log('Papers MCQ pool: ' + total + ' questions in ' + Object.keys(bank).length + ' subjects; ' + noKey + ' without a key (printed as "key not available"); ' + dupTotal + ' repeated stems');
  console.log('subjects where >= 80 % of keyed MCQs share one answer position (' + skewedSubjects.length + '): ' + skewedSubjects.join(', '));
  console.log('generated "Board SLO" items (templates from the section title, first option always right): ' + generated.mcqs + ' MCQs, ' + generated.shortQuestions + ' short, ' + generated.longQuestions + ' long in ' + generated.sections + ' topics');
  Object.entries(genByClass).forEach(([c, g]) => console.log('   ' + c + ': ' + g.sections + ' topics, ' + g.mcqs + ' MCQs, ' + g.shortQuestions + ' SQs, ' + g.longQuestions + ' LQs'));
  console.log('Islamiat chapters whose video is a placeholder (' + placeholder.length + '): shown as "no video" now');
  if (args.includes('--json')) console.log(JSON.stringify({ metrics, bank, genByClass, placeholder }, null, 1));
}

if (args.includes('--check')) {
  const base = JSON.parse(fs.readFileSync(BASE, 'utf8')).metrics;
  const worse = Object.keys(metrics).filter(k => metrics[k] > base[k]);
  worse.forEach(k => console.log('WORSE  ' + k + ': ' + base[k] + ' -> ' + metrics[k]));
  const better = Object.keys(metrics).filter(k => metrics[k] < base[k]);
  better.forEach(k => console.log('better ' + k + ': ' + base[k] + ' -> ' + metrics[k] + ' (run --write-baseline to keep the gain)'));
  console.log(worse.length ? 'content lint: WORSE than the baseline' : 'content lint: no worse than the baseline');
  process.exit(worse.length ? 1 : 0);
}
