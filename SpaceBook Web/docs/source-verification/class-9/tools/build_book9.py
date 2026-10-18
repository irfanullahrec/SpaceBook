"""Build a Class 9 textbook (Islamiat, Mutalia-e-Quran, HPE, Drawing) from page-by-page transcriptions.

    python -X utf8 tools/build_book9.py SUBJ   (SUBJ: isl, quran, hpe, drawing)

Same page syntax, builder and reader as the Class 6/8/10 books (class-6/tools/build_book6.py, build_math6.py);
registry window.CLS9_BOOKS, rendered by js/cls6_book_reader.js for classId 'cls9'.
Pages: class-9/<SUBJ>/pages/pNNN.txt, one file per source page (NNN = 0-based index into SOURCES).
Output is staged at class-9/<SUBJ>/build/<file>; tools/wire_book9.py copies it into js/.
"""
from pathlib import Path
import json, sys, datetime, os, re

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parent / 'class-6' / 'tools'))
import build_math6 as bm  # noqa: E402
import build_book6 as b6  # noqa: E402

b6.HERE = HERE
B9 = 'D:/SpaceBook/Books/9th/'
SOURCES = {'isl': {'pdf': [B9 + '9th islamyat/PDF/9th Islamyat.pdf']},
           'quran': {'pdf': [B9 + '9th MQ/PDF/Mutlia_e_Quran_Book_KPK_9.pdf']},
           'hpe': {'pdf': [B9 + '9th  HPE/PDF/HPE book UM 9th class KPK.pdf']},
           'drawing': {'jpg': B9 + '9th Drawing/JPG'},
           'sci': {'jpg': B9 + '9th General Science/JPG', 'pattern': r'General Science 9th book EM_page_\d{3}\.jpg'},
           'pakstudy': {'jpg': B9 + '9th Pak Study/JPG', 'pattern': r'Pak study _\d+\.jpg'},
           'eng': {'pdf': [B9 + '9th English/PDF/9th English.pdf']},
           'comp': {'jpg': B9 + '9th Computer Science/jpg', 'pattern': r'\d{3}_.*\.jpg'}}
SUBJECTS = {
    'isl': ('Islamiat', 'islamiat_9_data.js', 'ISLAMIAT_9_DATA', 'Islamiat 9 (KPTBB)'),
    'quran': ('Mutalia-e-Quran', 'mutalia_quran_9_data.js', 'MUTALIA_QURAN_9_DATA', 'Mutalia-e-Quran 9 (KPTBB)'),
    'hpe': ('Health & Physical Education', 'hpe_9_data.js', 'HPE_9_DATA', 'Health & Physical Education 9 (KPTBB, Urdu medium)'),
    'drawing': ('Art & Model Drawing', 'drawing_9_data.js', 'DRAWING_9_DATA', 'Art and Model Drawing 9 (KPTBB, English medium)'),
    'sci': ('General Science', 'general_science_9_book.js', 'GENERAL_SCIENCE_9_BOOK', 'General Science 9 (KPTBB, English medium)'),
    'pakstudy': ('Pakistan Studies', 'pakstudy_9_book.js', 'PAKSTUDY_9_BOOK', 'Mutalia-e-Pakistan 9 (KPTBB, Urdu medium)'),
    'eng': ('English', 'english_9_book.js', 'ENGLISH_9_BOOK', 'A Textbook of English 9 (KPTBB, English medium)'),
    'comp': ('Computer Science', 'computer_9_data.js', 'COMPUTER_9_DATA', 'A Textbook of Computer Science (KPTBB Grade X book, English medium) used for Class 9'),
}
LANGS = {'isl': ['ur', 'en', 'ps'], 'quran': ['ur', 'en', 'ps'], 'hpe': ['ur', 'en', 'ps'], 'pakstudy': ['ur', 'en', 'ps']}


def source_total(subj):
    s = SOURCES[subj]
    if 'pdf' in s:
        import pymupdf
        return sum(pymupdf.open(p).page_count for p in s['pdf'])
    return len([f for f in os.listdir(s['jpg']) if re.fullmatch(s.get('pattern', r'\d+\.jpg'), f)])


def main():
    subj = sys.argv[1]
    name, legacy_file, global_name, title = SUBJECTS[subj]
    total = source_total(subj)
    titles, starts, labels = b6.load_units(subj)
    b = b6.BookBuilder(titles, starts)
    files = sorted((HERE / subj / 'pages').glob('p[0-9][0-9][0-9].txt'))
    for expected, f in enumerate(files):
        if int(f.stem[1:]) != expected:
            raise SystemExit(f'pages must be consecutive: expected p{expected:03}.txt, found {f.name}')
        txt = f.read_text(encoding='utf-8')
        if '@status lesson' in txt:
            b.back_mode = False
        b.page(expected, txt)
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f'c9{subj}-s{len(solutions) + 1}'
                    solutions[sid] = owner.pop('sol')
                    owner['solId'] = sid
            if x.get('blocks'):
                extract(x['blocks'])
    units = [b.units[n] for n in sorted(b.units)]
    for u in units:
        for s_ in u['sections']:
            extract(s_['blocks'])
    words = b6.load_vocab(subj)
    for m in b.ledger:
        m['ocrWordRecall'] = None
        m.pop('english')
    empty = []
    for u in units:
        if u['number'] in labels:
            u['order'], u['number'] = u['number'], labels[u['number']]
        u['reviewStatus'] = {'reviewedPdfPages': len(u['sourcePdfPages'])}
        u.setdefault('exercise', {'source': 'exercises', 'count': len(u.get('exercises') or [])})
        u.setdefault('sloBank', {'source': 'slos'})
        if not u['sections']:
            empty.append(u['number'])
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
    J = lambda o: json.dumps(o, ensure_ascii=False).replace('{{OR}}', '||').replace('{{BAR}}', '|')
    js = [f'// Class 9 {name} (KPTBB) — generated by docs/source-verification/class-9/tools/build_book9.py {subj}',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          f'const {global_name} = ' + J(units) + ';',
          'if (typeof window !== "undefined") {',
          f'  window.{global_name} = {global_name};',
          '  window.CLS9_BOOKS = window.CLS9_BOOKS || {};',
          f'  window.CLS9_BOOKS[{json.dumps(subj)}] = {{units: {global_name}, book: ' + J(book) + ', words: ' + J(words) + '};',
          '  window.CLS6_SOLUTIONS = Object.assign(window.CLS6_SOLUTIONS || {}, ' + J(solutions) + ');',
          '}', '']
    out = HERE / subj / 'build' / legacy_file
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('\n'.join(js), encoding='utf-8')
    (HERE / subj / 'ledger.json').write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    with (HERE / subj / 'timing.log').open('a', encoding='utf-8') as tl:
        tl.write(datetime.datetime.now().isoformat(timespec='seconds') + '\t' + str(reviewed) + '\n')
    untr = [(m['pdfPage'] - 1, m['untranslated'][:3]) for m in b.ledger if m.get('untranslated')]
    print(f'{subj}: reviewed {reviewed}/{total} pages; {len(units)} units; empty units {empty}; vocab {len(words)}; answers {len(solutions)}; {out.name} {out.stat().st_size} bytes')
    if untr:
        print('UNTRANSLATED:', untr)


if __name__ == '__main__':
    main()
