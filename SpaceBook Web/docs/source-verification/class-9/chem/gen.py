# -*- coding: utf-8 -*-
"""Class 9 Chemistry page-by-page book: writes pages/pNNN.txt (NNN = index into pagemap.PAGES).

Text, translations, tables and diagrams come from the verified dataset (js/data_chem.js, dumped by chem/dump.js to
chem/data.json); every paragraph carries the page it is printed on (sourcePrintedPage / sourcePdfPage, or the page of
its sourceTranslationPairs twin), and each subtopic's sourceLayout lists the printed order of its blocks. A block goes
on the page of its first paragraph. fix/pNNN.txt replaces a generated page; front.txt holds the front/back matter.

    python -X utf8 chem/gen.py            writes pages/pNNN.txt
    python -X utf8 chem/gen.py report     prints placement problems only
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pagemap

C = json.loads((HERE / 'data.json').read_text(encoding='utf-8'))
PAGES = pagemap.PAGES
BY_PRINTED = {p[2]: i for i, p in enumerate(PAGES) if p[2] is not None}
BY_PDF = {(p[0], p[1]): i for i, p in enumerate(PAGES)}
# every scan that was not chosen still points at its printed page (the second scans of the same page)
import glob, os
for f in glob.glob(str(HERE.parent / 'chemistry*-page-*.json')):
    d = json.load(open(f, encoding='utf-8'))
    pr, pdf = d.get('printedPage'), os.path.basename(d.get('sourcePdf', ''))
    if pr in BY_PRINTED and (pdf, d['pdfPage']) not in BY_PDF:
        BY_PDF[(pdf, d['pdfPage'])] = BY_PRINTED[pr]
PDF_OF_UNIT = {1: ['chemistry pdf1.pdf'], 2: ['chemistry pdf1.pdf', 'chemistry2.pdf'], 3: ['chemistry2.pdf'],
               4: ['chemistry2.pdf', 'chemistry3.pdf'], 5: ['chemistry3.pdf'], 6: ['chemistry4(1).pdf'],
               7: ['chemistry4(1).pdf', 'chemistry5.pdf'], 8: ['chemistry5.pdf']}
PROBLEMS = []
TOPIC_FIRST = {}


def clean(s):
    return re.sub(r'\s+', ' ', str(s if s is not None else '').replace('||', '{{OR}}').replace('\n', ' ')).strip()


def cell(s):
    return clean(s).replace('|', '{{BAR}}')


def tri(en, ur=None, ps=None):
    en = clean(en)
    if ur and ps:
        return f'{en} || {clean(ur)} || {clean(ps)}'
    return en


def para_tri(p):
    return tri(p.get('text'), p.get('urdu'), p.get('pashto'))


def heading_op(text):
    t = clean(text)
    if re.match(r'^\d+\.\d+\.\d+', t):
        return '##'
    if re.match(r'^\d+\.\d+(\s|$)', t):
        return '#'
    return '###'


class Tracker:
    """Resolves (pdf, page) numbers of a unit that are only given as page numbers inside the unit's source PDFs."""

    def __init__(self, unit):
        self.pdfs = PDF_OF_UNIT[unit]
        self.k = 0
        self.last = None

    def idx(self, page):
        if self.last is not None and page < self.last - 12 and self.k + 1 < len(self.pdfs):
            self.k += 1
        self.last = page
        return BY_PDF.get((self.pdfs[self.k], page))


def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def load_texts():
    """normalised text per page index: Tesseract caches (class-9/chemistry*.ocr.json) and the Word dumps (chem/docxpages.py)"""
    import docxpages
    T = {}
    for f in glob.glob(str(HERE.parent / 'chemistry*.ocr.json')):
        for pg in json.load(open(f, encoding='utf-8')).get('pages', []):
            idx = BY_PDF.get((os.path.basename(pg.get('sourcePdf', '')), pg.get('pdfPage')))
            if idx is not None:
                T[idx] = T.get(idx, '') + norm(pg.get('text'))
    for f in docxpages.FILES:
        for printed, text in docxpages.split(f).items():
            if printed in BY_PRINTED:
                T[BY_PRINTED[printed]] = T.get(BY_PRINTED[printed], '') + norm(text)
    return T


TEXT = load_texts()


