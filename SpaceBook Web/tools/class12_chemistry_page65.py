"""PDF65 / printed122–123: hydration, bromination, epoxides and ozonolysis."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_page59 import Drawing

LABELS={
 'en':{'ethene':'ethene','propene':'propene','propan-2-ol':'propan-2-ol','cyclic':'cyclic bromonium','ion':'ion','dibromo':'1,2-dibromoethane','vic':'(a vic-dibromide)','bromoethanol':'2-bromoethanol','bromohydrin':'(ethylene bromohydrin)','peracetic':'peracetic acid','oxide':'ethylene oxide','oxirane':'(oxirane)','acetic':'acetic acid','molozonide':'ethylene molozonide','ozonide':'ethylene ozonide','rearrangment':'rearrangment'},
 'ur':{'ethene':'ایتھین','propene':'پروپین','propan-2-ol':'پروپین-2-اول','cyclic':'حلقوی برومونیم','ion':'آئن','dibromo':'1,2-ڈائی بروموایتھین','vic':'(وِس ڈائی برومائیڈ)','bromoethanol':'2-بروموایتھانول','bromohydrin':'(ایتھیلین بروموہائیڈرین)','peracetic':'پیرایسیٹک ایسڈ','oxide':'ایتھیلین آکسائیڈ','oxirane':'(آکسی رین)','acetic':'ایسیٹک ایسڈ','molozonide':'ایتھیلین مولوزونائیڈ','ozonide':'ایتھیلین اوزونائیڈ','rearrangment':'دوبارہ ترتیب'},
 'ps':{'ethene':'ایتین','propene':'پروپین','propan-2-ol':'پروپان-2-اول','cyclic':'کړیز برومونیم','ion':'ایون','dibromo':'1,2-ډای بروموایتان','vic':'(وِس ډای برومایډ)','bromoethanol':'2-بروموایتانول','bromohydrin':'(ایتلین بروموهایډرین)','peracetic':'پراسیټیک اسید','oxide':'ایتلین اکسایډ','oxirane':'(اوکسیران)','acetic':'اسیټیک اسید','molozonide':'ایتلین مولوزونایډ','ozonide':'ایتلین اوزونایډ','rearrangment':'بیا ترتیب'},
}


def reaction(kind,language):
    labels=LABELS[language]
    height={'hydration':145,'halogenation':255,'halohydration':440,'epoxidation':180,'air-oxidation':155,'ozonolysis':205}[kind]
    d=Drawing(1080,height,{'en':'Alkene reaction mechanism: ','ur':'الکین کے تعامل کا طریق کار: ','ps':'د الکین د تعامل میکانیزم: '}[language]+kind)
    def t(x,y,value,size=22):d.text(x,y,value,size)
    def cap(x,y,key):t(x,y,labels[key],16)
    def arrow(x1,x2,y,above='',below=''):
        d.line(x1,y,x2,y,'#a3264d',1.7,'marker-end="url(#arrow59)"')
        if above:t((x1+x2)/2,y-13,above,16)
        if below:t((x1+x2)/2,y+23,below,16)
    def epoxide(cx,y):
        t(cx,y-42,'O');t(cx-45,y,'CH₂');t(cx+45,y,'CH₂')
        d.line(cx-25,y-7,cx+23,y-7);d.line(cx-37,y-21,cx-8,y-40);d.line(cx+10,y-41,cx+35,y-19)
    def ethene_br_start():
        t(107,87,'H₂C = CH₂');t(229,87,'+');t(306,87,'Br—Br')
        cap(107,124,'ethene')
        d.path('M101 62C151 19 224 21 276 65',extra='marker-end="url(#arrow59)"')
        d.path('M306 64C304 31 331 32 331 64',extra='marker-end="url(#arrow59)"')
        arrow(359,405,80,below='− Br⁻')
    def carbocation():
        t(467,87,'H₂C⁺');t(553,87,'CH₂');d.line(491,80,532,80)
        d.line(554,98,554,121);t(554,147,'Br')
        for x,y in [(532,132),(532,141),(575,132),(575,141),(550,156),(559,156)]:d.dot(x,y,2.4)
        d.path('M529 137C489 139 467 117 467 99',extra='marker-end="url(#arrow59)"')
        arrow(589,641,80)
    def bromonium():
        t(692,87,'H₂C');t(791,87,'CH₂');d.line(713,80,770,80)
        d.line(701,101,733,133);d.line(783,101,753,133);t(744,148,'Br');t(736,124,'+',17)
        d.path('M779 116C809 133 782 154 761 146',extra='marker-end="url(#arrow59)"')
        cap(744,182,'cyclic');cap(744,204,'ion')
    if kind=='hydration':
        t(247,66,'CH₃—CH=CH₂ + H₂O');cap(168,109,'propene')
        arrow(476,605,59,'H₂SO₄','100°C')
        t(823,66,'CH₃—CH—CH₃');d.line(823,44,823,31);t(823,24,'OH');cap(823,109,'propan-2-ol')
    elif kind in ('halogenation','halohydration'):
        ethene_br_start();carbocation();bromonium()
        if kind=='halogenation':
            t(870,44,'Br⁻')
            d.path('M857 26C833 17 805 38 792 61',extra='marker-end="url(#arrow59)"')
            arrow(841,894,80)
            t(938,87,'H₂C');t(1023,87,'CH₂');d.line(957,80,1001,80)
            d.line(938,97,938,131);t(938,155,'Br');d.line(1023,65,1023,34);t(1023,23,'Br')
            cap(982,205,'dibromo');cap(982,229,'vic')
        else:
            t(920,84,'H₂O')
            d.path('M914 60C882 28 817 36 793 63',extra='marker-end="url(#arrow59)"')
            d.path('M918 98L994 98L994 289L939 289','#a3264d',extra='marker-end="url(#arrow59)"')
            # Protonated haloalcohol, followed by loss of H+ to the final product.
            for left,right,protonated in [(827,914,True),(606,693,False)]:
                t(left,297,'H₂C');t(right,297,'CH₂');d.line(left+22,289,right-22,289)
                d.line(left,306,left,334);t(left,356,'Br')
                d.line(right,276,right,246);t(right,235,'OH₂' if protonated else 'OH')
                if protonated:t(right,210,'+',18)
            arrow(774,731,289,below='− H⁺')
            cap(650,395,'bromoethanol');cap(650,420,'bromohydrin')
    elif kind=='epoxidation':
        t(127,68,'CH₂ = CH₂');t(266,68,'+');t(383,68,'CH₃COOOH')
        cap(127,103,'ethene');cap(383,103,'peracetic');arrow(478,615,61)
        epoxide(735,68);cap(735,109,'oxide');cap(735,131,'oxirane')
        t(858,68,'+');t(962,68,'CH₃COOH');cap(962,103,'acetic')
    elif kind=='air-oxidation':
        t(332,72,'CH₂ = CH₂ + ½ O₂');cap(258,109,'ethene');arrow(532,668,65,'Ag₂O','300°C')
        epoxide(824,72);cap(824,115,'oxide');cap(824,137,'oxirane')
    else:
        t(169,112,'CH₂ = CH₂ + O₃');cap(129,151,'ethene');arrow(335,453,105)
        # Printed molozonide: adjacent C–C at the base and three successive O atoms.
        t(532,141,'H₂C');t(616,141,'CH₂');d.line(552,134,595,134)
        t(534,83,'O');t(614,83,'O');t(574,39,'O')
        d.line(534,92,534,119);d.line(614,92,614,119);d.line(544,66,566,42);d.line(604,66,582,42)
        cap(574,181,'molozonide');arrow(682,815,105,labels['rearrangment'])
        # Printed ozonide: O–C–O–O–C five-membered ring.
        t(923,46,'O');t(875,99,'H₂C');t(971,99,'CH₂');t(884,153,'O');t(962,153,'O')
        d.line(916,49,891,77);d.line(931,49,954,77);d.line(880,108,883,129);d.line(968,108,963,129);d.line(895,146,951,146)
        cap(923,181,'ozonide')
    return d.finish()


paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def figure(name,formula):
    identity='chem12-p65-'+name
    blocks.append({'id':identity,'svg':reaction(name,'en'),'svgUrdu':reaction(name,'ur'),'svgPashto':reaction(name,'ps'),'sourceChemicalEquation':formula})
    layout.append({'type':'visual','blockId':identity})

add('In case of asymmetric alkenes, the reaction follows the Markovnikov’s rule. For example hydration of propene gives mainly isopropyl alcohol (propane–2–ol).',
    'غیر متناسب الکینز کی صورت میں تعامل مارکونیکوف کے اصول کی پیروی کرتا ہے۔ مثلاً پروپین کی ہائیڈریشن سے بنیادی طور پر آئسوپروپائل الکوحل (پروپین–2–اول) حاصل ہوتی ہے۔',
    'د نامتقارنو الکینونو په حالت کې تعامل د مارکوفنیکوف قاعده تعقیبوي. د بېلګې په توګه، د پروپین هایدرېشن په عمده ډول ایزوپروپایل الکول (پروپان–2–اول) ورکوي.')
figure('hydration','CH₃—CH=CH₂ + H₂O → CH₃—CH(OH)—CH₃; H₂SO₄,100°C')
add('16.5.7.4 Halogenation','16.5.7.4 ہیلوجینیشن','16.5.7.4 هالوجینېشن','heading')
add('Alkenes readily add halogen (chlorine and bromine) in an inert solvent such as carbon tetrachloride or carbon disulfide to form vicinal dihalides (or vic-dihalides). Vicinal dichlorides and dibromides are unstable at high temperature, while vicinal diiodides are unstable even at room temperature. The reactivity of various halogens with alkenes decrease down the group. Reaction involves in the formation of a cyclic halonium ion. For example ethene upon reaction with bromine in inert solvent, form 1, 2 dibromoethane (ethylene dibromide).',
    'الکینز غیر عامل محلل، مثلاً کاربن ٹیٹراکلورائیڈ یا کاربن ڈائی سلفائیڈ، میں آسانی سے ہیلوجن (کلورین اور برومین) شامل کر کے وِسینل ڈائی ہیلائیڈز (یا وِس ڈائی ہیلائیڈز) بناتے ہیں۔ وِسینل ڈائی کلورائیڈز اور ڈائی برومائیڈز زیادہ درجہ حرارت پر غیر مستحکم ہوتے ہیں، جبکہ وِسینل ڈائی آئیوڈائیڈز کمرے کے درجہ حرارت پر بھی غیر مستحکم ہوتے ہیں۔ الکینز کے ساتھ مختلف ہیلوجنوں کی تعامل پذیری گروپ میں نیچے کی طرف کم ہوتی ہے۔ تعامل میں حلقوی ہیلونیم آئن کی تشکیل شامل ہوتی ہے۔ مثلاً ایتھین غیر عامل محلل میں برومین کے ساتھ تعامل کر کے 1،2-ڈائی بروموایتھین (ایتھیلین ڈائی برومائیڈ) بناتا ہے۔',
    'الکینونه په غیر فعال محلل، لکه کاربن ټېټراکلورایډ یا کاربن ډای سلفایډ، کې په اسانۍ هالوجن (کلورین او برومین) ورزیاتوي او ویسینل ډای هالایډونه (یا وِس ډای هالایډونه) جوړوي. ویسینل ډای کلورایډونه او ډای برومایډونه په لوړه تودوخه کې بې ثباته دي، خو ویسینل ډای ایوډایډونه ان د خونې په تودوخه کې هم بې ثباته دي. له الکینونو سره د بېلابېلو هالوجنونو تعامل وړتیا په ګروپ کې ښکته خوا ته کمېږي. تعامل د کړیز هالونیم ایون جوړېدل رانغاړي. د بېلګې په توګه، ایتین په غیر فعال محلل کې له برومین سره د تعامل په پایله کې 1،2-ډای بروموایتان (ایتلین ډای برومایډ) جوړوي.')
figure('halogenation','H₂C=CH₂ + Br—Br → H₂C⁺—CH₂—Br (−Br⁻) → cyclic bromonium ion → BrCH₂—CH₂Br')
add('The bromination of alkenes provides a useful test for the presence of a double bond in the molecules. When dilute solution of bromine is added to a compound containing carbon-carbon double bond, the colour of bromine rapidly discharges as the colorless dibromo compound is formed. This is called bromine water test.',
    'الکینز کی برومینیشن سالموں میں دوہرے بند کی موجودگی کا مفید ٹیسٹ فراہم کرتی ہے۔ جب کاربن–کاربن دوہرا بند رکھنے والے مرکب میں برومین کا ہلکا محلول شامل کیا جائے تو بے رنگ ڈائی برومو مرکب بننے سے برومین کا رنگ تیزی سے ختم ہو جاتا ہے۔ اسے برومین واٹر ٹیسٹ کہتے ہیں۔',
    'د الکینونو برومینېشن په مالیکولونو کې د دوه ګوني تړون د شتون ګټوره ازموینه برابروي. کله چې د برومین رقیق محلول د کاربن–کاربن دوه ګوني تړون لرونکي مرکب ته ورزیات شي، د بې رنګه ډای برومو مرکب په جوړېدو د برومین رنګ ژر له منځه ځي. دې ته د برومین اوبو ازموینه ویل کېږي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Geminal dihalides (or gem-dihalide) have both halogen atoms attached to the same carbon atom whereas vicinal dihalides (or vic-dihalides) have their two halogen atoms attached to two adjacent carbon atoms.',
    'جیمینل ڈائی ہیلائیڈز (یا جیم ڈائی ہیلائیڈ) میں دونوں ہیلوجن ایٹم ایک ہی کاربن ایٹم سے جڑے ہوتے ہیں، جبکہ وِسینل ڈائی ہیلائیڈز (یا وِس ڈائی ہیلائیڈز) میں دونوں ہیلوجن ایٹم دو ساتھ والے کاربن ایٹموں سے جڑے ہوتے ہیں۔',
    'په جېمینل ډای هالایډونو (یا جېم ډای هالایډ) کې دواړه هالوجني اټومونه له یوه کاربني اټوم سره نښتي وي، خو په ویسینل ډای هالایډونو (یا وِس ډای هالایډونو) کې دوه هالوجني اټومونه له دوو ګاونډیو کاربني اټومونو سره نښتي وي.')
add('16.5.7.5 Halohydration','16.5.7.5 ہیلوہائیڈریشن','16.5.7.5 هالوهایدرېشن','heading')
add('When alkene is reacted with halogen in an inert solvent, vic-dihalides are formed, because halide ion is the only nucleophile available for reaction with the intermediate cyclic halonium ion. However if the reaction is performed in aqueous solution, water can also act as nucleophile and attack on cyclic halonium ion to form halo-alcohols, commonly known as halohydrin. For example; ethene when reacted with aqueous bromine, forms 2-bromoethanol, commonly called ethylene bromohydrin.',
    'جب الکین کا تعامل غیر عامل محلل میں ہیلوجن کے ساتھ کیا جائے تو وِس ڈائی ہیلائیڈز بنتے ہیں، کیونکہ درمیانی حلقوی ہیلونیم آئن کے ساتھ تعامل کے لیے صرف ہیلائیڈ آئن ہی نیوکلیوفائل کے طور پر دستیاب ہوتا ہے۔ تاہم اگر تعامل آبی محلول میں کیا جائے تو پانی بھی نیوکلیوفائل کے طور پر کام کر سکتا ہے اور حلقوی ہیلونیم آئن پر حملہ کر کے ہیلوالکوحل بنا سکتا ہے، جسے عام طور پر ہیلوہائیڈرین کہتے ہیں۔ مثلاً ایتھین آبی برومین کے ساتھ تعامل کر کے 2-بروموایتھانول بناتا ہے، جسے عموماً ایتھیلین بروموہائیڈرین کہتے ہیں۔',
    'کله چې الکین په غیر فعال محلل کې له هالوجن سره تعامل وکړي، وِس ډای هالایډونه جوړېږي، ځکه هالایډ ایون یوازینی نیوکلیوفایل دی چې له منځني کړیز هالونیم ایون سره د تعامل لپاره موجود وي. خو که تعامل په اوبلن محلول کې ترسره شي، اوبه هم د نیوکلیوفایل په توګه کار کولی شي او پر کړیز هالونیم ایون برید کوي، څو هالو الکولونه جوړ کړي چې عموماً هالوهایډرین بلل کېږي. د بېلګې په توګه، ایتین له اوبلن برومین سره په تعامل کې 2-بروموایتانول جوړوي، چې عموماً ایتلین بروموهایډرین بلل کېږي.')
figure('halohydration','H₂C=CH₂ + Br₂ → H₂C⁺—CH₂Br (−Br⁻) → cyclic bromonium ion; +H₂O → BrCH₂—CH₂OH₂⁺; −H⁺ → BrCH₂—CH₂OH')
add('Self-assessment','خود جانچ','ځان ارزونه','heading')
add('Predict the product of bromohydration of but-2-ene and write the complete reaction.',
    'بیوٹ-2-این کی بروموہائیڈریشن کی پیداوار کی پیش گوئی کریں اور مکمل تعامل لکھیں۔',
    'د بیوټ-2-ین د بروموهایدرېشن محصول اټکل کړئ او بشپړ تعامل ولیکئ.')
add('16.5.7.6 Epoxidation','16.5.7.6 ایپو آکسیڈیشن','16.5.7.6 ایپوکسیدېشن','heading')
add('Alkenes on reaction with peroxyacids (or peracid) yield cyclic ethers called epoxides (or oxiranes). This process in known as epoxidation. The most commonly used peracid, is peracetic acid. For example ethylene when treated with peracetic acid form ethylene oxide (epoxyethane or oxirane).',
    'الکینز پیروکسی تیزابوں (یا پیرایسڈ) کے ساتھ تعامل کر کے حلقوی ایتھر بناتے ہیں جنہیں ایپو آکسائیڈز (یا آکسی رینز) کہتے ہیں۔ یہ عمل ایپو آکسیڈیشن کہلاتا ہے۔ سب سے زیادہ استعمال ہونے والا پیرایسڈ، پیرایسیٹک ایسڈ ہے۔ مثلاً ایتھیلین، پیرایسیٹک ایسڈ کے ساتھ عمل کرنے پر ایتھیلین آکسائیڈ (ایپو آکسی ایتھین یا آکسی رین) بناتی ہے۔',
    'الکینونه له پراکسي اسیدونو (یا پراسید) سره په تعامل کې کړیز ایترونه ورکوي چې ایپوکسایډونه (یا اوکسیرانونه) بلل کېږي. دا بهیر ایپوکسیدېشن بلل کېږي. تر ټولو ډېر کارېدونکی پراسید، پراسیټیک اسید دی. د بېلګې په توګه، ایتلین له پراسیټیک اسید سره په تعامل کې ایتلین اکسایډ (ایپوکسي ایتان یا اوکسیران) جوړوي.')
figure('epoxidation','CH₂=CH₂ + CH₃COOOH → ethylene oxide (oxirane) + CH₃COOH')
add('On industrial scale, ethylene oxide is prepared, by air oxidation of ethene with silver oxide catalyst at 300°C.',
    'صنعتی پیمانے پر ایتھیلین آکسائیڈ، سلور آکسائیڈ عمل انگیز کے ساتھ 300°C پر ایتھین کی ہوا سے تکسید کے ذریعے تیار کی جاتی ہے۔',
    'په صنعتي کچه ایتلین اکسایډ د سپینو زرو اکسایډ کتلست په شتون کې په 300°C کې د ایتین د هوايي اکسیدېشن له لارې چمتو کېږي.')
figure('air-oxidation','CH₂=CH₂ + ½ O₂ → ethylene oxide (oxirane); Ag₂O,300°C')
add('16.5.7.7 Ozonolysis','16.5.7.7 اوزونولائسز','16.5.7.7 اوزونولایسس','heading')
add('When ozone (O₃) gas is passed through a solution of alkene in an inert solvent, at low temperature (−80°C), an addition product molozonide is formed. This molozonide rearranges rapidly to form ozonide.',
    'جب اوزون (O₃) گیس کو کم درجہ حرارت (−80°C) پر غیر عامل محلل میں الکین کے محلول سے گزارا جائے تو اضافی پیداوار مولوزونائیڈ بنتی ہے۔ یہ مولوزونائیڈ تیزی سے دوبارہ ترتیب پا کر اوزونائیڈ بناتا ہے۔',
    'کله چې اوزون (O₃) ګاز په ټیټه تودوخه (−80°C) کې په غیر فعال محلل کې د الکین له محلول څخه تېر شي، اضافي محصول مولوزونایډ جوړېږي. دا مولوزونایډ ژر بیا ترتیب مومي او اوزونایډ جوړوي.')
figure('ozonolysis','CH₂=CH₂ + O₃ → ethylene molozonide → ethylene ozonide')

record=section('16.12','Alkene hydration, halogenation, epoxidation and ozonolysis','الکینز کی ہائیڈریشن، ہیلوجینیشن، ایپو آکسیڈیشن اور اوزونولائسز','د الکینونو هایدرېشن، هالوجینېشن، ایپوکسیدېشن او اوزونولایسس',paras,layout,blocks,'122–123')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':65,'printedPages':[122,123]}]
record['sourceContinuesOnPdfPage']=66
carry=[{'from':'16.12','to':'16.13','startsAt':'Ozonides are highly unstable and explosive and cannot be isolated.'}]
issues=[{'id':'chem12-p123-epoxidation-wording','printedPage':123,'description':'Printed wording "This process in known" and reaction label "rearrangment" retained in English; translations convey their intended meaning.'},{'id':'chem12-p122-bromination-sequence','printedPage':122,'description':'Printed bromination/bromohydration mechanisms explicitly show an open carbocation before cyclic bromonium formation; the source sequence is preserved for review.'}]
if __name__=='__main__':save(65,[record],carry=carry,issues=issues,chapter_number=16)
