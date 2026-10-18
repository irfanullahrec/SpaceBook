from stathelp import *
c=cell
U='dispersion-skewness-kurtosis'
E19='stat11-ex-3-19'; E20='stat11-ex-3-20'; E21='stat11-ex-3-21'
def Q(e,*pairs):
    return [(f'k{i}',l,t,e) for i,(l,t) in enumerate(pairs)]
RAW4=r"m_4=m_4'-4m_1'm_3'+6(m_1')^2m_2'-3(m_1')^4"; RAW4T="m4 = m′4 − 4m′1m′3 + 6(m′1)²m′2 − 3(m′1)⁴"
RAW3=r"m_3=m_3'-3m_1'm_2'+2(m_1')^3"; RAW3T="m3 = m′3 − 3m′1m′2 + 2(m′1)³"
RAW2=r"m_2=m_2'-(m_1')^2"; RAW2T="m2 = m′2 − (m′1)²"
RAW1=r"m_1=m_1'-m_1'"; RAW1T="m1 = m′1 − m′1"
# ---------- scan 127 (printed 119) ----------
s=page(127,U,'119','Example 3.19: solution (raw moments, mean moments)','مثال 3.19: حل (خام معیارِ اثر، اوسطی معیارِ اثر)','بېلګه 3.19: حل (خام مومنټونه، اوسط مومنټونه)','moments-6')
Flow(s)
head(s,'sol19','Solution:','حل:','حل:',exampleId=E19)
add(s,'a1','(i) Raw moments:','(i) خام معیارِ اثر:','(i) خام مومنټونه:',role='solution',exampleId=E19)
add(s,'a2','Taking an arbitrary origin a = 2 in the given data.','دیے گئے اعداد و شمار میں من مانا مبدا a = 2 لیتے ہوئے۔','په ورکړل شویو معلوماتو کې خپلسري اصل a = 2 اخیستل.',role='solution',exampleId=E19)
add(s,'a3','(ii) Mean moments','(ii) اوسطی معیارِ اثر','(ii) اوسط مومنټونه',role='solution',exampleId=E19)
xs=[1,1,0,2,2,3,1,0,1,3]
rows=[[str(x),str(x-2),str((x-2)**2),str((x-2)**3),str((x-2)**4)] for x in xs]
s['tables']=[table('Example 3.19: arbitrary origin a = 2','مثال 3.19: من مانا مبدا a = 2','بېلګه 3.19: خپلسري اصل a = 2',[c('x'),c('(x − 2)'),c('(x − 2)²'),c('(x − 2)³'),c('(x − 2)⁴')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('-6'),c('14'),c('-18'),c('38')]],exampleId=E19)]
eq=[('r1',r"m_1'=\dfrac{\sum(x-2)}{n}=\dfrac{-6}{10}=-0.6","m′1 = Σ(x − 2)/n = −6/10 = −0.6",E19),
 ('r2',r"m_2'=\dfrac{\sum(x-2)^2}{n}=\dfrac{14}{10}=1.4","m′2 = Σ(x − 2)²/n = 14/10 = 1.4",E19),
 ('r3',r"m_3'=\dfrac{\sum(x-2)^3}{n}=\dfrac{-18}{10}=-1.8","m′3 = Σ(x − 2)³/n = −18/10 = −1.8",E19),
 ('r4',r"m_4'=\dfrac{\sum(x-2)^4}{n}=\dfrac{38}{10}=3.8","m′4 = Σ(x − 2)⁴/n = 38/10 = 3.8",E19),
 ('m1',RAW1+r"=-0.6-(-0.6)=-0.6+0.6=0",RAW1T+" = −0.6 − (−0.6) = −0.6 + 0.6 = 0",E19),
 ('m2',RAW2+r"=1.4-(-0.6)^2=1.4-0.36=1.04",RAW2T+" = 1.4 − (−0.6)² = 1.4 − 0.36 = 1.04",E19),
 ('m3a',RAW3,RAW3T,E19),
 ('m3b',r"=-1.8-3(-0.6)(1.4)+2(-0.6)^3","= −1.8 − 3(−0.6)(1.4) + 2(−0.6)³",E19),
 ('m3c',r"=-1.8+2.52-0.432=-2.232+2.52=0.29","= −1.8 + 2.52 − 0.432 = −2.232 + 2.52 = 0.29",E19),
 ('m4a',RAW4,RAW4T,E19)]
