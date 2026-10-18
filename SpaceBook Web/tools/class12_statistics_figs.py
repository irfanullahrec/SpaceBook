"""Coded SVG figures shared by Statistics XII page scripts."""
import html

E = html.escape


def svg_open(w, h, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{E(label)}"><rect width="{w}" height="{h}" fill="white"/>'


def venn_complement(label='Venn diagram of A and its complement'):
    """Rectangle S with circle A; complement shaded region outside the circle."""
    return (svg_open(320, 200, label) +
            '<rect x="40" y="10" width="270" height="180" fill="#bfdbfe" stroke="#1e3a8a" stroke-width="2"/>'
            '<circle cx="140" cy="100" r="75" fill="#bfdbfe" stroke="#111" stroke-width="2.5"/>'
            '<g font-family="Times New Roman,serif" font-size="18" fill="#111" text-anchor="middle">'
            '<text x="20" y="106">S =</text><text x="140" y="106">A</text>'
            '<text x="262" y="106">A</text><path d="M255 86h14" stroke="#111"/></g></svg>')


def venn_two(shade=None, labels=('A', 'B'), overlap=True, label='Venn diagram'):
    """Two circles in S. shade: None|'A'|'B'|'AB'|'union'|'Aonly'|'Bonly'."""
    a, b = labels
    cx2 = 190 if overlap else 230
    s = [svg_open(320, 200, label), '<defs><clipPath id="vA"><circle cx="120" cy="100" r="62"/></clipPath></defs>',
         '<rect x="10" y="10" width="300" height="180" fill="#fff" stroke="#1e3a8a" stroke-width="2"/>']
    fill = '#93c5fd'
    if shade in ('A', 'union', 'Aonly'):
        s.append(f'<circle cx="120" cy="100" r="62" fill="{fill}"/>')
    if shade in ('B', 'union', 'Bonly'):
        s.append(f'<circle cx="{cx2}" cy="100" r="62" fill="{fill}"/>')
    if shade == 'AB' and overlap:
        s.append(f'<circle cx="{cx2}" cy="100" r="62" fill="{fill}" clip-path="url(#vA)"/>')
    if shade == 'Aonly' and overlap:
        s.append(f'<circle cx="{cx2}" cy="100" r="62" fill="#fff" clip-path="url(#vA)"/>')
    if shade == 'Bonly' and overlap:
        s.append(f'<circle cx="{cx2}" cy="100" r="62" fill="#fff" clip-path="url(#vA)"/><circle cx="120" cy="100" r="62" fill="none"/>')
    s.append(f'<circle cx="120" cy="100" r="62" fill="none" stroke="#111" stroke-width="2"/><circle cx="{cx2}" cy="100" r="62" fill="none" stroke="#111" stroke-width="2"/>')
    s.append(f'<g font-family="Times New Roman,serif" font-size="18" fill="#111" text-anchor="middle"><text x="24" y="32">S</text>'
             f'<text x="{95 if overlap else 120}" y="106">{E(a)}</text><text x="{215 if overlap else cx2}" y="106">{E(b)}</text></g></svg>')
    return ''.join(s)


DICE36 = (r'S=\left\{\begin{matrix}' + (chr(92)*2+' ').join(', & '.join(f'({i},{j})' for j in range(1, 7)) for i in range(1, 7)) + r'\end{matrix}\right\}')


def venn_regions(label='Venn diagram with regions A∩B̄, A∩B, Ā∩B'):
    """Two overlapping circles in S with pointer labels to the three regions (as printed in 1.3.2)."""
    s = [svg_open(320, 210, label),
         '<rect x="20" y="10" width="260" height="160" fill="#dbeafe" stroke="#111" stroke-width="2"/>',
         '<circle cx="120" cy="80" r="55" fill="none" stroke="#111" stroke-width="2"/><circle cx="185" cy="80" r="55" fill="none" stroke="#111" stroke-width="2"/>',
         '<path d="M95 100L40 186M152 92L152 186M210 100L250 186" stroke="#111"/>',
         '<g font-family="Times New Roman,serif" font-size="15" fill="#111" text-anchor="middle">',
         '<text x="105" y="20">A</text><text x="200" y="20">B</text><text x="300" y="86">= S</text>',
         '<text x="40" y="202">A∩B̄</text><text x="152" y="202">A∩B</text><text x="255" y="202">Ā∩B</text></g></svg>']
    return ''.join(s)


def uniform_histogram(label='Histogram of the discrete uniform distribution'):
    """Equal-height adjacent rectangles with P(x)=1/N axis label, ticks 1, 2, …, N (as printed in 3.1.3)."""
    s = [svg_open(340, 200, label), '<g stroke="#111" fill="none" stroke-width="1.6">',
         '<path d="M80 165V20M80 165H300"/><path d="M80 14l-4 9h8z" fill="#111"/><path d="M306 165l-9-4v8z" fill="#111"/>',
         '<rect x="95" y="38" width="190" height="127"/><path d="M128 38V165M157 38V165M235 38V165"/></g>',
         '<g font-family="Times New Roman,serif" font-size="15" fill="#111" text-anchor="middle">',
         '<text x="40" y="44" font-size="13">P(x)=1/N</text><text x="196" y="96">…</text><text x="111" y="186">1</text><text x="142" y="186">2</text>',
         '<text x="260" y="186">N</text><text x="318" y="170">x</text></g></svg>']
    return ''.join(s)


def population_box(top, bottom, ktop, ntext, label='Population box'):
    """Two-row population box (e.g. 6R_A / 5R_B) with a K arrow at the top row (ktop=True) or bottom row, and N → total below.
    top/bottom are (main, subscript) tuples; ntext is the language-specific total label."""
    ky = 31 if ktop else 58
    def lab(y, v):
        main, sub = v
        return f'<text x="106" y="{y}" font-style="italic">{E(main)}<tspan font-size="12" dy="4">{E(sub)}</tspan></text>'
    return (svg_open(260, 120, label) + '<g font-family="Times New Roman,serif" font-size="18" fill="#111">'
            '<rect x="100" y="10" width="54" height="54" fill="none" stroke="#111"/><path d="M100 37H154" stroke="#111"/>'
            + lab(31, top) + lab(58, bottom) +
            f'<path d="M162 {ky-6}H210" stroke="#111"/><path d="M162 {ky-6}l9-4v8z" fill="#111"/><text x="218" y="{ky}" font-style="italic">K</text>'
            '<text x="40" y="100" font-style="italic">N</text><path d="M58 94H96" stroke="#111"/><path d="M104 94l-9-4v8z" fill="#111"/>'
            f'<text x="110" y="100">{E(ntext)}</text></g></svg>')


def continuous_uniform(label='Continuous uniform density: rectangle of height 1/(b−a) between a and b'):
    """f(x) axis, 1/(b−a) level, rectangle from a to b on the X axis (as printed in 4.1.2)."""
    return (svg_open(320, 220, label) + '<rect x="0" y="0" width="320" height="220" fill="#dbeafe"/>'
            '<g stroke="#111" fill="none" stroke-width="1.6"><path d="M60 190V20M60 190H300"/>'
            '<path d="M50 95H80"/><rect x="140" y="95" width="130" height="95"/></g>'
            '<g font-family="Times New Roman,serif" font-size="15" fill="#111" text-anchor="middle">'
            '<text x="40" y="28">f(x)</text><text x="35" y="90">1</text><path d="M22 95H48" stroke="#111"/><text x="35" y="112">b−a</text>'
            '<text x="55" y="206">o</text><text x="140" y="208">a</text><text x="270" y="208">b</text><text x="308" y="194">X</text></g></svg>')


import math as _m


def bell_path(cx=300, base=170, top=40, sd=70, x0=60, x1=540, step=4):
    pts = []
    for x in range(x0, x1 + 1, step):
        z = (x - cx) / sd
        pts.append(f'{x} {base - (base - top) * _m.exp(-z * z / 2):.1f}')
    return 'M' + 'L'.join(pts)


def normal_empirical(label='Normal curve with 68.3%, 95.4% and 99.7% within 1, 2 and 3 standard deviations'):
    """Bell curve on a blue panel; halves 0.5 / 0.5; ticks μ±σ, μ±2σ, μ±3σ; nested brackets for 68.3 / 95.4 / 99.7 %."""
    cx, sd, base = 300, 62, 150
    s = [svg_open(600, 300, label), '<rect width="600" height="300" fill="#bfdbfe"/>',
         f'<path d="{bell_path(cx, base, 30, sd, 30, 570)}" fill="none" stroke="#111" stroke-width="2"/>',
         f'<path d="M20 {base}H580M{cx} {base}V30" stroke="#111"/>']
    labs = ['μ-3σ', 'μ-2σ', 'μ-σ', '', 'μ+σ', 'μ+2σ', 'μ+3σ']
    for i, l in enumerate(labs):
        x = cx + (i - 3) * sd
        if l:
            s.append(f'<path d="M{x} {base-6}V{base+6}" stroke="#111"/><text x="{x}" y="{base+22}" text-anchor="middle" font-size="14">{l}</text>')
    for k, (pct, y) in enumerate([('68.3%', 190), ('95.4%', 222), ('99.7%', 254)], start=1):
        l, r = cx - k * sd, cx + k * sd
        s.append(f'<path d="M{l} {base+28}V{y}H{r}V{base+28}" fill="none" stroke="#111"/>'
                 f'<rect x="{cx-28}" y="{y-11}" width="56" height="20" fill="#bfdbfe"/><text x="{cx}" y="{y+5}" text-anchor="middle" font-size="14">{pct}</text>')
    s.append(f'<g font-family="Times New Roman,serif" font-size="15" fill="#111" text-anchor="middle"><text x="{cx-24}" y="80">0.5</text><text x="{cx+24}" y="80">0.5</text>'
             f'<text x="40" y="{base-6}">X−∞</text><text x="565" y="{base-6}">∞</text></g></svg>')
    return ''.join(s).replace('font-size="14">', 'font-size="14" font-family="Times New Roman,serif">')


def normal_shaded(a=None, b=None, labels=(), label='Standard normal curve with shaded area', marks=None, fill='#bae6fd', panel='#dbeafe', w=420, h=170, notes=(), zlabel=''):
    """Standard normal curve (z from −3.4 to 3.4) with the region between z=a and z=b shaded.
    labels: (z, text) pairs printed under the axis. marks: z positions for vertical lines."""
    cx, sd, base, top = w / 2, w / 7.4, h - 40, 18
    X = lambda z: cx + z * sd
    def curve_pts(z0, z1, n=60):
        return [(X(z0 + (z1 - z0) * i / n), base - (base - top) * _m.exp(-((z0 + (z1 - z0) * i / n) ** 2) / 2)) for i in range(n + 1)]
    s = [svg_open(w, h, label), f'<rect width="{w}" height="{h}" fill="{panel}"/>']
    if a is not None or b is not None:
        za = -3.6 if a is None else a
        zb = 3.6 if b is None else b
        pts = curve_pts(za, zb)
        s.append(f'<path d="M{X(za):.1f} {base}' + ''.join(f'L{x:.1f} {y:.1f}' for x, y in pts) + f'L{X(zb):.1f} {base}Z" fill="{fill}" stroke="none"/>')
    pts = curve_pts(-3.6, 3.6, 120)
    s.append('<path d="M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + '" fill="none" stroke="#111" stroke-width="1.8"/>')
    s.append(f'<path d="M8 {base}H{w-8}" stroke="#111"/>')
    for z in (marks or []):
        y = base - (base - top) * _m.exp(-z * z / 2)
        s.append(f'<path d="M{X(z):.1f} {base}V{y:.1f}" stroke="#111"/>')
    s.append('<g font-family="Times New Roman,serif" font-size="14" fill="#111" text-anchor="middle">')
    s.append(f'<text x="24" y="{base-6}">−∞</text><text x="{w-22}" y="{base-6}">∞</text>')
    for z, t in labels:
        s.append(f'<text x="{X(z):.1f}" y="{base+18}">{E(t)}</text>')
    for z, frac, t in notes:
        s.append(f'<text x="{X(z):.1f}" y="{base-(base-top)*frac:.1f}">{E(t)}</text>')
    if zlabel:
        s.append(f'<text x="{w-10}" y="{base+4}">{E(zlabel)}</text>')
    s.append('</g></svg>')
    return ''.join(s)


def paired_curves(a, b, xlabels, zlabels, xaxis='X', zaxis='Z', label='Area under the normal curve on the X scale and the standardized Z scale'):
    """Two stacked normal curves (original X scale on top, standardized Z below) with the same region shaded.
    a, b: z-limits (None = open). xlabels / zlabels: (z, text) pairs; marks drawn at each labelled z."""
    top = normal_shaded(a, b, labels=xlabels, marks=tuple(z for z, _ in xlabels), w=300, h=120, zlabel=xaxis, label=label)
    bot = normal_shaded(a, b, labels=zlabels, marks=tuple(z for z, _ in zlabels), w=300, h=120, zlabel=zaxis, label=label)
    body = lambda s: s[s.index('>') + 1:s.rindex('</svg>')]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 244" role="img" aria-label="{E(label)}">'
            f'<g>{body(top)}</g><g transform="translate(0,124)">{body(bot)}</g></svg>')


def strata_tree(lang='en', label='Population N divided into strata N1…Nk with random samples n1…nk'):
    T = {'en': ('(Population)', '(strata)', '(random samples from strata)'),
         'ur': ('(آبادی)', '(طبقات)', '(طبقات سے تصادفی نمونے)'),
         'ps': ('(نفوس)', '(طبقې)', '(له طبقو تصادفي نمونې)')}[lang]
    xs = [60, 120, 180, 300]
    s = [svg_open(580, 170, label), '<g font-family="Times New Roman,serif" font-size="16" fill="#111" text-anchor="middle">',
         '<circle cx="180" cy="22" r="13" fill="none" stroke="#111"/><text x="180" y="28">N</text>',
         f'<text x="345" y="28" text-anchor="start">{E(T[0])}</text>',
         '<path d="M180 35V50M60 50H300M60 50V70M120 50V70M180 50V70M300 50V70" stroke="#111" fill="none"/>']
    for i, x in enumerate(xs):
        k = 'k' if i == 3 else str(i + 1)
        s.append(f'<text x="{x}" y="90">N<tspan font-size="11" dy="4">{k}</tspan></text>'
                 f'<path d="M{x} 98V118" stroke="#111"/><path d="M{x-4} 112L{x} 120L{x+4} 112Z" fill="#111"/>'
                 f'<text x="{x}" y="140">n<tspan font-size="11" dy="4">{k}</tspan></text>')
    s.append('<text x="240" y="88" letter-spacing="2">…………</text><text x="240" y="138" letter-spacing="2">…………</text>')
    s.append(f'<text x="345" y="90" text-anchor="start">{E(T[1])}</text><text x="345" y="140" text-anchor="start">{E(T[2])}</text></g></svg>')
    return ''.join(s)


def two_tail(lo_label, hi_label, mid='1−α', tail='α/2', z=1.96, label='Two-tailed confidence region'):
    """Standard normal curve with both tails shaded beyond ±z, labelled α/2, 1−α, α/2 and limit labels under the axis."""
    w, h = 320, 130
    cx, sd, base, top = w / 2, w / 7.4, h - 32, 14
    X = lambda v: cx + v * sd
    def pts(z0, z1, n=40):
        return [(X(z0 + (z1 - z0) * i / n), base - (base - top) * _m.exp(-((z0 + (z1 - z0) * i / n) ** 2) / 2)) for i in range(n + 1)]
    s = [svg_open(w, h, label), f'<rect width="{w}" height="{h}" fill="#dbeafe"/>']
    for z0, z1 in ((-3.6, -z), (z, 3.6)):
        p = pts(z0, z1)
        s.append(f'<path d="M{X(z0):.1f} {base}' + ''.join(f'L{x:.1f} {y:.1f}' for x, y in p) + f'L{X(z1):.1f} {base}Z" fill="#fff"/>')
    s.append('<path d="M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts(-3.6, 3.6, 120)) + '" fill="none" stroke="#111" stroke-width="1.8"/>')
    s.append(f'<path d="M6 {base}H{w-6}M{X(-z):.1f} {base}V{base-(base-top)*_m.exp(-z*z/2):.1f}M{X(z):.1f} {base}V{base-(base-top)*_m.exp(-z*z/2):.1f}" stroke="#111"/>')
    s.append('<g font-family="Times New Roman,serif" font-size="14" fill="#111" text-anchor="middle">')
    s.append(f'<text x="{X(-2.6):.1f}" y="{base-34}">{E(tail)}</text><text x="{cx}" y="{base-48}">{E(mid)}</text><text x="{X(2.6):.1f}" y="{base-34}">{E(tail)}</text>')
    s.append(f'<text x="18" y="{base-4}">−∞</text><text x="{w-14}" y="{base-4}">∞</text>')
    s.append(f'<text x="{X(-z):.1f}" y="{base+18}">{E(lo_label)}</text><text x="{X(z):.1f}" y="{base+18}">{E(hi_label)}</text></g></svg>')
    return ''.join(s)


def t_two_tail(label='t-distribution with critical values ±t(α/2, ν)'):
    """Two-tailed t curve with labels α/2, 1−α, α/2 and ±t_{α/2,(υ)} under the axis."""
    return two_tail('−tα/2,(υ)', 'tα/2,(υ)', label=label).replace('>−∞<', '>t−∞<')


def ci_ladder(lang='en', label='100 confidence intervals stacked around μ; intervals 3 and 97 miss μ'):
    """Stacked interval bars around μ as printed: bars 1–4 at the bottom and 96–100 at the top (8 px apart),
    a dotted run of tiny bars in between; intervals 3 and 97 miss μ."""
    yl = {'en': 'Interval Number', 'ur': 'وقفے کا نمبر', 'ps': 'د واټن شمېره'}[lang]
    w, h, mu = 300, 270, 175
    s = [svg_open(w, h, label), '<g stroke="#111" fill="none">', '<path d="M60 236V14M60 236H285"/><path d="M285 236l-8-4v8z" fill="#111"/>']
    Y = lambda i: 228 - (i - 1) * 8 if i <= 4 else 30 + (100 - i) * 8
    bars = {1: (150, 205), 2: (158, 196), 3: (112, 160), 4: (150, 192), 96: (152, 192), 97: (182, 230), 98: (150, 198), 99: (156, 206), 100: (148, 190)}
    for i, (x0, x1) in bars.items():
        s.append(f'<path d="M{x0} {Y(i)}H{x1}" stroke-width="1.6"/>')
    for k in range(18):
        y = 66 + k * 8.4
        s.append(f'<path d="M{mu-3} {y:.1f}H{mu+3}"/>')
    s.append(f'<path d="M{mu} 236V18"/></g>')
    s.append('<g font-family="Times New Roman,serif" font-size="12" fill="#111" text-anchor="end">')
    for v in (20, 40, 60, 80, 100):
        y = 236 - v * 2.1
        s.append(f'<text x="56" y="{y+4:.0f}">{v}</text><path d="M58 {y:.0f}H62" stroke="#111"/>')
    for i, (x0, x1) in bars.items():
        if i in (3, 97, 1, 99):
            x = x1 + 12 if i in (97, 1, 99) else x0 - 10
            s.append(f'<text x="{x}" y="{Y(i)+4}" font-size="10" text-anchor="middle">{i}</text>')
        else:
            s.append(f'<text x="{x0-10}" y="{Y(i)+4}" font-size="10" text-anchor="middle">{i}</text>')
    s.append(f'<text x="{mu}" y="254" text-anchor="middle" font-style="italic" font-size="14">μ</text>')
    s.append(f'<text x="18" y="125" font-size="12" text-anchor="middle" transform="rotate(-90 18 125)">{E(yl)}</text></g></svg>')
    return ''.join(s)

def tail_test(kind, caption='', z=1.4, mid='1−α', tail=None, region_labels=None, label='Normal curve with rejection region', ticks=()):
    """kind: 'right' | 'left' | 'two'. Shaded tail(s) beyond ±z; caption under the axis; optional region labels
    region_labels = (left_text, centre_text, right_text) printed under the axis at tail/centre positions."""
    w, h = 320, 150 if region_labels else 128
    cx, sd, base, top = w / 2, w / 7.4, 100, 14
    X = lambda v: cx + v * sd
    def pts(z0, z1, n=40):
        return [(X(z0 + (z1 - z0) * i / n), base - (base - top) * _m.exp(-((z0 + (z1 - z0) * i / n) ** 2) / 2)) for i in range(n + 1)]
    s = [svg_open(w, h, label), f'<rect width="{w}" height="{h}" fill="#dbeafe"/>']
    spans = {'right': [(z, 3.6)], 'left': [(-3.6, -z)], 'two': [(-3.6, -z), (z, 3.6)]}[kind]
    for z0, z1 in spans:
        p = pts(z0, z1)
        s.append(f'<path d="M{X(z0):.1f} {base}' + ''.join(f'L{x:.1f} {y:.1f}' for x, y in p) + f'L{X(z1):.1f} {base}Z" fill="#fff"/>')
    s.append('<path d="M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts(-3.6, 3.6, 120)) + '" fill="none" stroke="#111" stroke-width="1.8"/>')
    s.append(f'<path d="M6 {base}H{w-6}" stroke="#111"/>')
    for zz in ([z] if kind == 'right' else [-z] if kind == 'left' else [-z, z]):
        s.append(f'<path d="M{X(zz):.1f} {base}V{base-(base-top)*_m.exp(-zz*zz/2):.1f}" stroke="#111"/>')
    t = tail or ('α' if kind != 'two' else 'α/2')
    s.append('<g font-family="Times New Roman,serif" font-size="14" fill="#111" text-anchor="middle">')
    mx = {'right': -0.5, 'left': 0.5, 'two': 0}[kind]
    s.append(f'<text x="{X(mx):.1f}" y="{base-42}">{E(mid)}</text>')
    if kind in ('right', 'two'):
        s.append(f'<text x="{X(z+0.9):.1f}" y="{base-30}">{E(t)}</text>')
    if kind in ('left', 'two'):
        s.append(f'<text x="{X(-z-0.9):.1f}" y="{base-30}">{E(t)}</text>')
    if region_labels:
        for xx, txt in ((X(-z - 0.9), region_labels[0]), (cx, region_labels[1]), (X(z + 0.9), region_labels[2])):
            for k, line in enumerate(str(txt).split(' / ')):
                s.append(f'<text x="{xx:.1f}" y="{base + 16 + k * 14}" font-size="11">{E(line)}</text>')
    for zz, txt in ticks:
        s.append(f'<text x="{X(zz):.1f}" y="{base + 16}" font-size="12">{E(txt)}</text>')
    if caption:
        s.append(f'<text x="{cx}" y="{h-8}" font-size="13" font-weight="bold">{E(caption)}</text>')
    s.append('</g></svg>')
    return ''.join(s)


def attr_tree(levels, label='Classification tree of attributes', w=360):
    """Classification tree: levels = list of rows; row r has 2**r labels (e.g. [['n'], ['(A)','(α)'], ...]).
    The last row may instead have the same count as the previous row (one vertical line per node, as in printed two-way trees)."""
    dy = 62
    h = 30 + dy * (len(levels) - 1) + 20
    s = [svg_open(w, h, label), f'<rect width="{w}" height="{h}" fill="#dbeafe"/>',
         '<g font-family="Times New Roman,serif" font-size="17" fill="#111" text-anchor="middle">']
    pos = []
    for r, row in enumerate(levels):
        y = 24 + dy * r
        xs = [w * (i + .5) / len(row) for i in range(len(row))]
        pos.append((xs, y))
        for x, t in zip(xs, row):
            bold = ' font-weight="bold" font-size="20"' if r == 0 else ''
            s.append(f'<text x="{x:.1f}" y="{y}"{bold}>{E(t)}</text>')
        if r:
            pxs, py = pos[r - 1]
            ratio = len(row) // len(pxs)
            for i, x in enumerate(xs):
                px = pxs[i // ratio]
                s.append(f'<path d="M{px:.1f} {py + 8}L{x:.1f} {y - 18}" stroke="#111" stroke-width="1.4"/>')
    s.append('</g></svg>')
    return ''.join(s)


def order_tree(lang='en', label='Tree of classes of order 0 to 3 for attributes A, B, C'):
    """Printed p270 tree: left labels 'Class of order k →' and a binary tree n → order-1 → order-2 → order-3 classes."""
    word = {'en': 'Class of order', 'ur': 'درجے کی جماعت', 'ps': 'د درجې ټولګی'}[lang]
    levels = [['n'], ['(A)', '(α)'], ['(AB)', '(Aβ)', '(αB)', '(αβ)'],
              ['(ABC)', '(ABγ)', '(AβC)', '(Aβγ)', '(αBC)', '(αBγ)', '(αβC)', '(αβγ)']]
    w, h, x0, dy = 640, 280, 170, 72
    s = [svg_open(w, h, label), f'<rect width="{w}" height="{h}" fill="#dbeafe"/>',
         '<g font-family="Times New Roman,serif" font-size="15" fill="#111" text-anchor="middle">']
    tw = w - x0 - 10
    pos = []
    for r, row in enumerate(levels):
        y = 26 + dy * r
        lab = f'{word} {r}' if lang == 'en' else f'{r} {word}'
        s.append(f'<text x="8" y="{y}" text-anchor="start">{E(lab)}</text>'
                 f'<path d="M128 {y - 5}H150" stroke="#111"/><path d="M146 {y - 9}L154 {y - 5}L146 {y - 1}Z" fill="#111"/>')
        xs = [x0 + tw * (i + .5) / len(row) for i in range(len(row))]
        for x, t in zip(xs, row):
            s.append(f'<text x="{x:.1f}" y="{y}">{E(t)}</text>')
        if pos:
            pxs, py = pos[-1]
            for i, x in enumerate(xs):
                s.append(f'<path d="M{pxs[i // 2]:.1f} {py + 8}L{x:.1f} {y - 17}" stroke="#111" stroke-width="1.3"/>')
        pos.append((xs, y))
    s.append('</g></svg>')
    return ''.join(s)


def chi_tail(crit, df=4, alpha='α=0.05', label='Chi-square curve with right-tail rejection region', xmax=None):
    """Right-skewed χ² density (df) on a light panel; area beyond crit shaded, labelled alpha; axis marks 0, crit and ∞."""
    w, h, base, top, x0, x1 = 320, 150, 118, 16, 22, 300
    k = df / 2
    xmax = xmax or max(crit * 1.9, df + 4 * (2 * df) ** .5)
    f = lambda x: x ** (k - 1) * _m.exp(-x / 2) if x > 0 else (1.0 if k == 1 else 0.0)
    xs = [xmax * i / 160 for i in range(1, 161)]
    fm = max(f(x) for x in xs)
    X = lambda x: x0 + (x1 - x0) * x / xmax
    Y = lambda x: base - (base - top) * min(f(x) / fm, 1.15)
    s = [svg_open(w, h, label), f'<rect width="{w}" height="{h}" fill="#dbeafe"/>']
    tail = [x for x in xs if x >= crit]
    s.append(f'<path d="M{X(crit):.1f} {base}L{X(crit):.1f} {Y(crit):.1f}' + ''.join(f'L{X(x):.1f} {Y(x):.1f}' for x in tail) + f'L{X(xmax):.1f} {base}Z" fill="#fff"/>')
    s.append('<path d="M' + 'L'.join(f'{X(x):.1f} {Y(x):.1f}' for x in xs) + '" fill="none" stroke="#111" stroke-width="1.8"/>')
    s.append(f'<path d="M{x0} {top - 6}V{base}H{x1 + 8}M{X(crit):.1f} {base}V{Y(crit):.1f}" stroke="#111" fill="none"/>')
    s.append(f'<g font-family="Times New Roman,serif" font-size="14" fill="#111" text-anchor="middle">'
             f'<text x="{x0}" y="{base + 18}">0</text><text x="{X(crit):.1f}" y="{base + 18}">{E(str(crit))}</text>'
             f'<text x="{x1 + 4}" y="{base - 4}">∞</text><text x="{X(crit) + 34:.1f}" y="{Y(crit) - 10:.1f}">{E(alpha)}</text></g></svg>')
    return ''.join(s)
