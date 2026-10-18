"""Mutalia-e-Quran XII PDF230-231: back matter — KPTBB textbook feedback form (PDF230); inside back cover: national anthem (summarised), developer and print details (PDF231). Run: python class12_quran_page230.py [230|231]"""
import sys
from class12_quran_common import BOOK, Builder, rec

STATEMENTS = [
    'Overall the book is interesting and user friendly.',
    'The language and content of the book is age / grade appropriate and the content is free of grammatical and punctuation errors.',
    'Content is supported with examples from real life / culture.',
    'Contents / texts are authentic and updated.',
    'Pictures / diagrams / graphs / illustrations are informative, relevant and clear if not, then identify them.',
    'Activities, projects and additional work is suggested for reinforcement of concepts.',
    'Assessment achievements are thought provoking and comprise cognitive, psychomotor and effective skills.',
    'The textbook is easy to be covered within academic year.',
]
UR = [
    'مجموعی طور پر کتاب دلچسپ اور استعمال میں آسان ہے۔',
    'کتاب کی زبان اور مواد عمر / جماعت کے مطابق ہے اور مواد قواعد اور اوقاف کی غلطیوں سے پاک ہے۔',
    'مواد کو حقیقی زندگی / ثقافت کی مثالوں سے تقویت دی گئی ہے۔',
    'مواد / متن مستند اور تازہ ہیں۔',
    'تصاویر / خاکے / گراف / اشکال معلوماتی، متعلقہ اور واضح ہیں؛ اگر نہیں تو ان کی نشان دہی کریں۔',
    'تصورات کی پختگی کے لیے سرگرمیاں، منصوبے اور اضافی کام تجویز کیے گئے ہیں۔',
    'جانچ کی سرگرمیاں فکر انگیز ہیں اور ادراکی، حرکی اور مؤثر مہارتوں پر مشتمل ہیں۔',
    'درسی کتاب تعلیمی سال کے اندر آسانی سے مکمل کی جا سکتی ہے۔',
]
PS = [
    'په ټولیز ډول کتاب په زړه پورې او د کارولو لپاره اسانه دی.',
    'د کتاب ژبه او منځپانګه له عمر / ټولګي سره سمه ده او منځپانګه له ګرامري او ټکي‌ګذارۍ تېروتنو پاکه ده.',
    'منځپانګه د ریښتیني ژوند / کلتور په بېلګو پیاوړې شوې.',
    'منځپانګه / متنونه معتبر او تازه دي.',
    'انځورونه / ډیاګرامونه / ګرافونه / شکلونه معلوماتي، اړوند او روښانه دي؛ که نه وي، په ګوته یې کړئ.',
    'د مفاهیمو د پیاوړتیا لپاره فعالیتونه، پروژې او اضافي کار وړاندیز شوي.',
    'ارزونې فکر راپاروونکې دي او ادراکي، حرکي او اغېزمنې مهارتونه لري.',
    'درسي کتاب په یوه تعلیمي کال کې په اسانۍ بشپړېدای شي.',
]


def p230():
    b = Builder()
    b.h('Khyber Pakhtunkhwa Textbook Board — Textbook Feedback Form', 'خیبر پختونخوا ٹیکسٹ بک بورڈ — درسی کتاب پر رائے کا فارم', 'د خیبر پښتونخوا د درسي کتابونو بورډ — د درسي کتاب د نظر فورمه')
    b.p('Khyber Pakhtunkhwa Textbook Board, Phase-V, Hayatabad, Peshawar. Phone: 091-9217714-15; Fax: 091-9217163; Website: www.kptbb.gov.pk',
        'خیبر پختونخوا ٹیکسٹ بک بورڈ، فیز-۵، حیات آباد، پشاور۔ فون: 091-9217714-15؛ فیکس: 091-9217163؛ ویب سائٹ: www.kptbb.gov.pk',
        'د خیبر پښتونخوا د درسي کتابونو بورډ، پنځم فاز، حیات آباد، پېښور. ټیلیفون: 091-9217714-15؛ فکس: 091-9217163؛ وېب‌پاڼه: www.kptbb.gov.pk')
    b.table('mq12-bm-feedback', ['S#', 'Statement', 'Remarks'], [[str(i), s, ''] for i, s in enumerate(STATEMENTS, 1)],
            ['نمبر شمار', 'بیان', 'رائے'], ['شمېره', 'بیان', 'نظر'],
            [[str(i), s, ''] for i, s in enumerate(UR, 1)], [[str(i), s, ''] for i, s in enumerate(PS, 1)])
    b.table('mq12-bm-feedback-2', ['Page No.', 'Observation/comments', 'Suggested amendment along with rationale'], [['', '', ''] for _ in range(5)],
            ['صفحہ نمبر', 'مشاہدہ / تبصرہ', 'مجوزہ ترمیم مع وجہ'], ['د مخ شمېره', 'لیدنه / تبصره', 'وړاندیز شوې سمون له دلیل سره'],
            [['', '', ''] for _ in range(5)], [['', '', ''] for _ in range(5)])
    b.p('General Remarks: ____  Name & Address: ____  Contact No. & Email: ____',
        'عمومی رائے: ____  نام و پتا: ____  رابطہ نمبر و ای میل: ____',
        'عمومي نظر: ____  نوم او پته: ____  د اړیکې شمېره او برېښنالیک: ____')
    BOOK.save(230, [('BM', rec(b, 'BM', 230, 230, first=True))], issues=[{'id': 'mq12-pdf230', 'unit': 'BM', 'printedPage': None,
               'description': 'Unnumbered back-matter page: KPTBB textbook feedback form (English in the original). The blank form rows are kept as empty table rows. Board logo not reproduced.'}])


