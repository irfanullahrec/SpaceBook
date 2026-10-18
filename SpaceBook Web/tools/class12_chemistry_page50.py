"""PDF50 printed92–93: table15.1 continuation, homologous series/table15.2."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def table(identity,headers,rows,ur,ps,urheaders,psheaders):
 blocks.append({'id':identity,'headers':headers,'rows':rows,'translations':[{'language':'اردو','headers':urheaders,'rows':ur},{'language':'پښتو','headers':psheaders,'rows':ps}]});layout.append({'type':'sourceDataTable','tableId':identity})
rows=[['Carboxylic acid','–C(=O)–OH or –COOH','Carboxyl','R–C(=O)–OH or CₙH₂ₙ₊₁COOH','CH₃–C(=O)–OH acetic acid (ethanoic acid)'],['Acid halide','–C(=O)–X or –COX','Halo carbonyl','R–C(=O)–X or CₙH₂ₙ₊₁COX','CH₃–C(=O)–Cl acetyl chloride'],['Acid amide','–C(=O)–NH₂ or –CONH₂','Amide','R–C(=O)–NH₂ or CₙH₂ₙ₊₁CONH₂','CH₃–C(=O)–NH₂ acetamide'],['Ester','–C(=O)–OR′ or –COOR','Ester (alkoxy carbonyl)','R–C(=O)–O–R or CₙH₂ₙ₊₁COOCₙH₂ₙ₊₁','CH₃–C(=O)–OCH₃ methyl acetate'],['Alkyl cyanide or Nitrile','–C≡N','Cyano','R–CN or CₙH₂ₙ₊₁CN','CH₃CN methyl cyanide']]
urclasses=['کاربوکسلک تیزاب','ایسڈ ہیلائیڈ','ایسڈ امائیڈ','ایسٹر','الکائل سائنائیڈ یا نائٹرائل'];psclasses=['کاربوکسیلیک اسید','اسید هالایډ','اسید امایډ','ایستر','الکایل سیانایډ یا نایټرایل']
urnames=['کاربوکسل','ہیلو کاربونائل','امائیڈ','ایسٹر (الکوکسی کاربونائل)','سائنو'];psnames=['کاربوکسیل','هالو کاربونیل','امایډ','ایستر (الکوکسي کاربونیل)','سیانو']
urex=['ایسیٹک تیزاب (ایتھانوئک تیزاب)','ایسیٹائل کلورائیڈ','ایسیٹ امائیڈ','میتھائل ایسیٹیٹ','میتھائل سائنائیڈ'];psex=['اسیتیک اسید (ایتانویک اسید)','اسیتایل کلورایډ','اسیت امایډ','میتیل اسیتېټ','میتیل سیانایډ'];formulas=['CH₃–C(=O)–OH','CH₃–C(=O)–Cl','CH₃–C(=O)–NH₂','CH₃–C(=O)–OCH₃','CH₃CN']
ur=[[urclasses[i],r[1],urnames[i],r[3],formulas[i]+' '+urex[i]] for i,r in enumerate(rows)];ps=[[psclasses[i],r[1],psnames[i],r[3],formulas[i]+' '+psex[i]] for i,r in enumerate(rows)]
table('chem12-table15-1-continuation',['Class of Compounds','Functional Group','Name of Functional group','General Formula','Example'],rows,ur,ps,['مرکبات کی قسم','فعلی گروپ','فعلی گروپ کا نام','عمومی فارمولا','مثال'],['د مرکباتو ډله','فعالي ګروپ','د فعالي ګروپ نوم','عمومي فورمول','بېلګه'])
add('Homologous Series','ہم سلسلہ خاندان','همولوګ لړۍ','heading')
add('A series of organic compounds in which all members possess similar structural features and similar chemical characteristics, but each member is different from the next member by a methylene (–CH₂–) group is called homologous series.',
 'نامیاتی مرکبات کا سلسلہ جس کے تمام ارکان مماثل ساختی اور کیمیائی خصوصیات رکھتے ہوں، مگر ہر رکن اگلے سے میتھیلین (–CH₂–) گروپ کا فرق رکھتا ہو، ہم سلسلہ خاندان ہے۔',
 'د عضوي مرکباتو لړۍ چې ټول غړي یې ورته جوړښتي او کیمیاوي ځانګړنې لري، خو هر غړی له راتلونکي څخه د میتیلین (–CH₂–) ګروپ توپیر لري، همولوګ لړۍ ده.')
add('All the members that differ from each other by methylene group, –CH₂–, are called homologues. Each class of organic compounds has its own homologous series which can be represented by a general formula. For example, alkanes (saturated hydrocarbons) form a series of compounds. It can be represented by a general formula CₙH₂ₙ₊₂ where ‘n’ shows the number of carbon atoms in the corresponding alkane.',
 'میتھیلین گروپ –CH₂– کا باہمی فرق رکھنے والے ارکان ہومولوگز ہیں۔ ہر قسم کا اپنا ہم سلسلہ خاندان ہے جس کا عمومی فارمولا ہے۔ مثلاً الکینز (سیر شدہ ہائیڈروکاربن) سلسلہ بناتے ہیں جس کا فارمولا CₙH₂ₙ₊₂ ہے؛ n متعلقہ الکین میں کاربن ایٹموں کی تعداد ہے۔',
 'په میتیلین ګروپ –CH₂– له یو بل توپیر لرونکي غړي هومولوګونه دي. هره ډله خپله همولوګ لړۍ لري چې عمومي فورمول لري. لکه الکانونه (مشبوع هایدروکاربنونه) لړۍ جوړوي چې فورمول یې CₙH₂ₙ₊₂ دی؛ n په اړوند الکان کې د کاربني اټومونو شمېر دی.')
add('Table 15.2 Alkane Homologous Series','جدول15.2 الکین ہم سلسلہ خاندان','جدول15.2 د الکانونو همولوګ لړۍ')
names=['Methane','Ethane','Propane','Butane','Pentane','Hexane','Heptane','Octane','Nonane','Decane'];urnames=['میتھین','ایتھین','پروپین','بیوٹین','پینٹین','ہیکسین','ہیپٹین','آکٹین','نونین','ڈیکین'];psnames=['میتان','ایتان','پروپان','بیوټان','پینټان','هېکسان','هېپټان','اوکټان','نونان','ډېکان']
sub=str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉');rows=[]
for n,name in enumerate(names,1):
 mf='CH₄' if n==1 else 'C'+str(n).translate(sub)+'H'+str(2*n+2).translate(sub)
 structural='CH₄' if n==1 else 'CH₃'+'CH₂'*(n-2)+'CH₃';rows.append([str(n),mf,name,structural])
table('chem12-table15-2',['No. of C atoms','Molecular formula (CₙH₂ₙ₊₂)','Name with suffix (–ane)','Structural formula'],rows,[[r[0],r[1],urnames[i],r[3]] for i,r in enumerate(rows)],[[r[0],r[1],psnames[i],r[3]] for i,r in enumerate(rows)],['C ایٹموں کی تعداد','سالماتی فارمولا (CₙH₂ₙ₊₂)','–ane لاحقے والا نام','ساختی فارمولا'],['د C اټومونو شمېر','مالیکولي فورمول (CₙH₂ₙ₊₂)','د –ane وروستاړي نوم','جوړښتي فورمول'])
add('As it is clear from alkane homologous series that each member is different from the adjacent member by CH₂. Similarly, this series can be expanded beyond C₁₀ to higher alkanes. Similar homologous series can be developed for alkenes, alkynes, alcohols, ethers, amines, carboxylic acids, carbonyl compounds etc.',
 'الکین خاندان سے واضح ہے کہ ہر رکن پڑوسی سے CH₂ کا فرق رکھتا ہے۔ سلسلہ C₁₀ سے آگے بلند الکینز تک بڑھ سکتا ہے۔ ایسے خاندان الکینز (دوہرے بند)، الکائنز، الکوحل، ایتھرز، امینز، کاربوکسلک تیزابوں اور کاربونائل مرکبات کے لیے بن سکتے ہیں۔',
 'د الکان لړۍ ښيي چې هر غړی له ګاونډي څخه د CH₂ توپیر لري. لړۍ له C₁₀ پورته لوړو الکانونو ته غځېدای شي. ورته لړۍ د الکینونو، الکاینونو، الکولونو، ایترونو، امینونو، کاربوکسیلیک اسیدونو او کاربونیل مرکباتو لپاره جوړېدای شي.')
add('Characteristics of homologous Series','ہم سلسلہ خاندان کی خصوصیات','د همولوګ لړۍ ځانګړنې','heading')
for row in [('As mentioned, each class of organic compounds has its own homologous series having general formula.','جیسا بیان ہوا، ہر قسم کا اپنا ہم سلسلہ خاندان اور عمومی فارمولا ہے۔','لکه یاد شول، هره ډله خپله همولوګ لړۍ او عمومي فورمول لري.'),('All the members of homologous series have similar chemical properties and same general methods of preparation similar structural features and same functional group.','تمام ارکان کی کیمیائی خصوصیات مماثل، تیاری کے عمومی طریقے یکساں، ساختی خصوصیات مماثل اور فعلی گروپ یکساں ہیں۔','ټول غړي ورته کیمیاوي ځانګړنې، یو شان عمومي چمتووالي لارې، ورته جوړښتي ځانګړنې او یو شان فعالي ګروپ لري.'),('The physical properties like melting point, boiling points, densities etc, increase down the series due to increase in their molecular masses.','سالماتی کمیت بڑھنے سے خاندان میں نیچے نقطہ پگھلاؤ، نقطہ ابال اور کثافت جیسے طبیعی خواص بڑھتے ہیں۔','د مالیکولي کتلو په زیاتېدو په لړۍ کې ښکته د وېلې کېدو او جوش ټکي او کثافتونه زیاتېږي.')]:add(*row,'list')
add('15.7 Detection of elements in Organic Compounds','15.7 نامیاتی مرکبات میں عناصر کی شناخت','15.7 په عضوي مرکباتو کې د عناصرو پېژندنه','heading')
add('The main elements present in organic compounds are carbon and hydrogen as well as oxygen, nitrogen, sulphur and halogens. Following methods can be used to detect these elements, in the organic compound.',
 'نامیاتی مرکبات کے بنیادی عناصر کاربن اور ہائیڈروجن، نیز آکسیجن، نائٹروجن، سلفر اور ہیلوجنز ہیں۔ ان کی شناخت کے لیے درج ذیل طریقے ہیں۔',
 'په عضوي مرکباتو کې اصلي عناصر کاربن او هایدروجن، او هم اکسیجن، نایتروجن، سلفر او هالوجنونه دي. د پېژندلو لپاره یې لاندې لارې کارېږي.')
record=section('15.5','Homologous series and functional-group table','ہم سلسلہ خاندان اور فعلی گروپوں کا جدول','همولوګ لړۍ او د فعالي ګروپونو جدول',paras,layout,blocks,'92–93');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':50,'printedPages':[92,93]}]
if __name__=='__main__':save(50,[record],trim=[{'id':'15.6','startsAt':'Detection of Carbon'}],chapter_number=15)
