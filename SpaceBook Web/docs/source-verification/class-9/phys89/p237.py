# -*- coding: utf-8 -*-
TITLE = 'Comprehensive questions 7-8 / numerical questions / web link (Unit 8 ends)'
from p236 import LQ2
KEY = 'Textbook answer key, printed page 254 (PDF page 259)'
N = [
    ('Perform the temperature conversions (a) Temperature difference in the body. The surface temperature of the body is normally about 7 °C lower than the internal temperature. Express this temperature difference in kelvins and in Fahrenheit degrees. (b) Blood storage. Blood stored at 4.0 °C lasts safely for about 3 weeks, whereas blood stored at −160 °C lasts for 5 years. Express both temperatures on the Fahrenheit and Kelvin scales.',
     'درجۂ حرارت کی تبدیلیاں کریں: (a) جسم میں درجۂ حرارت کا فرق۔ جسم کی سطح کا درجۂ حرارت عموماً اندرونی درجۂ حرارت سے تقریباً 7 °C کم ہوتا ہے۔ اس فرق کو کیلون اور فارن ہائیٹ درجوں میں ظاہر کریں۔ (b) خون کا ذخیرہ۔ 4.0 °C پر رکھا خون تقریباً 3 ہفتے محفوظ رہتا ہے جبکہ −160 °C پر 5 سال۔ دونوں درجۂ حرارت فارن ہائیٹ اور کیلون پیمانوں پر ظاہر کریں۔',
     'د تودوخې اړونې وکړئ: (a) په بدن کې د تودوخې توپیر. د بدن د سطحې تودوخه معمولاً تر داخلي تودوخې شاوخوا 7 °C ټیټه وي. دا توپیر په کېلوین او فارنهایټ درجو کې وښایاست. (b) د وینې ساتنه. په 4.0 °C کې ساتل شوې وینه شاوخوا 3 اونۍ او په −160 °C کې 5 کاله خوندي پاتې کېږي. دواړه تودوخې پر فارنهایټ او کېلوین پیمانو وښایاست.',
     'Book key: a. 7 K, 13 °F; b. −256 °F, 115 K. SpaceBook check: a difference of 7 °C = 7 K = 12.6 °F (≈13 °F); 4.0 °C = 39.2 °F = 277 K; −160 °C = −256 °F = 113 K.'),
    ('Consider a metre-stick composed of platinum (the coefficient of linear expansion for platinum is α = 8.8 × 10⁻⁶ K⁻¹). By what amount does the length of this metre-stick change if the temperature increases by 1.0 K?',
     'پلاٹینم کی ایک میٹر چھڑی لیں (α = 8.8 × 10⁻⁶ K⁻¹)۔ درجۂ حرارت 1.0 K بڑھنے پر اس کی لمبائی کتنی بدلے گی؟', 'د پلاټینم یو متره ډنډه (α = 8.8 × 10⁻⁶ K⁻¹). که تودوخه 1.0 K لوړه شي اوږدوالی یې څومره بدلېږي؟',
     'Book key: 8.8 × 10⁻⁶ m (Δl = α l₀ ΔT = 8.8 × 10⁻⁶ × 1 × 1).'),
    ('A railway line made of iron is 1200 km long and is laid at 25 °C. By how much will it contract in winter when the temperature falls to 15 °C? By how much will it expand when the temperature rises to 40 °C in summer? (the coefficient of linear expansion for iron is α = 12 × 10⁻⁶ K⁻¹).',
     'لوہے کی 1200 km لمبی ریلوے لائن 25 °C پر بچھائی گئی۔ سردیوں میں 15 °C پر یہ کتنی سکڑے گی اور گرمیوں میں 40 °C پر کتنی پھیلے گی؟ (α = 12 × 10⁻⁶ K⁻¹)', 'د اوسپنې 1200 km اوږده پټلۍ په 25 °C کې غوړول شوې. په ژمي کې 15 °C ته به څومره لنډه او په اوړي کې 40 °C ته به څومره اوږده شي؟ (α = 12 × 10⁻⁶ K⁻¹)',
     'Book key: 144 m, 216 m (contraction 12 × 10⁻⁶ × 1.2 × 10⁶ × 10 = 144 m; expansion × 15 K = 216 m).'),
    ('The volume of a brass ball is 800 cm³ at 20 °C. Find out the new volume of the ball if the temperature is raised to 52 °C. The coefficient of volumetric expansion of brass is 57 × 10⁻⁶ K⁻¹.',
     'پیتل کی گیند کا حجم 20 °C پر 800 cm³ ہے۔ درجۂ حرارت 52 °C ہونے پر نیا حجم معلوم کریں۔ γ = 57 × 10⁻⁶ K⁻¹۔', 'د پیتلو توپ حجم په 20 °C کې 800 cm³ دی. په 52 °C کې نوی حجم یې معلوم کړئ. γ = 57 × 10⁻⁶ K⁻¹.',
     'Book key: 1.228 cm³. SpaceBook check: ΔV = 57 × 10⁻⁶ × 800 × 32 = 1.459 cm³, so the new volume is about 801.46 cm³; the printed key value does not match the given data.'),
    ('What is the specific heat of a metal substance if 135 kJ of heat is needed to raise 4.1 kg of the metal from 18.0 °C to 37.2 °C?', 'اگر 4.1 kg دھات کا درجۂ حرارت 18.0 °C سے 37.2 °C تک بڑھانے کو 135 kJ حرارت درکار ہو تو اس کی مخصوص حرارت کیا ہے؟', 'که د 4.1 kg فلز تودوخه له 18.0 °C څخه 37.2 °C ته لوړولو ته 135 kJ تودوخه پکار وي، ځانګړې تودوخه یې څومره ده؟',
     'Book key: 1700 J/kgK (c = 135000 / (4.1 × 19.2) ≈ 1.7 × 10³ J kg⁻¹ K⁻¹).'),
    ('How much heat is needed to melt 23.50 kg of silver that is initially at 25 °C? (Specific Heat of silver is c = 230 J kg⁻¹ K⁻¹, Latent heat of fusion for silver is L_f = 8.82 × 10⁴ J kg⁻¹ (printed "J K⁻¹") and melting point of silver is 961 °C).',
     '25 °C پر موجود 23.50 kg چاندی پگھلانے کے لیے کتنی حرارت چاہیے؟ (c = 230 J kg⁻¹ K⁻¹، L_f = 8.82 × 10⁴ J kg⁻¹، نقطۂ پگھلاؤ 961 °C)', 'په 25 °C کې د 23.50 kg سپینو زرو د ویلې کولو لپاره څومره تودوخه پکار ده؟ (c = 230 J kg⁻¹ K⁻¹، L_f = 8.82 × 10⁴ J kg⁻¹، د ویلې کېدو ټکی 961 °C)',
     'Book key: 7.1 × 10⁶ J (heating 23.5 × 230 × 936 = 5.06 × 10⁶ J plus melting 23.5 × 8.82 × 10⁴ = 2.07 × 10⁶ J).'),
]
ITEMS = [('p', f'{i}. {q}', f'{i}. {u}', f'{i}. {p}') for i, (q, u, p, a) in enumerate(LQ2, 7)]
ITEMS2 = [('h', 'NUMERICAL QUESTIONS', 'عددی سوالات', 'عددي پوښتنې')] + [('p', f'{i}. {q}', f'{i}. {u}', f'{i}. {p}') for i, (q, u, p, a) in enumerate(N, 1)]
SECTIONS = [('source-u8-exercise-comprehensive', ('COMPREHENSIVE QUESTIONS', 'جامع سوالات', 'جامع پوښتنې'), ITEMS),
            ('source-u8-exercise-numerical', ('NUMERICAL QUESTIONS', 'عددی سوالات', 'عددي پوښتنې'), ITEMS2),
            ('source-u8-web-links', ('WEB LINK', 'ویب ربط', 'وېب تړنه'), [('p', 'http://www.thermopedia.com/', 'http://www.thermopedia.com/', 'http://www.thermopedia.com/')])]
EXTRA = dict(chapterEnd=True, textbookExercise=dict(numericalQuestions=[dict(num=i, q=q, urdu=u, pashto=p, ans=a, answerProvidedInSource=True, answerOrigin=KEY) for i, (q, u, p, a) in enumerate(N, 1)]))
