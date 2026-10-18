"""PDF94 (printed 175–176): Unit 17 reported-speech activity 1–11 (no 6; unit end); Unit 18 'Lines from the Deserted Village' (Oliver Goldsmith) outcomes."""
from class12_book_common import Book, Builder

BOOK = Book('english')
v = Builder()
v.h('Activity', 'سرگرمی', 'فعالیت')
v.p('Complete the given sentences in Reported Speech. Mind the introductory sentences and backshift of tenses.', 'دیے گئے جملوں کو بالواسطہ کلام میں مکمل کریں۔ تمہیدی جملوں اور زمانوں کی پیچھے منتقلی (backshift) کا خیال رکھیں۔', 'ورکړل شوې جملې په غیرمستقیمه وینا بشپړې کړئ. سریزه‌ییزو جملو او د زمانونو شاته تګ (backshift) ته پام وکړئ.')
A = [(1, 'Tahira: "She works in an office." — Tahira said (that) she ____'), (2, 'Jamila: "I am going to clean the room." — Jamila told me (that) she____'), (3, 'Jaffer: "They like the song." — Jaffer said (that) they ____'),
     (4, 'Iman and Marva: "We need new shoes." — Iman and Marva remarked (that) they ____'), (5, 'Kamran: "He can speak Spanish." — Kamran told us (that) he'), (7, 'Teacher: "Rauf has never been to Karachi." — The teacher said (that) Rauf ____'),
     (8, 'Luqman: The train didn\'t arrive on time." — Luqman said to Gul (that) the train'), (9, 'Eyma: "I\'m sitting on the chair." — Eyma said (that) she ____'), (10, 'Nauman: "Waleed doesn\'t eat meat." — Nauman told us (that) Waleed____'),
     (11, 'Hamid: "Abrahim and Naummy will travel to Kaghan." — Hamid remarked (that) Abrahim and Naummy____')]
v.group('lines', [(f'{n}. {s}',) * 3 for n, s in A])
for p in v.paras[-len(A):]: p['untranslatedByDesign'] = True
a = BOOK.record(v, 'eng12-u17-vocab-f', 'Reported speech — activity', 'بالواسطہ کلام — سرگرمی', 'غیرمستقیمه وینا — فعالیت', 94, [175])

UT = ('Lines from the Deserted Village (Poem)', 'اجڑے گاؤں سے اشعار (نظم)', 'له وران کلي څخه بیتونه (شعر)')
o = Builder()
o.h('Unit 18 — Lines from the deserted village (Poem) — Oliver Goldsmith', 'یونٹ 18 — اجڑے گاؤں سے اشعار (نظم) — اولیور گولڈ اسمتھ', 'واحد 18 — له وران کلي څخه بیتونه (شعر) — اولیور ګولډسمیټ')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
CT = ('Use critical thinking to respond orally and in writing to the text (post-reading ) to: give a personal opinion and justify stance related to viewpoints/ ideas and issues in the text read; relate what is read to his or her own feelings and experiences; explore causes and consequences of a problem or an issue and propose various solutions.',
      'تنقیدی سوچ استعمال کرتے ہوئے متن پر زبانی اور تحریری ردِعمل دیں (مطالعے کے بعد) تاکہ: پڑھے گئے متن کے نقطۂ ہائے نظر/ خیالات اور مسائل پر ذاتی رائے دیں اور موقف کا جواز پیش کریں؛ جو پڑھا اسے اپنے احساسات اور تجربات سے جوڑیں؛ کسی مسئلے کے اسباب و نتائج کی جستجو کریں اور مختلف حل تجویز کریں۔',
      'د انتقادي فکر په کارولو متن ته په خوله او لیکلي ډول غبرګون وښيي (له لوستلو وروسته) ترڅو: د لوستل شوي متن د لیدلورو/ نظرونو او مسایلو په اړه شخصي نظر ورکړي او دریځ یې ثابت کړي؛ لوستل شوي له خپلو احساساتو او تجربو سره وتړي؛ د یوې ستونزې لاملونه او پایلې وسپړي او بېلابېل حلونه وړاندیز کړي.')
