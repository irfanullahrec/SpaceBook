# -*- coding: utf-8 -*-
"""Unit 8 part B — PDF 162-167 (printed 159-164): water b-g, 8.4 balanced diet (Tables 8.2-8.4), 8.5 malnutrition."""
from bio9_tools import Section, photo_figure, svg_wrap, txt

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')
AI = ('Analysing and Interpreting', 'تجزیہ اور توضیح', 'شننه او تفسیر')


def water_rest(s):
    s.lines([
        ('b. The water present in blood dissolves oxygen from lungs. In this way, oxygen is transported to cells. Carbon dioxide is transported from cells to lungs in the same way. Similarly, water carries nutrients from digestive system to all cells of the body.',
         'b. خون میں موجود پانی پھیپھڑوں سے آکسیجن حل کرتا ہے۔ اس طرح آکسیجن خلیوں تک پہنچتی ہے۔ کاربن ڈائی آکسائیڈ اسی طرح خلیوں سے پھیپھڑوں تک پہنچتی ہے۔ اسی طرح پانی نظامِ انہضام سے غذائی اجزا جسم کے تمام خلیوں تک لے جاتا ہے۔',
         'b. په وینه کې اوبه له سږو اکسیجن حلوي. په دې ډول اکسیجن حجرو ته رسېږي. کاربن ډای اکساید هم په همدې ډول له حجرو سږو ته وړل کېږي. همدارنګه اوبه غذايي مواد د هضم له سیسټم د بدن ټولو حجرو ته وړي.'),
        ('c. Almost every cell in the body is bathed in interstitial fluid which is almost entirely water.', 'c. جسم کا تقریباً ہر خلیہ بین الخلوی سیال میں ڈوبا ہوتا ہے جو تقریباً مکمل طور پر پانی ہے۔', 'c. د بدن نږدې هره حجره په بین الحجروي مایع کې ډوبه ده چې نږدې ټوله اوبه ده.'),
        ('d. Water acts as a reactant in many metabolic reactions e.g. in hydrolysis reactions.', 'd. پانی بہت سے میٹابولک تعاملات میں متعامل کا کام کرتا ہے مثلاً ہائیڈرولیسس تعاملات میں۔', 'd. اوبه په ډېرو میټابولیکي تعاملونو کې د متعامل کار کوي لکه د هایډرولیزس تعاملونو کې.'),
        ('e. Water is a great stabilizer of body temperature. It absorbs and releases heat very slowly.', 'e. پانی جسم کے درجۂ حرارت کو بہترین طور پر مستحکم رکھتا ہے۔ یہ حرارت بہت آہستہ جذب اور خارج کرتا ہے۔', 'e. اوبه د بدن د تودوخې لوی ثابتوونکی دی. تودوخه ډېره ورو جذبوي او خوشې کوي.'),
        ('f. Water also acts as a lubricating medium. It is the major part of mucous and other lubricating fluids.', 'f. پانی چکنا کرنے والے واسطے کا کام بھی کرتا ہے۔ یہ بلغم اور دوسرے چکنا کرنے والے سیالوں کا بڑا حصہ ہے۔', 'f. اوبه د غوړوونکي منځني کار هم کوي. د بلغم او نورو غوړوونکو مایعاتو لویه برخه ده.'),
        ('g. Water is the flushing medium for the removal of toxic chemicals e.g. urea through kidneys.', 'g. پانی زہریلے کیمیکلز مثلاً یوریا کو گردوں کے ذریعے خارج کرنے کا واسطہ ہے۔', 'g. اوبه د زهرجنو کیمیاوي موادو لکه یوریا د پښتورګو له لارې د ایستلو منځنی دی.'),
    ])


def thyroid(L):
    neck = ('<path d="M150,10 C130,40 130,70 120,95 L280,95 C270,70 270,40 250,10 Z" fill="#f8bbd0" stroke="#c2185b"/>'
            '<ellipse cx="200" cy="72" rx="26" ry="14" fill="#e57373"/>')

    def box(x, big):
        b = f'<rect x="{x}" y="120" width="150" height="110" fill="#fce4ec" stroke="#555"/>'
        b += f'<rect x="{x+65}" y="125" width="20" height="100" rx="8" fill="#f48fb1"/>'
        if big:
            b += (f'<ellipse cx="{x+50}" cy="180" rx="34" ry="40" fill="#d81b60" opacity=".85"/>'
                  f'<ellipse cx="{x+100}" cy="180" rx="34" ry="40" fill="#d81b60" opacity=".85"/>')
        else:
            b += (f'<ellipse cx="{x+62}" cy="180" rx="12" ry="22" fill="#d81b60"/><ellipse cx="{x+88}" cy="180" rx="12" ry="22" fill="#d81b60"/>'
                  f'<rect x="{x+65}" y="182" width="20" height="8" fill="#d81b60"/>')
        return b
    body = neck + box(40, False) + box(230, True)
    body += '<path d="M100,40 L185,70" stroke="#333"/>' + txt(95, 44, L['goitre'], 13, 'end', 'bold')
    body += txt(115, 250, L['normal'], 13, 'middle', 'bold') + txt(305, 250, L['enlarged'], 13, 'middle', 'bold')
    return svg_wrap(body, 420, 262, L['title'])


TH = {'en': dict(title='Figure 8.7: Thyroid', goitre='Goitre', normal='Normal thyroid', enlarged='Enlarged thyroid'),
      'ur': dict(title='شکل 8.7', goitre='گلہڑ', normal='نارمل تھائیرائیڈ', enlarged='بڑھا ہوا تھائیرائیڈ'),
      'ps': dict(title='شکل 8.7', goitre='جاغور', normal='عادي تایرایډ', enlarged='لوی شوی تایرایډ')}


