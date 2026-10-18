"""Mutalia-e-Quran XII PDF65: p.62 — Lesson 6 vocabulary; exercise Q1 items 1–4. Run: python class12_quran_page065.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('أَوْفُوا بِالْعُقُودِ', 'Fulfil your promises', 'تم اپنے وعدے پورے کرو', 'خپلې ژمنې پوره کړئ'),
    ('الْمَوْقُوذَةُ', 'That which dies from a blow', 'چوٹ لگنے سے مرنے والا', 'په ګوزار مړ شوی'),
    ('أَكْمَلْتُ', 'I have perfected', 'میں نے مکمل کر دیا', 'ما بشپړ کړ'),
    ('قُمْتُمْ', 'You rise, you stand up', 'تم اٹھو، تم کھڑے ہو جاؤ', 'پاڅېږئ، ودرېږئ'),
    ('رُءُوسِكُمْ', 'Your heads', 'تمھارے سر', 'ستاسو سرونه'),
    ('الْكَعْبَيْنِ', 'Ankles', 'ٹخنے', 'بجلکې'),
    ('فَكَفَّ', 'Then He restrained', 'تو اس نے روک دیا', 'نو منع یې کړل'),
    ('لَمْ يُؤْتِ', 'He did not give', 'اس نے نہیں دیا', 'ورنه کړ'),
    ('أَرْبَعِينَ سَنَةً', 'Forty years', 'چالیس سال', 'څلوېښت کاله'),
    ('قَرَّبَا', 'They both offered a sacrifice', 'ان دونوں نے قربانی پیش کی', 'دواړو قرباني وړاندې کړه'),
    ('غُرَابًا', 'A crow', 'کوّا', 'کارغه'),
    ('يُصَلَّبُوا', 'They be crucified', 'انھیں سولی پر لٹکا دیا جائے گا', 'پر دار به وځړول شي'),
    ('الْمُنْخَنِقَةُ', 'That which dies by strangling', 'گلا گھٹنے سے مرنے والا', 'په زندۍ مړ شوی'),
    ('الْمُتَرَدِّيَةُ', 'That which dies by falling from a height', 'اوپر سے گر کر مرنے والا', 'له پاسه لوېدلی مړ شوی'),
    ('رَضِيتُ', 'I have approved', 'میں نے پسند کر لیا', 'ما خوښ کړ'),
    ('الْمَرَافِقِ', 'The elbows', 'کہنیاں', 'څنګلې'),
    ('أَرْجُلَكُمْ', 'Your feet', 'تمھارے پاؤں', 'ستاسو پښې'),
    ('هَمَّ', 'He intended', 'اس نے ارادہ کیا', 'اراده یې وکړه'),
    ('مُلُوكًا', 'Kings', 'بادشاہ', 'پاچاهان'),
    ('قَاعِدُونَ', 'Those who sit', 'بیٹھنے والے', 'ناست'),
    ('يَتِيهُونَ', 'They will wander', 'وہ بھٹکتے پھریں گے', 'سرګردانه به ګرځي'),
    ('لَأَقْتُلَنَّكَ', 'I will surely kill you', 'میں ضرور تجھے قتل کر دوں گا', 'زه به خامخا تا ووژنم'),
    ('يُحَارِبُونَ', 'They wage war', 'وہ لڑائی کرتے ہیں', 'جګړه کوي'),
    ('الْمَائِدَةُ', 'Table spread', 'دستر خوان', 'دسترخوان'),
]


def p65():
    b = Builder()
    VOC(b, 'mq12-l6-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, 'ٱلْمَآئِدَةُ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('green vegetables', 'سبزی', 'سبزي'), ('cooked vegetables', 'ترکاری', 'ترکاري'), ('table spread', 'دستر خوان', 'دسترخوان'), ('fruit', 'پھل', 'مېوه')])
    MCQ(b, 2, words(5, 2, 25, 27), ('— in it, after releasing the ihram, permission has been given for:', 'میں احرام کھولنے کے بعد اجازت دی گئی ہے:', '— په دې کې له احرام پرانیستو وروسته اجازه ورکړل شوې:'),
        [('shaving the head', 'سر منڈانے کی', 'د سر خرېیلو'), ('trimming the nails', 'ناخن تراشنے کی', 'د نوکانو پرې کولو'), ('hunting', 'شکار کی', 'د ښکار'), ('applying perfume', 'خوشبو لگانے کی', 'د خوشبو لګولو')])
    MCQ(b, 3, 'ٱلْمَوْقُوذَةُ', ('— is the animal that dies:', 'وہ جانور ہے جو مر جائے:', '— هغه ځناور دی چې مړ شي:'),
        [('by strangling', 'گلا گھٹنے سے', 'په زندۍ'), ('by a blow', 'چوٹ لگنے سے', 'په ګوزار'), ('by falling from above', 'اوپر سے گرنے سے', 'له پاسه په لوېدو'), ('by being gored', 'سینگ لگنے سے', 'په ښکر وهلو')])
    MCQ(b, 4, words(5, 5, 6, 11), ('— according to it, the food of the People of the Book has been declared:', 'کے مطابق اہلِ کتاب کا کھانا قرار دیا گیا ہے:', '— له دې سره سم د اهل کتابو خواړه ګرځول شوي:'),
        [('permissible', 'مباح', 'مباح'), ('disliked', 'مکروہ', 'مکروه'), ('lawful', 'حلال', 'حلال'), ('unlawful', 'حرام', 'حرام')])
    BOOK.save(65, [(6, rec(b, 6, 65, 65, kind='exercise'))], issues=[{'id': 'mq12-pdf065', 'unit': 6, 'printedPage': 62,
               'description': 'Four-column vocabulary rendered as one two-column table (24 rows). Quoted verse fragments drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p65()
