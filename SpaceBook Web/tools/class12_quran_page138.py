"""Mutalia-e-Quran XII PDF138: p.135 — Lesson 14 Surah al-Shura (1–53): naming and introduction, central theme, basic themes; surah heading; verses 42:1–2 (42:3 continues onto p.136; recorded there). Run: python class12_quran_page138.py"""
from class12_quran_common import BOOK, Builder, rec, S, L, V

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('A statement of the greatness and attributes of Allah Almighty', 'اللہ تعالیٰ کی عظمت اور اوصاف کا بیان', 'د الله تعالی د عظمت او صفتونو بیان'),
    ('Mention of divine revelation', 'وحیِ الٰہی کا ذکر', 'د الهي وحې یادونه'),
    ('A statement of the wisdom of the revelation of the Holy Qur\'an in Arabic', 'قرآنِ مجید کے عربی میں نزول کی حکمت کا بیان', 'په عربي کې د قرآن مجید د نزول د حکمت بیان'),
    ('Mention of the day of the gathering of the first and the last', 'اولین و آخرین کے جمع ہونے کے دن کا ذکر', 'د لومړنیو او وروستنیو د راټولېدو د ورځې یادونه'),
    ('A statement of the angels glorifying Allah Almighty and praying for forgiveness for the dwellers of the earth; and that the ownership of the treasures of the heavens and the earth, and the power to make provision ample or scant, rest with Allah Almighty', 'فرشتوں کا اللہ تعالیٰ کی پاکی بیان کرنے اور زمین والوں کے لیے مغفرت کی دعا کرنے کا بیان اور آسمان و زمین کے خزانوں کی ملکیت اور رزق میں وسعت یا تنگی پیدا کرنے کا اختیار اللہ تعالیٰ کے پاس ہونے کا بیان', 'د پرښتو له خوا د الله تعالی د پاکۍ بیانول او د ځمکې د اوسېدونکو لپاره د بښنې دعا کول؛ او د آسمان او ځمکې د خزانو ملکیت او په رزق کې د پراخۍ یا تنګۍ اختیار له الله تعالی سره دی'),
    ('Mention of the one mission of all the noble Prophets (peace be upon them): the supremacy of the religion', 'تمام انبیاء کرام علیہم السلام کا ایک ہی مشن غلبۂ دین کا ذکر', 'د ټولو انبیاء کرامو علیهم السلام یو مشن: د دین د غلبې یادونه'),
    ('A statement of the cause of the division of the People of the Book', 'اہلِ کتاب کے تفرقہ کی وجہ کا بیان', 'د اهل کتابو د تفرقې د لامل بیان'),
    ('A statement of Tawhid being burdensome to the polytheists', 'مشرکین پر توحید کے گراں ہونے کا بیان', 'پر مشرکانو د توحید د درنېدو بیان'),
    ('Proofs of the truthfulness of the teachings of the Prophet of Islam (peace and blessings of Allah be upon him)', 'پیغمبرِ اسلام صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی تعلیمات کی صداقت پر دلائل', 'د اسلام د پیغمبر صلی الله علیه وعلی آله واصحابه وسلم د تعلیماتو پر رښتینولۍ دلیلونه'),
    ('The command to the Prophet (peace and blessings of Allah be upon him) to remain engaged in the work of invitation and preaching', 'آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو دعوت و تبلیغ کے کام میں لگے رہنے کا حکم', 'هغه صلی الله علیه وعلی آله واصحابه وسلم ته د دعوت او تبلیغ په کار کې د بوخت پاتې کېدو حکم'),
    ('Declaration of the tolerant teaching of the Holy Prophet (peace and blessings of Allah be upon him)', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی روادارانہ تعلیم کا اعلان', 'د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د زغمناکې لارښوونې اعلان'),
    ('Special commands for the Holy Prophet (peace and blessings of Allah be upon him) about steadfastness in the struggle of preaching and establishing the religion, and a statement of some lofty qualities of the people of faith', 'تبلیغ و اقامتِ دین کی جدوجہد پر استقامت اختیار کرنے کے حوالے سے نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے لیے خصوصی احکامات اور اہلِ ایمان کے چند صفاتِ جلیلہ کا بیان', 'د تبلیغ او د دین د اقامت په هڅو کې د استقامت په اړه د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم لپاره ځانګړي حکمونه، او د مؤمنانو د ځینو لوړو صفتونو بیان'),
    ('A statement of the tillage of this world and the Hereafter', 'دنیا و آخرت کی کھیتی کا بیان', 'د دنیا او آخرت د کښت بیان'),
    ('Glad tidings to the believers and their rewards', 'مومنوں کو بشارت اور ان کے انعامات', 'مؤمنانو ته زېری او د هغوی انعامونه'),
    ('Mention of Allah Almighty accepting the repentance of His servants', 'اللہ تعالیٰ کا اپنے بندوں کی توبہ قبول فرمانے کا ذکر', 'د الله تعالی له خوا د خپلو بندګانو د توبې د منلو یادونه'),
    ('Mention of affliction reaching man because of his own deeds', 'انسان کو اپنے اعمال کی وجہ سے مصیبت پہنچنے کا ذکر', 'د خپلو عملونو له امله انسان ته د مصیبت د رسېدو یادونه'),
    ('A statement of the signs of the power of Allah Almighty', 'اللہ تعالیٰ کی قدرت کی نشانیوں کا بیان', 'د الله تعالی د قدرت د نښو بیان'),
    ('The subjugation of the seas and ships as a great sign and blessing of Allah Almighty', 'سمندروں کی تسخیر اور بحری جہاز اللہ تعالیٰ کی ایک بڑی نشانی اور نعمت', 'د سمندرونو تسخیر او بېړۍ د الله تعالی یوه لویه نښه او نعمت'),
    ('Mention of the required qualities of those who strive for establishing and spreading the religion', 'دین کی اقامت و اشاعت کی جدوجہد کرنے والوں کے مطلوبہ اوصاف کا ذکر', 'د دین د اقامت او خپرولو لپاره د هڅه کوونکو د غوښتل شویو صفتونو یادونه'),
    ('The permissibility of taking retribution with justice, the negation of oppression, and the praise of forgiving', 'عدل کے ساتھ بدلہ لینے کا جواز اور ظلم کی نفی اور معاف کرنے کی تعریف و تحسین', 'په عدل سره د بدلې اخیستلو جواز، د ظلم نفي او د بښنې ستاینه'),
    ('A statement that guidance and misguidance are in the power of Allah Almighty', 'ہدایت و گمراہی کا اختیار اللہ تعالیٰ کے پاس ہونے کا بیان', 'د هدایت او ګمراهۍ اختیار له الله تعالی سره دی'),
    ('Concern for the Hereafter and a statement of the evil end of the wrongdoers', 'فکرِ آخرت اور ظالموں کے انجامِ بد کا بیان', 'د آخرت فکر او د ظالمانو د بدې پایلې بیان'),
    ('Mention of giving the opponents a final chance to abandon opposition, accept the call of the Prophet of Islam (peace and blessings of Allah be upon him) and set right their hereafter', 'مخالفین کو مخالفت چھوڑ کر پیغمبرِ اسلام صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی دعوت کو قبول کر کے اپنی عاقبت سنوارنے کا آخری موقع دینے کا ذکر', 'مخالفانو ته د دې وروستي فرصت ورکولو یادونه چې مخالفت پرېږدي، د اسلام د پیغمبر صلی الله علیه وعلی آله واصحابه وسلم بلنه ومني او خپل آخرت سم کړي'),
    ('A statement of man\'s ingratitude', 'انسان کے ناشکرا پن کا بیان', 'د انسان د ناشکرۍ بیان'),
    ('Mention that the power to grant children rests with Allah Almighty', 'اولاد دینے کا اختیار اللہ تعالیٰ کے پاس ہونے کا ذکر', 'د اولاد ورکولو اختیار له الله تعالی سره دی'),
    ('Mention of the levels and modes of revelation', 'وحی کے مراتب و کیفیات کا ذکر', 'د وحې د درجو او کیفیتونو یادونه'),
    ('A statement of the wisdom of the revelation of the Qur\'an-e-Hakim', 'حکمتِ نزولِ قرآنِ حکیم کا بیان', 'د قرآن حکیم د نزول د حکمت بیان'),
    ('The knowledge of the Prophet of Islam (peace and blessings of Allah be upon him) is the result of the grace and bounty of God', 'پیغمبرِ اسلام صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کا علم فضل فیضِ خداوندی کا نتیجہ', 'د اسلام د پیغمبر صلی الله علیه وعلی آله واصحابه وسلم علم د الهي فضل او فیض پایله ده'),
    ('A statement of the duty of messengership and the straight path', 'فریضۂ رسالت اور صراطِ مستقیم کا بیان', 'د رسالت د فریضې او سمې لارې بیان'),
]


