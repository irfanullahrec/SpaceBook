from stathelp import *
c=cell
def q(s,key,en,ur,ps,ex,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,**m)
def o(s,key,en,ur,ps,ex): add(s,key,en,ur,ps,role='option',exerciseId=ex)
def row(lbl_en,lbl_ur,lbl_ps,vals): return [c(lbl_en,lbl_ur,lbl_ps)]+[c(str(v)) for v in vals]
# ---------- scan 203 (printed 193) ----------
U='regression-correlation'
s=page(203,U,'193','Exercise-5: Q5.3 (x) · Q5.4 – Q5.11','مشق-5: سوال 5.3 (x) · سوال 5.4 – 5.11','تمرین-5: پوښتنه 5.3 (x) · پوښتنې 5.4 – 5.11','exercise5-c',layout='exercise')
Flow(s)
ex='stat11-ex5-3-10'
q(s,'m10','(x) The geometric mean of the two regression coefficients b_y.x and b_x.y is equal to','(x) دو ریگریشن عددی سروں b_y.x اور b_x.y کا ہندسی اوسط برابر ہے','(x) د دوو ریګرېشن ضریبونو b_y.x او b_x.y هندسي اوسط له … سره مساوي دی',ex)
o(s,'m10a','(a) r_xy','(الف) r_xy','(الف) r_xy',ex)
o(s,'m10b','(b) r²_xy','(ب) r²_xy','(ب) r²_xy',ex)
o(s,'m10c','(c) 1','(ج) 1','(ج) 1',ex)
o(s,'m10d','(d) 0','(د) 0','(د) 0',ex)
q(s,'q54','5.4 Explain the concepts of the following (i) Regression (ii) Linear and nonlinear regression (iii) Dependent and independent variables','5.4 درج ذیل کے تصورات کی وضاحت کریں (i) ریگریشن (ii) خطی اور غیر خطی ریگریشن (iii) تابع اور آزاد متغیرات','5.4 د لاندې مفهومونه تشریح کړئ (i) ریګرېشن (ii) خطي او غیر خطي ریګرېشن (iii) تابع او خپلواک متغیرونه','stat11-ex5-4')
q(s,'q55','5.5 What do you mean by (i) Regression lines (ii) Regression coefficient (iii) Least squares principle','5.5 آپ کی کیا مراد ہے (i) ریگریشن لکیریں (ii) ریگریشن عددی سر (iii) کم از کم مربعات کا اصول','5.5 تاسو څه مطلب لرئ (i) د ریګرېشن کرښې (ii) ریګرېشن ضریب (iii) د لږ تر لږه مربعاتو اصل','stat11-ex5-5')
q(s,'q56','5.6 Distinguish between the following. (i) Simple and multiple regression. (ii) Scatter diagram and curve fitting.','5.6 درج ذیل میں فرق کریں۔ (i) سادہ اور متعدد ریگریشن۔ (ii) بکھراؤ خاکہ اور منحنی فٹ کرنا۔','5.6 په لاندې کې توپیر وکړئ. (i) ساده او څو‌ګونی ریګرېشن. (ii) د خپرېدو ډیاګرام او د منحني برابرول.','stat11-ex5-6')
q(s,'q57','5.7 Construct a scatter diagram for the following data','5.7 درج ذیل اعداد و شمار کے لیے بکھراؤ خاکہ بنائیں','5.7 د لاندې معلوماتو لپاره د خپرېدو ډیاګرام جوړ کړئ','stat11-ex5-7')
q(s,'q58','5.8 For the following data, find the linear regression equation for predicting y from x','5.8 درج ذیل اعداد و شمار کے لیے x سے y کی پیش گوئی کے لیے خطی ریگریشن مساوات معلوم کریں','5.8 د لاندې معلوماتو لپاره د x څخه د y د وړاندوینې لپاره خطي ریګرېشن معادله ومومئ','stat11-ex5-8')
q(s,'q59','5.9 The following table shows the ages (x) and systolic blood pressure (y) of eight persons','5.9 درج ذیل جدول آٹھ افراد کی عمروں (x) اور سسٹولک بلڈ پریشر (y) کو ظاہر کرتا ہے','5.9 لاندې جدول د اتو کسانو عمرونه (x) او سیسټولیک د وینې فشار (y) ښيي','stat11-ex5-9')
q(s,'q59a','(i) Fit a linear regression equation of y on x and estimate the blood pressure of a 70 years old person.','(i) x پر y کی خطی ریگریشن مساوات فٹ کریں اور 70 سال کی عمر کے شخص کے بلڈ پریشر کا تخمینہ لگائیں۔','(i) د x پر y خطي ریګرېشن معادله برابره کړئ او د 70 کلن کس د وینې فشار اټکل کړئ.','stat11-ex5-9')
q(s,'q59b','(ii) What is the regression coefficient and what does it mean?','(ii) ریگریشن عددی سر کیا ہے اور اس کا کیا مطلب ہے؟','(ii) ریګرېشن ضریب څه دی او څه مطلب لري؟','stat11-ex5-9')
q(s,'q510','5.10 Find the regression lines or equations for the data given below','5.10 نیچے دیے گئے اعداد و شمار کے لیے ریگریشن لکیریں یا مساواتیں معلوم کریں','5.10 د لاندې ورکړل شویو معلوماتو لپاره د ریګرېشن کرښې یا معادلې ومومئ','stat11-ex5-10')
q(s,'q511','5.11 Consider the following data, determine the estimated regression equation ŷ = a + bx: n = 10, Σx = 1710, Σy = 760, Σxy = 130628, Σx² = 293162, Σy² = 59390','5.11 درج ذیل اعداد و شمار پر غور کریں، تخمینی ریگریشن مساوات ŷ = a + bx معلوم کریں: n = 10, Σx = 1710, Σy = 760, Σxy = 130628, Σx² = 293162, Σy² = 59390','5.11 لاندې معلومات په پام کې ونیسئ، اټکل شوې ریګرېشن معادله ŷ = a + bx ومومئ: n = 10, Σx = 1710, Σy = 760, Σxy = 130628, Σx² = 293162, Σy² = 59390','stat11-ex5-11')
s['tables']=[table('Q5.7: x and y','سوال 5.7: x اور y','پوښتنه 5.7: x او y',row('x:','x:','x:',[6,4,1,1,3]),[row('y:','y:','y:',[6,1,4,3,1])]),
 table('Q5.8: x and y','سوال 5.8: x اور y','پوښتنه 5.8: x او y',row('x:','x:','x:',[7,9,6,12,9,5]),[row('y:','y:','y:',[6,6,3,5,6,4])]),
 table('Q5.9: age and blood pressure','سوال 5.9: عمر اور بلڈ پریشر','پوښتنه 5.9: عمر او د وینې فشار',row('Age (x):','عمر (x):','عمر (x):',[56,42,60,50,54,49,39,45]),[row('Blood pressure (y):','بلڈ پریشر (y):','د وینې فشار (y):',[160,130,125,135,145,115,140,120])]),
 table('Q5.10: x and y','سوال 5.10: x اور y','پوښتنه 5.10: x او y',row('x:','x:','x:',[3,5,6,9,10,12,15,20,22,28]),[row('y:','y:','y:',[10,12,15,18,20,22,27,30,32,34])])]
