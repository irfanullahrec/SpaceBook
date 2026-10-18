"""Class 8 Mathematics SVG generators (number lines with real values, etc.)."""
import re
import hashlib
from html import escape


def _lab(x, y, txt, size=14, anchor='middle', weight='400', color='#0f172a'):
    """SVG text; 'p/q' (optionally signed, optionally 'n p/q') is drawn as a stacked fraction."""
    m = re.fullmatch(r'([−-]?)(\d+ )?(√?\d+)/(\d+)', txt.strip())
    if not m:
        return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(txt)}</text>'
    sign, whole, num, den = m.groups()
    s = size - 2
    pre = (sign.replace('-', '−') if sign else '') + (whole.strip() if whole else '')
    wd = max(len(num), len(den)) * s * 0.62
    x = float(x)
    out = ''
    if pre:
        out += f'<text x="{x - wd / 2 - 2:.1f}" y="{y - 4}" text-anchor="end" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(pre)}</text>'
    out += (f'<text x="{x:.1f}" y="{y - s * .85:.1f}" text-anchor="middle" font-size="{s}" font-weight="{weight}" fill="{color}">{escape(num)}</text>'
            f'<line x1="{x - wd / 2:.1f}" y1="{y - s * .62:.1f}" x2="{x + wd / 2:.1f}" y2="{y - s * .62:.1f}" stroke="{color}" stroke-width="1"/>'
            f'<text x="{x:.1f}" y="{y + s * .45:.1f}" text-anchor="middle" font-size="{s}" font-weight="{weight}" fill="{color}">{escape(den)}</text>')
    return out


