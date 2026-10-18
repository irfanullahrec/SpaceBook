import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from gm import *
pages={}
def T(en,ur=None,ps=None):return f'{en} || {ur or en} || {ps or en}'
def P(en,ur,ps):return f'p {T(en,ur,ps)}\n'
def S(w,h,aria,body):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{aria}"><title>{aria}</title>{body}</svg>'
tx=lambda x,y,t,sz=12,fill='#0f172a':f'<text x="{x}" y="{y}" font-size="{sz}" fill="{fill}" font-family="sans-serif">{t}</text>'
PI=math.pi
def wave(fn,x0,x1,aria,ymax=1.3,w=560,h=230,tick=None,labels=None,asym=(),dots=(),col='#2563eb',lw=2.4,yl=(1,-1),pad=40,dashed=()):
    X=lambda v:pad+(v-x0)/(x1-x0)*(w-pad-20)
    Y=lambda v:h/2-v/ymax*(h/2-24)
    o=f'<path d="M{pad-10} {Y(0):.1f}H{w-10}M{X(0) if x0<=0<=x1 else pad:.1f} {h-8}V8" stroke="#334155" stroke-width="1.5" fill="none"/><path d="M{w-10} {Y(0):.1f}l-8-4v8Z" fill="#334155"/>'
    o+=tx(X(0)+6 if x0<=0<=x1 else pad+6,Y(yl[0])+4,str(yl[0]),11)+tx(X(0)+6 if x0<=0<=x1 else pad+6,Y(yl[1])+4,str(yl[1]),11)
    if labels:
        for v,t in labels:o+=f'<path d="M{X(v):.1f} {Y(0)-4:.1f}v8" stroke="#334155"/>'+tx(X(v)-10,Y(0)+(18 if True else 0),t,11)
    segs=[(x0,x1)] if not asym else []
    if asym:
        pts=sorted([x0]+list(asym)+[x1]);segs=[(a+1e-3,b-1e-3) for a,b in zip(pts[:-1],pts[1:])]
        for a in asym:o+=f'<path d="M{X(a):.1f} 6V{h-6}" stroke="#94a3b8" stroke-dasharray="4 4"/>'
    for a,b in segs:
        pts=[]
        n=200
        for i in range(n+1):
            v=a+(b-a)*i/n
            try:y=fn(v)
            except ZeroDivisionError:continue
            if abs(y)<=ymax*1.6:pts.append(f'{"M" if not pts else "L"}{X(v):.1f} {Y(max(-ymax*1.05,min(ymax*1.05,y))):.1f}')
        if pts:o+=f'<path d="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="{lw}"/>'
    for v in dots:o+=f'<circle cx="{X(v):.1f}" cy="{Y(fn(v)):.1f}" r="3.2" fill="#dc2626"/>'
    return S(w,h,aria,o)
