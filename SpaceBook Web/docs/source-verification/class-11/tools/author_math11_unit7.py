import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from math11_answer_authoring import Author,step,S
from math11_phrases import *
R=S.Rational
A=Author(7)
n,k,x,y,a,b=S.symbols('n k x y a b',positive=True)
put,flush=make_put(A)
PR=lambda:dict(answerUr=PROVED[1],answerPs=PROVED[2])
def proved(ex,q,p,ss):put(ex,q,p,'Proved.',ss,category='proofs',**PR())
# ------------------------------------------------------------ 7.1
def ind_sum(q,t,F):
    for m in range(1,13):assert S.simplify(sum(t(S.Integer(j)) for j in range(1,m+1))-F(S.Integer(m)))==0,(q,m)
    assert eq0(F(k)+t(k+1)-F(k+1)),q
    nxt=S.simplify(F(k)+t(k+1))
    fk1=tex(F(k+1))
    proved('7.1',q,'',[
     BASIS(r'n=1:\ \text{LHS}='+tex(t(S.Integer(1)))+r',\ \text{RHS}='+tex(S.simplify(F(S.Integer(1))))+r'\ \Rightarrow\ \text{LHS}=\text{RHS}'),
     HYP(r'S_k='+tex(F(k))),
     NEXT(r'S_{k+1}=S_k+t_{k+1}='+tex(F(k))+'+'+tex(t(k+1))+'='+(tex(S.factor(nxt)) if not nxt.has(S.factorial) else tex(nxt))+'='+fk1),
     CONC])
ind_sum(1,lambda j:2*j,lambda m:m*(m+1))
ind_sum(2,lambda j:4*j-3,lambda m:m*(2*m-1))
ind_sum(3,lambda j:3*j,lambda m:3*m*(m+1)/2)
ind_sum(4,lambda j:4*j-1,lambda m:m*(2*m+1))
ind_sum(5,lambda j:j**3,lambda m:(m*(m+1)/2)**2)
ind_sum(6,lambda j:j*S.factorial(j),lambda m:S.factorial(m+1)-1)
ind_sum(7,lambda j:j*(j+1),lambda m:m*(m+1)*(m+2)/3)
ind_sum(8,lambda j:2**(j-1),lambda m:2**m-1)
ind_sum(9,lambda j:1/S.Integer(3)**j,lambda m:R(1,2)*(1-1/S.Integer(3)**m))
# 10, 11 : hockey-stick identities by Pascal's rule
C=S.binomial
assert all(sum(C(j+4,5) for j in range(1,m+1))==C(m+5,6) for m in range(1,10))
proved('7.1',10,'',[BASIS(r'n=1:\ \dbinom55=1=\dbinom66'),HYP(r'\dbinom55+\dbinom65+\cdots+\dbinom{k+4}5=\dbinom{k+5}6'),
 NEXT(r'\text{Add }\dbinom{k+5}5\text{ and use Pascal\'s rule }\dbinom{m}{r}+\dbinom{m}{r-1}=\dbinom{m+1}{r}:\quad\dbinom{k+5}6+\dbinom{k+5}5=\dbinom{k+6}6=\dbinom{(k+1)+5}6'),CONC])
assert all(sum(C(j,2) for j in range(2,m+1))==C(m+1,3) for m in range(2,12))
proved('7.1',11,'',[step('Check the statement for the first value $n=2$.','پہلی قیمت $n=2$ کے لیے بیان کی جانچ کریں۔','د لومړي ارزښت $n=2$ لپاره بیان وڅېړئ.',r'\dbinom22=1=\dbinom33'),
 HYP(r'\dbinom22+\dbinom32+\cdots+\dbinom k2=\dbinom{k+1}3\quad(k\ge2)'),
 NEXT(r'\dbinom{k+1}3+\dbinom{k+1}2=\dbinom{k+2}3=\dbinom{(k+1)+1}3\quad\text{(Pascal\'s rule)}'),CONC])
# 12 ... divisibility
for m in range(1,15):
    assert (25**m-1)%24==0 and (10**(m+1)-9*m-10)%81==0
put('7.1',12,'(i)','Proved: $\\dfrac{5^{2n}-1}{24}$ is an integer.',[BASIS(r'n=1:\ \frac{5^2-1}{24}=1\ \text{(integer)}'),HYP(r'5^{2k}-1=24m\ \text{ for some integer }m'),
 NEXT(r'5^{2(k+1)}-1=25\cdot5^{2k}-1=25(5^{2k}-1)+24=25(24m)+24=24(25m+1)'),
 step('So $5^{2(k+1)}-1$ is a multiple of 24.','لہٰذا $5^{2(k+1)}-1$، 24 کا ضعف ہے۔','نو $5^{2(k+1)}-1$ د 24 ضرب دی.'),CONC],category='proofs',answerUr='ثابت: $\\dfrac{5^{2n}-1}{24}$ صحیح عدد ہے۔',answerPs='ثابت: $\\dfrac{5^{2n}-1}{24}$ صحیح عدد دی.')
put('7.1',12,'(ii)','Proved: $\\dfrac{10^{n+1}-9n-10}{81}$ is an integer.',[BASIS(r'n=1:\ \frac{10^2-9-10}{81}=\frac{81}{81}=1'),HYP(r'10^{k+1}-9k-10=81m\ \text{ for some integer }m'),
 NEXT(r'10^{k+2}-9(k+1)-10=10\left(10^{k+1}-9k-10\right)+81k+81=810m+81(k+1)=81(10m+k+1)'),CONC],category='proofs',answerUr='ثابت: $\\dfrac{10^{n+1}-9n-10}{81}$ صحیح عدد ہے۔',answerPs='ثابت: $\\dfrac{10^{n+1}-9n-10}{81}$ صحیح عدد دی.')
