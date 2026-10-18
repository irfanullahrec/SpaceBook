from stathelp import *
c=cell
U='dispersion-skewness-kurtosis'
E22='stat11-ex-3-22'; E23='stat11-ex-3-23'; E24='stat11-ex-3-24'; E25='stat11-ex-3-25'
RAW4=r"m_4=m_4'-4m_1'm_3'+6(m_1')^2m_2'-3(m_1')^4"; RAW4T="m4 = m′4 − 4m′1m′3 + 6(m′1)²m′2 − 3(m′1)⁴"
RAW3=r"m_3=m_3'-3m_1'm_2'+2(m_1')^3"; RAW3T="m3 = m′3 − 3m′1m′2 + 2(m′1)³"
RAW2=r"m_2=m_2'-(m_1')^2"; RAW2T="m2 = m′2 − (m′1)²"
RAW1=r"m_1=m_1'-m_1'"; RAW1T="m1 = m′1 − m′1"
# ---------- scan 131 (printed 123) ----------
s=page(131,U,'123','Example 3.22: moments about mean (ungrouped) · Example 3.23 (question)','مثال 3.22: اوسط کے گرد معیارِ اثر (غیر گروہی) · مثال 3.23 (سوال)','بېلګه 3.22: د اوسط شاوخوا مومنټونه (نه‌ګروپ شوي) · بېلګه 3.23 (پوښتنه)','moments-10')
Flow(s)
head(s,'ex22','Example: 3.22','مثال: 3.22','بېلګه: 3.22',exampleId=E22)
add(s,'q22','Compute first four moments about mean from the data x = 1, 1, 0, 2, 2, 3, 1, 0, 1, 3.','اعداد و شمار x = 1, 1, 0, 2, 2, 3, 1, 0, 1, 3 سے اوسط کے گرد پہلے چار معیارِ اثر حساب کریں۔','له معلوماتو x = 1, 1, 0, 2, 2, 3, 1, 0, 1, 3 څخه د اوسط شاوخوا لومړي څلور مومنټونه محاسبه کړئ.',role='question',exampleId=E22)
head(s,'sol22','Solution:','حل:','حل:',exampleId=E22)
add(s,'a1','(i) Raw moments:','(i) خام معیارِ اثر:','(i) خام مومنټونه:',role='solution',exampleId=E22)
add(s,'a2','(ii) Mean moments: Now putting these raw moments in the relations we get mean moments as;','(ii) اوسطی معیارِ اثر: اب ان خام معیارِ اثر کو تعلقات میں رکھنے سے ہمیں اوسطی معیارِ اثر یوں ملتے ہیں؛','(ii) اوسط مومنټونه: اوس دا خام مومنټونه په اړیکو کې ایښودو سره موږ اوسط مومنټونه داسې ترلاسه کوو؛',role='solution',exampleId=E22)
head(s,'ex23','Example: 3.23','مثال: 3.23','بېلګه: 3.23',exampleId=E23)
add(s,'q23','Compute first four moments about mean from the following data:','درج ذیل اعداد و شمار سے اوسط کے گرد پہلے چار معیارِ اثر حساب کریں:','له لاندې معلوماتو څخه د اوسط شاوخوا لومړي څلور مومنټونه محاسبه کړئ:',role='question',exampleId=E23,sourceGap=dict(note='The solution of Example 3.23 begins on the next page.'))
xs=[1,1,0,2,2,3,1,0,1,3]
s['tables']=[table('Example 3.22: powers of x','مثال 3.22: x کی طاقتیں','بېلګه 3.22: د x ځواکونه',[c('x'),c('x²'),c('x³'),c('x⁴')],[[c(str(x)),c(str(x**2)),c(str(x**3)),c(str(x**4))] for x in xs]+[[c('14'),c('30'),c('74'),c('198')]],exampleId=E22),
 table('Example 3.23: x and f','مثال 3.23: x اور f','بېلګه 3.23: x او f',[c('x:')]+[c(v) for v in '12345'],[[c('f:')]+[c(v) for v in ['5','7','10','6','2']]],exampleId=E23)]
