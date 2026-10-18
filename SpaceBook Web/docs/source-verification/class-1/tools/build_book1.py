"""Build a Class 1 textbook (any subject, Mathematics included) from its page-by-page transcriptions.

    python docs/source-verification/class-1/tools/build_book1.py SUBJ   (SUBJ: math, eng, isl, nazira, pashto, drawing)

Pages:   docs/source-verification/class-1/<SUBJ>/pages/pNNN.txt  (NNN = 0-based scan index; PDF page = NNN + 1)
Scans:   D:/SpaceBook/_cls1_jpg/<SUBJ>/NNN.jpg  (hard links to the Books/1st scans; see SOURCES)
Units:   <SUBJ>/units.tsv  (number, EN, UR, PS, first printed page, optional label) from the book's contents page.
Output:  js/<name>_1_book.js — registers window.CLS1_BOOKS[SUBJ] for js/cls1_book_reader.js. The legacy
         js/<name>_1_data.js files are left in place (copies in class-1/legacy-backup/).
         Answers go to window.CLS6_SOLUTIONS under 'c1<subj>-sN' ids (looked up by the shared math6_reader).

Page syntax: as documented in build_math6.py, plus the figs1.py generators (cnt, shapes, tens, cards, train,
tframe, hand) and
  @tab NAME        the current section also appears in subject tab NAME
  sol ANSWER ## EN || UR || PS     SpaceBook answer for the last question/part (shown behind a button)
"""
from pathlib import Path
import json, re, sys, datetime
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_math6 as bm

HERE = bm.HERE          # docs/source-verification/class-1
APP = bm.APP            # SpaceBook Web
SUBJECTS = {
    'math': ('Mathematics', 'math_1_book.js', 'MATH_1_BOOK', 'Mathematics 1 (KPTBB, based on Curriculum 2020, Test Edition)'),
    'eng': ('English', 'english_1_book.js', 'ENGLISH_1_BOOK', 'English 1 (KPTBB)'),
    'isl': ('Islamyat', 'islamyat_1_book.js', 'ISLAMYAT_1_BOOK', 'Islamiat 1 (KPTBB)'),
    'nazira': ('Nazira Quran', 'nazira_1_book.js', 'NAZIRA_1_BOOK', 'Nazira Quran 1 (KPTBB)'),
    'pashto': ('Pashto', 'pashto_1_book.js', 'PASHTO_1_BOOK', 'Pashto 1 (KPTBB)'),
    'drawing': ('Drawing', 'drawing_1_book.js', 'DRAWING_1_BOOK', 'Creative Arts and Drawing 1 (KPTBB)'),
    'urdu': ('Urdu', 'urdu_1_book.js', 'URDU_1_BOOK', 'Urdu 1 (KPTBB) — MISSING SOURCE'),
    'gk': ('General Knowledge', 'gk_1_book.js', 'GK_1_BOOK', 'General Knowledge 1 (KPTBB) — MISSING SOURCE'),
}
SRC = 'D:/SpaceBook/Books/1st/'
SOURCES = {
    'math': SRC + '1st Maths/JPG (146 scans) and PDF/Math book 1 KPTBB.pdf',
    'eng': SRC + '1st English/PDF/English book 1  KPTBB.pdf',
    'isl': SRC + '1st Islamyat/JPG and PDF/Islamiat book  KPTBB.pdf',
    'nazira': SRC + '1st Nazera/JPG and PDF/Nazera book 1 KPTBB.pdf',
    'pashto': SRC + '1st Pashto/JPG and PDF/Pashto book 1 KPTBB.pdf',
    'drawing': SRC + '1st Drawing/PDF/Drawing Book 1 KPTBB.pdf',
    'urdu': 'MISSING SOURCE',
    'gk': 'MISSING SOURCE',
}
JPG_ROOT = Path('D:/SpaceBook/_cls1_jpg')
# Slot order of "original || translation || translation" for books not printed in English.
LANGS = {'isl': ['ur', 'en', 'ps'], 'nazira': ['ur', 'en', 'ps'], 'pashto': ['ps', 'ur', 'en'], 'drawing': ['ur', 'en', 'ps'], 'urdu': ['ur', 'en', 'ps'], 'gk': ['ur', 'en', 'ps']}
IGNORE = {'not', 'for', 'sale', 'downloaded', 'from', 'awazeinqilab', 'com', 'download', 'millions', 'mcqs', 'books',
          'notes', 'any', 'subject', 'website', 'awaz', 'inqilab', 'free', 'government', 'perfect24u'}


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
    # <subj>/reorder.txt: lines "POS SCAN" -- read scan SCAN at reading position POS (for scans bound out of order)
    remap = {}
    ro = HERE / subj / 'reorder.txt'
    if ro.exists():
        for ln in ro.read_text(encoding='utf-8').splitlines():
            if ln.strip() and not ln.startswith('#'):
                pos, scan = map(int, ln.split()[:2]); remap[pos] = scan
        if sorted(remap) != sorted(remap.values()):
            raise SystemExit('reorder.txt must be a permutation of the same positions')
    for expected in range(len(files)):
        idx = remap.get(expected, expected)
        if idx >= len(files):
            raise SystemExit(f'reorder.txt: scan {idx} not written yet')
        b.page(idx, files[idx].read_text(encoding='utf-8'))
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f'c1{subj}-s{len(solutions) + 1}'
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
            'answerPdfPages': b.answer_pages, 'complete': total > 0 and reviewed >= total}
    if subj in LANGS:
        book['langs'] = LANGS[subj]
    js = [f'// Class 1 {name} (KPTBB) — generated by docs/source-verification/class-1/tools/build_book1.py {subj}',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          f'const {global_name} = ' + json.dumps(units, ensure_ascii=False) + ';',
          'if (typeof window !== "undefined") {',
          f'  window.{global_name} = {global_name};',
          '  window.CLS1_BOOKS = window.CLS1_BOOKS || {};',
          f'  window.CLS1_BOOKS[{json.dumps(subj)}] = {{units: {global_name}, book: ' + json.dumps(book, ensure_ascii=False) + ', words: ' + json.dumps(words, ensure_ascii=False) + '};',
          '  window.CLS6_SOLUTIONS = Object.assign(window.CLS6_SOLUTIONS || {}, ' + json.dumps(solutions, ensure_ascii=False) + ');',
          '}', '']
    out = APP / 'js' / out_file
    tmp = out.with_suffix('.js.tmp')
    tmp.write_text('\n'.join(js), encoding='utf-8')
    tmp.replace(out)
    (HERE / subj / 'ledger.json').write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    with (HERE / subj / 'timing.log').open('a', encoding='utf-8') as tl:
        tl.write(datetime.datetime.now().isoformat(timespec='seconds') + '\t' + str(reviewed) + '\n')
    untr = [(m['pdfPage'] - 1, m['untranslated'][:3]) for m in b.ledger if m['untranslated']]
    print(f'{subj}: reviewed {reviewed}/{total} pages; {len(units)} units; vocab {len(words)}; answers {len(solutions)}; {out.name} {out.stat().st_size} bytes')
    if bm.ANSWER_WARNINGS:
        print('ANSWER WARNINGS:', bm.ANSWER_WARNINGS)
    if untr:
        print('UNTRANSLATED:', untr)


if __name__ == '__main__':
    main()