proved('7.1',13,'(i)',[BASIS(r'n=1:\ 2^1=2>1'),HYP(r'2^k>k'),NEXT(r'2^{k+1}=2\cdot2^k>2k=k+k\ge k+1\quad(k\ge1)'),CONC])
assert all(S.factorial(m)>m*m for m in range(4,20))
proved('7.1',13,'(ii)',[step('Check the first value $n=4$.','پہلی قیمت $n=4$ کی جانچ کریں۔','لومړی ارزښت $n=4$ وڅېړئ.',r'4!=24>16=4^2'),HYP(r'k!>k^2\quad(k\ge4)'),
 NEXT(r'(k+1)!=(k+1)\,k!>(k+1)k^2>(k+1)(k+1)=(k+1)^2\quad\text{since }k^2>k+1\text{ for }k\ge2'),CONC])
assert all((3**(2*m-1)+2**(2*m-1))%5==0 and (4**m-1)%3==0 for m in range(1,15))
put('7.1',14,'(i)','Proved: 5 is a factor of $3^{2n-1}+2^{2n-1}$.',[BASIS(r'n=1:\ 3^1+2^1=5'),HYP(r'3^{2k-1}+2^{2k-1}=5m'),
 NEXT(r'3^{2k+1}+2^{2k+1}=9\cdot3^{2k-1}+4\cdot2^{2k-1}=4\left(3^{2k-1}+2^{2k-1}\right)+5\cdot3^{2k-1}=5\left(4m+3^{2k-1}\right)'),CONC],category='proofs',answerUr='ثابت: 5، $3^{2n-1}+2^{2n-1}$ کا جزو ہے۔',answerPs='ثابت: 5 د $3^{2n-1}+2^{2n-1}$ فکتور دی.')
put('7.1',14,'(ii)','Proved: $2^{2n}-1$ is a multiple of 3.',[BASIS(r'n=1:\ 2^2-1=3'),HYP(r'2^{2k}-1=3m'),NEXT(r'2^{2(k+1)}-1=4\cdot2^{2k}-1=4\left(2^{2k}-1\right)+3=12m+3=3(4m+1)'),CONC],category='proofs',answerUr='ثابت: $2^{2n}-1$، 3 کا ضعف ہے۔',answerPs='ثابت: $2^{2n}-1$ د 3 ضرب دی.')
proved('7.1',15,'',[step('Let $n=2m$ and induct on $m$. For $m=1$: $a^2-b^2=(a+b)(a-b)$, divisible by $a+b$.','$n=2m$ لیں اور $m$ پر استقرا کریں۔ $m=1$ کے لیے $a^2-b^2=(a+b)(a-b)$ پر $a+b$ سے تقسیم ہوتا ہے۔','$n=2m$ واخلئ او پر $m$ استقرا وکاروئ. د $m=1$ لپاره $a^2-b^2=(a+b)(a-b)$ چې پر $a+b$ وېشل کېږي.'),
 step('Assume $a+b$ divides $a^{2m}-b^{2m}$.','فرض کریں $a+b$، $a^{2m}-b^{2m}$ کو تقسیم کرتا ہے۔','فرض کړئ $a+b$ پر $a^{2m}-b^{2m}$ وېشي.'),
 step('Rewrite the next even power.','اگلی جفت قوت کو یوں لکھیں۔','بله جفته قوه داسې ولیکئ.',r'a^{2m+2}-b^{2m+2}=a^2\left(a^{2m}-b^{2m}\right)+b^{2m}\left(a^2-b^2\right)'),
 step('Both parts are divisible by $a+b$, so is their sum; by induction the result holds for every even $n$.','دونوں حصے $a+b$ سے قابلِ تقسیم ہیں، اس لیے ان کا مجموعہ بھی؛ استقرا سے نتیجہ ہر جفت $n$ کے لیے درست ہے۔','دواړه برخې پر $a+b$ وېشل کېږي، نو مجموعه یې هم؛ د استقرا له مخې پایله د هر جفت $n$ لپاره سمه ده.')])
