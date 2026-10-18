"""Step-by-step SpaceBook solutions for Class 11 Mathematics, Unit 11 (application of trigonometry).
All numbers are computed here; results are compared with the printed key (p.425) and any
disagreement is stated in the steps."""
import sys, os
from math import sin, cos, tan, asin, acos, atan, sqrt, radians, degrees, pi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math11_answer_authoring import Author, step, S
from math11_phrases import make_put

A = Author(11)
put, flush = make_put(A)
def T(en, ur, ps, m=None):
    return step(en, ur, ps, m)
def KEY(en, ur, ps):
    return T('Note on the printed answer key: ' + en, 'مطبوعہ جوابی کنجی کے بارے میں: ' + ur, 'د چاپ شوې ځوابي کیلي په اړه: ' + ps)
d = radians
def DM(deg, mins=0): return deg + mins / 60
def ang(x, mins=False):
    """degrees as 62.3° or 62°18′"""
    if mins:
        tot = round(x * 60)
        return f"{tot // 60}^\\circ{tot % 60}'"
    return f'{x:.1f}^\\circ'.replace('.0^', '^') if abs(x - round(x)) < 0.05 else f'{x:.1f}^\\circ'
def num(x, k=2):
    s = f'{x:.{k}f}'.rstrip('0').rstrip('.')
    return s
QED = T('Hence proved.', 'ثابت ہوا۔', 'ثابت شو.')
SUM = lambda m: T('The angles of a triangle add up to $180^\\circ$.', 'مثلث کے زاویوں کا مجموعہ $180^\\circ$ ہوتا ہے۔', 'د درې ګوني د زاویو مجموعه $180^\\circ$ ده.', m)
SINE = lambda m: T('Law of sines: $\\dfrac a{\\sin\\alpha}=\\dfrac b{\\sin\\beta}=\\dfrac c{\\sin\\gamma}$.', 'قانونِ جیب: $\\dfrac a{\\sin\\alpha}=\\dfrac b{\\sin\\beta}=\\dfrac c{\\sin\\gamma}$۔', 'د ساین قانون: $\\dfrac a{\\sin\\alpha}=\\dfrac b{\\sin\\beta}=\\dfrac c{\\sin\\gamma}$.', m)
COS = lambda m: T('Law of cosines: $c^2=a^2+b^2-2ab\\cos\\gamma$ (and similarly for the other sides).', 'قانونِ جیب التمام: $c^2=a^2+b^2-2ab\\cos\\gamma$ (اور اسی طرح دوسرے اضلاع کے لیے)۔', 'د کوساین قانون: $c^2=a^2+b^2-2ab\\cos\\gamma$ (او همداسې د نورو ضلعو لپاره).', m)
COSA = lambda m: T('Find an angle from three sides: $\\cos\\alpha=\\dfrac{b^2+c^2-a^2}{2bc}$.', 'تین اضلاع سے زاویہ: $\\cos\\alpha=\\dfrac{b^2+c^2-a^2}{2bc}$۔', 'له درې ضلعو زاویه: $\\cos\\alpha=\\dfrac{b^2+c^2-a^2}{2bc}$.', m)
RT = lambda m: T('In a right triangle use $\\sin=\\dfrac{\\text{opp}}{\\text{hyp}}$, $\\cos=\\dfrac{\\text{adj}}{\\text{hyp}}$, $\\tan=\\dfrac{\\text{opp}}{\\text{adj}}$.', 'قائمہ مثلث میں $\\sin=\\dfrac{\\text{مقابل}}{\\text{وتر}}$، $\\cos=\\dfrac{\\text{متصل}}{\\text{وتر}}$، $\\tan=\\dfrac{\\text{مقابل}}{\\text{متصل}}$ استعمال کریں۔', 'په قایم درې ګوني کې $\\sin=\\dfrac{\\text{مقابل}}{\\text{وتر}}$، $\\cos=\\dfrac{\\text{نږدې}}{\\text{وتر}}$، $\\tan=\\dfrac{\\text{مقابل}}{\\text{نږدې}}$ وکاروئ.', m)
FIG = lambda m: T('Draw a figure and mark the right triangle formed.', 'شکل بنائیں اور بننے والی قائمہ مثلث پر نشان لگائیں۔', 'شکل رسم کړئ او جوړ شوی قایم درې ګونی په نښه کړئ.', m)
ANSL = lambda m: T('Answer.', 'جواب۔', 'ځواب.', m)

# ═══════════════════════ 11.1 ═══════════════════════
put('11.1', 1, '', r'(i) $a=3,\ b=3\sqrt3\approx5.20,\ \beta=60^\circ$; (ii) $a\approx52.7,\ c\approx136.6,\ \alpha=22.7^\circ$; (iii) $a=b=5\sqrt2\approx7.07,\ \alpha=45^\circ$', [
    T('Part (i): hypotenuse $AB=6$, $\\alpha=30^\\circ$, $\\gamma=90^\\circ$.', 'حصہ (i): وتر $AB=6$، $\\alpha=30^\\circ$، $\\gamma=90^\\circ$۔', '(i) برخه: وتر $AB=6$، $\\alpha=30^\\circ$، $\\gamma=90^\\circ$.', r'\beta=90^\circ-30^\circ=60^\circ'),
    RT(r'a=6\sin30^\circ=3,\qquad b=6\cos30^\circ=3\sqrt3\approx5.20'),
    T('Part (ii): from the figure $b=AC=126$, $\\beta=67.3^\\circ$, $\\gamma=90^\\circ$.', 'حصہ (ii): شکل سے $b=AC=126$، $\\beta=67.3^\\circ$، $\\gamma=90^\\circ$۔', '(ii) برخه: له شکل نه $b=AC=126$، $\\beta=67.3^\\circ$، $\\gamma=90^\\circ$.', r'\alpha=90^\circ-67.3^\circ=22.7^\circ'),
    RT(r'a=\frac{b}{\tan\beta}=\frac{126}{\tan67.3^\circ}\approx52.7,\qquad c=\frac{b}{\sin\beta}=\frac{126}{\sin67.3^\circ}\approx136.6'),
    T('Part (iii): hypotenuse $AB=10$, $\\beta=45^\\circ$, $\\gamma=90^\\circ$.', 'حصہ (iii): وتر $AB=10$، $\\beta=45^\\circ$، $\\gamma=90^\\circ$۔', '(iii) برخه: وتر $AB=10$، $\\beta=45^\\circ$، $\\gamma=90^\\circ$.', r'\alpha=45^\circ,\ a=10\cos45^\circ=5\sqrt2,\ b=10\sin45^\circ=5\sqrt2')])
