"""PDF117 printed226–227: Unit 19 introduction, carbonyl group, nomenclature of aldehydes."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain,carbonyl
import class12_chemistry_rings as _R
ring=lambda f,*a,**k:f.ring(*a,**k)
F=Fig('arrow117');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'carbonyl group':('کاربونل گروپ','کاربونیل ګروپ'),'formaldehyde':('فارم الڈیہائیڈ','فورمالدیهاید'),'higher aldehydes':('بڑے الڈیہائیڈز','لوړ الدیهایډونه'),'ketones':('کیٹونز','کیټونونه'),
   'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'propionaldehyde':('پروپیون الڈیہائیڈ','پروپیون الدیهاید'),'butyraldehyde':('بیوٹائر الڈیہائیڈ','بیوټیرالدیهاید'),'benzaldehyde':('بینز الڈیہائیڈ','بنزالدیهاید'),
   'α–methyl butyraldehyde':('α–میتھائل بیوٹائر الڈیہائیڈ','α–میتایل بیوټیرالدیهاید'),'β–bromo butyraldehyde':('β–برومو بیوٹائر الڈیہائیڈ','β–برومو بیوټیرالدیهاید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def group(lang):return F.start(90)+C(425,60)+t(425,84,lb(lang,'carbonyl group'),12)+'</svg>'
def classes(lang):
 s=F.start(100)
 for x,(l,r,n) in zip((120,320,520,720),(('','','carbonyl group'),('H','H','formaldehyde'),('R','H','higher aldehydes'),('R',"R′",'ketones'))):s+=C(x,60,l,r)+t(x,84,lb(lang,n),12)
 return s+'</svg>'
def common(lang):
 s=F.start(250)
 s+=C(150,60,'H','H')+t(150,84,lb(lang,'formaldehyde'),12)+C(420,60,'CH₃','H')+t(420,84,lb(lang,'acetaldehyde'),12)+C(690,60,'CH₃—CH₂','H')+t(690,84,lb(lang,'propionaldehyde'),12)
 s+=C(250,170,'CH₃—CH₂—CH₂','H')+t(250,194,lb(lang,'butyraldehyde'),12)+ring(F,600,190,26)+line(600,164,600,150)+t(615,140,'C—H',15)+line(597,104,597,120)+line(603,104,603,120)+t(600,98,'O',14)+t(600,236,lb(lang,'benzaldehyde'),12)
 s+=t(0,0,'',1)
 return s+'</svg>'
def greek(lang):
 s=F.start(140)+chain(F,0,70,['CH₃','—','CH₂','—','CH','—','C','—','H'],15,{0:'γ',2:'β',4:'α'},{6:'=O'},{4:'CH₃'},center=220)+t(220,130,lb(lang,'α–methyl butyraldehyde'),12)
 s+=chain(F,0,70,['CH₃','—','CH','—','CH₂','—','C','—','H'],15,None,{2:'Br',6:'=O'},center=620)+t(560,92,'γ',11)+t(620,92,'β',11)+t(668,92,'α',11)+t(620,120,lb(lang,'β–bromo butyraldehyde'),12)
 return s+'</svg>'
def ex(lang):return F.start(80)+C(180,60,'H','H')+C(425,60,'CH₃','H')+C(680,60,'CH₃—CH₂','H')+'</svg>'

add('Introduction','تعارف','پېژندنه','heading')
add('Some important classes of organic compounds like aldehydes, ketones, carboxylic acids, esters, amides, acid halides and acid anhydrides contain a group called carbonyl group (shown below), and are therefore called carbonyl compounds. Many of these compounds are important commercially and in biological processes. In addition to their uses as reagents and solvents, they are constituents of fabrics, flavorings, plastics, and drugs. Naturally occurring carbonyl compounds include proteins, carbohydrates and nucleic acids which constitute major portion of plants and animals body.',
 'نامیاتی مرکبات کی بعض اہم جماعتوں جیسے الڈیہائیڈز، کیٹونز، کاربوکسیلک ایسڈز، ایسٹرز، امائیڈز، ایسڈ ہیلائیڈز اور ایسڈ این ہائیڈرائیڈز میں ایک گروپ ہوتا ہے جسے کاربونل گروپ کہتے ہیں (نیچے دکھایا گیا ہے)، اس لیے انہیں کاربونل مرکبات کہا جاتا ہے۔ ان میں سے بہت سے مرکبات تجارتی طور پر اور حیاتیاتی عملوں میں اہم ہیں۔ عاملین اور محللات کے طور پر استعمال کے علاوہ یہ کپڑوں، ذائقوں، پلاسٹک اور ادویات کے اجزا ہیں۔ قدرتی طور پر پائے جانے والے کاربونل مرکبات میں پروٹینز، کاربوہائیڈریٹس اور نیوکلیئک ایسڈز شامل ہیں جو پودوں اور جانوروں کے جسم کا بڑا حصہ ہیں۔',
 'د عضوي مرکباتو ځینې مهم ټولګي لکه الدیهایډونه، کیټونونه، کاربوکسیلیک اسیدونه، ایسټرونه، امایډونه، اسید هالایډونه او اسید انهایدرایډونه یو ګروپ لري چې کاربونیل ګروپ بلل کېږي (لاندې ښودل شوی)، نو له همدې امله کاربونیل مرکبات بلل کېږي. ډېر دا مرکبات په سوداګرۍ او بیولوژیکي بهیرونو کې مهم دي. د عاملونو او محللونو په توګه له کارونې سربېره، د ټوکرونو، خوندونو، پلاستیکونو او درملو برخې دي. په طبیعي ډول موندل کېدونکي کاربونیل مرکبات پروټینونه، کاربوهایدریټونه او نیوکلیک اسیدونه رانغاړي چې د نباتاتو او ژویو د بدن لویه برخه جوړوي.')
add('A carbonyl group is a functional group which is composed of a carbon atom doubly bonded to an oxygen atom.','کاربونل گروپ ایک فعلی گروپ ہے جو آکسیجن ایٹم سے دوہرے بند کے ذریعے جڑے کاربن ایٹم پر مشتمل ہے۔','کاربونیل ګروپ یو فعال ګروپ دی چې له یوه کاربني اټوم څخه جوړ دی چې له اکسیجني اټوم سره په دوه ګوني تړون تړلی دی.')
visual('chem12-p117-carbonyl-group',group)
add('The simplest carbonyl compounds are ketones and aldehydes. A ketone has two alkyl (or aryl) groups bonded to the carbonyl carbon atom. An aldehyde has one alkyl (or aryl) group and one hydrogen atom bonded to the carbonyl carbon atom. The functional group of aldehyde, which is carbonyl group along with one hydrogen (–CHO), is also called formyl group. Formaldehyde is the simplest aldehyde, with two hydrogen atoms bonded to the carbonyl group.',
 'سب سے سادہ کاربونل مرکبات کیٹونز اور الڈیہائیڈز ہیں۔ کیٹون میں کاربونل کاربن ایٹم سے دو الکائل (یا ایرائل) گروپ جڑے ہوتے ہیں۔ الڈیہائیڈ میں کاربونل کاربن ایٹم سے ایک الکائل (یا ایرائل) گروپ اور ایک ہائیڈروجن ایٹم جڑا ہوتا ہے۔ الڈیہائیڈ کا فعلی گروپ، یعنی ایک ہائیڈروجن کے ساتھ کاربونل گروپ (–CHO)، فارمائل گروپ بھی کہلاتا ہے۔ فارم الڈیہائیڈ سب سے سادہ الڈیہائیڈ ہے جس میں کاربونل گروپ سے دو ہائیڈروجن ایٹم جڑے ہوتے ہیں۔',
 'تر ټولو ساده کاربونیل مرکبات کیټونونه او الدیهایډونه دي. کیټون له کاربونیل کاربني اټوم سره دوه الکایل (یا اریل) ګروپونه لري. الدیهاید له کاربونیل کاربني اټوم سره یو الکایل (یا اریل) ګروپ او یو هایدروجني اټوم لري. د الدیهاید فعال ګروپ، چې له یوه هایدروجن سره کاربونیل ګروپ (–CHO) دی، فورمیل ګروپ هم بلل کېږي. فورمالدیهاید تر ټولو ساده الدیهاید دی چې له کاربونیل ګروپ سره دوه هایدروجني اټومونه لري.')
visual('chem12-p117-carbonyl-classes',classes)
add('If the two alkyl groups attached to carbonyl carbon are the same the ketone is called symmetrical and if different, it is called unsymmetrical ketone. Instead of alkyl, aryl group(s) can also be attached to carbonyl carbon, in aromatic aldehydes and ketones.','اگر کاربونل کاربن سے جڑے دونوں الکائل گروپ یکساں ہوں تو کیٹون متشاکل اور اگر مختلف ہوں تو غیر متشاکل کیٹون کہلاتا ہے۔ ارومیٹک الڈیہائیڈز اور کیٹونز میں الکائل کے بجائے ایرائل گروپ بھی کاربونل کاربن سے جڑ سکتے ہیں۔','که له کاربونیل کاربن سره تړلي دوه الکایل ګروپونه یو شان وي، کیټون متناظر او که بېل وي، نامتناظر کیټون بلل کېږي. په اروماتیکو الدیهایډونو او کیټونونو کې د الکایل پر ځای اریل ګروپ(ونه) هم له کاربونیل کاربن سره تړل کېدای شي.')
add('19.1 Nomenclature','19.1 نام گذاری','19.1 نومول','heading')
add('Two types of naming systems are used for naming aldehydes and ketones. Common system and IUPAC system.','الڈیہائیڈز اور کیٹونز کے نام رکھنے کے لیے دو نظام استعمال ہوتے ہیں: عام نظام اور IUPAC نظام۔','د الدیهایډونو او کیټونونو د نومولو لپاره دوه سیستمونه کارېږي: عام سیستم او IUPAC سیستم.')
add('19.1.1 Nomenclature of Aldehydes','19.1.1 الڈیہائیڈز کی نام گذاری','19.1.1 د الدیهایډونو نومول','heading')
add('a. Common System','a. عام نظام','a. عام سیستم','heading')
add('Common names of aldehydes are derived from the common names of carboxylic acids containing the same number of carbon atoms (Section 20.1). While naming aldehydes in this system, the ending “-ic acid” in the common name of corresponding carboxylic acid is replaced by the word “-aldehyde”.','الڈیہائیڈز کے عام نام اتنے ہی کاربن ایٹموں والے کاربوکسیلک ایسڈز کے عام ناموں سے اخذ کیے جاتے ہیں (حصہ 20.1)۔ اس نظام میں الڈیہائیڈز کا نام رکھتے وقت متعلقہ کاربوکسیلک ایسڈ کے عام نام کا اختتامیہ ”-ic acid“ لفظ ”-aldehyde“ سے بدل دیا جاتا ہے۔','د الدیهایډونو عام نومونه د ورته شمېر کاربني اټومونو لرونکو کاربوکسیلیک اسیدونو له عامو نومونو اخیستل کېږي (برخه 20.1). په دې سیستم کې د الدیهایډونو د نومولو پر مهال د اړوند کاربوکسیلیک اسید په عام نوم کې ”-ic acid“ پای په ”-aldehyde“ کلمه بدلېږي.')
visual('chem12-p117-common-aldehydes',common)
add('The position of other groups on the chain are indicated by Greek letters, α, β, γ etc. Letter starts from the carbon atom adjacent to formyl group. The first letter, is given to the carbon atom next to the carbonyl group.','زنجیر پر دوسرے گروپوں کا مقام یونانی حروف α، β، γ وغیرہ سے ظاہر کیا جاتا ہے۔ حروف فارمائل گروپ کے ملحقہ کاربن ایٹم سے شروع ہوتے ہیں۔ پہلا حرف کاربونل گروپ کے ساتھ والے کاربن ایٹم کو دیا جاتا ہے۔','پر ځنځیر د نورو ګروپونو موقعیت په یوناني تورو α، β، γ او نورو ښودل کېږي. توري د فورمیل ګروپ له ګاونډي کاربني اټوم پیلېږي. لومړی توری د کاربونیل ګروپ تر څنګ کاربني اټوم ته ورکول کېږي.')
visual('chem12-p117-greek-letters',greek)
add('b. IUPAC System','b. IUPAC نظام','b. IUPAC سیستم','heading')
add('In this system, following rules are used for naming aldehydes.','اس نظام میں الڈیہائیڈز کے نام رکھنے کے لیے درج ذیل اصول استعمال ہوتے ہیں۔','په دې سیستم کې د الدیهایډونو د نومولو لپاره لاندې قواعد کارېږي.')
rules=[('1. In IUPAC system, the ending “–e” of the corresponding alkane is replaced by “–al”.','1. IUPAC نظام میں متعلقہ الکین (اکیلے بند والے) کا اختتامیہ ”–e“ ”–al“ سے بدل دیا جاتا ہے۔','1. په IUPAC سیستم کې د اړوند الکان پای ”–e“ په ”–al“ بدلېږي.'),
 ('2. Prefixes di–, tri– etc. is added before suffix –al, when two or three carbonyl groups respectively, are present.','2. جب بالترتیب دو یا تین کاربونل گروپ ہوں تو لاحقہ –al سے پہلے سابقے di–، tri– وغیرہ لگائے جاتے ہیں۔','2. کله چې په ترتیب سره دوه یا درې کاربونیل ګروپونه وي، له –al وروستاړي مخکې di–، tri– او نور مختاړي ورزیاتېږي.'),
 ('3. If the aldehyde group is attached to a ring, the suffix carbaldehyde is used.','3. اگر الڈیہائیڈ گروپ حلقے سے جڑا ہو تو لاحقہ carbaldehyde استعمال ہوتا ہے۔','3. که الدیهاید ګروپ له کړۍ سره تړلی وي، carbaldehyde وروستاړی کارېږي.'),
 ('4. Locate the longest chain of carbon atoms containing formyl group to get the stem name.','4. بنیادی نام کے لیے فارمائل گروپ والی کاربن ایٹموں کی سب سے لمبی زنجیر تلاش کریں۔','4. د اصلي نوم لپاره د فورمیل ګروپ لرونکي کاربني اټومونو تر ټولو اوږد ځنځیر ومومئ.'),
 ('5. Carbon atoms of the selected chain are numbered from the carbon of formyl group (–CHO) because it is always at the terminal position. It is not necessary to mention the position of aldehydic carbonyl.','5. منتخب زنجیر کے کاربن ایٹموں کو فارمائل گروپ (–CHO) کے کاربن سے نمبر دیا جاتا ہے کیونکہ یہ ہمیشہ سرے پر ہوتا ہے۔ الڈیہائیڈی کاربونل کا مقام بتانا ضروری نہیں۔','5. د ټاکل شوي ځنځیر کاربني اټومونه د فورمیل ګروپ (–CHO) له کاربن شمېرل کېږي ځکه دا تل په پای موقعیت کې وي. د الدیهایدي کاربونیل موقعیت ښودل اړین نه دي.'),
 ('6. The rules for naming substituents are same as in case of alkanes.','6. متبادلات کے نام رکھنے کے اصول وہی ہیں جو الکینز (اکیلے بند والے) کے لیے ہیں۔','6. د بدیلونو د نومولو قواعد د الکانونو په څېر دي.')]
s0=len(paras)
for r in rules:paras.append(pair(*r))
layout.append({'type':'lines','indices':list(range(s0,len(paras)))})
add('Examples','مثالیں','بېلګې','heading')
visual('chem12-p117-iupac-examples-1',ex)
record=section('19.1','Introduction, carbonyl group and nomenclature of aldehydes','تعارف، کاربونل گروپ اور الڈیہائیڈز کی نام گذاری','پېژندنه، کاربونیل ګروپ او د الدیهایډونو نومول',paras,layout,blocks,'226–227')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':117,'printedPages':[226,227]}]
record['sourceContinuesOnPdfPage']=118
issues=[{'id':'chem12-p227-example-names','printedPage':227,'description':'First three IUPAC examples at the foot of printed 227 have no visible names in the scan; reproduced without names (no names invented).'}]
if __name__=='__main__':save(117,[record],issues=issues,chapter_number=19)
