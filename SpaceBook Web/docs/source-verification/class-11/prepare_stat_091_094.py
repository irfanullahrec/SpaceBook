from statlib import *
c=cell
U='central-tendency'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def L(s,items,group):
    for k,a,b,d in items: add(s,k,a,b,d,listGroup=group)
def q(s,key,en,ur,ps,ex,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,**m)
# ---------- scan 91 (printed 83) ----------
s=page(91,U,'83','Example 2.32 solution · Examples 2.33, 2.34: harmonic mean','مثال 2.32 کا حل · مثالیں 2.33، 2.34: ہارمونی اوسط','د بېلګې 2.32 حل · بېلګې 2.33، 2.34: هارمونیک اوسط','hm-examples-1')
F=Flow(s)
head(s,'sol32','Solution:','حل:','حل:',exampleId='stat11-ex-2-32')
add(s,'i2','(ii) Harmonic mean in case of discrete series or grouped data','(ii) منفصل سلسلے یا گروہی اعداد و شمار کی صورت میں ہارمونی اوسط','(ii) د منفصلې لړۍ یا ګروپي معلوماتو په حالت کې هارمونیک اوسط')
head(s,'ex33','Example: 2.33','مثال: 2.33','بېلګه: 2.33',exampleId='stat11-ex-2-33')
add(s,'q33','Calculate harmonic mean of the following distribution:','درج ذیل تقسیم کا ہارمونی اوسط حساب کریں:','د لاندې ویش هارمونیک اوسط محاسبه کړئ:',role='question',exampleId='stat11-ex-2-33')
head(s,'sol33','Solution:','حل:','حل:',exampleId='stat11-ex-2-33')
add(s,'i3','(iii) Harmonic mean in case of continuous series or grouped data','(iii) مسلسل سلسلے یا گروہی اعداد و شمار کی صورت میں ہارمونی اوسط','(iii) د دوامدارې لړۍ یا ګروپي معلوماتو په حالت کې هارمونیک اوسط')
head(s,'ex34','Example: 2.34','مثال: 2.34','بېلګه: 2.34',exampleId='stat11-ex-2-34')
add(s,'q34','Calculate the harmonic mean from the following data:','درج ذیل اعداد و شمار سے ہارمونی اوسط حساب کریں:','له لاندې معلوماتو څخه هارمونیک اوسط محاسبه کړئ:',role='question',exampleId='stat11-ex-2-34',sourceGap=dict(note='The solution follows on the next page.'))
s['tables']=[table('Example 2.32: x and 1/x','مثال 2.32: x اور 1/x','بېلګه 2.32: x او 1/x',[c('x'),c('1/x')],[[c(a),c(b)] for a,b in [('10','0.1'),('20','0.05'),('30','0.03'),('40','0.03'),('50','0.02')]]+[[c('Total','کل','ټول'),c('0.23')]],exampleId='stat11-ex-2-32',role='solution'),
 table('Example 2.33: x and f','مثال 2.33: x اور f','بېلګه 2.33: x او f',[c('x:')]+[c(str(v)) for v in [12,14,16,18,20,22]],[[c('f:')]+[c(str(v)) for v in [1,4,6,10,7,2]]],exampleId='stat11-ex-2-33'),
 table('Example 2.33: f/x','مثال 2.33: f/x','بېلګه 2.33: f/x',[c('x'),c('f'),c('f/x')],[[c(a),c(b),c(d)] for a,b,d in [('12','1','0.0833'),('14','4','0.2857'),('16','6','0.3750'),('18','10','0.5556'),('20','7','0.3500'),('22','2','0.0909')]]+[[c('Total','کل','ټول'),c('30'),c('1.7406')]],exampleId='stat11-ex-2-33',role='solution'),
 table('Example 2.34: class and frequency','مثال 2.34: جماعت اور تعدد','بېلګه 2.34: ټولګی او فریکونسي',[c('Class:','جماعت:','ټولګی:')]+[c(v) for v in ['0 – 9','10 – 19','20 – 29','30 – 39','40 – 49']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in [5,10,15,7,3]]],exampleId='stat11-ex-2-34')]
s['equations']=[eqn(91,'h1',r'\text{H.M}=\dfrac{n}{\sum\dfrac{1}{x}}=\dfrac{5}{0.23}=21.9\ \text{km/hour.}','H.M = n / (Σ 1/x) = 5/0.23 = 21.9 km/hour.',exampleId='stat11-ex-2-32'),
 eqn(91,'h2',r'\text{H.M}=\dfrac{\sum f}{\sum\dfrac{f}{x}}=\dfrac{30}{1.7406}=17.24','H.M = Σf / (Σ f/x) = 30/1.7406 = 17.24',exampleId='stat11-ex-2-33')]
