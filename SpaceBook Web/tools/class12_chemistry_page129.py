"""PDF129 printed250–251: Unit 20 introduction, carboxyl group and derivatives, nomenclature (common names, Table 20.1)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain,carbonyl
F=Fig('arrow129');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'carboxyl group':('کاربوکسل گروپ','کاربوکسیل ګروپ'),'aliphatic carboxylic acids':('ایلیفیٹک کاربوکسلک ایسڈز','الیفاتیک کاربوکسیلیک اسیدونه'),'aromatic carboxylic acids':('ارومیٹک کاربوکسلک ایسڈز','اروماتیک کاربوکسیلیک اسیدونه'),
   'carboxylic acid':('کاربوکسلک ایسڈ','کاربوکسیلیک اسید'),'acid halide':('ایسڈ ہیلائیڈ','اسید هالایډ'),'(acyl halide)':('(ایسائل ہیلائیڈ)','(اسایل هالایډ)'),'ester':('ایسٹر','ایسټر'),'acid anhydride':('ایسڈ این ہائیڈرائیڈ','اسید انهایدراید'),
   'acid amide':('ایسڈ امائیڈ','اسید اماید'),'nitrile':('نائٹرائل','نایټرایل'),'α– methylpropionic acid':('α– میتھائل پروپیونک ایسڈ','α– میتایل پروپیونیک اسید'),'(isobutyric acid)':('(آئسوبیوٹائرک ایسڈ)','(ایزوبیوټیریک اسید)'),'β– bromobutyric acid':('β– برومو بیوٹائرک ایسڈ','β– بروموبیوټیریک اسید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def cg(lang):return F.start(90)+C(425,60,'','O—H')+t(425,84,lb(lang,'carboxyl group'),12)+'</svg>'
def types(lang):return F.start(100)+C(250,60,'H/R','O—H')+t(250,84,lb(lang,'aliphatic carboxylic acids'),12)+C(600,60,'Ar','O—H')+t(600,84,lb(lang,'aromatic carboxylic acids'),12)+'</svg>'
def derivs(lang):
 s=F.start(200)
 for x,(r,n,n2) in zip((110,320,520,740),(('OH','carboxylic acid',None),('X','acid halide','(acyl halide)'),('OR','ester',None),('O—C(=O)—R','acid anhydride',None))):
  s+=C(x,60,'R',r)+t(x,84,lb(lang,n),12)+(t(x,100,lb(lang,n2),12) if n2 else '')
 s+=C(300,160,'R','NH₂')+t(300,184,lb(lang,'acid amide'),12)+t(550,160,'R—C≡N',16)+t(550,184,lb(lang,'nitrile'),12)
 return s+'</svg>'
def branched(lang):
 s=F.start(140)+chain(F,0,60,['CH₃','—','CH','—','COOH'],15,{0:'β',2:'α'},None,{2:'CH₃'},center=230)+t(230,118,lb(lang,'α– methylpropionic acid'),12)+t(230,134,lb(lang,'(isobutyric acid)'),12)
 s+=chain(F,0,60,['CH₃','—','CH','—','CH₂','—','COOH'],15,{0:'γ',2:'β',4:'α'},None,{2:'Br'},center=620)+t(620,118,lb(lang,'β– bromobutyric acid'),12)
 return s+'</svg>'

add('Introduction','تعارف','پېژندنه','heading')
add('The combination of a carbonyl group and a hydroxyl is called a carboxyl group; carb- from carbonyl and –oxyl from hydroxyl. Compounds containing the carboxyl group are distinctly acidic and are called carboxylic acids.','کاربونل گروپ اور ہائیڈروآکسل کا مجموعہ کاربوکسل گروپ کہلاتا ہے؛ carb- کاربونل سے اور –oxyl ہائیڈروآکسل سے۔ کاربوکسل گروپ والے مرکبات واضح طور پر تیزابی ہوتے ہیں اور کاربوکسلک ایسڈز کہلاتے ہیں۔','د کاربونیل ګروپ او هایدروکسیل یوځای کېدل کاربوکسیل ګروپ بلل کېږي؛ carb- له کاربونیل او –oxyl له هایدروکسیل څخه. د کاربوکسیل ګروپ لرونکي مرکبات په ښکاره ډول تېزابي دي او کاربوکسیلیک اسیدونه بلل کېږي.')
visual('chem12-p129-carboxyl',cg)
add('Carboxylic acids may be aliphatic or aromatic depending upon whether carboxyl group is attached to an alkyl group or an aryl group. The simplest acid is formic acid (HCOOH), with a hydrogen atom bonded to the carboxyl group, and also an aliphatic acid. Fatty acids are long-chain aliphatic carboxylic acids derived from the hydrolysis of fats and oils. Acids containing one such functional group are known as mono carboxylic acids, while those containing two carboxyl groups are called dicarboxylic acids.',
 'کاربوکسل گروپ الکائل گروپ سے جڑا ہے یا ایرائل گروپ سے، اس کے لحاظ سے کاربوکسلک ایسڈز ایلیفیٹک یا ارومیٹک ہو سکتے ہیں۔ سب سے سادہ ایسڈ فارمک ایسڈ (HCOOH) ہے، جس میں کاربوکسل گروپ سے ہائیڈروجن ایٹم جڑا ہے، اور یہ بھی ایلیفیٹک ایسڈ ہے۔ فیٹی ایسڈز لمبی زنجیر والے ایلیفیٹک کاربوکسلک ایسڈز ہیں جو چکنائیوں اور تیلوں کی ہائیڈرولائسز سے حاصل ہوتے ہیں۔ ایک ایسا فعلی گروپ رکھنے والے ایسڈز مونو کاربوکسلک ایسڈز اور دو کاربوکسل گروپ رکھنے والے ڈائی کاربوکسلک ایسڈز کہلاتے ہیں۔',
 'کاربوکسیلیک اسیدونه د دې پر بنسټ چې کاربوکسیل ګروپ له الکایل یا اریل ګروپ سره تړلی وي، الیفاتیک یا اروماتیک کېدای شي. تر ټولو ساده اسید فورمیک اسید (HCOOH) دی چې له کاربوکسیل ګروپ سره یو هایدروجني اټوم لري، او دا هم الیفاتیک اسید دی. غوړي اسیدونه اوږد ځنځیري الیفاتیک کاربوکسیلیک اسیدونه دي چې د غوړیو او تېلو له هایدرولیز ترلاسه کېږي. هغه اسیدونه چې یو داسې فعال ګروپ لري مونو کاربوکسیلیک اسیدونه، او هغه چې دوه کاربوکسیل ګروپونه لري ډای کاربوکسیلیک اسیدونه بلل کېږي.')
visual('chem12-p129-acid-types',types)
add('Carboxylic acids have many derivatives in which the –OH of an acid is replaced by other functional groups. Carboxylic acid derivatives are compounds with functional groups that can be converted to carboxylic acids by a simple acidic or basic hydrolysis. The most important acid derivatives are acid halides, esters, anhydrides, amides and nitriles.',
 'کاربوکسلک ایسڈز کے بہت سے مشتقات ہیں جن میں ایسڈ کا –OH دوسرے فعلی گروپوں سے بدل جاتا ہے۔ کاربوکسلک ایسڈ مشتقات وہ مرکبات ہیں جن کے فعلی گروپ سادہ تیزابی یا اساسی ہائیڈرولائسز سے کاربوکسلک ایسڈز میں بدل سکتے ہیں۔ سب سے اہم ایسڈ مشتقات ایسڈ ہیلائیڈز، ایسٹرز، این ہائیڈرائیڈز، امائیڈز اور نائٹرائلز ہیں۔',
 'کاربوکسیلیک اسیدونه ډېر مشتقات لري چې پکې د اسید –OH په نورو فعالو ګروپونو بدلېږي. د کاربوکسیلیک اسید مشتقات هغه مرکبات دي چې فعال ګروپونه یې د ساده اسیدي یا قلوي هایدرولیز په واسطه کاربوکسیلیک اسیدونو ته اوښتلی شي. تر ټولو مهم اسیدي مشتقات اسید هالایډونه، ایسټرونه، انهایدرایډونه، امایډونه او نایټرایلونه دي.')
visual('chem12-p129-derivatives',derivs)
add('Notice that in each case there is a carbon atom (highlighted in blue) with three bonds to heteroatoms. As a result, each of these carbon atoms has the same oxidation state as the carbon atom of a carboxylic acid. Thus, the inter-conversion of carboxylic acid and derivatives, do not involve change in oxidation state of this carbon. Although all of these derivatives (except nitrile) exhibit a carbonyl group, the presence of a carbonyl group is not a necessary requirement to qualify as a carboxylic acid derivative. Any compound with a carbon atom that has three bonds to heteroatoms that can be converted to carboxylic acids by a simple acidic or basic hydrolysis will be classified as a carboxylic acid derivative.',
 'غور کریں کہ ہر صورت میں ایک کاربن ایٹم (نیلے رنگ میں نمایاں) ہے جس کے ہیٹرو ایٹموں سے تین بند ہیں۔ نتیجتاً ان میں سے ہر کاربن ایٹم کی تکسیدی حالت وہی ہے جو کاربوکسلک ایسڈ کے کاربن ایٹم کی ہے۔ اس طرح کاربوکسلک ایسڈ اور مشتقات کی باہمی تبدیلی میں اس کاربن کی تکسیدی حالت نہیں بدلتی۔ اگرچہ یہ تمام مشتقات (نائٹرائل کے سوا) کاربونل گروپ رکھتے ہیں، لیکن کاربوکسلک ایسڈ مشتق ہونے کے لیے کاربونل گروپ کا ہونا لازمی شرط نہیں۔ کوئی بھی مرکب جس میں ایسا کاربن ایٹم ہو جس کے ہیٹرو ایٹموں سے تین بند ہوں اور جو سادہ تیزابی یا اساسی ہائیڈرولائسز سے کاربوکسلک ایسڈ میں بدل سکے، کاربوکسلک ایسڈ مشتق شمار ہوتا ہے۔',
 'پام وکړئ چې په هر حالت کې یو کاربني اټوم (په شین رنګ نښه شوی) شته چې له هېټرو اټومونو سره درې تړونونه لري. په پایله کې د دې هر کاربني اټوم اکسیډېشن حالت د کاربوکسیلیک اسید د کاربني اټوم په څېر دی. نو د کاربوکسیلیک اسید او مشتقاتو متقابل بدلون د دې کاربن د اکسیډېشن حالت بدلون نه رانغاړي. که څه هم دا ټول مشتقات (پرته له نایټرایل) کاربونیل ګروپ لري، د کاربوکسیلیک اسید مشتق کېدو لپاره د کاربونیل ګروپ شتون اړین شرط نه دی. هر هغه مرکب چې داسې کاربني اټوم ولري چې له هېټرو اټومونو سره درې تړونونه لري او د ساده اسیدي یا قلوي هایدرولیز په واسطه کاربوکسیلیک اسید ته واوړي، د کاربوکسیلیک اسید مشتق ګڼل کېږي.')
add('20.1 Nomenclature','20.1 نام گذاری','20.1 نومول','heading')
add('Nomenclature of carboxylic acid','کاربوکسلک ایسڈ کی نام گذاری','د کاربوکسیلیک اسید نومول','heading')
add('Following two types of naming is employed for naming of carboxylic acids.','کاربوکسلک ایسڈز کے نام رکھنے کے لیے درج ذیل دو طریقے استعمال ہوتے ہیں۔','د کاربوکسیلیک اسیدونو د نومولو لپاره لاندې دوه ډوله نومول کارېږي.')
add('(a) Common or Trivial Names','(a) عام یا روایتی نام','(a) عام یا دودیز نومونه','heading')
add('Many of the acids have common names. These names usually come from some Latin or Greek words that indicates the original source of the acid. Following table 20.1 lists some common aliphatic carboxylic acids, with their common names.','بہت سے ایسڈز کے عام نام ہیں۔ یہ نام عموماً بعض لاطینی یا یونانی الفاظ سے آتے ہیں جو ایسڈ کے اصل ماخذ کی نشاندہی کرتے ہیں۔ درج ذیل جدول 20.1 میں بعض عام ایلیفیٹک کاربوکسلک ایسڈز ان کے عام ناموں کے ساتھ دیے گئے ہیں۔','ډېر اسیدونه عام نومونه لري. دا نومونه معمولاً له ځینو لاتیني یا یوناني کلمو راځي چې د اسید اصلي سرچینه ښيي. لاندې جدول 20.1 ځینې عام الیفاتیک کاربوکسیلیک اسیدونه له عامو نومونو سره ښيي.')
tb={'id':'chem12-table20-1','headers':['Carbon atoms','Formula (common name)','Sources'],
 'rows':[['1','HCOOH formic acid','From Latin word formica means ‘ant’'],['2','CH₃COOH acetic acid','From Latin word acetum means ‘vinegar’'],['3','CH₃CH₂COOH propionic acid','From Greek word protos means ‘first’ and pion means ‘fat’'],['4','CH₃CH₂CH₂COOH butyric acid','From Latin word butyrum means ‘butter’'],['5','CH₃CH₂CH₂CH₂COOH valeric acid','Isolated from roots of valerian plant']],
 'translations':[{'language':'اردو','headers':['کاربن ایٹم','فارمولا (عام نام)','ماخذ'],'rows':[['1','HCOOH فارمک ایسڈ','لاطینی لفظ formica یعنی ’چیونٹی‘ سے'],['2','CH₃COOH ایسیٹک ایسڈ','لاطینی لفظ acetum یعنی ’سرکہ‘ سے'],['3','CH₃CH₂COOH پروپیونک ایسڈ','یونانی لفظ protos یعنی ’پہلا‘ اور pion یعنی ’چکنائی‘ سے'],['4','CH₃CH₂CH₂COOH بیوٹائرک ایسڈ','لاطینی لفظ butyrum یعنی ’مکھن‘ سے'],['5','CH₃CH₂CH₂CH₂COOH ویلیرک ایسڈ','ویلیرین پودے کی جڑوں سے الگ کیا گیا']]},
                 {'language':'پښتو','headers':['کاربني اټومونه','فورمول (عام نوم)','سرچینې'],'rows':[['1','HCOOH فورمیک اسید','له لاتیني کلمې formica یعنې ’مېږی‘'],['2','CH₃COOH اسیټیک اسید','له لاتیني کلمې acetum یعنې ’سرکه‘'],['3','CH₃CH₂COOH پروپیونیک اسید','له یوناني کلمې protos یعنې ’لومړی‘ او pion یعنې ’غوړي‘'],['4','CH₃CH₂CH₂COOH بیوټیریک اسید','له لاتیني کلمې butyrum یعنې ’کوچ‘'],['5','CH₃CH₂CH₂CH₂COOH والیریک اسید','د والیرین بوټي له ریښو جلا شوی']]}]}
add('Table 20.1 Common Names of few Organic Acids','جدول 20.1 چند نامیاتی ایسڈز کے عام نام','جدول 20.1 د څو عضوي اسیدونو عام نومونه')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('In case of branched acids, the common name of the acid is also used. Substituents are located with Greek letters α, β, γ, δ etc. as given below.','شاخ دار ایسڈز کی صورت میں بھی ایسڈ کا عام نام استعمال ہوتا ہے۔ متبادلات کا مقام یونانی حروف α، β، γ، δ وغیرہ سے بتایا جاتا ہے جیسا کہ نیچے دیا گیا ہے۔','د څانګه لرونکو اسیدونو په حالت کې هم د اسید عام نوم کارېږي. د بدیلونو موقعیت په یوناني تورو α، β، γ، δ او نورو ښودل کېږي لکه څنګه چې لاندې ورکړل شوي.')
visual('chem12-p129-branched',branched)
record=section('20.1','Introduction to carboxylic acids, derivatives and common names','کاربوکسلک ایسڈز کا تعارف، مشتقات اور عام نام','د کاربوکسیلیک اسیدونو پېژندنه، مشتقات او عام نومونه',paras,layout,blocks,'250–251')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':129,'printedPages':[250,251]}]
record['sourceContinuesOnPdfPage']=130
trim=[{'id':'20.2','startsAt':'(b)\nIUPAC Nomenclature'}]
if __name__=='__main__':save(129,[record],trim=trim,chapter_number=20)
