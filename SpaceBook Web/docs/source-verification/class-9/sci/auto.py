# -*- coding: utf-8 -*-
"""Draft page sources for Class 9 General Science from the verified audit modules + Word OCR page breaks.

    python -X utf8 sci/auto.py U        writes src/pNNN.src drafts for unit U (does not overwrite files marked '@keep')

Every audited item (SLO, section heading, paragraph, key point, MCQ, long/short question) is located in the
OCR text of the printed pages (footer numbers mark page ends); a paragraph that runs over a page end is split
at the matching word. Pages where an item could not be placed are reported for a visual check.
"""
import re, sys
from pathlib import Path
from expand import unit, sections

HERE = Path(__file__).resolve().parent
OCR = (HERE.parent / 'genscience' / 'word_text.txt').read_text(encoding='utf-8').splitlines()
JPG_OFFSET = 4          # printed page = JPG - 4 ; page file pNNN = JPG - 1 = printed + 3


def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())


def ocr_pages():
    pages, buf, last = {}, [], 0
    for line in OCR[105:]:
        m = re.fullmatch(r'\s*(\d{1,3})\s*', line)
        if m:
            v = int(m.group(1))
            if v == last + 1 or (last and v == last + 2):
                pages[v] = norm(' '.join(buf))
                if v == last + 2:
                    pages[last + 1] = pages[v]     # page footer lost in OCR: both pages share the block
                buf, last = [], v
                continue
        buf.append(line)
    return pages


PAGES = ocr_pages()


def locate(text, start, stop, first, with_pos=False):
    t = norm(text)
    offs = (0, 15, 40, 80, 120)
    keys = [(i, t[i:i + 30]) for i in offs if len(t[i:i + 30]) >= 20] or [(0, t)]
    for o, k in keys:
        for p in list(range(start, stop + 1)) + list(range(first, start)):
            if k and k in PAGES.get(p, ''):
                return (p, max(PAGES[p].find(k) - o, 0)) if with_pos else p
    return (None, None) if with_pos else None


def split_words(text, page):
    """Index i such that words[:i] end on `page` and words[i:] continue on page+1 (None if it fits)."""
    w = text.split()
    nxt = PAGES.get(page + 1, '')
    cur = PAGES.get(page, '')
    if norm(' '.join(w[-5:])) in cur:
        return None
    for i in range(len(w) - 1, 3, -1):
        if norm(' '.join(w[i - 4:i])) in cur and norm(' '.join(w[i:i + 4])) in nxt:
            return i
    return None


def items(n):
    U = unit(n)
    out = [('slo', f'use {n} slo {i}', s[0]) for i, s in enumerate(U.SLOS)]
    for rid, s in sections(n):
        out.append(('h', f'use {n} {rid} h', s[1][0]))
        for i, p in enumerate(s[2]):
            out.append(('p', f'use {n} {rid} {i}', p[0]))
    out += [('kp', f'use {n} kp {i}', k[0]) for i, k in enumerate(U.KEY_POINTS)]
    out += [('mcq', f'use {n} mcq {i}', m[0][0]) for i, m in enumerate(U.MCQS)]
    out += [('sq', f'use {n} sq {i}', q[0][0]) for i, q in enumerate(getattr(U, 'SQS', []))]
    out += [('lq', f'use {n} lq {i}', q[0][0]) for i, q in enumerate(U.LQS)]
    return out


def main(n):
    U = unit(n)
    printed = [g - JPG_OFFSET for g in U.SCANS]
    first, last = printed[0], printed[-1]
    pages = {p: [] for p in printed}      # p -> [(ocr position, ref)]
    lastpos = {}
    cur = first
    misses = []

    def put(p, pos, ref):
        if pos is None:
            pos = lastpos.get(p, -1) + 0.001
        lastpos[p] = pos
        pages.setdefault(p, []).append((pos, ref))

    for kind, ref, text in items(n):
        if kind == 'slo':                  # the unit opener page carries the learning outcomes
            put(first, -1 + len(pages[first]) * 0.001, ref)
            continue
        p, pos = locate(text, cur, last, first, with_pos=True)
        if p is None:
            misses.append((cur, ref, text[:50]))
            p = cur
        cur = p
        if kind == 'p':
            i = split_words(text, p)
            if i:
                put(p, pos, f'{ref} |wto:{i}')
                put(p + 1, -0.5, f'{ref} |wfrom:{i}')
                cur = p + 1
                continue
        put(p, pos, ref)
    from figs import FIGS
    for k, f in enumerate(FIGS):
        if first <= f[0] <= last:
            pos = PAGES.get(f[0], '').find(norm(f[5])[:25]) if f[5] else -1
            pages.setdefault(f[0], []).append((pos if pos >= 0 else 10 ** 9 + k, f'use fig {k}'))
    from figs import TABLES
    for k, tb in enumerate(TABLES):
        if first <= tb[0] <= last:
            pos = PAGES.get(tb[0], '').find(norm(tb[1]))
            pages.setdefault(tb[0], []).append((pos if pos >= 0 else 10 ** 9, f'use tbl {k}'))
    for p in pages:
        pages[p] = [r for _, r in sorted(pages[p], key=lambda x: x[0])]
    for p, refs in pages.items():
        f = HERE / 'src' / f'p{p + 3:03}.src'
        if f.exists() and '@keep' in f.read_text(encoding='utf-8'):
            continue
        head = [f'@printed {p}', '@status lesson']
        if p == first:
            head += [f'@unit {n} | {U.TITLE[0]} || {U.TITLE[1]} || {U.TITLE[2]}',
                     f'@sec {n}-intro | Unit {n}: {U.TITLE[0]} || یونٹ {n}: {U.TITLE[1]} || {n} څپرکی: {U.TITLE[2]}',
                     f'# Unit {n} — {U.TITLE[0]} || یونٹ {n} — {U.TITLE[1]} || {n} څپرکی — {U.TITLE[2]}',
                     'p After studying this unit the students will be able to: || اس یونٹ کے مطالعے کے بعد طلبہ اس قابل ہوں گے کہ: || د دې څپرکي له زده کړې وروسته به زده کوونکي وکولای شي چې:']
        f.write_text('\n'.join(head + refs) + '\n', encoding='utf-8')
    print(f'unit {n}: pages {first}-{last}; {sum(len(v) for v in pages.values())} refs; misses {len(misses)}')
    for m in misses:
        print('  MISS near p', m[0], m[1], '|', m[2])


if __name__ == '__main__':
    main(int(sys.argv[1]))
