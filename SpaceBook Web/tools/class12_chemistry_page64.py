"""PDF64 / printed120–121: elimination and alkene addition reactions."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_page59 import Drawing


def reactions(kind,language):
    labels={
        'en':{'ethyl bromide':'ethyl bromide','ethene':'ethene','ethane':'ethane','propene':'propene','propane':'propane','alcohol':'alcohol','ethyl alcohol':'ethyl alcohol','Vegetable oil':'Vegetable oil','Vegetable ghee':'Vegetable ghee','2-bromopropane':'2-bromopropane','1-bromopropane':'1-bromopropane','or':'or'},
        'ur':{'ethyl bromide':'ایتھائل برومائیڈ','ethene':'ایتھین (دوہرا بند)','ethane':'ایتھین (اکیلا بند)','propene':'پروپین (دوہرا بند)','propane':'پروپین (اکیلا بند)','alcohol':'الکوحل','ethyl alcohol':'ایتھائل الکوحل','Vegetable oil':'نباتاتی تیل','Vegetable ghee':'نباتاتی گھی','2-bromopropane':'2-بروموپروپین','1-bromopropane':'1-بروموپروپین','or':'یا'},
        'ps':{'ethyl bromide':'ایتایل برومایډ','ethene':'ایتین','ethane':'ایتان','propene':'پروپین','propane':'پروپان','alcohol':'الکول','ethyl alcohol':'ایتایل الکول','Vegetable oil':'نباتي غوړي','Vegetable ghee':'نباتي جامد غوړي','2-bromopropane':'2-بروموپروپان','1-bromopropane':'1-بروموپروپان','or':'یا'},
    }[language]
    height={'elimination':220,'hydrogenation':220,'ghee':115,'hbr-ethene':120,'hbr-propene':245,'hydration':130}[kind]
    d=Drawing(950,height,{'en':'Alkene reaction: ','ur':'الکین کا تعامل: ','ps':'د الکین تعامل: '}[language]+kind)
    def arrow(x1,x2,y,above='',below=''):
        d.line(x1,y,x2,y,'#a62147',1.7,'marker-end="url(#arrow59)"')
        if above:d.text((x1+x2)/2,y-13,above,16)
        if below:d.text((x1+x2)/2,y+24,below,16)
    def t(x,y,value,size=24):d.text(x,y,value,size)
    def caption(x,y,key):t(x,y,labels[key],16)
    if kind=='elimination':
        for x in (110,180):
            t(x,105,'C');t(x,44,'H' if x==110 else 'Br');t(x,170,'H')
            d.line(x,54,x,82);d.line(x,114,x,146)
        t(50,105,'H');t(240,105,'H');d.line(65,98,92,98);d.line(126,98,164,98);d.line(196,98,224,98)
        t(320,105,'+ KOH');caption(147,205,'ethyl bromide')
        arrow(404,508,98,labels['alcohol'],'60°C')
        for x in (575,645):t(x,105,'C')
        d.line(590,94,630,94);d.line(590,101,630,101)
        for x,dx in [(575,-27),(645,27)]:
            d.line(x+dx*.25,84,x+dx,50);d.line(x+dx*.25,116,x+dx,150)
            t(x+dx,39,'H');t(x+dx,172,'H')
        caption(610,205,'ethene');t(809,105,'+ H₂O + KBr',22)
    elif kind=='hydrogenation':
        for y,left,right,lc,rc,lower in [(52,'H₂C = CH₂ + H₂','CH₃ — CH₃','ethene','ethane',labels['or']+' Pt '+labels['or']+' Pd/25°C'),(152,'CH₃ — CH = CH₂ + H₂','CH₃ — CH₂ — CH₃','propene','propane','Pt '+labels['or']+' Pd/25°C')]:
            t(218,y,left);t(751,y,right);caption(170,y+36,lc);caption(750,y+36,rc)
            arrow(397,587,y-7,'Ni/200–250°C',lower)
    elif kind=='ghee':
        t(228,56,labels['Vegetable oil']+' + H₂',23);t(741,56,labels['Vegetable ghee'],23)
        arrow(430,583,49,'150–250°C','Raney Ni')
    elif kind=='hbr-ethene':
        t(230,51,'CH₂ = CH₂ + H — Br');t(742,51,'CH₃ — CH₂ — Br')
        arrow(462,575,44);caption(140,92,'ethene');caption(742,92,'ethyl bromide')
    elif kind=='hbr-propene':
        t(204,127,'CH₃ — CH = CH₂');caption(204,164,'propene')
        d.line(382,120,488,120);t(425,107,'HBr',18)
        d.path('M488 120L488 54L570 54',extra='marker-end="url(#arrow59)"')
        d.path('M488 120L488 196L570 196',extra='marker-end="url(#arrow59)"')
        t(739,61,'CH₃ — CH — CH₃');d.line(739,40,739,21);t(739,16,'Br',21)
        caption(739,96,'2-bromopropane')
        t(739,203,'CH₃ — CH₂ — CH₂ — Br',22);caption(739,235,'1-bromopropane')
    else:
        t(225,60,'H₂C = CH₂ + H₂O');t(758,60,'CH₃—CH₂—OH')
        arrow(447,583,53,'H₂SO₄','100°C');caption(140,101,'ethene');caption(758,101,'ethyl alcohol')
    return d.finish()


paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def figure(name,formula):
    identity='chem12-p64-'+name
    blocks.append({'id':identity,'svg':reactions(name,'en'),'svgUrdu':reactions(name,'ur'),'svgPashto':reactions(name,'ps'),'sourceChemicalEquation':formula})
    layout.append({'type':'visual','blockId':identity})

add('Industrially dehydration of alcohol is carried out by passing vapours of alcohol over alumina (Al₂O₃) at 400°C.',
    'صنعتی طور پر الکوحل کی آب ربائی، الکوحل کے بخارات کو 400°C پر ایلومینا (Al₂O₃) کے اوپر سے گزار کر کی جاتی ہے۔',
    'په صنعتي کچه له الکول څخه د اوبو ایستل د الکول د بخارونو په تېرولو سره پر الومینا (Al₂O₃) باندې په 400°C کې ترسره کېږي.')
add('16.5.5.2 Dehydrohalogenation of Alkyl Halides','16.5.5.2 الکائل ہیلائیڈز کی ڈی ہائیڈروہیلوجینیشن','16.5.5.2 د الکایل هالایډونو ډی هایدروهالوجینېشن','heading')
add('When an alkyl halide is heated with alcoholic solution of KOH or NaOH, hydrogen and halogen are eliminated which results in the formation of an alkene.',
    'جب کسی الکائل ہیلائیڈ کو KOH یا NaOH کے الکوحلی محلول کے ساتھ گرم کیا جائے تو ہائیڈروجن اور ہیلوجن خارج ہوتے ہیں، جس کے نتیجے میں الکین (دوہرے بند والا مرکب) بنتا ہے۔',
    'کله چې یو الکایل هالایډ د KOH یا NaOH له الکولي محلول سره تود شي، هایدروجن او هالوجن ترې ایستل کېږي چې په پایله کې الکین جوړېږي.')
figure('elimination','CH₃CH₂Br + KOH → CH₂=CH₂ + H₂O + KBr; alcohol,60°C')
add('16.5.6 Reactivity of Alkenes','16.5.6 الکینز کی تعامل پذیری','16.5.6 د الکینونو تعامل وړتیا','heading')
add('Alkenes are more reactive than alkanes due the presence of pi (π) bond in the alkene molecules. The overlap of atomic orbitals forming the pi bond is not as effective as that in sigma (δ) bonds. Thus, pi bond is weaker than a sigma bond and more easily broken. The electron density of pi bond lies above and below the bond axis. It is therefore, more exposed and easily accessible to an external electrophilic (electron seeking) reagent, commonly known as electrophile. It is, therefore, favorable for alkenes to add an electrophile across the double bond by breaking the weak pi bond to form strong sigma bonds and to produce a saturated compound. Such reactions in which unsaturated compounds are converted into saturated compounds, are called addition reactions. When addition reaction of alkenes is initiated by electrophile, this addition is specifically called electrophilic addition.',
    'الکینز کے سالموں میں پائی (π) بند کی موجودگی کی وجہ سے یہ الکینز (اکیلے بند والے مرکبات) سے زیادہ تعامل پذیر ہوتے ہیں۔ پائی بند بنانے والے ایٹمی آربیٹلوں کا تداخل سگما (δ) بندوں کے تداخل جتنا مؤثر نہیں ہوتا۔ لہٰذا پائی بند سگما بند سے کمزور ہوتا ہے اور زیادہ آسانی سے ٹوٹ جاتا ہے۔ پائی بند کی الیکٹرانی کثافت بند کے محور کے اوپر اور نیچے ہوتی ہے۔ اس لیے یہ زیادہ کھلی ہوتی ہے اور بیرونی الیکٹروفائل (الیکٹران طلب کرنے والے) عامل کو بآسانی دستیاب ہوتی ہے، جسے عام طور پر الیکٹروفائل کہتے ہیں۔ چنانچہ الکینز کے لیے یہ موزوں ہوتا ہے کہ کمزور پائی بند توڑ کر دوہرے بند پر الیکٹروفائل کا اضافہ کریں، مضبوط سگما بند بنائیں اور سیر شدہ مرکب پیدا کریں۔ ایسے تعاملات جن میں غیر سیر شدہ مرکبات سیر شدہ مرکبات میں تبدیل ہوں، اضافی تعاملات کہلاتے ہیں۔ جب الکینز کا اضافی تعامل الیکٹروفائل شروع کرے تو اس اضافے کو خاص طور پر الیکٹروفائل اضافہ کہتے ہیں۔',
    'الکینونه په خپلو مالیکولونو کې د پای (π) تړون د شتون له امله له الکانونو ډېر تعامل کوونکي دي. د پای تړون جوړوونکو اټومي اوربیټالونو تداخل د سیګما (δ) تړونونو هومره اغېزمن نه دی. نو پای تړون له سیګما تړون کمزوری دی او په اسانۍ ماتېږي. د پای تړون الکتروني کثافت د تړون د محور پورته او لاندې وي. له همدې امله ډېر بربنډ او بهرني الکتروفایلي (الکترون غوښتونکي) عامل ته په اسانۍ د لاسرسي وړ وي، چې عموماً الکتروفایل بلل کېږي. نو د الکینونو لپاره مناسبه ده چې کمزوری پای تړون مات کړي، پر دوه ګوني تړون الکتروفایل ورزیات کړي، قوي سیګما تړونونه جوړ کړي او مشبوع مرکب تولید کړي. داسې تعاملونه چې نامشبوع مرکبات په مشبوع مرکباتو بدلوي، اضافي تعاملونه بلل کېږي. کله چې د الکینونو اضافي تعامل الکتروفایل پیل کړي، دا اضافه په ځانګړي ډول الکتروفایلي اضافه بلل کېږي.')
add('16.5.7 Reactions of Alkenes','16.5.7 الکینز کے تعاملات','16.5.7 د الکینونو تعاملونه','heading')
add('16.5.7.1 Hydrogenation (Addition of Hydrogen)','16.5.7.1 ہائیڈروجینیشن (ہائیڈروجن کا اضافہ)','16.5.7.1 هایدروجینېشن (د هایدروجن زیاتول)','heading')
add('Alkenes readily add hydrogen to form alkanes in the presence of finely divided catalyst such as nickel, platinum or palladium at a temperature of 200–250°C and under moderate pressure (1–5 atm). This is called catalytic hydrogenation and reaction occurs on the surface of catalyst. The reaction is exothermic and the heat released during hydrogenation of an alkene is called heat of hydrogenation.',
    'الکینز، باریک تقسیم شدہ عمل انگیز مثلاً نکل، پلاٹینم یا پیلیڈیم کی موجودگی میں 200–250°C درجہ حرارت اور معتدل دباؤ (1–5 atm) پر آسانی سے ہائیڈروجن شامل کر کے الکینز (سیر شدہ مرکبات) بناتے ہیں۔ اسے عمل انگیزی ہائیڈروجینیشن کہتے ہیں اور تعامل عمل انگیز کی سطح پر ہوتا ہے۔ یہ تعامل حرارت خارج کرتا ہے، اور کسی الکین کی ہائیڈروجینیشن کے دوران خارج ہونے والی حرارت کو حرارتِ ہائیڈروجینیشن کہتے ہیں۔',
    'الکینونه د باریک وېشل شوي کتلست لکه نکل، پلاتین یا پالادیم په شتون کې، په 200–250°C تودوخه او منځني فشار (1–5 atm) کې، په اسانۍ هایدروجن ورزیاتوي او الکانونه جوړوي. دې ته کتلستي هایدروجینېشن ویل کېږي او تعامل د کتلست پر سطحه ترسره کېږي. تعامل تودوخه خوشې کوي، او د الکین د هایدروجینېشن پر مهال خوشې شوې تودوخه د هایدروجینېشن تودوخه بلل کېږي.')
figure('hydrogenation',['H₂C=CH₂ + H₂ → CH₃—CH₃; Ni/200–250°C or Pt or Pd/25°C','CH₃—CH=CH₂ + H₂ → CH₃—CH₂—CH₃; Ni/200–250°C, Pt or Pd/25°C'])
add('Preparation of vegetable ghee from vegetable oil is an example of catalytic hydrogenation at industrial scale. The catalyst used in this process is Raney Nickel after the name of M. Raney, who developed this catalyst.',
    'نباتاتی تیل سے نباتاتی گھی کی تیاری صنعتی پیمانے پر عمل انگیزی ہائیڈروجینیشن کی مثال ہے۔ اس عمل میں استعمال ہونے والا عمل انگیز رینی نکل ہے، جس کا نام M. Raney کے نام پر رکھا گیا، جنہوں نے یہ عمل انگیز تیار کیا تھا۔',
    'له نباتي غوړیو څخه د نباتي جامدو غوړیو جوړول په صنعتي کچه د کتلستي هایدروجینېشن بېلګه ده. په دې بهیر کې کارېدونکی کتلست رېني نکل دی، چې د M. Raney په نوم نومول شوی؛ هغه دا کتلست جوړ کړی و.')
figure('ghee','Vegetable oil + H₂ → Vegetable ghee; 150–250°C, Raney Ni')
add('16.5.7.2 Hydrohalogenation','16.5.7.2 ہائیڈروہیلوجینیشن','16.5.7.2 هایدروهالوجینېشن','heading')
add('Alkenes react with hydrogen halide (halogen acids: HCl, HBr or HI) to form an addition product, the alkyl halides (or haloalkanes). The order of reactivity of halogen acids increases down the group.',
    'الکینز ہائیڈروجن ہیلائیڈ (ہیلوجن تیزاب: HCl، HBr یا HI) کے ساتھ تعامل کر کے اضافی پیداوار، یعنی الکائل ہیلائیڈز (یا ہیلواَلکینز)، بناتے ہیں۔ ہیلوجن تیزابوں کی تعامل پذیری گروپ میں نیچے کی طرف بڑھتی ہے۔',
    'الکینونه له هایدروجن هالایډ (هالوجني اسیدونه: HCl، HBr یا HI) سره تعامل کوي او اضافي محصول، یعنې الکایل هالایډونه (یا هالو الکانونه)، جوړوي. د هالوجني اسیدونو تعامل وړتیا په ګروپ کې ښکته خوا ته زیاتېږي.')
figure('hbr-ethene','CH₂=CH₂ + H—Br → CH₃—CH₂—Br')
add('When the alkene is symmetric (as in the case of ethene), only single product is formed. However if the alkene is asymmetric, two different isomeric products are possible. For example, propene can react with HBr in the following two ways.',
    'جب الکین متناسب ہو (جیسے ایتھین)، تو صرف ایک پیداوار بنتی ہے۔ تاہم اگر الکین غیر متناسب ہو تو دو مختلف آئسومری پیداواریں ممکن ہوتی ہیں۔ مثلاً پروپین درج ذیل دو طریقوں سے HBr کے ساتھ تعامل کر سکتا ہے۔',
    'کله چې الکین متقارن وي (لکه ایتین)، یوازې یو محصول جوړېږي. خو که الکین نامتقارن وي، دوه بېلابېل ایزومري محصولات ممکن دي. د بېلګې په توګه، پروپین له HBr سره په لاندې دوو لارو تعامل کولی شي.')
figure('hbr-propene',['CH₃—CH=CH₂ + HBr → CH₃—CH(Br)—CH₃ (2-bromopropane)','CH₃—CH=CH₂ + HBr → CH₃—CH₂—CH₂—Br (1-bromopropane)'])
add('However, experimentally it has been found that 2–bromopropane is the major product. In fact this is in accordance with the Markovnikov’s rule, which states that; when an asymmetric reagent is added to an asymmetric alkene, the positive part of the molecule attaches itself to that carbon atom involved in the double bond, holding greater number of hydrogen atoms.',
    'تاہم تجرباتی طور پر معلوم ہوا ہے کہ 2–بروموپروپین بڑی پیداوار ہے۔ دراصل یہ مارکونیکوف کے اصول کے مطابق ہے، جو بیان کرتا ہے کہ جب غیر متناسب عامل کسی غیر متناسب الکین میں شامل کیا جائے تو سالمے کا مثبت حصہ دوہرے بند میں شامل اس کاربن ایٹم سے جڑتا ہے جس کے ساتھ ہائیڈروجن ایٹموں کی تعداد زیادہ ہو۔',
    'خو په تجربوي ډول موندل شوې چې 2–بروموپروپان عمده محصول دی. په حقیقت کې دا د مارکوفنیکوف له قاعدې سره سمون لري، چې وايي: کله چې یو نامتقارن عامل نامتقارن الکین ته ورزیات شي، د مالیکول مثبت برخه په دوه ګوني تړون کې له هغه کاربني اټوم سره نښلي چې ډېر هایدروجني اټومونه لري.')
add('16.5.7.3 Hydration','16.5.7.3 ہائیڈریشن','16.5.7.3 هایدرېشن','heading')
add('Alkenes can add a molecule of water across the double bond to form alcohol. This process is known as hydration. Direct hydration of alkene can be accomplished by acid-catalyzed addition of water at 100°C. The most commonly used acids to catalyze this reaction are sulfuric acid and phosphoric acid.',
    'الکینز اپنے دوہرے بند پر پانی کا ایک سالمہ شامل کر کے الکوحل بنا سکتے ہیں۔ اس عمل کو ہائیڈریشن کہتے ہیں۔ الکین کی براہ راست ہائیڈریشن 100°C پر تیزاب کی عمل انگیزی سے پانی شامل کر کے کی جا سکتی ہے۔ اس تعامل میں عمل انگیز کے طور پر سب سے زیادہ استعمال ہونے والے تیزاب سلفیورک ایسڈ اور فاسفورک ایسڈ ہیں۔',
    'الکینونه پر دوه ګوني تړون د اوبو یو مالیکول ورزیاتولی شي، څو الکول جوړ کړي. دا بهیر هایدرېشن بلل کېږي. د الکین مستقیم هایدرېشن په 100°C کې د اسید په کتلستۍ د اوبو په زیاتولو ترسره کېدای شي. د دې تعامل د کتلستۍ لپاره تر ټولو ډېر کارېدونکي اسیدونه سلفوریک اسید او فاسفوریک اسید دي.')
figure('hydration','H₂C=CH₂ + H₂O → CH₃—CH₂—OH; H₂SO₄,100°C')

record=section('16.11','Alkene preparation, reactivity and addition reactions','الکینز کی تیاری، تعامل پذیری اور اضافی تعاملات','د الکینونو چمتو کول، تعامل وړتیا او اضافي تعاملونه',paras,layout,blocks,'120–121')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':64,'printedPages':[120,121]}]
record['sourceContinuesOnPdfPage']=65
issues=[{'id':'chem12-p120-sigma-symbol','printedPage':120,'description':'Printed 16.5.6 text writes sigma (δ); retained as printed (σ intended).'},{'id':'chem12-p120-hydrogenation-temperature','printedPage':120,'description':'Prose groups nickel, platinum and palladium with 200–250°C; printed equations separately specify Ni at200–250°C and Pt/Pd at25°C. Both source statements retained.'}]
carry=[{'from':'16.11','to':'16.12','startsAt':'In case of asymmetric alkenes, the reaction follows the Markovnikov&#x27;s rule.'}]
if __name__=='__main__':save(64,[record],carry=carry,issues=issues,chapter_number=16)
