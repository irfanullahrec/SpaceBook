"""PDF63 (printed118–119): independent source builder; no shared mutations."""
import html
from class12_chemistry_opening import pair, section, SOURCE

paras, layout, blocks = [], [], []


def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))


def text(x,y,value,size=19,fill='#1b2430'):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" fill="{fill}">{html.escape(value)}</text>'


def line(x1,y1,x2,y2,width=1.8,color='#1b2430',dash=False):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="4 3"' if dash else '')+'/>'


def atom(x,y,label='C',size=21):
    return f'<rect x="{x-11}" y="{y-16}" width="22" height="22" fill="white"/>'+text(x,y,label,size)


def arrow(x,y,length=92,label='',under=''):
    out=line(x,y,x+length,y,1.8,'#9e2346')+f'<path d="M{x+length-8} {y-4}L{x+length} {y}L{x+length-8} {y+4}Z" fill="#9e2346"/>'
    if label:out+=text(x+length/2,y-12,label,16)
    if under:out+=text(x+length/2,y+24,under,16)
    return out


def visual(identity,body,height,labels=None,equations=None):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {height}" role="img"><g font-family="Arial,sans-serif">'+body+'</g></svg>'
    b={'id':identity,'svg':svg,'svgUrdu':svg,'svgPashto':svg}
    for f,n in [('svgUrdu',0),('svgPashto',1)]:
        for source,translations in (labels or {}).items():
            b[f]=b[f].replace('>'+html.escape(source)+'</text>','>'+html.escape(translations[n])+'</text>')
    if equations:b['sourceEquations']=equations
    blocks.append(b);layout.append({'type':'visual','blockId':identity})


