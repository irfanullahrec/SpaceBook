from stathelp import *
import math
c=cell
U='dispersion-skewness-kurtosis'
E28='stat11-ex-3-28'; E29='stat11-ex-3-29'; E30='stat11-ex-3-30'
def kurt():
    W,H=440,230; x0,x1=40,400; base=170
    cx=(x0+x1)/2
    o=f'<line x1="{x0-10}" y1="{base}" x2="{x1+10}" y2="{base}" stroke="#111" stroke-width="2"/><line x1="{cx}" y1="30" x2="{cx}" y2="{base}" stroke="#111" stroke-width="2"/>'
    sc=125/(1/0.55)
    for sg,col in ((0.55,'#111'),(0.8,'#111'),(1.1,'#111')):
        pts=[]
        for i in range(0,121):
            t=-3+6*i/120.0
            y=base-sc*math.exp(-t*t/(2*sg*sg))/sg
            pts.append(f'{cx+t*(x1-x0)/6.0:.1f},{y:.1f}')
        o+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2"/>'
    o+=T(cx,base+24,'Mean',14,'middle',700)
    o+=f'<line x1="{cx+16}" y1="52" x2="{cx+52}" y2="34" stroke="#111"/>'+T(cx+56,32,'Lepto-kurtic',12,'start')
    o+=f'<line x1="{cx+44}" y1="88" x2="{cx+78}" y2="62" stroke="#111"/>'+T(cx+82,62,'Meso-kurtic',12,'start')
    o+=f'<line x1="{cx+86}" y1="142" x2="{cx+112}" y2="110" stroke="#111"/>'+T(cx+116,108,'Platy-kurtic',12,'start')
    return svg(W,H,'Three symmetric curves: a tall narrow lepto-kurtic curve, a medium meso-kurtic curve and a flat platy-kurtic curve, all centred on the mean',o)
