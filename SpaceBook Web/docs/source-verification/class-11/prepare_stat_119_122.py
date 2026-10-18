from stathelp import *
c=cell
U='dispersion-skewness-kurtosis'
E14='stat11-ex-3-14'; E15='stat11-ex-3-15'
# ---------- scan 119 (printed 111) ----------
s=page(119,U,'111','3.5.8 (end) · Example 3.14: coefficient of variation, ungrouped data','3.5.8 (اختتام) · مثال 3.14: تغیر کا عددی سر، غیر گروہی اعداد و شمار','3.5.8 (پای) · بېلګه 3.14: د تغیر ضریب، نه‌ګروپ شوي معلومات','cv-1')
Flow(s)
add(s,'c1','better or consistent.','بہتر یا مستقل مزاج ہے۔','ښه یا یو شان دی.',sourceGap=dict(note='Completes the sentence from the previous page ("The smaller value of C.V means less variability which shows that performance is").'))
add(s,'i1','(i) Computation of coefficient of variation in case of ungrouped data','(i) غیر گروہی اعداد و شمار کی صورت میں تغیر کے عددی سر کا حساب','(i) د نه‌ګروپ شویو معلوماتو په حالت کې د تغیر د ضریب محاسبه')
head(s,'ex14','Example: 3.14','مثال: 3.14','بېلګه: 3.14',exampleId=E14)
add(s,'q14','Using the coefficient of variation, determine that which student performance is more consistent by considering their individual scores given below.','تغیر کے عددی سر کو استعمال کرتے ہوئے طے کریں کہ نیچے دیے گئے ان کے انفرادی اسکور کو مدنظر رکھتے ہوئے کس طالب علم کی کارکردگی زیادہ مستقل ہے۔','د تغیر د ضریب په کارولو سره وټاکئ چې د لاندې ورکړل شویو انفرادي نمرو په پام کې نیولو سره د کوم زده کوونکي فعالیت ډېر یو شان دی.',role='question',exampleId=E14)
head(s,'sol14','Solution:','حل:','حل:',exampleId=E14)
A=[58,59,60,54,65,66,52,75,69,52]; B=[56,86,89,78,71,73,84,65,66,48]
sa=[3364,3481,3600,2916,4225,4356,2704,5625,4761,2704]; sb=[3136,7396,7921,6084,5041,5329,7056,4225,4356,2304]
s['tables']=[table('Example 3.14: scores of students A and B','مثال 3.14: طلبہ A اور B کے اسکور','بېلګه 3.14: د A او B زده کوونکو نمرې',[c('x_A:')]+[c(str(v)) for v in A],[[c('x_B:')]+[c(str(v)) for v in B]],exampleId=E14),
 table('Example 3.14 solution table','مثال 3.14 کا حل: جدول','د بېلګې 3.14 د حل جدول',[c('x'),c('x_A²'),c('x'),c('x_B²')],[[c(str(A[i])),c(str(sa[i])),c(str(B[i])),c(str(sb[i]))] for i in range(10)]+[[c('Total 610','میزان 610','ټولیز 610'),c('37736'),c('716'),c('52848')]],exampleId=E14)]
