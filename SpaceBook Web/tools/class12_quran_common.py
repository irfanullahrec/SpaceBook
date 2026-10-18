"""Shared Class 12 Mutalia-e-Quran-e-Hakeem (Lazmi), KPTBB test edition 2026-27, developed by The ILM Foundation (Urdu source).
231 single portrait pages: PDF1 cover, PDF2 publisher ad (excluded), PDF3–8 front matter, PDF9 = printed p.6 (printed = pdf − 3),
PDF230 feedback form, PDF231 back cover. Lessons 1–24 are units (book's own numbering).

Qur'anic text: Uthmani script from the alquran.cloud cache D:/SpaceBook/_qcache/sNN.json (the scan prints the same text with
word-by-word Urdu glosses under each word group); English = M. M. Pickthall (1930, public domain) from pk_sNN.json;
Urdu = the book's own running translation transcribed from the scan; Pashto = ours, following the book's Urdu.
A verse that runs across a page break is recorded on the page where it ends."""
import json
from pathlib import Path
from class12_book_common import Book, Builder  # noqa: F401

BOOK = Book('quran')
CACHE = Path('D:/SpaceBook/_qcache')
BASMALA = 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ '
AR_DIG = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
UR_DIG = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

# (number, start page, english, urdu, pashto)
LESSONS = [
    (1, 6, 'Surah al-Nisa\' (verses 1–25)', 'سُوْرَةُ النِّسَآءِ (آیات: ۱ تا ۲۵)', 'سورة النساء (آیتونه ۱–۲۵)'),
    (2, 16, 'Surah al-Nisa\' (verses 26–70)', 'سُوْرَةُ النِّسَآءِ (آیات: ۲۶ تا ۷۰)', 'سورة النساء (آیتونه ۲۶–۷۰)'),
    (3, 26, 'Surah al-Nisa\' (verses 71–100)', 'سُوْرَةُ النِّسَآءِ (آیات: ۷۱ تا ۱۰۰)', 'سورة النساء (آیتونه ۷۱–۱۰۰)'),
    (4, 35, 'Surah al-Nisa\' (verses 101–134)', 'سُوْرَةُ النِّسَآءِ (آیات: ۱۰۱ تا ۱۳۴)', 'سورة النساء (آیتونه ۱۰۱–۱۳۴)'),
    (5, 43, 'Surah al-Nisa\' (verses 135–176)', 'سُوْرَةُ النِّسَآءِ (آیات: ۱۳۵ تا ۱۷۶)', 'سورة النساء (آیتونه ۱۳۵–۱۷۶)'),
    (6, 53, 'Surah al-Ma\'idah (verses 1–34)', 'سُوْرَةُ الْمَآئِدَةِ (آیات: ۱ تا ۳۴)', 'سورة المائدة (آیتونه ۱–۳۴)'),
    (7, 65, 'Surah al-Ma\'idah (verses 35–77)', 'سُوْرَةُ الْمَآئِدَةِ (آیات: ۳۵ تا ۷۷)', 'سورة المائدة (آیتونه ۳۵–۷۷)'),
    (8, 76, 'Surah al-Ma\'idah (verses 78–120)', 'سُوْرَةُ الْمَآئِدَةِ (آیات: ۷۸ تا ۱۲۰)', 'سورة المائدة (آیتونه ۷۸–۱۲۰)'),
    (9, 87, 'Surah al-Nur (verses 1–34)', 'سُوْرَةُ النُّوْرِ (آیات: ۱ تا ۳۴)', 'سورة النور (آیتونه ۱–۳۴)'),
    (10, 96, 'Surah al-Nur (verses 35–64)', 'سُوْرَةُ النُّوْرِ (آیات: ۳۵ تا ۶۴)', 'سورة النور (آیتونه ۳۵–۶۴)'),
    (11, 105, 'Surah al-Ahzab (verses 1–34)', 'سُوْرَةُ الْاَحْزَابِ (آیات: ۱ تا ۳۴)', 'سورة الاحزاب (آیتونه ۱–۳۴)'),
    (12, 114, 'Surah al-Ahzab (verses 35–73)', 'سُوْرَةُ الْاَحْزَابِ (آیات: ۳۵ تا ۷۳)', 'سورة الاحزاب (آیتونه ۳۵–۷۳)'),
    (13, 123, 'Surah Ha-Mim al-Sajdah', 'سُوْرَةُ حٰمٓ السَّجْدَةِ', 'سورة حم السجدة'),
    (14, 135, 'Surah al-Shura', 'سُوْرَةُ الشُّوْرٰى', 'سورة الشوری'),
    (15, 145, 'Surah Muhammad', 'سُوْرَةُ مُحَمَّدٍ', 'سورة محمد'),
    (16, 154, 'Surah al-Fath', 'سُوْرَةُ الْفَتْحِ', 'سورة الفتح'),
    (17, 162, 'Surah al-Hujurat', 'سُوْرَةُ الْحُجُرٰتِ', 'سورة الحجرات'),
    (18, 169, 'Surah al-Hadid', 'سُوْرَةُ الْحَدِيْدِ', 'سورة الحدید'),
    (19, 178, 'Surah al-Mujadalah', 'سُوْرَةُ الْمُجَادَلَةِ', 'سورة المجادلة'),
    (20, 186, 'Surah al-Hashr', 'سُوْرَةُ الْحَشْرِ', 'سورة الحشر'),
    (21, 193, 'Surah al-Mumtahanah', 'سُوْرَةُ الْمُمْتَحَنَةِ', 'سورة الممتحنة'),
    (22, 200, 'Surah al-Saff and Surah al-Jumu\'ah', 'سُوْرَةُ الصَّفِّ اور سُوْرَةُ الْجُمُعَةِ', 'سورة الصف او سورة الجمعة'),
    (23, 208, 'Surah al-Munafiqun and Surah al-Taghabun', 'سُوْرَةُ الْمُنٰفِقُوْنَ اور سُوْرَةُ التَّغَابُنِ', 'سورة المنافقون او سورة التغابن'),
    (24, 217, 'Surah al-Talaq and Surah al-Tahrim', 'سُوْرَةُ الطَّلَاقِ اور سُوْرَةُ التَّحْرِيْمِ', 'سورة الطلاق او سورة التحریم'),
]
UNITS = {'FM': ('Front matter', 'ابتدائیہ', 'لومړنۍ برخه'), 'BM': ('Back matter', 'اختتامیہ', 'وروستۍ برخه')}
for n, _, e, u, p in LESSONS:
    UNITS[n] = (e, u, p)


