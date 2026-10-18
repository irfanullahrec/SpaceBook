from stathelp import *
c=cell
U='dispersion-skewness-kurtosis'
E12='stat11-ex-3-12'; E13='stat11-ex-3-13'
# ---------- scan 115 (printed 107) ----------
s=page(115,U,'107','Example 3.12 (shortcut and step-deviation methods) · 3.5.5 Example 3.13 (question)','مثال 3.12 (مختصر اور قدمی انحراف کے طریقے) · 3.5.5 مثال 3.13 (سوال)','بېلګه 3.12 (لنډه او ګام‌انحراف طریقې) · 3.5.5 بېلګه 3.13 (پوښتنه)','sd-6')
Flow(s)
add(s,'n1','Now','اب','اوس',role='solution',exampleId=E12)
add(s,'n2','and','اور','او',role='solution',exampleId=E12)
add(s,'n3','(iii) By change of origin and scale method or step-deviation method','(iii) مبدا اور پیمانے کی تبدیلی کے طریقے یا قدمی انحراف کے طریقے سے','(iii) د اصل او پیمانې د بدلون طریقې یا ګام‌انحراف طریقې په واسطه',role='solution',exampleId=E12)
add(s,'n4','Here A = 3, h = 1, u = (x − A)/h = (x − 3)/1','یہاں A = 3, h = 1, u = (x − A)/h = (x − 3)/1','دلته A = 3, h = 1, u = (x − A)/h = (x − 3)/1',role='solution',exampleId=E12)
head(s,'h355','3.5.5 Calculation of standard deviation and variance in case of continuous series of grouped data','3.5.5 مسلسل سلسلے کے گروہی اعداد و شمار کی صورت میں معیاری انحراف اور تغیر کا حساب','3.5.5 د دوامدارې لړۍ د ګروپي معلوماتو په حالت کې د معیاري انحراف او وریانس محاسبه')
head(s,'ex13','Example: 3.13','مثال: 3.13','بېلګه: 3.13',exampleId=E13)
add(s,'q13','Find standard deviation and variance for the following frequency distribution.','درج ذیل تعدد تقسیم کے لیے معیاری انحراف اور تغیر معلوم کریں۔','د لاندې فریکونسي ویش لپاره معیاري انحراف او وریانس ومومئ.',role='question',exampleId=E13,sourceGap=dict(note='The data of Example 3.13 are printed at the top of the next page.'))
s['tables']=[table('Example 3.12: x, f, fx, fx²','مثال 3.12: x, f, fx, fx²','بېلګه 3.12: x, f, fx, fx²',[c('x'),c('f'),c('fx'),c('fx²')],[[c(str(a)),c(str(b)),c(str(d)),c(str(e))] for a,b,d,e in [(1,5,5,5),(2,10,20,40),(3,15,45,135),(4,12,48,192),(5,8,40,200)]]+[[c('Total','میزان','ټولیز'),c('50'),c('158'),c('572')]],exampleId=E12),
 table('Example 3.12: step-deviation table','مثال 3.12: قدمی انحراف کا جدول','بېلګه 3.12: د ګام‌انحراف جدول',[c('x'),c('f'),c('u = (x − 3)/1'),c('u²'),c('fu'),c('fu²')],[[c(str(a)),c(str(b)),c(str(d)),c(str(e)),c(str(g)),c(str(h))] for a,b,d,e,g,h in [(1,5,-2,4,-10,20),(2,10,-1,1,-10,10),(3,15,0,0,0,0),(4,12,1,1,12,12),(5,8,2,4,16,32)]]+[[c('Total','میزان','ټولیز'),c('50'),c('0'),c('–'),c('8'),c('74')]],exampleId=E12)]
