# -*- coding: utf-8 -*-
"""Unit 2 part B — PDF 34-41 (printed 29-36): 2.3-2.6, Figures 2.1-2.2, Key Points, Exercise."""
from bio9_tools import Section, svg_wrap, txt

STS = ('Science, Technology and Society', 'سائنس، ٹیکنالوجی اور معاشرہ', 'ساینس، ټکنالوژي او ټولنه')


def person(x, y, shirt):
    return (f'<circle cx="{x}" cy="{y}" r="11" fill="#8d6e63"/><rect x="{x-14}" y="{y+12}" width="28" height="40" rx="6" fill="{shirt}"/>'
            f'<rect x="{x-12}" y="{y+52}" width="10" height="38" fill="#263238"/><rect x="{x+2}" y="{y+52}" width="10" height="38" fill="#263238"/>')


def mosquito(x, y):
    return (f'<g stroke="#37474f" stroke-width="1.5" fill="none"><path d="M{x-20},{y} L{x+20},{y}"/><path d="M{x-8},{y} l-8,12 M{x},{y} l-2,14 M{x+8},{y} l6,12 M{x-8},{y} l-10,-8 M{x+8},{y} l10,-8"/></g>'
            f'<ellipse cx="{x}" cy="{y}" rx="16" ry="4" fill="#455a64"/><path d="M{x+16},{y} l12,3" stroke="#455a64" stroke-width="1.5"/>'
            f'<ellipse cx="{x-4}" cy="{y-8}" rx="10" ry="4" fill="#cfd8dc" opacity=".8"/>')


def transmission(L):
    b = ['<rect width="600" height="330" fill="#fff"/>']
    arrow = lambda d: f'<path d="{d}" stroke="#d81b60" stroke-width="4" fill="none"/>'
    head = lambda pts: f'<polygon points="{pts}" fill="#d81b60"/>'
    # infected RBC (top-left), second mosquito (top-right), men left/right, first mosquito bottom
    b.append('<ellipse cx="120" cy="45" rx="55" ry="18" fill="#f8bbd0"/><circle cx="120" cy="35" r="24" fill="#b71c1c" stroke="#7f0000"/>'
             + ''.join(f'<circle cx="{120+dx}" cy="{35+dy}" r="3" fill="#ffcdd2"/>' for dx, dy in [(-8, -6), (6, -10), (10, 4), (-4, 8), (-12, 4)]))
    b.append('<ellipse cx="330" cy="50" rx="60" ry="20" fill="#fff9c4"/>' + mosquito(330, 48))
    b.append('<ellipse cx="200" cy="270" rx="60" ry="20" fill="#fff9c4"/>' + mosquito(200, 268))
    b.append('<ellipse cx="60" cy="235" rx="45" ry="10" fill="#b3e5fc"/>' + person(60, 140, '#c62828'))
    b.append('<ellipse cx="340" cy="235" rx="45" ry="10" fill="#b3e5fc"/>' + person(340, 140, '#3949ab'))
    b.append(arrow('M180,30 Q235,15 265,35') + head('265,35 252,26 255,42'))
    b.append(arrow('M360,70 Q375,95 352,120') + head('352,120 348,104 362,110'))
    b.append(arrow('M150,282 Q90,285 70,250') + head('70,250 66,266 80,260'))
    b.append(arrow('M55,128 Q55,95 85,70') + head('85,70 70,74 80,84'))
    b.append(txt(140, 82, L['rbc1'], 11, 'start', 'bold') + txt(140, 96, L['rbc2'], 11, 'start', 'bold'))
    b.append(txt(260, 92, L['m2a'], 11, 'start', 'bold') + txt(260, 106, L['m2b'], 11, 'start', 'bold'))
    b.append(txt(95, 160, L['man1a'], 11, 'start', 'bold') + txt(95, 174, L['man1b'], 11, 'start', 'bold') + txt(95, 188, L['man'], 11, 'start', 'bold'))
    b.append(txt(275, 160, L['man2a'], 11, 'start', 'bold') + txt(275, 174, L['man1b'], 11, 'start', 'bold') + txt(275, 188, L['man'], 11, 'start', 'bold'))
    b.append(txt(160, 305, L['m1a'], 11, 'start', 'bold') + txt(160, 319, L['m1b'], 11, 'start', 'bold'))
    # side box Aedes / Anopheles
    b.append('<rect x="410" y="10" width="185" height="310" rx="10" fill="#f1f8e9" stroke="#7cb342" stroke-width="2"/>')
    b.append('<circle cx="455" cy="60" r="38" fill="#fff" stroke="#333"/>' + mosquito(455, 60))
    b.append('<circle cx="550" cy="60" r="38" fill="#fff" stroke="#333"/>' + mosquito(550, 60).replace('#455a64', '#8d6e63'))
    b.append(txt(455, 115, L['aedes'], 11, 'middle', 'normal', '#222', italic=True) + txt(455, 129, L['mosq'], 11, 'middle'))
    b.append(txt(550, 115, L['anoph'], 11, 'middle', 'normal', '#222', italic=True) + txt(550, 129, L['mosq'], 11, 'middle'))
    for i, line in enumerate(L['box']):
        b.append(txt(420, 160 + i * 20, line, 12, 'start'))
    return svg_wrap(''.join(b), 600, 330, L['title'])