build(s,127,['sol19','a1','a2','T:0','E:r1','E:r2','E:r3','E:r4','a3','E:m1','E:m2','E:m3a','E:m3b','E:m3c','E:m4a'],eq)
s['sourceNote']='Printed page 119. The data of Example 3.19 (1, 1, 0, 2, 2, 3, 1, 0, 1, 3) were printed at the foot of the previous page. The printed result of m3 is 0.29 (−2.232 + 2.52 = 0.288). The m4 working continues on the next page. Header graphics and watermark excluded; a second strip of the following scan appears at the bottom edge and is ignored.'
s['vocabulary']={}
save(s)
# ---------- scan 128 (printed 120) ----------
s=page(128,U,'120','Example 3.19 (m4 working) · Example 3.20: moments about P.M and mean moments','مثال 3.19 (m4 کا حل) · مثال 3.20: عارضی اوسط کے گرد اور اوسطی معیارِ اثر','بېلګه 3.19 (د m4 حل) · بېلګه 3.20: د لنډمهاله اوسط شاوخوا او اوسط مومنټونه','moments-7')
Flow(s)
head(s,'ex20','Example: 3.20','مثال: 3.20','بېلګه: 3.20',exampleId=E20)
add(s,'q20','Calculate the first four moments about the mean from the data given below','نیچے دیے گئے اعداد و شمار سے اوسط کے گرد پہلے چار معیارِ اثر حساب کریں','له لاندې ورکړل شویو معلوماتو څخه د اوسط شاوخوا لومړي څلور مومنټونه محاسبه کړئ',role='question',exampleId=E20)
head(s,'sol20','Solution:','حل:','حل:',exampleId=E20)
add(s,'a1','(i) Moments about P.M:','(i) عارضی اوسط (P.M) کے گرد معیارِ اثر:','(i) د لنډمهاله اوسط (P.M) شاوخوا مومنټونه:',role='solution',exampleId=E20)
add(s,'a2','Here a = 3','یہاں a = 3','دلته a = 3',role='solution',exampleId=E20)
add(s,'a3','(ii) Mean moments:','(ii) اوسطی معیارِ اثر:','(ii) اوسط مومنټونه:',role='solution',exampleId=E20)
rows=[('1','5','-2','-10','20','-40','80'),('2','7','-1','-7','7','-7','7'),('3','10','0','0','0','0','0'),('4','6','1','6','6','6','6'),('5','2','2','4','8','16','32')]
s['tables']=[table('Example 3.20: x and f','مثال 3.20: x اور f','بېلګه 3.20: x او f',[c('x:')]+[c(v) for v in '12345'],[[c('f:')]+[c(v) for v in ['5','7','10','6','2']]],exampleId=E20),
 table('Example 3.20: moments about P.M, a = 3','مثال 3.20: عارضی اوسط کے گرد معیارِ اثر، a = 3','بېلګه 3.20: د لنډمهاله اوسط شاوخوا مومنټونه، a = 3',[c('x'),c('f'),c('(x − 3)'),c('f(x − 3)'),c('f(x − 3)²'),c('f(x − 3)³'),c('f(x − 3)⁴')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('30'),c('–'),c('-7'),c('41'),c('-25'),c('125')]],exampleId=E20)]
