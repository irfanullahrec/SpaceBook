"""Class 8 Maths phase 6b: Review 2 Q4 g,h; Review 6 Q1j; Review 8 Q1j; 5.1 Q1; 5.3 Q10 (set laws verified on the actual sets).
Writes class-8/math/dsl/u8y.txt."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'u8y.txt'
L = []


def text(key, en, ur, ps, ans):
    L.append(f'{key} ~ @text {en}|{ur}|{ps} => {ans} %%')


def rows(key, rs, ans):
    L.append(f'{key} ~ @text ' + ' ;; '.join(rs) + f' => {ans} %%')


def same(t):
    return f'{t}|{t}|{t}'


text('Review Exercise 2|4|g', 'The digits 53 repeat forever: 0.4535353… = 0.4͔53 (recurring).', 'ہندسے 53 بار بار دہرائے جاتے ہیں: 0.4535353… دہرانے والا اعشاریہ ہے۔', 'رقمونه 53 تکراریږي: 0.4535353… تکراري اعشاریه ده.', 'Recurring decimal')
text('Review Exercise 2|4|h', 'The digits 7.6751053… never end and show no repeating block, so it is a non-recurring (non-terminating) decimal.', 'ہندسے 7.6751053… نہ ختم ہوتے ہیں نہ ان میں کوئی دہرانے والا ٹکڑا ہے، اس لیے یہ غیر دہرانے والا اعشاریہ ہے۔', 'رقمونه 7.6751053… نه پای ته رسیږي او نه تکراري برخه لري، نو دا غیر تکراري اعشاریه ده.', 'Non-recurring decimal')
for ex, q, right, why in [
    ('Review Exercise 6', 'j', 'iv', ('Algebraic expressions whose variables have whole-number powers are called polynomials.', 'وہ الجبری جملے جن کے متغیرات کی طاقتیں مکمل اعداد ہوں کثیر رکنی (پولینومیل) کہلاتے ہیں۔', 'هغه الجبري افادې چې د متغیرونو توانونه یې پوره عددونه وي پولینومیل بلل کیږي.')),
    ('Review Exercise 8', 'j', 'i', ('The line y = x is y = 1·x + 0, so its gradient is m = 1.', 'لکیر y = x کو y = 1·x + 0 لکھ سکتے ہیں، اس لیے اس کی ڈھلوان m = 1 ہے۔', 'کرښه y = x د y = 1·x + 0 په توګه لیکل کیږي، نو ډیالوان یې m = 1 دی.'))]:
    import json as _j
    for part in ['i', 'ii', 'iii', 'iv']:
        mark = 'correct' if part == right else 'not the answer'
        text(f'{ex}|{q}|{part}', f'Option {part}) is {mark}. ' + why[0], f'آپشن {part}) ' + ('درست ہے۔ ' if part == right else 'جواب نہیں۔ ') + why[1], f'انتخاب {part}) ' + ('سم دی. ' if part == right else 'ځواب نه دی. ') + why[2], f'Option {right}) is correct')
text('5.1|1|i', 'Descriptive form states the property in words: W = the set of whole numbers; Z⁺ = the set of positive integers; E = the set of non-negative even numbers; O = the set of positive odd numbers; P = the set of prime numbers.', 'بیانیہ صورت میں خاصیت الفاظ میں لکھی جاتی ہے: W = مکمل اعداد کا سیٹ؛ Z⁺ = مثبت صحیح اعداد کا سیٹ؛ E = غیر منفی جفت اعداد کا سیٹ؛ O = مثبت طاق اعداد کا سیٹ؛ P = مفرد اعداد کا سیٹ۔', 'تشریحي بڼه کې ځانګړتیا په ټکو لیکل کیږي: W = د پوره عددونو سیټ؛ Z⁺ = د مثبتو بشپړ عددونو سیټ؛ E = د غیر منفي جفت عددونو سیټ؛ O = د مثبتو تاق عددونو سیټ؛ P = د لومړنیو عددونو سیټ.', 'Five sets in descriptive form')
text('5.1|1|ii', 'Tabular form lists the elements: W = {0, 1, 2, 3, …}; Z⁺ = {1, 2, 3, 4, …}; E = {0, 2, 4, 6, …}; O = {1, 3, 5, 7, …}; P = {2, 3, 5, 7, 11, …}.', 'جدولی صورت میں عناصر لکھے جاتے ہیں: W = {0, 1, 2, 3, …}؛ Z⁺ = {1, 2, 3, 4, …}؛ E = {0, 2, 4, 6, …}؛ O = {1, 3, 5, 7, …}؛ P = {2, 3, 5, 7, 11, …}۔', 'جدولي بڼه کې عناصر لیکل کیږي: W = {0, 1, 2, 3, …}؛ Z⁺ = {1, 2, 3, 4, …}؛ E = {0, 2, 4, 6, …}؛ O = {1, 3, 5, 7, …}؛ P = {2, 3, 5, 7, 11, …}.', 'Five sets in tabular form')
text('5.1|1|iii', 'Set-builder form states the rule: W = {x | x ∈ W ∧ x ≥ 0}; Z⁺ = {x | x ∈ Z ∧ x > 0}; E = {x | x = 2n, n ∈ W}; O = {x | x = 2n − 1, n ∈ N}; P = {x | x is a prime number}.', 'سیٹ بلڈر صورت میں قاعدہ لکھا جاتا ہے: W = {x | x ∈ W ∧ x ≥ 0}؛ Z⁺ = {x | x ∈ Z ∧ x > 0}؛ E = {x | x = 2n, n ∈ W}؛ O = {x | x = 2n − 1, n ∈ N}؛ P = {x | x مفرد عدد ہے}۔', 'د سیټ جوړوونکې بڼه کې قاعده لیکل کیږي: W = {x | x ∈ W ∧ x ≥ 0}؛ Z⁺ = {x | x ∈ Z ∧ x > 0}؛ E = {x | x = 2n, n ∈ W}؛ O = {x | x = 2n − 1, n ∈ N}؛ P = {x | x لومړنی عدد دی}.', 'Five sets in set-builder form')

e1 = 'E⁺ ∪ O⁺ = N, and P ⊂ N, so (E⁺ ∪ O⁺) ∪ P = N; also O⁺ ∪ P = O⁺ ∪ {2}, so E⁺ ∪ (O⁺ ∪ P) = N. Union is associative. E⁺ ∩ O⁺ = ϕ, so (E⁺ ∩ O⁺) ∩ P = ϕ; O⁺ ∩ P = {3, 5, 7, 11, …} has no even number, so E⁺ ∩ (O⁺ ∩ P) = ϕ. Intersection is associative.'
u1 = 'E⁺ ∪ O⁺ = N اور P ⊂ N، اس لیے (E⁺ ∪ O⁺) ∪ P = N؛ نیز O⁺ ∪ P = O⁺ ∪ {2}، اس لیے E⁺ ∪ (O⁺ ∪ P) = N۔ اتحاد ایسوسی ایٹو ہے۔ E⁺ ∩ O⁺ = ϕ، اس لیے (E⁺ ∩ O⁺) ∩ P = ϕ؛ O⁺ ∩ P = {3, 5, 7, 11, …} میں کوئی جفت عدد نہیں، اس لیے E⁺ ∩ (O⁺ ∩ P) = ϕ۔ تقاطع ایسوسی ایٹو ہے۔'
p1 = 'E⁺ ∪ O⁺ = N او P ⊂ N، نو (E⁺ ∪ O⁺) ∪ P = N؛ همدارنګه O⁺ ∪ P = O⁺ ∪ {2}، نو E⁺ ∪ (O⁺ ∪ P) = N. اتحاد اسوسیټیو دی. E⁺ ∩ O⁺ = ϕ، نو (E⁺ ∩ O⁺) ∩ P = ϕ؛ O⁺ ∩ P = {3, 5, 7, 11, …} کې جفت عدد نشته، نو E⁺ ∩ (O⁺ ∩ P) = ϕ. تقاطع اسوسیټیو دی.'
e2 = 'Distributive: E⁺ ∪ (O⁺ ∩ P) = E⁺ ∪ {3, 5, 7, 11, …}; (E⁺ ∪ O⁺) ∩ (E⁺ ∪ P) = N ∩ (E⁺ ∪ P) = E⁺ ∪ {3, 5, 7, 11, …}. Equal. E⁺ ∩ (O⁺ ∪ P) = E⁺ ∩ (O⁺ ∪ {2}) = {2}; (E⁺ ∩ O⁺) ∪ (E⁺ ∩ P) = ϕ ∪ {2} = {2}. Equal.'
u2 = 'تقسیمی: E⁺ ∪ (O⁺ ∩ P) = E⁺ ∪ {3, 5, 7, 11, …}؛ (E⁺ ∪ O⁺) ∩ (E⁺ ∪ P) = N ∩ (E⁺ ∪ P) = E⁺ ∪ {3, 5, 7, 11, …}۔ برابر۔ E⁺ ∩ (O⁺ ∪ P) = E⁺ ∩ (O⁺ ∪ {2}) = {2}؛ (E⁺ ∩ O⁺) ∪ (E⁺ ∩ P) = ϕ ∪ {2} = {2}۔ برابر۔'
p2 = 'ویشونکی: E⁺ ∪ (O⁺ ∩ P) = E⁺ ∪ {3, 5, 7, 11, …}؛ (E⁺ ∪ O⁺) ∩ (E⁺ ∪ P) = N ∩ (E⁺ ∪ P) = E⁺ ∪ {3, 5, 7, 11, …}. برابر. E⁺ ∩ (O⁺ ∪ P) = E⁺ ∩ (O⁺ ∪ {2}) = {2}؛ (E⁺ ∩ O⁺) ∪ (E⁺ ∩ P) = ϕ ∪ {2} = {2}. برابر.'
L.append(f'5.3|10|i ~ @text {e1}|{u1}|{p1} ;; {e2}|{u2}|{p2} => Associative and distributive laws hold %%')

a1 = 'M = {1, 2, …, 9}, N = {3, 5, 7, 11, 13}, T = {3, 5, 7}. Associative: (M ∪ N) ∪ T = {1, …, 9, 11, 13} = M ∪ (N ∪ T); (M ∩ N) ∩ T = {3, 5, 7} = M ∩ (N ∩ T).'
b1 = 'M = {1, 2, …, 9}، N = {3, 5, 7, 11, 13}، T = {3, 5, 7}۔ ایسوسی ایٹو: (M ∪ N) ∪ T = {1, …, 9, 11, 13} = M ∪ (N ∪ T)؛ (M ∩ N) ∩ T = {3, 5, 7} = M ∩ (N ∩ T)۔'
c1 = 'M = {1, 2, …, 9}، N = {3, 5, 7, 11, 13}، T = {3, 5, 7}. اسوسیټیو: (M ∪ N) ∪ T = {1, …, 9, 11, 13} = M ∪ (N ∪ T)؛ (M ∩ N) ∩ T = {3, 5, 7} = M ∩ (N ∩ T).'
a2 = 'Distributive: M ∪ (N ∩ T) = M ∪ {3, 5, 7} = {1, …, 9}; (M ∪ N) ∩ (M ∪ T) = {1, …, 9, 11, 13} ∩ {1, …, 9} = {1, …, 9}. M ∩ (N ∪ T) = M ∩ N = {3, 5, 7}; (M ∩ N) ∪ (M ∩ T) = {3, 5, 7} ∪ {3, 5, 7} = {3, 5, 7}. Both laws hold.'
b2 = 'تقسیمی: M ∪ (N ∩ T) = M ∪ {3, 5, 7} = {1, …, 9}؛ (M ∪ N) ∩ (M ∪ T) = {1, …, 9, 11, 13} ∩ {1, …, 9} = {1, …, 9}۔ M ∩ (N ∪ T) = M ∩ N = {3, 5, 7}؛ (M ∩ N) ∪ (M ∩ T) = {3, 5, 7}۔ دونوں قوانین درست ہیں۔'
c2 = 'ویشونکی: M ∪ (N ∩ T) = M ∪ {3, 5, 7} = {1, …, 9}؛ (M ∪ N) ∩ (M ∪ T) = {1, …, 9, 11, 13} ∩ {1, …, 9} = {1, …, 9}. M ∩ (N ∪ T) = M ∩ N = {3, 5, 7}؛ (M ∩ N) ∪ (M ∩ T) = {3, 5, 7}. دواړه قوانین سم دي.'
L.append(f'5.3|10|ii ~ @text {a1}|{b1}|{c1} ;; {a2}|{b2}|{c2} => Associative and distributive laws hold %%')

OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L))
