"""Shared Class 12 Health & Physical Education (صحت و جسمانی تعلیم, KPTBB 2019-20) helpers: Urdu-original book; records carry (en, ur, ps).
Single-page scans: PDF n = printed page n - 5 (PDF6 = p.1)."""
from class12_book_common import Book, Builder  # noqa: F401

BOOK = Book('hpe')

UNITS = {
    1: ('Non-Communicable Diseases', 'غیر متعدی امراض', 'غیر ساري ناروغۍ'),
    2: ('Circulatory System and the Effects of Exercise', 'نظامِ دورانِ خون اور ورزش کے اثرات', 'د وینې د جریان سیستم او د تمرین اغېزې'),
    3: ('Doping', 'ڈوپنگ', 'ډوپینګ'),
    4: ('Emergency Situations', 'ہنگامی صورتِ حال', 'بیړني حالات'),
    5: ('Verbal and Physical Violence', 'زبانی و جسمانی تشدد', 'ژبنی او فزیکي تاوتریخوالی'),
    6: ('Sports and Biomechanical Principles', 'کھیل اور بائیو مکینیکل اصول', 'لوبې او بایومیخانیکي اصول'),
    7: ('Rules and Skills of Games', 'کھیلوں کے قوانین اور مہارتیں', 'د لوبو قوانین او مهارتونه'),
}


def pg(pdf):
    # printed p.107 is missing from the scan: PDF111 = p.106, PDF112 = p.108
    # printed p.148 is missing too: PDF151 = p.147, PDF152 = p.149
    return pdf - 5 if pdf <= 111 else (pdf - 4 if pdf <= 151 else pdf - 3)


def rec(b, unit, n, pdf, note=None, first=False, pages=None):
    r = BOOK.record(b, f'hpe12-ch{unit}-text-{n}', f'Chapter {unit} text ({n})', f'باب {unit} — متن ({n})', f'{unit} څپرکی — متن ({n})', pdf,
                    pages or [pg(pdf)], unit_title=UNITS[unit] if first else None)
    if note:
        r['sourceNote'] = note
    return r


def P(b, items):
    for x in items:
        b.p(*x)


def L(b, items):
    b.group('list', items)


def deco(r, text):
    r['sourceDecorativeImages'] = text
    return r


T = lambda x, y, s, sz=14, w='normal', a='middle', c='#1e293b': f'<text x="{x}" y="{y}" text-anchor="{a}" font-size="{sz}" font-weight="{w}" fill="{c}" font-family="sans-serif">{s}</text>'


def svg(W, H, body, cap):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{cap}"><rect width="{W}" height="{H}" fill="#ffffff"/>{body}{T(W / 2, H - 8, cap, 12)}</svg>', W / H


def lung_pair(x, y, fill, s=1.0):
    """Two lung lobes + trachea centred at x, top y."""
    return (f'<path d="M{x} {y} v{40*s}" stroke="#b45309" stroke-width="{6*s}"/>'
            f'<path d="M{x} {y+40*s} q{-20*s} {10*s} {-30*s} {25*s} M{x} {y+40*s} q{20*s} {10*s} {30*s} {25*s}" stroke="#b45309" stroke-width="{4*s}" fill="none"/>'
            f'<path d="M{x-12*s} {y+45*s} C{x-70*s} {y+40*s} {x-85*s} {y+150*s} {x-60*s} {y+175*s} C{x-40*s} {y+185*s} {x-12*s} {y+170*s} {x-12*s} {y+150*s} Z" fill="{fill}" stroke="#7f1d1d" stroke-width="2"/>'
            f'<path d="M{x+12*s} {y+45*s} C{x+70*s} {y+40*s} {x+85*s} {y+150*s} {x+60*s} {y+175*s} C{x+40*s} {y+185*s} {x+12*s} {y+170*s} {x+12*s} {y+150*s} Z" fill="{fill}" stroke="#7f1d1d" stroke-width="2"/>')