TR_EN = dict(title='Figure 2.1: Transmission of Plasmodium (Malaria) in human beings', rbc1='Infected', rbc2='red blood cells',
             m2a='Second infected', m2b='mosquito', man1a='First', man1b='infected', man='man', man2a='Second', m1a='First infected', m1b='mosquito',
             aedes='Aedes', anoph='Anopheles', mosq='mosquito',
             box=['Aedes mosquito transmits', 'viruses of dengue fever in', 'humans while Anopheles', 'mosquito transmits', 'plasmodium. See the', 'difference between the two', 'mosquitoes in above pictures.'])
TR_UR = dict(title='شکل 2.1', rbc1='متاثرہ', rbc2='سرخ خونی خلیات', m2a='دوسرا متاثرہ', m2b='مچھر', man1a='پہلا', man1b='متاثرہ', man='آدمی', man2a='دوسرا',
             m1a='پہلا متاثرہ', m1b='مچھر', aedes='ایڈیز', anoph='اینوفیلیز', mosq='مچھر',
             box=['ایڈیز مچھر انسانوں میں', 'ڈینگی بخار کے وائرس', 'منتقل کرتا ہے جبکہ', 'اینوفیلیز مچھر پلازموڈیم', 'منتقل کرتا ہے۔ اوپر کی', 'تصاویر میں دونوں مچھروں', 'کا فرق دیکھیں۔'])
TR_PS = dict(title='شکل 2.1', rbc1='اخته', rbc2='سرې وینې حجرې', m2a='دوهمه اخته', m2b='ماشۍ', man1a='لومړی', man1b='اخته', man='سړی', man2a='دوهم',
             m1a='لومړۍ اخته', m1b='ماشۍ', aedes='اېډیس', anoph='انوفلیس', mosq='ماشۍ',
             box=['اېډیس ماشۍ په انسانانو کې', 'د ډینګي تبې ویروسونه', 'لېږدوي په داسې حال کې', 'چې انوفلیس ماشۍ پلازموډیم', 'لېږدوي. په پورتنیو انځورونو', 'کې د دواړو ماشو توپیر', 'وګورئ.'])


def flowchart(L):
    """Figure 2.2: Steps in a Biological Method (boxes, arrows and the feedback loop as printed)."""
    b = []
    def box(x, y, w, h, fill, lines):
        out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="#90a4ae"/>'
        for i, ln in enumerate(lines):
            out += txt(x + w / 2, y + h / 2 + 5 - (len(lines) - 1) * 7 + i * 14, ln, 12, 'middle', 'bold', '#263238')
        return out
    def down(x, y1, y2):
        return f'<path d="M{x},{y1} L{x},{y2-6}" stroke="#263238" stroke-width="1.6"/><polygon points="{x-4},{y2-7} {x+4},{y2-7} {x},{y2}" fill="#263238"/>'
    b.append(box(140, 5, 150, 28, '#f48fb1', [L['problem']]))
    b.append(down(215, 33, 48))
    b.append(box(130, 48, 170, 34, '#ffffff', L['obs']))
    b.append(down(215, 82, 96))
    b.append(box(140, 96, 150, 34, '#fff59d', L['hyp']))
    b.append(down(215, 130, 144))
    b.append(box(140, 144, 150, 34, '#4fc3f7', L['ded']))
    b.append(down(215, 178, 192))
    b.append(box(105, 192, 220, 52, '#b3e5fc', [L['exp'], '', L['data']]))
    b.append(down(215, 213, 226))
    b.append(down(160, 244, 262) + down(280, 244, 262))
    b.append(box(95, 262, 130, 34, '#f48fb1', L['match']))
    b.append(box(232, 262, 150, 34, '#f48fb1', L['nomatch']))
    b.append(down(160, 296, 312))
    b.append(box(100, 312, 120, 26, '#f48fb1', [L['concl']]))
    b.append(down(160, 338, 352))
    b.append(box(90, 352, 140, 26, '#fff59d', [L['report']]))
    # feedback loop: from "do not match" right side up to "Development of Hypothesis"
    b.append('<path d="M382,279 L410,279 L410,113 L298,113" stroke="#263238" stroke-width="1.6" fill="none"/><polygon points="298,109 298,117 290,113" fill="#263238"/>')
    b.append(box(345, 170, 130, 34, '#fff59d', L['newhyp']))
    return svg_wrap(''.join(b), 480, 385, L['title'])


