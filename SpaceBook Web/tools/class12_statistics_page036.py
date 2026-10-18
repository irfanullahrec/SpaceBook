"""PDF36 printed 63–64: Unit 2 key points; Exercise 2.1 (true/false) and 2.2 (fill in the blanks)."""
from class12_statistics_common import Builder, save

k = Builder()
k.h('Key points', 'اہم نکات', 'مهم ټکي')
k.group('list', [
    ('A variable that is itself a function of the results of a random experiment is called random variable', 'وہ متغیر جو خود کسی تصادفی تجربے کے نتائج کا تفاعل ہو، تصادفی متغیر کہلاتا ہے', 'هغه متغیر چې پخپله د یوې تصادفي تجربې د پایلو تابع وي، تصادفي متغیر بلل کېږي'),
    ('A variable which takes jumping values or isolated values is called discrete random variable', 'وہ متغیر جو جست والی یا الگ تھلگ قیمتیں لیتا ہے، منفصل تصادفی متغیر کہلاتا ہے', 'هغه متغیر چې ټوپ وهونکي یا جلا قیمتونه اخلي، منفصل تصادفي متغیر بلل کېږي'),
    ('A variable which takes any value between two limits $[a,b]$, $a<b$ is called continuous random variable', 'وہ متغیر جو دو حدوں $[a,b]$، $a<b$ کے درمیان کوئی بھی قیمت لے، مسلسل تصادفی متغیر کہلاتا ہے', 'هغه متغیر چې د دوو حدونو $[a,b]$، $a<b$ ترمنځ هر قیمت اخلي، متصل تصادفي متغیر بلل کېږي'),
    ('If all possible values of a random variable along with their respective probabilities are shown in tabular form and sum of probabilities is equal to one, then such tabular form is called probability distribution', 'اگر تصادفی متغیر کی تمام ممکنہ قیمتیں متعلقہ احتمالات کے ساتھ جدولی شکل میں دکھائی جائیں اور احتمالات کا مجموعہ ایک ہو تو ایسی جدولی شکل کو احتمالی تقسیم کہتے ہیں', 'که د تصادفي متغیر ټول شوني قیمتونه له اړوندو احتمالونو سره په جدولي بڼه وښودل شي او د احتمالونو مجموعه یو وي، نو داسې جدولي بڼې ته احتمالي وېش وایي'),
    ('If all possible values of a random variable along with their respective probabilities are shown by a formula, then it is called probability function or probability mass function. It is denoted by $p(x_i)$', 'اگر تصادفی متغیر کی تمام ممکنہ قیمتیں متعلقہ احتمالات کے ساتھ فارمولا سے دکھائی جائیں تو اسے احتمالی تفاعل یا احتمالی کمیتی تفاعل کہتے ہیں۔ اسے $p(x_i)$ سے ظاہر کرتے ہیں', 'که د تصادفي متغیر ټول شوني قیمتونه له اړوندو احتمالونو سره د فورمول په واسطه وښودل شي، احتمالي تابع یا د احتمال کتلوي تابع بلل کېږي. په $p(x_i)$ ښودل کېږي'),
    ('The mean of a random variable is called mathematical expectation.', 'تصادفی متغیر کے اوسط کو ریاضیاتی توقع کہتے ہیں۔', 'د تصادفي متغیر منځني ته ریاضي تمه وایي.'),
    ('$E(c)=c$, where c is a constant', '$E(c)=c$، جہاں c ایک مستقل ہے', '$E(c)=c$، چې c یو ثابت دی'),
    ('Mean: $E(X)=\\Sigma x\\,p(x)$ where X is a discrete random variable', 'اوسط: $E(X)=\\Sigma x\\,p(x)$ جہاں X ایک منفصل تصادفی متغیر ہے', 'منځنی: $E(X)=\\Sigma x\\,p(x)$ چې X یو منفصل تصادفي متغیر دی'),
    ('Variance: $V(X)=E[X^2]-[E(X)]^2$', 'تغیر: $V(X)=E[X^2]-[E(X)]^2$', 'واریانس: $V(X)=E[X^2]-[E(X)]^2$'),
    ('The distribution of two or more random variables is called joint distribution.', 'دو یا زیادہ تصادفی متغیرات کی تقسیم کو مشترکہ تقسیم کہتے ہیں۔', 'د دوو یا ډېرو تصادفي متغیرونو وېش ته ګډ وېش وایي.'),
    ('If $f(x_i,y_j)=f(x_i)\\,f(y_j)$, then X and Y are independent', 'اگر $f(x_i,y_j)=f(x_i)\\,f(y_j)$ ہو تو X اور Y آزاد ہیں', 'که $f(x_i,y_j)=f(x_i)\\,f(y_j)$ وي، نو X او Y خپلواک دي'),
    ('$E(X+Y)=E(X)+E(Y)$ and $E(X-Y)=E(X)-E(Y)$', '$E(X+Y)=E(X)+E(Y)$ اور $E(X-Y)=E(X)-E(Y)$', '$E(X+Y)=E(X)+E(Y)$ او $E(X-Y)=E(X)-E(Y)$'),
    ('$E(XY)=E(X)\\,E(Y)$, if X and Y are independent.', '$E(XY)=E(X)\\,E(Y)$، اگر X اور Y آزاد ہوں۔', '$E(XY)=E(X)\\,E(Y)$، که X او Y خپلواک وي.'),
    ('$V(X+Y)=V(X)+V(Y)$ and $V(X-Y)=V(X)+V(Y)$, if X and Y are independent.', '$V(X+Y)=V(X)+V(Y)$ اور $V(X-Y)=V(X)+V(Y)$، اگر X اور Y آزاد ہوں۔', '$V(X+Y)=V(X)+V(Y)$ او $V(X-Y)=V(X)+V(Y)$، که X او Y خپلواک وي.'),
])
keys = k.build('stat12-u2-key-points', 'Unit 2 — Key points', 'یونٹ 2 — اہم نکات', 'واحد 2 — مهم ټکي', 36, [63])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.h('2.1 Read the following statements carefully and write T for true and F for false statement.', '2.1 درج ذیل بیانات غور سے پڑھیں اور درست کے لیے T اور غلط کے لیے F لکھیں۔', '2.1 لاندې بیانونه په غور ولولئ او د سم لپاره T او د ناسم لپاره F ولیکئ.')
e.group('lines', [
    ('i. Random variable is also called chance variable.', 'i. تصادفی متغیر کو اتفاقی متغیر بھی کہتے ہیں۔', 'i. تصادفي متغیر ته د چانس متغیر هم وایي.'),
    ('ii. Discrete random variable takes every value between two limits', 'ii. منفصل تصادفی متغیر دو حدوں کے درمیان ہر قیمت لیتا ہے', 'ii. منفصل تصادفي متغیر د دوو حدونو ترمنځ هر قیمت اخلي'),
    ('iii. The sum of probabilities in a probability distribution must be one.', 'iii. احتمالی تقسیم میں احتمالات کا مجموعہ لازماً ایک ہونا چاہیے۔', 'iii. په احتمالي وېش کې د احتمالونو مجموعه باید یو وي.'),
    ('iv. The probability function and pdf can be negative.', 'iv. احتمالی تفاعل اور pdf منفی ہو سکتے ہیں۔', 'iv. احتمالي تابع او pdf منفي کېدای شي.'),
    ('v. Mathematical expectation of a random variable is also called average or mean of the random variable.', 'v. تصادفی متغیر کی ریاضیاتی توقع کو تصادفی متغیر کا اوسط بھی کہتے ہیں۔', 'v. د تصادفي متغیر ریاضي تمې ته د تصادفي متغیر اوسط یا منځنی هم وایي.'),
    ('vi. Expected value of a constant is zero.', 'vi. کسی مستقل کی متوقع قیمت صفر ہوتی ہے۔', 'vi. د یوه ثابت تمه شوی قیمت صفر دی.'),
    ('vii. Variance of a constant is zero.', 'vii. کسی مستقل کا تغیر صفر ہوتا ہے۔', 'vii. د یوه ثابت واریانس صفر دی.'),
    ('viii. $E(X-Y)=E(X)-E(Y)$',) * 3,
    ('ix. $V(X-Y)=V(X)-V(Y)$',) * 3,
    ('x. If $f(x,y)=f(x)\\,f(y)$, it means X and Y are independent.', 'x. اگر $f(x,y)=f(x)\\,f(y)$ ہو تو اس کا مطلب ہے کہ X اور Y آزاد ہیں۔', 'x. که $f(x,y)=f(x)\\,f(y)$ وي، مانا یې دا ده چې X او Y خپلواک دي.'),
])
e.h('2.2 Fill in the blanks.', '2.2 خالی جگہیں پُر کریں۔', '2.2 تش ځایونه ډک کړئ.')
B = '______'
e.group('lines', [
    ('i. A discrete variable can take a ' + B + ' number of values within its range or an infinite number of values that are countable.', 'i. ایک منفصل متغیر اپنی حد میں ' + B + ' تعداد میں قیمتیں یا لامحدود قابلِ شمار قیمتیں لے سکتا ہے۔', 'i. یو منفصل متغیر په خپل حد کې ' + B + ' شمېر قیمتونه یا بې‌شمېره د شمېرلو وړ قیمتونه اخیستلای شي.'),
    ('ii. The probability function p(x) cannot exceed ' + B, 'ii. احتمالی تفاعل p(x) ' + B + ' سے زیادہ نہیں ہو سکتا', 'ii. احتمالي تابع p(x) له ' + B + ' څخه نه شي زیاتېدای'),
    ('iii. if $p(x)=\\frac{x}{21}$ for x = 1, 2, 3, 4, 5, 6 then $P(X=2\\text{ or }3)=$ ' + B, 'iii. اگر x = 1، 2، 3، 4، 5، 6 کے لیے $p(x)=\\frac{x}{21}$ ہو تو $P(X=2\\text{ or }3)=$ ' + B, 'iii. که د x = 1، 2، 3، 4، 5، 6 لپاره $p(x)=\\frac{x}{21}$ وي، نو $P(X=2\\text{ or }3)=$ ' + B),
    ('iv. A variable whose value are obtained from the outcomes of a random experiment is called ' + B, 'iv. وہ متغیر جس کی قیمتیں تصادفی تجربے کے نتائج سے حاصل ہوں، ' + B + ' کہلاتا ہے', 'iv. هغه متغیر چې قیمتونه یې د تصادفي تجربې له پایلو لاسته راځي، ' + B + ' بلل کېږي'),
    ('v. Random variables are classified into ' + B, 'v. تصادفی متغیرات کی درجہ بندی ' + B + ' میں کی جاتی ہے', 'v. تصادفي متغیرونه په ' + B + ' ډلبندي کېږي'),
    ('vi. The distribution of two or more random variables is called ' + B, 'vi. دو یا زیادہ تصادفی متغیرات کی تقسیم کو ' + B + ' کہتے ہیں', 'vi. د دوو یا ډېرو تصادفي متغیرونو وېش ته ' + B + ' وایي'),
    ('vii. The value of the expression $\\sum_i\\sum_j p(x_i,y_j)$ is always ' + B, 'vii. اظہاریہ $\\sum_i\\sum_j p(x_i,y_j)$ کی قیمت ہمیشہ ' + B + ' ہوتی ہے', 'vii. د $\\sum_i\\sum_j p(x_i,y_j)$ افادې قیمت تل ' + B + ' وي'),
    ('viii. If X and Y are two independent variables then $E(XY)=$ ' + B, 'viii. اگر X اور Y دو آزاد متغیرات ہوں تو $E(XY)=$ ' + B, 'viii. که X او Y دوه خپلواک متغیرونه وي، نو $E(XY)=$ ' + B),
    ('ix. If X and Y are independent random variables then $S.D(X-Y)=$ ' + B, 'ix. اگر X اور Y آزاد تصادفی متغیرات ہوں تو $S.D(X-Y)=$ ' + B, 'ix. که X او Y خپلواک تصادفي متغیرونه وي، نو $S.D(X-Y)=$ ' + B),
    ('x. If $E(X)=\\frac{2}{3}$, $E(X^2)=\\frac{8}{9}$ then $S.D(X)=$ ' + B, 'x. اگر $E(X)=\\frac{2}{3}$، $E(X^2)=\\frac{8}{9}$ ہو تو $S.D(X)=$ ' + B, 'x. که $E(X)=\\frac{2}{3}$، $E(X^2)=\\frac{8}{9}$ وي، نو $S.D(X)=$ ' + B),
])
ex = e.build('stat12-u2-exercise-a', 'Unit 2 Exercise — 2.1 and 2.2', 'یونٹ 2 مشق — 2.1 اور 2.2', 'واحد 2 تمرین — 2.1 او 2.2', 36, [64])

if __name__ == '__main__':
    save(36, [(2, keys), (2, ex)])
