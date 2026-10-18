"""Mutalia-e-Quran XII PDF90: p.87 — Lesson 9 Surah al-Nur (1–34): naming and introduction, central theme, basic themes, points to note. Run: python class12_quran_page090.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('The hadd punishment of zina and its commands', 'حدِ زنا اور اس کے احکام', 'د زنا حد او د هغې حکمونه'),
    ('The hadd punishment of qadhf (false accusation of unchastity)', 'حدِ قذف', 'د قذف حد'),
    ('The law of li\'an', 'لعان کا قانون', 'د لعان قانون'),
    ('The incident of ifk (the slander)', 'واقعہ اِفک', 'د افک پېښه'),
    ('Punishment for slander', 'تہمت کی سزا', 'د تور سزا'),
    ('Condemnation of shamelessness', 'بے حیائی کی مذمت', 'د بې‌حیایۍ غندنه'),
    ('Advice to the Muslims', 'مسلمانوں کو نصیحت', 'مسلمانانو ته نصیحت'),
    ('Etiquette of entering homes', 'گھر میں داخلے کے آداب', 'کور ته د ننوتلو آداب'),
    ('Veiling (purdah) and commands for the marriage of unmarried individuals', 'پردے اور بے نکاح افراد کے نکاح کے احکام', 'د پردې او د نا واده شویو کسانو د نکاح حکمونه'),
    ('Commands for protecting chastity and modesty', 'عفت و حیا کی حفاظت کے احکام', 'د عفت او حیا د ساتنې حکمونه'),
    ('The parable of the light of faith', 'نورِ ایمان کی تمثیل', 'د ایمان د نور مثال'),
    ('Qualities of the believers', 'اہلِ ایمان کے اوصاف', 'د مؤمنانو صفتونه'),
    ('The parable of the deeds of the disbelievers', 'کافروں کے اعمال کی تمثیل', 'د کافرانو د عملونو مثال'),
    ('Cosmic proofs of Tawhid', 'توحید پر آفاقی دلائل', 'پر توحید آفاقي دلیلونه'),
    ('Reproach of the hypocrites', 'منافقین پر گرفت', 'پر منافقانو نیونه'),
    ('The promise of khilafah on earth', 'خلافتِ ارضی کا وعدہ', 'په ځمکه کې د خلافت ژمنه'),
    ('Attaining guidance depends on obeying the Messenger (peace and blessings of Allah be upon him)', 'حصولِ ہدایت کا اطاعتِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر منحصر ہونا', 'د هدایت ترلاسه کول د رسول صلی الله علیه وعلی آله واصحابه وسلم پر اطاعت ولاړ دي'),
    ('The command to obey the Messenger (peace and blessings of Allah be upon him)', 'اطاعتِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کا حکم', 'د رسول صلی الله علیه وعلی آله واصحابه وسلم د اطاعت حکم'),
    ('Domestic life, persons with excuse', 'گھریلو معاشرت، معذور افراد', 'کورني ژوند، معذور کسان'),
    ('Relations of kinship with close people and relatives', 'قریبی لوگوں اور رشتہ داروں کے ساتھ صلہ رحمی کے تعلقات', 'له نږدې خلکو او خپلوانو سره د صله رحمۍ اړیکې'),
    ('Etiquette of the court of Messengership', 'بارگاہِ رسالت صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے آداب', 'د رسالت د دربار آداب'),
    ('Severe warning against deviating from obedience to the Messenger (peace and blessings of Allah be upon him)', 'اطاعتِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم سے انحراف پر سخت وعید', 'د رسول صلی الله علیه وعلی آله واصحابه وسلم له اطاعته د اوښتو پر سخت ګواښ'),
]


def p90():
    b = Builder()
    b.h('Lesson 9 — Surah al-Nur (verses 1 to 34)', 'سبق ۹ — سُوْرَةُ النُّوْرِ (آیات: ۱ تا ۳۴)', '۹ لوست — سورة النور (آیتونه ۱ تر ۳۴)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('In verse 35 of this surah it is stated that Allah Almighty is the Light of the heavens and the earth; with this connection its name is "Surah al-Nur". On the return from the battle of Banu Mustaliq, because of an incident that happened involuntarily, the Mother of the Believers Sayyidah \'A\'ishah Siddiqah (may Allah be pleased with her) was left behind the caravan, and on this basis the hypocrites slandered her chastity. The real aim of the hypocrites was to hurt the Noble Prophet, Khatam al-Nabiyyin (peace and blessings of Allah be upon him). Allah Almighty Himself refuted their accusation and, revealing verses on this in Surah al-Nur, bore witness to the innocence and purity of Sayyidah \'A\'ishah Siddiqah (may Allah be pleased with her). In the history of Islam this is called "the incident of ifk". In this surah not only was the innocence of Sayyidah \'A\'ishah (may Allah be pleased with her) declared, but the command of the hadd of qadhf was revealed for those who commit such an impure act, and the testimony of such people was rejected.', 'اس سورت کی آیت: ۳۵ میں بیان ہوا ہے کہ اللہ تعالیٰ آسمانوں اور زمین کا نور ہے، اسی مناسبت سے اس کا نام ”سُوْرَةُ النُّوْرِ“ ہے۔ غزوۂ بنی مصطلق سے واپسی پر غیر ارادی طور پر ایک پیش آنے والے واقعہ کی وجہ سے اُم المومنین سیدہ عائشہ صدیقہ رضی اللہ تعالیٰ عنہا قافلے سے پیچھے رہ گئیں اور اسی کو بنیاد بنا کر منافقین نے آپ رضی اللہ تعالیٰ عنہا کی عفت پر تہمت لگائی، منافقین کا اصل مقصد نبی کریم خاتم النبیین صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو ایذا پہنچانا تھا۔ اللہ تعالیٰ نے ان کے الزام کی خود تردید فرمائی اور سُوْرَةُ النُّوْرِ میں اس حوالے سے آیات نازل فرما کر سیدہ عائشہ صدیقہ رضی اللہ تعالیٰ عنہا کی برأت اور پاک دامنی کی گواہی دی۔ تاریخِ اسلام میں اسے ”واقعہ اِفک“ کہا جاتا ہے۔ اس سورت میں نہ صرف سیدہ عائشہ رضی اللہ تعالیٰ عنہا کی برأت بیان ہوئی بلکہ ایسی ناپاک حرکت کرنے والوں کے لیے حدِ قذف کا حکم نازل ہوا اور ان کی گواہی کو رد کیا گیا۔', 'د دې سورت په ۳۵ آیت کې بیان شوي چې الله تعالی د آسمانونو او ځمکې نور دی؛ له همدې نسبته یې نوم «سورة النور» دی. د بني مصطلق له غزا د راستنېدو پر مهال د یوې ناڅاپي پېښې له امله ام المؤمنین سیده عایشه صدیقه رضي الله تعالی عنها له کاروانه شاته پاتې شوه، او منافقانو همدا بنسټ ونیو او د هغې رضي الله تعالی عنها پر عفت یې تور ولګاوه؛ د منافقانو اصلي موخه نبي کریم خاتم النبیین صلی الله علیه وعلی آله واصحابه وسلم ته ځور رسول و. الله تعالی پخپله د هغوی تور رد کړ او په سورة النور کې یې په دې اړه آیتونه نازل کړل او د سیده عایشې صدیقې رضي الله تعالی عنها د برائت او پاکلمنۍ شاهدي یې ورکړه. د اسلام په تاریخ کې دې ته «د افک پېښه» ویل کېږي. په دې سورت کې نه یوازې د سیده عایشې رضي الله تعالی عنها برائت بیان شو، بلکې د داسې ناپاک کار کوونکو لپاره د قذف د حد حکم نازل شو او د هغوی شاهدي رد شوه.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Good dealings and social conduct', 'حُسنِ معاملات و معاشرت', 'ښه راکړه ورکړه او ټولنیز ژوند')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    S(b, [(('Points to note', 'قابلِ توجہ بات', 'د پام وړ خبره'),
           ('The believers were immensely delighted by the testimony of Allah Almighty concerning the pure life and character of the Mother of the Believers Sayyidah \'A\'ishah Siddiqah (may Allah be pleased with her). On the other side the storm raised by the hypocrites also settled down like foam.', 'اہلِ ایمان کو اُم المومنین سیدہ عائشہ صدیقہ رضی اللہ تعالیٰ عنہا کی پاکیزہ سیرت و کردار کے بارے میں اللہ تعالیٰ کی گواہی پر بے پناہ خوشی ہوئی۔ دوسری طرف منافقین کا اٹھایا ہوا طوفان بھی جھاگ کی طرح بیٹھ گیا۔', 'مؤمنانو ته د ام المؤمنین سیده عایشې صدیقې رضي الله تعالی عنها د پاکې سیرت او کردار په اړه د الله تعالی پر شاهدۍ بې‌حده خوښي وشوه؛ له بلې خوا د منافقانو پورته کړی توپان هم د ځګ په څېر کېناست.')),
          (None, ('Here this matter too should become well clear: even before the revelation of these verses this accusation was a major sin, but after the revelation of these verses, if even today any person says some improper thing regarding the dignity of the noble Prophets (peace be upon them), the Ahl al-Bayt (may Allah be pleased with them), the noble Companions (may Allah be pleased with them) and the saints (may Allah have mercy on them), then along with insolence towards these holy personalities the denial of the verses of Allah Almighty also follows. (We seek refuge in Allah.)', 'یہاں یہ بات بھی اچھی طرح واضح ہو جانا چاہیے کہ ان آیات کے نزول سے قبل بھی یہ الزام گناہ کبیرہ تھا لیکن ان آیات کے نزول کے بعد اگر آج بھی کوئی شخص انبیاءِ کرام علیہم السلام، اہلِ بیت اطہار رضی اللہ تعالیٰ عنہم، صحابہ کرام رضی اللہ تعالیٰ عنہم اور اولیاءِ کرام رحمۃ اللہ علیہم کی شان میں کوئی نازیبا بات کہے تو اس سے ان مقدس ہستیوں کی شان میں گستاخی کے ساتھ ساتھ اللہ تعالیٰ کی آیات کی تکذیب بھی لازم آتی ہے۔ (معاذ اللہ)', 'دلته دا خبره هم باید ښه روښانه شي چې د دې آیتونو له نزول مخکې هم دا تور کبیره ګناه وه، خو د دې آیتونو له نزول وروسته که نن هم څوک د انبیاوو علیهم السلام، د پاکو اهل بیتو رضي الله تعالی عنهم، د صحابه کرامو رضي الله تعالی عنهم او د اولیاوو رحمهم الله په شان کې کومه ناوړه خبره وکړي، نو د دې سپېڅلو شخصیتونو په شان کې له بې‌ادبۍ سره سره د الله تعالی د آیتونو تکذیب هم لازمېږي. (معاذ الله)'))])
    BOOK.save(90, [(9, rec(b, 9, 90, 90, first=True))], issues=[{'id': 'mq12-pdf090', 'unit': 9, 'printedPage': 87,
               'description': 'The 22 basic themes of Surah al-Nur (whole surah) are printed as a run-on numbered paragraph; rendered as a list.'}])


if __name__ == '__main__':
    p90()
