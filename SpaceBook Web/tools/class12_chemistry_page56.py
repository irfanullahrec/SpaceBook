"""PDF56 (printed104–105): nomenclature, alkyl groups, IUPAC rules1–2.

Build-only on import. Root integration may execute this file after PDF55.
All instructional structures are SVG; source printing ambiguities are retained.
"""
import html
from class12_chemistry_opening import pair, section, SOURCE


class Drawing:
    def __init__(self, width, height, title):
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title, quote=True)}"><rect width="100%" height="100%" fill="white"/>']

    def text(self, x, y, value, size=18, color='#111827'):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" text-anchor="middle" fill="{color}">{html.escape(value)}</text>')

    def line(self, x1, y1, x2, y2, color='#111827'):
        self.parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="1.8" fill="none"/>')

    def box(self, x, y, w, h):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="none" stroke="#334155" stroke-width="1.6"/>')

    def chain(self, x, y, atoms, step=61, top=None, bottom=None, terminal=False, numbers=None):
        for i, a in enumerate(atoms):
            xx=x+i*step
            self.text(xx,y,a)
            if i:
                self.line(xx-step+21,y-6,xx-21,y-6)
            if numbers:
                self.text(xx,y-25,str(numbers[i]),12)
        for i,a in (top or {}).items():
            xx=x+i*step
            self.line(xx,y-17,xx,y-39)
            self.text(xx,y-44,a)
        for i,a in (bottom or {}).items():
            xx=x+i*step
            self.line(xx,y+6,xx,y+27)
            self.text(xx,y+44,a)
        if terminal:
            xx=x+(len(atoms)-1)*step
            self.line(xx+21,y-6,xx+42,y-6)

    def done(self):
        return ''.join(self.parts)+'</svg>'


LABELS={
 'en': {'n-butane':'n-butane','n-pentane':'n-pentane','isobutane':'isobutane','isopentane':'isopentane','neopentane':'neopentane','neohexane':'neohexane','one':'One carbon','two':'Two carbon','three':'Three carbon','four':'Four carbon','methyl':'methyl group','ethyl':'ethyl group','propyl':'propyl group','n-propyl':'(or “n-propyl group”)','isopropyl':'isopropyl group','butyl':'butyl group','n-butyl':'(or “n-butyl group”)','isobutyl':'isobutyl group','sec-butyl':'sec-butyl group','tert-butyl':'tert-butyl group','t-butyl':'(or “t-butyl group”)','primary':'a primary (1°) carbon','secondary':'a secondary (2°) carbon','tertiary':'a tertiary (3°) carbon','correct':'(correct)','incorrect':'(incorrect)'},
 'ur': {'n-butane':'این بیوٹین','n-pentane':'این پینٹین','isobutane':'آئسو بیوٹین','isopentane':'آئسو پینٹین','neopentane':'نیو پینٹین','neohexane':'نیو ہیکسین','one':'ایک کاربن','two':'دو کاربن','three':'تین کاربن','four':'چار کاربن','methyl':'میتھائل گروپ','ethyl':'ایتھائل گروپ','propyl':'پروپائل گروپ','n-propyl':'(یا ”این پروپائل گروپ“)','isopropyl':'آئسو پروپائل گروپ','butyl':'بیوٹائل گروپ','n-butyl':'(یا ”این بیوٹائل گروپ“)','isobutyl':'آئسو بیوٹائل گروپ','sec-butyl':'سیک بیوٹائل گروپ','tert-butyl':'ٹرٹ بیوٹائل گروپ','t-butyl':'(یا ”ٹی بیوٹائل گروپ“)','primary':'پرائمری (1°) کاربن','secondary':'سیکنڈری (2°) کاربن','tertiary':'ٹرشری (3°) کاربن','correct':'(درست)','incorrect':'(غلط)'},
 'ps': {'n-butane':'این بیوتان','n-pentane':'این پېنتان','isobutane':'ایزوبیوتان','isopentane':'ایزوپېنتان','neopentane':'نیوپېنتان','neohexane':'نیوهېکسان','one':'یو کاربن','two':'دوه کاربنه','three':'درې کاربنه','four':'څلور کاربنه','methyl':'میتایل ګروپ','ethyl':'ایتایل ګروپ','propyl':'پروپایل ګروپ','n-propyl':'(یا «این پروپایل ګروپ»)','isopropyl':'ایزوپروپایل ګروپ','butyl':'بیوتایل ګروپ','n-butyl':'(یا «این بیوتایل ګروپ»)','isobutyl':'ایزوبیوتایل ګروپ','sec-butyl':'سیک بیوتایل ګروپ','tert-butyl':'ټرټ بیوتایل ګروپ','t-butyl':'(یا «ټي بیوتایل ګروپ»)','primary':'لومړنی (1°) کاربن','secondary':'دویم‌ډولی (2°) کاربن','tertiary':'درېیم‌ډولی (3°) کاربن','correct':'(سم)','incorrect':'(ناسم)'}
}


