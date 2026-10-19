/* SBA11y (Phase 12, first part): keyboard and screen-reader basics that every view shares, without scanning the page.
 *
 *   Tab bars   any group of buttons whose class contains "tab-btn" or "top-tab" (the chapter tabs, the Maths tabs, the sub-tab bars) becomes
 *              role=tablist / role=tab with aria-selected following the "active" class and a roving tabindex (only the active tab is in the
 *              Tab order); the arrow keys (mirrored in right-to-left pages), Home and End move between tabs and open the one reached.
 *              Applied after the render functions that draw the bars (through SBHooks) and re-synced after every click; no observer.
 *   Dialogs    SBA11y.trap(dialog, {onClose}) keeps Tab inside the dialog, Escape calls onClose, and focus returns to what had it before;
 *              it returns a release() function.
 *   SBA11y.enhance(scope) applies the tab roles inside scope (default: the document). */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory;
  else root.SBA11y = factory(root);
})(typeof self !== 'undefined' ? self : this, function (win) {
  'use strict';
  const doc = win.document;
  const TAB = 'button[class*="tab-btn"], button[class*="top-tab"]';
  const FOCUSABLE = 'a[href], summary, button:not([disabled]), input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';

  // a tab that opens a dialog instead of a panel (the Word Stats button) is in the bar but not in the arrow-key cycle
  const isAction = t => t.classList.contains('ws-subj-tab');
  const visible = t => !t.hidden && t.style.display !== 'none';
  const tabsOf = group => [...group.children].filter(c => c.matches && c.matches(TAB) && visible(c) && !isAction(c));
  function sync(group) {
    const all = [...group.children].filter(c => c.matches && c.matches(TAB));
    const tabs = all.filter(t => visible(t) && !isAction(t));
    if (tabs.length < 2) return;
    group.setAttribute('role', 'tablist');
    const active = tabs.find(t => t.classList.contains('active')) || tabs[0];
    all.forEach(t => {
      t.setAttribute('role', 'tab');
      if (isAction(t)) { t.setAttribute('aria-selected', 'false'); t.tabIndex = 0; return; }
      const on = t === active;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      if (visible(t)) t.tabIndex = on ? 0 : -1;
    });
  }
  function enhance(scope) {
    if (!doc) return;
    const seen = new Set();
    (scope || doc).querySelectorAll(TAB).forEach(b => { const g = b.parentElement; if (g && !seen.has(g)) { seen.add(g); sync(g); } });
  }

  function onKey(e) {
    const t = e.target && e.target.closest ? e.target.closest(TAB) : null;
    if (!t || !t.parentElement) return;
    sync(t.parentElement);
    const tabs = tabsOf(t.parentElement);
    if (tabs.length < 2 || !tabs.includes(t)) return;
    const rtl = win.getComputedStyle && win.getComputedStyle(t.parentElement).direction === 'rtl';
    const i = tabs.indexOf(t);
    let to = -1;
    if (e.key === 'ArrowRight') to = rtl ? i - 1 : i + 1;
    else if (e.key === 'ArrowLeft') to = rtl ? i + 1 : i - 1;
    else if (e.key === 'Home') to = 0;
    else if (e.key === 'End') to = tabs.length - 1;
    else return;
    e.preventDefault();
    to = (to + tabs.length) % tabs.length;
    const target = tabs[to], key = target.getAttribute('data-tab'), parent = t.parentElement;
    const parentSel = parent.classList.length ? '.' + [...parent.classList].join('.') : '';
    target.focus();
    target.click();                                 // automatic activation: the tab reached opens
    // opening a tab often redraws or reorders the bar (a button that is moved or replaced loses the focus to the page): put the focus back
    // on the same tab, whether the old button is still there or the new bar has a fresh one. Only when the focus fell to the page: a handler
    // that moved it on purpose (a dialog, a field) keeps it.
    const refocus = () => {
      const el = doc.contains(target) ? target : (key && parentSel ? doc.querySelector(parentSel + ' [data-tab="' + key + '"]') : null);
      const a = doc.activeElement;
      if (el && a !== el && (!a || a === doc.body)) el.focus();
      const bar = el && el.parentElement ? el.parentElement : (doc.contains(parent) ? parent : null);
      if (bar) sync(bar);
    };
    refocus();
    win.setTimeout(refocus, 0);                     // a redraw that a handler schedules for the next tick
  }
  function onClick(e) {
    const t = e.target && e.target.closest ? e.target.closest(TAB) : null;
    if (t && t.parentElement) win.setTimeout(() => sync(t.parentElement), 0);     // after the click handler has moved the "active" class
  }

  function onFocusIn(e) {
    const t = e.target && e.target.closest ? e.target.closest(TAB) : null;
    if (t && t.parentElement && t.getAttribute('role') !== 'tab') sync(t.parentElement);
  }

  // ---- dialogs
  // a control the keyboard can reach: not inside a hidden / aria-hidden / inert branch, and not inside a closed <details> (its summary stays reachable)
  function reachable(el, root) {
    for (let n = el; n && n !== root.parentNode; n = n.parentElement) {
      if (n.hidden || n.inert || n.getAttribute('aria-hidden') === 'true') return false;
      if (n.tagName === 'DETAILS' && !n.open) {
        const s = [...n.children].find(c => c.tagName === 'SUMMARY');
        if (!(s && s.contains(el))) return false;
      }
    }
    return true;
  }
  function trap(dialog, opts = {}) {
    const before = doc.activeElement;
    const focusables = () => [...dialog.querySelectorAll(FOCUSABLE)].filter(el => reachable(el, dialog));
    const onKeydown = e => {
      if (e.key === 'Escape' && opts.onClose) { e.preventDefault(); opts.onClose(); return; }
      if (e.key !== 'Tab') return;
      const f = focusables();
      if (!f.length) { e.preventDefault(); return; }
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && (doc.activeElement === first || !dialog.contains(doc.activeElement))) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && (doc.activeElement === last || !dialog.contains(doc.activeElement))) { e.preventDefault(); first.focus(); }
    };
    doc.addEventListener('keydown', onKeydown, true);
    const f = focusables();
    if (f.length && !dialog.contains(doc.activeElement)) f[0].focus();
    return function release() {
      doc.removeEventListener('keydown', onKeydown, true);
      if (before && before.focus && doc.contains(before)) before.focus();
    };
  }

  // after the functions that draw tab bars (extend through SBHooks: js/core/hooks.js)
  const DRAWS = ['switchSubjectTab', 'switchMathTab', 'openSubjectWorkspace', 'openMathView', 'selectMathChapter', 'selectSubjectChapter', 'switchScienceLessonSubTab',
    'switchLangLessonSubTab', 'switchMathTopicSubTab', 'switchChemTab', 'switchBioTab', 'switchPhysTab', 'switchEngTab', 'switchUrduTab', 'switchIslTab'];
  function hook() {
    if (!win.SBHooks) return;
    DRAWS.forEach(name => {
      if (typeof win[name] !== 'function') return;
      win.SBHooks.use(name, next => function () { const r = next.apply(this, arguments); try { enhance(); } catch (e) { /* never break navigation */ } return r; }, { id: 'a11y.js' });
    });
  }

  function init() {
    if (!doc) return;
    doc.addEventListener('keydown', onKey);
    doc.addEventListener('click', onClick);
    doc.addEventListener('focusin', onFocusIn);
    hook();
    enhance();
  }
  if (win === (typeof self !== 'undefined' ? self : null) && doc) init();
  return { enhance, trap, init, hook };
});
