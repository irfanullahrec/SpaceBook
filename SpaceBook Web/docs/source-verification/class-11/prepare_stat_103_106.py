from statlib import *
c=cell
U='dispersion-skewness-kurtosis'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def L(s,items,group):
    for k,a,b,d in items: add(s,k,a,b,d,listGroup=group)
# ---------- scan 103 (printed 95) ----------
s=page(103,U,'95','3.2.2 Demerits · 3.2.3 Uses of range · 3.3 Quartile deviation · Example 3.4','3.2.2 خامیاں · 3.2.3 حد کے استعمالات · 3.3 چوتھائی انحراف · مثال 3.4','3.2.2 زیانونه · 3.2.3 د رېنج کارونې · 3.3 څلورمه انحراف · بېلګه 3.4','qd-1')
F=Flow(s)
add(s,'dh','Demerits:','خامیاں:','زیانونه:')
L(s,[('d1','(i) It depends on two extreme values of a series and ignores the intermediate observations.','(i) یہ سلسلے کی دو انتہائی قدروں پر منحصر ہے اور درمیانی مشاہدات کو نظر انداز کرتا ہے۔','(i) دا د لړۍ په دوو سختو ارزښتونو پورې اړه لري او منځني کتنې له پامه غورځوي.'),('d2','(ii) It is highly influenced by abnormal value.','(ii) یہ غیر معمولی قدر سے بہت زیادہ متاثر ہوتا ہے۔','(ii) دا د غیر عادي ارزښت لخوا ډېر اغېزمن کېږي.')],'range-demerits')
head(s,'h323','3.2.3 Uses of range','3.2.3 حد کے استعمالات','3.2.3 د رېنج کارونې')
add(s,'t323','In spite of the fact that range is a rough measure of dispersion, even then it is commonly used;','اس حقیقت کے باوجود کہ حد انتشار کا ایک موٹا پیمانہ ہے، پھر بھی یہ عام طور پر استعمال ہوتی ہے؛','سره له دې چې رېنج د خپراوي یوه خام اندازه ده، بیا هم عموماً کارول کېږي؛')
L(s,[('u1','(i) in the quality control tests.','(i) معیار کی جانچ کے ٹیسٹوں میں۔','(i) د کیفیت د کنټرول په ازموینو کې.'),('u2','(ii) to measure variations in temperature during a day, a year.','(ii) ایک دن، ایک سال کے دوران درجہ حرارت میں تغیرات ناپنے کے لیے۔','(ii) د یوې ورځې، یوه کال په ترڅ کې د تودوخې د بدلونونو د اندازه کولو لپاره.'),('u3','(iii) in stock exchange quotations.','(iii) اسٹاک ایکسچینج کے نرخوں میں۔','(iii) د سټاک اېکسچینج په نرخونو کې.')],'range-uses')
head(s,'h33','3.3 Quartile deviation','3.3 چوتھائی انحراف','3.3 څلورمه انحراف')
add(s,'t33','The difference between third and first quartiles divided by 2 is called quartile deviation (Q.D). It is also known as semi-inter quartile range. Mathematically,','تیسری اور پہلی چوتھائی کے فرق کو 2 پر تقسیم کرنا چوتھائی انحراف (Q.D) کہلاتا ہے۔ اسے نیم بین الربعی حد بھی کہا جاتا ہے۔ ریاضیاتی طور پر،','د دریمې او لومړۍ څلورمې توپیر چې پر 2 وویشل شي څلورمه انحراف (Q.D) بلل کېږي. دې ته نیمه‌منځ څلورمه رېنج هم ویل کېږي. ریاضیاتي ډول،')
F.rest()
F.e('qd',r'\text{Q.D}=\dfrac{Q_3-Q_1}{2}\qquad\text{(Absolute dispersion)}','Q.D = (Q3 − Q1)/2   (Absolute dispersion)')
F.e('cqd',r'\text{Coefficient of Q.D}=\dfrac{Q_3-Q_1}{Q_3+Q_1}\qquad\text{(Relative dispersion)}','Coefficient of Q.D = (Q3 − Q1)/(Q3 + Q1)   (Relative dispersion)')
head(s,'h331','3.3.1 Calculation of quartile deviation','3.3.1 چوتھائی انحراف کا حساب','3.3.1 د څلورمې انحراف محاسبه')
add(s,'i1','(i) Quartile deviation in case of individual series or ungrouped data','(i) انفرادی سلسلے یا غیر گروہی اعداد و شمار کی صورت میں چوتھائی انحراف','(i) د انفرادي لړۍ یا نه‌ګروپ شویو معلوماتو په حالت کې څلورمه انحراف')
head(s,'ex4','Example: 3.4','مثال: 3.4','بېلګه: 3.4',exampleId='stat11-ex-3-4')
add(s,'q4','Compute quartile deviation and coefficient of quartile deviation for the following data: 21, 40, 348, 32, 29, 28, 25, 18, 17, 29, and 20.','درج ذیل اعداد و شمار کے لیے چوتھائی انحراف اور چوتھائی انحراف کا عددی سر حساب کریں: 21, 40, 348, 32, 29, 28, 25, 18, 17, 29 اور 20۔','د لاندې معلوماتو لپاره څلورمه انحراف او د څلورمې انحراف ضریب محاسبه کړئ: 21, 40, 348, 32, 29, 28, 25, 18, 17, 29 او 20.',role='question',exampleId='stat11-ex-3-4')
head(s,'sol4','Solution:','حل:','حل:',exampleId='stat11-ex-3-4')
add(s,'bd','By definition Q.D = (Q3 − Q1)/2','تعریف کے مطابق Q.D = (Q3 − Q1)/2','د تعریف له مخې Q.D = (Q3 − Q1)/2',role='solution',exampleId='stat11-ex-3-4')
add(s,'da','Data in an array is 17, 18, 20, 20, 21, 25, 28, 29, 32, 38, and 40. Here n = 11 is odd.','ترتیب شدہ اعداد و شمار 17, 18, 20, 20, 21, 25, 28, 29, 32, 38 اور 40 ہیں۔ یہاں n = 11 طاق ہے۔','په ترتیب شوي معلوماتو کې 17, 18, 20, 20, 21, 25, 28, 29, 32, 38 او 40 دي. دلته n = 11 طاق دی.',role='solution',exampleId='stat11-ex-3-4')
s['equations']+=[eqn(103,'q1a',r'\therefore\ Q_1=\left(\dfrac{n+1}{4}\right)\text{th value}','∴ Q1 = ((n + 1)/4)th value',exampleId='stat11-ex-3-4'),
 eqn(103,'q1b',r'=\left(\dfrac{11+1}{4}\right)\text{th value}=3\text{rd value}=20','= ((11 + 1)/4)th value = 3rd value = 20',exampleId='stat11-ex-3-4')]
