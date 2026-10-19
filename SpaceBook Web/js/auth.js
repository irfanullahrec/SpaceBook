// ─── ACCOUNTS: login / create account modal (talks to api/auth.php) ───
(function () {
  const API = 'api/auth.php';
  const TYPES = [['student', 'Student'], ['teacher', 'Teacher'], ['school', 'School']];
  let currentUser = null;

  async function call(action, body, extraHeaders) {
    const opts = { credentials: 'same-origin', headers: Object.assign({}, extraHeaders || {}) };
    if (body !== undefined) {
      opts.method = 'POST';
      opts.headers['Content-Type'] = 'application/json';
      opts.body = JSON.stringify(body);
    }
    let res;
    try {
      res = await fetch(`${API}?action=${action}`, opts);
    } catch (e) {
      return { ok: false, error: 'Cannot reach server. Check your connection.' };
    }
    try {
      return await res.json();
    } catch (e) {
      return { ok: false, error: 'Server error (is PHP running?)' };
    }
  }

  function deviceName() {
    const ua = (typeof navigator !== 'undefined' && navigator.userAgent) || '';
    return ua.replace(/\s+/g, ' ').slice(0, 60);
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  }

  function buildModal() {
    const wrap = document.createElement('div');
    wrap.id = 'authModal';
    wrap.className = 'auth-backdrop';
    wrap.hidden = true;
    wrap.innerHTML = `
      <div class="auth-card" role="dialog" aria-modal="true" aria-labelledby="authTitle">
        <button class="auth-close" type="button" aria-label="Close">✕</button>
        <h2 id="authTitle">Welcome to TuitionHub</h2>
        <div class="auth-tabs" role="tablist">
          <button type="button" data-tab="login" class="active">Login</button>
          <button type="button" data-tab="register">Create Account</button>
        </div>

        <form class="auth-form" data-form="login" novalidate>
          <label>WhatsApp Number
            <input name="whatsapp" type="tel" inputmode="tel" autocomplete="tel" placeholder="03XX XXXXXXX" required>
          </label>
          <label>Password
            <input name="password" type="password" autocomplete="current-password" required>
          </label>
          <p class="auth-error" aria-live="polite"></p>
          <button class="auth-submit" type="submit">Login</button>
        </form>

        <form class="auth-form" data-form="register" novalidate hidden>
          <label>Name
            <input name="name" type="text" autocomplete="name" maxlength="100" required>
          </label>
          <label>Father Name
            <input name="father_name" type="text" maxlength="100" required>
          </label>
          <fieldset class="auth-types">
            <legend>User Type</legend>
            ${TYPES.map(([v, l], i) => `
              <label class="auth-type"><input type="radio" name="user_type" value="${v}" ${i === 0 ? 'checked' : ''}><span>${l}</span></label>`).join('')}
          </fieldset>
          <label>WhatsApp Number
            <input name="whatsapp" type="tel" inputmode="tel" autocomplete="tel" placeholder="03XX XXXXXXX" required>
          </label>
          <label>Password
            <input name="password" type="password" autocomplete="new-password" minlength="6" required>
          </label>
          <p class="auth-error" aria-live="polite"></p>
          <button class="auth-submit" type="submit">Create Account</button>
        </form>
      </div>`;
    document.body.appendChild(wrap);

    wrap.addEventListener('click', e => { if (e.target === wrap) close(); });
    wrap.querySelector('.auth-close').addEventListener('click', close);
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !wrap.hidden) close(); });
    wrap.querySelectorAll('.auth-tabs button').forEach(b =>
      b.addEventListener('click', () => showTab(b.dataset.tab)));

    wrap.querySelectorAll('.auth-form').forEach(form => {
      form.addEventListener('submit', async e => {
        e.preventDefault();
        const err = form.querySelector('.auth-error');
        const btn = form.querySelector('.auth-submit');
        const data = Object.fromEntries(new FormData(form).entries());
        err.textContent = '';
        btn.disabled = true;
        // ask for a device token: offline-safe sync (js/core/sync.js) uses it instead of the cookie
        const r = await call(form.dataset.form, Object.assign({ want_device: true, device_name: deviceName() }, data));
        btn.disabled = false;
        if (!r.ok) { err.textContent = r.error || 'Something went wrong'; return; }
        if (r.device && window.SBSync) { try { await window.SBSync.setDevice(r.user.id, r.device); } catch (e) { /* sync falls back to the cookie */ } }
        setUser(r.user);
        form.reset();
        close();
      });
    });
    return wrap;
  }

  function modal() { return document.getElementById('authModal') || buildModal(); }

  function showTab(tab) {
    const m = modal();
    m.querySelectorAll('.auth-tabs button').forEach(b => b.classList.toggle('active', b.dataset.tab === tab));
    m.querySelectorAll('.auth-form').forEach(f => { f.hidden = f.dataset.form !== tab; });
    const first = m.querySelector(`.auth-form[data-form="${tab}"] input`);
    if (first) first.focus();
  }

  function open(tab) {
    modal().hidden = false;
    showTab(tab || 'login');
  }

  function close() { modal().hidden = true; }

  function closeMenu() {
    const menu = document.getElementById('authMenu');
    if (menu) menu.remove();
  }

  function showMenu(anchor) {
    if (document.getElementById('authMenu')) { closeMenu(); return; }
    const u = currentUser;
    const type = (TYPES.find(t => t[0] === u.user_type) || [, u.user_type])[1];
    const menu = document.createElement('div');
    menu.id = 'authMenu';
    menu.className = 'auth-menu';
    menu.innerHTML = `
      <div class="auth-menu-name">${esc(u.name)}</div>
      <div class="auth-menu-meta">${esc(type)} · +${esc(u.whatsapp)}</div>
      <button type="button" class="auth-logout">Logout</button>`;
    anchor.appendChild(menu);
    menu.addEventListener('click', e => e.stopPropagation());
    menu.querySelector('.auth-logout').addEventListener('click', async () => {
      const uid = currentUser && currentUser.id;
      await call('logout', {}, window.SBSync ? window.SBSync.bearerHeaders() : {});   // the device token ends with the logout
      if (window.SBSync && uid != null) { try { await window.SBSync.clearDevice(uid); } catch (e) { /* fine */ } }   // events waiting to be sent stay on the device
      setUser(null);
      closeMenu();
    });
    setTimeout(() => document.addEventListener('click', closeMenu, { once: true }));
  }

  function setUser(u) {
    currentUser = u || null;
    const avatar = document.querySelector('.header-user-avatar');
    if (avatar) {
      avatar.classList.toggle('auth-signed-in', !!currentUser);
      avatar.title = currentUser ? currentUser.name : 'Login / Create Account';
      let badge = avatar.querySelector('.auth-initial');
      if (currentUser) {
        if (!badge) { badge = document.createElement('span'); badge.className = 'auth-initial'; avatar.appendChild(badge); }
        badge.textContent = currentUser.name.trim().charAt(0).toUpperCase();
      } else if (badge) {
        badge.remove();
      }
    }
    document.dispatchEvent(new CustomEvent('spacebook:auth', { detail: { user: currentUser } }));
  }

  function init() {
    const avatar = document.querySelector('.header-user-avatar');
    if (avatar) {
      avatar.setAttribute('role', 'button');
      avatar.tabIndex = 0;
      const activate = () => (currentUser ? showMenu(avatar) : open('login'));
      avatar.addEventListener('click', e => { e.stopPropagation(); activate(); });
      avatar.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); } });
    }
    call('me').then(r => setUser(r.ok ? r.user : null));
  }

  window.SpaceBookAuth = {
    open, close,
    get user() { return currentUser; },
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
