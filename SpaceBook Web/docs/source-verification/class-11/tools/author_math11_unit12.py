"""Step-by-step SpaceBook solutions for Class 11 Mathematics, Unit 12
(graphs of trigonometric / inverse trigonometric functions, trigonometric equations).
Every answer is worked out here (sympy checks where possible); where the printed key
(p.425-429) disagrees, the step list says so."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math11_answer_authoring import Author, step, S
from math11_phrases import make_put
from m11plot import plot

A = Author(12)
put, flush = make_put(A)
pi = math.pi
def T(en, ur, ps, m=None, svg=None):
    d = step(en, ur, ps, m)
    if svg: d['svg'] = svg
    return d
def KEY(en, ur, ps):
    return T('Note on the printed answer key: ' + en, 'مطبوعہ جوابی کنجی کے بارے میں: ' + ur, 'د چاپ شوې ځوابي کیلي په اړه: ' + ps)
def check(expr):
    """Zero test: symbolic when sympy can, otherwise 50-digit numeric (inverse-trig sums)."""
    if S.simplify(expr) == 0: return
    free = list(expr.free_symbols)
    trials = [dict(zip(free, vals)) for vals in ([S.Rational(3, 7)] * len(free), [S.Rational(5, 3)] * len(free))] if free else [{}]
    for sub in trials:
        assert abs(S.N(expr.subs(sub), 50)) < S.Float('1e-40'), expr

# ═══════════════════════════════ 12.1 ═══════════════════════════════
FORM = lambda m: T('Write the function in the form $y=a\\,f(bx)$ and read off $a$ and $b$.',
                   'تفاعل کو $y=a\\,f(bx)$ کی صورت میں لکھیں اور $a$ اور $b$ معلوم کریں۔',
                   'تابع د $y=a\\,f(bx)$ په بڼه ولیکئ او $a$ او $b$ وټاکئ.', m)
PER_SC = lambda m: T('For $\\sin,\\cos,\\sec,\\csc$ the period is $\\dfrac{2\\pi}{|b|}$.',
                     '$\\sin,\\cos,\\sec,\\csc$ کا دور $\\dfrac{2\\pi}{|b|}$ ہوتا ہے۔',
                     'د $\\sin,\\cos,\\sec,\\csc$ دوره $\\dfrac{2\\pi}{|b|}$ ده.', m)
PER_TC = lambda m: T('For $\\tan$ and $\\cot$ the period is $\\dfrac{\\pi}{|b|}$.',
                     '$\\tan$ اور $\\cot$ کا دور $\\dfrac{\\pi}{|b|}$ ہوتا ہے۔',
                     'د $\\tan$ او $\\cot$ دوره $\\dfrac{\\pi}{|b|}$ ده.', m)
DOM = lambda m: T('Domain: remove the values of $x$ that make the function undefined.',
                  'ساحہ: $x$ کی وہ قیمتیں نکال دیں جن پر تفاعل غیر معین ہو۔',
                  'ساحه: د $x$ هغه ارزښتونه لرې کړئ چې تابع پکې نامعلومه وي.', m)
RNG = lambda m: T('Range: multiply the range of the basic function by $a$.',
                  'رینج: بنیادی تفاعل کے رینج کو $a$ سے ضرب دیں۔',
                  'رینج: د اساسي تابع رینج په $a$ ضرب کړئ.', m)

q1 = [
 ('(i)',   r'$R$; range $[-3,3]$; period $\frac{2\pi}3$',
  [FORM(r'a=3,\ b=3'), PER_SC(r'\text{period}=\frac{2\pi}{3}'), DOM(r'\sin3x\text{ is defined for every real }x\Rightarrow\text{domain}=R'), RNG(r'-1\le\sin3x\le1\Rightarrow-3\le3\sin3x\le3')]),
 ('(ii)',  r'domain $R-\{(2n+1)\pi:n\in Z\}$; range $R$; period $2\pi$',
  [FORM(r'a=1,\ b=\tfrac12'), PER_TC(r'\text{period}=\frac{\pi}{1/2}=2\pi'), DOM(r'\tan\tfrac x2\text{ undefined when }\tfrac x2=(2n+1)\tfrac\pi2\Rightarrow x=(2n+1)\pi'), RNG(r'\tan\text{ takes every real value}\Rightarrow\text{range}=R')]),
 ('(iii)', r'domain $R-\{\frac{n\pi}2:n\in Z\}$; range $R-(-1,1)$; period $\pi$',
  [FORM(r'a=1,\ b=2'), PER_SC(r'\text{period}=\frac{2\pi}{2}=\pi'), DOM(r'\csc2x=\frac1{\sin2x}\text{ undefined when }2x=n\pi\Rightarrow x=\frac{n\pi}2'), RNG(r'|\csc2x|\ge1\Rightarrow\text{range}=(-\infty,-1]\cup[1,\infty)=R-(-1,1)')]),
 ('(iv)',  r'domain $R$; range $[-1,1]$; period $\frac\pi2$',
  [FORM(r'a=1,\ b=4'), PER_SC(r'\text{period}=\frac{2\pi}{4}=\frac\pi2'), DOM(r'\cos4x\text{ is defined for every }x\Rightarrow\text{domain}=R'), RNG(r'-1\le\cos4x\le1')]),
 ('(v)',   r'domain $R-\{(2n+1)\frac\pi4:n\in Z\}$; range $R-(-6,6)$; period $\pi$',
  [FORM(r'a=6,\ b=2'), PER_SC(r'\text{period}=\frac{2\pi}{2}=\pi'), DOM(r'\sec2x=\frac1{\cos2x}\text{ undefined when }2x=(2n+1)\frac\pi2\Rightarrow x=(2n+1)\frac\pi4'), RNG(r'|\sec2x|\ge1\Rightarrow|6\sec2x|\ge6\Rightarrow\text{range}=(-\infty,-6]\cup[6,\infty)')]),
 ('(vi)',  r'domain $R-\{\frac{3n}2:n\in Z\}$; range $R$; period $\frac32$',
  [FORM(r'a=\tfrac72,\ b=\tfrac{2\pi}3'), PER_TC(r'\text{period}=\frac{\pi}{2\pi/3}=\frac32'), DOM(r'\cot\theta\text{ undefined at }\theta=n\pi:\ \frac{2\pi x}3=n\pi\Rightarrow x=\frac{3n}2'), RNG(r'\cot\text{ takes every real value}\Rightarrow\text{range}=R')]),
 ('(vii)', r'domain $R-\{(2n+1)\frac\pi2:n\in Z\}$; range $R$; period $\pi$',
  [FORM(r'a=-\tfrac14,\ b=1'), PER_TC(r'\text{period}=\frac\pi1=\pi'), DOM(r'\tan x\text{ undefined at }x=(2n+1)\frac\pi2'), RNG(r'-\tfrac14\tan x\text{ still takes every real value}\Rightarrow R')]),
 ('(viii)',r'domain $R-\{n\pi:n\in Z\}$; range $R-\left(-\frac12,\frac12\right)$; period $2\pi$',
  [FORM(r'a=\tfrac12,\ b=1'), PER_SC(r'\text{period}=2\pi'), DOM(r'\csc x\text{ undefined when }\sin x=0\Rightarrow x=n\pi'), RNG(r'|\csc x|\ge1\Rightarrow\left|\tfrac12\csc x\right|\ge\tfrac12')]),
 ('(ix)',  r'domain $R-\{4n+2:n\in Z\}$; range $R-(-1,1)$; period $8$',
  [FORM(r'a=1,\ b=\tfrac\pi4'), PER_SC(r'\text{period}=\frac{2\pi}{\pi/4}=8'), DOM(r'\cos\tfrac{\pi x}4=0\iff\tfrac{\pi x}4=(2n+1)\tfrac\pi2\iff x=4n+2'), RNG(r'|\sec\theta|\ge1\Rightarrow\text{range}=R-(-1,1)')]),
]
for p, ans, ss in q1: put('12.1', 1, p, ans, ss)

BOUND = lambda m: T('Use $-1\\le\\sin\\theta\\le1$ (or $-1\\le\\cos\\theta\\le1$) and build the expression step by step.',
                    '$-1\\le\\sin\\theta\\le1$ (یا $-1\\le\\cos\\theta\\le1$) سے شروع کر کے عبارت مرحلہ وار بنائیں۔',
                    'له $-1\\le\\sin\\theta\\le1$ (یا $-1\\le\\cos\\theta\\le1$) پیل وکړئ او عبارت ګام په ګام جوړ کړئ.', m)
put('12.1', 2, '(i)', r'maximum $-\frac32$, minimum $-\frac52$',
    [BOUND(r'-1\le\sin\left(\tfrac13\theta+2\right)\le1\Rightarrow-\tfrac12\le\tfrac12\sin(\cdot)\le\tfrac12'),
     T('Add $-2$ to every part.', 'ہر حصے میں $-2$ جمع کریں۔', 'هرې برخې ته $-2$ ورزیات کړئ.', r'-\tfrac52\le y\le-\tfrac32\Rightarrow y_{\max}=-\tfrac32,\ y_{\min}=-\tfrac52')])
put('12.1', 2, '(ii)', r'maximum $9$, minimum $1$',
    [BOUND(r'-1\le\sin(\theta+30^\circ)\le1\Rightarrow-4\le-4\sin(\cdot)\le4'),
     T('Add 5. The largest value occurs when $\\sin(\\theta+30^\\circ)=-1$, the smallest when it equals $1$.',
       '5 جمع کریں۔ سب سے بڑی قیمت $\\sin(\\theta+30^\\circ)=-1$ پر اور سب سے چھوٹی $1$ پر ہے۔',
       '5 ورزیات کړئ. تر ټولو لوی ارزښت د $\\sin(\\theta+30^\\circ)=-1$ پر مهال او تر ټولو کوچنی د $1$ پر مهال دی.', r'1\le y\le9')])
put('12.1', 2, '(iii)', r'maximum $\frac19$, minimum $\frac1{29}$',
    [BOUND(r'-1\le\sin(3\theta-45^\circ)\le1\Rightarrow-10\le10\sin(\cdot)\le10'),
     T('So the denominator lies between 9 and 29 (always positive).', 'لہٰذا مخرج 9 اور 29 کے درمیان ہے (ہمیشہ مثبت)۔', 'نو مخرج د 9 او 29 ترمنځ دی (تل مثبت).', r'9\le19-10\sin(3\theta-45^\circ)\le29'),
     T('A fraction with numerator 1 is largest when the denominator is smallest.', 'جس کسر کا شمار کنندہ 1 ہو وہ مخرج کے سب سے چھوٹا ہونے پر سب سے بڑا ہوتا ہے۔', 'هغه کسر چې صورت یې 1 وي، د مخرج د تر ټولو کوچني کېدو پر مهال تر ټولو لوی وي.', r'\frac1{29}\le y\le\frac19')])
put('12.1', 2, '(iv)', r'least positive value $\frac14$, greatest negative value $-\frac14$ (the function itself is unbounded)',
    [BOUND(r'-1\le\cos2\pi\theta\le1,\ \cos2\pi\theta\ne0'),
     T('When $0<\\cos2\\pi\\theta\\le1$, $y\\ge\\frac14$; when $-1\\le\\cos2\\pi\\theta<0$, $y\\le-\\frac14$.',
       'جب $0<\\cos2\\pi\\theta\\le1$ تو $y\\ge\\frac14$؛ جب $-1\\le\\cos2\\pi\\theta<0$ تو $y\\le-\\frac14$۔',
       'کله چې $0<\\cos2\\pi\\theta\\le1$ وي $y\\ge\\frac14$؛ کله چې $-1\\le\\cos2\\pi\\theta<0$ وي $y\\le-\\frac14$.', r'y=\frac1{4\cos2\pi\theta}\in\left(-\infty,-\tfrac14\right]\cup\left[\tfrac14,\infty\right)'),
     T('So the turning values are $\\frac14$ (a minimum on the positive branches) and $-\\frac14$ (a maximum on the negative branches), as in the printed key.',
       'لہٰذا موڑ کی قیمتیں $\\frac14$ (مثبت شاخوں پر کم سے کم) اور $-\\frac14$ (منفی شاخوں پر زیادہ سے زیادہ) ہیں، جیسا کہ مطبوعہ کنجی میں ہے۔',
       'نو د اوښتو ارزښتونه $\\frac14$ (په مثبتو څانګو کې لږ تر لږه) او $-\\frac14$ (په منفي څانګو کې زیات نه زیات) دي، لکه په چاپ شوې کیلي کې.')])

# ═══════════════════════════════ 12.2 ═══════════════════════════════
TABLE = lambda m: T('Make a table of values at the key angles.', 'اہم زاویوں پر قیمتوں کا جدول بنائیں۔', 'په مهمو زاویو د ارزښتونو جدول جوړ کړئ.', m)
PLOT = lambda svg: T('Plot the points and join them with a smooth curve (dashed lines are asymptotes).',
                     'نقاط لگا کر ہموار خم سے ملائیں (ٹوٹی لکیریں متقارب خطوط ہیں)۔',
                     'ټکي کېږدئ او په هوار منحني یې سره ونښلوئ (ټوټه کرښې مجانبونه دي).', None, svg)
sec = lambda x: 1 / math.cos(x)
csc = lambda x: 1 / math.sin(x)
cot = lambda x: math.cos(x) / math.sin(x)
put('12.2', 1, '(i)', r'A sine wave of amplitude 2 and period $2\pi$: $0$ at $0,\pi,2\pi$; maximum $2$ at $\frac\pi2$; minimum $-2$ at $\frac{3\pi}2$.',
    [TABLE(r'\begin{array}{c|ccccc}x&0&\frac\pi2&\pi&\frac{3\pi}2&2\pi\\\hline y&0&2&0&-2&0\end{array}'),
     PLOT(plot([(lambda x: 2*math.sin(x), '#2563eb', 'y = 2 sin x')], 0, 2*pi, -2.5, 2.5, title='y = 2 sin x'))])
put('12.2', 1, '(ii)', r'Two complete cycles (period $\pi$) between $1$ and $-1$: $y=1$ at $0,\pi,2\pi$; $y=-1$ at $\frac\pi2,\frac{3\pi}2$; zeros at $\frac\pi4,\frac{3\pi}4,\frac{5\pi}4,\frac{7\pi}4$.',
    [TABLE(r'\begin{array}{c|ccccccccc}x&0&\frac\pi4&\frac\pi2&\frac{3\pi}4&\pi&\frac{5\pi}4&\frac{3\pi}2&\frac{7\pi}4&2\pi\\\hline y&1&0&-1&0&1&0&-1&0&1\end{array}'),
     PLOT(plot([(lambda x: math.cos(2*x), '#2563eb', 'y = cos 2x')], 0, 2*pi, -1.5, 1.5, xstep=pi/4, title='y = cos 2x'))])
put('12.2', 1, '(iii)', r'The arch of $\sin x$ moved 4 units down: from $(0,-4)$ up to $\left(\frac\pi2,-3\right)$ and back to $(\pi,-4)$.',
    [TABLE(r'\begin{array}{c|ccccc}x&0&\frac\pi4&\frac\pi2&\frac{3\pi}4&\pi\\\hline y&-4&-3.29&-3&-3.29&-4\end{array}'),
     PLOT(plot([(lambda x: -4+math.sin(x), '#2563eb', 'y = −4 + sin x')], 0, pi, -5, 1, xstep=pi/4, title='y = -4 + sin x'))])
put('12.2', 1, '(iv)', r'Branches of $-\cot x$, period $\pi$, vertical asymptotes $x=-\pi,0,\pi$; zeros at $x=\pm\frac\pi2$; each branch rises from $-\infty$ to $+\infty$.',
    [TABLE(r'\begin{array}{c|ccccccc}x&-\frac{3\pi}4&-\frac\pi2&-\frac\pi4&\frac\pi4&\frac\pi2&\frac{3\pi}4\\\hline y&-1&0&1&-1&0&1\end{array}'),
     T('$\\cot x$ is undefined at $x=-\\pi,0,\\pi$, so these are vertical asymptotes.', '$x=-\\pi,0,\\pi$ پر $\\cot x$ غیر معین ہے، اس لیے یہ عمودی متقارب خطوط ہیں۔', 'په $x=-\\pi,0,\\pi$ کې $\\cot x$ نامعلوم دی، نو دا عمودي مجانبونه دي.'),
     PLOT(plot([(lambda x: -cot(x), '#2563eb', 'y = −cot x')], -pi, pi, -4, 4, xstep=pi/2, ystep=2, asym=(-pi, 0, pi), title='y = -cot x'))])
put('12.2', 1, '(v)', r'U-shaped branches of $2\csc2x$ (period $\pi$): minimum value $2$ at $x=\frac\pi4,\frac{5\pi}4$, maximum value $-2$ at $x=\frac{3\pi}4,\frac{7\pi}4$; asymptotes $x=0,\frac\pi2,\pi,\frac{3\pi}2,2\pi$.',
    [TABLE(r'\begin{array}{c|cccc}x&\frac\pi4&\frac{3\pi}4&\frac{5\pi}4&\frac{7\pi}4\\\hline y&2&-2&2&-2\end{array}'),
     T('$\\csc2x$ is undefined where $\\sin2x=0$, i.e. $x=\\frac{n\\pi}2$.', 'جہاں $\\sin2x=0$ یعنی $x=\\frac{n\\pi}2$ وہاں $\\csc2x$ غیر معین ہے۔', 'چېرته چې $\\sin2x=0$ یعنې $x=\\frac{n\\pi}2$، هلته $\\csc2x$ نامعلوم دی.'),
     PLOT(plot([(lambda x: 2*csc(2*x), '#2563eb', 'y = 2 csc 2x')], 0, 2*pi, -8, 8, xstep=pi/2, ystep=2, asym=(0, pi/2, pi, 3*pi/2, 2*pi), title='y = 2 csc 2x'))])
put('12.2', 1, '(vi)', r'On $\pi\le x\le2\pi$: $y=\sec\frac x2$ goes from $-\infty$ near $x=\pi$ (asymptote) up to $-1$ at $x=2\pi$; e.g. $y=-2$ at $x=\frac{4\pi}3$.',
    [TABLE(r'\begin{array}{c|cccc}x&\frac{7\pi}6&\frac{4\pi}3&\frac{3\pi}2&2\pi\\\hline y&-3.86&-2&-1.41&-1\end{array}'),
     T('$\\cos\\frac x2=0$ at $x=\\pi$, so $x=\\pi$ is a vertical asymptote.', '$x=\\pi$ پر $\\cos\\frac x2=0$، اس لیے $x=\\pi$ عمودی متقارب خط ہے۔', 'په $x=\\pi$ کې $\\cos\\frac x2=0$، نو $x=\\pi$ عمودي مجانب دی.'),
     PLOT(plot([(lambda x: sec(x/2), '#2563eb', 'y = sec(x/2)')], pi, 2*pi, -6, 1, xstep=pi/4, ystep=1, asym=(pi,), title='y = sec(x/2)'))])

GUESS = lambda name, m: T(f'The graph is a {name} curve; for $y=a\\sin b\\theta$ or $a\\cos b\\theta$: period $\\frac{{2\\pi}}{{|b|}}$, frequency $=\\frac1{{\\text{{period}}}}$, amplitude $|a|$.',
                          'یہ خم $\\sin/\\cos$ کی موج ہے؛ $y=a\\sin b\\theta$ یا $a\\cos b\\theta$ کے لیے دور $\\frac{2\\pi}{|b|}$، تعدد $=\\frac1{\\text{دور}}$، حیطہ $|a|$۔',
                          'دا منحني د $\\sin/\\cos$ څپه ده؛ د $y=a\\sin b\\theta$ یا $a\\cos b\\theta$ لپاره دوره $\\frac{2\\pi}{|b|}$، فریکونسي $=\\frac1{\\text{دوره}}$، امپلیتوډ $|a|$.', m)
for p, f, lab, name, b, per, fr in [('(i)', lambda t: math.cos(2*t), 'y = cos 2θ', 'cosine', '2', r'\pi', r'\frac1\pi'),
                                    ('(ii)', lambda t: math.sin(6*t), 'y = sin 6θ', 'sine', '6', r'\frac\pi3', r'\frac3\pi'),
                                    ('(iii)', lambda t: math.sin(pi*t), 'y = sin πθ', 'sine', r'\pi', '2', r'\frac12'),
                                    ('(iv)', lambda t: math.cos(pi/2*t), 'y = cos (π/2)θ', 'cosine', r'\tfrac\pi2', '4', r'\frac14')]:
    numeric = p in ('(iii)', '(iv)')
    put('12.2', 2, p, f'Period ${per}$, frequency ${fr}$, amplitude $1$',
        [GUESS(name, fr'a=1,\ b={b}\Rightarrow\text{{period}}=\frac{{2\pi}}{{{b}}}={per},\ \text{{frequency}}={fr},\ \text{{amplitude}}=1'),
         T('Sketch for checking (one or more complete cycles).', 'جانچ کے لیے خاکہ (ایک یا زیادہ مکمل چکر)۔', 'د ازمېښت لپاره خاکه (یو یا څو بشپړ دورونه).', None,
           plot([(f, '#2563eb', lab)], 0, 8 if numeric else 2*pi, -1.5, 1.5, xstep=1 if numeric else pi/2, xlabels=(lambda x: f'{x:g}') if numeric else None, title=lab))])

EXP = lambda m: T('Expand with the sum/difference formula.', 'مجموعہ/فرق کے کلیے سے کھولیں۔', 'د جمع/تفریق فورمول سره یې پراخ کړئ.', m)
VAL = lambda m: T('Substitute the known values and simplify.', 'معلوم قیمتیں رکھ کر مختصر کریں۔', 'معلوم ارزښتونه کېږدئ او ساده یې کړئ.', m)
QED = T('Hence proved.', 'ثابت ہوا۔', 'ثابت شو.')
th = S.Symbol('theta')
ids = [('(i)', S.sin(S.pi/2+th)-S.cos(th), r'\sin\left(\tfrac\pi2+\theta\right)=\sin\tfrac\pi2\cos\theta+\cos\tfrac\pi2\sin\theta', r'=1\cdot\cos\theta+0\cdot\sin\theta=\cos\theta'),
       ('(ii)', S.cos(S.pi/2+th)+S.sin(th), r'\cos\left(\tfrac\pi2+\theta\right)=\cos\tfrac\pi2\cos\theta-\sin\tfrac\pi2\sin\theta', r'=0\cdot\cos\theta-1\cdot\sin\theta=-\sin\theta'),
       ('(iii)', S.sin(S.pi-th)-S.sin(th), r'\sin(\pi-\theta)=\sin\pi\cos\theta-\cos\pi\sin\theta', r'=0-(-1)\sin\theta=\sin\theta'),
       ('(iv)', S.cos(S.pi-th)+S.cos(th), r'\cos(\pi-\theta)=\cos\pi\cos\theta+\sin\pi\sin\theta', r'=-\cos\theta+0=-\cos\theta'),
       ('(v)', S.tan(S.pi-th)+S.tan(th), r'\tan(\pi-\theta)=\frac{\sin(\pi-\theta)}{\cos(\pi-\theta)}', r'=\frac{\sin\theta}{-\cos\theta}=-\tan\theta'),
       ('(vi)', S.tan(2*S.pi-th)+S.tan(th), r'\tan(2\pi-\theta)=\tan(-\theta)\ \ (\text{period of }\tan\text{ divides }2\pi)', r'=-\tan\theta\ \ (\tan\text{ is an odd function})')]
for p, e, a, b in ids:
    check(e)
    put('12.2', 3, p, 'Proved (see the steps).', [EXP(a), VAL(b), QED])
PER = lambda m: T('Use the periodicity: $\\cos2k\\pi=1$ and $\\sin2k\\pi=0$ for every integer $k$.',
                  'دوریت استعمال کریں: ہر صحیح عدد $k$ کے لیے $\\cos2k\\pi=1$ اور $\\sin2k\\pi=0$۔',
                  'دوره ییز خاصیت وکاروئ: د هر صحیح عدد $k$ لپاره $\\cos2k\\pi=1$ او $\\sin2k\\pi=0$.', m)
dd = [('(i)', r'\sin(\theta+2k\pi)=\sin\theta\cos2k\pi+\cos\theta\sin2k\pi=\sin\theta\cdot1+\cos\theta\cdot0=\sin\theta'),
      ('(ii)', r'\cos(\theta+2k\pi)=\cos\theta\cos2k\pi-\sin\theta\sin2k\pi=\cos\theta\cdot1-\sin\theta\cdot0=\cos\theta'),
      ('(iii)', r'\tan(\theta+2k\pi)=\frac{\sin(\theta+2k\pi)}{\cos(\theta+2k\pi)}=\frac{\sin\theta}{\cos\theta}=\tan\theta'),
      ('(iv)', r'\cot(\theta+2k\pi)=\frac{\cos(\theta+2k\pi)}{\sin(\theta+2k\pi)}=\frac{\cos\theta}{\sin\theta}=\cot\theta'),
      ('(v)', r'\sec(\theta+2k\pi)=\frac1{\cos(\theta+2k\pi)}=\frac1{\cos\theta}=\sec\theta'),
      ('(vi)', r'\csc(\theta+2k\pi)=\frac1{\sin(\theta+2k\pi)}=\frac1{\sin\theta}=\csc\theta')]
for p, m in dd:
    first = PER(r'\cos2k\pi=1,\ \sin2k\pi=0') if p in ('(i)', '(ii)') else T('Use parts (i) and (ii): $\\sin(\\theta+2k\\pi)=\\sin\\theta$, $\\cos(\\theta+2k\\pi)=\\cos\\theta$.', 'حصہ (i) اور (ii) استعمال کریں: $\\sin(\\theta+2k\\pi)=\\sin\\theta$، $\\cos(\\theta+2k\\pi)=\\cos\\theta$۔', '(i) او (ii) برخې وکاروئ: $\\sin(\\theta+2k\\pi)=\\sin\\theta$، $\\cos(\\theta+2k\\pi)=\\cos\\theta$.')
    put('12.2', 4, p, 'Proved (see the steps).', [first, VAL(m), QED])

# ═══════════════════════════════ 12.3 ═══════════════════════════════
GR = lambda svg: T('Draw $y=f(\\theta)$ and the horizontal line $y=c$ over one period; the red points are the solutions in $[0,2\\pi)$.',
                   'ایک دور پر $y=f(\\theta)$ اور افقی خط $y=c$ کھینچیں؛ سرخ نقاط $[0,2\\pi)$ میں حل ہیں۔',
                   'په یوه دوره کې $y=f(\\theta)$ او افقي کرښه $y=c$ رسم کړئ؛ سره ټکي په $[0,2\\pi)$ کې حلونه دي.', None, svg)
GEN = lambda m: T('Add whole periods to get all solutions.', 'تمام حل حاصل کرنے کے لیے پورے دور جمع کریں۔', 'د ټولو حلونو لپاره بشپړې دورې ورزیاتې کړئ.', m)
tanf = lambda t: math.tan(t)
g3 = [('(i)', math.sin, 'sin θ', math.sqrt(2)/2, [pi/4, 3*pi/4], r'\theta=\frac\pi4+2n\pi\ \text{or}\ \theta=\frac{3\pi}4+2n\pi,\ n\in Z', 2),
      ('(ii)', math.cos, 'cos θ', -math.sqrt(3)/2, [5*pi/6, 7*pi/6], r'\theta=\frac{5\pi}6+2n\pi\ \text{or}\ \theta=\frac{7\pi}6+2n\pi,\ n\in Z', 2),
      ('(iii)', tanf, 'tan θ', math.sqrt(3), [pi/3, 4*pi/3], r'\theta=\frac\pi3+n\pi,\ n\in Z', 1),
      ('(iv)', math.cos, 'cos θ', 0.5, [pi/3, 5*pi/3], r'\theta=\frac\pi3+2n\pi\ \text{or}\ \theta=\frac{5\pi}3+2n\pi,\ n\in Z', 2),
      ('(v)', tanf, 'tan θ', -1.0, [3*pi/4, 7*pi/4], r'\theta=\frac{3\pi}4+n\pi,\ n\in Z', 1),
      ('(vi)', math.sin, 'sin θ', -0.5, [7*pi/6, 11*pi/6], r'\theta=\frac{7\pi}6+2n\pi\ \text{or}\ \theta=\frac{11\pi}6+2n\pi,\ n\in Z', 2)]
for p, f, lab, c, roots, gen, kind in g3:
    for r in roots: assert abs(f(r) - c) < 1e-9
    isTan = f is tanf
    svg = plot([(f, '#2563eb', 'y = ' + lab)], 0, 2*pi, -3 if isTan else -1.5, 3 if isTan else 1.5, xstep=pi/2,
               asym=(pi/2, 3*pi/2) if isTan else (), hlines=[(c, '#16a34a')], points=[(r, c, '') for r in roots], title=lab)
    rs = r',\ '.join(S.latex(S.nsimplify(r/pi)*S.pi) for r in roots)
    note = T('The two red points differ by $\\pi$, the period of $\\tan$, so one family covers both.' if isTan else 'The two points in one period give two families, each repeating every $2\\pi$.',
             'دونوں سرخ نقاط میں $\\pi$ (یعنی $\\tan$ کے دور) کا فرق ہے، اس لیے ایک ہی خاندان دونوں کو شامل کرتا ہے۔' if isTan else 'ایک دور میں دو نقاط سے حل کے دو خاندان بنتے ہیں جو ہر $2\\pi$ پر دہرائے جاتے ہیں۔',
             'دواړه سره ټکي $\\pi$ (د $\\tan$ دوره) توپیر لري، نو یوه کورنۍ دواړه رانغاړي.' if isTan else 'په یوه دوره کې دوه ټکي دوه کورنۍ جوړوي چې هره یې په هر $2\\pi$ کې تکرارېږي.', r'\theta=' + rs)
    put('12.3', 1, p, '$' + gen + '$', [GR(svg), note, GEN(gen)])

# ═══════════════════════════════ 12.4 ═══════════════════════════════
PRIN = lambda m: T('First find the angle in the principal interval that has the given value.', 'پہلے اصل وقفے میں وہ زاویہ معلوم کریں جس کی یہ قیمت ہو۔', 'لومړی په اصلي واټن کې هغه زاویه ومومئ چې دا ارزښت ولري.', m)
ALL = lambda m: T('The relation $\\text{arc}\\,f$ (lower case) means every angle with that value, so add the general solution.', '$\\text{arc}\\,f$ (چھوٹے حرف) سے مراد اس قیمت والے تمام زاویے ہیں، اس لیے عمومی حل لکھیں۔', '$\\text{arc}\\,f$ (کوچنی توری) ټولې هغه زاویې دي چې دا ارزښت لري، نو عمومي حل ولیکئ.', m)
put('12.4', 1, '(i)', r'$\left\{-\frac\pi2+2n\pi:n\in Z\right\}$', [PRIN(r'\sin\left(-\tfrac\pi2\right)=-1'), ALL(r'\sin\theta=-1\iff\theta=-\frac\pi2+2n\pi\ \left(=\tfrac{3\pi}2+2m\pi\right)'),
    KEY('the two sets printed, $-\\frac\\pi2+2n\\pi$ and $\\frac{3\\pi}2-2n\\pi$, are the same set.', 'چھپے ہوئے دونوں سیٹ $-\\frac\\pi2+2n\\pi$ اور $\\frac{3\\pi}2-2n\\pi$ ایک ہی سیٹ ہیں۔', 'چاپ شوي دواړه سیټونه $-\\frac\\pi2+2n\\pi$ او $\\frac{3\\pi}2-2n\\pi$ یو شان دي.')])
put('12.4', 1, '(ii)', r'$\left\{\frac{3\pi}4+2n\pi\right\}\cup\left\{\frac{5\pi}4+2n\pi\right\},\ n\in Z$', [PRIN(r'\cos\tfrac{3\pi}4=-\tfrac{\sqrt2}2'), ALL(r'\cos\theta=-\tfrac{\sqrt2}2\iff\theta=\pm\tfrac{3\pi}4+2n\pi,\ \text{i.e. }\tfrac{3\pi}4+2n\pi\text{ or }\tfrac{5\pi}4+2n\pi'),
    KEY('the first set is printed as $\\frac{3\\pi}4+2m$; it should be $\\frac{3\\pi}4+2m\\pi$.', 'پہلا سیٹ $\\frac{3\\pi}4+2m$ چھپا ہے؛ درست $\\frac{3\\pi}4+2m\\pi$ ہے۔', 'لومړی سیټ $\\frac{3\\pi}4+2m$ چاپ شوی؛ سم یې $\\frac{3\\pi}4+2m\\pi$ دی.')])
put('12.4', 1, '(iii)', r'$\left\{-\frac\pi6+n\pi:n\in Z\right\}$', [PRIN(r'\tan\left(-\tfrac\pi6\right)=-\tfrac1{\sqrt3}=-\tfrac{\sqrt3}3'), ALL(r'\tan\theta=-\tfrac{\sqrt3}3\iff\theta=-\frac\pi6+n\pi\ \ (\text{same as }-\tfrac\pi6+2n\pi\text{ together with }\tfrac{5\pi}6+2n\pi)')])
put('12.4', 2, '(i)', r'$\pi+2n\pi,\ n\in Z$', [VAL(r'\tan\tfrac{3\pi}4=-1'), ALL(r'\text{arc}\cos(-1):\ \cos\theta=-1\iff\theta=\pi+2n\pi')])
put('12.4', 2, '(ii)', r'$\frac12$', [PRIN(r'\text{Tan}^{-1}\tfrac1{\sqrt3}=\tfrac\pi6\ \ \left(\tan\tfrac\pi6=\tfrac1{\sqrt3}\right)'), VAL(r'\sin\tfrac\pi6=\tfrac12')])
put('12.4', 2, '(iii)', r'$\left\{-\frac12,\frac12\right\}$', [ALL(r'\cos\theta=-\tfrac{\sqrt3}2\iff\theta=\tfrac{5\pi}6+2n\pi\ \text{or}\ \tfrac{7\pi}6+2n\pi'),
    VAL(r'\sin\tfrac{5\pi}6=\tfrac12,\quad\sin\tfrac{7\pi}6=-\tfrac12\Rightarrow\text{value set }\left\{-\tfrac12,\tfrac12\right\}')])
put('12.4', 2, '(iv)', r'$-\frac34$ (taking the principal angle)', [PRIN(r'\theta=\text{Arc}\cos\left(-\tfrac45\right)\in\left(\tfrac\pi2,\pi\right),\ \cos\theta=-\tfrac45'),
    T('Find $\\sin\\theta$ (positive in the second quadrant).', '$\\sin\\theta$ معلوم کریں (دوسرے ربع میں مثبت)۔', '$\\sin\\theta$ ومومئ (په دویمه ربع کې مثبت).', r'\sin\theta=\sqrt{1-\tfrac{16}{25}}=\tfrac35'),
    VAL(r'\tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{3/5}{-4/5}=-\frac34')])
for p, a, b, ans in [('(i)', r'\text{Sin}^{-1}\tfrac{\sqrt2}2=\tfrac\pi4', r'\cos\tfrac\pi4=\tfrac{\sqrt2}2', r'\frac{\sqrt2}2'),
                     ('(ii)', r'\text{Cos}^{-1}\tfrac{\sqrt3}2=\tfrac\pi6', r'\tan\tfrac\pi6=\tfrac1{\sqrt3}=\tfrac{\sqrt3}3', r'\frac{\sqrt3}3'),
                     ('(iii)', r'\text{Cos}^{-1}\tfrac12=\tfrac\pi3', r'\sec\tfrac\pi3=\tfrac1{\cos\pi/3}=2', '2'),
                     ('(iv)', r'\text{Tan}^{-1}1=\tfrac\pi4', r'\csc\tfrac\pi4=\tfrac1{\sin\pi/4}=\sqrt2', r'\sqrt2'),
                     ('(v)', r'\text{Tan}^{-1}(-1)=-\tfrac\pi4', r'\sin\left(-\tfrac\pi4\right)=-\tfrac{\sqrt2}2', r'-\frac{\sqrt2}2'),
                     ('(vi)', r'\text{Sin}^{-1}\tfrac12=\tfrac\pi6', r'\sec\tfrac\pi6=\tfrac1{\cos\pi/6}=\tfrac2{\sqrt3}=\tfrac{2\sqrt3}3', r'\frac{2\sqrt3}3')]:
    put('12.4', 3, p, '$' + ans + '$', [PRIN(a), VAL(b)])
LET = lambda m: T('Let the inverse function equal $\\theta$ and write the ordinary trigonometric relation.', 'معکوس تفاعل کو $\\theta$ فرض کریں اور عام مثلثی تعلق لکھیں۔', 'معکوس تابع $\\theta$ فرض کړئ او عادي مثلثاتي اړیکه ولیکئ.', m)
put('12.4', 4, 'i)', '$u$', [LET(r'\theta=\text{Sin}^{-1}\tfrac1u\Rightarrow\sin\theta=\tfrac1u\ \ (u\ge1)'), VAL(r'\csc\theta=\frac1{\sin\theta}=u')])
put('12.4', 4, 'ii)', '$u$', [LET(r'\theta=\text{Tan}^{-1}u\Rightarrow\tan\theta=u'), VAL(r'\tan(\text{Tan}^{-1}u)=\tan\theta=u')])
put('12.4', 4, 'iii)', '$u$', [LET(r'\theta=\text{Cos}^{-1}\tfrac1{\sqrt{1+u^2}}\in\left(0,\tfrac\pi2\right),\ \cos\theta=\tfrac1{\sqrt{1+u^2}}'),
    T('Find $\\sin\\theta$ (positive since $\\theta$ is acute).', '$\\sin\\theta$ معلوم کریں (حادہ زاویہ ہونے سے مثبت)۔', '$\\sin\\theta$ ومومئ (د حاده زاویې له امله مثبت).', r'\sin\theta=\sqrt{1-\tfrac1{1+u^2}}=\tfrac u{\sqrt{1+u^2}}'),
    VAL(r'\tan\theta=\frac{u/\sqrt{1+u^2}}{1/\sqrt{1+u^2}}=u')])
put('12.4', 4, 'iv)', r'$\sqrt{1-u^2}$ (for $0<u\le1$)', [T('$\\text{Cos}^{-1}(\\cos t)=t$ whenever $t$ lies in $[0,\\pi]$.', 'جب $t$ وقفہ $[0,\\pi]$ میں ہو تو $\\text{Cos}^{-1}(\\cos t)=t$۔', 'کله چې $t$ په $[0,\\pi]$ کې وي، $\\text{Cos}^{-1}(\\cos t)=t$.', r't=\sqrt{1-u^2}\ \text{needs }0<u\le1,\ \text{then }0\le t<1<\pi'),
    VAL(r'\text{Cos}^{-1}\left(\cos\sqrt{1-u^2}\right)=\sqrt{1-u^2}')])

# ═══════════════════════════════ 12.5 ═══════════════════════════════
put('12.5', 1, '(i)', r'$x=\frac\pi3$', [PRIN(r'\text{Sin}^{-1}\tfrac12=\tfrac\pi6'), VAL(r'\tfrac\pi6=\tfrac\pi2-x\Rightarrow x=\tfrac\pi2-\tfrac\pi6=\tfrac\pi3')])
put('12.5', 1, '(ii)', r'$x=\frac{\sqrt3}2$', [PRIN(r'\text{Cos}^{-1}\tfrac{\sqrt3}2=\tfrac\pi6'), VAL(r'\tfrac\pi6=\tfrac\pi2-\text{Sin}^{-1}x\Rightarrow\text{Sin}^{-1}x=\tfrac\pi3\Rightarrow x=\sin\tfrac\pi3=\tfrac{\sqrt3}2')])
RANGE = lambda m: T('Check that the angle obtained lies in the principal range of the inverse function.', 'جانچیں کہ حاصل شدہ زاویہ معکوس تفاعل کی اصل حد میں ہے۔', 'وڅېړئ چې ترلاسه شوې زاویه د معکوس تابع په اصلي حد کې ده.', m)
put('12.5', 2, '(i)', 'Proved (see the steps).', [LET(r'\theta=\text{Sin}^{-1}x\Rightarrow x=\sin\theta,\ -\tfrac\pi2\le\theta\le\tfrac\pi2'),
    VAL(r'x=\sin\theta=\cos\left(\tfrac\pi2-\theta\right)'), RANGE(r'0\le\tfrac\pi2-\theta\le\pi\Rightarrow\text{Cos}^{-1}x=\tfrac\pi2-\theta'),
    VAL(r'\text{Sin}^{-1}x+\text{Cos}^{-1}x=\theta+\tfrac\pi2-\theta=\tfrac\pi2'), QED])
put('12.5', 2, '(ii)', r'Proved for $x>0$ (for $x<0$ the sum is $-\frac\pi2$).', [LET(r'\theta=\text{Tan}^{-1}x,\ x>0\Rightarrow0<\theta<\tfrac\pi2'),
    VAL(r'\tfrac1x=\cot\theta=\tan\left(\tfrac\pi2-\theta\right)'), RANGE(r'0<\tfrac\pi2-\theta<\tfrac\pi2\Rightarrow\text{Tan}^{-1}\tfrac1x=\tfrac\pi2-\theta'),
    VAL(r'\text{Tan}^{-1}x+\text{Tan}^{-1}\tfrac1x=\tfrac\pi2'), QED])
put('12.5', 2, '(iii)', 'Proved (see the steps).', [LET(r'\theta=\text{Arc}\tan x\in\left(-\tfrac\pi2,\tfrac\pi2\right),\ \tan\theta=x'),
    T('Use $\\sec^2\\theta=1+\\tan^2\\theta$; $\\sec\\theta>0$ in this interval.', '$\\sec^2\\theta=1+\\tan^2\\theta$ استعمال کریں؛ اس وقفے میں $\\sec\\theta>0$۔', '$\\sec^2\\theta=1+\\tan^2\\theta$ وکاروئ؛ په دې واټن کې $\\sec\\theta>0$.', r'\sec\theta=\sqrt{1+x^2}'), QED])
put('12.5', 2, '(iv)', 'Proved (see the steps).', [LET(r'\theta=\text{Sin}^{-1}x,\ \sin\theta=x,\ -\tfrac\pi2<\theta<\tfrac\pi2'),
    T('$\\cos\\theta\\ge0$ in this interval.', 'اس وقفے میں $\\cos\\theta\\ge0$۔', 'په دې واټن کې $\\cos\\theta\\ge0$.', r'\cos\theta=\sqrt{1-x^2}'),
    VAL(r'\tan\theta=\frac{\sin\theta}{\cos\theta}=\frac x{\sqrt{1-x^2}}'), QED])
put('12.5', 3, '(i)', r'$\frac45$', [T('Use $\\sin\\left(\\frac\\pi2-\\theta\\right)=\\cos\\theta$.', '$\\sin\\left(\\frac\\pi2-\\theta\\right)=\\cos\\theta$ استعمال کریں۔', '$\\sin\\left(\\frac\\pi2-\\theta\\right)=\\cos\\theta$ وکاروئ.', r'\sin\left[\tfrac\pi2-\text{Cos}^{-1}\tfrac45\right]=\cos\left(\text{Cos}^{-1}\tfrac45\right)=\tfrac45')])
put('12.5', 3, '(ii)', 'Does not exist.', [T('$\\text{Arc}\\cos t$ is defined only for $-1\\le t\\le1$.', '$\\text{Arc}\\cos t$ صرف $-1\\le t\\le1$ کے لیے معین ہے۔', '$\\text{Arc}\\cos t$ یوازې د $-1\\le t\\le1$ لپاره ټاکلی دی.', r'\tfrac\pi2\approx1.571>1\Rightarrow\text{Arc}\cos\tfrac\pi2\text{ is undefined}'),
    T('So the whole expression has no value.', 'لہٰذا پوری عبارت کی کوئی قیمت نہیں۔', 'نو ټول عبارت هېڅ ارزښت نه لري.')])
put('12.5', 4, '(i)', 'Proved (see the steps).', [LET(r'A=\text{Sin}^{-1}x,\ B=\text{Sin}^{-1}y:\ \sin A=x,\ \sin B=y,\ \cos A=\sqrt{1-x^2},\ \cos B=\sqrt{1-y^2}'),
    EXP(r'\cos(A-B)=\cos A\cos B+\sin A\sin B'), VAL(r'=\sqrt{1-x^2}\sqrt{1-y^2}+xy=\sqrt{(1-x^2)(1-y^2)}+xy'), QED])
put('12.5', 4, '(ii)', 'Proved (see the steps).', [LET(r'\theta=\text{Sin}^{-1}x\Rightarrow\sin\theta=x'), T('Use $\\cos2\\theta=1-2\\sin^2\\theta$.', '$\\cos2\\theta=1-2\\sin^2\\theta$ استعمال کریں۔', '$\\cos2\\theta=1-2\\sin^2\\theta$ وکاروئ.', r'\cos(2\,\text{Sin}^{-1}x)=1-2x^2'), QED])
put('12.5', 4, '(iii)', 'Proved (see the steps).', [LET(r'\theta=\text{Arc}\cos x,\ 0\le x\le1\Rightarrow0\le\theta\le\tfrac\pi2'),
    T('Use $\\cos2\\theta=2\\cos^2\\theta-1$.', '$\\cos2\\theta=2\\cos^2\\theta-1$ استعمال کریں۔', '$\\cos2\\theta=2\\cos^2\\theta-1$ وکاروئ.', r'\cos2\theta=2x^2-1'),
    RANGE(r'0\le2\theta\le\pi\Rightarrow\text{Arc}\cos(2x^2-1)=2\theta=2\,\text{Arc}\cos x'), QED])
put('12.5', 4, '(iv)', 'Proved (see the steps).', [LET(r'\theta=\text{Arc}\tan x,\ x\ge0\Rightarrow0\le\theta<\tfrac\pi2'),
    VAL(r'\sec\theta=\sqrt{1+\tan^2\theta}=\sqrt{1+x^2}\Rightarrow\cos\theta=\frac1{\sqrt{1+x^2}}'), QED])
put('12.5', 5, '(i)', r'$\text{Sin}^{-1}x=\text{Tan}^{-1}\frac x{\sqrt{1-x^2}},\ -1<x<1$', [LET(r'\theta=\text{Sin}^{-1}x\in\left(-\tfrac\pi2,\tfrac\pi2\right)'), VAL(r'\tan\theta=\frac x{\sqrt{1-x^2}}\Rightarrow\theta=\text{Tan}^{-1}\frac x{\sqrt{1-x^2}}')])
put('12.5', 5, '(ii)', r'$\text{Arc}\cos x=\text{Tan}^{-1}\frac{\sqrt{1-x^2}}x,\ 0<x\le1$', [LET(r'\theta=\text{Arc}\cos x\in\left[0,\tfrac\pi2\right)\ \text{for }0<x\le1'), VAL(r'\sin\theta=\sqrt{1-x^2},\ \tan\theta=\frac{\sqrt{1-x^2}}x\Rightarrow\theta=\text{Tan}^{-1}\frac{\sqrt{1-x^2}}x')])
put('12.5', 5, '(iii)', r'$\text{Arc}\cot x=\text{Tan}^{-1}\frac1x,\ x>0$', [LET(r'\theta=\text{Arc}\cot x\in\left(0,\tfrac\pi2\right)\ \text{for }x>0'), VAL(r'\tan\theta=\frac1{\cot\theta}=\frac1x\Rightarrow\theta=\text{Tan}^{-1}\frac1x')])
TANSUM = lambda m: T('Use $\\text{Tan}^{-1}a\\pm\\text{Tan}^{-1}b=\\text{Tan}^{-1}\\dfrac{a\\pm b}{1\\mp ab}$ (valid here because the angles are small).', '$\\text{Tan}^{-1}a\\pm\\text{Tan}^{-1}b=\\text{Tan}^{-1}\\dfrac{a\\pm b}{1\\mp ab}$ استعمال کریں (یہاں زاویے چھوٹے ہونے سے درست)۔', '$\\text{Tan}^{-1}a\\pm\\text{Tan}^{-1}b=\\text{Tan}^{-1}\\dfrac{a\\pm b}{1\\mp ab}$ وکاروئ (دلته زاویې کوچنۍ دي نو سم دی).', m)
check(S.atan(S.Rational(1,2))*2 + S.atan(-S.Rational(1,7)) - S.pi/4)
put('12.5', 6, '(i)', 'Verified: both sides equal $\\frac\\pi4$.', [TANSUM(r'2\,\text{Tan}^{-1}\tfrac12=\text{Tan}^{-1}\frac{\frac12+\frac12}{1-\frac14}=\text{Tan}^{-1}\tfrac43'),
    TANSUM(r'\text{Tan}^{-1}\tfrac43+\text{Tan}^{-1}\left(-\tfrac17\right)=\text{Tan}^{-1}\frac{\frac43-\frac17}{1+\frac4{21}}=\text{Tan}^{-1}\frac{25/21}{25/21}=\text{Tan}^{-1}1=\tfrac\pi4'), QED])
check(S.asin(S.Rational(77,85)) - S.asin(S.Rational(3,5)) - S.acos(S.Rational(15,17)))
put('12.5', 6, '(ii)', 'Verified (see the steps).', [LET(r'A=\text{Sin}^{-1}\tfrac{77}{85},\ \cos A=\tfrac{36}{85};\quad B=\text{Sin}^{-1}\tfrac35,\ \cos B=\tfrac45'),
    EXP(r'\cos(A-B)=\cos A\cos B+\sin A\sin B=\tfrac{36}{85}\cdot\tfrac45+\tfrac{77}{85}\cdot\tfrac35=\tfrac{144+231}{425}=\tfrac{15}{17}'),
    RANGE(r'0<B<A<\tfrac\pi2\Rightarrow0<A-B<\tfrac\pi2\Rightarrow A-B=\text{Cos}^{-1}\tfrac{15}{17}'), QED])
check(S.pi/4 - S.atan(S.Rational(1,11)) - S.atan(S.Rational(5,6)))
put('12.5', 7, '', r'$\text{Tan}^{-1}\frac56$', [VAL(r'\tfrac\pi4=\text{Tan}^{-1}1'), TANSUM(r'\text{Tan}^{-1}1-\text{Tan}^{-1}\tfrac1{11}=\text{Tan}^{-1}\frac{1-\frac1{11}}{1+\frac1{11}}=\text{Tan}^{-1}\frac{10/11}{12/11}=\text{Tan}^{-1}\frac56')])
put('12.5', 8, '(i)', r'Proved for $-\frac12\le x\le\frac12$.', [LET(r'\theta=\text{Sin}^{-1}x,\ \sin\theta=x'), T('Use $\\sin3\\theta=3\\sin\\theta-4\\sin^3\\theta$.', '$\\sin3\\theta=3\\sin\\theta-4\\sin^3\\theta$ استعمال کریں۔', '$\\sin3\\theta=3\\sin\\theta-4\\sin^3\\theta$ وکاروئ.', r'\sin3\theta=3x-4x^3'),
    RANGE(r'|x|\le\tfrac12\Rightarrow|\theta|\le\tfrac\pi6\Rightarrow|3\theta|\le\tfrac\pi2\Rightarrow3\theta=\text{Sin}^{-1}(3x-4x^3)'), QED])
put('12.5', 8, '(ii)', r'Proved for $\frac12\le x\le1$.', [LET(r'\theta=\text{Cos}^{-1}x,\ \cos\theta=x'), T('Use $\\cos3\\theta=4\\cos^3\\theta-3\\cos\\theta$.', '$\\cos3\\theta=4\\cos^3\\theta-3\\cos\\theta$ استعمال کریں۔', '$\\cos3\\theta=4\\cos^3\\theta-3\\cos\\theta$ وکاروئ.', r'\cos3\theta=4x^3-3x'),
    RANGE(r'\tfrac12\le x\le1\Rightarrow0\le\theta\le\tfrac\pi3\Rightarrow0\le3\theta\le\pi\Rightarrow3\theta=\text{Cos}^{-1}(4x^3-3x)'), QED])
put('12.5', 8, '(iii)', 'Proved (see the steps).', [LET(r'\theta=\text{Sin}^{-1}x,\ \sin\theta=x,\ \cos\theta=\sqrt{1-x^2}'), T('Use $\\sin2\\theta=2\\sin\\theta\\cos\\theta$.', '$\\sin2\\theta=2\\sin\\theta\\cos\\theta$ استعمال کریں۔', '$\\sin2\\theta=2\\sin\\theta\\cos\\theta$ وکاروئ.', r'\sin(2\,\text{Sin}^{-1}x)=2x\sqrt{1-x^2}'), QED])
put('12.5', 8, '(iv)', 'Proved (see the steps).', [LET(r'\theta=\text{Tan}^{-1}\sqrt x,\ \tan\theta=\sqrt x,\ 0\le\theta<\tfrac\pi2'),
    T('Use $\\cos2\\theta=\\dfrac{1-\\tan^2\\theta}{1+\\tan^2\\theta}$.', '$\\cos2\\theta=\\dfrac{1-\\tan^2\\theta}{1+\\tan^2\\theta}$ استعمال کریں۔', '$\\cos2\\theta=\\dfrac{1-\\tan^2\\theta}{1+\\tan^2\\theta}$ وکاروئ.', r'\cos2\theta=\frac{1-x}{1+x}'),
    RANGE(r'0\le2\theta<\pi\Rightarrow2\theta=\text{Cos}^{-1}\frac{1-x}{1+x}\Rightarrow\theta=\tfrac12\text{Cos}^{-1}\frac{1-x}{1+x}'), QED])
put('12.5', 8, '(v)', 'Proved (see the steps).', [LET(r'\theta=\text{Sin}^{-1}x,\ x\ge0\Rightarrow0\le\theta\le\tfrac\pi2'), VAL(r'\cos\theta=\sqrt{1-x^2}'),
    RANGE(r'0\le\theta\le\tfrac\pi2\subset[0,\pi]\Rightarrow\theta=\text{Cos}^{-1}\sqrt{1-x^2}'), QED])
a = S.Symbol('a', positive=True)
check(((a + 1/(a+1)) / (1 - a/(a+1))) - (a**2 + a + 1))
put('12.5', 8, '(vi)', r'Proved (for $a>-1$).', [VAL(r'\text{Cot}^{-1}(a+1)=\text{Tan}^{-1}\frac1{a+1}'),
    TANSUM(r'\text{Tan}^{-1}a+\text{Tan}^{-1}\frac1{a+1}=\text{Tan}^{-1}\frac{a+\frac1{a+1}}{1-\frac a{a+1}}'),
    VAL(r'=\text{Tan}^{-1}\frac{\frac{a^2+a+1}{a+1}}{\frac1{a+1}}=\text{Tan}^{-1}(a^2+a+1)'), QED])
put('12.5', 9, '', r'$xy+yz+zx=1$ (proved).', [VAL(r'\text{Tan}^{-1}x+\text{Tan}^{-1}y=\tfrac\pi2-\text{Tan}^{-1}z'),
    T('Take $\\tan$ of both sides; $\\tan\\left(\\frac\\pi2-\\phi\\right)=\\cot\\phi$.', 'دونوں طرف کا $\\tan$ لیں؛ $\\tan\\left(\\frac\\pi2-\\phi\\right)=\\cot\\phi$۔', 'د دواړو خواوو $\\tan$ واخلئ؛ $\\tan\\left(\\frac\\pi2-\\phi\\right)=\\cot\\phi$.', r'\frac{x+y}{1-xy}=\cot(\text{Tan}^{-1}z)=\frac1z'),
    T('Cross-multiply and rearrange.', 'طرفین کی ضرب کر کے ترتیب دیں۔', 'متقابل ضرب وکړئ او ترتیب یې کړئ.', r'z(x+y)=1-xy\Rightarrow xy+yz+zx=1'), QED])

# ═══════════════════════════════ 12.6 ═══════════════════════════════
REF = lambda m: T('Find the reference angle and the quadrants where the function has this sign.', 'حوالہ زاویہ معلوم کریں اور وہ ربع جن میں تفاعل کی یہ علامت ہو۔', 'حوالې زاویه او هغه ربعې ومومئ چې پکې تابع دا نښه لري.', m)
x = S.Symbol('x')
def sols_ok(expr, vals):
    for v in vals: assert abs(float(expr.subs(x, v))) < 1e-9, (expr, v)
sols_ok(S.cos(x) - S.sqrt(3)/2, [S.pi/6, 11*S.pi/6])
put('12.6', 1, '(i)', r'$\left\{\frac\pi6+2k\pi\right\}\cup\left\{\frac{11\pi}6+2k\pi\right\},\ k\in Z$', [REF(r'\cos\tfrac\pi6=\tfrac{\sqrt3}2;\ \cos>0\text{ in quadrants I and IV}\Rightarrow x=\tfrac\pi6,\ \tfrac{11\pi}6'), GEN(r'x=\tfrac\pi6+2k\pi\ \text{or}\ x=\tfrac{11\pi}6+2k\pi')])
sols_ok(S.sin(x) - S.Rational(1,2), [S.pi/6, 5*S.pi/6])
put('12.6', 1, '(ii)', r'$\left\{\frac\pi6+2k\pi\right\}\cup\left\{\frac{5\pi}6+2k\pi\right\},\ k\in Z$', [REF(r'\sin\tfrac\pi6=\tfrac12;\ \sin>0\text{ in quadrants I and II}\Rightarrow x=\tfrac\pi6,\ \tfrac{5\pi}6'), GEN(r'x=\tfrac\pi6+2k\pi\ \text{or}\ x=\tfrac{5\pi}6+2k\pi'),
    KEY('the second family is printed as $\\frac{5\\pi}6+k\\pi$; it must be $\\frac{5\\pi}6+2k\\pi$ (for example $\\sin\\frac{11\\pi}6=-\\frac12$).', 'دوسرا خاندان $\\frac{5\\pi}6+k\\pi$ چھپا ہے؛ درست $\\frac{5\\pi}6+2k\\pi$ ہے (مثلاً $\\sin\\frac{11\\pi}6=-\\frac12$)۔', 'دویمه کورنۍ $\\frac{5\\pi}6+k\\pi$ چاپ شوې؛ سمه یې $\\frac{5\\pi}6+2k\\pi$ ده (د بېلګې په توګه $\\sin\\frac{11\\pi}6=-\\frac12$).')])
sols_ok(S.tan(x) + S.sqrt(3), [2*S.pi/3, 5*S.pi/3])
put('12.6', 1, '(iii)', r'$\left\{\frac{2\pi}3+k\pi\right\},\ k\in Z$', [REF(r'\tan\tfrac\pi3=\sqrt3;\ \tan<0\text{ in quadrant II}\Rightarrow x=\pi-\tfrac\pi3=\tfrac{2\pi}3'), GEN(r'\tan\text{ has period }\pi\Rightarrow x=\tfrac{2\pi}3+k\pi')])
put('12.6', 1, '(iv)', r'$\theta=\frac{3\pi}4+k\pi,\ k\in Z$', [VAL(r'\cos\phi=-1\iff\phi=\pi+2k\pi'), VAL(r'2\theta-\tfrac\pi2=\pi+2k\pi\Rightarrow2\theta=\tfrac{3\pi}2+2k\pi\Rightarrow\theta=\tfrac{3\pi}4+k\pi')])
th2 = S.Symbol('t')
for v in [4*S.pi/9, 8*S.pi/9]: assert abs(float(1/S.cos(3*v/2) + 2)) < 1e-9
put('12.6', 1, '(v)', r'$\theta=\frac{4\pi}9+\frac{4k\pi}3$ or $\theta=\frac{8\pi}9+\frac{4k\pi}3,\ k\in Z$', [VAL(r'\sec\tfrac{3\theta}2=-2\iff\cos\tfrac{3\theta}2=-\tfrac12'),
    REF(r'\cos\phi=-\tfrac12\iff\phi=\tfrac{2\pi}3+2k\pi\ \text{or}\ \tfrac{4\pi}3+2k\pi'), VAL(r'\tfrac{3\theta}2=\tfrac{2\pi}3+2k\pi\Rightarrow\theta=\tfrac{4\pi}9+\tfrac{4k\pi}3;\quad\tfrac{3\theta}2=\tfrac{4\pi}3+2k\pi\Rightarrow\theta=\tfrac{8\pi}9+\tfrac{4k\pi}3')])
sols_ok(4*S.cos(x)**2 - 1, [S.pi/3, 2*S.pi/3, 4*S.pi/3, 5*S.pi/3])
put('12.6', 1, '(vi)', r'$\left\{\frac\pi3+k\pi\right\}\cup\left\{\frac{2\pi}3+k\pi\right\},\ k\in Z$', [VAL(r'4\cos^2x=1\Rightarrow\cos x=\pm\tfrac12'),
    REF(r'\cos x=\tfrac12\Rightarrow x=\tfrac\pi3,\tfrac{5\pi}3;\quad\cos x=-\tfrac12\Rightarrow x=\tfrac{2\pi}3,\tfrac{4\pi}3'), GEN(r'x=\tfrac\pi3+k\pi\ \text{or}\ x=\tfrac{2\pi}3+k\pi\ \ (\text{same as the four families of period }2\pi)')])
ZP = lambda m: T('A product is zero when one of its factors is zero.', 'حاصلِ ضرب صفر ہو تو اس کا کوئی ایک جز صفر ہوتا ہے۔', 'که ضرب صفر وي، یو عامل یې صفر وي.', m)
put('12.6', 2, '(i)', r'$0^\circ,90^\circ,180^\circ,270^\circ,360^\circ$', [ZP(r'\sin x=0\ \text{or}\ \cos x=0'), VAL(r'\sin x=0\Rightarrow x=0^\circ,180^\circ,360^\circ;\quad\cos x=0\Rightarrow x=90^\circ,270^\circ'),
    KEY('$360^\\circ$ is also in the interval $0\\le x\\le360^\\circ$, although the key omits it.', 'وقفہ $0\\le x\\le360^\\circ$ میں $360^\\circ$ بھی شامل ہے، اگرچہ کنجی میں درج نہیں۔', 'په $0\\le x\\le360^\\circ$ واټن کې $360^\\circ$ هم شامل دی، که څه هم کیلي کې نشته.')])
put('12.6', 2, '(ii)', r'$\frac\pi2,\ \frac{3\pi}2$', [VAL(r'\sin x\cot x=\sin x\cdot\frac{\cos x}{\sin x}=\cos x\quad(\sin x\ne0)'), VAL(r'\cos x=0\Rightarrow x=\tfrac\pi2,\tfrac{3\pi}2'),
    T('$x=0,\\pi,2\\pi$ are rejected because $\\cot x$ is undefined there.', '$x=0,\\pi,2\\pi$ رد ہیں کیونکہ وہاں $\\cot x$ غیر معین ہے۔', '$x=0,\\pi,2\\pi$ ردېږي ځکه هلته $\\cot x$ نامعلوم دی.')])
put('12.6', 2, '(iii)', r'$\frac\pi6,\ \frac\pi3,\ \frac{5\pi}6,\ \frac{5\pi}3$', [ZP(r'\sec x=2\ \text{or}\ \sin x=\tfrac12'), VAL(r'\sec x=2\Rightarrow\cos x=\tfrac12\Rightarrow x=\tfrac\pi3,\tfrac{5\pi}3;\quad\sin x=\tfrac12\Rightarrow x=\tfrac\pi6,\tfrac{5\pi}6')])
put('12.6', 2, '(iv)', r'$\frac\pi6,\ \frac\pi3,\ \frac{5\pi}6,\ \frac{5\pi}3$', [ZP(r'\csc x=2\ \text{or}\ \cos x=\tfrac12'), VAL(r'\csc x=2\Rightarrow\sin x=\tfrac12\Rightarrow x=\tfrac\pi6,\tfrac{5\pi}6;\quad\cos x=\tfrac12\Rightarrow x=\tfrac\pi3,\tfrac{5\pi}3')])
put('12.6', 3, '(i)', r'$\left\{\frac\pi4+n\pi\right\},\ n\in Z$', [VAL(r'\cos\theta\ne0\text{ (else }\sin\theta=\pm1\ne0)\Rightarrow\tan\theta=1'), GEN(r'\theta=\tfrac\pi4+n\pi\ \ (\text{this already contains }\tfrac{5\pi}4+n\pi)')])
put('12.6', 3, '(ii)', r'$\{k\pi\}\cup\left\{\frac\pi3+2k\pi\right\}\cup\left\{\frac{5\pi}3+2k\pi\right\},\ k\in Z$', [VAL(r'\frac{\sin\theta}{\cos\theta}=2\sin\theta\Rightarrow\sin\theta\left(\frac1{\cos\theta}-2\right)=0'),
    ZP(r'\sin\theta=0\Rightarrow\theta=k\pi;\quad\cos\theta=\tfrac12\Rightarrow\theta=\tfrac\pi3+2k\pi,\ \tfrac{5\pi}3+2k\pi')])
put('12.6', 3, '(iii)', r'$\left\{\frac\pi2+k\pi\right\},\ k\in Z$', [VAL(r'\sin\theta=\frac1{\sin\theta}\Rightarrow\sin^2\theta=1\Rightarrow\sin\theta=\pm1'), GEN(r'\theta=\tfrac\pi2+k\pi\ \ (=\tfrac\pi2+2k\pi\text{ or }\tfrac{3\pi}2+2k\pi)')])
put('12.6', 3, '(iv)', r'$\left\{\frac\pi3+2k\pi\right\}\cup\left\{\frac{5\pi}3+2k\pi\right\},\ k\in Z$', [VAL(r'\cos^2\tfrac\theta2=\tfrac34\Rightarrow\cos\tfrac\theta2=\pm\tfrac{\sqrt3}2'),
    REF(r'\tfrac\theta2=\tfrac\pi6+k\pi\ \text{or}\ \tfrac{5\pi}6+k\pi'), VAL(r'\theta=\tfrac\pi3+2k\pi\ \text{or}\ \tfrac{5\pi}3+2k\pi\ \ (\text{the key lists the same set with period }4\pi)')])
sols_ok(S.sin(x)*S.cos(x) - S.sqrt(3)/4, [S.pi/6, S.pi/3])
put('12.6', 3, '(v)', r'$\left\{\frac\pi6+n\pi\right\}\cup\left\{\frac\pi3+n\pi\right\},\ n\in Z$', [VAL(r'\sin x\cos x=\tfrac12\sin2x\Rightarrow\sin2x=\tfrac{\sqrt3}2'), REF(r'2x=\tfrac\pi3+2n\pi\ \text{or}\ \tfrac{2\pi}3+2n\pi'), VAL(r'x=\tfrac\pi6+n\pi\ \text{or}\ \tfrac\pi3+n\pi')])
put('12.6', 3, '(vi)', r'$\{m\pi\}\cup\left\{\frac{2\pi}3+2m\pi\right\}\cup\left\{\frac{4\pi}3+2m\pi\right\},\ m\in Z$', [VAL(r'2\sin\theta\cos\theta+\sin\theta=0\Rightarrow\sin\theta(2\cos\theta+1)=0'),
    ZP(r'\sin\theta=0\Rightarrow\theta=m\pi;\quad\cos\theta=-\tfrac12\Rightarrow\theta=\tfrac{2\pi}3+2m\pi,\ \tfrac{4\pi}3+2m\pi')])
QF = lambda m: T('Treat it as a quadratic in one trigonometric ratio and factorise.', 'اسے ایک مثلثی نسبت میں دو درجی مساوات سمجھ کر تجزی کریں۔', 'دا په یوه مثلثاتي نسبت کې دوه درجه یي معادله وګڼئ او تجزیه یې کړئ.', m)
s_ = S.Symbol('s')
assert S.factor(2*s_**2 - 3*s_ + 1) == (s_ - 1)*(2*s_ - 1)
put('12.6', 4, '(i)', r'$\left\{\frac\pi6+2k\pi\right\}\cup\left\{\frac{5\pi}6+2k\pi\right\}\cup\left\{\frac\pi2+2k\pi\right\},\ k\in Z$', [QF(r'(2\sin x-1)(\sin x-1)=0'), VAL(r'\sin x=\tfrac12\Rightarrow x=\tfrac\pi6+2k\pi,\tfrac{5\pi}6+2k\pi;\quad\sin x=1\Rightarrow x=\tfrac\pi2+2k\pi')])
put('12.6', 4, '(ii)', 'No real solution.', [T('Bound the left side.', 'بائیں طرف کی حد معلوم کریں۔', 'د کیڼ اړخ حد ومومئ.', r'0\le\cos^2x\le1,\ -1\le\sin x\le1\Rightarrow-1\le\cos^2x\sin x\le1<2'),
    T('The left side can never be 2, so there is no solution.', 'بائیں طرف کبھی 2 نہیں ہو سکتی، اس لیے کوئی حل نہیں۔', 'کیڼ اړخ هېڅکله 2 کېدای نه شي، نو حل نشته.')])
assert S.factor(2*s_**2 + s_ - 1) == (s_ + 1)*(2*s_ - 1)
put('12.6', 4, '(iii)', r'$\left\{\frac\pi6+2n\pi\right\}\cup\left\{\frac{5\pi}6+2n\pi\right\}\cup\left\{\frac{3\pi}2+2n\pi\right\},\ n\in Z$', [VAL(r'\cos^2x-\sin^2x=1-2\sin^2x'), QF(r'1-2\sin^2x=\sin x\Rightarrow2\sin^2x+\sin x-1=0\Rightarrow(2\sin x-1)(\sin x+1)=0'),
    VAL(r'\sin x=\tfrac12\Rightarrow x=\tfrac\pi6+2n\pi,\tfrac{5\pi}6+2n\pi;\quad\sin x=-1\Rightarrow x=\tfrac{3\pi}2+2n\pi')])
sols_ok(S.cos(2*x) + S.cos(x) + 1, [S.pi/2, 3*S.pi/2, 2*S.pi/3, 4*S.pi/3])
put('12.6', 4, '(iv)', r'$\left\{\frac\pi2+n\pi\right\}\cup\left\{\frac{2\pi}3+2n\pi\right\}\cup\left\{\frac{4\pi}3+2n\pi\right\},\ n\in Z$', [VAL(r'\cos2x=2\cos^2x-1'), QF(r'2\cos^2x-1+\cos x+1=0\Rightarrow\cos x(2\cos x+1)=0'),
    VAL(r'\cos x=0\Rightarrow x=\tfrac\pi2+n\pi;\quad\cos x=-\tfrac12\Rightarrow x=\tfrac{2\pi}3+2n\pi,\tfrac{4\pi}3+2n\pi'),
    KEY('it gives $\\frac\\pi2+2n\\pi$ only; $x=\\frac{3\\pi}2$ also satisfies the equation ($\\cos3\\pi+\\cos\\frac{3\\pi}2+1=-1+0+1=0$), so the family is $\\frac\\pi2+n\\pi$.', 'اس میں صرف $\\frac\\pi2+2n\\pi$ ہے؛ $x=\\frac{3\\pi}2$ بھی مساوات پوری کرتا ہے، اس لیے خاندان $\\frac\\pi2+n\\pi$ ہے۔', 'په کې یوازې $\\frac\\pi2+2n\\pi$ دی؛ $x=\\frac{3\\pi}2$ هم معادله پوره کوي، نو کورنۍ $\\frac\\pi2+n\\pi$ ده.')])
assert S.factor(2*s_**2 - s_ - 1) == (s_ - 1)*(2*s_ + 1)
put('12.6', 4, '(v)', r'$\left\{\frac\pi2+2m\pi\right\}\cup\left\{\frac{7\pi}6+2m\pi\right\}\cup\left\{\frac{11\pi}6+2m\pi\right\},\ m\in Z$', [VAL(r'2\cos^2x=2-2\sin^2x'), QF(r'1-\sin x=2-2\sin^2x\Rightarrow2\sin^2x-\sin x-1=0\Rightarrow(\sin x-1)(2\sin x+1)=0'),
    VAL(r'\sin x=1\Rightarrow x=\tfrac\pi2+2m\pi;\quad\sin x=-\tfrac12\Rightarrow x=\tfrac{7\pi}6+2m\pi,\tfrac{11\pi}6+2m\pi')])
assert S.factor(2*s_**2 - 3*s_ - 2) == (s_ - 2)*(2*s_ + 1)
put('12.6', 4, '(vi)', r'$\left\{\frac\pi3+2k\pi\right\}\cup\left\{\frac{5\pi}3+2k\pi\right\},\ k\in Z$', [VAL(r'\tan^2x=\sec^2x-1'), QF(r'\sec^2x-1=\tfrac32\sec x\Rightarrow2\sec^2x-3\sec x-2=0\Rightarrow(\sec x-2)(2\sec x+1)=0'),
    T('$\\sec x=-\\frac12$ is impossible because $|\\sec x|\\ge1$.', '$\\sec x=-\\frac12$ ناممکن ہے کیونکہ $|\\sec x|\\ge1$۔', '$\\sec x=-\\frac12$ ناشونی دی ځکه $|\\sec x|\\ge1$.', r'\sec x=2\Rightarrow\cos x=\tfrac12\Rightarrow x=\tfrac\pi3+2k\pi,\ \tfrac{5\pi}3+2k\pi')])
put('12.6', 4, '(vii)', 'No real solution.', [VAL(r'\cos2x=1-2\sin^2x'), QF(r'3-\sin x=1-2\sin^2x\Rightarrow2\sin^2x-\sin x+2=0'),
    T('The discriminant is negative, so $\\sin x$ has no real value.', 'ممیز منفی ہے، اس لیے $\\sin x$ کی کوئی حقیقی قیمت نہیں۔', 'ممیز منفي دی، نو $\\sin x$ هېڅ حقیقي ارزښت نه لري.', r'\Delta=(-1)^2-4(2)(2)=-15<0')])
sols_ok(S.sin(x) + S.cos(x) - 1, [0, S.pi/2])
put('12.6', 4, '(viii)', r'$\{2k\pi\}\cup\left\{\frac\pi2+2k\pi\right\},\ k\in Z$', [VAL(r'\sin\theta+\cos\theta=\sqrt2\sin\left(\theta+\tfrac\pi4\right)'), VAL(r'\sqrt2\sin\left(\theta+\tfrac\pi4\right)=1\Rightarrow\sin\left(\theta+\tfrac\pi4\right)=\tfrac1{\sqrt2}'),
    REF(r'\theta+\tfrac\pi4=\tfrac\pi4+2k\pi\ \text{or}\ \tfrac{3\pi}4+2k\pi\Rightarrow\theta=2k\pi\ \text{or}\ \tfrac\pi2+2k\pi')])

# ═══════════════════════════════ Review 12 ═══════════════════════════════
MCQ = lambda m: T('Work out the value and compare it with the options.', 'قیمت نکال کر اختیارات سے موازنہ کریں۔', 'ارزښت ومومئ او له انتخابونو سره یې پرتله کړئ.', m)
put('Review 12', 1, '(i)', r'(b) $\frac{3\pi}{10}+\frac{2\pi}5k$', [VAL(r'\sin4x\cos x+\cos4x\sin x=\sin5x=-1'), MCQ(r'5x=\tfrac{3\pi}2+2k\pi\Rightarrow x=\tfrac{3\pi}{10}+\tfrac{2\pi}5k\ \Rightarrow\ \text{(b)}')], category='mcqs')
check(S.atan(S.sqrt(3)) - S.acos(-S.Rational(1,2)) + S.pi/3)
put('Review 12', 1, '(ii)', r'(b) $-\frac\pi3$', [VAL(r'\text{Tan}^{-1}\sqrt3=\tfrac\pi3;\quad\text{Sec}^{-1}(-2)=\text{Cos}^{-1}\left(-\tfrac12\right)=\tfrac{2\pi}3'), MCQ(r'\tfrac\pi3-\tfrac{2\pi}3=-\tfrac\pi3\ \Rightarrow\ \text{(b)}'),
    KEY('it gives (d) $\\frac{2\\pi}3$, but the expression as printed equals $-\\frac\\pi3$.', 'اس میں (d) $\\frac{2\\pi}3$ ہے، لیکن چھپی ہوئی عبارت کی قیمت $-\\frac\\pi3$ ہے۔', 'په کې (d) $\\frac{2\\pi}3$ دی، خو چاپ شوی عبارت $-\\frac\\pi3$ کېږي.')], category='mcqs')
put('Review 12', 1, '(iii)', r'(b) $-\frac\pi2\le y\le\frac\pi2$', [MCQ(r'\text{the principal range of Sin}^{-1}\text{ is }\left[-\tfrac\pi2,\tfrac\pi2\right]\ \Rightarrow\ \text{(b)}')], category='mcqs')
put('Review 12', 1, '(iv)', r'(d) $\frac x{\sqrt{1+x^2}}$', [LET(r'\theta=\text{Tan}^{-1}x\Rightarrow\tan\theta=x,\ \cos\theta=\tfrac1{\sqrt{1+x^2}}'), MCQ(r'\sin\theta=\tan\theta\cos\theta=\frac x{\sqrt{1+x^2}}\ \Rightarrow\ \text{(d)}')], category='mcqs')
xs, ys = S.symbols('x y', positive=True)
check(S.simplify((xs/ys - (xs-ys)/(xs+ys)) / (1 + xs/ys*(xs-ys)/(xs+ys))) - 1)
put('Review 12', 1, '(v)', r'(c) $\frac\pi4$', [TANSUM(r'\frac{\frac xy-\frac{x-y}{x+y}}{1+\frac xy\cdot\frac{x-y}{x+y}}=\frac{x(x+y)-y(x-y)}{y(x+y)+x(x-y)}=\frac{x^2+y^2}{x^2+y^2}=1'), MCQ(r'\text{Tan}^{-1}1=\tfrac\pi4\ \Rightarrow\ \text{(c)}')], category='mcqs')
put('Review 12', 2, '(i)', '$2$', [FORM(r'-2\csc\pi x:\ b=\pi'), PER_SC(r'\text{period}=\frac{2\pi}{\pi}=2')])
put('Review 12', 2, '(ii)', '$1$', [FORM(r'6\tan\pi x:\ b=\pi'), PER_TC(r'\text{period}=\frac{\pi}{\pi}=1')])
put('Review 12', 2, '(iii)', r'$\frac43$', [FORM(r'\tfrac95\cos\left(-\tfrac{3\pi}2x\right):\ b=-\tfrac{3\pi}2,\ |b|=\tfrac{3\pi}2'), PER_SC(r'\text{period}=\frac{2\pi}{3\pi/2}=\frac43'),
    KEY('it prints $-\\frac43$; a period is a positive number, so the period is $\\frac43$.', 'اس میں $-\\frac43$ چھپا ہے؛ دور مثبت عدد ہوتا ہے، لہٰذا دور $\\frac43$ ہے۔', 'په کې $-\\frac43$ چاپ شوی؛ دوره مثبت عدد وي، نو دوره $\\frac43$ ده.')])
put('Review 12', 3, '(i)', r'$\left\{\frac\pi2+k\pi\right\}\cup\left\{\frac\pi6+2k\pi\right\}\cup\left\{\frac{5\pi}6+2k\pi\right\},\ k\in Z$', [VAL(r'\sin2x=2\sin x\cos x'), ZP(r'2\sin x\cos x-\cos x=0\Rightarrow\cos x(2\sin x-1)=0'),
    VAL(r'\cos x=0\Rightarrow x=\tfrac\pi2+k\pi;\quad\sin x=\tfrac12\Rightarrow x=\tfrac\pi6+2k\pi,\tfrac{5\pi}6+2k\pi')])
put('Review 12', 3, '(ii)', r'$\left\{\frac\pi2+k\pi\right\}\cup\{2k\pi\},\ k\in Z$', [VAL(r'\sin^2x=1-\cos^2x'), ZP(r'1-\cos^2x+\cos x=1\Rightarrow\cos x(1-\cos x)=0'),
    VAL(r'\cos x=0\Rightarrow x=\tfrac\pi2+k\pi;\quad\cos x=1\Rightarrow x=2k\pi')])
sols_ok(1/S.sin(x) - S.sqrt(3) - S.cos(x)/S.sin(x), [2*S.pi/3])
put('Review 12', 3, '(iii)', r'$\left\{\frac{2\pi}3+2k\pi\right\},\ k\in Z$', [VAL(r'\csc x-\cot x=\frac{1-\cos x}{\sin x}=\frac{2\sin^2\frac x2}{2\sin\frac x2\cos\frac x2}=\tan\frac x2'),
    VAL(r'\tan\tfrac x2=\sqrt3\Rightarrow\tfrac x2=\tfrac\pi3+k\pi\Rightarrow x=\tfrac{2\pi}3+2k\pi'),
    T('These values keep $\\sin x\\ne0$, so all are valid.', 'ان قیمتوں پر $\\sin x\\ne0$ ہے، اس لیے سب درست ہیں۔', 'په دې ارزښتونو کې $\\sin x\\ne0$ دی، نو ټول سم دي.')])
check(2*S.atan(S.Rational(2,3)) - S.asin(S.Rational(12,13)))
put('Review 12', 4, '(i)', 'Proved (see the steps).', [TANSUM(r'2\,\text{Tan}^{-1}\tfrac23=\text{Tan}^{-1}\frac{\frac43}{1-\frac49}=\text{Tan}^{-1}\frac{12}5'),
    T('An acute angle with $\\tan=\\frac{12}5$ has hypotenuse $13$.', 'جس حادہ زاویے کا $\\tan=\\frac{12}5$ ہو اس کا وتر $13$ ہے۔', 'هغه حاده زاویه چې $\\tan=\\frac{12}5$ ولري، وتر یې $13$ دی.', r'\sqrt{12^2+5^2}=13\Rightarrow\sin=\tfrac{12}{13}\Rightarrow\text{Tan}^{-1}\tfrac{12}5=\text{Sin}^{-1}\tfrac{12}{13}'), QED])
check(S.atan(S.Rational(3,4)) + S.atan(S.Rational(3,5)) - S.atan(S.Rational(8,19)) - S.pi/4)
put('Review 12', 4, '(ii)', 'Proved (see the steps).', [TANSUM(r'\text{Tan}^{-1}\tfrac34+\text{Tan}^{-1}\tfrac35=\text{Tan}^{-1}\frac{\frac{27}{20}}{\frac{11}{20}}=\text{Tan}^{-1}\frac{27}{11}'),
    TANSUM(r'\text{Tan}^{-1}\tfrac{27}{11}-\text{Tan}^{-1}\tfrac8{19}=\text{Tan}^{-1}\frac{\frac{513-88}{209}}{\frac{209+216}{209}}=\text{Tan}^{-1}\frac{425}{425}=\text{Tan}^{-1}1=\tfrac\pi4'), QED])
check(S.asin(S.Rational(4,5)) + S.asin(S.Rational(5,13)) + S.asin(S.Rational(16,65)) - S.pi/2)
put('Review 12', 4, '(iii)', r'The identity holds as $\text{Sin}^{-1}\frac45+\text{Sin}^{-1}\frac5{13}+\text{Sin}^{-1}\frac{16}{65}=\frac\pi2$ (the printed "$-$" sign is a misprint).', [
    LET(r'A=\text{Sin}^{-1}\tfrac45\ (\cos A=\tfrac35),\quad B=\text{Sin}^{-1}\tfrac5{13}\ (\cos B=\tfrac{12}{13})'),
    EXP(r'\cos(A+B)=\cos A\cos B-\sin A\sin B=\tfrac{36}{65}-\tfrac{20}{65}=\tfrac{16}{65}'),
    VAL(r'0<A+B<\pi\Rightarrow A+B=\text{Cos}^{-1}\tfrac{16}{65}=\tfrac\pi2-\text{Sin}^{-1}\tfrac{16}{65}'),
    VAL(r'\therefore\ \text{Sin}^{-1}\tfrac45+\text{Sin}^{-1}\tfrac5{13}+\text{Sin}^{-1}\tfrac{16}{65}=\tfrac\pi2'),
    T('As printed, the last term has a minus sign; then the left side would be $\\frac\\pi2-2\\,\\text{Sin}^{-1}\\frac{16}{65}\\approx1.073\\ne\\frac\\pi2$, so the sign must be "+".',
      'جیسا چھپا ہے آخری رکن پر منفی کی علامت ہے؛ تب بائیں طرف $\\frac\\pi2-2\\,\\text{Sin}^{-1}\\frac{16}{65}\\approx1.073\\ne\\frac\\pi2$ ہوگی، اس لیے علامت "+" ہونی چاہیے۔',
      'لکه څنګه چې چاپ شوی، وروستي حد منفي نښه لري؛ بیا به کیڼ اړخ $\\frac\\pi2-2\\,\\text{Sin}^{-1}\\frac{16}{65}\\approx1.073\\ne\\frac\\pi2$ وي، نو نښه باید "+" وي.')])
check(S.atan(S.Rational(1,11)) + S.atan(S.Rational(5,6)) - S.atan(S.Rational(1,3)) - S.atan(S.Rational(1,2)))
put('Review 12', 4, '(iv)', r'Both sides equal $\frac\pi4$ when the right side is read as $\text{Tan}^{-1}\frac13+\text{Tan}^{-1}\frac12$.', [
    T('As printed, the right side is a product of two inverse tangents, which is a misprint; the intended identity has a "+" sign.', 'جیسا چھپا ہے دائیں طرف دو معکوس ٹینجنٹ کا حاصلِ ضرب ہے جو طباعت کی غلطی ہے؛ مطلوبہ شناخت میں "+" کی علامت ہے۔', 'لکه څنګه چې چاپ شوی، ښي اړخ د دوو معکوس ټانجنټونو ضرب دی چې د چاپ تېروتنه ده؛ اصلي اتحاد کې "+" نښه ده.'),
    TANSUM(r'\text{Tan}^{-1}\tfrac1{11}+\text{Tan}^{-1}\tfrac56=\text{Tan}^{-1}\frac{\frac{6+55}{66}}{\frac{66-5}{66}}=\text{Tan}^{-1}1=\tfrac\pi4'),
    TANSUM(r'\text{Tan}^{-1}\tfrac13+\text{Tan}^{-1}\tfrac12=\text{Tan}^{-1}\frac{\frac56}{\frac56}=\tfrac\pi4'), QED])
put('Review 12', 5, '(i)', r'$\text{Cos}^{-1}A-\text{Cos}^{-1}B=\text{Cos}^{-1}\left(AB+\sqrt{1-A^2}\sqrt{1-B^2}\right)$ (for $A\le B$)', [
    T('As printed, $\\sqrt{A^2+B^2}$ is a misprint for $\\sqrt{1-A^2}\\sqrt{1-B^2}$; we prove the correct form.', 'جیسا چھپا ہے $\\sqrt{A^2+B^2}$ غلط ہے، درست $\\sqrt{1-A^2}\\sqrt{1-B^2}$ ہے؛ ہم درست صورت ثابت کرتے ہیں۔', 'چاپ شوی $\\sqrt{A^2+B^2}$ تېروتنه ده، سم یې $\\sqrt{1-A^2}\\sqrt{1-B^2}$ دی؛ موږ سمه بڼه ثابتوو.'),
    LET(r'\alpha=\text{Cos}^{-1}A,\ \beta=\text{Cos}^{-1}B\in[0,\pi]:\ \sin\alpha=\sqrt{1-A^2},\ \sin\beta=\sqrt{1-B^2}'),
    EXP(r'\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta=AB+\sqrt{1-A^2}\sqrt{1-B^2}'),
    RANGE(r'A\le B\Rightarrow\alpha\ge\beta\Rightarrow0\le\alpha-\beta\le\pi\Rightarrow\alpha-\beta=\text{Cos}^{-1}\left(AB+\sqrt{1-A^2}\sqrt{1-B^2}\right)'), QED])
put('Review 12', 5, '(ii)', r'$\text{Tan}^{-1}A-\text{Tan}^{-1}B=\text{Tan}^{-1}\dfrac{A-B}{1+AB}$ (for $AB>-1$)', [
    T('As printed, the denominator $1+AB$ is missing; we prove the correct form.', 'جیسا چھپا ہے مخرج $1+AB$ رہ گیا ہے؛ ہم درست صورت ثابت کرتے ہیں۔', 'لکه څنګه چې چاپ شوی، مخرج $1+AB$ پاتې دی؛ موږ سمه بڼه ثابتوو.'),
    LET(r'\alpha=\text{Tan}^{-1}A,\ \beta=\text{Tan}^{-1}B:\ \tan\alpha=A,\ \tan\beta=B'),
    EXP(r'\tan(\alpha-\beta)=\frac{\tan\alpha-\tan\beta}{1+\tan\alpha\tan\beta}=\frac{A-B}{1+AB}'),
    RANGE(r'AB>-1\Rightarrow-\tfrac\pi2<\alpha-\beta<\tfrac\pi2\Rightarrow\alpha-\beta=\text{Tan}^{-1}\frac{A-B}{1+AB}'), QED])

flush()
A.save(['12.1', '12.2', '12.3', '12.4', '12.5', '12.6', 'Review 12'], list(range(343, 401)) + [425, 426, 427, 428, 429])
