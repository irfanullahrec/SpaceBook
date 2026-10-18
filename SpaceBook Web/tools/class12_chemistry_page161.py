"""PDF161 printed316–317: parathion, 22.5 petrochemicals (Table 22.2), basic building block processes — cracking."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow161');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Parathion':('پیراتھیون','پاراتیون'),'S. No.':('نمبر شمار','شمېره'),'Feedstock':('خام مال','خام مواد'),'Primary petrochemicals':('بنیادی پیٹرو کیمیکلز','لومړني پټرو کیمیکلونه'),'Formulae':('فارمولے','فورمولونه'),
   'Natural gas':('قدرتی گیس','طبیعي ګاز'),'Naphtha':('نیفتھا','نفتا'),'Reformed':('ریفارمڈ','ریفارم شوې'),'Ethene':('ایتھین','ایتین'),'Propene':('پروپین','پروپین'),'Ethyne':('ایتھائن','ایتاین'),'Butadiene':('بیوٹا ڈائین','بیوټاډاین'),
   'Benzene':('بینزین','بنزین'),'Toluene':('ٹولوئین','ټولوین'),'o – xylene':('o – زائلین','o – زایلین'),'m – xylene':('m – زائلین','m – زایلین'),'p – xylene':('p – زائلین','p – زایلین'),
   'ortho-xylene':('آرتھو-زائلین','اورتو-زایلین'),'(1,2-dimethylbenzene)':('(1،2-ڈائی میتھائل بینزین)','(1،2-ډای میتایل بنزین)'),'meta-xylene':('میٹا-زائلین','میټا-زایلین'),'(1,3-dimethylbenzene)':('(1،3-ڈائی میتھائل بینزین)','(1،3-ډای میتایل بنزین)'),
   'para-xylene':('پیرا-زائلین','پارا-زایلین'),'(1,4-dimethylbenzene)':('(1،4-ڈائی میتھائل بینزین)','(1،4-ډای میتایل بنزین)')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def parathion(lang):
 s=F.start(230)+F.ring(425,140,32,subs={3:'NO₂'})+line(425,108,425,92)+t(425,86,'O',14)+line(431,78,445,62)+t(452,58,'P',15)+line(445,52,433,40)+line(441,48,429,36)+t(425,34,'S',14)
 s+=line(460,50,478,36)+t(500,34,'OCH₃',13)+line(460,60,478,70)+t(500,76,'OCH₃',13)+t(425,224,lb(lang,'Parathion'),12,'#ad1457')
 return s+'</svg>'
def table(lang):
 rows=[(1,'Natural gas',[('Ethene','CH₂ = CH₂'),('Propene','CH₃ – CH = CH₂'),('Ethyne','CH ≡ CH')]),(2,'Naphtha',[('Ethene','CH₂ = CH₂'),('Propene','CH₃ – CH = CH₂'),('Butadiene','CH₂ = CH – CH = CH₂')]),
       (3,'Reformed',[('Benzene',('ring',{})),('Toluene',('ring',{0:'CH₃'})),('o – xylene',('ring',{0:'CH₃',1:'CH₃'},'ortho-xylene','(1,2-dimethylbenzene)')),('m – xylene',('ring',{0:'CH₃',2:'CH₃'},'meta-xylene','(1,3-dimethylbenzene)')),('p – xylene',('ring',{0:'CH₃',3:'CH₃'},'para-xylene','(1,4-dimethylbenzene)'))])]
 y=50;H=sum(len(r[2]) for r in rows[:2])*34+5*140+50
 s=F.start(H)+f'<rect x="1" y="1" width="848" height="{H-2}" fill="none" stroke="#222" stroke-width="1.5"/><rect x="1" y="1" width="848" height="48" fill="#fce4ec"/>'
 for x,h in ((50,'S. No.'),(160,'Feedstock'),(330,'Primary petrochemicals'),(640,'Formulae')):s+=t(x,30,lb(lang,h),13)
 for x in (100,220,440):s+=line(x,0,x,H)
 s+=line(0,48,850,48)
 for no,feed,items in rows:
  top=y
  for name,f in items:
   h=34 if isinstance(f,str) else 140
   s+=t(330,y+h/2+5,lb(lang,name),13)
   if isinstance(f,str):s+=t(640,y+h/2+5,f,14)
   else:
    s+=F.ring(640,y+62,26,subs=f[1])
    if len(f)>2:s+=t(640,y+134,lb(lang,f[2])+' '+lb(lang,f[3]),10)
   y+=h;s+=line(220,y,850,y,0.8)
  s+=line(0,y,220,y)+t(50,(top+y)/2+5,f'{no}.',13)+t(160,(top+y)/2+(-3 if no==3 else 5),lb(lang,feed),13)+(t(160,(top+y)/2+13,lb(lang,'Naphtha'),13) if no==3 else '')
 return s+'</svg>'

visual('chem12-p161-parathion',parathion)
add('This compound breaks down fairly readily to products that appear to cause no biological damage. So, it has no long term damages but carefully handling is necessary. In short, the ideal pesticide is clearly not yet available.','یہ مرکب کافی آسانی سے ایسی مصنوعات میں ٹوٹ جاتا ہے جو بظاہر کوئی حیاتیاتی نقصان نہیں پہنچاتیں۔ اس لیے اس کے طویل مدتی نقصانات نہیں لیکن احتیاط سے برتنا ضروری ہے۔ مختصراً مثالی کیڑے مار دوا واضح طور پر ابھی دستیاب نہیں۔','دا مرکب په نسبتاً اسانۍ په داسې محصولاتو ماتېږي چې ښکاري هېڅ بیولوژیکي زیان نه رسوي. نو اوږدمهاله زیانونه نه لري خو په احتیاط سره چلول اړین دي. په لنډه توګه مثالي افت وژونکی په ښکاره ډول لا نه دی موجود.')
add('22.5 Petrochemicals','22.5 پیٹرو کیمیکلز','22.5 پټرو کیمیکلونه','heading')
add('Petroleum is a complex mixture of hydrocarbons formed by the decomposition of fossil remains. It exists as a gas (natural gas), liquid (crude oil) or as solids (oil shales) and is found deep underground or below seabed. About 10% of the petroleum is used to prepare a range of chemicals called petrochemicals. Petrochemicals as a group of chemicals produced directly or indirectly from the hydrocarbons of petroleum or natural gas. Examples of petrochemicals are plastics, rubbers, fibres, paints, solvents, and detergents.','پیٹرولیم ہائیڈروکاربنز کا ایک پیچیدہ آمیزہ ہے جو فوسل باقیات کی تحلیل سے بنتا ہے۔ یہ گیس (قدرتی گیس)، مائع (خام تیل) یا ٹھوس (آئل شیلز) کی صورت میں موجود ہے اور زمین کی گہرائی یا سمندر کی تہہ کے نیچے پایا جاتا ہے۔ تقریباً 10% پیٹرولیم کیمیکلز کی ایک رینج تیار کرنے کے لیے استعمال ہوتا ہے جنہیں پیٹرو کیمیکلز کہتے ہیں۔ پیٹرو کیمیکلز کیمیکلز کا وہ گروہ ہیں جو پیٹرولیم یا قدرتی گیس کے ہائیڈروکاربنز سے براہِ راست یا بالواسطہ تیار ہوتے ہیں۔ پیٹرو کیمیکلز کی مثالیں پلاسٹک، ربڑ، ریشے، پینٹ، محللات اور ڈٹرجنٹس ہیں۔','پټرولیم د هایدروکاربنونو یوه پېچلې ګډوله ده چې د فوسیلي پاتې شونو د تجزیې په واسطه جوړه شوې. دا د ګاز (طبیعي ګاز)، مایع (خام تېل) یا جامدو (تېلي شیل) په بڼه شته او د ځمکې ژوره لاندې یا د سمندر تر تل لاندې موندل کېږي. نږدې 10% پټرولیم د کیمیکلونو یوې لړۍ د چمتو کولو لپاره کارېږي چې پټرو کیمیکلونه بلل کېږي. پټرو کیمیکلونه د کیمیکلونو هغه ډله ده چې د پټرولیم یا طبیعي ګاز له هایدروکاربنونو څخه مستقیم یا غیر مستقیم تولیدېږي. د پټرو کیمیکلونو بېلګې پلاستیک، رابړ، ریښې، پینټ، محللونه او ډیټرجنټونه دي.')
add('Since every area of human activity makes use of petrochemicals or the materials made from them, our life without petrochemicals would be very different and less comfortable. The different petrochemicals are compiled in Table 22.2.','چونکہ انسانی سرگرمی کا ہر شعبہ پیٹرو کیمیکلز یا ان سے بنے مادوں کو استعمال کرتا ہے، اس لیے پیٹرو کیمیکلز کے بغیر ہماری زندگی بہت مختلف اور کم آرام دہ ہوتی۔ مختلف پیٹرو کیمیکلز جدول 22.2 میں درج ہیں۔','څرنګه چې د انساني فعالیت هره برخه پټرو کیمیکلونه یا له هغو جوړ مواد کاروي، زموږ ژوند به له پټرو کیمیکلونو پرته ډېر توپیر لرونکی او لږ ارامه وي. بېلابېل پټرو کیمیکلونه په جدول 22.2 کې راټول شوي.')
add('Table 22.2 Some Important Petrochemicals','جدول 22.2 چند اہم پیٹرو کیمیکلز','جدول 22.2 ځینې مهم پټرو کیمیکلونه')
visual('chem12-table22-2',table)
add('The Basic Building Block Processes','بنیادی تعمیری عمل','بنسټیزې جوړونکې عملیې','heading')
add('The basic building block petrochemical processes are divided into two groups. These processes are cracking and reforming process.','بنیادی تعمیری پیٹرو کیمیکل عمل دو گروہوں میں تقسیم ہیں۔ یہ عمل کریکنگ اور ریفارمنگ ہیں۔','بنسټیزې جوړونکې پټرو کیمیکل عملیې په دوو ډلو وېشل شوې. دا عملیې کریکنګ او ریفارمنګ دي.')
add('i. Cracking Process','i. کریکنگ کا عمل','i. د کریکنګ عملیه','heading')
add('Cracking is a process in which molecules of raw material are dissociated into smaller ones. There are two types of cracking process, thermal steam cracking and catalytic cracking.','کریکنگ وہ عمل ہے جس میں خام مال کے سالمات چھوٹے سالمات میں ٹوٹ جاتے ہیں۔ کریکنگ کے عمل کی دو اقسام ہیں، حرارتی بھاپ کریکنگ اور عمل انگیز کریکنگ۔','کریکنګ هغه عملیه ده چې پکې د خامو موادو مالیکولونه په کوچنیو مالیکولونو جلا کېږي. د کریکنګ عملیې دوه ډوله دي، تودوخیز بخار کریکنګ او کتلستي کریکنګ.')
add('a. Thermal Steam Cracking','a. حرارتی بھاپ کریکنگ','a. تودوخیز بخار کریکنګ','heading')
add('Steam cracking is the breaking of raw material such as ethane and propane yielding important petrochemical products, such as ethene and propene. Methane and hydrogen are also some of the major by-products.','بھاپ کریکنگ ایتھین اور پروپین جیسے خام مال کو توڑنا ہے جس سے ایتھین اور پروپین جیسی اہم پیٹرو کیمیکل مصنوعات حاصل ہوتی ہیں۔ میتھین اور ہائیڈروجن بھی بڑی ضمنی مصنوعات میں سے ہیں۔','بخار کریکنګ د خامو موادو لکه ایتان او پروپان ماتول دي چې مهم پټرو کیمیکل محصولات لکه ایتین او پروپین ورکوي. میتان او هایدروجن هم له اصلي ضمني محصولاتو څخه دي.')
add('b. Catalytic Cracking','b. عمل انگیز کریکنگ','b. کتلستي کریکنګ','heading')
add('Breaking of larger, stable molecules requires catalysis. Refinery products such as gas oil and fuel oil is passed through catalytic cracker to obtain gasoline and kerosene oil as major products and by-product, propene.','بڑے پائیدار سالمات کو توڑنے کے لیے عمل انگیزی درکار ہے۔ گیس آئل اور فیول آئل جیسی ریفائنری مصنوعات کو عمل انگیز کریکر سے گزارا جاتا ہے تاکہ بڑی مصنوعات کے طور پر گیسولین اور مٹی کا تیل اور ضمنی پیداوار پروپین حاصل ہو۔','د لویو ثابتو مالیکولونو ماتول کتلست ته اړتیا لري. د تصفیه خونې محصولات لکه ګاز آیل او فیول آیل د کتلستي کریکر څخه تېرېږي څو د اصلي محصولاتو په توګه ګازولین او د خاورو تېل او ضمني محصول پروپین ترلاسه شي.')
record=section('22.4','Parathion, petrochemicals and cracking','پیراتھیون، پیٹرو کیمیکلز اور کریکنگ','پاراتیون، پټرو کیمیکلونه او کریکنګ',paras,layout,blocks,'316–317')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':161,'printedPages':[316,317]}]
record['sourceContinuesOnPdfPage']=162
carry=[{'from':'22.4','to':'22.5','startsAt':'II. Reforming Process'}]
if __name__=='__main__':save(161,[record],carry=carry,chapter_number=22)