# ---------- scan 143 (printed 135) ----------
s=page(143,U,'135','Example 3.28 (Q2, Q3, Sk) · 3.8 Kurtosis','مثال 3.28 (Q2, Q3, Sk) · 3.8 نوکیلا پن','بېلګه 3.28 (Q2, Q3, Sk) · 3.8 تېزوالی','kurtosis-1')
Flow(s)
add(s,'a1','⇒ Q3 lies in the group (44.5 – 49.5)','⇒ Q3 گروہ (44.5 – 49.5) میں واقع ہے','⇒ Q3 په ګروپ (44.5 – 49.5) کې پرته ده',role='solution',exampleId=E28)
add(s,'a2','The given distribution is negatively skewed.','دی گئی تقسیم منفی کج ہے۔','ورکړل شوی ویش منفي کوړ دی.',role='solution',exampleId=E28)
head(s,'h38','3.8 Kurtosis','3.8 نوکیلا پن','3.8 تېزوالی')
add(s,'t38','Kurtosis is a Greek word introduced by Karl Pearson. It means the peakedness or flatness of the graph of a frequency distribution as compared to the normal curve.','نوکیلا پن ایک یونانی لفظ ہے جسے کارل پیئرسن نے متعارف کرایا۔ اس کا مطلب تعدد تقسیم کے گراف کا نارمل منحنی کے مقابلے میں نوکیلا یا چپٹا ہونا ہے۔','تېزوالی یو یوناني کلمه ده چې Karl Pearson معرفي کړه. پدې معنا چې د فریکونسي ویش د ګراف د نورمال منحني په پرتله تېز یا چپټ والی.')
L(s,[('k1','If curve of a distribution is like normal curve it is called meso-kurtic.','اگر تقسیم کا منحنی نارمل منحنی جیسا ہو تو اسے میسو کرٹک کہتے ہیں۔','که د ویش منحني د نورمال منحني په څېر وي نو دې ته میسو‌کرټیک ویل کېږي.'),('k2','If curve of a distribution is flatter than the normal curve, it is called platy-kurtic.','اگر تقسیم کا منحنی نارمل منحنی سے زیادہ چپٹا ہو تو اسے پلیٹی کرٹک کہتے ہیں۔','که د ویش منحني د نورمال منحني څخه ډېر چپټ وي نو دې ته پلېټي‌کرټیک ویل کېږي.'),('k3','If curve of a distribution is high peaked than the normal curve, it is called lepto-kurtic.','اگر تقسیم کا منحنی نارمل منحنی سے زیادہ اونچی چوٹی والا ہو تو اسے لیپٹو کرٹک کہتے ہیں۔','که د ویش منحني د نورمال منحني څخه ډېره لوړه څوکه ولري نو دې ته لېپټو‌کرټیک ویل کېږي.')],'kurt-types')
s['figures']=[dict(id='stat11-s143-fig1',svg=kurt(),caption='Lepto-kurtic, meso-kurtic and platy-kurtic curves about the mean',captionUrdu='اوسط کے گرد لیپٹو کرٹک، میسو کرٹک اور پلیٹی کرٹک منحنی',captionPashto='د اوسط شاوخوا لېپټو‌کرټیک، میسو‌کرټیک او پلېټي‌کرټیک منحنیګانې',labels=[lab('Lepto-kurtic','لیپٹو کرٹک','لېپټو‌کرټیک'),lab('Meso-kurtic','میسو کرٹک','میسو‌کرټیک'),lab('Platy-kurtic','پلیٹی کرٹک','پلېټي‌کرټیک'),lab('Mean','اوسط','اوسط')],sourceGap=dict(note='Redrawn as a coded schematic of the printed figure with three bell curves and leader labels.'))]
eq=[('a',r"\therefore\ Q_2=l_1+\dfrac{h}{f}\left(\dfrac{2\sum f}{4}-c\right)=39.5+\dfrac{5}{235}(500-495)=39.5+\dfrac{25}{235}","∴ Q2 = l1 + (h/f)(2Σf/4 − c) = 39.5 + (5/235)(500 − 495) = 39.5 + 25/235",E28),
 ('b',r"=39.5+0.1064=39.61","= 39.5 + 0.1064 = 39.61",E28),
 ('c',r"Q_3=3\left(\dfrac{\sum f}{4}\right)\text{th value}=3\left(\dfrac{1000}{2}\right)\text{th value}=750\text{ th value}","Q3 = 3(Σf/4)th value = 3(1000/2)th value = 750 th value   [printed denominator 2 in the second form]",E28),
 ('d',r"\therefore\ Q_3=l_1+\dfrac{h}{f}\left(\dfrac{3\sum f}{4}-c\right)","∴ Q3 = l1 + (h/f)(3Σf/4 − c)",E28),
 ('e',r"=44.5+\dfrac{5}{216}(750-730)","= 44.5 + (5/216)(750 − 730)",E28),
 ('f',r"=44.5+\dfrac{100}{216}=44.5+0.463=44.96","= 44.5 + 100/216 = 44.5 + 0.463 = 44.96",E28),
 ('g',r"\text{Hence Sk}=\dfrac{Q_1+Q_3-2Q_2}{Q_3-Q_1}=\dfrac{34.09+44.96-2(39.61)}{44.96-34.09}=\dfrac{-0.17}{10.87}=-0.202","Hence Sk = (Q1 + Q3 − 2Q2)/(Q3 − Q1) = (34.09 + 44.96 − 2(39.61))/(44.96 − 34.09) = −0.17/10.87 = −0.202",E28)]
