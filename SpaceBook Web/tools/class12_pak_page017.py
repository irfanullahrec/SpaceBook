"""Pak Studies XII PDF17 (spread): printed pp.25–26 — Ch.1 مشق Q1–Q5."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
e = Builder()
L = lambda rows: e.group('lines', rows)
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Fill in the blanks with suitable words.', '1۔ خالی جگہوں کو مناسب الفاظ سے پُر کریں۔', '۱. تش ځایونه په مناسبو کلمو ډک کړئ.')
L([('i. British historians gave the War of Independence the name ________ .', 'i۔ جنگِ آزادی کو انگریز مؤرخین نے ________ کا نام دیا۔', 'i. انګرېز تاریخپوهانو د خپلواکۍ جګړې ته ________ نوم ورکړ.'),
   ('ii. The proposal for the establishment of the Muslim League was presented by ________ .', 'ii۔ مسلم لیگ کے قیام کی تجویز ________ نے پیش کی تھی۔', 'ii. د مسلم لیګ د جوړېدو وړاندیز ________ وړاندې کړی و.'),
   ('iii. The government whose foundation Qutbuddin Aibak laid is called ________ .', 'iii۔ قطب الدین ایبک نے جس حکومت کی بنیاد رکھی اُسے ________ کہا جاتا ہے۔', 'iii. قطب‌الدین ایبک چې کوم حکومت بنسټ کېښود، هغې ته ________ ویل کېږي.'),
   ('iv. In 1906 the Simla Deputation met Viceroy ________ .', 'iv۔ شملہ وفد نے 1906ء میں وائسرائے ________ سے ملاقات کی۔', 'iv. د شملې پلاوي په ۱۹۰۶ز کې له وایسرای ________ سره ولیدل.'),
   ('v. The Muslims celebrated 22 December 1939 as ________ .', 'v۔ مسلمانوں نے 22 دسمبر 1939ء کا دن ________ کے طور پر منایا۔', 'v. مسلمانانو د ۱۹۳۹ز د ډسمبر ۲۲مه د ________ په توګه ولمانځله.'),
   ('vi. The Cabinet Mission consisted of ________ members of the British Parliament.', 'vi۔ کابینہ مشن برطانوی پارلیمنٹ کے ________ اراکین پر مشتمل تھا۔', 'vi. د کابینې ماموریت د برتانوي پارلمان له ________ غړو جوړ و.')])
e.p('2. Choose the correct word from the words given in brackets.', '2۔ بریکٹ میں دیے گئے الفاظ میں سے درست لفظ کا انتخاب کریں۔', '۲. په قوسونو کې له ورکړل شویو کلمو سمه کلمه وټاکئ.')
L([('i. In which year did Sir Syed Ahmad Khan visit England? (1863, 1869, 1875, 1886)', 'i۔ سرسید احمد خان نے انگلستان کا دورہ کس سال میں کیا؟ (1863ء، 1869ء، 1875ء، 1886ء)', 'i. سرسید احمد خان په کوم کال انګلستان ته سفر وکړ؟ (۱۸۶۳، ۱۸۶۹، ۱۸۷۵، ۱۸۸۶)'),
   ('ii. In which year did the Muslim League amend its aims? (1906, 1911, 1913, 1916)', 'ii۔ مسلم لیگ نے اپنے مقاصد میں کس سال ترمیم کی؟ (1906ء، 1911ء، 1913ء، 1916ء)', 'ii. مسلم لیګ په کوم کال خپلې موخې تعدیل کړې؟ (۱۹۰۶، ۱۹۱۱، ۱۹۱۳، ۱۹۱۶)'),
   ('iii. In which year did a delegation of Muslims meet the Viceroy of India Lord Minto? (1905, 1906, 1911, 1916)', 'iii۔ مسلمانوں کے ایک وفد نے کس سال میں وائسرائے ہند لارڈ منٹو سے ملاقات کی؟ (1905ء، 1906ء، 1911ء، 1916ء)', 'iii. د مسلمانانو یوه پلاوي په کوم کال د هند له وایسرای لارډ منټو سره ولیدل؟ (۱۹۰۵، ۱۹۰۶، ۱۹۱۱، ۱۹۱۶)'),
   ('iv. Which important event took place in 1911? (Lucknow Pact, Partition of Bengal, establishment of the Muslim League, annulment of the Partition of Bengal)', 'iv۔ 1911ء میں کون سا اہم واقعہ پیش آیا؟ (میثاقِ لکھنؤ، تقسیمِ بنگال، مسلم لیگ کا قیام، تنسیخِ تقسیمِ بنگال)', 'iv. په ۱۹۱۱ز کې کومه مهمه پېښه وشوه؟ (د لکهنؤ تړون، د بنګال وېش، د مسلم لیګ جوړېدل، د بنګال د وېش لغوه کېدل)'),
   ('v. Who announced the plan for the partition of India on 3 June 1947? (Lord Minto, Mountbatten, the Quaid-e-Azam, Nehru)', 'v۔ 3 جون 1947ء کو تقسیمِ ہند کے منصوبے کا اعلان کیا؟ (لارڈ منٹو نے، ماؤنٹ بیٹن نے، قائدِاعظم نے، نہرو نے)', 'v. د ۱۹۴۷ز د جون په ۳مه د هند د وېش د پلان اعلان چا وکړ؟ (لارډ منټو، ماونټبېټن، قائد اعظم، نهرو)'),
   ('vi. Who was the founder of the Indian National Congress? (Gandhi, Nehru, Dadabhai Naoroji, A. O. Hume)', 'vi۔ انڈین نیشنل کانگریس کا بانی کون تھا؟ (گاندھی، نہرو، دادا بھائی نوروجی، اے او ہیوم)', 'vi. د انډین نېشنل کانګرس بنسټګر څوک و؟ (ګاندي، نهرو، دادا بهايي نوروجي، اې. او. هیوم)')])
e.p('3. Identify the correct and incorrect among the following.', '3۔ مندرجہ ذیل میں صحیح اور غلط کی نشاندہی کریں۔', '۳. په لاندې کې سمې او ناسمې په نښه کړئ.')
L([('i. Education in Diniyat (Islamic sciences) at Aligarh College was compulsory for all.', 'i۔ علی گڑھ کالج میں دینیات (علومِ اسلامیہ) کی تعلیم سب کے لیے لازمی تھی۔', 'i. په علیګړ کالج کې د دینیاتو (اسلامي علومو) زده‌کړه د ټولو لپاره لازمي وه.'),
   ('ii. The founder of the Muhammadan Educational Conference was Maulana Muhammad Ali Jauhar.', 'ii۔ محمڈن ایجوکیشنل کانفرنس کے بانی مولانا محمد علی جوہر تھے۔', 'ii. د محمډن ایجوکیشنل کانفرنس بنسټګر مولانا محمد علي جوهر و.'),
   ('iii. The first president of the Muslim League was the Quaid-e-Azam Muhammad Ali Jinnah.', 'iii۔ مسلم لیگ کے پہلے صدر قائدِاعظم محمد علی جناح تھے۔', 'iii. د مسلم لیګ لومړی رئیس قائد اعظم محمد علي جناح و.'),
   ('iv. Turkey did not take part in the First World War.', 'iv۔ پہلی جنگِ عظیم میں ترکی نے حصہ نہیں لیا۔', 'iv. ترکیې په لومړۍ نړیواله جګړه کې ګډون ونه کړ.'),
   ('v. The word “Pakistan” was not used in the text of the Pakistan Resolution.', 'v۔ قراردادِ پاکستان کے متن میں لفظ ’’پاکستان‘‘ کا استعمال نہیں ہوا۔', 'v. د پاکستان پرېکړه‌لیک په متن کې د "پاکستان" کلمه نه ده کارول شوې.'),
   ('vi. The plan for the partition of India was presented on 3 June 1947.', 'vi۔ تقسیمِ ہند کا منصوبہ 3 جون 1947ء کو پیش کیا گیا۔', 'vi. د هند د وېش پلان د ۱۹۴۷ز د جون په ۳مه وړاندې شو.')])
e.p('4. Write short answers to the following questions.', '4۔ مندرجہ ذیل سوالات کے مختصر جوابات تحریر کریں۔', '۴. لاندې پوښتنو ته لنډ ځوابونه ولیکئ.')
L([('i. When and by whom was the foundation of Muslim government laid in northern India?', 'i۔ شمالی ہندوستان میں مسلمان حکومت کی بنیاد کب اور کس نے رکھی؟', 'i. په شمالي هندوستان کې د مسلمان حکومت بنسټ کله او چا کېښود؟'),
   ('ii. In Sir Syed Ahmad Khan’s view, what was the solution to all the difficulties of the Muslims?', 'ii۔ سرسید احمد خان کی نظر میں مسلمانوں کی تمام مشکلات کا حل کیا تھا؟', 'ii. د سرسید احمد خان په نظر د مسلمانانو د ټولو ستونزو حل څه و؟'),
   ('iii. Why was Western-style democracy not workable in united India?', 'iii۔ مغربی طرزِ جمہوریت متحدہ ہندوستان میں قابلِ عمل کیوں نہیں تھی؟', 'iii. لوېدیځ ډوله ډیموکراسي په متحده هندوستان کې ولې د عملي کېدو وړ نه وه؟'),
   ('iv. Write the three basic demands of the Simla Deputation (1906).', 'iv۔ شملہ وفد (1906ء) کے تین بنیادی مطالبات تحریر کریں۔', 'iv. د شملې پلاوي (۱۹۰۶ز) درې بنسټیزې غوښتنې ولیکئ.'),
   ('v. Why did the Congress and the Muslim League reject the proposals of the Cripps Mission?', 'v۔ کانگریس اور مسلم لیگ نے کرپس مشن کی تجاویز کو کیوں مسترد کیا تھا؟', 'v. کانګرس او مسلم لیګ د کرپس د ماموریت وړاندیزونه ولې رد کړل؟')])
e.p('5. Out of the dates given in column “A”, write the correct date for the events given in column “B” in column “C”.', '5۔ کالم ’’الف‘‘ میں دی گئی تاریخوں میں سے صحیح تاریخ کالم ’’ب‘‘ میں دیے گئے واقعات کے آگے کالم ’’ج‘‘ میں لکھیں۔', '۵. د "الف" ستون له ورکړل شویو نېټو څخه د "ب" ستون د پېښو مخې ته سمه نېټه په "ج" ستون کې ولیکئ.')
e.table('pak12-ch1-match', ['A', 'B', 'C'], [['1877', 'Cabinet Mission', ''], ['1905', 'Cripps Mission', ''], ['1916', 'Partition of Bengal', ''], ['1946', 'Lucknow Pact', ''], ['1942', 'Establishment of Aligarh College', '']],
        ['الف', 'ب', 'ج'], ['الف', 'ب', 'ج'],
        [['1877ء', 'کابینہ مشن', ''], ['1905ء', 'کرپس مشن', ''], ['1916ء', 'تقسیمِ بنگال', ''], ['1946ء', 'میثاقِ لکھنؤ', ''], ['1942ء', 'علی گڑھ کالج کا قیام', '']],
        [['۱۸۷۷ز', 'د کابینې ماموریت', ''], ['۱۹۰۵ز', 'د کرپس ماموریت', ''], ['۱۹۱۶ز', 'د بنګال وېش', ''], ['۱۹۴۶ز', 'د لکهنؤ تړون', ''], ['۱۹۴۲ز', 'د علیګړ کالج جوړېدل', '']])
ex = BOOK.record(e, 'pak12-ch1-exercise-1', 'Exercise (1)', 'مشق (۱)', 'تمرین (۱)', 17, [25, 26, 27])
issues = [{'id': 'pak12-pdf017', 'unit': 1, 'printedPage': 26, 'description': 'Q5 matching table continues on p.27 (rows 1946/Lucknow Pact and 1942/Aligarh College) and is recorded whole here; dates are deliberately jumbled for matching. Q2(v) omits “کس نے” in the question (as printed). Q3(ii) is a false statement by design (founder was Sir Syed).'}]

if __name__ == '__main__':
    BOOK.save(17, [(1, ex)], issues=issues)
