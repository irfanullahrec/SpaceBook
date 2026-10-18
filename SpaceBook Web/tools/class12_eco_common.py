"""Shared Class 12 Economics (کتابِ معاشیات حصہ دوم, Ilmi Kitab Khana 2019-20, Urdu source) helpers.
Landscape spreads (right page read first). PDF9 = p.xiv (R) + p.1 (L); from PDF10: right = 2n-18, left = 2n-17."""
from class12_book_common import Book, Builder  # noqa: F401
from class12_hpe_common import svg, T, labelled  # noqa: F401

BOOK = Book('eco')

UNITS = {
    1: ('National Income', 'قومی آمدنی', 'ملي عاید'),
    2: ('Money', 'زر', 'پیسې (زر)'),
    3: ('Bank', 'بنک', 'بانک'),
    4: ('Public Finance', 'سرکاری مالیات', 'دولتي مالیه'),
    5: ('International Trade', 'بین الاقوامی تجارت', 'نړیواله سوداګري'),
    6: ('Introduction to the Economy of Pakistan', 'معیشتِ پاکستان کا تعارف', 'د پاکستان د اقتصاد پېژندنه'),
    7: ('National Income of Pakistan', 'پاکستان کی قومی آمدنی', 'د پاکستان ملي عاید'),
    8: ('Economic Development and Planning', 'معاشی ترقی اور منصوبہ بندی', 'اقتصادي پرمختګ او پلان جوړونه'),
    9: ('Communications, Means of Transport and Development of Human Resources', 'مواصلات، ذرائع نقل و حمل اور انسانی ذرائع کی ترقی', 'مخابرات، د ترانسپورت وسایل او د بشري سرچینو پرمختګ'),
    10: ('Banking System of Pakistan', 'پاکستان کا بنکاری نظام', 'د پاکستان بانکي نظام'),
    11: ('Public Finance of the Government of Pakistan', 'حکومتِ پاکستان کے مالیات', 'د پاکستان د حکومت مالیه'),
    12: ('Foreign Trade of Pakistan', 'پاکستان کی بیرونی تجارت', 'د پاکستان بهرنۍ سوداګري'),
    13: ('Economic System of Islam', 'اسلام کا معاشی نظام', 'د اسلام اقتصادي نظام'),
}


def pages(pdf):
    if pdf == 9:
        return ['xiv', 1]
    if pdf >= 28:  # PDF27 is a duplicate scan of pp.34-35 (PDF26)
        return [2 * pdf - 20, 2 * pdf - 19]
    return [2 * pdf - 18, 2 * pdf - 17]


def rec(b, unit, n, pdf, pages_=None, note=None, first=False):
    r = BOOK.record(b, f'eco12-ch{unit}-text-{n}', f'Chapter {unit} text ({n})', f'باب {unit} — متن ({n})', f'{unit} څپرکی — متن ({n})', pdf,
                    pages_ or pages(pdf), unit_title=UNITS[unit] if first else None)
    if note:
        r['sourceNote'] = note
    return r


def P(b, items):
    for x in items:
        b.p(*x)


def L(b, items):
    b.group('list', items)


def fig_circular(lab, cap):
    """Circular flow: households (top), firms (bottom); outer dashed oval; inner arrows. lab keys: hh, firms, goods, value, services, factor_pay, price."""
    b = ('<ellipse cx="300" cy="150" rx="250" ry="110" fill="none" stroke="#1e293b" stroke-width="2" stroke-dasharray="8 5"/>'
         '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1e293b"/></marker></defs>'
         '<path d="M240 200 Q200 160 240 100" fill="none" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar)"/>'
         '<path d="M360 100 Q400 140 360 200" fill="none" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar)"/>')
    b += f'<rect x="230" y="28" width="140" height="28" rx="6" fill="#fff" stroke="#1e3a8a"/>' + T(300, 47, lab['hh'], 13, 'bold')
    b += f'<rect x="230" y="245" width="140" height="28" rx="6" fill="#fff" stroke="#1e3a8a"/>' + T(300, 264, lab['firms'], 13, 'bold')
    b += T(470, 30, lab['goods'], 12, 'bold') + T(570, 155, lab['value'], 12, 'bold', 'end') + T(30, 155, lab['services'], 12, 'bold', 'start')
    b += T(250, 150, lab['factor_pay'], 11, 'normal') + T(350, 150, lab['price'], 11, 'normal')
    b += T(150, 70, '1', 13, 'bold') + T(215, 120, '2', 13, 'bold') + T(450, 70, '3', 13, 'bold') + T(385, 120, '4', 13, 'bold')
    return svg(600, 300, b, cap)


