"""Pak Studies XII PDF105 (spread): pp.199–200 — Ch.10 مشق Q3(2)–Q10 (chapter 10 complete)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
e = Builder()
L = lambda rows: e.group('lines', rows)
L([('2. Iran is the only country which opposed Pakistan’s membership in the United Nations.', '2۔ ایران واحد ملک ہے جس نے اقوامِ متحدہ میں پاکستان کی رُکنیت کی مخالفت کی۔', '۲. ایران یوازینی هېواد دی چې په ملګرو ملتونو کې یې د پاکستان د غړیتوب مخالفت وکړ.'),
   ('3. Pakistan has always raised its voice against racial discrimination.', '3۔ پاکستان نے ہمیشہ نسلی امتیاز کے خلاف آواز اٹھائی۔', '۳. پاکستان تل د نژادي توپیر پر ضد غږ پورته کړی.'),
   ('4. Pakistan carried out atomic explosions in 1998.', '4۔ پاکستان نے 1998ء میں ایٹمی دھماکے کیے۔', '۴. پاکستان په ۱۹۹۸ز کې اټومي چاودنې وکړې.'),
   ('5. Pakistan had not recognised the Taliban government.', '5۔ پاکستان نے طالبان حکومت کو تسلیم نہیں کیا تھا۔', '۵. پاکستان د طالبانو حکومت په رسمیت نه و پېژندلی.')])
e.p('4. Match the events given in column “A” with the years given in column “B”.', '4۔ کالم ’’الف‘‘ میں دیے گئے واقعات کا تعلق کالم ’’ب‘‘ میں دیے گئے سالوں سے جوڑیں۔', '۴. د "الف" ستون پېښې د "ب" ستون له کلونو سره وښلوئ.')
A = [('Establishment of Pakistan', 'قیامِ پاکستان', 'د پاکستان جوړېدل', '1964'), ('Pakistan–China border dispute', 'پاک چین سرحدی تنازعہ', 'د پاک-چین سرحدي شخړه', '1960'),
     ('Indus Waters Treaty', 'سندھ طاس معاہدہ', 'د سند د حوزې تړون', '1950'), ('Organisation of Regional Cooperation for Development', 'علاقائی تعاون برائے ترقی کی تنظیم', 'د پراختیا لپاره د سیمه‌ییزې همکارۍ سازمان', '1947'),
     ('Pakistan’s atomic explosions', 'پاکستان کے ایٹمی دھماکے', 'د پاکستان اټومي چاودنې', '1979'), ('Establishment of the D-8 organisation', 'ڈی-ایٹ تنظیم کا قیام', 'د ډي-اېټ سازمان جوړېدل', '1998'),
     ('Islamic revolution in Iran', 'ایران میں اسلامی انقلاب', 'په ایران کې اسلامي انقلاب', '1997')]
e.table('pak12-ch10-match', ['Column “A”', 'Column “B”'], [[a[0], a[3]] for a in A], ['کالم ’’الف‘‘', 'کالم ’’ب‘‘'], ['ستون "الف"', 'ستون "ب"'],
        [[a[1], a[3] + 'ء'] for a in A], [[a[2], a[3] + 'ز'] for a in A])
e.p('5. Give short answers.', '5۔ مختصر جواب دیجیے۔', '۵. لنډ ځوابونه ورکړئ.')
L([('1. What is meant by foreign policy?', '1۔ خارجہ پالیسی سے کیا مراد ہے؟', '۱. له بهرنۍ پالیسۍ څه مراد دی؟'),
   ('2. Write five basic principles of foreign policy.', '2۔ خارجہ پالیسی کے پانچ بنیادی اصول لکھیے۔', '۲. د بهرنۍ پالیسۍ پنځه بنسټیز اصول ولیکئ.'),
   ('3. What is meant by the administrative troika?', '3۔ انتظامی تکون سے کیا مُراد ہے؟', '۳. له اداري درېیزې څه مراد دی؟'),
   ('4. Regional Cooperation for Development', '4۔ علاقائی تعاون برائے ترقی', '۴. د پراختیا لپاره سیمه‌ییزه همکاري'),
   ('5. Duties of the Ministry of Foreign Affairs', '5۔ وزارتِ خارجہ کے فرائض', '۵. د بهرنیو چارو وزارت دندې'),
   ('6. The role of political parties and pressure groups in foreign policy', '6۔ خارجہ پالیسی میں سیاسی جماعتوں و پریشر گروپ کا کردار', '۶. په بهرنۍ پالیسۍ کې د سیاسي ګوندونو او فشار ډلو رول'),
   ('7. Write a short note on Pakistan’s atomic explosions.', '7۔ پاکستان کے ایٹمی دھماکوں پر مختصر نوٹ لکھیں۔', '۷. د پاکستان پر اټومي چاودنو لنډ یادښت ولیکئ.'),
   ('8. What is meant by national security?', '8۔ قومی سلامتی سے کیا مُراد ہے؟', '۸. له ملي امنیت څه مراد دی؟')])
L([('6. What is meant by foreign policy? Write a note on the sources of the formation of Pakistan’s foreign policy.', '6۔ خارجہ پالیسی سے کیا مُراد ہے؟ پاکستان کی خارجہ پالیسی کی تشکیل کے ذرائع پر نوٹ لکھیں۔', '۶. له بهرنۍ پالیسۍ څه مراد دی؟ د پاکستان د بهرنۍ پالیسۍ د جوړېدو د سرچینو په اړه یادښت ولیکئ.'),
   ('7. Write a comprehensive note on the objectives of Pakistan’s foreign policy.', '7۔ پاکستان کی خارجہ پالیسی کے مقاصد پر جامع نوٹ لکھیں۔', '۷. د پاکستان د بهرنۍ پالیسۍ د موخو په اړه جامع یادښت ولیکئ.'),
   ('8. Describe the evolution of the relations of Pakistan and America.', '8۔ پاکستان اور امریکہ کے تعلقات کا ارتقا بیان کیجیے۔', '۸. د پاکستان او امریکا د اړیکو وده بیان کړئ.'),
   ('9. Explain the relations of Pakistan with the following countries: (a) Afghanistan (b) Iran (c) Saudi Arabia', '9۔ درج ذیل ممالک کے ساتھ پاکستان کے تعلقات کو واضح کیجیے۔ (ا) افغانستان (ب) ایران (ج) سعودی عرب', '۹. له لاندې هېوادونو سره د پاکستان اړیکې روښانه کړئ: (ا) افغانستان (ب) ایران (ج) سعودي عربستان'),
   ('10. Why has Pakistan’s foreign policy been under pressure on the Kashmir issue?', '10۔ کشمیر کے مسئلے پر پاکستان کی خارجہ پالیسی کیوں دباؤ کا شکار رہی؟', '۱۰. د کشمیر پر مسئله د پاکستان بهرنۍ پالیسي ولې د فشار ښکار وه؟')])
ex = BOOK.record(e, 'pak12-ch10-exercise-2', 'Exercise (2)', 'مشق (۲)', 'تمرین (۲)', 105, [199, 200])
ex['sourceNote'] = 'Q3 items 2–5 continue from p.198. The match table prints the years in shuffled order (as intended for matching); calendar suffixes are added per language.'
issues = [{'id': 'pak12-pdf105', 'unit': 10, 'printedPage': 199,
           'description': 'In Q4 the year list (1964, 1960, 1950, 1947, 1979, 1998, 1997) contains 1950 for the Pak–China border dispute (text says “decade of 1950”); Q5 items 4–6 are topics rather than questions. Retained as printed. Most of p.200 below Q10 is blank.'}]

if __name__ == '__main__':
    BOOK.save(105, [(10, ex)], issues=issues, complete_units=[10])
