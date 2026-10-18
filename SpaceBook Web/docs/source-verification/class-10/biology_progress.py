"""Durable Class 10 Biology progress: page records + inventory + checkpoint.

Usage (from any directory):
  python -X utf8 biology_progress.py record <json-file-with-list-of-records> [--next N] [--note "..."] [--chapter "..."]
Each record: {"pdfPage":N,"printedPage":"n"|null,"status":"corrected|verified-unchanged|excluded|unresolved|inspected",
              "kind":"...","compared":"...","data":"js/...","evidence":"tmp/class-10-biology/bio-NNN.png","validation":"...",
              "unresolved":"..." (optional)}
"""
import json, sys, time
from pathlib import Path

HERE = Path(__file__).parent
PAGES = HERE / 'biology-pages.json'
INV = HERE / 'inventory.json'
CKPT = HERE / 'checkpoint.json'
BOOK_ID = 'biology-Biology Class 10 kpk book'
PDF = r'D:\SpaceBook\Books\10th\10th Bio\PDF\Biology Class 10 kpk book.pdf'
TOTAL = 197


def load(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def dump(path, data):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
    tmp.replace(path)


def record(new_records, next_page=None, note=None, chapter=None):
    pages = {r['pdfPage']: r for r in load(PAGES, [])}
    for r in new_records:
        r['updatedAt'] = time.strftime('%Y-%m-%dT%H:%M:%S')
        pages[r['pdfPage']] = r
    ordered = [pages[k] for k in sorted(pages)]
    dump(PAGES, ordered)

    inv = load(INV, {'subjects': []})
    for subj in inv['subjects']:
        for book in subj.get('books', []):
            if book['id'] == BOOK_ID:
                st = lambda s: sorted({r['pdfPage'] for r in ordered if r['status'] == s})
                book['correctedPages'] = st('corrected')
                book['verifiedUnchangedPages'] = st('verified-unchanged')
                book['excludedPages'] = st('excluded')
                book['unresolvedPages'] = sorted({r['pdfPage'] for r in ordered if r.get('unresolved')})
                done = sorted({r['pdfPage'] for r in ordered if r['status'] in ('corrected', 'verified-unchanged', 'excluded')})
                last = 0
                for p in done:
                    if p == last + 1: last = p
                    else: break
                book['lastFullyVerifiedPage'] = last
                book['nextPage'] = (next_page or last + 1) if last < TOTAL else None
                book['status'] = 'completed' if last >= TOTAL and not book['unresolvedPages'] else ('reviewed-with-unresolved' if last >= TOTAL else 'in-progress')
                book['relationship'] = 'Single complete scanned PDF (197 pages, no text layer). JPG folder holds the same 197 scans at higher resolution (used for crops only). No chapter splits or alternate editions present.'
                book['pageReferences'] = [{'pdfPage': r['pdfPage'], 'printedPage': r.get('printedPage')} for r in ordered]
                if chapter: book['currentChapter'] = chapter
                inv['updatedAt'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                dump(INV, inv)
                break

    ck = load(CKPT, {})
    done = sorted({r['pdfPage'] for r in ordered if r['status'] in ('corrected', 'verified-unchanged', 'excluded')})
    last = 0
    for p in done:
        if p == last + 1: last = p
        else: break
    nxt = next_page or last + 1
    ck.update({
        'currentSubject': 'Biology',
        'userInstructionUpdate': '2026-10-12: User re-issued Class 10 instructions with BIOLOGY FIRST; after Biology continue Physics, Chemistry, Statistics, English, Urdu, Pakistan Studies, Computer Science, Civics, Economics, General Science, Drawing, HPE, Islamiat Compulsory, Islamiat Ikhtiari, Islamic History, Mutalia-e-Quran, then remaining. Mathematics excluded. No browser testing. English review (pending Unit 7 page 77 repair) and Urdu/other subjects resume after Biology.',
        'sourcePdf': PDF,
        'currentBook': PDF,
        'lastFullyVerifiedPdfPage': last,
        'nextPdfPage': nxt,
        'nextAction': f'Render and inspect Biology PDF page {nxt} (printed {nxt - 3 if nxt > 3 else "front matter"}); compare with js/biology_10_unit*_source.js overlay and reader; correct, save, record.' + (f' Note: {note}' if note else ''),
        'implementation': 'Class 10 Biology: js/biology_10_reader.js (wraps renderScienceLessonSubContent for bio/cls10 owned units), js/biology_10_front_source.js (cover/title/contents), js/biology_10_unit<NN>_source.js per unit; wired in index.html under the shared lock via docs/source-verification/class-10/biology_tools.py; checks via biology_check.cjs.',
        'currentChapter': chapter or ck.get('currentChapter'),
        'biologyProgress': {
            'inspectedPages': len(ordered),
            'correctedPages': len([r for r in ordered if r['status'] == 'corrected']),
            'verifiedUnchangedPages': len([r for r in ordered if r['status'] == 'verified-unchanged']),
            'excludedPages': len([r for r in ordered if r['status'] == 'excluded']),
            'unresolvedItems': [{'pdfPage': r['pdfPage'], 'issue': r['unresolved']} for r in ordered if r.get('unresolved')],
            'remainingPdfPages': TOTAL - last
        },
        'updatedAt': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    })
    dump(CKPT, ck)
    return last, nxt


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == 'record':
        recs = json.loads(Path(args[1]).read_text(encoding='utf-8'))
        nxt = int(args[args.index('--next') + 1]) if '--next' in args else None
        note = args[args.index('--note') + 1] if '--note' in args else None
        chapter = args[args.index('--chapter') + 1] if '--chapter' in args else None
        last, nxt = record(recs, nxt, note, chapter)
        print(f'saved; lastFullyVerifiedPdfPage={last} nextPdfPage={nxt}')