def p231():
    b = Builder()
    b.h('National Anthem', 'قومی ترانہ', 'ملي ترانه')
    b.p('The inside back cover prints the National Anthem of Pakistan (written by Hafeez Jalandhari). Summary: it blesses the sacred land of Pakistan as the symbol of a high resolve and the centre of faith; it prays that the order of the land, built on the strength of the brotherhood of the people, keep the nation, country and state forever flourishing; and it describes the crescent-and-star flag as the guide to progress and perfection, the interpreter of the past and the glory of the present, under the shade of God the Majestic.',
        'اندرونی پچھلے سرورق پر پاکستان کا قومی ترانہ (حفیظ جالندھری) درج ہے۔ خلاصہ: اس میں پاک سرزمین کو عزمِ عالی شان کا نشان اور یقین کا مرکز کہہ کر دعا دی گئی ہے؛ یہ دعا کی گئی ہے کہ عوام کی اخوت کی قوت پر قائم اس سرزمین کا نظام قوم، ملک اور سلطنت کو ہمیشہ شاد و آباد رکھے؛ اور ہلالی پرچم کو ترقی و کمال کا رہبر، ماضی کا ترجمان اور حال کی شان، خدائے ذوالجلال کے سائے میں قرار دیا گیا ہے۔',
        'د شا پښتي په دننه مخ د پاکستان ملي ترانه (حفیظ جالندهري) چاپ شوې. لنډیز: په هغه کې پاکې خاورې ته د لوړ عزم د نښې او د باور د مرکز په توګه دعا شوې؛ دعا شوې چې د خلکو د ورورولۍ پر ځواک ولاړ د دې خاورې نظام قوم، هېواد او دولت تل ودان وساتي؛ او د سپوږمۍ او ستوري بیرغ د پرمختګ او کمال لارښود، د تېر ژباړونکی او د اوسني وخت ویاړ، د ذوالجلال خدای تر سیوري لاندې بلل شوی.')
    b.p('Devloped by: The ILM Foundation (TIF), 245-1/I, Block 6, PECHS, Karachi-75400, Pakistan. (92-21) 3430 4450-51, 3430 2220 21; 0335-3399929; www.tif.edu.pk; info@tif.edu.pk; QuranProgramForStudents.',
        'تیار کردہ: دی علم فاؤنڈیشن (TIF)، 245-1/I، بلاک 6، پی ای سی ایچ ایس، کراچی-75400 پاکستان۔ (92-21) 3430 4450-51، 3430 2220 21؛ 0335-3399929؛ www.tif.edu.pk؛ info@tif.edu.pk؛ QuranProgramForStudents۔',
        'چمتو کوونکی: د علم بنسټ (TIF)، 245-1/I، بلاک 6، PECHS، کراچۍ-75400، پاکستان. (92-21) 3430 4450-51، 3430 2220 21؛ 0335-3399929؛ www.tif.edu.pk؛ info@tif.edu.pk؛ QuranProgramForStudents.')
    b.table('mq12-bm-print', ['Code number', 'Quantity', 'Printer'], [['PSP/WPP-19-77-2627(O)', '72,974', 'Watermark Printing and Packages, Peshawar']],
            ['کوڈ نمبر', 'تعداد', 'مطبع'], ['کوډ شمېره', 'شمېر', 'چاپخونه'],
            [['PSP/WPP-19-77-2627(O)', '72,974', 'واٹر مارک پرنٹنگ اینڈ پیکجز پشاور']], [['PSP/WPP-19-77-2627(O)', '72,974', 'واټر مارک پرنټنګ او پکېجز، پېښور']])
    BOOK.save(231, [('BM', rec(b, 'BM', 231, 231))], issues=[{'id': 'mq12-pdf231', 'unit': 'BM', 'printedPage': None,
               'description': 'Inside back cover. The National Anthem (Hafeez Jalandhari, d. 1982) is summarised rather than reproduced (copyright rule). The printed English typo "Devloped by:" is kept as printed. Decorative border and TIF logo not reproduced.'}])


if __name__ == '__main__':
    {'230': p230, '231': p231}.get(sys.argv[1] if len(sys.argv) > 1 else '230', p230)()
