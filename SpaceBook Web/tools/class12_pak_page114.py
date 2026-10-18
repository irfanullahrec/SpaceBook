"""Pak Studies XII PDF114–117: p.212 Ch.11 مشق Q3 (chapter 11 complete); back matter (Khatm-e-Nubuwwat frames, Al-Hujurat 10, National Anthem and imprint).

PDF114 = p.211 (duplicate of PDF113) + p.212; PDF115 = p.212 (duplicate) + unnumbered page with two framed texts;
PDF116 = unnumbered page with Al-Hujurat 10 + the framed page again (duplicate); PDF117 = back page: National Anthem and imprint.
Run with the PDF number as argument (114–117)."""
import sys
from class12_book_common import Book, Builder

BOOK = Book('pak')


def q3():
    e = Builder()
    e.p('3. Give short answers:', '3۔ مختصر جواب دیجیے:۔', '۳. لنډ ځوابونه ورکړئ:')
    e.group('lines', [('1. Review the situation of unemployment in the country.', '1۔ ملک میں بے روزگاری کی صورتِ حال کا جائزہ لیں۔', '۱. په هېواد کې د بې‌روزګارۍ حالت وڅېړئ.'),
                      ('2. How does the growing population affect economic progress?', '2۔ بڑھتی ہوئی آبادی کس طرح معاشی ترقی کو متاثر کرتی ہے؟', '۲. زیاتېدونکی نفوس څنګه پر اقتصادي پرمختګ اغېز کوي؟'),
                      ('3. With what problems is our agricultural sector faced?', '3۔ ہمارا زرعی شعبہ کن مسائل سے دوچار ہے؟', '۳. زموږ کرنیزه برخه له کومو ستونزو سره مخ ده؟'),
                      ('4. Write a note on the factors producing environmental pollution.', '4۔ ماحولیاتی آلودگی پیدا کرنے والے عوامل پر نوٹ لکھیں۔', '۴. د چاپېریالي ککړتیا د لاملونو په اړه یادښت ولیکئ.')])
    r = BOOK.record(e, 'pak12-ch11-exercise-2', 'Exercise (2)', 'مشق (۲)', 'تمرین (۲)', 114, [212])
    r['sourceNote'] = 'The left page of PDF114 is a second scan of p.211 (transcribed from PDF113). Faint show-through of the following framed page is visible on p.212 and is not content.'
    return r


def frames():
    b = Builder()
    b.h('Back matter: Finality of Prophethood', 'آخری صفحات: ختمِ نبوت', 'وروستۍ پاڼې: د نبوت ختم')
    b.p('Allah Almighty ordains: “(Our master) Muhammad (peace be upon him) is not the father of any of your men, but he is the Messenger of Allah Almighty and the Seal of the Prophets.” (Surah Al-Ahzab: verse 40)',
        'اللہ تعالیٰ کا ارشاد ہے: (سیدنا) محمد صلی اللہ علیہ وسلم تمہارے مردوں میں سے کسی کے باپ نہیں بلکہ اللہ تعالیٰ کے رسول اور خاتم الانبیاء ہیں۔ (سورہ الاحزاب: آیت ۴۰)',
        'الله تعالی فرمايي: "(زموږ سردار) محمد (صلی الله علیه وسلم) ستاسو له نارینه وو د هېچا پلار نه دی، بلکې د الله تعالی رسول او خاتم الانبیاء دی." (سورة الاحزاب: ۴۰ آیت)')
    b.p('(Our master) Hazrat Muhammad, the Messenger of Allah, the Seal of the Prophets (peace and blessings of Allah be upon him, his family and companions), ordains: “I am the last prophet. There is no prophet after me.”',
        '(سیدنا) حضرت محمد رسول اللہ خاتم النبیین صلی اللہ علیہ وعلیٰ آلہ واصحابہ وسلم کا ارشاد ہے: ’’میں آخری نبی ہوں۔ میرے بعد کوئی نبی نہیں ہے‘‘',
        '(زموږ سردار) حضرت محمد د الله رسول خاتم النبیین (صلی الله علیه وعلی آله واصحابه وسلم) فرمايي: "زه وروستی نبي یم. له ما وروسته هېڅ نبي نشته."')
    r = BOOK.record(b, 'pak12-bm-khatm-nubuwwat', 'Back matter: Finality of Prophethood', 'آخری صفحات: ختمِ نبوت', 'وروستۍ پاڼې: د نبوت ختم', 115, [])
    r['sourceNote'] = 'Unnumbered page after p.212 with two framed texts inside floral borders (ornament not reproduced). The left page of PDF115 is a second scan of p.212.'
    return r


