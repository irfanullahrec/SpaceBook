'use strict';
/* Nothing a student selects or hovers is sent to a website: translation and meanings come from the device; an owner-approved proxy is the only
 * way online, and it is off by default.   node --max-old-space-size=8192 tests/lexicon/privacy.js */
const fs = require('fs'), path = require('path');
const { load } = require('../../tools/lib/app_sandbox');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };
const calls = [];
const app = load({ page: 'lazy.html', quiet: true, before: sb => {
  sb.fetch = (u, o) => { if (/^https?:/.test(String(u))) calls.push({ url: String(u), method: o && o.method || 'GET' });     // the app's own api/ calls are relative and not the point here
    return Promise.resolve({ ok: true, status: 200, json: async () => ({ text: 'مشین ترجمہ' }) }); };
  Object.defineProperty(sb.navigator, 'onLine', { value: true, configurable: true });
} });
const run = c => app.run(c, 120000);

(async () => {
  // an unknown sentence, online: nothing is requested
  const out = await run(`SBTranslate.translate('The quick brown fox jumps over the lazy dog near the river bank', 'en', 'ur', true)`);
  check('translating a sentence online asks no website', calls.length === 0, calls.map(c => c.url).join(','));
  check('and the answer is a device gloss or nothing, never labelled a dictionary entry it is not', out && ['gloss', 'offline', 'none', 'dictionary'].includes(out.source), JSON.stringify(out));
  const w = await run(`SBTranslate.translate('water', 'en', 'ur', true)`);
  check('a known word comes from the dictionary on the device', w && w.source === 'dictionary' && w.text, JSON.stringify(w));
  check('still no request', calls.length === 0);

  // the word popover's old online lookup
  const f = await run(`fetchOnlineWordTranslation('xylophone')`);
  check('the old one-word online lookup does nothing and writes nothing into the dictionary', f === null && calls.length === 0 && run(`typeof ENG_URDU_DICT !== 'undefined' && !ENG_URDU_DICT['xylophone']`) === true);

  // with an owner-approved proxy: only the proxy is asked, and the result is labelled online/machine
  run(`window.SB_TRANSLATE_PROXY = 'https://owner.example/translate'`);
  const p = await run(`SBTranslate.translate('Another unseen sentence about rivers and mountains in the north', 'en', 'ur', true)`);
  check('with a proxy set, only the proxy is called', calls.length === 1 && calls[0].url === 'https://owner.example/translate' && calls[0].method === 'POST', JSON.stringify(calls));
  check('and its text is labelled as not from the book', p && p.source === 'online' && p.text === 'مشین ترجمہ', JSON.stringify(p));

  // source scan: no script names a third-party translation host
  const bad = [];
  for (const f of fs.readdirSync(path.join(__dirname, '..', '..', 'js')).filter(f => f.endsWith('.js') && !/_data\.js$/.test(f))) {
    const t = fs.readFileSync(path.join(__dirname, '..', '..', 'js', f), 'utf8');
    if (/translate\.googleapis\.com|api\.mymemory|translate\.google\.com|translated\.net/.test(t.replace(/\/\*[\s\S]*?\*\/|\/\/[^\n]*/g, ''))) bad.push(f);
  }
  check('no script contains a third-party translation or speech host', bad.length === 0, bad.join(','));

  console.log(`privacy tests: ${passed} passed, ${failed} failed`);
  process.exit(failed ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
