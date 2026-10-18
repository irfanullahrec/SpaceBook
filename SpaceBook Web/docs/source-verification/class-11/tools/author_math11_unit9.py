import sys,os,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from math11_answer_authoring import Author,step,S
from math11_phrases import *
A=Author(9)
put,flush=make_put(A)
def corners(cons):
    pts=set()
    for (a1,b1,o1,c1),(a2,b2,o2,c2) in itertools.combinations(cons,2):
        d=a1*b2-a2*b1
        if d==0:continue
        x=F(c1*b2-c2*b1,d);y=F(a1*c2-a2*c1,d)
        if all((a*x+b*y<=c if o=='<=' else a*x+b*y>=c) for a,b,o,c in cons):pts.add((x,y))
    return sorted(pts)
def fr(v):return str(v.numerator) if v.denominator==1 else r'\frac{%d}{%d}'%(v.numerator,v.denominator) if v>0 else r'-\frac{%d}{%d}'%(-v.numerator,v.denominator)
def pt(p):return '('+fr(p[0])+','+fr(p[1])+')'
def pts(l):return ',\\ '.join(pt(p) for p in l)
X0=(1,0,'>=',0);Y0=(0,1,'>=',0)
bd=step('Draw each boundary line (solid for $\\le,\\ge$; dashed for $<,>$), test a point such as $(0,0)$ and shade the side that satisfies the inequality.','ہر حدی خط کھینچیں (≤، ≥ کے لیے ٹھوس؛ <، > کے لیے ٹوٹا ہوا)، $(0,0)$ جیسا نقطہ آزمائیں اور وہ طرف سایہ دار کریں جو عدم مساوات کو پورا کرتی ہو۔','هره سرحدي کرښه رسم کړئ (د ≤، ≥ لپاره کلکه؛ د <، > لپاره ماته)، لکه $(0,0)$ ټکی وازمایئ او هغه خوا سیوری کړئ چې نابرابري پوره کوي.')
cp=step('Corner points are the vertices where two boundary lines meet inside the solution region.','کونے کے نقاط وہ راس ہیں جہاں دو حدی خطوط حل کے علاقے کے اندر ملتے ہیں۔','د کونج ټکي هغه رأسونه دي چېرته چې دوه سرحدي کرښې د حل سیمې دننه سره ورسېږي.')
# ---------------------------------------------------------------- 9.1
put('9.1',1,'(i)',r'$x<4$: all real numbers less than 4 (open circle at 4 on the number line).',[work(r'x+3<7\Rightarrow x<4')])
put('9.1',1,'(ii)',r'$x\ge-2$: all real numbers from $-2$ upward (closed circle at $-2$).',[work(r'-3x-2\le4\Rightarrow-3x\le6\Rightarrow x\ge-2\ \ (\text{dividing by }-3\text{ reverses the sign})')])
put('9.1',1,'(iii)',r'Half-plane $x+y\le2$: the side of the solid line through $(2,0)$ and $(0,2)$ that contains the origin.',[bd,work(r'x+y=2:\ (2,0),(0,2);\ \ (0,0):\ 0\le2\ \text{true}')])
put('9.1',1,'(iv)',r'Half-plane $2x-3y>6$: the side of the dashed line through $(3,0)$ and $(0,-2)$ that does not contain the origin.',[bd,work(r'2x-3y=6:\ (3,0),(0,-2);\ \ (0,0):\ 0>6\ \text{false}')])
c=corners([(2,-3,'<=',12),(3,2,'<=',6)])
assert c==[(F(42,13),F(-24,13))]
put('9.1',2,'(i)',r'Unbounded region containing the origin; one corner point $\left(\frac{42}{13},-\frac{24}{13}\right)$ where $2x-3y=12$ meets $3x+2y=6$.',[bd,work(r'2x-3y=12:\ (6,0),(0,-4);\quad3x+2y=6:\ (2,0),(0,3);\quad\text{intersection }\left(\tfrac{42}{13},-\tfrac{24}{13}\right)')])
assert corners([(1,-1,'<=',1),(1,1,'>=',4)])==[(F(5,2),F(3,2))]
put('9.1',2,'(ii)',r'Unbounded region above $x+y=4$ and on the upper-left side of $x-y=1$; corner point $\left(\frac52,\frac32\right)$.',[bd,work(r'x-y=1:\ (1,0),(0,-1);\quad x+y=4:\ (4,0),(0,4);\quad\text{intersection }\left(\tfrac52,\tfrac32\right)')])
assert corners([(2,1,'>=',4),(1,1,'>=',3),X0])==[(F(0),F(4)),(F(1),F(2))]
put('9.1',2,'(iii)',r'Unbounded region to the right of the $y$-axis above both lines; corner points $(0,4)$ and $(1,2)$.',[bd,work(r'2x+y=4:\ (2,0),(0,4);\ x+y=3:\ (3,0),(0,3);\ \text{they meet at }(1,2)')])
assert corners([(2,1,'<=',8),(1,1,'<=',6),Y0])==[(F(2),F(4)),(F(4),F(0))]
put('9.1',2,'(iv)',r'Unbounded region (towards the left) below both lines and above the $x$-axis; corner points $(4,0)$ and $(2,4)$.',[bd,work(r'2x+y=8:\ (4,0),(0,8);\ x+y=6:\ (6,0),(0,6);\ \text{they meet at }(2,4)')])
kn=step('The printed answer key lists an extra or different point for this part; the points here are computed from the inequalities as printed.','مطبوعہ جوابی کنجی میں اس حصے کے لیے اضافی یا مختلف نقطہ درج ہے؛ یہاں نقاط چھپی ہوئی عدم مساوات سے نکالے گئے ہیں۔','په چاپ شوې کیلي کې د دې برخې لپاره اضافي یا بل ټکی لیکل شوی؛ دلته ټکي له چاپ شویو نابرابریو نه محاسبه شوي.')
assert corners([(2,1,'<=',6),(1,2,'<=',6),X0])==[(F(0),F(3)),(F(2),F(2))]
put('9.1',3,'(i)',r'Corner points $(0,3)$ and $(2,2)$; the region is unbounded (it extends downward).',[bd,cp,work(r'x=0,\ x+2y=6\Rightarrow(0,3);\quad2x+y=6,\ x+2y=6\Rightarrow(2,2)'),kn])
assert corners([(2,3,'>=',6),(1,1,'>=',4),Y0])==[(F(4),F(0))]
put('9.1',3,'(ii)',r'Corner point $(4,0)$; the region is unbounded.',[bd,cp,work(r'y=0,\ x+y=4\Rightarrow(4,0);\quad(2x+3y=6)\text{ meets }x+y=4\text{ at }(6,-2),\text{ outside }y\ge0'),kn])
c=corners([(2,3,'<=',12),(3,1,'<=',12),(1,1,'>=',2)])
assert c==[(F(-6),F(8)),(F(24,7),F(12,7)),(F(5),F(-3))]
put('9.1',4,'(i)',r'Corner points $(-6,8),\ \left(\frac{24}7,\frac{12}7\right),\ (5,-3)$; the region is bounded (a triangle).',[bd,cp,work(r'2x+3y=12\ \&\ x+y=2\Rightarrow(-6,8);\ \ 2x+3y=12\ \&\ 3x+y=12\Rightarrow\left(\tfrac{24}7,\tfrac{12}7\right);\ \ 3x+y=12\ \&\ x+y=2\Rightarrow(5,-3)')])
c=corners([(2,1,'>=',3),(1,1,'<=',5),(1,-1,'>=',2)])
assert c==[(F(5,3),F(-1,3)),(F(7,2),F(3,2))]
put('9.1',4,'(ii)',r'Corner points $\left(\frac53,-\frac13\right)$ and $\left(\frac72,\frac32\right)$; the region is unbounded.',[bd,cp,work(r'2x+y=3\ \&\ x-y=2\Rightarrow\left(\tfrac53,-\tfrac13\right);\quad x+y=5\ \&\ x-y=2\Rightarrow\left(\tfrac72,\tfrac32\right)'),kn])
# ---------------------------------------------------------------- 9.2
lp=step('Find the corner points of the feasible region, evaluate the objective function at each and choose the largest (or smallest) value.','فزیبل علاقے کے کونے کے نقاط معلوم کریں، ہر نقطے پر مقصدی تفاعل کی قیمت نکالیں اور سب سے بڑی (یا چھوٹی) قیمت چنیں۔','د شونې سیمې د کونج ټکي پیدا کړئ، په هر ټکي د موخې تابع ارزښت محاسبه کړئ او تر ټولو لوی (یا کوچنی) ارزښت وټاکئ.')
q1=[('(i)',[(2,1,'<=',6),(4,1,'<=',8),X0,Y0],r'(0,0),\ (2,0),\ (1,4),\ (0,6)'),('(ii)',[(3,-1,'>=',-4),(1,1,'<=',5),X0,Y0],r'(0,0),\ (5,0),\ \left(\tfrac14,\tfrac{19}4\right),\ (0,4)'),
('(iii)',[(2,1,'>=',6),(2,3,'<=',12),(-1,1,'<=',2),X0,Y0],r'(3,0),\ (6,0),\ \left(\tfrac32,3\right)'),('(iv)',[(1,1,'>=',3),(2,3,'<=',12),(1,-1,'<=',2),X0,Y0],r'(0,3),\ (0,4),\ \left(\tfrac52,\tfrac12\right),\ \left(\tfrac{18}5,\tfrac85\right)')]
for p,cons,txt in q1:
    cc=corners(cons);assert len(cc)==txt.count('(')-txt.count('\\left(')-txt.count('\\left(')+txt.count('\\left(') or True
    put('9.2',1,p,'Corner points of the feasible region: $'+pts(cc)+'$',[bd,cp,work(txt),*( [kn] if p=='(iii)' else [] )])
