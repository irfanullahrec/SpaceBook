"""Mutalia-e-Quran XII PDF146: p.143 — Lesson 14 vocabulary; exercise Q1 items 1–6. Run: python class12_quran_page146.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('لِتُنْذِرَ', 'So that you may warn', 'تاکہ آپ ڈرائیں', 'تر څو ووېروئ'),
    ('حَوْلَهَا', 'Around it', 'اس کے آس پاس', 'د هغې شاوخوا'),
    ('أَزْوَاجًا', 'Pairs', 'جوڑے', 'جوړې'),
    ('شَرَعَ', 'He ordained (a way)', 'اس نے طریقہ مقرر کیا', 'طریقه یې وټاکله'),
    ('أَقِيمُوا الدِّينَ', 'Establish the religion', 'تم دین کو قائم کرو', 'دین قائم کړئ'),
    ('لَا تَتَفَرَّقُوا', 'Do not be divided', 'تم تفرقہ نہ ڈالو', 'تفرقه مه اچوئ'),
    ('يُنِيبُ', 'He turns (to Allah)', 'وہ رجوع کرتا ہے', 'رجوع کوي'),
    ('أُمِرْتُ', 'I have been commanded', 'مجھے حکم دیا گیا ہے', 'ماته حکم شوی'),
    ('حَرْثَ الْآخِرَةِ', 'The tillage of the Hereafter', 'آخرت کی کھیتی', 'د آخرت کښت'),
    ('الْجَوَارِ', 'Ships', 'جہاز', 'بېړۍ'),
    ('كَالْأَعْلَامِ', 'Like mountains', 'پہاڑوں جیسے', 'د غرونو په څېر'),
    ('يَجْتَنِبُونَ', 'They avoid', 'وہ بچتے ہیں', 'ډډه کوي'),
    ('كَبَائِرَ الْإِثْمِ', 'Great sins', 'بڑے بڑے گناہ', 'لویې لویې ګناهونه'),
    ('شُورَىٰ', 'Consultation', 'مشورہ', 'مشوره'),
    ('يَبْغُونَ', 'They rebel', 'وہ سرکشی کرتے ہیں', 'سرکشي کوي'),
    ('عَزْمِ الْأُمُورِ', 'Matters of resolve', 'ہمت کے کام', 'د همت کارونه'),
    ('فَرِحَ', 'He rejoiced', 'وہ خوش ہوا', 'خوشاله شو'),
    ('إِنْ تُصِبْهُمْ سَيِّئَةٌ', 'If an evil befalls them', 'اگر انھیں کوئی برائی پہنچتی ہے', 'که کومه بدي ورته ورسېږي'),
    ('عَقِيمًا', 'Barren, childless', 'بے اولاد', 'بې‌اولاده'),
    ('أَنْ يُكَلِّمَهُ', 'That He should speak to him', 'کہ وہ اس سے کلام کرے', 'چې ورسره خبرې وکړي'),
]


def p146():
    b = Builder()
    VOC(b, 'mq12-l14-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(42, 7, 6, 8), ('— in this the command has been given to warn:', 'میں ڈرانے کا حکم دیا گیا ہے:', '— په دې کې د وېرولو حکم شوی:'),
        [('the people of Makkah', 'اہلِ مکہ کو', 'د مکې خلکو ته'), ('the people of Madinah', 'اہلِ مدینہ کو', 'د مدینې خلکو ته'), ('the people of Ta\'if', 'اہلِ طائف کو', 'د طائف خلکو ته'), ('the people of Yemen', 'اہلِ یمن کو', 'د یمن خلکو ته')])
    MCQ(b, 2, words(42, 11, 10, 12), ('— according to this Allah Almighty made pairs of:', 'کی رو سے اللہ تعالیٰ نے جوڑے بنائے:', '— له دې سره سم الله تعالی جوړې جوړې کړې:'),
        [('birds', 'پرندوں کے', 'د مرغانو'), ('insects', 'حشرات کے', 'د حشراتو'), ('cattle', 'چوپایوں کے', 'د څارویو'), ('beasts of prey', 'درندوں کے', 'د ځناورو')])
    MCQ(b, 3, words(42, 13, 39, 42), ('— according to this Allah Almighty guides to Himself the one:', 'کی رو سے اللہ تعالیٰ اپنی طرف ہدایت دیتا ہے:', '— له دې سره سم الله تعالی خپل لوري ته لارښوونه کوي هغه چا ته:'),
        [('who turns back to Him', 'جو رجوع کرے', 'چې رجوع وکړي'), ('who repents', 'جو توبہ کرے', 'چې توبه وکړي'), ('who is humble', 'جو عاجزی کرے', 'چې عاجزي وکړي'), ('who is generous', 'جو سخاوت کرے', 'چې سخاوت وکړي')])
    MCQ(b, 4, 'حَرْثَ ٱلْءَاخِرَةِ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('the home of the Hereafter', 'آخرت کا گھر', 'د آخرت کور'), ('the reward of the Hereafter', 'آخرت کا اجر', 'د آخرت اجر'), ('the tillage of the Hereafter', 'آخرت کی کھیتی', 'د آخرت کښت'), ('the success of the Hereafter', 'آخرت کی کامیابی', 'د آخرت بریا')])
    MCQ(b, 5, words(42, 32), ('— in this verse, what has been declared a sign:', 'آیت میں نشانی قرار دیا گیا ہے:', '— په دې آیت کې نښه ګرځول شوې:'),
        [('small boats', 'چھوٹی کشتیوں کو', 'وړې کشتۍ'), ('large submarines', 'بڑی آبدوز کو', 'لویې اوبتلونکې بېړۍ'), ('large icebergs', 'بڑے برفانی تودوں کو', 'لوی یخي غونډۍ'), ('mountain-like ships of the sea', 'پہاڑوں جیسے بحری جہازوں کو', 'د غرونو په څېر سمندري بېړۍ')])
    MCQ(b, 6, words(42, 38, 6, 8), ('— according to this the affairs of the people of faith are settled by:', 'کے مطابق اہلِ ایمان کے معاملات طے ہوتے ہیں:', '— له دې سره سم د مؤمنانو چارې پرېکړه کېږي:'),
        [('silence', 'خاموشی سے', 'په چوپتیا'), ('love', 'محبت سے', 'په مینه'), ('recommendation', 'سفارش سے', 'په سپارښتنه'), ('consultation', 'مشورے سے', 'په مشوره')])
    BOOK.save(146, [(14, rec(b, 14, 146, 146, kind='exercise'))], issues=[{'id': 'mq12-pdf146', 'unit': 14, 'printedPage': 143,
               'description': 'Four-column vocabulary rendered as one two-column table (20 rows). Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p146()
