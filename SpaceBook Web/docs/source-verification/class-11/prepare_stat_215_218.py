from stathelp import *
c=cell
U='time-series'
E65='stat11-ex-6-5'; E66='stat11-ex-6-6'; E67='stat11-ex-6-7'; E68='stat11-ex-6-8'
def row(a,b,d,vals): return [c(a,b,d)]+[c(str(v)) for v in vals]
N1=(r'\sum y=na+b\sum x+c\sum x^2\qquad\text{(i)}','Σy = na + bΣx + cΣx²   (i)')
N2=(r'\sum xy=a\sum x+b\sum x^2+c\sum x^3\qquad\text{(ii)}','Σxy = aΣx + bΣx² + cΣx³   (ii)')
N3=(r'\sum x^2y=a\sum x^2+b\sum x^3+c\sum x^4\qquad\text{(iii)}','Σx²y = aΣx² + bΣx³ + cΣx⁴   (iii)')
# ---------- scan 215 (printed 205) ----------
s=page(215,U,'205','Example 6.5: solution · Example 6.6 (question)','مثال 6.5: حل · مثال 6.6 (سوال)','بېلګه 6.5: حل · بېلګه 6.6 (پوښتنه)','ts-ls-2')
Flow(s)
add(s,'c1','Years: 1985–1993; Production: 60, 65, 80, 73, 97, 105, 93, 111, 117 (data of Example 6.5).','سال: 1985–1993؛ پیداوار: 60, 65, 80, 73, 97, 105, 93, 111, 117 (مثال 6.5 کے اعداد و شمار)۔','کلونه: 1985–1993؛ تولید: 60, 65, 80, 73, 97, 105, 93, 111, 117 (د بېلګې 6.5 معلومات).',role='question',exampleId=E65,sourceGap=dict(note='Continues the question of Example 6.5 from the previous page.'))
head(s,'sol65','Solution:','حل:','حل:',exampleId=E65)
add(s,'a1','Equation of the straight line is ŷ = a + bx where','سیدھی لکیر کی مساوات ہے ŷ = a + bx جہاں','د مستقیمې کرښې معادله ده ŷ = a + bx چېرته چې',role='solution',exampleId=E65)
add(s,'a2','Thus the fitted straight line equation is ŷ = 89 + 7.1x','اس طرح فٹ کی گئی سیدھی لکیر کی مساوات ہے ŷ = 89 + 7.1x','په دې توګه برابره شوې مستقیمې کرښې معادله ده ŷ = 89 + 7.1x',role='solution',exampleId=E65)
add(s,'a3','Putting values of x, we get trend values, which are given in the last column of the table.','x کی قدریں رکھنے سے ہمیں رجحان کی قدریں ملتی ہیں، جو جدول کے آخری کالم میں دی گئی ہیں۔','د x ارزښتونه ایښودو سره موږ د تمایل ارزښتونه ترلاسه کوو، چې د جدول په وروستي کالم کې ورکړل شوي دي.',role='solution',exampleId=E65)
head(s,'ex66','Example: 6.6','مثال: 6.6','بېلګه: 6.6',exampleId=E66)
add(s,'q66','Using the method of least squares, determine the linear trend for the following data, also find the trend values.','کم از کم مربعات کے طریقے سے درج ذیل اعداد و شمار کے لیے خطی رجحان معلوم کریں، رجحان کی قدریں بھی معلوم کریں۔','د لږ تر لږه مربعاتو په طریقه د لاندې معلوماتو لپاره خطي تمایل وټاکئ، د تمایل ارزښتونه هم ومومئ.',role='question',exampleId=E66)
rows=[(1985,60,-4,-240,16,'60.6'),(1986,65,-3,-195,9,'67.7'),(1987,80,-2,-160,4,'74.8'),(1988,73,-1,-73,1,'81.9'),(1989,97,0,0,0,'89'),(1990,105,1,105,1,'96.1'),(1991,93,2,186,4,'103.2'),(1992,111,3,333,9,'110.3'),(1993,117,4,468,16,'117.4')]
s['tables']=[table('Example 6.5: years and production','مثال 6.5: سال اور پیداوار','بېلګه 6.5: کلونه او تولید',[c('Years:','سال:','کلونه:')]+[c(str(v)) for v in range(1985,1994)],[row('Production:','پیداوار:','تولید:',[60,65,80,73,97,105,93,111,117])],exampleId=E65),
 table('Example 6.5 solution table','مثال 6.5 کا حل: جدول','د بېلګې 6.5 د حل جدول',[c('Year','سال','کال'),c('Production (y)','پیداوار (y)','تولید (y)'),c('x'),c('xy'),c('x²'),c('Trend value ŷ = 89 + 7.1x','رجحان کی قدر ŷ = 89 + 7.1x','د تمایل ارزښت ŷ = 89 + 7.1x')],[[c(str(r[0])),c(str(r[1])),c(str(r[2])),c(str(r[3])),c(str(r[4])),c(r[5])] for r in rows]+[[c('Total','میزان','ټولیز'),c('801'),c('0'),c('424'),c('60'),c('801')]],exampleId=E65),
 table('Example 6.6: years and imports','مثال 6.6: سال اور درآمدات','بېلګه 6.6: کلونه او واردات',[c('Years:','سال:','کلونه:')]+[c(str(v)) for v in range(1990,1996)],[row("Import (in 000's Maunds):",'درآمد (ہزار من میں):','واردات (په زرو منو):',[83,92,71,90,169,191])],exampleId=E66)]
