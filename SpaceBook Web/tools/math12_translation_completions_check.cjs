// Focused coverage and preservation checks for the Unit 1 translation overlay.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');

const root = path.resolve(__dirname, '..');
const context = {};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root, 'js/math_12_data.js'), 'utf8') + '\nthis.auditUnits=MATH_12_DATA;this.auditTranslations=MATH12_SENTENCE_TRANSLATIONS;this.auditWords=MATH12_WORD_MEANINGS;', context, { timeout: 15000 });
const unit = context.auditUnits.find(chapter => Number(chapter.number) === 1);
assert(unit, 'Mathematics Unit 1 must load');
const sectionIds = ['sec-1-1', 'sec-1-2', 'sec-1-3', 'sec-1-4'];
const sections = sectionIds.map(id => {
    const section = unit.sections.find(candidate => candidate.id === id);
    assert(section, `Missing reviewed section ${id}`);
    return section;
});
const originalTextAndMath = value => JSON.stringify(value, (key, child) => /sentenceTranslations$/i.test(key) ? undefined : child);
const sourceSnapshot = originalTextAndMath(sections);
const priorPassages = new Map(Object.entries(context.auditTranslations).map(([key, value]) => [key, JSON.stringify(value)]));
const priorWords = new Map(Object.entries(context.auditWords).map(([key, value]) => [key, JSON.stringify(value)]));
const existingBlockTranslations = sections.flatMap(section => section.sourceBlocks.filter(block => block.sentenceTranslations?.length).map(block => ({ block, value: JSON.stringify(block.sentenceTranslations) })));
const overlay = fs.readFileSync(path.join(root, 'js/math12_translation_completions.js'), 'utf8');
new vm.Script(overlay, { filename: 'math12_translation_completions.js' });
vm.runInContext(overlay, context, { timeout: 15000 });

assert.equal(originalTextAndMath(sections), sourceSnapshot, 'Original English, lists, commands, numerical results, matrices and diagrams must remain unchanged');
for (const [key, value] of priorPassages) assert.equal(JSON.stringify(context.auditTranslations[key]), value, `Existing passage changed: ${key}`);
for (const [key, value] of priorWords) assert.equal(JSON.stringify(context.auditWords[key]), value, `Existing cached meaning changed: ${key}`);
for (const { block, value } of existingBlockTranslations) assert.equal(JSON.stringify(block.sentenceTranslations), value, `Existing block translation changed: ${block.text}`);

let coveredFields = 0;
let sentenceRows = 0;
const fieldCheck = (original, rows, description) => {
    assert(Array.isArray(rows) && rows.length > 0, `Missing translation: ${description}`);
    assert.equal(rows.map(row => row.en).join(' '), original, `English alignment failed: ${description}`);
    for (const row of rows) {
        assert(/[\u0600-\u06ff]/.test(row.ur || ''), `Urdu missing: ${description}`);
        assert(/[\u0600-\u06ff]/.test(row.ps || ''), `Pashto missing: ${description}`);
        // Earlier reviewed translations use Unicode powers in some formulas.
        // They are protected byte-for-byte above. New passages preserve the
        // original inline LaTeX literally in both added translations.
        if (!priorPassages.has(original)) for (const math of row.en.match(/\\\([\s\S]*?\\\)/g) || []) {
            assert(row.ur.includes(math), `Urdu altered new inline mathematics: ${description}`);
            assert(row.ps.includes(math), `Pashto altered new inline mathematics: ${description}`);
        }
    }
    coveredFields++;
    sentenceRows += rows.length;
};
for (const section of sections) {
    for (const block of section.sourceBlocks) {
        if (['heading', 'paragraph', 'clarification'].includes(block.type)) fieldCheck(block.text, block.sentenceTranslations, `${section.id} / ${block.text}`);
        if (block.type === 'list') (block.items || []).forEach((item, index) => {
            if (typeof item === 'string') fieldCheck(item, block.itemSentenceTranslations?.[index], `${section.id} / list item ${index}`);
        });
        if (['figure', 'diagram'].includes(block.type)) {
            if (block.caption) fieldCheck(block.caption, block.captionSentenceTranslations, `${section.id} / ${block.caption}`);
            if (block.alt) fieldCheck(block.alt, block.altSentenceTranslations, `${section.id} / ${block.alt}`);
        }
    }
}
const firstReport = JSON.parse(JSON.stringify(context.MATH12_TRANSLATION_COMPLETIONS_REPORT));
assert.equal(firstReport.sections.length, 4);
assert(firstReport.sections.every(section => section.missing.length === 0), 'Every owned reviewed text field must be covered');
const firstLoad = JSON.stringify(sections);
const firstPassages = JSON.stringify(context.auditTranslations);
const firstWords = JSON.stringify(context.auditWords);
vm.runInContext(overlay, context, { timeout: 15000 });
assert.equal(JSON.stringify(sections), firstLoad, 'Loading the overlay twice must not change block data');
assert.equal(JSON.stringify(context.auditTranslations), firstPassages, 'Loading twice must not change the translation cache');
assert.equal(JSON.stringify(context.auditWords), firstWords, 'Loading twice must not change vocabulary');

console.log(JSON.stringify({ passed: true, scope: firstReport.scope, coveredFields, sentenceRows, report: firstReport }, null, 2));
