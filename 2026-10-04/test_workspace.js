const fs = require('fs');
const vm = require('vm');

let areas = {};
const mockEl = (id = 'main') => ({
  style: {},
  classList: { add(){}, remove(){}, toggle(){}, contains(){ return false; } },
  set innerHTML(val) { areas[id] = val; },
  get innerHTML() { return areas[id] || ''; },
  appendChild(){},
  querySelectorAll: () => [],
  addEventListener: () => {}
});

const sandbox = {
  window: {
    addEventListener: () => {}
  },
  document: {
    getElementById: (id) => mockEl(id),
    querySelectorAll: () => [],
    querySelector: () => mockEl(),
    createElement: () => mockEl(),
    addEventListener: () => {},
    body: mockEl()
  },
  console: console,
  pageContent: () => mockEl('pageContent'),
  $: (id) => mockEl(id),
  setTimeout: (fn) => fn(),
  clearTimeout: () => {},
  setInterval: () => {},
  clearInterval: () => {}
};
sandbox.window = sandbox;
sandbox.addEventListener = () => {};

vm.createContext(sandbox);
vm.runInContext(fs.readFileSync('D:/SpaceBook/SpaceBook Web/js/data.js', 'utf8') + '\n;globalThis.DATA = DATA;', sandbox);
vm.runInContext(fs.readFileSync('D:/SpaceBook/SpaceBook Web/js/english_8_data.js', 'utf8') + '\n;globalThis.ENGLISH_8_DATA = ENGLISH_8_DATA;', sandbox);
vm.runInContext(fs.readFileSync('D:/SpaceBook/SpaceBook Web/js/app.js', 'utf8'), sandbox);

sandbox.openSubject('cls8', 'cls8-eng');
console.log('Areas populated:', Object.keys(areas));
console.log('pageContent has "CHAPTERS":', (areas['pageContent'] || '').includes('CHAPTERS'));
console.log('pageContent has "The Justice of Rasoolullah":', (areas['pageContent'] || '').includes('The Justice of Rasoolullah'));
console.log('subjectTopicArea has "The Justice of Rasoolullah":', (areas['subjectTopicArea'] || '').includes('The Justice of Rasoolullah'));
console.log('subjTabContent has "Nida: Asalam-o-Aliakum":', (areas['subjTabContent'] || '').includes('Nida: Asalam-o-Aliakum'));
console.log('subjTabContent length:', (areas['subjTabContent'] || '').length);
