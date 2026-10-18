# -*- coding: utf-8 -*-
"""Apply chNN.py to js/pakstudy_data.js: python apply_chapter.py 1"""
import os, sys, datetime, importlib
sys.stdout.reconfigure(encoding='utf-8')
import pak_tools as P

n = int(sys.argv[1])
C = importlib.import_module(f'ch{n:02d}')
L4 = ['الف', 'ب', 'ج', 'د']


def section(sid, tur, ten, tps, blocks):
    return dict(id=sid, title=tur, titleEn=ten, titlePs=tps,
                content='\n\n'.join(b[0] for b in blocks),
                contentEn='\n\n'.join(b[1] for b in blocks),
                contentPs='\n\n'.join(b[2] for b in blocks),
                blocks=[dict(ur=a, en=b, ps=c) for a, b, c in blocks])


if os.path.exists(P.LOCK):
    sys.exit('shared lock held')
open(P.LOCK, 'w', encoding='utf-8').write(f'class9-content-agent pakstudy ch{n} {datetime.datetime.now().isoformat()}')
try:
    data = P.load()
    u = next(x for x in data if x['number'] == n)
    u['sections'] = [section(*s) for s in C.SECTIONS]
    if getattr(C, 'INTRO_QURAN', None):
        u['introQuranHadith'] = [dict(arabic=a, translation=t, reference=r) for a, t, r in C.INTRO_QURAN]
    ex = u.setdefault('exercise', {})
    ex['mcqs'] = [dict(id=f'mcq{i+1}', question=q, options=o, correct=c, answer=f'({L4[c]}) {o[c]}', explanation=e)
                  for i, (q, o, c, e) in enumerate(C.MCQS)]
    ex['shortQuestions'] = [dict(qNo=f'سوال {i+1}', question=q, answer=a) for i, (q, a) in enumerate(C.SQS)]
    ex['longQuestions'] = [dict(qNo=f'تفصیلی سوال {i+1}', question=q, answer=a) for i, (q, a) in enumerate(C.LQS)]
    ex['activities'] = list(C.ACTIVITIES)
    ex['answerNote'] = 'SpaceBook answers (the textbook prints no answers).'
    printed = [P.printed_of(g) for g in C.SCANS if P.printed_of(g)]
    u['pageRange'] = f'صفحات {min(printed)} تا {max(printed)}'
    u['studyAidsNote'] = 'keyPoints, timeline and SLO questions are SpaceBook study aids, not textbook text.'
    u['sourceReview'] = dict(sources=sorted({P.source_of(g).split(' ')[0] for g in C.SCANS}), scans=C.SCANS, printedPages=sorted(set(printed)),
                             notes=C.NOTES, translations='contentEn/contentPs and blocks[].en/ps are SpaceBook translations paired with the Urdu.',
                             reviewedAt=datetime.date.today().isoformat())
    P.save(data)
finally:
    os.remove(P.LOCK)
entries = []
for g in C.SCANS:
    st = 'excluded' if g in P.DUPLICATE else 'corrected'
    note = f'duplicate scan of printed {P.printed_of(g)} (same as scan {P.DUPLICATE[g]})' if g in P.DUPLICATE else f'Chapter {n}: compared with page image; ' + ' '.join(C.NOTES)[:300]
    entries.append((g, st, note))
print(P.record_pages(entries)['counts'])
