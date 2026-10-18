# -*- coding: utf-8 -*-
"""Unit 7 part B — PDF 138-149 (printed 135-146): 7.2.2-7.5, Key Points, Exercise."""
from bio9_tools import Section, svg_wrap, txt
from unit4_figs import multiline
from unit4_figs2 import pointer

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')
STS = ('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه')


def reaction_box(L, inputs, outputs, colour):
    b = [txt(40, 18, L['reactants'], 13, 'start', 'bold', '#5e35b1') + txt(430, 18, L['products'], 13, 'end', 'bold', '#5e35b1'),
         f'<rect x="150" y="28" width="180" height="130" rx="18" fill="{colour}" stroke="#555"/>' + multiline(240, 90, L['centre'], 'middle', 12)]
    for i, t in enumerate(inputs):
        y = 55 + i * 28
        b.append(txt(20, y + 4, t, 12, 'start', 'bold') + f'<path d="M95,{y} h60" stroke="#e91e63" stroke-width="3"/><polygon points="155,{y-5} 165,{y} 155,{y+5}" fill="#e91e63"/>')
    for i, t in enumerate(outputs):
        y = 55 + i * 28
        b.append(f'<path d="M330,{y} h60" stroke="#333" stroke-width="2"/><polygon points="390,{y-4} 398,{y} 390,{y+4}" fill="#333"/>' + txt(402, y + 4, t, 12, 'start', 'bold'))
    b.append(pointer(240, 155, 240, 178, L['site'], 'middle'))
    return svg_wrap(''.join(b), 470, 200, L['title'])


LR = dict(title='Figure 7.6: Reactants and Products of the Light Reactions', reactants='Reactants', products='Products', centre=['Light', 'Reactions'], site='Granum of chloroplast')
LR_UR = dict(title='شکل 7.6', reactants='متعاملات', products='حاصلات', centre=['روشنی کے', 'تعاملات'], site='کلوروپلاسٹ کا گرینم')
LR_PS = dict(title='شکل 7.6', reactants='متعامل', products='محصولات', centre=['د رڼا', 'تعاملونه'], site='د کلوروپلاسټ ګرانوم')
DR = dict(title='Figure 7.7: Reactants and Products of the Dark Reactions', reactants='Reactants', products='Products', centre=['Dark', 'Reactions'], site='Stroma of chloroplast')
DR_UR = dict(title='شکل 7.7', reactants='متعاملات', products='حاصلات', centre=['تاریک', 'تعاملات'], site='کلوروپلاسٹ کا اسٹروما')
DR_PS = dict(title='شکل 7.7', reactants='متعامل', products='محصولات', centre=['د تیارې', 'تعاملونه'], site='د کلوروپلاسټ سټروما')


def light_fig(L):
    return reaction_box(L, ['Sunlight' if L['reactants'] == 'Reactants' else L.get('sun', 'Sunlight'), 'ADP + Pi', 'NADP', 'H₂O'], ['ATP', 'NADPH', 'O₂'], '#66bb6a')


def dark_fig(L):
    return reaction_box(L, ['ATP', 'NADPH', 'CO₂'], ['ADP + Pi', 'NADP', 'Glucose'], '#81d4fa')


def summary_fig(L):
    b = ['<path d="M120,70 Q60,70 60,150 Q60,230 140,235 L380,235 Q470,230 470,150 Q470,70 400,70 Z" fill="#b3e5fc" stroke="#0277bd" stroke-width="3"/>',
         '<rect x="150" y="110" width="80" height="80" rx="12" fill="#66bb6a"/>' + multiline(190, 145, L['light'], 'middle', 11),
         '<circle cx="360" cy="150" r="45" fill="#81d4fa" stroke="#0277bd"/>' + multiline(360, 145, L['dark'], 'middle', 11)]
    b.append('<path d="M190,30 V110 M190,190 V265" stroke="#455a64" stroke-width="5"/><circle cx="190" cy="22" r="14" fill="#b0bec5"/>' + txt(190, 26, 'H₂O', 9, 'middle', 'bold') + '<circle cx="190" cy="275" r="14" fill="#b0bec5"/>' + txt(190, 279, 'O₂', 9, 'middle', 'bold'))
    b.append('<path d="M100,95 L148,130" stroke="#fdd835" stroke-width="6"/>' + txt(70, 92, L['sun'], 11, 'start', 'bold'))
    b.append('<circle cx="400" cy="22" r="14" fill="#b0bec5"/>' + txt(400, 26, 'CO₂', 9, 'middle', 'bold') + '<path d="M400,36 Q400,80 380,108 M340,190 Q330,240 360,262" stroke="#29b6f6" stroke-width="5" fill="none"/>' + txt(380, 278, L['glucose'], 11, 'start', 'bold'))
    for y, t, d in [(125, 'NADP', -1), (148, 'ADP + Pi', -1), (172, 'NADPH', 1), (192, 'ATP', 1)]:
        b.append(txt(270, y, t, 10, 'middle', 'bold') + (f'<path d="M300,{y-4} h12" stroke="#333"/>' if d > 0 else f'<path d="M240,{y-4} h-8" stroke="#333"/>'))
    b.append(pointer(165, 115, 60, 125, L['granum'], 'end') + pointer(140, 210, 60, 175, L['stroma'], 'end') + pointer(90, 225, 60, 225, L['chloroplast'], 'end'))
    return svg_wrap('<g transform="translate(70,0)">' + ''.join(b) + '</g>', 600, 295, L['title'])


SM_EN = dict(title='Figure 7.8: Summary of the process of Photosynthesis', light=['Light', 'Reactions'], dark=['Dark', 'Reactions'], sun='Sunlight', glucose='Glucose', granum='Granum', stroma='Stroma', chloroplast='Chloroplast')
SM_UR = dict(title='شکل 7.8', light=['روشنی کے', 'تعاملات'], dark=['تاریک', 'تعاملات'], sun='سورج کی روشنی', glucose='گلوکوز', granum='گرینم', stroma='اسٹروما', chloroplast='کلوروپلاسٹ')
SM_PS = dict(title='شکل 7.8', light=['د رڼا', 'تعاملونه'], dark=['د تیارې', 'تعاملونه'], sun='د لمر رڼا', glucose='ګلوکوز', granum='ګرانوم', stroma='سټروما', chloroplast='کلوروپلاسټ')


def fermentation_fig(L, alcoholic=False):
    b = [txt(30, 70, L['glucose'], 13, 'start', 'bold'), '<path d="M100,65 h150" stroke="#333" stroke-width="3"/><polygon points="250,59 262,65 250,71" fill="#333"/>',
         txt(175, 85, L['glyco'], 11, 'middle', 'bold'), txt(268, 70, L['pyruvic'], 13, 'start', 'bold'),
         '<path d="M140,25 q35,25 70,0" stroke="#333" fill="none"/>' + txt(140, 18, '2ADP+2Pi', 10, 'middle') + txt(212, 18, '2ATP', 10, 'middle'),
         '<path d="M140,110 q35,-25 70,0" stroke="#333" fill="none"/>' + txt(140, 125, '2 NAD', 10, 'middle') + txt(212, 125, '2NADH', 10, 'middle'),
         '<path d="M330,80 v60" stroke="#333" stroke-width="3"/><polygon points="324,140 330,152 336,140" fill="#333"/>', txt(330, 172, L['end'], 13, 'middle', 'bold'),
         '<path d="M212,128 Q270,180 320,150" stroke="#888" fill="none" stroke-dasharray="4 3"/>']
    if alcoholic:
        b.append('<path d="M330,110 h50" stroke="#333" stroke-width="2"/>' + txt(386, 114, '2CO₂', 12, 'start', 'bold'))
    return svg_wrap(''.join(b), 440, 185, L['title'])


LA_EN = dict(title='Figure 7.9: Lactic acid Fermentation', glucose='Glucose', glyco='Glucolysis', pyruvic='2 Pyruvic acid', end='2 Lactic acid')
LA_UR = dict(title='شکل 7.9', glucose='گلوکوز', glyco='گلائکولائسس', pyruvic='2 پائروِک ایسڈ', end='2 لیکٹک ایسڈ')
LA_PS = dict(title='شکل 7.9', glucose='ګلوکوز', glyco='ګلایکولیزس', pyruvic='2 پایرویک اسید', end='2 لاکټیک اسید')
AF_EN = dict(LA_EN, title='Figure 7.10: Alcoholic Fermentation', end='2 Ethanol')
AF_UR = dict(LA_UR, title='شکل 7.10', end='2 ایتھینول')
AF_PS = dict(LA_PS, title='شکل 7.10', end='2 ایتانول')


def aerobic_fig(L):
    b = ['<rect x="60" y="20" width="150" height="130" fill="#e1f5fe" stroke="#90a4ae"/><rect x="60" y="160" width="150" height="130" fill="#e1f5fe" stroke="#90a4ae"/>',
         '<polygon points="270,20 270,290 540,290" fill="#fff" stroke="#333"/>']
    for y, t in [(30, L['glucose']), (115, L['pyruvic']), (160, 'Acetyl CoA')]:
        b.append(f'<rect x="95" y="{y}" width="80" height="22" fill="#a5d6a7"/>' + txt(135, y + 15, t, 10, 'middle', 'bold'))
    b.append('<path d="M135,52 V113 M135,137 V158" stroke="#333" stroke-width="4"/><circle cx="135" cy="230" r="35" fill="none" stroke="#333" stroke-width="4"/>' + txt(135, 233, 'Krebs cycle', 9, 'middle', 'bold', '#d81b60'))
    b.append(txt(165, 85, L['glyco'], 9, 'middle', 'bold', '#d81b60') + txt(410, 140, 'Electron Transport Chain', 11, 'middle', 'bold', '#d81b60', extra=' transform="rotate(48 410 140)"'))
    rows = [(75, '2', 'NADH', 345), (120, '2', 'NADH', 395), (185, '6', 'NADH', 450), (215, '2', 'FADH₂', 505)]
    for y, n, t, x in rows:
        b.append(f'<path d="M210,{y} h50" stroke="#f48fb1" stroke-width="8"/>' + txt(262, y + 4, n, 11, 'start', 'bold') + f'<rect x="272" y="{y-10}" width="50" height="20" fill="#fff59d"/>' + txt(297, y + 4, t, 10, 'middle', 'bold'))
        b.append(f'<path d="M322,{y} H{x} V300" stroke="#f48fb1" stroke-width="7" fill="none"/>')
    b.append('<path d="M60,60 H40 V300 M190,280 V300" stroke="#f48fb1" stroke-width="7" fill="none"/>')
    for x, t in [(40, '2 ATP'), (190, '2 ATP'), (345, '4 ATP'), (395, '6 ATP'), (450, '18 ATP'), (505, '4 ATP')]:
        b.append(txt(x, 320, t, 11, 'middle', 'bold'))
    b.append(txt(410, 345, L['total'], 12, 'middle', 'bold'))
    return svg_wrap(''.join(b), 560, 360, L['title'])


