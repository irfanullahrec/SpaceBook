"""PDF113 printed218–219: preparation of ethers, chemical reactivity, oxonium salts, cleavage of ether linkage."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow113');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'alcohol':('الکوحل','الکول'),'ether':('ایتھر','ایتر'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'diethyl ether':('ڈائی ایتھائل ایتھر','ډای ایتیل ایتر'),'sodium alkoxide':('سوڈیم الکوآکسائیڈ','سوډیم الکوکساید'),
   'alkyl halide':('الکائل ہیلائیڈ','الکایل هالایډ'),'sodium ethoxide':('سوڈیم ایتھوآکسائیڈ','سوډیم ایتوکساید'),'methyl chloride':('میتھائل کلورائیڈ','میتایل کلوراید'),'ethyl methyl ether':('ایتھائل میتھائل ایتھر','ایتیل میتایل ایتر'),
   'dialkyloxonium hydrogensulphate':('ڈائی الکائل آکسونیم ہائیڈروجن سلفیٹ','ډای الکایل اکسونیم هایدروجن سلفېټ'),'dialkyloxonium chloride':('ڈائی الکائل آکسونیم کلورائیڈ','ډای الکایل اکسونیم کلوراید'),'oxonium ion':('آکسونیم آئن','اکسونیم ایون'),
   'diethyloxonium ion':('ڈائی ایتھائل آکسونیم آئن','ډای ایتیل اکسونیم ایون')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def eqs(lang,rows):
 s=F.start(70*len(rows)+10)
 for i,(l,ln,a,b,r,rn) in enumerate(rows):
  y=40+70*i;s+=t(200,y,l,16)+t(200,y+22,'      '.join(lb(lang,x) for x in ln),12)+F.arrow(340,450,y-6,a,b)+t(600,y,r,16)+t(600,y+22,lb(lang,rn),12)
 return s+'</svg>'
def oxon(lang):
 s=F.start(200)
 for i,(reag,an,name) in enumerate((('conc. H₂SO₄','HSO₄⁻','dialkyloxonium hydrogensulphate'),('conc. HCl','Cl⁻','dialkyloxonium chloride'))):
  y=55+95*i;s+=t(150,y,'R—O—R  +  '+reag,16)+t(110,y+22,lb(lang,'ether'),12)+F.arrow(320,420,y-6)
  s+='<path d="M470 %d L462 %d L462 %d L470 %d M590 %d L598 %d L598 %d L590 %d" fill="none" stroke="#222" stroke-width="2"/>'%(y-30,y-30,y+30,y+30,y-30,y-30,y+30,y+30)+t(530,y,'R—O⁺—R',16)+line(530,y+6,530,y+16)+t(530,y+30,'H',13)+t(625,y,an,15)+t(560,y+48,lb(lang,name),12)
 return s+'</svg>'
def cleave(lang):
 s=F.start(310)+t(80,60,"R—O—R′",16)+t(80,82,lb(lang,'ether'),12)+F.arrow(130,220,54,'H₂SO₄','−HSO₄⁻')+t(290,60,"R—O⁺—R′",16)+line(285,66,285,78)+t(285,92,'H',13)+t(290,110,lb(lang,'oxonium ion'),12)
 s+=F.arrow(350,430,54,'H₂O')+'<rect x="440" y="36" width="80" height="44" fill="none" stroke="#222"/>'+t(480,58,'R—OH',15)+t(480,74,lb(lang,'alcohol'),11)+t(600,60,"+  R′—O⁺H₂",16)
 s+=line(650,70,650,150)+F.line(650,150,560,150,2,'#222','marker-end="url(#arrow113)"')+t(675,140,'−H⁺',13)+'<rect x="470" y="128" width="80" height="44" fill="none" stroke="#222"/>'+t(510,150,"R′—OH",15)+t(510,166,lb(lang,'alcohol'),11)
 s+=t(90,250,'C₂H₅—O—C₂H₅',16)+t(90,272,lb(lang,'diethyl ether'),12)+F.arrow(170,260,244,'H₂SO₄','−HSO₄⁻')+t(350,250,'C₂H₅—O⁺—C₂H₅',16)+line(350,256,350,268)+t(350,282,'H',13)+t(350,300,lb(lang,'diethyloxonium ion'),12)
 s+=F.arrow(440,540,244,'H₂O','−H⁺')+t(630,250,'2C₂H₅—OH',16)+t(630,272,lb(lang,'ethyl alcohol'),12)
 return s+'</svg>'

add('18.3.3 Preparation','18.3.3 تیاری','18.3.3 چمتو کول','heading')
add('Ethers can be prepared by the following methods.','ایتھرز درج ذیل طریقوں سے تیار کیے جا سکتے ہیں۔','ایترونه په لاندې طریقو چمتو کېدای شي.')
add('1. Intermolecular dehydration of alcohols','1. الکوحلز کی بین السالماتی آب ربائی','1. د الکولونو بین المالیکولي اوبه ایستنه','heading')
add('Alcohols on intramolecular dehydration with concentrated sulphuric acid, give alkenes (Sections 16.5.4.1 and 18.1.7.3). However, intermolecular dehydration of alcohol with concentrated sulphuric acid at 140°C, yields ethers.','مرتکز سلفیورک ایسڈ سے الکوحلز کی اندرون سالماتی آب ربائی الکینز (دوہرے بند والے) دیتی ہے (حصے 16.5.4.1 اور 18.1.7.3)۔ تاہم 140°C پر مرتکز سلفیورک ایسڈ سے الکوحل کی بین السالماتی آب ربائی ایتھرز دیتی ہے۔','له غلیظ سلفوریک اسید سره د الکولونو داخل المالیکولي اوبه ایستنه الکینونه ورکوي (برخې 16.5.4.1 او 18.1.7.3). خو په 140°C کې له غلیظ سلفوریک اسید سره د الکول بین المالیکولي اوبه ایستنه ایترونه ورکوي.')
visual('chem12-p113-dehydration',lambda l:eqs(l,[('R—OH  +  HO—R',['alcohol','alcohol'],'H₂SO₄','140°C','R—O—R  +  H₂O','ether'),('CH₃—CH₂—OH + HO—CH₂—CH₃',['ethyl alcohol','ethyl alcohol'],'H₂SO₄','140°C','CH₃—CH₂—O—CH₂—CH₃ + H₂O','diethyl ether')]))
add('The reaction conditions must be well controlled otherwise at temperature higher than 140°C; the formation of alkenes is favoured. This method is useful for preparation of symmetric ethers because in an attempt to prepare an unsymmetrical ether, by mixing different alcohols, we usually obtain a mixture of ethers, which is too difficult to be separated.',
 'تعامل کی شرائط کو اچھی طرح قابو میں رکھنا ضروری ہے ورنہ 140°C سے زیادہ درجہ حرارت پر الکینز (دوہرے بند والے) بننے کو ترجیح ملتی ہے۔ یہ طریقہ متشاکل ایتھرز کی تیاری کے لیے مفید ہے کیونکہ مختلف الکوحلز ملا کر غیر متشاکل ایتھر تیار کرنے کی کوشش میں عموماً ایتھرز کا آمیزہ ملتا ہے، جسے الگ کرنا بہت مشکل ہے۔',
 'د تعامل شرایط باید ښه کنټرول شي، که نه له 140°C څخه په لوړه تودوخه کې د الکینونو جوړېدل غوره کېږي. دا طریقه د متناظرو ایترونو د جوړولو لپاره ګټوره ده ځکه د بېلابېلو الکولونو په ګډولو د نامتناظر ایتر د جوړولو په هڅه کې معمولاً د ایترونو ګډوله ترلاسه کوو، چې جلا کول یې ډېر ستونزمن دي.')
add('2. Williamson’s Synthesis','2. ولیمسن کی تالیف','2. د ویلیامسن ترکیب','heading')
add('In this method, an alkoxide is treated with an alkyl halide. The alkoxide is usually derived from alcohols.','اس طریقے میں الکوآکسائیڈ کو الکائل ہیلائیڈ سے عمل کرایا جاتا ہے۔ الکوآکسائیڈ عموماً الکوحلز سے حاصل کیا جاتا ہے۔','په دې طریقه کې الکوکساید له الکایل هالایډ سره تعامل ورکول کېږي. الکوکساید معمولاً له الکولونو ترلاسه کېږي.')
visual('chem12-p113-williamson',lambda l:eqs(l,[('R – OH  +  Na',['alcohol'],'','','R – O⁻Na⁺  +  ½H₂','sodium alkoxide'),('R – O⁻Na⁺  +  R – X',['sodium alkoxide','alkyl halide'],'','','R – O – R  +  NaX','ether')]))
add('For example ethyl methyl ether can be prepared as follows.','مثلاً ایتھائل میتھائل ایتھر درج ذیل طرح تیار کیا جا سکتا ہے۔','د بېلګې په توګه ایتیل میتایل ایتر په لاندې ډول جوړېدای شي.')
visual('chem12-p113-williamson-example',lambda l:eqs(l,[('C₂H₅–OH  +  Na',['ethyl alcohol'],'','','C₂H₅ – O⁻Na⁺  +  ½H₂','sodium ethoxide'),('C₂H₅ – O⁻Na⁺  +  CH₃ – Cl',['sodium ethoxide','methyl chloride'],'','','C₂H₅–O–CH₃  +  NaCl','ethyl methyl ether')]))
add('18.3.4 Chemical Reactivity','18.3.4 کیمیائی تعامل پذیری','18.3.4 کیمیاوي تعامل وړتیا','heading')
add('Ethers are quite stable compounds. They do not react with bases, active metals, oxidising and reducing agents. They are also stable to weak and dilute acids. However, they form oxonium salts with strong and concentrated acids. The oxonium salts are unstable and can easily be cleaved. Their resistance to most of the reagents form the basis of their use as solvent for many organic reactions. The most important reaction of ether is the formation of oxonium salt and cleavage of ether linkage.',
 'ایتھرز کافی پائیدار مرکبات ہیں۔ یہ اساسوں، فعال دھاتوں، تکسیدی اور تخفیفی عاملوں سے تعامل نہیں کرتے۔ یہ کمزور اور ہلکے تیزابوں کے لیے بھی پائیدار ہیں۔ تاہم طاقتور اور مرتکز تیزابوں سے یہ آکسونیم نمکیات بناتے ہیں۔ آکسونیم نمکیات ناپائیدار ہیں اور آسانی سے ٹوٹ سکتے ہیں۔ زیادہ تر عاملوں کے خلاف ان کی مزاحمت بہت سے نامیاتی تعاملات میں بطور محلل ان کے استعمال کی بنیاد ہے۔ ایتھر کا سب سے اہم تعامل آکسونیم نمک کی تشکیل اور ایتھر بندھن کی شکست ہے۔',
 'ایترونه کافي ثابت مرکبات دي. له قلویانو، فعالو فلزونو، اکسیډایز کوونکو او ارجاع کوونکو عاملونو سره تعامل نه کوي. د کمزورو او رقیقو اسیدونو په وړاندې هم ثابت دي. خو له قوي او غلیظو اسیدونو سره د اکسونیم مالګې جوړوي. د اکسونیم مالګې بې ثباته دي او په اسانۍ ماتېدای شي. د ډېرو عاملونو په وړاندې د دوی مقاومت د ډېرو عضوي تعاملونو لپاره د محلل په توګه د دوی د کارونې بنسټ دی. د ایتر تر ټولو مهم تعامل د اکسونیم مالګې جوړېدل او د ایتري تړون ماتېدل دي.')
add('1. Formation of Oxonium Salts','1. آکسونیم نمکیات کی تشکیل','1. د اکسونیم مالګو جوړېدل','heading')
add('Ethers react with cold concentrated hydrochloric acid and sulphuric acid to form oxonium salts. Ethers donate a pair of electrons to hydrogen ion to form these salts.','ایتھرز ٹھنڈے مرتکز ہائیڈروکلورک ایسڈ اور سلفیورک ایسڈ سے تعامل کر کے آکسونیم نمکیات بناتے ہیں۔ ایتھرز یہ نمکیات بنانے کے لیے ہائیڈروجن آئن کو الیکٹرانوں کا ایک جوڑا دیتے ہیں۔','ایترونه له سړه غلیظ هایدروکلوریک اسید او سلفوریک اسید سره تعامل کوي او د اکسونیم مالګې جوړوي. ایترونه د دې مالګو د جوړولو لپاره هایدروجن ایون ته د الکترونونو یوه جوړه ورکوي.')
visual('chem12-p113-oxonium',oxon)
add('2. Cleavage of ether linkage','2. ایتھر بندھن کی شکست','2. د ایتري تړون ماتېدل','heading')
add('On prolong heating with dilute sulphuric acid, ethers undergo hydrolysis to original alcohols. The oxonium salt formed upon protonation, is further cleaved by attack of water nucleophile to form alcohols.','ہلکے سلفیورک ایسڈ کے ساتھ دیر تک گرم کرنے پر ایتھرز کی ہائیڈرولائسز ہو کر اصل الکوحلز بنتے ہیں۔ پروٹونیشن پر بننے والا آکسونیم نمک پانی کے نیوکلیوفائل کے حملے سے مزید ٹوٹ کر الکوحلز بناتا ہے۔','له رقیق سلفوریک اسید سره د اوږدې تودونې پر مهال ایترونه هایدرولیز کېږي او اصلي الکولونه جوړوي. د پروټونېشن پر مهال جوړ شوې اکسونیم مالګه د اوبو د نیوکلیوفایل په برید نوره ماتېږي او الکولونه جوړوي.')
visual('chem12-p113-cleavage',cleave)
add('Reaction of ethers with hot concentrated HI or HBr results in a mixture of alcohol and alkyl halide. The reaction involve the formation of oxonium ions, which is then cleaved by attack of iodide or bromide ion to form the corresponding alkyl halide and alcohol.','گرم مرتکز HI یا HBr سے ایتھرز کا تعامل الکوحل اور الکائل ہیلائیڈ کا آمیزہ دیتا ہے۔ اس تعامل میں آکسونیم آئن بنتے ہیں، جو پھر آئیوڈائیڈ یا برومائیڈ آئن کے حملے سے ٹوٹ کر متعلقہ الکائل ہیلائیڈ اور الکوحل بناتے ہیں۔','له تود غلیظ HI یا HBr سره د ایترونو تعامل د الکول او الکایل هالایډ ګډوله ورکوي. په تعامل کې اکسونیم ایونونه جوړېږي، چې بیا د ایوډایډ یا برومایډ ایون په برید ماتېږي او اړوند الکایل هالایډ او الکول جوړوي.')
record=section('18.14','Preparation and reactions of ethers','ایتھرز کی تیاری اور تعاملات','د ایترونو چمتو کول او تعاملونه',paras,layout,blocks,'218–219')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':113,'printedPages':[218,219]}]
record['sourceContinuesOnPdfPage']=114
trim=[{'id':'18.15','startsAt':'R-O-R+H-I'}]
if __name__=='__main__':save(113,[record],trim=trim,chapter_number=18)
