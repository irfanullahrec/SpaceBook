"""Mutalia-e-Quran XII PDF165: p.162 — Lesson 17 Surah al-Hujurat (1–18): naming and introduction, occasion of revelation, central theme, basic themes. Run: python class12_quran_page165.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Important teachings concerning reverence, honour, respect and courtesy towards Allah Almighty and the Holy Messenger (peace and blessings of Allah be upon him)', 'اللہ تعالیٰ اور رسول کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی تعظیم و توقیر اور ادب و احترام کے حوالے سے اہم تعلیمات', 'د الله تعالی او رسول کریم صلی الله علیه وعلی آله واصحابه وسلم د تعظیم، درناوي او ادب په اړه مهمې لارښوونې'),
    ('The command to be subordinate to the commands of the Messenger (peace and blessings of Allah be upon him)', 'رسالت مآب صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے احکامات کے تابع ہونے کا حکم', 'د رسالت مآب صلی الله علیه وعلی آله واصحابه وسلم د حکمونو د تابع کېدو حکم'),
    ('Necessary commands for fully investigating and verifying hearsay news', 'سنی سنائی خبروں کی مکمل تحقیق و تصدیق کے ضروری احکامات', 'د اورېدلو خبرونو د بشپړې څېړنې او تصدیق اړین حکمونه'),
    ('The command to follow the Holy Messenger (peace and blessings of Allah be upon him)', 'رسول کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اتباع کا حکم', 'د رسول کریم صلی الله علیه وعلی آله واصحابه وسلم د پیروۍ حکم'),
    ('Mention of the grace, generosity, favour and kindness of Allah Almighty upon the noble Companions (may Allah be pleased with them)', 'صحابہ کرام رضی اللہ عنہم پر اللہ تعالیٰ کے فضل و کرم اور انعام و احسان کا ذکر', 'پر صحابه کرامو رضي الله عنهم د الله تعالی د فضل، کرم، انعام او احسان یادونه'),
    ('Commands for the promotion of brotherhood and reconciliation', 'اخوت و مصالحت کے فروغ کے لیے احکامات', 'د ورورولۍ او پخلاینې د ودې لپاره حکمونه'),
    ('Commands and instructions for blocking the causes that scatter the unity of the Ummah', 'امت کا شیرازہ بکھیرنے والے اسباب کے سدِّ باب کے لیے احکامات و ہدایات', 'د امت د یووالي ړنګوونکو لاملونو د مخنیوي لپاره حکمونه او لارښوونې'),
    ('Global peace and human equality', 'عالمی امن و مساواتِ انسانی', 'نړیواله سوله او انساني برابري'),
    ('The Islamic concept of the different groups and tribes of human beings being merely a means of introduction', 'انسانوں کی مختلف گروہوں اور قبائل میں تقسیم محض تعارف کا ذریعہ ہونے کا اسلامی تصور', 'د انسانانو په بېلابېلو ډلو او قبیلو وېش یوازې د پېژندګلوۍ وسیله کېدو اسلامي تصور'),
    ('With Allah Almighty the standard of honour and excellence is piety', 'اللہ تعالیٰ کے نزدیک عزت اور فضیلت کا معیار تقویٰ ہے', 'د الله تعالی په وړاندې د عزت او فضیلت معیار تقوا ده'),
    ('A statement of the blessing of faith being a favour of Allah Almighty', 'نعمتِ ایمان پر اللہ تعالیٰ کا احسان ماننے کا بیان', 'د ایمان نعمت د الله تعالی احسان منلو بیان'),
    ('The qualities of the true people of faith', 'سچے اہلِ ایمان کی صفات', 'د رښتینو مؤمنانو صفتونه'),
    ('The majesty of the Exalted Lord', 'شانِ باری تعالیٰ', 'د باري تعالی شان'),
    ('Principles for the Muslims\' collective affairs and their unity', 'مسلمانوں کے لیے اجتماعی معاملات اور ان کے اتحاد کے اصول', 'د مسلمانانو لپاره د ټولیزو چارو او د هغوی د یووالي اصول'),
    ('Commands of jihad in the way of Allah', 'جہاد فی سبیل اللہ کے احکامات', 'د الله په لار کې د جهاد حکمونه'),
]


def p165():
    b = Builder()
    b.h('Lesson 17 — Surah al-Hujurat (verses 1 to 18)', 'سبق ۱۷ — سُوْرَةُ الْحُجُرَاتِ (آیات: ۱ تا ۱۸)', '۱۷ لوست — سورة الحجرات (آیتونه ۱ تر ۱۸)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('"Hujurat" is the plural of "hujrah", which means a room. In verse 4 of this surah those rooms are mentioned which the Mercy to the worlds, the Holy Messenger (peace and blessings of Allah be upon him), had built around the Prophet\'s Mosque, in which the Mothers of the Believers (may Allah be pleased with them) resided. With this connection its name is Surah al-Hujurat. In this way the dignity and greatness of those blessed walls has also been highlighted. Surah al-Hujurat was revealed in Madinah Munawwarah.',
            '"حُجُرَاتٌ" "حُجْرَةٌ" کی جمع ہے جس کا معنی کمرا ہے۔ اس سورت کی آیت: ۴ میں ان حجروں کا ذکر ہے جو رحمتِ دو عالم رسول کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم نے مسجد نبوی کے ارد گرد تعمیر کرائے تھے جن میں اُمہات المومنین رضی اللہ تعالیٰ عنہن رہائش پذیر تھیں۔ اسی مناسبت سے اس کا نام سُوْرَةُ الْحُجُرَاتِ ہے۔ یوں ان بابرکت در و دیوار کی شان اور عظمت بھی نمایاں کی گئی ہے۔ سُوْرَةُ الْحُجُرَاتِ مدینہ منورہ میں نازل ہوئی۔',
            '«حجرات» د «حجره» جمع ده چې مانا یې کوټه ده. د دې سورت په ۴ آیت کې د هغو حجرو یادونه ده چې د دواړو نړیو رحمت رسول کریم صلی الله علیه وعلی آله واصحابه وسلم د نبوي جومات شاوخوا جوړې کړې وې او پکې امهات المؤمنین رضي الله عنهن اوسېدې. په همدې مناسبت یې نوم سورة الحجرات دی؛ په دې توګه د هغو برکتناکو دروازو او دېوالونو شان او عظمت هم څرګند شوی. سورة الحجرات په مدینه منوره کې نازل شو.')),
          (('Occasion of revelation', 'شانِ نزول', 'د نزول شالید'),
           ('According to the opinion of the commentators, verse 4 was revealed concerning the delegation of the Banu Tamim tribe, who one day at noon, when it was the time of the Holy Prophet\'s (peace and blessings of Allah be upon him) midday rest — these people were not acquainted with etiquette — so some of them began calling "O Muhammad!" from outside the Prophet\'s (peace and blessings of Allah be upon him) room so that he would come out. On this a warning was given in this verse. In the books of Sirah the time of this delegation\'s arrival has been stated as 9 AH.',
            'مفسرین کی رائے کے مطابق آیت: ۴ قبیلہ بنو تمیم کے وفد کے بارے میں نازل ہوئی جنھوں نے ایک روز دوپہر کے وقت، جب نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے قیلولہ کا وقت تھا، یہ لوگ آداب سے واقف نہیں تھے، اس لیے ان میں سے کچھ لوگوں نے آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے حجرہ کے باہر ہی سے آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو یا محمد کہہ کر پکارنا شروع کر دیا تاکہ آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم باہر تشریف لے آئیں۔ اس پر اس آیت کریمہ میں تنبیہ فرمائی گئی ہے۔ کتبِ سیرت میں اس وفد کی آمد کا زمانہ ۹ھ بیان کیا گیا ہے۔',
            'د مفسرینو د رایې له مخې ۴ آیت د بنو تمیم قبیلې د پلاوي په اړه نازل شو چې یوه ورځ غرمه، کله چې د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د قیلولې وخت و، دا خلک له آدابو خبر نه وو، نو ځینو یې د هغه صلی الله علیه وعلی آله واصحابه وسلم د حجرې له بهره «یا محمد» ویل پیل کړل تر څو هغه صلی الله علیه وعلی آله واصحابه وسلم بهر راشي. پر دې په دې آیت کې خبرداری ورکړل شو. د سیرت په کتابونو کې د دې پلاوي د راتګ زمانه ۹ هجري بیان شوې.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Etiquette of social life', 'آدابِ معاشرت', 'د ټولنیز ژوند آداب')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    BOOK.save(165, [(17, rec(b, 17, 165, 165, first=True))], issues=[{'id': 'mq12-pdf165', 'unit': 17, 'printedPage': 162,
               'description': 'Lesson 17 heading: Surah al-Hujurat, verses 1 to 18. Fifteen basic themes printed as a run-on numbered paragraph; rendered as a list. Orange and yellow highlighter strokes and pasted sticky marks by a reader (excluded). The occasion-of-revelation sentence is printed with a broken construction (kept in sense).'}])


if __name__ == '__main__':
    p165()
