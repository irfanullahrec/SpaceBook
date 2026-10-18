from math11_answer_authoring import Author,step,S
from itertools import product,combinations,permutations
from math import factorial
R=S.Rational
A=Author(6)
def result(tex):return step('Substitute the given values and simplify.','دی گئی قیمتیں رکھ کر مختصر کریں۔','ورکړل شوي ارزښتونه کېږدئ او ساده یې کړئ.',tex)
addition=step('Use the addition law and count the intersection only once.','جمعی قانون استعمال کریں اور مشترک حصہ صرف ایک مرتبہ شمار کریں۔','د جمع قانون وکاروئ او ګډه برخه یوازې یو ځل وشمېرئ.',r'P(A\cup B)=P(A)+P(B)-P(A\cap B)')
complement=step('Subtract the probability of the complementary event from one.','متمم واقعے کا احتمال ایک سے تفریق کریں۔','د متممې پېښې احتمال له یوه منفي کړئ.',r'P(E^c)=1-P(E)')
def put(q,p,answer,steps,**kw):A.put('6.5',str(q),p,answer,steps,**kw)
assert R(2,5)+R(2,5)-R(1,2)==R(3,10)
put(1,'',r'$\frac3{10}$',[addition,result(r'P(A\cap B)=\frac25+\frac25-\frac12=\frac3{10}')])
assert R(1,2)+R(3,8)-R(3,4)==R(1,8)
put(2,'(i)',r'$\frac18$',[complement,result(r'P(B)=1-\frac58=\frac38'),addition,result(r'P(A\cap B)=\frac12+\frac38-\frac34=\frac18')])
put(2,'(ii)',r'$\frac14$',[step('Neither A nor B is the complement of their union.','نہ A نہ B کا واقعہ ان کے اجتماع کا متمم ہے۔','نه A او نه B د دوی د اتحاد متممه پېښه ده.',r'\overline A\cap\overline B=\overline{A\cup B}'),complement,result(r'P(\overline A\cap\overline B)=1-\frac34=\frac14')])
put(3,'',r'$0.1$',[addition,result(r'P(A\cap B)=0,\quad P(B)=0.6-0.5=0.1')])
event=[n for n in range(1,31) if n%2 or n in [1,4,9,16,25]];assert len(event)==17
put(4,'',r'$\frac{17}{30}$',[addition,step('There are 15 odd numbers, 5 squares, and 3 odd squares. The square 0 is outside the numbered tickets.','15 طاق اعداد، 5 مربع اور 3 طاق مربع ہیں۔ مربع 0 ٹکٹوں کی حد سے باہر ہے۔','15 طاق عددونه، 5 مربعونه او 3 طاق مربعونه شته. د 0 مربع د ټکټونو له حد څخه بهر دی.',r'P(E)=\frac{15+5-3}{30}=\frac{17}{30}')])
put(5,'',r'$\frac19$',[complement,result(r'1-\frac89=\frac19')])
put(6,'',r'$\frac13$',[step('With fair independent dice and the first result fixed at 4, the second die still has six equally likely outcomes. Two exceed 4.','غیر جانب دار آزاد پانسوں میں پہلے کا نتیجہ 4 مقرر ہونے پر بھی دوسرے کے چھ نتائج یکساں ممکن ہیں۔ دو نتائج 4 سے بڑے ہیں۔','په عادلانه خپلواکو ځارونو کې د لومړي 4 نتیجه ثابتولو سره هم دویم ځار شپږ مساوي احتمال لرونکې پایلې لري. دوه پایلې له 4 لویې دي.',r'P(\{5,6\})=\frac26=\frac13')])
put(7,'',r'$\frac6{13}$',[step('Neither red nor king means a black card that is not a king. Exclude the two black kings from the 26 black cards.','نہ سرخ نہ بادشاہ کا مطلب ایسا سیاہ پتہ ہے جو بادشاہ نہ ہو۔ 26 سیاہ پتوں سے دو سیاہ بادشاہ نکالیں۔','نه سور او نه پاچا، یعنې تور کارت چې پاچا نه وي. له 26 تورو کارتونو څخه دوه تور پاچاهان لرې کړئ.',r'P(E)=\frac{26-2}{52}=\frac6{13}')])
count=sum(a+b not in [7,11] for a,b in product(range(1,7),repeat=2));assert count==28
put(8,'',r'$\frac79$',[complement,result(r'P(E)=1-\frac{6+2}{36}=\frac{28}{36}=\frac79')])
warning=step('Independence is not stated in the question, so the marginal probabilities alone do not determine a unique answer. Let t=P(A∩B), where 0≤t≤1/7. Under the usual extra assumption of independent selections, t=(1/7)(1/5)=1/35.','سوال میں آزادی بیان نہیں ہوئی، اس لیے صرف انفرادی احتمالات سے منفرد جواب نہیں نکلتا۔ t=P(A∩B) لیں، جہاں 0≤t≤1/7۔ انتخاب آزاد ہونے کے اضافی معمول کے فرض پر t=(1/7)(1/5)=1/35۔','په پوښتنه کې خپلواکي نه ده ویل شوې، نو یوازې انفرادي احتمالونه یوازینی ځواب نه ټاکي. t=P(A∩B) ونیسئ چې 0≤t≤1/7. د خپلواکو انتخابونو په اضافي معمولي فرض کې t=(1/7)(1/5)=1/35.',r'0\le t\le\frac17,\quad t_{\rm independent}=\frac1{35}')
t=S.symbols('t')
for part,expr,expected in [('(i)',t,R(1,35)),('(ii)',R(12,35)-2*t,R(2,7)),('(iii)',R(23,35)+t,R(24,35)),('(iv)',R(12,35)-t,R(11,35))]:
    assert expr.subs(t,R(1,35))==expected
    general=S.latex(expr);val=S.latex(expected)
    put(9,part,'$'+general+'$; if selections are independent: $'+val+'$.',[warning,addition,result('P(E)='+general+r',\quad t=\frac1{35}\Rightarrow P(E)='+val)],answerUr='$'+general+'$؛ اگر انتخاب آزاد ہوں: $'+val+'$۔',answerPs='$'+general+'$؛ که انتخابونه خپلواک وي: $'+val+'$.')
