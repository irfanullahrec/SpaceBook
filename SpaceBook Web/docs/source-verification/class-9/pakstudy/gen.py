# -*- coding: utf-8 -*-
"""Class 9 Pakistan Studies page-by-page book: writes pages/pNNN.txt (NNN = scan g - 1, g = 1..114).

The Urdu text with English/Pashto translations was audited block by block earlier (js/pakstudy_data.js via
pakstudies/chNN.py). This tool places every block on its printed page using the Word OCR (page footers mark the
page ends); a paragraph that runs over a page end is split at the matching word.
Hand-made pages: fix/pNNN.txt replaces the generated page.  Front/back matter: front.txt (=== pNNN batches).

    python -X utf8 pak9/gen.py
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'pakstudies'))
import pak_tools as P

OCR = (HERE.parent / 'pakstudies' / 'word_text.txt').read_text(encoding='utf-8').splitlines()
L4 = ['الف', 'ب', 'ج', 'د']
TPS = {1: 'د پاکستان نظریاتي بنسټ', 2: 'د پاکستان جوړېدل', 3: 'د پاکستان ځمکه او چاپېریال', 4: 'د پاکستان تاریخ (لومړۍ برخه ۱۹۴۷–۱۹۷۱)'}
TR = str.maketrans({'ي': 'ی', 'ى': 'ی', 'ے': 'ی', 'ك': 'ک', 'ه': 'ہ', 'ۃ': 'ہ', 'ة': 'ہ', 'ھ': 'ہ', 'ۂ': 'ہ', 'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ؤ': 'و', 'ئ': 'ی',
                    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'})


def norm(s):
    s = re.sub(r'[ً-ٰٟٕٔ‌‍‎‏]', '', s).translate(TR)
    return re.sub(r'[^\w]|_', '', s.lower())


def ocr_pages():
    pages, buf, last = {}, [], 0
    for line in OCR[63:1187]:
        m = re.fullmatch(r'\s*(\d{1,3})\s*', line)
        if m:
            v = int(m.group(1))
            if v == last + 1 or (last and v == last + 2):
                pages[v] = norm(' '.join(buf))
                if v == last + 2:
                    pages[last + 1] = pages[v]
                buf, last = [], v
                continue
        buf.append(line)
    return pages


PAGES = ocr_pages()
G_OF = {}
for g in range(1, 115):
    p = P.printed_of(g)
    if p and g not in P.DUPLICATE:
        G_OF[p] = g


def locate(text, start, stop, first):
    t = norm(text)
    offs = (0, 20, 50, 90, 140, 200)
    keys = [(i, t[i:i + 28]) for i in offs if len(t[i:i + 28]) >= 18] or [(0, t)]
    for o, k in keys:
        for p in list(range(start, stop + 1)) + list(range(first, start)):
            if k and k in PAGES.get(p, ''):
                return p, max(PAGES[p].find(k) - o, 0)
    return None, None


def split_words(text, page):
    w = text.split()
    cur, nxt = PAGES.get(page, ''), PAGES.get(page + 1, '')
    if norm(' '.join(w[-4:])) in cur:
        return None
    for i in range(len(w) - 1, 3, -1):
        if norm(' '.join(w[i - 4:i])) in cur and norm(' '.join(w[i:i + 4])) in nxt:
            return i
    return None


MAP_SVG = ('<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Map in the textbook">'
           '<rect x="2" y="2" width="356" height="116" rx="10" fill="#f4f7fb" stroke="#9fb3c8" stroke-dasharray="6 4"/>'
           '<path d="M30 30 L70 22 L96 40 L110 70 L92 98 L60 96 L40 76 Z" fill="#cfe3c4" stroke="#6d8f5f"/>'
           '<path d="M52 40 C62 60 70 70 84 92" fill="none" stroke="#5b8bd0" stroke-width="2"/>'
           '<text x="140" y="56" font-size="15" font-family="sans-serif" fill="#34495e">Map · نقشہ</text>'
           '<text x="140" y="80" font-size="12" font-family="sans-serif" fill="#5d6d7e">Printed in the textbook</text>'
           '<text x="140" y="98" font-size="12" font-family="sans-serif" fill="#5d6d7e">(see the scan of page {page})</text></svg>')


def clean(s):
    return (s or '').replace('||', '{{OR}}').replace('\n', ' ').strip()


def tri(ur, en='', ps=''):
    return ' || '.join(clean(x) for x in (ur, en, ps)) if (en or ps) else clean(ur)


def block_lines(b, part=None):
    ur, en, ps = b['ur'], b.get('en', ''), b.get('ps', '')
    if part:
        mode, k = part
        w = ur.split()
        if mode == 'to':
            ur = ' '.join(w[:k])
        else:
            ur, en, ps = ' '.join(w[k:]), '↑', '↑'
    if ur.startswith('• '):
        return [f"### {tri(ur[2:], en.lstrip('• '), ps.lstrip('• '))}"]
    lines = [x for x in ur.split('\n') if x.strip()]
    if len(lines) > 1 and not part:
        el = [x for x in en.split('\n') if x.strip()]
        pl = [x for x in ps.split('\n') if x.strip()]
        if len(el) == len(lines) == len(pl):
            return [f'p {tri(a, b_, c)}' for a, b_, c in zip(lines, el, pl)]
    return [f'p {tri(ur, en, ps)}']


def unit_pages(u):
    n = u['number']
    rv = u['sourceReview']
    first, last = rv['printedPages'][0], rv['printedPages'][-1]
    pages = {p: [] for p in range(first, last + 1)}
    lastpos, misses = {}, []

    def put(p, pos, lines):
        if pos is None:
            pos = lastpos.get(p, -1) + 0.001
        lastpos[p] = pos
        pages.setdefault(p, []).append((pos, lines))

    put(first, -3, [f"@unit {n} | {u['title']} || {u['titleEn']} || {TPS[n]}",
                    f"@sec {n}-intro | باب {n}: {u['title']} || Chapter {n}: {u['titleEn']} || {n} څپرکی: {TPS[n]}",
                    f"# باب {n} — {u['title']} || Chapter {n} — {u['titleEn']} || {n} څپرکی — {TPS[n]}"])
    # introQuranHadith is the panel inside the front cover (front.txt p001), not part of chapter 1
    cur = first
    for s in u['sections']:
        head = [f"@sec {n}-{s['id']} | {s['id']} {s['title']} || {s['id']} {s.get('titleEn', '')} || {s['id']} {s.get('titlePs', '')}",
                f"## {s['id']} {s['title']} || {s['id']} {s.get('titleEn', '')} || {s['id']} {s.get('titlePs', '')}"]
        p, pos = locate(s['title'], cur, last, first)
        if p is None or p < cur:
            p, pos = cur, None
        put(p, pos, head)
        cur = p
        for b in s['blocks']:
            if b['ur'].lstrip('• ').strip() == s['title'].strip():
                continue                     # repeated printed heading
            fixed = re.match(r'^\(?(?:نقشہ \(صفحہ|کتاب کا صفحہ) (\d+)', b['ur'])
            if fixed:                        # map / page note that names its printed page
                pg = int(fixed.group(1))
                if b['ur'].startswith('نقشہ'):
                    put(pg, 10 ** 7, [f"svg {tri(b['ur'], b.get('en', ''), b.get('ps', ''))}", MAP_SVG.format(page=pg), 'endsvg'])
                else:
                    put(pg, -1, ['box note | SpaceBook نوٹ || SpaceBook note || د SpaceBook یادونه', f"p {tri(b['ur'], b.get('en', ''), b.get('ps', ''))}", 'endbox'])
                continue
            p, pos = locate(b['ur'].lstrip('• '), cur, last, first)
            if p is None:
                misses.append((cur, b['ur'][:40]))
                p = cur
            cur = p
            k = split_words(b['ur'], p) if not b['ur'].startswith('• ') else None
            if k and p + 1 <= last:
                put(p, pos, block_lines(b, ('to', k)))
                put(p + 1, -0.5, block_lines(b, ('from', k)))
                cur = p + 1
            else:
                put(p, pos, block_lines(b))
    # exercise (the book prints the questions at the end of the chapter; answers are SpaceBook's)
    ex = u['exercise']
    ex_lines = [f'@sec {n}-ex | مشق || Exercise || تمرین', '@tab doing', '# مشق || Exercise || تمرین',
                'q 1 | درست جواب کا انتخاب کریں۔ || Choose the correct answer. || سم ځواب وټاکئ.']
    for i, m in enumerate(ex['mcqs']):
        o = ' '.join(f'({L4[k]}) {clean(x)}' for k, x in enumerate(m['options']))
        ex_lines.append(f"qp {i + 1} | {clean(m['question'])} {o}")
        ex_lines.append(f"sol ({L4[m['correct']]}) {clean(m['options'][m['correct']])} ## {clean(m.get('explanation', ''))}")
    ex_lines.append('q 2 | مختصر جوابات دیں۔ || Give short answers. || لنډ ځوابونه ورکړئ.')
    for i, q in enumerate(ex['shortQuestions']):
        ex_lines += [f"qp {i + 1} | {clean(q['question'])}", f"sol جواب ## {clean(q['answer'])}"]
    ex_lines.append('q 3 | تفصیلی جوابات دیں۔ || Give detailed answers. || مفصل ځوابونه ورکړئ.')
    for i, q in enumerate(ex['longQuestions']):
        ex_lines += [f"qp {i + 1} | {clean(q['question'])}", f"sol جواب ## {clean(q['answer'])}"]
    if ex.get('activities'):
        ex_lines.append('box activity | سرگرمیاں || Activities || فعالیتونه')
        ex_lines += [f'- {clean(a)}' for a in ex['activities']]
        ex_lines.append('endbox')
    p, pos = locate(ex['mcqs'][0]['question'], first, last, first)
    if p is None or p < cur:
        p, pos = last - 1 if last - 1 >= cur else last, None
    put(p, pos if pos is not None else 10 ** 8, ex_lines)
    # SpaceBook study aids (not textbook text) after the exercise
    aids = [f'@sec {n}-aids | اہم نکات اور مشقی سوالات || Key points and SLO practice || مهم ټکي او تمریني پوښتنې', '## اہم نکات || Key Points || مهم ټکي']
    aids += [f'- {clean(k)}' for k in u.get('keyPoints', [])]
    if u.get('timeline'):
        aids += ['table اہم تاریخیں || Timeline || مهمې نېټې', 'th | سال || Year || کال | واقعہ || Event || پېښه']
        aids += [f"tr | {clean(t['year'])} | {clean(t['event'])}" for t in u['timeline']]
        aids.append('endtable')
    sb = u.get('sloBank') or {}
    if sb.get('mcqs'):
        aids += ['q 4 | SLO پر مبنی کثیر الانتخابی سوالات (SpaceBook) || SLO based MCQs (SpaceBook) || د SLO پر بنسټ څو ځوابه پوښتنې (SpaceBook)']
        for i, m in enumerate(sb['mcqs']):
            if 'correct' not in m:
                m = dict(m, correct=m['options'].index(m['answer']))
            o = ' '.join(f'({L4[k]}) {clean(x)}' for k, x in enumerate(m['options']))
            aids += [f"qp {i + 1} | {clean(m['question'])} {o}", f"sol ({L4[m['correct']]}) {clean(m['options'][m['correct']])} ## {clean(m.get('explanation', ''))}"]
    for key, no, lab in (('shortQuestions', 5, 'SLO پر مبنی مختصر سوالات (SpaceBook) || SLO based short questions (SpaceBook) || د SLO پر بنسټ لنډې پوښتنې (SpaceBook)'),
                         ('longQuestions', 6, 'SLO پر مبنی تفصیلی سوالات (SpaceBook) || SLO based long questions (SpaceBook) || د SLO پر بنسټ اوږدې پوښتنې (SpaceBook)')):
        if sb.get(key):
            aids.append(f'q {no} | {lab}')
            for i, q in enumerate(sb[key]):
                aids += [f"qp {i + 1} | {clean(q['question'])}", f"sol جواب ## {clean(q['answer'])}"]
    put(last, 10 ** 9, ['@issue Key points, timeline and SLO questions on this page are SpaceBook study aids, not textbook text.'] + aids)
    for p in pages:
        pages[p] = [l for _, ls in sorted(pages[p], key=lambda x: x[0]) for l in ls]
    return pages, misses


def main():
    data = P.load()
    out = {}
    for u in data:
        pages, misses = unit_pages(u)
        print(f"chapter {u['number']}: printed {min(pages)}-{max(pages)}; misses {len(misses)}")
        for m in misses:
            print('   MISS near', m[0], m[1])
        for pr, lines in pages.items():
            if pr not in G_OF:
                continue
            head = [f'@printed {pr}', '@status lesson']
            if pr + 1 in P.MISSING_PRINTED or pr - 1 in P.MISSING_PRINTED:
                head.append('@issue Printed page 52 is missing from every scan of this book; its text could not be recovered.')
            out[G_OF[pr] - 1] = head + lines
    for g, src in P.DUPLICATE.items():
        out[g - 1] = ['@status duplicate', f'@issue Scan {g} repeats scan {src} (printed page {P.printed_of(src)}).']
    front = (HERE / 'front.txt').read_text(encoding='utf-8')
    for blk in front.split('=== p')[1:]:
        no, _, body = blk.partition('\n')
        out[int(no)] = body.rstrip('\n').split('\n')
    pdir = HERE / 'pages'
    pdir.mkdir(exist_ok=True)
    for f in pdir.glob('p*.txt'):
        f.unlink()
    for k, lines in sorted(out.items()):
        fx = HERE / 'fix' / f'p{k:03}.txt'
        txt = fx.read_text(encoding='utf-8') if fx.exists() else '\n'.join(lines) + '\n'
        (pdir / f'p{k:03}.txt').write_text(txt, encoding='utf-8')
    missing = [k for k in range(114) if k not in out]
    print('pages', len(out), 'missing files', missing)


if __name__ == '__main__':
    main()
