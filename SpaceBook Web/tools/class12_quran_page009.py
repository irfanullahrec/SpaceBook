"""Mutalia-e-Quran XII PDF9: p.6 — Lesson 1 Surah al-Nisa' (1–25): naming and introduction, central theme, basic themes. Run: python class12_quran_page009.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

THEMES = [
    ('Emphasis on taqwa', 'تقویٰ کی تاکید', 'پر تقوا ټینګار'),
    ('Rights of women and orphans', 'عورتوں اور یتیموں کے حقوق', 'د ښځو او یتیمانو حقونه'),
    ('Commands of inheritance', 'وراثت کے احکام', 'د میراث حکمونه'),
    ('Severe warning on committing every kind of immorality', 'ہر قسم کی بدکاری کے ارتکاب پر شدید وعید', 'د هر ډول بدکارۍ پر کولو سخت ګواښ'),
    ('Statement about repentance', 'توبہ کا بیان', 'د توبې بیان'),
    ('Good treatment of women', 'عورتوں سے حسنِ سلوک', 'له ښځو سره ښه چلند'),
    ('Women forbidden in marriage', 'مُحرّماتِ نکاح', 'په نکاح کې حرامې ښځې'),
    ('Commands about marriage with slave-girls', 'کنیزوں سے نکاح کے بارے میں احکام', 'له وینځو سره د نکاح په اړه حکمونه'),
    ('Command to avoid major sins', 'کبیرہ گناہوں سے اجتناب کا حکم', 'له کبیره ګناهونو د ډډې حکم'),
    ('Responsibilities of husband and wife', 'زوجین کی ذمہ داریاں', 'د مېړه او مېرمنې مسؤلیتونه'),
    ('Emphasis on kindness and condemnation of miserliness', 'احسان کی تاکید اور بخل کی مذمت', 'پر احسان ټینګار او د بخل غندنه'),
    ('Rights of the servants (of Allah)', 'حقوق العباد', 'د بندګانو حقونه'),
    ('Statement that the Messenger of Allah (peace and blessings of Allah be upon him) will be a witness over all people on the Day of Gathering', 'رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کا میدانِ حشر میں سب لوگوں پر گواہ ہونے کا بیان', 'د دې بیان چې رسول الله صلی الله علیه وعلی آله واصحابه وسلم به د حشر په ډګر کې پر ټولو خلکو شاهد وي'),
    ('Method of tayammum', 'تیمم کا طریقہ', 'د تیمم طریقه'),
    ('Mischiefs of the Jews', 'یہود کی شرارتیں', 'د یهودو شرارتونه'),
    ('Favours upon the believers', 'مومنین پر انعامات', 'پر مؤمنانو انعامونه'),
    ('Trustworthiness', 'امانت داری', 'امانتداري'),
    ('Command to obey Allah Almighty and the Messenger of Allah (peace and blessings of Allah be upon him), and its blessings', 'اللہ تعالیٰ اور رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت کا حکم اور اس کی برکات', 'د الله تعالی او رسول الله صلی الله علیه وعلی آله واصحابه وسلم د اطاعت حکم او د هغې برکتونه'),
    ('The hypocrites\' refusal to obey the Messenger of Allah (peace and blessings of Allah be upon him), their turning away from presenting themselves at the court of Messengership for the prayer of forgiveness and intercession, and fleeing from fighting in the way of Allah', 'منافقین کا رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت سے انکار، دعائے مغفرت و شفاعت کے لیے بارگاہِ رسالت میں حاضری سے روگردانی اور قتال فی سبیل اللہ سے فرار', 'د منافقانو له خوا د رسول الله صلی الله علیه وعلی آله واصحابه وسلم له اطاعت انکار، د مغفرت او شفاعت د دعا لپاره د رسالت دربار ته له حاضرېدو مخ اړول او د الله په لار کې له جګړې تېښته'),
    ('Fighting in the way of Allah and its commands', 'قتال فی سبیل اللہ اور اس کے احکام', 'د الله په لار کې جګړه او د هغې حکمونه'),
    ('Death is an unalterable reality', 'موت ایک اٹل حقیقت', 'مرګ یو نه بدلېدونکی حقیقت دی'),
    ('Obedience to the Messenger (peace and blessings of Allah be upon him) and guidance about salam', 'اطاعتِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم اور سلام کے بارے میں ہدایات', 'د رسول صلی الله علیه وعلی آله واصحابه وسلم اطاعت او د سلام په اړه لارښوونې'),
    ('Severe reproach of the hypocrites', 'منافقین پر سخت گرفت', 'پر منافقانو سخت نیونه'),
    ('Excellence of the mujahidin', 'مجاہدین کی فضیلت', 'د مجاهدینو فضیلت'),
    ('Issues of migration (hijrah)', 'ہجرت کے مسائل', 'د هجرت مسایل'),
    ('Commands of blood-money on committing unintentional killing', 'قتلِ خطا کے ارتکاب پر دیت کے احکام', 'د ناقصدي وژنې پر کولو د دیت حکمونه'),
    ('Warning of severe punishment for the crime of intentional killing', 'قتلِ عمد کے جرم پر سخت سزا کی وعید', 'د قصدي وژنې پر جرم د سختې سزا ګواښ'),
    ('Commands of jihad', 'جہاد کے احکام', 'د جهاد حکمونه'),
    ('Shortening of prayer and the prayer of fear', 'نماز قصر اور نمازِ خوف', 'قصر لمونځ او د وېرې لمونځ'),
    ('Command to establish prayer with punctuality of time', 'پابندیِ وقت کے ساتھ اقامتِ صلوٰۃ کا حکم', 'د وخت په پابندۍ سره د لمانځه د قایمولو حکم'),
    ('Prohibition of taking the side of the treacherous, and instruction of repentance and seeking forgiveness', 'خائن کی طرف داری کی ممانعت اور توبہ و استغفار کی تلقین', 'د خاین د پلوي کولو منع او د توبې او استغفار سپارښتنه'),
    ('The grace and mercy of Allah Almighty upon the Noble Prophet (peace and blessings of Allah be upon him)', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر اللہ تعالیٰ کا فضل و رحمت', 'پر نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د الله تعالی فضل او رحمت'),
    ('Condemnation of shirk', 'شرک کی مذمت', 'د شرک غندنه'),
    ('The tricks of Satan', 'شیطان کی چالیں', 'د شیطان چلونه'),
    ('Excellence of good deeds', 'نیک اعمال کی فضیلت', 'د نېکو عملونو فضیلت'),
]


def p9():
    b = Builder()
    b.h('Lesson 1 — Surah al-Nisa\' (verses 1 to 25)', 'سبق ۱ — سُوْرَةُ النِّسَآءِ (آیات: ۱ تا ۲۵)', '۱ لوست — سورة النساء (آیتونه ۱ تر ۲۵)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('"Nisa\'" means "women". Since in this surah the rights and commands of women are stated in greater detail, it has been given the name "Surah al-Nisa\'". In the Age of Ignorance women had no rights. Women were an extremely oppressed and deprived class of society. The birth of daughters was considered a disgrace and they were buried alive. No rights of wives were fixed either; there was no limit on the number of wives for one man. Women were distributed like inherited property; step-sons married their step-mothers; slave-girls were compelled into prostitution; there was no protection of the honour and chastity of women. In these circumstances the Qur\'an Majeed granted women all their rights, gave them a share in inheritance, stated in detail the women forbidden in marriage, declared marriage with one\'s step-mother forbidden, fixed the number of wives and also commanded justice among them, gave women the right of mahr, maintenance, clothing and housing, and declared a righteous wife the best wealth.', '”نِسَآءِ“ کا مطلب ہے ”عورتیں“۔ کیوں کہ اس سورت میں عورتوں کے حقوق اور احکام زیادہ تفصیل سے بیان ہوئے ہیں، اس لیے اسے ”سُوْرَةُ النِّسَآءِ“ کا نام دیا گیا ہے۔ دورِ جاہلیت میں عورتوں کے کوئی حقوق نہ تھے۔ عورتیں معاشرہ کا انتہائی مظلوم اور محروم طبقہ تھیں۔ بیٹیوں کی پیدائش کو عار سمجھا جاتا اور ان کو زندہ دفن کر دیا جاتا۔ بیویوں کے بھی کوئی حقوق متعین نہ تھے، ایک مرد کے لیے بیویوں کی تعداد کی کوئی قید نہ تھی، عورتیں مالِ وراثت کی طرح تقسیم کر دی جاتیں، سوتیلے بیٹے ماں سے نکاح کر لیتے، کنیزوں کو جسم فروشی پر مجبور کیا جاتا، عورتوں کی عزت و عفت کا کوئی تحفظ نہ تھا۔ ان حالات میں قرآنِ مجید نے عورتوں کو ان کے جملہ حقوق عطا فرمائے، وراثت میں حصہ دیا، محرمات کی تفصیل بیان فرمائی، اپنی سوتیلی ماں سے نکاح کو حرام قرار دیا، بیویوں کی تعداد مُعین فرمائی نیز اُن کے درمیان عدل کا حکم فرمایا، عورتوں کو حق مہر، نان نفقہ، لباس اور رہائش کا حق دیا اور نیک بیوی کو بہترین دولت قرار دیا۔', '«نساء» یعنې «ښځې». څرنګه چې په دې سورت کې د ښځو حقونه او حکمونه په زیات تفصیل بیان شوي، نو «سورة النساء» نوم ورکړل شوی. د جاهلیت په دوره کې ښځو هېڅ حق نه درلود؛ ښځې د ټولنې ډېره مظلومه او بې‌برخې طبقه وه؛ د لوڼو زېږېدل شرم ګڼل کېده او ژوندۍ ښخېدې. د مېرمنو حقونه هم نه وو ټاکل شوي؛ د یوه نارینه لپاره د مېرمنو پر شمېر کوم بندیز نه و؛ ښځې د میراث د مال په څېر وېشل کېدې؛ میړني زامنو له خپلې میړنۍ مور سره نکاح کوله؛ وینځې فحشا ته اړ کېدې؛ د ښځو عزت او عفت هېڅ ساتنه نه درلوده. په دې حالاتو کې قرآن مجید ښځو ته ټول حقونه ورکړل، په میراث کې یې برخه ورکړه، د محرماتو تفصیل یې بیان کړ، له میړنۍ مور سره نکاح یې حرامه وګرځوله، د مېرمنو شمېر یې وټاکه او ترمنځ یې د عدل حکم وکړ، ښځو ته یې د مهر، نفقې، جامو او استوګنې حق ورکړ او نېکه مېرمن یې غوره شتمني وبلله.')),
          (None, ('This is a Madani surah. The greater part of it was revealed from 3 AH to 5 AH; for example, the verses related to the division of inheritance and the rights of orphans were revealed after the battle of Uhud, when seventy Companions (may Allah be pleased with them) had been martyred. The battle of Uhud took place in 3 AH. In this surah the prayer of fear is mentioned, which was offered in the battle of Dhat al-Riqa\' that took place in 4 AH. In the same way tayammum is stated, permission for which was given in the battle of Banu Mustaliq that took place in 5 AH.', 'یہ مدنی سورت ہے۔ اس کا زیادہ تر حصہ ۳ھ سے ۵ھ تک نازل ہوا۔ مثلاً وراثت کی تقسیم اور یتیموں کے حقوق سے متعلق آیات غزوۂ اُحد کے بعد نازل ہوئیں جب ستر صحابہ کرام رضی اللہ تعالیٰ عنہم شہید ہو گئے تھے۔ غزوۂ اُحد ۳ھ میں ہوا تھا۔ اس سورت میں نماز خوف کا ذکر ہے جو غزوۂ ذات الرقاع میں پڑھی گئی جو ۴ھ میں ہوا۔ اسی طرح تیمم کا بیان ہے جس کی اجازت غزوۂ بنی مصطلق میں دی گئی جو ۵ھ میں پیش آیا۔', 'دا مدني سورت دی؛ زیاته برخه یې له ۳ هـ تر ۵ هـ نازله شوې؛ د بېلګې په توګه د میراث د وېش او د یتیمانو د حقونو اړوند آیتونه د احد له غزا وروسته نازل شول، کله چې اویا صحابه کرام رضي الله تعالی عنهم شهیدان شوي وو؛ د احد غزا په ۳ هـ کې وشوه. په دې سورت کې د وېرې د لمانځه یادونه ده چې د ذات الرقاع په غزا کې وکړل شو، چې په ۴ هـ کې وه. همداسې د تیمم بیان دی چې اجازه یې د بني مصطلق په غزا کې ورکړل شوه، چې په ۵ هـ کې پېښه شوه.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Social commands and issues', 'معاشرتی احکام و مسائل', 'ټولنیز حکمونه او مسایل')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    BOOK.save(9, [(1, rec(b, 1, 9, 9, first=True))], issues=[{'id': 'mq12-pdf009', 'unit': 1, 'printedPage': 6,
               'description': 'The 35 basic themes are printed as a run-on numbered paragraph for the whole of Surah al-Nisa\' (all five lessons); rendered as a list. Pashto digits shown in Western form in the Pashto list labels.'}])


if __name__ == '__main__':
    p9()
