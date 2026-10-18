/* Parse Class 12 book-subject exercises (Pak Studies, Civics, HPE, Islamiat, Urdu, English, …).
 * Paragraph `text` is English (original or translation); numbering and instructions are read from it.
 * usage: node tools/class12_book_exercise_parse.cjs <subject> <unit> [--json] */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..');
const SUBJECTS = {
  stat: {file: 'js/stat_12_data.js', glob: 'STAT_12_DATA', lang: 'en'},
  eng: {file: 'js/english_12_data.js', glob: 'ENGLISH_12_DATA', lang: 'en'},
  urdu: {file: 'js/urdu_12_data.js', glob: 'URDU_12_DATA', lang: 'ur'},
  pakstudy: {file: 'js/pakstudy_12_data.js', glob: 'PAKSTUDY_12_DATA', lang: 'ur'},
  comp: {file: 'js/computer_12_data.js', glob: 'COMP_12_DATA', lang: 'en'},
  civics: {file: 'js/civics_12_data.js', glob: 'CIVICS_12_DATA', lang: 'ur'},
  econ: {file: 'js/economics_12_data.js', glob: 'ECON_12_DATA', lang: 'ur'},
  hpe: {file: 'js/hpe_12_data.js', glob: 'HPE_12_DATA', lang: 'ur'},
  islopt: {file: 'js/islamiat_ikhtiari_12_data.js', glob: 'ISLAMIAT_OPT_12_DATA', lang: 'ur'},
  islhist: {file: 'js/islamic_history_12_data.js', glob: 'ISLAMIC_HISTORY_12_DATA', lang: 'ur'},
  quran: {file: 'js/quran_12_data.js', glob: 'QURAN_12_DATA', lang: 'ur'},
};
const cache = {};
function load(subject) {
  if (cache[subject]) return cache[subject];
  const {file, glob} = SUBJECTS[subject];
  const ctx = {console}; vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(ROOT, file), 'utf8').split('const ' + glob + ' =').join('var ' + glob + ' ='), ctx);
  return (cache[subject] = ctx[glob]);
}
const plain = t => String(t || '').replace(/\\\(|\\\)/g, '').replace(/\s+/g, ' ').trim();
const NUM = {
  digit: /^(?:Q(?:uestion)?\.?\s*\d+\s*[:.)]?|\(?\d+\s*[.):]|\(\d+[ab]?\))\s*/i,
  roman: /^\(?(?:i|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii|xiii|xiv|xv|xvi|xvii|xviii|xix|xx)[.)]\s+|^(?:i|ii|iii|iv|vi|vii|viii|ix|xi|xii)\s+(?=[A-Z])/i,
  letter: /^\(?(?:[a-z]|'ayn)[.)]\s+/, // English letters, or the Urdu abjad order transliterated (… m, n, s, 'ayn, f, s, q, r)
};
const styleOf = t => NUM.digit.test(t) ? 'digit' : NUM.roman.test(t) ? 'roman' : NUM.letter.test(t) ? 'letter' : '';
const isOptionPair = t => (t.match(/\(\s*[a-dA-D]\s*\)/g) || []).length >= 2 && /^\(\s*[aAcC]\s*\)/.test(t); // "(a) … (b) …" printed two per line
const isOptionLine = t => (t.match(/\(\s*[a-dA-D]\s*\)|(?:^|\s)[a-dA-D]\.\s/g) || []).length >= 3 && /^\(?\s*[aA]\s*[.)]/.test(t);
const KIND = [
  [/four (answers|options|choices)|(on|against) the (most )?(correct|suitable|right) answer/i, 'mcq'],
  [/fill (in )?the blanks?|fill in|complete the sentences|blanks?/i, 'fill'],
  [/(statement|sentence|following|indicate|mark|write|choose|state)[\s\S]*\btrue\b[\s\S]*\bfalse\b|\btrue\b[\s\S]*\bfalse\b[\s\S]*(statement|sentence)|true\s*\/\s*false|correct and incorrect|correct\W+or\W+incorrect|right or wrong|yes\/no|yes or no|\(✓\)|✓|✗|tick|mark the correct (sentences|statements)|correct\W+(sentences|statements)?\W*and\W+(the\s+)?wrong/i, 'tf'],
  [/match|column/i, 'match'],
  [/choose|suitable answers?|correct (option|answer|one|alternative)|select (one|the correct)|encircle|multiple[- ]choice|mcqs?\b/i, 'mcq'],
  [/notes? on the following|write (short )?notes\s*:?\s*$/i, 'long'],
  [/short (answers?|questions?)|brief(ly)? answers?/i, 'short'],
  [/detail(ed)? answers?|long (answers?|questions?)|essay[- ]type|essay questions|descriptive|following questions in detail|in detail\s*:?\s*$/i, 'long'],
  [/^practical activit|^activit(y|ies)\b(?!\s*:\s*\S)|^project\b/i, 'activity'],
  [/answers? (to|of) the following|following questions|write answers/i, 'short'],
];
const CATEGORY = {fill: 'objective', tf: 'objective', match: 'objective', mcq: 'mcqs', short: 'shortQuestions', long: 'longQuestions', activity: 'activities'};
function instruction(t) {
  if (t.length > 220 || NUM.roman.test(t) || NUM.letter.test(t) || /[؀-ۿ]{3}/.test(t)) return null; // quoted verses ("… their false gods:") are questions // lettered/roman lines are items, not instructions
  const body = t.replace(NUM.digit, '');
  if (/\?\s*$/.test(body) && !/following/i.test(body)) return null;
  for (const [rx, kind] of KIND) if (rx.test(body)) return kind;
  return null;
}
const isHeader = t => /^(exercise( questions)?|model paper questions|exercise questions|questions?|مشق)\s*:?$/i.test(t);
function exerciseSections(ch, subject) {
  return ch.sections.filter(s => Array.isArray(s.paras) && s.paras.length && !/-answers-/.test(s.id) && ((subject === 'comp' && /-activities/.test(s.id)) ||/exercise|model|مشق|سوالات|review/i.test(s.id + ' ' + s.title) ||
    s.paras.some(p => /^(exercise( questions)?|model paper questions)\s*:?$/i.test(plain(p.text)))));
}
// English: each unit runs Reading Comprehension → Writing Suggestions → Oral Communication → Vocabulary and Grammar,
// with teaching prose between the tasks. Comprehension questions are numbered; writing/oral tasks and grammar
// activities start with an imperative line, and a grammar activity's numbered items stay with it as one question.
const ENG_HEAD = [[/^reading comprehension\b/i, 'comp'], [/^writing suggestions?\b/i, 'writing'], [/^oral communication\b/i, 'oral'],
  [/^vocabulary and grammar\b/i, 'vocab'], [/^activit(y|ies)( for students)?\s*:?$/i, 'act'], [/^(teacher'?s'? guidelines?|glossary|about the (poet|author|writer)|authors'? profile|khyber pakhtunkhwa textbook board)\b/i, 'skip']];
const ENG_TASK = /^(?:[A-H][.)]\s*|\([a-h]\)\.?\s*)?(use|identify|fill|choose|complete|pick|read|consult|write|white|make|change|combine|correct|rewrite|match|mark|give|find|underline|put|transcribe|join|punctuate|convert|turn|insert|supply|develop|prepare|divide|ask|discuss|arrange|translate|add|look(?! at (?:these|the following|this)\b)|listen|select|classify|name|explain|describe|draw|replace|separate|tick|circle|say|practi[cs]e|pronounce|construct|do|students|which|work|imagine|compose|summari[sz]e|paraphrase|analy[sz]e|compare|search|collect|visit|interview|record|present|deliver|hold|organi[sz]e|conduct|frame|state|try|get)\b/i;
function parseEnglish(ch) {
  const out = {mcqs: [], objective: [], shortQuestions: [], longQuestions: [], activities: []};
  let mode = null, current = null, block = null;
  // a Writing Suggestions block is mostly teaching prose: the task is what follows its "Activity" line, else the whole block
  const closeBlock = () => {
    if (block && block.refs.length) { const refs = block.actAt >= 0 && block.actAt < block.refs.length ? block.refs.slice(block.actAt) : block.refs; out.activities.push({cat: 'activities', kind: 'activity', q: refs, options: []}); }
    block = null;
  };
  for (const s of ch.sections) {
    if (!Array.isArray(s.paras) || /outcomes|-text|poem|-cover|imprint|foreword|acknowledg|toc/.test(s.id)) continue;
    s.paras.forEach((p, i) => {
      const t = plain(p.text), ref = {sectionId: s.id, index: i};
      if (!t || /^\[(editorial|note|source)/i.test(t)) return;
      const head = ENG_HEAD.find(([rx]) => rx.test(t));
      if (head && t.length < 70) {
        if (head[1] === 'act' && mode === 'writing' && block) { block.actAt = block.refs.length; return; }
        if (mode === 'writing') closeBlock();
        mode = head[1] === 'act' ? (mode === 'oral' ? 'oral' : 'vocab') : head[1];
        if (mode === 'writing') block = {refs: [], actAt: -1};
        current = null; return;
      }
      if (!mode || mode === 'skip') return;
      if (mode === 'comp') {
        if (styleOf(t) === 'digit') { current = {cat: 'shortQuestions', kind: 'short', q: [ref], options: []}; out.shortQuestions.push(current); }
        else if (current && !/^answer the (following )?questions?\s*:?$/i.test(t)) current.q.push(ref);
        return;
      }
      if (mode === 'writing') { block.refs.push(ref); return; }
      if (mode === 'oral') {
        if (!current) { current = {cat: 'activities', kind: 'activity', q: [ref], options: []}; out.activities.push(current); }
        else current.q.push(ref);
        return;
      }
      // vocabulary and grammar
      if (current && /^[a-d][.)]\s/.test(t)) { current.q.push(ref); return; } // answer choices (a. … b. …) of the current item
      if (/^using\b[\s\S]*\b(complete|fill|following|given)\b/i.test(t)) { current = {cat: 'objective', kind: 'grammar', q: [ref], options: []}; out.objective.push(current); return; }
      const lettered = /^(?:[A-H][.)]|\([a-h]\)\.?)\s*\S/.test(t);
      const task = styleOf(t) !== 'digit' && (ENG_TASK.test(t) && (lettered || !/\?\s*$/.test(t.replace(/\(.*\)$/, ''))) || lettered && /following|[?:]\s*$/i.test(t) || /in the following|the following (words|sentences)/i.test(t));
      if (task) { current = {cat: 'objective', kind: 'grammar', q: [ref], options: []}; out.objective.push(current); return; }
      if (current) current.q.push(ref);
    });
  }
  if (mode === 'writing') closeBlock();
  return out;
}
function parseUnit(subject, unit) {
  const ch = load(subject).find(c => String(c.number) === String(unit));
  if (!ch) throw new Error('no unit ' + unit);
  if (subject === 'eng') return {ch, out: parseEnglish(ch)};
  const out = {mcqs: [], objective: [], shortQuestions: [], longQuestions: [], activities: []};
  let group = null, current = null, started = false, paused = false;
  for (const s of exerciseSections(ch, subject)) {
    s.paras.forEach((p, i) => {
      const t = plain(p.text);
      if (!t || /^\[(editorial|note|source)/i.test(t)) return;
      if (/^(exercise( questions)?|model paper questions)\s*:?$/i.test(t)) { started = true; paused = false; group = null; current = null; return; }
      // lesson text resuming after an exercise block printed mid-chapter ("… continued", "(continued from p.27)", "Explanation")
      if (started && (/^(…|\.\.\.|\(continued)/i.test(t) || /^(explanation|translation|guidance for teachers|تشریح|ترجمہ)\s*:?$/i.test(t))) { paused = true; group = null; current = null; return; }
      // Urdu: grammar notes printed between the exercise questions ("Punctuation marks (Rumūz-e-Awqāf):" …) pause the
      // exercise until the next numbered question
      if (subject === 'urdu' && started && /^punctuation marks\b/i.test(t)) { paused = true; group = null; current = null; return; }
      if (subject === 'urdu' && paused && /^\(?\d+\s*[.)]\s/.test(t)) { paused = false; group = null; current = null; }
      if (subject === 'urdu' && paused) return; // grammar-note lines that only look like instructions
      if (!started && !/exercise|model|مشق|سوالات/i.test(s.id + ' ' + s.title) && !(subject === 'comp' && /-activities/.test(s.id))) return;
      if (/^(short|long|objective|important) questions\s*:?$/i.test(t)) { started = true; group = {kind: /short/i.test(t) ? 'short' : /objective/i.test(t) ? 'mcq' : 'long', style: '', ref: null}; current = null; return; }
      const ref = {sectionId: s.id, index: i};
      // Economics model papers: "Objective (Objective)", "Subjective (Subjective), Section I (Section I)", "Section II (Section II)"
      if (/^objective\s*\(objective\)\s*$/i.test(t)) { started = true; paused = false; group = {kind: 'mcq', style: '', ref: null}; current = null; return; }
      if (/^(subjective\b.*)?section\s+i\b(?!i)/i.test(t)) { started = true; paused = false; group = {kind: 'short', style: '', ref: null}; current = null; return; }
      if (/^section\s+ii\b/i.test(t)) { started = true; paused = false; group = {kind: 'long', style: '', ref: null}; current = null; return; }
      // printed answer lines (Economics model papers)
      if (/^(A|Ans(wer)?)\s*[.:]\s/.test(t) && current) { (current.printed = current.printed || []).push(ref); return; }
      // one choice per paragraph ("… is: ⏎ a. … ⏎ b. … ⏎ c. … ⏎ d. …"): accept the letters in order after a question ending in ":" or "—"
      const single = current && current.kind === 'mcq' && t.match(/^\(?([a-dA-D])[.)]\s/);
      const labels = x => (x.match(/(?:^|\s)\(?[a-dA-D][.)]\s/g) || []).length;
      if (single && labels(t) === 1 && single[1].toLowerCase() === String.fromCharCode(97 + current.options.length) && current.options.every(r => labels(plain(ch.sections.find(x => x.id === r.sectionId).paras[r.index].text)) === 1)) {
        const lr = current.q[current.q.length - 1], lt = plain(ch.sections.find(x => x.id === lr.sectionId).paras[lr.index].text);
        if (current.options.length || single[1].toLowerCase() === 'a' || /[:—–]\s*$/.test(lt) || styleOf(plain(ch.sections.find(x => x.id === current.q[0].sectionId).paras[current.q[0].index].text)) === 'digit') { current.options.push(ref); return; }
      }
      // a lone "(c) …" line after a printed pair "(a) … (b) …" (Economics)
      if (single && current.options.length && single[1].toLowerCase() === String.fromCharCode(97 + current.options.reduce((n, r) => n + labels(plain(ch.sections.find(x => x.id === r.sectionId).paras[r.index].text)), 0))) { current.options.push(ref); return; }
      // a question printed under no MCQ heading whose choices follow as "(a) … (b) …" becomes an MCQ
      if (current && current.kind !== 'mcq' && !current.options.length && current.cat !== 'activities' && isOptionPair(t) && labels(t) >= 2) {
        out[current.cat].splice(out[current.cat].indexOf(current), 1);
        current.kind = 'mcq'; current.cat = 'mcqs'; out.mcqs.push(current);
        if (group) group.kind = 'mcq';
        current.options.push(ref); return;
      }
      if ((isOptionLine(t) || (current && current.kind === 'mcq' && isOptionPair(t))) && current) { current.options.push(ref); return; }
      if (started && /^\([^()]*[,،][^()]*\)\s*$/.test(t) && !current) return; // word bank printed under a fill-in instruction
      if (started && /^activit(y|ies)\s*:\s*\S/i.test(t)) { group = {kind: 'activity', style: '', ref}; current = {cat: 'activities', kind: 'activity', q: [ref], options: []}; out.activities.push(current); return; }
      const kind = instruction(t);
      if (kind) {
        started = true; paused = false;
        group = {kind, style: '', ref};
        current = null;
        if (kind === 'match') { current = {cat: 'objective', kind, q: [ref], options: []}; out.objective.push(current); }
        return;
      }
      if (!started || paused) return;
      // Statistics numbers every question "4.17 …"; anything else (parts, data lines, tables' captions) continues it
      if (subject === 'stat' && current && current.cat === 'longQuestions' && !/^\d+\.\d+\s/.test(t)) { current.q.push(ref); return; }
      const style = styleOf(t);
      // code or a numbered list quoted inside a roman-numbered MCQ ("vii. Consider the following two pieces of code … 1. switch …")
      if (current && current.kind === 'mcq' && !current.options.length && group && group.kind === 'mcq' && group.style === 'roman' && style === 'digit' && !/^(Q(uestion)?\.?\s*)\d/i.test(t)) { current.q.push(ref); return; }
      // A differently numbered question after a list group ends that group (e.g. long questions 6–10 after group 5).
      if (group && group.style && style && style !== group.style && !(group.kind === 'match') ) {
        if (style === 'digit') group = null;
      }
      if (group && group.kind === 'match' && style) group = null;
      // numbering that restarts lower inside a digit-numbered group (… 7, 8, then 6, 7 …) begins new (long) questions
      const numNow = (t.match(/^\(?(\d+)[.)]/) || [])[1];
      if (group && style === 'digit' && group.style === 'digit' && numNow && group.last && +numNow <= group.last) group = null;
      if (group && style === 'digit' && numNow) group.last = +numNow;
      const lastText = current && plain(ch.sections.find(x => x.id === current.q[current.q.length - 1].sectionId).paras[current.q[current.q.length - 1].index].text);
      if (current && !current.options.length && /:\s*$/.test(lastText || '') && !instruction(t) && current.kind !== 'match' && !(subject === 'stat' && /^\d+\.\d+\s/.test(t))) { current.q.push(ref); return; } // "Describe any two:" + list line
      if (!style && current && !(current.kind === 'mcq' && current.options.length)) { current.q.push(ref); return; } // continuation
      const kindNow = group ? group.kind : 'long';
      if (group && !group.style) group.style = style;
      current = {cat: CATEGORY[kindNow], kind: kindNow, q: [ref], options: [], group: group && group.ref};
      out[current.cat].push(current);
    });
  }
  return {ch, out};
}
module.exports = {load, parseUnit, plain, SUBJECTS};
if (require.main === module) {
  const [subject, unit, flag] = process.argv.slice(2);
  const {ch, out} = parseUnit(subject, unit);
  const para = r => ch.sections.find(s => s.id === r.sectionId).paras[r.index];
  if (flag === '--json') { console.log(JSON.stringify(out)); return; }
  for (const [k, list] of Object.entries(out)) {
    if (!list.length) continue;
    console.log('== ' + k + ' (' + list.length + ')');
    list.forEach((item, n) => {
      console.log((n + 1) + '] [' + item.kind + '] ' + item.q.map(r => plain(para(r).text)).join(' ⏎ '));
      item.options.forEach(r => console.log('     ' + plain(para(r).text)));
      (item.printed || []).forEach(r => console.log('     PRINTED: ' + plain(para(r).text).slice(0, 160)));
    });
  }
}
