# -*- coding: utf-8 -*-
import json, re, sys, difflib
sys.stdout.reconfigure(encoding='utf-8')
import urdu9_tools as T
from urdu_diff import norm, SRC
D = T.load()
for u in D:
    raw = u['exercise'].get('rawExercise', '')
    bad = []
    for line in raw.split('\n'):
        n = norm(re.sub(r'\(.*?\)$', '', line))
        if len(n) < 12: continue
        m = difflib.SequenceMatcher(None, SRC, n, autojunk=False).find_longest_match(0, len(SRC), 0, len(n))
        lo = max(0, m.a - m.b - 30); hi = min(len(SRC), m.a + len(n) - m.b + 30)
        cov = sum(b.size for b in difflib.SequenceMatcher(None, SRC[lo:hi], n, autojunk=False).get_matching_blocks() if b.size >= 3) / len(n)
        if cov < 0.8: bad.append((round(cov, 2), line[:110]))
    print(f"lesson {u['number']}: flagged {len(bad)}")
    for b in bad[:12]: print('   ', b)