FC_EN = dict(title='Figure 2.2: Steps in a Biological Method', problem='Biological Problem', obs=['Observations and Study', 'of Background Research'],
             hyp=['Development of', 'Hypothesis'], ded=['Development of', 'Deductions'], exp='Experiments', data='Data Analysis',
             match=['Results match', 'with Hypothesis'], nomatch=['Results do not match', 'with Hypothesis'], concl='Conclusions',
             report='Reporting the Results', newhyp=['Development of', 'new Hypothesis'])
FC_UR = dict(title='شکل 2.2', problem='حیاتیاتی مسئلہ', obs=['مشاہدات اور سابقہ', 'تحقیق کا مطالعہ'], hyp=['مفروضے کی', 'تشکیل'], ded=['استنباط کی', 'تشکیل'],
             exp='تجربات', data='ڈیٹا کا تجزیہ', match=['نتائج مفروضے سے', 'مطابقت رکھتے ہیں'], nomatch=['نتائج مفروضے سے', 'مطابقت نہیں رکھتے'],
             concl='نتائج اخذ کرنا', report='نتائج کی رپورٹنگ', newhyp=['نئے مفروضے', 'کی تشکیل'])
FC_PS = dict(title='شکل 2.2', problem='بیولوژیکي ستونزه', obs=['کتنې او د پخوانۍ', 'څېړنې مطالعه'], hyp=['د فرضیې', 'جوړول'], ded=['د استنتاجونو', 'جوړول'],
             exp='تجربې', data='د معلوماتو شننه', match=['پایلې له فرضیې', 'سره سمون لري'], nomatch=['پایلې له فرضیې', 'سره سمون نه لري'],
             concl='پایلې', report='د پایلو راپور', newhyp=['د نوې فرضیې', 'جوړول'])