def pages(pdf):
    return [pdf - 3] if 9 <= pdf <= 229 else [None]


def rec(b, unit, n, pdf, pages_=None, first=False, kind='text'):
    u = UNITS[unit]
    if unit in ('FM', 'BM'):
        uid, le, lu, lp = unit.lower(), u[0], u[1], u[2]
    else:
        uid, le, lu, lp = f'l{unit}', f'Lesson {unit}', f'سبق {unit}', f'{unit} لوست'
    return BOOK.record(b, f'mq12-{uid}-{kind}-{n}', f'{le} — {kind} ({n})', f'{lu} — متن ({n})', f'{lp} — متن ({n})', pdf,
                       pages_ or pages(pdf), unit_title=u if first else None)


_ar, _en = {}, {}


def _load(s):
    if s not in _ar:
        _ar[s] = [x['text'] for x in json.loads((CACHE / f's{s}.json').read_text(encoding='utf-8'))['data']['ayahs']]
        _en[s] = [x['text'] for x in json.loads((CACHE / f'pk_s{s}.json').read_text(encoding='utf-8'))['data']['ayahs']]


def ayah(s, a):
    _load(s)
    t = _ar[s][a - 1]
    if a == 1 and s not in (1, 9):
        w = t.split(' ')
        if w[0].startswith('بِسْمِ'):
            t = ' '.join(w[4:])
    return t


