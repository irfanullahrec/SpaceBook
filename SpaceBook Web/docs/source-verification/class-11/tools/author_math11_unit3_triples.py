from math11_answer_authoring import Author,step,S
M=S.Matrix
A=Author(3)
def v(a):return r'\langle'+','.join(S.latex(S.simplify(x)) for x in a)+r'\rangle'
def result(expr):return step('Substitute and simplify to obtain the result.','قیمتیں رکھ کر مختصر کرنے سے نتیجہ حاصل ہوتا ہے۔','ارزښتونه کېږدئ او ساده یې کړئ ترڅو پایله ترلاسه شي.',expr)
def put(q,ans,steps,p=''):A.put('3.5',str(q),p,ans,steps)
triple=step('Compute the scalar triple product as the determinant with the three vectors as rows.','تین سمتیوں کو قطاروں میں لکھ کر مقطع سے عددی ثلاثی ضرب معلوم کریں۔','درې وېکټورونه د قطارونو په توګه ولیکئ او له ډیټرمینانټ څخه سکالر درې ګونی ضرب پیدا کړئ.',r'[\mathbf a\,\mathbf b\,\mathbf c]=\mathbf a\cdot(\mathbf b\times\mathbf c)=\det\begin{bmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{bmatrix}')
def tp(a,b,c):
    val=a.dot(b.cross(c));assert val==M.vstack(a.T,b.T,c.T).det()
    return val