eq=[('r1',r"m_1'=\dfrac{\sum x}{n}=\dfrac{14}{10}=1.4","m′1 = Σx/n = 14/10 = 1.4",E22),
 ('r2',r"m_2'=\dfrac{\sum x^2}{n}=\dfrac{30}{10}=3","m′2 = Σx²/n = 30/10 = 3",E22),
 ('r3',r"m_3'=\dfrac{\sum x^3}{n}=\dfrac{74}{10}=7.4","m′3 = Σx³/n = 74/10 = 7.4",E22),
 ('r4',r"m_4'=\dfrac{\sum x^4}{n}=\dfrac{198}{10}=19.8","m′4 = Σx⁴/n = 198/10 = 19.8",E22),
 ('m1',RAW1+r"=1.4-1.4=0",RAW1T+" = 1.4 − 1.4 = 0",E22),
 ('m2',RAW2+r"=3-(1.4)^2=3-1.98=1.04",RAW2T+" = 3 − (1.4)² = 3 − 1.98 = 1.04",E22),
 ('m3a',RAW3,RAW3T,E22),
 ('m3b',r"=7.4-3(1.4)(3)+2(1.4)^3=7.4-12.6+5.488","= 7.4 − 3(1.4)(3) + 2(1.4)³ = 7.4 − 12.6 + 5.488",E22),
 ('m3c',r"=12.888-12.6=0.288","= 12.888 − 12.6 = 0.288",E22),
 ('m4a',RAW4,RAW4T,E22),
 ('m4b',r"=19.8-4(1.4)(7.4)+6(1.4)^2(3)-3(1.4)^4","= 19.8 − 4(1.4)(7.4) + 6(1.4)²(3) − 3(1.4)⁴",E22),
 ('m4c',r"=19.8-41.44+35.28-11.5248","= 19.8 − 41.44 + 35.28 − 11.5248",E22),
 ('m4d',r"=55.08-52.965=2.12","= 55.08 − 52.965 = 2.12",E22)]
build(s,131,['ex22','q22','sol22','T:0','a1','E:r1','E:r2','E:r3','E:r4','a2','E:m1','E:m2','E:m3a','E:m3b','E:m3c','E:m4a','E:m4b','E:m4c','E:m4d','ex23','q23','T:1'],eq)
s['sourceNote']='Printed page 123. The raw moments are printed to the right of the table and are shown after it. Printed result values (m2 = 1.04, m3 = 0.288, m4 = 2.12) kept as printed; "3 − 1.98 = 1.04" is printed as shown. Pen scribbles next to the headings "Example: 3.22" and "Example: 3.23" are ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 132 (printed 124) ----------
s=page(132,U,'124','Example 3.23: moments about origin and mean moments · Example 3.24 (start)','مثال 3.23: مبدا کے گرد اور اوسطی معیارِ اثر · مثال 3.24 (آغاز)','بېلګه 3.23: د اصل شاوخوا او اوسط مومنټونه · بېلګه 3.24 (پیل)','moments-11')
Flow(s)
head(s,'sol23','Solution:','حل:','حل:',exampleId=E23)
add(s,'a1','(i) Moments about origin:','(i) مبدا کے گرد معیارِ اثر:','(i) د اصل شاوخوا مومنټونه:',role='solution',exampleId=E23)
add(s,'a2','(ii) Mean moments:','(ii) اوسطی معیارِ اثر:','(ii) اوسط مومنټونه:',role='solution',exampleId=E23)
head(s,'ex24','Example: 3.24','مثال: 3.24','بېلګه: 3.24',exampleId=E24)
add(s,'q24','Consider the following data; compute the first four moments about mean.','درج ذیل اعداد و شمار پر غور کریں؛ اوسط کے گرد پہلے چار معیارِ اثر حساب کریں۔','لاندې معلومات په پام کې ونیسئ؛ د اوسط شاوخوا لومړي څلور مومنټونه محاسبه کړئ.',role='question',exampleId=E24)
head(s,'sol24','Solution:','حل:','حل:',exampleId=E24)
add(s,'a3','(i) Moment about origin (zero)','(i) مبدا (صفر) کے گرد معیارِ اثر','(i) د اصل (صفر) شاوخوا مومنټ',role='solution',exampleId=E24,sourceGap=dict(note='The table and workings of Example 3.24 follow on the next page.'))
rows=[('1','5','5','5','5','5'),('2','7','14','28','56','112'),('3','10','30','90','270','810'),('4','6','24','96','384','1536'),('5','2','10','50','250','1250')]
s['tables']=[table('Example 3.23: moments about origin','مثال 3.23: مبدا کے گرد معیارِ اثر','بېلګه 3.23: د اصل شاوخوا مومنټونه',[c('x'),c('f'),c('fx'),c('fx²'),c('fx³'),c('fx⁴')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('30'),c('83'),c('269'),c('965'),c('3713')]],exampleId=E23),
 table('Example 3.24: group and frequency','مثال 3.24: گروہ اور تعدد','بېلګه 3.24: ډله او فریکونسي',[c('Group:','گروہ:','ډله:')]+[c(v) for v in ['0 – 4','5 – 9','10 – 14','15 – 19','20 – 24']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(v) for v in ['2','5','12','9','7']]],exampleId=E24)]
