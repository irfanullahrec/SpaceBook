import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from gm import *
pages={}
def T(en,ur=None,ps=None):return f'{en} || {ur or en} || {ps or en}'
def P(en,ur,ps):return f'p {T(en,ur,ps)}\n'
def M(t):return f'm {t}\n'
def EX(n,en,ur,ps):return f'example {n} | {T(en,ur,ps)}\n'
SOL=P('**Solution:**','**حل:**','**حل:**')
def S(w,h,aria,body):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{aria}"><title>{aria}</title>{body}</svg>'
tx=lambda x,y,t,sz=14,fill='#0f172a':f'<text x="{x}" y="{y}" font-size="{sz}" fill="{fill}" font-family="sans-serif">{t}</text>'
def tri(vs,labels,stroke='#2563eb',fill='#e0f2fe'):
    s=f'<polygon points="{" ".join(f"{x},{y}" for x,y in vs)}" fill="{fill}" fill-opacity=".5" stroke="{stroke}" stroke-width="2.4"/>'
    for t,(x,y) in labels:s+=tx(x,y,t)
    return s
def tfig(aria):return S(260,220,aria,tri([(30,180),(200,180),(230,30)],[('B',(232,24)),('C',(10,192)),('A',(204,196)),('a',(150,95)),('c',(220,95)),('b',(100,196)),('β',(215,60)),('γ',(48,172)),('α',(168,172))]))
f1115=tfig('Figure 11.15: triangle ABC with the sides a, b, c')
f1116=tfig('Figure 11.16: triangle ABC with the sides a, b, c')
f1117=tfig('Figure 11.17: triangle ABC with the sides a, b, c')
def box(en):return f'm {en}\n'
pages[323]=r'''@printed 323
@deco Unit-running header, folio and decorative footer band excluded
p and $\sin\alpha-\sin\beta=2\cos\dfrac{\alpha+\beta}2\sin\dfrac{\alpha-\beta}2$ we get || اور $\sin\alpha-\sin\beta=2\cos\dfrac{\alpha+\beta}2\sin\dfrac{\alpha-\beta}2$ سے ہمیں ملتا ہے || او $\sin\alpha-\sin\beta=2\cos\dfrac{\alpha+\beta}2\sin\dfrac{\alpha-\beta}2$ نه موږ ترلاسه کوو
m $\dfrac{a+b}{a-b}=\dfrac{2\sin\frac{\alpha+\beta}2\cos\frac{\alpha-\beta}2}{2\cos\frac{\alpha+\beta}2\sin\frac{\alpha-\beta}2}\ \Rightarrow\ \dfrac{a+b}{a-b}=\dfrac{\tan\frac12(\alpha+\beta)}{\tan\frac12(\alpha-\beta)}$
p Similarly $\dfrac{b+c}{b-c}=\dfrac{\tan\frac12(\beta+\gamma)}{\tan\frac12(\beta-\gamma)}$ and $\dfrac{c+a}{c-a}=\dfrac{\tan\frac12(\gamma+\alpha)}{\tan\frac12(\gamma-\alpha)}$. These three relations are known as the law of tangents. Note that the interchange of lengths $a$, $b$ result in the interchange of angles $\alpha$, $\beta$. Hence if $b>a$ then it is better to use the tangent formula in the form $\dfrac{b+a}{b-a}=\dfrac{\tan\frac12(\beta+\alpha)}{\tan\frac12(\beta-\alpha)}$ || اسی طرح $\dfrac{b+c}{b-c}=\dfrac{\tan\frac12(\beta+\gamma)}{\tan\frac12(\beta-\gamma)}$ اور $\dfrac{c+a}{c-a}=\dfrac{\tan\frac12(\gamma+\alpha)}{\tan\frac12(\gamma-\alpha)}$۔ یہ تینوں تعلقات قانونِ ٹینجنٹ کہلاتے ہیں۔ نوٹ کریں کہ لمبائیوں $a$، $b$ کے باہمی تبادلے سے زاویوں $\alpha$، $\beta$ کا تبادلہ ہوتا ہے۔ لہٰذا اگر $b>a$ ہو تو ٹینجنٹ کلیہ اس صورت میں استعمال کرنا بہتر ہے $\dfrac{b+a}{b-a}=\dfrac{\tan\frac12(\beta+\alpha)}{\tan\frac12(\beta-\alpha)}$ || په ورته ډول $\dfrac{b+c}{b-c}=\dfrac{\tan\frac12(\beta+\gamma)}{\tan\frac12(\beta-\gamma)}$ او $\dfrac{c+a}{c-a}=\dfrac{\tan\frac12(\gamma+\alpha)}{\tan\frac12(\gamma-\alpha)}$. دا درې اړیکې د ټینجنټو قانون بلل کېږي. یادونه وکړئ چې د اوږدوالو $a$، $b$ تبادله د زاویو $\alpha$، $\beta$ تبادله رامنځته کوي. له دې امله که $b>a$ وي نو د ټینجنټ فورمول په دې بڼه کارول غوره دي $\dfrac{b+a}{b-a}=\dfrac{\tan\frac12(\beta+\alpha)}{\tan\frac12(\beta-\alpha)}$
'''+EX(13,r'Use the law of tangents to solve the triangle ABC in which $a=925,\ c=432$ and $\beta=42^\circ30\'$.'.replace("\\'","′"),r'قانونِ ٹینجنٹ سے مثلث ABC حل کریں جس میں $a=925,\ c=432$ اور $\beta=42^\circ30′$ ہے۔',r'د ټینجنټو قانون په کارولو درې ګونی ABC حل کړئ چې په کې $a=925,\ c=432$ او $\beta=42^\circ30′$ دي.')+SOL+r'''m $\dfrac{a-c}{a+c}=\dfrac{\tan\frac12(\alpha-\gamma)}{\tan\frac12(\alpha+\gamma)}$
m $\text{But }\alpha+\gamma=180^\circ-\beta=137^\circ30′\Rightarrow\dfrac12(\alpha+\gamma)=68^\circ45′$
m $\text{Hence }\dfrac{925-432}{925+432}=\dfrac{\tan\frac12(\alpha-\gamma)}{\tan(68^\circ45′)}$
m $\text{Therefore }\tan\dfrac12(\alpha-\gamma)=\dfrac{493}{1357}\times2.5715=0.93\Rightarrow\dfrac12(\alpha-\gamma)=43^\circ3′\Rightarrow\alpha-\gamma=86^\circ6′$
m $\text{Now }\alpha+\gamma=137^\circ30′,\ \ \alpha-\gamma=86^\circ6′$
m $\text{By addition }2\alpha=223^\circ36′\Rightarrow\alpha=111^\circ48′;\ \ \text{by subtraction }2\gamma=51^\circ24′\Rightarrow\gamma=25^\circ42′$
'''
pages[324]=r'''@printed 324
@sec 11.1.2(d) | Half Angle Formulae || نصف زاویے کے کلیات || د نیمایي زاویې فورمولونه
@deco Unit-running header, folio and decorative footer band excluded
p To find $b$, we use the law of sines || $b$ معلوم کرنے کے لیے ہم قانونِ سائن استعمال کرتے ہیں || د $b$ د موندلو لپاره موږ د ساینو قانون کاروو
m $\dfrac b{\sin\beta}=\dfrac c{\sin\gamma}\Rightarrow b=\dfrac c{\sin\gamma}\sin\beta=\dfrac{432}{\sin25^\circ42′}\sin42^\circ30′=673$
endexample
### (d) Half Angle Formulae || (d) نصف زاویے کے کلیات || (d) د نیمایي زاویې فورمولونه
p The half angle formulae are very useful to solve a triangle when the measures of three sides of a triangle are given and no angle is known. These formulae could be derived using the law of cosines. || نصف زاویے کے کلیات مثلث حل کرنے کے لیے بہت مفید ہیں جب مثلث کے تین اضلاع کی پیمائشیں دی گئی ہوں اور کوئی زاویہ معلوم نہ ہو۔ یہ کلیات قانونِ کوسائن سے اخذ کیے جا سکتے ہیں۔ || د نیمایي زاویې فورمولونه د درې ګوني د حل لپاره ډېر ګټور دي کله چې د درې ګوني د درېیو ضلعو اندازې ورکړل شوې وي او هیڅ زاویه معلومه نه وي. دا فورمولونه د کوساینو د قانون په کارولو سره پیدا کېدای شي.
p **(i) The cosine of Half the Angle in Terms of Sides** **Theorem:** In any triangle ABC, show that $\cos\dfrac\alpha2=\sqrt{\dfrac{S(S-a)}{bc}}$, $\cos\dfrac\beta2=\sqrt{\dfrac{S(S-b)}{ac}}$, $\cos\dfrac\gamma2=\sqrt{\dfrac{S(S-c)}{ab}}$ where $S=\dfrac12(a+b+c)$ || **(i) اضلاع کے لحاظ سے نصف زاویے کا کوسائن** **مسئلہ:** کسی بھی مثلث ABC میں دکھائیں کہ $\cos\dfrac\alpha2=\sqrt{\dfrac{S(S-a)}{bc}}$، $\cos\dfrac\beta2=\sqrt{\dfrac{S(S-b)}{ac}}$، $\cos\dfrac\gamma2=\sqrt{\dfrac{S(S-c)}{ab}}$ جہاں $S=\dfrac12(a+b+c)$ || **(i) د ضلعو په لحاظ د نیمایي زاویې کوساین** **قضیه:** په هر درې ګوني ABC کې وښایاست چې $\cos\dfrac\alpha2=\sqrt{\dfrac{S(S-a)}{bc}}$، $\cos\dfrac\beta2=\sqrt{\dfrac{S(S-b)}{ac}}$، $\cos\dfrac\gamma2=\sqrt{\dfrac{S(S-c)}{ab}}$ چېرته چې $S=\dfrac12(a+b+c)$
'''+svgblock('Figure 11.15: triangle ABC with the sides $a$, $b$, $c$.','شکل 11.15: مثلث ABC جس کے اضلاع $a$، $b$، $c$ ہیں۔','شکل 11.15: درې ګونی ABC چې ضلعې یې $a$، $b$، $c$ دي.',f1115)+r'''p **Proof:** Let $S=\dfrac12(a+b+c)$. Using the law of cosines || **ثبوت:** فرض کریں $S=\dfrac12(a+b+c)$۔ قانونِ کوسائن سے || **ثبوت:** فرض کړئ $S=\dfrac12(a+b+c)$. د کوساینو د قانون په کارولو سره
m $\cos\alpha=\dfrac{b^2+c^2-a^2}{2bc}.\ \text{ But }\cos\alpha=2\cos^2\dfrac\alpha2-1.$
m $\text{Hence }2\cos^2\dfrac\alpha2-1=\dfrac{b^2+c^2-a^2}{2bc}\Rightarrow2\cos^2\dfrac\alpha2=\dfrac{b^2+c^2-a^2}{2bc}+1=\dfrac{(b+c)^2-a^2}{2bc}$
p The numerator being difference of two squares, can be written as $2\cos^2\dfrac\alpha2=\dfrac{[(b+c)+a][(b+c)-a]}{2bc}$. Since $a+b+c=2S$ and $b+c-a=2S-2a=2(S-a)$. || صورت دو مربعوں کا فرق ہونے کی وجہ سے $2\cos^2\dfrac\alpha2=\dfrac{[(b+c)+a][(b+c)-a]}{2bc}$ لکھا جا سکتا ہے۔ چونکہ $a+b+c=2S$ اور $b+c-a=2S-2a=2(S-a)$۔ || صورت د دوو مربعو توپیر وي، دا $2\cos^2\dfrac\alpha2=\dfrac{[(b+c)+a][(b+c)-a]}{2bc}$ لیکل کېدای شي. ځکه چې $a+b+c=2S$ او $b+c-a=2S-2a=2(S-a)$.
m $\text{Hence }2\cos^2\dfrac\alpha2=\dfrac{(2S)\times2(S-a)}{2bc}\ \Rightarrow\ \cos^2\dfrac\alpha2=\dfrac{S(S-a)}{bc}\ \text{ or }\ \cos\dfrac\alpha2=\pm\sqrt{\dfrac{S(S-a)}{bc}}$
'''
pages[325]=r'''@printed 325
@deco Unit-running header, folio and decorative footer band excluded
p As $\alpha<180^\circ$, $\dfrac\alpha2$ is a measure of acute angle, the value of $\cos\dfrac\alpha2$ will be positive. Hence || چونکہ $\alpha<180^\circ$ ہے، $\dfrac\alpha2$ حاد زاویے کی پیمائش ہے، $\cos\dfrac\alpha2$ کی قیمت مثبت ہوگی۔ لہٰذا || ځکه چې $\alpha<180^\circ$ دی، $\dfrac\alpha2$ د تېرې زاویې اندازه ده، د $\cos\dfrac\alpha2$ ارزښت مثبت وي. له دې امله
m $\cos\dfrac\alpha2=\sqrt{\dfrac{S(S-a)}{bc}}\qquad(1)$
p Similarly we can prove $\cos\dfrac\beta2=\sqrt{\dfrac{S(S-b)}{ac}}$ and $\cos\dfrac\gamma2=\sqrt{\dfrac{S(S-c)}{ab}}$. || اسی طرح ہم ثابت کر سکتے ہیں $\cos\dfrac\beta2=\sqrt{\dfrac{S(S-b)}{ac}}$ اور $\cos\dfrac\gamma2=\sqrt{\dfrac{S(S-c)}{ab}}$۔ || په ورته ډول موږ ثابتولای شو $\cos\dfrac\beta2=\sqrt{\dfrac{S(S-b)}{ac}}$ او $\cos\dfrac\gamma2=\sqrt{\dfrac{S(S-c)}{ab}}$.
p **(ii) The sines of Half the Angle in Terms of Sides** **Theorem:** In any triangle ABC, show that $\sin\dfrac\alpha2=\sqrt{\dfrac{(S-b)(S-c)}{bc}}$, $\sin\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{ac}}$, $\sin\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{ab}}$, where $S=\dfrac12(a+b+c)$ || **(ii) اضلاع کے لحاظ سے نصف زاویے کے سائن** **مسئلہ:** کسی بھی مثلث ABC میں دکھائیں کہ $\sin\dfrac\alpha2=\sqrt{\dfrac{(S-b)(S-c)}{bc}}$، $\sin\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{ac}}$، $\sin\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{ab}}$، جہاں $S=\dfrac12(a+b+c)$ || **(ii) د ضلعو په لحاظ د نیمایي زاویې ساین** **قضیه:** په هر درې ګوني ABC کې وښایاست چې $\sin\dfrac\alpha2=\sqrt{\dfrac{(S-b)(S-c)}{bc}}$، $\sin\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{ac}}$، $\sin\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{ab}}$، چېرته چې $S=\dfrac12(a+b+c)$
'''+svgblock('Figure 11.16: triangle ABC with the sides $a$, $b$, $c$.','شکل 11.16: مثلث ABC جس کے اضلاع $a$، $b$، $c$ ہیں۔','شکل 11.16: درې ګونی ABC چې ضلعې یې $a$، $b$، $c$ دي.',f1116)+r'''p **Proof:** $\cos\alpha=1-2\sin^2\dfrac\alpha2$. Hence || **ثبوت:** $\cos\alpha=1-2\sin^2\dfrac\alpha2$۔ لہٰذا || **ثبوت:** $\cos\alpha=1-2\sin^2\dfrac\alpha2$. له دې امله
m $2\sin^2\dfrac\alpha2=1-\cos\alpha=1-\dfrac{b^2+c^2-a^2}{2bc}=\dfrac{a^2-(b-c)^2}{2bc}=\dfrac{(a-b+c)(a+b-c)}{2bc}$
p Since $a+b+c=2S$ so $a-b+c=2S-2b=2(S-b)$ and $a+b-c=2S-2c=2(S-c)$. Substituting these values in the above equation || چونکہ $a+b+c=2S$ اس لیے $a-b+c=2S-2b=2(S-b)$ اور $a+b-c=2S-2c=2(S-c)$۔ ان قیمتوں کو مذکورہ مساوات میں رکھنے پر || ځکه چې $a+b+c=2S$ نو $a-b+c=2S-2b=2(S-b)$ او $a+b-c=2S-2c=2(S-c)$. دا ارزښتونه په پورتنۍ معادله کې ایښودو سره
m $2\sin^2\dfrac\alpha2=\dfrac{2(S-b)\times2(S-c)}{2bc}\Rightarrow\sin\dfrac\alpha2=\pm\sqrt{\dfrac{(S-b)(S-c)}{bc}}$
p Again $\sin\dfrac\alpha2$ is measure of an acute angle $\sin\dfrac\alpha2$ is always positive. Hence || ایک بار پھر $\sin\dfrac\alpha2$ حاد زاویے کی پیمائش ہے، $\sin\dfrac\alpha2$ ہمیشہ مثبت ہے۔ لہٰذا || بیا $\sin\dfrac\alpha2$ د تېرې زاویې اندازه ده، $\sin\dfrac\alpha2$ تل مثبت دی. له دې امله
m $\sin\dfrac\alpha2=\sqrt{\dfrac{(S-b)(S-c)}{bc}}\qquad(2)$
'''
pages[326]=r'''@printed 326
@sec 11.1.2(d)(iii) | The tangent of half the angle in terms of the sides || اضلاع کے لحاظ سے نصف زاویے کا ٹینجنٹ || د ضلعو په لحاظ د نیمایي زاویې ټینجنټ
@deco Unit-running header, folio and decorative footer band excluded
p Similarly $\sin\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{ac}}$ and $\sin\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{ab}}$. || اسی طرح $\sin\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{ac}}$ اور $\sin\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{ab}}$۔ || په ورته ډول $\sin\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{ac}}$ او $\sin\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{ab}}$.
p **(iii) The Tangent of Half the Angle in Terms of the Sides** **Theorem:** In any triangle ABC, show that $\tan\dfrac\alpha2=\sqrt{\dfrac{(S-b)(S-c)}{S(S-a)}}$, $\tan\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{S(S-b)}}$, $\tan\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{S(S-c)}}$ where $S=\dfrac12(a+b+c)$ || **(iii) اضلاع کے لحاظ سے نصف زاویے کا ٹینجنٹ** **مسئلہ:** کسی بھی مثلث ABC میں دکھائیں کہ $\tan\dfrac\alpha2=\sqrt{\dfrac{(S-b)(S-c)}{S(S-a)}}$، $\tan\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{S(S-b)}}$، $\tan\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{S(S-c)}}$ جہاں $S=\dfrac12(a+b+c)$ || **(iii) د ضلعو په لحاظ د نیمایي زاویې ټینجنټ** **قضیه:** په هر درې ګوني ABC کې وښایاست چې $\tan\dfrac\alpha2=\sqrt{\dfrac{(S-b)(S-c)}{S(S-a)}}$، $\tan\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{S(S-b)}}$، $\tan\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{S(S-c)}}$ چېرته چې $S=\dfrac12(a+b+c)$
'''+svgblock('Figure 11.17: triangle ABC with the sides $a$, $b$, $c$.','شکل 11.17: مثلث ABC جس کے اضلاع $a$، $b$، $c$ ہیں۔','شکل 11.17: درې ګونی ABC چې ضلعې یې $a$، $b$، $c$ دي.',f1117)+r'''p **Proof:** || **ثبوت:** || **ثبوت:**
m $\tan\dfrac\alpha2=\dfrac{\sin\frac\alpha2}{\cos\frac\alpha2}=\dfrac{\sqrt{(S-b)(S-c)/bc}}{\sqrt{S(S-a)/bc}}\qquad(\text{by (1) and (2)})$
m $\Rightarrow\tan\dfrac\alpha2=\sqrt{\dfrac{(S-b)(S-c)}{S(S-a)}}\qquad(3)$
p Similarly $\tan\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{S(S-b)}}$ and $\tan\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{S(S-c)}}$. Now if we multiply and divide the right hand side of (3) by $\sqrt{(S-a)}$ we get || اسی طرح $\tan\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{S(S-b)}}$ اور $\tan\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{S(S-c)}}$۔ اب اگر ہم (3) کے دائیں طرف کو $\sqrt{(S-a)}$ سے ضرب اور تقسیم دیں تو ہمیں ملتا ہے || په ورته ډول $\tan\dfrac\beta2=\sqrt{\dfrac{(S-c)(S-a)}{S(S-b)}}$ او $\tan\dfrac\gamma2=\sqrt{\dfrac{(S-a)(S-b)}{S(S-c)}}$. اوس که موږ د (3) ښي خوا په $\sqrt{(S-a)}$ ضرب او ووېشو نو موږ ترلاسه کوو
m $\tan\dfrac\alpha2=\dfrac1{(S-a)}\sqrt{\dfrac{(S-a)(S-b)(S-c)}S}$
p Denoting $\sqrt{\dfrac{(S-a)(S-b)(S-c)}S}$ by $r$, we get || $\sqrt{\dfrac{(S-a)(S-b)(S-c)}S}$ کو $r$ سے ظاہر کرنے پر ہمیں ملتا ہے || $\sqrt{\dfrac{(S-a)(S-b)(S-c)}S}$ په $r$ ښودلو سره موږ ترلاسه کوو
m $\tan\dfrac\alpha2=\dfrac r{S-a}\qquad(4)$
'''
for n,t in pages.items():
    open(f'{OUT}\\p{n}.txt','w',encoding='utf8').write(t)
print('ok')
