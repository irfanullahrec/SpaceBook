"""PDF57, printed106–107. Standalone record; root owns integration/checkpoint."""
import html
import math
from class12_chemistry_opening import pair, section, SOURCE

paras, layout, blocks = [], [], []


def add(e, u, p, kind='paragraph'):
    layout.append({'type': kind, 'indices': [len(paras)]})
    paras.append(pair(e, u, p))


def text(x, y, value, size=19, fill='#17212b'):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" fill="{fill}">{html.escape(value)}</text>'


def line(x1, y1, x2, y2, color='#17212b', width=1.8):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>'


def atom(x, y, label):
    return f'<rect x="{x-23}" y="{y-16}" width="46" height="23" fill="white"/>' + text(x, y, label)


def chain(x, y, groups, branches=None, numbers=True, reverse=False):
    branches = branches or {}
    result = ''.join(line(x+76*i+22, y-6, x+76*(i+1)-22, y-6) for i in range(len(groups)-1))
    for i, label in enumerate(groups):
        xx = x+76*i
        if i in branches:
            result += line(xx, y-18, xx, y-50) + atom(xx, y-57, branches[i])
        result += atom(xx, y, label)
        if numbers:
            number = len(groups)-i if reverse else i+1
            result += text(xx-9, y-23, str(number), 12)
    return result


def polygon(cx, cy, n, radius=48, full=False, rotation=0):
    points = [(cx+radius*math.sin(rotation+i*2*math.pi/n), cy-radius*math.cos(rotation+i*2*math.pi/n)) for i in range(n)]
    result = '<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+'" fill="none" stroke="#17212b" stroke-width="1.8"/>'
    if full:
        for x,y in points:
            result += f'<rect x="{x-19}" y="{y-12}" width="38" height="22" fill="white"/>'+text(x,y+6,'CH₂')
    return result, points


def visual(identity, body, height, labels=None):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 {height}" role="img"><g font-family="Arial,sans-serif">'+body+'</g></svg>'
    block = {'id': identity, 'svg': svg, 'svgUrdu': svg, 'svgPashto': svg}
    for field, n in [('svgUrdu', 0), ('svgPashto', 1)]:
        for source, translations in (labels or {}).items():
            block[field] = block[field].replace('>'+html.escape(source)+'</text>', '>'+html.escape(translations[n])+'</text>')
    blocks.append(block)
    layout.append({'type': 'visual', 'blockId': identity})


names = {
    '2-methylpentane': ('2-میتھائل پینٹین', '2-میتیل پینټان'),
    '3-ethyl-2-methylpentane': ('3-ایتھائل-2-میتھائل پینٹین', '3-ایتیل-2-میتیل پینټان'),
    '2,3-dimethylpentane': ('2،3-ڈائی میتھائل پینٹین', '2،3-ډای میتیل پینټان'),
    '3-isopropylpentane': ('3-آئسوپروپائل پینٹین', '3-ایزوپروپیل پینټان'),
    '(incorrect)': ('(غلط)', '(ناسم)'), '(correct)': ('(درست)', '(سم)'),
    '2,4-dimethylpentane': ('2،4-ڈائی میتھائل پینٹین', '2،4-ډای میتیل پینټان'),
    '2,3,4-trimethylpentane': ('2،3،4-ٹرائی میتھائل پینٹین', '2،3،4-ټرای میتیل پینټان'),
    'cyclopropane': ('سائیکلوپروپین', 'سایکلوپروپان'),
    'cyclobutane': ('سائیکلوبیوٹین', 'سایکلوبیوټان'),
    'cyclopentane': ('سائیکلوپینٹین', 'سایکلوپینټان'),
    'cyclohexane': ('سائیکلوہیکسین', 'سایکلوهېکسان'),
    'methylcyclopentane': ('میتھائل سائیکلوپینٹین', 'میتیل سایکلوپینټان'),
    'ethylcyclohexane': ('ایتھائل سائیکلوہیکسین', 'ایتیل سایکلوهېکسان'),
    '1,2-dimethylcyclohexane': ('1،2-ڈائی میتھائل سائیکلوہیکسین', '1،2-ډای میتیل سایکلوهېکسان'),
    '1-ethyl-3-methylcyclohexane': ('1-ایتھائل-3-میتھائل سائیکلوہیکسین', '1-ایتیل-3-میتیل سایکلوهېکسان'),
    '3-cyclopropylpentane': ('3-سائیکلوپروپائل پینٹین', '3-سایکلوپروپیل پینټان'),
    '2-cyclopropyl-3-methylbutane': ('2-سائیکلوپروپائل-3-میتھائل بیوٹین', '2-سایکلوپروپیل-3-میتیل بیوټان'),
    'or': ('یا', 'یا'),
}