eq=[('p1',r"=3.8-4(-0.6)(-1.8)+6(-0.6)^2(1.4)-3(-0.6)^4","= 3.8 − 4(−0.6)(−1.8) + 6(−0.6)²(1.4) − 3(−0.6)⁴",E19),
 ('p2',r"=3.8-4.32+3.024-0.3888\ \ =6.824-4.7088=2.12","= 3.8 − 4.32 + 3.024 − 0.3888  = 6.824 − 4.7088 = 2.12",E19),
 ('r1',r"m_1'=\dfrac{\sum f(x-3)}{\sum f}=\dfrac{-7}{30}=-0.23","m′1 = Σf(x − 3)/Σf = −7/30 = −0.23",E20),
 ('r2',r"m_2'=\dfrac{\sum f(x-3)^2}{\sum f}=\dfrac{41}{30}=1.37","m′2 = Σf(x − 3)²/Σf = 41/30 = 1.37",E20),
 ('r3',r"m_3'=\dfrac{\sum f(x-3)^3}{\sum f}=\dfrac{-25}{30}=-0.83","m′3 = Σf(x − 3)³/Σf = −25/30 = −0.83",E20),
 ('r4',r"m_4'=\dfrac{\sum f(x-3)^4}{\sum f}=\dfrac{125}{30}=4.17","m′4 = Σf(x − 3)⁴/Σf = 125/30 = 4.17",E20),
 ('m1',RAW1+r"=-0.23-(-0.23)=-0.23+0.23=0",RAW1T+" = −0.23 − (−0.23) = −0.23 + 0.23 = 0",E20),
 ('m2',RAW2+r"=1.37-(-0.23)^2=1.37-0.0529=1.32",RAW2T+" = 1.37 − (−0.23)² = 1.37 − 0.0529 = 1.32",E20),
 ('m3a',RAW3,RAW3T,E20),
 ('m3b',r"=-0.83-3(-0.23)(1.37)+2(-0.23)^3","= −0.83 − 3(−0.23)(1.37) + 2(−0.23)³",E20)]
build(s,128,['E:p1','E:p2','ex20','q20','T:0','sol20','a1','T:1','a2','E:r1','E:r2','E:r3','E:r4','a3','E:m1','E:m2','E:m3a','E:m3b'],eq)
s['sourceNote']='Printed page 120. The first two lines complete the m4 working of Example 3.19 (the printed result 2.12 is kept; 6.824 − 4.7088 = 2.1152). The m3 working of Example 3.20 continues on the next page. A black mark at the top-left corner is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 129 (printed 121) ----------
s=page(129,U,'121','Example 3.20 (end) · Example 3.21: raw moments about x = 12','مثال 3.20 (اختتام) · مثال 3.21: x = 12 کے گرد خام معیارِ اثر','بېلګه 3.20 (پای) · بېلګه 3.21: د x = 12 شاوخوا خام مومنټونه','moments-8')
Flow(s)
head(s,'ex21','Example: 3.21','مثال: 3.21','بېلګه: 3.21',exampleId=E21)
add(s,'q21','Calculate first four moments about x = 12 and then find mean moments from the following grouped frequency distribution.','درج ذیل گروہی تعدد تقسیم سے x = 12 کے گرد پہلے چار معیارِ اثر حساب کریں اور پھر اوسطی معیارِ اثر معلوم کریں۔','له لاندې ګروپي فریکونسي ویش څخه د x = 12 شاوخوا لومړي څلور مومنټونه محاسبه کړئ او بیا اوسط مومنټونه ومومئ.',role='question',exampleId=E21)
head(s,'sol21','Solution:','حل:','حل:',exampleId=E21)
add(s,'a1','(i) Raw moments:','(i) خام معیارِ اثر:','(i) خام مومنټونه:',role='solution',exampleId=E21)
rows=[('0 – 4','2','2','-10','-20','200','-2000','20000'),('5 – 9','5','7','-5','-25','125','-625','3125'),('10 – 14','12','12','0','0','0','0','0'),('15 – 19','9','17','5','45','225','1125','5625'),('20 – 24','7','22','10','70','700','7000','70000')]
s['tables']=[table('Example 3.21: group and frequency','مثال 3.21: گروہ اور تعدد','بېلګه 3.21: ډله او فریکونسي',[c('Group:','گروہ:','ډله:')]+[c(v) for v in ['0 – 4','5 – 9','10 – 14','15 – 19','20 – 24']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(v) for v in ['2','5','12','9','7']]],exampleId=E21),
 table('Example 3.21: raw moments about x = 12','مثال 3.21: x = 12 کے گرد خام معیارِ اثر','بېلګه 3.21: د x = 12 شاوخوا خام مومنټونه',[c('Group','گروہ','ډله'),c('f'),c('x'),c('(x − 12)'),c('f(x − 12)'),c('f(x − 12)²'),c('f(x − 12)³'),c('f(x − 12)⁴')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('35'),c('–'),c('–'),c('70'),c('1250'),c('5500'),c('98750')]],exampleId=E21)]
