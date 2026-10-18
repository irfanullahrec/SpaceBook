from math11_answer_authoring import Author,step,S
A=Author(2);M=S.Matrix;R=S.Rational
def tex(m):return r'\begin{bmatrix}'+r'\\'.join('&'.join(S.latex(v) for v in row) for row in m.tolist())+r'\end{bmatrix}'
def result(q,p,m,work,method=None):
    A.put('2.1',q,p,'$'+tex(m)+'$',[method or step('Use row-by-column multiplication and combine corresponding entries.','قطار کو کالم سے ضرب دیں اور متعلقہ اندراجات یکجا کریں۔','قطار په ستن ضرب کړئ او اړوند عناصر راټول کړئ.'),step('The calculation gives this matrix.','حساب سے یہ قالب حاصل ہوتا ہے۔','له محاسبې دا میټریکس ترلاسه کېږي.',work+'='+tex(m))])
m1=M([[1,2,4]]);m2=M([[1,0,2],[2,0,1],[0,1,2]]);m3=M([2,4,6])
result('1','(i)',m1*m2*m3,tex(m1*m2)+tex(m3))
m1=M([[1,-2,3]]);m2=M([[2,-1,5],[0,2,4],[-7,5,0]]);m3=M([[2,-5,7]])
result('1','(ii)',m1*m2-m3,tex(m1*m2)+'-'+tex(m3))
m1=M([[7,1,2],[9,2,1]]);m2=M([3,4,5]);m3=M([4,2])
result('1','(iii)',m1*m2+2*m3,tex(m1*m2)+'+2'+tex(m3))
m1=M([[1,3],[-1,-4]])+M([[3,-2],[-1,1]]);m2=M([[1,3,5],[2,4,6]])
result('1','(iv)',m1*m2,tex(m1)+tex(m2))
m1=M([[2,-5,1],[3,0,-4]]);m2=M([[1,-2,-3],[0,-1,5]]);m3=M([[0,1,-2],[0,-1,-1]])
result('2','',2*m1+3*m2-4*m3,'2'+tex(m1)+'+3'+tex(m2)+'-4'+tex(m3),step('Multiply every entry by its scalar, then add or subtract matching positions.','ہر اندراج کو اس کے عددی عامل سے ضرب دیں، پھر متعلقہ جگہوں کے اندراجات جمع یا تفریق کریں۔','هر عنصر په خپل عددي ضریب ضرب کړئ، بیا د ورته ځایونو عناصر جمع یا منفي کړئ.'))
a,b,c,f,g,h,x,y,z=S.symbols('a b c f g h x y z')
ma=M([[x,y,z]]);mb=M([[a,h,g],[h,b,f],[g,f,c]]);mc=M([x,y,z])
assert (ma*mb)*mc==ma*(mb*mc)
common=S.expand(((ma*mb)*mc)[0])
result('3','(i)',M([common]),r'(AB)C=A(BC)',step('Compute the intermediate row $AB$ and column $BC$. Each multiplication gives the same scalar matrix.','درمیانی قطار $AB$ اور کالم $BC$ معلوم کریں۔ دونوں ضربیں ایک ہی عددی قالب دیتی ہیں۔','منځنی قطار $AB$ او ستن $BC$ محاسبه کړئ. دواړه ضربونه یو شان عددي میټریکس ورکوي.'))
ma=M([[1,3],[-1,4]]);mb=M([[2,1,-3],[0,4,2]]);mc=M([[3,-1,5],[2,1,0]])
assert ma*(mb+mc)==ma*mb+ma*mc and ma*(mb-mc)==ma*mb-ma*mc
A.put('2.1','3','(ii)','$'+r'A(B+C)=AB+AC='+tex(ma*(mb+mc))+r',\quad A(B-C)=AB-AC='+tex(ma*(mb-mc))+'$',[step('Compute $AB$ and $AC$, then their sum and difference; compare with multiplying $A$ by $B+C$ and $B-C$.','$AB$ اور $AC$ معلوم کریں، پھر ان کا مجموعہ اور فرق لیں؛ $A$ کی $B+C$ اور $B-C$ سے ضرب سے موازنہ کریں۔','$AB$ او $AC$ محاسبه کړئ، بیا یې مجموعه او توپیر واخلئ؛ له $B+C$ او $B-C$ سره د $A$ له ضرب سره یې پرتله کړئ.',r'AB='+tex(ma*mb)+r',\quad AC='+tex(ma*mc)),step('Both distributive identities are verified.','دونوں تقسیمی مماثلتوں کی تصدیق ہوتی ہے۔','دواړه وېشونکې مطابقتونه تصدیق کېږي.',r'A(B+C)='+tex(ma*(mb+mc))+r',\quad A(B-C)='+tex(ma*(mb-mc)))])
ma=M([[1,4,4],[4,1,4],[4,4,1]]);assert ma**2/3-2*ma-9*S.eye(3)==S.zeros(3)
A.put('2.1','4','',r'$\frac13A^2-2A-9I=O$',[step('Square the matrix by row-by-column multiplication.','قطار کو کالم سے ضرب دے کر قالب کا مربع معلوم کریں۔','د قطار او ستن په ضرب د میټریکس مربع محاسبه کړئ.',r'A^2='+tex(ma**2)),step('Substitute and subtract corresponding entries; every entry is zero.','قیمت رکھیں اور متعلقہ اندراجات تفریق کریں؛ ہر اندراج صفر ہے۔','ارزښت ځای پر ځای او اړوند عناصر منفي کړئ؛ هر عنصر صفر دی.',r'\frac13A^2-2A-9I='+tex(S.zeros(3)))])
A.put('2.1','5','',r'$a=-\frac23,\quad b=\frac32$',[step('In a symmetric matrix, entries mirrored across the main diagonal are equal.','متناظر قالب میں مرکزی قطر کے دونوں طرف بالمقابل اندراجات برابر ہوتے ہیں۔','په متناظر میټریکس کې د اصلي قطر دواړو خواوو ته مقابل عناصر برابر دي.',r'2b=3,\quad 3a=-2,\quad 3=3'),step('Solve the two scalar equations.','دونوں عددی مساواتیں حل کریں۔','دواړه عددي معادلې حل کړئ.',r'b=\frac32,\quad a=-\frac23')])
for p,ma,mb,coef in [('(i)',M([[1,0,3],[-2,2,1]]),M([[2,1,1],[3,-1,4]]),3),('(ii)',M([[1,2,2],[3,-1,2]]),M([[4,6,2],[0,-4,2]]),1)]:
    value=3*ma+2*mb if p=='(i)' else ma+mb/2
    assert (value-3*ma==2*mb) if p=='(i)' else (2*(value-ma)==mb)
    result('6',p,value,r'X=3A+2B' if p=='(i)' else r'X=A+\frac12B',step('Isolate $X$ using the same matrix operation on both sides.','$X$ کو دونوں طرف ایک جیسا قالبی عمل کر کے الگ کریں۔','پر دواړو خواوو د ورته میټریکسي عمل په کولو $X$ جلا کړئ.'))