v = (14*tan(d(28)), 14/cos(d(28)), 8.9/tan(d(21.5)), 8.9/sin(d(21.5)), sqrt(450**2-14**2), degrees(asin(14/450)))
put('11.1', 2, '', rf'(i) $\alpha=62^\circ,\ b\approx{num(v[0])},\ c\approx{num(v[1])}$; (ii) $\alpha=68.5^\circ,\ a\approx{num(v[2])},\ c\approx{num(v[3])}$; (iii) $a\approx{num(v[4])},\ \beta\approx{num(v[5])}^\circ,\ \alpha\approx{num(90-v[5])}^\circ$', [
    SUM(r'\text{(i) }\alpha=90^\circ-28^\circ=62^\circ'), RT(rf'b=a\tan\beta=14\tan28^\circ\approx{num(v[0])},\quad c=\frac a{{\cos\beta}}=\frac{{14}}{{\cos28^\circ}}\approx{num(v[1])}'),
    SUM(r'\text{(ii) }\alpha=90^\circ-21.5^\circ=68.5^\circ'), RT(rf'a=\frac b{{\tan\beta}}=\frac{{8.9}}{{\tan21.5^\circ}}\approx{num(v[2])},\quad c=\frac b{{\sin\beta}}\approx{num(v[3])}'),
    T('Part (iii): $c$ is the hypotenuse; use Pythagoras for $a$.', 'حصہ (iii): $c$ وتر ہے؛ $a$ کے لیے فیثاغورث استعمال کریں۔', '(iii) برخه: $c$ وتر دی؛ د $a$ لپاره فیثاغورث وکاروئ.', rf'a=\sqrt{{450^2-14^2}}\approx{num(v[4])},\quad\sin\beta=\frac{{14}}{{450}}\Rightarrow\beta\approx{num(v[5])}^\circ,\ \alpha\approx{num(90-v[5])}^\circ'),
    T('(The value $c=450$ is used as printed; it may be a misprint for $45.0$.)', '(قیمت $c=450$ جیسی چھپی ہے استعمال کی گئی؛ ممکن ہے یہ $45.0$ کی غلطی ہو۔)', '(د $c=450$ ارزښت لکه چاپ شوی وکارول شو؛ کېدای شي دا د $45.0$ تېروتنه وي.)')])
h = 38*tan(d(33.23))
put('11.1', 3, '', rf'about ${num(h)}$ m', [FIG(r'\text{post }h,\ \text{distance }38\text{ m},\ \text{angle of elevation }33.23^\circ'), RT(rf'\tan33.23^\circ=\frac h{{38}}\Rightarrow h=38\tan33.23^\circ\approx{num(h)}\text{{ m}}')])
e = degrees(atan(82/62))
put('11.1', 4, '', rf'about ${num(e,1)}^\circ$', [FIG(r'\text{minar }82\text{ m (opposite)},\ \text{shadow }62\text{ m (adjacent)}'), RT(rf'\tan\theta=\frac{{82}}{{62}}\approx1.3226\Rightarrow\theta\approx{num(e,1)}^\circ')])
h = 65.7*tan(d(28.9))
put('11.1', 5, '', rf'about ${num(h,1)}$ m', [T('The angle of depression from the top equals the angle of elevation of the top from the boat (alternate angles).', 'چوٹی سے زاویہ انخفاض کشتی سے چوٹی کے زاویہ ارتفاع کے برابر ہے (متبادل زاویے)۔', 'له سر نه د ټیټوالي زاویه له کښتۍ نه د سر د لوړوالي له زاویې سره مساوي ده (متبادلې زاویې).'),
    RT(rf'\tan28.9^\circ=\frac h{{65.7}}\Rightarrow h=65.7\tan28.9^\circ\approx{num(h,1)}\text{{ m}}')])
x1, x2 = 52/tan(d(36)), 52/tan(d(24))
put('11.1', 6, '', rf'about ${num(x2-x1,1)}$ m', [FIG(r'\text{cliff }52\text{ m; ships at distances }x_1,\ x_2\text{ from its foot}'),
    RT(rf'x_1=\frac{{52}}{{\tan36^\circ}}\approx{num(x1)},\qquad x_2=\frac{{52}}{{\tan24^\circ}}\approx{num(x2)}'), ANSL(rf'x_2-x_1\approx{num(x2-x1,1)}\text{{ m}}\ \ (\text{{key: }}45.3\text{{ m, rounding}})')])
dd = 8/tan(d(35))
put('11.1', 7, '', rf'about ${num(dd)}$ m', [FIG(r'\text{difference in heights}=20-12=8\text{ m}'), RT(rf'\tan35^\circ=\frac8x\Rightarrow x=\frac8{{\tan35^\circ}}\approx{num(dd)}\text{{ m}}')])
h = 330*sin(d(35))
put('11.1', 8, '', rf'about ${num(h,1)}$ m', [T('Because of the 10 m sag, take the straight length of the string as $340-10=330$ m (as in the printed key).', '10 میٹر جھول کی وجہ سے ڈور کی سیدھی لمبائی $340-10=330$ میٹر لیں (جیسا مطبوعہ کنجی میں ہے)۔', 'د 10 متره ځوړند له امله د تار سمه اوږدوالی $340-10=330$ متره واخلئ (لکه په چاپ شوې کیلي کې).'),
    RT(rf'\sin35^\circ=\frac h{{330}}\Rightarrow h=330\sin35^\circ\approx{num(h,1)}\text{{ m}}')])
h1, h2 = 100*tan(d(50)), 100*tan(d(30))
put('11.1', 9, '', rf'about ${num(h1-h2,1)}$ m', [FIG(r'\text{observer }100\text{ m from the landing point}'), RT(rf'h_1=100\tan50^\circ\approx{num(h1)},\qquad h_2=100\tan30^\circ\approx{num(h2)}'),
    ANSL(rf'h_1-h_2\approx{num(h1-h2,1)}\text{{ m}}'), KEY('it states the answer in feet, but the data are in metres.', 'اس میں جواب فٹ میں ہے، حالانکہ دیا گیا ڈیٹا میٹر میں ہے۔', 'په کې ځواب په فټ کې دی، که څه هم معلومات په متر کې دي.')])
alt = 10/tan(d(54))
put('11.1', 10, '', rf'about ${num(alt,3)}$ cm', [T('The altitude bisects the base and the vertical angle.', 'ارتفاع قاعدے اور راسی زاویے کو نصف کرتا ہے۔', 'لوړوالی قاعده او عمودي زاویه نیمایي کوي.', r'\text{half base}=10\text{ cm},\ \text{half angle}=54^\circ'),
    RT(rf'\tan54^\circ=\frac{{10}}h\Rightarrow h=\frac{{10}}{{\tan54^\circ}}\approx{num(alt,3)}\text{{ cm}}')])

# ═══════════════════════ triangle solvers (with steps) ═══════════════════════
def sss(a, b, c, mins=False):
    al = degrees(acos((b*b+c*c-a*a)/(2*b*c))); be = degrees(acos((a*a+c*c-b*b)/(2*a*c))); ga = 180-al-be
    ss = [COSA(rf'\cos\alpha=\frac{{{b}^2+{c}^2-{a}^2}}{{2({b})({c})}}\approx{(b*b+c*c-a*a)/(2*b*c):.4f}\Rightarrow\alpha\approx{ang(al,mins)}'),
          COSA(rf'\cos\beta=\frac{{{a}^2+{c}^2-{b}^2}}{{2({a})({c})}}\approx{(a*a+c*c-b*b)/(2*a*c):.4f}\Rightarrow\beta\approx{ang(be,mins)}'),
          SUM(rf'\gamma=180^\circ-\alpha-\beta\approx{ang(ga,mins)}')]
    return (al, be, ga), ss
def sas(x, y, C, names, mins=False):
    """two sides x,y with included angle C (degrees); names=('a','b','\\gamma','c','\\alpha','\\beta')"""
    z = sqrt(x*x+y*y-2*x*y*cos(d(C)))
    X = degrees(acos((y*y+z*z-x*x)/(2*y*z))); Y = 180-C-X
    n1, n2, nC, nz, nX, nY = names
    ss = [COS(rf'{nz}^2={x}^2+{y}^2-2({x})({y})\cos{ang(C,mins)}\approx{z*z:.2f}\Rightarrow {nz}\approx{num(z)}'),
          COSA(rf'\cos{nX}=\frac{{{y}^2+{nz}^2-{x}^2}}{{2({y}){nz}}}\approx{(y*y+z*z-x*x)/(2*y*z):.4f}\Rightarrow {nX}\approx{ang(X,mins)}'),
          SUM(rf'{nY}=180^\circ-{ang(C,mins)}-{nX}\approx{ang(Y,mins)}')]
    return (z, X, Y), ss
