"""PDF111 printed214–215: nitration/halogenation of phenol, reaction with Na, oxidation, alcohol vs phenol (start)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow111');t=F.t;line=F.line;ring=F.ring
def builder():
 P=[];L=[];B=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def visual(identity,fn):B.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});L.append({'type':'visual','blockId':identity})
 return P,L,B,add,visual
N={'phenol':('فینول','فینول'),'o-nitrophenol (55%)':('o-نائٹرو فینول (55%)','o-نایټروفینول (55%)'),'m-nitrophenol (1%)':('m-نائٹرو فینول (1%)','m-نایټروفینول (1%)'),'p-nitrophenol (44%)':('p-نائٹرو فینول (44%)','p-نایټروفینول (44%)'),
   '2,4,6-trinitrophenol':('2،4،6-ٹرائی نائٹرو فینول','2،4،6-ټرای نایټروفینول'),'(picric acid)':('(پکرک ایسڈ)','(پکریک اسید)'),'2,4,6-tribromophenol':('2،4،6-ٹرائی برومو فینول','2،4،6-ټرای بروموفینول'),'(white ppt)':('(سفید رسوب)','(سپین رسوب)'),
   'o-bromophenol':('o-برومو فینول','o-بروموفینول'),'p-bromophenol':('p-برومو فینول','p-بروموفینول'),'sodium phenoxide':('سوڈیم فینو آکسائیڈ','سوډیم فینوکساید'),'p-benzoquinone':('p-بینزو کوئنون','p-بنزوکینون'),'water':('پانی','اوبه'),
   'methyl alcohol':('میتھائل الکوحل','میتایل الکول'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'n-propyl alcohol':('n-پروپائل الکوحل','n-پروپیل الکول'),'cyclopentanol':('سائیکلوپینٹانول','سایکلوپېنټانول'),'(cyclopentyl alcohol)':('(سائیکلوپینٹائل الکوحل)','(سایکلوپېنټیل الکول)'),
   'cyclohexanol':('سائیکلوہیکسانول','سایکلوهېکسانول'),'(cyclohexyl alcohol)':('(سائیکلوہیکسائل الکوحل)','(سایکلوهېکسیل الکول)'),'cyclohexane-1,2-diol':('سائیکلوہیکسین-1،2-ڈائی اول','سایکلوهېکسان-1،2-ډای ول')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def lab(x,y,lang,*ws):return ''.join(t(x,y+15*i,lb(lang,w),12) for i,w in enumerate(ws))
def nitr(lang):
 s=F.start(200)+ring(70,95,26,subs={0:'OH'})+lab(70,150,lang,'phenol')+line(110,95,210,95,2,'#222','marker-end="url(#arrow111)"')+t(160,85,'dil. HNO₃',12)+t(160,110,'25°C',12)+t(160,124,'−H₂O',12)
 for k,(v,n) in enumerate(zip((1,2,3),('o-nitrophenol (55%)','m-nitrophenol (1%)','p-nitrophenol (44%)'))):
  x=300+k*200;s+=ring(x,85,26,subs={0:'OH',v:'NO₂'})+lab(x,170 if v==3 else 148,lang,n)
  if k<2:s+=t(x+100,90,'+',20)
 return s+'</svg>'
def picric(lang):return F.start(180)+ring(160,80,28,subs={0:'OH'})+lab(160,135,lang,'phenol')+F.arrow(230,370,80,'conc. HNO₃','25°C')+ring(470,80,28,subs={0:'OH',1:'NO₂',3:'NO₂',5:'O₂N'})+lab(470,158,lang,'2,4,6-trinitrophenol','(picric acid)')+t(620,87,'+ 3H₂O',17)+'</svg>'
def brom(lang):return F.start(180)+ring(140,80,28,subs={0:'OH'})+lab(140,135,lang,'phenol')+t(230,87,'+ 3Br₂',16)+F.arrow(280,380,80,lb(lang,'water'))+ring(470,80,28,subs={0:'OH',1:'Br',3:'Br',5:'Br'})+lab(470,158,lang,'2,4,6-tribromophenol','(white ppt)')+t(620,87,'+ 3HBr',17)+'</svg>'
def mono(lang):
 s=F.start(190)+ring(120,85,26,subs={0:'OH'})+lab(120,140,lang,'phenol')+line(160,85,280,85,2,'#222','marker-end="url(#arrow111)"')+t(220,73,'Br₂, CCl₄',12)+t(220,100,'25°C',12)+t(220,114,'−HBr',12)
 s+=ring(370,85,26,subs={0:'OH',1:'Br'})+lab(370,140,lang,'o-bromophenol')+t(460,90,'+',20)+ring(560,85,26,subs={0:'OH',3:'Br'})+lab(560,162,lang,'p-bromophenol')
 return s+'</svg>'
def sodium(lang):return F.start(140)+ring(170,80,26,subs={0:'OH'})+lab(170,132,lang,'phenol')+t(260,86,'+ Na',16)+F.arrow(310,410,80)+ring(490,80,26,subs={0:'O⁻Na⁺'})+lab(490,132,lang,'sodium phenoxide')+t(620,86,'+ ½H₂↑',16)+'</svg>'
def quinone(lang):
 s=F.start(180)+ring(220,85,28,subs={0:'OH'})+lab(220,140,lang,'phenol')+F.arrow(290,410,85,'K₂Cr₂O₇','H₂SO₄, H₂O')
 s+=F.ring(500,85,28,kek=False)
 import math
 pts=[(500+28*math.sin(math.radians(60*i)),85-28*math.cos(math.radians(60*i))) for i in range(6)]
 for i in (1,4):
  (x1,y1),(x2,y2)=pts[i],pts[(i+1)%6];s+=line(500+(x1-500)*.76,85+(y1-85)*.76,500+(x2-500)*.76,85+(y2-85)*.76)
 for i,dy in ((0,-1),(3,1)):x,y=pts[i];s+=line(x-3,y,x-3,y+dy*16)+line(x+3,y,x+3,y+dy*16)+t(x,y+dy*28+5,'O',15)
 return s+lab(500,166,lang,'p-benzoquinone')+'</svg>'
def aliph(lang):
 import math
 s=F.start(260)
 for x,(f,n) in zip((140,420,690),(('CH₃ – OH','methyl alcohol'),('CH₃ – CH₂ – OH','ethyl alcohol'),('CH₃ – CH₂ – CH₂ – OH','n-propyl alcohol'))):s+=t(x,35,f,16)+lab(x,57,lang,n)
 pts=[(140+30*math.cos(math.radians(-90+72*i)),165+30*math.sin(math.radians(-90+72*i))) for i in range(5)]
 s+='<polygon points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in pts)+'" fill="none" stroke="#222" stroke-width="2"/>'+line(140,135,140,120)+t(140,112,'OH',14)+lab(140,220,lang,'cyclopentanol','(cyclopentyl alcohol)')
 s+=ring(420,165,30,kek=False,subs={0:'OH'})+lab(420,220,lang,'cyclohexanol','(cyclohexyl alcohol)')+ring(690,165,30,kek=False,subs={0:'OH',1:'OH'})+lab(690,220,lang,'cyclohexane-1,2-diol')
 return s+'</svg>'
P,L,B,add,visual=builder()
visual('chem12-p111-phenol-nitration',nitr)
add('With concentrated nitric acid, 2,4,6–trinitrophenol is formed (Section 16.8.5.2.8).','مرتکز نائٹرک ایسڈ کے ساتھ 2،4،6–ٹرائی نائٹرو فینول بنتا ہے (حصہ 16.8.5.2.8)۔','له غلیظ نایټریک اسید سره 2،4،6–ټرای نایټروفینول جوړېږي (برخه 16.8.5.2.8).')
visual('chem12-p111-picric',picric)
add('2. Halogenations','2. ہیلوجینیشن','2. هالوجینېشن','heading')
add('Phenol reacts with excess of halogen in aqueous solution to give 2,4,6–trihalophenol. For example, reaction of phenol with excess of bromine yield a white precipitate of 2,4,6–tribromophenol. The reaction is used for detection of phenol.','فینول آبی محلول میں ہیلوجن کی زیادتی سے تعامل کر کے 2،4،6–ٹرائی ہیلو فینول دیتا ہے۔ مثلاً برومین کی زیادتی سے فینول کا تعامل 2،4،6–ٹرائی برومو فینول کا سفید رسوب دیتا ہے۔ یہ تعامل فینول کی شناخت کے لیے استعمال ہوتا ہے۔','فینول په اوبلن محلول کې له ډېر هالوجن سره تعامل کوي او 2،4،6–ټرای هالوفینول ورکوي. د بېلګې په توګه له ډېر برومین سره د فینول تعامل د 2،4،6–ټرای بروموفینول سپین رسوب ورکوي. دا تعامل د فینول د پېژندلو لپاره کارېږي.')
visual('chem12-p111-tribromophenol',brom)
add('In the presence of a non–polar solvent like, carbon tetrachloride or carbon disulphide, at low temperature, phenol yields a mixture of o- and p-bromophenol. The two isomers differ in boiling point and can be separated by fractional distillation.','کاربن ٹیٹرا کلورائیڈ یا کاربن ڈائی سلفائیڈ جیسے غیر قطبی محلل کی موجودگی میں کم درجہ حرارت پر فینول o- اور p-برومو فینول کا آمیزہ دیتا ہے۔ دونوں آئسومر نقطۂ جوش میں مختلف ہیں اور جزوی کشید سے الگ کیے جا سکتے ہیں۔','د غیر قطبي محلل لکه کاربن ټیټراکلوراید یا کاربن ډای سلفاید په شتون کې په ټیټه تودوخه کې فینول د o- او p-بروموفینول ګډوله ورکوي. دواړه ایزومرونه د ایشېدو په ټکي کې توپیر لري او د جزوي تقطیر په واسطه جلا کېدای شي.')
visual('chem12-p111-monobromination',mono)
add('18.2.7.2 Reaction with Sodium Metal','18.2.7.2 سوڈیم دھات سے تعامل','18.2.7.2 له سوډیم فلز سره تعامل','heading')
add('Phenol, being acidic in nature, reacts with sodium metal to form salt, with the release of hydrogen gas (Section 18.2.4).','فینول تیزابی نوعیت کی وجہ سے سوڈیم دھات سے تعامل کر کے ہائیڈروجن گیس کے اخراج کے ساتھ نمک بناتا ہے (حصہ 18.2.4)۔','فینول د تېزابي طبیعت له امله له سوډیم فلز سره تعامل کوي او د هایدروجن ګاز له ازادېدو سره مالګه جوړوي (برخه 18.2.4).')
r11=section('18.11','Electrophilic substitution of phenol and reaction with sodium','فینول کا الیکٹروفائلی تبادلہ اور سوڈیم سے تعامل','د فینول الکتروفایلي بدلون او له سوډیم سره تعامل',P,L,B,'214')
r11['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':111,'printedPages':[214]}]
P,L,B,add,visual=builder()
visual('chem12-p111-sodium',sodium)
add('18.2.7.3 Oxidation','18.2.7.3 تکسید','18.2.7.3 اکسیډېشن','heading')
add('Phenol is observed to undergo oxidation even more readily than primary and secondary alcohols. The product is benzoquinone. Phenol can be oxidized into p-benzoquinone using dichromate or permanganate.','دیکھا گیا ہے کہ فینول کی تکسید ابتدائی اور ثانوی الکوحلز سے بھی زیادہ آسانی سے ہوتی ہے۔ پیداوار بینزو کوئنون ہے۔ ڈائی کرومیٹ یا پرمینگنیٹ سے فینول کی تکسید p-بینزو کوئنون میں کی جا سکتی ہے۔','لیدل شوي چې فینول حتی له لومړنیو او دویمیو الکولونو په اسانۍ اکسیډایز کېږي. محصول بنزوکینون دی. فینول د ډای کرومېټ یا پرمنګنېټ په کارولو p-بنزوکینون ته اکسیډایز کېدای شي.')
visual('chem12-p111-benzoquinone',quinone)
add('18.2.8 Difference between Alcohol and Phenol','18.2.8 الکوحل اور فینول میں فرق','18.2.8 د الکول او فینول توپیر','heading')
add('In both alcohols and phenols hydroxyl group is the functional group. In phenols hydroxyl group is attached to an aromatic carbon e.g. phenol, cresols, catechol etc. While in alcohols the hydroxyl group is attached to an aliphatic carbon atom. Alcohols are further classified into aliphatic and aromatic. If an alcohol does not contain an aromatic ring, it is called aliphatic alcohol e.g. methyl alcohol, ethyl alcohol, cyclohexanol etc. But alcohols containing hydroxyl group in a side chain attached to an aromatic ring are called aromatic alcohols e.g. benzyl alcohol, 2-phenylethanol etc.',
 'الکوحلز اور فینولز دونوں میں ہائیڈروآکسل گروپ فعلی گروپ ہے۔ فینولز میں ہائیڈروآکسل گروپ ارومیٹک کاربن سے جڑا ہوتا ہے، مثلاً فینول، کریسولز، کیٹیکول وغیرہ۔ جبکہ الکوحلز میں ہائیڈروآکسل گروپ ایلیفیٹک کاربن ایٹم سے جڑا ہوتا ہے۔ الکوحلز کو مزید ایلیفیٹک اور ارومیٹک میں تقسیم کیا جاتا ہے۔ اگر الکوحل میں ارومیٹک حلقہ نہ ہو تو اسے ایلیفیٹک الکوحل کہتے ہیں، مثلاً میتھائل الکوحل، ایتھائل الکوحل، سائیکلوہیکسانول وغیرہ۔ لیکن وہ الکوحلز جن میں ہائیڈروآکسل گروپ ارومیٹک حلقے سے جڑی ضمنی زنجیر میں ہو، ارومیٹک الکوحلز کہلاتے ہیں، مثلاً بینزائل الکوحل، 2-فینائل ایتھانول وغیرہ۔',
 'په الکولونو او فینولونو دواړو کې هایدروکسیل ګروپ فعال ګروپ دی. په فینولونو کې هایدروکسیل ګروپ له اروماتیک کاربن سره تړلی دی، لکه فینول، کریسولونه، کېټیکول او نور. په داسې حال کې چې په الکولونو کې هایدروکسیل ګروپ له الیفاتیک کاربني اټوم سره تړلی دی. الکولونه نور هم په الیفاتیکو او اروماتیکو وېشل کېږي. که الکول اروماتیکه کړۍ ونه لري، الیفاتیک الکول بلل کېږي، لکه میتایل الکول، ایتیل الکول، سایکلوهېکسانول او نور. خو هغه الکولونه چې هایدروکسیل ګروپ یې له اروماتیکې کړۍ سره په تړلي څنګه ځنځیر کې وي، اروماتیک الکولونه بلل کېږي، لکه بنزیل الکول، 2-فینیل ایتانول او نور.')
add('Some examples:','چند مثالیں:','ځینې بېلګې:','heading')
add('Aliphatic alcohols;','ایلیفیٹک الکوحلز؛','الیفاتیک الکولونه؛')
visual('chem12-p111-aliphatic-alcohols',aliph)
r12=section('18.12','Oxidation of phenol and alcohol versus phenol','فینول کی تکسید اور الکوحل بمقابلہ فینول','د فینول اکسیډېشن او الکول د فینول په وړاندې',P,L,B,'215')
r12['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':111,'printedPages':[215]}]
r12['sourceContinuesOnPdfPage']=112
trim=[{'id':'18.13','startsAt':'Aromatic alcohols;'}]
if __name__=='__main__':save(111,[r11,r12],trim=trim,chapter_number=18)
