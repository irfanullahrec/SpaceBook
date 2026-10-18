from statlib import *
c=cell
U='collection-presentation'
def pid(n,k): return f'stat11-s{n:03}-{k}'
# ---------- scan 51 (printed 43) ----------
s=page(51,U,'43','Examples 1.21, 1.22 · 1.7.1 Rules for Σ notation','مثالیں 1.21، 1.22 · 1.7.1 Σ علامت کے قواعد','بېلګې 1.21، 1.22 · 1.7.1 د Σ نښې قواعد','sigma-rules-1')
F=Flow(s)
head(s,'ex21','Example: 1.21','مثال: 1.21','بېلګه: 1.21',exampleId='stat11-ex-1-21')
add(s,'q21','Suppose x = 2, 4, 6, 3. Calculate Σx, Σx², (Σx)².','فرض کریں x = 2, 4, 6, 3۔ Σx، Σx²، (Σx)² حساب کریں۔','فرض کړئ x = 2, 4, 6, 3. Σx، Σx²، (Σx)² محاسبه کړئ.',role='question',exampleId='stat11-ex-1-21')
head(s,'sol21','Solution:','حل:','حل:',exampleId='stat11-ex-1-21')
s['tables']=[table('Example 1.21','مثال 1.21','بېلګه 1.21',[c('x'),c('x²')],[[c('2'),c('4')],[c('4'),c('16')],[c('6'),c('36')],[c('3'),c('9')],[c('Σx = 15'),c('Σx² = 65')]],exampleId='stat11-ex-1-21',role='solution'),
 table('Example 1.22','مثال 1.22','بېلګه 1.22',[c('x'),c('2x')],[[c('1'),c('2')],[c('2'),c('4')],[c('3'),c('6')],[c('4'),c('8')],[c('Σx = 10'),c('Σ2x = 20')]],exampleId='stat11-ex-1-22',role='solution')]
