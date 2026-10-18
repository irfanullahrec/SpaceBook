# -*- coding: utf-8 -*-
TITLE = 'Mass of Earth calculation / tip N kg⁻¹ = m s⁻² / Example 5.2 mass of Jupiter / Assignment 5.2'
SECTIONS = [
    ('5.2-calc', ('5.2 Mass of Earth (continued)', '5.2 زمین کی کمیت (جاری)', '5.2 د ځمکې کتله (دوام)'), [
        ('eq', None, 'm_E = [[9.8 Nkg^{-1} (6.4 × 10^6 m)^2|6.67 × 10^{-11} Nm^2 kg^{-2}]]'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', None, 'm_E = [[9.8 Nkg^{-1} × 4.1 × 10^{13} m^2|6.67 × 10^{-11} Nm^2 kg^{-2}]]'),
        ('p', 'therefore', 'لہٰذا', 'نو'),
        ('eq', None, 'm_E = 6 × 10^{24} kg'),
        ('p', 'Thus the mass of earth is approximately 6 × 10^{24} kg. This means that if we know acceleration due to gravity ‘g’ and radius ‘r’ of any planet or star we can calculate its mass.', 'چنانچہ زمین کی کمیت تقریباً 6 × 10^{24} kg ہے۔ اس کا مطلب ہے کہ اگر ہم کسی سیارے یا ستارے کا کششِ ثقل کا اسراع \'g\' اور نصف قطر \'r\' جانتے ہوں تو اس کی کمیت معلوم کر سکتے ہیں۔', 'نو د ځمکې کتله نږدې 6 × 10^{24} kg ده. دا پدې مانا چې که د هرې سیارې یا ستوري د جاذبې تعجیل \'g\' او شعاع \'r\' وپېژنو، کتله یې محاسبه کولی شو.'),
        ('h', 'TIP — Nkg^{-1} = ms^{-2}', 'نکتہ — Nkg^{-1} = ms^{-2}', 'لارښوونه — Nkg^{-1} = ms^{-2}'),
        ('p', 'Since N = kg ms^{-2}. Dividing both sides by kg: N/kg = ms^{-2} or N kg^{-1} = ms^{-2}', 'چونکہ N = kg ms^{-2}۔ دونوں طرف kg سے تقسیم کرنے پر: N/kg = ms^{-2} یا N kg^{-1} = ms^{-2}', 'څرنګه چې N = kg ms^{-2}. دواړه خواوې پر kg وېشلو سره: N/kg = ms^{-2} یا N kg^{-1} = ms^{-2}'),
    ]),
    ('ex5.2', ('Example 5.2 MASS OF JUPITER', 'مثال 5.2 مشتری کی کمیت', '5.2 مثال د مشتري کتله'), [
        ('p', 'Jupiter is the largest planet in the solar system. Radius of Jupiter is r_J = 7.15 × 10^7 m, the acceleration due to gravity on Jupiter is 24.7 N/kg. Calculate the mass of Jupiter.', 'مشتری نظامِ شمسی کا سب سے بڑا سیارہ ہے۔ مشتری کا نصف قطر r_J = 7.15 × 10^7 m ہے اور مشتری پر کششِ ثقل کا اسراع 24.7 N/kg ہے۔ مشتری کی کمیت معلوم کریں۔', 'مشتري د لمریز نظام تر ټولو لویه سیاره ده. د مشتري شعاع r_J = 7.15 × 10^7 m او پر مشتري د جاذبې تعجیل 24.7 N/kg دی. د مشتري کتله محاسبه کړئ.'),
        ('fig', 'Photograph: the planet Jupiter.', 'تصویر: سیارہ مشتری۔', 'انځور: مشتري سیاره.'),
        ('h', 'SOLUTION — GIVEN:', 'حل — معلوم:', 'حل — ورکړل شوي:'),
        ('ul', [('Radius of Jupiter r_J = 7.15 × 10^7 m', 'مشتری کا نصف قطر r_J = 7.15 × 10^7 m', 'د مشتري شعاع r_J = 7.15 × 10^7 m'), ('Acceleration due to gravity at Jupiter g_J = 24.7 N/kg', 'مشتری پر کششِ ثقل کا اسراع g_J = 24.7 N/kg', 'پر مشتري د جاذبې تعجیل g_J = 24.7 N/kg'), ('Gravitational Constant G = 6.673 × 10^{-11} Nm^2kg^{-2}', 'تجاذبی مستقل G = 6.673 × 10^{-11} Nm^2kg^{-2}', 'د جاذبې ثابت G = 6.673 × 10^{-11} Nm^2kg^{-2}')]),
        ('h', 'REQUIRED:', 'مطلوب:', 'غوښتل شوي:'),
        ('p', 'Mass of Jupiter m_J = ?', 'مشتری کی کمیت m_J = ?', 'د مشتري کتله m_J = ?'),
        ('p', 'The mass of a planet or star can be calculated by using equation 4.4 [printed; equation 5.3]', 'کسی سیارے یا ستارے کی کمیت مساوات 4.4 [کتاب میں یوں چھپا ہے؛ مراد مساوات 5.3] سے معلوم کی جا سکتی ہے', 'د سیارې یا ستوري کتله د 4.4 معادلې [په کتاب کې چاپ شوی؛ مطلب 5.3 معادله] په کارولو محاسبه کېدای شي'),
        ('eq', None, 'm_J = [[g_J r_J^2|G]]'),
        ('p', 'putting values', 'قدریں رکھنے سے', 'د ارزښتونو په ایښودلو'),
        ('eq', None, 'm_J = [[24.7 N/kg × (7.15 × 10^7 m)^2|6.673 × 10^{-11} Nm^2kg^{-2}]]'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', None, 'm_J = [[24.7 Nkg^{-1} × 5.11 × 10^{15} m^2|6.673 × 10^{-11} Nm^2kg^{-2}]]'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', None, 'm_J = 1.891 × 10^{16+11} kg'),
        ('p', 'therefore', 'لہٰذا', 'نو'),
        ('eq', None, 'm_J = 1.89 × 10^{27} kg   Answer'),
        ('p', 'Thus the mass of Jupiter is about 300 times the mass of the earth.', 'چنانچہ مشتری کی کمیت زمین کی کمیت سے تقریباً 300 گنا ہے۔', 'نو د مشتري کتله د ځمکې د کتلې شاوخوا 300 چنده ده.'),
    ]),
    ('as5.2', ('Assignment 5.2 MASS OF MOON', 'اسائنمنٹ 5.2 چاند کی کمیت', '5.2 دنده د سپوږمۍ کتله'), [
        ('p', 'If the radius of the moon is 1.74 × 10^6 m and have acceleration due to gravity on its surface as 1.6 ms^{-2}. Calculate the mass of moon.', 'اگر چاند کا نصف قطر 1.74 × 10^6 m ہو اور اس کی سطح پر کششِ ثقل کا اسراع 1.6 ms^{-2} ہو تو چاند کی کمیت معلوم کریں۔', 'که د سپوږمۍ شعاع 1.74 × 10^6 m وي او پر سطحه یې د جاذبې تعجیل 1.6 ms^{-2} وي، د سپوږمۍ کتله محاسبه کړئ.'),
    ]),
]
