'use strict';
/* Tab bars and dialogs: roles, selected state, roving tabindex, arrow keys, focus trap (js/core/a11y.js) in a real DOM (jsdom).
 *   node --max-old-space-size=8192 tests/a11y/tabs.js */
const { loadDom } = require('../../tools/lib/app_dom');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

(async () => {
  const app = await loadDom({ page: 'lazy.html' });
  const w = app.win, d = w.document;
  const r = c => { try { return app.run(c); } catch (e) { return 'ERR ' + e.message.slice(0, 120); } };
  check('the page has SBA11y', typeof w.SBA11y === 'object');
  r("openSubject('cls9', 'cls9-bio')"); await app.settle();
  r("selectSubjectChapter('bio', 0, 'cls9')"); await app.settle();
  const bar = d.querySelector('.math-nav-tabs');
  check('the chapter has a tab bar', !!bar);
  const TABSEL = 'button[class*="tab-btn"]:not([hidden]):not(.ws-subj-tab), button[class*="top-tab"]:not([hidden]):not(.ws-subj-tab)';
  const tabs = [...bar.querySelectorAll(TABSEL)];
  check('the bar is a tablist and every button a tab', bar.getAttribute('role') === 'tablist' && tabs.length >= 2 && tabs.every(t => t.getAttribute('role') === 'tab'), tabs.length + ' tabs');
  const selected = tabs.filter(t => t.getAttribute('aria-selected') === 'true');
  check('the Word Stats button in the bar is a tab that is never "selected"', (() => { const ws = d.querySelector('.ws-subj-tab'); return !ws || (ws.getAttribute('role') === 'tab' && ws.getAttribute('aria-selected') === 'false'); })());
  check('exactly one tab is selected and it is the active one', selected.length === 1 && selected[0].classList.contains('active'));
  check('only the selected tab is in the Tab order (roving tabindex)', tabs.filter(t => t.tabIndex === 0).length === 1 && tabs.filter(t => t.tabIndex === -1).length === tabs.length - 1);

  // arrow keys open the next tab
  const first = selected[0], idx = tabs.indexOf(first);
  first.focus();
  first.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true, cancelable: true }));
  await app.settle();
  const bar2 = d.querySelector('.math-nav-tabs'), tabs2 = [...bar2.querySelectorAll(TABSEL)];
  const sel2 = tabs2.filter(t => t.getAttribute('aria-selected') === 'true');
  check('ArrowRight opens the next tab and moves the selection', sel2.length === 1 && tabs2.indexOf(sel2[0]) === (idx + 1) % tabs2.length && sel2[0].classList.contains('active'), 'was ' + idx + ' now ' + tabs2.indexOf(sel2[0]));
  check('and the focus follows', d.activeElement === sel2[0]);
  sel2[0].dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Home', bubbles: true, cancelable: true }));
  await app.settle();
  const sel3 = [...d.querySelectorAll('.math-nav-tabs ' + TABSEL)].filter(t => t.getAttribute('aria-selected') === 'true');
  check('Home goes to the first tab', sel3.length === 1 && [...d.querySelectorAll('.math-nav-tabs ' + TABSEL)].indexOf(sel3[0]) === 0);
  const lastBtn = [...d.querySelectorAll('.math-nav-tabs ' + TABSEL)].pop();
  sel3[0].dispatchEvent(new w.KeyboardEvent('keydown', { key: 'End', bubbles: true, cancelable: true }));
  await app.settle();
  check('End goes to the last tab', [...d.querySelectorAll('.math-nav-tabs ' + TABSEL)].filter(t => t.getAttribute('aria-selected') === 'true')[0] === [...d.querySelectorAll('.math-nav-tabs ' + TABSEL)].pop());

  // a click moves the selection too
  const second = [...d.querySelectorAll('.math-nav-tabs ' + TABSEL)][1];
  second.click(); await app.settle();
  const after = [...d.querySelectorAll('.math-nav-tabs ' + TABSEL)].filter(t => t.getAttribute('aria-selected') === 'true');
  check('a mouse click moves the selection and the tab stop', after.length === 1 && after[0].tabIndex === 0);

  // dialog trap
  const dlg = d.createElement('div');
  dlg.innerHTML = '<button id="a">A</button><button id="b">B</button><button id="c">C</button>';
  d.body.appendChild(dlg);
  const opener = d.createElement('button'); opener.id = 'opener'; d.body.appendChild(opener); opener.focus();
  let closed = 0;
  const release = w.SBA11y.trap(dlg, { onClose: () => { closed++; } });
  check('the dialog takes the focus', dlg.contains(d.activeElement) && d.activeElement.id === 'a');
  d.getElementById('c').focus();
  d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Tab', bubbles: true, cancelable: true }));
  check('Tab on the last control goes to the first (the focus stays inside)', d.activeElement.id === 'a', d.activeElement.id);
  d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Tab', shiftKey: true, bubbles: true, cancelable: true }));
  check('Shift+Tab on the first control goes to the last', d.activeElement.id === 'c', d.activeElement.id);
  d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Escape', bubbles: true, cancelable: true }));
  check('Escape asks the dialog to close', closed === 1);
  release();
  check('releasing returns the focus to where it was', d.activeElement.id === 'opener', d.activeElement.id);
  d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Escape', bubbles: true, cancelable: true }));
  check('after release the trap is gone', closed === 1);

  // controls the keyboard cannot reach (hidden form, closed <details>) are not the "last" control
  const dlg2 = d.createElement('div');
  dlg2.innerHTML = '<button id="p">P</button><details><summary id="s">S</summary><input id="inner"></details><form hidden><input id="gone"></form><button id="q">Q</button><div aria-hidden="true"><button id="ah">x</button></div>';
  d.body.appendChild(dlg2); opener.focus();
  const release2 = w.SBA11y.trap(dlg2, { onClose: () => {} });
  d.getElementById('q').focus();
  d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Tab', bubbles: true, cancelable: true }));
  check('a hidden form or aria-hidden branch after the last control does not break the wrap', d.activeElement.id === 'p', d.activeElement.id);
  d.getElementById('p').focus();
  d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Tab', shiftKey: true, bubbles: true, cancelable: true }));
  check('Shift+Tab from the first control lands on the last reachable one', d.activeElement.id === 'q', d.activeElement.id);
  release2();
  const dlg3 = d.createElement('div');
  dlg3.innerHTML = '<button id="x1">1</button><details><summary id="x2">2</summary><input id="x3"></details>';
  d.body.appendChild(dlg3);
  const release3 = w.SBA11y.trap(dlg3, { onClose: () => {} });
  d.getElementById('x2').focus();
  d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Tab', bubbles: true, cancelable: true }));
  check('the summary of a closed <details> is the last reachable control (its field is not)', d.activeElement.id === 'x1', d.activeElement.id);
  dlg3.querySelector('details').open = true;
  d.getElementById('x3').focus();
  d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Tab', bubbles: true, cancelable: true }));
  check('once the <details> is open its field is the last control', d.activeElement.id === 'x1', d.activeElement.id);
  release3(); dlg3.remove();
  dlg2.remove(); dlg.remove();

  // the real dialogs use it
  const key = k => d.dispatchEvent(new w.KeyboardEvent('keydown', { key: k, bubbles: true, cancelable: true }));
  const trigger = d.createElement('button'); trigger.id = 'trigger'; d.body.appendChild(trigger); trigger.focus();
  w.SpaceBookAuth.open('login');
  const authModal = d.getElementById('authModal');
  check('the sign-in dialog takes the focus', !!authModal && !authModal.hidden && authModal.contains(d.activeElement), d.activeElement && d.activeElement.tagName);
  const authFocusables = [...authModal.querySelectorAll('input, button')].filter(el => !el.closest('[hidden]'));
  authFocusables[authFocusables.length - 1].focus();
  key('Tab');
  check('Tab on the last control of the sign-in dialog stays in the dialog', authModal.contains(d.activeElement));
  const authTabs = [...authModal.querySelectorAll('.auth-tabs > button')];
  check('the sign-in tabs are tabs with one selected', authTabs.length === 2 && authTabs.every(t => t.getAttribute('role') === 'tab') && authTabs.filter(t => t.getAttribute('aria-selected') === 'true').length === 1);
  authTabs[0].focus(); authTabs[0].dispatchEvent(new w.KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true, cancelable: true }));
  check('ArrowRight on "Login" opens "Create Account" and the selection follows', authTabs[1].getAttribute('aria-selected') === 'true' && authTabs[0].getAttribute('aria-selected') === 'false' && !authModal.querySelector('.auth-form[data-form="register"]').hidden);
  key('Escape');
  check('Escape closes the sign-in dialog and the focus returns to what opened it', authModal.hidden && d.activeElement === trigger, d.activeElement && (d.activeElement.id || d.activeElement.tagName));

  if (w.SBOffline && typeof w.SBOffline.openPanel === 'function') {
    trigger.focus();
    const p = w.SBOffline.openPanel();                         // the list loads in the background; the trap is set at once
    const ov = d.querySelector('.sb-off-overlay');
    check('the offline books dialog takes the focus', !!ov && ov.contains(d.activeElement), d.activeElement && d.activeElement.tagName);
    key('Escape');
    check('Escape closes the offline books dialog and the focus returns to the opener', !d.querySelector('.sb-off-overlay') && d.activeElement === trigger);
    try { await p; } catch (e) { /* the map is not served in this test */ }
  }

  // things that are clicked but are not buttons
  const tabKey = () => d.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Tab', bubbles: true, cancelable: true }));
  const send = (el, k, extra) => el.dispatchEvent(new w.KeyboardEvent('keydown', Object.assign({ key: k, bubbles: true, cancelable: true }, extra || {})));
  r("goToSubjects('cls9')"); await app.settle();
  const cards = [...d.querySelectorAll('.subject-card-wrapper')];
  check('the subject cards exist', cards.length >= 5, String(cards.length));
  check('before any keyboard use the cards are plain divs', cards.every(c => !c.hasAttribute('role')));
  tabKey();
  check('the first Tab press makes every subject card a button in the Tab order', cards.every(c => c.getAttribute('role') === 'button' && c.tabIndex === 0));
  let opened = null; const realOpenSubject = w.openSubject; w.openSubject = (a, b) => { opened = a + '/' + b; };
  cards[1].focus(); send(cards[1], 'Enter');
  check('Enter on a card opens that subject', opened && /^cls9\//.test(opened) && opened === (cards[1].getAttribute('onclick').match(/openSubject\('([^']+)','([^']+)'\)/) || []).slice(1, 3).join('/'), String(opened));
  opened = null; send(cards[2], ' ');
  check('Space does the same', !!opened);
  w.openSubject = realOpenSubject;
  const brand = d.querySelector('.header-brand');
  tabKey();
  check('the brand in the header is a button too', brand.getAttribute('role') === 'button' && brand.tabIndex === 0);
  check('real buttons are not given a role (the tab bars have their own)', [...d.querySelectorAll('button')].every(b => b.getAttribute('role') !== 'button'));

  r("openSubject('cls9', 'cls9-math')"); await app.settle();
  tabKey();
  const acc = d.querySelector('.math-acc-header');
  const accBtn = acc.querySelector(':scope > [data-sb-proxy]') || acc;               // the title stands in when the header holds its own controls
  check('an accordion header has a button (itself, or its title) with aria-expanded', accBtn.getAttribute('role') === 'button' && accBtn.getAttribute('aria-expanded') === 'false', accBtn.outerHTML.slice(0, 100));
  const wasOpen = acc.closest('.math-accordion-card').classList.contains('open');
  accBtn.focus(); send(accBtn, 'Enter'); await app.settle();
  check('Enter opens it and aria-expanded follows', acc.closest('.math-accordion-card').classList.contains('open') !== wasOpen && accBtn.getAttribute('aria-expanded') === (wasOpen ? 'false' : 'true'));
  check('no button contains another control (they may not nest)', [...d.querySelectorAll('[role="button"]')].every(b => !b.querySelector('button, a[href], input, select, textarea, [role="tab"], [role="button"]')), [...d.querySelectorAll('[role="button"]')].filter(b => b.querySelector('button, a[href], input, select, textarea, [role="tab"], [role="button"]')).map(b => b.className).join(','));
  send(accBtn, ' '); await app.settle();
  check('Space closes it again', acc.closest('.math-accordion-card').classList.contains('open') === wasOpen);

  r("openSubject('cls9', 'cls9-bio')"); await app.settle();
  r("selectSubjectChapter('bio', 0, 'cls9')"); await app.settle();
  const lessonTab = d.querySelector('.math-nav-tabs button[data-tab="lesson"]'); if (lessonTab) { lessonTab.click(); await app.settle(); }
  tabKey();
  const sents = [...d.querySelectorAll('.lesson-sentence:not([role])')];     // the Quran verses carry their own role and tab stop
  check('the lesson has sentences', sents.length > 20, String(sents.length));
  check('the whole text is one tab stop (not one per sentence)', sents.filter(s => s.tabIndex === 0).length === 1 && sents[0].tabIndex === 0);
  check('a sentence is not announced as a button (the text keeps reading as text)', !sents[0].hasAttribute('role'));
  sents[0].focus(); send(sents[0], 'ArrowDown');
  check('ArrowDown moves to the next sentence and makes it the tab stop', d.activeElement === sents[1] && sents[1].tabIndex === 0 && sents[0].tabIndex === -1);
  send(sents[1], 'End');
  check('End goes to the last sentence', d.activeElement === sents[sents.length - 1]);
  send(d.activeElement, 'Home'); send(d.activeElement, 'ArrowUp');
  check('ArrowUp on the first sentence stays on it', d.activeElement === sents[0]);
  let clicks = 0; sents[0].addEventListener('click', () => { clicks++; });
  send(sents[0], 'Enter');
  check('Enter on a sentence clicks it (opens its translation)', clicks === 1);
  sents[5].click();
  check('a mouse click on a sentence makes it the tab stop', sents[5].tabIndex === 0 && sents.filter(s => s.tabIndex === 0).length === 1);

  // the language and direction of what is being read (screen-reader voice)
  r("openSubject('cls9', 'cls9-urdu')"); await app.settle(); await app.settle();
  const urduAreas = [...d.querySelectorAll('.sb-rtl-medium')];
  check('an Urdu book has right-to-left reading areas that say lang="ur"', urduAreas.length > 0 && urduAreas.every(a => a.getAttribute('dir') === 'rtl') && urduAreas.some(a => a.getAttribute('lang') === 'ur'), urduAreas.map(a => a.getAttribute('lang')).join(','));
  r("openSubject('cls3', 'cls3-pashto')"); await app.settle(); await app.settle();
  check('a Pashto book says lang="ps"', [...d.querySelectorAll('.sb-rtl-medium')].some(a => a.getAttribute('lang') === 'ps'));
  r("openSubject('cls9', 'cls9-eng')"); await app.settle(); await app.settle();
  check('an English book keeps the page language (no lang on its areas, none left over from the Pashto book)', d.querySelectorAll('[data-sb-lang]').length === 0 && d.documentElement.getAttribute('lang') === 'en');

  console.log(`accessibility tests: ${passed} passed, ${failed} failed`);
  process.exit(failed ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
