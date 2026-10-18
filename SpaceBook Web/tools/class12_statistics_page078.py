"""PDF78 printed 147–148: Exercise 4.3 MCQs (viii)–(x); questions 4.4–4.17 (start)."""
from class12_statistics_common import Builder, save

b = Builder()
b.mcq('viii.', ('The area under the normal curve within two standard deviation of the mean is', 'اوسط سے دو معیاری انحراف کے اندر نارمل منحنی کے نیچے رقبہ ہے', 'د منځني څخه د دوو معیاري انحرافونو دننه د نورمال منحني لاندې مساحت دی'), ['68.3%', '95.4%', '99.7%', '99.99%'])
b.mcq('ix.', ('For a Normal distribution μ = 40, σ = 8. The value of Z for X = 52 is', 'نارمل تقسیم کے لیے μ = 40، σ = 8۔ X = 52 کے لیے Z کی قیمت ہے', 'د نورمال وېش لپاره μ = 40، σ = 8. د X = 52 لپاره د Z قیمت دی'), ['2.00', '−1.75', '0.80', '1.50'], per_line=4)
b.mcq('x.', ('An approximate relation between M.D about mean and S.D of Normal distribution is', 'نارمل تقسیم کے اوسط کے گرد اوسط انحراف اور معیاری انحراف کے درمیان تقریبی تعلق ہے', 'د نورمال وېش د منځني شاوخوا منځني انحراف او معیاري انحراف ترمنځ نږدې اړیکه ده'),
      ['5M.D = 4S.D', '4M.D = 5S.D', '3M.D = 3S.D', '3M.D = 2S.D'])
