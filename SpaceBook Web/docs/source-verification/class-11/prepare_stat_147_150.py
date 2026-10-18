from stathelp import *
c=cell
U='dispersion-skewness-kurtosis'
def q(s,key,en,ur,ps,ex,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,**m)
def o(s,key,en,ur,ps,ex): add(s,key,en,ur,ps,role='option',exerciseId=ex)
def mcq(s,pg,i,en,ur,ps,oe,ou,op,exb):
    ex=f'{exb}-{i}'; q(s,f'm{i}',en,ur,ps,ex)
    for k,a,b,d in zip('abcd',oe,ou,op): o(s,f'm{i}{k}',a,b,d,ex)
    return [f'm{i}']+[f'm{i}{k}' for k in 'abcd']
UL=['(الف)','(ب)','(ج)','(د)']
def ur_opts(*t): return [f'{UL[i]} {x}' for i,x in enumerate(t)]
def pe_opts(*t): return [f'({"abcd"[i]}) {x}' for i,x in enumerate(t)]
def en_opts(*t): return [f'({"abcd"[i]}) {x}' for i,x in enumerate(t)]
# ---------- scan 147 (printed 139) ----------
s=page(147,U,'139','Exercise-3: Q3.1 True or false · Q3.2 Fill in the blanks · Q3.3 (i)','مشق-3: سوال 3.1 صحیح یا غلط · سوال 3.2 خالی جگہیں پُر کریں · سوال 3.3 (i)','تمرین-3: پوښتنه 3.1 سم یا غلط · پوښتنه 3.2 تشې ډکې کړئ · پوښتنه 3.3 (i)','exercise3-a',layout='exercise')
Flow(s)
head(s,'h','Exercise-3','مشق-3','تمرین-3',exerciseId='stat11-ex3')
head(s,'h31','3.1 For the following statements, write “T” for true and “F” for false statements.','3.1 درج ذیل بیانات کے لیے صحیح کے لیے “T” اور غلط کے لیے “F” لکھیں۔','3.1 د لاندې بیانونو لپاره سم لپاره “T” او غلط لپاره “F” ولیکئ.',exerciseId='stat11-ex3-1')
T1=[('The difference between the highest and lowest observations in a data set is called the quartile range.','معلوماتی مجموعے میں سب سے بڑے اور سب سے چھوٹے مشاہدات کے فرق کو چوتھائی حد کہتے ہیں۔','په معلوماتو ټولګه کې د تر ټولو لوی او تر ټولو کوچني کتنو توپیر ته څلورمه رېنج ویل کېږي.'),
('S.D is the square of the variance.','S.D تغیر کا مربع ہے۔','S.D د وریانس مربع دی.'),
('The coefficient of variation is an absolute measure of dispersion.','تغیر کا عددی سر انتشار کا ایک مطلق پیمانہ ہے۔','د تغیر ضریب د خپراوي یوه مطلقه اندازه ده.'),
('In symmetrical distribution, the mean, median and mode are equal, provided that the mode is a single number.','متناسب تقسیم میں اوسط، وسطانیہ اور عادہ برابر ہوتے ہیں، بشرطیکہ عادہ ایک ہی عدد ہو۔','په متناسب ویش کې اوسط، میانه او مود مساوي وي، په دې شرط چې مود یو واحد عدد وي.'),
('Coefficient of variation is a relative measure of dispersion.','تغیر کا عددی سر انتشار کا ایک اضافی پیمانہ ہے۔','د تغیر ضریب د خپراوي یوه نسبي اندازه ده.'),
('The normal distribution is also known as meso-kurtic distribution.','نارمل تقسیم کو میسو کرٹک تقسیم بھی کہا جاتا ہے۔','نورمال ویش ته میسو‌کرټیک ویش هم ویل کېږي.'),
('S.D(x + 9) = S.D(x)','S.D(x + 9) = S.D(x)','S.D(x + 9) = S.D(x)'),
('The S.D of 3, 3, 3, 3, 3 is zero.','3, 3, 3, 3, 3 کا S.D صفر ہے۔','د 3, 3, 3, 3, 3 S.D صفر دی.'),
('The values of S.D and variance are never negative.','S.D اور تغیر کی قدریں کبھی منفی نہیں ہوتیں۔','د S.D او وریانس ارزښتونه هېڅکله منفي نه وي.'),
('A data having least C.V is considered more consistent.','کم سے کم C.V رکھنے والا ڈیٹا زیادہ مستقل مزاج سمجھا جاتا ہے۔','هغه معلومات چې لږ تر لږه C.V ولري ډېر یو شان ګڼل کېږي.')]
R='ivx'
rom=['i','ii','iii','iv','v','vi','vii','viii','ix','x']
for i,(a,b,d) in enumerate(T1): q(s,f't{i+1}',f'({rom[i]}) {a}',f'({rom[i]}) {b}',f'({rom[i]}) {d}',f'stat11-ex3-1-{rom[i]}')
head(s,'h32','3.2 Fill in the suitable word in the blanks.','3.2 خالی جگہوں میں موزوں لفظ پُر کریں۔','3.2 په تشو کې مناسب کلمه ډکه کړئ.',exerciseId='stat11-ex3-2')
F2=[('Measure of dispersion which utilizes only extreme values is ____________.','انتشار کا وہ پیمانہ جو صرف انتہائی قدریں استعمال کرتا ہے ____________ ہے۔','د خپراوي هغه اندازه چې یوازې سخت ارزښتونه کاروي ____________ ده.'),
('Standard deviation is the ____________ of variance.','معیاری انحراف تغیر کا ____________ ہے۔','معیاري انحراف د وریانس ____________ دی.'),
('____________ mean moment represent variance.','____________ اوسطی معیارِ اثر تغیر کو ظاہر کرتا ہے۔','____________ اوسط مومنټ وریانس ښيي.'),
('For a symmetric distribution coefficient of skewness is ____________.','متناسب تقسیم کے لیے کجی کا عددی سر ____________ ہے۔','د متناسب ویش لپاره د کوړوالي ضریب ____________ دی.'),
('Less is the C.V ____________ consistent is the series.','C.V جتنا کم ہو سلسلہ اتنا ہی ____________ مستقل مزاج ہوتا ہے۔','څومره چې C.V لږ وي لړۍ هومره ____________ یو شان وي.'),
('For a meso-kurtic curve, β2 is equal to ____________.','میسو کرٹک منحنی کے لیے β2 ____________ کے برابر ہے۔','د میسو‌کرټیک منحني لپاره β2 له ____________ سره مساوي دی.'),
('Sum of squares of the deviations from mean ____________.','اوسط سے انحرافات کے مربعوں کا مجموعہ ____________۔','له اوسط څخه د انحرافاتو د مربعاتو مجموعه ____________.'),
('The S.D of the five values 6, 6, 6, 6, 6 is ____________.','پانچ قدروں 6, 6, 6, 6, 6 کا S.D ____________ ہے۔','د پنځو ارزښتونو 6, 6, 6, 6, 6 S.D ____________ دی.'),
('The lack of symmetry is called ____________.','تشاکل کی کمی کو ____________ کہتے ہیں۔','د تناسب نشتوالی ته ____________ ویل کېږي.'),
('____________ possesses all the qualities needed for good measure of dispersion.','____________ میں انتشار کے اچھے پیمانے کے لیے درکار تمام خصوصیات پائی جاتی ہیں۔','____________ د خپراوي د ښې اندازې لپاره اړینې ټولې ځانګړتیاوې لري.')]
for i,(a,b,d) in enumerate(F2): q(s,f'f{i+1}',f'({rom[i]}) {a}',f'({rom[i]}) {b}',f'({rom[i]}) {d}',f'stat11-ex3-2-{rom[i]}')
head(s,'h33','3.3 Choose the correct answer.','3.3 صحیح جواب منتخب کریں۔','3.3 سم ځواب وټاکئ.',exerciseId='stat11-ex3-3')
ids=mcq(s,147,1,'(i) The value of coefficient of kurtosis b2 can be','(i) نوکیلے پن کے عددی سر b2 کی قدر ہو سکتی ہے','(i) د تېزوالي د ضریب b2 ارزښت کېدای شي',en_opts('greater than 3','less than three','equal to 3','all of the above'),ur_opts('3 سے بڑی','3 سے کم','3 کے برابر','مندرجہ بالا سب'),pe_opts('له 3 څخه لوی','له درېو څخه کم','له 3 سره مساوي','پورتني ټول'),'stat11-ex3-3')
s['sourceNote']='Printed page 139. Handwritten answers (T/F letters, words in the blanks, a tick on (d) in 3.3 (i)) are a reader\'s marks, not printed answers; they are ignored and no answer is recorded. Item (vii) of Q3.1 is the printed expression S.D(x + 9) = S.D(x). Header graphics and watermark excluded.'
s['vocabulary']={}
F=Flow(s);F.done()
save(s)
# ---------- scan 148 (printed 140) ----------
s=page(148,U,'140','Exercise-3: Q3.3 (ii)–(x) · Q3.4','مشق-3: سوال 3.3 (ii)–(x) · سوال 3.4','تمرین-3: پوښتنه 3.3 (ii)–(x) · پوښتنه 3.4','exercise3-b',layout='exercise')
Flow(s)
M=[('(ii) The S.D and variance of a set of values will be','(ii) اقدار کے مجموعے کا S.D اور تغیر ہوگا','(ii) د ارزښتونو د ټولګې S.D او وریانس به وي',('negative','positive and negative','always positive','all of the above'),('منفی','مثبت اور منفی','ہمیشہ مثبت','مندرجہ بالا سب'),('منفي','مثبت او منفي','تل مثبت','پورتني ټول')),
('(iii) If all values in a sample are same, then their variance is','(iii) اگر نمونے میں تمام قدریں ایک جیسی ہوں تو ان کا تغیر ہے','(iii) که په نمونه کې ټول ارزښتونه یو شان وي نو د هغو وریانس دی',('zero','one','not calculable','all of the above'),('صفر','ایک','قابلِ حساب نہیں','مندرجہ بالا سب'),('صفر','یو','د محاسبې وړ نه دی','پورتني ټول')),
('(iv) ____________ is the opposite of symmetry of a distribution.','(iv) ____________ تقسیم کے تشاکل کی ضد ہے۔','(iv) ____________ د ویش د تناسب ضد دی.',('S.D','mean','skewness','M.D'),('S.D','اوسط','کجی','M.D'),('S.D','اوسط','کوړوالی','M.D')),
('(v) The first mean moment is equal to','(v) پہلا اوسطی معیارِ اثر برابر ہے','(v) لومړی اوسط مومنټ مساوي دی',('A.M','first value','zero','one'),('حسابی اوسط','پہلی قدر','صفر','ایک'),('حسابي اوسط','لومړی ارزښت','صفر','یو')),
('(vi) The second mean moment is equal to','(vi) دوسرا اوسطی معیارِ اثر برابر ہے','(vi) دویم اوسط مومنټ مساوي دی',('M.D','Q.D','variance','S.D'),('M.D','Q.D','تغیر','S.D'),('M.D','Q.D','وریانس','S.D')),
('(vii) If V(X) = 4 then V(X + 5) = ?','(vii) اگر V(X) = 4 ہو تو V(X + 5) = ؟','(vii) که V(X) = 4 وي نو V(X + 5) = ؟',('9','20','4','zero'),('9','20','4','صفر'),('9','20','4','صفر')),
('(viii) If the mean of a random variable X is 3 and S.D = 5 then the variance of a variable (2X − 5) is','(viii) اگر بے ترتیب متغیر X کا اوسط 3 اور S.D = 5 ہو تو متغیر (2X − 5) کا تغیر ہے','(viii) که د تصادفي متغیر X اوسط 3 او S.D = 5 وي نو د متغیر (2X − 5) وریانس دی',('50','100','15','40'),('50','100','15','40'),('50','100','15','40')),
('(ix) If x̄ = 10 and C.V = 40, the variance of the series is','(ix) اگر x̄ = 10 اور C.V = 40 ہو تو سلسلے کا تغیر ہے','(ix) که x̄ = 10 او C.V = 40 وي نو د لړۍ وریانس دی',('4','8','12','16'),('4','8','12','16'),('4','8','12','16')),
('(x) The relationship between M.D and S.D is:','(x) M.D اور S.D کے درمیان تعلق ہے:','(x) د M.D او S.D ترمنځ اړیکه ده:',('M.D = (2/3) S.D','M.D = (4/5) S.D','M.D = (5/6) S.D','M.D = S.D'),('M.D = (2/3) S.D','M.D = (4/5) S.D','M.D = (5/6) S.D','M.D = S.D'),('M.D = (2/3) S.D','M.D = (4/5) S.D','M.D = (5/6) S.D','M.D = S.D'))]
seq=[]
for i,(a,b,d,oe,ou,op) in enumerate(M,2):
    seq+=mcq(s,148,i,a,b,d,en_opts(*oe),ur_opts(*ou),pe_opts(*op),'stat11-ex3-3')