s['equations']+=[eqn(215,'b',r'b=\dfrac{n\sum xy-\sum x\sum y}{n\sum x^2-\left(\sum x\right)^2}=\dfrac{9(424)}{9(160)}=7.1','b = (nΣxy − ΣxΣy)/(nΣx² − (Σx)²) = 9(424)/9(160) = 7.1',exampleId=E65),
 eqn(215,'a',r'a=\dfrac{\sum y}{n}-b\left(\dfrac{\sum x}{n}\right)=\dfrac{801}{9}=89','a = Σy/n − b(Σx/n) = 801/9 = 89',exampleId=E65)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(215,k) for k in ks])
s['flow']=[dict(type='table',index=0),P('c1','sol65'),dict(type='table',index=1),P('a1'),dict(type='equation',index=0),dict(type='equation',index=1),P('a2','a3','ex66','q66'),dict(type='table',index=2)]
s['sourceNote']='Printed page 205. The first table (years 1985–1993 and production) completes the data of Example 6.5 and is shown before the solution. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 216 (printed 206) ----------
s=page(216,U,'206','Example 6.6: solution · 6.1.5 Fitting of second degree parabola','مثال 6.6: حل · 6.1.5 دوسرے درجے کے قطع مکافی کی فٹنگ','بېلګه 6.6: حل · 6.1.5 د دویم درجې پیراپولا برابرول','ts-ls-3')
Flow(s)
head(s,'sol66','Solution:','حل:','حل:',exampleId=E66)
add(s,'a1','The equation of straight line is ŷ = a + bx, where','سیدھی لکیر کی مساوات ہے ŷ = a + bx، جہاں','د مستقیمې کرښې معادله ده ŷ = a + bx، چېرته چې',role='solution',exampleId=E66)
add(s,'a2','Thus the fitted least squares equation of straight line is ŷ = 116 + 11.3x.','اس طرح فٹ کی گئی کم از کم مربعات سیدھی لکیر کی مساوات ہے ŷ = 116 + 11.3x۔','په دې توګه برابره شوې د لږ تر لږه مربعاتو مستقیمې کرښې معادله ده ŷ = 116 + 11.3x.',role='solution',exampleId=E66)
add(s,'a3','Putting the values of x in this equation we get trend values which are given in the last column of the table.','اس مساوات میں x کی قدریں رکھنے سے ہمیں رجحان کی قدریں ملتی ہیں جو جدول کے آخری کالم میں دی گئی ہیں۔','پدې معادله کې د x ارزښتونه ایښودو سره موږ د تمایل ارزښتونه ترلاسه کوو چې د جدول په وروستي کالم کې ورکړل شوي دي.',role='solution',exampleId=E66)
head(s,'h615','6.1.5 Fitting of second degree parabola or quadratic trend by the method of least squares','6.1.5 کم از کم مربعات کے طریقے سے دوسرے درجے کے قطع مکافی یا دو درجی رجحان کی فٹنگ','6.1.5 د لږ تر لږه مربعاتو په طریقه د دویم درجې پیراپولا یا دوه‌درجي تمایل برابرول')
add(s,'t1','The equation of second degree parabola/quadratic trend is given by','دوسرے درجے کے قطع مکافی/دو درجی رجحان کی مساوات یوں دی جاتی ہے','د دویم درجې پیراپولا/دوه‌درجي تمایل معادله داسې ورکول کېږي')
add(s,'t2','Three normal equations for a, b, c respectively are;','a, b, c کے لیے بالترتیب تین معمول کی مساواتیں یہ ہیں؛','د a, b, c لپاره په ترتیب سره درې نورمال معادلې دا دي؛')
rows=[(1990,83,-5,-415,25,'59.5'),(1991,92,-3,-276,9,'82.1'),(1992,71,-1,-71,1,'104.7'),(1993,90,1,90,1,'127.3'),(1994,169,3,507,9,'149.9'),(1995,191,5,955,25,'172.5')]
s['tables']=[table('Example 6.6 solution table','مثال 6.6 کا حل: جدول','د بېلګې 6.6 د حل جدول',[c('Year','سال','کال'),c('y'),c('x'),c('xy'),c('x²'),c('Trend values ŷ = 116 + 11.3x','رجحان کی قدریں ŷ = 116 + 11.3x','د تمایل ارزښتونه ŷ = 116 + 11.3x')],[[c(str(r[0])),c(str(r[1])),c(str(r[2])),c(str(r[3])),c(str(r[4])),c(r[5])] for r in rows]+[[c('Total','میزان','ټولیز'),c('696'),c('0'),c('790'),c('70'),c('')]],exampleId=E66)]
s['equations']+=[eqn(216,'b',r'b=\dfrac{n\sum xy-\sum x\sum y}{n\sum x^2-\left(\sum x\right)^2}=\dfrac{6(790)}{6(70)}=11.3','b = (nΣxy − ΣxΣy)/(nΣx² − (Σx)²) = 6(790)/6(70) = 11.3',exampleId=E66),
 eqn(216,'a',r'a=\dfrac{\sum y}{n}-b\left(\dfrac{\sum x}{n}\right)=\dfrac{696}{6}=116','a = Σy/n − b(Σx/n) = 696/6 = 116',exampleId=E66),
 eqn(216,'q',r'\hat{y}=a+bx+cx^2','ŷ = a + bx + cx²'),
 eqn(216,'n1',N1[0],N1[1]),eqn(216,'n2',N2[0],N2[1]),eqn(216,'n3',N3[0],N3[1])]
