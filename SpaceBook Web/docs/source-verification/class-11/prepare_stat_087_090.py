from statlib import *
c=cell
U='central-tendency'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def L(s,items,group):
    for k,a,b,d in items: add(s,k,a,b,d,listGroup=group)
def axes(W,H):
    return f'<line x1="30" y1="12" x2="30" y2="{H-40}" stroke="#222" stroke-width="1.5"/><line x1="30" y1="{H-40}" x2="{W-70}" y2="{H-40}" stroke="#222" stroke-width="1.5"/>'
def sym():
    W,H=420,190
    o=axes(W,H)+'<path d="M40,148 C70,146 100,70 190,22 C280,70 310,146 340,148" fill="none" stroke="#1c6aa8" stroke-width="2"/><line x1="190" y1="22" x2="190" y2="150" stroke="#1c6aa8" stroke-width="2"/><circle cx="190" cy="150" r="4" fill="#1c6aa8"/>'
    o+=T(W-45,154,'Variable',12,'start')+f'<text transform="translate(12 80) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">Frequency</text>'+T(190,176,'Mean = Median = Mode',13)
    return svg(W,H,'Symmetrical frequency curve with mean, median and mode coinciding at the centre',o)
def skew(pos):
    W,H=420,190
    o=axes(W,H)
    if pos:
        o+='<path d="M40,148 C60,100 70,40 105,24 C150,22 170,90 250,128 C300,142 340,146 390,146" fill="none" stroke="#1c6aa8" stroke-width="2"/>'
        pts=[(105,24,'Mode',-10),(160,72,'Median',10),(215,112,'Mean',22)]
    else:
        o+='<path d="M40,148 C100,146 180,118 240,62 C265,42 285,26 300,24 C340,26 360,100 390,148" fill="none" stroke="#1c6aa8" stroke-width="2"/>'
        pts=[(190,100,'Mean',0),(245,58,'Median',18),(300,24,'Mode',0)]
    for x,y,t,dy in pts: o+=f'<line x1="{x}" y1="{y}" x2="{x}" y2="{H-40}" stroke="#1c6aa8" stroke-width="1.8"/><circle cx="{x}" cy="{H-40}" r="3" fill="#1c6aa8"/>'+T(x,H-24+ (10 if t=='Median' else 0),t,11)
    return svg(W,H,('Positively skewed' if pos else 'Negatively skewed')+' curve with mode, median and mean marked on the x-axis in the order '+('mode, median, mean' if pos else 'mean, median, mode'),o)
