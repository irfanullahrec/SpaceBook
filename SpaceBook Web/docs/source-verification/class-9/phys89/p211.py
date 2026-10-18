# -*- coding: utf-8 -*-
TITLE = 'Linear expansion: Figure 8.5, equations 8.6-8.8, coefficient of linear expansion'
SECTIONS = [
    ('8.4.1', ('8.4.1 THERMAL EXPANSION OF SOLIDS', '8.4.1 ٹھوس اجسام کا حرارتی پھیلاؤ', '8.4.1 د جامدو تودوخیز پراخوالی'), [
        ('p', 'The change in length Δl is also proportional to the original length l_o of the object. That is, for the same temperature increase, a 4 m long iron rod will increase in length twice as much as a 2 m long iron rod. We can write this proportionality as an equation:',
         'لمبائی کی تبدیلی Δl چیز کی ابتدائی لمبائی l_o کے بھی متناسب ہے۔ یعنی ایک جتنے درجۂ حرارت کے اضافے پر 4 m لمبی لوہے کی سلاخ کی لمبائی 2 m لمبی سلاخ سے دگنی بڑھے گی۔ اس تناسب کو ہم یوں لکھ سکتے ہیں:',
         'د اوږدوالي بدلون Δl د شي له لومړني اوږدوالي l_o سره هم متناسب دی. یعنې د تودوخې د یو شان زیاتوالي لپاره به د اوسپنې 4 m اوږده میله د 2 m اوږدې میلې په پرتله دوه چنده اوږده شي. دا تناسب داسې لیکو:'),
        ('eq', 'phys9-u8-lin2', 'Δl ∝ l_o', '2'),
        ('fig', 'Figure 8.5 LINEAR EXPANSION: a rod of original length l_o lengthens by Δl to l_T on heating.', 'شکل 8.5 طولی پھیلاؤ: گرم کرنے پر ابتدائی لمبائی l_o والی سلاخ Δl بڑھ کر l_T ہو جاتی ہے۔', '8.5 شکل اوږدیز پراخوالی: د l_o لومړني اوږدوالي میله په تودولو Δl اوږده کېږي او l_T ته رسېږي.'),
        ('p', 'combining equation 1 and equation 2 we get', 'مساوات 1 اور مساوات 2 کو ملانے سے', 'د 1 او 2 معادلو په یوځای کولو سره لرو'),
        ('eq', 'phys9-u8-lin3', 'Δl ∝ l_o ΔT'),
        ('p', 'changing proportionality into equality', 'تناسب کو مساوات میں بدلنے سے', 'د تناسب په مساوات بدلولو سره'),
        ('eq', 'phys9-u8-eq86', 'Δl = α l_o ΔT', '8.6'),
        ('p', "where 'α' the proportionality constant, is called the coefficient of linear thermal expansion for the particular material and has units of °C^{-1} and in SI as K^{-1}.",
         "جہاں تناسب کا مستقل 'α' اس مادے کا طولی حرارتی پھیلاؤ کا عددی سر کہلاتا ہے اور اس کی اکائی °C^{-1} اور SI میں K^{-1} ہے۔",
         "چېرې چې د تناسب ثابت 'α' د هغې مادې د اوږدیز تودوخیز پراخوالي ضریب بلل کېږي او واحد یې °C^{-1} او په SI کې K^{-1} دی."),
        ('p', 'since Δl = l_o − l_T (as printed), we can write the above equation as', 'چونکہ Δl = l_o − l_T (کتاب کے مطابق)، اوپر کی مساوات یوں لکھی جا سکتی ہے', 'څرنګه چې Δl = l_o − l_T (لکه چاپ شوی)، پورتنۍ معادله داسې لیکو'),
        ('eq', 'phys9-u8-lin4', 'l_T − l_o = α l_o ΔT'),
        ('p', 'taking l_o common', 'l_o کو مشترک لینے سے', 'د l_o په ګډ اخیستو'),
        ('eq', 'phys9-u8-lin5', 'l_T = l_o + α l_o ΔT'),
        ('p', 'therefore', 'لہٰذا', 'نو'),
        ('eq', 'phys9-u8-eq87', 'l_T = l_o(1 + α ΔT)', '8.7'),
        ('p', 'If the temperature change ΔT = T − T_o is negative, then Δl = l_o − l_T is also negative; the length shortens as the temperature decreases.',
         'اگر درجۂ حرارت کی تبدیلی ΔT = T − T_o منفی ہو تو Δl = l_o − l_T بھی منفی ہے؛ درجۂ حرارت گھٹنے پر لمبائی کم ہو جاتی ہے۔',
         'که د تودوخې بدلون ΔT = T − T_o منفي وي، نو Δl = l_o − l_T هم منفي دی؛ د تودوخې په ټیټېدو اوږدوالی لنډېږي.'),
        ('p', "From equation 8.6, we can define coefficient of linear thermal expansion α of a substance as the increase in length per unit length of the solid per kelvin 'K' rise in temperature.",
         "مساوات 8.6 سے ہم کسی مادے کے طولی حرارتی پھیلاؤ کے عددی سر α کی تعریف یوں کر سکتے ہیں: درجۂ حرارت میں فی کیلون 'K' اضافے پر ٹھوس کی فی اکائی لمبائی میں اضافہ۔",
         "له 8.6 معادلې د یوې مادې د اوږدیز تودوخیز پراخوالي ضریب α داسې تعریفوو: د تودوخې د هر کېلوین 'K' لوړېدو پر وړاندې د جامد د هر واحد اوږدوالي زیاتوالی."),
        ('eq', 'phys9-u8-eq88', 'α = [[Δl|l_o ΔT]]', '8.8'),
        ('p', 'In simple words, α is numerically the increase in 1 m long wire for 1 degree rise of temperature. The value of α depends upon the nature of material. The values of coefficients of linear thermal expansion (α) for different materials are given in the table 8.2.',
         'سادہ الفاظ میں α عددی طور پر 1 m لمبے تار کی لمبائی میں درجۂ حرارت کے 1 درجہ اضافے پر ہونے والا اضافہ ہے۔ α کی قدر مادے کی نوعیت پر منحصر ہے۔ مختلف مادوں کے طولی حرارتی پھیلاؤ کے عددی سر (α) جدول 8.2 میں دیے گئے ہیں۔',
         'په ساده ټکو، α په عددي ډول د 1 m اوږد سیم د اوږدوالي زیاتوالی دی کله چې تودوخه 1 درجه لوړه شي. د α ارزښت د مادې په طبیعت پورې اړه لري. د بېلابېلو موادو د اوږدیز تودوخیز پراخوالي ضریبونه (α) په 8.2 جدول کې ورکړل شوي.'),
    ]),
]
EXTRA = dict(
    definitions=[dict(term='Coefficient of linear thermal expansion (α)', definition='The increase in length per unit length of the solid per kelvin rise in temperature: α = Δl/(l_o ΔT); unit K⁻¹ (°C⁻¹).',
                      urdu='درجۂ حرارت میں فی کیلون اضافے پر ٹھوس کی فی اکائی لمبائی میں اضافہ؛ α = Δl/(l_o ΔT)؛ اکائی K⁻¹۔', pashto='د تودوخې د هر کېلوین لوړېدو پر وړاندې د جامد د هر واحد اوږدوالي زیاتوالی؛ α = Δl/(l_o ΔT)؛ واحد K⁻¹.')],
    formulaSourceLinks=[dict(name='Linear thermal expansion', blockIds=['phys9-u8-eq86', 'phys9-u8-eq87', 'phys9-u8-eq88'])],
)
