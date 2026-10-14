/* ======================================================================
 *  universal_translate.js — one translator for every book, tab and class
 *
 *  Select any word or sentence (mouse drag, double-click, or long-press on
 *  phones) in any language — English, Urdu, Pashto or Arabic — and a small
 *  bar offers the OTHER three languages. Tapping one shows the translation
 *  in a compact card that can switch between the three targets, read it
 *  aloud, or copy it. Single-word clicks that app.js already routes to
 *  showWordLookupPopover() open the same card, so there is one consistent
 *  translator across the whole project.
 *
 *  Self-contained: loaded after app.js, owns its own CSS
 *  (css/universal_translate.css). Public API: window.SBTranslate.
 * ====================================================================== */
(function () {
  'use strict';

  const LANGS = {
    en: { name: 'English', native: 'English', dir: 'ltr', tts: 'en-US', cls: 'ut-en' },
    ur: { name: 'Urdu', native: 'اردو', dir: 'rtl', tts: 'ur-PK', cls: 'ut-ur' },
    ps: { name: 'Pashto', native: 'پښتو', dir: 'rtl', tts: 'ps-AF', cls: 'ut-ps' },
    ar: { name: 'Arabic', native: 'العربية', dir: 'rtl', tts: 'ar-SA', cls: 'ut-ar' }
  };
  const ORDER = ['en', 'ur', 'ps', 'ar'];
  const MAX_CHARS = 1500;
  const IGNORE_SEL = 'input, textarea, select, [contenteditable=""], [contenteditable="true"], .ut-root, #eng-word-popover, .katex, script, style';

  // ── storage (per-viewer convenience only; always optional) ──────────────
  const store = {
    get(k, d) { try { const v = localStorage.getItem('sbT:' + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem('sbT:' + k, JSON.stringify(v)); } catch (e) { /* private mode */ } }
  };
  const memCache = new Map();

  // ── language detection (script-based, offline) ──────────────────────────
  const RX = {
    latin: /[A-Za-z]/g,
    arabicScript: /[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]/g,
    pashto: /[ټځڅډړږښګڼۍېۉ]/g, // ټ ځ څ ډ ړ ږ ښ ګ ڼ ۍ ې
    urdu: /[ٹڈڑںھہۂےۓ]/g,                      // ٹ ڈ ڑ ں ھ ہ ۂ ے ۓ
    arabic: /[ةكىيٱ]/g,                                            // ة ك ى ي ٱ
    harakat: /[ً-ْٰۡ]/g
  };
  const count = (s, rx) => (s.match(rx) || []).length;

  function detectLang(text) {
    const s = String(text || '');
    const lat = count(s, RX.latin);
    const ara = count(s, RX.arabicScript);
    if (lat === 0 && ara === 0) return { lang: 'en', sure: false };
    if (lat > ara) return { lang: 'en', sure: true };
    const ps = count(s, RX.pashto) * 3;
    const ur = count(s, RX.urdu) * 2;
    const harak = count(s, RX.harakat);
    const ar = count(s, RX.arabic) * 1.5 + (harak / Math.max(1, ara) > 0.18 ? harak : 0);
    const best = Math.max(ps, ur, ar);
    if (best === 0) return { lang: 'ur', sure: false };
    if (best === ps) return { lang: 'ps', sure: true };
    if (best === ur) return { lang: 'ur', sure: true };
    return { lang: 'ar', sure: true };
  }

  // ── translation engines ─────────────────────────────────────────────────
  function dictLookup(word, tgt) {
    if (!/^[a-z][a-z'-]*$/i.test(word)) return '';
    const key = word.toLowerCase();
    let e = null;
    try {
      if (typeof window.lookupEngWord === 'function') e = window.lookupEngWord(key);
      if (!e && typeof ENG_URDU_DICT !== 'undefined') e = ENG_URDU_DICT[key];
    } catch (err) { e = null; }
    if (!e) return '';
    const v = tgt === 'ur' ? e.u : tgt === 'ps' ? e.p : '';
    if (!v || v.toLowerCase() === key || /^اردو معنی/.test(v)) return '';
    return v;
  }

  async function viaGoogle(text, src, tgt) {
    const url = 'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=' +
      encodeURIComponent(src) + '&tl=' + encodeURIComponent(tgt) + '&q=' + encodeURIComponent(text);
    const res = await fetch(url);
    if (!res.ok) throw new Error('google ' + res.status);
    const data = await res.json();
    const out = (data && data[0] || []).map(p => p && p[0] || '').join('').trim();
    if (!out) throw new Error('google empty');
    return { text: out, detected: data[2] || '' };
  }

  async function viaMyMemory(text, src, tgt) {
    const pair = (src === 'auto' ? 'ur' : src) + '|' + tgt;
    const res = await fetch('https://api.mymemory.translated.net/get?q=' + encodeURIComponent(text.slice(0, 480)) + '&langpair=' + pair);
    if (!res.ok) throw new Error('mymemory ' + res.status);
    const data = await res.json();
    const out = data && data.responseData && String(data.responseData.translatedText || '').trim();
    if (!out || /MYMEMORY|WARNING|QUOTA|LIMIT|INVALID/i.test(out)) throw new Error('mymemory empty');
    return { text: out, detected: '' };
  }

  async function translate(text, src, tgt, sure) {
    const clean = String(text || '').replace(/\s+/g, ' ').trim().slice(0, MAX_CHARS);
    if (!clean) return { text: '', source: 'none' };
    const key = src + '>' + tgt + ':' + clean;
    if (memCache.has(key)) return memCache.get(key);
    const persisted = store.get('c:' + key, null);
    if (persisted) { memCache.set(key, persisted); return persisted; }

    let result = null;
    const dict = (src === 'en' && !/\s/.test(clean)) ? dictLookup(clean.replace(/[^A-Za-z'-]/g, ''), tgt) : '';
    try {
      const g = await viaGoogle(clean, sure ? src : 'auto', tgt);
      result = { text: g.text, source: 'online', dict, detected: g.detected };
    } catch (e1) {
      try {
        const m = await viaMyMemory(clean, src, tgt);
        result = { text: m.text, source: 'online', dict };
      } catch (e2) {
        result = dict ? { text: dict, source: 'dictionary' } : { text: '', source: 'offline' };
      }
    }
    if (result.text) {
      memCache.set(key, result);
      if (clean.length <= 300) store.set('c:' + key, result);
    }
    return result;
  }

  // ── speech ──────────────────────────────────────────────────────────────
  function speak(text, lang) {
    const clean = String(text || '').trim();
    if (!clean) return;
    const info = LANGS[lang] || LANGS.en;
    const synth = window.speechSynthesis;
    const voices = synth ? synth.getVoices() : [];
    const voice = voices.find(v => v.lang && v.lang.toLowerCase().startsWith(lang));
    if (synth && (voice || lang === 'en')) {
      synth.cancel();
      const u = new SpeechSynthesisUtterance(clean);
      u.lang = info.tts;
      if (voice) u.voice = voice;
      u.rate = 0.9;
      synth.speak(u);
      return;
    }
    if (lang === 'ps') { toast('Pashto voice is not available on this device'); return; }
    try {
      const a = new Audio('https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=' + lang + '&q=' + encodeURIComponent(clean.slice(0, 190)));
      a.play().catch(() => toast('Audio is not available right now'));
    } catch (e) { toast('Audio is not available right now'); }
  }

  // ── DOM helpers ─────────────────────────────────────────────────────────
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  function el(tag, cls, html) { const n = document.createElement(tag); if (cls) n.className = cls; if (html != null) n.innerHTML = html; return n; }

  let pill = null, card = null, toastEl = null;
  let state = { text: '', src: 'en', sure: false, tgt: null, rect: null, range: null, req: 0 };

  function stopAll(node) {
    // keep app.js' document click handler (and selection logic) away from our UI
    ['click', 'mousedown', 'mouseup', 'touchstart', 'touchend', 'pointerdown', 'pointerup'].forEach(t =>
      node.addEventListener(t, e => e.stopPropagation()));
  }

  function toast(msg) {
    if (!toastEl) { toastEl = el('div', 'ut-root ut-toast'); toastEl.setAttribute('role', 'status'); document.body.appendChild(toastEl); }
    toastEl.textContent = msg;
    toastEl.classList.add('ut-show');
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(() => toastEl && toastEl.classList.remove('ut-show'), 1800);
  }

  function targetsFor(src) { return ORDER.filter(l => l !== src); }
  function preferredTarget(src) {
    const p = store.get('pref:' + src, null);
    if (p && p !== src && LANGS[p]) return p;
    return src === 'en' ? 'ur' : 'en';
  }

  function place(node, rect) {
    const vw = window.innerWidth, vh = window.innerHeight, gap = 10;
    node.style.visibility = 'hidden';
    node.style.left = '0px'; node.style.top = '0px';
    const w = node.offsetWidth, h = node.offsetHeight;
    const r = rect || { left: vw / 2, right: vw / 2, top: vh / 3, bottom: vh / 3, width: 0 };
    let left = (r.left + r.right) / 2 - w / 2;
    left = Math.max(12, Math.min(left, vw - w - 12));
    // below the selection by default (phones draw their own menu above it)
    let top = r.bottom + gap;
    if (top + h > vh - 8) top = r.top - h - gap;
    if (top < 8) top = Math.max(8, Math.min(vh - h - 8, r.bottom + gap));
    node.style.left = Math.round(left) + 'px';
    node.style.top = Math.round(top) + 'px';
    node.style.visibility = '';
  }

  // ── the selection bar ───────────────────────────────────────────────────
  function showPill(text, rect, range) {
    hideCard();
    const det = detectLang(text);
    state = Object.assign(state, { text, src: det.lang, sure: det.sure, rect, range, tgt: null });
    if (!pill) {
      pill = el('div', 'ut-root ut-pill');
      pill.setAttribute('role', 'toolbar');
      pill.setAttribute('aria-label', 'Translate selection');
      stopAll(pill);
      pill.addEventListener('click', e => {
        const b = e.target.closest('button');
        if (!b) return;
        if (b.dataset.lang) openCard(state.text, b.dataset.lang, state.rect);
        else if (b.dataset.act === 'speak') speak(state.text, state.src);
      });
      document.body.appendChild(pill);
    }
    const pref = preferredTarget(state.src);
    pill.innerHTML =
      '<span class="ut-pill-icon" aria-hidden="true">文A</span>' +
      targetsFor(state.src).map(l =>
        '<button type="button" class="ut-pill-btn ' + LANGS[l].cls + (l === pref ? ' ut-pref' : '') + '" data-lang="' + l + '" title="Translate to ' + LANGS[l].name + '">' + LANGS[l].native + '</button>'
      ).join('') +
      '<button type="button" class="ut-pill-btn ut-pill-speak" data-act="speak" title="Listen" aria-label="Listen">🔊</button>';
    pill.classList.add('ut-show');
    place(pill, rect);
  }
  function hidePill() { if (pill) pill.classList.remove('ut-show'); }

  // ── the translation card ────────────────────────────────────────────────
  function openCard(text, tgt, rect, srcOverride) {
    hidePill();
    const det = srcOverride ? { lang: srcOverride, sure: true } : detectLang(text);
    state.text = String(text).trim();
    state.src = det.lang; state.sure = det.sure;
    state.rect = rect || state.rect;
    state.tgt = tgt && tgt !== state.src ? tgt : preferredTarget(state.src);
    store.set('pref:' + state.src, state.tgt);

    if (!card) {
      card = el('div', 'ut-root ut-card');
      card.setAttribute('role', 'dialog');
      card.setAttribute('aria-label', 'Translation');
      stopAll(card);
      card.addEventListener('click', e => {
        const b = e.target.closest('button');
        if (!b) { if (card.dataset.via === 'hover') hideCard(); return; }
        const l = b.dataset.lang, out = l ? (state.outs[l] || '') : '';
        if (b.dataset.act === 'close') hideCard();
        else if (b.dataset.act === 'speak-src') speak(state.text, state.src);
        else if (b.dataset.act === 'speak') speak(out, l);
        else if (b.dataset.act === 'copy') copyText(out);
        else if (b.dataset.act === 'more') card.classList.toggle('ut-expand');
      });
      document.body.appendChild(card);
    }
    card.dataset.via = 'select';
    renderCard();
  }

  // one row per other language: label on the left, its meaning right next to it
  function renderCard() {
    const src = state.src, S = LANGS[src];
    const long = state.text.length > 140;
    state.outs = {};
    card.innerHTML =
      '<div class="ut-card-head">' +
        '<span class="ut-chip">' + esc(S.native) + '</span>' +
        '<span class="ut-src ' + S.cls + (long ? ' ut-clamp' : '') + '" dir="' + S.dir + '">' + esc(state.text) + '</span>' +
        '<button type="button" class="ut-ic" data-act="speak-src" title="Listen" aria-label="Listen">🔊</button>' +
        '<button type="button" class="ut-ic ut-x" data-act="close" title="Close" aria-label="Close">✕</button>' +
      '</div>' +
      (long ? '<button type="button" class="ut-more" data-act="more">Show full text</button>' : '') +
      '<div class="ut-rows">' +
        targetsFor(src).map(l =>
          '<div class="ut-row" data-row="' + l + '">' +
            '<span class="ut-lab ' + LANGS[l].cls + '">' + LANGS[l].native + '</span>' +
            '<span class="ut-mean ' + LANGS[l].cls + '" dir="' + LANGS[l].dir + '" aria-live="polite"><span class="ut-loading">…</span></span>' +
            '<button type="button" class="ut-ic" data-act="speak" data-lang="' + l + '" title="Listen" aria-label="Listen to ' + LANGS[l].name + '">🔊</button>' +
            '<button type="button" class="ut-ic" data-act="copy" data-lang="' + l + '" title="Copy" aria-label="Copy ' + LANGS[l].name + '">⧉</button>' +
          '</div>'
        ).join('') +
      '</div>' +
      (src === 'ar' && count(state.text, RX.harakat) > 4 ? '<div class="ut-quran-note">For Quranic ayat, follow the approved translation in your textbook.</div>' : '');
    card.classList.add('ut-show');
    place(card, state.rect);

    const reqId = ++state.req;
    targetsFor(src).forEach(l => {
      translate(state.text, src, l, state.sure).then(r => {
        if (reqId !== state.req || !card) return;
        const cell = card.querySelector('.ut-row[data-row="' + l + '"] .ut-mean');
        if (!cell) return;
        if (!r.text) { cell.innerHTML = '<span class="ut-err">offline</span>'; return; }
        state.outs[l] = r.text;
        cell.textContent = r.text;
        cell.title = r.source === 'dictionary' ? 'Dictionary meaning' : 'Machine translation';
        place(card, state.rect);
      });
    });
  }

  function hideCard() { if (card) { card.classList.remove('ut-show', 'ut-expand'); state.req++; } }

  function copyText(t) {
    if (!t) return;
    const done = () => toast('Copied');
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done, () => fallbackCopy(t, done));
    else fallbackCopy(t, done);
  }
  function fallbackCopy(t, done) {
    const ta = el('textarea', 'ut-root'); ta.value = t; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); done(); } catch (e) { /* ignore */ }
    ta.remove();
  }

  // ── selection watching ──────────────────────────────────────────────────
  let pointerDown = false, selTimer = 0;

  function currentSelection() {
    const sel = window.getSelection && window.getSelection();
    if (!sel || sel.rangeCount === 0 || sel.isCollapsed) return null;
    const text = sel.toString().replace(/\s+/g, ' ').trim();
    if (text.length < 1 || text.length > MAX_CHARS) return null;
    if (!/[A-Za-z؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]/.test(text)) return null; // numbers / symbols only
    const range = sel.getRangeAt(0);
    const anchor = range.commonAncestorContainer.nodeType === 1 ? range.commonAncestorContainer : range.commonAncestorContainer.parentElement;
    if (!anchor || anchor.closest(IGNORE_SEL)) return null;
    const rects = range.getClientRects();
    const rect = rects.length ? rects[rects.length - 1] : range.getBoundingClientRect();
    if (!rect || (rect.width === 0 && rect.height === 0)) return null;
    // span the whole selection horizontally when it sits on one line
    const box = range.getBoundingClientRect();
    return { text, range, rect: { left: box.height < rect.height * 1.6 ? box.left : rect.left, right: box.height < rect.height * 1.6 ? box.right : rect.right, top: rect.top, bottom: rect.bottom, width: rect.width } };
  }

  function evaluateSelection() {
    if (pointerDown) return;
    if (card && card.classList.contains('ut-show')) return; // a word card is already open
    const s = currentSelection();
    if (s) showPill(s.text, s.rect, s.range);
    else hidePill();
  }

  document.addEventListener('pointerdown', e => {
    if (e.target.closest && e.target.closest('.ut-root')) return;
    pointerDown = true;
    hidePill();
  }, true);
  document.addEventListener('pointerup', () => {
    pointerDown = false;
    clearTimeout(selTimer);
    selTimer = setTimeout(evaluateSelection, 30);
  }, true);
  document.addEventListener('pointercancel', () => { pointerDown = false; }, true);
  document.addEventListener('selectionchange', () => {
    clearTimeout(selTimer);
    // phones adjust selections with handles (no pointerup) — wait for it to settle
    selTimer = setTimeout(evaluateSelection, pointerDown ? 600 : 350);
  });
  document.addEventListener('keyup', e => { if (e.shiftKey || e.key === 'Shift') { clearTimeout(selTimer); selTimer = setTimeout(evaluateSelection, 120); } });

  // finishing a drag-selection must not also "click" the text under it
  // (e.g. open a sentence drawer) — the selection bar is the response
  document.addEventListener('click', e => {
    if (e.target.closest && e.target.closest('.ut-root')) return;
    const sel = window.getSelection && window.getSelection();
    if (sel && !sel.isCollapsed && /\s/.test(sel.toString().trim()) && e.target.closest && e.target.closest('.lesson-sentence')) {
      e.stopPropagation();
    }
  }, true);

  // ── finding the word under the pointer ─────────────
  const HOLD_MS = 450, HOLD_SLOP = 8;
  const WORD_CH = /[\p{L}\p{M}\p{N}'’\-]/u;
  let hold = null, swallowClick = false;

  function wordAt(x, y) {
    let node, off;
    if (document.caretRangeFromPoint) {
      const r = document.caretRangeFromPoint(x, y);
      if (!r) return null;
      node = r.startContainer; off = r.startOffset;
    } else if (document.caretPositionFromPoint) {
      const p = document.caretPositionFromPoint(x, y);
      if (!p) return null;
      node = p.offsetNode; off = p.offset;
    } else return null;
    if (!node || node.nodeType !== 3) return null;
    const host = node.parentElement;
    if (!host || host.closest(IGNORE_SEL)) return null;
    const s = node.data;
    let a = off, b = off;
    while (a > 0 && WORD_CH.test(s[a - 1])) a--;
    while (b < s.length && WORD_CH.test(s[b])) b++;
    const word = s.slice(a, b).replace(/^['’\-]+|['’\-]+$/g, '');
    if (!word || !/\p{L}/u.test(word)) return null;
    const range = document.createRange();
    range.setStart(node, a); range.setEnd(node, b);
    const rect = range.getBoundingClientRect();
    // caret APIs snap to the nearest text, so make sure the pointer is really on the word
    if (!rect || x < rect.left - 4 || x > rect.right + 4 || y < rect.top - 4 || y > rect.bottom + 4) return null;
    return { word, range, rect };
  }

  const asRect = r => ({ left: r.left, right: r.right, top: r.top, bottom: r.bottom, width: r.width });
  function hasSelection() { const s = window.getSelection && window.getSelection(); return !!(s && !s.isCollapsed && s.toString().trim()); }

  // ── mouse: resting the pointer on a word opens its card; clicks are left alone ──
  const HOVER_MS = 280, HIDE_MS = 380;
  let hoverKey = '', hoverOpenT = 0, hoverHideT = 0, hoverRaf = false, lastMove = null;
  function hoverCardOpen() { return card && card.classList.contains('ut-show') && card.dataset.via === 'hover'; }
  function scheduleHide() {
    clearTimeout(hoverHideT);
    if (hoverCardOpen()) hoverHideT = setTimeout(() => { if (hoverCardOpen()) { hideCard(); hoverKey = ''; } }, HIDE_MS);
  }
  function onHoverFrame() {
    hoverRaf = false;
    const e = lastMove;
    if (!e) return;
    if (e.target.closest && e.target.closest('.ut-root')) { clearTimeout(hoverHideT); clearTimeout(hoverOpenT); return; }
    if (e.buttons || hasSelection() || (pill && pill.classList.contains('ut-show'))) { clearTimeout(hoverOpenT); return; }
    if (card && card.classList.contains('ut-show') && card.dataset.via !== 'hover') return; // a card opened from a selection stays put
    const w = wordAt(e.clientX, e.clientY);
    if (!w) { clearTimeout(hoverOpenT); hoverKey = ''; scheduleHide(); return; }
    const key = w.word + '@' + Math.round(w.rect.left) + ',' + Math.round(w.rect.top);
    if (key === hoverKey) { clearTimeout(hoverHideT); return; }
    hoverKey = key;
    clearTimeout(hoverOpenT);
    hoverOpenT = setTimeout(() => {
      if (hoverKey !== key || hasSelection()) return;
      clearTimeout(hoverHideT);
      state.range = w.range;
      openCard(w.word, null, asRect(w.rect));
      card.dataset.via = 'hover';
    }, HOVER_MS);
  }
  document.addEventListener('pointermove', e => {
    if (e.pointerType !== 'mouse') return;
    lastMove = e;
    if (!hoverRaf) { hoverRaf = true; requestAnimationFrame(onHoverFrame); }
  }, { passive: true });
  document.addEventListener('mouseleave', () => { clearTimeout(hoverOpenT); hoverKey = ''; scheduleHide(); });
  window.addEventListener('scroll', () => { clearTimeout(hoverOpenT); hoverKey = ''; }, true);

  // ── touch (no hover): press-and-hold on a word opens its card ──
  function cancelHold() { if (hold) { clearTimeout(hold.t); hold = null; } }
  document.addEventListener('pointerdown', e => {
    cancelHold();
    if (e.pointerType === 'mouse' || !e.isPrimary) return;
    if (e.target.closest && e.target.closest(IGNORE_SEL)) return;
    const x = e.clientX, y = e.clientY;
    hold = { x, y, t: setTimeout(() => {
      hold = null;
      const w = wordAt(x, y);
      if (!w) return;
      swallowClick = true;
      state.range = w.range;
      openCard(w.word, null, asRect(w.rect));
      card.dataset.via = 'touch';
    }, HOLD_MS) };
  }, true);
  document.addEventListener('pointermove', e => {
    if (hold && Math.hypot(e.clientX - hold.x, e.clientY - hold.y) > HOLD_SLOP) cancelHold();
  }, true);
  document.addEventListener('pointerup', cancelHold, true);
  document.addEventListener('pointercancel', cancelHold, true);
  window.addEventListener('scroll', cancelHold, true);
  // the release after a hold must not also tap the word (open a drawer, follow a link…)
  document.addEventListener('click', e => {
    if (!swallowClick) return;
    swallowClick = false;
    if (e.target.closest && e.target.closest('.ut-root')) return;
    e.preventDefault(); e.stopPropagation();
  }, true);
  document.addEventListener('pointerdown', () => { swallowClick = false; });
  document.addEventListener('contextmenu', e => {
    if (card && card.classList.contains('ut-show') && swallowClick) e.preventDefault();
  }, true);

  // outside click closes the card; Esc closes everything
  document.addEventListener('mousedown', e => {
    if (card && card.classList.contains('ut-show') && !(e.target.closest && e.target.closest('.ut-root'))) hideCard();
  }, true);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { hideCard(); hidePill(); } });

  // keep floating UI attached to the text while the page scrolls
  let rafPending = false;
  function follow() {
    rafPending = false;
    if (!state.range) return;
    let r;
    try { r = state.range.getBoundingClientRect(); } catch (e) { return; }
    if (!r || (r.width === 0 && r.height === 0)) { hidePill(); return; }
    if (r.bottom < 0 || r.top > window.innerHeight) { hidePill(); return; }
    state.rect = { left: r.left, right: r.right, top: r.top, bottom: r.bottom, width: r.width };
    if (pill && pill.classList.contains('ut-show')) place(pill, state.rect);
    if (card && card.classList.contains('ut-show')) place(card, state.rect);
  }
  window.addEventListener('scroll', () => { if (!rafPending) { rafPending = true; requestAnimationFrame(follow); } }, true);
  window.addEventListener('resize', () => { if (!rafPending) { rafPending = true; requestAnimationFrame(follow); } });

  // ── unify app.js' single-word popover with this translator ──────────────
  function rectOf(target, event) {
    if (target && target.getBoundingClientRect) {
      const r = target.getBoundingClientRect();
      if (r.width && r.height && r.height < 80) return r;
    }
    if (event && 'clientX' in event) return { left: event.clientX, right: event.clientX, top: event.clientY - 10, bottom: event.clientY + 10, width: 0 };
    return null;
  }

  // Clicking a word keeps whatever the page already does on click (sentence
  // translation, drawers…); word translation now opens on hover / long-press.
  // Only an explicit vocabulary card still opens the card when clicked.
  window.showWordLookupPopover = function (wordText, targetEl, event) {
    if (!(targetEl && targetEl.closest && targetEl.closest('.vocab-card'))) return;
    const word = String(wordText || '').trim().replace(/^[^\w؀-ۿ]+|[^\w؀-ۿ]+$/g, '');
    if (!word) return;
    state.range = null;
    openCard(word, null, rectOf(targetEl, event));
  };
  window.closeWordLookupPopover = function () {
    const old = document.getElementById('eng-word-popover');
    if (old) old.remove();
    if (card && card.dataset.via === 'select') hideCard();
  };

  // app.js' small hover tooltip (Urdu + Pashto) would sit on top of the hover
  // card, which already shows all four languages — keep it hidden
  if (typeof window.showWordHoverTooltip === 'function') {
    window.showWordHoverTooltip = function () {
      if (typeof window.hideWordHoverTooltip === 'function') window.hideWordHoverTooltip();
    };
  }

  // Arabic for step-by-step solution panels (steps carry en/ur/ps only):
  // translate the prose around $…$ maths, keep the maths untouched, cache on the step
  function prepareSteps(steps) {
    return Promise.all((steps || []).map(s => {
      if (!s || s.ar || !s.en) return null;
      if (s._arP) return s._arP;
      const parts = String(s.en).split(/(\$\$[^$]*\$\$|\$[^$]*\$)/);
      s._arP = Promise.all(parts.map(part => {
        if (/^\$/.test(part) || !/[A-Za-z]/.test(part)) return part;
        const lead = part.match(/^\s*/)[0], tail = part.match(/\s*$/)[0];
        return translate(part.trim(), 'en', 'ar', true).then(r => r.text ? lead + r.text + tail : part);
      })).then(out => { s.ar = out.join(''); return s.ar; });
      return s._arP;
    }));
  }

  window.SBTranslate = { translate, detectLang, speak, open: (text, tgt) => openCard(text, tgt, null), prepareSteps, languages: LANGS };
})();
