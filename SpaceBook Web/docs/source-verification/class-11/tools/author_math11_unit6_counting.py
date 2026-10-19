"""Step-by-step SpaceBook solutions for Class 11 Mathematics, Exercises 6.1-6.3
(factorials, permutations, combinations). Every count is checked with Python."""
import sys, os
from math import factorial as f, perm as P, comb as C
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math11_answer_authoring import Author, step, S
from math11_phrases import make_put

A = Author(6)
put, flush = make_put(A)
def T(en, ur, ps, m=None): return step(en, ur, ps, m)
def KEY(en, ur, ps): return T('Note on the printed answer key: ' + en, 'مطبوعہ جوابی کنجی کے بارے میں: ' + ur, 'د چاپ شوې ځوابي کیلي په اړه: ' + ps)
QED = T('Hence proved.', 'ثابت ہوا۔', 'ثابت شو.')
EXPF = lambda m: T('Expand the factorials and cancel common factors.', 'فیکٹوریل کھول کر مشترک اجزا منسوخ کریں۔', 'فکتوریلونه پراخ کړئ او ګډ عاملونه لرې کړئ.', m)
FPC = lambda m: T('Fundamental principle of counting: multiply the number of choices for each place.', 'گنتی کا بنیادی اصول: ہر جگہ کے انتخاب کی تعداد کو ضرب دیں۔', 'د شمېرنې بنسټیز اصل: د هر ځای د انتخابونو شمېر سره ضرب کړئ.', m)
NPR = lambda m: T('Use ${}^nP_r=\\dfrac{n!}{(n-r)!}$.', '${}^nP_r=\\dfrac{n!}{(n-r)!}$ استعمال کریں۔', '${}^nP_r=\\dfrac{n!}{(n-r)!}$ وکاروئ.', m)
NCR = lambda m: T('Use ${}^nC_r=\\dfrac{n!}{r!\\,(n-r)!}$.', '${}^nC_r=\\dfrac{n!}{r!\\,(n-r)!}$ استعمال کریں۔', '${}^nC_r=\\dfrac{n!}{r!\\,(n-r)!}$ وکاروئ.', m)
REP = lambda m: T('Permutations of $n$ objects with repeated letters: $\\dfrac{n!}{p!\\,q!\\cdots}$.', 'دہرائے گئے حروف والی $n$ اشیا کی ترتیبیں: $\\dfrac{n!}{p!\\,q!\\cdots}$۔', 'د تکرار شویو تورو لرونکو $n$ شیانو ترتیبونه: $\\dfrac{n!}{p!\\,q!\\cdots}$.', m)
QUAD = lambda m: T('Solve the resulting equation and keep only the admissible (positive integer) value.', 'حاصل مساوات حل کریں اور صرف قابلِ قبول (مثبت صحیح) قیمت رکھیں۔', 'ترلاسه شوې معادله حل کړئ او یوازې د منلو وړ (مثبت صحیح) ارزښت وساتئ.', m)
ANS = lambda m: T('Answer.', 'جواب۔', 'ځواب.', m)

