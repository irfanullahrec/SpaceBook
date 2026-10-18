"""PDF136 printed266–267: Table 20.5 interconversion of acid derivatives, self-assessment, Society Technology and Science."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow136');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'Acid derivative':('ایسڈ مشتق','اسید مشتق'),'Reaction of acid derivatives with':('ایسڈ مشتقات کا تعامل','د اسید مشتقاتو تعامل له'),'(Hydrolysis)':('(ہائیڈرولائسز)','(هایدرولایسس)'),'(Alcoholysis)':('(الکوحلائسز)','(الکولایسس)'),'(Ammonolysis)':('(امونولائسز)','(امونولایسس)'),
   'acid halide':('ایسڈ ہیلائیڈ','اسید هالاید'),'anhydride':('این ہائیڈرائیڈ','انهایدراید'),'ester':('ایسٹر','ایسټر'),'amide':('امائیڈ','امایډ'),'nitrile':('نائٹرائل','نایټرایل'),
   'carboxylic acid':('کاربوکسلک ایسڈ','کاربوکسیلیک اسید'),'alcohol':('الکوحل','الکول')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def acyl(x,y,left,right,size=13):
 """R–C(=O)–Z drawn compactly with C at x."""
 return t(x-8-6.5*len(left),y,left+'—',size)+t(x,y,'C',size)+t(x+8+6.5*len(right),y,'—'+right,size)+line(x-2,y-12,x-2,y-24,1.4)+line(x+2,y-12,x+2,y-24,1.4)+t(x,y-28,'O',11)
def table(lang):
 cols=[0,150,330,560,850];rows=[0,40,82,152,222,292,362,432]
 s=F.start(432)+f'<rect x="1" y="1" width="848" height="430" fill="none" stroke="#222" stroke-width="1.5"/>'
 for y in rows[2:-1]:s+=line(0,y,850,y,1)
 s+=line(150,40,850,40,1)
 for x in cols[1:-1]:s+=line(x,40 if x>150 else 0,x,432,1)
 s+=t(75,46,lb(lang,'Acid derivative'),13)+t(500,26,lb(lang,'Reaction of acid derivatives with'),13)
 for (a,b),x in zip((('H₂O','(Hydrolysis)'),("R′OH",'(Alcoholysis)'),('NH₃','(Ammonolysis)')),(240,445,705)):s+=t(x,58,a,13)+t(x,74,lb(lang,b),12)
 L=lambda x,y,v:t(x,y,lb(lang,v),11)
 # acid halide
 y=125;s+=acyl(75,y,'R','Cl')+L(75,y+18,'acid halide')+acyl(220,y,'R','OH')+t(285,y,'+ HCl',12)+L(220,y+18,'carboxylic acid')
 s+=acyl(420,y,'R',"OR′")+t(490,y,'+ HCl',12)+L(420,y+18,'ester')+acyl(680,y,'R','NH₂')+t(752,y,'+ HCl',12)+L(680,y+18,'amide')
 # anhydride
 y=195;s+=t(75,y,'R—C—O—C—R',12)+line(53,y-12,53,y-24,1.2)+line(57,y-12,57,y-24,1.2)+t(55,y-28,'O',10)+line(93,y-12,93,y-24,1.2)+line(97,y-12,97,y-24,1.2)+t(95,y-28,'O',10)+L(75,y+18,'anhydride')
 s+=t(190,y,'2',13)+acyl(240,y,'R','OH')+L(240,y+18,'carboxylic acid')
 s+=acyl(385,y,'R',"OR′")+t(442,y,'+',12)+acyl(490,y,'R','OH')+L(385,y+18,'ester')+L(490,y+18,'carboxylic acid')
 s+=acyl(625,y,'R','NH₂')+t(678,y,'+',12)+acyl(730,y,'R','OH')+L(625,y+18,'amide')+L(730,y+18,'carboxylic acid')
 # ester
 y=265;s+=acyl(75,y,'R','OR')+L(75,y+18,'ester')+acyl(210,y,'R','OH')+t(290,y,'+ ROH',12)+L(210,y+18,'carboxylic acid')+L(290,y+18,'alcohol')
 s+=acyl(410,y,'R',"OR′")+t(500,y,'+ ROH',12)+L(410,y+18,'ester')+L(500,y+18,'alcohol')+acyl(660,y,'R','NH₂')+t(750,y,'+ ROH',12)+L(660,y+18,'amide')+L(750,y+18,'alcohol')
 # amide
 y=342;s+=acyl(75,y,'R','NH₂')+L(75,y+16,'amide')+acyl(220,y,'R','OH')+t(290,y,'+ NH₃',12)+L(220,y+16,'carboxylic acid')+t(445,y-6,'---',13)+t(705,y-6,'---',13)
 # nitrile
 y=410;s+=t(75,y,'R—C≡N',13)+L(75,y+16,'nitrile')+acyl(220,y,'R','OH')+t(290,y,'+ NH₃',12)+L(220,y+16,'carboxylic acid')+t(445,y-6,'---',13)+t(705,y-6,'---',13)
 return s+'</svg>'

add('… halides, acid anhydride, ester, amide or nitrile. Similarly alcoholysis gives an ester and ammonolysis gives an amide. All of the reactions in Table 20.5 take place via attack of the nucleophile on the carbonyl carbon of the acid derivative, commonly called nucleophilic acyl substitution.','… ہیلائیڈز، ایسڈ این ہائیڈرائیڈ، ایسٹر، امائیڈ یا نائٹرائل سے شروع کریں۔ اسی طرح الکوحلائسز ایسٹر اور امونولائسز امائیڈ دیتی ہے۔ جدول 20.5 کے تمام تعاملات ایسڈ مشتق کے کاربونل کاربن پر نیوکلیوفائل کے حملے سے ہوتے ہیں، جسے عموماً نیوکلیوفائلی ایسائل استبدال کہتے ہیں۔','… هالایډونو، اسید انهایدراید، ایسټر، امایډ یا نایټرایل څخه پیل وکړو. همدارنګه الکولایسس ایسټر او امونولایسس امایډ ورکوي. د جدول 20.5 ټول تعاملونه د اسید مشتق پر کاربونیل کاربن د نیوکلیوفایل د برید له لارې ترسره کېږي، چې عموماً نیوکلیوفایلي اسایل بدلون بلل کېږي.')
add('Table 20.5 Reactions of Acid Derivatives with certain Derivatives Nucleophile','جدول 20.5 بعض نیوکلیوفائلز کے ساتھ ایسڈ مشتقات کے تعاملات','جدول 20.5 له ځینو نیوکلیوفایلونو سره د اسید مشتقاتو تعاملونه')
visual('chem12-table20-5',table)
add('Self-assessment','خود جائزہ','ځان ارزونه','heading')
add('Write the common and IUPAC names of derivatives of carboxylic acids, which yield acetic acid upon hydrolysis.','کاربوکسلک ایسڈز کے ان مشتقات کے عام اور IUPAC نام لکھیں جو ہائیڈرولائسز پر ایسیٹک ایسڈ دیتے ہیں۔','د کاربوکسیلیک اسیدونو د هغو مشتقاتو عام او IUPAC نومونه ولیکئ چې د هایدرولایسس پر مهال اسیټیک اسید ورکوي.','list')
add('Society, Technology And Science','معاشرہ، ٹیکنالوجی اور سائنس','ټولنه، ټکنالوژي او ساینس','heading')
add('Some of the most common organic acids in food are found within fruits. Many people are already aware that citric acid occurs in citrus fruits such as oranges, lemons and limes, but there are lesser known acids in fruits that you may not have heard of. These include malic acid, which is found in apples and tartaric acid found in grapes. These acids provide these fruits with that distinctive sharp taste. The mixture of acid and sugar is what gives fruits their unique flavor, so foods will often be deliberately fermented in particular acids to retain or increase the flavor.',
 'خوراک میں پائے جانے والے سب سے عام نامیاتی ایسڈز میں سے کچھ پھلوں میں ہوتے ہیں۔ بہت سے لوگ پہلے سے جانتے ہیں کہ سٹرک ایسڈ ترشاوہ پھلوں جیسے مالٹوں، لیموں اور لائم میں ہوتا ہے، لیکن پھلوں میں کم معروف ایسڈز بھی ہیں جن کا آپ نے شاید نہ سنا ہو۔ ان میں میلک ایسڈ شامل ہے جو سیب میں اور ٹارٹرک ایسڈ جو انگور میں پایا جاتا ہے۔ یہ ایسڈز ان پھلوں کو مخصوص ترش ذائقہ دیتے ہیں۔ ایسڈ اور شکر کا آمیزہ ہی پھلوں کو ان کا منفرد ذائقہ دیتا ہے، اس لیے ذائقہ برقرار رکھنے یا بڑھانے کے لیے خوراک کو اکثر جان بوجھ کر مخصوص ایسڈز میں خمیر کیا جاتا ہے۔',
 'په خوړو کې یو شمېر تر ټولو عام عضوي اسیدونه په مېوو کې موندل کېږي. ډېر خلک دمخه پوهېږي چې سیټریک اسید په ترشو مېوو لکه مالټو، لیمو او لایمونو کې شته، خو په مېوو کې لږ پېژندل شوي اسیدونه هم شته چې ښايي تاسو یې نه وي اورېدلي. په دې کې مالیک اسید چې په مڼو کې او ټارټریک اسید چې په انګورو کې موندل کېږي شامل دي. دا اسیدونه دغو مېوو ته هغه ځانګړی تېز خوند ورکوي. د اسید او بورې ګډوله مېوو ته ځانګړی خوند ورکوي، نو د خوند د ساتلو یا زیاتولو لپاره خواړه ډېری په قصدي ډول په ځانګړو اسیدونو کې تخمیر کېږي.')
add('In addition to taste, acids in fruits are also used as preservatives due to their ability to reduce the onset of bacterial degradation. High acidity helps to kill bacteria so food doesn\'t spoil as quickly e.g. Benzoic acid and sodium benzoate have inhibitory effect on growth of fungi; major cause of food spoilage.',
 'ذائقے کے علاوہ پھلوں کے ایسڈز بیکٹیریائی خرابی کے آغاز کو کم کرنے کی صلاحیت کی وجہ سے محافظ کے طور پر بھی استعمال ہوتے ہیں۔ زیادہ تیزابیت بیکٹیریا کو مارنے میں مدد دیتی ہے تاکہ خوراک جلدی خراب نہ ہو، مثلاً بینزوئک ایسڈ اور سوڈیم بینزوئیٹ پھپھوندی کی افزائش پر روک لگاتے ہیں؛ جو خوراک کی خرابی کی بڑی وجہ ہے۔',
 'د خوند سربېره، د مېوو اسیدونه د باکتریايي خرابېدو د پیل د کمولو د وړتیا له امله د ساتونکو په توګه هم کارېږي. لوړ تېزابیت د باکتریاوو په وژلو کې مرسته کوي څو خواړه ژر خراب نه شي، لکه بنزویک اسید او سوډیم بنزوېټ د پوڅکو پر ودې مخنیوونکی اغېز لري؛ چې د خوړو د خرابېدو لوی لامل دی.')
add('Many of the acids present in vegetables are also present in fruits. The key difference is that vegetables do not tend to be as acidic in their makeup, making them a potentially safer source of key acids if you struggle with acid reflux or high stomach acidity. Vegetables include citric acid, oxalic acid and benzoic acid. Oxalic acid is a naturally occurring acid found in a wide range of vegetables. Oxalates are known for binding to almost any mineral in the body. Oxalates build up insoluble compounds when binds with calcium, that can lead to kidney stones if precautions aren\'t taken. The principal acids found in dairy products are benzoic acid, lactic acid and a variety of fatty acids which contribute to dairy products.',
 'سبزیوں میں موجود بہت سے ایسڈز پھلوں میں بھی ہوتے ہیں۔ اہم فرق یہ ہے کہ سبزیاں اپنی ساخت میں اتنی تیزابی نہیں ہوتیں، اس لیے اگر آپ کو تیزابیت کی واپسی یا معدے کی زیادہ تیزابیت کا مسئلہ ہو تو یہ اہم ایسڈز کا ممکنہ طور پر زیادہ محفوظ ذریعہ ہیں۔ سبزیوں میں سٹرک ایسڈ، آگزیلک ایسڈ اور بینزوئک ایسڈ ہوتے ہیں۔ آگزیلک ایسڈ قدرتی طور پر پایا جانے والا ایسڈ ہے جو بہت سی سبزیوں میں ہوتا ہے۔ آگزیلیٹس جسم میں تقریباً ہر معدن سے جڑنے کے لیے مشہور ہیں۔ کیلشیم سے جڑ کر آگزیلیٹس ناحل پذیر مرکبات بناتے ہیں، جو احتیاط نہ کرنے پر گردے کی پتھری کا باعث بن سکتے ہیں۔ ڈیری مصنوعات میں پائے جانے والے بنیادی ایسڈز بینزوئک ایسڈ، لیکٹک ایسڈ اور مختلف فیٹی ایسڈز ہیں جو ڈیری مصنوعات میں حصہ ڈالتے ہیں۔',
 'په سبزیو کې شته ډېر اسیدونه په مېوو کې هم شته. اصلي توپیر دا دی چې سبزۍ په خپل جوړښت کې دومره تېزابي نه وي، نو که تاسو د تېزاب د بېرته راتګ یا د معدې د لوړ تېزابیت ستونزه لرئ، دا د مهمو اسیدونو یوه احتمالاً خوندي سرچینه ده. په سبزیو کې سیټریک اسید، اګزالیک اسید او بنزویک اسید شته. اګزالیک اسید په طبیعي ډول موندل کېدونکی اسید دی چې په ډېرو سبزیو کې شته. اګزالېټونه په بدن کې له نږدې هر منرال سره د تړلو لپاره پېژندل کېږي. اګزالېټونه له کلسیم سره په تړلو نه حلېدونکي مرکبات جوړوي، چې که احتیاط ونه شي د پښتورګو د تیږو لامل کېدای شي. په لبنیاتو کې موندل شوي اصلي اسیدونه بنزویک اسید، لاکټیک اسید او بېلابېل غوړ اسیدونه دي چې لبنیاتو کې ونډه لري.')
record=section('20.9','Table 20.5 and Society, Technology and Science','جدول 20.5 اور معاشرہ، ٹیکنالوجی اور سائنس','جدول 20.5 او ټولنه، ټکنالوژي او ساینس',paras,layout,blocks,'266–267')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':136,'printedPages':[266,267]}]
record['sourceContinuesOnPdfPage']=137
trim=[{'id':'20.10','startsAt':'Key Points'}]
if __name__=='__main__':save(136,[record],trim=trim,chapter_number=20)