a=M([2,1,3]);b=M([-1,2,1]);c=M([3,1,2]);val=tp(a,b,c)
put(1,'$'+str(val)+'$',[triple,result(r'\mathbf b\times\mathbf c='+v(b.cross(c))+r',\quad\mathbf a\cdot(\mathbf b\times\mathbf c)='+str(val))])
a=M([3,1,-1]);b=M([2,-3,1]);c=M([1,-3,-4]);val=tp(a,b,c)
put(2,'$V='+str(abs(val))+'$',[triple,step('Volume is the absolute value of the scalar triple product.','حجم عددی ثلاثی ضرب کی مطلق قیمت ہے۔','حجم د سکالر درې ګوني ضرب مطلق ارزښت دی.',r'V=|[\mathbf a\,\mathbf b\,\mathbf c]|=|'+str(val)+'|='+str(abs(val)))])
a=M([3,0,2]);b=M([1,2,1]);c=M([0,-1,4]);val=tp(a,b,c);assert val==tp(b,c,a)==tp(c,a,b)==-tp(a,c,b)
put(3,r'$[\mathbf a\,\mathbf b\,\mathbf c]=[\mathbf b\,\mathbf c\,\mathbf a]=[\mathbf c\,\mathbf a\,\mathbf b]='+str(val)+r',\quad(\mathbf c\times\mathbf b)\cdot\mathbf a='+str(-val)+'$',[triple,result(r'\mathbf b\times\mathbf c='+v(b.cross(c))+r',\quad\mathbf c\times\mathbf a='+v(c.cross(a))+r',\quad\mathbf a\times\mathbf b='+v(a.cross(b))),step('Cyclic changes preserve the product; reversing the two vectors in the cross product changes the sign.','دوری تبدیلیاں ضرب برقرار رکھتی ہیں؛ ضرب صلیبی میں دو سمتیوں کی ترتیب الٹنے سے نشان بدلتا ہے۔','دوراني بدلونونه ضرب ساتي؛ په صلیبي ضرب کې د دوو وېکټورونو ترتیب اړول نښه بدلوي.')])
a=M([1,-1,0]);b=M([0,1,-1]);c=M([-1,0,1]);assert tp(a,b,c)==0
put(4,r'$0$',[triple,result(r'(\mathbf j-\mathbf k)\times(\mathbf k-\mathbf i)=\langle1,1,1\rangle,\quad\langle1,-1,0\rangle\cdot\langle1,1,1\rangle=0')])
aa=M(S.symbols('a_1 a_2 a_3',real=True));bb=M(S.symbols('b_1 b_2 b_3',real=True));cc=aa.cross(bb)
assert S.expand(cc.dot(aa))==S.expand(cc.dot(bb))==0
assert S.expand(cc.dot(cc)-aa.dot(aa)*bb.dot(bb)+aa.dot(bb)**2)==0
put(5,r'$\mathbf a\times\mathbf b=\langle a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1\rangle$; $|\mathbf a\times\mathbf b|^2=|\mathbf a|^2|\mathbf b|^2-(\mathbf a\cdot\mathbf b)^2$.',[
step('Expand the cross product. In part (ii), its square means its dot product with itself, or squared magnitude.','ضرب صلیبی کھولیں۔ جز (ii) میں اس کے مربع سے مراد اس کی اپنے ساتھ ضرب نقطی، یعنی مقدار کا مربع ہے۔','صلیبي ضرب پراخ کړئ. په (ii) برخه کې مربع له خپل ځان سره نقطوي ضرب، یعنې د اندازې مربع دی.',r'\mathbf c=\mathbf a\times\mathbf b=\langle a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1\rangle'),
step('For (i), terms cancel in each dot product, proving orthogonality.','(i) میں ہر ضرب نقطی کے اجزا کٹ جاتے ہیں، جس سے عمودیت ثابت ہوتی ہے۔','په (i) کې د هر نقطوي ضرب حدونه حذف کېږي او عمودیت ثابتوي.',r'\mathbf a\cdot\mathbf c=a_1(a_2b_3-a_3b_2)+a_2(a_3b_1-a_1b_3)+a_3(a_1b_2-a_2b_1)=0,\quad\mathbf b\cdot\mathbf c=0'),
result(r'\text{(ii)}\quad|\mathbf c|^2=(a_2b_3-a_3b_2)^2+(a_3b_1-a_1b_3)^2+(a_1b_2-a_2b_1)^2'),
result(r'\text{(iii)}\quad(\mathbf a\cdot\mathbf b)^2=(a_1b_1+a_2b_2+a_3b_3)^2,\quad|\mathbf a|^2=a_1^2+a_2^2+a_3^2,\quad|\mathbf b|^2=b_1^2+b_2^2+b_3^2'),
step('For (iv), expand the product of the two squared magnitudes and subtract the squared dot product. The three remaining squares are exactly those in (ii).','(iv) میں دونوں مقداروں کے مربعوں کی ضرب کھول کر ضرب نقطی کا مربع تفریق کریں۔ باقی تین مربع بالکل (ii) والے ہیں۔','په (iv) کې د دواړو اندازو د مربعونو ضرب پراخ او د نقطوي ضرب مربع ترې منفي کړئ. پاتې درې مربعونه د (ii) برخې هماغه مربعونه دي.',r'(a_1^2+a_2^2+a_3^2)(b_1^2+b_2^2+b_3^2)-(a_1b_1+a_2b_2+a_3b_3)^2=|\mathbf c|^2')])
p=M([4,-2,1]);q=M([5,1,6]);r=M([2,2,-5]);s=M([3,5,0]);val=tp(q-p,r-p,s-p);assert val==0
put(6,r'$[\overrightarrow{PQ}\,\overrightarrow{PR}\,\overrightarrow{PS}]=0$',[triple,result(r'PQ=\langle1,3,5\rangle,\quad PR=\langle-2,4,-6\rangle,\quad PS=\langle-1,7,-1\rangle=PQ+PR'),step('Yes. The third displacement is the sum of the first two, so all four points lie in one plane.','جی ہاں۔ تیسری نقل مکانی پہلی دو کا مجموعہ ہے، لہٰذا چاروں نقاط ایک مستوی میں ہیں۔','هو. درېیم بېځایه کېدل د لومړیو دوو مجموعه ده، نو څلور واړه ټکي په یوه مستوي کې پراته دي.')])
c=S.symbols('c')
for part,a,b,w in [('(i)',M([1,2,3]),M([2,-3,4]),M([3,1,c])),('(ii)',M([1,1,-1]),M([1,-2,1]),M([c,1,-c])),('(iii)',M([1,1,2]),M([2,3,1]),M([c,2,6]))]:
    det=S.expand(tp(a,b,w));root=S.solve(det,c);assert len(root)==1 and det.subs(c,root[0])==0
    put(7,'$c='+S.latex(root[0])+'$',[triple,step('Coplanarity requires zero scalar triple product; solve the resulting linear equation.','ہم مستوی ہونے کے لیے عددی ثلاثی ضرب صفر ہو؛ حاصل خطی مساوات حل کریں۔','هم مستوي والی صفر سکالر درې ګونی ضرب غواړي؛ ترلاسه شوې خطي معادله حل کړئ.',S.latex(det)+'=0')],part)
