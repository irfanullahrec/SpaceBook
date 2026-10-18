from stathelp import *
c=cell
U='dispersion-skewness-kurtosis'
E16='stat11-ex-3-16'; E17='stat11-ex-3-17'; E18='stat11-ex-3-18'; E19='stat11-ex-3-19'
# ---------- scan 123 (printed 115) ----------
s=page(123,U,'115','Mean moments: formulas · Example 3.16: ungrouped data','اوسطی معیارِ اثر: فارمولے · مثال 3.16: غیر گروہی اعداد و شمار','اوسط مومنټونه: فورمولونه · بېلګه 3.16: نه‌ګروپ شوي معلومات','moments-2')
Flow(s)
add(s,'t1','m1, m2, m3, m4, … (Sample case) and their formulas are;','m1, m2, m3, m4, … (نمونے کی صورت) اور ان کے فارمولے یہ ہیں؛','m1, m2, m3, m4, … (د نمونې حالت) او د هغوی فورمولونه دا دي؛',sourceGap=dict(note='Continues the notation μ1, μ2, μ3, μ4 (Population case) from the previous page.'))
add(s,'lu','For ungrouped data','غیر گروہی اعداد و شمار کے لیے','د نه‌ګروپ شویو معلوماتو لپاره')
add(s,'lg','For grouped data','گروہی اعداد و شمار کے لیے','د ګروپي معلوماتو لپاره')
add(s,'t2','This is direct method of computation of moments about mean.','یہ اوسط کے گرد معیارِ اثر کے حساب کا براہِ راست طریقہ ہے۔','دا د اوسط شاوخوا د مومنټونو د محاسبې مستقیمه طریقه ده.')
add(s,'t3','Computation of moments about mean in case of individual series or ungrouped data','انفرادی سلسلے یا غیر گروہی اعداد و شمار کی صورت میں اوسط کے گرد معیارِ اثر کا حساب','د انفرادي لړۍ یا نه‌ګروپ شویو معلوماتو په حالت کې د اوسط شاوخوا د مومنټونو محاسبه')
head(s,'ex16','Example: 3.16','مثال: 3.16','بېلګه: 3.16',exampleId=E16)
add(s,'q16','Calculate the first four moments about mean for the data 1.05, 1.07, 1.19, 1.45.','اعداد و شمار 1.05, 1.07, 1.19, 1.45 کے لیے اوسط کے گرد پہلے چار معیارِ اثر حساب کریں۔','د معلوماتو 1.05, 1.07, 1.19, 1.45 لپاره د اوسط شاوخوا لومړي څلور مومنټونه محاسبه کړئ.',role='question',exampleId=E16)
head(s,'sol16','Solution:','حل:','حل:',exampleId=E16)
rows=[('1.05','-0.14','0.0196','-0.00274','0.000384'),('1.07','-0.12','0.0144','-0.00173','0.000207'),('1.19','0','0','0','0'),('1.45','0.26','0.0676','0.017576','0.00457'),('4.76','0','0.1016','0.013106','0.005161')]
s['tables']=[table('Example 3.16 solution table','مثال 3.16 کا حل: جدول','د بېلګې 3.16 د حل جدول',[c('x'),c('(x − x̄)'),c('(x − x̄)²'),c('(x − x̄)³'),c('(x − x̄)⁴')],[[c(v) for v in r] for r in rows],exampleId=E16)]
eq=[('u1',r'm_1=\dfrac{\sum(x-\bar{x})}{n}=0\qquad\qquad m_1=\dfrac{\sum f(x-\bar{x})}{\sum f}=0','m1 = Σ(x − x̄)/n = 0    m1 = Σf(x − x̄)/Σf = 0',None),
 ('u2',r'm_2=\dfrac{\sum(x-\bar{x})^2}{n}=S^2\qquad\qquad m_2=\dfrac{\sum f(x-\bar{x})^2}{\sum f}=S^2','m2 = Σ(x − x̄)²/n = S²    m2 = Σf(x − x̄)²/Σf = S²',None),
 ('u3',r'm_3=\dfrac{\sum(x-\bar{x})^3}{n}\qquad\qquad m_3=\dfrac{\sum f(x-\bar{x})^3}{\sum f}','m3 = Σ(x − x̄)³/n    m3 = Σf(x − x̄)³/Σf',None),
 ('u4',r'm_4=\dfrac{\sum(x-\bar{x})^4}{n}\qquad\qquad m_4=\dfrac{\sum f(x-\bar{x})^4}{\sum f}','m4 = Σ(x − x̄)⁴/n    m4 = Σf(x − x̄)⁴/Σf',None),
 ('a',r'\bar{x}=\dfrac{\sum x}{n}=\dfrac{4.76}{4}=1.19','x̄ = Σx/n = 4.76/4 = 1.19',E16),
 ('b',r'm_1=\dfrac{\sum(x-\bar{x})}{n}=\dfrac{0}{4}=0','m1 = Σ(x − x̄)/n = 0/4 = 0',E16)]
