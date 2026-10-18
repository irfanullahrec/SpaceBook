from math11_answer_authoring import Author,step,S
from math11_matrix_solutions import tex,system_steps
A=Author(2);M=S.Matrix
def put(q,p,ans,steps,**meta):A.put('Review 2',q,p,ans,steps,**meta)
items=[
 ('(i)',r'(c) $14a+3c=10b$',r'2(7a-5b)-(-1)(3c)=0\Rightarrow14a-10b+3c=0','Expand the order-two determinant and rearrange.','درجہ دو کا مقطع کھولیں اور ترتیب بدلیں۔','د دویم ترتیب ډیټرمینانټ پراخ او بیا تنظیم کړئ.'),
 ('(ii)',r'(d) $a_{11}A_{11}+a_{21}A_{21}+a_{31}A_{31}$',r'|A|=\sum_{i=1}^3a_{i1}A_{i1}','Expand along the first column, pairing each entry with its own cofactor.','پہلے کالم کے لحاظ سے کھولیں اور ہر اندراج کو اس کے اپنے معاون مقطع سے ضرب دیں۔','د لومړۍ ستنې له مخې پراخ کړئ او هر عنصر له خپل کوفکټور سره ضرب کړئ.'),
 ('(iii)',r'(c) $\alpha=\pm3$',r'|A^3|=|A|^3=(\alpha^2-4)^3=125\Rightarrow\alpha^2-4=5\Rightarrow\alpha=\pm3','For real values of the parameter, take the real cube root, then solve the quadratic.','مقدار کی حقیقی قیمتوں کے لیے حقیقی مکعب جذر لیں، پھر دو درجی مساوات حل کریں۔','د پارامتر د حقیقي ارزښتونو لپاره حقیقي مکعبي جذر واخلئ، بیا دوه درجه یي معادله حل کړئ.'),
 ('(iv)','(b) $47$',r'|A^t|=|A|=47','Transposition preserves the determinant.','منقول لینے سے مقطع نہیں بدلتا۔','ترانسپوز ډیټرمینانټ نه بدلوي.'),
 ('(v)','(d) $1125$',r'\det(15A)=15^2\det A=225(5)=1125','For an order-two matrix, scaling the entire matrix scales its determinant by the square of the scalar.','درجہ دو کے قالب کو کسی عدد سے ضرب دینے پر مقطع اس عدد کے مربع سے ضرب پاتا ہے۔','د دویم ترتیب میټریکس په عدد ضربول د هغه ډیټرمینانټ د عدد په مربع ضربوي.'),
 ('(vi)',r'(c) $3^nI_2$',r'A=3I_2\Rightarrow A^n=(3I_2)^n=3^nI_2','The matrix is three times the identity.','قالب اکائی قالب کا تین گنا ہے۔','میټریکس د واحد میټریکس درې چنده دی.')
]
for p,ans,math,en,ur,ps in items:put('1',p,ans,[step(en,ur,ps,math)],category='mcqs')
ma=M([[-5,1],[6,-1],[-2,0]]);mb=M([[4,-5,-1],[5,6,1]]);mc=M([5,-4,1]);value=ma*mb*mc
assert ma*(mb*mc)==(ma*mb)*mc
put('2','','$'+tex(value)+'$',[step('Multiply the last two matrices first to obtain a two-entry column.','پہلے آخری دو قالبوں کو ضرب دیں تاکہ دو اندراجات کا کالم ملے۔','لومړی وروستي دوه میټریکسونه ضرب کړئ څو دوه عناصرو لرونکې ستن ترلاسه شي.',tex(mb)+tex(mc)+'='+tex(mb*mc)),step('Multiply the first matrix by this column.','پہلے قالب کو اس کالم سے ضرب دیں۔','لومړی میټریکس په دې ستن ضرب کړئ.',tex(ma)+tex(mb*mc)+'='+tex(value))])
ma=M([[1,2,2],[2,1,2],[2,2,1]]);assert ma**2-4*ma-5*S.eye(3)==S.zeros(3)
put('3','',r'$A^2-4A-5I=O$',[step('Compute $A^2$ and compare it with $4A+5I$.','$A^2$ معلوم کریں اور $4A+5I$ سے موازنہ کریں۔','$A^2$ محاسبه کړئ او له $4A+5I$ سره یې پرتله کړئ.',r'A^2='+tex(ma**2)+r'=4A+5I'),step('Subtracting the equal matrices gives the zero matrix.','برابر قالبوں کو تفریق کرنے سے صفر قالب ملتا ہے۔','د برابرو میټریکسونو په منفي کولو صفر میټریکس ترلاسه کېږي.')])
ma=M([[2,1,3],[0,4,6],[7,2,1]]);mb=M([[4,0,-1],[2,0,3],[-1,2,4]]);value=2*ma-mb**2
put('4','','$'+str(value.det())+'$',[step('Square $B$ by matrix multiplication, then form $2A-B^2$.','$B$ کو قالبی ضرب سے مربع کریں، پھر $2A-B^2$ بنائیں۔','$B$ د میټریکسي ضرب له لارې مربع کړئ، بیا $2A-B^2$ جوړ کړئ.',r'B^2='+tex(mb**2)+r',\quad2A-B^2='+tex(value)),step('Evaluate the determinant of the resulting matrix.','حاصل شدہ قالب کا مقطع معلوم کریں۔','د ترلاسه شوي میټریکس ډیټرمینانټ محاسبه کړئ.',r'|2A-B^2|='+str(value.det()))])
a=S.symbols('a');ma=M([[a*a+2*a,2*a+1,1],[2*a+1,a+2,1],[3,3,1]])
assert S.factor(ma.det())==(a-1)**3
put('5','',r'$(a-1)^3$',[step('Subtract the third row from the first and second rows. Then factor $a-1$ from both new rows.','تیسری قطار پہلی اور دوسری سے تفریق کریں۔ پھر دونوں نئی قطاروں سے $a-1$ مشترک لیں۔','درېیم قطار له لومړي او دویم څخه منفي کړئ. بیا له دواړو نوو قطارونو $a-1$ مشترک وباسئ.',r'D=(a-1)^2\begin{vmatrix}a+3&2&0\\2&1&0\\3&3&1\end{vmatrix}'),step('Expand along the last column and simplify.','آخری کالم کے لحاظ سے کھولیں اور مختصر کریں۔','د وروستۍ ستنې له مخې پراخ او ساده کړئ.',r'D=(a-1)^2[(a+3)-4]=(a-1)^3')])
ma=M([[3,1,-1],[0,1,2]]);left=ma*ma.T;right=ma.T*ma
assert left==left.T and right==right.T
put('6','',r'$(AA^t)^t=AA^t,\quad(A^tA)^t=A^tA$',[step('Compute both products. Each has mirrored entries across its main diagonal.','دونوں ضربیں معلوم کریں۔ ہر ایک میں مرکزی قطر کے دونوں طرف بالمقابل اندراجات برابر ہیں۔','دواړه ضربونه محاسبه کړئ. هر یو د اصلي قطر دواړو خواوو ته برابر مقابل عناصر لري.',r'AA^t='+tex(left)+r',\quad A^tA='+tex(right)),step('Thus both products are symmetric, although they have different orders.','پس دونوں ضربیں متناظر ہیں، اگرچہ ان کی ترتیبیں مختلف ہیں۔','نو دواړه ضربونه متناظر دي، که څه هم ترتیبونه یې توپیر لري.')])
ma=M([[4,3,3],[-1,0,-1],[-4,-4,-3]]);assert ma**2==S.eye(3)
put('7','',r'$A^{-1}=A$',[step('Multiply $A$ by itself. The product is the identity, so $A$ is its own inverse.','$A$ کو خود سے ضرب دیں۔ حاصل اکائی قالب ہے، اس لیے $A$ اپنا معکوس خود ہے۔','$A$ په خپل ځان ضرب کړئ. حاصل واحد میټریکس دی، نو $A$ د خپل ځان معکوس دی.',r'A^2='+tex(ma**2)+r'=I_3')])
ma=M([[4,3],[-2,1]]);inv=ma.inv()
put('8','','$'+tex(ma+10*inv)+'$',[step('The determinant is 10. Use the order-two inverse formula.','مقطع 10 ہے۔ درجہ دو کے معکوس کا کلیہ استعمال کریں۔','ډیټرمینانټ 10 دی. د دویم ترتیب معکوس فورمول وکاروئ.',r'A^{-1}=\frac1{10}\begin{bmatrix}1&-3\\2&4\end{bmatrix}'),step('Add $A$ to ten times the inverse.','$A$ میں معکوس کا دس گنا جمع کریں۔','په $A$ کې د معکوس لس چنده جمع کړئ.',r'A+10A^{-1}='+tex(ma+10*inv))])
ma=M([[1,1,1],[2,-3,1],[-1,2,-1]]);rhs=M([4,2,-1]);allsteps=[]
for method,en,ur,ps in [('inverse','Matrix inversion method','قالب کے معکوس کا طریقہ','د میټریکس د معکوس طریقه'),('both-gauss','Gauss elimination and Gauss–Jordan methods','گاؤس اخراج اور گاؤس–جارڈن طریقے','د ګاوس حذف او ګاوس–جورډن طریقې'),('cramer',"Cramer's rule",'کریمر کا قاعدہ','د کرامر قاعده')]:
    value,steps=system_steps(ma,rhs,method);allsteps.append(step(en,ur,ps));allsteps.extend(steps)
assert ma*value==rhs
answer='$'+r',\quad'.join(k+'='+S.latex(v) for k,v in zip('xyz',value))+'$'
put('9','',answer,allsteps)
A.save(['Review 2'],[75,76])
