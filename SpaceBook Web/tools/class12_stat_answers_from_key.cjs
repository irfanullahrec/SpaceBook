/* Write tools/class12_answers/stat/uNN.json from the Statistics book's own ANSWERS pages:
 *   true/false, fill-in and MCQ keys ("4.3 (i) b (ii) a …") become the answers of the objective items;
 *   numerical questions point at their printed answer paragraph ({p: [...]});
 *   descriptive questions without a printed answer take SpaceBook answers from tools/class12_answers/stat/theory.json
 *   (keyed by question number, e.g. "4.4"). Questions still unanswered are listed.
 * usage: node tools/class12_stat_answers_from_key.cjs */
const fs = require('fs'), path = require('path');
const {load, parseUnit, plain} = require('./class12_book_exercise_parse.cjs');
const dir = path.join(__dirname, 'class12_answers', 'stat');
fs.mkdirSync(dir, {recursive: true});
const theoryFile = path.join(dir, 'theory.json');
const theory = fs.existsSync(theoryFile) ? JSON.parse(fs.readFileSync(theoryFile, 'utf8')) : {};
const ROMAN = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv'];
// "(i) T (ii) F …" → ['T', 'F', …]
const parts = text => {
  const out = []; const rx = /\((x{0,1}(?:ix|iv|v?i{0,3}))\)\s*/g; let m, last = null, lastIdx = 0;
  const marks = [];
  while ((m = rx.exec(text))) if (m[1]) marks.push({n: ROMAN.indexOf(m[1]), at: m.index, end: rx.lastIndex});
  marks.forEach((mk, k) => { out[mk.n] = text.slice(mk.end, k + 1 < marks.length ? marks[k + 1].at : undefined).trim(); });
  return out;
};
const missing = [];
for (const ch of load('stat')) {
  if (!/^\d+$/.test(String(ch.number))) continue;
  const unit = ch.number;
  const {out} = parseUnit('stat', unit);
  const para = r => ch.sections.find(s => s.id === r.sectionId).paras[r.index];
  const key = {};
  for (const s of ch.sections) if (/-answers-/.test(s.id)) s.paras.forEach((p, i) => {
    const m = plain(p.text).match(/^(\d+\.\d+)\s+([\s\S]*)$/);
    if (m) key[m[1]] = {ref: [s.id, i], text: m[2]};
  });
  const answers = {};
  const groupNo = q => q.group ? (plain(para(q.group).text).match(/^(\d+\.\d+)/) || [])[1] : null;
  for (const cat of ['mcqs', 'objective']) {
    const seen = {};
    answers[cat] = out[cat].map(q => {
      const g = q.kind === 'match' ? (plain(para(q.q[0]).text).match(/^(\d+\.\d+)/) || [])[1] : groupNo(q); const k = seen[g] = (seen[g] || 0); seen[g]++;
      if (q.kind === 'match' && g && theory[g]) return {s: [].concat(theory[g])};
      const val = g && key[g] ? parts(key[g].text)[k] : undefined;
      const tag = `${unit} ${cat} ${g} (${ROMAN[k]})`;
      if (val === undefined || val === '') { missing.push(tag + ' — no key'); return {c: q.kind === 'fill' ? undefined : '-', s: ['See the worked explanation.'], n: 'No printed key for this item.'}; }
      if (q.kind === 'tf') return {c: /^t/i.test(val) ? 'A' : 'B', s: [(/^t/i.test(val) ? 'True' : 'False') + ' (answer key in the textbook).']};
      if (q.kind === 'fill') return [val.replace(/[.;]\s*$/, ''), 'Answer from the textbook key.'];
      const letter = (val.match(/^\(?([a-d])\)?/i) || [])[1];
      if (!letter) { missing.push(tag + ' — key "' + val + '" not a letter'); return {c: '-', s: ['Key: ' + val], n: 'The printed key is not a choice letter.'}; }
      return {c: letter.toUpperCase(), s: ['Correct choice: (' + letter.toLowerCase() + ') — answer key in the textbook.']};
    });
  }
  let prev = null;
  answers.longQuestions = out.longQuestions.map(q => {
    let no = (plain(para(q.q[0]).text).match(/^(\d+\.\d+)/) || [])[1];
    if (!no && prev) no = prev.split('.')[0] + '.' + (+prev.split('.')[1] + 1); // a question whose number line is not in the text
    prev = no;
    const t = theory[no];
    if (key[no] && t) return {p: [key[no].ref], s: [].concat(t)};
    if (key[no]) return {p: [key[no].ref]};
    if (t) return Array.isArray(t) ? t : [t];
    missing.push(`${no} — ${plain(para(q.q[0]).text).slice(0, 110)}`);
    return ['(answer pending)'];
  });
  for (const k of Object.keys(answers)) if (!answers[k].length) delete answers[k];
  fs.writeFileSync(path.join(dir, 'u' + String(unit).padStart(2, '0') + '.json'), JSON.stringify(answers, null, 1));
}
console.log(missing.length + ' unanswered');
console.log(missing.join('\n'));
