from math11_answer_authoring import Author,step,S
R=S.Rational
A=Author(4)
def work(tex):return step('Substitute and simplify.','قیمتیں رکھ کر مختصر کریں۔','ارزښتونه کېږدئ او ساده یې کړئ.',tex)
ap=step('Use the arithmetic term and sum formulas.','حسابی رکن اور مجموعے کے کلیے استعمال کریں۔','د حسابي حد او مجموعې فورمولونه وکاروئ.',r'a_n=a_1+(n-1)d,\quad S_n=\frac n2(a_1+a_n)=\frac n2[2a_1+(n-1)d]')
gp=step('Use the geometric term formula with its constant ratio.','مستقل نسبت کے ساتھ ہندسی رکن کا کلیہ استعمال کریں۔','د ثابت نسبت سره د هندسي حد فورمول وکاروئ.',r'a_n=a_1r^{n-1}')
def put(ex,q,p,ans,ss,**kw):A.put(ex,str(q),p,ans,ss,**kw)
for p,a,d,n in [('(i)',9,-2,20),('(ii)',3,-R(1,3),11)]:
    last=a+(n-1)*d;total=R(n,2)*(a+last);assert sum(a+j*d for j in range(n))==total
    put('4.3',1,p,'$a_{'+str(n)+'}='+S.latex(last)+r',\quad S_{'+str(n)+'}='+S.latex(total)+'$',[ap,work('a_{'+str(n)+'}='+S.latex(S.Integer(a))+'+('+str(n)+'-1)('+S.latex(S.sympify(d))+')='+S.latex(last)+r',\quad S_{'+str(n)+'}='+str(n)+r'\frac{'+S.latex(a+last)+r'}2='+S.latex(total))])
for p,ans,tex in [
('(i)',r'a_{17}=50,\quad S_{17}=442',r'a_{17}=2+16(3)=50,\quad S_{17}=\frac{17}2(2+50)=442'),
('(ii)',r'n=21,\quad a_{21}=60,\quad d=5',r'210=\frac{21}2(-40+a_{21})\Rightarrow a_{21}=60,\quad d=\frac{60+40}{20}=5'),
('(iii)',r'n=9,\quad a_9=57',r'225=\frac n2[-14+8(n-1)]\Rightarrow4n^2-11n-225=0\Rightarrow(n-9)(4n+25)=0,\quad n=9,\ a_9=-7+8(8)=57'),
('(iv)',r'n=15,\quad a_1=0,\quad d=\frac27',r'30=\frac{15}2(a_1+4)\Rightarrow a_1=0,\quad d=\frac{4-0}{14}=\frac27')]:
    put('4.3',2,p,'$'+ans+'$',[ap,work(tex)])