def find_page(text, lo, hi):
    """first page in lo..hi whose text holds a 4-word shingle of `text` (the best-scoring page if several)"""
    w = [norm(x) for x in clean(text).split()]
    w = [x for x in w if x]
    if len(w) < 4:
        return None
    best, score = None, 0
    for pg in range(max(0, lo), min(len(PAGES) - 1, hi) + 1):
        t = TEXT.get(pg)
        if not t:
            continue
        sc = sum(1 for i in range(len(w) - 3) if ''.join(w[i:i + 4]) in t)
        if sc > score:
            best, score = pg, sc
    return best


def pages_of_sub(unit, sec, start=None):
    """page index per paragraph of a subtopic (None where unknown)."""
    paras = sec.get('paras') or []
    twin = {}
    tr = Tracker(unit)
    for pr in sec.get('sourceTranslationPairs') or []:
        pg = pr.get('sourcePdfPage')
        twin.setdefault(norm(pr.get('text'))[:60], tr.idx(pg) if pg else None)
    out = []
    for p in paras:
        idx = None
        if p.get('sourcePrintedPage') in BY_PRINTED:
            idx = BY_PRINTED[p['sourcePrintedPage']]
        elif p.get('sourcePdf') and p.get('sourcePdfPage'):
            idx = BY_PDF.get((os.path.basename(p['sourcePdf']), p['sourcePdfPage']))
        if idx is None:
            idx = twin.get(norm(p.get('text'))[:60])
        out.append(idx)
    # still unknown: find the page that holds the paragraph's words, searching forward from the last known page
    cur = start if start is not None else next((x for x in out if x is not None), 0)
    for i, p in enumerate(paras):
        if out[i] is not None:
            cur = out[i]
            continue
        hit = find_page(p.get('text'), cur, cur + 4)
        if hit is not None:
            out[i] = hit
            cur = hit
    return out


def svg_lines(item, ratio=None):
    svg = (item or {}).get('svg') or ''
    ratio = ratio or (item or {}).get('sourceWidthRatio')
    if ratio and '<svg' in svg and ' width=' not in svg.split('>', 1)[0]:
        svg = svg.replace('<svg', f'<svg width="{max(60, round(520 * ratio))}"', 1)
    return [l for l in svg.replace('\r', '').split('\n') if l.strip()]


def table_lines(tb):
    """DSL rows of a source table, cell = EN || UR || PS when translations exist."""
    heads = tb.get('headers') or []
    rows = tb.get('rows') or []
    ur = ps = None
    for t in tb.get('translations') or []:
        if t.get('language') in ('اردو', 'urdu'):
            ur = t
        elif t.get('language') in ('پښتو', 'pashto'):
            ps = t
    it = tb.get('interactiveTranslations') or {}

    def pick(kind, section, r, c, base):
        if kind is not None:
            if section == 'h':
                src = (kind.get('subHeaders') or kind.get('headers') or [])
                return src[c] if c < len(src) else None
            if r < len(kind.get('rows') or []) and c < len(kind['rows'][r]):
                v = kind['rows'][r][c]
                return v if isinstance(v, str) else None
        return None

    def trip(section, r, c, base):
        if not isinstance(base, str):
            return cell(base)
        u = pick(ur, section, r, c, base)
        p = pick(ps, section, r, c, base)
        if (u is None or p is None) and it:
            row = (it.get('headers') if section == 'h' else (it.get('rows') or [[]] * (r + 1))[r] if r < len(it.get('rows') or []) else [])
            x = row[c] if row and c < len(row) else None
            if isinstance(x, dict):
                u, p = x.get('urdu'), x.get('pashto')
        if u and p and base.strip() and clean(u) != clean(base):
            return f'{cell(base)} || {cell(u)} || {cell(p)}'
        return cell(base)
    out = []
    if heads and not tb.get('noHeader'):
        out.append('th | ' + ' | '.join(trip('h', 0, c, h) for c, h in enumerate(heads)))
    for r, row in enumerate(rows):
        out.append('tr | ' + ' | '.join(trip('r', r, c, v) for c, v in enumerate(row)))
    return out


class Page:
    def __init__(self, idx):
        self.idx = idx
        self.lines = []
        self.pre = []        # unit / section directives that open the page

    def add(self, *ls):
        self.lines.extend(ls)


PG = [Page(i) for i in range(len(PAGES))]