F.rest();F.tb(0)
F.e('a1',r'\text{and }\left(\sum x\right)^2=(15)^2=225.','and (Σx)² = (15)² = 225.',exampleId='stat11-ex-1-21')
head(s,'h171','1.7.1 Rules for Σ notation','1.7.1 Σ علامت کے قواعد','1.7.1 د Σ نښې قواعد')
F.rest()
F.e('r1',r'\text{i.}\ \sum_{i=1}^{n}c=nc',"i. Σ (i = 1 to n) c = nc")
add(s,'r1t','where c is a constant. It means that when Σ is applied on a constant it will be converted to n.','جہاں c ایک مستقلہ ہے۔ اس کا مطلب ہے کہ جب Σ کو کسی مستقلے پر لاگو کیا جائے تو وہ n میں تبدیل ہو جائے گا۔','چېرته چې c یو ثابت دی. پدې معنا چې کله Σ پر یو ثابت پلی شي نو هغه به په n بدل شي.')
F.rest()
F.e('r2',r'\text{ii.}\ \sum_{i=1}^{n}c\,x_i=c\sum_{i=1}^{n}x_i',"ii. Σ (i = 1 to n) c xi = c Σ (i = 1 to n) xi")
add(s,'r2t','where c is a constant.','جہاں c ایک مستقلہ ہے۔','چېرته چې c یو ثابت دی.')
add(s,'r2u','It means that when Σ is applied on the product of a constant and variable, constant can be written outside the Σ notation.','اس کا مطلب ہے کہ جب Σ کو کسی مستقلے اور متغیر کے حاصلِ ضرب پر لاگو کیا جائے تو مستقلے کو Σ علامت سے باہر لکھا جا سکتا ہے۔','پدې معنا چې کله Σ د یو ثابت او متغیر په ضرب حاصل پلی شي نو ثابت د Σ له نښې بهر لیکل کېدای شي.')
head(s,'ex22','Example: 1.22','مثال: 1.22','بېلګه: 1.22',exampleId='stat11-ex-1-22')
F.rest();F.tb(1)
F.e('a2',r'\text{and }2\sum x=2\times10=20','and 2Σx = 2 × 10 = 20',exampleId='stat11-ex-1-22')
add(s,'a2t','This implies that Σ2x = 2Σx where c = 2 is a constant.','اس سے ظاہر ہوتا ہے کہ Σ2x = 2Σx جہاں c = 2 ایک مستقلہ ہے۔','پدې معنا چې Σ2x = 2Σx چېرته چې c = 2 یو ثابت دی.')
F.rest()
F.e('r3',r'\text{iii.}\ \sum_{i=1}^{n}(x_i+y_i)=\sum_{i=1}^{n}x_i+\sum_{i=1}^{n}y_i',"iii. Σ (i = 1 to n) (xi + yi) = Σ xi + Σ yi")
F.done()
s['sourceNote']='Printed page 43. The foot of the scan shows a ghost of the page-number bar. A small ink mark is ignored. Header graphics and watermark excluded.'
s['vocabulary']={'constant':dict(ur='مستقلہ',ps='ثابت')}
save(s)
# ---------- scan 52 (printed 44) ----------
s=page(52,U,'44','Example 1.23 · rule iv · 1.7.2 Double summation notation · Example 1.24','مثال 1.23 · قاعدہ iv · 1.7.2 دوہرے مجموعے کی علامت · مثال 1.24','بېلګه 1.23 · قاعده iv · 1.7.2 د دوه‌ګونې مجموعې نښه · بېلګه 1.24','double-sum-1')
F=Flow(s)
head(s,'ex23','Example: 1.23','مثال: 1.23','بېلګه: 1.23',exampleId='stat11-ex-1-23')
add(s,'q23','Verify rule number (iii) above by considering the following data','درج ذیل اعداد و شمار پر غور کر کے اوپر دیے گئے قاعدہ نمبر (iii) کی تصدیق کریں','د لاندې معلوماتو په پام کې نیولو سره پورتنی قاعده شمېره (iii) تصدیق کړئ',role='question',exampleId='stat11-ex-1-23')
s['tables']=[table('Example 1.23','مثال 1.23','بېلګه 1.23',[c('x'),c('y'),c('x + y')],[[c('3'),c('5'),c('8')],[c('1'),c('3'),c('4')],[c('7'),c('4'),c('11')],[c('4'),c('2'),c('6')],[c('Σx = 15'),c('Σy = 14'),c('Σ(x + y) = 29')]],exampleId='stat11-ex-1-23',role='solution'),
 table('Layout of values with double subscript x_ij','دوہرے زیرنوشت x_ij والی قدروں کی ترتیب','د دوه‌ګونې لاندې‌لیک x_ij لرونکو ارزښتونو ترتیب',[c(''),c('X1'),c('X2'),c('…'),c('Xj'),c('…'),c('Xm')],[[c('1'),c('X11'),c('X12'),c('…'),c('X1j'),c('…'),c('X1m')],[c('2'),c('X21'),c('X22'),c('…'),c('X2j'),c('…'),c('X2m')],[c(''),c(''),c(''),c(''),c(''),c(''),c('')],[c('i'),c('Xi1'),c('Xi2'),c('…'),c('Xij'),c('…'),c('Xim')],[c(''),c(''),c(''),c(''),c(''),c(''),c('')],[c('n'),c('Xn1'),c('Xn2'),c('…'),c('Xnj'),c('…'),c('Xnm')]])]
