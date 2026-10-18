"""PDF31 printed54–55: alloy table and coordination-compound terminology."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def head(e,u,p):add(e,u,p,'heading')
def eq(v):add(v,v,v,'equation')
add('Table 14.4 Important Alloys and Their Uses','جدول 14.4 اہم مخلوط دھاتیں اور ان کے استعمال','جدول 14.4 مهم الیاژونه او د هغوی کارونې')
names=['Brass','Bronze','German Silver','Rolled Gold','Gun Metal','Duralumin','Solder','Bell metal','Stainless steel','Nickel steel'];ur=['پیتل','کانسی','جرمن سلور','رولڈ گولڈ','گن میٹل','ڈیورالومِن','سولڈر','بیل میٹل','اسٹین لیس اسٹیل','نکل اسٹیل'];ps=['ژېړ مس','برونز','جرمني سپین زر','رولډ ګولډ','ګن مېټل','ډیورالومین','سولډر','بېل مېټل','زنګ نه وهونکی فولاد','نیکل فولاد']
compositions=['Cu + Zn','Cu + Sn','Cu + Zn + Ni','Cu + Al','Cu + Sn + Zn + Pb','Al + Cu + Mg + Mn','Pb + Sn','Cu + Sn','Fe + Cr + Ni + C','Fe + Ni']
uses=[('In making utensils.','برتن بنانے میں۔','د لوښو په جوړولو کې.'),('In making coins, bell and utensils.','سکے، گھنٹی اور برتن بنانے میں۔','د سکو، زنګ او لوښو په جوړولو کې.'),('In making utensils.','برتن بنانے میں۔','د لوښو په جوړولو کې.'),('In making cheap ornaments.','سستے زیورات بنانے میں۔','د ارزانه ګاڼو په جوړولو کې.'),('In making guns, barrels, gears and bearings.','بندوقیں، نالیاں، گیئر اور بیئرنگ بنانے میں۔','د ټوپکونو، نلونو، ګیرونو او بېیرنګونو په جوړولو کې.'),('For making utensils.','برتن بنانے کے لیے۔','د لوښو د جوړولو لپاره.'),('For soldering.','سولڈر کرنے کے لیے۔','د سولډر کولو لپاره.'),('For casting bells and statues.','گھنٹیاں اور مجسمے ڈھالنے کے لیے۔','د زنګونو او مجسمو د اچولو لپاره.'),('For making utensils and surgical cutlery.','برتن اور جراحی کے اوزار بنانے کے لیے۔','د لوښو او جراحي وسایلو د جوړولو لپاره.'),('For making electrical wire, automobile parts.','برقی تار اور گاڑیوں کے پرزے بنانے کے لیے۔','د برېښنايي تارونو او د موټرو د پرزو د جوړولو لپاره.')]
rows=[[names[i],compositions[i],uses[i][0]] for i in range(10)]
blocks.append({'id':'chem12-table-14-4','headers':['Alloys','Compositions','Uses'],'rows':rows,'translations':[{'language':'اردو','headers':['مخلوط دھاتیں','ترکیبیں','استعمال'],'rows':[[ur[i],compositions[i],uses[i][1]] for i in range(10)]},{'language':'پښتو','headers':['الیاژونه','ترکیبونه','کارونې'],'rows':[[ps[i],compositions[i],uses[i][2]] for i in range(10)]}]});layout.append({'type':'sourceDataTable','tableId':blocks[-1]['id']})
head('14.2 Coordination Compounds','14.2 تناسقی مرکبات','14.2 کواردینېشن مرکبات')
add('Coordination compounds are those compounds in which a central atom or ion is attached with a fixed number of groups or molecules (ligands) through coordinate covalent bonds.',
    'تناسقی مرکبات وہ ہیں جن میں مرکزی ایٹم یا آئن، گروپوں یا سالموں (لیگنڈز) کی مقررہ تعداد کے ساتھ تناسقی اشتراکی بندوں سے جڑا ہو۔',
    'کواردینېشن مرکبات هغه دي چې پکې مرکزي اټوم یا ایون د ډلو یا مالیکولونو (لېګنډونو) له ټاکلي شمېر سره د کواردینېټ کووالنټ تړونونو له لارې تړلی وي.')
add('These compounds can be divided into two classes depending on their behaviour in aqueous solution.',
    'آبی محلول میں رویے کے مطابق ان مرکبات کو دو قسموں میں تقسیم کیا جا سکتا ہے۔',
    'دا مرکبات په اوبلن محلول کې د خپل چلند له مخې په دوو ډلو وېشل کېدای شي.')
head('1. Those which Lose their Identity in Solution i.e. Double Salts','1. محلول میں اپنی شناخت کھونے والے، یعنی دوہرے نمک','1. هغه چې په محلول کې خپل هویت له لاسه ورکوي، یعنې دوه ګونې مالګې')
add('These compounds exist as stable compounds only in the solid crystalline state and break up into constituent units in aqueous solution. For example, when crystals of potash alum are dissolved in water, Al³⁺, K⁺ and SO₄²⁻ ions are produced. This aqueous solution shows the same physical and chemical properties as a mixture of aqueous solution of aluminium sulphate and potassium sulphate. Some examples of double salts are,',
    'یہ صرف ٹھوس قلمی حالت میں مستحکم مرکبات ہوتے ہیں اور آبی محلول میں اپنے اجزا میں بٹ جاتے ہیں۔ مثلاً پوٹاش پھٹکری کے قلم پانی میں حل ہونے پر Al³⁺، K⁺ اور SO₄²⁻ آئن بناتے ہیں۔ یہ محلول ایلومینیم سلفیٹ اور پوٹاشیم سلفیٹ کے آبی محلولوں کے آمیزے جیسی طبعی اور کیمیائی خصوصیات دکھاتا ہے۔ دوہرے نمکوں کی بعض مثالیں ہیں:',
    'دا یوازې په جامد بلوري حالت کې د ثابتو مرکباتو په توګه وي او په اوبلن محلول کې په جوړوونکو واحدونو جلا کېږي. د بېلګې په توګه د پوټاش الم د بلورونو په اوبو کې حل کېدو سره Al³⁺، K⁺ او SO₄²⁻ ایونونه جوړېږي. دا محلول د المونیم سلفېټ او پوټاشیم سلفېټ د اوبلنو محلولونو د مخلوط په څېر فزیکي او کیمیاوي ځانګړنې ښيي. د دوه ګونو مالګو ځینې بېلګې دا دي:')
add('Mohr’s salt:','موہر کا نمک:','د موهر مالګه:');eq('FeSO₄.(NH₄)₂SO₄.6H₂O')
add('Potash alum:','پوٹاش پھٹکری:','پوټاش الم:');eq('Al₂(SO₄)₃.K₂SO₄.24H₂O')
add('These compounds lose their identity in the solution.','یہ مرکبات محلول میں اپنی شناخت کھو دیتے ہیں۔','دا مرکبات په محلول کې خپل هویت له لاسه ورکوي.')
head('2. Coordination or Complex Compounds','2. تناسقی یا کمپلیکس مرکبات','2. کواردینېشن یا کمپلېکس مرکبات')
add('These compounds exist as a stable compounds in the solid state and retain their identity in the solution. For example, when potassium ferrocyanide is dissolved in water, the aqueous solution does not show the characteristic test of Fe²⁺ and CN⁻ ions. The physical and chemical properties of the aqueous solution is entirely different from those of free Fe²⁺ and CN⁻ ions.',
    'یہ ٹھوس حالت میں مستحکم مرکبات ہیں اور محلول میں اپنی شناخت برقرار رکھتے ہیں۔ مثلاً پوٹاشیم فیروسائنائیڈ پانی میں حل ہونے پر محلول Fe²⁺ اور CN⁻ آئنوں کی مخصوص جانچ نہیں دکھاتا۔ محلول کی طبعی اور کیمیائی خصوصیات آزاد Fe²⁺ اور CN⁻ آئنوں سے بالکل مختلف ہیں۔',
    'دا په جامد حالت کې ثابت مرکبات دي او په محلول کې خپل هویت ساتي. د بېلګې په توګه د پوټاشیم فېروسیانایډ په اوبو کې حل کېدو سره اوبلن محلول د Fe²⁺ او CN⁻ ایونونو ځانګړې ازموینه نه ښيي. د محلول فزیکي او کیمیاوي ځانګړنې له آزادو Fe²⁺ او CN⁻ ایونونو څخه بشپړ توپیر لري.')
add('In coordination compounds, a central metal atom or ion is bonded to the surrounding electron-pair donors called ligands, through a coordinate bond. These compounds are also known as metal complexes because of the presence of complex metal ions. Some common examples of coordination compounds are,',
    'تناسقی مرکبات میں مرکزی دھاتی ایٹم یا آئن، گرد موجود الیکٹرون جوڑا دینے والے لیگنڈز سے تناسقی بند کے ذریعے جڑا ہے۔ کمپلیکس دھاتی آئنوں کی موجودگی کی وجہ سے یہ دھاتی کمپلیکس بھی کہلاتے ہیں۔ بعض عام مثالیں ہیں:',
    'په کواردینېشن مرکباتو کې مرکزي فلزي اټوم یا ایون د کواردینېټ تړون له لارې له شاوخوا الکترون جوړه ورکوونکو، چې لېګنډونه بلل کېږي، سره تړلی وي. د کمپلېکس فلزي ایونونو د شتون له امله دا فلزي کمپلېکسونه هم بلل کېږي. ځینې عامې بېلګې یې دا دي:')
add('Potassium ferrocyanide','پوٹاشیم فیروسائنائیڈ','پوټاشیم فېروسیانایډ');eq('K₄[Fe(CN)₆]')
add('Sodium nitroprusside','سوڈیم نائٹروپروسائیڈ','سوډیم نایټروپروسایډ');eq('Na₂[Fe(CN)₅NO].2H₂O')
head('Terminology Used in Coordination Compounds','تناسقی مرکبات میں استعمال ہونے والی اصطلاحات','په کواردینېشن مرکباتو کې کارېدونکې اصطلاحګانې')
head('14.2.1 Complex Ion','14.2.1 کمپلیکس آئن','14.2.1 کمپلېکس ایون')
head('1. Complex Ion','1. کمپلیکس آئن','1. کمپلېکس ایون')
add('A complex ion as a positively or negatively charged species containing a central metallic atom or ion surrounded by a suitable number of ligands.',
    'کمپلیکس آئن مثبت یا منفی بار والی نوع ہے، جس میں مرکزی دھاتی ایٹم یا آئن کے گرد لیگنڈز کی مناسب تعداد ہوتی ہے۔',
    'کمپلېکس ایون مثبت یا منفي چارج لرونکی ډول دی چې مرکزي فلزي اټوم یا ایون لري او شاوخوا یې د لېګنډونو مناسب شمېر وي.')
add('For example, when the aqueous solutions of Fe(CN)₂ and KCN are mixed together and evaporated a new compound is obtained. When the compound is dissolved in aqueous solution, it does not ionize as Fe²⁺ and CN⁻ ions but ionizes as K⁺ ion and [Fe(CN)₆]⁴⁻ ion (Ferrocyanide ion). On this basis it has been given a formula K₄[Fe(CN)₆]',
    'مثلاً Fe(CN)₂ اور KCN کے آبی محلول ملا کر تبخیر کرنے سے نیا مرکب حاصل ہوتا ہے۔ یہ آبی محلول میں حل ہونے پر Fe²⁺ اور CN⁻ آئنوں کی صورت میں آئنائز نہیں ہوتا، بلکہ K⁺ اور [Fe(CN)₆]⁴⁻ آئن (فیروسائنائیڈ آئن) بناتا ہے۔ اس بنیاد پر اس کا فارمولا K₄[Fe(CN)₆] ہے۔',
    'د بېلګې په توګه د Fe(CN)₂ او KCN اوبلن محلولونه په ګډولو او تبخیرولو یو نوی مرکب ترلاسه کېږي. کله چې مرکب په اوبلن محلول کې حل شي، د Fe²⁺ او CN⁻ ایونونو په بڼه نه ایوني کېږي، بلکې K⁺ او [Fe(CN)₆]⁴⁻ ایون (فېروسیانایډ ایون) جوړوي. له همدې امله فورمول یې K₄[Fe(CN)₆] ورکړل شوی دی.')
eq('Fe(CN)₂ + 4KCN → K₄[Fe(CN)₆]');eq('K₄[Fe(CN)₆] —Ionization→ 4K⁺ + [Fe(CN)₆]⁴⁻')
paras[-1]['urdu']='K₄[Fe(CN)₆] —آئنائزیشن→ 4K⁺ + [Fe(CN)₆]⁴⁻';paras[-1]['pashto']='K₄[Fe(CN)₆] —ایون کېدل→ 4K⁺ + [Fe(CN)₆]⁴⁻'
add('Here [Fe(CN)₆]⁴⁻ is called a complex ion. In the complex compound K₄[Fe(CN)₆], the complex ion is present consisting of the central iron ion, Fe²⁺, surrounded by six CN⁻ ions acting as ligands.',
    'یہاں [Fe(CN)₆]⁴⁻ کمپلیکس آئن ہے۔ K₄[Fe(CN)₆] میں کمپلیکس آئن مرکزی لوہے کے آئن Fe²⁺ پر مشتمل ہے، جس کے گرد چھ CN⁻ آئن لیگنڈز کے طور پر ہیں۔',
    'دلته [Fe(CN)₆]⁴⁻ کمپلېکس ایون بلل کېږي. په K₄[Fe(CN)₆] کې کمپلېکس ایون له مرکزي اوسپنې ایون Fe²⁺ څخه جوړ دی، چې شاوخوا یې شپږ CN⁻ ایونونه د لېګنډونو په توګه دي.')
head('2. Central Metal Atom or Ion','2. مرکزی دھاتی ایٹم یا آئن','2. مرکزي فلزي اټوم یا ایون')
add('Every complex ion contains a metal atom or ion to which one or more neutral molecules or ions are attached. This is known as the central metal atom or ion. For example, K₄[Fe(CN)₆], [Ag(NH₃)₂]Cl. In these examples, Fe²⁺ and Ag⁺ are the central metal ions.',
    'ہر کمپلیکس آئن میں دھاتی ایٹم یا آئن ہوتا ہے، جس سے ایک یا زیادہ بے بار سالمے یا آئن جڑے ہوتے ہیں۔ اسے مرکزی دھاتی ایٹم یا آئن کہتے ہیں۔ مثلاً K₄[Fe(CN)₆] اور [Ag(NH₃)₂]Cl میں Fe²⁺ اور Ag⁺ مرکزی دھاتی آئن ہیں۔',
    'هر کمپلېکس ایون فلزي اټوم یا ایون لري، چې یو یا ډېر خنثی مالیکولونه یا ایونونه ورسره تړلي دي. دا مرکزي فلزي اټوم یا ایون بلل کېږي. د بېلګې په توګه په K₄[Fe(CN)₆] او [Ag(NH₃)₂]Cl کې Fe²⁺ او Ag⁺ مرکزي فلزي ایونونه دي.')
record=section('14.6','Alloy uses and coordination compounds','مخلوط دھاتوں کے استعمال اور تناسقی مرکبات','د الیاژونو کارونې او کواردینېشن مرکبات',paras,layout,blocks,'54–55');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':31,'printedPages':[54,55]}]
if __name__=='__main__':save(31,[record],trim=[{'id':'14.7','startsAt':'3. Ligand'}],chapter_number=14)
