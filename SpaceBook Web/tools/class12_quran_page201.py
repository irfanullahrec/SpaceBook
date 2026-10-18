"""Mutalia-e-Quran XII PDF201: p.198 — Lesson 21 vocabulary (end); exercise Q1. Run: python class12_quran_page201.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, Q1, words

VOCAB = [
    ('يَفْصِلُ', 'He will decide', 'وہ فیصلہ کرے گا', 'پرېکړه به وکړي'),
    ('بُرَآءُ', 'Free of, disowning', 'بیزار', 'بېزاره'),
    ('عَادَيْتُمْ', 'You hold as enemies', 'تم دشمنی رکھتے ہو', 'دښمني لرئ'),
    ('لَا يَنْهَاكُمُ اللَّهُ', 'Allah does not forbid you', 'اللہ تمھیں منع نہیں کرتا', 'الله تاسو نه منع کوي'),
    ('تَبَرُّوهُمْ', 'You deal kindly with them', 'تم ان سے بھلائی کا سلوک کرو', 'ورسره ښه چلند وکړئ'),
    ('تُقْسِطُوا', 'You deal justly', 'تم انصاف کا برتاؤ کرو', 'انصاف وکړئ'),
    ('مُهَاجِرَاتٍ', 'Emigrant women', 'ہجرت کرنے والی عورتیں', 'هجرت کوونکې ښځې'),
    ('فَامْتَحِنُوهُنَّ', 'Then test them', 'تو تم ان کا امتحان لیا کرو', 'نو د هغوی ازموینه وکړئ'),
    ('فَإِنْ عَلِمْتُمُوهُنَّ', 'Then if you know them', 'پھر اگر وہ تمھیں معلوم ہو جائیں', 'بیا که درته معلومې شي'),
    ('فَلَا تَرْجِعُوهُنَّ', 'Then do not return them', 'تو انھیں واپس نہ بھیجو', 'نو بېرته یې مه لېږئ'),
    ('الْكَوَافِرِ', 'Disbelieving women', 'کافر عورتیں', 'کافرې ښځې'),
    ('إِنْ فَاتَكُمْ', 'If (one) slips away from you', 'اگر وہ تم سے چلی جائے', 'که له تاسو لاړه شي'),
    ('فَعَاقَبْتُمْ', 'Then your turn comes', 'پھر تمھاری باری آ جائے', 'بیا ستاسو وار راشي'),
    ('لَا يَسْرِقْنَ', 'They will not steal', 'وہ چوری نہیں کریں گی', 'غلا به نه کوي'),
]


def p201():
    b = Builder()
    b.table('mq12-l21-vocab-2', ['Word', 'Meaning'], [[w, e] for w, e, u, p in VOCAB], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in VOCAB], [[w, p] for w, e, u, p in VOCAB])
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(60, 1, 1, 8), ('— in this Allah Almighty has forbidden the people of faith to make their own and His enemies:', 'میں اللہ تعالیٰ نے اہلِ ایمان کو اپنے اور ان کے دشمنوں کو بنانے سے منع فرمایا ہے:', '— په دې کې الله تعالی مؤمنان له دې منع کړي چې خپل او د هغه دښمنان ونیسي:'),
        [('well-wishers', 'خیر خواہ', 'خیرغوښتونکي'), ('relatives', 'رشتہ دار', 'خپلوان'), ('advisers', 'مشیر', 'سلاکاران'), ('friends', 'دوست', 'دوستان')])
    MCQ(b, 2, 'يَثْقَفُوكُمْ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('they imprison you', 'تمھیں قید کر دیں', 'تاسو بندي کړي'), ('they gain control over you', 'تمھیں یرغمال بنا لیں', 'تاسو یرغمل کړي'), ('they exile you', 'تمھیں جلاوطن کر دیں', 'تاسو جلاوطنه کړي'), ('they crucify you', 'تمھیں سولی چڑھا دیں', 'تاسو دار ته وخېژوي')])
    MCQ(b, 3, words(60, 3, 1, 8), ('— according to this, on the Day of Resurrection, besides your children, what will never benefit you is your:', 'کی رو سے قیامت کے دن تمھیں ہرگز نفع نہ دیں گی تمھاری اولاد اور تمھاری:', '— له دې سره سم د قیامت په ورځ به تاسو ته هېڅکله ګټه ونه رسوي ستاسو اولاد او ستاسو:'),
        [('friendships', 'دوستیاں', 'دوستۍ'), ('relationships', 'تعلق داریاں', 'اړیکې'), ('kinship ties', 'رشتہ داریاں', 'خپلولۍ'), ('partisanships', 'طرف داریاں', 'پلوي')])
    MCQ(b, 4, words(60, 4, 13, 20), ('— according to this, Sayyiduna Ibrahim (peace be upon him) and his companions declared to the nation and their false gods:', 'کے مطابق سیدنا ابراہیم علیہ السلام اور ان کے ساتھیوں نے قوم اور ان کے باطل معبودوں سے اعلان کیا:', '— له دې سره سم سیدنا ابراهیم علیه السلام او د هغه ملګرو قوم او د هغوی باطلو معبودانو ته اعلان وکړ:'),
        [('of opposition', 'مخالفت کا', 'د مخالفت'), ('of condemnation', 'مذمت کا', 'د غندنې'), ('of enmity', 'دشمنی کا', 'د دښمنۍ'), ('of disavowal', 'بیزاری کا', 'د بېزارۍ')])
    MCQ(b, 5, words(60, 10, 1, 8), ('— in this, concerning believing emigrant women, the command is:', 'میں مومنین کو ہجرت کرنے والی مومن خواتین کے بارے میں حکم ہے:', '— په دې کې مؤمنانو ته د هجرت کوونکو مؤمنو ښځو په اړه حکم دی:'),
        [('to teach them', 'تعلیم دینے کا', 'د ښوونې'), ('to protect them', 'حفاظت کرنے کا', 'د ساتنې'), ('to test them', 'امتحان لینے کا', 'د ازموینې'), ('to send them back', 'واپس بھیجنے کا', 'د بېرته لېږلو')])
    MCQ(b, 6, words(60, 10, 44, 47), ('— in this, concerning disbelieving women, the Muslims have been taught:', 'میں مسلمانوں کو کافر عورتوں کے بارے میں تعلیم دی گئی:', '— په دې کې مسلمانانو ته د کافرو ښځو په اړه لارښوونه شوې:'),
        [('do not divorce them', 'انھیں طلاق نہ دو', 'طلاق مه ورکوئ'), ('do not give them their dower', 'انھیں ان کے مہر نہ دو', 'مهرونه یې مه ورکوئ'), ('do not exile them', 'انھیں جلاوطن نہ کرو', 'جلاوطنه یې مه کوئ'), ('do not keep them in marriage', 'انھیں نکاح میں نہ روکے رکھو', 'په نکاح کې یې مه ساتئ')])
    MCQ(b, 7, 'لَا يَسْرِقْنَ', ('— means:', 'سے مراد ہے:', '— مراد ترې ده:'),
        [('they will not associate partners', 'وہ شرک نہیں کریں گی', 'شرک به نه کوي'), ('they will not bring slander', 'وہ بہتان نہیں لائیں گی', 'بهتان به نه راوړي'), ('they will not steal', 'وہ چوری نہیں کریں گی', 'غلا به نه کوي'), ('they will not disobey', 'وہ نافرمانی نہیں کریں گی', 'نافرماني به نه کوي')])
    BOOK.save(201, [(21, rec(b, 21, 201, 201, kind='exercise'))], issues=[{'id': 'mq12-pdf201', 'unit': 21, 'printedPage': 198,
               'description': 'Last fourteen vocabulary rows (continued from p.197) rendered as a continuation table. Q1 Arabic quotations printed in very faint blue; matched to the verses. MCQ 2 option ب prints "تمھیں یرغمال بنا لیں" (kept). No printed key.'}])


if __name__ == '__main__':
    p201()
