"""Build a Class 5 textbook (every subject except Mathematics, which has build_math5.py) from its page-by-page transcriptions.

    python docs/source-verification/class-5/tools/build_book5.py SUBJ   (SUBJ: eng, sci, urdu, sst, sstum, isl, pashto)

Pages:   docs/source-verification/class-5/<SUBJ>/pages/pNNN.txt  (NNN = 0-based scan index; PDF page = NNN + 1)
Scans:   D:/SpaceBook/_cls5_jpg/<SUBJ>/NNN.jpg  (rendered from / linked to the Books/5th source files; see SOURCES)
Units:   <SUBJ>/units.tsv  (number, EN, UR, PS, first printed page, optional label) from the book's contents page.
Output:  js/<name>_5_data.js — keeps the legacy global (e.g. ENGLISH_5_DATA) and registers window.CLS5_BOOKS[SUBJ]
         for js/cls5_book_reader.js. Answers/solutions go to window.CLS5_SOLUTIONS under 'c5<subj>-sN' ids
         (js/math5_reader.js looks answers with a '-' in their id up there).

Page syntax: as documented in build_math5.py, plus
  @tab NAME        the current section also appears in subject tab NAME (grammar, vocabulary, ...)
  sol ANSWER ## EN || UR || PS     SpaceBook answer for the last question/part (shown behind a button)
"""
from pathlib import Path
import json, re, sys, datetime
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_math5 as bm

HERE = bm.HERE          # docs/source-verification/class-5
APP = bm.APP            # SpaceBook Web
SUBJECTS = {
    'eng': ('English', 'english_5_data.js', 'ENGLISH_5_DATA', 'English 5 (KPTBB, Curriculum 2020)'),
    'sci': ('General Science', 'general_science_5_data.js', 'GENERAL_SCIENCE_5_DATA', 'General Science 5 (KPTBB)'),
    'urdu': ('Urdu', 'urdu_5_data.js', 'URDU_5_DATA', 'Urdu 5 (KPTBB)'),
    'sst': ('Social Studies (EM)', 'social_studies_5_data.js', 'SOCIAL_STUDIES_5_DATA', 'Social Studies 5, English medium (KPTBB)'),
    'sstum': ('Social Studies (UM)', 'social_studies_um_5_data.js', 'SOCIAL_STUDIES_UM_5_DATA', 'Social Studies 5, Urdu medium (KPTBB)'),
    'isl': ('Islamiat', 'islamiat_5_data.js', 'ISLAMIAT_5_DATA', 'Islamiat 5 (KPTBB)'),
    'pashto': ('Pashto', 'pashto_5_data.js', 'PASHTO_5_DATA', 'Pashto 5 (KPTBB)'),
}
SOURCES = {
    'eng': r'D:\SpaceBook\Books\5th\5th English\JPG',
    'sci': r'D:\SpaceBook\Books\5th\5th General Science\JPG',
    'urdu': r'D:\SpaceBook\Books\5th\5th Urdu\JPG',
    'sst': r'D:\SpaceBook\Books\5th\5th Social Study\JPG',
    'sstum': r'D:\SpaceBook\Books\5th\5th Social Study UM\JPG',
    'isl': r'D:\SpaceBook\Books\5th\5th Islamiat\JPG',
    'pashto': r'D:\SpaceBook\Books\5th\5th Pashto\JPG',
}
JPG_ROOT = Path('D:/SpaceBook/_cls5_jpg')
# Slot order of "original || translation || translation" for books not printed in English.
LANGS = {'urdu': ['ur', 'en', 'ps'], 'isl': ['ur', 'en', 'ps'], 'sstum': ['ur', 'en', 'ps'], 'pashto': ['ps', 'ur', 'en']}
IGNORE = {'not', 'for', 'sale', 'downloaded', 'from', 'awazeinqilab', 'com', 'download', 'millions', 'mcqs', 'books',
          'notes', 'any', 'subject', 'website', 'awaz', 'inqilab', 'free', 'government'}


class BookBuilder(bm.Builder):
    def page(self, idx, text):
        keep = []
        for line in text.splitlines():
            s = line.strip()
            keep.append('// TAB ' + s[5:].strip() if s.startswith('@tab ') else line)
        tabs = [l[7:] for l in keep if l.startswith('// TAB ')]
        super().page(idx, '\n'.join(keep))
        if tabs and self.section is not None:
            for t in tabs:
                self.section.setdefault('tabs', [])
                if t not in self.section['tabs']:
                    self.section['tabs'].append(t)


def load_units(subj):
    f = HERE / subj / 'units.tsv'
    titles, starts, labels = {}, {}, {}
    if f.exists():
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            n, en, ur, ps, start, label = (line.split('\t') + [''] * 6)[:6]
            titles[int(n)] = (en.strip(), ur.strip(), ps.strip())
            if label.strip():
                labels[int(n)] = label.strip()
            starts[int(n)] = int(start) if start.strip().isdigit() else None
    return titles, starts, labels


