from statlib import *
c=cell
U='central-tendency'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def L(s,items,group):
    for k,a,b,d in items: add(s,k,a,b,d,listGroup=group)
# ---------- scan 71 (printed 63) ----------
s=page(71,U,'63','Combined mean · Example 2.10 · 2.2.5 Advantages of arithmetic mean','مشترکہ اوسط · مثال 2.10 · 2.2.5 حسابی اوسط کے فوائد','ګډ اوسط · بېلګه 2.10 · 2.2.5 د حسابي اوسط ګټې','combined-mean')
F=Flow(s)
F.e('cm',r'\bar{x}_c=\dfrac{n_1\bar{x}_1+n_2\bar{x}_2+\cdots+n_k\bar{x}_k}{n_1+n_2+\cdots+n_k}=\dfrac{\sum_{i=1}^{k}n_i\bar{x}_i}{\sum_{i=1}^{k}n_i}','x̄c = (n1 x̄1 + n2 x̄2 + ⋯ + nk x̄k)/(n1 + n2 + ⋯ + nk) = (Σ (i = 1 to k) ni x̄i)/(Σ (i = 1 to k) ni)')
head(s,'ex','Example: 2.10','مثال: 2.10','بېلګه: 2.10',exampleId='stat11-ex-2-10')
add(s,'q','The mean weight and number of fishes in three different samples are given below:','تین مختلف نمونوں میں مچھلیوں کا اوسط وزن اور تعداد نیچے دی گئی ہے:','په دریو بېلابېلو نمونو کې د کب اوسط وزن او شمېر لاندې ورکړل شوي:',role='question',exampleId='stat11-ex-2-10')
s['tables']=[table('Example 2.10: samples of fish','مثال 2.10: مچھلیوں کے نمونے','بېلګه 2.10: د کبانو نمونې',[c('Sample','نمونہ','نمونه'),c('No. of fish','مچھلیوں کی تعداد','د کبانو شمېر'),c('Mean weight (in grams)','اوسط وزن (گرام میں)','اوسط وزن (په ګرامو)')],[[c('1'),c('50'),c('113')],[c('2'),c('60'),c('120')],[c('3'),c('70'),c('115')]],exampleId='stat11-ex-2-10')]
F.rest();F.tb(0)
add(s,'q2','Calculate the mean weight of all the fishes taken together.','تمام مچھلیوں کو ملا کر ان کا اوسط وزن حساب کریں۔','ټول کبان یوځای کولو سره د هغو اوسط وزن محاسبه کړئ.',role='question',exampleId='stat11-ex-2-10')
head(s,'sol','Solution:','حل:','حل:',exampleId='stat11-ex-2-10')
add(s,'a','The mean weight of the combined samples is','مشترکہ نمونوں کا اوسط وزن ہے','د ګډو نمونو اوسط وزن دی',role='solution',exampleId='stat11-ex-2-10')
F.rest()
F.e('s1',r'\bar{x}_c=\dfrac{n_1\bar{x}_1+n_2\bar{x}_2+n_3\bar{x}_3}{n_1+n_2+n_3}','x̄c = (n1 x̄1 + n2 x̄2 + n3 x̄3)/(n1 + n2 + n3)',exampleId='stat11-ex-2-10')
F.e('s2',r'=\dfrac{50(113)+60(120)+70(115)}{50+60+70}','= (50(113) + 60(120) + 70(115))/(50 + 60 + 70)',exampleId='stat11-ex-2-10')
F.e('s3',r'=\dfrac{5650+7200+8050}{180}=\dfrac{20900}{180}=116.11','= (5650 + 7200 + 8050)/180 = 20900/180 = 116.11',exampleId='stat11-ex-2-10')
head(s,'h225','2.2.5 Advantages of arithmetic mean','2.2.5 حسابی اوسط کے فوائد','2.2.5 د حسابي اوسط ګټې')
L(s,[('a1','i. It is very simple to understand and to calculate.','i. اسے سمجھنا اور حساب کرنا بہت آسان ہے۔','i. دا د پوهېدو او محاسبې لپاره ډېر ساده دی.'),('a2','ii. It is familiar to all and most frequently used.','ii. یہ سب کے لیے مانوس ہے اور سب سے زیادہ استعمال ہوتا ہے۔','ii. دا د ټولو لپاره پېژندل شوی او تر ټولو ډېر کارېږي.'),('a3','iii. It considers all observations i.e. every value of the data set adds to Σx and contributes one point to n to determine the value of mean.','iii. یہ تمام مشاہدات کو مدنظر رکھتا ہے یعنی اعداد و شمار کے مجموعے کی ہر قدر Σx میں اضافہ کرتی ہے اور اوسط کی قدر معلوم کرنے کے لیے n میں ایک نقطے کا حصہ ڈالتی ہے۔','iii. دا ټولې کتنې په پام کې نیسي یعنې د معلوماتو د ټولګې هر ارزښت په Σx کې زیاتوالی راولي او د اوسط د ارزښت د موندلو لپاره په n کې یو نقطه ور اضافه کوي.'),('a4','iv. It is capable of further algebraic treatment that is used to evaluate mean deviation and standard deviation.','iv. یہ مزید الجبری عمل کے قابل ہے جو اوسط انحراف اور معیاری انحراف کا اندازہ لگانے میں استعمال ہوتا ہے۔','iv. دا د نورې الجبري پروسې وړ دی چې د اوسط انحراف او معیاري انحراف د ارزونې لپاره کارول کېږي.'),('a5','v. It is determined for almost every kind of quantitative data.','v. یہ تقریباً ہر قسم کے مقداری اعداد و شمار کے لیے معلوم کیا جاتا ہے۔','v. دا د نږدې هر ډول کمیتي معلوماتو لپاره ټاکل کېږي.')],'advantages')
F.done()
s['sourceNote']='Printed page 63. The foot of the scan shows a ghost of the following page-number bar ("93") from another page, ignored. Header graphics and watermark excluded.'
s['vocabulary']={'combined mean':dict(ur='مشترکہ اوسط',ps='ګډ اوسط')}
save(s)
# ---------- scan 72 (printed 64) ----------
s=page(72,U,'64','2.2.6 Disadvantages · 2.2.7 Weighted arithmetic mean · Example 2.11','2.2.6 خامیاں · 2.2.7 وزنی حسابی اوسط · مثال 2.11','2.2.6 زیانونه · 2.2.7 وزني حسابي اوسط · بېلګه 2.11','weighted-mean')
F=Flow(s)
head(s,'h226','2.2.6 Disadvantages of arithmetic mean','2.2.6 حسابی اوسط کی خامیاں','2.2.6 د حسابي اوسط زیانونه')
L(s,[('d1','(i) It cannot be applied to qualitative data.','(i) اسے کیفی اعداد و شمار پر لاگو نہیں کیا جا سکتا۔','(i) دا پر کیفي معلوماتو نشي پلي کېدای.'),('d2','(ii) It is highly affected by extreme values, especially when the number of observations is very small.','(ii) یہ انتہائی قدروں سے بہت متاثر ہوتا ہے، خاص طور پر جب مشاہدات کی تعداد بہت کم ہو۔','(ii) دا د سختو ارزښتونو لخوا ډېر اغېزمن کېږي، په ځانګړي ډول کله چې د کتنو شمېر ډېر لږ وي.'),('d3','(iii) It is not useful for highly skewed distributions.','(iii) یہ بہت زیادہ کج تقسیمات کے لیے مفید نہیں ہے۔','(iii) دا د ډېر کوړو ویشونو لپاره ګټور نه دی.'),('d4','(iv) It cannot be calculated for incomplete data.','(iv) اسے نامکمل اعداد و شمار کے لیے حساب نہیں کیا جا سکتا۔','(iv) دا د نیمګړو معلوماتو لپاره نشي محاسبه کېدای.'),('d5','(v) It may be a figure which does not exist in a series.','(v) یہ ایک ایسا عدد ہو سکتا ہے جو سلسلے میں موجود نہ ہو۔','(v) دا یو داسې عدد کېدای شي چې په لړۍ کې شتون ونلري.')],'disadvantages')
head(s,'h227','2.2.7 Weighted arithmetic mean','2.2.7 وزنی حسابی اوسط','2.2.7 وزني حسابي اوسط')
add(s,'t227','Arithmetic mean gives equal importance to all observations of a series but in daily life we see that all observations are not equally important, some are more important than others. For example, one kg of sugar, tea and salt do not have the same price. The subjects English, Mathematics, Urdu are not equally difficult. In order to make them equally important certain numerical values are assigned, called weights. For example, if the observations are prices, then weights are assigned in the form of quantities. If the observations are quantities, then weights are assigned in the form of prices. Formula for weighted arithmetic mean is','حسابی اوسط سلسلے کے تمام مشاہدات کو برابر اہمیت دیتا ہے لیکن روزمرہ زندگی میں ہم دیکھتے ہیں کہ تمام مشاہدات برابر اہم نہیں ہوتے، کچھ دوسروں سے زیادہ اہم ہوتے ہیں۔ مثال کے طور پر ایک کلوگرام چینی، چائے اور نمک کی قیمت یکساں نہیں ہوتی۔ انگریزی، ریاضی، اردو کے مضامین برابر مشکل نہیں ہیں۔ انہیں برابر اہم بنانے کے لیے کچھ عددی قدریں مقرر کی جاتی ہیں جنہیں وزن کہتے ہیں۔ مثال کے طور پر اگر مشاہدات قیمتیں ہوں تو وزن مقداروں کی صورت میں مقرر کیے جاتے ہیں۔ اگر مشاہدات مقداریں ہوں تو وزن قیمتوں کی صورت میں مقرر کیے جاتے ہیں۔ وزنی حسابی اوسط کا فارمولا ہے','حسابي اوسط د لړۍ ټولو کتنو ته مساوي اهمیت ورکوي خو په ورځني ژوند کې موږ ګورو چې ټولې کتنې مساوي مهمې نه دي، ځینې له نورو مهمې دي. د مثال په توګه یو کیلوګرام بوره، چای او مالګه یو شان بیه نه لري. د انګلیسي، ریاضي، اردو مضامین مساوي ستونزمن نه دي. د دې لپاره چې دوی مساوي مهم وګرځي ځینې شمېرنیز ارزښتونه ټاکل کېږي چې وزنونه بلل کېږي. د مثال په توګه که کتنې بیې وي نو وزنونه د کچو په بڼه ټاکل کېږي. که کتنې کچې وي نو وزنونه د بیو په بڼه ټاکل کېږي. د وزني حسابي اوسط فورمول دی')
F.rest()
F.e('w',r'\bar{x}_w=\dfrac{\sum_{i=1}^{n}w_ix_i}{\sum_{i=1}^{n}w_i}','x̄w = (Σ (i = 1 to n) wi xi)/(Σ (i = 1 to n) wi)')
add(s,'t2','Weighted arithmetic mean is more accurate than unweighted arithmetic mean. This average is used in the construction of index numbers.','وزنی حسابی اوسط غیر وزنی حسابی اوسط سے زیادہ درست ہوتا ہے۔ یہ اوسط اشاریہ اعداد کی تشکیل میں استعمال ہوتا ہے۔','وزني حسابي اوسط له نه‌وزني حسابي اوسط څخه ډېر دقیق دی. دا اوسط د شاخصي شمېرو په جوړولو کې کارول کېږي.')
head(s,'ex','Example: 2.11','مثال: 2.11','بېلګه: 2.11',exampleId='stat11-ex-2-11')
add(s,'q','A candidate got 73% marks in English, 82% in Mathematics 57% in chemistry, 62% in physics and 60% in Urdu. Find the weighted mean if the weights 4, 3, 3, 1, 1 are allotted to the subjects.','ایک امیدوار نے انگریزی میں 73%، ریاضی میں 82%، کیمیا میں 57%، طبیعیات میں 62% اور اردو میں 60% نمبر حاصل کیے۔ وزنی اوسط معلوم کریں اگر مضامین کو وزن 4, 3, 3, 1, 1 دیے گئے ہوں۔','یو نوماند په انګلیسي کې 73%، په ریاضي کې 82%، په کیمیا کې 57%، په فزیک کې 62% او په اردو کې 60% نمرې ترلاسه کړې. وزني اوسط ومومئ که چېرې مضامینو ته وزنونه 4, 3, 3, 1, 1 ورکړل شوي وي.',role='question',exampleId='stat11-ex-2-11')
head(s,'sol','Solution:','حل:','حل:',exampleId='stat11-ex-2-11')
s['tables']=[table('Example 2.11: marks, weights and wx','مثال 2.11: نمبر، وزن اور wx','بېلګه 2.11: نمرې، وزنونه او wx',[c('x'),c('w'),c('wx')],[[c(a),c(b),c(d)] for a,b,d in [('73','4','292'),('82','3','246'),('57','3','171'),('62','1','62'),('60','1','60')]]+[[c('Total','کل','ټول'),c('12'),c('831')]],exampleId='stat11-ex-2-11',role='solution')]
F.rest();F.tb(0)
F.done()
s['sourceNote']='Printed page 64. The weighted-mean value 69.25 is on the next page. Header graphics and watermark excluded.'
s['vocabulary']={'weights':dict(ur='وزن',ps='وزنونه')}
save(s)
# ---------- scan 73 (printed 65) ----------
s=page(73,U,'65','Example 2.11 (end) · 2.3 Median · 2.3.1 Individual series · Example 2.12, 2.13','مثال 2.11 (اختتام) · 2.3 وسطانیہ · 2.3.1 انفرادی سلسلہ · مثالیں 2.12، 2.13','بېلګه 2.11 (پای) · 2.3 میانه · 2.3.1 انفرادي لړۍ · بېلګې 2.12، 2.13','median-1')
F=Flow(s)
F.e('wm',r'\bar{x}_w=\dfrac{\sum_{i=1}^{n}w_ix_i}{\sum_{i=1}^{n}w_i}=\dfrac{831}{12}=69.25\%\ \text{marks}','x̄w = (Σ wi xi)/(Σ wi) = 831/12 = 69.25% marks',exampleId='stat11-ex-2-11')
head(s,'h23','2.3 Median','2.3 وسطانیہ','2.3 میانه')
add(s,'t23','A value which divides the ordered data in to two equal parts is called median. It is a positional average where 50 per cent values lie below the median and 50 per cent lies above the median. Median is used (i) when the exact mid-point of the distribution is desired, (ii) for asymmetric distributions, (iii) when the distribution has extreme values, (iv) when data are measured on an ordinal scale.','وہ قدر جو ترتیب دیے گئے اعداد و شمار کو دو برابر حصوں میں تقسیم کرے وسطانیہ کہلاتی ہے۔ یہ ایک مقامی اوسط ہے جہاں 50 فی صد قدریں وسطانیہ سے نیچے اور 50 فی صد اوپر ہوتی ہیں۔ وسطانیہ استعمال کیا جاتا ہے (i) جب تقسیم کا عین وسطی نقطہ مطلوب ہو، (ii) غیر متناسب تقسیمات کے لیے، (iii) جب تقسیم میں انتہائی قدریں ہوں، (iv) جب اعداد و شمار ترتیبی پیمانے پر ناپے گئے ہوں۔','هغه ارزښت چې ترتیب شوي معلومات په دوو مساوي برخو وېشي میانه بلل کېږي. دا یو موقعیتي اوسط دی چېرته چې 50 سلنه ارزښتونه د میانې لاندې او 50 سلنه یې پورته پراته وي. میانه کارول کېږي (i) کله چې د ویش دقیقه منځنۍ نقطه غوښتل کېږي، (ii) د غیرمتناسبو ویشونو لپاره، (iii) کله چې ویش سخت ارزښتونه ولري، (iv) کله چې معلومات د ترتیبي پیمانې په واسطه اندازه شوي وي.')
head(s,'h231','2.3.1 Computation of median in case of individual series or ungrouped data','2.3.1 انفرادی سلسلے یا غیر گروہی اعداد و شمار کی صورت میں وسطانیہ کا حساب','2.3.1 د انفرادي لړۍ یا نه‌ګروپ شویو معلوماتو په حالت کې د میانې محاسبه')
add(s,'ci','Case-i: When n is odd.','صورت-i: جب n طاق ہو۔','حالت-i: کله چې n طاق وي.')
add(s,'ci2','Arrange the data in ascending or descending order of magnitude, then','اعداد و شمار کو مقدار کے صعودی یا نزولی ترتیب میں ترتیب دیں، پھر','معلومات د کچې په پورته‌والي یا ښکته‌والي ترتیب ترتیب کړئ، بیا')
F.rest()
F.e('c1',r'\text{Median}=\left(\dfrac{n+1}{2}\right)\text{th value}','Median = ((n + 1)/2)th value')
head(s,'ex12','Example: 2.12','مثال: 2.12','بېلګه: 2.12',exampleId='stat11-ex-2-12')
add(s,'q12','The marks obtained by 7 students on an achievement test are; 17, 47, 15, 35, 25, 39, 44. Calculate the median marks.','7 طلبہ کے کارکردگی ٹیسٹ میں حاصل کردہ نمبر یہ ہیں؛ 17, 47, 15, 35, 25, 39, 44۔ وسطانیہ نمبر حساب کریں۔','د 7 زده کوونکو د السته راوړنې په ازموینه کې ترلاسه شوې نمرې دا دي؛ 17, 47, 15, 35, 25, 39, 44. د میانې نمرې محاسبه کړئ.',role='question',exampleId='stat11-ex-2-12')
head(s,'sol12','Solution:','حل:','حل:',exampleId='stat11-ex-2-12')
add(s,'a12','Arranging the data in ascending order x = 15, 17, 25, 35, 39, 44, 47. Here n = 7 is odd so,','اعداد و شمار کو صعودی ترتیب میں ترتیب دینے پر x = 15, 17, 25, 35, 39, 44, 47۔ یہاں n = 7 طاق ہے اس لیے،','معلومات په پورته‌والي ترتیب ترتیبولو سره x = 15, 17, 25, 35, 39, 44, 47. دلته n = 7 طاق دی نو،',role='solution',exampleId='stat11-ex-2-12')
F.rest()
F.e('s12a',r'\text{Median}=\left(\dfrac{n+1}{2}\right)\text{th value}','Median = ((n + 1)/2)th value',exampleId='stat11-ex-2-12')
F.e('s12b',r'=\left(\dfrac{7+1}{2}\right)\text{th value}=4\text{th value}=35','= ((7 + 1)/2)th value = 4th value = 35',exampleId='stat11-ex-2-12')
add(s,'cii','Case-ii: When n is even','صورت-ii: جب n جفت ہو','حالت-ii: کله چې n جفت وي')
add(s,'cii2','Arrange the data in ascending order, then','اعداد و شمار کو صعودی ترتیب میں ترتیب دیں، پھر','معلومات په پورته‌والي ترتیب ترتیب کړئ، بیا')
F.rest()
F.e('c2',r'\text{Median}=\dfrac{1}{2}\left[\left(\dfrac{n}{2}\right)\text{th value}+\left(\dfrac{n}{2}+1\right)\text{th value}\right]','Median = (1/2)[(n/2)th value + (n/2 + 1)th value]')
head(s,'ex13','Example: 2.13','مثال: 2.13','بېلګه: 2.13',exampleId='stat11-ex-2-13')
add(s,'q13','Find the median for the distribution of scores: 8, 12, 10, 14, 11, and 15.','نمبروں کی تقسیم 8, 12, 10, 14, 11 اور 15 کا وسطانیہ معلوم کریں۔','د نمرو د ویش 8, 12, 10, 14, 11 او 15 میانه ومومئ.',role='question',exampleId='stat11-ex-2-13')
F.done()
s['sourceNote']='Printed page 65. The first line completes Example 2.11 from the previous page. Header graphics and watermark excluded.'
s['vocabulary']={'positional':dict(ur='مقامی',ps='موقعیتي')}
save(s)
# ---------- scan 74 (printed 66) ----------
s=page(74,U,'66','Example 2.13 solution · 2.3.2 Discrete series or grouped data · Example 2.14','مثال 2.13 کا حل · 2.3.2 منفصل سلسلہ یا گروہی اعداد و شمار · مثال 2.14','د بېلګې 2.13 حل · 2.3.2 منفصله لړۍ یا ګروپي معلومات · بېلګه 2.14','median-2')
F=Flow(s)
head(s,'sol13','Solution:','حل:','حل:',exampleId='stat11-ex-2-13')
add(s,'a13','x = 8, 10, 11, 12, 14, 15. Here n = 6 is even, therefore','x = 8, 10, 11, 12, 14, 15۔ یہاں n = 6 جفت ہے، لہٰذا','x = 8, 10, 11, 12, 14, 15. دلته n = 6 جفت دی، نو',role='solution',exampleId='stat11-ex-2-13')
F.rest()
F.e('m1',r'\text{Median}=\dfrac{1}{2}\left[\left(\dfrac{6}{2}\right)\text{th value}+\left(\dfrac{6}{2}+1\right)\text{in value}\right]','Median = (1/2)[(6/2)th value + (6/2 + 1)in value]',exampleId='stat11-ex-2-13')
F.e('m2',r'\text{Median}=\dfrac{1}{2}\left[3\text{rd value}+4\text{th value}\right]','Median = (1/2)[3rd value + 4th value]',exampleId='stat11-ex-2-13')
F.e('m3',r'=\dfrac{1}{2}[11+12]=\dfrac{23}{2}=11.5','= (1/2)[11 + 12] = 23/2 = 11.5',exampleId='stat11-ex-2-13')
head(s,'h232','2.3.2 Computation of median in case of discrete series or grouped data','2.3.2 منفصل سلسلے یا گروہی اعداد و شمار کی صورت میں وسطانیہ کا حساب','2.3.2 د منفصلې لړۍ یا ګروپي معلوماتو په حالت کې د میانې محاسبه')
add(s,'si','Step-i: Arrange the data in ascending order along with frequencies.','مرحلہ-i: اعداد و شمار کو تعددات کے ساتھ صعودی ترتیب میں ترتیب دیں۔','ګام-i: معلومات له فریکونسیو سره په پورته‌والي ترتیب ترتیب کړئ.')
add(s,'sii','Step-ii: Compute the cumulative frequencies.','مرحلہ-ii: جمعی تعددات حساب کریں۔','ګام-ii: مجموعي فریکونسۍ محاسبه کړئ.')
add(s,'siii','Step-iii:','مرحلہ-iii:','ګام-iii:')
F.rest()
F.e('st',r'\text{Median}=\left(\dfrac{\sum f}{2}\right)\text{th value if }n=\sum f\text{ is even and}','Median = (Σf/2)th value if n = Σf is even and')
F.e('st2',r'\text{Median}=\left(\dfrac{\sum f+1}{2}\right)\text{th value if }n=\sum f\text{ is odd.}','Median = ((Σf + 1)/2)th value if n = Σf is odd.')
head(s,'ex14','Example: 2.14','مثال: 2.14','بېلګه: 2.14',exampleId='stat11-ex-2-14')
add(s,'q14','During the month of March, a teacher recorded the number of absentees for each student in a class of n = 20 and obtained the following distribution:','مارچ کے مہینے کے دوران ایک استاد نے n = 20 طلبہ کی جماعت میں ہر طالب علم کی غیر حاضریوں کی تعداد ریکارڈ کی اور درج ذیل تقسیم حاصل کی:','د مارچ په میاشت کې یو ښوونکي په n = 20 زده کوونکو ټولګي کې د هر زده کوونکي د غیرحاضرو شمېر ثبت کړ او لاندې ویش یې ترلاسه کړ:',role='question',exampleId='stat11-ex-2-14')
add(s,'q14b','Using the median, what is the average number of absentees for the class?','وسطانیہ استعمال کرتے ہوئے جماعت کی غیر حاضریوں کی اوسط تعداد کیا ہے؟','د میانې په کارولو سره د ټولګي د غیرحاضرو اوسط شمېر څه دی؟',role='question',exampleId='stat11-ex-2-14')
head(s,'sol14','Solution:','حل:','حل:',exampleId='stat11-ex-2-14')
add(s,'a14','Arrange the data along with frequencies as follows;','اعداد و شمار کو تعددات کے ساتھ اس طرح ترتیب دیں؛','معلومات له فریکونسیو سره داسې ترتیب کړئ؛',role='solution',exampleId='stat11-ex-2-14')
s['tables']=[table('Example 2.14: number of absentees','مثال 2.14: غیر حاضریوں کی تعداد','بېلګه 2.14: د غیرحاضرو شمېر',[c('No. of absentees:','غیر حاضریوں کی تعداد:','د غیرحاضرو شمېر:')]+[c(str(v)) for v in [2,0,3,5,1,4]],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in [5,2,7,1,3,2]]],exampleId='stat11-ex-2-14'),
 table('Example 2.14: arranged with cumulative frequency','مثال 2.14: جمعی تعدد کے ساتھ ترتیب','بېلګه 2.14: له مجموعي فریکونسي سره ترتیب',[c('x'),c('f'),c('c.f')],[[c(a),c(b),c(d)] for a,b,d in [('0','2','2'),('1','3','5'),('2','5','10'),('3','7','17'),('4','2','19'),('5','1','20')]]+[[c('Total','کل','ټول'),c('20'),c('−')]],exampleId='stat11-ex-2-14',role='solution')]
