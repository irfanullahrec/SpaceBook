'use strict';
/* Search inside the books (js/core/search.js + tools/build/make_search.js): words, index, the box in the header, offline package.
 *   node --max-old-space-size=8192 tests/search/search.js */
const fs = require('fs'), path = require('path'), os = require('os'), crypto = require('crypto');
const { spawnSync } = require('child_process');
const S = require('../../js/core/search.js');
const ROOT = path.resolve(__dirname, '..', '..');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };
const same = (a, b) => S.normalize(a) === S.normalize(b);

// ---------------------------------------------------------------- words
check('Latin: case and accents do not matter', same('Café', 'cafe') && same('MITOCHONDRIA', 'mitochondria'));
check('Arabic kaf and yeh are the Urdu letters', same('كتاب', 'کتاب') && same('الحياة', 'الحیاة'));
check('vowel marks, tatweel and the Quranic signs are dropped', same('کِتاب', 'کتاب') && same('كتـــاب', 'کتاب') && same('بِسْمِ', 'بسم'));
check('hamza and madda forms of alef fold to alef', same('أحمد', 'احمد') && same('إسلام', 'اسلام') && same('آپ', 'اپ'));
check('the heh family is one letter (teh marbuta, Arabic heh, Urdu heh, do-chashmi heh)', same('مدرسة', 'مدرسہ') && same('مدرسه', 'مدرسہ') && same('بھائی', 'بہائی'));
check('Pashto gaf and ye variants fold to the Urdu ones', same('ګل', 'گل') && same('کې', 'کی') && same('ډېر', 'ډیر'));
check('Arabic-Indic and Persian digits are digits', S.normalize('١٢٣ ۴۵۶') === '123 456');
check('a zero-width non-joiner separates, other invisible characters vanish', S.tokens('می‌خواہ').length === 2 && same('ab‍c', 'abc'));
check('presentation forms are plain letters (the word Allah as one glyph)', S.normalize('ﷲ').includes('الل'));
check('plurals: cells -> cell, studies -> study, boxes -> box; glass, analysis, bus stay', S.stem('cells') === 'cell' && S.stem('studies') === 'study' && S.stem('boxes') === 'box' && S.stem('glass') === 'glass' && S.stem('analysis') === 'analysis' && S.stem('bus') === 'bus');
check('tokens: one-letter words and long numbers are dropped', S.tokens('A cell has 2 nuclei 123456789 and 9.8').join(',') === 'cell,has,nuclei,and');

// ---------------------------------------------------------------- index and ranking
const book = [
  { title: 'Cells', text: 'The mitochondria make energy. Cells have a nucleus. Mitochondria are small.' },
  { title: 'Energy', text: 'Energy is stored in food. Plants make energy from light with chlorophyll.' },
  { title: 'Plants', text: 'Chlorophyll is green. Plants use light. Light and water make food.' },
];
const shard = S.makeShard(book);
check('shard: words with chapter/count pairs', shard.n === 3 && JSON.stringify(shard.x.mitochondria) === JSON.stringify([0, 2]) && shard.x.energy.length === 4);
check('shard: deterministic', JSON.stringify(S.makeShard(book)) === JSON.stringify(shard));
const find = q => S.searchShard(shard, S.tokens(q)).map(r => r.chapter);
check('one word finds the chapters that have it, best first', JSON.stringify(find('energy')) === JSON.stringify([1, 0]), JSON.stringify(find('energy')));
check('every word must be there (AND)', JSON.stringify(find('light food')) === JSON.stringify([2, 1]) || JSON.stringify(find('light food')) === JSON.stringify([1, 2]));
check('the last word may be unfinished', JSON.stringify(find('mitoch')) === JSON.stringify([0]) && find('chloro').length === 2);
check('an unfinished word before the last is matched as a prefix when no whole word fits', find('mitoch energy').length === 1 && find('energy mitoch').length === 1);
check('plural and singular meet', find('cell')[0] === 0 && find('cells')[0] === 0);
check('a word in the title weighs more than in the text', find('plants')[0] === 2, JSON.stringify(find('plants')));
check('a word that is nowhere gives nothing, an empty query gives nothing', find('zebra').length === 0 && find('').length === 0);
const many = S.makeShard(Array.from({ length: 60 }, (_, i) => ({ title: 'T' + i, text: 'common ' + 'common '.repeat(i % 5) })));
check('a word in every chapter keeps its 24 best', many.x.common.length === 48);

