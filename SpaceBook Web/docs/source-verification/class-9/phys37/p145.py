# -*- coding: utf-8 -*-
TITLE = 'Example 5.4 meteoroid / Extension Exercise 5.1 / Assignment 5.4 / Table 5.1 g with altitude / point to ponder'
_R = [['0.0', '9.8', 'Mean Earth radius'], ['8.8', '9.8', 'Mt. Everest'], ['36.6', '9.7', 'Highest manned balloon'], ['400', '8.7', 'Space shuttle orbit'], ['35 700', '0.2', 'Communications satellite']]
SECTIONS = [
    ('ex5.4', ('Example 5.4 METEOROID IN EARTH’S FIELD', 'مثال 5.4 زمین کے میدان میں شہابیہ', '5.4 مثال د ځمکې په ساحه کې شهاب'), [
        ('p', 'A meteoroid (a chunk of rock) is at 4.4 × 10^7 m from the earth, what is the value of free fall acceleration ‘g’ at this point due to earth?', 'ایک شہابیہ (چٹان کا ٹکڑا) زمین سے 4.4 × 10^7 m پر ہے؛ اس نقطے پر زمین کی وجہ سے آزادانہ گرنے کے اسراع \'g\' کی قدر کیا ہے؟', 'یو شهاب (د ډبرې ټوټه) له ځمکې 4.4 × 10^7 m لرې دی؛ په دې ټکي کې د ځمکې له امله د آزاد سقوط تعجیل \'g\' څومره دی؟'),
        ('h', 'SOLUTION — GIVEN:', 'حل — معلوم:', 'حل — ورکړل شوي:'),
        ('ul', [('Radius of earth r_E = 6.4 × 10^6 m', 'زمین کا نصف قطر r_E = 6.4 × 10^6 m', 'د ځمکې شعاع r_E = 6.4 × 10^6 m'), ('Acceleration due to gravity g = 9.8 ms^{-2}', 'کششِ ثقل کا اسراع g = 9.8 ms^{-2}', 'د جاذبې تعجیل g = 9.8 ms^{-2}'), ('height h = 4.4 × 10^7 m = 44 × 10^6 m', 'بلندی h = 4.4 × 10^7 m = 44 × 10^6 m', 'لوړوالی h = 4.4 × 10^7 m = 44 × 10^6 m')]),
        ('h', 'REQUIRED:', 'مطلوب:', 'غوښتل شوي:'),
        ('p', 'free-fall acceleration at height g_h = ?', 'بلندی پر آزادانہ گرنے کا اسراع g_h = ?', 'په لوړوالي کې د آزاد سقوط تعجیل g_h = ?'),
        ('p', 'The value of ‘g_h’ at height h, can be calculated by using equation 5.5', 'بلندی h پر \'g_h\' کی قدر مساوات 5.5 استعمال کر کے معلوم کی جا سکتی ہے', 'په h لوړوالي کې د \'g_h\' ارزښت د 5.5 معادلې په کارولو محاسبه کېدای شي'),
        ('eq', None, 'g_h = [[g r_E^2|(r_E + h)^2]]'),
        ('p', 'putting values', 'قدریں رکھنے سے', 'د ارزښتونو په ایښودلو'),
        ('eq', None, 'g_h = [[9.8 ms^{-2} × (6.4 × 10^6 m)^2|(6.4 × 10^6 m + 44 × 10^6 m)^2]]'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', None, 'g_h = [[9.8 ms^{-2} × (6.4 × 10^6 m)^2|(50.4 × 10^6 m)^2]]'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', None, 'g_h = [[9.8 ms^{-2} × 4.1 × 10^{13} m^2|2.54 × 10^{15} m^2]]'),
        ('p', 'therefore', 'لہٰذا', 'نو'),
        ('eq', None, 'g_h = 0.16 ms^{-2}   Answer'),
        ('h', 'EXTENSION EXERCISE 5.1', 'توسیعی مشق 5.1', '5.1 پراخه تمرین'),
        ('p', 'Confirm the value of ‘g’ for Jupiter given in Example 5.2, Using equation 5.5', 'مثال 5.2 میں دی گئی مشتری کے لیے \'g\' کی قدر کی مساوات 5.5 سے تصدیق کریں۔', 'په 5.2 مثال کې د مشتري لپاره ورکړل شوی د \'g\' ارزښت د 5.5 معادلې په کارولو تایید کړئ.'),
    ]),
    ('as5.4', ('Assignment 5.4 Value Of g At Specific Height', 'اسائنمنٹ 5.4 مخصوص بلندی پر g کی قدر', '5.4 دنده په ټاکلي لوړوالي کې د g ارزښت'), [
        ('p', 'Calculate the value of g at 1000 km and 35900 km above the earth surface.', 'زمین کی سطح سے 1000 km اور 35900 km بلندی پر g کی قدر معلوم کریں۔', 'د ځمکې له سطحې 1000 km او 35900 km لوړوالي کې د g ارزښت محاسبه کړئ.'),
        ('tab', 'phys9-u5-table51b', 'TABLE 5.1: CHANGE IN GRAVITATIONAL ACCELERATION WITH ALTITUDE [printed number; a second Table 5.1]', ['Altitude (km)', 'a (m/s²)', 'Altitude Example'], _R,
         (['بلندی (km)', 'a (m/s²)', 'بلندی کی مثال'], [[r[0], r[1], u] for r, u in zip(_R, ['زمین کا اوسط نصف قطر', 'ماؤنٹ ایورسٹ', 'سب سے اونچا انسان بردار غبارہ', 'خلائی شٹل کا مدار', 'مواصلاتی سیٹلائٹ'])]),
         (['لوړوالی (km)', 'a (m/s²)', 'د لوړوالي مثال'], [[r[0], r[1], u] for r, u in zip(_R, ['د ځمکې منځنۍ شعاع', 'د ایورسټ غر', 'تر ټولو لوړ انسان لرونکی بالون', 'د فضايي شټل مدار', 'مخابراتي سپوږمکۍ'])])),
        ('h', 'POINT TO PONDER', 'غور طلب نکتہ', 'د فکر ټکی'),
        ('p', 'The magnitude of g on the moon’s surface is about 1/6 of the value of g on Earth’s surface. Can you infer from this relationship that the moon’s mass is 1/6 of Earth’s mass? Why or why not?', 'چاند کی سطح پر g کی مقدار زمین کی سطح پر g کی قدر کا تقریباً 1/6 ہے۔ کیا آپ اس تعلق سے یہ نتیجہ نکال سکتے ہیں کہ چاند کی کمیت زمین کی کمیت کا 1/6 ہے؟ کیوں یا کیوں نہیں؟', 'د سپوږمۍ پر سطحه د g اندازه د ځمکې پر سطحه د g د ارزښت شاوخوا 1/6 ده. ایا له دې اړیکې پایله اخیستلی شئ چې د سپوږمۍ کتله د ځمکې د کتلې 1/6 ده؟ ولې یا ولې نه؟'),
    ]),
]