# ---------- scan 87 (printed 79) ----------
s=page(87,U,'79','2.4.6 table · 2.4.7 Empirical relationship among mean, median and mode · 2.5 Geometric mean','2.4.6 جدول · 2.4.7 اوسط، وسطانیہ اور عادہ کے درمیان تجرباتی تعلق · 2.5 ہندسی اوسط','2.4.6 جدول · 2.4.7 د اوسط، میانې او مود ترمنځ تجربوي اړیکه · 2.5 هندسي اوسط','empirical-gm-start')
F=Flow(s)
s['tables']=[table('Data level and the average to be used','اعداد و شمار کی سطح اور استعمال ہونے والا اوسط','د معلوماتو کچه او کارېدونکی اوسط',[c('Data level','اعداد و شمار کی سطح','د معلوماتو کچه'),c('Average to be used','استعمال ہونے والا اوسط','کارېدونکی اوسط')],[[c('Nominal','اسمی','نومي'),c('Mode','عادہ','مود')],[c('Ordinal','ترتیبی','ترتیبي'),c('Mode, median','عادہ، وسطانیہ','مود، میانه')],[c('Interval','وقفہ جاتی','انټروال'),c('Mode, median and mean','عادہ، وسطانیہ اور اوسط','مود، میانه او اوسط')],[c('Ratio','تناسبی','تناسبي'),c('Mode, median and mean','عادہ، وسطانیہ اور اوسط','مود، میانه او اوسط')]])]
F.tb(0)
head(s,'h247','2.4.7 Empirical relationship among mean, median and mode','2.4.7 اوسط، وسطانیہ اور عادہ کے درمیان تجرباتی تعلق','2.4.7 د اوسط، میانې او مود ترمنځ تجربوي اړیکه')
add(s,'t247','Knowing the values of mean, median and mode can give us some idea about the shape of a frequency distribution.','اوسط، وسطانیہ اور عادہ کی قدریں جاننا ہمیں تعدد تقسیم کی شکل کے بارے میں کچھ اندازہ دے سکتا ہے۔','د اوسط، میانې او مود د ارزښتونو پېژندل موږ ته د فریکونسي ویش د بڼې په اړه یو څه اټکل راکولای شي.')
add(s,'s1','(i) For symmetrical distribution the values of mean, median and mode are identical and they lie at the centre of the distribution.','(i) متناسب تقسیم کے لیے اوسط، وسطانیہ اور عادہ کی قدریں یکساں ہوتی ہیں اور وہ تقسیم کے مرکز میں واقع ہوتی ہیں۔','(i) د متناسب ویش لپاره د اوسط، میانې او مود ارزښتونه یو شان وي او د ویش په مرکز کې پراته وي.')
add(s,'s2','(ii) For asymmetrical or moderately skewed distributions like;','(ii) غیر متناسب یا اعتدال سے کج تقسیمات کے لیے جیسے؛','(ii) د غیرمتناسبو یا منځني کوړو ویشونو لپاره لکه؛')
add(s,'s3','Using this relation if any two measures are known then the third one can be evaluated approximately. Note that this relation does not hold in case of extremely skewed distributions.','اس تعلق کو استعمال کرتے ہوئے اگر کوئی دو پیمانے معلوم ہوں تو تیسرا تقریباً معلوم کیا جا سکتا ہے۔ نوٹ کریں کہ یہ تعلق انتہائی کج تقسیمات کی صورت میں برقرار نہیں رہتا۔','د دې اړیکې په کارولو سره که هر دوه اندازې معلومې وي نو دریمه نږدې ټاکل کېدای شي. یادونه وکړئ چې دا اړیکه د ډېرو کوړو ویشونو په حالت کې نه پاتې کېږي.')
head(s,'h25','2.5 Geometric mean','2.5 ہندسی اوسط','2.5 هندسي اوسط')
add(s,'t25','The nth root of the product of n positive values is called geometric mean. That is,','n مثبت قدروں کے حاصلِ ضرب کا n واں جذر ہندسی اوسط کہلاتا ہے۔ یعنی،','د n مثبتو ارزښتونو د ضرب حاصل n‌م جذر هندسي اوسط بلل کېږي. یعنې،')
s['figures']=[dict(id='stat11-s087-fig1',svg=sym(),caption='Symmetrical distribution: Mean = Median = Mode',captionUrdu='متناسب تقسیم: اوسط = وسطانیہ = عادہ',captionPashto='متناسب ویش: اوسط = میانه = مود',labels=[lab('Frequency','تعدد','فریکونسي'),lab('Variable','متغیر','متغیر')],sourceGap=dict(note='Redrawn as a coded schematic curve.')),
 dict(id='stat11-s087-fig2',svg=skew(True),caption='Positively skewed distribution: Mode < Median < Mean',captionUrdu='مثبت کج تقسیم: عادہ < وسطانیہ < اوسط',captionPashto='مثبت کوړ ویش: مود < میانه < اوسط',labels=[lab('Mode','عادہ','مود'),lab('Median','وسطانیہ','میانه'),lab('Mean','اوسط','اوسط')],sourceGap=dict(note='Redrawn as a coded schematic curve.')),
 dict(id='stat11-s087-fig3',svg=skew(False),caption='Negatively skewed distribution: Mean < Median < Mode',captionUrdu='منفی کج تقسیم: اوسط < وسطانیہ < عادہ',captionPashto='منفي کوړ ویش: اوسط < میانه < مود',labels=[lab('Mean','اوسط','اوسط'),lab('Median','وسطانیہ','میانه'),lab('Mode','عادہ','مود')],sourceGap=dict(note='Redrawn as a coded schematic curve.'))]
