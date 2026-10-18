from math11_answer_authoring import Author,RULES,step,S
A=Author(1);I=S.I;R=S.Rational;rt=S.sqrt;a,b=S.symbols('a b',real=True)
for p,e,v,w in [('(i)',I**9+I**19,0,r'i^9+i^{19}=i-i=0'),('(ii)',(-I)**23,I,r'(-i)^{23}=(-i)^{20}(-i)^3=i'),('(iii)',(-S.Integer(1))**R(-23,2),I,r'(-1)^{-23/2}=i^{-23}=i'),('(iv)',(-S.Integer(1))**R(15,2),-I,r'(-1)^{15/2}=i^{15}=-i')]:
    A.calc('1.1','1',p,e,v,'powers',w)
    if p in ('(iii)','(iv)'):A.answers[f'1.1|1|{p}']['steps'].insert(0,step(r'Use the principal square root $\sqrt{-1}=i$.',r'اصلی مربع جذر $\sqrt{-1}=i$ استعمال کریں۔',r'اصلي مربع جذر $\sqrt{-1}=i$ وکاروئ.'))
A.calc('1.1','2','',I**107+I**112+I**122+I**153,0,'powers',r'i^{107}+i^{112}+i^{122}+i^{153}=-i+1-1+i=0')
for p,e,v,w in [('(i)',3*(1+2*I)-2*(1-3*I),1+12*I,r'(3+6i)+(-2+6i)=1+12i'),('(ii)',R(1,2)-R(2,3)*I+R(1,4)-R(1,3)*I,R(3,4)-I,r'(\tfrac12+\tfrac14)+(-\tfrac23-\tfrac13)i=\tfrac34-i'),('(iii)',rt(2)+I+1+rt(2)*I,(1+rt(2))+(1+rt(2))*I,r'(\sqrt2+1)+(1+\sqrt2)i')]:A.calc('1.1','3',p,e,v,'add',w)
for p,e,v,w in [('(i)',a-(2-b*I),a-2+b*I,r'(a,0)-(2,-b)=(a-2,b)'),('(ii)',-3+I/2-(3+I/2),-6,r'(-3,\tfrac12)-(3,\tfrac12)=(-6,0)'),('(iii)',3*rt(3)-5*rt(7)*I-(rt(3)+2*rt(7)*I),2*rt(3)-7*rt(7)*I,r'(3\sqrt3-\sqrt3)+(-5\sqrt7-2\sqrt7)i=2\sqrt3-7\sqrt7i')]:A.calc('1.1','4',p,e,v,'subtract',w)
for p,e,v,w in [('(i)',(11+8*I)*(-7+5*I),-117-I,r'-77+55i-56i+40i^2=-117-i'),('(ii)',3*I*2*(1-I),6+6*I,r'6i-6i^2=6+6i'),('(iii)',(rt(2)+rt(3)*I)*(2*rt(2)-rt(3)*I),7+rt(6)*I,r'4-\sqrt6i+2\sqrt6i-3i^2=7+\sqrt6i')]:A.calc('1.1','5',p,e,v,'multiply',w)
for p,e,v,w in [('(i)',(4+I)/(3+5*I),(1-I)/2,r'\frac{(4+i)(3-5i)}{34}=\frac{17-17i}{34}=\frac12-\frac12i'),('(ii)',1/(-8+I),(-8-I)/65,r'\frac{-8-i}{(-8)^2+1^2}=-\frac8{65}-\frac1{65}i'),('(iii)',1/(7-3*I),(7+3*I)/58,r'\frac{7+3i}{7^2+3^2}=\frac7{58}+\frac3{58}i'),('(iv)',(6+I)/I,1-6*I,r'\frac{(6+i)(-i)}{i(-i)}=1-6i')]:A.calc('1.1','6',p,e,v,'divide',w)
for p,e,v,w in [('(i)',abs(1+2*I+2+3*I),rt(34),r'|3+5i|=\sqrt{3^2+5^2}=\sqrt{34}'),('(ii)',abs((1+2*I)*(2+3*I)),rt(65),r'|-4+7i|=\sqrt{16+49}=\sqrt{65}'),('(iii)',abs((1+2*I)/(2+3*I)),rt(65)/13,r'\left|\frac{8+i}{13}\right|=\frac{\sqrt{65}}{13}=\sqrt{\frac5{13}}')]:A.calc('1.1','7',p,e,v,'modulus',w)
for p,e,v,w in [('(i)',(1-2*I)/(2+I)+(4-I)/(3+2*I),(10-24*I)/13,r'-i+\frac{10-11i}{13}=\frac{10}{13}-\frac{24}{13}i'),('(ii)',(2+3*I)/(-5-4*I),(-22-7*I)/41,r'\frac{(2+3i)(-5+4i)}{41}=\frac{-22-7i}{41}'),('(iii)',(1+I)**2/(4+3*I),(6+8*I)/25,r'\frac{2i(4-3i)}{25}=\frac6{25}+\frac8{25}i')]:A.calc('1.1','8',p,e,v,'divide',w)
A.calc('1.1','9','',S.conjugate((3-2*I)*(2+3*I)/((1+2*I)*(2-I))),(63+16*I)/25,'conjugate',r'\frac{12+5i}{4+3i}=\frac{63-16i}{25}\quad\Rightarrow\quad\overline z=\frac{63+16i}{25}')
A.calc('1.1','10','',(I**18+(1/I)**25)**3,2-2*I,'powers',r'[-1-i]^3=(-1-i)^2(-1-i)=2i(-1-i)=2-2i')
A.calc('1.1','11','(i)',S.re((2-I)*(-2+I)/(2+I)),-R(2,5),'parts',r'\frac{z_1z_2}{\bar z_1}=\frac{-2+11i}{5}\quad\Rightarrow\quad Re=-\frac25')
A.calc('1.1','11','(ii)',S.im(1/((2-I)*(2+I))),0,'parts',r'\frac1{z_1\bar z_1}=\frac15\quad\Rightarrow\quad Im=0')
mcqs=[('(i)','(b) $2i$',r'\frac{2i}{1+i}=1+i,\quad(1+i)^2=2i','divide'),('(ii)',r'(c) $\frac{14}{25}+\frac{23}{25}i$',r'\frac{(5+2i)(4+3i)}{25}=\frac{14+23i}{25}','divide'),('(iii)','(a) $0$',r'i^{57}+\frac1{i^{25}}=i+\frac1i=i-i=0','powers'),('(iv)','(d): depends on whether $n$ is even or odd.',r'\sum_{k=0}^{n}i^{2k}=\sum_{k=0}^{n}(-1)^k=\begin{cases}1&n\text{ even}\\0&n\text{ odd}\end{cases}','powers'),('(v)','(a) X-axis ($y=0$).',r'|z-5i|^2=|z+5i|^2\Rightarrow x^2+(y-5)^2=x^2+(y+5)^2\Rightarrow y=0','modulus'),('(vi)',r'(b) $\frac{3+2i}{13}$',r'\frac1{3-2i}=\frac{3+2i}{(3-2i)(3+2i)}=\frac{3+2i}{13}','divide'),('(vii)',r'(b) $x=\frac5{13},\ y=\frac{14}{13}$',r'x+iy=\frac{4+i}{2-3i}=\frac{(4+i)(2+3i)}{13}=\frac5{13}+\frac{14}{13}i','divide')]
for p,answer,work,rule in mcqs:A.put('Review 1','1',p,answer,[RULES[rule],step('Compare the simplified value with the printed options.','مختصر قیمت کا مطبوعہ اختیارات سے موازنہ کریں۔','ساده شوی ارزښت له چاپ شوو انتخابونو سره پرتله کړئ.',work)],'mcqs')
A.answers['Review 1|1|(iv)'].update(answerUr='(d): اس کا انحصار $n$ کے جفت یا طاق ہونے پر ہے۔',answerPs='(d): دا د $n$ په جفت یا طاق والي پورې تړاو لري.')
A.answers['Review 1|1|(iv)']['steps'].append(step('There are $n+1$ alternating terms. The sum is 1 for even $n$ and 0 for odd $n$, so it is not always positive or always zero.','مخالف علامتوں والے $n+1$ اجزا ہیں۔ جفت $n$ کے لیے مجموعہ 1 اور طاق $n$ کے لیے 0 ہے؛ یہ ہمیشہ مثبت یا ہمیشہ صفر نہیں ہے۔','دلته $n+1$ متناوب حدونه شته. د جفت $n$ لپاره مجموعه 1 او د طاق $n$ لپاره 0 ده؛ دا تل مثبته یا تل صفر نه ده.'))
A.answers['Review 1|1|(v)'].update(answerUr='(a) X-محور ($y=0$)۔',answerPs='(a) X-محور ($y=0$).')
assert S.simplify((2*I/(1+I))**2-2*I)==0
assert S.simplify((5+2*I)/(4-3*I)-(14+23*I)/25)==0
assert I**57+1/I**25==0
assert S.simplify(1/(3-2*I)-(3+2*I)/13)==0
assert S.simplify((4+I)/(2-3*I)-(5+14*I)/13)==0
A.put('Review 1','2','','$0$',[RULES['powers'],step('Factor out $i^n$. The remaining four powers sum to zero.','$i^n$ مشترک لیں۔ باقی چار قوتوں کا مجموعہ صفر ہے۔','$i^n$ مشترک وباسئ. د پاتې څلورو قوو مجموعه صفر ده.',r'i^n(1+i+i^2+i^3)=i^n(1+i-1-i)=0')])
for p,e,v,w,rule in [('(i)',1+3*I+5+7*I,6+10*I,r'(1+5)+(3+7)i=6+10i','add'),('(ii)',1+3*I-(5+7*I),-4-4*I,r'(1-5)+(3-7)i=-4-4i','subtract'),('(iii)',(1+3*I)*(5+7*I),-16+22*I,r'5+7i+15i+21i^2=-16+22i','multiply'),('(iv)',(1+3*I)/(5+7*I),(13+4*I)/37,r'\frac{(1+3i)(5-7i)}{74}=\frac{26+8i}{74}=\frac{13+4i}{37}','divide')]:A.calc('Review 1','3',p,e,v,rule,w)
A.calc('Review 1','4','',abs(((2-I)+(1+I)+1)/((2-I)-(1+I)+1)),rt(2),'modulus',r'\left|\frac4{2-2i}\right|=|1+i|=\sqrt2')
A.calc('Review 1','5','',abs((1+I)/(1-I)-(1-I)/(1+I)),2,'modulus',r'\frac{1+i}{1-i}-\frac{1-i}{1+i}=i-(-i)=2i,\quad|2i|=2')
A.calc('Review 1','6','',S.conjugate(1/(3+4*I)),(3+4*I)/25,'conjugate',r'\frac1{3+4i}=\frac{3-4i}{25}\quad\Rightarrow\quad\overline z=\frac{3+4i}{25}')
A.calc('Review 1','7','',(3-2*I)/(2+3*I),-I,'divide',r'z^{-1}=\frac{3-2i}{2+3i}=\frac{(3-2i)(2-3i)}{13}=-i')
assert all(S.simplify(v+2/v-2)==0 for v in [1+I,1-I])
A.put('Review 1','8','',r'$z=1+i,\ 1-i$',[step(r'The denominator requires $z\ne0$. Multiply by $z$ and solve the quadratic.',r'مخرج کی وجہ سے $z\ne0$ لازم ہے۔ $z$ سے ضرب دیں اور دو درجی مساوات حل کریں۔',r'د مخرج له امله $z\ne0$ اړین دی. په $z$ ضرب کړئ او دوه درجه یي معادله حل کړئ.',r'z^2-2z+2=0\quad\Rightarrow\quad z=\frac{2\pm\sqrt{-4}}2=1\pm i'),step('Both roots are nonzero and satisfy the original equation.','دونوں جذر غیر صفر ہیں اور اصل مساوات کو پورا کرتے ہیں۔','دواړه جذرونه غیرصفر دي او اصلي معادله پوره کوي.')])
A.save(['1.1','Review 1'],[10,11,27,28])
