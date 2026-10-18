"""Mutalia-e-Quran XII PDF115: p.112 — Lesson 11 exercise Q1, Q2 items 1–4. Run: python class12_quran_page115.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words


def p115():
    b = Builder()
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(33, 2, 1, 6), ('— in it the Holy Prophet (peace and blessings of Allah be upon him) has been commanded, concerning the revelation, with:', 'میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو وحی کے متعلق فرمایا گیا ہے:', '— په دې کې نبي کریم صلی الله علیه وعلی آله واصحابه وسلم ته د وحې په اړه ویل شوي:'),
        [('writing it', 'لکھنے کا', 'د لیکلو'), ('remembering it', 'یاد کرنے کا', 'د یادولو'), ('following it', 'پیروی کا', 'د پیروۍ'), ('stating it', 'بیان کرنے کا', 'د بیانولو')])
    MCQ(b, 2, words(33, 6, 1, 5), ('— according to this the Holy Prophet (peace and blessings of Allah be upon him) has more right over the people of faith than their:', 'کی رو سے نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم اہلِ ایمان پر زیادہ حق رکھتے ہیں ان کی:', '— له دې سره سم نبي کریم صلی الله علیه وعلی آله واصحابه وسلم پر مؤمنانو تر دې ډېر حق لري:'),
        [('selves', 'جانوں سے', 'له ځانونو'), ('wealth', 'دولت سے', 'له شتمنۍ'), ('trade', 'تجارت سے', 'له سوداګرۍ'), ('kinsfolk', 'برادری سے', 'له قبیلې')])
    MCQ(b, 3, words(33, 13, 16, 19), ('— according to this a group was seeking permission from the Holy Prophet (peace and blessings of Allah be upon him) saying that our houses are:', 'کے مطابق ایک گروہ نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم سے یہ کہتے ہوئے اجازت مانگ رہا تھا کہ ہمارے گھر ہیں:', '— له دې سره سم یوې ډلې له نبي کریم صلی الله علیه وعلی آله واصحابه وسلم دا وایي اجازه غوښته چې زموږ کورونه دي:'),
        [('very far', 'بہت دور', 'ډېر لرې'), ('unbaked (kacha)', 'کچے', 'خامه'), ('unprotected', 'غیر محفوظ', 'ناخوندي'), ('dilapidated', 'بوسیدہ', 'زاړه')])
    MCQ(b, 4, words(33, 9, 11, 13), ('— according to this Allah Almighty helped in the battle of Ahzab:', 'کی رو سے اللہ تعالیٰ نے غزوۂ احزاب میں مدد کی:', '— له دې سره سم الله تعالی د احزابو په غزا کې مرسته وکړه:'),
        [('with a strong wind', 'تیز آندھی سے', 'په تېز توپان'), ('with angels', 'فرشتوں سے', 'په پرښتو'), ('with rain', 'بارش سے', 'په باران'), ('with armies', 'لشکروں سے', 'په لښکرو')])
    MCQ(b, 5, words(33, 19, 1, 2), ('— according to this the conduct of the hypocrites stated is:', 'کی رو سے منافقین کی روش بیان ہوئی ہے:', '— له دې سره سم د منافقانو کوم چلند بیان شوی:'),
        [('very miserly', 'سخت بخیل', 'ډېر بخیل'), ('cowardly', 'بزدل', 'بزدل'), ('conspiring', 'سازشی', 'دسیسه‌باز'), ('deceitful', 'مکار', 'چل‌باز')])
    MCQ(b, 6, words(33, 26, 15, 16), ('— means that one group you:', 'سے مراد ہے کہ ایک گروہ کو:', '— مراد دا ده چې یوه ډله مو:'),
        [('killed', 'قتل کیا', 'ووژله'), ('exiled', 'جلاوطن کیا', 'جلاوطنه کړه'), ('made captives', 'قیدی بنایا', 'بندي کړه'), ('forgave', 'معاف کیا', 'وبښله')])
    MCQ(b, 7, words(33, 32, 10, 12), ('— in it Allah Almighty instructed the Mothers of the Believers (may Allah be pleased with them):', 'میں امہات المومنین رضی اللہ تعالیٰ عنہن کو اللہ تعالیٰ نے تلقین کی:', '— په دې کې الله تعالی امهات المؤمنین رضي الله عنهن ته لارښوونه وکړه:'),
        [('not to speak softly with non-mahrams', 'نامحرم سے نرمی سے بات نہ کرنے کی', 'له نامحرم سره په نرمۍ خبرې نه کول'), ('to stay in their homes', 'گھروں میں ٹھہری رہنے کی', 'په کورونو کې پاتې کېدل'), ('not to display adornment', 'زینت کی نمائش نہ کرنے کی', 'د ښکلا نندارې نه کول'), ('to remember the verses of Allah Almighty', 'اللہ تعالیٰ کی آیات یاد رکھنے کی', 'د الله تعالی آیتونه یادول')])
    b.p(*Q2)
    AR(b, f'(1) {words(33, 1)}', 'What has the Holy Prophet (peace and blessings of Allah be upon him) been instructed in the verse?', 'آیت کریمہ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو کیا تلقین فرمائی گئی ہے؟', 'په آیت کې نبي کریم صلی الله علیه وعلی آله واصحابه وسلم ته څه لارښوونه شوې؟')
    AR(b, f'(2) {words(33, 4, 18, 32)}', 'What has been said in the verse concerning adopted sons?', 'آیت کریمہ میں منہ بولے بیٹوں کے حوالے سے کیا فرمایا گیا ہے؟', 'په آیت کې د خوله‌ویلو زامنو په اړه څه فرمایل شوي؟')
    AR(b, f'(3) {words(33, 10)}', 'Of what trial of the people of faith during the war is mention made in the verse?', 'آیت کریمہ میں جنگ کے دوران اہلِ ایمان کی کس آزمائش کا ذکر ہے؟', 'په آیت کې د جګړې پر مهال د مؤمنانو د کومې ازموینې یادونه ده؟')
    AR(b, f'(4) {words(33, 16)}', 'According to the verse, how have the hypocrites been warned about fleeing from death?', 'آیت کریمہ کے مطابق منافقین کو موت سے فرار ہونے پر کیسے خبردار کیا گیا ہے؟', 'د آیت له مخې منافقان له مرګه د تېښتې په اړه څنګه خبردار شوي؟')
    BOOK.save(115, [(11, rec(b, 11, 115, 115, kind='exercise'))], issues=[{'id': 'mq12-pdf115', 'unit': 11, 'printedPage': 112,
               'description': 'The Arabic quotations of Q1 are printed in very faint blue; read with contrast and matched to the verses (MCQ 6 read as وَتَأْسِرُونَ فَرِيقًا, 33:26). Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p115()
