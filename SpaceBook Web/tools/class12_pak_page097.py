"""Pak Studies XII PDF97 (spread): printed pp.183–184 — Ch.9 مشق Q1–Q10 (chapter 9 complete)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
e = Builder()
L = lambda rows: e.group('lines', rows)
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Four alternative answers are given for each question below. Mark the correct answer.', '1۔ ذیل میں ہر سوال کے چار متبادل جواب درج ہیں۔ درست جواب کی نشان دہی کیجیے:۔', '۱. لاندې د هرې پوښتنې څلور بدیل ځوابونه ورکړل شوي. سم ځواب په نښه کړئ.')
L([('i. In 2003–2004 what percentage of GDP was obtained from agriculture? (15 per cent, 20 per cent, 24 per cent, 30 per cent)', 'i۔ 2003ء-2004ء میں جی ڈی پی کا کتنا فی صد زراعت سے حاصل ہوا۔ (15 فی صد، 20 فی صد، 24 فی صد، 30 فی صد)', 'i. په ۲۰۰۳-۲۰۰۴ز کې د ناخالص کورني تولید څو سلنه له کرنې ترلاسه شوه؟ (۱۵ سلنه، ۲۰ سلنه، ۲۴ سلنه، ۳۰ سلنه)'),
   ('ii. At present how much of the production of industries consists of agriculture? (40 per cent, 50 per cent, 60 per cent, 65 per cent)', 'ii۔ اس وقت صنعتوں کی پیداوار کا کتنا حصہ زراعت پر مشتمل ہے۔ (40 فی صد، 50 فی صد، 60 فی صد، 65 فی صد)', 'ii. اوس مهال د صنعتونو د تولید څومره برخه په کرنه ولاړه ده؟ (۴۰ سلنه، ۵۰ سلنه، ۶۰ سلنه، ۶۵ سلنه)'),
   ('iii. Among us what percentage of agricultural crops is wasted because of plant diseases? (10 per cent, 15 per cent, 20 per cent, 25 per cent)', 'iii۔ ہمارے ہاں زرعی فصلوں کا کتنے فی صد حصہ نباتاتی بیماریوں کے باعث ضائع ہو جاتا ہے۔ (10 فی صد، 15 فی صد، 20 فی صد، 25 فی صد)', 'iii. زموږ د کرنیزو فصلونو څو سلنه برخه د نباتي ناروغیو له امله ضایع کېږي؟ (۱۰ سلنه، ۱۵ سلنه، ۲۰ سلنه، ۲۵ سلنه)'),
   ('iv. In which year did the government take many industries into national ownership? (in 1970, in 1971, in 1972, in 1974)', 'iv۔ حکومت نے کس سن میں بہت سی صنعتوں کو قومی تحویل میں لیا تھا۔ (1970ء میں، 1971ء میں، 1972ء میں، 1974ء میں)', 'iv. حکومت په کوم کال ډېر صنعتونه ملي ولکې ته واخیستل؟ (په ۱۹۷۰ز، په ۱۹۷۱ز، په ۱۹۷۲ز، په ۱۹۷۴ز)'),
   ('v. According to the opinion of economists, on how much of the area of a country should there be forests? (25 per cent, 40 per cent, 60 per cent, 80 per cent)', 'v۔ ماہرینِ اقتصادیات کی رائے کے مطابق کسی ملک کے کتنے رقبے پر جنگلات ہوں۔ (25 فی صد، 40 فی صد، 60 فی صد، 80 فی صد)', 'v. د اقتصادپوهانو د نظر له مخې د یوه هېواد پر څومره ساحه باید ځنګلونه وي؟ (۲۵ سلنه، ۴۰ سلنه، ۶۰ سلنه، ۸۰ سلنه)'),
   ('vi. Economic planning in Pakistan began — (in 1950, in 1955, in 1960, in 1965)', 'vi۔ پاکستان میں معاشی منصوبہ بندی کا آغاز ہوا۔ (1950ء میں، 1955ء میں، 1960ء میں، 1965ء میں)', 'vi. په پاکستان کې اقتصادي پلان جوړونه پیل شوه — (په ۱۹۵۰ز، په ۱۹۵۵ز، په ۱۹۶۰ز، په ۱۹۶۵ز)')])
e.p('2. Fill in the blanks.', '2۔ خالی جگہوں کو پُر کریں۔', '۲. تش ځایونه ډک کړئ.')
L([('i. Pakistan is a developing ________ country.', 'i۔ پاکستان ایک ترقی ________ ملک ہے۔', 'i. پاکستان یو پرمختیايي ________ هېواد دی.'),
   ('ii. In Pakistan ________ per cent of cultivation is irrigated by artificial irrigation.', 'ii۔ پاکستان میں کاشت کا ________ فی صد حصہ مصنوعی آب پاشی سے سیراب ہوتا ہے۔', 'ii. په پاکستان کې د کرنې ________ سلنه برخه په مصنوعي اوبه لګونه خړوبېږي.'),
   ('iii. In Pakistan comprehensive economic planning began for the first time in ________ .', 'iii۔ پاکستان میں پہلی مرتبہ ________ میں جامع معاشی منصوبہ بندی کا آغاز ہوا۔', 'iii. په پاکستان کې د لومړي ځل لپاره په ________ کې جامع اقتصادي پلان جوړونه پیل شوه.'),
   ('iv. At the time of the establishment of Pakistan there were only ________ medical colleges in the country.', 'iv۔ قیامِ پاکستان کے وقت ملک میں صرف ________ میڈیکل کالج تھے۔', 'iv. د پاکستان د جوړېدو پر وخت په هېواد کې یوازې ________ طبي کالجونه وو.')])
e.p('3. Write short answers.', '3۔ مختصر جواب لکھیں', '۳. لنډ ځوابونه ولیکئ.')
L([('i. Why is economic planning done?', 'i۔ معاشی منصوبہ بندی کیوں کی جاتی ہے؟', 'i. اقتصادي پلان جوړونه ولې کېږي؟'),
   ('ii. What are the five important basic objectives of the new National Education Policy (1998–2010)?', 'ii۔ نئی قومی تعلیمی پالیسی (2010ء-1998ء) کے پانچ اہم بنیادی مقاصد کیا ہیں؟', 'ii. د نوې ملي زده‌کړیزې پالیسۍ (۱۹۹۸–۲۰۱۰ز) پنځه مهمې بنسټیزې موخې کومې دي؟'),
   ('iii. Write a few benefits of forests.', 'iii۔ جنگلات کے چند فوائد تحریر کریں۔', 'iii. د ځنګلونو ځینې ګټې ولیکئ.'),
   ('iv. State the important exports of Pakistan.', 'iv۔ پاکستان کی اہم برآمدات بیان کریں۔', 'iv. د پاکستان مهم صادرات بیان کړئ.')])
L([('4. Review the state of economic planning in Pakistan.', '4۔ پاکستان میں معاشی منصوبہ بندی کی صورتِ حال کا جائزہ لیں۔', '۴. په پاکستان کې د اقتصادي پلان جوړونې حالت وڅېړئ.'),
   ('5. What measures is the government taking to solve the agricultural problems of Pakistan?', '5۔ پاکستان کے زرعی مسائل کو حل کرنے کے لیے حکومت کیا اقدامات کر رہی ہے؟', '۵. حکومت د پاکستان د کرنیزو ستونزو د حل لپاره کوم ګامونه پورته کوي؟'),
   ('6. State the reasons for Pakistan’s industrial backwardness and propose measures to increase industrial production.', '6۔ پاکستان کی صنعتی پسماندگی کی وجوہات بیان کریں اور صنعتی پیداوار بڑھانے کے لیے اقدامات تجویز کریں۔', '۶. د پاکستان د صنعتي وروسته پاتې‌والي لاملونه بیان کړئ او د صنعتي تولید د زیاتولو لپاره ګامونه وړاندیز کړئ.'),
   ('7. Write a detailed note on the important exports and imports of Pakistan.', '7۔ پاکستان کی اہم برآمدات اور درآمدات پر تفصیلی نوٹ لکھیں۔', '۷. د پاکستان د مهمو صادراتو او وارداتو په اړه مفصل یادښت ولیکئ.'),
   ('8. Throw light on the importance of natural resources in the economic development of Pakistan.', '8۔ پاکستان کی اقتصادی ترقی میں قدرتی وسائل کی اہمیت پر روشنی ڈالیں۔', '۸. د پاکستان په اقتصادي پرمختګ کې د طبیعي سرچینو پر اهمیت رڼا واچوئ.'),
   ('9. State the important points of Pakistan’s National Education Policy (1998–2010).', '9۔ پاکستان کی قومی تعلیمی پالیسی (2010ء-1998ء) کے اہم نکات بیان کریں۔', '۹. د پاکستان د ملي زده‌کړیزې پالیسۍ (۱۹۹۸–۲۰۱۰ز) مهم ټکي بیان کړئ.'),
   ('10. What is meant by IT? What efforts are being made in Pakistan for its promotion?', '10۔ آئی ٹی (IT) سے کیا مراد ہے؟ پاکستان میں اس کے فروغ کے لیے کیا کوششیں کی جا رہی ہیں؟', '۱۰. له آی ټي (IT) څخه څه مراد دی؟ په پاکستان کې د هغې د ودې لپاره کومې هڅې کېږي؟')])
ex = BOOK.record(e, 'pak12-ch9-exercise', 'Exercise', 'مشق', 'تمرین', 97, [183, 184])
issues = [{'id': 'pak12-pdf097', 'unit': 9, 'printedPage': 183, 'description': 'Q2(i) prints the blank inside “ترقی ________ ملک” (for “ترقی پذیر”); retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(97, [(9, ex)], issues=issues, complete_units=[9])
