from math11_answer_authoring import Author,step,S
from math11_matrix_solutions import tex,reduce_rows,inverse_steps,system_steps
A=Author(2);M=S.Matrix
for p,ma,reduced in [('(i)',M([[1,3,-1],[2,1,4],[3,4,-5]]),False),('(ii)',M([[2,3,-1,9],[1,-1,2,-3],[3,1,3,2]]),True),('(iii)',M([[2,-3,1],[1,1,2],[4,1,7]]),True),('(iv)',M([[1,0,-2],[2,1,1],[3,2,3]]),False)]:
    value,ops=reduce_rows(ma,reduced=reduced)
    A.put('2.3','1',p,'$'+tex(value)+'$',[step('Apply elementary row operations. An echelon form need not be unique.','ابتدائی قطاری اعمال لگائیں۔ زینہ دار شکل واحد ہونا ضروری نہیں۔','بنسټیز قطاري عملونه وکاروئ. د زینې بڼه لازماً یوازینۍ نه وي.',tex(ma))]+ops)
for p,ma in [('(i)',M([[4,-2,5],[2,1,0],[-1,2,3]])),('(ii)',M([[3,-1,6],[1,3,4],[-1,5,1]])),('(iii)',M([[1,2,-3],[0,-2,0],[-2,-2,2]])),('(iv)',M([[1,2,-1],[0,-1,3],[1,0,2]]))]:
    value,steps=inverse_steps(ma);A.put('2.3','2',p,'$A^{-1}='+tex(value)+'$',steps)
for q,p,ma in [('3','(i)',M([[1,0,-2],[2,2,1],[-1,2,3]])),('3','(ii)',M([[3,1,-4],[0,2,1],[1,-1,-2]])),('4','',M([[2,3,4,5],[3,4,5,6],[4,5,6,7],[9,10,11,12]]))]:
    value,ops=reduce_rows(ma,reduced=False);rank=sum(any(v!=0 for v in value.row(i)) for i in range(value.rows));assert rank==ma.rank()
    A.put('2.3',q,p,'$rank(A)='+str(rank)+'$',[step('Row-reduce the matrix and count the nonzero rows.','قالب کو قطاری اعمال سے مختصر کریں اور غیر صفر قطاریں گنیں۔','میټریکس په قطاري عملونو راکم کړئ او غیرصفر قطارونه وشمېرئ.',tex(ma))]+ops+[step('Rank is the number of nonzero rows in echelon form.','رتبہ زینہ دار شکل میں غیر صفر قطاروں کی تعداد ہے۔','رتبه په زینې بڼه کې د غیرصفر قطارونو شمېر دی.',r'rank(A)='+str(rank))])
cases=[
 ('1','(i)',M([[4,-3,1],[2,1,-4],[1,2,-2]]),M([11,-1,1]),'inverse'),
 ('1','(ii)',M([[1,1,1],[1,1,-2],[2,1,1]]),M([1,3,2]),'inverse'),
 ('2','(i)',M([[1,-1,4],[2,2,-1],[3,-2,3]]),M([4,2,-3]),'both-gauss'),
 ('2','(ii)',M([[2,4,-1],[1,-2,-2],[-5,-8,3]]),M([0,2,-2]),'both-gauss'),
 ('3','(i)',M([[1,-2,0],[3,1,0],[2,0,1]]),M([-4,-5,-1]),'cramer'),
 ('3','(ii)',M([[1,-1,2],[2,1,-2],[3,1,1]]),M([10,-4,7]),'cramer')]
for q,p,ma,rhs,method in cases:
    solution,steps=system_steps(ma,rhs,method)
    answer='$'+r',\quad'.join(k+'='+S.latex(v) for k,v in zip('xyz',solution))+'$'
    A.put('2.4',q,p,answer,steps)
for p,ma in [('(i)',M([[1,-1,1],[1,2,-1],[2,1,3]])),('(ii)',M([[1,1,2],[-2,1,-1],[-1,5,4]]))]:
    rr,ops=reduce_rows(ma);ns=ma.nullspace()
    if not ns:
        ans=r'$x_1=x_2=x_3=0$';last=step('There are no free variables, so only the zero solution exists.','کوئی آزاد متغیر نہیں، اس لیے صرف صفر حل موجود ہے۔','آزاد متغیر نشته، نو یوازې صفر حل شته.',ans.strip('$'))
    else:
        assert len(ns)==1 and ma*ns[0]==S.zeros(3,1)
        vec=ns[0]*S.ilcm(*[v.q for v in ns[0]]);assert ma*vec==S.zeros(3,1)
        ans='$'+r'\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=t'+tex(vec)+r',\quad t\in\mathbb R$'
        last=step('Use a free real parameter for the nullspace direction; zero is included when the parameter is zero.','عدم فضا کی سمت کے لیے آزاد حقیقی مقدار لیں؛ مقدار صفر ہونے پر صفر حل بھی شامل ہے۔','د صفر فضا د لوري لپاره آزاد حقیقي پارامتر وکاروئ؛ د پارامتر په صفر کې صفر حل هم شامل دی.',ans.strip('$'))
    A.put('2.4','4',p,ans,[step('Reduce the coefficient matrix; every right-hand side is zero.','سر کا قالب مختصر کریں؛ دائیں طرف ہر قیمت صفر ہے۔','ضریبي میټریکس راکم کړئ؛ د ښي خوا ټول ارزښتونه صفر دي.',tex(ma))]+ops+[last])
lam=S.symbols('lambda');ma=M([[1,5,3],[5,1,-lam],[1,2,lam]])
assert S.simplify(ma.det()+27*(lam-1))==0
vec=M([1,-2,3]);assert ma.subs(lam,1)*vec==S.zeros(3,1)
A.put('2.4','5','',r'$\lambda=1,\quad(x_1,x_2,x_3)=t(1,-2,3),\ t\in\mathbb R$; non-trivial when $t\ne0$.',[step('A homogeneous square system has a nonzero solution only when its coefficient determinant is zero.','ہم جنس مربع نظام کا غیر صفر حل صرف اس وقت ہوتا ہے جب سر کے قالب کا مقطع صفر ہو۔','همجنس مربع سیستم یوازې هغه وخت غیرصفر حل لري چې د ضریبي میټریکس ډیټرمینانټ صفر وي.',r'\det A=-27(\lambda-1)=0\Rightarrow\lambda=1'),step('With this value, row reduction gives $x_1=x_3/3$ and $x_2=-2x_3/3$. Set $x_3=3t$.','اس قیمت پر قطاری اختصار سے $x_1=x_3/3$ اور $x_2=-2x_3/3$ ملتے ہیں۔ $x_3=3t$ رکھیں۔','په دې ارزښت قطاري کمول $x_1=x_3/3$ او $x_2=-2x_3/3$ ورکوي. $x_3=3t$ ونیسئ.',r'(x_1,x_2,x_3)=t(1,-2,3),\quad t\ne0\text{ for a non-trivial solution}')],answerUr=r'$\lambda=1,\ (x_1,x_2,x_3)=t(1,-2,3),\ t\in\mathbb R$؛ غیر معمولی حل کے لیے $t\ne0$۔',answerPs=r'$\lambda=1,\ (x_1,x_2,x_3)=t(1,-2,3),\ t\in\mathbb R$؛ د غیرصفر حل لپاره $t\ne0$.')
A.save(['2.3','2.4'],[60,74])