F.rest()
ids=[p['id'] for p in s['paras']]
F.done()
# reorder: question text, table0, q14b..., table1, equations after
pre=[pid(74,k) for k in ('sol13','a13')]
s['flow']=[dict(type='paragraphs',ids=[pid(74,'sol13'),pid(74,'a13')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='equation',index=2),
 dict(type='paragraphs',ids=[pid(74,'h232'),pid(74,'si'),pid(74,'sii'),pid(74,'siii')]),dict(type='equation',index=3),dict(type='equation',index=4),
 dict(type='paragraphs',ids=[pid(74,'ex14'),pid(74,'q14')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(74,'q14b'),pid(74,'sol14'),pid(74,'a14')]),dict(type='table',index=1)]
s['equations'].append(eqn(74,'n1',r'\text{Here }n=\sum f=20\text{ is even}','Here n = Σf = 20 is even',exampleId='stat11-ex-2-14'))
s['equations'].append(eqn(74,'n2',r'\therefore\ \text{Median}=\dfrac{\sum f}{2}\text{th value}=\dfrac{20}{2}\text{th value}=10\text{th value}','∴ Median = (Σf/2)th value = (20/2)th value = 10th value',exampleId='stat11-ex-2-14'))
add(s,'z','Look this value in c.f column from the start, which shows that Median = 2','اس قدر کو c.f کالم میں شروع سے دیکھیں، جو ظاہر کرتا ہے کہ وسطانیہ = 2','دا ارزښت د c.f په ستون کې له پیله وګورئ، چې ښيي میانه = 2',role='solution',exampleId='stat11-ex-2-14')
s['flow']+=[dict(type='equation',index=5),dict(type='equation',index=6),dict(type='paragraphs',ids=[pid(74,'z')])]
s['sourceNote']='Printed page 66. The right-hand working of Example 2.14 (Here n = Σf = 20 is even ∴ Median = …) is printed beside the table and is given as equations after it. A thumb is visible at the top-left of the scan; ignored. Printed "in value" in the Example 2.13 working is retained. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