AN = ('Analyze how a writer/ poet uses language to: appeal to the senses through use of figurative language including similes, metaphors and imagery.',
      'تجزیہ کریں کہ ایک مصنف/ شاعر زبان کیسے استعمال کرتا ہے تاکہ: تشبیہات، استعارات اور پیکر تراشی سمیت مجازی زبان کے ذریعے حواس کو متاثر کرے۔',
      'تحلیل کړي چې یو لیکوال/ شاعر ژبه څنګه کاروي ترڅو: د تشبیهاتو، استعارو او انځورګرۍ په ګډون د مجازي ژبې له لارې حواسو ته اپیل وکړي.')
o.group('list', [
    ('Read a given poem and give orally and in writing: Theme and its development; Personal response with justification; Recognize literary techniques such as personification and alliteration.', 'دی گئی نظم پڑھیں اور زبانی و تحریری طور پر بیان کریں: موضوع اور اس کا ارتقا؛ جواز کے ساتھ ذاتی ردِعمل؛ ادبی تکنیکوں جیسے تجسیم اور تکرارِ حرفی کو پہچانیں۔', 'ورکړل شوی شعر ولولي او په خوله او لیکلي ډول ووايي: موضوع او د هغې وده؛ د دلیل سره شخصي غبرګون؛ ادبي تخنیکونه لکه تجسیم او د تورو تکرار وپېژني.'),
    CT, AN,
    ('Use critical thinking to respond orally and in writing to the text (post-reading ) to: give a personal opinion and justify stance related to viewpoints/ ideas and issues in the text read; relate what is read to his or her own feelings and experiences; scan to answer short questions; make simple inferences using context of the text and prior knowledge; distinguish between what is clearly stated and what is implied .',
     'تنقیدی سوچ استعمال کرتے ہوئے متن پر زبانی اور تحریری ردِعمل دیں (مطالعے کے بعد) تاکہ: پڑھے گئے متن کے نقطۂ ہائے نظر/ خیالات اور مسائل پر ذاتی رائے دیں اور موقف کا جواز پیش کریں؛ جو پڑھا اسے اپنے احساسات اور تجربات سے جوڑیں؛ مختصر سوالات کے جواب کے لیے تلاش کریں؛ متن کے سیاق اور سابقہ علم سے سادہ نتائج اخذ کریں؛ واضح اور ضمنی بات میں فرق کریں۔',
     'د انتقادي فکر په کارولو متن ته په خوله او لیکلي ډول غبرګون وښيي (له لوستلو وروسته) ترڅو: د لوستل شوي متن د لیدلورو/ نظرونو او مسایلو په اړه شخصي نظر ورکړي او دریځ یې ثابت کړي؛ لوستل شوي له خپلو احساساتو او تجربو سره وتړي؛ د لنډو پوښتنو د ځوابولو لپاره ولټوي؛ د متن له شرایطو او مخکینۍ پوهې ساده پایلې واخلي؛ د ښکاره او ضمني ترمنځ توپیر وکړي.'),
    AN,
    ('Use a thesaurus to locate the synonyms closest to the meaning of the given words.', 'دیے گئے الفاظ کے معنی کے قریب ترین مترادفات تلاش کرنے کے لیے تھیسارس (لغتِ مترادفات) استعمال کریں۔', 'د ورکړل شویو کلمو مانا ته د نږدې مترادفو موندلو لپاره تیسارس (د مترادفو قاموس) وکاروي.'),
    ('Use direct and indirect speech appropriately in speech and writing according to the required communicative function.', 'مطلوبہ ابلاغی مقصد کے مطابق گفتگو اور تحریر میں براہِ راست اور بالواسطہ کلام کو موزوں طور پر استعمال کریں۔', 'د اړین اړیکه‌ییز موخې سره سم په خبرو او لیکنه کې مستقیمه او غیرمستقیمه وینا په مناسب ډول وکاروي.'),
])
op = BOOK.record(o, 'eng12-u18-outcomes', 'Unit 18 — learning outcomes', 'یونٹ 18 — تعلیمی نتائج', 'واحد 18 — د زده کړې پایلې', 94, [176], unit_title=UT)
issues = [{'id': 'eng12-p175-176', 'unit': 17, 'printedPage': 175, 'description': 'Reported-speech activity skips item 6 (1–5, 7–11) as printed; item 8 lacks an opening quote; items 5 and 8 have no answer line. Unit 18 outcomes repeat “Analyze how a writer/ poet uses language…” as printed.'}]

if __name__ == '__main__':
    BOOK.save(94, [(17, a), (18, op)], issues=issues, complete_units=[17])