F.rest()
s['flow']=[dict(type='paragraphs',ids=[pid(91,'sol32')]),dict(type='table',index=0),dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(91,k) for k in ('i2','ex33','q33')]),dict(type='table',index=1),dict(type='paragraphs',ids=[pid(91,'sol33')]),dict(type='table',index=2),dict(type='equation',index=1),dict(type='paragraphs',ids=[pid(91,k) for k in ('i3','ex34','q34')]),dict(type='table',index=3)]
s['sourceNote']='Printed page 83. In the printed table of Example 2.32 the 1/x values for 30 and 40 are both printed 0.03 (as printed; the exact values 0.0333 and 0.025 are not shown). The right-hand working is shown after each table. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 92 (printed 84) ----------
s=page(92,U,'84','Example 2.34 solution · 2.6.2 Merits and demerits of harmonic mean · 2.6.3 Relationship among A.M, G.M and H.M','مثال 2.34 کا حل · 2.6.2 ہارمونی اوسط کی خوبیاں اور خامیاں · 2.6.3 A.M، G.M اور H.M کے درمیان تعلق','د بېلګې 2.34 حل · 2.6.2 د هارمونیک اوسط ګټې او زیانونه · 2.6.3 د A.M، G.M او H.M ترمنځ اړیکه','hm-relations')
F=Flow(s)
head(s,'sol34','Solution:','حل:','حل:',exampleId='stat11-ex-2-34')
head(s,'h262','2.6.2 Merits and demerits of harmonic mean','2.6.2 ہارمونی اوسط کی خوبیاں اور خامیاں','2.6.2 د هارمونیک اوسط ګټې او زیانونه')
add(s,'mh','Merits:','خوبیاں:','ګټې:')
L(s,[('m1','(i) It considers all the given data.','(i) یہ تمام دیے گئے اعداد و شمار کو مدنظر رکھتا ہے۔','(i) دا ټول ورکړل شوي معلومات په پام کې نیسي.'),('m2','(ii) It is not affected by fluctuation of sampling.','(ii) یہ نمونہ سازی کے اتار چڑھاؤ سے متاثر نہیں ہوتا۔','(ii) دا د نمونه‌اخیستنې د بدلونونو لخوا نه اغېزمنېږي.'),('m3','(iii) It is a good average for a highly variable series.','(iii) یہ بہت زیادہ متغیر سلسلے کے لیے اچھا اوسط ہے۔','(iii) دا د ډېر متغیرې لړۍ لپاره ښه اوسط دی.')],'hm-merits')
add(s,'dh','Demerits','خامیاں','زیانونه')
L(s,[('d1','(i) It cannot be calculated if any one of the observations is zero.','(i) اگر کوئی ایک مشاہدہ صفر ہو تو اسے حساب نہیں کیا جا سکتا۔','(i) که هر یوه کتنه صفر وي نو دا نشي محاسبه کېدای.'),('d2','(ii) It gives less importance to large values and more importance to small values.','(ii) یہ بڑی قدروں کو کم اہمیت اور چھوٹی قدروں کو زیادہ اہمیت دیتا ہے۔','(ii) دا لویو ارزښتونو ته لږ اهمیت او کوچنیو ارزښتونو ته ډېر اهمیت ورکوي.'),('d3','(iii) Its value is generally not a member of the series.','(iii) اس کی قدر عموماً سلسلے کا رکن نہیں ہوتی۔','(iii) د دې ارزښت په عمومي ډول د لړۍ غړی نه وي.')],'hm-demerits')
head(s,'h263','2.6.3 Relationship among A.M, G.M and H.M','2.6.3 A.M، G.M اور H.M کے درمیان تعلق','2.6.3 د A.M، G.M او H.M ترمنځ اړیکه')
add(s,'eq','Equality will hold only when all the observations are same.','برابری صرف اس وقت ہوگی جب تمام مشاہدات یکساں ہوں۔','برابري یوازې هغه وخت وي کله چې ټولې کتنې یو شان وي.')
add(s,'t2','If two measures are known, the third one can be approximately calculated by this relation.','اگر دو پیمانے معلوم ہوں تو اس تعلق سے تیسرا تقریباً حساب کیا جا سکتا ہے۔','که دوه اندازې معلومې وي نو دریمه د دې اړیکې په واسطه نږدې محاسبه کېدای شي.')
s['tables']=[table('Example 2.34: f/x','مثال 2.34: f/x','بېلګه 2.34: f/x',[c('Classes','جماعتیں','ټولګي'),c('f'),c('x'),c('f/x')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in [('0 – 9','5','4.5','1.1111'),('10 – 19','10','14.5','0.6897'),('20 – 29','15','24.5','0.6122'),('30 – 39','7','34.5','0.2029'),('40 – 49','3','44.5','0.0674')]]+[[c('Total','کل','ټول'),c('40'),c('–'),c('2.6833')]],exampleId='stat11-ex-2-34',role='solution')]
s['equations']=[eqn(92,'h',r'\text{H.M}=\dfrac{\sum f}{\sum\dfrac{f}{x}}=\dfrac{40}{2.6833}=14.91','H.M = Σf / (Σ f/x) = 40/2.6833 = 14.91',exampleId='stat11-ex-2-34'),
 eqn(92,'r1',r'\text{(i)}\ \text{A.M}\geq\text{G.M}\geq\text{H.M}','(i) A.M ≥ G.M ≥ H.M'),
 eqn(92,'r2',r'\text{(ii)}\ \text{G.M}=\sqrt{(\text{A.M})(\text{H.M})}','(ii) G.M = √((A.M)(H.M))')]