a=M([1,2,3]);b=M([4,5,6]);c=M([0,7,8]);val1=abs(tp(a,b,c))/6
p=M([2,3,1]);q=M([-1,-2,0]);r=M([0,2,-5]);s=M([0,1,-2]);val2=abs(tp(q-p,r-p,s-p))/6
put(8,r'(i) $V='+S.latex(val1)+r'$; (ii) $V='+S.latex(val2)+'$',[step('A tetrahedron has one sixth the volume of the parallelepiped built from three edges from the same vertex.','ایک ہی راس سے تین اضلاع سے بنے متوازی السطوح کے حجم کا چھٹا حصہ چہار سطحی کا حجم ہے۔','د یوه رأس له درې ضلعو جوړ موازي السطوح د حجم شپږمه برخه د څلورمخیز حجم دی.',r'V=\frac16|[\mathbf a\,\mathbf b\,\mathbf c]|'),triple,result(r'\text{(i)}\quad [\mathbf a\,\mathbf b\,\mathbf c]='+str(tp(a,b,c))),result(r'\text{(ii)}\quad AB='+v(q-p)+',\ AC='+v(r-p)+',\ AD='+v(s-p)+r',\quad [AB\,AC\,AD]='+str(tp(q-p,r-p,s-p)))])
put(9,r'(i) $1$; (ii) $-1$',[result(r'(\mathbf i\times\mathbf j)\cdot\mathbf k+\mathbf i\cdot\mathbf j=\mathbf k\cdot\mathbf k+0=1'),result(r'(\mathbf k\times\mathbf j)\cdot\mathbf i+\mathbf j\cdot\mathbf k=(-\mathbf i)\cdot\mathbf i+0=-1')])
A.save(['3.5'],[117])

A=Author(3)
def review(q,ans,steps,p='',**kw):A.put('Review 3',str(q),p,ans,steps,**kw)
mcqs=[
('(i)','c',r'1',[result(r'1+(-1)+1=1')]),
('(ii)','a',r'\text{Equilateral}',[step('The first two vectors add to the third, and all three squared lengths are 38. Hence all three triangle sides are equal.','پہلے دو سمتیوں کا مجموعہ تیسرا ہے اور تینوں کی مقداروں کے مربع 38 ہیں۔ لہٰذا مثلث کے تینوں اضلاع برابر ہیں۔','د لومړیو دوو وېکټورونو مجموعه درېیم دی او د درې واړو د اندازو مربعونه 38 دي. نو د مثلث درې واړه ضلعې برابرې دي.',r'\mathbf a+\mathbf b=\mathbf c,\quad|\mathbf a|^2=|\mathbf b|^2=|\mathbf c|^2=38')]),
('(iii)','d',r'\lambda=-2',[result(r'\mathbf b=2\mathbf a\Rightarrow-\lambda=2\Rightarrow\lambda=-2')]),
('(iv)','b',r'\mathbf a\perp\mathbf b',[step('Square both sides and expand the dot products. For nonzero vectors, the zero dot product means perpendicularity.','دونوں طرف مربع کر کے ضرب نقطی کھولیں۔ غیر صفر سمتیوں کے لیے صفر ضرب نقطی عمودیت ظاہر کرتی ہے۔','دواړه خواوې مربع او نقطوي ضربونه پراخ کړئ. د غیرصفر وېکټورونو صفر نقطوي ضرب عمودیت ښيي.',r'|\mathbf a+\mathbf b|^2-|\mathbf a-\mathbf b|^2=4\mathbf a\cdot\mathbf b=0')]),
('(v)','b',r'\frac2{\sqrt{14}}',[result(r'\frac{(2,3,-2)\cdot(1,2,3)}{\sqrt{14}}=\frac{2+6-6}{\sqrt{14}}=\frac2{\sqrt{14}}')]),
('(vi)','a',r'\alpha=-2,\ \beta=-3',[result(r'(\alpha-\beta-1)\mathbf a+(2\alpha+4)\mathbf b=0\Rightarrow 2\alpha+4=0,\quad\alpha-\beta-1=0')]),
('(vii)','a',r'\mathbf0',[result(r'(\mathbf b-\mathbf a)+(\mathbf c-\mathbf b)+(\mathbf a-\mathbf c)=\mathbf0')]),
('(viii)','b',r'\frac\pi4',[step('For nonzero vectors cancel the magnitudes to get |cos θ|=sin θ. Both π/4 and 3π/4 solve this on [0,π]; only π/4 is offered.','غیر صفر سمتیوں کی مقداریں کاٹنے سے |cos θ|=sin θ ملتا ہے۔ [0,π] میں π/4 اور 3π/4 دونوں حل ہیں؛ اختیارات میں صرف π/4 ہے۔','د غیرصفر وېکټورونو اندازې حذف کړئ، |cos θ|=sin θ ترلاسه کېږي. په [0,π] کې π/4 او 3π/4 دواړه حلونه دي؛ په انتخابونو کې یوازې π/4 شته.',r'|\cos\theta|=\sin\theta\Rightarrow\theta=\pi/4\ \text{or}\ 3\pi/4')])
]
for part,choice,ans,steps in mcqs:
    ur=('متساوی الاضلاع' if part=='(ii)' else '$'+ans+'$')
    ps=('متساوي الاضلاع' if part=='(ii)' else '$'+ans+'$')
    review(1,'('+choice+') $'+ans+'$',steps,part,category='mcqs',answerUr='('+choice+') '+ur,answerPs='('+choice+') '+ps)
