"""Build the Class 12 Mathematics textbook from its page-by-page transcriptions.

    python tools/build_book12.py math

Same page syntax, builder and reader as the Class 6/8 books (class-6/tools/build_book6.py); registry window.CLS12_BOOKS,
rendered by js/cls6_book_reader.js for classId 'cls12'. Pages: class-12/math/pages/pNNN.txt, one file per PDF page in
source order (SOURCES below). Page totals come from the source PDFs; renders for reading live outside the repo.
"""
from pathlib import Path
import json, sys, datetime

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parent / 'class-6' / 'tools'))
import build_math6 as bm
import build_book6 as b6

APP = HERE.parents[2]
b6.HERE = HERE                     # load_units / load_vocab / ocr_recall read class-8/<subj>/...
SOURCES = {'math': ['D:/SpaceBook/Books/12th/12th Maths/JPG'],
           'stat': ['D:/SpaceBook/Books/12th/12th Statistics/PDF/Statistics Book for 12 class KPTBB.pdf'],
           'pakstudy': ['D:/SpaceBook/Books/12th/12th Pak Studies/JPG']}
SUBJECTS = {
    'math': ('Mathematics', 'math_12_pagebook_data.js', 'MATH_12_PAGEBOOK_DATA', 'Mathematics 12 (KPTBB)'),
    'stat': ('Statistics', 'statistics_12_book_data.js', 'STATISTICS_12_BOOK_DATA', 'Statistics 12 (KPTBB)'),
    'pakstudy': ('Pakistan Studies', 'pakstudy_12_book.js', 'PAKSTUDY_12_BOOK', 'Mutalia-e-Pakistan 12 (KPTBB, Urdu medium)'),
}
BOOK_SOURCE = {'math': ['12th Maths/JPG'], 'stat': ['12th Statistics/PDF'], 'pakstudy': ['12th Pak Studies/JPG']}
BOOK_SOURCE_X = BOOK_SOURCE


sys.path.insert(0, str(HERE / 'book12'))
import importlib
_cfg = {}
for _k in ('pakstudy', 'hpe', 'civics', 'quran', 'islhist', 'islopt', 'econ', 'urdu', 'eng', 'comp', 'phys', 'chem', 'bio'):
    if (HERE / 'book12' / 'cfgs' / (_k + '.py')).exists():
        try:
            _m = importlib.import_module('cfgs.' + _k)
            if hasattr(_m, 'BOOK_NAME') and hasattr(_m, 'TOTAL_JPG'):
                _cfg[_k] = _m
        except Exception as _e:   # a config that is not finished must not stop the other builds
            print('note: cfg', _k, 'not loaded:', _e)
for _k, _c in _cfg.items():
    if hasattr(_c, 'BOOK_NAME'):
        SUBJECTS[_k] = _c.BOOK_NAME
        BOOK_SOURCE_X[_k] = _c.BOOK_SOURCE


def source_pages(subj):
    """One scan (JPG) per book page; pNNN = NNN-th file in sorted order (see math12/pagemap.py)."""
    if subj in _cfg:
        return list(range(_cfg[subj].TOTAL_JPG))
    if subj == 'stat':   # cover + PDF p3..p176 split into left/right halves (see stat12/pagemap.py)
        return list(range(349))
    return sorted(Path(SOURCES[subj][0]).glob('*_page_*.jpg'))


# Urdu-medium books: slot order of "original || translation || translation" (see math6_reader.js LANGS)
LANGS = {}


def close_stray_examples(txt, stack):
    """Maths pages often omit `endexample`; close an example left open when the next example, exercise, section or unit begins."""
    out = []
    for line in txt.split('\n'):
        op = line.split(' ', 1)[0]
        if op in ('example', 'exercise', '@sec', '@unit') or op in ('endbox', 'endexercise') and stack and stack[-1] != op[3:]:
            while stack and stack[-1] == 'example' and (op != 'endbox' or 'box' in stack):
                out.append('endexample')
                stack.pop()
            if op in ('@sec', '@unit'):
                while stack and stack[-1] == 'example':
                    out.append('endexample')
                    stack.pop()
        if op in ('box', 'example', 'exercise'):
            stack.append(op)
        elif op in ('endbox', 'endexample', 'endexercise') and stack:
            stack.pop()
        out.append(line)
    return '\n'.join(out)