# ------------------------------------------------------------ 7.2
sx=step('Use the binomial theorem $(p+q)^n=\\sum_{r=0}^{n}\\binom nr p^{n-r}q^r$.','دو رقمی مسئلہ $(p+q)^n=\\sum_{r=0}^{n}\\binom nr p^{n-r}q^r$ استعمال کریں۔','د دوه حدي قضیه $(p+q)^n=\\sum_{r=0}^{n}\\binom nr p^{n-r}q^r$ وکاروئ.')
tr=step(r'The general term is $T_{r+1}=\binom nr p^{n-r}q^r$.',r'عمومی رکن $T_{r+1}=\binom nr p^{n-r}q^r$ ہے۔',r'عمومي حد $T_{r+1}=\binom nr p^{n-r}q^r$ دی.')
e1=S.expand((x**2-1/y)**4);e2=S.expand((1+x*y)**7);e3=S.expand((S.sqrt(y)+1/S.sqrt(y))**5)
put('7.2',1,'(i)','$'+tex(e1)+'$',[sx,work(r'(x^2-1/y)^4=x^8-4x^6y^{-1}+6x^4y^{-2}-4x^2y^{-3}+y^{-4}')])
put('7.2',1,'(ii)','$'+tex(e2)+'$',[sx,work(r'(1+xy)^7=\sum_{r=0}^7\binom7r(xy)^r')])
assert S.simplify(e3-(y**R(5,2)+5*y**R(3,2)+10*y**R(1,2)+10/y**R(1,2)+5/y**R(3,2)+1/y**R(5,2)))==0
put('7.2',1,'(iii)',r'$y^{5/2}+5y^{3/2}+10y^{1/2}+10y^{-1/2}+5y^{-3/2}+y^{-5/2}$',[sx,work(r'\left(\sqrt y+\frac1{\sqrt y}\right)^5=\sum_{r=0}^5\binom5r y^{(5-2r)/2}')])
t2a=C(7,3)*2**4;t2b=C(10,7)*R(1,2)**3*(-3)**7;t2c=C(4,2)
put('7.2',2,'(i)',r'$560a^3$',[tr,work(r'T_4=\binom73\,2^{4}a^{3}=35\cdot16\,a^3=560a^3')])
put('7.2',2,'(ii)',r'$-\binom{10}7\,2^{-3}\cdot3^7\,x^3y^{-7}=-\dfrac{32805}{1}\cdot\dfrac{x^3}{y^7}$'.replace(r'\dfrac{32805}{1}\cdot','32805\\cdot'),[tr,work(r'T_8=\binom{10}7\left(\frac x2\right)^3\left(-\frac3y\right)^7=-120\cdot\frac{3^7}{8}\cdot\frac{x^3}{y^7}=-32805\,\frac{x^3}{y^7}')])
assert t2b==-32805
put('7.2',2,'(iii)',r'$6x^3$',[tr,work(r'T_3=\binom42\left(x^2\right)^2\left(x^{-1/2}\right)^2=6x^{4-1}=6x^3')])
t3a=C(9,3)*R(4,3)**6*R(-3,2)**3
put('7.2',3,'(i)','$2268$',[tr,work(r'T_{r+1}=\binom9r\left(\frac{4a^2}3\right)^{9-r}\left(-\frac3{2a}\right)^r:\ \ a^{18-3r}=a^0\Rightarrow r=6'),work(r'T_7=\binom96\left(\frac{4}{3}\right)^3\left(-\frac32\right)^6\cdot a^0='+tex(C(9,6)*R(4,3)**3*R(3,2)**6)+r'')])
v=C(9,6)*R(4,3)**3*R(3,2)**6;assert v==2268
t3b=C(10,2)*9;assert t3b==405
put('7.2',3,'(ii)','$405$',[tr,work(r'T_{r+1}=\binom{10}r x^{10-r}\left(-\frac3{x^4}\right)^r:\ 10-5r=0\Rightarrow r=2'),work(r'T_3=\binom{10}2(-3)^2=45\cdot9=405')])
put('7.2',3,'(iii)',r'$-\binom{21}7=-116280$',[tr,work(r'T_{r+1}=\binom{21}r x^{21-r}\left(-\frac1{x^2}\right)^r:\ 21-3r=0\Rightarrow r=7'),work(r'T_8=(-1)^7\binom{21}7=-116280')])
assert C(21,7)==116280
assert S.Poly(S.expand((x**2-x)**20),x).coeff_monomial(x**23)==-1140
put('7.2',4,'(i)','$-1140$',[tr,work(r'(x^2-x)^{20}=x^{20}(x-1)^{20}:\ \text{need the coefficient of }x^3\text{ in }(x-1)^{20}'),work(r'\binom{20}{17}(-1)^{17}=-\binom{20}3=-1140')])
put('7.2',4,'(ii)',r'$1120$',[tr,work(r'T_{r+1}=\binom8r2^{8-r}\left(-\frac1x\right)^r:\ x^{-r}=x^{-4}\Rightarrow r=4'),work(r'\binom84\,2^4=70\cdot16=1120=2^4\cdot{}^8C_4')])
assert C(8,4)*16==1120
c43=-C(9,3)*2**6*R(1,27);assert c43==-C(9,3)*R(64,27)
put('7.2',4,'(iii)',r'$-\binom93\cdot\dfrac{2^6}{27}=-\dfrac{5376}{27}=-\dfrac{1792}9$',[tr,work(r'a^6b^3:\ r=3,\quad \binom93(2a)^6\left(-\frac b3\right)^3=-84\cdot64\cdot\frac1{27}a^6b^3'),work(r'=-\frac{5376}{27}=-\frac{1792}9')])
assert c43==R(-1792,9)
put('7.2',5,'(i)',r'$70a^4b^4$',[step('For $n=8$ (even) there is one middle term, $T_5$.','$n=8$ (جفت) کے لیے ایک درمیانی رکن $T_5$ ہے۔','د $n=8$ (جفت) لپاره یو منځنی حد $T_5$ دی.'),work(r'T_5=\binom84\left(\frac ax\right)^4(bx)^4=70a^4b^4')])
put('7.2',5,'(ii)',r'$T_5=\dfrac{15309}8x^{13}$ and $T_6=-\dfrac{5103}{16}x^{14}$',[step('For $n=9$ (odd) there are two middle terms, $T_5$ and $T_6$.','$n=9$ (طاق) کے لیے دو درمیانی ارکان $T_5$ اور $T_6$ ہیں۔','د $n=9$ (طاق) لپاره دوه منځني حدونه $T_5$ او $T_6$ دي.'),
 work(r'T_5=\binom94(3x)^5\left(-\frac{x^2}2\right)^4=126\cdot243\cdot\frac1{16}x^{13}=\frac{15309}8x^{13}'),work(r'T_6=\binom95(3x)^4\left(-\frac{x^2}2\right)^5=-126\cdot81\cdot\frac1{32}x^{14}=-\frac{5103}{16}x^{14}')])
