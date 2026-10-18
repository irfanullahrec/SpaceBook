# -*- coding: utf-8 -*-
"""Apply a proofread prose lesson (lessonNN.py + optional lessonNN_ex.py) to urdu_data.js: python apply_prose.py 1"""
import os, sys, json, datetime, importlib
sys.stdout.reconfigure(encoding='utf-8')
import urdu9_tools as T

n = int(sys.argv[1])
L = importlib.import_module(f'lesson{n:02d}')
try:
    X = importlib.import_module(f'lesson{n:02d}_ex')
except ModuleNotFoundError:
    X = None


def sections():
    out = []
    for head, hen, hps, paras in L.SECTIONS:
        ur = [p[0] for p in paras]
        en = [p[1] for p in paras]
        ps = [p[2] for p in paras]
        out.append(dict(heading=head, headingEn=hen, headingPs=hps, paras=ur, urdu='\n\n'.join(ur),
                        english='\n'.join(en), pashto='\n'.join(ps), parasEnglish=en, parasPashto=ps))
    return out


if os.path.exists(T.LOCK):
    sys.exit('shared lock held')
open(T.LOCK, 'w', encoding='utf-8').write(f'class9-content-agent urdu lesson {n} {datetime.datetime.now().isoformat()}')
try:
    data = T.load()
    idx = next(i for i, u in enumerate(data) if u['number'] == n)
    u = json.loads(json.dumps(data[idx], ensure_ascii=False).replace('واصحابیہ', 'واصحابہ'))
    secs = sections()
    u['sections'] = secs
    u['urduSections'] = [s['urdu'] for s in secs]
    notes = list(L.NOTES)
    pdf = list(L.PDF)
    if X:
        u['title'] = X.TITLE
        if getattr(X, 'AUTHOR_INFO', None):
            u['authorInfo'] = X.AUTHOR_INFO
        X.fix_exercise(u['exercise'])
        u.update(getattr(X, 'SUMMARY', {}))
        notes += X.NOTES
        pdf = sorted(set(pdf) | set(X.EXTRA_PDF))
    src = getattr(L, 'SOURCE_LINE', '')
    u['sourceLine'] = src
    u['urduText'] = '\n\n'.join([u['title'], u.get('author', '')] + [s['heading'] + '\n' + s['urdu'] for s in secs] + ([src] if src else []))
    u['englishTranslation'] = '\n\n'.join(f'【 {s["headingEn"]} 】\n' + '\n\n'.join(s['parasEnglish']) for s in secs)
    u['pashtoTranslation'] = '\n\n'.join(f'【 {s["headingPs"]} 】\n' + '\n\n'.join(s['parasPashto']) for s in secs)
    u['sourceReview'] = dict(sourcePdf='D:/SpaceBook/Books/9th/9th urdu/PDF/9th Urdu.pdf', pdfPages=pdf,
                             printedPages=[T.printed_of(p) for p in pdf], notes=notes,
                             translations='English and Pashto are SpaceBook translations aligned paragraph by paragraph with the Urdu.',
                             reviewedAt=datetime.date.today().isoformat())
    data[idx] = u
    T.save(data)
finally:
    os.remove(T.LOCK)
print(T.record_pages([(p, 'corrected', f'Lesson {n}: compared with page image; ' + ' '.join(notes)[:400]) for p in pdf])['counts'])
