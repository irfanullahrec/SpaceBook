from statlib import *
c=cell
U='central-tendency'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def curve():
    o='<line x1="40" y1="130" x2="320" y2="130" stroke="#222" stroke-width="1.5"/>'+T(26,134,'X',13)
    o+='<path d="M60,128 C100,125 130,70 180,28 C230,65 260,125 310,128" fill="none" stroke="#1c6aa8" stroke-width="2"/><line x1="180" y1="28" x2="180" y2="130" stroke="#1c6aa8" stroke-width="2"/>'
    o+='<path d="M180,185 L180,140 M174,150 L180,140 L186,150" stroke="#1c6aa8" stroke-width="2" fill="none"/>'+T(180,202,'Representative',12)+T(180,217,'value here',12)
    return svg(360,230,'Bell-shaped curve with a vertical line at its centre marked as the representative value',o)
# ---------- scan 63 (printed 55) ----------
s=page(63,U,'55','2.1 Central tendency · 2.1.1 Types · 2.1.2 Properties of a good measure','2.1 مرکزی رجحان · 2.1.1 اقسام · 2.1.2 اچھے پیمانے کی خصوصیات','2.1 مرکزي تمایل · 2.1.1 ډولونه · 2.1.2 د ښې اندازې ځانګړتیاوې','central-tendency-intro')
head(s,'h21','2.1 Central tendency','2.1 مرکزی رجحان','2.1 مرکزي تمایل')
add(s,'t21a','After collection and presentation of data, the next important step is the analysis of data to bring out the hidden qualities in the form of few constants that will adequately describe the data. The first ever need in practice is to introduce “one representative value”. The position of this value may be anywhere in the given data but preferable is one which lies at the centre of the data and not in the extreme tails of the distribution. Graphically it can be shown as given in the figure.','اعداد و شمار کے اکٹھا کرنے اور پیشکش کے بعد اگلا اہم مرحلہ اعداد و شمار کا تجزیہ ہے تاکہ چند مستقلات کی صورت میں پوشیدہ خصوصیات سامنے لائی جا سکیں جو اعداد و شمار کو مناسب طور پر بیان کریں۔ عملی طور پر پہلی ضرورت "ایک نمائندہ قدر" متعارف کرانا ہے۔ اس قدر کی پوزیشن دیے گئے اعداد و شمار میں کہیں بھی ہو سکتی ہے لیکن بہتر وہ ہے جو اعداد و شمار کے مرکز میں ہو نہ کہ تقسیم کی انتہائی دموں میں۔ اسے گرافی طور پر اس طرح دکھایا جا سکتا ہے جیسا کہ شکل میں دیا گیا ہے۔','د معلوماتو له راټولولو او وړاندې کولو وروسته بله مهمه ګام د معلوماتو تحلیل دی ترڅو د څو ثابتونو په بڼه پټې ځانګړتیاوې راښکاره شي چې معلومات په مناسب ډول بیان کړي. په عمل کې لومړنۍ اړتیا "یو استازی ارزښت" معرفي کول دي. د دې ارزښت موقعیت په ورکړل شویو معلوماتو کې هر ځای کېدای شي خو غوره هغه دی چې د معلوماتو په مرکز کې وي نه د ویش په سختو لکیو کې. دا په ګرافي ډول داسې ښودل کېدای شي لکه څنګه چې په شکل کې ورکړل شوی.')
add(s,'t21b','This single representative value is called central tendency or central value or balancing point or average. High peak of the curve at this value shows that most of the observations in the given data are like this or near to it and very few values are lying far away from it. The procedures employed to find the central value are called measures of central tendency.','اس واحد نمائندہ قدر کو مرکزی رجحان یا مرکزی قدر یا توازن کا نقطہ یا اوسط کہتے ہیں۔ اس قدر پر منحنی کی اونچی چوٹی ظاہر کرتی ہے کہ دیے گئے اعداد و شمار میں زیادہ تر مشاہدات اس جیسے ہیں یا اس کے قریب ہیں اور بہت کم قدریں اس سے دور ہیں۔ مرکزی قدر معلوم کرنے کے لیے استعمال ہونے والے طریقے مرکزی رجحان کے پیمانے کہلاتے ہیں۔','دا واحد استازی ارزښت مرکزي تمایل یا مرکزي ارزښت یا د انډول نقطه یا اوسط بلل کېږي. په دې ارزښت د منحني لوړه څوکه ښيي چې په ورکړل شویو معلوماتو کې ډېرې کتنې د دې په څېر یا ورته نږدې دي او ډېر لږ ارزښتونه ترې لرې پراته دي. هغه طریقې چې مرکزي ارزښت موندلو لپاره کارول کېږي د مرکزي تمایل اندازې بلل کېږي.')
head(s,'h211','2.1.1 Types of measures of central tendency','2.1.1 مرکزی رجحان کے پیمانوں کی اقسام','2.1.1 د مرکزي تمایل د اندازو ډولونه')
add(s,'t211','Statistics deals with variability in this universe. It is not possible to have a single standard procedure for determining central tendency or average. Statisticians have developed different methods for measuring central tendency whose proper names are:','شماریات اس کائنات میں تغیر سے متعلق ہے۔ مرکزی رجحان یا اوسط کے تعین کے لیے ایک واحد معیاری طریقہ کار ممکن نہیں ہے۔ ماہرینِ شماریات نے مرکزی رجحان ناپنے کے لیے مختلف طریقے وضع کیے ہیں جن کے مناسب نام یہ ہیں:','احصایه په دې کائنات کې له تغیر سره معامله کوي. د مرکزي تمایل یا اوسط د ټاکلو لپاره یو واحد معیاري طریقه ممکنه نه ده. احصایه پوهانو د مرکزي تمایل د اندازې لپاره بېلابېلې طریقې جوړې کړې چې مناسب نومونه یې دا دي:')
head(s,'h211i','(i) Mathematical measure of central tendency','(i) مرکزی رجحان کا ریاضیاتی پیمانہ','(i) د مرکزي تمایل ریاضیاتي اندازه')
add(s,'t211i','Arithmetic mean, geometric mean and harmonic mean are called mathematical measures of central tendency.','حسابی اوسط، ہندسی اوسط اور ہارمونی اوسط مرکزی رجحان کے ریاضیاتی پیمانے کہلاتے ہیں۔','حسابي اوسط، هندسي اوسط او هارمونیک اوسط د مرکزي تمایل ریاضیاتي اندازې بلل کېږي.')
head(s,'h211ii','(ii) Positional measure of central tendency','(ii) مرکزی رجحان کا مقامی پیمانہ','(ii) د مرکزي تمایل موقعیتي اندازه')
add(s,'t211ii','Median, quartiles, deciles, percentiles and mode are positional measures of central tendency','وسطانیہ، چوتھائیاں (کوارٹائلز)، دسویں (ڈیسائلز)، فی صدکیات (پرسنٹائلز) اور عادہ مرکزی رجحان کے مقامی پیمانے ہیں','میانه، څلورمې، لسمې، سلمې او مود د مرکزي تمایل موقعیتي اندازې دي')
head(s,'h212','2.1.2 Properties of a good measure of central tendency','2.1.2 مرکزی رجحان کے اچھے پیمانے کی خصوصیات','2.1.2 د مرکزي تمایل د ښې اندازې ځانګړتیاوې')
add(s,'t212','A good measure of central tendency is one which','مرکزی رجحان کا اچھا پیمانہ وہ ہے جو','د مرکزي تمایل ښه اندازه هغه ده چې')
for i,(a,b,d) in enumerate([('i. is simple to understand and easy to calculate;','i. سمجھنے میں آسان اور حساب کرنے میں سادہ ہو؛','i. د پوهېدو لپاره ساده او د محاسبې لپاره اسانه وي؛'),('ii. make uses of all of the given data;','ii. دیے گئے تمام اعداد و شمار کو استعمال کرے؛','ii. ټول ورکړل شوي معلومات وکاروي؛'),('iii. is not too much affected by extreme values or wild observations, or outliers.','iii. انتہائی قدروں یا بے قاعدہ مشاہدات یا آؤٹ لائرز سے زیادہ متاثر نہ ہو۔','iii. د سختو ارزښتونو یا ډېرو بېلو کتنو یا باندنیو (outliers) لخوا ډېر اغېزمن نه شي.')],1): add(s,f'p{i}',a,b,d,listGroup='properties',**({'sourceGap':dict(note='The list continues with item iv on the next page.')} if i==3 else {}))
s['figures']=[dict(id='stat11-s063-fig1',svg=curve(),caption='Central tendency: representative value at the centre of the distribution',captionUrdu='مرکزی رجحان: تقسیم کے مرکز میں نمائندہ قدر',captionPashto='مرکزي تمایل: د ویش په مرکز کې استازی ارزښت',labels=[lab('Representative value here','نمائندہ قدر یہاں','استازی ارزښت دلته'),lab('X','X','X')],sourceGap=dict(note='Redrawn as a coded schematic curve.'))]
ids=[p['id'] for p in s['paras']]
s['flow']=[dict(type='paragraphs',ids=ids[:2]),dict(type='figure',index=0),dict(type='paragraphs',ids=ids[2:])]
s['sourceNote']='Printed page 55. In the book the figure sits to the right of the second paragraph (text wraps around it). Header graphics and watermark excluded.'
s['vocabulary']={'central tendency':dict(ur='مرکزی رجحان',ps='مرکزي تمایل'),'outliers':dict(ur='آؤٹ لائرز (بے قاعدہ قدریں)',ps='باندنۍ ارزښتونه')}
save(s)
# ---------- scan 64 (printed 56) ----------
s=page(64,U,'56','2.2 Arithmetic mean · Examples 2.1, 2.2 · 2.2.1 Individual series','2.2 حسابی اوسط · مثالیں 2.1، 2.2 · 2.2.1 انفرادی سلسلہ','2.2 حسابي اوسط · بېلګې 2.1، 2.2 · 2.2.1 انفرادي لړۍ','arithmetic-mean-1')
F=Flow(s)
add(s,'c1','iv. is capable of further mathematical treatment i.e. used to evaluate other statistics.','iv. مزید ریاضیاتی عمل کے قابل ہو یعنی دیگر شماریات کا اندازہ لگانے میں استعمال ہو سکے۔','iv. د نورې ریاضیاتي پروسې وړ وي یعنې د نورو احصایو د ارزونې لپاره وکارول شي.',listGroup='properties',sourceGap=dict(note='Continues the list begun at the foot of the previous page.'))
head(s,'h22','2.2 Arithmetic mean','2.2 حسابی اوسط','2.2 حسابي اوسط')
add(s,'t22','This is the most frequently used measure of central tendency. It is also called mean or average. It is defined as, the sum of all given values divided by the number of values is called Arithmetic mean, that is','یہ مرکزی رجحان کا سب سے زیادہ استعمال ہونے والا پیمانہ ہے۔ اسے اوسط بھی کہتے ہیں۔ اس کی تعریف یہ ہے کہ تمام دی گئی قدروں کا مجموعہ قدروں کی تعداد پر تقسیم کرنے سے حاصل ہونے والی مقدار حسابی اوسط کہلاتی ہے، یعنی','دا د مرکزي تمایل تر ټولو ډېر کارېدونکې اندازه ده. دې ته اوسط هم ویل کېږي. تعریف یې دا دی چې د ټولو ورکړل شویو ارزښتونو مجموعه د ارزښتونو په شمېر تقسیم کړل شي حسابي اوسط بلل کېږي، یعنې')
F.rest()
F.e('am',r'\text{A.M}=\dfrac{\text{Sum of all values}}{\text{Number of values}}','A.M = (Sum of all values) / (Number of values)')
add(s,'t22b','Notations used for A.M are μ (in population case) and x̄ (in sample case), so','حسابی اوسط کے لیے استعمال ہونے والی علامتیں μ (مجموعے کی صورت میں) اور x̄ (نمونے کی صورت میں) ہیں، لہٰذا','د حسابي اوسط لپاره کارېدونکې نښې μ (د ټولنې په حالت کې) او x̄ (د نمونې په حالت کې) دي، نو')
F.rest()
F.e('pm',r'\mu=\dfrac{\sum_{i=1}^{N}x_i}{N}\qquad\text{(Formula for population mean)}','μ = (Σ (i = 1 to N) xi) / N   (Formula for population mean)')
F.e('sm',r'\bar{x}=\dfrac{\sum_{i=1}^{n}x_i}{n}\qquad\text{(Formula for sample mean)}','x̄ = (Σ (i = 1 to n) xi) / n   (Formula for sample mean)')
head(s,'ex1','Example: 2.1','مثال: 2.1','بېلګه: 2.1',exampleId='stat11-ex-2-1')
add(s,'q1','For a population of N = 4 values x = 3, 7, 4, 6, the population mean is','N = 4 قدروں x = 3, 7, 4, 6 کے مجموعے کے لیے مجموعی اوسط ہے','د N = 4 ارزښتونو x = 3, 7, 4, 6 د ټولنې لپاره د ټولنې اوسط دی',role='question',exampleId='stat11-ex-2-1')
F.rest()
F.e('e1',r'\mu=\dfrac{\sum x}{N}=\dfrac{3+7+4+6}{4}=\dfrac{20}{4}=5','μ = Σx / N = (3 + 7 + 4 + 6)/4 = 20/4 = 5',exampleId='stat11-ex-2-1')
head(s,'h221','2.2.1 Computation of arithemetic mean in case of individual series or ungrouped data','2.2.1 انفرادی سلسلے یا غیر گروہی اعداد و شمار کی صورت میں حسابی اوسط کا حساب','2.2.1 د انفرادي لړۍ یا نه‌ګروپ شویو معلوماتو په حالت کې د حسابي اوسط محاسبه')
head(s,'hi','(i) By direct method','(i) براہِ راست طریقے سے','(i) په مستقیمه طریقه')
F.rest()
F.e('dm',r'\bar{x}=\dfrac{\sum x}{n}','x̄ = Σx / n')
head(s,'ex2','Example: 2.2','مثال: 2.2','بېلګه: 2.2',exampleId='stat11-ex-2-2')
add(s,'q2','Find mean for the scores 10, 8, 4, 6, and 12.','اسکورز 10, 8, 4, 6 اور 12 کا اوسط معلوم کریں۔','د نمرو 10, 8, 4, 6 او 12 اوسط ومومئ.',role='question',exampleId='stat11-ex-2-2')
head(s,'sol2','Solution:','حل:','حل:',exampleId='stat11-ex-2-2')
F.rest()
F.e('e2',r'\bar{x}=\dfrac{\sum x}{n}=\dfrac{40}{5}=8','x̄ = Σx / n = 40/5 = 8',exampleId='stat11-ex-2-2')
F.done()
s['sourceNote']='Printed page 56. Printed spelling "arithemetic" in the 2.2.1 heading is retained. The first line continues the list of properties from the previous page. Header graphics and watermark excluded.'
s['vocabulary']={'arithmetic mean':dict(ur='حسابی اوسط',ps='حسابي اوسط')}
save(s)
# ---------- scan 65 (printed 57) ----------
s=page(65,U,'57','(ii) Shortcut or coding method · Example 2.3 · (iii) Step-deviation method','(ii) مختصر یا کوڈنگ طریقہ · مثال 2.3 · (iii) گام انحراف طریقہ','(ii) لنډ یا کوډینګ طریقه · بېلګه 2.3 · (iii) ګام‌انحراف طریقه','shortcut-method')
F=Flow(s)
head(s,'hii','(ii) By shortcut or coding method','(ii) مختصر یا کوڈنگ طریقے سے','(ii) په لنډه یا کوډینګ طریقه')
F.rest()
F.e('sc',r'\bar{x}=A+\dfrac{\sum D}{n},','x̄ = A + ΣD / n,')
add(s,'t1','Where A = assumed or provisional mean and D = x − A','جہاں A = فرض کردہ یا عارضی اوسط اور D = x − A','چېرته چې A = انګېرل شوی یا لنډمهاله اوسط او D = x − A')
add(s,'t2','Any value in the given data can be chosen as A, but for convenience it is suggested to first arrange the data in ascending order of magnitude and then take the most middle value as A. If the number of observations is even, then take average of the two most middle values as A.','دیے گئے اعداد و شمار میں سے کوئی بھی قدر A کے طور پر منتخب کی جا سکتی ہے لیکن سہولت کے لیے تجویز کیا جاتا ہے کہ پہلے اعداد و شمار کو مقدار کے صعودی ترتیب میں ترتیب دیں اور پھر سب سے درمیانی قدر کو A لیں۔ اگر مشاہدات کی تعداد جفت ہو تو دو سب سے درمیانی قدروں کا اوسط A لیں۔','په ورکړل شویو معلوماتو کې هر ارزښت د A په توګه ټاکل کېدای شي خو د اسانتیا لپاره وړاندیز کېږي چې لومړی معلومات د کچې په پورته‌والي ترتیب ترتیب کړئ او بیا تر ټولو منځنی ارزښت د A په توګه واخلئ. که د کتنو شمېر جفت وي نو د دوو تر ټولو منځنیو ارزښتونو اوسط د A په توګه واخلئ.')
head(s,'ex3','Example: 2.3','مثال: 2.3','بېلګه: 2.3',exampleId='stat11-ex-2-3')
add(s,'q3','Let x = 10, 8, 4, 6, 12. Find average for these data by shortcut method.','فرض کریں x = 10, 8, 4, 6, 12۔ مختصر طریقے سے ان اعداد و شمار کا اوسط معلوم کریں۔','فرض کړئ x = 10, 8, 4, 6, 12. د لنډې طریقې په واسطه د دې معلوماتو اوسط ومومئ.',role='question',exampleId='stat11-ex-2-3')
head(s,'sol3','Solution:','حل:','حل:',exampleId='stat11-ex-2-3')
add(s,'a3','Arranging the given data, we have','دیے گئے اعداد و شمار کو ترتیب دینے پر ہمیں ملتا ہے','ورکړل شوي معلومات ترتیبولو سره موږ لرو',role='solution',exampleId='stat11-ex-2-3')
s['tables']=[table('Example 2.3: D = x − 8','مثال 2.3: D = x − 8','بېلګه 2.3: D = x − 8',[c('x'),c('D = x − 8')],[[c('4'),c('4 − 8 = −4')],[c('6'),c('= −2')],[c('8'),c('= 0')],[c('10'),c('= 2')],[c('12'),c('= 4')],[c(''),c('ΣD = 0')]],exampleId='stat11-ex-2-3',role='solution')]
F.rest();F.tb(0)
add(s,'a3b','Here A = 8','یہاں A = 8','دلته A = 8',role='solution',exampleId='stat11-ex-2-3')
F.rest()
F.e('e3',r'\therefore\ \bar{x}=A+\dfrac{\sum D}{n}=8+\dfrac{0}{5}=8+0=8','∴ x̄ = A + ΣD / n = 8 + 0/5 = 8 + 0 = 8',exampleId='stat11-ex-2-3')
head(s,'hiii','(iii) By change of origin and scale or step-deviation method','(iii) مبدا اور پیمانے کی تبدیلی یا گام انحراف طریقے سے','(iii) د اصل او پیمانې په بدلون یا ګام‌انحراف طریقه')
F.rest()
F.e('st',r'\bar{x}=A+\dfrac{\sum fu}{\sum f}\times h','x̄ = A + (Σfu / Σf) × h')
add(s,'t4','Where u = (x − A)/h and “h” is class interval.','جہاں u = (x − A)/h اور "h" جماعتی وقفہ ہے۔','چېرته چې u = (x − A)/h او "h" د ټولګي وقفه ده.')
add(s,'t5','This method is applicable only when there is an equal class interval in the data.','یہ طریقہ صرف اس وقت قابلِ اطلاق ہے جب اعداد و شمار میں جماعتی وقفہ مساوی ہو۔','دا طریقه یوازې هغه وخت د پلي کېدو وړ ده کله چې په معلوماتو کې د ټولګي وقفه مساوي وي.')
F.done()
s['sourceNote']='Printed page 57. In the table the entries below the first row are printed as "= −2", "= 0", etc. (the repeated "x − 8" is omitted in print). The foot shows a ghost of the page-number bar. Header graphics and watermark excluded.'
s['vocabulary']={'coding':dict(ur='کوڈنگ',ps='کوډینګ')}
save(s)
# ---------- scan 66 (printed 58) ----------
s=page(66,U,'58','Example 2.4 · 2.2.2 Discrete series or grouped data · Example 2.5','مثال 2.4 · 2.2.2 منفصل سلسلہ یا گروہی اعداد و شمار · مثال 2.5','بېلګه 2.4 · 2.2.2 منفصله لړۍ یا ګروپي معلومات · بېلګه 2.5','example24-25')
F=Flow(s)
head(s,'ex4','Example: 2.4','مثال: 2.4','بېلګه: 2.4',exampleId='stat11-ex-2-4')
add(s,'q4','Find mean for the scores 12, 8, 6, 10 and 4 by change of origin and scale method.','اسکورز 12, 8, 6, 10 اور 4 کا اوسط مبدا اور پیمانے کی تبدیلی کے طریقے سے معلوم کریں۔','د نمرو 12, 8, 6, 10 او 4 اوسط د اصل او پیمانې د بدلون په طریقه ومومئ.',role='question',exampleId='stat11-ex-2-4')
head(s,'sol4','Solution:','حل:','حل:',exampleId='stat11-ex-2-4')
add(s,'a4','Arranging the data in ascending order,','اعداد و شمار کو صعودی ترتیب میں ترتیب دینے پر،','معلومات په پورته‌والي ترتیب ترتیبولو سره،',role='solution',exampleId='stat11-ex-2-4')
s['tables']=[table('Example 2.4: u = (x − 8)/2','مثال 2.4: u = (x − 8)/2','بېلګه 2.4: u = (x − 8)/2',[c('x'),c('u = (x − 8)/2')],[[c('4'),c('(4 − 8)/2 = −2')],[c('6'),c('= −1')],[c('8'),c('= 0')],[c('10'),c('= 1')],[c('12'),c('= 2')],[c(''),c('Σu = 0')]],exampleId='stat11-ex-2-4',role='solution'),
 table('Example 2.5: x, f, fx','مثال 2.5: x، f، fx','بېلګه 2.5: x، f، fx',[c('x'),c('f'),c('fx')],[[c(a),c(b),c(d)] for a,b,d in [('12','1','12'),('14','4','56'),('16','6','96'),('18','10','180'),('20','7','140'),('22','2','44')]]+[[c('Total','کل','ټول'),c('30'),c('528')]],exampleId='stat11-ex-2-5',role='solution')]
