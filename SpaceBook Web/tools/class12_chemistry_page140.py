"""PDF140 printed274–275: carbohydrate definition, 21.1.1 classification — monosaccharides, trioses, oligosaccharides, glycosidic linkage."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
import math
F=Fig('arrow140');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows,kind='list'):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':kind,'indices':list(range(s0,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Glucose (open chain form)':('گلوکوز (کھلی زنجیر صورت)','ګلوکوز (خلاص ځنځیر بڼه)'),'Glucose (cyclic form)':('گلوکوز (حلقوی صورت)','ګلوکوز (حلقوي بڼه)'),'Fructose (open chain form)':('فرکٹوز (کھلی زنجیر صورت)','فرکټوز (خلاص ځنځیر بڼه)'),
   'Fructose (cyclic form)':('فرکٹوز (حلقوی صورت)','فرکټوز (حلقوي بڼه)'),'Glyceraldehyde':('گلیسرالڈیہائیڈ','ګلیسرالدیهاید'),'(an aldose)':('(ایک الڈوز)','(یو الدوز)'),'Dihydroxyacetone':('ڈائی ہائیڈروآکسی ایسیٹون','ډای هایدروکسي اسیتون'),
   '(a ketose)':('(ایک کیٹوز)','(یو کیټوز)'),'Glycerol':('گلیسرول','ګلیسرول'),'maltose':('مالٹوز','مالټوز'),'glucose':('گلوکوز','ګلوکوز'),'sucrose':('سکروز','سوکروز'),'fructose':('فرکٹوز','فرکټوز')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def fischer(x,y,top,rows,bottom,gap=30):
 """Vertical Fischer chain: top label, rows of (left,right) on C, bottom label."""
 s=t(x,y,top,14);yy=y
 for l,r in rows:
  s+=line(x,yy+6,x,yy+gap-14);yy+=gap
  s+=t(x,yy,'C',14)+(line(x-8,yy-5,x-26,yy-5)+t(x-44,yy,l,13) if l else '')+(line(x+8,yy-5,x+26,yy-5)+t(x+46,yy,r,13) if r else '')
 return s+line(x,yy+6,x,yy+gap-14)+t(x,yy+gap,bottom,14)
def sugars(lang):
 s=F.start(520)
 # glucose open chain
 s+=t(150,30,'H',14)+line(156,34,166,46)+t(170,58,'C',14)+line(176,50,190,36)+line(180,52,194,38)+t(200,30,'O',14)
 s+=fischer(170,58,'',[('H','OH'),('OH','H'),('H','OH'),('H','OH')],'CH₂OH').replace(t(170,58,'',14),'')+t(170,240,lb(lang,'Glucose (open chain form)'),12)
 s+=F.eq(280,360,140)
 # glucose pyranose drawn skeletally, O at upper right
 V=[(490,80),(620,80),(680,125),(620,170),(490,170),(430,125)]
 for i in range(6):s+=line(*V[i],*V[(i+1)%6])
 s+='<circle cx="620" cy="80" r="11" fill="#fff"/>'+t(620,86,'O',15)
 def sub(x,y,dx,dy,lab):return line(x,y,x+dx,y+dy)+t(x+dx*1.6,y+dy*1.6+5,lab,13)
 s+=sub(490,80,0,-22,'CH₂OH')+sub(490,80,0,0,'')
 s+=sub(680,125,22,-14,'OH')+sub(680,125,22,14,'H')
 s+=sub(620,170,0,-20,'H')+sub(620,170,0,20,'OH')+sub(490,170,0,-20,'OH')+sub(490,170,0,20,'H')
 s+=sub(430,125,-22,-14,'H')+sub(430,125,-22,14,'OH')+t(560,240,lb(lang,'Glucose (cyclic form)'),12)
 # fructose open chain
 y0=300;s+=t(170,y0,'CH₂OH',14)+line(170,y0+6,170,y0+16)+t(170,y0+30,'C',14)+line(178,y0+22,200,y0+22)+line(178,y0+28,200,y0+28)+t(214,y0+30,'O',14)
 yy=y0+30
 for l,rr in (('HO','H'),('H','OH'),('H','OH')):
  s+=line(170,yy+6,170,yy+16);yy+=30;s+=t(170,yy,'C',14)+line(162,yy-5,144,yy-5)+t(126,yy,l,13)+line(178,yy-5,196,yy-5)+t(214,yy,rr,13)
 s+=line(170,yy+6,170,yy+16)+t(170,yy+30,'CH₂OH',14)+t(170,yy+52,lb(lang,'Fructose (open chain form)'),12)
 s+=F.eq(280,360,410)
 # fructose furanose drawn skeletally, O at top
 V=[(560,330),(615,365),(595,425),(525,425),(505,365)]
 for i in range(5):s+=line(*V[i],*V[(i+1)%5])
 s+='<circle cx="560" cy="330" r="11" fill="#fff"/>'+t(560,336,'O',15)
 def sub(x,y,dx,dy,lab):return line(x,y,x+dx,y+dy)+t(x+dx*1.7,y+dy*1.7+5,lab,13)
 s+=sub(615,365,16,-16,'OH')+sub(615,365,24,8,'CH₂OH')+sub(505,365,-24,-8,'CH₂OH')
 s+=sub(595,425,0,-18,'OH')+sub(595,425,0,20,'H')+sub(525,425,0,-18,'H')+sub(525,425,0,20,'OH')+t(560,500,lb(lang,'Fructose (cyclic form)'),12)
 return s+'</svg>'
def trioses(lang):
 s=F.start(180)
 for x,(a,b,c),n1,n2 in ((180,('CH=O','CHOH','CH₂OH'),'Glyceraldehyde','(an aldose)'),(420,('CH₂OH','C=O','CH₂OH'),'Dihydroxyacetone','(a ketose)'),(660,('CH₂OH','CHOH','CH₂OH'),'Glycerol',None)):
  s+=t(x,30,a,15)+line(x-20,36,x-20,54)+t(x,72,b,15)+line(x-20,78,x-20,96)+t(x,114,c,15)+t(x,144,lb(lang,n1),12)+(t(x,160,lb(lang,n2),12) if n2 else '')
 return s+'</svg>'
def hyd(lang):
 s=F.start(170)+t(260,50,'C₁₂H₂₂O₁₁  +  H₂O',16)+t(200,72,lb(lang,'maltose'),12)+F.arrow(380,480,44)+t(560,50,'2C₆H₁₂O₆',16)+t(560,72,lb(lang,'glucose'),12)
 s+=t(260,130,'C₁₂H₂₂O₁₁  +  H₂O',16)+t(200,152,lb(lang,'sucrose'),12)+F.arrow(380,480,124)+t(600,130,'C₆H₁₂O₆  +  C₆H₁₂O₆',16)+t(540,152,lb(lang,'glucose'),12)+t(660,152,lb(lang,'fructose'),12)
 return s+'</svg>'

add('… having molecular formula C₅H₁₀O₄ cannot be represented by Cₙ(H₂O)ₙ formula. On the other hand, there are also some compounds which follow this Cₙ(H₂O)ₙ formula but they are not carbohydrates, for example formaldehyde (CH₂O) and acetic acid (C₂H₄O₂) [formaldehyde can be written as C(H₂O) and acetic acid as C₂(H₂O)₂].',
 '… جو کاربوہائیڈریٹس ہیں لیکن اس عمومی فارمولے کی پیروی نہیں کرتے۔ مثلاً 2-ڈی آکسی رائبوز جس کا سالماتی فارمولا C₅H₁₀O₄ ہے، Cₙ(H₂O)ₙ فارمولے سے ظاہر نہیں کیا جا سکتا۔ دوسری طرف کچھ مرکبات اس Cₙ(H₂O)ₙ فارمولے کی پیروی کرتے ہیں لیکن کاربوہائیڈریٹس نہیں ہیں، مثلاً فارم الڈیہائیڈ (CH₂O) اور ایسیٹک ایسڈ (C₂H₄O₂) [فارم الڈیہائیڈ کو C(H₂O) اور ایسیٹک ایسڈ کو C₂(H₂O)₂ لکھا جا سکتا ہے]۔',
 '… چې کاربوهایدرېټونه دي خو دا عمومي فورمول نه تعقیبوي. د بېلګې په توګه 2-ډی اکسي رایبوز چې مالیکولي فورمول یې C₅H₁₀O₄ دی، د Cₙ(H₂O)ₙ فورمول په واسطه نه شي ښودل کېدای. له بلې خوا ځینې مرکبات شته چې دا Cₙ(H₂O)ₙ فورمول تعقیبوي خو کاربوهایدرېټونه نه دي، لکه فورمالدیهاید (CH₂O) او اسیټیک اسید (C₂H₄O₂) [فورمالدیهاید د C(H₂O) او اسیټیک اسید د C₂(H₂O)₂ په توګه لیکل کېدای شي].')
paras[-1]['text']='… carbohydrates but they do not follow this general formula. For example, 2-deoxyribose having molecular formula C₅H₁₀O₄ cannot be represented by Cₙ(H₂O)ₙ formula. On the other hand, there are also some compounds which follow this Cₙ(H₂O)ₙ formula but they are not carbohydrates, for example formaldehyde (CH₂O) and acetic acid (C₂H₄O₂) [formaldehyde can be written as C(H₂O) and acetic acid as C₂(H₂O)₂].'
add('Hence, carbohydrates are polyhydroxy aldehydes (aldoses), or polyhydroxy ketones (ketoses) or compounds that give such compounds on hydrolysis. The hydroxyl group and the carbonyl group are the major functional groups in carbohydrates.','لہٰذا کاربوہائیڈریٹس پولی ہائیڈروآکسی الڈیہائیڈز (الڈوزز)، یا پولی ہائیڈروآکسی کیٹونز (کیٹوزز) یا ایسے مرکبات ہیں جو ہائیڈرولائسز پر ایسے مرکبات دیتے ہیں۔ ہائیڈروآکسل گروپ اور کاربونل گروپ کاربوہائیڈریٹس کے بڑے فعلی گروپ ہیں۔','نو کاربوهایدرېټونه پولي هایدروکسي الدیهایډونه (الدوزونه)، یا پولي هایدروکسي کیټونونه (کیټوزونه) یا هغه مرکبات دي چې د هایدرولایسس پر مهال داسې مرکبات ورکوي. هایدروکسیل ګروپ او کاربونیل ګروپ د کاربوهایدرېټونو لوی فعال ګروپونه دي.')
add('21.1.1 Classification','21.1.1 درجہ بندی','21.1.1 ډلبندي','heading')
add('Carbohydrates are classified on the basis of the number of simple sugar units present per molecule as monosaccharides, oligosaccharides and polysaccharides.','کاربوہائیڈریٹس کو فی سالمہ موجود سادہ شکر اکائیوں کی تعداد کی بنیاد پر مونوسیکرائیڈز، اولیگوسیکرائیڈز اور پولی سیکرائیڈز میں درجہ بند کیا جاتا ہے۔','کاربوهایدرېټونه په هر مالیکول کې د شته ساده بورې واحدونو د شمېر پر بنسټ په مونوساکاریډونو، اولیګوساکاریډونو او پولي ساکاریډونو ډلبندي کېږي.')
add('1. Monosaccharides','1. مونوسیکرائیڈز','1. مونوساکاریډونه','heading')
lines([('They are also called simple sugars. They contain only one sugar unit per molecule. They cannot be broken down into more simpler carbohydrates on hydrolysis. For example, glucose, fructose etc.','انہیں سادہ شکر بھی کہتے ہیں۔ ان میں فی سالمہ صرف ایک شکر اکائی ہوتی ہے۔ ہائیڈرولائسز پر انہیں مزید سادہ کاربوہائیڈریٹس میں توڑا نہیں جا سکتا۔ مثلاً گلوکوز، فرکٹوز وغیرہ۔','دوی ته ساده بوره هم وايي. په هر مالیکول کې یوازې یو د بورې واحد لري. د هایدرولایسس پر مهال په لا ساده کاربوهایدرېټونو نه ماتېږي. د بېلګې په توګه ګلوکوز، فرکټوز او نور.')])
visual('chem12-p140-glucose-fructose',sugars)
lines([('The monosaccharides are again subdivided on the basis of the type of functional group and the number of carbon atoms in the molecule.','مونوسیکرائیڈز کو پھر فعلی گروپ کی قسم اور سالمے میں کاربن ایٹموں کی تعداد کی بنیاد پر ذیلی تقسیم کیا جاتا ہے۔','مونوساکاریډونه بیا د فعال ګروپ د ډول او په مالیکول کې د کاربني اټومونو د شمېر پر بنسټ فرعي وېشل کېږي.'),
 ('On the basis of types of functional group monosaccharides may be classified as aldoses or ketoses. There are only two trioses: glyceraldehyde and dihydroxyacetone. Each has two hydroxyl groups, attached to different carbon atoms and one carbonyl group.','فعلی گروپ کی اقسام کی بنیاد پر مونوسیکرائیڈز کو الڈوزز یا کیٹوزز میں درجہ بند کیا جا سکتا ہے۔ صرف دو ٹرائیوزز ہیں: گلیسرالڈیہائیڈ اور ڈائی ہائیڈروآکسی ایسیٹون۔ ہر ایک میں مختلف کاربن ایٹموں سے جڑے دو ہائیڈروآکسل گروپ اور ایک کاربونل گروپ ہوتا ہے۔','د فعال ګروپ د ډولونو پر بنسټ مونوساکاریډونه په الدوزونو یا کیټوزونو ډلبندي کېدای شي. یوازې دوه ټرایوزونه شته: ګلیسرالدیهاید او ډای هایدروکسي اسیتون. هر یو له بېلابېلو کاربني اټومونو سره تړلي دوه هایدروکسیل ګروپونه او یو کاربونیل ګروپ لري.')])
visual('chem12-p140-trioses',trioses)
lines([('Similarly, on the basis of number of carbon atom in a molecule monosaccharides may be trioses, tetroses, pentoses, hexoses and so on.','اسی طرح سالمے میں کاربن ایٹموں کی تعداد کی بنیاد پر مونوسیکرائیڈز ٹرائیوزز، ٹیٹروزز، پینٹوزز، ہیکسوزز وغیرہ ہو سکتے ہیں۔','همدارنګه په مالیکول کې د کاربني اټومونو د شمېر پر بنسټ مونوساکاریډونه ټرایوزونه، ټېټروزونه، پېنټوزونه، هېکسوزونه او داسې نور کېدای شي.')])
add('2. Oligosaccharide','2. اولیگوسیکرائیڈ','2. اولیګوساکاریډ','heading')
lines([('An oligosaccharide is a carbohydrate that contains two to ten monosaccharide units covalently bonded to each other.','اولیگوسیکرائیڈ وہ کاربوہائیڈریٹ ہے جس میں دو سے دس مونوسیکرائیڈ اکائیاں ایک دوسرے سے شریک گرفتی بند سے جڑی ہوتی ہیں۔','اولیګوساکاریډ هغه کاربوهایدرېټ دی چې له دوو تر لسو مونوساکاریډ واحدونه لري چې له یو بل سره په کوولانټ تړون تړلي دي.'),
 ('Disaccharides are the most common type of oligosaccharide.','ڈائی سیکرائیڈز اولیگوسیکرائیڈ کی سب سے عام قسم ہیں۔','ډای ساکاریډونه د اولیګوساکاریډ تر ټولو عام ډول دی.'),
 ('A disaccharide is a carbohydrate that contains two monosaccharide units covalently bonded to each other. Like monosaccharides, disaccharides are crystalline, water-soluble substances. Sucrose (table sugar) and lactose (milk sugar) are disaccharides.','ڈائی سیکرائیڈ وہ کاربوہائیڈریٹ ہے جس میں دو مونوسیکرائیڈ اکائیاں ایک دوسرے سے شریک گرفتی بند سے جڑی ہوتی ہیں۔ مونوسیکرائیڈز کی طرح ڈائی سیکرائیڈز قلمی اور پانی میں حل پذیر مادے ہیں۔ سکروز (میز کی شکر) اور لیکٹوز (دودھ کی شکر) ڈائی سیکرائیڈز ہیں۔','ډای ساکاریډ هغه کاربوهایدرېټ دی چې دوه مونوساکاریډ واحدونه لري چې له یو بل سره په کوولانټ تړون تړلي دي. د مونوساکاریډونو په څېر، ډای ساکاریډونه قلمي او په اوبو کې حلېدونکي مواد دي. سوکروز (د مېز بوره) او لاکټوز (د شیدو بوره) ډای ساکاریډونه دي.'),
 ('Those oligosaccharides, which contain three and four units of monosaccharides per molecule, are called trisaccharides and tetrasaccharides respectively.','وہ اولیگوسیکرائیڈز جن میں فی سالمہ مونوسیکرائیڈز کی تین اور چار اکائیاں ہوں، بالترتیب ٹرائی سیکرائیڈز اور ٹیٹرا سیکرائیڈز کہلاتے ہیں۔','هغه اولیګوساکاریډونه چې په هر مالیکول کې د مونوساکاریډونو درې او څلور واحدونه لري، په ترتیب سره ټرای ساکاریډونه او ټېټرا ساکاریډونه بلل کېږي.'),
 ('Complete hydrolysis of an oligosaccharide produces similar or different types of monosaccharides. For example, maltose yields the same kind of two glucose units upon hydrolysis.','اولیگوسیکرائیڈ کی مکمل ہائیڈرولائسز یکساں یا مختلف اقسام کے مونوسیکرائیڈز پیدا کرتی ہے۔ مثلاً مالٹوز ہائیڈرولائسز پر ایک ہی قسم کی دو گلوکوز اکائیاں دیتا ہے۔','د اولیګوساکاریډ بشپړ هایدرولایسس ورته یا بېلابېل ډولونه مونوساکاریډونه تولیدوي. د بېلګې په توګه مالټوز د هایدرولایسس پر مهال د یو ډول دوه ګلوکوز واحدونه ورکوي.'),
 ('While sucrose yields two different types of monosaccharides i.e. glucose and fructose upon hydrolysis.','جبکہ سکروز ہائیڈرولائسز پر دو مختلف اقسام کے مونوسیکرائیڈز یعنی گلوکوز اور فرکٹوز دیتا ہے۔','په داسې حال کې چې سوکروز د هایدرولایسس پر مهال دوه بېلابېل ډولونه مونوساکاریډونه یعنې ګلوکوز او فرکټوز ورکوي.')])
visual('chem12-p140-disaccharide-hydrolysis',hyd)
add('Glycosidic Linkage or Bond','گلائیکوسائیڈک ربط یا بند','ګلایکوسایډیک اړیکه یا تړون','heading')
add('During the formation of disaccharides, the two monosaccharaide units combine together by an oxygen atom with the elimination of one water molecule. This type of linkage is …','ڈائی سیکرائیڈز کے بننے کے دوران دو مونوسیکرائیڈ اکائیاں پانی کے ایک سالمے کے اخراج کے ساتھ ایک آکسیجن ایٹم کے ذریعے آپس میں جڑ جاتی ہیں۔ اس قسم کے ربط کو …','د ډای ساکاریډونو د جوړېدو پر مهال دوه مونوساکاریډ واحدونه د اوبو د یوه مالیکول په ایستلو سره د یوه اکسیجني اټوم په واسطه یو ځای کېږي. دې ډول اړیکې ته …')
record=section('21.2','Carbohydrate definition and classification','کاربوہائیڈریٹس کی تعریف اور درجہ بندی','د کاربوهایدرېټونو تعریف او ډلبندي',paras,layout,blocks,'274–275')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':140,'printedPages':[274,275]}]
record['sourceContinuesOnPdfPage']=141
carry=[{'from':'21.2','to':'21.3','startsAt':'called glycosidic linkage'}]
if __name__=='__main__':save(140,[record],carry=carry,chapter_number=21)