build(s,123,['t1','lu','lg','E:u1','E:u2','E:u3','E:u4','t2','t3','ex16','q16','sol16','T:0','E:a','E:b'],eq)
s['sourceNote']='Printed page 115. The formulas for ungrouped data (left) and grouped data (right) are printed side by side and each left/right pair is kept as one equation. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 124 (printed 116) ----------
s=page(124,U,'116','Example 3.16 (end) · Example 3.17: discrete series','مثال 3.16 (اختتام) · مثال 3.17: منفصل سلسلہ','بېلګه 3.16 (پای) · بېلګه 3.17: منفصله لړۍ','moments-3')
Flow(s)
add(s,'t1','Calculation of moment about mean in case of discrete series or grouped data','منفصل سلسلے یا گروہی اعداد و شمار کی صورت میں اوسط کے گرد معیارِ اثر کا حساب','د منفصلې لړۍ یا ګروپي معلوماتو په حالت کې د اوسط شاوخوا د مومنټ محاسبه')
head(s,'ex17','Example: 3.17','مثال: 3.17','بېلګه: 3.17',exampleId=E17)
add(s,'q17','Find first four moments about the mean for the following data:','درج ذیل اعداد و شمار کے لیے اوسط کے گرد پہلے چار معیارِ اثر معلوم کریں:','د لاندې معلوماتو لپاره د اوسط شاوخوا لومړي څلور مومنټونه ومومئ:',role='question',exampleId=E17)
head(s,'sol17','Solution:','حل:','حل:',exampleId=E17)
rows=[('22','1','22','-17','-17','289','-4913','83521'),('27','4','108','-12','-48','576','-6912','82944'),('32','8','256','-07','-56','392','-2744','19208'),('37','11','407','-02','-22','44','-88','176'),('42','15','630','3','45','135','405','1215'),('47','9','423','8','72','576','4608','36864'),('52','2','104','13','26','338','4394','57122')]
s['tables']=[table('Example 3.17: x and f','مثال 3.17: x اور f','بېلګه 3.17: x او f',[c('x:')]+[c(v) for v in ['22','27','32','37','42','47','52']],[[c('f:')]+[c(v) for v in ['1','4','8','11','15','9','2']]],exampleId=E17),
 table('Example 3.17 solution table','مثال 3.17 کا حل: جدول','د بېلګې 3.17 د حل جدول',[c('x'),c('f'),c('fx'),c('(x − x̄)'),c('f(x − x̄)'),c('f(x − x̄)²'),c('f(x − x̄)³'),c('f(x − x̄)⁴')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('50'),c('1950'),c('–'),c('0'),c('2350'),c('-5250'),c('281050')]],exampleId=E17)]
