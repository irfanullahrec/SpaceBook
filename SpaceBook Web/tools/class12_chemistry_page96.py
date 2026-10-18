"""PDF96 printed184–185: preparation of amines — alkylation of ammonia, reduction of nitriles, nitroalkanes and amides."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow96');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'ammonia':('امونیا','امونیا'),'methyl amine':('میتھائل امائن','میتایل امین'),'dimethyl amine':('ڈائی میتھائل امائن','ډای میتایل امین'),'trimethyl amine':('ٹرائی میتھائل امائن','ټرای میتایل امین'),
   'quaternary methyl ammomium iodide':('کواٹرنری میتھائل امونیم آئیوڈائیڈ','څلورګوني میتایل امونیم ایوډایډ'),'nitrile':('نائٹرائل','نایټرایل'),'1°–amine':('1°–امائن','1°–امین'),'ethanenitrile':('ایتھین نائٹرائل','ایتان نایټرایل'),
   'ethanamine':('ایتھین امائن','ایتان امین'),'propanenitrile':('پروپین نائٹرائل','پروپان نایټرایل'),'propanamine':('پروپین امائن','پروپان امین'),'nitromethane':('نائٹرو میتھین','نایټرومیتان'),'methanamine':('میتھین امائن','میتان امین'),
   'nitroethane':('نائٹرو ایتھین','نایټروایتان'),'primary amide':('ابتدائی امائیڈ','لومړنی اماید'),'primary amine':('ابتدائی امائن','لومړنی امین'),'secondary amide':('ثانوی امائیڈ','دویمی اماید'),'secondary amine':('ثانوی امائن','دویمی امین'),
   'tertiary amide':('ثالثی امائیڈ','درېیمی اماید'),'tertiary amine':('ثالثی امائن','درېیمی امین')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def ammonia(lang):
 s=F.start(440)
 s+=t(70,74,'H—N̈',16)+t(80,48,'H',14)+line(80,54,80,62)+t(80,108,'H',14)+line(80,86,80,94)+t(160,74,'H₃C—I',15)+f'<path d="M95 62 Q120 40 150 60" fill="none" stroke="#222" stroke-width="1.5" marker-end="url(#arrow96)"/>'+F.arrow(200,260,68)
 s+=t(320,74,'H—N⁺—CH₃',16)+t(340,48,'H',14)+line(340,54,340,62)+t(340,108,'H',14)+line(340,86,340,94)+t(380,108,'I⁻',14)+t(470,40,':N̈H₃',14)+F.eq(420,500,68)+t(580,74,'H—N̈—CH₃',16)+t(575,108,'H',14)+line(575,86,575,94)
 s+=t(70,130,lb(lang,'ammonia'),12)+t(580,130,lb(lang,'methyl amine'),12)
 s+=t(170,185,'CH₃—NH₂ + I—CH₃',16)+t(120,205,lb(lang,'methyl amine'),12)+F.arrow(310,400,179)+t(540,185,'CH₃—NH—CH₃ + HI',16)+t(510,205,lb(lang,'dimethyl amine'),12)
 s+=t(170,250,'CH₃—NH—CH₃ + I—CH₃',16)+t(120,270,lb(lang,'dimethyl amine'),12)+F.arrow(310,400,244)+chain(F,0,250,['CH₃','—','N','—','CH₃','+ HI'],16,None,None,{2:'CH₃'},center=540)+t(520,312,lb(lang,'trimethyl amine'),12)
 s+=chain(F,0,360,['CH₃','—','N','—','CH₃','+ I—CH₃'],16,None,None,{2:'CH₃'},center=170)+t(120,428,lb(lang,'trimethyl amine'),12)+F.arrow(310,400,354)
 s+=t(540,360,'[(CH₃)₄N]⁺ I⁻',17)+t(540,390,lb(lang,'quaternary methyl ammomium iodide'),12)
 return s+'</svg>'
def nitriles(lang):
 s=F.start(230)
 s+=t(170,40,'R — C ≡ N',17)+t(170,62,lb(lang,'nitrile'),12)+F.arrow(300,430,34,'2H₂/Ni or','LiAlH₄ /ether')+t(560,40,'R — CH₂ — NH₂',17)+t(560,62,lb(lang,'1°–amine'),12)
 s+=t(170,120,'CH₃ — C ≡ N',17)+t(170,142,lb(lang,'ethanenitrile'),12)+F.arrow(300,430,114,'1. LiAlH₄ /ether','2. H₂O')+t(560,120,'CH₃ — CH₂ — NH₂',17)+t(560,142,lb(lang,'ethanamine'),12)
 s+=t(170,195,'CH₃—CH₂—C ≡ N + 2H₂',17)+t(170,217,lb(lang,'propanenitrile'),12)+F.arrow(320,430,189,'Ni')+t(570,195,'CH₃—CH₂—CH₂—NH₂',17)+t(570,217,lb(lang,'propanamine'),12)
 return s+'</svg>'
def nitro(lang):
 s=F.start(140)+t(170,40,'CH₃—NO₂ + 3H₂',17)+t(130,62,lb(lang,'nitromethane'),12)+F.arrow(300,400,34,'Ni')+t(560,40,'CH₃—NH₂ + 2H₂O',17)+t(530,62,lb(lang,'methanamine'),12)
 s+=t(170,110,'CH₃—CH₂—NO₂',17)+t(150,132,lb(lang,'nitroethane'),12)+F.arrow(300,400,104,'Fe/HCl')+t(540,110,'CH₃—CH₂—NH₂',17)+t(540,132,lb(lang,'ethanamine'),12)
 return s+'</svg>'
def amides(lang):
 s=F.start(330)
 for i,(g,a,b) in enumerate((('NH₂','primary amide','primary amine'),('NHR','secondary amide','secondary amine'),('NR₂','tertiary amide','tertiary amine'))):
  y=60+105*i;s+=t(190,y-38,'O',15)+line(187,y-32,187,y-16)+line(193,y-32,193,y-16)+t(190,y,'R — C — '+g,17)+t(190,y+24,lb(lang,a),12)
  s+=F.arrow(300,420,y-6,'1. LiAlH₄ /ether','2. H₂O')+t(540,y,'R — CH₂ — '+g,17)+t(540,y+24,lb(lang,b),12)
 return s+'</svg>'

add('17.3.5 Preparation of Amines','17.3.5 امائنز کی تیاری','17.3.5 د امینونو چمتو کول','heading')
add('Amines can be prepared by a number of different methods. Some of these are given below.','امائنز کئی مختلف طریقوں سے تیار کیے جا سکتے ہیں۔ ان میں سے چند درج ذیل ہیں۔','امینونه په څو بېلابېلو طریقو چمتو کېدای شي. ځینې یې لاندې ورکړل شوې.')
add('17.3.5.1 Alkylation of Ammonia by Alkyl halides','17.3.5.1 الکائل ہیلائیڈز سے امونیا کی الکائلیشن','17.3.5.1 د الکایل هالایډونو په واسطه د امونیا الکایلېشن','heading')
add('Ammonia is a very good nucleophile and will readily undergo alkylation when treated with an alkyl halide. When an alkyl halide is heated with alcoholic ammonia, it yields a mixture of primary, secondary, tertiary amines and quaternary ammonium salt. During this reaction the hydrogen atoms of ammonia are replaced by alkyl groups of alkyl halide, therefore, this reaction is also known as alkylation of ammonia. The reaction of ammonia with methyl iodide is given below.',
 'امونیا بہت اچھا نیوکلیوفائل ہے اور الکائل ہیلائیڈ سے عمل کرانے پر آسانی سے الکائلیشن کرتی ہے۔ جب الکائل ہیلائیڈ کو الکوحلی امونیا کے ساتھ گرم کیا جائے تو ابتدائی، ثانوی، ثالثی امائنز اور کواٹرنری امونیم نمک کا آمیزہ حاصل ہوتا ہے۔ اس تعامل میں امونیا کے ہائیڈروجن ایٹم الکائل ہیلائیڈ کے الکائل گروپوں سے بدل جاتے ہیں، اسی لیے اس تعامل کو امونیا کی الکائلیشن بھی کہتے ہیں۔ میتھائل آئیوڈائیڈ سے امونیا کا تعامل نیچے دیا گیا ہے۔',
 'امونیا ډېر ښه نیوکلیوفایل دی او له الکایل هالایډ سره په تعامل کې په اسانۍ الکایلېشن کوي. کله چې الکایل هالایډ له الکولي امونیا سره تود شي، د لومړنیو، دویمیو، درېیمیو امینونو او څلورګوني امونیم مالګې ګډوله ورکوي. په دې تعامل کې د امونیا هایدروجني اټومونه د الکایل هالایډ په الکایل ګروپونو بدلېږي، نو دې تعامل ته د امونیا الکایلېشن هم وايي. له میتایل ایوډایډ سره د امونیا تعامل لاندې ورکړل شوی.')
visual('chem12-p96-ammonia-alkylation',ammonia)
add('If the quaternary ammonium salt is the desired product, then an excess of the alkyl halide is used.','اگر کواٹرنری امونیم نمک مطلوبہ پیداوار ہو تو الکائل ہیلائیڈ کی زیادتی استعمال کی جاتی ہے۔','که څلورګونې امونیم مالګه مطلوب محصول وي، نو د الکایل هالایډ زیاته اندازه کارول کېږي.')
add('17.3.5.2 Reduction of Nitrogen Containing Functional Groups','17.3.5.2 نائٹروجن والے فعلی گروپوں کی تخفیف','17.3.5.2 د نایتروجن لرونکو فعالو ګروپونو ارجاع','heading')
add('17.3.5.2.1 Reduction of Nitriles','17.3.5.2.1 نائٹرائلز کی تخفیف','17.3.5.2.1 د نایټرایلونو ارجاع','heading')
add('When nitriles are reduced they yield the corresponding primary amines. This reduction can be brought about by hydrogen in the presence of catalyst such as Ni, Pt or Pd (catalytic hydrogenation) or by lithium aluminum hydride in ether, followed by workup.',
 'نائٹرائلز کی تخفیف سے متعلقہ ابتدائی امائنز حاصل ہوتے ہیں۔ یہ تخفیف Ni، Pt یا Pd جیسے عمل انگیز کی موجودگی میں ہائیڈروجن (عمل انگیز ہائیڈروجینیشن) سے یا ایتھر میں لیتھیم ایلومینیم ہائیڈرائیڈ اور اس کے بعد ورک اپ سے کی جا سکتی ہے۔',
 'کله چې نایټرایلونه ارجاع شي، اړوند لومړني امینونه ورکوي. دا ارجاع د Ni، Pt یا Pd په څېر کتلست په شتون کې د هایدروجن (کتلستي هایدروجینېشن) په واسطه یا په ایتر کې د لیتیم المونیم هایدراید او ورپسې ورک اپ په واسطه ترسره کېدای شي.')
visual('chem12-p96-nitriles',nitriles)
add('17.3.5.2.2 Reduction of Nitroalkanes','17.3.5.2.2 نائٹرو الکینز کی تخفیف','17.3.5.2.2 د نایټروالکانونو ارجاع','heading')
add('Primary amines are prepared by the reduction of nitroalkanes with hydrogen in the presence of Ni or Pt or Pd catalyst. They can also be reduced by Fe or Sn in hydrochloric acid.','ابتدائی امائنز Ni یا Pt یا Pd عمل انگیز کی موجودگی میں ہائیڈروجن سے نائٹرو الکینز کی تخفیف کر کے تیار کیے جاتے ہیں۔ ان کی تخفیف ہائیڈروکلورک ایسڈ میں Fe یا Sn سے بھی کی جا سکتی ہے۔','لومړني امینونه د Ni یا Pt یا Pd کتلست په شتون کې له هایدروجن سره د نایټروالکانونو د ارجاع په واسطه جوړېږي. دوی په هایدروکلوریک اسید کې د Fe یا Sn په واسطه هم ارجاع کېدای شي.')
visual('chem12-p96-nitroalkanes',nitro)
add('17.3.5.2.3 Reduction of Amides','17.3.5.2.3 امائیڈز کی تخفیف','17.3.5.2.3 د امایډونو ارجاع','heading')
add('Amines are obtained when amides are reduced by lithium aluminum hydride in ether. Primary, secondary and tertiary amides yield corresponding primary, secondary and tertiary amines respectively.','جب امائیڈز کی ایتھر میں لیتھیم ایلومینیم ہائیڈرائیڈ سے تخفیف کی جائے تو امائنز حاصل ہوتے ہیں۔ ابتدائی، ثانوی اور ثالثی امائیڈز بالترتیب متعلقہ ابتدائی، ثانوی اور ثالثی امائنز دیتے ہیں۔','کله چې امایډونه په ایتر کې د لیتیم المونیم هایدراید په واسطه ارجاع شي، امینونه ترلاسه کېږي. لومړني، دویمي او درېیمي امایډونه په ترتیب سره اړوند لومړني، دویمي او درېیمي امینونه ورکوي.')
visual('chem12-p96-amides',amides)
record=section('17.12','Preparation of amines','امائنز کی تیاری','د امینونو چمتو کول',paras,layout,blocks,'184–185')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':96,'printedPages':[184,185]}]
record['sourceContinuesOnPdfPage']=97
issues=[{'id':'chem12-p184-ammomium','printedPage':184,'description':'Printed "quaternary methyl ammomium iodide" retained in English.'}]
trim=[{'id':'17.13','startsAt':'17.3.6 |Reactivity of Amines'}]
if __name__=='__main__':save(96,[record],trim=trim,issues=issues,chapter_number=17)
