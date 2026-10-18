"""Pak Studies XII PDF113 (spread): left page re-scans p.210 (duplicate of PDF112); p.211 — Ch.11 مشق Q1–Q2."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
e = Builder()
L = lambda rows: e.group('lines', rows)
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Four answers are given below for each question. Choose the correct answer.', '1۔ ذیل میں ہر سوال کے چار جواب درج ہیں۔ آپ درست جواب کا انتخاب کیجیے:۔', '۱. لاندې د هرې پوښتنې څلور ځوابونه ورکړل شوي. سم ځواب وټاکئ.')
L([('i. In 1947 the population of Pakistan was — (25 million, 30 million, 33 million, 35 million)', 'i۔ 1947ء میں پاکستان کی آبادی تھی۔ (25 ملین، 30 ملین، 33 ملین، 35 ملین)', 'i. په ۱۹۴۷ز کې د پاکستان نفوس و — (۲۵ میلیونه، ۳۰ میلیونه، ۳۳ میلیونه، ۳۵ میلیونه)'),
   ('ii. In 1950, at what number was Pakistan in terms of population? (12th, 14th, 16th, 18th)', 'ii۔ 1950ء میں آبادی کے لحاظ سے پاکستان کس نمبر پر تھا۔ (12 ویں، 14 ویں، 16 ویں، 18 ویں)', 'ii. په ۱۹۵۰ز کې د نفوس له پلوه پاکستان په کوم نمبر کې و؟ (۱۲م، ۱۴م، ۱۶م، ۱۸م)'),
   ('iii. According to the statistics of 2004 the number of unemployed individuals in Pakistan is — (30 lakh, 32 lakh, 36 lakh, 40 lakh)', 'iii۔ 2004ء کے اعداد و شمار کے مطابق پاکستان میں بے روزگار افراد کی تعداد ہے۔ (30 لاکھ، 32 لاکھ، 36 لاکھ، 40 لاکھ)', 'iii. د ۲۰۰۴ز د شمېرو له مخې په پاکستان کې د بې‌روزګارو کسانو شمېر دی — (۳۰ لکه، ۳۲ لکه، ۳۶ لکه، ۴۰ لکه)'),
   ('iv. According to the statistics of 2014, for how many individuals is there one doctor in Pakistan? (1400, 1073, 1000, 1088)', 'iv۔ 2014ء کے اعداد و شمار کے مطابق پاکستان میں کتنے افراد کے لیے ایک ڈاکٹر ہے۔ (1400، 1073، 1000، 1088)', 'iv. د ۲۰۱۴ز د شمېرو له مخې په پاکستان کې د څو کسانو لپاره یو ډاکټر دی؟ (۱۴۰۰، ۱۰۷۳، ۱۰۰۰، ۱۰۸۸)'),
   ('v. According to the estimates of 2004 Pakistan’s literacy rate is — (40 per cent, 45 per cent, 50 per cent, 54 per cent)', 'v۔ 2004ء کے اندازوں کے مطابق پاکستان کی شرح خواندگی ہے۔ (40 فی صد، 45 فی صد، 50 فی صد، 54 فی صد)', 'v. د ۲۰۰۴ز د اټکلونو له مخې د پاکستان د سواد کچه ده — (۴۰ سلنه، ۴۵ سلنه، ۵۰ سلنه، ۵۴ سلنه)')])
e.p('2. Fill in the blanks with suitable words.', '2۔ خالی جگہوں کو موزوں الفاظ سے پُر کریں:۔', '۲. تش ځایونه په مناسبو کلمو ډک کړئ.')
L([('1. The total area of Pakistan is ________ square kilometres.', '1۔ پاکستان کا کل رقبہ ________ مربع کلومیٹر ہے۔', '۱. د پاکستان ټوله ساحه ________ مربع کیلومتره ده.'),
   ('2. At present an annual increase of ________ million individuals is taking place in the population of Pakistan.', '2۔ اس وقت پاکستان کی آبادی میں ________ ملین افراد کا سالانہ اضافہ ہو رہا ہے۔', '۲. اوس مهال د پاکستان په نفوس کې کلنی ________ میلیونه کسان زیاتېږي.'),
   ('3. In 2004 Pakistan came to number ________ in the world in terms of population.', '3۔ 2004ء میں پاکستان دُنیا میں آبادی کے لحاظ سے ________ نمبر پر آ گیا ہے۔', '۳. په ۲۰۰۴ز کې پاکستان د نفوس له پلوه په نړۍ کې ________ نمبر ته راغی.'),
   ('4. ________ per cent of children of primary-school-going age are not admitted to school.', '4۔ پرائمری سکول میں جانے والی عمر کے ________ فی صد بچے سکول میں داخل نہیں ہو پاتے۔', '۴. د لومړني ښوونځي د عمر ________ سلنه ماشومان ښوونځي ته نه داخلېږي.'),
   ('5. According to the estimates of 2004 our literacy rate is ________ per cent.', '5۔ 2004ء کے اندازوں کے مطابق ہماری شرح خواندگی ________ فی صد ہے۔', '۵. د ۲۰۰۴ز د اټکلونو له مخې زموږ د سواد کچه ________ سلنه ده.')])
ex = BOOK.record(e, 'pak12-ch11-exercise-1', 'Exercise (1)', 'مشق (۱)', 'تمرین (۱)', 113, [211])
ex['sourceNote'] = 'The left page of this spread is a second scan of p.210 (already transcribed from PDF112) and is not repeated. The exercise continues on p.212 (PDF114).'
issues = [{'id': 'pak12-pdf113', 'unit': 11, 'printedPage': 210, 'description': 'PDF113’s left page duplicates p.210 (also in PDF112); only p.211 is transcribed here. Q2 items use Urdu-Indic numerals (ا، ۲ …); normalised.'}]

if __name__ == '__main__':
    BOOK.save(113, [(11, ex)], issues=issues)
