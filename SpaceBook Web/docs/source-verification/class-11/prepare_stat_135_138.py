from stathelp import *
import math
c=cell
U='dispersion-skewness-kurtosis'
E25='stat11-ex-3-25'; E26='stat11-ex-3-26'
RAW4=r"m_4=m_4'-4m_1'm_3'+6(m_1')^2m_2'-3(m_1')^4"; RAW4T="m4 = m′4 − 4m′1m′3 + 6(m′1)²m′2 − 3(m′1)⁴"
RAW3=r"m_3=m_3'-3m_1'm_2'+2(m_1')^3"; RAW3T="m3 = m′3 − 3m′1m′2 + 2(m′1)³"
RAW2=r"m_2=m_2'-(m_1')^2"; RAW2T="m2 = m′2 − (m′1)²"
RAW1=r"m_1=m_1'-m_1'"; RAW1T="m1 = m′1 − m′1"

def skew(positive,aria):
    # gamma(k=3) shape: mode 2, median ~2.674, mean 3 (mirrored for negative skew)
    W,H=440,230; x0,x1=40,400; base=170; top=40
    f=lambda t:(t**2)*math.exp(-t)
    ts=[i*0.1 for i in range(0,101)]
    fx=lambda t:(x0+(x1-x0)*t/10.0) if positive else (x1-(x1-x0)*t/10.0)
    fy=lambda t:base-(base-top)*f(t)/f(2.0)
    pts=' '.join(f'{fx(t):.1f},{fy(t):.1f}' for t in ts)
    o=f'<line x1="{x0-10}" y1="{base}" x2="{x1+20}" y2="{base}" stroke="#1c7ab8" stroke-width="2"/>'
    o+=f'<polyline points="{pts}" fill="none" stroke="#1c7ab8" stroke-width="2.5"/>'
    names=[('Mode',2.0),('Median',2.674),('Mean',3.0)]
    for n,t in names:
        o+=f'<line x1="{fx(t):.1f}" y1="{fy(t):.1f}" x2="{fx(t):.1f}" y2="{base}" stroke="#1c7ab8" stroke-width="2"/>'
    if positive:
        o+=T(fx(2.674),base+22,'Median',15)+T(fx(2.0),base+40,'Mode',12)+T(fx(3.0)+4,base+40,'Mean',12)
    else:
        o+=T(fx(3.0),base+40,'Mean',12)+T(fx(2.674),base+22,'Median',15)+T(fx(2.0),base+40,'Mode',12)
    return svg(W,H,aria,o)

