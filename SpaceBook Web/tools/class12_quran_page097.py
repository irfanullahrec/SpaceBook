"""Mutalia-e-Quran XII PDF97: p.94 — Lesson 9 exercise Q1, Q2 items 1–6. Run: python class12_quran_page097.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words


def p97():
    b = Builder()
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(24, 2, 1, 8), ('— in it the punishment fixed for the unmarried adulterous man and woman is:', 'میں غیر شادی شدہ زانی مرد و عورت کی سزا مقرر کی گئی ہے:', '— په دې کې د نا واده شوي زاني نارینه او ښځې سزا ټاکل شوې:'),
        [('lashes', 'کوڑے', 'دُرې'), ('imprisonment', 'قید', 'بند'), ('exile', 'جلاوطنی', 'جلاوطني'), ('the gallows', 'سولی', 'دار')])
    MCQ(b, 2, words(24, 4, 10, 11), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('eighty spears', 'اسی نیزے', 'اتیا نېزې'), ('eighty lashes', 'اسی کوڑے', 'اتیا دُرې'), ('eighty wounds', 'اسی زخم', 'اتیا ټپونه'), ('eighty prisoners', 'اسی قیدی', 'اتیا بندیان')])
    MCQ(b, 3, 'إِفْكٌ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('envy', 'حسد', 'حسد'), ('backbiting', 'غیبت', 'غیبت'), ('hatred', 'بغض', 'کینه'), ('slander', 'بہتان', 'بهتان')])
    MCQ(b, 4, words(24, 27, 9, 10), ('— in the verse the etiquette of entering someone\'s house stated is:', 'آیت کریمہ میں کسی کے گھر میں داخل ہونے کا ادب بیان ہوا:', '— په آیت کې د چا کور ته د ننوتلو کوم ادب بیان شوی:'),
        [('seeking permission', 'اجازت لینا', 'اجازه اخیستل'), ('greeting with salam', 'سلام کرنا', 'سلام اچول'), ('lowering the gaze', 'نظر نیچی رکھنا', 'سترګې ټیټې ساتل'), ('lowering the voice', 'آواز پست رکھنا', 'غږ ټیټ ساتل')])
    MCQ(b, 5, words(24, 31, 16, 19), ('— in it the believing women have been commanded to draw their veils:', 'میں مومن خواتین کو اوڑھنیاں ڈالنے کا حکم دیا گیا ہے:', '— په دې کې مؤمنو ښځو ته د ټکریو اچولو حکم شوی:'),
        [('over their feet', 'اپنے پاؤں پر', 'پر خپلو پښو'), ('over their bosoms', 'اپنے گریبانوں پر', 'پر خپلو ګرېوانونو'), ('over their necks', 'اپنی گردنوں پر', 'پر خپلو غاړو'), ('over their hands', 'اپنے ہاتھوں پر', 'پر خپلو لاسونو')])
    MCQ(b, 6, 'ٱلتَّٰبِعِينَ غَيْرِ أُو۟لِى ٱلْإِرْبَةِ مِنَ ٱلرِّجَالِ', ('— this refers to such servants as do not have:', 'سے مراد ایسے خدمت گار ہیں جو نہیں رکھتے:', '— له دې څخه مراد داسې خدمتګاران دي چې نه لري:'),
        [('wealth', 'مال', 'مال'), ('strength', 'طاقت', 'ځواک'), ('reason', 'عقل', 'عقل'), ('sexual desire', 'جنسی خواہش', 'جنسي غوښتنه')])
    MCQ(b, 7, 'ٱلْأَيَٰمَىٰ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('divorced', 'طلاق یافتہ', 'طلاقې'), ('married', 'شادی شدہ', 'واده شوي'), ('widows', 'بیوہ', 'کونډې'), ('unmarried', 'بے نکاح', 'بې‌نکاحه')])
    b.p(*Q2)
    AR(b, f'(1) {words(24, 1)}', 'What has been told about Surah al-Nur in the verse?', 'آیت کریمہ میں سورۃ النور کے متعلق کیا بتایا گیا ہے؟', 'په آیت کې د سورة النور په اړه څه ویل شوي؟')
    AR(b, f'(2) {words(24, 2, 10, 22)}', 'Of what has warning been given in the verse at the time of carrying out the hadd on the adulterer and the adulteress?', 'آیت کریمہ میں زانی اور زانیہ پر حد جاری کرتے وقت کس بات کی تنبیہ کی گئی ہے؟', 'په آیت کې پر زاني او زانیې د حد د پلي کولو پر مهال د کومې خبرې خبرداری شوی؟')
    AR(b, f'(3) {words(24, 4, 1, 16)}', 'What has been commanded in the verse about those who slander chaste women?', 'آیت کریمہ میں پاک دامن عورتوں پر بہتان لگانے والوں کے بارے میں کیا حکم دیا گیا ہے؟', 'په آیت کې پر پاکلمنو ښځو د بهتان لګوونکو په اړه څه حکم شوی؟')
    AR(b, f'(4) {words(24, 11, 26, 32)}', 'What end of the slanderers has been stated in the verse?', 'آیت کریمہ میں بہتان لگانے والوں کا کیا انجام بیان ہوا ہے؟', 'په آیت کې د بهتان لګوونکو کومه پایله بیان شوې؟')
    AR(b, f'(5) {words(24, 21, 10, 17)}', 'According to the verse, to what does Satan command his followers?', 'آیت کریمہ کے مطابق شیطان اپنے پیروکاروں کو کس چیز کا حکم دیتا ہے؟', 'د آیت له مخې شیطان خپلو پیروانو ته د څه حکم کوي؟')
    AR(b, f'(6) {words(24, 30, 1, 11)}', 'What guidance has been given to believing men in the verse?', 'آیت کریمہ میں مومن مردوں کو کیا ہدایت دی گئی؟', 'په آیت کې مؤمنو نارینه وو ته څه لارښوونه شوې؟')
    BOOK.save(97, [(9, rec(b, 9, 97, 97, kind='exercise'))], issues=[{'id': 'mq12-pdf097', 'unit': 9, 'printedPage': 94,
               'description': 'Quoted verses drawn from the reference Uthmani text. No printed key. Faint first lines of the scan read with care.'}])


if __name__ == '__main__':
    p97()
