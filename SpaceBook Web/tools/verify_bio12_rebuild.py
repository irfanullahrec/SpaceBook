# -*- coding: utf-8 -*-
"""Compare rebuilt sections against the previous dataset to detect lost content."""
import json, io, re, sys, random
sys.stdout.reconfigure(encoding='utf-8')

OLD = r"D:\SpaceBook\SpaceBook Web\js\biology_12_data.js.bak"
NEW = r"D:\SpaceBook\SpaceBook Web\js\biology_12_data.js"


def load(path):
    src = io.open(path, encoding='utf-8').read()
    return json.loads(src[src.index('['):src.rindex(']') + 1])


def words(s):
    return re.findall(r"[a-z]{4,}", s.lower())


old, new = load(OLD), load(NEW)
print(f'chapters old={len(old)} new={len(new)}')

lost_samples = []
old_words = new_words = 0
def chapter_paras(ch):
    return [p for s in ch['sections'] for p in s['paras']] + \
           [s['heading'] for s in ch['sections']]


all_new = ' '.join(p for ch in new for p in chapter_paras(ch))
all_vocab = set(words(all_new))
old_words = new_words = 0
for oc, nc in zip(old, new):
    old_words += sum(len(p.split()) for p in chapter_paras(oc))
    new_words += sum(len(p.split()) for p in chapter_paras(nc))
    nc_vocab = set(words(' '.join(chapter_paras(nc))))
    for s in oc['sections']:
        for p in s['paras']:
            if len(p) < 100 or re.search(r'(?i)fig:|table:|awaz|mdcat', p):
                continue
            pw = words(p)
            if len(pw) < 12:
                continue
            present = sum(1 for w in pw if w in all_vocab)
            if present / len(pw) < 0.7:
                lost_samples.append((oc['number'], round(present / len(pw), 2), p))

print(f'words: old={old_words} new={new_words} (removed {old_words - new_words})')
print(f'old paragraphs with <70% words surviving ANYWHERE in new data: {len(lost_samples)}')
random.seed(7)
for n, frac, p in random.sample(lost_samples, min(25, len(lost_samples))):
    print(f'  ch{n} [{frac}]: {p[:150]!r}')
