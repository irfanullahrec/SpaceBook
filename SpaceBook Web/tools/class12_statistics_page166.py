"""PDF166 printed 323–324: Answers — Exercise 3 (3.1–3.32); Exercise 4 (4.1–4.13)."""
from class12_statistics_common import Builder, save

L = lambda s: (s,) * 3
F = lambda a, b: f'$\\frac{{{a}}}{{{b}}}$'
b = Builder()
b.h('Exercise-3', 'مشق-3', 'تمرین-3')
b.group('lines', [
    L('3.1 (i) F (ii) T (iii) F (iv) T (v) T (vi) F (vii) T (viii) T (ix) T (x) T'),
    ('3.2 (i) two (ii) one (iii) n (iv) n and p (v) np, npq (vi) n (vii) 0 and 1 (viii) random numbers (ix) independent (x) varies/changes',
     '3.2 (i) دو (ii) ایک (iii) n (iv) n اور p (v) np، npq (vi) n (vii) 0 اور 1 (viii) تصادفی اعداد (ix) آزاد (x) بدلتا ہے',
     '3.2 (i) دوه (ii) یو (iii) n (iv) n او p (v) np، npq (vi) n (vii) 0 او 1 (viii) تصادفي عددونه (ix) خپلواک (x) بدلېږي'),
    L('3.3 (i) b (ii) c (iii) c (iv) d (v) b (vi) c (vii) d (viii) a (ix) b (x) d'),
    L('3.10 (i) 0 (ii) 0.29 (iii) 0 (iv) 0.936 (v) 0.352'),
])
b.p('3.11', '3.11', '3.11')
b.dist('stat12-ans-3-11', ['0', '1', '2', '3', '4', '5'], ['0.095', '0.286', '0.343', '0.206', '0.062', '0.007'], total=None)
b.group('lines', [
    L('3.12 (i) 0.656 (ii) 0.891'), L('3.13 (i) 0.07776 (ii) 0.2592 (iii) 0.92224'), L('3.14 (i) 0.60501 (ii) 0.39499'),
    L('3.15 0.227'), L('3.16 0.62343'), L('3.17 0.0005'),
    ('3.19 (i) 40 bolts (ii) 6', '3.19 (i) 40 بولٹ (ii) 6', '3.19 (i) 40 بولټونه (ii) 6'),
    L('3.20 $n=12$, $p=0.25$'), L('3.21 $n=41$, $p=0.302$'),
    ('3.22 No, because q = 1.8 which cannot be greater than 1.', '3.22 نہیں، کیونکہ q = 1.8 ہے جو 1 سے بڑا نہیں ہو سکتا۔', '3.22 نه، ځکه q = 1.8 دی چې له 1 لوی کېدای نه شي.'),
    L('3.23 (i) 16 (ii) 0.9576'),
    ('3.24 mean = 3, variance = 1.6, S.D = 1.25', '3.24 اوسط = 3، تغیر = 1.6، S.D = 1.25', '3.24 منځنی = 3، واریانس = 1.6، S.D = 1.25'),
    L('3.25 (b) 52.08, 41.67, 12.5, 1.67, 0.08'),
    ('3.26 mean = 5.42 variance = 2.4824', '3.26 اوسط = 5.42 تغیر = 2.4824', '3.26 منځنی = 5.42 واریانس = 2.4824'),
    L('3.27 11.04 64.07 154.94 199.83 144.98 56.10 9.04'),
])
b.p('3.30', '3.30', '3.30')
b.dist('stat12-ans-3-30', ['1', '2', '3', '4', '5'], ['1/66', '2/11', '5/11', '10/33', '1/22'], xlabel='x', total=None)
b.group('lines', [
    ('Mean = 3.187, Variance = 0.706', 'اوسط = 3.187، تغیر = 0.706', 'منځنی = 3.187، واریانس = 0.706'),
    L('3.31 0.275'), L('3.32 0.213'),
])
ans3 = b.build('stat12-answers-ex3', 'Answers — Exercise 3', 'جوابات — مشق 3', 'ځوابونه — تمرین 3', 166, [323, 324])

c = Builder()
c.h('Exercise-4', 'مشق-4', 'تمرین-4')
c.group('lines', [
    L('4.1 (i) F (ii) F (iii) T (iv) T (v) T (vi) T (vii) F (viii) T (ix) F (x) T'),
    (f'4.2 (i) 4 (ii) Z~N(0,1) (iii) X = μ (iv) {F(4, 5)}σ (v) zero (vi) normal (vii) 10 (viii) mean = μ (ix) Mean = 0 (x) 95.4',
     f'4.2 (i) 4 (ii) Z~N(0,1) (iii) X = μ (iv) {F(4, 5)}σ (v) صفر (vi) نارمل (vii) 10 (viii) اوسط = μ (ix) اوسط = 0 (x) 95.4',
     f'4.2 (i) 4 (ii) Z~N(0,1) (iii) X = μ (iv) {F(4, 5)}σ (v) صفر (vi) نورمال (vii) 10 (viii) منځنی = μ (ix) منځنی = 0 (x) 95.4'),
    L('4.3 (i) b (ii) a (iii) b (iv) b (v) c (vi) c (vii) c (viii) b (ix) d (x) a'),
    L('4.8 (i) 0.0548 (ii) 0.044 (iii) 0.103 (iv) 0.475 (v) 0.950 (vi) 0.682 (vii) 0.006'),
    L('4.9 (i) 0.5987 (ii) 0.2119 (iii) 0.0668 (iv) 0.7734'),
    L('4.10 (i) 0.0043 (ii) 0.0735 (iii) 0.0103 (iv) 0.1196 (v) 0.9777 (vi) 0.9850'),
    L('4.11 (i) z = 2.58 (ii) z = 1.24 (iii) z = −1.75'),
    ('4.12 (i) z = 0.84 (ii) z = −0.25 (iii) z = −1.04 and +1.04', '4.12 (i) z = 0.84 (ii) z = −0.25 (iii) z = −1.04 اور +1.04', '4.12 (i) z = 0.84 (ii) z = −0.25 (iii) z = −1.04 او +1.04'),
    L('4.13 (i) 0.1587 (ii) 0.0228 (iii) 0.3721'),
])
ans4 = c.build('stat12-answers-ex4-a', 'Answers — Exercise 4 (4.1–4.13)', 'جوابات — مشق 4 (4.1–4.13)', 'ځوابونه — تمرین 4 (4.1–4.13)', 166, [324])
issues = [{'id': 'stat12-p324-411-illegible', 'unit': 4, 'printedPage': 324, 'description': 'Answer 4.11 (ii) is partly damaged in the scan (“z = 1.2?”); read as 1.24. Verify against a clean print.'}]

if __name__ == '__main__':
    save(166, [(3, ans3), (4, ans4)], issues=issues)