for i in range(4): s['tables'][i]['exerciseId']='stat11-ex5-q'+['57','58','59','510'][i]
build(s,203,['m10','m10a','m10b','m10c','m10d','q54','q55','q56','q57','T:0','q58','T:1','q59','T:2','q59a','q59b','q510','T:3','q511'],[])
s['sourceNote']='Printed page 193. The subscripts of b_y.x, b_x.y and r_xy are written with underscores in the plain text; r²_xy stands for r with the square. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 204 (printed 194) ----------
s=page(204,U,'194','Exercise-5: Q5.12 – Q5.19','مشق-5: سوال 5.12 – 5.19','تمرین-5: پوښتنې 5.12 – 5.19','exercise5-d',layout='exercise')
Flow(s)
q(s,'q512','5.12 Define the term correlation, simple correlation and multiple correlation.','5.12 اصطلاح ارتباط، سادہ ارتباط اور متعدد ارتباط کی تعریف کریں۔','5.12 د همتړاو، ساده همتړاو او څو‌ګونی همتړاو اصطلاح تعریف کړئ.','stat11-ex5-12')
q(s,'q513','5.13 Explain the following. (i) Correlation (ii) Positive correlation (iii) Negative correlation (iv) Coefficient of correlation.','5.13 درج ذیل کی وضاحت کریں۔ (i) ارتباط (ii) مثبت ارتباط (iii) منفی ارتباط (iv) ارتباطی عددی سر۔','5.13 لاندې تشریح کړئ. (i) همتړاو (ii) مثبت همتړاو (iii) منفي همتړاو (iv) د همتړاو ضریب.','stat11-ex5-13')
q(s,'q514','5.14 Find the coefficient of correlation between x and y for the following data.','5.14 درج ذیل اعداد و شمار کے لیے x اور y کے درمیان ارتباطی عددی سر معلوم کریں۔','5.14 د لاندې معلوماتو لپاره د x او y تر منځ د همتړاو ضریب ومومئ.','stat11-ex5-14')
q(s,'q515','5.15 For the following observations (a) sketch a scatter plot and estimate the correlation. (b) compute the Pearson coefficient of correlation.','5.15 درج ذیل مشاہدات کے لیے (الف) بکھراؤ پلاٹ بنائیں اور ارتباط کا تخمینہ لگائیں۔ (ب) پیئرسن کا ارتباطی عددی سر حساب کریں۔','5.15 د لاندې کتنو لپاره (a) د خپرېدو پلاټ رسم کړئ او همتړاو اټکل کړئ. (b) د Pearson د همتړاو ضریب محاسبه کړئ.','stat11-ex5-15')
q(s,'q516','5.16 Given the data. (i) Compute the least squares regression line of y on x and of x on y. (ii) Compute coefficient of correlation.','5.16 اعداد و شمار دیے گئے ہیں۔ (i) x پر y اور y پر x کی کم از کم مربعات ریگریشن لکیر حساب کریں۔ (ii) ارتباطی عددی سر حساب کریں۔','5.16 معلومات ورکړل شوي دي. (i) د x پر y او د y پر x د لږ تر لږه مربعاتو ریګرېشن کرښه محاسبه کړئ. (ii) د همتړاو ضریب محاسبه کړئ.','stat11-ex5-16')
q(s,'q517','5.17 With the help of following values n = 20, Σx = 40, Σy = 100, Σx² = 180, Σy² = 1424, Σxy = 404 (i) Fit a regression line of y on x. (ii) Find correlation coefficient.','5.17 درج ذیل قدروں کی مدد سے n = 20, Σx = 40, Σy = 100, Σx² = 180, Σy² = 1424, Σxy = 404 (i) x پر y کی ریگریشن لکیر فٹ کریں۔ (ii) ارتباطی عددی سر معلوم کریں۔','5.17 د لاندې ارزښتونو په مرسته n = 20, Σx = 40, Σy = 100, Σx² = 180, Σy² = 1424, Σxy = 404 (i) د x پر y ریګرېشن کرښه برابره کړئ. (ii) د همتړاو ضریب ومومئ.','stat11-ex5-17')
q(s,'q518','5.18 (a) Define rank correlation. When you would use (i) product moment correlation coefficient and (ii) rank correlation coefficient? (b) Calculate spearman’s coefficient of rank correlation for the following data.','5.18 (الف) درجاتی ارتباط کی تعریف کریں۔ آپ (i) حاصلِ ضرب معیارِ اثر ارتباطی عددی سر اور (ii) درجاتی ارتباطی عددی سر کب استعمال کریں گے؟ (ب) درج ذیل اعداد و شمار کے لیے سپیئرمین کا درجاتی ارتباطی عددی سر حساب کریں۔','5.18 (a) رتبه‌یي همتړاو تعریف کړئ. تاسو به (i) د ضرب-مومنټ همتړاو ضریب او (ii) رتبه‌یي همتړاو ضریب کله وکاروئ؟ (b) د لاندې معلوماتو لپاره د سپیرمن رتبه‌یي همتړاو ضریب محاسبه کړئ.','stat11-ex5-18')
q(s,'q519','5.19 (a) what do you mean by ranking of tied observations? Explain how you would find the coefficient of rank correlation for tied ranks. (b) Calculate rank correlation coefficient for the following data.','5.19 (الف) برابر مشاہدات کی درجہ بندی سے آپ کی کیا مراد ہے؟ وضاحت کریں کہ آپ برابر درجوں کے لیے درجاتی ارتباط کا عددی سر کیسے معلوم کریں گے۔ (ب) درج ذیل اعداد و شمار کے لیے درجاتی ارتباطی عددی سر حساب کریں۔','5.19 (a) د برابرو کتنو له رتبه‌بندۍ څخه تاسو څه مطلب لرئ؟ تشریح کړئ چې تاسو به د برابرو رتبو لپاره د رتبه‌یي همتړاو ضریب څنګه ومومئ. (b) د لاندې معلوماتو لپاره رتبه‌یي همتړاو ضریب محاسبه کړئ.','stat11-ex5-19')
t=lambda ttl,ur,ps,xs,ys,ex: table(ttl,ur,ps,row('x:','x:','x:',xs),[row('y:','y:','y:',ys)],exerciseId=ex)
s['tables']=[t('Q5.14: x and y','سوال 5.14: x اور y','پوښتنه 5.14: x او y',[6,2,10,4,8],[9,11,5,8,7],'stat11-ex5-q514'),
 t('Q5.15: x and y','سوال 5.15: x اور y','پوښتنه 5.15: x او y',[1,4,1,1,2,0,2,1],[7,2,3,6,0,6,3,5],'stat11-ex5-q515'),
 t('Q5.16: x and y','سوال 5.16: x اور y','پوښتنه 5.16: x او y',[48,40,32,34,30,50,26,50,22,43],[76,56,40,50,34,70,56,68,40,57],'stat11-ex5-q516'),
 t('Q5.18: x and y','سوال 5.18: x اور y','پوښتنه 5.18: x او y',[53,98,95,81,75,71,59,55],[47,25,32,37,30,40,39,45],'stat11-ex5-q518'),
 t('Q5.19: x and y','سوال 5.19: x اور y','پوښتنه 5.19: x او y',[65,63,64,68,62,70,66,68,69,71],[66,62,66,70,64,67,63,71,65,69],'stat11-ex5-q519')]