ma=M([[1,0,-1,2],[3,1,2,5],[0,-2,1,6]]);mb=M([[2,-1,3,1],[1,3,-1,4],[3,1,2,-1]])
assert (ma+mb).T==ma.T+mb.T
result('7','',(ma+mb).T,r'(A+B)^t=A^t+B^t',step('Add corresponding entries, then interchange rows and columns. Transposing first and adding gives the same matrix.','متعلقہ اندراجات جمع کریں، پھر قطاریں اور کالم بدلیں۔ پہلے منقول لینے اور پھر جمع کرنے سے بھی یہی قالب ملتا ہے۔','اړوند عناصر جمع کړئ، بیا قطارونه او ستنې سره بدل کړئ. لومړی ترانسپوز او بیا جمع کول همدا میټریکس ورکوي.'))
ma=M([[1,2,0],[3,-1,4]])
result('8','(i)',ma,r'(A^t)^t',step('Transposing twice restores the original rows and columns.','دو بار منقول لینے سے اصل قطاریں اور کالم واپس آتے ہیں۔','دوه ځله ترانسپوز اصلي قطارونه او ستنې بېرته راولي.'))
A.put('2.1','8','(ii)',r'$AA^t\ne A^tA$',[step('The first product has order $2\\times2$; the second has order $3\\times3$, so they cannot be equal.','پہلی ضرب کی ترتیب $2\\times2$ اور دوسری کی $3\\times3$ ہے، اس لیے وہ برابر نہیں ہو سکتیں۔','د لومړي ضرب ترتیب $2\\times2$ او د دویم $3\\times3$ دی، نو برابرېدای نشي.',r'AA^t='+tex(ma*ma.T)+r',\quad A^tA='+tex(ma.T*ma))])
for p,ma,mb in [('(i)',M([[2,-1,3],[1,0,1]]),M([[1,2],[2,2],[3,0]])),('(ii)',M([[1,2,0],[-1,1,4]]),M([[1,1],[2,3],[1,-2]]))]:
    assert (ma*mb).T==mb.T*ma.T
    result('9',p,(ma*mb).T,r'(AB)^t=B^tA^t',step('Multiply, then transpose; independently multiply the transposes in reverse order.','ضرب دیں، پھر منقول لیں؛ الگ سے منقول قالبوں کو الٹی ترتیب میں ضرب دیں۔','ضرب وکړئ، بیا ترانسپوز واخلئ؛ جلا ترانسپوزونه په معکوس ترتیب ضرب کړئ.'))
