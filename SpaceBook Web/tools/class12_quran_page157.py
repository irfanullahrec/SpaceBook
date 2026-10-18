"""Mutalia-e-Quran XII PDF157: p.154 — Lesson 16 Surah al-Fath (1–29): naming and introduction, occasion of revelation, central theme, basic themes; surah heading; verses 48:1–3. Run: python class12_quran_page157.py"""
from class12_quran_common import BOOK, Builder, rec, S, L, V

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Mention of the Treaty of Hudaybiyah', 'صلح حدیبیہ کا تذکرہ', 'د حدیبیې د سولې یادونه'),
    ('Rewards upon the believers', 'مومنین پر انعامات', 'پر مؤمنانو انعامونه'),
    ('Punishment for the hypocrites and the polytheists', 'منافقین اور مشرکین کے لیے عذاب', 'د منافقانو او مشرکانو لپاره عذاب'),
    ('The excellence and status of messengership, i.e. the emphatic command to show reverence and honour to the Prophet (peace and blessings of Allah be upon him)', 'فضیلت و شانِ رسالت یعنی آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی تعظیم و توقیر بجا لانے کا تاکیدی حکم', 'د رسالت فضیلت او شان، یعنې د هغه صلی الله علیه وعلی آله واصحابه وسلم د تعظیم او درناوي ټینګار شوی حکم'),
    ('The hand of mercy and power of Allah Almighty being over those who pledged allegiance at the blessed hand of the Prophet (peace and blessings of Allah be upon him)', 'آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے دستِ مبارک پر بیعت کرنے والوں پر اللہ تعالیٰ کے دستِ رحمت اور قدرت کا ہونا', 'د هغه صلی الله علیه وعلی آله واصحابه وسلم په مبارک لاس بیعت کوونکو د الله تعالی د رحمت او قدرت لاس'),
    ('The excuses, pretexts and misgivings of the hypocrites', 'منافقین کے حیلے بہانے اور بدگمانیاں', 'د منافقانو چلونه، پلمې او بدګومانۍ'),
    ('Severe reproach of the hypocritical role of the hypocrites', 'منافقین کے منافقانہ کردار پر سخت گرفت', 'د منافقانو پر منافقانه کړنو سخته نیونه'),
    ('A statement of Bay\'at al-Ridwan', 'بیعتِ رضوان کا بیان', 'د رضوان د بیعت بیان'),
    ('Conquests', 'فتوحات', 'بریاوې'),
    ('Glad tidings of spoils of war', 'غنیمتوں کی بشارت', 'د غنیمتونو زېری'),
    ('The supremacy of the Muslims over the polytheists', 'مشرکین پر مسلمانوں کا غلبہ', 'پر مشرکانو د مسلمانانو غلبه'),
    ('The wisdom of not fighting on the occasion of the Treaty of Hudaybiyah', 'صلح حدیبیہ کے موقع پر قتال نہ ہونے کی مصلحت', 'د حدیبیې د سولې پر مهال د جګړې نه کېدو مصلحت'),
    ('Confirmation of the dream of the Holy Prophet (peace and blessings of Allah be upon him)', 'نبی اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے خواب کی تصدیق', 'د نبي اکرم صلی الله علیه وعلی آله واصحابه وسلم د خوب تصدیق'),
    ('The purpose of the sending of the Prophet (peace and blessings of Allah be upon him)', 'آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کا مقصدِ بعثت', 'د هغه صلی الله علیه وعلی آله واصحابه وسلم د بعثت موخه'),
    ('The status of the Seal of the Messengers (peace and blessings of Allah be upon him)', 'شانِ خاتم الرسل صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم', 'د خاتم الرسل صلی الله علیه وعلی آله واصحابه وسلم شان'),
    ('The favours of the Exalted Lord upon the Prophet (peace and blessings of Allah be upon him)', 'آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر انعاماتِ باری تعالیٰ', 'پر هغه صلی الله علیه وعلی آله واصحابه وسلم د باري تعالی انعامونه'),
]


