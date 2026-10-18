import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from math11_answer_authoring import Author,step,S
from math11_phrases import *
R=S.Rational
A=Author(8)
put,flush=make_put(A)
x,h,y,a,b,c=S.symbols('x h y a b c')
# --------------------------------------------------------------- 8.1
f=x**2+x-1
assert [f.subs(x,v) for v in (-2,0,2,5)]==[1,-1,5,29]
assert sorted(S.solve(f-5,x))==[-3,2]
assert S.expand(f.subs(x,x+1))==x**2+3*x+1
assert S.simplify(S.expand((f.subs(x,x+h)-f)/h))==2*x+h+1
put('8.1',1,'(i)',r'$f(-2)=1,\ f(0)=-1,\ f(2)=5,\ f(5)=29$',[work(r'f(-2)=4-2-1=1,\ f(0)=-1,\ f(2)=4+2-1=5,\ f(5)=25+5-1=29')])
put('8.1',1,'(ii)',r'$x=2$ or $x=-3$',[work(r'x^2+x-1=5\Rightarrow x^2+x-6=0\Rightarrow(x+3)(x-2)=0')],answerUr='$x=2$ یا $x=-3$',answerPs='$x=2$ یا $x=-3$')
put('8.1',1,'(iii)',r'$x^2+3x+1$',[work(r'f(x+1)=(x+1)^2+(x+1)-1=x^2+2x+1+x+1-1=x^2+3x+1')])
put('8.1',1,'(iv)',r'$2x+h+1$',[work(r'\frac{f(x+h)-f(x)}h=\frac{(x+h)^2+(x+h)-x^2-x}h=\frac{2xh+h^2+h}h=2x+h+1')])
fq={'f':7*x-2,'g':2*x/(x**2-4),'h':4*S.sqrt(25-x**2),'k':x**2+1}
assert fq['f'].subs(x,6)==40 and fq['g'].subs(x,-1)==R(2,3) and fq['h'].subs(x,4)==12 and fq['k'].subs(x,R(1,2))==R(5,4)
put('8.1',2,'(i)',r'$f(6)=40,\ g(-1)=\frac23,\ h(4)=12,\ k\left(\frac12\right)=\frac54$',[work(r'f(6)=7(6)-2=40;\ g(-1)=\frac{-2}{1-4}=\frac23;\ h(4)=4\sqrt{25-16}=12;\ k\left(\tfrac12\right)=\tfrac14+1=\tfrac54')])
assert S.simplify((fq['f']-fq['f'].subs(x,2))/(x-2))==7
put('8.1',2,'(ii)','$7$',[work(r'\frac{f(x)-f(2)}{x-2}=\frac{(7x-2)-12}{x-2}=\frac{7(x-2)}{x-2}=7\quad(x\ne2)')])
put('8.1',3,'(i)',r'$x=\frac15$',[work(r'15x-3=0\Rightarrow x=\tfrac15')])
put('8.1',3,'(ii)',r'$x=3,\ 5$',[work(r'x^2-8x+15=(x-3)(x-5)=0')])
put('8.1',3,'(iii)',r'$x=0,\ \pm1$',[work(r'x^3-x=x(x-1)(x+1)=0')])
put('8.1',3,'(iv)',r'$x=1,\ \pm\sqrt5$',[work(r'x^3-x^2-5x+5=x^2(x-1)-5(x-1)=(x-1)(x^2-5)=0')])
put('8.1',4,'(i)',r'Domain $=R$; Range $=\left[-\frac65,\infty\right)$',[work(r'5x^2+2x-1=5\left(x+\tfrac15\right)^2-\tfrac65\ge-\tfrac65'),step('The printed key lists the range as $R$; a quadratic with positive leading coefficient has a least value, so the range is $[-6/5,\\infty)$.','مطبوعہ کنجی میں حد $R$ لکھی ہے؛ مثبت سربراہ عددی سر والے دو درجی کی کم از کم قیمت ہوتی ہے، اس لیے حد $[-6/5,\\infty)$ ہے۔','په چاپ شوې کیلي کې رینج $R$ لیکل شوی؛ د مثبت مخکني ضریب لرونکې دوه درجه یي تابع لږ تر لږه ارزښت لري، نو رینج $[-6/5,\\infty)$ دی.')],answerUr=r'دائرۂ کار $=R$؛ حد $=\left[-\frac65,\infty\right)$',answerPs=r'ډومېن $=R$؛ رینج $=\left[-\frac65,\infty\right)$')
put('8.1',4,'(ii)',r'Domain $=R-(-4,4)$; Range $=[0,\infty)$',[work(r'x^2-16\ge0\Rightarrow|x|\ge4;\quad\sqrt{x^2-16}\ge0\text{ and takes every value }\ge0')],answerUr=r'دائرۂ کار $=R-(-4,4)$؛ حد $=[0,\infty)$',answerPs=r'ډومېن $=R-(-4,4)$؛ رینج $=[0,\infty)$')
inv=step('Put $y=f(x)$, solve for $x$, then interchange $x$ and $y$.','$y=f(x)$ رکھیں، $x$ کے لیے حل کریں، پھر $x$ اور $y$ کو آپس میں بدل دیں۔','$y=f(x)$ کېږدئ، د $x$ لپاره حل کړئ، بیا $x$ او $y$ سره بدل کړئ.')
put('8.1',5,'(i)',r'$f^{-1}(x)=\dfrac{x+3}2$',[inv,work(r'y=2x-3\Rightarrow x=\frac{y+3}2')])
put('8.1',5,'(ii)',r'$f^{-1}(x)=3x+15$',[inv,work(r'y=\tfrac13x-5\Rightarrow x=3(y+5)=3y+15')])
put('8.1',5,'(iii)',r'$f^{-1}(x)=2-5x$',[inv,work(r'y=\frac{2-x}5\Rightarrow x=2-5y')])
put('8.1',5,'(iv)',r'$f^{-1}(x)=\dfrac12(x-4)^2,\ x\ge4$',[inv,work(r'y=4+\sqrt{2x}\Rightarrow(y-4)^2=2x\Rightarrow x=\tfrac12(y-4)^2,\ y\ge4')])
put('8.1',6,'(i)',r'$f^{-1}(x)=\sqrt[3]{x+2}$',[inv,work(r'y=x^3-2\Rightarrow x=\sqrt[3]{y+2}')])
put('8.1',6,'(ii)',r'$\sqrt[3]5$',[work(r'f^{-1}(3)=\sqrt[3]{3+2}=\sqrt[3]5')])
put('8.1',7,'(i)',r'Domain $f=R-\{3\}$, Range $f=R-\{1\}$',[work(r'x-3\ne0\Rightarrow x\ne3;\quad y=\frac{x-4}{x-3}=1-\frac1{x-3}\ne1')])
put('8.1',7,'(ii)',r'$f^{-1}(x)=\dfrac{3x-4}{x-1}$; Domain $f^{-1}=R-\{1\}$, Range $f^{-1}=R-\{3\}$',[inv,work(r'y(x-3)=x-4\Rightarrow x(y-1)=3y-4\Rightarrow x=\frac{3y-4}{y-1}'),work(r'\text{Domain}(f^{-1})=\text{Range}(f)=R-\{1\},\quad\text{Range}(f^{-1})=\text{Domain}(f)=R-\{3\}')])
# --------------------------------------------------------------- 8.2 (graphs)
pl=step('Plot the points and join them with a smooth line/curve.','نقاط لگائیں اور انہیں ہموار لکیر/منحنی سے ملائیں۔','ټکي ټاکئ او په نرمې کرښې/منحني یې سره یو کړئ.')
put('8.2',1,'(i)',r'A straight line with slope $2$, $y$-intercept $3$ and $x$-intercept $-\frac32$.',[work(r'x=0\Rightarrow y=3;\quad y=0\Rightarrow x=-\tfrac32;\quad x=1\Rightarrow y=5'),pl])
put('8.2',1,'(ii)',r'A straight line with slope $4$, $y$-intercept $-5$ and $x$-intercept $\frac54$.',[work(r'x=0\Rightarrow y=-5;\quad y=0\Rightarrow x=\tfrac54;\quad x=2\Rightarrow y=3'),pl])
put('8.2',2,'(i)',r'Parabola opening upward, vertex $(0,1)$, axis $x=0$, no $x$-intercept.',[work(r'f(x)=x^2+1\ge1;\ \text{table: }x=-2,-1,0,1,2\Rightarrow y=5,2,1,2,5'),pl])
put('8.2',2,'(ii)',r'Parabola opening downward, vertex $(0,1)$, $x$-intercepts $\pm1$.',[work(r'f(x)=1-x^2;\ \text{table: }x=-2,-1,0,1,2\Rightarrow y=-3,0,1,0,-3'),pl])
put('8.2',2,'(iii)',r'Parabola opening upward, vertex $(-1,0)$ on the $x$-axis, $y$-intercept $1$.',[work(r'f(x)=(x+1)^2;\ \text{table: }x=-3,-2,-1,0,1\Rightarrow y=4,1,0,1,4'),pl])
q3=[('(i)',r'$f(x)=\frac34x^2$: vertex $(0,0)$; $y$-intercept $0$; $x$-intercept $0$; axis $x=0$; opens upward',r'f(x)=\tfrac34x^2:\ \text{vertex }(0,0),\ a=\tfrac34>0'),
('(ii)',r'$f(x)=-2x^2+8$: vertex $(0,8)$; $y$-intercept $8$; $x$-intercepts $\pm2$; axis $x=0$; opens downward',r'-2x^2+8=0\Rightarrow x=\pm2;\ a=-2<0'),
('(iii)',r'$f(x)=-x^2+6x-5$: vertex $(3,4)$; $y$-intercept $-5$; $x$-intercepts $1,5$; axis $x=3$; opens downward',r'-x^2+6x-5=-(x-3)^2+4;\ -(x-1)(x-5)=0;\ a=-1<0'),
('(iv)',r'$f(x)=x^2+2x-3$: vertex $(-1,-4)$; $y$-intercept $-3$; $x$-intercepts $-3,1$; axis $x=-1$; opens upward',r'x^2+2x-3=(x+1)^2-4=(x+3)(x-1);\ a=1>0')]
for p,ans,w in q3:
    put('8.2',3,p,ans,[step(r'Complete the square: vertex $\left(-\frac b{2a},f\left(-\frac b{2a}\right)\right)$; $y$-intercept $f(0)$; $x$-intercepts from $f(x)=0$; opens up if $a>0$.',r'مربع مکمل کریں: راس $\left(-\frac b{2a},f\left(-\frac b{2a}\right)\right)$؛ $y$-قطع $f(0)$؛ $x$-قطع $f(x)=0$ سے؛ $a>0$ ہو تو اوپر کی طرف کھلتا ہے۔',r'مربع بشپړ کړئ: راس $\left(-\frac b{2a},f\left(-\frac b{2a}\right)\right)$؛ $y$-قطع $f(0)$؛ $x$-قطعونه د $f(x)=0$ نه؛ که $a>0$ وي پورته خلاصېږي.',w)])
