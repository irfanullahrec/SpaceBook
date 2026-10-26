'use strict';
/* js/sb_feed.js without a browser: how a post is dated, the four cards made from the student's own records (the same numbers the app reads in
 * assets/prep_summary.js), the shapes of the golden file tests/parity/feed_contract.json, and that nothing a student wrote reaches the page unescaped.
 *     node tests/feed/cards.js
 * The page itself (tabs, dialogs, scrolling, the real server) is tests/feed/browser.js. */
const fs = require('fs'), vm = require('vm'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const contract = JSON.parse(fs.readFileSync(path.join(ROOT, 'tests', 'parity', 'feed_contract.json'), 'utf8'));
let pass = 0, fail = 0;
const check = (label, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 400) : '')); } };

const DAY = 86400000;
const NOW = new Date(2026, 9, 23, 11, 0).getTime();                       // 23 Oct 2026, 11:00 local, the moment tools/test_prep_summary.js uses in the app
const pad = n => String(n).padStart(2, '0');

const day = k => { const d = new Date(NOW - k * DAY); return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); };

function load(store, user) {
  const ls = { getItem: k => (k in store ? store[k] : null), setItem: (k, v) => { store[k] = String(v); }, removeItem: k => { delete store[k]; }, key: i => Object.keys(store)[i], get length() { return Object.keys(store).length; } };
  const doc = { addEventListener() {}, getElementById() { return null; }, querySelector() { return null; }, querySelectorAll() { return []; }, createElement() { return { style: {}, appendChild() {} }; }, head: { appendChild() {} }, body: { appendChild() {} } };
  const g = { console, localStorage: ls, document: doc, TextEncoder, URLSearchParams, Date, Math, JSON, Number, String, Array, Object, Set, setTimeout, clearTimeout };
  g.window = g; g.SpaceBookAuth = { user };
  g.SB_STUDY_INDEX = { classes: [{ id: 'cls6', name: 'Class 6', subjects: [{ id: 'cls6-math', name: 'Mathematics', chapters: [{}, {}, {}] }, { id: 'cls6-eng', name: 'English', chapters: [{}, {}] }] }] };
  vm.createContext(g);
  vm.runInContext(fs.readFileSync(path.join(ROOT, 'js', 'sb_feed.js'), 'utf8'), g, { filename: 'sb_feed.js' });
  return g;
}

// ---- a student's records, the same ones tools/test_prep_summary.js of the app uses
const record = {
  v: 1, updatedAt: NOW,
  sessions: [{ id: 'a', track: 'pst', mode: 'practice', ts: NOW - 3 * DAY, n: 20, c: 14, ms: 600000 }, { id: 'b', track: 'pst', mode: 'mock', ts: NOW - DAY, n: 50, c: 35, ms: 3000000 }, { id: 'c', track: 'sst-gen', mode: 'practice', ts: NOW - 3600000, n: 10, c: 9, ms: 300000 }],
  days: {
    pst: { [day(3)]: [600000, 20, 14], [day(1)]: [3000000, 50, 35] },
    'sst-gen': { [day(0)]: [300000, 10, 9] },
    all: { [day(3)]: [600000, 20, 14], [day(1)]: [3000000, 50, 35], [day(0)]: [300000, 10, 9] },
  },
};
const plan = {
  id: 'p1', name: 'Class 6 term 1', classId: 'cls6', start: day(2), end: day(-6), updatedAt: NOW,
  scope: [{ subj: 'cls6-math', ch: [0, 1, 2] }],
  sessions: [
    { date: day(0), from: '16:00', to: '17:00', tasks: [{ cat: 'mcq', n: 10, done: 10, s: 'cls6-math', ch: 0 }, { cat: 'read', n: 2, done: 1, s: 'cls6-math', ch: 0 }] },
    { date: day(-1), from: '16:00', to: '17:00', tasks: [{ cat: 'sq', n: 4, done: 0, s: 'cls6-math', ch: 1 }] },
  ],
};
const store = { 'sbTP:v1:12': JSON.stringify(record), sb_study_plans_v1: JSON.stringify([plan]), 'sbWS:progress:12': JSON.stringify({ words: { 'en:fraction': { s: 'l', t: NOW }, 'en:ratio': { s: 'k', t: NOW }, 'en:other': { s: 'x' } } }), 'sbTP:v1:guest': JSON.stringify({ days: { all: { [day(0)]: [60000, 999, 999] } } }) };
const W = load(store, { id: 12, name: 'Ayesha Khan', user_type: 'student' });
const F = W.SBFeed;