def emit_sub(unit, topic, sec, last_page):
    """Emit one subtopic; returns the page index of its last block."""
    paras = sec.get('paras') or []
    pgs = pages_of_sub(unit, sec, last_page)
    layout = sec.get('sourceLayout')
    blocks_by_id = {b.get('id'): b for b in (sec.get('sourceBlocks') or []) if isinstance(b, dict)}
    cur = last_page
    if not layout:
        layout = [{'type': 'paragraph', 'indices': [i]} for i in range(len(paras))]
    blk_pg = []
    for blk in layout:
        ids = blk.get('indices') or []
        if blk.get('columns'):
            ids = [i for col in blk['columns'] for i in col]
        pg = next((pgs[i] for i in ids if i < len(pgs) and pgs[i] is not None), None)
        vis = blocks_by_id.get(blk.get('blockId') or blk.get('tableId'))
        if pg is None and vis:
            pp = vis.get('sourcePrintedPage')
            if pp in BY_PRINTED:
                pg = BY_PRINTED[pp]
            elif vis.get('sourcePdfPage'):
                pg = Tracker(unit).idx(vis['sourcePdfPage'])
        blk_pg.append(pg)
    # an unplaced heading sits with the block after it; any other unplaced block follows the block before it
    for k in range(len(layout)):
        if blk_pg[k] is None:
            if layout[k]['type'] == 'heading':
                blk_pg[k] = next((x for x in blk_pg[k + 1:] if x is not None), None)
            if blk_pg[k] is None:
                blk_pg[k] = next((x for x in reversed(blk_pg[:k]) if x is not None), None)
            if blk_pg[k] is None:
                blk_pg[k] = next((x for x in blk_pg[k + 1:] if x is not None), cur)
            PROBLEMS.append(f'unit {unit} {sec.get("num")} block {k} {layout[k]["type"]} placed by neighbours on page index {blk_pg[k]}')
    for k, blk in enumerate(layout):
        ids = blk.get('indices') or []
        if blk.get('columns'):
            ids = [i for col in blk['columns'] for i in col]
        vis = blocks_by_id.get(blk.get('blockId') or blk.get('tableId'))
        pg = blk_pg[k]
        if pg is None:
            continue
        cur = pg
        out = PG[pg]
        T = blk['type']
        P = lambda i: paras[i] if i < len(paras) else {}
        if k == 0 and TOPIC_FIRST.get(id(topic)) is None and topic.get('num') and topic.get('title'):
            TOPIC_FIRST[id(topic)] = True
            if not any(clean(paras[i].get('text')).startswith(str(topic['num'])) for b in layout[:3] for i in (b.get('indices') or [])[:1] if i < len(paras)):
                out.add(f'# {clean(topic["num"])} {clean(topic["title"])}')
        if T == 'heading':
            for i in ids:
                out.add(f'{heading_op(P(i).get("text"))} {para_tri(P(i))}')
        elif T in ('paragraph', 'visualParagraph', 'equation', 'parallelPhrases'):
            if T == 'visualParagraph' and vis:
                out.add(f'svg {tri((vis.get("name") or ""))}' if False else 'svg', *svg_lines(vis), 'endsvg')
            for i in ids:
                out.add(('m ' + clean(P(i).get('text'))) if T == 'equation' else f'p {para_tri(P(i))}')
        elif T in ('list', 'numberedList'):
            for i in ids:
                # a list that runs over a page break continues on the next page
                ipg = pgs[i] if i < len(pgs) and pgs[i] is not None else pg
                PG[max(ipg, pg)].add(f'- {para_tri(P(i))}')
                cur = max(cur, ipg)
        elif T == 'visual':
            if vis:
                out.add('svg', *svg_lines(vis), 'endsvg')
            else:
                PROBLEMS.append(f'unit {unit} {sec.get("num")} visual {blk.get("blockId")} not found')
        elif T == 'sourceDataTable':
            if vis:
                out.add(f'table {tri(vis.get("title"), vis.get("titleUrdu"), vis.get("titlePashto"))}' if vis.get('title') else 'table', *table_lines(vis), 'endtable')
            else:
                PROBLEMS.append(f'unit {unit} {sec.get("num")} table {blk.get("tableId")} not found')
        else:
            for i in ids:
                out.add(f'p {para_tri(P(i))}')
            PROBLEMS.append(f'unit {unit} {sec.get("num")} unknown layout type {T}')
    # figures and tables the layout never mentions are placed on the page they are printed on
    used = {b.get('blockId') or b.get('tableId') for b in layout}
    for b in sec.get('sourceBlocks') or []:
        bid = b.get('id')
        if not bid or bid in used:
            continue
        pp = b.get('sourcePrintedPage')
        if pp not in BY_PRINTED:
            continue
        if b.get('svg'):
            PG[BY_PRINTED[pp]].add('svg', *svg_lines(b), 'endsvg')
            PROBLEMS.append(f'unit {unit} {sec.get("num")} figure {bid} not in the layout: placed at the end of printed page {pp}')
        elif b.get('rows'):
            PG[BY_PRINTED[pp]].add(f'table {tri(b.get("title"), b.get("titleUrdu"), b.get("titlePashto"))}' if b.get('title') else 'table', *table_lines(b), 'endtable')
            PROBLEMS.append(f'unit {unit} {sec.get("num")} table {bid} not in the layout: placed at the end of printed page {pp}')
    return cur



