"""Mutalia-e-Quran XII PDF135: p.132 — Lesson 13 vocabulary; exercise Q1 items 1–5. Run: python class12_quran_page135.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('أَكِنَّةٍ', 'Coverings, veils', 'پردے', 'پردې'),
    ('وَقْرٌ', 'Heaviness (deafness)', 'بوجھ', 'درنښت'),
    ('وَيْلٌ', 'Woe, ruin', 'ہلاکت', 'هلاکت'),
    ('أَنْذَرْتُكُمْ', 'I warn you', 'میں تمھیں ڈراتا ہوں', 'تاسو وېروم'),
    ('صَرْصَرًا', 'A furious wind', 'تیز آندھی', 'تېز توپان'),
    ('أَيَّامٍ نَحِسَاتٍ', 'Days of ill-omen', 'نحوست کے دن', 'شومې ورځې'),
    ('تَسْتَتِرُونَ', 'You used to hide (screen yourselves)', 'تم پردہ کرتے تھے', 'تاسو پرده کوله'),
    ('لَا تَسْمَعُوا', 'Do not listen', 'تم مت سنو', 'مه اورئ'),
    ('وَالْغَوْا', 'And make noise', 'اور تم شور مچاؤ', 'او شور جوړ کړئ'),
    ('ثُمَّ اسْتَقَامُوا', 'Then they remained steadfast', 'پھر وہ قائم رہے / پھر انھوں نے استقامت اختیار کی', 'بیا ټینګ پاتې شول / بیا یې استقامت غوره کړ'),
    ('أَلَّا تَخَافُوا', 'That you should not fear', 'کہ تم خوف نہ کرو', 'چې مه وېرېږئ'),
    ('لَا تَحْزَنُوا', 'Do not grieve', 'تم غم نہ کرو', 'خپه مه کېږئ'),
    ('ادْفَعْ', 'Repel', 'تم دفع کرو', 'لرې یې کړه'),
    ('فَاسْتَعِذْ', 'Then seek refuge', 'تو تم پناہ مانگ لیا کرو', 'نو پناه وغواړه'),
    ('خَاشِعَةً', 'Lowly, dry and still', 'دبی ہوئی', 'ځپلې'),
    ('بِظَلَّامٍ لِلْعَبِيدِ', 'Unjust to the servants', 'بندوں پر ظلم کرنے والا', 'پر بندګانو ظلم کوونکی'),
    ('مَحِيصٍ', 'Place of escape', 'بھاگنے کی جگہ', 'د تېښتې ځای'),
    ('فَيَئُوسٌ قَنُوطٌ', 'Despairing, hopeless', 'مایوس، ناامید', 'مایوس، ناهیلی'),
    ('نَأَى بِجَانِبِهِ', 'He turned aside', 'اس نے اپنا پہلو پھیر لیا', 'خپل اړخ یې واړاوه'),
    ('دُعَاءٍ عَرِيضٍ', 'Lengthy supplications', 'لمبی چوڑی دعائیں', 'اوږدې پلنې دعاوې'),
]


def p135():
    b = Builder()
    VOC(b, 'mq12-l13-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, '', ('Surah Ha Mim al-Sajdah is one of those seven surahs which are called:', 'سُوْرَةُ حٰمٓ السَّجْدَةِ ان سات سورتوں میں سے ہے جو کہلاتی ہیں:', 'سورة حم السجده له هغو اوو سورتونو څخه دی چې ورته ویل کېږي:'),
        [('Musabbihat', 'مُسَبِّحَات', 'مسبحات'), ('Mu\'awwidhatayn', 'مُعَوِّذَتَيْن', 'معوذتین'), ('al-Zahrawayn', 'اَلزَّهْرَاوَيْن', 'الزهراوین'), ('Hawamim', 'حَوَامِيْم', 'حوامیم')])
    MCQ(b, 2, 'وَيْلٌ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('end', 'انجام', 'پایله'), ('warning', 'وعید', 'ګواښ'), ('ruin', 'ہلاکت', 'هلاکت'), ('recompense', 'بدلہ', 'بدله')])
    MCQ(b, 3, words(41, 34, 7, 10), ('— in this the command has been given to repel evil with:', 'میں دفع کرنے کا حکم دیا گیا ہے بدی کو:', '— په دې کې د بدۍ د لرې کولو حکم شوی:'),
        [('harshness', 'سختی سے', 'په سختۍ'), ('patience', 'صبر سے', 'په صبر'), ('goodness', 'نیکی سے', 'په ښېګڼه'), ('wisdom', 'حکمت سے', 'په حکمت')])
    MCQ(b, 4, words(41, 36, 6, 7), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('then seek refuge with Allah', 'تو اللہ کی پناہ مانگ لیا کرو', 'نو د الله پناه وغواړه'), ('then supplicate to Allah', 'تو اللہ سے دعا مانگ لیا کرو', 'نو له الله دعا وغواړه'), ('then ask Allah for help', 'تو اللہ کی مدد مانگ لیا کرو', 'نو د الله مرسته وغواړه'), ('then ask Allah for mercy', 'تو اللہ کی رحمت مانگ لیا کرو', 'نو د الله رحمت وغواړه')])
    MCQ(b, 5, words(41, 44, 23, 25), ('— according to this, in the ears of the polytheists there is:', 'کی رو سے مشرکوں کے کانوں میں ہے:', '— له دې سره سم د مشرکانو په غوږونو کې دي:'),
        [('a defect', 'خرابی', 'خرابي'), ('heaviness', 'بوجھ', 'درنښت'), ('a disease', 'بیماری', 'ناروغي'), ('deafness', 'بہرہ پن', 'کوڼوالی')])
    BOOK.save(135, [(13, rec(b, 13, 135, 135, kind='exercise'))], issues=[{'id': 'mq12-pdf135', 'unit': 13, 'printedPage': 132,
               'description': 'Four-column vocabulary rendered as one two-column table (20 rows). Q1 Arabic quotations printed in very faint blue; matched to the verses. No printed key.'}])


if __name__ == '__main__':
    p135()