pa=lambda k:pid(103,k)
s['flow']=[dict(type='paragraphs',ids=[pa(k) for k in ('dh','d1','d2','h323','t323','u1','u2','u3','h33','t33')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='paragraphs',ids=[pa(k) for k in ('h331','i1','ex4','q4','sol4','bd','da')]),dict(type='equation',index=2),dict(type='equation',index=3)]
s['sourceNote']='Printed page 95. In the printed Example 3.4 the question lists 348 and has 29 twice while the sorted array shows 38 and has 20 twice (the question appears to have a misprint; both are kept as printed). The first printed "Q3 − Q" in the solution is clipped and is read as Q3 − Q1. Header graphics and watermark excluded.'
s['vocabulary']={'quartile deviation':dict(ur='چوتھائی انحراف',ps='څلورمه انحراف')}
save(s)
# ---------- scan 104 (printed 96) ----------
s=page(104,U,'96','Example 3.4 (end) · Example 3.5: discrete series · Example 3.6: continuous series (start)','مثال 3.4 (اختتام) · مثال 3.5: منفصل سلسلہ · مثال 3.6: مسلسل سلسلہ (آغاز)','بېلګه 3.4 (پای) · بېلګه 3.5: منفصله لړۍ · بېلګه 3.6: دوامداره لړۍ (پیل)','qd-2')
F=Flow(s)
s['equations']+=[eqn(104,'q3a',r'Q_3=3\left(\dfrac{n+1}{4}\right)\text{th value}','Q3 = 3((n + 1)/4)th value',exampleId='stat11-ex-3-4'),
 eqn(104,'q3b',r'=3\left(\dfrac{11+1}{4}\right)\text{th value}=\dfrac{36}{4}\text{th}=9\text{th value}=32','= 3((11 + 1)/4)th value = 36/4 th = 9th value = 32',exampleId='stat11-ex-3-4'),
 eqn(104,'qd1',r'\therefore\ \text{Q.D}=\dfrac{Q_3-Q_1}{2}=\dfrac{32-20}{2}=\dfrac{12}{2}=6\qquad\text{(Absolute dispersion)}','∴ Q.D = (Q3 − Q1)/2 = (32 − 20)/2 = 12/2 = 6   (Absolute dispersion)',exampleId='stat11-ex-3-4'),
 eqn(104,'cq1',r'\text{Coefficient of Q.D}=\dfrac{Q_3-Q_1}{Q_3+Q_1}=\dfrac{32-20}{32+20}=\dfrac{12}{52}=0.23\qquad\text{(Relative dispersion)}','Coefficient of Q.D = (Q3 − Q1)/(Q3 + Q1) = (32 − 20)/(32 + 20) = 12/52 = 0.23   (Relative dispersion)',exampleId='stat11-ex-3-4'),
 eqn(104,'s1',r'\text{Since }\textstyle\sum f=477\text{ is odd},\ \therefore\ Q_1=\left(\dfrac{\sum f+1}{4}\right)\text{th value}=\left(\dfrac{477+1}{4}\right)\text{th value}','Since Σf = 477 is odd, ∴ Q1 = ((Σf + 1)/4)th value = ((477 + 1)/4)th value',exampleId='stat11-ex-3-5'),
 eqn(104,'s2',r'=\left(\dfrac{478}{4}\right)\text{th value}=119.5\text{th value}\ \Rightarrow\ Q_1=2','= (478/4)th value = 119.5th value ⇒ Q1 = 2',exampleId='stat11-ex-3-5'),
 eqn(104,'s3',r'Q_3=3\left(\dfrac{\sum f+1}{4}\right)\text{th value}=3\left(\dfrac{477+1}{4}\right)\text{th value}=358.5\text{th value}\ \Rightarrow\ Q_3=5','Q3 = 3((Σf + 1)/4)th value = 3((477 + 1)/4)th value = 358.5th value ⇒ Q3 = 5',exampleId='stat11-ex-3-5'),
 eqn(104,'s4',r'\text{Q.D}=\dfrac{Q_3-Q_1}{2}=\dfrac{5-2}{2}=\dfrac{3}{2}=1.5\qquad\text{(Absolute dispersion)}','Q.D = (Q3 − Q1)/2 = (5 − 2)/2 = 3/2 = 1.5   (Absolute dispersion)',exampleId='stat11-ex-3-5'),
 eqn(104,'s5',r'\text{Coefficient of Q.D}=\dfrac{Q_3-Q_1}{Q_3+Q_1}=\dfrac{5-2}{5+2}=\dfrac{3}{7}=0.43\qquad\text{(Relative dispersion)}','Coefficient of Q.D = (Q3 − Q1)/(Q3 + Q1) = (5 − 2)/(5 + 2) = 3/7 = 0.43   (Relative dispersion)',exampleId='stat11-ex-3-5')]
add(s,'i2','(ii) Quartile deviation in case of discrete series or grouped data','(ii) منفصل سلسلے یا گروہی اعداد و شمار کی صورت میں چوتھائی انحراف','(ii) د منفصلې لړۍ یا ګروپي معلوماتو په حالت کې څلورمه انحراف')
head(s,'ex5','Example: 3.5','مثال: 3.5','بېلګه: 3.5',exampleId='stat11-ex-3-5')
add(s,'q5','Find quartile deviation and coefficient of quartile deviation from the given distribution.','دی گئی تقسیم سے چوتھائی انحراف اور چوتھائی انحراف کا عددی سر معلوم کریں۔','له ورکړل شوي ویش څخه څلورمه انحراف او د څلورمې انحراف ضریب ومومئ.',role='question',exampleId='stat11-ex-3-5')
head(s,'sol5','Solution:','حل:','حل:',exampleId='stat11-ex-3-5')
add(s,'i3','(iii) Quartile deviation in case of continuous series or grouped data','(iii) مسلسل سلسلے یا گروہی اعداد و شمار کی صورت میں چوتھائی انحراف','(iii) د دوامدارې لړۍ یا ګروپي معلوماتو په حالت کې څلورمه انحراف')
head(s,'ex6','Example: 3.6','مثال: 3.6','بېلګه: 3.6',exampleId='stat11-ex-3-6')
add(s,'q6','Calculate quartile deviation and coefficient of quartile deviation of the data given below:','نیچے دیے گئے اعداد و شمار کا چوتھائی انحراف اور چوتھائی انحراف کا عددی سر حساب کریں:','د لاندې ورکړل شویو معلوماتو څلورمه انحراف او د څلورمې انحراف ضریب محاسبه کړئ:',role='question',exampleId='stat11-ex-3-6',sourceGap=dict(note='The data of Example 3.6 are printed at the top of the next page.'))
xs=[1,2,3,4,5,6,7]; fs=[26,113,120,95,60,42,21]; cf=[26,139,259,354,414,456,477]
s['tables']=[table('Example 3.5: x and f','مثال 3.5: x اور f','بېلګه 3.5: x او f',[c('x:')]+[c(str(v)) for v in xs],[[c('f:')]+[c(str(v)) for v in fs]],exampleId='stat11-ex-3-5'),
 table('Example 3.5 solution: x, f, c.f','مثال 3.5 کا حل: x, f, c.f','د بېلګې 3.5 حل: x, f, c.f',[c('x'),c('f'),c('c.f')],[[c(str(a)),c(str(b)),c(str(d))] for a,b,d in zip(xs,fs,cf)]+[[c('Total','میزان','ټولیز'),c('477'),c('–')]],exampleId='stat11-ex-3-5')]
F.rest()
pa=lambda k:pid(104,k)
s['flow']=[dict(type='equation',index=0),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='paragraphs',ids=[pa(k) for k in ('i2','ex5','q5')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pa('sol5')]),dict(type='table',index=1),dict(type='equation',index=4),dict(type='equation',index=5),dict(type='equation',index=6),dict(type='equation',index=7),dict(type='equation',index=8),dict(type='paragraphs',ids=[pa(k) for k in ('i3','ex6','q6')])]
s['sourceNote']='Printed page 96. The first lines complete Example 3.4. In Example 3.5 the solution table has c.f. 26, 139, 259, 354, 414, 456, 477 with total frequency 477; the working is printed beside the table and is kept in reading order after it. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 105 (printed 97) ----------
s=page(105,U,'97','Example 3.6 (data and solution) · 3.3.2 Merits and demerits of quartile deviation','مثال 3.6 (اعداد و شمار اور حل) · 3.3.2 چوتھائی انحراف کی خوبیاں اور خامیاں','بېلګه 3.6 (معلومات او حل) · 3.3.2 د څلورمې انحراف ګټې او زیانونه','qd-3')
F=Flow(s)
s['equations']+=[eqn(105,'e1',r'\because\ \textstyle\sum f=36\text{ is even}\ \therefore\ Q_1=\dfrac{\sum f}{4}=\dfrac{36}{4}=9\text{th value}','∵ Σf = 36 is even ∴ Q1 = Σf/4 = 36/4 = 9th value',exampleId='stat11-ex-3-6'),
 eqn(105,'e2',r'\Rightarrow\ Q_1\text{ lies in the group }(19.5-29.5)','⇒ Q1 lies in the group (19.5 − 29.5)',exampleId='stat11-ex-3-6'),
 eqn(105,'e3',r'\text{So }Q_1=l_1+\dfrac{h}{f}\left(\dfrac{\sum f}{4}-c\right)=19.5+\dfrac{10}{8}(9-3)=27','So Q1 = l1 + (h/f)(Σf/4 − c) = 19.5 + (10/8)(9 − 3) = 27',exampleId='stat11-ex-3-6'),
 eqn(105,'e4',r'\text{Also }Q_3=3\left(\dfrac{\sum f}{4}\right)=3\left(\dfrac{36}{4}\right)=27\text{th value}','Also Q3 = 3(Σf/4) = 3(36/4) = 27th value',exampleId='stat11-ex-3-6'),
 eqn(105,'e5',r'\text{It means that }Q_3\text{ lies in the group }(39.5-49.5)','It means that Q3 lies in the group (39.5 − 49.5)',exampleId='stat11-ex-3-6'),
 eqn(105,'e6',r'\text{So }Q_3=l_1+\dfrac{h}{f}\left(\dfrac{3\sum f}{4}-c\right)=39.5+\dfrac{10}{7}(27-25)=42.4','So Q3 = l1 + (h/f)(3Σf/4 − c) = 39.5 + (10/7)(27 − 25) = 42.4',exampleId='stat11-ex-3-6'),
 eqn(105,'e7',r'\text{Q.D}=\dfrac{Q_3-Q_1}{2}=\dfrac{42.4-27}{2}=7.7\qquad\text{(Absolute dispersion)}','Q.D = (Q3 − Q1)/2 = (42.4 − 27)/2 = 7.7   (Absolute dispersion)',exampleId='stat11-ex-3-6'),
 eqn(105,'e8',r'\text{Coefficient of Q.D}=\dfrac{Q_3-Q_1}{Q_3+Q_1}=\dfrac{42.4-27}{42.4+27}=\dfrac{15.4}{69.4}=0.22\qquad\text{(Relative dispersion)}','Coefficient of Q.D = (Q3 − Q1)/(Q3 + Q1) = (42.4 − 27)/(42.4 + 27) = 15.4/69.4 = 0.22   (Relative dispersion)',exampleId='stat11-ex-3-6')]
