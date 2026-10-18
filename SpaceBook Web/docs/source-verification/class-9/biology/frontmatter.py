# -*- coding: utf-8 -*-
"""PDF 1-6 front matter of the Class 9 Biology book, stored as structured data on BIO_DATA unit 1."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T
FM = dict(
    sourcePdfPages=[1, 2, 3, 4, 5, 6],
    title='A Textbook of BIOLOGY Grade IX', publisher='Khyber Pakhtunkhwa Textbook Board Peshawar',
    covers=[dict(pdfPage=1, note='Front cover photograph (frog, flowers, human circulatory system) — decorative, excluded from lessons.'),
            dict(pdfPage=3, note='Inner title page (Venus flytrap photograph, board logo) — decorative, excluded from lessons.')],
    quotePage=dict(pdfPage=2, lines=['مومن تو آپس میں بھائی بھائی ہیں۔', 'تو اپنے دو بھائیوں میں صلح کرا دیا کرو۔', 'اور اللہ سے ڈرتے رہو۔', 'تاکہ تم پر رحمت کی جائے۔'],
                   reference='(سورۃ الحجرات: ۱۰)', language='ur',
                   english='The believers are but brothers, so make settlement between your brothers. And fear Allah that you may receive mercy. (Surah Al-Hujurat: 10)',
                   pashto='مؤمنان خو یو د بل وروڼه دي، نو د خپلو دوو وروڼو ترمنځ روغه کوئ. او له الله وېرېږئ چې پر تاسو رحم وشي. (سورة الحجرات: ۱۰)'),
    credits=dict(pdfPage=4, lines=[
        'All rights reserved with the Khyber Pakhtunkhwa Textbook Board Peshawar',
        'Developed by Khyber Pakhtunkhwa Textbook Board, Peshawar and approved by the Directorate of Curriculum & Teacher Education (DCTE), Abbottabad vide NOC No. 1304-06/F.03/Vol-I/Biology-9th Dated 23-02-2018.',
        'Authors: Dr. Izhar Ahmad, Dr. Syed Zahir Shah, Zaigham Hassan, Dr. Mirza Hakim Khan, Rizwan Maqbool, Naveed Akhtar',
        'Review Supervision: Gohar Ali Khan, Director, Curriculum & Teacher Education Khyber Pakhtunkhwa, Abbottabad',
        'Focal Person: Zulfiqar Khan, Additional Director, Curriculum & Textbook Review, DCTE, Abbottabad',
        'Reviewers: Prof. Dr. Azhar Mehmood, GPGC, Mandian Abbottabad; Sher Muhammad, Principal, GHS, Gandhian Mansehra; Asghar Ali, SST, GHS, Gandhian Mansehra; Dr. Shafqat Hussain, SS (Desk Officer), DCTE Abbottabad; Salmana Zaman Khan, SS, KP Textbook Board, Peshawar',
        'Editor: Waqar Ahmad, SS (Biology), Khyber Pakhtunkhwa Textbook Board Peshawar',
        'Printing Supervision: Syed Muhammad Farrulsaqlain, Chairman; Abdul Wali Khan, (Member E&P), Khyber Pakhtunkhwa Textbook Board, Peshawar',
        'Printed for Academic Year 2025-26. Website: www.kptbb.gov.pk. Email: membertbb@yahoo.com. Telephone: 091-9217714-15']),
    contents=dict(pdfPages=[5, 6], rows=[
        [1, 'INTRODUCTION TO BIOLOGY', 1], [2, 'SOLVING A BIOLOGICAL PROBLEM', 23], [3, 'BIODIVERSITY', 37], [4, 'CELLS AND TISSUES', 63],
        [5, 'CELL CYCLE', 99], [6, 'ENZYMES', 116], [7, 'BIO-ENERGETICS', 129], [8, 'NUTRITION', 147], [9, 'TRANSPORT', 178],
        [None, 'GLOSSARY', 207], [None, 'INDEX', 215], [None, 'REFERENCES', 217]]),
)
d = T.load_bio(); u = next(x for x in d if x['number'] == 1); u['sourceFrontMatter'] = FM; T.save_bio(d)
P = []
P += [(1, 'excluded', 'Front cover photograph; decorative. Recorded in sourceFrontMatter.'),
      (2, 'corrected', 'Urdu verse page (Al-Hujurat 10) stored verbatim with English/Pashto in sourceFrontMatter.quotePage.'),
      (3, 'excluded', 'Inner title page; decorative. Recorded in sourceFrontMatter.'),
      (4, 'corrected', 'Credits page transcribed into sourceFrontMatter.credits.'),
      (5, 'corrected', 'Contents units 1-5 transcribed into sourceFrontMatter.contents.'),
      (6, 'corrected', 'Contents units 6-9, glossary, index, references transcribed.')]
notes = {7: 'Unit 1 opener + 12 learning outcomes: new bio1_slo section (previously absent).',
         8: 'Opening paragraphs and Figure 1.1 (coded photo-grid with source labels); previously merged/paraphrased.',
         9: '1.1 replaced paraphrase with verbatim text (Linneaus spelling, (i)-(iii) divisions); 1.2 branches i-viii verbatim; two Scientific Information boxes.',
         10: 'Branches ix-xvi verbatim + entomon box; 1.3 intro, 1.3.1, 1.3.2 verbatim (previous text was invented).',
         11: '1.3.3-1.3.5, 1.4, 1.4.1-1.4.3, Scientific Tips box and Penicillin STS box verbatim.',
         12: '1.4.4-1.4.7, Forensic/Health care boxes, career analysis table (semantic table).',
         13: '1.5 and 1.5.1-1.5.5 verbatim (previous text was paraphrased).',
         14: '1.6 intro + 5 verse boxes (Arabic, printed English, reference).',
         15: '4 verse boxes (Al-Anam 99, 101, Al-Raad 4, Al-Anam 102).',
         16: '4 verse boxes (Taha 53, Anbiya 30, Mominoon 14, Nahal 68-69).',
         17: '4 verse boxes (Noor 45, Hijr 19, Nahal 66, Anam 95). Removed non-source introQuran (Al-Baqarah 29).',
         18: '1.7, 1.7.1-1.7.5 verbatim.',
         19: '1.7.6-1.7.9, 1.8 intro, Level 1, Scientific Information box.',
         20: 'Bio-element bullets, coded Figure 1.2 pie chart (source values), Levels 2-4, STS transplant box.',
         21: 'Levels 5-8, higher-levels box, Analysing and Interpreting box.',
         22: 'Coded Figure 1.3 levels diagram; activity table. Source prints C6H12O5 (glucose is C6H12O6): printed value kept with labelled note.',
         23: '1.9 (i), (ii) verbatim; coded Figure 1.4 with labels Flagella, Eye spot, Nucleus, Chloroplast.',
         24: '1.9 (iii) verbatim, coded Figure 1.5, Activity box.',
         25: 'Key Points: 12 bullets verbatim (keyPoints + bio1_keypoints section).',
         26: 'Exercise A MCQs i-v replaced invented MCQs with source MCQs; answers labelled SpaceBook (no printed key).',
         27: 'MCQs vi-x source; vii ambiguity noted in explanation.',
         28: 'B short questions i-v and C detailed questions i-v verbatim; earlier authored answers kept and labelled.'}
P += [(n, 'corrected', notes[n]) for n in range(7, 29)]
prog = T.record_pages(P, next_page=29, current_chapter='Unit 2: Solving a Biological Problem')
prog['validationEvidence'] = prog.get('validationEvidence', []) + ['2026-10-12 Unit 1 (PDF 7-28): check_js OK (59 sections, no duplicate ids); render_check.cjs unit 1: 12 sections, 5 SVG, 2 tables, 0 problems in en/ur/ps; figures rasterised and visually compared to source.']
import json, io; json.dump(prog, io.open(T.PROGRESS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(prog['counts'], prog['nextPdfPage'])
print('ok' if T.check_js() else 'FAIL')