eq=[('a',r'S=\sqrt{\dfrac{572}{50}-\left(\dfrac{158}{50}\right)^2}','S = √(572/50 − (158/50)²)',E12),
 ('b',r'=\sqrt{11.44-9.9856}=1.21','= √(11.44 − 9.9856) = 1.21',E12),
 ('c',r'S^2=\dfrac{572}{50}-\left(\dfrac{158}{50}\right)^2','S² = 572/50 − (158/50)²',E12),
 ('d',r'=11.44-9.9856=1.4544','= 11.44 − 9.9856 = 1.4544',E12),
 ('e',r's=\sqrt{\dfrac{\sum fu^2}{\sum f}-\left(\dfrac{\sum fu}{\sum f}\right)^2}\times h','s = √(Σfu²/Σf − (Σfu/Σf)²) × h',E12),
 ('f',r's^2=\left[\dfrac{\sum fu^2}{\sum f}-\left(\dfrac{\sum fu}{\sum f}\right)^2\right]\times h^2','s² = [Σfu²/Σf − (Σfu/Σf)²] × h²',E12),
 ('g',r'S=\sqrt{\dfrac{74}{50}-\left(\dfrac{8}{50}\right)^2}\times 1=\sqrt{1.48-0.0256}\times 1=1.21','S = √(74/50 − (8/50)²) × 1 = √(1.48 − 0.0256) × 1 = 1.21',E12),
 ('h',r'S^2=\left[\dfrac{74}{50}-\left(\dfrac{8}{50}\right)^2\right]\times 1=1.48-0.0256=1.4544','S² = [74/50 − (8/50)²] × 1 = 1.48 − 0.0256 = 1.4544',E12)]
build(s,115,['T:0','n1','E:a','E:b','n2','E:c','E:d','n3','E:e','E:f','T:1','n4','E:g','E:h','h355','ex13','q13'],eq)
s['sourceNote']='Printed page 107. The x, f, fx, fx² table and the "Now … and …" workings are printed side by side and are shown table first. In the printed S² line of the step-deviation method the closing "× 1" and the bracket are placed as printed. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 116 (printed 108) ----------
s=page(116,U,'108','Example 3.13: direct method and shortcut method','مثال 3.13: براہِ راست طریقہ اور مختصر طریقہ','بېلګه 3.13: مستقیم طریقه او لنډه طریقه','sd-7')
Flow(s)
add(s,'c1','Marks: 5 – 9, 10 – 14, 15 – 19, 20 – 24 with frequencies 10, 20, 30, 15 (data of Example 3.13).','نمبر: 5 – 9، 10 – 14، 15 – 19، 20 – 24 اور تعدد 10، 20، 30، 15 (مثال 3.13 کے اعداد و شمار)۔','نمرې: 5 – 9، 10 – 14، 15 – 19، 20 – 24 او فریکونسي 10، 20، 30، 15 (د بېلګې 3.13 معلومات).',role='question',exampleId=E13,sourceGap=dict(note='Continues the question of Example 3.13 from the previous page.'))
head(s,'sol13','Solution:','حل:','حل:',exampleId=E13)
add(s,'m1','(i) By direct method','(i) براہِ راست طریقے سے','(i) په مستقیم طریقه',role='solution',exampleId=E13)
add(s,'m2','(ii) By shortcut method','(ii) مختصر طریقے سے','(ii) په لنډه طریقه',role='solution',exampleId=E13)
mk=['5 – 9','10 – 14','15 – 19','20 – 24']; fr=[10,20,30,15]; xs=[7,12,17,22]; fx=[70,240,510,330]
dv=['-8.33','-3.33','1.67','6.67']; sq=['69.39','11.09','2.79','44.49']; fs=['693.89','221.80','83.70','667.35']
s['tables']=[table('Example 3.13: marks and frequency','مثال 3.13: نمبر اور تعدد','بېلګه 3.13: نمرې او فریکونسي',[c('Marks:','نمبر:','نمرې:')]+[c(v) for v in mk],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in fr]],exampleId=E13),
 table('Example 3.13: direct method table','مثال 3.13: براہِ راست طریقے کا جدول','بېلګه 3.13: د مستقیمې طریقې جدول',[c('Marks','نمبر','نمرې'),c('f'),c('x'),c('fx'),c('(x − x̄)'),c('(x − x̄)²'),c('f(x − x̄)²')],[[c(mk[i]),c(str(fr[i])),c(str(xs[i])),c(str(fx[i])),c(dv[i]),c(sq[i]),c(fs[i])] for i in range(4)]+[[c('Total','میزان','ټولیز'),c('75'),c('–'),c('1150'),c('–'),c('–'),c('1666.75')]],exampleId=E13),
 table('Example 3.13: shortcut method table','مثال 3.13: مختصر طریقے کا جدول','بېلګه 3.13: د لنډې طریقې جدول',[c('Marks','نمبر','نمرې'),c('f'),c('x'),c('fx'),c('fx²')],[[c(mk[i]),c(str(fr[i])),c(str(xs[i])),c(str(fx[i])),c(str(v))] for i,v in enumerate([490,2880,8670,7260])]+[[c('Total','میزان','ټولیز'),c('75'),c('–'),c('1150'),c('19300')]],exampleId=E13)]
