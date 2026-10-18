"""Class 8 Mathematics: gridded graphs and proportion arrow tables."""
import re
from html import escape


def _num(v):
    return f'{round(v, 6):g}'.replace('-', '−')


def graph(spec):
    """Gridded graph. 'x=0..4.5:0.5 | y=0..9:1 | xl=Number of days | yl=Number of pages | pts=0,0;1,2 | line | curve | labels'
    x/y: range and grid step ('xn='/'yn=' change the axis-number step).  pts: plotted points.
    line: straight segments through pts; curve: smooth path through pts; labels: write (x, y) beside points."""
    parts = [p.strip() for p in spec.split('|')]
    o = {'xl': '', 'yl': '', 'pts': [], 'line': False, 'curve': False, 'labels': False, 'xn': None, 'yn': None}
    for p in parts:
        k, _, v = p.partition('=')
        k = k.strip()
        if k in ('x', 'y'):
            r, _, st = v.partition(':')
            a, b = [float(t) for t in r.split('..')]
            o[k] = (a, b, float(st or 1))
        elif k in ('xn', 'yn'):
            o[k] = float(v)
        elif k in ('xl', 'yl'):
            o[k] = v.strip()
        elif k == 'pts':
            o['pts'] = [tuple(float(t) for t in q.split(',')) for q in v.split(';')]
        elif k in ('line', 'curve', 'labels'):
            o[k] = True
        else:
            raise ValueError('graph: unknown option ' + k)
    (xa, xb, xs), (ya, yb, ys) = o['x'], o['y']
    nx, ny = round((xb - xa) / xs), round((yb - ya) / ys)
    cw = max(26, min(56, 460 / nx))
    ch = max(18, min(34, 300 / ny))
    L, T = 58, 18
    W, H = nx * cw, ny * ch
    X = lambda v: L + (v - xa) / xs * cw
    Y = lambda v: T + H - (v - ya) / ys * ch
    out = [f'<rect x="{L}" y="{T}" width="{W:.1f}" height="{H:.1f}" fill="#fff" stroke="#94a3b8"/>']
    for i in range(nx + 1):
        out.append(f'<line x1="{L + i * cw:.1f}" y1="{T}" x2="{L + i * cw:.1f}" y2="{T + H:.1f}" stroke="#cbd5e1"/>')
    for j in range(ny + 1):
        out.append(f'<line x1="{L}" y1="{T + j * ch:.1f}" x2="{L + W:.1f}" y2="{T + j * ch:.1f}" stroke="#cbd5e1"/>')
    out.append(f'<line x1="{L}" y1="{T + H:.1f}" x2="{L + W + 14:.1f}" y2="{T + H:.1f}" stroke="#0f172a" stroke-width="1.4"/>')
    out.append(f'<line x1="{L}" y1="{T + H:.1f}" x2="{L}" y2="{T - 10}" stroke="#0f172a" stroke-width="1.4"/>')
    out.append(f'<text x="{L + W + 18:.1f}" y="{T + H + 4:.1f}" font-size="12" font-style="italic">x</text>'
               f'<text x="{L - 4}" y="{T - 12}" font-size="12" font-style="italic">y</text>')
    xn, yn = o['xn'] or xs, o['yn'] or ys
    v = xa
    while v <= xb + 1e-9:
        out.append(f'<text x="{X(v):.1f}" y="{T + H + 16:.1f}" text-anchor="middle" font-size="11">{_num(v)}</text>')
        v += xn
    v = ya
    while v <= yb + 1e-9:
        out.append(f'<text x="{L - 6}" y="{Y(v) + 4:.1f}" text-anchor="end" font-size="11">{_num(v)}</text>')
        v += yn
    pts = o['pts']
    if o['line'] and len(pts) > 1:
        out.append('<polyline points="' + ' '.join(f'{X(a):.1f},{Y(b):.1f}' for a, b in pts) + '" fill="none" stroke="#1d4ed8" stroke-width="2"/>')
    if o['curve'] and len(pts) > 1:
        P = [(X(a), Y(b)) for a, b in pts]
        d = f'M{P[0][0]:.1f} {P[0][1]:.1f}'
        for i in range(len(P) - 1):
            p0 = P[i - 1] if i else P[i]
            p1, p2 = P[i], P[i + 1]
            p3 = P[i + 2] if i + 2 < len(P) else p2
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
        out.append(f'<path d="{d}" fill="none" stroke="#1d4ed8" stroke-width="2"/>')
    for a, b in pts:
        out.append(f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="3.6" fill="#1d4ed8"/>')
        if o['labels']:
            out.append(f'<text x="{X(a) + 6:.1f}" y="{Y(b) - 6:.1f}" font-size="10" fill="#1e3a8a">({_num(a)}, {_num(b)})</text>')
    out.append(f'<text x="{L + W / 2:.1f}" y="{T + H + 36:.1f}" text-anchor="middle" font-size="13">{escape(o["xl"])}</text>')
    out.append(f'<text transform="translate(16 {T + H / 2:.1f}) rotate(-90)" text-anchor="middle" font-size="13">{escape(o["yl"])}</text>')
    w, h = L + W + 30, T + H + 46
    label = f'Graph of {o["yl"] or "y"} against {o["xl"] or "x"}; points ' + ', '.join(f'({_num(a)}, {_num(b)})' for a, b in pts)
    return f'<svg viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def ptab(spec):
    """Proportion arrow table. 'Rupees : Days | 43000 : 25 | x : 4 | up, down'
    First part: column headings; then the rows; last part: arrow direction per column (up / down / none)."""
    parts = [p.strip() for p in spec.split('|')]
    heads = [h.strip() for h in parts[0].split(':')]
    dirs = [d.strip() for d in parts[-1].split(',')]
    rows = [[c.strip() for c in r.split(':')] for r in parts[1:-1]]
    cw, rh = 150, 22
    w = cw * len(heads) + 10
    h = 26 + rh * len(rows) + 6
    out = []
    for i, hd in enumerate(heads):
        cx = 10 + cw * i + cw / 2
        out.append(f'<text x="{cx}" y="16" text-anchor="middle" font-size="14" font-weight="700">{escape(hd)}</text>')
        if i < len(heads) - 1:
            for j in range(len(rows) + 1):
                out.append(f'<text x="{10 + cw * (i + 1)}" y="{16 + rh * j}" text-anchor="middle" font-size="14">:</text>')
        for j, r in enumerate(rows):
            v = r[i]
            it = ' font-style="italic"' if re.fullmatch(r'[a-z]', v) else ''
            out.append(f'<text x="{cx}" y="{38 + rh * j}" text-anchor="middle" font-size="14"{it}>{escape(v.replace("-", "−"))}</text>')
        d = dirs[i] if i < len(dirs) else 'none'
        if d in ('up', 'down'):
            ax = cx + (-38 if i == 0 else 38)
            y1, y2 = 24, 24 + rh * len(rows)
            tip, base = (y1, y2) if d == 'up' else (y2, y1)
            s = 1 if d == 'up' else -1
            out.append(f'<line x1="{ax}" y1="{base}" x2="{ax}" y2="{tip}" stroke="#0f172a" stroke-width="1.4"/>'
                       f'<path d="M{ax - 4} {tip + 6 * s} L{ax} {tip} L{ax + 4} {tip + 6 * s}" fill="none" stroke="#0f172a" stroke-width="1.4"/>')
    label = 'Proportion table ' + ' : '.join(heads) + '; ' + '; '.join(' : '.join(r) for r in rows) + '; arrows ' + ', '.join(dirs)
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def pdiv(spec):
    """Polynomial long division. 'd=2x | q=7x³ + 13x² − 6x − 3 | n=14x⁴ + 26x³ − 12x² − 6x | -±14x⁴ | 26x³ − 12x² − 6x | ...'
    d: divisor, q: quotient, n: dividend; each later part is one working row, right-aligned to the dividend's
    right edge; trailing '_' shift it left by one character; a row starting with '-' is a subtraction (underlined,
    the '-' itself is not drawn)."""
    parts = [p.strip() for p in spec.split('|')]
    d = q = n = ''
    rows = []
    for p in parts:
        if p.startswith('d='):
            d = p[2:].strip()
        elif p.startswith('q='):
            q = p[2:].strip()
        elif p.startswith('n='):
            n = p[2:].strip()
        else:
            rows.append(p)
    cw, rh = 8.6, 22
    mono = 'font-family="Consolas, Menlo, monospace"'
    L = len(d) * cw + 16
    span = max([len(n), len(q)] + [len(r.partition('>>')[0].rstrip().lstrip('-')) for r in rows])
    W = L + (span + 2) * cw + 16
    R = L + 8 + span * cw
    out = [f'<text x="{R:.1f}" y="18" text-anchor="end" font-size="14" {mono}>{escape(q)}</text>',
           f'<line x1="{L}" y1="24" x2="{R + 8:.1f}" y2="24" stroke="#0f172a" stroke-width="1.3"/>',
           f'<text x="{L - 6:.1f}" y="42" text-anchor="end" font-size="14" {mono}>{escape(d)}</text>',
           f'<text x="{R:.1f}" y="42" text-anchor="end" font-size="14" {mono}>{escape(n)}</text>']
    y = 42
    notes = any('>>' in r for r in rows)
    for r in rows:
        r, _, note = r.partition('>>')
        r, note = r.rstrip(), note.strip()
        pad = len(r) - len(r.rstrip('_'))
        r = r.rstrip('_')
        sub = r.startswith('-')
        if sub:
            r = r[1:]
        y += rh
        xe = R - pad * cw
        out.append(f'<text x="{xe:.1f}" y="{y}" text-anchor="end" font-size="14" {mono}>{escape(r)}</text>')
        if sub:
            out.append(f'<line x1="{xe - len(r) * cw - 4:.1f}" y1="{y + 6}" x2="{xe + 4:.1f}" y2="{y + 6}" stroke="#0f172a" stroke-width="1.2"/>')
        if note:
            out.append(f'<text x="{R + 18:.1f}" y="{y}" font-size="13" fill="#334155">{escape(note)}</text>')
    if notes:
        W += 150
    h = y + 14
    out.append(f'<path d="M{L} 24 q-6 10 -6 22" fill="none" stroke="#0f172a" stroke-width="1.3"/>')
    label = f'Long division of {n} by {d}; quotient {q}'
    return f'<svg viewBox="0 0 {W:.0f} {h}" width="{W:.0f}" role="img" aria-label="{escape(label)}" fill="#0f172a">' + ''.join(out) + '</svg>'


def sqdiv(spec):
    """Square root by long division. 'q=486 | n=23 61 96 | 4: | :-16____ | 88:761__ | :-704__ | 966:5796 | :-5796 | :0'
    q: quotient written above; n: radicand, space-separated digit pairs (each pair gets a bar).
    Remaining parts are 'divisor:text' rows; trailing '_' shift the text left by one digit column each,
    a text starting with '-' is a subtraction and is underlined."""
    parts = [p.strip() for p in spec.split('|')]
    q = n = ''
    rows = []
    extra = 0
    for p in parts:
        if p.startswith('x='):
            extra = int(p[2:])
        elif p.startswith('q='):
            q = p[2:].strip()
        elif p.startswith('n='):
            n = p[2:].strip()
        else:
            d, _, t = p.partition(':')
            rows.append((d.strip(), t))
    groups = n.split()
    cols = sum(len(g.replace('.', '')) for g in groups) + extra
    cw, rh = 11, 22
    dw = max([len(d) for d, _ in rows] + [1]) * 10 + 14
    L = dw + 8
    W = L + (cols + 1) * cw + 26
    R = L + 10 + (cols + 1) * cw
    mono = 'font-family="Consolas, Menlo, monospace"'
    out = []
    y = 18
    qpad = len(q) - len(q.rstrip('_'))
    q = q.rstrip('_')
    qd = len(q.replace('.', ''))
    out.append(f'<text x="{R - qpad * cw}" y="{y}" text-anchor="end" font-size="15" font-weight="700" {mono} textLength="{qd * cw}" lengthAdjust="spacingAndGlyphs">{escape(q)}</text>')
    y += 22
    x = L + 10 + cw
    for g in groups:
        digits = g.replace('.', '')
        txt_w = len(digits) * cw
        out.append(f'<text x="{x}" y="{y}" font-size="15" {mono} textLength="{txt_w}" lengthAdjust="spacingAndGlyphs">{escape(g)}</text>')
        out.append(f'<line x1="{x + 1}" y1="{y - 14}" x2="{x + txt_w - 1}" y2="{y - 14}" stroke="#0f172a" stroke-width="1"/>')
        x += txt_w
    out.append(f'<line x1="{L}" y1="{y - 18}" x2="{R + 6}" y2="{y - 18}" stroke="#0f172a" stroke-width="1.4"/>')
    first = True
    for d, t in rows:
        pad = len(t) - len(t.rstrip('_'))
        t = t.rstrip('_')
        if first and not t:
            out.append(f'<text x="{L - 8}" y="{y}" text-anchor="end" font-size="15" {mono}>{escape(d)}</text>')
            first = False
            continue
        first = False
        y += rh
        xe = R - pad * cw
        if d:
            out.append(f'<text x="{L - 8}" y="{y}" text-anchor="end" font-size="15" {mono}>{escape(d)}</text>')
        disp = t.replace('-', '−')
        out.append(f'<text x="{xe}" y="{y}" text-anchor="end" font-size="15" {mono} textLength="{len(disp) * cw}" lengthAdjust="spacingAndGlyphs">{escape(disp)}</text>')
        if t.startswith('-'):
            wdt = len(t) * cw + 2
            out.append(f'<line x1="{xe - wdt}" y1="{y + 6}" x2="{xe + 2}" y2="{y + 6}" stroke="#0f172a" stroke-width="1.2"/>')
    h = y + 12
    out.append(f'<line x1="{L}" y1="22" x2="{L}" y2="{h - 4}" stroke="#0f172a" stroke-width="1.4"/>')
    label = f'Square root of {n.replace(" ", "")} by division method; quotient {q}'
    return f'<svg viewBox="0 0 {W} {h}" width="{W}" role="img" aria-label="{escape(label)}" fill="#0f172a">' + ''.join(out) + '</svg>'
