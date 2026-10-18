"""Mutalia-e-Quran XII PDF124: p.121 — Lesson 12 vocabulary (end); exercise Q1, Q2 items 1–2. Run: python class12_quran_page124.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words

VOCAB = [
    ('أَخَوَاتِهِنَّ', 'Their sisters', 'ان کی بہنیں', 'د هغوی خویندې'),
    ('يُصَلُّونَ', 'They send blessings', 'وہ درود بھیجتے ہیں', 'درود لېږي'),
    ('سَلِّمُوا', 'Send peace (salutations)', 'تم سلام بھیجو', 'سلام ولېږئ'),
    ('فَقَدِ احْتَمَلُوا', 'Then they have surely borne', 'تو یقیناً انھوں نے بوجھ اٹھایا', 'نو یقیناً یې بار پر غاړه واخیست'),
    ('يُدْنِينَ', 'They should draw down', 'وہ لٹکا لیا کریں', 'راځوړند دې کړي'),
    ('جَلَابِيبِهِنَّ', 'Their outer sheets', 'اپنی چادریں', 'خپل څادرونه'),
]


def p124():
    b = Builder()
    b.table('mq12-l12-vocab-2', ['Word', 'Meaning'], [[w, e] for w, e, u, p in VOCAB], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in VOCAB], [[w, p] for w, e, u, p in VOCAB])
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, 'ٱلْقَٰنِتِينَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('men who are humble', 'عاجزی کرنے والے مرد', 'عاجزي کوونکي نارینه'), ('men who fear', 'ڈرنے والے مرد', 'وېرېدونکي نارینه'), ('men who are obedient', 'فرماں بردار مرد', 'فرمانبردار نارینه'), ('men who are content', 'قناعت کرنے والے مرد', 'قناعت کوونکي نارینه')])
    MCQ(b, 2, words(33, 35, 18, 20), ('— according to this, men and women guard their:', 'کی رو سے مرد اور خواتین حفاظت کرنے والے ہیں:', '— له دې سره سم نارینه او ښځې ساتونکي دي:'),
        [('eyes', 'آنکھوں کی', 'د سترګو'), ('faces', 'چہروں کی', 'د مخونو'), ('hands', 'ہاتھوں کی', 'د لاسونو'), ('private parts', 'شرم گاہوں کی', 'د شرمګاهونو')])
    MCQ(b, 3, words(33, 37, 22, 25), ('— according to this, Allah Almighty has more right that:', 'کے مطابق اللہ تعالیٰ زیادہ حق دار ہے کہ:', '— له دې سره سم الله تعالی ډېر حقدار دی چې:'),
        [('one should fast for Him', 'اس کے لیے روزہ رکھا جائے', 'د هغه لپاره روژه ونیول شي'), ('one should spend in His way', 'اس کی راہ میں خرچ کیا جائے', 'د هغه په لار کې ولګول شي'), ('jihad should be done in His way', 'اس کی راہ میں جہاد کیا جائے', 'د هغه په لار کې جهاد وشي'), ('He should be feared', 'اس سے ڈرا جائے', 'له هغه ووېرېږل شي')])
    MCQ(b, 4, 'مُبَشِّرًا', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('one who praises', 'تعریف کرنے والے', 'ستاینه کوونکی'), ('one who gives glad tidings', 'خوش خبری دینے والے', 'زېری ورکوونکی'), ('one who shows mercy', 'رحم کرنے والے', 'رحم کوونکی'), ('one who loves', 'محبت کرنے والے', 'مینه کوونکی')])
    MCQ(b, 5, words(33, 46, 5, 6), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('a bright star', 'روشن ستارہ', 'روښانه ستوری'), ('a shining sun', 'چمکتا سورج', 'ځلېدونکی لمر'), ('a light-giving lamp', 'روشن چراغ', 'روښانه څراغ'), ('a radiant moon', 'تابناک چاند', 'ځلانده سپوږمۍ')])
    MCQ(b, 6, words(33, 53, 25, 26), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('to sit on engaged in talk', 'باتوں میں لگے بیٹھے رہنا', 'په خبرو بوخت ناست پاتې کېدل'), ('to be busy in play', 'کھیل کود میں لگنا', 'په لوبو بوختېدل'), ('to be busy in necessary work', 'ضروری کام میں لگنا', 'په اړین کار بوختېدل'), ('to be busy in futile work', 'لایعنی کام میں لگنا', 'په بې‌ګټې کار بوختېدل')])
    MCQ(b, 7, words(33, 70, 6, 8), ('— in this the command is to speak in a manner that is:', 'میں بات کرنے کا حکم ہے:', '— په دې کې د خبرو کولو حکم دی:'),
        [('brief', 'مختصر', 'لنډه'), ('comprehensive', 'جامع', 'جامع'), ('straight', 'سیدھی', 'سمه'), ('quiet', 'آہستہ', 'ورو')])
    b.p(*Q2)
    AR(b, f'(1) {words(33, 39)}', 'What attributes of the noble Prophets (peace be upon them) have been stated in the verse?', 'آیت کریمہ میں انبیاء کرام علیہم السلام کی کون سی صفات بیان کی گئی ہیں؟', 'په آیت کې د انبیاء کرامو علیهم السلام کوم صفتونه بیان شوي؟')
    AR(b, f'(2) {words(33, 44)}', 'According to the verse, how will the people of faith be welcomed at the time of meeting Allah Almighty?', 'آیت کریمہ کے مطابق اللہ تعالیٰ سے ملاقات کے وقت اہلِ ایمان کا استقبال کس طرح کیا جائے گا؟', 'د آیت له مخې له الله تعالی سره د ملاقات پر مهال به د مؤمنانو هرکلی څنګه وشي؟')
    BOOK.save(124, [(12, rec(b, 12, 124, 124, kind='exercise'))], issues=[{'id': 'mq12-pdf124', 'unit': 12, 'printedPage': 121,
               'description': 'Last three rows of the vocabulary (continued from p.120) rendered as a continuation table. MCQ 7 quotes قُولُوا قَوْلًا سَدِيدًا (33:70). Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p124()
