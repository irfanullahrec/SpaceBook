"""Pak Studies XII PDF78 (spread): printed pp.145–146 — Ch.7 مشق Q1–Q10 (chapter 7 complete)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
e = Builder()
L = lambda rows: e.group('lines', rows)
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Fill in the blanks.', '1۔ خالی جگہوں کو پُر کریں۔', '۱. تش ځایونه ډک کړئ.')
L([('i. In Pakistan, besides Urdu, nearly ________ languages are spoken.', 'i۔ پاکستان میں اُردو کے علاوہ تقریباً ________ کے قریب زبانیں بولی جاتی ہیں۔', 'i. په پاکستان کې له اردو پرته شاوخوا ________ ژبې ویل کېږي.'),
   ('ii. The original script of the Punjabi language is ________ .', 'ii۔ پنجابی زبان کا اصل رسم الخط ________ ہے۔', 'ii. د پنجابي ژبې اصلي لیکدود ________ دی.'),
   ('iii. With reference to the ghazal in Pashto poetry a great name is that of ________ .', 'iii۔ پشتو شاعری میں غزل کے حوالے سے ایک بڑا نام ________ کا ہے۔', 'iii. په پښتو شاعرۍ کې د غزل په برخه کې یو لوی نوم د ________ دی.'),
   ('iv. In the subcontinent of Pakistan and India the Holy Quran was first translated into the ________ language.', 'iv۔ برصغیر پاک و ہند میں قرآن پاک کا ترجمہ سب سے پہلے ________ زبان میں کیا گیا۔', 'iv. د پاک و هند په نیمه لویه وچه کې قرآن پاک تر ټولو لومړی په ________ ژبه وژباړل شو.')])
e.p('2. Choose the correct word from the words given in brackets.', '2۔ بریکٹ میں دیے گئے الفاظ میں سے درست لفظ کا انتخاب کریں۔', '۲. په قوسونو کې له ورکړل شویو کلمو سمه کلمه وټاکئ.')
L([('i. Urdu is a word of which language? (Hindi, Persian, Arabic, Turkish)', 'i۔ اُردو کس زبان کا لفظ ہے؟ (ہندی، فارسی، عربی، ترکی)', 'i. اردو د کومې ژبې کلمه ده؟ (هندي، فارسي، عربي، ترکي)'),
   ('ii. The first poet of Urdu was — (Wali Dakani, Quli Qutb Shah, Khwaja Masud Salman, Mirza Ghalib)', 'ii۔ اُردو کے پہلے شاعر تھے۔ (ولی دکنی، قلی قطب شاہ، خواجہ مسعود سلمان، مرزا غالب)', 'ii. د اردو لومړی شاعر و — (ولي دکني، قلي قطب شاه، خواجه مسعود سلمان، مرزا غالب)'),
   ('iii. In the period of the Mughals, words of which language entered the Sindhi language in abundance? (Turkish, English, Persian, Arabic)', 'iii۔ مغلوں کے دور میں سندھی زبان میں کون سی زبان کے الفاظ کثرت سے شامل ہوئے؟ (ترکی، انگریزی، فارسی، عربی)', 'iii. د مغلو په دوره کې په سندهي ژبه کې د کومې ژبې کلمې په ډېره اندازه شاملې شوې؟ (ترکي، انګرېزي، فارسي، عربي)'),
   ('iv. The name of the first book of the Pashto language is — (Khair-ul-Bayan, Pata Khazana, Baz Nama, Dastar Nama)', 'iv۔ پشتو زبان کی پہلی کتاب کا نام ہے۔ (خیر البیان، پٹہ خزانہ، باز نامہ، دستار نامہ)', 'iv. د پښتو ژبې د لومړي کتاب نوم دی — (خیر البیان، پټه خزانه، باز نامه، دستار نامه)'),
   ('v. Who arranged the alphabet of the Pashto language? (Rahman Baba, Dost Muhammad Kamil, Khushal Khan Khattak, Saifullah)', 'v۔ پشتو زبان کے حروفِ تہجی مرتب کیے۔ (رحمان بابا، دوست محمد کامل، خوشحال خان خٹک، سیف اللہ)', 'v. د پښتو ژبې توري چا ترتیب کړل؟ (رحمان بابا، دوست محمد کامل، خوشحال خان خټک، سیف الله)')])
e.p('3. Identify the correct and incorrect among the following.', '3۔ مندرجہ ذیل میں صحیح اور غلط کی نشاندہی کریں۔', '۳. په لاندې کې سمې او ناسمې په نښه کړئ.')
L([('i. Urdu-e-Mualla was the name of a bazaar of Delhi.', 'i۔ اُردوئے معلیٰ دہلی کے ایک بازار کا نام تھا۔', 'i. اردوی معلی د ډیلي د یوه بازار نوم و.'),
   ('ii. Urdu literature began with prose.', 'ii۔ اُردو ادب کا آغاز نثر سے ہوا تھا۔', 'ii. د اردو ادب پیل له نثر څخه شوی و.'),
   ('iii. Amir Hamza Khan Shinwari gave the ghazal the status of a regular genre in Pashto poetry.', 'iii۔ امیر حمزہ خان شنواری نے پشتو شاعری میں غزل کو باقاعدہ صنف کا درجہ دیا۔', 'iii. امیر حمزه خان شینواري په پښتو شاعرۍ کې غزل ته د منظم ژانر درجه ورکړه.'),
   ('iv. Punjabi itself is a word of the Persian language.', 'iv۔ پنجابی خود فارسی زبان کا لفظ ہے۔', 'iv. پنجابي پخپله د فارسي ژبې کلمه ده.'),
   ('v. Major Raverty (Major Raverty) had written a book in the Pashto language.', 'v۔ میجر راورٹی (Major Raverty) نے پشتو زبان میں کتاب لکھی تھی۔', 'v. مېجر راورټي (Major Raverty) په پښتو ژبه کتاب لیکلی و.'),
   ('vi. Speakers of the Balochi language also exist in Turkmenistan and Oman.', 'vi۔ بلوچی زبان بولنے والے ترکمانستان اور اومان میں بھی موجود ہیں۔', 'vi. د بلوڅي ژبې ویونکي په ترکمنستان او عمان کې هم شته.')])
e.p('4. Match the words given in column “A” with the appropriate words of column “B”.', '4۔ کالم ’’الف‘‘ میں دیے گئے لفظوں کا کالم ’’ب‘‘ کے مناسب لفظوں سے جوڑ ملائیں۔', '۴. د "الف" ستون کلمې د "ب" ستون له مناسبو کلمو سره وښلوئ.')
e.table('pak12-ch7-match', ['Column “A”', 'Column “B”'],
        [['Waris Shah', 'Sohni Mahiwal'], ['Hashim Shah', 'Heer Ranjha'], ['Fazal Shah', 'Fazl Nama'], ['Hafiz Barkhurdar', 'Sassi Punnun'], ['Khushal Khan Khattak', 'Mirza Sahiban']],
        ['کالم ’’الف‘‘', 'کالم ’’ب‘‘'], ['ستون "الف"', 'ستون "ب"'],
        [['وارث شاہ', 'سوہنی مہینوال'], ['ہاشم شاہ', 'ہیر رانجھا'], ['فضل شاہ', 'فضل نامہ'], ['حافظ برخوردار', 'سسی پنوں'], ['خوشحال خان خٹک', 'مرزا صاحباں']],
        [['وارث شاه', 'سوهني مهینوال'], ['هاشم شاه', 'هیر رانجها'], ['فضل شاه', 'فضل نامه'], ['حافظ برخوردار', 'سسي پنون'], ['خوشحال خان خټک', 'مرزا صاحبان']])
e.p('5. Give short answers to the following questions.', '5۔ مندرجہ ذیل سوالات کے مختصر جواب دیجیے:۔', '۵. لاندې پوښتنو ته لنډ ځوابونه ورکړئ.')
L([('i. In the region where Pakistan is situated, traces of which ancient civilisations have been found?', 'i۔ پاکستان جس خطے میں واقع ہے وہاں کن قدیم تہذیبوں کے آثار ملے ہیں؟', 'i. پاکستان په کومه سیمه کې پروت دی، هلته د کومو لرغونو تمدنونو نښې موندل شوې؟'),
   ('ii. Why is the Urdu language the most suitable as the national language of Pakistan?', 'ii۔ اُردو زبان پاکستان کی قومی زبان کے طور پر کیوں سب سے زیادہ موزوں ہے؟', 'ii. اردو ژبه د پاکستان د ملي ژبې په توګه ولې تر ټولو مناسبه ده؟'),
   ('iii. By which names was the Urdu language called in different periods?', 'iii۔ اُردو زبان کو مختلف ادوار میں کن کن ناموں سے پکارا گیا؟', 'iii. اردو ژبه په بېلابېلو دورو کې په کومو کومو نومونو یادېده؟'),
   ('iv. When and for what purpose was the Pashto Academy established?', 'iv۔ پشتو اکیڈمی کا قیام کب اور کس مقصد کے تحت عمل میں لایا گیا؟', 'iv. پښتو اکاډمي کله او د کومې موخې لپاره جوړه شوه؟')])
L([('6. Write a note on the Punjabi language and literature.', '6۔ پنجابی زبان اور ادب پر نوٹ لکھیں۔', '۶. د پنجابي ژبې او ادب په اړه یادښت ولیکئ.'),
   ('7. What is the importance of the Urdu language and what is its role in national unity?', '7۔ اُردو زبان کی کیا اہمیت ہے اور اس کا قومی یک جہتی میں کیا کردار ہے؟', '۷. د اردو ژبې اهمیت څه دی او په ملي یووالي کې یې رول څه دی؟'),
   ('8. Write a comprehensive note on the evolution of the Pashto language and literature.', '8۔ پشتو زبان اور ادب کے ارتقا پر جامع نوٹ لکھیں۔', '۸. د پښتو ژبې او ادب د ودې په اړه جامع یادښت ولیکئ.'),
   ('9. Sindhi is an ancient language. Make this clear with arguments.', '9۔ سندھی ایک قدیم زبان ہے۔ دلائل سے واضح کریں۔', '۹. سندهي یوه لرغونې ژبه ده. په دلایلو یې روښانه کړئ.'),
   ('10. State the importance of Balochi as a regional language.', '10۔ علاقائی زبان کے طور پر بلوچی کی اہمیت بیان کریں۔', '۱۰. د سیمه‌ییزې ژبې په توګه د بلوڅي اهمیت بیان کړئ.')])
ex = BOOK.record(e, 'pak12-ch7-exercise', 'Exercise', 'مشق', 'تمرین', 78, [145, 146])
issues = [{'id': 'pak12-pdf078', 'unit': 7, 'printedPage': 145,
           'description': 'Q2(ii) lists “خواجہ مسعود سلمان” (the text has “مسعود سعد سلمان”); Q2(v) offers “دوست محمد کامل”, not mentioned in the chapter; Q3(iii) says Shinwari gave the ghazal “regular genre” status (text: “great progress”); the match table has “فضل نامہ” (Khushal’s work) in column B. All retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(78, [(7, ex)], issues=issues, complete_units=[7])