def main():
    subj = sys.argv[1]
    name, legacy_file, global_name, title = SUBJECTS[subj]
    total = len(source_pages(subj))
    titles, starts, labels = b6.load_units(subj)
    b = b6.BookBuilder(titles, starts)
    open_blocks = []
    files = sorted((HERE / subj / 'pages').glob('p[0-9][0-9][0-9].txt'))
    for expected, f in enumerate(files):
        if int(f.stem[1:]) != expected:
            raise SystemExit(f'pages must be consecutive: expected p{expected:03}.txt, found {f.name}')
        txt = f.read_text(encoding='utf-8')
        if subj == 'math':
            txt = close_stray_examples(txt, open_blocks)
        if '@status lesson' in txt:
            b.back_mode = False   # a stray back-matter page (e.g. a back cover) mid-book must not swallow later lessons
        b.page(expected, txt)
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f'c12{subj}-s{len(solutions) + 1}'
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
        m['ocrWordRecall'] = None if m['status'] in ('duplicate', 'blank', 'answers') else b6.ocr_recall(subj, m['pdfPage'] - 1, m['english'])
        m.pop('english')
    for u in units:
        if u['number'] in labels:
            u['order'], u['number'] = u['number'], labels[u['number']]
        u['reviewStatus'] = {'reviewedPdfPages': len(u['sourcePdfPages'])}
        # legacy URDU_10_DATA consumers (tools/validate.js) look for a truthy `exercise`; the reader uses `exercises`
        u.setdefault('exercise', {'source': 'exercises', 'count': len(u.get('exercises') or [])})
        u.setdefault('sloBank', {'source': 'slos'})
        for s in u['sections']:
            paras = [x.get('en', '') for x in s['blocks'] if x['t'] in ('h', 'p')]
            s['heading'] = s['title']
            s['headingUrdu'] = s['titleUrdu']
            s['paras'] = paras
            s['text'] = '\n\n'.join(paras)[:6000]
    reviewed = len(b.ledger)
    book = {'subject': subj, 'name': name, 'title': title, 'source': BOOK_SOURCE[subj], 'totalPdfPages': total,
            'reviewedPdfPages': reviewed, 'frontMatter': b.front, 'backMatter': b.back, 'answers': b.answers,
            'answerPdfPages': b.answer_pages, 'complete': reviewed >= total}
    if subj in LANGS:
        book['langs'] = LANGS[subj]
    if subj in _cfg:
        book['tabs'] = list(_cfg[subj].TABS)   # the other tabs (summary, SLOs, word count) keep the SpaceBook study views
        book['langs'] = list(_cfg[subj].LANGS)
    if subj in ('math', 'stat'):
        book['byNumber'] = True   # chapter list stays DATA.phys10Chapters/chem10Chapters; reader matches units by number
    # "||" and "|" are DSL separators; pages write the C OR operator as {{OR}} and a literal bar as {{BAR}}.
    J = lambda o: json.dumps(o, ensure_ascii=False).replace('{{OR}}', '||').replace('{{BAR}}', '|')
    js = [f'// Class 12 {name} (KPTBB) — generated by docs/source-verification/class-12/tools/build_book12.py {subj}',
          '// Source-reviewed page by page; edit the page transcriptions, not this file.',
          f'const {global_name} = ' + J(units) + ';',
          'if (typeof window !== "undefined") {',
          f'  window.{global_name} = {global_name};',
          '  window.CLS12_BOOKS = window.CLS12_BOOKS || {};',
          f'  window.CLS12_BOOKS[{json.dumps(subj)}] = {{units: {global_name}, book: ' + J(book) + ', words: ' + J(words) + '};',
          '  window.CLS6_SOLUTIONS = Object.assign(window.CLS6_SOLUTIONS || {}, ' + J(solutions) + ');',
          '}', '']
    import os
    out = Path(os.environ['BOOK12_OUT']) if os.environ.get('BOOK12_OUT') else (HERE / subj / 'build' / legacy_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('\n'.join(js), encoding='utf-8')
    (HERE / subj / 'ledger.json').write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    with (HERE / subj / 'timing.log').open('a', encoding='utf-8') as tl:
        tl.write(datetime.datetime.now().isoformat(timespec='seconds') + '\t' + str(reviewed) + '\n')
    low = [(m['pdfPage'] - 1, m['ocrWordRecall']) for m in b.ledger if m['ocrWordRecall'] is not None and m['ocrWordRecall'] < 0.85]
    untr = [(m['pdfPage'] - 1, m['untranslated'][:3]) for m in b.ledger if m['untranslated']]
    print(f'{subj}: reviewed {reviewed}/{total} pages; {len(units)} units; vocab {len(words)}; answers {len(solutions)}; {out.name} {out.stat().st_size} bytes')
    if low:
        print('LOW OCR RECALL (scan idx, recall):', low)
    if untr:
        print('UNTRANSLATED:', untr)


if __name__ == '__main__':
    main()