ma=M([[1,-3,4],[-3,2,-5],[4,-5,0]]);mb=M([[5,6,7],[6,-8,3],[7,3,1]])
assert ma.T==ma and mb.T==mb and (ma+mb).T==ma+mb
A.put('2.1','10','',r'$A^t=A,\quad B^t=B,\quad(A+B)^t=A+B$',[step('Check the matching entries across each main diagonal.','ہر مرکزی قطر کے دونوں طرف بالمقابل اندراجات دیکھیں۔','د هر اصلي قطر دواړو خواوو ته مقابل عناصر وګورئ.',r'A+B='+tex(ma+mb)),step('All three matrices equal their transposes, so all are symmetric.','تینوں قالب اپنے منقول کے برابر ہیں، اس لیے سب متناظر ہیں۔','درې واړه میټریکسونه له خپلو ترانسپوزونو سره برابر دي، نو ټول متناظر دي.')])
ma=M([[0,1,-2],[-1,0,3],[2,-3,0]]);mb=M([[0,-6,11],[6,0,-7],[-11,7,0]])
assert (ma+mb).T==-(ma+mb)
A.put('2.1','11','',r'$(A+B)^t=-(A+B)$',[step('Add the matrices. Transposing the sum reverses every entry sign.','قالب جمع کریں۔ مجموعے کا منقول لینے سے ہر اندراج کی علامت بدلتی ہے۔','میټریکسونه جمع کړئ. د مجموعې ترانسپوز د هر عنصر نښه بدلوي.',r'A+B='+tex(ma+mb)+r',\quad(A+B)^t='+tex((ma+mb).T)),step('Therefore the sum is skew-symmetric.','لہٰذا مجموعہ خلاف متناظر ہے۔','له همدې امله مجموعه ضد متناظره ده.')])
ma=M([[3,2,1],[4,5,6],[-2,3,4]])
assert (ma+ma.T).T==ma+ma.T and (ma-ma.T).T==-(ma-ma.T)
A.put('2.1','12','',r'$(A+A^t)^t=A+A^t;\quad(A-A^t)^t=-(A-A^t)$',[step('Compute the sum and difference explicitly.','مجموعہ اور فرق واضح طور پر معلوم کریں۔','مجموعه او توپیر په څرګند ډول محاسبه کړئ.',r'A+A^t='+tex(ma+ma.T)+r',\quad A-A^t='+tex(ma-ma.T)),step('The sum equals its transpose; the difference equals the negative of its transpose.','مجموعہ اپنے منقول کے برابر ہے؛ فرق اپنے منقول کے منفی کے برابر ہے۔','مجموعه له خپل ترانسپوز سره برابره ده؛ توپیر د خپل ترانسپوز له منفي سره برابر دی.')])
A.put('2.1','13','',r'$A+A^t$ is symmetric; $A-A^t$ is skew-symmetric.',[step('Use the transpose rules and the fact that transposing twice returns $A$.','منقول کے قواعد اور دو بار منقول لینے سے $A$ واپس آنے کی خاصیت استعمال کریں۔','د ترانسپوز قواعد او دا ځانګړنه وکاروئ چې دوه ځله ترانسپوز $A$ بېرته ورکوي.',r'\begin{aligned}(A+A^t)^t&=A^t+(A^t)^t=A^t+A=A+A^t\\(A-A^t)^t&=A^t-(A^t)^t=A^t-A=-(A-A^t)\end{aligned}')],answerUr=r'$A+A^t$ متناظر اور $A-A^t$ خلاف متناظر ہے۔',answerPs=r'$A+A^t$ متناظر او $A-A^t$ ضد متناظر دی.')
A.save(['2.1'],[41,42,43])
