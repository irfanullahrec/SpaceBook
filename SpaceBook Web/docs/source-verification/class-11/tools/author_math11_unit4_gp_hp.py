from math11_answer_authoring import Author,step,S
R=S.Rational
A=Author(4)
def work(tex):return step('Substitute and simplify.','قیمتیں رکھ کر مختصر کریں۔','ارزښتونه کېږدئ او ساده یې کړئ.',tex)
ap=step('Use the arithmetic term and sum formulas.','حسابی رکن اور مجموعے کے کلیے استعمال کریں۔','د حسابي حد او مجموعې فورمولونه وکاروئ.',r'a_n=a_1+(n-1)d,\quad S_n=\frac n2[2a_1+(n-1)d]')
gp=step('Use the geometric term and sum formulas.','ہندسی رکن اور مجموعے کے کلیے استعمال کریں۔','د هندسي حد او مجموعې فورمولونه وکاروئ.',r'a_n=a_1r^{n-1},\quad S_n=\frac{a_1(1-r^n)}{1-r}\ (r\ne1),\quad S_\infty=\frac{a_1}{1-r}\ (|r|<1)')
hp=step('Take reciprocals: the reciprocals of an H.P. form an A.P.','مقلوب لیں: ہارمونک ترقی کے مقلوب حسابی ترقی بناتے ہیں۔','معکوسونه واخلئ: د هارمونیک پرمختګ معکوسونه حسابي پرمختګ جوړوي.',r'\frac1{h_n}=\frac1{h_1}+(n-1)d')
def put(ex,q,p,ans,ss,**kw):A.put(ex,str(q),p,ans,ss,**kw)
# ---- 4.5
n=S.Symbol('n')
s1=3*(2**10-1);assert s1==sum(3*2**k for k in range(10))
s2=R(255,16);assert s2==sum(8*R(1,2)**k for k in range(8)) and 8*R(1,2)**7==R(1,16)
s3=16*(2**7-1);assert s3==sum(2**k for k in range(4,11))
s4=R(8,5)/(1+R(5,8));s5=2/(1-1/S.sqrt(2));s5=S.radsimp(s5)
s6=R(1,3)*(1-R(-3,2)**7)/(1+R(3,2))
assert s4==R(64,65) and S.simplify(s5-(4+2*S.sqrt(2)))==0
put('4.5',1,'',r'$\text{(i) }3069;\ \text{(ii) }\frac{255}{16};\ \text{(iii) }2032;\ \text{(iv) }\frac{64}{65};\ \text{(v) }4+2\sqrt2;\ \text{(vi) }'+S.latex(s6)+'$',[gp,
work(r'\text{(i) }a=3,r=2,n=10:\ S=3(2^{10}-1)=3069'),
work(r'\text{(ii) }r=\frac12,\ \frac1{16}=8\left(\frac12\right)^{n-1}\Rightarrow n=8:\ S=\frac{8(1-2^{-8})}{1/2}=\frac{255}{16}'),
work(r'\text{(iii) }a=2^4,r=2,n=7:\ S=16(2^7-1)=2032'),
step('In (iv) and (v) the list continues without end and |r|<1, so the infinite sum is used.','(iv) اور (v) میں فہرست بلا انتہا جاری ہے اور |r|<1 ہے، اس لیے لامحدود مجموعہ استعمال ہوا۔','په (iv) او (v) کې لړۍ بې پایه ده او |r|<1 دی، نو بې پایه مجموعه کارول شوې.',r'\text{(iv) }r=-\frac58:\ \frac{8/5}{1+5/8}=\frac{64}{65};\quad\text{(v) }r=\frac1{\sqrt2}:\ \frac{2}{1-1/\sqrt2}=4+2\sqrt2'),
work(r'\text{(vi) }a=\frac13,r=-\frac32,n=7:\ S_7=\frac13\cdot\frac{1-(-3/2)^7}{1+3/2}='+S.latex(s6))])
put('4.5',2,'',r'$\text{(i) }n=7,S_n=43;\ \text{(ii) }a_1=256,S_9=511;\ \text{(iii) }a_1=3,n=6$',[gp,
work(r'\text{(i) }(-2)^{n-1}=64=(-2)^6\Rightarrow n=7,\ S_7=\frac{1-(-2)^7}{1+2}=43'),
work(r'\text{(ii) }a_9=a_1\left(\frac12\right)^8=1\Rightarrow a_1=256,\ S_9=\frac{256(1-2^{-9})}{1/2}=511'),
work(r'\text{(iii) }S_n=\frac{a_1-ra_n}{1-r}=\frac{a_1-192}{3}=-63\Rightarrow a_1=3;\ 3(-2)^{n-1}=-96\Rightarrow(-2)^{n-1}=-32\Rightarrow n=6')])
put('4.5',3,'',r'$4,2,1,\frac12,\frac14;\quad S_\infty=8$',[gp,work(r'r=\frac{a_3}{a_2}=\frac12,\ a_1=\frac{a_2}r=4,\quad S_\infty=\frac{4}{1-1/2}=8')])
put('4.5',4,'',r'$\text{(i) }\frac89;\ \text{(ii) }\frac{18}{11};\ \text{(iii) }\frac{97}{45};\ \text{(iv) }\frac{41}{333}$',[step('Write the repeating part as an infinite geometric series and use S=a/(1−r).','دہرائے جانے والے حصے کو لامحدود ہندسی سلسلے کے طور پر لکھیں اور S=a/(1−r) استعمال کریں۔','تکراري برخه د بې پایه هندسي لړۍ په توګه ولیکئ او S=a/(1−r) وکاروئ.'),
work(r'\text{(i) }\frac{0.8}{1-0.1}=\frac89;\quad\text{(ii) }1+\frac{0.63}{1-0.01}=1+\frac7{11}=\frac{18}{11}'),
work(r'\text{(iii) }2.1+\frac{0.05}{1-0.1}=\frac{21}{10}+\frac1{18}=\frac{97}{45};\quad\text{(iv) }\frac{0.123}{1-0.001}=\frac{123}{999}=\frac{41}{333}')])
put('4.5',5,'',r'$r=3$',[gp,work(r'S_{10}=S_5(1+r^5)\Rightarrow1+r^5=244\Rightarrow r^5=243\Rightarrow r=3')],answerUr='$r=3$',answerPs='$r=3$')
put('4.5',6,'','Proved.',[step('Let k=a/(1−r) and x=rⁿ (r≠1). Then Sₙ=k(1−x), S₂ₙ=k(1−x²), S₃ₙ=k(1−x³).','k=a/(1−r) اور x=rⁿ (r≠1) لیں۔ تب Sₙ=k(1−x)، S₂ₙ=k(1−x²)، S₃ₙ=k(1−x³)۔','k=a/(1−r) او x=rⁿ (r≠1) واخلئ. نو Sₙ=k(1−x)، S₂ₙ=k(1−x²)، S₃ₙ=k(1−x³).'),
work(r'S_n(S_{3n}-S_{2n})=k(1-x)\cdot kx^2(1-x)=k^2x^2(1-x)^2'),
work(r'(S_n-S_{2n})^2=[k(x^2-x)]^2=k^2x^2(1-x)^2\quad\text{so both sides are equal.}')],answerUr='ثابت ہوا۔',answerPs='ثابت شو.')
put('4.5',7,'',r'$S_n=1-\left(\frac12\right)^n$',[gp,work(r'a_1=\frac12,\ r=\frac12:\ S_n=\frac{\frac12(1-2^{-n})}{1/2}=1-2^{-n}')])
put('4.5',8,'',r'$8,12,18\ \text{(or }18,12,8)$',[step('Take the three numbers as a/r, a, ar.','تین اعداد کو a/r، a، ar لیں۔','درې عددونه a/r، a، ar واخلئ.'),
work(r'a^3=1728\Rightarrow a=12;\quad12\left(\frac1r+1+r\right)=38\Rightarrow6r^2-13r+6=0\Rightarrow r=\frac32\text{ or }\frac23')],answerUr='$8,12,18$ (یا $18,12,8$)',answerPs='$8,12,18$ (یا $18,12,8$)')
put('4.5',9,'',r'$r=2$',[gp,work(r'S_6=S_3(1+r^3)=9S_3\Rightarrow r^3=8\Rightarrow r=2')])
put('4.5',10,'','$n=7$',[gp,work(r'r=\sqrt3:\ \frac{(\sqrt3)^n-1}{\sqrt3-1}=40+13\sqrt3\Rightarrow(\sqrt3)^n=(40+13\sqrt3)(\sqrt3-1)+1=27\sqrt3=(\sqrt3)^7\Rightarrow n=7')])
put('4.5',11,'','Proved.',[step('Let the G.P. have first term A and common ratio R, so a=AR^{p-1}, b=AR^{q-1}, c=AR^{r-1}.','فرض کریں پہلا رکن A اور نسبت R ہے، تب a=AR^{p-1}, b=AR^{q-1}, c=AR^{r-1}۔','فرض کړئ لومړی حد A او نسبت R دی، نو a=AR^{p-1}, b=AR^{q-1}, c=AR^{r-1}.'),
work(r'a^{q-r}b^{r-p}c^{p-q}=A^{(q-r)+(r-p)+(p-q)}R^{(p-1)(q-r)+(q-1)(r-p)+(r-1)(p-q)}=A^0R^0=1')],answerUr='ثابت ہوا۔',answerPs='ثابت شو.')
put('4.5',12,'',r'$\frac{24}5+\frac{24}{25}+\frac{24}{125}+\cdots$',[gp,work(r'a_1=4\cdot\frac{a_1r}{1-r}\Rightarrow1-r=4r\Rightarrow r=\frac15;\quad\frac{a_1}{1-1/5}=6\Rightarrow a_1=\frac{24}5')])
put('4.5',13,'','Proved.',[step('The series is geometric with first term x/3 and ratio x/3, and |x/3|<1 because 0<x<3.','یہ سلسلہ ہندسی ہے جس کا پہلا رکن x/3 اور نسبت x/3 ہے، اور 0<x<3 ہونے سے |x/3|<1 ہے۔','دا لړۍ هندسي ده، لومړی حد x/3 او نسبت x/3 دی، او 0<x<3 له امله |x/3|<1 دی.'),
work(r'y=\frac{x/3}{1-x/3}=\frac x{3-x}\Rightarrow3y-xy=x\Rightarrow x=\frac{3y}{1+y}')],answerUr='ثابت ہوا۔',answerPs='ثابت شو.')
dist=10+2*sum(R(10)/2**k for k in range(1,8));assert dist==R(955,32)
put('4.5',14,'',r'$\frac{955}{32}=29.84375\ \text{ft}$',[step('Interpretation: the distance is measured until the ball strikes the ground for the eighth time. It falls 10 ft, then rises and falls 5, 5/2, … for seven rebounds.','مفہوم: فاصلہ اس وقت تک ناپا جاتا ہے جب گیند آٹھویں بار زمین سے ٹکراتی ہے۔ یہ پہلے 10 فٹ گرتی ہے، پھر سات اچھالوں میں بالترتیب 5، 5/2، … اوپر جاتی اور نیچے آتی ہے۔','مطلب: واټن تر هغه مهاله اندازه کېږي چې بال اتمه ځل ځمکې ته ورسېږي. لومړی 10 فوټه لوېږي، بیا په اوو اچولو کې 5، 5/2، … پورته او ښکته ځي.'),
work(r'10+2\left(5+\frac52+\cdots+\frac{10}{2^7}\right)=10+2\cdot\frac{5\left(1-2^{-7}\right)}{1/2}=10+\frac{635}{32}=\frac{955}{32}')],answerUr=r'$\frac{955}{32}=29.84375$ فٹ',answerPs=r'$\frac{955}{32}=29.84375$ فوټه')
put('4.5',15,'',r'$\text{Rs. }16384;\ \text{total }\text{Rs. }1073741823$',[gp,work(r'a_{15}=2^{14}=16384;\quad S_{30}=\frac{1(2^{30}-1)}{2-1}=1073741823')],answerUr=r'$16384$ روپے؛ کل $1073741823$ روپے',answerPs=r'$16384$ روپۍ؛ ټوله $1073741823$ روپۍ')
put('4.5',16,'','$50\\%$ per day',[gp,work(r'64000r^6=729000\Rightarrow r^6=\frac{729}{64}=\left(\frac32\right)^6\Rightarrow r=\frac32,\ \text{increase}=\frac12=50\%')],answerUr='$50\\%$ روزانہ',answerPs='$50\\%$ هره ورځ')
# ---- 4.6
put('4.6',1,'',r'$\text{(i) }\frac1{26};\ \text{(ii) }\frac2{13};\ \text{(iii) }1$',[hp,
work(r'\text{(i) }2,5,8:\ d=3,\ 2+8(3)=26\Rightarrow\frac1{26}'),
work(r'\text{(ii) }\frac16,\frac12,\frac56:\ d=\frac13,\ \frac16+19\cdot\frac13=\frac{13}2\Rightarrow\frac2{13}'),
work(r'\text{(iii) }\frac{17}3,\frac{17}5,\frac{17}7\to\frac3{17},\frac5{17},\frac7{17}:\ d=\frac2{17},\ \frac3{17}+7\cdot\frac2{17}=1\Rightarrow1')])
put('4.6',2,'',r'$-\frac13,-\frac15,-\frac17,-\frac19,-\frac1{11}$',[hp,work(r'3,1,-1:\ d=-2;\ \text{next: }-3,-5,-7,-9,-11')])
put('4.6',3,'',r'$-\frac1{18}$',[hp,work(r'a+d=2,\ a+4d=-4\Rightarrow d=-2,\ a=4;\quad\frac1{h_{12}}=4+11(-2)=-18')])
put('4.6',4,'',r'$\text{(i) }A=2.925,\ G=\pm\sqrt{8.5094},\ H=\frac{17.0188}{5.85};\ \text{(ii) }A=-111,\ G=\pm36,\ H=-\frac{432}{37};\ \text{(iii) }A=x,\ G=\pm\sqrt{x^2-y^2},\ H=\frac{x^2-y^2}x$',[step('Use A=(a+b)/2, G=±√(ab) and H=2ab/(a+b). Then A·H=ab=G².','A=(a+b)/2، G=±√(ab) اور H=2ab/(a+b) استعمال کریں۔ پھر A·H=ab=G² ہے۔','A=(a+b)/2، G=±√(ab) او H=2ab/(a+b) وکاروئ. نو A·H=ab=G² دی.'),
work(r'\text{(i) }ab=8.5094,\ a+b=5.85,\ H=\frac{17.0188}{5.85}\approx2.9092;\ A\cdot H=8.5094=G^2'),
work(r'\text{(ii) }ab=1296,\ a+b=-222,\ H=\frac{2592}{-222}=-\frac{432}{37};\ A\cdot H=(-111)\left(-\frac{432}{37}\right)=1296=G^2'),
work(r'\text{(iii) }ab=x^2-y^2,\ a+b=2x,\ H=\frac{2(x^2-y^2)}{2x};\ A\cdot H=x^2-y^2=G^2\quad(x\ne0)')])
put('4.6',5,'',r'$n=-1$',[step('Equate the expression to 2ab/(a+b) with a≠b, a,b>0.','عبارت کو 2ab/(a+b) کے برابر رکھیں، جہاں a≠b اور a,b>0 ہوں۔','عبارت د 2ab/(a+b) سره برابر کړئ، چېرته چې a≠b او a,b>0 وي.'),
work(r'(a+b)(a^{n+1}+b^{n+1})=2ab(a^n+b^n)\Rightarrow(a-b)(a^{n+1}-b^{n+1})=0\Rightarrow a^{n+1}=b^{n+1}\Rightarrow n+1=0'),
step('Check: n=−1 gives 2/(1/a+1/b)=2ab/(a+b).','تصدیق: n=−1 سے 2/(1/a+1/b)=2ab/(a+b) ملتا ہے۔','تصدیق: n=−1 له 2/(1/a+1/b)=2ab/(a+b) ورکوي.')])
put('4.6',6,'','$16,\\ 24$',[hp,work(r'\frac1{12},\ ?,\ ?,\ \frac1{48}:\ d=\frac{1/48-1/12}3=-\frac1{48};\ \frac1{16},\frac1{24}\Rightarrow16,24')])
put('4.6',7,'',r'$\frac{35}{23},\frac{35}{31},\frac{35}{39},\frac{35}{47}$',[hp,work(r'\frac37\text{ and }\frac{11}7:\ d=\frac{8/7}5=\frac8{35};\ \frac{23}{35},\frac{31}{35},\frac{39}{35},\frac{47}{35}')])
put('4.6',8,'','Proved.',[step('For numbers a and b, A=(a+b)/2 and H=2ab/(a+b), while G²=ab.','اعداد a اور b کے لیے A=(a+b)/2، H=2ab/(a+b) اور G²=ab ہے۔','د a او b لپاره A=(a+b)/2، H=2ab/(a+b) او G²=ab دی.'),
work(r'A\cdot H=\frac{a+b}2\cdot\frac{2ab}{a+b}=ab=G^2')],answerUr='ثابت ہوا۔',answerPs='ثابت شو.')
put('4.6',9,'','$4\\text{ and }12$',[step('Use G²=AH, a+b=2A and ab=G².','G²=AH، a+b=2A اور ab=G² استعمال کریں۔','G²=AH، a+b=2A او ab=G² وکاروئ.'),
work(r'G^2=8\cdot6=48,\ a+b=16\Rightarrow t^2-16t+48=0\Rightarrow t=4,12')],answerUr='$4$ اور $12$',answerPs='$4$ او $12$')
put('4.6',10,'','$3\\text{ and }12$',[step('Use G²=ab and H=2ab/(a+b).','G²=ab اور H=2ab/(a+b) استعمال کریں۔','G²=ab او H=2ab/(a+b) وکاروئ.'),
work(r'ab=36,\ \frac{2(36)}{a+b}=\frac{24}5\Rightarrow a+b=15\Rightarrow t^2-15t+36=0\Rightarrow t=3,12')],answerUr='$3$ اور $12$',answerPs='$3$ او $12$')
# ---- Review 4
mc=lambda p,ans,w,ur=None:put('Review 4',1,p,ans,[step('Work out the result and compare it with the printed options.','نتیجہ نکال کر مطبوعہ اختیارات سے موازنہ کریں۔','پایله ومومئ او له چاپ شوو انتخابونو سره یې پرتله کړئ.',w)],category='mcqs',answerUr=ur or ans,answerPs=ur or ans)
t=[1+5*j for j in range(100)];u=[4+j for j in range(100)];assert sum(t)+sum(u)==30200
mc('(i)','(c) 30,200',r'\text{Odd places }1,6,11,\ldots:\ 50(2+99\cdot5)=24850;\ \text{even places }4,5,6,\ldots:\ 50(8+99)=5350;\ \text{total }30200')
assert S.solve(3*n**2+n-120200,n)[1]==200
mc('(ii)','(b) 200',r'\frac n2[4+3(n-1)]=60100\Rightarrow3n^2+n-120200=0\Rightarrow n=200')
mc('(iii)','(a) $a^2,b^2,c^2$ are in G.P.',r'b=ar,\ c=ar^2\Rightarrow a^2,a^2r^2,a^2r^4\text{ has ratio }r^2',ur='(a) $a^2,b^2,c^2$ ہندسی ترقی میں ہیں۔')
mc('(iv)','(b) 4',r'a_{n+1}-a_n=4(n+1)+1-4n-1=4')
mc('(v)','(d) 8, 16, 24, 32,…',r'\frac{16}8=2\ne\frac{24}{16}=\frac32',ur='(d) $8,16,24,32,\\ldots$')
mc('(vi)','(d) $-2,-6,-10,-14$',r'd=\frac{-18-2}5=-4:\ 2,-2,-6,-10,-14,-18')
mc('(vii)','(b) $G^2=AH$',r'AH=\frac{a+b}2\cdot\frac{2ab}{a+b}=ab=G^2')
assert R(81,2)*(1-R(1,3**7))==R(1093,27)
mc('(viii)','(b) 7',r'r=\frac13:\ \frac{27(1-3^{-n})}{2/3}=\frac{1093}{27}\Rightarrow3^{-n}=\frac1{2187}\Rightarrow n=7')
assert [x for x in S.solve(12*n**2+17*n-5,n)]==[R(-5,3),R(1,4)]
mc('(ix)','(b) $\\frac14$',r'\left(\frac52+2p\right)^2=\left(\frac{15}4+p\right)(2+p)\Rightarrow12p^2+17p-5=0\Rightarrow p=\frac14\ (p>0)')
mc('(x)','(d) $4/11$',r'5,\frac{19}4,\frac92,\frac{17}4:\ d=-\frac14,\ \frac1{h_{10}}=5-\frac94=\frac{11}4\Rightarrow h_{10}=\frac4{11}')
mc('(xi)','(c) $7/24$',r'r^4=\frac{1/48}{1/3}=\frac1{16}\Rightarrow r=\frac12:\ \frac16+\frac1{12}+\frac1{24}=\frac7{24}')
put('Review 4',2,'',r'$a_n=9-n;\ 8,7,6,5,\ldots;\ a_{10}=-1;\ S_n=\frac{n(17-n)}2,\ S_{10}=35$',[ap,work(r'a_n=8+(n-1)(-1)=9-n;\ a_{10}=-1;\ S_n=\frac n2[16-(n-1)]=\frac{n(17-n)}2;\ S_{10}=35')])
put('Review 4',3,'','$n=18\\text{ or }19$',[ap,work(r'\frac n2[108-3(n-1)]=513\Rightarrow n^2-37n+342=0\Rightarrow n=18\text{ or }19'),step('Both values give 513 because the 19th term is 0.','دونوں قیمتیں 513 دیتی ہیں کیونکہ 19واں رکن 0 ہے۔','دواړه ارزښتونه 513 ورکوي ځکه چې ۱۹ م حد 0 دی.')],answerUr='$n=18$ یا $19$',answerPs='$n=18$ یا $19$')
put('Review 4',4,'',r'$5,11,17,\ldots;\ a_n=6n-1$',[step('a₁=S₁ and aₙ=Sₙ−Sₙ₋₁.','a₁=S₁ اور aₙ=Sₙ−Sₙ₋₁۔','a₁=S₁ او aₙ=Sₙ−Sₙ₋₁.'),work(r'a_1=5;\ a_n=[2n+3n^2]-[2(n-1)+3(n-1)^2]=6n-1')])
assert sum(range(252,1000,3))==156375
put('Review 4',5,'','$156375$',[ap,work(r'a_1=252,\ a_n=999,\ n=\frac{999-252}3+1=250;\ S=125(252+999)=156375')])
put('Review 4',6,'',r'$\frac53$',[gp,work(r'a_1=1,\ r=\frac25:\ S_\infty=\frac1{1-2/5}=\frac53')])
put('Review 4',7,'','Proved.',[step('Use the A.P. condition a+c=2b, and write y=xr, z=xr² for the G.P.','حسابی ترقی کی شرط a+c=2b استعمال کریں اور y=xr، z=xr² لکھیں۔','د حسابي پرمختګ شرط a+c=2b وکاروئ او y=xr، z=xr² ولیکئ.'),
work(r'x^by^cz^a=x^{a+b+c}r^{c+2a},\quad x^cy^az^b=x^{a+b+c}r^{a+2b};\quad c+2a=a+2b\Leftrightarrow a+c=2b')],answerUr='ثابت ہوا۔',answerPs='ثابت شو.')
put('Review 4',8,'','$18$',[work(r'\frac{10\frac12+25\frac12}2=\frac{36}2=18')])
put('Review 4',9,'',r'$2,6,18\ \text{(or }18,6,2)$',[step('Take a/r, a, ar.','a/r، a، ar لیں۔','a/r، a، ar واخلئ.'),work(r'a^3=216\Rightarrow a=6;\ 6\left(\frac1r+1+r\right)=26\Rightarrow3r^2-10r+3=0\Rightarrow r=3\text{ or }\frac13')],answerUr='$2,6,18$ (یا $18,6,2$)',answerPs='$2,6,18$ (یا $18,6,2$)')
put('Review 4',10,'','$25$',[ap,work(r'a=15,d=2:\ \frac n2[30+2(n-1)]=n(n+14)=975\Rightarrow n^2+14n-975=0\Rightarrow n=25')])
put('Review 4',11,'',r'$193.75\ \text{ft}$',[step('Interpretation: the 100 ft is the rise in the first minute; each later minute is half the previous one.','مفہوم: 100 فٹ پہلے منٹ کی بلندی ہے؛ بعد کے ہر منٹ میں پچھلے سے آدھی بلندی ہوتی ہے۔','مطلب: 100 فوټه د لومړي دقیقې پورته والی دی؛ هره راتلونکې دقیقه د مخکنۍ نیمایي ده.'),
gp,work(r'a_1=100,\ r=\frac12,\ n=5:\ S_5=\frac{100(1-2^{-5})}{1/2}=193.75')],answerUr='$193.75$ فٹ',answerPs='$193.75$ فوټه')
A.save(['4.5','4.6','Review 4'],[144,145,146,147,148,149])
