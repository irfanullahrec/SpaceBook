/* Build js/<subject>12_exercise_banks.js for Class 12 book subjects (Pak Studies, Civics, HPE, Islamiat, Urdu, English, …)
 * from tools/class12_book_exercise_parse.cjs + authored answers in tools/class12_answers/<subject>/uNN.json.
 * Answer item forms:  ["B","explanation",...] for MCQ and true/false/yes-no (A = True/Yes, B = False/No);
 *                      ["step",...] or "short answer" for fill-in, matching, short, long and activity items;
 *                      null when the book prints the answer (Economics model papers) and it is correct — a whole
 *                      category can be given as "printed";
 *                      {c,s,a,n,r,d} for clarifications. "-" letter = no printed choice is correct (needs n).
 * usage: node tools/class12_book_exercise_build.cjs <subject> */
const fs = require('fs'), path = require('path'), vm = require('vm');
const {parseUnit, load, SUBJECTS} = require('./class12_book_exercise_parse.cjs');
const ROOT = path.resolve(__dirname, '..');
const subject = process.argv[2];
const runtime = {window: {}}; vm.createContext(runtime);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'js/class12_exercise_banks.js'), 'utf8'), runtime);
const TX = runtime.window.class12ExerciseText;
const bracket = text => { const r = TX.bracketChoices(text); return r ? r.options : null; };
const dir = path.join(ROOT, 'tools/class12_answers', subject);
const specs = {}, problems = [], warnings = [];
for (const file of fs.readdirSync(dir).filter(f => /^u\d+\.json$/.test(f)).sort()) {
  const unit = String(Number(file.match(/\d+/)[0]));
  const answers = JSON.parse(fs.readFileSync(path.join(dir, file), 'utf8'));
  const {ch, out} = parseUnit(subject, unit);
  const para = r => ch.sections.find(s => s.id === r.sectionId).paras[r.index];
  const items = {};
  for (const [cat, list] of Object.entries(out)) {
    const given = answers[cat] === 'printed' ? list.map(() => null) : answers[cat] || []; // "printed": every item has its printed answer (Economics short questions)
    if (!list.length && !given.length) continue;
    if (given.length !== list.length) { problems.push(`u${unit} ${cat}: ${list.length} questions, ${given.length} answers`); continue; }
    items[cat] = list.map((q, i) => {
      let a = given[i];
      const tag = `u${unit} ${cat} ${i + 1}`;
      const rec = {q: q.q.map(r => [r.sectionId, r.index])};
      if (q.printed) rec.p = q.printed.map(r => [r.sectionId, r.index]);
      // how are the choices printed?
      let mode = null, nOptions = 0;
      const qText = q.q.map(r => TX.stripNumber(para(r).text || '')).join(' ');
      // also MCQ groups that print (yes/no) after every statement
      if (q.kind === 'tf' || (q.kind === 'mcq' && /\((yes|true)\s*\/\s*(no|false)\)\s*[.؟?۔]?\s*$/i.test(qText))) { mode = 'tf'; nOptions = 2; rec.tf = /yes\/no|yes or no|\(yes|ہاں/i.test(qText + ' ' + (q.group ? para(q.group).text : '')) ? 'yn' : 'tf'; }
      else if (q.options.length >= 2 && !q.options.some(r => (String(para(r).text).match(/\(\s*[a-dA-D]\s*\)/g) || []).length >= 2)) { mode = 'o'; nOptions = q.options.length; rec.o = q.options.map(r => [r.sectionId, r.index]); }
      else if (q.options.length >= 1 || (q.kind === 'mcq' && TX.splitInline(qText))) {
        q.q.push(...q.options); rec.q = q.q.map(r => [r.sectionId, r.index]); rec.inline = 1;
        const joined = q.q.map(r => TX.stripNumber(para(r).text || '')).join(' ');
        const sp = TX.splitInline(joined); mode = 'inline'; nOptions = sp ? sp.options.length : 0;
        for (const f of ['urdu', 'pashto']) { const j = q.q.map(r => TX.stripNumber(para(r)[f] || '')).join(' '); if (j && !TX.splitInline(j, true)) warnings.push(`${tag}: ${f} choices not split`); }
      } else if (q.kind === 'mcq' && bracket(qText)) {
        mode = 'ob'; rec.ob = 1; nOptions = bracket(qText).length;
        for (const f of ['urdu', 'pashto']) { const j = q.q.map(r => para(r)[f] || '').join(' '); if (j && !bracket(j)) warnings.push(`${tag}: ${f} bracket choices not found`); else if (j && bracket(j).length !== nOptions) warnings.push(`${tag}: ${f} has ${bracket(j).length} choices vs ${nOptions}`); }
      }
      else if (q.kind === 'mcq' && / \/ /.test(qText)) { // "statement A. / statement B." — choose the correct one
        mode = 'os'; rec.os = 1; nOptions = qText.split(/\s+\/\s+/).length;
        for (const f of ['urdu', 'pashto']) { const j = q.q.map(r => para(r)[f] || '').join(' '); if (j && j.split(/\s+\/\s+/).length !== nOptions) warnings.push(`${tag}: ${f} slash choices differ`); }
      }
      if (q.kind === 'match' || q.kind === 'grammar') {
        // the printed table (matching columns, word lists) that follows the instruction
        const s = ch.sections.find(x => x.id === q.q[0].sectionId);
        const pos = (s.sourceLayout || []).findIndex(l => (l.indices || []).includes(q.q[0].index));
        const after = (s.sourceLayout || []).slice(pos + 1, q.kind === 'grammar' ? pos + 3 : undefined);
        const tbl = after.find(l => l.type === 'sourceDataTable');
        if (tbl) rec.d = tbl.tableId; else if (q.kind === 'match') warnings.push(`${tag}: matching table not found`);
      }
      if (a === null || a === undefined) {
        if (!rec.p) problems.push(`${tag}: null answer but no printed answer`);
        return rec;
      }
      if (typeof a === 'string') a = [a];
      if (Array.isArray(a)) a = (mode && mode !== null) ? {c: a[0], s: a.slice(1)} : {s: a};
      if (a.p) rec.p = a.p; // printed answer paragraphs picked by hand (e.g. a separate Answers page)
      if (a.r) rec.r = a.r;
      if (a.d) rec.d = a.d;
      if (a.n) rec.n = a.n;
      if (a.a) rec.a = a.a;
      rec.s = a.s || [];
      if (q.kind === 'fill' && !rec.a && rec.s.length) rec.a = rec.s[0]; // the filled-in word(s)
      if (!rec.s.length && !rec.p) problems.push(`${tag}: empty answer`);
      if (rec.s.some(x => typeof x !== 'string' || !x.trim())) problems.push(`${tag}: blank step`);
      if (mode) {
        if (nOptions < 2) problems.push(`${tag}: ${nOptions} options`);
        if (a.c === '-') { if (!a.n) problems.push(`${tag}: "-" needs a note`); }
        else {
          const c = String(a.c || '').toUpperCase().charCodeAt(0) - 65;
          if (!(c >= 0 && c < nOptions)) problems.push(`${tag}: bad letter ${a.c}`);
          rec.c = c;
        }
      }
      return rec;
    });
  }
  specs[unit] = {lang: SUBJECTS[subject].lang, items};
}
// Guard against parser drift: answers are paired by position, so each unit's question list is recorded and
// a later change must be accepted explicitly (node … <subject> --accept) after the answers are realigned.
const indexFile = path.join(dir, '_questions.json');
const index = {};
for (const [unit, spec] of Object.entries(specs)) {
  const {ch} = parseUnit(subject, unit);
  const text = ([sid, i]) => (ch.sections.find(s => s.id === sid).paras[i].text || '').slice(0, 70);
  index[unit] = Object.fromEntries(Object.entries(spec.items).map(([cat, list]) => [cat, list.map(it => text(it.q[0]))]));
}
if (fs.existsSync(indexFile) && !process.argv.includes('--accept')) {
  const old = JSON.parse(fs.readFileSync(indexFile, 'utf8'));
  for (const [unit, cats] of Object.entries(old)) for (const [cat, list] of Object.entries(cats)) {
    if (JSON.stringify((index[unit] || {})[cat] || []) !== JSON.stringify(list)) problems.push(`u${unit} ${cat}: question list changed since the answers were written — realign, then rebuild with --accept`);
  }
}
if (warnings.length) console.warn(warnings.join('\n'));
if (problems.length) { console.error(problems.join('\n')); process.exit(1); }
fs.writeFileSync(indexFile, JSON.stringify(index, null, 1));
const outFile = path.join(ROOT, 'js', subject + '12_exercise_banks.js');
fs.writeFileSync(outFile, `/* Generated by tools/class12_book_exercise_build.cjs from tools/class12_answers/${subject}/ — do not edit by hand. */\nregisterClass12ExerciseBanks(${JSON.stringify(subject)}, ${JSON.stringify(specs)});\n`);
console.log('wrote', path.relative(ROOT, outFile), Object.entries(specs).map(([u, s]) => u + ':' + Object.entries(s.items).map(([k, v]) => k.slice(0, 2) + v.length).join('')).join(' '));