add('Let us consider buta-1,3-diene to illustrate the phenomenon of conjugation. All the four carbon atoms in buta-1,3-diene are sp²-hybridized. The C–C and C–H sigma bonds are the result of the overlap of sp²-hybrid orbitals with each other and with 1s orbitals of the hydrogen atoms respectively. All the carbon and hydrogen atoms lie in the same plane. Additionally, each of the four carbon atom also possess an unhybridized p orbital, which are perpendicular to the plane of sigma bonds. These four p orbitals overlap to form delocalized pi molecular orbitals (Figure.16.4). These delocalized pi electrons are thus attracted by all four carbon atoms. The delocalization of pi electrons is responsible for greater stability of buta-1,3-diene. As a consequence of conjugation, the C–C single bond in buta-1,3-diene is 148 pm (1.48 Å) which is shorter than the normal C–C single bonds (154 pm) of alkane while the C–C double bond are 137 pm (1.37 Å) which are longer than normal isolated C–C double bonds (134 pm).',
    'آئیے اشتراک کے مظہر کی وضاحت کے لیے بیوٹا-1،3-ڈائین کو دیکھیں۔ بیوٹا-1،3-ڈائین کے چاروں کاربن ایٹم sp² ہائبرڈائزڈ ہیں۔ C–C اور C–H سگما بند بالترتیب sp² ہائبرڈ آربیٹلوں کے ایک دوسرے کے ساتھ اور ہائیڈروجن ایٹموں کے 1s آربیٹلوں کے ساتھ باہمی تداخل سے بنتے ہیں۔ تمام کاربن اور ہائیڈروجن ایٹم ایک ہی سطح میں ہوتے ہیں۔ مزید یہ کہ چاروں کاربن ایٹموں میں سے ہر ایک کا ایک غیر ہائبرڈائزڈ p آربیٹل بھی ہوتا ہے، جو سگما بندوں کی سطح پر عموداً ہوتا ہے۔ یہ چار p آربیٹل باہم متداخل ہو کر غیر مقامی پائی سالماتی آربیٹل بناتے ہیں (شکل16.4)۔ اس لیے یہ غیر مقامی پائی الیکٹران چاروں کاربن ایٹموں کی طرف کشش رکھتے ہیں۔ پائی الیکٹرانوں کا غیر مقامی ہونا بیوٹا-1،3-ڈائین کے زیادہ استحکام کا سبب ہے۔ اشتراک کے نتیجے میں بیوٹا-1،3-ڈائین کا C–C یک بند 148 pm (1.48 Å) ہوتا ہے، جو الکین کے عام C–C یک بندوں (154 pm) سے چھوٹا ہے، جبکہ C–C دوہرے بند 137 pm (1.37 Å) ہوتے ہیں، جو عام الگ تھلگ C–C دوہرے بندوں (134 pm) سے لمبے ہیں۔',
    'راځئ د کونجوګېشن د پدیدې د روښانه کولو لپاره بیوټا-1،3-ډایین په پام کې ونیسو. په بیوټا-1،3-ډایین کې ټول څلور کاربني اټومونه sp² هایبرډ شوي دي. د C–C او C–H سیګما تړونونه په ترتیب سره د sp² هایبرډ اوربیټالونو د یو بل سره او د هایدروجن اټومونو د 1s اوربیټالونو سره د پوښښ پایله دي. ټول کاربني او هایدروجني اټومونه په یوه سطحه کې پراته دي. سربېره پر دې، له څلورو کاربني اټومونو څخه هر یو یو ناهیبرډ شوی p اوربیټال هم لري چې د سیګما تړونونو پر سطحه عمودي دی. دا څلور p اوربیټالونه سره پوښښ کوي او غیرموضعي پای مالیکولي اوربیټالونه جوړوي (شکل16.4). نو دا غیرموضعي پای الکترونونه د ټولو څلورو کاربني اټومونو له خوا راکاږل کېږي. د پای الکترونونو غیرموضعي کېدل د بیوټا-1،3-ډایین د ډېر ثبات لامل دی. د کونجوګېشن په پایله کې په بیوټا-1،3-ډایین کې د C–C یوګونی تړون 148 pm (1.48 Å) دی، چې د الکان له عادي C–C یوګونو تړونونو (154 pm) څخه لنډ دی، حال دا چې د C–C دوه ګوني تړونونه 137 pm (1.37 Å) دي، چې له عادي جلا C–C دوه ګونو تړونونو (134 pm) څخه اوږده دي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('When the double bonds in a diene are separated from each other by two or more single bonds, they are called isolated double bonds. Adjacent double bonds in a diene are referred as comulated double bonds.',
    'جب کسی ڈائین میں دوہرے بند ایک دوسرے سے دو یا زیادہ یک بندوں کے ذریعے جدا ہوں تو انہیں الگ تھلگ دوہرے بند کہتے ہیں۔ ڈائین میں متصل دوہرے بندوں کو جمع شدہ دوہرے بند کہا جاتا ہے۔',
    'کله چې په یوه ډایین کې دوه ګوني تړونونه له یو بل څخه په دوو یا ډېرو یوګونو تړونونو جلا وي، هغوی جلا دوه ګوني تړونونه بلل کېږي. په ډایین کې څنګ په څنګ دوه ګوني تړونونه د راټولو شوو دوه ګونو تړونونو په نوم یادېږي.')


def conjugated_skeleton(points,orbital=False):
    out=''
    for i,((x,y),(xx,yy)) in enumerate(zip(points,points[1:])):
        out+=line(x,y,xx,yy)
        if not orbital and i in (0,2):out+=line(x,y-7,xx,yy-7,1.3)
    # Terminal carbons have two H atoms, internal carbons have one H each.
    hs=[[(points[0][0]-35,points[0][1]-18),(points[0][0],points[0][1]+38)],
        [(points[1][0],points[1][1]-38)],[(points[2][0],points[2][1]+38)],
        [(points[3][0],points[3][1]-38),(points[3][0]+35,points[3][1]+18)]]
    for i,((x,y),hydrogens) in enumerate(zip(points,hs)):
        for hx,hy in hydrogens:
            out+=line(x,y,hx,hy)+atom(hx,hy+5,'H',17)
        out+=atom(x,y+5,'C',19)+text(x+13,y+12,str(i+1),11,'#9e2346')
    return out


