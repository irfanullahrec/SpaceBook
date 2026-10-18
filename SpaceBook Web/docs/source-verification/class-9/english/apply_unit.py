# -*- coding: utf-8 -*-
"""Apply a unitNN.py correction module to english_data.js.  Usage: python apply_unit.py 1"""
import importlib, os, sys, datetime
sys.stdout.reconfigure(encoding='utf-8')
import eng9_tools as T

n = int(sys.argv[1])
m = importlib.import_module(f'unit{n:02d}')
if os.path.exists(T.LOCK):
    sys.exit('shared lock held: ' + open(T.LOCK, encoding='utf-8').read())
open(T.LOCK, 'w', encoding='utf-8').write(f'class9-content-agent english unit {n} {datetime.datetime.now().isoformat()}')
try:
    data = T.load()
    u = T.unit(data, n)
    if getattr(m, 'SOURCE_SLOS', None):
        u['sourceSlos'] = m.SOURCE_SLOS
    if getattr(m, 'PRE_READING', None):
        u['preReading'] = m.PRE_READING
    if getattr(m, 'GLOSSARY', None):
        u['glossary'] = [dict(word=w, pos='', meaning=mean, urdu=ur, pashto=ps, sourceMeaning=True) for w, mean, ur, ps in m.GLOSSARY]
        if 'glossaryTable' in u.get('exercise', {}):
            u['exercise']['glossaryTable'] = u['glossary']
    if getattr(m, 'COMPREHENSION', None):
        u.setdefault('exercise', {})['comprehension'] = [dict(question=q, answer=m.LAB + a, answerOrigin='SpaceBook') for q, a in m.COMPREHENSION]
    if hasattr(m, 'patch'):
        m.patch(u)
    u['sourceReview'] = dict(sourcePdf='D:/SpaceBook/Books/9th/9th English/PDF/9th English.pdf', pdfPages=m.PDF,
                             printedPages=sorted({T.printed_of(p) for p in m.PDF if T.printed_of(p)}), notes=m.NOTES,
                             reviewedAt=datetime.date.today().isoformat())
    if '_removed' in u:
        u['sourceReview']['removedUnverifiedText'] = u.pop('_removed')
    T.save(data)
finally:
    os.remove(T.LOCK)
entries = [(p, 'excluded-duplicate' if p in T.DUPLICATES else 'corrected', (f'Duplicate scan of printed page {T.DUPLICATES[p]}; inspected, no separate content. ' if p in T.DUPLICATES else '') + f'Unit {n}: compared with page image; ' + '; '.join(m.NOTES)[:400]) for p in m.PDF]
prog = T.record_pages(entries, next_page=m.PDF[-1] + 1)
print('unit', n, 'saved; progress', prog['counts'])
