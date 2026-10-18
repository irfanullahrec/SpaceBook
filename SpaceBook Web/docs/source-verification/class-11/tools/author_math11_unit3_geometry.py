from math11_answer_authoring import Author,step,S
from math11_vector_figures import construction
M=S.Matrix;R=S.Rational
A=Author(3)
def v(a):return r'\langle'+','.join(S.latex(S.simplify(x)) for x in a)+r'\rangle'
def put(ex,q,ans,steps,p=''):A.put(ex,str(q),p,ans,steps)
def result(expr):return step('Substitute the components and simplify.','اجزا کی قیمتیں رکھ کر مختصر کریں۔','د مؤلفو ارزښتونه کېږدئ او ساده یې کړئ.',expr)
def listed(values):return '; '.join('('+str(i+1)+') $'+x+'$' for i,x in enumerate(values))
chain=step('Use head-to-tail addition and reverse a vector when its direction is reversed.','سرے سے سر تک سمتی جمع استعمال کریں؛ سمت الٹنے پر سمتیے کی علامت بدلیں۔','د سر تر لکۍ وېکټوري جمع وکاروئ؛ د لوري په اوښتو د وېکټور نښه واړوئ.')
position=step('The vector from P to Q equals the position vector of Q minus that of P.','P سے Q تک سمتیہ، Q کے مقامی سمتیے اور P کے مقامی سمتیے کا فرق ہے۔','له P څخه Q ته وېکټور د Q او P د موقعیت وېکټورونو توپیر دی.',r'\overrightarrow{PQ}=\mathbf q-\mathbf p')
put('3.1',1,listed([r'\overrightarrow{DE}=-\mathbf a',r'\overrightarrow{EF}=-\mathbf b',r'\overrightarrow{FA}=-\mathbf c',r'\overrightarrow{AD}=2\mathbf b',r'\overrightarrow{BE}=2\mathbf c']),[chain,step('Opposite sides have opposite directed vectors. Each long diagonal is twice the parallel side.','مقابل اضلاع کے سمتیے مخالف ہیں۔ ہر بڑا قطر اپنے متوازی ضلع کا دوگنا ہے۔','مقابلې ضلعې مخالف لوري لري. هر لوی قطر د موازي ضلعې دوه چنده دی.',r'\mathbf a+\mathbf c=\mathbf b,\quad \overrightarrow{AD}=\mathbf a+\mathbf b+\mathbf c=2\mathbf b')])
draw=step('Place the indicated copies head to tail. For subtraction reverse b. The red arrow from the starting point to the final endpoint is the required vector.','دی گئی نقول سرے سے سر ملا کر رکھیں۔ تفریق کے لیے b کی سمت الٹیں۔ ابتدائی نقطے سے آخری سرے تک سرخ تیر مطلوبہ سمتیہ ہے۔','ورکړل شوې نقلونه سر په لکۍ کېږدئ. د تفریق لپاره د b لوری واړوئ. له پیل څخه تر وروستي سر پورې سور غشی مطلوب وېکټور دی.')
draw['svg']=construction()
put('3.1',2,listed([r'\mathbf a+\mathbf b+\mathbf b',r'\mathbf a+\mathbf a+(-\mathbf b)',r'\mathbf a+\mathbf a+\mathbf a+(-\mathbf b)+(-\mathbf b)']),[chain,draw])
put('3.1',3,listed([r'\overrightarrow{OR}=\frac12\mathbf p',r'\overrightarrow{PQ}=\mathbf q-\mathbf p',r'\overrightarrow{OS}=\frac34\mathbf q',r'\overrightarrow{RS}=\frac34\mathbf q-\frac12\mathbf p']),[position,step('R halves OP, while OS:SQ=3:1 gives three quarters of OQ. Subtract the position of R from that of S.','R، OP کو نصف کرتا ہے جبکہ OS:SQ=3:1 سے OQ کے تین چوتھائی ملتے ہیں۔ S کے مقام سے R کا مقام تفریق کریں۔','R د OP نیمایي ده، او OS:SQ=3:1 د OQ درې پر څلور برخه ورکوي. د S له موقعیت څخه د R موقعیت منفي کړئ.',r'\mathbf r=\frac12\mathbf p,\quad \mathbf s=\frac34\mathbf q')])
put('3.1',4,listed([r'\overrightarrow{AD}=\frac32\mathbf b',r'\overrightarrow{OD}=\mathbf a+\frac32\mathbf b',r'\overrightarrow{BD}=\mathbf a+\frac12\mathbf b']),[chain,result(r'\overrightarrow{AC}=\mathbf b,\quad\overrightarrow{CD}=\frac12\mathbf b,\quad\overrightarrow{OD}=\overrightarrow{OA}+\overrightarrow{AD}')])
put('3.1',5,listed([r'\overrightarrow{OM}=\frac12\mathbf a',r'\overrightarrow{MB}=\mathbf b-\frac12\mathbf a',r'\overrightarrow{MG}=\frac13\mathbf b-\frac16\mathbf a',r'\overrightarrow{OG}=\frac13(\mathbf a+\mathbf b)']),[position,step('MG:GB=1:2, so MG is one third of MB. Add OM to MG to reach G.','MG:GB=1:2 ہے، لہٰذا MG، MB کا ایک تہائی ہے۔ G تک پہنچنے کے لیے OM اور MG جمع کریں۔','MG:GB=1:2 دی، نو MG د MB درېیمه برخه ده. G ته د رسېدو لپاره OM او MG جمع کړئ.',r'\overrightarrow{OG}=\frac12\mathbf a+\frac13(\mathbf b-\frac12\mathbf a)=\frac13(\mathbf a+\mathbf b)')])
put('3.1',6,listed([r'\overrightarrow{PR}=\mathbf r-\mathbf p',r'\overrightarrow{PM}=\frac12(\mathbf r-\mathbf p)',r'\overrightarrow{OM}=\frac12(\mathbf p+\mathbf r)']),[position,result(r'\overrightarrow{OM}=\overrightarrow{OP}+\overrightarrow{PM}=\mathbf p+\frac12(\mathbf r-\mathbf p)')])
put('3.1',7,listed([r'\overrightarrow{AC}=\mathbf x+\mathbf y',r'\overrightarrow{AO}=\mathbf y',r'\overrightarrow{CD}=\mathbf y-\mathbf x',r'\overrightarrow{BF}=\mathbf y-2\mathbf x']),[chain,step('The centre bisects AD, which equals twice BC. The next side is y−x; AF has this same vector. Subtract AB from AF to obtain BF.','مرکز AD کو نصف کرتا ہے، اور AD، BC کا دوگنا ہے۔ اگلا ضلع y−x ہے؛ AF بھی اسی سمتیے کے برابر ہے۔ BF کے لیے AF سے AB تفریق کریں۔','مرکز AD نیموي چې د BC دوه چنده دی. راتلونکې ضلع y−x ده؛ AF هم همدغه وېکټور لري. د BF لپاره له AF څخه AB منفي کړئ.',r'\overrightarrow{BF}=\overrightarrow{BA}+\overrightarrow{AF}=-\mathbf x+(\mathbf y-\mathbf x)')])
combine=step('Add or subtract corresponding components. Magnitude is the square root of the sum of squared components.','متناظر اجزا جمع یا تفریق کریں۔ مقدار، اجزا کے مربعوں کے مجموعے کا جذر ہے۔','ورته مؤلفې جمع یا منفي کړئ. اندازه د مؤلفو د مربعونو د مجموعې جذر دی.',r'|(x,y,z)|=\sqrt{x^2+y^2+z^2}')
unit=step('Divide the vector by its nonzero magnitude to obtain a unit vector in the same direction.','اسی سمت کا اکائی سمتیہ حاصل کرنے کے لیے سمتیے کو اس کی غیر صفر مقدار پر تقسیم کریں۔','په همدې لوري د واحد وېکټور لپاره وېکټور په خپلې غیرصفر اندازې ووېشئ.',r'\widehat{\mathbf a}=\frac{\mathbf a}{|\mathbf a|}')
a=M([3,-5]);b=M([-2,3]);vals=[v(a+2*b),v(3*a-2*b),v(2*(a-b)),S.latex((a+b).norm()),S.latex(a.norm()-b.norm()),S.latex(a.norm()/b.norm())]
put('3.2',1,listed(vals),[combine,result(r'\mathbf a+\mathbf b=\langle1,-2\rangle,\quad |\mathbf a|=\sqrt{34},\quad|\mathbf b|=\sqrt{13}')]+[result(fr'({i+1})\quad {t}') for i,t in enumerate(vals)])
vecs=[M([3,0]),M([3,-4]),M([1,1,-2]),M([S.sqrt(3)/2,-R(1,2)])]
vals=[v(x/x.norm()) for x in vecs]
assert all(S.simplify((x/x.norm()).norm()-1)==0 for x in vecs)
put('3.2',2,listed(vals),[unit]+[result(fr'({i+1})\quad |\mathbf a|={S.latex(x.norm())},\quad\widehat{{\mathbf a}}={v(x/x.norm())}') for i,x in enumerate(vecs)])
p,q=S.symbols('p q');sol=S.solve(M([1,-9])-p*M([1,2])-q*M([5,-1]),[p,q]);assert sol=={p:-4,q:1}
put('3.2',3,r'$p=-4,\ q=1$',[step('Equate the i and j components and solve the two linear equations.','i اور j کے اجزا برابر رکھ کر دو خطی مساواتیں حل کریں۔','د i او j مؤلفې برابرې کړئ او دواړه خطي معادلې حل کړئ.',r'p+5q=1,\quad 2p-q=-9\ \Rightarrow\ 11q=11')])
x=S.symbols('x',real=True);roots=S.solve((x+2)**2+4-25,x);assert all(S.simplify((r+2)**2+4-25)==0 for r in roots)
put('3.2',4,r'$x=-2\pm\sqrt{21}$',[combine,result(r'|\mathbf p+\mathbf q|^2=(x+2)^2+2^2=25\Rightarrow(x+2)^2=21')])
ab=M([7,9])-M([-3,5]);put('3.2',5,'$|AB|='+S.latex(ab.norm())+r',\quad \widehat{AB}='+v(ab/ab.norm())+'$',[position,unit,result(r'\overrightarrow{AB}=\langle10,4\rangle,\quad|AB|=\sqrt{116}=2\sqrt{29}')])
dd=M([-2,-3])+M([0,5])-M([1,4]);assert dd==M([-3,-2])
put('3.2',6,r'$D=(-3,-2)$',[step('The diagonals have the same midpoint, so A+C=B+D.','قطروں کا وسطی نقطہ ایک ہی ہے، اس لیے A+C=B+D۔','د قطرونو منځنی ټکی یو دی، نو A+C=B+D.',r'D=A+C-B=(-2,-3)+(0,5)-(1,4)=(-3,-2)')])
for part,pa,pb in [('i.',[-1,2],[2,-1]),('ii.',[-2,1],[2,3]),('iii.',[-1,1,2],[2,-1,3]),('iv.',[2,4,6],[1,-2,3])]:
    d=M(pb)-M(pa);put('3.2',7,r'$\overrightarrow{PQ}='+v(d)+r',\quad |PQ|='+S.latex(d.norm())+'$',[position,result(v(M(pb))+'-'+v(M(pa))+'='+v(d)),combine],part)