P=lambda *ks:dict(type='paragraphs',ids=[pid(216,k) for k in ks])
s['flow']=[P('sol66'),dict(type='table',index=0),P('a1'),dict(type='equation',index=0),dict(type='equation',index=1),P('a2','a3','h615','t1'),dict(type='equation',index=2),P('t2'),dict(type='equation',index=3),dict(type='equation',index=4),dict(type='equation',index=5)]
s['sourceNote']='Printed page 206. In the solution table the last cell of the total row is empty. The three normal equations are printed with underlined slots labelled (i), (ii), (iii). A dark smear at the top-left corner is ignored. Header graphics and watermark excluded.'
s['vocabulary']={'parabola':dict(ur='قطع مکافی',ps='پیراپولا'),'quadratic trend':dict(ur='دو درجی رجحان',ps='دوه‌درجي تمایل')}
save(s)
# ---------- scan 217 (printed 207) ----------
s=page(217,U,'207','Example 6.7: second degree parabola (data, table, normal equations)','مثال 6.7: دوسرے درجے کا قطع مکافی (اعداد و شمار، جدول، معمول کی مساواتیں)','بېلګه 6.7: دویم درجې پیراپولا (معلومات، جدول، نورمال معادلې)','ts-quad-1')
Flow(s)
head(s,'ex67','Example: 6.7','مثال: 6.7','بېلګه: 6.7',exampleId=E67)
add(s,'q67','Fit a second degree parabola to the following data and find the trend values','درج ذیل اعداد و شمار پر دوسرے درجے کا قطع مکافی فٹ کریں اور رجحان کی قدریں معلوم کریں','پر لاندې معلوماتو دویم درجې پیراپولا برابره کړئ او د تمایل ارزښتونه ومومئ',role='question',exampleId=E67)
head(s,'sol67','Solution:','حل:','حل:',exampleId=E67)
add(s,'a1','The required equation to be fitted is ŷ = a + bx + cx²','فٹ کی جانے والی مطلوبہ مساوات ہے ŷ = a + bx + cx²','د برابرولو وړ اړینه معادله ده ŷ = a + bx + cx²',role='solution',exampleId=E67)
add(s,'a2','Three normal equation for a, b and c are;','a, b اور c کے لیے تین معمول کی مساواتیں یہ ہیں؛','د a, b او c لپاره درې نورمال معادلې دا دي؛',role='solution',exampleId=E67)
add(s,'a3','Putting values in above normal equations we have','اوپر دی گئی معمول کی مساواتوں میں قدریں رکھنے سے ہمیں ملتا ہے','په پورتنیو نورمالو معادلو کې ارزښتونه ایښودو سره موږ لرو',role='solution',exampleId=E67,sourceGap=dict(note='The working continues on the next page.'))
rows=[(2006,187,-3,9,-561,-27,1683,81,'192'),(2007,142,-2,4,-284,-8,568,16,'144'),(2008,133,-1,1,-133,-1,133,1,'120'),(2009,129,0,0,0,0,0,0,'119'),(2010,136,1,1,136,1,136,1,'144'),(2011,169,2,4,338,8,676,16,'192'),(2012,279,3,9,837,27,2511,81,'264')]
s['tables']=[table('Example 6.7: years and values','مثال 6.7: سال اور قدریں','بېلګه 6.7: کلونه او ارزښتونه',[c('Years:','سال:','کلونه:')]+[c(str(v)) for v in range(2006,2013)],[row('Values:','قدریں:','ارزښتونه:',[187,142,133,129,136,169,279])],exampleId=E67),
 table('Example 6.7 solution table','مثال 6.7 کا حل: جدول','د بېلګې 6.7 د حل جدول',[c('Year','سال','کال'),c('y'),c('x'),c('x²'),c('xy'),c('x³'),c('x²y'),c('x⁴'),c('Trend values ŷ = 119.9 + 11.89x + 11.99x²','رجحان کی قدریں ŷ = 119.9 + 11.89x + 11.99x²','د تمایل ارزښتونه ŷ = 119.9 + 11.89x + 11.99x²')],[[c(str(v)) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('1175'),c('0'),c('28'),c('333'),c('0'),c('5707'),c('196'),c('1175')]],exampleId=E67)]