def sections():
    out = []
    s = Section('bio2_3', '2.3', 'Experiments on Human Beings', 'انسانوں پر تجربات', 'پر انسانانو تجربې', [34, 35])
    s.p('In the end, the hypothesis was tested by experiments on human beings. In 1898 Italian biologists allowed an Anopheles mosquito to bite a malarial patient. The infected mosquito was then allowed to bite a healthy man. This person later became ill with malaria. In this way, it was confirmed that mosquitoes transmit Plasmodium and so are involved in the spread of malaria.',
        'آخر میں مفروضے کی جانچ انسانوں پر تجربات کے ذریعے کی گئی۔ 1898ء میں اطالوی ماہرینِ حیاتیات نے ایک اینوفیلیز مچھر کو ملیریا کے مریض کو کاٹنے دیا۔ پھر اس متاثرہ مچھر کو ایک صحت مند آدمی کو کاٹنے دیا گیا۔ یہ شخص بعد میں ملیریا میں مبتلا ہو گیا۔ اس طرح تصدیق ہو گئی کہ مچھر پلازموڈیم منتقل کرتے ہیں اور اس لیے ملیریا کے پھیلاؤ میں شامل ہیں۔',
        'په پای کې فرضیه پر انسانانو د تجربو له لارې وازمویل شوه. په 1898 کال کې ایټالوي بیولوژیستانو یوې انوفلیس ماشۍ ته اجازه ورکړه چې د ملاریا ناروغ وچیچي. بیا اخته ماشۍ ته اجازه ورکړل شوه چې یو روغ سړی وچیچي. دا کس وروسته په ملاریا ناروغ شو. په دې ډول تایید شوه چې ماشي پلازموډیم لېږدوي او له همدې امله د ملاریا په خپرېدو کې ونډه لري.')
    s.fig('bio2-fig2-1', transmission(TR_EN), transmission(TR_UR), transmission(TR_PS), .95,
          caption=('Figure 2.1: Transmission of Plasmodium (Malaria) in human beings', 'شکل 2.1: انسانوں میں پلازموڈیم (ملیریا) کی منتقلی', 'شکل 2.1: په انسانانو کې د پلازموډیم (ملاریا) لېږد'))
    s.fig('bio2-fig2-2', flowchart(FC_EN), flowchart(FC_UR), flowchart(FC_PS), .75,
          caption=('Figure 2.2: Steps in a Biological Method', 'شکل 2.2: حیاتیاتی طریقے کے مراحل', 'شکل 2.2: د بیولوژیکي میتود پړاوونه'))
    out.append(s)

    s = Section('bio2_4', '2.4', 'Theory, Law and Principle', 'نظریہ، قانون اور اصول', 'تیوري، قانون او اصل', [36])
    s.p('We know that when a hypothesis has been proved by experiments, scientists keep on trying to do more experiments on it. When a hypothesis is proved by many experiments, scientists develop more hypothesis from it and test them experimentally. If the new hypothesis are again proved, the original hypothesis becomes a theory. A scientific theory explains a phenomenon. Scientists try their best to disprove the theory by disproving the hypothesis. If a theory is proved again and again by experiments, it becomes a law or principle. A scientific law is a uniform or constant fact of nature. The examples of biological laws are Hardy-Weinberg\'s law and Mendel\'s laws of inheritance.',
        'ہم جانتے ہیں کہ جب کوئی مفروضہ تجربات سے ثابت ہو جاتا ہے تو سائنس دان اس پر مزید تجربات کرنے کی کوشش جاری رکھتے ہیں۔ جب کوئی مفروضہ بہت سے تجربات سے ثابت ہو جائے تو سائنس دان اس سے مزید مفروضے بناتے ہیں اور تجربات سے ان کی جانچ کرتے ہیں۔ اگر نئے مفروضے بھی ثابت ہو جائیں تو اصل مفروضہ نظریہ بن جاتا ہے۔ سائنسی نظریہ کسی مظہر کی وضاحت کرتا ہے۔ سائنس دان مفروضے کو غلط ثابت کر کے نظریے کو غلط ثابت کرنے کی پوری کوشش کرتے ہیں۔ اگر کوئی نظریہ تجربات سے بار بار ثابت ہو تو وہ قانون یا اصول بن جاتا ہے۔ سائنسی قانون فطرت کی ایک یکساں یا مستقل حقیقت ہے۔ حیاتیاتی قوانین کی مثالیں ہارڈی وائن برگ کا قانون اور مینڈل کے توارث کے قوانین ہیں۔',
        'موږ پوهېږو چې کله یوه فرضیه په تجربو ثابته شي، ساینس پوهان پرې د نورو تجربو هڅه کوي. کله چې یوه فرضیه په ډېرو تجربو ثابته شي، ساینس پوهان ترې نورې فرضیې جوړوي او په تجربو یې ازمویي. که نوې فرضیې بیا ثابتې شي، اصلي فرضیه تیوري کېږي. ساینسي تیوري یوه پدیده تشریح کوي. ساینس پوهان هڅه کوي چې د فرضیې په ناسم ثابتولو تیوري ناسمه ثابته کړي. که یوه تیوري بیا بیا په تجربو ثابته شي، قانون یا اصل کېږي. ساینسي قانون د طبیعت یو یوشان یا ثابت حقیقت دی. د بیولوژیکي قوانینو بېلګې د هارډي واینبرګ قانون او د میندل د وراثت قوانین دي.')
    out.append(s)

    s = Section('bio2_5', '2.5', 'Data Organization and Data Analysis', 'ڈیٹا کی تنظیم اور تجزیہ', 'د معلوماتو تنظیم او شننه', [36, 37])
    s.p('We have studied that researchers collect and analyse the data (information such as names, dates, numbers, values etc.) at various steps in scientific method. This data helps them to make hypothesis from observations and to conclude results from experiments. In order to use data in scientific method, scientists have to organize and analyse it. Scientists organize the collected data in the form of graphs, tables, flow charts, maps and diagrams. The collected data is analysed by using statistical methods like ratios and proportions. A ratio is a relationship with respect to relative size between two quantities of the same kind. A pure number to a pure number; an amount of money to an amount of money; a number of people to a number of people. Proportion means to join two equal ratios.',
        'ہم پڑھ چکے ہیں کہ محققین سائنسی طریقے کے مختلف مراحل پر ڈیٹا (معلومات جیسے نام، تاریخیں، اعداد، قدریں وغیرہ) جمع کرتے اور اس کا تجزیہ کرتے ہیں۔ یہ ڈیٹا انہیں مشاہدات سے مفروضہ بنانے اور تجربات سے نتائج اخذ کرنے میں مدد دیتا ہے۔ سائنسی طریقے میں ڈیٹا استعمال کرنے کے لیے سائنس دانوں کو اسے منظم کرنا اور اس کا تجزیہ کرنا ہوتا ہے۔ سائنس دان جمع شدہ ڈیٹا کو گراف، جدول، فلو چارٹ، نقشوں اور اشکال کی صورت میں منظم کرتے ہیں۔ جمع شدہ ڈیٹا کا تجزیہ نسبت اور تناسب جیسے شماریاتی طریقوں سے کیا جاتا ہے۔ نسبت ایک ہی قسم کی دو مقداروں کے درمیان اضافی جسامت کے لحاظ سے تعلق ہے۔ خالص عدد کا خالص عدد سے؛ رقم کا رقم سے؛ لوگوں کی تعداد کا لوگوں کی تعداد سے۔ تناسب کا مطلب دو برابر نسبتوں کو جوڑنا ہے۔',
        'موږ لوستي دي چې څېړونکي د ساینسي میتود په بېلابېلو پړاوونو کې معلومات (لکه نومونه، نېټې، عددونه، ارزښتونه او نور) راټولوي او شنني. دا معلومات ورسره له کتنو د فرضیې په جوړولو او له تجربو د پایلو په اخیستلو کې مرسته کوي. په ساینسي میتود کې د معلوماتو د کارولو لپاره ساینس پوهان باید هغه تنظیم او وشنني. ساینس پوهان راټول شوي معلومات د ګرافونو، جدولونو، فلوچارټونو، نقشو او انځورونو په بڼه تنظیموي. راټول شوي معلومات د نسبت او تناسب په څېر احصایوي میتودونو شنل کېږي. نسبت د یو ډول دوو کمیتونو ترمنځ د نسبي اندازې له مخې اړیکه ده. خالص عدد له خالص عدد سره؛ پیسې له پیسو سره؛ د خلکو شمېر د خلکو له شمېر سره. تناسب یعنې د دوو مساوي نسبتونو یوځای کول.')
    s.p('a : b = c : d', 'a : b = c : d', 'a : b = c : d', math=True)
    s.p('“a” and “d” are called the extremes, “b” and “c” are called the means. The product of the extremes is equal to the product of means. When three values in a proportion are known, the fourth one (a) can be calculated by using this rule. For example, if a biologist wants to know how many sparrows would be infected with malaria if he allows Culex mosquito to bite 50 sparrows. Previously in one of his findings, he already noticed that 6 out of 10 sparrow get malaria if bitten by Culex mosquito.',
        '”a“ اور ”d“ کو طرفین (extremes) اور ”b“ اور ”c“ کو وسطین (means) کہتے ہیں۔ طرفین کا حاصلِ ضرب وسطین کے حاصلِ ضرب کے برابر ہوتا ہے۔ جب تناسب میں تین قدریں معلوم ہوں تو اس اصول سے چوتھی (a) معلوم کی جا سکتی ہے۔ مثال کے طور پر، ایک ماہرِ حیاتیات جاننا چاہتا ہے کہ اگر وہ کیولیکس مچھر کو 50 چڑیوں کو کاٹنے دے تو کتنی چڑیاں ملیریا سے متاثر ہوں گی۔ اپنی ایک سابقہ تحقیق میں وہ پہلے ہی دیکھ چکا تھا کہ کیولیکس مچھر کے کاٹنے سے 10 میں سے 6 چڑیوں کو ملیریا ہو جاتا ہے۔',
        '”a“ او ”d“ ته طرفین او ”b“ او ”c“ ته وسطین ویل کېږي. د طرفینو حاصل ضرب د وسطینو له حاصل ضرب سره برابر دی. کله چې په تناسب کې درې ارزښتونه معلوم وي، څلورم (a) د دې قاعدې په کارولو محاسبه کېدای شي. د بېلګې په توګه، یو بیولوژیست غواړي پوه شي چې که کیولیکس ماشۍ ته اجازه ورکړي چې 50 چڼچڼې وچیچي، څو به یې په ملاریا اخته شي. پخوا یې په یوه موندنه کې لیدلي وو چې د کیولیکس ماشۍ له چیچلو 10 کې 6 چڼچڼې ملاریا نیسي.')
    s.callout(STS, [('The researchers conduct their research following the scientific method. They follow all the steps of the method. Initially they develop the hypothesis through certain observations. Through the observations, deduction or induction is made. Finally, experiments are conducted to prove or disprove the hypothesis.',
                     'محققین سائنسی طریقے پر عمل کرتے ہوئے تحقیق کرتے ہیں۔ وہ اس طریقے کے تمام مراحل پر عمل کرتے ہیں۔ شروع میں وہ کچھ مشاہدات کے ذریعے مفروضہ بناتے ہیں۔ مشاہدات کے ذریعے استنباط یا استقرا کیا جاتا ہے۔ آخر میں مفروضے کو ثابت یا رد کرنے کے لیے تجربات کیے جاتے ہیں۔',
                     'څېړونکي د ساینسي میتود په تعقیب څېړنه کوي. دوی د میتود ټول پړاوونه تعقیبوي. په پیل کې د ځینو کتنو له لارې فرضیه جوړوي. د کتنو له لارې استنتاج یا استقرا کېږي. په پای کې د فرضیې د ثابتولو یا ردولو لپاره تجربې کېږي.')])
    s.p('Here he applies proportion rule.', 'یہاں وہ تناسب کا اصول لگاتا ہے۔', 'دلته هغه د تناسب قاعده کاروي.')
    s.lines([(t, t, t) for t in ['a : b = c : d', 'a : 50 = 6 : 10', 'a/50 = 6/10', 'a × 10 = 50 × 6', 'a = 30']])
    s.p('It means that if he allows Culex mosquito to bite 50 sparrows, 30 out of them will get malaria.',
        'اس کا مطلب ہے کہ اگر وہ کیولیکس مچھر کو 50 چڑیوں کو کاٹنے دے تو ان میں سے 30 کو ملیریا ہو جائے گا۔',
        'د دې معنا دا ده چې که هغه کیولیکس ماشۍ ته اجازه ورکړي چې 50 چڼچڼې وچیچي، 30 به یې ملاریا ونیسي.')
    s.p('Proportion method can be used to draw conclusions. As in the above case we can find the fourth proportion of the data if three proportions are already available.',
        'تناسب کا طریقہ نتائج اخذ کرنے کے لیے استعمال ہو سکتا ہے۔ جیسا کہ اوپر کی مثال میں، اگر تین تناسب پہلے سے موجود ہوں تو ہم ڈیٹا کا چوتھا تناسب معلوم کر سکتے ہیں۔',
        'د تناسب میتود د پایلو د اخیستلو لپاره کارېدای شي. لکه په پورتنۍ بېلګه کې، که درې تناسبونه مخکې موجود وي، موږ د معلوماتو څلورم تناسب موندلای شو.')
    out.append(s)

    s = Section('bio2_6', '2.6', 'Mathematics - as an integral part of scientific process', 'ریاضی — سائنسی عمل کا لازمی جز', 'ریاضي — د ساینسي پروسې اړین جز', [37])
    s.p('Mathematical rules have been used in biology for many decades. Recently, however, because of developments in our understanding of biology, applications of mathematical rules in all sciences has increased tremendously. For example, the research projects, such as population studies, drug studies and sequencing of plants\' and animals\' DNA, require mathematical knowledge for organising and analysing the data.',
        'ریاضیاتی اصول کئی دہائیوں سے حیاتیات میں استعمال ہو رہے ہیں۔ تاہم حال ہی میں حیاتیات کے بارے میں ہماری سمجھ میں ترقی کی وجہ سے تمام سائنسوں میں ریاضیاتی اصولوں کا اطلاق بے حد بڑھ گیا ہے۔ مثال کے طور پر، تحقیقی منصوبوں جیسے آبادی کے مطالعات، ادویات کے مطالعات اور پودوں اور جانوروں کے ڈی این اے کی ترتیب معلوم کرنے کے لیے ڈیٹا کو منظم کرنے اور اس کا تجزیہ کرنے کے لیے ریاضیاتی علم درکار ہوتا ہے۔',
        'ریاضیاتي قاعدې د لسیزو راهیسې په بیولوژي کې کارول کېږي. خو په دې وروستیو کې د بیولوژي په اړه زموږ د پوهې د پرمختګ له امله په ټولو ساینسونو کې د ریاضیاتي قاعدو کارونه ډېره زیاته شوې ده. د بېلګې په توګه، څېړنیزې پروژې لکه د نفوسو مطالعې، د درملو مطالعې او د بوټو او ژویو د ډي ان اې ترتیب معلومول، د معلوماتو د تنظیم او شننې لپاره ریاضیاتي پوهې ته اړتیا لري.')
    out.append(s)
    return out