def load_vocab(subj):
    words = {}
    f = HERE / subj / 'vocab.tsv'
    if f.exists():
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) != 3:
                raise SystemExit(f'bad vocab line in {f.name}: {line}')
            words.setdefault(parts[0].strip().lower(), [parts[1].strip(), parts[2].strip()])
    return words


def ocr_recall(subj, idx, english):
    f = HERE / subj / 'ocr' / f'{idx:03}.json'
    if not f.exists() or subj in LANGS:
        return None
    ocr = ' '.join(l['text'] for l in json.loads(f.read_text(encoding='utf-8'))['lines'] if l['conf'] > 0.8)
    src = [w for w in re.findall(r'[a-z]{3,}', ocr.lower()) if w not in IGNORE]
    if len(src) < 8:
        return None
    stream = re.sub(r'[^a-z]', '', ' '.join(english).lower())
    return round(sum(1 for w in src if w in stream) / len(src), 3)


def main():
    subj = sys.argv[1]
    name, out_file, global_name, title = SUBJECTS[subj]
    total = len(list((JPG_ROOT / subj).glob('[0-9][0-9][0-9].jpg')))
    titles, starts, labels = load_units(subj)
    b = BookBuilder(titles, starts)
    files = sorted((HERE / subj / 'pages').glob('p[0-9][0-9][0-9].txt'))
    for expected, f in enumerate(files):
        if int(f.stem[1:]) != expected:
            raise SystemExit(f'pages must be consecutive: expected p{expected:03}.txt, found {f.name}')
        b.page(expected, f.read_text(encoding='utf-8'))
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f'c5{subj}-s{len(solutions) + 1}'
                    solutions[sid] = owner.pop('sol')
                    owner['solId'] = sid
            if x.get('blocks'):
                extract(x['blocks'])
    units = [b.units[n] for n in sorted(b.units)]
    for u in units:
        for s_ in u['sections']:
            extract(s_['blocks'])
    words = load_vocab(subj)
    for m in b.ledger:
        m['ocrWordRecall'] = None if m['status'] in ('duplicate', 'blank', 'answers') else ocr_recall(subj, m['pdfPage'] - 1, m['english'])
        m.pop('english')
    for u in units:
        if u['number'] in labels:
            u['order'], u['number'] = u['number'], labels[u['number']]
        u['reviewStatus'] = {'reviewedPdfPages': len(u['sourcePdfPages'])}
        for s in u['sections']:
            paras = [x.get('en', '') for x in s['blocks'] if x['t'] in ('h', 'p')]
            s['heading'] = s['title']
            s['headingUrdu'] = s['titleUrdu']
            s['paras'] = paras
            s['text'] = '\n\n'.join(paras)[:6000]
    reviewed = len(b.ledger)
    book = {'subject': subj, 'name': name, 'title': title, 'source': SOURCES[subj], 'totalPdfPages': total,
            'reviewedPdfPages': reviewed, 'frontMatter': b.front, 'backMatter': b.back, 'answers': b.answers,
            'answerPdfPages': b.answer_pages, 'complete': reviewed >= total}
    if subj in LANGS:
        book['langs'] = LANGS[subj]
    js = [f'// Class 5 {name} (KPTBB) — generated by docs/source-verification/class-5/tools/build_book5.py {subj}',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          f'const {global_name} = ' + json.dumps(units, ensure_ascii=False) + ';',
          'if (typeof window !== "undefined") {',
          f'  window.{global_name} = {global_name};',
          '  window.CLS5_BOOKS = window.CLS5_BOOKS || {};',
          f'  window.CLS5_BOOKS[{json.dumps(subj)}] = {{units: {global_name}, book: ' + json.dumps(book, ensure_ascii=False) + ', words: ' + json.dumps(words, ensure_ascii=False) + '};',
          '  window.CLS5_SOLUTIONS = Object.assign(window.CLS5_SOLUTIONS || {}, ' + json.dumps(solutions, ensure_ascii=False) + ');',
          '}', '']
    out = APP / 'js' / out_file
    tmp = out.with_suffix('.js.tmp')
    tmp.write_text('\n'.join(js), encoding='utf-8')
    tmp.replace(out)
    (HERE / subj / 'ledger.json').write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    with (HERE / subj / 'timing.log').open('a', encoding='utf-8') as tl:
        tl.write(datetime.datetime.now().isoformat(timespec='seconds') + '\t' + str(reviewed) + '\n')
    low = [(m['pdfPage'] - 1, m['ocrWordRecall']) for m in b.ledger if m['ocrWordRecall'] is not None and m['ocrWordRecall'] < 0.85]
    untr = [(m['pdfPage'] - 1, m['untranslated'][:3]) for m in b.ledger if m['untranslated']]
    print(f'{subj}: reviewed {reviewed}/{total} pages; {len(units)} units; vocab {len(words)}; answers {len(solutions)}; {out.name} {out.stat().st_size} bytes')
    if bm.ANSWER_WARNINGS:
        print('ANSWER WARNINGS:', bm.ANSWER_WARNINGS)
    if low:
        print('LOW OCR RECALL (scan idx, recall):', low)
    if untr:
        print('UNTRANSLATED:', untr)


if __name__ == '__main__':
    main()