def aas(side, opp, B, C, names, mins=False):
    """known side opposite angle `opp`; other angles B, C; returns the two other sides"""
    k = side/sin(d(opp))
    nk, nopp, nB, nC, sB, sC = names
    ss = [SINE(rf'\frac{{{nk}}}{{\sin{nopp}}}=\frac{{{side}}}{{\sin{ang(opp,mins)}}}\approx{k:.4f}'),
          SINE(rf'{sB}=\frac{{{side}\sin{ang(B,mins)}}}{{\sin{ang(opp,mins)}}}\approx{num(k*sin(d(B)))},\qquad {sC}=\frac{{{side}\sin{ang(C,mins)}}}{{\sin{ang(opp,mins)}}}\approx{num(k*sin(d(C)))}')]
    return (k*sin(d(B)), k*sin(d(C))), ss

# ═══════════════════════ 11.2 ═══════════════════════
(al, be, ga), ss = sss(209, 120, 241)
put('11.2', 1, '(i)', rf'$\alpha\approx{ang(al)},\ \beta\approx{ang(be)},\ \gamma\approx{ang(ga)}$', ss + [T('Indeed $209^2+120^2=241^2$, so $\\gamma=90^\\circ$ exactly.', 'واقعی $209^2+120^2=241^2$، لہٰذا $\\gamma=90^\\circ$ بالکل۔', 'رښتیا $209^2+120^2=241^2$، نو $\\gamma=90^\\circ$ دقیق.')])
(c_, al, be), ss = sas(120, 240, 32, ('a', 'b', r'\gamma', 'c', r'\alpha', r'\beta'))
put('11.2', 1, '(ii)', rf'$c\approx{num(c_,1)},\ \alpha\approx{ang(al)},\ \beta\approx{ang(be)}$', ss)
be = 180-100-56.4
(a_, b_), ss = aas(345, 56.4, 100, be, ('c', r'\gamma', r'\alpha', r'\beta', 'a', 'b'))
put('11.2', 1, '(iii)', rf'$\beta={ang(be)},\ a\approx{num(a_,0)},\ b\approx{num(b_,0)}$', [SUM(rf'\beta=180^\circ-100^\circ-56.4^\circ={ang(be)}')] + ss)
(b_, al, ga), ss = sas(24.5, 43.8, 112, ('a', 'c', r'\beta', 'b', r'\alpha', r'\gamma'))
put('11.2', 1, '(iv)', rf'$b\approx{num(b_,1)},\ \alpha\approx{ang(al)},\ \gamma\approx{ang(ga)}$', ss)
(a_, be, ga), ss = sas(1.6, 3.2, DM(100, 24), ('b', 'c', r'\alpha', 'a', r'\beta', r'\gamma'), mins=True)
put('11.2', 1, '(v)', rf'$a\approx{num(a_)},\ \beta\approx{ang(be,True)},\ \gamma\approx{ang(ga,True)}$', ss)
al = 180-DM(39, 30)-DM(34, 10)
(b_, c_), ss = aas(240, al, DM(39, 30), DM(34, 10), ('a', r'\alpha', r'\beta', r'\gamma', 'b', 'c'), mins=True)
put('11.2', 1, '(vi)', rf"$\alpha={ang(al,True)},\ b\approx{num(b_,0)},\ c\approx{num(c_,0)}$", [SUM(rf'\alpha=180^\circ-39^\circ30′-34^\circ10′={ang(al,True)}')] + ss)
ga = 180-35-70
(a_, b_), ss = aas(115, ga, 35, 70, ('c', r'\gamma', r'\alpha', r'\beta', 'a', 'b'))
put('11.2', 1, '(vii)', rf'$\gamma={ang(ga)},\ a\approx{num(a_,0)},\ b\approx{num(b_,0)}$', [SUM(rf'\gamma=180^\circ-35^\circ-70^\circ={ang(ga)}')] + ss)
sa = 37.5*sin(d(72))/12.4
put('11.2', 1, '(viii)', 'No triangle is possible.', [SINE(rf'\sin\alpha=\frac{{a\sin\beta}}b=\frac{{37.5\sin72^\circ}}{{12.4}}\approx{sa:.3f}'),
    T('A sine can never exceed 1, so no angle $\\alpha$ exists.', 'جیب کی قیمت کبھی 1 سے زیادہ نہیں ہو سکتی، اس لیے کوئی زاویہ $\\alpha$ موجود نہیں۔', 'ساین هېڅکله له 1 نه زیات نه شي کېدای، نو هېڅ زاویه $\\alpha$ نشته.', rf'{sa:.3f}>1')])
(a_, be, ga), ss = sas(12.5, 23, DM(38, 20), ('b', 'c', r'\alpha', 'a', r'\beta', r'\gamma'), mins=True)
put('11.2', 1, '(ix)', rf'$a\approx{num(a_)},\ \beta\approx{ang(be,True)},\ \gamma\approx{ang(ga,True)}$', ss)
(b_, al, ga), ss = sas(168, 319, DM(110, 22), ('a', 'c', r'\beta', 'b', r'\alpha', r'\gamma'), mins=True)
put('11.2', 1, '(x)', rf'$b\approx{num(b_,1)},\ \alpha\approx{ang(al,True)},\ \gamma\approx{ang(ga,True)}$', ss)

HALF = lambda m: T('Half-angle formula: $\\sin\\dfrac\\alpha2=\\sqrt{\\dfrac{(s-b)(s-c)}{bc}}$ with $s=\\dfrac{a+b+c}2$; the largest angle is opposite the longest side.', 'نصف زاویہ کا کلیہ: $\\sin\\dfrac\\alpha2=\\sqrt{\\dfrac{(s-b)(s-c)}{bc}}$ جہاں $s=\\dfrac{a+b+c}2$؛ سب سے بڑا زاویہ سب سے لمبے ضلع کے مقابل ہوتا ہے۔', 'د نیمې زاویې فورمول: $\\sin\\dfrac\\alpha2=\\sqrt{\\dfrac{(s-b)(s-c)}{bc}}$ چې $s=\\dfrac{a+b+c}2$؛ تر ټولو لویه زاویه د تر ټولو اوږدې ضلعې مخې ته وي.', m)
def largest(sides, names):
    a, b, c = sides
    s = (a+b+c)/2
    # side 0 is the longest
    v = sqrt((s-b)*(s-c)/(b*c)); A_ = 2*degrees(asin(v))
    return s, v, A_
for p, sides, nm in [('(i)', (74, 52, 47), r'\alpha'), ('(ii)', (9, 7, 7), r'\beta'), ('(iii)', (2.7, 2.3, 1.5), r'\gamma')]:
    s, v, A_ = largest(sides, nm)
    a, b, c = sides
    put('11.2', 2, p, rf'${nm}\approx{ang(A_,True)}$', [HALF(rf's=\frac{{{a}+{b}+{c}}}2={num(s)};\ \text{{longest side }}{a}\Rightarrow\text{{largest angle }}{nm}'),
        T('Substitute.', 'قیمتیں رکھیں۔', 'ارزښتونه کېږدئ.', rf'\sin\frac{{{nm}}}2=\sqrt{{\frac{{({num(s)}-{b})({num(s)}-{c})}}{{({b})({c})}}}}\approx{v:.5f}\Rightarrow\frac{{{nm}}}2\approx{ang(A_/2,True)}\Rightarrow {nm}\approx{ang(A_,True)}')])
