global.document = { addEventListener: () => {} };
global.window = { addEventListener: () => {} };
const fs = require('fs');
const appSrc = fs.readFileSync('js/app.js', 'utf8');
const { getSectionParagraphsWithTranslations, renderInteractiveParagraphHtml } = new Function(appSrc + '\nreturn { getSectionParagraphsWithTranslations, renderInteractiveParagraphHtml };')();

const dSrc = fs.readFileSync('js/english_12_data.js', 'utf8');
const cleanSrc = dSrc.replace(/if\s*\(typeof\s+DATA[\s\S]*$/, '') + '\nreturn ENGLISH_12_DATA;';
const data = new Function(cleanSrc)();

const u1 = data[0];
console.log('Unit 1 title:', u1.title);
console.log('Unit 1 sections:', u1.sections.length);

const s0 = u1.sections[0];
console.log('\n--- Section 0 heading:', s0.heading);
console.log('--- Section 0 headingUrdu:', s0.headingUrdu);
console.log('--- Section 0 headingPashto:', s0.headingPashto);

const prep = getSectionParagraphsWithTranslations(s0, u1);
console.log('\n======================================');
console.log('P[1] text:\n', prep[1].text);
console.log('P[1] urdu:\n', prep[1].urdu);
console.log('P[1] pashto:\n', prep[1].pashto);

const html1 = renderInteractiveParagraphHtml(prep[1].text, prep[1].urdu, prep[1].pashto, 1);
// Extract data-en, data-ur, data-ps from the HTML
const re = /data-en="([^"]+)"\s+data-ur="([^"]+)"\s+data-ps="([^"]+)"/g;
let match1;
let count1 = 0;
while ((match1 = re.exec(html1)) !== null) {
  count1++;
  console.log(`\nParagraph 2 Sentence ${count1}:`);
  console.log('  EN:', match1[1]);
  console.log('  UR:', match1[2]);
  console.log('  PS:', match1[3]);
}
let match;
let count = 0;
while ((match = re.exec(html)) !== null) {
  count++;
  console.log(`\nSentence ${count}:`);
  console.log('  EN:', match[1]);
  console.log('  UR:', match[2]);
  console.log('  PS:', match[3]);
}
