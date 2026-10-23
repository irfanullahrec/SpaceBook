'use strict';
/* The part of tools/assistant/build_assistant.js that runs INSIDE the app sandbox (written as a function so it can be sent there as text): every book of
 * Classes 1 to 10 and 12 (CLSn_BOOKS) as passages: the text of each unit in reading order, split at sentence ends into pieces of at most about 420
 * characters, each with the heading (or box title) it sits under. Exercises and their questions are not passages (the question bank has them). Dev-only. */
module.exports = function extractParas() {
  const R = window.MATH6_READER;
  const T = x => R.cellText(x);
  const out = [];
  for (let n = 1; n <= 12; n++) {
    const L = window['CLS' + n + '_BOOKS']; if (!L) continue;
    Object.keys(L).forEach(k => {
      const B = L[k]; if (!B || !B.units) return;
      const bk = { id: 'cls' + n + ':' + k, cls: n, key: k, langs: (B.book && B.book.langs) || ['en', 'ur', 'ps'], units: [] };
      B.units.forEach(u => {
        const paras = [];
        let curH = '';
        const add = (text) => {
          text = String(text || '').replace(/\*\*(.+?)\*\*/g, '$1').replace(/\s+/g, ' ').trim();
          if (text.length < 25) return;
          // pieces at sentence ends, up to ~420 characters
          const pieces = [];
          let cur = '';
          text.split(/(?<=[.!?؟۔…:])\s+/).forEach(s => {
            if ((cur + ' ' + s).length > 420 && cur) { pieces.push(cur); cur = s; } else cur = cur ? cur + ' ' + s : s;
            while (cur.length > 700) { pieces.push(cur.slice(0, 420)); cur = cur.slice(420); }
          });
          if (cur) pieces.push(cur);
          pieces.forEach(p => { if (p.length >= 25) paras.push([curH, p]); });
        };
        const grab = list => (list || []).forEach(b => {
          if (!b || typeof b !== 'object') return;
          if (b.t === 'h') { curH = T(b.en).slice(0, 110); return; }
          if (b.t === 'p' || b.t === 'm') add(T(b.en));
          else if (b.t === 'ul') add((b.items || []).map(i => T(i)).join(' • '));
          else if (b.t === 'table' && b.rows) add(b.rows.map(r => r.map(c => T(c).split('||')[0].trim()).join(' | ')).join('; '));
          else if (b.t === 'box' || b.t === 'example') { const keep = curH; const tt = T(b.title) || T(b.no); if (tt) curH = tt.slice(0, 110); grab(b.blocks); curH = keep; }
          else if (b.t === 'exercise' || b.t === 'q' || b.t === 'parts') return;
        });
        (u.sections || []).forEach(s => { curH = T(s.title).slice(0, 110); grab(s.blocks); });
        bk.units.push(paras);
      });
      out.push(bk);
    });
  }
  return out;
};
