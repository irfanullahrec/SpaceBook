from fractions import Fraction
out = ['@printed 82', '@deco Cartoon star mascot on the "I Have Learnt" banner.',
       'q 4 | Convert the following fractions into percentage. || درج ذیل کسور کو فیصد میں تبدیل کریں۔ || لاندې کسرونه په سلنه واړوئ.']
for l, (n, d) in zip('abcdefghij', [(1, 10), (2, 5), (4, 10), (9, 25), (3, 20), (21, 50), (1, 5), (7, 20), (9, 10), (6, 25)]):
    k = 100 // d
    out.append(rf'qp {l} | $\dfrac{{{n}}}{{{d}}}$')
    out.append(rf'sol {n * k}% ## Make the denominator 100: $\dfrac{{{n} \times {k}}}{{{d} \times {k}}} = \dfrac{{{n * k}}}{{100}} = {n * k}\%$. || نسب نما 100 بنائیں: $\dfrac{{{n} \times {k}}}{{{d} \times {k}}} = \dfrac{{{n * k}}}{{100}} = {n * k}\%$۔ || مخرج 100 کړئ: $\dfrac{{{n} \times {k}}}{{{d} \times {k}}} = \dfrac{{{n * k}}}{{100}} = {n * k}\%$.')
out.append('q 5 | Convert the following decimals into percentage form. || درج ذیل اعشاریہ اعداد کو فیصد کی صورت میں تبدیل کریں۔ || لاندې اعشاري عددونه د سلنې په بڼه واړوئ.')
for l, x in zip('abcdefghij', ['0.06', '0.14', '0.23', '0.34', '0.43', '0.55', '0.63', '0.71', '0.98', '0.3']):
    p = int(round(float(x) * 100))
    out.append(f'qp {l} | {x}')
    out.append(rf'sol {p}% ## Multiply by 100 (move the point two places right): {x} × 100 = {p}%. || 100 سے ضرب دیں (نقطہ دو مقام دائیں): {x} × 100 = {p}%۔ || په 100 کې ضرب کړئ (ټکی دوه ځایه ښي لوري ته): {x} × 100 = {p}%.')