AR_EN = dict(title='Figure 7.11: Steps of Aerobic Respiration and Energy chart', glucose='Glucose', pyruvic='Pyruvic acid', glyco='Glycolysis', total='Total net yield = 36 ATP')
AR_UR = dict(title='شکل 7.11', glucose='گلوکوز', pyruvic='پائروِک ایسڈ', glyco='گلائکولائسس', total='کل خالص حاصل = 36 ATP')
AR_PS = dict(title='شکل 7.11', glucose='ګلوکوز', pyruvic='پایرویک اسید', glyco='ګلایکولیزس', total='ټوله خالصه ګټه = 36 ATP')


def three(fn, a, b, c):
    return fn(a), fn(b), fn(c)


def sections(sec_7_2):
    s = sec_7_2
    s.pdf_pages += [138, 139]
    s.h('7.2.2 Intake of Carbon dioxide and Water by Plants', '7.2.2 پودوں کا کاربن ڈائی آکسائیڈ اور پانی حاصل کرنا', '7.2.2 د بوټو لخوا د کاربن ډای اکساید او اوبو اخیستل')
    s.p('CO₂ is present in air and it is one of the raw materials for photosynthesis. CO₂ is diffused from the outside air into the intercellular spaces of leaf through stomata. Stomata are small openings scattered particularly in the lower epidermis of leaf. Each stoma is guarded by two kidney shaped guard cells. Opening and closing of stomata regulates the diffusion of CO₂, water vapours and O₂ between the intercellular spaces of leaf mesophyll and the external air. After diffusing into the intercellular spaces, CO₂ attaches to the wet surfaces of mesophyll cells. Then it diffuses into the green cells and enters the stroma of chloroplasts. In the dark reaction of photosynthesis, CO₂ molecules are reduced to form glucose molecules.',
        'CO₂ ہوا میں موجود ہے اور یہ ضیائی تالیف کے خام مال میں سے ایک ہے۔ CO₂ بیرونی ہوا سے اسٹومیٹا کے ذریعے پتے کی بین الخلوی جگہوں میں نفوذ کرتی ہے۔ اسٹومیٹا چھوٹے سوراخ ہیں جو خاص طور پر پتے کی نچلی اپی ڈرمس میں بکھرے ہوتے ہیں۔ ہر اسٹوما کی حفاظت دو گردہ نما گارڈ سیلز کرتے ہیں۔ اسٹومیٹا کا کھلنا اور بند ہونا پتے کے میزوفل کی بین الخلوی جگہوں اور بیرونی ہوا کے درمیان CO₂، آبی بخارات اور O₂ کے نفوذ کو منظم کرتا ہے۔ بین الخلوی جگہوں میں نفوذ کے بعد CO₂ میزوفل خلیوں کی گیلی سطحوں سے جڑ جاتی ہے۔ پھر یہ سبز خلیوں میں نفوذ کر کے کلوروپلاسٹ کے اسٹروما میں داخل ہوتی ہے۔ ضیائی تالیف کے تاریک تعامل میں CO₂ کے مالیکیول تخفیف ہو کر گلوکوز کے مالیکیول بناتے ہیں۔',
        'CO₂ په هوا کې شته او د فوتوسنتز له خامو موادو څخه ده. CO₂ له بهرنۍ هوا د سټوماټا له لارې د پاڼې بین الحجروي فضاګانو ته ډیفیوژ کېږي. سټوماټا کوچني سوري دي چې په ځانګړي ډول د پاڼې په لاندې اپیډرمس کې خپاره وي. هر سټوما دوه پښتورګي ډوله ساتونکې حجرې ساتي. د سټوماټا خلاصېدل او تړل کېدل د پاڼې د میزوفیل د بین الحجروي فضاګانو او بهرنۍ هوا ترمنځ د CO₂، د اوبو بخار او O₂ ډیفیوژن تنظیموي. بین الحجروي فضاګانو ته له ډیفیوژن وروسته CO₂ د میزوفیل حجرو لوندو سطحو ته نښلي. بیا شنو حجرو ته ډیفیوژ کېږي او د کلوروپلاسټ سټروما ته ننوځي. د فوتوسنتز د تیارې په تعامل کې د CO₂ مالیکولونه ریډیوس کېږي او د ګلوکوز مالیکولونه جوړوي.')
    s.p('Water is also an essential requirement of photosynthesis. Water is absorbed by the roots of plants from the soil. It is then transported upward to the stem and leaves through xylem vessels. Most of this water is transpired from the leaves while a small portion is used in photosynthesis.',
        'پانی بھی ضیائی تالیف کی لازمی ضرورت ہے۔ پودوں کی جڑیں مٹی سے پانی جذب کرتی ہیں۔ پھر یہ زائلم ویسلز کے ذریعے تنے اور پتوں تک اوپر پہنچایا جاتا ہے۔ اس پانی کا زیادہ تر حصہ پتوں سے بخارات بن کر اڑ جاتا ہے جبکہ ایک چھوٹا حصہ ضیائی تالیف میں استعمال ہوتا ہے۔',
        'اوبه هم د فوتوسنتز اړینه اړتیا ده. د بوټو ریښې له خاورې اوبه جذبوي. بیا د زایلم رګونو له لارې ډډ او پاڼو ته پورته لېږدول کېږي. د دې اوبو ډېره برخه له پاڼو تبخیرېږي او یوه کوچنۍ برخه په فوتوسنتز کې کارېږي.')
    s.callout(SI, [('Nicotinamide Adenine Dinucleotide (NAD) is a coenzyme. Its reduced form is NADH. One form of this coenzyme also carries phosphate with it and is therefore called NADP.', 'نکوٹینامائیڈ ایڈینین ڈائی نیوکلیوٹائیڈ (NAD) ایک کو انزائم ہے۔ اس کی تخفیف شدہ شکل NADH ہے۔ اس کو انزائم کی ایک شکل اپنے ساتھ فاسفیٹ بھی رکھتی ہے اس لیے اسے NADP کہتے ہیں۔', 'نیکوټینامایډ اډینین ډای نیوکلیوټایډ (NAD) یو کو انزایم دی. ریډیوس شوې بڼه یې NADH ده. د دې کو انزایم یوه بڼه له ځان سره فاسفېټ هم لري نو NADP بلل کېږي.')])
    s.h('7.2.3 Mechanism of Photosynthesis', '7.2.3 ضیائی تالیف کا طریقۂ کار', '7.2.3 د فوتوسنتز میکانیزم')
    s.p('The process of photosynthesis is completed in two steps.', 'ضیائی تالیف کا عمل دو مراحل میں مکمل ہوتا ہے۔', 'د فوتوسنتز پروسه په دوو پړاوونو بشپړېږي.')
    s.h('i) Light Reactions', 'i) روشنی کے تعاملات', 'i) د رڼا تعاملونه')
    s.p('Light reactions take place in the granum of chloroplast. Chlorophyll molecules absorb light. Their energy level increases and their excited electrons are released. These high energy electrons are used to produce ATP from ADP and Pi. Light also breaks water molecule into hydrogen and oxygen (O₂). Oxygen is released while hydrogen atoms are used to reduce NADP into NADPH.',
        'روشنی کے تعاملات کلوروپلاسٹ کے گرینم میں ہوتے ہیں۔ کلوروفل مالیکیول روشنی جذب کرتے ہیں۔ ان کی توانائی کی سطح بڑھتی ہے اور ان کے برانگیختہ الیکٹرانز آزاد ہوتے ہیں۔ ان زیادہ توانائی والے الیکٹرانز سے ADP اور Pi سے ATP بنتا ہے۔ روشنی پانی کے مالیکیول کو ہائیڈروجن اور آکسیجن (O₂) میں بھی توڑتی ہے۔ آکسیجن خارج ہو جاتی ہے جبکہ ہائیڈروجن ایٹم NADP کو NADPH میں تخفیف کرنے میں استعمال ہوتے ہیں۔',
        'د رڼا تعاملونه د کلوروپلاسټ په ګرانوم کې کېږي. د کلوروفیل مالیکولونه رڼا جذبوي. د انرژۍ کچه یې لوړېږي او هیجاني الکترونونه یې خوشې کېږي. دا لوړ انرژي لرونکي الکترونونه له ADP او Pi څخه د ATP د جوړولو لپاره کارېږي. رڼا د اوبو مالیکول هم په هایدروجن او اکسیجن (O₂) ماتوي. اکسیجن خوشې کېږي او د هایدروجن اتومونه د NADP په NADPH ریډیوس کولو کې کارېږي.')
    s.fig('bio7-fig7-6', light_fig(LR), light_fig(dict(LR_UR, sun='سورج کی روشنی')), light_fig(dict(LR_PS, sun='د لمر رڼا')), .65, caption=('Figure 7.6: Reactants and Products of the Light Reactions', 'شکل 7.6: روشنی کے تعاملات کے متعاملات اور حاصلات', 'شکل 7.6: د رڼا د تعاملونو متعامل او محصولات'))
    s.h('ii) Dark Reactions (Calvin Cycle)', 'ii) تاریک تعاملات (کیلون سائیکل)', 'ii) د تیارې تعاملونه (کالوین دوره)')
    s.p('The details of dark reactions were discovered by Melvin Calvin. Dark reactions occur in the stroma of chloroplast. These reactions do not require energy of sunlight. During dark reactions, CO₂ molecules are reduced to make carbohydrates. For the reduction of CO₂, ATP provides energy while NADPH provides hydrogen.',
        'تاریک تعاملات کی تفصیلات میلون کیلون نے دریافت کیں۔ تاریک تعاملات کلوروپلاسٹ کے اسٹروما میں ہوتے ہیں۔ ان تعاملات کو سورج کی روشنی کی توانائی درکار نہیں ہوتی۔ تاریک تعاملات کے دوران CO₂ کے مالیکیول تخفیف ہو کر کاربوہائیڈریٹس بناتے ہیں۔ CO₂ کی تخفیف کے لیے ATP توانائی اور NADPH ہائیڈروجن فراہم کرتا ہے۔',
        'د تیارې د تعاملونو جزیات میلوین کالوین کشف کړل. د تیارې تعاملونه د کلوروپلاسټ په سټروما کې کېږي. دا تعاملونه د لمر رڼا انرژۍ ته اړتیا نه لري. د تیارې د تعاملونو پر مهال د CO₂ مالیکولونه ریډیوس کېږي او کاربوهایډریټونه جوړوي. د CO₂ د ریډکشن لپاره ATP انرژي او NADPH هایدروجن ورکوي.')
    s.fig('bio7-fig7-7', *three(dark_fig, DR, DR_UR, DR_PS), .65, caption=('Figure 7.7: Reactants and Products of the Dark Reactions', 'شکل 7.7: تاریک تعاملات کے متعاملات اور حاصلات', 'شکل 7.7: د تیارې د تعاملونو متعامل او محصولات'))
    s.fig('bio7-fig7-8', *three(summary_fig, SM_EN, SM_UR, SM_PS), .8, caption=('Figure 7.8: Summary of the process of Photosynthesis', 'شکل 7.8: ضیائی تالیف کے عمل کا خلاصہ', 'شکل 7.8: د فوتوسنتز د پروسې لنډیز'))
    s.callout(STS, [('Green plants are the primary producers as they are responsible for trapping light. Ultimately, this energy then travels to all other organism. We can improve the light trapping by adopting strategies at the producer level. Evergreen plants and broad leaved plants could increase the absorption of light and could ultimately be the sources of energy for the heterotrophs.', 'سبز پودے بنیادی پیدا کنندگان ہیں کیونکہ یہ روشنی جذب کرنے کے ذمہ دار ہیں۔ آخرکار یہ توانائی تمام دوسرے جانداروں تک پہنچتی ہے۔ ہم پیدا کنندگان کی سطح پر حکمتِ عملی اپنا کر روشنی کے جذب کو بہتر بنا سکتے ہیں۔ سدا بہار اور چوڑے پتوں والے پودے روشنی کا جذب بڑھا سکتے ہیں اور آخرکار ہیٹروٹرافس کے لیے توانائی کا ذریعہ بن سکتے ہیں۔', 'شنه بوټي لومړني تولیدوونکي دي ځکه چې د رڼا د نیولو مسؤل دي. په پای کې دا انرژي نورو ټولو ژوندیو موجوداتو ته ځي. موږ د تولیدوونکي په کچه د ستراتیژیو په غوره کولو د رڼا نیول ښه کولای شو. تل شنه او پلنې پاڼې لرونکي بوټي د رڼا جذب زیاتولای شي او په پای کې د هټروټروفونو لپاره د انرژۍ سرچینه کېدای شي.')])

    out = []
    s = Section('bio7_3', '7.3', 'The Concept of Limiting Factors in Photosynthesis', 'ضیائی تالیف میں محدود کرنے والے عوامل کا تصور', 'په فوتوسنتز کې د محدودوونکو عواملو مفهوم', [140, 141])
    s.p('Any environmental factors absence or deficiency of which can decrease the rate of a metabolic reaction, is called limiting factor for that reaction. Many factors act as the limiting factors for photosynthesis. Important limiting factors of photosynthesis are light intensity, temperature, concentration of carbon dioxide and the availability of water.',
        'کوئی بھی ماحولیاتی عامل جس کی عدم موجودگی یا کمی کسی میٹابولک تعامل کی شرح کم کر سکے، اس تعامل کے لیے محدود کرنے والا عامل کہلاتا ہے۔ بہت سے عوامل ضیائی تالیف کے لیے محدود کرنے والے عوامل کے طور پر کام کرتے ہیں۔ ضیائی تالیف کے اہم محدود کرنے والے عوامل روشنی کی شدت، درجۂ حرارت، کاربن ڈائی آکسائیڈ کا ارتکاز اور پانی کی دستیابی ہیں۔',
        'هر چاپېریالي عامل چې نشتوالی یا کمښت یې د یوه میټابولیکي تعامل کچه کمولای شي، د هغه تعامل لپاره محدودوونکی عامل بلل کېږي. ډېر عوامل د فوتوسنتز لپاره د محدودوونکو عواملو په توګه عمل کوي. د فوتوسنتز مهم محدودوونکي عوامل د رڼا شدت، تودوخه، د کاربن ډای اکساید غلظت او د اوبو شتون دي.')
    s.h('i) Effect of Light Intensity', 'i) روشنی کی شدت کا اثر', 'i) د رڼا د شدت اغېز')
    s.p('Light is a form of radiant energy which the chlorophyll absorbs and converts into chemical energy. This chemical energy is stored in organic compounds.', 'روشنی شعاعی توانائی کی ایک شکل ہے جسے کلوروفل جذب کر کے کیمیائی توانائی میں بدلتا ہے۔ یہ کیمیائی توانائی نامیاتی مرکبات میں ذخیرہ ہوتی ہے۔', 'رڼا د وړانګیزې انرژۍ یوه بڼه ده چې کلوروفیل یې جذبوي او په کیمیاوي انرژۍ یې بدلوي. دا کیمیاوي انرژي په عضوي مرکبونو کې زېرمه کېږي.')
    s.callout(('Quranic Information', 'قرآنی معلومات', 'قرآني معلومات'), [('Allah, the Almighty has created sun as the ultimate source of energy (food) which sustains all life forms on earth.', 'اللہ تعالیٰ نے سورج کو توانائی (خوراک) کا حتمی ذریعہ بنایا ہے جو زمین پر زندگی کی تمام اقسام کو برقرار رکھتا ہے۔', 'الله تعالی لمر د انرژۍ (خوړو) وروستۍ سرچینه پیدا کړې چې پر ځمکه د ژوند ټول ډولونه ساتي.')])
    s.p('Light intensity and quality varies from place to place and time to time. At dawn and sunset and in winter the intensity of light is low. The intensity of light is maximum at midday.', 'روشنی کی شدت اور معیار جگہ جگہ اور وقت وقت پر مختلف ہوتا ہے۔ صبح صادق، غروبِ آفتاب اور سردیوں میں روشنی کی شدت کم ہوتی ہے۔ دوپہر کو روشنی کی شدت زیادہ سے زیادہ ہوتی ہے۔', 'د رڼا شدت او کیفیت له ځایه ځای او له وخته وخت توپیر لري. په سهار، لمر لوېدو او ژمي کې د رڼا شدت کم وي. د رڼا شدت په غرمه کې اعظمي وي.')
    s.p('The quality and intensity of light affects the rate of photosynthesis. Very intense light damages chlorophyll and therefore has indirect effect on the rate of photosynthesis. Very weak light has low energy and therefore energy absorption by the chlorophyll is low. This results in lower rate of photosynthesis.',
        'روشنی کا معیار اور شدت ضیائی تالیف کی شرح پر اثر انداز ہوتے ہیں۔ بہت تیز روشنی کلوروفل کو نقصان پہنچاتی ہے اس لیے ضیائی تالیف کی شرح پر بالواسطہ اثر ڈالتی ہے۔ بہت کمزور روشنی میں توانائی کم ہوتی ہے اس لیے کلوروفل کم توانائی جذب کرتا ہے۔ اس سے ضیائی تالیف کی شرح کم ہو جاتی ہے۔',
        'د رڼا کیفیت او شدت د فوتوسنتز پر کچه اغېز کوي. ډېره تېزه رڼا کلوروفیل ته زیان رسوي او نو د فوتوسنتز پر کچه غیر مستقیم اغېز لري. ډېره کمزورې رڼا لږه انرژي لري او نو کلوروفیل لږه انرژي جذبوي. دا د فوتوسنتز د کچې د کمېدو لامل کېږي.')
    s.h('ii) Effect of CO₂ Concentration', 'ii) CO₂ کے ارتکاز کا اثر', 'ii) د CO₂ د غلظت اغېز')
    s.p('Carbon dioxide is one of the raw materials for photosynthesis. It provides carbon for the synthesis of glucose. As carbon dioxide concentrations rise, the rate of dark reaction increases. Various factors affect the closing and opening of stomata. When stomata are closed, the concentration of CO₂ falls down in the mesophyll tissue. This lowers down the rate of photosynthesis.',
        'کاربن ڈائی آکسائیڈ ضیائی تالیف کے خام مال میں سے ایک ہے۔ یہ گلوکوز کی تالیف کے لیے کاربن فراہم کرتی ہے۔ کاربن ڈائی آکسائیڈ کا ارتکاز بڑھنے سے تاریک تعامل کی شرح بڑھتی ہے۔ مختلف عوامل اسٹومیٹا کے کھلنے اور بند ہونے پر اثر انداز ہوتے ہیں۔ جب اسٹومیٹا بند ہوں تو میزوفل بافت میں CO₂ کا ارتکاز کم ہو جاتا ہے۔ اس سے ضیائی تالیف کی شرح کم ہو جاتی ہے۔',
        'کاربن ډای اکساید د فوتوسنتز له خامو موادو څخه دی. د ګلوکوز د جوړولو لپاره کاربن ورکوي. د کاربن ډای اکساید د غلظت په لوړېدو د تیارې د تعامل کچه زیاتېږي. بېلابېل عوامل د سټوماټا پر خلاصېدو او تړل کېدو اغېز کوي. کله چې سټوماټا تړلې وي، په میزوفیل نسج کې د CO₂ غلظت کمېږي. دا د فوتوسنتز کچه کموي.')
    s.callout(SI, [('Carbon dioxide is almost 0.03 percent in air. It is constantly removed from air by the autotrophs and is used in photosynthesis. This concentration of CO₂ almost remains constant in air because it is produced in respiration by all living organisms.', 'ہوا میں کاربن ڈائی آکسائیڈ تقریباً 0.03 فیصد ہے۔ آٹوٹرافس اسے مسلسل ہوا سے نکال کر ضیائی تالیف میں استعمال کرتے ہیں۔ ہوا میں CO₂ کا یہ ارتکاز تقریباً مستقل رہتا ہے کیونکہ یہ تمام جانداروں کے تنفس میں بنتی ہے۔', 'په هوا کې کاربن ډای اکساید شاوخوا 0.03 سلنه دی. اوټوټروفونه یې په دوامداره ډول له هوا اخلي او په فوتوسنتز کې یې کاروي. په هوا کې د CO₂ دا غلظت نږدې ثابت پاتې کېږي ځکه چې د ټولو ژوندیو موجوداتو په تنفس کې تولیدېږي.')])
    s.h('iii. Effect of Temperature', 'iii. درجۂ حرارت کا اثر', 'iii. د تودوخې اغېز')
    s.p('An optimum temperature is necessary for normal process of photosynthesis. Increase and decrease in temperature negatively affects the rate of photosynthesis. Generally a temperature, ranging between 20°C and 30°C is most suitable for photosynthesis. When temperature exceeds 30°C, the rate of photosynthesis lowers down. Similarly, at low temperature the rate declines and at freezing temperature it stops completely. However, plants growing in dry and hot localities and in cold regions have developed adaptations for high and low temperatures.',
        'ضیائی تالیف کے معمول کے عمل کے لیے موزوں ترین درجۂ حرارت ضروری ہے۔ درجۂ حرارت میں اضافہ اور کمی ضیائی تالیف کی شرح پر منفی اثر ڈالتے ہیں۔ عموماً 20°C اور 30°C کے درمیان درجۂ حرارت ضیائی تالیف کے لیے موزوں ترین ہے۔ جب درجۂ حرارت 30°C سے بڑھ جائے تو ضیائی تالیف کی شرح کم ہو جاتی ہے۔ اسی طرح کم درجۂ حرارت پر شرح گرتی ہے اور نقطۂ انجماد پر یہ مکمل طور پر رک جاتی ہے۔ تاہم خشک اور گرم علاقوں اور سرد علاقوں میں اگنے والے پودوں نے زیادہ اور کم درجۂ حرارت کے لیے موافقتیں پیدا کر لی ہیں۔',
        'د فوتوسنتز د عادي پروسې لپاره غوره تودوخه اړینه ده. د تودوخې زیاتوالی او کمښت د فوتوسنتز پر کچه منفي اغېز لري. عموماً د 20°C او 30°C ترمنځ تودوخه د فوتوسنتز لپاره تر ټولو مناسبه ده. کله چې تودوخه له 30°C زیاته شي، د فوتوسنتز کچه کمېږي. همدارنګه په ټیټه تودوخه کچه راټیټېږي او د کنګل په تودوخه کې بشپړ ودرېږي. خو په وچو او ګرمو سیمو او سړو سیمو کې شنه کېدونکو بوټو د لوړې او ټیټې تودوخې لپاره تطابقونه پیدا کړي دي.')
    s.callout(('Activity 7.1', 'سرگرمی 7.1', 'فعالیت 7.1'), [('• Design a model of light and dark reactions using low-cost materials.', '• کم قیمت اشیا سے روشنی اور تاریک تعاملات کا ماڈل بنائیں۔', '• په لږ لګښت موادو د رڼا او تیارې د تعاملونو ماډل جوړ کړئ.'),
                                                     ('• Demonstrate an experiment to show the process of photosynthesis using an aquatic plant, like Hydrilla.', '• ہائیڈریلا جیسے آبی پودے کے ذریعے ضیائی تالیف کا عمل دکھانے کے لیے تجربہ کریں۔', '• د هایډریلا په څېر د اوبو بوټي په کارولو د فوتوسنتز د پروسې د ښودلو لپاره تجربه وکړئ.'),
                                                     ('• Investigate the necessity for chlorophyll, light and carbon dioxide for photosynthesis, with experiments.', '• تجربات کے ذریعے ضیائی تالیف کے لیے کلوروفل، روشنی اور کاربن ڈائی آکسائیڈ کی ضرورت کی تحقیق کریں۔', '• د تجربو له لارې د فوتوسنتز لپاره د کلوروفیل، رڼا او کاربن ډای اکساید اړتیا وڅېړئ.')])
    out.append(s)

    s = Section('bio7_4', '7.4', 'Respiration', 'تنفس', 'تنفس', [141, 142, 143, 144, 145, 146])
    s.p('Respiration is defined as oxidation-reduction processes which occur inside the living cells during which organic food is broken down into carbon dioxide and water and energy is released. Glucose is the most common food used in this process. The purpose of respiration is to release energy for the living processes. Respiration is common to all living organisms because all of them need energy for life activities.',
        'تنفس کی تعریف تکسید و تخفیف کے وہ عوامل ہیں جو زندہ خلیوں کے اندر ہوتے ہیں جن کے دوران نامیاتی خوراک کاربن ڈائی آکسائیڈ اور پانی میں ٹوٹتی ہے اور توانائی خارج ہوتی ہے۔ گلوکوز اس عمل میں استعمال ہونے والی سب سے عام خوراک ہے۔ تنفس کا مقصد زندگی کے عوامل کے لیے توانائی خارج کرنا ہے۔ تنفس تمام جانداروں میں مشترک ہے کیونکہ سب کو زندگی کی سرگرمیوں کے لیے توانائی درکار ہے۔',
        'تنفس داسې تعریف کېږي: د اکسیډیشن-ریډکشن هغه پروسې چې د ژوندیو حجرو دننه کېږي او پکې عضوي خواړه په کاربن ډای اکساید او اوبو ماتېږي او انرژي خوشې کېږي. ګلوکوز په دې پروسه کې تر ټولو عام کارول کېدونکی خواړه دي. د تنفس موخه د ژوند پروسو لپاره د انرژۍ خوشې کول دي. تنفس په ټولو ژوندیو موجوداتو کې ګډ دی ځکه چې ټول د ژوند فعالیتونو لپاره انرژۍ ته اړتیا لري.')
    s.callout(SI, [('The term "cellular respiration" is used for the oxidation-reduction of food inside the cells. While the term "external respiration" or "brething" means the exchange of respiratory gases (CO₂ and O₂) between the organism and its environment.', 'اصطلاح ”خلوی تنفس“ خلیوں کے اندر خوراک کی تکسید و تخفیف کے لیے استعمال ہوتی ہے۔ جبکہ اصطلاح ”بیرونی تنفس“ یا ”سانس لینا“ سے مراد جاندار اور اس کے ماحول کے درمیان تنفسی گیسوں (CO₂ اور O₂) کا تبادلہ ہے۔', 'د ”حجروي تنفس“ اصطلاح د حجرو دننه د خوړو د اکسیډیشن-ریډکشن لپاره کارېږي. په داسې حال کې چې د ”بهرني تنفس“ یا ”ساه اخیستلو“ اصطلاح د ژوندي موجود او چاپېریال ترمنځ د تنفسي ګازونو (CO₂ او O₂) تبادله ده.')])
    s.h('7.4.1 Types of Respiration', '7.4.1 تنفس کی اقسام', '7.4.1 د تنفس ډولونه')
    s.p('Respiration is of two types: Anaerobic and Aerobic', 'تنفس دو اقسام کا ہے: غیر ہوائی اور ہوائی', 'تنفس دوه ډوله دی: غیر هوایي او هوایي')
    s.h('a. Anaerobic Respiration', 'a. غیر ہوائی تنفس', 'a. غیر هوایي تنفس')
    s.p('Anaerobic respiration (Fermentation) occurs in the absence of oxygen. It involves incomplete breakdown of organic food molecules and only a small amount of energy is released. It occurs in the cytoplasm of the cell. Anaerobic respiration is of two types; lactic acid fermentation and alcoholic fermentation.',
        'غیر ہوائی تنفس (فرمنٹیشن) آکسیجن کی عدم موجودگی میں ہوتا ہے۔ اس میں نامیاتی خوراک کے مالیکیولز کی نامکمل شکست ہوتی ہے اور صرف تھوڑی توانائی خارج ہوتی ہے۔ یہ خلیے کے سائٹوپلازم میں ہوتا ہے۔ غیر ہوائی تنفس دو اقسام کا ہے؛ لیکٹک ایسڈ فرمنٹیشن اور الکوحلک فرمنٹیشن۔',
        'غیر هوایي تنفس (تخمیر) د اکسیجن په نشتوالي کې کېږي. په دې کې د عضوي خوړو مالیکولونه نیمګړي ماتېږي او یوازې لږه انرژي خوشې کېږي. دا د حجرې په سایټوپلازم کې کېږي. غیر هوایي تنفس دوه ډوله دی؛ د لاکټیک اسید تخمیر او الکولي تخمیر.')
    s.h('i) Lactic Acid Fermentation', 'i) لیکٹک ایسڈ فرمنٹیشن', 'i) د لاکټیک اسید تخمیر')
    s.p('Lactic Acid Fermentation occurs in many microorganisms and also in the muscle cells of human beings when more energy is needed. It completes in two steps. Glycolysis is the first step in which glucose is broken down into two molecules of pyruvic acid and NAD is reduced to NADH. In the next step, Pyruvic acid is reduced by NADH into lactic acid. In the process, only two ATP molecules are produced from one glucose molecule.',
        'لیکٹک ایسڈ فرمنٹیشن بہت سے خرد جانداروں اور انسانوں کے عضلاتی خلیوں میں بھی اس وقت ہوتی ہے جب زیادہ توانائی کی ضرورت ہو۔ یہ دو مراحل میں مکمل ہوتی ہے۔ گلائکولائسس پہلا مرحلہ ہے جس میں گلوکوز پائروِک ایسڈ کے دو مالیکیولز میں ٹوٹتا ہے اور NAD تخفیف ہو کر NADH بنتا ہے۔ اگلے مرحلے میں NADH پائروِک ایسڈ کو لیکٹک ایسڈ میں تخفیف کرتا ہے۔ اس عمل میں ایک گلوکوز مالیکیول سے صرف دو ATP مالیکیول بنتے ہیں۔',
        'د لاکټیک اسید تخمیر په ډېرو مایکرو ژوندیو موجوداتو او د انسانانو په عضلي حجرو کې هم هغه وخت کېږي چې ډېرې انرژۍ ته اړتیا وي. په دوو پړاوونو بشپړېږي. ګلایکولیزس لومړی پړاو دی چې پکې ګلوکوز د پایرویک اسید په دوو مالیکولونو ماتېږي او NAD په NADH ریډیوس کېږي. په بل پړاو کې NADH پایرویک اسید په لاکټیک اسید ریډیوس کوي. په دې پروسه کې له یوه ګلوکوز مالیکول یوازې دوه ATP مالیکولونه جوړېږي.')
    s.callout(SI, [('Yoghurt is a dairy product produced by bacterial fermentation of milk. Fermentation of lactose produces lactic acid, which acts on milk protein to give yoghurt its texture and characteristic taste.', 'دہی دودھ کی بیکٹیریائی فرمنٹیشن سے بننے والی ڈیری پیداوار ہے۔ لیکٹوز کی فرمنٹیشن سے لیکٹک ایسڈ بنتا ہے جو دودھ کی پروٹین پر عمل کر کے دہی کو اس کی بناوٹ اور مخصوص ذائقہ دیتا ہے۔', 'مستې د شیدو د باکتریایي تخمیر له لارې جوړ شوی لبنیاتي محصول دی. د لاکټوز تخمیر لاکټیک اسید جوړوي چې د شیدو پر پروټین عمل کوي او مستو ته یې جوړښت او ځانګړی خوند ورکوي.')])
    s.fig('bio7-fig7-9', fermentation_fig(LA_EN), fermentation_fig(LA_UR), fermentation_fig(LA_PS), .6, caption=('Figure 7.9: Lactic acid Fermentation', 'شکل 7.9: لیکٹک ایسڈ فرمنٹیشن', 'شکل 7.9: د لاکټیک اسید تخمیر'))
    s.h('ii) Alcoholic Fermentation', 'ii) الکوحلک فرمنٹیشن', 'ii) الکولي تخمیر')
    s.p('It occurs in yeast and some bacteria. This type of anaerobic respiration is also completed in two steps: First step is glycolysis during which a glucose molecule is broken down into two molecules of pyruvic acid and NAD is reduced to NADH. In the next step, pyruvic acid is reduced by NADH to ethyl alcohol and CO₂. In alcoholic fermentation also two ATP molecules are produced from one glucose molecule.',
        'یہ خمیر اور بعض بیکٹیریا میں ہوتی ہے۔ غیر ہوائی تنفس کی یہ قسم بھی دو مراحل میں مکمل ہوتی ہے: پہلا مرحلہ گلائکولائسس ہے جس میں ایک گلوکوز مالیکیول پائروِک ایسڈ کے دو مالیکیولز میں ٹوٹتا ہے اور NAD تخفیف ہو کر NADH بنتا ہے۔ اگلے مرحلے میں NADH پائروِک ایسڈ کو ایتھائل الکوحل اور CO₂ میں تخفیف کرتا ہے۔ الکوحلک فرمنٹیشن میں بھی ایک گلوکوز مالیکیول سے دو ATP مالیکیول بنتے ہیں۔',
        'دا په خمیره او ځینو باکتریاوو کې کېږي. د غیر هوایي تنفس دا ډول هم په دوو پړاوونو بشپړېږي: لومړی پړاو ګلایکولیزس دی چې پکې یو ګلوکوز مالیکول د پایرویک اسید په دوو مالیکولونو ماتېږي او NAD په NADH ریډیوس کېږي. په بل پړاو کې NADH پایرویک اسید په ایتایل الکول او CO₂ ریډیوس کوي. په الکولي تخمیر کې هم له یوه ګلوکوز مالیکول دوه ATP مالیکولونه جوړېږي.')
    s.fig('bio7-fig7-10', fermentation_fig(AF_EN, True), fermentation_fig(AF_UR, True), fermentation_fig(AF_PS, True), .6, caption=('Figure 7.10: Alcoholic Fermentation', 'شکل 7.10: الکوحلک فرمنٹیشن', 'شکل 7.10: الکولي تخمیر'))
    s.p('SpaceBook note: Figures 7.9 and 7.10 print "Glucolysis" (for Glycolysis); the printed label is kept.', 'اسپیس بک نوٹ: شکل 7.9 اور 7.10 میں ”Glucolysis“ چھپا ہے (Glycolysis کے لیے)؛ چھپا لیبل رکھا گیا ہے۔', 'د سپېس بوک یادونه: شکل 7.9 او 7.10 ”Glucolysis“ چاپ کړی (د Glycolysis لپاره)؛ چاپ شوی لیبل ساتل شوی.', editorial=True)
    s.callout(SI, [('Yeast and some bacteria convert sugars into ethyl alcohol and carbon dioxide. During the fermentation process of bread, sugar is converted into alcohol and carbon dioxide. The carbon dioxide will form bubbles, which will be trapped by the gluten of the wheat causing the bread to rise. Because the bread fermentation takes a short period, only small amounts of alcohol are formed, most of which will evaporate during the bread baking process.', 'خمیر اور بعض بیکٹیریا شکر کو ایتھائل الکوحل اور کاربن ڈائی آکسائیڈ میں بدلتے ہیں۔ روٹی کی فرمنٹیشن کے دوران شکر الکوحل اور کاربن ڈائی آکسائیڈ میں بدلتی ہے۔ کاربن ڈائی آکسائیڈ بلبلے بناتی ہے جنہیں گندم کا گلوٹن روک لیتا ہے اور روٹی پھول جاتی ہے۔ چونکہ روٹی کی فرمنٹیشن تھوڑی دیر ہوتی ہے، اس لیے الکوحل کی معمولی مقدار بنتی ہے جس کا زیادہ تر حصہ پکاتے وقت بخارات بن کر اڑ جاتا ہے۔', 'خمیره او ځینې باکتریا بوره په ایتایل الکول او کاربن ډای اکساید بدلوي. د ډوډۍ د تخمیر پر مهال بوره په الکول او کاربن ډای اکساید بدلېږي. کاربن ډای اکساید پوکاڼي جوړوي چې د غنمو ګلوټن یې ساتي او ډوډۍ پړسېږي. ځکه چې د ډوډۍ تخمیر لنډ وخت نیسي، یوازې لږ الکول جوړېږي چې ډېره برخه یې د پخولو پر مهال تبخیرېږي.')])
    s.callout(STS, [('The practices of biotechnology are old and the human beings have used them since early history. Some of such practices include fermentation. Peoples have used grapes, berries, corn, rice, wheat, honey, potatoes, barley and other plant materials for fermentation. Various forms of alcohol are made for different purposes.', 'بائیو ٹیکنالوجی کے طریقے پرانے ہیں اور انسان ابتدائی تاریخ سے انہیں استعمال کرتا آیا ہے۔ ان میں سے بعض طریقوں میں فرمنٹیشن شامل ہے۔ لوگوں نے فرمنٹیشن کے لیے انگور، بیریز، مکئی، چاول، گندم، شہد، آلو، جو اور دیگر نباتاتی اشیا استعمال کیں۔ مختلف مقاصد کے لیے الکوحل کی مختلف اقسام بنائی جاتی ہیں۔', 'د بایوټکنالوژۍ کړنې زړې دي او انسانانو له لومړني تاریخ راهیسې کارولې دي. په دې کې تخمیر هم شامل دی. خلکو د تخمیر لپاره انګور، توتان، جوار، وريجې، غنم، شات، کچالو، اوربشې او نور نباتي مواد کارولي. د بېلابېلو موخو لپاره د الکول بېلابېل ډولونه جوړېږي.')])
    s.h('b. Aerobic Respiration', 'b. ہوائی تنفس', 'b. هوایي تنفس')
    s.p('Aerobic respiration needs free O₂. In aerobic respiration, organic food is completely broken down into CO₂ and H₂O and large amount of stored energy is released.', 'ہوائی تنفس کو آزاد O₂ درکار ہے۔ ہوائی تنفس میں نامیاتی خوراک مکمل طور پر CO₂ اور H₂O میں ٹوٹتی ہے اور ذخیرہ شدہ توانائی کی بڑی مقدار خارج ہوتی ہے۔', 'هوایي تنفس آزاد O₂ ته اړتیا لري. په هوایي تنفس کې عضوي خواړه په بشپړه توګه په CO₂ او H₂O ماتېږي او د زېرمه شوې انرژۍ ډېره اندازه خوشې کېږي.')
    s.lines([('C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + 36 ATP (net gain)', 'C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + 36 ATP (خالص حاصل)', 'C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + 36 ATP (خالصه ګټه)'),
             ('Glucose + Oxygen → Carbon dioxide + Water + 36 ATPs', 'گلوکوز + آکسیجن ← کاربن ڈائی آکسائیڈ + پانی + 36 ATP', 'ګلوکوز + اکسیجن ← کاربن ډای اکساید + اوبه + 36 ATP')])
    s.p('Aerobic Respiration completes in three steps:', 'ہوائی تنفس تین مراحل میں مکمل ہوتا ہے:', 'هوایي تنفس په درېیو پړاوونو بشپړېږي:')
    s.ol([('i. Glycolysis occurs in cytoplasm', 'i. گلائکولائسس سائٹوپلازم میں ہوتا ہے', 'i. ګلایکولیزس په سایټوپلازم کې کېږي'), ('ii. Krebs Cycle occurs in mitochondria', 'ii. کریبز سائیکل مائٹوکونڈریا میں ہوتا ہے', 'ii. کربس دوره په مایټوکونډریا کې کېږي'),
          ('iii. Electron transport chain also occurs in mitochondria', 'iii. الیکٹران ٹرانسپورٹ چین بھی مائٹوکونڈریا میں ہوتی ہے', 'iii. د الکترون لېږد زنځیر هم په مایټوکونډریا کې کېږي')])
    s.h('i) Glycolysis', 'i) گلائکولائسس', 'i) ګلایکولیزس')
    s.p('"Glyco" means glucose and "lysis" means splitting. Glycolysis is the breakdown of one glucose molecule (6 carbon compound) into two molecules of pyruvic acid (3 carbon compound). It takes place in the cytoplasm. In glycolysis, there is a net gain of two ATP molecules. Oxygen is not required for this process. That is why glycolysis occurs in both aerobic and anaerobic respiration.',
        '”گلائکو“ کا مطلب گلوکوز اور ”لائسس“ کا مطلب ٹوٹنا ہے۔ گلائکولائسس ایک گلوکوز مالیکیول (6 کاربن مرکب) کا پائروِک ایسڈ کے دو مالیکیولز (3 کاربن مرکب) میں ٹوٹنا ہے۔ یہ سائٹوپلازم میں ہوتا ہے۔ گلائکولائسس میں دو ATP مالیکیولز کا خالص حاصل ہوتا ہے۔ اس عمل کے لیے آکسیجن درکار نہیں۔ اسی لیے گلائکولائسس ہوائی اور غیر ہوائی دونوں تنفس میں ہوتا ہے۔',
        '”ګلایکو“ یعنې ګلوکوز او ”لیزس“ یعنې ماتېدل. ګلایکولیزس د یوه ګلوکوز مالیکول (6 کاربنه مرکب) د پایرویک اسید په دوو مالیکولونو (3 کاربنه مرکب) ماتېدل دي. دا په سایټوپلازم کې کېږي. په ګلایکولیزس کې د دوو ATP مالیکولونو خالصه ګټه وي. دې پروسې ته اکسیجن نه دی پکار. له همدې امله ګلایکولیزس په هوایي او غیر هوایي دواړو تنفسونو کې کېږي.')
    s.h('ii) Krebs Cycle', 'ii) کریبز سائیکل', 'ii) کربس دوره')
    s.p('This was discovered by a British scientist, Sir Hans Krebs and therefore named after his name as Krebs Cycle. It occurs in mitochondria where all the necessary enzymes are present.', 'یہ ایک برطانوی سائنس دان سر ہینز کریبز نے دریافت کیا اس لیے ان کے نام پر اسے کریبز سائیکل کہتے ہیں۔ یہ مائٹوکونڈریا میں ہوتا ہے جہاں تمام ضروری انزائمز موجود ہوتے ہیں۔', 'دا یو برتانوي ساینس پوه سر هانس کربس کشف کړه نو د هغه په نوم کربس دوره بلل کېږي. دا په مایټوکونډریا کې کېږي چېرته چې ټول اړین انزایمونه شته.')
    s.p('Before entering in Krebs cycle, pyruvic acids (generated in glycolysis) is changed into a 2-carbon compound called acetyl-Coenzyme A. It then goes through a series of reactions in which it is completely oxidised. These reactions produce CO₂ along with ATP. In these reactions, coenzymes NAD and FAD (Flavin Adenine Dinucleotide) are reduced to NADH and FADH₂ respectively.',
        'کریبز سائیکل میں داخل ہونے سے پہلے پائروِک ایسڈ (جو گلائکولائسس میں بنتا ہے) ایک 2 کاربن مرکب ایسیٹائل کو انزائم A میں بدل جاتا ہے۔ پھر یہ تعاملات کے ایک سلسلے سے گزرتا ہے جس میں مکمل تکسید ہو جاتی ہے۔ یہ تعاملات ATP کے ساتھ CO₂ بناتے ہیں۔ ان تعاملات میں کو انزائمز NAD اور FAD (فلیوِن ایڈینین ڈائی نیوکلیوٹائیڈ) بالترتیب NADH اور FADH₂ میں تخفیف ہوتے ہیں۔',
        'کربس دورې ته له ننوتلو مخکې پایرویک اسید (چې په ګلایکولیزس کې جوړېږي) په یوه 2 کاربنه مرکب ایسیټایل کو انزایم A بدلېږي. بیا د تعاملونو له یوې لړۍ تېرېږي چې پکې بشپړ اکسیډایز کېږي. دا تعاملونه له ATP سره CO₂ تولیدوي. په دې تعاملونو کې کو انزایمونه NAD او FAD (فلاوین اډینین ډای نیوکلیوټایډ) په ترتیب سره په NADH او FADH₂ ریډیوس کېږي.')
    s.h('iii) Electron Transport Chain', 'iii) الیکٹران ٹرانسپورٹ چین', 'iii) د الکترون لېږد زنځیر')
    s.p('The last step in aerobic respiration is the oxidation of reduced coenzymes (NADH and FADH₂) produced in glycolysis and Krebs cycle. It is done by using oxygen. During this step, two electrons are released from NADH and FADH₂. These electrons then pass along a series of electron carriers called cytochromes. During the transport from one cytochrome to the other, electrons lose energy. This energy is used to form ATP from ADP and Pi. At the end, the oxygen molecules accept electrons to form water.',
        'ہوائی تنفس کا آخری مرحلہ گلائکولائسس اور کریبز سائیکل میں بننے والے تخفیف شدہ کو انزائمز (NADH اور FADH₂) کی تکسید ہے۔ یہ آکسیجن کے استعمال سے ہوتی ہے۔ اس مرحلے میں NADH اور FADH₂ سے دو الیکٹران آزاد ہوتے ہیں۔ یہ الیکٹران پھر الیکٹران کیریئرز کے ایک سلسلے سے گزرتے ہیں جنہیں سائٹوکرومز کہتے ہیں۔ ایک سائٹوکروم سے دوسرے تک منتقلی کے دوران الیکٹران توانائی کھوتے ہیں۔ یہ توانائی ADP اور Pi سے ATP بنانے میں استعمال ہوتی ہے۔ آخر میں آکسیجن کے مالیکیول الیکٹران قبول کر کے پانی بناتے ہیں۔',
        'د هوایي تنفس وروستی پړاو په ګلایکولیزس او کربس دوره کې د جوړو شویو ریډیوس شویو کو انزایمونو (NADH او FADH₂) اکسیډیشن دی. دا د اکسیجن په کارولو کېږي. په دې پړاو کې له NADH او FADH₂ څخه دوه الکترونونه خوشې کېږي. دا الکترونونه بیا د الکترون وړونکو له یوې لړۍ تېرېږي چې سایټوکرومونه بلل کېږي. له یوه سایټوکروم بل ته د لېږد پر مهال الکترونونه انرژي له لاسه ورکوي. دا انرژي له ADP او Pi څخه د ATP د جوړولو لپاره کارېږي. په پای کې د اکسیجن مالیکولونه الکترونونه مني او اوبه جوړوي.')
    s.h('7.4.2 Energy Produced in Respiration', '7.4.2 تنفس میں پیدا ہونے والی توانائی', '7.4.2 په تنفس کې تولید شوې انرژي')
    s.p('The complete oxidation of one molecule of glucose into CO₂ and water generates 38 ATP. During glycolysis, two ATP molecules are also used. So there is net gain of 36 ATP from one glucose molecule. These ATP are generated step wise, some during glycolysis, some during Krebs cycle and many are generated during the electron transport chain.',
        'گلوکوز کے ایک مالیکیول کی CO₂ اور پانی میں مکمل تکسید سے 38 ATP بنتے ہیں۔ گلائکولائسس کے دوران دو ATP مالیکیول استعمال بھی ہوتے ہیں۔ اس لیے ایک گلوکوز مالیکیول سے 36 ATP کا خالص حاصل ہوتا ہے۔ یہ ATP مرحلہ وار بنتے ہیں، کچھ گلائکولائسس میں، کچھ کریبز سائیکل میں اور بہت سے الیکٹران ٹرانسپورٹ چین میں۔',
        'د ګلوکوز د یوه مالیکول بشپړ اکسیډیشن په CO₂ او اوبو 38 ATP تولیدوي. د ګلایکولیزس پر مهال دوه ATP مالیکولونه هم کارېږي. نو له یوه ګلوکوز مالیکول 36 ATP خالصه ګټه وي. دا ATP پړاو په پړاو جوړېږي، ځینې په ګلایکولیزس، ځینې په کربس دوره او ډېر یې د الکترون لېږد په زنځیر کې.')
    s.fig('bio7-fig7-11', *three(aerobic_fig, AR_EN, AR_UR, AR_PS), .8, caption=('Figure 7.11: Steps of Aerobic Respiration and Energy chart', 'شکل 7.11: ہوائی تنفس کے مراحل اور توانائی کا چارٹ', 'شکل 7.11: د هوایي تنفس پړاوونه او د انرژۍ چارټ'))
    s.table('bio7-tab7-1', ['Properties', 'Aerobic respiration', 'Anaerobic respiration'],
            [['Presence of Oxygen', 'Yes', 'No'], ['Number of ATP as net profit', '36', '02'], ['Final products', 'CO₂, H₂O', 'Lactic acid or Ethanol + CO₂'],
             ['Site of occurrence', 'Gycolysis in cytoplasm and Krebs cycle and electron transport chain in mitochondria', 'In cytoplasm'],
             ['Importance', 'Major source of energy for most organisms', '• Source of energy for anaerobic organisms • Source of energy for aerobic organisms in short supply of O₂ • Source of many useful products (ethanol, cheese etc)']],
            ['خصوصیات', 'ہوائی تنفس', 'غیر ہوائی تنفس'],
            [['آکسیجن کی موجودگی', 'ہاں', 'نہیں'], ['خالص منافع کے طور پر ATP کی تعداد', '36', '02'], ['آخری حاصلات', 'CO₂، H₂O', 'لیکٹک ایسڈ یا ایتھینول + CO₂'],
             ['وقوع کی جگہ', 'گلائکولائسس سائٹوپلازم میں اور کریبز سائیکل اور الیکٹران ٹرانسپورٹ چین مائٹوکونڈریا میں', 'سائٹوپلازم میں'],
             ['اہمیت', 'زیادہ تر جانداروں کے لیے توانائی کا بڑا ذریعہ', '• غیر ہوائی جانداروں کے لیے توانائی کا ذریعہ • O₂ کی کمی میں ہوائی جانداروں کے لیے توانائی کا ذریعہ • بہت سی مفید اشیا (ایتھینول، پنیر وغیرہ) کا ذریعہ']],
            ['ځانګړتیاوې', 'هوایي تنفس', 'غیر هوایي تنفس'],
            [['د اکسیجن شتون', 'هو', 'نه'], ['د خالصې ګټې په توګه د ATP شمېر', '36', '02'], ['وروستي محصولات', 'CO₂، H₂O', 'لاکټیک اسید یا ایتانول + CO₂'],
             ['د پېښېدو ځای', 'ګلایکولیزس په سایټوپلازم او کربس دوره او د الکترون لېږد زنځیر په مایټوکونډریا کې', 'په سایټوپلازم کې'],
             ['اهمیت', 'د ډېری ژوندیو موجوداتو لپاره د انرژۍ لویه سرچینه', '• د غیر هوایي موجوداتو لپاره د انرژۍ سرچینه • د O₂ په کمښت کې د هوایي موجوداتو لپاره د انرژۍ سرچینه • د ډېرو ګټورو محصولاتو (ایتانول، پنیر او نور) سرچینه']],
            ratio=1, caption=('TABLE 7.1: Difference between aerobic and anaerobic respiration', 'جدول 7.1: ہوائی اور غیر ہوائی تنفس میں فرق', 'جدول 7.1: د هوایي او غیر هوایي تنفس توپیر'))
    s.callout(('Activity 7.2:', 'سرگرمی 7.2:', 'فعالیت 7.2:'), [('Investigate the release of carbon dioxide during aerobic respiration in germinating seeds.', 'اگتے ہوئے بیجوں میں ہوائی تنفس کے دوران کاربن ڈائی آکسائیڈ کے اخراج کی تحقیق کریں۔', 'په ټوکېدونکو تخمونو کې د هوایي تنفس پر مهال د کاربن ډای اکساید خوشې کېدل وڅېړئ.')])
    out.append(s)

    s = Section('bio7_5', '7.5', 'Comparison between Photosynthesis and Respiration', 'ضیائی تالیف اور تنفس کا موازنہ', 'د فوتوسنتز او تنفس پرتله', [146])
    s.p('Photosynthesis and respiration are two important processes in the living world. Both of these processes are the opposite of one another. No life on the planet Earth would be possible without any one of these processes. A comparison of both of these processes is given below:',
        'ضیائی تالیف اور تنفس جانداروں کی دنیا کے دو اہم عوامل ہیں۔ یہ دونوں عوامل ایک دوسرے کے الٹ ہیں۔ ان میں سے کسی ایک کے بغیر کرۂ ارض پر زندگی ممکن نہ ہوتی۔ ان دونوں عوامل کا موازنہ ذیل میں دیا گیا ہے:',
        'فوتوسنتز او تنفس د ژوندۍ نړۍ دوه مهمې پروسې دي. دا دواړه پروسې یو د بل برعکس دي. د دې هرې یوې پروسې پرته پر ځمکه ژوند ممکن نه و. د دې دواړو پروسو پرتله لاندې ورکړل شوې:')
    rows_en = [['It is an energy storing process.', 'It is an energy releasing process.'],
               ['Energy of sunlight is trapped by the chlorophyll and converted into chemical energy and stored in organic food molecules.', 'Stored energy of food molecules is released for cellular activities.'],
               ['Carbon dioxide and water are used as raw materials while glucose and oxygen are the products.', 'Glucose and oxygen are the raw materials while carbon dioxide and water are the products.'],
               ['Oxygen is liberated as by product.', 'Oxygen is required in aerobic respiration'],
               ['It takes place only in green cells of plants, algae and some bacteria.', 'It takes place in all the cells of all living organisms.'],
               ['It is constructive (anabolic) process during which organic food molecules are synthesized and energy is stored.', 'It is a destructive (catabolic) process during which organic food molecules are broken down and energy is released.'],
               ['Due to photosynthesis plant body gains weight.', 'Due to respiration loss of weight occurs.'],
               ['It occurs only during day time when sunlight is available which is necessary for it.', 'It occurs round the clock, day and night. It does not require sunlight.']]
    rows_ur = [['یہ توانائی ذخیرہ کرنے والا عمل ہے۔', 'یہ توانائی خارج کرنے والا عمل ہے۔'], ['سورج کی روشنی کی توانائی کلوروفل جذب کر کے کیمیائی توانائی میں بدلتا اور نامیاتی خوراک کے مالیکیولز میں ذخیرہ کرتا ہے۔', 'خوراک کے مالیکیولز کی ذخیرہ شدہ توانائی خلوی سرگرمیوں کے لیے خارج ہوتی ہے۔'],
               ['کاربن ڈائی آکسائیڈ اور پانی خام مال کے طور پر استعمال ہوتے ہیں جبکہ گلوکوز اور آکسیجن حاصلات ہیں۔', 'گلوکوز اور آکسیجن خام مال ہیں جبکہ کاربن ڈائی آکسائیڈ اور پانی حاصلات ہیں۔'], ['آکسیجن ضمنی پیداوار کے طور پر خارج ہوتی ہے۔', 'ہوائی تنفس میں آکسیجن درکار ہے'],
               ['یہ صرف پودوں، الجی اور بعض بیکٹیریا کے سبز خلیوں میں ہوتا ہے۔', 'یہ تمام جانداروں کے تمام خلیوں میں ہوتا ہے۔'], ['یہ تعمیری (اینابولک) عمل ہے جس میں نامیاتی خوراک کے مالیکیول بنتے اور توانائی ذخیرہ ہوتی ہے۔', 'یہ تخریبی (کیٹابولک) عمل ہے جس میں نامیاتی خوراک کے مالیکیول ٹوٹتے اور توانائی خارج ہوتی ہے۔'],
               ['ضیائی تالیف سے پودے کا وزن بڑھتا ہے۔', 'تنفس سے وزن کم ہوتا ہے۔'], ['یہ صرف دن کے وقت ہوتا ہے جب سورج کی روشنی دستیاب ہو جو اس کے لیے ضروری ہے۔', 'یہ دن رات چوبیس گھنٹے ہوتا ہے۔ اسے سورج کی روشنی درکار نہیں۔']]
    rows_ps = [['دا د انرژۍ زېرمه کوونکې پروسه ده.', 'دا د انرژۍ خوشې کوونکې پروسه ده.'], ['د لمر رڼا انرژي کلوروفیل نیسي، په کیمیاوي انرژۍ یې بدلوي او په عضوي خوړو مالیکولونو کې یې زېرمه کوي.', 'د خوړو د مالیکولونو زېرمه شوې انرژي د حجروي فعالیتونو لپاره خوشې کېږي.'],
               ['کاربن ډای اکساید او اوبه د خامو موادو په توګه کارېږي او ګلوکوز او اکسیجن محصولات دي.', 'ګلوکوز او اکسیجن خام مواد دي او کاربن ډای اکساید او اوبه محصولات دي.'], ['اکسیجن د فرعي محصول په توګه خوشې کېږي.', 'په هوایي تنفس کې اکسیجن ته اړتیا ده'],
               ['دا یوازې د بوټو، الجي او ځینو باکتریاوو په شنو حجرو کې کېږي.', 'دا د ټولو ژوندیو موجوداتو په ټولو حجرو کې کېږي.'], ['دا جوړوونکې (انابولیک) پروسه ده چې پکې عضوي خواړه جوړېږي او انرژي زېرمه کېږي.', 'دا ویجاړوونکې (کټابولیک) پروسه ده چې پکې عضوي خواړه ماتېږي او انرژي خوشې کېږي.'],
               ['د فوتوسنتز له امله د بوټي وزن زیاتېږي.', 'د تنفس له امله وزن کمېږي.'], ['دا یوازې د ورځې کېږي کله چې د لمر رڼا شته وي چې ورته اړینه ده.', 'دا شپه او ورځ کېږي. د لمر رڼا ته اړتیا نه لري.']]
    s.table('bio7-tab7-2', ['Photosynthesis', 'Respiration'], rows_en, ['ضیائی تالیف', 'تنفس'], rows_ur, ['فوتوسنتز', 'تنفس'], rows_ps, ratio=1,
            caption=('Table 7.2 Comparison between photosynthesis and respiration', 'جدول 7.2 ضیائی تالیف اور تنفس کا موازنہ', 'جدول 7.2 د فوتوسنتز او تنفس پرتله'))
    out.append(s)
    return out