aa=M([3,5,2]);bb=M([2,-3,-5]);cc=M([5,2,-3]);assert aa+bb==cc and aa.dot(aa)==bb.dot(bb)==cc.dot(cc)==38
review(2,r'$\lambda=-9,\ \mu=27$',[step('A zero cross product makes the two nonzero vectors parallel. The first component fixes the multiplier as 3.','صفر ضرب صلیبی سے دو غیر صفر سمتیے متوازی ہیں۔ پہلا جز مضرب 3 مقرر کرتا ہے۔','صفر صلیبي ضرب دوه غیرصفر وېکټورونه موازي کوي. لومړۍ مؤلفه مضرب 3 ټاکي.',r'(3,-\lambda,\mu)=3(1,3,9)\Rightarrow-\lambda=9,\quad\mu=27')])
d=M([9,-1,1])+M([2,-2,-1]);unit=d/d.norm();assert S.simplify(unit.norm())==1
review(3,r'$\pm'+v(unit)+'$',[result(r'\mathbf a+\mathbf b=\langle11,-3,0\rangle,\quad|\mathbf a+\mathbf b|=\sqrt{130}'),step('Divide by the magnitude. Either sign is parallel; the positive sign points in the same direction.','مقدار پر تقسیم کریں۔ دونوں نشان متوازی ہیں؛ مثبت نشان کی سمت یکساں ہے۔','په اندازه یې ووېشئ. دواړه نښې موازي دي؛ مثبت نښه هماغه لوری لري.')])
x,y,z=S.symbols('x y z');r=M([x,y,z]);assert S.expand(r.cross(M([1,0,0])).dot(r.cross(M([0,1,0])))+x*y)==0
review(4,r'$0$',[result(r'\mathbf r\times\mathbf i=\langle0,z,-y\rangle,\quad\mathbf r\times\mathbf j=\langle-z,0,x\rangle'),result(r'0(-z)+z(0)+(-y)x+xy=0')])
a=M([7,1,-4]);b=M([2,6,3]);assert a.dot(b)==8 and b.norm()==7
review(5,r'$\frac87$',[step('Divide the dot product by the magnitude of b to obtain the scalar projection.','عددی پروجیکشن کے لیے ضرب نقطی کو b کی مقدار پر تقسیم کریں۔','د سکالر پروجکشن لپاره نقطوي ضرب د b په اندازه ووېشئ.',r'\operatorname{comp}_{\mathbf b}\mathbf a=\frac{14+6-12}{\sqrt{4+36+9}}=\frac87')])
lam=S.symbols('lambda');det=tp(M([1,3,1]),M([2,-1,-1]),M([0,lam,3]));root=S.solve(det,lam)[0];assert root==7
review(6,r'$\lambda=7$',[triple,result(S.latex(det)+r'=0\Rightarrow\lambda=7')])
review(7,r'$\theta=60^\circ\ \text{or}\ 120^\circ$',[step('A unit cross product has magnitude 1. Use the cross-product magnitude formula and include both angles in the usual interval 0 to 180 degrees.','اکائی ضرب صلیبی کی مقدار 1 ہے۔ ضرب صلیبی کی مقدار کا کلیہ لگائیں اور صفر سے 180 درجے کے معمول کے وقفے میں دونوں زاویے شامل کریں۔','د واحد صلیبي ضرب اندازه 1 ده. د صلیبي ضرب د اندازې فورمول وکاروئ او له صفر تر 180 درجو په معمولي واټن کې دواړه زاویې شاملې کړئ.',r'1=\sqrt3\cdot\frac23\sin\theta\Rightarrow\sin\theta=\frac{\sqrt3}{2}')])
p=M([0,0,2]);q=M([-1,3,2]);r=M([1,0,4]);c=(q-p).cross(r-p)
review(8,'$'+S.latex(c.norm()/2)+'$',[result(r'PQ=\langle-1,3,0\rangle,\quad PR=\langle1,0,2\rangle,\quad PQ\times PR='+v(c)),step('The triangle area is half the magnitude of the cross product of adjacent sides.','مثلث کا رقبہ ملحق اضلاع کی ضرب صلیبی کی مقدار کا نصف ہے۔','د مثلث مساحت د څنګ په څنګ ضلعو د صلیبي ضرب د اندازې نیمایي دی.',r'\mathcal A=\frac12|PQ\times PR|='+S.latex(c.norm()/2))])
p=M([1,2,-3]);q=M([5,8,1]);r=M([4,-2,2]);s=M([0,-8,-2]);assert p+r==q+s;c=(q-p).cross(s-p)
review(9,'$'+S.latex(c.norm())+'$',[result(r'AB=\langle4,6,4\rangle,\quad AD=\langle-1,-10,1\rangle,\quad AB\times AD='+v(c)),step('Use the full cross-product magnitude for the parallelogram area.','متوازی الاضلاع کے رقبے کے لیے ضرب صلیبی کی پوری مقدار لیں۔','د متوازي الاضلاع د مساحت لپاره د صلیبي ضرب بشپړه اندازه واخلئ.',r'\mathcal A=|AB\times AD|='+S.latex(c.norm()))])
review(10,r'(i) $a^2=b^2+c^2-2bc\cos A$; (ii) $a=b\cos C+c\cos B$.',[
step('Let u=AB and v=AC. Their lengths are c and b, their included angle is A, and BC=v−u has length a.','u=AB اور v=AC لیں۔ ان کی مقداریں c اور b، درمیانی زاویہ A، اور BC=v−u کی مقدار a ہے۔','u=AB او v=AC ونیسئ. اندازې یې c او b، منځنی زاویه A، او د BC=v−u اندازه a ده.',r'a^2=(\mathbf v-\mathbf u)\cdot(\mathbf v-\mathbf u)=b^2+c^2-2bc\cos A'),
step('For the projection law, use BC=BA+AC and dot with the unit vector along BC. The directed projections of BA and AC have lengths c cos B and b cos C.','قانون پروجیکشن کے لیے BC=BA+AC کو BC کے اکائی سمتیے سے ضرب نقطی دیں۔ BA اور AC کے نشان دار پروجیکشن c cos B اور b cos C ہیں۔','د پروجکشن قانون لپاره BC=BA+AC د BC له واحد وېکټور سره نقطوي ضرب کړئ. د BA او AC نښه لرونکي پروجکشنونه c cos B او b cos C دي.',r'a=\overrightarrow{BC}\cdot\widehat{BC}=\overrightarrow{BA}\cdot\widehat{BC}+\overrightarrow{AC}\cdot\widehat{BC}=c\cos B+b\cos C')])
A.save(['Review 3'],[117,118])