// ---- dating a post (the app's timeAgo, same words)
console.log('--- time and counts ---');
const t0 = 1793000000000;
check('Just now, minutes, hours, Yesterday, days', F.timeAgo(t0 - 20000, t0) === 'Just now' && F.timeAgo(t0 - 5 * 60000, t0) === '5m' && F.timeAgo(t0 - (3 * 3600000 + 5), t0) === '3h' && F.timeAgo(t0 - 30 * 3600000, t0) === 'Yesterday' && F.timeAgo(t0 - 3 * DAY, t0) === '3d' && F.timeAgo(0, t0) === '');
check('an older post gets a date, another year says the year', /^[A-Z][a-z]{2} \d{1,2}$/.test(F.timeAgo(t0 - 40 * DAY, t0)) && /^[A-Z][a-z]{2} \d{1,2}, \d{4}$/.test(F.timeAgo(t0 - 800 * DAY, t0)), [F.timeAgo(t0 - 40 * DAY, t0), F.timeAgo(t0 - 800 * DAY, t0)]);
check('short counts: 999, 1.2K, 1K, 15K, 1.5M', [999, 1200, 1000, 15300, 1500000].map(F.shortCount).join(' ') === '999 1.2K 1K 15K 1.5M');

// ---- the cards
console.log('--- the cards from the student\'s own records ---');
const c = F.collect(NOW);
check('totals: 80 questions, 58 right, 65 minutes, 3 sessions, streak 2 (the guest record is not used)', c.totals.questions === 80 && c.totals.correct === 58 && c.totals.minutes === 65 && c.totals.sessions === 3 && c.totals.streak === 2, c.totals);
check('today: 10 questions, 9 right, 5 minutes', c.totals.todayQuestions === 10 && c.totals.todayCorrect === 9 && c.totals.todayMinutes === 5, c.totals);
const stats = F.cards.stats(NOW);
check('the My Stats card has the numbers of My Stats and the golden fields', stats.questions === 80 && stats.accuracy === 73 && stats.minutes === 65 && stats.streak === 2 && stats.words === 2 && stats.plans === 1 && stats.tests.length === 2 && stats.tests[0].title === 'PST' && stats.tests[0].mcqs === 70 && stats.tests[0].acc === 70
  && JSON.stringify(Object.keys(stats).sort()) === JSON.stringify(Object.keys(contract.cards.stats).sort()), stats);
const prog = F.cards.progress(NOW, 38);
check('the day card: today\'s questions, minutes, the tasks of today\'s plans, the coins, the golden fields', prog.questions === 10 && prog.correct === 9 && prog.minutes === 5 && prog.tasksTotal === 2 && prog.tasksDone === 1 && prog.coins === 38 && prog.goal === 20 && prog.date === day(0)
  && JSON.stringify(Object.keys(prog).sort()) === JSON.stringify(Object.keys(contract.cards.progress).sort()), prog);
const pl = F.cards.plan('p1', NOW);
check('the plan card: name, label, subjects, days, tasks, golden fields (the server adds pct)', pl.name === 'Class 6 term 1' && pl.label === 'Class 6 · Mathematics' && pl.subjects[0] === 'Mathematics' && pl.days === 9 && pl.tasks === 16 && pl.done === 11
  && JSON.stringify(Object.keys(pl).sort()) === JSON.stringify(Object.keys(contract.cards.plan).filter(k => k !== 'pct').sort()), pl);
