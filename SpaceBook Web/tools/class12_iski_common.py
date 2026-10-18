"""Shared Class 12 Islamiat (Ikhtiari) helpers (KPTBB 2020-21, Urdu source).
Landscape spreads, right page read first. PDF1 cover, PDF2 publisher ad (excluded), PDF3-4 credits/preface/contents,
PDF5 = contents (R) + p.1 (L); from PDF6: right = 2n-10, left = 2n-9."""
from class12_book_common import Book, Builder  # noqa: F401

BOOK = Book('iski')

UNITS = {
    'FM': ('Front matter', 'ابتدائیہ', 'لومړنۍ برخه'),
    1: ('The Holy Quran', 'قرآنِ مجید اور اصولِ تفسیر', 'قرآن مجید او د تفسیر اصول'),
    2: ('Hadith', 'حدیثِ نبوی ﷺ اور اصولِ حدیث', 'نبوي حدیث ﷺ او د حدیث اصول'),
    3: ('Services of Muslims in academic progress', 'علمی پیش رفت میں مسلمانوں کی خدمات', 'په علمي پرمختګ کې د مسلمانانو خدمتونه'),
    4: ('The Islamic system of government and state', 'اسلام کا نظامِ حکومت و ریاست', 'د اسلام د حکومت او دولت نظام'),
    5: ('The present age and Islamic states', 'عصرِ حاضر اور اسلامی ریاستیں', 'اوسنی عصر او اسلامي دولتونه'),
    6: ('Arabic language and literature', 'عربی زبان و ادب', 'عربي ژبه او ادب'),
    'BM': ('Back matter', 'اختتامیہ', 'وروستۍ برخه'),
}


def pages(pdf):
    if pdf == 5:
        return [None, 1]
    return [2 * pdf - 10, 2 * pdf - 9]


def rec(b, unit, n, pdf, pages_=None, first=False, kind='text'):
    u = UNITS[unit]
    if unit in ('FM', 'BM'):
        uid, lab_en, lab_ur, lab_ps = unit.lower(), u[0], u[1], u[2]
    else:
        uid, lab_en, lab_ur, lab_ps = f'ch{unit}', f'Chapter {unit}', f'باب {unit}', f'{unit} څپرکی'
    return BOOK.record(b, f'iski12-{uid}-{kind}-{n}', f'{lab_en} — {kind} ({n})', f'{lab_ur} — متن ({n})', f'{lab_ps} — متن ({n})', pdf,
                       pages_ or pages(pdf), unit_title=u if first else None)


def P(b, items):
    for x in items:
        b.p(*x)


def L(b, items):
    b.group('list', items)


def AR(b, arabic, ref=''):
    """Arabic Quran/Hadith text, reproduced as printed (same in all languages)."""
    t = arabic + (f' ({ref})' if ref else '')
    b.add('paragraph', t, t, t)
    b.paras[-1]['arabicSource'] = True


def qa(b, rows):
    for qe, qu, qp, ae, au, ap in rows:
        b.p(qe, qu, qp)
        b.p(ae, au, ap)


def mcqs(b, items, start=1, per_line=2):
    for i, (q, o, k) in enumerate(items, start):
        if k is not None:
            o = [tuple(x + ' ✓' for x in v) if j == k else v for j, v in enumerate(o)]
        b.mcq(f'{i}.', q, o, per_line=per_line)


def O(e, u=None, p=None):
    return (e, u or e, p or e)


def S(b, rows):
    """Headed paragraphs: rows of ((h_en, h_ur, h_ps), (p_en, p_ur, p_ps) | [paras])."""
    for h, p in rows:
        b.h(*h)
        P(b, p if isinstance(p, list) else [p])


def V(b, label, arabic, ref, tr, expl=None):
    """Verse block: optional label line (en,ur,ps), Arabic text, translation (en,ur,ps), optional explanation paragraphs."""
    if label:
        b.p(*label)
    AR(b, arabic, ref)
    b.p('Translation: ' + tr[0], 'ترجمہ: ' + tr[1], 'ژباړه: ' + tr[2])
    if expl:
        b.h('Explanation', 'تشریح', 'تشریح')
        P(b, expl)
