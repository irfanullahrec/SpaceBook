"""Class 8 Mathematics: Cartesian plane with gridlines, lines/segments and labelled points."""
from html import escape


def _n(v):
    return f'{round(v, 4):g}'.replace('-', '−')


def plane(spec):
    """'x=-8..8 | y=-8..8 | step=2 | lines=m,c,x1,x2;... | segs=x1,y1,x2,y2;... | vlines=x,y1,y2;... | pts=x,y:label;...
       | labels=text@x,y;... | noarrows'
    lines: y = m x + c drawn from x1 to x2 with arrowheads; segs: plain segments with arrowheads;
    vlines: vertical line x from y1 to y2; pts: dots with an optional label; labels: free text at a point."""
    o = {'x': (-8, 8), 'y': (-8, 8), 'step': 2, 'lines': [], 'segs': [], 'vlines': [], 'hlines': [], 'pts': [], 'labels': [], 'arrows': True}
    for p in [t.strip() for t in spec.split('|') if t.strip()]:
        k, _, v = p.partition('=')
        k = k.strip()
        if k in ('x', 'y'):
            a, b = v.split('..')
            o[k] = (float(a), float(b))
        elif k == 'step':
            o['step'] = float(v)
        elif k in ('lines', 'segs', 'vlines', 'hlines'):
            o[k] = [[float(t) for t in q.split(',')] for q in v.split(';') if q.strip()]
        elif k == 'pts':
            for q in v.split(';'):
                xy, _, lab = q.partition(':')
                a, b = xy.split(',')
                o['pts'].append((float(a), float(b), lab.strip()))
        elif k == 'labels':
            for q in v.split(';'):
                t, _, xy = q.rpartition('@')
                a, b = xy.split(',')
                o['labels'].append((t, float(a), float(b)))
        elif k == 'noarrows':
            o['arrows'] = False
        elif k == 'tri':
            o['tri'] = [[float(t) for t in q.split(',')] for q in v.split(';')]
        else:
            raise ValueError('plane: unknown option ' + k)
    (xa, xb), (ya, yb) = o['x'], o['y']
    u = max(14, min(22, 340 / max(xb - xa, yb - ya)))
    L, T = 30, 24
    X = lambda v: L + (v - xa) * u
    Y = lambda v: T + (yb - v) * u
    W, H = X(xb) + 30, Y(ya) + 24
    out = ['<defs><marker id="plA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0f172a"/></marker>'
           '<marker id="plB" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1d4ed8"/></marker></defs>']
    v = xa
    while v <= xb + 1e-9:
        out.append(f'<line x1="{X(v):.1f}" y1="{Y(yb):.1f}" x2="{X(v):.1f}" y2="{Y(ya):.1f}" stroke="#cbd5e1" stroke-width="0.8"/>')
        v += 1
    v = ya
    while v <= yb + 1e-9:
        out.append(f'<line x1="{X(xa):.1f}" y1="{Y(v):.1f}" x2="{X(xb):.1f}" y2="{Y(v):.1f}" stroke="#cbd5e1" stroke-width="0.8"/>')
        v += 1
    out.append(f'<line x1="{X(xa) - 10:.1f}" y1="{Y(0):.1f}" x2="{X(xb) + 12:.1f}" y2="{Y(0):.1f}" stroke="#0f172a" stroke-width="1.4" marker-start="url(#plA)" marker-end="url(#plA)"/>')
    out.append(f'<line x1="{X(0):.1f}" y1="{Y(ya) + 10:.1f}" x2="{X(0):.1f}" y2="{Y(yb) - 12:.1f}" stroke="#0f172a" stroke-width="1.4" marker-start="url(#plA)" marker-end="url(#plA)"/>')
    out.append(f'<text x="{X(xb) + 16:.1f}" y="{Y(0) + 4:.1f}" font-size="12" font-style="italic">x</text>')
    out.append(f'<text x="{X(0) - 4:.1f}" y="{Y(yb) - 14:.1f}" font-size="12" font-style="italic">y</text>')
    s = o['step']
    v = xa
    while v <= xb + 1e-9:
        if abs(v) > 1e-9:
            out.append(f'<text x="{X(v):.1f}" y="{Y(0) + 13:.1f}" text-anchor="middle" font-size="10">{_n(v)}</text>')
        v += s
    v = ya
    while v <= yb + 1e-9:
        if abs(v) > 1e-9:
            out.append(f'<text x="{X(0) - 4:.1f}" y="{Y(v) + 3.5:.1f}" text-anchor="end" font-size="10">{_n(v)}</text>')
        v += s
    out.append(f'<text x="{X(0) - 4:.1f}" y="{Y(0) + 13:.1f}" text-anchor="end" font-size="10">0</text>')
    if o.get('tri'):
        out.append('<polygon points="' + ' '.join(f'{X(a):.1f},{Y(b):.1f}' for a, b in o['tri']) + '" fill="#f9a8d4" fill-opacity="0.7" stroke="#be185d" stroke-width="1"/>')
    mk = ' marker-start="url(#plB)" marker-end="url(#plB)"' if o['arrows'] else ''
    for m, c, x1, x2 in o['lines']:
        out.append(f'<line x1="{X(x1):.1f}" y1="{Y(m * x1 + c):.1f}" x2="{X(x2):.1f}" y2="{Y(m * x2 + c):.1f}" stroke="#1d4ed8" stroke-width="1.8"{mk}/>')
    for x1, y1, x2, y2 in o['segs']:
        out.append(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2):.1f}" y2="{Y(y2):.1f}" stroke="#1d4ed8" stroke-width="1.8"{mk}/>')
    for x0, y1, y2 in o['vlines']:
        out.append(f'<line x1="{X(x0):.1f}" y1="{Y(y1):.1f}" x2="{X(x0):.1f}" y2="{Y(y2):.1f}" stroke="#1d4ed8" stroke-width="1.8"{mk}/>')
    for y0, x1, x2 in o.get('hlines', []):
        out.append(f'<line x1="{X(x1):.1f}" y1="{Y(y0):.1f}" x2="{X(x2):.1f}" y2="{Y(y0):.1f}" stroke="#1d4ed8" stroke-width="1.8"{mk}/>')
    for px, py, lab in o['pts']:
        out.append(f'<circle cx="{X(px):.1f}" cy="{Y(py):.1f}" r="3.5" fill="#dc2626"/>')
        if lab:
            out.append(f'<text x="{X(px) + 6:.1f}" y="{Y(py) - 6:.1f}" font-size="11" font-weight="700" fill="#991b1b">{escape(lab)}</text>')
    for t, px, py in o['labels']:
        out.append(f'<text x="{X(px):.1f}" y="{Y(py):.1f}" font-size="12" font-weight="700" fill="#1e3a8a">{escape(t)}</text>')
    desc = [f'y = {_n(m)}x + {_n(c)}' for m, c, *_ in o['lines']] + [f'segment ({_n(a)}, {_n(b)}) to ({_n(c)}, {_n(d)})' for a, b, c, d in o['segs']] \
        + [f'x = {_n(a)}' for a, *_ in o['vlines']] + [f'y = {_n(a)}' for a, *_ in o['hlines']] + [f'point ({_n(a)}, {_n(b)}) {l}' for a, b, l in o['pts']]
    label = 'Coordinate plane; ' + '; '.join(desc)
    return f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'