eq=[('a',r'S=\sqrt{\dfrac{\sum f(x-\bar{x})^2}{\sum f}}','S = √(Σf(x − x̄)²/Σf)',E13),
 ('b',r'S^2=\dfrac{\sum f(x-\bar{x})^2}{\sum f}','S² = Σf(x − x̄)²/Σf',E13),
 ('c',r'\bar{x}=\dfrac{\sum x}{n}=\dfrac{1150}{75}=15.33','x̄ = Σx/n = 1150/75 = 15.33   [printed "Σx/n"]',E13),
 ('d',r's=\sqrt{\dfrac{1666.75}{75}}=\sqrt{22.22}=4.71\qquad\text{(Absolute dispersion)}','s = √(1666.75/75) = √22.22 = 4.71   (Absolute dispersion)',E13),
 ('e',r'S^2=\dfrac{1666.75}{75}=22.22','S² = 1666.75/75 = 22.22',E13),
 ('f',r'\text{Coefficient of S.D}=\dfrac{s}{\bar{x}}=\dfrac{4.71}{15.33}=0.31\qquad\text{(Relative dispersion)}','Coefficient of S.D = s/x̄ = 4.71/15.33 = 0.31   (Relative dispersion)',E13),
 ('g',r'S=\sqrt{\dfrac{\sum fx^2}{\sum f}-\left(\dfrac{\sum fx}{\sum f}\right)^2}','S = √(Σfx²/Σf − (Σfx/Σf)²)',E13),
 ('h',r'S^2=\dfrac{\sum fx^2}{\sum f}-\left(\dfrac{\sum fx}{\sum f}\right)^2','S² = Σfx²/Σf − (Σfx/Σf)²',E13)]
