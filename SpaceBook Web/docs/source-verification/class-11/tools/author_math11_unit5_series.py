from math11_answer_authoring import Author,step,S
R=S.Rational
A=Author(5)
n,x,k=S.symbols('n x k')
def work(tex):return step('Substitute and simplify.','قیمتیں رکھ کر مختصر کریں۔','ارزښتونه کېږدئ او ساده یې کړئ.',tex)
def put(ex,q,p,ans,ss,**kw):A.put(ex,str(q),p,ans,ss,**kw)
def chk(f,t,rng=range(1,9),sub=None):
    for m in rng:
        e=S.nsimplify(f.subs(n,m)) if not sub else f.subs(sub).subs(n,m)
        assert S.simplify(e-sum(t(j) for j in range(1,m+1)))==0,(f,m)
sq=step(r'Use $\sum k=\frac{n(n+1)}2,\ \sum k^2=\frac{n(n+1)(2n+1)}6,\ \sum k^3=\left[\frac{n(n+1)}2\right]^2$.',r'$\sum k=\frac{n(n+1)}2،\ \sum k^2=\frac{n(n+1)(2n+1)}6،\ \sum k^3=\left[\frac{n(n+1)}2\right]^2$ استعمال کریں۔',r'$\sum k=\frac{n(n+1)}2،\ \sum k^2=\frac{n(n+1)(2n+1)}6،\ \sum k^3=\left[\frac{n(n+1)}2\right]^2$ وکاروئ.')
agp=step(r'For terms $[a+(k-1)d]r^{k-1}$ use $S_n=\frac{a-[a+(n-1)d]r^n}{1-r}+\frac{dr(1-r^{n-1})}{(1-r)^2}$ for $r\ne1$.',r'$[a+(k-1)d]r^{k-1}$ والے ارکان کے لیے $r\ne1$ پر $S_n=\frac{a-[a+(n-1)d]r^n}{1-r}+\frac{dr(1-r^{n-1})}{(1-r)^2}$ استعمال کریں۔',r'د $[a+(k-1)d]r^{k-1}$ حدونو لپاره $r\ne1$ کې $S_n=\frac{a-[a+(n-1)d]r^n}{1-r}+\frac{dr(1-r^{n-1})}{(1-r)^2}$ وکاروئ.')
tele=step('Split each term into partial fractions; consecutive terms cancel (telescoping).','ہر رکن کو جزوی کسروں میں توڑیں؛ مسلسل ارکان کٹ جاتے ہیں۔','هر حد په جزوي کسرونو ووېشئ؛ پرله پسې حدونه یو بل لغوه کوي.')
diff=step('Take successive differences until they become constant or a geometric sequence, then build the nth term.','مسلسل فرق لیں جب تک وہ مستقل یا ہندسی ترتیب نہ بن جائیں، پھر عمومی رکن بنائیں۔','پرله پسې توپیرونه واخلئ تر هغې چې ثابت یا هندسي لړۍ شي، بیا عمومي حد جوړ کړئ.')
# ------------------------------------------------ 5.1
f=[n*(2*n-1)*(2*n+1)/3, n*(n+1)**2*(n+2)/12, 2*n*(n+1)*(2*n+1)/3, n**2*(2*n**2-1)]
t=[lambda j:(2*j-1)**2,lambda j:j*(j+1)*(2*j+1)/R(6),lambda j:(2*j)**2,lambda j:(2*j-1)**3]
for a,b in zip(f,t):chk(a,b)
f5=S.expand(S.summation((4*k-3)**3,(k,1,n)));chk(f5,lambda j:(4*j-3)**3)
f5t=S.factor(f5)
put('5.1',1,'',r'$\text{(i) }\frac{n(2n-1)(2n+1)}3;\ \text{(ii) }\frac{n(n+1)^2(n+2)}{12};\ \text{(iii) }\frac{2n(n+1)(2n+1)}3;\ \text{(iv) }n^2(2n^2-1);\ \text{(v) }'+S.latex(f5t)+'$',[sq,
work(r'\text{(i) }\sum(2k-1)^2=\sum(4k^2-4k+1)=\frac{n(4n^2-1)}3'),
work(r'\text{(ii) }t_k=\sum_{j=1}^kj^2=\frac{k(k+1)(2k+1)}6\Rightarrow S_n=\frac{n(n+1)^2(n+2)}{12}'),
work(r'\text{(iii) }\sum(2k)^2=4\cdot\frac{n(n+1)(2n+1)}6=\frac{2n(n+1)(2n+1)}3'),
work(r'\text{(iv) }\sum(2k-1)^3=\sum(8k^3-12k^2+6k-1)=n^2(2n^2-1)'),
work(r'\text{(v) }t_k=(4k-3)^3:\ S_n='+S.latex(f5t))])
assert sum(j*(j+1) for j in range(1,100))==333300
put('5.1',2,'','$333300$',[sq,work(r'\sum_{k=1}^{99}k(k+1)=\frac{99\cdot100\cdot101}3=333300')])
assert sum((2*j-1)**2 for j in range(1,51))==166650
put('5.1',3,'','$166650$',[sq,work(r'99=2(50)-1\Rightarrow n=50:\ \frac{n(2n-1)(2n+1)}3=\frac{50\cdot99\cdot101}3=166650')])
chk(n*(n+1)**2/2,lambda j:j*(3*j+1)/R(2))
put('5.1',4,'',r'$\frac{n(n+1)^2}2$',[sq,work(r'k\text{th term}=\frac k2(3k+1)\Rightarrow S_n=\frac12\left[3\cdot\frac{n(n+1)(2n+1)}6+\frac{n(n+1)}2\right]=\frac{n(n+1)^2}2')])
chk(n*(n+1)*(2*n+1)/6+n,lambda j:j**2+1)
put('5.1',5,'',r'$\frac{n(n+1)(2n+1)}6+n$',[sq,work(r't_k=k^2+1\Rightarrow S_n=\frac{n(n+1)(2n+1)}6+n=\frac{n(2n^2+3n+7)}6')],answerUr=r'$\frac{n(n+1)(2n+1)}6+n$',answerPs=r'$\frac{n(n+1)(2n+1)}6+n$')
chk(n*(n+1)*(n+2)*(n+3)/4,lambda j:j*(j+1)*(j+2))
put('5.1',6,'',r'$\frac{n(n+1)(n+2)(n+3)}4$',[sq,work(r't_k=k(k+1)(k+2)=k^3+3k^2+2k\Rightarrow S_n=\frac{n(n+1)(n+2)(n+3)}4')])
f7=S.factor(S.expand(S.summation(k*(k+4)*(k+8),(k,1,n))));chk(f7,lambda j:j*(j+4)*(j+8))
put('5.1',7,'','$'+S.latex(f7)+'$',[sq,work(r't_k=k(k+4)(k+8)=k^3+12k^2+32k\Rightarrow S_n='+S.latex(f7))])
f8=S.factor(S.expand(S.summation(4*k**2+5*k+1,(k,1,2*n))));chk(f8,lambda j:4*j**2+5*j+1,sub=None) if False else None
assert all(S.simplify(f8.subs(n,m)-sum(4*j**2+5*j+1 for j in range(1,2*m+1)))==0 for m in range(1,7))
put('5.1',8,'','$'+S.latex(f8)+'$',[sq,work(r'S_{2n}=4\cdot\frac{2n(2n+1)(4n+1)}6+5\cdot\frac{2n(2n+1)}2+2n='+S.latex(f8))])
f9a=S.factor(S.summation(k**2*(2*k+3),(k,1,n)));chk(f9a,lambda j:j**2*(2*j+3))
g=lambda m:S.Integer(1)*(3*(4**m+2*m**2)-4*m**3)
f9b=4*(4**n-1)+n*(n+1)*(2*n+1)-n**2*(n+1)**2
assert all(f9b.subs(n,m)==sum(g(j) for j in range(1,m+1)) for m in range(1,8))
put('5.1',9,'',r'$\text{(i) }'+S.latex(f9a)+r';\ \text{(ii) }4(4^n-1)+n(n+1)(2n+1)-n^2(n+1)^2$',[sq,
work(r'\text{(i) }\sum(2k^3+3k^2)=\frac{n^2(n+1)^2}2+\frac{n(n+1)(2n+1)}2='+S.latex(f9a)),
work(r'\text{(ii) }3\sum4^k+6\sum k^2-4\sum k^3=4(4^n-1)+n(n+1)(2n+1)-n^2(n+1)^2')])
# ------------------------------------------------ 5.2
f=(n-1)*2**(n+1)+2;chk(f,lambda j:j*2**j)
def agp_sum(a,d,r,m):return sum((a+(j-1)*d)*r**(j-1) for j in range(1,m+1))
def agp_formula(a,d,r):return (a-(a+(n-1)*d)*r**n)/(1-r)+d*r*(1-r**(n-1))/(1-r)**2
for a,d,r in [(1,3,x),(1,1,x),(1,2,R(1,2)),(1,6,-x)]:
    for m in range(1,7):
        xv=R(2,3)
        assert S.simplify(agp_formula(a,d,r).subs(n,m).subs(x,xv)-agp_sum(a,d,r,m).subs(x,xv))==0
