const fs = require('fs');
const vm = require('vm');

let lastHtml = '';
const mockEl = () => ({
  style: {},
  classList: { add(){}, remove(){}, toggle(){}, contains(){ return false; } },
  set innerHTML(val) { lastHtml = val; },
  get innerHTML() { return lastHtml; },
  appendChild(){},
  querySelectorAll: () => [],
  addEventListener: () => {}
});

const sandbox = {
  window: {},
  document: {
    getElementById: () => mockEl(),
    querySelectorAll: () => [],
    querySelector: () => mockEl(),
    createElement: () => mockEl(),
    addEventListener: () => {},
    body: mockEl()
  },
  console: console,
  setTimeout: (fn) => fn(),
  clearTimeout: () => {},
  setInterval: () => {},
  clearInterval: () => {}
};
sandbox.window = sandbox;
sandbox.window.addEventListener = () => {};

vm.createContext(sandbox);

vm.runInContext(fs.readFileSync('D:/SpaceBook/SpaceBook Web/js/data.js', 'utf8') + '\n;globalThis.DATA = DATA;', sandbox);
vm.runInContext(fs.readFileSync('D:/SpaceBook/SpaceBook Web/js/english_8_data.js', 'utf8') + '\n;globalThis.ENGLISH_8_DATA = ENGLISH_8_DATA;', sandbox);
vm.runInContext(fs.readFileSync('D:/SpaceBook/SpaceBook Web/js/app.js', 'utf8'), sandbox);

console.log('--- Testing goToSubjects("cls8") ---');
sandbox.goToSubjects('cls8');
console.log('HTML generated length:', lastHtml.length);
console.log('Contains "Class 8 — Subjects"?', lastHtml.includes('Class 8'));
console.log('Contains "English"?', lastHtml.includes('English'));
console.log('Contains "Subjects Not Uploaded Yet"?', lastHtml.includes('Subjects Not Uploaded Yet'));

console.log('--- Testing openSubject("cls8", "cls8-eng") ---');
sandbox.openSubject('cls8', 'cls8-eng');
console.log('Subject workspace HTML generated length:', lastHtml.length);
console.log('Contains "The Justice of Rasoolullah"?', lastHtml.includes('The Justice of Rasoolullah'));
console.log('Contains "Translations"?', lastHtml.includes('Translations'));
