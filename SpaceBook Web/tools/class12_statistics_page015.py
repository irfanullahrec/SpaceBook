"""PDF15 printed 21–22: Example 1.19 end, 1.3.4 conditional probability, Example 1.20, 1.3.5 multiplication law for dependent events, Example 1.21 question."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('$P(B)=\\frac{{}^{6}_{1}C}{{}^{10}_{1}C}=\\frac{6}{10}$. Therefore required probability of both green balls is',
    '$P(B)=\\frac{{}^{6}_{1}C}{{}^{10}_{1}C}=\\frac{6}{10}$۔ لہٰذا دونوں سبز گیندوں کا مطلوبہ احتمال یہ ہے',
    '$P(B)=\\frac{{}^{6}_{1}C}{{}^{10}_{1}C}=\\frac{6}{10}$. نو د دواړو شنو توپونو اړین احتمال دا دی')
b.mlines([r'P(A\text{ and }B)=P(A)\,P(B)', r'\phantom{P(A\text{ and }B)}=\frac{6}{10}\times\frac{6}{10}=\frac{36}{100}=0.36'])
b.h('1.3.4 Conditional probability', '1.3.4 مشروط احتمال', '1.3.4 شرطي احتمال')
b.p('Many times probability of an event is asked that is conditioned on some available information. For example (i) what is the probability that a person selected at random has diabetes given that he has a family history of diabetes. (ii) What is the probability that 3 occurs on a die given that an odd number has occurred. The given information reduces the original sample space by excluding some outcomes as being impossible which before receiving the information were believed possible. This reduced sample space is called conditional sample space and probabilities associated to it are called conditional probabilities.',
    'اکثر کسی واقعہ کا ایسا احتمال پوچھا جاتا ہے جو کسی دستیاب معلومات سے مشروط ہو۔ مثلاً (i) تصادفی طور پر منتخب شخص کو ذیابیطس ہونے کا احتمال کیا ہے جبکہ معلوم ہو کہ اس کے خاندان میں ذیابیطس کی تاریخ ہے۔ (ii) پانسے پر 3 آنے کا احتمال کیا ہے جبکہ معلوم ہو کہ طاق عدد آیا ہے۔ دی گئی معلومات اصل نمونہ فضا کو چھوٹا کر دیتی ہیں کیونکہ وہ کچھ نتائج کو ناممکن قرار دے کر خارج کر دیتی ہیں جو معلومات ملنے سے پہلے ممکن سمجھے جاتے تھے۔ اس چھوٹی نمونہ فضا کو مشروط نمونہ فضا اور اس سے متعلق احتمالات کو مشروط احتمالات کہتے ہیں۔',
    'ډېر ځله د یوې پېښې داسې احتمال پوښتل کېږي چې په کوم شته معلومات پورې مشروط وي. د بېلګې په توګه (i) احتمال یې څومره دی چې په تصادفي ډول ټاکل شوی کس شکر ولري په داسې حال کې چې د کورنۍ تاریخچه یې د شکرې ده. (ii) احتمال یې څومره دی چې په ډایس 3 راشي په داسې حال کې چې طاق عدد راغلی وي. ورکړل شوي معلومات اصلي نمونوي فضا کوچنۍ کوي ځکه چې ځینې هغه پایلې د ناشونو په توګه لرې کوي چې د معلوماتو تر ترلاسه کېدو مخکې شونې ګڼل کېدې. دې کوچنۍ شوې فضا ته شرطي نمونوي فضا او له هغې سره تړلو احتمالونو ته شرطي احتمالونه وایي.')
b.h('Definition of conditional probability', 'مشروط احتمال کی تعریف', 'د شرطي احتمال تعریف')
b.p('The conditional probability of an event A given that another event B has already occurred is denoted by $P(A/B)$ and is defined as;',
    'کسی واقعہ A کا مشروط احتمال، جبکہ دوسرا واقعہ B پہلے ہی واقع ہو چکا ہو، $P(A/B)$ سے ظاہر کیا جاتا ہے اور اس کی تعریف یہ ہے؛',
    'د A پېښې شرطي احتمال، په داسې حال کې چې بله پېښه B مخکې رامنځته شوې وي، په $P(A/B)$ ښودل کېږي او داسې تعریف کېږي؛')
b.eq(r'P(A/B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)\neq 0')
b.h('Example 1.20', 'مثال 1.20', 'بېلګه 1.20')
b.p('A coin is tossed twice. Find the conditional probability that two tails result, given that there is at least one tail?',
    'ایک سکہ دو بار اچھالا جاتا ہے۔ دو پَٹ آنے کا مشروط احتمال معلوم کریں جبکہ کم از کم ایک پَٹ آیا ہو؟',
    'یوه سکه دوه ځله اچول کېږي. د دوو لکیو د راتلو شرطي احتمال پیدا کړئ په داسې حال کې چې لږ تر لږه یوه لکۍ راغلې وي؟')
b.h(*SOL)
b.mlines([r'n(S)=2^n=2^2=4', r'S=\{HH,HT,TH,TT\}'])
b.p('Let A: 2 tail appear', 'فرض کریں A: 2 پَٹ آتے ہیں', 'فرض کړئ A: 2 لکۍ راځي')
b.eq(r'A=\{TT\}')
b.p('Let B: at least one tail appears', 'فرض کریں B: کم از کم ایک پَٹ آتا ہے', 'فرض کړئ B: لږ تر لږه یوه لکۍ راځي')
b.mlines([r'B=\{HT,TH,TT\}', r'n(B)=3', r'P(B)=\frac{n(B)}{n(S)}=\frac{3}{4}', r'A\cap B=(TT)', r'n(A\cap B)=1',
          r'P(A\cap B)=\frac{n(A\cap B)}{n(S)}=\frac{1}{4}', r'\therefore P(A/B)=\frac{P(A\cap B)}{P(B)}=\frac{1/4}{3/4}=\frac{1}{4}\times\frac{4}{3}=\frac{1}{3}'])
b.h('1.3.5 Multiplication law for dependent events', '1.3.5 تابع واقعات کے لیے قانونِ ضرب', '1.3.5 د تړلو پېښو لپاره د ضرب قانون')
b.h('Statement:', 'بیان:', 'بیان:')
b.p('If A and B are two dependent events then the probability that both A and B occur is equal to the probability that A occurs multiplied by the conditional probability of B given that A has already occurred. Symbolically,',
    'اگر A اور B دو تابع واقعات ہوں تو A اور B دونوں کے واقع ہونے کا احتمال، A کے واقع ہونے کے احتمال کو B کے مشروط احتمال (جبکہ A پہلے واقع ہو چکا ہو) سے ضرب دینے کے برابر ہے۔ علامتی طور پر،',
    'که A او B دوه تړلې پېښې وي، نو د A او B دواړو د رامنځته کېدو احتمال د A د رامنځته کېدو له احتمال سره برابر دی چې د B په شرطي احتمال (په داسې حال کې چې A مخکې رامنځته شوې وي) کې ضرب شي. په نښو کې،')
b.eq(r'P(A\text{ and }B)=P(A\cap B)=P(A)\,P(B/A)')
b.h('Proof:', 'ثبوت:', 'ثبوت:')
b.p('The conditional probability of B given that A has already occurred is', 'B کا مشروط احتمال، جبکہ A پہلے واقع ہو چکا ہو، یہ ہے', 'د B شرطي احتمال، په داسې حال کې چې A مخکې رامنځته شوې وي، دا دی')
b.eq(r'P(B/A)=\frac{P(B\cap A)}{P(A)}')
b.p('Multiplying both sides by P(A), we get', 'دونوں طرف P(A) سے ضرب دینے پر', 'دواړه خواوې په P(A) کې ضربولو سره')
b.mlines([r'P(A)\,P(B/A)=P(B\cap A)', r'\text{or } P(A\cap B)=P(A)\,P(B/A)\qquad(\because P(A\cap B)=P(B\cap A))'])
b.h('Example 1.21', 'مثال 1.21', 'بېلګه 1.21')
b.p('Suppose that a bag contains 10 balls of which 3 are white balls and 7 are green balls. If two balls are drawn at random one after another without replacement, find the probability that both balls drawn are green.',
    'فرض کریں ایک تھیلے میں 10 گیندیں ہیں جن میں 3 سفید اور 7 سبز ہیں۔ اگر دو گیندیں تصادفی طور پر یکے بعد دیگرے بغیر واپسی کے نکالی جائیں تو دونوں نکالی گئی گیندوں کے سبز ہونے کا احتمال معلوم کریں۔',
    'فرض کړئ په یوه کڅوړه کې 10 توپونه دي چې 3 یې سپین او 7 یې شنه دي. که دوه توپونه په تصادفي ډول یو په بل پسې بې له بېرته اچولو راوویستل شي، نو د دواړو راایستل شویو توپونو د شین کېدو احتمال پیدا کړئ.')
rec = b.build('stat12-p015-conditional', '1.3.4 Conditional probability and 1.3.5 multiplication law (dependent events)', '1.3.4 مشروط احتمال اور 1.3.5 قانونِ ضرب (تابع واقعات)', '1.3.4 شرطي احتمال او 1.3.5 د ضرب قانون (تړلې پېښې)', 15, [21, 22])

if __name__ == '__main__':
    save(15, [(1, rec)])