def words(s, a, i=None, j=None):
    """Arabic words i..j (1-based, inclusive) of verse s:a — for exercise questions that quote part of a verse."""
    w = ayah(s, a).split()
    return ' '.join(w[(i or 1) - 1:(j or len(w))])


def mark(a):
    return f'﴿{str(a).translate(AR_DIG)}﴾'


def V(b, s, a, ur, ps, a2=None):
    """Verse(s) s:a[..a2] with the book's Urdu and our Pashto; English is Pickthall."""
    _load(s)
    rng = range(a, (a2 or a) + 1)
    ar = ' '.join(f'{ayah(s, k)} {mark(k)}' for k in rng)
    en = ' '.join(_en[s][k - 1] for k in rng)
    ref = f'({s}:{a}' + (f'–{a2}' if a2 else '') + ')'
    b.p(f'{ar}\n{en} {ref}', f'{ar}\n{ur}', f'{ar}\n{ps}')
    b.paras[-1]['arabicSource'] = True


def AR(b, arabic, en, ur, ps):
    """A quoted Arabic phrase (exercise or note) followed by the instruction in each language."""
    b.p(f'{arabic} — {en}', f'{arabic} — {ur}', f'{arabic} — {ps}')


def L(b, items):
    b.group('list', items)


def S(b, rows):
    for h, p in rows:
        if h:
            b.h(*h)
        if p:
            b.p(*p)


def VOC(b, tid, rows):
    """Vocabulary table: rows = (arabic word, meaning en, meaning ur, meaning ps)."""
    b.h('Vocabulary', 'ذخیرۂ الفاظ', 'د کلمو زېرمه')
    b.table(tid, ['Word', 'Meaning'], [[w, e] for w, e, u, p in rows], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in rows], [[w, p] for w, e, u, p in rows])


KEYS = [('a', 'الف', 'الف'), ('b', 'ب', 'ب'), ('c', 'ج', 'ج'), ('d', 'د', 'د')]


def MCQ(b, n, ar, q, opts):
    """Multiple-choice item: ar = quoted Arabic ('' if none), q = (en, ur, ps), opts = [(en, ur, ps)] × 4."""
    lead = f'({n}) {ar} ' if ar else f'({n}) '
    b.p(lead + q[0], lead + q[1], lead + q[2])
    b.group('list', [(f'{k[0]}. {o[0]}', f'{k[1]}: {o[1]}', f'{k[2]}. {o[2]}') for k, o in zip(KEYS, opts)])


def KA(b):
    b.h('Matters of knowledge and action', 'علم و عمل کی باتیں', 'د علم او عمل خبرې')


def EX(b):
    b.h('Exercise', 'مشق', 'تمرین')


Q1 = ('Question 1: Put a tick (✓) on the correct answer:', 'سوال ۱: درست جواب پر صحیح (✓) کا نشان لگائیں:', '۱ پوښتنه: پر سم ځواب (✓) نښه ولګوئ:')
Q2 = ('Question 2: Give short answers to the following questions:', 'سوال ۲: مندرجہ ذیل سوالات کے مختصر جوابات دیجیے:', '۲ پوښتنه: لاندې پوښتنو ته لنډ ځوابونه ورکړئ:')
Q3 = ('Question 3: Give detailed answers to the following questions:', 'سوال ۳: مندرجہ ذیل سوالات کے تفصیلی جوابات دیجیے:', '۳ پوښتنه: لاندې پوښتنو ته تفصیلي ځوابونه ورکړئ:')
TR = ('Write the translation of the verse.', 'آیت کریمہ کا ترجمہ تحریر کریں۔', 'د آیت ژباړه ولیکئ.')
ACT = ('Activities for students', 'سرگرمیاں برائے طلبہ', 'د زده‌کوونکو لپاره فعالیتونه')
TCH = ('Guidance for teachers', 'ہدایات برائے اساتذہ کرام', 'د ښوونکو لپاره لارښوونې')
