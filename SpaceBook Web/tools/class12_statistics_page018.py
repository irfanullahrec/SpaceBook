"""PDF18 printed 27–28: Unit 1 Exercise 1.1 (true/false), 1.2 (fill in the blanks), 1.3 MCQs (i)–(x)."""
from class12_statistics_common import Builder, save

b = Builder()
b.h('Exercise', 'مشق', 'تمرین')
b.h('1.1 Write T for true and F for false statement.', '1.1 درست بیان کے لیے T اور غلط کے لیے F لکھیں۔', '1.1 د سم بیان لپاره T او د ناسم لپاره F ولیکئ.')
b.group('lines', [
    ('i. The range of probability is from zero to one.', 'i. احتمال کی حد صفر سے ایک تک ہے۔', 'i. د احتمال حد له صفر څخه تر یو پورې دی.'),
    ('ii. An event which contains only one sample point is called compound event.', 'ii. وہ واقعہ جس میں صرف ایک نمونہ نقطہ ہو، مرکب واقعہ کہلاتا ہے۔', 'ii. هغه پېښه چې یوازې یو نمونوي ټکی ولري، مرکبه پېښه بلل کېږي.'),
    ('iii. Events which cannot occur at a time are called not mutually exclusive events.', 'iii. وہ واقعات جو ایک وقت میں واقع نہ ہو سکیں، غیر باہم مانع واقعات کہلاتے ہیں۔', 'iii. هغه پېښې چې په یو وخت رامنځته نه شي، نه یو بل منع کوونکې پېښې بلل کېږي.'),
    ('iv. When a die is rolled four time, the number of sample points in the sample space will be 1296.', 'iv. جب ایک پانسہ چار بار پھینکا جائے تو نمونہ فضا میں نمونہ نقاط کی تعداد 1296 ہوگی۔', 'iv. کله چې یو ډایس څلور ځله واچول شي، نو په نمونوي فضا کې د نمونوي ټکو شمېر به 1296 وي.'),
    ('v. Two events are mutually exclusive if they have no outcomes in common.', 'v. دو واقعات باہم مانع ہوتے ہیں اگر ان میں کوئی نتیجہ مشترک نہ ہو۔', 'v. دوه پېښې یو بل منع کوونکې وي که هېڅ ګډه پایله ونه لري.'),
    ('vi. A and B are mutually exclusive events if $P(A\\text{ and }B)=P(A)\\,P(B)$', 'vi. A اور B باہم مانع واقعات ہیں اگر $P(A\\text{ and }B)=P(A)\\,P(B)$', 'vi. A او B یو بل منع کوونکې پېښې دي که $P(A\\text{ and }B)=P(A)\\,P(B)$'),
    ('vii. When two events are independent, the occurrence of one event will not change the probability of the second event.', 'vii. جب دو واقعات آزاد ہوں تو ایک واقعہ کا وقوع دوسرے واقعہ کے احتمال کو تبدیل نہیں کرے گا۔', 'vii. کله چې دوه پېښې خپلواکې وي، د یوې پېښې رامنځته کېدل به د دویمې پېښې احتمال بدل نه کړي.'),
    ('viii. The probability of drawing a red card form pack of 52 cards is $\\frac{26}{52}$.', 'viii. 52 پتوں کی گڈی سے سرخ پتا نکالنے کا احتمال $\\frac{26}{52}$ ہے۔', 'viii. د 52 کارتونو له ګډۍ څخه د سور کارت د راایستلو احتمال $\\frac{26}{52}$ دی.'),
    ('ix. Probability of an event will never be negative.', 'ix. کسی واقعہ کا احتمال کبھی منفی نہیں ہوگا۔', 'ix. د یوې پېښې احتمال به هېڅکله منفي نه وي.'),
    ('x. The complementary events are always not-mutually exclusive events.', 'x. تکمیلی واقعات ہمیشہ غیر باہم مانع واقعات ہوتے ہیں۔', 'x. بشپړوونکې پېښې تل نه یو بل منع کوونکې پېښې وي.'),
])
b.h('1.2 Fill in the suitable word in the blanks.', '1.2 خالی جگہوں میں مناسب لفظ بھریں۔', '1.2 په تشو ځایونو کې مناسبه کلمه ولیکئ.')
blank = '______'
b.group('lines', [
    ('(i) An event which cannot occur is known as ______ event.', '(i) جو واقعہ واقع نہ ہو سکے اسے ______ واقعہ کہتے ہیں۔', '(i) هغه پېښه چې رامنځته نه شي، ______ پېښه بلل کېږي.'),
    ('(ii) Totality of all possible outcomes of a random experiment is called ______', '(ii) کسی تصادفی تجربے کے تمام ممکنہ نتائج کی کلیت کو ______ کہتے ہیں', '(ii) د یوې تصادفي تجربې د ټولو شونو پایلو مجموعې ته ______ وایي'),
    ('(iii) An orderly arrangements of r distinct things out of n are called ______', '(iii) n میں سے r مختلف چیزوں کی مرتب ترتیبات کو ______ کہتے ہیں', '(iii) له n څخه د r بېلابېلو شیانو منظمو ترتیبونو ته ______ وایي'),
    ('(iv) The limits of probability are from ______', '(iv) احتمال کی حدیں ______ ہیں', '(iv) د احتمال حدونه ______ دي'),
    ('(v) The need for probability was originally felt in ______', '(v) احتمال کی ضرورت ابتدا میں ______ میں محسوس ہوئی', '(v) احتمال ته اړتیا په پیل کې په ______ کې احساس شوه'),
    ('(vi) $P(A\\cup B)$ can be expressed by the ______ law of probability.', '(vi) $P(A\\cup B)$ کو احتمال کے ______ قانون سے ظاہر کیا جا سکتا ہے۔', '(vi) $P(A\\cup B)$ د احتمال د ______ قانون په واسطه ښودل کېدای شي.'),
    ('(vii) If two events A and B are disjoint, the $P(A\\cup B)=$ ______', '(vii) اگر دو واقعات A اور B منفصل ہوں تو $P(A\\cup B)=$ ______', '(vii) که دوه پېښې A او B بېلې وي، نو $P(A\\cup B)=$ ______'),
    ('(viii) If $P(A\\cap B)=P(A)\\,P(B)$, then events A and B are ______', '(viii) اگر $P(A\\cap B)=P(A)\\,P(B)$ ہو تو واقعات A اور B ______ ہیں', '(viii) که $P(A\\cap B)=P(A)\\,P(B)$ وي، نو A او B پېښې ______ دي'),
    ('(ix) If $\\overline{A}$ is the compliment of A, the probability of $\\overline{A}$ is equal to ______', '(ix) اگر $\\overline{A}$ واقعہ A کا تکملہ ہو تو $\\overline{A}$ کا احتمال ______ کے برابر ہے', '(ix) که $\\overline{A}$ د A بشپړوونکې وي، نو د $\\overline{A}$ احتمال له ______ سره برابر دی'),
    ('(x) The probability of obtaining a total of 7 in single throw of two dice is ______', '(x) دو پانسوں کو ایک بار پھینکنے میں کل 7 آنے کا احتمال ______ ہے', '(x) د دوو ډایسونو په یو ځل اچولو کې د ټولټال 7 د ترلاسه کولو احتمال ______ دی'),
])
b.h('1.3 Choose the correct answer.', '1.3 درست جواب منتخب کریں۔', '1.3 سم ځواب وټاکئ.')
b.mcq('(i)', ('The probability of an event A lies between', 'کسی واقعہ A کا احتمال درمیان ہوتا ہے', 'د A پېښې احتمال ترمنځ وي'),
      [('−1 and +1', '−1 اور +1', '−1 او +1'), ('−1 and 0', '−1 اور 0', '−1 او 0'), ('0 and 1', '0 اور 1', '0 او 1'), ('+1 and −1', '+1 اور −1', '+1 او −1')])