build(s,143,['E:a','E:b','E:c','a1','E:d','E:e','E:f','E:g','a2','h38','t38','F:0','k1','k2','k3'],eq)
s['sourceNote']='Printed page 135. The first lines complete the Bowley working of Example 3.28. The three kurtosis statements are printed beside the figure and are shown before it. The figure labels "Lepto-kurtic", "Meso-kurtic" (printed "Mcso-kurtic" in the blurred scan), "Platy-kurtic" and "Mean" are redrawn. Header graphics and watermark excluded.'
s['vocabulary']={'kurtosis':dict(ur='نوکیلا پن',ps='تېزوالی')}
save(s)
# ---------- scan 144 (printed 136) ----------
s=page(144,U,'136','3.8.1 Measures of kurtosis · Example 3.29','3.8.1 نوکیلے پن کے پیمانے · مثال 3.29','3.8.1 د تېزوالي اندازې · بېلګه 3.29','kurtosis-2')
Flow(s)
add(s,'c1','It can be easily seen from the figure that lepto-kutic distribution has minimum dispersion which indicates that many values are clustered around the mean.','شکل سے آسانی سے دیکھا جا سکتا ہے کہ لیپٹو کرٹک تقسیم میں کم سے کم انتشار ہوتا ہے جو ظاہر کرتا ہے کہ بہت سی قدریں اوسط کے گرد جمع ہیں۔','له انځور څخه په اسانۍ لیدل کېدای شي چې لېپټو‌کرټیک ویش لږ تر لږه خپراوی لري چې ښيي ډېر ارزښتونه د اوسط شاوخوا راټول دي.')
head(s,'h381','3.8.1 Measures of kurtosis','3.8.1 نوکیلے پن کے پیمانے','3.8.1 د تېزوالي اندازې')
add(s,'t381','Kurtosis can be measured by either of the following two measures.','نوکیلے پن کو درج ذیل دو پیمانوں میں سے کسی ایک سے ناپا جا سکتا ہے۔','تېزوالی د لاندې دوو اندازو له هر یوې څخه اندازه کېدای شي.')
add(s,'m1','(i) Moment ratio','(i) معیارِ اثر کا تناسب','(i) د مومنټ نسبت')
add(s,'k1','If b2 = 3, the distribution is meso-kurtic. b2 < 3, the distribution is platy-kurtic. b2 > 3, the distribution is lepto-kurtic.','اگر b2 = 3 ہو تو تقسیم میسو کرٹک ہے۔ b2 < 3 ہو تو تقسیم پلیٹی کرٹک ہے۔ b2 > 3 ہو تو تقسیم لیپٹو کرٹک ہے۔','که b2 = 3 وي نو ویش میسو‌کرټیک دی. b2 < 3 وي نو ویش پلېټي‌کرټیک دی. b2 > 3 وي نو ویش لېپټو‌کرټیک دی.')
add(s,'m2','(ii) Percentile co-efficient of kurtosis','(ii) نوکیلے پن کا پرسنٹائل عددی سر','(ii) د تېزوالي پرسنټایل ضریب')
add(s,'k2','If K = 0.263, the distribution is meso-kurtic. K < 0.263, the distribution is platy-kurtic. K > 0.263, mean the distribution is lepto-kurtic.','اگر K = 0.263 ہو تو تقسیم میسو کرٹک ہے۔ K < 0.263 ہو تو تقسیم پلیٹی کرٹک ہے۔ K > 0.263 ہو تو مطلب تقسیم لیپٹو کرٹک ہے۔','که K = 0.263 وي نو ویش میسو‌کرټیک دی. K < 0.263 وي نو ویش پلېټي‌کرټیک دی. K > 0.263 وي نو پدې معنا ویش لېپټو‌کرټیک دی.')
head(s,'ex29','Example: 3.29','مثال: 3.29','بېلګه: 3.29',exampleId=E29)
add(s,'q29','The first four moments about x = 17.5 of a certain distribution are 0.3, 74, 45 and 121.25. Find out whether the distribution is lepto-kurtic, platy-kurtic or meso-kurtic.','کسی تقسیم کے x = 17.5 کے گرد پہلے چار معیارِ اثر 0.3, 74, 45 اور 121.25 ہیں۔ معلوم کریں کہ تقسیم لیپٹو کرٹک، پلیٹی کرٹک یا میسو کرٹک ہے۔','د یو ویش د x = 17.5 شاوخوا لومړي څلور مومنټونه 0.3, 74, 45 او 121.25 دي. ومومئ چې ویش لېپټو‌کرټیک، پلېټي‌کرټیک که میسو‌کرټیک دی.',role='question',exampleId=E29)
head(s,'sol29','Solution:','حل:','حل:',exampleId=E29)
add(s,'g1',"Given that m′1 = 0.3, m′2 = 74, m′3 = 45, m′4 = 121.25",'دیا گیا ہے کہ m′1 = 0.3, m′2 = 74, m′3 = 45, m′4 = 121.25','ورکړل شوي دي چې m′1 = 0.3, m′2 = 74, m′3 = 45, m′4 = 121.25',role='solution',exampleId=E29)
add(s,'g2','The second and fourth moments about mean are:','اوسط کے گرد دوسرا اور چوتھا معیارِ اثر یہ ہیں:','د اوسط شاوخوا دویم او څلورم مومنټونه دا دي:',role='solution',exampleId=E29,sourceGap=dict(note='The m4 working continues on the next page.'))
eq=[('b',r"b_2=\dfrac{m_4}{m_2^2}","b2 = m4/m2²",None),
 ('K',r"K=\dfrac{\text{Q.D}}{P_{90}-P_{10}},\qquad 0<K<0.5","K = Q.D/(P90 − P10),   0 < K < 0.5",None),
 ('em2',r"m_2=m_2'-(m_1')^2=74-(0.3)^2=74-0.09=73.91","m2 = m′2 − (m′1)² = 74 − (0.3)² = 74 − 0.09 = 73.91",E29),
 ('m4a',r"m_4=m_4'-4m_1'm_3'+6(m_1')^2m_2'-3(m_1')^4","m4 = m′4 − 4m′1m′3 + 6(m′1)²m′2 − 3(m′1)⁴",E29),
 ('m4b',r"=121.25-4(0.3)(45)+6(0.3)^2(74)-3(0.3)^4","= 121.25 − 4(0.3)(45) + 6(0.3)²(74) − 3(0.3)⁴",E29)]
