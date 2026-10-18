"""SVG generators for recurring Class 7 Mathematics figures (long division, division ladder, factor tree)."""
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


def dline(spec):
    """'0..1 | major=10 | minor=10 | top=0:0;0.09:0.4;0.16 | bottom=0.1;0.2' : decimal / fraction number line.
    The segment a..b is cut into `major` parts, each cut into `minor` parts. `top`/`bottom` are labels at values;
    'value:text' prints `text` at `value` (to reproduce the book's own label), frac 'n/d' text is drawn as a stacked fraction."""
    parts = [p.strip() for p in spec.split('|')]
    a, b = [float(x) for x in parts[0].split('..')]
    major, minor, tops, bottoms, dots = 10, 1, [], [], []
    for p in parts[1:]:
        k, _, v = p.partition('=')
        if k == 'major': major = int(v)
        elif k == 'minor': minor = int(v)
        elif k in ('top', 'bottom'):
            items = []
            for it in v.split(';'):
                val, _, txt = it.partition(':')
                items.append((float(eval(val, {}, {})), txt or val))
            (tops if k == 'top' else bottoms).extend(items)
        elif k == 'dots':
            dots = [float(eval(x, {}, {})) for x in v.split(',')]
    n = major * minor
    width = 620 if n > 20 else 420
    x0, y = 30, 62
    X = lambda v: x0 + (v - a) / (b - a) * (width - 2 * x0)
    out = [f'<line x1="{x0 - 18}" y1="{y}" x2="{width - x0 + 18}" y2="{y}" stroke="#0f172a" stroke-width="1.5"/>',
           f'<path d="M{x0 - 20} {y} l9 -5 v10 z" fill="#0f172a"/><path d="M{width - x0 + 20} {y} l-9 -5 v10 z" fill="#0f172a"/>']
    for i in range(n + 1):
        xv = X(a + (b - a) * i / n)
        big = i % minor == 0
        out.append(f'<line x1="{xv:.1f}" y1="{y - (8 if big else 4)}" x2="{xv:.1f}" y2="{y + (8 if big else 4)}" stroke="#0f172a" stroke-width="{1.4 if big else 0.8}"/>')

    def label(v, txt, above):
        xv = X(v)
        if '/' in txt:
            num, den = txt.split('/')
            yy = y - 30 if above else y + 22
            return (f'<text x="{xv:.1f}" y="{yy}" text-anchor="middle" font-size="12">{escape(num)}</text>'
                    f'<line x1="{xv - 7:.1f}" y1="{yy + 4}" x2="{xv + 7:.1f}" y2="{yy + 4}" stroke="#0f172a"/>'
                    f'<text x="{xv:.1f}" y="{yy + 17}" text-anchor="middle" font-size="12">{escape(den)}</text>')
        return f'<text x="{xv:.1f}" y="{y - 16 if above else y + 26}" text-anchor="middle" font-size="13">{escape(txt.replace("-", "−"))}</text>'
    out += [label(v, t, True) for v, t in tops] + [label(v, t, False) for v, t in bottoms]
    out += [f'<circle cx="{X(d):.1f}" cy="{y}" r="4" fill="#dc2626"/>' for d in dots]
    aria = 'Number line from {} to {} divided into {} parts; marked: {}'.format(parts[0].split('..')[0], parts[0].split('..')[1], n,
                                                                          ', '.join(t for _, t in tops + bottoms))
    return f'<svg viewBox="0 0 {width} {y + 52}" width="{width}" role="img" aria-label="{escape(aria)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def sqrtdiv(spec):
    """'23 | 5 29 | 2:4:1 29 ; 43:1 29:0' — square root by long division.
    QUOTIENT | DIVIDEND (digit pairs separated by spaces, each pair overlined) | steps 'divisor:subtrahend:remainder'.
    Optional 4th field 'down' draws a ↓ under the last pair on the first remainder row."""
    parts = [p.strip() for p in spec.split('|')]
    q, dividend = parts[0], parts[1]
    steps = [[x.strip() for x in s.split(':')] for s in parts[2].split(';')]
    pending = steps.pop()[0] if len(steps[-1]) == 1 else None   # trailing 'divisor' only: label without a step yet
    cw, lh = 9.9, 26   # Consolas advance at 18px
    width_chars = max([len(dividend)] + [len(s[1]) + 2 for s in steps] + [len(s[2]) for s in steps])
    lw = max(len(s[0]) for s in steps) * cw + 16
    right = lw + 14 + width_chars * cw
    W = right + 16
    out, y = [], 22
    out.append(f'<text x="{right}" y="{y}" text-anchor="end">{escape(q)}</text>')
    y += lh
    top = y - 18
    out.append(f'<line x1="{lw + 4}" y1="{top}" x2="{right + 6}" y2="{top}" stroke="#0f172a" stroke-width="1.4"/>')
    # dividend with pair overlines
    out.append(f'<text x="{right}" y="{y}" text-anchor="end" xml:space="preserve">{escape(dividend)}</text>')
    pos = len(dividend)
    for tok in reversed(dividend.split(' ')):
        x2 = right - (len(dividend) - pos) * cw
        x1 = x2 - len(tok) * cw
        out.append(f'<line x1="{x1 + 1}" y1="{y - 15}" x2="{x2 - 1}" y2="{y - 15}" stroke="#0f172a" stroke-width="1.1"/>')
        pos -= len(tok) + 1
    rows_left = [(steps[0][0], y)]
    for i, (dv, sub, rem) in enumerate(steps):
        y += lh
        out.append(f'<text x="{right}" y="{y}" text-anchor="end" xml:space="preserve">− {escape(sub)}</text>')
        out.append(f'<line x1="{right - (len(sub) + 2) * cw}" y1="{y + 7}" x2="{right + 4}" y2="{y + 7}" stroke="#0f172a" stroke-width="1.2"/>')
        y += lh
        out.append(f'<text x="{right}" y="{y}" text-anchor="end" xml:space="preserve">{escape(rem)}</text>')
        if i + 1 < len(steps):
            rows_left.append((steps[i + 1][0], y))
        elif pending:
            rows_left.append((pending, y))
    for dv, yy in rows_left:
        out.append(f'<text x="{lw - 4}" y="{yy}" text-anchor="end">{escape(dv)}</text>')
    out.append(f'<line x1="{lw + 4}" y1="{top}" x2="{lw + 4}" y2="{y + 6}" stroke="#0f172a" stroke-width="1.4"/>')
    label = f'Square root of {dividend.replace(" ", "")} by long division: quotient {q}; ' + '; '.join(f'divisor {d}, subtract {s}, remainder {r}' for d, s, r in steps)
    return f'<svg viewBox="0 0 {W} {y + 12}" width="{W}" role="img" aria-label="{escape(label)}" {FONT}>' + ''.join(out) + '</svg>'