# ───────────── 6.1 ─────────────
assert f(10)//(f(3)*f(3)*f(4)) == 4200 and f(10)//f(5)**2 == 252
put('6.1', 1, '(i)', '$4200$', [EXPF(r'\frac{10!}{3!\,3!\,4!}=\frac{3628800}{6\cdot6\cdot24}=\frac{3628800}{864}=4200')])
put('6.1', 1, '(ii)', r'$\frac5{16}$', [EXPF(r'\frac{3!+4!}{5!-4!}=\frac{6+24}{120-24}=\frac{30}{96}=\frac5{16}')])
put('6.1', 1, '(iii)', r'$\frac1{n(n+1)}$', [EXPF(r'\frac{(n-1)!}{(n+1)!}=\frac{(n-1)!}{(n+1)\,n\,(n-1)!}=\frac1{n(n+1)}')])
put('6.1', 1, '(iv)', '$252$', [EXPF(r'\frac{10!}{(5!)^2}=\frac{10\cdot9\cdot8\cdot7\cdot6}{5!}=\frac{30240}{120}=252')])
WF = lambda m: T('Complete the product to a factorial and divide by the missing factors.', 'حاصلِ ضرب کو فیکٹوریل تک مکمل کریں اور زائد اجزا سے تقسیم کریں۔', 'ضرب تر فکتوریل پورې بشپړ کړئ او په اضافي عاملونو یې وویشئ.', m)
put('6.1', 2, '(i)', r'$\frac{19!}{13!}$', [WF(r'19\cdot18\cdot17\cdot16\cdot15\cdot14=\frac{19\cdot18\cdots14\cdot13!}{13!}=\frac{19!}{13!}')])
put('6.1', 2, '(ii)', r'$2^6\cdot6!$', [WF(r'2\cdot4\cdot6\cdot8\cdot10\cdot12=2^6(1\cdot2\cdot3\cdot4\cdot5\cdot6)=2^6\cdot6!')])
put('6.1', 2, '(iii)', r'$\frac{(n+1)!}{(n-2)!}$', [WF(r'n(n^2-1)=(n+1)\,n\,(n-1)=\frac{(n+1)!}{(n-2)!}')])
put('6.1', 2, '(iv)', r'$\frac{(n+2)!}{3\,(n-1)!}$', [WF(r'\frac{n(n+1)(n+2)}3=\frac{(n+2)!}{3\,(n-1)!}')])
assert 8*7 + 2*8 + 3 == 75
put('6.1', 3, '(i)', 'Proved (see the steps).', [T('Write every fraction with the common denominator $8!$.', 'ہر کسر کو مشترک مخرج $8!$ پر لکھیں۔', 'هر کسر د ګډ مخرج $8!$ پر ولیکئ.', r'\frac1{6!}=\frac{8\cdot7}{8!},\quad\frac2{7!}=\frac{2\cdot8}{8!},\quad\frac3{8!}'),
    T('Add the numerators.', 'شمار کنندے جمع کریں۔', 'صورتونه جمع کړئ.', r'\frac{56+16+3}{8!}=\frac{75}{8!}'), QED])
n = S.Symbol('n', positive=True, integer=True)
assert S.expand((n+5)*(n+4)) == n**2 + 9*n + 20
put('6.1', 3, '(ii)', 'Proved (see the steps).', [EXPF(r'\frac{(n+5)!}{(n+3)!}=\frac{(n+5)(n+4)(n+3)!}{(n+3)!}=(n+5)(n+4)'), T('Multiply out.', 'ضرب کھولیں۔', 'ضرب پراخ کړئ.', r'(n+5)(n+4)=n^2+9n+20'), QED])
assert S.solve(n*(n-4)-12, n) == [6]
put('6.1', 4, '(i)', '$n=6$', [EXPF(r'\frac{n\cdot n!}{(n-5)!}=\frac{12\cdot n!}{(n-4)(n-5)!}\Rightarrow n=\frac{12}{n-4}'),
    QUAD(r'n(n-4)=12\Rightarrow n^2-4n-12=0\Rightarrow(n-6)(n+2)=0\Rightarrow n=6\ (n=-2\text{ rejected})')])
