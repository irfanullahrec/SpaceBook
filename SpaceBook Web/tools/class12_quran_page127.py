"""Mutalia-e-Quran XII PDF127: p.124 — Lesson 13 Surah Ha Mim al-Sajdah (1–54): naming and introduction, central theme, basic themes. Run: python class12_quran_page127.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

THEMES = [
    ('The greatness of the Qur\'an and a statement of its various attributes', 'عظمتِ قرآن اور اس کے مختلف اوصاف کا بیان', 'د قرآن عظمت او د هغه د بېلابېلو صفتونو بیان'),
    ('Declaration of the humanity of the Prophet of Islam (peace and blessings of Allah be upon him)', 'پیغمبرِ اسلام صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی بشریت کا اعلان', 'د اسلام د پیغمبر صلی الله علیه وعلی آله واصحابه وسلم د بشریت اعلان'),
    ('Mention of the call to truth of the Messenger of Allah (peace and blessings of Allah be upon him), and a statement of the obstinacy and end of the polytheists of Makkah', 'رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی دعوتِ حق کا ذکر اور مشرکینِ مکہ کی ہٹ دھرمی اور انجام کا بیان', 'د رسول الله صلی الله علیه وعلی آله واصحابه وسلم د حق بلنې یادونه، او د مکې د مشرکانو د ضد او پایلې بیان'),
    ('Mention of the everlasting reward of the believers', 'مومنین کے دائمی اجر کا ذکر', 'د مؤمنانو د تلپاتې اجر یادونه'),
    ('The objection of the disbelievers to Tawhid and its answer with cosmic proofs', 'کفار کا توحید پر اعتراض اور تکوینی دلائل سے اس کا جواب', 'پر توحید د کافرانو اعتراض او په تکویني دلیلونو د هغه ځواب'),
    ('Allah Almighty alone is the Creator and Administrator of the universe', 'اللہ تعالیٰ ہی کائنات کا خالق اور منتظم', 'یوازې الله تعالی د کائنات خالق او منتظم'),
    ('Lessons from the story of the nations that rejected the call of the messengers, and mention of the Resurrection', 'رسولوں کی دعوت کو جھٹلانے والی قوموں کی داستان سے عبرت اور قیامت کا تذکرہ', 'د هغو قومونو له کیسې عبرت چې د رسولانو بلنه یې دروغ وګڼله، او د قیامت یادونه'),
    ('The testimony of their own limbs against the polytheists, and mention of the domination of the devils over the disbelievers', 'مشرکین کے خلاف ان کے اعضا کی گواہی اور کفار پر شیاطین کے تسلط کا ذکر', 'د مشرکانو پر خلاف د هغوی د غړو شاهدي، او پر کافرانو د شیطانانو د تسلط یادونه'),
    ('Enmity towards the Holy Qur\'an and its end', 'قرآنِ کریم سے دشمنی اور اس کا انجام', 'له قرآن کریم سره دښمني او د هغې پایله'),
    ('A statement of showing steadfastness after accepting Allah Almighty as Lord', 'اللہ تعالیٰ کو رب مان کر استقامت کے اظہار کا بیان', 'الله تعالی رب منلو وروسته د استقامت د ښودلو بیان'),
    ('Mention of the honour and dignity of the believers', 'مومنین کے اعزاز و اکرام کا ذکر', 'د مؤمنانو د عزت او اکرام یادونه'),
    ('The command of patience, steadfastness and tolerance, that is, repaying evil with good, and mention of the divine rewards in return for it', 'صبر و ثبات اور رواداری یعنی برائی کا بدلہ اچھائی سے دینے کا حکم اور اس کے عوض انعاماتِ الٰہیہ کا تذکرہ', 'د صبر، ثبات او زغم حکم یعنې د بدۍ بدله په ښېګڼه ورکول، او د هغې په بدل کې د الهي انعامونو یادونه'),
    ('A statement of the etiquette of preaching the religion and the method of protection from the attacks of Satan', 'تبلیغِ دین کے آداب کا بیان اور شیطان کے حملوں سے بچنے کا طریقہ', 'د دین د تبلیغ د آدابو بیان او د شیطان له بریدونو د ژغورنې طریقه'),
    ('Mention of prostrating only before Allah Almighty', 'صرف اللہ تعالیٰ کے لیے سربسجود ہونے کا ذکر', 'یوازې الله تعالی ته د سجدې یادونه'),
    ('Mention of the great power of Allah Almighty and the vastness of His knowledge', 'اللہ تعالیٰ کی عظیم قدرت اور علم کی وسعت کا تذکرہ', 'د الله تعالی د لوی قدرت او د علم د پراخۍ یادونه'),
    ('A statement of the call to truth of the Messenger of Allah (peace and blessings of Allah be upon him)', 'رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی دعوتِ حق کا بیان', 'د رسول الله صلی الله علیه وعلی آله واصحابه وسلم د حق بلنې بیان'),
    ('Mention of the Holy Qur\'an being guidance and healing and of the proof of its truth, and a statement of the evil end of those who deny the divine verses', 'قرآنِ مجید کے ہدایت اور شفاء ہونے اور اس کی حقانیت کے ثبوت کا ذکر اور آیاتِ الٰہی کے منکرین کے انجامِ بد کا بیان', 'د قرآن مجید د هدایت او شفا کېدو او د هغه د حقانیت د ثبوت یادونه، او د الهي آیتونو د منکرانو د بدې پایلې بیان'),
    ('A statement of the denial of Hazrat Musa (peace be upon him)', 'حضرت موسیٰ علیہ السلام کی تکذیب کرنے کا بیان', 'د حضرت موسی علیه السلام د تکذیب بیان'),
    ('The evil end of the disbelievers and the warning of severe punishment for those who deny the Resurrection', 'کافروں کا انجامِ بد اور منکرینِ قیامت کے لیے شدید عذاب کی وعید', 'د کافرانو بده پایله او د قیامت منکرانو ته د سخت عذاب ګواښ'),
    ('Proofs of Tawhid and mention of man\'s ingratitude', 'توحید کے دلائل اور انسان کی ناشکری کا ذکر', 'د توحید دلیلونه او د انسان د ناشکرۍ یادونه'),
    ('A statement of the crookedness of the deniers, and mention of the signs of Allah Almighty present in the human self and in the universe', 'منکرین کی کج روی کا بیان اور انسانی جان اور کائنات میں موجود اللہ تعالیٰ کی نشانیوں کا تذکرہ', 'د منکرانو د کږلارۍ بیان، او په انساني نفس او کائنات کې د الله تعالی د موجودو نښو یادونه'),
]
D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')


def p127():
    b = Builder()
    b.h('Lesson 13 — Surah Ha Mim al-Sajdah (verses 1 to 54)', 'سبق ۱۳ — سُوْرَةُ حٰمٓ السَّجْدَةِ (آیات: ۱ تا ۵۴)', '۱۳ لوست — سورة حم السجده (آیتونه ۱ تر ۵۴)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('This surah begins with the letters Ha Mim, and in verse 37 is the word "sajdah" (prostration). With this connection its name is Ha Mim al-Sajdah. Its second name is "Fussilat" too, because this word has come in its first verse; further, it is also called "Surat al-Masabih" and "Surat al-Aqwat". It is a Makki surah. It is the second surah among the seven "Hawamim". Its subject is "practical Tawhid". In this surah there is a statement of calling towards the Oneness of the Exalted Lord. Since the most important means of calling towards Allah Almighty is the Qur\'an-e-Hakim, therefore very important verses on the greatness of the Qur\'an-e-Hakim have been stated in this surah.',
            'اس سورت کا آغاز حٰمٓ کے حروف سے ہوتا ہے اور آیت: ۳۷ میں لفظ سجدہ ہے۔ اس مناسبت سے اس کا نام حٰمٓ السَّجْدَةُ ہے۔ اس کا دوسرا نام فُصِّلَتْ بھی ہے، کیوں کہ اس کی پہلی آیت میں یہ لفظ آیا ہے، نیز اسے سُوْرَةُ الْمَصَابِيْحِ اور سُوْرَةُ الْأَقْوَاتِ بھی کہا جاتا ہے۔ یہ مکی سورت ہے۔ یہ سات "حوامیم" میں سے دوسری سورت ہے۔ اس کا موضوع ہے "توحیدِ عملی"۔ اس سورت میں توحیدِ باری تعالیٰ کی طرف بلانے کا بیان ہے۔ چوں کہ اللہ تعالیٰ کی طرف بلانے کا اہم ترین ذریعہ قرآنِ حکیم ہے، اس لیے اس سورت میں عظمتِ قرآنِ حکیم پر بہت اہم آیات بیان فرمائی گئی ہیں۔',
            'د دې سورت پیل د «حم» په تورو کېږي او په ۳۷ آیت کې د «سجده» کلمه ده؛ په همدې مناسبت یې نوم «حم السجده» دی. دویم نوم یې «فصلت» هم دی، ځکه چې دا کلمه یې په لومړي آیت کې راغلې؛ همدارنګه ورته «سورة المصابیح» او «سورة الاقوات» هم ویل کېږي. دا مکي سورت دی او له اوو «حوامیمو» څخه دویم سورت دی. موضوع یې «عملي توحید» ده. په دې سورت کې د باري تعالی توحید ته د بلنې بیان دی. څرنګه چې الله تعالی ته د بلنې تر ټولو مهمه وسیله قرآن حکیم دی، نو په دې سورت کې د قرآن حکیم د عظمت په اړه ډېر مهم آیتونه بیان شوي.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('A statement of the three beliefs (Tawhid, Prophethood and the Hereafter)', 'عقائدِ ثلاثہ (توحید، رسالت اور آخرت) کا بیان', 'د درې ګونو عقیدو (توحید، رسالت او آخرت) بیان')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    BOOK.save(127, [(13, rec(b, 13, 127, 127, first=True))], issues=[{'id': 'mq12-pdf127', 'unit': 13, 'printedPage': 124,
               'description': 'Lesson 13 heading: Surah Ha Mim al-Sajdah, verses 1 to 54. The basic themes are printed as a run-on paragraph whose item numbers are faint; rendered as a list of the printed themes. The intro says "fussilat" occurs in the first verse; in the standard count it is 41:3 (kept as printed).'}])


if __name__ == '__main__':
    p127()