left=[(90,204),(160,168),(230,204),(300,168)]
body=conjugated_skeleton(left)
body+=text(106,132,'1.37 Å',16,'#125764')+text(194,259,'1.48 Å',16,'#125764')+text(289,246,'1.37 Å',16,'#125764')
body+=text(245,48,'partial double',17,'#922233')+text(245,68,'bond',17,'#922233')+line(245,77,197,183,1.4)
# Four p orbitals, with opposite phases above/below the sigma-bond plane.
right=[(510,195),(575,159),(650,195),(715,159)]
for x,y in right:
    for sign,color in [(-1,'#087caa'),(1,'#72a000')]:
        a,b,c = y+sign*45,y+sign*76,y+sign*96
        body+=f'<path d="M{x} {y}Q{x-60} {a} {x-38} {b}Q{x} {c} {x+38} {b}Q{x+60} {a} {x} {y}Z" fill="{color}" fill-opacity="0.8" stroke="{color}" stroke-width="1"/>'
    body+=line(x,y-85,x,y+85,0.8,'#425d69',True)
body+=conjugated_skeleton(right,True)
body+=text(659,29,'small amount',17,'#922233')+text(659,49,'of overlap',17,'#922233')+line(659,57,616,121,1.4)
labels={'partial double':('جزوی دوہرا','جزوي دوه ګونی'),'bond':('بند','تړون'),'small amount':('تداخل کی کم','د پوښښ لږه'),'of overlap':('مقدار','اندازه')}
visual('chem12-figure16-4',body,330,labels)
add('Figure 16.4 Overlap of four p orbitals in buta-1,3-diene.',
    'شکل16.4 بیوٹا-1،3-ڈائین میں چار p آربیٹلوں کا باہمی تداخل۔',
    'شکل16.4 په بیوټا-1،3-ډایین کې د څلورو p اوربیټالونو پوښښ.')
add('16.5.4 Relative Stability of Alkenes','16.5.4 الکینز کا نسبتی استحکام','16.5.4 د الکینونو نسبي ثبات','heading')
add('Various alkenes have different stability which depends upon the position of the double bond in the molecule and the number, nature and relative position of substituents on double bonded carbon atoms. In general, the greater the number of alkyl groups attached to the double bonded carbons, the greater is the stability of alkene. For geometric isomers of an alkene, trans-isomer is always more stable than cis-isomers (Section 16.6.2.1). For isomeric dienes, conjugated dienes are more stable than non-conjugated.',
    'مختلف الکینز کا استحکام مختلف ہوتا ہے، جو سالمے میں دوہرے بند کی جگہ اور دوہرے بند والے کاربن ایٹموں پر متبادل گروہوں کی تعداد، نوعیت اور نسبتی جگہ پر منحصر ہے۔ عموماً دوہرے بند والے کاربنوں سے جڑے الکائل گروہوں کی تعداد جتنی زیادہ ہو، الکین کا استحکام اتنا زیادہ ہوتا ہے۔ کسی الکین کے ہندسی آئسومروں میں ٹرانس آئسومر ہمیشہ سِس آئسومروں سے زیادہ مستحکم ہوتا ہے (حصہ16.6.2.1)۔ آئسومری ڈائینز میں اشتراکی ڈائینز غیر اشتراکی ڈائینز سے زیادہ مستحکم ہوتے ہیں۔',
    'بېلابېل الکینونه بېلابېل ثبات لري چې په مالیکول کې د دوه ګوني تړون پر موقعیت او د دوه ګوني تړون لرونکو کاربني اټومونو د ځایناستو پر شمېر، طبیعت او نسبي موقعیت پورې تړلی دی. په عمومي ډول، د دوه ګوني تړون له کاربنونو سره د تړلو الکایل ګروپونو شمېر چې څومره ډېر وي، د الکین ثبات همغومره ډېر وي. د یوه الکین په هندسي ایزومرونو کې ټرانس ایزومر تل له سیس ایزومرونو ډېر ثابت وي (برخه16.6.2.1). د ایزومري ډایینونو لپاره، کونجوګېټ شوي ډایینونه له ناکونجوګېټ شوو څخه ډېر ثابت دي.')