head(s,'sol6','Solution:','حل:','حل:',exampleId='stat11-ex-3-6')
head(s,'h332','3.3.2 Merits and demerits of quartile deviation','3.3.2 چوتھائی انحراف کی خوبیاں اور خامیاں','3.3.2 د څلورمې انحراف ګټې او زیانونه')
add(s,'mh','Merits:','خوبیاں:','ګټې:')
L(s,[('m1','(i) It is easy to calculate.','(i) اس کا حساب آسان ہے۔','(i) محاسبه یې اسانه ده.'),('m2','(ii) It is not affected by extreme values.','(ii) یہ انتہائی قدروں سے متاثر نہیں ہوتا۔','(ii) دا د سختو ارزښتونو لخوا نه اغېزمن کېږي.')],'qd-merits')
add(s,'dh','Demerits:','خامیاں:','زیانونه:')
L(s,[('d1','(i) It is not based on all observations of a series.','(i) یہ سلسلے کے تمام مشاہدات پر مبنی نہیں ہے۔','(i) دا د لړۍ پر ټولو کتنو والړ نه دی.'),('d2','(ii) It is not capable of further mathematical treatment.','(ii) یہ مزید ریاضیاتی عمل کے قابل نہیں ہے۔','(ii) دا د نورې ریاضیاتي پروسې وړ نه دی.')],'qd-demerits')
mk=['10 – 19','20 – 29','30 – 39','40 – 49','50 – 49']
fq=[3,8,14,7,4]
add(s,'q6b','Marks: 10 – 19, 20 – 29, 30 – 39, 40 – 49, 50 – 49 with frequencies 3, 8, 14, 7, 4 (data of Example 3.6).','نمبر: 10 – 19، 20 – 29، 30 – 39، 40 – 49، 50 – 49 اور تعدد 3، 8، 14، 7، 4 (مثال 3.6 کے اعداد و شمار)۔','نمرې: 10 – 19، 20 – 29، 30 – 39، 40 – 49، 50 – 49 او فریکونسي 3، 8، 14، 7، 4 (د بېلګې 3.6 معلومات).',role='question',exampleId='stat11-ex-3-6',sourceGap=dict(note='Continues the question of Example 3.6 from the previous page; the last class is printed "50 – 49" in the question row (a misprint for 50 – 59).'))
s['tables']=[table('Example 3.6: marks and frequency','مثال 3.6: نمبر اور تعدد','بېلګه 3.6: نمرې او فریکونسي',[c('Marks:','نمبر:','نمرې:')]+[c(v) for v in mk],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in fq]],exampleId='stat11-ex-3-6'),
 table('Example 3.6 solution: marks, f, c.f, class boundaries','مثال 3.6 کا حل: نمبر، f، c.f، طبقاتی حدود','د بېلګې 3.6 حل: نمرې، f، c.f، د ټولګیو حدود',[c('Marks','نمبر','نمرې'),c('f'),c('c.f'),c('class boundaries','طبقاتی حدود','د ټولګیو حدود')],
  [[c(a),c(str(b)),c(str(d)),c(e)] for a,b,d,e in [('10 – 19',3,3,'9.5 – 19.5'),('20 – 29',8,11,'19.5 – 29.5'),('30 – 39',14,25,'29.5 – 39.5'),('40 – 49',7,32,'39.5 – 49.5'),('50 – 59',4,36,'49.5 – 59.5')]]+[[c('Total','میزان','ټولیز'),c('36'),c('–'),c('–')]],exampleId='stat11-ex-3-6')]