def fig_lung_tumour(lab):
    """lab = (Lung, Tumour, caption)"""
    b = lung_pair(150, 20, '#f9a8a8')
    b += '<circle cx="185" cy="120" r="18" fill="#f59e0b" stroke="#92400e" stroke-width="2"/><circle cx="110" cy="150" r="12" fill="#f59e0b" stroke="#92400e" stroke-width="2"/>'
    b += '<circle cx="340" cy="120" r="70" fill="#fee2e2" stroke="#1e293b" stroke-width="2"/><circle cx="340" cy="120" r="35" fill="#f59e0b" stroke="#92400e" stroke-width="2"/>'
    b += '<line x1="203" y1="120" x2="270" y2="120" stroke="#1e293b" stroke-width="2"/>'
    b += f'<line x1="200" y1="70" x2="250" y2="40" stroke="#1e293b"/>{T(255, 36, lab[0], 14, "bold", "start")}'
    b += f'<line x1="340" y1="155" x2="340" y2="205" stroke="#1e293b"/>{T(340, 220, lab[1], 14, "bold")}'
    return svg(440, 250, b, lab[2])


def fig_smoker(lab):
    """lab = (non-smoker, smoker, caption)"""
    b = lung_pair(110, 20, '#f9a8a8') + lung_pair(330, 20, '#3f3f46')
    b += T(110, 225, lab[0], 14, 'bold') + T(330, 225, lab[1], 14, 'bold')
    return svg(440, 255, b, lab[2])


def fig_heart(lab, cap):
    """Schematic heart section. lab: dict of label keys -> text (English labels as printed)."""
    b = ('<path d="M120 90 C80 90 70 150 90 210 C110 270 170 320 210 340 C250 320 310 270 330 210 C350 150 340 90 300 90 Z" fill="#fecdd3" stroke="#9f1239" stroke-width="2"/>'
         '<line x1="210" y1="95" x2="210" y2="335" stroke="#9f1239" stroke-width="3"/><line x1="95" y1="185" x2="325" y2="185" stroke="#9f1239" stroke-width="2"/>'
         '<rect x="165" y="20" width="22" height="75" fill="#2563eb"/><rect x="230" y="30" width="26" height="65" fill="#dc2626"/><path d="M243 30 q40 -25 80 0" stroke="#dc2626" stroke-width="14" fill="none"/>'
         '<rect x="200" y="55" width="80" height="14" fill="#7c3aed"/><rect x="300" y="110" width="60" height="12" fill="#f97316"/><rect x="60" y="110" width="60" height="12" fill="#f97316"/>'
         '<rect x="165" y="335" width="22" height="45" fill="#2563eb"/>')
    pos = {'svc': (176, 14), 'aorta': (243, 24), 'pa': (300, 60), 'pv': (370, 120), 'ra': (150, 150), 'la': (270, 150), 'rv': (150, 250), 'lv': (270, 250),
           'tri': (60, 205), 'mitral': (370, 190), 'pulv': (60, 250), 'aov': (370, 230), 'ivc': (176, 398)}
    for k, (x, y) in pos.items():
        if k in lab:
            a = 'start' if x > 300 else ('end' if x < 100 else 'middle')
            b += T(x, y, lab[k], 12, 'bold', a)
    return svg(440, 430, b, cap)


def fig_circulation(lab, cap):
    """Schematic body outline with heart, aorta and main vessels; lab keys: subclavian, arch, pv, pa, ivc, thoracic, abdominal."""
    b = ('<path d="M150 40 h100 l60 60 v120 h-40 v190 h-140 v-190 h-40 v-120 Z" fill="#fde68a" stroke="#92400e" stroke-width="1.5"/>'
         '<line x1="200" y1="60" x2="200" y2="400" stroke="#dc2626" stroke-width="7"/><line x1="185" y1="60" x2="185" y2="400" stroke="#1d4ed8" stroke-width="6"/>'
         '<path d="M200 80 q-60 0 -100 30 M200 80 q60 0 100 30" stroke="#1d4ed8" stroke-width="4" fill="none"/>'
         '<ellipse cx="200" cy="130" rx="24" ry="30" fill="#ef4444" stroke="#7f1d1d"/><path d="M200 105 q30 -30 60 0" stroke="#dc2626" stroke-width="6" fill="none"/>'
         '<ellipse cx="165" cy="300" rx="12" ry="20" fill="#f87171"/><ellipse cx="235" cy="300" rx="12" ry="20" fill="#f87171"/>')
    pos = {'subclavian': (95, 75, 'end'), 'arch': (270, 80, 'start'), 'pv': (270, 135, 'start'), 'pa': (95, 160, 'end'), 'ivc': (95, 270, 'end'),
           'thoracic': (270, 230, 'start'), 'abdominal': (270, 330, 'start')}
    for k, (x, y, a) in pos.items():
        if k in lab:
            b += f'<line x1="{x + (8 if a == "start" else -8) * -1}" y1="{y - 4}" x2="200" y2="{y - 4}" stroke="#1e293b" stroke-width="1"/>' + T(x, y, lab[k], 12, 'bold', a)
    return svg(400, 440, b, cap)


