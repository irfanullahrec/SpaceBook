import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from gm import *
pages={}
def T(en,ur=None,ps=None):return f'{en} || {ur or en} || {ps or en}'
def P(en,ur,ps):return f'p {T(en,ur,ps)}\n'
def M(t):return f'm {t}\n'
def Q(no,en,ur=None,ps=None):return f'q {no} | {T(en,ur,ps)}\n'
def EX(n,en,ur=None,ps=None):return f'example {n} | {T(en,ur,ps)}\n'
pages[303]=r'''@printed 303
@issue This page is a low-quality (blurred) photograph. In Exercise 10.2 the given values are read as: Q1 tan θ = −1/5 (the denominator is unclear), Q2 sin θ = 5/13, Q3 sin θ = 4/5, Q4 cos θ = −3/7 (unclear; a value with |cos θ| ≤ 1). The fractions should be rechecked against a sharper scan.
@deco Exercise banner, unit-running header, folio and decorative footer band excluded
m $=2\cdot\dfrac{\sin\theta}{\cos\theta}\cos^2\theta=2\sin\theta\cos\theta=\sin2\theta$
p (ii) $\sin4\theta=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta$ (as printed). L.H.S $=\sin4\theta=\sin[2(2\theta)]=2\sin2\theta\cos2\theta$ (Use $\sin2a=2\sin a\cos a$, with $a=2\theta$) $=2(2\sin\theta\cos\theta)(2\cos^2\theta-1)=4\sin\theta\cos\theta(2\cos^2\theta-1)=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta=$ R.H.S. || (ii) $\sin4\theta=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta$ (جیسا چھپا ہے)۔ بایاں طرف $=\sin4\theta=\sin[2(2\theta)]=2\sin2\theta\cos2\theta$ ($\sin2a=2\sin a\cos a$ میں $a=2\theta$ لیں) $=2(2\sin\theta\cos\theta)(2\cos^2\theta-1)=4\sin\theta\cos\theta(2\cos^2\theta-1)=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta=$ دایاں طرف۔ || (ii) $\sin4\theta=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta$ (لکه چې چاپ شوی). کیڼه خوا $=\sin4\theta=\sin[2(2\theta)]=2\sin2\theta\cos2\theta$ (په $\sin2a=2\sin a\cos a$ کې $a=2\theta$ واخلئ) $=2(2\sin\theta\cos\theta)(2\cos^2\theta-1)=4\sin\theta\cos\theta(2\cos^2\theta-1)=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta=$ ښي خوا.
endexample
exercise 10.2
'''+Q(1,r'Find the values of $\sin2\theta$, $\cos2\theta$ and $\tan2\theta$, given $\tan\theta=-\dfrac15$, $\theta$ in quadrant II.',r'$\sin2\theta$، $\cos2\theta$ اور $\tan2\theta$ کی قیمتیں معلوم کریں، دیا گیا ہے $\tan\theta=-\dfrac15$، $\theta$ دوسرے ربع میں ہے۔',r'د $\sin2\theta$، $\cos2\theta$ او $\tan2\theta$ ارزښتونه پیدا کړئ، ورکړل شوی دی $\tan\theta=-\dfrac15$، $\theta$ په دویم ربع کې دی.')+Q(2,r'If $\sin\theta=\dfrac5{13}$ and terminal ray of $\theta$ is in the second quadrant, then find (i) $\sin2\theta$ (ii) $\cos2\theta$ (iii) $\tan2\theta$',r'اگر $\sin\theta=\dfrac5{13}$ اور $\theta$ کی انتہائی شعاع دوسرے ربع میں ہو تو معلوم کریں (i) $\sin2\theta$ (ii) $\cos2\theta$ (iii) $\tan2\theta$',r'که $\sin\theta=\dfrac5{13}$ او د $\theta$ وروستۍ وړانګه په دویم ربع کې وي نو پیدا کړئ (i) $\sin2\theta$ (ii) $\cos2\theta$ (iii) $\tan2\theta$')+Q(3,r'If $\sin\theta=\dfrac45$ and terminal ray of $\theta$ is in the second quadrant, then find (i) $\sin2\theta$ (ii) $\cos\dfrac\theta2$',r'اگر $\sin\theta=\dfrac45$ اور $\theta$ کی انتہائی شعاع دوسرے ربع میں ہو تو معلوم کریں (i) $\sin2\theta$ (ii) $\cos\dfrac\theta2$',r'که $\sin\theta=\dfrac45$ او د $\theta$ وروستۍ وړانګه په دویم ربع کې وي نو پیدا کړئ (i) $\sin2\theta$ (ii) $\cos\dfrac\theta2$')+Q(4,r'If $\cos\theta=-\dfrac37$ and terminal ray of $\theta$ is in 3rd quadrant, then find $\sin\dfrac\theta2$.',r'اگر $\cos\theta=-\dfrac37$ اور $\theta$ کی انتہائی شعاع تیسرے ربع میں ہو تو $\sin\dfrac\theta2$ معلوم کریں۔',r'که $\cos\theta=-\dfrac37$ او د $\theta$ وروستۍ وړانګه په دریم ربع کې وي نو $\sin\dfrac\theta2$ پیدا کړئ.')+Q(5,r'Use double angle identities to evaluate exactly. (i) $\sin\dfrac{2\pi}3$ (ii) $\cos\dfrac{2\pi}3$',r'دوہرے زاویے کی مماثلتیں استعمال کر کے صحیح قیمت معلوم کریں۔ (i) $\sin\dfrac{2\pi}3$ (ii) $\cos\dfrac{2\pi}3$',r'د دوه چنده زاویې هویتونه په کارولو دقیق ارزول. (i) $\sin\dfrac{2\pi}3$ (ii) $\cos\dfrac{2\pi}3$')+Q(6,r'Use the half angle identities to evaluate exactly. (i) $\cos15^\circ$ (ii) $\tan67.5^\circ$ (iii) $\sin112.5^\circ$ (iv) $\cos\dfrac\pi8$ (v) $\tan75^\circ$ (vi) $\sin\dfrac{5\pi}{12}$',r'نصف زاویے کی مماثلتیں استعمال کر کے صحیح قیمت معلوم کریں۔ (i) $\cos15^\circ$ (ii) $\tan67.5^\circ$ (iii) $\sin112.5^\circ$ (iv) $\cos\dfrac\pi8$ (v) $\tan75^\circ$ (vi) $\sin\dfrac{5\pi}{12}$',r'د نیمایي زاویې هویتونه په کارولو دقیق ارزول. (i) $\cos15^\circ$ (ii) $\tan67.5^\circ$ (iii) $\sin112.5^\circ$ (iv) $\cos\dfrac\pi8$ (v) $\tan75^\circ$ (vi) $\sin\dfrac{5\pi}{12}$')
pages[304]=r'''@printed 304
@sec 10.4 | Sum, Difference and Product of sine and cosine || سائن اور کوسائن کا مجموعہ، فرق اور حاصل ضرب || د ساین او کوساین مجموعه، توپیر او ضرب
@sec 10.4.1 | Converting Product to Sums or Differences || حاصل ضرب کو مجموعے یا فرق میں بدلنا || ضرب په مجموعو یا توپیرونو بدلول
@deco Unit-running header, folio and decorative footer band excluded
'''+Q(7,'Prove the following identities:')+r'''qp (i) | $\cos^4\theta-\sin^4\theta=\dfrac1{\sec2\theta}$ || $\cos^4\theta-\sin^4\theta=\dfrac1{\sec2\theta}$ || $\cos^4\theta-\sin^4\theta=\dfrac1{\sec2\theta}$
qp (ii) | $\tan\dfrac\theta2+\cot\dfrac\theta2=\dfrac2{\sin\theta}$ || $\tan\dfrac\theta2+\cot\dfrac\theta2=\dfrac2{\sin\theta}$ || $\tan\dfrac\theta2+\cot\dfrac\theta2=\dfrac2{\sin\theta}$
qp (iii) | $\dfrac{1+\cos2\theta}{1-\cos2\theta}=\cot^2\theta$ (printed with $1+\cos2\theta$ in the denominator) || $\dfrac{1+\cos2\theta}{1-\cos2\theta}=\cot^2\theta$ || $\dfrac{1+\cos2\theta}{1-\cos2\theta}=\cot^2\theta$
qp (iv) | $\csc2\theta-\cot2\theta=\tan\theta$ || $\csc2\theta-\cot2\theta=\tan\theta$ || $\csc2\theta-\cot2\theta=\tan\theta$
qp (v) | $\dfrac{\sin3\beta}{\sin\beta}-\dfrac{\cos3\beta}{\cos\beta}=2$ || $\dfrac{\sin3\beta}{\sin\beta}-\dfrac{\cos3\beta}{\cos\beta}=2$ || $\dfrac{\sin3\beta}{\sin\beta}-\dfrac{\cos3\beta}{\cos\beta}=2$
qp (vi) | $\dfrac{\sin3\theta}{\cos\theta}+\dfrac{\cos3\theta}{\sin\theta}=2\cot2\theta$ (printed with a plus sign as "$=2\cot2\theta$") || $\dfrac{\sin3\theta}{\cos\theta}+\dfrac{\cos3\theta}{\sin\theta}=2\cot2\theta$ || $\dfrac{\sin3\theta}{\cos\theta}+\dfrac{\cos3\theta}{\sin\theta}=2\cot2\theta$
qp (vii) | $\dfrac{\cos^3\theta-\sin^3\theta}{\cos\theta-\sin\theta}=\dfrac{2+\sin2\theta}2$ || $\dfrac{\cos^3\theta-\sin^3\theta}{\cos\theta-\sin\theta}=\dfrac{2+\sin2\theta}2$ || $\dfrac{\cos^3\theta-\sin^3\theta}{\cos\theta-\sin\theta}=\dfrac{2+\sin2\theta}2$
qp (viii) | $\dfrac{2\cos^3\theta}{1-\sin\theta}=2\cos\theta+\sin2\theta$ (as printed) || $\dfrac{2\cos^3\theta}{1-\sin\theta}=2\cos\theta+\sin2\theta$ || $\dfrac{2\cos^3\theta}{1-\sin\theta}=2\cos\theta+\sin2\theta$
qp (ix) | $\cot2\theta=\dfrac12\left(\cot\theta-\dfrac1{\cot\theta}\right)$ || $\cot2\theta=\dfrac12\left(\cot\theta-\dfrac1{\cot\theta}\right)$ || $\cot2\theta=\dfrac12\left(\cot\theta-\dfrac1{\cot\theta}\right)$
qp (x) | $\dfrac{\sin\alpha+\cos\alpha}{\cos\alpha-\sin\alpha}+\dfrac{\sin\alpha-\cos\alpha}{\cos\alpha+\sin\alpha}=2\tan2\alpha$ || $\dfrac{\sin\alpha+\cos\alpha}{\cos\alpha-\sin\alpha}+\dfrac{\sin\alpha-\cos\alpha}{\cos\alpha+\sin\alpha}=2\tan2\alpha$ || $\dfrac{\sin\alpha+\cos\alpha}{\cos\alpha-\sin\alpha}+\dfrac{\sin\alpha-\cos\alpha}{\cos\alpha+\sin\alpha}=2\tan2\alpha$
qp (xi) | $\tan\dfrac\alpha2=\dfrac{\sin\alpha}{1+\cos\alpha}$ || $\tan\dfrac\alpha2=\dfrac{\sin\alpha}{1+\cos\alpha}$ || $\tan\dfrac\alpha2=\dfrac{\sin\alpha}{1+\cos\alpha}$
qp (xii) | $\dfrac{\csc\theta-\cot\theta}{1+\cos\theta}=\csc\theta\tan^2\dfrac\theta2$ || $\dfrac{\csc\theta-\cot\theta}{1+\cos\theta}=\csc\theta\tan^2\dfrac\theta2$ || $\dfrac{\csc\theta-\cot\theta}{1+\cos\theta}=\csc\theta\tan^2\dfrac\theta2$
qp (xiii) | $\cos^2\dfrac\theta2=\dfrac{1-\cos^2\theta}{2-2\cos\theta}$ || $\cos^2\dfrac\theta2=\dfrac{1-\cos^2\theta}{2-2\cos\theta}$ || $\cos^2\dfrac\theta2=\dfrac{1-\cos^2\theta}{2-2\cos\theta}$
qp (xiv) | $\dfrac{1-\tan^2\frac\alpha2}{1+\tan^2\frac\alpha2}=\cos\alpha$ || $\dfrac{1-\tan^2\frac\alpha2}{1+\tan^2\frac\alpha2}=\cos\alpha$ || $\dfrac{1-\tan^2\frac\alpha2}{1+\tan^2\frac\alpha2}=\cos\alpha$
qp (xv) | $\sin2\theta-4\sin^3\theta\cos\theta=\sin2\theta\cos2\theta$ || $\sin2\theta-4\sin^3\theta\cos\theta=\sin2\theta\cos2\theta$ || $\sin2\theta-4\sin^3\theta\cos\theta=\sin2\theta\cos2\theta$
'''+Q(8,r'Write $\cos^4\theta$ in terms of the first power of one or more cosine functions.',r'$\cos^4\theta$ کو ایک یا زیادہ کوسائن تفاعل کی پہلی قوت کی صورت میں لکھیں۔',r'$\cos^4\theta$ د یو یا ډېرو کوساین تابعګانو په لومړي توان کې ولیکئ.')+Q(9,'Prove the following identities:')+r'''qp (i) | $\sin4\theta=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta$ || $\sin4\theta=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta$ || $\sin4\theta=8\sin\theta\cos^3\theta-4\sin\theta\cos\theta$
qp (ii) | $\cot4\theta=\dfrac{1-\tan^22\theta}{2\tan2\theta}$ || $\cot4\theta=\dfrac{1-\tan^22\theta}{2\tan2\theta}$ || $\cot4\theta=\dfrac{1-\tan^22\theta}{2\tan2\theta}$
qp (iii) | $\cot3\theta=\dfrac{\cot^3\theta-3\cot\theta}{3\cot^2\theta-1}$ || $\cot3\theta=\dfrac{\cot^3\theta-3\cot\theta}{3\cot^2\theta-1}$ || $\cot3\theta=\dfrac{\cot^3\theta-3\cot\theta}{3\cot^2\theta-1}$
endexercise
### 10.4 Sum, Difference and Product of sine and cosine || 10.4 سائن اور کوسائن کا مجموعہ، فرق اور حاصل ضرب || 10.4 د ساین او کوساین مجموعه، توپیر او ضرب
### 10.4.1 Converting Product to Sums or Differences || 10.4.1 حاصل ضرب کو مجموعے یا فرق میں بدلنا || 10.4.1 ضرب په مجموعو یا توپیرونو بدلول
'''+P('We know that','ہم جانتے ہیں کہ','موږ پوهېږو چې')+M(r'\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta\qquad(1)')+P('and','اور','او')+M(r'\sin(\alpha-\beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta\qquad(2)')+P('Adding (1) and (2) we get','(1) اور (2) کو جمع کرنے پر ہمیں ملتا ہے','د (1) او (2) په جمع کولو موږ ترلاسه کوو')
pages[305]=r'''@printed 305
@deco Unit-running header, folio and decorative footer band excluded
m $\sin(\alpha+\beta)+\sin(\alpha-\beta)=2\sin\alpha\cos\beta$
m $\therefore\ 2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)\qquad(3)$
'''+P('Now Subtracting (2) from (1)','اب (1) میں سے (2) تفریق کرنے پر','اوس له (1) نه (2) تفریق کولو سره')+r'''m $\sin(\alpha+\beta)-\sin(\alpha-\beta)=2\cos\alpha\sin\beta$
m $\therefore\ 2\cos\alpha\sin\beta=\sin(\alpha+\beta)-\sin(\alpha-\beta)\qquad(4)$
'''+P('We also know that;','ہم یہ بھی جانتے ہیں کہ؛','موږ دا هم پوهېږو چې؛')+r'''m $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta\qquad(5)$
m $\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta\qquad(6)$
'''+P('Adding (5) and (6) we have,','(5) اور (6) کو جمع کرنے پر ہمارے پاس ہے،','د (5) او (6) په جمع کولو موږ لرو،')+r'''m $\therefore\ 2\cos\alpha\cos\beta=\cos(\alpha+\beta)+\cos(\alpha-\beta)\qquad(7)$
'''+P('Subtracting (6) from (5) we get,','(5) میں سے (6) تفریق کرنے پر ہمیں ملتا ہے،','له (5) نه (6) تفریق کولو سره موږ ترلاسه کوو،')+r'''m $-2\sin\alpha\sin\beta=\cos(\alpha+\beta)-\cos(\alpha-\beta)$
m $\therefore\ 2\sin\alpha\sin\beta=\cos(\alpha-\beta)-\cos(\alpha+\beta)\qquad(8)$
'''+P('So, by converting products into sums or differences we get the following four identities:','یوں حاصل ضرب کو مجموعوں یا فرق میں بدلنے سے ہمیں درج ذیل چار مماثلتیں ملتی ہیں:','نو د ضربونو په مجموعو یا توپیرونو بدلولو سره موږ لاندې څلور هویتونه ترلاسه کوو:')+r'''m $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$
m $2\cos\alpha\sin\beta=\sin(\alpha+\beta)-\sin(\alpha-\beta)$
m $2\cos\alpha\cos\beta=\cos(\alpha+\beta)+\cos(\alpha-\beta)$
m $2\sin\alpha\sin\beta=\cos(\alpha-\beta)-\cos(\alpha+\beta)$
'''+P('These identities are usually called the **Product-to-Sum formulae**.','یہ مماثلتیں عموماً **حاصل ضرب سے مجموعہ کے کلیات** کہلاتی ہیں۔','دا هویتونه معمولاً د **ضرب نه مجموعې فورمولونه** بلل کېږي.')+EX(16,r'Write the product $2\sin5\theta\cos3\theta$ as a sum or difference of sine and cosine.',r'حاصل ضرب $2\sin5\theta\cos3\theta$ کو سائن اور کوسائن کے مجموعے یا فرق کی صورت میں لکھیں۔',r'ضرب $2\sin5\theta\cos3\theta$ د ساین او کوساین د مجموعې یا توپیر په بڼه ولیکئ.')+P(r'**Solution:** Using the identity $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$ we have,',r'**حل:** مماثلت $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$ استعمال کرتے ہوئے ہمارے پاس ہے،',r'**حل:** د هویت $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$ په کارولو موږ لرو،')+r'''m $2\sin5\theta\cos3\theta=\sin(5\theta+3\theta)+\sin(5\theta-3\theta)=\sin8\theta+\sin2\theta$
endexample
'''+EX(17,r'Express $\sin10\theta\cos4\theta$ as a sum or difference.',r'$\sin10\theta\cos4\theta$ کو مجموعے یا فرق کی صورت میں ظاہر کریں۔',r'$\sin10\theta\cos4\theta$ د مجموعې یا توپیر په بڼه وښیئ.')+P(r'**Solution:** Using the identity $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$ we have, $\sin\alpha\cos\beta=\dfrac12[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$',r'**حل:** مماثلت $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$ استعمال کرتے ہوئے ہمارے پاس ہے، $\sin\alpha\cos\beta=\dfrac12[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$',r'**حل:** د هویت $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$ په کارولو موږ لرو، $\sin\alpha\cos\beta=\dfrac12[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$')+r'''m $\sin10\theta\cos4\theta=\dfrac12[\sin(10\theta+4\theta)+\sin(10\theta-4\theta)]=\dfrac12(\sin14\theta+\sin6\theta)$
endexample
'''
pages[306]=r'''@printed 306
@sec 10.4.2 | Converting Sums or Differences to Products || مجموعوں یا فرق کو حاصل ضرب میں بدلنا || مجموعې یا توپیرونه په ضرب بدلول
@deco Unit-running header, folio and decorative footer band excluded
'''+EX(18,r'Write the product $2\cos45^\circ\cos15^\circ$ as a sum or difference.',r'حاصل ضرب $2\cos45^\circ\cos15^\circ$ کو مجموعے یا فرق کی صورت میں لکھیں۔',r'ضرب $2\cos45^\circ\cos15^\circ$ د مجموعې یا توپیر په بڼه ولیکئ.')+P(r'**Solution:** Using the identity $2\cos\alpha\cos\beta=\cos(\alpha+\beta)+\cos(\alpha-\beta)$ we have,',r'**حل:** مماثلت $2\cos\alpha\cos\beta=\cos(\alpha+\beta)+\cos(\alpha-\beta)$ استعمال کرتے ہوئے ہمارے پاس ہے،',r'**حل:** د هویت $2\cos\alpha\cos\beta=\cos(\alpha+\beta)+\cos(\alpha-\beta)$ په کارولو موږ لرو،')+r'''m $\therefore\ 2\cos45^\circ\cos15^\circ=\cos(45^\circ+15^\circ)+\cos(45^\circ-15^\circ)=\cos60^\circ+\cos30^\circ$
endexample
### 10.4.2 Converting Sums or Differences to Products || 10.4.2 مجموعوں یا فرق کو حاصل ضرب میں بدلنا || 10.4.2 مجموعې یا توپیرونه په ضرب بدلول
p Let $\alpha+\beta=\theta\ \cdots(1)$ and $\alpha-\beta=\phi\ \cdots(2)$. Adding (1) and (2), we have $\alpha=\dfrac{\theta+\phi}2$. Subtracting (2) from (1), we have $\beta=\dfrac{\theta-\phi}2$. || فرض کریں $\alpha+\beta=\theta\ \cdots(1)$ اور $\alpha-\beta=\phi\ \cdots(2)$۔ (1) اور (2) کو جمع کرنے پر $\alpha=\dfrac{\theta+\phi}2$ ملتا ہے۔ (1) میں سے (2) تفریق کرنے پر $\beta=\dfrac{\theta-\phi}2$ ملتا ہے۔ || فرض کړئ $\alpha+\beta=\theta\ \cdots(1)$ او $\alpha-\beta=\phi\ \cdots(2)$. د (1) او (2) په جمع کولو $\alpha=\dfrac{\theta+\phi}2$ ترلاسه کېږي. له (1) نه (2) تفریق کولو $\beta=\dfrac{\theta-\phi}2$ ترلاسه کېږي.
p Substituting $\alpha=\dfrac{\theta+\phi}2$ and $\beta=\dfrac{\theta-\phi}2$ in the four identities of section 10.4.1, we get || حصہ 10.4.1 کی چار مماثلتوں میں $\alpha=\dfrac{\theta+\phi}2$ اور $\beta=\dfrac{\theta-\phi}2$ رکھنے پر ہمیں ملتا ہے || د 10.4.1 برخې په څلورو هویتونو کې $\alpha=\dfrac{\theta+\phi}2$ او $\beta=\dfrac{\theta-\phi}2$ ایښودو سره موږ ترلاسه کوو
m $\sin\theta+\sin\phi=2\sin\dfrac{\theta+\phi}2\cos\dfrac{\theta-\phi}2$
m $\sin\theta-\sin\phi=2\cos\dfrac{\theta+\phi}2\sin\dfrac{\theta-\phi}2$
m $\cos\theta+\cos\phi=2\cos\dfrac{\theta+\phi}2\cos\dfrac{\theta-\phi}2$
m $\cos\theta-\cos\phi=-2\sin\dfrac{\theta+\phi}2\sin\dfrac{\theta-\phi}2$
p These identities are usually called the **sum-to-product formulae**. || یہ مماثلتیں عموماً **مجموعہ سے حاصل ضرب کے کلیات** کہلاتی ہیں۔ || دا هویتونه معمولاً د **مجموعې نه ضرب فورمولونه** بلل کېږي.
example 19 | Convert the sum $\sin16^\circ+\sin12^\circ$ into product. || مجموعہ $\sin16^\circ+\sin12^\circ$ کو حاصل ضرب میں بدلیں۔ || مجموعه $\sin16^\circ+\sin12^\circ$ په ضرب بدل کړئ.
p **Solution:** We know that, $\sin\theta+\sin\phi=2\sin\dfrac{\theta+\phi}2\cos\dfrac{\theta-\phi}2$ || **حل:** ہم جانتے ہیں کہ $\sin\theta+\sin\phi=2\sin\dfrac{\theta+\phi}2\cos\dfrac{\theta-\phi}2$ || **حل:** موږ پوهېږو چې $\sin\theta+\sin\phi=2\sin\dfrac{\theta+\phi}2\cos\dfrac{\theta-\phi}2$
'''
for n,t in pages.items():
    open(f'{OUT}\\p{n}.txt','w',encoding='utf8').write(t)
print('ok')