assert 126*243*R(1,16)==R(15309,8) and 126*81*R(1,32)==R(5103,16)
put('7.2',5,'(iii)',r'$-252x^{10}y^5$',[step('For $n=10$ the middle term is $T_6$.','$n=10$ کے لیے درمیانی رکن $T_6$ ہے۔','د $n=10$ لپاره منځنی حد $T_6$ دی.'),work(r'T_6=\binom{10}5\left(3x^2\right)^5\left(-\frac y3\right)^5=-252x^{10}y^5')])
put('7.2',6,'','There is no constant term.',[tr,work(r'T_{r+1}=\binom{23}r\left(2\sqrt x\right)^{23-r}\left(-3x^{-3/2}\right)^r\ \propto\ x^{(23-4r)/2}'),step('A constant term needs $23-4r=0$, i.e. $r=23/4$, which is not an integer. So no constant term exists.','مستقل رکن کے لیے $23-4r=0$ یعنی $r=23/4$ چاہیے جو صحیح عدد نہیں۔ لہٰذا کوئی مستقل رکن نہیں۔','د ثابت حد لپاره $23-4r=0$ یعنې $r=23/4$ پکار دی چې صحیح عدد نه دی. نو ثابت حد نشته.')],answerUr='کوئی مستقل رکن نہیں۔',answerPs='ثابت حد نشته.')
v1=S.expand((2+S.sqrt(3))**5+(2-S.sqrt(3))**5);v2=S.expand((1+S.sqrt(2))**4-(1-S.sqrt(2))**4);v3=S.expand((a+b)**5+(a-b)**5)
assert v1==724 and v2==24*S.sqrt(2)
put('7.2',7,'(i)','$724$',[step('In $(p+q)^n+(p-q)^n$ the odd powers of $q$ cancel and the even-power terms double.','$(p+q)^n+(p-q)^n$ میں $q$ کی طاق قوتیں کٹ جاتی ہیں اور جفت قوتوں والے ارکان دوگنے ہو جاتے ہیں۔','په $(p+q)^n+(p-q)^n$ کې د $q$ طاقې قوې حذف کېږي او جفتې قوې دوه برابره کېږي.'),work(r'2\left[2^5+\binom52 2^3(\sqrt3)^2+\binom54 2(\sqrt3)^4\right]=2[32+240+90]=724')])
put('7.2',7,'(ii)',r'$24\sqrt2$',[step('In $(p+q)^n-(p-q)^n$ the even powers of $q$ cancel and the odd-power terms double.','$(p+q)^n-(p-q)^n$ میں $q$ کی جفت قوتیں کٹ جاتی ہیں اور طاق قوتوں والے ارکان دوگنے ہو جاتے ہیں۔','په $(p+q)^n-(p-q)^n$ کې د $q$ جفتې قوې حذف کېږي او طاقې قوې دوه برابره کېږي.'),work(r'2\left[\binom41\sqrt2+\binom43(\sqrt2)^3\right]=2[4\sqrt2+8\sqrt2]=24\sqrt2')])
assert v3==2*a**5+20*a**3*b**2+10*a*b**4
put('7.2',7,'(iii)',r'$2a^5+20a^3b^2+10ab^4$',[work(r'2\left[a^5+\binom52a^3b^2+\binom54ab^4\right]=2a^5+20a^3b^2+10ab^4')])
terms=[C(10,r)*3**(10-r)*R(-3,2)**r for r in range(11)];mx=max(range(11),key=lambda r:abs(terms[r]));assert mx==3 and terms[3]==-885735
put('7.2',8,'',r'$T_4=-885735$',[step(r'For $(a+b)^n$, $\left|\frac{T_{r+1}}{T_r}\right|=\frac{n-r+1}{r}\left|\frac ba\right|$. Here $a=3$, $b=-2x=-\frac32$.',r'$(a+b)^n$ کے لیے $\left|\frac{T_{r+1}}{T_r}\right|=\frac{n-r+1}{r}\left|\frac ba\right|$۔ یہاں $a=3$، $b=-2x=-\frac32$۔',r'د $(a+b)^n$ لپاره $\left|\frac{T_{r+1}}{T_r}\right|=\frac{n-r+1}{r}\left|\frac ba\right|$. دلته $a=3$، $b=-2x=-\frac32$.'),
 work(r'\frac{11-r}{r}\cdot\frac12\ge1\iff r\le\frac{11}3\Rightarrow r=3\text{ gives the greatest term }T_4'),work(r'T_4=\binom{10}33^7\left(-\frac32\right)^3=-120\cdot2187\cdot\frac{27}8=-885735')])
t9=[C(20,r)*12**(20-r)*(-4)**r for r in range(21)];m9=max(range(21),key=lambda r:abs(t9[r]));assert m9==5
put('7.2',9,'',r'$T_6=-\binom{20}5\,12^{15}\,4^5$',[step(r'Here $a=x=12$, $b=-y=-4$: $\left|\frac{T_{r+1}}{T_r}\right|=\frac{21-r}{r}\cdot\frac13\ge1\iff r\le\frac{21}4=5.25$.',r'یہاں $a=x=12$، $b=-y=-4$: $\left|\frac{T_{r+1}}{T_r}\right|=\frac{21-r}{r}\cdot\frac13\ge1\iff r\le\frac{21}4=5.25$۔',r'دلته $a=x=12$، $b=-y=-4$: $\left|\frac{T_{r+1}}{T_r}\right|=\frac{21-r}{r}\cdot\frac13\ge1\iff r\le\frac{21}4=5.25$.'),
 work(r'r=5\Rightarrow T_6=\binom{20}512^{15}(-4)^5=-15504\cdot12^{15}\cdot4^5'),
 step('The printed key shows a different exponent pattern; the value computed here is the greatest term by the ratio test.','مطبوعہ جوابی کنجی میں قوتوں کی صورت مختلف چھپی ہے؛ یہاں نسبت کی جانچ سے نکلا رکن سب سے بڑا ہے۔','په چاپ شوې کیلي کې د قوتونو بڼه توپیر لري؛ دلته د نسبت له ازموینې ترلاسه شوی حد تر ټولو لوی دی.')])
put('7.2',10,'',r'Proved: $\sum\binom nr=2^n$ and $\sum_{\text{odd}}=\sum_{\text{even}}=2^{n-1}$',[step('Put $x=1$ in $(1+x)^n=\\sum\\binom nrx^r$.','$(1+x)^n=\\sum\\binom nrx^r$ میں $x=1$ رکھیں۔','په $(1+x)^n=\\sum\\binom nrx^r$ کې $x=1$ کېږدئ.',r'2^n=\binom n0+\binom n1+\cdots+\binom nn'),
 step('Put $x=-1$.','$x=-1$ رکھیں۔','$x=-1$ کېږدئ.',r'0=\left[\binom n0+\binom n2+\cdots\right]-\left[\binom n1+\binom n3+\cdots\right]'),
 step('So the even-order and odd-order sums are equal; together they equal $2^n$, hence each is $2^{n-1}$.','لہٰذا جفت اور طاق درجے کے مجموعے برابر ہیں؛ دونوں مل کر $2^n$ ہیں، اس لیے ہر ایک $2^{n-1}$ ہے۔','نو د جفت او طاق مرتبو مجموعې سره برابرې دي؛ دواړه یوځای $2^n$ دي، نو هره یوه $2^{n-1}$ ده.')],category='proofs',answerUr='ثابت: $\\sum\\binom nr=2^n$ اور طاق اور جفت مجموعے $=2^{n-1}$۔',answerPs='ثابت: $\\sum\\binom nr=2^n$ او طاق او جفت مجموعې $=2^{n-1}$.')