put('5.2',1,'',r'$\text{(i) }(n-1)2^{n+1}+2;\ \text{(ii) }\frac{1-(3n-2)x^n}{1-x}+\frac{3x(1-x^{n-1})}{(1-x)^2};\ \text{(iii) }\frac{1-x^n}{(1-x)^2}-\frac{nx^n}{1-x};\ \text{(iv) }6-\frac{2n+3}{2^{n-1}};\ \text{(v) }\frac{1-(6n-5)(-x)^n}{1+x}-\frac{6x\left(1-(-x)^{n-1}\right)}{(1+x)^2}$',[agp,
work(r'\text{(i) }a=1,d=1,r=2\ (\text{terms }k\cdot2^k=2\cdot k2^{k-1}):\ S=(n-1)2^{n+1}+2'),
work(r'\text{(ii) }a=1,d=3,r=x;\ \text{(iii) }a=1,d=1,r=x;\ \text{(iv) }a=1,d=2,r=\tfrac12;\ \text{(v) }a=1,d=6,r=-x'),
step('The formula needs r≠1; if x=1 in (ii),(iii) the series is an ordinary A.P. and the sums are n(3n−1)/2 and n(n+1)/2, and in (v) x=−1 gives n(3n−2).','فارمولے کے لیے r≠1 ضروری ہے؛ x=1 پر (ii)،(iii) سادہ حسابی ترقی ہیں اور مجموعے n(3n−1)/2 اور n(n+1)/2 ہیں، اور (v) میں x=−1 پر n(3n−2) ملتا ہے۔','فورمول r≠1 غواړي؛ که x=1 وي (ii)،(iii) ساده حسابي پرمختګ دي او مجموعې n(3n−1)/2 او n(n+1)/2 دي، او په (v) کې x=−1 له n(3n−2) ورکوي.')])
put('5.2',2,'',r'$\text{(i) }\frac{1+6x+x^2}{(1-x)^3}\ (|x|<1);\ \text{(ii) }\frac92$',[step('Use the infinite sums of k·yᵏ⁻¹ and k²·yᵏ⁻¹ for |y|<1: Σk y^{k−1}=1/(1−y)² and Σk² y^{k−1}=(1+y)/(1−y)³.','|y|<1 کے لیے k·yᵏ⁻¹ اور k²·yᵏ⁻¹ کے لامحدود مجموعے: Σk y^{k−1}=1/(1−y)² اور Σk² y^{k−1}=(1+y)/(1−y)³۔','د |y|<1 لپاره د k·yᵏ⁻¹ او k²·yᵏ⁻¹ بې پایه مجموعې: Σk y^{k−1}=1/(1−y)² او Σk² y^{k−1}=(1+y)/(1−y)³.'),
work(r'\text{(i) }\sum(2k-1)^2x^{k-1}=4\sum k^2x^{k-1}-4\sum kx^{k-1}+\sum x^{k-1}=\frac{4(1+x)}{(1-x)^3}-\frac4{(1-x)^2}+\frac1{1-x}=\frac{1+6x+x^2}{(1-x)^3}'),
work(r'\text{(ii) }y=\frac13:\ \frac{1+1/3}{(2/3)^3}=\frac{4/3}{8/27}=\frac92')])
put('5.2',3,'',r'$t_n=\frac{n-1}{2^{n-1}}$',[step('The numerators are 0,1,2,3,… and the denominators are 1,2,4,8,….','صورتیں 0,1,2,3,… اور مخرج 1,2,4,8,… ہیں۔','صورتونه 0,1,2,3,… او مخرجونه 1,2,4,8,… دي.'),work(r't_n=\frac{n-1}{2^{n-1}}')])
put('5.2',4,'','$9$',[agp,work(r'\frac{2k+3}{3^{k-1}}:\ a=5,d=2,r=\frac13;\ S_\infty=\frac{a}{1-r}+\frac{dr}{(1-r)^2}=\frac{15}2+\frac32=9')])
put('5.2',5,'',r'$r=\frac14$',[step('For |r|<1 the sum to infinity is a/(1−r)+dr/(1−r)² with a=3, d=2.','|r|<1 پر لامحدود مجموعہ a/(1−r)+dr/(1−r)² ہے، جہاں a=3 اور d=2 ہے۔','د |r|<1 لپاره بې پایه مجموعه a/(1−r)+dr/(1−r)² ده، چې a=3 او d=2 دي.'),
work(r'\frac{3-r}{(1-r)^2}=\frac{44}9\Rightarrow44r^2-79r+17=0\Rightarrow r=\frac14\text{ or }\frac{17}{11}'),
step('Only r=1/4 satisfies |r|<1, so r=1/4.','صرف r=1/4 شرط |r|<1 پوری کرتا ہے، اس لیے r=1/4۔','یوازې r=1/4 شرط |r|<1 پوره کوي، نو r=1/4.')],answerUr=r'$r=\frac14$',answerPs=r'$r=\frac14$')
# ------------------------------------------------ 5.3
def ser(ex,q,tn,Sn,seq,w):
    for j,v in enumerate(seq,1):assert tn.subs(n,j)==v,(q,j)
    chk(Sn,lambda j:tn.subs(n,j))
    put(ex,q,'','$t_n='+S.latex(tn)+r',\quad S_n='+S.latex(Sn)+'$',[diff,work(w)])
