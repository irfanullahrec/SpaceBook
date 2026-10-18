from math11_answer_authoring import Author,step,S
M=S.Matrix;R=S.Rational
A=Author(3)
def v(a):return r'\langle'+','.join(S.latex(S.simplify(x)) for x in a)+r'\rangle'
def put(ex,q,ans,steps):A.put(ex,str(q),'',ans,steps)
def result(expr):return step('Substitute the components and simplify.','اجزا کی قیمتیں رکھ کر مختصر کریں۔','د مؤلفو ارزښتونه کېږدئ او ساده یې کړئ.',expr)
def listed(values):return '; '.join('('+str(i+1)+') $'+x+'$' for i,x in enumerate(values))
dot=step('Multiply matching components and add to obtain the dot product.','ضرب نقطی کے لیے متناظر اجزا ضرب دے کر جمع کریں۔','د نقطوي ضرب لپاره ورته مؤلفې ضرب او جمع کړئ.',r'\mathbf a\cdot\mathbf b=a_1b_1+a_2b_2+a_3b_3')
unit=step('Divide a nonzero vector by its magnitude to obtain its unit direction.','اکائی سمت کے لیے غیر صفر سمتیے کو اس کی مقدار پر تقسیم کریں۔','د واحد لوري لپاره غیرصفر وېکټور په خپلې اندازې ووېشئ.',r'\widehat{\mathbf a}=\mathbf a/|\mathbf a|')
cross=step('Use the component formula for the cross product; keep the order of the vectors.','ضرب صلیبی کے اجزا کا کلیہ استعمال کریں؛ سمتیوں کی ترتیب برقرار رکھیں۔','د صلیبي ضرب د مؤلفو فورمول وکاروئ؛ د وېکټورونو ترتیب وساتئ.',r'\mathbf a\times\mathbf b=\langle a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1\rangle')
a=M([3,4,-1]);b=M([1,-1,3]);c=M([2,1,-5]);values=[a.dot(b),a.dot(c),a.dot(b+c),(2*a+3*b).dot(c),(a-b).dot(c)]
assert values==[-4,15,11,-12,29]
put('3.3',1,listed(list(map(S.latex,values))),[dot]+[result(fr'({i+1})\quad {S.latex(x)}') for i,x in enumerate(values)])
d=M([2,2,-5])+M([2,1,-7]);assert d.norm()==13
put('3.3',2,'$'+v(d/13)+'$',[result(r'\mathbf a+\mathbf b='+v(d)+r',\quad|\mathbf a+\mathbf b|=13'),unit])
pairs=[(M([1,-1,1]),M([-1,1,2])),(M([3,4,0]),M([0,2,-5])),(M([2,0,-3]),M([1,1,1]))]
answers=[];steps=[step('For nonzero vectors, divide the dot product by the product of magnitudes, then take the inverse cosine.','غیر صفر سمتیوں کے لیے ضرب نقطی کو مقداروں کی ضرب پر تقسیم کریں، پھر معکوس کوسائن لیں۔','د غیرصفر وېکټورونو لپاره نقطوي ضرب د اندازو په حاصل ضرب ووېشئ، بیا معکوس کوساین واخلئ.',r'\cos\theta=\frac{\mathbf a\cdot\mathbf b}{|\mathbf a||\mathbf b|},\quad0\le\theta\le\pi')]
for i,(a,b) in enumerate(pairs):
    cs=S.simplify(a.dot(b)/(a.norm()*b.norm()));deg=float(S.acos(cs)*180/S.pi)
    val=r'\cos^{-1}\!\left('+S.latex(cs)+r'\right)\approx '+f'{deg:.2f}'+r'^\circ'
    answers.append(val);steps.append(result(fr'({i+1})\quad \cos\theta=\frac{{{a.dot(b)}}}{{{S.latex(a.norm()*b.norm())}}}={S.latex(cs)}'))
