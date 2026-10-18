"""PDF62 printed116–117: alkene naming, orbital structure and conjugation."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from html import escape
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def svg_start(h):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 {h}" role="img"><rect width="880" height="{h}" fill="white"/><g font-family="Arial,sans-serif" fill="#17212b">'
def text(x,y,v,size=22):return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}">{escape(v)}</text>'
def line(x,y,a,b,w=2):return f'<path d="M{x} {y}L{a} {b}" fill="none" stroke="#222" stroke-width="{w}"/>'
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
def chain(x,y,groups,doubles=(),numbers=None,branch=None,step=68):
 s=''
 for i in range(len(groups)-1):
  for dy in ([-3,3] if i in doubles else [0]):s+=line(x+i*step+22,y-6+dy,x+(i+1)*step-22,y-6+dy)
 for i,g in enumerate(groups):
  if branch and i==branch[0]:s+=line(x+i*step,y-20,x+i*step,y-48)+text(x+i*step,y-55,branch[1],20)
  s+=text(x+i*step,y,g,21)
  if numbers:s+=text(x+i*step-10,y-24,str(numbers[i]),13)
 return s
def common(lang):
 a={'en':['α-butylene','β-butylene'],'ur':['α-بیوٹیلین','β-بیوٹیلین'],'ps':['α-بیوټیلین','β-بیوټیلین']}[lang]
 return svg_start(150)+chain(105,68,['CH₂','CH','CH₂','CH₃'],[0],['α','β','γ','δ'])+text(205,115,a[0],19)+chain(530,68,['CH₃','CH','CH','CH₃'],[1],['α','β','γ','δ'])+text(635,115,a[1],19)+'</g></svg>'
add('Greek letters, α, β, γ etc. are used to distinguish isomers having double bonds at different positions.','مختلف مقامات پر دوہرے بند رکھنے والے آئسومروں میں فرق کے لیے یونانی حروف α، β، γ وغیرہ استعمال ہوتے ہیں۔','یوناني توري α، β، γ او نور په بېلابېلو موقعیتونو کې د دوه ګونو تړونونو لرونکو ایزومرونو د توپیر لپاره کارېږي.')
visual('chem12-p62-common-names',common)
add('(b) IUPAC System','(b) IUPAC نظام','(b) د IUPAC سیستم','heading')
add('The IUPAC rules for naming alkenes are;','الکینز کے نام رکھنے کے IUPAC اصول یہ ہیں؛','د الکینونو د نومولو IUPAC اصول دا دي؛')
rules=[
('i. Select the longest continuous carbon chain that include the maximum number of double bonds.','i. طویل ترین مسلسل کاربن زنجیر منتخب کریں جس میں دوہرے بندوں کی زیادہ سے زیادہ تعداد ہو۔','i. تر ټولو اوږد پرله پسې کاربني ځنځیر وټاکئ چې د دوه ګونو تړونونو تر ټولو ډېر شمېر ولري.'),
('ii. The name given to the longest chain will act as parent name, whereby the suffix -ane of the corresponding alkane is replaced by suffix -ene.','ii. طویل ترین زنجیر کا نام بنیادی نام ہو گا، جس میں متعلقہ الکین کا لاحقہ -ane بدل کر -ene کر دیا جاتا ہے۔','ii. تر ټولو اوږده ځنځیر ته ورکړل شوی نوم به بنسټیز نوم وي، چې د اړوند الکان -ane وروستاړی په -ene بدلېږي.'),
('iii. If there are two double bonds, the suffix is -diene; for three, -triene; for four, -tetraene; and so on, are used.','iii. دو دوہرے بند ہوں تو لاحقہ -diene؛ تین کے لیے -triene؛ چار کے لیے -tetraene؛ اور اسی طرح دوسرے لاحقے استعمال ہوتے ہیں۔','iii. که دوه دوه ګوني تړونونه وي، -diene وروستاړی؛ د دریو لپاره -triene؛ د څلورو لپاره -tetraene او همداسې نور کارېږي.'),
('iv. Number the chain from the end that gives lower number to the doubly bonded carbons.','iv. زنجیر کی نمبر گذاری اس سرے سے کریں جو دوہرے بند والے کاربنوں کو کم نمبر دے۔','iv. ځنځیر له هغې خوا وشمېرئ چې د دوه ګوني تړون کاربنونو ته ټیټه شمېره ورکړي.'),
('v. Since double bond appears between two carbon atoms, therefore its position is indicated by the number of that carbon atom, bearing lower number and this number is written before suffix -ene, -diene etc.','v. چونکہ دوہرا بند دو کاربن ایٹموں کے درمیان ہوتا ہے، اس لیے اس کا مقام ان میں کم نمبر والے کاربن ایٹم کے نمبر سے ظاہر کیا جاتا ہے، اور یہ نمبر -ene، -diene وغیرہ لاحقوں سے پہلے لکھا جاتا ہے۔','v. څرنګه چې دوه ګونی تړون د دوو کاربني اټومونو ترمنځ وي، نو موقعیت یې د ټیټې شمېرې لرونکي کاربني اټوم په شمېره ښودل کېږي او دا شمېره له -ene، -diene او نورو وروستاړو مخکې لیکل کېږي.'),
('vi. Carbon-carbon double bonds take precedence over alkyl groups in determining the main carbon chain and the direction in which it is numbered.','vi. بنیادی کاربن زنجیر اور اس کی نمبر گذاری کی سمت مقرر کرنے میں کاربن–کاربن دوہرے بندوں کو الکائل گروپوں پر ترجیح حاصل ہے۔','vi. د اصلي کاربني ځنځیر او د هغه د شمېرلو د لوري په ټاکلو کې کاربن–کاربن دوه ګوني تړونونه پر الکایل ګروپونو لومړیتوب لري.'),
('vii. Name substituent groups as in alkanes, indicating their locations by the number of the main-chain carbon to which they are attached.','vii. متبادل گروپوں کے نام الکینز کی طرح رکھیں اور ان کے مقامات بنیادی زنجیر کے اس کاربن کے نمبر سے بتائیں جس سے وہ جڑے ہوں۔','vii. د ځایناستو ګروپونو نومونه د الکانونو په څېر ولیکئ او موقعیتونه یې د اصلي ځنځیر د هغه کاربن په شمېره وښيئ چې ورسره تړلي دي.'),
('viii. For compounds that show geometric isomerism, add the appropriate prefix: cis- or trans-.(see section 16.6)','viii. ہندسی آئسومرزم دکھانے والے مرکبات کے لیے مناسب سابقہ cis- یا trans- شامل کریں۔ (حصہ16.6 دیکھیے)','viii. د هغو مرکباتو لپاره چې هندسي ایزومېریزم ښيي، مناسب cis- یا trans- مختاړی ورزیات کړئ. (برخه16.6 وګورئ)')]
for row in rules:add(*row,'list')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Now α, β, γ are replaced by numbers 1, 2, 3 in IUPAC.','اب IUPAC میں α، β، γ کی جگہ اعداد1،2،3 استعمال ہوتے ہیں۔','اوس په IUPAC کې د α، β، γ پر ځای 1،2،3 شمېرې کارېږي.')
add('Examples','مثالیں','بېلګې','heading')
def examples(lang):
 names={'en':['ethene','propene','but-1-ene','but-2-ene','4-methylpent-1-ene','penta-1,3-diene'],'ur':['ایتھین','پروپین','بیوٹ-1-این','بیوٹ-2-این','4-میتھائل پینٹ-1-این','پینٹا-1،3-ڈائین'],'ps':['ایتین','پروپین','بیوټ-1-ین','بیوټ-2-ین','4-میتایل پینټ-1-ین','پینټا-1،3-ډایین']}[lang]
 s=svg_start(490)
 specs=[(100,65,['CH₂','CH₂'],[0],None,None),(540,65,['CH₃','CH','CH₂'],[1],None,None),(75,208,['CH₃','CH₂','CH','CH₂'],[2],[4,3,2,1],None),(525,208,['CH₃','CH','CH','CH₃'],[1],[1,2,3,4],None),(65,397,['CH₃','CH','CH₂','CH','CH₂'],[3],[5,4,3,2,1],(1,'CH₃')),(510,397,['CH₂','CH','CH','CH','CH₃'],[0,2],[1,2,3,4,5],None)]
 for name,(x,y,g,d,n,b) in zip(names,specs):s+=chain(x,y,g,d,n,b)+text(x+(len(g)-1)*34,y+44,name,18)
 return s+'</g></svg>'
visual('chem12-p62-iupac-examples',examples)
add('16.5.2 Structure','16.5.2 ساخت','16.5.2 جوړښت','heading')
add('Consider ethene (C₂H₄) to illustrate the structure of alkenes. In ethene, each carbon atom has three sp²-hybridized orbitals which are coplanar. One of the sp²-hybrid orbitals of one carbon atom overlaps linearly with that of another carbon atom to form a sigma (δ) bond. The other two sp²-hybrid orbitals of each carbon atom overlap with 1s orbital of hydrogen atoms to form C-H sigma bonds. The unhybridized p-orbitals of the two carbon atoms, which remain perpendicular to the plane of hybridized orbitals, overlap in a side-wise (parallel) fashion to form a pi (π) bond between the two carbon atoms. (Figure.16.3).','الکینز کی ساخت واضح کرنے کے لیے ایتھین (C₂H₄) پر غور کریں۔ ایتھین میں ہر کاربن ایٹم کے تین sp² مخلوط مدار ہیں جو ایک ہی سطح میں واقع ہیں۔ ایک کاربن ایٹم کا ایک sp² مخلوط مدار دوسرے کاربن ایٹم کے ایسے مدار کے ساتھ خطی تداخل سے سگما (δ) بند بناتا ہے۔ ہر کاربن ایٹم کے باقی دو sp² مخلوط مدار ہائیڈروجن ایٹموں کے 1s مداروں سے تداخل کر کے C–H سگما بند بناتے ہیں۔ دونوں کاربن ایٹموں کے غیر مخلوط p مدار، جو مخلوط مداروں کی سطح پر عمودی رہتے ہیں، پہلو بہ پہلو (متوازی) تداخل سے دونوں کاربن ایٹموں کے درمیان پائی (π) بند بناتے ہیں۔ (شکل16.3)۔','د الکینونو د جوړښت د روښانولو لپاره ایتین (C₂H₄) په پام کې ونیسئ. په ایتین کې هر کاربني اټوم درې sp² هایبرډ اوربیټلونه لري چې په یوه سطحه کې دي. د یوه کاربني اټوم یو sp² هایبرډ اوربیټل د بل کاربني اټوم له همداسې اوربیټل سره خطي پوښښ کوي، څو سیګما (δ) تړون جوړ کړي. د هر کاربني اټوم نور دوه sp² هایبرډ اوربیټلونه د هایدروجني اټومونو له 1s اوربیټلونو سره پوښښ کوي، څو C–H سیګما تړونونه جوړ کړي. د دواړو کاربني اټومونو غیر هایبرډ p اوربیټلونه، چې د هایبرډ اوربیټلونو سطحې ته عمودي پاتې کېږي، په اړخیز (موازي) ډول پوښښ کوي، څو د دواړو کاربني اټومونو ترمنځ پای (π) تړون جوړ کړي. (شکل16.3).')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('In 1993, the IUPAC recommended a logical change in the positions of the numbers used in names. Instead of placing the numbers before the root name (1-butene), they recommended placing them immediately before the part of the name they locate (but-1-ene).','1993 میں IUPAC نے ناموں میں استعمال ہونے والے اعداد کے مقامات میں منطقی تبدیلی کی سفارش کی۔ اعداد کو بنیادی نام سے پہلے (1-butene) رکھنے کے بجائے اس حصے سے فوراً پہلے رکھنے کی سفارش کی گئی جس کا وہ مقام بتاتے ہیں (but-1-ene)۔','په 1993 کې IUPAC په نومونو کې د کارېدونکو شمېرو په موقعیتونو کې د منطقي بدلون سپارښتنه وکړه. د بنسټیز نوم مخکې د شمېرو د لیکلو (1-butene) پر ځای یې سپارښتنه وکړه چې شمېرې سم د نوم له هغې برخې مخکې ولیکل شي چې موقعیت یې ښيي (but-1-ene).')
def orbitals(lang):
 s=svg_start(300)
 # Planar sigma skeleton with the two perpendicular p orbitals.
 for cx in (230,385):
  for cy in (73,223):s+=f'<ellipse cx="{cx}" cy="{cy}" rx="24" ry="49" fill="#ecfdf5" stroke="#2f6b52" stroke-width="1.6"/>'
  s+=text(cx,154,'C',21)+text(cx,69,'p',18)
 for x in (273,342):s+=f'<ellipse cx="{x}" cy="147" rx="36" ry="21" fill="#ede2f3" stroke="#785887"/>'+text(x,154,'sp²',18)
 for cx,direction in [(230,-1),(385,1)]:
  for sign in [-1,1]:
   xx=cx+direction*60;yy=147+sign*32;hx=cx+direction*90;hy=147+sign*48
   s+=f'<ellipse cx="{xx}" cy="{yy}" rx="34" ry="18" transform="rotate({sign*direction*28} {xx} {yy})" fill="#ede2f3" stroke="#785887"/>'+text(xx,yy+6,'sp²',15)
   s+=f'<circle cx="{hx}" cy="{hy}" r="21" fill="#fff8c9" stroke="#806c25" stroke-dasharray="3 3"/>'+text(hx,hy+6,'H',18)+text(hx+direction*8,hy-sign*26,'δ',14)
 s+=text(230,154,'C',21)+text(385,154,'C',21)
 s+='<path d="M231 31 Q306 -4 385 31 M231 265 Q306 292 385 265" stroke="#222" fill="none"/>'+text(307,24,'π',19)+text(307,282,'π',19)
 # The second source view locates the electron pair above/below the C–C axis.
 for cx in (650,750):
  for cy in (87,202):s+=f'<ellipse cx="{cx}" cy="{cy}" rx="26" ry="51" fill="none" stroke="#6c9384" stroke-width="1.6"/>'
  s+=text(cx,151,'C',20)
 s+=line(668,145,732,145)
 for cx,d in [(650,-1),(750,1)]:
  s+=f'<path d="M{cx-8*d} 142L{cx+43*d} 125" stroke="#222" stroke-width="2" stroke-dasharray="2 4"/>'+text(cx+51*d,124,'H',19)
  s+=f'<path d="M{cx+10*d} 155L{cx+35*d} 166L{cx+31*d} 178Z" fill="#222"/>'+text(cx+48*d,190,'H',19)
 s+='<path d="M650 54Q700 25 750 54 M650 236Q700 268 750 236 M650 76Q700 93 750 76 M650 218Q700 204 750 218" stroke="#6c9384" fill="none"/>'+text(700,70,'••',18)
 return s+'</g></svg>'
visual('chem12-p62-ethene-orbitals',orbitals)
add('Figure 16.3 Orbital overlap discription in formation of sigma and pi bonds in ethene.','شکل16.3 ایتھین میں سگما اور پائی بندوں کی تشکیل میں مداروں کے تداخل کی وضاحت۔','شکل16.3 په ایتین کې د سیګما او پای تړونونو په جوړېدو کې د اوربیټلونو د پوښښ تشریح.')
add('The overall structure of ethene is planar in which H–C–C and H–C–H bond angles are approximately equal to 120°. The carbon-carbon double bond length is 134 pm and C–H bond lengths are 108 pm.','ایتھین کی مجموعی ساخت مسطح ہے جس میں H–C–C اور H–C–H بند زاویے تقریباً 120° کے برابر ہیں۔ کاربن–کاربن دوہرے بند کی لمبائی 134 pm اور C–H بندوں کی لمبائیاں 108 pm ہیں۔','د ایتین ټولیز جوړښت هوار دی، چې د H–C–C او H–C–H تړوني زاویې پکې نږدې 120° دي. د کاربن–کاربن دوه ګوني تړون اوږدوالی 134 pm او د C–H تړونونو اوږدوالی 108 pm دی.')
add('16.5.3 Conjugation','16.5.3 کنجوگیشن','16.5.3 کنجوګېشن','heading')
add('If an alkene has two double bonds, it is called a diene (or alkadiene), if three double bonds, then triene (or alkatriene) and so on. When two double bonds in an alkene (diene, triene etc) are separated by just one single bond, the two double bonds are said to be conjugated and the alkene is a conjugated alkene. The interaction between the two double bonds in a conjugated dienes (or triene etc.) delocalizes the electron density and increases the stability of the molecule, and termed as conjugation. The simplest diene that can have two conjugated pi bonds is buta-1,3-diene. Similarly hexa-1,3,5-triene is a triene with three conjugated double bonds and so on.','اگر الکین میں دو دوہرے بند ہوں تو اسے ڈائین (یا الکاڈائین)، تین ہوں تو ٹرائین (یا الکاٹرائین) اور اسی طرح کہتے ہیں۔ جب الکین (ڈائین، ٹرائین وغیرہ) کے دو دوہرے بندوں کے درمیان صرف ایک یک بند ہو تو دونوں دوہرے بند کنجوگیٹڈ کہلاتے ہیں اور الکین کو کنجوگیٹڈ الکین کہتے ہیں۔ کنجوگیٹڈ ڈائین (یا ٹرائین وغیرہ) کے دو دوہرے بندوں کے درمیان باہمی اثر الیکٹران کثافت کو غیر مقامی بناتا اور سالمے کے استحکام کو بڑھاتا ہے، اور اسے کنجوگیشن کہتے ہیں۔ دو کنجوگیٹڈ پائی بند رکھنے والا سادہ ترین ڈائین بیوٹا-1،3-ڈائین ہے۔ اسی طرح ہیکسا-1،3،5-ٹرائین تین کنجوگیٹڈ دوہرے بندوں والا ٹرائین ہے، وغیرہ۔','که الکین دوه دوه ګوني تړونونه ولري، ډایین (یا الکاډایین) بلل کېږي؛ که درې ولري، ټرایین (یا الکاټرایین) او همداسې نور. کله چې په الکین (ډایین، ټرایین او نورو) کې دوه دوه ګوني تړونونه یوازې په یوه یو ګوني تړون سره جلا وي، دواړه دوه ګوني تړونونه کنجوګېټ شوي او الکین کنجوګېټ شوی الکین بلل کېږي. په کنجوګېټ شوي ډایین (یا ټرایین او نورو) کې د دوو دوه ګونو تړونونو ترمنځ متقابل اغېز د الکترون کثافت غیر موضعي کوي او د مالیکول ثبات زیاتوي، او کنجوګېشن بلل کېږي. تر ټولو ساده ډایین چې دوه کنجوګېټ شوي پای تړونونه لرلی شي، بیوټا-1،3-ډایین دی. همدارنګه هیکسا-1،3،5-ټرایین د دریو کنجوګېټ شوو دوه ګونو تړونونو لرونکی ټرایین دی، او همداسې نور.')
def conjugated(lang):
 names={'en':['buta-1,3-diene','hexa-1,3,5-triene'],'ur':['بیوٹا-1،3-ڈائین','ہیکسا-1،3،5-ٹرائین'],'ps':['بیوټا-1،3-ډایین','هیکسا-1،3،5-ټرایین']}[lang]
 return svg_start(125)+text(205,48,'CH₂=CH–CH=CH₂')+text(205,95,names[0],19)+text(635,48,'CH₂=CH–CH=CH–CH=CH₂')+text(635,95,names[1],19)+'</g></svg>'
visual('chem12-p62-conjugated-formulas',conjugated)
record=section('16.9','Alkene nomenclature, structure and conjugation','الکینز کی نام گذاری، ساخت اور کنجوگیشن','د الکینونو نومول، جوړښت او کنجوګېشن',paras,layout,blocks,'116–117')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':62,'printedPages':[116,117]}]
issues=[{'id':'chem12-p117-printed-symbol-spelling','printedPage':117,'description':'Source sigma symbol resembles δ and Figure16.3 spells discription; these printed forms are preserved pending glyph review.'}]
if __name__=='__main__':save(62,[record],carry=[{'from':'16.9','to':'16.10','startsAt':'Let us consider buta-1,3-diene'}],issues=issues,chapter_number=16)