add('Measurement and comparison of the heats of hydrogenation or heats of combustion of different isomeric alkenes, give us a clue about the relative stability of these alkenes. Stable alkenes evolve small amount of heat upon combustion and hydrogenation and vice versa.',
    'مختلف آئسومری الکینز کی حرارت ہائیڈروجنیشن یا حرارت احتراق کی پیمائش اور موازنہ ہمیں ان الکینز کے نسبتی استحکام کا اشارہ دیتے ہیں۔ مستحکم الکینز احتراق اور ہائیڈروجنیشن پر کم حرارت خارج کرتے ہیں اور اس کے برعکس بھی درست ہے۔',
    'د بېلابېلو ایزومري الکینونو د هایدروجنېشن یا د سوځېدو د تودوخې اندازه کول او پرتله کول موږ ته د دې الکینونو د نسبي ثبات په اړه نښه راکوي. ثابت الکینونه د سوځېدو او هایدروجنېشن پر مهال لږه تودوخه خوشې کوي او برعکس هم همداسې ده.')
add('Consider the heats of combustion of the four isomeric butylenes of molecular formula C₄H₈, as given below. Comparison of the heats of combustion of butylenes shows that but-1-ene evolves the largest amount of heat on combustion. In other words, but-1-ene possess the highest energy and is thus the least stable of the four butylenes. Similarly isobutylene (2-methylpropene) has lowest value of enthalpy of combustion, and the most stable of the four isomers.',
    'سالماتی فارمولے C₄H₈ والے چار آئسومری بیوٹیلینز کی حرارت احتراق کو دیکھیں، جو نیچے دی گئی ہے۔ بیوٹیلینز کی حرارت احتراق کا موازنہ ظاہر کرتا ہے کہ بیوٹ-1-این احتراق پر سب سے زیادہ حرارت خارج کرتا ہے۔ دوسرے لفظوں میں بیوٹ-1-این کی توانائی سب سے زیادہ ہے، اس لیے چاروں بیوٹیلینز میں یہ سب سے کم مستحکم ہے۔ اسی طرح آئسوبیوٹیلین (2-میتھائل پروپین، دوہرے بند والا) کی اینتھالپی احتراق سب سے کم ہے اور یہ چاروں آئسومروں میں سب سے زیادہ مستحکم ہے۔',
    'د C₄H₈ مالیکولي فورمول لرونکو څلورو ایزومري بیوټیلینونو د سوځېدو تودوخې په پام کې ونیسئ، لکه لاندې چې ورکړل شوې دي. د بیوټیلینونو د سوځېدو د تودوخې پرتله ښيي چې بیوټ-1-این د سوځېدو پر مهال تر ټولو ډېره تودوخه خوشې کوي. په بل عبارت، بیوټ-1-این تر ټولو لوړه انرژي لري، نو د څلورو بیوټیلینونو تر منځ تر ټولو لږ ثابت دی. همدارنګه ایزوبیوټیلین (2-میتیل پروپین) د سوځېدو د انتالپي تر ټولو ټیټ ارزښت لري او د څلورو ایزومرونو تر منځ تر ټولو ثابت دی.')


def alkene(x,y,lt,lb,rt,rb):
    # Explicit substituent geometry preserves the printed cis/trans distinction.
    body=line(x+10,y-8,x+65,y-8)+line(x+10,y-2,x+65,y-2)
    for cx,dx,up,down in [(x,-37,lt,lb),(x+76,37,rt,rb)]:
        body+=line(cx,y-5,cx+dx,y-44)+line(cx,y-5,cx+dx,y+34)
        body+=text(cx+dx,y-49,up,20)+text(cx+dx,y+51,down,20)+atom(cx,y,'C')
    return body


