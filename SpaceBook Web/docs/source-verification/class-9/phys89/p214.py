# -*- coding: utf-8 -*-
TITLE = 'γ = 3α (eq 8.12) / Table 8.2 thermal expansion coefficients / derivation of γ = 3α'
H = ['Material', 'Coefficient of linear expansion α (°C⁻¹ or K⁻¹)', 'Coefficient of volume expansion γ (°C⁻¹ or K⁻¹)']
R = [['Solids', '', ''], ['Aluminum', '25 × 10⁻⁶', '75 × 10⁻⁶'], ['Brass', '19 × 10⁻⁶', '57 × 10⁻⁶'], ['Copper', '17 × 10⁻⁶', '51 × 10⁻⁶'],
     ['Iron or Steel', '12 × 10⁻⁶', '35 × 10⁻⁶'], ['Lead', '29 × 10⁻⁶', '87 × 10⁻⁶'], ['Concrete, Brick', '12 × 10⁻⁶', '36 × 10⁻⁶'],
     ['Fluids', '', ''], ['Ethyl alcohol', '-', '1100 × 10⁻⁶'], ['Petrol', '-', '950 × 10⁻⁶'], ['Mercury', '-', '180 × 10⁻⁶'],
     ['Water', '-', '210 × 10⁻⁶'], ['Air and most other gases at atmospheric pressure', '-', '3400 × 10⁻⁶']]
HU = ['مادہ', 'طولی پھیلاؤ کا عددی سر α (°C⁻¹ یا K⁻¹)', 'حجمی پھیلاؤ کا عددی سر γ (°C⁻¹ یا K⁻¹)']
NU = ['ٹھوس', 'ایلومینیم', 'پیتل', 'تانبا', 'لوہا یا فولاد', 'سیسہ', 'کنکریٹ، اینٹ', 'سیال', 'ایتھائل الکحل', 'پٹرول', 'پارہ', 'پانی', 'ہوا اور زیادہ تر گیسیں فضائی دباؤ پر']
HP = ['ماده', 'د اوږدیز پراخوالي ضریب α (°C⁻¹ یا K⁻¹)', 'د حجمي پراخوالي ضریب γ (°C⁻¹ یا K⁻¹)']
NP = ['جامدات', 'المونیم', 'پیتل', 'مس', 'اوسپنه یا فولاد', 'سرپ', 'کانکرېټ، خښته', 'مایعات', 'ایتایل الکول', 'پټرول', 'سیماب', 'اوبه', 'هوا او ډېری ګازونه په اتموسفیري فشار']
SECTIONS = [
    ('8.4.1', ('8.4.1 THERMAL EXPANSION OF SOLIDS', '8.4.1 ٹھوس اجسام کا حرارتی پھیلاؤ', '8.4.1 د جامدو تودوخیز پراخوالی'), [
        ('p', 'the coefficient of linear thermal expansion α of solids', 'ٹھوس اجسام کے طولی حرارتی پھیلاؤ کے عددی سر α کا', 'د جامدو د اوږدیز تودوخیز پراخوالي د ضریب α'),
        ('eq', 'phys9-u8-eq812', 'γ = 3α', '8.12'),
        ('p', 'The values of coefficients of volume thermal expansion γ for different substances are given in the table 8.2, which is approximately three times the coefficient of linear thermal expansion α.',
         'مختلف مادوں کے حجمی حرارتی پھیلاؤ کے عددی سر γ کی قدریں جدول 8.2 میں دی گئی ہیں جو طولی حرارتی پھیلاؤ کے عددی سر α کا تقریباً تین گنا ہیں۔',
         'د بېلابېلو موادو د حجمي تودوخیز پراخوالي ضریب γ ارزښتونه په 8.2 جدول کې دي چې د اوږدیز تودوخیز پراخوالي د ضریب α شاوخوا درې چنده دي.'),
        ('tab', 'phys9-u8-table82', 'TABLE 8.2: THERMAL EXPANSION COEFFICIENTS AT 20 °C', H, R,
         (HU, [[NU[i]] + r[1:] for i, r in enumerate(R)]), (HP, [[NP[i]] + r[1:] for i, r in enumerate(R)])),
        ('p', 'To see how this relationship comes about, suppose that the solid has the shape of a cube of side L. The increment in the length of each side is ΔL, and treating this as a small (infinitesimal) quantity, the increment in the volume L^3 is',
         'یہ تعلق کیسے بنتا ہے، یہ دیکھنے کے لیے فرض کریں کہ ٹھوس L ضلع والا مکعب ہے۔ ہر ضلع کی لمبائی میں اضافہ ΔL ہے اور اسے بہت چھوٹی (لامتناہی چھوٹی) مقدار مان کر حجم L^3 میں اضافہ یہ ہے',
         'د دې لپاره چې وګورو دا اړیکه څنګه جوړېږي، فرض کړئ جامد د L ضلع لرونکی مکعب دی. د هرې ضلعې د اوږدوالي زیاتوالی ΔL دی او دا ډېر کوچنی کمیت ګڼلو سره د حجم L^3 زیاتوالی دا دی'),
        ('eq', 'phys9-u8-g3a-1', 'ΔV = Δ(L)^3 = 3L^2 ΔL'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', 'phys9-u8-g3a-2', 'ΔV = 3L^2 × α L ΔT'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', 'phys9-u8-g3a-3', 'ΔV = 3α L^3 ΔT'),
        ('p', 'therefore', 'لہٰذا', 'نو'),
        ('eq', 'phys9-u8-g3a-4', 'ΔV = 3α V ΔT'),
        ('p', 'Comparing this result for ΔV with Equation 8.9, we see that γ = 3α.', 'ΔV کے اس نتیجے کا مساوات 8.9 سے موازنہ کرنے پر γ = 3α ملتا ہے۔', 'د ΔV دا پایله له 8.9 معادلې سره په پرتله کولو ګورو چې γ = 3α.'),
    ], True),
]
EXTRA = dict(tables=[dict(id='phys9-u8-table82', sourceNumber='Table 8.2', title='TABLE 8.2: THERMAL EXPANSION COEFFICIENTS AT 20 °C', headers=H, rows=R)],
             formulaSourceLinks=[dict(name='Relation between γ and α', blockIds=['phys9-u8-eq812'])])