put('7.2',11,'','Proved.',[step(r'Write $(1+x)^n=C_0+C_1x+C_2x^2+\cdots+C_nx^n$ and differentiate both sides with respect to $x$.',r'$(1+x)^n=C_0+C_1x+C_2x^2+\cdots+C_nx^n$ لکھیں اور دونوں طرف $x$ کے لحاظ سے تفرق کریں۔',r'$(1+x)^n=C_0+C_1x+C_2x^2+\cdots+C_nx^n$ ولیکئ او دواړه خواوې د $x$ په اړه تفریق کړئ.',r'n(1+x)^{n-1}=C_1+2C_2x+3C_3x^2+\cdots+nC_nx^{n-1}'),
 step(r'Alternatively, $rC_r=n\binom{n-1}{r-1}$, so the right side is $n\sum\binom{n-1}{r-1}x^{r-1}=n(1+x)^{n-1}$.',r'متبادل طور پر $rC_r=n\binom{n-1}{r-1}$، لہٰذا دایاں طرف $n\sum\binom{n-1}{r-1}x^{r-1}=n(1+x)^{n-1}$ ہے۔',r'بدیل ډول $rC_r=n\binom{n-1}{r-1}$، نو ښي خوا $n\sum\binom{n-1}{r-1}x^{r-1}=n(1+x)^{n-1}$ ده.')],category='proofs',**PR())
# ------------------------------------------------------------ 7.3
bs=step(r'Use $(1+z)^m=1+mz+\frac{m(m-1)}{2!}z^2+\frac{m(m-1)(m-2)}{3!}z^3+\cdots,\ |z|<1$.',r'$(1+z)^m=1+mz+\frac{m(m-1)}{2!}z^2+\frac{m(m-1)(m-2)}{3!}z^3+\cdots،\ |z|<1$ استعمال کریں۔',r'$(1+z)^m=1+mz+\frac{m(m-1)}{2!}z^2+\frac{m(m-1)(m-2)}{3!}z^3+\cdots،\ |z|<1$ وکاروئ.')
def ser(e,v,N=4):return S.series(e,v,0,N).removeO()
s1=ser((1-x)**R(-1,2),x);s2=ser((1-x)**R(3,2),x);s3=ser((8+12*x)**R(2,3),x)
assert s1==1+x/2+3*x**2/8+5*x**3/16 and s2==1-3*x/2+3*x**2/8+x**3/16 and s3==4+4*x-x**2+2*x**3/3
put('7.3',1,'(i)',r'$1+\dfrac x2+\dfrac{3x^2}8+\dfrac{5x^3}{16}+\cdots$',[bs,work(r'(1-x)^{-1/2}:\ m=-\tfrac12,\ z=-x')])
put('7.3',1,'(ii)',r'$1-\dfrac{3x}2+\dfrac{3x^2}8+\dfrac{x^3}{16}+\cdots$',[bs,work(r'(1-x)^{3/2}:\ m=\tfrac32,\ z=-x')])
put('7.3',1,'(iii)',r'$4+4x-x^2+\dfrac23x^3+\cdots$',[bs,work(r'(8+12x)^{2/3}=8^{2/3}\left(1+\tfrac32x\right)^{2/3}=4\left[1+x-\tfrac14x^2+\tfrac16x^3-\cdots\right]')])
assert abs(float(5*(1+R(1,25))**R(1,2))-5.099)<1e-3
put('7.3',2,'(i)','$5.099$',[bs,work(r'\sqrt{26}=5\left(1+\tfrac1{25}\right)^{1/2}=5\left[1+\tfrac1{50}-\tfrac1{5000}+\cdots\right]=5.0990\ldots\approx5.099')])
put('7.3',2,'(ii)','$1.001$',[bs,work(r'\frac1{\sqrt{0.998}}=(1-0.002)^{-1/2}=1+0.001+0.0000015+\cdots=1.0010015\approx1.001')])
put('7.3',2,'(iii)','$5.01330$',[bs,work(r'\sqrt[3]{126}=5\left(1+\tfrac1{125}\right)^{1/3}=5\left[1+\tfrac1{375}-\tfrac1{70\,312.5}\cdots\right]\approx5.01330')])
assert abs(float(126**R(1,3))-5.01330)<5e-6
s3x=ser(S.sqrt((1-x)/(1+x)),x)
assert s3x==1-x+x**2/2-x**3/2
put('7.3',3,'',r'$1-x+\dfrac{x^2}2-\dfrac{x^3}2+\cdots$',[bs,work(r'(1-x)^{1/2}(1+x)^{-1/2}=\left[1-\tfrac x2-\tfrac{x^2}8-\tfrac{x^3}{16}\right]\left[1-\tfrac x2+\tfrac{3x^2}8-\tfrac{5x^3}{16}\right]=1-x+\tfrac{x^2}2-\tfrac{x^3}2')])
assert ser(S.sqrt((1-3*x)/(1+4*x)),x,2)==1-7*x/2
put('7.3',4,'','Proved.',[bs,work(r'(1-3x)^{1/2}(1+4x)^{-1/2}\approx\left(1-\tfrac{3x}2\right)(1-2x)\approx1-\tfrac{7x}2\quad(x^2\text{ neglected})')],category='proofs',**PR())
assert ser((8+3*x)**R(2,3)/((2+3*x)*S.sqrt(4-5*x)),x,2)==1-R(5,8)*x
put('7.3',5,'','Proved.',[bs,work(r'(8+3x)^{2/3}\approx4\left(1+\tfrac x4\right),\ (2+3x)=2\left(1+\tfrac{3x}2\right),\ \sqrt{4-5x}\approx2\left(1-\tfrac{5x}8\right)'),work(r'\frac{4(1+x/4)}{4(1+3x/2)(1-5x/8)}\approx\left(1+\tfrac x4\right)\left(1-\tfrac{3x}2\right)\left(1+\tfrac{5x}8\right)\approx1+\left(\tfrac14-\tfrac32+\tfrac58\right)x=1-\tfrac58x')],category='proofs',**PR())
t=S.symbols('t')
assert ser((1-2*t)**R(1,2)*(1+t)**-2,t,3)==1-3*t+R(9,2)*t**2
put('7.3',6,'',r'$1-\dfrac3x+\dfrac9{2x^2}$',[step(r'Divide numerator and denominator by $x^3$ and put $t=\frac1x$.',r'صورت اور مخرج کو $x^3$ سے تقسیم کریں اور $t=\frac1x$ رکھیں۔',r'صورت او مخرج پر $x^3$ تقسیم کړئ او $t=\frac1x$ کېږدئ.',r'\frac{x\sqrt{x^2-2x}}{(x+1)^2}=\frac{\sqrt{1-2t}}{(1+t)^2}'),bs,work(r'(1-2t)^{1/2}(1+t)^{-2}=\left(1-t-\tfrac{t^2}2\right)\left(1-2t+3t^2\right)=1-3t+\tfrac92t^2\quad(t^3\text{ neglected})')])
assert ser((1+x)**R(1,4)+(1-x)**R(1,4),x,4)==2-R(3,16)*x**2
put('7.3',7,'',r'$a=2,\quad b=\dfrac3{16}$',[bs,work(r'(1+x)^{1/4}+(1-x)^{1/4}=2\left[1+\tfrac{(1/4)(-3/4)}{2}x^2\right]=2-\tfrac3{16}x^2\Rightarrow a=2,\ b=\tfrac3{16}')])
lhs=((1+x/2)**3-(1+3*x)**R(1,2))/(1-R(5,6)*x)
assert ser(lhs,x,4)==R(15,8)*x**2
put('7.3',8,'','Proved.',[bs,work(r'(1+\tfrac x2)^3=1+\tfrac{3x}2+\tfrac{3x^2}4+\tfrac{x^3}8,\quad(1+3x)^{1/2}=1+\tfrac{3x}2-\tfrac{9x^2}8+\tfrac{27x^3}{16}'),work(r'\text{Numerator}=\tfrac{15x^2}8-\tfrac{25x^3}{16};\quad\left(1-\tfrac{5x}6\right)^{-1}=1+\tfrac{5x}6+\cdots'),work(r'\frac{\tfrac{15x^2}8-\tfrac{25x^3}{16}}{1-\tfrac{5x}6}=\tfrac{15x^2}8\ (\text{to }x^3):\quad\tfrac{15}8x^2+\left(\tfrac{15}8\cdot\tfrac56-\tfrac{25}{16}\right)x^3=\tfrac{15}8x^2')],category='proofs',**PR())
assert ser(((1+x)/(1-x))**2,x,7)==1+4*x+8*x**2+12*x**3+16*x**4+20*x**5+24*x**6
put('7.3',9,'',r'$4n\ \ (n\ge1)$',[step(r'Write $\left(\frac{1+x}{1-x}\right)^2=(1+x)^2(1-x)^{-2}$ and use $(1-x)^{-2}=\sum(r+1)x^r$.',r'$\left(\frac{1+x}{1-x}\right)^2=(1+x)^2(1-x)^{-2}$ لکھیں اور $(1-x)^{-2}=\sum(r+1)x^r$ استعمال کریں۔',r'$\left(\frac{1+x}{1-x}\right)^2=(1+x)^2(1-x)^{-2}$ ولیکئ او $(1-x)^{-2}=\sum(r+1)x^r$ وکاروئ.'),work(r'[x^n]=(n+1)+2n+(n-1)=4n\quad(n\ge1)')])
import math
v10=sum(R((-1)**j*math.prod(range(1,2*j,2)),math.factorial(j)*4**j) for j in range(0,60))
assert abs(float(v10)-float(S.sqrt(R(2,3))))<1e-12
put('7.3',10,'(i)',r'$\sqrt{\dfrac23}$',[bs,work(r'(1+z)^{-1/2}=1-\tfrac z2+\tfrac{1\cdot3}{2!}\tfrac{z^2}{2^2}-\cdots;\ \text{with }z=\tfrac12\text{ the terms are }1-\tfrac1{2^2}+\tfrac{1\cdot3}{2!}\tfrac1{2^4}-\cdots'),work(r'\text{Sum}=\left(1+\tfrac12\right)^{-1/2}=\left(\tfrac32\right)^{-1/2}=\sqrt{\tfrac23}')],answerUr=r'$\sqrt{\dfrac23}$',answerPs=r'$\sqrt{\dfrac23}$')
def tt(j):
    r=R(1)
    for i in range(j):r*=R(5+3*i,8+4*i)
    return r
