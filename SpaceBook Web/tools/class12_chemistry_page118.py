"""PDF118 printed228–229: IUPAC aldehyde examples, nomenclature of ketones, isomerism in aldehydes and ketones."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain,carbonyl
import math
F=Fig('arrow118');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'butanal':('بیوٹانل','بیوټانال'),'2-methylpropanal':('2-میتھائل پروپانل','2-میتایل پروپانال'),'4-chloro-3-methylpentanal':('4-کلورو-3-میتھائل پینٹانل','4-کلورو-3-میتایل پېنټانال'),'3-methylpent-3-enal':('3-میتھائل پینٹ-3-اینل','3-میتایل پېنټ-3-ینال'),
   'ethanedial':('ایتھین ڈائی ال','ایتان ډای ال'),'propanedial':('پروپین ڈائی ال','پروپان ډای ال'),'cyclopentanecarbaldehyde':('سائیکلوپینٹین کاربالڈیہائیڈ','سایکلوپېنټان کاربالدیهاید'),
   'dimethyl ketone':('ڈائی میتھائل کیٹون','ډای میتایل کیټون'),'(acetone)':('(ایسیٹون)','(اسیتون)'),'ethyl methyl ketone':('ایتھائل میتھائل کیٹون','ایتیل میتایل کیټون'),'diethyl ketone':('ڈائی ایتھائل کیٹون','ډای ایتیل کیټون'),
   'propanone':('پروپانون','پروپانون'),'butanone':('بیوٹانون','بیوټانون'),'pentan-2-one':('پینٹین-2-اون','پېنټان-2-ون'),'3-methylbutan-2-one':('3-میتھائل بیوٹین-2-اون','3-میتایل بیوټان-2-ون'),
   '1-bromobutan-2-one':('1-برومو بیوٹین-2-اون','1-برومو بیوټان-2-ون'),'hexane-2,4-dione':('ہیکسین-2،4-ڈائی اون','هېکسان-2،4-ډای ون'),'cyclohexanone':('سائیکلوہیکسانون','سایکلوهېکسانون'),
   'phenylethanone':('فینائل ایتھانون','فینیل ایتانون'),'(acetophenone)':('(ایسیٹو فینون)','(اسیټوفینون)'),'benzene-1,2-dicarbaldehyde':('بینزین-1،2-ڈائی کاربالڈیہائیڈ','بنزین-1،2-ډای کاربالدیهاید'),
   'benzene-1,3-dicarbaldehyde':('بینزین-1،3-ڈائی کاربالڈیہائیڈ','بنزین-1،3-ډای کاربالدیهاید'),'benzene-1,4-dicarbaldehyde':('بینزین-1،4-ڈائی کاربالڈیہائیڈ','بنزین-1،4-ډای کاربالدیهاید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def ald(lang):
 s=F.start(330)
 s+=chain(F,0,60,['CH₃','—','CH₂','—','CH₂','—','C','—','H'],15,None,{6:'=O'},center=220)+t(220,84,lb(lang,'butanal'),12)
 s+=chain(F,0,60,['CH₃','—','CH','—','C','—','H'],15,{0:'3',2:'2',4:'1'},{2:'CH₃',4:'=O'},center=620)+t(620,84,lb(lang,'2-methylpropanal'),12)
 s+=chain(F,0,170,['CH₃','—','CH','—','CH','—','CH₂','—','C','—','H'],15,None,{2:'Cl',4:'CH₃',8:'=O'},center=220)+t(220,194,lb(lang,'4-chloro-3-methylpentanal'),12)
 s+=chain(F,0,170,['CH₃','—','CH','=','C','—','CH₂','—','C','—','H'],15,None,{4:'CH₃',8:'=O'},center=620)+t(620,194,lb(lang,'3-methylpent-3-enal'),12)
 s+=chain(F,0,280,['H','—','C','—','C','—','H'],15,None,{2:'=O',4:'=O'},center=140)+t(140,304,lb(lang,'ethanedial'),12)
 s+=chain(F,0,280,['H','—','C','—','CH₂','—','C','—','H'],15,None,{2:'=O',6:'=O'},center=400)+t(400,304,lb(lang,'propanedial'),12)
 pts=[(640+28*math.cos(math.radians(-90+72*i)),280+28*math.sin(math.radians(-90+72*i))) for i in range(5)]
 s+='<polygon points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in pts)+'" fill="none" stroke="#222" stroke-width="2"/>'+line(pts[1][0],pts[1][1],pts[1][0]+24,pts[1][1]-10)+t(pts[1][0]+48,pts[1][1]-4,'C—H',15)+line(pts[1][0]+33,pts[1][1]-20,pts[1][0]+33,pts[1][1]-36)+line(pts[1][0]+39,pts[1][1]-20,pts[1][0]+39,pts[1][1]-36)+t(pts[1][0]+36,pts[1][1]-42,'O',14)
 s+=t(660,322,lb(lang,'cyclopentanecarbaldehyde'),12)
 return s+'</svg>'
def kcommon(lang):
 s=F.start(110)+C(150,60,'CH₃','CH₃')+t(150,84,lb(lang,'dimethyl ketone'),12)+t(150,100,lb(lang,'(acetone)'),12)+C(420,60,'CH₃—CH₂','CH₃')+t(420,84,lb(lang,'ethyl methyl ketone'),12)+C(690,60,'CH₃—CH₂','CH₂—CH₃')+t(690,84,lb(lang,'diethyl ketone'),12)
 return s+'</svg>'
def kiupac(lang):
 s=F.start(400)
 s+=C(110,60,'CH₃','CH₃')+t(110,84,lb(lang,'propanone'),12)+C(320,60,'CH₃—CH₂','CH₃')+t(320,84,lb(lang,'butanone'),12)
 s+=chain(F,0,60,['CH₃','—','C','—','CH₂','—','CH₂','—','CH₃'],14,{0:'1',4:'3',6:'4',8:'5'},{2:'=O'},center=640)+t(640,84,lb(lang,'pentan-2-one'),12)
 s+=chain(F,0,170,['CH₃','—','C','—','CH','—','CH₃'],14,{0:'1',6:'4'},{2:'=O',4:'CH₃'},center=200)+t(200,194,lb(lang,'3-methylbutan-2-one'),12)
 s+=chain(F,0,170,['CH₃','—','CH₂','—','C','—','CH₂','—','Br'],15,{0:'4',2:'3',6:'1'},{4:'=O'},center=600)+t(600,194,lb(lang,'1-bromobutan-2-one'),12)
 s+=chain(F,0,290,['CH₃','—','C','—','CH₂','—','C','—','CH₂','—','CH₃'],14,{0:'1',4:'3',8:'5',10:'6'},{2:'=O',6:'=O'},center=230)+t(230,314,lb(lang,'hexane-2,4-dione'),12)
 s+=F.ring(520,320,30,kek=False)+line(517,290,517,274)+line(523,290,523,274)+t(520,268,'O',14)+t(520,368,lb(lang,'cyclohexanone'),12)
 s+=F.ring(700,325,28)+line(724,311,744,301)+t(750,295,'C',15)+line(747,287,747,271)+line(753,287,753,271)+t(750,265,'O',14)+line(760,299,780,307)+t(800,313,'CH₃',14)+t(720,368,lb(lang,'phenylethanone'),12)+t(720,384,lb(lang,'(acetophenone)'),12)
 return s+'</svg>'
def dicarb(lang):
 s=F.start(190)
 for x,(v,n) in zip((180,425,670),((1,'benzene-1,2-dicarbaldehyde'),(2,'benzene-1,3-dicarbaldehyde'),(3,'benzene-1,4-dicarbaldehyde'))):
  s+=F.ring(x,80,28,subs={0:'CHO',v:'CHO'});
  for i in range(v+1):a=math.radians(60*i);s+=t(x+18*math.sin(a),80-18*math.cos(a)+4,str(i+1),10,'#555')
  s+=t(x,170 if v==3 else 150,lb(lang,n),12)
 return s+'</svg>'

add('Examples (continued)','مثالیں (جاری)','بېلګې (دوام)','heading')
visual('chem12-p118-iupac-aldehydes',ald)
add('19.1.2 Nomenclature of Ketones','19.1.2 کیٹونز کی نام گذاری','19.1.2 د کیټونونو نومول','heading')
add('a. Common System','a. عام نظام','a. عام سیستم','heading')
add('In this system ketones are named by writing first the name of the alkyl groups attached to the carbonyl carbon followed by the word “ketone”. For similar alkyl or aryl groups prefix “di” is used before their name. In case of different groups attached to the carbonyl carbon, alphabetical order is followed for writing their names.','اس نظام میں کیٹونز کے نام پہلے کاربونل کاربن سے جڑے الکائل گروپوں کے نام اور پھر لفظ ”کیٹون“ لکھ کر رکھے جاتے ہیں۔ یکساں الکائل یا ایرائل گروپوں کے لیے ان کے نام سے پہلے سابقہ ”di“ استعمال ہوتا ہے۔ کاربونل کاربن سے مختلف گروپ جڑے ہونے کی صورت میں ان کے نام حروفِ تہجی کی ترتیب سے لکھے جاتے ہیں۔','په دې سیستم کې کیټونونه په دې ډول نومول کېږي چې لومړی له کاربونیل کاربن سره د تړلو الکایل ګروپونو نوم او ورپسې د ”کیټون“ کلمه لیکل کېږي. د ورته الکایل یا اریل ګروپونو لپاره له نوم مخکې ”di“ مختاړی کارېږي. که له کاربونیل کاربن سره بېل ګروپونه تړلي وي، نومونه یې د الفبا په ترتیب لیکل کېږي.')
visual('chem12-p118-common-ketones',kcommon)
add('b. IUPAC System','b. IUPAC نظام','b. IUPAC سیستم','heading')
add('While naming ketones in IUPAC system the following rules are followed;','IUPAC نظام میں کیٹونز کے نام رکھتے وقت درج ذیل اصول اپنائے جاتے ہیں؛','په IUPAC سیستم کې د کیټونونو د نومولو پر مهال لاندې قواعد تعقیبېږي؛')
rules=[('1. Select the longest chain for stem name of ketone, which is then named by replacing the ending “–e” of corresponding alkane by “–one”.','1. کیٹون کے بنیادی نام کے لیے سب سے لمبی زنجیر منتخب کریں، جس کا نام متعلقہ الکین (اکیلے بند والے) کے اختتامیہ ”–e“ کو ”–one“ سے بدل کر رکھا جاتا ہے۔','1. د کیټون د اصلي نوم لپاره تر ټولو اوږد ځنځیر وټاکئ، چې بیا د اړوند الکان پای ”–e“ په ”–one“ بدلولو نومول کېږي.'),
 ('2. Prefix di–, tri– etc. is added before suffix –one, if more than one carbonyl groups are present.','2. اگر ایک سے زیادہ کاربونل گروپ ہوں تو لاحقہ –one سے پہلے سابقے di–، tri– وغیرہ لگائے جاتے ہیں۔','2. که له یوه ډېر کاربونیل ګروپونه وي، له –one وروستاړي مخکې di–، tri– او نور مختاړي ورزیاتېږي.'),
 ('3. The carbons of the selected chain are numbered to mention the position of the carbonyl carbon before suffix –one because in ketones carbonyl group may occur at various positions on the carbon chain.','3. منتخب زنجیر کے کاربنوں کو نمبر دیا جاتا ہے تاکہ لاحقہ –one سے پہلے کاربونل کاربن کا مقام بتایا جا سکے، کیونکہ کیٹونز میں کاربونل گروپ کاربن زنجیر پر مختلف مقامات پر ہو سکتا ہے۔','3. د ټاکل شوي ځنځیر کاربنونه شمېرل کېږي څو له –one وروستاړي مخکې د کاربونیل کاربن موقعیت وښودل شي، ځکه په کیټونونو کې کاربونیل ګروپ پر کاربني ځنځیر بېلابېلو ځایونو کې کېدای شي.'),
 ('4. Numbering is done from that end at which the carbonyl carbon has the lowest possible number. No numbering is necessary for propanone and butanone.','4. نمبر اس سرے سے دیا جاتا ہے جہاں سے کاربونل کاربن کو کم سے کم ممکنہ نمبر ملے۔ پروپانون اور بیوٹانون کے لیے نمبر دینا ضروری نہیں۔','4. شمېرنه له هغه پای کېږي چې کاربونیل کاربن تر ټولو ټیټه ممکنه شمېره ولري. د پروپانون او بیوټانون لپاره شمېرنه اړینه نه ده.'),
 ('5. If substituents are attached to the selected chain then the same rules are obeyed as mentioned for IUPAC names of alkanes.','5. اگر منتخب زنجیر سے متبادلات جڑے ہوں تو وہی اصول اپنائے جاتے ہیں جو الکینز (اکیلے بند والے) کے IUPAC ناموں کے لیے بیان ہوئے۔','5. که له ټاکل شوي ځنځیر سره بدیلونه تړلي وي، د الکانونو د IUPAC نومونو لپاره یاد شوي ورته قواعد تعقیبېږي.')]
s0=len(paras)
for r in rules:paras.append(pair(*r))
layout.append({'type':'lines','indices':list(range(s0,len(paras)))})
visual('chem12-p118-iupac-ketones',kiupac)
add('Isomerism in Aldehydes and Ketones','الڈیہائیڈز اور کیٹونز میں آئسومرزم','په الدیهایډونو او کیټونونو کې ایزومېریزم','heading')
add('Aldehydes containing four or more carbon atoms and ketones containing five or more carbon atoms can exhibit chain isomerism. For example, butanal and 2-methylpropanal are chain isomers of aldehydes containing four carbon atoms, while pentan-2-one and 3-methylbutanone are chain isomers of ketone containing five carbon atoms.','چار یا زیادہ کاربن ایٹموں والے الڈیہائیڈز اور پانچ یا زیادہ کاربن ایٹموں والے کیٹونز زنجیری آئسومرزم ظاہر کر سکتے ہیں۔ مثلاً بیوٹانل اور 2-میتھائل پروپانل چار کاربن ایٹموں والے الڈیہائیڈز کے زنجیری آئسومر ہیں، جبکہ پینٹین-2-اون اور 3-میتھائل بیوٹانون پانچ کاربن ایٹموں والے کیٹون کے زنجیری آئسومر ہیں۔','څلور یا ډېر کاربني اټومونه لرونکي الدیهایډونه او پنځه یا ډېر کاربني اټومونه لرونکي کیټونونه ځنځیري ایزومېریزم ښودلی شي. د بېلګې په توګه بیوټانال او 2-میتایل پروپانال د څلور کاربني اټومونو لرونکو الدیهایډونو ځنځیري ایزومرونه دي، په داسې حال کې چې پېنټان-2-ون او 3-میتایل بیوټانون د پنځه کاربني اټومونو لرونکي کیټون ځنځیري ایزومرونه دي.')
add('Ketones having five or more carbon atoms and aromatic aldehydes can exhibit position isomerism. For example, pentan-2-one and pentan-3-one are position isomers of ketone having five carbon atoms. Aromatic aldehydes can also show position isomerism e.g. benzene-1,2-dicarbaldehyde, benzene-1,3-dicarbaldehyde and benzene-1,4-dicarbaldehyde are position isomers.','پانچ یا زیادہ کاربن ایٹموں والے کیٹونز اور ارومیٹک الڈیہائیڈز مقامی آئسومرزم ظاہر کر سکتے ہیں۔ مثلاً پینٹین-2-اون اور پینٹین-3-اون پانچ کاربن ایٹموں والے کیٹون کے مقامی آئسومر ہیں۔ ارومیٹک الڈیہائیڈز بھی مقامی آئسومرزم ظاہر کر سکتے ہیں، مثلاً بینزین-1،2-ڈائی کاربالڈیہائیڈ، بینزین-1،3-ڈائی کاربالڈیہائیڈ اور بینزین-1،4-ڈائی کاربالڈیہائیڈ مقامی آئسومر ہیں۔','پنځه یا ډېر کاربني اټومونه لرونکي کیټونونه او اروماتیک الدیهایډونه موقعیتي ایزومېریزم ښودلی شي. د بېلګې په توګه پېنټان-2-ون او پېنټان-3-ون د پنځه کاربني اټومونو لرونکي کیټون موقعیتي ایزومرونه دي. اروماتیک الدیهایډونه هم موقعیتي ایزومېریزم ښودلی شي، لکه بنزین-1،2-ډای کاربالدیهاید، بنزین-1،3-ډای کاربالدیهاید او بنزین-1،4-ډای کاربالدیهاید موقعیتي ایزومرونه دي.')
visual('chem12-p118-dicarbaldehydes',dicarb)
add('Aldehydes and ketones have the same general formula, CₙH₂ₙO and can exhibit functional group isomerism e.g. propanal and propanone are functional groups isomers. Aldehydes and ketones also show tautomerism (Section 16.6.1).','الڈیہائیڈز اور کیٹونز کا عمومی فارمولا CₙH₂ₙO یکساں ہے اور یہ فعلی گروپ آئسومرزم ظاہر کر سکتے ہیں، مثلاً پروپانل اور پروپانون فعلی گروپ آئسومر ہیں۔ الڈیہائیڈز اور کیٹونز ٹاٹومرزم بھی ظاہر کرتے ہیں (حصہ 16.6.1)۔','الدیهایډونه او کیټونونه ورته عمومي فورمول CₙH₂ₙO لري او د فعال ګروپ ایزومېریزم ښودلی شي، لکه پروپانال او پروپانون د فعال ګروپ ایزومرونه دي. الدیهایډونه او کیټونونه ټاټومېریزم هم ښيي (برخه 16.6.1).')
record=section('19.2','IUPAC aldehyde examples, ketone nomenclature and isomerism','IUPAC الڈیہائیڈ مثالیں، کیٹونز کی نام گذاری اور آئسومرزم','د IUPAC الدیهاید بېلګې، د کیټونونو نومول او ایزومېریزم',paras,layout,blocks,'228–229')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':118,'printedPages':[228,229]}]
record['sourceContinuesOnPdfPage']=119
carry=[{'from':'19.2','to':'19.3','startsAt':'229\n19.2\nStructure'}]
if __name__=='__main__':save(118,[record],carry=carry,chapter_number=19)