build(s,144,['c1','h381','t381','m1','E:b','k1','m2','E:K','k2','ex29','q29','sol29','g1','g2','E:em2','E:m4a','E:m4b'],eq)
s['sourceNote']='Printed page 136. Printed spellings kept: "lepto-kutic" and "mean the distribution is lepto-kurtic". The conditions after each measure are printed as three stacked lines each and are joined in one paragraph per measure. A black mark at the top-left corner is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 145 (printed 137) ----------
s=page(145,U,'137','Example 3.29 (end) · Example 3.30: kurtosis conditions','مثال 3.29 (اختتام) · مثال 3.30: نوکیلے پن کی شرائط','بېلګه 3.29 (پای) · بېلګه 3.30: د تېزوالي شرطونه','kurtosis-3')
Flow(s)
add(s,'a1','To test the kurtosis of this distribution we compute','اس تقسیم کے نوکیلے پن کو جانچنے کے لیے ہم حساب کرتے ہیں','د دې ویش د تېزوالي د ازموینې لپاره موږ محاسبه کوو',role='solution',exampleId=E29)
add(s,'a2','⇒ The given distribution is platy-kurtic.','⇒ دی گئی تقسیم پلیٹی کرٹک ہے۔','⇒ ورکړل شوی ویش پلېټي‌کرټیک دی.',role='solution',exampleId=E29)
head(s,'ex30','Example: 3.30','مثال: 3.30','بېلګه: 3.30',exampleId=E30)
add(s,'q30','The second moment about the mean of a symmetrical distribution is 3.5. What must be the value of the fourth moment about the mean in order that the distribution be (i) lepto-kurtic (ii) mesto-kurtic (iii) platy- kurtic.','ایک متناسب تقسیم کا اوسط کے گرد دوسرا معیارِ اثر 3.5 ہے۔ اوسط کے گرد چوتھے معیارِ اثر کی قدر کیا ہونی چاہیے تاکہ تقسیم (i) لیپٹو کرٹک (ii) میسو کرٹک (iii) پلیٹی کرٹک ہو۔','د یوه متناسب ویش د اوسط شاوخوا دویم مومنټ 3.5 دی. د اوسط شاوخوا د څلورم مومنټ ارزښت باید څومره وي چې ویش (i) لېپټو‌کرټیک (ii) میسو‌کرټیک (iii) پلېټي‌کرټیک شي.',role='question',exampleId=E30)
head(s,'sol30','Solution:','حل:','حل:',exampleId=E30)
add(s,'b1','(i) For lepto-kurtic distribution','(i) لیپٹو کرٹک تقسیم کے لیے','(i) د لېپټو‌کرټیک ویش لپاره',role='solution',exampleId=E30)
add(s,'b2','(ii) For meso-kurtic distribution','(ii) میسو کرٹک تقسیم کے لیے','(ii) د میسو‌کرټیک ویش لپاره',role='solution',exampleId=E30)
add(s,'b3','(iii) For platy-kurtic distribution','(iii) پلیٹی کرٹک تقسیم کے لیے','(iii) د پلېټي‌کرټیک ویش لپاره',role='solution',exampleId=E30,sourceGap=dict(note='The page number at the bottom is partly cut off by the scan.'))
eq=[('m4',r"=121.25-54+39.96-0.0243=161.21-54.0243","= 121.25 − 54 + 39.96 − 0.0243 = 161.21 − 54.0243",E29),
 ('m4b',r"=107.1857","= 107.1857",E29),
 ('bb2',r"b_2=\dfrac{m_4}{m_2^2}=\dfrac{107.1857}{(73.91)^2}=\dfrac{107.1857}{5462.6881}=0.02\ \text{which is less than }3.","b2 = m4/m2² = 107.1857/(73.91)² = 107.1857/5462.6881 = 0.02 which is less than 3.",E29),
 ('l1',r"b_2>3","b2 > 3",E30),
 ('l2',r"\text{or}\ \ \dfrac{m_4}{m_2^2}>3","or m4/m2² > 3",E30),
 ('l3',r"\text{or}\ \ m_4>3m_2^2>3(3.5)^2>36.75","or m4 > 3m2² > 3(3.5)² > 36.75",E30),
 ('e1',r"b_2=3","b2 = 3",E30),
 ('e2',r"\text{or}\ \ \dfrac{m_4}{m_2^2}=3","or m4/m2² = 3",E30),
 ('e3',r"\text{or}\ \ m_4=3m_2^2=3(3.5)^2=36.75","or m4 = 3m2² = 3(3.5)² = 36.75",E30),
 ('p1',r"b_2<3","b2 < 3",E30),
 ('p2',r"\text{or}\ \ \dfrac{m_4}{m_2^2}<3","or m4/m2² < 3",E30),
 ('p3',r"\text{or}\ \ m_4<3m_2^2<3(3.5)^2<36.75","or m4 < 3m2² < 3(3.5)² < 36.75",E30)]