BOX_RE = re.compile(r'^(Activity\s*:?\s*[\d.]*|Society, Technology and Science|Scientific Information|Do You Know\??|Test Yourself[^—]*|Key Points?|Tidbit|Fun Fact|Remember|Think\s*(?:and|&)\s*Discuss|Note)\s*(?:—|-)\s+(.+)$', re.I)
BOX_HEADS = re.compile(r'^(Activity\s*:?\s*[\d.]*|Society, Technology and Science|Scientific Information|Do You Know\??|Test Yourself|Key Points?|Tidbit|Fun Fact|Remember|Note)$', re.I)


def box_kind(title):
    t = title.lower()
    return 'check' if t.startswith(('activity', 'test yourself', 'think')) else 'note' if t.startswith(('note', 'remember')) else 'info'


def boxify(lines):
    """Callouts printed in a frame become box ... endbox; a paragraph that repeats the caption of the table after it is dropped."""
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        en = l.split(' || ')[0]
        m = BOX_RE.match(en[2:]) if l.startswith('p ') else None
        if m:
            title, rest = m.group(1).strip(), m.group(2)
            parts = l[2:].split(' || ')
            tr = [x for x in parts]
            ur = parts[1].split('—')[-1].strip() if len(parts) == 3 and '—' in parts[1] else None
            ps = parts[2].split('—')[-1].strip() if len(parts) == 3 and '—' in parts[2] else None
            body = f'p {rest} || {ur} || {ps}' if ur and ps else f'p {rest}'
            ttl = title
            if len(parts) == 3 and '—' in parts[1] and '—' in parts[2]:
                ttl = f'{title} || {parts[1].split("—")[0].strip()} || {parts[2].split("—")[0].strip()}'
            out += [f'box {box_kind(title)} | {ttl}', body, 'endbox']
            i += 1
            continue
        if l.startswith('### ') and BOX_HEADS.match(en[4:].strip().rstrip(':')):
            title = l[4:]
            j = i + 1
            body = []
            while j < len(lines) and (lines[j].startswith(('p ', '- ', 'table', 'th |', 'tr |', 'endtable', 'svg', '<svg', 'endsvg'))):
                body.append(lines[j])
                j += 1
            if body:
                out += [f'box {box_kind(en[4:])} | {title}'] + body + ['endbox']
                i = j
                continue
        if l.startswith('p ') and i + 1 < len(lines) and lines[i + 1].startswith('table ') and lines[i + 1][6:].split(' || ')[0].strip() == en[2:].strip():
            i += 1
            continue
        out.append(l)
        i += 1
    return out


ROMAN = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv']
HEAD = {'mcqs': ('Choose the correct option.', 'درست آپشن منتخب کریں۔', 'سم انتخاب وټاکئ.'),
        'sq': ('SHORT QUESTIONS. Answer briefly the following questions.', 'مختصر سوالات۔ درج ذیل سوالات کے مختصر جوابات دیں۔', 'لنډې پوښتنې. لاندې پوښتنو ته لنډ ځوابونه ورکړئ.'),
        'lq': ('LONG QUESTIONS. Answer the following questions in detail.', 'طویل سوالات۔ درج ذیل سوالات کے تفصیلی جوابات دیں۔', 'اوږدې پوښتنې. لاندې پوښتنو ته په تفصیل ځواب ورکړئ.')}