head(s,'sol23','Solution:','حل:','حل:',exampleId='stat11-ex-1-23')
s['paras']=[p for p in s['paras'] if p['id']!=pid(52,'sol23')]
F.rest();F.tb(0)
add(s,'a1','Also Σx + Σy = 15 + 14 = 29. Hence proved that, Σ(x + y) = Σx + Σy','نیز Σx + Σy = 15 + 14 = 29۔ لہٰذا ثابت ہوا کہ Σ(x + y) = Σx + Σy','همداراز Σx + Σy = 15 + 14 = 29. نو ثابته شوه چې Σ(x + y) = Σx + Σy',role='solution',exampleId='stat11-ex-1-23')
F.rest()
F.e('r4',r'\text{iv.}\ \sum_{i=1}^{n}(x_i-y_i)=\sum_{i=1}^{n}x_i-\sum_{i=1}^{n}y_i',"iv. Σ (i = 1 to n) (xi − yi) = Σ xi − Σ yi")
head(s,'h172','1.7.2 Double summation notation','1.7.2 دوہرے مجموعے کی علامت','1.7.2 د دوه‌ګونې مجموعې نښه')
add(s,'t172','xij: It denotes values of a variable with double subscript notation, j = 1, 2,…,m denotes serial number of the variable and i = 1, 2,…,n denotes values of the variable that is,','xij: یہ دوہرے زیرنوشت علامت کے ساتھ متغیر کی قدروں کو ظاہر کرتا ہے، j = 1, 2,…,m متغیر کا سلسلہ وار نمبر ظاہر کرتا ہے اور i = 1, 2,…,n متغیر کی قدروں کو ظاہر کرتا ہے یعنی،','xij: دا د دوه‌ګونې لاندې‌لیک نښې سره د متغیر ارزښتونه ښيي، j = 1, 2,…,m د متغیر لړ شمېره ښيي او i = 1, 2,…,n د متغیر ارزښتونه ښيي یعنې،')
F.rest();F.tb(1)
add(s,'t172b','Where x11 means first observation of the first variable, x12 means first observation of the second and so on. Here we need two summation notations, one for representing variables and second for values of the variables , that is','جہاں x11 پہلے متغیر کے پہلے مشاہدے کو ظاہر کرتا ہے، x12 دوسرے متغیر کے پہلے مشاہدے کو ظاہر کرتا ہے اور اسی طرح۔ یہاں ہمیں دو مجموعہ علامتوں کی ضرورت ہے، ایک متغیرات کو ظاہر کرنے کے لیے اور دوسری متغیرات کی قدروں کے لیے، یعنی','دلته x11 د لومړي متغیر لومړۍ کتنه ښيي، x12 د دویم متغیر لومړۍ کتنه ښيي او همداسې نور. دلته موږ ته دوه د مجموعې نښو ته اړتیا ده، یوه د متغیرونو د ښودلو لپاره او دویمه د متغیرونو د ارزښتونو لپاره، یعنې')
F.rest()
F.e('d1',r'\sum_{i=1}^{n}\sum_{i=1}^{m}x_{ij}=x_{11}+x_{12}+\cdots+x_{nm}\ ,\ \text{means sum of all values.}','Σ (i = 1 to n) Σ (i = 1 to m) xij = x11 + x12 + ⋯ + xnm, means sum of all values.')
head(s,'ex24','Example: 1.24','مثال: 1.24','بېلګه: 1.24',exampleId='stat11-ex-1-24')
add(s,'q24','Find ΣΣ xij for the data given below;','نیچے دیے گئے اعداد و شمار کے لیے ΣΣ xij معلوم کریں؛','د لاندې ورکړل شویو معلوماتو لپاره ΣΣ xij ومومئ؛',role='question',exampleId='stat11-ex-1-24',sourceGap=dict(note='The data table of Example 1.24 is on the next page.'))
F.done()
s['sourceNote']='Printed page 44. The double-sum expression is printed with the inner index "i=1" for both sums (a misprint for j=1) and is retained. The first row of the xij layout table is a header (X1 … Xm) with the row labels 1, 2, i, n in the first column and two blank spacer rows. Header graphics and watermark excluded.'
s['vocabulary']={'double subscript':dict(ur='دوہرا زیرنوشت',ps='دوه‌ګونی لاندې‌لیک')}
save(s)
# ---------- scan 53 (printed 45) ----------
s=page(53,U,'45','Example 1.24 data · Rules for double summation · 1.7.3 Product notation · Example 1.25','مثال 1.24 کے اعداد · دوہرے مجموعے کے قواعد · 1.7.3 حاصلِ ضرب کی علامت · مثال 1.25','د بېلګې 1.24 معلومات · د دوه‌ګونې مجموعې قواعد · 1.7.3 د ضرب نښه · بېلګه 1.25','double-sum-product')
F=Flow(s)
s['tables']=[table('Example 1.24: values x_ij (rows i, columns j) with totals','مثال 1.24: قدریں x_ij (قطاریں i، کالم j) مع میزان','بېلګه 1.24: ارزښتونه x_ij (کتارونه i، ستونونه j) له مجموعو سره',[c('i \\ j'),c('1'),c('2'),c('3'),c('Total','کل','ټول')],[[c('1'),c('3'),c('5'),c('2'),c('10')],[c('2'),c('0'),c('7'),c('1'),c('8')],[c('3'),c('4'),c('3'),c('9'),c('16')],[c('Total','کل','ټول'),c('7'),c('15'),c('12'),c('ΣΣ xij = 34')]],exampleId='stat11-ex-1-24',role='solution')]
F.tb(0)
add(s,'hr','Rules for double summation notation','دوہرے مجموعے کی علامت کے قواعد','د دوه‌ګونې مجموعې د نښې قواعد',kind='heading')
F.rest()
F.e('d1',r'\text{i.}\ \sum_{i=1}^{n}\sum_{j=1}^{m}x_{ij}=\sum_{j=1}^{m}\sum_{i=1}^{n}x_{ij}','i. Σ (i = 1 to n) Σ (j = 1 to m) xij = Σ (j = 1 to m) Σ (i = 1 to n) xij')
F.e('d2',r'\text{ii.}\ \sum_{i=1}^{n}\sum_{j=1}^{m}c\,x_{ij}=c\sum_{i=1}^{n}\sum_{j=1}^{m}x_{ij}','ii. Σ Σ c xij = c Σ Σ xij')
F.e('d3',r'\text{iii.}\ \sum_{i=1}^{n}\sum_{j=1}^{m}(x_{ij}+y_{ij})=\sum_{i=1}^{n}\sum_{j=1}^{m}x_{ij}+\sum_{i=1}^{n}\sum_{j=1}^{m}y_{ij}','iii. Σ Σ (xij + yij) = Σ Σ xij + Σ Σ yij')
F.e('d4',r'\text{iv.}\ \sum_{i=1}^{n}\sum_{j=1}^{m}x_iy_j=\sum_{i=1}^{n}x_i\sum_{j=1}^{m}y_j','iv. Σ (i = 1 to n) Σ (j = 1 to m) xi yj = Σ (i = 1 to n) xi Σ (j = 1 to m) yj')
head(s,'h173','1.7.3 Product notation','1.7.3 حاصلِ ضرب کی علامت','1.7.3 د ضرب نښه')
add(s,'t173','Π: (upper case pi): is notation for product. It is a Greek letter.','Π: (بڑا پائی): حاصلِ ضرب کی علامت ہے۔ یہ ایک یونانی حرف ہے۔','Π: (لوی پای): د ضرب حاصل نښه ده. دا یو یوناني توری دی.')
F.rest()
F.e('p0',r'\prod_{i=1}^{n}x_i\ :\ \text{means product of the values of the variable X, i.e. }(x_1)(x_2)\cdots(x_n).','Π (i = 1 to n) xi : means product of the values of the variable X, i.e. (x1)(x2)···(xn).')
head(s,'ex25','Example: 1.25','مثال: 1.25','بېلګه: 1.25',exampleId='stat11-ex-1-25')
add(s,'q25','If xi = 2, 3, 4. Compute Π xi (i = 1 to 3) and Π xi² (i = 1 to 3).','اگر xi = 2, 3, 4 ہوں تو Π xi (i = 1 سے 3) اور Π xi² (i = 1 سے 3) حساب کریں۔','که xi = 2, 3, 4 وي نو Π xi (i = 1 څخه تر 3) او Π xi² (i = 1 څخه تر 3) محاسبه کړئ.',role='question',exampleId='stat11-ex-1-25')
head(s,'sol25','Solution:','حل:','حل:',exampleId='stat11-ex-1-25')
F.rest()
F.e('s1',r'\prod_{i=1}^{3}x_i=(x_1)(x_2)(x_3)=2\times3\times4=24','Π (i = 1 to 3) xi = (x1)(x2)(x3) = 2×3×4 = 24',exampleId='stat11-ex-1-25')
F.e('s2',r'\prod_{i=1}^{3}x_i^2=(x_1^2)(x_2^2)(x_3^2)=(2^2)(3^2)(4^2)=(4)(9)(16)=576','Π (i = 1 to 3) xi² = (x1²)(x2²)(x3²) = (2²)(3²)(4²) = (4)(9)(16) = 576',exampleId='stat11-ex-1-25')
F.done()
s['sourceNote']='Printed page 45. In rule iii the final "y" is partly hidden by the watermark and is read as y_ij; in rule iv the subscripts of x and y are very small and are read as x_i y_j (the right side Σ x_i Σ y_j). A cross mark and a stray mark in the margin are ignored. The foot of the scan shows a ghost of the page-number bar. Header graphics and watermark excluded.'
s['vocabulary']={'product':dict(ur='حاصلِ ضرب',ps='ضرب حاصل')}
save(s)
# ---------- scan 54 (printed 46) ----------
s=page(54,U,'46','1.7.4 Rules for product notation','1.7.4 حاصلِ ضرب کی علامت کے قواعد','1.7.4 د ضرب د نښې قواعد','product-rules')
F=Flow(s)
head(s,'h174','1.7.4 Rules for product notation','1.7.4 حاصلِ ضرب کی علامت کے قواعد','1.7.4 د ضرب د نښې قواعد')
F.rest()
F.e('i',r'\text{i.}\ \prod_{i=1}^{n}c=c\times c\times\cdots\times c=c^n','i. Π (i = 1 to n) c = c × c × ⋯ × c = cⁿ')
F.e('ii',r'\text{ii.}\ \prod_{i=1}^{n}c\,x_i=c^n\prod_{i=1}^{n}x_i','ii. Π (i = 1 to n) c xi = cⁿ Π (i = 1 to n) xi')
F.e('iii',r'\text{iii.}\ \log\left(\prod_{i=1}^{n}x_i\right)=\log\left[(x_1)(x_2)\cdots(x_n)\right]=\log(x_1)+\log(x_2)+\cdots+\log(x_n)=\sum_{i=1}^{n}\log(x_i)','iii. log(Π xi) = log[(x1)(x2)···(xn)] = log(x1) + log(x2) + ⋯ + log(xn) = Σ log(xi)')
F.e('iv',r'\text{iv.}\ \prod_{i=1}^{n}\frac{x_i}{y_i}=\frac{\prod_{i=1}^{n}x_i}{\prod_{i=1}^{n}y_i}','iv. Π (xi / yi) = (Π xi) / (Π yi)')
F.e('v',r'\text{v.}\ \prod_{i=1}^{n}x_iy_i=\prod_{i=1}^{n}x_i\prod_{i=1}^{n}y_i','v. Π xi yi = Π xi × Π yi')
F.e('vi',r'\text{vi.}\ \prod_{i=1}^{n}(x_i+y_i)=(x_1+y_1)(x_2+y_2)\cdots(x_n+y_n)','vi. Π (xi + yi) = (x1 + y1)(x2 + y2)···(xn + yn)')
F.e('vii',r'\text{vii.}\ \prod_{i=1}^{n}(x_i-y_i)=(x_1-y_1)(x_2-y_2)\cdots(x_n-y_n)','vii. Π (xi − yi) = (x1 − y1)(x2 − y2)···(xn − yn)')
F.done()
s['sourceNote']='Printed page 46. Rule i is printed "c×c×  ×c = c^n" with the middle dots missing; it is given with the ellipsis. The lower half of the page is blank. The top of the scan shows a white band and the foot shows a ghost of the page-number bar. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
