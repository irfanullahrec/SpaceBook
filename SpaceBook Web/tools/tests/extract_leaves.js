'use strict';
/* The part of tools/tests/build_test_bank.js that runs INSIDE the app sandbox (it is written as a function so it can be sent there as text).
 * It walks every CLSn_BOOKS book and returns the books (title, languages, units with their sections) and one record per question or part that a student
 * can be asked: its text in the book's languages, its options (an inline "a. b. c. d." list, circles, or a) b) lines under a roman part), the heading
 * above it ("SHORT QUESTIONS", "Choose the correct option"), its answer as the Ans button would show it (a solution record, the printed key, a written
 * answer) and the printed page. Classifying and filtering is done by the builder, in plain Node. Dev-only. */
module.exports = function extract() {
  const R = window.MATH6_READER, M = window.SBMcq;
  const stores = Object.keys(window).filter(k => /SOLUTIONS/.test(k)).map(k => window[k]).filter(v => v && typeof v === 'object');
  const sol = id => { if (!id) return null; for (const s of stores) { const r = s[id]; if (r && typeof r === 'object' && (r.answer !== undefined || r.steps)) return r; } return null; };
  const T = x => R.cellText(x);
  const trio = x => x && typeof x === 'object' ? [T(x.en), T(x.ur), T(x.ps)] : [T(x), '', ''];
  const stepsOf = r => r && r.steps ? r.steps.map(s => T(s && (s.en || s.ur))).filter(t => t && !/^(agent answer|نمونے کا جواب|p\. ?\d+)\.?$/i.test(t)).join(' ') : '';
  const HEAD = /short|long|mcq|choose|correct|select|tick|fill|blank|true|false|match|answer|questions|detail|brief|constructed|structured|comprehension|vocabulary|مختصر|تفصیل|لنډ|درست|صحیح|خالی|ملائیں|سوال|جواب|ځواب|پوښت|ډک|ولیکئ|ولیکئ|لوی/i;
  const out = [], books = [];
  for (let n = 1; n <= 12; n++) {
    const L = window['CLS' + n + '_BOOKS']; if (!L) continue;
    Object.keys(L).forEach(k => {
      const B = L[k]; if (!B || !B.units) return;
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
          const rec = { id: String(s.id || ''), t: T(s.title), ex, text: text.replace(/\s+/g, ' ').slice(0, 7000) };
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
          let pg = null, lastQ = null, head = '';
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
            const own = sol(node.solId);
            let rec = null;
            if (!own) { try { rec = R.leafAnswer(exId, node, owner, pn, optText); } catch (e) { rec = null; } }
            const ansRaw = own ? own.answer : rec ? rec.answer : '';
            const wl = !!(rec && rec.steps && rec.steps.some(x => /one line for the whole question/.test((x && x.en) || '')));
            let cor = -1;
            if (o && ansRaw && M) { try { cor = M.resolve(ansRaw, o, pn); } catch (e) { cor = -1; } }
            emit({ ex: exId == null ? '' : String(exId), no: String(node.no == null ? '' : node.no), pn: pn || '', head, instr: instr || '', q: t3, stem: o ? stem : '', o, cor,
              a: T(ansRaw), st: own ? stepsOf(own) : rec ? stepsOf(rec) : '', wl: wl ? 1 : 0, sid: node.solId || '', src: own ? 'sol' : rec ? (rec.src === 'book' ? 'key' : 'extra') : '' });
          };
          const emitParts = (ps, owner, exId, instr) => {
            const labs = R.partLabels(ps);
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
            if (b.t === 'exercise') { exId = String(b.id); head = ''; }
            if (b.t === 'q') {
              lastQ = b;
              const ps = b.parts || [];
              const txt = T(b.en);
              if (ps.length) emitParts(ps, b, exId, txt);
              else if (!b.solId && txt.length < 220 && HEAD.test(txt) && !(R.answerOf && R.answerOf(exId, b, null) && R.answerOf(exId, b, null).kind !== 'none')) head = txt;
              else leafOf(b, b, exId, null, null, '');
            } else if (b.t === 'parts' && lastQ) emitParts(b.parts || [], lastQ, exId, T(lastQ.en));
            (b.blocks || []).forEach(x => walk(x, exId));
          };
          (s.blocks || []).forEach(b => walk(b, null));
        }));
      });
    });
  }
  return { books, leaves: out, stores: stores.map(s => Object.keys(s).length) };
};
