"""PDF6 printed 3–4: permutation examples 1.1–1.3, permutations with/without repetition, rule of combination."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('Consider the above example, n=3 (number of objects), r=2 (group size), therefore the number of permutations is equal to $ {}^{3}_{2}P=\\frac{3!}{(3-2)!}=\\frac{3\\cdot 2\\cdot 1}{1!}=\\frac{3\\cdot 2\\cdot 1}{1}=6$',
    'اوپر کی مثال پر غور کریں، n=3 (اشیاء کی تعداد)، r=2 (گروہ کا سائز)، لہٰذا ترتیبات کی تعداد $ {}^{3}_{2}P=\\frac{3!}{(3-2)!}=\\frac{3\\cdot 2\\cdot 1}{1!}=\\frac{3\\cdot 2\\cdot 1}{1}=6$ ہے',
    'پورتنۍ بېلګه په پام کې ونیسئ، n=3 (د شیانو شمېر)، r=2 (د ډلې اندازه)، نو د ترتیبونو شمېر $ {}^{3}_{2}P=\\frac{3!}{(3-2)!}=\\frac{3\\cdot 2\\cdot 1}{1!}=\\frac{3\\cdot 2\\cdot 1}{1}=6$ دی')
b.h('Example 1.1', 'مثال 1.1', 'بېلګه 1.1')
b.p('How many different three digit numbers can be formed from the digits 3, 4, 5, 6, 7, 8.',
    'ہندسوں 3، 4، 5، 6، 7، 8 سے کتنے مختلف تین ہندسی اعداد بنائے جا سکتے ہیں۔',
    'له 3، 4، 5، 6، 7، 8 رقمونو څخه څو بېلابېل درې رقمي عددونه جوړېدای شي.')
b.h(*SOL)
b.p('Here $n=6$, $r=3$, the number of permutations is given by', 'یہاں $n=6$، $r=3$، ترتیبات کی تعداد یہ ہے', 'دلته $n=6$، $r=3$، د ترتیبونو شمېر داسې دی')
b.eq(r'{}^{6}_{3}P=\frac{6!}{(6-3)!}=\frac{6!}{3!}=\frac{6\cdot 5\cdot 4\cdot 3!}{3!}=6\cdot 5\cdot 4=120')
b.h('Permutations when all objects are taken at a time (without repetition)', 'جب تمام اشیاء ایک وقت میں لی جائیں (بغیر تکرار) تو ترتیبات', 'کله چې ټول شیان په یو وخت کې واخیستل شي (پرته له تکرار) نو ترتیبونه')
b.p('When all of the given objects are considered at a time in the formation of groups i.e. $r=n$ then the total number of permutations $= {}^{n}_{n}P=n!$',
    'جب گروہ بنانے میں دی گئی تمام اشیاء ایک وقت میں لی جائیں یعنی $r=n$ تو ترتیبات کی کل تعداد $= {}^{n}_{n}P=n!$',
    'کله چې د ډلو په جوړولو کې ټول ورکړل شوي شیان په یو وخت کې ونیول شي یعنې $r=n$، نو د ترتیبونو ټول شمېر $= {}^{n}_{n}P=n!$')
b.h('Example 1.2', 'مثال 1.2', 'بېلګه 1.2')
b.p('How many different permutations can be made from the letters of the word “BOXER”?',
    'لفظ “BOXER” کے حروف سے کتنی مختلف ترتیبات بنائی جا سکتی ہیں؟',
    'د “BOXER” کلمې له تورو څخه څو بېلابېل ترتیبونه جوړېدای شي؟')
b.h(*SOL)
b.p('Here $r=n=5$, therefore, total number of permutations $=5!=5\\cdot 4\\cdot 3\\cdot 2\\cdot 1=120$',
    'یہاں $r=n=5$، لہٰذا ترتیبات کی کل تعداد $=5!=5\\cdot 4\\cdot 3\\cdot 2\\cdot 1=120$',
    'دلته $r=n=5$، نو د ترتیبونو ټول شمېر $=5!=5\\cdot 4\\cdot 3\\cdot 2\\cdot 1=120$')
b.h('Permutations when all objects are taken at a time (with repetition)', 'جب تمام اشیاء ایک وقت میں لی جائیں (تکرار کے ساتھ) تو ترتیبات', 'کله چې ټول شیان په یو وخت کې واخیستل شي (له تکرار سره) نو ترتیبونه')
b.p('When all of the given objects are considered at a time in the formation of groups and out of them $n_1$ are of one kind, $n_2$ are of second kind… $n_k$ are of the $k^{th}$ kind, then the total number of permutations is given by',
    'جب گروہ بنانے میں تمام دی گئی اشیاء ایک وقت میں لی جائیں اور ان میں سے $n_1$ ایک قسم کی، $n_2$ دوسری قسم کی … $n_k$ اشیاء $k^{th}$ قسم کی ہوں، تو ترتیبات کی کل تعداد یہ ہے',
    'کله چې د ډلو په جوړولو کې ټول ورکړل شوي شیان په یو وخت کې ونیول شي او له هغو څخه $n_1$ د یو ډول، $n_2$ د دویم ډول … $n_k$ د $k^{th}$ ډول وي، نو د ترتیبونو ټول شمېر دا دی')
b.eq(r'\binom{n}{n_1,n_2,\cdots,n_k}=\frac{n!}{n_1!\,n_2!\cdots n_k!},\quad\text{where } n_1+n_2+\ldots+n_k=n')
b.h('Example 1.3', 'مثال 1.3', 'بېلګه 1.3')
b.p('How many different permutations can be made from the letters of the word “STATISTICS”?',
    'لفظ “STATISTICS” کے حروف سے کتنی مختلف ترتیبات بنائی جا سکتی ہیں؟',
    'د “STATISTICS” کلمې له تورو څخه څو بېلابېل ترتیبونه جوړېدای شي؟')
b.h(*SOL)
b.p("Here $n=10$ (total number of letters), $n_1=3$ (number of S's), $n_2=3$ (number of T's), $n_3=2$ (number of I's), $n_4=1$ (number of A's) and $n_5=1$ (number of C's). Therefore, the required number of permutations is given by",
    'یہاں $n=10$ (حروف کی کل تعداد)، $n_1=3$ (S کی تعداد)، $n_2=3$ (T کی تعداد)، $n_3=2$ (I کی تعداد)، $n_4=1$ (A کی تعداد) اور $n_5=1$ (C کی تعداد)۔ لہٰذا مطلوبہ ترتیبات کی تعداد یہ ہے',
    'دلته $n=10$ (د تورو ټول شمېر)، $n_1=3$ (د S شمېر)، $n_2=3$ (د T شمېر)، $n_3=2$ (د I شمېر)، $n_4=1$ (د A شمېر) او $n_5=1$ (د C شمېر). نو د ترتیبونو اړین شمېر دا دی')
b.mlines([r'\binom{n}{n_1,n_2,n_3,n_4,n_5}=\frac{n!}{n_1!\,n_2!\,n_3!\,n_4!\,n_5!}',
          r'\binom{10}{3,3,2,1,1}=\frac{10!}{3!\,3!\,2!\,1!\,1!}=\frac{10\cdot 9\cdot 8\cdot 7\cdot 6\cdot 5\cdot 3\cdot 2\cdot 1}{3\cdot 2\cdot 1\cdot 3\cdot 2\cdot 1\cdot 2\cdot 1\cdot 1\cdot 1}=50400'])
b.h('Rule of combination', 'انتخاب (Combination) کا قاعدہ', 'د کمبینېشن (ټاکنې) قاعده')
b.p('The groups which can be made from a given number of objects by taking together some or all of the objects at a time without regard the order of the objects are called combinations. For example, if there are three objects A, B and C then combinations of size two will be AB, AC, and BC. Generally if there are “n” objects then the total number of combinations of size “r” is given by the formula $ {}^{n}_{r}C=\\frac{n!}{(n-r)!\\,r!}$',
    'دی گئی اشیاء میں سے کچھ یا تمام اشیاء کو ایک وقت میں ان کی ترتیب کا لحاظ کیے بغیر اکٹھا لے کر جو گروہ بنائے جا سکتے ہیں، انہیں انتخابات (combinations) کہتے ہیں۔ مثلاً اگر تین اشیاء A، B اور C ہوں تو دو کے سائز کے انتخابات AB، AC اور BC ہوں گے۔ عام طور پر اگر “n” اشیاء ہوں تو “r” سائز کے انتخابات کی کل تعداد اس فارمولا سے ملتی ہے $ {}^{n}_{r}C=\\frac{n!}{(n-r)!\\,r!}$',
    'هغه ډلې چې له ورکړل شویو شیانو څخه د شیانو د ترتیب له پام کې نیولو پرته په یو وخت کې د ځینو یا ټولو شیانو په یوځای اخیستلو جوړېږي، کمبینېشنونه (ټاکنې) بلل کېږي. د بېلګې په توګه که درې شیان A، B او C وي، نو د دوو په اندازه ټاکنې به AB، AC او BC وي. په عمومي ډول که “n” شیان وي، نو د “r” اندازې د ټاکنو ټول شمېر له دې فورمول څخه لاسته راځي $ {}^{n}_{r}C=\\frac{n!}{(n-r)!\\,r!}$')
b.p('By formula the number of combinations for above example is equal to', 'فارمولا کے ذریعے اوپر کی مثال کے انتخابات کی تعداد یہ ہے', 'د فورمول له مخې د پورتنۍ بېلګې د ټاکنو شمېر دا دی')
b.eq(r'{}^{3}_{2}C=\frac{3!}{(3-2)!\,2!}=\frac{3\cdot 2\cdot 1}{1!\,2\cdot 1}=3')
b.p('It can be deduced that:', 'اس سے یہ نتیجہ نکالا جا سکتا ہے کہ:', 'له دې څخه دا پایله اخیستل کېدای شي چې:')
b.mlines([r'\binom{n}{n}=\binom{n}{0}=1', r'\binom{n}{r}=\binom{n}{n-r}', r'\binom{n}{1}=\binom{n}{n-1}=n', r'\binom{n}{r}+\binom{n}{r-1}=\binom{n+1}{r}'], kind='list')
b.h('Example 1.4', 'مثال 1.4', 'بېلګه 1.4')
b.p('In how many ways a committee of three men can be selected from seven men?',
    'سات آدمیوں میں سے تین آدمیوں کی ایک کمیٹی کتنے طریقوں سے منتخب کی جا سکتی ہے؟',
    'له اوو سړیو څخه د درېیو سړیو یوه کمېټه په څو ډوله ټاکل کېدای شي؟')
rec = b.build('stat12-p006-permutations', 'Permutation examples and the rule of combination', 'ترتیبات کی مثالیں اور انتخاب کا قاعدہ', 'د ترتیب بېلګې او د ټاکنې قاعده', 6, [3, 4])

if __name__ == '__main__':
    save(6, [(1, rec)])