KEY_POINTS = [
    ('The scientific method has four steps.', 'سائنسی طریقے کے چار مراحل ہیں۔', 'ساینسي میتود څلور پړاوونه لري.'),
    ('First steps is to make observations, second step is to make hypothesis and deduction, third step is to conduct experiments and fourth step is to analyze the data and draw conclusion.',
     'پہلا مرحلہ مشاہدات کرنا، دوسرا مرحلہ مفروضہ اور استنباط بنانا، تیسرا مرحلہ تجربات کرنا اور چوتھا مرحلہ ڈیٹا کا تجزیہ کر کے نتیجہ اخذ کرنا ہے۔',
     'لومړی پړاو کتنې کول، دوهم پړاو فرضیه او استنتاج جوړول، درېیم پړاو تجربې کول او څلورم پړاو د معلوماتو شننه او پایله اخیستل دي.'),
    ('When more research is carried out on a hypothesis and all the available evidence favours it then it becomes theory.',
     'جب کسی مفروضے پر مزید تحقیق کی جائے اور تمام دستیاب شواہد اس کے حق میں ہوں تو وہ نظریہ بن جاتا ہے۔',
     'کله چې پر یوې فرضیې نوره څېړنه وشي او ټول موجود شواهد یې ملاتړ وکړي، نو تیوري کېږي.'),
    ('Scientific laws must be simple, true, universal and absolute.', 'سائنسی قوانین کا سادہ، سچا، آفاقی اور مطلق ہونا ضروری ہے۔', 'ساینسي قوانین باید ساده، رښتیني، نړیوال او مطلق وي.'),
    ('Scientific laws represent the cornerstone of scientific discovery.', 'سائنسی قوانین سائنسی دریافت کا سنگِ بنیاد ہیں۔', 'ساینسي قوانین د ساینسي کشف بنسټیزه ډبره ده.'),
    ('Recorded observations and information are called data.', 'درج شدہ مشاہدات اور معلومات کو ڈیٹا کہتے ہیں۔', 'ثبت شوو کتنو او معلوماتو ته ډېټا (معلومات) ویل کېږي.'),
    ('Biology can be better understood by the use of Mathematics principles.', 'ریاضی کے اصولوں کے استعمال سے حیاتیات کو بہتر سمجھا جا سکتا ہے۔', 'د ریاضي د اصولو په کارولو بیولوژي ښه پوهېدلای شي.'),
    ('Malaria is a disease that is transmitted to people by infected mosquitoes.', 'ملیریا ایک بیماری ہے جو متاثرہ مچھروں کے ذریعے لوگوں میں منتقل ہوتی ہے۔', 'ملاریا یوه ناروغي ده چې د اخته ماشو له لارې خلکو ته لېږدول کېږي.'),
    ('Malaria is very common throughout the world. People with Malaria typically have cycles of chills and fever.', 'ملیریا پوری دنیا میں بہت عام ہے۔ ملیریا کے مریضوں کو عموماً سردی لگنے اور بخار کے دورے پڑتے ہیں۔', 'ملاریا په ټوله نړۍ کې ډېره عامه ده. د ملاریا ناروغان معمولاً د یخنۍ او تبې دورې لري.'),
]

