"""PDF165 printed 321–322: Answers — Exercise 1 (1.21–1.30); Exercise 2 (2.1–2.24)."""
from class12_statistics_common import Builder, save

L = lambda s: (s,) * 3
F = lambda a, b: f'$\\frac{{{a}}}{{{b}}}$'
a = Builder()
a.group('lines', [
    L('1.21 (b) 0.92'), L(f'1.22 {F(8, 36)}'), L(f'1.24 {F(1, 4)}'), L('1.25 (i) 0.0059 (ii) 0.0045'), L(f'1.26 (b) {F(1, 3)}'),
    L('1.27 (i) 0.12 (ii) 0.6 (iii) 0.68'), L(f'1.28 {F(3, 4)}'), L(f'1.29 (i) {F(1, 210)} (ii) {F(209, 210)}'),
    L('1.30 (a) $p=\\frac{1}{2},d=1$ (b) $p=\\frac{1}{4},d=\\frac{1}{3}$'),
])
ans1 = a.build('stat12-answers-ex1-b', 'Answers — Exercise 1 (1.21–1.30)', 'جوابات — مشق 1 (1.21–1.30)', 'ځوابونه — تمرین 1 (1.21–1.30)', 165, [321])

b = Builder()
b.h('Exercise-2', 'مشق-2', 'تمرین-2')
b.group('lines', [
    L('2.1 (i) T (ii) F (iii) T (iv) F (v) T (vi) F (vii) T (viii) T (ix) F (x) T'),
    (f'2.2 (i) finite (ii) unity (iii) {F(5, 21)} (iv) random variable (v) discrete & continuous (vi) joint distribution (vii) one (viii) E(X)E(Y) (ix) S.D(X)+S.D(Y) (x) {F(2, 3)}',
     f'2.2 (i) متناہی (ii) اکائی (iii) {F(5, 21)} (iv) تصادفی متغیر (v) غیر مسلسل اور مسلسل (vi) مشترکہ تقسیم (vii) ایک (viii) E(X)E(Y) (ix) S.D(X)+S.D(Y) (x) {F(2, 3)}',
     f'2.2 (i) محدود (ii) یو (iii) {F(5, 21)} (iv) تصادفي متغیر (v) ناپرلپسې او پرلپسې (vi) ګډ وېش (vii) یو (viii) E(X)E(Y) (ix) S.D(X)+S.D(Y) (x) {F(2, 3)}'),
    L('2.3 (i) b (ii) b (iii) b (iv) c (v) d (vi) c (vii) c (viii) b (ix) a (x) d'),
    ('2.6 (i) continuous (ii) continuous (iii) discrete (iv) continuous (v) continuous (vi) discrete (vii) continuous (viii) continuous (ix) discrete (x) discrete',
     '2.6 (i) مسلسل (ii) مسلسل (iii) غیر مسلسل (iv) مسلسل (v) مسلسل (vi) غیر مسلسل (vii) مسلسل (viii) مسلسل (ix) غیر مسلسل (x) غیر مسلسل',
     '2.6 (i) پرلپسې (ii) پرلپسې (iii) ناپرلپسې (iv) پرلپسې (v) پرلپسې (vi) ناپرلپسې (vii) پرلپسې (viii) پرلپسې (ix) ناپرلپسې (x) ناپرلپسې'),
])
b.p('2.8', '2.8', '2.8')
b.dist('stat12-ans-2-8', ['0', '1', '2'], [F(1, 4), F(2, 4), F(1, 4)], total=None)
b.p('2.9', '2.9', '2.9')
b.dist('stat12-ans-2-9', ['0', '1', '2', '3'], [F(1, 8), F(3, 8), F(3, 8), F(1, 8)], total=None)
b.p('2.10 (i) 0.3 (ii) 0.6 (iii) 0.8', '2.10 (i) 0.3 (ii) 0.6 (iii) 0.8', '2.10 (i) 0.3 (ii) 0.6 (iii) 0.8')
b.p('2.11', '2.11', '2.11')
b.dist('stat12-ans-2-11', ['−3', '−1', '1', '3'], [F(1, 8), F(3, 8), F(3, 8), F(1, 8)], total=None)
b.p('2.12', '2.12', '2.12')
b.dist('stat12-ans-2-12', ['−5', '−4', '−3', '−2', '−1', '0', '1', '2', '3', '4', '5'], [F(k, 36) for k in (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)], total=None)
b.group('lines', [
    ('2.13 No, because sum of probabilities is not equal to one', '2.13 نہیں، کیونکہ احتمالات کا مجموعہ ایک کے برابر نہیں', '2.13 نه، ځکه چې د احتمالونو مجموعه له یو سره برابره نه ده'),
    L(f'2.14 (i) {F(3, 8)} (ii) {F(1, 2)} (iii) {F(3, 4)}'), L('2.15 (b) (i) 3 (ii) 0.125 (iii) 0.019'),
    L('2.17 (i) 0.5 (ii) 3.5 (iii) 6'), L('2.18 0.55, 1.35, 1.16'), L('2.19 (i) 2.6 (ii) 1.34 (iii) 1.16'),
    L(f'2.20 (i) 20 (ii) {F(2, 3)} (iii) {F(2, 63)} (iv) 0.178'),
    ('2.21 Mean $=\\frac{4}{9}$ Variance $=\\frac{13}{162}$, S.D = 0.2833', '2.21 اوسط $=\\frac{4}{9}$ تغیر $=\\frac{13}{162}$، S.D = 0.2833', '2.21 منځنی $=\\frac{4}{9}$ واریانس $=\\frac{13}{162}$، S.D = 0.2833'),
    L('2.22 $E(X)=2$, $E(Y)=0.5$, $E(X+Y)=2.5$, $E(XY)=1$'),
    ('2.23 (i) Yes, X & Y are independent (ii) 35, 36.8, 71.8, 1288', '2.23 (i) ہاں، X اور Y آزاد ہیں (ii) 35، 36.8، 71.8، 1288', '2.23 (i) هو، X او Y خپلواک دي (ii) 35، 36.8، 71.8، 1288'),
    L('2.24 (i) 0.41 (ii) 0.24 (iii) 0.65 (iv) 0.65'),
])
ans2 = b.build('stat12-answers-ex2-a', 'Answers — Exercise 2 (2.1–2.24)', 'جوابات — مشق 2 (2.1–2.24)', 'ځوابونه — تمرین 2 (2.1–2.24)', 165, [321, 322])

if __name__ == '__main__':
    save(165, [(1, ans1), (2, ans2)])