def p157():
    b = Builder()
    b.h('Lesson 16 — Surah al-Fath (verses 1 to 29)', 'سبق ۱۶ — سُوْرَةُ الْفَتْحِ (آیات: ۱ تا ۲۹)', '۱۶ لوست — سورة الفتح (آیتونه ۱ تر ۲۹)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('In the first verse of this surah it is said: "Indeed, We have granted you (O Prophet, peace and blessings of Allah be upon him) a clear victory." In this verse the Treaty of Hudaybiyah has been declared a "clear victory". The Holy Messenger (peace and blessings of Allah be upon him) and the Muslims were given the glad tidings of this victory. With this connection the name of this surah has been kept Surah al-Fath. Surah al-Fath is a Madani surah.',
            'اس سورت کی پہلی آیت میں فرمایا گیا ہے کہ اِنَّا فَتَحْنَا لَكَ فَتْحًا مُّبِيْنًا "بے شک ہم نے آپ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) کو کھلی فتح عطا فرمائی۔" اس آیت میں صلح حدیبیہ کو "فتحِ مبین" قرار دیا گیا ہے۔ رسول اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم اور مسلمانوں کو اس فتح کی بشارت دی ہے۔ اسی مناسبت سے اس سورت کا نام سُوْرَةُ الْفَتْحِ رکھا گیا ہے۔ سُوْرَةُ الْفَتْحِ مدنی سورت ہے۔',
            'د دې سورت په لومړي آیت کې ویل شوي: «بې‌شکه موږ تاسو (صلی الله علیه وعلی آله واصحابه وسلم) ته ښکاره بریا درکړه.» په دې آیت کې د حدیبیې سوله «ښکاره بریا» ګرځول شوې. رسول اکرم صلی الله علیه وعلی آله واصحابه وسلم او مسلمانانو ته د دې بریا زېری ورکړل شوی. په همدې مناسبت د دې سورت نوم سورة الفتح ایښودل شوی. سورة الفتح مدني سورت دی.')),
          (('Occasion of revelation', 'شانِ نزول', 'د نزول شالید'),
           ('Its revelation took place in 6 AH at the time when the Prophet (peace and blessings of Allah be upon him), after making a treaty with the disbelievers on a few conditions at the place of Hudaybiyah, was returning to Madinah Munawwarah. In the history of Islam this treaty is called the "Treaty of Hudaybiyah". This surah was revealed against the background of this event. Since the Muslims were returning without performing \'Umrah, and from some conditions too it apparently seemed that the Muslims had to make peace by yielding, therefore their hearts were grieved and they were exhausted by the intensity of sorrow. To console the Muslims, Allah Almighty, at the very beginning of this surah, announced a very great glad tidings: that in the form of the treaty Allah Almighty has granted Sayyiduna Hazrat Muhammad, the Messenger of Allah, the Seal of the Prophets (peace and blessings of Allah be upon him and his family and companions) a magnificent victory. With the revelation of this surah the hearts of the Muslims became completely satisfied and at peace.',
            'اس کا نزول ۶ھ میں اُس وقت ہوا جب آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم حدیبیہ کے مقام پر کفار سے چند شرائط پر معاہدہ کرنے کے بعد مدینہ منورہ واپس تشریف لا رہے تھے۔ یہ معاہدہ تاریخِ اسلام میں "صلح حدیبیہ" کہلاتا ہے۔ یہ سورت اسی واقعہ کے پس منظر میں نازل ہوئی۔ چونکہ مسلمان عمرہ ادا کیے بغیر واپس آ رہے تھے اور بعض شرائط سے بھی بظاہر ایسا لگ رہا تھا کہ مسلمانوں کو دب کر صلح کرنی پڑی ہے اس لیے وہ دل گرفتہ اور شدتِ غم سے نڈھال تھے۔ اللہ تعالیٰ نے مسلمانوں کی دل جوئی کے لیے خصوصی طور پر اس سورت کے آغاز ہی میں ایک بہت بڑی خوش خبری کا اعلان فرمایا کہ صلح نامہ کی شکل میں اللہ تعالیٰ نے سیدنا حضرت مُحَمَّدٌ رَّسُوْلُ اللهِ خَاتَمُ النَّبِيِّيْنَ صَلَّى اللهُ عَلَيْهِ وَعَلٰی آلِهِ وَأَصْحَابِهِ وَسَلَّمَ کو ایک عظیم الشان فتح عطا فرمائی ہے۔ اس سورت کے نازل ہونے سے مسلمانوں کے دل مکمل طور پر مطمئن اور پرسکون ہو گئے۔',
            'د دې نزول په ۶ هجري کې هغه مهال وشو چې هغه صلی الله علیه وعلی آله واصحابه وسلم د حدیبیې په ځای له کافرانو سره پر ځینو شرطونو له تړون وروسته مدینې منورې ته راستنېده. دا تړون د اسلام په تاریخ کې «د حدیبیې سوله» بلل کېږي. دا سورت د همدې پېښې په شالید کې نازل شو. څرنګه چې مسلمانان له عمرې پرته راستنېدل او له ځینو شرطونو هم داسې ښکارېده چې مسلمانانو د کمزورۍ له مخې سوله منلې، نو زړه‌ماتي او له ډېر غم ستړي وو. الله تعالی د مسلمانانو د زړه‌ښه‌والي لپاره په ځانګړي ډول د دې سورت په پیل کې یو ډېر لوی زېری اعلان کړ چې د سولې لیک په بڼه الله تعالی سیدنا حضرت محمد رسول الله خاتم النبیین صلی الله علیه وعلی آله واصحابه وسلم ته یوه ستره بریا ورکړې ده. د دې سورت په نازلېدو سره د مسلمانانو زړونه بشپړ ډاډه او ارام شول.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Glad tidings of the supremacy of Islam', 'غلبۂ اسلام کی نوید', 'د اسلام د غلبې زېری')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    b.h('Surah al-Fath (48) — Madani; order of revelation 111; verses 29, sections 4', 'سُوْرَةُ الْفَتْحِ ۴۸ — مَدَنِيَّةٌ ۱۱۱ — اٰیَاتُهَا ۲۹، رُکُوْعَاتُهَا ۴', 'سورة الفتح (۴۸) — مدني؛ د نزول ترتیب ۱۱۱؛ آیتونه ۲۹، رکوعونه ۴')
    b.p('بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nIn the name of Allah, the Beneficent, the Merciful.', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nاللہ کے نام سے شروع جو بڑا مہربان نہایت رحم فرمانے والا ہے', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nد الله په نوم پیل چې ډېر مهربان، بې‌حده رحم کوونکی دی')
    b.paras[-1]['arabicSource'] = True
    V(b, 48, 1, 'بے شک ہم نے آپ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) کو کھلی فتح عطا فرمائی۔',
      'بې‌شکه موږ تاسو (صلی الله علیه وعلی آله واصحابه وسلم) ته ښکاره بریا درکړه.')
    V(b, 48, 2, 'تاکہ اللہ آپ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) کے لیے آپ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) کے اگلے اور پچھلے (بظاہر) خلافِ اولیٰ سب کام معاف فرمائے اور وہ آپ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) پر اپنی نعمت مکمل فرمائے اور آپ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) کو سیدھے راستہ پر ثابت قدم رکھے۔',
      'تر څو الله ستاسو (صلی الله علیه وعلی آله واصحابه وسلم) لپاره ستاسو (صلی الله علیه وعلی آله واصحابه وسلم) مخکیني او وروستني (ظاهراً) خلاف اولی ټول کارونه وبښي، او پر تاسو (صلی الله علیه وعلی آله واصحابه وسلم) خپل نعمت پوره کړي، او تاسو (صلی الله علیه وعلی آله واصحابه وسلم) پر سمه لار ثابت قدم وساتي.')
    V(b, 48, 3, 'اور (تاکہ) اللہ آپ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) کی زبردست مدد فرمائے۔',
      'او (تر څو) الله ستاسو (صلی الله علیه وعلی آله واصحابه وسلم) زوروره مرسته وکړي.')
    BOOK.save(157, [(16, rec(b, 16, 157, 157, first=True))], issues=[{'id': 'mq12-pdf157', 'unit': 16, 'printedPage': 154,
               'description': 'Lesson 16 heading: Surah al-Fath, verses 1 to 29. Sixteen basic themes printed as a run-on numbered paragraph; rendered as a list. Surah cartouche: al-Fath 48, Madaniyyah 111, ayat 29, ruku 4. A reader\'s thumb visible at the right edge (excluded).'}])


if __name__ == '__main__':
    p157()