put('6.1', 4, '(ii)', '$n=9$', [EXPF(r'\frac{n!}{(n-4)!}\div\frac{(n-1)!}{(n-4)!}=\frac{n!}{(n-1)!}=n'), ANS(r'n:1=9:1\Rightarrow n=9')])
put('6.1', 5, '(i)', 'Proved (see the steps).', [T('Separate the even and odd factors of $(2n)!$.', '$(2n)!$ کے جفت اور طاق اجزا الگ کریں۔', 'د $(2n)!$ جفت او طاق عاملونه جلا کړئ.', r'(2n)!=[2\cdot4\cdot6\cdots2n]\,[1\cdot3\cdot5\cdots(2n-1)]'),
    T('Take a factor 2 out of each even number.', 'ہر جفت عدد سے 2 کا جز باہر نکالیں۔', 'له هر جفت عدد نه د 2 عامل بهر کړئ.', r'2\cdot4\cdots2n=2^n(1\cdot2\cdots n)=2^n\,n!'),
    T('Divide by $n!$.', '$n!$ سے تقسیم کریں۔', 'په $n!$ یې وویشئ.', r'\frac{(2n)!}{n!}=2^n\,(1\cdot3\cdot5\cdots(2n-1))'), QED])
put('6.1', 5, '(ii)', 'Proved (see the steps).', [T('Use part (i) and $(2n+1)!=(2n+1)\\,(2n)!$.', 'حصہ (i) اور $(2n+1)!=(2n+1)\\,(2n)!$ استعمال کریں۔', '(i) برخه او $(2n+1)!=(2n+1)\\,(2n)!$ وکاروئ.', r'\frac{(2n+1)!}{n!}=(2n+1)\frac{(2n)!}{n!}=2^n(1\cdot3\cdots(2n-1))(2n+1)'), QED])

# ───────────── 6.2 ─────────────
assert (P(6, 6), P(20, 2), P(16, 3)) == (720, 380, 3360)
put('6.2', 1, '(i)', '$720$', [NPR(r'{}^6P_6=\frac{6!}{0!}=720')])
put('6.2', 1, '(ii)', '$380$', [NPR(r'{}^{20}P_2=20\cdot19=380')])
put('6.2', 1, '(iii)', '$3360$', [NPR(r'{}^{16}P_3=16\cdot15\cdot14=3360')])
assert P(11, 5) == 56*P(11, 3) and P(9, 5) == 9*P(8, 4) and P(25, 2) == 600
put('6.2', 2, '(i)', '$n=11$', [NPR(r'{}^nP_5={}^nP_3\,(n-3)(n-4)'), QUAD(r'(n-3)(n-4)=56=8\cdot7\Rightarrow n-3=8\Rightarrow n=11')])
put('6.2', 2, '(ii)', '$n=9$', [NPR(r'{}^nP_5=n(n-1)(n-2)(n-3)(n-4)=n\cdot{}^{n-1}P_4'), ANS(r'n\cdot{}^{n-1}P_4=9\cdot{}^{n-1}P_4\Rightarrow n=9')])
put('6.2', 2, '(iii)', '$n=5$', [NPR(r'{}^{n^2}P_2=n^2(n^2-1)=600'), QUAD(r'(n^2)^2-n^2-600=0\Rightarrow(n^2-25)(n^2+24)=0\Rightarrow n^2=25\Rightarrow n=5')])
put('6.2', 3, '(i)', 'Proved (see the steps).', [FPC(r'\text{1st place: }n\text{ choices; the other }r-1\text{ places are filled from the remaining }n-1\text{ objects in }{}^{n-1}P_{r-1}\text{ ways}'),
    ANS(r'{}^nP_r=n\cdot{}^{n-1}P_{r-1}'), QED])
put('6.2', 3, '(ii)', 'Proved (see the steps).', [T('Fix one particular object $x$. Arrangements of $r$ objects either omit $x$ or contain it.', 'ایک خاص شے $x$ مقرر کریں۔ $r$ اشیا کی ترتیبوں میں یا $x$ شامل نہیں یا شامل ہے۔', 'یو ځانګړی شی $x$ وټاکئ. د $r$ شیانو ترتیبونه یا $x$ نه لري یا یې لري.', r'\text{without }x:\ {}^{n-1}P_r'),
    FPC(r'\text{with }x:\ x\text{ can take any of the }r\text{ places, the rest in }{}^{n-1}P_{r-1}\text{ ways}\Rightarrow r\cdot{}^{n-1}P_{r-1}'),
    ANS(r'{}^nP_r={}^{n-1}P_r+r\cdot{}^{n-1}P_{r-1}'), QED])