eq=[('r1',r"m_1'=\dfrac{\sum fx}{\sum f}=\dfrac{83}{30}=2.77\qquad\qquad m_2'=\dfrac{\sum fx^2}{\sum f}=\dfrac{269}{30}=8.97","m′1 = Σfx/Σf = 83/30 = 2.77    m′2 = Σfx²/Σf = 269/30 = 8.97",E23),
 ('r3',r"m_3'=\dfrac{\sum fx^3}{\sum f}=\dfrac{965}{30}=32.17\qquad\qquad m_4'=\dfrac{\sum fx^4}{\sum f}=\dfrac{3713}{30}=123.77","m′3 = Σfx³/Σf = 965/30 = 32.17    m′4 = Σfx⁴/Σf = 3713/30 = 123.77",E23),
 ('m1',RAW1+r"=2.77-2.77=0",RAW1T+" = 2.77 − 2.77 = 0",E23),
 ('m2',RAW2+r"=8.97-(2.77)^2=8.97-7.673=1.3",RAW2T+" = 8.97 − (2.77)² = 8.97 − 7.673 = 1.3",E23),
 ('m3a',RAW3,RAW3T,E23),
 ('m3b',r"=32.17-3(2.77)(8.97)+2(2.77)^3","= 32.17 − 3(2.77)(8.97) + 2(2.77)³",E23),
 ('m3c',r"=32.17-74.541+42.51=74.68-74.54=0.14","= 32.17 − 74.541 + 42.51 = 74.68 − 74.54 = 0.14",E23),
 ('m4a',RAW4,RAW4T,E23),
 ('m4b',r"=123.77-4(2.77)(32.17)+6(2.77)^2(8.97)-3(2.77)^4","= 123.77 − 4(2.77)(32.17) + 6(2.77)²(8.97) − 3(2.77)⁴",E23),
 ('m4c',r"=123.77-356.44+412.96-176.62=536.73-533.06=3.67","= 123.77 − 356.44 + 412.96 − 176.62 = 536.73 − 533.06 = 3.67",E23)]
