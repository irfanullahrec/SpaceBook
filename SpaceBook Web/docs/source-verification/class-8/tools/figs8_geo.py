"""Class 8 Mathematics: labelled right-angled triangles and other simple geometry figures."""
from html import escape


import math


def circ(spec):
    """Circle with arcs / sectors. 'r=70 | O | arc=20:110:A:B | sector=20:110 | dotted | chord=C:B:200:340 | lab=Arc@1.2:65
       | pts=A:20;B:110;D:200 | angle=θ'
    Angles are in degrees anticlockwise from the +x axis.  arc: drawn thick from a1 to a2 with end labels.
    sector: shaded sector from a1 to a2 (radii drawn).  dotted: the rest of the circle is dotted.
    chord: a chord between two angles with end labels.  pts: named points on the circle.
    lab: free text at (scale, angle) in polar form.  angle: label for the central angle.  O: mark the centre."""
    parts = [p.strip() for p in spec.split('|')]
    o = {'r': 70, 'O': False, 'arcs': [], 'sectors': [], 'dotted': False, 'chords': [], 'labs': [], 'pts': [], 'angle': '', 'rl': ''}
    for p in parts:
        k, _, v = p.partition('=')
        k = k.strip()
        if k == 'r':
            o['r'] = float(v)
        elif k == 'O':
            o['O'] = True
        elif k == 'dotted':
            o['dotted'] = True
        elif k == 'arc':
            a1, a2, *lab = v.split(':')
            o['arcs'].append((float(a1), float(a2), lab))
        elif k == 'sector':
            a1, a2 = v.split(':')[:2]
            o['sectors'].append((float(a1), float(a2)))
        elif k == 'chord':
            l1, l2, a1, a2 = v.split(':')
            o['chords'].append((l1, l2, float(a1), float(a2)))
        elif k == 'lab':
            for q in v.split(';'):
                t, _, pa = q.rpartition('@')
                s, a = pa.split(':')
                o['labs'].append((t, float(s), float(a)))
        elif k == 'pts':
            for q in v.split(';'):
                n, a = q.split(':')
                o['pts'].append((n, float(a)))
        elif k == 'angle':
            o['angle'] = v.strip()
        elif k == 'rl':
            o['rl'] = v.strip()
        else:
            raise ValueError('circ: unknown option ' + k)
    R = o['r']
    cx = cy = R + 40
    P = lambda a, s=1.0: (cx + s * R * math.cos(math.radians(a)), cy - s * R * math.sin(math.radians(a)))
    out = []
    dash = ' stroke-dasharray="3 4"' if o['dotted'] else ''
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#0f172a" stroke-width="1.2"{dash}/>')
    for a1, a2 in o['sectors']:
        x1, y1 = P(a1); x2, y2 = P(a2)
        large = 1 if (a2 - a1) % 360 > 180 else 0
        out.append(f'<path d="M{cx} {cy}L{x1:.1f} {y1:.1f}A{R} {R} 0 {large} 0 {x2:.1f} {y2:.1f}Z" fill="#f9a8d4" fill-opacity="0.8" stroke="#0f172a" stroke-width="1.3"/>')
    for a1, a2, lab in o['arcs']:
        x1, y1 = P(a1); x2, y2 = P(a2)
        large = 1 if (a2 - a1) % 360 > 180 else 0
        out.append(f'<path d="M{x1:.1f} {y1:.1f}A{R} {R} 0 {large} 0 {x2:.1f} {y2:.1f}" fill="none" stroke="#0f172a" stroke-width="2.6"/>')
        for name, a in zip(lab, (a1, a2)):
            x, y = P(a, 1.14)
            out.append(f'<circle cx="{P(a)[0]:.1f}" cy="{P(a)[1]:.1f}" r="2.5"/><text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-size="12" font-weight="700">{escape(name)}</text>')
    for l1, l2, a1, a2 in o['chords']:
        x1, y1 = P(a1); x2, y2 = P(a2)
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#0f172a" stroke-width="1.3"/><line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#0f172a" stroke-width="1.3"/>')
        for name, a in ((l1, a1), (l2, a2)):
            x, y = P(a, 1.14)
            out.append(f'<circle cx="{P(a)[0]:.1f}" cy="{P(a)[1]:.1f}" r="2.5"/><text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-size="12" font-weight="700">{escape(name)}</text>')
    for name, a in o['pts']:
        x, y = P(a, 1.14)
        out.append(f'<circle cx="{P(a)[0]:.1f}" cy="{P(a)[1]:.1f}" r="2.5"/><text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-size="12" font-weight="700">{escape(name)}</text>')
    if o['O']:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="2.5"/><text x="{cx - 8}" y="{cy + 14}" font-size="12" font-weight="700">O</text>')
    if o['angle'] and o['sectors']:
        a1, a2 = o['sectors'][0]
        am = (a1 + a2) / 2
        x, y = P(am, 0.28)
        out.append(f'<path d="M{P(a1, 0.18)[0]:.1f} {P(a1, 0.18)[1]:.1f}A{R * 0.18:.1f} {R * 0.18:.1f} 0 0 0 {P(a2, 0.18)[0]:.1f} {P(a2, 0.18)[1]:.1f}" fill="none" stroke="#0f172a"/>')
        out.append(f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-size="12" font-style="italic">{escape(o["angle"])}</text>')
    if o['rl'] and o['sectors']:
        a1, a2 = o['sectors'][0]
        x, y = P(a1, 0.55)
        out.append(f'<text x="{x:.1f}" y="{y + 14:.1f}" text-anchor="middle" font-size="12" font-style="italic">{escape(o["rl"])}</text>')
    for t, s, a in o['labs']:
        x, y = P(a, s)
        out.append(f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-size="12">{escape(t)}</text>')
    S = 2 * (R + 40)
    label = 'Circle' + ('; arcs ' + ', '.join(''.join(l) for _, _, l in o['arcs']) if o['arcs'] else '') + ('; shaded sector' if o['sectors'] else '')
    return f'<svg viewBox="0 0 {S:.0f} {S:.0f}" width="{S:.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def rtri(spec):
    """Right-angled triangle. 'A,B,C | base=4cm | alt=3cm | hyp=5cm | right=B | flip'
    Vertices are named in order: first at the left of the base, second at the right angle (bottom right),
    third at the top. base/alt/hyp: edge labels (any text). flip: right angle at the bottom-left instead."""
    parts = [p.strip() for p in spec.split('|')]
    names = [n.strip() for n in parts[0].split(',')]
    o = {'base': '', 'alt': '', 'hyp': '', 'flip': False, 'w': 150, 'h': 110}
    for p in parts[1:]:
        k, _, v = p.partition('=')
        k = k.strip()
        if k in ('base', 'alt', 'hyp'):
            o[k] = v.strip()
        elif k == 'flip':
            o['flip'] = True
        elif k in ('w', 'h'):
            o[k] = float(v)
        else:
            raise ValueError('rtri: unknown option ' + k)
    L, T = 40, 24
    W, H = o['w'], o['h']
    if o['flip']:
        A, B, C = (L + W, T + H), (L, T + H), (L, T)
        sq = f'M{L} {T + H - 12}h12v12'
    else:
        A, B, C = (L, T + H), (L + W, T + H), (L + W, T)
        sq = f'M{L + W - 12} {T + H}v-12h12'
    out = [f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="#fff" stroke="#0f172a" stroke-width="1.5"/>',
           f'<path d="{sq}" fill="none" stroke="#0f172a" stroke-width="1.2"/>']
    nA, nB, nC = (names + ['', '', ''])[:3]
    out.append(f'<text x="{A[0] - 6 if not o["flip"] else A[0] + 6}" y="{A[1] + 15}" text-anchor="{"end" if not o["flip"] else "start"}" font-size="13" font-weight="700">{escape(nA)}</text>')
    out.append(f'<text x="{B[0] + 6 if not o["flip"] else B[0] - 6}" y="{B[1] + 15}" text-anchor="{"start" if not o["flip"] else "end"}" font-size="13" font-weight="700">{escape(nB)}</text>')
    out.append(f'<text x="{C[0]}" y="{C[1] - 8}" text-anchor="middle" font-size="13" font-weight="700">{escape(nC)}</text>')
    if o['base']:
        out.append(f'<text x="{(A[0] + B[0]) / 2}" y="{A[1] + 16}" text-anchor="middle" font-size="12">{escape(o["base"])}</text>')
    if o['alt']:
        x = B[0] + (8 if not o['flip'] else -8)
        out.append(f'<text x="{x}" y="{(B[1] + C[1]) / 2 + 4}" text-anchor="{"start" if not o["flip"] else "end"}" font-size="12">{escape(o["alt"])}</text>')
    if o['hyp']:
        mx, my = (A[0] + C[0]) / 2, (A[1] + C[1]) / 2
        dx = -10 if not o['flip'] else 10
        out.append(f'<text x="{mx + dx}" y="{my - 6}" text-anchor="{"end" if not o["flip"] else "start"}" font-size="12">{escape(o["hyp"])}</text>')
    label = f'Right-angled triangle {nA}{nB}{nC} with right angle at {nB}' + (f'; base {o["base"]}' if o['base'] else '') + (f'; altitude {o["alt"]}' if o['alt'] else '') + (f'; hypotenuse {o["hyp"]}' if o['hyp'] else '')
    return f'<svg viewBox="0 0 {L + W + 50:.0f} {T + H + 30:.0f}" width="{L + W + 50:.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'