def hujurat():
    b = Builder()
    b.p('“The believers are but brothers to one another; so make peace between your two brothers, and keep fearing Allah, so that mercy may be shown to you.” (Surah Al-Hujurat: 10)',
        'مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحم کیا جائے۔ (سورۃ الحجرات: ۱۰)',
        '"مؤمنان خو یو د بل وروڼه دي؛ نو د خپلو دوو وروڼو ترمنځ روغه وکړئ، او له الله ووېرېږئ، څو پر تاسو رحم وشي." (سورة الحجرات: ۱۰)')
    r = BOOK.record(b, 'pak12-bm-hujurat', 'Back matter: Al-Hujurat 10', 'آخری صفحات: سورۃ الحجرات ۱۰', 'وروستۍ پاڼې: سورة الحجرات ۱۰', 116, [])
    r['sourceNote'] = 'Unnumbered framed page (floral border not reproduced). The right page of PDF116 repeats the Finality-of-Prophethood page (PDF115).'
    return r


def anthem():
    b = Builder()
    b.h('Back page: National Anthem and printing details', 'آخری صفحہ: قومی ترانہ اور طباعت کی تفصیلات', 'وروستۍ پاڼه: ملي سرود او د چاپ جزییات')
    b.h('قومی ترانہ', 'قومی ترانہ', 'قومی ترانہ')
    for ln in ['پاک سرزمین شاد باد — کشورِ حسین شاد باد', 'تو نشانِ عزمِ عالی شان — ارضِ پاکستان', 'مرکزِ یقین شاد باد', 'پاک سرزمین کا نظام — قوتِ اخوتِ عوام',
               'قوم، ملک، سلطنت — پائندہ تابندہ باد', 'شاد باد منزلِ مراد', 'پرچمِ ستارہ و ہلال — رہبرِ ترقی و کمال', 'ترجمانِ ماضی شانِ حال — جانِ استقبال', 'سایۂ خدائے ذوالجلال']:
        b.p(ln, ln, ln)
    b.p('Code No.: PSP/MPP-38-135-2122(O) | Quantity: 81,935 | Printer: Muslim Printing Press, Lahore',
        'کوڈ نمبر: PSP/MPP-38-135-2122(O) | تعداد: 81,935 | مطبع: مسلم پرنٹنگ پریس لاہور',
        'کوډ شمېره: PSP/MPP-38-135-2122(O) | شمېر: ۸۱,۹۳۵ | چاپخونه: مسلم پرنټنګ پرېس لاهور')
    r = BOOK.record(b, 'pak12-back-cover', 'Back page: National Anthem and printing details', 'آخری صفحہ: قومی ترانہ اور طباعت کی تفصیلات', 'وروستۍ پاڼه: ملي سرود او د چاپ جزییات', 117, [])
    r['sourceNote'] = 'The National Anthem is shown in Urdu in all language views (same treatment as the other Class 12 books).'
    return r


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 114
    if n == 114:
        BOOK.save(114, [(11, q3())], issues=[{'id': 'pak12-pdf114', 'unit': 11, 'printedPage': 211, 'description': 'PDF114’s right page duplicates p.211 (also in PDF113); only p.212 is transcribed here.'}])
    elif n == 115:
        BOOK.save(115, [(11, frames())], issues=[{'id': 'pak12-pdf115', 'unit': 11, 'printedPage': 212, 'description': 'PDF115’s left page duplicates p.212 (also in PDF114); the right page is an unnumbered framed back-matter page.'}])
    elif n == 116:
        BOOK.save(116, [(11, hujurat())], issues=[{'id': 'pak12-pdf116', 'unit': 11, 'printedPage': 212, 'description': 'PDF116’s right page duplicates the framed Finality-of-Prophethood page from PDF115.'}])
    elif n == 117:
        BOOK.save(117, [(11, anthem())], complete_units=[11])
