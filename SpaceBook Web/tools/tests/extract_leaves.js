'use strict';
/* The part of tools/tests/build_test_bank.js that runs INSIDE the app sandbox (it is written as a function so it can be sent there as text).
 * It walks every CLSn_BOOKS book, and the five Mathematics books that are not CLSn_BOOKS (Classes 5, 6, 7, 8 and 11: MATH_n_DATA chapters -> exercises ->
 * questions -> parts, answered by MATH_n_SOLUTIONS and the printed key MATH_n_BOOK.answers, as js/math5_reader.js ... math11_reader.js show them).
 * It returns the books (title, languages, units with their sections) and one record per question or part that a student can be asked: its text in the
 * book's languages, its options (an inline "a. b. c. d." list, circles, or a) b) lines under a roman part), the heading above it ("SHORT QUESTIONS",
 * "Choose the correct option"), its answer as the Ans button would show it (a solution record, the printed key, a written answer) and the printed page.
 * Classifying and filtering is done by the builder, in plain Node. Dev-only. */
module.exports = function extract() {
  const R = window.MATH6_READER, M = window.SBMcq;
  // MATH_n_SOLUTIONS ids ("s12") repeat from class to class: they are looked up in their own class (msol), never in the shared search
  const stores = Object.keys(window).filter(k => /SOLUTIONS/.test(k) && !/^MATH_\d+_SOLUTIONS$/.test(k)).map(k => window[k]).filter(v => v && typeof v === 'object');
  const isRec = r => r && typeof r === 'object' && (r.answer !== undefined || r.steps);
  const sol = id => { if (!id) return null; for (const s of stores) { const r = s[id]; if (isRec(r)) return r; } return null; };
  const msol = n => id => { const S = window['MATH_' + n + '_SOLUTIONS']; const r = id && S ? S[id] : null; return isRec(r) ? r : null; };
  // Mathematics only: the options of "stem (i) one ii) two iii) three iv) four)" and "stem (i. one ii. two iii. three iv. four)" (Classes 5, 6 and 7 label them with
  // roman numbers, which SBMcq.splitInline does not read), and the answer written the same way ("ii) 3", "Option ii) not zero", "Correct option: iii")
  const ROM = ['i', 'ii', 'iii', 'iv', 'v'];
  const nrm = t => String(t == null ? '' : t).toLowerCase().replace(/\$/g, '').replace(/[^\p{L}\p{N}]+/gu, '');
  const splitRoman = text => {
    const t = String(text == null ? '' : text).replace(/\s+/g, ' ').trim();
    let at = -1, m; const rx = /\(\s*i\s*[.)]\s/g;
    while ((m = rx.exec(t))) at = m.index;
    if (at < 4 || !/\)\s*$/.test(t)) return null;
    const body = t.slice(at + 1).replace(/\)\s*$/, '');
    const marks = []; let from = 0;
    for (const lab of ROM) {
      const re = new RegExp('(?:^|\\s)' + lab + '\\s*[.)]\\s', 'g'); re.lastIndex = from;
      const hit = re.exec(body); if (!hit) break;
      marks.push({ lab, at: hit.index + (hit[0].length - hit[0].replace(/^\s+/, '').length), end: re.lastIndex }); from = re.lastIndex;
    }
    if (marks.length < 3 || marks[0].at !== 0) return null;
    const opts = marks.map((mk, k) => body.slice(mk.end, k + 1 < marks.length ? marks[k + 1].at : body.length).replace(/\s+$/, '').trim());
    const stem = t.slice(0, at).trim();
    return stem.length >= 4 && opts.every(o => o && o.length <= 220) ? { stem, opts } : null;
  };
  const resolveRoman = (raw, opts) => {
    const a = String(raw == null ? '' : raw).replace(/\s+/g, ' ').trim().replace(/^(?:the\s+)?(?:correct\s+)?(?:answer|option)\s*(?:is)?\s*:?\s*/i, '');
    const m = /^\(?\s*(iv|v|i{1,3})\s*(?:[.)]|:|$|\s)\s*(.*)$/i.exec(a);
    if (m) {
      const k = ROM.indexOf(m[1].toLowerCase()), rest = m[2].replace(/^[.:)\s]+/, '').trim();
      if (k < 0 || k >= opts.length) return -1;
      if (!rest || /^is correct/i.test(rest)) return k;
      const r = nrm(rest) || rest.trim(), o = nrm(opts[k]) || String(opts[k]).trim();               // "%" has no letters or digits: it is compared as it is
      return r && o && (r === o || r.includes(o) || o.includes(r)) ? k : -1;           // the label and the words must name the same option
    }
    const n = nrm(a), hits = opts.map((o, k) => [nrm(o), k]).filter(([o]) => o && o === n);
    return n && hits.length === 1 ? hits[0][1] : -1;
  };
  // a figure or a table printed after a question (before the next one) belongs to it: the bank holds text only, so that question cannot be asked
  const figQ = new WeakSet();
  const markFig = list => {
    let last = null;
    (list || []).forEach(x => {
      if (!x || typeof x !== 'object') return;
      if (x.t === 'q') last = x; else if (x.t === 'exercise' || x.t === 'h' || x.t === 'p' || x.t === 'box') last = null;
      else if ((x.t === 'svg' || x.t === 'table') && last) figQ.add(last);
    });
  };
  const T = x => R.cellText(x);
  const trio = x => x && typeof x === 'object' ? [T(x.en), T(x.ur), T(x.ps)] : [T(x), '', ''];
  const stepsOf = r => r && r.steps ? r.steps.map(s => T(s && (s.en || s.ur))).filter(t => t && !/^(agent answer|نمونے کا جواب|p\. ?\d+)\.?$/i.test(t)).join(' ') : '';
  // Mathematics: a step is its words and the line of working ($m$) that goes with it
  const stepsOfM = r => r && r.steps ? r.steps.map(s => { const w = T(s && (s.en || s.ur)), m = T(s && s.m); return ((/^(agent answer|نمونے کا جواب|p\. ?\d+)\.?$/i.test(w) ? '' : w) + (m ? ' $' + m + '$' : '')).trim(); }).filter(Boolean).join(' ') : '';
  const HEAD = /short|long|mcq|choose|correct|select|tick|fill|blank|true|false|match|answer|questions|detail|brief|constructed|structured|comprehension|vocabulary|مختصر|تفصیل|لنډ|درست|صحیح|خالی|ملائیں|سوال|جواب|ځواب|پوښت|ډک|ولیکئ|ولیکئ|لوی/i;
  const out = [], books = [];
  // one book: n the class, k the subject key, B {book, words, units}, how {sol(id): the solution record of a question, keyOf(exercise): the key of its printed answers,
  // strict: Mathematics (an MCQ whose solution names no option takes the printed key, and the two must agree)}
  const addBook = (n, k, B, how) => {
      const sol = how.sol;
      const bk = { id: 'cls' + n + ':' + k, cls: n, key: k, title: (B.book && B.book.title) || '', langs: (B.book && B.book.langs) || ['en', 'ur', 'ps'],
        units: B.units.map(u => ({ n: u.number, title: T(u.title), secs: (u.sections || []).map(s => {
          // the words of a lesson section (not its exercises), enough to tell which topic a question belongs to
          let ex = false, text = '';
          const grab = list => (list || []).forEach(b => {
            if (!b || typeof b !== 'object' || text.length > 7000) return;
            if (b.t === 'exercise') { ex = true; return; }
            if (b.t === 'p' || b.t === 'h' || b.t === 'm') text += ' ' + T(b.en);
            if (b.t === 'ul') (b.items || []).forEach(i => { text += ' ' + T(i); });
            if (b.t === 'box' || b.t === 'example') { text += ' ' + T(b.title); grab(b.blocks); }
          });
          grab(s.blocks);
          // Mathematics sections hold a lesson and the exercise that follows it: a section is an exercise only when it has no lesson text
          const rec = { id: String(s.id || ''), t: T(s.title), ex: how.strict ? ex && text.replace(/\s+/g, ' ').trim().length < 80 : ex, text: text.replace(/\s+/g, ' ').slice(0, 7000) };
          // language books also hand over the lesson as a flat list of events, for tools/grammar/build_grammar.js
          if (/^(eng|urdu|pashto|arabic)$/.test(k)) {
            const flat = [], cut = t => t.length > 1200 ? t.slice(0, 1200) : t;
            const tr = x => trio(x).map(cut);
            const walkF = (list, bt) => (list || []).forEach(b => {
              if (!b || typeof b !== 'object' || flat.length > 90) return;
              if (b.t === 'h') flat.push({ k: 'h', l: b.l, t: tr(b) });
              else if (b.t === 'p') flat.push({ k: 'p', b: bt || '', t: tr(b) });
              else if (b.t === 'ul') flat.push({ k: 'ul', b: bt || '', t: (b.items || []).slice(0, 14).map(i => cut(trio(i)[0])) });
              else if (b.t === 'box') { flat.push({ k: 'box', kind: b.kind || '', t: tr(b.title || '') }); walkF(b.blocks, T(b.title) || b.kind || ''); }
              else if (b.t === 'example') { flat.push({ k: 'eg', t: tr(b.title || '') }); walkF(b.blocks, T(b.title) || 'example'); }
              else if (b.t === 'exercise') flat.push({ k: 'ex', id: String(b.id) });
              else if (b.t === 'table' && b.rows) flat.push({ k: 'tbl', rows: b.rows.slice(0, 14).map(r => r.map(c => cut(T(c).split('||')[0].trim()))) });
              else if (b.t === 'm') flat.push({ k: 'p', b: bt || '', t: [cut(T(b.en)), '', ''] });
            });
            walkF(s.blocks, '');
            rec.flat = flat;
          }
          return rec;
        }) })),
        words: B.words ? Object.entries(B.words).map(([w, m]) => [w].concat(Array.isArray(m) ? m : [String(m)])) : [] };
      books.push(bk);
      R.withBook(B.words, B.book, () => {
        B.units.forEach((u, ui) => (u.sections || []).forEach((s, si) => {
          let pg = null, lastQ = null, lastBare = null, head = '', exKey = null;
          const base = { b: bk.id, u: ui, p: si };
          const emit = (rec) => { try { out.push(Object.assign({}, base, rec, { pg })); } catch (e) { /* skip */ } };
          // the options a roman-numbered part carries as the a) b) c) d) parts after it
          const leafOf = (node, owner, exId, pn, opts, instr) => {
            const t3 = trio(node);
            const text = t3[0];
            let o = null, stem = text, optText = null;
            const sp = M && M.splitInline ? M.splitInline(text) : null;
            if (opts && Object.keys(opts).length >= 3) { o = ['a', 'b', 'c', 'd', 'e'].filter(x => opts[x] !== undefined).map(x => T(opts[x])); optText = opts; }
            else if (sp) { o = sp.opts; stem = sp.stem; optText = {}; sp.opts.forEach((x, i) => { optText['abcde'[i]] = x; }); }
            let rom = null;
            if (!o && how.strict && (rom = splitRoman(text))) { o = rom.opts; stem = rom.stem; }
            const pick = raw => { try { return rom ? resolveRoman(raw, o) : M.resolve(raw, o, pn); } catch (e) { return -1; } };
            let own = sol(node.solId);
            let rec = null;
            const keyRec = () => { try { return R.leafAnswer(exKey != null ? exKey : exId, node, owner, pn, optText); } catch (e) { return null; } };
            if (!own) rec = keyRec();
            let ansRaw = own ? own.answer : rec ? rec.answer : '';
            let cor = -1, clash = 0;
            const isWl = r => !!(r && r.steps && r.steps.some(x => /one line for the whole question/.test((x && x.en) || '')));
            if (o && ansRaw && M && !(how.strict && isWl(rec))) cor = how.strict ? pick(ansRaw) : (() => { try { return M.resolve(ansRaw, o, pn); } catch (e) { return -1; } })();
            if (how.strict && o && own) {
              // the reader takes the printed key when the solution names no option; where both name one, they must be the same one
              const k2 = keyRec(), kc = k2 && k2.answer && M && !isWl(k2) ? pick(k2.answer) : -1;
              if (cor < 0 && kc >= 0) { own = null; rec = k2; ansRaw = k2.answer; cor = kc; }
              else if (cor >= 0 && kc >= 0 && kc !== cor) clash = 1;
            }
            const wl = isWl(rec);
            const steps = how.strict ? stepsOfM : stepsOf;
            emit({ ex: exId == null ? '' : String(exId), clash, fig: how.strict && (figQ.has(owner) || figQ.has(node)) ? 1 : 0, no: String(node.no == null ? '' : node.no), pn: pn || '', head, instr: instr || '', q: t3, stem: o ? stem : '', o, cor,
              a: T(ansRaw), st: own ? steps(own) : rec ? steps(rec) : '', wl: wl ? 1 : 0, sid: node.solId || '', src: own ? 'sol' : rec ? (rec.src === 'book' ? 'key' : 'extra') : '' });
          };
          // Mathematics (Class 8): a multiple-choice question is a question whose parts i) ii) iii) iv) are the options. Every option carries a solution of its own
          // that names the right one ("Option ii) is correct", "Correct option: iii"); the key line of the heading question ("a) iv; b) iii; ...") says the same.
          // Where the two disagree, or the key names two options, there is no single right answer: the question is left out.
          const OPTSOL = /^\s*(?:correct option\s*:\s*\(?([ivx]+|[a-e])\)?\s*\.?|option\s+\(?([ivx]+|[a-e])\)?\s+is\s+correct\b.*)$/i;
          const optionGroup = (ps, labs, owner, exId, instr) => {
            if (!how.strict || ps.length < 3 || ps.length > 5 || ps.some(p => T(p.en).length > 90)) return false;
            const roman = labs.every((l, i) => l === ROM[i]), letters = labs.every((l, i) => l === 'abcde'[i]);
            if (!roman && !letters) return false;
            const named = ps.map(p => { const r = sol(p.solId), m = r ? OPTSOL.exec(T(r.answer)) : null; return m ? (m[1] || m[2]).toLowerCase() : null; });
            // the key line of the heading question ("a) iv; b) iii, iv; ...") has a label for this question, or one of the options says it is the right one
            const line = lastBare ? (sol(lastBare.solId) || {}).answer || ((R.answerOf && R.answerOf(exKey != null ? exKey : exId, lastBare, null)) || {}).answer || '' : '';
            const mine = line ? R.keyParts(T(line)).find(x => x.k === R.partKey(owner.no)) : null;
            if (!named.some(Boolean) && !mine) return false;
            const right = new Set(named.filter(Boolean));
            let cor = -1, clash = 0;
            if (right.size === 1) cor = labs.indexOf([...right][0]); else if (right.size > 1) clash = 1;
            if (mine) {
              const labels = (mine.t.match(/\b(?:iv|v|i{1,3}|[a-e])\b/gi) || []).map(x => x.toLowerCase());
              if (labels.length > 1) cor = -1;                                          // "iii, iv": more than one right option
              else if (labels.length === 1 && cor < 0) cor = labs.indexOf(labels[0]);
              else if (labels.length === 1 && cor !== labs.indexOf(labels[0])) clash = 1;
            }
            emit({ ex: exId == null ? '' : String(exId), clash, fig: figQ.has(owner) ? 1 : 0, grp: 1, no: String(owner.no == null ? '' : owner.no), pn: '', head, instr: '', q: trio(owner), stem: T(owner.en), o: ps.map(p => T(p.en)), cor,
              a: cor >= 0 ? T(ps[cor].en) : '', st: '', wl: 0, sid: '', src: 'sol' });
            return true;
          };
          const emitParts = (ps, owner, exId, instr) => {
            const labs = R.partLabels(ps);
            if (optionGroup(ps, labs, owner, exId, instr)) return;
            const isOpt = ps.map((p, i) => /^[a-e]$/.test(labs[i]) && labs.slice(0, i).some(x => R.isRoman(x)));
            ps.forEach((p, i) => {
              if (isOpt[i]) return;
              const opts = {};
              const circ = String(p.en || '').split('○');
              if (circ.length === 4 || circ.length === 5) circ.slice(1).forEach((t, kk) => { opts['abcd'[kk]] = t.trim(); });
              for (let j = i + 1; j < ps.length && isOpt[j]; j++) opts[labs[j]] = ps[j].en;
              leafOf(p, owner, exId, labs[i], Object.keys(opts).length >= 3 ? opts : null, instr);
            });
          };
          const walk = (b, exId) => {
            if (!b || typeof b !== 'object') return;
            if (b.t === 'page' && b.printed != null) pg = b.printed;
            const isEx = b.t === 'exercise';
            if (isEx) { exId = String(b.id); exKey = how.keyOf(b); head = ''; lastBare = null; }
            if (how.strict && b.blocks) markFig(b.blocks);
            if (b.t === 'q') {
              lastQ = b;
              const ps = b.parts || [];
              const txt = T(b.en);
              if (!ps.length) lastBare = b;
              if (ps.length) emitParts(ps, b, exId, txt);
              else if (!b.solId && txt.length < 220 && HEAD.test(txt) && !(R.answerOf && R.answerOf(exKey != null ? exKey : exId, b, null) && R.answerOf(exKey != null ? exKey : exId, b, null).kind !== 'none')) head = txt;
              else leafOf(b, b, exId, null, null, '');
            } else if (b.t === 'parts' && lastQ) emitParts(b.parts || [], lastQ, exId, T(lastQ.en));
            (b.blocks || []).forEach(x => walk(x, exId));
            // a question after the exercise (not inside it) is not answered by the exercise's key; the next heading does not belong to it either
            if (isEx) { exKey = null; if (how.strict) { head = ''; lastBare = null; } }
          };
          if (how.strict) markFig(s.blocks);
          (s.blocks || []).forEach(b => walk(b, null));
        }));
      });
  };
  for (let n = 1; n <= 12; n++) {
    const L = window['CLS' + n + '_BOOKS']; if (!L) continue;
    Object.keys(L).forEach(k => { const B = L[k]; if (B && B.units) addBook(n, k, B, { sol, keyOf: b => String(b.id) }); });
  }
  // the Mathematics books of Classes 5, 6, 7, 8 and 11: a chapter is a unit, the word list (meanings of words) is not part of the bank
  const MATHS = {
    5: typeof MATH_5_DATA !== 'undefined' ? [MATH_5_DATA, typeof MATH_5_BOOK !== 'undefined' ? MATH_5_BOOK : null] : null,
    6: typeof MATH_6_DATA !== 'undefined' ? [MATH_6_DATA, typeof MATH_6_BOOK !== 'undefined' ? MATH_6_BOOK : null] : null,
    7: typeof MATH_7_DATA !== 'undefined' ? [MATH_7_DATA, typeof MATH_7_BOOK !== 'undefined' ? MATH_7_BOOK : null] : null,
    8: typeof MATH_8_DATA !== 'undefined' ? [MATH_8_DATA, typeof MATH_8_BOOK !== 'undefined' ? MATH_8_BOOK : null] : null,
    11: typeof MATH_11_DATA !== 'undefined' ? [MATH_11_DATA, typeof MATH_11_BOOK !== 'undefined' ? MATH_11_BOOK : null] : null
  };
  Object.keys(MATHS).forEach(n => {
    if (!MATHS[n] || !MATHS[n][1] || (window['CLS' + n + '_BOOKS'] && window['CLS' + n + '_BOOKS'].math)) return;
    const data = MATHS[n][0], book = MATHS[n][1];
    const B = { book, words: null, units: data.map(ch => ({ number: ch.number, title: ch.title, sections: ch.sections || [] })) };
    // the printed answers of an exercise are filed under its key (ansKey / key), else its name
    addBook(+n, 'math', B, { sol: msol(n), keyOf: b => String(b.ansKey || b.key || b.id), strict: true });
  });
  return { books, leaves: out, stores: stores.map(s => Object.keys(s).length) };
};
