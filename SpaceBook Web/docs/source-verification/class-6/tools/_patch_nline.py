from pathlib import Path
p = Path('tools/figs.py'); s = p.read_text(encoding='utf-8')
if 'circ=' not in s:
    s = s.replace("""    arcs, dots, qpos, labels = [], [], None, None""", """    arcs, dots, qpos, labels, circ, braces, tops = [], [], None, None, [], [], []""")
    s = s.replace("""        elif p.startswith('labels='):
            labels = p[7:].split(',')""", """        elif p.startswith('labels='):
            labels = p[7:].split(',')
        elif p.startswith('circ='):
            circ = [int(x) for x in p[5:].split(',')]
        elif p.startswith('brace='):
            braces = [x.split(':') for x in p[6:].split(';')]
        elif p.startswith('top='):
            tops = [x.split(':') for x in p[4:].split(';')]""")
    s = s.replace("""    x0, y = 24, 70""", """    x0, y = 24, 70 if not tops else 84""")
    s = s.replace("""    for d in dots:
        out.append(f'<circle cx="{X(d)}" cy="{y}" r="5" fill="#dc2626"/>')""", """    for d in dots:
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
        out.append(f'<text x="{(xa + xb) / 2}" y="{y - 40}" text-anchor="middle" font-size="14" font-weight="700">{escape(txt)}</text>')""")
    s = s.replace("""<path d="M0 0L10 5L0 10z" fill="#7c3aed"/></marker></defs>')""", """<path d="M0 0L10 5L0 10z" fill="#7c3aed"/></marker><marker id="{mid}t" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#0f172a"/></marker></defs>')""")
    s = s.replace("""    return f'<svg viewBox="0 0 {w} 110" width="{w}" role="img" aria-label="{escape(label)}" font-family""", """    hgt = y + (90 if braces else 40)
    return f'<svg viewBox="0 0 {w} {hgt}" width="{w}" role="img" aria-label="{escape(label)}" font-family""")
    assert s.count('circ=') >= 1 and 'hgt' in s
    p.write_text(s, encoding='utf-8')
print('figs ok')
