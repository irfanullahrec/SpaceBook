const fs = require('fs');
const src = fs.readFileSync('js/app.js', 'utf8');
global.document = { addEventListener: () => {}, querySelector: () => null, querySelectorAll: () => [] };
global.window = { addEventListener: () => {}, speechSynthesizer: null };
const fn = new Function(src + '\nreturn { getSectionParagraphsWithTranslations, renderInteractiveParagraphHtml, splitSentenceText };');
const { getSectionParagraphsWithTranslations, renderInteractiveParagraphHtml, splitSentenceText } = fn();

const sec = {
  paras: [
    'There is indeed a good model for you in the Messenger of Allah- for the one who has hope in Allah and the last Day, and (who) remembers Allah profusely. Al-Ahzab, verse 21.'
  ],
  urdu: 'یقیناً تمہارے لیے اللہ کے رسول میں بہترین نمونہ ہے، اس شخص کے لیے جو اللہ اور یوم آخرت کی امید رکھتا ہو اور اللہ کو کثرت سے یاد کرتا ہو۔ الاحزاب، آیت 21۔',
  pashto: 'په حقیقت کې ستاسو لپاره په رسول الله صلی الله علیه وسلم کې ښه نمونه ده، د هغه چا لپاره چې په الله او د قیامت په ورځ هیله لري او د الله ډېر ذکر کوي. الاحزاب، ۲۱ آیت.'
};

const prep = getSectionParagraphsWithTranslations(sec);
console.log('Prepared paras count:', prep.length);
console.log('Para 0 text:', prep[0].text);
console.log('Para 0 urdu:', prep[0].urdu);
console.log('Para 0 pashto:', prep[0].pashto);

const html = renderInteractiveParagraphHtml(prep[0].text, prep[0].urdu, prep[0].pashto, 0);
console.log('--- Rendered HTML sample ---');
console.log(html);