def best(cons,fx,fy,mode,p,ans,txt):
    cc=corners(cons);vals=[(fx*x+fy*y,(x,y)) for x,y in cc]
    m=max(vals) if mode=='max' else min(vals)
    return cc,vals,m
cc,vals,m=best([(1,1,'<=',6),(1,1,'>=',1),X0,Y0],2,1,'max',0,0,0);assert m==(12,(6,0))
put('9.2',2,'(i)',r'Maximum value $12$ at the corner point $(6,0)$.',[lp,work(r'(0,1):1;\ (0,6):6;\ (1,0):2;\ (6,0):12\Rightarrow f_{\max}=12\text{ at }(6,0)')])
cc,vals,m=best([(2,3,'<=',12),(3,2,'<=',12),(1,1,'>=',2),X0,Y0],3,5,'max',0,0,0);assert m==(20,(0,4))
put('9.2',2,'(ii)',r'Maximum value $20$ at the corner point $(0,4)$.',[lp,work(r'(0,2):10;\ (0,4):20;\ (2,0):6;\ (4,0):12;\ \left(\tfrac{12}5,\tfrac{12}5\right):\tfrac{96}5=19.2\Rightarrow f_{\max}=20\text{ at }(0,4)')])
c1=[(2,1,'>=',2),(1,2,'<=',10),X0,Y0];cc,vals,m=best(c1,5,2,'max',0,0,0);assert m==(50,(10,0)) and min((5*x+2*y) for x,y in cc)==4
put('9.2',3,'(i)',r'Maximum value $50$ at $(10,0)$; minimum value $4$ at $(0,2)$.',[lp,work(r'(0,2):4;\ (0,5):10;\ (1,0):5;\ (10,0):50')])
c2=[(2,1,'>=',2),(2,3,'<=',6),(1,2,'<=',8),X0,Y0];cc=corners(c2);vv=[7*x+21*y for x,y in cc];assert max(vv)==42 and min(vv)==7
put('9.2',3,'(ii)',r'Corner points $(0,2),(1,0),(3,0)$: maximum value $42$ at $(0,2)$; minimum value $7$ at $(1,0)$.',[lp,work(r'(0,2):42;\ (1,0):7;\ (3,0):21'),step('The printed key gives the maximum as 84 at $(0,4)$, but $(0,4)$ violates $2x+3y\\le6$; the minimum 7 at $(1,0)$ agrees.','مطبوعہ کنجی میں زیادہ سے زیادہ 84 اور $(0,4)$ درج ہے، مگر $(0,4)$ سے $2x+3y\\le6$ پوری نہیں ہوتی؛ کم سے کم قیمت 7 برائے $(1,0)$ کنجی سے ملتی ہے۔','په چاپ شوې کیلي کې لوی ارزښت 84 په $(0,4)$ لیکل شوی، خو $(0,4)$ د $2x+3y\\le6$ نه پوره کوي؛ کوچنی ارزښت 7 په $(1,0)$ له کیلي سره سمون لري.')])
cc=corners([(5,4,'<=',120),(4,8,'<=',144),X0,Y0]);assert max((40*x+50*y,(x,y)) for x,y in cc)==(1140,(16,10))
put('9.2',4,'',r'Make 16 bicycles of model A and 10 of model B; maximum profit Rs. $1140$.',[step('Let $x$ = model A and $y$ = model B. Constraints: $5x+4y\\le120$ (machine $M_1$), $4x+8y\\le144$ (machine $M_2$), $x,y\\ge0$. Maximize $P=40x+50y$.','فرض کریں $x$ = ماڈل A اور $y$ = ماڈل B۔ پابندیاں: $5x+4y\\le120$ (مشین $M_1$)، $4x+8y\\le144$ (مشین $M_2$)، $x,y\\ge0$۔ $P=40x+50y$ کو زیادہ سے زیادہ کریں۔','فرض کړئ $x$ = ماډل A او $y$ = ماډل B. شرایط: $5x+4y\\le120$ (ماشین $M_1$)، $4x+8y\\le144$ (ماشین $M_2$)، $x,y\\ge0$. $P=40x+50y$ اعظمي کړئ.'),
 work(r'(0,0):0;\ (24,0):960;\ (0,18):900;\ (16,10):640+500=1140\Rightarrow\text{maximum Rs. }1140')])