NOTE = 'SpaceBook answer — the textbook prints no answer key for this exercise.'
MCQS = [
    ('i. Which one is the first step in biological method?', ['Hypothesis', 'Experiment', 'Observations', 'Deduction'], 2,
     NOTE + ' Of the printed options, observations come first; section 2.1 lists recognition of the problem before observations.'),
    ('ii. What is the correct experiment to know that Plasmodium destroys red blood cells?',
     ['Examine the blood of a single healthy person', 'Examine the blood of a single infected person', 'Allow mosquito to bite a healthy person and examine his blood', 'Examine the blood of some healthy and also some infected persons'], 3,
     NOTE + ' An experimental group with a control group, as in Step 3 of the malaria problem.'),
    ('iii. What is the best way to analyse the data collected from experiments?',
     ['Reading the data and drawing conclusions', 'Discussion with scientists', 'Simple calculations on calculator', 'Application of statistical formulae'], 3, NOTE + ' Section 2.5.'),
    ('iv. People who slept near smoky fire had less chance to suffer from malaria. Why?',
     ['Smoke kills Plasmodium in their blood', 'Fire increases temperature and Plasmodia are killed in air', 'Mosquitoes cannot tolerate smoke and are repelled', 'Smoke kills Plasmodium present in mosquitoes'], 2, NOTE),
    ('v. Which one of the following is NOT a characteristic of a hypothesis.',
     ['It must be consistent with all available data', 'It must be testable', 'It must be correct', 'Must make deductions'], 2,
     NOTE + ' A hypothesis is a tentative answer that can be disproved.'),
    ('vi. Deductions are made from;', ['Observations', 'Hypothesis', 'Experiment results', 'Solution of biological problem'], 1, NOTE + ' Section 2.1 (iv).'),
    ('vii. Which one of the following is true about the statement of hypothesis?', ['Logical', 'Possible answer', 'based upon observations', 'All of them'], 3, NOTE),
    ('viii. The actual answer to scientific problem is:', ['Observations', 'Hypothesis', 'Data', 'Conclusion'], 3, NOTE),
    ('ix. Which mosquito can transmit Plasmodium in human beings?', ['Anopheles', 'Culex', 'Aedes', 'All of these'], 0, NOTE + ' Figure 2.1 box.'),
    ('x. For the first time, who found Plasmodium in the blood of malarial patient?', ['Ronald Ross', 'Laveran', 'A. F. A. King', 'Mendel'], 1, NOTE + ' Laveran, 1878.'),
]
SQ = ['i. What is a science? How does it work?', 'ii. Control group is important for scientific study, How?', 'iii. What deductions were developed during the study of malaria?',
      'iv. How Ronald Ross conducted the experiment to prove that mosquitoes are involved in the spread of malaria?',
      'v. At what stage of the biological method, Hypothesis, is accepted or rejected?']
