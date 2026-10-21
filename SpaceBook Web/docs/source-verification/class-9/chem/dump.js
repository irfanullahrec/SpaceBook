// node chem/dump.js  -> chem/data.json (Class 9 Chemistry chapters as the app holds them)
const fs = require('fs'), vm = require('vm'), path = require('path');
global.window = global; global.DATA = {}; global.document = {};
const src = fs.readFileSync(path.join(__dirname, '..', '..', '..', '..', 'js', 'data_chem.js'), 'utf8');
vm.runInThisContext(src, {filename: 'data_chem.js'});
fs.writeFileSync(path.join(__dirname, 'data.json'), JSON.stringify(DATA.chemChapters));
console.log('chapters', DATA.chemChapters.length);