out += [
    'q 6 | Sajid scored 365 marks out of 500. What percentage did he score? || ساجد نے 500 میں سے 365 نمبر حاصل کیے۔ اس نے کتنے فیصد نمبر حاصل کیے؟ || ساجد له 500 څخه 365 نمرې واخیستې. څو سلنه یې واخیسته؟',
    r'sol 73% ## $\dfrac{365}{500} = \dfrac{365 \div 5}{500 \div 5} = \dfrac{73}{100} = 73\%$. || $\dfrac{365}{500} = \dfrac{73}{100} = 73\%$۔ || $\dfrac{365}{500} = \dfrac{73}{100} = 73\%$.',
    'q 7 | There are 40 students in a class. If 5% are absent on Monday, calculate: || ایک جماعت میں 40 طلبہ ہیں۔ اگر پیر کو 5% غیر حاضر ہوں تو معلوم کریں: || په یوه ټولګي کې 40 زده کوونکي دي. که د دوشنبې په ورځ 5% غیر حاضر وي، حساب کړئ:',
    'qp a | the number of absent students || غیر حاضر طلبہ کی تعداد || د غیر حاضرو زده کوونکو شمېر',
    r'sol 2 students ## $\dfrac{5}{100} \times 40 = 2$. || $\dfrac{5}{100} \times 40 = 2$۔ || $\dfrac{5}{100} \times 40 = 2$.',
    'qp b | the number of present students || حاضر طلبہ کی تعداد || د حاضرو زده کوونکو شمېر',
    'sol 38 students ## 40 − 2 = 38. || 40 − 2 = 38۔ || 40 − 2 = 38.',
    'q 8 | In an exam, 450 students appeared. 25% got first division, 55% got second division and the rest just passed the exam. Find the number of students who just passed the exam. || ایک امتحان میں 450 طلبہ شریک ہوئے۔ 25% نے فرسٹ ڈویژن، 55% نے سیکنڈ ڈویژن حاصل کی اور باقی صرف پاس ہوئے۔ صرف پاس ہونے والے طلبہ کی تعداد معلوم کریں۔ || په یوه ازموینه کې 450 زده کوونکو ګډون وکړ. 25% لومړۍ درجه، 55% دوهمه درجه واخیسته او پاتې یوازې بریالي شول. د هغو زده کوونکو شمېر معلوم کړئ چې یوازې بریالي شول.',
    r'sol 90 students ## Just passed = 100% − 25% − 55% = 20%; $\dfrac{20}{100} \times 450 = 90$. || صرف پاس = 100% − 25% − 55% = 20%؛ $\dfrac{20}{100} \times 450 = 90$۔ || یوازې بریالي = 100% − 25% − 55% = 20%؛ $\dfrac{20}{100} \times 450 = 90$.',
    'q 9 | 12% of apples in a basket are red. Write this percentage in fraction and decimal. || ایک ٹوکری میں 12% سیب سرخ ہیں۔ اس فیصد کو کسر اور اعشاریہ میں لکھیں۔ || په یوه ټوکرۍ کې 12% مڼې سرې دي. دا سلنه په کسر او اعشاریه ولیکئ.',
    r'sol $\dfrac{3}{25}$ and 0.12 ## $12\% = \dfrac{12}{100} = \dfrac{3}{25}$ and $\dfrac{12}{100} = 0.12$. || $12\% = \dfrac{12}{100} = \dfrac{3}{25}$ اور $0.12$۔ || $12\% = \dfrac{12}{100} = \dfrac{3}{25}$ او $0.12$.',
    "q 10 | A tank can hold 85 liters of water. It's 40% filled. What percentage of the tank is empty? Write the answer in decimal and fraction. || ایک ٹینکی میں 85 لیٹر پانی آ سکتا ہے۔ یہ 40% بھری ہوئی ہے۔ ٹینکی کا کتنا فیصد خالی ہے؟ جواب اعشاریہ اور کسر میں لکھیں۔ || یوه ټانکۍ 85 لیټره اوبه نیولی شي. 40% ډکه ده. د ټانکۍ څو سلنه تشه ده؟ ځواب په اعشاریه او کسر ولیکئ.",
    r'sol 60% = 0.6 = $\dfrac{3}{5}$ ## Empty part = 100% − 40% = 60% = $\dfrac{60}{100}$ = 0.6 = $\dfrac{3}{5}$ (that is 51 litres of the 85 litres). || خالی حصہ = 100% − 40% = 60% = 0.6 = $\dfrac{3}{5}$ (یعنی 85 میں سے 51 لیٹر)۔ || تشه برخه = 100% − 40% = 60% = 0.6 = $\dfrac{3}{5}$ (یعنې له 85 څخه 51 لیټره).',
    'endexercise',
    '@sec u4-summary | I Have Learnt || میں نے سیکھا || ما زده کړل',
    '# I Have Learnt || میں نے سیکھا || ما زده کړل',
    '- comparing numbers up to 3 - digit with 2 decimal places using signs <, > or =. || 2 اعشاری مقامات والے 3 ہندسوں تک کے اعداد کا علامات <، > یا = سے موازنہ کرنا۔ || د 2 اعشاري ځایونو لرونکو تر 3 رقمونو پورې عددونو پرتله د <، > یا = نښو سره.',
    '- arranging numbers up to 3 - digit numbers with 2 decimal places in ascending and descending order. || 2 اعشاری مقامات والے 3 ہندسوں تک کے اعداد کو صعودی اور نزولی ترتیب میں لکھنا۔ || د 2 اعشاري ځایونو لرونکي تر 3 رقمونو پورې عددونه په زیاتېدونکي او کمېدونکي ترتیب کېښودل.',
    '- adding and subtracting in 4 - digit numbers up to 3 - decimal places. || 3 اعشاری مقامات تک کے 4 ہندسی اعداد جمع اور تفریق کرنا۔ || تر 3 اعشاري ځایونو پورې د 4 رقمي عددونو جمع او تفریق.',
    '- multiplying a 3 - digit number up to 2 decimal places by 10, 100, and 1000 || 2 اعشاری مقامات تک کے 3 ہندسی عدد کو 10، 100 اور 1000 سے ضرب دینا || تر 2 اعشاري ځایونو پورې 3 رقمي عدد په 10، 100 او 1000 کې ضربول',
    'box note | Vocabulary || ذخیرۂ الفاظ || لغتونه',
    'table Vocabulary || ذخیرۂ الفاظ || لغتونه',
    'tr | decimal', 'tr | fraction', 'tr | decimal Point', 'tr | percentage', 'tr | decimal place', 'tr | estimation', 'tr | round-off',
    'endtable', 'endbox']
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p088.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
