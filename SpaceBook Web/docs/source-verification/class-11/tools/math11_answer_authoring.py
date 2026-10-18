"""Utilities for separately authored, source-linked Mathematics answers."""
import json, subprocess, re
from pathlib import Path
import sympy as S
HERE=Path(__file__).resolve().parents[1]
APP=HERE.parents[2]
def load_unit(n):
    js="const fs=require('fs'),vm=require('vm');const c={window:{}};vm.createContext(c);vm.runInContext(fs.readFileSync(process.argv[1],'utf8')+';this.u=MATH_11_DATA',c);process.stdout.write(JSON.stringify(c.u.find(x=>x.number===Number(process.argv[2]))));"
    return json.loads(subprocess.run(['node','-e',js,str(APP/'js/math_11_data.js'),str(n)],check=True,capture_output=True,encoding='utf-8').stdout)
def step(en,ur,ps,m=None):
    d=dict(en=en,ur=ur,ps=ps)
    if m:d['m']=m
    return d
def normalize_answer(value):
    if isinstance(value,str):
        return re.sub(r'\\(qquad|quad)(?=[A-Za-z])',lambda m:m.group(0)+' ',value).replace('غیر معمولی حل','غیر صفر حل')
    if isinstance(value,list):return [normalize_answer(v) for v in value]
    if isinstance(value,dict):
        out={k:(v if k in ('question','prompt') else normalize_answer(v)) for k,v in value.items()}
        if out.get('answer','').endswith(', hence parallel.'):
            math=out['answer'].removesuffix(', hence parallel.')
            out.setdefault('answerUr',math+'، لہٰذا متوازی ہیں۔')
            out.setdefault('answerPs',math+'، نو موازي دي.')
        return out
    return value
