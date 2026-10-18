# -*- coding: utf-8 -*-
TITLE = 'Example 7.4 solution / Assignment 7.4 density of rock / Activity: water and oil'
SECTIONS = [
    ('ex7.4-sol', ('Example 7.4 — solution', 'مثال 7.4 — حل', '7.4 مثال — حل'), [
        ('h', 'SOLUTION — GIVEN:', 'حل — معلوم:', 'حل — ورکړل شوي:'),
        ('ul', [('Weight in air W_A = 7.84 N', 'ہوا میں وزن W_A = 7.84 N', 'په هوا کې وزن W_A = 7.84 N'), ('Weight in water W_B = 6.86 N', 'پانی میں وزن W_B = 6.86 N', 'په اوبو کې وزن W_B = 6.86 N'), ('Density of water ρ_f = 1.00 × 10^3 kg/m³', 'پانی کی کثافت ρ_f = 1.00 × 10^3 kg/m³', 'د اوبو کثافت ρ_f = 1.00 × 10^3 kg/m³')]),
        ('h', 'REQUIRED:', 'مطلوب:', 'غوښتل شوي:'),
        ('p', 'Density of crown ρ_o = ?', 'تاج کی کثافت ρ_o = ?', 'د تاج کثافت ρ_o = ?'),
        ('p', 'The apparent weight of the crown in water W_B is equal to the weight in air W_A minus the buoyant force F_B exerted by water i.e. W_B = W_A − F_B which means that', 'پانی میں تاج کا ظاہری وزن W_B ہوا میں وزن W_A منفی پانی کی تیرانے والی قوت F_B کے برابر ہے یعنی W_B = W_A − F_B جس کا مطلب ہے', 'په اوبو کې د تاج ظاهري وزن W_B د هوا د وزن W_A او د اوبو د لامبو قوت F_B د تفاوت سره مساوي دی یعنې W_B = W_A − F_B چې معنا یې ده'),
        ('eq', None, 'F_B − W_A = W_B   [printed; i.e. F_B = W_A − W_B]'),
        ('eq', None, 'F_B = 7.84 N − 6.86 N'),
        ('eq', None, 'F_B = 0.98 N'),
        ('p', 'The relationship between the weight ‘W’ and the buoyant force ‘F_B’ is', 'وزن \'W\' اور تیرانے والی قوت \'F_B\' کے درمیان تعلق ہے', 'د وزن \'W\' او د لامبو قوت \'F_B\' ترمنځ اړیکه ده'),
        ('eq', None, '[[W|F_B]] = [[ρ_o|ρ_f]]'),
        ('p', 'Rearrange the equation to isolate the unknown:', 'نامعلوم کو الگ کرنے کے لیے مساوات کو ترتیب دیں:', 'د نامعلوم د جلا کولو لپاره معادله بیا ترتیب کړئ:'),
        ('eq', None, 'ρ_o = [[W|F_B]] × ρ_f'),
        ('p', 'putting values', 'قدریں رکھنے سے', 'د ارزښتونو په ایښودلو'),
        ('eq', None, 'ρ_o = [[7.84 N|0.98 N]] × 1 × 10^3 kg/m^3'),
        ('eq', None, 'therefore   ρ_o = 8 × 10^3 kg/m^3   Answer'),
        ('p', 'From Table 7.1, the density of gold is 19.3 × 10^3 kg/m³. As 8.0 × 10^3 kg/m³ is quite less than 19.3 × 10^3 kg/m³, the crown cannot be pure gold.', 'جدول 7.1 سے سونے کی کثافت 19.3 × 10^3 kg/m³ ہے۔ چونکہ 8.0 × 10^3 kg/m³ قدر 19.3 × 10^3 kg/m³ سے کافی کم ہے، تاج خالص سونے کا نہیں ہو سکتا۔', 'له 7.1 جدول څخه د سرو زرو کثافت 19.3 × 10^3 kg/m³ دی. څرنګه چې 8.0 × 10^3 kg/m³ له 19.3 × 10^3 kg/m³ ډېر کم دی، تاج خالص سره زر نه شي کېدای.'),
        ('fig', 'Figure: the crown hanging from a spring balance — 7.84 N in air and 6.86 N in water.', 'شکل: کمانی ترازو سے لٹکا تاج — ہوا میں 7.84 N اور پانی میں 6.86 N۔', 'شکل: له فنري ترازو ځوړند تاج — په هوا کې 7.84 N او په اوبو کې 6.86 N.'),
    ]),
    ('as7.4', ('Assignment 7.4 DENSITY OF ROCK', 'اسائنمنٹ 7.4 چٹان کی کثافت', '7.4 دنده د ډبرې کثافت'), [
        ('p', 'A geologist finds that a Moon rock whose weight is 90.9 N has an apparent weight of 60.6 N when submerged in water. What is the density of the rock?', 'ایک ماہرِ ارضیات کو معلوم ہوتا ہے کہ چاند کی ایک چٹان جس کا وزن 90.9 N ہے، پانی میں ڈوبنے پر اس کا ظاہری وزن 60.6 N ہے۔ چٹان کی کثافت کیا ہے؟', 'یو ځمکپوه مومي چې د سپوږمۍ یوه ډبره چې وزن یې 90.9 N دی، په اوبو کې د ډوبېدو پر مهال ظاهري وزن یې 60.6 N دی. د ډبرې کثافت څومره دی؟'),
    ]),
    ('act7-oil', ('Activity — WATER AND OIL', 'سرگرمی — پانی اور تیل', 'فعالیت — اوبه او تېل'), [
        ('p', 'Pour some water into a clear glass. Then pour in some cooking oil. Which liquid is less dense?', 'ایک صاف گلاس میں کچھ پانی ڈالیں۔ پھر کچھ کھانے کا تیل ڈالیں۔ کون سا مائع کم کثیف ہے؟', 'په یوه روښانه ګیلاس کې یو څه اوبه واچوئ. بیا یو څه د پخلي تېل واچوئ. کومه مایع کمه کثیفه ده؟'),
        ('fig', 'Photograph: cooking oil being poured into a glass of water; the oil floats on top.', 'تصویر: پانی کے گلاس میں کھانے کا تیل ڈالا جا رہا ہے؛ تیل اوپر تیرتا ہے۔', 'انځور: د اوبو ګیلاس ته د پخلي تېل اچول کېږي؛ تېل پورته لامبو وهي.'),
    ]),
]
