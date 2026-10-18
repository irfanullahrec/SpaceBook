"""PDF168 printed 327–328: Answers — Exercise 6 (6.9–6.28); Exercise 7; Exercise 8 (8.1–8.2)."""
from class12_statistics_common import Builder, save

L = lambda s: (s,) * 3
a = Builder()
a.group('lines', [
    L('6.9 (i) $\\overline{X}=5.9$ (ii) $s^2=5.8178$ (iii) $s_{\\overline{x}}=0.7667$'), L('6.10 (i) $E(\\overline{X})=\\mu=14$ (ii) $E(s^2)=\\sigma^2=9.333$'),
    L('6.14 $(9.84<\\mu<12.16)$'), L('6.15 $(0.774<\\mu<0.826)$'), L('6.16 $(788.24<\\mu<811.76)$'), L('6.17 $(-2.27<\\mu<2.67)$'),
    L('6.18 $(63.412<\\mu<64.588)$'), L('6.19 $(31.59<\\mu<54.93)$'), L('6.20 $(2.4<\\mu_1-\\mu_2<7.6)$'), L('6.21 $(0.55<\\mu_2-\\mu_1<1.25)$'),
    L('6.23 $(4.3371<\\mu<4.4229)$'), L('6.24 $(33.52<\\mu<35.28)$'), L('6.25 $(-15.3<\\mu_A-\\mu_B<1.3)$'), L('6.26 $(0.45<P<0.75)$'),
    L('6.27 $(0.62<P<0.74)$'), L('6.28 $(-0.206<P_1-P_2<-0.120)$'),
])
ans6 = a.build('stat12-answers-ex6-b', 'Answers — Exercise 6 (6.9–6.28)', 'جوابات — مشق 6 (6.9–6.28)', 'ځوابونه — تمرین 6 (6.9–6.28)', 168, [327])

R = lambda n, s, v, d: (f'{n} ${s}={v}$, {d[0]} $H_0$', f'{n} ${s}={v}$، $H_0$ {d[1]}', f'{n} ${s}={v}$، $H_0$ {d[2]}')
REJ = ('reject', 'رد کریں', 'رد کړئ'); ACC = ('accept', 'قبول کریں', 'ومنئ')
b = Builder()
b.h('Exercise-7', 'مشق-7', 'تمرین-7')
b.group('lines', [
    L('7.1 (i) F (ii) T (iii) F (iv) F (v) T (vi) T (vii) T (viii) F (ix) T (x) F'),
    ('7.2 (i) assertion (ii) null (iii) alternative (iv) composite (v) first, second (vi) level of significance (vii) 0, 1 (viii) rejection region (ix) rule (x) degrees of freedom',
     '7.2 (i) دعویٰ (ii) صفری (iii) متبادل (iv) مرکب (v) پہلی، دوسری (vi) معنویت کی سطح (vii) 0، 1 (viii) رد کا علاقہ (ix) قاعدہ (x) درجاتِ آزادی',
     '7.2 (i) ادعا (ii) صفري (iii) بدیله (iv) مرکبه (v) لومړۍ، دویمه (vi) د معنی‌داریت کچه (vii) 0، 1 (viii) د ردولو سیمه (ix) قاعده (x) د ازادۍ درجې'),
    L('7.3 (i) c (ii) a (iii) b (iv) a (v) c (vi) a (vii) c (viii) b (ix) b (x) b'),
    R('7.10', 'z', '2.61', REJ), R('7.11', 'z', '2.4', REJ), R('7.12', 'z', '-2.88', REJ), R('7.13', 'z', '2.33', REJ), R('7.14', 'z', '-1.93', REJ),
    R('7.16', 't', '0.316', ACC), R('7.17', 't', '1.844', ACC), R('7.19', 'z', '4.22', REJ), R('7.20', 'z', '-1.334', ACC),
    R('7.22', 't', '3.33', REJ), R('7.23', 't', '3.05', REJ), R('7.25', 'z', '2.19', REJ), R('7.26', 'z', '-0.73', ACC),
    R('7.27', 'z', '-2.1004', ACC), R('7.29', 'z', '-3.1623', REJ), R('7.30', 'z', '9.6825', REJ),
])
ans7 = b.build('stat12-answers-ex7', 'Answers — Exercise 7', 'جوابات — مشق 7', 'ځوابونه — تمرین 7', 168, [327, 328])

c = Builder()
c.h('Exercise-8', 'مشق-8', 'تمرین-8')
c.group('lines', [
    L('8.1 (i) F (ii) T (iii) T (iv) F (v) T (vi) F (vii) T (viii) F (ix) T (x) F'),
    ('8.2 (i) dichotomous (ii) order (iii) second (iv) zero (v) $\\frac{(A)(B)}{n}$ (vi) zero (vii) not same (viii) −1 to +1 (ix) equal (x) 20',
     '8.2 (i) دو حصوں میں منقسم (ii) درجہ (iii) دوسرے (iv) صفر (v) $\\frac{(A)(B)}{n}$ (vi) صفر (vii) ایک جیسے نہیں (viii) −1 سے +1 (ix) برابر (x) 20',
     '8.2 (i) دوه‌ګونی (ii) درجه (iii) دویمې (iv) صفر (v) $\\frac{(A)(B)}{n}$ (vi) صفر (vii) یو شان نه (viii) له −1 تر +1 (ix) برابر (x) 20'),
])
ans8 = c.build('stat12-answers-ex8-a', 'Answers — Exercise 8 (8.1–8.2)', 'جوابات — مشق 8 (8.1–8.2)', 'ځوابونه — تمرین 8 (8.1–8.2)', 168, [328])
issues = [{'id': 'stat12-p328-727-accept', 'unit': 7, 'printedPage': 328, 'description': 'Answer 7.27 prints z = −2.1004 “accept H₀”; at 1% one-tailed (critical −2.33) this is consistent. Printed answers retained as given.'}]

if __name__ == '__main__':
    save(168, [(6, ans6), (7, ans7), (8, ans8)], issues=issues)