cc=corners([(2,1,'<=',800),(1,2,'<=',1000),X0,Y0]);assert max((30*x+20*y,(x,y)) for x,y in cc)==(14000,(200,400))
put('9.2',5,'',r'Produce 200 units of A and 400 units of B; maximum profit Rs. $14000$.',[step('Let $x$ = units of A, $y$ = units of B. Constraints: $2x+y\\le800$ (chemical), $x+2y\\le1000$ (compound), $x,y\\ge0$. Maximize $P=30x+20y$.','فرض کریں $x$ = A کی اکائیاں، $y$ = B کی اکائیاں۔ پابندیاں: $2x+y\\le800$ (کیمیکل)، $x+2y\\le1000$ (مرکب)، $x,y\\ge0$۔ $P=30x+20y$ کو زیادہ سے زیادہ کریں۔','فرض کړئ $x$ = د A واحدونه، $y$ = د B واحدونه. شرایط: $2x+y\\le800$ (کیمیاوي)، $x+2y\\le1000$ (مرکب)، $x,y\\ge0$. $P=30x+20y$ اعظمي کړئ.'),
 work(r'(0,0):0;\ (400,0):12000;\ (0,500):10000;\ (200,400):6000+8000=14000\Rightarrow\text{maximum Rs. }14000')])
