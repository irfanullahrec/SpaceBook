"""PDF86 printed164–165: isopropyl/tert-butyl chloride, IUPAC naming of alkyl halides, structure, physical properties."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow86');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'isopropyl chloride':('آئسوپروپائل کلورائیڈ','ایزوپروپیل کلوراید'),'tert-butyl chloride':('ٹرشری بیوٹائل کلورائیڈ','ټرشري بیوټیل کلوراید'),'chloromethane':('کلورو میتھین','کلورومیتان'),
   'chloroethane':('کلورو ایتھین','کلوروایتان'),'1-chloropropane':('1-کلورو پروپین','1-کلوروپروپان'),'2-chloropropane':('2-کلورو پروپین','2-کلوروپروپان'),'2-chloro-2-methylpropane':('2-کلورو-2-میتھائل پروپین','2-کلورو-2-میتایل پروپان'),
   '4-bromo-5-chloro-2,2-dimethylheptane':('4-برومو-5-کلورو-2،2-ڈائی میتھائل ہیپٹین','4-برومو-5-کلورو-2،2-ډای میتایل هېپټان'),'4-bromo-2-fluoro-2-methylpentane':('4-برومو-2-فلورو-2-میتھائل پینٹین','4-برومو-2-فلورو-2-میتایل پېنټان'),
   'sp³-s overlap':('sp³-s تداخل','sp³-s تداخل'),'sp³-p overlap':('sp³-p تداخل','sp³-p تداخل')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def quat(x,y,top,bot,name,lang,nums=None):
 s=t(x,y-40,top,17)+line(x,y-34,x,y-18)+t(x,y,'H₃C — C — Cl',18)+line(x,y+8,x,y+24)+t(x,y+42,bot,17)+t(x,y+66,lb(lang,name),13)
 if nums:s+=t(x,y-58,nums[0],11)+t(x-58,y-16,nums[1],11)+t(x-8,y-16,nums[2],11)
 return s
def isomers(lang):return F.start(140)+quat(250,70,'CH₃','H','isopropyl chloride',lang)+quat(600,70,'CH₃','CH₃','tert-butyl chloride',lang)+'</svg>'
def examples(lang):
 s=F.start(400)
 for x,(f,n) in zip((140,400),(('CH₃—Cl','chloromethane'),('CH₃—CH₂—Cl','chloroethane'))):s+=t(x,40,f,17)+t(x,62,lb(lang,n),12)
 s+=chain(F,0,40,['CH₃','—','CH₂','—','CH₂','—','Cl'],17,{0:'3',2:'2',4:'1'},center=690)+t(690,62,lb(lang,'1-chloropropane'),12)
 s+=quat(220,150,'CH₃','H','2-chloropropane',lang,('3','1','2'))+quat(560,150,'CH₃','CH₃','2-chloro-2-methylpropane',lang,('3','1','2'))
 s+=chain(F,0,300,['H₃C','—','C','—','CH₂','—','CH','—','CH','—','CH₂','—','CH₃'],16,{0:'1',2:'2',4:'3',6:'4',8:'5',10:'6',12:'7'},{2:'CH₃',6:'Br',8:'Cl'},{2:'CH₃'},center=200)
 s+=t(200,372,lb(lang,'4-bromo-5-chloro-2,2-dimethylheptane'),12)
 s+=chain(F,0,300,['H₃C','—','C','—','CH₂','—','CH','—','CH₃'],16,{0:'1',2:'2',4:'3',6:'4',8:'5'},{2:'F',6:'Br'},{2:'CH₃'},center=620)
 s+=t(620,372,lb(lang,'4-bromo-2-fluoro-2-methylpentane'),12)
 return s+'</svg>'
def methylcl(lang):
 s=F.start(200);cx,cy=230,110
 for (x,y,ang) in ((cx,cy-55,90),(cx-60,cy+25,-20),(cx,cy+60,90)):
  s+=f'<ellipse cx="{(cx+x)/2}" cy="{(cy+y)/2}" rx="28" ry="12" fill="#9e9e9e" opacity=".85" transform="rotate({ang} {(cx+x)/2} {(cy+y)/2})"/>'
  s+=f'<circle cx="{x}" cy="{y}" r="12" fill="white" stroke="#333"/>'+t(x,y+5,'H',13)
 s+=f'<ellipse cx="{cx+40}" cy="{cy}" rx="34" ry="13" fill="#9e9e9e" opacity=".85"/><ellipse cx="{cx+105}" cy="{cy+8}" rx="28" ry="18" fill="none" stroke="#333"/>'+t(cx+80,cy+6,'Cl',14)
 s+=t(cx,cy+5,'C',16)+t(cx+80,cy-70,lb(lang,'sp³-s overlap'),13)+t(cx+120,cy-25,lb(lang,'sp³-p overlap'),13)
 x0,y0=620,110;s+=t(x0,y0-60,'H',16)+line(x0,y0-54,x0,y0-12)+t(x0,y0+5,'C',17)+line(x0+8,y0+4,x0+50,y0+22)+t(x0+62,y0+30,'Cl',16)
 s+=line(x0-8,y0+4,x0-50,y0+20,1.5,'#222','stroke-dasharray="2 3"')+t(x0-60,y0+28,'H',16)+line(x0,y0+10,x0-8,y0+44,4)+t(x0-10,y0+62,'H',16)+t(x0+55,y0-35,'109.5°',14)
 return s+'</svg>'

visual('chem12-p86-position-isomers',isomers)
add('The two alkyl halides, n-propyl chloride and isopropyl chloride, given above are example of position isomers.','اوپر دیے گئے دو الکائل ہیلائیڈز، n-پروپائل کلورائیڈ اور آئسوپروپائل کلورائیڈ، مقامی آئسومرز کی مثال ہیں۔','پورته ورکړل شوي دوه الکایل هالایډونه، n-پروپیل کلوراید او ایزوپروپیل کلوراید، د موقعیتي ایزومرونو بېلګه ده.')
add('(b) IUPAC System','(b) IUPAC نظام','(b) IUPAC سیستم','heading')
add('The systematic (IUPAC) nomenclature treats an alkyl halide as an alkane with a halo–substituent: Fluorine is fluoro–, chlorine is chloro–, bromine is bromo–, and iodine is iodo–. The result is a systematic haloalkane name. The following steps should be followed for naming alkyl halides.',
 'نظامی (IUPAC) نام گذاری الکائل ہیلائیڈ کو ہیلو–متبادل والا الکین (اکیلے بند والا) سمجھتی ہے: فلورین فلورو–، کلورین کلورو–، برومین برومو– اور آئیوڈین آئیوڈو– ہے۔ نتیجہ ایک نظامی ہیلو الکین نام ہوتا ہے۔ الکائل ہیلائیڈز کے نام رکھنے کے لیے درج ذیل مراحل اپنائے جائیں۔',
 'سیستماتیک (IUPAC) نومول الکایل هالایډ د هالو–بدیل لرونکي الکان په توګه ګڼي: فلورین فلورو–، کلورین کلورو–، برومین برومو– او ایوډین ایوډو– دی. پایله یو سیستماتیک هالوالکان نوم دی. د الکایل هالایډونو د نومولو لپاره لاندې ګامونه تعقیب شي.')
steps=[('1. Select the longest continuous chain of carbon atoms, containing the halogen atoms.','1. کاربن ایٹموں کی وہ سب سے لمبی مسلسل زنجیر منتخب کریں جس میں ہیلوجن ایٹم ہوں۔','1. د کاربني اټومونو هغه تر ټولو اوږد پرله پسې ځنځیر وټاکئ چې هالوجني اټومونه لري.'),
 ('2. Number the chain from the end closer to halogen atom. If both alkyl and halogen are present in a molecule then number the chain from the end closer to alkyl group or halogen atom.','2. زنجیر کو ہیلوجن ایٹم کے قریب والے سرے سے نمبر دیں۔ اگر سالمے میں الکائل اور ہیلوجن دونوں ہوں تو زنجیر کو الکائل گروپ یا ہیلوجن ایٹم کے قریب والے سرے سے نمبر دیں۔','2. ځنځیر له هغه پای څخه شمېره کړئ چې هالوجني اټوم ته نږدې وي. که په مالیکول کې الکایل او هالوجن دواړه وي، ځنځیر له هغه پای څخه شمېره کړئ چې الکایل ګروپ یا هالوجني اټوم ته نږدې وي.'),
 ('3. Indicate the position of halogen and alkyl group by suitable locants.','3. ہیلوجن اور الکائل گروپ کا مقام مناسب نشان دہ اعداد سے ظاہر کریں۔','3. د هالوجن او الکایل ګروپ موقعیت په مناسبو ځای ښوونکو شمېرو وښیئ.'),
 ('4. Prefix di, tri, tetra etc. is used to indicate the number of halogen atoms.','4. ہیلوجن ایٹموں کی تعداد ظاہر کرنے کے لیے سابقے di، tri، tetra وغیرہ استعمال ہوتے ہیں۔','4. د هالوجني اټومونو د شمېر د ښودلو لپاره di، tri، tetra او نور مختاړي کارېږي.'),
 ('5. If two different halogen atoms are present in a molecule at same position from the two ends, the one to be assigned the lower locant is that one cited first in alphabetical order. When an alkyl and halogen occupy equivalent positions, again number the chain from the end to give lowest number to one that comes first in alphabetical order.','5. اگر سالمے میں دو مختلف ہیلوجن ایٹم دونوں سروں سے ایک ہی مقام پر ہوں تو کم نشان دہ عدد اس کو دیا جائے جو حروفِ تہجی کی ترتیب میں پہلے آئے۔ جب الکائل اور ہیلوجن مساوی مقامات پر ہوں تو پھر زنجیر کو اس سرے سے نمبر دیں جس سے حروفِ تہجی میں پہلے آنے والے کو سب سے کم نمبر ملے۔','5. که په مالیکول کې دوه بېل هالوجني اټومونه له دواړو پایونو په یوه موقعیت کې وي، ټیټه ځای ښوونکې شمېره هغه ته ورکول کېږي چې د الفبا په ترتیب لومړی راځي. کله چې الکایل او هالوجن معادل موقعیتونه ولري، بیا هم ځنځیر له هغه پای څخه شمېره کړئ چې د الفبا په ترتیب لومړي ته تر ټولو ټیټه شمېره ورکړي.')]
s0=len(paras)
for r in steps:paras.append(pair(*r))
layout.append({'type':'lines','indices':list(range(s0,len(paras)))})
add('Examples','مثالیں','بېلګې','heading')
visual('chem12-p86-iupac-examples',examples)
add('17.1.2 Structure of Alkyl Halides','17.1.2 الکائل ہیلائیڈز کی ساخت','17.1.2 د الکایل هالایډونو جوړښت','heading')
add('To understand the structure of alkyl halides, let us consider methyl chloride as an example. In this molecule the carbon atom is sp³-hybridized and all the bonds of carbon are sigma. During the process of bond formation, one sp³–hybrid orbital of carbon atom overlaps with the half-filled p orbital of chlorine atom and form carbon-chlorine sigma bond, while the remaining three sp³-hybrid orbitals overlap with 1s orbitals of three hydrogen atoms and form three carbon-hydrogen sigma bonds (Figure 17.1). The bond lengths of carbon-chlorine and carbon-hydrogen bonds are 178 pm and 108 pm respectively. The H–C–H and H–C–Cl bond angles are approximately equal to 109.5°.',
 'الکائل ہیلائیڈز کی ساخت سمجھنے کے لیے میتھائل کلورائیڈ کو مثال کے طور پر لیں۔ اس سالمے میں کاربن ایٹم sp³-ہائبرڈ ہے اور کاربن کے تمام بند سگما ہیں۔ بند بننے کے عمل میں کاربن ایٹم کا ایک sp³–ہائبرڈ آربیٹل کلورین ایٹم کے نیم پُر p آربیٹل سے تداخل کر کے کاربن–کلورین سگما بند بناتا ہے، جبکہ باقی تین sp³-ہائبرڈ آربیٹل تین ہائیڈروجن ایٹموں کے 1s آربیٹلوں سے تداخل کر کے تین کاربن–ہائیڈروجن سگما بند بناتے ہیں (شکل 17.1)۔ کاربن–کلورین اور کاربن–ہائیڈروجن بندوں کی لمبائیاں بالترتیب 178 pm اور 108 pm ہیں۔ H–C–H اور H–C–Cl بند زاویے تقریباً 109.5° کے برابر ہیں۔',
 'د الکایل هالایډونو د جوړښت د پوهېدو لپاره، میتایل کلوراید د بېلګې په توګه ونیسئ. په دې مالیکول کې کاربني اټوم sp³-هایبرېډ دی او د کاربن ټول تړونونه سیګما دي. د تړون د جوړېدو په بهیر کې د کاربني اټوم یو sp³–هایبرېډ اوربیټال د کلورین اټوم له نیم ډک p اوربیټال سره تداخل کوي او کاربن–کلورین سیګما تړون جوړوي، په داسې حال کې چې پاتې درې sp³-هایبرېډ اوربیټالونه د دریو هایدروجني اټومونو له 1s اوربیټالونو سره تداخل کوي او درې کاربن–هایدروجن سیګما تړونونه جوړوي (شکل 17.1). د کاربن–کلورین او کاربن–هایدروجن تړونونو اوږدوالي په ترتیب سره 178 pm او 108 pm دي. د H–C–H او H–C–Cl تړون زاویې نږدې 109.5° سره برابرې دي.')
visual('chem12-figure17-1',methylcl)
add('Figure 17.1 Orbital hybridization model of bonding in methyl chloride','شکل 17.1 میتھائل کلورائیڈ میں بندش کا آربیٹل ہائبرڈائزیشن ماڈل','شکل 17.1 په میتایل کلوراید کې د تړون د اوربیټال هایبرېډیزېشن ماډل')
add('17.1.3 Physical Properties','17.1.3 طبعی خصوصیات','17.1.3 فزیکي ځانګړنې','heading')
for e,u,p in [
 ('Lower alkyl halides such as methyl fluoride, methyl chloride, methyl bromide, ethyl fluoride, ethyl chloride and propyl fluorides are gases at room temperature. Mostly higher n-alkyl halides up to C₁₆ are liquids and above are solids.','کم کاربن والے الکائل ہیلائیڈز جیسے میتھائل فلورائیڈ، میتھائل کلورائیڈ، میتھائل برومائیڈ، ایتھائل فلورائیڈ، ایتھائل کلورائیڈ اور پروپائل فلورائیڈز کمرے کے درجہ حرارت پر گیسیں ہیں۔ زیادہ تر بڑے n-الکائل ہیلائیڈز C₁₆ تک مائع اور اس سے اوپر ٹھوس ہیں۔','ټیټ الکایل هالایډونه لکه میتایل فلوراید، میتایل کلوراید، میتایل برومایډ، ایتیل فلوراید، ایتیل کلوراید او پروپیل فلورایډونه د کوټې په تودوخه کې ګازونه دي. ډېری لوړ n-الکایل هالایډونه تر C₁₆ پورې مایعات او له هغه پورته جامد دي.'),
 ('They have higher boiling points than the corresponding alkanes. For a given alkyl group the boiling points of alkyl halides increase with increasing size of the halogen atom, while for a given halogen atom the boiling points of alkyl halides increase with the increasing size of the alkyl group. For isomeric alkyl halides, the compound with the more highly branched alkyl group normally has the lowest boiling point.','ان کے نقطۂ جوش متعلقہ الکینز (اکیلے بند والے) سے زیادہ ہیں۔ کسی دیے گئے الکائل گروپ کے لیے ہیلوجن ایٹم کا حجم بڑھنے سے الکائل ہیلائیڈز کے نقطۂ جوش بڑھتے ہیں، جبکہ کسی دیے گئے ہیلوجن ایٹم کے لیے الکائل گروپ کا حجم بڑھنے سے نقطۂ جوش بڑھتے ہیں۔ ہم ترکیب الکائل ہیلائیڈز میں عموماً زیادہ شاخ دار الکائل گروپ والے مرکب کا نقطۂ جوش سب سے کم ہوتا ہے۔','د ایشېدو ټکي یې له اړوندو الکانونو لوړ دي. د یوه ورکړل شوي الکایل ګروپ لپاره د هالوجني اټوم د اندازې په زیاتېدو د الکایل هالایډونو د ایشېدو ټکي زیاتېږي، او د یوه ورکړل شوي هالوجني اټوم لپاره د الکایل ګروپ د اندازې په زیاتېدو د ایشېدو ټکي زیاتېږي. په ایزومري الکایل هالایډونو کې معمولاً هغه مرکب چې ډېر څانګه لرونکی الکایل ګروپ لري، تر ټولو ټیټ د ایشېدو ټکی لري.'),
 ('They are usually insoluble in water due to their inability to form hydrogen bonding with water. They are soluble in organic solvents.','پانی سے ہائیڈروجن بندش نہ بنا سکنے کی وجہ سے یہ عموماً پانی میں حل نہیں ہوتے۔ یہ نامیاتی محللات میں حل پذیر ہیں۔','له اوبو سره د هایدروجني تړون د نه جوړولو له امله معمولاً په اوبو کې نه حلېږي. په عضوي محللونو کې حلېږي.'),
 ('Alkyl chlorides and alkyl fluorides are lighter than water while alkyl iodides and alkyl bromides are denser than water. A mixture of an alkyl halide and water separates into two layers. When the alkyl halide is a fluoride or chloride, it is the upper layer and water is the lower. The situation is reversed when the alkyl halide is a bromide or an iodide.','الکائل کلورائیڈز اور الکائل فلورائیڈز پانی سے ہلکے ہیں جبکہ الکائل آئیوڈائیڈز اور الکائل برومائیڈز پانی سے زیادہ کثیف ہیں۔ الکائل ہیلائیڈ اور پانی کا آمیزہ دو تہوں میں الگ ہو جاتا ہے۔ جب الکائل ہیلائیڈ فلورائیڈ یا کلورائیڈ ہو تو وہ اوپری تہہ اور پانی نچلی تہہ ہوتا ہے۔ جب الکائل ہیلائیڈ برومائیڈ یا آئیوڈائیڈ ہو تو صورتحال الٹ ہوتی ہے۔','الکایل کلورایډونه او الکایل فلورایډونه له اوبو سپک دي، خو الکایل ایوډایډونه او الکایل برومایډونه له اوبو ډېر کثیف دي. د الکایل هالایډ او اوبو ګډوله په دوو طبقو بېلېږي. کله چې الکایل هالایډ فلوراید یا کلوراید وي، پورتنۍ طبقه ده او اوبه لاندې دي. کله چې الکایل هالایډ برومایډ یا ایوډایډ وي، حالت برعکس دی.')]:
 add(e,u,p,'list')
record=section('17.2','IUPAC naming, structure and physical properties of alkyl halides','الکائل ہیلائیڈز کی IUPAC نام گذاری، ساخت اور طبعی خصوصیات','د الکایل هالایډونو IUPAC نومول، جوړښت او فزیکي ځانګړنې',paras,layout,blocks,'164–165')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':86,'printedPages':[164,165]}]
record['sourceContinuesOnPdfPage']=87
carry=[{'from':'17.2','to':'17.3','startsAt':'Table 7.1 Boiling Points of Alkyl Halides'}]
if __name__=='__main__':save(86,[record],carry=carry,chapter_number=17)
