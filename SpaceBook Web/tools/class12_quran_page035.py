"""Mutalia-e-Quran XII PDF35: p.32 — Lesson 3 vocabulary; exercise Q1 items 1–4. Run: python class12_quran_page035.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('خُذُوا', 'Hold, take', 'تم رکھو، تم پکڑو', 'ونیسئ، ولرئ'),
    ('فَانْفِرُوا', 'So go forth', 'پس تم نکلو', 'نو ووځئ'),
    ('لَيُبَطِّئَنَّ', 'He will surely lag behind', 'وہ ضرور دیر لگائے گا', 'خامخا به ځنډ کوي'),
    ('كَيْدَ', 'Plot, deceit, trick', 'مکر، فریب، چال', 'چل، فرېب، دوکه'),
    ('بُرُوجٍ مُشَيَّدَةٍ', 'Strong fortresses', 'مضبوط قلعے', 'ټینګې کلاګانې'),
    ('لَا تُكَلَّفُ', 'Responsibility is not placed on you', 'تم پر ذمہ داری نہیں ڈالی جاتی ہے', 'پر تا مسؤلیت نه اچول کېږي'),
    ('أَنْ يَكُفَّ', 'That He restrains', 'کہ وہ روک دے', 'چې ودروي'),
    ('كِفْلٌ', 'A burden', 'بوجھ', 'بار'),
    ('فِئَتَيْنِ', 'Two groups', 'دو گروہ', 'دوه ډلې'),
    ('وَدُّوا', 'They wished', 'انھوں نے چاہا', 'هغوی وغوښتل'),
    ('أَلْقَى', 'He offered', 'اس نے پیش کیا', 'هغه وړاندې کړ'),
    ('حِذْرَكُمْ', 'Your means of protection', 'اپنے بچاؤ کا سامان', 'د خپلې ساتنې سامان'),
    ('ثُبَاتٍ', 'In detachments', 'دستوں کی صورت میں', 'په ډلو ډلو'),
    ('مَوَدَّةٌ', 'Friendship', 'دوستی', 'دوستي'),
    ('يُدْرِكْكُمُ الْمَوْتُ', 'Death will overtake you', 'موت تمھیں آ پکڑے گی', 'مرګ به مو ونیسي'),
    ('لَاتَّبَعْتُمْ', 'You would surely have followed', 'یقیناً تم نے پیروی کی', 'یقیناً به مو پیروي کړې وه'),
    ('حَرِّضِ', 'Urge (them)', 'آپ ترغیب دلایے', 'وهڅوئ'),
    ('أَشَدُّ تَنْكِيلًا', 'Most severe in punishment', 'سزا میں بہت سخت', 'په سزا کې ډېر سخت'),
    ('لَيَجْمَعَنَّكُمْ', 'He will surely gather you', 'وہ تمھیں ضرور جمع کرے گا', 'خامخا به مو راټول کړي'),
    ('أَرْكَسَهُمْ', 'He turned them back', 'اس نے انھیں اُلٹا پھیر دیا ہے', 'هغوی یې سرچپه واړول'),
    ('فَتَبَيَّنُوا', 'Then verify well', 'تو خوب تحقیق کر لیا کرو', 'نو ښه تحقیق وکړئ'),
    ('مُسْتَضْعَفِينَ', 'Helpless, weak', 'بے بس، کمزور', 'بې‌وسه، کمزوري'),
]


def p35():
    b = Builder()
    VOC(b, 'mq12-l3-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(4, 71, 8, 10), ('— according to it, Muslims are commanded to go out to fight:', 'کے مطابق مسلمانوں کو حکم ہے کہ وہ لڑائی کے لیے نکلیں:', '— له دې سره سم مسلمانانو ته حکم دی چې جګړې ته ووځي:'),
        [('with a few individuals together', 'کچھ افراد مل کر', 'څو کسان یوځای'), ('secretly', 'چھپ چھپ کر', 'پټ پټ'), ('all together', 'سب مل کر', 'ټول یوځای'), ('one by one', 'اکیلے اکیلے ہو کر', 'یو یو')])
    MCQ(b, 2, 'مَوَدَّةٌ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('friendship', 'دوستی', 'دوستي'), ('goodwill', 'خیر خواہی', 'خیرخواهي'), ('social contact', 'میل جول', 'ګډ ژوند'), ('relationship', 'تعلق داری', 'اړیکه')])
    MCQ(b, 3, words(4, 76, 18, 22), ('— according to it, Satan\'s plot is:', 'کے مطابق شیطان کا مکر ہے:', '— له دې سره سم د شیطان چل دی:'),
        [('ineffective', 'بے اثر', 'بې‌اغېزه'), ('weak', 'کمزور', 'کمزوری'), ('apparent', 'ظاہری', 'ظاهري'), ('temporary', 'عارضی', 'لنډمهاله')])
    MCQ(b, 4, words(4, 81, 14, 17), ('— according to it, the consultations the hypocrites hold at night, Allah Almighty:', 'کی رو سے منافقین جو مشورے راتوں کو کرتے ہیں اللہ تعالیٰ اُسے:', '— له دې سره سم منافقان چې د شپې کومې مشورې کوي، الله تعالی یې:'),
        [('is hearing', 'سن رہا ہے', 'اوري'), ('is seeing', 'دیکھ رہا ہے', 'ګوري'), ('is writing', 'لکھ رہا ہے', 'لیکي'), ('is stating', 'بیان کر رہا ہے', 'بیانوي')])
    BOOK.save(35, [(3, rec(b, 3, 35, 35, kind='exercise'))], issues=[{'id': 'mq12-pdf035', 'unit': 3, 'printedPage': 32,
               'description': 'Four-column vocabulary rendered as one two-column table (22 rows). No printed key.'}])


if __name__ == '__main__':
    p35()