build(s,132,['sol23','a1','T:0','E:r1','E:r3','a2','E:m1','E:m2','E:m3a','E:m3b','E:m3c','E:m4a','E:m4b','E:m4c','ex24','q24','T:1','sol24','a3'],eq)
s['sourceNote']='Printed page 124. The raw moments are printed in two side-by-side pairs, each kept as one equation. Pen scribbles beside "Example: 3.24" and ink marks at the page edges are ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 133 (printed 125) ----------
s=page(133,U,'125','Example 3.24: workings · 3.6.2 Sheppard\'s correction','مثال 3.24: حل · 3.6.2 شیپرڈ کی تصحیح','بېلګه 3.24: حل · 3.6.2 د شیپرډ سمون','moments-12')
Flow(s)
add(s,'a2','(ii) Mean moments:','(ii) اوسطی معیارِ اثر:','(ii) اوسط مومنټونه:',role='solution',exampleId=E24)
head(s,'h362',"3.6.2 Sheppard's correction","3.6.2 شیپرڈ کی تصحیح","3.6.2 د شیپرډ سمون")
add(s,'t362',"When summary statistics like mean, standard deviation and moments etc. are computed from a continuous grouped frequency distribution, the frequencies are allotted to the mid-points of the classes, which surely create error and need correction. This point was first noticed by W.F Sheppard and suggested the following corrected formulas known as Sheppard's correction. Note that first and","جب اوسط، معیاری انحراف اور معیارِ اثر وغیرہ جیسے خلاصی شماریات کسی مسلسل گروہی تعدد تقسیم سے حساب کیے جاتے ہیں تو تعدد کو طبقات کے وسطی نقطوں سے منسوب کیا جاتا ہے، جو یقیناً غلطی پیدا کرتا ہے اور تصحیح کا متقاضی ہے۔ یہ نکتہ سب سے پہلے ڈبلیو۔ایف۔ شیپرڈ نے محسوس کیا اور درج ذیل تصحیح شدہ فارمولے تجویز کیے جو شیپرڈ کی تصحیح کہلاتے ہیں۔ نوٹ کریں کہ پہلا اور","کله چې لنډیز احصایې لکه اوسط، معیاري انحراف او مومنټونه او نور له یوه دوامداره ګروپي فریکونسي ویش څخه محاسبه کېږي نو فریکونسي د ټولګیو منځنیو نقطو ته ورکول کېږي، چې یقیناً تېروتنه رامنځته کوي او سمون ته اړتیا لري. دا ټکی لومړی W.F Sheppard ولیدل او لاندې سمون شوي فورمولونه یې وړاندیز کړل چې د شیپرډ سمون بلل کېږي. پام وکړئ چې لومړی او",sourceGap=dict(note='The sentence continues on the next page ("third mean moments need no correction.").'))
rows=[('0 – 4','2','2','4','8','16','32'),('5 – 9','5','7','35','245','1715','12005'),('10 – 14','12','12','144','1728','20736','248832'),('15 – 19','9','17','153','2601','44217','751689'),('20 – 24','7','22','154','3388','74536','1639792')]
s['tables']=[table('Example 3.24: moments about origin','مثال 3.24: مبدا کے گرد معیارِ اثر','بېلګه 3.24: د اصل شاوخوا مومنټونه',[c('Group','گروہ','ډله'),c('f'),c('x'),c('fx'),c('fx²'),c('fx³'),c('fx⁴')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('35'),c('–'),c('490'),c('7970'),c('141220'),c('2652350')]],exampleId=E24)]
eq=[('r1',r"m_1'=\dfrac{\sum fx}{\sum f}=\dfrac{490}{35}=14\qquad\qquad m_2'=\dfrac{\sum fx^2}{\sum f}=\dfrac{7970}{35}=227.71","m′1 = Σfx/Σf = 490/35 = 14    m′2 = Σfx²/Σf = 7970/35 = 227.71",E24),
 ('r3',r"m_3'=\dfrac{\sum fx^3}{\sum f}=\dfrac{141220}{35}=4034.86\qquad\qquad m_4'=\dfrac{\sum fx^4}{\sum f}=\dfrac{2652350}{35}=75781.43","m′3 = Σfx³/Σf = 141220/35 = 4034.86    m′4 = Σfx⁴/Σf = 2652350/35 = 75781.43",E24),
 ('m1',RAW1+r"=14-14=0",RAW1T+" = 14 − 14 = 0",E24),
 ('m2',RAW2+r"=227.71-(14)^2=227.71-196=31.71",RAW2T+" = 227.71 − (14)² = 227.71 − 196 = 31.71",E24),
 ('m3a',RAW3,RAW3T,E24),
 ('m3b',r"=4034.86-3(14)(227.71)+2(14)^3","= 4034.86 − 3(14)(227.71) + 2(14)³",E24),
 ('m3c',r"=4034.86-9563.82+5488","= 4034.86 − 9563.82 + 5488",E24),
 ('m3d',r"=9522.86-9563.82=-40.96","= 9522.86 − 9563.82 = −40.96",E24),
 ('m4a',RAW4,RAW4T,E24),
 ('m4b',r"=75781.86-4(14)(4034.86)+6(14)^2(227.71)-3(14)^4","= 75781.86 − 4(14)(4034.86) + 6(14)²(227.71) − 3(14)⁴   [printed 75781.86; the next line has 75781.43]",E24),
 ('m4c',r"=75781.43-225952.16+267786.96-115248","= 75781.43 − 225952.16 + 267786.96 − 115248",E24),
 ('m4d',r"=343568.39-341200.16=2368.23","= 343568.39 − 341200.16 = 2368.23",E24)]
