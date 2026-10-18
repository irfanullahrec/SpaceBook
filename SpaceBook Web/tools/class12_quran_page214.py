"""Mutalia-e-Quran XII PDF214: p.211 — Surah al-Taghabun (1–18): naming and introduction, central theme, basic themes; surah heading; verse 64:1 (64:2 begins at the foot; recorded with p.212). Run: python class12_quran_page214.py"""
from class12_quran_common import BOOK, Builder, rec, S, L, V

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Sanctification and praise of Allah Almighty; His greatness and attributes', 'اللہ تعالیٰ کی تقدیس و تحمید، اس کی عظمت اور صفات', 'د الله تعالی تقدیس او حمد، د هغه عظمت او صفتونه'),
    ('Mention of the purposeful creation of man and the universe', 'انسان اور کائنات کی بامقصد تخلیق کا ذکر', 'د انسان او کائنات د موخه‌لرونکي پیدایښت یادونه'),
    ('Belief in Prophethood and the Hereafter', 'رسالت اور آخرت پر ایمان', 'پر رسالت او آخرت ایمان'),
    ('The objection of the deniers to the messengers', 'رسولوں پر منکرین کا اعتراض', 'پر رسولانو د منکرانو اعتراض'),
    ('Warning of grave consequences to the deniers of Prophethood and the Hereafter', 'رسالت اور آخرت کے منکرین کو سنگین نتائج کی وعید', 'د رسالت او آخرت منکرانو ته د سختو پایلو ګواښ'),
    ('Appearance in the presence of Allah Almighty for accountability of deeds', 'اعمال کی جواب دہی کے لیے اللہ تعالیٰ کے حضور پیشی', 'د عملونو د ځواب‌ورکولو لپاره د الله تعالی حضور ته وړاندې کېدل'),
    ('The call to believe in Allah Almighty, His Messenger (peace and blessings of Allah be upon him) and the Qur\'an-e-Hakim', 'اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم اور قرآنِ حکیم پر ایمان لانے کی دعوت', 'پر الله تعالی، د هغه پر رسول صلی الله علیه وعلی آله واصحابه وسلم او قرآن حکیم د ایمان راوړلو بلنه'),
    ('The good end of those who accept the call to faith', 'دعوتِ ایمان قبول کرنے والوں کا عمدہ انجام', 'د ایمان د بلنې منونکو ښه پایله'),
    ('The evil end of those who do not accept the call to faith', 'دعوتِ ایمان قبول نہ کرنے والوں کا برا انجام', 'د ایمان د بلنې نه منونکو بده پایله'),
    ('The effects of faith on individual life', 'فرد کی ذاتی زندگی پر ایمان کے اثرات', 'د فرد پر شخصي ژوند د ایمان اغېزې'),
    ('The effects on afflictions of perfect faith in and reliance on Allah Almighty', 'مصائب میں اللہ تعالیٰ پر کامل ایمان اور بھروسہ رکھنا', 'په مصیبتونو کې پر الله تعالی بشپړ ایمان او توکل ساتل'),
    ('Emphasis on obeying Allah Almighty and His Messenger (peace and blessings of Allah be upon him)', 'اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت کی تاکید', 'د الله تعالی او د هغه د رسول صلی الله علیه وعلی آله واصحابه وسلم د اطاعت ټینګار'),
    ('Declaring the Messenger of Allah (peace and blessings of Allah be upon him) absolved of responsibility towards the deniers', 'منکرین سے رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو بری الذمہ قرار دینا', 'له منکرانو څخه د رسول الله صلی الله علیه وعلی آله واصحابه وسلم بري‌الذمه ګرځول'),
    ('The effects of faith on the individual\'s outlook concerning wife and children', 'بیوی بچوں کے بارے میں فرد کے نقطۂ نظر پر ایمان کے اثرات', 'د مېرمنې او ماشومانو په اړه د فرد پر لیدلوري د ایمان اغېزې'),
    ('Declaring wealth and children a trial for man', 'انسان کے لیے مال اور اولاد آزمائش قرار', 'د انسان لپاره مال او اولاد ازموینه ګرځول'),
    ('The call to fulfil the demands of faith', 'ایمان کے تقاضے ادا کرنے کی دعوت', 'د ایمان د غوښتنو د پوره کولو بلنه'),
    ('The command to adopt piety, to hear and obey', 'تقویٰ اختیار کرنے، سمع و طاعت کا حکم', 'د تقوا د غوره کولو، اورېدو او اطاعت حکم'),
    ('Mention of the reward of those who avoid miserliness and spend in the way of Allah', 'بخل سے بچنے اور انفاق فی سبیل اللہ کرنے والوں کے اجر کا ذکر', 'له بخل د ډډې او د الله په لار کې د لګښت کوونکو د اجر یادونه'),
    ('A statement of Tawhid and the attributes of the Exalted Lord', 'توحید و صفاتِ باری تعالیٰ کا بیان', 'د توحید او د باري تعالی د صفتونو بیان'),
]


