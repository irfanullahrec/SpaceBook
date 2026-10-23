'use strict';
/* Stored sentence translations: the key is the same in the build and in the page, a stored sentence is answered from the device (no network),
 * a sentence made of stored sentences is answered by joining them, an unknown sentence gets a labelled word-by-word gloss, never a made-up text.
 *   node --max-old-space-size=8192 tests/lexicon/sentences.js */
const fs = require('fs'), path = require('path');
const { load } = require('../../tools/lib/app_sandbox');
const K = require('../../js/sb_sentkey.js');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

// the data files
const JS = path.join(__dirname, '..', '..', 'js');
let total = 0, bad = 0, firstBad = '';
for (let i = 0; i < K.SHARDS; i++) {
  const f = path.join(JS, 'sent_data_' + i + '.js');
  check('shard ' + i + ' exists', fs.existsSync(f));
  if (!fs.existsSync(f)) continue;
  const w = {}; new Function('window', fs.readFileSync(f, 'utf8'))(w);
  const d = w['SB_SENT_' + i].d;
  for (const [key, v] of Object.entries(d)) {
    total++;
    const p = v.split('\t');
    if (K.shard(key) !== i || p.length !== 4 || !/^[cm-]{3}$/.test(p[0]) || !(p[1] || p[2] || p[3])) { bad++; if (!firstBad) firstBad = key + ' ' + v.slice(0, 40); }
  }
}
check('every stored sentence is in the right shard with 4 fields', bad === 0, bad + ' bad, first ' + firstBad);
check('there are stored sentences', total > 1000, String(total));

// the key is the same in the browser as in the build
const calls = [];
const app = load({ page: 'lazy.html', quiet: true, before: sb => { sb.fetch = (u) => { if (/^https?:/.test(String(u))) calls.push(String(u)); return Promise.resolve({ ok: false, status: 503 }); }; } });
const sample = ['Circle the correct answer.', "Don't  STOP.", 'a mixture of gases, 5 cm long'];
sample.forEach(s => check('same key in the page and in the build for "' + s + '"', app.run(`SBSentKey.key(${JSON.stringify(s)})`) === K.key(s)));
check('punctuation, case and spacing do not change the key', K.key("Don't stop.") === K.key('dont  STOP'));

const run = async c => app.run(c, 120000);
(async () => {
  const a = await run(`SBTranslate.translate('Circle the correct answer.', 'en', 'ur', true)`);
  check('a stored sentence is answered from the device', a && a.source === 'curated' && /دائرہ/.test(a.text), JSON.stringify(a));
  const b = await run(`SBTranslate.translate('Fill in the blanks. Circle the correct answer.', 'en', 'ps', true)`);
  check('two stored sentences are joined', b && b.source === 'curated' && /ډک کړئ/.test(b.text) && /کړۍ/.test(b.text), JSON.stringify(b));
  const c = await run(`SBTranslate.translate('Circle the correct answer.', 'en', 'ar', true)`);
  check('Arabic too', c && /دائرة/.test(c.text), JSON.stringify(c));
  const u = await run(`SBTranslate.translate('Zebras graze quietly beside the northern lakes at dawn.', 'en', 'ur', true)`);
  check('an unknown sentence is a labelled gloss or nothing, never presented as a translation', !u.text || u.source === 'gloss' || u.source === 'offline', JSON.stringify(u));
  check('nothing went to any website', calls.length === 0, calls.join(','));
  console.log(`sentence tests: ${passed} passed, ${failed} failed`);
  process.exit(failed ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
