"""PDF68 printed 127–128: Example 4.3 solutions (a)–(l), each with its shaded standard normal curve; 4.2.7 inverse use of the area table."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import normal_shaded

K = dict(w=300, h=120, zlabel='Z')
parts = [
    ('a', r'P[-\infty<Z<\infty]=1', -3.6, 3.6, dict(marks=(0,), labels=((0, '0'),), notes=((-0.45, .45, '0.5'), (0.45, .45, '0.5')))),
    ('b', r'P[0<Z<\infty]=0.5', 0, None, dict(marks=(0,), labels=((0, '0'),), notes=((0.6, .45, '0.5'),))),
    ('c', r'P[-\infty<Z<0]=0.5', None, 0, dict(marks=(0,), labels=((0, '0'),), notes=((-0.6, .45, '0.5'),))),
    ('d', r'P[0<Z<2.63]=0.4957', 0, 2.63, dict(marks=(0, 2.63), labels=((0, '0'), (2.63, '2.63')))),
    ('e', r'P[-1.45<Z<0]=0.4265', -1.45, 0, dict(marks=(-1.45, 0), labels=((-1.45, '−1.45'), (0, '0')))),
    ('f', r'P[1<Z<1.5]=P[0<Z<1.5]-P[0<Z<1]=0.4332-0.3413=0.0919', 1, 1.5, dict(marks=(0, 1, 1.5), labels=((0, '0'), (1, '1'), (1.5, '1.5')))),
    ('g', r'P[Z\ge 1.64]=P[0<Z<\infty]-P[0<Z<1.64]=0.5-0.4498=0.0502', 1.64, None, dict(marks=(0, 1.64), labels=((0, '0'), (1.64, '1.64')))),
    ('h', r'P[-1.96<Z<-1.06]=P[-1.96<Z<0]-P[-1.06<Z<0]=0.4750-0.3554=0.1196', -1.96, -1.06, dict(marks=(-1.96, -1.06, 0), labels=((-1.96, '−1.96'), (-1.06, '−1.06'), (0, '0')))),
    ('i', r'P[Z<-1.64]=P[0<Z<\infty]-P[-1.64<Z<0]=0.5-0.4498=0.0502', None, -1.64, dict(marks=(-1.64, 0), labels=((-1.64, '−1.64'), (0, '0')))),
    ('j', r'P[-1.70<Z<1.25]=P[-1.70<Z<0]+P[0<Z<1.25]=0.4554+0.3944=0.8498', -1.70, 1.25, dict(marks=(-1.70, 0, 1.25), labels=((-1.70, '−1.70'), (0, '0'), (1.25, '1.25')))),
    ('k', r'P[Z>-2.46]=P[-2.46<Z<0]+P[0<Z<\infty]=0.4931+0.5=0.9931', -2.46, None, dict(marks=(-2.46, 0), labels=((-2.46, '−2.46'), (0, '0')))),
    ('l', r'P[Z<2.11]=P[-\infty<Z<0]+P[0<Z<2.11]=0.5+0.4826=0.9826', None, 2.11, dict(marks=(0, 2.11), labels=((0, '0'), (2.11, '2.11')))),
]
b = Builder()
for letter, latex, a, z1, kw in parts:
    svg = normal_shaded(a, z1, label=f'Example 4.3 ({letter}) shaded area', **K, **kw)
    text = f'{letter}. ${latex}$'
    b.vpara(f'stat12-ex4-3-{letter}', svg, text, text, text)
sol = b.build('stat12-p068-example-4-3-solutions', 'Example 4.3 — solutions (a)–(l)', 'مثال 4.3 — حل (a)–(l)', 'بېلګه 4.3 — حلونه (a)–(l)', 68, [127, 128])

c = Builder()
c.h('4.2.7 Inverse use of table of areas under standard normal curve', '4.2.7 معیاری نارمل منحنی کے نیچے رقبوں کے جدول کا الٹا استعمال', '4.2.7 د معیاري نورمال منحني لاندې د مساحتونو د جدول معکوس کارول')
c.p('Hope you will be able to determine the interval probability for the standard normal variable Z from the area table. Now we try to reverse the process and determine a value or values of Z corresponding to a given area (probability) from the same areas table. This is called inverse use of the area table.',
    'امید ہے آپ رقبے کے جدول سے معیاری نارمل متغیر Z کا وقفہ احتمال معلوم کر سکیں گے۔ اب ہم اس عمل کو الٹنے کی کوشش کرتے ہیں اور اسی رقبوں کے جدول سے دیے گئے رقبے (احتمال) کے مطابق Z کی قیمت یا قیمتیں معلوم کرتے ہیں۔ اسے رقبے کے جدول کا الٹا استعمال کہتے ہیں۔',
    'هیله ده چې د مساحت له جدول څخه به د معیاري نورمال متغیر Z د واټن احتمال وټاکلای شئ. اوس هڅه کوو چې دا بهیر معکوس کړو او له همدې مساحتونو جدول څخه د ورکړل شوي مساحت (احتمال) سره سم د Z قیمت یا قیمتونه وټاکو. دې ته د مساحت د جدول معکوس کارول وایي.')
inv = c.build('stat12-p068-inverse-table', '4.2.7 Inverse use of the area table', '4.2.7 رقبے کے جدول کا الٹا استعمال', '4.2.7 د مساحت د جدول معکوس کارول', 68, [128])
issues = [{'id': 'stat12-p128-part-k-sign', 'unit': 4, 'printedPage': 128, 'description': 'Example 4.3(k) is asked as P[Z < −2.46] on page 126 but solved as P[Z > −2.46] on page 128; both printed forms retained. Part (j) is asked with −1.7 and solved with −1.70.'}]

if __name__ == '__main__':
    save(68, [(4, sol), (4, inv)], issues=issues)