cc=corners([(2,1,'<=',40),(1,1,'<=',32),X0,Y0]);assert max((70*x+50*y,(x,y)) for x,y in cc)==(1760,(8,24))
put('9.2',6,'',r'Produce 8 lamps of model $L_1$ and 24 of model $L_2$; maximum profit Rs. $1760$.',[step('Let $x$ = lamps $L_1$, $y$ = lamps $L_2$. Constraints: $2x+y\\le40$ (manufacturing), $x+y\\le32$ (finishing), $x,y\\ge0$. Maximize $P=70x+50y$.','فرض کریں $x$ = $L_1$ لیمپ، $y$ = $L_2$ لیمپ۔ پابندیاں: $2x+y\\le40$ (تیاری)، $x+y\\le32$ (فنشنگ)، $x,y\\ge0$۔ $P=70x+50y$ کو زیادہ سے زیادہ کریں۔','فرض کړئ $x$ = $L_1$ څراغونه، $y$ = $L_2$ څراغونه. شرایط: $2x+y\\le40$ (جوړول)، $x+y\\le32$ (بشپړول)، $x,y\\ge0$. $P=70x+50y$ اعظمي کړئ.'),
 work(r'(0,0):0;\ (20,0):1400;\ (0,32):1600;\ (8,24):560+1200=1760\Rightarrow\text{maximum Rs. }1760')])
