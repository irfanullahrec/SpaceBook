from physics_agent1_sequential import save, render
def tr(text,urdu,pashto): return dict(text=text,urdu=urdu,pashto=pashto,translationOrigin='SpaceBook')
paras=[
 tr('In physics we deal with numbers that are either very small or very large, it becomes difficult to write these numbers. For example, the mass of moon is approximately 70,000,000,000,000,000,000,000 kilograms. If we use this number often, we would surely like to have a more compact notation for it. This is exactly what standard form or scientific notation is. It represents a number as the product of a number greater than 1 and less than 10 (called the mantissa) and a power of 10 (termed as exponent):',
 'طبیعیات میں ہمیں بہت چھوٹے یا بہت بڑے اعداد سے واسطہ پڑتا ہے، جنہیں لکھنا مشکل ہو جاتا ہے۔ مثلاً چاند کی کمیت تقریباً 70,000,000,000,000,000,000,000 کلوگرام ہے۔ اگر یہ عدد بار بار استعمال ہو تو ہم اسے زیادہ مختصر انداز میں لکھنا چاہیں گے۔ معیاری صورت یا سائنسی طرزِ اظہار یہی ہے۔ اس میں عدد کو 1 سے بڑے اور 10 سے چھوٹے عدد، جسے مینٹیسا کہتے ہیں، اور 10 کی کسی قوت، جسے ایکسپوننٹ کہتے ہیں، کے حاصلِ ضرب کی صورت میں ظاہر کیا جاتا ہے:',
 'په فزیک کې له ډېر کوچنیو یا ډېرو لویو عددونو سره کار کوو، چې لیکل یې ستونزمن کېږي. د بېلګې په توګه، د سپوږمۍ کتله شاوخوا 70,000,000,000,000,000,000,000 کیلوګرامه ده. که دا عدد ډېر کاروو، نو په لا لنډه بڼه یې لیکل غواړو. معیاري یا علمي بڼه همدا ده. عدد د داسې عدد، چې له 1 څخه لوی او له 10 څخه کوچنی وي او مانتیسا بلل کېږي، او د 10 د یوې قوې، چې توان بلل کېږي، د ضرب په بڼه څرګندېږي:'),
 tr('number (N) = mantissa (M) × 10ⁿ, where n is the exponent.','عدد (N) = مینٹیسا (M) × 10ⁿ، جہاں n ایکسپوننٹ ہے۔','عدد (N) = مانتیسا (M) × 10ⁿ، چې n توان دی.'),
 tr('The mass of moon can thus be written compactly as 7 × 10²² kg, where 7 is the mantissa and 22 is the exponent. Similarly, the diameter of atomic nucleus is about 0.00000000000001m, which in standard form or scientific notation is 1 × 10⁻¹⁴ m.',
 'یوں چاند کی کمیت مختصراً 7 × 10²² کلوگرام لکھی جا سکتی ہے، جہاں 7 مینٹیسا اور 22 ایکسپوننٹ ہے۔ اسی طرح جوہری مرکزے کا قطر تقریباً 0.00000000000001 میٹر ہے، جو معیاری صورت یا سائنسی طرزِ اظہار میں 1 × 10⁻¹⁴ میٹر ہے۔',
 'په دې توګه د سپوږمۍ کتله په لنډ ډول 7 × 10²² کیلوګرامه لیکل کېږي، چې 7 مانتیسا او 22 توان دی. همدارنګه د اټومي هستې قطر شاوخوا 0.00000000000001 متره دی، چې په معیاري یا علمي بڼه 1 × 10⁻¹⁴ متره کېږي.'),
 tr('STEPS FOR CONVERTING NUMBER TO STANDARD FORM','عدد کو معیاری صورت میں تبدیل کرنے کے مراحل','معیاري بڼې ته د عدد د بدلولو ګامونه'),
 tr('1. In a given number N, move the decimal point and place it after first non-zero digit which will make it mantissa (M).',
 '1۔ دیے گئے عدد N میں اعشاری نقطہ حرکت دے کر پہلے غیر صفر ہندسے کے بعد رکھیں؛ اس سے مینٹیسا (M) حاصل ہوگا۔',
 '1. په ورکړل شوي عدد N کې اعشاري ټکی ولېږدوئ او د لومړي ناصفر رقم وروسته یې کېږدئ؛ دا به مانتیسا (M) شي.'),
 tr('2. If the decimal is moved towards left from its given initial position then the power of 10 will be positive and whatever is the number of digits through which the decimal point has been moved that will be the value of exponent (power of 10).',
 '2۔ اگر اعشاری نقطہ اپنی ابتدائی جگہ سے بائیں طرف منتقل کیا جائے تو 10 کی قوت مثبت ہوگی، اور جتنے ہندسے اعشاری نقطہ عبور کرے گا، اتنی ہی ایکسپوننٹ، یعنی 10 کی قوت، کی قدر ہوگی۔',
 '2. که اعشاري ټکی له خپلې لومړنۍ ځایه چپ لوري ته ولېږدول شي، د 10 توان به مثبت وي، او د هغو رقمونو شمېر چې اعشاري ټکی ترې تېر شوی دی، د توان ارزښت به وي.'),
 tr('3. Similarly, if the decimal point is moved towards right from its given position then the power of 10 will be negative and whatever is the number of digits through which the decimal point has been moved that will be the value of exponent (power of 10).',
 '3۔ اسی طرح اگر اعشاری نقطہ اپنی جگہ سے دائیں طرف منتقل کیا جائے تو 10 کی قوت منفی ہوگی، اور جتنے ہندسے نقطہ عبور کرے گا، اتنی ہی ایکسپوننٹ، یعنی 10 کی قوت، کی عددی قدر ہوگی۔',
 '3. همدارنګه، که اعشاري ټکی له خپلې ورکړل شوې ځایه ښي لوري ته ولېږدول شي، د 10 توان به منفي وي، او د هغو رقمونو شمېر چې اعشاري ټکی ترې تېر شوی دی، د توان عددي ارزښت به وي.'),
 tr('Example 1.1 AVERAGE DISTANCE BETWEEN EARTH AND MOON','مثال 1.1: زمین اور چاند کے درمیان اوسط فاصلہ','بېلګه 1.1: د ځمکې او سپوږمۍ ترمنځ منځنی واټن'),
 tr('Average distance between earth and moon is 384,400,000 m. Write this number in Standard form / scientific notation.',
 'زمین اور چاند کے درمیان اوسط فاصلہ 384,400,000 میٹر ہے۔ اس عدد کو معیاری صورت یا سائنسی طرزِ اظہار میں لکھیں۔',
 'د ځمکې او سپوږمۍ ترمنځ منځنی واټن 384,400,000 متره دی. دا عدد په معیاري یا علمي بڼه ولیکئ.'),
 tr('For Standard form / scientific notation we can write the term as distance = 384400000.0 × 10⁰ m',
 'معیاری صورت یا سائنسی طرزِ اظہار کے لیے ہم یوں لکھ سکتے ہیں: فاصلہ = 384400000.0 × 10⁰ میٹر۔',
 'د معیاري یا علمي بڼې لپاره داسې لیکلای شو: واټن = 384400000.0 × 10⁰ متره.'),
 tr('For Standard form / scientific notation in order to get mantissa (M) in which the 1st digit before the decimal is non-zero, we have to move the decimal 8 digits towards left. Therefore, the power of 10 will be positive 8, that is distance = 3.84400000 × 10⁸ m — Answer',
 'معیاری صورت یا سائنسی طرزِ اظہار میں ایسا مینٹیسا (M) حاصل کرنے کے لیے، جس میں اعشاری نقطے سے پہلے پہلا ہندسہ غیر صفر ہو، اعشاری نقطہ 8 ہندسے بائیں طرف منتقل کرنا ہوگا۔ لہٰذا 10 کی قوت مثبت 8 ہوگی، یعنی فاصلہ = 3.84400000 × 10⁸ میٹر — جواب۔',
 'په معیاري یا علمي بڼه کې د داسې مانتیسا (M) د ترلاسه کولو لپاره چې له اعشاري ټکي مخکې لومړی رقم ناصفر وي، اعشاري ټکی باید 8 رقمونه چپ لوري ته ولېږدوو. نو د 10 توان به مثبت 8 وي، یعنې واټن = 3.84400000 × 10⁸ متره — ځواب.'),
 tr('EXTENSION EXERCISE 1.1: Why we used the word average in problem statement.',
 'اضافی مشق 1.1: سوال کے بیان میں اوسط کا لفظ کیوں استعمال کیا گیا ہے؟',
 'اضافي تمرین 1.1: د مسئلې په بیان کې د منځني کلمه ولې کارول شوې ده؟')
]
example=dict(num='1.1',title='AVERAGE DISTANCE BETWEEN EARTH AND MOON',statement=paras[8]['text'],given='Distance = 384,400,000 m',required='Standard form / scientific notation',formula='N = M × 10ⁿ',solution=paras[9]['text']+'\n\n'+paras[10]['text'],answer='3.84400000 × 10⁸ m',sourcePdfPage=15,sourcePrintedPage=10,solutionOrigin='textbook')
save(dict(pdfPage=15,printedPage=10,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',title='Scientific notation / Example 1.1',numericals=[example],sections=[dict(code='1.4',heading='1.4 Standard Form / Scientific Notation',paras=paras,blocks=[dict(type='formula',latex=r'N=M\times10^n'),dict(type='extensionExercise',number='1.1',question=paras[-1]['text'])])],comparison='Preserved original paragraph, numbered three-step list and full worked solution separately; original answer precision retained; extension question stored without invented solution'))
render(16)
