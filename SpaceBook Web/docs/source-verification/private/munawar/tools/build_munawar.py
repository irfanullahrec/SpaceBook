"""Build one Munawar (Kanz) book from its page-by-page transcriptions.

    python docs/source-verification/private/munawar/tools/build_munawar.py c1-math        one book (id = c<class>-<code>, see registry.py)
    python docs/source-verification/private/munawar/tools/build_munawar.py --all          every book, one process each (a class's tools are imported by name)

Pages:   docs/source-verification/private/munawar/<id>/pages/pNNN.txt   (NNN = 0-based page of the sample PDF; PDF page = NNN + 1)
Units:   <id>/units.tsv   (n, EN, UR, PS, first printed page, optional label) from the book's contents page; without it the book
         has one placeholder unit ("Contents in preparation")
Vocab:   <id>/vocab.tsv   (word, Urdu, Pashto) for the word-meaning table of the Words tab
Output:  js/munawar_c<N>_<code>_book.js which registers window.CLS<N>_BOOKS['mun-<code>'] = {units, book, words} (the class's own reader,
         js/cls<N>_book_reader.js, shows it: the subject id minus "cls<N>-" is the key). Answers/solutions go to window.CLS6_SOLUTIONS
         under 'mc<N><code>-sN' ids (the shared math6 reader looks them up there).

The page syntax, the figure generators and the answer helpers are the class's own pipeline copy (class-<N>/tools/build_math6.py, figs.py,
solve.py): a Munawar page is written exactly like a Government page of the same class. See class-4/tools/build_book4.py for the line syntax
(plus @tab NAME and `sol ANSWER ## EN || UR || PS`).
A book with no pages is still built: every unit of units.tsv is listed with no sections, and the reader says "awaiting page-by-page review".
"""
from pathlib import Path
import datetime
import json
import subprocess
import sys

MUN = Path(__file__).resolve().parents[1]          # docs/source-verification/private/munawar
SRC = MUN.parents[1]                                # docs/source-verification
APP = SRC.parents[1]                                # SpaceBook Web
sys.path.insert(0, str(Path(__file__).resolve().parent))
import registry  # noqa: E402

SLOT_ORDER = {'en': None, 'bl': None, 'ur': ['ur', 'en', 'ps']}   # "original || translation || translation" for Urdu-medium books
PLACEHOLDER = ('Contents in preparation', 'فہرست زیرِ تیاری ہے', 'فهرست د چمتو کېدو په حال کې دی')


def load_units(bid):
    titles, starts, labels = {}, {}, {}
    f = MUN / bid / 'units.tsv'
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


def load_vocab(bid):
    words = {}
    f = MUN / bid / 'vocab.tsv'
    if f.exists():
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) != 3:
                raise SystemExit(f'bad vocab line in {f}: {line}')
            words.setdefault(parts[0].strip().lower(), [parts[1].strip(), parts[2].strip()])
    return words


def build(bid):
    entry = next((e for e in registry.entries() if e['id'] == bid), None)
    if not entry:
        raise SystemExit(f'unknown book {bid}; see registry.py')
    cls, code = entry['cls'], entry['code']
    tools = SRC / f'class-{cls}' / 'tools'
    sys.path.insert(0, str(tools))
    import build_math6 as bm  # the class's own copy: its figure ops and answer helpers

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

    titles, starts, labels = load_units(bid)
    if not titles:
        titles, starts = {1: PLACEHOLDER}, {1: None}
    b = BookBuilder(titles, starts)
    files = sorted((MUN / bid / 'pages').glob('p[0-9][0-9][0-9].txt'))
    for expected, f in enumerate(files):
        if int(f.stem[1:]) != expected:
            raise SystemExit(f'pages must be consecutive: expected p{expected:03}.txt, found {f.name}')
        b.page(expected, f.read_text(encoding='utf-8'))
    if b.stack:
        print('note: open container carried past last reviewed page:', b.stack[-1]['t'])

    prefix = f'mc{cls}{code}'
    solutions = {}

    def extract(list_):
        for x in list_:
            for owner in ([x] if x.get('t') == 'q' else []) + (x.get('parts') or []):
                if owner.get('sol'):
                    sid = f'{prefix}-s{len(solutions) + 1}'
                    solutions[sid] = owner.pop('sol')
                    owner['solId'] = sid
            if x.get('blocks'):
                extract(x['blocks'])

    units = [b.units[n] for n in sorted(b.units)]
    for u in units:
        for s_ in u['sections']:
            extract(s_['blocks'])
    words = load_vocab(bid)
    for m in b.ledger:
        m['ocrWordRecall'] = None
        m.pop('english', None)
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
    reviewed, total = len(b.ledger), entry['pdfPages']
    book = {'subject': entry['key'], 'name': entry['name'], 'title': f"{entry['name']} {cls} (Munawar Publisher, Kanz series)",
            'series': 'munawar', 'publisher': 'Munawar Publisher', 'class': cls,
            'source': f"{registry.PDF_DIR}/{entry['pdf']}", 'totalPdfPages': total,
            'reviewedPdfPages': reviewed, 'frontMatter': b.front, 'backMatter': b.back, 'answers': b.answers,
            'answerPdfPages': b.answer_pages, 'complete': reviewed >= total}
    if SLOT_ORDER.get(entry['medium']):
        book['langs'] = SLOT_ORDER[entry['medium']]
    glob = f'MUNAWAR_C{cls}_{code.upper()}_DATA'
    js = [f'// Munawar {entry["name"]} {cls} - generated by docs/source-verification/private/munawar/tools/build_munawar.py {bid}',
          '// Transcribed page by page from the publisher\'s sample PDF; edit the page transcriptions, not this file.',
          f'const {glob} = ' + json.dumps(units, ensure_ascii=False) + ';',
          'if (typeof window !== "undefined") {',
          f'  window.{glob} = {glob};',
          f'  window.CLS{cls}_BOOKS = window.CLS{cls}_BOOKS || {{}};',
          f'  window.CLS{cls}_BOOKS[{json.dumps(entry["key"])}] = {{units: {glob}, book: ' + json.dumps(book, ensure_ascii=False) + ', words: ' + json.dumps(words, ensure_ascii=False) + '};',
          '  window.CLS6_SOLUTIONS = Object.assign(window.CLS6_SOLUTIONS || {}, ' + json.dumps(solutions, ensure_ascii=False) + ');',
          '}', '']
    out = APP / 'js' / entry['dataFile']
    tmp = out.with_suffix('.js.tmp')
    tmp.write_text('\n'.join(js), encoding='utf-8', newline='\n')
    tmp.replace(out)
    (MUN / bid).mkdir(parents=True, exist_ok=True)
    (MUN / bid / 'ledger.json').write_text(json.dumps(b.ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    untr = [(m['pdfPage'] - 1, m['untranslated'][:3]) for m in b.ledger if m['untranslated']]
    print(f'{bid}: reviewed {reviewed}/{total} pages; {len(units)} units; vocab {len(words)}; answers {len(solutions)}; {out.name} {out.stat().st_size} bytes')
    if bm.ANSWER_WARNINGS:
        print('ANSWER WARNINGS:', bm.ANSWER_WARNINGS)
    if untr:
        print('UNTRANSLATED:', untr)


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    if sys.argv[1] == '--all':
        failed = []
        for e in registry.entries():
            r = subprocess.run([sys.executable, '-P', str(Path(__file__)), e['id']])
            if r.returncode:
                failed.append(e['id'])
        if failed:
            raise SystemExit('failed: ' + ', '.join(failed))
        return
    build(sys.argv[1])


if __name__ == '__main__':
    main()
