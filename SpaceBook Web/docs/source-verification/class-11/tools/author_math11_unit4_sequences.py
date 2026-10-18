from math11_answer_authoring import Author,step,S
from math import comb
R=S.Rational
A=Author(4)
def work(tex):return step('Substitute and simplify.','قیمتیں رکھ کر مختصر کریں۔','ارزښتونه کېږدئ او ساده یې کړئ.',tex)
ap=step('Use the first term and the constant difference.','پہلا رکن اور مستقل مشترک فرق استعمال کریں۔','لومړی حد او ثابت ګډ توپیر وکاروئ.',r'a_n=a_1+(n-1)d')
mean=step('For m inserted arithmetic means there are m+1 equal gaps between the endpoints.','m حسابی اوسط داخل کرنے پر دونوں سروں کے درمیان m+1 برابر وقفے ہوتے ہیں۔','د m حسابي منځنیو په ورګډولو د دواړو پایونو ترمنځ m+1 برابر واټنونه وي.',r'd=\frac{b-a}{m+1},\quad A_j=a+jd')
def put(ex,q,p,ans,steps,**kw):A.put(ex,str(q),p,ans,steps,**kw)
finite=[
('(i)','Finite: 25 terms.','محدود: 25 ارکان۔','محدود: 25 حدونه.',r'50=2n\Rightarrow n=25'),
('(ii)','Infinite.','لامحدود۔','بې پایه.',r'a_n=\frac{1+(-1)^{n-1}}2,\quad n=1,2,\ldots'),
('(iii)','Infinitely many terms, as indicated by the left ellipsis.','بائیں طرف کے نقطوں کے مطابق لامحدود ارکان۔','د کیڼو ټکو له مخې بې پایه حدونه.',r'\{\ldots,-4,0,4,\ldots,60\}=\{4k:k\in\mathbb Z,\ k\le15\}'),
('(iv)','Finite: 8 terms.','محدود: 8 ارکان۔','محدود: 8 حدونه.',r'\left(-\frac13\right)^{n-1}=-\frac1{2187}=\left(-\frac13\right)^7\Rightarrow n=8')]
for p,en,ur,ps,m in finite:
    ss=[step(en,ur,ps,m)]
    if p=='(iii)':ss.append(step('The printed left ellipsis makes this list unbounded to the left. It has no first term, so it is not a usual sequence indexed from n=1.','مطبوعہ بائیں نقطے فہرست کو بائیں طرف غیر محدود بناتے ہیں۔ اس کا پہلا رکن نہیں، اس لیے یہ n=1 سے شروع ہونے والی معمول کی ترتیب نہیں۔','چاپ شوي کیڼ ټکي لست کیڼ لوري ته بې حده کوي. لومړی حد نه لري، نو له n=1 پیلېدونکی عادي ترتیب نه دی.'))
    put('4.1',1,p,en,ss,answerUr=ur,answerPs=ps)
n=S.symbols('n',integer=True,positive=True)
for p,expr,expected in [('(i)',n*(n+1)/2,[1,3,6,10]),('(ii)',(-1)**(n-1)*2**(n+1),[4,-8,16,-32]),('(iii)',R(1,3)**n,[R(1,3),R(1,9),R(1,27),R(1,81)]),('(iv)',n*(n-1)*(n-2)/6,[0,0,1,4])]:
    values=[S.simplify(expr.subs(n,j)) for j in range(1,5)];assert values==expected
    tex=r',\ '.join(map(S.latex,values))
    put('4.1',2,p,'$'+tex+'$',[step('Set n=1,2,3,4 in the given formula.','دیے گئے کلیے میں n=1,2,3,4 رکھیں۔','په ورکړل شوي فورمول کې n=1,2,3,4 کېږدئ.',r'(a_1,a_2,a_3,a_4)=('+tex+')')])