F.rest()
pa=lambda k:pid(105,k)
s['flow']=[dict(type='paragraphs',ids=[pa('q6b')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pa('sol6')]),dict(type='table',index=1)]+[dict(type='equation',index=i) for i in range(8)]+[dict(type='paragraphs',ids=[pa(k) for k in ('h332','mh','m1','m2','dh','d1','d2')])]
s['sourceNote']='Printed page 97. The page begins with the data rows of Example 3.6 (printed as a text row, last class "50 – 49" in the question row but "50 – 59" in the solution table). In the printed Q.D line the first term of the numerator appears as "4 .4 − 27" (read as 42.4 − 27). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 106 (printed 98) ----------
s=page(106,U,'98','3.4 Mean deviation · 3.4.1 Calculation · Example 3.7 (table)','3.4 اوسط انحراف · 3.4.1 حساب · مثال 3.7 (جدول)','3.4 اوسط انحراف · 3.4.1 محاسبه · بېلګه 3.7 (جدول)','md-1')
F=Flow(s)
head(s,'h34','3.4 Mean Deviation:','3.4 اوسط انحراف:','3.4 اوسط انحراف:')
add(s,'t34','The arithmetic mean of the absolute deviations of observations taken from mean or median or mode is called mean deviation. Symbolically it is written as;','اوسط یا وسطانیہ یا عادہ سے لیے گئے مشاہدات کے مطلق انحرافات کا حسابی اوسط اوسط انحراف کہلاتا ہے۔ علامتی طور پر اسے یوں لکھا جاتا ہے؛','د اوسط یا میانې یا مود څخه اخیستل شویو کتنو د مطلقو انحرافاتو حسابي اوسط اوسط انحراف بلل کېږي. په علامتي ډول دا داسې لیکل کېږي؛')
add(s,'t34b','These formulas are used for absolute dispersion. Its relative measure is coefficient of mean division defined as;','یہ فارمولے مطلق انتشار کے لیے استعمال ہوتے ہیں۔ اس کا اضافی پیمانہ اوسط انحراف کا عددی سر ہے جس کی تعریف یوں ہے؛','دا فورمولونه د مطلق خپراوي لپاره کارول کېږي. د دې نسبي اندازه د اوسط انحراف ضریب دی چې په دې توګه تعریف شوی؛')
add(s,'t34c','Note that M.D from mode is rarely used so we ignore it for computations.','نوٹ کریں کہ عادہ سے M.D شاذ و نادر استعمال ہوتا ہے اس لیے ہم حساب کے لیے اسے نظر انداز کرتے ہیں۔','پام وکړئ چې د مود څخه M.D په ندرت کارول کېږي نو موږ یې د محاسبې لپاره پرېږدو.')
head(s,'h341','3.4.1 Calculation of mean deviation','3.4.1 اوسط انحراف کا حساب','3.4.1 د اوسط انحراف محاسبه')
add(s,'i1','(i) Mean deviation in case of individual series or ungrouped data','(i) انفرادی سلسلے یا غیر گروہی اعداد و شمار کی صورت میں اوسط انحراف','(i) د انفرادي لړۍ یا نه‌ګروپ شویو معلوماتو په حالت کې اوسط انحراف')
head(s,'ex7','Example: 3.7','مثال: 3.7','بېلګه: 3.7',exampleId='stat11-ex-3-7')
add(s,'q7','Compute mean deviation from (i) arithmetic mean (ii) median and coefficient of mean division from the values 2, 6, 9, 12, 8, 13, 5, 6, 23 and 16.','(i) حسابی اوسط (ii) وسطانیہ سے اوسط انحراف اور اوسط انحراف کا عددی سر قدروں 2, 6, 9, 12, 8, 13, 5, 6, 23 اور 16 سے حساب کریں۔','له (i) حسابي اوسط (ii) میانې څخه اوسط انحراف او د اوسط انحراف ضریب د ارزښتونو 2, 6, 9, 12, 8, 13, 5, 6, 23 او 16 څخه محاسبه کړئ.',role='question',exampleId='stat11-ex-3-7')
head(s,'sol7','Solution:','حل:','حل:',exampleId='stat11-ex-3-7')
s['equations']+=[eqn(106,'m1',r'\text{M.D}=\dfrac{\sum|x-\text{Mean}|}{n}\ \text{ or }\ \dfrac{\sum|x-\text{Median}|}{n}\ \text{ or }\ \dfrac{\sum|x-\text{Mode}|}{n}\qquad\text{(For ungrouped data)}','M.D = Σ|x − Mean|/n or Σ|x − Median|/n or Σ|x − Mode|/n   (For ungrouped data)'),
 eqn(106,'m2',r'\text{M.D}=\dfrac{\sum f|x-\text{Mean}|}{\sum f}\ \text{ or }\ \dfrac{\sum f|x-\text{Median}|}{\sum f}\ \text{ or }\ \dfrac{\sum f|x-\text{Mode}|}{\sum f}\qquad\text{(For grouped data)}','M.D = Σf|x − Mean|/Σf or Σf|x − Median|/Σf or Σf|x − Mode|/Σf   (For grouped data)'),
 eqn(106,'m3',r'\text{Coefficient of M.D}=\dfrac{\text{M.D}}{\text{Mean}}\ \text{ or }\ \dfrac{\text{M.D}}{\text{Median}}','Coefficient of M.D = M.D/Mean or M.D/Median')]
