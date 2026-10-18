# -*- coding: utf-8 -*-
"""Compare each stored English paragraph of a unit with the OCR of its PDF pages.
Usage: python para_diff.py <unit> <pdfStart> <pdfEnd>
Reports, per paragraph, the best-matching OCR window and the word differences."""
import json, os, re, sys, difflib, subprocess
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
unit, a, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
js = os.path.join(HERE, '..', '..', '..', '..', 'js', 'english_data.js')
paras = json.loads(subprocess.check_output(['node', '-e', f"""
const fs=require('fs'),vm=require('vm');const c={{}};vm.createContext(c);
vm.runInContext(fs.readFileSync({json.dumps(js)},'utf8').replace(/const ENGLISH_DATA/,'var ENGLISH_DATA'),c);
const u=c.ENGLISH_DATA.find(x=>x.number==={unit});const out=[];
u.sections.forEach((s,i)=>(s.paras||[s.text]).forEach((p,j)=>out.push([i,j,p])));
process.stdout.write(JSON.stringify(out));"""]).decode('utf-8'))

def norm(t):
    t = re.sub(r'[؀-ۿﷰ-﷿ﹰ-﻿]+', ' ', t)
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.findall(r"[A-Za-z0-9']+", t.lower())

def letters(t):
    t = re.sub(r'[\u0600-\u06FF\uFDF0-\uFDFF\uFE70-\uFEFF]+', '', t)
    return re.sub(r'[^a-z0-9]', '', t.lower())

ocr = ''; pagepos = []
for n in range(a, b + 1):
    f = os.path.join(HERE, 'ocr', f'page-{n:03d}.json')
    if os.path.exists(f):
        for l in json.load(open(f, encoding='utf-8'))['lines']:
            t = letters(l['text']); pagepos.append((len(ocr), n)); ocr += t
def page_at(k):
    p = a
    for pos, n in pagepos:
        if pos <= k: p = n
    return p
def best_cover(sent):
    """fraction of sentence letters found via the 3 longest matching runs anywhere in OCR"""
    sm = difflib.SequenceMatcher(None, ocr, sent, autojunk=False)
    blocks = [b for b in sm.get_matching_blocks() if b.size >= 4]
    covered = sum(b.size for b in blocks)
    return covered / max(1, len(sent)), (page_at(blocks[0].a) if blocks else None)

def sentences(p):
    return [x for x in re.split(r'(?<=[.!?:;"”])\s+', p) if len(letters(x)) >= 12]

total = flagged = 0
for i, j, p in paras:
    for sent in sentences(p):
        sl = letters(sent); total += 1
        # local window search keeps the matcher fast
        m = difflib.SequenceMatcher(None, ocr, sl, autojunk=False).find_longest_match(0, len(ocr), 0, len(sl))
        lo = max(0, m.a - m.b - 40); hi = min(len(ocr), m.a + len(sl) - m.b + 40)
        sm = difflib.SequenceMatcher(None, ocr[lo:hi], sl, autojunk=False)
        cov = sum(b.size for b in sm.get_matching_blocks() if b.size >= 3) / len(sl)
        if cov < 0.93:
            flagged += 1
            # second chance: maybe the sentence is split across scrambled lines -> check halves
            h = len(sl) // 2
            c2 = []
            for part in (sl[:h], sl[h:]):
                mm = difflib.SequenceMatcher(None, ocr, part, autojunk=False).find_longest_match(0, len(ocr), 0, len(part))
                c2.append(mm.size / len(part))
            tag = '~ ' if min(c2) > 0.6 else '!!'
            print(f'{tag} [{i}.{j}] cov={cov:.2f} halves={c2[0]:.2f}/{c2[1]:.2f} pdf{page_at(lo)}: {sent[:150]}')
print(f'sentences {total}, flagged {flagged}')