RULES={
 'powers':step('Use the repeating cycle $i,-1,-i,1$ and reduce integer exponents modulo four.','دورانی ترتیب $i,-1,-i,1$ استعمال کریں اور صحیح عددی قوتوں کو چار کے باقی سے مختصر کریں۔','د $i,-1,-i,1$ تکراري لړۍ وکاروئ او صحیح قوې د څلورو پر پاتې شوني ساده کړئ.'),
 'add':step('Add real parts together and imaginary coefficients together.','حقیقی حصوں کو آپس میں اور خیالی حصوں کے سر کو آپس میں جمع کریں۔','حقیقي برخې سره او د خیالي برخو ضریبونه سره جمع کړئ.'),
 'subtract':step('Subtract the second real and imaginary coefficients from the first.','دوسرے حقیقی اور خیالی سر کو پہلے سے تفریق کریں۔','د دویم عدد حقیقي او خیالي ضریبونه د لومړي له ضریبونو منفي کړئ.'),
 'multiply':step('Expand the product, replace $i^2$ by $-1$ and collect like terms.','ضرب کھولیں، $i^2$ کی جگہ $-1$ رکھیں اور ہم جنس اجزا یکجا کریں۔','ضرب پراخ کړئ، د $i^2$ پر ځای $-1$ کېږدئ او ورته حدونه راټول کړئ.'),
 'divide':step('Multiply numerator and denominator by the conjugate of the denominator.','صورت اور مخرج کو مخرج کے مزدوج سے ضرب دیں۔','صورت او مخرج د مخرج په مزدوج ضرب کړئ.'),
 'modulus':step(r'For $z=a+bi$, use $|z|=\sqrt{a^2+b^2}$. The modulus is nonnegative.',r'$z=a+bi$ کے لیے $|z|=\sqrt{a^2+b^2}$ استعمال کریں۔',r'د $z=a+bi$ لپاره $|z|=\sqrt{a^2+b^2}$ وکاروئ.'),
 'conjugate':step('Simplify first, then reverse the sign of the imaginary coefficient.','پہلے مختصر کریں، پھر خیالی سر کی علامت بدلیں۔','لومړی ساده کړئ، بیا د خیالي ضریب نښه واړوئ.'),
 'parts':step('Write the expression as $A+Bi$ with real $A,B$; then $Re=A$ and $Im=B$.','عبارت کو حقیقی $A,B$ کے ساتھ $A+Bi$ لکھیں؛ پھر $Re=A$ اور $Im=B$ ہیں۔','عبارت د حقیقي $A,B$ په مرسته $A+Bi$ ولیکئ؛ بیا $Re=A$ او $Im=B$ دي.'),
 'verify':step('Evaluate both sides with $i^2=-1$ and compare the real and imaginary parts.','$i^2=-1$ سے دونوں طرف کی قیمت معلوم کریں اور حقیقی و خیالی حصوں کا موازنہ کریں۔','د $i^2=-1$ په کارولو دواړه خواوې محاسبه او حقیقي او خیالي برخې پرتله کړئ.'),
 'factor':step('Factor the polynomial, solve each factor and include every distinct complex root.','کثیر رقمی کو اجزائے ضربی میں لکھیں، ہر جز حل کریں اور ہر مختلف مختلط جذر شامل کریں۔','څو حدي تجزیه کړئ، هر عامل حل کړئ او ټول بېلابېل مختلط جذرونه شامل کړئ.'),
 'quadratic':step('Put the equation in standard form and apply the quadratic formula.','مساوات کو معیاری شکل میں لکھیں اور دو درجی مساوات کا کلیہ لگائیں۔','معادله په معیاري بڼه ولیکئ او د دوه درجه یي معادلې فورمول وکاروئ.'),
 'substitute':step('Substitute the proposed value. It is a solution when the result is zero.','دی گئی قیمت رکھیں۔ حاصل صفر ہو تو یہ مساوات کا حل ہے۔','ورکړل شوی ارزښت ځای پر ځای کړئ. که پایله صفر وي، دا د معادلې حل دی.')
}
class Author:
    def __init__(self,unit):
        self.unit=load_unit(unit);self.source={};self.answers={};self.checks=[]
        for ex in self.unit['exercises']:
            def walk(bs):
                for b in bs:
                    if b['t']=='q':
                        self.source[f"{ex['id']}|{b['no']}|"]=(b,b)
                        for part in b.get('parts',[]):self.source[f"{ex['id']}|{b['no']}|{part['no']}"]=(part,b)
                    if b.get('blocks'):walk(b['blocks'])
            walk(ex['blocks'])
    def put(self,ex,q,p,answer,steps,category=None,answerUr=None,answerPs=None):
        key=f'{ex}|{q}|{p}';owner,parent=self.source[key]
        value=dict(question=owner['en'],prompt=parent['en'],answer=answer,steps=steps,provenance='SpaceBook authored solution')
        if category:value['category']=category
        if answerUr:value['answerUr']=answerUr
        if answerPs:value['answerPs']=answerPs
        self.answers[key]=normalize_answer(value)
    def calc(self,ex,q,p,expr,result,rule,work):
        assert S.simplify(S.expand_complex(expr-result))==0,(ex,q,p,expr,result)
        self.checks.append(f'{ex}|{q}|{p}')
        self.put(ex,q,p,'$'+S.latex(result)+'$',[RULES[rule],step('Simplify to obtain the answer.','مختصر کرنے سے جواب حاصل ہوتا ہے۔','په ساده کولو ځواب ترلاسه کېږي.',work)])
    def save(self,exercises,pages):
        leaves={k for k,(o,q) in self.source.items() if k.split('|')[0] in exercises and (o is not q or not q.get('parts'))}
        assert set(self.answers)==leaves,(set(self.answers)-leaves,leaves-set(self.answers))
        f=HERE/'math'/'authored-solutions.json'
        previous=f.read_text(encoding='utf-8') if f.exists() else None
        existing=json.loads(previous) if previous else {}
        for key,value in self.answers.items():
            value['sourceCheckedPdfPages']=pages
            if key in existing:assert existing[key]==value,f'Refuse to overwrite changed solution {key}'
            existing[key]=value
        assert (f.read_text(encoding='utf-8') if f.exists() else None)==previous,'Concurrent answers edit'
        f.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'Saved {len(self.answers)} authored answers for {exercises}; {len(self.checks)} symbolic arithmetic checks.')