for p,tex,desc,ur,ps in [
('(i)',r'a_n=\frac n{n+1}','The numerator is the position and the denominator is one greater.','صورت مقام کے برابر اور مخرج ایک زیادہ ہے۔','صورت د ځای شمېره او مخرج یو زیات دی.'),
('(ii)',r'a_n=(-1)^{n-1}2n','Use even magnitudes and alternating signs, starting positive.','جفت مقداریں اور بدلتی علامتیں لیں، ابتدا مثبت سے کریں۔','جفت مقدارونه او بدلېدونکې نښې واخلئ، له مثبت څخه پیل وکړئ.'),
('(iii)',r'a_n=(-1)^{n-1}','Alternate 1 and −1, starting with 1.','1 سے شروع کر کے 1 اور −1 باری باری لیں۔','له 1 پیل او 1 او −1 په وار وار واخلئ.')]:
    put('4.1',3,p,'$'+tex+'$',[step(desc,ur,ps,tex)])
for p,vals,tex in [('(i)',[3,2,3,2,3],r'a_2=5-3=2,\ a_3=5-2=3,\ a_4=5-3=2,\ a_5=5-2=3'),('(ii)',[3,3,R(3,2),R(1,2),R(1,8)],r'a_2=3/1=3,\ a_3=3/2,\ a_4=(3/2)/3=1/2,\ a_5=(1/2)/4=1/8')]:
    put('4.1',4,p,'$'+r',\ '.join(map(S.latex,vals))+'$',[step('Compute each term from the preceding term; the index in the recurrence advances by one.','ہر رکن پچھلے رکن سے نکالیں؛ تکراری تعلق میں اشاریہ ایک بڑھتا ہے۔','هر حد له مخکیني حد څخه محاسبه کړئ؛ په تکراري اړیکه کې اندېس یو زیاتېږي.',tex)])
for p,tex in [('(i)',r'-1+1+3+5+7+9'),('(ii)',r'-1+2-4+8-16'),('(iii)',r'\frac12+\frac14+\frac18+\cdots'),('(iv)',r'1+\frac32+\frac94+\frac{27}8+\cdots')]:
    put('4.1',5,p,'$'+tex+'$',[step('Replace the summation index by consecutive integers, starting at its printed lower limit.','جمع کے اشاریے کی جگہ مطبوعہ زیریں حد سے مسلسل صحیح اعداد رکھیں۔','د جمع اندېس پر ځای له چاپ شوي ښکته حد څخه پرله پسې صحیح عددونه کېږدئ.',tex)])
rows={v:[comb(v,j) for j in range(v+1)] for v in [5,6,8]}
for v,row in rows.items():
    assert all(R(row[j])*(v-j)/(j+1)==row[j+1] for j in range(v))
