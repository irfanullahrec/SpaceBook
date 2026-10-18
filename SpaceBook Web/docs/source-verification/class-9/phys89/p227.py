# -*- coding: utf-8 -*-
TITLE = 'Energy to vaporize water / Table 8.4 latent heats of fusion and vaporization / gallium information / point to ponder'
H = ['Material', 'Melting Point (°C)', 'Latent Heat of fusion (J/kg)', 'Boiling Point (°C)', 'Latent Heat of Vaporization (J/kg)']
R = [['Helium', '-269.65', '5.23 × 10³', '-269', '2.09 × 10⁴'], ['Oxygen', '-218.79', '1.38 × 10⁴', '-183', '2.13 × 10⁵'],
     ['Water', '0', '3.33 × 10⁵', '100', '2.26 × 10⁶'], ['Mercury', '-39', '1.13 × 10⁴', '357', '2.93 × 10⁵'],
     ['Sulphur', '119', '3.81 × 10⁴', '445', '3.26 × 10⁵'], ['Lead', '327', '2.45 × 10⁴', '1750', '8.70 × 10⁵'],
     ['Aluminum', '660', '3.97 × 10⁵', '2450', '1.14 × 10⁷'], ['Copper', '1083', '1.34 × 10⁵', '1187', '5.06 × 10⁶'],
     ['Silver', '961', '8.82 × 10⁴', '2193', '2.33 × 10⁶'], ['Gold', '1063', '6.44 × 10⁴', '2660', '1.58 × 10⁶']]
