"""Shared Class 12 Islamic History (Tarikh-e-Islam, Banu Abbas part 2; KPTBB 2022-23, Urdu source).
PDF1 cover (portrait), PDF2 publisher ad (excluded), PDF3 title page = p.1 (portrait), PDF4 = pp.2–3, PDF5 = pp.4–5 (contents);
landscape spreads from PDF4: right = 2n-6, left = 2n-5. Lessons 1–42 are units (book's own numbering)."""
from class12_book_common import Book, Builder  # noqa: F401

BOOK = Book('ihist')

# (number, start page, english, urdu, pashto)
LESSONS = [
    (1, 6, 'Beginning of the Abbasid caliphate', 'آغاز خلافت بنوعباس', 'د بنو عباس د خلافت پیل'),
    (2, 11, 'Abu al-Abbas Abdullah al-Saffah', 'ابوالعباس عبداللہ سفاح', 'ابوالعباس عبدالله سفاح'),
    (3, 13, 'Abu Ja\'far al-Mansur', 'ابوجعفر منصور', 'ابوجعفر منصور'),
    (4, 23, 'Abu Abdullah Muhammad al-Mahdi', 'ابوعبداللہ محمد مہدی', 'ابوعبدالله محمد مهدي'),
    (5, 27, 'Harun al-Rashid', 'ہارون الرشید', 'هارون الرشید'),
    (6, 40, 'Muhammad al-Amin al-Rashid', 'محمد امین الرشید', 'محمد امین الرشید'),
    (7, 42, 'Ma\'mun al-Rashid', 'مامون الرشید', 'مامون الرشید'),
    (8, 53, 'Abu Ishaq Muhammad bin Harun al-Mu\'tasim billah', 'ابواسحاق محمد بن ہارون معتصم باللہ', 'ابواسحاق محمد بن هارون معتصم بالله'),
    (9, 55, 'Abu Ja\'far Harun al-Wathiq billah', 'ابوجعفر ہارون واثق باللہ', 'ابوجعفر هارون واثق بالله'),
    (10, 56, 'Ja\'far bin Mu\'tasim al-Mutawakkil billah', 'جعفر معتصم بن متوکل باللہ', 'جعفر بن معتصم متوکل بالله'),
    (11, 60, 'Muhammad bin Ja\'far al-Muntasir billah', 'محمد بن جعفر منتصر باللہ', 'محمد بن جعفر منتصر بالله'),
    (12, 61, 'Abu Abdullah Muhammad bin Ja\'far al-Mu\'tazz billah', 'ابوعبداللہ محمد بن جعفر معتز باللہ', 'ابوعبدالله محمد بن جعفر معتز بالله'),
    (13, 62, 'Abu al-Abbas Ahmad bin Mutawakkil al-Mu\'tamid \'ala Allah', 'ابوالعباس احمد بن متوکل معتمد علی اللہ', 'ابوالعباس احمد بن متوکل معتمد علی الله'),
    (14, 65, 'Abu al-Abbas Ahmad bin Muwaffaq al-Mu\'tadid billah', 'ابوالعباس احمد بن موفق معتضد باللہ', 'ابوالعباس احمد بن موفق معتضد بالله'),
    (15, 66, 'Abu Muhammad Ali bin Mu\'tadid al-Muktafi billah', 'ابومحمد علی بن معتضد مکتفی باللہ', 'ابومحمد علي بن معتضد مکتفي بالله'),
    (16, 67, 'Abu al-Fadl Ja\'far bin Mu\'tadid al-Muqtadir billah', 'ابوالفضل جعفر بن معتضد مقتدر باللہ', 'ابوالفضل جعفر بن معتضد مقتدر بالله'),
    (17, 73, 'Abu al-Qasim Fadl bin Muqtadir al-Muti\' lillah', 'ابوالقاسم فضل بن مقتدر مطیع اللہ', 'ابوالقاسم فضل بن مقتدر مطیع لله'),
    (18, 74, 'Abu al-Fadl Abd al-Karim bin Muti\' al-Ta\'i\' lillah', 'ابوالفضل عبدالکریم بن مطیع طائع اللہ', 'ابوالفضل عبدالکریم بن مطیع طائع لله'),
    (19, 75, 'Abu al-Abbas Ahmad bin Muqtadir al-Qadir billah', 'ابوالعباس احمد بن مقتدر قادر باللہ', 'ابوالعباس احمد بن مقتدر قادر بالله'),
    (20, 76, 'Abu Ja\'far Abdullah bin Qadir al-Qa\'im bi-amr Allah', 'ابوجعفر عبداللہ بن قادر قائم بامراللہ', 'ابوجعفر عبدالله بن قادر قائم بامرالله'),
    (21, 81, 'Abu Mansur Fadl bin Mustazhir al-Mustarshid billah', 'ابومنصور فضل بن مستظہر مسترشد باللہ', 'ابومنصور فضل بن مستظهر مسترشد بالله'),
    (22, 83, 'Abu al-Abbas Ahmad bin Mustadi\' al-Nasir li-Din Allah', 'ابوالعباس احمد بن مستضی ناصرالدین اللہ', 'ابوالعباس احمد بن مستضيء ناصر لدین الله'),
    (23, 88, 'Abu Ja\'far Mansur al-Mustansir billah; Abu Ahmad Abdullah bin Mustansir al-Musta\'sim billah', 'ابوجعفر منصور مستنصر باللہ۔ ابواحمد عبداللہ بن مستنصر معتصم باللہ', 'ابوجعفر منصور مستنصر بالله؛ ابواحمد عبدالله بن مستنصر مستعصم بالله'),
    (24, 92, 'The Mu\'tazilah, the Qaramitah, the Buyid or Daylami dynasty, the Seljuqs, the Crusades', 'فرقہ معتزلہ، فرقہ قرامطہ، خاندان بویہ یا دیلمی، سلجوقی، صلیبی جنگیں', 'معتزله، قرامطه، د بویه یا دیلمي کورنۍ، سلجوقیان، صلیبي جګړې'),
    (25, 109, 'The last caliphs; decline of the Abbasid dynasty', 'آخری خلفاء۔ خاندانِ عباسیہ کا زوال', 'وروستي خلفاء؛ د عباسي کورنۍ زوال'),
    (26, 126, 'Scholars of the Abbasid era', 'علمائے عباسیہ', 'د عباسي دورې علماء'),
    (27, 132, 'Amirs of Andalus', 'امیرانِ اندلس', 'د اندلس امیران'),
    (28, 134, 'Muslims in Andalus', 'مسلمان اندلس میں', 'مسلمانان په اندلس کې'),
    (29, 143, 'Amir Abd al-Aziz bin Musa (era of the amirate)', 'امیر عبدالعزیز بن موسیٰ (دورِ امارت)', 'امیر عبدالعزیز بن موسی (د امارت دوره)'),
    (30, 145, 'Amir Samh bin Malik Khawlani', 'امیر سمح بن مالک خولانی', 'امیر سمح بن مالک خولاني'),
    (31, 151, 'Amir Abd al-Rahman al-Dakhil', 'امیر عبدالرحمان الداخل', 'امیر عبدالرحمان الداخل'),
    (32, 158, 'Hisham bin Abd al-Rahman', 'ہشام بن عبدالرحمان', 'هشام بن عبدالرحمان'),
    (33, 160, 'Amir Abd al-Rahman II al-Awsat', 'امیر عبدالرحمان ثانی الاوسط', 'امیر عبدالرحمان دویم الاوسط'),
    (34, 166, 'Abd al-Rahman III al-Nasir — the golden era of the Umayyads', 'عبدالرحمان ناصر ثالث۔ بنوامیہ کا سنہرا دور', 'عبدالرحمان ناصر درېیم — د بنو امیه طلايي دوره'),
    (35, 175, 'Hisham II al-Mu\'ayyad billah', 'ہشام ثانی المؤید باللہ', 'هشام دویم المؤید بالله'),
    (36, 178, 'Other rulers of Andalus besides the Umayyads', 'بنوامیہ کے علاوہ اندلس کے دیگر حکمران', 'له بنو امیه پرته د اندلس نور واکمنان'),
    (37, 184, 'The Nasrid dynasty of Granada', 'نصری خاندان غرناطہ', 'د غرناطې نصري کورنۍ'),
    (38, 189, 'Causes of the decline of the Islamic sultanate of Andalus', 'اسلامی سلطنت اندلس کے زوال کے اسباب', 'د اندلس د اسلامي سلطنت د زوال لاملونه'),
    (39, 202, 'Scholars of Andalus', 'علمائے اندلس', 'د اندلس علماء'),
    (40, 211, 'Buildings of Andalus', 'عماراتِ اندلسیہ', 'د اندلس ودانۍ'),
    (41, 216, 'Islamic Spain on the highway of progress', 'اسلامی سپین۔ شاہراہ ترقی پر', 'اسلامي هسپانیه — د پرمختګ پر لویه لاره'),
    (42, 223, 'Bibliography', 'کتابیات', 'کتابیات'),
]
UNITS = {'FM': ('Front matter', 'ابتدائیہ', 'لومړنۍ برخه')}
for n, _, e, u, p in LESSONS:
    UNITS[n] = (e, u, p)


