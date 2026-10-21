"""Word-level differences between a book's data and the OCR of its scan: data word (>= 5 letters) that is not an OCR word of the page or its
neighbours but has an OCR word at edit distance 1-2 -> a typo on one side (the scan is the judge).

    python tools/qa/word_pairs.py <page_text.json> <ocr dir> [--min-len 5]

Prints "page data-word | ocr-word". Words made only of capitals, or containing digits, are skipped."""
import sys, os, re, json
from difflib import SequenceMatcher


def lev(a, b, mx=2):
    if abs(len(a) - len(b)) > mx: return mx + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        if min(cur) > mx: return mx + 1
        prev = cur
    return prev[-1]


pt, od = sys.argv[1], sys.argv[2]
raw = open('js/word_stats_words.js', encoding='utf8').read()
_j = json.loads(raw[raw.index('{'):raw.rindex('}') + 1])
_D = _j['SB_WORD_STATS_WORDS'] if 'SB_WORD_STATS_WORDS' in _j else _j
freq = dict(zip(_D['words']['en'].split(chr(10)), [int(x, 36) for x in _D['freq']['en'].split(',')]))
ml = int(sys.argv[sys.argv.index('--min-len') + 1]) if '--min-len' in sys.argv else 5
pages = json.load(open(pt, encoding='utf8'))
ocrw = {}
for f in os.listdir(od):
    m = re.match(r'p(\d+)\.txt$', f)
    if m: ocrw[int(m.group(1))] = set(re.findall(r"[A-Za-z]+", open(os.path.join(od, f), encoding='utf8').read().lower()))
allocr = set().union(*ocrw.values()) if ocrw else set()
META = re.compile(r'authored_aligned|source_verified|SpaceBook|transcri|decorative|retained|preserved|scan prints|navigation', re.I)
out = []
for pg in sorted(pages, key=int):
    n = int(pg)
    near = ocrw.get(n, set()) | ocrw.get(n - 1, set()) | ocrw.get(n + 1, set())
    if not near: continue
    seen = set()
    for s in pages[pg]:
        if META.search(s): continue
        for w in re.findall(r"[A-Za-z]{%d,}" % ml, s):
            lw = w.lower()
            if lw in seen or lw in near or w.isupper(): continue
            seen.add(lw)
            if lw in allocr and False: continue
            # a typo candidate: the data word is rare in the whole project and the scan has a common word right next to it
            c = [v for v in near if len(v) >= ml - 1 and lev(lw, v) <= 2 and v != lw and freq.get(v, 0) >= 8] if freq.get(lw, 0) <= 2 else []
            if c: out.append((n, w, sorted(c, key=lambda v: lev(lw, v))[:2]))
print(len(out), 'pairs')
for n, w, c in out: print(n, w, '|', ' '.join(c))
