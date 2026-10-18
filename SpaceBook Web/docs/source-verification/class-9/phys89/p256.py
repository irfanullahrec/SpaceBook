# -*- coding: utf-8 -*-
TITLE = 'Unit 9 comprehensive and numerical questions (Unit 9 ends)'
SA = 'SpaceBook answer (no answer is printed in the textbook)'
KEY = 'Textbook answer key, printed page 254 (PDF page 259), with SpaceBook check'
LQ = [
    ('Explain conduction of heat and its mechanism. Describe any three of its practical applications.', 'حرارت کے ایصال اور اس کے طریقۂ کار کی وضاحت کریں اور اس کے کوئی تین عملی استعمالات بیان کریں۔', 'د تودوخې هدایت او میکانیزم یې تشریح کړئ او درې عملي کارونې یې بیان کړئ.',
     'Conduction: flow of heat through matter from hot to cold parts without bulk movement. Hotter atoms vibrate more and pass energy to neighbours by collisions; in metals free electrons gain energy and diffuse to colder parts. Applications: metal cooking pots, wire gauze over a flame, pot holders/table mats of poor conductors, woolen clothes, igloos, ice box with cork, soldering (p.234-238).'),
    ('Explain thermal conductivity of a substance and its mathematical description.', 'کسی مادے کی حرارتی ایصالیت اور اس کی ریاضیاتی تفصیل بیان کریں۔', 'د یوې مادې تودوخیز هدایت او ریاضي بیان یې تشریح کړئ.',
     'Thermal conductivity measures a substance’s ability to conduct heat. The rate of heat flow Q/t through a slab increases with temperature difference (T_h − T_c) and area A, decreases with thickness L, and depends on the material: Q/t = k A (T_h − T_c)/L, so k = QL/(A t (T_h − T_c)); unit W m⁻¹ K⁻¹ (p.238-239).'),
    ('Explain convection of heat and its mechanism. Explain any three of its practical applications.', 'حرارت کے کنویکشن اور اس کے طریقۂ کار کی وضاحت کریں اور تین عملی استعمالات بیان کریں۔', 'د تودوخې حمل او میکانیزم یې تشریح کړئ او درې عملي کارونې یې بیان کړئ.',
     'Convection: heat transfer by bulk motion of a fluid. Heated fluid expands, becomes less dense and rises; cooler dense fluid replaces it, setting up convection currents. Applications: heating water in a kettle, sea and land breezes, thermals for birds and gliders, refrigerator air circulation, ventilation and chimneys (p.240-242).'),
    ('Explain radiation of heat and its mechanism. Describe any three of its practical applications.', 'حرارت کی اشعاع اور اس کے طریقۂ کار کی وضاحت کریں اور تین عملی استعمالات بیان کریں۔', 'د تودوخې وړانګې او میکانیزم یې تشریح کړئ او درې عملي کارونې یې بیان کړئ.',
     'Radiation: heat transfer from hot to cold with or without a medium, by electromagnetic (mainly infrared) waves emitted by accelerating charges in vibrating molecules. Rate depends on colour/texture, surface temperature and area. Applications: black fins on refrigerator heat exchangers, shiny teapots, white summer clothing, thermos flask with silvered walls, solar heating (p.243-246).'),
    ('Discuss the greenhouse effect. Explain its importance and global warming concern.', 'گرین ہاؤس اثر پر بحث کریں اور اس کی اہمیت اور عالمی حدت کی تشویش بیان کریں۔', 'د شنې خونې اغېز وڅېړئ او اهمیت یې او د نړیوالې تودوخې اندېښنه بیان کړئ.',
     'Earth absorbs sunlight (26% reflected, 19% absorbed by air and clouds, the rest by the surface) and re-radiates longer-wavelength infrared that greenhouse gases absorb and partly return, warming the surface by about 33 °C — essential for life. Extra CO₂ from factories and vehicles has raised the global average temperature by 0.85 °C (1880-2012); remedies: cut emissions and plant more vegetation (p.246-248).'),
]
N = [
    ("A person's body is covered with 1.6 m² of wool clothing. The thickness of the wool is 2.0 × 10³ m (printed; 2.0 × 10⁻³ m is meant). The temperature at the outside surface of the wool is 11 °C, and the skin temperature is 36 °C. How much heat per second does the person lose due to conduction? Thermal conductivity of wool is k = 0.04 W m⁻¹ K⁻¹.",
     'کسی شخص کا جسم 1.6 m² اونی کپڑوں سے ڈھکا ہے۔ اون کی موٹائی 2.0 × 10³ m (کتاب میں؛ مراد 2.0 × 10⁻³ m) ہے۔ اون کی بیرونی سطح کا درجۂ حرارت 11 °C اور جلد کا 36 °C ہے۔ ایصال سے وہ فی سیکنڈ کتنی حرارت کھوتا ہے؟ اون کی ایصالیت k = 0.04 W m⁻¹ K⁻¹۔',
     'د یوه کس بدن په 1.6 m² وړینو جامو پوښل شوی. د وړۍ ضخامت 2.0 × 10³ m (په کتاب کې؛ مطلب 2.0 × 10⁻³ m) دی. د وړۍ بهرنۍ سطحه 11 °C او پوستکی 36 °C دی. د هدایت له لارې په هره ثانیه کې څومره تودوخه له لاسه ورکوي؟ k = 0.04 W m⁻¹ K⁻¹.',
     'Book key: 8.0 × 10² W. Check: Q/t = 0.04 × 1.6 × 25 / 2.0 × 10⁻³ = 800 W.'),
    ('The external wall of a brick house has an area of 16 m² and thickness 0.3 m. The temperatures inside and outside the house are respectively 20 °C and 0 °C. Calculate the rate of heat loss through the wall. Thermal conductivity of brick is k = 0.84 W m⁻¹ K⁻¹.',
     'اینٹ کے گھر کی بیرونی دیوار کا رقبہ 16 m² اور موٹائی 0.3 m ہے۔ اندر اور باہر کا درجۂ حرارت بالترتیب 20 °C اور 0 °C ہے۔ دیوار سے حرارت کے ضیاع کی شرح معلوم کریں۔ k = 0.84 W m⁻¹ K⁻¹۔',
     'د خښتو د کور بهرنی دېوال 16 m² مساحت او 0.3 m ضخامت لري. دننه او بهر تودوخه په ترتیب 20 °C او 0 °C ده. له دېوال د تودوخې د ضایع کچه معلومه کړئ. k = 0.84 W m⁻¹ K⁻¹.',
     'SpaceBook check: Q/t = 0.84 × 16 × 20 / 0.3 ≈ 896 W (8.96 × 10² W). The printed key lists four values (8.0 × 10² W; 6.1 × 10⁴ J; 533 W; 6.0 × 10³ W) for three problems, and none matches this one.'),
    ('Window glass has thermal conductivity of 0.8 W m⁻¹ K⁻¹. Calculate the rate at which heat is conducted through a window of area 2.0 m² and thickness 4.0 mm. The temperature inside an air-conditioned room is 20 °C. The outdoor temperature is 35 °C.',
     'کھڑکی کے شیشے کی ایصالیت 0.8 W m⁻¹ K⁻¹ ہے۔ 2.0 m² رقبے اور 4.0 mm موٹائی کی کھڑکی سے حرارت کے ایصال کی شرح معلوم کریں۔ ایئر کنڈیشنڈ کمرے کا درجۂ حرارت 20 °C اور باہر کا 35 °C ہے۔',
     'د کړکۍ د ښیښې هدایت 0.8 W m⁻¹ K⁻¹ دی. د 2.0 m² مساحت او 4.0 mm ضخامت کړکۍ له لارې د تودوخې د هدایت کچه معلومه کړئ. د ایرکنډیشن خونې تودوخه 20 °C او بهر 35 °C ده.',
     'Book key (fourth entry): 6.0 × 10³ W. Check: Q/t = 0.8 × 2.0 × 15 / 4.0 × 10⁻³ = 6000 W.'),
]
LITEMS = [('h', 'COMPREHENSIVE QUESTIONS — Give an extended response to the following questions.', 'جامع سوالات — درج ذیل سوالات کا تفصیلی جواب دیں۔', 'جامع پوښتنې — لاندې پوښتنو ته پراخ ځواب ورکړئ.')]
LITEMS += [('p', f'{i}. {q}', f'{i}. {u}', f'{i}. {p}') for i, (q, u, p, a) in enumerate(LQ, 1)]
NITEMS = [('h', 'NUMERICAL QUESTIONS', 'عددی سوالات', 'عددي پوښتنې')] + [('p', f'{i}. {q}', f'{i}. {u}', f'{i}. {p}') for i, (q, u, p, a) in enumerate(N, 1)]
SECTIONS = [('source-u9-exercise-comprehensive', ('COMPREHENSIVE QUESTIONS', 'جامع سوالات', 'جامع پوښتنې'), LITEMS),
            ('source-u9-exercise-numerical', ('NUMERICAL QUESTIONS', 'عددی سوالات', 'عددي پوښتنې'), NITEMS)]
EXTRA = dict(chapterEnd=True, textbookExercise=dict(
    lq=[dict(num=i, q=q, urdu=u, pashto=p, ans=a, answerOrigin=SA, answerProvidedInSource=False) for i, (q, u, p, a) in enumerate(LQ, 1)],
    numericalQuestions=[dict(num=i, q=q, urdu=u, pashto=p, ans=a, answerProvidedInSource=(i != 2), answerOrigin=KEY) for i, (q, u, p, a) in enumerate(N, 1)]))