def prefixes(kind, language):
    labels=LABELS[language]
    d=Drawing(700,155 if kind!='neo' else 190,'Alkane '+kind+' prefix structural examples')
    if kind=='n':
        d.chain(55,60,['CH₃','CH₂','CH₂','CH₃'])
        d.chain(390,60,['CH₃','CH₂','CH₂','CH₂','CH₃'])
        names=['n-butane','n-pentane']; ys=100
    elif kind=='iso':
        d.chain(65,85,['CH₃','CH','CH₃'],top={1:'CH₃'})
        d.chain(390,85,['CH₃','CH','CH₂','CH₃'],top={1:'CH₃'})
        names=['isobutane','isopentane'];ys=120
    else:
        d.chain(65,85,['CH₃','C','CH₃'],top={1:'CH₃'},bottom={1:'CH₃'})
        d.chain(390,85,['CH₃','C','CH₂','CH₃'],top={1:'CH₃'},bottom={1:'CH₃'})
        names=['neopentane','neohexane'];ys=170
    d.text(155,ys,labels[names[0]],17);d.text(500,ys,labels[names[1]],17)
    return d.done()


def alkyl_groups(language):
    l=LABELS[language];d=Drawing(1040,430,'Eight alkyl groups: one, two, three and four carbons')
    for x,w in [(15,150),(165,205),(370,655)]:d.box(x,8,w,162)
    d.text(90,32,l['one'],16);d.text(267,32,l['two'],16);d.text(696,32,l['three'],16)
    d.chain(80,91,['CH₃'],terminal=True);d.text(90,126,l['methyl'],16)
    d.chain(225,91,['CH₃','CH₂'],terminal=True);d.text(267,126,l['ethyl'],16)
    d.chain(420,91,['CH₃','CH₂','CH₂'],terminal=True);d.text(485,125,l['propyl'],16);d.text(485,149,l['n-propyl'],15)
    d.chain(810,91,['CH₃','CH'],top={1:'CH₃'},terminal=True);d.text(864,132,l['isopropyl'],16)
    d.box(15,180,1010,242);d.text(520,206,l['four'],17)
    d.chain(50,287,['CH₃','CH₂','CH₂','CH₂'],step=54,terminal=True);d.text(145,325,l['butyl'],16);d.text(145,350,l['n-butyl'],15)
    d.chain(315,287,['CH₃','CH','CH₂'],step=54,top={1:'CH₃'},terminal=True);d.text(375,325,l['isobutyl'],16)
    d.chain(570,287,['CH₃','CH₂','CH'],step=54,top={2:'CH₃'},terminal=True);d.text(632,325,l['sec-butyl'],16)
    d.chain(865,287,['CH₃','C'],step=54,top={1:'CH₃'},bottom={1:'CH₃'},terminal=True);d.text(910,369,l['tert-butyl'],16);d.text(910,396,l['t-butyl'],15)
    return d.done()