eq=[('a',r'm_2=\dfrac{(x-\bar{x})^2}{n}=\dfrac{0.1016}{4}=0.025','m2 = (x − x̄)²/n = 0.1016/4 = 0.025   [printed without Σ]',E16),
 ('b',r'm_3=\dfrac{(x-\bar{x})^3}{n}=\dfrac{0.0131106}{4}=0.0033','m3 = (x − x̄)³/n = 0.0131106/4 = 0.0033   [printed without Σ; 0.0131106 as printed]',E16),
 ('c',r'm_4=\dfrac{(x-\bar{x})^4}{n}=\dfrac{0.005161}{4}=0.0013','m4 = (x − x̄)⁴/n = 0.005161/4 = 0.0013   [printed without Σ]',E16),
 ('d',r'\bar{x}=\dfrac{fx}{f}=\dfrac{1950}{50}=39','x̄ = fx/f = 1950/50 = 39   [printed without Σ]',E17),
 ('e',r'm_1=\dfrac{f(x-\bar{x})}{f}=\dfrac{0}{50}=0','m1 = f(x − x̄)/f = 0/50 = 0   [printed without Σ]',E17)]
build(s,124,['E:a','E:b','E:c','t1','ex17','q17','T:0','sol17','T:1','E:d','E:e'],eq)
s['sourceNote']='Printed page 116. The first three formulas complete Example 3.16 (the printed fractions omit the summation signs). In the solution table the x − x̄ entries "−07" and "−02" are printed with a leading zero for −7 and −2; the word "Total" and "1950" wrap across two lines in the total row. A handwritten red mark at the top-left is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 125 (printed 117) ----------
s=page(125,U,'117','Example 3.17 (end) · Example 3.18: continuous series','مثال 3.17 (اختتام) · مثال 3.18: مسلسل سلسلہ','بېلګه 3.17 (پای) · بېلګه 3.18: دوامداره لړۍ','moments-4')
Flow(s)
add(s,'t1','Calculation of moments about mean in case of continuous series;','مسلسل سلسلے کی صورت میں اوسط کے گرد معیارِ اثر کا حساب؛','د دوامدارې لړۍ په حالت کې د اوسط شاوخوا د مومنټونو محاسبه؛')
head(s,'ex18','Example: 3.18','مثال: 3.18','بېلګه: 3.18',exampleId=E18)
add(s,'q18','Compute the first four moments about mean for the following data:','درج ذیل اعداد و شمار کے لیے اوسط کے گرد پہلے چار معیارِ اثر حساب کریں:','د لاندې معلوماتو لپاره د اوسط شاوخوا لومړي څلور مومنټونه محاسبه کړئ:',role='question',exampleId=E18)
head(s,'sol18','Solution:','حل:','حل:',exampleId=E18)
add(s,'nw','Now','اب','اوس',role='solution',exampleId=E18)
rows=[('0 – 9','2','4.5','9','-13','-26','338','-4394','57122'),('10 – 19','4','14.5','58','-3','-12','36','-108','324'),('20 – 29','3','24.5','73.5','7','21','147','1029','7203'),('30 – 39','1','34.5','34.5','17','17','289','4913','83521')]
s['tables']=[table('Example 3.18: classes and frequency','مثال 3.18: طبقات اور تعدد','بېلګه 3.18: ټولګي او فریکونسي',[c('Classes:','طبقات:','ټولګي:')]+[c(v) for v in ['0 – 9','10 – 19','20 – 29','30 – 39']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(v) for v in ['2','4','3','1']]],exampleId=E18),
 table('Example 3.18 solution table','مثال 3.18 کا حل: جدول','د بېلګې 3.18 د حل جدول',[c('Classes','طبقات','ټولګي'),c('f'),c('x'),c('fx'),c('(x − x̄)'),c('f(x − x̄)'),c('f(x − x̄)²'),c('f(x − x̄)³'),c('f(x − x̄)⁴')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('10'),c(''),c('175'),c('–'),c('–'),c('810'),c('1440'),c('148170')]],exampleId=E18)]
