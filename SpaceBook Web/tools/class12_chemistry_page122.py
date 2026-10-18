"""PDF122 printed236–237: cyanohydrin note, relative reactivity, reduction to hydrocarbons (Clemmensen, Wolf–Kishner)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl
F=Fig('arrow122');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'A ketone':('ایک کیٹون','یو کیټون'),'An aldehyde':('ایک الڈیہائیڈ','یو الدیهاید'),'has two electron-donating alkyl groups':('دو الیکٹران دینے والے الکائل گروپ رکھتا ہے','دوه الکترون ورکوونکي الکایل ګروپونه لري'),
   'that stabilize the partial positive charge':('جو جزوی مثبت چارج کو پائیدار کرتے ہیں','چې نیمګړی مثبت چارج ثابتوي'),'has only one electron-donating alkyl group':('صرف ایک الیکٹران دینے والا الکائل گروپ رکھتا ہے','یوازې یو الکترون ورکوونکی الکایل ګروپ لري'),
   'that stabilizes the partial positive charge':('جو جزوی مثبت چارج کو پائیدار کرتا ہے','چې نیمګړی مثبت چارج ثابتوي'),'ketone':('کیٹون','کیټون'),'less electrophilic':('کم الیکٹروفائلی','لږ الکتروفایلي'),'alkoxide':('الکوآکسائیڈ','الکوکساید'),
   'more crowded':('زیادہ گنجان','ډېر ګڼ'),'product':('پیداوار','محصول'),'aldehyde':('الڈیہائیڈ','الدیهاید'),'more electrophilic':('زیادہ الیکٹروفائلی','ډېر الکتروفایلي'),'less crowded':('کم گنجان','لږ ګڼ'),
   'aldehyde/ketone':('الڈیہائیڈ/کیٹون','الدیهاید/کیټون'),'alkane':('الکین (اکیلا بند)','الکان'),'acetaldehyde (ethanal)':('ایسیٹ الڈیہائیڈ (ایتھانل)','اسیټالدیهاید (ایتانال)'),'ethane':('ایتھین (اکیلا بند)','ایتان'),
   'acetone':('ایسیٹون','اسیتون'),'propane':('پروپین (اکیلا بند)','پروپان'),'hydrazine':('ہائیڈرازین','هایدرازین'),'hydrazone':('ہائیڈرازون','هایدرازون'),'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'acetaldehdye':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def electronic(lang):
 s=F.start(140)+C(220,60,'R','R')+t(222,74,'δ+',10)+t(220,86,lb(lang,'A ketone'),12)+t(220,104,lb(lang,'has two electron-donating alkyl groups'),12)+t(220,120,lb(lang,'that stabilize the partial positive charge'),12)
 s+=C(620,60,'R','H')+t(622,74,'δ+',10)+t(620,86,lb(lang,'An aldehyde'),12)+t(620,104,lb(lang,'has only one electron-donating alkyl group'),12)+t(620,120,lb(lang,'that stabilizes the partial positive charge'),12)
 return s+'</svg>'
def tet(x,y,top,l,r,b2):return t(x-30,y-24,top,14)+line(x-16,y-18,x-6,y-8)+t(x,y+4,'C',15)+line(x+6,y-6,x+20,y-20)+t(x+30,y-24,l,14)+line(x-6,y+8,x-20,y+22)+t(x-26,y+34,r,13)+line(x+6,y+8,x+20,y+22)+t(x+26,y+34,b2,13)
def steric(lang):
 s=F.start(260)
 for i,(b,n1,n2,n3,n4) in enumerate((('R','ketone','less electrophilic','more crowded','more crowded'),('H','aldehyde','more electrophilic','less crowded','less crowded'))):
  y=60+120*i;s+=C(140,y,'R',b)+t(140,y+24,lb(lang,n1),12)+t(140,y+40,lb(lang,n2),12,'#1565c0')+F.arrow(220,310,y-6,'N̈u⁻')
  s+=tet(390,y,'O⁻','Nu','R',b)+t(390,y+52,lb(lang,'alkoxide'),12)+t(390,y+66,lb(lang,n3),12,'#ad1457')+F.eq(470,560,y-6)+t(515,y-18,'H—Nu',12)+t(515,y+16,'−N̈u⁻',12)
  s+=tet(660,y,'HO','Nu','R',b)+t(660,y+52,lb(lang,'product'),12)+t(660,y+66,lb(lang,n4),12,'#ad1457')
 return s+'</svg>'
def clem(lang):
 s=F.start(250)
 for i,(l,r,n,p,pn) in enumerate((('','','aldehyde/ketone','—CH₂—  +  H₂O','alkane'),('CH₃','H','acetaldehyde (ethanal)','CH₃—CH₃  +  H₂O','ethane'),('CH₃','CH₃','acetone','CH₃—CH₂—CH₃  +  H₂O','propane'))):
  y=60+80*i;s+=C(170,y,l,r)+t(170,y+22,lb(lang,n),12)+F.arrow(300,450,y-6,'Zn-Hg, conc. HCl')+t(600,y,p,15)+t(580,y+22,lb(lang,pn),12)
 return s+'</svg>'
def wk(lang):
 s=F.start(220)
 for i,(l,r,n,hz,p,pn) in enumerate((('','','aldehyde/ketone','—C—','—CH₂—','alkane'),('CH₃','H','acetaldehyde','CH₃—C—H','CH₃—CH₃','ethane'))):
  y=70+110*i;s+=C(120,y,l,r)+t(120,y+22,lb(lang,n),12)+t(250,y,'+ NH₂—NH₂',15)+t(255,y+22,lb(lang,'hydrazine'),12)+F.arrow(320,380,y-6,'','−H₂O')
  s+=t(440,y-36,'N—NH₂',14)+line(437,y-30,437,y-15)+line(443,y-30,443,y-15)+t(440,y,hz,15)+t(440,y+22,lb(lang,'hydrazone' if i==0 else 'acetaldehdye'),12)+(t(440,y+38,lb(lang,'hydrazone'),12) if i else '')
  s+=F.arrow(500,610,y-6,'KOH, 200°C','−N₂')+t(690,y,p,15)+t(690,y+22,lb(lang,pn),12)
 return s+'</svg>'

add('Addition of hydrogen cyanide in the presence of cyanide base to form cynohydrins, follow this type of mechanism (Section 19.6.3.3).','سائنائیڈ اساس کی موجودگی میں ہائیڈروجن سائنائیڈ کا اضافہ، جس سے سائنو ہائیڈرنز بنتے ہیں، اسی قسم کے طریق کار پر ہوتا ہے (حصہ 19.6.3.3)۔','د سیانایډ قلوي په شتون کې د هایدروجن سیانایډ زیاتول چې سیانوهایډرینونه جوړوي، همدا ډول میکانیزم تعقیبوي (برخه 19.6.3.3).')
add('19.6.2 Relative Reactivity','19.6.2 اضافی تعامل پذیری','19.6.2 نسبي تعامل وړتیا','heading')
add('Generally aldehydes are more reactive than ketones towards nucleophilic additions. They usually react more quickly than ketones and the position of the equilibrium usually lies more toward the products than with ketones. The enhanced reactivity of aldehydes is due to an electronic effect and a steric effect.','عموماً الڈیہائیڈز نیوکلیوفائلی اضافوں کے لیے کیٹونز سے زیادہ تعامل پذیر ہیں۔ یہ عموماً کیٹونز سے زیادہ تیزی سے تعامل کرتے ہیں اور توازن کا مقام کیٹونز کی نسبت زیادہ پیداواروں کی طرف ہوتا ہے۔ الڈیہائیڈز کی زیادہ تعامل پذیری ایک برقی اثر اور ایک فضائی اثر کی وجہ سے ہے۔','عموماً الدیهایډونه د نیوکلیوفایلي اضافو په وړاندې له کیټونونو ډېر تعامل کوونکي دي. معمولاً له کیټونونو چټک تعامل کوي او د توازن ځای د کیټونونو په پرتله ډېر د محصولاتو خوا ته وي. د الدیهایډونو زیات تعامل د یوه برقي اغېز او یوه فضايي اغېز له امله دی.')
add('(a) Electronic Effect','(a) برقی اثر','(a) برقي اغېز','heading')
add('A ketone has two electron donating alkyl groups that can stabilize (neutralize) the partial positive on the carbon atom of the carbonyl group. In contrast, aldehydes have only one electron-donating group (formaldehyde has none); thus the partial positive charge of an aldehyde is less stabilized than a ketone. As a result, aldehydes are more electrophilic than ketones and therefore more reactive.','کیٹون میں دو الیکٹران دینے والے الکائل گروپ ہوتے ہیں جو کاربونل گروپ کے کاربن ایٹم پر جزوی مثبت چارج کو پائیدار (بے اثر) کر سکتے ہیں۔ اس کے برعکس الڈیہائیڈز میں صرف ایک الیکٹران دینے والا گروپ ہوتا ہے (فارم الڈیہائیڈ میں کوئی نہیں)؛ اس لیے الڈیہائیڈ کا جزوی مثبت چارج کیٹون کی نسبت کم پائیدار ہوتا ہے۔ نتیجتاً الڈیہائیڈز کیٹونز سے زیادہ الیکٹروفائلی اور اس لیے زیادہ تعامل پذیر ہیں۔','کیټون دوه الکترون ورکوونکي الکایل ګروپونه لري چې د کاربونیل ګروپ پر کاربني اټوم نیمګړی مثبت چارج ثابتولی (بې اثره کولی) شي. په مقابل کې الدیهایډونه یوازې یو الکترون ورکوونکی ګروپ لري (فورمالدیهاید هېڅ نه لري)؛ نو د الدیهاید نیمګړی مثبت چارج د کیټون په پرتله لږ ثابت دی. په پایله کې الدیهایډونه له کیټونونو ډېر الکتروفایلي او له همدې امله ډېر تعامل کوونکي دي.')
visual('chem12-p122-electronic-effect',electronic)
add('(b) Steric Hindrance','(b) فضائی رکاوٹ','(b) فضايي خنډ','heading')
add('An aldehyde has only one bulky alkyl group (except formaldehyde) while ketone has two alkyl groups with carbonyl carbon. Thus the aldehydic carbonyl carbon is more exposed toward nucleophilic attack, than ketones. Similarly the transition state of nucleophilic addition of aldehyde is less crowded and of lower energy than ketones.','الڈیہائیڈ میں صرف ایک بھاری الکائل گروپ ہوتا ہے (فارم الڈیہائیڈ کے سوا) جبکہ کیٹون میں کاربونل کاربن کے ساتھ دو الکائل گروپ ہوتے ہیں۔ اس لیے الڈیہائیڈی کاربونل کاربن کیٹونز کی نسبت نیوکلیوفائلی حملے کے لیے زیادہ کھلا ہوتا ہے۔ اسی طرح الڈیہائیڈ کے نیوکلیوفائلی اضافے کی عبوری حالت کیٹونز کی نسبت کم گنجان اور کم توانائی والی ہوتی ہے۔','الدیهاید یوازې یو دروند الکایل ګروپ لري (پرته له فورمالدیهاید)، خو کیټون له کاربونیل کاربن سره دوه الکایل ګروپونه لري. نو د الدیهایدي کاربونیل کاربن د کیټونونو په پرتله د نیوکلیوفایلي برید لپاره ډېر بربنډ دی. همدارنګه د الدیهاید د نیوکلیوفایلي اضافې انتقالي حالت د کیټونونو په پرتله لږ ګڼ او ټیټې انرژۍ لرونکی دی.')
visual('chem12-p122-steric',steric)
add('19.6.3 Reduction of Aldehydes and Ketones','19.6.3 الڈیہائیڈز اور کیٹونز کی تخفیف','19.6.3 د الدیهایډونو او کیټونونو ارجاع','heading')
add('Addition of hydrogen to aldehydes and ketones is called reduction. Following are some important reactions of aldehydes and ketones that involve reduction.','الڈیہائیڈز اور کیٹونز میں ہائیڈروجن کے اضافے کو تخفیف کہتے ہیں۔ الڈیہائیڈز اور کیٹونز کے چند اہم تعاملات جن میں تخفیف شامل ہے درج ذیل ہیں۔','الدیهایډونو او کیټونونو ته د هایدروجن زیاتول ارجاع بلل کېږي. د الدیهایډونو او کیټونونو ځینې مهم تعاملونه چې ارجاع رانغاړي لاندې دي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Formaldehyde is the most reactive than all other higher aldehydes and ketones. The high reactivity is attributed to the unavailability of electron donating bulky alkyl groups with carbonyl carbon of formaldehyde.','فارم الڈیہائیڈ دوسرے تمام بڑے الڈیہائیڈز اور کیٹونز سے زیادہ تعامل پذیر ہے۔ اس زیادہ تعامل پذیری کی وجہ فارم الڈیہائیڈ کے کاربونل کاربن کے ساتھ الیکٹران دینے والے بھاری الکائل گروپوں کا نہ ہونا ہے۔','فورمالدیهاید له ټولو نورو لوړو الدیهایډونو او کیټونونو ډېر تعامل کوونکی دی. دا لوړ تعامل د فورمالدیهاید له کاربونیل کاربن سره د الکترون ورکوونکو درنو الکایل ګروپونو نشتوالي ته منسوب دی.')
add('19.6.3.1 To Hydrocarbons','19.6.3.1 ہائیڈروکاربنز تک','19.6.3.1 هایدروکاربنونو ته','heading')
add('Aldehydes and ketones can be reduced to saturated hydrocarbons either by Clemmensen reduction or by Wolf-Kishner reduction.','الڈیہائیڈز اور کیٹونز کی سیر شدہ ہائیڈروکاربنز تک تخفیف یا تو کلیمنسن تخفیف یا وولف-کشنر تخفیف سے کی جا سکتی ہے۔','الدیهایډونه او کیټونونه یا د کلیمنسن ارجاع یا د وولف-کشنر ارجاع په واسطه مشبوع هایدروکاربنونو ته ارجاع کېدای شي.')
add('(a) Clemmenson Reduction','(a) کلیمنسن تخفیف','(a) د کلیمنسن ارجاع','heading')
add('In this reaction aldehydes and ketones are reduced to alkanes in the presence of Zinc amalgam (Zn-Hg) and conc. HCl as reducing agent.','اس تعامل میں زنک ملغم (Zn-Hg) اور مرتکز HCl کی بطور تخفیفی عامل موجودگی میں الڈیہائیڈز اور کیٹونز کی تخفیف الکینز (اکیلے بند والے) میں ہوتی ہے۔','په دې تعامل کې د ارجاع کوونکي عامل په توګه د جستو ملغمې (Zn-Hg) او غلیظ HCl په شتون کې الدیهایډونه او کیټونونه الکانونو ته ارجاع کېږي.')
visual('chem12-p122-clemmensen',clem)
add('(b) Wolf-Kishner Reduction','(b) وولف-کشنر تخفیف','(b) د وولف-کشنر ارجاع','heading')
add('When an aldehyde or ketone is treated with hydrazine a corresponding hydrazone is obtained, which on heating with KOH in boiling ethylene glycol (200°C) gives corresponding alkanes.','جب الڈیہائیڈ یا کیٹون کو ہائیڈرازین سے عمل کرایا جائے تو متعلقہ ہائیڈرازون حاصل ہوتا ہے، جو ابلتے ایتھیلین گلائیکول (200°C) میں KOH کے ساتھ گرم کرنے پر متعلقہ الکینز (اکیلے بند والے) دیتا ہے۔','کله چې الدیهاید یا کیټون له هایدرازین سره تعامل وکړي، اړوند هایدرازون ترلاسه کېږي، چې په ایشېدونکي ایتیلین ګلایکول (200°C) کې له KOH سره د تودولو پر مهال اړوند الکانونه ورکوي.')
visual('chem12-p122-wolf-kishner',wk)
record=section('19.6','Relative reactivity and reduction to hydrocarbons','اضافی تعامل پذیری اور ہائیڈروکاربنز تک تخفیف','نسبي تعامل وړتیا او هایدروکاربنونو ته ارجاع',paras,layout,blocks,'236–237')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':122,'printedPages':[236,237]}]
record['sourceContinuesOnPdfPage']=123
issues=[{'id':'chem12-p236-spellings','printedPage':236,'description':'Printed "cynohydrins", "Clemmenson", "Wolf-Kishner" and "acetaldehdye" retained.'}]
if __name__=='__main__':save(122,[record],issues=issues,chapter_number=19)