def rline(spec):
    """Real number line.
    'A..B | step=1 | minor=0.5 | plus | pts=v:label;v:label | top=a:b:text;... | brace=a:b:text;... | hops=a:b;... | hoplab=a:b:text | origin'
    pts: red dot at real value v with its label above ('p/q' stacked).  plus: '+' before positive tick labels.
    top: arrow above the line from a to b with a caption.  brace: brace below the line from a to b with a caption.
    hops: unit arcs under the line from a to b.  hoplab: boxed caption centred under a..b.  origin: arrow up to 0 labelled Origin."""
    parts = [p.strip() for p in spec.split('|')]
    a, b = [float(x) for x in parts[0].split('..')]
    opt = {'step': 1.0, 'minor': 0.0, 'plus': False, 'pts': [], 'top': [], 'brace': [], 'origin': False, 'hops': [], 'hoplab': [], 'ticklabels': True, 'only': None}
    for p in parts[1:]:
        k, _, v = p.partition('=')
        k = k.strip()
        if k in ('step', 'minor'):
            opt[k] = float(v)
        elif k in ('plus', 'origin'):
            opt[k] = True
        elif k == 'only':
            opt['only'] = [float(t) for t in v.split(',')]
        elif k == 'nolabels':
            opt['ticklabels'] = False
        elif k == 'pts':
            opt['pts'] = [(float(x.split(':', 1)[0]), x.split(':', 1)[1]) for x in v.split(';')]
        elif k in ('top', 'brace', 'hoplab'):
            opt[k] = [x.split(':', 2) for x in v.split(';')]
        elif k == 'hops':
            opt['hops'] = [tuple(float(t) for t in x.split(':')) for x in v.split(';')]
        else:
            raise ValueError('rline: unknown option ' + k)
    unit = max(22, min(60, 620 / max((b - a) / opt['step'], 1))) / opt['step']
    x0 = 30
    y = 34
    if opt['pts']:
        y += 34
    if opt['top']:
        y += 30
    X = lambda v: x0 + (v - a) * unit
    w = X(b) + 32
    mid = 'rl' + hashlib.md5(spec.encode()).hexdigest()[:8]
    out = [f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#1d4ed8"/></marker></defs>',
           f'<line x1="{x0 - 18}" y1="{y}" x2="{X(b) + 18:.1f}" y2="{y}" stroke="#0f172a" stroke-width="1.6"/>',
           f'<path d="M{x0 - 20} {y} l9 -5 v10 z" fill="#0f172a"/><path d="M{X(b) + 20:.1f} {y} l-9 -5 v10 z" fill="#0f172a"/>']
    if opt['minor']:
        v = a
        while v <= b + 1e-9:
            out.append(f'<line x1="{X(v):.1f}" y1="{y - 4}" x2="{X(v):.1f}" y2="{y + 4}" stroke="#0f172a" stroke-width="1"/>')
            v += opt['minor']
    v = a
    while v <= b + 1e-9:
        lab = f'{round(v, 6):g}'.replace('-', '−')
        if opt['plus'] and v > 0:
            lab = '+' + lab
        if opt['only'] is not None and not any(abs(v - t) < 1e-9 for t in opt['only']):
            v += opt['step']
            continue
        out.append(f'<line x1="{X(v):.1f}" y1="{y - 7}" x2="{X(v):.1f}" y2="{y + 7}" stroke="#0f172a" stroke-width="1.4"/>')
        if opt['ticklabels']:
            out.append(f'<text x="{X(v):.1f}" y="{y + 25}" text-anchor="middle" font-size="14">{escape(lab)}</text>')
        v += opt['step']
    for val, lab in opt['pts']:
        out.append(f'<circle cx="{X(val):.1f}" cy="{y}" r="4.5" fill="#dc2626"/>')
        out.append(f'<line x1="{X(val):.1f}" y1="{y - 8}" x2="{X(val):.1f}" y2="{y - 18}" stroke="#dc2626" stroke-width="1.2"/>')
        out.append(_lab(f'{X(val):.1f}', y - 24, lab, 14, color='#991b1b'))
    ty = y - (64 if opt['pts'] else 24)
    for s0, e0, txt in opt['top']:
        xa, xb = X(float(s0)), X(float(e0))
        out.append(f'<line x1="{xa:.1f}" y1="{ty}" x2="{xb:.1f}" y2="{ty}" stroke="#1d4ed8" stroke-width="1.6" marker-end="url(#{mid})"/>')
        out.append(f'<text x="{(xa + xb) / 2:.1f}" y="{ty - 8}" text-anchor="middle" font-size="13" font-weight="700" fill="#1e3a8a">{escape(txt)}</text>')
    hgt = y + 34
    if opt['hops']:
        for s0, e0 in opt['hops']:
            st = 1 if e0 > s0 else -1
            v = s0
            while (v - e0) * st < -1e-9:
                xa, xb = X(v), X(v + st)
                out.append(f'<path d="M{xa:.1f} {y + 32} Q{(xa + xb) / 2:.1f} {y + 46} {xb:.1f} {y + 32}" fill="none" stroke="#0f766e" stroke-width="1.5"/>')
                v += st
        hgt = y + 54
    for s0, e0, txt in opt['brace']:
        xa, xb = X(float(s0)), X(float(e0))
        yb = hgt
        out.append(f'<path d="M{xa:.1f} {yb} q0 8 8 8 H{(xa + xb) / 2 - 8:.1f} q8 0 8 8 q0 -8 8 -8 H{xb - 8:.1f} q8 0 8 -8" fill="none" stroke="#334155" stroke-width="1.3"/>')
        out.append(_lab(f'{(xa + xb) / 2:.1f}', yb + 34, txt, 13, weight='700', color='#334155'))
    if opt['brace']:
        hgt += 44
    for s0, e0, txt in opt['hoplab']:
        xa, xb = X(float(s0)), X(float(e0))
        out.append(f'<rect x="{(xa + xb) / 2 - 36:.1f}" y="{hgt}" width="72" height="22" rx="3" fill="none" stroke="#b91c1c"/>')
        out.append(f'<text x="{(xa + xb) / 2:.1f}" y="{hgt + 16}" text-anchor="middle" font-size="13">{escape(txt)}</text>')
    if opt['hoplab']:
        hgt += 30
    if opt['origin']:
        out.append(f'<line x1="{X(0):.1f}" y1="{hgt + 26}" x2="{X(0):.1f}" y2="{y + 32}" stroke="#1d4ed8" stroke-width="1.6" marker-end="url(#{mid})"/>')
        out.append(f'<text x="{X(0):.1f}" y="{hgt + 42}" text-anchor="middle" font-size="13" font-weight="700" fill="#991b1b">Origin</text>')
        hgt += 50
    label = f'Number line from {a:g} to {b:g}' + ''.join(f'; point {lab} at {val:g}' for val, lab in opt['pts'])
    return f'<svg viewBox="0 0 {w:.0f} {hgt}" width="{w:.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


from figs8_graph import graph, ptab, sqdiv, pdiv  # noqa: E402,F401
from figs8_venn import venn  # noqa: E402,F401
from figs8_pat import pattern, area  # noqa: E402,F401
from figs8_plane import plane  # noqa: E402,F401
from figs8_geo import rtri, circ  # noqa: E402,F401
