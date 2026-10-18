"""PDF141 printed276–277: glycosidic bond (maltose), polysaccharides, 21.1.2 functions, 21.1.3 nutritional importance."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow141');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows,kind='list'):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':kind,'indices':list(range(s0,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'glycosidic bond':('گلائیکوسائیڈک بند','ګلایکوسایډیک تړون'),'maltose':('مالٹوز','مالټوز'),'sucrose':('سکروز','سوکروز'),'glucose':('گلوکوز','ګلوکوز'),'Acid':('تیزاب','اسید'),
   'Carbohydrate':('کاربوہائیڈریٹ','کاربوهایدرېټ'),'(Oxidation)':('(تکسید)','(اکسیډېشن)'),'Energy':('توانائی','انرژي')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def sub(x,y,dx,dy,lab):return line(x,y,x+dx,y+dy)+t(x+dx*1.6,y+dy*1.6+5,lab,13)
def pyran(ox,oy,left='OH',right='H'):
 V=[(ox,oy),(ox+120,oy),(ox+170,oy+40),(ox+120,oy+80),(ox,oy+80),(ox-50,oy+40)]
 s=''.join(line(*V[i],*V[(i+1)%6]) for i in range(6))+f'<circle cx="{ox+120}" cy="{oy}" r="11" fill="#fff"/>'+t(ox+120,oy+6,'O',15)
 s+=sub(ox,oy,0,-20,'CH₂OH')+sub(ox,oy+80,0,-18,'OH')+sub(ox,oy+80,0,20,'H')+sub(ox+120,oy+80,0,-18,'H')+sub(ox+120,oy+80,0,20,'OH')
 s+=sub(ox-50,oy+40,-18,-12,'H')+(sub(ox-50,oy+40,-18,12,left) if left else '')+sub(ox+170,oy+40,16,-12,'H')
 return s,(ox+170,oy+40)
def maltose(lang):
 s=F.start(200)
 a,(x1,y1)=pyran(110,50);b,(x2,y2)=pyran(450,50,None)
 s+=a+b
 s+=line(x1,y1,x1+40,y1+30)+t(x1+56,y1+36,'O',15)+line(x1+70,y1+30,400,90)
 s+=sub(620,90,16,12,'OH')+t(x1+56,y1+60,lb(lang,'glycosidic bond'),12)+t(400,190,lb(lang,'maltose'),12)
 return s+'</svg>'
def poly(lang):
 s=F.start(90)+t(240,50,'n (C₁₂H₂₂O₁₁)  +  nH₂O',16)+t(230,72,lb(lang,'sucrose'),12)+F.arrow(370,480,44,lb(lang,'Acid'))+t(570,50,'n C₆H₁₂O₆',16)+t(570,72,lb(lang,'glucose'),12)
 return s+'</svg>'
def oxid(lang):
 s=F.start(70)+t(220,45,lb(lang,'Carbohydrate')+'  +  O₂',16)+F.arrow(330,450,39,lb(lang,'(Oxidation)'))+t(600,45,'CO₂  +  H₂O  +  '+lb(lang,'Energy'),16)
 return s+'</svg>'
def atp(lang):
 s=F.start(80)+t(250,40,'C₆H₁₂O₆  +  6O₂',16)+F.arrow(350,460,34)+t(600,40,'6CO₂  +  6H₂O  +  '+lb(lang,'Energy'),16)+t(690,62,'(ATP)',12)
 return s+'</svg>'

add('… called glycosidic linkage or glycosidic bond e.g. two glucose units combined by a glycosidic bond to form maltose as shown below.','… گلائیکوسائیڈک ربط یا گلائیکوسائیڈک بند کہتے ہیں، مثلاً دو گلوکوز اکائیاں گلائیکوسائیڈک بند سے جڑ کر مالٹوز بناتی ہیں جیسا کہ نیچے دکھایا گیا ہے۔','… ګلایکوسایډیک اړیکه یا ګلایکوسایډیک تړون وايي، لکه دوه ګلوکوز واحدونه د ګلایکوسایډیک تړون په واسطه یو ځای کېږي او مالټوز جوړوي لکه څنګه چې لاندې ښودل شوي.')
visual('chem12-p141-maltose',maltose)
add('Polysaccharides','پولی سیکرائیڈز','پولي ساکاریډونه','heading')
lines([('A polysaccharide is a complex class of carbohydrate that contains many monosaccharide units covalently bonded to each other. The number of monosaccharide units present in a polysaccharide varies from above ten units to more than hundreds units.','پولی سیکرائیڈ کاربوہائیڈریٹ کی ایک پیچیدہ جماعت ہے جس میں بہت سی مونوسیکرائیڈ اکائیاں ایک دوسرے سے شریک گرفتی بند سے جڑی ہوتی ہیں۔ پولی سیکرائیڈ میں موجود مونوسیکرائیڈ اکائیوں کی تعداد دس سے زیادہ سے لے کر سینکڑوں سے زیادہ تک ہوتی ہے۔','پولي ساکاریډ د کاربوهایدرېټ یوه پېچلې ډله ده چې ډېر مونوساکاریډ واحدونه لري چې له یو بل سره په کوولانټ تړون تړلي دي. په پولي ساکاریډ کې د مونوساکاریډ واحدونو شمېر له لسو ډېر څخه تر سلګونو ډېر پورې توپیر کوي.'),
 ('Polysaccharides, like disaccharides and oligosaccharides, undergo hydrolysis under appropriate conditions to produce monosaccharides.','پولی سیکرائیڈز، ڈائی سیکرائیڈز اور اولیگوسیکرائیڈز کی طرح، مناسب حالات میں ہائیڈرولائسز سے مونوسیکرائیڈز پیدا کرتے ہیں۔','پولي ساکاریډونه د ډای ساکاریډونو او اولیګوساکاریډونو په څېر په مناسبو شرایطو کې هایدرولایز کېږي او مونوساکاریډونه تولیدوي.'),
 ('Both cellulose and starch are naturally occurring polysaccharides that are very prevalent in the world of plants.','سیلولوز اور نشاستہ دونوں قدرتی پولی سیکرائیڈز ہیں جو پودوں کی دنیا میں بہت عام ہیں۔','سلولوز او نشایسته دواړه طبیعي پولي ساکاریډونه دي چې د بوټو په نړۍ کې ډېر عام دي.'),
 ('The paper is mainly cellulose, as is the cotton in clothing fabrics and the wood used in home construction.','کاغذ بنیادی طور پر سیلولوز ہے، جیسا کہ کپڑوں میں روئی اور گھروں کی تعمیر میں استعمال ہونے والی لکڑی۔','کاغذ اساساً سلولوز دی، لکه د جامو په ټوکرو کې مالوچ او د کورونو په جوړولو کې کارېدونکی لرګی.'),
 ('Starch is a component of many types of foods, including bread, potatoes, rice, corn, beans and peas.','نشاستہ بہت سی اقسام کی خوراک کا جزو ہے جن میں روٹی، آلو، چاول، مکئی، پھلیاں اور مٹر شامل ہیں۔','نشایسته د ډېرو ډولونو خوړو برخه ده، چې ډوډۍ، کچالو، وریجې، جوار، لوبیا او مټر پکې شامل دي.')])
visual('chem12-p141-polysaccharide-hydrolysis',poly)
add('21.1.2 Functions','21.1.2 افعال','21.1.2 دندې','heading')
add('Basic function of carbohydrates is the production of energy for the performance of vital activities in living organisms. They are also known as ‘fuel of life’ because they produce energy by the process of oxidation.','کاربوہائیڈریٹس کا بنیادی فعل جانداروں میں حیاتی سرگرمیوں کی انجام دہی کے لیے توانائی پیدا کرنا ہے۔ انہیں ’زندگی کا ایندھن‘ بھی کہا جاتا ہے کیونکہ یہ تکسید کے عمل سے توانائی پیدا کرتے ہیں۔','د کاربوهایدرېټونو بنسټیزه دنده په ژوندیو موجوداتو کې د حیاتي فعالیتونو د ترسره کولو لپاره د انرژۍ تولید دی. دوی ته ’د ژوند سونګ‘ هم ویل کېږي ځکه د اکسیډېشن د عملیې په واسطه انرژي تولیدوي.')
visual('chem12-p141-carbohydrate-oxidation',oxid)
add('These are chief sources of energy, therefore, they spare proteins and lipids for other important functions of the body. Some important functions are given below.','یہ توانائی کے اہم ذرائع ہیں، اس لیے یہ پروٹینز اور لپڈز کو جسم کے دوسرے اہم افعال کے لیے بچا لیتے ہیں۔ چند اہم افعال نیچے دیے گئے ہیں۔','دا د انرژۍ اصلي سرچینې دي، نو پروټینونه او لیپیډونه د بدن د نورو مهمو دندو لپاره خوندي ساتي. ځینې مهمې دندې لاندې ورکړل شوې.')
lines([('Glucose is used as an immediate source of energy for the sick and sportsmen. It is also used in the manufacture of jams and sweets.','گلوکوز بیماروں اور کھلاڑیوں کے لیے توانائی کے فوری ذریعے کے طور پر استعمال ہوتا ہے۔ یہ جیم اور مٹھائیوں کی تیاری میں بھی استعمال ہوتا ہے۔','ګلوکوز د ناروغانو او لوبغاړو لپاره د انرژۍ د سمدستي سرچینې په توګه کارېږي. د مربا او خوږو په جوړولو کې هم کارېږي.'),
 ('Fructose is used as a sweetening agent in confectionary, in medicinal syrup. It is also used to prevent sandiness in ice-creams. It is also used as a substitute of table sugar (sucrose) for the obese and the diabetic.','فرکٹوز مٹھائیوں اور دوائی شربت میں مٹھاس پیدا کرنے والے عامل کے طور پر استعمال ہوتا ہے۔ یہ آئس کریم میں ریتلے پن کو روکنے کے لیے بھی استعمال ہوتا ہے۔ موٹاپے اور ذیابیطس کے مریضوں کے لیے یہ میز کی شکر (سکروز) کے متبادل کے طور پر بھی استعمال ہوتا ہے۔','فرکټوز په خوږو او درملیزو شربتونو کې د خوږوونکي عامل په توګه کارېږي. په آیسکریم کې د شګلنتوب د مخنیوي لپاره هم کارېږي. د چاغو او شکري ناروغانو لپاره د مېز د بورې (سوکروز) د بدیل په توګه هم کارېږي.'),
 ('Sucrose is used as a food and as ingredient of jams, jellies, confectionaries, syrup. It is also used in the preparation of sucrose octaacetate, which is used for the denaturation of alcohols and for making anhydrous adhesives.','سکروز خوراک کے طور پر اور جیم، جیلی، مٹھائیوں اور شربت کے جزو کے طور پر استعمال ہوتا ہے۔ یہ سکروز اوکٹا ایسیٹیٹ کی تیاری میں بھی استعمال ہوتا ہے، جو الکوحلز کو ناقابلِ استعمال بنانے اور بے آب چپکنے والے مادے بنانے کے لیے استعمال ہوتا ہے۔','سوکروز د خوړو په توګه او د مربا، جیلي، خوږو او شربت د اجزاوو په توګه کارېږي. د سوکروز اوکټا اسیټېټ په جوړولو کې هم کارېږي، چې د الکولونو د ډینېچر کولو او د بې اوبو سرېښونو د جوړولو لپاره کارېږي.'),
 ('Starch is principally used as a food. It is industrially used for manufacturing of ethanui by the process of fermentation. It is also used as a stiffening agent in textile industry and in laundry. It is also used as an adhesive to fasten paper.','نشاستہ بنیادی طور پر خوراک کے طور پر استعمال ہوتا ہے۔ صنعتی طور پر یہ تخمیر کے عمل سے ایتھانول کی تیاری کے لیے استعمال ہوتا ہے۔ یہ کپڑے کی صنعت اور دھلائی میں سختی دینے والے عامل کے طور پر بھی استعمال ہوتا ہے۔ کاغذ جوڑنے کے لیے یہ چپکنے والے مادے کے طور پر بھی استعمال ہوتا ہے۔','نشایسته اساساً د خوړو په توګه کارېږي. په صنعت کې د تخمیر د عملیې په واسطه د ایتانول د جوړولو لپاره کارېږي. د ټوکر په صنعت او مینځلو کې د کلکوونکي عامل په توګه هم کارېږي. د کاغذ د نښلولو لپاره د سرېښ په توګه هم کارېږي.'),
 ('Cellulose has no food value but is used as a roughage in our diet for promoting the peristaltic motion of digestive tract. It is used for the manufacturing of paper.','سیلولوز کی کوئی غذائی قدر نہیں لیکن یہ نظامِ ہضم کی پیرسٹالٹک حرکت کو فروغ دینے کے لیے ہماری خوراک میں ریشے کے طور پر استعمال ہوتا ہے۔ یہ کاغذ کی تیاری کے لیے استعمال ہوتا ہے۔','سلولوز غذايي ارزښت نه لري خو زموږ په خوړو کې د هاضمې لارې د پېریسټالټیک حرکت د پیاوړتیا لپاره د ریښو په توګه کارېږي. د کاغذ د جوړولو لپاره کارېږي.'),
 ('Oligosaccharides are involved in the formation of secreted proteins like antibodies and blood clotting factors.','اولیگوسیکرائیڈز اینٹی باڈیز اور خون جمانے والے عوامل جیسے خارج ہونے والے پروٹینز کی تشکیل میں شامل ہیں۔','اولیګوساکاریډونه د افرازي پروټینونو لکه انټي باډیو او د وینې د غوټه کېدو د عواملو په جوړولو کې ونډه لري.'),
 ('The receptors on the cell membrane are the complexes of carbohydrates with certain proteins. The receptors are involved in molecular targeting or molecular recognition.','خلیے کی جھلی پر موجود ریسیپٹرز بعض پروٹینز کے ساتھ کاربوہائیڈریٹس کے کمپلیکس ہیں۔ ریسیپٹرز سالماتی ہدف بندی یا سالماتی شناخت میں شامل ہیں۔','د حجرې پر غشا اخیستونکي له ځینو پروټینونو سره د کاربوهایدرېټونو کمپلېکسونه دي. اخیستونکي په مالیکولي هدف ټاکنه یا مالیکولي پېژندنه کې ونډه لري.')])
add('21.1.3 Nutritional Importance','21.1.3 غذائی اہمیت','21.1.3 غذايي اهمیت','heading')
add('Carbohydrates are the most important energy containing nutrients for living organisms. Plant contains stored carbohydrates called starch while animals contain stored carbohydrates called glycogen. Both, these polymers are broken down into the simplest monosaccharide units known as glucose, before oxidation. Then glucose is oxidized in the body cells by different types of pathways (series of enzymatic chemical reactions) to release energy. This energy is stored in the form of molecules known as ATP (adenosine triphosphate) in the different parts of the body.',
 'کاربوہائیڈریٹس جانداروں کے لیے توانائی رکھنے والے سب سے اہم غذائی اجزا ہیں۔ پودوں میں ذخیرہ شدہ کاربوہائیڈریٹس کو نشاستہ کہتے ہیں جبکہ جانوروں میں ذخیرہ شدہ کاربوہائیڈریٹس کو گلائیکوجن کہتے ہیں۔ یہ دونوں پولیمر تکسید سے پہلے سادہ ترین مونوسیکرائیڈ اکائیوں یعنی گلوکوز میں توڑے جاتے ہیں۔ پھر جسم کے خلیوں میں گلوکوز کی مختلف راستوں (خامروں سے ہونے والے کیمیائی تعاملات کا سلسلہ) سے تکسید ہوتی ہے اور توانائی خارج ہوتی ہے۔ یہ توانائی جسم کے مختلف حصوں میں ATP (ایڈینوسین ٹرائی فاسفیٹ) کہلانے والے سالمات کی صورت میں ذخیرہ ہوتی ہے۔',
 'کاربوهایدرېټونه د ژوندیو موجوداتو لپاره تر ټولو مهم انرژي لرونکي غذايي مواد دي. بوټي زېرمه شوي کاربوهایدرېټونه لري چې نشایسته بلل کېږي، په داسې حال کې چې ژوي زېرمه شوي کاربوهایدرېټونه لري چې ګلایکوجن بلل کېږي. دا دواړه پولیمرونه له اکسیډېشن مخکې تر ټولو ساده مونوساکاریډ واحدونو یعنې ګلوکوز ته ماتېږي. بیا ګلوکوز د بدن په حجرو کې د بېلابېلو لارو (د انزایمي کیمیاوي تعاملونو لړۍ) په واسطه اکسیډایز کېږي او انرژي خوشې کوي. دا انرژي د بدن په بېلابېلو برخو کې د ATP (اډینوسین ټرای فاسفېټ) په نوم مالیکولونو په بڼه زېرمه کېږي.')
add('Tidbit — Adenosine Triphosphate','مختصر معلومات — ایڈینوسین ٹرائی فاسفیٹ','لنډ معلومات — اډینوسین ټرای فاسفېټ','heading')
add('Adenosine triphosphate, also known as ATP, is a molecule that carries energy within cells. It is the main energy currency of the cell and it is an end product of the processes of photophosphorylation (adding a phosphate group to a molecule using energy from light), cellular respiration and fermentation. All living things use ATP. It is also used in signal convert pathways for cell communication and is incorporated into deoxyribonucleic acid (DNA) during DNA synthesis.',
 'ایڈینوسین ٹرائی فاسفیٹ، جسے ATP بھی کہتے ہیں، ایک سالمہ ہے جو خلیوں کے اندر توانائی منتقل کرتا ہے۔ یہ خلیے کی توانائی کی بنیادی کرنسی ہے اور فوٹو فاسفوریلیشن (روشنی کی توانائی سے سالمے میں فاسفیٹ گروپ کا اضافہ)، خلوی تنفس اور تخمیر کے عمل کی آخری پیداوار ہے۔ تمام جاندار ATP استعمال کرتے ہیں۔ یہ خلوی رابطے کے سگنل راستوں میں بھی استعمال ہوتا ہے اور DNA کی تالیف کے دوران ڈی آکسی رائبونیوکلک ایسڈ (DNA) میں شامل ہو جاتا ہے۔',
 'اډینوسین ټرای فاسفېټ چې ATP هم بلل کېږي، یو مالیکول دی چې په حجرو کې انرژي لېږدوي. دا د حجرې د انرژۍ اصلي پیسې دي او د فوټو فاسفوریلېشن (د رڼا د انرژۍ په کارولو سره مالیکول ته د فاسفېټ ګروپ زیاتول)، حجروي تنفس او تخمیر د عملیو وروستی محصول دی. ټول ژوندي موجودات ATP کاروي. د حجروي اړیکو د سیګنال په لارو کې هم کارېږي او د DNA د جوړېدو پر مهال په ډی اکسي رایبونیوکلیک اسید (DNA) کې شاملېږي.')
visual('chem12-p141-glucose-oxidation-atp',atp)
add('One mole of glucose on complete oxidation by citric acid cycle produces 36 ATPs.','سٹرک ایسڈ سائیکل کے ذریعے گلوکوز کے ایک مول کی مکمل تکسید سے 36 ATP بنتے ہیں۔','د سیټریک اسید د دورې په واسطه د ګلوکوز د یوه مول بشپړ اکسیډېشن 36 ATP تولیدوي.')
record=section('21.3','Glycosidic bond, polysaccharides, functions and nutritional importance','گلائیکوسائیڈک بند، پولی سیکرائیڈز، افعال اور غذائی اہمیت','ګلایکوسایډیک تړون، پولي ساکاریډونه، دندې او غذايي اهمیت',paras,layout,blocks,'276–277')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':141,'printedPages':[276,277]}]
record['sourceContinuesOnPdfPage']=142
issues=[{'id':'chem12-p276-printing','printedPage':276,'description':'Polysaccharide hydrolysis equation labels n(C₁₂H₂₂O₁₁) as "sucrose"; "ethanui" (ethanol) in the starch bullet; both retained as printed.'}]
carry=[{'from':'21.3','to':'21.4','startsAt':'Role of Various Carbohydrates in Health'}]
if __name__=='__main__':save(141,[record],carry=carry,issues=issues,chapter_number=21)
