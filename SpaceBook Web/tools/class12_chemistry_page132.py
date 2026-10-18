"""PDF132 printed258–259: preparation of carboxylic acids (nitriles, alcohols, aldehydes, alkylbenzenes) and 20.6 Reactivity introduction."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,carbonyl,tetra
F=Fig('arrow132');t=F.t;line=F.line
C=lambda *a,**k:carbonyl(F,*a,**k);T=lambda *a,**k:tetra(F,*a,**k)
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'nitrile':('نائٹرائل','نایټرایل'),'carboxylic acid':('کاربوکسلک ایسڈ','کاربوکسیلیک اسید'),'sodium carboxylate':('سوڈیم کاربوکسیلیٹ','سوډیم کاربوکسیلېټ'),'Acid-catalyzed hydrolysis:':('تیزاب سے عمل انگیز ہائیڈرولائسز:','اسیدي کتلستي هایدرولایسس:'),
   'Base-catalyzed hydrolysis:':('اساس سے عمل انگیز ہائیڈرولائسز:','قلوي کتلستي هایدرولایسس:'),'ethanenitrile':('ایتھین نائٹرائل','ایتان نایټرایل'),'acetic acid':('ایسیٹک ایسڈ','اسیټیک اسید'),'1° -alcohol':('1° -الکوحل','1° -الکول'),
   'aldehyde':('الڈیہائیڈ','الدیهاید'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'acetaldehyde':('ایسیٹ الڈیہائیڈ','اسیټالدیهاید'),'toluene':('ٹولوئین','ټولوین'),'benzoic acid':('بینزوئک ایسڈ','بنزویک اسید'),
   'ethylbenzene':('ایتھائل بینزین','ایتیل بنزین'),'carboxylic acid':('کاربوکسلک ایسڈ','کاربوکسیلیک اسید'),'or derivative':('یا مشتق','یا مشتق'),'substitution product':('استبدالی پیداوار','د بدلون محصول')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def nitr(lang):
 s=F.start(310)+t(20,22,lb(lang,'Acid-catalyzed hydrolysis:'),13,'#222').replace('text-anchor="middle"','text-anchor="start"')
 s+=t(180,70,'R—C≡N  +  2H₂O  +  HCl',16)+t(110,92,lb(lang,'nitrile'),12)+F.arrow(320,420,64)+C(520,70,'R','OH')+t(520,94,lb(lang,'carboxylic acid'),12)+t(660,70,'+  NH₄Cl',16)
 s+=t(20,132,lb(lang,'Base-catalyzed hydrolysis:'),13,'#222').replace('text-anchor="middle"','text-anchor="start"')
 s+=t(180,180,'R—C≡N  +  H₂O  +  NaOH',16)+t(110,202,lb(lang,'nitrile'),12)+F.arrow(320,420,174)+C(520,180,'R','O⁻Na⁺')+t(520,204,lb(lang,'sodium carboxylate'),12)+t(670,180,'+  NH₃',16)
 s+=t(170,280,'CH₃—C≡N  +  2H₂O',16)+t(110,302,lb(lang,'ethanenitrile'),12)+F.arrow(300,420,274,'H⁺ or ⁻OH')+C(520,280,'CH₃','OH')+t(520,304,lb(lang,'acetic acid'),12)+t(660,280,'+  NH₃',16)
 return s.replace('viewBox="0 0 850 310"','viewBox="0 0 850 315"')+'</svg>'
def alc(lang):
 s=F.start(260)
 for i,(g,n1,n2,n3) in enumerate((('R','1° -alcohol','aldehyde','carboxylic acid'),('CH₃','ethyl alcohol','acetaldehyde','acetic acid'))):
  y=60+130*i;s+=T(110,y,'OH',g,'H','H')+t(110,y+60,lb(lang,n1),12)+F.arrow(200,300,y-6,'[O]','−H₂O')+C(400,y,g,'H')+t(400,y+26,lb(lang,n2),12)+F.arrow(480,580,y-6,'[O]')+C(680,y,g,'OH')+t(680,y+26,lb(lang,n3),12)
 return s+'</svg>'
def ald(lang):
 s=F.start(90)+C(250,50,'R','H')+t(250,74,lb(lang,'aldehyde'),12)+F.arrow(340,460,44,'[O]')+C(560,50,'R','OH')+t(560,74,lb(lang,'carboxylic acid'),12)
 return s+'</svg>'
def alkbz(lang):
 s=F.start(270)
 s+=F.ring(110,80,30,subs={1:'CH₃'})+t(110,135,lb(lang,'toluene'),12)+t(220,86,'+ 3[O]',16)+F.arrow(280,410,80,'1. KMnO₄, ⁻OH','2. H₃O⁺')+F.ring(500,80,30,subs={1:'COOH'})+t(500,135,lb(lang,'benzoic acid'),12)+t(660,86,'+  H₂O',16)
 s+=F.ring(110,210,30,subs={1:'CH₂—CH₃'})+t(110,265,lb(lang,'ethylbenzene'),12)+t(220,216,'+ 6[O]',16)+F.arrow(280,410,210,'1. KMnO₄, ⁻OH','2. H₃O⁺')+F.ring(500,210,30,subs={1:'COOH'})+t(500,265,lb(lang,'benzoic acid'),12)+t(690,216,'+ CO₂ + 2H₂O',16)
 return s+'</svg>'
def subst(lang):
 s=F.start(110)+C(200,50,'R','Z')+t(200,74,lb(lang,'carboxylic acid'),12)+t(200,90,lb(lang,'or derivative'),12)+t(310,56,'+  N̈u⁻',16)+F.arrow(370,470,50)+C(570,50,'R','Nu')+t(570,74,lb(lang,'substitution product'),12)+t(690,56,'+  Z̈⁻',16)
 return s+'</svg>'

add('20.5.2 Hydrolysis of Nitriles','20.5.2 نائٹرائلز کی ہائیڈرولائسز','20.5.2 د نایټرایلونو هایدرولایسس','heading')
add('Hydrolysis of nitriles with aqueous acid or base yields a carboxylic acid. In the presence of base catalyst, the final product is actually salt of carboxylic acid, which on acid workup yields carboxylic acid.','آبی تیزاب یا اساس سے نائٹرائلز کی ہائیڈرولائسز کاربوکسلک ایسڈ دیتی ہے۔ اساسی عمل انگیز کی موجودگی میں آخری پیداوار دراصل کاربوکسلک ایسڈ کا نمک ہوتی ہے، جو تیزابی ورک اپ پر کاربوکسلک ایسڈ دیتا ہے۔','د اوبلن اسید یا قلوي په واسطه د نایټرایلونو هایدرولایسس کاربوکسیلیک اسید ورکوي. د قلوي کتلست په شتون کې وروستی محصول په حقیقت کې د کاربوکسیلیک اسید مالګه وي، چې په اسیدي ورک اپ کاربوکسیلیک اسید ورکوي.')
visual('chem12-p132-nitrile-hydrolysis',nitr)
add('The reaction proceeds through the formation of an amide intermediate which may be isolated if desired. Hydrolysis of ethanenitrile yield acetic acid.','یہ تعامل ایک امائیڈ درمیانی کے بننے سے آگے بڑھتا ہے جسے ضرورت ہو تو الگ کیا جا سکتا ہے۔ ایتھین نائٹرائل کی ہائیڈرولائسز ایسیٹک ایسڈ دیتی ہے۔','دا تعامل د امایډ منځني په جوړېدو مخ ته ځي چې که اړتیا وي جلا کېدای شي. د ایتان نایټرایل هایدرولایسس اسیټیک اسید ورکوي.')
add('20.5.3 Oxidation of Primary Alcohols','20.5.3 ابتدائی الکوحلز کی تکسید','20.5.3 د لومړنیو الکولونو اکسیډېشن','heading')
add('Primary alcohols can be oxidized to carboxylic acids by oxidizing agents like acidified permangnate or dichromate, through intermediate aldehyde. (Section 18.1.7.5)','ابتدائی الکوحلز کی تیزابی پرمینگنیٹ یا ڈائی کرومیٹ جیسے تکسیدی عاملوں سے درمیانی الڈیہائیڈ کے ذریعے کاربوکسلک ایسڈز تک تکسید کی جا سکتی ہے۔ (حصہ 18.1.7.5)','لومړني الکولونه د اسیدي پرمنګنېټ یا ډای کرومېټ په څېر اکسیډایز کوونکو عاملونو په واسطه د منځني الدیهاید له لارې کاربوکسیلیک اسیدونو ته اکسیډایز کېدای شي. (برخه 18.1.7.5)')
visual('chem12-p132-alcohol-oxidation',alc)
add('20.5.4 Oxidation of Aldehydes','20.5.4 الڈیہائیڈز کی تکسید','20.5.4 د الدیهایډونو اکسیډېشن','heading')
add('Oxidation of an aldehyde in the presence of oxidizing agents like acidified permanganate dichromate or silver oxide gives a carboxylic acid with the same number of carbon atoms (Sections 18.1.7.5 and 19.6.4).','تیزابی پرمینگنیٹ، ڈائی کرومیٹ یا سلور آکسائیڈ جیسے تکسیدی عاملوں کی موجودگی میں الڈیہائیڈ کی تکسید اتنے ہی کاربن ایٹموں والا کاربوکسلک ایسڈ دیتی ہے (حصے 18.1.7.5 اور 19.6.4)۔','د اسیدي پرمنګنېټ، ډای کرومېټ یا سلور اکساید په څېر اکسیډایز کوونکو عاملونو په شتون کې د الدیهاید اکسیډېشن د ورته شمېر کاربني اټومونو لرونکی کاربوکسیلیک اسید ورکوي (برخې 18.1.7.5 او 19.6.4).')
visual('chem12-p132-aldehyde-oxidation',ald)
add('20.5.5 Oxidation of Alkyl Benzenes','20.5.5 الکائل بینزینز کی تکسید','20.5.5 د الکایل بنزینونو اکسیډېشن','heading')
add('Benzoic acid can be prepared by the oxidation of alkyl side chain present on the benzene ring, with oxidizing agent like alkaline permanganate. Any side chain is converted to carboxyl group, and benzoic acid is formed in product. The purple colour of the potassium permanganate is eventually replaced by a dark brown precipitate of manganese dioxide. The mixture is finally acidified with dilute sulphuric acid.',
 'بینزوئک ایسڈ بینزین رنگ پر موجود الکائل ضمنی زنجیر کی اساسی پرمینگنیٹ جیسے تکسیدی عامل سے تکسید کر کے تیار کیا جا سکتا ہے۔ کوئی بھی ضمنی زنجیر کاربوکسل گروپ میں بدل جاتی ہے اور پیداوار میں بینزوئک ایسڈ بنتا ہے۔ پوٹاشیم پرمینگنیٹ کا جامنی رنگ بالآخر مینگنیز ڈائی آکسائیڈ کے گہرے بھورے رسوب سے بدل جاتا ہے۔ آخر میں آمیزے کو ہلکے سلفیورک ایسڈ سے تیزابی بنایا جاتا ہے۔',
 'بنزویک اسید د بنزین پر حلقه د شته الکایل څنګیز ځنځیر د قلوي پرمنګنېټ په څېر اکسیډایز کوونکي عامل په واسطه د اکسیډېشن له لارې چمتو کېدای شي. هر څنګیز ځنځیر په کاربوکسیل ګروپ بدلېږي او په محصول کې بنزویک اسید جوړېږي. د پوتاشیم پرمنګنېټ ارغواني رنګ په پای کې د منګنیز ډای اکساید د تور نسواري رسوب په واسطه ځای نیول کېږي. په پای کې ګډوله د رقیق سلفوریک اسید په واسطه اسیدي کېږي.')
visual('chem12-p132-alkylbenzene-oxidation',alkbz)
add('The reaction illustrates the striking stability of aromatic rings towards oxidizing agents.','یہ تعامل تکسیدی عاملوں کے مقابلے میں ارومیٹک رنگز کی نمایاں پائیداری ظاہر کرتا ہے۔','دا تعامل د اکسیډایز کوونکو عاملونو په وړاندې د اروماتیک حلقو په زړه پورې ثبات ښيي.')
add('20.6 Reactivity','20.6 تعامل پذیری','20.6 تعامل وړتیا','heading')
add('The carboxylic group is so named because it contains a carboxyl group and, a hydroxyl group. The two groups influence each other to such an extent that the reactivity of carboxylic acids shows little resemblance to those of carbonyl compounds (aldehydes and ketones) on one hand and alcohols on the other hand.','کاربوکسلک گروپ کا یہ نام اس لیے ہے کہ اس میں کاربونل گروپ اور ہائیڈروآکسل گروپ ہوتا ہے۔ دونوں گروپ ایک دوسرے پر اس حد تک اثر ڈالتے ہیں کہ کاربوکسلک ایسڈز کی تعامل پذیری ایک طرف کاربونل مرکبات (الڈیہائیڈز اور کیٹونز) اور دوسری طرف الکوحلز سے بہت کم مشابہت رکھتی ہے۔','کاربوکسیلیک ګروپ ځکه دا نوم لري چې کاربونیل ګروپ او هایدروکسیل ګروپ لري. دواړه ګروپونه پر یو بل دومره اغېز کوي چې د کاربوکسیلیک اسیدونو تعامل وړتیا له یوې خوا د کاربونیل مرکباتو (الدیهایډونو او کیټونونو) او له بلې خوا د الکولونو سره ډېر لږ ورته والی لري.')
add('Although the carboxylic acid (and its derivatives) also contain a carbonyl group, but still they do not exhibit the characteristic reactions of aldehydes and ketones. For example, they do not undergo nucleophilic addition reactions and more commonly react by nucleophilic acyl substitution, where one nucleophile replaces another on the acyl (C=O) carbon atom, shown below.','اگرچہ کاربوکسلک ایسڈ (اور اس کے مشتقات) میں بھی کاربونل گروپ ہوتا ہے، پھر بھی یہ الڈیہائیڈز اور کیٹونز کے مخصوص تعاملات ظاہر نہیں کرتے۔ مثلاً یہ نیوکلیوفائلی اضافی تعاملات نہیں کرتے اور زیادہ تر نیوکلیوفائلی ایسائل استبدال سے تعامل کرتے ہیں، جس میں ایسائل (C=O) کاربن ایٹم پر ایک نیوکلیوفائل دوسرے کی جگہ لیتا ہے، جیسا کہ نیچے دکھایا گیا ہے۔','که څه هم کاربوکسیلیک اسید (او مشتقات یې) هم کاربونیل ګروپ لري، خو بیا هم د الدیهایډونو او کیټونونو ځانګړي تعاملونه نه ښيي. د بېلګې په توګه نیوکلیوفایلي اضافي تعاملونه نه کوي او ډېری د نیوکلیوفایلي اسایل بدلون په واسطه تعامل کوي، چې پکې د اسایل (C=O) پر کاربني اټوم یو نیوکلیوفایل د بل ځای نیسي، لکه څنګه چې لاندې ښودل شوي.')
visual('chem12-p132-acyl-substitution',subst)
record=section('20.5','Preparation of carboxylic acids and reactivity','کاربوکسلک ایسڈز کی تیاری اور تعامل پذیری','د کاربوکسیلیک اسیدونو چمتو کول او تعامل وړتیا',paras,layout,blocks,'258–259')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':132,'printedPages':[258,259]}]
record['sourceContinuesOnPdfPage']=133
trim=[{'id':'20.6','startsAt':'ketones, because the carbon atom'}]
if __name__=='__main__':save(132,[record],trim=trim,chapter_number=20)