put('3.3',3,listed(answers),steps)
a=M([1,7,3]);b=M([1,-1,2]);c=M([2,1,-3]);assert a.dot(b)==a.dot(c)==0
put('3.3',4,r'$(1,7,3)\cdot(1,-1,2)=0,\quad(1,7,3)\cdot(2,1,-3)=0$',[dot,result(r'1-7+6=0,\quad2+7-9=0'),step('A zero dot product of nonzero vectors proves perpendicularity.','غیر صفر سمتیوں کی ضرب نقطی صفر ہونا عمودیت ثابت کرتا ہے۔','د غیرصفر وېکټورونو صفر نقطوي ضرب عمودیت ثابتوي.')])
a=M([1,2,1]);b=M([2,1,-1]);d=a.cross(b);assert d.dot(a)==d.dot(b)==0
put('3.3',5,'$'+v(d)+'$',[step('Let the required vector have components x,y,z. Solve the two zero-dot-product equations; choose a convenient nonzero solution.','مطلوبہ سمتیے کے اجزا x,y,z فرض کریں۔ صفر ضرب نقطی کی دو مساواتیں حل کر کے مناسب غیر صفر حل لیں۔','د مطلوب وېکټور مؤلفې x,y,z ونیسئ. د صفر نقطوي ضرب دوه معادلې حل او مناسب غیرصفر حل وټاکئ.',r'x+2y+z=0,\quad2x+y-z=0\Rightarrow x=-y,\ z=-y'),result(r'(x,y,z)=(-3,3,-3),\quad\mathbf d\cdot\mathbf a=\mathbf d\cdot\mathbf b=0')])
assert d==M([-3,3,-3])
a=M([1,3,-4]);b=M([2,-3,5]);m1=-a.dot(a)/a.dot(b);m2=-a.dot(b)/b.dot(b)
assert S.simplify((a+m1*b).dot(a))==0 and S.simplify((a+m2*b).dot(b))==0
put('3.3',6,listed([r'm='+S.latex(m1),r'm='+S.latex(m2)]),[dot,result(r'\mathbf a\cdot\mathbf a=26,\quad\mathbf a\cdot\mathbf b=-27,\quad\mathbf b\cdot\mathbf b=38'),result(r'26-27m=0\Rightarrow m=\frac{26}{27};\quad-27+38m=0\Rightarrow m=\frac{27}{38}')])
projection=step('The textbook projection is the signed scalar component: divide the dot product by the magnitude of the vector projected onto.','کتاب میں پروجیکشن نشان دار عددی جز ہے: ضرب نقطی کو اس سمتیے کی مقدار پر تقسیم کریں جس پر عکس لیا جا رہا ہے۔','په کتاب کې پروجکشن نښه لرونکې سکالر مؤلفه ده: نقطوي ضرب د هغه وېکټور په اندازه ووېشئ چې پروجکشن پرې اخیستل کېږي.',r'\operatorname{comp}_{\mathbf b}\mathbf a=\frac{\mathbf a\cdot\mathbf b}{|\mathbf b|},\quad\operatorname{comp}_{\mathbf a}\mathbf b=\frac{\mathbf a\cdot\mathbf b}{|\mathbf a|}')
vals=[];steps=[dot,projection]
for i,(a,b) in enumerate([(M([0,-R(3,2),R(4,5)]),M([1,-2,-2])),(M([-3,1,2]),M([-1,-1,5]))]):
    ab=a.dot(b);vals.append(r'\operatorname{comp}_{\mathbf b}\mathbf a='+S.latex(S.simplify(ab/b.norm()))+r',\quad\operatorname{comp}_{\mathbf a}\mathbf b='+S.latex(S.simplify(ab/a.norm())))
    steps.append(result(fr'({i+1})\quad\mathbf a\cdot\mathbf b={S.latex(ab)},\quad|\mathbf a|={S.latex(a.norm())},\quad|\mathbf b|={S.latex(b.norm())}'))