COSH = lambda m: T('Half-angle cosine formula: $\\cos\\dfrac\\alpha2=\\sqrt{\\dfrac{s(s-a)}{bc}}$ (similarly for $\\beta,\\gamma$).', 'نصف زاویہ کوسائن کا کلیہ: $\\cos\\dfrac\\alpha2=\\sqrt{\\dfrac{s(s-a)}{bc}}$ (اسی طرح $\\beta,\\gamma$ کے لیے)۔', 'د نیمې زاویې کوساین فورمول: $\\cos\\dfrac\\alpha2=\\sqrt{\\dfrac{s(s-a)}{bc}}$ (همداسې د $\\beta,\\gamma$ لپاره).', m)
for p, (a, b, c) in [('(i)', (9, 7, 5)), ('(ii)', (1.2, 9, 10)), ('(iii)', (6, 8, 12))]:
    s = (a+b+c)/2
    al = 2*degrees(acos(sqrt(s*(s-a)/(b*c)))); be = 2*degrees(acos(sqrt(s*(s-b)/(a*c)))); ga = 180-al-be
    put('11.2', 3, p, rf'$\alpha\approx{ang(al)},\ \beta\approx{ang(be)},\ \gamma\approx{ang(ga)}$', [COSH(rf's=\frac{{{a}+{b}+{c}}}2={num(s)}'),
        T('Find $\\alpha$ and $\\beta$.', '$\\alpha$ اور $\\beta$ معلوم کریں۔', '$\\alpha$ او $\\beta$ ومومئ.', rf'\cos\frac\alpha2=\sqrt{{\frac{{{num(s)}({num(s)}-{a})}}{{({b})({c})}}}}\Rightarrow\alpha\approx{ang(al)};\quad\cos\frac\beta2=\sqrt{{\frac{{{num(s)}({num(s)}-{b})}}{{({a})({c})}}}}\Rightarrow\beta\approx{ang(be)}'),
        SUM(rf'\gamma\approx180^\circ-{ang(al)}-{ang(be)}\approx{ang(ga)}')])
x = 20*sin(d(20))/sin(d(120)); y = 20*sin(d(40))/sin(d(120))
put('11.2', 4, '', rf'about ${num(x,1)}$ cm and ${num(y,1)}$ cm', [T('The diagonal and two adjacent sides form a triangle; the angle opposite the diagonal is $180^\\circ-20^\\circ-40^\\circ=120^\\circ$.', 'وتر نما قطر اور دو متصل اضلاع ایک مثلث بناتے ہیں؛ قطر کے مقابل زاویہ $180^\\circ-20^\\circ-40^\\circ=120^\\circ$ ہے۔', 'قطر او دوه نږدې ضلعې یو درې ګونی جوړوي؛ د قطر مخې ته زاویه $180^\\circ-20^\\circ-40^\\circ=120^\\circ$ ده.'),
    SINE(rf'x=\frac{{20\sin20^\circ}}{{\sin120^\circ}}\approx{num(x,1)},\qquad y=\frac{{20\sin40^\circ}}{{\sin120^\circ}}\approx{num(y,1)}')])
dist = sqrt(2*1050**2-2*1050**2*cos(d(127)))
put('11.2', 5, '', rf'about ${num(dist,0)}$ km', [T('In 2 hours each plane flies $525\\times2=1050$ km.', '2 گھنٹوں میں ہر جہاز $525\\times2=1050$ کلومیٹر اڑتا ہے۔', 'په 2 ساعتونو کې هره الوتکه $525\\times2=1050$ کیلومتره الوځي.'),
    COS(rf'd^2=1050^2+1050^2-2(1050)(1050)\cos127^\circ\Rightarrow d\approx{num(dist,0)}\text{{ km}}')])
(al, be, ga), ss = sss(285, 375, 396, mins=True)
put('11.2', 6, '', rf"$\approx{ang(al,True)},\ {ang(be,True)},\ {ang(ga,True)}$", ss)
x = 30*sin(d(30))/sin(d(110)); y = 30*sin(d(40))/sin(d(110))
put('11.2', 7, '', rf'about ${num(2*(x+y),1)}$ cm', [T('The diagonal splits the parallelogram into two triangles; the angle opposite the diagonal is $180^\\circ-30^\\circ-40^\\circ=110^\\circ$.', 'قطر متوازی الاضلاع کو دو مثلثوں میں تقسیم کرتا ہے؛ قطر کے مقابل زاویہ $180^\\circ-30^\\circ-40^\\circ=110^\\circ$ ہے۔', 'قطر متوازي الاضلاع په دوو درې ګونو وېشي؛ د قطر مخې ته زاویه $180^\\circ-30^\\circ-40^\\circ=110^\\circ$ ده.'),
    SINE(rf'x=\frac{{30\sin30^\circ}}{{\sin110^\circ}}\approx{num(x)},\qquad y=\frac{{30\sin40^\circ}}{{\sin110^\circ}}\approx{num(y)}'), ANSL(rf'\text{{perimeter}}=2(x+y)\approx{num(2*(x+y),1)}\text{{ cm}}')])
put('11.2', 8, '(i)', 'Proved (see the steps).', [COSA(r'1+\cos\alpha=1+\frac{b^2+c^2-a^2}{2bc}=\frac{2bc+b^2+c^2-a^2}{2bc}'), T('Use $(b+c)^2-a^2=(b+c+a)(b+c-a)$.', '$(b+c)^2-a^2=(b+c+a)(b+c-a)$ استعمال کریں۔', '$(b+c)^2-a^2=(b+c+a)(b+c-a)$ وکاروئ.', r'=\frac{(b+c)^2-a^2}{2bc}=\frac{(b+c+a)(b+c-a)}{2bc}'), QED])
put('11.2', 8, '(ii)', 'Proved (see the steps).', [COSA(r'1-\cos\alpha=1-\frac{b^2+c^2-a^2}{2bc}=\frac{a^2-(b^2-2bc+c^2)}{2bc}'), T('Use $a^2-(b-c)^2=(a-b+c)(a+b-c)$.', '$a^2-(b-c)^2=(a-b+c)(a+b-c)$ استعمال کریں۔', '$a^2-(b-c)^2=(a-b+c)(a+b-c)$ وکاروئ.', r'=\frac{a^2-(b-c)^2}{2bc}=\frac{(a-b+c)(a+b-c)}{2bc}'), QED])

# ═══════════════════════ 11.3 ═══════════════════════
AR2 = lambda m: T('Two sides and the included angle: $\\Delta=\\tfrac12ab\\sin\\gamma$.', 'دو اضلاع اور درمیانی زاویہ: $\\Delta=\\tfrac12ab\\sin\\gamma$۔', 'دوه ضلعې او منځنۍ زاویه: $\\Delta=\\tfrac12ab\\sin\\gamma$.', m)
AR1 = lambda m: T('One side and two angles: $\\Delta=\\dfrac{a^2\\sin\\beta\\sin\\gamma}{2\\sin\\alpha}$ (find the third angle first).', 'ایک ضلع اور دو زاویے: $\\Delta=\\dfrac{a^2\\sin\\beta\\sin\\gamma}{2\\sin\\alpha}$ (پہلے تیسرا زاویہ معلوم کریں)۔', 'یوه ضلع او دوه زاویې: $\\Delta=\\dfrac{a^2\\sin\\beta\\sin\\gamma}{2\\sin\\alpha}$ (لومړی درېیمه زاویه ومومئ).', m)
HER = lambda m: T("Three sides: Heron's formula $\\Delta=\\sqrt{s(s-a)(s-b)(s-c)}$, $s=\\dfrac{a+b+c}2$.", 'تین اضلاع: ہیرون کا کلیہ $\\Delta=\\sqrt{s(s-a)(s-b)(s-c)}$، $s=\\dfrac{a+b+c}2$۔', 'درې ضلعې: د هیرون فورمول $\\Delta=\\sqrt{s(s-a)(s-b)(s-c)}$، $s=\\dfrac{a+b+c}2$.', m)
def sas_area(x, y, C, lab, mins=False):
    v = 0.5*x*y*sin(d(C)); return v, [AR2(rf'\Delta=\tfrac12({x})({y})\sin{ang(C,mins)}\approx{num(v)}')]