head(s,'h34','3.4 Explain the terms:','3.4 اصطلاحات کی وضاحت کریں:','3.4 اصطلاحات تشریح کړئ:',exerciseId='stat11-ex3-4')
q(s,'t1','(i) Dispersion','(i) انتشار','(i) خپراوی','stat11-ex3-4-i')
q(s,'t2','(ii) Measures of dispersion','(ii) انتشار کے پیمانے','(ii) د خپراوي اندازې','stat11-ex3-4-ii')
q(s,'t3','(iii) Absolute and relative measures of dispersion.','(iii) انتشار کے مطلق اور اضافی پیمانے۔','(iii) د خپراوي مطلقې او نسبي اندازې.','stat11-ex3-4-iii')
build(s,148,seq+['h34','t1','t2','t3'],[])
s['sourceNote']='Printed page 140. Handwritten ticks beside the options (for example (c) in (ii), (a) in (iii), (c) in (iv)) are a reader\'s marks, not printed answers; they are ignored and no answer is recorded. Q3.3 (iv) has a blank to be completed. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 149 (printed 141) ----------
s=page(149,U,'141','Exercise-3: Q3.5 – Q3.13 (start)','مشق-3: سوال 3.5 – 3.13 (آغاز)','تمرین-3: پوښتنې 3.5 – 3.13 (پیل)','exercise3-c',layout='exercise')
Flow(s)
q(s,'q35','3.5 Describe the role of measures of central tendency and measures of dispersion which they play in the statistical analysis.','3.5 شماریاتی تجزیے میں مرکزی رجحان کے پیمانوں اور انتشار کے پیمانوں کے کردار کو بیان کریں۔','3.5 په احصایوي تحلیل کې د مرکزي تمایل د اندازو او د خپراوي د اندازو رول بیان کړئ.','stat11-ex3-5')
q(s,'q36','3.6 Define range, coefficient of range and Semi-inter quartile range or quartile deviation.','3.6 حد، حد کا عددی سر اور نیم بین الربعی حد یا چوتھائی انحراف کی تعریف کریں۔','3.6 رېنج، د رېنج ضریب او نیمه‌منځ څلورمه رېنج یا څلورمه انحراف تعریف کړئ.','stat11-ex3-6')
q(s,'q37','3.7 The following data give the number of times the metal detector was set off by passengers at a small airport during 15 consecutive half-hour periods on March 2016. 10, 8, 0, 13, 12, 2, 7, 4, 11, 1, 20, 14, 5, 3 and 15. Calculate range, the three quartiles, semi-inter quartile range or quartile deviation and coefficient of quadratic deviation.','3.7 درج ذیل اعداد و شمار مارچ 2016 میں ایک چھوٹے ہوائی اڈے پر 15 مسلسل آدھے گھنٹے کے وقفوں کے دوران مسافروں کی وجہ سے میٹل ڈیٹیکٹر کے بجنے کی تعداد دیتے ہیں۔ 10, 8, 0, 13, 12, 2, 7, 4, 11, 1, 20, 14, 5, 3 اور 15۔ حد، تینوں چوتھائیاں، نیم بین الربعی حد یا چوتھائی انحراف اور چوتھائی انحراف کا عددی سر حساب کریں۔','3.7 لاندې معلومات د 2016 کال د مارچ په یوه کوچني هوایيډګر کې د 15 پرله‌پسې نیم ساعته وختونو په اوږدو کې د مسافرو له امله د فلزي کشف کوونکي د غږېدو شمېر ورکوي. 10, 8, 0, 13, 12, 2, 7, 4, 11, 1, 20, 14, 5, 3 او 15. رېنج، درې څلورمې، نیمه‌منځ څلورمه رېنج یا څلورمه انحراف او د څلورمې انحراف ضریب محاسبه کړئ.','stat11-ex3-7')
q(s,'q38','3.8 Compute range, semi-inter quartile range or quartile deviation and coefficient of quadratic deviation for the data given below:','3.8 نیچے دیے گئے اعداد و شمار کے لیے حد، نیم بین الربعی حد یا چوتھائی انحراف اور چوتھائی انحراف کا عددی سر حساب کریں:','3.8 د لاندې ورکړل شویو معلوماتو لپاره رېنج، نیمه‌منځ څلورمه رېنج یا څلورمه انحراف او د څلورمې انحراف ضریب محاسبه کړئ:','stat11-ex3-8')
q(s,'q39','3.9 Calculate the range, quartile deviation and its coefficient from the following data:','3.9 درج ذیل اعداد و شمار سے حد، چوتھائی انحراف اور اس کا عددی سر حساب کریں:','3.9 له لاندې معلوماتو څخه رېنج، څلورمه انحراف او د هغه ضریب محاسبه کړئ:','stat11-ex3-9')
q(s,'q310','3.10 (a) Define mean deviation and its coefficient. Discuss its disadvantages. (b) Find the mean deviation from (i) arithmetic mean (ii) median and its coefficients from the following data: 21, 19, 22, 24, 26, 17, 24, 18, 19, 25, 27, 32, 28, 36, 25.','3.10 (الف) اوسط انحراف اور اس کے عددی سر کی تعریف کریں۔ اس کے نقصانات پر بحث کریں۔ (ب) درج ذیل اعداد و شمار سے (i) حسابی اوسط (ii) وسطانیہ سے اوسط انحراف اور اس کے عددی سر معلوم کریں: 21, 19, 22, 24, 26, 17, 24, 18, 19, 25, 27, 32, 28, 36, 25۔','3.10 (a) اوسط انحراف او د هغه ضریب تعریف کړئ. د هغه زیانونه وڅېړئ. (b) له لاندې معلوماتو څخه د (i) حسابي اوسط (ii) میانې څخه اوسط انحراف او د هغه ضریبونه ومومئ: 21, 19, 22, 24, 26, 17, 24, 18, 19, 25, 27, 32, 28, 36, 25.','stat11-ex3-10',sourceGap=dict(note='The printed data list reads "24 26" with a missing comma after 24.'))
q(s,'q311','3.11 Calculate (a) mean coefficient of dispersion and (b) median coefficient of dispersion from the following data.','3.11 درج ذیل اعداد و شمار سے (الف) اوسط عددی سرِ انتشار اور (ب) وسطانی عددی سرِ انتشار حساب کریں۔','3.11 له لاندې معلوماتو څخه (a) اوسط د خپراوي ضریب او (b) میانه‌یي د خپراوي ضریب محاسبه کړئ.','stat11-ex3-11')
q(s,'q312','3.12 Compute mean deviation from mean and median from following data:','3.12 درج ذیل اعداد و شمار سے اوسط اور وسطانیہ سے اوسط انحراف حساب کریں:','3.12 له لاندې معلوماتو څخه د اوسط او میانې څخه اوسط انحراف محاسبه کړئ:','stat11-ex3-12')
q(s,'q313','3.13 (a) what is meant by standard deviation and variance what is the relationship between them. (b) The following data give the number of items purchased by each of six customers who shopped on a certain day at a supermarket: 19, 15, 20, 14,','3.13 (الف) معیاری انحراف اور تغیر سے کیا مراد ہے؟ ان کے درمیان کیا تعلق ہے؟ (ب) درج ذیل اعداد و شمار ایک سپر مارکیٹ میں کسی دن خریداری کرنے والے چھ گاہکوں میں سے ہر ایک کی خریدی گئی اشیاء کی تعداد دیتے ہیں: 19, 15, 20, 14،','3.13 (a) د معیاري انحراف او وریانس څخه څه مطلب دی؟ د دوی ترمنځ څه اړیکه ده؟ (b) لاندې معلومات په یوه سوپر مارکیټ کې د یوې ورځې د پېرېدونکو شپږو کسانو له هر یوه د پېرل شویو توکو شمېر ورکوي: 19, 15, 20, 14،','stat11-ex3-13',sourceGap=dict(note='The data list continues on the next page ("16, 18. Find its standard deviation and variance.").'))
h=['63','64','65','66','67','68','69','70','71']
s['tables']=[table('Q3.8: height and number of students','سوال 3.8: قد اور طلبہ کی تعداد','پوښتنه 3.8: قد او د زده کوونکو شمېر',[c('Height in inches:','قد انچوں میں:','قد په انچونو کې:')]+[c(v) for v in h],[[c('Number of students:','طلبہ کی تعداد:','د زده کوونکو شمېر:')]+[c(v) for v in ['4','6','10','20','30','13','12','3','2']]],exerciseId='stat11-ex3-q38'),
 table('Q3.9: ages and number of workers','سوال 3.9: عمریں اور کارکنوں کی تعداد','پوښتنه 3.9: عمرونه او د کارکوونکو شمېر',[c('Ages:','عمریں:','عمرونه:')]+[c(v) for v in ['18 – 19','20 – 24','25 – 29','30 – 34','35 – 44','45 – 49']],[[c('No. of workers:','کارکنوں کی تعداد:','د کارکوونکو شمېر:')]+[c(v) for v in ['10','22','23','30','9','6']]],exerciseId='stat11-ex3-q39'),
 table('Q3.11: size of item and frequency','سوال 3.11: شے کا سائز اور تعدد','پوښتنه 3.11: د توکي اندازه او فریکونسي',[c('Size of item:','شے کا سائز:','د توکي اندازه:')]+[c(v) for v in ['4','6','8','10','12','14','16']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(v) for v in ['2','4','5','3','2','1','4']]],exerciseId='stat11-ex3-q311'),
 table('Q3.12: classes and frequency','سوال 3.12: طبقات اور تعدد','پوښتنه 3.12: ټولګي او فریکونسي',[c('Classes:','طبقات:','ټولګي:')]+[c(v) for v in ['118 – 126','127 – 135','136 – 144','145 – 153','154 – 162','163 – 171','172 – 180']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(v) for v in ['3','5','9','12','5','4','2']]],exerciseId='stat11-ex3-q312')]
