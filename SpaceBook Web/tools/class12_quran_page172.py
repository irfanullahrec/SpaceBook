"""Mutalia-e-Quran XII PDF172: p.169 — Lesson 18 Surah al-Hadid (1–29): naming and introduction, central theme, basic themes. Run: python class12_quran_page172.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Mention of the Oneness and greatness of Allah Almighty', 'اللہ تعالیٰ کی توحید اور عظمت کا ذکر', 'د الله تعالی د توحید او عظمت یادونه'),
    ('A comprehensive statement of the attributes of the Exalted Lord', 'صفاتِ باری تعالیٰ کا جامع بیان', 'د باري تعالی د صفتونو جامع بیان'),
    ('Emphasis on believing sincerely in Allah Almighty and the Holy Messenger (peace and blessings of Allah be upon him)', 'خلوص کے ساتھ اللہ تعالیٰ اور رسول اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر ایمان لانے کی تاکید', 'په اخلاص سره پر الله تعالی او رسول اکرم صلی الله علیه وعلی آله واصحابه وسلم د ایمان راوړلو ټینګار'),
    ('The promise of the best reward for the sincere people of faith', 'مخلص اہلِ ایمان کے لیے بہترین اجر کا وعدہ', 'مخلصو مؤمنانو ته د غوره اجر وعده'),
    ('Encouragement to spending in the way of Allah', 'انفاق فی سبیل اللہ کی ترغیب', 'د الله په لار کې لګښت ته هڅونه'),
    ('Glad tidings of light and Paradise in the Hereafter for the sincere believers', 'آخرت میں مخلص مومنین کے لیے نور اور جنت کی بشارت', 'په آخرت کې مخلصو مؤمنانو ته د نور او جنت زېری'),
    ('Deprivation of light and punishment for the hypocrites', 'منافقین کے لیے نور سے محرومی اور عذاب', 'منافقانو ته له نوره بې‌برخې کېدل او عذاب'),
    ('Encouragement to adopting fear of God', 'خشیتِ الٰہی اختیار کرنے کی ترغیب', 'د الهي وېرې غوره کولو ته هڅونه'),
    ('The excellence of spending in the way of Allah', 'انفاق فی سبیل اللہ کی فضیلت', 'د الله په لار کې د لګښت فضیلت'),
    ('A statement of the blessings of perfect faith', 'کامل ایمان کی برکات کا بیان', 'د بشپړ ایمان د برکتونو بیان'),
    ('The reality of the transient life of the world', 'دنیا کی عارضی زندگی کی حقیقت', 'د دنیا د لنډمهاله ژوند حقیقت'),
    ('Encouragement to preparing for the Hereafter', 'آخرت کی تیاری کی ترغیب', 'د آخرت تیارۍ ته هڅونه'),
    ('Mention of the condemnation of miserliness', 'بخل کی مذمت کا ذکر', 'د بخل د غندنې یادونه'),
    ('The purpose of the sending of the messengers', 'رسولوں کی بعثت کا مقصد', 'د رسولانو د بعثت موخه'),
    ('Encouragement to jihad for the establishment of justice and equity', 'عدل و انصاف کے قیام کے لیے جہاد کی ترغیب', 'د عدل او انصاف د قیام لپاره جهاد ته هڅونه'),
    ('Refutation of monasticism', 'رہبانیت کی تردید', 'د رهبانیت ردول'),
    ('The fruits of following the Messenger (peace and blessings of Allah be upon him)', 'اتباعِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے ثمرات', 'د رسول صلی الله علیه وعلی آله واصحابه وسلم د پیروۍ ګټې'),
    ('Double reward for the sincere people of faith', 'مخلص اہلِ ایمان کے لیے دوگنا اجر', 'مخلصو مؤمنانو ته دوه چنده اجر'),
    ('Allah Almighty\'s complete authority over His bounty', 'اللہ تعالیٰ کا اپنے فضل پر کامل اختیار', 'پر خپل فضل د الله تعالی بشپړ اختیار'),
]


def p172():
    b = Builder()
    b.h('Lesson 18 — Surah al-Hadid (verses 1 to 29)', 'سبق ۱۸ — سُوْرَةُ الْحَدِيْدِ (آیات: ۱ تا ۲۹)', '۱۸ لوست — سورة الحدید (آیتونه ۱ تر ۲۹)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('"Hadid" means "iron". In the twenty-fifth verse of this surah the word "hadid" has come; with this connection the name of this surah has been kept Surah al-Hadid. Surah al-Hadid is a Madani surah. This surah is the first of the "Musabbihat". "Musabbihat" is the name given to those surahs whose beginning is with the word "sabbaha" or "yusabbihu", for example Surah al-Hadid, Surah al-Hashr, Surah al-Saff, Surah al-Jumu\'ah and Surah al-Taghabun. At the time of the revelation of this surah there were countless dangers for the Muslims; the power of disbelief was striving with its last tactics to wipe out the Muslims. The battle of Badr and the battles after it had convinced the disbelievers that now they had to fight the Muslims once with full force, otherwise the Muslims would go on advancing.',
            '"حَدِيْدٌ" کے معنی "لوہا" ہیں۔ اس سورت کی پچیسویں آیت میں لفظ "حَدِيْدٌ" آیا ہے۔ اسی مناسبت سے اس کا نام سُوْرَةُ الْحَدِيْدِ رکھا گیا ہے۔ سُوْرَةُ الْحَدِيْدِ مدنی سورت ہے۔ یہ سورت "مُسَبِّحَات" میں سے پہلی سورت ہے۔ "مُسَبِّحَات" ان سورتوں کو کہا جاتا ہے جن کا آغاز لفظ "سَبَّحَ" یا "يُسَبِّحُ" سے ہوا ہے مثلاً سُوْرَةُ الْحَدِيْدِ، سُوْرَةُ الْحَشْرِ، سُوْرَةُ الصَّفِّ، سُوْرَةُ الْجُمُعَةِ اور سُوْرَةُ التَّغَابُنِ۔ اس سورت کے نزول کے وقت مسلمانوں کے لیے بے شمار خطرات تھے، کفر کی طاقت اپنے آخری حربوں کے ساتھ مسلمانوں کو مٹانے کے لیے ہاتھ پاؤں مار رہی تھی۔ غزوۂ بدر اور اس کے بعد کے غزوات نے کافروں کو یہ باور کرا دیا تھا کہ اب بھرپور اور یک بارگی مسلمانوں کا مقابلہ کرنا ہوگا ورنہ مسلمان بڑھتے ہی چلے جائیں گے۔',
            '«حدید» مانا «اوسپنه» ده. د دې سورت په پنځه ویشتم آیت کې د «حدید» کلمه راغلې؛ په همدې مناسبت یې نوم سورة الحدید ایښودل شوی. سورة الحدید مدني سورت دی او د «مسبحاتو» لومړی سورت دی. «مسبحات» هغو سورتونو ته ویل کېږي چې پیل یې په «سبح» یا «یسبح» کلمه شوی، لکه سورة الحدید، سورة الحشر، سورة الصف، سورة الجمعه او سورة التغابن. د دې سورت د نزول پر مهال مسلمانانو ته بې‌شمېره خطرونه وو؛ د کفر ځواک په خپلو وروستیو چلونو سره د مسلمانانو د له منځه وړلو لپاره لاس او پښې وهلې. د بدر غزا او له هغې وروسته غزاګانو کافرانو ته دا باور ورکړی و چې اوس باید په بشپړ ځواک او یوځل له مسلمانانو سره مقابله وکړي، ګڼې مسلمانان به مخ پر وړاندې ځي.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('The power of Allah Almighty; the demands of faith in Allah (spending, jihad and fighting in the way of Allah, and steadfastness)', 'اللہ تعالیٰ کی قدرت، ایمان باللہ کے تقاضے (انفاق، جہاد و قتال فی سبیل اللہ اور ثابت قدمی)', 'د الله تعالی قدرت، پر الله د ایمان غوښتنې (لګښت، د الله په لار کې جهاد او قتال، او ثابت قدمي)')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    BOOK.save(172, [(18, rec(b, 18, 172, 172, first=True))], issues=[{'id': 'mq12-pdf172', 'unit': 18, 'printedPage': 169,
               'description': 'Lesson 18 heading: Surah al-Hadid, verses 1 to 29. Nineteen basic themes printed as a run-on numbered paragraph; rendered as a list. Lower part of p.169 blank.'}])


if __name__ == '__main__':
    p172()