if (process.env.SB_UNIT_ONLY) { console.log(`search tests (words and ranking only): ${passed} passed, ${failed} failed`); process.exit(failed ? 1 : 0); }

// ---------------------------------------------------------------- the builder
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sbsearch-'));
const r = spawnSync(process.execPath, ['--max-old-space-size=8192', 'tools/build/make_search.js', '--only', 'cls9-bio,cls12-urdu', '--out', tmp], { cwd: ROOT, encoding: 'utf8', maxBuffer: 1 << 26 });
check('the builder runs', r.status === 0, (r.stderr || '').slice(-300));
const idx = fs.existsSync(path.join(tmp, 'index.json')) ? JSON.parse(fs.readFileSync(path.join(tmp, 'index.json'), 'utf8')) : { subjects: {} };
const bio = idx.subjects['cls9-bio'], urd = idx.subjects['cls12-urdu'];
check('the index lists both subjects with their chapters and calls', !!bio && !!urd && bio.n === bio.c.length && bio.n >= 5 && bio.c.every(c => c.t && /\w+\(.*\)/.test(c.o)), bio && JSON.stringify(bio.c[0]));
const biologyShard = bio ? JSON.parse(fs.readFileSync(path.join(tmp, 'cls9-bio.json'), 'utf8')) : null;
const urduShard = urd ? JSON.parse(fs.readFileSync(path.join(tmp, 'cls12-urdu.json'), 'utf8')) : null;
check('the hash in the index is the hash of the file', bio && bio.h === crypto.createHash('sha256').update(fs.readFileSync(path.join(tmp, 'cls9-bio.json'), 'utf8')).digest('hex').slice(0, 12));
check('the shard holds words, no markup residue (no word with <, >, =, ;, &, braces or quotes; no tag name from the attributes)', biologyShard && Object.keys(biologyShard.x).length > 1000 && !Object.keys(biologyShard.x).some(w => /[<>=;&{}"]/.test(w) || w === 'nbsp' || w === 'quot' || w === 'amp'), biologyShard && Object.keys(biologyShard.x).filter(w => /[<>=;&{}"]/.test(w) || w === 'nbsp' || w === 'quot' || w === 'amp').slice(0, 8).join(','));
check('the translation lines kept in attributes are indexed (Urdu words in an English book)', biologyShard && Object.keys(biologyShard.x).some(w => /[؀-ۿ]/.test(w)));

// ---------------------------------------------------------------- the committed index is part of the offline packages
const committed = path.join(ROOT, 'content', 'search', 'index.json'), offlineMap = path.join(ROOT, 'content', 'offline_map.json');
if (fs.existsSync(committed) && fs.existsSync(offlineMap)) {
  const ci = JSON.parse(fs.readFileSync(committed, 'utf8')), om = JSON.parse(fs.readFileSync(offlineMap, 'utf8'));
  const ids = Object.keys(ci.subjects);
  check('the committed index covers the subjects with a chapter list', ids.length > 100, String(ids.length));
  const bad = ids.filter(id => {
    const s = om.subjects[id], src = 'content/search/' + id + '.json';
    return !s || !s.files.includes(src) || !om.files[src] || om.files[src].v !== ci.subjects[id].h || !s.assets.includes('content/search/index.json');
  });
  check('every indexed subject has its shard (same hash) and the shared index in its offline package', bad.length === 0, bad.slice(0, 5).join(','));
  check('every shard file is the one the index describes', ids.every(id => crypto.createHash('sha256').update(fs.readFileSync(path.join(ROOT, 'content', 'search', id + '.json'), 'utf8')).digest('hex').slice(0, 12) === ci.subjects[id].h));
}