def carbon_degrees(language):
    l=LABELS[language];d=Drawing(810,185,'Primary, secondary and tertiary carbon atoms')
    for x,top,bottom,name in [(130,'H','H','primary'),(405,'R','H','secondary'),(675,'R','R','tertiary')]:
        d.chain(x-61,86,['R','C'],top={1:top},bottom={1:bottom},terminal=True)
        d.text(x,166,l[name],17)
    return d.done()


def longest_chain(language):
    l=LABELS[language];d=Drawing(920,285,'Correct and incorrect selections of the longest continuous carbon chain')
    d.chain(55,80,['H₃C','CH','CH₂','CH₂','CH₃'],top={1:'CH₃'},step=70)
    d.box(25,59,344,37);d.text(195,124,l['correct'],18,'#166534')
    # The visible source prints “Cl” where a CH2 group would be expected.
    # Preserve this ambiguity for source review instead of silently correcting it.
    d.chain(535,80,['H₃C','CH','CH₂','Cl','CH₃'],top={1:'CH₃'},step=70)
    d.box(570,13,280,83);d.text(710,124,l['correct'],18,'#166534')
    d.chain(310,230,['H₃C','CH','CH₂','CH₂','CH₃'],top={1:'CH₃'},step=70)
    d.box(278,163,133,84);d.text(452,277,l['incorrect'],18,'#991b1b')
    return d.done()


def numbering(language):
    l=LABELS[language];d=Drawing(920,165,'Numbering the parent chain from the end nearest a branch')
    for x, nums, key in [(55,[1,2,3,4,5],'correct'),(535,[5,4,3,2,1],'incorrect')]:
        d.chain(x,90,['H₃C','CH','CH₂','CH₂','CH₃'],top={1:'CH₃'},step=70)
        for i,n in enumerate(nums):d.text(x+i*70,114 if i==1 else 65,str(n),13)
        d.text(x+140,148,l[key],18,'#166534' if key=='correct' else '#991b1b')
    return d.done()


paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def visual(identity, builder):
    blocks.append({'id':identity,'svg':builder('en'),'svgUrdu':builder('ur'),'svgPashto':builder('ps')})
    layout.append({'type':'visual','blockId':identity})

add('i. The prefix n– (from normal) is used for those alkanes in which all the carbon atoms are in one continuous straight chain.',
    'i. سابقہ n– (نارمل سے) ان الکینز کے لیے استعمال ہوتا ہے جن کے تمام کاربن ایٹم ایک مسلسل سیدھی زنجیر میں ہوتے ہیں۔',
    'i. د n– مختاړی (له نارمل څخه) د هغو الکانونو لپاره کارېږي چې ټول کاربني اټومونه یې په یوه پرله‌پسې نېغه ځنځیر کې وي.')
visual('chem12-pdf56-normal-alkanes',lambda lang:prefixes('n',lang))
add('ii. The prefix iso– is used for those alkanes which have a methyl group (CH₃–) attached to the second last carbon atom of the continuous chain.',
    'ii. سابقہ iso– ان الکینز کے لیے استعمال ہوتا ہے جن کی مسلسل زنجیر کے آخری سے دوسرے کاربن ایٹم کے ساتھ ایک میتھائل گروپ (CH₃–) جڑا ہوتا ہے۔',
    'ii. د iso– مختاړی د هغو الکانونو لپاره کارېږي چې د پرله‌پسې ځنځیر له پای څخه له دویم کاربني اټوم سره یې یو میتایل ګروپ (CH₃–) نښتی وي.')
visual('chem12-pdf56-iso-alkanes',lambda lang:prefixes('iso',lang))
add('iii. The prefix neo– is used for those alkanes which have two methyl groups attached to the second last carbon atom of the continuous chain.',
    'iii. سابقہ neo– ان الکینز کے لیے استعمال ہوتا ہے جن کی مسلسل زنجیر کے آخری سے دوسرے کاربن ایٹم کے ساتھ دو میتھائل گروپ جڑے ہوتے ہیں۔',
    'iii. د neo– مختاړی د هغو الکانونو لپاره کارېږي چې د پرله‌پسې ځنځیر له پای څخه له دویم کاربني اټوم سره یې دوه میتایل ګروپونه نښتي وي.')
