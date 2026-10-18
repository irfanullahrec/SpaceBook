"""PDF169 printed 329–330: Answers — Exercise 8 (8.3–8.23); Exercise 9 (9.1–9.25)."""
from class12_statistics_common import Builder, save

L = lambda s: (s,) * 3
REJ = ('reject', 'رد کریں', 'رد کړئ'); ACC = ('accept', 'قبول کریں', 'ومنئ')
X = lambda n, v, d: (f'{n} $\\chi^2={v}$, {d[0]} $H_0$', f'{n} $\\chi^2={v}$، $H_0$ {d[1]}', f'{n} $\\chi^2={v}$، $H_0$ {d[2]}')
a = Builder()
a.group('lines', [
    L('8.3 (i) c (ii) b (iii) d (iv) d (v) b (vi) c (vii) b (viii) c (ix) c (x) b'),
    ('8.9 Q = −0.76, the association between extravagant fathers and extravagant sons is negative.', '8.9 Q = −0.76، فضول خرچ باپوں اور فضول خرچ بیٹوں کے درمیان تلازم منفی ہے۔', '8.9 Q = −0.76، د مسرفو پلرونو او مسرفو زامنو ترمنځ تړاو منفي دی.'),
    ('8.10 Q = 0, attributes A and B are independent.', '8.10 Q = 0، صفات A اور B آزاد ہیں۔', '8.10 Q = 0، صفتونه A او B خپلواک دي.'),
    ('8.11 Q = 0.46, there is positive association.', '8.11 Q = 0.46، مثبت تلازم ہے۔', '8.11 Q = 0.46، مثبت تړاو شته.'),
    ('8.12 Q = 0.9, there is high degree of positive association between intelligent fathers and sons.', '8.12 Q = 0.9، ذہین باپوں اور بیٹوں کے درمیان اعلیٰ درجے کا مثبت تلازم ہے۔', '8.12 Q = 0.9، د هوښیارو پلرونو او زامنو ترمنځ لوړه کچه مثبت تړاو شته.'),
    ('8.13 Q = −0.57, it means that vaccine and small-pox are negatively associated i.e. vaccine prevents the attack of small-pox.', '8.13 Q = −0.57، اس کا مطلب ہے کہ ویکسین اور چیچک منفی طور پر متلازم ہیں یعنی ویکسین چیچک کے حملے کو روکتی ہے۔', '8.13 Q = −0.57، مانا دا ده چې واکسین او چیچک منفي تړاو لري یعنې واکسین د چیچک له حملې مخنیوی کوي.'),
    X('8.14', '48.24', REJ), X('8.15', '8.89', REJ), X('8.16', '60.183', REJ), X('8.18', '598.51', REJ), X('8.19', '29.79', REJ), X('8.20', '763.76', REJ),
    L('8.22 $\\chi^2=3.279$, C = 0.067'), L('8.23 $\\chi^2=1048.5$, C = 0.3681'),
])
ans8 = a.build('stat12-answers-ex8-b', 'Answers — Exercise 8 (8.3–8.23)', 'جوابات — مشق 8 (8.3–8.23)', 'ځوابونه — تمرین 8 (8.3–8.23)', 169, [329])

Fc = lambda n, v, d: (f'{n} $F_c={v}$ {d[0]} $H_0$', f'{n} $F_c={v}$، $H_0$ {d[1]}', f'{n} $F_c={v}$، $H_0$ {d[2]}')
b = Builder()
b.h('Exercise-9', 'مشق-9', 'تمرین-9')
b.group('lines', [
    L('9.1 (i) T (ii) T (iii) F (iv) T (v) T (vi) T (vii) T (viii) F (ix) T (x) F'),
    ('9.2 (i) experimental unit (ii) randomization (iii) replication (iv) extraneous factors (v) efficient (vi) component variances (vii) no problem (viii) can never (ix) replication (x) field experiments',
     '9.2 (i) تجرباتی اکائی (ii) تصادفیت (iii) تکرار (iv) خارجی عوامل (v) مؤثر (vi) جزوی تغیرات (vii) کوئی مسئلہ نہیں (viii) کبھی نہیں (ix) تکرار (x) کھیت کے تجربات',
     '9.2 (i) تجربوي واحد (ii) تصادفي کول (iii) تکرار (iv) بهرني عوامل (v) موثر (vi) برخه‌ییز واریانسونه (vii) هېڅ ستونزه نه (viii) هېڅکله نه (ix) تکرار (x) ځمکنۍ تجربې'),
    L('9.3 (i) c (ii) c (iii) a (iv) b (v) b (vi) a (vii) d (viii) c (ix) d (x) d'),
    Fc('9.16', '0.277', ACC), Fc('9.17', '1.37', ACC), Fc('9.18', '0.055', ACC), Fc('9.19', '4', REJ), Fc('9.20', '3.333', ACC),
    Fc('9.21', '5.56', REJ), Fc('9.22', '2.56', ACC), Fc('9.23', '0.82', ACC), Fc('9.24', '2.10', ACC), Fc('9.25', '6.46', ACC),
])
ans9 = b.build('stat12-answers-ex9', 'Answers — Exercise 9', 'جوابات — مشق 9', 'ځوابونه — تمرین 9', 169, [329, 330])
issues = [{'id': 'stat12-p330-925', 'unit': 9, 'printedPage': 330, 'description': 'Answers list 9.25 (F = 6.46) although Exercise 9 ends at 9.24; printed answer retained.'}]

if __name__ == '__main__':
    save(169, [(8, ans8), (9, ans9)], issues=issues)