build(s,116,['c1','T:0','sol13','m1','E:a','E:b','T:1','E:c','E:d','E:e','E:f','m2','E:g','E:h','T:2'],eq)
s['sourceNote']='Printed page 108. The question data at the top are printed as aligned Marks/Frequency rows and are shown as a table. A handwritten loop on the "70" in the lower table and a dark edge shadow at the bottom-right are ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 117 (printed 109) ----------
s=page(117,U,'109','Example 3.13 (shortcut end, step-deviation) · 3.5.6 Difference between S.D and variance','مثال 3.13 (مختصر کا اختتام، قدمی انحراف) · 3.5.6 معیاری انحراف اور تغیر میں فرق','بېلګه 3.13 (د لنډې پای، ګام‌انحراف) · 3.5.6 د معیاري انحراف او وریانس توپیر','sd-8')
Flow(s)
add(s,'n1','(iii) By change of origin and scale method or step deviation method','(iii) مبدا اور پیمانے کی تبدیلی کے طریقے یا قدمی انحراف کے طریقے سے','(iii) د اصل او پیمانې د بدلون طریقې یا ګام‌انحراف طریقې په واسطه',role='solution',exampleId=E13)
add(s,'n2','Here A = 17, h = 5 so u = (x − A)/h = (x − 17)/5','یہاں A = 17, h = 5 لہٰذا u = (x − A)/h = (x − 17)/5','دلته A = 17, h = 5 نو u = (x − A)/h = (x − 17)/5',role='solution',exampleId=E13)
head(s,'h356','3.5.6 Difference between standard deviation and variance','3.5.6 معیاری انحراف اور تغیر میں فرق','3.5.6 د معیاري انحراف او وریانس توپیر')
add(s,'t356','Both tell us about the average variability of the given data about the mean but the unit of S.D is the same as the unit of measurement of the original data i.e. if observations have unit k.g, then unit of S.D will also be k.g, whereas, the unit of variance is square of the unit of measurement (i.e. if the observations are in meters, the unit of variance will be expressed in square meters, so many times, it becomes difficult to actually determine the magnitude of variation also variance is sensitive to extreme values. However, variance is the backbone of inferential statistics.','دونوں ہمیں دیے گئے اعداد و شمار کی اوسط کے گرد اوسط تغیر پذیری کے بارے میں بتاتے ہیں لیکن S.D کی اکائی اصل اعداد و شمار کی پیمائش کی اکائی کے برابر ہوتی ہے یعنی اگر مشاہدات کی اکائی کلوگرام ہو تو S.D کی اکائی بھی کلوگرام ہوگی، جبکہ تغیر کی اکائی پیمائش کی اکائی کا مربع ہوتی ہے (یعنی اگر مشاہدات میٹر میں ہوں تو تغیر کی اکائی مربع میٹر میں ظاہر ہوگی، اس لیے کئی بار تغیر کی مقدار کا اصل تعین مشکل ہو جاتا ہے، نیز تغیر انتہائی قدروں کے لیے حساس ہے۔ تاہم، تغیر استنباطی شماریات کی ریڑھ کی ہڈی ہے۔','دواړه موږ ته د ورکړل شویو معلوماتو د اوسط شاوخوا اوسط متغیرتیا په اړه وايي خو د S.D واحد د اصلي معلوماتو د اندازې له واحد سره یو شان دی یعنې که کتنې د کیلوګرام واحد ولري نو د S.D واحد به هم کیلوګرام وي، پداسې حال کې چې د وریانس واحد د اندازې د واحد مربع دی (یعنې که کتنې په مترو کې وي د وریانس واحد به په مربع مترو کې ښودل کېږي، نو ډېر ځله د تغیر د اندازې ټاکل ستونزمن کېږي او وریانس د سختو ارزښتونو لپاره هم حساس دی. خو وریانس د استنباطي احصایې بنسټ دی.',sourceGap=dict(note='The opening parenthesis after "(i.e. if the observations are in meters, …" is never closed in the printed text.'))
mk=['5 – 9','10 – 14','15 – 19','20 – 24']; fr=[10,20,30,15]; xs=[7,12,17,22]
s['tables']=[table('Example 3.13: step-deviation table','مثال 3.13: قدمی انحراف کا جدول','بېلګه 3.13: د ګام‌انحراف جدول',[c('Marks','نمبر','نمرې'),c('f'),c('x'),c('u = (x − 17)/5'),c('fu'),c('fu²')],[[c(mk[i]),c(str(fr[i])),c(str(xs[i])),c(str(u)),c(str(a)),c(b)] for i,(u,a,b) in enumerate([(-2,-20,'+40'),(-1,-20,'+20'),(0,0,'0'),(1,15,'15')])]+[[c('Total','میزان','ټولیز'),c('75'),c('–'),c('–'),c('-25'),c('75')]],exampleId=E13)]
eq=[('a',r'\therefore\ S=\sqrt{\dfrac{19300}{75}-\left(\dfrac{1150}{75}\right)^2}=\sqrt{257.33-235.11}=\sqrt{22.22}=4.71','∴ S = √(19300/75 − (1150/75)²) = √(257.33 − 235.11) = √22.22 = 4.71',E13),
 ('b',r'S^2=\dfrac{19300}{75}-\left(\dfrac{1150}{75}\right)^2=257.33-235.11=22.22','S² = 19300/75 − (1150/75)² = 257.33 − 235.11 = 22.22   [the printed subtrahend reads (93001/75), a misprint for (1150/75)]',E13),
 ('c',r's=\sqrt{\dfrac{\sum fu^2}{\sum f}-\left(\dfrac{\sum fu}{\sum f}\right)^2}\times h','s = √(Σfu²/Σf − (Σfu/Σf)²) × h',E13),
 ('d',r's^2=\left[\dfrac{\sum fu^2}{\sum f}-\left(\dfrac{\sum fu}{\sum f}\right)^2\right]\times h^2','s² = [Σfu²/Σf − (Σfu/Σf)²] × h²',E13),
 ('e',r'S=\sqrt{\dfrac{75}{75}-\left(\dfrac{-25}{75}\right)^2}\times 5=\sqrt{1-0.111}\times 5=(0.943)\times 5=4.71','S = √(75/75 − (−25/75)²) × 5 = √(1 − 0.111) × 5 = (0.943) × 5 = 4.71',E13),
 ('f',r'S^2=\dfrac{75}{75}-\left(\dfrac{-25}{75}\right)^2\times 5^2=(1-0.111)\times 25=(0.889)(25)=22.22','S² = 75/75 − (−25/75)² × 5² = (1 − 0.111) × 25 = (0.889)(25) = 22.22',E13)]