build(s,145,['E:m4','E:m4b','a1','E:bb2','a2','ex30','q30','sol30','b1','E:l1','E:l2','E:l3','b2','E:e1','E:e2','E:e3','b3','E:p1','E:p2','E:p3'],eq)
s['sourceNote']='Printed page 137. The first lines complete the m4 working of Example 3.29 (161.21 − 54.0243 is printed; the result 107.1857 is kept). Printed spellings kept: "mesto-kurtic" in the question. The page number at the bottom is partly cut off. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 146 (printed 138) ----------
s=page(146,U,'138','Key points of Unit 3','یونٹ 3 کے اہم نکات','د دریم واحد مهم ټکي','key-points')
Flow(s)
head(s,'h','Key points','اہم نکات','مهم ټکي')
L(s,[('k1','The difference between values of a variable around an average value is called dispersion.','کسی اوسط قدر کے گرد متغیر کی قدروں کے درمیان فرق انتشار کہلاتا ہے۔','د یوه اوسط ارزښت شاوخوا د متغیر د ارزښتونو ترمنځ توپیر خپراوی بلل کېږي.'),
 ('k2','The difference between largest and smallest observations in a data set is called range.','اعداد و شمار کے مجموعے میں سب سے بڑے اور سب سے چھوٹے مشاہدات کا فرق حد (رینج) کہلاتا ہے۔','په معلوماتو ټولګه کې د تر ټولو لوی او تر ټولو کوچني کتنو توپیر رېنج بلل کېږي.'),
 ('k3','The difference between third and first quartiles divided by 2 is called quartile deviation.','تیسری اور پہلی چوتھائی کے فرق کو 2 پر تقسیم کرنا چوتھائی انحراف کہلاتا ہے۔','د دریمې او لومړۍ څلورمې توپیر چې پر 2 وویشل شي څلورمه انحراف بلل کېږي.'),
 ('k4','The arithmetic mean of the absolute or mod deviations of observations taken from mean or median or mode is called mean deviation.','اوسط یا وسطانیہ یا عادہ سے لیے گئے مشاہدات کے مطلق یا ماڈ انحرافات کا حسابی اوسط اوسط انحراف کہلاتا ہے۔','د اوسط یا میانې یا مود څخه اخیستل شویو کتنو د مطلقو یا مود انحرافاتو حسابي اوسط اوسط انحراف بلل کېږي.'),
 ('k5','The positive square root of the average of the squared deviations of observations taken from mean is called standard deviation.','اوسط سے لیے گئے مشاہدات کے مربع انحرافات کے اوسط کا مثبت جذر معیاری انحراف کہلاتا ہے۔','له اوسط څخه اخیستل شویو کتنو د مربع انحرافاتو د اوسط مثبت جذر معیاري انحراف بلل کېږي.')],'unit3-key-points-1')