visual('chem12-pdf56-neo-alkanes',lambda lang:prefixes('neo',lang))
add('Alkyl group (R–)','الکائل گروپ (R–)','الکایل ګروپ (R–)','heading')
add('Alkyl group contain a hydrogen atom less than alkane and represented by R– having general formula CₙH₂ₙ₊₁. The name of alkyl group is derived by replacing the –ane suffix of the corresponding alkane with –yl. Methane becomes methyl (CH₃–); ethane becomes ethyl (CH₃CH₂–) and so on. The dash at the end of the chain represents a potential point of attachment for some other atom or group of atoms. Some of the alkyl groups are shown below.',
    'الکائل گروپ میں الکین کی نسبت ایک ہائیڈروجن ایٹم کم ہوتا ہے اور اسے R– سے ظاہر کیا جاتا ہے؛ اس کا عمومی فارمولا CₙH₂ₙ₊₁ ہے۔ الکائل گروپ کا نام متعلقہ الکین کے لاحقے –ane کو –yl سے بدل کر بنایا جاتا ہے۔ میتھین سے میتھائل (CH₃–)، ایتھین سے ایتھائل (CH₃CH₂–) بنتا ہے، اور اسی طرح آگے۔ زنجیر کے آخر میں ڈیش کسی دوسرے ایٹم یا ایٹموں کے گروپ کے جڑنے کی ممکنہ جگہ ظاہر کرتا ہے۔ بعض الکائل گروپ نیچے دکھائے گئے ہیں۔',
    'په الکایل ګروپ کې د الکان په پرتله یو هایدروجن اټوم کم وي او په R– ښودل کېږي؛ عمومي فورمول یې CₙH₂ₙ₊₁ دی. د الکایل ګروپ نوم د اړوند الکان د –ane وروستاړي پر ځای د –yl په ایښودلو جوړېږي. میتان په میتایل (CH₃–)، ایتان په ایتایل (CH₃CH₂–) بدلېږي او همداسې نور. د ځنځیر په پای کې کرښه د بل اټوم یا د اټومونو د ګروپ د نښلېدو احتمالي ځای ښيي. ځینې الکایل ګروپونه لاندې ښودل شوي دي.')
visual('chem12-pdf56-alkyl-groups',alkyl_groups)
add('The names of the secondary–butyl (sec–butyl) and tertiary–butyl (tert–butyl or t–butyl) groups are based on the degree of alkyl substitution of the carbon atom attached to the main chain. In the sec–butyl group, the carbon atom bonded to the main chain is secondary (2°) or bonded to two other carbon atoms. In the tert–butyl group, it is tertiary (3°) or bonded to three other carbon atoms.',
    'سیکنڈری بیوٹائل (سیک بیوٹائل) اور ٹرشری بیوٹائل (ٹرٹ بیوٹائل یا ٹی بیوٹائل) گروپوں کے نام مرکزی زنجیر سے جڑے کاربن ایٹم کے الکائل متبادلوں کی تعداد پر مبنی ہیں۔ سیک بیوٹائل گروپ میں مرکزی زنجیر سے بند بنانے والا کاربن ایٹم سیکنڈری (2°) ہوتا ہے، یعنی دو دوسرے کاربن ایٹموں سے جڑا ہوتا ہے۔ ٹرٹ بیوٹائل گروپ میں یہ ٹرشری (3°) ہوتا ہے، یعنی تین دوسرے کاربن ایٹموں سے جڑا ہوتا ہے۔',
    'د ثانوي بیوتایل (سیک بیوتایل) او ثالثي بیوتایل (ټرټ بیوتایل یا ټي بیوتایل) ګروپونو نومونه له اصلي ځنځیر سره د نښتي کاربني اټوم د الکایل بدیلونو پر درجې ولاړ دي. په سیک بیوتایل ګروپ کې له اصلي ځنځیر سره تړلی کاربني اټوم دویم‌ډولی (2°) دی، یعنې له دوو نورو کاربني اټومونو سره تړلی دی. په ټرټ بیوتایل ګروپ کې درېیم‌ډولی (3°) دی، یعنې له دریو نورو کاربني اټومونو سره تړلی دی.')
