"""Pak Studies XII PDF47 (spread): printed pp.83–84 — Ch.4 مشق Q1–Q8 (chapter 4 complete)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
e = Builder()
L = lambda rows: e.group('lines', rows)
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Fill in the blanks with suitable words.', '1۔ خالی جگہوں کو مناسب الفاظ سے پُر کریں:-', '۱. تش ځایونه په مناسبو کلمو ډک کړئ.')
L([('i. The General Assembly of the United Nations approved the Universal Declaration of Human Rights on 10 December ________ .', 'i۔ اقوامِ متحدہ کی جنرل اسمبلی نے عالمی انسانی حقوق کا اعلامیہ 10 دسمبر ________ کو منظور کیا۔', 'i. د ملګرو ملتونو عمومي اسمبلۍ د بشري حقونو نړیواله اعلامیه د ډسمبر په ۱۰مه ________ تصویب کړه.'),
   ('ii. ________ presented the Objectives Resolution in the Constituent Assembly.', 'ii۔ قراردادِ مقاصد ________ نے دستور ساز اسمبلی میں پیش کی تھی۔', 'ii. د موخو پرېکړه‌لیک ________ په اساسي قانون جوړوونکې اسمبلۍ کې وړاندې کړی و.'),
   ('iii. The first constitution of Pakistan was enforced in ________ .', 'iii۔ پاکستان کا پہلا آئین ________ میں نافذ کیا گیا۔', 'iii. د پاکستان لومړی اساسي قانون په ________ کې پلی شو.'),
   ('iv. In the 1973 constitution ________ was defined for the first time.', 'iv۔ 1973ء کے آئین میں پہلی مرتبہ ________ کی تعریف کی گئی۔', 'iv. د ۱۹۷۳ز په اساسي قانون کې د لومړي ځل لپاره د ________ تعریف وشو.'),
   ('v. The interest-free banking system was started in January ________ .', 'v۔ سود سے پاک بینکاری کا نظام جنوری ________ میں شروع کیا گیا۔', 'v. له سوده پاک بانکداري نظام د ________ په جنورۍ کې پیل شو.')])
e.p('2. Choose the correct word from the words given in brackets.', '2۔ بریکٹ میں دیے گئے الفاظ میں سے درست لفظ کا انتخاب کریں:-', '۲. په قوسونو کې له ورکړل شویو کلمو سمه کلمه وټاکئ.')
L([('i. Who played the most important role in the preparation of the Objectives Resolution? (Maulana Maududi, Maulana Ashraf Ali Thanvi, Syed Sulaiman Nadvi, Maulana Shabbir Ahmad Usmani)', 'i۔ قراردادِ مقاصد کی تیاری میں کس نے سب سے اہم کردار ادا کیا؟ (مولانا مودودی، مولانا اشرف علی تھانوی، سید سلیمان ندوی، مولانا شبیر احمد عثمانی)', 'i. د موخو پرېکړه‌لیک په چمتو کولو کې تر ټولو مهم رول چا ولوباوه؟ (مولانا مودودي، مولانا اشرف علي تهانوي، سید سلیمان ندوي، مولانا شبیر احمد عثماني)'),
   ('ii. When was the first constitution of Pakistan enforced? (1950, 1952, 1954, 1956)', 'ii۔ پاکستان کا پہلا آئین کب نافذ کیا گیا؟ (1950ء، 1952ء، 1954ء، 1956ء)', 'ii. د پاکستان لومړی اساسي قانون کله پلی شو؟ (۱۹۵۰، ۱۹۵۲، ۱۹۵۴، ۱۹۵۶)'),
   ('iii. In which constitution of Pakistan was there no office of Prime Minister? (1935, 1956, 1962, 1973)', 'iii۔ پاکستان کے کون سے آئین میں وزیرِاعظم کا عہدہ نہیں تھا؟ (1935ء، 1956ء، 1962ء، 1973ء)', 'iii. د پاکستان په کوم اساسي قانون کې د لومړي وزیر څوکۍ نه وه؟ (۱۹۳۵، ۱۹۵۶، ۱۹۶۲، ۱۹۷۳)'),
   ('iv. In which constitution of Pakistan was Islam declared the state religion? (1935, 1956, 1962, 1973)', 'iv۔ پاکستان کے کون سے آئین میں اسلام کو سرکاری مذہب قرار دیا گیا؟ (1935ء، 1956ء، 1962ء، 1973ء)', 'iv. د پاکستان په کوم اساسي قانون کې اسلام رسمي دین وګڼل شو؟ (۱۹۳۵، ۱۹۵۶، ۱۹۶۲، ۱۹۷۳)'),
   ('v. When was the Zakat Ordinance enforced? (20 June 1980, 23 March 1986, 23 March 1988, 11 August 1990)', 'v۔ زکوٰۃ آرڈیننس کا نفاذ کب ہوا؟ (20 جون 1980ء، 23 مارچ 1986ء، 23 مارچ 1988ء، 11 اگست 1990ء)', 'v. د زکات فرمان کله پلی شو؟ (۲۰ جون ۱۹۸۰، ۲۳ مارچ ۱۹۸۶، ۲۳ مارچ ۱۹۸۸، ۱۱ اګست ۱۹۹۰)')])
e.p('3. Identify the correct and incorrect among the following.', '3۔ مندرجہ ذیل میں سے صحیح اور غلط کی نشاندہی کریں:-', '۳. په لاندې کې سمې او ناسمې په نښه کړئ.')
L([('i. After the establishment of Pakistan the work of constitution-making remained in abeyance for many years.', 'i۔ قیامِ پاکستان کے بعد کئی سال تک آئین سازی کا کام التوا کا شکار رہا۔', 'i. د پاکستان له جوړېدو وروسته څو کاله د اساسي قانون جوړونې کار ځنډېدلی و.'),
   ('ii. Under the 1956 constitution there was no condition of being a Muslim for the Prime Minister of Pakistan.', 'ii۔ 1956ء کے آئین کے تحت پاکستان کے وزیرِاعظم کے لیے مسلمان ہونے کی شرط نہیں تھی۔', 'ii. د ۱۹۵۶ز د اساسي قانون له مخې د پاکستان د لومړي وزیر لپاره د مسلمان کېدو شرط نه و.'),
   ('iii. In the period of Zia-ul-Haq’s government, the teaching of Islamiat was made compulsory in schools for the first time.', 'iii۔ ضیاء الحق کے دورِ حکومت میں پہلی دفعہ سکولوں میں اسلامیات کی تعلیم کو لازمی قرار دیا گیا۔', 'iii. د ضیاءالحق د حکومت په دوره کې د لومړي ځل لپاره په ښوونځیو کې د اسلامیاتو زده‌کړه لازمي شوه.'),
   ('iv. Under the 1973 constitution government employees can take part in politics directly.', 'iv۔ 1973ء کے آئین کے تحت سرکاری ملازمین سیاست میں براہِ راست حصہ لے سکتے ہیں۔', 'iv. د ۱۹۷۳ز د اساسي قانون له مخې دولتي کارکوونکي په مستقیم ډول په سیاست کې ګډون کولی شي.'),
   ('v. Many things are common in the Universal Declaration of Human Rights and the Farewell Sermon.', 'v۔ عالمی انسانی حقوق کے اعلامیے اور خطبہ حجۃ الوداع میں بہت سی باتیں مشترک ہیں۔', 'v. د بشري حقونو په نړیواله اعلامیه او د حجة الوداع په خطبه کې ډېرې خبرې ګډې دي.')])
e.p('4. Write short answers to the following questions.', '4۔ مندرجہ ذیل سوالات کے مختصر جوابات تحریر کریں:-', '۴. لاندې پوښتنو ته لنډ ځوابونه ولیکئ.')
L([('i. What concept of sovereignty has been given in the Objectives Resolution?', 'i۔ قراردادِ مقاصد میں حاکمیتِ اعلیٰ کا کیا تصور دیا گیا ہے؟', 'i. د موخو په پرېکړه‌لیک کې د لوړ حاکمیت کوم تصور ورکړل شوی؟'),
   ('ii. What are the duties of the Council of Islamic Ideology?', 'ii۔ اسلامی نظریاتی کونسل کے کیا فرائض ہیں؟', 'ii. د اسلامي نظریاتي شورا دندې څه دي؟'),
   ('iii. How has the word “Muslim” been defined in the 1973 constitution?', 'iii۔ 1973ء کے آئین میں لفظ ’’مسلمان‘‘ کی تعریف کیسے کی گئی ہے؟', 'iii. د ۱۹۷۳ز په اساسي قانون کې د "مسلمان" کلمه څنګه تعریف شوې؟'),
   ('iv. In the Farewell Sermon, what did the Holy Prophet (peace and blessings of Allah be upon him, his family and companions) say about slaves?', 'iv۔ خطبہ حجۃ الوداع میں حضور صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم نے غلاموں کے بارے میں کیا ارشاد فرمایا؟', 'iv. د حجة الوداع په خطبه کې حضور صلی الله علیه وعلی آله واصحابه وسلم د غلامانو په اړه څه وفرمایل؟'),
   ('v. In the Farewell Sermon, what did the Holy Prophet (peace and blessings of Allah be upon him, his family and companions) emphasise about women?', 'v۔ خطبہ حجۃ الوداع میں حضور صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم نے عورتوں کے بارے میں کیا تاکید فرمائی؟', 'v. د حجة الوداع په خطبه کې حضور صلی الله علیه وعلی آله واصحابه وسلم د ښځو په اړه څه ټینګار وفرمایه؟')])
L([('5. Why was the Objectives Resolution made a part of the constitution? Make a detailed review.', '5۔ قراردادِ مقاصد کو آئین کا حصہ کیوں بنایا گیا؟ تفصیلی جائزہ لیں۔', '۵. د موخو پرېکړه‌لیک ولې د اساسي قانون برخه شو؟ مفصله کتنه وکړئ.'),
   ('6. Write the Islamic provisions included in the 1973 constitution.', '6۔ 1973ء کے آئین میں شامل اسلامی دفعات تحریر کریں۔', '۶. د ۱۹۷۳ز په اساسي قانون کې شاملې اسلامي مادې ولیکئ.'),
   ('7. What similarity is found between the United Nations Universal Declaration of Human Rights and the Farewell Sermon? Review.', '7۔ اقوامِ متحدہ کے عالمگیر انسانی حقوق کے اعلامیے اور خطبہ حجۃ الوداع میں کیا مماثلت پائی جاتی ہے؟ جائزہ لیں۔', '۷. د ملګرو ملتونو د بشري حقونو نړیوالې اعلامیې او د حجة الوداع خطبې ترمنځ څه ورته‌والی موندل کېږي؟ کتنه وکړئ.'),
   ('8. What progress has been made so far towards the enforcement of Islam in Pakistan?', '8۔ پاکستان میں نفاذِ اسلام کی طرف اب تک کیا پیش رفت ہوئی ہے؟', '۸. په پاکستان کې د اسلام د پلي کولو پر لور تر اوسه څه پرمختګ شوی؟')])
ex = BOOK.record(e, 'pak12-ch4-exercise', 'Exercise', 'مشق', 'تمرین', 47, [83, 84])
issues = [{'id': 'pak12-pdf047', 'unit': 4, 'printedPage': 84, 'description': 'Q2(iii) asks in which constitution there was no office of Prime Minister (1962, presidential) though the chapter text does not state this explicitly — retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(47, [(4, ex)], issues=issues, complete_units=[4])