LQ = ['i. Differentiate between inductive reasoning and deductive reasoning?', 'ii. Explain how biologists use scientific method to solve the mysteries of addressing the malarial problem?',
      'iii. Explain that how mathematics can be used to interpret the data obtained through experimentation.']
PROJECT = ('Project! 1. Identify and pose meaningful, answerable scientific question/ biological problem. 2. For your biological problem: • Formulate and test a working hypothesis. '
           '• Write instructions for conducting investigations or following a procedure. • Select appropriate instruments and materials to conduct an investigation. '
           '• Describe safe laboratory procedures. • Organize data appropriately using techniques such as tables and graphs. • Analyze data to make predictions, decisions or draw conclusions. '
           '• Confirm, modify or reject a hypothesis using data analysis. • Use ratio and proportion in appropriate situations to solve problems.')


def keypoints_section():
    s = Section('bio2_keypoints', 'Key Points', 'Key Points', 'اہم نکات', 'مهم ټکي', [38])
    s.ul(KEY_POINTS)
    return s


def exercise():
    na = 'The textbook prints no answer for this question.'
    return dict(sourcePdfPages=[39, 40, 41], sourcePrintedPages=[34, 35, 36], heading='A. Encircle the best suitable answers.',
                mcqs=[dict(q=q, options=o, correct=c, explanation=e, answerOrigin='SpaceBook') for q, o, c, e in MCQS],
                shortQuestions=[dict(q=q, answer=na, sourceSection='B. Give short answers to the following questions') for q in SQ],
                detailedQuestions=[dict(q=q, answer=na, sourceSection='C. Give detailed answers to the following questions.') for q in LQ],
                activities=[dict(title='Project!', desc=PROJECT, sourcePrintedPage=36)])