put('3.3',7,listed(vals),steps)
put('3.3',8,r'$\cos\theta=\frac12$',[dot,result(r'|\langle\sqrt2,1,1\rangle|=2,\quad\cos\theta=\frac{\langle\sqrt2,1,1\rangle\cdot\langle0,1,0\rangle}{2\cdot1}=\frac12')])
for q,d in [(9,M([2,1,-1])),(10,M([5,0,3])-M([-2,1,2]))]:
    force=M([2,3,1]);work=force.dot(d)
    put('3.3',q,'$W='+str(work)+r'\ \text{J}$',[step('Work is force dotted with displacement; use B−A when the endpoints are given. The stated joules assume force in newtons and displacement in metres.','کام، قوت اور نقل مکانی کی ضرب نقطی ہے؛ سرے دیے ہوں تو B−A لیں۔ جول کے لیے قوت نیوٹن اور نقل مکانی میٹر میں فرض ہیں۔','کار د قوې او بېځایه کېدو نقطوي ضرب دی؛ د سرونو په ورکړه B−A واخلئ. جول د قوې لپاره نیوټن او د بېځایه کېدو لپاره متر فرض کوي.',r'\mathbf S='+v(d)+r',\quad W=\mathbf F\cdot\mathbf S='+str(work))])
a=M([3,-2,1]);b=M([1,-3,5]);c=M([2,1,-4]);assert a==b+c and a.dot(c)==0
p=M([1,0,1]);q=M([1,1,1]);r=M([1,1,0]);assert (p-q).dot(r-q)==0 and (p-q).norm()==(r-q).norm()==1
put('3.3',11,r'(i) $14+21=35$; (ii) $\angle PQR=90^\circ,\ |PQ|=|QR|=1$.',[step('For (i), a=b+c, so the three vectors can form triangle sides. The vectors a and c are perpendicular, and their squared lengths add to the squared length of b.','(i) میں a=b+c، لہٰذا تینوں سمتیے مثلث کے اضلاع بن سکتے ہیں۔ a اور c عمود ہیں اور ان کی مقداروں کے مربعوں کا مجموعہ b کی مقدار کے مربع کے برابر ہے۔','په (i) کې a=b+c، نو درې واړه وېکټورونه د مثلث ضلعې جوړوي. a او c عمود دي، او د اندازو د مربعونو مجموعه د b د اندازې مربع ده.',r'\mathbf a\cdot\mathbf c=6-2-4=0,\quad|\mathbf a|^2=14,\ |\mathbf c|^2=21,\ |\mathbf b|^2=35'),step('For (ii), the two sides from Q are perpendicular unit vectors. Therefore the right triangle is isosceles.','(ii) میں Q سے دونوں اضلاع عمودی اکائی سمتیے ہیں۔ لہٰذا قائم الزاویہ مثلث متساوی الساقین ہے۔','په (ii) کې له Q څخه دواړه ضلعې عمودي واحد وېکټورونه دي. نو قائم الزاویه مثلث متساوي الساقین دی.',r'\overrightarrow{QP}=\langle0,-1,0\rangle,\quad\overrightarrow{QR}=\langle0,0,-1\rangle')])
put('3.3',12,r'$\angle APB=90^\circ$',[step('Take the circle centre as origin, diameter endpoints a and −a, and a point p on the semicircle. Their radii have equal magnitude.','دائرے کا مرکز مبدا، قطر کے سرے a اور −a، اور نصف دائرے پر نقطہ p لیں۔ ان کے نصف قطروں کی مقدار یکساں ہے۔','د دایرې مرکز مبدا، د قطر سرونه a او −a، او پر نیمه دایره ټکی p ونیسئ. د شعاعو اندازې برابرې دي.',r'|\mathbf p|=|\mathbf a|'),step('The two chord vectors have zero dot product, so they are perpendicular.','دونوں وتر سمتیوں کی ضرب نقطی صفر ہے، اس لیے وہ عمود ہیں۔','د دواړو وتر وېکټورونو نقطوي ضرب صفر دی، نو عمود دي.',r'(\mathbf a-\mathbf p)\cdot(-\mathbf a-\mathbf p)=|\mathbf p|^2-|\mathbf a|^2=0')])
put('3.3',13,r'$|X-A|=|X-B|=|X-C|$',[step('Let X be the intersection of the perpendicular bisectors of AB and BC. For a nondegenerate triangle these two lines are not parallel.','AB اور BC کے عمودی منصفوں کا نقطہ تقاطع X لیں۔ غیر منحط مثلث کے لیے یہ دو خطوط متوازی نہیں ہوتے۔','د AB او BC د عمودي منصفونو د تقاطع ټکی X ونیسئ. په غیرمنحط مثلث کې دا دوه کرښې موازي نه دي.'),step('Being on the first bisector gives XA=XB; being on the second gives XB=XC. Hence XA=XC, so X lies on the third perpendicular bisector as well.','پہلے منصف پر ہونے سے XA=XB؛ دوسرے پر ہونے سے XB=XC۔ پس XA=XC، لہٰذا X تیسرے عمودی منصف پر بھی ہے۔','پر لومړي منصف د واقع کېدو له امله XA=XB؛ پر دویم له امله XB=XC. نو XA=XC، ځکه X پر درېیم عمودي منصف هم پروت دی.',r'|\mathbf x-\mathbf a|^2=|\mathbf x-\mathbf b|^2=|\mathbf x-\mathbf c|^2')])
def cross_checked(a,b):
    c=a.cross(b)
    assert c.dot(a)==c.dot(b)==0
    assert S.simplify(c.dot(c)-(a.dot(a)*b.dot(b)-a.dot(b)**2))==0
    return c
