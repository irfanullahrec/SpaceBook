"""Islamic History XII PDF116: p.222 — end of lesson 41, exercise; p.223 — Lesson 42 Bibliography (table 1). Run: python class12_ihist_page116.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

ROWS = [
    ('Tarikh Tabari', 'تاریخ طبری', 'تاریخ طبري', 'Muhammad bin Jarir al-Basri; tr. Sayyid Ibrahim', 'محمد بن جریر البصری، ترجمہ سیّد ابراہیم', 'محمد بن جریر البصري؛ ژباړه سید ابراهیم', 'Nafees Academy, Karachi', 'نفیس اکیڈمی، کراچی', 'نفیس اکېډمي، کراچۍ'),
    ('Rasul-e-Rahmat', 'رسولِ رحمت', 'رسول رحمت', 'Riaz Ahmad Sayyid', 'ریاض احمد سیّد', 'ریاض احمد سید', 'Institute of Seerat Studies, Islamabad', 'انسٹیٹیوٹ آف سیرت سٹڈیز اسلام آباد', 'د سیرت مطالعاتو انسټیټیوټ، اسلام اباد'),
    ('Hadi-e-\'Alam', 'ہادیٔ عالم', 'هادي عالم', 'Muhammad Wali Razi', 'محمد ولی رازی', 'محمد ولي رازي', 'Dar al-\'Ulum, Karachi', 'دارالعلوم کراچی', 'دارالعلوم، کراچۍ'),
    ('Ma\'mulat-e-Mustafa', 'معمولاتِ مصطفیٰ', 'معمولات مصطفی', 'Sufi Muhammad Akram Madani', 'صوفی محمد اکرم مدنی', 'صوفي محمد اکرم مدني', 'Book Corner, Main Bazar, Jhelum', 'بک کارنر مین بازار جہلم', 'بک کارنر، مین بازار، جهلم'),
    ('Hazrat \'Umar Faruq (may Allah be pleased with him)', 'حضرت عمر فاروق رضی اللہ تعالیٰ عنہ', 'حضرت عمر فاروق رضي الله تعالی عنه', 'Muhammad Husayn Haykal; translation', 'محمد حسین ہیکل ترجمہ', 'محمد حسین هیکل؛ ژباړه', 'Habib Ashar, Maktabah Meri Library, Lahore', 'حبیب اشعر مکتبہ میری لائبریری لاہور', 'حبیب اشعر، مکتبه میري لایبرېري، لاهور'),
    ('Khilafat-e-Andalus', 'خلافتِ اندلس', 'خلافت اندلس', 'Nawab Dhu al-Qadr Jang', 'نواب ذوالقدر جنگ', 'نواب ذوالقدر جنګ', 'Maktabah al-Quraysh, Lahore', 'مکتبہ القریش، لاہور', 'مکتبه القریش، لاهور'),
    ('Tarikh Ibn Kathir', 'تاریخ ابن کثیر', 'تاریخ ابن کثیر', '\'Imad al-Din Ibn Kathir', 'عماد الدین ابن کثیر', 'عمادالدین ابن کثیر', 'Nafees Academy, Karachi', 'نفیس اکیڈمی، کراچی', 'نفیس اکېډمي، کراچۍ'),
    ('Tabaqat Ibn Sa\'d', 'طبقات ابن سعد', 'طبقات ابن سعد', 'tr. Allama Abdullah', 'ترجمہ علامہ عبداللہ', 'ژباړه علامه عبدالله', 'Nafees Academy, Karachi', 'نفیس اکیڈمی، کراچی', 'نفیس اکېډمي، کراچۍ'),
    ('Tarikh Ibn Khaldun', 'تاریخ ابن خلدون', 'تاریخ ابن خلدون', 'tr. Hakim Ahmad Husayn', 'ترجمہ حکیم احمد حسین', 'ژباړه حکیم احمد حسین', 'Nafees Academy, Karachi', 'نفیس اکیڈمی، کراچی', 'نفیس اکېډمي، کراچۍ'),
    ('Khutbat-e-Sirat-e-Muhammad', 'خطباتِ سیرۃ محمد', 'خطبات سیرة محمد', 'F. D. Chaudhry', 'انیف ڈی چودھری', 'اېف ډي چوهدري', 'Nawabad, Wah Cantt', 'نواب آباد، واہ کینٹ', 'نواب اباد، واه کېنټ'),
    ('Rahmat al-lil-\'Alamin', 'رحمت اللعالمین', 'رحمة للعالمین', 'Qadi Muhammad Sulayman Mansurpuri', 'قاضی محمد سلیمان منصور پوری', 'قاضي محمد سلیمان منصورپوري', 'Shaykh Ghulam Ali and Sons, Lahore', 'شیخ غلام علی اینڈ سنز لاہور', 'شیخ غلام علي او زامن، لاهور'),
    ('Nuqush', 'نقوش', 'نقوش', 'Muhammad Tufayl', 'محمد طفیل', 'محمد طفیل', 'Idarah Farogh-e-Amjad, Lahore', 'ادارہ فروغِ امجد، لاہور', 'اداره فروغ امجد، لاهور'),
]


def p116():
    b = Builder()
    S(b, [(None, ('… he wants to obtain progress, but instead of progress decline alone has become his destiny. One will have to reflect seriously on this issue: in what thing lies the secret of our real progress? Undoubtedly the Qur\'an and Sunnah alone are the guarantors of our progress. In their light, acquiring modern sciences, we can obtain our lost place again.', 'کر ترقی حاصل کرنا چاہتا ہے لیکن ترقی کی بجائے تنزل ہی اس کا مقدر بن گیا ہے۔ اس مسئلے پر سنجیدگی سے غور کرنا ہو گا کہ ہماری حقیقی ترقی کا راز کس چیز میں ہے۔ بلاشبہ قرآن و سنت ہی ہماری ترقی کے ضامن ہیں۔ ان کی روشنی میں ہم جدید علوم حاصل کر کے دوبارہ اپنا کھویا ہوا مقام حاصل کر سکتے ہیں۔', '… شوی پرمختګ غواړي، خو د پرمختګ پر ځای یې ښکته‌والی برخلیک شوی. پر دې مسئله باید جدي غور وشي چې زموږ د اصلي پرمختګ راز په څه کې دی. بې‌له شکه قرآن او سنت زموږ د پرمختګ ضامن دي؛ د هغوی په رڼا کې نوي علوم ترلاسه کولی او خپل ورک شوی مقام بیا موندلی شو.'))])
    b.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    L(b, [('1. Review the social progress of Andalus in the era of the Banu Umayyah.', '۱۔ بنو امیہ کے دور میں اندلس کی معاشرتی ترقی کا جائزہ لیں۔', '۱. د بنو امیه په دوره کې د اندلس د ټولنیز پرمختګ کتنه وکړئ.'),
          ('2. Throw light on the agricultural progress of Spain.', '۲۔ سپین کی زرعی ترقی پر روشنی ڈالیں۔', '۲. د اسپانیا پر کرنیز پرمختګ رڼا واچوئ.'),
          ('3. State the industrial progress of Andalus in your own words.', '۳۔ اندلس کی صنعتی ترقی اپنے الفاظ میں بیان کریں۔', '۳. د اندلس صنعتي پرمختګ په خپلو الفاظو بیان کړئ.'),
          ('4. Write a short note on the scholarly progress of Spain.', '۴۔ سپین کی علمی ترقی پر مختصر نوٹ تحریر کریں۔', '۴. د اسپانیا پر علمي پرمختګ لنډ یادښت ولیکئ.')])
    b.p('5. Fill in the blanks.', '۵۔ خالی جگہیں پر کریں۔', '۵. تشې ډکې کړئ.')
    L(b, [('a. The Muslims entered Spain in the capacity of ______.', 'الف: مسلمان سپین میں ______ کی حیثیت سے داخل ہوئے۔', 'الف. مسلمانان اسپانیا ته د ______ په توګه ننوتل.'),
          ('b. The capital of Islamic Spain was ______.', 'ب: اسلامی سپین کا دارالخلافہ ______ تھا۔', 'ب. د اسلامي اسپانیا پلازمېنه ______ وه.'),
          ('c. Spain was counted among the ______ countries of the world.', 'ج: سپین کا شمار دنیا کے ______ ملکوں میں ہوتا تھا۔', 'ج. اسپانیا د نړۍ په ______ هېوادونو کې شمېرل کېده.'),
          ('d. The income of Spain was ______ than the whole of Europe.', 'د: سپین کی آمدنی پورے یورپ سے ______ تھی۔', 'د. د اسپانیا عاید له ټولې اروپا ______ و.'),
          ('e. In Granada the gardens of ______ had world-wide fame.', 'ہ: غرناطہ میں ______ کے باغات عالمگیر شہرت کے حامل تھے۔', 'ه. په غرناطه کې د ______ باغونه نړیوال شهرت درلود.'),
          ('f. The ______ of Spain were sent to the whole world.', 'و: سپین کی ______ پوری دنیا میں بھیجی جاتی تھیں۔', 'و. د اسپانیا ______ ټولې نړۍ ته لېږل کېدل.'),
          ('g. The university of Cordoba was changed into ______.', 'ز: قرطبہ کی یونیورسٹی کو ______ میں بدل دیا۔', 'ز. د قرطبې پوهنتون په ______ بدل شو.')])
    r1 = rec(b, 41, 222, 116, [222], kind='exercise')
    t = Builder()
    t.h('Bibliography', 'کتابیات', 'کتابیات')
    t.p('The following books have been benefited from in preparing this book:', 'اس کتاب کی تیاری میں مندرجہ ذیل کتب سے استفادہ کیا گیا ہے:', 'د دې کتاب په چمتو کولو کې له لاندې کتابونو ګټه اخیستل شوې:')
    en = [[str(i + 1), r[0], r[3], r[6]] for i, r in enumerate(ROWS)]
    ur = [[str(i + 1).translate(D), r[1], r[4], r[7]] for i, r in enumerate(ROWS)]
    ps = [[str(i + 1).translate(D), r[2], r[5], r[8]] for i, r in enumerate(ROWS)]
    t.table('ihist12-l42-bibliography-1', ['No.', 'Name of book', 'Author/Translator', 'Publisher'], en,
            ['نمبر شمار', 'نام کتاب', 'مصنف/مترجم', 'پبلشر'], ['شمېره', 'د کتاب نوم', 'لیکوال/ژباړن', 'خپرندوی'], ur, ps)
    BOOK.save(116, [(41, r1), (42, rec(t, 42, 223, 116, [223], first=True))], complete_units=[41], issues=[{'id': 'ihist12-pdf116', 'unit': 42, 'printedPage': 223,
               'description': 'Bibliography p.223 rendered as a structured table. Printed forms kept: "محمد بن جریر البصری", "انیف ڈی چودھری", "حبیب اشعر مکتبہ میری لائبریری". Student circle around exercise item 1 excluded; no printed key for p.222. Finger in the scan excluded.'}])


if __name__ == '__main__':
    p116()