for part,d,known,mode in [('i.',[-2,3],[1,-2],'Q'),('ii.',[4,-5],[-1,1],'P'),('iii.',[-1,3,-2],[2,-1,-3],'Q'),('iv.',[2,-3,-4],[3,-1,4],'P')]:
    answer=M(known)+M(d) if mode=='Q' else M(known)-M(d)
    put('3.2',8,'$'+mode+'='+v(answer)+'$',[position,result((r'Q=P+\overrightarrow{PQ}' if mode=='Q' else r'P=Q-\overrightarrow{PQ}')+'='+v(answer))],part)
a=M([1,1,1]);b=M([4,-2,3]);c=M([1,-2,1]);d=2*a-b+3*c;res=6*d/d.norm();assert S.simplify(res.norm()-6)==0 and res.cross(d)==S.zeros(3,1)
put('3.2',9,r'$\pm'+v(res)+'$',[combine,result(r'2\mathbf a-\mathbf b+3\mathbf c='+v(d)+r',\quad|2\mathbf a-\mathbf b+3\mathbf c|='+S.latex(d.norm())),unit,step('Multiply the unit direction by 6. Both signs are parallel; the plus sign has the same direction.','اکائی سمت کو 6 سے ضرب دیں۔ دونوں نشان متوازی ہیں؛ مثبت نشان کی سمت یکساں ہے۔','واحد لوری په 6 ضرب کړئ. دواړه نښې موازي دي؛ مثبت نښه هماغه لوری لري.',r'\mathbf v=\pm6\frac{2\mathbf a-\mathbf b+3\mathbf c}{|2\mathbf a-\mathbf b+3\mathbf c|}')])
section=step('For PR:RQ=m:n, use the weighted position vectors; external division uses a difference.','PR:RQ=m:n کے لیے وزن دار مقامی سمتیے استعمال کریں؛ خارجی تقسیم میں فرق لیں۔','د PR:RQ=m:n لپاره وزن لرونکي موقعیت وېکټورونه وکاروئ؛ په بهرني وېش کې توپیر واخلئ.',r'\mathbf r_{\rm int}=\frac{n\mathbf p+m\mathbf q}{m+n},\quad \mathbf r_{\rm ext}=\frac{m\mathbf q-n\mathbf p}{m-n}')
pa=M([1,2,-1]);pb=M([-1,1,1]);put('3.2',10,r'$\mathbf r_{\rm int}='+v((pa+2*pb)/3)+r',\quad \mathbf r_{\rm ext}='+v(2*pb-pa)+'$',[section,result(r'\mathbf r_{\rm int}=\frac{\mathbf p+2\mathbf q}{3},\quad\mathbf r_{\rm ext}=2\mathbf q-\mathbf p')])
for part,pa,pb,m,n,external in [('(i)',[0,5],[4,1],2,5,False),('(ii)',[2,-3],[3,2],4,3,True)]:
    value=(m*M(pb)-n*M(pa))/(m-n) if external else (n*M(pa)+m*M(pb))/(m+n)
    put('3.2',11,'$'+v(value)+'$',[section,result(r'\mathbf r='+v(value))],part)
