"""Class 5 Mathematics SVG figure generators (used as `op spec || caption` lines; see build_math5.py FIG5_OPS)."""
from html import escape

FONT = 'font-family="Segoe UI, Arial, sans-serif" fill="#0f172a"'


def _t(x, y, s, size=16, anchor='middle', weight='400', fill='#0f172a'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}">{escape(str(s))}</text>'


def jumps(spec):
    """'5,7,9,?,?,? | +2,+2,+2 [| above] [| gap=110]' -> terms in a row with curved arcs between neighbours
    (use ';' to separate terms that contain commas, e.g. '400,000; 40,000; 4,000; ?').
    A term written [] is drawn as an empty answer box; arc labels are given left to right (missing labels = no label)."""
    parts = [p.strip() for p in spec.split('|')]
    sep = ';' if ';' in parts[0] else ','
    terms = [x.strip() for x in parts[0].split(sep)]
    labels = [x.strip() for x in parts[1].split(sep)] if len(parts) > 1 and parts[1] else []
    opts = parts[2:]
    where = 'above' if 'above' in opts else 'below'
    gap = next((int(o[4:]) for o in opts if o.startswith('gap=')), 62)
    x0 = max(40, gap // 2)
    w = gap * (len(terms) - 1) + 2 * x0
    h = 110
    ty = 34 if where == 'below' else 84
    out = [f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="Number pattern {escape(", ".join(terms))}" {FONT}>']
    for i, term in enumerate(terms):
        x = x0 + i * gap
        if term == '[]':
            out.append(f'<rect x="{x-11}" y="{ty-17}" width="22" height="22" fill="#fff" stroke="#334155" stroke-width="1.5"/>')
        else:
            out.append(_t(x, ty, term, 17))
        if i < len(terms) - 1:
            x2 = x + gap
            if where == 'below':
                out.append(f'<path d="M{x+4} {ty+8} Q{x + gap/2} {ty+48} {x2-4} {ty+8}" fill="none" stroke="#0369a1" stroke-width="1.6"/>')
                if i < len(labels) and labels[i]:
                    out.append(_t(x + gap / 2, ty + 62, labels[i], 15, fill='#0369a1'))
            else:
                out.append(f'<path d="M{x+4} {ty-22} Q{x + gap/2} {ty-62} {x2-4} {ty-22}" fill="none" stroke="#0369a1" stroke-width="1.6"/>')
                if i < len(labels) and labels[i]:
                    out.append(_t(x + gap / 2, ty - 50, labels[i], 15, fill='#0369a1'))
    out.append('</svg>')
    return '\n'.join(out)


def hchart(spec):
    """'10,19,28,37,46,55,64,73,82,91 [| #7dd3fc]' -> 1-100 hundreds chart (10 x 10) with the listed numbers shaded."""
    parts = [p.strip() for p in spec.split('|')]
    marks = {int(x) for x in parts[0].split(',') if x.strip()}
    fill = parts[1] if len(parts) > 1 else '#7dd3fc'
    c = 36
    w = h = c * 10 + 4
    out = [f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="Hundreds chart with {", ".join(map(str, sorted(marks)))} shaded" {FONT}>']
    for n in range(1, 101):
        r, k = divmod(n - 1, 10)
        x, y = 2 + k * c, 2 + r * c
        out.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{fill if n in marks else "#fff"}" stroke="#334155" stroke-width="1"/>')
        out.append(_t(x + c / 2, y + c / 2 + 6, n, 15))
    out.append('</svg>')
    return '\n'.join(out)


def segbars(spec):
    """'24:6 ; 18:6 | cm' -> one bar per item (length:piece), divided into equal pieces; first piece and total labelled."""
    parts = [p.strip() for p in spec.split('|')]
    unit = parts[1] if len(parts) > 1 else ''
    items = [tuple(int(v) for v in x.split(':')) for x in parts[0].split(';')]
    longest = max(L for L, _ in items)
    scale = 300 / longest
    w, rowh = 360, 64
    out = [f'<svg viewBox="0 0 {w} {rowh * len(items) + 10}" width="{w}" role="img" aria-label="Bars cut into equal pieces" {FONT}>']
    for i, (L, p) in enumerate(items):
        y = 22 + i * rowh
        out.append(f'<rect x="30" y="{y}" width="{L*scale:.1f}" height="10" rx="3" fill="#f472b6" stroke="#9d174d"/>')
        for k in range(0, L // p + 1):
            x = 30 + k * p * scale
            out.append(f'<line x1="{x:.1f}" y1="{y-8}" x2="{x:.1f}" y2="{y+18}" stroke="#334155" stroke-width="1.4"/>')
        out.append(_t(30 + p * scale / 2, y - 10, f'{p}{unit}', 13))
        out.append(_t(30 + L * scale / 2, y + 36, f'{L}{unit}', 14))
    out.append('</svg>')
    return '\n'.join(out)


def _frac_label(x, y, num, den, size=16):
    return (_t(x, y, num, size) + f'<line x1="{x-10}" y1="{y+5}" x2="{x+10}" y2="{y+5}" stroke="#0f172a" stroke-width="1.3"/>'
            + _t(x, y + 22, den, size))


def fracs(spec):
    """Row of fraction pictures and operators, e.g. 'c2/1 + c4/1 = c4/2 + c4/1 = c4/3'.
    cN/K: circle cut into N equal sectors with K shaded (from the top, anticlockwise);
    bN/K: bar cut into N equal parts with K shaded (from the left); gRxC/K: R x C grid with K cells shaded (row by row).
    Append :nolabel to hide the fraction under a picture; append @#hex to change the shade colour.
    Any other token (+, −, ×, ÷, =, of, a number) is drawn as text."""
    import math
    toks = spec.split()
    out, x, H = [], 10, 128
    shade = '#0f9f8f'
    for tok in toks:
        label = True
        col = shade
        if '@' in tok:
            tok, col = tok.split('@')
        if tok.endswith(':nolabel'):
            tok, label = tok[:-8], False
        kind = tok[0]
        if kind in 'cbg' and '/' in tok:
            shape, k = tok[1:].split('/')
            k = int(k)
            if kind == 'c':
                n = int(shape); r = 34; cx, cy = x + r + 2, 44
                for i in range(n):
                    a0 = math.pi / 2 + 2 * math.pi * i / n
                    a1 = math.pi / 2 + 2 * math.pi * (i + 1) / n
                    x0, y0 = cx + r * math.cos(a0), cy - r * math.sin(a0)
                    x1, y1 = cx + r * math.cos(a1), cy - r * math.sin(a1)
                    big = 1 if (a1 - a0) > math.pi else 0
                    fill = col if i < k else '#fff'
                    if n == 1:
                        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#0f172a" stroke-width="1.5"/>')
                    else:
                        out.append(f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 0 {x1:.1f} {y1:.1f} Z" fill="{fill}" stroke="#0f172a" stroke-width="1.5"/>')
                wdt = 2 * r + 4
                if label:
                    out.append(_frac_label(cx, 102, k, n))
            elif kind == 'b':
                n = int(shape); pw = 22 if n > 4 else 30
                for i in range(n):
                    out.append(f'<rect x="{x + i*pw}" y="26" width="{pw}" height="36" fill="{col if i < k else "#fff"}" stroke="#0f172a" stroke-width="1.4"/>')
                wdt = n * pw
                if label:
                    out.append(_frac_label(x + wdt / 2, 102, k, n))
            else:
                R, C = (int(v) for v in shape.split('x')); cs = 18
                for i in range(R * C):
                    rr, cc = divmod(i, C)
                    out.append(f'<rect x="{x + cc*cs}" y="{10 + rr*cs}" width="{cs}" height="{cs}" fill="{col if i < k else "#fff"}" stroke="#0f172a" stroke-width="1.1"/>')
                wdt = C * cs
                if label:
                    out.append(_frac_label(x + wdt / 2, 102, k, R * C))
            x += wdt + 14
        else:
            out.append(_t(x + 10, 50, tok, 20))
            x += 10 + 8 * len(tok) + 12
    W = x
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="Fraction pictures: {escape(spec)}" {FONT}>' + ''.join(out) + '</svg>'


def rectlab(spec):
    """Labelled rectangle: 'W H fill | A,B,C,D | bottom text | centre text | right text'
    corners are given anticlockwise from bottom-left (A bottom-left, B bottom-right, C top-right, D top-left)."""
    p = [x.strip() for x in spec.split('|')] + [''] * 5
    w, h, fill = p[0].split()
    w, h = float(w), float(h)
    corners = [c.strip() for c in p[1].split(',')] if p[1] else ['', '', '', '']
    x0, y0 = 30, 24
    W = x0 + w + 110
    H = y0 + h + 48
    out = [f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" role="img" aria-label="Rectangle {escape(p[1])} {escape(p[2])}" {FONT}>',
           f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="{fill}" stroke="#0f172a" stroke-width="1.6"/>']
    pts = [(x0 - 10, y0 + h + 14), (x0 + w + 10, y0 + h + 14), (x0 + w + 10, y0 - 6), (x0 - 10, y0 - 6)]
    for (x, y), c in zip(pts, corners):
        out.append(_t(x, y, c, 15))
    if p[2]:
        out.append(_t(x0 + w / 2, y0 + h + 34, p[2], 15))
    if p[3]:
        out.append(_t(x0 + w / 2, y0 + h / 2 + 5, p[3], 15))
    if p[4]:
        out.append(_t(x0 + w + 16, y0 + h / 2 + 5, p[4], 15, anchor='start'))
    out.append('</svg>')
    return '\n'.join(out)


def decgrid(spec):
    """'cols=2 rows=4 | 0.2 | 0.4 | 0.08' -> 10x10 grid: first `cols` columns blue, first `rows` rows yellow, overlap green,
    with the three labels (columns value, rows value, product) beside the grid."""
    p = [x.strip() for x in spec.split('|')]
    kv = dict(x.split('=') for x in p[0].split())
    nc, nr = int(kv['cols']), int(kv['rows'])
    c = 26
    x0, y0 = 70, 10
    out = []
    for r in range(10):
        for k in range(10):
            fill = '#16a34a' if (k < nc and r < nr) else '#38bdf8' if k < nc else '#fde047' if r < nr else '#fff'
            out.append(f'<rect x="{x0 + k*c}" y="{y0 + r*c}" width="{c}" height="{c}" fill="{fill}" stroke="#334155" stroke-width="1"/>')
    out.append(_t(x0 + 10 * c + 26, y0 + nr * c / 2 + 5, p[2], 15))
    out.append(_t(x0 - 26, y0 + 9 * c, p[1], 15))
    out.append(_t(x0 - 26, y0 + nr * c / 2 + 5, p[3], 15))
    W, H = x0 + 10 * c + 60, y0 + 10 * c + 10
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="Hundred grid: {nc} columns blue, {nr} rows yellow, {nc*nr} squares green" {FONT}>' + ''.join(out) + '</svg>'


def angle(spec):
    """Angle figure. 'rays=0,210 | arc=0:210:22:210° | right=0:90 | pts=A@210,B@0,O | len=120 | dot'
    rays: directions in degrees (0 = east, anticlockwise). arc=a0:a1:r:label draws an arc anticlockwise from a0 to a1
    (several arcs separated by ';'). right=a0:a1 draws a right-angle square between rays a0 and a1.
    pts: letter@direction labels at ray ends; a bare letter labels the vertex. 'dot' marks the vertex."""
    import math
    kv = {}
    for part in spec.split('|'):
        part = part.strip()
        if '=' in part:
            k, v = part.split('=', 1)
            kv[k.strip()] = v.strip()
        elif part:
            kv[part] = ''
    L = float(kv.get('len', 110))
    rays = [float(a) for a in kv.get('rays', '').split(',') if a.strip()]
    pad = 30
    cx, cy = L + pad, L + pad
    W = H = 2 * (L + pad)
    out = []
    pt = lambda a, r: (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
    for a in rays:
        x, y = pt(a, L)
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#0369a1" stroke-width="2"/>')
        hx, hy = pt(a, L - 10)
        lx, ly = pt(a + 4, L - 12)
        rx, ry = pt(a - 4, L - 12)
        out.append(f'<path d="M{x:.1f} {y:.1f} L{lx:.1f} {ly:.1f} M{x:.1f} {y:.1f} L{rx:.1f} {ry:.1f}" stroke="#0369a1" stroke-width="2" fill="none"/>')
    for arc in [a for a in kv.get('arc', '').split(';') if a.strip()]:
        f = arc.split(':')
        a0, a1, r = float(f[0]), float(f[1]), float(f[2])
        lab = f[3] if len(f) > 3 else ''
        x0, y0 = pt(a0, r)
        x1, y1 = pt(a1, r)
        sweep = (a1 - a0) % 360
        big = 1 if sweep > 180 else 0
        out.append(f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 0 {x1:.1f} {y1:.1f}" fill="none" stroke="#dc2626" stroke-width="1.6"/>')
        if lab:
            mx, my = pt(a0 + sweep / 2, r + 18)
            out.append(_t(mx, my + 5, lab, 14, fill='#dc2626'))
    if 'right' in kv:
        a0, a1 = (float(v) for v in kv['right'].split(':'))
        s = 14
        p1, p2 = pt(a0, s), pt(a1, s)
        p3 = (p1[0] + p2[0] - cx, p1[1] + p2[1] - cy)
        out.append(f'<path d="M{p1[0]:.1f} {p1[1]:.1f} L{p3[0]:.1f} {p3[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="#dc2626" stroke-width="1.5"/>')
    for p in [p.strip() for p in kv.get('pts', '').split(',') if p.strip()]:
        if '@' in p:
            n, a = p.split('@')
            x, y = pt(float(a), L + 14)
            out.append(_t(x, y + 5, n, 15, weight='600'))
        else:
            out.append(_t(cx + 4, cy + 22, p, 15, weight='600'))
    for p in [p.strip() for p in kv.get('nums', '').split(',') if p.strip()]:
        n, a = p.split('@')
        x, y = pt(float(a), 22)
        out.append(_t(x, y + 5, n, 15, weight='600'))
    if 'ring' in kv:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{float(kv["ring"])}" fill="none" stroke="#0f172a" stroke-width="1.3"/>')
    if 'dot' in kv:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#ec4899"/>')
    ys = [cy] + [pt(a, L + 14)[1] for a in rays]
    for arc in [a for a in kv.get('arc', '').split(';') if a.strip()]:
        f = arc.split(':')
        a0, a1, r = float(f[0]), float(f[1]), float(f[2]) + 24
        sweep = (a1 - a0) % 360
        ys += [pt(a0 + sweep * k / 8, r)[1] for k in range(9)]
    y0, y1 = max(0, min(ys) - 22), min(H, max(ys) + 28)
    return f'<svg viewBox="0 {y0:.0f} {W:.0f} {y1 - y0:.0f}" width="{min(W, 300):.0f}" role="img" aria-label="Angle figure" {FONT}>' + ''.join(out) + '</svg>'


def protractor(spec):
    """Protractor on a base ray. 'mark=90 | label=C | ray | names=A,B'
    Draws a semicircular protractor with 10° ticks (outer scale 0..180 left to right, inner scale 180..0) centred on the vertex;
    'mark' adds a point (and label) at that inner-scale reading; 'ray' also draws the finished arm through it."""
    import math
    kv = {}
    for part in spec.split('|'):
        part = part.strip()
        if '=' in part:
            k, v = part.split('=', 1)
            kv[k.strip()] = v.strip()
        elif part:
            kv[part] = ''
    R = 120
    down = 'down' in kv
    cx, cy = (160, 30) if down else (160, 150)
    sg = -1 if down else 1
    names = kv.get('names', 'A,B').split(',')
    out = [f'<path d="M{cx - R} {cy} A{R} {R} 0 0 {1 if sg > 0 else 0} {cx + R} {cy} Z" fill="#fde68a" fill-opacity="0.35" stroke="#b45309" stroke-width="1.4"/>',
           f'<path d="M{cx - R + 22} {cy} A{R - 22} {R - 22} 0 0 {1 if sg > 0 else 0} {cx + R - 22} {cy}" fill="none" stroke="#b45309" stroke-width="0.8"/>']
    for d in range(0, 181, 10):
        a = math.radians(180 - d)
        x1, y1 = cx + R * math.cos(a), cy - sg * R * math.sin(a)
        x2, y2 = cx + (R - 9) * math.cos(a), cy - sg * (R - 9) * math.sin(a)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#b45309" stroke-width="1"/>')
        if d % 30 == 0:
            ox, oy = cx + (R - 16) * math.cos(a), cy - sg * (R - 16) * math.sin(a)
            ix, iy = cx + (R - 32) * math.cos(a), cy - sg * (R - 32) * math.sin(a)
            out.append(_t(ox, oy + 3, d, 9, fill='#b45309'))
            out.append(_t(ix, iy + 3, 180 - d, 9, fill='#be185d'))
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#b45309" stroke-width="0.3"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#facc15" stroke="#b45309"/>')
    if down:
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx - R - 30}" y2="{cy}" stroke="#0369a1" stroke-width="2"/>')
        out.append(f'<path d="M{cx - R - 30} {cy} l9 -4 v8 z" fill="#0369a1"/>')
        out.append(_t(cx, cy - 10, names[0], 15, weight='600'))
        out.append(_t(cx - R - 22, cy - 10, names[1] if len(names) > 1 else '', 15, weight='600'))
    else:
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + R + 30}" y2="{cy}" stroke="#0369a1" stroke-width="2"/>')
        out.append(f'<path d="M{cx + R + 30} {cy} l-9 -4 v8 z" fill="#0369a1"/>')
        out.append(_t(cx, cy + 20, names[0], 15, weight='600'))
        out.append(_t(cx + R + 22, cy + 20, names[1] if len(names) > 1 else '', 15, weight='600'))
    if 'mark' in kv:
        m = float(kv['mark'])
        a = math.radians(180 + m if down else m)
        mx, my = cx + (R + 6) * math.cos(a), cy - (R + 6) * math.sin(a)
        out.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="3.5" fill="#dc2626"/>')
        if kv.get('label'):
            lx, ly = cx + (R + 20) * math.cos(a), cy - (R + 20) * math.sin(a)
            out.append(_t(lx, ly + 5, kv['label'], 15, weight='600'))
        if 'ray' in kv:
            ex, ey = cx + (R + 12) * math.cos(a), cy - (R + 12) * math.sin(a)
            out.append(f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#0369a1" stroke-width="2"/>')
    return f'<svg viewBox="0 {-10 if down else 0} 340 {195 if down else 180}" width="320" role="img" aria-label="Protractor placed on ray {escape(names[0])}{escape(names[1] if len(names) > 1 else "")}" {FONT}>' + ''.join(out) + '</svg>'


def clock(spec):
    """Analogue clock. 'h=3 m=0 s=52' -> hour, minute and (optional) second hand; s in seconds (0..59)."""
    import math
    kv = dict(p.split('=') for p in spec.split())
    h, m = float(kv.get('h', 0)), float(kv.get('m', 0))
    R, c = 90, 100
    out = [f'<circle cx="{c}" cy="{c}" r="{R}" fill="#fff" stroke="#9f1239" stroke-width="5"/>']
    for k in range(60):
        a = math.radians(90 - k * 6)
        r1 = R - (9 if k % 5 == 0 else 5)
        out.append(f'<line x1="{c + (R - 2) * math.cos(a):.1f}" y1="{c - (R - 2) * math.sin(a):.1f}" x2="{c + r1 * math.cos(a):.1f}" y2="{c - r1 * math.sin(a):.1f}" stroke="{"#dc2626" if k % 5 == 0 else "#334155"}" stroke-width="{2 if k % 5 == 0 else 1}"/>')
    for n in range(1, 13):
        a = math.radians(90 - n * 30)
        out.append(_t(c + (R - 22) * math.cos(a), c - (R - 22) * math.sin(a) + 6, n, 16))
    def hand(deg, length, w, col):
        a = math.radians(90 - deg)
        return f'<line x1="{c}" y1="{c}" x2="{c + length * math.cos(a):.1f}" y2="{c - length * math.sin(a):.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
    out.append(hand((h % 12) * 30 + m * 0.5, R * 0.5, 5, '#0f172a'))
    out.append(hand(m * 6, R * 0.78, 4, '#0f172a'))
    if 's' in kv:
        out.append(hand(float(kv['s']) * 6, R * 0.82, 1.5, '#dc2626'))
    out.append(f'<circle cx="{c}" cy="{c}" r="5" fill="#ec4899"/>')
    return f'<svg viewBox="0 0 200 200" width="180" role="img" aria-label="Clock showing {int(h)}:{int(m):02d}" {FONT}>' + ''.join(out) + '</svg>'


def poly(spec):
    """Labelled polygon. 'A:0,0 B:3,0 C:1.5,2.6 | fill=#0ea5e9 | sides=3 cm,3 cm,3 cm | angles=60°,60°,60° | right=B | ticks=1,1,1 | scale=50'
    Points in drawing units (y up). sides[i] labels edge P[i]P[i+1]; angles[i] label at vertex i (blank = none);
    right=letters marks right angles; ticks=n per edge (equal-side marks)."""
    import math
    parts = [p.strip() for p in spec.split('|')]
    pts = []
    for tok in parts[0].split():
        n, xy = tok.split(':')
        x, y = (float(v) for v in xy.split(','))
        pts.append((n, x, y))
    kv = {}
    for p in parts[1:]:
        if '=' in p:
            k, v = p.split('=', 1)
            kv[k.strip()] = v.strip()
    sc = float(kv.get('scale', 50))
    xs = [x for _, x, _ in pts]
    ys = [y for _, _, y in pts]
    pad = 46
    W = (max(xs) - min(xs)) * sc + 2 * pad
    H = (max(ys) - min(ys)) * sc + 2 * pad
    P = [(n, pad + (x - min(xs)) * sc, pad + (max(ys) - y) * sc) for n, x, y in pts]
    gx = sum(p[1] for p in P) / len(P)
    gy = sum(p[2] for p in P) / len(P)
    fill = kv.get('fill', '#bae6fd')
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for _, x, y in P) + ' Z'
    out = [f'<path d="{d}" fill="{fill}" fill-opacity="0.85" stroke="#0f172a" stroke-width="1.8"/>']
    sides = [s.strip() for s in kv.get('sides', '').split(',')] if kv.get('sides') else []
    ticks = [int(t) for t in kv.get('ticks', '').split(',')] if kv.get('ticks') else []
    k = len(P)
    for i in range(k):
        (_, x1, y1), (_, x2, y2) = P[i], P[(i + 1) % k]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ex_, ey_ = x2 - x1, y2 - y1
        el_ = math.hypot(ex_, ey_) or 1
        nx, ny = -ey_ / el_, ex_ / el_
        if nx * (mx - gx) + ny * (my - gy) < 0:
            nx, ny = -nx, -ny
        if i < len(sides) and sides[i]:
            off = 14 + 3.4 * len(sides[i]) * abs(nx)
            out.append(_t(mx + nx * off, my + ny * 16 + 5, sides[i], 14))
        if i < len(ticks) and ticks[i]:
            ex, ey = x2 - x1, y2 - y1
            el = math.hypot(ex, ey)
            ux, uy = ex / el, ey / el
            for t in range(ticks[i]):
                off = (t - (ticks[i] - 1) / 2) * 5
                cx_, cy_ = mx + ux * off, my + uy * off
                out.append(f'<line x1="{cx_ - uy * 6:.1f}" y1="{cy_ + ux * 6:.1f}" x2="{cx_ + uy * 6:.1f}" y2="{cy_ - ux * 6:.1f}" stroke="#0f172a" stroke-width="1.5"/>')
    angles = [a.strip() for a in kv.get('angles', '').split(',')] if kv.get('angles') else []
    rights = set(kv.get('right', ''))
    for i, (n, x, y) in enumerate(P):
        vx, vy = x - gx, y - gy
        vl = math.hypot(vx, vy) or 1
        if not n.startswith('_'):
            out.append(_t(x + vx / vl * 16, y + vy / vl * 16 + 5, n, 15, weight='600'))
        if n in rights:
            (_, ax, ay), (_, bx, by) = P[i - 1], P[(i + 1) % k]
            u1 = ((ax - x), (ay - y)); l1 = math.hypot(*u1); u1 = (u1[0] / l1 * 12, u1[1] / l1 * 12)
            u2 = ((bx - x), (by - y)); l2 = math.hypot(*u2); u2 = (u2[0] / l2 * 12, u2[1] / l2 * 12)
            out.append(f'<path d="M{x + u1[0]:.1f} {y + u1[1]:.1f} L{x + u1[0] + u2[0]:.1f} {y + u1[1] + u2[1]:.1f} L{x + u2[0]:.1f} {y + u2[1]:.1f}" fill="none" stroke="#dc2626" stroke-width="1.5"/>')
        if i < len(angles) and angles[i]:
            out.append(_t(x - vx / vl * 26, y - vy / vl * 26 + 5, angles[i], 12, fill='#b91c1c'))
    return f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{min(W, 320):.0f}" role="img" aria-label="Figure {escape(" ".join(n for n, _, _ in pts))}" {FONT}>' + ''.join(out) + '</svg>'


def uprays(spec):
    """'A,B | 3.8 cm | marks=D,C@3.8 cm' -> base AB with two upright rays and right-angle squares;
    optional marks= labels for the points marked on the rays (left,right) with the side length written beside them."""
    parts = [p.strip() for p in spec.split('|')]
    a, b = [x.strip() for x in parts[0].split(',')]
    base = parts[1] if len(parts) > 1 else ''
    marks = None
    for p in parts[2:]:
        if p.startswith('marks='):
            names, _, lab = p[6:].partition('@')
            marks = ([x.strip() for x in names.split(',')], lab.strip())
    out = ['<line x1="60" y1="190" x2="220" y2="190" stroke="#0369a1" stroke-width="2"/>']
    for x in (60, 220):
        out.append(f'<line x1="{x}" y1="190" x2="{x}" y2="25" stroke="#0f172a" stroke-width="2"/><path d="M{x} 18 l-5 10 h10 z" fill="#0f172a"/>')
    out.append('<rect x="60" y="176" width="14" height="14" fill="#f9a8d4" stroke="#dc2626"/><rect x="206" y="176" width="14" height="14" fill="#f9a8d4" stroke="#dc2626"/>')
    out.append(_t(60, 212, a, 15, weight='600') + _t(220, 212, b, 15, weight='600') + _t(140, 212, base, 14))
    if marks:
        (l, r), lab = marks
        for x, n, side in ((60, l, 'end'), (220, r, 'start')):
            out.append(f'<line x1="{x - 12}" y1="70" x2="{x + 12}" y2="70" stroke="#dc2626" stroke-width="2"/>')
            out.append(_t(x - 18 if side == 'end' else x + 18, 75, n, 15, anchor=side, weight='600'))
            out.append(_t(x - 10 if side == 'end' else x + 10, 135, lab, 13, anchor=side))
    return '<svg viewBox="0 0 290 225" width="260" role="img" aria-label="Upright rays at both ends of the base" ' + FONT + '>' + ''.join(out) + '</svg>'


_SYM = {
    'leaf': '<path d="M60 150 C20 110 0 70 20 40 C35 15 55 20 60 40 C65 20 85 15 100 40 C120 70 100 110 60 150 Z" fill="#5eead4" stroke="#0f766e" stroke-width="2"/>',
    'maple': '<path d="M60 10 L70 40 L95 30 L85 60 L115 65 L90 85 L100 110 L70 100 L62 150 L58 150 L50 100 L20 110 L30 85 L5 65 L35 60 L25 30 L50 40 Z" fill="#f43f5e" stroke="#9f1239" stroke-width="1.5"/>',
    'butterfly': '<ellipse cx="38" cy="55" rx="34" ry="30" fill="#f97316" stroke="#1f2937" stroke-width="3"/><ellipse cx="82" cy="55" rx="34" ry="30" fill="#f97316" stroke="#1f2937" stroke-width="3"/><ellipse cx="42" cy="105" rx="24" ry="22" fill="#fb923c" stroke="#1f2937" stroke-width="3"/><ellipse cx="78" cy="105" rx="24" ry="22" fill="#fb923c" stroke="#1f2937" stroke-width="3"/><rect x="56" y="35" width="8" height="90" rx="4" fill="#1f2937"/>',
    'M': '<path d="M15 145 V20 H40 L60 75 L80 20 H105 V145 H85 V60 L66 110 H54 L35 60 V145 Z" fill="#f43f5e" stroke="#9f1239" stroke-width="1.5"/>',
    'ellipse': '<ellipse cx="60" cy="80" rx="55" ry="30" fill="#fde68a" stroke="#0f172a" stroke-width="2"/>',
}


def symfig(spec):
    """'leaf maple | v' -> row of simple shapes each with a vertical line of symmetry (kinds: leaf, maple, butterfly, M, ellipse).
    Option 'red' draws the line in red (default blue)."""
    parts = [p.strip() for p in spec.split('|')]
    kinds = parts[0].split()
    col = '#dc2626' if 'red' in parts[1:] else '#0284c7'
    out = []
    for i, k in enumerate(kinds):
        x = i * 140
        out.append(f'<g transform="translate({x + 10},0)">{_SYM[k]}<line x1="60" y1="2" x2="60" y2="158" stroke="{col}" stroke-width="2.5"/></g>')
    W = 140 * len(kinds) + 10
    return f'<svg viewBox="0 0 {W} 162" width="{min(W, 420)}" role="img" aria-label="Shapes with a line of symmetry: {escape(", ".join(kinds))}" {FONT}>' + ''.join(out) + '</svg>'


def symlines(spec):
    """'square | rect' -> a square with its 4 lines of symmetry and a rectangle with its 2 lines of symmetry."""
    out = ['<rect x="20" y="20" width="90" height="90" fill="none" stroke="#0f172a" stroke-width="2"/>']
    for x1, y1, x2, y2 in ((65, 5, 65, 125), (5, 65, 125, 65), (8, 8, 122, 122), (122, 8, 8, 122)):
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0284c7" stroke-width="1.5"/>')
    out.append('<rect x="170" y="35" width="150" height="60" fill="none" stroke="#0f172a" stroke-width="2"/>')
    out.append('<line x1="245" y1="10" x2="245" y2="120" stroke="#0284c7" stroke-width="1.5"/><line x1="155" y1="65" x2="335" y2="65" stroke="#0284c7" stroke-width="1.5"/>')
    return f'<svg viewBox="0 0 345 130" width="320" role="img" aria-label="Square with four lines of symmetry and rectangle with two lines of symmetry" {FONT}>' + ''.join(out) + '</svg>'


def tryshapes(spec):
    """Pentagon, bent arrow and letter T (Try Yourself on reflective symmetry)."""
    import math
    pts = ' '.join(f'{60 + 45 * math.cos(math.radians(90 + 72 * k)):.1f},{70 - 45 * math.sin(math.radians(90 + 72 * k)):.1f}' for k in range(5))
    out = [f'<polygon points="{pts}" fill="#22d3ee" stroke="#0f172a" stroke-width="2"/>',
           '<path d="M150 95 L175 75 L175 88 L205 88 L205 50 L192 50 L212 25 L232 50 L219 50 L219 102 L175 102 L175 115 Z" fill="#fef08a" stroke="#0f172a" stroke-width="2"/>',
           '<path d="M260 25 H330 V42 H303 V120 H287 V42 H260 Z" fill="#fff" stroke="#0f172a" stroke-width="2"/>']
    return f'<svg viewBox="0 0 345 130" width="320" role="img" aria-label="A regular pentagon, a bent arrow and the letter T" {FONT}>' + ''.join(out) + '</svg>'


def quarterturn(spec):
    """Four right angles (4 × 90°) around a point: a complete revolution."""
    out = ['<line x1="20" y1="80" x2="220" y2="80" stroke="#0f172a" stroke-width="1.6"/><line x1="120" y1="5" x2="120" y2="155" stroke="#0f172a" stroke-width="1.6"/>',
           '<path d="M20 80 l10 -5 v10 z M220 80 l-10 -5 v10 z M120 5 l-5 10 h10 z M120 155 l-5 -10 h10 z" fill="#0f172a"/>',
           '<rect x="110" y="70" width="20" height="20" fill="none" stroke="#dc2626"/>',
           _t(95, 68, '90°', 13), _t(147, 68, '90°', 13), _t(95, 103, '90°', 13), _t(147, 103, '90°', 13)]
    return f'<svg viewBox="0 0 240 160" width="220" role="img" aria-label="Four 90 degree angles make a complete revolution" {FONT}>' + ''.join(out) + '</svg>'


def petals(spec):
    """Four-petal flower turned through 0°, 90°, 180°, 270°, 360° (petal numbers 1-4 move round)."""
    import math
    out = []
    labels = [(0, '0°'), (90, '90°'), (180, '180°'), (270, '270°'), (360, '360°')]
    for i, (turn, lab) in enumerate(labels):
        cx, cy = 60 + i * 120, 80
        for p in range(4):
            a = math.radians(turn + 90 * p)
            px, py = cx + 26 * math.cos(a), cy - 26 * math.sin(a)
            rot = -math.degrees(a)
            fill = '#0f766e' if not (i == 4 and p in (0, 2)) else ('#38bdf8' if p == 0 else '#be123c')
            out.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="24" ry="10" transform="rotate({rot:.1f} {px:.1f} {py:.1f})" fill="{fill}"/>')
            nx, ny = cx + 52 * math.cos(a), cy - 52 * math.sin(a)
            out.append(_t(nx, ny + 5, p + 1, 12))
        out.append(_t(cx, 152, lab, 13, fill='#dc2626'))
        if i:
            out.append(f'<circle cx="{cx}" cy="{cy}" r="44" fill="none" stroke="#dc2626" stroke-dasharray="5 4"/>')
        if i < 4:
            out.append(f'<path d="M{cx + 50} 20 h18" stroke="#db2777" stroke-width="2"/><path d="M{cx + 70} 20 l-7 -4 v8 z" fill="#db2777"/>')
    return f'<svg viewBox="0 0 600 160" width="560" role="img" aria-label="A four-petal flower rotated by 0, 90, 180, 270 and 360 degrees" {FONT}>' + ''.join(out) + '</svg>'


def rotseq(spec):
    """'rhombus' -> rhombus turned 0°, 90°, 180°, 270°, 360° (two coloured corner dots show the turn);
    'arrow' -> upward arrow turned 0°, 90°, 180°, 270°, 360°."""
    kind = spec.strip()
    out = []
    for i in range(5):
        cx, cy = 60 + i * 120, 70
        rot = 90 * i
        if kind == 'rhombus':
            shape = (f'<polygon points="{cx - 52},{cy} {cx},{cy - 26} {cx + 52},{cy} {cx},{cy + 26}" fill="#fed7aa" stroke="#0f172a" stroke-width="1.6"/>'
                     f'<circle cx="{cx - 42}" cy="{cy}" r="4" fill="#22d3ee"/><circle cx="{cx + 42}" cy="{cy}" r="4" fill="#ec4899"/>')
        else:
            shape = f'<path d="M{cx} {cy - 45} L{cx + 30} {cy - 12} H{cx + 12} V{cy + 45} H{cx - 12} V{cy - 12} H{cx - 30} Z" fill="#38bdf8" stroke="#1e3a8a" stroke-width="1.5"/>'
        out.append(f'<g transform="rotate({rot} {cx} {cy})">{shape}</g>')
        out.append(_t(cx, 140, f'{rot}°', 13, fill='#dc2626'))
        if i < 4:
            out.append(f'<path d="M{cx + 50} 125 h18" stroke="#db2777" stroke-width="2"/><path d="M{cx + 70} 125 l-7 -4 v8 z" fill="#db2777"/>')
    return f'<svg viewBox="0 0 600 150" width="560" role="img" aria-label="Shape turned through 0, 90, 180, 270 and 360 degrees" {FONT}>' + ''.join(out) + '</svg>'


def rotshapes(spec):
    """Try Yourself shapes: an hourglass (two triangles meeting at a point) and a trapezium."""
    out = ['<polygon points="20,10 90,10 55,60 90,110 20,110 55,60" fill="#fef9c3" stroke="#0f172a" stroke-width="2"/>',
           '<polygon points="120,15 210,15 200,110 130,110" fill="#14b8a6" stroke="#0f172a" stroke-width="2"/>']
    return f'<svg viewBox="0 0 230 125" width="220" role="img" aria-label="An hourglass shape and a trapezium" {FONT}>' + ''.join(out) + '</svg>'


def symgrid(spec):
    """6 x 6 grid with a horizontal and a vertical line of symmetry through the centre (Try It! colouring grid)."""
    c = 24
    out = []
    for r in range(6):
        for k in range(6):
            out.append(f'<rect x="{30 + k * c}" y="{20 + r * c}" width="{c}" height="{c}" fill="#fff" stroke="#0f172a" stroke-width="1.2"/>')
    out.append(f'<line x1="102" y1="5" x2="102" y2="179" stroke="#be123c" stroke-width="2"/><line x1="12" y1="92" x2="192" y2="92" stroke="#be123c" stroke-width="2"/>')
    out.append('<path d="M102 3 l-5 9 h10 z M102 181 l-5 -9 h10 z M10 92 l9 -5 v10 z M194 92 l-9 -5 v10 z" fill="#be123c"/>')
    return f'<svg viewBox="0 0 205 185" width="200" role="img" aria-label="Six by six grid with horizontal and vertical lines of symmetry" {FONT}>' + ''.join(out) + '</svg>'


_SHP = {
    'isotrap': ('<polygon points="25,15 95,15 110,95 10,95" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#f472b6'),
    'pentagon': ('<polygon points="60,8 112,46 92,106 28,106 8,46" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#f9a8d4'),
    'irrpent': ('<polygon points="15,30 70,5 105,35 118,95 20,115" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#5f9ea0'),
    'arch': ('<path d="M10 100 A50 50 0 0 1 110 100" fill="none" stroke="{c}" stroke-width="7"/>', '#e879f9'),
    'isotri': ('<polygon points="60,5 105,110 15,110" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#86efac'),
    'H': ('<path d="M25 10 H45 V50 H75 V10 H95 V110 H75 V68 H45 V110 H25 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#fef08a'),
    'umbrella': ('<path d="M10 55 Q60 -5 110 55 Q97 47 85 55 Q72 47 60 55 Q48 47 35 55 Q22 47 10 55 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/><path d="M60 55 V105 Q60 115 52 113" fill="none" stroke="#0f172a" stroke-width="3"/>', '#a78bfa'),
    'A': ('<path d="M10 110 L48 10 H72 L110 110 H88 L80 86 H40 L32 110 Z M46 68 H74 L60 30 Z" fill="{c}" fill-rule="evenodd" stroke="#0f172a" stroke-width="1.5"/>', '#e879f9'),
    'I': ('<path d="M25 10 H95 V28 H70 V92 H95 V110 H25 V92 H50 V28 H25 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#0d9488'),
    'arrowR': ('<path d="M5 45 H75 V25 L115 60 L75 95 V75 H5 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#22d3ee'),
    'diamond': ('<polygon points="60,5 115,60 60,115 5,60" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#e11d48'),
    'cross4': ('<path d="M60 3 L72 20 H65 V53 H98 V46 L117 60 L98 74 V67 H65 V100 H72 L60 117 L48 100 H55 V67 H22 V74 L3 60 L22 46 V53 H55 V20 H48 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#e879f9'),
    'trap': ('<polygon points="25,20 95,20 110,100 10,100" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#1e1b4b'),
    'star4': ('<polygon points="60,3 72,48 117,60 72,72 60,117 48,72 3,60 48,48" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#f43f5e'),
    'zshape': ('<path d="M10 10 H70 V60 H110 V110 H50 V60 H10 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#4f46e5'),
}


def shape(spec):
    """'pentagon [| line=v|h|both|none] [| centre]' -> one preset shape (see _SHP), optionally with lines of symmetry and centre dot."""
    parts = [p.strip() for p in spec.split('|')]
    body, col = _SHP[parts[0]]
    out = [body.format(c=col)]
    for p in parts[1:]:
        if p.startswith('line='):
            v = p[5:]
            if v in ('v', 'both'):
                out.append('<line x1="60" y1="0" x2="60" y2="120" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5 3"/>')
            if v in ('h', 'both'):
                out.append('<line x1="0" y1="60" x2="120" y2="60" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5 3"/>')
        if p == 'centre':
            out.append('<circle cx="60" cy="60" r="4" fill="#dc2626"/>')
    return f'<svg viewBox="0 0 120 120" width="110" role="img" aria-label="{escape(parts[0])}" {FONT}>' + ''.join(out) + '</svg>'


_PIPS = {1: [(.5, .5)], 2: [(.25, .75), (.75, .25)], 3: [(.2, .8), (.5, .5), (.8, .2)], 4: [(.25, .25), (.75, .25), (.25, .75), (.75, .75)],
         5: [(.25, .25), (.75, .25), (.5, .5), (.25, .75), (.75, .75)], 6: [(.3, .2), (.7, .2), (.3, .5), (.7, .5), (.3, .8), (.7, .8)]}


def net(spec):
    """Net of a solid on a grid of squares. 'r,c[:pips] r,c[:pips] ... [| labels=Top@r,c;Bottom@r,c] [| fill=#hex]'
    Each token is a unit square at row r, column c (0-based); optional dice pips 1-6 drawn inside."""
    parts = [p.strip() for p in spec.split('|')]
    cells = []
    for tok in parts[0].split():
        rc, _, pip = tok.partition(':')
        r, c = (int(v) for v in rc.split(','))
        cells.append((r, c, pip[1:] if pip.startswith('#') else (int(pip) if pip else 0)))
    kv = dict(p.split('=', 1) for p in parts[1:] if '=' in p)
    fill = kv.get('fill', '#fff')
    s = 46
    R = max(r for r, _, _ in cells) + 1
    C = max(c for _, c, _ in cells) + 1
    out = []
    for r, c, pip in cells:
        x, y = 10 + c * s, 10 + r * s
        out.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{fill}" stroke="#0f172a" stroke-width="1.6"/>')
        if isinstance(pip, str):
            out.append(_t(x + s / 2, y + s / 2 + 5, pip, 15))
            continue
        for px, py in _PIPS.get(pip, []):
            out.append(f'<circle cx="{x + px * s:.1f}" cy="{y + py * s:.1f}" r="4" fill="#0f172a"/>')
    H = 20 + R * s
    for lab in [l for l in kv.get('labels', '').split(';') if l]:
        name, _, rc = lab.partition('@')
        r, c = (int(v) for v in rc.split(','))
        out.append(_t(10 + c * s + s / 2, 10 + (r + 1) * s + 18, name, 13))
        H = max(H, 10 + (r + 1) * s + 26)
    W = 20 + C * s
    return f'<svg viewBox="0 0 {W} {H}" width="{min(W, 320)}" role="img" aria-label="Net made of {len(cells)} squares" {FONT}>' + ''.join(out) + '</svg>'


def box3d(spec):
    """'W H D | front=5 top=2 right=1 back=3 left=4 bottom=6 | fill=#fde68a' -> oblique drawing of a cube/cuboid;
    hidden edges dashed; face numbers written on visible faces and (smaller) for hidden faces."""
    parts = [p.strip() for p in spec.split('|')]
    W, H, D = (float(v) for v in parts[0].split())
    kv = {}
    for p in parts[1:]:
        for tok in p.split():
            if '=' in tok:
                k, v = tok.split('=', 1)
                kv[k] = v
    s = 40
    w, h, d = W * s, H * s, D * s * 0.5
    x0, y0 = 20, 20 + d
    fx, fy = x0, y0
    dx, dy = d, -d
    fill = kv.get('fill', '#fde68a')
    out = [f'<polygon points="{fx},{fy} {fx + w},{fy} {fx + w},{fy + h} {fx},{fy + h}" fill="{fill}" fill-opacity="0.9" stroke="#0f172a" stroke-width="1.6"/>',
           f'<polygon points="{fx},{fy} {fx + dx},{fy + dy} {fx + w + dx},{fy + dy} {fx + w},{fy}" fill="{fill}" fill-opacity="0.6" stroke="#0f172a" stroke-width="1.6"/>',
           f'<polygon points="{fx + w},{fy} {fx + w + dx},{fy + dy} {fx + w + dx},{fy + h + dy} {fx + w},{fy + h}" fill="{fill}" fill-opacity="0.75" stroke="#0f172a" stroke-width="1.6"/>']
    bx, by = fx + dx, fy + h + dy
    out.append(f'<path d="M{bx} {by} L{fx} {fy + h} M{bx} {by} H{bx + w} M{bx} {by} V{fy + dy}" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="5 4" fill="none"/>')
    lab = lambda x, y, k, sz=15: _t(x, y, kv[k], sz) if k in kv else ''
    out.append(lab(fx + w / 2, fy + h / 2 + 5, 'front'))
    out.append(lab(fx + w / 2 + dx / 2, fy + dy / 2 + 5, 'top'))
    out.append(lab(fx + w + dx / 2, fy + h / 2 + dy / 2 + 5, 'right'))
    out.append(lab(fx + dx / 2 + 6, fy + h / 2 + dy / 2 + 5, 'back', 12))
    out.append(lab(fx + 10, fy + h / 2 + 5, 'left', 12))
    out.append(lab(fx + w / 2 + dx / 2, fy + h + dy / 2 + 5, 'bottom', 12))
    Wt, Ht = w + d + 40, h + d + 40
    return f'<svg viewBox="0 0 {Wt:.0f} {Ht:.0f}" width="{min(Wt, 300):.0f}" role="img" aria-label="Solid with numbered faces" {FONT}>' + ''.join(o for o in out if o) + '</svg>'


_SHP.update({
    'righttri': ('<polygon points="10,25 110,95 10,95" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#0ea5e9'),
    'notchrect': ('<path d="M20 25 H100 Q100 35 110 35 V85 Q100 85 100 95 H20 Q20 85 10 85 V35 Q20 35 20 25 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#fef08a'),
    'chevron': ('<polygon points="5,25 80,25 115,60 80,95 5,95 40,60" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#10b981'),
    'divide': ('<rect x="5" y="52" width="110" height="16" fill="{c}" stroke="#0f172a" stroke-width="1"/><circle cx="60" cy="28" r="10" fill="{c}" stroke="#0f172a"/><circle cx="60" cy="92" r="10" fill="{c}" stroke="#0f172a"/>', '#f472b6'),
    'xcross': ('<path d="M20 5 L60 45 L100 5 L115 20 L75 60 L115 100 L100 115 L60 75 L20 115 L5 100 L45 60 L5 20 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#ef4444'),
    'plusarrows': ('<path d="M48 5 H72 V45 H95 V35 L115 60 L95 85 V75 H72 V115 H48 V75 H25 V85 L5 60 L25 35 V45 H48 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#db2777'),
    'wave': ('<path d="M5 45 Q35 20 60 45 T115 40 V80 Q85 105 60 80 T5 85 Z" fill="{c}" stroke="#0f172a" stroke-width="1.5"/>', '#7c3aed'),
})


_BARCOL = ['#06b6d4', '#10b981', '#ef4444', '#ec4899', '#3b5bdb', '#f59e0b', '#8b5cf6', '#84cc16']


def bars(spec):
    """Bar graph on squared paper. 'January=18; February=19; ... | max=40 | step=10 | sq=5 | x=Months | y=Average Temperature
    | unit=° | scale=Scale: 1 square = 5°C | horiz'  ('horiz' draws horizontal bars)."""
    parts = [p.strip() for p in spec.split('|')]
    data = [(k.strip(), float(v)) for k, v in (x.split('=') for x in parts[0].split(';') if x.strip())]
    kv = {}
    flags = set()
    for p in parts[1:]:
        if '=' in p:
            k, v = p.split('=', 1); kv[k.strip()] = v.strip()
        else:
            flags.add(p)
    mx, step = float(kv.get('max', 40)), float(kv.get('step', 10))
    sqv = float(kv.get('sq', step / 2))
    unit = kv.get('unit', '')
    horiz = 'horiz' in flags
    n = len(data)
    out = []
    if not horiz:
        x0, y0, H = 70, 250, 200
        cw = 56
        W = cw * n + 20
        k = H / mx
        for i in range(int(mx / sqv) + 1):
            y = y0 - i * sqv * k
            out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + W}" y2="{y:.1f}" stroke="#94a3b8" stroke-width="0.8"/>')
        for i in range(int(W / (cw / 2)) + 1):
            x = x0 + i * cw / 2
            out.append(f'<line x1="{x:.1f}" y1="{y0 - H}" x2="{x:.1f}" y2="{y0}" stroke="#94a3b8" stroke-width="0.8"/>')
        t = 0
        while t <= mx + 1e-9:
            out.append(_t(x0 - 8, y0 - t * k + 4, f'{t:g}{unit}', 12, anchor='end'))
            t += step
        for i, (lab, v) in enumerate(data):
            x = x0 + 10 + i * cw
            out.append(f'<rect x="{x + 8}" y="{y0 - v * k:.1f}" width="{cw - 26}" height="{v * k:.1f}" fill="{_BARCOL[i % len(_BARCOL)]}" stroke="#0f172a"/>')
            out.append(_t(x + cw / 2 - 5, y0 + 16, lab, 11))
        out.append(f'<path d="M{x0} {y0 - H - 15} V{y0} H{x0 + W + 12}" fill="none" stroke="#0f172a" stroke-width="1.6"/>')
        out.append(_t(x0 + W / 2, y0 + 36, kv.get('x', ''), 13))
        out.append(f'<text x="18" y="{y0 - H / 2}" font-size="13" text-anchor="middle" fill="#be123c" transform="rotate(-90 18 {y0 - H / 2})">{escape(kv.get("y", ""))}</text>')
        if kv.get('scale'):
            out.append(f'<rect x="{x0 + W - 150}" y="{y0 - H - 34}" width="150" height="22" fill="#334155"/>' + _t(x0 + W - 75, y0 - H - 18, kv['scale'], 12, fill='#fff'))
        Wt, Ht = x0 + W + 30, y0 + 46
    else:
        x0, y0, Wd = 120, 30, 320
        rh = 34
        Hh = rh * n + 10
        k = Wd / mx
        for i in range(int(mx / sqv) + 1):
            x = x0 + i * sqv * k
            out.append(f'<line x1="{x:.1f}" y1="{y0}" x2="{x:.1f}" y2="{y0 + Hh}" stroke="#94a3b8" stroke-width="0.8"/>')
        for i in range(n * 2 + 1):
            y = y0 + i * rh / 2
            out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + Wd}" y2="{y:.1f}" stroke="#94a3b8" stroke-width="0.8"/>')
        t = 0
        while t <= mx + 1e-9:
            out.append(_t(x0 + t * k, y0 + Hh + 16, f'{t:g}{unit}', 12))
            t += step
        for i, (lab, v) in enumerate(data):
            y = y0 + 5 + i * rh
            out.append(f'<rect x="{x0}" y="{y + 4}" width="{v * k:.1f}" height="{rh - 14}" fill="{_BARCOL[i % len(_BARCOL)]}" stroke="#0f172a"/>')
            out.append(_t(x0 - 8, y + rh / 2 + 2, lab, 12, anchor='end'))
        out.append(f'<path d="M{x0} {y0 - 10} V{y0 + Hh} H{x0 + Wd + 12}" fill="none" stroke="#0f172a" stroke-width="1.6"/>')
        out.append(_t(x0 + Wd / 2, y0 + Hh + 36, kv.get('x', ''), 13))
        out.append(_t(60, y0 - 12, kv.get('y', ''), 13, fill='#be123c'))
        if kv.get('scale'):
            out.append(f'<rect x="{x0 + Wd - 160}" y="{y0 - 28}" width="160" height="20" fill="#334155"/>' + _t(x0 + Wd - 80, y0 - 14, kv['scale'], 12, fill='#fff'))
        Wt, Ht = x0 + Wd + 30, y0 + Hh + 46
    return f'<svg viewBox="0 0 {Wt:.0f} {Ht:.0f}" width="{min(Wt, 460):.0f}" role="img" aria-label="Bar graph: {escape(", ".join(f"{a} {b:g}" for a, b in data))}" {FONT}>' + ''.join(out) + '</svg>'