NU = ['ہیلیم', 'آکسیجن', 'پانی', 'پارہ', 'گندھک', 'سیسہ', 'ایلومینیم', 'تانبا', 'چاندی', 'سونا']
NP = ['هیلیم', 'اکسیجن', 'اوبه', 'سیماب', 'ګوګړ', 'سرپ', 'المونیم', 'مس', 'سپین زر', 'سره زر']
HU = ['مادہ', 'نقطۂ پگھلاؤ (°C)', 'پگھلاؤ کی مخفی حرارت (J/kg)', 'نقطۂ کھولاؤ (°C)', 'بخارات کی مخفی حرارت (J/kg)']
HP = ['ماده', 'د ویلې کېدو ټکی (°C)', 'د ویلې کېدو پټه تودوخه (J/kg)', 'د ایشېدو ټکی (°C)', 'د بخار کېدو پټه تودوخه (J/kg)']
SECTIONS = [
    ('8.6.3', ('8.6.3 EXPERIMENT FOR ICE - WATER PHASE CHANGE AND TEMPERATURE-TIME GRAPH ON HEATING ICE', '8.6.3 برف-پانی حالت کی تبدیلی کا تجربہ اور برف گرم کرنے پر درجۂ حرارت-وقت گراف', '8.6.3 د یخ-اوبو د حالت بدلون تجربه او د یخ د تودولو د تودوخې-وخت ګراف'), [
        ('p', 'more energy is required to vaporize water; it would take 2260 kJ to change 1 kg of liquid water at the normal boiling point (100 °C at atmospheric pressure) to steam (water vapor). This example shows that the energy for a phase change is enormous compared to energy associated with temperature changes without a phase change.',
         'زیادہ توانائی پانی کو بخار بنانے کے لیے درکار ہے؛ معمول کے نقطۂ کھولاؤ (فضائی دباؤ پر 100 °C) پر 1 kg مائع پانی کو بھاپ بنانے میں 2260 kJ لگیں گے۔ یہ مثال بتاتی ہے کہ حالت کی تبدیلی کی توانائی، حالت بدلے بغیر درجۂ حرارت کی تبدیلی کی توانائی کے مقابلے میں بہت زیادہ ہے۔',
         'ډېره انرژي د اوبو د بخار کولو لپاره پکار ده؛ په عادي ایشېدو ټکي (په اتموسفیري فشار 100 °C) کې د 1 kg مایع اوبو بخار کولو ته 2260 kJ پکار دي. دا بېلګه ښيي چې د حالت بدلون انرژي د حالت له بدلون پرته د تودوخې بدلون په پرتله ډېره لویه ده.'),
        ('p', 'The latent heat of fusion for a given substance is different from the latent heat of vaporization for that substance. Representative values for melting point, latent heat of fusion, boiling point, and latent heat of vaporization are listed in Table 8.4.',
         'کسی مادے کی پگھلاؤ کی مخفی حرارت اس کی بخارات بننے کی مخفی حرارت سے مختلف ہے۔ نقطۂ پگھلاؤ، پگھلاؤ کی مخفی حرارت، نقطۂ کھولاؤ اور بخارات کی مخفی حرارت کی نمائندہ قدریں جدول 8.4 میں ہیں۔',
         'د یوې مادې د ویلې کېدو پټه تودوخه د هماغې مادې د بخار کېدو له پټې تودوخې توپیر لري. د ویلې کېدو ټکي، د ویلې کېدو پټې تودوخې، د ایشېدو ټکي او د بخار کېدو پټې تودوخې نمونه ییز ارزښتونه په 8.4 جدول کې دي.'),
        ('tab', 'phys9-u8-table84', 'TABLE 8.4: LATENT HEATS OF FUSION AND VAPORIZATION', H, R, (HU, [[NU[i]] + r[1:] for i, r in enumerate(R)]), (HP, [[NP[i]] + r[1:] for i, r in enumerate(R)])),
        ('h', 'INFORMATION', 'معلومات', 'معلومات'),
        ('p', 'The element gallium has a heat of fusion of only 80 kJ kg^{-1} and a melting of 30 °C hence it melts when ever placed on palm.', 'عنصر گیلیم کی پگھلاؤ کی حرارت صرف 80 kJ kg^{-1} اور نقطۂ پگھلاؤ 30 °C ہے، اس لیے ہتھیلی پر رکھتے ہی پگھل جاتا ہے۔', 'ګالیم عنصر یوازې 80 kJ kg^{-1} د ویلې کېدو تودوخه او 30 °C د ویلې کېدو ټکی لري، نو کله چې پر ورغوي کېښودل شي ویلې کېږي.'),
        ('h', 'POINT TO PONDER', 'غور طلب نکتہ', 'د فکر ټکی'),
        ('p', 'Why is a scald from steam often more serious than one from boiling water? Steam at 100 °C contains more thermal energy than water. The difference is due to the latent heat of vaporization, which for water is quite high. As the steam touches the skin and condenses, a large amount of energy is released, causing more severe burns.',
         'بھاپ سے جلنا اکثر ابلتے پانی سے جلنے سے زیادہ سنگین کیوں ہوتا ہے؟ 100 °C کی بھاپ میں پانی سے زیادہ حرارتی توانائی ہوتی ہے۔ یہ فرق بخارات بننے کی مخفی حرارت کی وجہ سے ہے جو پانی کی کافی زیادہ ہے۔ بھاپ جلد کو چھو کر تکثیف ہوتی ہے تو بہت زیادہ توانائی خارج ہوتی ہے جس سے زیادہ شدید جلن ہوتی ہے۔',
         'ولې د بخار سوځېدنه ډېری وخت د ایشېدونکو اوبو تر سوځېدنې ډېره جدي وي؟ د 100 °C بخار تر اوبو ډېره تودوخیزه انرژي لري. توپیر د بخار کېدو د پټې تودوخې له امله دی چې د اوبو لپاره ډېره لوړه ده. کله چې بخار پوستکي ته ورسېږي او تکاثف وکړي، ډېره انرژي خوشې کېږي او سخته سوځېدنه رامنځته کوي.'),
        ('p', 'Editorial note: Table 8.4 prints several values as "× × 10ⁿ"; the duplicated multiplication sign is removed. The copper boiling point is reproduced as printed (1187 °C).', 'ادارتی نوٹ: جدول 8.4 میں کئی قدریں "× × 10ⁿ" چھپی ہیں؛ دہرا ضرب کا نشان ہٹا دیا گیا۔ تانبے کا نقطۂ کھولاؤ کتاب کے مطابق (1187 °C) رکھا گیا۔', 'سمونیز یادښت: په 8.4 جدول کې ځینې ارزښتونه "× × 10ⁿ" چاپ شوي؛ تکرار شوې ضرب نښه لرې شوه. د مسو د ایشېدو ټکی لکه چاپ شوی (1187 °C) ساتل شوی.'),
    ], True),
]
EXTRA = dict(tables=[dict(id='phys9-u8-table84', sourceNumber='Table 8.4', title='TABLE 8.4: LATENT HEATS OF FUSION AND VAPORIZATION', headers=H, rows=R)])