eq=[('p1',r"=-0.83+0.9453-0.0243","= −0.83 + 0.9453 − 0.0243",E20),
 ('p2',r"=-.8543+0.9453=0.091","= −.8543 + 0.9453 = 0.091",E20),
 ('p3',RAW4,RAW4T,E20),
 ('p4',r"=4.17-4(-0.23)(-0.83)+6(-0.23)^2(1.37)-3(-0.23)^4","= 4.17 − 4(−0.23)(−0.83) + 6(−0.23)²(1.37) − 3(−0.23)⁴",E20),
 ('p5',r"=4.17-0.7636+0.4348-0.0084","= 4.17 − 0.7636 + 0.4348 − 0.0084",E20),
 ('p6',r"=4.6048-0.772=3.833","= 4.6048 − 0.772 = 3.833",E20),
 ('r1',r"m_1'=\dfrac{\sum f(x-12)}{\sum f}=\dfrac{70}{35}=2\qquad\qquad m_2'=\dfrac{\sum f(x-12)^2}{\sum f}=\dfrac{1250}{35}=35.7","m′1 = Σf(x − 12)/Σf = 70/35 = 2    m′2 = Σf(x − 12)²/Σf = 1250/35 = 35.7",E21),
 ('r3',r"m_3'=\dfrac{\sum f(x-12)^3}{\sum f}=\dfrac{5500}{35}=157.14\qquad\qquad m_4'=\dfrac{\sum f(x-12)^4}{\sum f}=\dfrac{98750}{35}=2821.43","m′3 = Σf(x − 12)³/Σf = 5500/35 = 157.14    m′4 = Σf(x − 12)⁴/Σf = 98750/35 = 2821.43",E21)]
