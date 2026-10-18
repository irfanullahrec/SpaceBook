"""PDF77 printed146–147: side-chain chlorination of toluene, electrophilic aromatic substitution mechanism, nitration."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow77');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'toluene':('ٹولوئین','تولوین'),'benzyl chloride':('بینزائل کلورائیڈ','بنزیل کلوراید'),'benzal chloride':('بینزل کلورائیڈ','بنزال کلوراید'),'benzotrichloride':('بینزو ٹرائی کلورائیڈ','بنزوټرای کلوراید'),
   'benzene':('بینزین','بنزین'),'substituted product':('متبادل پیداوار','بدیل محصول'),'catalyst':('عمل انگیز','کتلست'),'electrophile':('الیکٹروفائل','الکتروفایل'),
   '(slow)':('(سست)','(ورو)'),'(fast)':('(تیز)','(چټک)'),'arenium ion':('ایرینیم آئن','ارینیم ایون'),'substitution product':('تبادلے کی پیداوار','د بدلون محصول'),
   'nitrobenzene':('نائٹرو بینزین','نایټروبنزین'),'o-nitrotoluene (63%)':('o-نائٹرو ٹولوئین (63%)','o-نایټروتولوین (63%)'),'m-nitrotoluene (3%)':('m-نائٹرو ٹولوئین (3%)','m-نایټروتولوین (3%)'),
   'p-nitrotoluene (34%)':('p-نائٹرو ٹولوئین (34%)','p-نایټروتولوین (34%)'),'U.V.light':('بالائے بنفشی روشنی','ماورای بنفش رڼا')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def P(cx,cy,r):return [(cx+r*math.sin(math.radians(60*i)),cy-r*math.cos(math.radians(60*i))) for i in range(6)]
def ring(cx,cy,r=28,dbl=(0,2,4),circle=False,subs=None):
 s=F.ring(cx,cy,r,kek=False,circle=circle,subs=subs);pts=P(cx,cy,r)
 for i in dbl:
  (x1,y1),(x2,y2)=pts[i],pts[(i+1)%6];k=.76;s+=line(cx+(x1-cx)*k,cy+(y1-cy)*k,cx+(x2-cx)*k,cy+(y2-cy)*k)
 return s
def arenium(cx,cy,dbl,plus_v,r=28):
 """sp3 carbon at vertex 1 bearing H (up) and E (right); ⊕ near vertex plus_v."""
 s=ring(cx,cy,r,dbl);pts=P(cx,cy,r);x,y=pts[1]
 s+=line(x,y,x+8,y-20,1.5)+t(x+12,y-24,'H',14)+line(x,y,x+20,y+6,1.5)+t(x+30,y+12,'E',14)
 px,py=pts[plus_v];s+=t(cx+(px-cx)*.55,cy+(py-cy)*.55+5,'⊕',14)
 return s
def sidechain(lang):
 s=F.start(160)
 s+=ring(70,85,28,subs={0:'CH₃'})+t(70,140,lb(lang,'toluene'),13)+t(130,92,'+ Cl₂',17)+F.arrow(165,245,85,lb(lang,'U.V.light'),'−HCl',12)
 for k,(sub,name) in enumerate((('CH₂Cl','benzyl chloride'),('CHCl₂','benzal chloride'),('CCl₃','benzotrichloride'))):
  x=300+k*200;s+=ring(x,85,28,subs={0:sub})+t(x,140,lb(lang,name),13)
  if k<2:s+=F.arrow(x+45,x+150,85,'Cl₂','−HCl',12)
 return s+'</svg>'
def general(lang):
 s=F.start(130)+ring(150,65,28,subs={1:'H'})+t(150,120,lb(lang,'benzene'),13)+t(235,72,'+ E — B',18)
 s+=F.arrow(290,410,65,lb(lang,'catalyst'))+ring(490,65,28,subs={1:'E'})+t(490,120,lb(lang,'substituted product'),13)+t(600,72,'+ H — B',18)
 return s+'</svg>'
def step1(lang):
 return F.start(70)+t(200,35,'E — B + '+lb(lang,'catalyst'),18)+F.arrow(320,470,29)+t(600,35,'E⁺ + B⁻'+lb(lang,'catalyst'),18)+t(530,60,lb(lang,'electrophile'),13)+'</svg>'
def step2(lang):
 s=F.start(130)+ring(180,62,28)+t(180,118,lb(lang,'benzene'),13)+t(260,69,'+ E⁺',18)
 s+=f'<path d="M190 30 Q240 0 255 48" fill="none" stroke="#222" stroke-width="1.5" marker-end="url(#arrow77)"/>'
 s+=F.arrow(300,430,62,lb(lang,'(slow)'))+arenium(520,62,(3,5),2)+t(520,118,lb(lang,'arenium ion'),13)
 return s+'</svg>'
def hybrid(lang):
 s=F.start(110)
 for k,(dbl,pv) in enumerate((((3,5),2),((2,5),4),((2,4),0))):
  x=180+k*240;s+=arenium(x,55,dbl,pv)
  if k<2:s+=t(x+120,62,'⟷',22)
 return s+'</svg>'
def step3(lang):
 s=F.start(130)+arenium(170,60,(3,5),2)+t(170,118,lb(lang,'arenium ion'),13)
 s+=F.arrow(270,400,60,'B⁻'+lb(lang,'catalyst'),lb(lang,'(fast)'))+ring(480,60,28,subs={1:'E'})+t(480,118,lb(lang,'substitution product'),13)+t(650,67,'+ H–B + '+lb(lang,'catalyst'),17)
 return s+'</svg>'
def nitration(lang):
 s=F.start(125)+ring(180,60,28)+t(180,115,lb(lang,'benzene'),13)+t(270,67,'+ HNO₃',18)
 s+=F.arrow(320,430,60,'H₂SO₄','60°C')+ring(510,60,28,subs={1:'NO₂'})+t(510,115,lb(lang,'nitrobenzene'),13)+t(620,67,'+ H₂O',18)
 return s+'</svg>'
def nitrotoluene(lang):
 s=F.start(190)+ring(70,90,28,subs={0:'CH₃'})+t(70,145,lb(lang,'toluene'),13)
 s+=line(120,90,215,90,2,'#222','marker-end="url(#arrow77)"')+t(167,80,'HNO₃',13)+t(167,106,'H₂SO₄',13)+t(167,124,'−H₂O',13)
 for k,(sub,name) in enumerate((({0:'CH₃',1:'NO₂'},'o-nitrotoluene (63%)'),({0:'CH₃',2:'NO₂'},'m-nitrotoluene (3%)'),({0:'CH₃',3:'NO₂'},'p-nitrotoluene (34%)'))):
  x=300+k*200;s+=ring(x,80,28,subs=sub)+t(x,165 if k==2 else 145,lb(lang,name),13)
  if k<2:s+=t(x+100,85,'+',20)
 return s+'</svg>'

add('However, when halogen is treated with toluene in the presence of ultraviolet light, halogenation occurs at aliphatic side chain (methyl group) to yield successively, benzyl chloride, benzal chloride and benzo trichloride. The reaction follow free radical substitution mechanism (Section 16.3), instead of addition.',
 'تاہم جب ٹولوئین کو بالائے بنفشی روشنی کی موجودگی میں ہیلوجن سے عمل کرایا جائے تو ہیلوجینیشن ایلیفیٹک ضمنی زنجیر (میتھائل گروپ) پر ہوتی ہے اور یکے بعد دیگرے بینزائل کلورائیڈ، بینزل کلورائیڈ اور بینزو ٹرائی کلورائیڈ بنتے ہیں۔ یہ تعامل اضافے کے بجائے آزاد ریڈیکل تبادلے کے طریق کار (حصہ 16.3) پر چلتا ہے۔',
 'خو کله چې تولوین د ماورای بنفش رڼا په شتون کې له هالوجن سره تعامل وکړي، هالوجینېشن په الیفاتیکه څنګه ځنځیر (میتایل ګروپ) کې کېږي او یو په بل پسې بنزیل کلوراید، بنزال کلوراید او بنزوټرای کلوراید جوړوي. دا تعامل د اضافې پر ځای د ازاد رادیکال د بدلون میکانیزم (برخه 16.3) تعقیبوي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('The name Benzene hexachloride (BHC) is incorrectly used for 1,2,3,4,5,6–hexachlorocyclohexane. The most important isomer for commercial purposes is the Lindane, which is used in shampoos to kill head lice.',
 'نام بینزین ہیکسا کلورائیڈ (BHC) غلط طور پر 1،2،3،4،5،6–ہیکسا کلورو سائیکلوہیکسین کے لیے استعمال ہوتا ہے۔ تجارتی مقاصد کے لیے سب سے اہم آئسومر لنڈین ہے، جو سر کی جوئیں مارنے کے لیے شیمپو میں استعمال ہوتا ہے۔',
 'د بنزین هېکسا کلوراید (BHC) نوم په ناسم ډول د 1،2،3،4،5،6–هېکسا کلوروسایکلوهېکسان لپاره کارېږي. د سوداګریزو موخو لپاره تر ټولو مهم ایزومر لینډېن دی، چې د سر د سپږو د وژلو لپاره په شامپوګانو کې کارېږي.')
visual('chem12-p77-toluene-side-chain',sidechain)
add('16.8.5.2 Electrophilic Aromatic Substitution Reactions','16.8.5.2 الیکٹروفائلی ارومیٹک تبادلے کے تعاملات','16.8.5.2 الکتروفایلي اروماتیک بدلون تعاملونه','heading')
add('16.8.5.2.1 General Introduction','16.8.5.2.1 عمومی تعارف','16.8.5.2.1 عمومي پېژندنه','heading')
add('Reaction in which hydrogen atom of the aromatic ring is replaced by an electrophile is called electrophilic aromatic substitution reaction. Benzene ring with its delocalized pi electrons is an electron rich system. It is attacked by electrophiles giving substituted products. A generalized electrophilic substitution reaction is shown below. The catalysts most commonly used are acids.',
 'وہ تعامل جس میں ارومیٹک حلقے کا ہائیڈروجن ایٹم الیکٹروفائل سے بدل جائے، الیکٹروفائلی ارومیٹک تبادلے کا تعامل کہلاتا ہے۔ اپنے غیر مقامی پائی الیکٹرانوں کے ساتھ بینزین حلقہ الیکٹرانوں سے بھرپور نظام ہے۔ اس پر الیکٹروفائل حملہ کرتے ہیں اور متبادل پیداواریں بنتی ہیں۔ ایک عمومی الیکٹروفائلی تبادلے کا تعامل نیچے دکھایا گیا ہے۔ سب سے زیادہ استعمال ہونے والے عمل انگیز تیزاب ہیں۔',
 'هغه تعامل چې پکې د اروماتیکې کړۍ هایدروجني اټوم په الکتروفایل بدل شي، الکتروفایلي اروماتیک بدلون تعامل بلل کېږي. د بنزین کړۍ له خپلو غیر ځایي پای الکترونونو سره له الکترونونو ډک سیستم دی. الکتروفایلونه پرې برید کوي او بدیل لرونکي محصولات ورکوي. یو عمومي الکتروفایلي بدلون تعامل لاندې ښودل شوی. تر ټولو ډېر کارېدونکي کتلستونه اسیدونه دي.')
visual('chem12-p77-general-eas',general)
add('Mechanism of electrophilic aromatic substitution reaction involves the following three steps.','الیکٹروفائلی ارومیٹک تبادلے کے تعامل کے طریق کار میں درج ذیل تین مراحل شامل ہیں۔','د الکتروفایلي اروماتیک بدلون تعامل میکانیزم لاندې درې پړاوونه لري.')
add('Step–1: Formation of an electrophile','مرحلہ–1: الیکٹروفائل کی تشکیل','پړاو–1: د الکتروفایل جوړېدل')
visual('chem12-p77-step1',step1)
add('Step–2: The electrophile attacks the aromatic ring to produce a non-aromatic carbocation called arenium ion or sigma-complex.','مرحلہ–2: الیکٹروفائل ارومیٹک حلقے پر حملہ کر کے ایک غیر ارومیٹک کاربوکیٹائن بناتا ہے جسے ایرینیم آئن یا سگما-کمپلیکس کہتے ہیں۔','پړاو–2: الکتروفایل پر اروماتیکې کړۍ برید کوي او یو غیر اروماتیک کاربوکاټیون جوړوي چې ارینیم ایون یا سیګما-کمپلېکس بلل کېږي.')
visual('chem12-p77-step2',step2)
add('The intermediate arenium ion is resonance stabilized and is a hybrid of the following three structures. This resonance-stabilized carbocation is called a sigma-complex because the electrophile is joined to the benzene ring by a new sigma-bond.',
 'درمیانی ایرینیم آئن ریزونینس سے پائیدار ہے اور درج ذیل تین ساختوں کا ہائبرڈ ہے۔ اس ریزونینس سے پائیدار کاربوکیٹائن کو سگما-کمپلیکس کہتے ہیں کیونکہ الیکٹروفائل ایک نئے سگما-بند کے ذریعے بینزین حلقے سے جڑ جاتا ہے۔',
 'منځنی ارینیم ایون د ریزونانس له لارې ثابت دی او د لاندې دریو جوړښتونو هایبرېډ دی. دې ریزونانس ثابت کاربوکاټیون ته سیګما-کمپلېکس وايي ځکه چې الکتروفایل د یوه نوي سیګما-تړون په واسطه د بنزین له کړۍ سره نښلي.')
visual('chem12-p77-arenium-hybrid',hybrid)
add('Step–3: The intermediate arenium ion is non-aromatic species and is unstable. It loses a proton to form a stable aromatic substitution product.','مرحلہ–3: درمیانی ایرینیم آئن غیر ارومیٹک نوع ہے اور ناپائیدار ہے۔ یہ ایک پروٹان کھو کر پائیدار ارومیٹک تبادلے کی پیداوار بناتا ہے۔','پړاو–3: منځنی ارینیم ایون غیر اروماتیک ډول دی او بې ثباته دی. یو پروټون له لاسه ورکوي او ثابت اروماتیک بدلون محصول جوړوي.')
visual('chem12-p77-step3',step3)
add('The overall reaction is the substitution of a proton by an electrophile on the aromatic ring: electrophilic aromatic substitution.','مجموعی تعامل ارومیٹک حلقے پر پروٹان کا الیکٹروفائل سے تبادلہ ہے: الیکٹروفائلی ارومیٹک تبادلہ۔','ټول تعامل پر اروماتیکې کړۍ د پروټون د الکتروفایل په واسطه بدلون دی: الکتروفایلي اروماتیک بدلون.')
add('16.8.5.2.2 Nitration','16.8.5.2.2 نائٹریشن','16.8.5.2.2 نایټرېشن','heading')
add('Benzene reacts with concentrated nitric acid in the presence of concentrated sulphuric acid at 60°C to form nitrobenzene.','بینزین مرتکز سلفیورک ایسڈ کی موجودگی میں 60°C پر مرتکز نائٹرک ایسڈ سے تعامل کر کے نائٹرو بینزین بناتی ہے۔','بنزین په 60°C کې د غلیظ سلفوریک اسید په شتون کې له غلیظ نایټریک اسید سره تعامل کوي او نایټروبنزین جوړوي.')
visual('chem12-p77-nitration',nitration)
add('While nitration of toluene in above conditions yield a mixture of isomeric o-,m- and p–nitrotoluene, in unequal proportions. The ortho and para products predominate, while very little meta product is obtained due to ortho/para orienting effect of methyl group (see Section 16.8.5.2.7).',
 'جبکہ انہی شرائط میں ٹولوئین کی نائٹریشن سے ہم ترکیب o-، m- اور p–نائٹرو ٹولوئین کا آمیزہ غیر مساوی تناسب میں حاصل ہوتا ہے۔ اورتھو اور پیرا پیداواریں غالب ہوتی ہیں، جبکہ میتھائل گروپ کے اورتھو/پیرا سمت دینے والے اثر (دیکھیے حصہ 16.8.5.2.7) کی وجہ سے میٹا پیداوار بہت کم حاصل ہوتی ہے۔',
 'په داسې حال کې چې په پورته شرایطو کې د تولوین نایټرېشن د ایزومري o-، m- او p–نایټروتولوین ګډوله په نابرابرو تناسبونو ورکوي. اورتو او پارا محصولات غالب دي، خو د میتایل ګروپ د اورتو/پارا لوري ورکوونکي اغېز (وګورئ برخه 16.8.5.2.7) له امله ډېر لږ میټا محصول ترلاسه کېږي.')
visual('chem12-p77-nitrotoluenes',nitrotoluene)
add('In case of nitration, the electrophile is nitronium ion, produced by reaction of concentrated nitric and sulfuric acid. The electrophile nitronium ion attacks on benzene ring and forms substitution products via arenium ion intermediate (Section 16.8.5.2.1).',
 'نائٹریشن میں الیکٹروفائل نائٹرونیم آئن ہے، جو مرتکز نائٹرک اور سلفیورک ایسڈ کے تعامل سے بنتا ہے۔ الیکٹروفائل نائٹرونیم آئن بینزین حلقے پر حملہ کرتا ہے اور ایرینیم آئن درمیانی کے ذریعے تبادلے کی پیداواریں بناتا ہے (حصہ 16.8.5.2.1)۔',
 'د نایټرېشن په حالت کې الکتروفایل نایټرونیم ایون دی، چې د غلیظ نایټریک او سلفوریک اسید له تعامل جوړېږي. الکتروفایل نایټرونیم ایون د بنزین پر کړۍ برید کوي او د ارینیم ایون د منځني له لارې بدلون محصولات جوړوي (برخه 16.8.5.2.1).')

record=section('16.24','Side-chain halogenation, electrophilic substitution mechanism and nitration','ضمنی زنجیر کی ہیلوجینیشن، الیکٹروفائلی تبادلے کا طریق کار اور نائٹریشن','د څنګه ځنځیر هالوجینېشن، د الکتروفایلي بدلون میکانیزم او نایټرېشن',paras,layout,blocks,'146–147')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':77,'printedPages':[146,147]}]
record['sourceContinuesOnPdfPage']=78
issues=[]
carry=[{'from':'16.24','to':'16.25','startsAt':'HNO, + 2H2SO'}]
if __name__=='__main__':save(77,[record],carry=carry,issues=issues,chapter_number=16)
