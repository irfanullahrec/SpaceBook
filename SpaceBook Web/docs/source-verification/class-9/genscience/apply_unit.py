# -*- coding: utf-8 -*-
"""Apply unitNN.py to js/general_science_9_data.js: python apply_unit.py 1"""
import os, sys, datetime, importlib
sys.stdout.reconfigure(encoding='utf-8')
import gs_tools as G

n = int(sys.argv[1])
U = importlib.import_module(f'unit{n:02d}')
L = 'abcd'


def tri(t):
    return dict(text=t[0], urdu=t[1], pashto=t[2])


def section(num, title, paras, pages):
    return dict(sectionNum=num, title=title[0], heading=title[0], headingUrdu=title[1], headingPashto=title[2],
                urduTitle=title[1], pashtoTitle=title[2],
                paras=[tri(p) for p in paras], translationStatus='authored_aligned_paragraphs',
                sourcePrintedPages=pages, sourceJpgPages=[p + 4 for p in pages])


if os.path.exists(G.LOCK):
    sys.exit('shared lock held: ' + open(G.LOCK, encoding='utf-8').read())
open(G.LOCK, 'w', encoding='utf-8').write(f'class9-content-agent general-science unit{n} {datetime.datetime.now().isoformat()}')
try:
    data = G.load()
    u = data[n - 1]
    assert u['number'] == n
    printed = [G.printed_of(g) for g in U.SCANS if G.printed_of(g)]
    u.update(title=U.TITLE[0], titleUrdu=U.TITLE[1], titlePashto=U.TITLE[2], type='chapter',
             pageRange=f'Pages {min(printed)} - {max(printed)}',
             slos=[tri(s) for s in U.SLOS],
             sections=[section(*s) for s in U.SECTIONS],
             keyPoints=[p[0] for p in U.KEY_POINTS],
             keyPointsTranslated=[tri(p) for p in U.KEY_POINTS],
             englishSummary=' '.join(p[0] for p in U.KEY_POINTS),
             urduSummary=' '.join(p[1] for p in U.KEY_POINTS),
             pashtoSummary=' '.join(p[2] for p in U.KEY_POINTS))
    ex = dict(mcqs=[], shortQuestions=[], longQuestions=[])
    for i, (q, opts, c, expl) in enumerate(U.MCQS):
        ex['mcqs'].append(dict(id=f'u{n}-mcq{i + 1}', q=q[0], qUrdu=q[1], qPashto=q[2], options=opts, correct=c,
                               answer=f'({L[c]}) {opts[c]}', explanation=expl))
    for key, items in (('shortQuestions', getattr(U, 'SQS', [])), ('longQuestions', U.LQS)):
        for i, (q, a) in enumerate(items):
            ex[key].append(dict(id=f'u{n}-{key[:2]}{i + 1}', q=q[0], qUrdu=q[1], qPashto=q[2], answer=a,
                                answerOrigin='SpaceBook-authored answer (not printed in source)'))
    if getattr(U, 'ACTIVITIES', None):
        ex['activities'] = list(U.ACTIVITIES)
    if getattr(U, 'GLOSSARY', None):
        u['glossary'] = [dict(word=t, pos='term', meaning=m, urdu=ur, pashto=ps, sentence=f'Textbook glossary, p.{pg}')
                         for t, m, ur, ps, pg in U.GLOSSARY]
    ex['answerNote'] = 'MCQ keys and answers are SpaceBook-authored; the textbook prints no answer key.'
    u['exercise'] = ex
    u['sourceReview'] = dict(source='D:/SpaceBook/Books/9th/9th General Science/JPG', jpgPages=list(U.SCANS),
                             printedPages=printed, notes=U.NOTES,
                             translations='Urdu and Pashto are SpaceBook translations paired paragraph by paragraph with the English textbook text.',
                             reviewedAt=datetime.date.today().isoformat())
    G.save(data)
finally:
    os.remove(G.LOCK)
entries = [(g, 'corrected', f'Unit {n}: compared with page image; ' + ' '.join(U.NOTES)[:300]) for g in U.SCANS]
entries += [(g, 'corrected', f'Glossary attached to unit {n} (ch.glossary), compared with page image.') for g in getattr(U, 'GLOSSARY_SCANS', [])]
entries += [(g, 'excluded', note) for g, note in getattr(U, 'EXCLUDED_SCANS', [])]
print(G.record_pages(entries)['counts'])