def p214():
    b = Builder()
    b.h('Surah al-Taghabun (verses 1 to 18)', 'سُوْرَةُ التَّغَابُنِ (آیات: ۱ تا ۱۸)', 'سورة التغابن (آیتونه ۱ تر ۱۸)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('The name of this surah is taken from verse 9. The Day of Resurrection has been called "yawm al-taghabun". "Taghabun" comes from "ghabn", which means loss and damage. The literal meaning of "taghabun" is causing loss to someone. Ghabn is used for financial loss as well as for loss of opinion and intellect. In this way, on the Day of Resurrection everyone will regret their shortcomings and will feel the loss of deficiency in deeds; that is why that day has been called "yawm al-taghabun". According to the opinion of most commentators this surah was revealed probably in the early Madani period after the Holy Prophet (peace and blessings of Allah be upon him) emigrated to Madinah Munawwarah. However, according to some commentators its last three verses are Madani and the rest are Makki.',
            'اس سورت کا نام آیت: ۹ سے ماخوذ ہے۔ قیامت کے دن کو "يَوْمُ التَّغَابُنِ" کہا گیا ہے۔ "تَغَابُنٌ" غَبَنٌ سے نکلا ہے جس کے معنی خسارہ اور نقصان کے ہیں۔ "تَغَابُنٌ" کے لغوی معنیٰ ہیں کسی کو نقصان پہنچانا۔ غبن مالی نقصان کو بھی کہتے ہیں اور رائے اور عقل کے نقصان کو بھی۔ اس طرح قیامت کے روز سبھی اپنی اپنی کوتاہی پر نادم اور عمل کی کمی پر خسارہ کا احساس کریں گے اس لیے اس دن کو "يَوْمُ التَّغَابُنِ" کہا گیا ہے۔ اکثر مفسرین کرام کی رائے کے مطابق یہ سورت نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی مدینہ منورہ ہجرت فرمانے کے بعد غالباً ابتدائی مدنی دور میں نازل ہوئی۔ البتہ کچھ مفسرین کرام کے مطابق آخری تین آیات مدنی ہیں اور باقی مکی ہیں۔',
            'د دې سورت نوم له ۹ آیت څخه اخیستل شوی. د قیامت ورځ ته «یوم التغابن» ویل شوي. «تغابن» له «غبن» څخه راوتلی چې مانا یې زیان او تاوان دی. د «تغابن» لغوي مانا چا ته زیان رسول دي. غبن مالي زیان ته هم ویل کېږي او د رایې او عقل زیان ته هم. په دې توګه به د قیامت په ورځ ټول پر خپلو کمزوریو پښېمانه وي او د عمل پر کمښت به د زیان احساس کوي، له همدې امله هغې ورځې ته «یوم التغابن» ویل شوي. د ډېرو مفسرینو د رایې له مخې دا سورت مدینې منورې ته د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم له هجرت وروسته احتمالاً په لومړني مدني پړاو کې نازل شوی؛ خو د ځینو مفسرینو په وینا وروستي درې آیتونه مدني او پاتې یې مکي دي.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('A statement of the articles of faith (Tawhid, Prophethood and the Hereafter)', 'ایمانیات (توحید، رسالت اور آخرت) کا بیان', 'د ایماني عقیدو (توحید، رسالت او آخرت) بیان')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    b.h('Surah al-Taghabun (64) — Madani; order of revelation 108; verses 18, sections 2', 'سُوْرَةُ التَّغَابُنِ ۶۴ — مَدَنِيَّةٌ ۱۰۸ — اٰیَاتُهَا ۱۸، رُکُوْعَاتُهَا ۲', 'سورة التغابن (۶۴) — مدني؛ د نزول ترتیب ۱۰۸؛ آیتونه ۱۸، رکوعونه ۲')
    b.p('بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nIn the name of Allah, the Beneficent, the Merciful.', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nاللہ کے نام سے شروع جو بڑا مہربان نہایت رحم فرمانے والا ہے', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nد الله په نوم پیل چې ډېر مهربان، بې‌حده رحم کوونکی دی')
    b.paras[-1]['arabicSource'] = True
    V(b, 64, 1, 'اللہ کی تسبیح کرتی ہے ہر وہ چیز جو آسمانوں میں ہے اور جو زمینوں میں ہے اسی کے لیے بادشاہی ہے اور اسی کے لیے تمام تعریفیں ہیں اور وہ ہر چیز پر بڑی قدرت والا ہے۔',
      'د الله تسبیح وايي هر هغه شی چې په آسمانونو کې دی او چې په ځمکو کې دی؛ پاچاهي د هماغه ده او ټولې ستاینې د هماغه دي؛ او هغه پر هر شي لوی قدرت لرونکی دی.')
    BOOK.save(214, [(23, rec(b, 23, 214, 214))], issues=[{'id': 'mq12-pdf214', 'unit': 23, 'printedPage': 211,
               'description': 'Nineteen basic themes of al-Taghabun printed as a run-on numbered paragraph; rendered as a list. Surah cartouche: al-Taghabun 64, Madaniyyah 108, ayat 18, ruku 2. Verse 64:2 begins on the last line of p.211 and is recorded with p.212.'}])


if __name__ == '__main__':
    p214()
