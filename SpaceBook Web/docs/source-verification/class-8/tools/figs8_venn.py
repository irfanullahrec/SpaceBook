"""Class 8 Mathematics: Venn diagrams for 2 or 3 sets with optional region shading."""
import hashlib
from html import escape

COL = {'a': '#93c5fd', 'b': '#fca5a5', 'c': '#86efac'}


def venn(spec):
    """'sets=A,B | a=1 2 | ab=3 | b=4 | out=9 | U=U | shade=a,ab | note=text;text | nocirclelabels'
    sets: 2 or 3 set names (circles a, b[, c]).  Region keys use those letters: a, b, c, ab, ac, bc, abc, out.
    Region values are space-separated elements.  U: universal-set label (draws the rectangle).
    shade: regions filled with a highlight colour.  note: caption lines drawn under the diagram."""
    parts = [p.strip() for p in spec.split('|')]
    o = {'sets': ['A', 'B'], 'U': None, 'shade': [], 'note': [], 'regions': {}}
    for p in parts:
        k, _, v = p.partition('=')
        k = k.strip()
        if k == 'sets':
            o['sets'] = [s.strip() for s in v.split(',')]
        elif k == 'U':
            o['U'] = v.strip()
        elif k == 'shade':
            o['shade'] = [s.strip() for s in v.split(',') if s.strip()]
        elif k == 'note':
            o['note'] = [s.strip() for s in v.split(';') if s.strip()]
        elif k in ('a', 'b', 'c', 'ab', 'ac', 'bc', 'abc', 'out'):
            o['regions'][k] = v.split()
        else:
            raise ValueError('venn: unknown option ' + k)
    three = len(o['sets']) == 3
    W, H = (360, 300) if three else (380, 220)
    cx, cy = W / 2, (150 if three else 110)
    if three:
        circ = {'a': (cx - 55, cy - 38), 'b': (cx + 55, cy - 38), 'c': (cx, cy + 50)}
        r = 88
        spots = {'a': (cx - 95, cy - 62), 'b': (cx + 95, cy - 62), 'c': (cx, cy + 100), 'ab': (cx, cy - 82),
                 'ac': (cx - 62, cy + 34), 'bc': (cx + 62, cy + 34), 'abc': (cx, cy - 4), 'out': (34, H - 18)}
    else:
        circ = {'a': (cx - 62, cy), 'b': (cx + 62, cy)}
        r = 92
        spots = {'a': (cx - 105, cy), 'b': (cx + 105, cy), 'ab': (cx, cy), 'out': (30, H - 14)}
    letters = list(circ)
    mid = 'vn' + hashlib.md5(spec.encode()).hexdigest()[:8]
    out = ['<defs>']
    for L, (x, y) in circ.items():
        out.append(f'<clipPath id="{mid}{L}"><circle cx="{x}" cy="{y}" r="{r}"/></clipPath>')
    for reg in o['shade']:
        inc = [] if reg == 'out' else list(reg)
        exc = [L for L in letters if L not in inc]
        out.append(f'<mask id="{mid}m{reg}"><rect x="0" y="0" width="{W}" height="{H}" fill="#fff"/>'
                   + ''.join(f'<circle cx="{circ[L][0]}" cy="{circ[L][1]}" r="{r}" fill="#000"/>' for L in exc) + '</mask>')
    out.append('</defs>')
    out.append(f'<rect x="4" y="4" width="{W - 8}" height="{H - 8}" fill="#fff" stroke="{"#0f172a" if o["U"] else "none"}" stroke-width="1.4"/>')
    for reg in o['shade']:
        inc = [] if reg == 'out' else list(reg)
        g = f'<rect x="4" y="4" width="{W - 8}" height="{H - 8}" fill="#fde047" fill-opacity="0.75"/>'
        for L in inc:
            g = f'<g clip-path="url(#{mid}{L})">{g}</g>'
        out.append(f'<g mask="url(#{mid}m{reg})">{g}</g>')
    for L, (x, y) in circ.items():
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{COL[L]}" fill-opacity="0.18" stroke="#0f172a" stroke-width="1.5"/>')
    if o['U']:
        out.append(f'<text x="14" y="24" font-size="15" font-weight="700">{escape(o["U"])}</text>')
    lab_pos = {'a': (circ['a'][0] - r * 0.75, circ['a'][1] - r * 0.78 if three else circ['a'][1] + r + 0), 'b': (circ['b'][0] + r * 0.75, circ['b'][1] - r * 0.78 if three else circ['b'][1] + r + 0)}
    if not three:
        lab_pos = {'a': (circ['a'][0] - r * 0.78, cy + r * 0.82), 'b': (circ['b'][0] + r * 0.78, cy + r * 0.82)}
    else:
        lab_pos['c'] = (circ['c'][0] + r * 0.82, circ['c'][1] + r * 0.72)
    for L, name in zip(letters, o['sets']):
        x, y = lab_pos[L]
        out.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-size="15" font-weight="700">{escape(name)}</text>')
    for reg, items in o['regions'].items():
        x0, y0 = spots[reg]
        per = 3 if reg not in ('ab', 'abc', 'ac', 'bc') else 2
        rows = [items[i:i + per] for i in range(0, len(items), per)]
        for j, row in enumerate(rows):
            y = y0 + (j - (len(rows) - 1) / 2) * 17 + 5
            txt = '   '.join(row)
            anchor = 'start' if reg == 'out' else 'middle'
            out.append(f'<text x="{x0:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="13" xml:space="preserve">{escape(txt)}</text>')
    hh = H
    for i, line in enumerate(o['note']):
        out.append(f'<text x="{W / 2}" y="{H + 18 + i * 17}" text-anchor="middle" font-size="12" fill="#334155">{escape(line)}</text>')
    if o['note']:
        hh = H + 10 + 17 * len(o['note'])
    label = 'Venn diagram of sets ' + ', '.join(o['sets']) + ''.join(f'; {k}: {" ".join(v)}' for k, v in o['regions'].items()) + (f'; shaded {", ".join(o["shade"])}' if o['shade'] else '')
    return f'<svg viewBox="0 0 {W} {hh}" width="{W}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'