# unit 8's exercise items carry no page numbers in the dataset: printed pages of its MCQs / short / long questions
UNIT8_PAGES = {'mcqs': 246, 'sq': 247, 'lq': 248}


def strip_no(s):
    m = re.match(r'^\s*\(?([ivxIVX]+)[.)]\s*(.*)$', str(s or ''), flags=re.S)
    return (m.group(1).lower(), m.group(2)) if m else (None, str(s or ''))


def mcq_tri(q):
    qp = q.get('sourceQuestionPair') or {}
    ops = q.get('sourceOptionPairs') or []
    en_stem = clean(strip_no(qp.get('text') or q['q'])[1])
    L = 'abcdefgh'
    en = en_stem + ' ' + ' '.join(f'({L[i]}) {clean(o)}' for i, o in enumerate(q['opts']))
    if qp.get('urdu') and qp.get('pashto') and len(ops) == len(q['opts']) and all(o.get('urdu') and o.get('pashto') for o in ops):
        ur = clean(strip_no(qp['urdu'])[1]) + ' ' + ' '.join(f'({L[i]}) {clean(o["urdu"])}' for i, o in enumerate(ops))
        ps = clean(strip_no(qp['pashto'])[1]) + ' ' + ' '.join(f'({L[i]}) {clean(o["pashto"])}' for i, o in enumerate(ops))
        return f'{en} || {ur} || {ps}'
    return en


def emit_exercise(c):
    u = c['num']
    te = c.get('textbookExercise') or {}
    items = []          # (page idx, lines)
    nums = [x for x in (c.get('numericals') or []) if x.get('sourcePrintedPage') and (te.get('sq') or te.get('mcqs')) and x['sourcePrintedPage'] >= min(q.get('sourcePrintedPage') or 999 for k in ('mcqs', 'sq', 'lq') for q in te.get(k, []))]
    groups = ['mcqs'] + (['num'] if nums else []) + ['sq', 'lq']
    gno = {g: k + 1 for k, g in enumerate(groups)}
    for key in groups:
        group = nums if key == 'num' else (te.get(key) or [])
        for n, q in enumerate(group):
            if key == 'num':
                pg = BY_PRINTED.get(q['sourcePrintedPage'])
                if pg is None:
                    continue
                L = []
                if n == 0:
                    L.append('q %d | Solve the following numerical questions. || درج ذیل عددی سوالات حل کریں۔ || لاندې عددي پوښتنې حل کړئ.' % gno[key])
                qp_, ap_ = q.get('sourceQuestionPair') or {}, q.get('sourceFinalAnswerPair') or {}
                en = clean(qp_.get('text') or q.get('statement')) + ' ' + clean(ap_.get('text') or '')
                if qp_.get('urdu') and qp_.get('pashto'):
                    L.append(f'q {ROMAN[n]} | {en.strip()} || {clean(qp_["urdu"])} {clean(ap_.get("urdu"))} || {clean(qp_["pashto"])} {clean(ap_.get("pashto"))}')
                else:
                    L.append(f'q {ROMAN[n]} | {en.strip()}')
                L.append('qsolution ' + clean(q.get('answer'))[:200])
                for x in str(q.get('solution') or '').split(chr(10)):
                    if clean(x):
                        L.append('ss ' + clean(x))
                L.append('endsolution')
                items.append((pg, L))
                continue
            pr = q.get('sourcePrintedPage') or ((247 if (key == 'mcqs' and n >= 8) else UNIT8_PAGES[key]) if u == 8 else None)
            pg = BY_PRINTED.get(pr)
            if pg is None:
                PROBLEMS.append(f'unit {u} exercise {key} {n} has no page')
                continue
            L = []
            if n == 0:
                he = HEAD[key]
                L.append(f'q {gno[key]} | {he[0]} || {he[1]} || {he[2]}')
            if key == 'mcqs':
                L.append(f'qp {ROMAN[n]} | {mcq_tri(q)}')
                letter = 'abcdefgh'[q['ans']] if isinstance(q.get('ans'), int) else None
                if letter:
                    L.append(f'solution ({letter})')
                    if q.get('exp'):
                        L.append(f'ss {clean(q["exp"])}')
                    L.append('endsolution')
            else:
                qp = q.get('sourceQuestionPair') or {}
                no, rest = strip_no(q['q'])
                if isinstance(qp, dict) and qp.get('urdu') and qp.get('pashto'):
                    _, ur = strip_no(qp['urdu'])
                    _, ps = strip_no(qp['pashto'])
                    _, en = strip_no(qp.get('text') or q['q'])
                    text = f'{clean(en)} || {clean(ur)} || {clean(ps)}'
                else:
                    text = clean(rest)
                L.append(f'q {no or ROMAN[n]} | {text}')
                for tb in q.get('sourceTables') or []:
                    L.append('table')
                    L.extend(table_lines(tb))
                    L.append('endtable')
                ans = [clean(x) for x in str(q.get('ans') or '').split(chr(10)) if clean(x)]
                cut = next((k for k, x in enumerate(ans) if x.lower().startswith('project work')), None)
                ans = ans[:cut] if cut is not None else ans
                ans = [x for x in ans if not re.match(r'^(Answer|SpaceBook-authored[^:]*):?$', x)]
                if ans:
                    L.append('qsolution ' + ans[0][:200])
                    for x in ans[1:]:
                        L.append('ss ' + x)
                    L.append('endsolution')
            items.append((pg, L))
    seen = set()
    last_pg = items[-1][0] if items else None
    for a in list(te.get('projectWork') or []) + list(te.get('activities') or []):
        sp = a.get('sourcePromptPair') or {}
        text = clean(sp.get('text') or a.get('prompt') or a.get('procedure'))
        if not text or text[:60] in seen or 'Project' not in str(a.get('name') or a.get('title') or a.get('num') or ''):
            continue
        seen.add(text[:60])
        pg = BY_PRINTED.get(a.get('sourcePrintedPage')) if a.get('sourcePrintedPage') else None
        if pg is None:
            pg = last_pg
        if pg is not None:
            body = f'p {text} || {clean(sp["urdu"])} || {clean(sp["pashto"])}' if sp.get('urdu') and sp.get('pashto') else f'p {text}'
            items.append((pg, ['box teach | Project Work || منصوبہ || پروژه', body, 'endbox']))
    if not items:
        return
    first, last = items[0][0], items[-1][0]
    PG[first].lines.append(f'@sec {u}-ex | Exercise || مشق || تمرین')
    PG[first].lines.append(f'exercise {u}')
    for pg, L in items:
        PG[pg].lines.extend(L)
    PG[last].lines.append('endexercise')


