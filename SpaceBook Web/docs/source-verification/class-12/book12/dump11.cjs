'use strict';
/* Dumps a Class 11 book's page-by-page source records (js/<name>_11_data.js) whole, as JSON, for engine11.py.
 *   node dump11.cjs <data file in js/> <GLOBAL name> <out.json> */
const fs = require('fs'), path = require('path'), vm = require('vm');
const ROOT = path.resolve(__dirname, '..', '..', '..', '..');
const [dataFile, glob, out] = process.argv.slice(2);
const sb = {window: {}, console};
vm.createContext(sb);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'js', dataFile), 'utf8') + `\n;this.__D = ${glob};`, sb, {filename: dataFile});
const D = JSON.parse(JSON.stringify(sb.__D));
fs.mkdirSync(path.dirname(path.resolve(out)), {recursive: true});
fs.writeFileSync(out, JSON.stringify(D));
console.log(glob, 'chapters', D.length, 'sections', D.reduce((n, c) => n + (c.sections || []).length, 0));
