# -*- coding: utf-8 -*-
TITLE = 'Thermal conductivity k (equation 9.2), definition and units / Table 9.1 (continued) / Example 9.1 Styrofoam ice box begins'
from p243 import H, R2, U2, P2, HU, HP
SECTIONS = [
    ('9.2', ('9.2 THERMAL CONDUCTIVITY', '9.2 حرارتی ایصالیت', '9.2 تودوخیز هدایت'), [
        ('p', 'Where k is the thermal conductivity of the material of the bar. Thermal conductivity depends on the nature of the material. Such that', 'جہاں k سلاخ کے مادے کی حرارتی ایصالیت ہے۔ حرارتی ایصالیت مادے کی نوعیت پر منحصر ہے، کہ', 'چېرې چې k د میلې د مادې تودوخیز هدایت دی. تودوخیز هدایت د مادې په طبیعت پورې اړه لري، داسې چې'),
        ('eq', 'phys9-u9-eq92', 'k = [[Q × L|A × t × (T_h − T_c)]]', '9.2'),
        ('p', 'As a special case, if L = 1 m, A = 1 m^2, T_h − T_c = 1 °C or 1 K and t = 1 s, then from Equation 9.2 we obtain k = Q. Thus the thermal conductivity k of a substance is defined as', 'خاص صورت میں اگر L = 1 m، A = 1 m^2، T_h − T_c = 1 °C یا 1 K اور t = 1 s ہو تو مساوات 9.2 سے k = Q ملتا ہے۔ یوں کسی مادے کی حرارتی ایصالیت k کی تعریف یہ ہے', 'په ځانګړي حالت کې که L = 1 m، A = 1 m^2، T_h − T_c = 1 °C یا 1 K او t = 1 s وي، له 9.2 معادلې k = Q لاسته راځي. نو د یوې مادې تودوخیز هدایت k داسې تعریفېږي'),
        ('q', 'the quantity of heat which flows through one square metre of area of the substance in one second when a temperature difference of one kelvin is maintained across a thickness of one meter.', 'حرارت کی وہ مقدار جو ایک سیکنڈ میں مادے کے ایک مربع میٹر رقبے سے گزرتی ہے جب ایک میٹر موٹائی کے آر پار ایک کیلون کا درجۂ حرارت کا فرق قائم رکھا جائے۔', 'د تودوخې هغه اندازه چې په یوه ثانیه کې د مادې له یو مربع متر مساحت تېرېږي کله چې د یو متر ضخامت په اوږدو د یو کېلوین د تودوخې توپیر وساتل شي.'),
        ('p', 'The SI units of thermal conductivity are W m^{-1} K^{-1} or J m^{-1} K^{-1} s^{-1}. Some typical values of thermal conductivity are listed in Table 9.1.', 'حرارتی ایصالیت کی SI اکائیاں W m^{-1} K^{-1} یا J m^{-1} K^{-1} s^{-1} ہیں۔ کچھ عام قدریں جدول 9.1 میں ہیں۔', 'د تودوخیز هدایت SI واحدونه W m^{-1} K^{-1} یا J m^{-1} K^{-1} s^{-1} دي. ځینې عام ارزښتونه په 9.1 جدول کې دي.'),
        ('tab', 'phys9-u9-table91b', 'TABLE 9.1 (continued)', H, R2, (HU, [[U2[i], r[1]] for i, r in enumerate(R2)]), (HP, [[P2[i], r[1]] for i, r in enumerate(R2)])),
        ('h', 'Example 9.1 STYROFOAM ICE BOX', 'مثال 9.1 اسٹائروفوم آئس باکس', '9.1 بېلګه د سټایروفوم د یخ صندوق'),
        ('p', 'A Styrofoam (k = 0.010 W/mK) ice box has a total area of 0.950 m^2 and walls with an average thickness of 2.50 cm. The box contains ice, water, and canned beverages at 0 °C. The inside of the box is kept cold by melting ice. What is the rate of energy transfer in J/s if the ice box is kept at 35.0 °C?',
         'اسٹائروفوم (k = 0.010 W/mK) کے آئس باکس کا کل رقبہ 0.950 m^2 اور دیواروں کی اوسط موٹائی 2.50 cm ہے۔ ڈبے میں 0 °C پر برف، پانی اور ڈبہ بند مشروبات ہیں۔ پگھلتی برف ڈبے کو اندر سے ٹھنڈا رکھتی ہے۔ اگر آئس باکس 35.0 °C پر رکھا ہو تو توانائی کی منتقلی کی شرح J/s میں کیا ہے؟',
         'د سټایروفوم (k = 0.010 W/mK) د یخ صندوق ټوله مساحت 0.950 m^2 او د دېوالونو منځنی ضخامت 2.50 cm دی. په صندوق کې په 0 °C یخ، اوبه او قطي مشروبات دي. ویلې کېدونکی یخ صندوق دننه سوړ ساتي. که صندوق په 35.0 °C کې وي، د انرژۍ د لېږد کچه په J/s څومره ده؟'),
        ('p', 'SOLUTION — GIVEN: Area A = 0.950 m^2; Length L = 2.50 cm = 0.0250 m; Temperature difference T_h − T_c = 35 °C − 0 °C = 35 °C = 35 K; thermal conductivity of Styrofoam k = 0.010 W m^{-1} K^{-1}. REQUIRED: rate of heat transfer Q/t = ?',
         'حل — دیا گیا: رقبہ A = 0.950 m^2؛ لمبائی L = 2.50 cm = 0.0250 m؛ درجۂ حرارت کا فرق T_h − T_c = 35 K؛ اسٹائروفوم کی ایصالیت k = 0.010 W m^{-1} K^{-1}۔ مطلوب: حرارت کی منتقلی کی شرح Q/t = ?',
         'حل — ورکړل شوي: مساحت A = 0.950 m^2؛ اوږدوالی L = 2.50 cm = 0.0250 m؛ د تودوخې توپیر T_h − T_c = 35 K؛ د سټایروفوم هدایت k = 0.010 W m^{-1} K^{-1}. غوښتل شوي: د تودوخې د لېږد کچه Q/t = ?'),
        ('p', 'The rate of energy transfer is given as', 'توانائی کی منتقلی کی شرح یوں ہے', 'د انرژۍ د لېږد کچه داسې ده'),
        ('eq', 'phys9-u9-ex91-1', '[[Q|t]] = k × A × [[T_h − T_c|L]]'),
        ('p', 'putting values', 'قدریں رکھنے سے', 'د ارزښتونو په ایښودلو'),
        ('eq', 'phys9-u9-ex91-2', '[[Q|t]] = 0.010 [[W|m K]] × 0.950 m^2 × [[35 K|0.0250 m]]'),
    ]),
]
EXTRA = dict(definitions=[dict(term='Thermal conductivity (k)', definition='The quantity of heat which flows through one square metre of area of the substance in one second when a temperature difference of one kelvin is maintained across a thickness of one meter; k = QL/(At(T_h − T_c)); SI unit W m⁻¹ K⁻¹.', urdu='ایک میٹر موٹائی پر ایک کیلون فرق کے ساتھ ایک سیکنڈ میں ایک مربع میٹر سے گزرنے والی حرارت؛ اکائی W m⁻¹ K⁻¹۔', pashto='د یو متر ضخامت پر یو کېلوین توپیر سره په یوه ثانیه کې له یو مربع متر تېرېدونکې تودوخه؛ واحد W m⁻¹ K⁻¹.')],
             formulaSourceLinks=[dict(name='Thermal conduction (rate of heat flow)', blockIds=['phys9-u9-eq91', 'phys9-u9-eq92'])])
