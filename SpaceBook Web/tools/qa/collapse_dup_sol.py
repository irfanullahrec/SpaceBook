"""Collapse `sol ANSWER ## X || X || X` (the same text in all three language slots) to `sol ANSWER ## X`.

    python -X utf8 tools/qa/collapse_dup_sol.py

A step that repeats one language three times shows an English (or Urdu) sentence under the Urdu and Pashto labels;
a single part is shown once, in the book's first language, and the sentence-click translation lines supply the rest.
"""
import collections, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'docs' / 'source-verification'
tot = collections.Counter()
for cls in ('class-9', 'class-10'):
    for f in sorted((ROOT / cls).glob('*/pages/p[0-9][0-9][0-9].txt')):
        raw = f.read_bytes()
        crlf = b'\r\n' in raw
        L = raw.decode('utf-8').replace('\r\n', '\n').split('\n')
        ch = 0
        for i, l in enumerate(L):
            if l.startswith('sol ') and ' ## ' in l:
                a, _, w = l[4:].partition(' ## ')
                parts = [x.strip() for x in w.split(' || ')]
                if len(parts) == 3 and parts[0] == parts[1] == parts[2] and parts[0]:
                    L[i] = 'sol ' + a + ' ## ' + parts[0]
                    ch += 1
        if ch:
            tot[cls + '/' + f.parent.parent.name] += ch
            data = ('\r\n' if crlf else '\n').join(L).encode('utf-8')
            for attempt in range(10):   # Windows sometimes refuses a write for a moment (EINVAL)
                try:
                    f.write_bytes(data)
                    break
                except OSError:
                    time.sleep(1.0)
            else:
                raise
print(dict(tot), sum(tot.values()))
