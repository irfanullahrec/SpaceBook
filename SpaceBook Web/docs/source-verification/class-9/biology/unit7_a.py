# -*- coding: utf-8 -*-
"""Unit 7 part A — PDF 132-137 (printed 129-134): SLOs, 7.1 bioenergetics, redox, ATP, 7.2 photosynthesis, 7.2.1."""
from bio9_tools import Section, svg_wrap, txt
from unit4_figs import multiline
from unit4_figs2 import pointer, chloroplast_fig

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')
STS = ('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه')


def box(x, y, w, h, fill, lines, size=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>' + multiline(x + w / 2, y + h / 2 + 4 - (len(lines) - 1) * 7, lines, 'middle', size)


def redox_fig(L):
    b = ['<path d="M400,110 Q260,10 110,110" stroke="#333" stroke-width="3" fill="none"/><polygon points="112,100 100,118 122,116" fill="#333"/>',
         '<path d="M110,150 Q260,250 400,150" stroke="#333" stroke-width="3" fill="none"/><polygon points="398,160 410,142 388,144" fill="#333"/>']
    b.append(box(40, 112, 70, 36, '#fff176', [L['glucose']]) + txt(122, 135, '+', 14, 'middle', 'bold') + box(135, 112, 70, 36, '#fff176', [L['oxygen']]))
    b.append(box(370, 108, 70, 44, '#fff176', L['co2']) + txt(452, 135, '+', 14, 'middle', 'bold') + box(462, 112, 60, 36, '#fff176', [L['water']]))
    b.append(box(440, 30, 70, 30, '#f48fb1', [L['energy']]) + '<path d="M440,45 L340,55" stroke="#e91e63" stroke-width="2"/><polygon points="340,49 330,56 342,61" fill="#e91e63"/>')
    b.append(box(440, 200, 70, 30, '#f48fb1', [L['energy']]) + '<path d="M370,205 L438,214" stroke="#e91e63" stroke-width="2"/><polygon points="436,208 446,215 434,220" fill="#e91e63"/>')
    b.append(txt(260, 22, L['redox'], 12, 'middle', 'bold') + txt(260, 50, L['ps'], 12, 'middle', 'bold') + txt(260, 220, L['resp'], 12, 'middle', 'bold') + txt(260, 250, L['redox'], 12, 'middle', 'bold'))
    return svg_wrap(''.join(b), 540, 265, L['title'])


RX_EN = dict(title='Figure 7.1: Importance of Oxidation-Reduction Reactions', glucose='Glucose', oxygen='Oxygen', co2=['Carbon', 'dioxide'], water='Water', energy='Energy', redox='Oxidation - Reduction', ps='Photosynthesis', resp='Respiration')
RX_UR = dict(title='شکل 7.1', glucose='گلوکوز', oxygen='آکسیجن', co2=['کاربن', 'ڈائی آکسائیڈ'], water='پانی', energy='توانائی', redox='تکسید - تخفیف', ps='ضیائی تالیف', resp='تنفس')
RX_PS = dict(title='شکل 7.1', glucose='ګلوکوز', oxygen='اکسیجن', co2=['کاربن', 'ډای اکساید'], water='اوبه', energy='انرژي', redox='اکسیډیشن - ریډکشن', ps='فوتوسنتز', resp='تنفس')


def atp_molecule(x, y, n=3, scale=1.0):
    b = [f'<g transform="translate({x},{y}) scale({scale})">']
    for i in range(n):
        b.append(f'<circle cx="{i*34}" cy="0" r="12" fill="#fff176" stroke="#f9a825"/>' + txt(i * 34, 4, 'P', 11, 'middle', 'bold'))
        if i < n - 1:
            b.append(f'<path d="M{i*34+12},0 q5,-6 10,0" stroke="#333" fill="none" stroke-width="2"/>')
    b.append(f'<path d="M{(n-1)*34+12},0 h30 v20" stroke="#333" stroke-width="2" fill="none"/>')
    b.append(f'<polygon points="{(n-1)*34+40},20 {(n-1)*34+75},5 {(n-1)*34+110},20 {(n-1)*34+97},60 {(n-1)*34+53},60" fill="#ec407a" stroke="#ad1457"/>')
    b.append(f'<polygon points="{(n-1)*34+105},10 {(n-1)*34+125},-20 {(n-1)*34+160},-20 {(n-1)*34+170},5 {(n-1)*34+150},25 {(n-1)*34+120},25" fill="#64b5f6" stroke="#1565c0"/>')
    b.append(f'<polygon points="{(n-1)*34+125},-20 {(n-1)*34+140},-55 {(n-1)*34+175},-55 {(n-1)*34+190},-25 {(n-1)*34+160},-20" fill="#4fc3f7" stroke="#1565c0"/>')
    b.append('</g>')
    return ''.join(b)


def atp_fig(L):
    b = [atp_molecule(60, 140)]
    b.append(txt(95, 100, L['phosphate'], 12, 'middle', 'bold') + '<path d="M78,155 L95,185 L112,155" stroke="#333" fill="none"/>' + multiline(95, 200, L['bonds'], 'middle'))
    b.append(txt(193, 185, L['ribose'], 12, 'middle', 'bold') + txt(320, 105, L['adenine'], 12, 'start', 'bold') + txt(300, 60, 'NH₂', 11))
    return svg_wrap(''.join(b), 420, 230, L['title'])


AT_EN = dict(title='Figure 7.2: Structural formula of an ATP molecule', phosphate='Phosphate groups', bonds=['High energy', 'bonds'], ribose='Ribose', adenine='Adenine')
AT_UR = dict(title='شکل 7.2', phosphate='فاسفیٹ گروپس', bonds=['زیادہ توانائی', 'والے بانڈ'], ribose='رائبوز', adenine='ایڈینین')
AT_PS = dict(title='شکل 7.2', phosphate='فاسفېټ ګروپونه', bonds=['لوړې انرژۍ', 'اړیکې'], ribose='رایبوز', adenine='اډینین')


def atp_breakdown(L):
    b = [txt(270, 20, 'ATP + H₂O → ADP + Pi + 7.3 Kcal', 15, 'middle', 'bold')]
    b.append('<rect x="20" y="35" width="230" height="160" fill="#e3f2fd" stroke="#333"/><rect x="290" y="35" width="230" height="160" fill="#e3f2fd" stroke="#333"/>')
    b.append(atp_molecule(40, 110, 3, .75) + atp_molecule(345, 110, 2, .75) + '<circle cx="320" cy="100" r="9" fill="#fff176" stroke="#f9a825"/>' + txt(320, 104, 'Pi', 9, 'middle', 'bold') + txt(333, 104, '+', 12))
    b.append(txt(135, 185, L['atp'], 11, 'middle', 'bold') + txt(405, 185, L['adp'], 11, 'middle', 'bold'))
    b.append('<path d="M250,170 h35" stroke="#333" stroke-width="3"/><polygon points="285,164 295,170 285,176" fill="#333"/>' + txt(268, 160, L['water'], 10, 'middle', 'bold'))
    b.append('<ellipse cx="555" cy="110" rx="32" ry="16" fill="#fff176"/>' + txt(555, 114, L['energy'], 11, 'middle', 'bold') + txt(523, 114, '+', 12))
    return svg_wrap(''.join(b), 600, 210, L['title'])


AB_EN = dict(title='Figure 7.3: Breakdown of ATP to release energy', atp='Adenosine Tri Phosphate (ATP)', adp='Adenosine Di Phosphate (ADP)', water='Water', energy='Energy')
AB_UR = dict(title='شکل 7.3', atp='ایڈینوسین ٹرائی فاسفیٹ (ATP)', adp='ایڈینوسین ڈائی فاسفیٹ (ADP)', water='پانی', energy='توانائی')
AB_PS = dict(title='شکل 7.3', atp='اډینوزین ټرای فاسفېټ (ATP)', adp='اډینوزین ډای فاسفېټ (ADP)', water='اوبه', energy='انرژي')


def atp_cycle(L):
    b = ['<path d="M470,110 Q275,40 85,110" stroke="#e91e63" stroke-width="5" fill="none"/><polygon points="88,100 72,115 94,118" fill="#e91e63"/>',
         '<path d="M85,170 Q275,240 470,170" stroke="#e91e63" stroke-width="5" fill="none"/><polygon points="466,162 482,168 462,180" fill="#e91e63"/>']
    for x, lab in ((60, 'ATP'), (500, 'ATP')):
        b.append(f'<circle cx="{x}" cy="140" r="42" fill="#64b5f6" stroke="#1565c0"/>' + txt(x, 145, lab, 12, 'middle', 'bold'))
    b.append(''.join(f'<circle cx="{18 + k*4}" cy="{110 + k*12}" r="8" fill="#fff59d" stroke="#f9a825"/>' for k in range(3)) + ''.join(f'<circle cx="{465 + k*4}" cy="{100 + k*12}" r="8" fill="#fff59d" stroke="#f9a825"/>' for k in range(2)))
    b.append('<ellipse cx="220" cy="95" rx="38" ry="18" fill="#fff9c4"/>' + txt(220, 99, L['energy'], 11, 'middle', 'bold') + '<ellipse cx="220" cy="185" rx="38" ry="18" fill="#fff9c4"/>' + txt(220, 189, L['energy'], 11, 'middle', 'bold'))
    b.append('<circle cx="330" cy="100" r="8" fill="#fff" stroke="#333"/>' + txt(345, 104, 'Pi', 11) + '<circle cx="330" cy="180" r="8" fill="#fff" stroke="#333"/>' + txt(345, 184, 'Pi', 11))
    b.append(txt(150, 40, L['water'], 11, 'middle', 'bold') + txt(400, 55, L['break'], 12, 'middle', 'bold') + txt(150, 245, L['form'], 12, 'middle', 'bold') + txt(400, 235, L['water'], 11, 'middle', 'bold'))
    return svg_wrap(''.join(b), 560, 260, L['title'])


AC_EN = dict(title='Figure 7.4: The ATP-ADP Cycle', energy='Energey', water='Water', break_='', **{'break': 'Breakdown of ATP'}, form='Formation of ATP')
AC_UR = dict(title='شکل 7.4', energy='توانائی', water='پانی', **{'break': 'ATP کی شکست'}, form='ATP کی تشکیل')
AC_PS = dict(title='شکل 7.4', energy='انرژي', water='اوبه', **{'break': 'د ATP ماتېدل'}, form='د ATP جوړېدل')

CP_EN = dict(title='Fig. 7.5: Chloroplast structure', granum=['Granum', '(stack of thylakoids)'], thylakoid='Thylakoid', inner=['Inner', 'membrane'], outer=['Outer', 'membrane'], stroma=['Stroma', '(aqueous space)'])
CP_UR = dict(title='شکل 7.5', granum=['گرینم', '(تھائیلاکوئیڈز کا ڈھیر)'], thylakoid='تھائیلاکوئیڈ', inner=['اندرونی', 'جھلی'], outer=['بیرونی', 'جھلی'], stroma=['اسٹروما', '(آبی جگہ)'])
CP_PS = dict(title='شکل 7.5', granum=['ګرانوم', '(د تایلاکویډونو ډېرۍ)'], thylakoid='تایلاکویډ', inner=['داخلي', 'غشا'], outer=['بهرنۍ', 'غشا'], stroma=['سټروما', '(اوبلنه فضا)'])


def three(fn, a, b, c):
    return fn(a), fn(b), fn(c)


def sections():
    out = []
    s = Section('bio7_slo', 'SLOs', 'Student Learning Outcomes', 'طلبہ کے حاصلاتِ تعلم', 'د زده کوونکو د زده کړې پایلې', [132])
    s.h('After studying this unit, the students will be able to:', 'اس یونٹ کا مطالعہ کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د دې یونټ له مطالعې وروسته به زده کوونکي وکولای شي چې:')
    s.ul([
        ('Define bioenergetics as the study of energy relationships and energy conversions in living organisms.', 'بائیو انرجیٹکس کی تعریف جانداروں میں توانائی کے تعلقات اور تبدیلیوں کے مطالعے کے طور پر کر سکیں۔', 'بایوانرژیټیک په ژوندیو موجوداتو کې د انرژۍ د اړیکو او بدلونونو د مطالعې په توګه تعریف کړي.'),
        ('Describe the importance of Oxidation-Reduction reactions for the flow of energy through living systems.', 'جاندار نظاموں میں توانائی کے بہاؤ کے لیے تکسید و تخفیف کے تعاملات کی اہمیت بیان کر سکیں۔', 'په ژوندیو سیسټمونو کې د انرژۍ د جریان لپاره د اکسیډیشن-ریډکشن تعاملونو اهمیت بیان کړي.'),
        ('Explain ATP as a molecule that is the chief energy currency of all cells.', 'ATP کی وضاحت اس مالیکیول کے طور پر کر سکیں جو تمام خلیوں کی بنیادی توانائی کی کرنسی ہے۔', 'ATP د هغه مالیکول په توګه تشریح کړي چې د ټولو حجرو د انرژۍ اصلي اسعار دی.'),
        ('Describe the synthesis and breaking of ATP through ATP-ADP cycle.', 'ATP-ADP چکر کے ذریعے ATP کی تالیف اور شکست بیان کر سکیں۔', 'د ATP-ADP دورې له لارې د ATP جوړېدل او ماتېدل بیان کړي.'),
        ('State that photosynthesis is the fundamental process by which plants manufacture carbohydrates from raw materials.', 'بیان کر سکیں کہ ضیائی تالیف وہ بنیادی عمل ہے جس سے پودے خام مال سے کاربوہائیڈریٹس بناتے ہیں۔', 'بیان کړي چې فوتوسنتز هغه بنسټیزه پروسه ده چې بوټي پرې له خامو موادو کاربوهایډریټونه جوړوي.'),
        ('State the equation (in words or symbols) for photosynthesis.', 'ضیائی تالیف کی مساوات (الفاظ یا علامات میں) بیان کر سکیں۔', 'د فوتوسنتز معادله (په کلمو یا نښو) بیان کړي.'),
        ('Reason out that all forms of life are completely dependent on photosynthesis.', 'دلیل دے سکیں کہ زندگی کی تمام اقسام مکمل طور پر ضیائی تالیف پر منحصر ہیں۔', 'دلیل ورکړي چې د ژوند ټول ډولونه په بشپړه توګه پر فوتوسنتز متکي دي.'),
        ('Describe that chlorophyll traps light energy and converts it into chemical energy for the formation of carbohydrates and their subsequent storage.', 'بیان کر سکیں کہ کلوروفل روشنی کی توانائی کو جذب کر کے کاربوہائیڈریٹس بنانے اور ذخیرہ کرنے کے لیے کیمیائی توانائی میں بدلتا ہے۔', 'بیان کړي چې کلوروفیل د رڼا انرژي نیسي او د کاربوهایډریټونو د جوړولو او زېرمه کولو لپاره یې په کیمیاوي انرژۍ بدلوي.'),
        ('Outline the processes (Light and Dark reactions) involved in photosynthesis.', 'ضیائی تالیف میں شامل عوامل (روشنی اور تاریک تعاملات) کا خاکہ پیش کر سکیں۔', 'په فوتوسنتز کې شاملې پروسې (د رڼا او تیارې تعاملونه) لنډې بیان کړي.'),
        ('Describe, in general terms, the intake of carbon dioxide and water by plants.', 'پودوں کے ذریعے کاربن ڈائی آکسائیڈ اور پانی کے حصول کو عمومی طور پر بیان کر سکیں۔', 'د بوټو په واسطه د کاربن ډای اکساید او اوبو اخیستل په عمومي ډول بیان کړي.'),
        ('Explain the concept of limiting factors in photosynthesis.', 'ضیائی تالیف میں محدود کرنے والے عوامل کے تصور کی وضاحت کر سکیں۔', 'په فوتوسنتز کې د محدودوونکو عواملو مفهوم تشریح کړي.'),
        ('State the effect of varying light intensity, carbon dioxide concentration and temperature on the rate of photosynthesis.', 'ضیائی تالیف کی شرح پر روشنی کی شدت، کاربن ڈائی آکسائیڈ کے ارتکاز اور درجۂ حرارت میں تبدیلی کا اثر بیان کر سکیں۔', 'د فوتوسنتز پر کچه د رڼا د شدت، کاربن ډای اکساید د غلظت او تودوخې د بدلون اغېز بیان کړي.'),
        ('Describe anaerobic respiration by means of word and symbol equation', 'غیر ہوائی تنفس کو الفاظ اور علامتی مساوات سے بیان کر سکیں', 'غیر هوایي تنفس د کلمو او نښو په معادله بیان کړي'),
        ('Describe the importance of Anaerobic Respiration', 'غیر ہوائی تنفس کی اہمیت بیان کر سکیں', 'د غیر هوایي تنفس اهمیت بیان کړي'),
        ('Describe aerobic respiration by means of word and symbol equation.', 'ہوائی تنفس کو الفاظ اور علامتی مساوات سے بیان کر سکیں۔', 'هوایي تنفس د کلمو او نښو په معادله بیان کړي.'),
        ('Outline the mechanism of respiration while defining Glycolysis, Krebs cycle and Electron Transport Chain.', 'گلائکولائسس، کریبز سائیکل اور الیکٹران ٹرانسپورٹ چین کی تعریف کرتے ہوئے تنفس کے طریقۂ کار کا خاکہ پیش کر سکیں۔', 'د ګلایکولیزس، کربس دورې او د الکترون لېږد زنځیر په تعریف سره د تنفس میکانیزم لنډ بیان کړي.'),
        ('Compare aerobic and anaerobic respiration with reference to the amount of energy released.', 'خارج ہونے والی توانائی کی مقدار کے حوالے سے ہوائی اور غیر ہوائی تنفس کا موازنہ کر سکیں۔', 'د خوشې شوې انرژۍ د اندازې له مخې هوایي او غیر هوایي تنفس پرتله کړي.'),
        ('List ways in which respiratory energy is used in the body.', 'وہ طریقے درج کر سکیں جن سے تنفسی توانائی جسم میں استعمال ہوتی ہے۔', 'هغه لارې ولیکي چې په بدن کې تنفسي انرژي پرې کارېږي.'),
        ('Compare respiration and photosynthesis', 'تنفس اور ضیائی تالیف کا موازنہ کر سکیں', 'تنفس او فوتوسنتز پرتله کړي'),
    ])
    out.append(s)

    s = Section('bio7_1', '7.1', 'Bioenergetics', 'بائیو انرجیٹکس', 'بایوانرژیټیک', [133, 134, 135, 136])
    s.p('In previous unit, you have learnt about many activities that living organisms perform. These include cell division, respiration, growth, irritability etc. All these activities are possible because of chemical reactions occurring in their bodies (metabolism). Some reactions require energy while other reactions release energy. Organisms have very sophisticated systems of capturing, storing and utilizing energy. In this unit, you will study the nature of energy used by organisms and the basic processes by which organisms capture and store energy.',
        'پچھلے یونٹ میں آپ نے جانداروں کی بہت سی سرگرمیوں کے بارے میں سیکھا۔ ان میں خلوی تقسیم، تنفس، نشوونما، حساسیت وغیرہ شامل ہیں۔ یہ تمام سرگرمیاں ان کے جسموں میں ہونے والے کیمیائی تعاملات (میٹابولزم) کی وجہ سے ممکن ہیں۔ بعض تعاملات کو توانائی درکار ہوتی ہے جبکہ دوسرے تعاملات توانائی خارج کرتے ہیں۔ جانداروں میں توانائی حاصل کرنے، ذخیرہ کرنے اور استعمال کرنے کے بہت ترقی یافتہ نظام ہیں۔ اس یونٹ میں آپ جانداروں کے استعمال کردہ توانائی کی نوعیت اور ان بنیادی عوامل کا مطالعہ کریں گے جن سے جاندار توانائی حاصل اور ذخیرہ کرتے ہیں۔',
        'په تېر یونټ کې تاسو د ژوندیو موجوداتو د ډېرو فعالیتونو په اړه زده کړل. په دې کې حجروي وېش، تنفس، وده، حساسیت او نور شامل دي. دا ټول فعالیتونه د هغوی په بدنونو کې د کیمیاوي تعاملونو (میټابولیزم) له امله ممکن دي. ځینې تعاملونه انرژۍ ته اړتیا لري او نور انرژي خوشې کوي. ژوندي موجودات د انرژۍ د نیولو، زېرمه کولو او کارولو ډېر پرمختللي سیسټمونه لري. په دې یونټ کې به تاسو د ژوندیو موجوداتو د کارول شوې انرژۍ طبیعت او هغه بنسټیزې پروسې ولولئ چې ژوندي موجودات پرې انرژي نیسي او زېرمه کوي.')
    s.h('7.1 Bioenergetics', '7.1 بائیو انرجیٹکس', '7.1 بایوانرژیټیک')
    s.p('Bioenergetics is the study of transformation of energy in organisms. All organisms need energy to keep them alive and functioning.', 'بائیو انرجیٹکس جانداروں میں توانائی کی تبدیلی کا مطالعہ ہے۔ تمام جانداروں کو زندہ اور فعال رہنے کے لیے توانائی درکار ہے۔', 'بایوانرژیټیک په ژوندیو موجوداتو کې د انرژۍ د بدلون مطالعه ده. ټول ژوندي موجودات د ژوندي او فعال پاتې کېدو لپاره انرژۍ ته اړتیا لري.')
    s.callout(SI, [('The metabolic processes which occur inside the living bodies all the times, involve the making or breaking of bonds in the molecules. When chemical bonds are broken, energy is released and when bonds are formed, energy is stored.', 'جاندار جسموں کے اندر ہر وقت ہونے والے میٹابولک عوامل میں مالیکیولز کے بانڈ بنتے یا ٹوٹتے ہیں۔ جب کیمیائی بانڈ ٹوٹتے ہیں تو توانائی خارج ہوتی ہے اور جب بانڈ بنتے ہیں تو توانائی ذخیرہ ہوتی ہے۔', 'هغه میټابولیکي پروسې چې تل د ژوندیو بدنونو دننه کېږي، په مالیکولونو کې د اړیکو جوړېدل یا ماتېدل لري. کله چې کیمیاوي اړیکې ماتې شي، انرژي خوشې کېږي او کله چې اړیکې جوړې شي، انرژي زېرمه کېږي.')])
    s.p('Sun is the ultimate source of energy for all organisms. However, only autotrophs use this energy directly. They capture solar energy and convert it into stored chemical energy through the process of photosynthesis. The energy stored in food is then transformed into mechanical and heat energy during respiration. Thus, the two main processes involving energy transformation are photosynthesis and respiration.',
        'سورج تمام جانداروں کے لیے توانائی کا حتمی ذریعہ ہے۔ تاہم صرف آٹوٹرافس اس توانائی کو براہِ راست استعمال کرتے ہیں۔ یہ شمسی توانائی حاصل کر کے ضیائی تالیف کے ذریعے اسے ذخیرہ شدہ کیمیائی توانائی میں بدلتے ہیں۔ خوراک میں ذخیرہ شدہ توانائی پھر تنفس کے دوران میکانیکی اور حرارتی توانائی میں بدلتی ہے۔ اس طرح توانائی کی تبدیلی کے دو بڑے عوامل ضیائی تالیف اور تنفس ہیں۔',
        'لمر د ټولو ژوندیو موجوداتو لپاره د انرژۍ وروستۍ سرچینه ده. خو یوازې اوټوټروفونه دا انرژي مستقیم کاروي. دوی د لمر انرژي نیسي او د فوتوسنتز له لارې یې په زېرمه شوې کیمیاوي انرژۍ بدلوي. په خوړو کې زېرمه شوې انرژي بیا د تنفس پر مهال په میخانیکي او تودوخیزې انرژۍ بدلېږي. په دې توګه د انرژۍ د بدلون دوه اصلي پروسې فوتوسنتز او تنفس دي.')
    s.h('7.1.1 Importance of Oxidation-Reduction Reactions', '7.1.1 تکسید و تخفیف کے تعاملات کی اہمیت', '7.1.1 د اکسیډیشن-ریډکشن تعاملونو اهمیت')
    s.p('Both photosynthesis and respiration are basically oxidation-reduction processes. Oxidation is defined as the loss of hydrogen or electrons. Reduction is the opposite of oxidation in which hydrogen or electrons are gained.',
        'ضیائی تالیف اور تنفس دونوں بنیادی طور پر تکسید و تخفیف کے عوامل ہیں۔ تکسید (آکسیڈیشن) کی تعریف ہائیڈروجن یا الیکٹرانز کا ضیاع ہے۔ تخفیف (ریڈکشن) تکسید کا الٹ ہے جس میں ہائیڈروجن یا الیکٹرانز حاصل ہوتے ہیں۔',
        'فوتوسنتز او تنفس دواړه په اصل کې د اکسیډیشن-ریډکشن پروسې دي. اکسیډیشن د هایدروجن یا الکترونونو له لاسه ورکول تعریف کېږي. ریډکشن د اکسیډیشن برعکس دی چې پکې هایدروجن یا الکترونونه ترلاسه کېږي.')
    s.callout(SI, [('Energy can neither be stored nor released without oxidation-reduction reactions. Therefore, life processes would be impossible without oxidation-reduction reactions.', 'تکسید و تخفیف کے تعاملات کے بغیر توانائی نہ ذخیرہ ہو سکتی ہے نہ خارج۔ اس لیے تکسید و تخفیف کے تعاملات کے بغیر زندگی کے عوامل ناممکن ہوتے۔', 'بې له اکسیډیشن-ریډکشن تعاملونو انرژي نه زېرمه کېدای شي او نه خوشې. نو بې له دې تعاملونو د ژوند پروسې ناممکنې وې.')])
    s.p('In photosynthesis, a chain of oxidation-reduction reactions occurs during which carbon dioxide and water are combined to make food molecules. In these oxidation-reduction reactions, energy is stored in food molecules. Respiration is also oxidation-reduction process during which food molecules are broken down into carbon dioxide and water. In these oxidation-reduction reactions, energy is liberated from food molecules.',
        'ضیائی تالیف میں تکسید و تخفیف کے تعاملات کا ایک سلسلہ ہوتا ہے جس کے دوران کاربن ڈائی آکسائیڈ اور پانی مل کر خوراک کے مالیکیول بناتے ہیں۔ ان تعاملات میں توانائی خوراک کے مالیکیولز میں ذخیرہ ہوتی ہے۔ تنفس بھی تکسید و تخفیف کا عمل ہے جس کے دوران خوراک کے مالیکیول کاربن ڈائی آکسائیڈ اور پانی میں ٹوٹتے ہیں۔ ان تعاملات میں خوراک کے مالیکیولز سے توانائی آزاد ہوتی ہے۔',
        'په فوتوسنتز کې د اکسیډیشن-ریډکشن تعاملونو یوه لړۍ کېږي چې پکې کاربن ډای اکساید او اوبه یوځای کېږي او د خوړو مالیکولونه جوړوي. په دې تعاملونو کې انرژي د خوړو په مالیکولونو کې زېرمه کېږي. تنفس هم د اکسیډیشن-ریډکشن پروسه ده چې پکې د خوړو مالیکولونه په کاربن ډای اکساید او اوبو ماتېږي. په دې تعاملونو کې له خوړو مالیکولونو انرژي آزادېږي.')
    s.fig('bio7-fig7-1', *three(redox_fig, RX_EN, RX_UR, RX_PS), .75, caption=('Figure 7.1: Importance of Oxidation-Reduction Reactions', 'شکل 7.1: تکسید و تخفیف کے تعاملات کی اہمیت', 'شکل 7.1: د اکسیډیشن-ریډکشن تعاملونو اهمیت'))
    s.h('7.1.2 ATP as the Energy Currency of Cells', '7.1.2 ATP خلیوں کی توانائی کی کرنسی', '7.1.2 ATP د حجرو د انرژۍ اسعار')
    s.p('Cells use energy for performing activities like synthesis of proteins, cell division and growth etc. Energy is provided to all living cells by Adenosine Tri Phosphate (ATP). It is an energy rich molecule and is called as the "energy currency" of cells. Cells make ATPs to store energy while they break ATPs to get energy.',
        'خلیے پروٹین سازی، خلوی تقسیم اور نشوونما جیسی سرگرمیوں کے لیے توانائی استعمال کرتے ہیں۔ تمام زندہ خلیوں کو توانائی ایڈینوسین ٹرائی فاسفیٹ (ATP) فراہم کرتا ہے۔ یہ توانائی سے بھرپور مالیکیول ہے اور خلیوں کی ”توانائی کی کرنسی“ کہلاتا ہے۔ خلیے توانائی ذخیرہ کرنے کے لیے ATP بناتے ہیں جبکہ توانائی حاصل کرنے کے لیے ATP توڑتے ہیں۔',
        'حجرې د پروټین جوړولو، حجروي وېش او ودې په څېر فعالیتونو لپاره انرژي کاروي. ټولو ژوندیو حجرو ته انرژي اډینوزین ټرای فاسفېټ (ATP) ورکوي. دا د انرژۍ ډک مالیکول دی او د حجرو ”د انرژۍ اسعار“ بلل کېږي. حجرې د انرژۍ د زېرمه کولو لپاره ATP جوړوي او د انرژۍ د ترلاسه کولو لپاره یې ماتوي.')
    s.fig('bio7-fig7-2', *three(atp_fig, AT_EN, AT_UR, AT_PS), .6, caption=('Figure 7.2: Structural formula of an ATP molecule', 'شکل 7.2: ATP مالیکیول کا ساختی فارمولا', 'شکل 7.2: د ATP مالیکول جوړښتي فورمول'))
    s.p('ATP molecule has 3 components i.e. one adenine (a nitrogenous base), one ribose sugar and three phosphate groups. The covalent bonds between phosphates groups are high-energy bonds.',
        'ATP مالیکیول کے 3 اجزا ہیں یعنی ایک ایڈینین (ایک نائٹروجنی اساس)، ایک رائبوز شکر اور تین فاسفیٹ گروپس۔ فاسفیٹ گروپس کے درمیان کوویلنٹ بانڈ زیادہ توانائی والے بانڈ ہیں۔',
        'د ATP مالیکول 3 برخې لري یعنې یو اډینین (نایټروجني قاعده)، یوه رایبوز بوره او درې فاسفېټ ګروپونه. د فاسفېټ ګروپونو ترمنځ کوولانټ اړیکې د لوړې انرژۍ اړیکې دي.')
    s.callout(SI, [('ATP is the currency of energy of a cell. A cell with more ATP is able to do more work.', 'ATP خلیے کی توانائی کی کرنسی ہے۔ زیادہ ATP والا خلیہ زیادہ کام کر سکتا ہے۔', 'ATP د حجرې د انرژۍ اسعار دی. ډېر ATP لرونکې حجره ډېر کار کولای شي.')])
    s.p('When a cell needs energy, one bond between phosphate groups is broken. It releases 7.3 kcal (7,300 calories) energy. As a result, one inorganic phosphate (Pi) separates and ATP is converted to ADP (Adenosine Diphosphate).',
        'جب خلیے کو توانائی کی ضرورت ہوتی ہے تو فاسفیٹ گروپس کے درمیان ایک بانڈ ٹوٹ جاتا ہے۔ اس سے 7.3 kcal (7,300 کیلوریز) توانائی خارج ہوتی ہے۔ نتیجتاً ایک غیر نامیاتی فاسفیٹ (Pi) الگ ہوتا ہے اور ATP، ADP (ایڈینوسین ڈائی فاسفیٹ) میں بدل جاتا ہے۔',
        'کله چې حجره انرژۍ ته اړتیا ولري، د فاسفېټ ګروپونو ترمنځ یوه اړیکه ماتېږي. دا 7.3 kcal (7,300 کالورۍ) انرژي خوشې کوي. په پایله کې یو غیر عضوي فاسفېټ (Pi) جلا کېږي او ATP په ADP (اډینوزین ډای فاسفېټ) بدلېږي.')
    s.fig('bio7-fig7-3', *three(atp_breakdown, AB_EN, AB_UR, AB_PS), .9, caption=('Figure 7.3: Breakdown of ATP to release energy', 'شکل 7.3: توانائی کے اخراج کے لیے ATP کی شکست', 'شکل 7.3: د انرژۍ د خوشې کولو لپاره د ATP ماتېدل'))
    s.p('When a cell has energy, it stores the energy by combining one inorganic phosphate (Pi) with ADP. In this way, ATP is formed.', 'جب خلیے کے پاس توانائی ہو تو وہ ایک غیر نامیاتی فاسفیٹ (Pi) کو ADP سے جوڑ کر توانائی ذخیرہ کرتا ہے۔ اس طرح ATP بنتا ہے۔', 'کله چې حجره انرژي ولري، د ADP سره د یو غیر عضوي فاسفېټ (Pi) په یوځای کولو انرژي زېرمه کوي. په دې ډول ATP جوړېږي.')
    s.fig('bio7-fig7-4', *three(atp_cycle, AC_EN, AC_UR, AC_PS), .8, caption=('Figure 7.4: The ATP-ADP Cycle', 'شکل 7.4: ATP-ADP چکر', 'شکل 7.4: د ATP-ADP دوره'))
    s.p('SpaceBook note: Figure 7.4 prints "Energey" and shows ATP at both ends of the cycle (the right-hand molecule is drawn with two phosphates, i.e. ADP). Printed labels are kept.', 'اسپیس بک نوٹ: شکل 7.4 میں ”Energey“ چھپا ہے اور چکر کے دونوں سروں پر ATP لکھا ہے (دائیں مالیکیول میں دو فاسفیٹ ہیں یعنی ADP)۔ چھپے لیبل رکھے گئے ہیں۔', 'د سپېس بوک یادونه: شکل 7.4 ”Energey“ چاپ کړی او د دورې په دواړو سرونو ATP لیکلی (ښی مالیکول دوه فاسفېټه لري یعنې ADP). چاپ شوي لیبلونه ساتل شوي.', editorial=True)
    s.p('ATP molecules are constantly broken by the cell into ADP and inorganic phosphate and energy is obtained. At the same time, ATP molecules are constantly regenerated from ADP and phosphate using energy released from the breakdown of food. This is how constant cycle of ATP breakdown and reformation goes on in the living cells.',
        'خلیہ ATP مالیکیولز کو مسلسل ADP اور غیر نامیاتی فاسفیٹ میں توڑتا ہے اور توانائی حاصل ہوتی ہے۔ اسی وقت خوراک کی شکست سے خارج ہونے والی توانائی سے ADP اور فاسفیٹ سے ATP مالیکیول مسلسل دوبارہ بنتے رہتے ہیں۔ اسی طرح زندہ خلیوں میں ATP کی شکست اور دوبارہ تشکیل کا مسلسل چکر چلتا رہتا ہے۔',
        'حجره ATP مالیکولونه په دوامداره ډول په ADP او غیر عضوي فاسفېټ ماتوي او انرژي ترلاسه کېږي. په همدې وخت کې د خوړو له ماتېدو د خوشې شوې انرژۍ په کارولو له ADP او فاسفېټ څخه ATP مالیکولونه بیا بیا جوړېږي. په ژوندیو حجرو کې د ATP د ماتېدو او بیا جوړېدو دوامداره دوره همداسې روانه وي.')
    s.callout(('Analysing and Interpreting', 'تجزیہ اور توضیح', 'شننه او تفسیر'), [('Design the molecular model of ATP using low-cost, no-cost materials and label its components and high-energy P-P bonds.', 'کم قیمت یا مفت اشیا سے ATP کا مالیکیولی ماڈل بنائیں اور اس کے اجزا اور زیادہ توانائی والے P-P بانڈز کے نام لکھیں۔', 'په لږ لګښت یا وړیا موادو د ATP مالیکولي ماډل جوړ کړئ او برخې یې او د لوړې انرژۍ P-P اړیکې ونوموئ.')])
    out.append(s)

    s = Section('bio7_2', '7.2', 'Photosynthesis: A life sustaining process', 'ضیائی تالیف: زندگی برقرار رکھنے والا عمل', 'فوتوسنتز: د ژوند ساتونکې پروسه', [136, 137])
    s.p('The word Photosynthesis is the combination of two Greek words; "Photo" means light and "Synthesis" means to manufacture. Photosynthesis is defined as the manufacturing of organic food (glucose) in the presence of chlorophyll, using CO₂, water and sunlight and releasing oxygen as a byproduct. Photosynthesis occurs in autotrophic organisms (plants, algae, and some bacteria).',
        'لفظ فوٹو سنتھیسس دو یونانی الفاظ کا مجموعہ ہے؛ ”فوٹو“ یعنی روشنی اور ”سنتھیسس“ یعنی تیار کرنا۔ ضیائی تالیف کی تعریف یہ ہے کہ کلوروفل کی موجودگی میں CO₂، پانی اور سورج کی روشنی استعمال کر کے نامیاتی خوراک (گلوکوز) تیار کرنا اور ضمنی پیداوار کے طور پر آکسیجن خارج کرنا۔ ضیائی تالیف آٹوٹرافک جانداروں (پودوں، الجی اور بعض بیکٹیریا) میں ہوتی ہے۔',
        'د فوتوسنتز کلمه د دوو یوناني کلمو ترکیب دی؛ ”فوتو“ یعنې رڼا او ”سنتیزس“ یعنې جوړول. فوتوسنتز داسې تعریف کېږي: د کلوروفیل په شتون کې د CO₂، اوبو او لمر رڼا په کارولو د عضوي خوړو (ګلوکوز) جوړول او د فرعي محصول په توګه د اکسیجن خوشې کول. فوتوسنتز په اوټوټروفیکو موجوداتو (بوټو، الجي او ځینو باکتریاوو) کې کېږي.')
    s.callout(STS, [('What do the photovoltaic array (solar energy system) and the tomato plant have in common? They both convert sunlight (radiant energy) into forms useful to humans. The photovoltaic array absorbs solar energy and stores it as chemical potential energy in batteries. The leaves of the tomato plant absorb solar energy that is (mainly) stored as chemical potential energy in compounds called carbohydrates',
                     'فوٹو وولٹائک ایرے (شمسی توانائی کا نظام) اور ٹماٹر کے پودے میں کیا چیز مشترک ہے؟ دونوں سورج کی روشنی (شعاعی توانائی) کو انسانوں کے لیے مفید شکلوں میں بدلتے ہیں۔ فوٹو وولٹائک ایرے شمسی توانائی جذب کر کے بیٹریوں میں کیمیائی پوٹینشل توانائی کے طور پر ذخیرہ کرتا ہے۔ ٹماٹر کے پودے کے پتے شمسی توانائی جذب کرتے ہیں جو (زیادہ تر) کاربوہائیڈریٹس نامی مرکبات میں کیمیائی پوٹینشل توانائی کے طور پر ذخیرہ ہوتی ہے',
                     'فوټوولټایک سیسټم (د لمر انرژۍ سیسټم) او د رومي بانجان بوټي کې څه ګډ دي؟ دواړه د لمر رڼا (وړانګیزه انرژي) انسانانو ته په ګټورو بڼو بدلوي. فوټوولټایک سیسټم د لمر انرژي جذبوي او په بټریو کې یې د کیمیاوي پوټنشیل انرژۍ په توګه زېرمه کوي. د رومي بانجان د بوټي پاڼې د لمر انرژي جذبوي چې (ډېری یې) په کاربوهایډریټونو نومو مرکبونو کې د کیمیاوي پوټنشیل انرژۍ په توګه زېرمه کېږي')])
    s.lines([('6CO₂ + 12H₂O —(Sun light, Chlorophyll)→ C₆H₁₂O₆ + 6O₂ + 6H₂O', '6CO₂ + 12H₂O —(سورج کی روشنی، کلوروفل)→ C₆H₁₂O₆ + 6O₂ + 6H₂O', '6CO₂ + 12H₂O —(د لمر رڼا، کلوروفیل)→ C₆H₁₂O₆ + 6O₂ + 6H₂O'),
             ('Carbon Dioxide + Water —(Sun light, Chlorophyll)→ Glucose + Oxygen + Water', 'کاربن ڈائی آکسائیڈ + پانی —(سورج کی روشنی، کلوروفل)→ گلوکوز + آکسیجن + پانی', 'کاربن ډای اکساید + اوبه —(د لمر رڼا، کلوروفیل)→ ګلوکوز + اکسیجن + اوبه')])
    s.p('Photosynthesis acts as energy capturing and storing process. Heterotrophic organisms cannot carry out photosynthesis and are unable to use energy of sunlight directly. Therefore, for their energy needs, they depend directly or indirectly on plants. Photosynthesis also provides oxygen, which is used by all aerobic organisms for respiration.',
        'ضیائی تالیف توانائی حاصل کرنے اور ذخیرہ کرنے کے عمل کے طور پر کام کرتی ہے۔ ہیٹروٹرافک جاندار ضیائی تالیف نہیں کر سکتے اور سورج کی روشنی کی توانائی براہِ راست استعمال نہیں کر سکتے۔ اس لیے اپنی توانائی کی ضروریات کے لیے یہ براہِ راست یا بالواسطہ پودوں پر منحصر ہیں۔ ضیائی تالیف آکسیجن بھی فراہم کرتی ہے جو تمام ہوائی جاندار تنفس کے لیے استعمال کرتے ہیں۔',
        'فوتوسنتز د انرژۍ د نیولو او زېرمه کولو پروسه ده. هټروټروفیک موجودات فوتوسنتز نه شي کولای او د لمر رڼا انرژي مستقیم نه شي کارولای. نو د خپلو انرژۍ اړتیاوو لپاره مستقیم یا غیر مستقیم پر بوټو متکي دي. فوتوسنتز اکسیجن هم برابروي چې ټول هوایي موجودات یې د تنفس لپاره کاروي.')
    s.h('7.2.1 Role of Chlorophyll and Sunlight in photosynthesis', '7.2.1 ضیائی تالیف میں کلوروفل اور سورج کی روشنی کا کردار', '7.2.1 په فوتوسنتز کې د کلوروفیل او لمر رڼا رول')
    s.p('Chlorophyll is a complex organic compound. It absorbs sunlight (blue and red portion) and converts it into chemical energy for the formation of carbohydrates (glucose). The green portion of sunlight is mainly reflected. That is why chlorophyll appears green. When chlorophyll absorbs light, its electrons are excited. The energy of excited electrons is used to make ATP.',
        'کلوروفل ایک پیچیدہ نامیاتی مرکب ہے۔ یہ سورج کی روشنی (نیلا اور سرخ حصہ) جذب کر کے کاربوہائیڈریٹس (گلوکوز) بنانے کے لیے اسے کیمیائی توانائی میں بدلتا ہے۔ سورج کی روشنی کا سبز حصہ زیادہ تر منعکس ہو جاتا ہے۔ اسی لیے کلوروفل سبز نظر آتا ہے۔ جب کلوروفل روشنی جذب کرتا ہے تو اس کے الیکٹرانز برانگیختہ ہو جاتے ہیں۔ برانگیختہ الیکٹرانز کی توانائی ATP بنانے میں استعمال ہوتی ہے۔',
        'کلوروفیل یو پېچلی عضوي مرکب دی. د لمر رڼا (آبي او سره برخه) جذبوي او د کاربوهایډریټونو (ګلوکوز) د جوړولو لپاره یې په کیمیاوي انرژۍ بدلوي. د لمر رڼا شنه برخه ډېری منعکسېږي. له همدې امله کلوروفیل شین ښکاري. کله چې کلوروفیل رڼا جذب کړي، الکترونونه یې هیجان ته راځي. د هیجاني الکترونونو انرژي د ATP په جوړولو کې کارېږي.')
    s.p('In plants and algae, chlorophyll is present in chloroplasts while in photosynthetic prokaryotes, it is present in the cell membrane.', 'پودوں اور الجی میں کلوروفل کلوروپلاسٹ میں ہوتا ہے جبکہ ضیائی تالیف کرنے والے پروکیریوٹس میں یہ خلوی جھلی میں ہوتا ہے۔', 'په بوټو او الجي کې کلوروفیل په کلوروپلاسټونو کې وي په داسې حال کې چې په فوتوسنتیټیکو پروکاریوټونو کې د حجرې په غشا کې وي.')
    s.fig('bio7-fig7-5', *three(chloroplast_fig, CP_EN, CP_UR, CP_PS), .6, caption=('Fig. 7.5: Chloroplast structure', 'شکل 7.5: کلوروپلاسٹ کی ساخت', 'شکل 7.5: د کلوروپلاسټ جوړښت'))
    s.callout(('Point to Ponder', 'غور طلب نکتہ', 'د فکر وړ ټکی'), [('Suggest what would happen to the living organisms if the process of photosynthesis stops.', 'بتائیں کہ اگر ضیائی تالیف کا عمل رک جائے تو جانداروں کا کیا ہوگا۔', 'ووایاست که د فوتوسنتز پروسه ودرېږي نو ژوندیو موجوداتو ته به څه پېښ شي.')])
    s.callout(SI, [('Photosynthetic prokaryotes lack chloroplasts but they do have unstacked photosynthetic membrances, which work like thylakoid membrane. Chlorophyll is attached to the thylakoid membrane.', 'ضیائی تالیف کرنے والے پروکیریوٹس میں کلوروپلاسٹ نہیں ہوتے لیکن ان میں غیر تہ دار ضیائی تالیفی جھلیاں ہوتی ہیں جو تھائیلاکوئیڈ جھلی کی طرح کام کرتی ہیں۔ کلوروفل تھائیلاکوئیڈ جھلی سے جڑا ہوتا ہے۔', 'فوتوسنتیټیک پروکاریوټونه کلوروپلاسټ نه لري خو بې پوړه فوتوسنتیټیکې غشاوې لري چې د تایلاکویډ غشا په څېر کار کوي. کلوروفیل له تایلاکویډ غشا سره نښتی دی.')])
    s.p('The photosynthetic pigments are organized in the form of clusters, called photosystems, in thylakoid membranes of chloroplasts. Chlorophyll-a is the main photosynthetic pigment. Others are called accessory pigments and include chlorophyll-b and carotenoids.',
        'ضیائی تالیفی رنگدار مادے کلوروپلاسٹ کی تھائیلاکوئیڈ جھلیوں میں گچھوں کی شکل میں منظم ہوتے ہیں جنہیں فوٹو سسٹمز کہتے ہیں۔ کلوروفل-a بنیادی ضیائی تالیفی رنگدار مادہ ہے۔ دوسروں کو معاون رنگدار مادے کہتے ہیں جن میں کلوروفل-b اور کیروٹینائیڈز شامل ہیں۔',
        'فوتوسنتیټیک رنګونه د کلوروپلاسټونو په تایلاکویډي غشاوو کې د غونچو په بڼه تنظیم شوي چې فوټوسیسټمونه بلل کېږي. کلوروفیل-a اصلي فوتوسنتیټیک رنګ دی. نورو ته مرستندوی رنګونه ویل کېږي چې کلوروفیل-b او کاروټینویډونه پکې دي.')
    s.p('Chlorophylls absorb mainly blue and red lights. Some wave lengths are not absorbed by chlorophyll -a and are very affectively absorbed by accessory pigments and vice-versa.',
        'کلوروفلز زیادہ تر نیلی اور سرخ روشنی جذب کرتے ہیں۔ بعض طولِ موج کلوروفل-a جذب نہیں کرتا جبکہ معاون رنگدار مادے انہیں بہت مؤثر طریقے سے جذب کرتے ہیں اور اس کے برعکس۔',
        'کلوروفیلونه ډېری آبي او سره رڼا جذبوي. ځینې څپې کلوروفیل-a نه جذبوي او مرستندوی رنګونه یې ډېر اغېزمن جذبوي او برعکس.')
    out.append(s)
    return out