assert abs(float(sum(tt(j) for j in range(0,500)))-float(2*(4**R(2,3)-1)))<1e-9
put('7.3',10,'(ii)',r'$2\left(4^{2/3}-1\right)=2\left(2^{4/3}-1\right)\approx3.0397$',[
 step(r'Ratio of consecutive terms: $\frac{t_j}{t_{j-1}}=\frac{5+3(j-1)}{8+4(j-1)}$. Put $i=j+1$: it becomes $\frac34\cdot\frac{i-1/3}{i}$.',r'مسلسل ارکان کی نسبت: $\frac{t_j}{t_{j-1}}=\frac{5+3(j-1)}{8+4(j-1)}$۔ $i=j+1$ رکھیں تو یہ $\frac34\cdot\frac{i-1/3}{i}$ بن جاتی ہے۔',r'د پرله پسې حدونو نسبت: $\frac{t_j}{t_{j-1}}=\frac{5+3(j-1)}{8+4(j-1)}$. $i=j+1$ کېږدئ نو دا $\frac34\cdot\frac{i-1/3}{i}$ کېږي.'),
 step(r'For $(1-x)^{-2/3}=\sum u_ix^i$ the coefficient ratio is $\frac{u_i}{u_{i-1}}=\frac{i-1/3}i\,x$. With $x=\frac34$ this is the same ratio, and $t_0=1=2u_1$ because $u_1=\frac23\cdot\frac34=\frac12$.',r'$(1-x)^{-2/3}=\sum u_ix^i$ کے لیے سروں کی نسبت $\frac{u_i}{u_{i-1}}=\frac{i-1/3}i\,x$ ہے۔ $x=\frac34$ پر یہی نسبت بنتی ہے، اور $t_0=1=2u_1$ کیونکہ $u_1=\frac23\cdot\frac34=\frac12$۔',r'د $(1-x)^{-2/3}=\sum u_ix^i$ لپاره د ضریبونو نسبت $\frac{u_i}{u_{i-1}}=\frac{i-1/3}i\,x$ دی. په $x=\frac34$ همدا نسبت جوړېږي، او $t_0=1=2u_1$ ځکه چې $u_1=\frac23\cdot\frac34=\frac12$.'),
 work(r'\text{Sum}=2\sum_{i\ge1}u_i=2\left[(1-x)^{-2/3}-1\right]=2\left[\left(\tfrac14\right)^{-2/3}-1\right]=2\left(4^{2/3}-1\right)')],
 answerUr=r'$2\left(4^{2/3}-1\right)\approx3.0397$',answerPs=r'$2\left(4^{2/3}-1\right)\approx3.0397$')