def p138():
    b = Builder()
    b.h('Lesson 14 — Surah al-Shura (verses 1 to 53)', 'سبق ۱۴ — سُوْرَةُ الشُّوْرٰی (آیات: ۱ تا ۵۳)', '۱۴ لوست — سورة الشوری (آیتونه ۱ تر ۵۳)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('In verse 38 the word "al-Shura" has come, which means consulting one another. With this connection its name is Surah al-Shura. Surah al-Shura is a Makki surah. It is the third surah among the seven "Hawamim".',
            'آیت: ۳۸ میں اَلشُّوْرٰی کا لفظ آیا ہے جس کا معنی ہے مشورہ کرنا۔ اسی مناسبت سے اس کا نام سُوْرَةُ الشُّوْرٰی ہے۔ سُوْرَةُ الشُّوْرٰی مکی سورت ہے۔ یہ سات "حَوَامِیْم" میں سے تیسری سورت ہے۔',
            'په ۳۸ آیت کې د «الشوری» کلمه راغلې چې مانا یې مشوره کول دي؛ په همدې مناسبت یې نوم سورة الشوری دی. سورة الشوری مکي سورت دی او له اوو «حوامیمو» څخه درېیم سورت دی.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('The three beliefs (Tawhid, Prophethood and the Hereafter) and the truth of the Holy Qur\'an', 'عقائدِ ثلاثہ (توحید، رسالت اور آخرت) اور حقانیتِ قرآنِ مجید', 'درې ګونې عقیدې (توحید، رسالت او آخرت) او د قرآن مجید حقانیت')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    b.h('Surah al-Shura (42) — Makki; order of revelation 62; verses 53, sections 5', 'سُوْرَةُ الشُّوْرٰی ۴۲ — مَكِّيَّةٌ ۶۲ — اٰیَاتُهَا ۵۳، رُکُوْعَاتُهَا ۵', 'سورة الشوری (۴۲) — مکي؛ د نزول ترتیب ۶۲؛ آیتونه ۵۳، رکوعونه ۵')
    b.p('بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nIn the name of Allah, the Beneficent, the Merciful.', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nاللہ کے نام سے شروع جو بڑا مہربان نہایت رحم فرمانے والا ہے', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nد الله په نوم پیل چې ډېر مهربان، بې‌حده رحم کوونکی دی')
    b.paras[-1]['arabicSource'] = True
    V(b, 42, 1, 'حٰمٓ۔ عٓسٓقٓ۔', 'حم. عسق.', a2=2)
    BOOK.save(138, [(14, rec(b, 14, 138, 138, first=True))], issues=[{'id': 'mq12-pdf138', 'unit': 14, 'printedPage': 135,
               'description': 'Lesson 14 heading: Surah al-Shura, verses 1 to 53. Twenty-nine basic themes printed as a run-on numbered paragraph; rendered as a list. Surah cartouche: al-Shura 42, Makkiyyah 62, ayat 53, ruku 5. The book\'s Urdu "حٰمٓ۔ عٓسٓقٓ۔" covers verses 1–2 together. Verse 42:3 begins on the last line of p.135 and is recorded with p.136.'}])


if __name__ == '__main__':
    p138()
