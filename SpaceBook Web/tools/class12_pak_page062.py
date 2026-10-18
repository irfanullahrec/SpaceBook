"""Pak Studies XII PDF62 (spread): printed pp.113–114 — Ch.5 resources (cont.), sense of responsibility; مشق Q1–Q3(iii)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
P = t.p
P('… should take place, and in no part should such conditions arise from which a sense of deprivation arises in it.',
  '… چاہیے اور کسی بھی حصے میں ایسے حالات نہیں ہونے چاہئیں جس سے اس میں احساسِ محرومی پیدا ہو۔',
  '… وشي، او په هېڅ برخه کې باید داسې حالات نه وي چې له امله یې پکې د محرومیت احساس پیدا شي.')
t.h('Sense of responsibility', 'احساسِ ذمہ داری', 'د مسؤولیت احساس')
P('If the performance of all the institutions of the country is good, and from the bureaucracy up to the ruling class everyone has this feeling that they are servants of the people and the people are part of them, then a sense of responsibility will naturally arise in all the institutions and individuals of the country, and this will help in the progress and welfare of the people.',
  'اگر ملک کے تمام اداروں کی کارکردگی اچھی ہوگی اور نوکرشاہی سے لے کر حکمران طبقے تک سب میں یہ احساس ہوگا کہ وہ عوام کے خادم ہیں اور عوام کا حصہ ہیں تو ملک کے تمام اداروں اور افراد میں فطری طور پر ایک احساسِ ذمہ داری ابھرے گا اور اس سے عوام کی ترقی و بہبود میں مدد ملے گی۔',
  'که د هېواد د ټولو ادارو کارکردګي ښه وي، او له دیوان‌سالارۍ نیولې تر واکمنې طبقې پورې په ټولو کې دا احساس وي چې دوی د خلکو خادمان دي او د خلکو برخه دي، نو د هېواد په ټولو ادارو او کسانو کې به په طبیعي ډول د مسؤولیت احساس راپورته شي او دا به د خلکو په پرمختګ او هوساینه کې مرسته وکړي.')
rec = BOOK.record(t, 'pak12-ch5-text-15', 'Chapter 5 text (15)', 'بابِ پنجم — متن (۱۵)', 'پنځم څپرکی — متن (۱۵)', 62, [113])

e = Builder()
L = lambda rows: e.group('lines', rows)
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Fill in the blanks with suitable words.', '1۔ خالی جگہوں کو مناسب الفاظ سے پُر کریں۔', '۱. تش ځایونه په مناسبو کلمو ډک کړئ.')
L([('i. ________ first presented the concept of the welfare state.', 'i۔ فلاحی ریاست کا تصور سب سے پہلے ________ نے پیش کیا۔', 'i. د هوساینې دولت تصور تر ټولو لومړی ________ وړاندې کړ.'),
   ('ii. Hazrat Umar (RA) divided the empire into ________ administrative provinces.', 'ii۔ حضرت عمرؓ نے سلطنت کو ________ انتظامی صوبوں میں تقسیم کیا۔', 'ii. حضرت عمر (رض) سلطنت په ________ اداري ولایتونو ووېشله.'),
   ('iii. The total number of seats of the Senate is ________ .', 'iii۔ سینیٹ کی کل نشستوں کی تعداد ________ ہے۔', 'iii. د سنا د ټولو څوکیو شمېر ________ دی.'),
   ('iv. The foremost condition for good governance is the rule of ________ .', 'iv۔ بہتر اسلوبِ حکمرانی کے لیے اولین شرط ________ کی حکمرانی ہے۔', 'iv. د ښې حکومتولۍ لومړنی شرط د ________ حاکمیت دی.'),
   ('v. The new local and district system has completed its first fixed term ________ in 2005.', 'v۔ نیا بلدیاتی و ضلعی نظام اپنی پہلی مقررہ معیاد ________ 2005ء میں مکمل کر چکا ہے۔', 'v. نوي ښاروالۍ او ولسوالۍ نظام خپله لومړۍ ټاکلې موده ________ په ۲۰۰۵ز کې بشپړه کړې.')])
e.p('2. Choose the correct answer.', '2۔ درست جواب کا انتخاب کریں۔', '۲. سم ځواب وټاکئ.')
L([('i. According to the 1973 constitution, what kind of state is Pakistan? (parliamentary, unitary, presidential, federal)', 'i۔ 1973ء کے آئین کے مطابق پاکستان کیسی مملکت ہے؟ (پارلیمانی، وحدانی، صدارتی، وفاقی)', 'i. د ۱۹۷۳ز د اساسي قانون له مخې پاکستان څه ډول دولت دی؟ (پارلماني، واحد، ولسمشریز، فدرالي)'),
   ('ii. What is the total number of seats in the Senate? (70, 80, 90, 104)', 'ii۔ سینیٹ میں نشستوں کی کل تعداد کتنی ہے؟ (70، 80، 90، 104)', 'ii. په سنا کې د څوکیو ټول شمېر څومره دی؟ (۷۰، ۸۰، ۹۰، ۱۰۴)'),
   ('iii. How many total seats does the province of Khyber Pakhtunkhwa have in the National Assembly? (40, 42, 55, 44)', 'iii۔ قومی اسمبلی میں صوبہ خیبر پختونخوا کی کل کتنی نشستیں ہیں؟ (40، 42، 55، 44)', 'iii. په ملي اسمبلۍ کې د خیبر پښتونخوا ولایت ټولې څو څوکۍ دي؟ (۴۰، ۴۲، ۵۵، ۴۴)'),
   ('iv. After how many years is the election of the members of the National Assembly held? (3 years, 4 years, 5 years, 6 years)', 'iv۔ قومی اسمبلی کے ممبران کا انتخاب کتنے سال بعد ہوتا ہے؟ (3 سال، 4 سال، 5 سال، 6 سال)', 'iv. د ملي اسمبلۍ د غړو ټاکنه له څو کلونو وروسته کېږي؟ (۳ کاله، ۴ کاله، ۵ کاله، ۶ کاله)'),
   ('v. Into how many provinces had Hazrat Umar Farooq (RA) divided his empire? (4, 6, 7, 8)', 'v۔ حضرت عمر فاروقؓ نے اپنی سلطنت کو کتنے صوبوں میں تقسیم کیا تھا؟ (4، 6، 7، 8)', 'v. حضرت عمر فاروق (رض) خپله سلطنت په څو ولایتونو وېشلې وه؟ (۴، ۶، ۷، ۸)')])
e.p('3. Write short answers.', '3۔ مختصر جوابات تحریر کریں۔', '۳. لنډ ځوابونه ولیکئ.')
L([('i. What measures did Hazrat Umar Farooq (RA) take for public welfare?', 'i۔ حضرت عمر فاروقؓ نے رفاہِ عامہ کے لیے کون سے اقدامات کیے؟', 'i. حضرت عمر فاروق (رض) د عامې هوساینې لپاره کوم ګامونه پورته کړل؟'),
   ('ii. What method did Hazrat Umar Farooq (RA) adopt for the appointment of officials?', 'ii۔ حضرت عمر فاروقؓ نے عمال کی تقرری کے لیے کیا طریقہ کار اپنایا؟', 'ii. حضرت عمر فاروق (رض) د عاملانو د ټاکلو لپاره کومه طریقه غوره کړه؟'),
   ('iii. What are the special powers of the President of Pakistan?', 'iii۔ صدرِ پاکستان کے خصوصی اختیارات کیا ہیں؟', 'iii. د پاکستان د ولسمشر ځانګړي واکونه کوم دي؟')])
ex = BOOK.record(e, 'pak12-ch5-exercise-1', 'Exercise (1)', 'مشق (۱)', 'تمرین (۱)', 62, [114])
issues = [{'id': 'pak12-pdf062', 'unit': 5, 'printedPage': 114,
           'description': 'Q1(v) prints “معیاد” (for “میعاد”) and its blank sits awkwardly before “2005ء”; Q2(iii) lists options in the order (40، 42، 55، 44); retained as printed. The printed page number on p.113 is obscured by the border ornament.'}]

if __name__ == '__main__':
    BOOK.save(62, [(5, rec), (5, ex)], issues=issues)
