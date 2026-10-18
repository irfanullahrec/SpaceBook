"""PDF94 printed180–181: Grignard + CO₂ example, amines classification, nomenclature, physical properties."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow94');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'methylmagnesium':('میتھائل میگنیشیم','میتایل مګنیزیم'),'bromide':('برومائیڈ','برومایډ'),'addition product':('اضافی پیداوار','اضافي محصول'),'(workup)':('(ورک اپ)','(ورک اپ)'),'acetic acid':('ایسیٹک ایسڈ','اسیټیک اسید'),
   'Ammonia':('امونیا','امونیا'),'Amines':('امائنز','امینونه'),'Primary':('ابتدائی','لومړنی'),'Secondary':('ثانوی','دویمی'),'Tertiary':('ثالثی','درېیمی'),
   'n-propyl amine':('n-پروپائل امائن','n-پروپیل امین'),'ethyl methyl amine':('ایتھائل میتھائل امائن','ایتیل میتایل امین'),'trimethyl amine':('ٹرائی میتھائل امائن','ټرای میتایل امین'),'ethyl dimethyl amine':('ایتھائل ڈائی میتھائل امائن','ایتیل ډای میتایل امین'),
   'propan-1-amine':('پروپین-1-امائن','پروپان-1-امین'),'N-methylethanamine':('N-میتھائل ایتھین امائن','N-میتایل ایتان امین'),'N,N-dimethylethanamine':('N،N-ڈائی میتھائل ایتھین امائن','N،N-ډای میتایل ایتان امین'),'3-methylbutan-2-amine':('3-میتھائل بیوٹین-2-امائن','3-میتایل بیوټان-2-امین'),
   '1° or 2° amine:':('1° یا 2° امائن:','1° یا 2° امین:'),'hydrogen bond donor and acceptor':('ہائیڈروجن بند دینے اور لینے والا','د هایدروجني تړون ورکوونکی او اخیستونکی')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def acetic(lang):
 s=F.start(140)+t(80,70,'CH₃—MgBr +',16)+t(170,30,'O',15)+line(167,36,167,52)+line(173,36,173,52)+t(170,70,'C',17)+line(167,78,167,94)+line(173,78,173,94)+t(170,112,'O',15)
 s+=t(70,100,lb(lang,'methylmagnesium'),12)+t(70,116,lb(lang,'bromide'),12)+F.arrow(220,290,64)
 s+=t(380,30,'O',15)+line(377,36,377,52)+line(383,36,383,52)+t(395,70,'CH₃—C—O⁻Mg⁺Br',16)+t(395,96,lb(lang,'addition product'),12)+F.arrow(500,590,64,'H₃O⁺',lb(lang,'(workup)'))
 s+=t(680,30,'O',15)+line(677,36,677,52)+line(683,36,683,52)+t(680,70,'CH₃—C—OH',16)+t(680,96,lb(lang,'acetic acid'),12)
 return s+'</svg>'
def nh(x,y,top,left,right):
 return t(x,y-34,top,15)+line(x,y-28,x,y-14)+t(x-36,y+5,left,15)+line(x-24,y,x-10,y)+t(x,y+5,'N̈',16)+line(x+10,y,x+24,y)+t(x+36,y+5,right,15)
def classes(lang):
 s=F.start(170)+'<rect x="20" y="40" width="130" height="100" fill="white" stroke="#222"/>'+t(85,30,lb(lang,'Ammonia'),14)+nh(85,100,'H','H','H')
 s+=F.arrow(160,220,90)+'<rect x="230" y="40" width="590" height="120" rx="8" fill="white" stroke="#222"/>'+t(525,30,lb(lang,'Amines'),14)
 for x,(top,l,r,name,deg) in zip((330,525,720),(('H','H','R','Primary','(1°)'),('H','R','R','Secondary','(2°)'),('R','R','R','Tertiary','(2°)'))):
  s+=nh(x,100,top,l,r)+t(x,135,lb(lang,name),13)+t(x,152,deg,12)
 return s+'</svg>'
def common(lang):
 s=F.start(200)
 s+=t(220,40,'CH₃—CH₂—CH₂—NH₂',16)+t(220,62,lb(lang,'n-propyl amine'),12)+t(620,40,'CH₃—CH₂—NH—CH₃',16)+t(620,62,lb(lang,'ethyl methyl amine'),12)
 s+=chain(F,0,150,['CH₃','—','N','—','CH₃'],16,None,{2:'CH₃'},center=220)+t(220,178,lb(lang,'trimethyl amine'),12)
 s+=chain(F,0,150,['CH₃','—','N','—','C₂H₅'],16,None,{2:'CH₃'},center=620)+t(620,178,lb(lang,'ethyl dimethyl amine'),12)
 return s+'</svg>'
def iupac(lang):
 s=F.start(200)
 s+=t(220,40,'CH₃—CH₂—CH₂—NH₂',16)+t(220,62,lb(lang,'propan-1-amine'),12)+t(620,40,'CH₃—CH₂—NH—CH₃',16)+t(620,62,lb(lang,'N-methylethanamine'),12)
 s+=chain(F,0,150,['CH₃','—','CH₂','—','N','—','CH₃'],16,None,{4:'CH₃'},center=220)+t(220,178,lb(lang,'N,N-dimethylethanamine'),12)
 s+=chain(F,0,150,['CH₃','—','CH','—','CH','—','CH₃'],16,None,{2:'NH₂',4:'CH₃'},center=620)+t(620,178,lb(lang,'3-methylbutan-2-amine'),12)
 return s+'</svg>'
def hbond(lang):
 s=F.start(170,520)+t(180,40,'H',15)+line(186,46,198,58)+t(210,70,'N',16)+'<ellipse cx="236" cy="66" rx="12" ry="8" fill="none" stroke="#222"/>'+t(236,70,':',12)+line(200,72,180,82)+t(170,90,'R',15)+line(206,78,198,96)+t(196,110,'R',15)
 s+=t(272,70,'⋯ H',16)+line(290,76,302,88)+t(312,100,'N',16)+'<ellipse cx="338" cy="96" rx="12" ry="8" fill="none" stroke="#222"/>'+line(302,102,282,112)+t(272,120,'R',15)+line(310,108,306,126)+t(306,140,'R',15)
 s+=t(260,152,lb(lang,'1° or 2° amine:'),12)+t(260,166,lb(lang,'hydrogen bond donor and acceptor'),12)
 return s+'</svg>'

visual('chem12-p94-acetic-acid',acetic)
add('This method is particularly used for conversion of alkyl halides to carboxylic acids. The resulting carboxylic acids contain a carbon more than parent alkyl halide.','یہ طریقہ خاص طور پر الکائل ہیلائیڈز کو کاربوکسیلک ایسڈز میں تبدیل کرنے کے لیے استعمال ہوتا ہے۔ حاصل ہونے والے کاربوکسیلک ایسڈز میں اصل الکائل ہیلائیڈ سے ایک کاربن زیادہ ہوتا ہے۔','دا طریقه په ځانګړي ډول د الکایل هالایډونو په کاربوکسیلیک اسیدونو د بدلولو لپاره کارېږي. ترلاسه شوي کاربوکسیلیک اسیدونه د اصلي الکایل هالایډ څخه یو کاربن ډېر لري.')
add('17.3 Amines','17.3 امائنز','17.3 امینونه','heading')
add('Amines are important nitrogen containing organic compounds. These are the derivatives of ammonia in which one or more hydrogen atoms have been replaced by one or more similar or different alkyl groups (or aryl groups).','امائنز نائٹروجن رکھنے والے اہم نامیاتی مرکبات ہیں۔ یہ امونیا کے وہ مشتقات ہیں جن میں ایک یا زیادہ ہائیڈروجن ایٹم ایک یا زیادہ یکساں یا مختلف الکائل گروپوں (یا ایرائل گروپوں) سے بدل دیے گئے ہوں۔','امینونه مهم نایتروجن لرونکي عضوي مرکبات دي. دا د امونیا هغه مشتقات دي چې پکې یو یا ډېر هایدروجني اټومونه په یوه یا ډېرو ورته یا بېلو الکایل ګروپونو (یا اریل ګروپونو) بدل شوي وي.')
add('On the basis of the number of alkyl or aryl groups directly bonded to nitrogen atom, amines have been classified into primary, secondary and tertiary amines shown below.','نائٹروجن ایٹم سے براہِ راست جڑے الکائل یا ایرائل گروپوں کی تعداد کی بنیاد پر امائنز کو ابتدائی، ثانوی اور ثالثی امائنز میں تقسیم کیا گیا ہے، جیسا کہ نیچے دکھایا گیا ہے۔','له نایتروجني اټوم سره د مستقیم تړلو الکایل یا اریل ګروپونو د شمېر پر بنسټ امینونه په لومړنیو، دویمیو او درېیمیو امینونو وېشل شوي، لکه څنګه چې لاندې ښودل شوي.')
visual('chem12-p94-amine-classes',classes)
add('17.3.1 Nomenclature','17.3.1 نام گذاری','17.3.1 نومول','heading')
add('Amines are named by common and IUPAC systems.','امائنز کے نام عام اور IUPAC نظاموں سے رکھے جاتے ہیں۔','امینونه د عام او IUPAC سیستمونو په واسطه نومول کېږي.')
add('a. Common system','a. عام نظام','a. عام سیستم','heading')
for e,u,p in [('Common names of amines are formed from the names of the alkyl groups bonded to nitrogen, followed by the suffix -amine.','امائنز کے عام نام نائٹروجن سے جڑے الکائل گروپوں کے ناموں کے بعد لاحقہ -amine لگا کر بنائے جاتے ہیں۔','د امینونو عام نومونه له نایتروجن سره د تړلو الکایل ګروپونو له نومونو وروسته د -amine وروستاړي په راوړلو جوړېږي.'),
 ('The prefixes di- and tri- are used to describe two and three identical substituents, attached to nitrogen.','نائٹروجن سے جڑے دو اور تین یکساں متبادلات کو ظاہر کرنے کے لیے سابقے di- اور tri- استعمال ہوتے ہیں۔','له نایتروجن سره د تړلو دوو او دریو ورته بدیلونو د ښودلو لپاره di- او tri- مختاړي کارېږي.'),
 ('If different alkyl groups are attached to the nitrogen, then they are named separately in alphabetical order.','اگر نائٹروجن سے مختلف الکائل گروپ جڑے ہوں تو ان کے نام حروفِ تہجی کی ترتیب سے الگ الگ رکھے جاتے ہیں۔','که له نایتروجن سره بېل الکایل ګروپونه تړلي وي، د الفبا په ترتیب جلا جلا نومول کېږي.')]:
 add(e,u,p,'list')
visual('chem12-p94-common-amines',common)
add('b. IUPAC system','b. IUPAC نظام','b. IUPAC سیستم','heading')
add('In IUPAC nomenclature of amines, the longest continuous chain of carbon atoms determines the root name. The -e ending in the alkane name is changed to suffix -amine and a number shows the position of the amino group along the chain. Other substituents on the carbon chain are given numbers, and the prefix N- is used for each substituent on nitrogen.',
 'امائنز کی IUPAC نام گذاری میں کاربن ایٹموں کی سب سے لمبی مسلسل زنجیر بنیادی نام طے کرتی ہے۔ الکین (اکیلے بند والے) کے نام کا آخری -e لاحقے -amine سے بدل دیا جاتا ہے اور ایک عدد زنجیر میں امائنو گروپ کا مقام ظاہر کرتا ہے۔ کاربن زنجیر پر دوسرے متبادلات کو نمبر دیے جاتے ہیں، اور نائٹروجن پر ہر متبادل کے لیے سابقہ N- استعمال ہوتا ہے۔',
 'د امینونو په IUPAC نومولو کې د کاربني اټومونو تر ټولو اوږد پرله پسې ځنځیر اصلي نوم ټاکي. د الکان په نوم کې وروستی -e په -amine وروستاړي بدلېږي او یوه شمېره په ځنځیر کې د امینو ګروپ موقعیت ښيي. پر کاربني ځنځیر نورو بدیلونو ته شمېرې ورکول کېږي، او پر نایتروجن د هر بدیل لپاره N- مختاړی کارېږي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Amines also possess metamerism. For example, ethyl methyl amine and trimethyl amine are metamers of each other.','امائنز میں میٹامرزم بھی پایا جاتا ہے۔ مثلاً ایتھائل میتھائل امائن اور ٹرائی میتھائل امائن ایک دوسرے کے میٹامر ہیں۔','امینونه میټامېریزم هم لري. د بېلګې په توګه ایتیل میتایل امین او ټرای میتایل امین د یو بل میټامرونه دي.')
visual('chem12-p94-iupac-amines',iupac)
add('17.3.2 Physical Properties','17.3.2 طبعی خصوصیات','17.3.2 فزیکي ځانګړنې','heading')
add('Low molecular weight amines are generally gases or low boiling liquids at room temperature. They possess a characteristic ammonia like smell.','کم سالماتی وزن والے امائنز عموماً کمرے کے درجہ حرارت پر گیسیں یا کم نقطۂ جوش والے مائع ہیں۔ ان کی امونیا جیسی مخصوص بو ہوتی ہے۔','ټیټ مالیکولي وزن لرونکي امینونه معمولاً د کوټې په تودوخه کې ګازونه یا ټیټ د ایشېدو ټکي لرونکي مایعات دي. د امونیا په څېر ځانګړی بوی لري.','list')
add('Amines have higher boiling points than alkanes of similar molecular weight due to the presence of intermolecular hydrogen bondings. The molecules of primary and secondary amines have high boiling points because they are able to form hydrogen bondings among their molecules.','امائنز کے نقطۂ جوش ملتے جلتے سالماتی وزن والے الکینز (اکیلے بند والے) سے بین السالماتی ہائیڈروجن بندش کی موجودگی کی وجہ سے زیادہ ہیں۔ ابتدائی اور ثانوی امائنز کے سالمات کے نقطۂ جوش زیادہ ہیں کیونکہ یہ اپنے سالمات کے درمیان ہائیڈروجن بندش بنا سکتے ہیں۔','امینونه د بین المالیکولي هایدروجني تړون د شتون له امله د ورته مالیکولي وزن لرونکو الکانونو په پرتله لوړ د ایشېدو ټکي لري. د لومړنیو او دویمیو امینونو مالیکولونه لوړ د ایشېدو ټکي لري ځکه دوی کولی شي د خپلو مالیکولونو ترمنځ هایدروجني تړون جوړ کړي.','list')
visual('chem12-p94-amine-hbond',hbond)
add('Molecules of tertiary amines cannot form hydrogen bonding among themselves, thus having lower boiling points than primary and secondary amines of the same molecular weight.','ثالثی امائنز کے سالمات آپس میں ہائیڈروجن بندش نہیں بنا سکتے، اس لیے ان کے نقطۂ جوش اسی سالماتی وزن کے ابتدائی اور ثانوی امائنز سے کم ہیں۔','د درېیمیو امینونو مالیکولونه په خپل منځ کې هایدروجني تړون نه شي جوړولی، نو د ورته مالیکولي وزن لرونکو لومړنیو او دویمیو امینونو په پرتله ټیټ د ایشېدو ټکي لري.','list')
add('However, all lower primary, secondary and tertiary amines can form hydrogen bonding with water and therefore lower amines are soluble in water.','تاہم تمام کم کاربن والے ابتدائی، ثانوی اور ثالثی امائنز پانی سے ہائیڈروجن بندش بنا سکتے ہیں اور اس لیے کم امائنز پانی میں حل پذیر ہیں۔','خو ټول ټیټ لومړني، دویمي او درېیمي امینونه له اوبو سره هایدروجني تړون جوړولی شي او له همدې امله ټیټ امینونه په اوبو کې حلېږي.','list')
record=section('17.10','Amines: classification, nomenclature and physical properties','امائنز: درجہ بندی، نام گذاری اور طبعی خصوصیات','امینونه: ډلبندي، نومول او فزیکي ځانګړنې',paras,layout,blocks,'180–181')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':94,'printedPages':[180,181]}]
record['sourceContinuesOnPdfPage']=95
issues=[{'id':'chem12-p180-tertiary-label','printedPage':180,'description':'Amine classification figure labels Tertiary as "(2°)"; retained as printed (3° intended).'}]
carry=[{'from':'17.10','to':'17.11','startsAt':'181\nH\nH\nR\nR\nH\nNOT FOR SALE'}]
if __name__=='__main__':save(94,[record],carry=carry,issues=issues,chapter_number=17)