F.rest();F.tb(0)
add(s,'a4b','Here A = 8 and h = 2','یہاں A = 8 اور h = 2','دلته A = 8 او h = 2',role='solution',exampleId='stat11-ex-2-4')
F.rest()
F.e('e4',r'\therefore\ \bar{x}=A+\dfrac{\sum u}{n}\times h=8+\dfrac{0}{5}\times2=8+0=8','∴ x̄ = A + (Σu / n) × h = 8 + (0/5) × 2 = 8 + 0 = 8',exampleId='stat11-ex-2-4')
add(s,'t4','All the three methods give the same answer but shortcut methods are used to reduce mathematical labour and save time.','تینوں طریقے ایک ہی جواب دیتے ہیں لیکن مختصر طریقے ریاضیاتی محنت کم کرنے اور وقت بچانے کے لیے استعمال ہوتے ہیں۔','درې واړه طریقې یو شان ځواب ورکوي خو لنډې طریقې د ریاضیاتي زحمت د کمولو او وخت ژغورلو لپاره کارول کېږي.')
head(s,'h222','2.2.2 Computation of arithmetic mean in case of discrete series or grouped data','2.2.2 منفصل سلسلے یا گروہی اعداد و شمار کی صورت میں حسابی اوسط کا حساب','2.2.2 د منفصلې لړۍ یا ګروپي معلوماتو په حالت کې د حسابي اوسط محاسبه')
head(s,'ex5','Example: 2.5','مثال: 2.5','بېلګه: 2.5',exampleId='stat11-ex-2-5')
add(s,'q5','Calculate the arithmetic mean for the following data: x: 12, 14, 16, 18, 20, 22; f: 1, 4, 6, 10, 7, 2','درج ذیل اعداد و شمار کا حسابی اوسط حساب کریں: x: 12, 14, 16, 18, 20, 22؛ f: 1, 4, 6, 10, 7, 2','د لاندې معلوماتو حسابي اوسط محاسبه کړئ: x: 12, 14, 16, 18, 20, 22؛ f: 1, 4, 6, 10, 7, 2',role='question',exampleId='stat11-ex-2-5')
head(s,'sol5','Solution:','حل:','حل:',exampleId='stat11-ex-2-5')
add(s,'i5','(i) By direct method','(i) براہِ راست طریقے سے','(i) په مستقیمه طریقه',role='solution',exampleId='stat11-ex-2-5')
F.rest()
F.e('e5',r'\bar{x}=\dfrac{\sum fx}{\sum f}','x̄ = Σfx / Σf',exampleId='stat11-ex-2-5')
F.rest();F.tb(1)
F.done()
s['sourceNote']='Printed page 58. A thumb is visible at the top-left of the scan and a small mark at the left; both ignored. The printed data lines (x / f) of Example 2.5 are combined into the question text. The page ends with the direct-method table; the remaining methods continue on the next page. Header graphics and watermark excluded.'
s['vocabulary']={'discrete series':dict(ur='منفصل سلسلہ',ps='منفصله لړۍ')}
save(s)
