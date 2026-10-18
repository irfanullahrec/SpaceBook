"""PDF164 printed 319–320: Unit 9 Exercise 9.22 (end)–9.24 (unit end); Answers — Exercise 1 (1.1–1.20)."""
from class12_statistics_common import Builder, save

b = Builder()
b.p('Construct an ANOVA table for the data. Test α = 0.05 that five population means are equal.', 'مواد کے لیے ANOVA جدول بنائیں۔ α = 0.05 پر جانچ کریں کہ پانچ آبادیوں کے اوسط برابر ہیں۔', 'د معلوماتو لپاره د ANOVA جدول جوړ کړئ. په α = 0.05 وازموئ چې د پنځو نفوسونو منځني برابر دي.')
b.group('lines', [
    ('9.23 Compare the following random samples.', '9.23 درج ذیل تصادفی نمونوں کا موازنہ کریں۔', '9.23 لاندې تصادفي نمونې پرتله کړئ.'),
    ('Sample 1: 17 19 4 9 10 11', 'نمونہ 1: 17 19 4 9 10 11', 'نمونه 1: 17 19 4 9 10 11'),
    ('Sample 2: 12 15 6 8 10 11 12', 'نمونہ 2: 12 15 6 8 10 11 12', 'نمونه 2: 12 15 6 8 10 11 12'),
    ('Sample 3: 20 23 9 13 15', 'نمونہ 3: 20 23 9 13 15', 'نمونه 3: 20 23 9 13 15'),
    ('Perform ANOVA and test the hypothesis at α = 0.05 that the samples came from populations having same means.', 'ANOVA کریں اور α = 0.05 پر اس مفروضے کی جانچ کریں کہ نمونے یکساں اوسط والی آبادیوں سے آئے ہیں۔', 'ANOVA ترسره کړئ او په α = 0.05 دا فرضیه وازموئ چې نمونې د یو شان منځنیو لرونکو نفوسونو څخه راغلې دي.'),
    ('9.24 The results shown in the following table were obtained through completely randomized design.', '9.24 درج ذیل جدول میں دکھائے گئے نتائج مکمل تصادفی ڈیزائن کے ذریعے حاصل کیے گئے۔', '9.24 په لاندې جدول کې ښودل شوې پایلې د بشپړ تصادفي ډیزاین له لارې ترلاسه شوې.'),
])
R = [['A', '2', '1', '0', '2', ''], ['B', '2', '5', '3', '4', '5'], ['C', '3', '2', '3', '2', '4']]
H = [''] * 6
b.table('stat12-t-q9-24', H, R, H, H, R, R, noHeader=True)
b.p('Test at 1% level of significance that there is no difference in the means of the three populations.', '1% معنویت کی سطح پر جانچ کریں کہ تینوں آبادیوں کے اوسطوں میں کوئی فرق نہیں۔', 'د 1% معنی‌داریت په کچه وازموئ چې د درېیو نفوسونو په منځنیو کې هېڅ توپیر نشته.')
ex = b.build('stat12-u9-exercise-d', 'Unit 9 Exercise — 9.22 (end) to 9.24', 'یونٹ 9 مشق — 9.22 (اختتام) تا 9.24', 'واحد 9 تمرین — 9.22 (پای) تر 9.24', 164, [319])

a = Builder()
a.h('ANSWERS', 'جوابات', 'ځوابونه')
a.h('Exercise-1', 'مشق-1', 'تمرین-1')
L = lambda s: (s,) * 3
a.group('lines', [
    L('1.1 (i) T (ii) F (iii) F (iv) T (v) T (vi) F (vii) T (viii) T (ix) T (x) F'),
    ('1.2 (i) impossible (ii) sample space (iii) permutations (iv) 0 to 1 (v) gambling (vi) addition (vii) P(A) + P(B) (viii) independent (ix) 1−P(A) (x) $\\frac{6}{36}$',
     '1.2 (i) ناممکن (ii) نمونہ جاتی فضا (iii) ترتیبات (iv) 0 سے 1 (v) جوا (vi) جمع (vii) P(A) + P(B) (viii) آزاد (ix) 1−P(A) (x) $\\frac{6}{36}$',
     '1.2 (i) ناشونی (ii) نمونوي فضا (iii) ترتیبونه (iv) له 0 تر 1 (v) قمار (vi) جمع (vii) P(A) + P(B) (viii) خپلواک (ix) 1−P(A) (x) $\\frac{6}{36}$'),
    L('1.3 (i) c (ii) d (iii) c (iv) d (v) b (vi) c (vii) d (viii) b (ix) c (x) b'),
    L('1.5 (i) 40320 (ii) 6375600 (iii) 10626 (iv) 3876 (v) 167960'),
    L('1.7 40320, 720'), L('1.8 60'),
    L('1.9 (i) 4989600 (ii) 15135120 (iii) 19958400 (iv) 4989600 (v) 50400'),
    L('1.10 330'), L('1.15 0.50'), L('1.16 $\\frac{5}{36}$'),
    L('1.17 (i) $\\frac{1}{8}$ (ii) $\\frac{3}{8}$ (iii) $\\frac{7}{8}$'), L('1.18 0.0045'),
    L('1.19 (i) $\\frac{13}{52}$ (ii) $\\frac{26}{52}$ (iii) $\\frac{4}{52}$'), L('1.20 (i) $\\frac{1}{3}$ (ii) 0.133'),
])
ans1 = a.build('stat12-answers-ex1-a', 'Answers — Exercise 1 (1.1–1.20)', 'جوابات — مشق 1 (1.1–1.20)', 'ځوابونه — تمرین 1 (1.1–1.20)', 164, [320])

if __name__ == '__main__':
    save(164, [(9, ex), (1, ans1)], complete_units=[9])
