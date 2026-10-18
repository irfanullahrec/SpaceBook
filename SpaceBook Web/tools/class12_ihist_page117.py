"""Islamic History XII PDF117: p.224 — Bibliography (table 2); inside back cover — Qur'an 33:40 and two hadiths. PDF118: back cover. Run: python class12_ihist_page117.py [118]"""
import sys
from class12_ihist_common import BOOK, Builder, rec, S

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

ROWS = [
    (13, 'Assi Salah Khilafat-e-Rashidah', 'اَسی سالہ خلافتِ راشدہ', 'اتیا کلنه خلافت راشده', 'Mi\'raj al-Din', 'معراج الدین', 'معراج الدین', 'Hafiz Mas\'ud Amjad', 'حافظ مسعود امجد', 'حافظ مسعود امجد'),
    (14, 'Musalman Europe mein', 'مسلمان یورپ میں', 'مسلمانان په اروپا کې', 'Shaykh Muhammad Ihsan al-Haqq Sulayman, M.A.', 'شیخ محمد احسان الحق سلیمان ایم اے', 'شیخ محمد احسان الحق سلیمان، ایم اې', 'Qaumi Kutub Khanah, Lahore', 'قومی کتب خانہ، لاہور', 'قومي کتب خانه، لاهور'),
    (15, 'Khutbat-e-Rasul', 'خطباتِ رسول', 'خطبات رسول', 'Professor Imtiaz Ahmad', 'پروفیسر امتیاز احمد', 'پروفیسر امتیاز احمد', 'Matbu\'at Hurmat, Rawalpindi', 'مطبوعات حرمت راولپنڈی', 'مطبوعات حرمت، راولپنډۍ'),
    (16, 'Khalifah Harun al-Rashid', 'خلیفہ ہارون الرشید', 'خلیفه هارون الرشید', 'Rais Ahmad Ja\'fari', 'رئیس احمد جعفری', 'رئیس احمد جعفري', 'Maqbool Academy, Shah \'Alam Market, Lahore', 'مقبول اکیڈمی، شاہ عالم مارکیٹ لاہور', 'مقبول اکېډمي، شاه عالم مارکېټ، لاهور'),
    (17, 'Al-Baramikah', 'البرامکہ', 'البرامکه', 'Mawlana Abd al-Razzaq Kanpuri', 'مولانا عبدالرزاق کانپوری', 'مولانا عبدالرزاق کانپوري', 'Nafees Academy, Urdu Bazar, Lahore', 'نفیس اکیڈمی اردو بازار لاہور', 'نفیس اکېډمي، اردو بازار، لاهور'),
    (18, 'Tarikh-e-Islam', 'تاریخِ اسلام', 'د اسلام تاریخ', 'Dr. Hamid al-Din', 'ڈاکٹر حمید الدین', 'ډاکټر حمیدالدین', 'Ferozsons, Lahore', 'فیروز سنز، لاہور', 'فیروز سنز، لاهور'),
    (19, 'Tarikh-e-Islam', 'تاریخِ اسلام', 'د اسلام تاریخ', 'Shah Mu\'in al-Din', 'شاہ معین الدین', 'شاه معین الدین', 'Qur\'an Limited, Urdu Bazar, Lahore', 'قرآن لمیٹڈ اردو بازار لاہور', 'قرآن لمیټډ، اردو بازار، لاهور'),
    (20, 'The Messanger', 'The Messanger', 'The Messanger', 'R. V. C. Bodley; tr. Muhammad Amin Faridi', 'آر۔ وی۔ سی۔ باڈلے، ترجمہ: محمد امین فریدی', 'ار. وي. سي. باډلي؛ ژباړه: محمد امین فریدي', 'Maktabah \'Aliyah, Lahore', 'مکتبہ عالیہ، لاہور', 'مکتبه عالیه، لاهور'),
    (21, 'History of the Arabs', 'History of the Arabs', 'History of the Arabs', 'P.K HI. HI.; Mazhar al-Haqq', 'P.K HI. HI. مظہر الحق', 'P.K HI. HI.؛ مظهر الحق', 'University Book Agency, Peshawar', 'یونیورسٹی بک ایجنسی، پشاور', 'یونیورسټي بک اېجنسي، پېښور'),
    (22, 'A History of Early Islam', 'A History of Early Islam', 'A History of Early Islam', '', '', '', '', '', ''),
    (23, 'A Short History of Saracens', 'A Short History of Saracens', 'A Short History of Saracens', 'Amir \'Ali Sayyid', 'امیر علی سیّد', 'امیر علي سید', 'Macmillan Co. Ltd, New York', 'Macmillan Co. Ltd New York', 'Macmillan Co. Ltd، نیویارک'),
    (24, 'The Moors In Spain', 'The Moors In Spain', 'The Moors In Spain', 'Stanely Lane Pools', 'Stanely Lane Pools', 'Stanely Lane Pools', 'United Publishers, Lahore', 'یونائیٹڈ پبلشرز لاہور', 'یونایټډ پبلشرز، لاهور'),
    (25, 'outlInes of Islamic', 'outlInes of Islamic', 'outlInes of Islamic', 'K.Ali', 'K.Ali', 'K.Ali', '', '', ''),
    (26, 'Sayyarah Digest, Rasul Number', 'سیارہ ڈائجسٹ رسول نمبر', 'سیاره ډایجسټ، رسول ګڼه', 'Sulayman Yusuf', 'سلیمان یوسف', 'سلیمان یوسف', '', '', ''),
]


