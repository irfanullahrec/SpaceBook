# -*- coding: utf-8 -*-
"""Attach the book's فرہنگ (PDF 131-142) to each lesson as `glossary` and record PDF 1-2, 131-150."""
import os, sys, datetime
sys.stdout.reconfigure(encoding='utf-8')
import urdu9_tools as T, glossary as G

if os.path.exists(T.LOCK):
    sys.exit('shared lock held')
open(T.LOCK, 'w', encoding='utf-8').write(f'class9-content-agent urdu glossary {datetime.datetime.now().isoformat()}')
try:
    data = T.load()
    for n, rows in G.GLOSSARY.items():
        u = T.lesson(data, n)
        u['glossary'] = [dict(word=w, meaning=m, meaningEn=en, meaningPs=ps, source='فرہنگ (درسی کتاب)') for w, m, en, ps in rows]
        u['glossaryNote'] = G.NOTE_TOP + ' English and Pashto meanings are SpaceBook translations of the printed Urdu meaning.'
        sr = u.setdefault('sourceReview', {})
        pages = sorted(set(G.PAGES[n]))
        sr['glossaryPdfPages'] = pages
        sr['glossaryPrintedPages'] = [T.printed_of(p) for p in pages]
    T.save(data)
finally:
    os.remove(T.LOCK)

notes = {}
for n, pages in G.PAGES.items():
    for p in pages:
        notes.setdefault(p, []).append(n)
entries = [(p, 'corrected', f'فرہنگ for lessons {sorted(set(ls))}: transcribed from page image into lesson.glossary (Urdu meaning as printed; English/Pashto SpaceBook). ' + ' '.join(c for c in G.CORRECTIONS if str(p) in c or 'Lesson 1' in c and p == 131)[:250])
           for p, ls in sorted(notes.items())]
entries += [(143, 'excluded', 'Authors\' introduction (مؤلفین کا تعارف); not lesson content, not represented in the app.'),
            (1, 'excluded', 'Front cover; no lesson content.'),
            (2, 'excluded', 'Imprint page; no lesson content.'),
            (144, 'excluded', 'Quran verse (al-Hujurat 49:10) and hadith panel; front matter, not lesson content.'),
            (145, 'excluded', 'Hadith panels (Khatam an-Nabiyyin; halal earning); front matter.'),
            (146, 'excluded', 'National anthem page; front matter.'),
            (147, 'excluded', 'Title page; front matter.'),
            (148, 'verifiedUnchanged', 'حاصلاتِ تعلم (book SLO list); inspected, no per-lesson app record derives from it.'),
            (149, 'verifiedUnchanged', 'Contents (prose): lesson titles, authors and printed start pages match the app lesson records.'),
            (150, 'verifiedUnchanged', 'Contents (poetry, ghazal, فرہنگ printed p.129): titles and poets match the app records.')]
print(T.record_pages(entries, next_page=None)['counts'])