put('6.2', 4, '', '$40320$', [NPR(r'{}^8P_8=8!=40320')])
put('6.2', 5, '', '$5040$', [T('"Fasting" has 7 different letters.', '"Fasting" میں 7 مختلف حروف ہیں۔', '"Fasting" کې 7 بېلابېل توري دي.', r'7!=5040')])
assert P(5, 4) == 120 and 2*P(4, 3) == 48
put('6.2', 6, '', '$120$ numbers; $48$ of them are even', [NPR(r'{}^5P_4=5\cdot4\cdot3\cdot2=120'), FPC(r'\text{even: units digit }2\text{ or }4\ (2\text{ ways}),\ \text{other 3 places }{}^4P_3=24\Rightarrow2\cdot24=48')])
put('6.2', 7, '(i)', '$125$', [FPC(r'5\cdot5\cdot5=125')])
put('6.2', 7, '(ii)', '$60$', [FPC(r'5\cdot4\cdot3=60')])
assert f(4)*f(5) == 2880
put('6.2', 8, '', '$2880$', [T('"equation" has 8 different letters: 5 vowels (e, u, a, i, o) and 3 consonants.', '"equation" میں 8 مختلف حروف ہیں: 5 حروفِ علت (e, u, a, i, o) اور 3 حروفِ صحیح۔', '"equation" کې 8 بېلابېل توري دي: 5 غږیز (e, u, a, i, o) او 3 بې غږه.'),
    FPC(r'\text{vowels as one block: }4\text{ units}\Rightarrow4!;\ \text{vowels inside the block: }5!\Rightarrow4!\cdot5!=24\cdot120=2880')])
assert sum(P(6, r) for r in range(1, 7)) == 1956
put('6.2', 9, '', '$1956$', [NPR(r'\sum_{r=1}^6{}^6P_r=6+30+120+360+720+720=1956')])
assert P(8, 5) == 6720 and 7*2*P(6, 3) == 1680
put('6.2', 10, '(i)', '$1680$', [T('Choose two adjacent seats for the pair: 7 pairs of neighbouring seats, and the two students can swap.', 'جوڑے کے لیے دو ساتھ والی نشستیں چنیں: 7 جوڑیاں، اور دونوں طالب علم جگہ بدل سکتے ہیں۔', 'د جوړې لپاره دوه څنګ پر څنګ څوکۍ وټاکئ: 7 جوړې، او دواړه زده کوونکي ځای بدلولی شي.', r'7\times2=14'),
    FPC(r'\text{other 3 students in the remaining 6 seats: }{}^6P_3=120\Rightarrow14\times120=1680'),
    KEY('it prints 3360. Its answer to (ii), 5040, equals $6720-1680$, which confirms 1680 here.', 'اس میں 3360 چھپا ہے۔ اس کا (ii) کا جواب 5040 یعنی $6720-1680$ ہے، جو یہاں 1680 کی تصدیق کرتا ہے۔', 'په کې 3360 چاپ شوی. د (ii) ځواب یې 5040 دی چې $6720-1680$ کېږي، او دا دلته 1680 تاییدوي.')])
