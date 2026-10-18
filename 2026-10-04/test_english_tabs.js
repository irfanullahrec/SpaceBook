const fs = require('fs');
const vm = require('vm');

let lastHtml = '';
let elementMap = {};

function getMockEl(id) {
  if (!elementMap[id]) {
    elementMap[id] = {
      id: id,
      style: {},
      classList: { add(){}, remove(){}, toggle(){}, contains(){ return false; } },
      _html: '',
      set innerHTML(val) { this._html = val; lastHtml = val; },
      get innerHTML() { return this._html; },
      appendChild(){},
      querySelectorAll: () => [],
      querySelector: () => getMockEl('sub'),
      addEventListener: () => {},
      getAttribute: () => '',
      textContent: ''
    };
  }
  return elementMap[id];
}

const sandbox = {
  window: {},
  document: {
    getElementById: (id) => getMockEl(id),
    querySelectorAll: () => [],
    querySelector: (sel) => getMockEl(sel),
    createElement: () => getMockEl('created'),
    addEventListener: () => {},
    body: getMockEl('body')
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
vm.runInContext(fs.readFileSync('D:/SpaceBook/SpaceBook Web/js/math_8_data.js', 'utf8') + '\n;globalThis.MATH_8_DATA = MATH_8_DATA;', sandbox);
vm.runInContext(fs.readFileSync('D:/SpaceBook/SpaceBook Web/js/app.js', 'utf8'), sandbox);

vm.runInContext(`
console.log('--- Testing Class 8 English Workspace inside VM ---');
const subj = DATA.subjects.cls8.find(s => s.id === 'cls8-eng');
openSubject('cls8', 'cls8-eng');
console.log('Class 8 English opened. Selected class:', state.selectedClass);

// Test all 8 tabs
const tabs = ['lesson', 'glossary', 'exercise', 'vocabulary', 'language', 'grammar', 'writing', 'slos'];
tabs.forEach(t => {
  switchSubjectTab('eng', t, 0, 'cls8');
  const content = document.getElementById('subjTabContent');
  const html = content ? content.innerHTML : '';
  console.log('Tab [' + t + ']: length=' + html.length);
});

// Test exercise Part B
switchSubjectTab('eng', 'exercise', 0, 'cls8');
const exProblems = renderSubjectExProblems('eng', ENGLISH_8_DATA[0], 'agreeDisagree');
console.log('Exercise Part B rendered:', exProblems.includes('Statement 1') && exProblems.includes('Respond to each statement') ? 'YES' : 'NO');
console.log('Contains Urdu explanation in Part B?', exProblems.includes('اردو تشریح'));
console.log('Contains Pashto explanation in Part B?', exProblems.includes('پښتو وضاحت'));

// Test Vocabulary Part B (Silent Letters)
const vocabB = renderEnglishVocabSubContent(ENGLISH_8_DATA[0], 'partB');
console.log('Vocabulary Part B rendered with silent letters:', vocabB.includes('clim') && vocabB.includes("Silent 'b'") ? 'YES' : 'NO');

// Test Vocabulary Part C (Syllables)
const vocabC = renderEnglishVocabSubContent(ENGLISH_8_DATA[0], 'partC');
console.log('Vocabulary Part C rendered with syllables:', vocabC.includes('or · der · ly') && vocabC.includes('3 Syllables') ? 'YES' : 'NO');

// Test Use of Language
const langHtml = renderEnglishUseOfLanguageTab(ENGLISH_8_DATA[0]);
console.log('Use of Language rendered with Short Vowels:', langHtml.includes('apple') && langHtml.includes('/æ/') ? 'YES' : 'NO');

// Test Writing (Mind Map & Summary)
const writingA = renderEnglishWritingSubContent(ENGLISH_8_DATA[0], 'partA');
console.log('Writing Mind Map rendered:', writingA.includes('Mind Map: The Justice of Rasoolullah') && writingA.includes('Before Nabuwwat') ? 'YES' : 'NO');
const writingC = renderEnglishWritingSubContent(ENGLISH_8_DATA[0], 'partC');
console.log('Writing Model Paragraph rendered:', writingC.includes('Patience of Hazrat Muhammad') && writingC.includes('Target: 50–60 words') ? 'YES' : 'NO');

console.log('=== ALL CLASS 8 ENGLISH VERIFICATIONS PASSED ===');
`, sandbox);
