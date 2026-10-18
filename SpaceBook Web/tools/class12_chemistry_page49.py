"""PDF49 printed90–91: classification charts, rings and source table15.1."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
import math
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,body,labels=None):
 svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 500" role="img"><g font-family="Arial" font-size="18" fill="#222">'+body+'</g></svg>'
 b={'id':identity,'svg':svg,'svgUrdu':svg,'svgPashto':svg}
 for field,n in [('svgUrdu',0),('svgPashto',1)]:
  for old,words in (labels or {}).items():b[field]=b[field].replace('>'+old+'</text>','>'+words[n]+'</text>')
 blocks.append(b);layout.append({'type':'visual','blockId':identity})
labels={'Organic compounds':('نامیاتی مرکبات','عضوي مرکبات'),'Acyclic':('غیر حلقوی','غیر کړیز'),'Cyclic':('حلقوی','کړیز'),'Straight chain':('سیدھی زنجیر','مستقیم ځنځیر'),'Branched chain':('شاخ دار زنجیر','څانګه لرونکی ځنځیر'),'Homocyclic':('ہم حلقوی','هوموسایکلیک'),'Heterocyclic':('غیر ہم حلقوی','هېټروسایکلیک'),'Alicyclic':('ایلی سائیکلیک','الی سایکلیک'),'Aromatic':('ارومیٹک','اروماتیک')}
body='<path d="M380 45V75H180V120M380 75H600V120M180 155V185H90V230M180 185H270V230M600 155V185H500V230M600 185H675V230M500 265V300H420V345M500 300H580V345" fill="none" stroke="#222" stroke-width="2"/>'
for x,y,label in [(300,35,'Organic compounds'),(150,145,'Acyclic'),(570,145,'Cyclic'),(20,260,'Straight chain'),(200,260,'Branched chain'),(450,255,'Homocyclic'),(625,255,'Heterocyclic'),(370,370,'Alicyclic'),(540,370,'Aromatic')]:body+=f'<text x="{x}" y="{y}">{label}</text>'
visual('chem12-p90-classification-chart',body,labels)
add('On the other hand, heterocyclic organic compounds are those cyclic compounds in which ring contain at least one atom other than carbon.',
 'دوسری طرف غیر ہم حلقوی نامیاتی مرکبات وہ حلقوی مرکبات ہیں جن کے حلقے میں کم از کم ایک غیر کاربن ایٹم ہے۔',
 'بل لوري ته هېټروسایکلیک عضوي مرکبات هغه کړیز مرکبات دي چې په کړۍ کې یې لږ تر لږه یو له کاربن پرته اټوم وي.')
def ring(x,y,n=6,r=35,double=False,hetero=None,full=False):
 offset=math.pi if n==5 else 0
 pts=[(x+r*math.sin(2*math.pi*i/n+offset),y-r*math.cos(2*math.pi*i/n+offset)) for i in range(n)]
 b='<path d="M'+'L'.join(f'{a:.2f} {c:.2f}' for a,c in pts)+'Z" fill="none" stroke="#222" stroke-width="2"/>'
 if double:
  for i in ([1,3] if n==5 else range(0,n,2)):
   a,c=pts[i];d,e=pts[(i+1)%n];b+=f'<path d="M{x+(a-x)*.80} {y+(c-y)*.80}L{x+(d-x)*.80} {y+(e-y)*.80}" stroke="#222" stroke-width="1.5"/>'
 if full:
  label=full if isinstance(full,str) else 'CH₂'
  for a,c in pts:b+=f'<rect x="{a-17}" y="{c-13}" width="34" height="22" fill="white"/><text x="{a-15}" y="{c+4}">{label}</text>'
 if hetero:
  a,c=pts[0 if n==5 else n//2];b+=f'<rect x="{a-10}" y="{c-12}" width="24" height="27" fill="white"/><text x="{a-7}" y="{c+7}">{hetero}</text>'
 return b
body=ring(60,60,3,30,full=True)+ring(160,60,3,30)+ring(275,60,4,30,full=True)+ring(375,60,4,30)+ring(510,60)
body+=ring(80,225,double=True)+ring(195,225,double=True,full='CH')+ring(325,225,double=True)+ring(455,225,double=True)+ring(515,225,double=True)
body+='<text x="309" y="166">CH₃</text><path d="M325 190V174" stroke="#222"/><text x="135" y="225">or</text><text x="100" y="62">or</text><text x="318" y="70">or</text><text x="48" y="120">Cyclopropane</text><text x="265" y="120">Cyclobutane</text><text x="465" y="120">Cyclohexane</text><text x="48" y="280">Benzene</text><text x="295" y="280">Toluene</text><text x="450" y="280">Naphthalene</text><text x="610" y="65">Alicyclic</text><text x="610" y="88">Organic Compounds</text><text x="585" y="215">Aromatic (Homocyclic)</text><text x="610" y="240">Organic Compounds</text>'
body+=ring(90,385,double=True,hetero='N')+ring(245,385,n=5,double=True,hetero='S')+ring(395,385,n=5,double=True,hetero='O')+ring(545,385,n=5,double=True,hetero='N')
body+='<text x="555" y="438">H</text><text x="55" y="465">Pyridine</text><text x="208" y="465">Thiopene</text><text x="370" y="465">Furan</text><text x="520" y="475">Pyrrole</text><text x="610" y="375">Heterocyclic</text><text x="610" y="400">Organic Compounds</text>'
names={'Cyclopropane':('سائیکلوپروپین','سایکلوپروپان'),'Cyclobutane':('سائیکلوبیوٹین','سایکلوبیوټان'),'Cyclohexane':('سائیکلوہیکسین','سایکلوهېکسان'),'Benzene':('بینزین','بنزین'),'Toluene':('ٹولیوئن','تولوین'),'Naphthalene':('نیفتھلین','نفتالین'),'Pyridine':('پائریڈین','پیریډین'),'Thiopene':('تھیوپین','تیوپین'),'Furan':('فیوران','فوران'),'Pyrrole':('پائرول','پیرول'),'Organic Compounds':('نامیاتی مرکبات','عضوي مرکبات'),'Aromatic (Homocyclic)':('ارومیٹک (ہم حلقوی)','اروماتیک (هوموسایکلیک)'),'or':('یا','یا'),**labels}
visual('chem12-p90-cyclic-structures',body,names)
add('b. Classification on the basis of Functional group','b. فعلی گروپ کی بنیاد پر درجہ بندی','b. د فعالي ګروپ پر بنسټ ډلبندي','heading')
add('An atoms or a group of atoms or multiple bonds that gives certain characteristic properties to an organic compound is called a functional group because it is the chemically active or functional part of a molecule. Each functional group represents a different class of organic compounds.',
 'ایٹم یا ایٹموں کا گروپ یا کثیر بند جو نامیاتی مرکب کو خاص امتیازی خصوصیات دے، فعلی گروپ ہے، کیونکہ سالمے کا کیمیائی طور پر فعال یا فعلی حصہ ہے۔ ہر فعلی گروپ نامیاتی مرکبات کی الگ قسم ظاہر کرتا ہے۔',
 'اټوم یا د اټومونو ګروپ یا څوګوني تړونونه چې عضوي مرکب ته ځانګړې ځانګړنې ورکوي، فعالي ګروپ دی، ځکه د مالیکول کیمیاوي فعال یا فعالي برخه ده. هر فعالي ګروپ د عضوي مرکباتو بېله ډله ښيي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Alkanes contain only single bonds and having general formula is CₙH₂ₙ₊₂ where n = 1, 2, 3, … shows number of carbon atoms e.g. methane (CH₄), ethane (C₂H₆) etc.',
 'الکینز صرف یک بند رکھتے ہیں اور عمومی فارمولا CₙH₂ₙ₊₂ ہے، جہاں n = 1, 2, 3, … کاربن ایٹموں کی تعداد ہے، مثلاً میتھین (CH₄)، ایتھین (C₂H₆) وغیرہ۔',
 'الکانونه یوازې یوګوني تړونونه لري او عمومي فورمول یې CₙH₂ₙ₊₂ دی، چې n = 1, 2, 3, … د کاربني اټومونو شمېر ښيي، لکه میتان (CH₄)، ایتان (C₂H₆) او نور.')
add('Different classes of organic compounds, their functional groups and general formulae are summarized in the following table along with example.',
 'نامیاتی مرکبات کی مختلف اقسام، فعلی گروپ اور عمومی فارمولے مثالوں سمیت درج ذیل جدول میں ہیں۔',
 'د عضوي مرکباتو بېلابېلې ډلې، فعالي ګروپونه او عمومي فورمولونه له بېلګو سره په لاندې جدول کې راټول دي.')
add('Table: 15.1 Classification of Organic Compounds Based on Functional Groups','جدول15.1 فعلی گروپوں کی بنیاد پر نامیاتی مرکبات کی درجہ بندی','جدول15.1 د فعالي ګروپونو پر بنسټ د عضوي مرکباتو ډلبندي')
rows=[['Alkane','–','–','CₙH₂ₙ₊₂','CH₄ methane'],['Alkene','>C=C<','Double bond','CₙH₂ₙ','C₂H₄ or CH₂=CH₂ ethene'],['Alkyne','–C≡C–','Triple bond','CₙH₂ₙ₋₂','HC≡CH or C₂H₂ ethyne'],['Alkyl halide','–X (F, Cl, Br, I)','Halo (Flouro, Chloro, Bromo)','R–X or CₙH₂ₙ₊₁X','CH₃–Cl methyl chloride; C₂H₅–I ethyl iodide'],['Alcohol or alkanol','–OH','Hydroxyl','R–OH or CₙH₂ₙ₊₁OH','CH₃–OH methyl alcohol (methanol)'],['Amine','–NH₂','Amino','R–NH₂ or CₙH₂ₙ₊₁NH₂','CH₃–NH₂ methyl amine'],['Ether','–O–','Oxygen (oxa)','R–O–R or (CₙH₂ₙ₊₁)₂O','CH₃–O–CH₃ dimethyl ether'],['Ketone','–C(=O)–','Carbonyl (Keto group)','(CₙH₂ₙ₊₁)₂CO','CH₃–C(=O)–CH₃ dimethyl ketone (acetone)'],['Aldehyde','–C(=O)–H or –CHO','Formyl','R–C(=O)–H or CₙH₂ₙ₊₁CHO','CH₃–C(=O)–H acetaldehyde (ethanal)']]
urclasses=['الکین','الکین (دوہرا بند)','الکائن','الکائل ہیلائیڈ','الکوحل یا الکانول','امین','ایتھر','کیٹون','ایلڈیہائیڈ'];psclasses=['الکان','الکین','الکاین','الکایل هالایډ','الکول یا الکانول','امین','ایتر','کیټون','الدیهایډ']
urtypes=['–','دوہرا بند','سہرا بند','ہیلو (فلورو، کلورو، برومو)','ہائیڈروکسل','امینو','آکسیجن (آکسا)','کاربونائل (کیٹو گروپ)','فارمائل'];pstypes=['–','دوه ګونی تړون','درې ګونی تړون','هالو (فلورو، کلورو، برومو)','هایدروکسیل','امینو','اکسیجن (اوکسا)','کاربونیل (کیټو ګروپ)','فارمیل']
examples=[('میتھین','میتان'),('ایتھین','ایتین'),('ایتھائن','ایتاین'),('میتھائل کلورائیڈ؛ ایتھائل آئیوڈائیڈ','میتیل کلورایډ؛ ایتیل ایوډایډ'),('میتھائل الکوحل (میتھانول)','میتیل الکول (میتانول)'),('میتھائل امین','میتیل امین'),('ڈائی میتھائل ایتھر','ډای میتیل ایتر'),('ڈائی میتھائل کیٹون (ایسیٹون)','ډای میتیل کیټون (اسیتون)'),('ایسیٹ ایلڈیہائیڈ (ایتھانال)','اسیت الدیهایډ (ایتانال)')]
trans=[]
for n,lang,classes,types,headers in [(0,'اردو',urclasses,urtypes,['مرکبات کی قسم','فعلی گروپ','فعلی گروپ کا نام','عمومی فارمولا','مثال']),(1,'پښتو',psclasses,pstypes,['د مرکباتو ډله','فعالي ګروپ','د فعالي ګروپ نوم','عمومي فورمول','بېلګه'])]:
 translated=[]
 for i,r in enumerate(rows):
  # Keep example formulas from the source and translate their explanatory names.
  formulas=['CH₄','C₂H₄ / CH₂=CH₂','HC≡CH / C₂H₂','CH₃–Cl / C₂H₅–I','CH₃–OH','CH₃–NH₂','CH₃–O–CH₃','CH₃–C(=O)–CH₃','CH₃–C(=O)–H']
  translated.append([classes[i],r[1],types[i],r[3],formulas[i]+' '+examples[i][n]])
 trans.append({'language':lang,'headers':headers,'rows':translated})
blocks.append({'id':'chem12-table15-1-first','headers':['Class of Compounds','Functional Group','Name of Functional group','General Formula','Example'],'rows':rows,'translations':trans});layout.append({'type':'sourceDataTable','tableId':blocks[-1]['id']})
record=section('15.4','Cyclic structures and functional groups','حلقوی ساختیں اور فعلی گروپ','کړیز جوړښتونه او فعالي ګروپونه',paras,layout,blocks,'90–91');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':49,'printedPages':[90,91]}];record['sourceContinuesOnPdfPage']=50
if __name__=='__main__':save(49,[record],carry=[{'from':'15.4','to':'15.5','startsAt':'91\nO\n0\n-C-OH'}],issues=[{'id':'chem12-p90-thiopene','printedPage':90,'description':'Printed ring caption Thiopene retained; structural diagram comparison pending.'}],chapter_number=15)
