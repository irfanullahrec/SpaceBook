# -*- coding: utf-8 -*-
"""Unit 3 part A — PDF 42-53 (printed 37-41, 44-50). Printed 42-43 are missing from every local PDF copy."""
from bio9_tools import Section, photo_figure, svg_wrap, txt

SI = ('Scientific Information', 'سائنسی معلومات', 'ساینسي معلومات')


def taxonomy_ladder(L):
    """Figure 3.1: taxonomic hierarchy of Panther, rank boxes stepping down with arrows."""
    ranks = ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species']
    fills = ['#dcedc8', '#b3e5fc', '#f48fb1', '#ec407a', '#ffffff', '#f8bbd0', '#fff9c4']
    b = []
    for i, r in enumerate(ranks):
        x = 120 + i * 22; y = 10 + i * 58; w = 150 - i * 8
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="3" fill="{fills[i]}" stroke="#607d8b"/>')
        b.append(txt(x + w / 2, y + 15, L[r], 10, 'middle', 'bold', '#263238'))
        if r != 'species':
            for k in range(max(1, 5 - i // 2)):
                b.append(f'<rect x="{x + 12 + k * 22}" y="{y + 22}" width="12" height="7" fill="#fff" stroke="#546e7a" stroke-width=".8"/>')
            b.append(f'<path d="M{x + w / 2},{y + 40} q4,10 18,14" stroke="#455a64" stroke-width="5" fill="none"/>')
        b.append(txt(x + w + 10, y + 25, L['eg_' + r], 12, 'start', 'normal', '#111', italic=(r in ('genus', 'species'))))
    # leopard silhouette
    b.append('<path d="M20,360 q20,-40 70,-38 q40,2 60,20 l8,-6 q6,8 -2,14 l-6,30 h-8 l2,-26 h-40 l-6,28 h-8 l2,-28 q-30,4 -40,10 l-6,22 h-8 l4,-26 q-20,0 -22,0 z" fill="#c8a165" stroke="#5d4037"/>')
    for x, y in [(50, 340), (70, 332), (90, 345), (110, 336), (130, 342), (60, 352), (100, 354)]:
        b.append(f'<circle cx="{x}" cy="{y}" r="3" fill="#4e342e"/>')
    return svg_wrap(''.join(b), 470, 420, L['title'])


TAX_EN = dict(title='Figure 3.1: Taxonomic hierarchy of Panther', kingdom='KINGDOM', phylum='PHYLUM', **{'class': 'CLASS'}, order='ORDER', family='FAMILY', genus='GENUS', species='SPECIES',
              eg_kingdom='Animalia', eg_phylum='Chordata', eg_class='Mammalia', eg_order='Carnivora', eg_family='Felidae', eg_genus='Panthera', eg_species='Panthera pardus')
TAX_UR = dict(TAX_EN, title='شکل 3.1', kingdom='کنگڈم (مملکت)', phylum='فائلم', **{'class': 'کلاس (جماعت)'}, order='آرڈر', family='فیملی', genus='جنس (جینس)', species='نوع (اسپیشیز)')
TAX_PS = dict(TAX_EN, title='شکل 3.1', kingdom='کنګډم', phylum='فایلم', **{'class': 'کلاس'}, order='آرډر', family='کورنۍ', genus='جینس', species='نوع')


def virus(L):
    """Figure 3.13: bacteriophage with labelled protein coat, DNA, sheath, core, cell wall."""
    b = ['<path d="M30,230 Q170,200 310,230 L310,280 L30,280 Z" fill="#f0f4c3" stroke="#827717"/>']
    b.append('<polygon points="170,20 205,40 205,85 170,105 135,85 135,40" fill="#b39ddb" stroke="#4527a0" stroke-width="2"/>')
    b.append(txt(170, 68, L['dna'], 12, 'middle', 'bold', '#fff'))
    b.append('<rect x="160" y="105" width="20" height="10" fill="#7e57c2"/>')
    b.append('<rect x="158" y="115" width="24" height="70" fill="#f06292" stroke="#ad1457"/>' + ''.join(f'<path d="M158,{120+k*9} h24" stroke="#ad1457"/>' for k in range(7)))
    b.append('<rect x="166" y="185" width="8" height="40" fill="#5e35b1"/>')
    b.append('<path d="M158,185 L95,150 L70,232 M182,185 L245,150 L270,232 M162,190 L130,230 M178,190 L210,230" stroke="#455a64" stroke-width="3" fill="none"/>')
    b.append('<path d="M205,45 L250,30" stroke="#333"/>' + txt(254, 28, L['coat1'], 11) + txt(254, 41, L['coat2'], 11))
    b.append('<path d="M158,140 L95,110" stroke="#333"/>' + txt(50, 108, L['sheath'], 11))
    b.append('<path d="M170,222 L110,255" stroke="#333"/>' + txt(70, 262, L['core'], 11))
    b.append('<path d="M240,228 L270,268" stroke="#333"/>' + txt(262, 278, L['wall'], 11))
    return svg_wrap(''.join(b), 340, 290, L['title'])


VIR_EN = dict(title='Figure 3.13: Virus', dna='DNA', coat1='Protein', coat2='coat', sheath='Sheath', core='Core', wall='Cell wall')
VIR_UR = dict(title='شکل 3.13', dna='DNA', coat1='پروٹین', coat2='کوٹ', sheath='شیتھ', core='کور', wall='خلوی دیوار')
VIR_PS = dict(title='شکل 3.13', dna='DNA', coat1='پروټیني', coat2='پوښ', sheath='شیت', core='کور', wall='د حجرې دېوال')


def grid(sid, title, items, items_ur, items_ps, note_en='Photographs in the book', cols=2):
    return (photo_figure(title, items, note_en, cols=cols),
            photo_figure(title, items_ur, 'کتاب میں تصاویر', cols=cols),
            photo_figure(title, items_ps, 'په کتاب کې انځورونه', cols=cols))


def sections():
    out = []
    s = Section('bio3_slo', 'SLOs', 'Student Learning Outcomes', 'طلبہ کے حاصلاتِ تعلم', 'د زده کوونکو د زده کړې پایلې', [42])
    s.h('After studying this unit the students will be able to:', 'اس یونٹ کا مطالعہ کرنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د دې یونټ له مطالعې وروسته به زده کوونکي وکولای شي چې:')
    s.ul([
        ('Define biodiversity.', 'حیاتیاتی تنوع کی تعریف کر سکیں۔', 'د ژوندیو تنوع تعریف کړي.'),
        ('Describe the major variety of life on the planet Earth.', 'کرۂ ارض پر زندگی کے بڑے تنوع کو بیان کر سکیں۔', 'پر ځمکه د ژوند لوی تنوع بیان کړي.'),
        ('Relate the importance of biodiversity with natural ecosystem through examples.', 'مثالوں کے ذریعے حیاتیاتی تنوع کی اہمیت کا قدرتی ماحولیاتی نظام سے تعلق بیان کر سکیں۔', 'د بېلګو له لارې د ژوندیو تنوع اهمیت له طبیعي ایکوسیسټم سره وتړي.'),
        ('Describe the basis of classification of living organisms.', 'جانداروں کی درجہ بندی کی بنیاد بیان کر سکیں۔', 'د ژوندیو موجوداتو د ډلبندۍ بنسټ بیان کړي.'),
        ('Explain the aims and principles of classification; keeping in view its historical background.', 'درجہ بندی کے مقاصد اور اصولوں کی اس کے تاریخی پس منظر کو مدِنظر رکھتے ہوئے وضاحت کر سکیں۔', 'د ډلبندۍ موخې او اصول د هغې تاریخي شالید په پام کې نیولو سره تشریح کړي.'),
        ('Identify the contributions of Aristotle as the founder of biological classification.', 'حیاتیاتی درجہ بندی کے بانی کے طور پر ارسطو کی خدمات کی شناخت کر سکیں۔', 'د بیولوژیکي ډلبندۍ د بنسټګر په توګه د ارسطو خدمتونه وپېژني.'),
        ('Explain the basis for establishing 5 kingdoms.', '5 کنگڈمز قائم کرنے کی بنیاد کی وضاحت کر سکیں۔', 'د 5 کنګډمونو د جوړولو بنسټ تشریح کړي.'),
        ('Compare two and five kingdom classification systems.', 'دو اور پانچ کنگڈم درجہ بندی کے نظاموں کا موازنہ کر سکیں۔', 'د دوه او پنځه کنګډمي ډلبندۍ سیسټمونه پرتله کړي.'),
        ('Rationalize that five kingdom system better explains diversity of living organisms.', 'دلیل دے سکیں کہ پانچ کنگڈم نظام جانداروں کے تنوع کی بہتر وضاحت کرتا ہے۔', 'دلیل ورکړي چې پنځه کنګډمي سیسټم د ژوندیو موجوداتو تنوع ښه تشریح کوي.'),
        ('Describe the contributions of Abu Usman Umer Aljahiz in describing the characteristics of animal species.', 'جانوروں کی انواع کی خصوصیات بیان کرنے میں ابو عثمان عمر الجاحظ کی خدمات بیان کر سکیں۔', 'د ژویو د نوعو د ځانګړتیاوو په بیانولو کې د ابو عثمان عمر الجاحظ خدمتونه بیان کړي.'),
        ('Describe the diagnostic characteristics of the five kingdoms.', 'پانچ کنگڈمز کی تشخیصی خصوصیات بیان کر سکیں۔', 'د پنځو کنګډمونو تشخیصي ځانګړتیاوې بیان کړي.'),
        ('Describe the acellular structure of virus and justify why viruses are excluded from the five kingdom classification system.', 'وائرس کی غیر خلوی ساخت بیان کر سکیں اور ثابت کر سکیں کہ وائرسوں کو پانچ کنگڈم درجہ بندی سے کیوں خارج رکھا گیا ہے۔', 'د ویروس غیر حجروي جوړښت بیان کړي او ثابت کړي چې ویروسونه ولې له پنځه کنګډمي ډلبندۍ ایستل شوي دي.'),
        ('Describe the aims and principles of binomial nomenclature.', 'دو اسمی نظامِ نام گذاری کے مقاصد اور اصول بیان کر سکیں۔', 'د دوه نومي نوم ایښودنې موخې او اصول بیان کړي.'),
        ('Describe using local examples, the importance of binomial nomenclature.', 'مقامی مثالوں سے دو اسمی نظامِ نام گذاری کی اہمیت بیان کر سکیں۔', 'د سیمه ییزو بېلګو په کارولو د دوه نومي نوم ایښودنې اهمیت بیان کړي.'),
        ('Define the concept of conservation.', 'تحفظ کے تصور کی تعریف کر سکیں۔', 'د ساتنې مفهوم تعریف کړي.'),
        ('Explain the impact of human beings on biodiversity.', 'حیاتیاتی تنوع پر انسانوں کے اثرات کی وضاحت کر سکیں۔', 'پر ژوندیو تنوع د انسانانو اغېز تشریح کړي.'),
        ('Identify causes of deforestation and its effects on biodiversity.', 'جنگلات کی کٹائی کی وجوہات اور حیاتیاتی تنوع پر اس کے اثرات کی شناخت کر سکیں۔', 'د ځنګلونو د وهلو لاملونه او پر ژوندیو تنوع یې اغېزې وپېژني.'),
        ('Enumerate the reasons for conservation of biodiversity.', 'حیاتیاتی تنوع کے تحفظ کی وجوہات شمار کر سکیں۔', 'د ژوندیو تنوع د ساتنې لاملونه وشمېري.'),
        ('Describe some of the issues of conservation in Pakistan (especially with regard to deforestation and hunting)', 'پاکستان میں تحفظ کے بعض مسائل (خاص طور پر جنگلات کی کٹائی اور شکار کے حوالے سے) بیان کر سکیں', 'په پاکستان کې د ساتنې ځینې ستونزې (په ځانګړي ډول د ځنګلونو وهلو او ښکار په اړه) بیان کړي'),
    ])
    out.append(s)

    s = Section('bio3_1', '3.1', 'Biodiversity', 'حیاتیاتی تنوع', 'د ژوندیو تنوع', [43, 44])
    s.p('Have you ever thought about the number and variety of living organisms in the world? Scientists believe that there are about two millions different types of organisms in the world. In Pakistan, there are about 6000 kinds of plants and 23,000 types of animals. Although these organisms share many common characters, they are different in size, shape, colour, morphology, behaviour and reproduction methods. The differences among the living organisms add to the biodiversity of an area. Each species has a specific role in an ecosystem. Loss of species makes an ecosystem less productive.',
        'کیا آپ نے کبھی دنیا میں جانداروں کی تعداد اور تنوع کے بارے میں سوچا ہے؟ سائنس دانوں کا خیال ہے کہ دنیا میں تقریباً بیس لاکھ مختلف اقسام کے جاندار ہیں۔ پاکستان میں پودوں کی تقریباً 6000 اقسام اور جانوروں کی 23,000 اقسام ہیں۔ اگرچہ ان جانداروں میں بہت سی مشترک خصوصیات ہیں، لیکن یہ جسامت، شکل، رنگ، بیرونی ساخت، رویے اور تولید کے طریقوں میں مختلف ہیں۔ جانداروں کے درمیان فرق کسی علاقے کے حیاتیاتی تنوع میں اضافہ کرتا ہے۔ ہر نوع کا ماحولیاتی نظام میں ایک مخصوص کردار ہوتا ہے۔ انواع کے خاتمے سے ماحولیاتی نظام کم پیداواری ہو جاتا ہے۔',
        'ایا تاسو کله په نړۍ کې د ژوندیو موجوداتو د شمېر او تنوع په اړه فکر کړی دی؟ ساینس پوهان باور لري چې په نړۍ کې شاوخوا دوه میلیونه بېلابېل ډولونه ژوندي موجودات شته. په پاکستان کې د بوټو شاوخوا 6000 ډولونه او د ژویو 23,000 ډولونه شته. که څه هم دا موجودات ډېرې ګډې ځانګړتیاوې لري، خو په جسامت، بڼه، رنګ، مورفولوژي، چلند او د تکثر په لارو کې توپیر لري. د ژوندیو موجوداتو ترمنځ توپیرونه د یوې سیمې د ژوندیو تنوع زیاتوي. هره نوع په ایکوسیسټم کې ځانګړی رول لري. د نوعو له منځه تلل ایکوسیسټم لږ تولیدي کوي.')
    # Unit 3 opener collage (plants/animals in a hand) is uncaptioned decoration: inspected and excluded.
    s.p('In this unit, we will study how numerous kinds of organisms are classified. We will also study the effects of human activities on the existence of organisms.',
        'اس یونٹ میں ہم مطالعہ کریں گے کہ جانداروں کی بے شمار اقسام کی درجہ بندی کیسے کی جاتی ہے۔ ہم جانداروں کی بقا پر انسانی سرگرمیوں کے اثرات کا بھی مطالعہ کریں گے۔',
        'په دې یونټ کې به موږ ولولو چې د ژوندیو موجوداتو بې شمېره ډولونه څنګه ډلبندي کېږي. موږ به د ژوندیو موجوداتو پر شتون د انساني فعالیتونو اغېزې هم ولولو.')
    s.callout(('Point to Ponder', 'غور طلب نکتہ', 'د فکر وړ ټکی'), [
        ('At least 40% of the world\'s economy and 80% of the needs of the poor are derived from biological resources. In addition, the richer the biodiversity, the greater the opportunity for medical discoveries, economic development and responses to new challenges.',
         'دنیا کی معیشت کا کم از کم 40% اور غریبوں کی ضروریات کا 80% حیاتیاتی وسائل سے حاصل ہوتا ہے۔ مزید یہ کہ حیاتیاتی تنوع جتنا زیادہ ہو، طبی دریافتوں، معاشی ترقی اور نئے چیلنجوں سے نمٹنے کے مواقع اتنے ہی زیادہ ہوتے ہیں۔',
         'د نړۍ د اقتصاد لږ تر لږه 40% او د بې وزلو د اړتیاوو 80% له بیولوژیکي سرچینو ترلاسه کېږي. سربېره پر دې، هر څومره چې د ژوندیو تنوع بډای وي، د طبي کشفونو، اقتصادي پرمختګ او نویو ننګونو ته د ځواب ورکولو فرصتونه هومره ډېر وي.')])
    s.h('3.1 Biodiversity', '3.1 حیاتیاتی تنوع', '3.1 د ژوندیو تنوع')
    s.p('The term \'biodiversity\' is derived from a Greek word, \'bio\' which means \'life\' and \'diversity\' means variety within a species and among species. So biodiversity may be defined as the variety of organisms present in different ecosystems.',
        'اصطلاح ’بائیو ڈائیورسٹی‘ یونانی لفظ سے ماخوذ ہے: ’بائیو‘ یعنی ’زندگی‘ اور ’ڈائیورسٹی‘ یعنی کسی نوع کے اندر اور انواع کے درمیان تنوع۔ چنانچہ حیاتیاتی تنوع کی تعریف یوں کی جا سکتی ہے کہ مختلف ماحولیاتی نظاموں میں موجود جانداروں کا تنوع۔',
        'د ’بایوډایورسټي‘ اصطلاح له یوناني کلمې اخیستل شوې: ’بایو‘ یعنې ’ژوند‘ او ’ډایورسټي‘ یعنې د یوې نوعې دننه او د نوعو ترمنځ تنوع. نو د ژوندیو تنوع داسې تعریف کېدای شي: په بېلابېلو ایکوسیسټمونو کې د موجودو ژوندیو موجوداتو تنوع.')
    s.p('Biodiversity is not distributed uniformly on the Earth. Biologists estimated that today\'s global biodiversity may consist of more than 100 million kinds of organisms. The biodiversity of an area depends on climate, altitude and composition of soils etc. Tropical Regions of the Earth have richer biodiversity while Polar Regions have fewer species.',
        'حیاتیاتی تنوع زمین پر یکساں طور پر تقسیم نہیں ہے۔ ماہرینِ حیاتیات کا اندازہ ہے کہ آج کا عالمی حیاتیاتی تنوع 10 کروڑ سے زیادہ اقسام کے جانداروں پر مشتمل ہو سکتا ہے۔ کسی علاقے کا حیاتیاتی تنوع آب و ہوا، بلندی اور مٹی کی ترکیب وغیرہ پر منحصر ہے۔ زمین کے استوائی علاقوں میں حیاتیاتی تنوع زیادہ ہے جبکہ قطبی علاقوں میں انواع کم ہیں۔',
        'د ژوندیو تنوع پر ځمکه یو شان نه دی وېشل شوی. بیولوژیستانو اټکل کړی چې نننی نړیوال تنوع ښايي له 100 میلیونو ډېر ډولونه ژوندي موجودات ولري. د یوې سیمې د ژوندیو تنوع په اقلیم، لوړوالي او د خاورې په ترکیب او نورو پورې اړه لري. د ځمکې استوایي سیمې بډای تنوع لري په داسې حال کې چې قطبي سیمې لږې نوعې لري.')
    s.h('Importance of Biodiversity', 'حیاتیاتی تنوع کی اہمیت', 'د ژوندیو تنوع اهمیت')
    s.p('Following aspects show the importance of biodiversity.', 'درج ذیل پہلو حیاتیاتی تنوع کی اہمیت ظاہر کرتے ہیں۔', 'لاندې اړخونه د ژوندیو تنوع اهمیت ښيي.')
    s.lines([
        ('a. Food for human beings: Biodiversity provides high variety of food for human beings. crops, livestock, forestry and fish are important source of food for human beings.',
         'a. انسانوں کے لیے خوراک: حیاتیاتی تنوع انسانوں کے لیے خوراک کا بہت زیادہ تنوع فراہم کرتا ہے۔ فصلیں، مویشی، جنگلات اور مچھلی انسانوں کے لیے خوراک کا اہم ذریعہ ہیں۔',
         'a. د انسانانو لپاره خواړه: د ژوندیو تنوع انسانانو ته د خوړو ډېر تنوع برابروي. فصلونه، څاروي، ځنګلونه او کبان د انسانانو لپاره د خوړو مهمه سرچینه ده.'),
        ('b. Production of drugs: Biodiversity plays a vital role in human and animal health. A wide variety of plants, animals and fungi are used as medicine and essential vitamins. Drugs such as Streptomycin, Neomycin and Erythromycin are derived from bacteria. Drugs like caffeine, morphine, quinine etc. are produced by other plants.',
         'b. ادویات کی تیاری: حیاتیاتی تنوع انسانی اور حیوانی صحت میں اہم کردار ادا کرتا ہے۔ پودوں، جانوروں اور فنجائی کی وسیع اقسام دوا اور ضروری وٹامنز کے طور پر استعمال ہوتی ہیں۔ اسٹریپٹومائسین، نیومائسین اور اریتھرومائسین جیسی ادویات بیکٹیریا سے حاصل ہوتی ہیں۔ کیفین، مارفین، کونین وغیرہ جیسی ادویات دوسرے پودے تیار کرتے ہیں۔',
         'b. د درملو تولید: د ژوندیو تنوع د انسان او حیوان په روغتیا کې مهم رول لري. د بوټو، ژویو او فنجای پراخ ډولونه د درملو او اړینو ویټامینونو په توګه کارول کېږي. سټرېپټومایسین، نیومایسین او اریتهرومایسین په څېر درمل له باکتریاوو اخیستل کېږي. کافین، مورفین، کونین او نور درمل نور بوټي تولیدوي.'),
        ('c. Industrial benefits of biodiversity: Biodiversity plays an important role in the production of industrial materials. Building material, fibres, dyes, resins, gums, adhesives, rubber and oil are some of the industrial materials derived from the plants.',
         'c. حیاتیاتی تنوع کے صنعتی فوائد: حیاتیاتی تنوع صنعتی مواد کی تیاری میں اہم کردار ادا کرتا ہے۔ تعمیراتی سامان، ریشے، رنگ، رال، گوند، چپکنے والے مادے، ربڑ اور تیل پودوں سے حاصل ہونے والے چند صنعتی مواد ہیں۔',
         'c. د ژوندیو تنوع صنعتي ګټې: د ژوندیو تنوع د صنعتي موادو په تولید کې مهم رول لري. د ودانۍ مواد، تارونه، رنګونه، رالونه، ګوندونه، سرېښونه، ربړ او تېل له بوټو ترلاسه کېدونکي ځینې صنعتي مواد دي.'),
        ('d. Relation with Ecosystems: Biodiversity is the essential component of ecosystems. In an ecosystem, species show interaction among each other. Each species has a specific role in the ecosystem. Loss of species makes the ecosystem less productive. Natural cycles for example water cycle, nitrogen cycle etc going on in the ecosystem. Fertility of soils, balanced climate and numerous other factors depend upon its biodiversity.',
         'd. ماحولیاتی نظاموں سے تعلق: حیاتیاتی تنوع ماحولیاتی نظاموں کا لازمی جز ہے۔ ماحولیاتی نظام میں انواع ایک دوسرے سے تعامل کرتی ہیں۔ ہر نوع کا ماحولیاتی نظام میں مخصوص کردار ہے۔ انواع کا خاتمہ ماحولیاتی نظام کو کم پیداواری بنا دیتا ہے۔ قدرتی چکر مثلاً پانی کا چکر، نائٹروجن کا چکر وغیرہ ماحولیاتی نظام میں جاری رہتے ہیں۔ مٹی کی زرخیزی، متوازن آب و ہوا اور دیگر بے شمار عوامل اس کے حیاتیاتی تنوع پر منحصر ہیں۔',
         'd. له ایکوسیسټمونو سره اړیکه: د ژوندیو تنوع د ایکوسیسټمونو اړین جز دی. په ایکوسیسټم کې نوعې یو له بل سره تعامل کوي. هره نوع په ایکوسیسټم کې ځانګړی رول لري. د نوعو له منځه تلل ایکوسیسټم لږ تولیدي کوي. طبیعي دورې لکه د اوبو دوره، د نایټروجن دوره او نورې په ایکوسیسټم کې روانې وي. د خاورې حاصلخېزي، متوازن اقلیم او ډېر نور عوامل د هغې په ژوندیو تنوع پورې اړه لري.'),
    ])
    s.callout(SI, [('There are 130,000 plants which depend on bees for pollination.', 'ایک لاکھ تیس ہزار (130,000) پودے پولینیشن کے لیے شہد کی مکھیوں پر انحصار کرتے ہیں۔', '130,000 بوټي د ګردې (پولینیشن) لپاره پر مچیو متکي دي.'),
                   ('One third of all our food, fruits and vegetable would not exist without pollinator visiting the flowers.', 'ہماری تمام خوراک، پھلوں اور سبزیوں کا ایک تہائی حصہ پھولوں پر آنے والے پولینیٹرز کے بغیر موجود نہ ہوتا۔', 'زموږ د ټولو خوړو، مېوو او سبزیو درېیمه برخه به پرته له ګلانو ته د ګرده رسوونکو له راتګ نه وه.')])
    out.append(s)

    s = Section('bio3_2', '3.2', 'Classification of Organisms', 'جانداروں کی درجہ بندی', 'د ژوندیو موجوداتو ډلبندي', [44, 45])
    s.p('Biologists have identified and described about 2 million kinds of organisms (0.5 million types of plants and 1.5 million of animals). These are only a small percentage of the total kinds estimated to live on the Earth. To study such a large collection of organisms, biologists classify them. Classification is a method by which biologists divide organisms into groups and subgroups on the basis of similarities and differences.',
        'ماہرینِ حیاتیات نے تقریباً 20 لاکھ اقسام کے جانداروں (5 لاکھ اقسام کے پودے اور 15 لاکھ جانور) کی شناخت اور وضاحت کی ہے۔ یہ زمین پر رہنے والی اندازاً کل اقسام کا صرف ایک چھوٹا سا حصہ ہیں۔ جانداروں کے اتنے بڑے مجموعے کا مطالعہ کرنے کے لیے ماہرینِ حیاتیات ان کی درجہ بندی کرتے ہیں۔ درجہ بندی ایک طریقہ ہے جس کے ذریعے ماہرینِ حیاتیات جانداروں کو مماثلتوں اور فرق کی بنیاد پر گروہوں اور ذیلی گروہوں میں تقسیم کرتے ہیں۔',
        'بیولوژیستانو شاوخوا 2 میلیونه ډولونه ژوندي موجودات (0.5 میلیونه ډوله بوټي او 1.5 میلیونه ژوي) پېژندلي او تشریح کړي دي. دا پر ځمکه د اوسېدونکو اټکل شویو ټولو ډولونو یوه کوچنۍ سلنه ده. د دومره لوی شمېر ژوندیو موجوداتو د مطالعې لپاره بیولوژیستان هغوی ډلبندي کوي. ډلبندي هغه میتود دی چې بیولوژیستان پرې ژوندي موجودات د ورته والي او توپیرونو پر بنسټ په ډلو او فرعي ډلو وېشي.')
    s.h('3.2.1 Basis of Classification', '3.2.1 درجہ بندی کی بنیاد', '3.2.1 د ډلبندۍ بنسټ')
    s.p('Aristotle classified organisms on the basis of habitat (air, water, land). However, it was not justified as animals in one group may have nothing in common except their habitat. For example, fish and turtle cannot be placed in one group.',
        'ارسطو نے جانداروں کی درجہ بندی مسکن (ہوا، پانی، خشکی) کی بنیاد پر کی۔ تاہم یہ درست نہیں تھی کیونکہ ایک گروہ کے جانوروں میں مسکن کے سوا کچھ بھی مشترک نہیں ہو سکتا۔ مثال کے طور پر، مچھلی اور کچھوے کو ایک گروہ میں نہیں رکھا جا سکتا۔',
        'ارسطو ژوندي موجودات د استوګنځای (هوا، اوبه، وچه) پر بنسټ ډلبندي کړل. خو دا سمه نه وه ځکه چې په یوه ډله کې ژوي ښايي له استوګنځای پرته بل څه ګډ ونه لري. د بېلګې په توګه، کب او کیسپ په یوه ډله کې نه شي اېښودل کېدای.')
    s.p('Later, Biologists began to classify organisms on the basis of physical characteristics. Some of the characteristics which are used to classify organisms are as follows:',
        'بعد میں ماہرینِ حیاتیات نے جسمانی خصوصیات کی بنیاد پر جانداروں کی درجہ بندی شروع کی۔ جانداروں کی درجہ بندی کے لیے استعمال ہونے والی چند خصوصیات درج ذیل ہیں:',
        'وروسته بیولوژیستانو د فزیکي ځانګړتیاوو پر بنسټ د ژوندیو موجوداتو ډلبندي پیل کړه. د ډلبندۍ لپاره کارېدونکې ځینې ځانګړتیاوې دا دي:')
    s.ul([('Prokaryotic or Eukaryotic cell', 'پروکیریوٹک یا یوکیریوٹک خلیہ', 'پروکاریوټیکه یا یوکاریوټیکه حجره'),
          ('Unicellular or Multicellular', 'یک خلوی یا کثیر خلوی', 'یو حجروي یا څو حجروي'),
          ('Autotrophs (Photosynthetic) or Heterotrophs (Non-photosynthetic)', 'آٹوٹرافس (ضیائی تالیف کرنے والے) یا ہیٹروٹرافس (ضیائی تالیف نہ کرنے والے)', 'اوټوټروفونه (فوتوسنتیټیک) یا هټروټروفونه (غیر فوتوسنتیټیک)')])
    s.p('Modern system of classification is based not only on the habitat and physical characteristics but also on genetics, anatomy, physiology and evolutionary history.',
        'درجہ بندی کا جدید نظام نہ صرف مسکن اور جسمانی خصوصیات بلکہ جینیات، اناٹومی، فزیالوجی اور ارتقائی تاریخ پر بھی مبنی ہے۔',
        'د ډلبندۍ عصري سیسټم نه یوازې پر استوګنځای او فزیکي ځانګړتیاوو بلکې پر جنیټیک، اناټومي، فزیولوژي او تکاملي تاریخ هم ولاړ دی.')
    s.h('3.2.2 Aims of Classification', '3.2.2 درجہ بندی کے مقاصد', '3.2.2 د ډلبندۍ موخې')
    s.p('As discussed earlier, classification is the arrangement of organism on the basis of certain characteristics. The aims of classifying organism into certain group are:',
        'جیسا کہ پہلے بیان ہوا، درجہ بندی بعض خصوصیات کی بنیاد پر جانداروں کی ترتیب ہے۔ جانداروں کو مخصوص گروہوں میں درجہ بند کرنے کے مقاصد یہ ہیں:',
        'لکه څنګه چې مخکې وویل شول، ډلبندي د ځینو ځانګړتیاوو پر بنسټ د ژوندیو موجوداتو ترتیب دی. په ځانګړو ډلو کې د ژوندیو موجوداتو د ډلبندۍ موخې دا دي:')
    s.ul([('To determine similarities and differences among organisms so that they can be studied easily.', 'جانداروں کے درمیان مماثلتیں اور فرق معلوم کرنا تاکہ ان کا آسانی سے مطالعہ کیا جا سکے۔', 'د ژوندیو موجوداتو ترمنځ ورته والی او توپیرونه معلومول ترڅو په اسانۍ مطالعه شي.'),
          ('To provide an idea about the sequence of evolution of organisms from simple to complex.', 'جانداروں کے سادہ سے پیچیدہ تک ارتقا کی ترتیب کے بارے میں تصور فراہم کرنا۔', 'له ساده تر پېچلو پورې د ژوندیو موجوداتو د تکامل د ترتیب په اړه مفکوره ورکول.'),
          ('To express relationships based on common features.', 'مشترک خصوصیات کی بنیاد پر تعلقات کو ظاہر کرنا۔', 'د ګډو ځانګړتیاوو پر بنسټ اړیکې څرګندول.'),
          ('To name and place the organisms in a proper group.', 'جانداروں کو نام دینا اور مناسب گروہ میں رکھنا۔', 'ژوندیو موجوداتو ته نوم ورکول او په مناسبه ډله کې یې ځای پر ځای کول.')])
    s.h('3.2.3 Principles of Classification', '3.2.3 درجہ بندی کے اصول', '3.2.3 د ډلبندۍ اصول')
    s.p('Biologists follow certain principles for classification. A few of the principles are:', 'ماہرینِ حیاتیات درجہ بندی کے لیے بعض اصولوں پر عمل کرتے ہیں۔ چند اصول یہ ہیں:', 'بیولوژیستان د ډلبندۍ لپاره ځینې اصول تعقیبوي. ځینې اصول دا دي:')
    s.ul([('Organisms are classified on the basis of apparent similarities among them.', 'جانداروں کی درجہ بندی ان کے درمیان ظاہری مماثلتوں کی بنیاد پر کی جاتی ہے۔', 'ژوندي موجودات د هغوی ترمنځ د ښکاره ورته والي پر بنسټ ډلبندي کېږي.'),
          ('Organisms are classified in one group or in closer groups if they have more homologous structures.', 'اگر جانداروں میں زیادہ ہومولوگس ساختیں ہوں تو انہیں ایک گروہ یا قریبی گروہوں میں رکھا جاتا ہے۔', 'که ژوندي موجودات ډېر همولوګ جوړښتونه ولري، په یوه ډله یا نږدې ډلو کې ډلبندي کېږي.'),
          ('The anatomical features and evolutionary history is also considered during classification.', 'درجہ بندی کے دوران اناٹومی کی خصوصیات اور ارتقائی تاریخ کو بھی مدِنظر رکھا جاتا ہے۔', 'د ډلبندۍ پر مهال اناټومیکي ځانګړتیاوې او تکاملي تاریخ هم په پام کې نیول کېږي.')])
    out.append(s)

    s = Section('bio3_3', '3.3', 'Hierarchy of Taxonomy', 'ٹیکسانومی کی درجہ بندی', 'د ټکسانومۍ کچې', [45, 46])
    s.p('Swedish naturalist Carolus Linnaeus (1707-1778) proposed a system of different ranks or levels for the classification of organisms. Such ranks are called taxa (singular “taxon”). The taxa are arranged like a ladder (from larger and more general to smaller and more specific).',
        'سویڈن کے ماہرِ فطرت کیرولس لینیئس (1707-1778) نے جانداروں کی درجہ بندی کے لیے مختلف درجوں یا سطحوں کا نظام تجویز کیا۔ ایسے درجوں کو ٹیکسا (واحد ”ٹیکسن“) کہتے ہیں۔ ٹیکسا ایک سیڑھی کی طرح (بڑے اور زیادہ عام سے چھوٹے اور زیادہ مخصوص تک) ترتیب دیے جاتے ہیں۔',
        'سویډني طبیعت پوه کارولوس لینیوس (1707-1778) د ژوندیو موجوداتو د ډلبندۍ لپاره د بېلابېلو رتبو یا کچو سیسټم وړاندې کړ. داسې رتبو ته ټکسا (مفرد ”ټکسن“) ویل کېږي. ټکسا د زینې په څېر (له لوی او عام څخه تر کوچني او ځانګړي پورې) ترتیبېږي.')
    s.p('Species is the basic and smallest unit of classification. A species contains similar organisms. A group of organisms that can naturally interbreed and produce fertile offspring is known as species. The members of a species have the same number of chromosomes. For example, all human beings have 46 chromosomes and belong to the same species.',
        'نوع درجہ بندی کی بنیادی اور سب سے چھوٹی اکائی ہے۔ ایک نوع میں ایک جیسے جاندار ہوتے ہیں۔ جانداروں کا وہ گروہ جو قدرتی طور پر آپس میں افزائشِ نسل کر کے زرخیز اولاد پیدا کر سکے، نوع کہلاتا ہے۔ ایک نوع کے ارکان میں کروموسومز کی تعداد یکساں ہوتی ہے۔ مثال کے طور پر، تمام انسانوں میں 46 کروموسومز ہوتے ہیں اور وہ ایک ہی نوع سے تعلق رکھتے ہیں۔',
        'نوع د ډلبندۍ بنسټیز او تر ټولو کوچنی واحد دی. یوه نوع ورته ژوندي موجودات لري. د ژوندیو موجوداتو هغه ډله چې په طبیعي ډول سره نسل اخیستلای او حاصلخېز اولاد تولیدولای شي، نوع بلل کېږي. د یوې نوعې غړي د کروموزومونو یو شان شمېر لري. د بېلګې په توګه، ټول انسانان 46 کروموزومونه لري او یوې نوعې پورې اړه لري.')
    s.p('Genus is the group of species that are similar in some characters. Closely related genera (plural of genus) are grouped into a family. Closely related families are grouped into one order.',
        'جنس (جینس) ان انواع کا گروہ ہے جو بعض خصوصیات میں ملتی جلتی ہوں۔ قریبی تعلق رکھنے والی جنسوں (جینس کی جمع جنیرا) کو ایک فیملی میں رکھا جاتا ہے۔ قریبی تعلق رکھنے والی فیملیز کو ایک آرڈر میں رکھا جاتا ہے۔',
        'جینس د هغو نوعو ډله ده چې په ځینو ځانګړتیاوو کې ورته وي. نږدې اړوند جنرا (د جینس جمع) په یوه کورنۍ کې ډله کېږي. نږدې اړوندې کورنۍ په یوه آرډر کې ډله کېږي.')
    s.p('Similarly, closely related orders are grouped into a class; classes in a phylum and phyla (plural of phylum) into a kingdom. A kingdom is the largest taxon of the classification system.',
        'اسی طرح قریبی تعلق رکھنے والے آرڈرز کو ایک کلاس میں؛ کلاسز کو ایک فائلم میں اور فائلا (فائلم کی جمع) کو ایک کنگڈم میں رکھا جاتا ہے۔ کنگڈم درجہ بندی کے نظام کا سب سے بڑا ٹیکسن ہے۔',
        'په همدې ډول نږدې اړوند آرډرونه په یوه کلاس کې؛ کلاسونه په یوه فایلم کې او فایلا (د فایلم جمع) په یوه کنګډم کې ډله کېږي. کنګډم د ډلبندۍ د سیسټم تر ټولو لوی ټکسن دی.')
    s.fig('bio3-fig3-1', taxonomy_ladder(TAX_EN), taxonomy_ladder(TAX_UR), taxonomy_ladder(TAX_PS), .7,
          caption=('Figure 3.1: Taxonomic hierarchy of Panther', 'شکل 3.1: پینتھر (تیندوے) کی ٹیکسانومی درجہ بندی', 'شکل 3.1: د پړانګ ټکسانومیکي کچې'))
    s.callout(('How to define species?', 'نوع کی تعریف کیسے کی جائے؟', 'نوع څنګه تعریف کړو؟'), [
        ('• In the definition of species we must emphasize on their existence “in nature” because two organisms related to different but closely related species can cross-breed under artificial conditions. In such unnatural crosses they usually produce infertile offspring. For example, a cross between a male donkey and a female horse produces an infertile mule.',
         '• نوع کی تعریف میں ہمیں ان کے ”فطرت میں“ وجود پر زور دینا چاہیے کیونکہ مختلف مگر قریبی انواع سے تعلق رکھنے والے دو جاندار مصنوعی حالات میں آپس میں ملاپ کر سکتے ہیں۔ ایسے غیر فطری ملاپ میں وہ عموماً بانجھ اولاد پیدا کرتے ہیں۔ مثال کے طور پر، نر گدھے اور مادہ گھوڑی کے ملاپ سے بانجھ خچر پیدا ہوتا ہے۔',
         '• د نوع په تعریف کې باید د هغوی ”په طبیعت کې“ شتون ټینګار وکړو ځکه چې د بېلابېلو خو نږدې نوعو دوه موجودات په مصنوعي شرایطو کې سره نسل اخیستلای شي. په داسې غیر طبیعي یوځای کېدو کې معمولاً شنډ اولاد تولیدوي. د بېلګې په توګه، د نر خره او ښځینه اسې له یوځای کېدو شنډه قاطره پیدا کېږي.'),
        ('• Moreover, this definition can be useful for classifying sexually reproducing organisms only. However, many organisms e.g. bacteria, many other unicellular organisms and fungi reproduce only asexually. These organisms do not interbreed. So, it is difficult to differentiate between two species of these organisms.',
         '• مزید یہ کہ یہ تعریف صرف جنسی تولید کرنے والے جانداروں کی درجہ بندی کے لیے مفید ہو سکتی ہے۔ تاہم بہت سے جاندار مثلاً بیکٹیریا، بہت سے دوسرے یک خلوی جاندار اور فنجائی صرف غیر جنسی تولید کرتے ہیں۔ یہ جاندار آپس میں افزائشِ نسل نہیں کرتے۔ اس لیے ان جانداروں کی دو انواع میں فرق کرنا مشکل ہے۔',
         '• سربېره پر دې، دا تعریف یوازې د جنسي تکثر کوونکو موجوداتو د ډلبندۍ لپاره ګټور کېدای شي. خو ډېر موجودات لکه باکتریا، ډېر نور یو حجروي موجودات او فنجای یوازې غیر جنسي تکثر کوي. دا موجودات سره نسل نه اخلي. نو د دې موجوداتو د دوو نوعو ترمنځ توپیر ستونزمن دی.'),
        ('• Biologists generally agree on the fact that species are groups of organisms with similar characteristics. They can be distinguished from other species and do not normally interbreed with other species in nature.',
         '• ماہرینِ حیاتیات عموماً اس حقیقت پر متفق ہیں کہ انواع ملتی جلتی خصوصیات والے جانداروں کے گروہ ہیں۔ انہیں دوسری انواع سے الگ پہچانا جا سکتا ہے اور وہ فطرت میں عموماً دوسری انواع سے افزائشِ نسل نہیں کرتے۔',
         '• بیولوژیستان عموماً پر دې حقیقت متفق دي چې نوعې د ورته ځانګړتیاوو لرونکو موجوداتو ډلې دي. دوی له نورو نوعو جلا پېژندل کېدای شي او په طبیعت کې معمولاً له نورو نوعو سره نسل نه اخلي.')])
    s.p('[Source gap] Printed pages 42 and 43 are missing from the scanned textbook (PDF page 46 is printed page 41 and PDF page 47 is printed page 44). Their text, and the figures numbered between 3.1 and 3.6, are not reproduced here. The lesson resumes with the 1988 modification by Margulis and Schwartz.',
        '[ماخذ میں خلا] چھپے ہوئے صفحات 42 اور 43 اسکین شدہ نصابی کتاب میں موجود نہیں (PDF صفحہ 46 چھپا ہوا صفحہ 41 اور PDF صفحہ 47 چھپا ہوا صفحہ 44 ہے)۔ ان کا متن اور شکل 3.1 اور 3.6 کے درمیان والی اشکال یہاں شامل نہیں۔ سبق مارگولس اور شوارٹز کی 1988ء کی ترمیم سے دوبارہ شروع ہوتا ہے۔',
        '[په سرچینه کې تشه] چاپ شوې پاڼې 42 او 43 په سکن شوي درسي کتاب کې نشته (PDF پاڼه 46 چاپ شوې پاڼه 41 او PDF پاڼه 47 چاپ شوې پاڼه 44 ده). د هغو متن او د 3.1 او 3.6 ترمنځ شکلونه دلته نه دي راوړل شوي. لوست د مارګولیس او شوارټز د 1988 تعدیل څخه بیا پیلېږي.',
        editorial=True, sourceGap=dict(printedPages=[42, 43], betweenPdfPages=[46, 47]))
    out.append(s)

    s = Section('bio3_4', '3.4', 'Five-Kingdom System of Classification', 'پانچ کنگڈم نظامِ درجہ بندی', 'پنځه کنګډمي ډلبندي سیسټم', [47, 48, 49, 50, 51, 52, 53])
    s.p('In 1988, two scientists Margulis and Schwartz further modified the Whittaker system on the basis of cellular structure, mode of nutrition and method of reproduction. According to their scheme, Kingdom Monera was given the name Kingdom Prokaryotae. They also expanded the kingdom Protista by including all unicellular and simple eukaryotic organisms and some non-true fungi in it.',
        '1988ء میں دو سائنس دانوں مارگولس اور شوارٹز نے خلوی ساخت، غذا حاصل کرنے کے طریقے اور تولید کے طریقے کی بنیاد پر وٹیکر کے نظام میں مزید ترمیم کی۔ ان کی اسکیم کے مطابق کنگڈم مونیرا کو کنگڈم پروکیریوٹی کا نام دیا گیا۔ انہوں نے تمام یک خلوی اور سادہ یوکیریوٹک جانداروں اور بعض غیر حقیقی فنجائی کو شامل کر کے کنگڈم پروٹسٹا کو بھی وسعت دی۔',
        'په 1988 کال کې دوو ساینس پوهانو مارګولیس او شوارټز د حجروي جوړښت، د تغذیې د طریقې او د تکثر د طریقې پر بنسټ د وټیکر سیسټم نور تعدیل کړ. د دوی د طرحې له مخې کنګډم مونېرا ته د کنګډم پروکاریوټي نوم ورکړل شو. دوی د ټولو یو حجروي او ساده یوکاریوټیکو موجوداتو او ځینو غیر رښتینو فنجای په شاملولو کنګډم پروټیسټا هم پراخ کړ.')
    s.fig('bio3-fig3-6', *grid('m', 'Figure 3.6 Lynn Margulis', [('', 'Lynn Margulis (portrait photograph)')], [('', 'لِن مارگولس (تصویر)')], [('', 'لین مارګولیس (انځور)')], cols=1), .3,
          caption=('Figure 3.6 Lynn Margulis', 'شکل 3.6 لِن مارگولس', 'شکل 3.6 لین مارګولیس'))
    s.p('Five-Kingdom System of Classification includes the following Kingdoms', 'پانچ کنگڈم نظامِ درجہ بندی میں درج ذیل کنگڈمز شامل ہیں', 'پنځه کنګډمي ډلبندي سیسټم لاندې کنګډمونه لري')
    s.h('i) Kingdom Monera', 'i) کنگڈم مونیرا', 'i) کنګډم مونېرا')
    s.p('This kingdom includes prokaryotic organisms (also known as prokaryotes). They are unicellular or colonial. These organisms lack membrane-bounded organelles (nucleus, mitochondria, plastids, endoplasmic reticulum, lysosomes, vacuoles etc.) Their cell wall does not contain cellulose. It is made up of murein (a molecule of polysaccharides and amino acids). They are heterotrophic but some produce their food by photosynthesis or chemosynthesis. Examples are bacteria and blue green algae (Cyanobacteria).',
        'اس کنگڈم میں پروکیریوٹک جاندار (جنہیں پروکیریوٹس بھی کہتے ہیں) شامل ہیں۔ یہ یک خلوی یا کالونیل ہوتے ہیں۔ ان جانداروں میں جھلی دار عضیات (مرکزہ، مائٹوکونڈریا، پلاسٹڈز، اینڈوپلازمک ریٹیکولم، لائسوسومز، ویکیولز وغیرہ) نہیں ہوتے۔ ان کی خلوی دیوار میں سیلولوز نہیں ہوتا۔ یہ میورین (پولی سیکرائیڈز اور امائنو ایسڈز کا ایک مالیکیول) سے بنی ہوتی ہے۔ یہ ہیٹروٹرافک ہیں لیکن بعض ضیائی تالیف یا کیمو سنتھیسز سے اپنی خوراک تیار کرتے ہیں۔ مثالیں بیکٹیریا اور نیلی سبز الجی (سائنو بیکٹیریا) ہیں۔',
        'په دې کنګډم کې پروکاریوټیک موجودات (چې پروکاریوټونه هم بلل کېږي) شامل دي. دوی یو حجروي یا کلونیایي وي. دا موجودات غشا لرونکي اورګانیلونه (هسته، مایټوکونډریا، پلاسټیډونه، انډوپلازمیک ریټیکولم، لایزوزومونه، واکیولونه او نور) نه لري. د دوی د حجرې دېوال سلولوز نه لري. دا له میورین (د پولي سکرایډونو او امینو اسیدونو یو مالیکول) جوړ دی. دوی هټروټروفیک دي خو ځینې یې خپل خواړه د فوتوسنتز یا کیموسنتز له لارې جوړوي. بېلګې یې باکتریا او شین شنه الجي (سیانوباکتریا) دي.')
    s.fig('bio3-fig3-7', *grid('7', 'Figure 3.7', [('a', 'Bacterial cells'), ('b', 'Bacterial cells'), ('c', 'Colony of Nostoc'), ('d', 'Filament of Nostoc')],
                                [('a', 'بیکٹیریائی خلیات'), ('b', 'بیکٹیریائی خلیات'), ('c', 'نوسٹاک کی کالونی'), ('d', 'نوسٹاک کا فلامنٹ')],
                                [('a', 'باکتریایي حجرې'), ('b', 'باکتریایي حجرې'), ('c', 'د نوسټاک کلوني'), ('d', 'د نوسټاک تار')]), .6,
          caption=('Figure 3.7: showing examples of kingdom Monera; (a & b) Bacterial cells, c) colony of Nostoc, d) filament of Nostoc',
                   'شکل 3.7: کنگڈم مونیرا کی مثالیں؛ (a اور b) بیکٹیریائی خلیات، c) نوسٹاک کی کالونی، d) نوسٹاک کا فلامنٹ',
                   'شکل 3.7: د کنګډم مونېرا بېلګې؛ (a او b) باکتریایي حجرې، c) د نوسټاک کلوني، d) د نوسټاک تار'))
    s.h('ii) Kingdom Protista', 'ii) کنگڈم پروٹسٹا', 'ii) کنګډم پروټیسټا')
    s.p('This kingdom includes the eukaryotes which are unicellular or unicellular-colonial and do not form tissues. Some protists contain chlorophyll and make their own food while others lack chlorophyll and cannot prepare their own food. Examples of protists are Plasmodium, Euglena, Paramecium, Chlamydomonas etc.',
        'اس کنگڈم میں وہ یوکیریوٹس شامل ہیں جو یک خلوی یا یک خلوی کالونیل ہیں اور بافتیں نہیں بناتے۔ بعض پروٹسٹس میں کلوروفل ہوتا ہے اور وہ اپنی خوراک خود بناتے ہیں جبکہ دوسروں میں کلوروفل نہیں ہوتا اور وہ اپنی خوراک تیار نہیں کر سکتے۔ پروٹسٹس کی مثالیں پلازموڈیم، یوگلینا، پیرامیشیم، کلیمائیڈوموناس وغیرہ ہیں۔',
        'په دې کنګډم کې هغه یوکاریوټونه شامل دي چې یو حجروي یا یو حجروي کلونیایي وي او نسجونه نه جوړوي. ځینې پروټیسټونه کلوروفیل لري او خپل خواړه جوړوي په داسې حال کې چې نور کلوروفیل نه لري او خپل خواړه نه شي جوړولای. د پروټیسټونو بېلګې پلازموډیم، یوګلینا، پارامیشیم، کلامیډوموناس او نور دي.')
    s.fig('bio3-fig3-8', *grid('8', 'Figure 3.8', [('a', 'Diatom'), ('b', 'Amoeba'), ('c', 'Dinoflagellate'), ('d', 'Slime mold'), ('e', 'Euglena'), ('f', 'Spirogyra'), ('g', 'Chlamydomonas'), ('h', 'Paramecium')],
                                [('a', 'ڈائٹم'), ('b', 'امیبا'), ('c', 'ڈائنو فلیجیلیٹ'), ('d', 'سلائم مولڈ'), ('e', 'یوگلینا'), ('f', 'اسپائروگائرا'), ('g', 'کلیمائیڈوموناس'), ('h', 'پیرامیشیم')],
                                [('a', 'ډایټم'), ('b', 'امیبا'), ('c', 'ډاینوفلاجیلېټ'), ('d', 'سلایم مولډ'), ('e', 'یوګلینا'), ('f', 'سپایروګایرا'), ('g', 'کلامیډوموناس'), ('h', 'پارامیشیم')], cols=4), .85,
          caption=('Figure 3.8: Few examples of Kingdom Protista; a. Diatom, b. Amoeba, c. Dinoflagellate, d. Slime mold, e. Euglena, f. Spirogyra, g. Chlamydomonas, h. Paramecium',
                   'شکل 3.8: کنگڈم پروٹسٹا کی چند مثالیں؛ a. ڈائٹم، b. امیبا، c. ڈائنو فلیجیلیٹ، d. سلائم مولڈ، e. یوگلینا، f. اسپائروگائرا، g. کلیمائیڈوموناس، h. پیرامیشیم',
                   'شکل 3.8: د کنګډم پروټیسټا ځینې بېلګې؛ a. ډایټم، b. امیبا، c. ډاینوفلاجیلېټ، d. سلایم مولډ، e. یوګلینا، f. سپایروګایرا، g. کلامیډوموناس، h. پارامیشیم'))
    s.callout(SI, [('Prokaryotes (pro means before and karyo refers to nucleus) are single called organisms that do not have a nucleus or any other membrane bound organelles inside them.',
                    'پروکیریوٹس (پرو کا مطلب پہلے اور کیریو سے مراد مرکزہ) یک خلوی جاندار ہیں جن کے اندر مرکزہ یا کوئی دوسرا جھلی دار عضیہ نہیں ہوتا۔',
                    'پروکاریوټونه (پرو یعنې مخکې او کاریو هستې ته اشاره کوي) یو حجروي موجودات دي چې دننه یې هسته یا بل غشا لرونکی اورګانیل نه وي.'),
                   ('Eukaryotes (Eu means true and karyo refers to nucleus) are organisms, whose cells have a well defined membrane bound nucleus and organelles.',
                    'یوکیریوٹس (یو کا مطلب حقیقی اور کیریو سے مراد مرکزہ) وہ جاندار ہیں جن کے خلیوں میں واضح جھلی دار مرکزہ اور عضیات ہوتے ہیں۔',
                    'یوکاریوټونه (یو یعنې رښتینی او کاریو هستې ته اشاره کوي) هغه موجودات دي چې حجرې یې ښه ټاکلې غشا لرونکې هسته او اورګانیلونه لري.')])
    s.h('iii) Kingdom Fungi', 'iii) کنگڈم فنجائی', 'iii) کنګډم فنجای')
    s.p('They are unicellular or multicellular eukaryotes. They lack chlorophyll and are hetrotrophic. They live as saprophytes (deriving food from the dead organic matter) or parasites (deriving food from the living cells of the host). Fungi get nutrients in a unique way i.e. by absorption. Their cell wall is made of chitin. Examples are yeast, Penicillium, bread mold, mushrooms, rust and smut etc.',
        'یہ یک خلوی یا کثیر خلوی یوکیریوٹس ہیں۔ ان میں کلوروفل نہیں ہوتا اور یہ ہیٹروٹرافک ہیں۔ یہ سیپروفائٹس (مردہ نامیاتی مادے سے خوراک حاصل کرنے والے) یا طفیلیوں (میزبان کے زندہ خلیات سے خوراک حاصل کرنے والے) کے طور پر رہتے ہیں۔ فنجائی ایک منفرد طریقے یعنی جذب کے ذریعے غذائی اجزا حاصل کرتے ہیں۔ ان کی خلوی دیوار کائٹن سے بنی ہوتی ہے۔ مثالیں خمیر، پینسیلیم، بریڈ مولڈ، کھمبیاں، رسٹ اور اسمٹ وغیرہ ہیں۔',
        'دوی یو حجروي یا څو حجروي یوکاریوټونه دي. کلوروفیل نه لري او هټروټروفیک دي. دوی د ساپروفایټ (له مړه عضوي مادې خواړه اخلي) یا پرازیت (د کوربه له ژوندیو حجرو خواړه اخلي) په توګه ژوند کوي. فنجای په یوه ځانګړې لاره یعنې د جذب له لارې غذايي مواد ترلاسه کوي. د دوی د حجرې دېوال له کایټین جوړ دی. بېلګې یې خمیره، پنسیلیم، د ډوډۍ پوپنه، مرخېړي، رسټ او سمټ او نور دي.')
    s.fig('bio3-fig3-9', *grid('9', 'Figure 3.9', [('a', 'Rhizopus (bread mold)'), ('b', 'Morchella'), ('c', 'Mushroom'), ('d', 'Amanita'), ('e', 'Rust spores'), ('f', 'Smut spores')],
                                [('a', 'رائزوپس (بریڈ مولڈ)'), ('b', 'مورکیلا'), ('c', 'کھمبی'), ('d', 'امانیٹا'), ('e', 'رسٹ کے بیضے'), ('f', 'اسمٹ کے بیضے')],
                                [('a', 'رایزوپس (د ډوډۍ پوپنه)'), ('b', 'مورچیلا'), ('c', 'مرخېړی'), ('d', 'امانیټا'), ('e', 'د رسټ سپورونه'), ('f', 'د سمټ سپورونه')], cols=3), .75,
          caption=('Figure 3.9: Examples of fungi; a) Rhizopus (bread mold), b) Morchella, c) Mushroom, d) Amanita, e) Rust spores, f) Smut spores',
                   'شکل 3.9: فنجائی کی مثالیں؛ a) رائزوپس (بریڈ مولڈ)، b) مورکیلا، c) کھمبی، d) امانیٹا، e) رسٹ کے بیضے، f) اسمٹ کے بیضے',
                   'شکل 3.9: د فنجای بېلګې؛ a) رایزوپس (د ډوډۍ پوپنه)، b) مورچیلا، c) مرخېړی، d) امانیټا، e) د رسټ سپورونه، f) د سمټ سپورونه'))
    s.h('iv) Kingdom Plantae', 'iv) کنگڈم پلانٹی', 'iv) کنګډم پلانټي')
    s.p('This kingdom includes plants. They are multicellular eukaryotic organisms which contain chlorophyll and prepare their own food. They have cell wall made up of cellulose. Common examples are mosses, ferns, conifers and flowering plants (rose, wheat, sugarcane etc.)',
        'اس کنگڈم میں پودے شامل ہیں۔ یہ کثیر خلوی یوکیریوٹک جاندار ہیں جن میں کلوروفل ہوتا ہے اور یہ اپنی خوراک خود تیار کرتے ہیں۔ ان کی خلوی دیوار سیلولوز سے بنی ہوتی ہے۔ عام مثالیں مازز، فرنز، کونیفرز اور پھول دار پودے (گلاب، گندم، گنا وغیرہ) ہیں۔',
        'په دې کنګډم کې بوټي شامل دي. دوی څو حجروي یوکاریوټیک موجودات دي چې کلوروفیل لري او خپل خواړه جوړوي. د حجرې دېوال یې له سلولوز جوړ دی. عامې بېلګې یې ماسونه، فرنونه، مخروطي ونې او ګل لرونکي بوټي (ګلاب، غنم، ګنې او نور) دي.')
    s.fig('bio3-fig3-10', *grid('10', 'Figure 3.10', [('a', 'Mosses'), ('b', 'Ferns'), ('c', 'Cycas'), ('d', 'Pinus'), ('e', 'Maize'), ('f', 'Brassica')],
                                 [('a', 'مازز'), ('b', 'فرنز'), ('c', 'سائیکس'), ('d', 'پائنس'), ('e', 'مکئی'), ('f', 'براسیکا')],
                                 [('a', 'ماسونه'), ('b', 'فرنونه'), ('c', 'سایکس'), ('d', 'پاینس'), ('e', 'جوار'), ('f', 'براسیکا')]), .7,
          caption=('Figure 3.10: Examples of plants; a) Mosses, b) Ferns, c) Cycas, d) Pinus, e) Maize, f) Brassica',
                   'شکل 3.10: پودوں کی مثالیں؛ a) مازز، b) فرنز، c) سائیکس، d) پائنس، e) مکئی، f) براسیکا',
                   'شکل 3.10: د بوټو بېلګې؛ a) ماسونه، b) فرنونه، c) سایکس، d) پاینس، e) جوار، f) براسیکا'))
    s.h('v) Kingdom Animalia', 'v) کنگڈم اینیمیلیا', 'v) کنګډم انیمالیا')
    s.p('Kingdom Animalia include multicellular eukaryotic organisms which lack cell wall and chlorophyll. They cannot prepare their own food and are heterotrophs. Animals ingest food and digest it within their bodies. Animals are classified into two groups on the basis of presence or absence of a vertebral column (back bone): invertebrates (earthworm, starfish, insects etc.) and vertebrates (fish, amphibians, reptiles, birds and mammals).',
        'کنگڈم اینیمیلیا میں کثیر خلوی یوکیریوٹک جاندار شامل ہیں جن میں خلوی دیوار اور کلوروفل نہیں ہوتا۔ یہ اپنی خوراک تیار نہیں کر سکتے اور ہیٹروٹرافس ہیں۔ جانور خوراک نگلتے اور اسے اپنے جسم کے اندر ہضم کرتے ہیں۔ جانوروں کو ریڑھ کی ہڈی (بیک بون) کی موجودگی یا عدم موجودگی کی بنیاد پر دو گروہوں میں تقسیم کیا جاتا ہے: غیر فقاریے (کیچوا، اسٹار فش، حشرات وغیرہ) اور فقاریے (مچھلیاں، جل تھلیے، رینگنے والے جانور، پرندے اور ممالیہ)۔',
        'کنګډم انیمالیا څو حجروي یوکاریوټیک موجودات لري چې د حجرې دېوال او کلوروفیل نه لري. دوی خپل خواړه نه شي جوړولای او هټروټروف دي. ژوي خواړه تېروي او په خپل بدن کې یې هضموي. ژوي د ملا د تیر (فقرې) د شتون یا نه شتون پر بنسټ په دوو ډلو وېشل کېږي: غیر فقاریه (چینجی، سټارفش، حشرات او نور) او فقاریه (کبان، دوه ژوندي، خزنده، مرغان او تي لرونکي).')
    s.fig('bio3-fig3-11', *grid('11', 'Figure 3.11', [('a', 'Sponges'), ('b', 'Flatworm'), ('c', 'Roundworm'), ('d', 'Starfish'), ('e', 'Snail'), ('f', 'Insect')],
                                 [('a', 'اسفنج'), ('b', 'فلیٹ ورم'), ('c', 'راؤنڈ ورم'), ('d', 'اسٹار فش'), ('e', 'گھونگا'), ('f', 'حشرہ')],
                                 [('a', 'سپنجونه'), ('b', 'پلن چینجی'), ('c', 'ګرد چینجی'), ('d', 'سټارفش'), ('e', 'حلزون'), ('f', 'حشره')], cols=3), .75,
          caption=('Figure 3.11: Examples of invertebrate animals; a) sponges, b) flatworm, c) roundworm, d) starfish, e) snail, f) insect',
                   'شکل 3.11: غیر فقاری جانوروں کی مثالیں؛ a) اسفنج، b) فلیٹ ورم، c) راؤنڈ ورم، d) اسٹار فش، e) گھونگا، f) حشرہ',
                   'شکل 3.11: د غیر فقاریه ژویو بېلګې؛ a) سپنجونه، b) پلن چینجی، c) ګرد چینجی، d) سټارفش، e) حلزون، f) حشره'))
    s.fig('bio3-fig3-12', *grid('12', 'Figure 3.12', [('a', 'Fish'), ('b', 'Frog'), ('c', 'Crocodile'), ('d', 'Birds'), ('e', 'Bat'), ('f', 'Cat')],
                                 [('a', 'مچھلی'), ('b', 'مینڈک'), ('c', 'مگرمچھ'), ('d', 'پرندے'), ('e', 'چمگادڑ'), ('f', 'بلی')],
                                 [('a', 'کب'), ('b', 'چنګښه'), ('c', 'تمساح'), ('d', 'مرغان'), ('e', 'شاپرک'), ('f', 'پیشو')], cols=3), .75,
          caption=('Figure 3.12: Examples of vertebrate animals; a) fish, b) frog, c) crocodile, d) birds, e) bat, f) cat',
                   'شکل 3.12: فقاری جانوروں کی مثالیں؛ a) مچھلی، b) مینڈک، c) مگرمچھ، d) پرندے، e) چمگادڑ، f) بلی',
                   'شکل 3.12: د فقاریه ژویو بېلګې؛ a) کب، b) چنګښه، c) تمساح، d) مرغان، e) شاپرک، f) پیشو'))
    s.h('Comparison between Two Kingdom and Five Kingdom systems of classification', 'دو کنگڈم اور پانچ کنگڈم نظامِ درجہ بندی کا موازنہ', 'د دوه کنګډمي او پنځه کنګډمي ډلبندۍ سیسټمونو پرتله')
    s.table('bio3-tab3-2', ['', 'Two Kingdom system', 'Five Kingdom system'],
            [['1.', 'It was proposed by Carolus Linnaeus in 1751.', 'It was proposed by Robert Whittakar in 1969.'],
             ['2.', 'Organisms are classified into 2 kingdoms', 'Organisms are classified into 5 kingdoms'],
             ['3.', 'It is based on nutrition and motility', 'It is based on the cell structure, complexity of body, mode of nutrition and evolution'],
             ['4.', 'The placement of organisms like Euglena, bacteria, fungi in plantae is questionable due to certain reasons', 'Organisms are better placed on the basis of body, cell structure and evolution']],
            ['', 'دو کنگڈم نظام', 'پانچ کنگڈم نظام'],
            [['1.', 'اسے کیرولس لینیئس نے 1751ء میں تجویز کیا۔', 'اسے رابرٹ وٹیکر نے 1969ء میں تجویز کیا۔'],
             ['2.', 'جانداروں کو 2 کنگڈمز میں درجہ بند کیا جاتا ہے', 'جانداروں کو 5 کنگڈمز میں درجہ بند کیا جاتا ہے'],
             ['3.', 'یہ غذا اور حرکت پر مبنی ہے', 'یہ خلوی ساخت، جسم کی پیچیدگی، غذا کے طریقے اور ارتقا پر مبنی ہے'],
             ['4.', 'یوگلینا، بیکٹیریا، فنجائی جیسے جانداروں کو پلانٹی میں رکھنا بعض وجوہات سے قابلِ اعتراض ہے', 'جانداروں کو جسم، خلوی ساخت اور ارتقا کی بنیاد پر بہتر جگہ دی گئی ہے']],
            ['', 'دوه کنګډمي سیسټم', 'پنځه کنګډمي سیسټم'],
            [['1.', 'دا کارولوس لینیوس په 1751 کې وړاندې کړ.', 'دا رابرټ وټیکر په 1969 کې وړاندې کړ.'],
             ['2.', 'موجودات په 2 کنګډمونو ډلبندي کېږي', 'موجودات په 5 کنګډمونو ډلبندي کېږي'],
             ['3.', 'دا پر تغذیه او حرکت ولاړ دی', 'دا پر حجروي جوړښت، د بدن پېچلتیا، د تغذیې طریقه او تکامل ولاړ دی'],
             ['4.', 'په پلانټي کې د یوګلینا، باکتریا، فنجای په څېر موجوداتو ځای پر ځای کول د ځینو لاملونو له امله د پوښتنې وړ دی', 'موجودات د بدن، حجروي جوړښت او تکامل پر بنسټ ښه ځای پر ځای شوي دي']],
            ratio=1, caption=('Table 3.2: Comparison between Two kingdom and Five kingdom Systems of classification', 'جدول 3.2: دو کنگڈم اور پانچ کنگڈم نظامِ درجہ بندی کا موازنہ', 'جدول 3.2: د دوه کنګډمي او پنځه کنګډمي ډلبندۍ سیسټمونو پرتله'))
    s.table('bio3-tab3-3', ['Kingdom', 'Cell Type', 'Nuclear Envelope', 'Cell Wall', 'Mode of Nutrition'],
            [['Monera', 'Prokaryotic Unicellular or colonial', 'Absent', 'Polysaccharide and amino acids', 'Autotrophic or heterotrophic'],
             ['Protista', 'Eukaryotic Unicellular, colonial or simple multicellular', 'Present', 'Present in some forms, various types', 'Photosynthetic or heterotrophic or combination of these'],
             ['Fungi', 'Eukaryotic Unicellular or multicellular', 'Present', 'Chitin', 'Heterotrophic'],
             ['Plantae', 'Eukaryotic Multicellular', 'Present', 'Cellulose and other polysaccharides', 'Photosynthetic and autotroph'],
             ['Animalia', 'Eukaryotic Multicellular', 'Present', 'Absent', 'Heterotroph']],
            ['کنگڈم', 'خلیے کی قسم', 'مرکزی جھلی', 'خلوی دیوار', 'غذا کا طریقہ'],
            [['مونیرا', 'پروکیریوٹک، یک خلوی یا کالونیل', 'غیر موجود', 'پولی سیکرائیڈ اور امائنو ایسڈز', 'آٹوٹرافک یا ہیٹروٹرافک'],
             ['پروٹسٹا', 'یوکیریوٹک، یک خلوی، کالونیل یا سادہ کثیر خلوی', 'موجود', 'بعض اقسام میں موجود، مختلف اقسام', 'ضیائی تالیفی یا ہیٹروٹرافک یا دونوں کا امتزاج'],
             ['فنجائی', 'یوکیریوٹک، یک خلوی یا کثیر خلوی', 'موجود', 'کائٹن', 'ہیٹروٹرافک'],
             ['پلانٹی', 'یوکیریوٹک، کثیر خلوی', 'موجود', 'سیلولوز اور دیگر پولی سیکرائیڈز', 'ضیائی تالیفی اور آٹوٹراف'],
             ['اینیمیلیا', 'یوکیریوٹک، کثیر خلوی', 'موجود', 'غیر موجود', 'ہیٹروٹراف']],
            ['کنګډم', 'د حجرې ډول', 'هستوي پوښ', 'د حجرې دېوال', 'د تغذیې طریقه'],
            [['مونېرا', 'پروکاریوټیک، یو حجروي یا کلونیایي', 'نشته', 'پولي سکرایډ او امینو اسیدونه', 'اوټوټروفیک یا هټروټروفیک'],
             ['پروټیسټا', 'یوکاریوټیک، یو حجروي، کلونیایي یا ساده څو حجروي', 'شته', 'په ځینو ډولونو کې شته، بېلابېل ډولونه', 'فوتوسنتیټیک یا هټروټروفیک یا د دواړو ګډون'],
             ['فنجای', 'یوکاریوټیک، یو حجروي یا څو حجروي', 'شته', 'کایټین', 'هټروټروفیک'],
             ['پلانټي', 'یوکاریوټیک، څو حجروي', 'شته', 'سلولوز او نور پولي سکرایډونه', 'فوتوسنتیټیک او اوټوټروف'],
             ['انیمالیا', 'یوکاریوټیک، څو حجروي', 'شته', 'نشته', 'هټروټروف']],
            ratio=1, caption=('Table 3.3: Distinguishing characteristics of the five kingdoms of living organisms', 'جدول 3.3: جانداروں کی پانچ کنگڈمز کی امتیازی خصوصیات', 'جدول 3.3: د ژوندیو موجوداتو د پنځو کنګډمونو توپیري ځانګړتیاوې'))
    s.callout(('Analysing and Interpreting:', 'تجزیہ اور توضیح:', 'شننه او تفسیر:'),
              [('Examine some living or preserved plants and animals and classify these animals and plants into their respective kingdoms.',
                'کچھ زندہ یا محفوظ شدہ پودوں اور جانوروں کا معائنہ کریں اور انہیں ان کی متعلقہ کنگڈمز میں درجہ بند کریں۔',
                'ځینې ژوندي یا ساتل شوي بوټي او ژوي وڅېړئ او هغوی په خپلو اړوندو کنګډمونو کې ډلبندي کړئ.')])
    out.append(s)

    s = Section('bio3_5', '3.5', 'Viruses: Unique Particles', 'وائرس: منفرد ذرات', 'ویروسونه: ځانګړې ذرې', [53])
    s.callout(SI, [('Prions and Viroids are also acellular particles like virus. Prions are made of protein only while viroids are made of circular RNA only. Both cause diseases in plants.',
                    'پرائیونز اور وائرائیڈز بھی وائرس کی طرح غیر خلوی ذرات ہیں۔ پرائیونز صرف پروٹین سے بنے ہوتے ہیں جبکہ وائرائیڈز صرف دائرہ نما آر این اے سے۔ دونوں پودوں میں بیماریاں پیدا کرتے ہیں۔',
                    'پریونونه او وایرویډونه هم د ویروس په څېر غیر حجروي ذرې دي. پریونونه یوازې له پروټین جوړ دي په داسې حال کې چې وایرویډونه یوازې له کړۍ ډوله RNA جوړ دي. دواړه په بوټو کې ناروغۍ پیدا کوي.')])
    s.p('Viruses are unique particles. They are not considered as living organisms and are not included in the classification system. They have some living characters. For example, they reproduce. They contain RNA or DNA as hereditary material which is enclosed in a protein coat. They also have non-living characters. For example, they are not made of cells and so do not respire or excrete. They live as parasites in all types of organisms and cause diseases in them. They use the metabolism of the cells in which they live. Outside the living host cells, they are inactive. Viruses can be crystallized and this is a property of non-living materials. In crystal form they can be stored for an indefinite period of time, without any loss of reproductive ability. When the crystallized viruses are placed under favourable conditions, they again start reproducing.',
        'وائرس منفرد ذرات ہیں۔ انہیں جاندار نہیں سمجھا جاتا اور درجہ بندی کے نظام میں شامل نہیں کیا جاتا۔ ان میں کچھ جانداروں والی خصوصیات ہیں۔ مثال کے طور پر، یہ تولید کرتے ہیں۔ ان میں موروثی مادے کے طور پر آر این اے یا ڈی این اے ہوتا ہے جو پروٹین کے خول میں بند ہوتا ہے۔ ان میں بے جان اشیا والی خصوصیات بھی ہیں۔ مثال کے طور پر، یہ خلیات سے نہیں بنے ہوتے اس لیے تنفس یا اخراج نہیں کرتے۔ یہ ہر قسم کے جانداروں میں طفیلیوں کے طور پر رہتے اور ان میں بیماریاں پیدا کرتے ہیں۔ یہ ان خلیوں کا میٹابولزم استعمال کرتے ہیں جن میں یہ رہتے ہیں۔ زندہ میزبان خلیوں سے باہر یہ غیر فعال ہوتے ہیں۔ وائرسوں کو قلمایا جا سکتا ہے اور یہ بے جان مادوں کی خاصیت ہے۔ قلمی شکل میں انہیں تولیدی صلاحیت کھوئے بغیر غیر معینہ مدت تک محفوظ رکھا جا سکتا ہے۔ جب قلمائے ہوئے وائرسوں کو موافق حالات میں رکھا جائے تو یہ دوبارہ تولید شروع کر دیتے ہیں۔',
        'ویروسونه ځانګړې ذرې دي. دوی ژوندي موجودات نه ګڼل کېږي او د ډلبندۍ په سیسټم کې نه دي شامل. دوی ځینې ژوندۍ ځانګړتیاوې لري. د بېلګې په توګه، تکثر کوي. دوی د ارثي مادې په توګه RNA یا DNA لري چې په پروټیني پوښ کې تړل شوې وي. دوی بې ژوندي ځانګړتیاوې هم لري. د بېلګې په توګه، له حجرو جوړ نه دي او نو تنفس یا اطراح نه کوي. دوی په هر ډول موجوداتو کې د پرازیت په توګه ژوند کوي او په هغوی کې ناروغۍ پیدا کوي. دوی د هغو حجرو میټابولیزم کاروي چې پکې اوسېږي. له ژوندیو کوربه حجرو بهر غیر فعال وي. ویروسونه کرسټال کېدای شي او دا د بې ژوندو موادو ځانګړتیا ده. په کرسټالي بڼه د تکثر د وړتیا له لاسه ورکولو پرته د نامعلوم وخت لپاره ساتل کېدای شي. کله چې کرسټال شوي ویروسونه په مناسبو شرایطو کې کېښودل شي، بیا تکثر پیلوي.')
    s.fig('bio3-fig3-13', virus(VIR_EN), virus(VIR_UR), virus(VIR_PS), .4,
          caption=('Figure 3.13: Virus', 'شکل 3.13: وائرس', 'شکل 3.13: ویروس'))
    out.append(s)
    return out
