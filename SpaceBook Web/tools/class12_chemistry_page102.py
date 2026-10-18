"""PDF102 printed196–197: nomenclature of alcohols (common and IUPAC), physical properties (start)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow102');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'methyl alcohol':('میتھائل الکوحل','میتایل الکول'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'n-propyl alcohol':('n-پروپائل الکوحل','n-پروپیل الکول'),'isopropyl alcohol':('آئسوپروپائل الکوحل','ایزوپروپیل الکول'),
   'n-butyl alcohol':('n-بیوٹائل الکوحل','n-بیوټیل الکول'),'sec-butyl alcohol':('سیکنڈری بیوٹائل الکوحل','سېکنډري بیوټیل الکول'),'tert-butyl alcohol':('ٹرشری بیوٹائل الکوحل','ټرشري بیوټیل الکول'),'isobutyl alcohol':('آئسوبیوٹائل الکوحل','ایزوبیوټیل الکول'),
   'ethylene glycol':('ایتھیلین گلائیکول','ایتیلین ګلایکول'),'propylene glycol':('پروپیلین گلائیکول','پروپیلین ګلایکول'),'trimethylene glycol':('ٹرائی میتھیلین گلائیکول','ټرای میتیلین ګلایکول'),'glycerol':('گلیسرول','ګلیسرول'),
   'methanol':('میتھانول','میتانول'),'ethanol':('ایتھانول','ایتانول'),'propan-1-ol':('پروپین-1-اول','پروپان-1-ول'),'propan-2-ol':('پروپین-2-اول','پروپان-2-ول'),'butan-2-ol':('بیوٹین-2-اول','بیوټان-2-ول'),
   '2,2,4-trimethylpentan-3-ol':('2،2،4-ٹرائی میتھائل پینٹین-3-اول','2،2،4-ټرای میتایل پېنټان-3-ول'),'ethane-1,2-diol':('ایتھین-1،2-ڈائی اول','ایتان-1،2-ډای ول'),'propane-1,2,3-triol':('پروپین-1،2،3-ٹرائی اول','پروپان-1،2،3-ټرای ول')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def C(x,y,toks,num=None,up=None,down=None,name=None,lang='en',size=15,dy=None):
 s=chain(F,0,y,toks,size,num,up,down,center=x)
 if name:s+=t(x,y+(dy if dy else (52 if down else 24)),lb(lang,name),12)
 return s
def common(lang):
 s=F.start(420)
 s+=C(200,40,['CH₃','–','OH'],name='methyl alcohol',lang=lang)+C(600,40,['CH₃','–','CH₂','–','OH'],name='ethyl alcohol',lang=lang)
 s+=C(200,140,['CH₃','–','CH₂','–','CH₂','–','OH'],name='n-propyl alcohol',lang=lang)+C(600,140,['CH₃','—','CH','—','OH'],up={2:'CH₃'},name='isopropyl alcohol',lang=lang)
 s+=C(200,240,['CH₃','–','CH₂','–','CH₂','–','CH₂','–','OH'],name='n-butyl alcohol',lang=lang)+C(600,240,['CH₃','—','CH₂','—','CH','—','CH₃'],up={4:'OH'},name='sec-butyl alcohol',lang=lang)
 s+=C(200,345,['CH₃','—','C','—','OH'],up={2:'CH₃'},down={2:'CH₃'},name='tert-butyl alcohol',lang=lang)+C(600,345,['CH₃','—','CH','—','CH₂','—','OH'],down={2:'CH₃'},name='isobutyl alcohol',lang=lang)
 return s+'</svg>'
def glycols(lang):
 s=F.start(110)
 s+=C(150,60,['CH₂','—','CH₂'],up={0:'OH',2:'OH'},name='ethylene glycol',lang=lang)+C(420,60,['CH₂','—','CH','—','CH₃'],up={0:'OH',2:'OH'},name='propylene glycol',lang=lang)
 s+=C(690,60,['CH₂','—','CH₂','—','CH₂'],up={0:'OH',4:'OH'},name='trimethylene glycol',lang=lang)
 return s+'</svg>'
def glycerol(lang):return F.start(110)+C(425,70,['CH₂','—','CH','—','CH₂'],up={0:'OH',2:'OH',4:'OH'},name='glycerol',lang=lang)+'</svg>'
def iupac(lang):
 s=F.start(400)
 s+=C(220,40,['CH₃','—','OH'],name='methanol',lang=lang)+C(620,40,['CH₃','—','CH₂','—','OH'],name='ethanol',lang=lang)
 s+=C(220,130,['CH₃','—','CH₂','—','CH₂','—','OH'],{0:'3',2:'2',4:'1'},name='propan-1-ol',lang=lang)+C(620,130,['CH₃','—','CH','—','CH₃'],{0:'3',4:'1'},{2:'OH'},name='propan-2-ol',lang=lang)
 s+=C(220,225,['CH₃','—','CH','—','CH₂','—','CH₃'],{0:'1',4:'3',6:'4'},None,{2:'OH'},name='butan-2-ol',lang=lang,dy=64)+C(620,225,['CH₃','—','C','—','CH','—','C','—','CH₃'],{0:'1',8:'5'},{2:'CH₃',4:'OH',6:'CH₃'},{2:'CH₃',6:'H'},name='2,2,4-trimethylpentan-3-ol',lang=lang,dy=60)
 s+=t(220,320,'¹CH₂—OH',15)+line(200,328,200,344)+t(220,362,'²CH₂—OH',15)+t(220,386,lb(lang,'ethane-1,2-diol'),12)
 s+=C(620,320,['CH₂','—','CH₂','—','CH₂'],{0:'1',2:'2',4:'3'},None,{0:'OH',2:'OH',4:'OH'},name='propane-1,2,3-triol',lang=lang,dy=62)
 return s.replace('viewBox="0 0 850 400"','viewBox="0 0 850 410"')+'</svg>'

add('a. Common System','a. عام نظام','a. عام سیستم','heading')
add('In this system, monohydric alcohols are named as “alkyl alcohols”. That is alkyl group of the alcohol is named first, which is followed by the word alcohol. For example,','اس نظام میں مونو ہائیڈرک الکوحلز کے نام ”الکائل الکوحلز“ کے طور پر رکھے جاتے ہیں۔ یعنی الکوحل کے الکائل گروپ کا نام پہلے لیا جاتا ہے، جس کے بعد لفظ الکوحل آتا ہے۔ مثلاً،','په دې سیستم کې مونوهایدریک الکولونه د ”الکایل الکولونو“ په توګه نومول کېږي. یعنې د الکول الکایل ګروپ لومړی نومول کېږي او ورپسې د الکول کلمه راځي. د بېلګې په توګه،')
visual('chem12-p102-common-alcohols',common)
add('The n-propyl alcohol and isopropyl alcohol are isomers. The four isomeric butyl alcohols are names as follows.','n-پروپائل الکوحل اور آئسوپروپائل الکوحل آئسومر ہیں۔ چار ہم ترکیب بیوٹائل الکوحلز کے نام درج ذیل ہیں۔','n-پروپیل الکول او ایزوپروپیل الکول ایزومرونه دي. څلور ایزومري بیوټیل الکولونه داسې نومول کېږي.')
add('Suffix glycols is used for dihydric alcohols (more commonly for vicinal diols).','ڈائی ہائیڈرک الکوحلز (زیادہ تر وسینل ڈائی اولز) کے لیے لاحقہ گلائیکولز استعمال ہوتا ہے۔','د ډای هایدریک الکولونو (ډېری وېسینل ډای اولونو) لپاره د ګلایکولونو وروستاړی کارېږي.')
visual('chem12-p102-glycols',glycols)
add('The smallest trihydric alcohol is named as glycerol.','سب سے چھوٹے ٹرائی ہائیڈرک الکوحل کا نام گلیسرول ہے۔','تر ټولو کوچنی ټرای هایدریک الکول ګلیسرول نومول شوی.')
visual('chem12-p102-glycerol',glycerol)
add('b. IUPAC System','b. IUPAC نظام','b. IUPAC سیستم','heading')
add('In this system alcohols are named as “alkanols”. That is, the final ‘–e’ of the corresponding alkane is replaced by suffix ‘–ol’.','اس نظام میں الکوحلز کے نام ”الکینولز“ کے طور پر رکھے جاتے ہیں۔ یعنی متعلقہ الکین (اکیلے بند والے) کا آخری ’–e‘ لاحقے ’–ol‘ سے بدل دیا جاتا ہے۔','په دې سیستم کې الکولونه د ”الکانولونو“ په توګه نومول کېږي. یعنې د اړوند الکان وروستی ’–e‘ په ’–ol‘ وروستاړي بدلېږي.')
add('The IUPAC rules are','IUPAC اصول یہ ہیں','د IUPAC قواعد دا دي','heading')
rules=[('1. Select the longest continuous carbon chain containing the –OH group(s).','1. وہ سب سے لمبی مسلسل کاربن زنجیر منتخب کریں جس میں –OH گروپ ہوں۔','1. هغه تر ټولو اوږد پرله پسې کاربني ځنځیر وټاکئ چې –OH ګروپ(ونه) ولري.'),
 ('2. The ending “–e” of the corresponding alkane is replaced by suffix “–ol”.','2. متعلقہ الکین (اکیلے بند والے) کا اختتامیہ ”–e“ لاحقے ”–ol“ سے بدل دیا جاتا ہے۔','2. د اړوند الکان پای ”–e“ په ”–ol“ وروستاړي بدلېږي.'),
 ('3. Number the chain from one end or the other, so as to give lowest number to the carbon carrying the –OH group.','3. زنجیر کو کسی ایک سرے سے اس طرح نمبر دیں کہ –OH گروپ والے کاربن کو سب سے کم نمبر ملے۔','3. ځنځیر له یوه یا بل پای داسې شمېره کړئ چې –OH ګروپ لرونکي کاربن ته تر ټولو ټیټه شمېره ورکړل شي.'),
 ('4. Mention the position of the hydroxyl group by putting its number before the suffix “–ol”.','4. ہائیڈروآکسل گروپ کا مقام اس کا نمبر لاحقے ”–ol“ سے پہلے لکھ کر بتائیں۔','4. د هایدروکسیل ګروپ موقعیت د هغه شمېرې له ”–ol“ وروستاړي مخکې په لیکلو وښیئ.'),
 ('5. Indicate the position of the other substituents (if any) using the numbers of the carbon atoms, to which they are attached.','5. دوسرے متبادلات (اگر ہوں) کا مقام ان کاربن ایٹموں کے نمبروں سے ظاہر کریں جن سے وہ جڑے ہوں۔','5. د نورو بدیلونو (که وي) موقعیت د هغو کاربني اټومونو په شمېرو وښیئ چې ورسره تړلي دي.'),
 ('6. The substituents, along with their positions, are named in alphabetical order before the parent name.','6. متبادلات کے نام ان کے مقامات سمیت بنیادی نام سے پہلے حروفِ تہجی کی ترتیب سے رکھے جاتے ہیں۔','6. بدیلونه له خپلو موقعیتونو سره له اصلي نوم مخکې د الفبا په ترتیب نومول کېږي.'),
 ('7. If the number of carbon atoms carrying the hydroxyl group is the same from either side, then number the chain from the end which is heavily substituted.','7. اگر ہائیڈروآکسل گروپ والے کاربن ایٹم کا نمبر دونوں جانب سے یکساں ہو تو زنجیر کو اس سرے سے نمبر دیں جو زیادہ متبادل والا ہو۔','7. که د هایدروکسیل ګروپ لرونکي کاربني اټوم شمېره له دواړو خواوو یو شان وي، ځنځیر له هغه پای شمېره کړئ چې ډېر بدیلونه لري.'),
 ('8. In case of dihydric, trihydric and polyhydric alcohols, the prefix di, tri, tetra etc. is used before “–ol”, along with the numbers of the carbon atoms to which these hydroxyl groups are attached.','8. ڈائی ہائیڈرک، ٹرائی ہائیڈرک اور پولی ہائیڈرک الکوحلز کی صورت میں ”–ol“ سے پہلے سابقے di، tri، tetra وغیرہ ان کاربن ایٹموں کے نمبروں کے ساتھ استعمال ہوتے ہیں جن سے یہ ہائیڈروآکسل گروپ جڑے ہوں۔','8. د ډای هایدریک، ټرای هایدریک او پولي هایدریک الکولونو په حالت کې له ”–ol“ مخکې di، tri، tetra او نور مختاړي د هغو کاربني اټومونو له شمېرو سره کارېږي چې دا هایدروکسیل ګروپونه ورسره تړلي دي.'),
 ('9. If more than one hydroxyl groups are attached to the same carbon atom, the number of that carbon atom is repeated.','9. اگر ایک ہی کاربن ایٹم سے ایک سے زیادہ ہائیڈروآکسل گروپ جڑے ہوں تو اس کاربن ایٹم کا نمبر دہرایا جاتا ہے۔','9. که له یوه کاربني اټوم سره له یوه ډېر هایدروکسیل ګروپونه تړلي وي، د هغه کاربني اټوم شمېره تکرارېږي.')]
s0=len(paras)
for r in rules:paras.append(pair(*r))
layout.append({'type':'lines','indices':list(range(s0,len(paras)))})
add('The following examples will illustrate the above rules.','درج ذیل مثالیں اوپر کے اصولوں کی وضاحت کریں گی۔','لاندې بېلګې به پورته قواعد روښانه کړي.')
visual('chem12-p102-iupac-alcohols',iupac)
add('18.1.2 Physical Properties','18.1.2 طبعی خصوصیات','18.1.2 فزیکي ځانګړنې','heading')
add('Lower alcohols are colourless liquids while alcohols of high molecular mass are solids, at room temperature.','کمرے کے درجہ حرارت پر کم کاربن والے الکوحلز بے رنگ مائع جبکہ زیادہ سالماتی کمیت والے الکوحلز ٹھوس ہیں۔','د کوټې په تودوخه کې ټیټ الکولونه بې رنګه مایعات او د لوړې مالیکولي کتلې الکولونه جامد دي.','list')
add('They have characteristic sweet smell.','ان کی مخصوص میٹھی بو ہوتی ہے۔','ځانګړی خوږ بوی لري.','list')
add('The melting and boiling points are generally increase with the size of alkyl group, and also number of –OH groups (Table 18.1).','نقطۂ پگھلاؤ اور نقطۂ جوش عموماً الکائل گروپ کے حجم اور –OH گروپوں کی تعداد کے ساتھ بڑھتے ہیں (جدول 18.1)۔','د ویلې کېدو او ایشېدو ټکي عموماً د الکایل ګروپ له اندازې او د –OH ګروپونو له شمېر سره زیاتېږي (جدول 18.1).','list')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('The -e ending of an alkane name is dropped before a suffix beginning with a vowel (-ol) and retained before one beginning with a consonant (-diol).','الکین (اکیلے بند والے) کے نام کا آخری -e حرفِ علت سے شروع ہونے والے لاحقے (-ol) سے پہلے گرا دیا جاتا ہے اور حرفِ صحیح سے شروع ہونے والے لاحقے (-diol) سے پہلے برقرار رکھا جاتا ہے۔','د الکان د نوم پای -e د هغه وروستاړي مخکې چې په غږیز توری (-ol) پیلېږي غورځول کېږي، او د هغه مخکې چې په بې غږه توری (-diol) پیلېږي ساتل کېږي.')
record=section('18.2','Nomenclature of alcohols','الکوحلز کی نام گذاری','د الکولونو نومول',paras,layout,blocks,'196–197')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':102,'printedPages':[196,197]}]
record['sourceContinuesOnPdfPage']=103
issues=[{'id':'chem12-p197-triol-printing','printedPage':197,'description':'Propane-1,2,3-triol is printed as ¹CH₂—²CH₂—³CH₂ (middle carbon should be CH); retained as printed (zoom-confirmed). Printed "names as follows" retained.'}]
trim=[{'id':'18.3','startsAt':'(Table 18.1). Among isomeric'}]
if __name__=='__main__':save(102,[record],trim=trim,issues=issues,chapter_number=18)