pairs=[(M([0,1,0]),M([0,2,3])),(M([2,-3,0]),M([0,0,1])),(M([2,-3,5]),M([6,2,-3]))]
put('3.4',1,listed([v(cross_checked(a,b)) for a,b in pairs]),[cross]+[result(fr'({i+1})\quad {v(a)}\times{v(b)}={v(a.cross(b))}') for i,(a,b) in enumerate(pairs)])
pairs=[(M([-1,2,-3]),M([2,-4,6]),-2),(M([3,6,-9]),M([1,2,-3]),R(1,3))]
for a,b,k in pairs:assert b==k*a and a.cross(b)==S.zeros(3,1)
put('3.4',2,listed([r'\mathbf b=-2\mathbf a,\ \mathbf a\times\mathbf b=\mathbf0',r'\mathbf b=\frac13\mathbf a,\ \mathbf a\times\mathbf b=\mathbf0']),[step('First compare component ratios to get a scalar multiple. Independently calculate the cross product; it is zero in each case. Both criteria establish parallelism.','پہلے اجزا کے تناسب سے عددی مضرب حاصل کریں۔ الگ سے ضرب صلیبی معلوم کریں؛ دونوں صورتوں میں صفر ہے۔ دونوں معیار متوازیت ثابت کرتے ہیں۔','لومړی د مؤلفو نسبتونه د سکالر مضرب لپاره پرتله کړئ. بیا جلا صلیبي ضرب محاسبه کړئ؛ په دواړو کې صفر دی. دواړه معیارونه موازي والی ثابتوي.'),cross])
def perpendicular_pair(q,pairs,magnitude=1):
    vals=[];st=[cross,unit]
    for i,(a,b) in enumerate(pairs):
        c=cross_checked(a,b);out=magnitude*c/c.norm();assert S.simplify(out.norm()-magnitude)==0
        vals.append(r'\pm'+v(out));st.append(result(fr'({i+1})\quad\mathbf a\times\mathbf b={v(c)},\quad|\mathbf a\times\mathbf b|={S.latex(c.norm())}'))
    put('3.4',q,listed(vals),st)
perpendicular_pair(3,[(M([1,-2,3]),M([2,1,-1])),(M([3,-1,6]),M([1,4,1]))])
a=M([3,-6,5]);b=M([2,-1,4]);c=M([1,1,-1]);assert (a+b).cross(a-b)==-2*a.cross(b)
put('3.4',4,listed([v(cross_checked(a,b)),v(cross_checked(b,c)),v(cross_checked(a+b,a-b))]),[cross,result(r'(\mathbf a+\mathbf b)\times(\mathbf a-\mathbf b)=-2(\mathbf a\times\mathbf b)')])
tri=step('Form two side vectors from the same vertex. The triangle area is half the magnitude of their cross product.','ایک ہی راس سے دو ضلع سمتیے بنائیں۔ مثلث کا رقبہ ان کی ضرب صلیبی کی مقدار کا نصف ہے۔','له یوه رأس څخه د دوو ضلعو وېکټورونه جوړ کړئ. د مثلث مساحت د صلیبي ضرب د اندازې نیمایي دی.',r'\mathcal A=\frac12|\overrightarrow{PQ}\times\overrightarrow{PR}|')
vals=[];st=[tri,cross]
for i,(p,q,r) in enumerate([(M([-2,-3,0]),M([3,2,0]),M([-1,-8,0])),(M([-2,-1,3]),M([1,2,-1]),M([4,3,-3]))]):
    a=q-p;b=r-p;c=cross_checked(a,b);vals.append(S.latex(c.norm()/2));st.append(result(fr'({i+1})\quad PQ={v(a)},\quad PR={v(b)},\quad PQ\times PR={v(c)}'))
