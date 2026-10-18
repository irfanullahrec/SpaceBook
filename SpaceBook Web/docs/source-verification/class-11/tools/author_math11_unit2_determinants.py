from math11_answer_authoring import Author,step,S
A=Author(2);M=S.Matrix
def det(m):return r'\begin{vmatrix}'+r'\\'.join('&'.join(S.latex(v) for v in row) for row in m.tolist())+r'\end{vmatrix}'
def put(q,p,ans,steps,ur=None,ps=None):A.put('2.2',q,p,ans,steps,answerUr=ur,answerPs=ps)
ma=M([[1,3,1],[-1,2,0],[2,0,-2]])
positions=[(0,0),(1,0),(1,2),(2,0),(2,1),(2,2)]
cof=',\\quad'.join(fr'A_{{{r+1}{c+1}}}={ma.cofactor(r,c)}' for r,c in positions)
put('1','','$'+cof+fr',\quad|A|={ma.det()}$',[step(r'A cofactor is $A_{ij}=(-1)^{i+j}M_{ij}$; delete row $i$ and column $j$ to form its minor.',r'معاون مقطع $A_{ij}=(-1)^{i+j}M_{ij}$ ہے؛ اس کے ذیلی مقطع کے لیے قطار $i$ اور کالم $j$ حذف کریں۔',r'کوفکټور $A_{ij}=(-1)^{i+j}M_{ij}$ دی؛ د هغه د ماینر لپاره قطار $i$ او ستن $j$ لرې کړئ.',cof),step('Expand the determinant along the first row.','پہلی قطار کے لحاظ سے مقطع کھولیں۔','ډیټرمینانټ د لومړي قطار له مخې پراخ کړئ.',fr'|A|=1({ma.cofactor(0,0)})+3({ma.cofactor(0,1)})+1({ma.cofactor(0,2)})={ma.det()}')])
reasons=[
 ('(i)','The third column is zero.','تیسرا کالم صفر ہے۔','درېیمه ستن صفر ده.',r'C_3=0\Rightarrow |A|=0'),
 ('(ii)','The second row is -4 times the third row, so two rows are proportional.','دوسری قطار تیسری قطار کا -4 گنا ہے، اس لیے دو قطاریں متناسب ہیں۔','دویم قطار د درېیم قطار -4 چنده دی، نو دوه قطارونه متناسب دي.',r'R_2=-4R_3\Rightarrow |A|=0'),
 ('(iii)','The right matrix is the transpose of the left; transposition preserves the determinant.','دائیں قالب بائیں کا منقول ہے؛ منقول لینے سے مقطع نہیں بدلتا۔','ښی میټریکس د کیڼ ترانسپوز دی؛ ترانسپوز ډیټرمینانټ نه بدلوي.',r'|A^t|=|A|'),
 ('(iv)','Factor -3 out of the third column.','تیسرے کالم سے -3 مشترک لیں۔','له درېیمې ستنې -3 مشترک وباسئ.',r'\begin{bmatrix}0\\-3\\-6\end{bmatrix}=-3\begin{bmatrix}0\\1\\2\end{bmatrix}'),
 ('(v)','The second and third rows are interchanged, which changes the determinant sign.','دوسری اور تیسری قطاروں کی جگہ بدلی گئی ہے، جس سے مقطع کی علامت بدلتی ہے۔','دویم او درېیم قطارونه بدل شوي، چې د ډیټرمینانټ نښه بدلوي.',r'R_2\leftrightarrow R_3\Rightarrow D_{\rm right}=-D_{\rm left}'),
 ('(vi)','The new second row is the old second row plus twice the third row. This leaves the determinant unchanged.','نئی دوسری قطار پرانی دوسری قطار اور تیسری قطار کے دو گنے کا مجموعہ ہے۔ اس سے مقطع نہیں بدلتا۔','نوی دویم قطار زوړ دویم قطار جمع د درېیم قطار دوه چنده دی. دا ډیټرمینانټ نه بدلوي.',r'R_2\to R_2+2R_3:\quad(3,1,2)+2(1,2,2)=(5,5,6)')
]
for p,en,ur,ps,work in reasons:put('2',p,en,[step(en,ur,ps,work)],ur,ps)
aa,bb,cc,dd,ee,ff,gg,hh,kk=S.symbols('a b c d e f g h k')
general=M([[aa,bb,cc],[dd,ee,ff],[gg,hh,kk]])
assert general.det()==general.T.det()
put('3','',r'$|A^t|=|A|$',[step('Write a general order-three matrix and expand both determinants. The same six products occur.','درجہ تین کا عمومی قالب لکھیں اور دونوں مقطع کھولیں۔ وہی چھ ضربیں حاصل ہوتی ہیں۔','د درېیم ترتیب عمومي میټریکس ولیکئ او دواړه ډیټرمینانټونه پراخ کړئ. هماغه شپږ ضربونه راځي.',r'A=\begin{bmatrix}a&b&c\\d&e&f\\g&h&k\end{bmatrix},\quad|A|=|A^t|=aek+bfg+cdh-ceg-bdk-afh')])
for p,ma in [('(i)',M([[0,1,3],[-1,2,1],[2,1,1]])),('(ii)',M([[3,4,-2],[2,4,-6],[-4,2,0]])),('(iii)',M([[3,1,2],[6,-5,4],[-9,8,-7]])),('(iv)',M([[2,1,-3],[1,1,0],[-2,3,4]]))]:
    terms='+'.join(fr'({ma[0,c]})({ma.cofactor(0,c)})' for c in range(3))
    assert sum(ma[0,c]*ma.cofactor(0,c) for c in range(3))==ma.det()
    put('4',p,'$'+str(ma.det())+'$',[step('Expand along the first row using the signed cofactors.','علامتوں والے معاون مقطع استعمال کر کے پہلی قطار کے لحاظ سے کھولیں۔','د نښه لرونکو کوفکټورونو په کارولو د لومړي قطار له مخې پراخ کړئ.',det(ma)+'='+terms+'='+str(ma.det()))])
