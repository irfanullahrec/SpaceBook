// Verify the exact Unit 8 sections currently completed by the translation addon.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const context = {};
vm.createContext(context);
const run = name => vm.runInContext(fs.readFileSync(path.join(root, name), 'utf8'), context, { filename: name, timeout: 15000 });
run('js/math_12_data.js');
run('js/math12_translation_completions.js');
vm.runInContext('this.units=MATH_12_DATA;this.translations=MATH12_SENTENCE_TRANSLATIONS;', context);
const unit = context.units.find(chapter => chapter.number === 8);
const stripTranslations = (key, value) => /sentenceTranslations$/i.test(key) ? undefined : value;
const original = JSON.stringify(unit, stripTranslations);
const priorPassages = Object.fromEntries(Object.entries(context.translations).map(([key, value]) => [key, JSON.stringify(value)]));
run('js/math12_unit8_translations.js');
const report = JSON.parse(JSON.stringify(context.MATH12_UNIT8_TRANSLATION_REPORT));
assert.equal(JSON.stringify(unit, stripTranslations), original, 'Original English, mathematical expressions, commands, tables and figures must remain unchanged');
for (const [key, value] of Object.entries(priorPassages)) assert.equal(JSON.stringify(context.translations[key]), value, `Previously authored translation overwritten: ${key}`);
const completed = report.completedSectionIds;
assert.deepEqual(completed, Array.from(unit.sections.slice(0, completed.length), section => section.id), 'Completed source sections must be sequential');
const pending = unit.sections.slice(completed.length).map(section => section.id);
assert.equal(report.nextSection, pending[0] || null, 'Checkpoint must identify the actual next unfinished section');
assert(report.sections.every(section => section.missing.length === 0), JSON.stringify(report.sections));
let verifiedFields = 0;
const check = (originalText, rows, field) => {
    assert(Array.isArray(rows) && rows.length, `Missing translation: ${field}`);
    assert.equal(rows.map(row => row.en).join(' '), originalText, `English alignment failed: ${field}`);
    for (const row of rows) {
        if (row.mathematicalNotation) {
            assert.equal(row.ur, row.en);
            assert.equal(row.ps, row.en);
        } else {
            assert(/[\u0600-\u06ff]/.test(row.ur || ''), `Urdu missing: ${field}`);
            assert(/[\u0600-\u06ff]/.test(row.ps || ''), `Pashto missing: ${field}`);
        }
        for (const expression of row.en.match(/\\\([\s\S]*?\\\)/g) || []) {
            assert(row.ur.includes(expression), `Urdu altered mathematics: ${field}`);
            assert(row.ps.includes(expression), `Pashto altered mathematics: ${field}`);
        }
    }
    verifiedFields++;
};
const proseCell = text => typeof text === 'string' && /[A-Za-z]{2,}/.test(text.replace(/\\\([\s\S]*?\\\)/g, ''));
for (const section of unit.sections.filter(section => completed.includes(section.id))) {
    for (const block of section.sourceBlocks) {
        if (['heading', 'paragraph', 'clarification'].includes(block.type)) check(block.text, block.sentenceTranslations, section.id + ': ' + block.text);
        if (block.caption) check(block.caption, block.captionSentenceTranslations, section.id + ': caption');
        if (block.alt) check(block.alt, block.altSentenceTranslations, section.id + ': figure description');
        if (block.type === 'list') (block.items || []).forEach((text, index) => { if (typeof text === 'string') check(text, block.itemSentenceTranslations?.[index], section.id + ': list item'); });
        (block.headers || []).forEach((text, index) => { if (proseCell(text)) check(text, block.headerSentenceTranslations?.[index], section.id + ': table header'); });
        (block.rows || []).forEach((row, rowIndex) => {
            if (Array.isArray(row)) row.forEach((text, index) => { if (proseCell(text)) check(text, block.cellSentenceTranslations?.[rowIndex]?.[index], section.id + ': table cell'); });
        });
    }
}
const firstUnit = JSON.stringify(unit);
const firstCache = JSON.stringify(context.translations);
run('js/math12_unit8_translations.js');
assert.equal(JSON.stringify(unit), firstUnit, 'Repeated loading must not change chapter data');
assert.equal(JSON.stringify(context.translations), firstCache, 'Repeated loading must not change the translation cache');
const output = { passed: true, verifiedFields, pendingSections: pending, report };
fs.writeFileSync(path.join(root, 'docs/source-verification/class-12/math12-unit8-translations-check.json'), JSON.stringify(output, null, 2) + '\n');
console.log(JSON.stringify(output, null, 2));