# ---------- scan 135 (printed 127) ----------
s=page(135,U,'127','Example 3.25: moments about mean and corrected moments','مثال 3.25: اوسط کے گرد اور تصحیح شدہ معیارِ اثر','بېلګه 3.25: د اوسط شاوخوا او سمون شوي مومنټونه','moments-14')
Flow(s)
add(s,'f0','Find','معلوم کریں','ومومئ',sourceGap=dict(note='Completes the question of Example 3.25 begun on the previous page.'))
L(s,[('f1','(i) First four moments about mean','(i) اوسط کے گرد پہلے چار معیارِ اثر','(i) د اوسط شاوخوا لومړي څلور مومنټونه'),('f2','(ii) Corrected mean moments','(ii) تصحیح شدہ اوسطی معیارِ اثر','(ii) سمون شوي اوسط مومنټونه'),('f3','(iii) Moment ratios and','(iii) معیارِ اثر کے تناسب اور','(iii) د مومنټ نسبتونه او'),('f4','(iv) Mean, variance and standard deviation','(iv) اوسط، تغیر اور معیاری انحراف','(iv) اوسط، وریانس او معیاري انحراف')],'ex325-find')
head(s,'sol25','Solution:','حل:','حل:',exampleId=E25)
add(s,'g1',"Given that m′1 = 0.45, m′2 = 8.73, m′3 = 12.15, m′4 = 204.93 and a = 35",'دیا گیا ہے کہ m′1 = 0.45, m′2 = 8.73, m′3 = 12.15, m′4 = 204.93 اور a = 35','ورکړل شوي دي چې m′1 = 0.45, m′2 = 8.73, m′3 = 12.15, m′4 = 204.93 او a = 35',role='solution',exampleId=E25)
add(s,'g2','(i) Moments about mean are:','(i) اوسط کے گرد معیارِ اثر یہ ہیں:','(i) د اوسط شاوخوا مومنټونه دا دي:',role='solution',exampleId=E25)
add(s,'g3','(ii)','(ii)','(ii)',role='solution',exampleId=E25)
eq=[('m1',RAW1+r"=0.45-0.45=0",RAW1T+" = 0.45 − 0.45 = 0",E25),
 ('m2',RAW2+r"=8.73-(0.45)^2=8.73-0.2025=8.53",RAW2T+" = 8.73 − (0.45)² = 8.73 − 0.2025 = 8.53",E25),
 ('m3a',RAW3,RAW3T,E25),
 ('m3b',r"=12.15-3(0.45)(8.73)+2(0.45)^3","= 12.15 − 3(0.45)(8.73) + 2(0.45)³",E25),
 ('m3c',r"=12.15-11.7855+0.18225=0.55","= 12.15 − 11.7855 + 0.18225 = 0.55",E25),
 ('m4a',RAW4,RAW4T,E25),
 ('m4b',r"=204.93-4(0.45)(12.15)+6(0.45)^2(8.73)-3(0.45)^4","= 204.93 − 4(0.45)(12.15) + 6(0.45)²(8.73) − 3(0.45)⁴",E25),
 ('m4c',r"=204.93-21.87+10.607-0.1230=193.54","= 204.93 − 21.87 + 10.607 − 0.1230 = 193.54",E25),
 ('c2a',r"m_2(\text{corrected})=m_2(\text{uncorrected})-\dfrac{h^2}{12}","m2(corrected) = m2(uncorrected) − h²/12",E25),
 ('c2b',r"=8.53-\dfrac{(3)^2}{12}","= 8.53 − (3)²/12",E25),
 ('c2c',r"=8.53-\dfrac{9}{12}=8.53-0.75=7.78","= 8.53 − 9/12 = 8.53 − 0.75 = 7.78",E25),
 ('c4a',r"m_4(\text{corrected})=m_4(\text{uncorrected})-\dfrac{h^2}{2}\,m_2(\text{uncorrected})+\dfrac{7}{240}h^4","m4(corrected) = m4(uncorrected) − (h²/2)m2(uncorrected) + (7/240)h⁴",E25),
 ('c4b',r"=193.54-\dfrac{(3)^2}{2}(8.53)+\dfrac{7}{240}(3)^4","= 193.54 − ((3)²/2)(8.53) + (7/240)(3)⁴",E25),
 ('c4c',r"=193.54-38.385+2.3625","= 193.54 − 38.385 + 2.3625",E25),
 ('c4d',r"=195.9065-38.385=157.52","= 195.9065 − 38.385 = 157.52",E25)]
