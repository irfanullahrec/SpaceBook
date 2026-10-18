"""Mutalia-e-Quran XII PDF189: p.186 — Lesson 20 Surah al-Hashr (1–24): naming and introduction, central theme, basic themes; surah heading; verse 59:1 (59:2 begins at the foot; recorded with p.187). Run: python class12_quran_page189.py"""
from class12_quran_common import BOOK, Builder, rec, S, L, V

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Glorification and sanctification of the Exalted Lord', 'تسبیح و تقدیسِ باری تعالیٰ', 'د باري تعالی تسبیح او تقدیس'),
    ('The state of the humiliating exile of the Banu Nadir', 'بنو نضیر کی ذلت آمیز جلاوطنی کا حال', 'د بنو نضیر د ذلیلې جلاوطنۍ حال'),
    ('Commands of mal-e-fay\' (wealth gained without fighting) and of obeying the Messenger of Allah (peace and blessings of Allah be upon him) in every circumstance', 'مالِ فے اور ہر حال میں رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت کے احکام', 'د مال فیء او په هر حال کې د رسول الله صلی الله علیه وعلی آله واصحابه وسلم د اطاعت حکمونه'),
    ('The virtues and merits of the Muhajirin and the Ansar', 'مہاجرین اور انصار کے فضائل و مناقب', 'د مهاجرینو او انصارو فضیلتونه او مناقب'),
    ('The excellence of the believers who come after the noble Companions (may Allah be pleased with them)', 'صحابہ کرام رضی اللہ عنہم کے بعد آنے والے مومنین کی فضیلت', 'له صحابه کرامو رضي الله عنهم وروسته د راتلونکو مؤمنانو فضیلت'),
    ('Reproach of the evil conduct of the hypocrites in the battle of Banu Nadir', 'غزوۂ بنی نضیر میں منافقین کے برے کردار پر گرفت', 'د بنو نضیر په غزا کې د منافقانو پر بد چلند نیونه'),
    ('The selfish relationship between the hypocrites and the Jews', 'منافقین اور یہود کا خود غرضی کا تعلق', 'د منافقانو او یهودو د ځان‌غوښتنې اړیکه'),
    ('Emphasis on the people of faith to avoid sinfulness and to adopt fear of God', 'اہلِ ایمان کو فسق سے بچنے اور خشیتِ الٰہی اختیار کرنے کی تاکید', 'مؤمنانو ته له فسق د ډډې او د الهي وېرې د غوره کولو ټینګار'),
    ('The greatness of the Qur\'an Majid', 'قرآن مجید کی عظمت', 'د قرآن مجید عظمت'),
    ('A statement of the Beautiful Names of Allah Almighty and His attributes', 'اللہ تعالیٰ کے اسماء الحسنیٰ اور اس کی صفات کا بیان', 'د الله تعالی د اسماء الحسنی او د هغه د صفتونو بیان'),
]


