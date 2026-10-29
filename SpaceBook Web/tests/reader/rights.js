'use strict';
/* The rights notice and the reader's copy guard (js/sb_rights.js) in a real browser (the installed Chrome through Playwright):
 *     SB_PAGE=lazy.html node --max-old-space-size=4096 tests/reader/rights.js
 * Notice: the owner's words exactly (written out below, apart from the source), shown once per book on a device, accessible, usable on a screen as small as a phone on its side,
 *         says nothing about permission or endorsement by anybody. Guard: Ctrl+C, Select All + Ctrl+C, cut and dragging do not export book text, typing fields still copy,
 *         the text stays selectable and the sentence translation still works. Dev-only, never shipped. */
const { serve, launch } = require('../baseline/lib');

let pass = 0, fail = 0;
const check = (name, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + name); } else { fail++; console.log('FAIL  ' + name + (detail !== undefined ? '  -> ' + String(JSON.stringify(detail)).slice(0, 300) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

const WORDS = 'SpaceBook provides an interactive learning environment designed to make education easier and more accessible. Rights in the original textbooks, text, illustrations, and other source materials remain with their respective owners. SpaceBook does not claim ownership of those materials. Subscription charges support the platform’s development, hosting, interactive features, and maintenance; they do not transfer ownership of textbook content or grant reproduction rights. Users may use content only as permitted by applicable law and the relevant licence. Unauthorized copying, redistribution, republication, or commercial reuse is prohibited. For attribution concerns, permission requests, or removal requests, please contact SpaceBook through its support channel.';

(async () => {
  const { server, url } = await serve(0);
  const browser = await launch();
  const errors = [];

  async function open(width, height, noticeTest) {
    const ctx = await browser.newContext({ viewport: { width, height }, permissions: ['clipboard-read', 'clipboard-write'] });
    const page = await ctx.newPage();
    page.on('pageerror', e => errors.push(e.message));
    if (noticeTest) await page.addInitScript(() => { window.SB_RIGHTS_TEST = true; });
    await page.goto(url + (process.env.SB_PAGE || 'lazy.html'), { waitUntil: 'domcontentloaded', timeout: 180000 });
    for (let k = 0; k < 4; k++) {
      try { await page.waitForFunction(() => typeof openSubject === 'function' && typeof renderHome === 'function' && window.SBRights, null, { timeout: 120000 }); await sleep(2500); break; } catch (e) { /* the first load may reload itself once */ }
    }
    return { ctx, page };
  }
  const dialog = page => page.evaluate(() => {
    const d = document.querySelector('#sbRightsNotice .sbrt-dialog'); if (!d) return null;
    const r = d.getBoundingClientRect();
    return { text: d.querySelector('p').textContent, title: d.querySelector('h2').textContent, role: d.getAttribute('role'), modal: d.getAttribute('aria-modal'), labelled: !!document.getElementById(d.getAttribute('aria-labelledby')), described: !!document.getElementById(d.getAttribute('aria-describedby')),
      focusInside: d.contains(document.activeElement), inertSiblings: [...document.body.children].filter(c => c.id !== 'sbRightsNotice' && c.hasAttribute('inert')).length, h: Math.round(r.height), buttons: [...d.querySelectorAll('button')].map(b => b.textContent) };
  });

  // ---------- the notice
  let { ctx, page } = await open(1366, 768, true);
  check('the notice is not shown before a book is opened', await dialog(page) === null);
  await page.evaluate(() => { goToSubjects('cls5'); openSubject('cls5', 'cls5-math'); }); await sleep(1200);
  let d = await dialog(page);
  check('opening a book shows the notice', !!d);
  check('the notice has the owner\'s words, exactly', d && d.text === WORDS, d && d.text);
  check('it is a modal dialog with a title and a description, focus inside, the page behind inert', d && d.role === 'dialog' && d.modal === 'true' && d.labelled && d.described && d.focusInside && d.inertSiblings >= 1, d);
  check('it offers "I understand" and a way to contact support', d && d.buttons.join('|') === 'I understand|Contact support', d && d.buttons);
  check('it says nothing about permission, approval or endorsement by anybody', !/endors|approved|government|authori[sz]ed by|with the permission|licensed to/i.test(d ? d.text : 'x'), d && d.text);
  let stays = true;
  for (let k = 0; k < 4; k++) { await page.keyboard.press('Tab'); if (!(await page.evaluate(() => document.querySelector('#sbRightsNotice').contains(document.activeElement)))) stays = false; }
  check('Tab stays inside the notice', stays);
  await page.click('#sbRightsNotice .sbrt-ok'); await sleep(400);
  check('"I understand" closes it and the page is usable again', (await dialog(page)) === null && await page.evaluate(() => document.querySelectorAll('[inert]').length === 0));
  await page.evaluate(() => { openSubject('cls5', 'cls5-math'); }); await sleep(800);
  check('the same book does not show it again', await dialog(page) === null);
  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof openSubject === 'function' && window.SBRights, null, { timeout: 120000 }); await sleep(2500);
  await page.evaluate(() => { openSubject('cls5', 'cls5-math'); }); await sleep(800);
  check('and not after the page is loaded again (it is kept on the device)', await dialog(page) === null);
  await page.evaluate(() => { goToSubjects('cls5'); openSubject('cls5', 'cls5-sci'); }); await sleep(1200);
  check('another book shows it once more', (await dialog(page)) !== null);
  await page.keyboard.press('Escape'); await sleep(300);
  check('Esc closes it and counts as seen', (await dialog(page)) === null && await page.evaluate(() => SBRights.seen('cls5:cls5-sci')));
  await page.evaluate(() => { SBRights.reset(); openSubject('cls6', 'cls6-eng'); }); await sleep(1200);
  await page.click('#sbRightsNotice .sbrt-help'); await sleep(900);
  check('"Contact support" closes the notice and opens the website\'s report dialog', (await dialog(page)) === null && await page.evaluate(() => { const o = document.querySelector('.sbfb-overlay'); return !!o && !o.hidden; }));
  await ctx.close();

  // a phone on its side (943 x 311 CSS px, like the owner's phone): the notice must stay usable
  ({ ctx, page } = await open(943, 311, true));
  await page.evaluate(() => { goToSubjects('cls5'); openSubject('cls5', 'cls5-math'); }); await sleep(1200);
  const land = await page.evaluate(() => {
    const dlg = document.querySelector('#sbRightsNotice .sbrt-dialog'), ok = dlg.querySelector('.sbrt-ok');
    dlg.scrollTop = dlg.scrollHeight; const b = ok.getBoundingClientRect(), r = dlg.getBoundingClientRect();
    return { dialogH: Math.round(r.height), maxH: getComputedStyle(dlg).maxHeight, okVisible: b.top >= r.top - 1 && b.bottom <= r.bottom + 1 && b.height >= 40, viewportH: innerHeight };
  });
  check('on a screen 311 px high the notice is not collapsed and its button can be reached', land.dialogH > 150 && land.okVisible, land);
  await ctx.close();

  // the notice is not shown to the app's hidden reminder page, nor to automated runs unless a test asks
  ({ ctx, page } = await open(1366, 768, false));
  await page.evaluate(() => { goToSubjects('cls5'); openSubject('cls5', 'cls5-math'); }); await sleep(1000);
  check('automated runs skip the notice (so the other suites can click)', await dialog(page) === null);
  await ctx.close();
  ({ ctx, page } = await open(1366, 768, true));
  await page.evaluate(() => { window.SB_BACKGROUND_READ = true; goToSubjects('cls5'); openSubject('cls5', 'cls5-math'); }); await sleep(1000);
  check('the app\'s hidden page that reads the study plans never shows it', await dialog(page) === null);
  await ctx.close();

  // ---------- the guard, on a real chapter of Class 11 English
  ({ ctx, page } = await open(1366, 768, false));
  await page.evaluate(() => { openSubject('cls11', 'cls11-eng'); selectSubjectChapter('eng', 1, 'cls11'); }); await sleep(5000);
  const sel = await page.evaluate(() => {
    const s = [...document.querySelectorAll('.bk-page .m6-s')].find(e => (e.textContent || '').trim().length > 60);
    if (!s) return null;
    const r = document.createRange(); r.selectNodeContents(s); const g = getSelection(); g.removeAllRanges(); g.addRange(r);
    return { len: g.toString().length, userSelect: getComputedStyle(s).userSelect, page: !!document.querySelector('.bk-page') };
  });
  check('book text can be selected (selection is what the learning tools use)', !!sel && sel.len > 40 && sel.userSelect !== 'none', sel);
  await page.evaluate(() => navigator.clipboard.writeText('SENTINEL'));
  await page.keyboard.press('Control+C'); await sleep(300);
  check('Ctrl+C on selected book text leaves the clipboard as it was', await page.evaluate(() => navigator.clipboard.readText()) === 'SENTINEL');
  await page.evaluate(() => { const s = [...document.querySelectorAll('.bk-page .m6-s')].find(e => (e.textContent || '').trim().length > 60); const r = document.createRange(); r.selectNodeContents(s); const g = getSelection(); g.removeAllRanges(); g.addRange(r); });
  await page.keyboard.press('Control+X'); await sleep(300);
  check('Ctrl+X does not export it either', await page.evaluate(() => navigator.clipboard.readText()) === 'SENTINEL');
  await page.evaluate(() => { getSelection().removeAllRanges(); document.body.focus(); });
  await page.keyboard.press('Control+A'); await page.keyboard.press('Control+C'); await sleep(300);
  check('Select All then Ctrl+C does not export the book (the selection reaches it)', await page.evaluate(() => navigator.clipboard.readText()) === 'SENTINEL');
  const toast = await page.evaluate(() => { const t = document.querySelector('.sbrt-toast'); return t ? { on: t.classList.contains('sbrt-on'), text: t.textContent, live: t.getAttribute('aria-live'), role: t.getAttribute('role') } : null; });
  check('the person is told why, politely, in a status message', !!toast && toast.on && /Copying book text is turned off/.test(toast.text) && toast.role === 'status', toast);
  const typing = await page.evaluate(async () => {
    const t = document.createElement('textarea'); t.value = 'my own note'; document.body.appendChild(t); t.focus(); t.select();
    return new Promise(res => setTimeout(() => res(true), 50));
  });
  await page.keyboard.press('Control+C'); await sleep(300);
  check('typing fields keep copy (a note, the search box, the report form)', typing && await page.evaluate(() => navigator.clipboard.readText()) === 'my own note');
  const drag = await page.evaluate(() => {
    const ev = () => new DragEvent('dragstart', { bubbles: true, cancelable: true });
    const s = [...document.querySelectorAll('.bk-page .m6-s')].find(e => (e.textContent || '').trim().length > 20);
    const a = ev(); s.dispatchEvent(a);
    const img = document.createElement('img'); img.src = 'data:image/gif;base64,R0lGODlhAQABAAAAACw='; s.closest('.bk-page').appendChild(img);
    const b = ev(); img.dispatchEvent(b);
    const w = document.createElement('div'); w.setAttribute('draggable', 'true'); w.textContent = 'drag me'; s.closest('.bk-page').appendChild(w);
    const c = ev(); w.dispatchEvent(c);
    return { text: a.defaultPrevented, picture: b.defaultPrevented, exerciseWidget: c.defaultPrevented };
  });
  check('dragging book text or a book picture out is prevented, a widget that is dragged on purpose still works', drag.text && drag.picture && !drag.exerciseWidget, drag);
  const menu = await page.evaluate(() => {
    const send = (el, type) => { const ev = new PointerEvent('contextmenu', { bubbles: true, cancelable: true, pointerType: type }); el.dispatchEvent(ev); return ev.defaultPrevented; };
    const s = [...document.querySelectorAll('.bk-page .m6-s')].find(e => (e.textContent || '').trim().length > 20);
    const t = document.createElement('textarea'); document.body.appendChild(t);
    return { mouseOnBook: send(s, 'mouse'), touchOnBook: send(s, 'touch'), mouseInTextBox: send(t, 'mouse') };
  });
  check('the browser\'s right-click menu (Copy, Ask Gemini, Search Google) is not opened over book text, but a long press on a touch screen and a text box keep theirs', menu.mouseOnBook && !menu.touchOnBook && !menu.mouseInTextBox, menu);
  await page.evaluate(() => { getSelection().removeAllRanges(); });
  const sent = await page.evaluate(() => { const e = [...document.querySelectorAll('.bk-page .m6-s')].find(x => { const b = x.getBoundingClientRect(); return b.width > 80 && b.top > 150 && b.bottom < 700; }); if (!e) return null; e.scrollIntoView({ block: 'center' }); const b = e.getBoundingClientRect(); return { x: b.left + 30, y: b.top + b.height / 2 }; });
  if (sent) await page.mouse.click(sent.x, sent.y);
  await sleep(1200);
  check('clicking a sentence still shows its translation', await page.evaluate(() => [...document.querySelectorAll('.m6-tr')].some(e => !e.hidden && e.getBoundingClientRect().height > 8)));
  const a11y = await page.evaluate(() => ({ hidden: !!document.querySelector('.bk-page:not(.bk-blank)[aria-hidden="true"], #subjTabContent[aria-hidden="true"]'), inert: document.querySelectorAll('[inert]').length, noSelectRule: [...document.styleSheets].some(s => { try { return [...s.cssRules].some(r => /sbrt|bk-page/.test(r.selectorText || '') && /user-select\s*:\s*none/.test(r.cssText)); } catch (e) { return false; } }) }));
  check('nothing was hidden from screen readers or made unselectable by the guard', !a11y.hidden && a11y.inert === 0 && !a11y.noSelectRule, a11y);
  await ctx.close();

  check('nothing threw in the console', errors.length === 0, errors.slice(0, 3));
  await browser.close(); server.close();
  console.log('rights notice and guard tests: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