put('6.2', 10, '(ii)', '$5040$', [NPR(r'\text{all seatings: }{}^8P_5=6720'), ANS(r'\text{not together}=6720-1680=5040')])
assert 5*5 + 5*5*4 == 125
put('6.2', 11, '', '$125$', [FPC(r'\text{2-digit: first digit non-zero }(5),\ \text{second }(5)\Rightarrow25'), FPC(r'\text{3-digit: }5\cdot5\cdot4=100'), ANS(r'25+100=125')])
assert (f(8)//f(3), f(10)//(f(2)*f(2)*f(3)), f(10)//(f(3)*f(3)*f(2)), f(6)//(f(2)*f(2))) == (6720, 151200, 50400, 180)
put('6.2', 12, '(i)', '$6720$', [REP(r'\text{BOOKWORM: 8 letters, O three times}\Rightarrow\frac{8!}{3!}=6720')])
put('6.2', 12, '(ii)', '$151200$', [REP(r'\text{BOOKKEEPER: 10 letters, O}\times2,\ \text{K}\times2,\ \text{E}\times3\Rightarrow\frac{10!}{2!\,2!\,3!}=151200')])
put('6.2', 12, '(iii)', '$50400$', [REP(r'\text{ABBOTTABAD: 10 letters, A}\times3,\ \text{B}\times3,\ \text{T}\times2\Rightarrow\frac{10!}{3!\,3!\,2!}=50400')])
put('6.2', 12, '(iv)', '$180$', [REP(r'\text{LETTER: 6 letters, E}\times2,\ \text{T}\times2\Rightarrow\frac{6!}{2!\,2!}=180')])
tot = f(10)//(f(4)*f(2)*f(2))
vals = [f(9)//(f(3)*f(2)*f(2)), f(8)//(f(3)*f(2)), f(8)//(f(2)*f(2)*f(2))]
ll = f(9)//(f(4)*f(2))
assert (tot, *vals, tot-vals[0], ll, tot-ll) == (37800, 15120, 3360, 5040, 22680, 7560, 30240)
base = REP(r'\text{EXCELLENCE: 10 letters, E}\times4,\ \text{C}\times2,\ \text{L}\times2\Rightarrow\frac{10!}{4!\,2!\,2!}=37800')
put('6.2', 13, '(total)', '$37800$', [base])
put('6.2', 13, '(i)', '$15120$', [REP(r'\text{fix E first: 9 letters left, E}\times3,\ \text{C}\times2,\ \text{L}\times2\Rightarrow\frac{9!}{3!\,2!\,2!}=15120')])
put('6.2', 13, '(ii)', '$3360$', [REP(r'\text{fix E first and C last: 8 left, E}\times3,\ \text{L}\times2\Rightarrow\frac{8!}{3!\,2!}=3360')])
put('6.2', 13, '(iii)', '$5040$', [REP(r'\text{E at both ends: 8 left, E}\times2,\ \text{C}\times2,\ \text{L}\times2\Rightarrow\frac{8!}{2!\,2!\,2!}=5040')])
put('6.2', 13, '(iv)', '$22680$', [ANS(r'37800-15120=22680')])
put('6.2', 13, '(v)', '$7560$', [REP(r'\text{treat LL as one letter: 9 units, E}\times4,\ \text{C}\times2\Rightarrow\frac{9!}{4!\,2!}=7560')])
put('6.2', 13, '(vi)', '$30240$', [ANS(r'37800-7560=30240')])
put('6.2', 14, '', '$12$', [T('Circular arrangement of 5 objects that can also be turned over (a ring): $\\dfrac{(n-1)!}2$.', '5 اشیا کی دائروی ترتیب جو الٹی بھی کی جا سکے (چھلا): $\\dfrac{(n-1)!}2$۔', 'د 5 شیانو دایروي ترتیب چې اړول کېدای شي (کړۍ): $\\dfrac{(n-1)!}2$.', r'\frac{4!}2=12')])
put('6.2', 15, '', '$240$', [T('Treat the two particular persons as one unit: 6 units round a table.', 'دونوں خاص افراد کو ایک اکائی سمجھیں: میز کے گرد 6 اکائیاں۔', 'دواړه ځانګړي کسان یو واحد وګڼئ: د مېز شاوخوا 6 واحدونه.', r'(6-1)!=120'),
    FPC(r'\text{the two persons can change places: }120\times2=240'),
    KEY('it prints 120, which leaves out the 2 ways the pair can sit; the full count is 240.', 'اس میں 120 چھپا ہے جس میں جوڑے کے بیٹھنے کے 2 طریقے شامل نہیں؛ مکمل تعداد 240 ہے۔', 'په کې 120 چاپ شوی چې د جوړې د کښېناستو 2 لارې نه دي شاملې؛ بشپړ شمېر 240 دی.')])

# ───────────── 6.3 ─────────────
assert C(9, 2) == 36 and C(9, 4) == 6*C(7, 2) and C(16, 2) == 30*C(4, 3) and C(25, 2) == 30*C(5, 3)
put('6.3', 1, '(i)', '$n=9$', [NCR(r'\frac{n(n-1)}2=36\Rightarrow n^2-n-72=0'), QUAD(r'(n-9)(n+8)=0\Rightarrow n=9')])
put('6.3', 1, '(ii)', '$n=8$', [NCR(r'\frac{(n+1)n(n-1)(n-2)}{24}=6\cdot\frac{(n-1)(n-2)}2'), QUAD(r'\frac{(n+1)n}{24}=3\Rightarrow n^2+n-72=0\Rightarrow(n+9)(n-8)=0\Rightarrow n=8')])
put('6.3', 1, '(iii)', '$n=4$ or $n=5$', [NCR(r'\frac{n^2(n^2-1)}2=30\cdot\frac{n(n-1)(n-2)}6'), T('Cancel $n(n-1)$ (non-zero).', '$n(n-1)$ منسوخ کریں (غیر صفر)۔', '$n(n-1)$ لرې کړئ (صفر نه دی).', r'\frac{n(n+1)}2=5(n-2)'),
    QUAD(r'n^2-9n+20=0\Rightarrow(n-4)(n-5)=0\Rightarrow n=4,5')])
assert P(7, 4) == 840 and C(7, 4) == 35
put('6.3', 2, '', '$n=7,\\ r=4$', [T('Use ${}^nP_r=r!\\,{}^nC_r$.', '${}^nP_r=r!\\,{}^nC_r$ استعمال کریں۔', '${}^nP_r=r!\\,{}^nC_r$ وکاروئ.', r'r!=\frac{840}{35}=24\Rightarrow r=4'),
    NPR(r'n(n-1)(n-2)(n-3)=840=7\cdot6\cdot5\cdot4\Rightarrow n=7')])
assert C(10, 3)*3 == 36*C(5, 2)
put('6.3', 3, '', '$n=5$', [NCR(r'\frac{{}^{2n}C_3}{{}^nC_2}=\frac{2n(2n-1)(2n-2)/6}{n(n-1)/2}=\frac{4(2n-1)}3'), QUAD(r'\frac{4(2n-1)}3=\frac{36}3=12\Rightarrow2n-1=9\Rightarrow n=5')])
put('6.3', 4, '(i)', 'Proved (see the steps).', [NCR(r'{}^{n-1}C_r+{}^{n-1}C_{r-1}=\frac{(n-1)!}{r!\,(n-1-r)!}+\frac{(n-1)!}{(r-1)!\,(n-r)!}'),
    T('Take the common denominator $r!\\,(n-r)!$.', 'مشترک مخرج $r!\\,(n-r)!$ لیں۔', 'ګډ مخرج $r!\\,(n-r)!$ واخلئ.', r'=\frac{(n-1)!\,[(n-r)+r]}{r!\,(n-r)!}=\frac{n!}{r!\,(n-r)!}={}^nC_r'), QED])
put('6.3', 4, '(ii)', 'Proved (see the steps).', [NCR(r'r\cdot{}^nC_r=r\cdot\frac{n!}{r!\,(n-r)!}=\frac{n\,(n-1)!}{(r-1)!\,(n-r)!}'),
    T('Recognise ${}^{n-1}C_{r-1}$.', '${}^{n-1}C_{r-1}$ پہچانیں۔', '${}^{n-1}C_{r-1}$ وپېژنئ.', r'=n\cdot\frac{(n-1)!}{(r-1)!\,((n-1)-(r-1))!}=n\cdot{}^{n-1}C_{r-1}'), QED])
put('6.3', 5, '(i)', '$66$', [T('A line is fixed by any 2 of the points.', 'کوئی بھی 2 نقاط ایک خط متعین کرتے ہیں۔', 'هر 2 ټکي یوه کرښه ټاکي.', r'{}^{12}C_2=\frac{12\cdot11}2=66')])
put('6.3', 5, '(ii)', '$220$', [T('A triangle is fixed by any 3 of the points (no three collinear).', 'کوئی بھی 3 نقاط (جو ہم خط نہ ہوں) ایک مثلث متعین کرتے ہیں۔', 'هر 3 ټکي (چې په یوه کرښه نه وي) یو درې ګونی ټاکي.', r'{}^{12}C_3=\frac{12\cdot11\cdot10}{6}=220')])
put('6.3', 6, '', '$9$', [T('Segments joining any two vertices, minus the 6 sides.', 'کوئی بھی دو راسوں کو ملانے والے قطعات، منہا 6 اضلاع۔', 'هغه برخې چې هر دوه رأسونه سره نښلوي، منفي 6 ضلعې.', r'{}^6C_2-6=15-6=9')])
put('6.3', 7, '', '$190$', [T('Each handshake is a pair of people.', 'ہر مصافحہ دو افراد کا جوڑا ہے۔', 'هر لاس ورکول د دوو کسانو جوړه ده.', r'{}^{20}C_2=\frac{20\cdot19}2=190')])
put('6.3', 8, '', '$35$', [T('The first 3 are fixed; choose the other 4 from the remaining 7.', 'پہلے 3 لازمی ہیں؛ باقی 4 بقیہ 7 میں سے چنیں۔', 'لومړۍ 3 لازمي دي؛ پاتې 4 له پاتې 7 نه وټاکئ.', r'{}^7C_4=35')])
assert C(6, 4)*C(7, 4) == 525 and C(13, 8) == 1287 and C(13, 8) - 6*C(7, 7) == 1281 and C(6, 5)*C(7, 3) + C(6, 6)*C(7, 2) == 231
put('6.3', 9, '(i)', '$525$', [FPC(r'{}^6C_4\cdot{}^7C_4=15\cdot35=525')])
put('6.3', 9, '(ii)', '$1287$', [NCR(r'\text{all committees: }{}^{13}C_8=1287'), T('With only 6 women, every 8-person committee already has at least 2 men.', 'صرف 6 خواتین ہیں، اس لیے ہر 8 رکنی کمیٹی میں کم از کم 2 مرد ہوں گے۔', 'یوازې 6 ښځې دي، نو په هره 8 کسیزه کمېټه کې لږ تر لږه 2 نارینه وي.', r'\Rightarrow1287')])
put('6.3', 9, '(iii)', '$1281$', [T('Subtract committees with fewer than 2 women (0 women is impossible; exactly 1 woman: ${}^6C_1\\cdot{}^7C_7$).', 'جن کمیٹیوں میں 2 سے کم خواتین ہوں انہیں منہا کریں (0 خاتون ناممکن؛ صرف 1 خاتون: ${}^6C_1\\cdot{}^7C_7$)۔', 'هغه کمېټې کمې کړئ چې له 2 کمې ښځې لري (0 ښځه ناشونې؛ یوازې 1 ښځه: ${}^6C_1\\cdot{}^7C_7$).', r'1287-6\cdot1=1281')])
put('6.3', 9, '(iv)', '$231$', [FPC(r'(5W,3M):\ {}^6C_5\cdot{}^7C_3=6\cdot35=210;\quad(6W,2M):\ {}^6C_6\cdot{}^7C_2=21'), ANS(r'210+21=231')])

flush()
A.save(['6.1', '6.2', '6.3'], list(range(170, 190)) + [416, 417])
