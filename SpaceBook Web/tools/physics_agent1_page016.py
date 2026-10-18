from physics_agent1_sequential import save, render
def tr(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto,translationOrigin='SpaceBook')
paras=[
 tr('Which is the average distance between earth and moon in standard form or scientific notation.','یہ زمین اور چاند کے درمیان اوسط فاصلہ معیاری صورت یا سائنسی طرزِ اظہار میں ہے۔','دا د ځمکې او سپوږمۍ ترمنځ منځنی واټن په معیاري یا علمي بڼه دی.'),
 tr('Assignment 1.1 MASS OF EARTH','مشق 1.1: زمین کی کمیت','دنده 1.1: د ځمکې کتله'),
 tr('The mass of Earth is 5,980,000,000,000,000,000,000,000 kg, write this number in Standard form / scientific notation.',
 'زمین کی کمیت 5,980,000,000,000,000,000,000,000 کلوگرام ہے؛ اس عدد کو معیاری صورت یا سائنسی طرزِ اظہار میں لکھیں۔',
 'د ځمکې کتله 5,980,000,000,000,000,000,000,000 کیلوګرامه ده؛ دا عدد په معیاري یا علمي بڼه ولیکئ.'),
 tr('Example 1.2 NUMBER OF SECONDS IN A YEAR','مثال 1.2: ایک سال میں سیکنڈوں کی تعداد','بېلګه 1.2: په یوه کال کې د ثانیو شمېر'),
 tr('Find the number of seconds in a year and write the answer in Standard form or scientific notation.',
 'ایک سال میں سیکنڈوں کی تعداد معلوم کریں اور جواب معیاری صورت یا سائنسی طرزِ اظہار میں لکھیں۔',
 'په یوه کال کې د ثانیو شمېر ومومئ او ځواب په معیاري یا علمي بڼه ولیکئ.'),
 tr('We know that there are 365 days in a year (y), 24 hours in a day (d), 60 minutes in an hour (h), and 60 seconds (s) in a minute (min). These four relationships are conversion factors. Starting with 1 y and multiplying by these conversion factors, we obtain',
 'ہم جانتے ہیں کہ ایک سال (y) میں 365 دن، ایک دن (d) میں 24 گھنٹے، ایک گھنٹے (h) میں 60 منٹ اور ایک منٹ (min) میں 60 سیکنڈ (s) ہوتے ہیں۔ یہ چار تعلقات تبدیلی کے عوامل ہیں۔ ایک سال سے شروع کرکے ان عوامل سے ضرب دینے پر ہمیں حاصل ہوتا ہے:',
 'موږ پوهېږو چې په یوه کال (y) کې 365 ورځې، په یوه ورځ (d) کې 24 ساعته، په یوه ساعت (h) کې 60 دقیقې او په یوه دقیقه (min) کې 60 ثانیې (s) وي. دا څلور اړیکې د تبدیلۍ ضریبونه دي. له یوه کال څخه پیل او په دې ضریبونو ضرب کولو سره ترلاسه کوو:'),
 tr('1 y = 1 y × (365 d / 1 y) × (24 h / 1 d) × (60 min / 1 h) × (60 s / 1 min)',
 '1 سال = 1 سال × (365 دن / 1 سال) × (24 گھنٹے / 1 دن) × (60 منٹ / 1 گھنٹہ) × (60 سیکنڈ / 1 منٹ)',
 '1 کال = 1 کال × (365 ورځې / 1 کال) × (24 ساعته / 1 ورځ) × (60 دقیقې / 1 ساعت) × (60 ثانیې / 1 دقیقه)'),
 tr('or 1 y = 1 × 365 × 24 × 60 × 60 s; or 1 y = 31536000 s',
 'یا 1 سال = 1 × 365 × 24 × 60 × 60 سیکنڈ؛ یا 1 سال = 31536000 سیکنڈ۔',
 'یا 1 کال = 1 × 365 × 24 × 60 × 60 ثانیې؛ یا 1 کال = 31536000 ثانیې.'),
 tr('For Standard form / scientific notation we can write the term as 1 y = 31536000.0 × 10⁰ s',
 'معیاری صورت یا سائنسی طرزِ اظہار میں ہم یوں لکھ سکتے ہیں: 1 سال = 31536000.0 × 10⁰ سیکنڈ۔',
 'په معیاري یا علمي بڼه داسې لیکلای شو: 1 کال = 31536000.0 × 10⁰ ثانیې.'),
 tr('In order to get mantissa (M) in which the 1st digit before the decimal is non-zero, we have to move the decimal 7 digits towards left. Therefore, the power of 10 will be positive 7, that is 1 y = 3.1536000 × 10⁷ s — Answer',
 'ایسا مینٹیسا (M) حاصل کرنے کے لیے جس میں اعشاری نقطے سے پہلے پہلا ہندسہ غیر صفر ہو، اعشاری نقطہ 7 ہندسے بائیں طرف منتقل کرنا ہوگا۔ لہٰذا 10 کی قوت مثبت 7 ہوگی، یعنی 1 سال = 3.1536000 × 10⁷ سیکنڈ — جواب۔',
 'د داسې مانتیسا (M) د ترلاسه کولو لپاره چې له اعشاري ټکي مخکې لومړی رقم ناصفر وي، اعشاري ټکی باید 7 رقمونه چپ لوري ته ولېږدوو. نو د 10 توان مثبت 7 دی، یعنې 1 کال = 3.1536000 × 10⁷ ثانیې — ځواب.'),
 tr('EXTENSION EXERCISE 1.2: Is this value exact? After each 4 years we have a leap year in which we have 366 days, how would we account for that?',
 'اضافی مشق 1.2: کیا یہ قدر بالکل درست ہے؟ ہر 4 سال کے بعد لیپ سال آتا ہے جس میں 366 دن ہوتے ہیں؛ ہم اسے حساب میں کیسے شامل کریں گے؟',
 'اضافي تمرین 1.2: آیا دا ارزښت دقیق دی؟ هر څلور کاله وروسته یو کبیسه کال راځي چې 366 ورځې لري؛ دا به په حساب کې څنګه شامل کړو؟'),
 tr('Assignment 1.2 SECONDS IN A WEEK','مشق 1.2: ایک ہفتے میں سیکنڈ','دنده 1.2: په یوه اونۍ کې ثانیې'),
 tr('Calculate the number of seconds in a week. Express the number in power of 10 notation.',
 'ایک ہفتے میں سیکنڈوں کی تعداد کا حساب لگائیں۔ عدد کو 10 کی قوت کی صورت میں ظاہر کریں۔',
 'په یوه اونۍ کې د ثانیو شمېر حساب کړئ. عدد د 10 د توان په بڼه څرګند کړئ.'),
 tr('Example 1.3 SMALLEST MOLECULE','مثال 1.3: سب سے چھوٹا سالمہ','بېلګه 1.3: تر ټولو کوچنی مالیکول'),
 tr('The smallest molecule is the diatomic hydrogen (H₂), with a bond length of 0.000,000,000,074 m. Write the answer in Standard form.',
 'سب سے چھوٹا سالمہ دو جوہری ہائیڈروجن (H₂) ہے، جس کے بند کی لمبائی 0.000,000,000,074 میٹر ہے۔ جواب معیاری صورت میں لکھیں۔',
 'تر ټولو کوچنی مالیکول دوه اټومي هایدروجن (H₂) دی، چې د تړون اوږدوالی یې 0.000,000,000,074 متره دی. ځواب په معیاري بڼه ولیکئ.')
]
example=dict(num='1.2',title='NUMBER OF SECONDS IN A YEAR',statement=paras[4]['text'],given='365 days/year; 24 hours/day; 60 minutes/hour; 60 seconds/minute',required='Number of seconds in a year in standard form / scientific notation',formula='1 y = 1 y × (365 d / 1 y) × (24 h / 1 d) × (60 min / 1 h) × (60 s / 1 min)',solution='\n\n'.join(p['text'] for p in paras[5:10]),answer='1 y = 3.1536000 × 10⁷ s',sourcePdfPage=16,sourcePrintedPage=11,solutionOrigin='textbook')
blocks=[dict(type='assignment',number='1.1',title='MASS OF EARTH',question=paras[2]['text']),dict(type='formula',latex=r'1\,\mathrm{y}=1\,\mathrm{y}\times\frac{365\,\mathrm{d}}{1\,\mathrm{y}}\times\frac{24\,\mathrm{h}}{1\,\mathrm{d}}\times\frac{60\,\mathrm{min}}{1\,\mathrm{h}}\times\frac{60\,\mathrm{s}}{1\,\mathrm{min}}'),dict(type='extensionExercise',number='1.2',question=paras[10]['text']),dict(type='assignment',number='1.2',title='SECONDS IN A WEEK',question=paras[12]['text']),dict(type='exampleQuestion',number='1.3',question=paras[14]['text'],solutionStatus='Continues on immediately following PDF page')]
save(dict(pdfPage=16,printedPage=11,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',title='Assignments 1.1–1.2 / Examples 1.2–1.3',numericals=[example],sections=[dict(code='1.4',heading='1.4 Standard Form / Scientific Notation',paras=paras,blocks=blocks)],comparison='Full source solution and conversion factors retained; assignments and extension questions stored separately; Example 1.3 solution awaits next page'))
render(17)
