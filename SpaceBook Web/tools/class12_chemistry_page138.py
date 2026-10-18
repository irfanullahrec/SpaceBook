"""PDF138 printed270–271: Unit 20 exercise Q2 short answers, Q3 detailed answers, Project."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow138');t=F.t;line=F.line
def ch(x,y,toks,up,size=15):return chain(F,0,y,toks,size,None,up,center=x)
P=[];L=[];blocks=[]
def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
def lines(rows,kind='lines'):
 s0=len(P)
 for r in rows:P.append(pair(*r))
 L.append({'type':kind,'indices':list(range(s0,len(P)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});L.append({'type':'visual','blockId':identity})
def names(lang):
 s=F.start(270)
 s+=t(20,40,'i.',14)+ch(210,60,['HO','—','C','—','CH','—','CH₂','—','C','—','OH'],{2:'=O',4:'CH₃',8:'=O'})
 s+=t(440,40,'ii.',14)+ch(640,60,['H₃C','—','CH₂','—','CH','—','CH₂','—','C','—','OH'],{4:'CH₃',8:'=O'})
 s+=t(20,140,'iii.',14)+ch(210,160,['H₃C','—','CH₂','—','CH','—','CH₂','—','C','—','OC₂H₅'],{4:'CH₃',8:'=O'})
 s+=t(440,140,'iv.',14)+ch(640,160,['H₂C','=','CH','—','CH₂','—','CH₂','—','C','—','NH₂'],{8:'=O'})
 s+=t(20,240,'v.',14)+ch(210,255,['HC','≡','C','—','CH₂','—','CH₂','—','C','—','OH'],{8:'=O'})
 return s+'</svg>'

add('Q2. Write short answers of the following questions.','سوال 2. درج ذیل سوالات کے مختصر جوابات لکھیں۔','پوښتنه 2. د لاندې پوښتنو لنډ ځوابونه ولیکئ.','heading')
lines([('i. Why anhydrous acetic acid is known as glacial acetic acid?','i. بے آب ایسیٹک ایسڈ کو گلیشیل ایسیٹک ایسڈ کیوں کہا جاتا ہے؟','i. بې اوبو اسیټیک اسید ته ولې ګلېشیل اسیټیک اسید وايي؟'),
 ('ii. The boiling points of carboxylic acids are higher than corresponding alcohols. Explain briefly.','ii. کاربوکسلک ایسڈز کے نقطۂ جوش متعلقہ الکوحلز سے زیادہ ہیں۔ مختصراً وضاحت کریں۔','ii. د کاربوکسیلیک اسیدونو د ایشېدو ټکي له اړوندو الکولونو لوړ دي. په لنډه توګه یې تشریح کړئ.'),
 ('iii. How carboxylic acids are stronger acids than phenol, alcohols and water?','iii. کاربوکسلک ایسڈز فینول، الکوحلز اور پانی سے زیادہ طاقتور ایسڈز کیسے ہیں؟','iii. کاربوکسیلیک اسیدونه له فینول، الکولونو او اوبو څنګه قوي اسیدونه دي؟'),
 ('iv. Why methanoic acid is stronger acid than ethanoic acid?','iv. میتھانوئک ایسڈ ایتھانوئک ایسڈ سے زیادہ طاقتور ایسڈ کیوں ہے؟','iv. میتانویک اسید له ایتانویک اسید ولې قوي اسید دی؟'),
 ('v. Chloroacetic acid is a derivative of acetic acid. Why chloroacetic acid is stronger acid than acetic acid?','v. کلورو ایسیٹک ایسڈ ایسیٹک ایسڈ کا مشتق ہے۔ کلورو ایسیٹک ایسڈ ایسیٹک ایسڈ سے زیادہ طاقتور ایسڈ کیوں ہے؟','v. کلورو اسیټیک اسید د اسیټیک اسید مشتق دی. کلورو اسیټیک اسید له اسیټیک اسید ولې قوي اسید دی؟'),
 ('vi. How carboxylic acids can be obtained readily by the oxidation of primary alcohols?','vi. ابتدائی الکوحلز کی تکسید سے کاربوکسلک ایسڈز آسانی سے کیسے حاصل کیے جا سکتے ہیں؟','vi. د لومړنیو الکولونو د اکسیډېشن په واسطه کاربوکسیلیک اسیدونه په اسانۍ څنګه ترلاسه کېدای شي؟'),
 ('vii. Carboxylic acids are less reactive towards nucleophile, compared to aldehydes. Why?','vii. کاربوکسلک ایسڈز الڈیہائیڈز کے مقابلے میں نیوکلیوفائل کی طرف کم تعامل پذیر ہیں۔ کیوں؟','vii. کاربوکسیلیک اسیدونه د الدیهایډونو په پرتله د نیوکلیوفایل په وړاندې لږ تعامل کوونکي دي. ولې؟'),
 ('viii. Why amides are the least reactive derivatives of carboxylic acid, towards nucleophile?','viii. امائیڈز نیوکلیوفائل کی طرف کاربوکسلک ایسڈ کے سب سے کم تعامل پذیر مشتقات کیوں ہیں؟','viii. امایډونه د نیوکلیوفایل په وړاندې د کاربوکسیلیک اسید تر ټولو لږ تعامل کوونکي مشتقات ولې دي؟'),
 ('ix. Esters can be hydrolysed in both acidic and basic conditions. Why base hydrolysis of esters is also called saponification?','ix. ایسٹرز تیزابی اور اساسی دونوں حالات میں ہائیڈرولائز ہو سکتے ہیں۔ ایسٹرز کی اساسی ہائیڈرولائسز کو سیپونیفکیشن بھی کیوں کہتے ہیں؟','ix. ایسټرونه په اسیدي او قلوي دواړو شرایطو کې هایدرولایز کېدای شي. د ایسټرونو قلوي هایدرولایسس ته ولې سپونیفیکېشن هم وايي؟'),
 ('x. Acid halides are the most reactive of all acid derivatives towards nucleophiles. Explain briefly.','x. ایسڈ ہیلائیڈز نیوکلیوفائلز کی طرف تمام ایسڈ مشتقات میں سب سے زیادہ تعامل پذیر ہیں۔ مختصراً وضاحت کریں۔','x. اسید هالایډونه د نیوکلیوفایلونو په وړاندې په ټولو اسید مشتقاتو کې تر ټولو ډېر تعامل کوونکي دي. په لنډه توګه یې تشریح کړئ.')])
add('Q3. Write detail answers of the following questions.','سوال 3. درج ذیل سوالات کے تفصیلی جوابات لکھیں۔','پوښتنه 3. د لاندې پوښتنو مفصل ځوابونه ولیکئ.','heading')
lines([('1. Explain the acidity of carboxylic acids. How their acid strength is affected by electron donating and withdrawing substitutions?','1. کاربوکسلک ایسڈز کی تیزابیت کی وضاحت کریں۔ الیکٹران دینے اور کھینچنے والے متبادلات سے ان کی تیزابی طاقت کیسے متاثر ہوتی ہے؟','1. د کاربوکسیلیک اسیدونو تېزابیت تشریح کړئ. د الکترون ورکوونکو او راکښونکو بدیلونو په واسطه د هغوی تېزابي قوت څنګه اغېزمن کېږي؟'),
 ('2. How will you prepare acetic acid by using?','2. آپ درج ذیل کو استعمال کر کے ایسیٹک ایسڈ کیسے تیار کریں گے؟','2. تاسو د لاندې په کارولو اسیټیک اسید څنګه چمتو کوئ؟'),
 ('i. a nitrile   ii. a Grignard reagent   iii. an alcohol   iv. an aldehyde   v. an acid halide','i. نائٹرائل   ii. گرینیارڈ عامل   iii. الکوحل   iv. الڈیہائیڈ   v. ایسڈ ہیلائیڈ','i. نایټرایل   ii. ګرینیارډ عامل   iii. الکول   iv. الدیهاید   v. اسید هالاید'),
 ('3. Starting from acetic acid, how will you prepare each of the following?','3. ایسیٹک ایسڈ سے شروع کر کے آپ درج ذیل میں سے ہر ایک کیسے تیار کریں گے؟','3. له اسیټیک اسید څخه په پیل، تاسو لاندې هر یو څنګه چمتو کوئ؟'),
 ('i. acetyl chloride   ii. acetic anhydride   iii. acetamide   iv. ethyl acetate   v. ethyl alcohol','i. ایسیٹائل کلورائیڈ   ii. ایسیٹک این ہائیڈرائیڈ   iii. ایسیٹامائیڈ   iv. ایتھائل ایسیٹیٹ   v. ایتھائل الکوحل','i. اسیټیل کلوراید   ii. اسیټیک انهایدراید   iii. اسیټامایډ   iv. ایتیل اسیټېټ   v. ایتیل الکول'),
 ('4. Write an equation for:','4. درج ذیل کے لیے مساوات لکھیں:','4. د لاندې لپاره معادله ولیکئ:'),
 ('i. Hydrolysis of acetyl chloride   ii. Reaction of benzoyl chloride with methanol.   iii. Esterification of butan-1-ol with acetic anhydride.   iv. Ammonolysis of butanoyl chloride.   v. Fischer esterfication of pentanoic acid with ethanol.','i. ایسیٹائل کلورائیڈ کی ہائیڈرولائسز   ii. میتھانول کے ساتھ بینزوائل کلورائیڈ کا تعامل۔   iii. ایسیٹک این ہائیڈرائیڈ کے ساتھ بیوٹین-1-اول کی ایسٹریفکیشن۔   iv. بیوٹانوائل کلورائیڈ کی امونولائسز۔   v. ایتھانول کے ساتھ پینٹانوئک ایسڈ کی فشر ایسٹریفکیشن۔','i. د اسیټیل کلوراید هایدرولایسس   ii. له میتانول سره د بنزویل کلوراید تعامل.   iii. له اسیټیک انهایدراید سره د بیوټان-1-ول ایسټریفیکېشن.   iv. د بیوټانویل کلوراید امونولایسس.   v. له ایتانول سره د پېنټانویک اسید فیشر ایسټریفیکېشن.'),
 ('5. (a) Describe three methods for preparation of carboxylic acids.','5. (a) کاربوکسلک ایسڈز کی تیاری کے تین طریقے بیان کریں۔','5. (a) د کاربوکسیلیک اسیدونو د چمتو کولو درې طریقې بیان کړئ.'),
 ('(b) Write the systematic names for the following organic compounds;','(b) درج ذیل نامیاتی مرکبات کے منظم نام لکھیں؛','(b) د لاندې عضوي مرکباتو سیستماتیک نومونه ولیکئ؛')])
visual('chem12-p138-q5b-structures',names)
lines([('(c) Draw the structural formula of the following organic compounds;','(c) درج ذیل نامیاتی مرکبات کے ساختی فارمولے بنائیں؛','(c) د لاندې عضوي مرکباتو جوړښتي فورمولونه رسم کړئ؛'),
 ('i. 3-ethyl-4-methylpentanoic acid   ii. ethyl 3-methylbutanoate   iii. 2-chloropropanoyl bromide   iv. ethanoic propanoic anhydride   v. 3,3-dimethylbutanenitrile','i. 3-ایتھائل-4-میتھائل پینٹانوئک ایسڈ   ii. ایتھائل 3-میتھائل بیوٹانوایٹ   iii. 2-کلورو پروپانوائل برومائیڈ   iv. ایتھانوئک پروپانوئک این ہائیڈرائیڈ   v. 3،3-ڈائی میتھائل بیوٹین نائٹرائل','i. 3-ایتیل-4-میتایل پېنټانویک اسید   ii. ایتیل 3-میتایل بیوټانوېټ   iii. 2-کلورو پروپانویل بروماید   iv. ایتانویک پروپانویک انهایدراید   v. 3،3-ډای میتایل بیوټان نایټرایل'),
 ('(d) Complete the following reactions.','(d) درج ذیل تعاملات مکمل کریں۔','(d) لاندې تعاملونه بشپړ کړئ.'),
 ('i. CH₃CH₂CH₂COOH + PCl₅ ⟶','i. CH₃CH₂CH₂COOH + PCl₅ ⟶','i. CH₃CH₂CH₂COOH + PCl₅ ⟶'),
 ('ii. CH₃CH₂COOH + SOCl₂ ⟶','ii. CH₃CH₂COOH + SOCl₂ ⟶','ii. CH₃CH₂COOH + SOCl₂ ⟶'),
 ('iii. CH₃CH₂CONH₂ + LiAlH₄ ⟶','iii. CH₃CH₂CONH₂ + LiAlH₄ ⟶','iii. CH₃CH₂CONH₂ + LiAlH₄ ⟶'),
 ('iv. CH₃COOCOCH₃ + NH₃ ⟶','iv. CH₃COOCOCH₃ + NH₃ ⟶','iv. CH₃COOCOCH₃ + NH₃ ⟶'),
 ('v. CH₃CH₂COOCH₃ + NaOH ⟶','v. CH₃CH₂COOCH₃ + NaOH ⟶','v. CH₃CH₂COOCH₃ + NaOH ⟶'),
 ('vi. CH₃CH₂COONa + NaOH —CaO⟶','vi. CH₃CH₂COONa + NaOH —CaO⟶','vi. CH₃CH₂COONa + NaOH —CaO⟶'),
 ('vii. CH₃CH₂COOC₂H₅ + LiAlH₄ ⟶','vii. CH₃CH₂COOC₂H₅ + LiAlH₄ ⟶','vii. CH₃CH₂COOC₂H₅ + LiAlH₄ ⟶'),
 ('viii. CH₃CH₂MgBr + CH₃CH₂CN ⟶','viii. CH₃CH₂MgBr + CH₃CH₂CN ⟶','viii. CH₃CH₂MgBr + CH₃CH₂CN ⟶')])
add('Project','پروجیکٹ','پروژه','heading')
add('Add few drops or a small crystal of available carboxylic acid with about 2-3 mL of aq. NaHCO₃ and shake well. Formation of bubbles of carbon dioxide is positive test, for presence of carboxylic acid.','دستیاب کاربوکسلک ایسڈ کے چند قطرے یا ایک چھوٹا قلم تقریباً 2-3 mL آبی NaHCO₃ میں ڈالیں اور اچھی طرح ہلائیں۔ کاربن ڈائی آکسائیڈ کے بلبلوں کا بننا کاربوکسلک ایسڈ کی موجودگی کا مثبت ٹیسٹ ہے۔','د موجود کاربوکسیلیک اسید څو څاڅکي یا یو کوچنی قلم له نږدې 2-3 mL اوبلن NaHCO₃ سره ګډ کړئ او ښه یې وښورئ. د کاربن ډای اکساید د بلبلو جوړېدل د کاربوکسیلیک اسید د شتون مثبت ازموینه ده.')
r12=section('20.12','Unit 20 exercise: short and detailed questions, Project','یونٹ 20 مشق: مختصر اور تفصیلی سوالات، پروجیکٹ','د 20 واحد تمرین: لنډې او مفصلې پوښتنې، پروژه',P,L,blocks,'270–271')
r12['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':138,'printedPages':[270,271]}]
if __name__=='__main__':save(138,[r12],chapter_number=20)