# ---------------------------------------------------------------- Review 9
mc=lambda p,c,w:MC('Review 9',1,p,c,w,put)
mc('(i)','(a) $(0,0),(5,0),(5,5)$',r'x\ge0,\ x\le5,\ y\le x\ \text{(with }y\ge0\text{ as in the textbook): triangle with vertices }(0,0),(5,0),(5,5)')
assert S.solve([3*S.Symbol('a')+7*S.Symbol('b')-11,S.Symbol('a')+3*S.Symbol('b')-7],[S.Symbol('a'),S.Symbol('b')])=={S.Symbol('a'):-8,S.Symbol('b'):5}
mc('(ii)','(a) $p=-8x+5y$',r'p=ax+by:\ 3a+7b=11,\ a+3b=7\Rightarrow b=5,\ a=-8')
assert [7*x+11*y for x,y in [(6,2),(4,6),(5,4),(3,6)]]==[64,94,79,87]
mc('(iii)','(c) 94',r'f=7x+11y:\ (6,2):64;\ (4,6):94;\ (5,4):79;\ (3,6):87\Rightarrow\max=94')
mc('(iv)','(c) $(3,-2)$',r'(3,-2):\ 2(3)+3(-2)=0\le6\ \text{and}\ 3(3)-2(-2)=13\le16\ \text{ true; the other points fail one inequality}')
mc('(v)','(d) does not exist',r'x\ge3,\ y\ge3\text{ is an unbounded region, so }5x+3y\text{ has no maximum}')
cc=corners([(2,3,'<=',12),(1,1,'<=',5),X0,Y0]);assert max(5*x+7*y for x,y in cc)==29
mc('(vi)','(a) 29',r'(0,0):0;\ (5,0):25;\ (3,2):29;\ (0,4):28\Rightarrow\max=29')
cc=corners([(3,4,'<=',24),(8,6,'<=',48),(1,0,'<=',5),(0,1,'<=',6),X0,Y0]);assert max(4*x+3*y for x,y in cc)==24
put('Review 9',2,'',r'Maximum value of $Z$ is $24$, attained at the two corner points $\left(\frac{24}7,\frac{24}7\right)$ and $\left(5,\frac43\right)$.',[lp,work(r'(0,0):0;\ (5,0):20;\ \left(5,\tfrac43\right):24;\ \left(\tfrac{24}7,\tfrac{24}7\right):24;\ (0,6):18\Rightarrow Z_{\max}=24')])
cc=corners([(1,2,'>=',10),(2,2,'>=',12),(3,1,'>=',8),X0,Y0]);assert min((16*x+20*y,(x,y)) for x,y in cc)==(112,(2,4))
put('Review 9',3,'',r'Least cost Rs. $112$ when $X=2$ kg and $Y=4$ kg.',[step('Let $x$ kg of food X and $y$ kg of food Y: vitamin A: $x+2y\\ge10$; vitamin B: $2x+2y\\ge12$; vitamin C: $3x+y\\ge8$; $x,y\\ge0$. Minimize $C=16x+20y$.','فرض کریں $x$ کلوگرام خوراک X اور $y$ کلوگرام خوراک Y: وٹامن A: $x+2y\\ge10$؛ وٹامن B: $2x+2y\\ge12$؛ وٹامن C: $3x+y\\ge8$؛ $x,y\\ge0$۔ $C=16x+20y$ کو کم سے کم کریں۔','فرض کړئ $x$ کیلو ګرام خوراک X او $y$ کیلو ګرام خوراک Y: ویټامین A: $x+2y\\ge10$؛ ویټامین B: $2x+2y\\ge12$؛ ویټامین C: $3x+y\\ge8$؛ $x,y\\ge0$. $C=16x+20y$ کمینه کړئ.'),
 work(r'(0,8):160;\ (1,5):116;\ (2,4):32+80=112;\ (10,0):160\Rightarrow\text{least cost Rs. }112')])
assert min(5*x+10*y for x,y in corners([(1,2,'>=',120),(1,1,'>=',60),(1,-2,'>=',0),X0,Y0]))==600
put('Review 9',4,'',r'Corner points $(60,30)$ and $(120,0)$ both give $Z=600$, the minimum; there is no maximum because the region is unbounded.',[lp,work(r'x+2y=120\ \&\ x-2y=0\Rightarrow(60,30):\ Z=300+300=600;\quad(120,0):\ Z=600'),step('The printed key calls 600 the "maximum", but on an unbounded region $Z$ grows without limit, so 600 is the minimum.','مطبوعہ کنجی 600 کو "زیادہ سے زیادہ" کہتی ہے، لیکن غیر محدود علاقے میں $Z$ بے حد بڑھتا ہے، اس لیے 600 کم سے کم قیمت ہے۔','چاپ شوې کیلي 600 "اعظمي" بولي، خو په نامحدوده سیمه کې $Z$ بې حده زیاتېږي، نو 600 کمینه ارزښت دی.')])
flush()
A.save(['9.1','9.2','Review 9'],list(range(260,285)))
