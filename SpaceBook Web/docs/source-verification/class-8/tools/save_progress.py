"""Write docs/source-verification/class-8/progress.json: Class 8 source inventory and verification status.

Usage: save_progress.py [--next "exact next action"]
Timing samples are appended by build runs to math/timing.log (ISO time, reviewed pages).
"""
import json, sys, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
BOOKS = Path(r'D:\SpaceBook\Books\8th')
ORDER = ['8th MAths', '8th English', '8th General Science', 'Urdu', '8th CS', '8th Geography', '8th History', '8th Islamiat',
         '8th M Q', '8th Arabi', '8th Drawing', '8th HPE', '8th PAshto']
NAMES = {'8th MAths': 'Mathematics', '8th English': 'English', '8th General Science': 'General Science', 'Urdu': 'Urdu',
         '8th CS': 'Computer Science', '8th Geography': 'Geography', '8th History': 'History', '8th Islamiat': 'Islamiat',
         '8th M Q': 'Mutalia-e-Quran', '8th Arabi': 'Arabic', '8th Drawing': 'Drawing', '8th HPE': 'Health & Physical Education', '8th PAshto': 'Pashto'}
APP_FILES = {'8th MAths': 'js/math_8_data.js', '8th English': 'js/english_8_data.js', '8th General Science': 'js/general_science_8_data.js',
             'Urdu': 'js/urdu_8_data.js', '8th CS': 'js/computer_8_data.js', '8th Geography': 'js/geography_8_data.js',
             '8th History': 'js/history_8_data.js', '8th Islamiat': 'js/islamiat_8_data.js', '8th M Q': 'js/mutalia_quran_8_data.js',
             '8th Arabi': 'js/arabic_8_data.js', '8th Drawing': 'js/drawing_8_data.js', '8th HPE': 'js/hpe_8_data.js', '8th PAshto': 'js/pashto_8_data.js'}

CODES = {'8th MAths': 'math', '8th English': 'eng', '8th General Science': 'sci', 'Urdu': 'urdu', '8th CS': 'comp', '8th Geography': 'geo',
         '8th History': 'hist', '8th Islamiat': 'isl', '8th M Q': 'quran', '8th Arabi': 'arabic', '8th Drawing': 'drawing',
         '8th HPE': 'hpe', '8th PAshto': 'pashto'}


def pages_of(folder):
    jpg = folder / 'JPG'
    numbered = sorted(p for p in jpg.glob('*.jpg') if p.stem.isdigit()) if jpg.exists() else []
    pdfs = sorted(str(p) for d in folder.iterdir() if d.is_dir() and d.name.lower().startswith('pdf') for p in d.glob('*.pdf')) if folder.exists() else []
    return len(numbered), str(jpg), pdfs


