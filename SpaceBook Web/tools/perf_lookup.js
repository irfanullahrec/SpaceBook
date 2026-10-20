'use strict';
/* CPU-only timing of the two instant lookups of Phase 11 (docs/PERFORMANCE.md): a word meaning and a search inside the books.
 *   node --max-old-space-size=8192 tools/perf_lookup.js
 * Word lookup: the first lookup (it loads the lexicon and the dictionary: bytes and ms) and the next ones (ms each, p50 / p95 / max over a few thousand).
 * Search: the shared index (bytes, parse ms), the biggest shard (bytes, parse + word-list sort ms), and a query on it (ms each); what "Search all classes" has to
 * transfer (sum of the shards, raw and gzipped). Network time is not measured. Dev-only. */
const fs = require('fs'), path = require('path'), zlib = require('zlib');
const { load, ROOT } = require('./lib/app_sandbox');
const S = require('../js/core/search.js');
const now = () => Number(process.hrtime.bigint()) / 1e6;
const pct = (a, p) => { const s = a.slice().sort((x, y) => x - y); return s[Math.min(s.length - 1, Math.floor(s.length * p))]; };
const f = (n, d = 1) => n.toFixed(d);

// ---- word lookup
const app = load({ page: 'lazy.html', quiet: true });
let t = now();
app.run("SBOfflineLookup('water', 'en', 'ur')");
const first = now() - t, st = app.sb.SBLazy.stats();
const rows = JSON.parse(app.run('JSON.stringify(SB_LEXICON_V1.rows)'));
const words = [];
rows.forEach((r, i) => { if (i % 5 === 0) { const w = String(r[0] || '').split(/[،,]/)[0].replace(/\(.*?\)/g, '').trim(); if (w && w.split(' ').length <= 2) words.push(w); } });
const each = [];
for (const w of words.slice(0, 1500)) { const t1 = now(); app.run(`SBOfflineLookup(${JSON.stringify(w)}, 'en', 'ur')`); each.push(now() - t1); }
console.log(`word lookup: first ${f(first)} ms (loaded ${st.loaded} files, ${(st.bytesLoaded / 1e6).toFixed(2)} MB); next ${each.length}: p50 ${f(pct(each, 0.5), 2)} ms, p95 ${f(pct(each, 0.95), 2)} ms, max ${f(Math.max(...each), 2)} ms (the cost of one app.run call is part of each)`);

// ---- search
const dir = path.join(ROOT, 'content', 'search');
if (!fs.existsSync(path.join(dir, 'index.json'))) { console.log('search: content/search/ is missing (node tools/build/make_search.js)'); process.exit(0); }
const idxText = fs.readFileSync(path.join(dir, 'index.json'), 'utf8');
t = now(); const idx = JSON.parse(idxText); const idxMs = now() - t;
console.log(`search index: ${(idxText.length / 1024).toFixed(0)} KB (${(zlib.gzipSync(idxText).length / 1024).toFixed(0)} KB gzipped), parse ${f(idxMs)} ms, ${Object.keys(idx.subjects).length} subjects`);
const files = Object.keys(idx.subjects).map(id => ({ id, text: fs.readFileSync(path.join(dir, id + '.json'), 'utf8') }));
const raw = files.reduce((n, x) => n + x.text.length, 0), gz = files.reduce((n, x) => n + zlib.gzipSync(x.text).length, 0);
console.log(`search all classes transfers: ${(raw / 1048576).toFixed(1)} MB raw, ${(gz / 1048576).toFixed(1)} MB gzipped, in ${files.length} files`);
const big = files.slice().sort((a, b) => b.text.length - a.text.length)[0];
t = now(); const shard = JSON.parse(big.text); const parse = now() - t;
const qs = ['cell', 'velocity energy', 'determinant', 'chlorophyll', 'electron', 'mitoch', 'fraction', 'capacitor'];
t = now(); S.searchShard(shard, S.tokens(qs[0]), 5); const firstQuery = now() - t;     // includes the one-time sort of the word list
const qt = [];
for (let r = 0; r < 20; r++) for (const q of qs) { const t1 = now(); S.searchShard(shard, S.tokens(q), 5); qt.push(now() - t1); }
console.log(`biggest shard ${big.id}: ${(big.text.length / 1024).toFixed(0)} KB, ${Object.keys(shard.x).length} words; parse ${f(parse)} ms; first query (builds the sorted word list) ${f(firstQuery)} ms; next ${qt.length}: p50 ${f(pct(qt, 0.5), 3)} ms, p95 ${f(pct(qt, 0.95), 3)} ms`);
// a whole search over every shard in memory (the worst case of "Search all classes" without the network)
const all = files.map(x => JSON.parse(x.text));
t = now(); for (const sh of all) S.searchShard(sh, S.tokens('energy'), 5); const allMs = now() - t;
console.log(`one query over all ${all.length} shards already in memory: ${f(allMs)} ms (includes sorting each word list once)`);
