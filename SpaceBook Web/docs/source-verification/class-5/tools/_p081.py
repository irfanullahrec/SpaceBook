from decimal import Decimal
from fractions import Fraction
out = ['@printed 75',
       '@deco Cartoon book mascot on "Exercise 5"; cartoon boy beside the speech bubble; picture of a school building with a clock tower and a path.',
       'exercise 5',
       'q 1 | Convert the following fractions into decimals. || درج ذیل کسور کو اعشاریہ میں تبدیل کریں۔ || لاندې کسرونه په اعشاریو واړوئ.']
for l, (n, d) in zip('abcdefghijkl', [(45, 2), (19, 25), (7, 40), (33, 100), (97, 8), (78, 8), (34, 25), (2, 5), (55, 16), (69, 30), (72, 45), (99, 55)]):
    v = format((Decimal(n) / Decimal(d)).normalize(), 'f')
    out.append(rf'qp {l} | $\dfrac{{{n}}}{{{d}}}$')
    out.append(f'sol {v} ## Divide the numerator by the denominator: {n} ÷ {d} = {v}. || شمار کنندہ کو نسب نما سے تقسیم کریں: {n} ÷ {d} = {v}۔ || صورت پر مخرج ووېشئ: {n} ÷ {d} = {v}.')
out += [
    r'q 2 | Noman ate $\dfrac{1}{8}$ of a pizza. How can we write this in decimal form? || نعمان نے پیزا کا $\dfrac{1}{8}$ حصہ کھایا۔ ہم اسے اعشاریہ کی صورت میں کیسے لکھ سکتے ہیں؟ || نعمان د پیزا $\dfrac{1}{8}$ برخه وخوړه. موږ دا په اعشاري بڼه څنګه لیکلی شو؟',
    'sol 0.125 ## 1 ÷ 8: write 1 as 1.000; 10 ÷ 8 = 1 r 2, 20 ÷ 8 = 2 r 4, 40 ÷ 8 = 5 → 0.125. || 1 ÷ 8: 1 کو 1.000 لکھیں؛ 10 ÷ 8 = 1 باقی 2، 20 ÷ 8 = 2 باقی 4، 40 ÷ 8 = 5 → 0.125۔ || 1 ÷ 8: 1 د 1.000 په بڼه ولیکئ؛ 10 ÷ 8 = 1 پاتې 2، 20 ÷ 8 = 2 پاتې 4، 40 ÷ 8 = 5 → 0.125.',
    'endexercise',
    '@sec u4-round | Rounding-off Decimals || اعشاریہ اعداد کو مدور کرنا || د اعشاري عددونو ګردول',
    '# Rounding-off Decimals || اعشاریہ اعداد کو مدور کرنا || د اعشاري عددونو ګردول',
    'box note',
    'p The school library is at the distance of 1.47 kilometres from the laboratory. Write this distance in kilometers to the nearest tenths. || اسکول کی لائبریری لیبارٹری سے 1.47 کلومیٹر کے فاصلے پر ہے۔ یہ فاصلہ کلومیٹر میں قریب ترین دسویں تک لکھیں۔ || د ښوونځي کتابتون له لابراتوار څخه 1.47 کیلومتره لرې دی. دا واټن په کیلومترو کې تر نږدې لسمې پورې ولیکئ.',
    'endbox',
    'p Find the distance to the nearest tenth, we need to round-off this distance to one decimal place. || فاصلہ قریب ترین دسویں تک معلوم کرنے کے لیے ہمیں اسے ایک اعشاری مقام تک مدور کرنا ہوگا۔ || د واټن تر نږدې لسمې پورې معلومولو لپاره باید دا واټن تر یوه اعشاري ځای پورې ګرد کړو.',
    r'eq 1.\textcircled{4}\,\underline{7} = 1.5',
    'p Circle the digit at the tenths place, || دسویں کے مقام کے ہندسے پر دائرہ لگائیں۔ || د لسمو د ځای په رقم کړۍ وکړئ.',
    'p Look at the digit next to the tenths place(i.e. hundredths place). If this digit is 5 or greater than 5, we will add 1 to the tenths digit and remove all the next digits towards its right. If this digit is smaller than 5, we will write the tenths place digit as it is and remove all the digits towards its right. || دسویں کے مقام کے ساتھ والے ہندسے (یعنی سوویں کے مقام) کو دیکھیں۔ اگر یہ ہندسہ 5 یا 5 سے بڑا ہو تو دسویں کے ہندسے میں 1 جمع کریں اور اس کے دائیں طرف کے تمام ہندسے ہٹا دیں۔ اگر یہ ہندسہ 5 سے چھوٹا ہو تو دسویں کے مقام کا ہندسہ جوں کا توں لکھیں اور اس کے دائیں طرف کے تمام ہندسے ہٹا دیں۔ || د لسمو د ځای څنګ ته رقم (یعنې د سلمو ځای) ته وګورئ. که دا رقم 5 یا له 5 څخه لوی وي، د لسمو رقم ته 1 جمع کړئ او د هغه ښي لوري ټول رقمونه لرې کړئ. که دا رقم له 5 څخه کوچنی وي، د لسمو د ځای رقم هماغسې ولیکئ او د هغه ښي لوري ټول رقمونه لرې کړئ.',
    r'p In 1.47, the digit next to 4 is 7 which is greater than 5, so: $1.47 \approx 1.5$ || 1.47 میں 4 کے ساتھ والا ہندسہ 7 ہے جو 5 سے بڑا ہے، اس لیے: $1.47 \approx 1.5$ || په 1.47 کې د 4 څنګ ته رقم 7 دی چې له 5 څخه لوی دی، نو: $1.47 \approx 1.5$',
]
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p081.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