def p117():
    b = Builder()
    en = [[str(r[0]), r[1], r[4], r[7]] for r in ROWS]
    ur = [[str(r[0]).translate(D), r[2], r[5], r[8]] for r in ROWS]
    ps = [[str(r[0]).translate(D), r[3], r[6], r[9]] for r in ROWS]
    b.table('ihist12-l42-bibliography-2', ['No.', 'Name of book', 'Author/Translator', 'Publisher'], en,
            ['نمبر شمار', 'نام کتاب', 'مصنف/مترجم', 'پبلشر'], ['شمېره', 'د کتاب نوم', 'لیکوال/ژباړن', 'خپرندوی'], ur, ps)
    r1 = rec(b, 42, 224, 117, [224])
    t = Builder()
    S(t, [(('Allah Almighty says:', 'اللہ تعالیٰ کا ارشاد ہے:', 'الله تعالی فرمايي:'),
           ('"Muhammad (peace and blessings of Allah be upon him, his family and companions) is not the father of any of your men, but he is the Messenger of Allah Almighty and the Seal of the Prophets." (Surah al-Ahzab: 40)', '”محمد صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم تمہارے مردوں میں سے کسی کے باپ نہیں بلکہ اللہ تعالیٰ کے رسول اور خاتم الانبیاء ہیں۔“ (سورۃ الاحزاب: ۴۰)', '«محمد صلی الله علیه وعلی آله واصحابه وسلم ستاسو د نارینه وو څخه د هېچا پلار نه دی، بلکې د الله تعالی رسول او د انبیاوو خاتم دی.» (سورة الاحزاب: ۴۰)')),
          (('Hazrat Muhammad, the Messenger of Allah, Khatam al-Nabiyyin (peace and blessings of Allah be upon him, his family and companions) says:', 'حضرت محمد رسول اللہ خاتم النبیین صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کا ارشاد ہے:', 'حضرت محمد رسول الله خاتم النبیین صلی الله علیه وعلی آله واصحابه وسلم فرمايي:'),
           ('"I am the last Prophet. After me there is no prophet."', '”میں آخری نبی ہوں۔ میرے بعد کوئی نبی نہیں ہے۔“', '«زه وروستی نبي یم؛ زما وروسته هېڅ نبي نشته.»')),
          (None, ('"The curse of Allah Almighty is upon the one who gives a bribe and the one who takes it." (Ibn Majah)', '”رشوت دینے اور لینے والے پر اللہ تعالیٰ کی لعنت ہے۔“ (ابن ماجہ)', '«پر بډې ورکوونکي او اخیستونکي د الله تعالی لعنت دی.» (ابن ماجه)'))])
    r2 = rec(t, 42, None, 117, [None], kind='cover')
    BOOK.save(117, [(42, r1), (42, r2)], issues=[{'id': 'ihist12-pdf117', 'unit': 42, 'printedPage': 224,
               'description': 'Bibliography p.224 continues the table (items 13–26). Items 20–26 are printed outside the ruled table with irregular columns; cells left blank where nothing is printed; English titles and names kept exactly as printed ("The Messanger", "P.K HI. HI.", "Stanely Lane Pools", "outlInes of Islamic"). The left half of the spread is the unnumbered inside back cover (Qur\'an 33:40, two hadiths) — transcribed; ornamental border not reproduced. Finger in scan excluded.'}])


