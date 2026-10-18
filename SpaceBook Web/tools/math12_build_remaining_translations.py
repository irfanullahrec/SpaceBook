"""Pair tmp/m12/tr-<section>.json ([ur, ps] per pending original, in order) with tmp/m12/pending.json originals
and write js/math12_remaining_translations.js (same add()/attach format as the unit translation files)."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
pending = json.loads((ROOT / 'tmp/m12/pending.json').read_text(encoding='utf-8'))
done, adds = [], []
for sid, info in pending.items():
    f = ROOT / f'tmp/m12/tr-{sid}.json'
    miss = info['missing']
    if not f.exists():
        continue
    tr = json.loads(f.read_text(encoding='utf-8'))
    if len(tr) != len(miss):
        sys.exit(f'{sid}: {len(tr)} translations for {len(miss)} originals')
    for en, (ur, ps) in zip(miss, tr):
        if not ur.strip() or not ps.strip():
            sys.exit(f'{sid}: empty translation for {en[:60]}')
        adds.append(f'    add({json.dumps(en, ensure_ascii=False)}, {json.dumps(ur, ensure_ascii=False)}, {json.dumps(ps, ensure_ascii=False)});')
    done.append(sid)
tail = (ROOT / 'js/math12_unit9_translations.js').read_text(encoding='utf-8')
attach = tail[tail.index('    const complete = rows'):]
attach = attach.replace("globalThis.MATH12_UNIT9_TRANSLATION_REPORT", "globalThis.MATH12_REMAINING_TRANSLATION_REPORT")
js = ('// Translations for the remaining Class 12 Maths source sections (6.6, 8.4, 9.2–9.4). Source English is unchanged.\n'
      '(function () {\n    \'use strict\';\n'
      '    if (typeof MATH_12_DATA === \'undefined\' || typeof MATH12_SENTENCE_TRANSLATIONS === \'undefined\') return;\n'
      '    const authored = new Map();\n    const add = (en, ur, ps) => authored.set(en, [{ en, ur, ps }]);\n'
      + '\n'.join(adds) + '\n\n'
      f'    const completedSectionIds = {json.dumps(done)};\n'
      '    const report = { scope: \'Remaining Class 12 Maths source sections.\', completedSectionIds, sections: [], newPassageEntries: 0 };\n'
      '    for (const [english, rows] of authored) {\n'
      '        if (!Object.prototype.hasOwnProperty.call(MATH12_SENTENCE_TRANSLATIONS, english) || !(MATH12_SENTENCE_TRANSLATIONS[english] || []).every(r => r.ur && r.ps)) {\n'
      '            MATH12_SENTENCE_TRANSLATIONS[english] = rows;\n            report.newPassageEntries++;\n        }\n    }\n'
      '    const sectionsById = new Map(); for (const ch of MATH_12_DATA) for (const s of ch.sections || []) sectionsById.set(s.id, s);\n'
      '    const unit = { sections: completedSectionIds.map(id => sectionsById.get(id)).filter(Boolean) };\n'
      + attach)
(ROOT / 'js/math12_remaining_translations.js').write_text(js, encoding='utf-8')
print('sections', done, 'entries', len(adds))