const q = F.cards.question('Chemistry', 'Class 9', 'Unit 4');
check('the question card has the golden fields; nothing tagged means no card', JSON.stringify(Object.keys(q).sort()) === JSON.stringify(Object.keys(contract.cards.question).sort()) && F.cards.question('', '', '') === null && F.cards.question('x'.repeat(100)).subject.length === 60);
const empty = load({}, { id: 99, name: 'New Student', user_type: 'student' }).SBFeed;
check('with nothing done there is nothing to share: no stats, no day card, no plan', empty.cards.stats(NOW) === null && empty.cards.progress(NOW, 0) === null && empty.cards.plan(undefined, NOW) === null);
const guest = load({ 'sbTP:v1:guest': JSON.stringify(record) }, null).SBFeed;
check('a guest\'s own record is read for the guest', guest.cards.stats(NOW).questions === 80);
check('a plan label says "all subjects" when every subject is in the plan, "N chapters" for a part of one subject, "N subjects" for several', (() => {
  const mk = scope => load({ sb_study_plans_v1: JSON.stringify([Object.assign({}, plan, { scope })]) }, { id: 1, name: 'A B' }).SBFeed.cards.plan('p1', NOW).label;
  return mk([{ subj: 'cls6-math', ch: [0, 1, 2] }, { subj: 'cls6-eng', ch: [0, 1] }]) === 'Class 6 · all subjects' && mk([{ subj: 'cls6-math', ch: [0] }]) === 'Class 6 · Mathematics · 1 chapter' && mk([{ subj: 'cls6-math', ch: [0, 1] }]) === 'Class 6 · Mathematics · 2 chapters' && mk([{ subj: 'cls6-math', ch: [0] }, { subj: 'cls6-eng', ch: [0] }]) === 'Class 6 · 2 subjects';
})());

// ---- what is drawn
console.log('--- the page ---');
const post = Object.assign({}, contract.post, { author: Object.assign({}, contract.author, { name: '<b>Ali</b> K.' }), body: '<img src=x onerror=alert(1)> & "quotes"' });
let html = F._html.post(post, t0 + 60000);
check('a student\'s words and name are escaped', !/<img|<b>Ali|onerror=alert\(1\)>/.test(html) && html.includes('&lt;img src=x onerror=alert(1)&gt; &amp; &quot;quotes&quot;') && html.includes('&lt;b&gt;Ali&lt;/b&gt; K.'), html.slice(0, 500));
const kinds = { stats: contract.cards.stats, progress: contract.cards.progress, plan: contract.cards.plan, question: contract.cards.question };
check('every card kind of the golden file is drawn', Object.keys(kinds).every(k => { const h = F._html.post(Object.assign({}, contract.post, { kind: k, body: 'x', card: kinds[k] }), t0); return h.includes('sbfd-attach') || k === 'question' && h.includes('sbfd-chips'); }));
const evil = Object.assign({}, contract.cards.plan, { name: '<script>alert(1)</script>', label: '"><img src=x>', subjects: ['<i>x</i>'] });
html = F._html.post(Object.assign({}, contract.post, { kind: 'plan', body: '', card: evil }), t0);
check('a card is escaped too', !/<script>|<img src|<i>x/.test(html) && html.includes('&lt;script&gt;'), html.slice(0, 300));
html = F._html.post(contract.share, t0 + 1000);
check('a share draws the original inside it, and says so when the original is gone', html.includes('sbfd-shared') && html.includes('Which chapter of Biology is the hardest?') && F._html.post(Object.assign({}, contract.share, { shared: null }), t0).includes("This post isn't available"));
const big = F._html.post(Object.assign({}, contract.post, { body: 'Revise a little every day.' }), t0);
check('a few plain words are shown big on a colour, a long text is not', big.includes('sbfd-big') && !F._html.post(Object.assign({}, contract.post, { body: 'w'.repeat(200) }), t0).includes('sbfd-big'));
check('Urdu text is drawn right to left', F._html.post(Object.assign({}, contract.post, { body: 'کل کا ٹیسٹ بہت اچھا ہوا، سب کو شکریہ' }), t0).includes('dir="rtl"'));
check('the like button says whether it is on', F._html.post(Object.assign({}, contract.post, { liked: true }), t0).includes('aria-pressed="true"') && F._html.post(Object.assign({}, contract.post, { liked: false }), t0).includes('aria-pressed="false"'));

console.log('---\nfeed cards: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
