/* Parse Class 12 textbook exercise records into question lists.
 * usage: node tools/class12_exercise_parse.cjs <subject> <unit> [--json]
 * subject: phys | chem   — prints the parsed questions so answers can be authored in order. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..');
const SUBJECTS = {
  phys: {file: 'js/phys_12_data.js', glob: 'PHYS_12_DATA'},
  chem: {file: 'js/chem_12_data.js', glob: 'CHEM_12_DATA'},
};
const cache = {};
function load(subject) {
  if (cache[subject]) return cache[subject];
  const {file, glob} = SUBJECTS[subject];
  const ctx = {console}; vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(ROOT, file), 'utf8').split('const ' + glob + ' =').join('var ' + glob + ' ='), ctx);
  return (cache[subject] = ctx[glob]);
}
const plain = t => String(t || '').replace(/\\\(|\\\)/g, '').trim();
const OPTION = /^\(?([A-Da-d])[.)]\s*/;
const HEADINGS = [
  [/choose the (best|correct)|multiple[- ]choice|^mcqs?\b|^exercise\b|encircle/i, 'mcqs'],
  [/conceptual questions?|short questions?|short answers?/i, 'shortQuestions'],
  [/comprehensive questions?|detailed questions?|detail(ed)? answers?|long questions?|descriptive/i, 'longQuestions'],
  [/numerical (problems?|questions?)|^numericals?\b|^problems?\b/i, 'numericals'],
  [/^project\b|^activit(y|ies)\b(?!\s*:)/i, 'activities'],
  [/key points|glossary|summary|society,? technology/i, 'skip'],
];
const isHeading = text => {
  const t = plain(text);
  if (t.length > 90) return null;
  for (const [rx, cat] of HEADINGS) if (rx.test(t)) return cat;
  return null;
};
function exerciseSections(ch, subject) {
  return ch.sections.filter(s => Array.isArray(s.paras) && s.paras.length &&
    /exercise|mcq|conceptual|comprehensive|numerical|short and detailed|detailed questions|review/i.test(s.id + ' ' + s.title) &&
    !/solved|answer-key|correction|structures|answers of mcqs/i.test(s.id + ' ' + s.title));
}
function parseUnit(subject, unit) {
  const ch = load(subject).find(c => String(c.number) === String(unit));
  if (!ch) throw new Error('no unit ' + unit);
  const out = {mcqs: [], shortQuestions: [], longQuestions: [], numericals: [], activities: []};
  let cat = null, current = null;
  for (const s of exerciseSections(ch, subject)) {
    s.paras.forEach((p, i) => {
      const text = plain(p.text);
      if (!text || /^\[(editorial|note|source)/i.test(text)) return;
      const head = isHeading(text);
      if (head) { cat = head; current = null; return; }
      if (cat === 'skip' || !cat) return;
      const ref = {sectionId: s.id, index: i};
      const opt = text.match(OPTION);
      if (opt && current && cat === 'mcqs' && !/^\d/.test(text)) { current.options.push(ref); return; }
      if (/^answer\b|^\(?ans[.:]/i.test(text) && current) { current.printedAnswer = ref; return; }
      if (cat === 'mcqs') {
        // a stem paragraph after an option-less question (e.g. "A spectrum is shown below.") continues it
        if (current && !current.options.length && !/^\[?\d+[.)]\]?\s/.test(text)) { current.q.push(ref); return; }
        current = {q: [ref], options: []}; out.mcqs.push(current); return;
      }
      // continuation lines (no leading number) attach to the previous question;
      // roman-numbered lines after a digit-numbered question are its parts.
      const roman = /^\[?[ivx]+[.)]\]?\s/i.test(text), digit = /^\[?\d+[.)]\]?\s/.test(text);
      if (current && ((!roman && !digit && !/^Q\.?\s*\d/i.test(text)) || (roman && current.style === 'digit'))) { current.q.push(ref); return; }
      current = {q: [ref], options: [], style: digit ? 'digit' : roman ? 'roman' : ''}; out[cat].push(current);
    });
  }
  return {ch, out};
}
module.exports = {load, parseUnit, plain};
if (require.main === module) {
  const [subject, unit, flag] = process.argv.slice(2);
  const {ch, out} = parseUnit(subject, unit);
  const para = r => ch.sections.find(s => s.id === r.sectionId).paras[r.index];
  if (flag === '--json') { console.log(JSON.stringify(out)); return; }
  for (const [k, list] of Object.entries(out)) {
    if (!list.length) continue;
    console.log('== ' + k + ' (' + list.length + ')');
    list.forEach((item, n) => {
      console.log((n + 1) + '] ' + item.q.map(r => plain(para(r).text)).join(' ⏎ '));
      item.options.forEach(r => console.log('     ' + plain(para(r).text)));
      if (item.printedAnswer) console.log('     PRINTED: ' + plain(para(item.printedAnswer).text));
    });
  }
}
