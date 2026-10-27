'use strict';
/* Builds the search index (Phase 12): what the header search box reads (js/core/search.js).
 *   content/search/index.json     for every subject with a chapter list: class, name, hash and size of its shard, and its chapters
 *                                 (title and the call its own sidebar button makes, so a result can open the chapter with that button)
 *   content/search/<subject>.json the words of the subject: word -> [chapter, count, ...] (see makeShard in js/core/search.js)
 * The text of a chapter is what a student can read: every tab of every chapter is rendered in a fresh app sandbox (the same walk as
 * tools/build/make_offline.js), tags and formula markup are dropped, and the translation lines kept in data-en / data-ur / data-ps /
 * data-ar attributes are included, so a word in any of the four languages finds the chapter.
 *   node --max-old-space-size=8192 tools/build/make_search.js [--only cls9-bio,cls9-math] [--page lazy.html] [--out dir]
 *   node tools/build/make_search.js --check    exit 1 when the committed index is stale (fast: the data hashes, the normaliser, and three
 *                                              sample subjects re-rendered and compared byte for byte)
 * Run through tools/build/all.js. Dev-only. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { load, ROOT } = require('../lib/app_sandbox');
const { makeShard } = require('../../js/core/search.js');
const args = process.argv.slice(2);
const arg = k => (args.includes(k) ? args[args.indexOf(k) + 1] : null);
const CHECK = args.includes('--check');
const PAGE = arg('--page') || 'lazy.html';
const ONLY = arg('--only') ? arg('--only').split(',') : null;
const OUT = path.resolve(ROOT, arg('--out') || path.join('content', 'search'));
const sha256 = buf => crypto.createHash('sha256').update(buf).digest('hex');
const lf = file => fs.readFileSync(path.join(ROOT, file), 'utf8').replace(/\r\n/g, '\n');

const VIEWS = {
  generic: { area: 'subjectTopicArea', content: 'subjTabContent', chapter: 'select\\w*(?:Chapter|Unit|Lesson|Page)', tab: 'switchSubjectTab', reset: 'state.activeSubjTab = null; ' },
  math: { area: 'mathTopicArea', content: 'mathTabContent', chapter: 'selectMathChapter', tab: 'switchMathTab', reset: '' },
};
const unesc = oc => oc.replace(/&#39;|&quot;/g, "'");
const ENT = { nbsp: ' ', amp: '&', lt: '<', gt: '>', quot: '"', apos: "'" };
const decode = s => s.replace(/&(?:#x([0-9a-f]+)|#(\d+)|([a-z]+));/gi, (m, h, d, n) => h ? String.fromCodePoint(parseInt(h, 16)) : d ? String.fromCodePoint(+d) : (ENT[n.toLowerCase()] !== undefined ? ENT[n.toLowerCase()] : m));
function htmlText(html) {
  const lang = [...html.matchAll(/\sdata-(?:en|ur|ps|ar)="([^"]*)"/g)].map(m => m[1]);              // translation lines kept in attributes
  const body = html
    .replace(/<(script|style|svg)\b[\s\S]*?<\/\1>/gi, ' ')
    .replace(/<span class="katex-mathml">[\s\S]*?<\/span>/gi, ' ')                                    // the formula is drawn twice (MathML for readers + glyphs)
    .replace(/<[^>]+>/g, ' ');
  return (decode(body) + ' ' + decode(lang.join(' ')).replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ');       // the lines in attributes may hold escaped markup of their own
}
const cleanTitle = t => decode(t).replace(/\s+/g, ' ').trim().slice(0, 120);

function buildSubject(s) {
  const app = load({ page: PAGE, quiet: true });
  const step = code => { try { return app.run(code, 120000); } catch (e) { return null; } };
  step(`openSubject(${JSON.stringify(s.classId)}, ${JSON.stringify(s.id)})`);
  const body = step(`document.getElementById('dashboard-body').innerHTML`) || '';
  const V = body.includes('id="mathTopicArea"') ? VIEWS.math : VIEWS.generic;
  const re = new RegExp('<(button|div|a|li|span)\\b[^>]*onclick="(' + V.chapter + '\\([^"]*)"[^>]*>([\\s\\S]*?)</\\1>', 'g');
  const list = [];
  const seenCall = new Set();
  for (const m of body.matchAll(re)) {
    const oc = unesc(m[2]);
    if (seenCall.has(oc)) continue;
    seenCall.add(oc);
    list.push({ o: oc, t: cleanTitle(m[3].replace(/<[^>]+>/g, ' ')) });
  }
  if (!list.length) return null;
  const chapters = [];
  for (const ch of list) {
    step(`${V.reset}${ch.o}`);
    const area = step(`document.getElementById('${V.area}').innerHTML`) || '';
    let text = htmlText(area);
    for (const t of [...new Set([...area.matchAll(new RegExp('onclick="(' + V.tab + '\\([^"]*)"', 'g'))].map(m => m[1]))]) {
      step(`document.getElementById('${V.content}').innerHTML = ''`);
      step(unesc(t));
      text += ' ' + htmlText(step(`document.getElementById('${V.content}').innerHTML`) || '');
    }
    chapters.push({ title: ch.t, text });
  }
  return { list, shard: makeShard(chapters) };
}

// A full build renders every subject in a fresh sandbox of the page and the sandboxes are not given back, so one process needs more memory than a
// small machine has free and dies part-way without a message. A full build therefore asks a child process for each subject (the same code, --only one subject).
// one process is faster; a child per subject is used when less than 3 GB is free (or with --isolate); --in-process forces one process
const ISOLATE = !ONLY && !CHECK && !args.includes('--in-process') && (args.includes('--isolate') || require('os').freemem() < 3 * 2 ** 30);
function buildIsolated(s) {
  const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'sbsearch-'));
  try {
    const p = require('child_process').spawnSync(process.execPath, ['--max-old-space-size=4096', __filename, '--only', s.id, '--out', tmp, '--page', PAGE], { stdio: 'ignore' });
    if (p.status !== 0) throw new Error('the search index of ' + s.id + ' could not be built (child process exit ' + p.status + (p.signal ? ', ' + p.signal : '') + ')');
    const shardFile = path.join(tmp, s.id + '.json');
    if (!fs.existsSync(shardFile)) return null;
    const entry = JSON.parse(fs.readFileSync(path.join(tmp, 'index.json'), 'utf8')).subjects[s.id];
    const text = fs.readFileSync(shardFile, 'utf8');
    return { text, shard: JSON.parse(text), list: entry.c.map(x => ({ o: x.o, t: x.t })) };
  } finally { fs.rmSync(tmp, { recursive: true, force: true }); }
}

const BUILDER_VERSION = 1;                                // bump when the way text is taken from the page (htmlText, the walk of chapters and tabs) changes
const SAMPLE = [{ title: 'Cells and Studies', text: 'Mitochondria make energy. Boxes, glass, analysis \u0643\u0650\u062a\u0627\u0628 \u06f1\u06f2\u06f3 \u06af\u064f\u0644 123456789.' }, { title: 'Light', text: 'Plants use light.' }];
function inputsHash() {
  const man = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'lazy_manifest.json'), 'utf8'));
  const h = [];
  for (const f of man.files) { h.push(f.src + ':' + f.sha256); for (const a of (f.also || []).concat(f.after || [])) h.push(a.src + ':' + a.sha256); }
  // what the normaliser DOES (not how its file reads): its answer for every character of the basic plane, and the shard of a fixed sample
  const S = require('../../js/core/search.js'), fp = [];
  for (let c = 0; c < 0x10000; c++) if (c < 0xd800 || c > 0xdfff) fp.push(S.normalize(String.fromCharCode(c)));
  h.push('normalizer:' + sha256(fp.join('\u0001')), 'shard:' + sha256(JSON.stringify(S.makeShard(SAMPLE))), 'builder:' + BUILDER_VERSION);
  return sha256(h.sort().join('\n'));
}

const probe = load({ page: PAGE, quiet: true });
const allSubjects = probe.run('DATA.classes.flatMap(c => (DATA.subjects[c.id] || []).map(s => ({ classId: c.id, id: s.id, name: s.name })))');

if (CHECK) {
  const indexFile = path.join(ROOT, 'content', 'search', 'index.json');
  if (!fs.existsSync(indexFile)) { console.log('FAIL  content/search/index.json does not exist (node tools/build/make_search.js)'); process.exit(1); }
  const idx = JSON.parse(fs.readFileSync(indexFile, 'utf8'));
  let bad = 0;
  if (idx.source !== inputsHash()) { console.log('FAIL  the search index is older than the book data or the normaliser (node tools/build/make_search.js)'); bad++; }
  const ids = Object.keys(idx.subjects).sort((a, b) => idx.subjects[a].bytes - idx.subjects[b].bytes);
  const sample = [...new Set([0.3, 0.55, 0.8].map(q => ids[Math.floor(ids.length * q)]))];          // three subjects of middling size, from different classes
  for (const id of sample) {
    const s = allSubjects.find(x => x.id === id);
    const r = s && buildSubject(s);
    const stored = fs.readFileSync(path.join(ROOT, 'content', 'search', id + '.json'), 'utf8');
    if (!r || JSON.stringify(r.shard) + '\n' !== stored) { console.log('FAIL  ' + id + ': its search index differs from what the page shows now (node tools/build/make_search.js)'); bad++; }
  }
  if (!bad) console.log(`search index: fresh (${ids.length} subjects; ${sample.length} re-rendered and identical)`);
  process.exit(bad ? 1 : 0);
}

fs.mkdirSync(OUT, { recursive: true });
const index = { schema: 'spacebook.search/1', source: ONLY ? 'partial' : inputsHash(), subjects: {} };
const skipped = [];
let total = 0;
const t0 = Date.now();
for (const s of allSubjects) {
  if (ONLY && !ONLY.includes(s.id)) continue;
  const r = ISOLATE ? buildIsolated(s) : buildSubject(s);
  if (!r) { skipped.push(s.id); continue; }
  const text = r.text || JSON.stringify(r.shard) + '\n';
  fs.writeFileSync(path.join(OUT, s.id + '.json'), text);
  index.subjects[s.id] = { classId: s.classId, name: s.name, h: sha256(text).slice(0, 12), bytes: Buffer.byteLength(text), n: r.list.length, c: r.list.map(x => ({ t: x.t, o: x.o })) };
  total += Buffer.byteLength(text);
  console.log(`${s.id.padEnd(18)} ${String(r.list.length).padStart(3)} chapters  ${String(Object.keys(r.shard.x).length).padStart(7)} words  ${(Buffer.byteLength(text) / 1024).toFixed(0).padStart(6)} KB`);
}
index.subjects = Object.fromEntries(Object.keys(index.subjects).sort().map(k => [k, index.subjects[k]]));
fs.writeFileSync(path.join(OUT, 'index.json'), JSON.stringify(index) + '\n');
console.log(`wrote ${Object.keys(index.subjects).length} subjects, ${(total / 1048576).toFixed(1)} MB of shards, index ${(fs.statSync(path.join(OUT, 'index.json')).size / 1024).toFixed(0)} KB, ${((Date.now() - t0) / 1000).toFixed(0)} s` + (skipped.length ? `; no chapter list (not searchable): ${skipped.join(', ')}` : ''));
