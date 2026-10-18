// inspect a *_data.js file: node tools/inspect_data.js <file> <varname>
const fs = require('fs');
const path = require('path');
const file = process.argv[2];
const varname = process.argv[3];
const src = fs.readFileSync(path.resolve(file), 'utf8');
const fn = new Function(src + '\n;return typeof ' + varname + " !== 'undefined' ? " + varname + ' : (typeof DATA !== "undefined" ? DATA : null);');
const data = fn();
if (!data) { console.log('no var found'); process.exit(1); }
const arr = Array.isArray(data) ? data : null;
if (arr) {
  console.log('chapters:', arr.length);
  const ch = arr[0];
  console.log('ch keys:', Object.keys(ch).join(', '));
  for (const k of Object.keys(ch)) {
    const v = ch[k];
    if (Array.isArray(v)) console.log('  ', k, 'len', v.length);
    else if (v && typeof v === 'object') console.log('  ', k, 'keys', Object.keys(v).join(','));
    else console.log('  ', k, '=', String(v).slice(0, 80));
  }
  if (Array.isArray(ch.sections) && ch.sections[0]) {
    console.log('sec keys:', Object.keys(ch.sections[0]).join(', '));
  }
  if (ch.exercise) {
    for (const k of Object.keys(ch.exercise)) {
      const v = ch.exercise[k];
      if (Array.isArray(v)) console.log('exercise.' + k, 'len', v.length, v[0] ? JSON.stringify(v[0]).slice(0, 200) : '');
    }
  }
  console.log('--- per-chapter section counts ---');
  arr.forEach((c, i) => console.log(i, (c.title || c.name || '').slice(0, 45), '| sections:', (c.sections || []).length, '| text:', Array.isArray(c.textbookText) ? c.textbookText.length : 0));
} else {
  console.log('keys:', Object.keys(data).join(', '));
}
