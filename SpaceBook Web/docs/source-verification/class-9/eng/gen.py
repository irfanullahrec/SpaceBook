# -*- coding: utf-8 -*-
"""Class 9 English page-by-page book: writes pages/pNNN.txt (NNN = PDF page - 1, PDF 1..165).

Text comes from the verified dataset (js/english_data.js, audited page by page in class-9/english); every item is
placed on its printed page by searching the per-page OCR (english/ocr/page-NNN.json). Exercise items are shown
with SpaceBook solutions (the book prints none). fix/pNNN.txt replaces a generated page; front.txt holds the
front/back matter (=== pNNN batches).

    python -X utf8 eng/gen.py
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'english'))
import eng9_tools as E

LET = 'abcdefgh'
Q_FIELDS = ('question', 'sentence', 'original', 'prompt', 'direct', 'active', 'statement', 'line', 'lines', 'phrase', 'textPhrase',
            'word', 'pair', 'base', 'singular', 'poemWord', 'simile', 'figure', 'quote', 'urdu', 'task', 'stanza', 'couplet',
            'topic', 'title', 'type', 'device', 'category')
SKIP_FIELDS = {'num', 'answerOrigin', 'origin', 'sourceMeaning', 'cognitiveLevel', 'slo'}


def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def ocr_text(n):
    f = HERE.parent / 'english' / 'ocr' / f'page-{n:03}.json'
    if not f.exists():
        return ''
    L = json.loads(f.read_text(encoding='utf-8'))['lines']
    return norm(' '.join(l['text'] for l in sorted(L, key=lambda l: (l['y'] // 25, l['x']))))


PAGES = {n: ('' if n in E.DUPLICATES else ocr_text(n)) for n in range(1, 166)}


def clean(s):
    if isinstance(s, list):
        s = ', '.join(clean(x) for x in s)
    elif isinstance(s, dict):
        s = '; '.join(f'{k}: {clean(v)}' for k, v in s.items())
    return str(s if s is not None else '').replace('||', '{{OR}}').replace('##', '#').replace('\n', ' ').strip()


def humanize(k):
    k = re.sub(r'^exercise\d+_', '', k)
    k = re.sub(r'([a-z])([A-Z])', r'\1 \2', k).replace('_', ' ')
    return k[:1].upper() + k[1:]


def shingles(text):
    w = [norm(x) for x in (text or '').split()]
    w = [x for x in w if x]
    if len(w) < 4:
        j = ''.join(w)
        return [(len(w), j)] if len(j) >= 10 else []
    return [(i + 4, ''.join(w[i:i + 4])) for i in range(len(w) - 3)]


class Placer:
    """Collect items in book order, then assign pages by DP over OCR shingle scores (pages never go backwards)."""

    def __init__(self, first, last):
        self.first, self.last = first, last
        self.items = []          # dict(text, lines | para, fixed page)
        self.misses = []

    def put(self, p, pos, lines):          # fixed page
        self.items.append(dict(text=None, lines=lines, fixed=p, order=pos))

    def place(self, text, lines):
        self.items.append(dict(text=text, lines=lines))

    def para(self, en, ur, ps, prefix):
        self.items.append(dict(text=en, para=(en, ur, ps), lines=prefix))

    def solve(self):
        pages = list(range(self.first, self.last + 1))
        K = len(pages)
        rows = []
        for it in self.items:
            sc = [0.0] * K
            if it.get('fixed') is None and it['text']:
                sh = shingles(it['text'])
                if sh:
                    for k, p in enumerate(pages):
                        t = PAGES.get(p, '')
                        sc[k] = sum(1 for _, x in sh if x in t) / len(sh)
                if max(sc) == 0:
                    self.misses.append((None, it['text'][:50]))
            rows.append(sc)
        NEG = -1e9
        dp = [[NEG] * K for _ in rows]
        bk = [[0] * K for _ in rows]
        for i, it in enumerate(self.items):
            for k in range(K):
                if it.get('fixed') is not None and pages[k] != it['fixed']:
                    continue
                if i == 0:
                    best, arg = 0.0, k
                else:
                    best, arg = NEG, 0
                    for q in range(k + 1):
                        v = dp[i - 1][q] - 0.02 * (k - q)
                        if v > best:
                            best, arg = v, q
                if best > NEG / 2:
                    dp[i][k] = best + rows[i][k]
                    bk[i][k] = arg
        k = max(range(K), key=lambda x: dp[-1][x])
        assign = [0] * len(self.items)
        for i in range(len(self.items) - 1, -1, -1):
            assign[i] = pages[k]
            k = bk[i][k]
        out = {p: [] for p in pages}
        for i, it in enumerate(self.items):
            p = assign[i]
            if 'para' not in it:
                out[p].append(it['lines'])
                continue
            en, ur, ps = it['para']
            nxt = assign[i + 1] if i + 1 < len(self.items) else self.last
            cut = None
            if chr(10) not in en and nxt > p and p < self.last:
                cur_t, nxt_t = PAGES.get(p, ''), PAGES.get(p + 1, '')
                sh = shingles(en)
                hits_cur = [e for e, x in sh if x in cur_t]
                hits_nxt = [e for e, x in sh if x in nxt_t and x not in cur_t]
                if hits_cur and hits_nxt and max(hits_cur) < len(en.split()) - 1 and min(hits_nxt) > max(hits_cur) - 4:
                    cut = max(hits_cur)
            if cut:
                w = en.split()
                out[p].append(it['lines'] + para_lines(' '.join(w[:cut]), ur, ps))
                out[p + 1].insert(0, [f'p {clean(" ".join(w[cut:]))}' + (' || ↑ || ↑' if ur else '')])
            else:
                out[p].append(it['lines'] + para_lines(en, ur, ps))
        return out


def para_lines(en, ur='', ps=''):
    en_l = [x.strip() for x in en.split('\n') if x.strip()]
    ur_l = [x.strip() for x in (ur or '').split('\n') if x.strip()]
    ps_l = [x.strip() for x in (ps or '').split('\n') if x.strip()]
    if len(en_l) > 1:
        if ur and len(ur_l) == len(en_l) == len(ps_l):
            return [f'p {clean(a)} || {clean(b)} || {clean(c)}' for a, b, c in zip(en_l, ur_l, ps_l)]
        out = [f'p {clean(a)}' for a in en_l]
        if ur:
            out[-1] = f"p {clean(en_l[-1])} || {clean(' / '.join(ur_l))} || {clean(' / '.join(ps_l))}"
        return out
    return [f'p {clean(en)} || {clean(ur)} || {clean(ps)}' if ur else f'p {clean(en)}']


def item_lines(no, it):
    """One exercise item -> qp/sol lines (SpaceBook solution)."""
    if not isinstance(it, dict):
        return [f'qp {no} | {clean(it)}']
    qf = next((f for f in Q_FIELDS if it.get(f)), None)
    q = re.sub(r'^\s*(\d+|[a-z]|[ivx]+)[.)]\s+', '', clean(it[qf])) if qf else ''
    opts = it.get('options')
    if isinstance(opts, list) and opts:
        q += ' ' + ' '.join(f'({LET[i]}) {clean(o)}' for i, o in enumerate(opts))
        c = it.get('correct')
        if isinstance(c, int) and 0 <= c < len(opts):
            ans = f'({LET[c]}) {clean(opts[c])}'
        else:
            ans = clean(it.get('answer') or c)
        return [f'qp {no} | {q}', f"sol {ans} ## {clean(it.get('explanation', ''))}".rstrip(' #')]
    rest = [(k, v) for k, v in it.items() if k != qf and k not in SKIP_FIELDS and v not in ('', None, [])]
    if not rest:
        return [f'qp {no} | {q}']
    if len(rest) == 1:
        sol = clean(rest[0][1])
    else:
        sol = ' · '.join(f'{humanize(k)}: {clean(v)}' for k, v in rest)
    head = sol.split(' · ')[0][:60] if len(rest) == 1 else 'Solution'
    return [f'qp {no} | {q or "—"}', f'sol {clean(head)} ## {sol}']


def unit_pages(u):
    n = u['number']
    rv = u['sourceReview']
    first, last = rv['pdfPages'][0], rv['pdfPages'][-1]
    P = Placer(first, last)
    P.put(first, -3, [f"@unit {n} | {clean(u['title'])} || {clean(u.get('titleUrdu', ''))} || {clean(u.get('titlePashto', ''))}",
                      f"@sec {n}-intro | Unit {n}: {clean(u['title'])} || یونٹ {n}: {clean(u.get('titleUrdu', ''))} || {n} څپرکی: {clean(u.get('titlePashto', ''))}",
                      f"# Unit {n} — {clean(u['title'])} || یونٹ {n} — {clean(u.get('titleUrdu', ''))} || {n} څپرکی — {clean(u.get('titlePashto', ''))}"])
    if u.get('sourceSlos'):
        P.put(first, -2, ['p After reading the unit the students will be able to: || اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ: || د دې څپرکي له لوستلو وروسته به زده کوونکي وکولای شي چې:']
              + [f'slo {clean(s)}' for s in u['sourceSlos']])
    for i, pr in enumerate(u.get('preReading') or []):
        lines = (['## Pre-reading || مطالعے سے پہلے || له لوستلو مخکې'] if i == 0 else []) + [f"p {clean(pr.get('q'))}"]
        if pr.get('a') and not str(pr['a']).startswith('Pre-reading question'):
            lines.append(f"p {clean(pr['a'])}")
        P.place(pr.get('q'), lines)
    reading_head = False
    for k, s in enumerate(u['sections']):
        paras = s.get('paras') or ([s['text']] if s.get('text') else [])
        ur = [x for x in (s.get('urdu') or '').split('\n') if x.strip()]
        ps = [x for x in (s.get('pashto') or '').split('\n') if x.strip()]
        paired = len(ur) == len(paras) == len(ps)
        sec = f"@sec {n}-s{k + 1} | {clean(s.get('heading'))} || {clean(s.get('headingUrdu', ''))} || {clean(s.get('headingPashto', ''))}"
        for j, para in enumerate(paras):
            lines = []
            if j == 0:
                lines.append(sec)
                if not reading_head:
                    lines.append('## Reading || مطالعہ || لوستل')
                    reading_head = True
            u_, p_ = (ur[j], ps[j]) if paired else ('', '')
            P.para(para, u_, p_, lines)
        if not paired and (s.get('urdu') or s.get('pashto')):
            P.place(None, ['box note | Translation of this passage || اس حصے کا ترجمہ || د دې برخې ژباړه',
                                f"p (Urdu and Pashto translation of the passage above) || {clean(s.get('urdu'))} || {clean(s.get('pashto'))}", 'endbox'])
    gl = u.get('glossary') or u.get('exercise', {}).get('glossaryTable')
    if gl:
        lines = ['table Glossary || فرہنگ || وییپانګه', 'th | Word || لفظ || کلمه | Meaning || معنی || مانا']
        for g in gl:
            w = clean(g.get('word')) + (f" ({clean(g['pos'])})" if g.get('pos') else '')
            lines.append(f"tr | {w} | {clean(g.get('meaning'))} || {clean(g.get('urdu'))} || {clean(g.get('pashto'))}")
        lines.append('endtable')
        P.place(' '.join(f"{g.get('word', '')} {g.get('meaning', '')}" for g in gl[:4]), lines)
    # exercises in dataset order (= book order), each item on the page where it is printed
    ex = u.get('exercise') or {}
    ex_head = [f'@sec {n}-ex | Exercises || مشقیں || تمرینونه', '@tab doing', '# Exercises || مشقیں || تمرینونه']
    ex_start = next((p for p in range(first + 1, last + 1) if 'comprehension' in PAGES.get(p, '')), first)
    qno = [0]

    class Coll:
        def __init__(self):
            self.blocks = []

        def place(self, text, lines):
            self.blocks[-1].append((text, lines))

    C = Coll()

    def group(key, val):
        if key in ('glossaryTable', 'answerNote') or val in (None, '', [], {}):
            return
        if isinstance(val, str):
            if key == 'title':
                C.place(None, [f'### {clean(val)}'])
            return
        if isinstance(val, dict):
            if all(isinstance(v, str) for v in val.values()):
                lines = [f'box activity | {humanize(key)}']
                lines += [f'p {humanize(k2)}: {clean(v)}' if k2 not in ('title',) else f'p {clean(v)}' for k2, v in val.items()]
                C.place(next(iter(val.values())), lines + ['endbox'])
                return
            for k2, v2 in val.items():
                group(k2, v2)
            return
        if isinstance(val, list):
            first_it = val[0]
            if isinstance(first_it, dict) and {'topic', 'explanation'} <= set(first_it):
                for g in val:
                    lines = [f"box teach | {clean(g['topic'])}", f"p {clean(g['explanation'])}"]
                    lines += [f'- {clean(e)}' for e in (g.get('examples') or [])]
                    C.place(g['topic'] + ' ' + str(g['explanation']), lines + ['endbox'])
                return
            if isinstance(first_it, dict) and {'title', 'content'} <= set(first_it) and len(first_it) <= 3:
                for g in val:
                    lines = [f"### {clean(g['title'])}"] + [f'p {clean(x)}' for x in str(g['content']).split('\n') if x.strip()]
                    C.place(g['title'], lines)
                return
            if isinstance(first_it, dict) and 'items' in first_it and 'instruction' in first_it:
                for g in val:
                    qno[0] += 1
                    lines = [f"q {qno[0]} | {clean(g.get('title', ''))} {clean(g.get('instruction', ''))}".rstrip()]
                    for i, it in enumerate(g.get('items') or []):
                        lines += item_lines(i + 1, it)
                    C.place(g.get('instruction'), lines)
                return
            qno[0] += 1
            head = [f'q {qno[0]} | {humanize(key)}']
            for i, it in enumerate(val):
                qtext = ''
                if isinstance(it, dict):
                    qf = next((f for f in Q_FIELDS if it.get(f)), None)
                    qtext = clean(it[qf]) if qf else ''
                else:
                    qtext = clean(it)
                C.place(qtext if len(norm(qtext)) >= 8 else None, (head if i == 0 else []) + item_lines(i + 1, it))

    for key, val in ex.items():
        C.blocks.append([])
        group(key, val)

    def where(block):
        for text, _ in block:
            sh = shingles(text) if text else []
            if not sh:
                continue
            best = max(range(ex_start, last + 1), key=lambda p: sum(1 for _, x in sh if x in PAGES.get(p, '')))
            hits = [PAGES[best].find(x) for _, x in sh if x in PAGES.get(best, '')]
            if hits:
                return (best, min(hits))
        return None
    keyed, lastk = [], (ex_start, -1)
    for b in C.blocks:
        if b:
            k = where(b) or (lastk[0], lastk[1] + 0.5)
            keyed.append((k, b))
            lastk = k
    keyed.sort(key=lambda x: x[0])      # book order (the dataset groups exercises by type)
    qn = 0
    if keyed:
        t0, l0 = keyed[0][1][0]
        keyed[0][1][0] = (t0, ex_head + l0)
    else:
        P.place(None, ex_head)
    for _, b in keyed:
        for text, lines in b:
            fixed = []
            for l in lines:
                if l.startswith('q ') and ' | ' in l:
                    qn += 1
                    l = f'q {qn} | ' + l.split(' | ', 1)[1]
                fixed.append(l)
            P.place(text, fixed)
    qno[0] = qn
    # SpaceBook SLO practice (not textbook text) after the exercises
    sq = u.get('sloQuestions') or {}
    aids = ['@issue The SLO-based questions on this page are SpaceBook practice material, not textbook text.',
            f'@sec {n}-slo | SLO-based practice || SLO پر مبنی مشق || د SLO پر بنسټ تمرین', '## SLO-based practice (SpaceBook) || SLO پر مبنی مشق || د SLO پر بنسټ تمرین']
    for key, lab in (('mcqs', 'SLO-based MCQs'), ('shortQuestions', 'SLO-based short questions'), ('longQuestions', 'SLO-based long questions')):
        if sq.get(key):
            qno[0] += 1
            aids.append(f'q {qno[0]} | {lab}')
            for i, it in enumerate(sq[key]):
                aids += item_lines(i + 1, it)
    if len(aids) > 3:
        P.put(last, None, aids)
    pages = P.solve()
    out = {p: [l for ls in items for l in ls] for p, items in pages.items()}
    return out, P.misses


def main():
    data = E.load()
    out = {}
    for u in data:
        pages, misses = unit_pages(u)
        print(f"unit {u['number']}: pdf {min(pages)}-{max(pages)}; misses {len(misses)}")
        for m in misses[:12]:
            print('   MISS near', m[0], m[1])
        for pdf, lines in pages.items():
            pr = E.printed_of(pdf)
            head = ['@status duplicate', f'@issue PDF page {pdf} repeats printed page {pr}.'] if pdf in E.DUPLICATES else [f'@printed {pr}', '@status lesson']
            if pdf in E.DUPLICATES:
                out[pdf - 1] = head
                continue
            if pr in (136, 138):
                head.append('@issue Printed page 137 is missing from every copy of this book (PDF, JPG and Word); its text could not be recovered.')
            out[pdf - 1] = head + lines
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
    print('pages', len(out), 'missing files', [k for k in range(165) if k not in out])


if __name__ == '__main__':
    main()
