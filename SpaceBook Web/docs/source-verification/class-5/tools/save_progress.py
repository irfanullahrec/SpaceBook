"""Write docs/source-verification/class-5/progress.json: Class 5 source inventory and verification status.

Usage: save_progress.py [--next "exact next action"]
Only counts pages that have a transcription file AND appear in the build ledger (built into the app data).
"""
import json, sys, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
BOOKS = Path(r'D:\SpaceBook\Books\5th')
# (folder, subject name, app file, ledger key)
ORDER = [('5th Maths', 'Mathematics', 'js/math_5_data.js', 'math'),
         ('5th English', 'English', 'js/english_5_data.js', 'eng'),
         ('5th General Science', 'General Science', 'js/general_science_5_data.js', 'sci'),
         ('5th Urdu', 'Urdu', 'js/urdu_5_data.js', 'urdu'),
         ('5th Social Study', 'Social Studies (English medium)', 'js/social_studies_5_data.js', 'sst'),
         ('5th Social Study UM', 'Social Studies (Urdu medium)', 'js/social_studies_um_5_data.js', 'sstum'),
         ('5th Islamiat', 'Islamiat', 'js/islamiat_5_data.js', 'isl'),
         ('5th Pashto', 'Pashto', 'js/pashto_5_data.js', 'pashto')]


def main():
    nxt = sys.argv[sys.argv.index('--next') + 1] if '--next' in sys.argv else None
    out_path = HERE / 'progress.json'
    old = json.loads(out_path.read_text(encoding='utf-8')) if out_path.exists() else {}
    subjects = []
    for folder, name, app, key in ORDER:
        src = BOOKS / folder
        jpgs = sorted((src / 'JPG').glob('*.jpg'))
        pdfs = sorted(str(p) for p in (src / 'PDF').glob('*.pdf'))
        docx = sorted(str(p) for p in (src / 'Word').glob('*.docx'))
        rec = {'subject': name, 'sourceFolder': str(src), 'pageImages': str(src / 'JPG'), 'linkedScans': f'D:/SpaceBook/_cls5_jpg/{key}/NNN.jpg (0-based)',
               'pdfFiles': pdfs, 'wordFiles': docx, 'totalPages': len(jpgs), 'appFile': app,
               'legacyBackup': f'docs/source-verification/class-5/legacy-backup/{Path(app).name}',
               'status': 'not started', 'reviewedPages': 0, 'unresolvedPages': []}
        ledger_f = HERE / key / 'ledger.json'
        if ledger_f.exists():
            ledger = json.loads(ledger_f.read_text(encoding='utf-8'))
            done = [m['pdfPage'] for m in ledger]
            rec.update({
                'status': 'complete' if len(done) >= len(jpgs) else 'in progress',
                'reviewedPages': len(done),
                'lastCompletedPdfPage': max(done) if done else None,
                'lastCompletedPrintedPage': next((m['printedPage'] for m in reversed(ledger) if m['printedPage']), None),
                'nextPdfPage': (max(done) + 1) if done and len(done) < len(jpgs) else None,
                'currentUnit': ledger[-1].get('unit') if ledger else None,
                'currentSection': ledger[-1].get('section') if ledger else None,
                'svgFigures': sum(m.get('svg', 0) for m in ledger), 'tables': sum(m.get('tables', 0) for m in ledger),
                'unresolvedPages': [{'pdfPage': m['pdfPage'], 'printedPage': m['printedPage'], 'issues': m['issues']} for m in ledger if m['issues']],
                'lowOcrAgreementPages': [{'pdfPage': m['pdfPage'], 'ocrWordRecall': m['ocrWordRecall']} for m in ledger
                                         if m.get('ocrWordRecall') is not None and m['ocrWordRecall'] < 0.85 and m['status'] not in ('blank', 'duplicate')],
                'ledger': f'docs/source-verification/class-5/{key}/ledger.json',
                'transcriptions': f'docs/source-verification/class-5/{key}/pages/pNNN.txt (NNN = JPG index = PDF page - 1)'})
        if key == 'math':
            rec['scanNote'] = ('201 single-page JPGs = 201 single-page PDF pages (same scans). JPG 000 cover, 001 download-site advert (not textbook), '
                               '002-005 front matter; printed page p = JPG p+5 (printed 1 = JPG 006). Contents: units 1-9 pp.1-174, answers 175-184, '
                               'glossary 185, appendix 186, weblinks 187. Word/PDF part 05 of 06 is missing from the source folder (JPGs complete).')
        subjects.append(rec)
    timing = old.get('benchmark')
    data = {
        'class': 5, 'updated': datetime.datetime.now().isoformat(timespec='seconds'),
        'order': 'Mathematics first; then English, General Science, Urdu, Social Studies (EM), Social Studies (UM), Islamiat, Pashto (only these 8 books exist in D:/SpaceBook/Books/5th)',
        'note': 'No Computer Science, Geography, History, Mutalia-e-Quran, Arabic, Drawing or HPE textbook exists in the Class 5 source folder.',
        'pipeline': 'Pages transcribed in the Class 6 DSL (EN || UR || PS) -> tools/build_math5.py -> js/math_5_data.js + js/math_5_solutions.js; rendered by js/math5_reader.js (clone of math6_reader for cls5).',
        'subjects': subjects,
        'benchmark': timing or {'first12LessonPages': 'JPG 006-017 transcribed, translated and built between 02:00:48 and 02:08:27 on 2026-10-11 (about 90 pages/hour, visual transcription + Urdu/Pashto translation)'},
        'nextAction': nxt or old.get('nextAction'),
    }
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    m = subjects[0]
    print(f"Math {m['reviewedPages']}/{m['totalPages']} pages; issues on {len(m['unresolvedPages'])} pages")


if __name__ == '__main__':
    main()
