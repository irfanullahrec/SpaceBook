"""Mutalia-e-Quran XII PDF114: p.111 — Lesson 11 matters of knowledge and action; vocabulary. Run: python class12_quran_page114.py"""
from class12_quran_common import BOOK, Builder, rec, KA, L, VOC

VOCAB = [
    ('قَلْبَيْنِ', 'Two hearts', 'دو دل', 'دوه زړونه'),
    ('جَوْفِهِ', 'His breast (inside)', 'اُس کا سینہ', 'د هغه سینه'),
    ('مَسْطُورًا', 'Written down', 'لکھا ہوا', 'لیکل شوی'),
    ('مِيثَاقًا', 'Covenant', 'عہد', 'ژمنه'),
    ('غَلِيظًا', 'Firm, solemn', 'پختہ', 'ټینګ'),
    ('أَسْفَلَ', 'Lowest, below', 'سب سے نچلا', 'تر ټولو لاندې'),
    ('زَاغَتِ الْأَبْصَارُ', 'The eyes grew wild (with fear)', 'آنکھیں پتھرا گئیں', 'سترګې ټکانې شوې'),
    ('الْحَنَاجِرَ', 'The throats (hearts in the mouth)', 'دل (کلیجے)', 'زړونه (ځیګرونه)'),
    ('بُيُوتَنَا عَوْرَةٌ', 'Our houses are exposed', 'ہمارے گھر غیر محفوظ ہیں', 'زموږ کورونه ناخوندي دي'),
    ('إِنْ فَرَرْتُمْ', 'If you flee', 'اگر تم بھاگو', 'که وتښتئ'),
    ('لَا تُمَتَّعُونَ', 'You will not enjoy (benefit)', 'تم فائدہ نہ اٹھا سکو گے', 'ګټه به وانه خلئ'),
    ('أَشِحَّةً', 'Very miserly', 'سخت بخیل', 'ډېر بخیلان'),
    ('يَرْجُو اللَّهَ', 'He hopes for (meeting) Allah', 'وہ اللہ سے اُمید رکھتا ہے', 'له الله هیله لري'),
    ('فَلَا تَخْضَعْنَ', 'So do not be soft (in speech)', 'تو تم نرم لہجہ نہ رکھو', 'نو نرمه لهجه مه کوئ'),
    ('وَقَرْنَ', 'And stay', 'اور تم ٹھہری رہو', 'او پاتې شئ'),
    ('تَبَرُّجَ الْجَاهِلِيَّةِ', 'Displaying adornment as in the age of ignorance', 'جاہلیت کی طرح زینت اختیار کرنا', 'د جاهلیت په څېر د ښکلا ښودل'),
]