eq=[('a',r'm_2=\dfrac{\sum f(x-\bar{x})^2}{f}=\dfrac{2350}{50}=47','m2 = Σf(x − x̄)²/f = 2350/50 = 47',E17),
 ('b',r'm_3=\dfrac{\sum f(x-\bar{x})^3}{f}=\dfrac{-5250}{50}=-105','m3 = Σf(x − x̄)³/f = −5250/50 = −105',E17),
 ('c',r'm_4=\dfrac{\sum f(x-\bar{x})^4}{f}=\dfrac{281050}{50}=5621','m4 = Σf(x − x̄)⁴/f = 281050/50 = 5621',E17),
 ('d',r'\bar{x}=\dfrac{\sum fx}{\sum f}=\dfrac{175}{10}=17.5','x̄ = Σfx/Σf = 175/10 = 17.5',E18),
 ('e',r'm_1=\dfrac{\sum f(x-\bar{x})}{\sum f}=\dfrac{0}{10}=0\qquad\qquad m_2=\dfrac{\sum f(x-\bar{x})^2}{\sum f}=\dfrac{810}{10}=81','m1 = Σf(x − x̄)/Σf = 0/10 = 0    m2 = Σf(x − x̄)²/Σf = 810/10 = 81',E18)]
build(s,125,['E:a','E:b','E:c','t1','ex18','q18','T:0','sol18','T:1','E:d','nw','E:e'],eq)
s['sourceNote']='Printed page 117. The first three lines complete Example 3.17 (the printed 281050/50 = 5621 is kept). In the solution table of Example 3.18 the x entry of the total row is empty. m1 and m2 are printed side by side after the word "Now" and are kept as one equation. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 126 (printed 118) ----------
s=page(126,U,'118','Example 3.18 (end) · Raw moments · Relationship between mean and raw moments · Example 3.19 (start)','مثال 3.18 (اختتام) · خام معیارِ اثر · اوسطی اور خام معیارِ اثر کا تعلق · مثال 3.19 (آغاز)','بېلګه 3.18 (پای) · خام مومنټونه · د اوسط او خامو مومنټونو اړیکه · بېلګه 3.19 (پیل)','moments-5')
Flow(s)
add(s,'t1','(ii) Raw moments or moments about any arbitrary point or provisional mean (a): When moments are computed about the P.M, they are called raw moments and are denoted by','(ii) خام معیارِ اثر یا کسی بھی من مانے نقطے یا عارضی اوسط (a) کے گرد معیارِ اثر: جب معیارِ اثر P.M کے گرد حساب کیے جائیں تو انہیں خام معیارِ اثر کہا جاتا ہے اور ظاہر کیا جاتا ہے','(ii) خام مومنټونه یا د هر خپلسري نقطې یا لنډمهاله اوسط (a) شاوخوا مومنټونه: کله چې مومنټونه د P.M شاوخوا محاسبه شي نو دوی ته خام مومنټونه ویل کېږي او ښودل کېږي')
add(s,'lu','For ungrouped data','غیر گروہی اعداد و شمار کے لیے','د نه‌ګروپ شویو معلوماتو لپاره')
add(s,'lg','For grouped data','گروہی اعداد و شمار کے لیے','د ګروپي معلوماتو لپاره')
add(s,'t2','Relationship between mean and raw moments','اوسطی اور خام معیارِ اثر کا تعلق','د اوسط او خامو مومنټونو اړیکه')
add(s,'t3','This is shortcut method for calculation of mean moments.','یہ اوسطی معیارِ اثر کے حساب کا مختصر طریقہ ہے۔','دا د اوسط مومنټونو د محاسبې لنډه طریقه ده.')
head(s,'ex19','Example: 3.19','مثال: 3.19','بېلګه: 3.19',exampleId=E19)
add(s,'q19','Compute the first four moments for the following data: 1, 1, 0, 2, 2, 3, 1, 0, 1, 3','درج ذیل اعداد و شمار کے لیے پہلے چار معیارِ اثر حساب کریں: 1, 1, 0, 2, 2, 3, 1, 0, 1, 3','د لاندې معلوماتو لپاره لومړي څلور مومنټونه محاسبه کړئ: 1, 1, 0, 2, 2, 3, 1, 0, 1, 3',role='question',exampleId=E19)
eq=[('a',r'm_3=\dfrac{\sum f(x-\bar{x})^3}{\sum f}=\dfrac{1440}{10}=144\qquad\qquad m_4=\dfrac{\sum f(x-\bar{x})^4}{\sum f}=\dfrac{148170}{10}=14817','m3 = Σf(x − x̄)³/Σf = 1440/10 = 144    m4 = Σf(x − x̄)⁴/Σf = 148170/10 = 14817',E18),
 ('n1',r'\mu_1^{\prime},\ \mu_2^{\prime},\ \mu_3^{\prime},\ \mu_4^{\prime},\ \ldots\qquad\text{(Population case)}',"μ′1, μ′2, μ′3, μ′4, …   (Population case)",None),
 ('n2',r"m_1^{\prime},\ m_2^{\prime},\ m_3^{\prime},\ m_4^{\prime},\ \ldots\qquad\text{(Sample case) and their formulas are:}","m′1, m′2, m′3, m′4, …   (Sample case) and their formulas are:",None),
 ('r1',r"m_1'=\dfrac{\sum(x-a)}{n}\qquad\qquad m_1'=\dfrac{\sum f(x-a)}{\sum f}","m′1 = Σ(x − a)/n    m′1 = Σf(x − a)/Σf",None),
 ('r2',r"m_2'=\dfrac{\sum(x-a)^2}{n}\qquad\qquad m_2'=\dfrac{\sum f(x-a)^2}{\sum f}","m′2 = Σ(x − a)²/n    m′2 = Σf(x − a)²/Σf",None),
 ('r3',r"m_3'=\dfrac{\sum(x-a)^3}{n}\qquad\qquad m_3'=\dfrac{\sum f(x-a)^3}{\sum f}","m′3 = Σ(x − a)³/n    m′3 = Σf(x − a)³/Σf",None),
 ('r4',r"m_4'=\dfrac{\sum(x-a)^4}{n}\qquad\qquad m_4'=\dfrac{\sum f(x-a)^4}{\sum f}","m′4 = Σ(x − a)⁴/n    m′4 = Σf(x − a)⁴/Σf",None),
 ('s1',r"m_1=m_1'-m_1'=0","m1 = m′1 − m′1 = 0",None),
 ('s2',r"m_2=m_2'-(m_1')^2","m2 = m′2 − (m′1)²",None),
 ('s3',r"m_3=m_3'-3m_1'm_2'+2(m_1')^3","m3 = m′3 − 3m′1m′2 + 2(m′1)³",None),
 ('s4',r"m_4=m_4'-4m_1'm_3'+6(m_1')^2m_2'-3(m_1')^4","m4 = m′4 − 4m′1m′3 + 6(m′1)²m′2 − 3(m′1)⁴",None)]
build(s,126,['E:a','t1','E:n1','E:n2','lu','lg','E:r1','E:r2','E:r3','E:r4','t2','E:s1','E:s2','E:s3','E:s4','t3','ex19','q19'],eq)
s['sourceNote']='Printed page 118. The first line completes Example 3.18. The raw-moment formulas for ungrouped (left) and grouped (right) data are printed side by side and each pair is kept as one equation. The data values of Example 3.19 are printed on a separate row and are continued from this page onward. Header graphics and watermark excluded.'
s['vocabulary']={'raw moments':dict(ur='خام معیارِ اثر',ps='خام مومنټونه')}
save(s)
