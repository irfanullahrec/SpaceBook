"""Shared trilingual step phrases and helpers for Class 11 Mathematics answers (Units 7-12)."""
import sympy as S
from math11_answer_authoring import step

def work(tex):
    return step('Substitute and simplify.','قیمتیں رکھ کر مختصر کریں۔','ارزښتونه کېږدئ او ساده یې کړئ.',tex)
def note(en,ur,ps,m=None):return step(en,ur,ps,m)

PROVED=('Proved.','ثابت ہوا۔','ثابت شو.')
BASIS=lambda m:step('Check the statement for $n=1$.','$n=1$ کے لیے بیان کی جانچ کریں۔','د $n=1$ لپاره بیان وڅېړئ.',m)
HYP=lambda m:step('Assume the statement is true for $n=k$.','فرض کریں کہ بیان $n=k$ کے لیے درست ہے۔','فرض کړئ چې بیان د $n=k$ لپاره سم دی.',m)
NEXT=lambda m:step('Add the next term (or work with $n=k+1$) and simplify to the required form.','اگلا رکن جمع کریں (یا $n=k+1$ لیں) اور مطلوبہ صورت تک مختصر کریں۔','بل حد جمع کړئ (یا $n=k+1$ واخلئ) او غوښتل شوې بڼې ته یې ساده کړئ.',m)
CONC=step('Hence the statement is true for $n=k+1$. By mathematical induction it holds for every positive integer $n$.','لہٰذا بیان $n=k+1$ کے لیے بھی درست ہے۔ استقرائے ریاضی سے یہ ہر مثبت صحیح عدد $n$ کے لیے درست ہے۔','له دې امله بیان د $n=k+1$ لپاره هم سم دی. د ریاضیاتي استقرا له مخې دا د هر مثبت صحیح عدد $n$ لپاره سم دی.')
def MC(ex,q,p,choice,w,put,ur=None,ps=None,en='Work out the result and compare it with the printed options.',ur_s='نتیجہ نکال کر مطبوعہ اختیارات سے موازنہ کریں۔',ps_s='پایله ومومئ او له چاپ شوو انتخابونو سره یې پرتله کړئ.',cat='mcqs'):
    put(ex,q,p,choice,[step(en,ur_s,ps_s,w)],category=cat,answerUr=ur or choice,answerPs=ps or choice)
def eq0(e):
    """Symbolic zero test tolerant of factorials / binomials."""
    e=S.combsimp(S.expand_func(e)) if e.has(S.factorial,S.binomial) else e
    return S.simplify(e)==0
def tex(e):return S.latex(e)

def make_put(A):
    """put() that stores per-part entries when the printed question has no separate parts, merging them at flush()."""
    PEND={}
    def put(ex,q,p,ans,ss,**kw):
        key=f'{ex}|{q}|{p}'
        if key in A.source:
            A.put(ex,str(q),p,ans,ss,**kw)
        else:
            PEND.setdefault((ex,str(q)),[]).append((p,ans,ss,kw))
    def flush():
        for (ex,q),lst in PEND.items():
            ans='; '.join(f'{p} {a}' for p,a,_,_ in lst)
            ur='; '.join(f"{p} {kw.get('answerUr',a)}" for p,a,_,kw in lst)
            ps='; '.join(f"{p} {kw.get('answerPs',a)}" for p,a,_,kw in lst)
            steps=[]
            for p,a,ss,kw in lst:
                steps.append(step(f'Part {p}',f'حصہ {p}',f'برخه {p}'));steps+=ss
            cat=lst[0][3].get('category')
            A.put(ex,q,'',ans,steps,category=cat,answerUr=ur,answerPs=ps)
        PEND.clear()
    return put,flush