def p114():
    b = Builder()
    KA(b)
    L(b, [('The dignity of the Pure Wives (may Allah be pleased with them) of the Prophet (peace and blessings of Allah be upon him) is that they hold the sanctity of being mothers for the people of faith.', 'آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی ازواجِ مطہرات رضی اللہ عنہن کی شان یہ ہے کہ وہ اہلِ ایمان کے لیے ماں ہونے کا تقدس رکھتی ہیں۔', 'د هغه صلی الله علیه وعلی آله واصحابه وسلم د پاکو مېرمنو رضي الله عنهن شان دا دی چې هغوی د مؤمنانو لپاره د مور د سپېڅلتیا درجه لري.'),
          ('The Messenger of Allah (peace and blessings of Allah be upon him), with respect to all his sayings, deeds and states, is the best model for all aspects of individual and collective life. The people of faith should keep the pure life of the Prophet (peace and blessings of Allah be upon him) before them in all matters and follow his excellent example.', 'رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم اپنے تمام اقوال، افعال اور احوال کے لحاظ سے زندگی کے انفرادی اور اجتماعی تمام گوشوں کے لیے بہترین نمونہ ہیں۔ اہلِ ایمان کو چاہیے کہ وہ تمام معاملات میں آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی حیاتِ طیبہ کو سامنے رکھیں اور اسوۂ حسنہ کی پیروی کریں۔', 'رسول الله صلی الله علیه وعلی آله واصحابه وسلم د خپلو ټولو ویناوو، کړنو او حالاتو له مخې د ژوند د فردي او ټولنیزو ټولو اړخونو لپاره غوره بېلګه دی. مؤمنان باید په ټولو چارو کې د هغه صلی الله علیه وعلی آله واصحابه وسلم پاک ژوند مخې ته کېږدي او د هغه د غوره اسوې پیروي وکړي.'),
          ('When the people of truth, with the help of Allah Almighty, clash with the people of falsehood, then the wealth and means of the people of falsehood are of no use to them. Allah Almighty creates such means for the people of truth that the spirits of the enemies of Islam are broken, and the doors of victories are opened for the people of faith.', 'اہلِ حق جب اللہ تعالیٰ کی مدد سے اہلِ باطل سے ٹکراتے ہیں تو اہلِ باطل کے مال و اسباب ان کے کچھ کام نہیں آتے۔ اللہ تعالیٰ اہلِ حق کے لیے ایسے اسباب پیدا فرماتا ہے کہ دشمنانِ اسلام کے حوصلے پست ہو جاتے ہیں اور وہ اہلِ ایمان کے لیے فتوحات کے دروازے کھل جاتے ہیں۔', 'کله چې د حق خلک د الله تعالی په مرسته د باطل له خلکو سره ټکر کوي، نو د باطل د خلکو مال او اسباب هېڅ په کار نه ورځي. الله تعالی د حق د خلکو لپاره داسې اسباب پیدا کوي چې د اسلام د دښمنانو حوصلې ماتې شي او د مؤمنانو لپاره د بریاوو دروازې پرانیستل شي.'),
          ('For a woman to protect her chastity it is also necessary that, while speaking with a non-mahram, she speaks with her tongue with a degree of firmness in tone and seriousness; further, she should not speak in such an informal manner from which any kind of wrong expectations arise in anyone\'s heart.', 'ایک خاتون کو اپنی عفت کی حفاظت کے لیے یہ بھی ضروری ہے کہ وہ غیر محرم سے بات کرتے ہوئے اپنی زبان سے کسی حد تک سخت لہجہ میں سنجیدگی سے بات کرے۔ نیز ایسے بے تکلف انداز میں بات نہ کرے جس سے کسی قسم کی غلط توقعات کسی کے دل میں پیدا ہوں۔', 'د یوې ښځې لپاره د خپل عفت د ساتنې لپاره دا هم اړینه ده چې له نامحرم سره د خبرو پر مهال په خپله ژبه تر یوه حده په سخته لهجه او جديت خبرې وکړي؛ همدارنګه په داسې بې‌تکلفه انداز خبرې ونه کړي چې د چا په زړه کې د کوم ډول ناسمو تمو لامل شي.'),
          ('Through His commands Allah Almighty did not put the pure Ahl al-Bayt (may Allah be pleased with them) of the Holy Prophet (peace and blessings of Allah be upon him) into any hardship; rather, to raise them to the highest ranks He purified their souls, reformed their deeds, and purified their character.', 'اللہ تعالیٰ نے اپنے احکامات کے ذریعہ نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے اہلِ بیتِ اطہار رضی اللہ عنہم کو کسی مشقت میں مبتلا نہیں کیا بلکہ انھیں اعلیٰ مراتب پر فائز فرمانے کے لیے ان کے نفوس کا تزکیہ کیا، ان کے اعمال کی اصلاح کی اور اخلاق کی تطہیر فرمائی۔', 'الله تعالی د خپلو حکمونو له لارې د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم پاک اهل بیت رضي الله عنهم په کومه سختۍ کې ندي اچولي، بلکې د لوړو درجو د رسولو لپاره یې د هغوی نفسونه پاک کړل، عملونه یې اصلاح کړل او اخلاق یې پاک کړل.')])
    VOC(b, 'mq12-l11-vocab', VOCAB)
    BOOK.save(114, [(11, rec(b, 11, 114, 114))], issues=[{'id': 'mq12-pdf114', 'unit': 11, 'printedPage': 111,
               'description': 'Four-column vocabulary rendered as one two-column table (16 rows). Third knowledge point prints "اور وہ اہلِ ایمان کے لیے" (kept). Lower part of p.111 blank.'}])


if __name__ == '__main__':
    p114()