visual('chem12-pdf56-carbon-degrees',carbon_degrees)
add('(b) IUPAC System','(b) آئی یو پیک نظام','(b) د IUPAC سیستم','heading')
add('In this system the parent names of the alkanes are retained such as methane, ethane, propane, butane, pentane, hexane and so on while the branching (if any) is treated as substituent, attached to the main continuous carbon chain.',
    'اس نظام میں الکینز کے اصل نام برقرار رہتے ہیں، مثلاً میتھین، ایتھین، پروپین، بیوٹین، پینٹین، ہیکسین اور اسی طرح آگے؛ جبکہ شاخ (اگر موجود ہو) کو مرکزی مسلسل کاربن زنجیر سے جڑا متبادل سمجھا جاتا ہے۔',
    'په دې سیستم کې د الکانونو اصلي نومونه ساتل کېږي، لکه میتان، ایتان، پروپان، بیوتان، پېنتان، هېکسان او داسې نور؛ خو څانګه (که موجوده وي) له اصلي پرله‌پسې کاربني ځنځیر سره د نښتي بدیل په توګه ګڼل کېږي.')
add('Rules for naming of alkanes:','الکینز کی نام گذاری کے قواعد:','د الکانونو د نومولو قواعد:','heading')
add('1. Find the longest continuous chain of carbon atoms and use this chain as the base name or parent or stem name.',
    '1. کاربن ایٹموں کی سب سے لمبی مسلسل زنجیر تلاش کریں اور اس زنجیر کو بنیادی نام یا اصل نام یا جڑ کے نام کے طور پر استعمال کریں۔',
    '1. د کاربني اټومونو تر ټولو اوږد پرله‌پسې ځنځیر ومومئ او دا ځنځیر د بنسټیز نوم، اصلي نوم یا ریښې نوم په توګه وکاروئ.')
visual('chem12-pdf56-longest-chain',longest_chain)
add('2. Number the longest chain, beginning with the end nearest a branch.',
    '2. سب سے لمبی زنجیر کو اس سرے سے نمبر دیں جو کسی شاخ کے سب سے قریب ہو۔',
    '2. تر ټولو اوږد ځنځیر له هغه پای څخه شمېرې کړئ چې څانګې ته تر ټولو نږدې وي.')
visual('chem12-pdf56-numbering',numbering)

record=section('16.3','Alkane nomenclature and alkyl groups','الکینز کی نام گذاری اور الکائل گروپ','د الکانونو نومول او الکایل ګروپونه',paras,layout,blocks,'104–105')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':56,'printedPages':[104,105]}]
record['sourceContinuesOnPdfPage']=57
issues=[{'id':'chem12-p105-longest-chain-printing','printedPage':105,'description':'The second longest-chain diagram labelled correct visibly shows Cl at the fourth horizontal group, where CH₂ would be chemically expected. The SVG retains the visible Cl; final source review must resolve whether the scan lost H₂ or the book printed an error. No silent chemical correction was applied.'},
        {'id':'chem12-p105-butyl-degree-wording','printedPage':105,'description':'The source counts carbon neighbours within the alkyl group when defining sec-/tert-butyl attachment carbons. Its wording about a carbon already bonded to the main chain is retained verbatim; no explanatory source correction was substituted.'}]
trim=[{'id':'16.4','startsAt':'3. Name the substituents on the longest chain'}]

if __name__=='__main__':
    from class12_chemistry_sync import save
    save(56,[record],trim=trim,issues=issues,chapter_number=16)
