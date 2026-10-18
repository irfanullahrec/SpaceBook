# -*- coding: utf-8 -*-
TITLE = 'Unit 8 exercise: multiple choice questions'
ORIGIN = 'SpaceBook answer key (the textbook answer key covers assignments and numerical problems only)'
M = [
    ('The S.I. unit of heat is', 'حرارت کی SI اکائی ہے', 'د تودوخې SI واحد دی', ['J', 'kg', 'K⁻¹', 'K'], 0, 'Heat is energy transferred; its SI unit is the joule (p.200).'),
    ('The S.I. unit of temperature is', 'درجۂ حرارت کی SI اکائی ہے', 'د تودوخې د درجې SI واحد دی', ['°C', '°F', 'J', 'K'], 3, 'Kelvin scale is adopted in SI (p.203).'),
    ('The Fahrenheit and Celsius scale reading of temperature coincide at', 'فارن ہائیٹ اور سیلسیس پیمانے کی ریڈنگ کس درجۂ حرارت پر برابر ہوتی ہے', 'د فارنهایټ او سېلسیس پیمانو لوستنه په کومه تودوخه کې یو شان کېږي', ['0°', '−460°', '−273°', '−40°'], 3, 'T°F = 9/5 T°C + 32 gives T = −40 when both readings are equal.'),
    ('310 K in centigrade scale is', '310 K سینٹی گریڈ پیمانے پر ہے', '310 K په سانتي ګرېډ پیمانه کې دی', ['37 °C', '310 °C', '63 °C', '273 °C'], 0, 'T°C = T_K − 273 = 310 − 273 = 37 °C.'),
    ('When water at 0 °C is heated, it contracts till temperature reaches', '0 °C کا پانی گرم کرنے پر کس درجۂ حرارت تک سکڑتا ہے', 'کله چې 0 °C اوبه تودې شي، تر کومې تودوخې کوچنۍ کېږي', ['1 °C', '4 °C', '100 °C', '100 K'], 1, 'Anomalous expansion: volume decreases up to 4 °C (p.212-213).'),
    ('The S.I. unit of specific heat is', 'مخصوص حرارت کی SI اکائی ہے', 'د ځانګړې تودوخې SI واحد دی', ['J K⁻¹', 'J K⁻¹ kg⁻¹', 'J kg⁻¹', 'J K kg'], 1, 'c = ΔQ/(m ΔT): J kg⁻¹ K⁻¹ (p.217).'),
    ('The relation between coefficient of linear and volume expansion is;', 'طولی اور حجمی پھیلاؤ کے عددی سروں کا تعلق ہے', 'د اوږدیز او حجمي پراخوالي د ضریبونو اړیکه ده', ['α = 3γ', 'γ = 3α', 'γ = α/2', 'γ = 6α'], 1, 'Equation 8.12: γ = 3α.'),
    ('The S.I. unit of Latent heat is', 'مخفی حرارت کی SI اکائی ہے', 'د پټې تودوخې SI واحد دی', ['J K⁻¹', 'J kg⁻¹', 'J K kg⁻¹', 'J K kg'], 1, 'L = ΔQ/m: J kg⁻¹ (p.219-220).'),
    ('How much heat is required to melt of 1 kg of Zinc at its boiling temperature 240 °C with latent heat of 113 × 10³ J kg⁻¹', '1 kg زنک کو 240 °C پر (کتاب میں "نقطۂ کھولاؤ") پگھلانے کے لیے کتنی حرارت درکار ہے جبکہ مخفی حرارت 113 × 10³ J kg⁻¹ ہو', 'د 1 kg جستو د ویلې کولو لپاره په 240 °C کې (په کتاب کې "د ایشېدو ټکی") څومره تودوخه پکار ده که پټه تودوخه 113 × 10³ J kg⁻¹ وي', ['113 × 10³ J', '1.13 × 10³ J', '2.4 × 10⁵ J', '2.71 × 10⁷ J'], 0, 'ΔQ = m L_f = 1 × 113 × 10³ J. (The question prints "boiling temperature"; melting is meant.)'),
    ('The amount of heat required to raise the temperature of 1 kg of water by 1 K is', '1 kg پانی کا درجۂ حرارت 1 K بڑھانے کے لیے درکار حرارت ہے', 'د 1 kg اوبو د تودوخې 1 K لوړولو اړینه تودوخه ده', ['1 J', '400 J', '310 J', '4190 J'], 3, 'Specific heat of water 4190 J kg⁻¹ K⁻¹ (p.217).'),
]
L = 'ABCD'
ITEMS = [('h', 'EXERCISE', 'مشق', 'تمرین'), ('h', 'MULTIPLE CHOICE QUESTIONS — Choose the best possible answer:', 'کثیر الانتخابی سوالات — بہترین جواب منتخب کریں:', 'څو ځوابیزې پوښتنې — غوره ځواب وټاکئ:')]
for i, (q, u, p, o, a, e) in enumerate(M, 1):
    opts = '   '.join(f'{L[k]}. {x}' for k, x in enumerate(o))
    ITEMS.append(('p', f'{i}. {q}  {opts}', f'{i}. {u}  {opts}', f'{i}. {p}  {opts}'))
SECTIONS = [('source-u8-exercise-mcqs', ('EXERCISE — MULTIPLE CHOICE QUESTIONS', 'مشق — کثیر الانتخابی سوالات', 'تمرین — څو ځوابیزې پوښتنې'), ITEMS)]
EXTRA = dict(textbookExercise=dict(mcqs=[dict(num=i, q=q, urdu=u, pashto=p, opts=o, optsUrdu=o, optsPashto=o, ans=a, exp=f'SpaceBook answer: ({L[a]}) {o[a]}. {e}',
                                              answerOrigin=ORIGIN, answerProvidedInSource=False) for i, (q, u, p, o, a, e) in enumerate(M, 1)]))