add(s,'l1','Population standard deviation: (Parameter)','آبادی کا معیاری انحراف: (پیرامیٹر)','د ټولنې معیاري انحراف: (پارامېټر)',listGroup='unit3-key-points-2')
add(s,'l2','Sample standard deviation (biased): (Statistic)','نمونے کا معیاری انحراف (متعصب): (شماریہ)','د نمونې معیاري انحراف (تعصب لرونکی): (احصایه)',listGroup='unit3-key-points-2')
add(s,'l3','Sample standard deviation (unbiased): (Statistic)','نمونے کا معیاری انحراف (غیر متعصب): (شماریہ)','د نمونې معیاري انحراف (بې‌تعصبه): (احصایه)',listGroup='unit3-key-points-2')
L(s,[('k6','Variance is the square of the S.D.','تغیر S.D کا مربع ہے۔','وریانس د S.D مربع دی.'),
 ('k7','The ratio of S.D and the mean expressed in percentage is called coefficient of variation.','S.D اور اوسط کی نسبت جو فیصد میں ظاہر کی جائے تغیر کا عددی سر کہلاتی ہے۔','د S.D او اوسط نسبت چې په سلنه کې ښودل شي د تغیر ضریب بلل کېږي.'),
 ('k8','The lack of symmetry is called skewness.','تشاکل کی کمی کو کجی کہتے ہیں۔','د تناسب نشتوالی ته کوړوالی ویل کېږي.')],'unit3-key-points-3')
add(s,'p','The Pearsonian coefficient of skewness,','کجی کا پیئرسنی عددی سر،','د کوړوالي پیرسني ضریب،',listGroup='unit3-key-points-4')
add(s,'b','The Bowley coefficient of skewness','کجی کا باؤلے عددی سر','د کوړوالي بولي ضریب',listGroup='unit3-key-points-4')
add(s,'k9','Kurtosis means the peakedness or flatness of the graph of a frequency distribution as compared to the normal curve.','نوکیلا پن تعدد تقسیم کے گراف کا نارمل منحنی کے مقابلے میں نوکیلا یا چپٹا ہونا ہے۔','تېزوالی د فریکونسي ویش د ګراف د نورمال منحني په پرتله تېز یا چپټ والی دی.',listGroup='unit3-key-points-5')
eq=[('s1',r"\sigma=\sqrt{\dfrac{\sum(x-\mu)^2}{N}}\qquad\text{(Parameter)}","σ = √(Σ(x − μ)²/N)   (Parameter)",None),
 ('s2',r"S=\sqrt{\dfrac{\sum(x-\bar{x})^2}{n}}\qquad\text{(Statistic)}","S = √(Σ(x − x̄)²/n)   (Statistic)",None),
 ('s3',r"s=\sqrt{\dfrac{\sum(x-\bar{x})^2}{n-1}}\qquad\text{(Statistic)}","s = √(Σ(x − x̄)²/(n − 1))   (Statistic)",None),
 ('q1',r"Sk=\dfrac{3(Mean-Median)}{S},\qquad -3<Sk<3","Sk = 3(Mean − Median)/S,   −3 < Sk < 3",None),
 ('q2',r"Sk=\dfrac{Q_1+Q_3-2Q_2}{Q_3-Q_1},\qquad -1<Sk<1","Sk = (Q1 + Q3 − 2Q2)/(Q3 − Q1),   −1 < Sk < 1",None)]
build(s,146,['h','k1','k2','k3','k4','k5','l1','E:s1','l2','E:s2','l3','E:s3','k6','k7','k8','p','E:q1','b','E:q2','k9'],eq)
s['sourceNote']='Printed page 138. This page lists the key points of the unit as a bulleted list; each formula bullet is printed as a label with the formula and the word (Parameter) or (Statistic) on the same line. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