def asa_area(s, B, C, mins=False):
    Aang = 180-B-C; v = s*s*sin(d(B))*sin(d(C))/(2*sin(d(Aang)))
    return v, [SUM(rf'\text{{third angle}}=180^\circ-{ang(B,mins)}-{ang(C,mins)}={ang(Aang,mins)}'), AR1(rf'\Delta=\frac{{{s}^2\sin{ang(B,mins)}\sin{ang(C,mins)}}}{{2\sin{ang(Aang,mins)}}}\approx{num(v)}')]
def heron(a, b, c):
    s = (a+b+c)/2; v = sqrt(s*(s-a)*(s-b)*(s-c))
    return v, [HER(rf's={num(s)},\quad\Delta=\sqrt{{{num(s)}({num(s-a)})({num(s-b)})({num(s-c)})}}\approx{num(v)}')]
areas = [('(i)', sas_area(15, 80, 38, 'g')), ('(ii)', sas_area(14, 12, 82, 'a')), ('(iii)', asa_area(30, 50, 100)), ('(iv)', asa_area(40, 50, 60)),
         ('(v)', heron(7.0, 8.0, 2.0)), ('(vi)', heron(11, 9.0, 8.0)), ('(vii)', sas_area(414, 485, DM(49, 47), 'a', True)), ('(viii)', asa_area(32, DM(47, 24), DM(70, 16), True)),
         ('(ix)', asa_area(47, DM(60, 25), DM(41, 35), True)), ('(x)', asa_area(57, DM(23, 24), DM(71, 36), True)), ('(xi)', sas_area(925, 433, DM(42, 17), 'b', True)), ('(xii)', sas_area(92, 71, DM(56, 44), 'g', True))]
key113 = [369.42, 83, 680, 564.7, 6.4, 35.5, 76662, 400.5, 651.7, 614.5, 134736.6, 2730.7]
for (p, (v, ss)), k in zip(areas, key113):
    extra = []
    if abs(v - k) / k > 0.02:
        extra = [KEY(f'it prints ${k}$; the data as printed give ${num(v)}$.', f'اس میں ${k}$ چھپا ہے؛ چھپے ہوئے ڈیٹا سے ${num(v)}$ آتا ہے۔', f'په کې ${k}$ چاپ شوی؛ له چاپ شوو معلوماتو ${num(v)}$ راځي.')]
    put('11.3', 1, p, rf'$\Delta\approx{num(v)}$ square units', ss + extra)
put('11.3', 2, '', r'$\gamma=180^\circ-\alpha-\beta$ and $c=\sqrt{\dfrac{2\Delta\sin\gamma}{\sin\alpha\sin\beta}}$; with $\beta$ read as $65^\circ35′$: $\gamma\approx82^\circ$, $c\approx22.2$', [
    T('As printed $\\beta=65^\\circ65′$ is impossible (minutes are less than 60); we read it as $65^\\circ35′$, which matches the printed answer.', 'جیسا چھپا ہے $\\beta=65^\\circ65′$ ناممکن ہے (منٹ 60 سے کم ہوتے ہیں)؛ ہم اسے $65^\\circ35′$ پڑھتے ہیں جو مطبوعہ جواب سے مطابقت رکھتا ہے۔', 'لکه څنګه چې چاپ شوی $\\beta=65^\\circ65′$ ناشونی دی (دقیقې له 60 کمې وي)؛ موږ یې $65^\\circ35′$ لولو چې له چاپ شوي ځواب سره سمون لري.'),
    SUM(rf'\gamma=180^\circ-32^\circ25′-65^\circ35′={ang(180-DM(32,25)-DM(65,35),True)}'),
    AR1(r'\Delta=\frac{c^2\sin\alpha\sin\beta}{2\sin\gamma}\Rightarrow c^2=\frac{2\Delta\sin\gamma}{\sin\alpha\sin\beta}'),
    T('Substitute $\\Delta=121.34$.', '$\\Delta=121.34$ رکھیں۔', '$\\Delta=121.34$ کېږدئ.', rf'c^2=\frac{{2(121.34)\sin{ang(180-DM(32,25)-DM(65,35),True)}}}{{\sin32^\circ25′\sin65^\circ35′}}\approx{2*121.34*sin(d(180-DM(32,25)-DM(65,35)))/(sin(d(DM(32,25)))*sin(d(DM(65,35)))):.2f}\Rightarrow c\approx{num(sqrt(2*121.34*sin(d(180-DM(32,25)-DM(65,35)))/(sin(d(DM(32,25)))*sin(d(DM(65,35))))))}')])
v, ss = asa_area(30, 22.5, 112.5)
put('11.3', 3, '', rf'Area $\approx{num(v)}$ m$^2$; cost $\approx$ Rs. ${num(5*v,0)}$', ss + [ANSL(rf'\text{{cost}}=5\times{num(v)}\approx\text{{Rs. }}{num(5*v,0)}'),
    KEY('it gives Rs. 1125, i.e. an area of 225 m$^2$; this is the area when the 30 m side lies between the two given angles ($\\Delta=\\frac{30^2\\sin22.5^\\circ\\sin112.5^\\circ}{2\\sin45^\\circ}$), which is what the computation above uses.', 'اس میں Rs. 1125 یعنی 225 مربع میٹر رقبہ ہے؛ یہ اس صورت کا رقبہ ہے جب 30 میٹر کا ضلع دونوں زاویوں کے درمیان ہو، جو اوپر کے حساب میں لیا گیا ہے۔', 'په کې Rs. 1125 یعنې 225 مربع متره مساحت دی؛ دا د هغې حالت مساحت دی چې 30 متره ضلع د دواړو زاویو ترمنځ وي، چې پورته حساب کې اخیستل شوې.')])
v = 0.5*53*42*sin(d(135))
put('11.3', 4, '', rf'about ${num(v,0)}$ ft$^2$', [AR2(rf'\Delta=\tfrac12(53)(42)\sin135^\circ=1113\times\frac{{\sqrt2}}2\approx{num(v,1)}\ \text{{ft}}^2'), ANSL(rf'\approx{num(v,0)}\ \text{{ft}}^2')])

# ═══════════════════════ 11.4 ═══════════════════════
RADII = lambda m: T('Use $s=\\dfrac{a+b+c}2$, $\\Delta=\\sqrt{s(s-a)(s-b)(s-c)}$, $r=\\dfrac\\Delta s$, $R=\\dfrac{abc}{4\\Delta}$, $r_1=\\dfrac\\Delta{s-a}$.', '$s=\\dfrac{a+b+c}2$، $\\Delta=\\sqrt{s(s-a)(s-b)(s-c)}$، $r=\\dfrac\\Delta s$، $R=\\dfrac{abc}{4\\Delta}$، $r_1=\\dfrac\\Delta{s-a}$ استعمال کریں۔', '$s=\\dfrac{a+b+c}2$، $\\Delta=\\sqrt{s(s-a)(s-b)(s-c)}$، $r=\\dfrac\\Delta s$، $R=\\dfrac{abc}{4\\Delta}$، $r_1=\\dfrac\\Delta{s-a}$ وکاروئ.', m)
def tri(a, b, c):
    s = (a+b+c)/2; D = sqrt(s*(s-a)*(s-b)*(s-c)); return s, D