b.mcq('(ii)', ('Probability is expressed as', 'احتمال ظاہر کیا جاتا ہے بطور', 'احتمال ښودل کېږي د')
      , [('ratio', 'نسبت', 'نسبت'), ('proportion', 'تناسب', 'تناسب'), ('percentage', 'فیصد', 'سلنه'), ('all of the above', 'تمام مندرجہ بالا', 'پورته ټول')])
b.mcq('(iii)', ('When two events cannot happen simultaneously in a single trial, the events are said to be', 'جب ایک ہی آزمائش میں دو واقعات بیک وقت واقع نہ ہو سکیں تو واقعات کہلاتے ہیں', 'کله چې په یوه ازمېښت کې دوه پېښې په یو وخت رامنځته نه شي، پېښې بلل کېږي'),
      [('dependent', 'تابع', 'تړلې'), ('equally likely', 'مساوی امکان والے', 'مساوي امکان لرونکې'), ('mutually Exclusive', 'باہم مانع', 'یو بل منع کوونکې'), ('independent', 'آزاد', 'خپلواکې')])
b.mcq('(iv)', ('An event consisting of those elements, which are not in A is called', 'ان عناصر پر مشتمل واقعہ جو A میں نہیں، کہلاتا ہے', 'هغه پېښه چې د هغو عناصرو څخه جوړه وي چې په A کې نه دي، بلل کېږي'),
      [('primary event', 'بنیادی واقعہ', 'لومړنۍ پېښه'), ('derived event', 'ماخوذ واقعہ', 'مشتقه پېښه'), ('simple event', 'سادہ واقعہ', 'ساده پېښه'), ('complementary event', 'تکمیلی واقعہ', 'بشپړوونکې پېښه')])
