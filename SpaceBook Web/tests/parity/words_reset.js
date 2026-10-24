'use strict';
/* The ↺ Reset of the My Vocabulary card ("Words from Subjects & Units" on Home → My Stats): the website clears every mark of the student
 * (the stored record and the synced items), asks first, and leaves the next student's record alone. The app does the same by calling
 * SBWordStats.resetWords({ask: false}) in its web page (assets/reader_bridge.js, SBApp.resetWords).
 *     node --max-old-space-size=6144 tests/parity/words_reset.js
 * Dev-only. */
const { load } = require('../../tools/lib/app_sandbox');

let pass = 0, fail = 0;
const check = (l, ok, d) => { if (ok) { pass++; console.log('PASS  ' + l); } else { fail++; console.log('FAIL  ' + l + (d !== undefined ? '  -> ' + JSON.stringify(d).slice(0, 400) : '')); } };

const now = Date.now(), DAY = 86400000;
const mine = { v: 1, words: {
  'en:cell': { s: 'l', t: now - 3600e3 }, 'en:atom': { s: 'l', t: now - 3 * DAY }, 'en:mass': { s: 'k', t: now - DAY },
  'ur:کتاب': { s: 'l', t: now - 100 }, 'ps:کور': { s: 'k', t: now - 5 * DAY }, 'ar:علم': { s: 'l', t: now - 2 * DAY },
} };
const other = { v: 1, words: { 'en:force': { s: 'l', t: now - DAY } } };

(async () => {
  const app = load({ quiet: true, before(sb) {
    sb.localStorage.setItem('sbWS:progress:guest', JSON.stringify(mine));
    sb.localStorage.setItem('sbWS:progress:somebody else', JSON.stringify(other));
  } });
  const sb = app.sb, W = sb.SBWordStats;
  const stored = key => { try { return Object.keys(JSON.parse(sb.localStorage.getItem(key) || '{}').words || {}).length; } catch (e) { return -1; } };
  for (const k of Object.keys(mine.words)) await sb.SBItems.put('word', k, { s: mine.words[k].s }, { at: mine.words[k].t });

  const card = () => { const el = sb.document.getElementById('homeMyWords'); W.renderMyWords(el); return el.innerHTML; };
  check('the card has a Reset button', /SBWordStats\.resetWords\(\)/.test(card()) && />↺ Reset</.test(card()));
  check('enabled while words are marked', !/resetWords\(\)"[^>]*disabled/.test(card()) && W.progressSummary().total === 6, W.progressSummary());

  sb.confirm = q => { sb.__asked = q; return false; };
  const no = await W.resetWords();
  check('it asks first, with the number of words, and "no" changes nothing', no === false && /6 words/.test(sb.__asked) && W.progressSummary().total === 6 && stored('sbWS:progress:guest') === 6 && sb.SBItems.list('word').length === 6, [no, sb.__asked]);

  sb.confirm = () => true;
  const n = await W.resetWords();
  check('"yes" clears all six marks', n === 6, n);
  check('the counts are zero, today and the week too', JSON.stringify([W.progressSummary().learnt, W.progressSummary().knew, W.progressSummary().today, W.progressSummary().week, W.progressSummary().total]) === '[0,0,0,0,0]', W.progressSummary());
  check('the stored record is empty', stored('sbWS:progress:guest') === 0);
  check('and the synced items are deleted (a tombstone each, so they do not come back)', sb.SBItems.list('word').length === 0);
  check('another student\'s record is untouched', stored('sbWS:progress:somebody else') === 1);
  check('the card shows zeros and the button is disabled', /resetWords\(\)"[^>]*disabled/.test(card()) && />0</.test(card()));
  check('nothing to reset: no question, answer 0', (sb.confirm = () => { throw new Error('asked'); }, await W.resetWords()) === 0);

  // the app skips the question (it asked in its own dialog)
  // (marks that only exist as synced items, made on another device, are cleared too)
  await sb.SBItems.put('word', 'en:river', { s: 'l' }); await sb.SBItems.put('word', 'en:lake', { s: 'k' });
  sb.confirm = () => { throw new Error('asked'); };
  check('{ask: false} clears without asking', await W.resetWords({ ask: false }) === 2 && sb.SBItems.list('word').length === 0);

  console.log(`\n${pass} passed, ${fail} failed  (words reset)`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  ' + (e && e.stack || e)); process.exit(1); });