for p, (a, b, c) in [('(i)', (3, 5, 6)), ('(ii)', (21, 20, 29))]:
    s, D = tri(a, b, c)
    put('11.4', 1, p, rf'$r\approx{num(D/s)},\ R\approx{num(a*b*c/(4*D))}$', [RADII(rf's={num(s)},\ \Delta=\sqrt{{{num(s)}({num(s-a)})({num(s-b)})({num(s-c)})}}\approx{num(D)}'),
        T('Substitute.', 'قیمتیں رکھیں۔', 'ارزښتونه کېږدئ.', rf'r=\frac{{{num(D)}}}{{{num(s)}}}\approx{num(D/s)},\qquad R=\frac{{({a})({b})({c})}}{{4({num(D)})}}\approx{num(a*b*c/(4*D))}')])
s, D = tri(55, 25, 70); r = D/s
put('11.4', 2, '', rf'$r\approx{num(r)}$ m, area $=\pi r^2\approx{num(pi*r*r,0)}$ m$^2$', [RADII(rf's=75,\ \Delta=\sqrt{{75(20)(50)(5)}}\approx{num(D)}'), T('In-radius and the circle′s area.', 'اندرونی نصف قطر اور دائرے کا رقبہ۔', 'داخلي شعاع او د دایرې مساحت.', rf'r=\frac{{{num(D)}}}{{75}}\approx{num(r)},\qquad\pi r^2\approx{num(pi*r*r,0)}\text{{ m}}^2')])
s, D = tri(30, 25, 20)
put('11.4', 3, '(i)', rf'$r_1=\dfrac\Delta{{s-30}}\approx{num(D/(s-30))}$ dm', [RADII(rf's=37.5,\ \Delta=\sqrt{{37.5(7.5)(12.5)(17.5)}}\approx{num(D)}'), T('Escribed circle opposite the largest side (30).', 'سب سے بڑے ضلع (30) کے مقابل بیرونی دائرہ۔', 'د تر ټولو لویې ضلعې (30) مخې ته بهرنۍ دایره.', rf'r_1=\frac{{{num(D)}}}{{37.5-30}}\approx{num(D/(s-30))}')])
put('11.4', 3, '(ii)', rf'$r_3=\dfrac\Delta{{s-20}}\approx{num(D/(s-20))}$ dm', [RADII(rf's=37.5,\ \Delta\approx{num(D)}'), T('Escribed circle opposite the smallest side (20).', 'سب سے چھوٹے ضلع (20) کے مقابل بیرونی دائرہ۔', 'د تر ټولو کوچنۍ ضلعې (20) مخې ته بهرنۍ دایره.', rf'r_3=\frac{{{num(D)}}}{{37.5-20}}\approx{num(D/(s-20))}')])
FORM = lambda m: T('Use $r=\\dfrac\\Delta S$, $r_1=\\dfrac\\Delta{S-a}$, $r_2=\\dfrac\\Delta{S-b}$, $r_3=\\dfrac\\Delta{S-c}$, $\\Delta^2=S(S-a)(S-b)(S-c)$.', '$r=\\dfrac\\Delta S$، $r_1=\\dfrac\\Delta{S-a}$، $r_2=\\dfrac\\Delta{S-b}$، $r_3=\\dfrac\\Delta{S-c}$، $\\Delta^2=S(S-a)(S-b)(S-c)$ استعمال کریں۔', '$r=\\dfrac\\Delta S$، $r_1=\\dfrac\\Delta{S-a}$، $r_2=\\dfrac\\Delta{S-b}$، $r_3=\\dfrac\\Delta{S-c}$، $\\Delta^2=S(S-a)(S-b)(S-c)$ وکاروئ.', m)
put('11.4', 4, '(i)', 'Proved (see the steps).', [FORM(r'r\,r_1r_2r_3=\frac{\Delta^4}{S(S-a)(S-b)(S-c)}=\frac{\Delta^4}{\Delta^2}=\Delta^2'), T('Take the square root.', 'جذر لیں۔', 'جذر ونیسئ.', r'\sqrt{r\,r_1r_2r_3}=\Delta'), QED])
put('11.4', 4, '(ii)', 'Proved (see the steps).', [T('Use $\\sin\\alpha=\\dfrac{2\\Delta}{bc}$, $\\sin\\beta=\\dfrac{2\\Delta}{ca}$, $\\sin\\gamma=\\dfrac{2\\Delta}{ab}$.', '$\\sin\\alpha=\\dfrac{2\\Delta}{bc}$، $\\sin\\beta=\\dfrac{2\\Delta}{ca}$، $\\sin\\gamma=\\dfrac{2\\Delta}{ab}$ استعمال کریں۔', '$\\sin\\alpha=\\dfrac{2\\Delta}{bc}$، $\\sin\\beta=\\dfrac{2\\Delta}{ca}$، $\\sin\\gamma=\\dfrac{2\\Delta}{ab}$ وکاروئ.', r'abc(\sin\alpha+\sin\beta+\sin\gamma)=2\Delta(a+b+c)'),
    T('Since $a+b+c=2s$:', 'چونکہ $a+b+c=2s$:', 'ځکه $a+b+c=2s$:', r'=2\Delta\cdot2s=4\Delta s'), QED])
put('11.4', 4, '(iii)', 'Proved (see the steps).', [FORM(r'r_1r_2r_3=\frac{\Delta^3}{(S-a)(S-b)(S-c)}=\frac{\Delta^3\,S}{S(S-a)(S-b)(S-c)}=\frac{\Delta^3S}{\Delta^2}=\Delta S'), T('Write $\\Delta=rS$.', '$\\Delta=rS$ لکھیں۔', '$\\Delta=rS$ ولیکئ.', r'\Delta S=rS\cdot S=rS^2'), QED])
Sa, a_, b_, c_ = S.symbols('S a b c', positive=True)
put('11.4', 5, '(i)', 'Proved (see the steps).', [FORM(r'r_1+r_2-r_3... '.replace('... ', '') if False else r'r_1+r_2=\Delta\left(\frac1{S-a}+\frac1{S-b}\right)=\frac{\Delta(2S-a-b)}{(S-a)(S-b)}=\frac{\Delta c}{(S-a)(S-b)}'),
    T('Similarly combine $r_3-r$.', 'اسی طرح $r_3-r$ کو یکجا کریں۔', 'همداسې $r_3-r$ یو ځای کړئ.', r'r_3-r=\Delta\left(\frac1{S-c}-\frac1S\right)=\frac{\Delta c}{S(S-c)}'),
    T('Add and use $\\Delta^2=S(S-a)(S-b)(S-c)$.', 'جمع کریں اور $\\Delta^2=S(S-a)(S-b)(S-c)$ استعمال کریں۔', 'جمع یې کړئ او $\\Delta^2=S(S-a)(S-b)(S-c)$ وکاروئ.', r'r_1+r_2+r_3-r=\Delta c\,\frac{S(S-c)+(S-a)(S-b)}{\Delta^2}=\frac{c\,(2S^2-(a+b+c)S+ab)}{\Delta}=\frac{c\cdot ab}{\Delta}'),
    T('Since $R=\\dfrac{abc}{4\\Delta}$:', 'چونکہ $R=\\dfrac{abc}{4\\Delta}$:', 'ځکه $R=\\dfrac{abc}{4\\Delta}$:', r'\frac{abc}{\Delta}=4R'), QED])
