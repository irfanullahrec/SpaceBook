"""Mutalia-e-Quran XII PDF218: p.215 — Lesson 23 exercise Q1 items 2–8, Q2. Run: python class12_quran_page218.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, words


def p218():
    b = Builder()
    MCQ(b, 2, words(63, 2, 1, 3), ('— according to this the hypocrites have made a shield of:', 'کی رو سے منافقین نے ڈھال بنا رکھا ہے:', '— له دې سره سم منافقانو ډال ګرځولي:'),
        [('their innocence', 'اپنی معصومیت کو', 'خپل معصومیت'), ('their wealth', 'اپنے مال کو', 'خپل مال'), ('their connections', 'اپنے تعلقات کو', 'خپلې اړیکې'), ('their oaths', 'اپنی قسموں کو', 'خپل قسمونه')])
    MCQ(b, 3, words(63, 3, 6, 8), ('— according to this, on the hearts of the hypocrites has been placed:', 'کی رو سے منافقین کے دلوں پر لگا دی گئی ہے:', '— له دې سره سم د منافقانو پر زړونو لګول شوې:'),
        [('blackness', 'سیاہی', 'تورتیا'), ('an obstruction', 'رکاوٹ', 'خنډ'), ('a seal', 'مہر', 'مهر'), ('a knot', 'گرہ', 'غوټه')])
    MCQ(b, 4, words(63, 4, 12, 14), ('— in this the bodies of the hypocrites have been likened to:', 'میں منافقین کے اجسام کو تشبیہ دی گئی ہے:', '— په دې کې د منافقانو بدنونه تشبیه شوي:'),
        [('dry wood', 'خشک لکڑی سے', 'له وچ لرګي'), ('wet wood', 'گیلی لکڑی سے', 'له لوند لرګي'), ('strong wood', 'مضبوط لکڑی سے', 'له ټینګ لرګي'), ('hollow wood', 'کھوکھلی لکڑی سے', 'له تش لرګي')])
    MCQ(b, 5, 'تُعْلِنُونَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('you conceal', 'تم چھپاتے ہو', 'پټوئ'), ('you make public', 'تم ظاہر کرتے ہو', 'ښکاره کوئ'), ('you spread', 'تم نشر کرتے ہو', 'خپروئ'), ('you overlook', 'تم درگزر کرتے ہو', 'تېرېږئ')])
    MCQ(b, 6, 'يَوْمُ ٱلتَّغَابُنِ', ('— means:', 'کا مطلب ہے:', '— مطلب یې دی:'),
        [('the day of regret', 'پچھتاوے کا دن', 'د پښېمانۍ ورځ'), ('the day of celebration', 'جشن کا دن', 'د جشن ورځ'), ('the day of loss and gain', 'ہار اور جیت کا دن', 'د ګټې او بایلنې ورځ'), ('the day of sorrow', 'افسوس کا دن', 'د افسوس ورځ')])
    MCQ(b, 7, words(64, 12, 8, 12), ('— according to this, the responsibility of the Messenger of Allah (peace and blessings of Allah be upon him) is clearly:', 'کی رو سے رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے ذمے ہے واضح طور پر:', '— له دې سره سم د رسول الله صلی الله علیه وعلی آله واصحابه وسلم پر غاړه په ښکاره ډول:'),
        [('giving glad tidings', 'خوش خبری دینا', 'زېری ورکول'), ('warning', 'ڈرانا', 'وېرول'), ('conveying the message', 'پیغام پہنچانا', 'پیغام رسول'), ('making (people) accept', 'منوانا', 'منل ورکول')])
    MCQ(b, 8, words(64, 15, 1, 4), ('— in this wealth and children have been declared:', 'میں مال اور اولاد کو قرار دیا:', '— په دې کې مال او اولاد ګرځول شوي:'),
        [('a trial', 'آزمائش', 'ازموینه'), ('a reward', 'انعام', 'انعام'), ('a helper', 'مددگار', 'مرستندوی'), ('a burden', 'بوجھ', 'بار')])
    b.p(*Q2)
    AR(b, f'(1) {words(63, 1, 1, 8)}', 'According to the verse, what did the hypocrites testify on coming to the Holy Prophet (peace and blessings of Allah be upon him)?', 'آیت کریمہ کے مطابق منافقین نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے پاس آ کر کیا گواہی دیتے تھے؟', 'د آیت له مخې منافقانو به نبي کریم صلی الله علیه وعلی آله واصحابه وسلم ته راتلل نو څه شاهدي به یې ورکوله؟')
    AR(b, f'(2) {words(63, 4, 21, 23)}', 'What warning has been given in the verse concerning the hypocrites?', 'آیت کریمہ میں منافقین کے حوالے سے کیا تنبیہ کی گئی ہے؟', 'په آیت کې د منافقانو په اړه کوم خبرداری شوی؟')
    AR(b, f'(3) {words(63, 6)}', 'What deprivation of the hypocrites has been stated in the verse?', 'آیت کریمہ میں منافقین کی کیا محرومی بیان کی گئی ہے؟', 'په آیت کې د منافقانو کومه بې‌برخې کېدنه بیان شوې؟')
    AR(b, f'(4) {words(63, 9)}', 'What advice has been given in the verse to the people of faith concerning wealth and children?', 'آیت کریمہ میں اہلِ ایمان کو مال و اولاد کے حوالے سے کیا نصیحت کی گئی ہے؟', 'په آیت کې مؤمنانو ته د مال او اولاد په اړه څه نصیحت شوی؟')
    AR(b, f'(5) {words(64, 4)}', 'What glory of the knowledge of Allah Almighty has been stated in the verse?', 'آیت کریمہ میں اللہ تعالیٰ کے علم کی کیا شان بیان کی گئی ہے؟', 'په آیت کې د الله تعالی د علم کوم شان بیان شوی؟')
    AR(b, f'(6) {words(64, 7, 8, 20)}', 'What has been told in the verse concerning being raised after death?', 'آیت کریمہ میں مرنے کے بعد اٹھائے جانے کے حوالے سے کیا بتایا گیا ہے؟', 'په آیت کې له مرګ وروسته د راپاڅولو په اړه څه ویل شوي؟')
    AR(b, f'(7) {words(64, 16, 1, 9)}', 'What guidance has been given to the people of faith in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کیا ہدایات دی گئی ہیں؟', 'په آیت کې مؤمنانو ته کومې لارښوونې شوې؟')
    AR(b, f'(8) {words(64, 17)}', 'In the verse, of which rewards of Allah Almighty for giving qard hasan is mention made?', 'آیت میں اللہ تعالیٰ کو قرضِ حسنہ دینے پر کن انعامات کا ذکر ہے؟', 'په آیت کې الله تعالی ته د ښه پور ورکولو لپاره د کومو انعامونو یادونه ده؟')
    BOOK.save(218, [(23, rec(b, 23, 218, 218, kind='exercise'))], issues=[{'id': 'mq12-pdf218', 'unit': 23, 'printedPage': 215,
               'description': 'Q1 Arabic quotations printed in faint blue; matched to the verses. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p218()
