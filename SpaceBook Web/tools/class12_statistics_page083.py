"""PDF83 printed 157–158: sampling without replacement, Example 5.1 (all samples of size 2), 5.1.9 probability/non-probability sampling, 5.1.10 simple random sampling (start)."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h('◆ Sampling without replacement', '◆ بغیر واپسی کے نمونہ گیری', '◆ پرته له بېرته اچولو نمونه اخیستنه')
b.p('When the item selected for a sample is not returned to the population before drawing the next item, it is called sampling without replacement (S.W.O.R). In this case;', 'جب نمونے کے لیے منتخب شے اگلی شے نکالنے سے پہلے آبادی میں واپس نہ رکھی جائے تو اسے بغیر واپسی کے نمونہ گیری (S.W.O.R) کہتے ہیں۔ اس صورت میں؛', 'کله چې د نمونې لپاره ټاکل شوی توکی د بل توکي له راایستلو مخکې نفوس ته بېرته ورنه کړل شي، پرته له بېرته اچولو نمونه اخیستنه (S.W.O.R) بلل کېږي. په دې حالت کې؛')
b.group('lines', [
    ('i. Possible samples will be ${}^{N}_{n}C$', 'i. ممکنہ نمونے ${}^{N}_{n}C$ ہوں گے', 'i. شونې نمونې به ${}^{N}_{n}C$ وي'),
    ('ii. Probability of selection of each unit changes from draw to draw.', 'ii. ہر اکائی کے انتخاب کا احتمال ہر بار بدل جاتا ہے۔', 'ii. د هر واحد د ټاکل کېدو احتمال له یوه ځل څخه تر بل بدلېږي.'),
    ('iii. Sampling units will be dependent.', 'iii. نمونہ اکائیاں تابع ہوں گی۔', 'iii. نمونوي واحدونه به تړلي وي.'),
    ('iv. Sampling units can be selected only once.', 'iv. نمونہ اکائیاں صرف ایک بار منتخب ہو سکتی ہیں۔', 'iv. نمونوي واحدونه یوازې یو ځل ټاکل کېدای شي.'),
    ('v. The sample size is less or equal to the population size, that is, $n\\le N$.', 'v. نمونے کا سائز آبادی کے سائز سے کم یا برابر ہوتا ہے، یعنی $n\\le N$۔', 'v. د نمونې اندازه د نفوس له اندازې کمه یا برابره وي، یعنې $n\\le N$.'),
])
b.h('Example 5.1', 'مثال 5.1', 'بېلګه 5.1')
b.p('Suppose a population consist of values 2, 4, 6, 8. Draw all possible samples of size two (i) with replacement and (ii) without replacement.', 'فرض کریں ایک آبادی قیمتوں 2، 4، 6، 8 پر مشتمل ہے۔ دو کے سائز کے تمام ممکنہ نمونے (i) واپسی کے ساتھ اور (ii) بغیر واپسی کے نکالیں۔', 'فرض کړئ یو نفوس له 2، 4، 6، 8 قیمتونو جوړ دی. د دوو په اندازه ټولې شونې نمونې (i) له بېرته اچولو سره او (ii) پرته له بېرته اچولو راوباسئ.')
b.h(*SOL)
b.p('Given 2, 4, 6, 8 (population), N = 4 (population size), n = 2 (sample size)', 'دیا گیا ہے 2، 4، 6، 8 (آبادی)، N = 4 (آبادی کا سائز)، n = 2 (نمونے کا سائز)', 'ورکړل شوي 2، 4، 6، 8 (نفوس)، N = 4 (د نفوس اندازه)، n = 2 (د نمونې اندازه)')
b.p('(i) Sampling with replacement case:', '(i) واپسی کے ساتھ نمونہ گیری کی صورت:', '(i) له بېرته اچولو سره د نمونه اخیستنې حالت:')
b.p('The number of samples in this case $=N^n=4^2=16$. The procedure for drawing samples is that divide total number of samples by population size i.e. $\\frac{16}{4}=4$ and write every unit of the population 4-times in the first column, then divide the obtained result 4 by the population size i.e. $\\frac{4}{4}=1$ and write every element of the population once in the second column as shown below;',
    'اس صورت میں نمونوں کی تعداد $=N^n=4^2=16$۔ نمونے نکالنے کا طریقہ یہ ہے کہ نمونوں کی کل تعداد کو آبادی کے سائز پر تقسیم کریں یعنی $\\frac{16}{4}=4$ اور آبادی کی ہر اکائی کو پہلے کالم میں 4 بار لکھیں، پھر حاصل شدہ نتیجہ 4 کو آبادی کے سائز پر تقسیم کریں یعنی $\\frac{4}{4}=1$ اور آبادی کے ہر عنصر کو دوسرے کالم میں ایک بار لکھیں جیسا کہ نیچے دکھایا گیا ہے؛',
    'په دې حالت کې د نمونو شمېر $=N^n=4^2=16$. د نمونو د راایستلو طریقه دا ده چې د نمونو ټول شمېر د نفوس پر اندازه ووېشئ یعنې $\\frac{16}{4}=4$ او د نفوس هر واحد په لومړي ستون کې 4 ځله ولیکئ، بیا لاسته راغلې پایله 4 د نفوس پر اندازه ووېشئ یعنې $\\frac{4}{4}=1$ او د نفوس هر عنصر په دویم ستون کې یو ځل ولیکئ لکه څنګه چې لاندې ښودل شوي؛')
b.table('stat12-t-ex5-1-swr', ['', '', '', ''], [['(2, 2)', '(4, 2)', '(6, 2)', '(8, 2)'], ['(2, 4)', '(4, 4)', '(6, 4)', '(8, 4)'], ['(2, 6)', '(4, 6)', '(6, 6)', '(8, 6)'], ['(2, 8)', '(4, 8)', '(6, 8)', '(8, 8)']],
        ['', '', '', ''], ['', '', '', ''], noHeader=True)
b.p('(ii) Sampling without replacement case', '(ii) بغیر واپسی کے نمونہ گیری کی صورت', '(ii) پرته له بېرته اچولو د نمونه اخیستنې حالت')
b.p('The number of samples in this case $={}^{N}_{n}C={}^{4}_{2}C=6$. The procedure for drawing samples in this case is that consider the first unit 2 with all other units of the population and keep it aside, then consider 4 with remaining units and keep it aside and so on, we have',
    'اس صورت میں نمونوں کی تعداد $={}^{N}_{n}C={}^{4}_{2}C=6$۔ اس صورت میں نمونے نکالنے کا طریقہ یہ ہے کہ پہلی اکائی 2 کو آبادی کی باقی تمام اکائیوں کے ساتھ لیں اور الگ رکھ دیں، پھر 4 کو باقی اکائیوں کے ساتھ لیں اور الگ رکھ دیں وغیرہ، ہمیں ملتا ہے',
    'په دې حالت کې د نمونو شمېر $={}^{N}_{n}C={}^{4}_{2}C=6$. په دې حالت کې د نمونو د راایستلو طریقه دا ده چې لومړی واحد 2 د نفوس له ټولو نورو واحدونو سره ونیسئ او یو طرف ته یې کېږدئ، بیا 4 له پاتې واحدونو سره ونیسئ او یو طرف ته یې کېږدئ او داسې نور، لاسته راځي')
b.table('stat12-t-ex5-1-swor', ['', '', '', '', '', ''], [['(2,4)', '(2,6)', '(2,8)', '(4,6)', '(4,8)', '(6,8)']], ['', '', '', '', '', ''], ['', '', '', '', '', ''], noHeader=True)
ex = b.build('stat12-p083-swor-example', 'Sampling without replacement — Example 5.1', 'بغیر واپسی کے نمونہ گیری — مثال 5.1', 'پرته له بېرته اچولو نمونه اخیستنه — بېلګه 5.1', 83, [157, 158])

c = Builder()
c.h('5.1.9 Probability and non-probability sampling methods', '5.1.9 احتمالی اور غیر احتمالی نمونہ گیری کے طریقے', '5.1.9 د احتمالي او غیر احتمالي نمونه اخیستنې طریقې')
c.p('Sampling methods are broadly divided in to two categories (i) Probability sampling methods and (ii) non-probability sampling methods.', 'نمونہ گیری کے طریقوں کو وسیع طور پر دو اقسام میں تقسیم کیا جاتا ہے (i) احتمالی نمونہ گیری کے طریقے اور (ii) غیر احتمالی نمونہ گیری کے طریقے۔', 'د نمونه اخیستنې طریقې په پراخه کچه په دوو ډلو وېشل کېږي (i) د احتمالي نمونه اخیستنې طریقې او (ii) د غیر احتمالي نمونه اخیستنې طریقې.')
c.h('◆ Probability sampling methods', '◆ احتمالی نمونہ گیری کے طریقے', '◆ د احتمالي نمونه اخیستنې طریقې')
c.p('When each sampling unit of the population has non-zero probability of selection at each draw, the selection procedure is known as probability sampling or random sampling and the sample selected is called random sample. We will describe here the simple random sampling, stratified random sampling and systematic random sampling methods.',
    'جب آبادی کی ہر نمونہ اکائی کے ہر بار انتخاب کا احتمال غیر صفر ہو تو انتخاب کا طریقہ احتمالی نمونہ گیری یا تصادفی نمونہ گیری کہلاتا ہے اور منتخب نمونہ تصادفی نمونہ کہلاتا ہے۔ یہاں ہم سادہ تصادفی نمونہ گیری، طبقاتی تصادفی نمونہ گیری اور منظم تصادفی نمونہ گیری کے طریقے بیان کریں گے۔',
    'کله چې د نفوس هر نمونوي واحد په هر ځل کې د ټاکل کېدو غیر صفر احتمال ولري، د ټاکنې طریقه احتمالي نمونه اخیستنه یا تصادفي نمونه اخیستنه بلل کېږي او ټاکل شوې نمونه تصادفي نمونه بلل کېږي. دلته به ساده تصادفي نمونه اخیستنه، طبقه‌بندي تصادفي نمونه اخیستنه او منظمه تصادفي نمونه اخیستنه بیان کړو.')
c.h('◆ Non-probability sampling methods', '◆ غیر احتمالی نمونہ گیری کے طریقے', '◆ د غیر احتمالي نمونه اخیستنې طریقې')
c.p('When selection of units for a sample on each draw is not based on probability but personal judgment plays a significant role, the selection procedure is called non-probability sampling or non-random sampling. Commonly used non-probability sampling methods are: purposive or judgment sampling, Quota sampling, convenience sampling etc.',
    'جب ہر بار نمونے کے لیے اکائیوں کا انتخاب احتمال پر مبنی نہ ہو بلکہ ذاتی رائے اہم کردار ادا کرے تو انتخاب کا طریقہ غیر احتمالی نمونہ گیری یا غیر تصادفی نمونہ گیری کہلاتا ہے۔ عام طور پر استعمال ہونے والے غیر احتمالی طریقے یہ ہیں: بامقصد یا رائے پر مبنی نمونہ گیری، کوٹہ نمونہ گیری، سہولتی نمونہ گیری وغیرہ۔',
    'کله چې په هر ځل د نمونې لپاره د واحدونو ټاکنه پر احتمال ولاړه نه وي بلکې شخصي قضاوت مهم رول ولوبوي، د ټاکنې طریقه غیر احتمالي نمونه اخیستنه یا غیر تصادفي نمونه اخیستنه بلل کېږي. په عام ډول کارېدونکې غیر احتمالي طریقې دا دي: هدفمنده یا قضاوتي نمونه اخیستنه، کوټه نمونه اخیستنه، اسانتیايي نمونه اخیستنه او نور.')
c.h('5.1.10 Simple random sampling', '5.1.10 سادہ تصادفی نمونہ گیری', '5.1.10 ساده تصادفي نمونه اخیستنه')
c.p('In this method, each and every unit in the population has an equal chance of being selected for a sample. It is also known as random sampling. It is the simplest and widely used method among probability sampling methods. It is a base for other complicated sampling methods. It is the best one for homogenous population. The sample selected by this method is called simple random sample or simply random sample. A random sample may either be selected by with',
    'اس طریقے میں آبادی کی ہر اکائی کے نمونے کے لیے منتخب ہونے کا موقع یکساں ہوتا ہے۔ اسے تصادفی نمونہ گیری بھی کہتے ہیں۔ یہ احتمالی نمونہ گیری کے طریقوں میں سب سے سادہ اور بکثرت استعمال ہونے والا طریقہ ہے۔ یہ دوسرے پیچیدہ طریقوں کی بنیاد ہے۔ یہ یکساں (homogenous) آبادی کے لیے بہترین ہے۔ اس طریقے سے منتخب نمونے کو سادہ تصادفی نمونہ یا صرف تصادفی نمونہ کہتے ہیں۔ تصادفی نمونہ یا تو',
    'په دې طریقه کې په نفوس کې هر واحد د نمونې لپاره د ټاکل کېدو مساوي چانس لري. دې ته تصادفي نمونه اخیستنه هم وایي. دا د احتمالي نمونه اخیستنې د طریقو له منځه تر ټولو ساده او پراخه کارېدونکې طریقه ده. د نورو پېچلو طریقو بنسټ دی. د همجنس نفوس لپاره تر ټولو ښه ده. په دې طریقه ټاکل شوې نمونه ساده تصادفي نمونه یا یوازې تصادفي نمونه بلل کېږي. تصادفي نمونه کېدای شي یا')
sm = c.build('stat12-p083-sampling-methods', '5.1.9 Probability and non-probability sampling; 5.1.10 simple random sampling', '5.1.9 احتمالی اور غیر احتمالی نمونہ گیری؛ 5.1.10 سادہ تصادفی نمونہ گیری', '5.1.9 احتمالي او غیر احتمالي نمونه اخیستنه؛ 5.1.10 ساده تصادفي نمونه اخیستنه', 83, [158])

if __name__ == '__main__':
    save(83, [(5, ex), (5, sm)])
