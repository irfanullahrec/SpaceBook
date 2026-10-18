"""Mutalia-e-Quran XII PDF194: p.191 — Lesson 20 vocabulary; exercise Q1 items 1–4. Run: python class12_quran_page194.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('دِيَارِهِمْ', 'Their homes', 'اُن کے گھر', 'د هغوی کورونه'),
    ('أَنَّهُمْ مَانِعَتُهُمْ', 'That they would protect them', 'کہ وہ ان کو بچا لیں گے', 'چې هغوی به یې وژغوري'),
    ('حُصُونُهُمْ', 'Their fortresses', 'اُن کے قلعے', 'د هغوی کلاګانې'),
    ('الْجَلَاءَ', 'Exile', 'جلاوطنی', 'جلاوطني'),
    ('مَنْ يُشَاقِّ', 'Whoever opposes', 'جو مخالفت کرتا ہے', 'څوک چې مخالفت کوي'),
    ('شَدِيدُ الْعِقَابِ', 'Severe in punishment', 'بہت سخت عذاب', 'ډېر سخت عذاب'),
    ('قَطَعْتُمْ', 'You cut down', 'تم نے کاٹا', 'تاسو پرې کړل'),
    ('لِينَةٍ', 'A date-palm', 'کھجور کا درخت', 'د کجورې ونه'),
    ('تَرَكْتُمُوهَا', 'You left it', 'تم نے اسے چھوڑ دیا', 'تاسو پرېښوده'),
    ('فَمَا أَوْجَفْتُمْ', 'You did not spur on', 'تو تم نے نہیں دوڑائے', 'نو تاسو ونه ځغلول'),
    ('خَيْلٍ', 'Horses', 'گھوڑے', 'اسونه'),
    ('يُسَلِّطُ', 'He gives authority', 'وہ غالب کر دیتا ہے', 'غالبوي'),
    ('شُحَّ نَفْسِهِ', 'The greed of his own soul', 'اُس کے نفس کا بخل', 'د هغه د نفس بخل'),
    ('لَا نُطِيعُ', 'We will not obey', 'ہم نہیں مانیں گے', 'نه به منو'),
    ('رَهْبَةً', 'Fear, dread', 'ڈر، خوف', 'وېره'),
    ('قُرًى مُحَصَّنَةٍ', 'Fortified towns', 'قلعہ بند بستیاں', 'کلابند کلي'),
    ('مِنْ وَرَاءِ جُدُرٍ', 'From behind walls', 'دیواروں کی آڑ میں', 'د دېوالونو تر شا'),
    ('وَلْتَنْظُرْ نَفْسٌ', 'And let every soul look', 'اور چاہیے کہ ہر شخص دیکھتا رہے', 'او هر کس دې وګوري'),
    ('لِغَدٍ', 'For tomorrow', 'کل کے لیے', 'د سبا لپاره'),
    ('جَبَلٍ', 'A mountain', 'پہاڑ', 'غر'),
    ('خَشْيَةِ اللَّهِ', 'The fear of Allah', 'اللہ کا خوف', 'د الله وېره'),
    ('الْمُؤْمِنُ', 'The Giver of security', 'امن بخشنے والا', 'امن بښونکی'),
]


def p194():
    b = Builder()
    VOC(b, 'mq12-l20-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(59, 2, 1, 10), ('— according to this, Allah Almighty made the disbelievers of the People of the Book homeless from their:', 'کے مطابق اللہ تعالیٰ نے کافر اہلِ کتاب کو بے دخل کیا ان کے:', '— له دې سره سم الله تعالی کافر اهل کتاب له خپلو ... بې‌ځایه کړل:'),
        [('gardens', 'باغات سے', 'باغونو'), ('fields', 'کھیتوں سے', 'کښتونو'), ('houses', 'گھروں سے', 'کورونو'), ('forts', 'قلعوں سے', 'کلاګانو')])
    MCQ(b, 2, words(59, 2, 19, 24), ('— according to this, the Jews thought that their ___ would save them from the punishment of Allah Almighty:', 'کی رو سے یہود کا گمان تھا کہ انھیں اللہ تعالیٰ کے عذاب سے بچا لیں گے ان کے:', '— له دې سره سم یهودو ګومان کاوه چې د الله تعالی له عذابه به یې وژغوري د هغوی:'),
        [('forts', 'قلعے', 'کلاګانې'), ('wealth', 'مال', 'مال'), ('tribes', 'قبائل', 'قبیلې'), ('armies', 'لشکر', 'لښکرې')])
    MCQ(b, 3, 'ٱلْجَلَآءَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('jail', 'جیل', 'زندان'), ('exile', 'جلاوطنی', 'جلاوطني'), ('cantonment', 'چھاؤنی', 'چاوڼۍ'), ('war', 'جنگ', 'جګړه')])
    MCQ(b, 4, words(59, 5, 1, 4), ('— in this, the cutting of which trees in the war with the Jews is mentioned:', 'میں یہود کے ساتھ لڑائی کے لیے درختوں کے کاٹنے کا ذکر ہے:', '— په دې کې له یهودو سره د جګړې لپاره د کومو ونو د پرې کولو یادونه ده:'),
        [('date-palms', 'کھجور کے', 'د کجورو'), ('olive trees', 'زیتون کے', 'د زیتونو'), ('pomegranate trees', 'انار کے', 'د انارو'), ('jujube trees', 'بیری کے', 'د بېرو')])
    BOOK.save(194, [(20, rec(b, 20, 194, 194, kind='exercise'))], issues=[{'id': 'mq12-pdf194', 'unit': 20, 'printedPage': 191,
               'description': 'The vocabulary table is printed blurred (out of focus); words read with care. Four-column vocabulary rendered as one two-column table (22 rows). The exercise continues on p.192. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p194()