s['equations']=[eqn(87,'emp',r'\text{Mode}=3\,\text{Median}-2\,\text{Mean}','Mode = 3Median − 2Mean'),eqn(87,'gm',r'\text{G.M}=\sqrt[n]{x_1\cdot x_2\cdots x_n}=(x_1\cdot x_2\cdots x_n)^{1/n}','G.M = ⁿ√(x1 · x2 ··· xn) = (x1 · x2 ··· xn)^(1/n)')]
F.rest()
s['flow']=[dict(type='table',index=0),dict(type='paragraphs',ids=[pid(87,k) for k in ('h247','t247','s1')]),dict(type='figure',index=0),dict(type='paragraphs',ids=[pid(87,'s2')]),dict(type='figure',index=1),dict(type='figure',index=2),dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(87,k) for k in ('s3','h25','t25')]),dict(type='equation',index=1)]
s['sourceNote']='Printed page 79. The 2.4.6 table of data levels continues from the previous page. The page-number badge at the foot is partly cut off. Header graphics and watermark excluded.'
s['vocabulary']={'geometric mean':dict(ur='ہندسی اوسط',ps='هندسي اوسط')}
save(s)
# ---------- scan 88 (printed 80) ----------
s=page(88,U,'80','Geometric mean: example, logarithm form · 2.5.1 Computation · Example 2.29','ہندسی اوسط: مثال، لوگارتھمی صورت · 2.5.1 حساب · مثال 2.29','هندسي اوسط: بېلګه، لوګارېتمي بڼه · 2.5.1 محاسبه · بېلګه 2.29','gm-1')
F=Flow(s)
head(s,'ex','Example:','مثال:','بېلګه:')
add(s,'t1','G.M of the values 2, 4 and 8 is;','قدروں 2، 4 اور 8 کا ہندسی اوسط ہے؛','د ارزښتونو 2، 4 او 8 هندسي اوسط دی؛')
F.rest()
F.e('e1',r'\text{G.M}=(2\times4\times8)^{1/3}=(64)^{1/3}=(4^3)^{1/3}=4','G.M = (2 × 4 × 8)^(1/3) = (64)^(1/3) = (4³)^(1/3) = 4')
add(s,'t2','G.M by this formula is difficult to calculate when the figures are large in size and greater in number. This can be simplified by using logarithm.','اس فارمولے سے ہندسی اوسط کا حساب اس وقت مشکل ہوتا ہے جب اعداد سائز میں بڑے اور تعداد میں زیادہ ہوں۔ اسے لوگارتھم استعمال کر کے آسان بنایا جا سکتا ہے۔','د دې فورمول په واسطه د هندسي اوسط محاسبه هغه وخت ستونزمنه وي کله چې شمېرې په کچه لوی او په شمېر ډېرې وي. دا د لوګارېتم په کارولو سره ساده کېدای شي.')
F.rest()
F.e('l1',r'\log\text{G.M}=\log(x_1\cdot x_2\cdots x_n)^{1/n}','log G.M = log(x1 · x2 ··· xn)^(1/n)')
F.e('l2',r'=\dfrac{1}{n}\left(\log x_1+\log x_2+\cdots+\log x_n\right)','= (1/n)(log x1 + log x2 + ⋯ + log xn)')
F.e('l3',r'=\dfrac{1}{n}\left(\sum_{i=1}^{n}\log x_i\right)','= (1/n)(Σ (i = 1 to n) log xi)')
add(s,'t3','Taking antilog on both sides','دونوں اطراف کا اینٹی لوگ لیتے ہوئے','په دواړو خواوو انټي‌لوګ اخیستلو سره')
F.rest()
F.e('f1',r'\text{G.M}=\text{antilog}\left(\dfrac{\sum_{i=1}^{n}\log x}{n}\right)\qquad\text{(Formula for ungrouped data)}','G.M = antilog((Σ (i = 1 to n) log x)/n)   (Formula for ungrouped data)')
F.e('f2',r'=\text{antilog}\left(\dfrac{\sum_{i=1}^{n}f\log x}{n}\right)\qquad\text{(Formula for grouped data)}','= antilog((Σ (i = 1 to n) f log x)/n)   (Formula for grouped data)')
add(s,'t4','It is a mathematical average and is an appropriate average to use for the data relating to proportions, ratios, and rate of increase, rate of growth, percentages and index numbers.','یہ ایک ریاضیاتی اوسط ہے اور تناسب، شرحوں، اضافے کی شرح، نمو کی شرح، فیصد اور اشاریہ اعداد سے متعلق اعداد و شمار کے لیے استعمال کرنے کے لیے موزوں اوسط ہے۔','دا یو ریاضیاتي اوسط دی او د تناسبونو، نسبتونو، د زیاتوالي کچې، د ودې کچې، سلنو او شاخصي شمېرو پورې اړوندو معلوماتو لپاره د کارولو مناسب اوسط دی.')
head(s,'h251','2.5.1 Computation of geometric mean','2.5.1 ہندسی اوسط کا حساب','2.5.1 د هندسي اوسط محاسبه')
add(s,'i1','(i) Geometric mean in case of individual series or ungrouped data','(i) انفرادی سلسلے یا غیر گروہی اعداد و شمار کی صورت میں ہندسی اوسط','(i) د انفرادي لړۍ یا نه‌ګروپ شویو معلوماتو په حالت کې هندسي اوسط')
head(s,'ex29','Example: 2.29','مثال: 2.29','بېلګه: 2.29',exampleId='stat11-ex-2-29')
add(s,'q29','Calculate geometric mean for the data: 50, 51, 52, 53, and 54.','اعداد و شمار 50, 51, 52, 53 اور 54 کے لیے ہندسی اوسط حساب کریں۔','د معلوماتو 50, 51, 52, 53 او 54 لپاره هندسي اوسط محاسبه کړئ.',role='question',exampleId='stat11-ex-2-29')
head(s,'sol29','Solution:','حل:','حل:',exampleId='stat11-ex-2-29')
s['tables']=[table('Example 2.29: x and log x','مثال 2.29: x اور log x','بېلګه 2.29: x او log x',[c('x'),c('log x')],[[c(a),c(b)] for a,b in [('50','1.6990'),('51','1.7076'),('52','1.7160'),('53','1.7243'),('54','1.7324')]]+[[c('Total','کل','ټول'),c('8.5793')]],exampleId='stat11-ex-2-29',role='solution')]
s['equations']+= [eqn(88,'s',r'\text{G.M}=\text{antilog}\left(\dfrac{\sum_{i=1}^{n}\log x}{n}\right)=\text{antilog}\dfrac{8.5793}{5}=\text{antilog}(1.71586)=51.991','G.M = antilog((Σ (i = 1 to n) log x)/n) = antilog(8.5793/5) = antilog(1.71586) = 51.991',exampleId='stat11-ex-2-29')]
F.rest()
ids=[p['id'] for p in s['paras']]
s['flow']=[dict(type='paragraphs',ids=[pid(88,'ex'),pid(88,'t1')]),dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(88,'t2')]),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='paragraphs',ids=[pid(88,'t3')]),dict(type='equation',index=4),dict(type='equation',index=5),dict(type='paragraphs',ids=[pid(88,k) for k in ('t4','h251','i1','ex29','q29','sol29')]),dict(type='table',index=0),dict(type='equation',index=6)]
s['sourceNote']='Printed page 80. In the printed table the right-hand working sits beside the table and follows it here. A colour smudge at the top-left is ignored. Header graphics and watermark excluded.'
s['vocabulary']={'antilog':dict(ur='اینٹی لوگ',ps='انټي‌لوګ'),'logarithm':dict(ur='لوگارتھم',ps='لوګارېتم')}
save(s)
# ---------- scan 89 (printed 81) ----------
s=page(89,U,'81','Examples 2.30, 2.31: geometric mean for discrete and continuous series','مثالیں 2.30، 2.31: منفصل اور مسلسل سلسلوں کے لیے ہندسی اوسط','بېلګې 2.30، 2.31: د منفصلې او دوامدارې لړۍ لپاره هندسي اوسط','gm-2')
F=Flow(s)
add(s,'i2','(ii) Geometric mean in case of discrete series or grouped data','(ii) منفصل سلسلے یا گروہی اعداد و شمار کی صورت میں ہندسی اوسط','(ii) د منفصلې لړۍ یا ګروپي معلوماتو په حالت کې هندسي اوسط')
head(s,'ex30','Example: 2.30','مثال: 2.30','بېلګه: 2.30',exampleId='stat11-ex-2-30')
add(s,'q30','Calculate geometric mean of the distribution;','تقسیم کا ہندسی اوسط حساب کریں؛','د ویش هندسي اوسط محاسبه کړئ؛',role='question',exampleId='stat11-ex-2-30')
head(s,'sol30','Solution:','حل:','حل:',exampleId='stat11-ex-2-30')
add(s,'i3','(iii) Geometric mean in case of continuous series or grouped data','(iii) مسلسل سلسلے یا گروہی اعداد و شمار کی صورت میں ہندسی اوسط','(iii) د دوامدارې لړۍ یا ګروپي معلوماتو په حالت کې هندسي اوسط')
head(s,'ex31','Example: 2.31','مثال: 2.31','بېلګه: 2.31',exampleId='stat11-ex-2-31')
add(s,'q31','Calculate the geometric mean of the following distribution.','درج ذیل تقسیم کا ہندسی اوسط حساب کریں۔','د لاندې ویش هندسي اوسط محاسبه کړئ.',role='question',exampleId='stat11-ex-2-31')
head(s,'sol31','Solution:','حل:','حل:',exampleId='stat11-ex-2-31')
s['tables']=[table('Example 2.30: x and f','مثال 2.30: x اور f','بېلګه 2.30: x او f',[c('x:')]+[c(str(v)) for v in [3,4,5,6,7,8,9,10,11]],[[c('f:')]+[c(str(v)) for v in [2,5,9,14,15,8,6,3,1]]],exampleId='stat11-ex-2-30'),
 table('Example 2.30: log x and f log x','مثال 2.30: log x اور f log x','بېلګه 2.30: log x او f log x',[c('x'),c('f'),c('log x'),c('f log x')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in [('3','2','0.4771','0.9542'),('4','5','0.6021','3.0105'),('5','9','0.6990','6.2910'),('6','14','0.7782','10.8948'),('7','15','0.8451','12.6765'),('8','8','0.9031','7.2248'),('9','6','0.9542','5.7252'),('10','3','1.0000','3.000'),('11','1','1.0414','1.0414')]]+[[c('Total','کل','ټول'),c('63'),c('–'),c('50.8184')]],exampleId='stat11-ex-2-30',role='solution'),
 table('Example 2.31: groups and frequency','مثال 2.31: گروہ اور تعدد','بېلګه 2.31: ډلې او فریکونسي',[c('Groups:','گروہ:','ډلې:')]+[c(v) for v in ['10 – 19','20 – 29','30 – 39','40 – 49','50 – 59']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in [15,35,45,25,12]]],exampleId='stat11-ex-2-31'),
 table('Example 2.31: f log x','مثال 2.31: f log x','بېلګه 2.31: f log x',[c('Groups','گروہ','ډلې'),c('f'),c('x'),c('f log x')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in [('10 – 19','15','14.5','17.4205'),('20 – 29','35','24.5','48.6208'),('30 – 39','45','34.5','69.2019'),('40 – 49','25','44.5','41.2090'),('50 – 59','12','54.5','20.8368')]]+[[c('Total','کل','ټول'),c('132'),c('–'),c('197.2890')]],exampleId='stat11-ex-2-31',role='solution')]