LAB = 'SpaceBook-authored answer based on this unit (the textbook prints no answers):\n'
SQ_ANS = [
    'Science is the study of the world through observation and experiment. It works by the scientific method: a problem is recognized, observations are made, a hypothesis is formed, deductions are drawn, experiments test them, and conclusions are reported.',
    'A control group is examined under the same conditions but without the factor being tested. Comparing it with the experimental group shows whether the result is caused by that factor. In the malaria experiment, blood of 100 healthy persons (control) was compared with blood of 100 malarial patients (experimental).',
    '1) "If Plasmodium is the cause of malaria, then all malarial patients should have Plasmodium in their blood." 2) "If mosquitoes transmit Plasmodium, then Plasmodium should be present in mosquitoes."',
    'Ross let a female Anopheles mosquito bite a malarial patient and found Plasmodium multiplying in its stomach. He then used sparrows: a female Culex mosquito bit a sparrow with malaria; Plasmodium multiplied in the stomach wall and moved to the salivary glands. Infected mosquitoes bit healthy sparrows, which got malaria and had many Plasmodium in their blood.',
    'At the experiment and data-analysis stage. If the results match the hypothesis it is accepted (conclusions); if they do not match, it is rejected and a new hypothesis is developed (Figure 2.2).',
]
LQ_ANS = [
    'Deductive reasoning starts from a hypothesis taken as true and draws its logical consequences using "if ... then" (e.g. "If all plant cells have a nucleus, then a nucleus will be observed in each cell of a blade of grass"). Inductive reasoning works the other way: from many specific observations a general statement or hypothesis is built (e.g. King\'s observations on sleeping outdoors, smoky fires and mosquito nets led to the hypothesis "Mosquitoes transmit Plasmodium"). The unit notes that through observations "deduction or induction is made".',
    'Problem 1 (cause of malaria): observations linked malaria with marshes and "bad air"; Laveran (1878) saw microorganisms, later named Plasmodium, in patients\' blood. Hypothesis: "Plasmodium is the cause of malaria"; deduction: all patients should have Plasmodium in their blood. Experiment: blood of 100 patients (experimental group) and 100 healthy persons (control group); only patients had Plasmodium, so the hypothesis was accepted. Problem 2 (transmission): King (1883) listed observations; hypothesis "Mosquitoes transmit Plasmodium"; deduction: Plasmodium should be present in mosquitoes. Ross\'s mosquito and sparrow experiments proved it, and in 1898 Italian biologists confirmed it in human beings.',
    'Data is organized in graphs, tables, flow charts, maps and diagrams and analysed with statistical methods such as ratio and proportion. In a proportion a : b = c : d the product of the extremes equals the product of the means, so a fourth value can be found from three known ones. Example: if 6 of 10 sparrows get malaria from Culex bites, then for 50 sparrows a : 50 = 6 : 10, a × 10 = 50 × 6, a = 30. Population studies, drug studies and DNA sequencing all need such mathematics.',
]


def exercise():
    return dict(sourcePdfPages=[39, 40, 41], sourcePrintedPages=[34, 35, 36], heading='A. Encircle the best suitable answers.',
                mcqs=[dict(q=q, options=o, correct=c, explanation=e, answerOrigin='SpaceBook') for q, o, c, e in MCQS],
                shortQuestions=[dict(q=q, answer=LAB + a, sourceSection='B. Give short answers to the following questions') for q, a in zip(SQ, SQ_ANS)],
                detailedQuestions=[dict(q=q, answer=LAB + a, sourceSection='C. Give detailed answers to the following questions.') for q, a in zip(LQ, LQ_ANS)],
                activities=[dict(title='Project!', desc=PROJECT, sourcePrintedPage=36)])
