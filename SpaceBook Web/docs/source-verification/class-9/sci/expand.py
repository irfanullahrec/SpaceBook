# -*- coding: utf-8 -*-
"""Class 9 General Science page builder: src/pNNN.src -> pages/pNNN.txt (pNNN = JPG number - 1).

The English text and its Urdu/Pashto translations were verified paragraph by paragraph in the
earlier audit (class-9/genscience/unitNN.py). Page sources reuse them by reference:

    use U SEC A-B      paragraphs A..B of section SEC of unit U       -> p lines
    use U SEC h        that section's heading                         -> ## heading line
    use U slo A-B      SLO items                                      -> slo lines
    use U kp A-B       key points                                     -> - lines
    use U mcq A-B      MCQs (question + options)                      -> qp lines
    use U mcqsol       SpaceBook answer line for all MCQs of the unit -> sol line
    use U sq A-B / use U lq A-B   short / long questions              -> qp lines (+ sol with answer)
    use gl A-B         glossary rows                                  -> tr lines
A paragraph range may be followed by "|split" to keep only part of a paragraph:
    use 1 1.1 3 |to:Mesopotamians        text up to and including that word (rest goes on next page)
    use 1 1.1 3 |from:Mesopotamians      text after that word
(split is applied to the English; the whole Urdu/Pashto translation goes with the |to part.)

    python -X utf8 sci/expand.py list U          print reference ids with English previews
    python -X utf8 sci/expand.py NNN [NNN ...] | all
"""
import importlib, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'genscience'))
LET = 'abcd'


def unit(n):
    return importlib.import_module(f'unit{n:02d}')


def sections(n):
    """[(refid, section)] in book order, duplicates removed; refid has no spaces and is unique."""
    U = unit(n)
    seen, out, ids = set(), [], set()
    for s in list(U.SECTIONS) + list(getattr(U, 'SECTIONS_B', [])):
        if id(s) in seen or any(s is o for _, o in out) or any(s[0] == o[0] and s[1] == o[1] and s[2] == o[2] for _, o in out):
            continue
        seen.add(id(s))
        rid = s[0].replace(' ', '_').replace('(', '').replace(')', '')
        while rid in ids:
            rid += '+'
        ids.add(rid)
        out.append((rid, s))
    return out


def find_sec(n, sec):
    for rid, s in sections(n):
        if rid == sec:
            return s
    raise SystemExit(f'unit {n}: no section {sec}')


def rng(a):
    if '-' in a:
        x, y = a.split('-')
        return range(int(x), int(y) + 1)
    return [int(a)]


def tri(t):
    return ' || '.join(x.replace('||', '{{OR}}').replace(chr(10), ' ') for x in t)


def split_text(t, mode, word):
    en = t[0]
    i = en.find(word)
    if i < 0:
        raise SystemExit(f'split word not found: {word!r} in {en[:60]!r}')
    cut = i + len(word)
    if mode == 'to':
        return (en[:cut].rstrip(), t[1], t[2])
    return (en[cut:].lstrip(' ,;'), '↑', '↑')


FIG_SVG = ('<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Textbook photograph">'
           '<rect x="2" y="2" width="356" height="116" rx="10" fill="#f4f7fb" stroke="#9fb3c8" stroke-dasharray="6 4"/>'
           '<rect x="24" y="24" width="96" height="72" rx="6" fill="#dde7f1" stroke="#7d93ab"/>'
           '<circle cx="98" cy="42" r="8" fill="#f2c14e"/><path d="M28 92 L58 56 L80 80 L94 66 L116 92 Z" fill="#7fa36b"/>'
           '<text x="140" y="54" font-size="15" font-family="sans-serif" fill="#34495e">{label}</text>'
           '<text x="140" y="78" font-size="12" font-family="sans-serif" fill="#5d6d7e">Photograph / diagram in the textbook</text>'
           '<text x="140" y="96" font-size="12" font-family="sans-serif" fill="#5d6d7e">(see the scan of page {page})</text></svg>')

BOXES = (('For Your Information', 'note', 'For Your Information || آپ کی معلومات کے لیے || ستاسو د معلوماتو لپاره'),
         ('Do You Know?', 'note', 'Do You Know? || کیا آپ جانتے ہیں؟ || آیا پوهېږئ؟'),
         ('Activity', 'activity', 'Activity || سرگرمی || فعالیت'),
         ('Tidbit', 'note', 'Tidbit || دلچسپ بات || په زړه پورې ټکی'))


CAP = re.compile(r'\s*\((?:Fig|Figure|Figs|شکل|اشکال|انځور)(?=[\s.:\d,،])')