eq=[('a',r'\bar{x}=\dfrac{\sum x_A}{n}=\dfrac{610}{10}=61\qquad\bar{x}_B=\dfrac{\sum x_B}{n}=\dfrac{716}{10}=71.6','x̄ = Σx_A/n = 610/10 = 61    x̄_B = Σx_B/n = 716/10 = 71.6',E14)]
build(s,119,['c1','i1','ex14','q14','T:0','sol14','T:1','E:a'],eq)
s['sourceNote']='Printed page 111. The question data are printed as two aligned rows (xA and xB). In the solution table the first total "610" is printed on the same line as the word Total. The two means are printed side by side and are kept as one equation. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 120 (printed 112) ----------
s=page(120,U,'112','Example 3.14 (end) · Example 3.15: grouped data (question start)','مثال 3.14 (اختتام) · مثال 3.15: گروہی اعداد و شمار (سوال کا آغاز)','بېلګه 3.14 (پای) · بېلګه 3.15: ګروپي معلومات (د پوښتنې پیل)','cv-2')
Flow(s)
add(s,'c1','Since C.V_A < C.V_B therefore, student-A performance is more consistent.','چونکہ C.V_A < C.V_B لہٰذا طالب علم A کی کارکردگی زیادہ مستقل ہے۔','ځکه چې C.V_A < C.V_B نو د A زده کوونکي فعالیت ډېر یو شان دی.',role='solution',exampleId=E14)
add(s,'i3','(iii) Computation of coefficient of variation from grouped data','(iii) گروہی اعداد و شمار سے تغیر کے عددی سر کا حساب','(iii) له ګروپي معلوماتو څخه د تغیر د ضریب محاسبه',sourceGap=dict(note='The scan numbers this item "(iii)"; no item "(ii)" is printed.'))
head(s,'ex15','Example: 3.15','مثال: 3.15','بېلګه: 3.15',exampleId=E15)
add(s,'q15','Expenditure of families in two cities are given below:','دو شہروں میں خاندانوں کے اخراجات نیچے دیے گئے ہیں:','په دوو ښارونو کې د کورنیو لګښتونه لاندې ورکړل شوي دي:',role='question',exampleId=E15,sourceGap=dict(note='The question continues on the next page ("Calculate the coefficient of variation in each case …").'))
ex=['21 – 30','31 – 40','41 – 50','51 – 60','61 – 70','71 – 80','81 – 90']; ca=[3,61,132,153,140,51,2]; cb=[2,14,20,27,28,7,2]
s['tables']=[table('Example 3.15: expenditure of families in two cities','مثال 3.15: دو شہروں میں خاندانوں کے اخراجات','بېلګه 3.15: په دوو ښارونو کې د کورنیو لګښتونه',[c('Expenditure (in Rs)','اخراجات (روپوں میں)','لګښت (په روپیو)'),c('No. of families – City A','خاندانوں کی تعداد – شہر A','د کورنیو شمېر – ښار A'),c('No. of families – City B','خاندانوں کی تعداد – شہر B','د کورنیو شمېر – ښار B')],[[c(ex[i]),c(str(ca[i])),c(str(cb[i]))] for i in range(7)],exampleId=E15)]
eq=[('a',r's_A=\sqrt{\dfrac{1}{n-1}\left[\sum x_A^2-\dfrac{\left(\sum x_A\right)^2}{n}\right]}\qquad s_B=\sqrt{\dfrac{1}{n-1}\left[\sum x_B^2-\dfrac{\left(\sum x_B\right)^2}{n}\right]}','s_A = √((1/(n − 1))[Σx_A² − (Σx_A)²/n])    s_B = √((1/(n − 1))[Σx_B² − (Σx_B)²/n])',E14),
 ('b',r'=\sqrt{\dfrac{1}{10-1}\left[37736-\dfrac{(610)^2}{10}\right]}\qquad=\sqrt{\dfrac{1}{10-1}\left[52848-\dfrac{(716)^2}{10}\right]}','= √((1/(10 − 1))[37736 − (610)²/10])    = √((1/(10 − 1))[52848 − (716)²/10])',E14),
 ('c',r'=7.64\qquad\qquad=13.26','= 7.64    = 13.26',E14),
 ('d',r'\text{C.V}_A=\dfrac{s_A}{\bar{x}_A}\times 100\qquad\text{C.V}_B=\dfrac{s_B}{\bar{x}_B}\times 100','C.V_A = (s_A/x̄_A) × 100    C.V_B = (s_B/x̄_B) × 100',E14),
 ('e',r'=\dfrac{7.64}{61}\times 100=12.5\%\qquad=\dfrac{13}{71.6}\times 100=18.5\%','= (7.64/61) × 100 = 12.5%    = (13/71.6) × 100 = 18.5%   [printed 13 for s_B]',E14)]
