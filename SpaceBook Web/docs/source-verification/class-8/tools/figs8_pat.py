"""Class 8 Mathematics: growing dot/square patterns for number sequences."""
from html import escape


def area(spec):
    """Area model: a rectangle split into 2 x 2 parts.
    'w=x:a | h=x:b | cells=x²,ax;bx,ab | top=x + a | side=x + b | pts=D,J,C;E,F,G;A,H,B | shade=0,0'
    w / h: the two widths (left, right) and heights (top, bottom), each a label; sizes are taken from 'ws' / 'hs'
    (default 3:1).  cells: labels row by row.  pts: 3 x 3 corner/edge/centre point letters (rows top to bottom).
    shade: 'r,c' cells drawn darker."""
    o = {'w': ['x', 'a'], 'h': ['x', 'b'], 'ws': [3, 1], 'hs': [3, 1], 'cells': [['', ''], ['', '']], 'top': '', 'side': '',
         'pts': None, 'shade': []}
    for p in [x.strip() for x in spec.split('|')]:
        k, _, v = p.partition('=')
        k = k.strip()
        if k in ('w', 'h'):
            o[k] = [t.strip() for t in v.split(':')]
        elif k in ('ws', 'hs'):
            o[k] = [float(t) for t in v.split(':')]
        elif k == 'cells':
            o['cells'] = [[t.strip() for t in r.split(',')] for r in v.split(';')]
        elif k in ('top', 'side'):
            o[k] = v.strip()
        elif k == 'pts':
            o['pts'] = [[t.strip() for t in r.split(',')] for r in v.split(';')]
        elif k == 'shade':
            o['shade'] = [tuple(int(t) for t in x.split(',')) for x in v.split(';')]
        else:
            raise ValueError('area: unknown option ' + k)
    S = 200
    W1 = S * o['ws'][0] / sum(o['ws'])
    H1 = S * o['hs'][0] / sum(o['hs'])
    x0, y0 = 60, 50
    xs = [x0, x0 + W1, x0 + S]
    ys = [y0, y0 + H1, y0 + S]
    out = ['<defs><marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0f172a"/></marker></defs>']
    fills = [['#bfdbfe', '#a5f3fc'], ['#a5f3fc', '#bfdbfe']]
    for r in range(2):
        for c in range(2):
            f = '#60a5fa' if (r, c) in o['shade'] else fills[r][c]
            out.append(f'<rect x="{xs[c]:.1f}" y="{ys[r]:.1f}" width="{xs[c + 1] - xs[c]:.1f}" height="{ys[r + 1] - ys[r]:.1f}" fill="{f}" stroke="#0f172a" stroke-width="1.3"/>')
            out.append(f'<text x="{(xs[c] + xs[c + 1]) / 2:.1f}" y="{(ys[r] + ys[r + 1]) / 2 + 5:.1f}" text-anchor="middle" font-size="14" font-style="italic">{escape(o["cells"][r][c])}</text>')
    # dimension arrows: widths along the bottom, heights along the right, totals along the top / left
    for c in range(2):
        yb = ys[2] + 16
        out.append(f'<line x1="{xs[c] + 3:.1f}" y1="{yb}" x2="{xs[c + 1] - 3:.1f}" y2="{yb}" stroke="#0f172a" marker-start="url(#arA)" marker-end="url(#arA)"/>')
        out.append(f'<text x="{(xs[c] + xs[c + 1]) / 2:.1f}" y="{yb + 15}" text-anchor="middle" font-size="13" font-style="italic">{escape(o["w"][c])}</text>')
    for r in range(2):
        xr = xs[2] + 16
        out.append(f'<line x1="{xr}" y1="{ys[r] + 3:.1f}" x2="{xr}" y2="{ys[r + 1] - 3:.1f}" stroke="#0f172a" marker-start="url(#arA)" marker-end="url(#arA)"/>')
        out.append(f'<text x="{xr + 8}" y="{(ys[r] + ys[r + 1]) / 2 + 5:.1f}" font-size="13" font-style="italic">{escape(o["h"][r])}</text>')
    if o['top']:
        yt = ys[0] - 24
        out.append(f'<line x1="{xs[0] + 3}" y1="{yt}" x2="{xs[2] - 3}" y2="{yt}" stroke="#0f172a" marker-start="url(#arA)" marker-end="url(#arA)"/>')
        out.append(f'<text x="{(xs[0] + xs[2]) / 2}" y="{yt - 6}" text-anchor="middle" font-size="13" font-style="italic">{escape(o["top"])}</text>')
    if o['side']:
        xl = xs[0] - 24
        out.append(f'<line x1="{xl}" y1="{ys[0] + 3}" x2="{xl}" y2="{ys[2] - 3}" stroke="#0f172a" marker-start="url(#arA)" marker-end="url(#arA)"/>')
        out.append(f'<text transform="translate({xl - 8} {(ys[0] + ys[2]) / 2}) rotate(-90)" text-anchor="middle" font-size="13" font-style="italic">{escape(o["side"])}</text>')
    if o['pts']:
        for r in range(3):
            for c in range(3):
                t = o['pts'][r][c] if r < len(o['pts']) and c < len(o['pts'][r]) else ''
                if t:
                    dx = -9 if c == 0 else (9 if c == 2 else 6)
                    dy = -5 if r == 0 else (14 if r == 2 else -4)
                    anchor = 'end' if c == 0 else 'start'
                    out.append(f'<text x="{xs[c] + dx:.1f}" y="{ys[r] + dy:.1f}" text-anchor="{anchor}" font-size="12" font-weight="700">{escape(t)}</text>')
    W, H = xs[2] + 50, ys[2] + 40
    label = (f'Area model: width {o["w"][0]} + {o["w"][1]}, height {o["h"][0]} + {o["h"][1]}; parts '
             + ', '.join(c for row in o['cells'] for c in row))
    return f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def pattern(spec):
    """'kind=tri | n=4 | labels=1,;3,;6,;10,......'
    kind: tri (staircase of dots, row k has k dots), pyr (pyramid of squares, rows 1,3,5,...),
    grid (n x n squares).  n: number of figures (figure k uses size k)."""
    o = {'kind': 'tri', 'n': 4, 'labels': []}
    for p in [x.strip() for x in spec.split('|')]:
        k, _, v = p.partition('=')
        k = k.strip()
        if k == 'kind':
            o['kind'] = v.strip()
        elif k == 'n':
            o['n'] = int(v)
        elif k == 'labels':
            o['labels'] = [t.strip() for t in v.split(';')]
        else:
            raise ValueError('pattern: unknown option ' + k)
    u = 14
    figs, x = [], 10
    hmax = 0
    for k in range(1, o['n'] + 1):
        items = []
        if o['kind'] == 'tri':
            w, h = k * u, k * u
            for r in range(k):
                for c in range(r + 1):
                    items.append(('c', c * u + u / 2, r * u + u / 2))
        elif o['kind'] == 'itri':
            # inverted triangle of dots: rows 2k+1, 2k-1, ..., 1 (figure k = 1 starts with rows 3, 1)
            top_n = 2 * k + 1
            w, h = top_n * u, (k + 1) * u
            for r in range(k + 1):
                cnt = top_n - 2 * r
                for c in range(cnt):
                    items.append(('c', r * u + c * u + u / 2, r * u + u / 2))
        elif o['kind'] == 'rdots':
            # rectangle of dots: (k + 1) rows by (k + 2) columns
            w, h = (k + 2) * u, (k + 1) * u
            for r in range(k + 1):
                for c in range(k + 2):
                    items.append(('c', c * u + u / 2, r * u + u / 2))
        elif o['kind'] == 'pyr':
            w, h = (2 * k - 1) * u, k * u
            for r in range(k):
                cnt = 2 * r + 1
                off = (k - 1 - r) * u
                for c in range(cnt):
                    items.append(('s', off + c * u, r * u))
        else:
            w, h = k * u, k * u
            for r in range(k):
                for c in range(k):
                    items.append(('s', c * u, r * u))
        figs.append((x, w, h, items))
        x += w + 26
        hmax = max(hmax, h)
    out = []
    base = 10 + hmax
    for i, (fx, w, h, items) in enumerate(figs):
        top = base - h
        for t, a, b in items:
            if t == 'c':
                out.append(f'<circle cx="{fx + a:.1f}" cy="{top + b:.1f}" r="{u * 0.32:.1f}" fill="#0f172a"/>')
            else:
                out.append(f'<rect x="{fx + a + 1:.1f}" y="{top + b + 1:.1f}" width="{u - 2}" height="{u - 2}" fill="#fff" stroke="#0f172a" stroke-width="1.2"/>')
        if i < len(o['labels']):
            out.append(f'<text x="{fx + w / 2:.1f}" y="{base + 18}" text-anchor="middle" font-size="13">{escape(o["labels"][i])}</text>')
    W = x
    H = base + 26
    names = {'tri': 'triangular dot patterns', 'pyr': 'square pyramids', 'grid': 'square grids'}
    label = f'{o["n"]} {names.get(o["kind"], o["kind"])} labelled ' + ', '.join(o['labels'])
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'
