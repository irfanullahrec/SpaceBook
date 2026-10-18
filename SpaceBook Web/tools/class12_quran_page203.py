"""Mutalia-e-Quran XII PDF203: p.200 — Lesson 22 Surah al-Saff and Surah al-Jumu'ah; Surah al-Saff (1–14): naming and introduction, central theme, basic themes. Run: python class12_quran_page203.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Glorification and praise of Allah Almighty, and His attributes', 'اللہ تعالیٰ کی تسبیح و تحمید اور صفات', 'د الله تعالی تسبیح، حمد او صفتونه'),
    ('Severe reproach of the contradiction between word and deed', 'قول و فعل کے تضاد پر سخت گرفت', 'د خبرې او عمل پر تضاد سخته نیونه'),
    ('Fighting in the way of Allah in an organised manner for the exaltation of the name of Allah Almighty', 'اللہ تعالیٰ کے نام کی سربلندی کے لیے منظم ہو کر قتال فی سبیل اللہ کرنا', 'د الله تعالی د نوم د لوړتیا لپاره په منظم ډول د الله په لار کې قتال'),
    ('Severe warning to those who turn away from obedience to the Messenger of Allah (peace and blessings of Allah be upon him) and from jihad for the supremacy of the true religion', 'رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت اور غلبۂ دینِ حق کے لیے جہاد سے اعراض کرنے والوں کے لیے سخت تنبیہ', 'د رسول الله صلی الله علیه وعلی آله واصحابه وسلم له اطاعت او د حق دین د غلبې لپاره له جهاد مخ اړوونکو ته سخت خبرداری'),
    ('Glad tidings of the coming of the Holy Prophet (peace and blessings of Allah be upon him) on the tongue of Sayyiduna \'Isa (peace be upon him)', 'سیدنا عیسیٰ علیہ السلام کی زبانی نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی آمد کی بشارت', 'د سیدنا عیسی علیه السلام په ژبه د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د راتګ زېری'),
    ('The purpose of the sending of the Holy Prophet (peace and blessings of Allah be upon him): the supremacy of the religion of Islam over all false religions', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کا مقصدِ بعثت — دینِ اسلام کا تمام ادیانِ باطلہ پر غلبہ', 'د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د بعثت موخه — پر ټولو باطلو دینونو د اسلام د دین غلبه'),
    ('Encouragement to the beneficial trade of striving with wealth and life in the way of Allah Almighty for great success in this world and the Hereafter', 'دنیا و آخرت کی عظیم کامیابی کے لیے مال و جان کے ساتھ اللہ تعالیٰ کی راہ میں نفع بخش تجارت کی ترغیب', 'د دنیا او آخرت د لویې بریا لپاره په مال او ځان سره د الله تعالی په لار کې ګټورې سوداګرۍ ته هڅونه'),
    ('Encouragement to jihad for the supremacy of the true religion', 'غلبۂ دینِ حق کے لیے جہاد کرنے کی ترغیب', 'د حق دین د غلبې لپاره جهاد ته هڅونه'),
    ('The great honour of being helpers of Allah Almighty and His Messenger (peace and blessings of Allah be upon him), and mention of the supremacy of the disciples of Sayyiduna \'Isa (peace be upon him)', 'اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے مددگار ہونے کا عظیم سعادت اعزاز، سیدنا عیسیٰ علیہ السلام کے حواریوں کے غلبہ کا ذکر', 'د الله تعالی او د هغه د رسول صلی الله علیه وعلی آله واصحابه وسلم د مرستندویانو کېدو ستر وياړ، او د سیدنا عیسی علیه السلام د حواریانو د غلبې یادونه'),
    ('The command to revere, honour and obey the Messenger (peace and blessings of Allah be upon him)', 'رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی تعظیم، توقیر اور اطاعت کا حکم', 'د رسول صلی الله علیه وعلی آله واصحابه وسلم د تعظیم، درناوي او اطاعت حکم'),
    ('The means of success in the Hereafter: faith, sincerity, unity and jihad', 'آخرت کی کامیابی کا ذریعہ — ایمان، اخلاص، اتحاد اور جہاد', 'د آخرت د بریا وسیله — ایمان، اخلاص، یووالی او جهاد'),
]


def p203():
    b = Builder()
    b.h('Lesson 22 — Surah al-Saff and Surah al-Jumu\'ah', 'سبق ۲۲ — سُوْرَةُ الصَّفِّ اور سُوْرَةُ الْجُمُعَةِ', '۲۲ لوست — سورة الصف او سورة الجمعه')
    b.h('Surah al-Saff (verses 1 to 14)', 'سُوْرَةُ الصَّفِّ (آیات: ۱ تا ۱۴)', 'سورة الصف (آیتونه ۱ تر ۱۴)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('In "Surah al-Saff" the greatness is mentioned of those who strive in the way of Allah Almighty in ranks like a solid structure. With this connection its name has been kept "Surah al-Saff". It begins with the glorification of Allah Almighty, so this surah too is included among the "Musabbihat". It is narrated from Sayyiduna \'Abdullah ibn Salam (may Allah be pleased with him) that a group of the Companions of the Messenger (peace and blessings of Allah be upon him) was sitting with us and we said: if we knew which deed is the most beloved to Allah Almighty, we would do it. On this Allah Almighty revealed the verses of this surah, and the Holy Prophet (peace and blessings of Allah be upon him) recited this surah to us. (Jami\' al-Tirmidhi, 3309)',
            'سُوْرَةُ الصَّفِّ" میں اللہ تعالیٰ کی راہ میں صف بستہ ہو کر سیسہ پلائی ہوئی دیوار کی طرح جہاد کرنے والوں کی عظمت کا ذکر ہے۔ اسی مناسبت سے اس کا نام "سُوْرَةُ الصَّفِّ" رکھا گیا ہے۔ اس کی ابتدا اللہ تعالیٰ کی تسبیح سے ہوتی ہے، اس لیے یہ سورت بھی "مُسَبِّحَات" میں شامل ہے۔ سیدنا عبداللہ بن سلام رضی اللہ تعالیٰ عنہ سے روایت ہے کہ اصحابِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم میں سے ایک جماعت ہمارے ساتھ بیٹھی اور ہم نے کہا: اگر ہمیں معلوم ہو جائے کہ اللہ تعالیٰ کے نزدیک سب سے پسندیدہ عمل کون سا ہے تو ہم اسی کو انجام دیں؟ اس پر اللہ تعالیٰ نے اس سورت کی آیات نازل فرمائیں اور نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم نے یہ سورت ہم پر تلاوت فرمائی۔ (جامع ترمذی، ۳۳۰۹)',
            'په «سورة الصف» کې د هغو کسانو د عظمت یادونه ده چې د الله تعالی په لار کې په لیکو کې د سرپ ویلي دېوال په څېر جهاد کوي؛ په همدې مناسبت یې نوم «سورة الصف» ایښودل شوی. پیل یې د الله تعالی په تسبیح کېږي، نو دا سورت هم په «مسبحاتو» کې شامل دی. له سیدنا عبدالله بن سلام رضي الله عنه روایت دی چې د رسول صلی الله علیه وعلی آله واصحابه وسلم له اصحابو یوه ډله له موږ سره کېناسته او موږ وویل: که موږ ته معلومه شي چې د الله تعالی په وړاندې تر ټولو خوښ عمل کوم دی، نو همغه به وکړو. پر دې الله تعالی د دې سورت آیتونه نازل کړل او نبي کریم صلی الله علیه وعلی آله واصحابه وسلم دا سورت موږ ته تلاوت کړ. (جامع ترمذي، ۳۳۰۹)')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('The purpose of the sending of Sayyiduna Hazrat Muhammad, the Messenger of Allah (peace and blessings of Allah be upon him)', 'سیدنا حضرت محمد رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی بعثت کا مقصد', 'د سیدنا حضرت محمد رسول الله صلی الله علیه وعلی آله واصحابه وسلم د بعثت موخه')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    BOOK.save(203, [(22, rec(b, 22, 203, 203, first=True))], issues=[{'id': 'mq12-pdf203', 'unit': 22, 'printedPage': 200,
               'description': 'Lesson 22 covers two surahs (al-Saff 1–14 and al-Jumu\'ah 1–11). Eleven basic themes of al-Saff printed as a run-on numbered paragraph; rendered as a list. Item 9 prints "عظیم سعادت اعزاز" (kept). The opening quotation mark of the intro is printed without its pair. A reader\'s thumb at the right edge excluded.'}])


if __name__ == '__main__':
    p203()