build(s,135,['f0','f1','f2','f3','f4','sol25','g1','g2','E:m1','E:m2','E:m3a','E:m3b','E:m3c','E:m4a','E:m4b','E:m4c','g3','E:c2a','E:c2b','E:c2c','E:c4a','E:c4b','E:c4c','E:c4d'],eq)
s['sourceNote']='Printed page 127. The first lines complete the question of Example 3.25 (the list (i)–(iv) is printed as an indented list). The printed m4 working uses rounded intermediate values (21.87, 10.607, 0.1230). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 136 (printed 128) ----------
s=page(136,U,'128','Example 3.25 (end) · 3.7 Skewness · Positive skewness','مثال 3.25 (اختتام) · 3.7 کجی · مثبت کجی','بېلګه 3.25 (پای) · 3.7 کوړوالی · مثبت کوړوالی','skewness-1')
Flow(s)
add(s,'a1','(iii) Moment ratios are','(iii) معیارِ اثر کے تناسب یہ ہیں','(iii) د مومنټ نسبتونه دا دي',role='solution',exampleId=E25)
add(s,'a2','Moment ratios in standard unit are','معیاری اکائی میں معیارِ اثر کے تناسب یہ ہیں','په معیاري واحد کې د مومنټ نسبتونه دا دي',role='solution',exampleId=E25)
add(s,'a3','(iv) Mean and variance:','(iv) اوسط اور تغیر:','(iv) اوسط او وریانس:',role='solution',exampleId=E25)
head(s,'h37','3.7 Skewness','3.7 کجی','3.7 کوړوالی')
add(s,'t37','The lack of symmetry is called skewness. In a skewed distribution, the observations are not equally distributed around a measure of central tendency i.e. the number of observations to one side of central value is greater than the other. Graphically, the tail to one side will be longer than the other.','تشاکل کی کمی کو کجی کہتے ہیں۔ کج تقسیم میں مشاہدات مرکزی رجحان کے کسی پیمانے کے گرد برابر تقسیم نہیں ہوتے یعنی مرکزی قدر کی ایک طرف مشاہدات کی تعداد دوسری طرف سے زیادہ ہوتی ہے۔ گراف میں ایک طرف کی دم دوسری طرف سے لمبی ہوگی۔','د تناسب نشتوالی ته کوړوالی ویل کېږي. په کوړ ویش کې کتنې د مرکزي تمایل د یوې اندازې شاوخوا مساوي نه وېشل کېږي یعنې د مرکزي ارزښت یوې خوا ته د کتنو شمېر له بلې خوا څخه ډېر وي. په ګراف کې یوې خوا ته لکۍ له بلې خوا څخه اوږده وي.')
add(s,'p1','(i) Positive skewness','(i) مثبت کجی','(i) مثبت کوړوالی')
add(s,'p2','If right hand side tail is longer than the left hand side tail, the distribution is said to have positive skewness i.e.','اگر دائیں طرف کی دم بائیں طرف کی دم سے لمبی ہو تو تقسیم کو مثبت کجی والی کہا جاتا ہے یعنی','که د ښي لوري لکۍ د کیڼ لوري له لکۍ څخه اوږده وي نو ویش ته مثبت کوړوالی لرونکی ویل کېږي یعنې')
add(s,'n1','(ii) Negative skewness','(ii) منفی کجی','(ii) منفي کوړوالی')
add(s,'n2','If left hand side tail is longer than the right hand side tail, the distribution','اگر بائیں طرف کی دم دائیں طرف کی دم سے لمبی ہو تو تقسیم','که د کیڼ لوري لکۍ د ښي لوري له لکۍ څخه اوږده وي نو ویش',sourceGap=dict(note='The sentence continues on the next page ("is said to have negative skewness i.e.").'))
s['figures']=[dict(id='stat11-s136-fig1',svg=skew(True,'Positively skewed distribution with mode, median and mean marked from left to right'),caption='Positively skewed distribution',captionUrdu='مثبت کج تقسیم',captionPashto='مثبت کوړ ویش',labels=[lab('Median','وسطانیہ','میانه'),lab('Mode','عادہ','مود'),lab('Mean','اوسط','اوسط')],sourceGap=dict(note='Redrawn as a coded schematic of the printed curve; the printed caption is "[+ively skewed distribution]".'))]
eq=[('b1',r"b_1=\dfrac{m_3^2}{m_2^3}=\dfrac{(0.547)^2}{(8.53)^3}=\dfrac{0.2992}{620.65}=0.00048","b1 = m3²/m2³ = (0.547)²/(8.53)³ = 0.2992/620.65 = 0.00048",E25),
 ('b2',r"b_2=\dfrac{m_4}{m_2^2}=\dfrac{193.544}{(8.53)^2}=\dfrac{193.544}{72.7605}=2.66","b2 = m4/m2² = 193.544/(8.53)² = 193.544/72.7605 = 2.66",E25),
 ('g1',r"\gamma_1=\sqrt{b_1}=\sqrt{0.00048}=0.02","γ1 = √b1 = √0.00048 = 0.02",E25),
 ('g2',r"\gamma_2=b_2-3=2.66-3=-0.34","γ2 = b2 − 3 = 2.66 − 3 = −0.34",E25),
 ('i1',r"\text{A.M}=\bar{x}=m_1'+a=0.45+35=35.45","A.M = x̄ = m′1 + a = 0.45 + 35 = 35.45",E25),
 ('i2',r"\text{Variance}=S^2=m_2=m_2'-(m_1')^2=8.73-(0.45)^2=8.73-0.2025=8.53","Variance = S² = m2 = m′2 − (m′1)² = 8.73 − (0.45)² = 8.73 − 0.2025 = 8.53",E25),
 ('i3',r"\text{S.D}=S=\sqrt{S^2}=\sqrt{8.53}=2.92","S.D = S = √S² = √8.53 = 2.92",E25)]