build(s,149,['q35','q36','q37','q38','T:0','q39','T:1','q310','q311','T:2','q312','T:3','q313'],[])
s['sourceNote']='Printed page 141. Small ink ticks beside question numbers (3.7, 3.8, 3.9) are a reader\'s marks and are ignored. The data of Q3.8, Q3.9, Q3.11 and Q3.12 are printed as aligned rows and are shown as tables after their questions. Printed spellings kept: "quadratic deviation" (for quartile deviation). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 150 (printed 142) ----------
s=page(150,U,'142','Exercise-3: Q3.13 (end) – Q3.18 (start)','مشق-3: سوال 3.13 (اختتام) – 3.18 (آغاز)','تمرین-3: پوښتنه 3.13 (پای) – 3.18 (پیل)','exercise3-d',layout='exercise')
Flow(s)
q(s,'q313','16, 18. Find its standard deviation and variance.','16, 18۔ اس کا معیاری انحراف اور تغیر معلوم کریں۔','16, 18. د هغه معیاري انحراف او وریانس ومومئ.','stat11-ex3-13',sourceGap=dict(note='Completes Q3.13 (b) from the previous page.'))
q(s,'q314','3.14 Consider the following two data sets: (a) Calculate the mean for each of these two data sets, and comment on the relationship between the two means. (b) Calculate the standard deviation for each of these two data sets and comment on the relationship between the two standard deviations.','3.14 درج ذیل دو ڈیٹا سیٹس پر غور کریں: (الف) ان دونوں ڈیٹا سیٹس میں سے ہر ایک کا اوسط حساب کریں اور دونوں اوسطوں کے تعلق پر تبصرہ کریں۔ (ب) ان دونوں ڈیٹا سیٹس میں سے ہر ایک کا معیاری انحراف حساب کریں اور دونوں معیاری انحرافات کے تعلق پر تبصرہ کریں۔','3.14 لاندې دوه معلوماتي سیټونه په پام کې ونیسئ: (a) د دې دوو معلوماتي سیټونو له هر یوه اوسط محاسبه کړئ او د دواړو اوسطونو په اړیکه تبصره وکړئ. (b) د دې دوو معلوماتي سیټونو له هر یوه معیاري انحراف محاسبه کړئ او د دواړو معیاري انحرافاتو په اړیکه تبصره وکړئ.','stat11-ex3-14')
q(s,'q315','3.15 Compute standard deviation, variance and coefficient of standard deviation from the following data:','3.15 درج ذیل اعداد و شمار سے معیاری انحراف، تغیر اور معیاری انحراف کا عددی سر حساب کریں:','3.15 له لاندې معلوماتو څخه معیاري انحراف، وریانس او د معیاري انحراف ضریب محاسبه کړئ:','stat11-ex3-15')
q(s,'q316','3.16 The following table gives the frequency distribution of the numbers of computers sold during the past 30 weeks at an electronics store:','3.16 درج ذیل جدول ایک الیکٹرانکس اسٹور میں پچھلے 30 ہفتوں کے دوران فروخت ہونے والے کمپیوٹروں کی تعداد کی تعدد تقسیم دیتا ہے:','3.16 لاندې جدول په یوه بریښنایي هټۍ کې د تېرو 30 اونیو په اوږدو کې د پلورل شویو کمپیوټرونو د شمېر فریکونسي ویش ورکوي:','stat11-ex3-16')
q(s,'q316b','Calculate the standard deviation and variance.','معیاری انحراف اور تغیر حساب کریں۔','معیاري انحراف او وریانس محاسبه کړئ.','stat11-ex3-16')
q(s,'q317','3.17 (a) Explain in detail the coefficient of variation. What for we use it? (b) Consider the following data','3.17 (الف) تغیر کے عددی سر کی تفصیل سے وضاحت کریں۔ ہم اسے کس لیے استعمال کرتے ہیں؟ (ب) درج ذیل اعداد و شمار پر غور کریں','3.17 (a) د تغیر ضریب په تفصیل تشریح کړئ. موږ یې د څه لپاره کاروو؟ (b) لاندې معلومات په پام کې ونیسئ','stat11-ex3-17')
q(s,'q317b','Compare the variation in the distribution of wages of the workers in two factories by computing the C.V in each case and comment on these results.','ہر صورت میں C.V حساب کر کے دو کارخانوں میں کارکنوں کی اجرتوں کی تقسیم میں تغیر کا موازنہ کریں اور ان نتائج پر تبصرہ کریں۔','په هره حالت کې C.V محاسبه کولو سره په دوو کارخانو کې د کارکوونکو د مزدورۍ په ویش کې تغیر پرتله کړئ او پر دې پایلو تبصره وکړئ.','stat11-ex3-17')
q(s,'q318','3.18 Two students x and y appeared in first year examination and obtained the following scores:','3.18 دو طلبہ x اور y پہلے سال کے امتحان میں شریک ہوئے اور درج ذیل اسکور حاصل کیے:','3.18 دوه زده کوونکي x او y د لومړي کال په ازموینه کې ګډون وکړ او لاندې نمرې یې ترلاسه کړې:','stat11-ex3-18',sourceGap=dict(note='The scores of Q3.18 are printed on the next page.'))
s['tables']=[table('Q3.14: two data sets','سوال 3.14: دو ڈیٹا سیٹس','پوښتنه 3.14: دوه معلوماتي سیټونه',[c('Data set i:','ڈیٹا سیٹ i:','معلوماتي سیټ i:'),c('8'),c('16'),c('20'),c('35')],[[c('Data set ii:','ڈیٹا سیٹ ii:','معلوماتي سیټ ii:'),c('5'),c('13'),c('17'),c('32')]],exerciseId='stat11-ex3-q314'),
 table('Q3.15: x and f','سوال 3.15: x اور f','پوښتنه 3.15: x او f',[c('x:')]+[c(v) for v in ['525','500','475','450','425','400','375']],[[c('f:')]+[c(v) for v in ['24','35','46','37','47','34','22']]],exerciseId='stat11-ex3-q315'),
 table('Q3.16: computers sold','سوال 3.16: فروخت شدہ کمپیوٹر','پوښتنه 3.16: پلورل شوي کمپیوټرونه',[c('Classes:','طبقات:','ټولګي:')]+[c(v) for v in ['19 – 20','17 – 18','15 – 16','13 – 14','11 – 12','9 – 10','7 – 8','5 – 6','3 – 4','1 – 2']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(v) for v in ['1','2','2','5','9','4','3','2','1','1']]],exerciseId='stat11-ex3-q316'),
 table('Q3.17: wages and number of workers','سوال 3.17: اجرتیں اور کارکنوں کی تعداد','پوښتنه 3.17: مزدورۍ او د کارکوونکو شمېر',[c('Wages in Rs.','اجرتیں روپوں میں','مزدورۍ په روپیو'),c('No. of workers – Factory A','کارکنوں کی تعداد – کارخانہ A','د کارکوونکو شمېر – کارخانه A'),c('No. of workers – Factory B','کارکنوں کی تعداد – کارخانہ B','د کارکوونکو شمېر – کارخانه B')],[[c(a),c(b),c(d)] for a,b,d in [('2001 – 3000','3','2'),('3001 – 4000','61','14'),('4001 – 5000','132','20'),('5001 – 6000','153','27'),('6001 – 7000','140','28'),('7001 – 8000','51','7'),('8001 – 9000','2','2')]],exerciseId='stat11-ex3-q317')]
build(s,150,['q313','q314','T:0','q315','T:1','q316','T:2','q316b','q317','T:3','q317b','q318'],[])
s['sourceNote']='Printed page 142. The first lines complete Q3.13. A black pen mark at the left of Q3.15 and handwritten notes ("Part B", a tick) near Q3.17 are ignored. The two-level table header "No. of workers / Factory A / Factory B" in Q3.17 is flattened to three columns. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
