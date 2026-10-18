# -*- coding: utf-8 -*-
import sys, json, io, datetime; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T
E = [(p, 'corrected', f'Glossary page (printed {p-3}) transcribed as trilingual table bio-gloss-{p}.') for p in range(210, 218)]
E += [(218, 'corrected', 'Index A-H transcribed as trilingual tables (columns cropped at 150 dpi to read page numbers; "Guard cell 133" faint).'),
      (219, 'corrected', 'Index I-Z transcribed as trilingual tables.'),
      (220, 'corrected', 'References (9 books) transcribed verbatim.'), (221, 'corrected', 'Online learning list (12 URLs, one printed twice) transcribed.'),
      (222, 'corrected', 'About the Authors page 1 transcribed with Urdu/Pashto pairs.'),
      (223, 'corrected', 'About the Authors page 2 + Urdu verse box (Al-Ahzab 40) with English/Pashto translations.'),
      (224, 'excluded', 'Blank KPTBB textbook feedback form (statements 1-8, comment grid); non-instructional, not reproduced.'),
      (225, 'excluded', 'Back cover: building photo, national anthem text and print details (code PSP/ANP-23-92-2425(O), quantity 45,000, price 337.00, Al Naveed Printers). Non-instructional; anthem lyrics not reproduced.')]
prog = T.record_pages(E, next_page=None, current_chapter='Biology complete')
prog['nextPdfPage'] = None
prog['subjectComplete'] = True
prog.setdefault('validationEvidence', []).append(dict(date=datetime.date.today().isoformat(), units='1-9 + back matter', check='bio9_tools.check_js + render_check.cjs per unit', result='BIO_DATA ok: units=10 sections=84 dupIds=[]; problems=0 for every unit'))
json.dump(prog, io.open(T.PROGRESS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cp = r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-9\checkpoint.json'
c = json.load(io.open(cp, encoding='utf-8'))
c.update(currentSubject='Physics', biologyComplete=True, lastFullyVerifiedPdfPage=None, nextPdfPage=1, currentChapter=None,
         biologySummary='All 225 PDF pages recorded: 221 corrected, 4 excluded; source gaps printed 26 and 42-43 unresolved (no alternate copy).',
         lastUpdated=datetime.datetime.now().isoformat(timespec='seconds'),
         nextAction='Start Class 9 Physics: inventory D:/SpaceBook/Books/9th Physics source, inspect existing physics dataset for class 9, set up physics progress file.')
json.dump(c, io.open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(prog['counts'], len(prog['pages']))
