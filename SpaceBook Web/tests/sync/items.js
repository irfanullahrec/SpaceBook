'use strict';
/* Integration: js/core/items.js (+ sync.js, consent.js, the word/games/BISE mirrors) against the real PHP API and MySQL.
 *   node tests/sync/items.js
 * Two "devices" are two copies of the page (app sandbox) signed in to one account; the network can be switched off per device. */
const harness = require('./harness');

const BM = (s, ch, p, tb) => ({ key: [s, ch, tb || '', p].join('|'), value: { c: 'cls5', s, ch, p, tb: tb || '', t: 'Title ' + ch } });
const settle = async (h, ...devs) => { for (const d of devs) { await d.sb.SBItems.syncNow(); } await h.sleep(120); };

(async () => {
  const h = await harness.start();
  const { check, sleep } = h;
  console.log('--- user items: two devices, one account ---');

  // 0. with the owner's switch off the items stay on the device and no request is made; turning it on sends them
  {
    const a = await h.account();
    const A = h.newApp(); await A.signIn(a);
    await A.sb.SBItems.put('bm', BM('cls5-urdu', 1, 1).key, BM('cls5-urdu', 1, 1).value);
    await sleep(100);
    check('switch off: the bookmark is kept here and nothing is sent or queued', A.sb.SBItems.list('bm').length === 1 && !A.net.log.some(r => r.url.includes('v2/sync')) && (await A.sb.SBSync.pending()) === 0, A.net.log);
    A.sb.SBSync.setServerFlags({ syncV2: true });
    await A.sb.SBItems.syncNow(); await sleep(150);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a)); await settle(h, B);
    check('switch on: the bookmark made while it was off reaches the account and a second device', B.sb.SBItems.list('bm').length === 1);
  }

  // 1. a bookmark, a note, a position and a marked word reach the second device
  {
    const a = await h.account();
    const A = h.newApp({ flag: true }); await A.signIn(a);
    const b1 = BM('cls5-math', 2, 3);
    await A.sb.SBItems.put('bm', b1.key, b1.value);
    await A.sb.SBItems.put('note', '11111111-2222-4333-8444-555555555555', { c: 'cls5', s: 'cls5-math', ch: 2, p: 3, tb: '', t: 'Fractions', x: 'Remember the common denominator', q: 'common denominator', k: 'note' });
    await A.sb.SBItems.put('pos', 'cls5-math', { c: 'cls5', ch: 2, p: 3, tb: 'Lessons', n: 9, t: 'Fractions' });
    await A.sb.SBItems.put('word', 'en:fraction', { s: 'l' });
    await settle(h, A);
    check('with the switch on the items go out', A.sb.SBSync.isEnabled() && (await A.sb.SBSync.pending()) === 0, await A.sb.SBSync.status());
    const B = h.newApp({ flag: true });
    const seen = [];
    B.sb.SBItems.on('change', e => seen.push(e.kind + ':' + e.key + ':' + e.origin));
    await B.signIn(a, await h.secondDevice(a));
    await settle(h, B);
    check('the second device sees the bookmark with the same place and title', JSON.stringify(B.sb.SBItems.get('bm', b1.key)) === JSON.stringify(b1.value), B.sb.SBItems.get('bm', b1.key));
    const note = B.sb.SBItems.get('note', '11111111-2222-4333-8444-555555555555');
    check('and the note with its quote and text', note && note.x === 'Remember the common denominator' && note.q === 'common denominator' && note.k === 'note', note);
    check('and where the first device stopped, and the marked word', B.sb.SBItems.get('pos', 'cls5-math').p === 3 && B.sb.SBItems.get('word', 'en:fraction').s === 'l');
    check('a change event with origin "remote" told the page for each item', seen.filter(x => x.endsWith(':remote')).length === 4, seen);

    // 2. the second device edits and deletes; the first follows
    await B.sb.SBItems.put('note', '11111111-2222-4333-8444-555555555555', Object.assign({}, note, { x: 'edited on the second phone' }));
    await B.sb.SBItems.del('bm', b1.key);
    await settle(h, B); await settle(h, A);
    check('an edit made on the other device arrives', A.sb.SBItems.get('note', '11111111-2222-4333-8444-555555555555').x === 'edited on the second phone');
    check('a delete made on the other device arrives', A.sb.SBItems.get('bm', b1.key) === null && A.sb.SBItems.list('bm').length === 0);
  }

  // 3. offline: nothing is lost, nothing is sent twice
  {
    const a = await h.account();
    const A = h.newApp({ flag: true }); await A.signIn(a);
    A.offline();
    await A.sb.SBItems.put('bm', BM('cls5-eng', 1, 0).key, BM('cls5-eng', 1, 0).value);
    await A.sb.SBItems.put('bm', BM('cls5-eng', 1, 1).key, BM('cls5-eng', 1, 1).value);
    await sleep(50);
    const st = await A.sb.SBSync.status();
    check('offline the two bookmarks wait in the outbox and the page still shows them', st.pending === 2 && st.signedIn && A.sb.SBItems.list('bm').length === 2, st);
    A.online();
    await settle(h, A);
    check('back online they are delivered once', (await A.sb.SBSync.pending()) === 0);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a)); await settle(h, B);
    check('and the other device has both', B.sb.SBItems.list('bm').length === 2);
    await settle(h, A); await settle(h, B);
    check('a further round changes nothing (no duplicates)', A.sb.SBItems.list('bm').length === 2 && B.sb.SBItems.list('bm').length === 2);
  }

  // 4. the later time wins on both devices, whichever arrives first
  {
    const a = await h.account();
    const A = h.newApp({ flag: true }); await A.signIn(a);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a));
    const id = '22222222-2222-4333-8444-555555555555';
    const v = x => ({ c: 'cls9', s: 'cls9-phy', ch: 1, p: 0, tb: '', t: 'T', x, q: '', k: 'note' });
    const t0 = Date.now();
    A.offline(); B.offline();
    await B.sb.SBItems.put('note', id, v('second, later'), { at: t0 + 2000 });
    await A.sb.SBItems.put('note', id, v('first, earlier'), { at: t0 + 1000 });
    B.online(); await settle(h, B);          // the later edit reaches the server first
    A.online(); await settle(h, A);          // the earlier one arrives after it
    await settle(h, B);
    check('the earlier edit arriving late does not replace the later one (on the device that sent it, or the other)', A.sb.SBItems.get('note', id).x === 'second, later' && B.sb.SBItems.get('note', id).x === 'second, later', [A.sb.SBItems.get('note', id), B.sb.SBItems.get('note', id)]);
  }

  // 5. a guest's bookmarks are offered to the account, once, and kept on the device if the answer is no
  {
    const a = await h.account(), a2 = await h.account();
    const G = h.newApp({ flag: true });                      // nobody signed in
    await G.sb.SBItems.put('bm', BM('cls5-sci', 3, 1).key, BM('cls5-sci', 3, 1).value);
    check('a guest keeps the bookmark on the device', G.sb.SBItems.list('bm').length === 1 && (await G.sb.SBSync.pendingGuest()) === 0);
    await G.signIn(a);
    await settle(h, G);
    check('on sign-in the student is asked once', G.net.prompts.length === 1 && /bookmarks or notes/.test(G.net.prompts[0]), G.net.prompts);
    const R = h.newApp({ flag: true }); await R.signIn(a, await h.secondDevice(a)); await settle(h, R);
    check('after "yes" the bookmark is on the account and on a second device', R.sb.SBItems.list('bm').length === 1);

    const N = h.newApp({ flag: true, consent: false });
    await N.sb.SBItems.put('bm', BM('cls5-sci', 4, 2).key, BM('cls5-sci', 4, 2).value);
    await N.signIn(a2); await settle(h, N);
    const R2 = h.newApp({ flag: true }); await R2.signIn(a2, await h.secondDevice(a2)); await settle(h, R2);
    check('after "no" nothing of the guest reaches the account', N.net.prompts.length === 1 && R2.sb.SBItems.list('bm').length === 0);
  }

  // 6. best runs only go up; deleting one is refused by the server
  {
    const a = await h.account();
    const A = h.newApp({ flag: true }); await A.signIn(a);
    const key = 'cls5|g-quiz|u0|count|abc123|10';
    await A.sb.SBItems.put('gbest', key, { b: 0.7 });
    await A.sb.SBItems.put('gbest', key, { b: 0.5 });
    await settle(h, A);
    const B = h.newApp({ flag: true }); await B.signIn(a, await h.secondDevice(a)); await settle(h, B);
    check('the other device holds the higher run (0.5 was only a local overwrite and the server kept 0.7)', B.sb.SBItems.get('gbest', key).b === 0.7, B.sb.SBItems.get('gbest', key));
  }

  // 7. one owner switch for both platforms
  {
    const A = h.newApp();
    check('without any switch the older sync is off', !A.sb.SBSync.isEnabled());
    A.sb.SBSync.setServerFlags({ syncV2: true });
    check('the server publishing syncV2 switches it on for this browser', A.sb.SBSync.isEnabled());
    A.sb.localStorage.setItem('sb_sync_v2', 'off');
    check('and a browser can still force it off for testing', !A.sb.SBSync.isEnabled());
    A.sb.localStorage.setItem('sb_sync_v2', 'on'); A.sb.SBSync.setServerFlags({ syncV2: false });
    check('or force it on', A.sb.SBSync.isEnabled());
  }

  h.finish('user items (client + server)');
})().catch(e => { console.log('FAIL  ' + (e && e.stack || e)); process.exit(1); });