A.answers if False else None
put('8.2',4,'(i)','(e)',[note('Vertex $(2,0)$: a parabola opening upward touching the $x$-axis at $x=2$ (matched with the printed graphs as in the textbook key).','راس $(2,0)$: اوپر کھلنے والی مکافی جو $x=2$ پر $x$-محور کو چھوتی ہے (مطبوعہ گرافوں کے ساتھ جیسا کتاب کی کنجی میں ہے)۔','راس $(2,0)$: پورته خلاصه پارابولا چې په $x=2$ د $x$-محور لمس کوي (له چاپ شوو ګرافونو سره لکه د کتاب په کیلي کې).')],answerUr='(e)',answerPs='(e)')
for p,ans,desc in [('(ii)','(c)',r'Vertex $(-4,0)$, opens upward.'),('(iii)','(b)',r'Vertex $(0,-2)$, opens upward.'),('(iv)','(a)',r'Vertex $(-1,-2)$, opens upward.'),('(v)','(f)',r'Vertex $(2,4)$, opens downward.'),('(vi)','(d)',r'Vertex $(4,0)$, opens downward.')]:
    put('8.2',4,p,ans,[note('Read the vertex and direction from the equation, then pick the matching graph (as in the textbook key): '+desc,'مساوات سے راس اور رخ پڑھیں، پھر موزوں گراف چنیں (جیسا کتاب کی کنجی میں ہے): '+desc,'له معادلې نه راس او لوری ولولئ، بیا برابر ګراف وټاکئ (لکه د کتاب په کیلي کې): '+desc)],answerUr=ans,answerPs=ans)