def apply_edits(lines, edit_text):
    """fix/pNNN.edit: d 3-5 | s 4 | text | i 2 | text | x 6-7 > p012 end|top   (numbers = body lines as listed by show.py)"""
    heads, body, dirs, pending = [], [], [], []
    for l in lines:
        if l.startswith('@'):
            (heads if not body and l.split()[0] in ('@printed', '@status') else pending).append(l)
        else:
            dirs.append(pending)
            pending = []
            body.append(l)
    tail = pending
    moves, dele, sub, ins = [], set(), {}, {}

    def rng(t):
        a, _, b = t.strip().partition('-')
        return list(range(int(a), int(b or a) + 1))
    for raw in edit_text.splitlines():
        raw = raw.rstrip()
        if not raw or raw.startswith('#'):
            continue
        op, _, rest = raw.partition(' ')
        if op == 'd':
            dele.update(rng(rest))
        elif op == 's':
            n, _, t = rest.partition('|')
            sub[int(n)] = t.strip()
        elif op == 'i':
            n, _, t = rest.partition('|')
            ins.setdefault(int(n), []).append(t.strip())
        elif op == 'x':
            r, _, dest = rest.partition('>')
            parts = dest.split()
            moves.append((rng(r), int(parts[0][1:]), parts[1] if len(parts) > 1 else 'end'))
            dele.update(rng(r))
    out = list(heads)
    out.extend(ins.get(0, []))
    for k, l in enumerate(body, 1):
        out.extend(dirs[k - 1])
        if k not in dele:
            out.append(sub.get(k, l))
        out.extend(ins.get(k, []))
    out.extend(tail)
    return out, [(t, w, [body[i - 1] for i in r]) for r, t, w in moves]