build(s,136,['a1','E:b1','E:b2','a2','E:g1','E:g2','a3','E:i1','E:i2','E:i3','h37','t37','p1','p2','F:0','n1','n2'],eq)
s['sourceNote']='Printed page 128. The figure under "Positive skewness" shows a right-tailed curve with the vertical lines Mode, Median and Mean in that order from left to right, captioned "[+ively skewed distribution]". Pen marks at the top-left corner are ignored. Header graphics and watermark excluded.'
s['vocabulary']={'skewness':dict(ur='کجی',ps='کوړوالی')}
save(s)
# ---------- scan 137 (printed 129) ----------
s=page(137,U,'129','Negative skewness (figure) · 3.7.1 Measures of skewness · Example 3.26 (question)','منفی کجی (شکل) · 3.7.1 کجی کے پیمانے · مثال 3.26 (سوال)','منفي کوړوالی (انځور) · 3.7.1 د کوړوالي اندازې · بېلګه 3.26 (پوښتنه)','skewness-2')
Flow(s)
add(s,'c1','is said to have negative skewness i.e.','کو منفی کجی والی کہا جاتا ہے یعنی','ته منفي کوړوالی لرونکی ویل کېږي یعنې',sourceGap=dict(note='Completes the sentence from the previous page ("If left hand side tail is longer than the right hand side tail, the distribution").'))
head(s,'h371','3.7.1 Measures of skewness','3.7.1 کجی کے پیمانے','3.7.1 د کوړوالي اندازې')
add(s,'t371','Skewness can be measured by any of the following formulas.','کجی کو درج ذیل فارمولوں میں سے کسی ایک سے ناپا جا سکتا ہے۔','کوړوالی د لاندې فورمولونو له هر یو څخه اندازه کېدای شي.')
add(s,'m1','(i) The moment ratio','(i) معیارِ اثر کا تناسب','(i) د مومنټ نسبت')
add(s,'m2','(ii) The Pearsonian coefficient of skewness','(ii) کجی کا پیئرسنی عددی سر','(ii) د کوړوالي پیرسني ضریب')
add(s,'m3','(iii) The Bowley coefficient of skewness','(iii) کجی کا باؤلے عددی سر','(iii) د کوړوالي بولي ضریب')
add(s,'n1','For all of the above three formulas if Sk = 0, the distribution is symmetrical. Sk > 0, the distribution is positively skewed. Sk < 0, the distribution is negatively skewed.','مندرجہ بالا تینوں فارمولوں کے لیے اگر Sk = 0 ہو تو تقسیم متناسب ہے۔ Sk > 0 ہو تو تقسیم مثبت کج ہے۔ Sk < 0 ہو تو تقسیم منفی کج ہے۔','د پورتنیو درېیو فورمولونو لپاره که Sk = 0 وي نو ویش متناسب دی. Sk > 0 وي نو ویش مثبت کوړ دی. Sk < 0 وي نو ویش منفي کوړ دی.')
head(s,'ex26','Example: 3.26','مثال: 3.26','بېلګه: 3.26',exampleId=E26)
add(s,'q26','Calculate coefficient of skewness for the data 1, 9, 5, 8 and 7 by, (i) The Karl Pearson\'s method (ii) The Bowley\'s method.','اعداد و شمار 1, 9, 5, 8 اور 7 کے لیے کجی کا عددی سر حساب کریں، (i) کارل پیئرسن کے طریقے سے (ii) باؤلے کے طریقے سے۔','د معلوماتو 1, 9, 5, 8 او 7 لپاره د کوړوالي ضریب محاسبه کړئ، (i) د Karl Pearson په طریقه (ii) د Bowley په طریقه.',role='question',exampleId=E26)
s['figures']=[dict(id='stat11-s137-fig1',svg=skew(False,'Negatively skewed distribution with mean, median and mode marked from left to right'),caption='Negatively skewed distribution',captionUrdu='منفی کج تقسیم',captionPashto='منفي کوړ ویش',labels=[lab('Mean','اوسط','اوسط'),lab('Median','وسطانیہ','میانه'),lab('Mode','عادہ','مود')],sourceGap=dict(note='Redrawn as a coded schematic of the printed curve; the printed caption is "[−ively skewed distribution]".'))]
eq=[('r1',r"\gamma_1=\dfrac{m_3}{m_2^{3/2}}=\dfrac{m_3}{S^3},\qquad -\infty<\gamma_1<\infty","γ1 = m3/m2^(3/2) = m3/S³,   −∞ < γ1 < ∞",None),
 ('r2',r"Sk=\dfrac{3(\text{Mean}-\text{Median})}{S},\qquad -3<Sk<3","Sk = 3(Mean − Median)/S,   −3 < Sk < 3",None),
 ('r3',r"Sk=\dfrac{Q_1+Q_3-2Q_2}{Q_3-Q_1},\qquad -1<Sk<1","Sk = (Q1 + Q3 − 2Q2)/(Q3 − Q1),   −1 < Sk < 1",None)]
