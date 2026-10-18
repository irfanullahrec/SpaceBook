"""Mutalia-e-Quran XII PDF148: p.145 — Lesson 15 Surah Muhammad (1–38): naming and introduction, central theme, basic themes. Run: python class12_quran_page148.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('A comparison of the states of the disbelievers and the people of faith and of their end', 'کفار اور اہلِ ایمان کے احوال اور ان کے انجام کا موازنہ', 'د کافرانو او مؤمنانو د حالاتو او پایلو پرتله'),
    ('Encouragement to jihad', 'جہاد کی ترغیب', 'جهاد ته هڅونه'),
    ('The excellence of the martyrs', 'شہداء کی فضیلت', 'د شهیدانو فضیلت'),
    ('The exemplary end of the disbelievers', 'کفار کا عبرت ناک انجام', 'د کافرانو عبرتناکه پایله'),
    ('Commands of war for the Muslims', 'مسلمانوں کے لیے جنگ کے احکام', 'د مسلمانانو لپاره د جګړې حکمونه'),
    ('The blessings of Paradise for the people of faith', 'اہلِ ایمان کے لیے جنت کی نعمتیں', 'د مؤمنانو لپاره د جنت نعمتونه'),
    ('Mention of the hypocrites being punished', 'منافقین کو سزا دیے جانے کا ذکر', 'منافقانو ته د سزا ورکولو یادونه'),
    ('Glad tidings to the believers of increase in guidance and of steadfastness in piety', 'ایمان والوں کے لیے ہدایت میں اضافہ اور تقویٰ پر استقامت کی بشارت', 'مؤمنانو ته په هدایت کې د زیاتوالي او پر تقوا د استقامت زېری'),
    ('The instruction to the Prophet (peace and blessings of Allah be upon him) to seek forgiveness for the people of faith', 'آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو اہلِ ایمان کے لیے بخشش مانگنے کی تلقین', 'هغه صلی الله علیه وعلی آله واصحابه وسلم ته د مؤمنانو لپاره د بښنې غوښتلو لارښوونه'),
    ('Conclusive proof (itmam al-hujjah) for the deniers', 'منکرین کے لیے اتمامِ حجت', 'منکرانو ته د حجت پوره کول'),
    ('The conduct of the hypocrites about jihad', 'منافقین کا جہاد کے بارے میں طرزِ عمل', 'د جهاد په اړه د منافقانو چلند'),
    ('The causes of the misguidance of the hypocrites', 'منافقین کی گمراہی کے اسباب', 'د منافقانو د ګمراهۍ لاملونه'),
    ('A picture of the death of the hypocrites and a stern warning to them', 'منافقین کی موت کا نقشہ اور ان کے لیے سخت وعید', 'د منافقانو د مرګ انځور او هغوی ته سخت ګواښ'),
    ('Allah Almighty informing His Messenger (peace and blessings of Allah be upon him) of all the conspiracies and moves of the hypocrites', 'اللہ تعالیٰ کا منافقین کی تمام سازشوں اور حرکتوں سے اپنے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو آگاہ فرما دینا', 'د الله تعالی له خوا خپل رسول صلی الله علیه وعلی آله واصحابه وسلم ته د منافقانو له ټولو دسیسو او حرکتونو خبرول'),
    ('A warning to the disbelievers and their end', 'کفار کو تنبیہ اور ان کا انجام', 'کافرانو ته خبرداری او د هغوی پایله'),
    ('The command to the people of faith to obey Allah Almighty and His Messenger (peace and blessings of Allah be upon him)', 'اہلِ ایمان کو اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت کا حکم', 'مؤمنانو ته د الله تعالی او د هغه د رسول صلی الله علیه وعلی آله واصحابه وسلم د اطاعت حکم'),
    ('Instructions to the Muslims for facing the disbelievers', 'مسلمانوں کو کفار کے مقابلے کے لیے ہدایات', 'مسلمانانو ته د کافرانو د مقابلې لپاره لارښوونې'),
    ('Encouragement to spending in the way of Allah', 'انفاق فی سبیل اللہ کی ترغیب', 'د الله په لار کې لګښت ته هڅونه'),
    ('Divine rewards for carrying out the commands of Allah Almighty', 'اللہ تعالیٰ کے احکام کی انجام دہی پر انعاماتِ خداوندی', 'د الله تعالی د حکمونو د ترسره کولو پر الهي انعامونه'),
    ('Mention of the punishment of the hypocrites and the disbelievers', 'منافقین و کفار کی سزا کا ذکر', 'د منافقانو او کافرانو د سزا یادونه'),
]


def p148():
    b = Builder()
    b.h('Lesson 15 — Surah Muhammad (verses 1 to 38)', 'سبق ۱۵ — سُوْرَةُ مُحَمَّدٍ (آیات: ۱ تا ۳۸)', '۱۵ لوست — سورة محمد (آیتونه ۱ تر ۳۸)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('In verse 2 of this surah the name "Muhammad" (the Seal of the Prophets, peace and blessings of Allah be upon him and his family and companions) has come; with this connection its name is Surah Muhammad (peace and blessings of Allah be upon him). The second name of this surah is "Surat al-Qital" too; this word is mentioned in verse 20 of this surah. Since in this surah war between Islam and disbelief is mentioned and the commands of jihad and fighting have been stated.\nThis surah was revealed in the very early period of the Madani life after the Hijrah to Madinah Munawwarah. In this blessed surah three groups are mentioned: the people of faith, the disbelievers and the hypocrites. The states of the last two groups are given, and the people of Islam have been made aware of their conduct and end with respect to Islam.',
            'اس سورت کی آیت: ۲ میں مُحَمَّدٍ (خَاتَمُ النَّبِيِّيْنَ صَلَّى اللهُ عَلَيْهِ وَعَلٰی آلِهِ وَأَصْحَابِهِ وَسَلَّمَ) آیا ہے اسی مناسبت سے اس کا نام سُوْرَةُ مُحَمَّدٍ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) ہے۔ اس سورت کا دوسرا نام "سُوْرَةُ الْقِتَالِ" بھی ہے۔ یہ لفظ اس سورت کی آیت: ۲۰ میں مذکور ہے۔ چونکہ اس سورت میں اسلام اور کفر کے مابین جنگ کا تذکرہ ہے اور جہاد و قتال کے احکام بیان فرمائے گئے ہیں۔\nیہ سورت ہجرتِ مدینہ منورہ کے بعد مدنی زندگی کے بالکل ابتدائی دور میں نازل ہوئی۔ اس سورتِ مبارکہ میں تین گروہوں کا ذکر کیا گیا ہے، اہلِ ایمان، کفار اور منافقین۔ آخر الذکر دونوں گروہوں کے احوال، ان کے اسلام کے حوالے سے طرزِ عمل اور انجام سے اہلِ اسلام کو آگاہ کیا گیا ہے۔',
            'د دې سورت په ۲ آیت کې «محمد» (خاتم النبیین صلی الله علیه وعلی آله واصحابه وسلم) راغلی؛ په همدې مناسبت یې نوم سورة محمد (صلی الله علیه وعلی آله واصحابه وسلم) دی. د دې سورت دویم نوم «سورة القتال» هم دی؛ دا کلمه د دې سورت په ۲۰ آیت کې یاده شوې، ځکه په دې سورت کې د اسلام او کفر ترمنځ د جګړې یادونه ده او د جهاد او قتال حکمونه بیان شوي.\nدا سورت مدینې منورې ته له هجرت وروسته د مدني ژوند په بېخي لومړني پړاو کې نازل شو. په دې مبارک سورت کې د درېیو ډلو یادونه شوې: مؤمنان، کافران او منافقان. د وروستیو دوو ډلو له حالاتو، د اسلام په اړه له چلند او پایلې څخه مسلمانان خبر کړای شوي.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Encouragement to and commands of jihad and fighting and of spending in the way of Allah', 'جہاد و قتال اور انفاق فی سبیل اللہ کی ترغیب اور احکام', 'د جهاد او قتال او د الله په لار کې د لګښت هڅونه او حکمونه')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    BOOK.save(148, [(15, rec(b, 15, 148, 148, first=True))], issues=[{'id': 'mq12-pdf148', 'unit': 15, 'printedPage': 145,
               'description': 'Lesson 15 heading: Surah Muhammad, verses 1 to 38. Twenty basic themes printed as a run-on numbered paragraph; rendered as a list. The intro sentence beginning "چونکہ…" is left incomplete as printed. Lower part of p.145 blank.'}])


if __name__ == '__main__':
    p148()
