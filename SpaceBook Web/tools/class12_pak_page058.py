"""Pak Studies XII PDF58 (spread): printed pp.105–106 — Ch.5 Bait-ul-Mal, Hijri calendar, Amir-ul-Momineen, Qazi, public welfare; devolution of power: aims and expectations."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
H('Bait-ul-Mal (public treasury)', 'بیت المال', 'بیت المال')
P('Before the era of Hazrat Umar (RA) there had been no need for a Bait-ul-Mal, because whatever income came in was distributed immediately. In the era of Hazrat Umar (RA) extensive conquests took place, as a result of which income increased considerably. In this connection, with mutual consultation, he established a Bait-ul-Mal in the provinces, while the central Bait-ul-Mal was established in Madina.',
  'حضرت عمرؓ کے دور سے قبل بیت المال کی ضرورت نہیں پڑی تھی۔ کیونکہ جو آمدنی ہوتی تھی اسے فوراً تقسیم کر دیا جاتا تھا۔ حضرت عمرؓ کے دور میں وسیع فتوحات ہوئیں۔ جس کے نتیجے میں آمدنی کافی بڑھ گئی تھی۔ اس سلسلے میں آپ نے باہمی مشورے سے صوبوں میں بیت المال قائم کیے۔ جبکہ مرکزی بیت المال مدینہ میں قائم کیا گیا۔',
  'د حضرت عمر (رض) له دورې مخکې د بیت المال اړتیا نه وه پېښه شوې، ځکه چې کوم عاید به راته هغه سمدستي وېشل کېده. د حضرت عمر (رض) په دوره کې پراخې فتوحات وشول، چې په پایله کې یې عاید ډېر زیات شو. په دې لړ کې هغه د ګډې مشورې سره په ولایتونو کې بیت المالونه جوړ کړل، او مرکزي بیت المال په مدینه کې جوړ شو.')
P('Whatever sum remained with the provinces after expenditure was returned to the central Bait-ul-Mal.',
  'صوبوں کے پاس مصارف کے بعد جو رقم بچ جاتی تھی وہ مرکزی بیت المال کو واپس کر دی جاتی تھی۔',
  'له لګښتونو وروسته چې کومه پیسه له ولایتونو سره پاتې کېده، مرکزي بیت المال ته بېرته ورکول کېده.')
P('The major sources of income of the Bait-ul-Mal were these:',
  'بیت المال کی آمدنی کے بڑے ذرائع یہ تھے۔',
  'د بیت المال د عاید لویې سرچینې دا وې:')
t.group('lines', [('i. Spoils of war (mal-e-ghanimat)', 'i۔ مالِ غنیمت', 'i. د غنیمت مال'), ('ii. Zakat', 'ii۔ زکوٰۃ', 'ii. زکات'), ('iii. Ushr', 'iii۔ عشر', 'iii. عشر'),
                  ('iv. Kharaj', 'iv۔ خراج', 'iv. خراج'), ('v. Jizya, etc.', 'v۔ جزیہ وغیرہ', 'v. جزیه او نور')])
H('Introduction of the Hijri year', 'سنہ ہجری کا اجراء', 'د هجري کال رواجول')
P('The business of the state had spread considerably. The Arabs used to reckon dates from some particular event. Hazrat Umar (RA) presented this issue in the Majlis-e-Shura. There was much discussion and at last it was unanimously decided to start the Islamic calendar from the Hijra (migration) of the Holy Prophet (peace and blessings of Allah be upon him, his family and companions), because the Hijra is the most important event in the history of Islam. The practical start of this calendar took place in 16 AH.',
  'کاروبارِ سلطنت کافی پھیل گیا تھا۔ اہلِ عرب کسی خاص واقعہ سے شمار کا حساب کیا کرتے تھے۔ حضرت عمرؓ نے یہ مسئلہ مجلسِ شوریٰ میں پیش کیا۔ کافی بحث ہوئی اور آخرکار متفقہ طور پر نبی کریم صلی اللہ علیہ وعلیٰ آلہ واصحابہ وسلم کی ہجرت سے اسلامی کیلنڈر شروع کرنے کا فیصلہ کیا گیا۔ کیونکہ ہجرت تاریخِ اسلام میں اہم ترین واقعہ ہے۔ اس کیلنڈر کا عملی آغاز ۱۶ ہجری سے ہوا۔',
  'د سلطنت چارې ډېرې پراخې شوې وې. عربانو به د کوم ځانګړي پېښې له مخې شمېر حسابوه. حضرت عمر (رض) دا مسئله مجلس شورا ته وړاندې کړه. ډېر بحث وشو او بالاخره په اتفاق پرېکړه وشوه چې اسلامي کلیز د نبي کریم (صلی الله علیه وعلی آله واصحابه وسلم) له هجرت پیل شي، ځکه چې هجرت د اسلام په تاریخ کې تر ټولو مهمه پېښه ده. د دې کلیز عملي پیل په ۱۶ هجري کې وشو.')
H('The title of Amir-ul-Momineen', 'امیر المومنین کا لقب', 'د امیر المؤمنین لقب')
P('The caliph was generally remembered by the title “Khalifa-e-Rasool” (successor of the Messenger) (peace and blessings of Allah be upon him, his family and companions). He began the title of Amir-ul-Momineen. Later the caliph came to be remembered only by the title of Amir-ul-Momineen.',
  'خلیفہ عام طور پر خلیفۂ رسول صلی اللہ علیہ وعلیٰ آلہ واصحابہ وسلم کے لقب سے یاد کیے جاتے تھے۔ آپ نے امیر المومنین کے لقب کی ابتداء کی۔ بعد میں خلیفہ کو امیر المومنین کے لقب سے ہی یاد کیا جانے لگا۔',
  'خلیفه به عموماً د "خلیفهٔ رسول" (صلی الله علیه وعلی آله واصحابه وسلم) په لقب یادېده. هغه د امیر المؤمنین لقب پیل کړ. وروسته خلیفه یوازې د امیر المؤمنین په لقب یادېده.')
H('Qazi (judge)', 'قاضی', 'قاضي')
P('The qazis decided cases. They were given a cash salary. The judiciary had complete freedom. There was no pressure of any kind on it from the executive. So much so that, on the complaint of an ordinary person, the qazi could summon even the Amir-ul-Momineen to court. In the eyes of the law all people were equal.',
  'قاضی مقدمات کا فیصلہ کرتے تھے۔ ان کو نقد تنخواہ دی جاتی تھی۔ عدلیہ کو مکمل آزادی حاصل تھی۔ ان پر انتظامیہ کا کسی قسم کا دباؤ نہیں ہوتا تھا۔ یہاں تک کہ قاضی کسی عام شخص کی شکایت پر امیر المومنین کو بھی عدالت میں بلا سکتا تھا۔ قانون کی نظر میں تمام لوگ برابر تھے۔',
  'قاضیانو د قضیو پرېکړې کولې. دوی ته نغده تنخواه ورکول کېده. قضا ته بشپړه ازادي حاصله وه. پر دوی د اجرائیې هېڅ ډول فشار نه و. تر دې چې قاضي د یوه عام کس په شکایت امیر المؤمنین هم محکمې ته رابللی شو. د قانون په نظر کې ټول خلک برابر وو.')
H('Public welfare', 'رفاہِ عامہ', 'عامه هوساینه')
P('He gave public welfare priority over other works. For the first time in the history of the world he fixed stipends for needy people. Salaries were paid to the disabled and the destitute from the Bait-ul-Mal. He had guest houses built in most cities, where travellers were fed at the expense of the Bait-ul-Mal. In Madina a public langar (free kitchen) was set up for the poor. Hazrat Umar (RA) managed it himself. Special care was taken of orphaned children. A stipend was fixed for children from the very day of their birth. He used to patrol himself at night so that he could learn the conditions of the poor. Whatever sum remained from government expenditure was distributed among the Muslims. For the first time in the history of the world he introduced a system of pension. He had several canals dug to improve irrigation and means of transport.',
  'آپ نے رفاہِ عامہ کو دیگر کاموں پر فوقیت دی۔ آپ نے دنیا کی تاریخ میں پہلی دفعہ ضرورت مند لوگوں کے وظائف مقرر کیے۔ معذور اور محتاج افراد کو بیت المال سے تنخواہیں ادا کی جاتی تھیں۔ اکثر شہروں میں مہمان خانے بنوائے۔ جہاں بیت المال کے خرچ سے مسافروں کو کھانا کھلایا جاتا تھا۔ مدینہ میں غریبوں کے لیے عام لنگر قائم تھا۔ اس کا انتظام حضرت عمرؓ خود کرتے تھے۔ لاوارث بچوں کا خاص خیال رکھا جاتا تھا۔ بچوں کی پیدائش کے دن سے ہی ان کا وظیفہ مقرر کر دیا جاتا تھا۔ آپ رات کو خود گشت کیا کرتے تھے تاکہ غریبوں کے حالات معلوم کر سکیں۔ سرکاری اخراجات سے جو رقم بچ جاتی وہ مسلمانوں میں تقسیم کی جاتی تھی۔ آپ نے دنیا کی تاریخ میں پہلی مرتبہ پنشن کا نظام رائج کیا۔ آپ نے آب پاشی اور ذرائع آمد و رفت بہتر بنانے کے لیے کئی نہریں کھدوائیں۔',
  'هغه عامې هوساینې ته پر نورو کارونو لومړیتوب ورکړ. هغه د نړۍ په تاریخ کې د لومړي ځل لپاره اړمنو خلکو ته وظیفې وټاکلې. معلولینو او اړمنو کسانو ته له بیت المال څخه تنخواوې ورکول کېدې. په ډېرو ښارونو کې یې مېلمستونونه جوړ کړل، چې هلته به مسافرو ته د بیت المال په لګښت ډوډۍ ورکول کېده. په مدینه کې د بېوزلو لپاره عام لنګر جوړ و، چې اداره یې حضرت عمر (رض) پخپله کوله. بې‌سرپرسته ماشومانو ته ځانګړې پاملرنه کېده. د ماشومانو وظیفه د هغوی د زېږون له ورځې ټاکل کېده. هغه به د شپې پخپله ګرځېده، څو د بېوزلو حالات معلوم کړي. له دولتي لګښتونو چې کومه پیسه پاتې کېده، هغه په مسلمانانو وېشل کېده. هغه د نړۍ په تاریخ کې د لومړي ځل لپاره د تقاعد نظام رواج کړ. هغه د اوبو لګولو او د تګ راتګ د وسیلو د ښه کولو لپاره څو ویالې وکیندلې.')
H('Devolution of power to the lower level and better governance', 'اختیارات کی نچلی سطح پر منتقلی اور بہتر اسلوبِ حکمرانی', 'ښکته کچې ته د واکونو لېږد او ښه حکومتولي')
H('Aims and expectations', 'اہداف اور توقعات', 'موخې او تمې')
P('The system of governance that prevailed in Pakistan after the attainment of independence in 1947 was based on the imperialist and neo-colonial system of the British. The roots of this system were established on feudal and imperialist foundations. The people had no participation in it, nor were their wishes and intentions included. With independence this imperialist and outdated system ought to have been changed, but for various reasons no one made an effort to change the system.',
  '1947ء میں آزادی کے حصول کے بعد پاکستان میں جو نظامِ حکمرانی رائج ہوا وہ انگریزوں کے سامراجی اور نوآبادیاتی نظام پر مبنی تھا۔ اس نظام کی جڑیں جاگیردارانہ اور سامراجی بنیادوں پر قائم تھیں۔ عوام کا اس میں کوئی عمل دخل اور مرضی و منشا شامل نہ تھی۔ آزادی کے ساتھ اس سامراجی و دقیانوسی نظام کو تبدیل کرنا چاہیے تھا لیکن مختلف وجوہات کی بنا پر کسی نے نظام کی تبدیلی کے لیے کوشش نہیں کی۔',
  'په ۱۹۴۷ز کې له خپلواکۍ وروسته په پاکستان کې کوم حکومتي نظام رواج شو، هغه د انګرېزانو پر امپریالیستي او نوي استعماري نظام ولاړ و. د دې نظام ریښې پر فیوډالي او امپریالیستي بنسټونو ولاړې وې. خلکو پکې هېڅ ونډه او خوښه نه درلوده. له خپلواکۍ سره باید دا امپریالیستي او زوړ نظام بدل شوی وای، خو د بېلابېلو لاملونو له امله چا د نظام د بدلون هڅه ونه کړه.')
P('The previous President proposed that, in accordance with the constitution, to bring “true democracy”, democracy should be established at three levels:',
  'گزشتہ صدر نے آئین کے مطابق ’’حقیقی جمہوریت‘‘ لانے کے لیے یہ تجویز پیش کی کہ جمہوریت تین سطح پر استوار ہو۔',
  'پخواني ولسمشر وړاندیز وکړ چې د اساسي قانون سره سم د "ریښتینې ولسواکۍ" راوستلو لپاره ولسواکي په درې کچو ولاړه شي:')
t.group('lines', [('1. Federal', '1۔ وفاقی', '۱. فدرالي'), ('2. Provincial', '2۔ صوبائی', '۲. ولایتي')])
rec = BOOK.record(t, 'pak12-ch5-text-11', 'Chapter 5 text (11)', 'بابِ پنجم — متن (۱۱)', 'پنځم څپرکی — متن (۱۱)', 58, [105, 106])
rec['sourceNote'] = 'The three-level list begins at the foot of p.106 (items 1–2); item 3 continues on p.107 (PDF59).'
issues = [{'id': 'pak12-pdf058', 'unit': 5, 'printedPage': 105, 'description': 'p.105 numbers the Bait-ul-Mal income sources i–iv in Roman numerals then switches to “7۔ جزیہ” for the fifth item; normalised to “v” in the structured list and noted here.'}]

if __name__ == '__main__':
    BOOK.save(58, [(5, rec)], issues=issues)
