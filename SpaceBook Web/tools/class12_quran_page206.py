"""Mutalia-e-Quran XII PDF206: p.203 — al-Saff knowledge point 3; Surah al-Jumu'ah (1–11): naming and introduction, excellence box, central theme, basic themes; surah heading; verses 62:1–2. Run: python class12_quran_page206.py"""
from class12_quran_common import BOOK, Builder, rec, S, L, V

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Glorification and sanctification of Allah Almighty', 'اللہ تعالیٰ کی تسبیح و تقدیس', 'د الله تعالی تسبیح او تقدیس'),
    ('A statement of the attributes of the Exalted Lord', 'صفاتِ باری تعالیٰ کا بیان', 'د باري تعالی د صفتونو بیان'),
    ('Proof of the power of the Exalted Lord', 'قدرتِ باری تعالیٰ کی دلیل', 'د باري تعالی د قدرت دلیل'),
    ('Mention of the sending of the Holy Messenger (peace and blessings of Allah be upon him) and of his four duties of messengership', 'رسول اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی بعثت اور آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے چار فرائضِ رسالت کا تذکرہ', 'د رسول اکرم صلی الله علیه وعلی آله واصحابه وسلم د بعثت او د هغه د رسالت د څلورو فرایضو یادونه'),
    ('The turning away of the Jews from the Torah', 'تورات سے یہود کا اعراض', 'له تورات د یهودو مخ اړول'),
    ('Severe reproach of the false claims and evil deeds of the Jews', 'یہود کے غلط دعوؤں اور برے اعمال پر سخت ملامت', 'د یهودو پر ناسمو دعوو او بدو عملونو سخته ملامتیا'),
    ('Emphasis on the Friday prayer and its commands', 'نمازِ جمعہ کی تاکید اور اس کے احکام', 'د جمعې د لمانځه ټینګار او د هغه حکمونه'),
]