Q = lambda n, e, u, p: b.p(f'{n} {e}', f'{n} {u}', f'{n} {p}')
Q('4.4', '(a) Define continuous uniform probability distribution. (b) Find mean and variance of the continuous uniform distribution.', '(a) مسلسل یکساں احتمالی تقسیم کی تعریف کریں۔ (b) مسلسل یکساں تقسیم کا اوسط اور تغیر معلوم کریں۔', '(a) متصل یونیفارم احتمالي وېش تعریف کړئ. (b) د متصل یونیفارم وېش منځنی او واریانس پیدا کړئ.')
Q('4.5', 'Describe Normal distribution and throw light on the importance of Normal distribution.', 'نارمل تقسیم بیان کریں اور نارمل تقسیم کی اہمیت پر روشنی ڈالیں۔', 'نورمال وېش بیان کړئ او د نورمال وېش په اهمیت رڼا واچوئ.')
Q('4.6', 'Define Normal distribution. Write down its properties.', 'نارمل تقسیم کی تعریف کریں۔ اس کی خصوصیات لکھیں۔', 'نورمال وېش تعریف کړئ. ځانګړنې یې ولیکئ.')
Q('4.7', 'Define standard normal variable and standard Normal distribution. What is the role of this distribution?', 'معیاری نارمل متغیر اور معیاری نارمل تقسیم کی تعریف کریں۔ اس تقسیم کا کردار کیا ہے؟', 'معیاري نورمال متغیر او معیاري نورمال وېش تعریف کړئ. د دې وېش رول څه دی؟')
Q('4.8', 'If Z is a standard normal variable, calculate:', 'اگر Z ایک معیاری نارمل متغیر ہو تو معلوم کریں:', 'که Z یو معیاري نورمال متغیر وي، محاسبه کړئ:')
b.mlines([r'(i)\ P[Z>1.60]\qquad(v)\ P[-1.96<Z<1.96]', r'(ii)\ P[1.60<Z<2.30]\qquad(vi)\ P[-1.50<Z<0.67]', r'(iii)\ P[-1.64<Z<-1.02]\qquad(vii)\ P[Z<-2.50]', r'(iv)\ P[0<Z<1.96]'])
Q('4.9', 'Find the proportion of a Normal distribution that corresponds to each of the following sections:', 'نارمل تقسیم کا وہ تناسب معلوم کریں جو درج ذیل حصوں میں سے ہر ایک کے مطابق ہو:', 'د نورمال وېش هغه برخه پیدا کړئ چې د لاندې هرې برخې سره سمون لري:')
b.eq(r'(i)\ Z<0.25\quad(ii)\ Z>0.80\quad(iii)\ Z<-1.50\quad(iv)\ Z>-0.75')
Q('4.10', 'Let Z ~ N (0, 1). Find the area under the normal curve in the following cases:', 'فرض کریں Z ~ N (0, 1)۔ درج ذیل صورتوں میں نارمل منحنی کے نیچے رقبہ معلوم کریں:', 'فرض کړئ Z ~ N (0, 1). په لاندې حالتونو کې د نورمال منحني لاندې مساحت پیدا کړئ:')
b.group('lines', [
    ('(i) to the right of 2.63  (ii) to the left of −1.45', '(i) 2.63 کے دائیں  (ii) −1.45 کے بائیں', '(i) د 2.63 ښي خوا ته  (ii) د −1.45 کیڼ خوا ته'),
    ('(iii) between 2.27 and 3.02  (iv) between −1.96 and −1.06', '(iii) 2.27 اور 3.02 کے درمیان  (iv) −1.96 اور −1.06 کے درمیان', '(iii) د 2.27 او 3.02 ترمنځ  (iv) د −1.96 او −1.06 ترمنځ'),
    ('(v) between −2.65 and 2.09  (vi) below 2.17', '(v) −2.65 اور 2.09 کے درمیان  (vi) 2.17 سے نیچے', '(v) د −2.65 او 2.09 ترمنځ  (vi) له 2.17 لاندې'),
])
Q('4.11', 'Determine the Z-value in the following statements:', 'درج ذیل بیانات میں Z کی قیمت معلوم کریں:', 'په لاندې بیانونو کې د Z قیمت وټاکئ:')
b.eq(r'(i)\ P[Z>z]=0.005\quad(ii)\ P[Z>z]=0.1075\quad(iii)\ P[Z>z]=0.9599')
Q('4.12', 'For a Normal distribution, find the Z-score location that divides the distribution as follows:', 'نارمل تقسیم کے لیے وہ Z اسکور مقام معلوم کریں جو تقسیم کو یوں تقسیم کرے:', 'د نورمال وېش لپاره د Z نمرې هغه ځای پیدا کړئ چې وېش داسې ووېشي:')
b.group('lines', [
    ('(i) separate the top 20% from the rest.', '(i) اوپر کے 20% کو باقی سے الگ کرے۔', '(i) پورتنۍ 20% له پاتې برخې جلا کړي.'),
    ('(ii) separate the top 60% from the rest.', '(ii) اوپر کے 60% کو باقی سے الگ کرے۔', '(ii) پورتنۍ 60% له پاتې برخې جلا کړي.'),
    ('(iii) separate the middle 70% from the rest.', '(iii) درمیانی 70% کو باقی سے الگ کرے۔', '(iii) منځنۍ 70% له پاتې برخې جلا کړي.'),
])
Q('4.13', 'Suppose the distribution of X is normal having mean 46 and standard deviation 4. Compute the following probabilities:', 'فرض کریں X کی تقسیم نارمل ہے جس کا اوسط 46 اور معیاری انحراف 4 ہے۔ درج ذیل احتمالات معلوم کریں:', 'فرض کړئ د X وېش نورمال دی چې منځنی یې 46 او معیاري انحراف یې 4 دی. لاندې احتمالونه محاسبه کړئ:')
b.eq(r'(i)\ P[X>50]\quad(ii)\ P[X<38]\quad(iii)\ P[45\le X\le 49]')
Q('4.14', 'A Normal distribution has mean = 100 and variance = 225. Find the following probabilities:', 'ایک نارمل تقسیم کا اوسط = 100 اور تغیر = 225 ہے۔ درج ذیل احتمالات معلوم کریں:', 'یو نورمال وېش منځنی = 100 او واریانس = 225 لري. لاندې احتمالونه پیدا کړئ:')
b.mlines([r'(i)\ P[X\ge 76]\quad(ii)\ P[X\ge 124]\quad(ii)\ P[X\le 92.5]', r'(iv)\ P[X\le 107.5]\quad(v)\ P[91\le X\le 127]\quad(vi)\ P[112\le X\le 128.5]'])
Q('4.15', 'The average seasonal rainfall in certain country is 16 inches with a standard deviation of 4 inches. What is the probability that in a year the rainfall in the country will be between 20 inches and 24 inches?', 'کسی ملک میں اوسط موسمی بارش 16 انچ اور معیاری انحراف 4 انچ ہے۔ کسی سال ملک میں بارش کے 20 انچ اور 24 انچ کے درمیان ہونے کا احتمال کیا ہے؟', 'په یوه ټاکلي هېواد کې منځنی موسمي باران 16 انچه او معیاري انحراف یې 4 انچه دی. احتمال یې څومره دی چې په یوه کال کې د هېواد باران د 20 او 24 انچو ترمنځ وي؟')
Q('4.16', 'In a certain book, the frequency distribution of the number of words per page may be taken as approximately normally with mean 400 and SD 25. If a page is chosen at random, what is the probability that the number of words lies between 415 and 450?', 'ایک کتاب میں فی صفحہ الفاظ کی تعداد کی تعددی تقسیم کو تقریباً نارمل سمجھا جا سکتا ہے جس کا اوسط 400 اور معیاری انحراف 25 ہے۔ اگر ایک صفحہ تصادفی طور پر چنا جائے تو الفاظ کی تعداد کے 415 اور 450 کے درمیان ہونے کا احتمال کیا ہے؟', 'په یوه کتاب کې په هر مخ کې د کلمو د شمېر فریکونسي وېش نږدې نورمال ګڼل کېدای شي چې منځنی یې 400 او معیاري انحراف یې 25 دی. که یو مخ په تصادفي ډول وټاکل شي، احتمال یې څومره دی چې د کلمو شمېر د 415 او 450 ترمنځ وي؟')
Q('4.17', 'The heights of a certain population of corn plants follow a Normal distribution with mean 145cm and standard deviation 22cm. What percentage of the plant heights are', 'مکئی کے پودوں کی ایک آبادی کی اونچائیاں نارمل تقسیم کی پیروی کرتی ہیں جن کا اوسط 145cm اور معیاری انحراف 22cm ہے۔ پودوں کی اونچائیوں کا کتنا فیصد ہے', 'د جوارو د بوټو د یوه ټاکلي نفوس لوړوالی نورمال وېش تعقیبوي چې منځنی یې 145cm او معیاري انحراف یې 22cm دی. د بوټو د لوړوالي څو سلنه دي')
rec = b.build('stat12-u4-exercise-b', 'Unit 4 Exercise — 4.3 (viii)–(x) and questions 4.4 to 4.17', 'یونٹ 4 مشق — 4.3 (viii)–(x) اور سوالات 4.4 تا 4.17', 'واحد 4 تمرین — 4.3 (viii)–(x) او پوښتنې 4.4 تر 4.17', 78, [147, 148])
issues = [{'id': 'stat12-p148-q414-label', 'unit': 4, 'printedPage': 148, 'description': 'Question 4.14 labels its third part “(ii)” a second time (should be (iii)); printed label retained.'}]

if __name__ == '__main__':
    save(78, [(4, rec)], issues=issues)
