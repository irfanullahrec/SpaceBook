"""PDF71 (printed 129–130): Unit 13 third conditional 14–20; C matching table; D simple/compound/complex 1–10 (unit end); Unit 14 opener 'Lingkuan Gorge' (Tu Peng-Cheng) outcomes."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
TC = ['They ____ (be) late if they ____ (not / take) a taxi.', 'She ____ (not / meet) him if she ____ (not / come) to Islamabad.', 'He ____ (take) a taxi if he ____ (have) enough money.', 'I ____ (call) you if I ____ (not / forget) my phone.',
      'We ____ (come) if we ____ (be) invited.', 'She ____ (not / do) it if she ____ (know) you were ill.', 'He ____ (be) on time if he ____ (leave) earlier.']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(TC, 14)])
for p in w.paras: p['untranslatedByDesign'] = True
w.p('C. Match the two halves of the conditional sentences given in column A and B', 'C. کالم A اور B میں دیے گئے شرطیہ جملوں کے دونوں حصوں کو ملائیں', 'C. د A او B په ستونونو کې د ورکړل شویو شرطي جملو دواړه نیمایي سره برابرې کړئ')
M = [["I wouldn't have overslept", "if you'd asked."], ['If she had gone to bed earlier,', "you wouldn't have been so stressed at the last minute."], ['I could have lent you the money', "she wouldn't have been so tired."],
     ["They wouldn't have found out", 'if you had studied medicine.'], ['You could have been a doctor', 'if my alarm clock had gone off.'], ["If you'd been more organised,", "they wouldn't have had so many problems."], ["If they'd taken my advice,", "if you hadn't told them."]]
w.table('eng12-u13-cond-match', ['A', 'B'], M, ['A', 'B'], ['A', 'B'], M, M)
w.p('D. Write simple, compound or complex before relevant sentence.', 'D. متعلقہ جملے سے پہلے سادہ، مرکب یا پیچیدہ لکھیں۔', 'D. د اړوندې جملې مخکې ساده، مرکبه یا پېچلې ولیکئ.')
D = ['Life is a bed of thorns.', 'It is never a bed of roses.', 'Man struggles hard to earn his living.', 'He runs after money and wants to enjoy power.', 'In the race for money and power he gets hurt.', 'Fears, worries and frustration hurt his mind.',
     'He becomes restless and loses peace of mind.', 'He realises that money is not everything in life.', 'It gives temporary satisfaction, but robs him of peace and happiness in life.', 'What makes man happy is contentment.']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(D, 1)])
for p in w.paras[-len(D):]: p['untranslatedByDesign'] = True
ex = BOOK.record(w, 'eng12-u13-vocab-c', 'Third conditional 14–20; C matching; D sentence types', 'تیسرا شرطیہ 14–20؛ C ملانا؛ D جملوں کی اقسام', 'درېیم شرطي 14–20؛ C برابرول؛ D د جملو ډولونه', 71, [129])

UT = ('Lingkuan Gorge', 'لنگ کوان گھاٹی', 'لینګ‌کوان دره')
o = Builder()
o.h('Unit 14 — Lingkuan Gorge (A Man Should Never Leave his Post) — Tu Peng-Cheng', 'یونٹ 14 — لنگ کوان گھاٹی (آدمی کو کبھی اپنی جگہ نہیں چھوڑنی چاہیے) — تو پنگ چینگ', 'واحد 14 — لینګ‌کوان دره (سړی باید هېڅکله خپل پوسټ پرې نه ږدي) — تو پنګ چېنګ')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Use pre-reading strategies to predict the content of a text from topic / picture, title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.', 'سابقہ علم، سوالات اور سیاقی اشاروں کو استعمال کرتے ہوئے موضوع / تصویر، عنوان / سرخیوں، کلیدی الفاظ اور بصری مواد وغیرہ سے متن کے مواد کی پیش گوئی کے لیے مطالعے سے پہلے کی حکمتِ عملیاں استعمال کریں۔', 'د مخکینۍ پوهې، پوښتنو او شرایطي نښو په کارولو د موضوع / انځور، سرلیک / سرټکو، کلیدي کلمو او لیدنیزو موادو څخه د متن د منځپانګې د وړاندوینې لپاره د لوستلو مخکې ستراتیژۍ وکاروي.'),
    ('Analyze passages in the text to identify the theme/ general subject, key idea/ central thought (a statement about the general subject), and supporting details.', 'متن کے اقتباسات کا تجزیہ کر کے موضوع/ عمومی مضمون، کلیدی خیال/ مرکزی سوچ (عمومی مضمون کے بارے میں ایک بیان) اور معاون تفصیلات کی نشاندہی کریں۔', 'د متن برخې تحلیل کړي ترڅو موضوع/ عمومي مضمون، کلیدي نظر/ مرکزي فکر (د عمومي مضمون په اړه یو بیان) او ملاتړي جزییات وپېژني.'),
    ('Apply critical thinking to interact with text and use intensive reading strategies (while-reading) to: scan to answer short questions; make simple inferences using context of the text and prior knowledge; distinguish between what is clearly stated and what is implied.', 'متن سے تعامل کے لیے تنقیدی سوچ کا اطلاق کریں اور گہرے مطالعے کی حکمتِ عملیاں (دورانِ مطالعہ) استعمال کریں تاکہ: مختصر سوالات کے جواب کے لیے تلاش کریں؛ متن کے سیاق اور سابقہ علم سے سادہ نتائج اخذ کریں؛ واضح طور پر بیان کردہ اور ضمنی بات میں فرق کریں۔', 'له متن سره د تعامل لپاره انتقادي فکر پلي کړي او د ژورو لوستلو ستراتیژۍ (د لوستلو پر مهال) وکاروي ترڅو: د لنډو پوښتنو د ځوابولو لپاره ولټوي؛ د متن له شرایطو او مخکینۍ پوهې ساده پایلې واخلي؛ د ښکاره ویل شوي او ضمني ترمنځ توپیر وکړي.'),
    ('Use critical thinking to respond orally and in writing to the text (post-reading) to: give a personal opinion and justify stance related to viewpoints/ ideas and issues in the text read; relate what is read to his or her own feelings and experiences; explore causes and consequences of a problem or an issue and propose various solutions; evaluate material read.', 'تنقیدی سوچ استعمال کرتے ہوئے متن پر زبانی اور تحریری ردِعمل دیں (مطالعے کے بعد) تاکہ: پڑھے گئے متن کے نقطۂ ہائے نظر/ خیالات اور مسائل پر ذاتی رائے دیں اور موقف کا جواز پیش کریں؛ جو پڑھا اسے اپنے احساسات اور تجربات سے جوڑیں؛ کسی مسئلے کے اسباب و نتائج کی جستجو کریں اور مختلف حل تجویز کریں؛ پڑھے گئے مواد کا جائزہ لیں۔', 'د انتقادي فکر په کارولو متن ته په خوله او لیکلي ډول غبرګون وښيي (له لوستلو وروسته) ترڅو: د لوستل شوي متن د لیدلورو/ نظرونو او مسایلو په اړه شخصي نظر ورکړي او دریځ یې ثابت کړي؛ لوستل شوي له خپلو احساساتو او تجربو سره وتړي؛ د یوې ستونزې لاملونه او پایلې وسپړي او بېلابېل حلونه وړاندیز کړي؛ لوستل شوي مواد وارزوي.'),
    ('Use appropriate vocabulary and spelling in their own writing .', 'اپنی تحریر میں موزوں ذخیرۂ الفاظ اور املا استعمال کریں۔', 'په خپله لیکنه کې مناسب لغات او املا وکاروي.'),
    ('Identify, analyze and construct conditional sentences.', 'شرطیہ جملوں کی نشاندہی، تجزیہ اور تشکیل کریں۔', 'شرطي جملې وپېژني، تحلیل او جوړې کړي.'),
    ('Analyze and construct simple, compound and complex sentences.', 'سادہ، مرکب اور پیچیدہ جملوں کا تجزیہ اور تشکیل کریں۔', 'ساده، مرکبې او پېچلې جملې تحلیل او جوړې کړي.'),
])
op = BOOK.record(o, 'eng12-u14-outcomes', 'Unit 14 — learning outcomes', 'یونٹ 14 — تعلیمی نتائج', 'واحد 14 — د زده کړې پایلې', 71, [130], unit_title=UT)

if __name__ == '__main__':
    BOOK.save(71, [(13, ex), (14, op)], complete_units=[13])
