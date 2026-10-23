'use strict';
/* Keeps the website and the Android app the same product. Reads docs/parity.json (the machine-readable twin of docs/PARITY_MATRIX.md) and checks it
 * against the code of both platforms:
 *     node tools/parity/check.js [--app "<folder of the app repo>"] [--write-matrix]
 *   - every feature has an id, an area, a status from the list, and what each platform does about it;
 *     `web-only`, `app-only`, `partial` and `blocked` need a written exemption (why, and what the counterpart will be);
 *     `platform-specific` names its counterpart; `same` names both implementations; `retired` says since when and why
 *   - the endpoints the app calls (ApiService.kt) all exist on the server and are exactly the list in parity.json
 *   - the sync event types the server accepts (api/v2/sync.php) are the list in parity.json, and every type the website (js/) or the app
 *     (Kotlin) sends is one of them
 *   - the user item kinds (api/lib/items.php) are the list in parity.json, with who writes each
 *   - every migration has a down script (except the baseline) and is named in a PHP test
 *   - docs/PARITY_MATRIX.md is the table made from parity.json (--write-matrix rewrites it); a hand-edited matrix fails
 * Where the app folder is absent (CI checks out this repository only) the checks of the app's own files are skipped and say so.
 * Dev-only, never deployed. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const args = process.argv.slice(2);
const APP = path.resolve(args.includes('--app') ? args[args.indexOf('--app') + 1] : path.join(ROOT, '..', 'SpaceBook App'));
const KOTLIN = path.join(APP, 'app', 'src', 'main', 'java');
const HAVE_APP = fs.existsSync(KOTLIN);
const WRITE = args.includes('--write-matrix');

let pass = 0, fail = 0;
const check = (label, ok, detail) => { if (ok) { pass++; console.log('PASS  ' + label); } else { fail++; console.log('FAIL  ' + label + (detail !== undefined ? '  -> ' + (typeof detail === 'string' ? detail : JSON.stringify(detail)).slice(0, 700) : '')); } };
const read = f => fs.readFileSync(path.join(ROOT, f), 'utf8');
const walk = (dir, rx, out = []) => { for (const e of fs.existsSync(dir) ? fs.readdirSync(dir, { withFileTypes: true }) : []) { const p = path.join(dir, e.name); if (e.isDirectory()) { if (e.name !== 'node_modules') walk(p, rx, out); } else if (rx.test(e.name)) out.push(p); } return out; };
const sameSet = (a, b) => JSON.stringify([...new Set(a)].sort()) === JSON.stringify([...new Set(b)].sort());
const diffSets = (a, b) => ({ onlyInCode: a.filter(x => !b.includes(x)), onlyInParityJson: b.filter(x => !a.includes(x)) });

const P = JSON.parse(read('docs/parity.json'));
console.log('--- docs/parity.json ---');

// ---- features
const STATUS = P.statuses;
check('the status list is the documented one', sameSet(STATUS, ['same', 'platform-specific', 'web-only', 'app-only', 'partial', 'blocked', 'retired']), STATUS);
const ids = P.features.map(f => f.id);
check(`${P.features.length} features, ids unique`, new Set(ids).size === ids.length, ids.filter((x, i) => ids.indexOf(x) !== i));
const bad = [];
for (const f of P.features) {
  const need = (k, min) => { if (typeof f[k] !== 'string' || f[k].trim().length < (min || 3)) bad.push(`${f.id}: needs "${k}"`); };
  need('area'); need('name');
  if (!STATUS.includes(f.status)) { bad.push(`${f.id}: unknown status ${f.status}`); continue; }
  if (f.status === 'same') { need('web'); need('app'); need('data'); }
  if (f.status === 'platform-specific') { need('web', 1); need('app', 1); need('counterpart', 12); }
  if (['web-only', 'app-only', 'partial', 'blocked'].includes(f.status)) need('exemption', 40);
  if (f.status === 'retired') need('exemption', 40);
  if (f.status === 'blocked') need('ownerDecision', 12);
}
check('every feature says what each platform does, and every web-only / app-only / partial / blocked / retired row has a written exemption', bad.length === 0, bad.slice(0, 8));
const open = P.features.filter(f => ['web-only', 'app-only', 'partial', 'blocked'].includes(f.status));
console.log(`      ${P.features.filter(f => f.status === 'same').length} same, ${P.features.filter(f => f.status === 'platform-specific').length} platform-specific, ${P.features.filter(f => f.status === 'retired').length} retired, ${open.length} with an exemption: ${open.map(f => f.id + ' (' + f.status + ')').join(', ') || 'none'}`);

// ---- endpoints
console.log('--- endpoints ---');
const serverFiles = [...walk(path.join(ROOT, 'api'), /\.php$/)].map(f => path.relative(path.join(ROOT, 'api'), f).replace(/\\/g, '/')).filter(f => !/^(lib|migrations)\//.test(f) && !/^(db|session|migrate|config|config\.sample)\.php$/.test(f));
check('the server endpoints are the list in parity.json', sameSet(serverFiles, P.endpoints.server), diffSets(serverFiles, P.endpoints.server));
const appEndpoints = new Set();
if (HAVE_APP) {
  const api = walk(KOTLIN, /ApiService\.kt$/)[0];
  const src = api ? fs.readFileSync(api, 'utf8') : '';
  for (const m of src.matchAll(/@(GET|POST)\("([^"]+)"\)/g)) appEndpoints.add(m[1] + ' ' + m[2]);
  const list = [...appEndpoints];
  check(`the app's ${list.length} calls (ApiService.kt) are the list in parity.json`, sameSet(list, P.endpoints.app), diffSets(list, P.endpoints.app));
  const missing = list.filter(e => { const p = e.split(' ')[1].split('?')[0]; return p.startsWith('api/') ? !serverFiles.includes(p.replace(/^api\//, '')) : !fs.existsSync(path.join(ROOT, p)); });
  check('every call the app makes exists on the server (or is a published file)', missing.length === 0, missing);
} else console.log('SKIP  the app folder is not here: ApiService.kt was not read');

// ---- sync events
console.log('--- sync events ---');
const syncPhp = read('api/v2/sync.php');
const body = syncPhp.slice(syncPhp.indexOf('function sync_apply'), syncPhp.indexOf('$accepted = []'));
const serverEvents = [...body.matchAll(/case '([a-z.]+)':/g)].map(m => m[1]);
check('the event types the server accepts are the list in parity.json', sameSet(serverEvents, P.syncEvents.server), diffSets(serverEvents, P.syncEvents.server));
const webEvents = new Set();
for (const f of walk(path.join(ROOT, 'js'), /\.js$/)) {
  if (/_data\.js$|lexicon_data|word_stats_words|test_prep_bank|study_plan_index/.test(f)) continue;
  for (const m of fs.readFileSync(f, 'utf8').matchAll(/\bemit(?:Latest)?\(\s*['"]([a-z]+(?:\.[a-z]+)*)['"]/g)) webEvents.add(m[1]);
}
const webList = [...webEvents];
check('every event type the website sends is one the server accepts, and they are the list in parity.json', webList.every(e => serverEvents.includes(e)) && sameSet(webList, P.syncEvents.web), { sends: webList, listed: P.syncEvents.web });
if (HAVE_APP) {
  const kt = walk(KOTLIN, /\.kt$/);
  const appEvents = new Set();
  for (const f of kt) {
    const s = fs.readFileSync(f, 'utf8');
    for (const m of s.matchAll(/\bemit\(\s*"([a-z.]+)"/g)) appEvents.add(m[1]);
    for (const m of s.matchAll(/"(item\.put|item\.del)"/g)) appEvents.add(m[1]);
  }
  const al = [...appEvents];
  check('every event type the app sends is one the server accepts, and they are the list in parity.json', al.every(e => serverEvents.includes(e)) && sameSet(al, P.syncEvents.app), { sends: al, listed: P.syncEvents.app });
}

// ---- user items
console.log('--- user items ---');
const items = read('api/lib/items.php');
const kinds = [...items.slice(items.indexOf('function sb_item_kinds')).matchAll(/^\s{8}'([a-z]+)' => \[/gm)].map(m => m[1]);
check('the item kinds the server stores are the list in parity.json', sameSet(kinds, Object.keys(P.itemKinds)), diffSets(kinds, Object.keys(P.itemKinds)));
const itemBad = [];
for (const [k, v] of Object.entries(P.itemKinds)) {
  if (!v.what || !v.web || !v.app) itemBad.push(k + ': needs what, web and app');
  if (v.web !== '-' && v.web && !/\b(sb_library|items|word_stats|sb_games|sb_bise|continue_learning)\b/.test(v.web)) itemBad.push(k + ': web names no module');
}
check('every item kind says what it is and which module of each platform writes it', itemBad.length === 0, itemBad);
const webKinds = new Set();
for (const f of walk(path.join(ROOT, 'js'), /\.js$/)) {
  if (/_data\.js$|lexicon_data|word_stats_words|test_prep_bank|study_plan_index/.test(f)) continue;
  for (const m of fs.readFileSync(f, 'utf8').matchAll(/(?:\bI\(\)|\bI|SBItems|window\.SBItems)\.(?:put|del|adopt)\(\s*'([a-z]+)'/g)) webKinds.add(m[1]);
}
const declaredWeb = Object.entries(P.itemKinds).filter(([, v]) => v.web !== '-').map(([k]) => k);
check('every item kind the website writes is declared, and each declared one is written by the website', [...webKinds].every(k => kinds.includes(k)) && declaredWeb.every(k => webKinds.has(k)), { written: [...webKinds], declared: declaredWeb });
if (HAVE_APP) {
  const lib = walk(KOTLIN, /ItemCodec\.kt$|LibraryItems\.kt$/)[0];
  const ls = lib ? fs.readFileSync(lib, 'utf8') : '';
  const appKinds = [...ls.matchAll(/const val (?:BM|NOTE|POS|PREF) = "([a-z]+)"/g)].map(m => m[1]);
  const declaredApp = Object.entries(P.itemKinds).filter(([, v]) => v.app !== '-').map(([k]) => k);
  check('the item kinds the app keeps in its database are the ones parity.json declares for it', sameSet(appKinds, declaredApp), diffSets(appKinds, declaredApp));
}

// ---- migrations
console.log('--- migrations ---');
const migs = fs.readdirSync(path.join(ROOT, 'api', 'migrations')).filter(f => /^\d{3}_[a-z0-9_]+\.sql$/.test(f) && !/\.down\.sql$/.test(f));
const tests = walk(path.join(ROOT, 'tests', 'php'), /\.php$/).map(f => fs.readFileSync(f, 'utf8')).join('\n');
const noDown = migs.filter(f => !/^001_/.test(f) && !fs.existsSync(path.join(ROOT, 'api', 'migrations', f.replace(/\.sql$/, '.down.sql'))));
check(`all ${migs.length} migrations have a down script (the baseline excepted)`, noDown.length === 0, noDown);
const untested = migs.filter(f => !/^001_/.test(f) && !tests.includes(f));
check('every migration is named in a PHP test (tests/php)', untested.length === 0, untested);

// ---- the matrix document
console.log('--- docs/PARITY_MATRIX.md ---');
const md = matrix();
const mdFile = path.join(ROOT, 'docs', 'PARITY_MATRIX.md');
if (WRITE) { fs.writeFileSync(mdFile, md); console.log('wrote docs/PARITY_MATRIX.md'); }
const have = fs.existsSync(mdFile) ? fs.readFileSync(mdFile, 'utf8').replace(/\r\n/g, '\n') : '';
check('docs/PARITY_MATRIX.md is the table made from parity.json (node tools/parity/check.js --write-matrix)', have === md);

console.log(`---\nparity check: ${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);

function matrix() {
  const esc = s => String(s == null ? '' : s).replace(/\|/g, '\\|').replace(/\n/g, ' ');
  const out = [];
  out.push('# Web / App parity matrix', '');
  out.push('Generated from `docs/parity.json` by `node tools/parity/check.js --write-matrix`. **Do not edit this file**: change the JSON, run the command, commit both.');
  out.push('The product is one: SpaceBook Web (`SpaceBook Web/`) and SpaceBook App (`SpaceBook App/`, its own repository) have the same functions, the same data and one database (`tafseelk_spacebook`, reached only through the PHP API); only the user interface differs. Rules: `D:\\SpaceBook\\CLAUDE.md`.', '');
  out.push('Status: **same** (one implementation or two with identical data and rules) · **platform-specific** (each platform does it its own way for a reason of the platform, the counterpart is named) · **web-only / app-only / partial / blocked** (open: each carries a written reason and what is planned) · **retired** (was there, is not reachable or wanted any more).', '');
  const areas = [...new Set(P.features.map(f => f.area))];
  for (const a of areas) {
    out.push('## ' + a, '', '| id | Feature | Web | App | Data lives in | Status |', '|---|---|---|---|---|---|');
    for (const f of P.features.filter(x => x.area === a)) {
      const st = f.status + (f.exemption ? ' ⚠' : '');
      out.push(`| ${f.id} | ${esc(f.name)} | ${esc(f.web)} | ${esc(f.app)} | ${esc(f.data)} | ${st} |`);
    }
    out.push('');
  }
  const flagged = P.features.filter(f => f.exemption || f.counterpart);
  out.push('## Why a row is not plainly "same"', '');
  for (const f of flagged) out.push(`- **${f.id} ${esc(f.name)}** (${f.status}): ${esc(f.exemption || f.counterpart)}${f.ownerDecision ? ' **Owner decision:** ' + esc(f.ownerDecision) : ''}`);
  out.push('', '## Exemptions in the data', '');
  for (const e of P.catalogExemptions) out.push(`- ${e.subjects.join(', ')}: ${esc(e.reason)}${e.ownerDecision ? ' **Owner decision:** ' + esc(e.ownerDecision) : ''}`);
  out.push('', '## One database, the same rules', '');
  out.push('Endpoints the server publishes: ' + P.endpoints.server.map(e => '`' + e + '`').join(', ') + '.', '');
  out.push('Endpoints the app calls: ' + P.endpoints.app.map(e => '`' + e + '`').join(', ') + '.', '');
  out.push('Sync events (`api/v2/sync.php`): accepted ' + P.syncEvents.server.map(e => '`' + e + '`').join(', ') + '; the website sends ' + P.syncEvents.web.map(e => '`' + e + '`').join(', ') + '; the app sends ' + P.syncEvents.app.map(e => '`' + e + '`').join(', ') + '.', '');
  out.push('| item kind | What | Website | App |', '|---|---|---|---|');
  for (const [k, v] of Object.entries(P.itemKinds)) out.push(`| \`${k}\` | ${esc(v.what)} | ${esc(v.web)} | ${esc(v.app)} |`);
  out.push('', '## The owner\'s sync switch', '', esc(P.syncSwitch), '', '## Open owner decisions', '');
  for (const d of P.ownerDecisions) out.push('- ' + esc(d));
  out.push('');
  return out.join('\n');
}