// ---------------------------------------------------------------- the box in the header
(async () => {
  const { loadDom } = require('../../tools/lib/app_dom');
  const requested = [];
  const app = await loadDom({
    page: 'index.html',
    beforeScripts: w => {
      w.fetch = url => {
        requested.push(String(url));
        const m = /^content\/search\/([^?]+)/.exec(String(url));
        const f = m && path.join(tmp, m[1]);
        if (!f || !fs.existsSync(f)) return Promise.resolve({ ok: false, status: 404, json: () => Promise.reject(new Error('404')) });
        const text = fs.readFileSync(f, 'utf8');
        return Promise.resolve({ ok: true, status: 200, json: () => Promise.resolve(JSON.parse(text)) });
      };
    },
  });
  const w = app.win, d = w.document;
  check('the page has SBSearch', typeof w.SBSearch === 'object' && typeof w.SBSearch.init === 'function');
  const type = async q => { const inp = d.getElementById('globalHubSearch'); inp.value = q; w.handleGlobalSearch(q); for (let i = 0; i < 6; i++) await app.settle(); };
  const rows = () => [...d.querySelectorAll('#searchResultsDropdown .sb-ft-row')];
  const dd = () => d.getElementById('searchResultsDropdown');

  // no book is open and nothing is downloaded: it says so and offers the whole library
  await type('chlorophyll');
  check('nothing open, nothing downloaded: a note and the "Search all classes" button', !!dd().querySelector('.sb-ft .sb-ft-all') && rows().length === 0);

  // a word of the open book
  w.openSubject('cls9', 'cls9-bio'); await app.settle();
  const terms = Object.entries(biologyShard.x).filter(([t, p]) => p.length === 2 && /^[a-z]{8,}$/.test(t) && p[1] >= 2).map(([t, p]) => [t, p[0]]);
  const [word, chapter] = terms[Math.floor(terms.length / 2)];
  await type(word);
  check('a word of the open book lists chapters of it, the right one first', rows().length >= 1 && rows()[0].textContent.includes(bio.c[chapter].t), word + ' -> ' + (rows()[0] && rows()[0].textContent));
  check('each row says where it is (class, subject, number of matches)', /Class 9/.test(rows()[0].textContent) && /match/.test(rows()[0].textContent), rows()[0].textContent);
  const searchRequests = requested.filter(u => !/^api\//.test(u));            // the sign-in check of the page is not the search
  check('the search asked only for files of this site under content/search/', searchRequests.length > 0 && searchRequests.every(u => /^content\/search\//.test(u)), requested.join(','));
  check('the shard is fetched by its content hash', requested.some(u => u === 'content/search/cls9-bio.json?v=' + bio.h));

  // an unfinished last word
  await type(word.slice(0, word.length - 2));
  check('an unfinished last word still finds it', rows().some(r => r.textContent.includes(bio.c[chapter].t)));

  // a click opens the book and the chapter with the chapter's own button
  const calls = [];
  const fnName = bio.c[chapter].o.match(/^(\w+)\(/)[1];
  const real = w[fnName];
  w[fnName] = function () { calls.push(fnName + ':' + [].slice.call(arguments).join(',')); return real.apply(this, arguments); };
  await type(word);
  rows()[0].click(); await app.settle();
  check('a click opens the chapter through its own button', calls.length === 1 && calls[0].startsWith(fnName + ':'), JSON.stringify(calls));
  check('and closes the search box', dd().style.display === 'none');
  w[fnName] = real;

  // a word that is only in the Urdu book, typed with other letter forms: needs the whole library
  const urTerm = Object.entries(urduShard.x).find(([t, p]) => /^[؀-ۿ]{5,}$/.test(t) && p.length === 2 && p[1] >= 2 && !(t in biologyShard.x) && !Object.keys(biologyShard.x).some(k => k.startsWith(t)));
  const variant = urTerm[0].replace(/ی/g, 'ي').replace(/ک/g, 'ك') + 'ِ';              // Arabic yeh and kaf, plus a vowel mark
  await type(variant);
  check('a word of another book is not found in the open one, a button offers all classes', rows().length === 0 && !!dd().querySelector('.sb-ft-all'), variant);
  dd().querySelector('.sb-ft-all').click();
  for (let i = 0; i < 8; i++) await app.settle();
  const urdRows = rows();
  check('"Search all classes" finds it, with Arabic letter forms and a vowel mark in the query', urdRows.length >= 1 && urdRows[0].textContent.includes('12') || urdRows.some(r => /Class 12/.test(r.textContent)), urdRows.map(r => r.textContent).join(' | '));
  check('and does not keep every book in memory', w.SBSearch._state.shards.size <= 8);

  // an obscure word the titles do not have: the "no results" block makes room for the book results
  console.log(`search tests: ${passed} passed, ${failed} failed`);
  fs.rmSync(tmp, { recursive: true, force: true });
  process.exit(failed ? 1 : 0);
})().catch(e => { console.log('CRASH', e && e.stack || e); process.exit(1); });
