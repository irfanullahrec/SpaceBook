"""Mutalia-e-Quran XII PDF155: p.152 — Lesson 15 exercise Q1, Q2. Run: python class12_quran_page155.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words


def p155():
    b = Builder()
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, 'ٱلرِّقَابِ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('necks', 'گردنیں', 'غاړې'), ('feet', 'پاؤں', 'پښې'), ('arms', 'بازو', 'مټې'), ('legs', 'ٹانگیں', 'لنګي')])
    MCQ(b, 2, 'ٱلْحَرْبُ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('arrow', 'تیر', 'غشی'), ('sword', 'تلوار', 'توره'), ('war', 'جنگ', 'جګړه'), ('armour', 'زرہ', 'زغره')])
    MCQ(b, 3, words(47, 12, 14, 20), ('— according to this, the disbelievers eat like:', 'کی رو سے کفر کرنے والے ایسے کھاتے ہیں جیسے:', '— له دې سره سم کافران داسې خوري لکه:'),
        [('the ignorant', 'جاہل', 'ناپوه'), ('cattle', 'چوپائے', 'څاروي'), ('the hungry', 'بھوکے', 'وږي'), ('the greedy', 'لالچی', 'حریصان')])
    MCQ(b, 4, 'عَسَلٍ مُّصَفًّى', ('— means:', 'سے مراد ہے:', '— مراد ترې دي:'),
        [('clean water', 'صاف پانی', 'پاکې اوبه'), ('purified honey', 'صاف شہد', 'صاف شات'), ('clean milk', 'صاف دودھ', 'پاکې شیدې'), ('pure wine', 'پاکیزہ شراب', 'پاک شراب')])
    MCQ(b, 5, words(47, 15, 43, 47), ('— according to this, the boiling water will cut the people of Hell\'s:', 'کی رو سے کھولتا ہوا پانی اہلِ جہنم کی کاٹ کر رکھ دے گا:', '— له دې سره سم ایشېدلې اوبه به د دوزخیانو ټوټې کړي:'),
        [('tongue', 'زبان', 'ژبه'), ('legs', 'ٹانگ', 'لنګي'), ('nose', 'ناک', 'پوزه'), ('intestines', 'آنتیں', 'کولمې')])
    MCQ(b, 6, words(47, 35, 1, 2), ('— in this the Muslims have been instructed:', 'میں مسلمانوں کو ہدایت ہے:', '— په دې کې مسلمانانو ته لارښوونه ده:'),
        [('do not differ', 'اختلاف نہ کرو', 'اختلاف مه کوئ'), ('do not lose courage', 'ہمت نہ ہارو', 'همت مه بایلئ'), ('do not grieve', 'غم نہ کھاؤ', 'غم مه کوئ'), ('do not show your back', 'پیٹھ نہ دکھاؤ', 'شا مه ورګرځوئ')])
    MCQ(b, 7, words(47, 36, 1, 5), ('— according to this the life of this world is:', 'کی رو سے دنیاوی زندگی ہے:', '— له دې سره سم د دنیا ژوند دی:'),
        [('adornment and finery', 'زیب و زینت', 'ښکلا او سینګار'), ('luxury and pleasure', 'عیش و عشرت', 'عیش او عشرت'), ('travel and sightseeing', 'سیر و سیاحت', 'سیل او سفر'), ('play and amusement', 'کھیل و تماشا', 'لوبه او تماشه')])
    b.p(*Q2)
    AR(b, f'(1) {words(47, 1)}', 'According to the verse, whose deeds are wasted?', 'آیت کریمہ کے مطابق کن لوگوں کے اعمال ضائع ہو جاتے ہیں؟', 'د آیت له مخې د کومو خلکو عملونه ضایع کېږي؟')
    AR(b, f'(2) {words(47, 4, 7, 20)}', 'According to the verse, what treatment of prisoners has been commanded?', 'آیت کریمہ کی رو سے قیدیوں کے ساتھ کس سلوک کا حکم ہے؟', 'د آیت له مخې له بندیانو سره د کوم چلند حکم دی؟')
    AR(b, f'(3) {words(47, 13, 11, 14)}', 'According to the verse, what was the end of the disobedient towns?', 'آیت کریمہ کی رو سے نافرمان بستیوں کا کیا انجام ہوا؟', 'د آیت له مخې د نافرمانو کلیو پایله څه شوه؟')
    AR(b, f'(4) {words(47, 20, 21, 30)}', 'What condition of the hypocrites at the command of jihad has been stated in the verse?', 'آیت کریمہ میں جہاد کے حکم پر منافقین کی کیا کیفیت بیان ہوئی ہے؟', 'په آیت کې د جهاد پر حکم د منافقانو کوم حالت بیان شوی؟')
    AR(b, f'(5) {words(47, 29)}', 'Which assumption of the hypocrites is mentioned in the verse?', 'آیت کریمہ میں منافقین کے کس گمان کا ذکر ہے؟', 'په آیت کې د منافقانو د کوم ګومان یادونه ده؟')
    AR(b, f'(6) {words(47, 38, 8, 17)}', 'What has been told in the verse about those who are miserly?', 'آیت کریمہ میں بخل کرنے والوں کے حوالے سے کیا بتایا گیا ہے؟', 'په آیت کې د بخل کوونکو په اړه څه ویل شوي؟')
    AR(b, f'(7) {words(47, 38, 24, 32)}', 'What warning has been given in the verse to those who turn away from the divine command?', 'آیت کریمہ میں حکمِ الٰہی سے منہ پھیرنے والوں کو کیا تنبیہ دی گئی ہے؟', 'په آیت کې له الهي حکم مخ اړوونکو ته کوم خبرداری ورکړل شوی؟')
    BOOK.save(155, [(15, rec(b, 15, 155, 155, kind='exercise'))], issues=[{'id': 'mq12-pdf155', 'unit': 15, 'printedPage': 152,
               'description': 'Q1 Arabic quotations printed in very faint blue; matched to the verses. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p155()