yv=S.sqrt(2)-1
assert S.simplify(yv**2+2*yv-1)==0 and S.simplify(4*(yv/2)**2+4*(yv/2)-1)==0
put('7.3',11,'','Proved.',[step(r'Compare with $(1-z)^{-1/2}=1+\frac z2+\frac{1\cdot3}{2!}\frac{z^2}{2^2}+\frac{1\cdot3\cdot5}{3!}\frac{z^3}{2^3}+\cdots$. With $z=\frac12$ the series becomes $1+y$.',r'$(1-z)^{-1/2}=1+\frac z2+\frac{1\cdot3}{2!}\frac{z^2}{2^2}+\frac{1\cdot3\cdot5}{3!}\frac{z^3}{2^3}+\cdots$ سے موازنہ کریں۔ $z=\frac12$ پر یہ سلسلہ $1+y$ بنتا ہے۔',r'د $(1-z)^{-1/2}=1+\frac z2+\frac{1\cdot3}{2!}\frac{z^2}{2^2}+\frac{1\cdot3\cdot5}{3!}\frac{z^3}{2^3}+\cdots$ سره پرتله کړئ. په $z=\frac12$ دا لړۍ $1+y$ کېږي.'),
 work(r'1+y=\left(1-\tfrac12\right)^{-1/2}=\sqrt2\Rightarrow y=\sqrt2-1'),work(r'y^2+2y-1=(\sqrt2-1)^2+2(\sqrt2-1)-1=3-2\sqrt2+2\sqrt2-2-1=0')],category='proofs',**PR())
put('7.3',12,'','Proved.',[step(r'The series is the same as in question 11, so $2y=\sqrt2-1$, i.e. $y=\frac{\sqrt2-1}2$.',r'سلسلہ سوال 11 والا ہی ہے، اس لیے $2y=\sqrt2-1$ یعنی $y=\frac{\sqrt2-1}2$۔',r'لړۍ د 11 پوښتنې په څېر ده، نو $2y=\sqrt2-1$ یعنې $y=\frac{\sqrt2-1}2$.'),
 work(r'4y^2+4y-1=(2y)^2+2(2y)-1=(\sqrt2-1)^2+2(\sqrt2-1)-1=0')],category='proofs',**PR())
nn=S.symbols('nn',positive=True)
lhs=ser((1+x)**(1/nn),x,3)
rhs=ser((2*nn+(nn+1)*x)/(2*nn+(nn-1)*x),x,3)
assert S.simplify(lhs-rhs)==0
put('7.3',13,'','Proved.',[step(r'Expand the left side: $(1+x)^{1/n}\approx1+\frac xn+\frac{1}{2}\cdot\frac1n\left(\frac1n-1\right)x^2$.',r'بائیں طرف کو پھیلائیں: $(1+x)^{1/n}\approx1+\frac xn+\frac{1}{2}\cdot\frac1n\left(\frac1n-1\right)x^2$۔',r'کیڼه خوا پراخه کړئ: $(1+x)^{1/n}\approx1+\frac xn+\frac{1}{2}\cdot\frac1n\left(\frac1n-1\right)x^2$.'),
 step(r'Expand the right side: $\left[1+\frac{(n+1)x}{2n}\right]\left[1+\frac{(n-1)x}{2n}\right]^{-1}\approx1+\frac xn+\frac{(1-n)x^2}{2n^2}$.',r'دایاں طرف پھیلائیں: $\left[1+\frac{(n+1)x}{2n}\right]\left[1+\frac{(n-1)x}{2n}\right]^{-1}\approx1+\frac xn+\frac{(1-n)x^2}{2n^2}$۔',r'ښي خوا پراخه کړئ: $\left[1+\frac{(n+1)x}{2n}\right]\left[1+\frac{(n-1)x}{2n}\right]^{-1}\approx1+\frac xn+\frac{(1-n)x^2}{2n^2}$.'),
 step(r'Both give $1+\frac xn-\frac{(n-1)x^2}{2n^2}$ up to $x^2$, so $\sqrt[n]{1+x}\approx\frac{2n+(n+1)x}{2n+(n-1)x}$.',r'دونوں $x^2$ تک $1+\frac xn-\frac{(n-1)x^2}{2n^2}$ دیتے ہیں، لہٰذا $\sqrt[n]{1+x}\approx\frac{2n+(n+1)x}{2n+(n-1)x}$۔',r'دواړه تر $x^2$ پورې $1+\frac xn-\frac{(n-1)x^2}{2n^2}$ ورکوي، نو $\sqrt[n]{1+x}\approx\frac{2n+(n+1)x}{2n+(n-1)x}$.')],category='proofs',**PR())
h,pp,qq=S.symbols('h pp qq')
assert S.simplify(S.series((1+h)**pp*pp-qq*(1+h)**qq,h,0,2).removeO()-((pp-qq)+(pp**2-qq**2)*h))==0
put('7.3',14,'','Proved.',[step(r'Put $x=1+h$ with $h$ so small that $h^2$ may be neglected: $x^m=(1+h)^m\approx1+mh$.',r'$x=1+h$ رکھیں جہاں $h$ اتنا چھوٹا ہے کہ $h^2$ نظر انداز ہو سکے: $x^m=(1+h)^m\approx1+mh$۔',r'$x=1+h$ کېږدئ چېرته چې $h$ دومره وړوکی دی چې $h^2$ هیر شي: $x^m=(1+h)^m\approx1+mh$.'),
 work(r'px^p-qx^q\approx p(1+ph)-q(1+qh)=(p-q)+(p^2-q^2)h=(p-q)\left[1+(p+q)h\right]\approx(p-q)(1+h)^{p+q}=(p-q)x^{p+q}')],category='proofs',**PR())