ser('5.3',1,3*n**2+1,n*(n+1)*(2*n+1)/2+n,[4,13,28,49,76],r'\Delta:9,15,21,27;\ \Delta^2=6\Rightarrow t_n=3n^2+1,\ S_n=\frac{n(n+1)(2n+1)}2+n')
ser('5.3',2,3*n**2+n,n*(n+1)**2,[4,14,30,52,80,114],r'\Delta:10,16,22,28,34;\ \Delta^2=6\Rightarrow t_n=3n^2+n,\ S_n=\frac{n(n+1)(2n+1)}2+\frac{n(n+1)}2=n(n+1)^2')
ser('5.3',3,n**2+3*n,n*(n+1)*(n+5)/3,[4,10,18,28,40],r'\Delta:6,8,10,12;\ \Delta^2=2\Rightarrow t_n=n^2+3n,\ S_n=\frac{n(n+1)(2n+1)}6+\frac{3n(n+1)}2=\frac{n(n+1)(n+5)}3')
ser('5.3',4,3**(n-1)+2,(3**n-1)/2+2*n,[3,5,11,29,83,245],r'\Delta:2,6,18,54,162\text{ (ratio }3)\Rightarrow t_n=3+(3^{n-1}-1)=3^{n-1}+2,\ S_n=\frac{3^n-1}2+2n')
ser('5.3',5,3*2**n-3,3*2**(n+1)-6-3*n,[3,9,21,45,93,189],r'\Delta:6,12,24,48,96\text{ (ratio }2)\Rightarrow t_n=3+6(2^{n-1}-1)=3\cdot2^n-3,\ S_n=3(2^{n+1}-2)-3n')
ser('5.3',6,5**(n-1)+27,(5**n-1)/4+27*n,[28,32,52,152,652],r'\Delta:4,20,100,500\text{ (ratio }5)\Rightarrow t_n=28+(5^{n-1}-1)=5^{n-1}+27,\ S_n=\frac{5^n-1}4+27n')
# ------------------------------------------------ 5.4
chk(n/(n+1),lambda j:R(1,j*(j+1)))
chk(n/(2*n+1),lambda j:R(1,(2*j-1)*(2*j+1)))
chk(n/(6*n+4),lambda j:R(1,(3*j-1)*(3*j+2)))
chk(n/(4*(3*n+4)),lambda j:R(1,(3*j+1)*(3*j+4)))
put('5.4',1,'',r'$\text{(i) }\frac n{n+1};\ \text{(ii) }\frac n{2n+1};\ \text{(iii) }\frac16;\ \text{(iv) }\frac1{36}$',[tele,
work(r'\text{(i) }\frac1{k(k+1)}=\frac1k-\frac1{k+1}\Rightarrow S_n=1-\frac1{n+1}=\frac n{n+1}'),
work(r'\text{(ii) }\frac1{(2k-1)(2k+1)}=\frac12\left(\frac1{2k-1}-\frac1{2k+1}\right)\Rightarrow S_n=\frac12\left(1-\frac1{2n+1}\right)=\frac n{2n+1}'),
work(r'\text{(iii) }\frac1{(3k-1)(3k+2)}=\frac13\left(\frac1{3k-1}-\frac1{3k+2}\right)\Rightarrow S_\infty=\frac13\cdot\frac12=\frac16'),
work(r'\text{(iv) }\frac1{(9k-5)(9k+4)}=\frac19\left(\frac1{9k-5}-\frac1{9k+4}\right)\Rightarrow S_\infty=\frac19\cdot\frac14=\frac1{36}')])
put('5.4',2,'',r'$\frac n{2(3n+2)}$',[tele,work(r'9k^2+3k-2=(3k-1)(3k+2),\ \frac1{(3k-1)(3k+2)}=\frac13\left(\frac1{3k-1}-\frac1{3k+2}\right)\Rightarrow S_n=\frac13\left(\frac12-\frac1{3n+2}\right)=\frac n{2(3n+2)}')])
assert all(S.Rational(1)-R(1,m)==sum(R(1,j*(j-1)) for j in range(2,m+1)) for m in range(2,9))
put('5.4',3,'',r'$\frac{n-1}n$',[tele,work(r'\frac1{k(k-1)}=\frac1{k-1}-\frac1k\Rightarrow S_n=1-\frac1n=\frac{n-1}n')])
chk(n/(4*(n+4)),lambda j:R(1,(j+3)*(j+4)))
put('5.4',4,'',r'$\frac n{4(n+4)}$',[tele,work(r'k^2+7k+12=(k+3)(k+4),\ \frac1{(k+3)(k+4)}=\frac1{k+3}-\frac1{k+4}\Rightarrow S_n=\frac14-\frac1{n+4}=\frac n{4(n+4)}')])
# ------------------------------------------------ Review 5
mc=lambda p,ans,w,ur=None:put('Review 5',1,p,ans,[step('Work out the result and compare it with the printed options.','نتیجہ نکال کر مطبوعہ اختیارات سے موازنہ کریں۔','پایله ومومئ او له چاپ شوو انتخابونو سره یې پرتله کړئ.',w)],category='mcqs',answerUr=ur or ans,answerPs=ur or ans)
mc('(i)','(b) $6n+11$',r't_{n+1}=6(n+1)+5=6n+11')
mc('(ii)','(c) 3',r'1+\sum_{j\ge1}\frac{4j-2}{3^j}=1+4\cdot\frac34-2\cdot\frac12=3')
mc('(iii)',r'(c) $99\cdot2^{100}+1$',r'\sum_{k=1}^nk2^{k-1}=(n-1)2^n+1,\ n=100\Rightarrow99\cdot2^{100}+1')
mc('(iv)','(b) $(n^2+n)$',r't_n=n(n+1)=n^2+n')
mc('(v)','(c) $n+2(2^n-1)$',r'\sum_{k=1}^n(1+2^k)=n+(2^{n+1}-2)=n+2(2^n-1)')
assert sum(3+2**r for r in range(1,11))==2076
mc('(vi)','(c) 2076',r'30+(2^{11}-2)=30+2046=2076')
mc('(vii)','(a) $\frac{n+1}2$',r't_n=\frac{1+2+\cdots+n}n=\frac{n(n+1)/2}n=\frac{n+1}2')
mc('(viii)','(a) $n^2(2n^2-1)$',r'\sum_{k=1}^n(2k-1)^3=n^2(2n^2-1)')
put('Review 5',2,'',r'$\frac{n(n+1)(n+2)}3$',[sq,work(r'\sum k(k+1)=\frac{n(n+1)(2n+1)}6+\frac{n(n+1)}2=\frac{n(n+1)(n+2)}3')])
f3=S.factor(S.summation(k*(k+2)*(k+4),(k,1,n)));chk(f3,lambda j:j*(j+2)*(j+4))
put('Review 5',3,'','$'+S.latex(f3)+'$',[sq,work(r'k(k+2)(k+4)=k^3+6k^2+8k\Rightarrow S_n='+S.latex(f3))])
chk(n/(4*(3*n+4)),lambda j:R(1,(3*j+1)*(3*j+4)))
put('Review 5',4,'',r'$S_n=\frac n{4(3n+4)},\quad S_\infty=\frac1{12}$',[tele,work(r'\frac1{(3k+1)(3k+4)}=\frac13\left(\frac1{3k+1}-\frac1{3k+4}\right)\Rightarrow S_n=\frac13\left(\frac14-\frac1{3n+4}\right)=\frac n{4(3n+4)}\to\frac1{12}')])
for m in range(1,7):
    xv=R(2,5);assert S.simplify(agp_formula(5,7,x).subs(n,m).subs(x,xv)-agp_sum(5,7,x,m).subs(x,xv))==0
