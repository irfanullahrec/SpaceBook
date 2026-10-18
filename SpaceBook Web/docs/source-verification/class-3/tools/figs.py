"""SVG generators for recurring Class 6 Mathematics figures (long division, division ladder, factor tree)."""
import re
from html import escape

FONT = "font-family=\"Consolas, 'Courier New', monospace\" font-size=\"18\" fill=\"#0f172a\""


def longdiv(spec):
    """'15 | 250 | 16@2 | -15@1 ; 100@2 ; -90@2 ; 10@2'  — text@col: last character sits under dividend digit col."""
    parts = [p.strip() for p in spec.split('|')]
    divisor, dividend, quotient = parts[0], parts[1], parts[2]
    steps = [s.strip() for s in parts[3].split(';')] if len(parts) > 3 and parts[3] else []
    cw, lh = 11, 26
    dx = 16 + len(divisor) * cw + 14       # x of dividend start
    def at(token):
        text, _, col = token.partition('@')
        col = int(col) if col else len(dividend) - 1
        return text.strip(), dx + (col + 1) * cw
    q, qx = at(quotient)
    out = [f'<text x="{qx}" y="22" text-anchor="end">{escape(q)}</text>',
           f'<text x="{dx - 14}" y="{22 + lh}" text-anchor="end">{escape(divisor)}</text>',
           f'<path d="M{dx - 10} {lh + 30} q8 -14 0 -30 H{dx + max(len(dividend), 3) * cw + 22}" fill="none" stroke="#0f172a" stroke-width="1.5"/>',
           f'<text x="{dx + len(dividend) * cw}" y="{22 + lh}" text-anchor="end">{escape(dividend)}</text>']
    y = 22 + lh
    width = dx + max(len(dividend), 3) * cw + 30
    for s in steps:
        t, x = at(s)
        y += lh
        out.append(f'<text x="{x}" y="{y}" text-anchor="end">{escape(t.replace("-", "−"))}</text>')
        if t.startswith('-'):
            out.append(f'<line x1="{x - len(t) * cw - 2}" y1="{y + 7}" x2="{x + 2}" y2="{y + 7}" stroke="#0f172a" stroke-width="1.3"/>')
    h = y + 12
    label = f'Long division of {dividend} by {divisor}: quotient {q}' + (f', remainder {steps[-1].split("@")[0]}' if steps else '')
    return f'<svg viewBox="0 0 {width} {h}" width="{width}" role="img" aria-label="{escape(label)}" {FONT}>' + ''.join(out) + '</svg>'


def ladder(spec):
    """'2:60, 2:30, 3:15, :5' — division ladder used for prime factorization / HCF / LCM."""
    rows = [tuple(x.strip() for x in r.split(':', 1)) for r in spec.split(';' if ';' in spec else ',')]
    lw = max(len(r[0]) for r in rows) * 11 + 16
    rw = max(len(r[1]) for r in rows) * 11 + 40
    lh = 32
    out = []
    for i, (d, n) in enumerate(rows):
        y = 8 + i * lh
        out.append(f'<text x="{lw - 8}" y="{y + 22}" text-anchor="end">{escape(d)}</text>')
        out.append(f'<text x="{lw + rw / 2}" y="{y + 22}" text-anchor="middle">{escape(n)}</text>')
        if i < len(rows) - 1:
            out.append(f'<line x1="2" y1="{y + lh}" x2="{lw + rw}" y2="{y + lh}" stroke="#0f172a" stroke-width="1.3"/>')
    h = 8 + len(rows) * lh + 4
    out.append(f'<line x1="{lw}" y1="4" x2="{lw}" y2="{h - 4}" stroke="#0f172a" stroke-width="1.5"/>')
    label = 'Division ladder: ' + '; '.join(f'{n} ÷ {d}' if d else n for d, n in rows)
    return f'<svg viewBox="0 0 {lw + rw + 4} {h}" width="{lw + rw + 4}" role="img" aria-label="{escape(label)}" {FONT}>' + ''.join(out) + '</svg>'


def _parse(s, i=0):
    m = re.match(r'\s*([^(),\s]+)', s[i:])
    node = {'v': m.group(1), 'c': []}
    i += m.end()
    if i < len(s) and s[i] == '(':
        i += 1
        while True:
            child, i = _parse(s, i)
            node['c'].append(child)
            if s[i] == ',':
                i += 1
            elif s[i] == ')':
                i += 1
                break
    return node, i


def ftree(spec):
    """'120(10(5*,2*),12(3*,4(2*,2*)))' — factor tree; '*' marks circled prime leaves."""
    allc = spec.startswith('#')
    root, _ = _parse(spec.lstrip('#').replace(' ', ''))
    leaves = []
    def place(n, d):
        n['d'] = d
        if not n['c']:
            n['x'] = len(leaves); leaves.append(n)
        else:
            for c in n['c']:
                place(c, d + 1)
            n['x'] = sum(c['x'] for c in n['c']) / len(n['c'])
    place(root, 0)
    sx, sy, px, py = 58, 62, 34, 26
    out = []
    def draw(n):
        x, y = px + n['x'] * sx, py + n['d'] * sy
        for c in n['c']:
            cx, cy = px + c['x'] * sx, py + c['d'] * sy
            out.append(f'<line x1="{x}" y1="{y + 10}" x2="{cx}" y2="{cy - 16}" stroke="#334155" stroke-width="1.4"/>')
            draw(c)
        if allc and len(n['c']) == 2:
            a, b2 = n['c']
            out.append(f'<text x="{px + (a["x"] + b2["x"]) / 2 * sx}" y="{py + a["d"] * sy}" text-anchor="middle">×</text>')
        v = n['v']
        prime = v.endswith('*') or allc
        v = v.rstrip('*')
        if prime:
            out.append(f'<circle cx="{x}" cy="{y - 6}" r="15" fill="#e0f2fe" stroke="#0284c7"/>')
        out.append(f'<text x="{x}" y="{y}" text-anchor="middle">{escape(v)}</text>')
    draw(root)
    depth = max(l['d'] for l in leaves)
    w = px * 2 + (len(leaves) - 1) * sx
    h = py + depth * sy + 22
    label = f'Factor tree of {root["v"]}; prime factors ' + ' × '.join(l['v'].rstrip('*') for l in leaves)
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" font-size="17" fill="#0f172a">' + ''.join(out) + '</svg>'


def stair(spec):
    """Continued division (HCF by division). Steps separated by ';', each 'divisor|dividend|quotient|w1,w2,...'.
    Working tokens may carry @col (dividend digit column for the last character). Labels: 'divisor<label',
    'dividend>label' (arrow towards the label). The remainder of each step is the next step's divisor."""
    steps = []
    for raw in spec.split(';'):
        f = [x.strip() for x in raw.split('|')]
        steps.append({'d': f[0], 'n': f[1], 'q': f[2], 'w': [x.strip() for x in f[3].split(',')] if len(f) > 3 and f[3] else []})
    def lab(tok, ch):
        t, _, l = tok.partition(ch)
        return t.strip(), l.strip()
    cw, rh = 11, 25
    maxlen = max(len(lab(s['n'], '>')[0]) for s in steps)
    W = maxlen * cw + 34
    left = max([len(lab(s['d'], '<')[1]) * 7.5 + 40 for s in steps if '<' in s['d']] + [0])
    X0 = 20 + left + max(len(lab(s['d'], '<')[0]) for s in steps) * cw + 8
    out = []
    ymax = 0
    xmax = 0
    for k, s in enumerate(steps):
        b = X0 + k * W
        R = b + W - 8
        drow = 1 + 2 * k
        y = lambda r: 22 + r * rh
        d, dl = lab(s['d'], '<')
        n, nl = lab(s['n'], '>')
        out.append(f'<text x="{R}" y="{y(drow - 1)}" text-anchor="end">{escape(s["q"])}</text>')
        out.append(f'<line x1="{b}" y1="{y(drow - 1) + 7}" x2="{b + W}" y2="{y(drow - 1) + 7}" stroke="#0f172a" stroke-width="1.4"/>')
        out.append(f'<line x1="{b}" y1="{y(drow - 1) + 7}" x2="{b}" y2="{y(drow) + 8}" stroke="#0f172a" stroke-width="1.4"/>')
        out.append(f'<text x="{b - 6}" y="{y(drow)}" text-anchor="end">{escape(d)}</text>')
        out.append(f'<line x1="{b - len(d) * cw - 10}" y1="{y(drow) + 8}" x2="{b}" y2="{y(drow) + 8}" stroke="#0f172a" stroke-width="1.4"/>')
        out.append(f'<text x="{R}" y="{y(drow)}" text-anchor="end">{escape(n)}</text>')
        if dl:
            x2 = b - len(d) * cw - 12
            out.append(f'<line x1="{x2}" y1="{y(drow) - 6}" x2="{x2 - 34}" y2="{y(drow) - 6}" stroke="#334155" stroke-dasharray="2 2"/><path d="M{x2 - 34} {y(drow) - 6} l7 -4 v8 z" fill="#334155"/>')
            out.append(f'<text x="{x2 - 38}" y="{y(drow)}" text-anchor="end" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#0369a1">{escape(dl)}</text>')
        if nl:
            x1 = R + 6
            out.append(f'<line x1="{x1}" y1="{y(drow) - 6}" x2="{x1 + 34}" y2="{y(drow) - 6}" stroke="#334155" stroke-dasharray="2 2"/><path d="M{x1 + 34} {y(drow) - 6} l-7 -4 v8 z" fill="#334155"/>')
            out.append(f'<text x="{x1 + 38}" y="{y(drow)}" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#0369a1">{escape(nl)}</text>')
            xmax = max(xmax, x1 + 40 + len(nl) * 7.5)
        start = R - len(n) * cw
        for i, tok in enumerate(s['w']):
            t, _, col = tok.partition('@')
            x = start + (int(col) + 1) * cw if col else R
            r = drow + 1 + i
            out.append(f'<text x="{x}" y="{y(r)}" text-anchor="end">{escape(t.replace("-", "−"))}</text>')
            if t.startswith('-'):
                out.append(f'<line x1="{b - (0 if k == len(steps) - 1 else 0) - 4}" y1="{y(r) + 7}" x2="{b + W + (W if k < len(steps) - 1 else 0) * 0}" y2="{y(r) + 7}" stroke="#0f172a" stroke-width="1.3"/>')
            ymax = max(ymax, y(r))
        ymax = max(ymax, y(drow))
        xmax = max(xmax, b + W + 4)
    label = 'Continued division: ' + '; '.join(f'{lab(s["n"], ">")[0]} ÷ {lab(s["d"], "<")[0]} = {s["q"]}' for s in steps)
    return f'<svg viewBox="0 0 {xmax + 6} {ymax + 12}" width="{xmax + 6}" role="img" aria-label="{escape(label)}" {FONT}>' + ''.join(out) + '</svg>'