UNIT_NAMES = {4: ('Structure of Molecules', 'سالموں کی ساخت', 'د مالیکولونو جوړښت'),
              5: ('Physical States of Matter', 'مادّے کی طبعی حالتیں', 'د مادې فزیکي حالتونه'),
              6: ('Solutions', 'محلول', 'محلولونه'),
              7: ('Electrochemistry', 'برق کیمیا', 'برقي کیمیا'),
              8: ('Chemical Reactivity', 'کیمیائی تعامل پذیری', 'کیمیاوي عکس العمل منل')}
UNIT_START = {1: 1, 2: 40, 3: 63, 4: 91, 5: 121, 6: 152, 7: 182, 8: 218}


def main(report=False):
    cur = None
    firsts = {}
    for c in C:
        u = c['num']
        i = BY_PRINTED[UNIT_START[u]]
        nm = UNIT_NAMES.get(u) or (c['name'], c.get('nameUr'), c.get('namePs'))
        PG[i].pre.append(f'@unit {u} | {tri(*nm)}')
        PG[i].pre.append(f'@sec {u}-opening | Student Learning Outcomes || طلبہ کے تعلیمی حاصلات || د زده کوونکو د زده کړې پایلې')
        PG[i].lines.append(f'# Unit {u}: {tri(*nm)}')
        PG[i].lines.append('## Student Learning Outcomes || طلبہ کے تعلیمی حاصلات || د زده کوونکو د زده کړې پایلې')
        PG[i].lines.append('p After studying this unit, students will be able to: || اس اکائی کے مطالعے کے بعد طلبہ اس قابل ہوں گے کہ: || د دې څپرکي له لوستلو وروسته به زده کوونکي وکولی شي چې:')
        for sp in c.get('sourceLearningOutcomePairs') or []:
            PG[i].lines.append(f'slo {tri(sp.get("text"), sp.get("urdu"), sp.get("pashto"))}')
    for ci, c in enumerate(C):
        unit = c['num']
        for t in c['topics']:
            for sec in t['subtopics']:
                before = [len(p.lines) for p in PG]
                cur = emit_sub(unit, t, sec, cur)
                for i, p in enumerate(PG):
                    if len(p.lines) != before[i]:
                        firsts.setdefault((unit, t.get('num'), sec.get('num')), i)
                        sid = sec.get('num') or t.get('num')
                        p.pre_sec = getattr(p, 'pre_sec', []) + [f'@sec {sid} | {tri(sec.get("name") or "", sec.get("headingUrdu"), sec.get("headingPashto"))}']
                        # section directive goes before the section's first line on that page
                        p.lines.insert(before[i], p.pre_sec.pop())
                        break
    for c in C:
        emit_exercise(c)
    for p in PROBLEMS:
        print('PROBLEM', p)
    if report:
        return
    out = HERE / 'pages'
    out.mkdir(exist_ok=True)
    fix = HERE / 'fix'
    xfer = {}          # lines moved to other pages by fix/*.edit: {target page: [(where, [lines])]}
    texts = {}
    for i, page in enumerate(PG):
        f = fix / f'p{i:03}.txt'
        head = []
        printed = PAGES[i][2]
        if printed is not None:
            head.append(f'@printed {printed}')
        head.append('@status ' + ('front-matter' if i < 4 else 'back-matter' if i >= len(PAGES) - 2 else 'lesson'))
        if f.exists():
            texts[i] = f.read_text(encoding='utf-8').splitlines()
            continue
        lines = head + page.pre + boxify(page.lines)
        ef = fix / f'p{i:03}.edit'
        if ef.exists():
            lines, moved = apply_edits(lines, ef.read_text(encoding='utf-8'))
            for t, w, ls in moved:
                xfer.setdefault(t, []).append((w, ls))
        texts[i] = lines
    for t, items in xfer.items():
        lines = texts[t]
        k = next((n for n, l in enumerate(lines) if not l.startswith('@')), len(lines))
        for w, ls in items:
            if w == 'top':
                lines[k:k] = ls
            else:
                lines.extend(ls)
    for i in range(len(PG)):
        (out / f'p{i:03}.txt').write_text('\n'.join(texts[i]) + '\n', encoding='utf-8')
    empty = [i for i, p in enumerate(PG) if not p.lines and not (fix / f'p{i:03}.txt').exists()]
    print('pages written', len(PG), 'empty', len(empty), empty[:40])


if __name__ == '__main__':
    main(report=len(sys.argv) > 1 and sys.argv[1] == 'report')