alpha=S.symbols('alpha');assert S.solve(alpha**2+(alpha+1)**2+4-9,alpha)==[-2,1]
put('3.2',12,r'$\alpha=1\ \text{or}\ -2$',[combine,result(r'\alpha^2+(\alpha+1)^2+4=9\Rightarrow2(\alpha+2)(\alpha-1)=0')])
assert M([2,3,4])+M([-1,3,-1])==M([1,6,3])
put('3.2',13,r'$z=3$',[step('The i and j components show that w=u+v. Thus its k component must also equal the sum. The directed sides closing the triangle are u, v and −w.','i اور j کے اجزا بتاتے ہیں کہ w=u+v ہے۔ اس لیے k کا جز بھی مجموعے کے برابر ہے۔ مثلث بند کرنے والے سمتی اضلاع u، v اور −w ہیں۔','د i او j مؤلفې ښيي چې w=u+v دی. نو د k مؤلفه هم د مجموعې سره برابره ده. د مثلث تړونکي لوري u، v او −w دي.',r'\mathbf u+\mathbf v=\langle1,6,3\rangle=\mathbf w\Rightarrow z=3')])
ab=M([3,1,0])-M([2,-1,1]);cd=M([-1,-2,1])-M([2,4,-2]);assert cd==-3*ab
put('3.2',14,r'$\overrightarrow{CD}=-3\overrightarrow{AB}$, hence parallel.',[position,result(r'\overrightarrow{AB}=\langle1,2,-1\rangle,\quad\overrightarrow{CD}=\langle-3,-6,3\rangle=-3\overrightarrow{AB}')])
A.save(['3.1','3.2'],[85,97,98])
