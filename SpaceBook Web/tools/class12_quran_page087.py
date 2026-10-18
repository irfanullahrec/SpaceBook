"""Mutalia-e-Quran XII PDF87: p.84 — Lesson 8 vocabulary; exercise Q1 items 1–3. Run: python class12_quran_page087.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('لُعِنَ', 'Was cursed', 'لعنت کی گئی', 'لعنت پرې وشو'),
    ('يَتَنَاهَوْنَ', 'They used to forbid one another', 'وہ ایک دوسرے کو روکا کرتے تھے', 'یو بل به یې منع کاوه'),
    ('لَا تُحَرِّمُوا', 'Do not make unlawful', 'تم حرام نہ ٹھہراؤ', 'حرام یې مه ګرځوئ'),
    ('عَقَّدْتُمُ', 'You firmly resolved', 'تم نے پختہ ارادہ کیا', 'تاسو ټینګه اراده وکړه'),
    ('عَشَرَةِ', 'Ten', 'دس', 'لس'),
    ('الْأَنْصَابُ', 'Idols', 'بت', 'بتان'),
    ('رِجْسٌ', 'Impurity, filth', 'ناپاکی، گندگی', 'ناپاکي، ګندګي'),
    ('أَنْ يُوقِعَ', 'That he casts', 'کہ وہ ڈال دے', 'چې واچوي'),
    ('الْبَغْضَاءَ', 'Hatred', 'بغض', 'کینه'),
    ('الْمَيْسِرِ', 'Gambling', 'جوا', 'قمار'),
    ('كَثْرَةُ الْخَبِيثِ', 'The abundance of the impure', 'گندگی / ناپاک کی کثرت', 'د ناپاکو ډېروالی'),
    ('لِسَانِ', 'Tongue', 'زبان', 'ژبه'),
    ('لَتَجِدَنَّ', 'You will surely find', 'آپ ضرور پائیں گے', 'تاسو به خامخا ومومئ'),
    ('طَيِّبَاتِ', 'Pure things', 'پاکیزہ چیزیں', 'پاک شیان'),
    ('فَكَفَّارَتُهُ', 'Then its expiation', 'تو اس کا کفارہ', 'نو کفاره یې'),
    ('أَوْسَطِ', 'Average (middle) degree', 'اوسط (درمیانی) درجہ', 'منځنۍ درجه'),
    ('الْأَزْلَامُ', 'Divining arrows', 'جوئے کے تیر', 'د قمار غشي'),
    ('فَاجْتَنِبُوهُ', 'So avoid it', 'لہٰذا تم اس سے بچو', 'نو ترې ځان وساتئ'),
    ('الْعَدَاوَةَ', 'Enmity', 'عداوت / دشمنی', 'دښمني'),
    ('الْخَمْرِ', 'Wine', 'شراب', 'شراب'),
    ('صَيْدُ', 'Game, hunting', 'شکار', 'ښکار'),
    ('نُرِيدُ', 'We want', 'ہم چاہتے ہیں', 'موږ غواړو'),
]


def p87():
    b = Builder()
    VOC(b, 'mq12-l8-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, 'طَيِّبَٰتِ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('tasty', 'مزے دار', 'خوندوره'), ('excellent', 'عمدہ', 'غوره'), ('pure', 'پاکیزہ', 'پاک'), ('pleasant-looking', 'خوش نما', 'ښکلي')])
    MCQ(b, 2, words(5, 89, 13, 16), ('— according to it, one expiation for breaking an oath is:', 'کی رو سے قسم توڑنے کا ایک کفارہ ہے:', '— له دې سره سم د قسم ماتولو یوه کفاره ده:'),
        [('helping ten poor people', 'دس مسکینوں کی مدد کرنا', 'د لسو مسکینانو مرسته'), ('feeding five poor people', 'پانچ مسکینوں کو کھانا کھلانا', 'پنځو مسکینانو ته خواړه ورکول'), ('clothing ten poor people', 'دس مسکینوں کو کپڑے پہنانا', 'لسو مسکینانو ته جامې ورکول'), ('feeding ten poor people', 'دس مسکینوں کو کھانا کھلانا', 'لسو مسکینانو ته خواړه ورکول')])
    MCQ(b, 3, words(5, 96, 3, 4), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('game of the land', 'خشکی کا شکار', 'د وچې ښکار'), ('game of the sea', 'سمندر کا شکار', 'د سمندر ښکار'), ('game of the air', 'فضا کا شکار', 'د هوا ښکار'), ('game of the desert', 'صحرا کا شکار', 'د دښتې ښکار')])
    BOOK.save(87, [(8, rec(b, 8, 87, 87, kind='exercise'))], issues=[{'id': 'mq12-pdf087', 'unit': 8, 'printedPage': 84,
               'description': 'Four-column vocabulary rendered as one two-column table (22 rows). Quoted verse fragments drawn from the reference Uthmani text. No printed key. A finger and the page edge in the scan excluded.'}])


if __name__ == '__main__':
    p87()
