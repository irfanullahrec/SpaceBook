"""PDF97 printed186–187: reactivity of amines, alkylation, Schiff's bases, amides, diazonium salts."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow97');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Functioning as a base':('اساس کے طور پر کام','د قلوي په توګه عمل'),'Functioning as a nucleophile':('نیوکلیوفائل کے طور پر کام','د نیوکلیوفایل په توګه عمل'),'primary amine':('ابتدائی امائن','لومړنی امین'),
   'secondary amine':('ثانوی امائن','دویمی امین'),'tertiary amine':('ثالثی امائن','درېیمی امین'),'quaternary ammonium salt':('کواٹرنری امونیم نمک','څلورګونې امونیم مالګه'),'1°-amine':('1°-امائن','1°-امین'),
   'aldehyde/ketone':('الڈیہائیڈ/کیٹون','الدیهاید/کیټون'),'N-substituted imine':('N-متبادل امین','N-بدیلي ایمین'),"(a Schiff's base)":('(شف بیس)','(د شیف قلوي)'),'methanamine':('میتھین امائن','میتان امین'),
   '(methyl amine)':('(میتھائل امائن)','(میتایل امین)'),'propanone':('پروپانون','پروپانون'),'(acetone)':('(ایسیٹون)','(اسیتون)'),'N-methylpropan-2-imine':('N-میتھائل پروپین-2-امین','N-میتایل پروپان-2-ایمین'),
   'acid halide':('ایسڈ ہیلائیڈ','اسید هالایډ'),'N-substituted amide':('N-متبادل امائیڈ','N-بدیلي اماید'),'2° -amine':('2°-امائن','2°-امین'),'N,N-disubstituted amide':('N،N-دو متبادل امائیڈ','N،N-دوه بدیلي اماید'),
   '1°–amine':('1°–امائن','1°–امین'),'diazonium salt':('ڈائی ایزونیم نمک','ډای ازونیم مالګه'),'methyl amine':('میتھائل امائن','میتایل امین'),'methanediazonium':('میتھین ڈائی ایزونیم','میتان ډای ازونیم'),'chloride':('کلورائیڈ','کلوراید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def roles(lang):
 s=F.start(140)+'<rect x="20" y="30" width="390" height="100" fill="white" stroke="#222"/><rect x="440" y="30" width="390" height="100" fill="white" stroke="#222"/>'
 s+=t(215,22,lb(lang,'Functioning as a base'),13)+t(635,22,lb(lang,'Functioning as a nucleophile'),13)
 s+=t(70,85,'R₃N:',17)+t(150,80,'H—Cl',15)+F.arrow(120,190,86)+t(290,86,'R₃N⁺—H  Cl⁻',16)
 s+=t(490,85,'R₃N:',17)+t(575,80,'H₃C—Cl',15)+F.arrow(540,615,86)+t(720,86,'R₃N⁺—CH₃  Cl⁻',16)
 return s+'</svg>'
def alkyl(lang):
 s=F.start(230)
 s+=t(110,40,'CH₃—NH₂  +  H₃C—I',16)+t(90,62,lb(lang,'primary amine'),12)+F.arrow(230,300,34)+t(390,40,'(CH₃)NH₂⁺—CH₃  I⁻',16)+F.eq(490,550,34)+t(560,22,':NH₂CH₃',13)+t(680,40,'(CH₃)₂NH',16)+t(680,62,lb(lang,'secondary amine'),12)
 s+=t(110,120,'(CH₃)₂NH  +  H₃C—I',16)+F.arrow(230,300,114)+t(390,120,'(CH₃)₂NH⁺—CH₃  I⁻',16)+F.eq(490,550,114)+t(680,120,'(CH₃)₃N',16)+t(680,142,lb(lang,'tertiary amine'),12)
 s+=t(110,195,'(CH₃)₃N:  +  H₃C—I',16)+F.arrow(230,300,189)+t(420,195,'(CH₃)₄N⁺  I⁻',16)+t(420,217,lb(lang,'quaternary ammonium salt'),12)
 return s+'</svg>'
def carbonyl(x,y,l,r,size=16):return t(x,y-36,'O',14)+line(x-3,y-30,x-3,y-15)+line(x+3,y-30,x+3,y-15)+t(x,y,l+'—C—'+r,size)
def schiff(lang):
 s=F.start(230)
 s+=t(90,60,'R—NH₂  +',16)+t(70,82,lb(lang,'1°-amine'),12)+carbonyl(220,60,'','')+t(220,82,lb(lang,'aldehyde/ketone'),12)+F.eq(300,380,54)+t(340,40,'H⁺',13)
 s+=t(520,22,'N—R',15)+line(517,28,517,44)+line(523,28,523,44)+t(520,60,'—C—',16)+t(640,60,'+ H₂O',16)+t(520,82,lb(lang,'N-substituted imine'),12)+t(520,98,lb(lang,"(a Schiff's base)"),12)
 s+=t(90,170,'CH₃—NH₂  +',16)+t(80,192,lb(lang,'methanamine'),12)+t(80,208,lb(lang,'(methyl amine)'),12)+carbonyl(230,170,'CH₃','CH₃')+t(230,192,lb(lang,'propanone'),12)+t(230,208,lb(lang,'(acetone)'),12)
 s+=F.eq(310,390,164)+t(350,150,'H⁺',13)+t(520,132,'N—CH₃',15)+line(507,138,507,154)+line(513,138,513,154)+t(510,170,'H₃C—C—CH₃',16)+t(660,170,'+ H₂O',16)+t(520,192,lb(lang,'N-methylpropan-2-imine'),12)+t(520,208,lb(lang,"(a Schiff's base)"),12)
 return s+'</svg>'
def amide(lang,second):
 s=F.start(120)
 if second:s+=t(80,30,'R',14)+line(80,36,80,48)+t(90,66,'R—N̈H',16)+t(80,88,lb(lang,'2° -amine'),12)
 else:s+=t(90,66,'R—N̈H₂',16)+t(80,88,lb(lang,'1°-amine'),12)
 s+=t(170,66,'+',16)+carbonyl(250,66,'R','X')+t(250,88,lb(lang,'acid halide'),12)+F.arrow(320,430,60)+carbonyl(540,66,'R','NR₂' if second else 'NHR')+t(660,66,'+ HCl',16)
 s+=t(540,88,lb(lang,'N,N-disubstituted amide' if second else 'N-substituted amide'),12)
 return s+'</svg>'
def diazo(lang):
 s=F.start(150)+t(200,40,'R—NH₂ + NaNO₂ + 2HCl',16)+t(120,62,lb(lang,'1°–amine'),12)+F.arrow(360,440,34)+t(600,40,'R—N₂⁺Cl⁻ + 2H₂O + NaCl',16)+t(560,62,lb(lang,'diazonium salt'),12)
 s+=t(200,110,'CH₃—NH₂ + NaNO₂ + 2HCl',16)+t(120,132,lb(lang,'methyl amine'),12)+F.arrow(360,440,104)+t(620,110,'CH₃—N₂⁺Cl⁻ + 2H₂O + NaCl',16)+t(570,132,lb(lang,'methanediazonium'),12)+t(570,148,lb(lang,'chloride'),12)
 return s.replace('viewBox="0 0 850 150"','viewBox="0 0 850 156"')+'</svg>'

add('17.3.6 Reactivity of Amines','17.3.6 امائنز کی تعامل پذیری','17.3.6 د امینونو تعامل وړتیا','heading')
add('The chemistry of amines is mainly due to the lone pair of electron on nitrogen atom. This lone pair of electrons is available to the electron deficient reagents such as acids and electrophiles. Therefore, they can act as base or nucleophile in reactions. Therefore, common chemical reactions are acid-base reactions, nucleophilic substitution and nucleophilic addition reactions.',
 'امائنز کی کیمیا زیادہ تر نائٹروجن ایٹم پر الیکٹرانوں کے تنہا جوڑے کی وجہ سے ہے۔ یہ تنہا جوڑا تیزابوں اور الیکٹروفائلز جیسے الیکٹرانوں کی کمی والے عاملوں کے لیے دستیاب ہوتا ہے۔ اس لیے یہ تعاملات میں اساس یا نیوکلیوفائل کا کام کر سکتے ہیں۔ چنانچہ عام کیمیائی تعاملات تیزاب–اساس تعاملات، نیوکلیوفائلی تبادلہ اور نیوکلیوفائلی اضافی تعاملات ہیں۔',
 'د امینونو کیمیا اساساً پر نایتروجني اټوم د الکترونونو د یوازینۍ جوړې له امله ده. دا یوازینۍ جوړه د الکترون کمښت لرونکو عاملونو لکه اسیدونو او الکتروفایلونو ته شته ده. نو په تعاملونو کې د قلوي یا نیوکلیوفایل په توګه عمل کولی شي. له همدې امله عام کیمیاوي تعاملونه اسید–قلوي تعاملونه، نیوکلیوفایلي بدلون او نیوکلیوفایلي اضافي تعاملونه دي.')
visual('chem12-p97-amine-roles',roles)
add('17.3.7 Reactions of Amines','17.3.7 امائنز کے تعاملات','17.3.7 د امینونو تعاملونه','heading')
add('17.3.7.1 Overview','17.3.7.1 جائزہ','17.3.7.1 کتنه','heading')
add('Amines are important and reactive organic compounds. These react with a number of different substances to produce valuable organic compounds. Some of their reactions are:','امائنز اہم اور تعامل پذیر نامیاتی مرکبات ہیں۔ یہ کئی مختلف مادوں سے تعامل کر کے قیمتی نامیاتی مرکبات بناتے ہیں۔ ان کے چند تعاملات یہ ہیں:','امینونه مهم او تعامل کوونکي عضوي مرکبات دي. دوی له بېلابېلو موادو سره تعامل کوي او ارزښتناک عضوي مرکبات جوړوي. ځینې تعاملونه یې دا دي:')
add('17.3.7.2 Alkylation of Amines by Alkyl Halides','17.3.7.2 الکائل ہیلائیڈز سے امائنز کی الکائلیشن','17.3.7.2 د الکایل هالایډونو په واسطه د امینونو الکایلېشن','heading')
add('When a primary amine is treated with an alkyl halide, they produce a mixture of secondary, tertiary amines and quaternary ammonium salt. In this process the hydrogen atoms in the amine are successively replaced by the alkyl groups of alkyl halide. This reaction proceeds via SN2 mechanism.',
 'جب ابتدائی امائن کو الکائل ہیلائیڈ سے عمل کرایا جائے تو ثانوی، ثالثی امائنز اور کواٹرنری امونیم نمک کا آمیزہ بنتا ہے۔ اس عمل میں امائن کے ہائیڈروجن ایٹم یکے بعد دیگرے الکائل ہیلائیڈ کے الکائل گروپوں سے بدلتے ہیں۔ یہ تعامل SN2 طریق کار سے ہوتا ہے۔',
 'کله چې لومړنی امین له الکایل هالایډ سره تعامل وکړي، د دویمیو، درېیمیو امینونو او څلورګونې امونیم مالګې ګډوله جوړوي. په دې بهیر کې د امین هایدروجني اټومونه یو په بل پسې د الکایل هالایډ په الکایل ګروپونو بدلېږي. دا تعامل د SN2 میکانیزم له لارې کېږي.')
visual('chem12-p97-amine-alkylation',alkyl)
add('17.3.7.3 Reaction of Amines with Aldehydes and Ketones','17.3.7.3 امائنز کا الڈیہائیڈز اور کیٹونز سے تعامل','17.3.7.3 له الدیهایډونو او کیټونونو سره د امینونو تعامل','heading')
add('Primary amines react with aldehydes and ketones, in the presence of acid catalyst and yield condensation products called N-substituted imines or secondary imines. These imines are also known as Schiff’s bases.',
 'ابتدائی امائنز تیزابی عمل انگیز کی موجودگی میں الڈیہائیڈز اور کیٹونز سے تعامل کر کے تکثیفی پیداواریں دیتے ہیں جنہیں N-متبادل امینز یا ثانوی امینز کہتے ہیں۔ ان امینز کو شف بیسز بھی کہا جاتا ہے۔',
 'لومړني امینونه د اسیدي کتلست په شتون کې له الدیهایډونو او کیټونونو سره تعامل کوي او د تراکم محصولات ورکوي چې N-بدیلي ایمینونه یا دویمي ایمینونه بلل کېږي. دې ایمینونو ته د شیف قلویان هم وايي.')
visual('chem12-p97-schiff',schiff)
add('17.3.7.4 Preparation of Amides','17.3.7.4 امائیڈز کی تیاری','17.3.7.4 د امایډونو جوړول','heading')
add('Primary amine react with acid chloride or acid anhydride to produce a secondary amide (or N-substituted amide).','ابتدائی امائن ایسڈ کلورائیڈ یا ایسڈ این ہائیڈرائیڈ سے تعامل کر کے ثانوی امائیڈ (یا N-متبادل امائیڈ) بناتا ہے۔','لومړنی امین له اسید کلوراید یا اسید انهایدراید سره تعامل کوي او دویمی اماید (یا N-بدیلي اماید) جوړوي.')
visual('chem12-p97-secondary-amide',lambda l:amide(l,False))
add('Secondary amines react with acid halides or anhydrides to produce a tertiary amide (or N,N-disubstituted amide).','ثانوی امائنز ایسڈ ہیلائیڈز یا این ہائیڈرائیڈز سے تعامل کر کے ثالثی امائیڈ (یا N،N-دو متبادل امائیڈ) بناتے ہیں۔','دویمي امینونه له اسید هالایډونو یا انهایدرایډونو سره تعامل کوي او درېیمی اماید (یا N،N-دوه بدیلي اماید) جوړوي.')
visual('chem12-p97-tertiary-amide',lambda l:amide(l,True))
add('As tertiary amines have no hydrogen atom directly attached to the nitrogen, therefore, they donot react with acid chlorides or anhydrides to produce amides.','چونکہ ثالثی امائنز میں نائٹروجن سے براہِ راست کوئی ہائیڈروجن ایٹم جڑا نہیں ہوتا، اس لیے یہ ایسڈ کلورائیڈز یا این ہائیڈرائیڈز سے تعامل کر کے امائیڈز نہیں بناتے۔','څرنګه چې درېیمي امینونه له نایتروجن سره مستقیم تړلی هایدروجني اټوم نه لري، نو له اسید کلورایډونو یا انهایدرایډونو سره تعامل نه کوي چې امایډونه جوړ کړي.')
add('17.3.7.5 Preparation of Diazonium Salts','17.3.7.5 ڈائی ایزونیم نمکیات کی تیاری','17.3.7.5 د ډای ازونیم مالګو جوړول','heading')
add('Diazonium salts are compounds that contain diazonium ion (R/Ar–N₂⁺) as cation. When primary amines are treated with nitrous acid they yield highly unstable salts known as diazonium salts. This reaction is termed as diazotization reaction. Nitrous acid being an unstable acid is prepared in situ by the reaction of sodium nitrite and dilute hydrochloric acid.',
 'ڈائی ایزونیم نمکیات وہ مرکبات ہیں جن میں کیٹائن کے طور پر ڈائی ایزونیم آئن (R/Ar–N₂⁺) ہوتا ہے۔ جب ابتدائی امائنز کو نائٹرس ایسڈ سے عمل کرایا جائے تو یہ انتہائی ناپائیدار نمکیات دیتے ہیں جنہیں ڈائی ایزونیم نمکیات کہتے ہیں۔ اس تعامل کو ڈائی ایزوٹائزیشن تعامل کہا جاتا ہے۔ نائٹرس ایسڈ ناپائیدار تیزاب ہونے کی وجہ سے سوڈیم نائٹرائٹ اور ہلکے ہائیڈروکلورک ایسڈ کے تعامل سے in situ تیار کیا جاتا ہے۔',
 'د ډای ازونیم مالګې هغه مرکبات دي چې د کاټیون په توګه ډای ازونیم ایون (R/Ar–N₂⁺) لري. کله چې لومړني امینونه له نایټرس اسید سره تعامل وکړي، ډېرې بې ثباته مالګې ورکوي چې د ډای ازونیم مالګې بلل کېږي. دې تعامل ته د ډای ازوټایزېشن تعامل وايي. نایټرس اسید د بې ثباته اسید په توګه د سوډیم نایټرایټ او رقیق هایدروکلوریک اسید له تعامل in situ جوړېږي.')
visual('chem12-p97-diazonium',diazo)
record=section('17.13','Reactivity and reactions of amines','امائنز کی تعامل پذیری اور تعاملات','د امینونو تعامل وړتیا او تعاملونه',paras,layout,blocks,'186–187')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':97,'printedPages':[186,187]}]
record['sourceContinuesOnPdfPage']=98
issues=[{'id':'chem12-p186-alkylation-cycle','printedPage':186,'description':'Printed curved-arrow alkylation cycle (primary → secondary → tertiary → quaternary) reconstructed as condensed coded equations; printed "donot" retained.'}]
trim=[{'id':'17.14','startsAt':'Society, Technology And Science'}]
if __name__=='__main__':save(97,[record],trim=trim,issues=issues,chapter_number=17)