names={'but-1-ene':('بیوٹ-1-این','بیوټ-1-این'),'cis-but-2-ene':('سِس-بیوٹ-2-این','سیس-بیوټ-2-این'),
       'trans-but-2-ene':('ٹرانس-بیوٹ-2-این','ټرانس-بیوټ-2-این'),'Isobutylene':('آئسوبیوٹیلین','ایزوبیوټیلین'),
       '(2-methylpropene)':('(2-میتھائل پروپین)','(2-میتیل پروپین)'),
       'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'ethene':('ایتھین','ایتین')}
body=text(175,44,'CH₃ – CH₂ – CH = CH₂',21)+text(175,75,'but-1-ene',18)
body+=text(355,44,'+ 6O₂',21)+arrow(425,38)+text(709,44,'4CO₂ + 4H₂O + 2719 kJ/mol',21)
for y,lt,lb,rt,rb,name,heat in [(179,'CH₃','H','CH₃','H','cis-but-2-ene','2712'),(359,'CH₃','H','H','CH₃','trans-but-2-ene','2707'),(539,'H','H','CH₃','CH₃','Isobutylene','2703')]:
    body+=alkene(140,y,lt,lb,rt,rb)+text(178,y+82,name,18)
    if name=='Isobutylene':body+=text(178,y+106,'(2-methylpropene)',18)
    body+=text(355,y,'+ 6O₂',21)+arrow(425,y-6)+text(709,y,f'4CO₂ + 4H₂O + {heat} kJ/mol',21)
eqs=['CH₃–CH₂–CH=CH₂ + 6O₂ → 4CO₂ + 4H₂O + 2719 kJ/mol',
     'cis-CH₃–CH=CH–CH₃ + 6O₂ → 4CO₂ + 4H₂O + 2712 kJ/mol',
     'trans-CH₃–CH=CH–CH₃ + 6O₂ → 4CO₂ + 4H₂O + 2707 kJ/mol',
     'CH₂=C(CH₃)₂ + 6O₂ → 4CO₂ + 4H₂O + 2703 kJ/mol']
visual('chem12-p119-combustion-isomers',body,675,names,eqs)
add('16.5.5 Preparation of Alkenes','16.5.5 الکینز کی تیاری','16.5.5 د الکینونو جوړول','heading')
add('Alkenes can be prepared by the following methods.',
    'الکینز درج ذیل طریقوں سے تیار کیے جا سکتے ہیں۔',
    'الکینونه په لاندې طریقو جوړېدای شي.')
add('16.5.5.1 Dehydration of Alcohols','16.5.5.1 الکوحلوں کی آب ربائی','16.5.5.1 له الکولونو د اوبو ایستل','heading')
add('When an alcohol is heated at 170°C, in the presence of sulfuric acid, a water molecule is eliminated, resulting in the formation of an alkene.',
    'جب کسی الکوحل کو سلفیورک تیزاب کی موجودگی میں 170°C پر گرم کیا جاتا ہے تو پانی کا ایک سالمہ نکل جاتا ہے اور نتیجتاً ایک الکین بنتا ہے۔',
    'کله چې یو الکول د سلفوریک اسید په شتون کې په 170°C تودوخه ګرم شي، د اوبو یو مالیکول ترې ایستل کېږي او په پایله کې یو الکین جوړېږي.')
body=line(165,85,235,85)
for x,top in [(165,'H'),(235,'OH')]:
    body+=line(x,85,x,41)+line(x,85,x,128)+text(x,32,top,21)+text(x,151,'H',21)+atom(x,91)
body+=line(110,85,165,85)+text(95,91,'H',21)+line(235,85,290,85)+text(305,91,'H',21)+text(200,185,'ethyl alcohol',19)
body+=arrow(377,85,115,'H₂SO₄','170°C')+alkene(585,91,'H','H','H','H')+text(625,185,'ethene',19)+text(780,91,'+ H₂O',23)
visual('chem12-p119-alcohol-dehydration',body,215,names,['CH₃CH₂OH → CH₂=CH₂ + H₂O (H₂SO₄,170°C)'])

record=section('16.10','Conjugation, stability and preparation of alkenes',
               'الکینز کا اشتراک، استحکام اور تیاری','د الکینونو کونجوګېشن، ثبات او جوړول',paras,layout,blocks,'118–119')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':63,'printedPages':[118,119]}]
record['sourceChapterNumber']=16
record['sourceContinuesOnPdfPage']=64
issues=[
    {'id':'chem12-p118-comulated-typo','pdfPage':63,'printedPage':118,'description':'The Tidbit prints “comulated double bonds”; this spelling is retained in English, with the intended cumulated sense translated.','status':'source_printed_typo_retained'},
    {'id':'chem12-p118-trans-always','pdfPage':63,'printedPage':118,'description':'The source says a trans-isomer is “always” more stable than cis-isomers. This categorical statement is retained; its scope needs scientific review.','status':'source_statement_retained_pending_review'}]

# Integration must carry16.10→16.11 from this exact prefix BEFORE replacement:
# "Industrially dehydration of alcohol is carried out by passing vapours of alcohol over"
# That text begins PDF64; the preparation heading and first dehydration diagram
# belong to PDF63 and are implemented above. No save() runs from this module.
