"""PDF112 printed216–217: aromatic alcohols vs phenols, ethers, nomenclature, physical properties."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow112');t=F.t;line=F.line;ring=F.ring
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'phenylmethanol':('فینائل میتھانول','فینیل میتانول'),'(benzyl alcohol)':('(بینزائل الکوحل)','(بنزیل الکول)'),'2-phenylethanol':('2-فینائل ایتھانول','2-فینیل ایتانول'),'phenol':('فینول','فینول'),'o-cresol':('o-کریسول','o-کریسول'),
   'm-chlorophenol':('m-کلورو فینول','m-کلوروفینول'),'dimethyl ether':('ڈائی میتھائل ایتھر','ډای میتایل ایتر'),'ethyl methyl ether':('ایتھائل میتھائل ایتھر','ایتیل میتایل ایتر'),'methyl phenyl ether':('میتھائل فینائل ایتھر','میتایل فینیل ایتر'),
   '(anisole)':('(اینیسول)','(انیسول)'),'diethyl ether':('ڈائی ایتھائل ایتھر','ډای ایتیل ایتر'),'diphenyl ether':('ڈائی فینائل ایتھر','ډای فینیل ایتر'),'methoxymethane':('میتھوآکسی میتھین','میتوکسي میتان'),'methoxyethane':('میتھوآکسی ایتھین','میتوکسي ایتان'),
   'ethoxyethane':('ایتھوآکسی ایتھین','ایتوکسي ایتان'),'2-methoxypropane':('2-میتھوآکسی پروپین','2-میتوکسي پروپان'),'2-methoxy-3-methylbutane':('2-میتھوآکسی-3-میتھائل بیوٹین','2-میتوکسي-3-میتایل بیوټان'),
   'Alcohol':('الکوحل','الکول'),'Ether':('ایتھر','ایتر'),'water + ether':('پانی + ایتھر','اوبه + ایتر'),'hydrogen bond':('ہائیڈروجن بند','هایدروجني تړون'),'no hydrogen bond':('ہائیڈروجن بند نہیں','هایدروجني تړون نشته'),
   'donor':('دینے والا','ورکوونکی'),'acceptor':('لینے والا','اخیستونکی'),'no donor':('دینے والا نہیں','ورکوونکی نشته')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def lab(x,y,lang,*ws):return ''.join(t(x,y+15*i,lb(lang,w),12) for i,w in enumerate(ws))
def arom(lang):
 s=F.start(145)+ring(220,65,28)+line(248,65,265,65)+t(320,71,'CH₂—OH',15)+lab(240,116,lang,'phenylmethanol','(benzyl alcohol)')
 s+=ring(500,65,28)+line(528,65,545,65)+t(625,71,'CH₂—CH₂—OH',15)+lab(560,116,lang,'2-phenylethanol')
 return s+'</svg>'
def phenols(lang):
 s=F.start(150)
 for x,(sub,n) in zip((180,425,670),(({0:'OH'},'phenol'),({0:'OH',1:'CH₃'},'o-cresol'),({0:'OH',4:'Cl'},'m-chlorophenol'))):s+=ring(x,80,28,subs=sub)+lab(x,135,lang,n)
 return s+'</svg>'
def ethers(lang):
 s=F.start(110)+t(180,40,'CH₃—O—CH₃',16)+lab(180,62,lang,'dimethyl ether')+t(180,80,'(R–O–R)',12)+t(420,40,'CH₃—CH₂—O—CH₃',16)+lab(420,62,lang,'ethyl methyl ether')+t(420,80,"(R–O–R′)",12)
 s+=t(620,46,'CH₃—O—',16)+ring(705,40,24)+lab(670,82,lang,'methyl phenyl ether')
 return s+'</svg>'
def common(lang):
 s=F.start(140)
 for x,y,f,ns in ((150,35,'CH₃ – O – CH₃',['dimethyl ether']),(420,35,'CH₃ – CH₂ – O – CH₃',['ethyl methyl ether']),(690,35,'CH₃ – CH₂ – O – CH₂ – CH₃',['diethyl ether']),(420,95,'CH₃ – O – C₆H₅',['methyl phenyl ether','(anisole)']),(690,95,'C₆H₅ – O – C₆H₅',['diphenyl ether'])):
  s+=t(x,y,f,15)+lab(x,y+20,lang,*ns)
 return s+'</svg>'
def iupac(lang):
 s=F.start(230)+t(150,35,'CH₃ – O – CH₃',15)+lab(150,55,lang,'methoxymethane')+t(420,35,'CH₃ – CH₂ – O – CH₃',15)+lab(420,55,lang,'methoxyethane')+t(690,35,'CH₃ – CH₂ – O – CH₂ – CH₃',15)+lab(690,55,lang,'ethoxyethane')
 s+=chain(F,0,160,['CH₃','—','CH','—','O','—','CH₃'],15,{0:'1',2:'2'},{2:'³CH₃'},center=260)+lab(260,190,lang,'2-methoxypropane')
 s+=chain(F,0,160,['CH₃','—','CH','—','CH','—','CH₃'],15,{0:'4',2:'3',4:'2',6:'1'},{2:'CH₃',4:'OCH₃'},center=600)+lab(600,190,lang,'2-methoxy-3-methylbutane')
 return s+'</svg>'
def hbond(lang):
 s=F.start(190)+line(283,20,283,170,1.5,'#999')+line(566,20,566,170,1.5,'#999')
 for x,(title,a,b,mid,left,right) in zip((140,425,710),(('Alcohol','O—H','O','hydrogen bond','donor','acceptor'),('Ether','O—R','O','no hydrogen bond','no donor','acceptor'),('water + ether','O—H','O','hydrogen bond','donor','acceptor'))):
  s+=t(x,30,lb(lang,title),14,'#ad1457')+t(x-50,80,a,15)+t(x,80,'⋯⋯',15)+t(x+45,80,b,15)+t(x-70,110,'R' if title!='water + ether' else 'H',13)+t(x+55,58,'H' if title=='Alcohol' else 'R',13)+t(x+55,110,'R',13)
  s+=lab(x,140,lang,mid)+t(x-65,160,lb(lang,left),12)+t(x+60,160,lb(lang,right),12)
 return s+'</svg>'

add('Aromatic alcohols;','ارومیٹک الکوحلز؛','اروماتیک الکولونه؛')
visual('chem12-p112-aromatic-alcohols',arom)
add('Phenols;','فینولز؛','فینولونه؛')
visual('chem12-p112-phenols',phenols)
add('It should be noted that benzyl alcohol and cresols are also isomers. But benzyl alcohol is an aromatic alcohol, while cresols are phenols.','یاد رہے کہ بینزائل الکوحل اور کریسولز بھی آئسومر ہیں۔ لیکن بینزائل الکوحل ارومیٹک الکوحل ہے جبکہ کریسولز فینولز ہیں۔','د یادونې وړ ده چې بنزیل الکول او کریسولونه هم ایزومرونه دي. خو بنزیل الکول اروماتیک الکول دی، په داسې حال کې چې کریسولونه فینولونه دي.')
add('18.3 Ethers','18.3 ایتھرز','18.3 ایترونه','heading')
add('Ethers are a class of organic compounds in which the oxygen atom is linked to two alkyl groups or two aryl groups or one alkyl and one aryl group. Thus the functional group of ethers is C – O – C. They can be represented by the general formula R – O –R. Ethers are described as symmetrical or unsymmetrical depending on whether the two groups bonded to oxygen are the same or different. Unsymmetrical ethers are also called mixed ethers. Diethyl ether is a symmetrical ether; ethyl methyl ether is an unsymmetrical ether (R – O – R′). Examples of ethers are:',
 'ایتھرز نامیاتی مرکبات کی وہ جماعت ہیں جن میں آکسیجن ایٹم دو الکائل گروپوں یا دو ایرائل گروپوں یا ایک الکائل اور ایک ایرائل گروپ سے جڑا ہو۔ اس طرح ایتھرز کا فعلی گروپ C – O – C ہے۔ انہیں عمومی فارمولا R – O –R سے ظاہر کیا جا سکتا ہے۔ آکسیجن سے جڑے دونوں گروپ یکساں یا مختلف ہونے کے لحاظ سے ایتھرز کو متشاکل یا غیر متشاکل کہا جاتا ہے۔ غیر متشاکل ایتھرز کو مخلوط ایتھرز بھی کہتے ہیں۔ ڈائی ایتھائل ایتھر متشاکل ایتھر ہے؛ ایتھائل میتھائل ایتھر غیر متشاکل ایتھر (R – O – R′) ہے۔ ایتھرز کی مثالیں یہ ہیں:',
 'ایترونه د عضوي مرکباتو هغه ټولګی دی چې پکې اکسیجني اټوم له دوو الکایل ګروپونو یا دوو اریل ګروپونو یا یوه الکایل او یوه اریل ګروپ سره تړلی وي. نو د ایترونو فعال ګروپ C – O – C دی. د R – O –R عمومي فورمول په واسطه ښودل کېدای شي. له اکسیجن سره تړلي دوه ګروپونه چې یو شان یا بېل وي، ایترونه متناظر یا نامتناظر بلل کېږي. نامتناظرو ایترونو ته ګډ ایترونه هم وايي. ډای ایتیل ایتر متناظر ایتر دی؛ ایتیل میتایل ایتر نامتناظر ایتر (R – O – R′) دی. د ایترونو بېلګې دا دي:')
visual('chem12-p112-ether-examples',ethers)
add('18.3.1 Nomenclature','18.3.1 نام گذاری','18.3.1 نومول','heading')
add('a. Common System','a. عام نظام','a. عام سیستم','heading')
add('The two alkyl or aryl groups that are attached to the oxygen atom are named in alphabetical order and the word ether is added. When both alkyl groups are the same, the prefix di- precedes the name of the alkyl group.','آکسیجن ایٹم سے جڑے دونوں الکائل یا ایرائل گروپوں کے نام حروفِ تہجی کی ترتیب سے لیے جاتے ہیں اور لفظ ایتھر لگایا جاتا ہے۔ جب دونوں الکائل گروپ یکساں ہوں تو الکائل گروپ کے نام سے پہلے سابقہ di- لگتا ہے۔','له اکسیجني اټوم سره تړلي دوه الکایل یا اریل ګروپونه د الفبا په ترتیب نومول کېږي او د ایتر کلمه ورزیاتېږي. کله چې دواړه الکایل ګروپونه یو شان وي، د الکایل ګروپ له نوم مخکې di- مختاړی راځي.')
add('Examples','مثالیں','بېلګې','heading')
visual('chem12-p112-common-ethers',common)
add('b. IUPAC System','b. IUPAC نظام','b. IUPAC سیستم','heading')
add('Ethers are named in IUPAC nomenclature, as alkoxy derivatives of alkanes. The larger alkyl group is taken for parent name and the smaller alkyl group along with oxygen atom is named as alkoxy before the parent name.','IUPAC نام گذاری میں ایتھرز کے نام الکینز (اکیلے بند والے) کے الکوآکسی مشتقات کے طور پر رکھے جاتے ہیں۔ بڑے الکائل گروپ کو بنیادی نام کے لیے لیا جاتا ہے اور چھوٹے الکائل گروپ کا آکسیجن ایٹم سمیت نام بنیادی نام سے پہلے الکوآکسی کے طور پر رکھا جاتا ہے۔','په IUPAC نومولو کې ایترونه د الکانونو د الکوکسي مشتقاتو په توګه نومول کېږي. لوی الکایل ګروپ د اصلي نوم لپاره نیول کېږي او کوچنی الکایل ګروپ له اکسیجني اټوم سره له اصلي نوم مخکې د الکوکسي په توګه نومول کېږي.')
add('Examples','مثالیں','بېلګې','heading')
visual('chem12-p112-iupac-ethers',iupac)
add('18.3.2 Physical Properties','18.3.2 طبعی خصوصیات','18.3.2 فزیکي ځانګړنې','heading')
for e,u,p in [('Dimethyl ether and ethyl methyl ether are gases at RTP, while others are colourless volatile liquids with pleasant odours.','ڈائی میتھائل ایتھر اور ایتھائل میتھائل ایتھر RTP پر گیسیں ہیں، جبکہ دوسرے خوشگوار بو والے بے رنگ اڑنے والے مائع ہیں۔','ډای میتایل ایتر او ایتیل میتایل ایتر په RTP کې ګازونه دي، خو نور د خوندور بوی لرونکي بې رنګه الوتونکي مایعات دي.'),
 ('Ethers are highly inflammable.','ایتھرز انتہائی آتش گیر ہیں۔','ایترونه ډېر اور اخیستونکي دي.'),
 ('They have much lower boiling points than those of alcohols of comparable molecular weights due to absence of hydrogen bonding (Figure 18.3).','ہائیڈروجن بندش نہ ہونے کی وجہ سے ان کے نقطۂ جوش ملتے جلتے سالماتی وزن کے الکوحلز سے بہت کم ہیں (شکل 18.3)۔','د هایدروجني تړون د نشتوالي له امله د ورته مالیکولي وزن لرونکو الکولونو په پرتله ډېر ټیټ د ایشېدو ټکي لري (شکل 18.3).'),
 ('Low molecular weight ethers show some solubility in water as they can form hydrogen bonding with water (Figure 18.3). Ethers are readily soluble in organic solvents.','کم سالماتی وزن والے ایتھرز پانی میں کچھ حل پذیری ظاہر کرتے ہیں کیونکہ یہ پانی سے ہائیڈروجن بندش بنا سکتے ہیں (شکل 18.3)۔ ایتھرز نامیاتی محللات میں آسانی سے حل ہوتے ہیں۔','ټیټ مالیکولي وزن لرونکي ایترونه په اوبو کې یو څه حلېدنه ښيي ځکه له اوبو سره هایدروجني تړون جوړولی شي (شکل 18.3). ایترونه په عضوي محللونو کې په اسانۍ حلېږي.'),
 ('Ethers are generally less dense than water.','ایتھرز عموماً پانی سے کم کثیف ہیں۔','ایترونه عموماً له اوبو لږ کثیف دي.'),
 ('They are readily soluble in organic solvents.','یہ نامیاتی محللات میں آسانی سے حل ہوتے ہیں۔','په عضوي محللونو کې په اسانۍ حلېږي.')]:
 add(e,u,p,'list')
visual('chem12-figure18-3',hbond)
add('Figure 18.3 Hydrogen bonding in alcohol molecules, and between water and ether.','شکل 18.3 الکوحل سالمات میں اور پانی اور ایتھر کے درمیان ہائیڈروجن بندش۔','شکل 18.3 د الکول په مالیکولونو کې او د اوبو او ایتر ترمنځ هایدروجني تړون.')
record=section('18.13','Alcohols vs phenols (examples), ethers, nomenclature and physical properties','الکوحلز بمقابلہ فینولز (مثالیں)، ایتھرز، نام گذاری اور طبعی خصوصیات','الکولونه او فینولونه (بېلګې)، ایترونه، نومول او فزیکي ځانګړنې',paras,layout,blocks,'216–217')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':112,'printedPages':[216,217]}]
record['sourceContinuesOnPdfPage']=113
trim=[{'id':'18.14','startsAt':'18.3.3 Preparation'}]
if __name__=='__main__':save(112,[record],trim=trim,chapter_number=18)