a,b,c,l,m,n,x,y,z=S.symbols('a b c l m n x y z')
ma=M([[a,b,c],[l,m,n],[x,y,z]]);assert ma.det()==ma.T.det()
put('5','(i)',r'$|A|=|A^t|$',[step('The right determinant is the transpose of the left, so their values agree.','دائیں مقطع بائیں کا منقول ہے، اس لیے دونوں کی قیمت برابر ہے۔','ښی ډیټرمینانټ د کیڼ ترانسپوز دی، نو ارزښتونه یې برابر دي.',det(ma)+'='+det(ma.T))])
ma=M([[a,b,c],[1-3*a,2-3*b,3-3*c],[4,5,6]]);mb=M([[a,b,c],[1,2,3],[4,5,6]])
assert S.expand(ma.det()-mb.det())==0
put('5','(ii)',r'$D_{\rm left}=D_{\rm right}$',[step('Add three times the first row to the second row. This row operation preserves the determinant.','پہلی قطار کا تین گنا دوسری قطار میں جمع کریں۔ اس قطاری عمل سے مقطع نہیں بدلتا۔','د لومړي قطار درې چنده په دویم قطار کې جمع کړئ. دا قطاري عمل ډیټرمینانټ نه بدلوي.',r'R_2\to R_2+3R_1:\quad(1-3a,2-3b,3-3c)+3(a,b,c)=(1,2,3)')])
ma=M([[1,1,1],[a,b,c],[b+c,c+a,a+b]]);assert ma.det()==0
put('5','(iii)','$0$',[step('Add row two to row three; row three becomes a multiple of row one. Two proportional rows give a zero determinant.','دوسری قطار تیسری میں جمع کریں؛ تیسری قطار پہلی کا مضرب بن جاتی ہے۔ دو متناسب قطاروں کا مقطع صفر ہوتا ہے۔','دویم قطار په درېیم کې جمع کړئ؛ درېیم قطار د لومړي مضرب ګرځي. دوه متناسب قطارونه صفر ډیټرمینانټ ورکوي.',r'R_3\to R_3+R_2=(a+b+c)(1,1,1)=(a+b+c)R_1')])
ma=M([[b*c,c*a,a*b],[a,b,c],[a*a,b*b,c*c]]);mb=M([[1,1,1],[a*a,b*b,c*c],[a**3,b**3,c**3]])
assert S.expand(ma.det()-mb.det())==0
put('5','(iv)',r'$D_{\rm left}=D_{\rm right}$',[step('When $abc$ is nonzero, multiply columns one, two and three by $a,b,c$ respectively, then factor $abc$ from the first row.','جب $abc$ غیر صفر ہو، پہلے، دوسرے اور تیسرے کالم کو بالترتیب $a,b,c$ سے ضرب دیں، پھر پہلی قطار سے $abc$ مشترک لیں۔','کله چې $abc$ غیرصفر وي، لومړۍ، دویمه او درېیمه ستن په ترتیب په $a,b,c$ ضرب کړئ، بیا له لومړي قطار څخه $abc$ مشترک وباسئ.',r'abcD_{\rm left}=\begin{vmatrix}abc&abc&abc\\a^2&b^2&c^2\\a^3&b^3&c^3\end{vmatrix}=abcD_{\rm right}'),step('Both sides are the same polynomial after expansion, so the identity also holds when one or more of $a,b,c$ is zero.','کھولنے پر دونوں طرف ایک ہی کثیر رقمی ہے، اس لیے $a,b,c$ میں سے ایک یا زیادہ صفر ہوں تب بھی مماثلت درست ہے۔','د پراخولو وروسته دواړه خواوې یو شان څو حدي دي، نو که له $a,b,c$ څخه یو یا څو صفر وي هم مطابقت سم دی.',r'D_{\rm left}=D_{\rm right}='+S.latex(S.factor(ma.det())))])
ma=M([[a-b,b-c,c-a],[b-c,c-a,a-b],[c-a,a-b,b-a]])
counter=ma.subs({a:1,b:2,c:3});assert counter.det()==-6
put('6','(i)','False as printed: $a=1,b=2,c=3$ gives determinant $-6$, not $0$.',[step('The source prints $b-a$ in the bottom-right position. Keep that entry and test $a=1,b=2,c=3$.','اصل کتاب میں نیچے دائیں اندراج $b-a$ ہے۔ اسے برقرار رکھ کر $a=1,b=2,c=3$ رکھیں۔','په سرچینه کې ښکته ښی عنصر $b-a$ دی. همدا عنصر وساتئ او $a=1,b=2,c=3$ وازمویئ.',det(counter)+'=-6'),step('Therefore the asserted zero identity cannot be proved for the printed matrix. The printed identity is incorrect.','لہٰذا مطبوعہ قالب کے لیے صفر ہونے کی مماثلت ثابت نہیں ہو سکتی۔ مطبوعہ مماثلت غلط ہے۔','نو د چاپ شوي میټریکس لپاره د صفر مطابقت نشي ثابتېدای. چاپ شوی مطابقت ناسم دی.')],ur='مطبوعہ صورت میں غلط: $a=1,b=2,c=3$ پر مقطع $-6$ ہے، $0$ نہیں۔',ps='په چاپ شوې بڼه ناسم: د $a=1,b=2,c=3$ لپاره ډیټرمینانټ $-6$ دی، $0$ نه دی.')
ma=M([[1,a,a**3],[1,b,b**3],[1,c,c**3]]);expected=(a-b)*(b-c)*(c-a)*(a+b+c);assert S.expand(ma.det()-expected)==0
put('6','(ii)',r'$(a-b)(b-c)(c-a)(a+b+c)$',[step('Subtract the first row from rows two and three, then factor $b-a$ and $c-a$.','پہلی قطار دوسری اور تیسری سے تفریق کریں، پھر $b-a$ اور $c-a$ مشترک لیں۔','لومړی قطار له دویم او درېیم څخه منفي کړئ، بیا $b-a$ او $c-a$ مشترک وباسئ.',r'D=(b-a)(c-a)\begin{vmatrix}1&a&a^3\\0&1&b^2+ab+a^2\\0&1&c^2+ac+a^2\end{vmatrix}'),step('Subtract the second row from the third and simplify the remaining factor.','دوسری قطار تیسری سے تفریق کریں اور باقی عامل مختصر کریں۔','دویم قطار له درېیم څخه منفي کړئ او پاتې عامل ساده کړئ.',r'D=(b-a)(c-a)(c-b)(a+b+c)=(a-b)(b-c)(c-a)(a+b+c)')])
A.save(['2.2'],[53,54])