deg=lambda d:d*PI/180
f1214=wave(lambda v:math.sin(v),0,2*PI,'Figure 12.14: the graph of y = sin x on [0, 2 pi]',ymax=1.25,dots=[deg(d) for d in range(0,361,30)],labels=[(deg(d),f'{d}°') for d in range(30,361,30)])
f1215=wave(lambda v:math.sin(v),-2*PI,4*PI,'Figure 12.15: the extended graph of y = sin x',ymax=1.25,labels=[(-2*PI,'-2π'),(-PI,'-π'),(PI,'π'),(2*PI,'2π'),(3*PI,'3π'),(4*PI,'4π')])
f1216=wave(lambda v:math.cos(v),0,2*PI,'Figure 12.16: the graph of y = cos x on [0, 2 pi]',ymax=1.25,dots=[deg(d) for d in range(0,361,30)],labels=[(deg(d),f'{d}°') for d in range(30,361,30)])
f1217=wave(lambda v:math.cos(v),-2*PI,4*PI,'Figure 12.17: the extended graph of y = cos x',ymax=1.25,labels=[(-2*PI,'-2π'),(-PI,'-π'),(PI,'π'),(2*PI,'2π'),(3*PI,'3π'),(4*PI,'4π')])
f1218=wave(lambda v:math.tan(v),0,PI,'Figure 12.18: the graph of y = tan x on [0, pi] with the asymptote at 90 degrees',ymax=2.6,asym=(PI/2,),dots=[deg(d) for d in (30,60,120,150)],labels=[(deg(d),f'{d}°') for d in (30,60,90,120,150,180)],yl=(2,-2),w=480,h=300,pad=60)
f1219=wave(lambda v:math.tan(v),-PI,2.4*PI,'Figure 12.19: the extended graph of y = tan x with asymptotes at odd multiples of pi/2',ymax=2.6,asym=tuple(PI/2+k*PI for k in range(-2,3)),labels=[(-PI,'-π'),(PI,'π'),(2*PI,'2π')],yl=(2,-2),w=560,h=300,pad=50)
f1220=wave(lambda v:1/math.tan(v),0,PI,'Figure 12.20: the graph of y = cot x on [0, pi] with the asymptotes at 0 and 180 degrees',ymax=2.6,asym=(0,PI),dots=[deg(d) for d in (30,60,90,120,150)],labels=[(deg(d),f'{d}°') for d in (30,60,90,120,150)],yl=(2,-2),w=480,h=300,pad=60)
f1221=wave(lambda v:1/math.tan(v),-PI,2.4*PI,'Figure 12.21: the extended graph of y = cot x with asymptotes at multiples of pi',ymax=2.6,asym=tuple(k*PI for k in range(-1,3)),labels=[(-PI,'-π'),(PI,'π'),(2*PI,'2π')],col='#be185d',yl=(2,-2),w=560,h=300,pad=50)
def tb(cap,xs,ys):
    return f'table {cap}\nth | $x$ | '+' | '.join(xs)+'\ntr | $y$ | '+' | '.join(ys)+'\nendtable\n'