put('11.4', 5, '(ii)', 'Proved (see the steps).', [FORM(r'r_1r_2+r_2r_3+r_3r_1=\Delta^2\,\frac{(S-c)+(S-a)+(S-b)}{(S-a)(S-b)(S-c)}'),
    T('Simplify: $(S-a)+(S-b)+(S-c)=3S-2S=S$.', 'مختصر کریں: $(S-a)+(S-b)+(S-c)=3S-2S=S$۔', 'ساده کړئ: $(S-a)+(S-b)+(S-c)=3S-2S=S$.', r'=\frac{\Delta^2S}{(S-a)(S-b)(S-c)}=\frac{\Delta^2S^2}{\Delta^2}=S^2'), QED])
put('11.4', 5, '(iii)', 'Proved (see the steps).', [FORM(r'\frac1{r_1}+\frac1{r_2}+\frac1{r_3}=\frac{(S-a)+(S-b)+(S-c)}{\Delta}=\frac{3S-2S}{\Delta}=\frac S\Delta'), T('And $\\dfrac1r=\\dfrac S\\Delta$.', 'اور $\\dfrac1r=\\dfrac S\\Delta$۔', 'او $\\dfrac1r=\\dfrac S\\Delta$.', r'\frac1{r_1}+\frac1{r_2}+\frac1{r_3}=\frac1r'), QED])
for p, sd, nm, lt in [('(i)', 'a', r'\alpha', '1'), ('(ii)', 'b', r'\beta', '2'), ('(iii)', 'c', r'\gamma', '3')]:
    others = {'a': ('b', 'c'), 'b': ('a', 'c'), 'c': ('a', 'b')}[sd]
    put('11.4', 6, p, 'Proved (see the steps).', [T('Use the half-angle formula for the tangent.', 'نصف زاویے کے ٹینجنٹ کا کلیہ استعمال کریں۔', 'د نیمې زاویې ټانجنټ فورمول وکاروئ.', rf'\tan\frac{{{nm}}}2=\sqrt{{\frac{{(S-{others[0]})(S-{others[1]})}}{{S(S-{sd})}}}}'),
        T('Multiply by $S$ and use $\\Delta^2=S(S-a)(S-b)(S-c)$.', '$S$ سے ضرب دیں اور $\\Delta^2=S(S-a)(S-b)(S-c)$ استعمال کریں۔', 'په $S$ ضرب کړئ او $\\Delta^2=S(S-a)(S-b)(S-c)$ وکاروئ.', rf'S\tan\frac{{{nm}}}2=\sqrt{{\frac{{S(S-a)(S-b)(S-c)}}{{(S-{sd})^2}}}}=\frac\Delta{{S-{sd}}}=r_{lt}'), QED])
k = S.Symbol('k', positive=True)
sk = S.Rational(9) * k; Dk = S.sqrt(sk*(sk-3*k)*(sk-7*k)*(sk-8*k))
assert S.simplify(Dk - 6*S.sqrt(3)*k**2) == 0
put('11.4', 7, '', r'$3\sqrt3,\ 7\sqrt3,\ 8\sqrt3$ m', [T('Let the sides be $3k,7k,8k$.', 'اضلاع $3k,7k,8k$ فرض کریں۔', 'ضلعې $3k,7k,8k$ فرض کړئ.', r's=\frac{3k+7k+8k}2=9k'),
    HER(r'\Delta=\sqrt{9k\cdot6k\cdot2k\cdot k}=\sqrt{108}\,k^2=6\sqrt3\,k^2'), T('Use $r=\\dfrac\\Delta s=2$.', '$r=\\dfrac\\Delta s=2$ استعمال کریں۔', '$r=\\dfrac\\Delta s=2$ وکاروئ.', r'\frac{6\sqrt3k^2}{9k}=2\Rightarrow k=\sqrt3'),
    ANSL(r'3k=3\sqrt3,\ 7k=7\sqrt3,\ 8k=8\sqrt3')])

# ═══════════════════════ Review 11 ═══════════════════════
MCQ = lambda m: T('Work out the value and compare it with the options.', 'قیمت نکال کر اختیارات سے موازنہ کریں۔', 'ارزښت ومومئ او له انتخابونو سره یې پرتله کړئ.', m)
put('Review 11', 1, '(i)', r'(c) $\sqrt{21}$', [MCQ(r'b=\sqrt{c^2-a^2}=\sqrt{25-4}=\sqrt{21}\Rightarrow\text{(c)}')], category='mcqs')
put('Review 11', 1, '(ii)', r'(b) $24\sqrt2$ ft', [MCQ(r'\sin45^\circ=\frac{24}{L}\Rightarrow L=\frac{24}{1/\sqrt2}=24\sqrt2\Rightarrow\text{(b)}')], category='mcqs')
put('Review 11', 1, '(iii)', r'(a) $\frac a4\sqrt{4b^2-a^2}$', [MCQ(r'h=\sqrt{b^2-\tfrac{a^2}4}=\tfrac12\sqrt{4b^2-a^2},\ \Delta=\tfrac12a h=\tfrac a4\sqrt{4b^2-a^2}\Rightarrow\text{(a)}')], category='mcqs')
put('Review 11', 1, '(iv)', r'(d) $\Delta=\sqrt{7(4)(2)(1)}$', [MCQ(r's=\tfrac{3+5+6}2=7,\ s-a=4,\ s-b=2,\ s-c=1\Rightarrow\Delta=\sqrt{7(4)(2)(1)}\Rightarrow\text{(d)}')], category='mcqs')
put('Review 11', 1, '(v)', r'(d) 3 cm', [MCQ(r'\text{right angle at }B,\ \angle A=30^\circ,\ AC=6:\ BC=AC\sin30^\circ=3\text{ cm}\Rightarrow\text{(d)}')], category='mcqs')
put('Review 11', 1, '(vi)', r'(c) $75\sqrt3$ m', [T('The angle of depression from the top equals the angle of elevation from the object.', 'چوٹی سے زاویہ انخفاض شے سے زاویہ ارتفاع کے برابر ہے۔', 'له سر نه د ټیټوالي زاویه له شي نه د لوړوالي له زاویې سره مساوي ده.'),
    MCQ(r'\tan30^\circ=\frac{75}x\Rightarrow x=\frac{75}{1/\sqrt3}=75\sqrt3\text{ m}\Rightarrow\text{(c)}')], category='mcqs')
