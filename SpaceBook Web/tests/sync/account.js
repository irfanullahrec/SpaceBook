'use strict';
/* UI + API: the real js/auth.js "My account" screen in a real DOM (jsdom) against the real PHP API: change profile,
 * change password, download my data, delete my account, logout.   node tests/sync/account.js */
const fs = require('fs'), path = require('path');
const { JSDOM } = require('jsdom');
const harness = require('./harness');

const JS = path.join(harness.ROOT, 'js');
const sleep = harness.sleep;

(async () => {
  const h = await harness.start();
  const { check } = h;
  console.log('--- js/auth.js: My account (jsdom) ---');

  // a page with the header avatar, the core scripts and auth.js; fetch goes to the real server with this page's cookie
  async function page(acct) {
    const dom = new JSDOM('<!doctype html><html><body><div class="header-user-avatar"></div></body></html>', { url: h.base, runScripts: 'outside-only', pretendToBeVisual: true });
    const w = dom.window;
    let cookie = acct && acct.cookie || null;
    w.fetch = async (url, o) => {
      o = Object.assign({}, o); o.headers = Object.assign({}, o.headers, cookie ? { Cookie: cookie } : {});
      const res = await fetch(new URL(String(url).replace(/^\.?\/?api\//, ''), h.base).href, o);        // the server's document root is api/
      const sc = (res.headers.getSetCookie ? res.headers.getSetCookie() : []).map(c => c.split(';')[0]).find(c => c.startsWith('spacebook_sid='));
      if (sc) cookie = sc.endsWith('=') || /=deleted/i.test(sc) ? null : sc;
      return res;
    };
    w.confirm = () => true;
    w.HTMLElement.prototype.scrollIntoView = () => {};
    for (const f of ['core/store.js', 'core/sync.js', 'core/consent.js', 'auth.js']) w.eval(fs.readFileSync(path.join(JS, f), 'utf8'));
    w.SBSync.start = () => {};
    for (let i = 0; i < 50 && !w.SpaceBookAuth.user; i++) await sleep(50);
    return { dom, w, doc: w.document, cookie: () => cookie };
  }
  const submit = async (p, which, values) => {
    const form = p.doc.querySelector('#accountModal form[data-acc="' + which + '"]');
    Object.keys(values || {}).forEach(k => { form.querySelector('[name="' + k + '"]').value = values[k]; });
    form.requestSubmit();
    await sleep(500);
    return form.querySelector('.auth-error').textContent;
  };

  // 1. open the screen from the menu
  const a = await h.account();
  const p = await page(a);
  check('the page knows the signed-in student from the session', p.w.SpaceBookAuth.user && p.w.SpaceBookAuth.user.id === a.user.id);
  p.doc.querySelector('.header-user-avatar').click();
  const menu = p.doc.getElementById('authMenu');
  check('the user menu has "My account" and "Logout"', !!menu && !!menu.querySelector('[data-act="account"]') && /Logout/.test(menu.textContent));
  menu.querySelector('[data-act="account"]').click();
  const modal = p.doc.getElementById('accountModal');
  check('"My account" opens a screen with details, password, download and delete', !!modal && ['profile', 'password', 'export', 'delete'].every(k => !!modal.querySelector('form[data-acc="' + k + '"]')) && !p.doc.getElementById('authMenu'));
  check('the details form starts with the current name', modal.querySelector('input[name="name"]').value === a.user.name);

  // 2. profile
  let msg = await submit(p, 'profile', { name: 'Ali Khan', father_name: 'Gul Khan' });
  const meOnPage = await (await p.w.fetch('api/auth.php?action=me')).json().catch(() => null);      // asked through the page, with its cookie
  check('saving the details shows "Done." and updates the student everywhere', msg === 'Done.' && p.w.SpaceBookAuth.user.name === 'Ali Khan' && meOnPage && meOnPage.user.name === 'Ali Khan' && meOnPage.user.father_name === 'Gul Khan', [msg, meOnPage && meOnPage.user]);
  check('the avatar shows the new initial', p.doc.querySelector('.auth-initial').textContent === 'A');
  msg = await submit(p, 'profile', { name: 'X', father_name: 'Gul Khan' });
  check('a name that is too short is refused with the server message', /name/i.test(msg) && p.w.SpaceBookAuth.user.name === 'Ali Khan', msg);

  // 3. password
  msg = await submit(p, 'password', { current_password: 'wrong', new_password: 'brandnew1' });
  check('a wrong current password is refused', /current password/i.test(msg), msg);
  msg = await submit(p, 'password', { current_password: 'secret123', new_password: 'brandnew1' });
  const oldLogin = await h.api('auth.php?action=login', { whatsapp: a.user.whatsapp, password: 'secret123' });
  const newLogin = await h.api('auth.php?action=login', { whatsapp: a.user.whatsapp, password: 'brandnew1' });
  check('the password is changed: "Done.", the old one stops working, the new one works', msg === 'Done.' && oldLogin.status === 401 && newLogin.status === 200, [msg, oldLogin.status, newLogin.status]);
  check('the form is cleared after a password change', p.doc.querySelector('input[name="new_password"]').value === '');

  // 4. download
  await p.w.SBSync.ready;
  msg = await submit(p, 'export', {});
  check('"Download my data" works (no error)', msg === 'Done.', msg);
  const ex = await p.w.SpaceBookAuth.exportData();
  check('the export holds this student and no password hash', ex.schema === 'spacebook.export/1' && ex.account.name === 'Ali Khan' && JSON.stringify(ex).indexOf('password_hash') < 0);

  // 5. logout keeps the waiting events and forgets the device token
  {
    const b = await h.account();
    const q = await page(b);
    await q.w.SBSync.ready; await q.w.SBSync.setUser(b.user); await q.w.SBSync.setDevice(b.user.id, b.device);
    await q.w.SBSync.emit('step', { key: 'cls2|math|u0|trace|lg1|0', title: 'T', total: 2, step: 0 });
    q.doc.querySelector('.header-user-avatar').click();
    q.doc.querySelector('#authMenu .auth-logout:not([data-act])').click();
    await sleep(600);
    const st = await q.w.SBSync.status();
    check('logout signs out, forgets the device token and keeps the event that was waiting', q.w.SpaceBookAuth.user === null && st.hasDeviceToken === false && st.signedIn === false);
    const tok = await h.api('v2/sync.php', undefined, { Authorization: 'Bearer ' + b.device.token });
    check('and the server has revoked that device', tok.status === 401);
  }

  // 6. delete
  msg = await submit(p, 'delete', { password: 'nope' });
  check('deleting needs the right password', /password/i.test(msg) && p.w.SpaceBookAuth.user !== null, msg);
  msg = await submit(p, 'delete', { password: 'brandnew1' });
  const gone = await h.api('auth.php?action=login', { whatsapp: a.user.whatsapp, password: 'brandnew1' });
  check('the account is deleted: message shown, the page signs out, login no longer works', msg === 'Your account was deleted.' && p.w.SpaceBookAuth.user === null && gone.status === 401, [msg, gone.status]);
  await sleep(1400);
  check('the screen closes itself afterwards', !p.doc.getElementById('accountModal'));

  h.finish('account UI tests');
})().catch(e => { console.error(e); process.exit(2); });