mcm=lambda p,c,w:MC('Review 7',1,p,c,w,put)
assert C(4,2)*2**2*5**2==600 and C(7,3)*(-2)**3==-280
mcm('(i)','(a) $600x^2y^2$',r'T_3=\binom42(2x)^2(5y)^2=6\cdot4\cdot25\,x^2y^2=600x^2y^2')
mcm('(ii)',r'(b) $-280$',r'(x^3)^{7-r}(-2y^2)^r:\ x^{21-3r}y^{2r}=x^{12}y^6\Rightarrow r=3;\ \binom73(-2)^3=35\cdot(-8)=-280')
mcm('(iii)','(a) 5',r'\text{The odd powers of }\sqrt{x^2-1}\text{ cancel, leaving only even powers; the highest power of }x\text{ is }x^5\ (\text{degree }5)')
mcm('(iv)','(a) 6',r'\text{Even powers of }\sqrt y\text{ survive: }r=0,2,4,6,8,10\Rightarrow6\text{ terms}')
assert S.expand((S.sqrt(2)+1)**5+(S.sqrt(2)-1)**5)==58*S.sqrt(2)
mcm('(v)',r'(b) $58\sqrt2$',r'2\left[(\sqrt2)^5+10(\sqrt2)^3+5\sqrt2\right]=2[4\sqrt2+20\sqrt2+5\sqrt2]=58\sqrt2')
mcm('(vi)',r'(c) $2^{n-1}-1$',r'\sum_{r=0}^{n-1}\binom{n-1}r=2^{n-1};\ \text{removing }r=0\text{ (value 1) gives }2^{n-1}-1')
mcm('(vii)',r'(d) $2^{28}$',r'(1+x)^{29}\text{ has 30 coefficients, symmetric about the middle; the last 15 sum to }\frac{2^{29}}2=2^{28}')
assert sum(C(10,r) for r in (1,3,5,7,9))==512
mcm('(viii)','(a) 512',r'\text{Sum of odd-order coefficients}=2^{10-1}=512')
assert C(8,4)*2**4*3**4==90720
put('Review 7',2,'',r'$90720x^{12}y^4$',[step('For $n=8$ the middle term is $T_5$.','$n=8$ کے لیے درمیانی رکن $T_5$ ہے۔','د $n=8$ لپاره منځنی حد $T_5$ دی.'),work(r'T_5=\binom84(2x^3)^4(3y)^4=70\cdot16\cdot81\,x^{12}y^4=90720x^{12}y^4')])
assert C(7,3)*2**4*(-4)**3==-35840
put('Review 7',3,'','$-35840$',[step('The fourth term is $T_4$ (use $r=3$).','چوتھا رکن $T_4$ ہے ($r=3$ لیں)۔','څلورم حد $T_4$ دی ($r=3$ واخلئ).'),work(r'T_4=\binom73(2x)^4(-4y)^3=35\cdot16\cdot(-64)\,x^4y^3=-35840\,x^4y^3')])
put('Review 7',4,'','$a=4$',[step(r'The term containing $y^3$ has $r=3$.',r'$y^3$ والا رکن $r=3$ پر ہے۔',r'د $y^3$ لرونکی حد په $r=3$ دی.'),work(r'T_4=\binom43(ax)(2y)^3=32a\,xy^3=2^7xy^3\Rightarrow32a=128\Rightarrow a=4')])
assert C(10,5)==252
put('Review 7',5,'','$252$',[tr,work(r'T_{r+1}=\binom{10}r\left(\frac2{x^2}\right)^{10-r}\left(\frac{x^2}2\right)^r\propto x^{4r-20}:\ r=5'),work(r'T_6=\binom{10}5\cdot2^5\cdot2^{-5}=252'),step('The printed key lists 840 for this item; with the expression as printed the constant term is 252.','اس سوال کے لیے مطبوعہ کنجی میں 840 درج ہے؛ جیسا سوال چھپا ہے اس کے مطابق مستقل رکن 252 ہے۔','د دې پوښتنې لپاره په چاپ شوې کیلي کې 840 لیکل شوی؛ لکه چې پوښتنه چاپ شوې، ثابت حد 252 دی.')])
assert round(float(1-R(5,100)+C(5,2)*R(1,10000)),4)==0.951
put('Review 7',6,'','$0.951$',[bs,work(r'(0.99)^5=(1-0.01)^5\approx1-5(0.01)+10(0.01)^2=1-0.05+0.001=0.951')])
assert all((7**m-3**m)%4==0 for m in range(1,30))
proved('Review 7',7,'',[BASIS(r'n=1:\ 7-3=4'),HYP(r'7^k-3^k=4m'),NEXT(r'7^{k+1}-3^{k+1}=7\cdot7^k-3\cdot3^k=7\left(7^k-3^k\right)+4\cdot3^k=28m+4\cdot3^k=4\left(7m+3^k\right)'),CONC])
proved('Review 7',8,'',[step(r'For $x>-1$ and $n=1$: $(1+x)^1=1+x$, so the statement holds.',r'$x>-1$ اور $n=1$ کے لیے $(1+x)^1=1+x$، لہٰذا بیان درست ہے۔',r'د $x>-1$ او $n=1$ لپاره $(1+x)^1=1+x$، نو بیان سم دی.'),HYP(r'(1+x)^k\ge1+kx'),
 NEXT(r'(1+x)^{k+1}=(1+x)(1+x)^k\ge(1+x)(1+kx)=1+(k+1)x+kx^2\ge1+(k+1)x'),
 step(r'We used $1+x>0$ (to keep the inequality direction) and $kx^2\ge0$.',r'ہم نے $1+x>0$ (تاکہ عدم مساوات کا رخ نہ بدلے) اور $kx^2\ge0$ استعمال کیا۔',r'موږ $1+x>0$ (ترڅو د نابرابرۍ لوری ونه بدلېږي) او $kx^2\ge0$ وکارول.'),CONC])
flush()
A.save(['7.1','7.2','7.3','Review 7'],list(range(205,231)))
