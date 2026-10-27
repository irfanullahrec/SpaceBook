"""Compares the typed pages of a book with the OCR of its scans: which printed lines are not in any typed page?
    python -X utf8 tools/launch/ocr_compare.py <pages dir> <ocr dir> <offset> [page numbers ...]
  <pages dir>  folder of pNNN.txt, relative to docs/source-verification   e.g. class-9/eng/pages
  <ocr dir>    folder of page-NNN.json (lines with text and conf)        e.g. class-9/english/ocr
  <offset>     page file index + offset = OCR page number                 e.g. 1
Without page numbers: a summary (lines checked, lines not found, pages with 4 or more not found).
With page numbers: the lines of those pages that are not found, to be typed from the scan.
A line counts as found when its first or its last 24 letters and digits occur in any typed page of the book, so an OCR misreading, an underlined word
(<u>) or a reworded item shows up as "not found" too: look at the scan before typing. Only lines of 25 or more characters with confidence above 0.8 count.
Dev-only, never shipped."""
import json, re, glob, os, sys

SV = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs', 'source-verification')


def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        return 2
    pages_dir, ocr_dir, off = sys.argv[1], sys.argv[2], int(sys.argv[3])
    show = [int(x) for x in sys.argv[4:]]
    files = sorted(glob.glob(os.path.join(SV, pages_dir, 'p*.txt')))
    alltext = ''.join(norm(open(f, encoding='utf8').read()) for f in files)

    def missing(n):
        o = os.path.join(SV, ocr_dir, 'page-%03d.json' % (n + off))
        if not os.path.exists(o):
            return None, []
        d = json.load(open(o, encoding='utf8'))
        lines = [l['text'] for l in d['lines'] if len(l['text']) >= 25 and l.get('conf', 1) > 0.8]
        return len(lines), [t for t in lines if len(norm(t)) >= 20 and norm(t)[:24] not in alltext and norm(t)[-24:] not in alltext]

    if show:
        for n in show:
            print('=== p%03d' % n)
            for t in missing(n)[1]:
                print('  -', t[:130])
        return 0
    rows = []
    for f in files:
        n = int(os.path.basename(f)[1:4])
        c, m = missing(n)
        if c is not None:
            rows.append((n, c, len(m)))
    tl, tm = sum(r[1] for r in rows), sum(r[2] for r in rows)
    print('pages', len(rows), 'ocr lines', tl, 'not found', tm, '%.1f%%' % (100 * tm / max(1, tl)))
    bad = [r for r in rows if r[2] >= 4]
    print('pages with >= 4 not found:', len(bad))
    print(' '.join('p%03d:%d/%d' % r for r in bad[:80]))
    return 0


sys.exit(main())