def p189():
    b = Builder()
    b.h('Lesson 20 — Surah al-Hashr (verses 1 to 24)', 'سبق ۲۰ — سُوْرَةُ الْحَشْرِ (آیات: ۱ تا ۲۴)', '۲۰ لوست — سورة الحشر (آیتونه ۱ تر ۲۴)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('The name of this surah is taken from the words "li-awwali al-hashr" present in its second verse. "Hashr" means gathering together scattered individuals, or gathering scattered individuals to remove them from some place or to exile them. For this reason its name has been kept "Surah al-Hashr". The second name of this surah is also "Surah Bani al-Nadir", because in this surah the Jewish tribe of Banu Nadir is mentioned. All the members of the Jewish tribe of Banu Nadir were driven out of their homes with disgrace and humiliation and exiled from Madinah Munawwarah. Surah al-Hashr was revealed against the background of the event of the exile of the Banu Nadir. In it the basic reasons for the battle of Banu Nadir have been stated. Despite all their resources their exile was humiliating, and until the end of the world they were made a sign of warning for opposing and insulting the Holy Messenger (peace and blessings of Allah be upon him) and for conspiring against him.',
            'اس سورت کا نام اس کی دوسری آیت میں موجود الفاظ "لِاَوَّلِ الْحَشْرِ" سے ماخوذ ہے۔ "حَشْرٌ" کے معنی ہیں منتشر افراد کو اکٹھا کرنا یا بکھرے ہوئے افراد کو کسی جگہ سے نکالنے یا جلاوطن کرنے کے لیے اکٹھا کرنا۔ اسی وجہ سے اس کا نام "سُوْرَةُ الْحَشْرِ" رکھا گیا ہے۔ اس سورت کا دوسرا نام "سُوْرَةُ بَنِي النَّضِيْرِ" بھی ہے کیوں کہ اس سورت میں یہود کے قبیلہ بنو نضیر کا ذکر ہے۔ یہود کے قبیلہ بنو نضیر کے تمام افراد کو ان کے گھروں سے نکال کر ذلت و رسوائی کے ساتھ مدینہ منورہ سے جلاوطن کیا گیا۔ سُوْرَةُ الْحَشْرِ بنو نضیر کی جلاوطنی کے واقعہ کے پس منظر میں نازل ہوئی۔ اس میں غزوۂ بنی نضیر کی بنیادی وجوہات بیان ہوئی ہیں۔ تمام تر وسائل کے باوجود ان کی ذلت آمیز جلاوطنی ہوئی اور رہتی دنیا تک انھیں رسول کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی مخالفت و توہین اور آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے خلاف سازش کرنے پر نشانِ عبرت بنا دیا گیا۔',
            'د دې سورت نوم د هغه په دویم آیت کې د موجودو کلمو «لاول الحشر» څخه اخیستل شوی. «حشر» مانا ده خپاره کسان راټولول، یا خپاره شوي کسان له کوم ځایه د ایستلو یا جلاوطنولو لپاره راټولول؛ له همدې امله یې نوم «سورة الحشر» ایښودل شوی. د دې سورت دویم نوم «سورة بني النضیر» هم دی، ځکه په دې سورت کې د یهودو د بنو نضیر قبیلې یادونه ده. د یهودو د بنو نضیر قبیلې ټول کسان له خپلو کورونو وویستل شول او په ذلت او رسوایۍ له مدینې منورې جلاوطنه شول. سورة الحشر د بنو نضیر د جلاوطنۍ د پېښې په شالید کې نازل شو؛ په دې کې د بنو نضیر د غزا بنسټیز لاملونه بیان شوي. د ټولو وسایلو سره سره د هغوی ذلیله جلاوطني وشوه، او د رسول کریم صلی الله علیه وعلی آله واصحابه وسلم د مخالفت، سپکاوي او د هغه پر خلاف د دسیسو له امله د نړۍ تر پایه د عبرت نښه وګرځول شول.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('The importance of following the Holy Messenger (peace and blessings of Allah be upon him) and the end of rebellion', 'اتباعِ رسول کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اہمیت اور سرکشی کا انجام', 'د رسول کریم صلی الله علیه وعلی آله واصحابه وسلم د پیروۍ اهمیت او د سرکشۍ پایله')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    b.h('Surah al-Hashr (59) — Madani; order of revelation 101; verses 24, sections 3', 'سُوْرَةُ الْحَشْرِ ۵۹ — مَدَنِيَّةٌ ۱۰۱ — اٰیَاتُهَا ۲۴، رُکُوْعَاتُهَا ۳', 'سورة الحشر (۵۹) — مدني؛ د نزول ترتیب ۱۰۱؛ آیتونه ۲۴، رکوعونه ۳')
    b.p('بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nIn the name of Allah, the Beneficent, the Merciful.', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nاللہ کے نام سے شروع جو بڑا مہربان نہایت رحم فرمانے والا ہے', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nد الله په نوم پیل چې ډېر مهربان، بې‌حده رحم کوونکی دی')
    b.paras[-1]['arabicSource'] = True
    V(b, 59, 1, 'اللہ کی تسبیح کی ہر اس چیز نے جو آسمانوں میں ہے اور جو زمینوں میں ہے اور وہی بہت غالب بڑی حکمت والا ہے۔',
      'د الله تسبیح یې ووېله هر هغه شي چې په آسمانونو کې دی او چې په ځمکو کې دی؛ او همغه ډېر غالب، ډېر حکمتناک دی.')
    BOOK.save(189, [(20, rec(b, 20, 189, 189, first=True))], issues=[{'id': 'mq12-pdf189', 'unit': 20, 'printedPage': 186,
               'description': 'Lesson 20 heading: Surah al-Hashr, verses 1 to 24. Ten basic themes printed as a run-on numbered paragraph; rendered as a list. Surah cartouche: al-Hashr 59, Madaniyyah 101, ayat 24, ruku 3. Verse 59:2 begins on the last two lines of p.186 and is recorded with p.187.'}])


if __name__ == '__main__':
    p189()
