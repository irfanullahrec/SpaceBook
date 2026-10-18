from math11_answer_authoring import step,S
def tex(m,cut=None):
    body=r'\\'.join('&'.join(S.latex(v) for v in row) for row in m.tolist())
    if cut:return r'\left[\begin{array}{'+'c'*cut+'|'+'c'*(m.cols-cut)+'}'+body+r'\end{array}\right]'
    return r'\begin{bmatrix}'+body+r'\end{bmatrix}'
def reduce_rows(original,reduced=True,columns=None,cut=None):
    mat=original.copy();transform=S.eye(mat.rows);out=[];r=0
    def record(op,en,ur,ps):
        assert transform*original==mat,'row-equivalence check'
        assert transform.det()!=0,'invertible row operation'
        out.append(step(en,ur,ps,op+r'\quad\Rightarrow\quad'+tex(mat,cut)))
    for c in range(columns if columns is not None else mat.cols):
        candidates=[j for j in range(r,mat.rows) if mat[j,c]!=0]
        if not candidates:continue
        pivot=next((j for j in candidates if mat[j,c]==1),candidates[0])
        if pivot!=r:
            mat.row_swap(r,pivot);transform.row_swap(r,pivot)
            record(fr'R_{r+1}\leftrightarrow R_{pivot+1}','Interchange these two rows.','ان دو قطاروں کی جگہ بدلیں۔','دا دوه قطارونه سره بدل کړئ.')
        value=mat[r,c]
        if value!=1:
            mat.row_op(r,lambda v,j:v/value);transform.row_op(r,lambda v,j:v/value)
            record(fr'R_{r+1}\to({S.latex(1/value)})R_{r+1}','Scale the pivot row so its leading entry becomes one.','محوری قطار کو عدد سے ضرب دیں تاکہ اس کا ابتدائی اندراج ایک ہو جائے۔','محوري قطار په عدد ضرب کړئ څو مخکښ عنصر یې یو شي.')
        targets=[j for j in range(mat.rows) if j!=r] if reduced else list(range(r+1,mat.rows))
        for j in targets:
            value=mat[j,c]
            if value==0:continue
            mat.row_op(j,lambda v,k:v-value*mat[r,k]);transform.row_op(j,lambda v,k:v-value*transform[r,k])
            record(fr'R_{j+1}\to R_{j+1}-({S.latex(value)})R_{r+1}','Eliminate this entry with a multiple of the pivot row.','محوری قطار کے مضرب سے اس اندراج کو صفر کریں۔','د محوري قطار په مضرب دا عنصر صفر کړئ.')
        r+=1
        if r==mat.rows:break
    assert mat.rank()==original.rank()
    if reduced and columns is None:assert mat==original.rref()[0]
    return mat,out
def inverse_steps(ma):
    augmented=ma.row_join(S.eye(ma.rows))
    reduced,ops=reduce_rows(augmented,columns=ma.cols,cut=ma.cols)
    assert reduced[:,:ma.cols]==S.eye(ma.rows)
    inverse=reduced[:,ma.cols:]
    assert ma*inverse==S.eye(ma.rows) and inverse*ma==S.eye(ma.rows)
    return inverse,[step(r'Augment $A$ with the identity matrix. Row-reduce $[A\mid I]$ to $[I\mid A^{-1}]$.',r'$A$ کے ساتھ اکائی قالب ملائیں۔ قطاری اعمال سے $[A\mid I]$ کو $[I\mid A^{-1}]$ بنائیں۔',r'له $A$ سره واحد میټریکس یوځای کړئ. په قطاري عملونو $[A\mid I]$ په $[I\mid A^{-1}]$ بدل کړئ.',tex(augmented,ma.cols))]+ops+[step('The right block is the inverse; multiplying it by $A$ gives the identity.','دائیں حصہ معکوس ہے؛ اسے $A$ سے ضرب دینے پر اکائی قالب ملتا ہے۔','ښی بلاک معکوس دی؛ په $A$ یې ضربول واحد میټریکس ورکوي.',r'A^{-1}='+tex(inverse))]
def system_steps(ma,rhs,method):
    solution=ma.inv()*rhs
    assert ma*solution==rhs
    steps=[]
    if method=='inverse':
        steps=[step('Write $AX=B$ and multiply by the inverse of $A$.','$AX=B$ لکھیں اور $A$ کے معکوس سے ضرب دیں۔','$AX=B$ ولیکئ او د $A$ په معکوس ضرب کړئ.',r'|A|='+str(ma.det())+r'\ne0,\quad A^{-1}='+tex(ma.inv())),step('The solution column is $X=A^{-1}B$.','حل کا کالم $X=A^{-1}B$ ہے۔','د حل ستن $X=A^{-1}B$ ده.',r'X='+tex(ma.inv())+tex(rhs)+'='+tex(solution))]
    elif method=='cramer':
        ds=[]
        for col in range(ma.cols):
            changed=ma.copy();changed[:,col]=rhs;ds.append(changed.det())
        steps=[step("Replace each coefficient column in turn by the constants and take its determinant.","باری باری ہر سر کے کالم کو مستقل اعداد سے بدلیں اور اس کا مقطع لیں۔","په وار هر ضریبي ستن په ثابتو عددونو بدله کړئ او ډیټرمینانټ یې واخلئ.",r'D='+str(ma.det())+r',\quad'+r',\quad'.join(fr'D_{i+1}={d}' for i,d in enumerate(ds))),step("By Cramer's rule, divide each replacement determinant by the coefficient determinant.","کریمر کے قاعدے سے ہر بدلے ہوئے مقطع کو سر کے مقطع پر تقسیم کریں۔","د کرامر د قاعدې له مخې هر بدل شوی ډیټرمینانټ په ضریبي ډیټرمینانټ ووېشئ.",r'X='+tex(S.Matrix([d/ma.det() for d in ds])))]
    elif method=='both-gauss':
        augmented=ma.row_join(rhs);upper,forward=reduce_rows(augmented,reduced=False,columns=ma.cols,cut=ma.cols)
        rr,backward=reduce_rows(upper,reduced=True,columns=ma.cols,cut=ma.cols)
        assert rr[:,:ma.cols]==S.eye(ma.rows) and rr[:,-1]==solution
        steps=[step('Gauss elimination: reduce the augmented matrix to echelon form.','گاؤس اخراج: توسیعی قالب کو زینہ دار شکل میں بدلیں۔','د ګاوس حذف: پراخ شوی میټریکس زینې بڼې ته راکم کړئ.',tex(augmented,ma.cols))]+forward+[step('Back-substitute from the last row upwards to obtain the solution. This completes Gauss elimination.','آخری قطار سے اوپر کی طرف قیمتیں واپس رکھیں اور حل حاصل کریں۔ اس سے گاؤس اخراج مکمل ہوتا ہے۔','له وروستي قطار څخه پورته ارزښتونه بېرته ځای پر ځای او حل ترلاسه کړئ. په دې د ګاوس حذف بشپړېږي.',r'X='+tex(solution)),step('Gauss–Jordan: continue above each pivot to obtain reduced echelon form.','گاؤس–جارڈن: ہر محور کے اوپر کے اندراجات بھی صفر کر کے مختصر زینہ دار شکل حاصل کریں۔','ګاوس–جورډن: د هر محور پورته عناصر هم صفر کړئ څو راکمه شوې زینې بڼه ترلاسه شي.')]+backward+[step('The final column gives the same solution.','آخری کالم وہی حل دیتا ہے۔','وروستۍ ستن هماغه حل ورکوي.',r'X='+tex(solution))]
    return solution,steps