KEY_POINTS = [
    ('Bioenergetics is the study of energy relationships and energy conversions in organisms.', 'بائیو انرجیٹکس جانداروں میں توانائی کے تعلقات اور تبدیلیوں کا مطالعہ ہے۔', 'بایوانرژیټیک په ژوندیو موجوداتو کې د انرژۍ د اړیکو او بدلونونو مطالعه ده.'),
    ('Oxidation is defined as the loss of hydrogen or electrons while reduction is the opposite of oxidation in which hydrogen or electrons are gained.', 'تکسید ہائیڈروجن یا الیکٹرانز کا ضیاع ہے جبکہ تخفیف اس کا الٹ ہے جس میں ہائیڈروجن یا الیکٹرانز حاصل ہوتے ہیں۔', 'اکسیډیشن د هایدروجن یا الکترونونو له لاسه ورکول دي او ریډکشن یې برعکس دی چې پکې هایدروجن یا الکترونونه ترلاسه کېږي.'),
    ('In living cells, energy is provided by Adenosine Tri Phosphate (ATP).', 'زندہ خلیوں میں توانائی ایڈینوسین ٹرائی فاسفیٹ (ATP) فراہم کرتا ہے۔', 'په ژوندیو حجرو کې انرژي اډینوزین ټرای فاسفېټ (ATP) ورکوي.'),
    ('When a cell needs energy, one bond between phosphate groups of ATP is broken to release 7.3 kcal (7,300 calories) energy.', 'جب خلیے کو توانائی چاہیے تو ATP کے فاسفیٹ گروپس کے درمیان ایک بانڈ ٹوٹ کر 7.3 kcal (7,300 کیلوریز) توانائی خارج کرتا ہے۔', 'کله چې حجره انرژۍ ته اړتیا ولري، د ATP د فاسفېټ ګروپونو ترمنځ یوه اړیکه ماتېږي او 7.3 kcal (7,300 کالورۍ) انرژي خوشې کوي.'),
    ('Photosynthesis is the manufacturing of organic food (glucose) in the presence of chlorophyll, using CO₂, water and sunlight and releasing oxygen as a by-product.', 'ضیائی تالیف کلوروفل کی موجودگی میں CO₂، پانی اور سورج کی روشنی سے نامیاتی خوراک (گلوکوز) بنانا اور ضمنی پیداوار کے طور پر آکسیجن خارج کرنا ہے۔', 'فوتوسنتز د کلوروفیل په شتون کې د CO₂، اوبو او لمر رڼا په کارولو د عضوي خوړو (ګلوکوز) جوړول او د فرعي محصول په توګه د اکسیجن خوشې کول دي.'),
    ('Photosynthesis occurs in autotrophic organisms (plants, algae, and some bacteria).', 'ضیائی تالیف آٹوٹرافک جانداروں (پودوں، الجی اور بعض بیکٹیریا) میں ہوتی ہے۔', 'فوتوسنتز په اوټوټروفیکو موجوداتو (بوټو، الجي او ځینو باکتریاوو) کې کېږي.'),
    ('Chlorophyll absorbs sunlight (blue and red portion) and converts it into chemical energy for the formation of carbohydrates (glucose).', 'کلوروفل سورج کی روشنی (نیلا اور سرخ حصہ) جذب کر کے کاربوہائیڈریٹس (گلوکوز) بنانے کے لیے کیمیائی توانائی میں بدلتا ہے۔', 'کلوروفیل د لمر رڼا (آبي او سره برخه) جذبوي او د کاربوهایډریټونو (ګلوکوز) د جوړولو لپاره یې په کیمیاوي انرژۍ بدلوي.'),
    ('Photosynthesis is completed in two steps. During light reactions chlorophyll molecules absorb light. Their high energy electrons are used to produce ATP. During dark reactions, CO₂ molecules are reduced to make carbohydrates by using ATP and NADPH.', 'ضیائی تالیف دو مراحل میں مکمل ہوتی ہے۔ روشنی کے تعاملات میں کلوروفل مالیکیول روشنی جذب کرتے ہیں۔ ان کے زیادہ توانائی والے الیکٹران ATP بنانے میں استعمال ہوتے ہیں۔ تاریک تعاملات میں ATP اور NADPH کے استعمال سے CO₂ کے مالیکیول تخفیف ہو کر کاربوہائیڈریٹس بناتے ہیں۔', 'فوتوسنتز په دوو پړاوونو بشپړېږي. د رڼا په تعاملونو کې د کلوروفیل مالیکولونه رڼا جذبوي. لوړ انرژي لرونکي الکترونونه یې د ATP په جوړولو کې کارېږي. د تیارې په تعاملونو کې د ATP او NADPH په کارولو د CO₂ مالیکولونه ریډیوس کېږي او کاربوهایډریټونه جوړوي.'),
    ('Any environmental factor whose absence or deficiency can decrease the rate of a metabolic reaction, is called a limiting factor for that reaction.', 'کوئی بھی ماحولیاتی عامل جس کی عدم موجودگی یا کمی کسی میٹابولک تعامل کی شرح کم کر سکے، اس تعامل کا محدود کرنے والا عامل کہلاتا ہے۔', 'هر چاپېریالي عامل چې نشتوالی یا کمښت یې د میټابولیکي تعامل کچه کمولای شي، د هغه تعامل محدودوونکی عامل بلل کېږي.'),
    ('Respiration is defined as the oxidation-reduction process which occurs inside the living cells. During respiration, organic food is broken down into carbon dioxide and water and energy is released.', 'تنفس زندہ خلیوں کے اندر ہونے والا تکسید و تخفیف کا عمل ہے۔ تنفس کے دوران نامیاتی خوراک کاربن ڈائی آکسائیڈ اور پانی میں ٹوٹتی ہے اور توانائی خارج ہوتی ہے۔', 'تنفس د ژوندیو حجرو دننه د اکسیډیشن-ریډکشن پروسه ده. د تنفس پر مهال عضوي خواړه په کاربن ډای اکساید او اوبو ماتېږي او انرژي خوشې کېږي.'),
    ('Anaerobic respiration occurs in the absence of oxygen. It involves incomplete breakdown of organic food molecules and only a small amount of energy is released.', 'غیر ہوائی تنفس آکسیجن کی عدم موجودگی میں ہوتا ہے۔ اس میں نامیاتی خوراک کی نامکمل شکست ہوتی ہے اور صرف تھوڑی توانائی خارج ہوتی ہے۔', 'غیر هوایي تنفس د اکسیجن په نشتوالي کې کېږي. په دې کې عضوي خواړه نیمګړي ماتېږي او یوازې لږه انرژي خوشې کېږي.'),
    ('During lactic acid fermentation glucose is broken down into two molecules of pyruvic acid and then each pyruvic acid is reduced into lactic acid.', 'لیکٹک ایسڈ فرمنٹیشن میں گلوکوز پائروِک ایسڈ کے دو مالیکیولز میں ٹوٹتا ہے اور پھر ہر پائروِک ایسڈ لیکٹک ایسڈ میں تخفیف ہوتا ہے۔', 'د لاکټیک اسید په تخمیر کې ګلوکوز د پایرویک اسید په دوو مالیکولونو ماتېږي او بیا هر پایرویک اسید په لاکټیک اسید ریډیوس کېږي.'),
    ('During alcoholic fermentation glucose is broken down into two molecules of pyruvic acid and then each pyruvic acid is reduced to ethyl alcohol and CO₂.', 'الکوحلک فرمنٹیشن میں گلوکوز پائروِک ایسڈ کے دو مالیکیولز میں ٹوٹتا ہے اور پھر ہر پائروِک ایسڈ ایتھائل الکوحل اور CO₂ میں تخفیف ہوتا ہے۔', 'په الکولي تخمیر کې ګلوکوز د پایرویک اسید په دوو مالیکولونو ماتېږي او بیا هر پایرویک اسید په ایتایل الکول او CO₂ ریډیوس کېږي.'),
    ('Aerobic Respiration completes in three steps i.e. glycolysis, Krebs cycle and electron transport chain.', 'ہوائی تنفس تین مراحل یعنی گلائکولائسس، کریبز سائیکل اور الیکٹران ٹرانسپورٹ چین میں مکمل ہوتا ہے۔', 'هوایي تنفس په درېیو پړاوونو یعنې ګلایکولیزس، کربس دوره او د الکترون لېږد زنځیر کې بشپړېږي.'),
    ('Glycolysis is the breakdown of one glucose molecule into two molecules of pyruvic acid. It changes into acetyl-CoA. In Krebs cycle, acetyl CoA is completely oxidized.', 'گلائکولائسس ایک گلوکوز مالیکیول کا پائروِک ایسڈ کے دو مالیکیولز میں ٹوٹنا ہے۔ یہ ایسیٹائل CoA میں بدلتا ہے۔ کریبز سائیکل میں ایسیٹائل CoA کی مکمل تکسید ہوتی ہے۔', 'ګلایکولیزس د یوه ګلوکوز مالیکول د پایرویک اسید په دوو مالیکولونو ماتېدل دي. دا په ایسیټایل CoA بدلېږي. په کربس دوره کې ایسیټایل CoA بشپړ اکسیډایز کېږي.'),
    ('In the electron transport chain, electrons pass along a series of electron carriers (cytochromes) and lose energy. This energy is used to form ATP.', 'الیکٹران ٹرانسپورٹ چین میں الیکٹران کیریئرز (سائٹوکرومز) کے سلسلے سے گزرتے اور توانائی کھوتے ہیں۔ یہ توانائی ATP بنانے میں استعمال ہوتی ہے۔', 'د الکترون لېږد په زنځیر کې الکترونونه د الکترون وړونکو (سایټوکرومونو) له لړۍ تېرېږي او انرژي له لاسه ورکوي. دا انرژي د ATP په جوړولو کې کارېږي.'),
    ('In the complete oxidation of one molecule of glucose into CO₂ and water, the net gain is 36 ATPs.', 'گلوکوز کے ایک مالیکیول کی CO₂ اور پانی میں مکمل تکسید میں خالص حاصل 36 ATP ہے۔', 'د ګلوکوز د یوه مالیکول په بشپړ اکسیډیشن په CO₂ او اوبو کې خالصه ګټه 36 ATP ده.'),
]