F.rest()
s['flow']=[dict(type='paragraphs',ids=[pid(92,'sol34')]),dict(type='table',index=0),dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(92,k) for k in ('h262','mh','m1','m2','m3','dh','d1','d2','d3','h263')]),dict(type='equation',index=1),dict(type='paragraphs',ids=[pid(92,'eq')]),dict(type='equation',index=2),dict(type='paragraphs',ids=[pid(92,'t2')])]
s['sourceNote']='Printed page 84. A colour smudge at the top-left is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 93 (printed 85) ----------
s=page(93,U,'85','Key points (Unit 2)','اہم نکات (یونٹ 2)','مهم ټکي (دویم واحد)','keypoints-u2')
F=Flow(s)
head(s,'h','Key points','اہم نکات','مهم ټکي')
add(s,'k1','A single representative value is called central tendency or central value or balancing point or average.','ایک واحد نمائندہ قدر مرکزی رجحان یا مرکزی قدر یا توازن کا نقطہ یا اوسط کہلاتی ہے۔','یو واحد استازی ارزښت مرکزي تمایل یا مرکزي ارزښت یا د انډول نقطه یا اوسط بلل کېږي.',listGroup='kp',summary=True)
add(s,'k2','The sum of all given values divided by the number of values is called Arithmetic Mean.','تمام دی گئی قدروں کا مجموعہ قدروں کی تعداد پر تقسیم کرنے سے حاصل ہونے والی مقدار حسابی اوسط کہلاتی ہے۔','د ټولو ورکړل شویو ارزښتونو مجموعه د ارزښتونو په شمېر تقسیم حسابي اوسط بلل کېږي.',listGroup='kp',summary=True)
add(s,'k3','A value which divides the ordered data in to two equal parts is called median.','وہ قدر جو ترتیب دیے گئے اعداد و شمار کو دو برابر حصوں میں تقسیم کرے وسطانیہ کہلاتی ہے۔','هغه ارزښت چې ترتیب شوي معلومات په دوو مساوي برخو وېشي میانه بلل کېږي.',listGroup='kp2',summary=True)
add(s,'k4','A value that appears most often in a data set is called mode.','وہ قدر جو اعداد و شمار کے مجموعے میں سب سے زیادہ بار آئے عادہ کہلاتی ہے۔','هغه ارزښت چې په معلوماتو ټولګه کې تر ټولو ډېر ځله راځي مود بلل کېږي.',listGroup='kp2',summary=True)
add(s,'k5','Mode = 3Median − 2Mean.','عادہ = 3 وسطانیہ − 2 اوسط۔','مود = 3 میانه − 2 اوسط.',listGroup='kp2',summary=True)
add(s,'k6','The nth root of the product of n positive values is called geometric mean.','n مثبت قدروں کے حاصلِ ضرب کا n واں جذر ہندسی اوسط کہلاتا ہے۔','د n مثبتو ارزښتونو د ضرب حاصل n‌م جذر هندسي اوسط بلل کېږي.',listGroup='kp2',summary=True)
add(s,'k7','The reciprocal of the arithmetic mean of the reciprocals of the values is called harmonic mean.','قدروں کے معکوسات کے حسابی اوسط کا معکوس ہارمونی اوسط کہلاتا ہے۔','د ارزښتونو د معکوسونو د حسابي اوسط معکوس هارمونیک اوسط بلل کېږي.',listGroup='kp2',summary=True)
s['equations']=[eqn(93,'pm',r'\mu=\dfrac{\sum_{i=1}^{n}x_i}{N}\qquad\text{(Formula for population mean)}','μ = (Σ (i = 1 to n) xi) / N   (Formula for population mean)',summary=True),eqn(93,'sm',r'\bar{x}=\dfrac{\sum_{i=1}^{n}x_i}{n}\qquad\text{(Formula for sample mean)}','x̄ = (Σ (i = 1 to n) xi) / n   (Formula for sample mean)',summary=True),eqn(93,'r1',r'\text{A.M}\geq\text{G.M}\geq\text{H.M}','A.M ≥ G.M ≥ H.M',summary=True),eqn(93,'r2',r'\text{G.M}=\sqrt{(\text{A.M})(\text{H.M})}','G.M = √((A.M)(H.M))',summary=True)]
F.rest()
s['flow']=[dict(type='paragraphs',ids=[pid(93,k) for k in ('h','k1','k2')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='paragraphs',ids=[pid(93,k) for k in ('k3','k4','k5','k6','k7')]),dict(type='equation',index=2),dict(type='equation',index=3)]
s['sourceNote']='Printed page 85. In the printed population-mean formula the upper limit of the summation is n (a misprint for N) and is retained. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 94 (printed 86) ----------
s=page(94,U,'86','Exercise-2: Q2.1 True or false · Q2.2 Fill in the blanks','مشق-2: سوال 2.1 صحیح یا غلط · سوال 2.2 خالی جگہیں پُر کریں','تمرین-2: پوښتنه 2.1 سم یا غلط · پوښتنه 2.2 تشې ډکې کړئ','exercise2-a',layout='exercise')
head(s,'h','Exercise-2','مشق-2','تمرین-2',exerciseId='stat11-ex2')
head(s,'h21','2.1 State whether the following statements are true or false.','2.1 بتائیں کہ درج ذیل بیانات صحیح ہیں یا غلط۔','2.1 وښیئ چې لاندې بیانونه سم دي که غلط.',exerciseId='stat11-ex2-1')
TF=[('(i) A value which is repeated most number of times in the data set is called harmonic mean.','(i) وہ قدر جو اعداد و شمار کے مجموعے میں سب سے زیادہ بار دہرائی جائے ہارمونی اوسط کہلاتی ہے۔','(i) هغه ارزښت چې په معلوماتو ټولګه کې تر ټولو ډېر ځله تکرارېږي هارمونیک اوسط بلل کېږي.'),('(ii) Median is highly affected by extreme values.','(ii) وسطانیہ انتہائی قدروں سے بہت متاثر ہوتا ہے۔','(ii) میانه د سختو ارزښتونو لخوا ډېره اغېزمنېږي.'),('(iii) For a symmetric unimodal distribution the arithmetic mean, median and mode are not equal.','(iii) متناسب یک عادی تقسیم کے لیے حسابی اوسط، وسطانیہ اور عادہ برابر نہیں ہوتے۔','(iii) د متناسب یو‌مودي ویش لپاره حسابي اوسط، میانه او مود مساوي نه وي.'),('(iv) 5th decile = 50th percentile.','(iv) پانچواں دسواں = پچاسواں فی صدکیہ۔','(iv) پنځمه لسمه = پنځوسمه سلمه.'),('(v) The sum of deviations observations from A.M is always equal to zero.','(v) مشاہدات کے A.M سے انحرافات کا مجموعہ ہمیشہ صفر کے برابر ہوتا ہے۔','(v) د کتنو له A.M څخه د انحرافاتو مجموعه تل له صفر سره مساوي وي.'),('(vi) An average is a single value which represents the entire data.','(vi) اوسط ایک واحد قدر ہے جو پورے اعداد و شمار کی نمائندگی کرتی ہے۔','(vi) اوسط یو واحد ارزښت دی چې ټول معلومات استازیتوب کوي.'),('(vii) Geometric mean cannot be calculated if any value in the data is zero or negative.','(vii) اگر اعداد و شمار میں کوئی قدر صفر یا منفی ہو تو ہندسی اوسط حساب نہیں کیا جا سکتا۔','(vii) که په معلوماتو کې هر ارزښت صفر یا منفي وي نو هندسي اوسط نشي محاسبه کېدای.'),('(viii) Median divides the series in to two equal parts.','(viii) وسطانیہ سلسلے کو دو برابر حصوں میں تقسیم کرتا ہے۔','(viii) میانه لړۍ په دوو مساوي برخو وېشي.'),('(ix) Mode depends on all the values of the data.','(ix) عادہ اعداد و شمار کی تمام قدروں پر منحصر ہوتا ہے۔','(ix) مود د معلوماتو په ټولو ارزښتونو پورې اړه لري.'),('(x) Quartiles divide the series in to three equal parts.','(x) چوتھائیاں سلسلے کو تین برابر حصوں میں تقسیم کرتی ہیں۔','(x) څلورمې لړۍ په دریو مساوي برخو وېشي.')]
for i,(a,b,d) in enumerate(TF,1): q(s,f't{i}',a,b,d,'stat11-ex2-1',listGroup='truefalse')
head(s,'h22','2.2 Fill in the suitable words in the blanks.','2.2 خالی جگہوں میں مناسب الفاظ پُر کریں۔','2.2 په تشو کې مناسب کلمې ډکې کړئ.',exerciseId='stat11-ex2-2')
FB=[('(i) Weighted mean is more ________ than unweighted mean.','(i) وزنی اوسط غیر وزنی اوسط سے زیادہ ________ ہوتا ہے۔','(i) وزني اوسط له نه‌وزني اوسط څخه ډېر ________ دی.'),('(ii) If A.M of certain values is 9 and their G.M is 6, then the H.M is ________.','(ii) اگر کچھ قدروں کا A.M 9 ہو اور ان کا G.M 6 ہو تو H.M ________ ہے۔','(ii) که د ځینو ارزښتونو A.M 9 وي او د هغو G.M 6 وي نو H.M ________ دی.'),('(iii) A value which divides an ordered series in to two equal parts is called ________.','(iii) وہ قدر جو ترتیب دیے گئے سلسلے کو دو برابر حصوں میں تقسیم کرے ________ کہلاتی ہے۔','(iii) هغه ارزښت چې ترتیب شوې لړۍ په دوو مساوي برخو وېشي ________ بلل کېږي.'),('(iv) The variable value having maximum frequency in a frequency distribution is called ________.','(iv) تعدد تقسیم میں زیادہ سے زیادہ تعدد والی متغیر قدر ________ کہلاتی ہے۔','(iv) په فریکونسي ویش کې د اعظمي فریکونسي لرونکی متغیر ارزښت ________ بلل کېږي.'),('(v) Out of all the measures of central tendency ________ is the only measure which is not unique.','(v) مرکزی رجحان کے تمام پیمانوں میں سے ________ واحد پیمانہ ہے جو منفرد نہیں۔','(v) د مرکزي تمایل له ټولو اندازو څخه ________ یوازینۍ اندازه ده چې ځانګړې نه ده.'),('(vi) The distribution which has only one mode is called ________.','(vi) وہ تقسیم جس کا صرف ایک عادہ ہو ________ کہلاتی ہے۔','(vi) هغه ویش چې یوازې یو مود ولري ________ بلل کېږي.'),('(vii) Second quartile, 5th decile and 50th percentile are same as ________.','(vii) دوسری چوتھائی، پانچواں دسواں اور پچاسواں فی صدکیہ ________ کے برابر ہیں۔','(vii) دویمه څلورمه، پنځمه لسمه او پنځوسمه سلمه له ________ سره یو شان دي.'),('(viii) The 3rd quartile and ________ percentile are same.','(viii) تیسری چوتھائی اور ________ فی صدکیہ برابر ہیں۔','(viii) دریمه څلورمه او ________ سلمه یو شان دي.'),('(ix) The general name for quartiles, deciles and percentiles is ________.','(ix) چوتھائیوں، دسویں اور فی صدکیات کا عمومی نام ________ ہے۔','(ix) د څلورمو، لسمو او سلمو عمومي نوم ________ دی.'),('(x) The most suitable average for measuring speed, per unit of time, is ________.','(x) فی اکائی وقت رفتار ناپنے کے لیے سب سے موزوں اوسط ________ ہے۔','(x) د واحد وخت په اړه د چټکتیا د اندازې لپاره تر ټولو مناسب اوسط ________ دی.')]
for i,(a,b,d) in enumerate(FB,1): q(s,f'b{i}',a,b,d,'stat11-ex2-2',listGroup='fill')
F=Flow(s);F.done()
s['sourceNote']='Printed page 86. A colour smudge at the top-left is ignored. Blanks are drawn as underlines. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