def p206():
    b = Builder()
    L(b, [('Allah Almighty helps the people of faith against the disbelievers, and in the end grants supremacy to the people of faith alone. Therefore in changing circumstances the people of faith should not despair, and trusting in the promises of Allah Almighty they should keep using their life, wealth and other abilities for the supremacy of the true religion.', 'اللہ تعالیٰ ایمان والوں کی کفار کے مقابلہ میں مدد فرماتا ہے اور غلبہ بالآخر اہلِ ایمان کو ہی عطا فرماتا ہے۔ چنانچہ بدلتے حالات میں اہلِ ایمان کو مایوس نہیں ہونا چاہیے اور اللہ تعالیٰ کے وعدوں پر یقین رکھتے ہوئے غلبۂ دینِ حق کے لیے اپنی جان و مال اور دیگر صلاحیتوں کو استعمال کرتے رہنا چاہیے۔', 'الله تعالی د کافرانو په مقابل کې د مؤمنانو مرسته کوي او بالاخره غلبه یوازې مؤمنانو ته ورکوي؛ نو په بدلېدونکو حالاتو کې مؤمنان باید مایوسه نه شي، او د الله تعالی پر وعدو باور سره د حق دین د غلبې لپاره خپل ځان، مال او نور وړتیاوې کاروي.')])
    b.h('Surah al-Jumu\'ah (verses 1 to 11)', 'سُوْرَةُ الْجُمُعَةِ (آیات: ۱ تا ۱۱)', 'سورة الجمعه (آیتونه ۱ تر ۱۱)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('In this surah the Friday prayer is mentioned, so its name has been kept Surah al-Jumu\'ah. Surah al-Jumu\'ah has three basic parts. In the first part, in connection with the sending, the messengership of the Holy Prophet (peace and blessings of Allah be upon him) is stated. In the second part the misdeeds of the Bani Isra\'il are mentioned, and in the third part the Friday prayer is stated. It is narrated from Sayyiduna Jabir ibn \'Abdullah (may Allah be pleased with them both) that we were offering prayer with the Holy Prophet (peace and blessings of Allah be upon him) (and listening to the Friday sermon) when meanwhile a trade caravan laden with grain passed by. People went off towards it; with the Holy Prophet (peace and blessings of Allah be upon him) no one remained except a total of twelve (12) men. (Sahih Bukhari: 936)',
            'اس سورت میں جمعہ کی نماز کا ذکر ہے اس لیے اس کا نام سُوْرَةُ الْجُمُعَةِ رکھا گیا ہے۔ سُوْرَةُ الْجُمُعَةِ کے تین بنیادی حصے ہیں۔ پہلے حصے میں بعثت کے ضمن میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی رسالت کا بیان ہے۔ دوسرے حصے میں بنی اسرائیل کی بداعمالیوں کا تذکرہ ہے اور تیسرے حصے میں نمازِ جمعہ کا بیان ہے۔ سیدنا جابر بن عبداللہ رضی اللہ تعالیٰ عنہما سے روایت ہے کہ ہم نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے ساتھ نماز پڑھ (کر خطبۂ جمعہ سن) رہے تھے کہ اتنے میں سے ایک تجارتی قافلہ غلہ لادے ہوئے ادھر سے گزرا۔ لوگ اس کی طرف چل دیے، نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے ساتھ کل بارہ (۱۲) آدمیوں کے سوا کوئی نہ بچا۔ (صحیح بخاری: ۹۳۶)',
            'په دې سورت کې د جمعې د لمانځه یادونه ده، له همدې امله یې نوم سورة الجمعه ایښودل شوی. د سورة الجمعه درې بنسټیزې برخې دي: په لومړۍ برخه کې د بعثت په ترڅ کې د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د رسالت بیان دی؛ په دویمه برخه کې د بني اسرائیلو د بدو عملونو یادونه ده؛ او په درېیمه برخه کې د جمعې د لمانځه بیان دی. له سیدنا جابر بن عبدالله رضي الله عنهما روایت دی چې موږ له نبي کریم صلی الله علیه وعلی آله واصحابه وسلم سره لمونځ کاوه (او د جمعې خطبه مو اورېده) چې په همدې کې یو سوداګریز کاروان غله بار تېر شو؛ خلک ورپسې لاړل، او له نبي کریم صلی الله علیه وعلی آله واصحابه وسلم سره له ټولټال دولسو (۱۲) سړو پرته هېڅوک پاتې نه شول. (صحیح بخاري: ۹۳۶)'))])
    b.p('Excellence: "The Messenger (peace and blessings of Allah be upon him) used to recite Surah al-Jumu\'ah and Surah al-Munafiqun in the Friday prayer." (Sahih Muslim: 877)',
        'فضیلت: "رسول کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم جمعہ کی نماز میں سُوْرَةُ الْجُمُعَةِ اور سُوْرَةُ الْمُنَافِقُوْنَ تلاوت فرماتے تھے۔" (صحیح مسلم: ۸۷۷)',
        'فضیلت: «رسول کریم صلی الله علیه وعلی آله واصحابه وسلم به د جمعې په لمانځه کې سورة الجمعه او سورة المنافقون تلاوت کول.» (صحیح مسلم: ۸۷۷)')
    S(b, [(('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Mention of the sending of the Holy Prophet (peace and blessings of Allah be upon him) and of the duties of his office', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی بعثت اور فرائضِ منصبی کا ذکر', 'د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د بعثت او د منصب د فرایضو یادونه')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    b.h('Surah al-Jumu\'ah (62) — Madani; order of revelation 110; verses 11, sections 2', 'سُوْرَةُ الْجُمُعَةِ ۶۲ — مَدَنِيَّةٌ ۱۱۰ — اٰیَاتُهَا ۱۱، رُکُوْعَاتُهَا ۲', 'سورة الجمعه (۶۲) — مدني؛ د نزول ترتیب ۱۱۰؛ آیتونه ۱۱، رکوعونه ۲')
    b.p('بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nIn the name of Allah, the Beneficent, the Merciful.', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nاللہ کے نام سے شروع جو بڑا مہربان نہایت رحم فرمانے والا ہے', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nد الله په نوم پیل چې ډېر مهربان، بې‌حده رحم کوونکی دی')
    b.paras[-1]['arabicSource'] = True
    V(b, 62, 1, 'اللہ کی تسبیح کرتی ہے ہر وہ چیز جو آسمانوں میں ہے اور جو زمینوں میں ہے جو بادشاہ، ہر عیب سے پاک، بہت غالب، بڑی حکمت والا ہے۔',
      'د الله تسبیح وايي هر هغه شی چې په آسمانونو کې دی او چې په ځمکو کې دی؛ هغه چې پاچا، له هر عیب پاک، ډېر غالب، ډېر حکمتناک دی.')
    V(b, 62, 2, 'وہی (اللہ) ہے جس نے ان پڑھ لوگوں میں ان ہی میں سے ایک (عظمت والے) رسول کو بھیجا جو اُن پر اس (اللہ) کی آیات تلاوت کرتے ہیں اور اُن کا تزکیہ کرتے ہیں اور انھیں کتاب اور حکمت کی تعلیم دیتے ہیں جب کہ اس سے پہلے وہ لوگ یقیناً کھلی گم راہی میں تھے۔',
      'همغه (الله) دی چې په نالوستو خلکو کې یې له هماغوی څخه یو (عظمت لرونکی) رسول ولېږه چې پر هغوی د هغه (الله) آیتونه تلاوتوي، هغوی پاکوي، او هغوی ته د کتاب او حکمت ښوونه کوي، حال دا چې له دې مخکې هغوی یقیناً په ښکاره ګمراهۍ کې وو.')
    BOOK.save(206, [(22, rec(b, 22, 206, 206))], issues=[{'id': 'mq12-pdf206', 'unit': 22, 'printedPage': 203,
               'description': 'The third al-Saff knowledge point (top of p.203) is recorded here before the al-Jumu\'ah introduction. The "Fadilat" side box is rendered after the introduction. Surah cartouche: al-Jumu\'ah 62, Madaniyyah 110, ayat 11, ruku 2. The narration prints "کہ اتنے میں سے ایک تجارتی قافلہ" (kept).'}])


if __name__ == '__main__':
    p206()