tex=r'\begin{aligned}'+r'\\'.join('n='+str(v)+r':\quad '+','.join(map(str,row)) for v,row in rows.items())+r'\end{aligned}'
put('4.1',6,'','$'+tex+'$',[step('Start with p₀=1 and use the recursive definition until pₙ=1.','p₀=1 سے شروع کریں اور pₙ=1 تک تکراری تعریف استعمال کریں۔','له p₀=1 پیل کړئ او تر pₙ=1 پورې تکراري تعریف وکاروئ.',r'p_0=1,\quad p_{r+1}=\frac{n-r}{r+1}p_r'),work(tex)])
put('4.2',1,'','$44$',[ap,work(r'a_{15}=2+14(5-2)=44')])
put('4.2',2,'','$38$',[ap,work(r'108=8+20d\Rightarrow d=5,\quad a_7=8+6(5)=38')])
put('4.2',3,'','$25$',[ap,work(r'78=6+3(n-1)\Rightarrow n=25')])
put('4.2',4,'',r'$d=2,\quad a_7=21$',[work(r'a_{n+1}-a_n=[2(n+1)+7]-(2n+7)=2,\quad a_7=2(7)+7=21')])
put('4.2',5,'',r'$d=\log b,\quad a_n=\log(ab^{n-1})$',[step('For real logarithms assume a,b>0 and use one fixed valid base. Apply the product and power laws.','حقیقی لوگارتھم کے لیے a,b>0 اور ایک مقرر درست اساس فرض کریں۔ حاصل ضرب اور قوت کے قوانین استعمال کریں۔','د حقیقي لوګاریتمونو لپاره a,b>0 او یوه ثابته سمه قاعده فرض کړئ. د ضرب او قوې قوانین وکاروئ.',r'\log(ab^j)=\log a+j\log b'),ap,work(r'a_n=\log a+(n-1)\log b=\log(ab^{n-1})')])
put('4.2',6,'',r'$k=\frac72;\quad14,19,24$',[work(r'2(6k-2)=(2k+7)+(8k-4)\Rightarrow2k=7'),work(r'2k+7=14,\quad6k-2=19,\quad8k-4=24')])
put('4.2',7,'',r'$\frac53,2,\frac73,\frac83,\ldots;\quad a_n=\frac{n+4}3$',[ap,work(r'2a_1+8d=6,\quad2d=\frac23\Rightarrow d=\frac13,\quad a_1=\frac53')])
put('4.2',8,'','True if $a+b+c\\ne0$; false in general.',[
step('Assume a,b,c are nonzero so every displayed fraction exists, and write T=a+b+c.','تمام کسرات کے وجود کے لیے a,b,c غیر صفر فرض کریں اور T=a+b+c لکھیں۔','د ټولو کسرونو د شتون لپاره a,b,c ناصفر فرض کړئ او T=a+b+c ولیکئ.',r'\frac{b+c-a}{a}=\frac Ta-2,\quad\frac{c+a-b}{b}=\frac Tb-2,\quad\frac{a+b-c}{c}=\frac Tc-2'),
work(r'2\left(\frac Tb-2\right)=\frac Ta-2+\frac Tc-2\Rightarrow T\left(\frac2b-\frac1a-\frac1c\right)=0'),
step('If T≠0, divide by T to obtain the required arithmetic-mean condition. Without this extra condition the claim fails: a=1,b=1,c=−2 makes all three given fractions −2, while their reciprocals 1,1,−1/2 are not in A.P.','اگر T≠0 تو T سے تقسیم کرنے پر مطلوبہ حسابی اوسط کی شرط ملتی ہے۔ اس اضافی شرط کے بغیر دعویٰ غلط ہے: a=1,b=1,c=−2 پر دی گئی تینوں کسرات −2 ہیں مگر مقلوب 1,1,−1/2 حسابی ترتیب میں نہیں۔','که T≠0 وي، پر T وېش د حسابي منځني غوښتل شوی شرط ورکوي. له دې اضافي شرط پرته ادعا ناسمه ده: a=1,b=1,c=−2 ورکړل شوي درې واړه کسرونه −2 کوي، خو مقلوبونه 1,1,−1/2 په حسابي ترتیب کې نه دي.')
],answerUr='اگر $a+b+c\\ne0$ تو درست؛ عمومی طور پر غلط۔',answerPs='که $a+b+c\\ne0$ وي سم دی؛ په عمومي ډول ناسم دی.')
put('4.2',9,'',r'$3\ \mathrm m$',[ap,work(r'a_8=24+7(-3)=3')])
put('4.2',10,'','$15135$',[step('There are ten yearly decreases from 1960 to 1970.','1960 سے 1970 تک دس سالانہ کمیاں ہیں۔','له 1960 څخه تر 1970 پورې لس کلني کمښتونه دي.',r'20135-500(1970-1960)=15135')])
put('4.2',11,'','45 hours.',[step('Read the stated distances literally: 1000 feet in hour one and 100 feet in every later hour. The question does not say 100 feet less each hour.','بیان کردہ فاصلوں کے مطابق پہلے گھنٹے میں 1000 فٹ اور ہر بعد کے گھنٹے میں 100 فٹ ہیں۔ سوال ہر گھنٹے میں 100 فٹ کم نہیں کہتا۔','ورکړل شوي واټنونه واخلئ: په لومړي ساعت کې 1000 فټه او په هر وروسته ساعت کې 100 فټه. پوښتنه هر ساعت 100 فټه کم نه وايي.',r'1000+100(t-1)=5400\Rightarrow t=45')],answerUr='45 گھنٹے۔',answerPs='45 ساعته.')
put('4.2',12,'','18,500 dollars.',[ap,work(r'a_{21}=3500+20(750)=18500')],answerUr='18,500 ڈالر۔',answerPs='18,500 ډالره.')
put('4.2',13,'',r'$(i)\ 15;\ (ii)\ \frac7{24};\ (iii)\ -111;\ (iv)\ a^2+b^2$',[step('The arithmetic mean is half the sum.','حسابی اوسط مجموعے کا نصف ہے۔','حسابي منځنی د مجموعې نیمایي دی.',r'A=\frac{x+y}2'),work(r'\frac{12+18}2=15,\quad\frac{1/3+1/4}2=\frac7{24},\quad\frac{-6-216}2=-111,\quad\frac{(a+b)^2+(a-b)^2}2=a^2+b^2')])
put('4.2',14,'',r'$(i)\ \frac{59}4,\frac{47}2,\frac{129}4;\qquad(ii)\ 20,23,26,29$',[mean,work(r'(i)\ d=\frac{41-6}4=\frac{35}4,\quad A_j=6+j\frac{35}4,\quad j=1,2,3'),work(r'(ii)\ d=\frac{32-17}5=3,\quad A_j=17+3j,\quad j=1,2,3,4')])
put('4.2',15,'',r'$n=0$ for distinct positive $a,b$.',[step('For positive a,b, multiply by the nonzero denominator and factor.','مثبت a,b کے لیے غیر صفر مخرج سے ضرب دے کر اجزائے ضربی بنائیں۔','د مثبتو a,b لپاره په ناصفر مخرج ضرب او تجزیه وکړئ.',r'2(a^{n+1}+b^{n+1})=(a+b)(a^n+b^n)\iff(a-b)(a^n-b^n)=0'),
step('When a≠b are positive, (a/b)ⁿ=1 implies n=0. If a=b, every value for which the expression is defined works. Positivity is needed for this usual unique real-exponent answer.','جب مثبت a≠b ہوں تو (a/b)ⁿ=1 سے n=0 ملتا ہے۔ اگر a=b تو ہر وہ قیمت درست ہے جس پر عبارت معین ہو۔ عام منفرد حقیقی قوت والے جواب کے لیے مثبت ہونا ضروری ہے۔','کله چې مثبت a≠b وي، (a/b)ⁿ=1 د n=0 پایله ورکوي. که a=b وي، هر ارزښت چې عبارت پکې تعریف شوی وي سم دی. د دې معمولي یوازیني حقیقي توان ځواب لپاره مثبت والی اړین دی.')],
answerUr=r'مختلف مثبت $a,b$ کے لیے $n=0$۔',answerPs=r'د بېلو مثبتو $a,b$ لپاره $n=0$.')
put('4.2',16,'',r'$\frac{11}2,6,\frac{13}2,7,\frac{15}2;\quad\text{sum}=\frac{65}2=5\left(\frac{13}2\right)$',[mean,work(r'd=\frac{8-5}6=\frac12,\quad\sum_{j=1}^5(5+j/2)=\frac{65}2=5\left(\frac{5+8}2\right)')])
put('4.2',17,'','$n=8$',[mean,work(r'\frac{5+3d}{5+7d}=\frac7{13}\Rightarrow65+39d=35+49d\Rightarrow d=3'),work(r'32=5+(n+1)3\Rightarrow n=8')])
assert sum(5+R(j,2) for j in range(1,6))==R(65,2)
assert [R(1+(-1)**(j-1),2) for j in range(1,5)]==[1,0,1,0]
assert [R(1+(-2)-1,1),R(-2+1-1,1),R(1+1+2,-2)]==[-2,-2,-2]
A.save(['4.1','4.2'],[125,128,129])