fruit=[('apple',i>=5) for i in range(20)]+[('orange',i>=3) for i in range(10)]
allpairs=list(combinations(fruit,2));good=sum((a[0]==b[0]=='apple')or(a[1] and b[1]) for a,b in allpairs);assert len(allpairs)==435 and good==316
put(10,'',r'$\frac{316}{435}$',[step('Draw two distinct fruits without replacement. Let A mean both apples and G mean both good. There are 22 good fruits, including 15 good apples.','دو مختلف پھل واپس رکھے بغیر نکالیں۔ A دونوں سیب اور G دونوں اچھے ہونے کا واقعہ ہو۔ 22 اچھے پھل ہیں، جن میں 15 اچھے سیب ہیں۔','دوه بېلې مېوې له بېرته ایښودلو پرته وباسئ. A دواړه مڼې او G دواړه ښې مېوې ونیسئ. 22 ښې مېوې دي چې 15 یې ښې مڼې دي.'),addition,result(r'P(A\cup G)=\frac{\binom{20}2+\binom{22}2-\binom{15}2}{\binom{30}2}=\frac{190+231-105}{435}=\frac{316}{435}')])
A.save(['6.5'],[203,204])

A=Author(6)
def review(q,p,answer,steps,**kw):A.put('Review 6',str(q),p,answer,steps,**kw)
entries=[
('(i)','a','2520',r'{}^7P_5=7\cdot6\cdot5\cdot4\cdot3=2520','Assign distinct letters to five fixed vertices; order matters.','پانچ مقررہ رؤوس کو مختلف حروف دیں؛ ترتیب اہم ہے۔','پنځو ثابتو رأسونو ته بېل توري وټاکئ؛ ترتیب مهم دی.'),
('(ii)','c','28',r'7\cdot4=28','Choose any of seven tens digits and one of four odd units digits. Repetition is allowed.','دہائی کا کوئی ایک سات ہندسوں میں سے اور اکائی کا چار طاق ہندسوں میں سے لیں۔ تکرار جائز ہے۔','د لسګونو رقم له اوو او د یوګونو رقم له څلورو طاقو رقمونو وټاکئ. تکرار اجازه لري.'),
('(iv)','d',r'\frac{n+2}{n-1}',r'\frac{(n+2)!(n-2)!}{(n+1)!(n-1)!}=\frac{n+2}{n-1},\quad n\ge2','Cancel factorials; the stated factorial expression requires integer n≥2.','عام فیکٹوریل کاٹیں؛ دی گئی عبارت کے لیے صحیح عدد n≥2 درکار ہے۔','ګډ فکټوریلونه حذف کړئ؛ ورکړل شوې عبارت صحیح عدد n≥2 غواړي.'),
('(v)','a','768',r'(5-1)!\,2^5=24\cdot32=768','Treat each couple as one block around the table, then choose either order within each couple.','ہر جوڑے کو میز کے گرد ایک اکائی سمجھیں، پھر ہر جوڑے کی دو اندرونی ترتیبیں لیں۔','هره جوړه د مېز شاوخوا یو بلاک ونیسئ، بیا د هرې جوړې دوه دنني ترتیبونه واخلئ.'),
('(vi)','d','4775',r'\binom{20}4-\binom84=4845-70=4775','Subtract all-girl committees from all four-person committees.','تمام چار افراد کی کمیٹیوں سے صرف لڑکیوں والی کمیٹیاں تفریق کریں۔','له ټولو څلور کسیزو کمیټو څخه یوازې د نجونو کمیټې منفي کړئ.'),
('(vii)','c','512',r'2^{3\cdot3}=2^9=512','Each of the nine entries can independently be either 0 or 1.','نو میں سے ہر اندراج آزادانہ 0 یا 1 ہو سکتا ہے۔','له نهو عناصرو هر یو په خپلواک ډول 0 یا 1 کېدای شي.'),
('(viii)','b','20',r'\binom82-8=28-8=20','Connect every pair of vertices, then exclude the eight polygon sides.','رؤوس کا ہر جوڑا ملائیں، پھر کثیرالاضلاع کے آٹھ اضلاع نکال دیں۔','د رأسونو هره جوړه سره ونښلوئ، بیا اته ضلعې لرې کړئ.')]
for part,choice,ans,work,en,ur,ps in entries:review(1,part,'('+choice+') $'+ans+'$',[step(en,ur,ps,work)],category='mcqs')
adjacent=sum(abs(p.index(3)-p.index(7))==1 for p in permutations([2,3,4,6,7,8]));assert adjacent==240
review(1,'(iii)','No listed option is correct; $240$.',[step('Combine 3 and 7 into one block. Five objects can be ordered in 5! ways, and the block can be 37 or 73.','3 اور 7 کو ایک اکائی بنائیں۔ پانچ اشیا کی 5! ترتیبیں ہیں، اور اکائی 37 یا 73 ہو سکتی ہے۔','3 او 7 یو بلاک ونیسئ. پنځه شیان 5! ترتیبونه لري، او بلاک 37 یا 73 کېدای شي.',r'2\cdot5!=240'),step('The correct value is absent from the four printed options.','درست قیمت چار مطبوعہ اختیارات میں موجود نہیں۔','سم ارزښت په څلورو چاپ شوو انتخابونو کې نشته.')],category='mcqs',answerUr='کوئی مطبوعہ انتخاب درست نہیں؛ $240$۔',answerPs='هېڅ چاپ شوی انتخاب سم نه دی؛ $240$.')
review(1,'(ix)','(c) Not defined.',[step('Elementary conditional probability requires P(B)>0. Here division by P(B)=0 is not defined.','ابتدائی مشروط احتمال کے لیے P(B)>0 ضروری ہے۔ یہاں P(B)=0 پر تقسیم معین نہیں۔','لومړنی مشروط احتمال P(B)>0 غواړي. دلته پر P(B)=0 وېش تعریف شوی نه دی.',r'P(A|B)=\frac{P(A\cap B)}{P(B)}')],category='mcqs',answerUr='(c) تعریف شدہ نہیں۔',answerPs='(c) نه دی تعریف شوی.')
review(1,'(x)','No option follows in every case. (d) follows if $P(A\\cap B)>0$.',[step('Assume positive marginals so both conditional probabilities exist. Cross-multiplication yields either equal marginals or zero intersection probability.','دونوں مشروط احتمالات کے وجود کے لیے انفرادی احتمالات مثبت فرض کریں۔ ضرب تبادلی سے یا دونوں انفرادی احتمالات برابر ہیں یا مشترک احتمال صفر ہے۔','د دواړو مشروطو احتمالونو د شتون لپاره انفرادي احتمالونه مثبت فرض کړئ. متقابل ضرب یا برابر انفرادي احتمالونه یا صفر ګډ احتمال ورکوي.',r'P(A\cap B)\,[P(A)-P(B)]=0'),step('For example, disjoint events with probabilities 1/4 and 1/2 have both conditional probabilities zero, so (d) fails. Conversely A={1,2}, B={2,3} on a fair die have equal conditional probabilities but are neither equal nor disjoint, ruling out (a), (b) and (c) as universal answers.','مثلاً جدا واقعات کے احتمال 1/4 اور 1/2 ہوں تو دونوں مشروط احتمالات صفر ہیں، اس لیے (d) درست نہیں۔ دوسری طرف منصف پانسے پر A={1,2}، B={2,3} کے مشروط احتمالات برابر ہیں مگر واقعات نہ برابر ہیں نہ جدا؛ اس لیے (a)، (b)، (c) بھی ہر صورت میں درست نہیں۔','د بېلګې په توګه د جلا پېښو احتمالونه 1/4 او 1/2 وي، دواړه مشروط احتمالونه صفر دي، نو (d) ناکامېږي. خو پر عادلانه ځار A={1,2}، B={2,3} برابر مشروط احتمالونه لري، مګر نه برابر دي او نه جلا؛ نو (a)، (b)، (c) هم عمومي ځوابونه نه دي.')],category='mcqs',answerUr='کوئی انتخاب ہر صورت میں لازم نہیں۔ اگر $P(A\\cap B)>0$ ہو تو (d)۔',answerPs='هېڅ انتخاب په هر حالت کې لازم نه دی. که $P(A\\cap B)>0$ وي، نو (d).')
symmetry=step('Equal binomial coefficients in the same row have equal or complementary lower indices. Since r and r+2 differ, their sum equals the upper index.','ایک ہی قطار کے برابر دو رقمی سر کے زیریں اشاریے برابر یا متمم ہوتے ہیں۔ چونکہ r اور r+2 مختلف ہیں، ان کا مجموعہ بالائی اشاریے کے برابر ہے۔','په یوه قطار کې برابر دوه حدي ضریبونه برابر یا متمم ښکته اندېسونه لري. څرنګه چې r او r+2 بېل دي، مجموعه یې له پورته اندېس سره برابره ده.',r'\binom Nr=\binom N{r+2}\Rightarrow r+(r+2)=N')
review(2,'(i)',r'$r=n-1$',[symmetry,result(r'2r+2=2n\Rightarrow r=n-1')])
review(2,'(ii)',r'$56$',[symmetry,result(r'2r+2=18\Rightarrow r=8,\quad\binom85=56')])
assert R(factorial(56)//factorial(56-47),factorial(54)//factorial(54-44))==30800
review(3,'',r'$r=41$',[step('Expand the permutations as factorials and cancel common factors.','ترتیبات کو فیکٹوریل میں لکھ کر مشترک عوامل کاٹیں۔','ترتیبونه په فکټوریل ولیکئ او ګډ عوامل حذف کړئ.',r'\frac{{}^{56}P_{r+6}}{{}^{54}P_{r+3}}=\frac{56!}{(50-r)!}\frac{(51-r)!}{54!}=56\cdot55(51-r)'),result(r'3080(51-r)=30800\Rightarrow51-r=10\Rightarrow r=41')])
value=factorial(12)//(factorial(4)*factorial(3)*factorial(5));assert value==27720
review(4,'',r'$27720$',[step('Arrange twelve factors, dividing by the factorial of each repeated-factor count.','بارہ عوامل ترتیب دیں اور ہر مکرر عامل کی تعداد کے فیکٹوریل پر تقسیم کریں۔','دولس عاملونه ترتیب او د هر تکراري عامل د شمېر پر فکټوریل ووېشئ.',r'\frac{12!}{4!\,3!\,5!}=27720')])
circular=step('Fix one position to remove rotational duplicates. For an adjacent pair treat the two people as a block and allow its two internal orders.','گردشی تکرار ختم کرنے کے لیے ایک جگہ مقرر کریں۔ ملحق جوڑے کو ایک اکائی سمجھیں اور اس کی دو اندرونی ترتیبیں لیں۔','د دوراني تکرار د لرې کولو لپاره یو ځای ثابت کړئ. څنګ په څنګ جوړه یو بلاک ونیسئ او دوه دنني ترتیبونه یې واخلئ.')
review(5,'(i)',r'$72$',[circular,result(r'5!-2\cdot4!=120-48=72')])
review(5,'(ii)',r'$48$',[circular,result(r'2\cdot4!=48')])
review(6,'',r'$\frac25$',[circular,result(r'\frac{2\cdot4!}{5!}=\frac25')])
pa,pb,cond=R(4,5),R(1,2),R(2,5);joint=pa*cond
for part,val,work in [('(i)',joint,r'P(A\cap B)=P(A)P(B|A)=0.8(0.4)=0.32'),('(ii)',joint/pb,r'P(A|B)=\frac{0.32}{0.5}=0.64'),('(iii)',pa+pb-joint,r'P(A\cup B)=0.8+0.5-0.32=0.98')]:
    review(7,part,'$'+str(float(val))+'$',[addition,result(work)])
review(8,'',r'$1680$',[step('The prefix fixes 3 and 5. Fill the remaining four ordered positions without replacement from the other eight digits.','ابتدائی ہندسے 3 اور 5 مقرر ہیں۔ باقی چار ترتیب دار جگہیں دوسرے آٹھ ہندسوں سے بغیر تکرار پُر کریں۔','لومړني رقمونه 3 او 5 ثابت دي. پاتې څلور ترتیب لرونکي ځایونه له نورو اتو رقمونو بې تکراره ډک کړئ.',r'{}^8P_4=8\cdot7\cdot6\cdot5=1680')])
unique=set(permutations([2,3,0,3,4,2,3]));assert sum(p[0]!=0 for p in unique)==360
review(9,'',r'$360$',[step('Use all seven digits to exceed one million. Subtract arrangements beginning with zero; 2 is repeated twice and 3 three times.','دس لاکھ سے بڑھنے کے لیے ساتوں ہندسے لیں۔ صفر سے شروع ہونے والی ترتیبیں نکالیں؛ 2 دو مرتبہ اور 3 تین مرتبہ ہے۔','له یو میلیون څخه د اوښتلو لپاره ټول اووه رقمونه وکاروئ. په صفر پیلېدونکي ترتیبونه منفي کړئ؛ 2 دوه ځله او 3 درې ځله تکرار دی.',r'\frac{7!}{2!\,3!}-\frac{6!}{2!\,3!}=420-60=360')])
review(10,'',r'$\frac2{n-1}\ (n\ge3);\quad1\ (n=2)$',[circular,result(r'P=\frac{2(n-2)!}{(n-1)!}=\frac2{n-1}\quad(n\ge3)'),step('If there are only two men, they necessarily sit together, so the probability is 1.','اگر صرف دو مرد ہوں تو وہ لازماً ساتھ بیٹھیں گے، اس لیے احتمال 1 ہے۔','که یوازې دوه نارینه وي، خامخا یوځای کېني، نو احتمال 1 دی.')])
for part,fav in [('(i)',1),('(ii)',2),('(iii)',3),('(iv)',1)]:
    review(11,part,'$'+S.latex(R(fav,4))+'$',[step('Assume a fair spinner. Its four equal sectors are equally likely; count the required colours.','قرص کو غیر جانب دار فرض کریں۔ اس کے چار برابر حصے یکساں ممکن ہیں؛ مطلوبہ رنگ گنیں۔','قرص عادلانه فرض کړئ. څلور برابرې برخې یې مساوي احتمال لري؛ غوښتل شوي رنګونه وشمېرئ.',r'P(E)=\frac{'+str(fav)+r'}4='+S.latex(R(fav,4)))])
A.save(['Review 6'],[204,205])
