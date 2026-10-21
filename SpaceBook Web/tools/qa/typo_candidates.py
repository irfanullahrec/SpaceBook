"""Typo candidates of an English book: words of the data that are rare in the whole project (frequency <= 2 in js/word_stats_words.js) and
do not occur in the OCR of any page of the scan folder.

    python tools/qa/typo_candidates.py <page_text.json> <ocr dir> [--max N]

Prints "page word" lines; each one is then opened next to its scan. Words with digits, capitals-only, or shorter than 5 letters are skipped."""
import sys, os, re, json
pt, od = sys.argv[1], sys.argv[2]
mx = int(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else 400
raw = open('js/word_stats_words.js', encoding='utf8').read()
j = json.loads(raw[raw.index('{'):raw.rindex('}') + 1])
D = j['SB_WORD_STATS_WORDS'] if 'SB_WORD_STATS_WORDS' in j else j
W = D['words']['en'].split('\n'); F = [int(x, 36) for x in D['freq']['en'].split(',')]
freq = dict(zip(W, F))
ocr = ' '.join(open(os.path.join(od, f), encoding='utf8').read().lower() for f in os.listdir(od) if f.endswith('.txt'))
ocrl = re.sub(r'[^a-z]', '', ocr)
pages = json.load(open(pt, encoding='utf8'))
out = []
for pg in sorted(pages, key=int):
    seen = set()
    for s in pages[pg]:
        for w in re.findall(r"[A-Za-z]{5,}", s):
            lw = w.lower()
            if lw in seen: continue
            seen.add(lw)
            if freq.get(lw, 0) <= 2 and lw not in ocrl:
                out.append((pg, w, freq.get(lw, 0)))
print(len(out), 'candidates')
for pg, w, f in out[:mx]: print(pg, w, f)
