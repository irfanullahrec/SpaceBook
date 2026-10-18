# -*- coding: utf-8 -*-
TITLE = 'Example 4.4 Seesaw balance / Extension Exercise 4.2 / Assignment 4.4'
SECTIONS = [
    ('ex4.4', ('Example 4.4 SEESAW BALANCE', 'مثال 4.4 سی سا کا توازن', '4.4 مثال د ټال توازن'), [
        ('p', 'Two Children Romiasa and Sanaan are sitting on a seesaw. The see-saw is balanced on a pivot as Romiasa is at 1 m and Sanaan at 1.5 m from the pivot (as shown in figure). If Romiasa weight is 600 N, what is the weight of Sanaan?', 'دو بچے رومیسہ اور سنان ایک سی سا پر بیٹھے ہیں۔ سی سا محور پر متوازن ہے جبکہ رومیسہ محور سے 1 m اور سنان 1.5 m پر ہے (جیسا کہ شکل میں ہے)۔ اگر رومیسہ کا وزن 600 N ہو تو سنان کا وزن کیا ہے؟', 'دوه ماشومان رومیسه او سنان پر یوه ټال ناست دي. ټال پر محور متوازن دی؛ رومیسه له محور 1 m او سنان 1.5 m لرې دی (لکه په شکل کې). که د رومیسې وزن 600 N وي، د سنان وزن څومره دی؟'),
        ('fig', 'Figure: seesaw with d_R = 1 m, d_S = 1.5 m, W_R = 600 N, W_S = ?', 'شکل: سی سا جس میں d_R = 1 m، d_S = 1.5 m، W_R = 600 N، W_S = ?', 'شکل: ټال چې d_R = 1 m، d_S = 1.5 m، W_R = 600 N، W_S = ?'),
        ('h', 'SOLUTION — GIVEN:', 'حل — معلوم:', 'حل — ورکړل شوي:'),
        ('ul', [('Romaisa’s Weight W_R = 600 N', 'رومیسہ کا وزن W_R = 600 N', 'د رومیسې وزن W_R = 600 N'), ('Romaisa’s Moment arm = d_R = 1 m', 'رومیسہ کا مومنٹ آرم = d_R = 1 m', 'د رومیسې مومنټ بازو = d_R = 1 m'), ('Sanaan’s Moment arm = d_S = 1.5 m', 'سنان کا مومنٹ آرم = d_S = 1.5 m', 'د سنان مومنټ بازو = d_S = 1.5 m')]),
        ('h', 'REQUIRED:', 'مطلوب:', 'غوښتل شوي:'),
        ('p', 'Sanaan’s Weight W_S = ?', 'سنان کا وزن W_S = ?', 'د سنان وزن W_S = ?'),
        ('p', 'Here Romaisa is producing anticlockwise torque, while Sanaan is producing clockwise torque, Therefor by second condition of equilibrium', 'یہاں رومیسہ خلافِ گھڑی وار ٹارک پیدا کر رہی ہے جبکہ سنان گھڑی وار ٹارک، لہٰذا توازن کی دوسری شرط سے', 'دلته رومیسه د ساعت خلاف تورک او سنان د ساعت لوري تورک پیدا کوي، نو د توازن د دویم شرط له مخې'),
        ('eq', None, 'τ_R − τ_S = 0'),
        ('p', 'As the see-saw is balanced, therefore we can write second condition of equilibrium as principle of moments ‘The Sum of the clockwise moments = sum of the anticlockwise moments', 'چونکہ سی سا متوازن ہے، اس لیے ہم توازن کی دوسری شرط کو مومنٹس کے اصول کے طور پر لکھ سکتے ہیں: \'گھڑی وار مومنٹس کا مجموعہ = خلافِ گھڑی وار مومنٹس کا مجموعہ', 'څرنګه چې ټال متوازن دی، د توازن دویم شرط د مومنټونو د اصل په توګه لیکلی شو: \'د ساعت لوري مومنټونو مجموعه = د ساعت خلاف مومنټونو مجموعه'),
        ('eq', None, 'τ_R = τ_S'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', None, 'W_R d_R = W_S d_S'),
        ('p', 'dividing both sides by d_S', 'دونوں طرف d_S سے تقسیم کرنے پر', 'دواړه خواوې پر d_S وېشلو سره'),
        ('eq', None, 'W_S = [[W_R d_R|d_S]]'),
        ('p', 'putting values', 'قدریں رکھنے سے', 'د ارزښتونو په ایښودلو'),
        ('eq', None, 'W_S = [[600 N × 1 m|1.5]]'),
        ('p', 'therefore', 'لہٰذا', 'نو'),
        ('eq', None, 'W_S = 400 N   Answer'),
        ('p', 'Hence the weight of Sanaan is 400 N.', 'لہٰذا سنان کا وزن 400 N ہے۔', 'نو د سنان وزن 400 N دی.'),
        ('h', 'EXTENSION EXERCISE 4.2', 'توسیعی مشق 4.2', '4.2 پراخه تمرین'),
        ('p', 'Find the mass of Sanaan and Romaisa.', 'سنان اور رومیسہ کی کمیت معلوم کریں۔', 'د سنان او رومیسې کتله معلومه کړئ.'),
    ]),
    ('as4.4', ('Assignment 4.4 CALCULATING MASSES', 'اسائنمنٹ 4.4 کمیتوں کا حساب', '4.4 دنده د کتلو محاسبه'), [
        ('p', 'With a beam two masses m₁ and m₂ are suspended at distance 0.4 m and 0.5 m respectively from suspension point as shown in the figure. Ignoring the weight of the balance, if m₂ = 1.6 kg, what is the mass m₁?', 'ایک بیم سے دو کمیتیں m₁ اور m₂ لٹکانے کے نقطے سے بالترتیب 0.4 m اور 0.5 m کے فاصلے پر لٹکائی گئی ہیں جیسا کہ شکل میں ہے۔ ترازو کے وزن کو نظر انداز کرتے ہوئے اگر m₂ = 1.6 kg ہو تو کمیت m₁ کیا ہے؟', 'له یوه شاه تیر څخه دوه کتلې m₁ او m₂ د ځړولو له ټکي په ترتیب 0.4 m او 0.5 m واټن کې ځړول شوې لکه په شکل کې. د تلې وزن له پامه غورځولو سره، که m₂ = 1.6 kg وي، m₁ کتله څومره ده؟'),
        ('fig', 'Figure: beam with m₁ = ? kg at d₁ = 0.4 m and m₂ = 1.6 kg at d₂ = 0.5 m.', 'شکل: بیم جس میں d₁ = 0.4 m پر m₁ = ? kg اور d₂ = 0.5 m پر m₂ = 1.6 kg۔', 'شکل: شاه تیر چې په d₁ = 0.4 m کې m₁ = ? kg او په d₂ = 0.5 m کې m₂ = 1.6 kg.'),
    ]),
]