def photo1(n, en, ur, ps):
    return [photo_figure(n, [('', t)], c, w=320, cols=1, cell_h=150) for t, c in
            ((en, 'Photograph in the book'), (ur, 'کتاب میں تصویر'), (ps, 'په کتاب کې انځور'))]


def sections(sec_8_3):
    water_rest(sec_8_3)
    sec_8_3.pdf_pages = sorted(set(sec_8_3.pdf_pages) | {162})
    out = []

    s = Section('bio8_4', '8.4', 'Balanced Diet', 'متوازن غذا', 'متوازن خوراک', [162, 163, 164])
    foods = [('Bread (Roti)', 'روٹی', 'ډوډۍ', '52%', '52%', '9%'), ('Rice (cooked)', 'چاول (پکے ہوئے)', 'وريجې (پخې)', '23%', '0.1%', '2.2%'), ('Banana', 'کیلا', 'کېله', '20%', '0.5%', '1.0%'),
             ('Potato', 'آلو', 'کچالو', '19%', '0.1%', '2%'), ('Peas', 'مٹر', 'مټر', '16.7%', '0.5%', '5.2%'), ('Apples', 'سیب', 'مڼې', '12.8%', '0.5%', '0.3%'), ('Cabbage', 'بند گوبھی', 'ګوبي', '5.5%', '0.3%', '1.2%'),
             ('Spinach (palak saag)', 'پالک (پالک ساگ)', 'پالک', '3.2%', '0.3%', '1.6%'), ('Eggs', 'انڈے', 'هګۍ', '0.7%', '12%', '13%'), ('Milk', 'دودھ', 'شیدې', '4%', '4%', '3%'), ('Butter', 'مکھن', 'کوچ', '0.4%', '81%', '0.6%'),
             ('Cheese', 'پنیر', 'پنیر', '2%', '32%', '25%'), ('Meat', 'گوشت', 'غوښه', '0', '30%', '22%'), ('Chicken', 'مرغی', 'چرګ', '0', '11%', '20%'), ('Fish', 'مچھلی', 'کب', '0', '0.4%', '17%')]
    s.h('8.4 Balanced Diet', '8.4 متوازن غذا', '8.4 متوازن خوراک')
    s.p('Our diet is, quite simply, what we eat. "A balanced diet contains carbohydrate, protein, fat, vitamins, minerals and fiber in the correct proportions."',
        'ہماری غذا سیدھے لفظوں میں وہ ہے جو ہم کھاتے ہیں۔ ”متوازن غذا میں کاربوہائیڈریٹ، پروٹین، چکنائی، وٹامنز، معدنیات اور ریشہ درست تناسب میں ہوتے ہیں۔“',
        'زموږ خوراک په ساده ډول هغه څه دي چې موږ یې خورو. ”متوازن خوراک کاربوهایډریټ، پروټین، غوړ، ویټامینونه، معدنونه او فایبر په سم تناسب لري.“')
    s.p('We must have carbohydrate, protein, fat, vitamins, minerals and fiber in the correct proportions. If there is not enough protein, we will not be able to grow properly and to repair ourselves i.e. wounds will not heal properly. If we do not have enough energy containing foods we will feel tired. If we have too much energy containing foods we will become overweight. Similarly, our diet should also provide a regular supply of vitamins and minerals for optimum health.',
        'ہمیں کاربوہائیڈریٹ، پروٹین، چکنائی، وٹامنز، معدنیات اور ریشہ درست تناسب میں لینا چاہیے۔ اگر پروٹین کافی نہ ہو تو ہم ٹھیک طرح بڑھ نہیں سکیں گے اور اپنی مرمت نہیں کر سکیں گے یعنی زخم ٹھیک سے نہیں بھریں گے۔ اگر توانائی والی غذائیں کافی نہ ہوں تو ہم تھکاوٹ محسوس کریں گے۔ اگر توانائی والی غذائیں بہت زیادہ ہوں تو ہمارا وزن زیادہ ہو جائے گا۔ اسی طرح ہماری غذا کو بہترین صحت کے لیے وٹامنز اور معدنیات کی باقاعدہ فراہمی بھی کرنی چاہیے۔',
        'موږ باید کاربوهایډریټ، پروټین، غوړ، ویټامینونه، معدنونه او فایبر په سم تناسب ولرو. که پروټین بس نه وي، په سمه توګه وده او ځان ترمیم نه شو کولای یعنې ټپونه به سم نه رغېږي. که د انرژۍ لرونکي خواړه بس نه وي، ستړیا به احساس کړو. که د انرژۍ لرونکي خواړه ډېر وي، وزن به مو زیات شي. همدارنګه زموږ خوراک باید د غوره روغتیا لپاره د ویټامینونو او معدنونو منظم رسول هم برابر کړي.')
    s.table('bio8-tab8-2', ['Food', 'Carbohydrate', 'Fat', 'Protein'], [[f[0], *f[3:]] for f in foods],
            ['خوراک', 'کاربوہائیڈریٹ', 'چکنائی', 'پروٹین'], [[f[1], *f[3:]] for f in foods],
            ['خواړه', 'کاربوهایډریټ', 'غوړ', 'پروټین'], [[f[2], *f[3:]] for f in foods], ratio=.55,
            caption=('Table 8.2: Common foods and their Composition', 'جدول 8.2: عام غذائیں اور ان کی ترکیب', 'جدول 8.2: عام خواړه او د هغوی جوړښت'))
    s.p('SpaceBook note: Table 8.2 prints 52% fat for bread (roti), the same figure as its carbohydrate. Wheat roti normally contains only a few percent fat, so this value appears to be a printing error. The printed value is kept.',
        'اسپیس بک نوٹ: جدول 8.2 میں روٹی کے لیے چکنائی 52% چھپی ہے جو اس کے کاربوہائیڈریٹ کے برابر ہے۔ گندم کی روٹی میں عموماً صرف چند فیصد چکنائی ہوتی ہے، اس لیے یہ قدر چھپائی کی غلطی معلوم ہوتی ہے۔ چھپی ہوئی قدر رکھی گئی ہے۔',
        'د سپېس بوک یادونه: جدول 8.2 د ډوډۍ لپاره 52% غوړ چاپ کړی چې د کاربوهایډریټ سره برابر دی. د غنمو ډوډۍ معمولاً یوازې څو سلنه غوړ لري، نو دا ارزښت د چاپ تېروتنه ښکاري. چاپ شوی ارزښت ساتل شوی.', editorial=True)
    s.p('The amount of each component of balanced diet is determined according to the energy requirements. The energy requirements are not same for all. Diet and energy requirements are always related to age, gender and activity of individual.',
        'متوازن غذا کے ہر جز کی مقدار توانائی کی ضروریات کے مطابق طے کی جاتی ہے۔ توانائی کی ضروریات سب کے لیے یکساں نہیں ہوتیں۔ غذا اور توانائی کی ضروریات ہمیشہ فرد کی عمر، جنس اور سرگرمی سے متعلق ہوتی ہیں۔',
        'د متوازن خوراک د هرې برخې مقدار د انرژۍ د اړتیاوو له مخې ټاکل کېږي. د انرژۍ اړتیاوې د ټولو لپاره یو شان نه دي. خوراک او د انرژۍ اړتیاوې تل د فرد له عمر، جنس او فعالیت سره تړلې وي.')
    s.h('(i) Relationship of Energy Requirements with Age', '(i) توانائی کی ضروریات کا عمر سے تعلق', '(i) د انرژۍ د اړتیاوو اړیکه له عمر سره')
    s.p('During growth period, new cells are formed at a greater rate and cells expend more energy. So the body needs foods that contain more energy. Children at the age of 13-15 years need more food per kilogram of body weight than adults. Similarly, children need more calcium and iron for their growing bones and red blood cells respectively.',
        'نشوونما کے دور میں نئے خلیے زیادہ شرح سے بنتے ہیں اور خلیے زیادہ توانائی خرچ کرتے ہیں۔ اس لیے جسم کو زیادہ توانائی والی غذائیں درکار ہوتی ہیں۔ 13-15 سال کی عمر کے بچوں کو بالغوں کی نسبت فی کلوگرام جسمانی وزن زیادہ خوراک درکار ہوتی ہے۔ اسی طرح بچوں کو بالترتیب بڑھتی ہڈیوں اور سرخ خونی خلیوں کے لیے زیادہ کیلشیم اور آئرن درکار ہوتا ہے۔',
        'د ودې په دوره کې نوې حجرې په لوړه کچه جوړېږي او حجرې ډېره انرژي مصرفوي. نو بدن ډېرې انرژۍ لرونکو خوړو ته اړتیا لري. د 13-15 کلونو ماشومان د لویانو په پرتله د بدن د وزن په هر کیلوګرام ډېرو خوړو ته اړتیا لري. همدارنګه ماشومان په ترتیب سره د وده کوونکو هډوکو او سرو وینې حجرو لپاره ډېر کلسیم او اوسپنې ته اړتیا لري.')
    s.h('(ii) Relationship of Energy Requirements with Gender', '(ii) توانائی کی ضروریات کا جنس سے تعلق', '(ii) د انرژۍ د اړتیاوو اړیکه له جنس سره')
    s.p('Women have a comparatively lower metabolic rate than men of the same age and weight. So men need foods that provide more energy.',
        'خواتین کی میٹابولک شرح اسی عمر اور وزن کے مردوں کے مقابلے میں نسبتاً کم ہوتی ہے۔ اس لیے مردوں کو زیادہ توانائی دینے والی غذائیں درکار ہیں۔',
        'د ښځو میټابولیکي کچه د همغه عمر او وزن له نارینه وو نسبتاً ټیټه ده. نو نارینه ډېرې انرژۍ ورکوونکو خوړو ته اړتیا لري.')
    s.h('(iii) Relationship of Energy Requirements with Activity', '(iii) توانائی کی ضروریات کا سرگرمی سے تعلق', '(iii) د انرژۍ د اړتیاوو اړیکه له فعالیت سره')
    s.p('People have different lifestyles and varied nature of work. A man with sedentary habits does not require as much energy as the man who remains physically active for most of the day.',
        'لوگوں کے طرزِ زندگی اور کام کی نوعیت مختلف ہوتی ہے۔ بیٹھے رہنے کی عادت والے شخص کو اتنی توانائی درکار نہیں جتنی دن کا زیادہ حصہ جسمانی طور پر متحرک رہنے والے کو۔',
        'خلک بېلابېل ژوند ډولونه او د کار بېلابېله بڼه لري. هغه سړی چې ناست ژوند لري دومره انرژۍ ته اړتیا نه لري لکه هغه چې د ورځې ډېره برخه بدني فعال وي.')
    s.p('SpaceBook note: the three sub-headings on PDF 163 are partly faded in the scan. They are completed from their visible words and the parallel wording of the paragraphs.',
        'اسپیس بک نوٹ: PDF 163 پر تینوں ذیلی عنوانات اسکین میں جزوی طور پر دھندلے ہیں۔ انہیں نظر آنے والے الفاظ اور پیراگرافوں کی متوازی عبارت سے مکمل کیا گیا ہے۔',
        'د سپېس بوک یادونه: په PDF 163 کې درې فرعي سرلیکونه په سکن کې یو څه تت دي. د ښکاره کلمو او د پراګرافونو د موازي متن له مخې بشپړ شوي.', editorial=True)
    t3 = [('Carbohydrates', 'کاربوہائیڈریٹس', 'کاربوهایډریټونه', '45-65%', '264-382g', '344-500g', '215-310g', '280-404g'),
          ('Proteins', 'پروٹینز', 'پروټینونه', '10-15%', '58-88g', '76-115g', '48-72g', '62-93g'),
          ('Fats', 'چکنائی', 'غوړ', '20-35%', '54-95g', '70-123g', '44-77g', '57-100g')]
    s.table('bio8-tab8-3', ['', 'Percentage of daily diet', 'Male (80 kg) Sedentary', 'Male (80 kg) Active', 'Female (65 kg) Sedentary', 'Female (65kg) Active'], [[r[0], *r[3:]] for r in t3],
            ['', 'روزانہ غذا کا فیصد', 'مرد (80 kg) کم متحرک', 'مرد (80 kg) متحرک', 'خاتون (65 kg) کم متحرک', 'خاتون (65kg) متحرک'], [[r[1], *r[3:]] for r in t3],
            ['', 'د ورځني خوراک سلنه', 'نارینه (80 kg) ناست', 'نارینه (80 kg) فعال', 'ښځینه (65 kg) ناسته', 'ښځینه (65kg) فعاله'], [[r[2], *r[3:]] for r in t3], ratio=.85,
            caption=('Table 8.3: Recommended daily requirements of Carbohydrates (energy), Proteins and Fats for adults', 'جدول 8.3: بالغوں کے لیے کاربوہائیڈریٹس (توانائی)، پروٹینز اور چکنائی کی تجویز کردہ روزانہ ضروریات', 'جدول 8.3: د لویانو لپاره د کاربوهایډریټونو (انرژۍ)، پروټینونو او غوړو سپارښتل شوې ورځنۍ اړتیاوې'))
    s.callout(AI, [('Record a weekly chart of your daily diet. Compare it with the balanced diet requirements.', 'اپنی روزانہ غذا کا ہفتہ وار چارٹ بنائیں۔ اس کا متوازن غذا کی ضروریات سے موازنہ کریں۔', 'د خپل ورځني خوراک اوونیز چارټ ثبت کړئ. له متوازن خوراک اړتیاوو سره یې پرتله کړئ.')])
    G = {'Child': ('بچہ', 'ماشوم'), 'Female': ('خاتون', 'ښځینه'), 'Male': ('مرد', 'نارینه')}
    t4 = [('Child', '2-3', '1,000', '1,000 - 1,400', '1,000 - 1,400'), ('Female', '4-8', '1,200', '1,400 - 1,600', '1,400 - 1,800'), ('Female', '9-13', '1,600', '1,600 - 2,000', '1,800 - 2,000'),
          ('Female', '14-18', '1,800', '2,000', '2,400'), ('Female', '19-30', '2,000', '2,000 - 2,200', '2,400'), ('Female', '31-50', '1,800', '2,000', '2,200'), ('Female', '51+', '1,600', '1,800', '2,000 - 2,200'),
          ('Male', '4-8', '1,400', '1,400 - 1,600', '1,600 - 2,000'), ('Male', '9-13', '1,800', '1,800 - 2,200', '2,000 - 2,600'), ('Male', '14-18', '2,200', '2,400 - 2,800', '2,800 - 3,200'),
          ('Male', '19-30', '2,400', '2,600 - 2,800', '3,000'), ('Male', '31-50', '2,200', '2,400 - 2,600', '2,800 - 3,000'), ('Male', '51+', '2,000', '2,200 - 2,400', '2,400 - 2,800')]
    s.table('bio8-tab8-4', ['Gender', 'Age (years)', 'Sedentary', 'Moderately Active', 'Active'], [list(r) for r in t4],
            ['جنس', 'عمر (سال)', 'کم متحرک', 'معتدل متحرک', 'متحرک'], [[G[r[0]][0], *r[1:]] for r in t4],
            ['جنس', 'عمر (کلونه)', 'ناست', 'منځنی فعال', 'فعال'], [[G[r[0]][1], *r[1:]] for r in t4], ratio=.85,
            caption=('Table 8.4: Estimated Energy Requirements (in kilocalories) for each Gender and age group as per the activity level', 'جدول 8.4: سرگرمی کی سطح کے مطابق ہر جنس اور عمر کے گروہ کے لیے تخمینی توانائی کی ضروریات (کلو کیلوریز میں)', 'جدول 8.4: د فعالیت د کچې له مخې د هر جنس او عمر ډلې لپاره اټکل شوې د انرژۍ اړتیاوې (په کیلوکالوریو)'))
    s.p('In the book the three activity columns (Sedentary, Moderately Active, Active) are grouped under one "Activity Level" header.', 'کتاب میں سرگرمی کے تینوں کالم (کم متحرک، معتدل متحرک، متحرک) ایک ”سرگرمی کی سطح“ کے عنوان کے نیچے ہیں۔', 'په کتاب کې د فعالیت درې ستنې (ناست، منځنی فعال، فعال) د یوه ”د فعالیت کچه“ سرلیک لاندې دي.', editorial=True)
    out.append(s)

    s = Section('bio8_5', '8.5', 'Malnutrition', 'سوئے تغذیہ', 'سوءتغذیه', [164, 165, 166, 167])
    s.h('8.5 Malnutrition', '8.5 سوئے تغذیہ', '8.5 سوءتغذیه')
    s.p('Taking a diet in which the required nutrients are not in enough quantity or over the required quantity is called malnutrition. Under nutrition is a consequence of consuming low amount of essential nutrients while over nutrition means taking too much nutrients. Severe malnutrition may result in death, heart diseases, constipation and obesity. The major types of malnutrition are Protein-Energy Malnutrition (PEM), Mineral Deficiency Diseases (MDD) and Over Intake of Nutrients (OIN).',
        'ایسی غذا لینا جس میں درکار غذائی اجزا کافی مقدار میں نہ ہوں یا درکار مقدار سے زیادہ ہوں، سوئے تغذیہ کہلاتا ہے۔ کم غذائیت ضروری غذائی اجزا کی کم مقدار کھانے کا نتیجہ ہے جبکہ زیادہ غذائیت کا مطلب بہت زیادہ غذائی اجزا لینا ہے۔ شدید سوئے تغذیہ موت، دل کی بیماریوں، قبض اور موٹاپے کا باعث بن سکتا ہے۔ سوئے تغذیہ کی بڑی اقسام پروٹین انرجی مال نیوٹریشن (PEM)، معدنی کمی کی بیماریاں (MDD) اور غذائی اجزا کا زیادہ استعمال (OIN) ہیں۔',
        'داسې خوراک اخیستل چې اړین غذايي مواد پکې بس مقدار نه وي یا له اړین مقدار ډېر وي سوءتغذیه بلل کېږي. کمه تغذیه د اړینو غذايي موادو د لږ مقدار د خوړلو پایله ده او ډېره تغذیه د ډېرو غذايي موادو اخیستل دي. سخته سوءتغذیه ښايي د مړینې، زړه ناروغیو، قبضیت او چاغښت لامل شي. د سوءتغذیې لوی ډولونه د پروټین انرژۍ سوءتغذیه (PEM)، معدني کمښت ناروغۍ (MDD) او د غذايي موادو زیات اخیستل (OIN) دي.')
    s.h('A- Protein-Energy Malnutrition (PEM)', 'A- پروٹین انرجی مال نیوٹریشن (PEM)', 'A- د پروټین انرژۍ سوءتغذیه (PEM)')
    s.p('The term Protein-Energy Malnutrition (PEM) applies to a condition in which the body is not getting required amounts of proteins or any energy producing nutrients (carbohydrates, proteins, lipids). It may also occur when the body cannot absorb such nutrients due to other diseases (e.g. AIDS or cancer). Two important diseases associated with PEM are marasmus and kwashiorkor.',
        'پروٹین انرجی مال نیوٹریشن (PEM) کی اصطلاح ایسی حالت پر لاگو ہوتی ہے جس میں جسم کو پروٹینز یا توانائی پیدا کرنے والے غذائی اجزا (کاربوہائیڈریٹس، پروٹینز، لپڈز) کی درکار مقدار نہیں مل رہی۔ یہ اس وقت بھی ہو سکتا ہے جب جسم دوسری بیماریوں (مثلاً ایڈز یا کینسر) کی وجہ سے ایسے غذائی اجزا جذب نہ کر سکے۔ PEM سے وابستہ دو اہم بیماریاں میرازمس اور کواشیورکور ہیں۔',
        'د پروټین انرژۍ سوءتغذیې (PEM) اصطلاح په هغه حالت کارېږي چې بدن د پروټینونو یا انرژي تولیدوونکو غذايي موادو (کاربوهایډریټونو، پروټینونو، لیپیډونو) اړین مقدار نه ترلاسه کوي. دا هغه وخت هم پېښېدای شي چې بدن د نورو ناروغیو (لکه ایډز یا سرطان) له امله داسې غذايي مواد جذب نه کړای شي. له PEM سره تړلې دوه مهمې ناروغۍ مرازمس او کواشیورکور دي.')
    s.callout(SI, [('Soya beans are used as a major source of protein in many different forms and soya milk has been found to be a good substitute for more costly cow or goat milk.', 'سویا بین کئی مختلف شکلوں میں پروٹین کے بڑے ذریعے کے طور پر استعمال ہوتی ہے اور سویا دودھ زیادہ مہنگے گائے یا بکری کے دودھ کا اچھا متبادل پایا گیا ہے۔', 'سویا لوبیا په ډېرو بېلابېلو بڼو د پروټین د لویې سرچینې په توګه کارېږي او د سویا شیدې د ګرانو غوا یا وزې شیدو ښه بدیل موندل شوي.')])
    s.h('i. Marasmus', 'i. میرازمس', 'i. مرازمس')
    s.p('This type of PEM occurs in children due to very low intake of carbohydrates, fats and protein. Children suffering from marasmus have very thin bodies. Their body weight is less than 60 percent of the expected weight for their age. They have almost no fats and muscle strength in their bodies. They also suffer from low body temperature and anaemia. Marasmus can be treated by adding all nutrients to the diet. In severe cases, this disease may lead to death.',
        'PEM کی یہ قسم بچوں میں کاربوہائیڈریٹس، چکنائی اور پروٹین کی بہت کم مقدار لینے سے ہوتی ہے۔ میرازمس کے شکار بچوں کے جسم بہت دبلے ہوتے ہیں۔ ان کا جسمانی وزن ان کی عمر کے متوقع وزن کے 60 فیصد سے کم ہوتا ہے۔ ان کے جسم میں چکنائی اور عضلاتی طاقت تقریباً نہیں ہوتی۔ وہ جسم کے کم درجۂ حرارت اور انیمیا کا بھی شکار ہوتے ہیں۔ میرازمس کا علاج غذا میں تمام غذائی اجزا شامل کر کے کیا جا سکتا ہے۔ شدید صورتوں میں یہ بیماری موت کا باعث بن سکتی ہے۔',
        'د PEM دا ډول په ماشومانو کې د کاربوهایډریټونو، غوړو او پروټین د ډېر لږ اخیستو له امله پېښېږي. په مرازمس اخته ماشومان ډېر نري بدنونه لري. د بدن وزن یې د خپل عمر د تمه شوي وزن له 60 سلنې لږ وي. په بدن کې یې نږدې غوړ او عضلي ځواک نه وي. د بدن له ټیټې تودوخې او کم خونۍ هم ځوریږي. مرازمس خوراک ته د ټولو غذايي موادو په ورزیاتولو درملېدای شي. په سختو پېښو کې دا ناروغي ښايي د مړینې لامل شي.')
    s.fig('bio8-fig8-5', *photo1('Figure 8.5', 'Child suffering from Marasmus', 'میرازمس کا شکار بچہ', 'په مرازمس اخته ماشوم'), .3,
          caption=('Figure 8.5: Child suffering from Marasmus', 'شکل 8.5: میرازمس کا شکار بچہ', 'شکل 8.5: په مرازمس اخته ماشوم'))
    s.h('ii. Kwashiorkor', 'ii. کواشیورکور', 'ii. کواشیورکور')
    s.p('Kwashiorkor is a more severe form of PEM. It occurs in children or adults due to inadequate intake of proteins. The Kwashiorkor patients are very thin but have swollen stomach. They also suffer from thinning of hair and loss of teeth. Their body fails to produce antibodies against diseases. Kwashiorkor can be treated by adding proteins to the diet. In severe cases, this disease may also lead to death.',
        'کواشیورکور PEM کی زیادہ شدید شکل ہے۔ یہ بچوں یا بالغوں میں پروٹینز کی ناکافی مقدار لینے سے ہوتا ہے۔ کواشیورکور کے مریض بہت دبلے ہوتے ہیں لیکن ان کا پیٹ سوجا ہوتا ہے۔ ان کے بال پتلے ہو جاتے ہیں اور دانت گر جاتے ہیں۔ ان کا جسم بیماریوں کے خلاف اینٹی باڈیز بنانے میں ناکام رہتا ہے۔ کواشیورکور کا علاج غذا میں پروٹینز شامل کر کے کیا جا سکتا ہے۔ شدید صورتوں میں یہ بیماری بھی موت کا باعث بن سکتی ہے۔',
        'کواشیورکور د PEM سخت ډول دی. په ماشومانو یا لویانو کې د پروټینونو د ناکافي اخیستو له امله پېښېږي. د کواشیورکور ناروغان ډېر نري وي خو ګېډه یې پړسېدلې وي. وېښتان یې نري کېږي او غاښونه یې لوېږي. بدن یې د ناروغیو پر وړاندې د انټي باډيو په جوړولو کې پاتې راځي. کواشیورکور خوراک ته د پروټینونو په ورزیاتولو درملېدای شي. په سختو پېښو کې دا ناروغي هم ښايي د مړینې لامل شي.')
    s.fig('bio8-fig8-6', *photo1('Figure 8.6', 'Child suffering from Kwashiorkor', 'کواشیورکور کا شکار بچہ', 'په کواشیورکور اخته ماشوم'), .3,
          caption=('Figure 8.6: Child suffering from Kwashiorkor', 'شکل 8.6: کواشیورکور کا شکار بچہ', 'شکل 8.6: په کواشیورکور اخته ماشوم'))
    s.h('B- Mineral Deficiency Diseases (MDD)', 'B- معدنی کمی کی بیماریاں (MDD)', 'B- معدني کمښت ناروغۍ (MDD)')
    s.p("Mineral deficiencies occur when a person's mineral intake consistently falls below the recommended requirement. Mineral deficiencies can lead to a variety of diseases e.g. anaemia, goiter, osteoporosis and rickets.",
        'معدنی کمی اس وقت ہوتی ہے جب کسی شخص کا معدنیات کا استعمال مسلسل تجویز کردہ ضرورت سے کم رہے۔ معدنی کمی مختلف بیماریوں کا باعث بن سکتی ہے مثلاً انیمیا، گلہڑ، اوسٹیوپوروسس اور رکٹس۔',
        'معدني کمښت هغه وخت پېښېږي چې د یو کس د معدنونو اخیستل په دوامداره توګه له سپارښتل شوې اړتیا ټیټ وي. معدني کمښت ښايي د بېلابېلو ناروغیو لامل شي لکه کم خوني، جاغور، اوسټیوپوروزس او ریکټس.')
    s.callout(('Activity 8.2', 'سرگرمی 8.2', 'فعالیت 8.2'), [('The quality and quantity of food intake affects health and therefore, poor food intake may lead to certain food related disorders. Mention few of such disorders from your own environment, discuss how they are affecting the general population and how the nutrition could be improved considering the economic conditions of the people.',
        'خوراک کا معیار اور مقدار صحت کو متاثر کرتے ہیں اس لیے ناقص خوراک بعض غذا سے متعلق خرابیوں کا باعث بن سکتی ہے۔ اپنے ماحول سے ایسی چند خرابیاں بتائیں، بحث کریں کہ یہ عام آبادی کو کیسے متاثر کر رہی ہیں اور لوگوں کے معاشی حالات کو مدِنظر رکھتے ہوئے غذائیت کیسے بہتر بنائی جا سکتی ہے۔',
        'د خوړو کیفیت او مقدار پر روغتیا اغېز کوي او له همدې امله کمزوری خوراک ښايي له خوړو سره تړلو ځینو اختلالاتو ته لار هواره کړي. له خپل چاپېریاله داسې څو اختلالات یاد کړئ، وڅېړئ چې څنګه پر عام نفوس اغېز کوي او د خلکو اقتصادي حالت ته په پام تغذیه څنګه ښه کېدای شي.')])
    s.lines([
        ('(i) Anaemia means lesser than normal quantity of red blood cells or haemoglobin in blood. It occurs when the body has poor iron intake or poor absorption of iron. When there is deficiency of iron in the body, it cannot make the required number of red blood cells. The common symptom of anaemia is constant fatigue and weakness. Prolonged anaemia results in hair loss, brittle hair and nails.',
         '(i) انیمیا کا مطلب خون میں سرخ خونی خلیوں یا ہیموگلوبن کی معمول سے کم مقدار ہے۔ یہ اس وقت ہوتا ہے جب جسم کم آئرن لے یا آئرن کم جذب کرے۔ جب جسم میں آئرن کی کمی ہو تو یہ سرخ خونی خلیوں کی درکار تعداد نہیں بنا سکتا۔ انیمیا کی عام علامت مسلسل تھکاوٹ اور کمزوری ہے۔ طویل انیمیا سے بال گرتے ہیں اور بال اور ناخن بھربھرے ہو جاتے ہیں۔',
         '(i) کم خوني په وینه کې د سرو وینې حجرو یا هیموګلوبین له عادي مقدار کم مقدار ته وايي. دا هغه وخت پېښېږي چې بدن لږه اوسپنه واخلي یا اوسپنه کمه جذب کړي. کله چې په بدن کې د اوسپنې کمښت وي، د سرو وینې حجرو اړین شمېر نه شي جوړولای. د کم خونۍ عامه نښه دوامداره ستړیا او کمزوري ده. اوږده کم خوني د وېښتانو د تویېدو او د وېښتانو او نوکانو د ماتېدو لامل کېږي.'),
        ('(ii) Osteoporosis is a disease in which bones become porous and fragile. It occurs when the body does not take the required amounts of calcium or vitamin D.', '(ii) اوسٹیوپوروسس ایسی بیماری ہے جس میں ہڈیاں مسام دار اور نازک ہو جاتی ہیں۔ یہ اس وقت ہوتی ہے جب جسم کیلشیم یا وٹامن D کی درکار مقدار نہ لے۔', '(ii) اوسټیوپوروزس هغه ناروغي ده چې هډوکي پکې سوري سوري او نازک کېږي. هغه وخت پېښېږي چې بدن د کلسیم یا ویټامین D اړین مقدار وانخلي.'),
        ('(iii) Goiter is a disease in which the thyroid gland present in the neck enlarges. This gland uses iodine for making its secretions. When there is deficiency of iodine in diet, the gland enlarges. It results in a swelling in the neck.', '(iii) گلہڑ ایسی بیماری ہے جس میں گردن میں موجود تھائیرائیڈ غدود بڑھ جاتا ہے۔ یہ غدود اپنی رطوبتیں بنانے کے لیے آیوڈین استعمال کرتا ہے۔ جب غذا میں آیوڈین کی کمی ہو تو غدود بڑھ جاتا ہے۔ اس سے گردن میں سوجن ہو جاتی ہے۔', '(iii) جاغور هغه ناروغي ده چې په غاړه کې تایرایډ غده پکې لویېږي. دا غده د خپلو افرازاتو د جوړولو لپاره ایوډین کاروي. کله چې په خوراک کې د ایوډین کمښت وي، غده لویېږي. پایله یې په غاړه کې پړسوب دی.'),
    ])
    s.p('SpaceBook note: the left margin of PDF 166 is cut off in the scan. The first word "Anaemia" and the item number "(i)" are restored from the visible letters and from items (ii) and (iii).',
        'اسپیس بک نوٹ: PDF 166 کا بایاں حاشیہ اسکین میں کٹا ہوا ہے۔ پہلا لفظ ”Anaemia“ اور نمبر ”(i)“ نظر آنے والے حروف اور اشیا (ii) اور (iii) سے بحال کیے گئے ہیں۔',
        'د سپېس بوک یادونه: د PDF 166 کیڼه څنډه په سکن کې پرې شوې. لومړۍ کلمه ”Anaemia“ او شمېره ”(i)“ له ښکاره تورو او له (ii) او (iii) څخه بېرته راوستل شوې.', editorial=True)
    s.fig('bio8-fig8-7', thyroid(TH['en']), thyroid(TH['ur']), thyroid(TH['ps']), .45,
          caption=('Figure 8.7 Thyorlod', 'شکل 8.7 تھائیرائیڈ', 'شکل 8.7 تایرایډ'))
    s.p('SpaceBook note: the figure caption is printed "Thyorlod". It means Thyroid.', 'اسپیس بک نوٹ: شکل کا عنوان ”Thyorlod“ چھپا ہے۔ مراد تھائیرائیڈ ہے۔', 'د سپېس بوک یادونه: د شکل سرلیک ”Thyorlod“ چاپ شوی. مطلب یې تایرایډ دی.', editorial=True)
    s.h('C- Over Intake of Nutrients (OIN)', 'C- غذائی اجزا کا زیادہ استعمال (OIN)', 'C- د غذايي موادو زیات اخیستل (OIN)')
    s.p('The over consumption of high calorie diet leads to overweight and obesity. Obese people may suffer from hypertension, liver, renal and heart disorders. Excessive fat consumption can be fatal. Some fats get deposited on the inner walls of the arteries causing arteriosclerosis. It leads to cardio-vascular diseases and other complications like hypertension, diabetes etc.',
        'زیادہ کیلوری والی غذا کا حد سے زیادہ استعمال وزن کی زیادتی اور موٹاپے کا باعث بنتا ہے۔ موٹے لوگ ہائی بلڈ پریشر، جگر، گردوں اور دل کی خرابیوں کا شکار ہو سکتے ہیں۔ چکنائی کا حد سے زیادہ استعمال جان لیوا ہو سکتا ہے۔ کچھ چکنائی شریانوں کی اندرونی دیواروں پر جم کر آرٹیریوسکلیروسس پیدا کرتی ہے۔ اس سے دل اور خون کی نالیوں کی بیماریاں اور ہائی بلڈ پریشر، ذیابیطس وغیرہ جیسی دوسری پیچیدگیاں پیدا ہوتی ہیں۔',
        'د لوړې کالورۍ خوراک ډېر مصرف د زیات وزن او چاغښت لامل کېږي. چاغ خلک ښايي په لوړ فشار، د ځيګر، پښتورګو او زړه اختلالاتو اخته شي. د غوړو ډېر مصرف وژونکی کېدای شي. ځینې غوړ د شریانونو پر داخلي دېوالونو کېني او ارټیریوسکلیروزس رامنځته کوي. دا د زړه او رګونو ناروغیو او نورو اختلاطاتو لکه لوړ فشار، شکرې او نورو ته لار هواروي.')
    s.p('Similarly, over-intake of vitamin D causes nausea, fatigue, vomiting, renal damage etc. Over-intake of vitamin A leads to dry itchy skin, painful swelling of legs and hands, enlargement of spleen etc.',
        'اسی طرح وٹامن D کا زیادہ استعمال متلی، تھکاوٹ، الٹی، گردوں کو نقصان وغیرہ کا باعث بنتا ہے۔ وٹامن A کا زیادہ استعمال خشک خارش والی جلد، ٹانگوں اور ہاتھوں کی دردناک سوجن، تلی کے بڑھنے وغیرہ کا باعث بنتا ہے۔',
        'همدارنګه د ویټامین D زیات اخیستل زړه بدوالی، ستړیا، کانګې، پښتورګو ته زیان او نور رامنځته کوي. د ویټامین A زیات اخیستل وچ خارښتي پوستکي، د پښو او لاسونو دردناک پړسوب، د تورې لویېدو او نورو ته لار هواروي.')
    s.h('Causes of Malnutrition', 'سوئے تغذیہ کی وجوہات', 'د سوءتغذیې لاملونه')
    s.p('There are many reasons of suffering from malnutrition.', 'سوئے تغذیہ کا شکار ہونے کی بہت سی وجوہات ہیں۔', 'په سوءتغذیه د اخته کېدو ډېر لاملونه شته.')
    s.lines([
        ('a. Malnutrition may be due to a lack of knowledge of a balanced diet.', 'a. سوئے تغذیہ متوازن غذا کے بارے میں علم کی کمی کی وجہ سے ہو سکتا ہے۔', 'a. سوءتغذیه ښايي د متوازن خوراک په اړه د پوهې د نشتوالي له امله وي.'),
        ('b. Poor absorption of nutrients in the body can also be a reason for malnutrition.', 'b. جسم میں غذائی اجزا کا ناقص جذب بھی سوئے تغذیہ کی وجہ ہو سکتا ہے۔', 'b. په بدن کې د غذايي موادو کمزوری جذب هم د سوءتغذیې لامل کېدای شي.'),
        ('c. Poverty is among the most common reasons of malnutrition. Malnutrition is especially widespread in under developed countries.', 'c. غربت سوئے تغذیہ کی سب سے عام وجوہات میں سے ہے۔ سوئے تغذیہ خاص طور پر پسماندہ ممالک میں عام ہے۔', 'c. بېوزلي د سوءتغذیې تر ټولو عامو لاملونو څخه ده. سوءتغذیه په ځانګړي ډول په وروسته پاتې هېوادونو کې پراخه ده.'),
        ('d. Famine is another reason behind malnutrition. Famine means widespread lack of food to feed all the people living in the area. Famines are caused due to increasing population, drought, flooding, crop diseases, unequal food distribution due to wars, wrong economic policies etc.', 'd. قحط سوئے تغذیہ کی ایک اور وجہ ہے۔ قحط کا مطلب علاقے میں رہنے والے تمام لوگوں کو کھلانے کے لیے خوراک کی وسیع کمی ہے۔ قحط بڑھتی آبادی، خشک سالی، سیلاب، فصلوں کی بیماریوں، جنگوں کی وجہ سے خوراک کی غیر مساوی تقسیم، غلط معاشی پالیسیوں وغیرہ سے پڑتے ہیں۔', 'd. قحطي د سوءتغذیې بل لامل دی. قحطي په سیمه کې د ټولو اوسېدونکو د خوړلو لپاره د خوړو پراخ کمښت ته وايي. قحطي د مخ په زیاتېدونکي نفوس، وچکالۍ، سېلابونو، د فصلونو ناروغیو، د جګړو له امله د خوړو نابرابر وېش، ناسمو اقتصادي پالیسیو او نورو له امله رامنځته کېږي.'),
    ])
    s.callout(AI, [('Enlist different food components and write the consequences of their over / under intake.', 'خوراک کے مختلف اجزا کی فہرست بنائیں اور ان کے زیادہ / کم استعمال کے نتائج لکھیں۔', 'د خوړو بېلابېلې برخې لېست کړئ او د هغوی د زیات / کم اخیستو پایلې ولیکئ.')])
    out.append(s)
    return out
