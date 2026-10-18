t = lambda n: f'{n:,}'.replace(',', '{,}')
out = ['@printed 19', '@deco Cartoon boy with cap beside the speech bubble; picture of a boy skipping with a rope (decorative).',
       'q 4 | Solve the following numbers. || درج ذیل اعداد کو حل کریں۔ || لاندې عددونه حل کړئ.']
for l, (a, b) in zip('abcdefgh', [(13440,15),(86449,29),(32536,56),(47088,48),(56780,20),(26166,98),(73810,11),(64454,32)]):
    q, r = divmod(a, b)
    out.append(f'qp {l} | ${t(a)} \div {b}$')
    ans = f'{q:,}' + (f' r {r}' if r else '')
    out.append(f'sol {ans} ## Long division: {b} × {q:,} = {b*q:,}, and {a:,} − {b*q:,} = {r}. || لمبی تقسیم: {b} × {q:,} = {b*q:,} اور {a:,} − {b*q:,} = {r}۔ || اوږد وېش: {b} × {q:,} = {b*q:,} او {a:,} − {b*q:,} = {r}.')
out += [
 'q 5 | Aliya has Rs. 22,580. She wants to distribute it among 18 people. || عالیہ کے پاس 22,580 روپے ہیں۔ وہ یہ رقم 18 لوگوں میں تقسیم کرنا چاہتی ہے۔ || د عالیې سره 22,580 روپۍ دي. غواړي دا پیسې پر 18 کسانو ووېشي.',
 'qp a | How much money will each person get? || ہر شخص کو کتنی رقم ملے گی؟ || هر کس ته به څومره پیسې ورسېږي؟',
 'sol Rs. 1,254 ## 22,580 ÷ 18 = 1,254 r 8. || 22,580 ÷ 18 = 1,254 باقی 8۔ || 22,580 ÷ 18 = 1,254 پاتې 8.',
 'qp b | How much money will be left? || کتنی رقم بچ جائے گی؟ || څومره پیسې به پاتې شي؟',
 'sol Rs. 8 ## The remainder of 22,580 ÷ 18 is 8 (18 × 1,254 = 22,572). || 22,580 ÷ 18 کا باقی 8 ہے (18 × 1,254 = 22,572)۔ || د 22,580 ÷ 18 پاتې شونی 8 دی (18 × 1,254 = 22,572).',
 "q 6 | Omar's monthly income is Rs. 13,582. Find his total income in 3 years. || عمر کی ماہانہ آمدنی 13,582 روپے ہے۔ 3 سال میں اس کی کل آمدنی معلوم کریں۔ || د عمر میاشتنی عاید 13,582 روپۍ دی. په 3 کلونو کې یې ټول عاید معلوم کړئ.",
 'sol Rs. 488,952 ## 3 years = 3 × 12 = 36 months; 13,582 × 36 = 488,952. || 3 سال = 3 × 12 = 36 مہینے؛ 13,582 × 36 = 488,952۔ || 3 کاله = 3 × 12 = 36 میاشتې؛ 13,582 × 36 = 488,952.',
 'q 7 | A toy factory manufactures 28,550 toys in 25 days. How many toys will it manufacture in one day? || کھلونوں کی ایک فیکٹری 25 دنوں میں 28,550 کھلونے بناتی ہے۔ ایک دن میں وہ کتنے کھلونے بنائے گی؟ || د لوبو یوه فابریکه په 25 ورځو کې 28,550 لوبې جوړوي. په یوه ورځ کې به څو لوبې جوړې کړي؟',
 'sol 1,142 toys ## 28,550 ÷ 25 = 1,142. || 28,550 ÷ 25 = 1,142۔ || 28,550 ÷ 25 = 1,142.',
 'q 8 | Hammad bought one laptop, for Rs. 89,710. Find the price of 10 such laptops. || حماد نے ایک لیپ ٹاپ 89,710 روپے میں خریدا۔ ایسے 10 لیپ ٹاپ کی قیمت معلوم کریں۔ || حماد یو لپ ټاپ په 89,710 روپیو واخیست. د داسې 10 لپ ټاپونو بیه معلومه کړئ.',
 'sol Rs. 897,100 ## 89,710 × 10 = 897,100 (put one zero to the right). || 89,710 × 10 = 897,100 (دائیں طرف ایک صفر لگائیں)۔ || 89,710 × 10 = 897,100 (ښي لوري ته یو صفر کېږدئ).',
 'q 9 | There are 145 boxes of pencils each containing 5 pencils. If 48 boxes have blue pencils and the rest have red pencils, find: || پنسلوں کے 145 ڈبے ہیں جن میں سے ہر ایک میں 5 پنسلیں ہیں۔ اگر 48 ڈبوں میں نیلی پنسلیں ہوں اور باقی میں سرخ، تو معلوم کریں: || د پنسلو 145 بکسونه دي چې په هر یوه کې 5 پنسلې دي. که په 48 بکسونو کې شنې (نیلي) پنسلې وي او په پاتې نورو کې سرې، نو معلوم کړئ:',
 'qp a | the total number of pencils. || پنسلوں کی کل تعداد۔ || د پنسلو ټول شمېر.',
 'sol 725 pencils ## 145 × 5 = 725. || 145 × 5 = 725۔ || 145 × 5 = 725.',
 'qp b | the number of red pencils. || سرخ پنسلوں کی تعداد۔ || د سرو پنسلو شمېر.',
 'sol 485 pencils ## Red boxes = 145 − 48 = 97; red pencils = 97 × 5 = 485. || سرخ ڈبے = 145 − 48 = 97؛ سرخ پنسلیں = 97 × 5 = 485۔ || سره بکسونه = 145 − 48 = 97؛ سرې پنسلې = 97 × 5 = 485.',
 'endexercise',
 '@sec u1-patterns | Number Patterns || عددی نمونے (پیٹرن) || د عددونو بېلګې (پېټرن)',
 '# Number Patterns || عددی نمونے (پیٹرن) || د عددونو بېلګې (پېټرن)',
 'box note',
 'p Arham has started exercising. He increased his exercise time gradually. He exercised for 5 minutes on Monady, 7 minutes on Tuesday and 9 minutes on Wednesday. If he keeps increasing the time in the same manner, for how many minutes will he exercise on Thursday? || ارحم نے ورزش شروع کی ہے۔ اس نے آہستہ آہستہ ورزش کا وقت بڑھایا۔ اس نے پیر کو 5 منٹ، منگل کو 7 منٹ اور بدھ کو 9 منٹ ورزش کی۔ اگر وہ اسی طرح وقت بڑھاتا رہے تو جمعرات کو کتنے منٹ ورزش کرے گا؟ || ارحم ورزش پیل کړې ده. هغه خپل د ورزش وخت ورو ورو زیات کړ. هغه د دوشنبې په ورځ 5 دقیقې، د سه شنبې په ورځ 7 دقیقې او د چهارشنبې په ورځ 9 دقیقې ورزش وکړ. که په همدې ډول وخت زیاتوي، د پنجشنبې په ورځ به څو دقیقې ورزش وکړي؟',
 'endbox',
 '@issue "Monady" (for Monday) is a printing error in the source; kept as printed.',
]
open('math/pages/p024.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