assert sum(range(25,351,5))==12375
put('4.3',3,'','$12375$',[ap,work(r'n=\frac{350-25}5+1=66,\quad S=\frac{66}2(25+350)=12375')])
assert sum(v**3 for v in [8,12,16])==6336
put('4.3',4,'','8,12,16, or the reverse order.',[
step('Use three equally spaced numbers centred at a.','a کے گرد تین مساوی فاصلے والے اعداد لیں۔','د a شاوخوا درې په برابر واټن عددونه واخلئ.',r'(a-d)+a+(a+d)=36\Rightarrow a=12'),
work(r'(a-d)^3+a^3+(a+d)^3=3a^3+6ad^2=6336\Rightarrow5184+72d^2=6336\Rightarrow d=\pm4')],
answerUr='8,12,16 یا معکوس ترتیب۔',answerPs='8,12,16 یا سرچپه ترتیب.')
assert sum(v*v for v in [2,4,6,8])==120
put('4.3',5,'','2,4,6,8, or the reverse order.',[
step('Use the suggested symmetric terms; their common difference is 2d.','تجویز کردہ متناسب ارکان لیں؛ ان کا مشترک فرق 2d ہے۔','وړاندیز شوي متقارن حدونه واخلئ؛ ګډ توپیر یې 2d دی.',r'4a=20\Rightarrow a=5,\quad4a^2+20d^2=120\Rightarrow d=\pm1')],
answerUr='2,4,6,8 یا معکوس ترتیب۔',answerPs='2,4,6,8 یا سرچپه ترتیب.')
put('4.3',6,'','$-21$',[ap,work(r'3a+15d=-6,\quad3a+20d=-11\Rightarrow5d=-5\Rightarrow d=-1,\ a=3'),work(r'x_3+x_8+x_{22}=3a+(2+7+21)d=9-30=-21')])
n,j=S.symbols('n j',integer=True,positive=True)
assert S.simplify(S.summation(6*j-7,(j,1,n))-n*(3*n-4))==0
put('4.3',7,'','$n(3n-4)$',[step('Group each consecutive three terms. The jth group is (6j−5)+(6j−3)−(6j−1)=6j−7.','ہر تین مسلسل ارکان کا گروہ بنائیں۔ jواں گروہ (6j−5)+(6j−3)−(6j−1)=6j−7 ہے۔','هر درې پرله پسې حدونه ډله کړئ. jمه ډله (6j−5)+(6j−3)−(6j−1)=6j−7 ده.',r'S=\sum_{j=1}^n(6j-7)=6\frac{n(n+1)}2-7n=n(3n-4)')])
put('4.3',8,'','$n^2$',[ap,work(r'1+3+\cdots+(2n-1)=\frac n2[1+(2n-1)]=n^2')])
assert sum(range(306,694,9))==21978
put('4.3',9,'','$21978$',[ap,work(r'9(34)=306,\quad9(77)=693,\quad n=77-34+1=44,\quad S=\frac{44}2(306+693)=21978')])
put('4.3',10,'','Rs. 280, 260, 240, 220.',[ap,work(r'1000=\frac42[2a+3(-20)]\Rightarrow a=280')],answerUr='280، 260، 240، 220 روپے۔',answerPs='280، 260، 240، 220 روپۍ.')
put('4.3',11,'','576 feet.',[ap,work(r'S_6=\frac62[2(16)+5(32)]=576')],answerUr='576 فٹ۔',answerPs='576 فټه.')
put('4.3',12,'','Rs. 465.',[ap,work(r'S_{30}=\frac{30}2(1+30)=465')],answerUr='465 روپے۔',answerPs='465 روپۍ.')
put('4.3',13,'','3140 seats.',[ap,work(r'S_{40}=\frac{40}2[2(20)+39(3)]=3140')],answerUr='3140 نشستیں۔',answerPs='3140 څوکۍ.')
put('4.3',14,'',r'16 means: $1+\frac{49j}{17},\ j=1,\ldots,16$.',[ap,step('Include both endpoints in the resulting series, so n terms contain n−2 inserted means.','حاصل سلسلے میں دونوں سرے شامل ہیں، اس لیے n ارکان میں n−2 داخل شدہ اوسط ہیں۔','په لاسته راغلې لړۍ کې دواړه پایونه شامل دي، نو n حدونه n−2 ورګډ شوي منځني لري.',r'459=\frac n2(1+50)\Rightarrow n=18,\quad m=16,\quad d=\frac{49}{17}')],answerUr=r'16 اوسط: $1+\frac{49j}{17},\ j=1,\ldots,16$۔',answerPs=r'16 منځني: $1+\frac{49j}{17},\ j=1,\ldots,16$.')
A.save(['4.3'],[135])
A=Author(4)
x,y=S.symbols('x y',nonzero=True)
seqs=[(5,3),(8,-R(1,2)),(-R(9,16),-R(2,3)),(x/y,-y/x)]
lines=[]
for i,(a,r) in enumerate(seqs,1):
    row=[S.simplify(a*r**j) for j in range(5)]
    assert all(S.simplify(row[j+1]-r*row[j])==0 for j in range(4))
    lines.append('('+str(i)+r')\quad '+r',\ '.join(map(S.latex,row)))