build(s,117,['E:a','E:b','n1','E:c','E:d','T:0','n2','E:e','E:f','h356','t356'],eq)
s['sourceNote']='Printed page 109. The page number at the bottom is partly cut off by the scan. The first lines complete the shortcut method of Example 3.13. In the S² line the printed subtrahend reads (93001/75) (misprint for 1150/75) and the printed "×" placement in the step-deviation S² line is kept. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 118 (printed 110) ----------
s=page(118,U,'110','3.5.7 Properties of variance and S.D · 3.5.8 Coefficient of variation','3.5.7 تغیر اور معیاری انحراف کی خصوصیات · 3.5.8 تغیر کا عددی سر','3.5.7 د وریانس او معیاري انحراف ځانګړتیاوې · 3.5.8 د تغیر ضریب','sd-9')
Flow(s)
head(s,'h357','3.5.7 Properties of variance and standard deviation','3.5.7 تغیر اور معیاری انحراف کی خصوصیات','3.5.7 د وریانس او معیاري انحراف ځانګړتیاوې')
add(s,'p1','(i) Variance and S.D of a constant are zero. That is V(c) = 0, where c is any constant and S.D(c) = 0','(i) مستقل کا تغیر اور S.D صفر ہوتے ہیں۔ یعنی V(c) = 0، جہاں c کوئی بھی مستقل ہے اور S.D(c) = 0','(i) د ثابت وریانس او S.D صفر وي. یعنې V(c) = 0، چېرته چې c هر ثابت دی او S.D(c) = 0',listGroup='sd-props')
add(s,'p2','(ii) If a constant c is added to or subtracted from the values of a variable, variance and S.D will not change. That is, V(x ± c) = V(x) and S.D(x ± c) = S.D(x).','(ii) اگر متغیر کی قدروں میں کوئی مستقل c جمع یا تفریق کیا جائے تو تغیر اور S.D تبدیل نہیں ہوں گے۔ یعنی V(x ± c) = V(x) اور S.D(x ± c) = S.D(x)۔','(ii) که د متغیر په ارزښتونو کې یو ثابت c جمع یا تفریق شي نو وریانس او S.D به نه بدلېږي. یعنې V(x ± c) = V(x) او S.D(x ± c) = S.D(x).',listGroup='sd-props')
add(s,'p3','(iii) If values of a variable are multiplied or divided by a constant, then variance will be changed by the square of that constant and S.D by absolute of that constant. That is,','(iii) اگر متغیر کی قدروں کو کسی مستقل سے ضرب یا تقسیم کیا جائے تو تغیر اس مستقل کے مربع سے اور S.D اس مستقل کی مطلق قدر سے تبدیل ہوگا۔ یعنی،','(iii) که د متغیر ارزښتونه په یو ثابت ضرب یا تقسیم شي نو وریانس به د هغه ثابت په مربع او S.D به د هغه ثابت په مطلق ارزښت بدل شي. یعنې،',listGroup='sd-props')
add(s,'p4','(iv) Variance and S.D of the sum or difference of two independent variables is equal to the sum of their respective variances and standard deviations. That is,','(iv) دو آزاد متغیرات کے مجموعے یا فرق کا تغیر اور S.D ان کے متعلقہ تغیرات اور معیاری انحرافات کے مجموعے کے برابر ہوتا ہے۔ یعنی،','(iv) د دوو خپلواکو متغیرونو د مجموعې یا توپیر وریانس او S.D د هغوی د اړوندو وریانسونو او معیاري انحرافاتو له مجموعې سره مساوي وي. یعنې،',listGroup='sd-props')
head(s,'h358','3.5.8 Coefficient of variation','3.5.8 تغیر کا عددی سر','3.5.8 د تغیر ضریب')
add(s,'t358','This measure of relative dispersion is very popular and reliable. It is independent of the unit of measurement and expresses the result in percentage. It is used to compare the performance of any two or more series of data. It was suggested by Professor Karl person. It is abbreviated as C.V and is defined as: the ratio of standard deviation and the mean expressed in percentage is called Coefficient of variation.','اضافی انتشار کا یہ پیمانہ بہت مقبول اور قابلِ اعتماد ہے۔ یہ پیمائش کی اکائی سے آزاد ہے اور نتیجہ فیصد میں ظاہر کرتا ہے۔ یہ اعداد و شمار کے کسی بھی دو یا زیادہ سلسلوں کی کارکردگی کا موازنہ کرنے کے لیے استعمال ہوتا ہے۔ یہ پروفیسر کارل پرسن نے تجویز کیا تھا۔ اسے C.V سے مختصر کیا جاتا ہے اور اس کی تعریف یوں ہے: معیاری انحراف اور اوسط کی نسبت جو فیصد میں ظاہر کی جائے تغیر کا عددی سر کہلاتی ہے۔','د نسبي خپراوي دا اندازه ډېره مشهوره او د باور وړ ده. دا د اندازې له واحد څخه خپلواکه ده او پایله په سلنه کې ښيي. دا د معلوماتو د هرو دوو یا ډېرو لړیو د فعالیت د پرتلې لپاره کارول کېږي. دا د پروفیسر Karl person لخوا وړاندیز شوې وه. دا د C.V په توګه لنډېږي او تعریف یې دا دی: د معیاري انحراف او اوسط نسبت چې په سلنه کې ښودل شي د تغیر ضریب بلل کېږي.')
add(s,'t358b','The smaller value of C.V means less variability which shows that performance is','C.V کی چھوٹی قدر کا مطلب کم تغیر پذیری ہے جو ظاہر کرتی ہے کہ کارکردگی','د C.V کوچنی ارزښت پدې معنا دی چې لږ متغیرتیا ده چې ښيي چې فعالیت',sourceGap=dict(note='The sentence continues on the next page.'))
eq=[('a',r'V(cx)=c^2\,V(x)\qquad\text{and}\qquad V\!\left(\dfrac{x}{c}\right)=\dfrac{V(x)}{c^2}','V(cx) = c²V(x)   and   V(x/c) = V(x)/c²',None),
 ('b',r'\text{S.D}(cx)=|c|\,\text{S.D}(x)\qquad\text{S.D}\!\left(\dfrac{x}{c}\right)=\dfrac{\text{S.D}(x)}{|c|}','S.D(cx) = |c| S.D(x)   S.D(x/c) = S.D(x)/|c|',None),
 ('c',r'V(x\pm y)=V(x)+V(y)','V(x ± y) = V(x) + V(y)',None),
 ('d',r'\text{S.D}(x\pm y)=\sqrt{V(x)+V(y)}','S.D(x ± y) = √(V(x) + V(y))',None),
 ('e',r'\text{C.V}=\dfrac{\sigma}{\mu}\times 100\qquad\text{(Population case)}','C.V = (σ/μ) × 100   (Population case)',None),
 ('f',r'\text{C.V}=\dfrac{s}{\bar{x}}\times 100\qquad\text{(Sample case)}','C.V = (s/x̄) × 100   (Sample case)',None)]
build(s,118,['h357','p1','p2','p3','E:a','E:b','p4','E:c','E:d','h358','t358','E:e','E:f','t358b'],eq)
s['sourceNote']='Printed page 110. Printed wording kept: "Karl person" (for Karl Pearson), "k.g". The printed formula for the sum or difference of independent variables gives S.D as the square root of the sum of the variances. Header graphics and watermark excluded.'
s['vocabulary']={'coefficient of variation':dict(ur='تغیر کا عددی سر',ps='د تغیر ضریب')}
save(s)
