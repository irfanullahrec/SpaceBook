"""Mutalia-e-Quran XII PDF56: p.53 — Lesson 6 Surah al-Ma'idah (1–34): naming and introduction, Prophetic sayings, central theme, basic themes 1–37. Run: python class12_quran_page056.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Emphasis on fulfilling covenants', 'ایفائے عہد کی تاکید', 'د ژمنو د پوره کولو ټینګار'),
    ('Command to honour and revere the symbols of Allah', 'شعائر اللہ کی تعظیم و توقیر بجا لانے کا حکم', 'د الله د شعایرو د درناوي حکم'),
    ('Statement of lawful and unlawful things', 'حلال و حرام چیزوں کا بیان', 'د حلالو او حرامو شیانو بیان'),
    ('Announcement of the completion of religion', 'تکمیلِ دین کا اعلان', 'د دین د بشپړېدو اعلان'),
    ('Commands of wudu, ghusl and tayammum', 'وضو، غسل اور تیمم کے احکام', 'د اودس، غسل او تیمم حکمونه'),
    ('Command to keep the covenant of Allah Almighty', 'اللہ تعالیٰ کے عہد کی پابندی کا حکم', 'د الله تعالی د ژمنې د پابندۍ حکم'),
    ('Emphasis on justice', 'عدل کی تاکید', 'پر عدل ټینګار'),
    ('Mention of the favour of Allah Almighty upon the Muslims', 'مسلمانوں پر اللہ تعالیٰ کے احسان کا ذکر', 'پر مسلمانانو د الله تعالی د احسان یادونه'),
    ('Covenant-breaking of the Jews and Christians and its punishment', 'یہود و نصاریٰ کی عہد شکنی اور اس کی سزا', 'د یهودو او نصاراوو ژمنه ماتونه او د هغې سزا'),
    ('The coming of the Messenger of Allah (peace and blessings of Allah be upon him)', 'رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی تشریف آوری', 'د رسول الله صلی الله علیه وعلی آله واصحابه وسلم راتګ'),
    ('Advice to the People of the Book and pointing out their wrong beliefs', 'اہلِ کتاب کو نصیحت اور ان کے غلط عقائد کی نشان دہی', 'اهل کتابو ته نصیحت او د هغوی د غلطو عقیدو په ګوته کول'),
    ('Sayyiduna Musa\'s (peace be upon him) call to the Banu Isra\'il to jihad and fighting', 'سیدنا موسیٰ علیہ السلام کی بنی اسرائیل کو جہاد و قتال کی دعوت', 'د سیدنا موسی علیه السلام له خوا بني اسرائیلو ته د جهاد او جګړې بلنه'),
    ('Statement of the Banu Isra\'il\'s refusal of jihad and fighting, and its punishment', 'بنی اسرائیل کا جہاد و قتال کرنے سے انکار اور اس کی سزا کا بیان', 'د بني اسرائیلو له جهاد او جګړې انکار او د هغې سزا بیان'),
    ('The story of Habil and Qabil', 'قصہ ہابیل و قابیل', 'د هابیل او قابیل کیسه'),
    ('Laws of war', 'جنگی قوانین', 'جنګي قوانین'),
    ('Means of nearness to Allah', 'قربتِ الٰہی کے وسیلے', 'د الهي نږدېوالي وسیلې'),
    ('Mention of the punishment for theft', 'چوری کی سزا کا ذکر', 'د غلا د سزا یادونه'),
    ('Condemnation of the hypocrites and the Jews', 'منافقین اور یہود کی مذمت', 'د منافقانو او یهودو غندنه'),
    ('Commands of the Tawrah', 'تورات کے احکام', 'د تورات حکمونه'),
    ('Mention of the Injil', 'انجیل کا ذکر', 'د انجیل یادونه'),
    ('Command to judge according to the Qur\'an Majeed', 'قرآنِ مجید کے مطابق فیصلے کرنے کا حکم', 'د قرآن مجید سره سم د پرېکړې حکم'),
    ('Prohibition of friendship with the Jews, Christians and disbelievers', 'یہود و نصاریٰ اور کفار سے دوستی کی ممانعت', 'له یهودو، نصاراوو او کافرانو سره د دوستۍ منع'),
    ('The conduct and end of the hypocrites', 'منافقین کا طرزِ عمل اور انجام', 'د منافقانو چلند او پایله'),
    ('Mention of the qualities of the believers', 'مومنین کے اوصاف کا ذکر', 'د مؤمنانو د صفتونو یادونه'),
    ('Crimes of the Jews', 'یہود کے جرائم', 'د یهودو جرمونه'),
    ('Blessings of enforcing the Shari\'ah', 'نفاذِ شریعت کی برکات', 'د شریعت د پلي کولو برکتونه'),
    ('Allah Almighty Himself being the Protector of the Messenger of Allah (peace and blessings of Allah be upon him)', 'اللہ تعالیٰ کا رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے لیے خود محافظ ہونا', 'د رسول الله صلی الله علیه وعلی آله واصحابه وسلم لپاره د الله تعالی پخپله ساتونکی کېدل'),
    ('Call to the People of the Book to reform', 'اہلِ کتاب کو دعوتِ اصلاح', 'اهل کتابو ته د اصلاح بلنه'),
    ('Prohibition of excess in religion', 'دین میں غلو کرنے کی ممانعت', 'په دین کې له غلو منع'),
    ('Refutation of the wrong beliefs attributed to Sayyiduna \'Isa (peace be upon him)', 'سیدنا عیسیٰ علیہ السلام سے منسوب غلط عقائد کا رد', 'سیدنا عیسی علیه السلام ته منسوبو غلطو عقیدو رد'),
    ('Reason for the curse upon the disbelievers of the Banu Isra\'il', 'بنی اسرائیل کی کفار پر لعنت کی وجہ', 'د بني اسرائیلو پر کافرانو د لعنت لامل'),
    ('Enmity of the Jews and polytheists', 'یہود و مشرکین کی عداوت', 'د یهودو او مشرکانو دښمني'),
    ('Description of the people of truth', 'اہلِ حق کی تعریف', 'د حق خلکو ستاینه'),
    ('Mention of lawful and unlawful things', 'حلال و حرام چیزوں کا ذکر', 'د حلالو او حرامو شیانو یادونه'),
    ('Expiation of oaths', 'قسم کا کفارہ', 'د قسم کفاره'),
    ('Prohibition of hunting in the state of ihram, and its commands', 'حالتِ احرام میں شکار کی ممانعت اور احکام', 'د احرام په حال کې د ښکار منع او حکمونه'),
    ('Definitive command of the prohibition of wine and gambling', 'شراب اور جوا بازیوں کی حرمت کا قطعی حکم', 'د شرابو او قمار د حرمت قطعي حکم'),
]


def p56():
    b = Builder()
    b.h('Lesson 6 — Surah al-Ma\'idah (verses 1 to 34)', 'سبق ۶ — سُوْرَةُ الْمَآئِدَةِ (آیات: ۱ تا ۳۴)', '۶ لوست — سورة المائدة (آیتونه ۱ تر ۳۴)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('Surah al-Ma\'idah is a Madani surah. It is also called "Surat al-\'Uqud", because in its first verse there is an emphasis on fulfilling promises. "Ma\'idah" means "a dining cloth (table spread)". In it the descent of a miraculous table spread is mentioned. This name has been taken from verses 112 and 114 of the surah, when the disciples demanded of Sayyiduna \'Isa (peace be upon him) that a table spread be sent down from the heaven, and Allah Almighty, by the blessing of the prayer of Sayyiduna \'Isa (peace be upon him), sent down the table spread from the heaven. The revelation of the surah began in the time of the Treaty of Hudaybiyah, and its completion took place on the plain of \'Arafat on the occasion of the Farewell Hajj.', 'سُوْرَةُ الْمَآئِدَةِ مدنی سورت ہے۔ اسے ”سُوْرَةُ الْعُقُوْدِ“ بھی کہا جاتا ہے کیوں کہ اس کی پہلی آیت میں وعدے پورے کرنے کی تاکید ہے۔ ”مَآئِدَةٌ“ کا معنی ”دستر خوان“ ہے اس میں ایک معجزانہ دستر خوان کے نزول کا ذکر ہے۔ یہ نام اس سورت کی آیت: ۱۱۲ اور ۱۱۴ سے لیا گیا ہے کہ جب حواریوں نے سیدنا عیسیٰ علیہ السلام سے آسمان سے مائدہ اُتارنے کا مطالبہ کیا اللہ تعالیٰ نے سیدنا عیسیٰ علیہ السلام کی دعا کی برکت سے آسمان سے مائدہ نازل فرمایا۔ سورت کے نزول کا آغاز صلح حدیبیہ کے زمانہ میں ہوا اور اس کی تکمیل حجۃ الوداع کے موقع پر میدانِ عرفات میں ہوئی۔', 'سورة المائده مدني سورت دی. «سورة العقود» هم ورته ویل کېږي، ځکه په لومړي آیت کې یې د ژمنو د پوره کولو ټینګار دی. «مائده» یعنې «دسترخوان». په دې کې د یوه معجزه‌ییز دسترخوان د نزول یادونه ده؛ دا نوم د سورت له ۱۱۲ او ۱۱۴ آیتونو اخیستل شوی، کله چې حواریانو له سیدنا عیسی علیه السلام وغوښتل چې له اسمانه مائده راکوزه شي، او الله تعالی د سیدنا عیسی علیه السلام د دعا په برکت له اسمانه مائده نازله کړه. د سورت نزول د حدیبیې د سولې په وخت کې پیل شو او بشپړېدل یې د حجة الوداع پر مهال د عرفاتو په ډګر کې وشول.')),
          (('Sayings of the Prophet (peace and blessings of Allah be upon him)', 'فرامینِ نبوی صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم', 'نبوي فرمانونه'),
           ('1. Sayyidah Asma\' bint Yazid (may Allah be pleased with her) narrates that she says: "I was holding the reins of the she-camel (named \'Adba\') of the Noble Prophet (peace and blessings of Allah be upon him) when the whole of Surah al-Ma\'idah was revealed upon him (peace and blessings of Allah be upon him). It was near that the she-camel\'s arms would break from the weight of the revelation." (Musnad Ahmad: 27575)', '۱۔ سیدہ اسماء بنت یزید رضی اللہ تعالیٰ عنہا سے روایت ہے وہ کہتی ہیں کہ: ”میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی عضباء اونٹنی کی لگام تھامے ہوئے تھی کہ آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر سُوْرَةُ الْمَآئِدَةِ پوری نازل ہوئی۔ قریب تھا کہ اس (وحی کے) بوجھ سے اونٹنی کے بازو ٹوٹ جاتے۔“ (مسند احمد: ۲۷۵۷۵)', '۱. له سیده اسماء بنت یزید رضي الله تعالی عنها روایت دی، هغه وايي: «ما د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د عضباء اوښې واګې نیولې وې چې پر هغه صلی الله علیه وعلی آله واصحابه وسلم ټوله سورة المائده نازله شوه؛ نږدې وه چې د هغې (وحي) له باره د اوښې لاسونه مات شي.» (مسند احمد: ۲۷۵۷۵)')),
          (None, ('2. Sayyiduna Tariq bin Shihab (may Allah be pleased with him) narrates that a Jew came to Sayyiduna \'Umar bin Khattab (may Allah be pleased with him) and said: O Amir al-Mu\'minin! If this verse — "اَلْيَوْمَ اَكْمَلْتُ لَكُمْ دِيْنَكُمْ وَاَتْمَمْتُ عَلَيْكُمْ نِعْمَتِيْ وَرَضِيْتُ لَكُمُ الْاِسْلَامَ دِيْنًا" (Surah al-Ma\'idah: 3), "This day I have perfected your religion for you, and completed My favour upon you, and chosen Islam for you as religion" — had been revealed upon us, we would have celebrated that day as an \'Id. So Sayyiduna \'Umar (may Allah be pleased with him) said: "I know well on what day this verse was revealed. This verse was revealed on Friday, the day of \'Arafah." (Sahih Bukhari: 4268)', '۲۔ سیدنا طارق بن شہاب رضی اللہ تعالیٰ عنہ سے روایت ہے کہ ایک یہودی سیدنا عمر بن خطاب رضی اللہ تعالیٰ عنہ کے پاس آیا اور کہنے لگا: اے امیر المومنین! اگر یہ آیت: اَلْيَوْمَ اَكْمَلْتُ لَكُمْ دِيْنَكُمْ وَاَتْمَمْتُ عَلَيْكُمْ نِعْمَتِيْ وَرَضِيْتُ لَكُمُ الْاِسْلَامَ دِيْنًا (سُوْرَةُ الْمَآئِدَةِ: ۳) ”آج کے دن میں نے تمھارے لیے تمھارا دین مکمل کر دیا اور تم پر اپنی نعمت پوری کر دی اور تمھارے لیے اسلام کو بطورِ دین پسند کر لیا۔“ ہم پر نازل ہوتی تو ہم اس دن کو بطور عید مناتے تو سیدنا عمر رضی اللہ تعالیٰ عنہ نے فرمایا: ”میں خوب جانتا ہوں یہ آیت کس دن نازل ہوئی، یہ آیت عرفہ کے روز جمعہ کے دن نازل ہوئی۔“ (صحیح بخاری: ۴۲۶۸)', '۲. له سیدنا طارق بن شهاب رضي الله تعالی عنه روایت دی چې یو یهودي سیدنا عمر بن خطاب رضي الله تعالی عنه ته راغی او ویې ویل: ای امیرالمؤمنینه! که دا آیت — «اَلْيَوْمَ اَكْمَلْتُ لَكُمْ دِيْنَكُمْ وَاَتْمَمْتُ عَلَيْكُمْ نِعْمَتِيْ وَرَضِيْتُ لَكُمُ الْاِسْلَامَ دِيْنًا» (سورة المائده: ۳) «نن ما تاسو ته ستاسو دین بشپړ کړ، پر تاسو مې خپل نعمت پوره کړ او تاسو ته مې اسلام د دین په توګه غوره کړ» — پر موږ نازل شوی وای، نو موږ به هغه ورځ د اختر په توګه لمانځله. نو سیدنا عمر رضي الله تعالی عنه وفرمایل: «زه ښه پوهېږم چې دا آیت په کومه ورځ نازل شو؛ دا آیت د عرفې په ورځ، د جمعې په ورځ نازل شو.» (صحیح بخاري: ۴۲۶۸)')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Beliefs and acts of worship', 'عقائد و عبادات', 'عقیدې او عبادتونه')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    BOOK.save(56, [(6, rec(b, 6, 56, 56, first=True))], issues=[{'id': 'mq12-pdf056', 'unit': 6, 'printedPage': 53,
               'description': 'The 37 basic themes of Surah al-Ma\'idah (whole surah) are printed as a run-on numbered paragraph; continued on p.54 (item 37 completes on p.54 and is given whole here). Hadith references kept as printed.'}])


if __name__ == '__main__':
    p56()