xv=[2,6,9,12,8,13,5,6,23,16]
mn=[-8,-4,-1,2,-2,3,-5,-4,13,6]; am=[8,4,1,2,2,3,5,4,13,6]
md=['-6.5','-2.5','0.5','3.5','-0.5','4.5','-3.5','-2.5','14.5','7.5']; amd=['6.5','2.5','0.5','3.5','0.5','4.5','3.5','2.5','14.5','7.5']
s['tables']=[table('Example 3.7: deviations from mean and median','مثال 3.7: اوسط اور وسطانیہ سے انحرافات','بېلګه 3.7: له اوسط او میانې څخه انحرافات',[c('x'),c('x − x̄'),c('|x − x̄|'),c('x − Median'),c('|x − Median|')],
 [[c(str(a)),c(str(b)),c(str(d)),c(e),c(f)] for a,b,d,e,f in zip(xv,mn,am,md,amd)]+[[c('100'),c('–'),c('48'),c('–'),c('46')]],exampleId='stat11-ex-3-7')]
F.rest()
pa=lambda k:pid(106,k)
s['flow']=[dict(type='paragraphs',ids=[pa(k) for k in ('h34','t34')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='paragraphs',ids=[pa('t34b')]),dict(type='equation',index=2),dict(type='paragraphs',ids=[pa(k) for k in ('t34c','h341','i1','ex7','q7','sol7')]),dict(type='table',index=0)]
s['sourceNote']='Printed page 98. Printed wording kept: "rarely" is spelled "rarely" with a dropped letter in the scan, and "coefficient of mean division" is used for coefficient of mean deviation. In the table the minus signs of the median column are printed with stray spacing ("−6 .5"). The solution continues on the next page. Header graphics and watermark excluded.'
s['vocabulary']={'mean deviation':dict(ur='اوسط انحراف',ps='اوسط انحراف')}
save(s)
