"""PDF38 printed 67–68: Unit 2 exercise questions 2.7–2.20."""
from class12_statistics_common import Builder, save

b = Builder()
Q = lambda n, e, u, p: b.p(f'{n} {e}', f'{n} {u}', f'{n} {p}')
Q('2.7', 'Define probability distribution, probability function and probability density function. What are the two basic properties of all probability functions?', 'احتمالی تقسیم، احتمالی تفاعل اور احتمالی کثافتی تفاعل کی تعریف کریں۔ تمام احتمالی تفاعلات کی دو بنیادی خصوصیات کیا ہیں؟', 'احتمالي وېش، احتمالي تابع او د احتمال کثافت تابع تعریف کړئ. د ټولو احتمالي تابع ګانو دوه بنسټیزې ځانګړنې کومې دي؟')
Q('2.8', 'Find probability distribution for the number of heads when 2 balanced coins are tossed.', 'جب 2 متوازن سکے اچھالے جائیں تو چِت کی تعداد کی احتمالی تقسیم معلوم کریں۔', 'کله چې 2 متوازنې سکې واچول شي، د سرونو د شمېر احتمالي وېش پیدا کړئ.')
Q('2.9', 'In a family of three children find the probability distribution for the number of girls.', 'تین بچوں والے خاندان میں لڑکیوں کی تعداد کی احتمالی تقسیم معلوم کریں۔', 'په درې ماشومه کورنۍ کې د نجونو د شمېر احتمالي وېش پیدا کړئ.')
Q('2.10', 'A random variable has the following probability distribution.', 'ایک تصادفی متغیر کی احتمالی تقسیم یہ ہے۔', 'یو تصادفي متغیر لاندې احتمالي وېش لري.')
b.dist('stat12-t-q2-10', ['4', '6', '7', '10'], ['0.2', '0.4', 'c', '0.1'], total=None)
b.p('(i) Find the value of c. (ii) $P(X<7)$ (iii) $P(X\\ge 6)$', '(i) c کی قیمت معلوم کریں۔ (ii) $P(X<7)$ (iii) $P(X\\ge 6)$', '(i) د c قیمت پیدا کړئ. (ii) $P(X<7)$ (iii) $P(X\\ge 6)$')
Q('2.11', 'A coin is tossed three times in succession. Find the probability distribution for the number of heads minus number of tails.', 'ایک سکہ یکے بعد دیگرے تین بار اچھالا جاتا ہے۔ چِت کی تعداد تفریق پَٹ کی تعداد کی احتمالی تقسیم معلوم کریں۔', 'یوه سکه په پرله پسې ډول درې ځله اچول کېږي. د سرونو شمېر منفي د لکیو شمېر احتمالي وېش پیدا کړئ.')
Q('2.12', 'A pair of fair dice is rolled once. Find the probability distribution for the difference of dots.', 'منصفانہ پانسوں کا ایک جوڑا ایک بار پھینکا جاتا ہے۔ نقطوں کے فرق کی احتمالی تقسیم معلوم کریں۔', 'د عادلانه ډایسونو یوه جوړه یو ځل اچول کېږي. د ټکو د توپیر احتمالي وېش پیدا کړئ.')
Q('2.13', 'Check whether the following is a probability distribution or not? If not, then why?', 'جانچیں کہ درج ذیل احتمالی تقسیم ہے یا نہیں؟ اگر نہیں تو کیوں؟', 'وګورئ چې لاندې احتمالي وېش دی که نه؟ که نه وي، نو ولې؟')
b.dist('stat12-t-q2-13', ['0', '10', '15', '25', '50'], ['0.1', '0.3', '0.4', '0.3', '0.1'], total=None)
Q('2.14', 'A discrete random variable has the probability mass function:', 'ایک منفصل تصادفی متغیر کا احتمالی کمیتی تفاعل یہ ہے:', 'یو منفصل تصادفي متغیر دا د احتمال کتلوي تابع لري:')
b.eq(r'p(x)=\left\{\begin{matrix}\frac{{}^{3}_{x}C}{8}, & x=0,1,2,3\\ 0, & \textit{elsewhere}\end{matrix}\right.')
b.p('Find (i) $P(X=2)$ (ii) $P(X>1)$ (iii) $P(0<X<3)$', 'معلوم کریں (i) $P(X=2)$ (ii) $P(X>1)$ (iii) $P(0<X<3)$', 'پیدا کړئ (i) $P(X=2)$ (ii) $P(X>1)$ (iii) $P(0<X<3)$')
Q('2.15', '(a) Define p.d.f and state its properties. (b) The density function of a continuous random variable X is:', '(a) p.d.f کی تعریف کریں اور اس کی خصوصیات بیان کریں۔ (b) ایک مسلسل تصادفی متغیر X کا کثافتی تفاعل یہ ہے:', '(a) p.d.f تعریف کړئ او ځانګړنې یې بیان کړئ. (b) د یوه متصل تصادفي متغیر X کثافت تابع دا ده:')
b.eq(r'f(x)=\begin{bmatrix}Ax^2, & 0\le x\le 1\\ 0, & \textit{elsewhere}\end{bmatrix}')
b.p('Find (i) value of the constant A (ii) $P(X\\le 0.5)$ (ii) $P(0.2<X<0.3)$.', 'معلوم کریں (i) مستقل A کی قیمت (ii) $P(X\\le 0.5)$ (ii) $P(0.2<X<0.3)$۔', 'پیدا کړئ (i) د ثابت A قیمت (ii) $P(X\\le 0.5)$ (ii) $P(0.2<X<0.3)$.')
Q('2.16', 'Discuss mathematical expectation. Write some of its important properties.', 'ریاضیاتی توقع پر بحث کریں۔ اس کی چند اہم خصوصیات لکھیں۔', 'په ریاضي تمه بحث وکړئ. ځینې مهمې ځانګړنې یې ولیکئ.')
Q('2.17', 'For the following discrete probability distribution of X', 'X کی درج ذیل منفصل احتمالی تقسیم کے لیے', 'د X د لاندې منفصل احتمالي وېش لپاره')
b.dist('stat12-t-q2-17', ['−2', '1', '2'], ['1/3', '1/6', '1/2'], total=None)
b.p('Find (i) E(X) (ii) E(X²) (iii) E(2X+5)', 'معلوم کریں (i) E(X) (ii) E(X²) (iii) E(2X+5)', 'پیدا کړئ (i) E(X) (ii) E(X²) (iii) E(2X+5)')
Q('2.18', 'Find the mean, variance and standard deviation for the following probability distribution:', 'درج ذیل احتمالی تقسیم کا اوسط، تغیر اور معیاری انحراف معلوم کریں:', 'د لاندې احتمالي وېش منځنی، واریانس او معیاري انحراف پیدا کړئ:')
b.dist('stat12-t-q2-18', ['−1', '0', '1', '2', '3'], ['0.125', '0.5', '0.2', '0.05', '0.125'], xlabel='$Y$', plabel='$p(y)$', total=None)
Q('2.19', 'Let Y be a random variable with probability distribution as follows:', 'فرض کریں Y ایک تصادفی متغیر ہے جس کی احتمالی تقسیم یہ ہے:', 'فرض کړئ Y یو تصادفي متغیر دی چې احتمالي وېش یې دا دی:')
b.dist('stat12-t-q2-19', ['1', '2', '3', '4', '5'], ['0.125', '0.45', '0.25', '0.05', '0.125'], xlabel='$Y$', plabel='$p(y)$', total=None)
b.group('lines', [
    ('Find (i) Expected value', 'معلوم کریں (i) متوقع قیمت', 'پیدا کړئ (i) تمه شوی قیمت'),
    ('(ii) Variance', '(ii) تغیر', '(ii) واریانس'),
    ('(iii) S.D for the random variable Y', '(iii) تصادفی متغیر Y کا معیاری انحراف', '(iii) د تصادفي متغیر Y معیاري انحراف'),
])
Q('2.20', 'A variable X has the p.d.f $f(x)=\\begin{bmatrix}kx^3(1-x), & 0\\le x\\le 1\\\\ 0, & \\textit{otherwise}\\end{bmatrix}$', 'ایک متغیر X کا p.d.f یہ ہے $f(x)=\\begin{bmatrix}kx^3(1-x), & 0\\le x\\le 1\\\\ 0, & \\textit{otherwise}\\end{bmatrix}$', 'یو متغیر X دا p.d.f لري $f(x)=\\begin{bmatrix}kx^3(1-x), & 0\\le x\\le 1\\\\ 0, & \\textit{otherwise}\\end{bmatrix}$')
b.p('Find (i) The value of k (ii) E(X) (iii) Variance (iv) S.D', 'معلوم کریں (i) k کی قیمت (ii) E(X) (iii) تغیر (iv) معیاری انحراف', 'پیدا کړئ (i) د k قیمت (ii) E(X) (iii) واریانس (iv) معیاري انحراف')
rec = b.build('stat12-u2-exercise-c', 'Unit 2 Exercise — questions 2.7 to 2.20', 'یونٹ 2 مشق — سوالات 2.7 تا 2.20', 'واحد 2 تمرین — پوښتنې 2.7 تر 2.20', 38, [67, 68])
issues = [{'id': 'stat12-p68-q215-label', 'unit': 2, 'printedPage': 68, 'description': 'Question 2.15(b) labels its third part “(ii)” a second time (should be (iii)); printed labels retained.'},
          {'id': 'stat12-p67-q213-sum', 'unit': 2, 'printedPage': 67, 'description': 'Question 2.13 probabilities as printed sum to 1.2 — this is intentional for the “is it a distribution?” check; values kept as printed.'}]

if __name__ == '__main__':
    save(38, [(2, rec)], issues=issues)