NOTE = 'SpaceBook answer — the textbook prints no answer key for this exercise.'
MCQS = [
    ('i. The site of the cell for the dark reaction is:', ['Mitochondria', 'Ribosome', 'Granum of chloroplast', 'Stroma of chloroplast'], 3, NOTE),
    ('ii. The organisms responsible for trapping light energy are:', ['Plants', 'Algae', 'Photosynthetic organisms', 'Fungi'], 2, NOTE + ' Options c and d are printed in the order "d. Fungi, c. Photosynthetic organisms".'),
    ('iii. Photosynthesis takes place in:', ['Mesophyll cells', 'Guard cells', 'Phloem cells', 'All of the above'], 0, NOTE + ' Mesophyll cells are the main photosynthetic cells; guard cells also contain chloroplasts.'),
    ('iv. One of the following is not a limiting factor for enzymes in photosynthesis:', ['CO₂ concentration', 'Temperature', 'Light intensity', 'Pigments'], 3, NOTE),
    ('v. One of the following pair of light colours is important for photosynthesis:', ['Green and yellow', 'Yellow and orange', 'Green and orange', 'Red and blue'], 3, NOTE),
    ('vi. One of the following may not be required for respiration:', ['Oxygen', 'Food molecule', 'Enzymes', 'CO₂'], 3, NOTE + ' Oxygen is not needed in anaerobic respiration, but CO₂ is a product, not a requirement.'),
    ('vii. In the structure of ATP, the three phosphate groups are linked to:', ['Ribose', 'Glucose', 'Adenine', 'H₂O'], 0, NOTE),
    ('viii. A car engine uses fuel for work to do. To carry out functions, a living cell uses:', ['Electric power', 'Generator', 'ATP', 'Heat energy'], 2, NOTE),
    ('ix. Inside a bacterial cell, glycolysis occurs in:', ['Mesosome', 'Cytoplasm', 'Mitochondria', 'Nucleoid'], 1, NOTE),
    ('x. The consumption during the conversion of pyruivic acid into ethanol during anaerobic respiration is / are:', ['one NADH', 'one NADH and CO₂', 'two NADH', 'only CO₂'], 0, NOTE + ' Each pyruvic acid is reduced by one NADH; CO₂ is released, not consumed.'),
]
SQ = ['i. Why is ATP regarded as the currency of the living cell?', 'ii. What is the role of pigments during photosynthesis?', 'iii. Draw the structure of ATP molecule.',
      'iv. Compare lactic acid fermentation with alcoholic fermentation.', 'v. Why are oxidation and reduction important for plants?']