def fig_si(lab, cap):
    """Saving-investment equilibrium: axes O-X (income), O-Y (saving & investment); S-S rising line; I-I horizontal; points E,H,K,L,M,N,P."""
    o = (60, 260)
    b = ('<defs><marker id="ax" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1e293b"/></marker></defs>'
         f'<line x1="{o[0]}" y1="{o[1]}" x2="460" y2="{o[1]}" stroke="#1e293b" stroke-width="2" marker-end="url(#ax)"/>'
         f'<line x1="{o[0]}" y1="{o[1]}" x2="{o[0]}" y2="20" stroke="#1e293b" stroke-width="2" marker-end="url(#ax)"/>'
         '<line x1="110" y1="290" x2="400" y2="30" stroke="#b91c1c" stroke-width="2.5"/>'
         '<line x1="60" y1="150" x2="440" y2="150" stroke="#1d4ed8" stroke-width="2.5"/>'
         '<line x1="233" y1="150" x2="233" y2="260" stroke="#1e293b" stroke-width="1.5"/>'
         '<line x1="190" y1="150" x2="190" y2="260" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="5 4"/>'
         '<line x1="300" y1="90" x2="300" y2="260" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="5 4"/>')
    for t, x, y in [('O', 45, 268), ('X', 470, 265), ('Y', 55, 15), ('S', 405, 28), ('S', 100, 300), ('I', 45, 155), ('I', 450, 155), ('E', 240, 142), ('P', 180, 142),
                    ('M', 308, 142), ('L', 308, 86), ('N', 186, 280), ('H', 233, 280), ('K', 300, 280)]:
        b += T(x, y, t, 14, 'bold')
    b += T(260, 20, lab[0], 12, 'bold') + f'<text x="25" y="150" font-size="12" font-weight="bold" fill="#1e293b" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 25 150)">{lab[1]}</text>'
    return svg(500, 320, b, cap)


def eqx(b, latex):
    """Formula line (same in all languages); formulas carrying printed English words are marked untranslatedByDesign."""
    b.eq(latex)
    if 'text{' in latex:
        b.paras[-1]['untranslatedByDesign'] = True


def qa(b, rows):
    """Model-paper short Q&A rows: (q_en, q_ur, q_ps, a_en, a_ur, a_ps)."""
    for qe, qu, qp, ae, au, ap in rows:
        b.p(qe, qu, qp)
        b.p(ae, au, ap)


def mcqs(b, items, start=1, per_line=2):
    """MCQ items: (question_triple, [option_triples], tick_index or None); a printed ✓ is appended to the ticked option."""
    for i, (q, o, k) in enumerate(items, start):
        if k is not None:
            o = [tuple(x + ' ✓' for x in v) if j == k else v for j, v in enumerate(o)]
        b.mcq(f'{i}.', q, o, per_line=per_line)


def model(b, unit, n, pdf, page):
    """Record for chapter model-paper questions."""
    ps_digits = str(n).translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹'))
    return BOOK.record(b, f'eco12-ch{unit}-model-{n}', f'Chapter {unit} model paper questions ({n})', f'باب {unit}: ماڈل پرچہ سوالات ({ps_digits})',
                       f'{unit} څپرکی: د نمونې پرچې پوښتنې ({ps_digits})', pdf, [page])