def p118():
    t = Builder()
    S(t, [(None, ('All rights are reserved with the Khyber Pakhtunkhwa Textbook Board, Peshawar.', 'جملہ حقوق بحق خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور محفوظ ہیں۔', 'ټول حقوق د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور سره خوندي دي.')),
          (None, ('Prepared by: Khyber Pakhtunkhwa Textbook Board, Peshawar', 'تیار کردہ: خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'چمتو کوونکی: د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')),
          (None, ('Approved by: Federal Ministry of Education, Government of Pakistan, Islamabad, for all colleges of Pakistan', 'منظور شدہ: وفاقی وزارتِ تعلیم، حکومتِ پاکستان، اسلام آباد برائے جملہ کالجز پاکستان', 'منظور شوی: د پاکستان حکومت فدرالي د پوهنې وزارت، اسلام اباد، د پاکستان د ټولو کالجونو لپاره')),
          (('National Anthem', 'قومی ترانہ', 'ملي ترانه'),
           ('The back cover prints the National Anthem of Pakistan (by Hafeez Jalandhari). Its text is not reproduced here; it praises the sacred land of Pakistan, prays for its prosperity and permanence, and calls the flag of crescent and star the guide of progress and perfection.', 'پچھلے سرورق پر پاکستان کا قومی ترانہ (حفیظ جالندھری) چھپا ہوا ہے۔ اس کا متن یہاں نقل نہیں کیا گیا؛ اس میں پاکستان کی پاک سرزمین کی تعریف، اس کی خوشحالی اور پائندگی کی دعا، اور ہلالی پرچم کو ترقی و کمال کا رہبر کہا گیا ہے۔', 'په شاتني پوښ کې د پاکستان ملي ترانه (حفیظ جالندهري) چاپ شوې ده. متن یې دلته نه دی نقل شوی؛ په هغې کې د پاکستان د پاکې خاورې ستاینه، د هغې د سوکالۍ او تلپاتې کېدو دعا، او د هلال او ستوري بیرغ د پرمختګ او کمال لارښود بلل شوی.')),
          (None, ('Code number: SP/QKK-14-57-2223(O). Number of copies: 12,030. Printer: Qaumi Kutub Khanah, Lahore.', 'کوڈ نمبر: SP/QKK-14-57-2223(O)۔ تعداد: 12,030۔ مطبع: قومی کتب خانہ، لاہور۔', 'کوډ نمبر: SP/QKK-14-57-2223(O). شمېر: 12,030. چاپخونه: قومي کتب خانه، لاهور.'))])
    BOOK.save(118, [(42, rec(t, 42, None, 118, [None], kind='backcover'))], complete_units=[42], issues=[{'id': 'ihist12-pdf118', 'unit': 42, 'printedPage': None,
               'description': 'Back cover (scan split across the two halves; the right edge is cut). The National Anthem (Hafeez Jalandhari, d.1982) is summarised, not transcribed, per the copyright rule. The price is cut off at the scan edge and is not given.'}])


if __name__ == '__main__':
    p118() if sys.argv[1:] == ['118'] else p117()