add('3. Name the substituents on the longest chain (as alkyl groups), before the stem name. Give the location of each substituent by the number of the main chain carbon atom to which it is attached.',
    '3. طویل ترین زنجیر پر موجود متبادل گروہوں کے نام (الکائل گروہوں کے طور پر) بنیادی نام سے پہلے لکھیں۔ ہر متبادل گروہ کی جگہ مرکزی زنجیر کے اس کاربن ایٹم کے نمبر سے بتائیں جس سے وہ جڑا ہے۔',
    '3. په تر ټولو اوږده ځنځیر کې د ځایناستو نومونه (د الکایل ګروپونو په توګه) له بنسټیز نوم مخکې ولیکئ. د هر ځایناستي موقعیت د اصلي ځنځیر د هغه کاربني اټوم په شمېره وښيئ چې ورسره تړلی دی.')
visual('chem12-p106-rule3', chain(230, 95, ['H₃C', 'CH', 'CH₂', 'CH₂', 'CH₃'], {1:'CH₃'})+text(390, 138, '2-methylpentane'), 165, names)
add('Tidbit', 'مختصر معلومات', 'لنډ معلومات', 'heading')
add('Except carboxylic acids and its some derivatives, the names of all other organic compounds are written as single word without any space.',
    'کاربوکسلک تیزابوں اور ان کے بعض مشتقات کے سوا، دیگر تمام نامیاتی مرکبات کے نام کسی فاصلے کے بغیر ایک ہی لفظ کے طور پر لکھے جاتے ہیں۔',
    'له کاربوکسیلیک اسیدونو او د هغوی له ځینو مشتقاتو پرته، د ټولو نورو عضوي مرکباتو نومونه له تشې پرته د یوه ټکي په توګه لیکل کېږي.')
add('4. When two or more different substituents are present, list them in alphabetical order.',
    '4. جب دو یا زیادہ مختلف متبادل گروہ موجود ہوں تو انہیں حروف تہجی کی ترتیب سے لکھیں۔',
    '4. کله چې دوه یا ډېر بېلابېل ځایناستي موجود وي، هغوی په الفبايي ترتیب ولیکئ.')
visual('chem12-p106-rule4', chain(230,95,['H₃C','CH','CH','CH₂','CH₃'],{1:'CH₃',2:'C₂H₅'})+text(390,138,'3-ethyl-2-methylpentane'),165,names)
add('5. When two or more of the same alkyl substituent are present, use the prefixes di–, tri–, tetra–, and so on (ignored in alphabetizing).',
    '5. جب ایک ہی الکائل متبادل گروہ دو یا زیادہ بار موجود ہو تو سابقے ڈائی–، ٹرائی–، ٹیٹرا– وغیرہ استعمال کریں (حروف تہجی کی ترتیب میں ان کو شمار نہیں کیا جاتا)۔',
    '5. کله چې یو ډول الکایل ځایناستی دوه یا ډېر ځله موجود وي، د ډای–، ټرای–، ټېټرا– او نورو مختاړو څخه کار واخلئ (په الفبايي ترتیب کې نه شمېرل کېږي).')
visual('chem12-p106-rule5', chain(230,95,['H₃C','CH','CH','CH₂','CH₃'],{1:'CH₃',2:'CH₃'})+text(390,138,'2,3-dimethylpentane'),165,names)
add('6. When there are more than one longest chains, select the chain which carries more substituents.',
    '6. جب ایک سے زیادہ طویل ترین زنجیریں موجود ہوں تو وہ زنجیر منتخب کریں جس پر زیادہ متبادل گروہ ہوں۔',
    '6. کله چې له یوه څخه ډېر تر ټولو اوږده ځنځیرونه موجود وي، هغه ځنځیر غوره کړئ چې ډېر ځایناستي لري.')