def labelled(W, H, shapes, labels, cap):
    """Generic schematic: shapes = raw svg string; labels = [(text, tx, ty, anchor, px, py)] with a leader line from label to point (px, py) (None = no line)."""
    b = shapes
    for text, tx, ty, a, px, py in labels:
        if px is not None:
            sx = tx + (4 if a == 'start' else (-4 if a == 'end' else 0))
            b += f'<line x1="{sx}" y1="{ty - 4}" x2="{px}" y2="{py}" stroke="#1e293b" stroke-width="1"/>'
        b += T(tx, ty, text, 12, 'bold', a)
    return svg(W, H, b, cap)


def vessel_bed(x0, y, w, h=60):
    """Artery (red, right) → capillary mesh → vein (blue, left), horizontal."""
    s = f'<path d="M{x0 + w} {y} q-60 0 -{w * .3} {h / 3}" stroke="#dc2626" stroke-width="16" fill="none"/>'
    s += f'<path d="M{x0} {y} q60 0 {w * .3} {h / 3}" stroke="#1d4ed8" stroke-width="16" fill="none"/>'
    for i in range(6):
        yy = y + 8 + i * h / 7
        s += f'<path d="M{x0 + w * .3} {y + h / 3} C{x0 + w * .45} {yy} {x0 + w * .55} {yy + 10} {x0 + w * .7} {y + h / 3}" stroke="{["#1d4ed8", "#7c3aed", "#dc2626"][i % 3]}" stroke-width="2" fill="none"/>'
    return s


def fig_longjump_runway(cap, lab):
    """lab: dict pit_len, pit_w, gap, board, board_w, board_t, board_len, run_len, run_w (texts)."""
    b = ('<rect x="120" y="20" width="200" height="200" fill="#fef3c7" stroke="#dc2626" stroke-width="2"/>'
         '<rect x="150" y="250" width="120" height="22" fill="#e5e7eb" stroke="#dc2626" stroke-width="2"/>'
         '<rect x="150" y="272" width="120" height="250" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
         '<line x1="150" y1="25" x2="150" y2="215" stroke="#dc2626" stroke-dasharray="3 3"/><line x1="210" y1="220" x2="210" y2="250" stroke="#dc2626" stroke-dasharray="3 3"/>'
         '<line x1="210" y1="280" x2="210" y2="515" stroke="#dc2626" stroke-dasharray="3 3"/><line x1="155" y1="510" x2="265" y2="510" stroke="#dc2626" stroke-dasharray="3 3"/>')
    b += T(115, 120, lab['pit_len'], 12, 'bold', 'end') + T(115, 230, lab['pit_w'], 12, 'bold', 'end') + T(225, 240, lab['gap'], 12, 'bold', 'start')
    b += T(280, 258, lab['board'], 12, 'bold', 'start') + T(280, 278, lab['board_len'], 12, 'bold', 'start')
    b += T(140, 258, lab['board_w'], 12, 'bold', 'end') + T(140, 278, lab['board_t'], 12, 'bold', 'end')
    b += T(215, 400, lab['run_len'], 12, 'bold', 'start') + T(210, 500, lab['run_w'], 12, 'bold', 'middle')
    return svg(440, 545, b, cap)