b.mcq('(v)', ('If A is an event, the conditional probability of A given A is equal to', 'اگر A ایک واقعہ ہو تو A دیا ہونے پر A کا مشروط احتمال برابر ہے', 'که A یوه پېښه وي، د A په شرط د A شرطي احتمال برابر دی له'),
      [('zero', 'صفر', 'صفر'), ('one', 'ایک', 'یو'), '$\\infty$', '0.8'])
b.mcq('(vi)', ('If a coin is tossed three times, then the probability of getting at most one head is equal to', 'اگر ایک سکہ تین بار اچھالا جائے تو زیادہ سے زیادہ ایک چِت آنے کا احتمال برابر ہے', 'که یوه سکه درې ځله واچول شي، نو د تر ټولو زیات یو سر د ترلاسه کولو احتمال برابر دی له'),
      ['$3/8$', '$7/8$', '$1/2$', '$1/8$'])
b.mcq('(vii)', ('The probability of throwing an even sum with two fair dice is', 'دو منصفانہ پانسوں سے جفت مجموعہ آنے کا احتمال ہے', 'د دوو عادلانه ډایسونو سره د جفت مجموعې د راتلو احتمال دی'),
      ['$1/4$', '$1/16$', '$1$', '$1/2$'])
b.mcq('(viii)', ('The probability of six on a fair die is $1/6$. The probability of not six is', 'منصفانہ پانسے پر چھ آنے کا احتمال $1/6$ ہے۔ چھ نہ آنے کا احتمال ہے', 'په عادلانه ډایس د شپږو احتمال $1/6$ دی. د شپږو نه راتلو احتمال دی'),
      ['$2/6$', '$5/6$', '$1/2$', '$6/6$'])
b.mcq('(ix)', ('$P(A)+P(\\overline{A})$ is equal to', '$P(A)+P(\\overline{A})$ برابر ہے', '$P(A)+P(\\overline{A})$ برابر دی له'), ['0', '$\\infty$', '1', '0.5'])
b.mcq('(x)', ('A fair die and a fair coin are thrown at a time. The number of combined outcomes is', 'ایک منصفانہ پانسہ اور ایک منصفانہ سکہ ایک ساتھ پھینکے جاتے ہیں۔ مشترکہ نتائج کی تعداد ہے', 'یو عادلانه ډایس او یوه عادلانه سکه یوځای اچول کېږي. د ګډو پایلو شمېر دی'),
      ['6', '12', '2', '8'])
rec = b.build('stat12-u1-exercise-a', 'Unit 1 Exercise — 1.1 to 1.3', 'یونٹ 1 مشق — 1.1 تا 1.3', 'واحد 1 تمرین — 1.1 تر 1.3', 18, [27, 28])

if __name__ == '__main__':
    save(18, [(1, rec)])
