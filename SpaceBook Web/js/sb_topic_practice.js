/* sb_topic_practice.js — under every topic of every Lessons tab: two tabs, "SLOs" and "Exercise".
 * Each has the practice types that fit the topic: MCQs, Short Questions, Long Questions and, where the text allows,
 * True / False, Blanks and Column matching. How many of each depends on how long the topic is.
 *   SLOs     : questions aimed at the chapter's learning outcomes (each tagged with the outcome it serves);
 *   Exercise : the textbook's own exercise questions that belong to the topic first, topped up with exercise-style
 *              questions made from the topic text.
 * Real questions already stored in the chapter data (MCQs, SQs, LQs ...) are used before any are generated.
 * Generated questions are plain cloze / definition / rewording drills made offline from the topic text — they are
 * practice, not a substitute for the textbook's printed answers. Works offline. */
(function () {
  'use strict';
  const norm = s => String(s == null ? '' : s).replace(/\s+/g, ' ').trim();
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const AR = /[ء-يٱ-ۓݐ-ݿﭐ-﷿ﹰ-ﻼ]/g, LA = /[A-Za-z]/g;
  const lang = t => { const a = (t.match(AR) || []).length, l = (t.match(LA) || []).length; if (a > l) return /[ټځڅډړږښګڼۍې]/.test(t) ? 'ps' : 'ur'; return 'en'; };
  const WORD = /[\p{L}\p{M}\p{N}][\p{L}\p{M}\p{N}'’-]*/gu;
  const words = t => (String(t).match(WORD) || []);
  const STOP = new Set(('the a an and or but if then than that this these those of in on at to from by for with as is are was were be been being it its into over under about between during before after also can could may might must shall should will would not no nor so such each any all some more most other another their there they them he she his her we our you your i have has had do does did which who whom whose what when where why how one two three because while through within without upon up down out off very only same both either neither per via using used use called known').split(' '));
  const STOP_UR = new Set('کا کی کے میں سے ہے ہیں اور کو پر کہ یہ وہ کر تھا تھی تھے گیا گئی گئے ہو ہوتا ہوتی ہوتے جو جس جن اس ان ایک بھی نے تک لیے لئے ساتھ بعد پہلے کیا کیں کرتا کرتی کرتے والا والی والے جاتا جاتی جاتے سکتا سکتی سکتے ہوئے ہوئی ہوں یا تو ہی نہ نہیں بہت کسی کوئی ہر دو ذریعے دوران طرح صورت عمل دیگر مختلف مثال اہم بنیادی پایا پائی پائے رہتا رہتی رہتے ہوتا'.split(' '));
  const STOP_PS = new Set('د په له او چې دی دي ده ده؟ یو هم نو خو چي کې ته لکه نه ډېر هر دا هغه دغه یې به ورته ورکړ شي شو وي وو'.split(' '));
  const isStop = (w, l) => (l === 'en' ? STOP.has(w.toLowerCase()) : l === 'ur' ? STOP_UR.has(w) : STOP_PS.has(w) || STOP_UR.has(w));
  const SPLIT = /(?<=[.!?؟۔])\s+(?=\S)/;
  const sentencesOf = t => norm(t).split(SPLIT).map(norm).filter(s => words(s).length >= 5);

  // deterministic shuffle so a topic always shows the same practice
  function seedOf(str) { let h = 2166136261; for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  function rng(seed) { let s = seed || 1; return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return ((s >>> 0) % 100000) / 100000; }; }
  function shuffle(a, r) { const o = a.slice(); for (let i = o.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [o[i], o[j]] = [o[j], o[i]]; } return o; }
  const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));

  const L = {
    en: {slo: '🎯 SLOs', ex: '✍️ Exercise', mcq: 'MCQs', sq: 'Short Questions', lq: 'Long Questions', tf: 'True / False', bl: 'Blanks', co: 'Columns',
      show: 'Show answer', hide: 'Hide answer', t: 'True', f: 'False', right: '✔ Correct', wrong: '✘ Not quite — correct answer: ', blank: 'Fill in the blank:', match: 'Match the terms with their meanings:',
      noEx: 'No exercise question of this chapter belongs to this topic; these are exercise-style questions made from the topic.', slo: 'SLO: ',
      what: t => `What is meant by “${t}”?`, note: t => `Write a short note on “${t}”.`, explain: t => `Explain “${t}” in detail.`, discuss: t => `Discuss the main points about “${t}”.`,
      tfq: 'Say whether the statement is true or false:', mcqq: 'Choose the correct word to complete the sentence:'},
    ur: {slo: '🎯 تعلیمی نتائج (SLOs)', ex: '✍️ مشق', mcq: 'کثیرالانتخابی سوالات', sq: 'مختصر سوالات', lq: 'تفصیلی سوالات', tf: 'درست / غلط', bl: 'خالی جگہیں', co: 'کالم ملائیں',
      show: 'جواب دیکھیں', hide: 'جواب چھپائیں', t: 'درست', f: 'غلط', right: '✔ درست', wrong: '✘ درست جواب: ', blank: 'خالی جگہ پُر کریں:', match: 'اصطلاحات کو ان کے مفہوم سے ملائیں:',
      noEx: 'اس باب کا کوئی مشقی سوال اس عنوان سے متعلق نہیں ملا؛ یہ عنوان کے متن سے بنائے گئے مشق نما سوالات ہیں۔', slo: 'تعلیمی نتیجہ: ',
      what: t => `«${t}» سے کیا مراد ہے؟`, note: t => `«${t}» پر مختصر نوٹ لکھیں۔`, explain: t => `«${t}» کی تفصیل بیان کریں۔`, discuss: t => `«${t}» کے بارے میں اہم نکات بیان کریں۔`,
      tfq: 'بتائیں کہ بیان درست ہے یا غلط:', mcqq: 'جملہ مکمل کرنے کے لیے درست لفظ منتخب کریں:'},
    ps: {slo: '🎯 SLOs', ex: '✍️ تمرین', mcq: 'ګڼ‌ځوابیزې پوښتنې', sq: 'لنډې پوښتنې', lq: 'اوږدې پوښتنې', tf: 'سم / غلط', bl: 'تشې ځایونه', co: 'کالمونه سره وصل کړئ',
      show: 'ځواب وګورئ', hide: 'ځواب پټ کړئ', t: 'سم', f: 'غلط', right: '✔ سم', wrong: '✘ سم ځواب: ', blank: 'تشه ځای ډک کړئ:', match: 'اصطلاحات د هغوی له معنا سره وصل کړئ:',
      noEx: 'د دې څپرکي هېڅ تمرین پوښتنه له دې سرلیک سره نه اړوند؛ دا د سرلیک له متن جوړې شوې تمرین ډوله پوښتنې دي.', slo: 'SLO: ',
      what: t => `«${t}» څه ته وايي؟`, note: t => `د «${t}» په اړه لنډه یادداشت ولیکئ.`, explain: t => `«${t}» په تفصیل سره بیان کړئ.`, discuss: t => `د «${t}» په اړه مهم ټکي بیان کړئ.`,
      tfq: 'ووایئ چې بیان سم دی که غلط:', mcqq: 'د جملې بشپړولو لپاره سم کلمه وټاکئ:'}
  };

  // ---------- key terms ----------
  function termsOf(text, l) {
    const freq = new Map();
    words(text).forEach((w, i) => {
      const k = l === 'en' ? w.toLowerCase() : w;
      if (isStop(w, l) || /^\d/.test(w)) return;
      if (w.length < (l === 'en' ? 5 : 4)) return;
      freq.set(k, (freq.get(k) || 0) + 1);
    });
    return [...freq.entries()].sort((a, b) => b[1] - a[1] || b[0].length - a[0].length).map(e => e[0]);
  }
  function sameShape(w, pool, r, n, avoid) {
    const c = pool.filter(p => p !== w && !avoid.has(p) && Math.abs(p.length - w.length) <= Math.max(3, w.length * 0.5));
    return shuffle(c.length >= n ? c : pool.filter(p => p !== w && !avoid.has(p)), r).slice(0, n);
  }
  const replaceWord = (s, w, repl, l) => { const idx = (l === 'en' ? s.toLowerCase() : s).indexOf(l === 'en' ? w.toLowerCase() : w); if (idx < 0) return null; return s.slice(0, idx) + repl + s.slice(idx + w.length); };

  // ---------- generators ----------
  function defsOf(sents, l) {
    const out = [];
    sents.forEach(s => {
      let m;
      if (l === 'en') m = s.match(/^([A-Z][^,.;:]{2,45}?)\s+(?:is|are|means|refers to|is called|is known as|can be defined as)\s+(?!(?:\w+ed|\w+ing|being|also|not|then|used|found)\b)(.{20,})$/);
      else m = s.match(/^(.{3,40}?)\s+(?:کو|سے|کا|کی)\s+(.{12,}?)\s+(?:کہتے ہیں|کہلاتا ہے|کہلاتی ہے|کہا جاتا ہے)[۔.]?$/) || s.match(/^(.{3,40}?)\s+(?:وایي|بلل کېږي|نومېږي)\s*(.*)$/);
      if (m) out.push({term: norm(m[1]), def: l === 'en' ? s : s});
    });
    return out;
  }
  function build(topic, plan) {
    // topic: {title, text, pool (chapter terms), slos: [strings]}
    const text = norm(topic.text), l = lang(text), T = L[l] || L.en;
    const sents = sentencesOf(text);
    const S = Math.max(sents.length, 1);
    const r = rng(seedOf(topic.title + '|' + plan));
    const terms = termsOf(text, l);
    const pool = [...new Set([...terms, ...(topic.pool || [])])];
    const n = {mcq: clamp(Math.round(S / 3), 2, 12), tf: clamp(Math.round(S / 4), 2, 10), bl: clamp(Math.round(S / 3), 2, 10), sq: clamp(Math.round(S / 4), 1, 8), lq: clamp(Math.round(S / 9), 1, 4)};
    // sentences for this plan: SLO plan ranks by outcome overlap, exercise plan takes the others
    let ranked = sents.map((s, i) => ({s, i, sc: 0}));
    if (plan === 'slo' && topic.slos && topic.slos.length) {
      const sw = new Set(topic.slos.flatMap(x => words(x).filter(w => !isStop(w, lang(x))).map(w => w.toLowerCase())));
      ranked.forEach(o => { o.sc = words(o.s).filter(w => sw.has(w.toLowerCase())).length; });
      ranked.sort((a, b) => b.sc - a.sc || a.i - b.i);
    } else if (plan === 'ex') ranked = ranked.filter(o => o.i % 2 === 1).concat(ranked.filter(o => o.i % 2 === 0));
    const slosFor = s => { if (plan !== 'slo' || !topic.slos) return ''; const sw = new Set(words(s).map(w => w.toLowerCase())); let best = '', bs = 0; topic.slos.forEach(x => { const sc = words(x).filter(w => sw.has(w.toLowerCase())).length; if (sc > bs) { bs = sc; best = x; } }); return bs ? best : ''; };
    const usedTerms = new Set(), out = {mcq: [], tf: [], bl: [], sq: [], lq: [], co: []};
    const pick = s => terms.find(t => !usedTerms.has(t) && (l === 'en' ? s.toLowerCase() : s).includes(l === 'en' ? t : t));
    // blanks + MCQs (cloze)
    for (const o of ranked) {
      if (out.bl.length >= n.bl && out.mcq.length >= n.mcq) break;
      const t = pick(o.s); if (!t) continue;
      const stem = replaceWord(o.s, t, '_______', l); if (!stem) continue;
      usedTerms.add(t);
      const ans = (l === 'en' ? t : t);
      if (out.mcq.length < n.mcq) {
        const d = sameShape(t, pool, r, 3, new Set([t]));
        if (d.length >= 3) { const opts = shuffle([ans, ...d], r); out.mcq.push({q: T.mcqq + ' ' + stem, opts, a: opts.indexOf(ans), slo: slosFor(o.s)}); continue; }
      }
      if (out.bl.length < n.bl) out.bl.push({q: stem, a: ans, slo: slosFor(o.s)});
    }
    // true / false
    let k = 0;
    for (const o of ranked) {
      if (out.tf.length >= n.tf) break;
      const t = terms.find(x => (l === 'en' ? o.s.toLowerCase() : o.s).includes(x));
      const makeFalse = (k++ % 2 === 1) && t;
      if (makeFalse) {
        const d = sameShape(t, pool, r, 1, new Set([t]))[0]; const f = d && replaceWord(o.s, t, d, l);
        if (f) { out.tf.push({q: f, a: false, fix: o.s, slo: slosFor(o.s)}); continue; }
      }
      out.tf.push({q: o.s, a: true, slo: slosFor(o.s)});
    }
    // short questions: definitions first, then notes on key terms
    const defs = defsOf(sents, l);
    defs.slice(0, n.sq).forEach(d => out.sq.push({q: T.what(d.term), a: d.def, slo: slosFor(d.def)}));
    for (const t of terms) {
      if (out.sq.length >= n.sq) break;
      if (out.sq.some(x => x.q.includes(t))) continue;
      const hit = sents.filter(s => (l === 'en' ? s.toLowerCase() : s).includes(t)).slice(0, 2);
      if (hit.length) out.sq.push({q: T.note(t), a: hit.join(' '), slo: slosFor(hit[0])});
    }
    // long questions: the whole topic, then groups of sentences around its main terms
    out.lq.push({q: T.explain(topic.title), a: sents.slice(0, Math.min(sents.length, 8)).join(' '), slo: topic.slos && topic.slos[0] || ''});
    for (let i = 0; i < terms.length && out.lq.length < n.lq; i++) {
      const hit = sents.filter(s => (l === 'en' ? s.toLowerCase() : s).includes(terms[i])).slice(0, 5);
      if (hit.length >= 3) out.lq.push({q: T.discuss(terms[i]), a: hit.join(' '), slo: slosFor(hit[0])});
    }
    // columns need at least three definitions
    if (defs.length >= 3) {
      const pairs = defs.slice(0, 8).map(d => ({t: d.term, m: norm(d.def.replace(d.term, '').replace(/^\s*(?:is|are|means|refers to|is called|is known as|can be defined as|کو|سے|کا|کی|وایي)\s+/i, '')).slice(0, 110)}));
      out.co.push({pairs, order: shuffle(pairs.map((p, i) => i), r)});
    }
    return {out, l, T};
  }

  // ---------- real questions found in the chapter data ----------
  const QKEYS = ['q', 'question', 'questionText', 'stem', 'text', 'prompt', 'en'];
  const qText = o => { for (const k of QKEYS) if (typeof o[k] === 'string' && o[k].length > 8) return o[k]; return ''; };
  function collect(ch) {
    const items = [], seen = new Set();
    (function walk(o, path, depth) {
      if (!o || typeof o !== 'object' || depth > 7 || seen.has(o)) return; seen.add(o);
      if (Array.isArray(o)) { o.forEach(x => walk(x, path, depth + 1)); return; }
      const q = qText(o);
      const opts = o.options || o.choices || o.opts;
      if (q && (Array.isArray(opts) && opts.length >= 3 || /question|mcq|sq|lq|exercise|slo|problem|blank|true/i.test(path))) {
        const kind = Array.isArray(opts) ? 'mcq' : /true|false|tf/i.test(path) ? 'tf' : /blank|fill/i.test(path) ? 'bl' : /long|lq/i.test(path) ? 'lq' : 'sq';
        const ans = o.answer != null ? o.answer : (o.correct != null ? o.correct : (o.ans != null ? o.ans : o.solution));
        items.push({kind, q: norm(q), opts: Array.isArray(opts) ? opts.map(x => norm(typeof x === 'string' ? x : (x.text || x.en || ''))) : null, ans, ex: /exercise/i.test(path), path});
        return;
      }
      Object.keys(o).forEach(k => { if (typeof o[k] === 'object') walk(o[k], path + '.' + k, depth + 1); });
    })(ch, '', 0);
    return items;
  }
  function chapterOf() {
    try {
      const s = window.state; if (!s) return null;
      const cls = s.selectedClass, subj = s.activeSubject;
      if (typeof window.getSubjectChapterList === 'function' && subj && subj !== 'math') { const l = window.getSubjectChapterList(subj, cls); if (l && l[s.selectedSubjChapter || 0]) return l[s.selectedSubjChapter || 0]; }
      if (typeof window.getMathChapterList === 'function') { const l = window.getMathChapterList(); if (l && l[s.selectedMathChapter || 0]) return l[s.selectedMathChapter || 0]; }
    } catch (e) { /* no data: generated practice only */ }
    return null;
  }
  const slosOf = ch => (ch && Array.isArray(ch.slos) ? ch.slos : []).map(x => norm(typeof x === 'string' ? x : (x.text || x.en || x.slo || ''))).filter(Boolean);
  function overlap(a, b) { const wa = new Set(words(a).filter(w => w.length > 3).map(w => w.toLowerCase())); let c = 0; new Set(words(b).filter(w => w.length > 3).map(w => w.toLowerCase())).forEach(w => { if (wa.has(w)) c++; }); return c; }

  // ---------- UI ----------
  function mcqHtml(item, id) {
    return `<div class="sb-tp-q"><div class="sb-tp-qt">${esc(item.q)}${item.slo ? `<div class="sb-tp-slo">${esc(item.slo)}</div>` : ''}</div>` +
      `<div class="sb-tp-opts">${item.opts.map((o, i) => `<button type="button" class="sb-tp-opt" data-i="${i}">${esc(o)}</button>`).join('')}</div><div class="sb-tp-fb"></div></div>`;
  }
  function renderPanel(data, kind, T, noEx) {
    const out = data.out[kind];
    if (!out || !out.length) return '';
    if (kind === 'mcq') return out.map((q, i) => `<div data-a="${q.a}">${mcqHtml(q)}</div>`).join('');
    if (kind === 'tf') return out.map(q => `<div class="sb-tp-q" data-a="${q.a ? 1 : 0}"><div class="sb-tp-qt">${esc(T.tfq)} ${esc(q.q)}${q.slo ? `<div class="sb-tp-slo">${esc(q.slo)}</div>` : ''}</div><div class="sb-tp-opts"><button type="button" class="sb-tp-tf" data-v="1">${T.t}</button><button type="button" class="sb-tp-tf" data-v="0">${T.f}</button></div><div class="sb-tp-fb"></div>${q.fix ? `<div class="sb-tp-ans" hidden>${esc(q.fix)}</div>` : ''}</div>`).join('');
    if (kind === 'co') return out.map(c => `<div class="sb-tp-q"><div class="sb-tp-qt">${esc(T.match)}</div><div class="sb-tp-co"><ol>${c.pairs.map(p => `<li>${esc(p.t)}</li>`).join('')}</ol><ol type="a">${c.order.map(i => `<li>${esc(c.pairs[i].m)}</li>`).join('')}</ol></div><button type="button" class="sb-tp-show">${T.show}</button><div class="sb-tp-ans" hidden>${c.pairs.map((p, i) => `${i + 1} → ${String.fromCharCode(97 + c.order.indexOf(i))}`).join(' · ')}</div></div>`).join('');
    return out.map(q => `<div class="sb-tp-q"><div class="sb-tp-qt">${kind === 'bl' ? esc(T.blank) + ' ' : ''}${esc(q.q)}${q.slo ? `<div class="sb-tp-slo">${esc(q.slo)}</div>` : ''}</div><button type="button" class="sb-tp-show">${T.show}</button><div class="sb-tp-ans" hidden>${esc(q.a)}</div></div>`).join('');
  }
  const KINDS = ['mcq', 'sq', 'lq', 'tf', 'bl', 'co'];

  function mount(card, topic, real) {
    const text = topic.text, l = lang(text), T = L[l] || L.en;
    const dataS = build(topic, 'slo'), dataE = build(topic, 'ex');
    // real chapter questions go first
    const merge = (data, items, tag) => {
      items.forEach(it => {
        if (it.kind === 'mcq' && it.opts) {
          let a = typeof it.ans === 'number' ? it.ans : it.opts.findIndex(o => norm(o) === norm(String(it.ans || '')) || norm(String(it.ans || '')).charAt(0).toLowerCase() === 'abcd'.charAt(it.opts.indexOf(o)));
          if (a < 0) a = typeof it.ans === 'string' && /^[a-d]$/i.test(it.ans.trim()) ? 'abcd'.indexOf(it.ans.trim().toLowerCase()) : 0;
          data.out.mcq.unshift({q: it.q, opts: it.opts, a, slo: ''});
        } else if (it.kind === 'tf') data.out.tf.unshift({q: it.q, a: /true|درست|سم/i.test(String(it.ans)), slo: ''});
        else if (it.kind === 'bl') data.out.bl.unshift({q: it.q, a: norm(String(it.ans || '')), slo: ''});
        else (data.out[it.kind === 'lq' ? 'lq' : 'sq']).unshift({q: it.q, a: norm(typeof it.ans === 'string' ? it.ans : (it.ans && (it.ans.en || it.ans.text)) || ''), slo: ''});
      });
    };
    merge(dataS, real.slo, 'slo'); merge(dataE, real.ex, 'ex');
    const tabs = [['slo', T.slo, dataS], ['ex', T.ex, dataE]];
    const host = document.createElement('div');
    host.className = 'sb-tp'; host.setAttribute('dir', l === 'en' ? 'ltr' : 'rtl');
    host.innerHTML = `<div class="sb-tp-top">${tabs.map(t => `<button type="button" class="sb-tp-tab" data-t="${t[0]}">${t[1]}</button>`).join('')}</div><div class="sb-tp-body" hidden></div>`;
    const body = host.querySelector('.sb-tp-body');
    function show(key) {
      const data = key === 'slo' ? dataS : dataE;
      const kinds = KINDS.filter(k => data.out[k] && data.out[k].length);
      const label = {mcq: T.mcq, sq: T.sq, lq: T.lq, tf: T.tf, bl: T.bl, co: T.co};
      body.hidden = false; body.dataset.key = key;
      body.innerHTML = (key === 'ex' && !real.ex.length ? `<div class="sb-tp-note">${esc(T.noEx)}</div>` : '') +
        `<div class="sb-tp-sub">${kinds.map((k, i) => `<button type="button" class="sb-tp-subtab${i ? '' : ' on'}" data-k="${k}">${label[k]} (${data.out[k].length})</button>`).join('')}</div><div class="sb-tp-list"></div>`;
      const list = body.querySelector('.sb-tp-list');
      const open = k => { list.innerHTML = renderPanel(data, k, T); body.querySelectorAll('.sb-tp-subtab').forEach(b => b.classList.toggle('on', b.dataset.k === k)); };
      if (kinds.length) open(kinds[0]); else list.textContent = '—';
      body.querySelectorAll('.sb-tp-subtab').forEach(b => b.addEventListener('click', e => { e.stopPropagation(); open(b.dataset.k); }));
      host.querySelectorAll('.sb-tp-tab').forEach(b => b.classList.toggle('on', b.dataset.t === key));
    }
    host.addEventListener('click', e => {
      e.stopPropagation();
      const tab = e.target.closest('.sb-tp-tab');
      if (tab) { if (tab.classList.contains('on')) { body.hidden = true; tab.classList.remove('on'); } else show(tab.dataset.t); return; }
      const opt = e.target.closest('.sb-tp-opt');
      if (opt) { const q = opt.closest('[data-a]'); const a = +q.dataset.a; const i = +opt.dataset.i; const fb = q.querySelector('.sb-tp-fb');
        q.querySelectorAll('.sb-tp-opt').forEach((b, j) => { b.disabled = true; b.classList.toggle('ok', j === a); b.classList.toggle('bad', j === i && i !== a); });
        fb.textContent = i === a ? T.right : T.wrong + q.querySelectorAll('.sb-tp-opt')[a].textContent; return; }
      const tf = e.target.closest('.sb-tp-tf');
      if (tf) { const q = tf.closest('[data-a]'); const ok = tf.dataset.v === q.dataset.a; q.querySelectorAll('.sb-tp-tf').forEach(b => { b.disabled = true; b.classList.toggle('ok', b.dataset.v === q.dataset.a); b.classList.toggle('bad', b === tf && !ok); });
        const fb = q.querySelector('.sb-tp-fb'); fb.textContent = ok ? T.right : T.wrong + (q.dataset.a === '1' ? T.t : T.f); const fix = q.querySelector('.sb-tp-ans'); if (fix && !ok || fix && q.dataset.a === '0') fix.hidden = false; return; }
      const sh = e.target.closest('.sb-tp-show');
      if (sh) { const a = sh.parentElement.querySelector('.sb-tp-ans'); a.hidden = !a.hidden; sh.textContent = a.hidden ? T.show : T.hide; }
    });
    return host;
  }

  // ---------- finding topics ----------
  const CARD = '.math-topic-card, .para-card';
  const NOT = '.topic-ex-item, .slo-accordion-card, .slo-question-accordion, .sb-tp, [id^="m11-bank"], .m11-q, .sb-tp-q';
  function topicText(card) {
    const c = card.cloneNode(true);
    c.querySelectorAll('.math-acc-header, .para-card-header, .sb-topic-tools, .sb-tri-drawer, .sb-tp, button, script, style, .katex, svg, details, [id^="sent-trans-"], .para-qa-box, .m11-box-t').forEach(x => x.remove());
    return norm(c.textContent);
  }
  function titleOf(card) {
    const h = card.querySelector('.math-acc-header h3, .para-card-header span:last-child, h3, h4, .m11-h3'); return norm(h ? h.textContent : '') || 'this topic';
  }
  let timer = 0;
  function scan() {
    const cards = [...document.querySelectorAll(CARD)].filter(c => !c.dataset.sbTp && !c.closest('.sb-tp') && !c.matches(NOT) && !c.querySelector(':scope .math-topic-card') && !c.closest('.topic-ex-item, .slo-accordion-card, .slo-question-accordion'));
    if (!cards.length) return;
    const groups = new Map();
    cards.forEach(c => { const g = c.parentElement; if (!groups.has(g)) groups.set(g, []); groups.get(g).push(c); });
    const ch = chapterOf();
    const slos = slosOf(ch);
    const items = ch ? collect(ch) : [];
    groups.forEach(list => {
      const infos = list.map(c => ({card: c, title: titleOf(c), text: topicText(c)})).filter(i => words(i.text).length >= 25);
      if (!infos.length) return;
      const pool = [...new Set(infos.flatMap(i => termsOf(i.text, lang(i.text)).slice(0, 25)))];
      const best = (str) => { let bi = -1, bs = 1; infos.forEach((inf, k) => { const sc = overlap(str, inf.title + ' ' + inf.text); if (sc > bs) { bs = sc; bi = k; } }); return bi; };
      const real = infos.map(() => ({slo: [], ex: []})), sloMap = infos.map(() => []);
      slos.forEach(s => { const b = best(s); if (b >= 0) sloMap[b].push(s); });
      items.forEach(it => { const b = best(it.q); if (b >= 0) (it.ex ? real[b].ex : real[b].slo).push(it); });
      infos.forEach((inf, k) => {
        inf.card.dataset.sbTp = '1';
        const body = inf.card.querySelector(':scope > .math-accordion-body') || inf.card;
        real[k].slo = real[k].slo.slice(0, 12); real[k].ex = real[k].ex.slice(0, 12);
        body.appendChild(mount(inf.card, {title: inf.title, text: inf.text, pool, slos: sloMap[k]}, real[k]));
      });
    });
  }
  const later = () => { if (!timer) timer = setTimeout(() => { timer = 0; try { scan(); } catch (e) { /* never break the page */ } }, 400); };
  function start() {
    const s = document.createElement('style'); s.id = 'sb-tp-css';
    s.textContent = `
    .sb-tp{margin:1rem 0 .3rem;padding-top:.7rem;border-top:1px dashed #cbd5e1;font-size:.95rem;text-align:start}
    .sb-tp-top,.sb-tp-sub{display:flex;gap:.45rem;flex-wrap:wrap;margin-bottom:.6rem}
    .sb-tp-tab,.sb-tp-subtab{border:1px solid #cbd5e1;background:#fff;color:#0f172a;border-radius:999px;padding:.3rem .85rem;font:600 .82rem system-ui,sans-serif;cursor:pointer}
    .sb-tp-tab.on{background:#0369a1;border-color:#0369a1;color:#fff}.sb-tp-subtab.on{background:#dcfce7;border-color:#16a34a;color:#166534}
    .sb-tp-q{background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:.7rem .9rem;margin:.5rem 0}
    .sb-tp-qt{font-weight:600;line-height:1.7}.sb-tp-slo{font-weight:500;font-size:.78rem;color:#92400e;background:#fef3c7;border-radius:6px;display:inline-block;padding:.05rem .45rem;margin-top:.3rem}
    .sb-tp-opts{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.5rem}
    .sb-tp-opt,.sb-tp-tf,.sb-tp-show{border:1px solid #cbd5e1;background:#fff;border-radius:8px;padding:.3rem .7rem;cursor:pointer;font:500 .88rem system-ui,sans-serif}
    .sb-tp-opt.ok,.sb-tp-tf.ok{background:#dcfce7;border-color:#16a34a}.sb-tp-opt.bad,.sb-tp-tf.bad{background:#fee2e2;border-color:#dc2626}
    .sb-tp-fb{margin-top:.4rem;font-weight:600;font-size:.85rem}.sb-tp-ans{margin-top:.5rem;background:#f0fdf4;border-inline-start:3px solid #16a34a;padding:.45rem .7rem;border-radius:6px;line-height:1.75}
    .sb-tp-note{background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:.5rem .7rem;margin-bottom:.5rem;font-size:.85rem;color:#92400e}
    .sb-tp-co{display:flex;gap:2rem;flex-wrap:wrap;margin:.4rem 0}.sb-tp-co ol{margin:0;padding-inline-start:1.6rem}
    .sb-tp-show{margin-top:.5rem}
    `;
    document.head.appendChild(s);
    new MutationObserver(later).observe(document.body, {childList: true, subtree: true});
    later();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
  window.SBTopicPractice = {build, lang, sentencesOf, termsOf, collect, scan};
})();
