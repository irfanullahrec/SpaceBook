# -*- coding: utf-8 -*-
TITLE = 'Geostationary satellite speed / Example 5.5 Earth around Sun / Assignment 5.5'
SECTIONS = [
    ('5.5-geo', ('Geostationary satellites', 'جیو اسٹیشنری سیٹلائٹ', 'جیوسټېشنري سپوږمکۍ'), [
        ('p', 'Geostationary communications satellites are placed in a circular orbit that is 3.59 × 10^7 m = 35.9 × 10^6 m above the surface of the earth. Their orbital speed can be calculated by equation 5.6 as', 'جیو اسٹیشنری مواصلاتی سیٹلائٹ زمین کی سطح سے 3.59 × 10^7 m = 35.9 × 10^6 m اوپر دائروی مدار میں رکھے جاتے ہیں۔ ان کی مداری رفتار مساوات 5.6 سے یوں معلوم کی جا سکتی ہے', 'جیوسټېشنري مخابراتي سپوږمکۍ د ځمکې له سطحې 3.59 × 10^7 m = 35.9 × 10^6 m پورته په دایروي مدار کې اچول کېږي. مداري سرعت یې د 5.6 معادلې په واسطه داسې محاسبه کېږي'),
        ('eq', None, 'v = √([[G m_E|r_E + h]])'),
        ('p', 'putting values', 'قدریں رکھنے سے', 'د ارزښتونو په ایښودلو'),
        ('eq', None, 'v = √(6.673 × 10^{-11} Nm^2kg^{-2} [[6 × 10^{24} kg|(35.9 + 6.4) × 10^6 m]])'),
        ('p', 'therefore', 'لہٰذا', 'نو'),
        ('eq', None, 'v = 3.07 × 10^3 ms^{-1}   or   v = 3.07 kms^{-1}'),
        ('p', 'This equation can also be used to measure the velocity of any planet or celestial object moving in a circular path.', 'یہ مساوات دائروی راستے پر حرکت کرنے والے کسی بھی سیارے یا فلکی جسم کی رفتار معلوم کرنے کے لیے بھی استعمال ہو سکتی ہے۔', 'دا معادله په دایروي لار د هرې خوځېدونکې سیارې یا اسماني جسم د سرعت د اندازه کولو لپاره هم کارول کېدای شي.'),
    ]),
    ('ex5.5', ('Example 5.5 SPEED OF EARTH AROUND SUN', 'مثال 5.5 سورج کے گرد زمین کی رفتار', '5.5 مثال د لمر شاوخوا د ځمکې سرعت'), [
        ('p', 'The mass of the Sun is 1.99 × 10^{30} kg, and the radius of the Earth’s orbit around the Sun is 1.5 × 10^{11} m. From this, calculate the orbital speed of the Earth.', 'سورج کی کمیت 1.99 × 10^{30} kg ہے اور سورج کے گرد زمین کے مدار کا نصف قطر 1.5 × 10^{11} m ہے۔ اس سے زمین کی مداری رفتار معلوم کریں۔', 'د لمر کتله 1.99 × 10^{30} kg او د لمر شاوخوا د ځمکې د مدار شعاع 1.5 × 10^{11} m ده. له دې څخه د ځمکې مداري سرعت محاسبه کړئ.'),
        ('h', 'SOLUTION — GIVEN:', 'حل — معلوم:', 'حل — ورکړل شوي:'),
        ('ul', [('Radius r = 1.5 × 10^{11} m', 'نصف قطر r = 1.5 × 10^{11} m', 'شعاع r = 1.5 × 10^{11} m'), ('Mass of Sun m_s = 1.99 × 10^{30} kg', 'سورج کی کمیت m_s = 1.99 × 10^{30} kg', 'د لمر کتله m_s = 1.99 × 10^{30} kg'), ('Gravitational Constant G = 6.673 × 10^{-11} Nm^2kg^{-2}', 'تجاذبی مستقل G = 6.673 × 10^{-11} Nm^2kg^{-2}', 'د جاذبې ثابت G = 6.673 × 10^{-11} Nm^2kg^{-2}')]),
        ('h', 'REQUIRED:', 'مطلوب:', 'غوښتل شوي:'),
        ('p', 'Orbital Speed v = ?', 'مداری رفتار v = ?', 'مداري سرعت v = ?'),
        ('p', 'the orbital speed is', 'مداری رفتار ہے', 'مداري سرعت دی'),
        ('eq', None, 'v = √(G [[m_s|r]])'),
        ('p', 'putting values', 'قدریں رکھنے سے', 'د ارزښتونو په ایښودلو'),
        ('eq', None, 'v = √(6.673 × 10^{-11} Nm^2kg^{-2} [[1.99 × 10^{30} kg|1.5 × 10^{11} m]])'),
        ('p', 'therefore', 'لہٰذا', 'نو'),
        ('eq', None, 'v = 3.0 × 10^4 m/s = 30 km/s   Answer'),
    ]),
    ('as5.5', ('Assignment 5.5 ORBITAL SPEED OF A SATELLITE', 'اسائنمنٹ 5.5 سیٹلائٹ کی مداری رفتار', '5.5 دنده د سپوږمکۍ مداري سرعت'), [
        ('p', 'If a satellite orbits the earth at 2,000 km above sea level, how fast must the orbiting satellite travel to maintain a circular orbit?', 'اگر کوئی سیٹلائٹ سطحِ سمندر سے 2,000 km اوپر زمین کے گرد گھومے تو دائروی مدار برقرار رکھنے کے لیے اسے کتنی تیزی سے چلنا چاہیے؟', 'که یوه سپوږمکۍ د سمندر له سطحې 2,000 km پورته د ځمکې شاوخوا وګرځي، د دایروي مدار د ساتلو لپاره باید څومره چټکه وخوځېږي؟'),
    ]),
]