put('Review 5',5,'',r'$\frac{5-(7n-2)x^n}{1-x}+\frac{7x(1-x^{n-1})}{(1-x)^2}\ (x\ne1)$',[agp,work(r'a=5,\ d=7,\ r=x:\ a+(n-1)d=7n-2'),step('If x=1 the series is an A.P. with sum n(7n+3)/2.','اگر x=1 ہو تو یہ حسابی ترقی ہے جس کا مجموعہ n(7n+3)/2 ہے۔','که x=1 وي دا حسابي پرمختګ دی چې مجموعه یې n(7n+3)/2 ده.')])
put('Review 5',6,'',r'$\frac n{n+1}$',[tele,work(r'\frac1{k(k+1)}=\frac1k-\frac1{k+1}\Rightarrow S_n=1-\frac1{n+1}=\frac n{n+1}')])
f7a=S.factor(S.summation((2*k-1)*(k+1)**2,(k,1,n)));chk(f7a,lambda j:(2*j-1)*(j+1)**2)
f7b=S.factor(S.summation((2*k+1)*k**2,(k,1,n)));chk(f7b,lambda j:(2*j+1)*j**2)
put('Review 5',7,'',r'$\text{(i) }'+S.latex(f7a)+r';\ \text{(ii) }'+S.latex(f7b)+'$',[sq,
work(r'\text{(i) }t_k=(2k-1)(k+1)^2=2k^3+3k^2-k-1\Rightarrow S_n='+S.latex(f7a)),
work(r'\text{(ii) }t_k=(2k+1)k^2=2k^3+k^2\Rightarrow S_n='+S.latex(f7b))])
f8a=n**2*(n+1)**2/4+3*(3**n-1)/2;chk(f8a,lambda j:j**3+3**j)
f8b=n*(n+1)*(4*n+11)/6;chk(f8b,lambda j:2*j**2+3*j)
f8c=S.factor(S.summation(k*(k+1)*(k+4),(k,1,n)));chk(f8c,lambda j:j*(j+1)*(j+4))
chk(n*(4*n**2-1)/3,lambda j:(2*j-1)**2)
put('Review 5',8,'',r'$\text{(i) }\frac{n^2(n+1)^2}4+\frac{3(3^n-1)}2;\ \text{(ii) }\frac{n(n+1)(4n+11)}6;\ \text{(iii) }'+S.latex(f8c)+r';\ \text{(iv) }\frac{n(4n^2-1)}3$',[sq,
work(r'\text{(i) }\sum k^3+\sum3^k=\frac{n^2(n+1)^2}4+\frac{3(3^n-1)}2'),
work(r'\text{(ii) }2\cdot\frac{n(n+1)(2n+1)}6+3\cdot\frac{n(n+1)}2=\frac{n(n+1)(4n+11)}6'),
work(r'\text{(iii) }k(k+1)(k+4)=k^3+5k^2+4k\Rightarrow S_n='+S.latex(f8c)),
work(r'\text{(iv) }\sum(4k^2-4k+1)=\frac{n(4n^2-1)}3')])
f9a=n*(n**2+3*n+5)/3;chk(f9a,lambda j:j**2+j+1)
f9b=(3**(n+1)-3+2*n)/4;chk(f9b,lambda j:(3**j+1)/R(2))
put('Review 5',9,'',r'$\text{(i) }\frac{n(n^2+3n+5)}3;\ \text{(ii) }\frac{3^{n+1}+2n-3}4$',[diff,
work(r'\text{(i) }\Delta:4,6,8,10;\ t_n=n^2+n+1;\ S_n=\frac{n(n+1)(2n+1)}6+\frac{n(n+1)}2+n=\frac{n(n^2+3n+5)}3'),
work(r'\text{(ii) }\Delta:3,9,27;\ t_n=2+\frac{3^n-3}2=\frac{3^n+1}2;\ S_n=\frac12\left[\frac{3(3^n-1)}2+n\right]=\frac{3^{n+1}+2n-3}4')])
chk(2*n-2+2**(1-n),lambda j:2*(1-R(1,2**j)))
put('Review 5',10,'',r'$t_n=2\left(1-\frac1{2^n}\right),\quad S_n=2n-2+\frac1{2^{n-1}}$',[gp if False else step('The nth term is the sum of n terms of a G.P. with first term 1 and ratio 1/2.','nواں رکن ایسی ہندسی ترقی کے n ارکان کا مجموعہ ہے جس کا پہلا رکن 1 اور نسبت 1/2 ہے۔','nم حد د هغه هندسي پرمختګ د n حدونو مجموعه ده چې لومړی حد یې 1 او نسبت 1/2 دی.'),
work(r't_n=\frac{1-2^{-n}}{1-1/2}=2-2^{1-n};\quad S_n=\sum(2-2^{1-k})=2n-2\left(1-2^{-n}\right)=2n-2+2^{1-n}')])
A.save(['5.1','5.2','5.3','5.4','Review 5'],[150,151,152,153,154,155,156,157,158,159,160])
