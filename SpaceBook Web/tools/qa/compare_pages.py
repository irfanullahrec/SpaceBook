"""Triage for page-by-page proofreading: compare the OCR of each scan page with the data strings recorded against that page.

    python tools/qa/compare_pages.py <page_text.json> <ocr dir> [--top N] [--json out.json] [--pages a-b]

Both sides are reduced to lower-case letters (OCR drops spaces, so word tokens are unreliable) and compared by character 5-gram
coverage:
  scan_lines   = OCR lines (>= 14 letters) whose 5-grams are mostly missing from the data of the WHOLE book: text on the scan that the
                 data does not carry anywhere (missing line, or OCR junk);
  data_strings = data strings whose 5-grams are mostly missing from the OCR of the page and its two neighbours (page attribution in the
                 data drifts by a page): typo-ridden, not printed, or OCR junk;
  suspect_words = words (>= 6 letters) of well-covered data strings that do not occur in the OCR letters of those three pages at all:
                 typo candidates.
The score is what a person has to look at; the worst pages are opened next to their image.
"""
import sys, os, re, json

META = re.compile(r'authored_aligned|source_verified|printed|SpaceBook|transcri|decorative|retained|preserved|scan prints|navigation', re.I)


def letters(s):
    return re.sub(r'[^a-z]', '', s.lower())


def grams(s, n=5):
    return {s[i:i + n] for i in range(len(s) - n + 1)}


def main():
    pt, od = sys.argv[1], sys.argv[2]
    top = int(sys.argv[sys.argv.index('--top') + 1]) if '--top' in sys.argv else 15
    rng = None
    if '--pages' in sys.argv:
        a, b = sys.argv[sys.argv.index('--pages') + 1].split('-'); rng = (int(a), int(b))
    pages = json.load(open(pt, encoding='utf8'))
    book_g = set()
    for lst in pages.values():
        for s in lst:
            if not META.search(s): book_g |= grams(letters(s))
    texts = {}
    for fn in os.listdir(od):
        m = re.match(r'p(\d+)\.txt$', fn)
        if m: texts[int(m.group(1))] = open(os.path.join(od, fn), encoding='utf8').read()
    res = []
    for n in sorted(texts):
        if rng and not (rng[0] <= n <= rng[1]): continue
        ocr_lines = texts[n].split('\n')
        ocr_all = letters(' '.join(ocr_lines))
        data_strs = [x for x in pages.get(str(n), []) if not META.search(x)]
        near_all = letters(' '.join(texts.get(k, '') for k in (n - 1, n, n + 1)))
        og = grams(near_all)
        scan_lines = []
        for l in ocr_lines:
            ll = letters(l)
            if len(ll) < 14 or 'inqilab' in ll or 'awaz' in ll: continue
            g = grams(ll)
            if g and len(g & book_g) / len(g) < 0.6: scan_lines.append(l.strip())
        data_unc, suspect = [], []
        for s in data_strs:
            ls = letters(s)
            if len(ls) < 14: continue
            g = grams(ls)
            cov = len(g & og) / len(g) if g else 1
            if cov < 0.6: data_unc.append(s.strip()[:120])
            elif cov < 0.98:
                for w in re.findall(r'[A-Za-z]{6,}', s):
                    if w.lower() not in near_all: suspect.append(w)
        res.append({'page': n, 'ocr_letters': len(ocr_all), 'data_strings_n': len(data_strs), 'scan_lines': scan_lines, 'data_strings': data_unc,
                    'suspect_words': sorted(set(suspect)), 'score': len(scan_lines) + len(data_unc) + len(set(suspect))})
    res.sort(key=lambda r: -r['score'])
    if '--json' in sys.argv: json.dump(res, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)
    print('pages', len(res), 'clean (score 0):', sum(1 for r in res if r['score'] == 0), 'score >= 5:', sum(1 for r in res if r['score'] >= 5))
    for r in res[:top]:
        print('p%d score %d (ocr %d letters, %d data strings)' % (r['page'], r['score'], r['ocr_letters'], r['data_strings_n']))
        for l in r['scan_lines'][:4]: print('   SCAN :', l[:110])
        for l in r['data_strings'][:3]: print('   DATA :', l[:110])
        if r['suspect_words']: print('   WORDS:', ' '.join(r['suspect_words'][:15]))


main()