tex=r'\begin{aligned}'+r'\\'.join(lines)+r'\end{aligned}'
put('4.4',1,'','$'+tex+'$',[gp,step('Multiply by r four times after the first term. In (iv), x and y must be nonzero.','پہلے رکن کے بعد چار بار r سے ضرب دیں۔ (iv) میں x اور y غیر صفر ہوں۔','له لومړي حد وروسته څلور ځله په r ضرب کړئ. په (iv) کې x او y باید ناصفر وي.',tex)])
put('4.4',2,'',r'$a_1=3,\quad r=\pm3$',[gp,work(r'a_1r^2=27,\quad a_1r^4=243\Rightarrow r^2=9,\quad r=\pm3,\quad a_1=27/9=3')])
put('4.4',3,'',r'$-\frac{\sqrt2}4$',[gp,work(r'r=\frac{-\sqrt2}2,\quad a_7=a_2r^5=2\left(-\frac{\sqrt2}2\right)^5=-\frac{\sqrt2}4')])
put('4.4',4,'','$11$',[gp,work(r'\frac1{64}=16\left(\frac12\right)^{n-1}\Rightarrow2^{-6}=2^{5-n}\Rightarrow n=11')])
put('4.4',5,'',r'$x=13;\quad20,10,5$',[work(r'(x-3)^2=(x+7)(x-8)\Rightarrow x^2-6x+9=x^2-x-56\Rightarrow x=13,\quad r=\frac12')])
put('4.4',6,'','$ln=m^2$',[gp,work(r'l=a_1r^9,\quad m=a_1r^{12},\quad n=a_1r^{15}\Rightarrow ln=a_1^2r^{24}=m^2')])
put('4.4',7,'',r'Common ratio $1/r$.',[step('Nonzero terms have reciprocals; the ratio of consecutive reciprocals is constant.','غیر صفر ارکان کے مقلوب موجود ہیں؛ مسلسل مقلوبوں کی نسبت مستقل ہے۔','ناصفر حدونه مقلوبونه لري؛ د پرله پسې مقلوبونو نسبت ثابت دی.',r'\frac{1/a_{n+1}}{1/a_n}=\frac{a_n}{a_{n+1}}=\frac1r')],answerUr=r'مشترک نسبت $1/r$۔',answerPs=r'ګډ نسبت $1/r$.')
gm=step('An inserted geometric middle term satisfies G²=ab, so retain both algebraic signs. For positive numbers, the conventional geometric mean is the positive root.','داخل شدہ ہندسی درمیانی رکن G²=ab پورا کرتا ہے، اس لیے دونوں الجبری علامتیں رکھیں۔ مثبت اعداد کا روایتی ہندسی اوسط مثبت جذر ہے۔','ورګډ شوی هندسي منځنی حد G²=ab پوره کوي، نو دواړه الجبري نښې وساتئ. د مثبتو عددونو دودیز هندسي منځنی مثبت جذر دی.',r'G^2=ab')
put('4.4',8,'',r'$(i)\ \pm\sqrt{8.5094};\ (ii)\ \pm36;\ (iii)\ \pm\sqrt{x^2-y^2};\ (iv)\ \pm i\sqrt7$.',[gm,
work(r'3.14(2.71)=8.5094,\quad(-6)(-216)=1296,\quad(x+y)(x-y)=x^2-y^2,\quad(\sqrt2+3)(\sqrt2-3)=-7'),
step('In (iii) a real middle term requires x²≥y²; nonzero endpoints are required for a nonzero-ratio G.P. In (iv) there is no real geometric mean; the displayed roots are complex.','(iii) میں حقیقی درمیانی رکن کے لیے x²≥y² ضروری ہے؛ غیر صفر نسبت والے ہندسی تواتر کے لیے سرے غیر صفر ہوں۔ (iv) میں حقیقی ہندسی اوسط نہیں؛ دکھائے گئے جذر مختلط ہیں۔','په (iii) کې حقیقي منځنی حد x²≥y² غواړي؛ د ناصفر نسبت هندسي ترتیب لپاره پایونه ناصفر وي. په (iv) کې حقیقي هندسي منځنی نشته؛ ښودل شوي جذرونه مختلط دي.')])
assert R(32,9)*R(3,2)**6==R(81,2) and 14*(-R(1,2))**7==-R(7,64)
put('4.4',9,'',r'$(i)\ \frac{16}3,8,12,18,27\ \text{or}\ -\frac{16}3,8,-12,18,-27;\quad(ii)\ -7,\frac72,-\frac74,\frac78,-\frac7{16},\frac7{32}$',[
gp,step('For m inserted means use b=arᵐ⁺¹ and include all real ratios.','m داخل شدہ اوسطوں کے لیے b=arᵐ⁺¹ استعمال کریں اور تمام حقیقی نسبتیں شامل کریں۔','د m ورګډ شوو منځنیو لپاره b=arᵐ⁺¹ وکاروئ او ټول حقیقي نسبتونه شامل کړئ.',r'(i)\ r^6=\frac{81/2}{32/9}=\frac{729}{64}\Rightarrow r=\pm\frac32;\qquad(ii)\ r^7=\frac{-7/64}{14}=-\frac1{128}\Rightarrow r=-\frac12')])
put('4.4',10,'','$49,1$',[step('For positive numbers write them as A+24 and A−24, where A is their arithmetic mean. Take the conventional nonnegative geometric mean G.','مثبت اعداد کو A+24 اور A−24 لکھیں، جہاں A حسابی اوسط ہے۔ روایتی غیر منفی ہندسی اوسط G لیں۔','مثبت عددونه A+24 او A−24 ولیکئ، چې A حسابي منځنی دی. دودیز نامنفي هندسي منځنی G واخلئ.',r'G=A-18,\quad G^2=A^2-24^2\Rightarrow(A-18)^2=A^2-576\Rightarrow A=25,\ G=7')])
put('4.4',11,'',r'$\prod_{j=1}^nG_j=(\sqrt{ab})^n$ for positive means.',[
step('Assume positive endpoints and positive inserted means, so r>0. Multiply the terms and use b=arⁿ⁺¹.','مثبت سرے اور مثبت داخل شدہ اوسط فرض کریں، اس لیے r>0۔ ارکان ضرب دیں اور b=arⁿ⁺¹ استعمال کریں۔','مثبت پایونه او مثبت ورګډ شوي منځني فرض کړئ، نو r>0 دی. حدونه ضرب او b=arⁿ⁺¹ وکاروئ.',r'\prod_{j=1}^n ar^j=a^nr^{n(n+1)/2}=(a^2r^{n+1})^{n/2}=(ab)^{n/2}=(\sqrt{ab})^n'),
step('If negative-ratio branches are allowed, the sign of the single geometric mean must be chosen consistently. The claim with a fixed positive square root is not universal: between 1 and 4, the inserted mean −2 has product −2, not 2.','اگر منفی نسبت والی شاخیں جائز ہوں تو واحد ہندسی اوسط کی علامت مناسب منتخب کرنا ضروری ہے۔ مقرر مثبت جذر کے ساتھ دعویٰ عمومی نہیں: 1 اور 4 کے درمیان داخل شدہ اوسط −2 کا حاصل ضرب −2 ہے، 2 نہیں۔','که د منفي نسبت څانګې اجازه ولري، د یوازیني هندسي منځني نښه باید سمه وټاکل شي. له ثابت مثبت جذر سره ادعا عمومي نه ده: د 1 او 4 ترمنځ ورګډ شوی منځنی −2 حاصل ضرب −2 لري، نه 2.')],
answerUr=r'مثبت اوسطوں کے لیے $\prod_{j=1}^nG_j=(\sqrt{ab})^n$۔',answerPs=r'د مثبتو منځنیو لپاره $\prod_{j=1}^nG_j=(\sqrt{ab})^n$.')
put('4.4',12,'',r'$n=-\frac12$ for distinct positive $a,b$.',[
step('For a,b>0 set a=x² and b=y² with x,y>0. Multiply by the denominator and factor.','a,b>0 کے لیے a=x² اور b=y² لیں جہاں x,y>0۔ مخرج سے ضرب دے کر اجزائے ضربی بنائیں۔','د a,b>0 لپاره a=x² او b=y² ونیسئ چې x,y>0 وي. په مخرج ضرب او تجزیه وکړئ.',r'x^{2n+2}+y^{2n+2}=xy(x^{2n}+y^{2n})\iff(x-y)(x^{2n+1}-y^{2n+1})=0'),
step('Distinct positive x,y imply 2n+1=0. If a=b, every defined exponent works.','مختلف مثبت x,y سے 2n+1=0 ملتا ہے۔ اگر a=b تو ہر معین قوت درست ہے۔','بېل مثبت x,y د 2n+1=0 پایله ورکوي. که a=b وي، هر تعریف شوی توان سم دی.',r'\frac{a^{1/2}+b^{1/2}}{a^{-1/2}+b^{-1/2}}=\sqrt{ab}')],
answerUr=r'مختلف مثبت $a,b$ کے لیے $n=-\frac12$۔',answerPs=r'د بېلو مثبتو $a,b$ لپاره $n=-\frac12$.')
A.save(['4.4'],[140,141])