def choice_diagram(dx, correct):
    # Same seven-node carbon skeleton; blue outline selects each printed parent chain.
    body = chain(dx+48,130,['H₃C','CH₂','CH','CH₂','CH₃'],numbers=False)
    body += chain(dx+124,70,['H₃C','CH','CH₃'],numbers=False)
    body += line(dx+200,78,dx+200,111)
    if correct:
        body += f'<path d="M{dx+178} 41H{dx+303}V105H{dx+377}V151H{dx+178}Z" fill="none" stroke="#438a91" stroke-width="1.5"/>'
        for xx,yy,number in [(276,48,1),(200,48,2),(200,108,3),(276,108,4),(352,108,5)]:
            body += text(dx+xx-9,yy,str(number),12)
        body += text(dx+200,178,'3-ethyl-2-methylpentane',17)+text(dx+200,205,'(correct)',17,'#297b38')
    else:
        body += f'<rect x="{dx+18}" y="103" width="360" height="48" fill="none" stroke="#438a91" stroke-width="1.5"/>'
        for i in range(5): body += text(dx+48+76*i-9,108,str(i+1),12)
        body += text(dx+200,178,'3-isopropylpentane',17)+text(dx+200,205,'(incorrect)',17,'#a43826')
    return body


visual('chem12-p106-rule6', choice_diagram(0,False)+choice_diagram(385,True),235,names)
add('Other examples', 'دیگر مثالیں', 'نورې بېلګې', 'heading')
visual('chem12-p106-other-examples',chain(48,95,['H₃C','CH','CH₂','CH','CH₃'],{1:'CH₃',3:'CH₃'})+text(200,140,'2,4-dimethylpentane',17)+chain(428,95,['H₃C','CH','CH','CH','CH₃'],{1:'CH₃',2:'CH₃',3:'CH₃'},reverse=True)+text(580,140,'2,3,4-trimethylpentane',17),175,names)
add('16.2.1.2 Nomenclature of Cycloalkanes', '16.2.1.2 سائیکلوالکینز کی نام گذاری', '16.2.1.2 د سایکلوالکانونو نومول', 'heading')
add('Cycloalkanes are alkanes that contain a ring of three or more carbons. Cycloalkanes are named by placing the prefix “cyclo–” to the name of alkane having the same number of carbon atoms as in the ring. For convenience, cycloalkanes are represented by geometric figures e.g. cyclopropane is represented by a triangle, cyclobutane by a square, cyclopentane by a pentagon, cyclohexane by a hexagon and so on. Each corner of these geometric figures represent a –CH₂– group.',
    'سائیکلوالکینز ایسے الکینز ہیں جن میں تین یا زیادہ کاربن ایٹموں کا حلقہ ہوتا ہے۔ سائیکلوالکینز کا نام اس الکین کے نام سے پہلے سابقہ ”سائیکلو–“ لگا کر رکھا جاتا ہے جس کے کاربن ایٹموں کی تعداد حلقے کے کاربن ایٹموں کے برابر ہو۔ سہولت کے لیے سائیکلوالکینز کو ہندسی شکلوں سے ظاہر کیا جاتا ہے، مثلاً سائیکلوپروپین کو مثلث، سائیکلوبیوٹین کو مربع، سائیکلوپینٹین کو مخمس، سائیکلوہیکسین کو مسدس وغیرہ سے ظاہر کیا جاتا ہے۔ ان ہندسی شکلوں کا ہر کونہ ایک –CH₂– گروہ ظاہر کرتا ہے۔',
    'سایکلوالکانونه هغه الکانونه دي چې د دریو یا ډېرو کاربني اټومونو کړۍ لري. سایکلوالکانونه د هغه الکان له نوم مخکې د «سایکلو–» مختاړي په ایښودلو نومول کېږي چې د کاربني اټومونو شمېر یې د کړۍ له کاربني اټومونو سره برابر وي. د اسانتیا لپاره سایکلوالکانونه په هندسي شکلونو ښودل کېږي؛ لکه سایکلوپروپان په مثلث، سایکلوبیوټان په مربع، سایکلوپینټان په پنځه ضلعي، سایکلوهېکسان په شپږ ضلعي او داسې نور. د دې هندسي شکلونو هر کونج د –CH₂– ګروپ څرګندوي.')
body = ''
for cx,cy,n,name,rotation in [(115,80,3,'cyclopropane',0),(505,80,4,'cyclobutane',math.pi/4),(115,260,5,'cyclopentane',0),(505,260,6,'cyclohexane',0)]:
    body += polygon(cx,cy,n,65 if n==6 else 50,True,rotation)[0]+text(cx+93,cy+5,'or')+polygon(cx+185,cy,n,40,False,rotation)[0]+text(cx+90,cy+84,name)