def strip_caps(x):
    """Remove '(Fig ...)' captions (balanced parentheses; an unclosed one runs to the end) - figures are panels now."""
    while True:
        m = CAP.search(x)
        if not m:
            return x
        d, j = 0, m.start() + len(m.group(0)) - len(m.group(0).lstrip())
        while j < len(x):
            d += {'(': 1, ')': -1}.get(x[j], 0)
            j += 1
            if d == 0:
                break
        x = (x[:m.start()] + ' ' + x[j:].lstrip()).strip() if d == 0 else x[:m.start()].rstrip()


def strip_label(t):
    m = re.search(r'[:؟?]| - ', t[:45])
    return t[m.end():].strip() if m else t


def boxed(t):
    for lab, kind, title in BOXES:
        if t[0].startswith(lab):
            body = tuple(strip_label(x) for x in t)
            return [f'box {kind} | {title}', f'p {tri(body)}', 'endbox']
    return None


def resolve(line):
    parts, _, opt = line[4:].partition('|')
    a = parts.split()
    out = []
    if a[0] == 'tbl':
        from figs import TABLES
        return list(TABLES[int(a[1])][2])
    if a[0] == 'fig':
        from figs import FIGS
        pg, lab, en, ur, ps, _ = FIGS[int(a[1])]
        lu = lab.replace('Fig', 'شکل').replace('Figure', 'شکل')
        lp = lab.replace('Fig', 'شکل').replace('Figure', 'شکل')
        return [f'svg {lab}: {en} || {lu}: {ur} || {lp}: {ps}'.replace('شکلure', 'شکل'), FIG_SVG.format(label=lab, page=pg), 'endsvg']
    if a[0] == 'gl':
        from glossary import GLOSSARY
        for i in rng(a[1]):
            t, m, ur, ps, pg = GLOSSARY[i]
            out.append(f'tr | {t} | {m} || {ur} || {ps}')
        return out
    n, kind = int(a[0]), a[1]
    U = unit(n)
    if kind == 'slo':
        return [f'slo {tri(U.SLOS[i])}' for i in rng(a[2])]
    if kind == 'kp':
        r = list(rng(a[2]))
        if r[0] == 0:
            out += [f'@sec {n}-kp | Key Points || اہم نکات || مهم ټکي', '## Key Points || اہم نکات || مهم ټکي']
        return out + [f'- {tri(U.KEY_POINTS[i])}' for i in r]
    if kind == 'mcq':
        r = list(rng(a[2]))
        if r[0] == 0:
            out += [f'@sec {n}-ex | Exercise || مشق || تمرین', '@tab doing', '# Exercise || مشق || تمرین',
                    'q 1 | Choose the correct answer. || درست جواب کا انتخاب کریں۔ || سم ځواب وټاکئ.']
        for i in r:
            q, opts, c, expl = U.MCQS[i]
            o = ' '.join(f'({LET[k]}) {x}' for k, x in enumerate(opts))
            out.append(f'qp {i + 1} | {q[0]} {o} || {q[1]} {o} || {q[2]} {o}')
        if r[-1] == len(U.MCQS) - 1:
            out += resolve(f'use {n} mcqsol')
        return out
    if kind == 'mcqsol':
        ans = '; '.join(f'{i + 1}: ({LET[m[2]]}) {m[1][m[2]]}' for i, m in enumerate(U.MCQS))
        why = ' '.join(f'{i + 1}. {m[3]}' for i, m in enumerate(U.MCQS))
        return [f'sol {ans} ## SpaceBook answers (the textbook prints no key). {why} || SpaceBook جوابات (کتاب میں جوابی کلید نہیں)۔ || د SpaceBook ځوابونه (کتاب کې کیلي نشته).']
    if kind in ('sq', 'lq'):
        items = U.SQS if kind == 'sq' else U.LQS
        r = list(rng(a[2]))
        if r[0] == 0:
            qn = 2 if kind == 'sq' or not getattr(U, 'SQS', None) else 3
            label = ('Answer the following short questions. || درج ذیل مختصر سوالات کے جواب دیں۔ || لاندې لنډې پوښتنې ځواب کړئ.' if kind == 'sq'
                     else 'Answer the following questions in detail. || درج ذیل سوالات کے تفصیلی جواب دیں۔ || لاندې پوښتنو ته مفصل ځواب ورکړئ.')
            out.append(f'q {qn} | {label}')
        for i in r:
            q, ans = items[i]
            out.append(f'qp {i + 1} | {tri(q)}')
            out.append(f'sol See the unit text ## {ans} || {ans} || {ans}')
        return out
    sec = find_sec(n, kind)
    if a[2] == 'h':
        if 'cont' in sec[0]:
            return [f'@sec {n}-{kind} | {sec[1][0]} || {sec[1][1]} || {sec[1][2]}']
        if not sec[0].replace('.', '').isdigit():
            return [f'@sec {n}-{kind} | {sec[1][0]} || {sec[1][1]} || {sec[1][2]}', f'### {tri(sec[1])}']
        return [f'@sec {n}-{kind} | {sec[0]} {sec[1][0]} || {sec[0]} {sec[1][1]} || {sec[0]} {sec[1][2]}',
                f'## {sec[0]} {sec[1][0]} || {sec[0]} {sec[1][1]} || {sec[0]} {sec[1][2]}']
    for i in rng(a[2]):
        t = sec[2][i]
        if t[0].startswith('Table 4.3'):
            from figs import TABLE43
            out += TABLE43
            continue
        if t[0].startswith('Fig'):
            continue                       # caption-only paragraph: the figure panel (figs.py) replaces it
        if not opt.strip():
            t = tuple(strip_caps(x) for x in t)
        else:
            t = (t[0], strip_caps(t[1]), strip_caps(t[2]))
        if opt.strip():
            mode, _, word = opt.strip().partition(':')
            if mode in ('wto', 'wfrom'):
                w = t[0].split()
                k = int(word)
                head = strip_caps(' '.join(w[:k]))
                cw = strip_caps(t[0]).split()
                kk = len(head.split())
                t = (' '.join(cw[:kk]), t[1], t[2]) if mode == 'wto' else (' '.join(cw[kk:]), '↑', '↑')
            else:
                t = split_text(t, mode, word)
        tid = None
        if 'Tidbit:' in t[0]:              # a Tidbit box printed beside the paragraph: split it out
            cut = [t[0].index('Tidbit:')]
            for x, mk in ((t[1], ('دلچسپ بات:',)), (t[2], ('لنډ معلومات:', 'په زړه پورې ټکی:', 'دلچسپ ټکی:'))):
                k = next((x.index(m) for m in mk if m in x), -1)
                cut.append(k)
            tid = tuple(x[c:].strip() if c >= 0 else '↑' for x, c in zip(t, cut))
            t = tuple(x[:c].strip() if c >= 0 else x for x, c in zip(t, cut))
        bx = boxed(t) if not opt.strip() else None
        if bx:
            out += bx
        elif t[0].startswith('Fig'):
            out.append(f'p ({t[0]}) || ({t[1]}) || ({t[2]})')
        elif any(chr(10) in c for c in t):
            L3 = [[x.strip() for x in col.split(chr(10)) if x.strip()] for col in t]
            if len(L3[0]) == len(L3[1]) == len(L3[2]):
                for k, row in enumerate(zip(*L3)):
                    bullet = row[0][:1] in '•·▪-–' or k > 0
                    row = tuple(r.lstrip('•·▪-– ').strip() for r in row)
                    out.append(('- ' if bullet else 'p ') + tri(row))
            else:
                out.append('p ' + tri(tuple(' / '.join(c) for c in L3)))
        else:
            out.append(f'p {tri(t)}')
        if tid:
            out += boxed(tid) if tid[1] != '↑' else ['box note | Tidbit || دلچسپ بات || په زړه پورې ټکی', f'p {strip_label(tid[0])} || ↑ || ↑', 'endbox']
    return out


def expand(n):
    src = (HERE / 'src' / f'p{n:03}.src').read_text(encoding='utf-8')
    out = []
    for line in src.splitlines():
        out += resolve(line) if line.startswith('use ') else [line]
    (HERE / 'pages' / f'p{n:03}.txt').write_text('\n'.join(out).rstrip('\n') + '\n', encoding='utf-8')


def listing(n):
    U = unit(n)
    print('SLO', len(U.SLOS), 'KP', len(U.KEY_POINTS), 'MCQ', len(U.MCQS), 'SQ', len(getattr(U, 'SQS', [])), 'LQ', len(U.LQS))
    for rid, s in sections(n):
        print(f'== {rid} {s[1][0]}  pages {s[3] if len(s) > 3 else ""}')
        for i, p in enumerate(s[2]):
            print(f'  {i:2d} {p[0][:90]}')


if __name__ == '__main__':
    if sys.argv[1] == 'list':
        listing(int(sys.argv[2])); raise SystemExit
    ns = sorted(int(p.stem[1:]) for p in (HERE / 'src').glob('p*.src')) if sys.argv[1:] == ['all'] else [int(a) for a in sys.argv[1:]]
    for n in ns:
        expand(n)
    print('expanded', ns)
