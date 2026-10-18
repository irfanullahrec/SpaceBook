/* ======================================================================
 *  structure_harmonizer.js — same language controls in every book
 *
 *  Standard books (Classes 1–10 book readers) show ONE language bar per
 *  lesson:  📖 Original (X) · X + L1 · X + L2  (window.SBLangMode 0/1/2),
 *  where the + modes show each original paragraph with its translation
 *  underneath. The older Class 9/10/12 science readers instead put an
 *  "English / اردو / پښتو / All" switch on every paragraph.
 *
 *  This file converts those older readers on the fly: the per-paragraph
 *  switches are hidden and the standard bar is added once at the top of
 *  the lesson, driven by the same global mode, so a student's choice
 *  carries across every book. The verified textbook content is untouched.
 * ====================================================================== */
(function () {
  'use strict';

  const HELP = 'Original: the textbook text only. The other tabs show each original line with its translation below it. Tap a dotted word for its meaning.';
  const mode = () => Number(window.SB_LANG_MODE || 0);
  const clean = s => String(s || '').replace(/[\u{1F1E6}-\u{1F1FF}\u{1F4D1}]/gu, '').replace(/\s*\(.*?\)\s*/g, ' ').trim();
  const latin = s => (String(s).match(/[A-Za-z]/g) || []).length > (String(s).match(/[؀-ۿ]/g) || []).length;

  // which paragraphs (idx) live inside a container
  function paraIdxs(scope) {
    return [...scope.querySelectorAll('.para-lang-tabs-bar[id^="para-lang-tabs-"]')].map(b => b.id.slice('para-lang-tabs-'.length));
  }

  function applyMode(scope) {
    const m = mode();
    paraIdxs(scope).forEach(i => {
      const en = document.getElementById('para-lang-en-' + i);
      const ur = document.getElementById('para-lang-ur-' + i);
      const ps = document.getElementById('para-lang-ps-' + i);
      if (!en || !ur || !ps) return;
      en.style.display = 'block';
      ur.style.display = m === 1 ? 'block' : 'none';
      ps.style.display = m === 2 ? 'block' : 'none';
      [ur, ps].forEach(b => b.classList.add('sh-trans'));
    });
  }

  function labels(scope) {
    const i = paraIdxs(scope)[0];
    const en = document.getElementById('para-lang-en-' + i);
    const bar = document.getElementById('para-lang-tabs-' + i);
    const btns = bar ? [...bar.querySelectorAll('button')] : [];
    const orig = en && !latin(en.textContent) ? 'Urdu' : 'English';
    const name = lang => {
      const b = btns.find(x => (x.getAttribute('onclick') || '').includes("'" + lang + "'"));
      const t = b ? clean(b.textContent) : '';
      return /urdu|اردو/i.test(b ? b.textContent : '') ? 'Urdu' : /pashto|پښتو/i.test(b ? b.textContent : '') ? 'Pashto' : (t || lang);
    };
    return [orig, name('ur'), name('ps')];
  }

  function convert(scope) {
    // containers are reused when a reader re-renders a tab, so look for the bar itself
    if (scope.querySelector(':scope > .sh-bar')) { applyMode(scope); return; }
    const ids = paraIdxs(scope);
    if (!ids.length) return;
    scope.classList.add('sh-converted');
    const [o, a, b] = labels(scope);
    const cur = mode();
    const tab = (n, label) => '<button type="button" class="sb-langtab" data-m="' + n + '" aria-pressed="' + (cur === n) + '" onclick="SBLangMode(' + n + ')">' + label + '</button>';
    const bar = document.createElement('div');
    bar.className = 'm6-root sh-bar';
    bar.innerHTML = '<div class="m6-tools m6-tabs" role="group" aria-label="Text language">' +
      tab(0, '📖 Original (' + o + ')') + tab(1, o + ' + ' + a) + tab(2, o + ' + ' + b) + '</div><p class="m6-help">' + HELP + '</p>';
    scope.insertBefore(bar, scope.firstChild);
    applyMode(scope);
  }

  // the lesson content container of the old readers
  function scopes() {
    const out = new Set();
    document.querySelectorAll('.para-lang-tabs-bar[id^="para-lang-tabs-"]').forEach(b => {
      const s = b.closest('#subjTabContent, #bioTabContent, #chemTabContent, #physTabContent, .math-topic-area');
      if (s) out.add(s);
    });
    return [...out];
  }

  // ── Part 2: readers with no language bar at all ─────────────────────────
  // (Class 7/9/10/12 Math, Class 10/12 English, Class 9/12 Urdu, Class 11 books,
  //  Class 12 humanities). The same bar is added; "+ L1/L2" modes show each
  //  paragraph's translation under it — the textbook's own translation where
  //  the dataset has one aligned to the paragraph, otherwise a clearly marked
  //  machine translation, fetched only when the paragraph scrolls into view.
  const UNIT_SEL = 'p, li, .para-text-box, .poetic-line-row';
  const SKIP = 'button, h1, h2, h3, h4, h5, h6, table, .sh-bar, .sh-mt, .ut-root, .katex, .math-acc-header, .m6-tools, .m6-help, .m5-tools, .m5-help, nav, [class*="tabs-bar"], .rt-filter, .para-card-header';
  const NAMES = { en: 'English', ur: 'Urdu', ps: 'Pashto', ar: 'Arabic' };
  const PAIRS = { en: ['ur', 'ps'], ur: ['en', 'ps'], ps: ['en', 'ur'], ar: ['ur', 'en'] };
  const detect = s => (window.SBTranslate ? window.SBTranslate.detectLang(s).lang : (latin(s) ? 'en' : 'ur'));
  const appState = () => { try { return state; } catch (e) { return {}; } };

  function units(scope) {
    const all = [...scope.querySelectorAll(UNIT_SEL)].filter(e =>
      !e.closest(SKIP) && !e.closest('details') && !/source-note/.test(e.className) &&
      e.textContent.trim().length >= 20 && /[A-Za-z؀-ۿ]{3,}/.test(e.textContent));
    const set = new Set(all);
    // leaf-most only: a paragraph box that holds <p>s is represented by those <p>s
    return all.filter(e => ![...e.querySelectorAll(UNIT_SEL)].some(d => set.has(d)));
  }

  function bookLang(list) {
    const score = {};
    list.slice(0, 40).forEach(u => { const l = detect(u.textContent); score[l] = (score[l] || 0) + Math.min(400, u.textContent.length); });
    let best = 'en', top = -1;
    Object.keys(score).forEach(l => { if (score[l] > top) { top = score[l]; best = l; } });
    return best === 'ar' && score.ur ? 'ur' : best; // Quran books: the reading language is Urdu
  }

  // textbook translations stored with Class 9 Urdu, aligned to its paragraph cards
  function storedFor(u, tgt) {
    const st = appState();
    const card = u.closest('.para-card[id^="para-item-"]');
    if (!card || st.selectedClass !== 'cls9' || typeof URDU_DATA === 'undefined') return null;
    const ch = URDU_DATA[st.selectedSubjChapter || 0];
    if (!ch) return null;
    if (!ch.__shFlat) {
      const split = t => String(t || '').split(/【[^】]*】/).slice(1).map(x => x.split(/\n+/).map(s => s.trim()).filter(Boolean));
      const en = split(ch.englishTranslation), ps = split(ch.pashtoTranslation), flat = [];
      (ch.sections || []).forEach((s, i) => {
        if (Array.isArray(s.paras) && s.paras.length) {
          const e = en[i] || [], p = ps[i] || [], n = s.paras.length;
          s.paras.forEach((_, j) => {
            if (e.length === n) flat.push({ en: e[j], ps: p[j] });
            else flat.push(j === n - 1 ? { en: e.join(' '), ps: p.join(' ') } : { en: '', ps: '' });
          });
        } else flat.push({ en: s.english || '', ps: s.pashto || '' });
      });
      ch.__shFlat = flat;
    }
    const row = ch.__shFlat[+card.id.slice('para-item-'.length)];
    if (!row) return null;
    const v = tgt === 'en' ? row.en : tgt === 'ps' ? row.ps : '';
    return v === undefined ? null : v; // '' = covered by the last paragraph of its section
  }

  const queue = []; let busy = 0;
  function pump() {
    while (busy < 3 && queue.length) {
      const job = queue.shift(); busy++;
      window.SBTranslate.translate(job.text, job.src, job.tgt, true)
        .then(r => job.done(r && r.text ? r.text : ''), () => job.done(''))
        .then(() => { busy--; pump(); });
    }
  }

  // Class 11 books: every paragraph keeps its translations in a closed <details> with lang-tagged children
  function detailsBlocks(scope) {
    return [...scope.querySelectorAll('details')].filter(d => d.querySelector(':scope > [lang], :scope > * > [lang]'));
  }
  function applyDetails(scope, tgt) {
    detailsBlocks(scope).forEach(d => {
      const kids = [...d.querySelectorAll('[lang]')].filter(k => k.closest('details') === d && !k.closest('summary'));
      const has = tgt && kids.some(k => k.getAttribute('lang') === tgt);
      if (!tgt || !has) {
        if (d.dataset.shOpened) { d.open = false; delete d.dataset.shOpened; }
        kids.forEach(k => { k.style.display = ''; });
        return;
      }
      if (!d.open) { d.open = true; d.dataset.shOpened = '1'; }
      kids.forEach(k => { k.style.display = k.getAttribute('lang') === tgt ? '' : 'none'; });
    });
  }

  // sentence-level translations stored on .lesson-sentence spans (data-en / data-ur / data-ps)
  function sentenceText(u, tgt) {
    const sents = [...u.querySelectorAll('.lesson-sentence')];
    if (!sents.length) return null;
    const key = 'data-' + tgt;
    const parts = sents.map(x => x.getAttribute(key) || '').filter(Boolean);
    return parts.length ? parts.join(' ') : null;
  }

  function fill(u) {
    const scope = u.closest('.sh-generic');
    const m = mode();
    if (!scope || !m) return;
    const tgt = PAIRS[scope.dataset.shOrig][m - 1];
    u.__shT = u.__shT || {};
    if (u.__shT[tgt]) { u.__shT[tgt].hidden = false; return; }
    const src = detect(u.textContent);
    if (src === tgt) return;
    const box = document.createElement('div');
    box.className = 'sh-mt ' + (tgt === 'en' ? 'sh-ltr' : 'sh-rtl sh-' + tgt);
    box.dataset.lang = tgt;
    box.setAttribute('dir', tgt === 'en' ? 'ltr' : 'rtl');
    u.__shT[tgt] = box;
    if (u.tagName === 'LI') u.appendChild(box); else u.insertAdjacentElement('afterend', box);
    const sent = sentenceText(u, tgt);
    const stored = sent !== null ? sent : storedFor(u, tgt);
    if (stored !== null) {
      if (stored) box.textContent = stored; else box.remove();
      return;
    }
    if (!window.SBTranslate) { box.remove(); return; }
    box.innerHTML = '<span class="sh-wait">Translating…</span>';
    queue.push({
      text: u.textContent.replace(/\s+/g, ' ').trim().slice(0, 1400), src, tgt,
      done: txt => {
        if (!txt) { box.innerHTML = '<span class="sh-wait">Translation needs internet</span>'; return; }
        box.textContent = txt;
        const tag = document.createElement('span');
        tag.className = 'sh-tag'; tag.textContent = 'Machine translation';
        box.appendChild(tag);
      }
    });
    pump();
  }

  const io = 'IntersectionObserver' in window
    ? new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) fill(e.target); }), { rootMargin: '300px 0px' })
    : null;

  function applyGeneric(scope) {
    const m = mode();
    const tgt = m ? PAIRS[scope.dataset.shOrig][m - 1] : null;
    scope.querySelectorAll('.sh-mt').forEach(x => { x.hidden = !tgt || x.dataset.lang !== tgt; });
    const dets = detailsBlocks(scope);
    if (dets.length) { applyDetails(scope, tgt); return; } // the book's own translations, nothing to fetch
    if (!tgt) return;
    units(scope).forEach(u => {
      if (u.__shT && u.__shT[tgt]) { u.__shT[tgt].hidden = false; return; }
      if (io) { io.unobserve(u); io.observe(u); } else fill(u);
    });
  }

  function genericScopes() {
    return [...document.querySelectorAll('.math-topic-area')].map(a => a.querySelector('#subjTabContent') || a)
      .filter(s => s.offsetParent !== null && !s.querySelector('[data-sbmode], .mq-tabs, .para-lang-tabs-bar') &&
        !(s.querySelector('.sb-langtab') && !s.querySelector('.sh-gbar')));
  }

  function generic(scope) {
    if (scope.querySelector(':scope > .sh-gbar')) { applyGeneric(scope); return; }
    const list = units(scope);
    if (list.length < 2) return;
    const tagged = [...scope.querySelectorAll('[lang]')].filter(e => !e.closest('details') && !e.closest(SKIP) && PAIRS[e.getAttribute('lang')]);
    let o = bookLang(list);
    if (tagged.length && detailsBlocks(scope).length) {
      const w = {};
      tagged.forEach(e => { const l = e.getAttribute('lang'); w[l] = (w[l] || 0) + e.textContent.length; });
      o = Object.keys(w).sort((x, y) => w[y] - w[x])[0];
      if (o === 'ar') o = 'ur';
    }
    const [a, b] = PAIRS[o];
    scope.dataset.shOrig = o;
    scope.classList.add('sh-generic');
    const cur = mode();
    const tab = (n, label) => '<button type="button" class="sb-langtab" data-m="' + n + '" aria-pressed="' + (cur === n) + '" onclick="SBLangMode(' + n + ')">' + label + '</button>';
    const bar = document.createElement('div');
    bar.className = 'm6-root sh-bar sh-gbar';
    bar.innerHTML = '<div class="m6-tools m6-tabs" role="group" aria-label="Text language">' +
      tab(0, '📖 Original (' + NAMES[o] + ')') + tab(1, NAMES[o] + ' + ' + NAMES[a]) + tab(2, NAMES[o] + ' + ' + NAMES[b]) +
      '</div><p class="m6-help">' + HELP + '</p>';
    scope.insertBefore(bar, scope.firstChild);
    applyGeneric(scope);
  }

  // ── Part 3: one set of Mathematics tab names in every class ─────────────
  // Classes use three namings for the same five tabs; show the same words everywhere
  // (counts such as "(21)" are kept). Only the visible label changes.
  const MATH_TABS = ['Lessons', 'Worked Examples', 'Exercises', 'SLOs & MCQs', 'Summary & Formulas'];
  function mathTabs() {
    const cur = window.SBContinue && window.SBContinue.current && window.SBContinue.current();
    if (!cur || !/-math$/.test(cur.subjId)) return;
    const tabs = [...document.querySelectorAll('.math-topic-area .math-top-tab, .math-topic-area .math-tab-btn')]
      .filter(b => !b.closest('#subjTabContent'));
    if (tabs.length !== 5) return;
    tabs.forEach((b, i) => {
      const want = MATH_TABS[i];
      const text = [...b.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim());
      const node = text[text.length - 1];
      if (!node) return;
      const raw = node.textContent.trim();
      const count = (raw.match(/\(\d+\)\s*$/) || [''])[0];
      const label = ' ' + want + (count ? ' ' + count : '');
      if (node.textContent !== label && raw.replace(/^\d+\.\s*/, '') !== want + (count ? ' ' + count : '')) node.textContent = label;
    });
  }

  function run() {
    scopes().forEach(convert);
    genericScopes().forEach(generic);
    mathTabs();
  }

  // one global mode for old and new readers alike
  function hookMode() {
    const orig = window.SBLangMode;
    if (typeof orig !== 'function' || orig.__sh) return false;
    const wrapped = function (n) {
      const r = orig.apply(this, arguments);
      document.querySelectorAll('.sh-converted').forEach(applyMode);
      document.querySelectorAll('.sh-generic').forEach(applyGeneric);
      return r;
    };
    wrapped.__sh = true;
    window.SBLangMode = wrapped;
    return true;
  }
  if (!hookMode()) {
    // no standard reader loaded: provide the same global switch
    window.SB_LANG_MODE = window.SB_LANG_MODE || 0;
    window.SBLangMode = function (n) {
      window.SB_LANG_MODE = n;
      document.querySelectorAll('[data-sbmode]').forEach(r => { r.dataset.sbmode = String(n); });
      document.querySelectorAll('.sb-langtab').forEach(b => b.setAttribute('aria-pressed', String(Number(b.dataset.m) === n)));
      document.querySelectorAll('.sh-converted').forEach(applyMode);
      document.querySelectorAll('.sh-generic').forEach(applyGeneric);
    };
    window.SBLangMode.__sh = true;
  }

  let t = 0;
  const schedule = () => { clearTimeout(t); t = setTimeout(run, 120); };
  function start() {
    new MutationObserver(schedule).observe(document.getElementById('dashboard-body') || document.body, { childList: true, subtree: true });
    schedule();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();

  window.SBHarmonizer = {
    refresh: run,
    // translate every paragraph of the open lesson now (printing, or when scrolling isn't observable)
    fillAll: () => document.querySelectorAll('.sh-generic').forEach(sc => { if (mode()) units(sc).forEach(fill); })
  };
})();
