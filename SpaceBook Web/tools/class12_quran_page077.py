"""Mutalia-e-Quran XII PDF77: p.74 — Lesson 7 vocabulary (end); exercise Q1, Q2 items 1–4. Run: python class12_quran_page077.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words

VOCAB = [
    ('ثَالِثُ ثَلَاثَةٍ', 'The third of three', 'تین میں سے تیسرا', 'له درېیو درېیم'),
    ('لَيَمَسَّنَّ', 'It will surely touch', 'یقیناً وہ ضرور پہنچے گا', 'خامخا به ورسېږي'),
    ('لَمْ يَنْتَهُوا', 'They did not desist', 'وہ باز نہیں آئے', 'لاس یې وانه خیست'),
    ('كَانَا يَأْكُلَانِ', 'Both used to eat', 'وہ دونوں کھایا کرتے تھے', 'دواړو به خوړل'),
]


def p77():
    b = Builder()
    b.table('mq12-l7-vocab-2', ['Word', 'Meaning'], [[w, e] for w, e, u, p in VOCAB], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in VOCAB], [[w, p] for w, e, u, p in VOCAB])
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(5, 38, 1, 4), ('— according to it, cutting off the hand is the punishment for:', 'کے مطابق ہاتھ کاٹنا سزا ہے:', '— له دې سره سم د لاس پرې کول د ... سزا ده:'),
        [('theft', 'چوری کی', 'غلا'), ('drinking wine', 'شراب نوشی کی', 'شراب څښل'), ('murder', 'قتل کی', 'وژنه'), ('breach of trust', 'خیانت کی', 'خیانت')])
    MCQ(b, 2, 'يُحَرِّفُونَ ٱلْكَلِمَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('they forget the word', 'وہ کلام کو بھلا دیتے ہیں', 'کلام هېروي'), ('they abandon the word', 'وہ کلام کو چھوڑ دیتے ہیں', 'کلام پرېږدي'), ('they alter the word', 'وہ کلام کو بدل دیتے ہیں', 'کلام اړوي'), ('they ignore the word', 'وہ کلام کو نظر انداز کر دیتے ہیں', 'کلام له پامه غورځوي')])
    MCQ(b, 3, words(5, 45, 13, 14), ('— according to it, the retaliation stated is:', 'کی رو سے بدلہ بیان ہوا ہے:', '— له دې سره سم کومه بدله بیان شوې:'),
        [('life for life', 'جان کے بدلے جان', 'ځان د ځان په بدل'), ('eye for eye', 'آنکھ کے بدلے آنکھ', 'سترګه د سترګې په بدل'), ('nose for nose', 'ناک کے بدلے ناک', 'پوزه د پوزې په بدل'), ('tooth for tooth', 'دانت کے بدلے دانت', 'غاښ د غاښ په بدل')])
    MCQ(b, 4, 'قِصَاصٌ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('ransom', 'فدیہ', 'فدیه'), ('retaliation', 'بدلہ', 'بدله'), ('covenant', 'معاہدہ', 'تړون'), ('peace', 'صلح', 'روغه')])
    MCQ(b, 5, words(5, 48, 28, 32), ('— according to it, what has been appointed for every Ummah is:', 'کے مطابق ہر اُمت کے لیے مقرر کیا گیا ہے:', '— له دې سره سم هر امت ته ټاکل شوي:'),
        [('a Messenger and a scripture', 'رسول اور صحیفہ', 'رسول او صحیفه'), ('a law and a way', 'شریعت اور راستہ', 'شریعت او لاره'), ('prayer and sacrifice', 'نماز اور قربانی', 'لمونځ او قرباني'), ('wisdom and advice', 'حکمت اور نصیحت', 'حکمت او نصیحت')])
    MCQ(b, 6, words(5, 51, 2, 9), ('— in this verse, the Jews and Christians are forbidden:', 'آیت کریمہ میں یہود و نصاریٰ سے منع کیا گیا:', '— په دې آیت کې له یهودو او نصاراوو ... منع شوې:'),
        [('travelling with them', 'سفر کرنے سے', 'سفر'), ('befriending them', 'دوستی کرنے سے', 'دوستي'), ('doing business with them', 'کاروبار کرنے سے', 'سوداګري'), ('living with them', 'رہائش اختیار کرنے سے', 'استوګنه')])
    MCQ(b, 7, '"مُهَيْمِنًا"', ('— in it the attribute of the Qur\'an Majeed stated is that it:', 'میں قرآن مجید کی صفت بیان ہوئی کہ وہ:', '— په دې کې د قرآن مجید صفت بیان شوی چې هغه:'),
        [('was revealed with the truth', 'حق کے ساتھ نازل ہوا', 'په حق نازل شوی'), ('is a guardian over previous books', 'سابقہ کتب پر نگران ہے', 'پر پخوانیو کتابونو څارونکی دی'), ('abrogates previous books', 'سابقہ کتب کا ناسخ ہے', 'د پخوانیو کتابونو ناسخ دی'), ('confirms previous books', 'سابقہ کتب کی تصدیق کرنے والا ہے', 'د پخوانیو کتابونو تصدیقوونکی دی')])
    b.p(*Q2)
    AR(b, f'(1) {words(5, 42, 1, 4)}', 'Which two qualities of the Jews have been stated in the verse?', 'آیت کریمہ میں یہود کی کون سی دو بُری صفات بیان ہوئی ہیں؟', 'په آیت کې د یهودو کوم دوه بد صفتونه بیان شوي؟')
    AR(b, f'(2) {words(5, 52, 1, 12)}', 'According to the verse, why do the hypocrites run towards the People of the Book?', 'آیت کریمہ کے مطابق منافقین اہلِ کتاب کی طرف کیوں دوڑتے ہیں؟', 'د آیت له مخې منافقان ولې د اهل کتابو پر لور منډې وهي؟')
    AR(b, f'(3) {words(5, 58, 1, 7)}', 'According to the verse, what was the conduct of the disbelievers at the time of the adhan?', 'آیت کریمہ کے مطابق اذان کے وقت کفار کا کیا طرزِ عمل ہوتا تھا؟', 'د آیت له مخې د اذان پر مهال د کافرانو چلند څنګه و؟')
    AR(b, f'(4) {words(5, 64, 9, 18)}', 'What answer has been given in the verse to the insolence of the Jews?', 'آیت کریمہ میں یہود کی گستاخی کا کیا جواب دیا گیا ہے؟', 'په آیت کې د یهودو بې‌ادبۍ ته څه ځواب ورکړل شوی؟')
    BOOK.save(77, [(7, rec(b, 7, 77, 77, kind='exercise'))], issues=[{'id': 'mq12-pdf077', 'unit': 7, 'printedPage': 74,
               'description': 'Four further vocabulary words continue from p.73. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p77()