def bars(spec):
    """'cats=May,June,July | series=Research:15,25,10;Designing:20,25,15 | ymax=40 | step=5 | ylab=No. of employees | xlab=Months | horiz=0 | title=…'
    Grouped bar chart (vertical by default; horiz=1 draws horizontal bars). One series gives a simple bar chart;
    'hist=1' draws touching bars (histogram)."""
    kv = {}
    for part in spec.split('|'):
        if '=' in part:
            k, v = part.split('=', 1)
            kv[k.strip()] = v.strip()
    cats = [c.strip() for c in kv['cats'].split(',')]
    series = []
    for s in kv['series'].split(';'):
        name, _, vals = s.rpartition(':')
        series.append((name.strip(), [float(v) for v in vals.split(',')]))
    ymax = float(kv.get('ymax', max(max(v) for _, v in series)))
    step = float(kv.get('step', ymax / 5))
    cols = ['#e11d48', '#fb923c', '#86efac', '#38bdf8', '#a78bfa', '#facc15']
    horiz = kv.get('horiz') == '1'
    hist = kv.get('hist') == '1'
    ns = len(series)
    L, T, R, B = 62, 30, 20, 70
    plot = 420 if not horiz else 360
    group = plot / len(cats)
    bw = (group if hist else group * 0.7) / ns
    W = L + plot + R if not horiz else L + 80 + 300 + R
    H = T + 240 + B if not horiz else T + plot + 50
    out = []
    if not horiz:
        y0, ph = T + 240, 240
        ticks = []
        v = 0.0
        while v <= ymax + 1e-9:
            y = y0 - v / ymax * ph
            out.append(f'<line x1="{L}" y1="{y:.1f}" x2="{L + plot}" y2="{y:.1f}" stroke="#e2e8f0"/>')
            out.append(f'<text x="{L - 6}" y="{y + 4:.1f}" text-anchor="end" font-size="11">{v:g}</text>')
            v += step
        for ci, c in enumerate(cats):
            gx = L + ci * group + (0 if hist else group * 0.15)
            for si, (_, vals) in enumerate(series):
                h = vals[ci] / ymax * ph
                out.append(f'<rect x="{gx + si * bw:.1f}" y="{y0 - h:.1f}" width="{bw - (0 if hist else 2):.1f}" height="{h:.1f}" fill="{cols[si % 6]}" stroke="#0f172a" stroke-width="0.6"/>')
            out.append(f'<text x="{L + ci * group + group / 2:.1f}" y="{y0 + 16}" text-anchor="middle" font-size="11">{escape(c)}</text>')
        out.append(f'<line x1="{L}" y1="{T - 10}" x2="{L}" y2="{y0}" stroke="#0f172a" stroke-width="1.4"/><line x1="{L}" y1="{y0}" x2="{L + plot + 10}" y2="{y0}" stroke="#0f172a" stroke-width="1.4"/>')
        out.append(f'<text x="16" y="{T + ph / 2}" text-anchor="middle" font-size="12" transform="rotate(-90 16 {T + ph / 2})">{escape(kv.get("ylab", ""))}</text>')
        out.append(f'<text x="{L + plot / 2}" y="{y0 + 34}" text-anchor="middle" font-size="12">{escape(kv.get("xlab", ""))}</text>')
        ly = y0 + 52
    else:
        x0, pw = L + 80, 300
        v = 0.0
        while v <= ymax + 1e-9:
            x = x0 + v / ymax * pw
            out.append(f'<line x1="{x:.1f}" y1="{T}" x2="{x:.1f}" y2="{T + plot}" stroke="#e2e8f0"/>')
            out.append(f'<text x="{x:.1f}" y="{T + plot + 14}" text-anchor="middle" font-size="11">{v:g}</text>')
            v += step
        for ci, c in enumerate(cats):
            gy = T + ci * group + group * 0.15
            for si, (_, vals) in enumerate(series):
                w = vals[ci] / ymax * pw
                out.append(f'<rect x="{x0}" y="{gy + si * bw:.1f}" width="{w:.1f}" height="{bw - 2:.1f}" fill="{cols[si % 6]}" stroke="#0f172a" stroke-width="0.6"/>')
            out.append(f'<text x="{x0 - 6}" y="{T + ci * group + group / 2 + 4:.1f}" text-anchor="end" font-size="11">{escape(c)}</text>')
        out.append(f'<line x1="{x0}" y1="{T - 6}" x2="{x0}" y2="{T + plot}" stroke="#0f172a" stroke-width="1.4"/><line x1="{x0}" y1="{T + plot}" x2="{x0 + pw + 10}" y2="{T + plot}" stroke="#0f172a" stroke-width="1.4"/>')
        out.append(f'<text x="{x0 + pw / 2}" y="{T + plot + 32}" text-anchor="middle" font-size="12">{escape(kv.get("ylab", ""))}</text>')
        ly = T + plot + 46
    if ns > 1:
        lx = L
        for si, (name, _) in enumerate(series):
            out.append(f'<rect x="{lx}" y="{ly - 9}" width="10" height="10" fill="{cols[si % 6]}"/><text x="{lx + 14}" y="{ly}" font-size="11">{escape(name)}</text>')
            lx += 24 + 7 * len(name)
    if kv.get('title'):
        out.append(f'<text x="{W / 2}" y="16" text-anchor="middle" font-size="13" font-weight="700">{escape(kv["title"])}</text>')
    data = '; '.join(f'{c}: ' + ', '.join(f'{n} {vals[i]:g}' if ns > 1 else f'{vals[i]:g}' for n, vals in series) for i, c in enumerate(cats))
    label = f'{"Histogram" if hist else ("Horizontal" if horiz else "Vertical")} {"multiple " if ns > 1 else ""}bar graph' + (f' "{kv["title"]}"' if kv.get('title') else '') + f'. {data}'
    return f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{min(W, 520):.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def linegraph(spec):
    """'cats=Week 1,Week 2 | vals=4,8 | ymax=10 | step=2 | ylab=Marks | xlab=Weeks | title=…' — line graph with points."""
    kv = {}
    for part in spec.split('|'):
        if '=' in part:
            k, v = part.split('=', 1)
            kv[k.strip()] = v.strip()
    cats = [c.strip() for c in kv['cats'].split(',')]
    vals = [float(v) for v in kv['vals'].split(',')]
    ymax = float(kv.get('ymax', max(vals)))
    step = float(kv.get('step', ymax / 5))
    L, T, pw, ph = 70, 30, 400, 230
    W, H = L + pw + 20, T + ph + 60
    out = []
    v = 0.0
    while v <= ymax + 1e-9:
        y = T + ph - v / ymax * ph
        out.append(f'<line x1="{L}" y1="{y:.1f}" x2="{L + pw}" y2="{y:.1f}" stroke="#e2e8f0"/><text x="{L - 6}" y="{y + 4:.1f}" text-anchor="end" font-size="11">{v:g}</text>')
        v += step
    gx = pw / len(cats)
    pts = [(L + gx * (i + 0.5), T + ph - val / ymax * ph) for i, val in enumerate(vals)]
    for i, c in enumerate(cats):
        out.append(f'<line x1="{pts[i][0]:.1f}" y1="{T}" x2="{pts[i][0]:.1f}" y2="{T + ph}" stroke="#f1f5f9"/><text x="{pts[i][0]:.1f}" y="{T + ph + 16}" text-anchor="middle" font-size="11">{escape(c)}</text>')
    out.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="#e11d48" stroke-width="2.2"/>')
    out += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="#e11d48"/>' for x, y in pts]
    out.append(f'<line x1="{L}" y1="{T - 8}" x2="{L}" y2="{T + ph}" stroke="#0f172a" stroke-width="1.4"/><line x1="{L}" y1="{T + ph}" x2="{L + pw}" y2="{T + ph}" stroke="#0f172a" stroke-width="1.4"/>')
    out.append(f'<text x="16" y="{T + ph / 2}" text-anchor="middle" font-size="12" transform="rotate(-90 16 {T + ph / 2})">{escape(kv.get("ylab", ""))}</text><text x="{L + pw / 2}" y="{T + ph + 36}" text-anchor="middle" font-size="12">{escape(kv.get("xlab", ""))}</text>')
    if kv.get('title'):
        out.append(f'<text x="{W / 2}" y="16" text-anchor="middle" font-size="13" font-weight="700">{escape(kv["title"])}</text>')
    label = 'Line graph' + (f' "{kv["title"]}"' if kv.get('title') else '') + '. ' + '; '.join(f'{c}: {v:g}' for c, v in zip(cats, vals))
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def pie(spec):
    """'1st week:36;2nd week:45;… | unit=°' — pie chart; values are sector angles (unit=°) or amounts (converted to angles)."""
    import math
    parts = spec.split('|')
    kv = {}
    for part in parts[1:]:
        if '=' in part:
            k, v = part.split('=', 1)
            kv[k.strip()] = v.strip()
    items = []
    for it in parts[0].split(';'):
        n, _, v = it.rpartition(':')
        items.append((n.strip(), float(v)))
    total = sum(v for _, v in items)
    angles = [v if kv.get('unit') == '°' else v / total * 360 for _, v in items]
    cols = ['#f9a8d4', '#fde047', '#e11d48', '#0d9488', '#7c3aed', '#ec4899', '#38bdf8', '#86efac', '#fb923c', '#a3a3a3']
    cx, cy, r = 150, 140, 110
    out, a0 = [], -90.0
    for i, ((n, v), ang) in enumerate(zip(items, angles)):
        a1 = a0 + ang
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        large = 1 if ang > 180 else 0
        out.append(f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z" fill="{cols[i % len(cols)]}" stroke="#fff" stroke-width="1.5"/>')
        am = math.radians((a0 + a1) / 2)
        lr = r * 0.62
        out.append(f'<text x="{cx + lr * math.cos(am):.1f}" y="{cy + lr * math.sin(am) + 4:.1f}" text-anchor="middle" font-size="11" font-weight="700" paint-order="stroke" stroke="#fff" stroke-width="2.5">{ang:g}°</text>')
        a0 = a1
    ly = 30
    for i, (n, v) in enumerate(items):
        out.append(f'<rect x="290" y="{ly - 10}" width="12" height="12" fill="{cols[i % len(cols)]}"/><text x="308" y="{ly}" font-size="12">{escape(n)}</text>')
        ly += 20
    label = 'Pie chart: ' + '; '.join(f'{n} {ang:g} degrees' for (n, _), ang in zip(items, angles))
    return f'<svg viewBox="0 0 440 290" width="440" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


def poly(spec):
    """'A:40,25;B:170,25;C:170,155;D:40,155 | fill=#fde047 | in=a@A;b@B;98°@D | txt=7 m:100,15 | right=A,B | desc=…'
    Labelled polygon (coordinates in a 0–260 × 0–200 box). in: text placed just inside a vertex (angle names/values).
    right: vertices that get a right-angle mark. txt: free labels at x,y. desc: accessible description."""
    kv = {}
    parts = spec.split('|')
    verts = []
    for v in [t.strip() for t in parts[0].split(';') if t.strip()]:
        n, _, xy = v.rpartition(':')
        x, y = (float(c) for c in xy.split(','))
        verts.append((n, x, y))
    for part in parts[1:]:
        if '=' in part:
            k, val = part.split('=', 1)
            kv[k.strip()] = val.strip()
    cx = sum(v[1] for v in verts) / len(verts)
    cy = sum(v[2] for v in verts) / len(verts)
    pos = {n: (x, y) for n, x, y in verts}
    xs = [v[1] for v in verts]; ys = [v[2] for v in verts]
    W, H = max(xs) + 40, max(ys) + 30
    out = [f'<polygon points="{" ".join(f"{x},{y}" for _, x, y in verts)}" fill="{kv.get("fill", "#e0f2fe")}" stroke="#0f172a" stroke-width="1.6"/>']
    for n, x, y in verts:
        dx, dy = x - cx, y - cy
        d = max((dx * dx + dy * dy) ** 0.5, 1)
        out.append(f'<text x="{x + dx / d * 14:.1f}" y="{y + dy / d * 14 + 5:.1f}" text-anchor="middle" font-weight="700">{escape(n)}</text>')
    for item in [t.strip() for t in kv.get('in', '').split(';') if t.strip()]:
        lab, _, vn = item.rpartition('@')
        if vn in pos:
            x, y = pos[vn]
            dx, dy = cx - x, cy - y
            d = max((dx * dx + dy * dy) ** 0.5, 1)
            out.append(f'<text x="{x + dx / d * 22:.1f}" y="{y + dy / d * 22 + 5:.1f}" text-anchor="middle" font-size="13" fill="#7c2d12">{escape(lab)}</text>')
    names = [v[0] for v in verts]
    for vn in [t.strip() for t in kv.get('right', '').split(',') if t.strip()]:
        if vn in pos:
            i = names.index(vn)
            (x, y), (x1, y1), (x2, y2) = pos[vn], verts[i - 1][1:], verts[(i + 1) % len(verts)][1:]
            def unit(ax, ay):
                l = max((ax * ax + ay * ay) ** 0.5, 1); return ax / l * 10, ay / l * 10
            u1, u2 = unit(x1 - x, y1 - y), unit(x2 - x, y2 - y)
            out.append(f'<path d="M{x + u1[0]:.1f} {y + u1[1]:.1f} L{x + u1[0] + u2[0]:.1f} {y + u1[1] + u2[1]:.1f} L{x + u2[0]:.1f} {y + u2[1]:.1f}" fill="none" stroke="#0f172a"/>')
    for item in [t.strip() for t in kv.get('txt', '').split(';') if t.strip()]:
        lab, _, xy = item.rpartition(':')
        x, y = (float(c) for c in xy.split(','))
        out.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="13">{escape(lab)}</text>')
    label = kv.get('desc') or ('Polygon ' + ''.join(names))
    return f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{min(W, 300):.0f}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#0f172a">' + ''.join(out) + '</svg>'


def grid(spec):
    """'range=-7..7 | pts=A:7,5;B:-4,4 | lines=x=3;y=-2;pts:-1,-3:2,3 | labels=Quadrant I:4,6 | guides=1 | origin=Origin'
    Cartesian plane with integer grid. pts: labelled points. lines: vertical x=a, horizontal y=b,
    or a segment through two points 'pts:x1,y1:x2,y2' (extended to the grid edge). guides=1 draws dashed
    projections from each point to the axes. labels: free text at (x,y)."""
    kv = {}
    for part in spec.split('|'):
        if '=' in part:
            k, v = part.split('=', 1)
            kv[k.strip()] = v.strip()
    lo, hi = (int(t) for t in kv.get('range', '-7..7').split('..'))
    u = 22
    n = hi - lo
    pad = 34
    W = H = n * u + 2 * pad
    X = lambda x: pad + (x - lo) * u
    Y = lambda y: pad + (hi - y) * u
    out = []
    for i in range(lo, hi + 1):
        out.append(f'<line x1="{X(i)}" y1="{Y(hi)}" x2="{X(i)}" y2="{Y(lo)}" stroke="#cbd5e1" stroke-width="1"/>')
        out.append(f'<line x1="{X(lo)}" y1="{Y(i)}" x2="{X(hi)}" y2="{Y(i)}" stroke="#cbd5e1" stroke-width="1"/>')
    defs = '<defs><marker id="gr-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0f172a"/></marker></defs>'
    out.append(f'<line x1="{X(lo) - 14}" y1="{Y(0)}" x2="{X(hi) + 14}" y2="{Y(0)}" stroke="#0f172a" stroke-width="1.6" marker-start="url(#gr-a)" marker-end="url(#gr-a)"/>')
    out.append(f'<line x1="{X(0)}" y1="{Y(lo) + 14}" x2="{X(0)}" y2="{Y(hi) - 14}" stroke="#0f172a" stroke-width="1.6" marker-start="url(#gr-a)" marker-end="url(#gr-a)"/>')
    out.append(f'<text x="{X(hi) + 4}" y="{Y(0) - 8}" font-size="13" font-weight="700" text-anchor="end">X-axis</text>')
    out.append(f'<text x="{X(0) + 6}" y="{Y(hi) - 4}" font-size="13" font-weight="700">Y-axis</text>')
    for i in range(lo, hi + 1):
        if i:
            out.append(f'<text x="{X(i)}" y="{Y(0) + 15}" font-size="11" text-anchor="middle">{i}</text>')
            out.append(f'<text x="{X(0) - 4}" y="{Y(i) + 4}" font-size="11" text-anchor="end">{i}</text>')
    out.append(f'<text x="{X(0) - 4}" y="{Y(0) + 13}" font-size="11" text-anchor="end">0</text>')
    out.append(f'<circle cx="{X(0)}" cy="{Y(0)}" r="3.5" fill="#1d4ed8"/>')
    desc = []
    for ln in [t.strip() for t in kv.get('lines', '').split(';') if t.strip()]:
        if ln.startswith('x='):
            a = float(ln[2:])
            out.append(f'<line x1="{X(a)}" y1="{Y(lo)}" x2="{X(a)}" y2="{Y(hi)}" stroke="#dc2626" stroke-width="2.2"/>')
            out.append(f'<text x="{X(a) + 4}" y="{Y(hi) + 14}" font-size="13" fill="#dc2626" font-weight="700">x = {ln[2:]}</text>')
            desc.append(f'vertical line x = {ln[2:]}')
        elif ln.startswith('y='):
            b = float(ln[2:])
            out.append(f'<line x1="{X(lo)}" y1="{Y(b)}" x2="{X(hi)}" y2="{Y(b)}" stroke="#dc2626" stroke-width="2.2"/>')
            out.append(f'<text x="{X(lo) + 4}" y="{Y(b) - 5}" font-size="13" fill="#dc2626" font-weight="700">y = {ln[2:]}</text>')
            desc.append(f'horizontal line y = {ln[2:]}')
        elif ln.startswith('pts:'):
            p1, p2 = ln[4:].split(':')[:2]
            (x1, y1), (x2, y2) = [tuple(float(v) for v in p.split(',')) for p in (p1, p2)]
            if x1 == x2:
                ends = [(x1, lo), (x1, hi)]
            else:
                m = (y2 - y1) / (x2 - x1)
                cands = []
                for xe in (lo, hi):
                    ye = y1 + m * (xe - x1)
                    if lo <= ye <= hi:
                        cands.append((xe, ye))
                if m:
                    for ye in (lo, hi):
                        xe = x1 + (ye - y1) / m
                        if lo <= xe <= hi:
                            cands.append((xe, ye))
                cands = sorted(set(cands))
                ends = [cands[0], cands[-1]] if len(cands) >= 2 else [(x1, y1), (x2, y2)]
            lab = ln.split(':')[3] if ln.count(':') >= 3 else ''
            out.append(f'<line x1="{X(ends[0][0])}" y1="{Y(ends[0][1])}" x2="{X(ends[1][0])}" y2="{Y(ends[1][1])}" stroke="#dc2626" stroke-width="2.2"/>')
            if lab:
                out.append(f'<text x="{X(ends[1][0]) - 4}" y="{Y(ends[1][1]) + 16}" font-size="13" fill="#dc2626" font-weight="700" text-anchor="end">{escape(lab)}</text>')
            desc.append(f'line through ({p1}) and ({p2})' + (f' labelled {lab}' if lab else ''))
    for si, sh in enumerate([t.strip() for t in kv.get('shape', '').split('/') if t.strip()]):
        coords = [tuple(float(v) for v in c.split(',')) for c in sh.split(';') if c.strip()]
        col = ['#38bdf8', '#f472b6', '#4ade80'][si % 3]
        out.append(f'<polygon points="{" ".join(f"{X(x)},{Y(y)}" for x, y in coords)}" fill="{col}" fill-opacity="0.35" stroke="#0f172a" stroke-width="1.8"/>')
        desc.append('polygon with vertices ' + ', '.join(f'({x:g}, {y:g})' for x, y in coords))
    pts = []
    for p in [t.strip() for t in kv.get('pts', '').split(';') if t.strip()]:
        name, _, xy = p.rpartition(':')
        x, y = (float(v) for v in xy.split(','))
        pts.append((name, x, y, xy))
        if kv.get('guides') == '1':
            out.append(f'<path d="M{X(x)} {Y(0)} V{Y(y)} H{X(0)}" fill="none" stroke="#db2777" stroke-width="1.4" stroke-dasharray="4 3"/>')
        out.append(f'<circle cx="{X(x)}" cy="{Y(y)}" r="4" fill="#be123c"/>')
        lbl = f'{name} ({xy.replace(",", ", ")})' if name else f'({xy.replace(",", ", ")})'
        if kv.get('nameonly') == '1':
            lbl = name
        anchor = 'end' if x > (lo + hi) / 2 else 'start'
        dx = -7 if anchor == 'end' else 7
        if kv.get('nolabel') != '1':
            out.append(f'<text x="{X(x) + dx}" y="{Y(y) - 7}" font-size="13" font-weight="700" text-anchor="{anchor}" paint-order="stroke" stroke="#fff" stroke-width="3">{escape(lbl)}</text>')
    for lb in [t.strip() for t in kv.get('labels', '').split(';') if t.strip()]:
        txt, _, xy = lb.rpartition(':')
        x, y = (float(v) for v in xy.split(','))
        out.append(f'<text x="{X(x)}" y="{Y(y)}" font-size="13" font-weight="700" fill="#be185d" text-anchor="middle" paint-order="stroke" stroke="#fff" stroke-width="3">{escape(txt)}</text>')
    if kv.get('origin'):
        out.append(f'<text x="{X(0) + 8}" y="{Y(0) + 28}" font-size="12" font-weight="700">{escape(kv["origin"])} (0, 0)</text>')
    label = f'Cartesian plane from {lo} to {hi} on both axes' + (('; points ' + ', '.join(f'{n} ({xy})'.strip() for n, _, _, xy in pts)) if pts else '') + (('; ' + '; '.join(desc)) if desc else '')
    return f'<svg viewBox="0 0 {W} {H}" width="{min(W, 420)}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + defs + ''.join(out) + '</svg>'


def venn(spec):
    """'layout=overlap | U=U | names=A,B | a=1,2 | b=3 | ab=4 | o=5 | shade=ab,a'
    layout: single (one set), overlap, disjoint, subset (B drawn inside A).
    Regions: a = only in A, b = only in B (inside B for subset), ab = in both, o = outside the sets (in U).
    shade: comma list of regions (a, b, ab, o) to fill."""
    kv = {}
    for part in spec.split('|'):
        if '=' in part:
            k, v = part.split('=', 1)
            kv[k.strip()] = v.strip()
    layout = kv.get('layout', 'overlap')
    names = [x.strip() for x in kv.get('names', 'A,B').split(',')]
    reg = {k: [x.strip() for x in kv.get(k, '').split(',') if x.strip()] for k in ('a', 'b', 'ab', 'o')}
    shade = {x.strip() for x in kv.get('shade', '').split(',') if x.strip()}
    W, H = 380, 220
    fill, sh = '#ffffff', '#93c5fd'
    defs, body, clips = [], [], []

    def words(items, cx, cy, maxw=4):
        out, rows = [], [items[i:i + maxw] for i in range(0, len(items), maxw)] or []
        y0 = cy - (len(rows) - 1) * 10
        for r, row in enumerate(rows):
            out.append(f'<text x="{cx}" y="{y0 + r * 20 + 5}" text-anchor="middle">{escape(", ".join(row))}</text>')
        return ''.join(out)

    rect = f'<rect x="4" y="4" width="{W - 8}" height="{H - 8}" fill="{sh if "o" in shade else fill}" stroke="#0f172a" stroke-width="1.6"/>'
    body.append(rect)
    body.append(f'<text x="14" y="26" font-weight="700">{escape(kv.get("U", "U"))}</text>')
    if layout == 'single':
        body.append(f'<ellipse cx="190" cy="115" rx="120" ry="70" fill="{sh if "a" in shade else fill}" stroke="#0f172a" stroke-width="1.6"/>')
        body.append(f'<text x="95" y="80" font-weight="700">{escape(names[0])}</text>')
        body.append(words(reg['a'], 195, 118))
        body.append(words(reg['o'], 330, 200, 3))
    elif layout == 'disjoint':
        for i, (cx, key) in enumerate(((110, 'a'), (270, 'b'))):
            body.append(f'<circle cx="{cx}" cy="115" r="72" fill="{sh if key in shade else fill}" stroke="#0f172a" stroke-width="1.6"/>')
            body.append(f'<text x="{cx - 58}" y="62" font-weight="700">{escape(names[i] if i < len(names) else "")}</text>')
            body.append(words(reg[key], cx, 118, 3))
        body.append(words(reg['o'], 190, 205, 6))
    elif layout == 'subset':
        body.append(f'<ellipse cx="190" cy="115" rx="150" ry="88" fill="{sh if "a" in shade else fill}" stroke="#0f172a" stroke-width="1.6"/>')
        body.append(f'<ellipse cx="225" cy="118" rx="75" ry="48" fill="{sh if "b" in shade else fill}" stroke="#0f172a" stroke-width="1.6"/>')
        body.append(f'<text x="62" y="70" font-weight="700">{escape(names[0])}</text>')
        body.append(f'<text x="165" y="92" font-weight="700">{escape(names[1] if len(names) > 1 else "")}</text>')
        body.append(words(reg['a'], 100, 120, 2))
        body.append(words(reg['b'], 228, 125, 3))
        body.append(words(reg['o'], 330, 205, 3))
    else:
        ca, cb, r = (140, 115), (240, 115), 80
        defs.append(f'<clipPath id="vA{id(spec)}"><circle cx="{ca[0]}" cy="{ca[1]}" r="{r}"/></clipPath>')
        body.append(f'<circle cx="{ca[0]}" cy="{ca[1]}" r="{r}" fill="{sh if "a" in shade else fill}" stroke="none"/>')
        body.append(f'<circle cx="{cb[0]}" cy="{cb[1]}" r="{r}" fill="{sh if "b" in shade else fill}" stroke="none"/>')
        body.append(f'<circle cx="{cb[0]}" cy="{cb[1]}" r="{r}" fill="{sh if "ab" in shade else fill}" clip-path="url(#vA{id(spec)})"/>')
        body.append(f'<circle cx="{ca[0]}" cy="{ca[1]}" r="{r}" fill="none" stroke="#0f172a" stroke-width="1.6"/>')
        body.append(f'<circle cx="{cb[0]}" cy="{cb[1]}" r="{r}" fill="none" stroke="#0f172a" stroke-width="1.6"/>')
        body.append(f'<text x="{ca[0] - 70}" y="52" font-weight="700">{escape(names[0])}</text>')
        body.append(f'<text x="{cb[0] + 55}" y="52" font-weight="700">{escape(names[1] if len(names) > 1 else "")}</text>')
        body.append(words(reg['a'], 105, 118, 2))
        body.append(words(reg['ab'], 190, 118, 1))
        body.append(words(reg['b'], 275, 118, 2))
        body.append(words(reg['o'], 330, 205, 3))
    desc = {'single': f'one set {names[0]}', 'disjoint': f'disjoint sets {" and ".join(names)}',
            'subset': f'{names[-1]} inside {names[0]}', 'overlap': f'overlapping sets {" and ".join(names)}'}[layout]
    parts = [f'{k}: {", ".join(v)}' for k, v in (('only ' + names[0], reg['a']), (('only ' + names[1]) if len(names) > 1 else 'b', reg['b']),
                                                 ('both', reg['ab']), ('outside', reg['o'])) if v]
    label = f'Venn diagram, universal set {kv.get("U", "U")}, {desc}' + ('; ' + '; '.join(parts) if parts else '') + (f'; shaded: {", ".join(sorted(shade))}' if shade else '')
    return (f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" font-size="15" fill="#0f172a">'
            + (f'<defs>{"".join(defs)}</defs>' if defs else '') + ''.join(body) + '</svg>')


def proptable(spec):
    """'Dresses | Time | 5, x | 3, 12 | down, down' — two-column proportion table with direction arrows
    (same direction = direct proportion, opposite = inverse proportion)."""
    h1, h2, c1, c2, dirs = [p.strip() for p in spec.split('|')]
    c1 = [x.strip() for x in c1.split(',')]
    c2 = [x.strip() for x in c2.split(',')]
    d1, d2 = [x.strip() for x in dirs.split(',')]
    n = len(c1)
    W, top, lh = 300, 30, 28
    H = top + n * lh + 14
    out = [f'<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="#fef9c3" stroke="#a16207" stroke-dasharray="3 2"/>',
           f'<text x="80" y="{top - 6}" text-anchor="middle" font-weight="700">{escape(h1)}</text>',
           f'<text x="150" y="{top - 6}" text-anchor="middle">:</text>',
           f'<text x="220" y="{top - 6}" text-anchor="middle" font-weight="700">{escape(h2)}</text>']
    for i in range(n):
        y = top + (i + 1) * lh - 6
        out.append(f'<text x="86" y="{y}" text-anchor="start" font-style="{"italic" if c1[i].isalpha() else "normal"}">{escape(c1[i])}</text>')
        out.append(f'<text x="150" y="{y}" text-anchor="middle">:</text>')
        out.append(f'<text x="226" y="{y}" text-anchor="start" font-style="{"italic" if c2[i].isalpha() else "normal"}">{escape(c2[i])}</text>')
    y0, y1 = top + 6, top + n * lh - 2
    for x, d in ((76, d1), (216, d2)):
        a, b = (y0, y1) if d == 'down' else (y1, y0)
        out.append(f'<line x1="{x}" y1="{a}" x2="{x}" y2="{b}" stroke="#dc2626" stroke-width="2" marker-end="url(#pt-a)"/>')
    defs = '<defs><marker id="pt-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#dc2626"/></marker></defs>'
    kind = 'same direction (direct proportion)' if d1 == d2 else 'opposite directions (inverse proportion)'
    label = f'{h1} : {h2}; ' + '; '.join(f'{a} : {b}' for a, b in zip(c1, c2)) + f'; arrows point in {kind}'
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" font-size="16" fill="#0f172a">' + defs + ''.join(out) + '</svg>'


def meansext(spec):
    """'a : b :: c : d' — proportion with a 'means' bracket over terms 2–3 and an 'extremes' bracket under terms 1 and 4."""
    toks = spec.split()
    xs, x, out = [], 30, []
    for t in toks:
        w = max(len(t), 1) * 13 + 14
        cx = x + w / 2
        out.append(f'<text x="{cx}" y="78" text-anchor="middle" font-size="24" font-weight="700">{escape(t)}</text>')
        xs.append(cx)
        x += w
    terms = [xs[i] for i in (0, 2, 4, 6)]
    red = '#dc2626'
    out.append(f'<path d="M{terms[1]} 54 V36 H{terms[2]} V54" fill="none" stroke="{red}" stroke-width="1.8" marker-end="url(#me-a)"/>')
    out.append(f'<line x1="{terms[1]}" y1="36" x2="{terms[1]}" y2="54" stroke="{red}" stroke-width="1.8" marker-end="url(#me-a)"/>')
    out.append(f'<text x="{(terms[1] + terms[2]) / 2}" y="26" text-anchor="middle" font-size="18" font-weight="700">means</text>')
    out.append(f'<path d="M{terms[0]} 90 V106 H{terms[3]} V90" fill="none" stroke="{red}" stroke-width="1.8" marker-end="url(#me-a)"/>')
    out.append(f'<line x1="{terms[0]}" y1="106" x2="{terms[0]}" y2="90" stroke="{red}" stroke-width="1.8" marker-end="url(#me-a)"/>')
    out.append(f'<text x="{(terms[0] + terms[3]) / 2}" y="130" text-anchor="middle" font-size="18" font-weight="700">extremes</text>')
    defs = f'<defs><marker id="me-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="{red}"/></marker></defs>'
    label = f'Proportion {spec}: means are {toks[2]} and {toks[4]}, extremes are {toks[0]} and {toks[6]}'
    return f'<svg viewBox="0 0 {x + 30} 140" width="{x + 30}" role="img" aria-label="{escape(label)}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + defs + ''.join(out) + '</svg>'


def shapes(spec):
    """'bar:5:5@5/5=1 + bar:5:2@2/5' or 'pie:3:3' : fraction models joined by the printed operator.
    bar:n:k = rectangle cut into n equal cells with the first k shaded; pie:n:k = circle cut into n equal sectors.
    '@label' under a model; a/b text renders as a stacked fraction (optionally followed by '=text')."""
    import math
    tokens = re.split(r'\s+([+=−-])\s+', spec.strip())
    out, x, H = [], 6, 110

    def lab(cx, y, txt):
        m = re.match(r'^(\d+)/(\d+)(.*)$', txt)
        if not m:
            return f'<text x="{cx}" y="{y + 14}" text-anchor="middle" font-size="14">{escape(txt)}</text>'
        num, den, rest = m.groups()
        return (f'<text x="{cx}" y="{y + 10}" text-anchor="middle" font-size="13">{num}</text><line x1="{cx - 8}" y1="{y + 14}" x2="{cx + 8}" y2="{y + 14}" stroke="#0f172a"/>'
                f'<text x="{cx}" y="{y + 28}" text-anchor="middle" font-size="13">{den}</text>' + (f'<text x="{cx + 11}" y="{y + 19}" font-size="14">{escape(rest)}</text>' if rest else ''))
    descr = []
    for tok in tokens:
        if tok in '+=−-':
            out.append(f'<text x="{x + 8}" y="40" text-anchor="middle" font-size="18">{tok}</text>')
            x += 22
            descr.append(tok)
            continue
        body, _, label = tok.partition('@')
        kind, n, k = body.split(':')
        n, k = int(n), int(k)
        if kind == 'bar':
            cw = 34
            for i in range(n):
                out.append(f'<rect x="{x + i * cw}" y="16" width="{cw}" height="40" fill="{"#7dd3fc" if i < k else "#fff"}" stroke="#0f172a" stroke-width="1.3"/>')
            cx = x + n * cw / 2
            x += n * cw + 8
        else:
            r, cx0, cy = 34, x + 36, 40
            for i in range(n):
                a0, a1 = 2 * math.pi * i / n - math.pi / 2, 2 * math.pi * (i + 1) / n - math.pi / 2
                big = 1 if a1 - a0 > math.pi else 0
                d = (f'M{cx0} {cy} L{cx0 + r * math.cos(a0):.1f} {cy + r * math.sin(a0):.1f} A{r} {r} 0 {big} 1 {cx0 + r * math.cos(a1):.1f} {cy + r * math.sin(a1):.1f} Z'
                     if n > 1 else f'M{cx0 - r} {cy} a{r} {r} 0 1 0 {2 * r} 0 a{r} {r} 0 1 0 {-2 * r} 0')
                out.append(f'<path d="{d}" fill="{"#fde047" if i < k else "#fff"}" stroke="#0f172a" stroke-width="1.3"/>')
            cx = cx0
            x += 80
        if label:
            out.append(lab(cx, 64, label))
        descr.append(f'{kind} of {n} equal parts with {k} shaded' + (f' ({label})' if label else ''))
    return f'<svg viewBox="0 0 {x + 4} {H}" width="{x + 4}" role="img" aria-label="{escape("; ".join(descr))}" font-family="Segoe UI, Arial, sans-serif" fill="#0f172a">' + ''.join(out) + '</svg>'


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
