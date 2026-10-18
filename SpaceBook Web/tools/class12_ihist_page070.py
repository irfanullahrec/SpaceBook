"""Islamic History XII PDF70: p.132 — exercise of lesson 26 (end); Lesson 27 Amirs of Andalus table (start); p.133 — table (end). Run: python class12_ihist_page070.py"""
from class12_ihist_common import BOOK, Builder, rec, L

TF = (' (true/false)', ' (درست/غلط)', ' (سم/ناسم)')
D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')


def tf(items):
    return [(e + TF[0], u + TF[1], p + TF[2]) for e, u, p in items]


def period(a, b):
    if not a:
        return '', '', ''
    return f'{a} CE to {b} CE', f'{a}ء تا {b}ء'.translate(D), f'{a}ع تر {b}ع'.translate(D)


def table(t, tid, rows):
    en, ur, ps = [], [], []
    for ne, nu, np, a, b in rows:
        pe, pu, pp = period(a, b)
        en.append([ne, pe]); ur.append([nu, pu]); ps.append([np, pp])
    t.table(tid, ['Name', 'Period of rule'], en, ['نام', 'عرصہ حکومت'], ['نوم', 'د واکمنۍ موده'], ur, ps)


def p70():
    b = Builder()
    L(b, tf([('d. Imam Malik was a pupil of Imam Ja\'far Sadiq.', 'د: امام مالک امام جعفر صادق کے شاگرد تھے۔', 'د. امام مالک د امام جعفر صادق شاګرد و.'),
             ('e. Imam Shafi\'i was a pupil of Imam Malik.', 'ہ: امام شافعی امام مالک کے شاگرد تھے۔', 'ه. امام شافعي د امام مالک شاګرد و.'),
             ('f. Imam Shafi\'i\'s famous book is "Kitab al-Umm".', 'و: امام شافعی کی مشہور کتاب ”کتاب الام“ ہے۔', 'و. د امام شافعي مشهور کتاب «کتاب الام» دی.'),
             ('g. Imam Ahmad was born in Madinah.', 'ز: امام احمد مدینہ میں پیدا ہوئے۔', 'ز. امام احمد په مدینه کې زېږېدلی.'),
             ('h. Imam Ahmad was a pupil of Imam Shafi\'i.', 'ح: امام احمد، امام شافعی کے شاگرد تھے۔', 'ح. امام احمد د امام شافعي شاګرد و.'),
             ('i. Bu \'Ali Sina had mastery of medicine.', 'ط: بوعلی سینا علمِ طب پر دسترس رکھتے تھے۔', 'ط. بوعلي سینا په طب کې مهارت درلود.'),
             ('j. Bu \'Ali Sina\'s books were taught in the universities of Europe.', 'ی: بوعلی سینا کی کتابیں یورپ کی یونیورسٹیوں میں پڑھائی جاتی تھیں۔', 'ی. د بوعلي سینا کتابونه د اروپا په پوهنتونونو کې تدریسېدل.'),
             ('k. Ya\'qub bin Ishaq Kindi was born in Kufa.', 'ک: یعقوب بن اسحاق کندی کوفہ میں پیدا ہوئے۔', 'ک. یعقوب بن اسحاق کندي په کوفه کې زېږېدلی.'),
             ('l. Farabi was an Arab.', 'ل: فارابی عرب تھا۔', 'ل. فارابي عرب و.'),
             ('m. Tabari came to India to acquire knowledge.', 'م: طبری علم کے حصول کے لئے ہندوستان آیا۔', 'م. طبري د علم د زده‌کړې لپاره هندوستان ته راغی.'),
             ('n. Mas\'udi was born in Kufa.', 'ن: مسعودی کوفہ میں پیدا ہوا۔', 'ن. مسعودي په کوفه کې زېږېدلی.')]))
    r1 = rec(b, 26, 132, 70, [132], kind='exercise')
    t = Builder()
    t.h('Amirs of Andalus', 'امیرانِ اندلس', 'د اندلس امیران')
    table(t, 'ihist12-l27-amirs-1', [
        ('Tariq bin Ziyad, Musa bin Nusayr', 'طارق بن زیاد، موسیٰ بن نصیر', 'طارق بن زیاد، موسی بن نصیر', 712, 714),
        ('Abd al-Aziz bin Musa', 'عبدالعزیز بن موسیٰ', 'عبدالعزیز بن موسی', 714, 716),
        ('Harb bin Abd al-Rahman', 'حرب بن عبدالرحمان', 'حرب بن عبدالرحمن', 716, 718),
        ('Amir Samh bin Malik Fulani', 'امیر سمع بن مالک فولانی', 'امیر سمح بن مالک خولاني', 718, 721),
        ('Amir \'Anbasah bin Suhaym Kalbi', 'امیر عنبسہ بن شحیم کلبی', 'امیر عنبسه بن سحیم کلبي', 721, 725)])
    r2 = rec(t, 27, 132, 70, [132], first=True)
    t2 = Builder()
    table(t2, 'ihist12-l27-amirs-2', [
        ('\'Uqbah bin Hajjaj Saluli', 'عقبہ بن حجاج سلولی', 'عقبه بن حجاج سلولي', 725, 756),
        ('Abd al-Malik bin Balj bin Bishr', 'عبدالملک بن بلخ بن بشر', 'عبدالملک بن بلج بن بشر', None, None),
        ('Abu al-Khattab Kham bin Khirar', 'ابوالخطاب خام بن خرار', 'ابوالخطاب خام بن خرار', None, None),
        ('Tha\'bah bin Salam Judhami', 'ثعبہ بن سلام جذامی', 'ثعبه بن سلام جذامي', None, None),
        ('Amir Abd al-Rahman al-Dakhil', 'امیر عبدالرحمان الداخل', 'امیر عبدالرحمن الداخل', 756, 788),
        ('Hisham bin Abd al-Rahman', 'ہشام بن عبدالرحمان', 'هشام بن عبدالرحمن', 788, 796),
        ('al-Hakam I bin Hisham', 'الحکم اول بن ہشام', 'الحکم اول بن هشام', 796, 822),
        ('Abd al-Rahman II al-Awsat', 'عبدالرحمان ثانی الاوسط', 'عبدالرحمن دویم الاوسط', 822, 842),
        ('Muhammad I bin Abd al-Rahman al-Awsat', 'محمد اول بن عبدالرحمان الاوسط', 'محمد اول بن عبدالرحمن الاوسط', 842, 876),
        ('al-Mundhir bin Muhammad', 'المنذر بن محمد', 'المنذر بن محمد', 876, 878),
        ('Abdullah bin Muhammad', 'عبداللہ بن محمد', 'عبدالله بن محمد', 878, 903),
        ('Abd al-Rahman Nasir', 'عبدالرحمان ناصر', 'عبدالرحمن ناصر', 903, 953),
        ('al-Hakam II', 'الحکم ثانی', 'الحکم دویم', 953, 969),
        ('Hisham II', 'ہشام ثانی', 'هشام دویم', 969, 1000),
        ('Muluk al-Tawa\'if (party kings)', 'طوائف الملوکی', 'طوایف الملوکي', 1000, 1232),
        ('Abd al-Rahman bin Hisham', 'عبدالرحمان بن ہشام', 'عبدالرحمن بن هشام', None, None),
        ('Muhammad bin Abd al-Rahman Mu\'tamid', 'محمد بن عبدالرحمان معتمد', 'محمد بن عبدالرحمن معتمد', None, None),
        ('The last dynasty', 'آخری خاندان', 'وروستۍ کورنۍ', 1232, 1492)])
    BOOK.save(70, [(26, r1), (27, r2), (27, rec(t2, 27, 133, 70, [133]))], complete_units=[26], issues=[{'id': 'ihist12-pdf070', 'unit': 27, 'printedPage': 132,
               'description': 'Lesson 27 "امیرانِ اندلس" is a two-page list (pp.132–133) rendered as structured tables. On p.133 the printed dates sit between rows; they are assigned to the nearest row as printed, and rows with no printed date are left blank (Abd al-Malik bin Balj, Abu al-Khattab, Tha\'bah, Abd al-Rahman bin Hisham, Muhammad bin Abd al-Rahman). Printed names and dates kept as printed (e.g. "عتبہ بن حجاج", "بلخ بن بشر", "سمع بن مالک فولانی", "عنبسہ بن شحیم", "المنذر ۸۷۶ء تا ۸۷۸ء", "عبدالرحمان ناصر ۹۰۳ء تا ۹۵۳ء"); Pashto gives standard spellings for the first two. Student ticks on p.132 excluded.'}])


if __name__ == '__main__':
    p70()
