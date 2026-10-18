"""PDF119 printed230–231: structure of carbonyl group, bond angles, physical properties of aldehydes and ketones."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl
import math
F=Fig('arrow119');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'carbon and the oxygen are both sp²':('کاربن اور آکسیجن دونوں sp² ہیں','کاربن او اکسیجن دواړه sp² دي'),'C–H σ bond':('C–H σ بند','C–H σ تړون'),'C–O σ bond':('C–O σ بند','C–O σ تړون'),'C–O π bond':('C–O π بند','C–O π تړون'),
   'lone pairs':('تنہا جوڑے','یوازینۍ جوړې'),'formaldehyde':('فارم الڈیہائیڈ','فورمالدیهاید'),'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'acetone':('ایسیٹون','اسیتون'),
   'butane':('بیوٹین','بیوټان'),'methoxyethane':('میتھوآکسی ایتھین','میتوکسي ایتان'),'propane-1-ol':('پروپین-1-اول','پروپان-1-ول'),'propanal':('پروپانل','پروپانال'),'Ketone':('کیٹون','کیټون'),'Aldehyde':('الڈیہائیڈ','الدیهاید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def orbitals(lang):
 s=F.start(200)
 def lobes(cx,cy,c,n):
  o=''
  for k in range(n):a=math.radians(90*k);o+=f'<ellipse cx="{cx+22*math.cos(a):.1f}" cy="{cy-22*math.sin(a):.1f}" rx="20" ry="11" fill="{c}" stroke="#333" transform="rotate({-90*k} {cx+22*math.cos(a):.1f} {cy-22*math.sin(a):.1f})"/>'
  return o
 s+=f'<circle cx="40" cy="60" r="9" fill="#fdd835" stroke="#333"/>'+t(40,64,'H',11)+f'<circle cx="40" cy="120" r="9" fill="#fdd835" stroke="#333"/>'+t(40,124,'H',11)
 s+=lobes(110,90,'#9ccc65',4)+t(110,95,'C',13)+t(170,95,'+',18)+lobes(230,90,'#9ccc65',4)+t(230,95,'O',13)+F.arrow(280,350,90)
 s+='<ellipse cx="470" cy="50" rx="70" ry="22" fill="#ef9a9a" stroke="#333"/><ellipse cx="470" cy="130" rx="70" ry="22" fill="#ef9a9a" stroke="#333"/><ellipse cx="470" cy="90" rx="60" ry="14" fill="#9ccc65" stroke="#333"/>'
 s+=f'<circle cx="390" cy="75" r="9" fill="#fdd835" stroke="#333"/>'+t(390,79,'H',11)+f'<circle cx="390" cy="105" r="9" fill="#fdd835" stroke="#333"/>'+t(390,109,'H',11)+t(430,95,'C',13)+t(510,95,'O',13)
 s+=t(450,22,lb(lang,'C–H σ bond')+'   '+lb(lang,'C–O σ bond'),12)+t(600,95,lb(lang,'lone pairs'),12)+t(470,166,lb(lang,'C–O π bond'),12)+t(470,190,'H₂C = Ö:',15)+t(140,170,lb(lang,'carbon and the oxygen are both sp²'),12)
 return s+'</svg>'
def angles(lang):
 s=F.start(170)
 for x,(l,r,a1,a2,a3,n) in zip((150,425,700),(('H','H','121.7°','121.7°','116.5°','formaldehyde'),('H₃C','H','123.9°','118.6°','117.5°','acetaldehyde'),('H₃C','CH₃','121.4°','121.4°','117.2°','acetone'))):
  s+=t(x,30,'O',16)+line(x-3,36,x-3,70)+line(x+3,36,x+3,70)+t(x,86,'C',16)+line(x-8,92,x-40,118)+t(x-52,128,l,14)+line(x+8,92,x+40,118)+t(x+52,128,r,14)
  s+=t(x-48,62,a1,12,'#c62828')+t(x+48,62,a2,12,'#c62828')+t(x,128,a3,12,'#c62828')+t(x,156,lb(lang,n),12)
 return s+'</svg>'
def bp(lang):
 s=F.start(190)
 for x,(f,n,b) in zip((150,420,690),(('CH₃CH₂CH₂CH₃','butane','bp 0°C'),('CH₃—O—CH₂CH₃','methoxyethane','bp 8°C'),('CH₃CH₂CH₂—OH','propane-1-ol','bp 97°C'))):s+=t(x,35,f,15)+t(x,55,lb(lang,n),12)+t(x,71,b,12)
 s+=C(300,140,'CH₃CH₂','H')+t(300,162,lb(lang,'propanal'),12)+t(300,178,'bp 49°C',12)+C(560,140,'CH₃','CH₃')+t(560,162,lb(lang,'acetone'),12)+t(560,178,'bp 56°C',12)
 return s+'</svg>'
def hb(lang):
 s=F.start(200)
 for x,(r2,n) in zip((250,600),(("R′",'Ketone'),('H','Aldehyde'))):
  s+=t(x+60,30,'δ−',11)+t(x+60,50,'Ö',16)+line(x+52,56,x+40,70)+t(x+34,82,'H',14)+t(x+20,70,'δ+',11)+line(x+68,56,x+80,70)+t(x+86,82,'H',14)+t(x+100,70,'δ+',11)
  s+=line(x+28,86,x+8,104,1.5,'#222','stroke-dasharray="2 3"')+t(x,110,'Ö',16)+t(x-22,104,'δ−',11)+line(x-3,116,x-3,138)+line(x+3,116,x+3,138)+t(x,152,'C',16)+t(x-22,152,'δ+',11)+line(x-8,158,x-30,176)+t(x-38,188,'R',14)+line(x+8,158,x+30,176)+t(x+38,188,r2,14)+t(x,200,lb(lang,n),12)
 return s.replace('viewBox="0 0 850 200"','viewBox="0 0 850 210"')+'</svg>'

add('19.2 Structure','19.2 ساخت','19.2 جوړښت','heading')
add('Let us consider formaldehyde as an example to illustrate the structure of carbonyl group of aldehyde and ketone. The carbon and oxygen in the carbonyl group, present in aldehydes and ketones are linked by a sigma bond and a pi bond. Both carbon as well as oxygen of the carbonyl group are sp²-hybridized. The carbon-oxygen sigma and pi bonds are formed by linear sp²-sp² and sidewise overlap of p orbitals respectively. Two of the sp²-hybrid orbitals of oxygen has two unshared electron pairs, while two of the sp²-hybrid orbitals of carbon overlap with s orbitals of two hydrogen atoms to form carbon-hydrogen sigma bonds in formaldehyde (Figure 19.1).',
 'الڈیہائیڈ اور کیٹون کے کاربونل گروپ کی ساخت واضح کرنے کے لیے فارم الڈیہائیڈ کو مثال کے طور پر لیں۔ الڈیہائیڈز اور کیٹونز کے کاربونل گروپ میں کاربن اور آکسیجن ایک سگما بند اور ایک پائی بند سے جڑے ہوتے ہیں۔ کاربونل گروپ کا کاربن اور آکسیجن دونوں sp²-ہائبرڈ ہیں۔ کاربن–آکسیجن سگما اور پائی بند بالترتیب sp²-sp² کے سیدھے تداخل اور p آربیٹلوں کے پہلو کے رخ تداخل سے بنتے ہیں۔ آکسیجن کے دو sp²-ہائبرڈ آربیٹلوں میں دو غیر مشترک الیکٹرانی جوڑے ہوتے ہیں، جبکہ فارم الڈیہائیڈ میں کاربن کے دو sp²-ہائبرڈ آربیٹل دو ہائیڈروجن ایٹموں کے s آربیٹلوں سے تداخل کر کے کاربن–ہائیڈروجن سگما بند بناتے ہیں (شکل 19.1)۔',
 'د الدیهاید او کیټون د کاربونیل ګروپ د جوړښت د روښانه کولو لپاره فورمالدیهاید د بېلګې په توګه ونیسئ. په الدیهایډونو او کیټونونو کې د کاربونیل ګروپ کاربن او اکسیجن د یوه سیګما او یوه پای تړون په واسطه تړلي دي. د کاربونیل ګروپ کاربن او اکسیجن دواړه sp²-هایبرېډ دي. د کاربن–اکسیجن سیګما او پای تړونونه په ترتیب سره د sp²-sp² مستقیم تداخل او د p اوربیټالونو اړخیز تداخل په واسطه جوړېږي. د اکسیجن دوه sp²-هایبرېډ اوربیټالونه دوه نه شریکې الکتروني جوړې لري، په داسې حال کې چې په فورمالدیهاید کې د کاربن دوه sp²-هایبرېډ اوربیټالونه د دوو هایدروجني اټومونو له s اوربیټالونو سره تداخل کوي او کاربن–هایدروجن سیګما تړونونه جوړوي (شکل 19.1).')
visual('chem12-figure19-1',orbitals)
add('Figure 19.1 Orbital hybridization model of formaldehyde.','شکل 19.1 فارم الڈیہائیڈ کا آربیٹل ہائبرڈائزیشن ماڈل۔','شکل 19.1 د فورمالدیهاید د اوربیټال هایبرېډیزېشن ماډل.')
add('The three atoms attached to carbonyl carbon lie in a plane and are arranged in trigonal planar manner. The carbon-oxygen bond length is 120 pm, which is significantly shorter than carbon-oxygen bond length in alcohols and ether (142 pm). The bond angles around carbonyl carbon are approximately 120°. Slight deviation is observed depending upon nature of atoms or groups attached to carbon in various aldehydes and ketones. The bond angles in some of the known aldehydes and ketones are shown in (Figure 19.2).',
 'کاربونل کاربن سے جڑے تینوں ایٹم ایک مستوی میں ہوتے ہیں اور تکونی مستوی ترتیب میں ہوتے ہیں۔ کاربن–آکسیجن بند کی لمبائی 120 pm ہے، جو الکوحلز اور ایتھر میں کاربن–آکسیجن بند کی لمبائی (142 pm) سے نمایاں طور پر کم ہے۔ کاربونل کاربن کے گرد بند زاویے تقریباً 120° ہیں۔ مختلف الڈیہائیڈز اور کیٹونز میں کاربن سے جڑے ایٹموں یا گروپوں کی نوعیت کے لحاظ سے معمولی انحراف دیکھا جاتا ہے۔ چند معلوم الڈیہائیڈز اور کیٹونز کے بند زاویے (شکل 19.2) میں دکھائے گئے ہیں۔',
 'له کاربونیل کاربن سره تړلي درې اټومونه په یوه سطحه کې پراته دي او په درې ګوټي سطحي ډول ترتیب شوي. د کاربن–اکسیجن تړون اوږدوالی 120 pm دی، چې په الکولونو او ایتر کې د کاربن–اکسیجن تړون له اوږدوالي (142 pm) څخه په ښکاره لنډ دی. د کاربونیل کاربن شاوخوا د تړون زاویې نږدې 120° دي. په بېلابېلو الدیهایډونو او کیټونونو کې له کاربن سره د تړلو اټومونو یا ګروپونو د طبیعت له مخې لږ انحراف لیدل کېږي. د ځینو پېژندل شویو الدیهایډونو او کیټونونو د تړون زاویې په (شکل 19.2) کې ښودل شوې.')
visual('chem12-figure19-2',angles)
add('Figure 19.2 Bond angles in some aldehydes and ketones.','شکل 19.2 بعض الڈیہائیڈز اور کیٹونز میں بند زاویے۔','شکل 19.2 په ځینو الدیهایډونو او کیټونونو کې د تړون زاویې.')
add('19.3 Physical Properties','19.3 طبعی خصوصیات','19.3 فزیکي ځانګړنې','heading')
for e,u,p in [('Lower aldehydes like formaldehyde and acetaldehyde have very sharp pungent odour whereas higher members of aldehydes as well as most of the ketones have pleasant odour.','فارم الڈیہائیڈ اور ایسیٹ الڈیہائیڈ جیسے کم کاربن والے الڈیہائیڈز کی بو بہت تیز اور چبھنے والی ہوتی ہے جبکہ الڈیہائیڈز کے بڑے ارکان اور زیادہ تر کیٹونز کی بو خوشگوار ہوتی ہے۔','ټیټ الدیهایډونه لکه فورمالدیهاید او اسیټالدیهاید ډېر تېز او سوځوونکی بوی لري، په داسې حال کې چې د الدیهایډونو لوړ غړي او ډېری کیټونونه خوندور بوی لري.'),
 ('Formaldehyde is a gas at room temperature while other aldehydes are colourless volatile liquids. Formaldehyde is often stored and used as a 40% aqueous solution called formalin. Acetone and other members of ketone series are also colourless volatile liquids.','فارم الڈیہائیڈ کمرے کے درجہ حرارت پر گیس ہے جبکہ دوسرے الڈیہائیڈز بے رنگ اڑنے والے مائع ہیں۔ فارم الڈیہائیڈ اکثر 40% آبی محلول کے طور پر ذخیرہ اور استعمال ہوتا ہے جسے فارملین کہتے ہیں۔ ایسیٹون اور کیٹون سلسلے کے دوسرے ارکان بھی بے رنگ اڑنے والے مائع ہیں۔','فورمالدیهاید د کوټې په تودوخه کې ګاز دی، خو نور الدیهایډونه بې رنګه الوتونکي مایعات دي. فورمالدیهاید ډېری د 40% اوبلن محلول په توګه ساتل او کارول کېږي چې فورمالین بلل کېږي. اسیتون او د کیټون لړۍ نور غړي هم بې رنګه الوتونکي مایعات دي.'),
 ('Aldehydes and ketones are polar compounds due to high dipole moment of their C=O bond. As a result they have higher boiling points than the corresponding alkanes and non-polar compounds like ethers. But they cannot form hydrogen bonds with themselves, therefore they usually have lower boiling points than corresponding alcohols. Boiling point of aldehydes and ketones increase with the increase in the molecular mass.','الڈیہائیڈز اور کیٹونز اپنے C=O بند کے زیادہ ڈائی پول مومنٹ کی وجہ سے قطبی مرکبات ہیں۔ نتیجتاً ان کے نقطۂ جوش متعلقہ الکینز (اکیلے بند والے) اور ایتھرز جیسے غیر قطبی مرکبات سے زیادہ ہیں۔ لیکن یہ آپس میں ہائیڈروجن بند نہیں بنا سکتے، اس لیے ان کے نقطۂ جوش عموماً متعلقہ الکوحلز سے کم ہوتے ہیں۔ سالماتی کمیت بڑھنے سے الڈیہائیڈز اور کیٹونز کا نقطۂ جوش بڑھتا ہے۔','الدیهایډونه او کیټونونه د خپل C=O تړون د لوړ ډای پول مومنټ له امله قطبي مرکبات دي. په پایله کې له اړوندو الکانونو او غیر قطبي مرکباتو لکه ایترونو لوړ د ایشېدو ټکي لري. خو له یو بل سره هایدروجني تړون نه شي جوړولی، نو معمولاً له اړوندو الکولونو ټیټ د ایشېدو ټکي لري. د مالیکولي کتلې په زیاتېدو د الدیهایډونو او کیټونونو د ایشېدو ټکی زیاتېږي.')]:
 add(e,u,p,'list')
visual('chem12-p119-boiling-points',bp)
add('Lower aldehydes and ketones, upto four carbon atoms are water soluble. Water solubility decreases as the size of the non-polar alkyl group increases. Higher members of aldehydes and ketones are usually insoluble in water, while formaldehyde is highly soluble in water. Carbonyl compounds cannot form hydrogen bonds with themselves as there is no hydrogen on the carbonyl oxygen. However, their solubility in water is due to hydrogen bond formation of carbonyl oxygen with water molecules (Figure 19.3)',
 'چار کاربن ایٹموں تک کے کم کاربن والے الڈیہائیڈز اور کیٹونز پانی میں حل پذیر ہیں۔ غیر قطبی الکائل گروپ کا حجم بڑھنے سے پانی میں حل پذیری گھٹتی ہے۔ الڈیہائیڈز اور کیٹونز کے بڑے ارکان عموماً پانی میں ناحل پذیر ہیں، جبکہ فارم الڈیہائیڈ پانی میں بہت حل پذیر ہے۔ کاربونل مرکبات آپس میں ہائیڈروجن بند نہیں بنا سکتے کیونکہ کاربونل آکسیجن پر ہائیڈروجن نہیں ہوتا۔ تاہم پانی میں ان کی حل پذیری کاربونل آکسیجن کے پانی کے سالمات سے ہائیڈروجن بند بنانے کی وجہ سے ہے (شکل 19.3)',
 'تر څلورو کاربني اټومونو ټیټ الدیهایډونه او کیټونونه په اوبو کې حلېږي. د غیر قطبي الکایل ګروپ د اندازې په زیاتېدو په اوبو کې حلېدنه کمېږي. د الدیهایډونو او کیټونونو لوړ غړي معمولاً په اوبو کې نه حلېږي، خو فورمالدیهاید په اوبو کې ډېر حلېږي. کاربونیل مرکبات له یو بل سره هایدروجني تړون نه شي جوړولی ځکه پر کاربونیل اکسیجن هایدروجن نشته. خو په اوبو کې د دوی حلېدنه د اوبو له مالیکولونو سره د کاربونیل اکسیجن د هایدروجني تړون له امله ده (شکل 19.3)','list')
visual('chem12-figure19-3',hb)
add('Figure 19.3 Hydrogen bond of aldehyde and ketone with water.','شکل 19.3 پانی کے ساتھ الڈیہائیڈ اور کیٹون کا ہائیڈروجن بند۔','شکل 19.3 له اوبو سره د الدیهاید او کیټون هایدروجني تړون.')
add('19.4 Preparation of aldehydes and Ketones','19.4 الڈیہائیڈز اور کیٹونز کی تیاری','19.4 د الدیهایډونو او کیټونونو چمتو کول','heading')
add('Aldehydes and ketones may be prepared by the following methods.','الڈیہائیڈز اور کیٹونز درج ذیل طریقوں سے تیار کیے جا سکتے ہیں۔','الدیهایډونه او کیټونونه په لاندې طریقو چمتو کېدای شي.')
record=section('19.3','Structure and physical properties of aldehydes and ketones','الڈیہائیڈز اور کیٹونز کی ساخت اور طبعی خصوصیات','د الدیهایډونو او کیټونونو جوړښت او فزیکي ځانګړنې',paras,layout,blocks,'230–231')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':119,'printedPages':[230,231]}]
record['sourceContinuesOnPdfPage']=120
carry=[{'from':'19.3','to':'19.4','startsAt':'19.4.1 Ozonolysis of Alkenes'}]
if __name__=='__main__':save(119,[record],carry=carry,chapter_number=19)