def main():
    nxt = sys.argv[sys.argv.index('--next') + 1] if '--next' in sys.argv else None
    out_path = HERE / 'progress.json'
    old = json.loads(out_path.read_text(encoding='utf-8')) if out_path.exists() else {}
    subjects = []
    for key in ORDER:
        n, jpg, pdfs = pages_of(BOOKS / key)
        rec = {'subject': NAMES.get(key, key), 'sourceFolder': str(BOOKS / key), 'pageImages': jpg, 'pdfFiles': pdfs,
               'totalPages': n, 'appFile': APP_FILES[key], 'status': 'not started (waits for Mathematics to finish)',
               'reviewedPages': 0, 'correctedPages': 0, 'unresolvedPages': []}
        if key == '8th MAths':
            ledger = json.loads((HERE / 'math' / 'ledger.json').read_text(encoding='utf-8'))
            done = [m['pdfPage'] for m in ledger]
            rec.update({
                'status': 'complete' if len(done) >= n else 'in progress',
                'reviewedPages': len(done), 'correctedPages': len([m for m in ledger if m['status'] != 'blank']),
                'lastCompletedPdfPage': max(done) if done else None,
                'lastCompletedPrintedPage': next((m['printedPage'] for m in reversed(ledger) if m['printedPage']), None),
                'nextPdfPage': (max(done) + 1) if done and len(done) < n else None,
                'currentUnit': ledger[-1]['unit'] if ledger else None, 'currentSection': ledger[-1]['section'] if ledger else None,
                'unresolvedPages': [{'pdfPage': m['pdfPage'], 'issues': m['issues']} for m in ledger if m['issues']],
                'lowOcrAgreementPages': [{'pdfPage': m['pdfPage'], 'ocrWordRecall': m['ocrWordRecall']} for m in ledger
                                         if m['ocrWordRecall'] is not None and m['ocrWordRecall'] < 0.85 and m['status'] != 'blank'],
                'ledger': 'docs/source-verification/class-8/math/ledger.json',
                'transcriptions': 'docs/source-verification/class-8/math/pages/pNNN.txt (NNN = JPG index = PDF page - 1)',
                'note': 'Previous js/math_8_data.js (unverified, saved as math/legacy_math_8_data.json) is replaced unit by unit as pages are reviewed; units with no reviewed page still show the legacy content.', 'scanNote': 'Printed page 1 = JPG 005; printed page 308 = JPG 310, so two printed pages are missing from the scan set (to be located).'})
        elif (HERE / CODES[key] / 'ledger.json').exists():
            code = CODES[key]
            ledger = json.loads((HERE / code / 'ledger.json').read_text(encoding='utf-8'))
            done = [m['pdfPage'] for m in ledger]
            total = len(list((Path('D:/SpaceBook/_cls8_jpg') / code).glob('[0-9][0-9][0-9].jpg'))) or n
            rec.update({
                'totalPages': total,
                'status': 'complete' if total and len(done) >= total else 'in progress',
                'reviewedPages': len(done), 'correctedPages': len([m for m in ledger if m['status'] not in ('blank', 'duplicate')]),
                'lastCompletedPdfPage': max(done) if done else None,
                'nextPdfPage': (max(done) + 1) if done and len(done) < total else None,
                'unresolvedPages': [{'pdfPage': m['pdfPage'], 'issues': m['issues']} for m in ledger if m['issues']],
                'ledger': f'docs/source-verification/class-8/{code}/ledger.json',
                'transcriptions': f'docs/source-verification/class-8/{code}/pages/pNNN.txt'})
        else:
            rec['status'] = 'not started (app shows unverified legacy data)'
        subjects.append(rec)
    timing = []
    tl = HERE / 'math' / 'timing.log'
    if tl.exists():
        for line in tl.read_text(encoding='utf-8').splitlines():
            t, n = line.split('\t')
            timing.append((datetime.datetime.fromisoformat(t), int(n)))
    speed = None
    if len(timing) >= 2:
        (t0, n0), (t1, n1) = timing[0], timing[-1]
        hours = (t1 - t0).total_seconds() / 3600
        speed = round((n1 - n0) / hours, 1) if hours > 0 else None
    data = {
        'class': 8, 'updated': datetime.datetime.now().isoformat(timespec='seconds'),
        'order': 'Mathematics first; then English, General Science, Urdu, Computer Science, Geography, History, Islamiat, Mutalia-e-Quran, Arabic, Drawing, HPE, Pashto',
        'note': 'No separate Social Studies textbook exists in the Class 8 source folder (Geography and History are separate books). Source folder D:/SpaceBook/Books/8th.',
        'subjects': subjects,
        'speed': {'pagesPerHourOverall': speed, 'samples': len(timing),
                  'benchmarkFirst10Pages': old.get('speed', {}).get('benchmarkFirst10Pages') or {'pages': 16, 'minutes': 11, 'pagesPerHour': 87, 'measured': 'pages 9-24 between 01:25:57 and 01:37:03 on 2026-10-10 (manual visual transcription + Urdu/Pashto translation)'}},
        'nextAction': nxt or old.get('nextAction'),
    }
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    m = subjects[0]
    print(f"Math {m['reviewedPages']}/{m['totalPages']} pages; speed {speed} pages/hour")


if __name__ == '__main__':
    main()