s['equations']=[eqn(89,'g1',r'\text{G.M}=\text{antilog}\left(\dfrac{\sum_{i=1}^{n}f\log x}{\sum f}\right)=\text{antilog}\left(\dfrac{50.8184}{63}\right)=\text{antilog}(0.8066)=6.406','G.M = antilog((Σ (i = 1 to n) f log x)/Σf) = antilog(50.8184/63) = antilog(0.8066) = 6.406',exampleId='stat11-ex-2-30'),
 eqn(89,'g2',r'\text{G.M}=\text{antilog}\left(\dfrac{\sum_{i=1}^{n}f\log x}{\sum f}\right)=\text{antilog}\left(\dfrac{197.2890}{132}\right)=\text{antilog}(1.4946)=31.23','G.M = antilog((Σ (i = 1 to n) f log x)/Σf) = antilog(197.2890/132) = antilog(1.4946) = 31.23',exampleId='stat11-ex-2-31')]
F.rest()
s['flow']=[dict(type='paragraphs',ids=[pid(89,k) for k in ('i2','ex30','q30')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(89,'sol30')]),dict(type='table',index=1),dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(89,k) for k in ('i3','ex31','q31')]),dict(type='table',index=2),dict(type='paragraphs',ids=[pid(89,'sol31')]),dict(type='table',index=3),dict(type='equation',index=1)]
s['sourceNote']='Printed page 81. The printed header of the second column of the Example 2.30 solution table is "log x" twice (the second column is f log x); it is read as f log x. The right-hand working is shown after each table. The foot of the scan shows a ghost of another page-number bar ("93"), ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 90 (printed 82) ----------
s=page(90,U,'82','2.5.2 Advantages and disadvantages of geometric mean · 2.6 Harmonic mean · Example 2.32','2.5.2 ہندسی اوسط کے فوائد اور نقصانات · 2.6 ہارمونی اوسط · مثال 2.32','2.5.2 د هندسي اوسط ګټې او زیانونه · 2.6 هارمونیک اوسط · بېلګه 2.32','gm-adv-hm')
F=Flow(s)
head(s,'h252','2.5.2 Advantages and disadvantages of geometric mean.','2.5.2 ہندسی اوسط کے فوائد اور نقصانات۔','2.5.2 د هندسي اوسط ګټې او زیانونه.')
add(s,'ah','Advantages:','فوائد:','ګټې:')
L(s,[('a1','(i) It takes into account all values of a series.','(i) یہ سلسلے کی تمام قدروں کو مدنظر رکھتا ہے۔','(i) دا د لړۍ ټول ارزښتونه په پام کې نیسي.'),('a2','(ii) It gives more weight to smaller values and less weight to larger values. Hence it is a better measure than arithmetic mean.','(ii) یہ چھوٹی قدروں کو زیادہ وزن اور بڑی قدروں کو کم وزن دیتا ہے۔ لہٰذا یہ حسابی اوسط سے بہتر پیمانہ ہے۔','(ii) دا کوچنیو ارزښتونو ته ډېر وزن او لویو ارزښتونو ته لږ وزن ورکوي. نو دا له حسابي اوسط څخه ښه اندازه ده.'),('a3','(iii) It is not affected by fluctuations of sampling.','(iii) یہ نمونہ سازی کے اتار چڑھاؤ سے متاثر نہیں ہوتا۔','(iii) دا د نمونه‌اخیستنې د بدلونونو لخوا نه اغېزمنېږي.')],'gm-adv')
add(s,'dh','Disadvantages:','نقصانات:','زیانونه:')
L(s,[('d1','(i) It is not easy to calculate.','(i) اس کا حساب آسان نہیں۔','(i) محاسبه یې اسانه نه ده.'),('d2','(ii) If one value in the data set is zero, the geometric mean will be zero.','(ii) اگر اعداد و شمار کے مجموعے میں ایک قدر صفر ہو تو ہندسی اوسط صفر ہوگا۔','(ii) که د معلوماتو په ټولګه کې یو ارزښت صفر وي نو هندسي اوسط به صفر وي.'),('d3','(iii) If any one or more values are negative, either geometric mean cannot be calculated or an absurd value will be obtained.','(iii) اگر کوئی ایک یا زیادہ قدریں منفی ہوں تو یا تو ہندسی اوسط حساب نہیں کیا جا سکتا یا ایک بے معنی قدر حاصل ہوگی۔','(iii) که هر یو یا ډېر ارزښتونه منفي وي نو یا هندسي اوسط نشي محاسبه کېدای یا یو بې‌معنا ارزښت به ترلاسه شي.')],'gm-dis')
head(s,'h26','2.6 Harmonic mean','2.6 ہارمونی اوسط','2.6 هارمونیک اوسط')
add(s,'t26','The reciprocal of the arithmetic mean of the reciprocals of the values is called harmonic mean.','قدروں کے معکوسات کے حسابی اوسط کا معکوس ہارمونی اوسط کہلاتا ہے۔','د ارزښتونو د معکوسونو د حسابي اوسط معکوس هارمونیک اوسط بلل کېږي.')
F.rest()
F.e('hm1',r'\text{H.M}=\dfrac{n}{\sum_{i=1}^{n}\dfrac{1}{x_i}}\qquad\text{(Formula for ungrouped data)}','H.M = n / (Σ (i = 1 to n) 1/xi)   (Formula for ungrouped data)')
F.e('hm2',r'=\dfrac{\sum f_i}{\sum_{i=1}^{n}\dfrac{f_i}{x_i}}\qquad\text{(Formula for grouped data)}','= (Σ fi) / (Σ (i = 1 to n) fi/xi)   (Formula for grouped data)')
add(s,'t2','It is also mathematical average but not very popular. It is used in those places where largest weight is given to small items. It is suitable for averaging time and speed.','یہ بھی ریاضیاتی اوسط ہے لیکن زیادہ مقبول نہیں۔ یہ ان جگہوں پر استعمال ہوتا ہے جہاں چھوٹی اشیاء کو سب سے زیادہ وزن دیا جاتا ہے۔ یہ وقت اور رفتار کا اوسط نکالنے کے لیے موزوں ہے۔','دا هم ریاضیاتي اوسط دی خو ډېر مشهور نه دی. دا هغو ځایونو کې کارول کېږي چېرته چې کوچنیو توکو ته تر ټولو ډېر وزن ورکول کېږي. دا د وخت او چټکتیا د اوسط اخیستو لپاره مناسب دی.')
head(s,'h261','2.6.1 Calculation of harmonic mean','2.6.1 ہارمونی اوسط کا حساب','2.6.1 د هارمونیک اوسط محاسبه')
add(s,'i1','(i) Harmonic mean in case of individual series or ungrouped data','(i) انفرادی سلسلے یا غیر گروہی اعداد و شمار کی صورت میں ہارمونی اوسط','(i) د انفرادي لړۍ یا نه‌ګروپ شویو معلوماتو په حالت کې هارمونیک اوسط')
head(s,'ex32','Example: 2.32','مثال: 2.32','بېلګه: 2.32',exampleId='stat11-ex-2-32')
add(s,'q32','Five tractors are running at the rate of 10, 20, 30, 40, 50 km/hour respectively. What would be the average speed? Use harmonic mean.','پانچ ٹریکٹر بالترتیب 10, 20, 30, 40, 50 کلومیٹر فی گھنٹہ کی رفتار سے چل رہے ہیں۔ اوسط رفتار کیا ہوگی؟ ہارمونی اوسط استعمال کریں۔','پنځه ټراکټورونه په ترتیب سره 10, 20, 30, 40, 50 کیلومتر په ساعت چټکتیا روان دي. اوسط چټکتیا به څومره وي؟ هارمونیک اوسط وکاروئ.',role='question',exampleId='stat11-ex-2-32',sourceGap=dict(note='The solution of Example 2.32 follows on the next page.'))
F.rest()
ids=[p['id'] for p in s['paras']]
s['flow']=[dict(type='paragraphs',ids=[pid(90,k) for k in ('h252','ah','a1','a2','a3','dh','d1','d2','d3','h26','t26')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='paragraphs',ids=[pid(90,k) for k in ('t2','h261','i1','ex32','q32')])]
s['sourceNote']='Printed page 82. A ghost of the following page-number bar shows at the foot. Header graphics and watermark excluded.'
s['vocabulary']={'harmonic mean':dict(ur='ہارمونی اوسط',ps='هارمونیک اوسط')}
save(s)