LQ = ['i. Explain the mechanism of photosynthesis.', 'ii. What is the concept of a limiting factor? What are the different limiting factors for photosynthesis?',
      'iii. Why is aerobic respiration considered to be more efficient than anaerobic respiration?', 'iv. Aerobic respiration generates more ATP molecules than anaerobic process. Which processes of aerobic respiration are responsible for this higher generation of ATP and how?']
LAB = 'SpaceBook-authored answer based on this unit (the textbook prints no answers):\n'
SQ_ANS = ['ATP provides energy to all living cells for activities such as protein synthesis, cell division and growth. Cells make ATP to store energy and break it to get energy (7.3 kcal per bond), so it works like money that is earned and spent.',
          'Chlorophyll-a (main pigment) and accessory pigments (chlorophyll-b, carotenoids) in photosystems absorb mainly blue and red light; their excited electrons provide energy to make ATP and NADPH in the light reactions.',
          'See Figure 7.2: three phosphate groups joined by two high-energy bonds, attached to ribose sugar, which is attached to the nitrogenous base adenine.',
          'Both occur without oxygen, in the cytoplasm, begin with glycolysis and give 2 ATP per glucose. Lactic acid fermentation (many microorganisms, human muscle cells) reduces pyruvic acid to lactic acid. Alcoholic fermentation (yeast, some bacteria) reduces pyruvic acid to ethyl alcohol and CO₂.',
          'Photosynthesis and respiration are oxidation-reduction processes. Through them plants store energy in food (photosynthesis) and release it for cellular work (respiration); without redox reactions energy could neither be stored nor released.']