put('Review 11', 1, '(vii)', '(c) Circumcentre', [MCQ(r'\text{the right bisectors meet at the point equidistant from all three vertices: the circumcentre}\Rightarrow\text{(c)}')], category='mcqs')
put('Review 11', 1, '(viii)', r'(b) $\Delta^2$', [MCQ(r'r\,r_1r_2r_3=\frac\Delta S\cdot\frac{\Delta^3}{(S-a)(S-b)(S-c)}=\frac{\Delta^4}{\Delta^2}=\Delta^2\Rightarrow\text{(b)}')], category='mcqs')
(b_, al, ga), ss = sas(0.7, 0.8, DM(141, 30), ('a', 'c', r'\beta', 'b', r'\alpha', r'\gamma'), mins=True)
put('Review 11', 2, '(i)', rf'$b\approx{num(b_)},\ \alpha\approx{ang(al,True)},\ \gamma\approx{ang(ga,True)}$', ss)
put('Review 11', 2, '(ii)', 'No triangle is possible.', [T('Triangle inequality: the sum of two sides must exceed the third.', 'مثلث کی عدم مساوات: دو اضلاع کا مجموعہ تیسرے سے زیادہ ہونا چاہیے۔', 'د درې ګوني نامساوات: د دوو ضلعو مجموعه باید له درېیمې زیاته وي.', r'34+23=57<58'), T('So these lengths cannot form a triangle.', 'لہٰذا یہ لمبائیاں مثلث نہیں بنا سکتیں۔', 'نو دا اوږدوالي درې ګونی نه شي جوړولی.')])
(c_, al, be), ss = sas(15.6, 18, DM(35, 10), ('a', 'b', r'\gamma', 'c', r'\alpha', r'\beta'), mins=True)
put('Review 11', 2, '(iii)', rf'$c\approx{num(c_,1)},\ \alpha\approx{ang(al,True)},\ \beta\approx{ang(be,True)}$', ss)
(c_, al, be), ss = sas(48, 32, 57, ('a', 'b', r'\gamma', 'c', r'\alpha', r'\beta'), mins=True)
put('Review 11', 2, '(iv)', rf'$c\approx{num(c_)},\ \alpha\approx{ang(al,True)},\ \beta\approx{ang(be,True)}$', ss)
(a_, be, ga), ss = sas(35, 37, DM(23, 25), ('b', 'c', r'\alpha', 'a', r'\beta', r'\gamma'), mins=True)
put('Review 11', 2, '(v)', rf'$a\approx{num(a_)},\ \beta\approx{ang(be,True)},\ \gamma\approx{ang(ga,True)}$', ss)
al = 180-37.2-100
(b_, c_), ss = aas(58.4, al, 37.2, 100, ('a', r'\alpha', r'\beta', r'\gamma', 'b', 'c'))
put('Review 11', 2, '(vi)', rf'$\alpha={num(al,1)}^\circ,\ b\approx{num(b_,1)},\ c\approx{num(c_,1)}$', [SUM(rf'\alpha=180^\circ-37.2^\circ-100^\circ={num(al,1)}^\circ')] + ss)
ga = 180-DM(30, 24)-DM(72, 6)
(a_, b_), ss = aas(13.6, ga, DM(30, 24), DM(72, 6), ('c', r'\gamma', r'\alpha', r'\beta', 'a', 'b'), mins=True)
put('Review 11', 2, '(vii)', rf'$\gamma={ang(ga,True)},\ a\approx{num(a_)},\ b\approx{num(b_,1)}$', [SUM(rf'\gamma=180^\circ-30^\circ24′-72^\circ6′={ang(ga,True)}')] + ss)
SMALL = lambda m: T('The smallest angle is opposite the shortest side.', 'سب سے چھوٹا زاویہ سب سے چھوٹے ضلع کے مقابل ہوتا ہے۔', 'تر ټولو کوچنۍ زاویه د تر ټولو لنډې ضلعې مخې ته وي.', m)
for p, (a, b, c) in [('(i)', (4.3, 5.1, 6.3)), ('(ii)', (3, 4.2, 3.8))]:
    t = degrees(acos((b*b+c*c-a*a)/(2*b*c)))
    put('Review 11', 3, p, rf'about ${num(t,1)}^\circ$', [SMALL(rf'\text{{shortest side}}={a}'), COSA(rf'\cos\theta=\frac{{{b}^2+{c}^2-{a}^2}}{{2({b})({c})}}\approx{(b*b+c*c-a*a)/(2*b*c):.4f}\Rightarrow\theta\approx{num(t,1)}^\circ')])
LARGE = lambda m: T('The largest angle is opposite the longest side.', 'سب سے بڑا زاویہ سب سے لمبے ضلع کے مقابل ہوتا ہے۔', 'تر ټولو لویه زاویه د تر ټولو اوږدې ضلعې مخې ته وي.', m)
for p, (a, b, c) in [('(i)', (4.1, 2.9, 3.3)), ('(ii)', (9.4, 6.0, 8))]:
    t = degrees(acos((b*b+c*c-a*a)/(2*b*c)))
    put('Review 11', 4, p, rf'about ${num(t,1)}^\circ$', [LARGE(rf'\text{{longest side}}={a}'), COSA(rf'\cos\theta=\frac{{{b}^2+{c}^2-{a}^2}}{{2({b})({c})}}\approx{(b*b+c*c-a*a)/(2*b*c):.4f}\Rightarrow\theta\approx{num(t,1)}^\circ')])
d1 = sqrt(25**2+35**2-2*25*35*cos(d(36))); d2 = sqrt(25**2+35**2-2*25*35*cos(d(144)))
put('Review 11', 5, '', rf'about ${num(d2,1)}$ cm and ${num(d1,1)}$ cm', [T('Adjacent angles of a parallelogram are $36^\\circ$ and $144^\\circ$; each diagonal is opposite one of them.', 'متوازی الاضلاع کے متصل زاویے $36^\\circ$ اور $144^\\circ$ ہیں؛ ہر قطر ان میں سے ایک کے مقابل ہے۔', 'د متوازي الاضلاع نږدې زاویې $36^\\circ$ او $144^\\circ$ دي؛ هر قطر د یوې مخې ته دی.'),
    COS(rf'd_1^2=25^2+35^2-2(25)(35)\cos36^\circ\Rightarrow d_1\approx{num(d1)};\quad d_2^2=25^2+35^2-2(25)(35)\cos144^\circ\Rightarrow d_2\approx{num(d2)}')])
put('Review 11', 6, '', r'$25\sqrt3\approx43.3$ m', [RT(r'\sin60^\circ=\frac h{50}\Rightarrow h=50\cdot\frac{\sqrt3}2=25\sqrt3\approx43.3\text{ m}')])
r1, r2 = 40/sin(d(14)), 55/sin(d(19))
put('Review 11', 7, '', rf'robin $\approx{num(r1,1)}$ ft, crow $\approx{num(r2,1)}$ ft from the worm', [FIG(r'\text{robin }40\text{ ft high, crow }40+15=55\text{ ft high}'),
    RT(rf'\text{{robin: }}\sin14^\circ=\frac{{40}}{{d_1}}\Rightarrow d_1=\frac{{40}}{{\sin14^\circ}}\approx{num(r1,1)};\quad\text{{crow: }}d_2=\frac{{55}}{{\sin19^\circ}}\approx{num(r2,1)}'),
    KEY('it gives only 165.3 ft, which is the robin′s distance; the crow′s distance is also asked.', 'اس میں صرف 165.3 فٹ ہے جو رابن کا فاصلہ ہے؛ کوے کا فاصلہ بھی پوچھا گیا ہے۔', 'په کې یوازې 165.3 فټه ده چې د رابن واټن دی؛ د کارغه واټن هم پوښتل شوی.')])
h = 20/(1/tan(d(48))-1/tan(d(61)))
put('Review 11', 8, '', rf'about ${num(h,1)}$ m', [FIG(r'A\text{ and }B\text{ on the same side, }AB=20\text{ m},\ A\text{ farther}'),
    RT(r'x_A=\frac h{\tan48^\circ},\ x_B=\frac h{\tan61^\circ},\ x_A-x_B=20'),
    T('Solve for $h$.', '$h$ معلوم کریں۔', '$h$ ومومئ.', rf'h=\frac{{20}}{{\cot48^\circ-\cot61^\circ}}\approx{num(h,1)}\text{{ m}}')])

flush()
A.save(['11.1', '11.2', '11.3', '11.4', 'Review 11'], list(range(303, 340)) + [425])