pages[355]=r'''@printed 355
@deco Unit-running header, folio and decorative footer band excluded
p Take a set of rectangular axes, choosing a convenient length for $30^\circ$ on the $x$-axis and a convenient length as a unit on the $y$-axis. We plot the points $(x,y)$ to get the following graph of $y=\sin x$ in the interval $(0,2\pi)$ || مستطیلی محوروں کا ایک سیٹ لیں، $x$-محور پر $30^\circ$ کے لیے موزوں لمبائی اور $y$-محور پر اکائی کے طور پر موزوں لمبائی منتخب کریں۔ ہم نقاط $(x,y)$ پلاٹ کر کے وقفے $(0,2\pi)$ میں $y=\sin x$ کا درج ذیل گراف حاصل کرتے ہیں || د مستطیلي محورونو یو سېټ واخلئ، په $x$-محور د $30^\circ$ لپاره مناسب اوږدوالی او په $y$-محور د واحد په توګه مناسب اوږدوالی وټاکئ. موږ ټکي $(x,y)$ رسموو چې په وقفه $(0,2\pi)$ کې د $y=\sin x$ لاندې ګراف ترلاسه کړو
'''+svgblock('Figure 12.14: $y=\\sin x$ on $[0,2\\pi]$.','شکل 12.14: $[0,2\\pi]$ پر $y=\\sin x$۔','شکل 12.14: په $[0,2\\pi]$ باندې $y=\\sin x$.',f1214)+r'''p We note for all values of $x$, $-1\le\sin x\le1$. We often call the graph of $y=\sin x$, a sine wave and the graph in the interval $[0,2\pi]$ a cycle. Extended graph of $\sin x$ which is the repetition of the graph in figure 12.14 is given in figure 12.15. || ہم نوٹ کرتے ہیں کہ $x$ کی تمام قیمتوں کے لیے $-1\le\sin x\le1$۔ ہم اکثر $y=\sin x$ کے گراف کو سائن لہر اور وقفے $[0,2\pi]$ میں گراف کو ایک چکر کہتے ہیں۔ $\sin x$ کا توسیع شدہ گراف جو شکل 12.14 کے گراف کی تکرار ہے شکل 12.15 میں دیا گیا ہے۔ || موږ یادونه کوو چې د $x$ د ټولو ارزښتونو لپاره $-1\le\sin x\le1$. موږ اکثراً د $y=\sin x$ ګراف ته د ساین څپه او په وقفه $[0,2\pi]$ کې ګراف ته یوه دوره وایو. د $\sin x$ غځول شوی ګراف چې د شکل 12.14 د ګراف تکرار دی په شکل 12.15 کې ورکړل شوی.
'''+svgblock('Figure 12.15: the extended graph of $y=\\sin x$ over $[-2\\pi,4\\pi]$.','شکل 12.15: $[-2\\pi,4\\pi]$ پر $y=\\sin x$ کا توسیع شدہ گراف۔','شکل 12.15: په $[-2\\pi,4\\pi]$ باندې د $y=\\sin x$ غځول شوی ګراف.',f1215)+r'''p **(b) Graph of $y=\cos x,\ -2\pi\le x\le2\pi$.** The cosine function also has a period of $2\pi$, and its range is $[-1,1]$. Values of $(x,y)$, satisfying $y=\cos x$ are given below in the form of a table. || **(b) $y=\cos x,\ -2\pi\le x\le2\pi$ کا گراف۔** کوسائن تفاعل کا دور بھی $2\pi$ ہے اور اس کی سعت $[-1,1]$ ہے۔ $y=\cos x$ کو پورا کرنے والی $(x,y)$ کی قیمتیں نیچے جدول کی صورت میں دی گئی ہیں۔ || **(b) د $y=\cos x,\ -2\pi\le x\le2\pi$ ګراف.** د کوساین تابع دوره هم $2\pi$ ده او رینج یې $[-1,1]$ دی. د $y=\cos x$ پوره کوونکي $(x,y)$ ارزښتونه لاندې په جدول بڼه ورکړل شوي.
'''
pages[356]=r'''@printed 356
@sec 12.2.2(c) | Graph of y = tan x, 0 ≤ x ≤ π || y = tan x کا گراف || د y = tan x ګراف
@deco Unit-running header, folio and decorative footer band excluded
'''+tb('Values of $y=\\cos x$ || $y=\\cos x$ کی قیمتیں || د $y=\\cos x$ ارزښتونه',[f'{d}°' for d in (0,30,60,90,120,150,180,210,240,270,300,330,360)],['1','0.87','0.5','0','-0.5','-0.87','-1','-0.87','-0.5','0','0.5','0.87','1'])+r'''p Plotting the points $(x,y)$; the graph of $y=\cos x$ on the interval $[0,2\pi]$, is shown in figure 12.16. Extended graph of $y=\cos x$ is shown in figure 12.17. || نقاط $(x,y)$ پلاٹ کرنے سے وقفے $[0,2\pi]$ پر $y=\cos x$ کا گراف شکل 12.16 میں دکھایا گیا ہے۔ $y=\cos x$ کا توسیع شدہ گراف شکل 12.17 میں دکھایا گیا ہے۔ || ټکي $(x,y)$ رسمولو سره په وقفه $[0,2\pi]$ باندې د $y=\cos x$ ګراف په شکل 12.16 کې ښودل شوی. د $y=\cos x$ غځول شوی ګراف په شکل 12.17 کې ښودل شوی.
'''+svgblock('Figure 12.16: $y=\\cos x$ on $[0,2\\pi]$.','شکل 12.16: $[0,2\\pi]$ پر $y=\\cos x$۔','شکل 12.16: په $[0,2\\pi]$ باندې $y=\\cos x$.',f1216)+svgblock('Figure 12.17: the extended graph of $y=\\cos x$ over $[-2\\pi,4\\pi]$.','شکل 12.17: $[-2\\pi,4\\pi]$ پر $y=\\cos x$ کا توسیع شدہ گراف۔','شکل 12.17: په $[-2\\pi,4\\pi]$ باندې د $y=\\cos x$ غځول شوی ګراف.',f1217)+r'''p **(c) Graph of $y=\tan x,\ 0\le x\le\pi$.** The period of $\tan x$ is $\pi$ and the domain is the set $R-\{x\mid x=(2n+1)\dfrac\pi2,\ n\in Z\}$. When $x=(2n+1)\dfrac\pi2$, $n\in Z$ or $x=\pm90^\circ,\pm270^\circ,\ldots$; the tangent function is not defined, at these values of $x$, it becomes very large, in other words it approaches $\pm\infty$. || **(c) $y=\tan x,\ 0\le x\le\pi$ کا گراف۔** $\tan x$ کا دور $\pi$ ہے اور دائرہ سیٹ $R-\{x\mid x=(2n+1)\dfrac\pi2,\ n\in Z\}$ ہے۔ جب $x=(2n+1)\dfrac\pi2$، $n\in Z$ یا $x=\pm90^\circ,\pm270^\circ,\ldots$ ہو تو ٹینجنٹ تفاعل متعین نہیں ہوتا، $x$ کی ان قیمتوں پر یہ بہت بڑا ہو جاتا ہے، دوسرے الفاظ میں یہ $\pm\infty$ کی طرف جاتا ہے۔ || **(c) د $y=\tan x,\ 0\le x\le\pi$ ګراف.** د $\tan x$ دوره $\pi$ ده او ډومین سېټ $R-\{x\mid x=(2n+1)\dfrac\pi2,\ n\in Z\}$ دی. کله چې $x=(2n+1)\dfrac\pi2$، $n\in Z$ یا $x=\pm90^\circ,\pm270^\circ,\ldots$ وي نو ټینجنټ تابع تعریف شوې نه ده، د $x$ په دغو ارزښتونو کې دا ډېره لویه کېږي، په بل عبارت دا $\pm\infty$ ته نږدې کېږي.
'''
pages[357]=r'''@printed 357
@sec 12.2.2(d) | Graph of y = cot x, -π ≤ x ≤ π || y = cot x کا گراف || د y = cot x ګراف
@deco Unit-running header, folio and decorative footer band excluded
p In the interval $[0,\pi]$ as we approach $90^\circ$ from the left, the tangent becomes larger positively, that is, it tends to $+\infty$; and when we approach $90^\circ$ from the right, it becomes larger negatively, that is it tends to $-\infty$. Table of values $(x,y)$ satisfying $y=\tan x$ on $[0,\pi]$ are given in the below table. The graph is shown in figure 12.18. || وقفے $[0,\pi]$ میں جب ہم $90^\circ$ کی طرف بائیں سے آتے ہیں تو ٹینجنٹ مثبت طور پر بڑا ہوتا جاتا ہے، یعنی $+\infty$ کی طرف جاتا ہے؛ اور جب ہم $90^\circ$ کی طرف دائیں سے آتے ہیں تو یہ منفی طور پر بڑا ہوتا جاتا ہے، یعنی $-\infty$ کی طرف جاتا ہے۔ $[0,\pi]$ پر $y=\tan x$ کو پورا کرنے والی $(x,y)$ کی قیمتوں کا جدول نیچے دیا گیا ہے۔ گراف شکل 12.18 میں دکھایا گیا ہے۔ || په وقفه $[0,\pi]$ کې کله چې موږ له کیڼ لوري نه $90^\circ$ ته نږدې کېږو ټینجنټ په مثبت ډول لوی کېږي، یعنې $+\infty$ ته مخه کوي؛ او کله چې موږ له ښي لوري نه $90^\circ$ ته نږدې کېږو دا په منفي ډول لوی کېږي، یعنې $-\infty$ ته مخه کوي. په $[0,\pi]$ باندې د $y=\tan x$ پوره کوونکي $(x,y)$ ارزښتونو جدول لاندې ورکړل شوی. ګراف په شکل 12.18 کې ښودل شوی.
'''+tb('Values of $y=\\tan x$ on $[0,\\pi]$ || $[0,\\pi]$ پر $y=\\tan x$ کی قیمتیں || په $[0,\\pi]$ باندې د $y=\\tan x$ ارزښتونه',[f'{d}°' for d in (0,30,60,90,120,150,180)],['0','0.58','1.73','$-\\infty/\\infty$','-1.73','-0.58','0'])+svgblock('Figure 12.18: $y=\\tan x$ on $[0,\\pi]$ with the asymptote at $90^\\circ$.','شکل 12.18: $[0,\\pi]$ پر $y=\\tan x$ جس کا قاربی خط $90^\\circ$ پر ہے۔','شکل 12.18: په $[0,\\pi]$ باندې $y=\\tan x$ چې اسیمپټوټ یې په $90^\\circ$ کې دی.',f1218)+r'''p Extended graph of $y=\tan x$ is given in figure 12.19. || $y=\tan x$ کا توسیع شدہ گراف شکل 12.19 میں دیا گیا ہے۔ || د $y=\tan x$ غځول شوی ګراف په شکل 12.19 کې ورکړل شوی.
'''+svgblock('Figure 12.19: the extended graph of $y=\\tan x$.','شکل 12.19: $y=\\tan x$ کا توسیع شدہ گراف۔','شکل 12.19: د $y=\\tan x$ غځول شوی ګراف.',f1219)+r'''p **(d) Graph of $y=\cot x,\ -\pi\le x\le\pi$.** The period of cotangent is also $\pi$. || **(d) $y=\cot x,\ -\pi\le x\le\pi$ کا گراف۔** کوٹینجنٹ کا دور بھی $\pi$ ہے۔ || **(d) د $y=\cot x,\ -\pi\le x\le\pi$ ګراف.** د کوټینجنټ دوره هم $\pi$ ده.
'''
pages[358]=r'''@printed 358
@deco Unit-running header, folio and decorative footer band excluded
p Table of values $(x,y)$ satisfying $y=\cot x$ on $[0,\pi]$ is given below, while graph is shown in figure 12.20. || $[0,\pi]$ پر $y=\cot x$ کو پورا کرنے والی $(x,y)$ کی قیمتوں کا جدول نیچے دیا گیا ہے، جبکہ گراف شکل 12.20 میں دکھایا گیا ہے۔ || په $[0,\pi]$ باندې د $y=\cot x$ پوره کوونکي $(x,y)$ ارزښتونو جدول لاندې ورکړل شوی، پداسې حال کې چې ګراف په شکل 12.20 کې ښودل شوی.
'''+tb('Values of $y=\\cot x$ on $[0,\\pi]$ || $[0,\\pi]$ پر $y=\\cot x$ کی قیمتیں || په $[0,\\pi]$ باندې د $y=\\cot x$ ارزښتونه',[f'{d}°' for d in (0,30,60,90,120,150,180)],['$\\infty$','1.73','0.58','0','-0.58','-1.73','$-\\infty$'])+svgblock('Figure 12.20: $y=\\cot x$ on $[0,\\pi]$.','شکل 12.20: $[0,\\pi]$ پر $y=\\cot x$۔','شکل 12.20: په $[0,\\pi]$ باندې $y=\\cot x$.',f1220)+r'''p Extended graph of $y=\cot x$ is given below in figure 12.21, which is the repetition of the graph given in figure 12.20. || $y=\cot x$ کا توسیع شدہ گراف نیچے شکل 12.21 میں دیا گیا ہے جو شکل 12.20 میں دیے گئے گراف کی تکرار ہے۔ || د $y=\cot x$ غځول شوی ګراف لاندې په شکل 12.21 کې ورکړل شوی چې د شکل 12.20 کې ورکړل شوي ګراف تکرار دی.
'''+svgblock('Figure 12.21: the extended graph of $y=\\cot x$.','شکل 12.21: $y=\\cot x$ کا توسیع شدہ گراف۔','شکل 12.21: د $y=\\cot x$ غځول شوی ګراف.',f1221)
for n,t in pages.items():
    open(f'{OUT}\\p{n}.txt','w',encoding='utf8').write(t)
print('ok')