def nline(spec):
    """'-5..11 | 0>9 above | 9>6 below | dots=-3,2 | q=-1' : number line with ticks, curved jump arrows,
    optional filled dots and a '?' label at position q (drawn instead of the number)."""
    parts = [p.strip() for p in spec.split('|')]
    a, b = [int(x) for x in parts[0].split('..')]
    arcs, dots, qpos, labels, circ, braces, tops = [], [], None, None, [], [], []
    for p in parts[1:]:
        if p.startswith('dots='):
            dots = [float(x) for x in p[5:].split(',')]
        elif p.startswith('q='):
            qpos = int(p[2:])
        elif p.startswith('labels='):
            labels = p[7:].split(',')
        elif p.startswith('circ='):
            circ = [int(x) for x in p[5:].split(',')]
        elif p.startswith('brace='):
            braces = [x.split(':') for x in p[6:].split(';')]
        elif p.startswith('top='):
            tops = [x.split(':') for x in p[4:].split(';')]
        else:
            m = re.match(r'(-?\d+)\s*>\s*(-?\d+)\s*(above|below)?', p)
            arcs.append((int(m.group(1)), int(m.group(2)), m.group(3) or 'above'))
    import hashlib
    mid = 'nl' + hashlib.md5(spec.encode()).hexdigest()[:8]
    n = b - a
    step = max(26, min(52, 640 // max(n, 1)))
    x0, y = 24, 70 if not tops else 84
    X = lambda v: x0 + (v - a) * step
    w = X(b) + 24
    out = [f'<line x1="{x0 - 16}" y1="{y}" x2="{X(b) + 16}" y2="{y}" stroke="#0f172a" stroke-width="1.6"/>',
           f'<path d="M{x0 - 18} {y} l9 -5 v10 z" fill="#0f172a"/><path d="M{X(b) + 18} {y} l-9 -5 v10 z" fill="#0f172a"/>']
    for v in range(a, b + 1):
        out.append(f'<line x1="{X(v)}" y1="{y - 7}" x2="{X(v)}" y2="{y + 7}" stroke="#0f172a" stroke-width="1.4"/>')
        lab = '?' if v == qpos else (labels[v - a] if labels else str(v).replace('-', '−'))
        out.append(f'<text x="{X(v)}" y="{y + 26}" text-anchor="middle" font-size="15">{escape(lab)}</text>')
    for d in dots:
        out.append(f'<circle cx="{X(d)}" cy="{y}" r="5" fill="#dc2626"/>')
    for c in circ:
        out.append(f'<circle cx="{X(c)}" cy="{y + 21}" r="12" fill="none" stroke="#dc2626" stroke-width="1.6"/>')
    for s0, e0, txt in braces:
        xa, xb = X(int(s0)), X(int(e0))
        yb = y + 38
        out.append(f'<path d="M{xa} {yb} q0 8 8 8 H{(xa + xb) / 2 - 8} q8 0 8 8 q0 -8 8 -8 H{xb - 8} q8 0 8 -8" fill="none" stroke="#334155" stroke-width="1.3"/>')
        out.append(f'<text x="{(xa + xb) / 2}" y="{yb + 34}" text-anchor="middle" font-size="14" font-weight="700">{escape(txt)}</text>')
    for s0, e0, txt in tops:
        xa, xb = X(int(s0)), X(int(e0))
        out.append(f'<line x1="{xa}" y1="{y - 30}" x2="{xb}" y2="{y - 30}" stroke="#0f172a" stroke-width="1.5" marker-end="url(#{mid}t)"/>')
        out.append(f'<text x="{(xa + xb) / 2}" y="{y - 40}" text-anchor="middle" font-size="14" font-weight="700">{escape(txt)}</text>')
    for s, e, side in arcs:
        x1, x2 = X(s), X(e)
        h = min(46, 14 + abs(e - s) * 4)
        cy = y - h if side == 'above' else y + 34 + h
        y1 = y - 8 if side == 'above' else y + 32
        color = '#0f766e' if side == 'above' else '#7c3aed'
        out.append(f'<path d="M{x1} {y1} Q{(x1 + x2) / 2} {cy} {x2} {y1}" fill="none" stroke="{color}" stroke-width="1.8"/>')
        out[-1] = out[-1].replace('/>', f' marker-end="url(#{mid}{side[0]})"/>')
    out.insert(0, f'<defs><marker id="{mid}a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0f766e"/></marker><marker id="{mid}b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#7c3aed"/></marker><marker id="{mid}t" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#0f172a"/></marker></defs>')
    label = f'Number line from {a} to {b}' + ''.join(f'; arrow from {s} to {e}' for s, e, _ in arcs)
    hgt = y + (90 if braces else (40 + max([min(46, 14 + abs(e - s) * 4) for s, e, sd in arcs if sd == 'below'] + [0])))
    return f'<svg viewBox="0 0 {w} {hgt}" width="{w}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def beads(spec):
    """'10x10 | 60:#dc2626:red | 40:#38bdf8:blue' -> grid of coloured beads filled row by row."""
    parts = [p.strip() for p in spec.split('|')]
    rows, cols = [int(x) for x in parts[0].split('x')]
    groups = [p.split(':') for p in parts[1:]]
    colours = []
    for n, col, _name in groups:
        colours += [col] * int(n)
    r, gap = 9, 24
    out = []
    for i, col in enumerate(colours[:rows * cols]):
        x, y = 14 + (i % cols) * gap, 14 + (i // cols) * gap
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#334155" stroke-width="1"/><circle cx="{x - 3}" cy="{y - 3}" r="2.2" fill="#fff" fill-opacity=".7"/>')
    w, h = 28 + (cols - 1) * gap, 28 + (rows - 1) * gap
    label = 'Grid of ' + ', '.join(f'{n} {name} beads' for n, _c, name in groups)
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="{escape(label)}">' + ''.join(out) + '</svg>'


def grid(spec):
    """'10x10 | #84cc16:1-2:1-10 ; #84cc16:3-3:1-5' -> grid with coloured rectangles (cols a-b, rows c-d, 1-based)."""
    parts = [p.strip() for p in spec.split('|')]
    rows, cols = [int(x) for x in parts[0].split('x')]
    fills = {}
    counts = {}
    if len(parts) > 1:
        for rect in parts[1].split(';'):
            col, cr, rr = rect.strip().split(':')
            c1, c2 = [int(x) for x in cr.split('-')]
            r1, r2 = [int(x) for x in rr.split('-')]
            for c in range(c1, c2 + 1):
                for r in range(r1, r2 + 1):
                    fills[(r, c)] = col
    for v in fills.values():
        counts[v] = counts.get(v, 0) + 1
    s = 24
    out = []
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            out.append(f'<rect x="{2 + (c - 1) * s}" y="{2 + (r - 1) * s}" width="{s}" height="{s}" fill="{fills.get((r, c), "#ffffff")}" stroke="#334155" stroke-width="1"/>')
    w, h = 4 + cols * s, 4 + rows * s
    label = f'{rows} by {cols} grid; ' + ', '.join(f'{n} cells coloured {k}' for k, n in counts.items())
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="{escape(label)}">' + ''.join(out) + '</svg>'


def bar(spec):
    """'parts=10 | fill=3 | top=30 | bottom=3/10 or 30% | colour=#ef4444' (parts=0 -> one continuous bar, fill as fraction e.g. 0.08)."""
    o = dict(p.strip().split('=', 1) for p in spec.split('|'))
    parts = int(o.get('parts', 0))
    col = o.get('colour', '#ef4444')
    W, x0, y0, bh = 560, 20, 48, 42
    out = []
    if parts:
        u = W / parts
        fill = int(o.get('fill', 0))
        for i in range(parts):
            out.append(f'<rect x="{x0 + i * u:.1f}" y="{y0}" width="{u:.1f}" height="{bh}" fill="{col if i < fill else "#fff"}" stroke="#334155" stroke-width="1.2"/>')
        fw = fill * u
    else:
        fw = W * float(o.get('fill', 0))
        out.append(f'<rect x="{x0}" y="{y0}" width="{W}" height="{bh}" fill="#fff" stroke="#334155" stroke-width="1.2"/>')
        out.append(f'<rect x="{x0}" y="{y0}" width="{fw:.1f}" height="{bh}" fill="{col}" stroke="#334155" stroke-width="1.2"/>')

    def brace(xa, xb, y, up):
        m = (xa + xb) / 2
        d = -1 if up else 1
        return f'<path d="M{xa} {y - 6 * d} v{6 * d} H{m - 8} l8 {8 * d} l8 {-8 * d} H{xb} v{-6 * d}" fill="none" stroke="#334155" stroke-width="1.2"/>'
    if 'top' in o:
        out.append(brace(x0, x0 + W, y0 - 8, True))
        out.append(f'<text x="{x0 + W / 2}" y="{y0 - 22}" text-anchor="middle" font-size="16">{escape(o["top"])}</text>')
    if 'bottom' in o:
        out.append(brace(x0, x0 + fw, y0 + bh + 8, False))
        out.append(f'<text x="{x0 + fw / 2}" y="{y0 + bh + 40}" text-anchor="middle" font-size="16">{escape(o["bottom"])}</text>')
    label = f'Bar model: total {o.get("top", "")}, shaded part {o.get("bottom", "")}'
    return f'<svg viewBox="0 0 {W + 40} {y0 + bh + 54}" width="{W + 40}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


_ICON = {
    'pencil': ('<g transform="rotate(-45 0 0)"><rect x="-4" y="-22" width="8" height="34" fill="#cbd5e1" stroke="#334155"/>'
               '<path d="M-4 12 L0 22 L4 12 Z" fill="#fde68a" stroke="#334155"/><rect x="-4" y="-26" width="8" height="5" fill="#94a3b8" stroke="#334155"/></g>', 36),
    'book': ('<rect x="-12" y="-17" width="24" height="34" rx="2" fill="#dc2626" stroke="#7f1d1d"/><line x1="-8" y1="-17" x2="-8" y2="17" stroke="#7f1d1d"/>', 34),
    'ball': ('<circle r="13" fill="#f97316" stroke="#7c2d12"/><path d="M-13 0 H13 M0 -13 V13" stroke="#7c2d12" fill="none"/>', 32),
    'apple': ('<circle r="13" fill="#dc2626" stroke="#7f1d1d"/><path d="M0 -13 q2 -6 6 -7" stroke="#14532d" fill="none" stroke-width="2"/>', 32),
    # Class 3 counting objects
    'sharpener': ('<rect x="-13" y="-10" width="26" height="20" rx="3" fill="#2563eb" stroke="#1e3a8a"/><rect x="-6" y="-10" width="12" height="7" fill="#cbd5e1" stroke="#475569"/><circle cx="4" cy="3" r="4" fill="#1e3a8a"/>', 34),
    'chocolate': ('<rect x="-15" y="-10" width="30" height="20" rx="3" fill="#78350f" stroke="#451a03"/><path d="M-5 -10 V10 M5 -10 V10 M-15 0 H15" stroke="#451a03"/>', 38),
    'die': ('<rect x="-12" y="-12" width="24" height="24" rx="4" fill="#fff" stroke="#334155" stroke-width="1.5"/><circle cx="-6" cy="-6" r="2.2" fill="#0f172a"/><circle r="2.2" fill="#0f172a"/><circle cx="6" cy="6" r="2.2" fill="#0f172a"/>', 32),
    'star': ('<path d="M0 -14 L4 -4 L14 -4 L6 3 L9 13 L0 7 L-9 13 L-6 3 L-14 -4 L-4 -4 Z" fill="#facc15" stroke="#a16207"/>', 32),
    'flower': ('<g fill="#f472b6" stroke="#9d174d"><circle cx="0" cy="-8" r="6"/><circle cx="8" cy="0" r="6"/><circle cx="0" cy="8" r="6"/><circle cx="-8" cy="0" r="6"/></g><circle r="5" fill="#facc15"/>', 34),
    'dot': ('<circle r="10" fill="#38bdf8" stroke="#0c4a6e"/>', 26),
    'egg': ('<ellipse rx="10" ry="13" fill="#fef3c7" stroke="#92400e"/>', 26),
    'car': ('<rect x="-15" y="-6" width="30" height="12" rx="3" fill="#ef4444" stroke="#7f1d1d"/><path d="M-9 -6 L-5 -13 H6 L10 -6" fill="#fecaca" stroke="#7f1d1d"/><circle cx="-8" cy="7" r="4" fill="#0f172a"/><circle cx="8" cy="7" r="4" fill="#0f172a"/>', 38),
    'fish': ('<path d="M-14 0 Q-2 -11 10 0 Q-2 11 -14 0 Z M10 0 L16 -7 V7 Z" fill="#f59e0b" stroke="#78350f"/>', 36),
    'bird': ('<ellipse rx="12" ry="8" fill="#60a5fa" stroke="#1e3a8a"/><circle cx="9" cy="-6" r="5" fill="#60a5fa" stroke="#1e3a8a"/><path d="M14 -6 L19 -4 L14 -3 Z" fill="#f59e0b"/>', 34),
    'banana': ('<path d="M-14 -6 Q0 14 14 -6 Q0 6 -14 -6 Z" fill="#fde047" stroke="#a16207"/>', 34),
    'mango': ('<ellipse rx="10" ry="13" fill="#facc15" stroke="#a16207" transform="rotate(20)"/>', 28),
    'tree': ('<rect x="-3" y="2" width="6" height="12" fill="#92400e"/><circle cy="-6" r="11" fill="#22c55e" stroke="#14532d"/>', 30),
    'sun': ('<g stroke="#f59e0b" stroke-width="2.5">' + ''.join(f'<line x1="0" y1="-10" x2="0" y2="-15" transform="rotate({a})"/>' for a in range(0, 360, 30)) + '</g><circle r="9" fill="#fbbf24" stroke="#d97706"/>', 34),
    'moon': ('<path d="M4 -13 A13 13 0 1 0 4 13 A10 10 0 1 1 4 -13 Z" fill="#fcd34d" stroke="#b45309"/>', 32),
    'mountain': ('<path d="M-15 12 L-3 -12 L3 -2 L7 -8 L15 12 Z" fill="#94a3b8" stroke="#475569"/><path d="M-3 -12 L-7 -4 L-1 -5 Z" fill="#f8fafc"/>', 34),
    'coin': ('<circle r="12" fill="#fbbf24" stroke="#92400e" stroke-width="1.5"/><circle r="8" fill="none" stroke="#92400e"/>', 30),
    'stick': ('<rect x="-2" y="-16" width="4" height="32" rx="2" fill="#d97706" stroke="#78350f"/>', 10),
    'orange': ('<circle r="13" fill="#fb923c" stroke="#9a3412"/><path d="M0 -13 q4 -7 10 -6 q-4 5 -10 6" fill="#16a34a" stroke="#14532d"/>', 32),
    'strawberry': ('<path d="M-11 -6 Q0 -10 11 -6 Q9 8 0 15 Q-9 8 -11 -6 Z" fill="#dc2626" stroke="#7f1d1d"/><path d="M-8 -7 L-3 -12 L0 -8 L3 -12 L8 -7" fill="#16a34a" stroke="#14532d"/><g fill="#fde68a"><circle cx="-4" cy="0" r="1"/><circle cx="4" cy="1" r="1"/><circle cx="0" cy="7" r="1"/></g>', 30),
    'icecream': ('<path d="M-8 -2 L0 18 L8 -2 Z" fill="#f59e0b" stroke="#78350f"/><circle cy="-7" r="9" fill="#f9a8d4" stroke="#9d174d"/>', 26),
    'sweet': ('<path d="M-16 -7 L-9 0 L-16 7 Z M16 -7 L9 0 L16 7 Z" fill="#f472b6" stroke="#9d174d"/><ellipse rx="10" ry="8" fill="#fb923c" stroke="#9d174d"/><path d="M-4 -7 V7 M4 -7 V7" stroke="#fde047" stroke-width="2"/>', 38),
    'cake': ('<rect x="-14" y="-6" width="28" height="16" rx="3" fill="#fbcfe8" stroke="#9d174d"/><ellipse cy="-6" rx="14" ry="5" fill="#fce7f3" stroke="#9d174d"/><line x1="-16" y1="12" x2="16" y2="12" stroke="#64748b" stroke-width="2"/>', 38),
    'bead': ('<circle r="9" fill="#92400e" stroke="#451a03"/><path d="M-5 -2 q5 -6 10 0" stroke="#fbbf24" fill="none" stroke-width="2"/>', 22),
    'block': ('<rect x="-12" y="-12" width="24" height="24" fill="#22c55e" stroke="#14532d" stroke-width="1.5"/><rect x="-8" y="-8" width="16" height="16" fill="#fff" stroke="#14532d"/>', 30),
    'bag': ('<rect x="-12" y="-10" width="24" height="26" rx="5" fill="#f87171" stroke="#7f1d1d"/><path d="M-6 -10 V-15 H6 V-10" fill="none" stroke="#1e3a8a" stroke-width="2"/><rect x="-8" y="2" width="16" height="9" rx="2" fill="#fca5a5" stroke="#7f1d1d"/>', 32),
    'tractor': ('<rect x="-16" y="-4" width="26" height="10" fill="#16a34a" stroke="#14532d"/><rect x="-4" y="-14" width="12" height="10" fill="#bbf7d0" stroke="#14532d"/><circle cx="-10" cy="8" r="8" fill="#0f172a"/><circle cx="12" cy="10" r="5" fill="#0f172a"/>', 40),
    'pomegranate': ('<circle r="12" fill="#b91c1c" stroke="#7f1d1d"/><path d="M-4 -12 L-3 -16 L0 -13 L3 -16 L4 -12" fill="#7f1d1d"/>', 30),
    'pizza': ('<circle r="13" fill="#fdba74" stroke="#9a3412"/><g fill="#dc2626"><circle cx="-5" cy="-4" r="2.5"/><circle cx="5" cy="-3" r="2.5"/><circle cx="0" cy="5" r="2.5"/><circle cx="-6" cy="5" r="2"/><circle cx="6" cy="6" r="2"/></g>', 32),
    'peach': ('<circle r="12" fill="#f97316" stroke="#9a3412"/><path d="M0 -12 q-6 -5 -11 -2 q6 3 11 2" fill="#16a34a"/>', 30),
    'pear': ('<path d="M0 -12 Q5 -12 5 -4 Q12 4 8 11 Q0 16 -8 11 Q-12 4 -5 -4 Q-5 -12 0 -12 Z" fill="#a3e635" stroke="#3f6212"/><path d="M0 -12 q4 -5 9 -4" stroke="#14532d" fill="none" stroke-width="2"/>', 28),
    'hockey': ('<path d="M10 -16 L-6 10 Q-9 15 -14 13" fill="none" stroke="#1f2937" stroke-width="4" stroke-linecap="round"/>', 30),
    'football': ('<circle r="13" fill="#fff" stroke="#0f172a"/><polygon points="0,-5 5,-1 3,5 -3,5 -5,-1" fill="#0f172a"/>', 32),
    'bat': ('<rect x="-4" y="-16" width="8" height="26" rx="3" fill="#d6b48a" stroke="#78350f" transform="rotate(-20)"/><rect x="-1.5" y="-24" width="3" height="9" fill="#475569" transform="rotate(-20)"/>', 26),
    'racket': ('<ellipse cy="-6" rx="9" ry="11" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/><rect x="-1.5" y="5" width="3" height="12" fill="#1d4ed8"/>', 26),
    'paddle': ('<circle cy="-4" r="10" fill="#ef4444" stroke="#7f1d1d"/><rect x="-2.5" y="5" width="5" height="11" fill="#b45309"/>', 26),
    'child': ('<circle cy="-10" r="6" fill="#fcd34d" stroke="#92400e"/><path d="M-7 -3 H7 L9 12 H-9 Z" fill="#60a5fa" stroke="#1e3a8a"/><path d="M-4 12 V17 M4 12 V17" stroke="#0f172a" stroke-width="2"/>', 24),
    'carpic': ('<path d="M-16 4 Q-15 -4 -8 -5 L-4 -11 H6 L11 -5 Q16 -4 16 4 Z" fill="#2563eb" stroke="#1e3a8a"/><circle cx="-9" cy="5" r="4" fill="#0f172a"/><circle cx="9" cy="5" r="4" fill="#0f172a"/>', 38),
    'deer': ('<ellipse cx="0" cy="2" rx="11" ry="6" fill="#a16207"/><path d="M-8 6 V16 M-3 6 V16 M4 6 V16 M9 6 V16" stroke="#713f12" stroke-width="2"/><path d="M9 -2 L13 -12 L17 -11 L14 -1 Z" fill="#a16207"/><path d="M13 -12 l-3 -6 M15 -12 l3 -6" stroke="#713f12"/>', 34),
    'elephant': ('<ellipse cx="0" cy="0" rx="14" ry="10" fill="#57534e"/><circle cx="13" cy="-4" r="7" fill="#57534e"/><path d="M18 -2 Q22 8 18 14" stroke="#57534e" stroke-width="4" fill="none"/><path d="M-9 8 V17 M-3 8 V17 M4 8 V17 M9 8 V17" stroke="#44403c" stroke-width="4"/>', 40),
    'monkey': ('<circle cy="-8" r="6" fill="#a16207"/><circle cy="-7" r="3.5" fill="#fde68a"/><ellipse cy="5" rx="7" ry="9" fill="#a16207"/><path d="M7 6 Q16 6 14 -4" stroke="#a16207" stroke-width="2" fill="none"/>', 30),
    'cheetah': ('<ellipse rx="13" ry="7" fill="#eab308"/><circle cx="13" cy="-4" r="5" fill="#eab308"/><g fill="#1c1917"><circle cx="-5" cy="-2" r="1.5"/><circle cx="2" cy="1" r="1.5"/><circle cx="-8" cy="3" r="1.5"/><circle cx="6" cy="-3" r="1.5"/></g><path d="M-9 5 V15 M-4 5 V15 M5 5 V15 M9 5 V15" stroke="#a16207" stroke-width="2.5"/>', 40),
    'cube': ('<rect x="-10" y="-10" width="20" height="20" fill="#60a5fa" stroke="#1e3a8a"/>', 22),
}


def icons(spec):
    """'pencil:7 | book:4 [@ PER_ROW]' -> rows of simple object icons (counting pictures); '@ 5' wraps after 5 objects."""
    spec, _, per = spec.partition('@')
    per = int(per) if per.strip() else 0
    groups = [(k.strip(), int(n)) for k, n in (p.split(':') for p in spec.split('|'))]
    out, x, y, w = [], 22, 30, 0
    for name, n in groups:
        shape, step = _ICON[name]
        for k in range(n):
            if per and k and k % per == 0:
                w, x, y = max(w, x), 22, y + 40
            out.append(f'<g transform="translate({x} {y})">{shape}</g>')
            x += step
        x += 28
    w = max(w, x)
    label = ', '.join(f'{n} {name}s' for name, n in groups)
    return f'<svg viewBox="0 0 {w} {y + 30}" width="{w}" role="img" aria-label="{escape(label)}">' + ''.join(out) + '</svg>'


def cross(spec):
    """'A,B,C | 4:3 | 2:5' -> Method II continued-ratio diagram (a1:b1, b2:c2 -> a1*b2 : b1*b2 : b1*c2)."""
    parts = [p.strip() for p in spec.split('|')]
    names = [n.strip() for n in parts[0].split(',')]
    a1, b1 = [x.strip() for x in parts[1].split(':')]
    b2, c2 = [x.strip() for x in parts[2].split(':')]
    r = [int(a1) * int(b2), int(b1) * int(b2), int(b1) * int(c2)]
    xs = [60, 165, 270]
    out = ['<defs><marker id="m6cr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#334155"/></marker></defs>']
    for x, n in zip(xs, names):
        out.append(f'<text x="{x}" y="20" text-anchor="middle" font-weight="700">{escape(n)}</text>')
    out += [f'<text x="{xs[0]}" y="56" text-anchor="middle">{a1}</text><text x="112" y="56">:</text><text x="{xs[1]}" y="56" text-anchor="middle">{b1}</text>',
            f'<text x="{xs[1]}" y="86" text-anchor="middle">{b2}</text><text x="217" y="86">:</text><text x="{xs[2]}" y="86" text-anchor="middle">{c2}</text>',
            f'<line x1="{xs[0] + 10}" y1="50" x2="{xs[1] - 10}" y2="80" stroke="#334155" marker-end="url(#m6cr)"/>',
            f'<line x1="{xs[1] + 9}" y1="78" x2="{xs[1] + 9}" y2="58" stroke="#334155" marker-end="url(#m6cr)"/>',
            f'<line x1="{xs[1] + 12}" y1="50" x2="{xs[2] - 10}" y2="80" stroke="#334155" marker-end="url(#m6cr)"/>',
            '<line x1="30" y1="100" x2="300" y2="100" stroke="#0f172a" stroke-width="1.4"/>',
            f'<text x="{xs[0]}" y="126" text-anchor="middle">{r[0]}</text><text x="112" y="126">:</text><text x="{xs[1]}" y="126" text-anchor="middle">{r[1]}</text><text x="217" y="126">:</text><text x="{xs[2]}" y="126" text-anchor="middle">{r[2]}</text>',
            '<line x1="30" y1="134" x2="300" y2="134" stroke="#0f172a" stroke-width="1.4"/>']
    label = f'Continued ratio by cross multiplication: {a1}:{b1} and {b2}:{c2} give {r[0]}:{r[1]}:{r[2]}'
    return f'<svg viewBox="0 0 330 145" width="330" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" font-size="17" fill="#0f172a">' + ''.join(out) + '</svg>'


def venn(spec):
    """Venn diagram. 'W H | E cx cy rx ry fill label lx ly | C cx cy r fill label lx ly | T x y text | ...'.
    The rectangle (universal set U) fills the whole box; 'U' label is drawn top-left."""
    parts = [p.strip() for p in spec.split('|')]
    W, H = [int(x) for x in parts[0].split()]
    out = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" fill="#fdba74" stroke="#9a3412" stroke-width="1.5"/>',
           f'<rect x="12" y="10" width="34" height="28" rx="3" fill="#fff" stroke="#334155"/><text x="29" y="30" text-anchor="middle" font-size="16">U</text>']
    labels = []
    for p in parts[1:]:
        f = p.split()
        if f[0] == 'E':
            cx, cy, rx, ry = [float(x) for x in f[1:5]]
            out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{f[5]}" stroke="#1e3a8a" stroke-width="1.5" fill-opacity=".9"/>')
            if len(f) > 6:
                out.append(f'<text x="{f[7]}" y="{f[8]}" text-anchor="middle" font-size="17" font-weight="700">{escape(f[6])}</text>')
                labels.append(f[6])
        elif f[0] == 'T':
            out.append(f'<text x="{f[1]}" y="{f[2]}" text-anchor="middle" font-size="15">{escape(" ".join(f[3:]))}</text>')
    label = 'Venn diagram in universal set U with sets ' + ', '.join(labels)
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def balance(spec):
    """Level balance. 'L groups | R groups' e.g. '2 3 | 5' or '2 3 2 | 5 2'; groups are counts of erasers,
    or 'x' for an unknown box. Equation label is drawn under the beam."""
    left, right = [s.split() for s in spec.split('|')]
    W, H = 420, 200
    out = [f'<rect x="202" y="40" width="16" height="120" fill="#a16207"/><path d="M160 180 h100 l-18 -20 h-64 z" fill="#a16207"/>',
           '<line x1="70" y1="40" x2="350" y2="40" stroke="#a16207" stroke-width="6" stroke-linecap="round"/>']
    for cx in (85, 335):
        out.append(f'<line x1="{cx}" y1="40" x2="{cx - 60}" y2="112" stroke="#94a3b8"/><line x1="{cx}" y1="40" x2="{cx + 60}" y2="112" stroke="#94a3b8"/>'
                   f'<path d="M{cx - 72} 112 h144 q-12 16 -72 16 q-60 0 -72 -16z" fill="#fde68a" stroke="#a16207"/>')

    def pan(groups, cx):
        widths = [26 if g == 'x' else int(g) * 9 for g in groups]
        total = sum(widths) + 8 * (len(groups) - 1)
        x = cx - total / 2
        s = []
        for g, w in zip(groups, widths):
            if g == 'x':
                s.append(f'<rect x="{x}" y="86" width="26" height="26" fill="#93c5fd" stroke="#1e3a8a"/><text x="{x + 13}" y="104" text-anchor="middle" font-size="15" font-style="italic" font-weight="700">x</text>')
            else:
                for i in range(int(g)):
                    s.append(f'<rect x="{x + i * 9}" y="96" width="8" height="16" rx="1" fill="#ef4444" stroke="#7f1d1d"/>')
            x += w + 8
        return ''.join(s)
    out.append(pan(left, 85) + pan(right, 335))
    fmt = lambda gs: ' + '.join(gs)
    label = f'{fmt(left)} = {fmt(right)}'
    out.append(f'<text x="210" y="196" text-anchor="middle" font-size="16" font-weight="700">{escape(label)}</text>')
    return (f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="Level balance: {escape(label)}" '
            f'font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>')


def tiles(spec):
    """Algebra tiles: 'LEFT = RIGHT' with tokens like x*1 +1*5 -1*5 on each side (counts after *)."""
    left, right = [s.split() for s in spec.split('=')]
    col = {'x': ('#7dd3fc', '#0c4a6e', 'x'), '+1': ('#22d3ee', '#155e75', '+1'), '-1': ('#f472b6', '#831843', '−1')}
    def side(tokens, x0):
        out, x, y = [], x0, 10
        for t in tokens:
            k, n = t.split('*')
            for i in range(int(n)):
                if x > x0 + 5 * 30:
                    x, y = x0, y + 30
                f, s, lab = col[k]
                out.append(f'<rect x="{x}" y="{y}" width="26" height="26" rx="3" fill="{f}" stroke="{s}"/>'
                           f'<text x="{x + 13}" y="{y + 18}" text-anchor="middle" font-size="{13 if k == "x" else 11}" font-style="{"italic" if k == "x" else "normal"}" font-weight="700">{lab}</text>')
                x += 30
            x, y = x0, y + 34
        return out, y
    lo, ly = side(left, 10)
    ro, ry = side(right, 230)
    H = max(ly, ry) + 4
    lab = ' + '.join(left) + ' = ' + ' + '.join(right)
    return (f'<svg viewBox="0 0 420 {H}" width="420" role="img" aria-label="Algebra tiles: {escape(lab)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">'
            + ''.join(lo + ro) + f'<text x="205" y="{H / 2 + 6}" text-anchor="middle" font-size="22" font-weight="700">=</text></svg>')


def _lbl(x, y, t, anchor='middle', size=14):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="600">{escape(t)}</text>' if t else ''


def rect(spec):
    """'W H fill | top | right | bottom | left | centre' (W, H are drawing proportions)."""
    p = [s.strip() for s in spec.split('|')] + [''] * 6
    w, h, fill = p[0].split()
    w, h = float(w), float(h)
    k = min(240 / w, 150 / h)
    W, H = w * k, h * k
    x0, y0 = 60, 30
    out = [f'<rect x="{x0}" y="{y0}" width="{W:.0f}" height="{H:.0f}" fill="{fill}" stroke="#1e293b" stroke-width="1.5"/>',
           _lbl(x0 + W / 2, y0 - 8, p[1]), _lbl(x0 + W + 6, y0 + H / 2 + 5, p[2], 'start'),
           _lbl(x0 + W / 2, y0 + H + 20, p[3]), _lbl(x0 - 6, y0 + H / 2 + 5, p[4], 'end'),
           _lbl(x0 + W / 2, y0 + H / 2 + 5, p[5])]
    VW, VH = x0 + W + 90, y0 + H + 30
    lab = ', '.join(t for t in p[1:6] if t)
    return (f'<svg viewBox="0 0 {VW:.0f} {VH:.0f}" width="{VW:.0f}" role="img" aria-label="Rectangle: {escape(lab)}" '
            f'font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>')


def path(spec):
    """Path around/inside a rectangle. 'W H d out|in | outer-top | outer-left | inner-top | inner-left | path-label'."""
    p = [s.strip() for s in spec.split('|')] + [''] * 6
    w, h, d, mode = p[0].split()
    w, h, d = float(w), float(h), float(d)
    k = min(260 / (w + 2 * d if mode == 'out' else w), 160 / (h + 2 * d if mode == 'out' else h))
    x0, y0 = 70, 30
    if mode == 'out':
        OW, OH, IW, IH, off = (w + 2 * d) * k, (h + 2 * d) * k, w * k, h * k, d * k
    else:
        OW, OH, IW, IH, off = w * k, h * k, (w - 2 * d) * k, (h - 2 * d) * k, d * k
    out = [f'<rect x="{x0}" y="{y0}" width="{OW:.0f}" height="{OH:.0f}" fill="#d6d3d1" stroke="#44403c" stroke-width="1.5"/>',
           f'<rect x="{x0 + off:.0f}" y="{y0 + off:.0f}" width="{IW:.0f}" height="{IH:.0f}" fill="#4ade80" stroke="#166534" stroke-width="1.5"/>',
           _lbl(x0 + OW / 2, y0 - 8, p[1]), _lbl(x0 - 6, y0 + OH / 2 + 5, p[2], 'end'),
           _lbl(x0 + OW / 2, y0 + off + 18, p[3], size=13), _lbl(x0 + off + 6, y0 + OH / 2 + 5, p[4], 'start', 13),
           _lbl(x0 + OW / 2, y0 + OH + 20, p[5], size=13)]
    VW, VH = x0 + OW + 30, y0 + OH + 30
    lab = ', '.join(t for t in p[1:6] if t)
    return (f'<svg viewBox="0 0 {VW:.0f} {VH:.0f}" width="{VW:.0f}" role="img" aria-label="Path {"around" if mode == "out" else "inside"} a rectangle: {escape(lab)}" '
            f'font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>')


def shape(spec):
    """'para|trap|tri [nest] | key=label ...' keys: base top alt oalt ibase itop ialt centre.
    nest draws a shaded path between an outer and an inner copy of the shape."""
    parts = [s.strip() for s in spec.split('|')]
    kind, *flags = parts[0].split()
    L = dict(p.split('=', 1) for p in parts[1:] if '=' in p)
    pts = {'para': [(60, 150), (120, 30), (330, 30), (270, 150)],
           'trap': [(60, 150), (140, 30), (250, 30), (330, 150)],
           'tri': [(60, 150), (195, 30), (330, 150)]}[kind]
    apex_x = pts[1][0]
    out = []
    poly = lambda P, f, s: f'<polygon points="{" ".join(f"{x:.0f},{y:.0f}" for x, y in P)}" fill="{f}" stroke="{s}" stroke-width="1.6"/>'
    if 'nest' in flags:
        cx = sum(x for x, _ in pts) / len(pts)
        cy = sum(y for _, y in pts) / len(pts) + (12 if kind == 'tri' else 0)
        inner = [(cx + (x - cx) * 0.72, cy + (y - cy) * 0.72) for x, y in pts]
        out.append(poly(pts, '#7dd3fc', '#0369a1'))
        out.append(poly(inner, '#ffffff', '#0369a1'))
        ix = inner[1][0]
        iy0, iy1 = inner[1][1], inner[0][1]
        out.append(f'<line x1="{ix:.0f}" y1="{iy0:.0f}" x2="{ix:.0f}" y2="{iy1:.0f}" stroke="#0f172a" stroke-width="1.3"/>')
        out.append(_lbl(ix + 6, (iy0 + iy1) / 2 + 5, L.get('ialt', ''), 'start', 13))
        out.append(_lbl((inner[0][0] + inner[-1][0]) / 2 + 40, iy1 - 6, L.get('ibase', ''), size=13))
        if kind != 'tri':
            out.append(_lbl((inner[1][0] + inner[2][0]) / 2, iy0 + 16, L.get('itop', ''), size=13))
        out.append(f'<line x1="40" y1="{pts[1][1]}" x2="40" y2="{pts[0][1]}" stroke="#334155" stroke-dasharray="3 3" marker-start="url(#shA)" marker-end="url(#shA)"/>')
        out.append(_lbl(34, (pts[1][1] + pts[0][1]) / 2 + 5, L.get('oalt', ''), 'end', 13))
    else:
        out.append(poly(pts, '#fff7ed' if kind != 'tri' else '#ecfeff', '#0f172a'))
        out.append(f'<line x1="{apex_x}" y1="{pts[1][1]}" x2="{apex_x}" y2="{pts[0][1]}" stroke="#0f172a" stroke-width="1.3"/>'
                   f'<path d="M{apex_x} {pts[0][1] - 8} h8 v8" fill="none" stroke="#0f172a"/>')
        out.append(_lbl(apex_x + 8, (pts[1][1] + pts[0][1]) / 2 + 5, L.get('alt', ''), 'start', 13))
    out.append(_lbl((pts[0][0] + pts[-1][0]) / 2, pts[0][1] + 20, L.get('base', '')))
    if kind != 'tri':
        out.append(_lbl((pts[1][0] + pts[2][0]) / 2, pts[1][1] - 8, L.get('top', '')))
    out.append(_lbl(195, 95, L.get('centre', '')))
    lab = ', '.join(f'{k} {v}' for k, v in L.items())
    name = {'para': 'Parallelogram', 'trap': 'Trapezium', 'tri': 'Triangle'}[kind]
    return (f'<svg viewBox="0 0 380 180" width="380" role="img" aria-label="{name}{" with a shaded path" if "nest" in flags else ""}: {escape(lab)}" '
            f'font-family="Segoe UI, Arial, sans-serif" fill="#0f172a"><defs><marker id="shA" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#334155"/></marker></defs>'
            + ''.join(out) + '</svg>')


_SOLID = {
    'pyramid': ('<polygon points="100,20 40,140 150,150" fill="#60a5fa" stroke="#1e3a8a"/><polygon points="100,20 40,140 20,120" fill="#1e40af" stroke="#1e3a8a"/>'
                '<path d="M20 120 L120 118 L150 150 M100 20 L120 118" fill="none" stroke="#1e3a8a" stroke-dasharray="4 3"/>',
                {'vertex': (100, 20), 'face': (105, 110), 'edge': (40, 140)}),
    'cone': ('<path d="M100 20 L45 140 A55 14 0 0 0 155 140 Z" fill="#e11d48" fill-opacity=".75" stroke="#881337"/>'
             '<ellipse cx="100" cy="140" rx="55" ry="14" fill="#fda4af" stroke="#881337"/>',
             {'vertex': (100, 20), 'curved': (115, 80), 'flat': (130, 142), 'edge': (60, 150)}),
    'cyl': ('<rect x="55" y="30" width="90" height="110" fill="#a5f3fc" stroke="#0e7490"/>'
            '<ellipse cx="100" cy="140" rx="45" ry="12" fill="#22d3ee" stroke="#0e7490"/>'
            '<ellipse cx="100" cy="30" rx="45" ry="12" fill="#22d3ee" stroke="#0e7490"/>',
            {'top': (130, 30), 'curved': (140, 85), 'bottom': (130, 142), 'edge': (60, 34), 'edge2': (60, 146)}),
    'cube': ('<polygon points="55,60 135,60 135,140 55,140" fill="#f5d0fe" stroke="#701a75"/>'
             '<polygon points="55,60 85,35 165,35 135,60" fill="#fae8ff" stroke="#701a75"/>'
             '<polygon points="135,60 165,35 165,115 135,140" fill="#e879f9" stroke="#701a75"/>',
             {'vertex': (55, 60), 'face': (95, 100), 'edge': (150, 48)}),
    'cuboid': ('<polygon points="30,70 150,70 150,135 30,135" fill="#fda4af" stroke="#9f1239"/>'
               '<polygon points="30,70 60,45 180,45 150,70" fill="#fecdd3" stroke="#9f1239"/>'
               '<polygon points="150,70 180,45 180,110 150,135" fill="#fb7185" stroke="#9f1239"/>',
               {'vertex': (30, 135), 'face': (90, 100), 'edge': (90, 45), 'length': (90, 152), 'width': (170, 128), 'height': (186, 82)}),
    'sphere': ('<defs><radialGradient id="sg{n}" cx=".35" cy=".35"><stop offset="0" stop-color="#fef08a"/><stop offset="1" stop-color="#b45309"/></radialGradient></defs>'
               '<circle cx="100" cy="85" r="55" fill="url(#sg{n})"/>',
               {'curved': (150, 85)}),
    'hemi': ('<path d="M45 70 A55 55 0 0 0 155 70 Z" fill="#e5e7eb" stroke="#374151"/>'
             '<ellipse cx="100" cy="70" rx="55" ry="12" fill="#f9fafb" stroke="#374151" stroke-dasharray="3 3"/><circle cx="100" cy="70" r="3"/>',
             {'circ': (150, 66), 'curved': (140, 110)}),
}
_SOLID_N = [0]


def solid(spec):
    """'cone|cyl|cube|cuboid|sphere|hemi | key=label ...' -> 3-D solid with labelled parts (arrows to the right side)."""
    parts = [s.strip() for s in spec.split('|')]
    kind = parts[0]
    labels = dict(p.split('=', 1) for p in parts[1:] if '=' in p)
    _SOLID_N[0] += 1
    body, anchors = _SOLID[kind]
    body = body.replace('{n}', str(_SOLID_N[0]))
    out = [body]
    ys = {}
    for k, text in labels.items():
        ax, ay = anchors[k]
        ty = ay
        while any(abs(ty - y) < 18 for y in ys.values()):
            ty += 18
        ys[k] = ty
        out.append(f'<line x1="{ax}" y1="{ay}" x2="212" y2="{ty - 4}" stroke="#334155"/>'
                   f'<text x="216" y="{ty}" font-size="13" font-weight="600">{escape(text)}</text>')
    H = max([170] + [y + 10 for y in ys.values()])
    W = 340 if labels else 210
    names = {'pyramid': 'Pyramid', 'cone': 'Cone', 'cyl': 'Cylinder', 'cube': 'Cube', 'cuboid': 'Cuboid', 'sphere': 'Sphere', 'hemi': 'Hemisphere'}
    lab = names[kind] + (': ' + ', '.join(labels.values()) if labels else '')
    return (f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="{escape(lab)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def reflect(spec):
    """'C R v|h K | x,y x,y ... | fill | show|dots|none' -> grid with mirror line x=K (v) or y=K (h),
    shape polygon in grid units; 'show' also draws the reflected image, 'dots' marks reflected vertices only."""
    parts = [s.strip() for s in spec.split('|')]
    C, R, ori, K = parts[0].split()
    C, R, K = int(C), int(R), float(K)
    pts = [tuple(float(v) for v in p.split(',')) for p in parts[1].split()]
    fill = parts[2] if len(parts) > 2 and parts[2] else '#f9a8d4'
    mode = parts[3] if len(parts) > 3 else 'none'
    s, ox, oy = 34, 14, 22
    X = lambda x: ox + x * s
    Y = lambda y: oy + y * s
    out = [f'<rect x="{ox}" y="{oy}" width="{C * s}" height="{R * s}" fill="#fff" stroke="#334155"/>']
    out += [f'<line x1="{X(i)}" y1="{oy}" x2="{X(i)}" y2="{Y(R)}" stroke="#94a3b8"/>' for i in range(1, C)]
    out += [f'<line x1="{ox}" y1="{Y(j)}" x2="{X(C)}" y2="{Y(j)}" stroke="#94a3b8"/>' for j in range(1, R)]
    poly = lambda P, f: f'<polygon points="{" ".join(f"{X(x):.0f},{Y(y):.0f}" for x, y in P)}" fill="{f}" stroke="#334155" stroke-width="1.4"/>'
    out.append(poly(pts, fill))
    ref = [(2 * K - x, y) if ori == 'v' else (x, 2 * K - y) for x, y in pts]
    if mode == 'show':
        out.append(poly(ref, fill))
    if mode in ('show', 'dots'):
        out += [f'<circle cx="{X(x):.0f}" cy="{Y(y):.0f}" r="3.5" fill="#0f172a"/>' for x, y in ref + pts]
    if ori == 'v':
        out.append(f'<line x1="{X(K)}" y1="{oy - 14}" x2="{X(K)}" y2="{Y(R) + 14}" stroke="#be123c" stroke-width="2" stroke-dasharray="6 4"/>')
    else:
        out.append(f'<line x1="{ox - 12}" y1="{Y(K)}" x2="{X(C) + 12}" y2="{Y(K)}" stroke="#be123c" stroke-width="2" stroke-dasharray="6 4"/>')
    W, H = X(C) + 16, Y(R) + 22
    lab = f'Shape on a {C} by {R} grid with a {"vertical" if ori == "v" else "horizontal"} line of reflection' + (', and its reflected image' if mode == 'show' else '')
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="{lab}">' + ''.join(out) + '</svg>'


def transv(spec):
    """Two parallel lines cut by a transversal.
    'P Q R S A B | ul ur ll lr | ul ur ll lr' -> line end labels (top line P..Q, bottom R..S, transversal A top, B bottom)
    and angle labels at the top and bottom crossings (use - for none)."""
    parts = [s.strip() for s in spec.split('|')]
    names = parts[0].split()
    top, bot = parts[1].split(), parts[2].split()
    y1, y2 = 60, 130
    x1, x2 = 200, 165
    dx = (x1 - x2) / (y2 - y1)
    xt = lambda y: x1 + (y1 - y) * dx
    out = ['<defs><marker id="tvA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z"/></marker></defs>']
    for y in (y1, y2):
        out.append(f'<line x1="40" y1="{y}" x2="320" y2="{y}" stroke="#0f172a" stroke-width="1.6" marker-start="url(#tvA)" marker-end="url(#tvA)"/>')
    out.append(f'<line x1="{xt(y2 + 55):.0f}" y1="{y2 + 55}" x2="{xt(y1 - 45):.0f}" y2="{y1 - 45}" stroke="#0f172a" stroke-width="1.6" marker-end="url(#tvA)"/>')
    for y, labs in ((y1, top), (y2, bot)):
        x = xt(y)
        out.append(f'<circle cx="{x:.0f}" cy="{y}" r="11" fill="none" stroke="#64748b"/>')
        for (ddx, ddy), t in zip(((-24, -8), (24, -8), (-26, 22), (22, 22)), labs):
            if t != '-':
                out.append(f'<text x="{x + ddx:.0f}" y="{y + ddy}" font-size="14" text-anchor="middle">{escape(t)}</text>')
    if len(names) >= 6:
        P, Q, R, S, A, B = [n if n != '-' else '' for n in names[:6]]
        out += [f'<text x="46" y="{y1 - 8}" font-size="15">{escape(P)}</text>', f'<text x="304" y="{y1 - 8}" font-size="15">{escape(Q)}</text>',
                f'<text x="46" y="{y2 - 8}" font-size="15">{escape(R)}</text>', f'<text x="304" y="{y2 - 8}" font-size="15">{escape(S)}</text>',
                f'<text x="{xt(y1 - 45) + 10:.0f}" y="{y1 - 38}" font-size="15">{escape(A)}</text>', f'<text x="{xt(y2 + 55) - 18:.0f}" y="{y2 + 52}" font-size="15">{escape(B)}</text>']
    nm = ''.join(names[:6]).replace('-', '')
    lab = (f'Parallel lines {names[0]}{names[1]} and {names[2]}{names[3]} cut by transversal {names[4]}{names[5]}' if len(nm) == 6 else 'Two parallel lines cut by a transversal') + '; angles at top crossing ' + ', '.join(top) + '; at bottom crossing ' + ', '.join(bot)
    return f'<svg viewBox="0 0 360 200" width="360" role="img" aria-label="{escape(lab)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def bisect(spec):
    """Perpendicular bisector construction of AB. 'stage [A B C D M]' stage 1: arcs from A; 2: + arcs from B meeting at C, D; 3: + line CD and midpoint."""
    p = spec.split()
    st = int(p[0])
    A, B, C, D, M = [x if x != '-' else '' for x in (p[1:6] + ['A', 'B', 'C', 'D', 'M'][len(p[1:6]):])]
    ax, bx, y = 60, 300, 120
    r = 150
    mx = (ax + bx) / 2
    dy = (r * r - (mx - ax) ** 2) ** 0.5
    out = [f'<line x1="{ax}" y1="{y}" x2="{bx}" y2="{y}" stroke="#0f172a" stroke-width="2"/>',
           f'<circle cx="{ax}" cy="{y}" r="3.5"/><circle cx="{bx}" cy="{y}" r="3.5"/>',
           f'<text x="{ax - 6}" y="{y + 22}">{A}</text><text x="{bx - 4}" y="{y + 22}">{B}</text>']
    import math

    def arc(cx, cy, ang):
        a1, a2 = math.radians(ang - 12), math.radians(ang + 12)
        x1, y1 = cx + r * math.cos(a1), cy - r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy - r * math.sin(a2)
        return f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 0 {x2:.1f} {y2:.1f}" fill="none" stroke="#2563eb" stroke-width="1.5"/>'
    ang = math.degrees(math.atan2(dy, mx - ax))
    out += [arc(ax, y, ang), arc(ax, y, -ang)]
    if st >= 2:
        out += [arc(bx, y, 180 - ang), arc(bx, y, 180 + ang)]
        out += [f'<text x="{mx + 6}" y="{y - dy - 6:.0f}">{C}</text><text x="{mx + 6}" y="{y + dy + 18:.0f}">{D}</text>']
    if st >= 3:
        out.append(f'<line x1="{mx}" y1="{y - dy - 10:.0f}" x2="{mx}" y2="{y + dy + 10:.0f}" stroke="#be123c" stroke-width="2"/>')
        out.append(f'<rect x="{mx}" y="{y - 12}" width="12" height="12" fill="none" stroke="#be123c"/><circle cx="{mx}" cy="{y}" r="3.5" fill="#be123c"/><text x="{mx - 20}" y="{y + 20}">{M}</text>')
    H = y + dy + 30
    lab = {1: f'Segment {A}{B} with arcs drawn from {A}', 2: f'Arcs from {A} and {B} crossing at {C} and {D}', 3: f'Line {C}{D} is the perpendicular bisector of {A}{B}, meeting it at {M}'}[st]
    return (f'<svg viewBox="0 {y - dy - 30:.0f} 360 {H - (y - dy - 30):.0f}" width="360" role="img" aria-label="{lab}" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="700" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def _arc(cx, cy, r, a0, a1, color='#2563eb'):
    import math
    x1, y1 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
    x2, y2 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    return f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 {large} 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="1.5"/>'


def _lab(x, y, t):
    return f'<text x="{x}" y="{y}">{escape(t)}</text>' if t and t != '-' else ''


def perpon(spec):
    """Perpendicular at a point O on line PQ. 'stage P Q O R S T U' (stage 0..4)."""
    import math
    p = spec.split()
    st = int(p[0])
    P, Q, O, R, S, T, U = (p[1:8] + ['P', 'Q', 'O', 'R', 'S', 'T', 'U'][len(p[1:8]):])
    y, ox, r1, r2 = 130, 180, 60, 95
    out = [f'<defs><marker id="po{st}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z"/></marker></defs>',
           f'<line x1="20" y1="{y}" x2="340" y2="{y}" stroke="#0f172a" stroke-width="1.8" marker-start="url(#po{st})" marker-end="url(#po{st})"/>',
           f'<circle cx="{ox}" cy="{y}" r="3.5"/>', _lab(28, y + 22, P), _lab(322, y + 22, Q), _lab(ox + 6, y - 8, O)]
    if st >= 1:
        out += [_arc(ox, y, r1, 160, 200), _arc(ox, y, r1, -20, 20), _lab(ox - r1 - 4, y + 22, R), _lab(ox + r1 - 4, y + 22, S)]
    h = (r2 * r2 - r1 * r1) ** 0.5
    ang = math.degrees(math.atan2(h, r1))
    if st >= 2:
        out.append(_arc(ox - r1, y, r2, ang - 12, ang + 12))
    if st >= 3:
        out += [_arc(ox + r1, y, r2, 180 - ang - 12, 180 - ang + 12), _lab(ox + 8, y - h - 6, T)]
    if st >= 4:
        out += [f'<line x1="{ox}" y1="{y - h - 20:.0f}" x2="{ox}" y2="{y + 70}" stroke="#be123c" stroke-width="2" marker-start="url(#po{st})" marker-end="url(#po{st})"/>',
                f'<rect x="{ox}" y="{y - 12}" width="12" height="12" fill="none" stroke="#be123c"/>', _lab(ox + 8, y + 66, U)]
    lab = ['Line ' + P + Q + ' with point ' + O, 'Arc from ' + O + ' cutting the line at ' + R + ' and ' + S, 'Arc from ' + R,
           'Arcs from ' + R + ' and ' + S + ' meeting at ' + T, T + U + ' is perpendicular to ' + P + Q + ' at ' + O][st]
    return (f'<svg viewBox="0 {y - h - 30:.0f} 360 {h + 120:.0f}" width="360" role="img" aria-label="{escape(lab)}" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="700" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def perpoff(spec):
    """Perpendicular from a point P not on line MN. 'stage M N P Q R S' (stage 0..3)."""
    import math
    p = spec.split()
    st = int(p[0])
    M, N, P, Q, R, S = (p[1:7] + ['M', 'N', 'P', 'Q', 'R', 'S'][len(p[1:7]):])
    y, px, py, r = 90, 180, 30, 85
    d = y - py
    half = (r * r - d * d) ** 0.5
    out = [f'<defs><marker id="pf{st}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z"/></marker></defs>',
           f'<line x1="20" y1="{y}" x2="340" y2="{y}" stroke="#0f172a" stroke-width="1.8" marker-start="url(#pf{st})" marker-end="url(#pf{st})"/>',
           f'<circle cx="{px}" cy="{py}" r="3.5"/>', _lab(28, y + 22, M), _lab(322, y + 22, N), _lab(px + 8, py - 4, P)]
    if st >= 1:
        a = math.degrees(math.atan2(d, half))
        out += [_arc(px, py, r, -a - 25, -180 + a + 25 + 360) if False else _arc(px, py, r, 180 + a - 8, 360 - a + 8),
                _lab(px - half - 14, y - 8, Q), _lab(px + half + 4, y - 8, R)]
    sy = y + (r * r - half * half) ** 0.5
    if st >= 2:
        b = math.degrees(math.atan2(sy - y, half))
        out += [_arc(px - half, y, r, -b - 10, -b + 10), _arc(px + half, y, r, 180 + b - 10, 180 + b + 10), _lab(px + 8, sy + 18, S)]
    if st >= 3:
        out += [f'<line x1="{px}" y1="{py - 15}" x2="{px}" y2="{sy + 12:.0f}" stroke="#be123c" stroke-width="2" marker-start="url(#pf{st})" marker-end="url(#pf{st})"/>',
                f'<rect x="{px}" y="{y - 12}" width="12" height="12" fill="none" stroke="#be123c"/>']
    lab = ['Line ' + M + N + ' and point ' + P + ' above it', 'Arc from ' + P + ' cutting ' + M + N + ' at ' + Q + ' and ' + R,
           'Arcs from ' + Q + ' and ' + R + ' meeting at ' + S + ' below the line', P + S + ' is perpendicular to ' + M + N][st]
    return (f'<svg viewBox="0 0 360 {sy + 40:.0f}" width="360" role="img" aria-label="{escape(lab)}" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="700" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def angcon(spec):
    """Compass construction of an angle. 'V B | arc AMAX | pts a:L ... | cross a:L:f ... | ray a:L | mark a:TEXT'
    V = vertex label, B = base ray label; main arc of radius r from 0 to AMAX degrees; pts = marked points on the
    main arc (with small crossing arcs); cross = intersection of bisecting arcs at angle a, distance f*r; ray = final ray."""
    import math
    parts = [s.strip() for s in spec.split('|')]
    V, B = (parts[0].split() + ['O', 'B'])[:2]
    opts = {}
    for p in parts[1:]:
        k, _, v = p.partition(' ')
        opts[k] = v.split()
    ox, oy, r = 110, 270, 100
    P = lambda a, d=r: (ox + d * math.cos(math.radians(a)), oy - d * math.sin(math.radians(a)))
    out = ['<defs><marker id="acA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z"/></marker></defs>',
           f'<line x1="{ox}" y1="{oy}" x2="{ox + 260}" y2="{oy}" stroke="#0f172a" stroke-width="1.8" marker-end="url(#acA)"/>',
           f'<circle cx="{ox}" cy="{oy}" r="3"/>', _lab(ox - 6, oy + 22, V), _lab(ox + 250, oy + 22, B)]
    if 'arc' in opts:
        amax = float(opts['arc'][0])
        out.append(_arc(ox, oy, r, -5, amax))
    for item in opts.get('pts', []):
        a, L = item.split(':')
        a = float(a)
        x, y = P(a)
        out.append(_arc(x - r * math.cos(math.radians(a - 60)) + 0, y + r * math.sin(math.radians(a - 60)), r, a - 60 + 180 - 12, a - 60 + 180 + 12) if False else '')
        # short crossing tick through the point, perpendicular-ish to the main arc
        tx, ty = math.cos(math.radians(a)), -math.sin(math.radians(a))
        out.append(f'<line x1="{x - 9 * tx - 7 * ty:.1f}" y1="{y - 9 * ty + 7 * tx:.1f}" x2="{x + 9 * tx + 7 * ty:.1f}" y2="{y + 9 * ty - 7 * tx:.1f}" stroke="#2563eb" stroke-width="1.5"/>')
        if a == 0:
            out.append(_lab(x - 4, oy + 22, L))
        else:
            out.append(_lab(x + 6 * tx - 14, y + 6 * ty - 6, L))
    for item in opts.get('cross', []):
        f = item.split(':')
        a, L = float(f[0]), f[1]
        d = float(f[2]) if len(f) > 2 else 1.6
        x, y = P(a, d * r)
        out.append(f'<path d="M{x - 12:.1f} {y - 8:.1f} Q{x:.1f} {y + 4:.1f} {x + 12:.1f} {y - 8:.1f} M{x - 12:.1f} {y + 8:.1f} Q{x:.1f} {y - 4:.1f} {x + 12:.1f} {y + 8:.1f}" fill="none" stroke="#2563eb" stroke-width="1.5"/>')
        out.append(_lab(x + 8, y - 10, L))
    for item in opts.get('ray', []):
        a, L = item.split(':')
        a = float(a)
        x, y = P(a, 2.3 * r)
        out.append(f'<line x1="{ox}" y1="{oy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#be123c" stroke-width="2" marker-end="url(#acA)"/>')
        out.append(_lab(x + 6, y + 4, L))
    if 'mark' in opts:
        a, T = opts['mark'][0].split(':', 1)
        a = float(a)
        out.append(_arc(ox, oy, 34, 0, a, '#0f172a'))
        if len(opts['mark']) > 1:
            x, y = P(a / 2, 50)
            out.append(f'<text x="{x:.0f}" y="{y + 5:.0f}" font-size="13">{escape(T)}</text>')
        else:
            x, y = P(a / 2, 50)
            out.append(f'<text x="{x:.0f}" y="{y + 5:.0f}" font-size="13">{escape(T)}</text>')
    lab = f'Compass construction at vertex {V} on ray {V}{B}' + (f'; final ray {opts["ray"][0].split(":")[1]} at {opts["ray"][0].split(":")[0]} degrees' if 'ray' in opts else '')
    left = -150 if any(float(x.split(':')[0]) > 100 for x in opts.get('ray', [])) else 0
    return (f'<svg viewBox="{left} 0 {400 - left} 305" width="{400 - left}" role="img" aria-label="{escape(lab)}" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="700" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def bisangle(spec):
    """'DEG [compass]' -> an angle of DEG° with its bisector and the two equal halves marked."""
    p = spec.split()
    a = float(p[0])
    h = a / 2
    hs = (f'{h:g}°')
    body = f'O B | arc {a + 15:g} | pts 0:- {a:g}:- | cross {h:g}:-:1.6 | ray {a:g}:A {h:g}:C'
    svg = angcon(body)
    import math
    ox, oy = 110, 270
    x, y = ox + 70 * math.cos(math.radians(h / 2)), oy - 70 * math.sin(math.radians(h / 2))
    x2, y2 = ox + 70 * math.cos(math.radians(h * 1.5)), oy - 70 * math.sin(math.radians(h * 1.5))
    extra = (_arc(ox, oy, 40, 0, a, '#0f172a') + f'<text x="{x:.0f}" y="{y:.0f}" font-size="12" fill="#be123c">{hs}</text>'
             f'<text x="{x2:.0f}" y="{y2:.0f}" font-size="12" fill="#be123c">{hs}</text>')
    svg = svg.replace('aria-label="', f'aria-label="Angle of {a:g} degrees bisected into two angles of {hs}; ', 1)
    return svg.replace('</svg>', extra + '</svg>')


_PAL = ['#0ea5e9', '#f97316', '#a855f7', '#22c55e', '#e11d48', '#eab308']


def chart(spec):
    """Grouped bar chart.
    'v|h | max STEP | title T | x XLABEL | y YLABEL | cats A,B,C | S1=1,2,3 | S2=4,5,6'  (series name before '=').
    v = vertical bars, h = horizontal bars."""
    parts = [s.strip() for s in spec.split('|')]
    ori = parts[0]
    o, series = {}, []
    for p in parts[1:]:
        k, _, v = p.partition(' ')
        if k in ('max', 'title', 'x', 'y', 'cats', 'colors'):
            o[k] = v.strip()
        else:
            name, _, vals = p.partition('=')
            series.append((name.strip(), [float(x) for x in vals.split(',')]))
    cats = [c.strip() for c in o['cats'].split(',')]
    vmax, step = [float(x) for x in o['max'].split()]
    cols = o['colors'].split(',') if 'colors' in o else _PAL
    ns, nc = len(series), len(cats)
    out = []
    if ori == 'v':
        L, T, W, H = 70, 40, max(320, nc * (ns * 22 + 26)), 230
        sx = lambda v: T + H - v / vmax * H
        n = int(round(vmax / step))
        for i in range(n + 1):
            v = i * step
            out.append(f'<line x1="{L}" y1="{sx(v):.1f}" x2="{L + W}" y2="{sx(v):.1f}" stroke="#e2e8f0"/><text x="{L - 6}" y="{sx(v) + 4:.1f}" text-anchor="end" font-size="11">{v:g}</text>')
        gw = W / nc
        bw = min(26, (gw - 14) / ns)
        for ci, c in enumerate(cats):
            gx = L + ci * gw + (gw - bw * ns) / 2
            for si, (nm, vals) in enumerate(series):
                v = vals[ci]
                fc = cols[ci % len(cols)] if (ns == 1 and 'colors' in o) else cols[si % len(cols)]
                out.append(f'<rect x="{gx + si * bw:.1f}" y="{sx(v):.1f}" width="{bw - 2:.1f}" height="{T + H - sx(v):.1f}" fill="{fc}"><title>{escape(nm)} – {escape(c)}: {v:g}</title></rect>')
            out.append(f'<text x="{L + ci * gw + gw / 2:.1f}" y="{T + H + 16}" text-anchor="middle" font-size="12">{escape(c)}</text>')
        out.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{T + H}" stroke="#0f172a" stroke-width="1.5"/><line x1="{L}" y1="{T + H}" x2="{L + W}" y2="{T + H}" stroke="#0f172a" stroke-width="1.5"/>')
        out.append(f'<text x="{L + W / 2}" y="{T + H + 36}" text-anchor="middle" font-size="13" font-weight="600">{escape(o.get("x", ""))}</text>')
        out.append(f'<text transform="translate(16 {T + H / 2}) rotate(-90)" text-anchor="middle" font-size="13" font-weight="600">{escape(o.get("y", ""))}</text>')
        VW, VH = L + W + 20, T + H + 50
    else:
        L, T, W = 110, 40, 380
        gh = max(26, ns * 18 + 10)
        H = nc * gh
        sx = lambda v: L + v / vmax * W
        n = int(round(vmax / step))
        for i in range(n + 1):
            v = i * step
            out.append(f'<line x1="{sx(v):.1f}" y1="{T}" x2="{sx(v):.1f}" y2="{T + H}" stroke="#e2e8f0"/><text x="{sx(v):.1f}" y="{T + H + 15}" text-anchor="middle" font-size="11">{v:g}</text>')
        bh = min(20, (gh - 8) / ns)
        for ci, c in enumerate(cats[::-1]):
            ci0 = nc - 1 - ci
            gy = T + ci * gh + (gh - bh * ns) / 2
            for si, (nm, vals) in enumerate(series):
                v = vals[ci0]
                fc = cols[ci0 % len(cols)] if (ns == 1 and 'colors' in o) else cols[si % len(cols)]
                out.append(f'<rect x="{L}" y="{gy + si * bh:.1f}" width="{sx(v) - L:.1f}" height="{bh - 2:.1f}" fill="{fc}"><title>{escape(nm)} – {escape(c)}: {v:g}</title></rect>')
            out.append(f'<text x="{L - 6}" y="{T + ci * gh + gh / 2 + 4:.1f}" text-anchor="end" font-size="12">{escape(c)}</text>')
        out.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{T + H}" stroke="#0f172a" stroke-width="1.5"/><line x1="{L}" y1="{T + H}" x2="{L + W}" y2="{T + H}" stroke="#0f172a" stroke-width="1.5"/>')
        out.append(f'<text x="{L + W / 2}" y="{T + H + 34}" text-anchor="middle" font-size="13" font-weight="600">{escape(o.get("x", ""))}</text>')
        out.append(f'<text transform="translate(14 {T + H / 2}) rotate(-90)" text-anchor="middle" font-size="13" font-weight="600">{escape(o.get("y", ""))}</text>')
        VW, VH = L + W + 20, T + H + 46
    if o.get('title'):
        out.append(f'<text x="{VW / 2}" y="16" text-anchor="middle" font-size="14" font-weight="700">{escape(o["title"])}</text>')
    if ns > 1 or series[0][0]:
        lx = VW - 10
        for si, (nm, _) in reversed(list(enumerate(series))):
            w = 22 + 7 * len(nm)
            lx -= w
            out.append(f'<rect x="{lx}" y="24" width="12" height="12" fill="{cols[si % len(cols)]}"/><text x="{lx + 16}" y="34" font-size="12">{escape(nm)}</text>')
    desc = '; '.join(f'{nm or "values"}: ' + ', '.join(f'{c} {v:g}' for c, v in zip(cats, vals)) for nm, vals in series)
    lab = f'{"Vertical" if ori == "v" else "Horizontal"} {"multiple " if ns > 1 else ""}bar graph{": " + o["title"] if o.get("title") else ""}. {desc}'
    return (f'<svg viewBox="0 0 {VW:.0f} {VH:.0f}" width="{VW:.0f}" role="img" aria-label="{escape(lab)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def pie(spec):
    """'Label=value; Label=value; ... [| deg] [| upto N] [| title T]' -> pie chart drawn anticlockwise from the right.
    deg: values are already angles. upto N: draw only the first N sectors (construction steps)."""
    import math
    parts = [s.strip() for s in spec.split('|')]
    items = [(a.strip(), float(b)) for a, b in (x.split('=') for x in parts[0].split(';') if x.strip())]
    flags = {p.split(' ', 1)[0]: (p.split(' ', 1)[1] if ' ' in p else '') for p in parts[1:]}
    total = sum(v for _, v in items)
    angs = [v if 'deg' in flags else v / total * 360 for _, v in items]
    upto = int(flags.get('upto', len(items)) or len(items))
    cx, cy, r = 170, 150, 115
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="#0f172a" stroke-width="1.5"/>']
    a0 = 0.0
    pal = ['#f9a8d4', '#a5f3fc', '#bbf7d0', '#fde68a', '#c4b5fd', '#fdba74', '#99f6e4', '#fecaca']
    for i, ((lab, v), a) in enumerate(zip(items, angs)):
        if i >= upto:
            break
        a1 = a0 + a
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
        large = 1 if a > 180 else 0
        out.append(f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 0 {x1:.1f} {y1:.1f} Z" fill="{pal[i % len(pal)]}" stroke="#0f172a" stroke-width="1.2"><title>{escape(lab)}: {a:g}°</title></path>')
        m = math.radians(a0 + a / 2)
        d = r * (0.58 if a > 40 else 0.72)
        tx, ty = cx + d * math.cos(m), cy - d * math.sin(m)
        fs = 12 if a >= 25 else 10
        deg = f'{a:.2f}'.rstrip('0').rstrip('.') + '°'
        out.append(f'<text x="{tx:.1f}" y="{ty - 2:.1f}" text-anchor="middle" font-size="{fs}" font-weight="600">{escape(lab)}</text>'
                   f'<text x="{tx:.1f}" y="{ty + 12:.1f}" text-anchor="middle" font-size="{fs}">{deg}</text>')
        a0 = a1
    out.append(f'<circle cx="{cx}" cy="{cy}" r="3"/>')
    H = 300
    if flags.get('title'):
        out.insert(0, f'<text x="{cx}" y="20" text-anchor="middle" font-size="14" font-weight="700">{escape(flags["title"])}</text>')
        out = [o.replace(f'cy="{cy}"', f'cy="{cy + 10}"') for o in out]
    desc = ', '.join(f'{lab} {a:.1f} degrees' for (lab, _), a in list(zip(items, angs))[:upto])
    return (f'<svg viewBox="0 0 340 {H}" width="340" role="img" aria-label="Pie chart: {escape(desc)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def spinner(spec):
    """'1 2 3 4 5 6 7 8' -> spinner with equal sectors labelled clockwise from the top, with an arrow."""
    import math
    labs = spec.split()
    n = len(labs)
    cx, cy, r = 110, 110, 95
    pal = ['#a78bfa', '#f9a8d4', '#fbcfe8', '#fef9c3', '#67e8f9', '#64748b', '#f9a8d4', '#22c55e', '#bae6fd', '#fda4af']
    out = []
    for i, lab in enumerate(labs):
        a0 = 90 - i * 360 / n
        a1 = a0 - 360 / n
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
        out.append(f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f} Z" fill="{pal[i % len(pal)]}" stroke="#0f172a"/>')
        m = math.radians((a0 + a1) / 2)
        out.append(f'<text x="{cx + 0.68 * r * math.cos(m):.1f}" y="{cy - 0.68 * r * math.sin(m) + 6:.1f}" text-anchor="middle" font-size="18" font-weight="700">{escape(lab)}</text>')
    out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 45}" y2="{cy - 25}" stroke="#be123c" stroke-width="3"/><circle cx="{cx}" cy="{cy}" r="5" fill="#be123c"/>')
    return (f'<svg viewBox="0 0 220 220" width="220" role="img" aria-label="Spinner with {n} equal parts labelled {", ".join(labs)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def ptree(spec):
    """'p | A, B, ...' -> one-level probability tree with probability p on each branch."""
    p, _, rest = spec.partition('|')
    labs = [x.strip() for x in rest.split(',')]
    n = len(labs)
    H = 50 + 60 * n
    out = []
    for i, lab in enumerate(labs):
        y = 30 + i * 60 + 10
        out.append(f'<line x1="20" y1="{H / 2}" x2="150" y2="{y}" stroke="#0f172a" stroke-width="1.5"/>'
                   f'<text x="160" y="{y + 5}" font-size="16" font-weight="700">{escape(lab)}</text>'
                   f'<text x="70" y="{(H / 2 + y) / 2 - 6:.0f}" font-size="14">{escape(p.strip())}</text>')
    out.append(f'<path d="M230 {30} q14 0 14 14 V{H / 2 - 8} l10 8 l-10 8 V{H - 44} q0 14 -14 14" fill="none" stroke="#0f172a"/>'
               f'<text x="262" y="{H / 2 - 4}" font-size="14" font-weight="700">sample space</text><text x="262" y="{H / 2 + 14}" font-size="13">all possible outcomes</text>')
    return (f'<svg viewBox="0 0 420 {H}" width="420" role="img" aria-label="Tree diagram: outcomes {", ".join(labs)}, each with probability {escape(p.strip())}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def hundred(spec):
    """Class 4: 1-100 chart. 'COLOUR=n,n,... ; COLOUR=n,...' highlights cells (empty spec = plain chart)."""
    marks = {}
    bycol = spec.strip().startswith('bycol')
    spec = spec.replace('bycol', '', 1) if bycol else spec
    for grp in [g.strip() for g in spec.split(';') if g.strip()]:
        col, _, nums = grp.partition('=')
        for n in nums.split(','):
            if n.strip():
                marks[int(n)] = col.strip()
    c = 36
    out = []
    for n in range(1, 101):
        r, k = divmod(n - 1, 10)
        if bycol:
            r, k = k, r
        x, y = 2 + k * c, 2 + r * c
        out.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{marks.get(n, "#fff")}" stroke="#334155"/>'
                   f'<text x="{x + c / 2}" y="{y + 23}" text-anchor="middle">{n}</text>')
    label = 'Hundred chart' + (' with highlighted numbers ' + ', '.join(str(n) for n in sorted(marks)) if marks else '')
    return (f'<svg viewBox="0 0 {10 * c + 4} {10 * c + 4}" width="{10 * c + 4}" role="img" aria-label="{escape(label)}" '
            f'font-family="sans-serif" font-size="14" fill="#0f172a">' + ''.join(out) + '</svg>')


def jumps(spec):
    """Class 4: number pattern with curved jumps. 'TERMS | STEP' e.g. '30,27,24,21,18,15,12 | -3' (terms may be '?')."""
    terms, _, step = spec.partition('|')
    terms = [t.strip() for t in terms.split(',')]
    step = step.strip()
    gap = 72
    w = 30 + gap * (len(terms) - 1) + 30
    out = []
    for i, t in enumerate(terms):
        x = 30 + i * gap
        out.append(f'<text x="{x}" y="22" fill="#0f172a">{escape(t)}</text>')
        if i:
            px = x - gap
            out.append(f'<path d="M{px + 2} 34 Q{px + gap / 2} 90 {x - 2} 34" fill="none" stroke="#1d4ed8" stroke-width="2"/>'
                       f'<text x="{px + gap / 2}" y="100" fill="#1d4ed8" font-size="14">{escape(step)}</text>')
    label = 'Pattern ' + ', '.join(terms) + ' with jumps of ' + step
    return (f'<svg viewBox="0 0 {w} 110" width="{w}" role="img" aria-label="{escape(label)}" font-family="sans-serif" '
            f'font-size="16" text-anchor="middle">' + ''.join(out) + '</svg>')


def rowsof(spec):
    """Class 4: objects arranged in equal rows. 'R C [colour]' -> R rows of C objects, each row ringed."""
    p = spec.split()
    r, c, col = int(p[0]), int(p[1]), (p[2] if len(p) > 2 else '#1e40af')
    s, gap = 26, 10
    w = c * (s + gap) + 30
    h = r * (s + 22) + 10
    out = []
    for i in range(r):
        y = 8 + i * (s + 22)
        out.append(f'<rect x="4" y="{y}" width="{w - 8}" height="{s + 12}" rx="{(s + 12) / 2}" fill="none" stroke="#be185d" stroke-width="2"/>')
        for k in range(c):
            x = 15 + k * (s + gap)
            out.append(f'<rect x="{x}" y="{y + 6}" width="{s}" height="{s}" rx="4" fill="{col}"/><circle cx="{x + s / 2}" cy="{y + 6 + s / 2}" r="5" fill="#93c5fd"/>')
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="{r} rows of {c}">' + ''.join(out) + '</svg>')


def flower(spec):
    """Class 4: multiplication flower. 'N [petal colour]' -> centre 'N×', inner ring 1-10, petals N×1 ... N×10."""
    import math
    p = spec.split()
    n, col = int(p[0]), (p[1] if len(p) > 1 else '#ef4444')
    blank = 'blank' in p   # Class 3 exercise: only the first petal (n x 1) is filled in
    cx = cy = 130
    out = []
    for k in range(10):
        a = math.radians(-90 + 36 * k + 18)
        px, py = cx + 92 * math.cos(a), cy + 92 * math.sin(a)
        out.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="30" ry="24" transform="rotate({36 * k + 18} {px:.1f} {py:.1f})" fill="{col}" stroke="#7f1d1d" stroke-width="1"/>'
                   f'<text x="{px:.1f}" y="{py + 6:.1f}" font-size="18" font-weight="bold" fill="#fff">{"" if blank and k else n * (k + 1)}</text>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="#fde047" stroke="#ca8a04"/>')
    for k in range(10):
        a = math.radians(-90 + 36 * k + 18)
        out.append(f'<text x="{cx + 44 * math.cos(a):.1f}" y="{cy + 44 * math.sin(a) + 5:.1f}" font-size="13" fill="#0f172a">{k + 1}</text>')
    out.append(f'<text x="{cx}" y="{cy + 10}" font-size="28" fill="#0f172a">{n}×</text>')
    return (f'<svg viewBox="0 0 260 260" width="260" role="img" aria-label="Multiplication flower of {n}: '
            + ('petals to fill in for ' + str(n) + ' times 1 to 10' if blank else ', '.join(str(n * k) for k in range(1, 11))) + '" font-family="sans-serif" text-anchor="middle">' + ''.join(out) + '</svg>')


def fpie(spec):
    """Class 4: fraction circle. 'N K [colour] [| label]' -> circle cut into N equal sectors, K shaded (from 12 o'clock, clockwise).
    N may be 'h4' / 'v2' style for straight cuts? No: always sectors. Label (e.g. 3/4) is drawn under the circle as a fraction."""
    import math
    body, _, lab = spec.partition('|')
    p = body.split()
    n, col = int(p[0]), (p[2] if len(p) > 2 else '#a78bfa')
    # Class 3: K may also be a comma list of 1-based sectors (sector 1 starts at 12 o'clock, clockwise)
    shade = {int(x) - 1 for x in p[1].split(',')} if ',' in p[1] else set(range(int(p[1])))
    k = len(shade)
    r, cx, cy = 50, 60, 58
    out = []
    for i in range(n):
        a0, a1 = math.radians(-90 + 360 * i / n), math.radians(-90 + 360 * (i + 1) / n)
        x0, y0, x1, y1 = cx + r * math.cos(a0), cy + r * math.sin(a0), cx + r * math.cos(a1), cy + r * math.sin(a1)
        big = 1 if 360 / n > 180 else 0
        d = f'M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z' if n > 1 else f'M{cx - r} {cy} a{r} {r} 0 1 0 {2 * r} 0 a{r} {r} 0 1 0 {-2 * r} 0'
        out.append(f'<path d="{d}" fill="{col if i in shade else "#fff"}" stroke="#0f172a" stroke-width="1.5"/>')
    h = 116
    lab = lab.strip()
    if lab and '/' not in lab:
        out.append(f'<text x="{cx}" y="140" text-anchor="middle" font-size="16">{escape(lab)}</text>')
        h = 150
    elif lab:
        num, _, den = lab.partition('/')
        out.append(f'<text x="{cx}" y="134" text-anchor="middle" font-size="16">{escape(num)}</text><line x1="{cx - 10}" y1="140" x2="{cx + 10}" y2="140" stroke="#0f172a"/><text x="{cx}" y="157" text-anchor="middle" font-size="16">{escape(den)}</text>')
        h = 162
    return (f'<svg viewBox="0 0 120 {h}" width="120" role="img" aria-label="Circle in {n} equal parts with {k} shaded'
            + (f', {escape(lab)}' if lab else '') + '" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>')


def frow(spec):
    """Class 4: several fraction figures in one row. 'fpie 4 3 #a78bfa | 3/4 ;; fpie 4 1 #7dd3fc | 1/4' (any generators, ';;'-separated)."""
    parts = [x.strip() for x in spec.split(';;') if x.strip()]
    svgs = []
    for part in parts:
        kind, _, arg = part.partition(' ')
        svgs.append(globals()[kind](arg))
    return '<div style="display:flex;flex-wrap:wrap;gap:24px;justify-content:center;align-items:flex-end">' + ''.join(svgs) + '</div>'


def fgrid(spec):
    """Class 4: rectangle cut into R x C equal cells. 'R C SHADE [colour] [| label]'; SHADE = count (first cells,
    row by row) or a comma list of 1-based cell numbers (row-major), e.g. '3 3 1,2,4,5 #7dd3fc | 4/9'."""
    body, _, lab = spec.partition('|')
    p = body.split()
    r, c, sh, col = int(p[0]), int(p[1]), p[2], (p[3] if len(p) > 3 else '#7dd3fc')
    cells = set(int(x) for x in sh.split(',')) if ',' in sh else set(range(1, int(sh) + 1))
    W, H = 120, 120
    cw, chh = W / c, H / r
    out = []
    for i in range(r):
        for k in range(c):
            n = i * c + k + 1
            out.append(f'<rect x="{2 + k * cw:.1f}" y="{2 + i * chh:.1f}" width="{cw:.1f}" height="{chh:.1f}" fill="{col if n in cells else "#fff"}" stroke="#0f172a" stroke-width="1.5"/>')
    h = H + 6
    lab = lab.strip()
    if lab and '/' not in lab:
        out.append(f'<text x="{W / 2 + 2}" y="{H + 26}" text-anchor="middle" font-size="16">{escape(lab)}</text>')
        h = H + 36
    elif lab:
        num, _, den = lab.partition('/')
        x = W / 2 + 2
        out.append(f'<text x="{x}" y="{H + 24}" text-anchor="middle" font-size="16">{escape(num)}</text><line x1="{x - 10}" y1="{H + 30}" x2="{x + 10}" y2="{H + 30}" stroke="#0f172a"/><text x="{x}" y="{H + 47}" text-anchor="middle" font-size="16">{escape(den)}</text>')
        h = H + 52
    return (f'<svg viewBox="0 0 {W + 4} {h}" width="{W + 4}" role="img" aria-label="Shape in {r * c} equal parts with {len(cells)} shaded'
            + (f', {escape(lab)}' if lab else '') + '" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>')


def fxsq(spec):
    """Class 4: square cut by both diagonals into 4 triangles. 'SHADE [colour] [| label]'; SHADE = letters of shaded
    triangles t (top), r (right), b (bottom), l (left), e.g. 'r #2563eb | 1/4' or 'trbl'."""
    body, _, lab = spec.partition('|')
    p = body.split()
    sh, col = p[0], (p[1] if len(p) > 1 else '#2563eb')
    s = 120
    tri = {'t': f'2,2 {s + 2},2 {s / 2 + 2},{s / 2 + 2}', 'r': f'{s + 2},2 {s + 2},{s + 2} {s / 2 + 2},{s / 2 + 2}',
           'b': f'2,{s + 2} {s + 2},{s + 2} {s / 2 + 2},{s / 2 + 2}', 'l': f'2,2 2,{s + 2} {s / 2 + 2},{s / 2 + 2}'}
    out = [f'<polygon points="{pts}" fill="{col if k in sh else "#fff"}" stroke="#0f172a" stroke-width="1.5"/>' for k, pts in tri.items()]
    h = s + 6
    lab = lab.strip()
    if lab and '/' not in lab:
        out.append(f'<text x="{s / 2 + 2}" y="{s + 26}" text-anchor="middle" font-size="16">{escape(lab)}</text>')
        h = s + 36
    elif lab:
        num, _, den = lab.partition('/')
        x = s / 2 + 2
        out.append(f'<text x="{x}" y="{s + 24}" text-anchor="middle" font-size="16">{escape(num)}</text><line x1="{x - 10}" y1="{s + 30}" x2="{x + 10}" y2="{s + 30}" stroke="#0f172a"/><text x="{x}" y="{s + 47}" text-anchor="middle" font-size="16">{escape(den)}</text>')
        h = s + 52
    n = len([k for k in 'trbl' if k in sh])
    return (f'<svg viewBox="0 0 {s + 4} {h}" width="{s + 4}" role="img" aria-label="Square cut into 4 equal triangles with {n} shaded'
            + (f', {escape(lab)}' if lab else '') + '" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>')


def ftext(spec):
    """Class 4: a symbol or short text between figures in a frow, e.g. 'ftext +'."""
    return f'<svg viewBox="0 0 30 120" width="30" font-family="sans-serif" font-size="22" fill="#0f172a"><text x="15" y="66" text-anchor="middle">{escape(spec.strip())}</text></svg>'


ROMAN = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11: 'XI', 12: 'XII'}


def clock(spec):
    """Class 4: analogue clock. 'H:M[:S] [| caption]' -> clock face with hour, minute (and red second) hands."""
    import math
    body, _, cap = spec.partition('|')
    roman = body.strip().startswith('R ')   # Class 3: 'R H:M' -> dial with Roman numerals
    if roman:
        body = body.strip()[2:]
    blank = body.strip() == '-'
    parts = [0, 0] if blank else [int(x) for x in body.strip().split(':')]
    h, m, s = (parts + [None, None])[:3]
    cx = cy = 80
    r = 70
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r + 6}" fill="#dc2626"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff"/>']
    big, small = [], []
    for k in range(60):
        a = math.radians(k * 6 - 90)
        r0 = r - (9 if k % 5 == 0 else 4)
        (big if k % 5 == 0 else small).append(f'M{cx + r0 * math.cos(a):.0f} {cy + r0 * math.sin(a):.0f}L{cx + r * math.cos(a):.0f} {cy + r * math.sin(a):.0f}')
    out.append(f'<path d="{"".join(small)}" stroke="#0f172a"/><path d="{"".join(big)}" stroke="#0f172a" stroke-width="2"/>')
    out.append('<g text-anchor="middle" font-size="13" font-weight="bold">' + ''.join(
        f'<text x="{cx + (r - 20) * math.cos(math.radians(n * 30 - 90)):.0f}" y="{cy + (r - 20) * math.sin(math.radians(n * 30 - 90)) + 5:.0f}">{ROMAN[n] if roman else n}</text>' for n in range(1, 13)) + '</g>')
    def hand(deg, length, width, col):
        a = math.radians(deg - 90)
        return f'<line x1="{cx}" y1="{cy}" x2="{cx + length * math.cos(a):.1f}" y2="{cy + length * math.sin(a):.1f}" stroke="{col}" stroke-width="{width}" stroke-linecap="round"/>'
    if not blank:
        out.append(hand((h % 12) * 30 + m * 0.5, r * 0.5, 5, '#0f172a'))
        out.append(hand(m * 6, r * 0.78, 3, '#0f172a'))
    if s is not None and not blank:
        out.append(hand(s * 6, r * 0.85, 1.5, '#dc2626'))
    out.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#dc2626"/>')
    hgt, W, dx = 2 * cy, 2 * cx, 0
    if cap.strip():
        W = max(W, int(len(cap.strip()) * 7) + 10)
        dx = (W - 2 * cx) / 2
        out.append(f'<text x="{cx}" y="{2 * cy + 18}" text-anchor="middle" font-size="13">{escape(cap.strip())}</text>')
        hgt += 26
    label = 'Clock face without hands' if blank else f'Clock showing {h}:{m:02}' + (f':{s:02}' if s is not None else '')
    return (f'<svg viewBox="{-dx} 0 {W} {hgt}" width="{W}" role="img" aria-label="{label}" font-family="sans-serif" fill="#0f172a">'
            + ''.join(out) + '</svg>')


def digital(spec):
    """Class 4: digital clock. 'TEXT [| am/pm]' e.g. '11:09:45 | a.m'."""
    t, _, ap = spec.partition('|')
    t, ap = t.strip(), ap.strip()
    w = 30 + len(t) * 20
    out = [f'<rect x="2" y="2" width="{w}" height="70" rx="12" fill="#fecaca" stroke="#b91c1c" stroke-width="3"/>',
           f'<rect x="12" y="12" width="{w - 20}" height="50" rx="6" fill="#0f172a"/>',
           f'<text x="{w - 10}" y="{30 if ap else 52}" text-anchor="end" font-size="13" fill="#e2e8f0">{escape(ap)}</text>' if ap else '',
           f'<text x="{(w + 4) / 2}" y="{55 if ap else 47}" text-anchor="middle" font-size="26" font-family="Consolas, monospace" fill="#a5f3fc">{escape(t)}</text>']
    return f'<svg viewBox="0 0 {w + 4} 74" width="{w + 4}" role="img" aria-label="Digital clock showing {escape(t)} {escape(ap)}" font-family="sans-serif">' + ''.join(out) + '</svg>'


def timeline24(spec):
    """Class 4: 12-hour vs 24-hour clock strip for one day (no arguments)."""
    cw = 26
    out = []
    for hr in range(24):
        x = 70 + hr * cw
        col = '#1e1b4b' if hr < 5 or hr >= 20 else ('#4d7c0f' if hr < 7 or hr >= 18 else '#facc15')
        out.append(f'<rect x="{x}" y="40" width="{cw}" height="18" fill="{col}" stroke="#fff" stroke-width="0.5"/>')
        out.append(f'<text x="{x + cw / 2}" y="34" text-anchor="middle" font-size="11">{hr % 12 if hr % 12 else (0 if hr == 0 else 12)}</text>')
        out.append(f'<text x="{x + cw / 2}" y="75" text-anchor="end" font-size="10" transform="rotate(-90 {x + cw / 2} 75)">{hr:02} 00</text>')
    out.append(f'<text x="{70 + 24 * cw}" y="34" text-anchor="middle" font-size="11">12</text>')
    out.append('<text x="2" y="34" font-size="11">12-hour</text><text x="2" y="100" font-size="11">24-hour</text>')
    out.append(f'<text x="{70 + 3 * cw}" y="14" font-size="11">am</text><text x="{70 + 12 * cw}" y="14" text-anchor="middle" font-size="11">noon</text><text x="{70 + 17 * cw}" y="14" font-size="11">pm</text>')
    out.append(f'<text x="70" y="14" font-size="11">midnight</text><text x="{70 + 24 * cw}" y="14" text-anchor="end" font-size="11">midnight</text>')
    return f'<svg viewBox="0 0 {80 + 24 * cw} 112" width="{80 + 24 * cw}" role="img" aria-label="Hours of a day on the 12-hour and 24-hour clocks" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def geo(spec):
    """Class 4 geometry sketch. 'W H ; item ; item ...' with items:
      L x1 y1 x2 y2 [colour] [both|end|none]   line / ray / double-arrow line (default both = line with 2 arrows)
      S x1 y1 x2 y2 [colour]                   plain segment
      P x y label [dx dy]                      text label (default offset 0)
      D x y [r]                                 dot
      A cx cy r a0 a1 [label]                  angle arc (degrees, 0 = right, counter-clockwise)
      R x y                                     small right-angle square at x,y (size 12, towards +x,-y)
      C cx cy r [fill]                          circle
      G x y w h [fill]                          rectangle"""
    import math
    items = [x.strip() for x in spec.split(';')]
    W, H = [float(v) for v in items[0].split()[:2]]
    out = ['<defs><marker id="ga" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0 L8 4 L0 8z" fill="context-stroke"/></marker></defs>']
    for it in items[1:]:
        if not it:
            continue
        p = it.split()
        k = p[0]
        if k == 'L':
            x1, y1, x2, y2 = map(float, p[1:5])
            col = p[5] if len(p) > 5 and p[5].startswith('#') else '#dc2626'
            mode = p[-1] if p[-1] in ('both', 'end', 'none') else 'both'
            ms = ' marker-start="url(#ga)"' if mode == 'both' else ''
            me = '' if mode == 'none' else ' marker-end="url(#ga)"'
            out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="2"{ms}{me}/>')
        elif k == 'S':
            x1, y1, x2, y2 = map(float, p[1:5])
            col = p[5] if len(p) > 5 else '#0f172a'
            out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="2"/>')
        elif k == 'P':
            x, y = float(p[1]), float(p[2])
            out.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="15">{escape(p[3].replace("_", " "))}</text>')
        elif k == 'D':
            r = p[3] if len(p) > 3 else '3.5'
            out.append(f'<circle cx="{p[1]}" cy="{p[2]}" r="{r}" fill="#0f172a"/>')
        elif k == 'A':
            cx, cy, r, a0, a1 = map(float, p[1:6])
            x0, y0 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
            x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
            big = 1 if (a1 - a0) % 360 > 180 else 0
            out.append(f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 0 {x1:.1f} {y1:.1f}" fill="none" stroke="#2563eb" stroke-width="1.8"/>')
            if len(p) > 6:
                am = math.radians((a0 + a1) / 2)
                out.append(f'<text x="{cx + (r + 16) * math.cos(am):.1f}" y="{cy - (r + 16) * math.sin(am) + 5:.1f}" text-anchor="middle" font-size="14" fill="#1d4ed8">{escape(p[6].replace("_", " "))}</text>')
        elif k == 'R':
            x, y = float(p[1]), float(p[2])
            out.append(f'<path d="M{x + 12} {y} V{y - 12} H{x}" fill="none" stroke="#2563eb" stroke-width="1.5"/>')
        elif k == 'C':
            fill = p[4] if len(p) > 4 else 'none'
            out.append(f'<circle cx="{p[1]}" cy="{p[2]}" r="{p[3]}" fill="{fill}" stroke="#0f172a" stroke-width="2"/>')
        elif k == 'G':
            fill = p[5] if len(p) > 5 else 'none'
            out.append(f'<rect x="{p[1]}" y="{p[2]}" width="{p[3]}" height="{p[4]}" fill="{fill}" stroke="#0f172a" stroke-width="2"/>')
        else:
            raise ValueError('geo: unknown item ' + k)
    return f'<svg viewBox="0 0 {W:g} {H:g}" width="{W:g}" role="img" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def protractor(spec):
    """Class 4: protractor with outer scale (0 at left) and inner scale (0 at right).
    'protractor [DEG [ENDLABEL [BASELABEL]]] [| parts]' -> optional ray from O at DEG (measured from the right baseline);
    'parts' adds the labels baseline / centre point / inner scale / outer scale."""
    import math
    body, _, extra = spec.partition('|')
    p = body.split()
    cx, cy, R = 200, 200, 170
    out = [f'<path d="M{cx - R} {cy} A{R} {R} 0 0 1 {cx + R} {cy} Z" fill="#fdf2f8" stroke="#0f172a" stroke-width="1.5"/>',
           f'<path d="M{cx - R + 18} {cy} A{R - 18} {R - 18} 0 0 1 {cx + R - 18} {cy}" fill="none" stroke="#86efac" stroke-width="12"/>',
           f'<path d="M{cx - R + 34} {cy} A{R - 34} {R - 34} 0 0 1 {cx + R - 34} {cy}" fill="none" stroke="#f9a8d4" stroke-width="12"/>']
    ticks = []
    for d in range(0, 181):
        a = math.radians(180 - d)
        ln = 10 if d % 10 == 0 else (6 if d % 5 == 0 else 3)
        ticks.append(f'M{cx + R * math.cos(a):.1f} {cy - R * math.sin(a):.1f}L{cx + (R - ln) * math.cos(a):.1f} {cy - (R - ln) * math.sin(a):.1f}')
    out.append(f'<path d="{"".join(ticks)}" stroke="#0f172a" stroke-width="0.8"/>')
    lab = []
    for d in range(0, 181, 10):
        a = math.radians(180 - d)
        lab.append(f'<text x="{cx + (R - 18) * math.cos(a):.1f}" y="{cy - (R - 18) * math.sin(a) + 3:.1f}" font-size="9">{d}</text>')
        lab.append(f'<text x="{cx + (R - 34) * math.cos(a):.1f}" y="{cy - (R - 34) * math.sin(a) + 3:.1f}" font-size="9" fill="#9d174d">{180 - d}</text>')
        if d % 30 == 0:
            out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + (R - 42) * math.cos(a):.1f}" y2="{cy - (R - 42) * math.sin(a):.1f}" stroke="#cbd5e1" stroke-width="0.8"/>')
    out.append('<g text-anchor="middle">' + ''.join(lab) + '</g>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="#1d4ed8"/><text x="{cx}" y="{cy + 18}" text-anchor="middle" font-size="14">O</text>')
    W, H = 2 * cx, cy + 26
    if p:
        deg = float(p[0])
        a = math.radians(deg)
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + R + 20}" y2="{cy}" stroke="#1d4ed8" stroke-width="2"/>')
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + (R + 10) * math.cos(a):.1f}" y2="{cy - (R + 10) * math.sin(a):.1f}" stroke="#1d4ed8" stroke-width="2"/>')
        if len(p) > 1:
            out.append(f'<text x="{cx + (R + 22) * math.cos(a):.1f}" y="{cy - (R + 22) * math.sin(a) + 5:.1f}" text-anchor="middle" font-size="14">{escape(p[1])}</text>')
        if len(p) > 2:
            out.append(f'<text x="{cx + R + 14}" y="{cy + 18}" text-anchor="middle" font-size="14">{escape(p[2])}</text>')
    if extra.strip() == 'parts':
        out.append(f'<text x="{cx - R + 10}" y="{cy + 40}" font-size="12">baseline</text><text x="{cx}" y="{cy + 56}" text-anchor="middle" font-size="12">centre point</text>'
                   f'<text x="{cx + 60}" y="{cy + 40}" font-size="12" fill="#9d174d">inner scale (right to left)</text><text x="{cx - R}" y="14" font-size="12">outer scale (left to right)</text>')
        H = cy + 62
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="Protractor" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def sqgrid(spec):
    """Class 4: square grid with outlined/shaded shapes. 'COLS ROWS [cell] ; rect c r w h [colour] [fill] ; poly c,r c,r ... [colour] [fill] ;
    fillcells COLOUR c,r c,r ... ; label c r TEXT ; mirror v|h K' (c, r = grid coordinates from the top-left corner, 0-based).
    Shapes are drawn along grid lines; 'mirror' draws a dashed line of symmetry."""
    items = [x.strip() for x in spec.split(';') if x.strip()]
    head = items[0].split()
    C, R = int(head[0]), int(head[1])
    dots = 'dots' in head
    head = [h for h in head if h != 'dots']
    s = float(head[2]) if len(head) > 2 else 30
    pad = 6
    out = []
    grid = ''.join(f'M{pad + i * s} {pad}V{pad + R * s}' for i in range(C + 1)) + ''.join(f'M{pad} {pad + j * s}H{pad + C * s}' for j in range(R + 1))
    if dots:
        out.append(''.join(f'<circle cx="{pad + i * s}" cy="{pad + j * s}" r="2" fill="#0f172a"/>' for i in range(C + 1) for j in range(R + 1)))
        grid = ''
    shapes = []
    for it in items[1:]:
        p = it.split()
        k = p[0]
        X = lambda c: pad + float(c) * s
        if k == 'rect':
            c, r, w, h = map(float, p[1:5])
            col = p[5] if len(p) > 5 else '#dc2626'
            fill = p[6] if len(p) > 6 else 'none'
            shapes.append(f'<rect x="{X(c)}" y="{X(r)}" width="{w * s}" height="{h * s}" fill="{fill}" stroke="{col}" stroke-width="3"/>')
        elif k == 'poly':
            pts = [q for q in p[1:] if ',' in q]
            rest = [q for q in p[1:] if ',' not in q]
            col = rest[0] if rest else '#dc2626'
            fill = rest[1] if len(rest) > 1 else 'none'
            shapes.append(f'<polygon points="{" ".join(f"{X(a)},{X(b)}" for a, b in (q.split(",") for q in pts))}" fill="{fill}" stroke="{col}" stroke-width="3"/>')
        elif k == 'path':
            pts = [q for q in p[1:] if ',' in q]
            rest = [q for q in p[1:] if ',' not in q]
            col = rest[0] if rest else '#1d4ed8'
            shapes.append(f'<polyline points="{" ".join(f"{X(a)},{X(b)}" for a, b in (q.split(",") for q in pts))}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round"/>')
        elif k == 'fillcells':
            col = p[1]
            for q in p[2:]:
                a, b = q.split(',')
                out.append(f'<rect x="{X(a)}" y="{X(b)}" width="{s}" height="{s}" fill="{col}"/>')
        elif k == 'label':
            out_l = ' '.join(p[3:]).replace('_', ' ')
            shapes.append(f'<text x="{X(float(p[1]) + 0.5)}" y="{X(float(p[2]) + 0.5) + 5}" text-anchor="middle" font-size="{min(14, s * 0.5):.0f}">{escape(out_l)}</text>')
        elif k == 'mirror':
            K = float(p[2])
            if p[1] == 'v':
                shapes.append(f'<line x1="{X(K)}" y1="{pad - 4}" x2="{X(K)}" y2="{pad + R * s + 4}" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="8 5"/>')
            else:
                shapes.append(f'<line x1="{pad - 4}" y1="{X(K)}" x2="{pad + C * s + 4}" y2="{X(K)}" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="8 5"/>')
        else:
            raise ValueError('sqgrid: unknown item ' + k)
    W, H = C * s + 2 * pad, R * s + 2 * pad
    return (f'<svg viewBox="0 0 {W:g} {H:g}" width="{W:g}" role="img" aria-label="Square grid" font-family="sans-serif" fill="#0f172a">'
            + ''.join(out) + f'<path d="{grid}" stroke="#94a3b8" stroke-width="1" fill="none"/>' + ''.join(shapes) + '</svg>')


def lgraph(spec):
    """Class 4 line graph. 'cats A,B,C | vals 1,2,3 | y MIN MAX STEP | xlab X | ylab Y | title T'."""
    o = {}
    for part in spec.split('|'):
        k, _, v = part.strip().partition(' ')
        o[k] = v.strip()
    cats = [c.strip() for c in o['cats'].split(',')]
    vals = [float(v) for v in o['vals'].split(',')]
    ymin, ymax, step = [float(x) for x in o['y'].split()]
    L, T, gw, H = 70, 34 if o.get('title') else 14, 62, 220
    W = gw * len(cats)
    Y = lambda v: T + H - (v - ymin) / (ymax - ymin) * H
    out = []
    v = ymin
    while v <= ymax + 1e-9:
        out.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{L + W}" y2="{Y(v):.1f}" stroke="#cbd5e1"/><text x="{L - 6}" y="{Y(v) + 4:.1f}" text-anchor="end" font-size="11">{v:g}</text>')
        v += step
    pts = []
    for i, (c, val) in enumerate(zip(cats, vals)):
        x = L + gw * (i + 0.5)
        out.append(f'<line x1="{x}" y1="{T}" x2="{x}" y2="{T + H}" stroke="#e2e8f0"/>'
                   f'<text x="{x}" y="{T + H + 16}" text-anchor="middle" font-size="11">{escape(c)}</text>')
        pts.append((x, Y(val)))
    out.append(f'<line x1="{L}" y1="{T + H}" x2="{L + W + 10}" y2="{T + H}" stroke="#0f172a"/><line x1="{L}" y1="{T + H}" x2="{L}" y2="{T - 6}" stroke="#0f172a"/>')
    out.append('<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '" fill="none" stroke="#be185d" stroke-width="2.5"/>')
    out.extend(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#be185d"/>' for x, y in pts)
    if o.get('title'):
        out.append(f'<text x="{L + W / 2}" y="18" text-anchor="middle" font-size="13" fill="#b91c1c" font-weight="600">{escape(o["title"])}</text>')
    if o.get('xlab'):
        out.append(f'<text x="{L + W / 2}" y="{T + H + 36}" text-anchor="middle" font-size="12" fill="#b91c1c">{escape(o["xlab"])}</text>')
    if o.get('ylab'):
        out.append(f'<text x="16" y="{T + H / 2}" text-anchor="middle" font-size="12" fill="#b91c1c" transform="rotate(-90 16 {T + H / 2})">{escape(o["ylab"])}</text>')
    label = 'Line graph: ' + ', '.join(f'{c} {v:g}' for c, v in zip(cats, vals))
    return (f'<svg viewBox="0 0 {L + W + 20} {T + H + 44}" width="{L + W + 20}" role="img" aria-label="{escape(label)}" '
            f'font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>')


def mindmap(spec):
    """Class 4: mind map. 'CENTRE | node ; node ; ...' -> centre box with satellite boxes around it ('/' = line break)."""
    import math
    centre, _, rest = spec.partition('|')
    nodes = [n.strip() for n in rest.split(';') if n.strip()]
    W, H, cx, cy = 520, 340, 260, 170
    out = []
    def box(x, y, text, fill, bold=False):
        lines = text.split('/')
        w = max(90, max(len(l) for l in lines) * 8 + 20)
        h = 22 + 16 * len(lines)
        t = ''.join(f'<text x="{x}" y="{y - h / 2 + 22 + 16 * i}" text-anchor="middle" font-size="13"{" font-weight=\"bold\"" if bold else ""}>{escape(l.strip())}</text>' for i, l in enumerate(lines))
        return f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#0e7490" stroke-width="1.5"/>' + t
    pts = []
    for i, n in enumerate(nodes):
        a = math.radians(-90 + 360 * i / len(nodes))
        pts.append((cx + 200 * math.cos(a), cy + 125 * math.sin(a), n))
    out += [f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="#1e3a8a" stroke-width="1.5"/>' for x, y, _ in pts]
    out += [box(x, y, n, '#bae6fd') for x, y, n in pts]
    out.append(box(cx, cy, centre.strip(), '#7dd3fc', True))
    return (f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="Mind map: {escape(centre.strip())} — '
            + escape(', '.join(n.replace('/', ' ') for n in nodes)) + '" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>')


def pairs(spec):
    """Class 3: beads counted in pairs. 'A-B' -> rows A..B, row n has n beads with each pair ringed; 'n' -> one row."""
    a, _, b = spec.strip().partition('-')
    rows = list(range(int(a), int(b or a) + 1))
    out, y, w = [], 24, 0
    bead = '<circle r="9" fill="#92400e" stroke="#451a03"/><path d="M-5 -2 q5 -6 10 0" stroke="#fbbf24" fill="none" stroke-width="2"/>'
    for n in rows:
        if len(rows) > 1:
            out.append(f'<text x="18" y="{y + 5}" text-anchor="end" font-size="14">{n}.</text>')
        x = 40
        for k in range(n):
            if k % 2 == 0 and k + 1 < n:
                out.append(f'<ellipse cx="{x + 10}" cy="{y}" rx="23" ry="14" fill="none" stroke="#0f172a" stroke-width="1.5"/>')
            out.append(f'<g transform="translate({x} {y})">{bead}</g>')
            x += 20 if k % 2 == 0 else 32
        w = max(w, x + 10)
        y += 34
    label = '; '.join(f'{n} beads: {n // 2} pairs' + (' and 1 left over' if n % 2 else '') for n in rows)
    return f'<svg viewBox="0 0 {w} {y - 10}" width="{w}" role="img" aria-label="{escape(label)}" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def nl3(spec):
    """Class 3 number line in real units. 'A..B step S | mark=v,v | hide=v,v | top=v:TEXT;v:TEXT | dots=v,v'
    mark: value label in a coloured box (and a dot); hide: label left blank ('__'); top: a label box above the tick."""
    parts = [p.strip() for p in spec.split('|')]
    rng, _, st = parts[0].partition('step')
    a, b = [int(x) for x in rng.split('..')]
    s = int(st) if st.strip() else 1
    mark, hide, top, dots = set(), set(), {}, set()
    for p in parts[1:]:
        k, _, v = p.partition('=')
        k = k.strip()
        if k == 'mark':
            mark = {int(x) for x in v.split(',')}
        elif k == 'hide':
            hide = {int(x) for x in v.split(',')}
        elif k == 'dots':
            dots = {int(x) for x in v.split(',')}
        elif k == 'top':
            for item in v.split(';'):
                val, _, txt = item.partition(':')
                top[int(val)] = txt.strip()
    vals = list(range(a, b + 1, s))
    step = max(30, min(56, 660 // max(len(vals) - 1, 1)))
    x0, y = 26, 70 if top else 34
    X = lambda v: x0 + (v - a) / s * step
    out = [f'<line x1="{x0 - 18}" y1="{y}" x2="{X(b) + 18}" y2="{y}" stroke="#be185d" stroke-width="2"/>',
           f'<path d="M{x0 - 20} {y} l10 -6 v12 z" fill="#be185d"/><path d="M{X(b) + 20} {y} l-10 -6 v12 z" fill="#be185d"/>']
    pal = ['#be185d', '#16a34a', '#f59e0b', '#1d4ed8', '#7c3aed', '#0891b2']
    for v in vals:
        out.append(f'<line x1="{X(v):.1f}" y1="{y - 7}" x2="{X(v):.1f}" y2="{y + 7}" stroke="#0f172a" stroke-width="1.4"/>')
        lab = '__' if v in hide else str(v)
        if v in mark:
            col = pal[sorted(mark).index(v) % len(pal)]
            out.append(f'<rect x="{X(v) - 15:.1f}" y="{y + 10}" width="30" height="22" rx="3" fill="{col}"/>')
            out.append(f'<text x="{X(v):.1f}" y="{y + 26}" text-anchor="middle" font-size="15" fill="#fff" font-weight="700">{lab}</text>')
            out.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="4.5" fill="{col}"/>')
        else:
            out.append(f'<text x="{X(v):.1f}" y="{y + 26}" text-anchor="middle" font-size="15">{lab}</text>')
    for v in dots:
        out.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="5" fill="#dc2626"/>')
    for v, txt in top.items():
        wd = max(30, len(txt) * 9 + 12)
        out.append(f'<line x1="{X(v):.1f}" y1="{y - 8}" x2="{X(v):.1f}" y2="{y - 20}" stroke="#0f172a"/>')
        out.append(f'<rect x="{X(v) - wd / 2:.1f}" y="{y - 48}" width="{wd}" height="28" rx="4" fill="#fdf2f8" stroke="#be185d"/>')
        out.append(f'<text x="{X(v):.1f}" y="{y - 29}" text-anchor="middle" font-size="14">{escape(txt)}</text>')
    w = X(b) + 30
    label = f'Number line from {a} to {b} in steps of {s}' + (f'; marked {", ".join(map(str, sorted(mark)))}' if mark else '') + ''.join(f'; {t} at {v}' for v, t in top.items())
    return f'<svg viewBox="0 0 {w:.0f} {y + 40}" width="{w:.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def tower(spec):
    """Class 3: tower(s) of number blocks. 'up 1-9 ;; down 9-1' -> blocks stacked bottom-to-top with an arrow beside."""
    pal = ['#1d4ed8', '#1d4ed8', '#db2777', '#facc15', '#84cc16', '#1e40af', '#22c55e', '#dc2626', '#fde047']
    svgs = []
    for part in [p.strip() for p in spec.split(';;') if p.strip()]:
        kind, _, rng = part.partition(' ')
        a, b = [int(x) for x in rng.split('-')]
        bottom_to_top = list(range(1, 10))[:max(a, b)] if True else []
        vals = list(range(min(a, b), max(a, b) + 1))
        n = len(vals)
        out = []
        for k, v in enumerate(vals):
            y = 10 + (n - 1 - k) * 34
            out.append(f'<rect x="10" y="{y}" width="56" height="32" rx="3" fill="{pal[(v - 1) % len(pal)]}" stroke="#0f172a"/>')
            out.append(f'<text x="38" y="{y + 23}" text-anchor="middle" font-size="18" font-weight="700" fill="#fff" stroke="#0f172a" stroke-width="0.6">{v}</text>')
        h = 10 + n * 34
        if kind == 'up':
            out.append(f'<line x1="86" y1="{h - 6}" x2="86" y2="24" stroke="#0284c7" stroke-width="4"/><path d="M76 28 L86 10 L96 28 Z" fill="#0284c7"/>')
            lab = f'Tower of blocks {vals[0]} to {vals[-1]} in ascending order (smallest at the bottom)'
        else:
            out.append(f'<line x1="86" y1="16" x2="86" y2="{h - 22}" stroke="#0284c7" stroke-width="4"/><path d="M76 {h - 26} L86 {h - 8} L96 {h - 26} Z" fill="#0284c7"/>')
            lab = f'Tower of blocks read from {vals[-1]} down to {vals[0]}: descending order'
        svgs.append(f'<svg viewBox="0 0 104 {h + 6}" width="104" role="img" aria-label="{lab}" font-family="sans-serif">' + ''.join(out) + '</svg>')
    return '<div style="display:flex;gap:40px;justify-content:center;align-items:flex-end">' + ''.join(svgs) + '</div>'


def bond(spec):
    """Class 3: number bonds. '42: 40, 2 ;; 25: 20, 5 [| +]' -> each number on top split into two circled parts."""
    spec, _, op = spec.partition('|')
    groups = []
    for g in spec.split(';;'):
        top, _, parts = g.partition(':')
        groups.append((top.strip(), [p.strip() for p in parts.split(',')]))
    out, x = [], 10
    for k, (top, parts) in enumerate(groups):
        cx = x + 70
        out.append(f'<text x="{cx}" y="24" text-anchor="middle" font-size="20" font-weight="700">{escape(top)}</text>')
        for j, p in enumerate(parts):
            px = x + 25 + j * 90
            out.append(f'<line x1="{cx}" y1="32" x2="{px}" y2="78" stroke="#334155" stroke-width="2"/>')
            out.append(f'<circle cx="{px}" cy="96" r="20" fill="#fff" stroke="#334155" stroke-width="2"/><text x="{px}" y="103" text-anchor="middle" font-size="18">{escape(p)}</text>')
        x += 160
        if op.strip() and k < len(groups) - 1:
            out.append(f'<text x="{x}" y="26" text-anchor="middle" font-size="22">{escape(op.strip())}</text>')
            x += 20
    label = '; '.join(f'{t} splits into {" and ".join(p)}' for t, p in groups)
    return f'<svg viewBox="0 0 {x} 124" width="{x}" role="img" aria-label="{escape(label)}" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def sq8(spec):
    """Class 3: square cut by both diagonals and both midlines into 8 triangles. 'SHADE [colour]'; SHADE = comma list
    of 1-8, numbered clockwise from the top-left triangle on the top edge (1 = top-left upper, 2 = top-right upper,
    3 = right-top, 4 = right-bottom, 5 = bottom-right, 6 = bottom-left, 7 = left-bottom, 8 = left-top), or '-' for none."""
    p = spec.split()
    sh = set() if not p or p[0] == '-' else {int(x) for x in p[0].split(',')}
    col = p[1] if len(p) > 1 else '#4ade80'
    o, s, c = 2, 120, 62
    pts = [(o, o, c, o), (c, o, s + o, o), (s + o, o, s + o, c), (s + o, c, s + o, s + o),
           (s + o, s + o, c, s + o), (c, s + o, o, s + o), (o, s + o, o, c), (o, c, o, o)]
    out = [f'<polygon points="{a},{b} {d},{e} {c},{c}" fill="{col if i + 1 in sh else "#fff"}" stroke="#15803d" stroke-width="1.5"/>'
           for i, (a, b, d, e) in enumerate(pts)]
    return f'<svg viewBox="0 0 124 124" width="124" role="img" aria-label="Square in 8 equal triangles, {len(sh)} shaded">' + ''.join(out) + '</svg>'


def cal(spec):
    """Class 3: year calendar as HTML month tables (Sun-first). 'YEAR' -> 12 small month grids; days that do not fit
    in 5 rows wrap to the first row (as printed in KPTBB calendars)."""
    import calendar as _c
    y = int(spec.split()[0])
    names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    head = ''.join(f'<th style="background:#be185d;color:#fff;font-size:10px;padding:1px 2px">{d}</th>' for d in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
    cells = []
    for m in range(1, 13):
        first = (_c.weekday(y, m, 1) + 1) % 7
        n = _c.monthrange(y, m)[1]
        grid = [[''] * 7 for _ in range(5)]
        for d in range(1, n + 1):
            k = first + d - 1
            r, c = divmod(k, 7)
            if r >= 5:
                r -= 5
            grid[r][c] = str(d)
        rows = ''.join('<tr>' + ''.join(f'<td style="padding:1px 3px;text-align:right;font-size:12px;{"color:#be185d;" if c == 0 else ""}">{v}</td>' for c, v in enumerate(row)) + '</tr>' for row in grid)
        cells.append(f'<table style="border-collapse:collapse;background:#fef9c3;margin:4px"><caption style="font-weight:700">{names[m - 1]}</caption><tr>{head}</tr>{rows}</table>')
    return '<div role="img" aria-label="Calendar of ' + str(y) + '" style="display:flex;flex-wrap:wrap;justify-content:center">' + ''.join(cells) + '</div>'


def ruler(spec):
    """Class 3: centimetre ruler 0-N with millimetre ticks. 'N [| seg=A:0,B:5.7] [| pt=A:0;B:9]'
    seg draws a line segment above the ruler between two labelled points (values in cm); pt only marks points."""
    parts = [p.strip() for p in spec.split('|')]
    n = int(parts[0])
    seg, pts = None, []
    for p in parts[1:]:
        k, _, v = p.partition('=')
        items = [x.split(':') for x in v.replace(';', ',').split(',') if x]
        if k.strip() == 'seg':
            seg = [(a.strip(), float(b)) for a, b in items]
        elif k.strip() == 'pt':
            pts = [(a.strip(), float(b)) for a, b in items]
    u, x0 = 40, 20
    X = lambda v: x0 + v * u
    w = X(n) + 20
    top = 60
    out = [f'<rect x="{x0 - 10}" y="{top}" width="{n * u + 20}" height="50" rx="3" fill="#f59e0b" stroke="#92400e"/>']
    for mm in range(n * 10 + 1):
        h = 16 if mm % 10 == 0 else (10 if mm % 5 == 0 else 6)
        out.append(f'<line x1="{X(mm / 10):.1f}" y1="{top}" x2="{X(mm / 10):.1f}" y2="{top + h}" stroke="#451a03" stroke-width="{1.4 if mm % 10 == 0 else 0.7}"/>')
        if mm % 10 == 0:
            out.append(f'<text x="{X(mm / 10):.1f}" y="{top + 32}" text-anchor="middle" font-size="13" font-weight="700">{mm // 10}</text>')
    out.append(f'<text x="{x0}" y="{top + 46}" font-size="10">centimeters</text>')
    if seg:
        (a, va), (b, vb) = seg[:2]
        out.append(f'<line x1="{X(va)}" y1="{top - 8}" x2="{X(vb)}" y2="{top - 8}" stroke="#1d4ed8" stroke-width="2.5"/>')
        pts = pts + seg
    for lab, v in pts:
        out.append(f'<circle cx="{X(v)}" cy="{top - 8}" r="3.5" fill="#0f172a"/><text x="{X(v)}" y="{top - 18}" text-anchor="middle" font-size="15" fill="#be185d">{escape(lab)}</text>')
    label = f'Ruler from 0 to {n} cm with millimetre marks' + (f'; segment {seg[0][0]}{seg[1][0]} from {seg[0][1]:g} cm to {seg[1][1]:g} cm' if seg else '')
    return f'<svg viewBox="0 0 {w} {top + 56}" width="{w}" role="img" aria-label="{escape(label)}" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def symf(spec):
    """Class 3 symmetry figure (100x100 box). 'KIND [fill] [| x1,y1,x2,y2 ; ...]' -> shape with dashed fold lines.
    KIND: square, rect, tri, circle, A, H, plus, arrow, star, pent, kite, rhombus, hexlong, roundrect, house, apple,
    butterfly, plane, flower, trap1 (right trapezium), trap2, lshape, para, arrowpent."""
    body, _, lines = spec.partition('|')
    p = body.split()
    kind, fill = p[0], (p[1] if len(p) > 1 else '#93c5fd')
    S = {
        'square': '<rect x="15" y="15" width="70" height="70"/>',
        'rect': '<rect x="5" y="25" width="90" height="50"/>',
        'tri': '<polygon points="50,10 92,85 8,85"/>',
        'circle': '<circle cx="50" cy="50" r="38"/>',
        'A': '<path d="M38 10 H62 L92 90 H72 L65 70 H35 L28 90 H8 Z M41 52 H59 L50 26 Z" fill-rule="evenodd"/>',
        'H': '<path d="M18 10 H36 V42 H64 V10 H82 V90 H64 V58 H36 V90 H18 Z"/>',
        'plus': '<path d="M38 8 H62 V38 H92 V62 H62 V92 H38 V62 H8 V38 H38 Z"/>',
        'arrow': '<polygon points="50,8 92,48 68,48 68,92 32,92 32,48 8,48"/>',
        'star': '<polygon points="50,6 61,38 95,38 67,58 78,92 50,71 22,92 33,58 5,38 39,38"/>',
        'pent': '<polygon points="50,8 92,40 76,90 24,90 8,40"/>',
        'kite': '<polygon points="50,5 80,35 50,95 20,35"/>',
        'rhombus': '<polygon points="50,5 90,50 50,95 10,50"/>',
        'hexlong': '<polygon points="5,50 25,25 75,25 95,50 75,75 25,75"/>',
        'roundrect': '<path d="M5 25 H70 A25 25 0 0 1 70 75 H5 Z"/>',
        'house': '<polygon points="50,8 92,42 80,42 80,92 20,92 20,42 8,42"/>',
        'apple': '<path d="M50 25 C30 5 2 20 8 50 C14 80 35 95 50 85 C65 95 86 80 92 50 C98 20 70 5 50 25 Z"/><rect x="47" y="5" width="6" height="18"/>',
        'butterfly': '<path d="M50 30 C35 0 0 5 8 35 C12 50 30 50 45 52 C25 60 15 90 40 85 C48 82 50 70 50 60 C50 70 52 82 60 85 C85 90 75 60 55 52 C70 50 88 50 92 35 C100 5 65 0 50 30 Z"/>',
        'plane': '<path d="M50 5 C55 5 56 15 56 30 L92 50 V58 L56 50 V75 L68 85 V90 L50 85 L32 90 V85 L44 75 V50 L8 58 V50 L44 30 C44 15 45 5 50 5 Z"/>',
        'flower': ''.join(f'<ellipse cx="50" cy="22" rx="9" ry="22" transform="rotate({a} 50 50)"/>' for a in range(0, 360, 45)) + '<circle cx="50" cy="50" r="10" fill="#fde047"/>',
        'trap1': '<polygon points="20,10 45,10 90,90 20,90"/>',
        'trap2': '<polygon points="35,10 92,10 92,90 8,90"/>',
        'lshape': '<polygon points="10,10 50,10 50,40 92,40 92,90 10,90"/>',
        'para': '<polygon points="10,10 60,25 92,95 42,80"/>',
        'arrowpent': '<polygon points="5,55 45,15 92,25 92,85 45,95"/>',
    }
    out = [f'<g fill="{fill}" stroke="#0f172a" stroke-width="1.5">{S[kind]}</g>']
    for ln in [x for x in lines.split(';') if x.strip()]:
        x1, y1, x2, y2 = [float(v) for v in ln.split(',')]
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#be185d" stroke-width="1.6" stroke-dasharray="4 3"/>')
    n = len([x for x in lines.split(';') if x.strip()])
    return f'<svg viewBox="-5 -5 110 110" width="120" role="img" aria-label="{escape(kind)} figure with {n} dashed line(s)">' + ''.join(out) + '</svg>'


def tally(spec):
    """Class 3 tally marks. 'N' -> groups of five (four strokes crossed by a fifth) plus the remaining strokes."""
    n = int(spec.split()[0])
    out, x = [], 6
    for g in range(n // 5):
        for k in range(4):
            out.append(f'<line x1="{x + k * 8}" y1="6" x2="{x + k * 8 - 3}" y2="30" stroke="#0f172a" stroke-width="2"/>')
        out.append(f'<line x1="{x - 6}" y1="24" x2="{x + 30}" y2="10" stroke="#b91c1c" stroke-width="2"/>')
        x += 44
    for k in range(n % 5):
        out.append(f'<line x1="{x + k * 8}" y1="6" x2="{x + k * 8 - 3}" y2="30" stroke="#0f172a" stroke-width="2"/>')
    w = x + (n % 5) * 8 + 6
    return f'<svg viewBox="0 0 {w} 36" width="{w}" role="img" aria-label="Tally marks for {n}">' + ''.join(out) + '</svg>'


def pgraph(spec):
    """Class 3 picture graph. 'LABEL:ICON:N ; LABEL:ICON:N ... [| key TEXT]' -> one row per label with N icons."""
    body, _, key = spec.partition('| key')
    rows = [r.strip().split(':') for r in body.split(';') if r.strip()]
    out, y = [], 0
    maxn = max(int(n) for _, _, n in rows)
    for lab, ic, n in rows:
        shape, step = _ICON[ic]
        out.append(f'<rect x="0" y="{y}" width="130" height="40" rx="5" fill="#fce7f3" stroke="#9d174d"/><text x="65" y="{y + 25}" text-anchor="middle" font-size="14">{escape(lab)}</text>')
        out.append(f'<rect x="136" y="{y}" width="{maxn * 40 + 20}" height="40" rx="5" fill="#fff" stroke="#9d174d"/>')
        for k in range(int(n)):
            out.append(f'<g transform="translate({160 + k * 40} {y + 22})">{shape}</g>')
        y += 46
    w = 156 + maxn * 40
    if key.strip():
        out.append(f'<text x="{w}" y="{y + 14}" text-anchor="end" font-size="13" font-weight="700">{escape(key.strip())}</text>')
        y += 20
    label = '; '.join(f'{l}: {n} pictures' for l, _, n in rows) + (f'; key {key.strip()}' if key.strip() else '')
    return f'<svg viewBox="0 0 {w + 4} {y}" width="{w + 4}" role="img" aria-label="{escape(label)}" font-family="sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'



def arl(spec):
    """Arabic letter/word grid (right to left) — reuses the Class 1 generator (class-1/tools/figs1.py arl):
    'COLS [c] [s=56] [w=1.6] | b~با t~تا ; d ; ...' (see that docstring)."""
    import importlib.util
    from pathlib import Path
    p = Path(__file__).resolve().parents[2] / 'class-1' / 'tools' / 'figs1.py'
    spec_ = importlib.util.spec_from_file_location('figs1_for_cls3', p)
    mod = importlib.util.module_from_spec(spec_)
    spec_.loader.exec_module(mod)
    return mod.arl(spec)
