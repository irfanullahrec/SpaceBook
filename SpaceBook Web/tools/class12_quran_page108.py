"""Mutalia-e-Quran XII PDF108: p.105 — Lesson 11 Surah al-Ahzab (1–34): naming and introduction, central theme, basic themes. Run: python class12_quran_page108.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
P = ('Prophet (peace and blessings of Allah be upon him)', 'صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم', 'صلی الله علیه وعلی آله واصحابه وسلم')
THEMES = [
    ('Reform of wrong customs', 'غلط رسومات کی اصلاح', 'د غلطو رواجونو اصلاح'),
    ('Commands concerning adopted (so-called) sons', 'منہ بولے بیٹے کے بارے میں احکام', 'د خوله‌ویلي زوی په اړه حکمونه'),
    ('The lofty rank of the Messenger of Allah (peace and blessings of Allah be upon him) and of the Pure Wives (may Allah be pleased with them)', 'رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم اور ازواجِ مطہرات رضی اللہ عنہن کا بلند مرتبہ', 'د رسول الله صلی الله علیه وعلی آله واصحابه وسلم او د پاکو مېرمنو رضي الله عنهن لوړ مقام'),
    ('The battle of Ahzab', 'غزوۂ احزاب', 'د احزابو غزا'),
    ('Reproach of the conduct of the hypocrites', 'منافقین کے طرزِ عمل پر گرفت', 'د منافقانو پر چلند نیونه'),
    ('The importance of the blessed example of the Messenger of Allah (peace and blessings of Allah be upon him)', 'رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے اسوۂ مبارکہ کی اہمیت', 'د رسول الله صلی الله علیه وعلی آله واصحابه وسلم د مبارک اسوې اهمیت'),
    ('Praise of the people of faith', 'اہلِ ایمان کی تعریف', 'د مؤمنانو ستاینه'),
    ('Mention of the battle of Banu Qurayzah', 'غزوۂ بنی قریظہ کا ذکر', 'د بني قریظه د غزا یادونه'),
    ('Commands of purdah (veiling)', 'پردے کے احکام', 'د پردې حکمونه'),
    ('The greatness of the pure Ahl al-Bayt (may Allah be pleased with them)', 'اہلِ بیتِ اطہار رضی اللہ عنہم کی عظمت', 'د پاک اهل بیت رضي الله عنهم عظمت'),
    ('Qualities of believing men and women deserving forgiveness and a great reward', 'مغفرت اور اجرِ عظیم کے مستحق مومن مردوں اور عورتوں کی صفات', 'د بښنې او لوی اجر وړ مؤمنو نارینه وو او ښځو صفتونه'),
    ('The marriage of Sayyidah Zaynab bint Jahsh (may Allah be pleased with her) to the Holy Prophet (peace and blessings of Allah be upon him)', 'سیدہ زینب بنت جحش رضی اللہ عنہا کا نبی اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم سے نکاح', 'د سیدې زینب بنت جحش رضي الله عنها له نبي اکرم صلی الله علیه وعلی آله واصحابه وسلم سره نکاح'),
    ('Remembrance of Allah (dhikr)', 'ذکرِ الٰہی', 'د الله ذکر'),
    ('The exalted status of the Holy Prophet (peace and blessings of Allah be upon him)', 'نبی اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی شان', 'د نبي اکرم صلی الله علیه وعلی آله واصحابه وسلم شان'),
    ('An issue of divorce', 'طلاق کا ایک مسئلہ', 'د طلاق یوه مسئله'),
    ('Some commands for the marriages of the Prophet (peace and blessings of Allah be upon him)', 'آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے لیے نکاح کے بعض احکام', 'د هغه صلی الله علیه وعلی آله واصحابه وسلم لپاره د نکاح ځینې حکمونه'),
    ('Etiquette of the house of the Holy Prophet (peace and blessings of Allah be upon him)', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے گھر کے آداب', 'د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د کور آداب'),
    ('The command to send blessings and peace upon the Holy Prophet (peace and blessings of Allah be upon him)', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر درود و سلام بھیجنے کا حکم', 'پر نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د درود او سلام لېږلو حکم'),
    ('Warning to the hypocrites', 'منافقین کو وعید', 'منافقانو ته ګواښ'),
    ('Mention of the Resurrection', 'قیامت کا ذکر', 'د قیامت یادونه'),
    ('The end of the disbelievers', 'کفار کا انجام', 'د کافرانو پایله'),
    ('Advice to the Muslims to avoid causing hurt and distress to the Messenger of Allah (peace and blessings of Allah be upon him)', 'مسلمانوں کو رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی ایذا رسانی اور دل آزاری سے بچنے کی نصیحت', 'مسلمانانو ته د رسول الله صلی الله علیه وعلی آله واصحابه وسلم له ځورونې او زړه‌ماتونې د ډډې نصیحت'),
    ('Glad tidings of success for those who obey Allah Almighty and His Messenger (peace and blessings of Allah be upon him)', 'اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت کرنے والوں کے لیے کامیابی کی بشارت', 'د الله تعالی او د هغه د رسول صلی الله علیه وعلی آله واصحابه وسلم د اطاعت کوونکو لپاره د بریا زېری'),
    ('Mention of man\'s accepting the responsibility of bearing the trust of Allah Almighty', 'انسان کی طرف سے اللہ تعالیٰ کی امانت کو اٹھانے کی ذمہ داری قبول کرنے کا ذکر', 'د انسان له خوا د الله تعالی د امانت د پورته کولو د مسؤلیت د منلو یادونه'),
    ('Announcement of punishment for the hypocrites and the polytheists and of acceptance of the repentance of the believers', 'منافقین اور مشرکین کو عذاب اور مومنین کی توبہ کی قبولیت کا اعلان', 'منافقانو او مشرکانو ته د عذاب او د مؤمنانو د توبې د منلو اعلان'),
]


def p108():
    b = Builder()
    b.h('Lesson 11 — Surah al-Ahzab (verses 1 to 34)', 'سبق ۱۱ — سُوْرَةُ الْأَحْزَابِ (آیات: ۱ تا ۳۴)', '۱۱ لوست — سورة الاحزاب (آیتونه ۱ تر ۳۴)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('"Al-Ahzab" is the plural of "hizb", which means a group or a party. In verse 20 of this surah "al-Ahzab", that is, those groups, are mentioned who in the battle of Ahzab (the battle of the Trench) united against the people of faith and attacked Madinah Munawwarah. With this connection its name is Surah al-Ahzab. This surah is Madani and was revealed after the battle of Ahzab in 5 AH. In this surah three important events are mentioned in detail: the battle of Ahzab, the battle of Banu Qurayzah, and the marriage of the Holy Prophet (peace and blessings of Allah be upon him) to Sayyidah Zaynab (may Allah be pleased with her). Besides these events many other important themes have also been stated, such as: the greatness of the Holy Prophet (peace and blessings of Allah be upon him), the virtue and lofty status of the pure Ahl al-Bayt (may Allah be pleased with them) of the Holy Messenger, especially the Pure Wives (may Allah be pleased with them), and abandoning the customs of the age of ignorance, etc.',
            '"اَلْأَحْزَابُ" "حِزْبٌ" کی جمع ہے جس کے معنی گروہ اور جماعت کے ہیں۔ اس سورت کی آیت: ۲۰ میں "اَلْأَحْزَابُ" یعنی ان گروہوں کا ذکر ہوا ہے جنھوں نے غزوۂ احزاب (غزوۂ خندق) میں اہلِ ایمان کے خلاف متحد ہو کر مدینہ منورہ پر حملہ کیا تھا۔ اسی مناسبت سے اس کا نام سُوْرَةُ الْأَحْزَابِ ہے۔ یہ سورت مدنی ہے جو غزوۂ احزاب کے بعد ۵ھ میں نازل ہوئی۔ اس سورت میں تین اہم واقعات غزوۂ احزاب، غزوۂ بنی قریظہ اور نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کا سیدہ زینب رضی اللہ عنہا سے نکاح کا تفصیلی ذکر ہے۔ ان واقعات کے علاوہ بھی دوسرے بہت سے اہم مضامین بیان ہوئے ہیں۔ جیسے: نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی عظمت، رسول کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے اہلِ بیتِ اطہار رضی اللہ عنہم خصوصاً ازواجِ مطہرات رضی اللہ تعالیٰ عنہن کی فضیلت و بلند شان اور زمانۂ جاہلیت کی رسومات کو ترک کرنا وغیرہ۔',
            '"الاحزاب" د "حزب" جمع ده چې مانا یې ډله او جماعت دی. د دې سورت په ۲۰ آیت کې د "الاحزاب" یعنې د هغو ډلو یادونه شوې چې د احزابو په غزا (د خندق غزا) کې د مؤمنانو پر خلاف سره یو شوې او پر مدینه منوره یې برید وکړ. په همدې مناسبت یې نوم سورة الاحزاب دی. دا سورت مدني دی چې د احزابو له غزا وروسته په ۵ هجري کې نازل شو. په دې سورت کې درې مهمې پېښې په تفصیل یادې شوې: د احزابو غزا، د بني قریظه غزا او له سیدې زینب رضي الله عنها سره د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم نکاح. له دې پېښو پرته نور ډېر مهم مضامین هم بیان شوي، لکه: د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم عظمت، د رسول کریم صلی الله علیه وعلی آله واصحابه وسلم د پاک اهل بیت رضي الله عنهم په ځانګړي ډول د پاکو مېرمنو رضي الله عنهن فضیلت او لوړ شان، او د جاهلیت د زمانې د رواجونو پرېښودل او داسې نور.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Family, social and military etiquette', 'خاندانی، معاشرتی اور عسکری آداب', 'کورني، ټولنیز او پوځي آداب')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    BOOK.save(108, [(11, rec(b, 11, 108, 108, first=True))], issues=[{'id': 'mq12-pdf108', 'unit': 11, 'printedPage': 105,
               'description': 'Lesson 11 heading: Surah al-Ahzab, verses 1 to 34. Twenty-five basic themes printed as a run-on numbered paragraph; rendered as a list. The intro cites verse 20 for the word al-Ahzab (kept as printed).'}])


if __name__ == '__main__':
    p108()