visual('chem12-p107-ring-conventions',body,380,names)
add('Monosubstituted cycloalkanes are named as alkylcycloalkanes. For polysubstituted cycloalkanes, the prefixes di–, tri– etc. should be used to represent the number of identical substituents. Their positions are specified by numbering the carbon atoms of the ring in the direction that gives the lowest number to the substituents at the first point of difference.',
    'ایک متبادل گروہ والے سائیکلوالکینز کا نام الکائل سائیکلوالکین رکھا جاتا ہے۔ کئی متبادل گروہوں والے سائیکلوالکینز میں یکساں متبادل گروہوں کی تعداد ظاہر کرنے کے لیے ڈائی–، ٹرائی– وغیرہ سابقے استعمال کیے جانے چاہییں۔ ان کی جگہیں حلقے کے کاربن ایٹموں کو اس سمت میں نمبر دے کر بتائی جاتی ہیں جو اختلاف کے پہلے مقام پر متبادل گروہوں کو سب سے کم نمبر دے۔',
    'یو ځایناستی لرونکي سایکلوالکانونه د الکایل سایکلوالکانونو په نوم نومول کېږي. د څو ځایناستو لرونکو سایکلوالکانونو لپاره باید د ورته ځایناستو د شمېر د ښودلو لپاره ډای–، ټرای– او نور مختاړي وکارول شي. د هغوی موقعیتونه د کړۍ د کاربني اټومونو په داسې لوري شمېرلو سره ټاکل کېږي چې د توپیر په لومړي ځای کې ځایناستو ته تر ټولو ټیټ نمبر ورکړي.')


def substituted(cx,cy,n,subs,numbers=()):
    body, points = polygon(cx,cy,n)
    for i,label in subs.items():
        x,y=points[i]
        angle = i*2*math.pi/n
        ex,ey = x+31*math.sin(angle),y-31*math.cos(angle)
        body += line(x,y,ex,ey)+text(ex+12*math.sin(angle),ey-4,label)
    for i in numbers:
        x,y=points[i]
        body += text(x-8,y-5,str(i+1),12)
    return body


body = substituted(205,115,5,{0:'CH₃'})+text(205,190,'methylcyclopentane',18)
body += substituted(575,115,6,{0:'C₂H₅'})+text(575,190,'ethylcyclohexane',18)
body += substituted(205,330,6,{0:'CH₃',1:'CH₃'},(0,1))+text(205,405,'1,2-dimethylcyclohexane',18)
body += substituted(575,330,6,{0:'C₂H₅',2:'CH₃'},(0,1,2))+text(575,405,'1-ethyl-3-methylcyclohexane',18)
visual('chem12-p107-substituted-rings',body,440,names)
add('When the ring contains fewer carbon atoms than an alkyl group attached to it, the compound is named as an alkane and the ring is treated as a cycloalkyl substituent.',
    'جب حلقے میں اس سے جڑے الکائل گروہ کی نسبت کم کاربن ایٹم ہوں تو مرکب کا نام الکین کے طور پر رکھا جاتا ہے اور حلقے کو سائیکلوالکائل متبادل گروہ سمجھا جاتا ہے۔',
    'کله چې په کړۍ کې د ورسره تړلي الکایل ګروپ په پرتله لږ کاربني اټومونه وي، مرکب د الکان په توګه نومول کېږي او کړۍ د سایکلوالکایل ځایناستي په توګه ګڼل کېږي.')
body = chain(48,130,['CH₃','CH₂','CH','CH₂','CH₃'])
body += polygon(200,51,3,29,rotation=math.pi)[0]+line(200,80,200,110)+text(205,174,'3-cyclopropylpentane',17)
body += chain(466,130,['CH₃','CH','CH','CH₃'],{2:'CH₃'})
body += polygon(542,51,3,29,rotation=math.pi)[0]+line(542,80,542,110)+text(588,174,'2-cyclopropyl-3-methylbutane',17)
visual('chem12-p107-cycloalkyl-substituents',body,205,names)

record = section('16.4', 'Alkane naming rules and nomenclature of cycloalkanes',
                 'الکینز کی نام گذاری کے اصول اور سائیکلوالکینز کی نام گذاری',
                 'د الکانونو د نومولو اصول او د سایکلوالکانونو نومول', paras, layout, blocks, '106–107')
record['sourceReferences'] = [{'sourcePdf':SOURCE,'pdfPage':57,'printedPages':[106,107]}]
record['sourceChapterNumber'] = 16
issues = []

# Integration boundary: original16.4 holds pages56–57 through the paragraph
# before substituted rings. Original16.5 starts with those ring labels and must
# be trimmed at "16.2.2 Physical Properties" once this complete57 record is added.
# There are deliberately no file writes or save() calls in this builder.