build(s,129,['E:p1','E:p2','E:p3','E:p4','E:p5','E:p6','ex21','q21','T:0','sol21','a1','T:1','E:r1','E:r3'],eq)
s['sourceNote']='Printed page 121. The first lines complete the m3 and m4 workings of Example 3.20. The raw moments of Example 3.21 are printed in two side-by-side pairs, each kept as one equation. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 130 (printed 122) ----------
s=page(130,U,'122','Example 3.21 (mean moments) · (iii) Moments about origin','مثال 3.21 (اوسطی معیارِ اثر) · (iii) مبدا کے گرد معیارِ اثر','بېلګه 3.21 (اوسط مومنټونه) · (iii) د اصل شاوخوا مومنټونه','moments-9')
Flow(s)
add(s,'a1','(ii) Mean moments:','(ii) اوسطی معیارِ اثر:','(ii) اوسط مومنټونه:',role='solution',exampleId=E21)
add(s,'t1','(iii) Moments about origin','(iii) مبدا کے گرد معیارِ اثر','(iii) د اصل شاوخوا مومنټونه')
add(s,'t2','When moments are computed about P.M = 0, they are called moments about origin or moments about zero. These are also called raw moments. Formulas in this case are:','جب معیارِ اثر P.M = 0 کے گرد حساب کیے جائیں تو انہیں مبدا کے گرد معیارِ اثر یا صفر کے گرد معیارِ اثر کہا جاتا ہے۔ انہیں خام معیارِ اثر بھی کہتے ہیں۔ اس صورت میں فارمولے یہ ہیں:','کله چې مومنټونه د P.M = 0 شاوخوا محاسبه شي نو دوی ته د اصل شاوخوا مومنټونه یا د صفر شاوخوا مومنټونه ویل کېږي. دې ته خام مومنټونه هم ویل کېږي. پدې حالت کې فورمولونه دا دي:')
add(s,'lu','For ungrouped data','غیر گروہی اعداد و شمار کے لیے','د نه‌ګروپ شویو معلوماتو لپاره')
add(s,'lg','For grouped data','گروہی اعداد و شمار کے لیے','د ګروپي معلوماتو لپاره')
add(s,'t3','Put these raw moments in the relations to get mean moments.','ان خام معیارِ اثر کو تعلقات میں رکھ کر اوسطی معیارِ اثر حاصل کریں۔','دا خام مومنټونه په اړیکو کې کېږدئ ترڅو اوسط مومنټونه ترلاسه شي.')
eq=[('m1',RAW1+r"=2-2=0",RAW1T+" = 2 − 2 = 0",E21),
 ('m2',RAW2+r"=35.7-2^2=35.7-4=31.7",RAW2T+" = 35.7 − 2² = 35.7 − 4 = 31.7",E21),
 ('m3a',RAW3,RAW3T,E21),
 ('m3b',r"=157.14-3(2)(35.7)+2(2^3)","= 157.14 − 3(2)(35.7) + 2(2³)",E21),
 ('m3c',r"=157.14-214.2+16","= 157.14 − 214.2 + 16",E21),
 ('m3d',r"=173.14-214.2=-41.06","= 173.14 − 214.2 = −41.06",E21),
 ('m4a',RAW4,RAW4T,E21),
 ('m4b',r"=2821.43-4(2)(157.14)+6(2)^2(35.7)-3(2)^4","= 2821.43 − 4(2)(157.14) + 6(2)²(35.7) − 3(2)⁴",E21),
 ('m4c',r"=2821.43-1257.12+856.8-48","= 2821.43 − 1257.12 + 856.8 − 48",E21),
 ('m4d',r"=3678.23-1305.12=2373.11","= 3678.23 − 1305.12 = 2373.11",E21),
 ('o1',r"m_1'=\dfrac{\sum x}{n}\qquad\qquad m_1'=\dfrac{\sum fx}{\sum f}","m′1 = Σx/n    m′1 = Σfx/Σf",None),
 ('o2',r"m_2'=\dfrac{\sum x^2}{n}\qquad\qquad m_2'=\dfrac{\sum fx^2}{\sum f}","m′2 = Σx²/n    m′2 = Σfx²/Σf",None),
 ('o3',r"m_3'=\dfrac{\sum x^3}{n}\qquad\qquad m_3'=\dfrac{\sum fx^3}{\sum f}","m′3 = Σx³/n    m′3 = Σfx³/Σf",None),
 ('o4',r"m_4'=\dfrac{\sum x^4}{n}\qquad\qquad m_4'=\dfrac{\sum fx^4}{\sum f}","m′4 = Σx⁴/n    m′4 = Σfx⁴/Σf",None)]
build(s,130,['a1','E:m1','E:m2','E:m3a','E:m3b','E:m3c','E:m3d','E:m4a','E:m4b','E:m4c','E:m4d','t1','t2','lu','lg','E:o1','E:o2','E:o3','E:o4','t3'],eq)
s['sourceNote']='Printed page 122. The formulas for moments about the origin are printed in two columns (ungrouped left, grouped right); each pair is kept as one equation. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
