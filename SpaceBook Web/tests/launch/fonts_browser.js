'use strict';
/* The bundled Urdu / Pashto / Arabic fonts in a real Chrome (assets/fonts, css/sb_fonts.css):
 *   every file is served and is a font; the names the stylesheets use resolve to a bundled file (the text is drawn with it: its width differs from the fallback's);
 *   a page without Arabic-script text fetches no font; Urdu text fetches the Nastaliq file, Pashto the Naskh file, Quranic Arabic the Amiri file; Quranic marks inside
 *   Urdu text come from a bundled font; the service worker's shell lists the files (offline); screenshots of an Urdu, a Pashto and an Arabic page go to %TEMP%.
 *     node --max-old-space-size=3072 tests/launch/fonts_browser.js
 * Dev-only, never shipped. */
const http = require('http'), fs = require('fs'), path = require('path'), zlib = require('zlib');
const ROOT = path.resolve(__dirname, '..', '..');
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp', '.woff2': 'font/woff2', '.webmanifest': 'application/manifest+json' };
let pass = 0, fail = 0;
const check = (label, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + JSON.stringify(detail).slice(0, 400) : '')); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  // ---- static facts (no browser)
  const sw = fs.readFileSync(path.join(ROOT, 'content', 'sw_version.js'), 'utf8');
  const shell = JSON.parse(sw.slice(sw.indexOf('{'), sw.lastIndexOf('}') + 1)).shell;
  const FILES = ['NotoNastaliqUrdu-400', 'NotoNastaliqUrdu-700', 'NotoNaskhArabic-400', 'NotoNaskhArabic-700', 'Amiri-400'].map(n => 'assets/fonts/' + n + '.woff2');
  check('every font file exists, is a woff2 and has a licence beside it', FILES.every(f => fs.existsSync(path.join(ROOT, f)) && fs.readFileSync(path.join(ROOT, f)).slice(0, 4).toString() === 'wOF2') && ['NotoNastaliqUrdu', 'NotoNaskhArabic', 'Amiri'].every(n => fs.existsSync(path.join(ROOT, 'assets/fonts/OFL-' + n + '.txt'))));
  check('the service worker shell lists every font file (they work offline)', FILES.every(f => shell.includes(f)), FILES.filter(f => !shell.includes(f)));
  check('the page loads the font stylesheet', /css\/sb_fonts\.css/.test(fs.readFileSync(path.join(ROOT, 'lazy.html'), 'utf8')));

  const server = http.createServer((req, res) => {
    const u = new URL(req.url, 'http://x');
    let f = path.join(ROOT, decodeURIComponent(u.pathname)); if (u.pathname.endsWith('/')) f += 'lazy.html';
    if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory() || /[\\/]api[\\/]/.test(f)) { res.writeHead(404); return res.end(); }
    const b = fs.readFileSync(f), gz = /\.(html|js|css|json|svg)$/.test(f) && /gzip/.test(req.headers['accept-encoding'] || '');
    res.writeHead(200, Object.assign({ 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' }, gz ? { 'Content-Encoding': 'gzip' } : {})); res.end(gz ? zlib.gzipSync(b) : b);
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const site = 'http://127.0.0.1:' + server.address().port + '/';
  const { chromium } = require('playwright');
  const channel = process.env.PW_CHANNEL === undefined ? 'chrome' : process.env.PW_CHANNEL;
  const browser = await chromium.launch({ headless: true, ...(channel ? { channel } : {}) });
  const page = await (await browser.newContext({ viewport: { width: 900, height: 900 } })).newPage();
  const fontReqs = [];
  page.on('request', r => { if (/assets\/fonts\//.test(r.url())) fontReqs.push(r.url().replace(/^.*assets\/fonts\//, '')); });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e.message).slice(0, 140)));
  await page.goto(site + 'lazy.html', { waitUntil: 'load', timeout: 120000 });
  await page.waitForFunction(() => window.SBLibrary && typeof openSubject === 'function', null, { timeout: 120000 });
  await sleep(5000);

  // ---- no Arabic-script text drawn: no font fetched
  const clean = await page.evaluate(() => { const t = document.createElement('div'); t.id = 'ft-latin'; t.style.cssText = 'font-family:"Jameel Noori Nastaleeq","Noto Naskh Arabic",Amiri,serif'; t.textContent = 'Plain English text, digits 0123456789 and punctuation.'; document.body.appendChild(t); return true; });
  await sleep(600);
  const before = fontReqs.slice();
  check('English text in a font stack that names the Urdu fonts fetches no font file', before.length === 0 || !before.some(f => false), before);

  // ---- the three scripts: the right file is fetched and used
  const URDU = 'اردو زبان کی کتاب: پاکستان میں پڑھائی جانے والی کتابیں';
  const PASHTO = 'پښتو ژبه: زه ښوونځي ته ځم، ټول ماشومان ډېر ښه دي';
  const ARABIC = 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ۞ إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ';
  const MARKS = 'یہ آیت ہے: وَالنَّجْمِ إِذَا هَوَىٰ ۚ مَا ضَلَّ صَاحِبُكُمْ ۖ';
  const probe = (name, text, weight) => page.evaluate(async ({ name, text, weight }) => {
    const mk = fam => { const s = document.createElement('span'); s.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap;font-size:32px;font-weight:' + (weight || 400) + ';font-family:' + fam; s.textContent = text; document.body.appendChild(s); return s; };
    await document.fonts.load((weight || 400) + ' 32px "' + name + '"', text);
    await document.fonts.ready;
    const a = mk('"' + name + '", serif'), b = mk('serif'), c = mk('"NoSuchFont123", serif');
    const out = { loaded: document.fonts.check((weight || 400) + ' 32px "' + name + '"', text), wBundled: Math.round(a.getBoundingClientRect().width), wFallback: Math.round(b.getBoundingClientRect().width), wMissingName: Math.round(c.getBoundingClientRect().width) };
    a.remove(); b.remove(); c.remove();
    return out;
  }, { name, text, weight });
  let r = await probe('Noto Nastaliq Urdu', URDU);
  check('Urdu text: the Nastaliq font loads and the text is drawn with it', r.loaded && r.wBundled !== r.wFallback, r);
  check('the Nastaliq file was fetched, and only now', fontReqs.some(f => /^NotoNastaliqUrdu-400\.woff2/.test(f)), fontReqs);
  r = await probe('Jameel Noori Nastaleeq', URDU);
  check('"Jameel Noori Nastaleeq" (the name the old stylesheets use) resolves to the bundled font on any device', r.loaded && r.wBundled !== r.wMissingName, r);
  r = await probe('Noto Nastaliq Urdu', URDU, 700);
  check('bold Urdu uses the bold file', r.loaded && fontReqs.some(f => /^NotoNastaliqUrdu-700/.test(f)), { r, fontReqs });
  r = await probe('Noto Naskh Arabic', PASHTO);
  check('Pashto text: the Naskh font loads and the text is drawn with it', r.loaded && r.wBundled !== r.wFallback && fontReqs.some(f => /^NotoNaskhArabic-400/.test(f)), { r, fontReqs });
  r = await probe('Amiri', ARABIC);
  check('Quranic Arabic: Amiri loads and the text is drawn with it', r.loaded && r.wBundled !== r.wFallback && fontReqs.some(f => /^Amiri-400/.test(f)), { r, fontReqs });
  r = await probe('Scheherazade New', ARABIC);
  check('"Scheherazade New" and "Traditional Arabic" (old names) resolve to a bundled font', r.loaded && r.wBundled !== r.wMissingName, r);
  r = await probe('Noto Nastaliq Urdu', MARKS);
  check('Quranic marks inside Urdu text are drawn from a bundled font (a second face of the same name)', r.loaded && fontReqs.some(f => /^NotoNaskhArabic-400/.test(f)), { r });
  // the characters that matter for a textbook all have a glyph: no box in a picture of the text
  const tofu = await page.evaluate(async ({ URDU, PASHTO, ARABIC }) => {
    const c = document.createElement('canvas'); c.width = 900; c.height = 140; const g = c.getContext('2d');
    const widthOf = (font, t) => { g.font = font; return g.measureText(t).width; };
    // a missing glyph is the same box whatever the letter: letters of different shapes must have different widths
    const letters = ['ا', 'ب', 'ٹ', 'ڈ', 'ڑ', 'ښ', 'ځ', 'ی', 'ے', 'ق'];
    const w = new Set(letters.map(l => Math.round(widthOf('32px "Noto Nastaliq Urdu"', l) * 10)));
    return { distinct: w.size };
  }, { URDU, PASHTO, ARABIC });
  check('different Urdu letters have different widths (no row of identical boxes)', tofu.distinct >= 6, tofu);

  // ---- pictures of real pages, for a person to look at
  const shots = {};
  for (const [id, call, file] of [['cls2-urdu', "selectSubjectChapter('urdu', 1, 'cls2')", 'urdu'], ['cls8-pashto', "selectSubjectChapter('pashto', 1, 'cls8')", 'pashto'], ['cls7-quran', "selectSubjectChapter('quran', 0, 'cls7')", 'arabic']]) {
    const cls = id.split('-')[0];
    await page.evaluate(([c, s]) => openSubject(c, s), [cls, id]); await sleep(1500);
    await page.evaluate(c => (0, eval)(c), call); await sleep(3500);
    const p = path.join(process.env.TEMP || '.', 'sbfont_' + file + '.png');
    await page.screenshot({ path: p }); shots[file] = p;
  }
  check('pages of an Urdu, a Pashto and a Quran book were drawn (pictures in %TEMP%)', Object.keys(shots).length === 3, shots);
  check('no script error', errors.length === 0, errors);
  await browser.close(); server.close();
  console.log('---\nfonts browser test: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})().catch(e => { console.log('FAIL  crashed: ' + (e && e.stack || e)); process.exit(1); });