LQ_ANS = ['Two steps. Light reactions (granum): chlorophyll absorbs light, excited electrons make ATP from ADP and Pi; water is split, O₂ is released and hydrogen reduces NADP to NADPH. Dark reactions/Calvin cycle (stroma): CO₂ is reduced to glucose using energy from ATP and hydrogen from NADPH (Figures 7.6-7.8).',
          'A limiting factor is any environmental factor whose absence or deficiency decreases the rate of a metabolic reaction. For photosynthesis: light intensity (too weak gives low energy, too intense damages chlorophyll), CO₂ concentration (about 0.03% in air; closed stomata lower it), temperature (best 20-30°C) and availability of water.',
          'Aerobic respiration breaks glucose completely into CO₂ and water and gives a net 36 ATP per glucose, while anaerobic respiration breaks it incompletely and gives only 2 ATP (Table 7.1).',
          'Krebs cycle and the electron transport chain in mitochondria. The Krebs cycle completely oxidises acetyl CoA, producing ATP and reduced coenzymes NADH and FADH₂. In the electron transport chain, electrons from NADH and FADH₂ pass along cytochromes, losing energy that forms ATP; oxygen accepts the electrons forming water. Most ATP (Figure 7.11) is made here.']


def keypoints_section():
    s = Section('bio7_keypoints', 'Key Points', 'Key Points', 'اہم نکات', 'مهم ټکي', [147])
    s.ul(KEY_POINTS)
    return s


def exercise():
    return dict(sourcePdfPages=[148, 149], sourcePrintedPages=[145, 146], heading='A. Encircle the best suitable answers.',
                mcqs=[dict(q=q, options=o, correct=c, explanation=e, answerOrigin='SpaceBook') for q, o, c, e in MCQS],
                shortQuestions=[dict(q=q, answer=LAB + a, sourceSection='B. Give short answers for the following questions.') for q, a in zip(SQ, SQ_ANS)],
                detailedQuestions=[dict(q=q, answer=LAB + a, sourceSection='C. Give detailed answers for the following questions') for q, a in zip(LQ, LQ_ANS)],
                activities=[dict(title='Activity 7.1', desc='Design a model of light and dark reactions using low-cost materials. Demonstrate an experiment to show the process of photosynthesis using an aquatic plant, like Hydrilla. Investigate the necessity for chlorophyll, light and carbon dioxide for photosynthesis, with experiments.', sourcePrintedPage=138),
                            dict(title='Activity 7.2', desc='Investigate the release of carbon dioxide during aerobic respiration in germinating seeds.', sourcePrintedPage=143)])