build(s,204,['q512','q513','q514','T:0','q515','T:1','q516','T:2','q517','q518','T:3','q519','T:4'],[])
s['sourceNote']='Printed page 194. The data of each question are printed as aligned x and y rows and are shown as tables after their questions. Printed spellings kept: "spearman’s", "what do you mean". Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 205 (printed 195) ----------
U='time-series'
s=page(205,U,'195','Unit 6: Time Series · Learning outcomes','یونٹ 6: وقتی سلسلہ · سیکھنے کے نتائج','شپږم واحد: وخت لړۍ · د زده کړې پایلې','unit6-outcomes',layout='outcomes')
Flow(s)
head(s,'unit','Unit-6','یونٹ-6','واحد-6')
head(s,'title','Time Series','وقتی سلسلہ','د وخت لړۍ')
add(s,'intro','After studying this unit, the students will be able to:','اس یونٹ کے مطالعے کے بعد طلبہ اس قابل ہوں گے کہ:','د دې واحد له لوستلو وروسته به زده کوونکي وکولای شي چې:')
O=[('Define time series. Define and construct historiogram.','وقتی سلسلے کی تعریف کریں۔ تاریخی خاکہ (ہسٹوریوگرام) کی تعریف کریں اور بنائیں۔','د وخت لړۍ تعریف کړي. تاریخي ډیاګرام (هسټوریوګرام) تعریف او جوړ کړي.'),
('Describe the components of a time series: i. Secular trend, ii. Seasonal variation, iii. Cyclical fluctuations, and iv. Irregular movements.','وقتی سلسلے کے اجزاء بیان کریں: i. صدیوی رجحان، ii. موسمی تغیر، iii. دوری اتار چڑھاؤ، اور iv. بے قاعدہ حرکات۔','د وخت لړۍ برخې بیان کړي: i. عمري تمایل، ii. موسمي تغیر، iii. دوري بدلونونه، او iv. بې‌قاعدې حرکتونه.'),
('Explain ‘analysis of time series’.','‘وقتی سلسلے کے تجزیے’ کی وضاحت کریں۔','‘د وخت لړۍ تحلیل’ تشریح کړي.'),
('Describe additive and multiplicative models utilized for analysis of time series.','وقتی سلسلے کے تجزیے کے لیے استعمال ہونے والے جمعی اور ضربی ماڈلز بیان کریں۔','د وخت لړۍ د تحلیل لپاره کارېدونکي جمعي او ضربي ماډلونه بیان کړي.'),
('Explain the technique of coding the time series.','وقتی سلسلے کی کوڈنگ کی تکنیک کی وضاحت کریں۔','د وخت لړۍ د کوډ کولو تخنیک تشریح کړي.'),
('Describe and apply the method of freehand curve to measure the secular trend.','صدیوی رجحان ناپنے کے لیے آزاد دستی منحنی کے طریقے کو بیان کریں اور لاگو کریں۔','د عمري تمایل د اندازه کولو لپاره د آزاد لاس منحني طریقه بیان او پلي کړي.'),
('Identify the merits and demerits of the freehand curve method.','آزاد دستی منحنی کے طریقے کی خوبیوں اور خامیوں کی نشاندہی کریں۔','د آزاد لاس منحني د طریقې ګټې او زیانونه وپېژني.'),
('Describe and apply the method of semi-averages to measure the secular trend including the algebraic form of semi-averages trend line.','صدیوی رجحان ناپنے کے لیے نیم اوسط کے طریقے کو بیان کریں اور لاگو کریں بشمول نیم اوسط رجحان لکیر کی الجبری شکل۔','د عمري تمایل د اندازه کولو لپاره د نیمه اوسطونو طریقه بیان او پلي کړي د نیمه اوسطونو د تمایل کرښې الجبري بڼې په شمول.'),
('Identify the merits and demerits of the method of semi-averages.','نیم اوسط کے طریقے کی خوبیوں اور خامیوں کی نشاندہی کریں۔','د نیمه اوسطونو د طریقې ګټې او زیانونه وپېژني.'),
('Describe and apply the method of moving averages to measure the secular trend.','صدیوی رجحان ناپنے کے لیے متحرک اوسط کے طریقے کو بیان کریں اور لاگو کریں۔','د عمري تمایل د اندازه کولو لپاره د خوځېدونکو اوسطونو طریقه بیان او پلي کړي.'),
('Identify the merits and demerits of the method of moving averages.','متحرک اوسط کے طریقے کی خوبیوں اور خامیوں کی نشاندہی کریں۔','د خوځېدونکو اوسطونو د طریقې ګټې او زیانونه وپېژني.'),
('Describe and apply the method of least squares to measure: i. linear secular trend, ii. Quartile secular trend, for estimating trend values.','کم از کم مربعات کے طریقے کو بیان کریں اور لاگو کریں تاکہ ناپا جا سکے: i. خطی صدیوی رجحان، ii. چوتھائی صدیوی رجحان، رجحان کی قدروں کے تخمینے کے لیے۔','د لږ تر لږه مربعاتو طریقه بیان او پلي کړي ترڅو اندازه شي: i. خطي عمري تمایل، ii. څلورمه عمري تمایل، د تمایل د ارزښتونو د اټکل لپاره.'),
('Describe and apply the technique of shifting of origin in the least squares secular trend.','کم از کم مربعات صدیوی رجحان میں مبدا کی منتقلی کی تکنیک کو بیان کریں اور لاگو کریں۔','د لږ تر لږه مربعاتو په عمري تمایل کې د اصل د بدلولو تخنیک بیان او پلي کړي.'),
('Identify the merits and demerits of the least squares secular trend.','کم از کم مربعات صدیوی رجحان کی خوبیوں اور خامیوں کی نشاندہی کریں۔','د لږ تر لږه مربعاتو د عمري تمایل ګټې او زیانونه وپېژني.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F=Flow(s);F.done()
s['sourceNote']='Printed page 195. Unit 6 opening page: learning outcomes in a bordered box. A thumb is visible at the top-right corner of the scan. Printed spellings kept: "historiogram". Header graphics and watermark excluded.'
s['vocabulary']={'time series':dict(ur='وقتی سلسلہ',ps='د وخت لړۍ'),'secular trend':dict(ur='صدیوی رجحان',ps='عمري تمایل')}
save(s)
# ---------- scan 206 (printed 196) ----------
s=page(206,U,'196','6.1 Time series · Examples · Analysis of time series (start)','6.1 وقتی سلسلہ · مثالیں · وقتی سلسلے کا تجزیہ (آغاز)','6.1 د وخت لړۍ · بېلګې · د وخت لړۍ تحلیل (پیل)','ts-intro-1')
Flow(s)
head(s,'h61','6.1 Time series','6.1 وقتی سلسلہ','6.1 د وخت لړۍ')
add(s,'t1','A series of observations of the same characteristics arranged according to the time of occurrence is known as time series. The time may be hour, day, week, month, quarter, year or decade etc. Examples of time series are:','ایک ہی خصوصیات کے مشاہدات کا سلسلہ جو وقوع کے وقت کے مطابق ترتیب دیا گیا ہو وقتی سلسلہ کہلاتا ہے۔ وقت گھنٹہ، دن، ہفتہ، مہینہ، سہ ماہی، سال یا دہائی وغیرہ ہو سکتا ہے۔ وقتی سلسلے کی مثالیں یہ ہیں:','د یو شان ځانګړتیاوو د کتنو لړۍ چې د پېښېدو د وخت له مخې ترتیب شوې وي د وخت لړۍ بلل کېږي. وخت ساعت، ورځ، اوونۍ، میاشت، ربع، کال یا لسیزه او نور کېدای شي. د وخت لړۍ بېلګې دا دي:')
add(s,'e1','(i) Daily prices (Rs per kg) of a chicken shop are:','(i) مرغی کی دکان کی روزانہ قیمتیں (روپے فی کلو) ہیں:','(i) د چرګانو د هټۍ ورځنۍ بیې (روپۍ په کیلو) دا دي:')
add(s,'e2','(ii) First year admission of a college over a number of years:','(ii) کئی سالوں میں ایک کالج کے پہلے سال کے داخلے:','(ii) د څو کلونو په اوږدو کې د یو کالج د لومړي کال داخلې:')
add(s,'e3','(iii) Quarterly sale of sugar bags at a utility store in a village for the year 2015.','(iii) سال 2015 کے لیے ایک گاؤں میں یوٹیلٹی سٹور پر چینی کے تھیلوں کی سہ ماہی فروخت۔','(iii) د 2015 کال لپاره په یوه کلي کې د یوټیلټي سټور کې د بورې د کڅوړو ربعوار پلور.')
add(s,'e4','(iv) Yearly record of export and import (in metric ton) of a company:','(iv) ایک کمپنی کی برآمد اور درآمد (میٹرک ٹن میں) کا سالانہ ریکارڈ:','(iv) د یوې شرکت د صادراتو او وارداتو (په میټریک ټن) کلنی ریکارډ:')
add(s,'h2','Analysis of time series','وقتی سلسلے کا تجزیہ','د وخت لړۍ تحلیل')
add(s,'t2','The description, measurement and isolation of various changes in a time series during a period of time are called analysis of time series. Times series analysis helps in (i) understanding the real behaviour of the past (ii) predicting the future behaviour like demand, production, weather conditions, prices etc. (iii) to compare the present accomplishments with the past performance. (iv) planning','کسی مدت کے دوران وقتی سلسلے میں مختلف تبدیلیوں کی تفصیل، پیمائش اور علیحدگی وقتی سلسلے کا تجزیہ کہلاتی ہے۔ وقتی سلسلے کا تجزیہ (i) ماضی کے حقیقی رویے کو سمجھنے (ii) مستقبل کے رویے جیسے طلب، پیداوار، موسمی حالات، قیمتوں وغیرہ کی پیش گوئی (iii) موجودہ کامیابیوں کا ماضی کی کارکردگی سے موازنہ کرنے (iv) منصوبہ بندی میں مدد دیتا ہے','د یوې مودې په اوږدو کې په وخت لړۍ کې د بېلابېلو بدلونونو بیان، اندازه کول او جلا کول د وخت لړۍ تحلیل بلل کېږي. د وخت لړۍ تحلیل (i) د تېر وخت د ریښتیني چلند په پوهېدو (ii) د راتلونکي چلند لکه غوښتنه، تولید، هوا حالات، بیې او نورو په وړاندوینه (iii) د اوسنیو لاسته‌راوړنو د تېر فعالیت سره په پرتله کولو (iv) پلان جوړونې کې مرسته کوي',sourceGap=dict(note='The sentence continues on the next page ("… (iv) planning …").'))
s['tables']=[table('Daily prices of a chicken shop','مرغی کی دکان کی روزانہ قیمتیں','د چرګانو د هټۍ ورځنۍ بیې',[c('Day','دن','ورځ'),c('Sunday','اتوار','یکشنبه'),c('Monday','پیر','دوشنبه'),c('Tuesday','منگل','سه‌شنبه'),c('Wednesday','بدھ','چهارشنبه'),c('Thursday','جمعرات','پنجشنبه'),c('Friday','جمعہ','جمعه'),c('Saturday','ہفتہ','شنبه')],[[c('Price','قیمت','بیه')]+[c(str(v)) for v in [150,148,150,155,155,145,145]]]),
 table('First year admission of a college','ایک کالج کے پہلے سال کے داخلے','د یو کالج د لومړي کال داخلې',[c('Year','سال','کال')]+[c(str(v)) for v in range(2011,2017)],[[c('Number of admissions','داخلوں کی تعداد','د داخلو شمېر')]+[c(str(v)) for v in [1180,1200,1100,1240,1228,1000]]]),
 table('Quarterly sale of sugar bags, 2015','چینی کے تھیلوں کی سہ ماہی فروخت، 2015','د بورې د کڅوړو ربعوار پلور، 2015',[c('Quarter','سہ ماہی','ربع'),c('Spring','بہار','پسرلی'),c('Summer','گرمی','اوړی'),c('Autumn','خزاں','مني'),c('Winter','سردی','ژمی')],[[c('No. of bags sold','فروخت شدہ تھیلوں کی تعداد','پلورل شوو کڅوړو شمېر'),c('234'),c('270'),c('190'),c('210')]]),
 table('Yearly export and import (metric ton)','سالانہ برآمد اور درآمد (میٹرک ٹن)','کلنی صادرات او واردات (میټریک ټن)',[c('Year','سال','کال'),c('Export','برآمد','صادرات'),c('Import','درآمد','واردات')],[[c(str(a)),c(str(b)),c(str(d))] for a,b,d in [(2010,4000,1500),(2011,4500,2000),(2012,5000,1000),(2013,3000,1400)]])]
P=lambda *ks:dict(type='paragraphs',ids=[pid(206,k) for k in ks])
s['flow']=[P('h61','t1','e1'),dict(type='table',index=0),P('e2'),dict(type='table',index=1),P('e3'),dict(type='table',index=2),P('e4'),dict(type='table',index=3),P('h2','t2')]
s['sourceNote']='Printed page 196. Header graphics and watermark excluded.'
s['vocabulary']={'time series':dict(ur='وقتی سلسلہ',ps='د وخت لړۍ')}
save(s)