# --------------------------------------------------------------- 8.3
put('8.3',1,'(i)',r'Upward parabola, $x$-intercepts $1,3$, vertex $(2,-1)$, $y$-intercept $3$.',[work(r'f(x)=(x-1)(x-3)=x^2-4x+3=(x-2)^2-1'),pl])
put('8.3',1,'(ii)',r'Downward parabola, $x$-intercepts $\pm1$, vertex $(0,2)$, $y$-intercept $2$.',[work(r'f(x)=-2(x+1)(x-1)=-2x^2+2'),pl])
put('8.3',2,'(i)',r'Upward parabola, $x$-intercepts $-1,3$, vertex $(1,-4)$, $y$-intercept $-3$.',[work(r'x^2-2x-3=(x-3)(x+1)=(x-1)^2-4'),pl])
put('8.3',2,'(ii)',r'Downward parabola, $x$-intercepts $-1,2$, vertex $\left(\frac12,\frac94\right)$, $y$-intercept $2$.',[work(r'-(x^2-x-2)=-(x-2)(x+1)=-\left(x-\tfrac12\right)^2+\tfrac94'),pl])
assert S.expand((x-3)*(x-4))==x**2-7*x+12
put('8.3',3,'',r'$y=x^2-7x+12$',[step('Use the intercept form $y=(x-p)(x-q)$ with $p=3$, $q=4$.','قطع کی صورت $y=(x-p)(x-q)$ لیں جہاں $p=3$، $q=4$۔','د قطع بڼه $y=(x-p)(x-q)$ واخلئ چېرته چې $p=3$، $q=4$.'),work(r'y=(x-3)(x-4)=x^2-7x+12')])
e41=S.expand(-R(1,2)*(x+5)*(x-3));e42=S.expand(-R(1,6)*(x+7)*(x-10))
assert e41.subs(x,-1)==8 and e42.subs(x,4)==11
put('8.3',4,'(i)',r'$y=-\dfrac12x^2-x+\dfrac{15}2$',[work(r'y=a(x+5)(x-3);\ (-1,8):\ a(4)(-4)=8\Rightarrow a=-\tfrac12'),work(r'y=-\tfrac12(x^2+2x-15)=-\tfrac12x^2-x+\tfrac{15}2')])
put('8.3',4,'(ii)',r'$y=-\dfrac16x^2+\dfrac12x+\dfrac{35}3$',[work(r'y=a(x+7)(x-10);\ (4,11):\ a(11)(-6)=11\Rightarrow a=-\tfrac16'),work(r'y=-\tfrac16(x^2-3x-70)=-\tfrac16x^2+\tfrac12x+\tfrac{35}3')])
put('8.3',5,'(i)',r'$x$-axis at $(3,0)$; $y$-axis at $(0,-3)$',[work(r'y=0\Rightarrow x=3;\quad x=0\Rightarrow y=-3')])
put('8.3',5,'(ii)',r'$x$-axis at $\left(-\frac12,0\right)$; $y$-axis at $(0,1)$',[work(r'y=0\Rightarrow x=-\tfrac12;\quad x=0\Rightarrow y=1')])
put('8.3',6,'(i)',r'$\left(\frac13,\frac53\right)$',[work(r'-x+2=2x+1\Rightarrow x=\tfrac13,\ y=2-\tfrac13=\tfrac53')])
put('8.3',6,'(ii)',r'$(2,4)$',[work(r'3x-2=-x+6\Rightarrow x=2,\ y=4')])
put('8.3',7,'(i)',r'$(1,3)$ and $(-2,0)$',[work(r'-x^2+4=x+2\Rightarrow x^2+x-2=0\Rightarrow(x+2)(x-1)=0;\ y=x+2:\ (1,3),(-2,0)')])
put('8.3',7,'(ii)',r'$(-1,-3)$ and $(-2,-1)$',[work(r'x^2+x-3=-2x-5\Rightarrow x^2+3x+2=0\Rightarrow(x+1)(x+2)=0;\ y=-2x-5:\ (-1,-3),(-2,-1)')])
put('8.3',8,'',r'$(2,-2)$',[work(r'2x-y=6,\ 3x+y=4\Rightarrow5x=10\Rightarrow x=2,\ y=-2')])
put('8.3',9,'',r'Air speed $=5$ km/min, wind velocity $=1$ km/min',[step('Let air speed $a$ and wind speed $w$. Against the wind: $a-w=\\frac{24}6=4$. With the wind: $a+w=\\frac{24}4=6$.','ہوائی رفتار $a$ اور ہوا کی رفتار $w$ لیں۔ ہوا کے خلاف: $a-w=\\frac{24}6=4$۔ ہوا کے ساتھ: $a+w=\\frac{24}4=6$۔','د هوايي چټکتیا $a$ او د باد چټکتیا $w$ واخلئ. د باد په مخالف: $a-w=\\frac{24}6=4$. د باد سره: $a+w=\\frac{24}4=6$.'),work(r'a=\frac{4+6}2=5,\quad w=\frac{6-4}2=1')])
# --------------------------------------------------------------- Review 8
mc=lambda p,c,w:MC('Review 8',1,p,c,w,put)
mc('(i)',r'(d) $(-2,2]$',r'\frac{2-x}{x+2}\ge0\text{ and }x\ne-2\Rightarrow-2<x\le2')
mc('(ii)','(b) Only onto function',r'f(-1)=f(1)=1\text{ (not one-one)};\ \{1,0,1,4\}=B\text{ (onto)}')
mc('(iii)',r'(c) $\left\{1,2,\frac43,\frac73\right\}$',r'f^{-1}(y)=\frac{y+5}3:\ y=-1,-2,1,2\Rightarrow\frac43,1,2,\frac73')
assert S.expand((2*x+3)**2+6)==4*x**2+12*x+15
mc('(iv)',r'(b) $9x^2+12x+10$',r'f(2x+3)=(2x+3)^2+6\Rightarrow f(t)=t^2+6;\ f(3x+2)=(3x+2)^2+6=9x^2+12x+10')
mc('(v)','(a) 0',r'f(x)+f(1/x)=x^3-\frac1{x^3}+\frac1{x^3}-x^3=0')
fx=lambda t:t**2-3*t+4
assert sorted(S.solve(fx(x)-fx(2*x+1),x))==[-1,R(2,3)]
mc('(vi)',r'(b) $\frac23$',r'x^2-3x+4=(2x+1)^2-3(2x+1)+4\Rightarrow3x^2+x-2=0\Rightarrow x=\tfrac23\text{ or }-1;\ \text{of the options, }\tfrac23')
mc('(vii)',r'(d) $(-\infty,1)\cup(2,\infty)$',r'x^2-3x+2=(x-1)(x-2)>0\Rightarrow x<1\text{ or }x>2')
mc('(viii)',r'(c) $g(x)=-x^2-2x+5$',r'\text{The curve opens downward with its vertex above the }x\text{-axis; of (c) and (d) the textbook key gives (c): vertex }(-1,6)')
put('Review 8',2,'',r'Domain $f=\left[-2\sqrt3,-\sqrt3\right]\cup\left[\sqrt3,2\sqrt3\right]$',[work(r'12-x^2\ge0\Rightarrow|x|\le2\sqrt3;\quad3-\sqrt{12-x^2}\ge0\Rightarrow12-x^2\le9\Rightarrow|x|\ge\sqrt3')])
assert S.expand(3*x**2-2*x+5).subs(x,0)==5
put('Review 8',3,'',r'$f(x)=3x^2-2x+5$',[work(r'f(x)=ax^2+bx+c:\ c=5;\ a-b+5=10;\ a+b+5=6\Rightarrow a-b=5,\ a+b=1\Rightarrow a=3,\ b=-2')])
put('Review 8',4,'',r'(i) $[2,\infty)$; (ii) $R$',[work(r'\text{(i) }x^2\ge0\Rightarrow x^2+2\ge2;\quad\text{(ii) }f(x)=x\text{ takes every real value}')])
put('Review 8',5,'',r'(i) $32$; (ii) $82.4$; (iii) $14$; (iv) $c=100$',[work(r't(0)=32;\ t(28)=\tfrac{252}5+32=82.4;\ t(-10)=-18+32=14;\ \tfrac{9c}5+32=212\Rightarrow c=100')])
put('Review 8',6,'',r'(i) $2$; (ii) $\dfrac43$',[work(r'f^{-1}(y)=\frac{y+7}8:\ f^{-1}(9)=2,\ f^{-1}\left(\tfrac{11}3\right)=\tfrac{32/3}8=\tfrac43')])
sol=S.solve([8-4*a+2*b+1+3,-1-a-b+1],[a,b]);assert sol=={a:2,b:-2}
put('Review 8',7,'',r'$a=2,\ b=-2$',[work(r'f(2)=8-4a+2b+1=-3\Rightarrow2a-b=6;\quad f(-1)=-1-a-b+1=0\Rightarrow b=-a'),work(r'3a=6\Rightarrow a=2,\ b=-2'),step('The printed key shows "$b=-2y$", an obvious misprint for $b=-2$.','مطبوعہ کنجی میں "$b=-2y$" چھپا ہے جو $b=-2$ کی واضح چھپائی کی غلطی ہے۔','په چاپ شوې کیلي کې "$b=-2y$" چاپ شوی چې د $b=-2$ څرګنده چاپي تېروتنه ده.')])
put('Review 8',8,'',r'(i) line through $(0,3)$ and $(6,0)$; (ii) parabola opening downward with vertex $(0,0)$ through $(\pm1,-3),(\pm2,-12)$; (iii) parabola opening upward, $x$-intercepts $\frac12,3$, vertex $\left(\frac74,-\frac{25}8\right)$, $y$-intercept $3$',[work(r'\text{(iii) }2x^2-7x+3=(2x-1)(x-3)=2\left(x-\tfrac74\right)^2-\tfrac{25}8'),pl])
put('Review 8',9,'',r'(i) upward parabola, $x$-intercepts $-3,1$, vertex $(-1,-4)$, $y$-intercept $-3$; (ii) upward parabola $y=3x^2-3$, $x$-intercepts $\pm1$, vertex $(0,-3)$',[work(r'\text{(i) }x^2+2x-3=(x+3)(x-1)=(x+1)^2-4;\quad\text{(ii) }3(x+1)(x-1)=3x^2-3'),pl])
put('Review 8',10,'',r'(i) $\left(-\frac13,\frac{11}3\right)$; (ii) $(-1,0)$ (the line touches the parabola)',[work(r'\text{(i) }x+4=-2x+3\Rightarrow x=-\tfrac13,\ y=\tfrac{11}3'),work(r'\text{(ii) }x^2-x-2=-3x-3\Rightarrow(x+1)^2=0\Rightarrow x=-1,\ y=0\ (\text{tangent})')])
flush()
A.save(['8.1','8.2','8.3','Review 8'],list(range(231,260)))