build(s,137,['c1','F:0','h371','t371','m1','E:r1','m2','E:r2','m3','E:r3','n1','ex26','q26'],eq)
s['sourceNote']='Printed page 129. The figure under "Negative skewness" shows a left-tailed curve with Mean, Median and Mode marked from left to right, captioned "[−ively skewed distribution]". The conditions for Sk are printed as three lines (= 0, > 0, < 0) and are joined in one paragraph. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 138 (printed 130) ----------
s=page(138,U,'130','Example 3.26: solution (Karl Pearson and Bowley methods)','مثال 3.26: حل (کارل پیئرسن اور باؤلے کے طریقے)','بېلګه 3.26: حل (د Karl Pearson او Bowley طریقې)','skewness-3')
Flow(s)
head(s,'sol26','Solution:','حل:','حل:',exampleId=E26)
add(s,'a1',"(i) Karl Pearson's method",'(i) کارل پیئرسن کا طریقہ','(i) د Karl Pearson طریقه',role='solution',exampleId=E26)
add(s,'a2','Since n = 5 is odd therefore Median = ((n + 1)/2)th value = ((5 + 1)/2)th value = 3rd value = 7','چونکہ n = 5 طاق ہے اس لیے وسطانیہ = ((n + 1)/2)ویں قدر = ((5 + 1)/2)ویں قدر = تیسری قدر = 7','ځکه چې n = 5 طاق دی نو میانه = ((n + 1)/2) ارزښت = ((5 + 1)/2) ارزښت = دریم ارزښت = 7',role='solution',exampleId=E26)
add(s,'a3','It means that given distribution of values is −vely skewed.','اس کا مطلب ہے کہ قدروں کی دی گئی تقسیم منفی کج ہے۔','دا پدې معنا ده چې د ارزښتونو ورکړل شوی ویش منفي کوړ دی.',role='solution',exampleId=E26)
add(s,'a4',"(ii) Bowley's method",'(ii) باؤلے کا طریقہ','(ii) د Bowley طریقه',role='solution',exampleId=E26)
s['tables']=[table('Example 3.26: deviations from the mean','مثال 3.26: اوسط سے انحرافات','بېلګه 3.26: له اوسط څخه انحرافات',[c('x'),c('(x − x̄)'),c('(x − x̄)²')],[[c(str(a)),c(str(b)),c(str(d))] for a,b,d in [(1,-5,25),(5,-1,1),(7,1,1),(8,2,4),(9,3,9)]]+[[c('Total 30','میزان 30','ټولیز 30'),c('0'),c('40')]],exampleId=E26)]
eq=[('p0',r"Sk=\dfrac{3(Mean-Median)}{S}","Sk = 3(Mean − Median)/S",E26),
 ('p1',r"\bar{x}=\dfrac{\sum x}{n}=\dfrac{30}{5}=6","x̄ = Σx/n = 30/5 = 6",E26),
 ('p2',r"s=\sqrt{\dfrac{\sum(x-\bar{x})^2}{n-1}}=\sqrt{\dfrac{40}{5-1}}=\sqrt{\dfrac{40}{4}}=3.16","s = √(Σ(x − x̄)²/(n − 1)) = √(40/(5 − 1)) = √(40/4) = 3.16",E26),
 ('p3',r"\therefore\ Sk=\dfrac{3(6-7)}{3.16}=\dfrac{-3}{3.16}=-0.95","∴ Sk = 3(6 − 7)/3.16 = −3/3.16 = −0.95",E26),
 ('b0',r"Sk=\dfrac{Q_1+Q_3-2Q_2}{Q_3-Q_1}","Sk = (Q1 + Q3 − 2Q2)/(Q3 − Q1)",E26),
 ('b1',r"Q_1=\left(\dfrac{n+1}{4}\right)\text{th value}=\left(\dfrac{5+1}{4}\right)\text{th value}=(1.5)\text{th value}","Q1 = ((n + 1)/4)th value = ((5 + 1)/4)th value = (1.5)th value",E26),
 ('b2',r"=1\text{st value}+0.5(2\text{nd value}-1\text{st value})","= 1st value + 0.5(2nd value − 1st value)",E26),
 ('b3',r"=1+0.5(5-1)=1+0.5(4)=1+2=3","= 1 + 0.5(5 − 1) = 1 + 0.5(4) = 1 + 2 = 3",E26),
 ('b4',r"Q_2=2\left(\dfrac{n+1}{4}\right)\text{th value}=\left(\dfrac{n+1}{2}\right)\text{th value}=\left(\dfrac{5+1}{2}\right)\text{th value}=3\text{rd value}=7","Q2 = 2((n + 1)/4)th value = ((n + 1)/2)th value = ((5 + 1)/2)th value = 3rd value = 7",E26),
 ('b5',r"Q_3=3\left(\dfrac{n+1}{4}\right)\text{th value}=3\left(\dfrac{5+1}{4}\right)\text{th value}=(4.5)\text{th value}","Q3 = 3((n + 1)/4)th value = 3((5 + 1)/4)th value = (4.5)th value",E26),
 ('b6',r"=4\text{th value}+0.5(5\text{th value}-4\text{th value})","= 4th value + 0.5(5th value − 4th value)",E26),
 ('b7',r"=8+0.5(9-8)","= 8 + 0.5(9 − 8)",E26),
 ('b8',r"=8+0.5=8.5","= 8 + 0.5 = 8.5",E26)]
build(s,138,['sol26','a1','E:p0','T:0','E:p1','a2','E:p2','E:p3','a3','a4','E:b0','E:b1','E:b2','E:b3','E:b4','E:b5','E:b6','E:b7','E:b8'],eq)
s['sourceNote']='Printed page 130. The table lists the data in ascending order (1, 5, 7, 8, 9); the mean is printed to its right and is shown after the table. The Bowley working continues on the next page. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