build(s,133,['T:0','E:r1','E:r3','a2','E:m1','E:m2','E:m3a','E:m3b','E:m3c','E:m3d','E:m4a','E:m4b','E:m4c','E:m4d','h362','t362'],eq)
s['sourceNote']='Printed page 125. The table of Example 3.24 (continuing from the previous page) is at the top of the page. The raw moments are printed in two side-by-side pairs, each kept as one equation. The "m3" result −40.96 and "m4" result 2368.23 are as printed. Header graphics and watermark excluded.'
s['vocabulary']={'sheppard':dict(ur='شیپرڈ',ps='شیپرډ')}
save(s)
# ---------- scan 134 (printed 126) ----------
s=page(134,U,'126','Sheppard\'s correction (formulas) · 3.6.3 Moment ratios · Example 3.25 (start)','شیپرڈ کی تصحیح (فارمولے) · 3.6.3 معیارِ اثر کے تناسب · مثال 3.25 (آغاز)','د شیپرډ سمون (فورمولونه) · 3.6.3 د مومنټ نسبتونه · بېلګه 3.25 (پیل)','moments-13')
Flow(s)
add(s,'c1','third mean moments need no correction.','تیسرا اوسطی معیارِ اثر کو تصحیح کی ضرورت نہیں۔','دریم اوسط مومنټونه سمون ته اړتیا نه لري.',sourceGap=dict(note='Completes the sentence from the previous page ("Note that first and").'))
add(s,'c2','All moments calculated in previous examples are uncorrected. Put them in these formulas to get corrected moments and variance.','پچھلی مثالوں میں حساب کیے گئے تمام معیارِ اثر غیر تصحیح شدہ ہیں۔ تصحیح شدہ معیارِ اثر اور تغیر حاصل کرنے کے لیے انہیں ان فارمولوں میں رکھیں۔','په تېرو بېلګو کې محاسبه شوي ټول مومنټونه ناسمون شوي دي. سمون شوي مومنټونه او وریانس ترلاسه کولو لپاره دا په دې فورمولونو کې کېږدئ.')
head(s,'h363','3.6.3 Moment ratios','3.6.3 معیارِ اثر کے تناسب','3.6.3 د مومنټ نسبتونه')
add(s,'t363','Name of the ratios tells that both numerators and denominators will have moments: The commonly used moment ratios given by Karl Pearson are:','تناسب کا نام بتاتا ہے کہ شمار کنندہ اور نسب نما دونوں میں معیارِ اثر ہوں گے۔ کارل پیئرسن کے دیے ہوئے عام طور پر استعمال ہونے والے معیارِ اثر کے تناسب یہ ہیں:','د نسبتونو نوم ښیي چې شمېرونکی او مخرج دواړه به مومنټونه ولري: د Karl Pearson لخوا ورکړل شوي عموماً کارېدونکي د مومنټ نسبتونه دا دي:')
add(s,'t364','where β is Greek alphabet pronounced as beta.','جہاں β یونانی حرف ہے جسے بیٹا پڑھا جاتا ہے۔','چېرته چې β یوناني توری دی چې بیټا تلفظ کېږي.')
add(s,'t365','Due to some mathematical flaws, Karl Pearson redefined moment ratios which are independent of origin and scale of measurement as follows;','کچھ ریاضیاتی نقائص کی وجہ سے کارل پیئرسن نے معیارِ اثر کے تناسب کو دوبارہ بیان کیا جو مبدا اور پیمائش کے پیمانے سے آزاد ہیں، جو یوں ہیں؛','د ځینو ریاضیاتي نیمګړتیاوو له امله Karl Pearson د مومنټ نسبتونه بیا تعریف کړل چې د اصل او اندازې د پیمانې څخه خپلواک دي، په دې توګه؛')
add(s,'t366','where γ is Greek alphabet pronounced as gamma.','جہاں γ یونانی حرف ہے جسے گیما پڑھا جاتا ہے۔','چېرته چې γ یوناني توری دی چې ګاما تلفظ کېږي.')
add(s,'t367','These are standard measures and give important information about the shape of the distribution, that is γ1 tells about skewness and γ2 about kurtosis.','یہ معیاری پیمانے ہیں اور تقسیم کی شکل کے بارے میں اہم معلومات دیتے ہیں، یعنی γ1 کجی کے بارے میں اور γ2 نوکیلے پن کے بارے میں بتاتا ہے۔','دا معیاري اندازې دي او د ویش د شکل په اړه مهمې معلومات ورکوي، یعنې γ1 د کوړوالي په اړه او γ2 د تېزوالي په اړه وايي.')
head(s,'ex25','Example 3.25','مثال 3.25','بېلګه 3.25',exampleId=E25)
add(s,'q25','The first four moments about the P.M = 35, h = 3 are 0.45, 8.73, 12.15 and 204.93.','عارضی اوسط P.M = 35، h = 3 کے گرد پہلے چار معیارِ اثر 0.45, 8.73, 12.15 اور 204.93 ہیں۔','د لنډمهاله اوسط P.M = 35، h = 3 شاوخوا لومړي څلور مومنټونه 0.45, 8.73, 12.15 او 204.93 دي.',role='question',exampleId=E25,sourceGap=dict(note='The question of Example 3.25 continues on the next page.'))
eq=[('s1',r"m_2(\text{corrected})=m_2(\text{uncorrected})-\dfrac{h^2}{12}","m2(corrected) = m2(uncorrected) − h²/12",None),
 ('s2',r"m_4(\text{corrected})=m_4(\text{uncorrected})-\dfrac{h^2}{2}\,m_2(\text{uncorrected})+\dfrac{7}{240}h^4","m4(corrected) = m4(uncorrected) − (h²/2)m2(uncorrected) + (7/240)h⁴",None),
 ('p1',r"\beta_1=\dfrac{\mu_3^2}{\mu_2^3},\qquad \beta_2=\dfrac{\mu_4}{\mu_2^2}\qquad\text{(Population case)}","β1 = μ3²/μ2³,  β2 = μ4/μ2²   (Population case)",None),
 ('p2',r"b_1=\dfrac{m_3^2}{m_2^3},\qquad b_2=\dfrac{m_4}{m_2^2}\qquad\text{(Sample case)}","b1 = m3²/m2³,  b2 = m4/m2²   (Sample case)",None),
 ('g1',r"\gamma_1=\sqrt{b_1}=\sqrt{\dfrac{m_3^2}{m_2^3}}=\dfrac{m_3}{m_2^{3/2}}=\dfrac{m_3}{S^3},\qquad -\infty<\gamma_1<\infty","γ1 = √b1 = √(m3²/m2³) = m3/m2^(3/2) = m3/S³,   −∞ < γ1 < ∞",None),
 ('g2',r"\gamma_2=b_2-3=\dfrac{m_4}{m_2^2}-3=\dfrac{m_4}{S^4}-3,\qquad -\infty<\gamma_2<\infty","γ2 = b2 − 3 = m4/m2² − 3 = m4/S⁴ − 3,   −∞ < γ2 < ∞",None)]
build(s,134,['c1','E:s1','E:s2','c2','h363','t363','E:p1','t364','E:p2','t365','E:g1','E:g2','t366','t367','ex25','q25'],eq)
s['sourceNote']='Printed page 126. The first line completes the sentence from the previous page. The two pairs of moment-ratio formulas are printed with a vertical bracket and the labels "(Population case)" and "(Sample case)" on the right. Printed spellings kept: "Sheppard" in the section heading. Header graphics and watermark excluded.'
s['vocabulary']={'moment ratios':dict(ur='معیارِ اثر کے تناسب',ps='د مومنټ نسبتونه')}
save(s)