put('3.4',5,listed(vals),st)
f=M([3,-2,5]);p=M([1,-2,2]);vals=[];st=[step('Use the displacement from the reference point to the point of application, then calculate r×F in that order.','حوالہ نقطے سے نقطہ عمل تک نقل مکانی لیں، پھر اسی ترتیب سے r×F معلوم کریں۔','له مرجع ټکي څخه د قوې د عمل تر ټکي بېځایه کېدل واخلئ، بیا په همدې ترتیب r×F محاسبه کړئ.',r'\boldsymbol\tau=(\mathbf p-\mathbf o)\times\mathbf F'),cross]
for i,o in enumerate([M([0,0,0]),M([1,2,1])]):
    r=p-o;moment=cross_checked(r,f);vals.append(v(moment));st.append(result(fr'({i+1})\quad\mathbf r={v(r)},\quad\boldsymbol\tau={v(moment)}'))
put('3.4',6,listed(vals),st)
put('3.4',7,r'$\mathbf A\times\mathbf B=\mathbf B\times\mathbf C=\mathbf C\times\mathbf A$',[step('Substitute C=−A−B, distribute the cross product and use A×A=B×B=0 and B×A=−A×B.','C=−A−B رکھیں، ضرب صلیبی تقسیم کریں اور A×A=B×B=0 نیز B×A=−A×B استعمال کریں۔','C=−A−B کېږدئ، صلیبي ضرب ووېشئ او A×A=B×B=0 او B×A=−A×B وکاروئ.',r'\mathbf B\times\mathbf C=-\mathbf B\times\mathbf A-\mathbf B\times\mathbf B=\mathbf A\times\mathbf B'),result(r'\mathbf C\times\mathbf A=-\mathbf A\times\mathbf A-\mathbf B\times\mathbf A=\mathbf A\times\mathbf B')])
vals=[];st=[cross,unit]
for i,(a,b,magnitude) in enumerate([(M([1,1,2]),M([-2,1,-3]),1),(M([2,-3,4]),M([4,-2,-4]),10)]):
    c=cross_checked(a,b);out=magnitude*c/c.norm();assert S.simplify(out.norm()-magnitude)==0
    vals.append(r'\pm'+v(out));st.append(result(fr'({i+1})\quad\mathbf a\times\mathbf b={v(c)},\quad\mathbf n=\pm {magnitude}\frac{{{v(c)}}}{{{S.latex(c.norm())}}}'))
put('3.4',8,listed(vals),st)
vals=[];st=[step('For diagonal vectors d1 and d2, the parallelogram area is half the magnitude of d1×d2. This follows by writing the diagonals as u+v and v−u.','قطر سمتیوں d1 اور d2 کے لیے متوازی الاضلاع کا رقبہ d1×d2 کی مقدار کا نصف ہے۔ قطر u+v اور v−u لکھنے سے یہ حاصل ہوتا ہے۔','د قطري وېکټورونو d1 او d2 لپاره د متوازي الاضلاع مساحت د d1×d2 د اندازې نیمایي دی. قطرونه u+v او v−u لیکل دا پایله ورکوي.',r'\mathcal A=\frac12|\mathbf d_1\times\mathbf d_2|')]
for i,(a,b) in enumerate([(M([4,1,-2]),M([-2,3,4])),(M([3,2,-2]),M([1,-3,4]))]):
    c=cross_checked(a,b);vals.append(S.latex(c.norm()/2));st.append(result(fr'({i+1})\quad\mathbf d_1\times\mathbf d_2={v(c)},\quad\mathcal A={S.latex(c.norm()/2)}'))
put('3.4',9,listed(vals),st)
A.save(['3.3','3.4'],[106,112,113])
