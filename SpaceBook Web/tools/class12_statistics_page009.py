"""PDF9 printed 9–10: notes on Axiom I, Axioms II–III, 1.2.5 probability of simple events, Examples 1.5–1.8 (start)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('Note that:', 'نوٹ کریں کہ:', 'پام وکړئ چې:')
b.group('lines', [
    ('(i) If $P(E)=0$, the event E is said to be null event.', '(i) اگر $P(E)=0$ ہو تو واقعہ E خالی واقعہ کہلاتا ہے۔', '(i) که $P(E)=0$ وي، نو E پېښه تشه پېښه بلل کېږي.'),
    ('(ii) If $P(E)=1$, the event E is said to be sure event.', '(ii) اگر $P(E)=1$ ہو تو واقعہ E یقینی واقعہ کہلاتا ہے۔', '(ii) که $P(E)=1$ وي، نو E پېښه حتمي پېښه بلل کېږي.'),
    ('Axiom (II) $\\;P(S)=1$', 'مسلّمہ (II) $\\;P(S)=1$', 'اصل (II) $\\;P(S)=1$'),
    ('Axiom (III) If $E_1$ and $E_2$ are mutually exclusive events, then $P(E_1\\cup E_2)=P(E_1)+P(E_2)$',
     'مسلّمہ (III) اگر $E_1$ اور $E_2$ باہم مانع واقعات ہوں تو $P(E_1\\cup E_2)=P(E_1)+P(E_2)$',
     'اصل (III) که $E_1$ او $E_2$ یو بل منع کوونکې پېښې وي، نو $P(E_1\\cup E_2)=P(E_1)+P(E_2)$'),
])
b.h('1.2.5 Calculation of probability in case of simple events', '1.2.5 سادہ واقعات کی صورت میں احتمال کا حساب', '1.2.5 د ساده پېښو په حالت کې د احتمال محاسبه')
b.h('Example 1.5', 'مثال 1.5', 'بېلګه 1.5')
b.p('If a coin is tossed, what is the chance of a head?', 'اگر ایک سکہ اچھالا جائے تو چِت آنے کا کیا امکان ہے؟', 'که یوه سکه واچول شي، د سر د راتلو چانس څومره دی؟')
b.h(*SOL)
b.mlines([r'n(S)=2^n=2^1=2', r'S=\{H,T\}'])
b.p('Let A: head occurs', 'فرض کریں A: چِت آتا ہے', 'فرض کړئ A: سر راځي')
b.mlines([r'A=\{H\}', r'n(A)=1', r'\therefore P(A)=\frac{n(A)}{n(S)}=\frac{m}{n}=\frac{1}{2}=0.5'])
b.p('It will be more suitable for interpretation to express the answer in percentage.', 'تشریح کے لیے جواب کو فیصد میں ظاہر کرنا زیادہ موزوں ہوگا۔', 'د تفسیر لپاره به ښه وي چې ځواب په سلنه کې وښودل شي.')
b.h('Example 1.6', 'مثال 1.6', 'بېلګه 1.6')
b.p('A fair coin is tossed twice. What is the probability that exactly one head occurs?', 'ایک منصفانہ سکہ دو بار اچھالا جاتا ہے۔ ٹھیک ایک چِت آنے کا احتمال کیا ہے؟', 'یوه عادلانه سکه دوه ځله اچول کېږي. د دقیقاً یو سر د راتلو احتمال څومره دی؟')
b.h(*SOL)
b.mlines([r'n(S)=2^n=2^2=4', r'S=\{HH,HT,TH,TT\}'])
b.p('Let A: exactly one head', 'فرض کریں A: ٹھیک ایک چِت', 'فرض کړئ A: دقیقاً یو سر')
b.mlines([r'A=\{HT,TH\}', r'n(A)=2', r'P(A)=\frac{n(A)}{n(S)}=\frac{2}{4}=\frac{1}{2}=0.5'])
b.h('Example 1.7', 'مثال 1.7', 'بېلګه 1.7')
b.p('Three fair coins are tossed once. Find the probability of (i) exactly two tails (ii) at least two tails (iii) at most 2 heads.',
    'تین منصفانہ سکے ایک بار اچھالے جاتے ہیں۔ احتمال معلوم کریں: (i) ٹھیک دو پَٹ (ii) کم از کم دو پَٹ (iii) زیادہ سے زیادہ 2 چِت۔',
    'درې عادلانه سکې یو ځل اچول کېږي. احتمال یې پیدا کړئ: (i) دقیقاً دوه لکۍ (ii) لږ تر لږه دوه لکۍ (iii) تر ټولو زیات 2 سرونه.')
b.h(*SOL)
b.mlines([r'n(S)=2^n=2^3=8', r'S=\{HHH,HHT,HTH,HTT,THH,THT,TTH,TTT\}'])
b.p('(i) Let A: exactly two tails', '(i) فرض کریں A: ٹھیک دو پَٹ', '(i) فرض کړئ A: دقیقاً دوه لکۍ')
b.mlines([r'A=\{HTT,THT,TTH\}', r'n(A)=3', r'P(A)=\frac{n(A)}{n(S)}=\frac{3}{8}=0.375'])
b.p('(ii) Let B: at least two tails', '(ii) فرض کریں B: کم از کم دو پَٹ', '(ii) فرض کړئ B: لږ تر لږه دوه لکۍ')
b.mlines([r'B=\{HTT,THT,TTH,TTT\}', r'n(B)=4', r'P(B)=\frac{n(B)}{n(S)}=\frac{4}{8}=\frac{1}{2}=0.5'])
b.p('(iii) Let C: at most 2 heads', '(iii) فرض کریں C: زیادہ سے زیادہ 2 چِت', '(iii) فرض کړئ C: تر ټولو زیات 2 سرونه')
b.mlines([r'C=\{HHT,HTH,HTT,THH,THT,TTH,TTT\}', r'n(C)=7', r'P(C)=\frac{n(C)}{n(S)}=\frac{7}{8}=0.875'])
b.h('Example 1.8', 'مثال 1.8', 'بېلګه 1.8')
b.p('If a die is rolled, what is the probability that the number appearing on top is (i) an odd number (ii) an even number less than 5.',
    'اگر ایک پانسہ پھینکا جائے تو اوپر آنے والا عدد (i) طاق عدد ہو (ii) 5 سے کم جفت عدد ہو، اس کا احتمال کیا ہے؟',
    'که ډایس واچول شي، احتمال یې څومره دی چې پورته راغلی عدد (i) طاق عدد وي (ii) له 5 څخه کوچنی جفت عدد وي.')
b.h(*SOL)
b.p('For die $n(S)=6^n$', 'پانسے کے لیے $n(S)=6^n$', 'د ډایس لپاره $n(S)=6^n$')
rec = b.build('stat12-p009-simple-events', '1.2.5 Probability of simple events — Examples 1.5–1.8', '1.2.5 سادہ واقعات کا احتمال — مثالیں 1.5–1.8', '1.2.5 د ساده پېښو احتمال — بېلګې 1.5–1.8', 9, [9, 10])

if __name__ == '__main__':
    save(9, [(1, rec)])