build(s,120,['E:a','E:b','E:c','E:d','E:e','c1','i3','ex15','q15','T:0'],eq)
s['sourceNote']='Printed page 112. The A and B workings are printed side by side and each pair is kept as one equation. The printed C.V_B line uses 13 (instead of 13.26) over 71.6 giving 18.5%. The two-level table header "No. of families / City A / City B" is flattened to two columns. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 121 (printed 113) ----------
s=page(121,U,'113','Example 3.15: solution','مثال 3.15: حل','بېلګه 3.15: حل','cv-3')
Flow(s)
add(s,'q15b','Calculate the coefficient of variation in each case, and check which city may be considered more consistent.','ہر صورت میں تغیر کا عددی سر حساب کریں اور جانچیں کہ کون سا شہر زیادہ مستقل سمجھا جا سکتا ہے۔','په هره حالت کې د تغیر ضریب محاسبه کړئ او وګورئ چې کوم ښار ډېر یو شان ګڼل کېدای شي.',role='question',exampleId=E15,sourceGap=dict(note='Completes the question of Example 3.15 from the previous page.'))
head(s,'sol15','Solution:','حل:','حل:',exampleId=E15)
add(s,'ca','City A','شہر A','ښار A',role='solution',exampleId=E15)
add(s,'cb','City B','شہر B','ښار B',role='solution',exampleId=E15)
xs=['25.5','35.5','45.5','55.5','65.5','75.5','85.5']; us=[-3,-2,-1,0,1,2,3]
fA=[3,61,132,153,140,51,2]; fuA=[-9,-122,-132,0,140,102,6]; fu2A=[27,244,132,0,140,204,18]
fB=[2,14,20,27,28,7,2]; fuB=[-6,-28,-20,0,28,14,6]; fu2B=[18,56,20,0,28,28,18]
s['tables']=[table('Example 3.15 solution table','مثال 3.15 کا حل: جدول','د بېلګې 3.15 د حل جدول',[c('Expenditure (in Rs)','اخراجات (روپوں میں)','لګښت (په روپیو)'),c('x'),c('u = (x − 55.5)/10'),c('City A: f','شہر A: f','ښار A: f'),c('City A: fu','شہر A: fu','ښار A: fu'),c('City A: fu²','شہر A: fu²','ښار A: fu²'),c('City B: f','شہر B: f','ښار B: f'),c('City B: fu','شہر B: fu','ښار B: fu'),c('City B: fu²','شہر B: fu²','ښار B: fu²')],
 [[c(['21 – 30','31 – 40','41 – 50','51 – 60','61 – 70','71 – 80','81 – 90'][i]),c(xs[i]),c(str(us[i])),c(str(fA[i])),c(str(fuA[i])),c(str(fu2A[i])),c(str(fB[i])),c(str(fuB[i])),c(str(fu2B[i]))] for i in range(7)]+[[c('Total','میزان','ټولیز'),c('–'),c('–'),c('542'),c('-15'),c('765'),c('100'),c('-6'),c('168')]],exampleId=E15)]
eq=[('a1',r'\bar{x}=a+\dfrac{\sum fu}{\sum f}\times h','x̄ = a + (Σfu/Σf) × h',E15),
 ('a2',r'=55.5+\dfrac{(-15)}{542}\times 10=55.22','= 55.5 + ((−15)/542) × 10 = 55.22',E15),
 ('a3',r'S=\sqrt{\dfrac{\sum fu^2}{\sum f}-\left(\dfrac{\sum fu}{\sum f}\right)^2}\times h','S = √(Σfu²/Σf − (Σfu/Σf)²) × h',E15),
 ('a4',r'=\sqrt{\dfrac{765}{542}-\left(\dfrac{-15}{542}\right)^2}\times 10','= √(765/542 − (−15/542)²) × 10',E15),
 ('a5',r'=\sqrt{1.4114-0.0009}\times 10','= √(1.4114 − 0.0009) × 10',E15),
 ('a6',r'=\sqrt{1.4105}\times 10=1.1876\times 10','= √1.4105 × 10 = 1.1876 × 10',E15),
 ('a7',r'=\sqrt{1.4105}\times 10=1.1876\times 10=11.88','= √1.4105 × 10 = 1.1876 × 10 = 11.88   [this line is printed twice in the scan]',E15),
 ('b1',r'\bar{x}=55.5+\dfrac{(-6)}{100}\times 10','x̄ = 55.5 + ((−6)/100) × 10',E15),
 ('b2',r'=55.5-0.6=54.9','= 55.5 − 0.6 = 54.9',E15),
 ('b3',r'S=\sqrt{\dfrac{168}{100}-\left(\dfrac{-6}{100}\right)^2}\times 10','S = √(168/100 − (−6/100)²) × 10',E15),
 ('b4',r'=\sqrt{1.68-0.0036}\times 10','= √(1.68 − 0.0036) × 10',E15),
 ('b5',r'=\sqrt{1.6764}\times 10','= √1.6764 × 10',E15),
 ('b6',r'=1.2948\times 10','= 1.2948 × 10',E15),
 ('b7',r'=12.95','= 12.95',E15),
 ('b8',r'\text{C.V}=\dfrac{12.95}{54.9}\times 100=23.59\ \%','C.V = (12.95/54.9) × 100 = 23.59 %',E15)]
