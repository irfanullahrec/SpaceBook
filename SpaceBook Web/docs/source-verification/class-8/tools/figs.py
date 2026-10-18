"""SVG generators for recurring Class 8 (copied from the Class 6 tool) Mathematics figures (long division, division ladder, factor tree)."""
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
