"""PDF10 printed 11–12: Example 1.8 solution, Example 1.9 (two dice), Example 1.10 (cards), Example 1.11 question."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'\text{Here } n(S)=6^1=6', r'S=\{1,2,3,4,5,6\}'])
b.p('(i) Let A: an odd number', '(i) فرض کریں A: طاق عدد', '(i) فرض کړئ A: طاق عدد')
b.mlines([r'A=\{1,3,5\}', r'n(A)=3', r'P(A)=\frac{n(A)}{n(S)}=\frac{3}{6}=0.5'])
b.p('(ii) Let B: an even number less than 5', '(ii) فرض کریں B: 5 سے کم جفت عدد', '(ii) فرض کړئ B: له 5 څخه کوچنی جفت عدد')
b.mlines([r'B=\{2,4\}', r'n(B)=2', r'P(B)=\frac{n(B)}{n(S)}=\frac{2}{6}=\frac{1}{3}'])
b.h('Example 1.9', 'مثال 1.9', 'بېلګه 1.9')
b.p('Two dice are thrown once, what is the probability that (i) the total score is 8 (ii) score is at least 10 (iii) 5 occurs on the second die.',
    'دو پانسے ایک بار پھینکے جاتے ہیں، احتمال کیا ہے کہ (i) کل مجموعہ 8 ہو (ii) مجموعہ کم از کم 10 ہو (iii) دوسرے پانسے پر 5 آئے۔',
    'دوه ډایسونه یو ځل اچول کېږي، احتمال یې څومره دی چې (i) ټوله نمره 8 وي (ii) نمره لږ تر لږه 10 وي (iii) په دویم ډایس 5 راشي.')
b.h(*SOL)
b.mlines([r'\text{For two dice } n(S)=6^n=6^2=36',
          r'S=\left\{\begin{matrix}(1,1), & (1,2), & (1,3), & (1,4), & (1,5), & (1,6)\\ (2,1), & (2,2), & (2,3), & (2,4), & (2,5), & (2,6)\\ (3,1), & (3,2), & (3,3), & (3,4), & (3,5), & (3,6)\\ (4,1), & (4,2), & (4,3), & (4,4), & (4,5), & (4,6)\\ (5,1), & (5,2), & (5,3), & (5,4), & (5,5), & (5,6)\\ (6,1), & (6,2), & (6,3), & (6,4), & (6,5), & (6,6)\end{matrix}\right\}'])
b.p('(i) Let A: the total score is 8', '(i) فرض کریں A: کل مجموعہ 8 ہے', '(i) فرض کړئ A: ټوله نمره 8 ده')
b.mlines([r'A=\{(2,6),(3,5),(4,4),(5,3),(6,2)\}', r'n(A)=5', r'P(A)=\frac{n(A)}{n(S)}=\frac{5}{36}'])
b.p('(ii) Let B: score is at least 10', '(ii) فرض کریں B: مجموعہ کم از کم 10 ہے', '(ii) فرض کړئ B: نمره لږ تر لږه 10 ده')
b.mlines([r'B=\{(4,6),(5,5),(6,4),(5,6),(6,5),(6,6)\}', r'n(B)=6', r'P(B)=\frac{n(B)}{n(S)}=\frac{6}{36}=\frac{1}{6}'])
b.p('(iii) Let C: 5 occurs on the second die', '(iii) فرض کریں C: دوسرے پانسے پر 5 آتا ہے', '(iii) فرض کړئ C: په دویم ډایس 5 راځي')
b.mlines([r'C=\{(1,5),(2,5),(3,5),(4,5),(5,5),(6,5)\}', r'n(C)=6', r'P(C)=\frac{n(C)}{n(S)}=\frac{6}{36}=\frac{1}{6}'])
b.h('Example 1.10', 'مثال 1.10', 'بېلګه 1.10')
b.p('From an ordinary pack of 52 cards, one card is drawn at random. Find the chance of drawing (i) a heart (ii) a red card.',
    'تاش کے 52 پتوں کی ایک عام گڈی میں سے ایک پتا تصادفی طور پر نکالا جاتا ہے۔ (i) پان (ہارٹ) کا پتا (ii) سرخ پتا نکلنے کا امکان معلوم کریں۔',
    'د 52 کارتونو له یوې عادي ګډۍ څخه یو کارت په تصادفي ډول راایستل کېږي. د (i) هارټ (ii) سور کارت د راوتلو چانس پیدا کړئ.')
b.h(*SOL)
b.eq(r'n(S)={}^{n}_{r}C={}^{52}_{1}C=\frac{52!}{(52-1)!\,1!}=\frac{52\cdot 51!}{51!\,1}=52')
b.p('(i) Let A: card is heart', '(i) فرض کریں A: پتا پان (ہارٹ) کا ہے', '(i) فرض کړئ A: کارت هارټ دی')
b.p('$n(A)={}^{13}_{1}C=13$ (As there are 13 heart cards in an ordinary pack)', '$n(A)={}^{13}_{1}C=13$ (کیونکہ عام گڈی میں پان کے 13 پتے ہوتے ہیں)', '$n(A)={}^{13}_{1}C=13$ (ځکه چې په عادي ګډۍ کې 13 هارټ کارتونه وي)')
b.eq(r'P(A)=\frac{n(A)}{n(S)}=\frac{13}{52}=\frac{1}{4}=0.25')
b.p('(ii) Let B: card is red', '(ii) فرض کریں B: پتا سرخ ہے', '(ii) فرض کړئ B: کارت سور دی')
b.p('$n(B)={}^{26}_{1}C=26$ (As there are 26 red cards in a pack)', '$n(B)={}^{26}_{1}C=26$ (کیونکہ گڈی میں 26 سرخ پتے ہوتے ہیں)', '$n(B)={}^{26}_{1}C=26$ (ځکه چې په ګډۍ کې 26 سره کارتونه وي)')
b.eq(r'P(B)=\frac{n(B)}{n(S)}=\frac{26}{52}=\frac{1}{2}=0.5=50\%')
b.h('Example 1.11', 'مثال 1.11', 'بېلګه 1.11')
b.p('A bag contains 12 identical balls of which 5 white, 4 red and 3 black balls. Two balls are drawn. What is the probability that (i) both are red (ii) one white ball and one black ball?',
    'ایک تھیلے میں 12 یکساں گیندیں ہیں جن میں 5 سفید، 4 سرخ اور 3 سیاہ ہیں۔ دو گیندیں نکالی جاتی ہیں۔ احتمال کیا ہے کہ (i) دونوں سرخ ہوں (ii) ایک سفید اور ایک سیاہ گیند ہو؟',
    'په یوه کڅوړه کې 12 ورته توپونه دي چې 5 یې سپین، 4 سره او 3 تور دي. دوه توپونه راایستل کېږي. احتمال یې څومره دی چې (i) دواړه سره وي (ii) یو سپین او یو تور توپ وي؟')
rec = b.build('stat12-p010-dice-cards', 'Examples 1.8–1.11 — dice, cards and balls', 'مثالیں 1.8–1.11 — پانسے، تاش اور گیندیں', 'بېلګې 1.8–1.11 — ډایس، کارتونه او توپونه', 10, [11, 12])

if __name__ == '__main__':
    save(10, [(1, rec)])