s['equations']+=[eqn(217,'q',r'\hat{y}=a+bx+cx^2','ŷ = a + bx + cx²',exampleId=E67),
 eqn(217,'n1',N1[0],N1[1],exampleId=E67),eqn(217,'n2',N2[0],N2[1],exampleId=E67),eqn(217,'n3',N3[0],N3[1],exampleId=E67),
 eqn(217,'e4',r'1175=7a+28c\qquad\text{(4)}','1175 = 7a + 28c   (4)',exampleId=E67),
 eqn(217,'e5',r'333=28b\qquad\text{(5)}\qquad\Rightarrow\ b=\dfrac{333}{28}=11.89','333 = 28b   (5)   ⇒ b = 333/28 = 11.89',exampleId=E67),
 eqn(217,'e6',r'5707=28a+196c\qquad\text{(6)}','5707 = 28a + 196c   (6)',exampleId=E67)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(217,k) for k in ks])
s['flow']=[P('ex67','q67'),dict(type='table',index=0),P('sol67','a1'),dict(type='equation',index=0),P('a2'),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='table',index=1),P('a3'),dict(type='equation',index=4),dict(type='equation',index=5),dict(type='equation',index=6)]
s['sourceNote']='Printed page 207. In the printed text b = 333/28 = 11.89 stands beside equation (5). The equations (4)–(6) are labelled with underlined slots. A black dot near the right margin of the table is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 218 (printed 208) ----------
s=page(218,U,'208','Example 6.7 (solving for a and c) · Example 6.8: second degree parabola (start)','مثال 6.7 (a اور c کا حل) · مثال 6.8: دوسرے درجے کا قطع مکافی (آغاز)','بېلګه 6.7 (د a او c حل) · بېلګه 6.8: دویم درجې پیراپولا (پیل)','ts-quad-2')
Flow(s)
add(s,'a1','Multiply equation (4) by 4 and subtract it from equation (6)','مساوات (4) کو 4 سے ضرب دیں اور اسے مساوات (6) سے منہا کریں','معادله (4) په 4 ضرب کړئ او له معادلې (6) څخه یې تفریق کړئ',role='solution',exampleId=E67)
add(s,'a2','Put this value of c in equation (4) we have','c کی یہ قدر مساوات (4) میں رکھنے سے ہمیں ملتا ہے','د c دا ارزښت په معادله (4) کې ایښودو سره موږ لرو',role='solution',exampleId=E67)
add(s,'a3','Thus the required fitted equation of second degree parabola is','اس طرح دوسرے درجے کے قطع مکافی کی مطلوبہ فٹ کی گئی مساوات ہے','په دې توګه د دویم درجې پیراپولا اړینه برابره شوې معادله ده',role='solution',exampleId=E67)
add(s,'a4','The trend values are given in the last column which is obtained by putting the values of x in the above equation.','رجحان کی قدریں آخری کالم میں دی گئی ہیں جو اوپر دی گئی مساوات میں x کی قدریں رکھنے سے حاصل ہوتی ہیں۔','د تمایل ارزښتونه په وروستي کالم کې ورکړل شوي دي چې د پورتنۍ معادلې په x ارزښتونو ایښودو سره ترلاسه کېږي.',role='solution',exampleId=E67)
head(s,'ex68','Example: 6.8','مثال: 6.8','بېلګه: 6.8',exampleId=E68)
add(s,'q68','Fit a second degree parabola to the following data and find the trend values:','درج ذیل اعداد و شمار پر دوسرے درجے کا قطع مکافی فٹ کریں اور رجحان کی قدریں معلوم کریں:','پر لاندې معلوماتو دویم درجې پیراپولا برابره کړئ او د تمایل ارزښتونه ومومئ:',role='question',exampleId=E68)
head(s,'sol68','Solution:','حل:','حل:',exampleId=E68)
add(s,'b1','Required equation of the second degree parabola is','دوسرے درجے کے قطع مکافی کی مطلوبہ مساوات ہے','د دویم درجې پیراپولا اړینه معادله ده',role='solution',exampleId=E68)
add(s,'b2','Three normal equations are','تین معمول کی مساواتیں یہ ہیں','درې نورمال معادلې دا دي',role='solution',exampleId=E68,sourceGap=dict(note='The list of normal equations continues on the next page; only equation (i) is printed here.'))
s['tables']=[table('Example 6.8: year and y','مثال 6.8: سال اور y','بېلګه 6.8: کال او y',[c('Year','سال','کال')]+[c(v) for v in ['1980','1981','982','983','1984','1985','986','1987']],[row('y','y','y',[100,87,96,102,139,210,289,307])],exampleId=E68)]
s['equations']+=[eqn(218,'m1',r'\begin{aligned}5707&=28a+196c\\ 4700&=28a+112c\\ 1007&=84c\end{aligned}\qquad\text{or}\qquad c=\dfrac{1007}{84}=11.99','5707 = 28a + 196c; 4700 = 28a + 112c; subtract: 1007 = 84c or c = 1007/84 = 11.99   [4 × (4) is printed as 4700 = 28a + 112c]',exampleId=E67),
 eqn(218,'m2',r'\begin{aligned}1175&=7a+28(11.99)\\ &=7a+335.72\\ 1175-335.72&=7a\\ 839.28&=7a\end{aligned}\qquad\text{or}\qquad a=\dfrac{839.28}{7}=119.9','1175 = 7a + 28(11.99) = 7a + 335.72; 1175 − 335.72 = 7a; 839.28 = 7a or a = 839.28/7 = 119.9',exampleId=E67),
 eqn(218,'m3',r'\hat{y}=119.9+11.89x+11.99x^2','ŷ = 119.9 + 11.89x + 11.99x²',exampleId=E67),
 eqn(218,'q',r'\hat{y}=a+bx+cx^2','ŷ = a + bx + cx²',exampleId=E68),
 eqn(218,'n1',N1[0],N1[1],exampleId=E68)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(218,k) for k in ks])
s['flow']=[P('a1'),dict(type='equation',index=0),P('a2'),dict(type='equation',index=1),P('a3'),dict(type='equation',index=2),P('a4','ex68','q68'),dict(type='table',index=0),P('sol68','b1'),dict(type='equation',index=3),P('b2'),dict(type='equation',index=4)]
s['sourceNote']='Printed page 208. The subtraction of equations (4) and (6) and the substitution for a are printed as stacked lines and are each kept as one equation. In the question row of Example 6.8 the years 1982, 1983 and 1986 are printed as "982", "983" and "986" (leading 1 missing); kept as printed. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