def pages(pdf):
    # PDF9–10 duplicate PDF7–8; PDF94/95 both show pp.180–181 (one duplicate)
    if pdf <= 8:
        r = 2 * pdf - 6
    elif pdf <= 22:
        r = 2 * pdf - 10
    elif pdf <= 95:
        r = 2 * pdf - 8
    else:
        r = 2 * pdf - 10
    return [r, r + 1]


def rec(b, unit, n, pdf, pages_=None, first=False, kind='text'):
    u = UNITS[unit]
    if unit == 'FM':
        uid, le, lu, lp = 'fm', u[0], u[1], u[2]
    else:
        uid, le, lu, lp = f'l{unit}', f'Lesson {unit}', f'سبق {unit}', f'{unit} لوست'
    return BOOK.record(b, f'ihist12-{uid}-{kind}-{n}', f'{le} — {kind} ({n})', f'{lu} — متن ({n})', f'{lp} — متن ({n})', pdf,
                       pages_ or pages(pdf), unit_title=u if first else None)


def P(b, items):
    for x in items:
        b.p(*x)


def L(b, items):
    b.group('list', items)


def AR(b, arabic, ref=''):
    t = arabic + (f' ({ref})' if ref else '')
    b.add('paragraph', t, t, t)
    b.paras[-1]['arabicSource'] = True


def H(b, e, u, p):
    b.h(e, u, p)


def S(b, rows):
    """rows of (heading (en,ur,ps) or None, paragraph (en,ur,ps))."""
    for h, p in rows:
        if h:
            b.h(*h)
        if p:
            b.p(*p)