build(s,121,['q15b','sol15','T:0','ca','E:a1','E:a2','E:a3','E:a4','E:a5','E:a6','E:a7','cb','E:b1','E:b2','E:b3','E:b4','E:b5','E:b6','E:b7','E:b8'],eq)
s['sourceNote']='Printed page 113. The City A and City B workings are printed in two columns; City A is shown first, then City B. The line "= √1.4105 × 10 = 1.1876 × 10" appears twice in City A (the second adds "= 11.88"); both are kept. The two-level table header (City A / City B with f, fu, fu²) is flattened to nine columns. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 122 (printed 114) ----------
s=page(122,U,'114','Example 3.15 (end) · 3.5.9–3.5.10 Merits and demerits · 3.6 Moments · 3.6.1 Types of moments','مثال 3.15 (اختتام) · 3.5.9–3.5.10 خوبیاں اور خامیاں · 3.6 معیارِ اثر (مومنٹس) · 3.6.1 معیارِ اثر کی اقسام','بېلګه 3.15 (پای) · 3.5.9–3.5.10 ګټې او زیانونه · 3.6 مومنټونه · 3.6.1 د مومنټونو ډولونه','moments-1')
Flow(s)
add(s,'r1','Since C.V for city A is smaller than C.V for city B, it means that there is less variability in the expenditures of families of city A. Hence city A is more consistent.','چونکہ شہر A کا C.V شہر B کے C.V سے چھوٹا ہے، اس کا مطلب ہے کہ شہر A کے خاندانوں کے اخراجات میں تغیر پذیری کم ہے۔ لہٰذا شہر A زیادہ مستقل ہے۔','ځکه چې د A ښار C.V د B ښار له C.V څخه کوچنی دی، پدې معنا چې د A ښار د کورنیو په لګښتونو کې لږ متغیرتیا شته. نو A ښار ډېر یو شان دی.',role='solution',exampleId=E15)
head(s,'h359','3.5.9 Merits and demerits of standard deviation','3.5.9 معیاری انحراف کی خوبیاں اور خامیاں','3.5.9 د معیاري انحراف ګټې او زیانونه')
add(s,'mh','Merits','خوبیاں','ګټې')
L(s,[('m1','(i) It is most widely used measure of dispersion.','(i) یہ انتشار کا سب سے زیادہ وسیع پیمانے پر استعمال ہونے والا پیمانہ ہے۔','(i) دا د خپراوي تر ټولو ډېر کارېدونکې اندازه ده.'),('m2','(ii) It is based on all values of a variable.','(ii) یہ متغیر کی تمام قدروں پر مبنی ہے۔','(ii) دا د متغیر پر ټولو ارزښتونو والړ دی.'),('m3','(iii) It is a reliable measure of dispersion.','(iii) یہ انتشار کا قابلِ اعتماد پیمانہ ہے۔','(iii) دا د خپراوي د باور وړ اندازه ده.'),('m4','(iv) It is suitable for further statistical treatment.','(iv) یہ مزید شماریاتی عمل کے لیے موزوں ہے۔','(iv) دا د نورې احصایوي پروسې لپاره مناسب دی.')],'sd-merits')
add(s,'dh','Demerits','خامیاں','زیانونه')
L(s,[('d1','(i) It is relatively difficult to compute.','(i) اس کا حساب نسبتاً مشکل ہے۔','(i) محاسبه یې نسبتاً ستونزمنه ده.'),('d2','(ii) It is highly affected by extreme values.','(ii) یہ انتہائی قدروں سے بہت زیادہ متاثر ہوتا ہے۔','(ii) دا د سختو ارزښتونو لخوا ډېر اغېزمن کېږي.')],'sd-demerits')
head(s,'h3510','3.5.10 Advantages and disadvantages of variance','3.5.10 تغیر کے فوائد اور نقصانات','3.5.10 د وریانس ګټې او زیانونه')
add(s,'ah','Advantages','فوائد','ګټې')
L(s,[('v1','(i) It is based on all the observations of a series.','(i) یہ سلسلے کے تمام مشاہدات پر مبنی ہے۔','(i) دا د لړۍ پر ټولو کتنو والړ دی.'),('v2','(ii) It possesses all the properties of a good measure of dispersion.','(ii) اس میں انتشار کے اچھے پیمانے کی تمام خصوصیات پائی جاتی ہیں۔','(ii) دا د خپراوي د ښې اندازې ټولې ځانګړتیاوې لري.')],'var-adv')
add(s,'sh','Disadvantages','نقصانات','زیانونه')
L(s,[('w1','(i) Its unit is square of the unit of measurement of data.','(i) اس کی اکائی اعداد و شمار کی پیمائش کی اکائی کا مربع ہے۔','(i) واحد یې د معلوماتو د اندازې د واحد مربع دی.'),('w2','(ii) It is sensitive to extreme values.','(ii) یہ انتہائی قدروں کے لیے حساس ہے۔','(ii) دا د سختو ارزښتونو لپاره حساس دی.')],'var-dis')
head(s,'h36','3.6 Moments','3.6 معیارِ اثر (مومنٹس)','3.6 مومنټونه')
add(s,'t36','Measures of central tendency tell us only about the balancing point of a distribution. Measures of dispersion also give only one information that is, about the variability. We need such a technique which gives more information about the distribution at once. This purpose is achieved by computation of moments. That is, First raw moment tells us about the mean, second mean moment tells us about the variance, third mean moment tells us about the Skewness and fourth mean moment tells us about the kurtosis.','مرکزی رجحان کے پیمانے ہمیں تقسیم کے صرف توازن کے نقطے کے بارے میں بتاتے ہیں۔ انتشار کے پیمانے بھی صرف ایک معلومات دیتے ہیں یعنی تغیر پذیری کے بارے میں۔ ہمیں ایسی تکنیک چاہیے جو تقسیم کے بارے میں ایک ہی وقت میں زیادہ معلومات دے۔ یہ مقصد معیارِ اثر کے حساب سے حاصل ہوتا ہے۔ یعنی پہلا خام معیارِ اثر ہمیں اوسط کے بارے میں، دوسرا اوسطی معیارِ اثر تغیر کے بارے میں، تیسرا اوسطی معیارِ اثر کجی کے بارے میں اور چوتھا اوسطی معیارِ اثر نوکیلے پن کے بارے میں بتاتا ہے۔','د مرکزي تمایل اندازې موږ ته یوازې د ویش د انډول د نقطې په اړه وايي. د خپراوي اندازې هم یوازې یو معلومات ورکوي یعنې د متغیرتیا په اړه. موږ داسې تخنیک ته اړتیا لرو چې د ویش په اړه په یو وخت کې ډېر معلومات ورکړي. دا موخه د مومنټونو په محاسبه ترلاسه کېږي. یعنې لومړی خام مومنټ موږ ته د اوسط په اړه، دویم اوسط مومنټ د وریانس په اړه، دریم اوسط مومنټ د کوړوالي په اړه او څلورم اوسط مومنټ د تېزوالي په اړه وايي.')
head(s,'h361','3.6.1 Types of moments','3.6.1 معیارِ اثر کی اقسام','3.6.1 د مومنټونو ډولونه')
add(s,'i1','(i) Mean moments or moments about arithmetic mean','(i) اوسطی معیارِ اثر یا حسابی اوسط کے گرد معیارِ اثر','(i) اوسط مومنټونه یا د حسابي اوسط شاوخوا مومنټونه')
add(s,'t361','When moments are computed about the A.M, they are called mean moments. Mean moments are denoted by','جب معیارِ اثر حسابی اوسط کے گرد حساب کیے جائیں تو انہیں اوسطی معیارِ اثر کہا جاتا ہے۔ اوسطی معیارِ اثر کو ظاہر کیا جاتا ہے','کله چې مومنټونه د A.M شاوخوا محاسبه شي نو دوی ته اوسط مومنټونه ویل کېږي. اوسط مومنټونه ښودل کېږي',sourceGap=dict(note='The notation μ1, μ2, μ3, μ4, … (Population case) at the foot of the page continues the sentence; the next page continues the notation for the sample case.'))
eq=[('a',r'\bar{x}\ \text{from }\ \dfrac{11.88}{55.22}','',None)]
s['equations']+=[eqn(122,'c',r'\text{C.V}=\dfrac{s}{\bar{x}}\times 100=\dfrac{11.88}{55.22}\times 100=21.51\%','C.V = (s/x̄) × 100 = (11.88/55.22) × 100 = 21.51%',exampleId=E15),
 eqn(122,'m',r'\mu_1,\ \mu_2,\ \mu_3,\ \mu_4,\ \ldots\qquad\text{(Population case)}','μ1, μ2, μ3, μ4, …   (Population case)')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(122,k) for k in ks])
s['flow']=[dict(type='equation',index=0),P('r1','h359','mh','m1','m2','m3','m4','dh','d1','d2','h3510','ah','v1','v2','sh','w1','w2','h36','t36','h361','i1','t361'),dict(type='equation',index=1)]
s['sourceNote']='Printed page 114. The first line completes the City B comparison of Example 3.15 (C.V for City A = 21.51%). The "s/x̄" in the printed C.V line is small and blurred. Printed wording kept: "disadvantages", "That is, First raw moment …". Black scan artefacts at the top-left corner are ignored. Header graphics and watermark excluded.'
s['vocabulary']={'moments':dict(ur='معیارِ اثر',ps='مومنټونه'),'mean moments':dict(ur='اوسطی معیارِ اثر',ps='اوسط مومنټونه')}
save(s)
