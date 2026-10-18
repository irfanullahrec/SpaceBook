from stathelp import *
c=cell
U='index-numbers'
E410='stat11-ex-4-10'; E411='stat11-ex-4-11'
# ---------- scan 172 (printed 162) ----------
s=page(172,U,'162','4.2.1 (iv) Computation: aggregative expenditure and household budget methods · Example 4.10 (question)','4.2.1 (iv) حساب: مجموعی اخراجات اور گھریلو بجٹ کے طریقے · مثال 4.10 (سوال)','4.2.1 (iv) محاسبه: د مجموعي لګښت او د کورنۍ د بودیجې طریقې · بېلګه 4.10 (پوښتنه)','index-cpi-2')
Flow(s)
add(s,'m2','(ii) The household or family budget method:','(ii) گھریلو یا خاندانی بجٹ کا طریقہ:','(ii) د کورنۍ یا کورنیز بودیجې طریقه:')
add(s,'m2b','(Both methods give the same result.)','(دونوں طریقے ایک ہی نتیجہ دیتے ہیں۔)','(دواړه طریقې یو شان پایله ورکوي.)')
head(s,'ex410','Example: 4.10','مثال: 4.10','بېلګه: 4.10',exampleId=E410)
add(s,'q410','Calculate the consumer price index number from the data given below by (i) Aggregative expenditure method and (ii) Household/family budget method.','نیچے دیے گئے اعداد و شمار سے صارف قیمتی اشاریہ عدد حساب کریں (i) مجموعی اخراجات کے طریقے اور (ii) گھریلو/خاندانی بجٹ کے طریقے سے۔','له لاندې ورکړل شویو معلوماتو څخه د مصرف کوونکي د بیې شاخص شمېره محاسبه کړئ د (i) مجموعي لګښت طریقې او (ii) کورنۍ/کورنیزې بودیجې طریقې په واسطه.',role='question',exampleId=E410)
rows=[('Rice','5 maund','Rs. per maund','6','8'),('Millets','5 maund','Rs. per maund','4','5'),('Wheat','1 maund','Rs. per maund','5','10'),('Gram','1 maund','Rs. per maund','3','6'),('Arhar','1/2 maund','Rs. per maund','4','6'),('Pulses','2 maund','Rs. per maund','3','4'),('Ghee','4 seer','Rs. per seer','1.25','2'),('Gur','2 maund','Rs. per maund','2.50','5'),('Salt','2 1/2 seer','Rs. per seer','4','5'),('Oil','24 seer','Rs. per seer','2','2.5'),('Clothing','40 yard','Rs. per yard','0.25','0.5'),('Fire-wood','10 maund','Rs. per maund','0.50','0.8'),('Kerosene oil','1 tin','Rs. per tin','4','6'),('House rent','1 house','Rs. per house','12','15')]
s['tables']=[table('Example 4.10: quantities consumed and prices','مثال 4.10: استعمال شدہ مقداریں اور قیمتیں','بېلګه 4.10: مصرف شوي مقدارونه او بیې',[c('Commodities','اجناس','توکي'),c('Quantity consumed (1939)','استعمال شدہ مقدار (1939)','مصرف شوی مقدار (1939)'),c('Unit of price','قیمت کی اکائی','د بیې واحد'),c('Price in (1939)','قیمت (1939)','بیه په (1939)'),c('Price in (1940)','قیمت (1940)','بیه په (1940)')],[[c(v) for v in r] for r in rows],exampleId=E410)]
s['equations']+=[eqn(172,'a',r'P_{0n}=\dfrac{\sum p_nq_0}{\sum p_0q_0}\times 100','P0n = (Σ pn q0 / Σ p0 q0) × 100'),
 eqn(172,'b',r'P_{0n}=\dfrac{\sum\left(\dfrac{p_n}{p_0}\right)p_0q_0}{\sum p_0q_0}\times 100','P0n = Σ(pn/p0) p0 q0 / Σ p0 q0 × 100')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(172,k) for k in ks])
s['flow']=[dict(type='equation',index=0),P('m2'),dict(type='equation',index=1),P('m2b','ex410','q410'),dict(type='table',index=0)]
s['sourceNote']='Printed page 162. The first formula completes the aggregative expenditure method from the previous page. In the table the quantities 1/2 maund and 2 1/2 seer are printed as mixed fractions. A blue ink tick next to "Example: 4.10" is ignored. Header graphics and watermark excluded. Scan 171 is a second copy of printed page 161.'
s['vocabulary']={}
save(s)
# ---------- scan 173 (printed 163) ----------
s=page(173,U,'163','Example 4.10: solution table and aggregative expenditure method','مثال 4.10: حل کا جدول اور مجموعی اخراجات کا طریقہ','بېلګه 4.10: د حل جدول او د مجموعي لګښت طریقه','index-cpi-3')
Flow(s)
head(s,'sol410','Solution:','حل:','حل:',exampleId=E410)
add(s,'a1','We consider 1939 as base year and 1940 as current year then the necessary calculation required for both methods are given in the following table.','ہم 1939 کو بنیادی سال اور 1940 کو موجودہ سال لیتے ہیں تو دونوں طریقوں کے لیے مطلوبہ حسابات درج ذیل جدول میں دیے گئے ہیں۔','موږ 1939 د بنسټیز کال او 1940 د اوسني کال په توګه نیسو نو د دواړو طریقو لپاره اړین محاسبې په لاندې جدول کې ورکړل شوې دي.',role='solution',exampleId=E410)
add(s,'a2','(i) CPI for 1940 by aggregative expenditure method is','(i) 1940 کا CPI مجموعی اخراجات کے طریقے سے ہے','(i) د 1940 CPI د مجموعي لګښت په طریقه دی',role='solution',exampleId=E410)
rows=[('Rice','5','6','8','40','30','1.333','39.99'),('Millets','5','4','5','25','20','1.25','25.00'),('Wheat','1','5','10','10','5','2.00','10.00'),('Gram','1','3','6','6','3','2.00','6.00'),('Arhar','0.5','4','6','3','2','1.50','3.00'),('Pulses','2','3','4','8','6','1.333','7.998'),('Ghee','4','1.25','2','8','5','1.60','8.00'),('Gur','2','2.50','5','10','5','2.00','10.00'),('Salt','2.5','4','5','12.5','10','1.25','12.50'),('Oil','24','2','2.5','60','48','1.25','60.00'),('Clothing','40','0.25','0.5','20','10','2.00','20.00'),('Fire-wood','10','0.50','0.8','8','5','1.60','8.00'),('Kerosene oil','1','4','6','6','4','1.50','6.00'),('House rent','1','12','15','15','12','1.25','15.00')]
s['tables']=[table('Example 4.10 solution table','مثال 4.10 کا حل: جدول','د بېلګې 4.10 د حل جدول',[c('Commodities','اجناس','توکي'),c('q0'),c('p0'),c('pn'),c('pn q0'),c('p0 q0'),c('(pn/p0)'),c('(pn/p0) p0 q0')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c(''),c('–'),c('–'),c('231.5'),c('165'),c('–'),c('231.488')]],exampleId=E410)]
s['equations']+=[eqn(173,'e',r'P_{0n}=\dfrac{\sum p_nq_0}{\sum p_0q_0}\times 100=\dfrac{231.5}{165}\times 100=140.3\ \%','P0n = (Σ pn q0 / Σ p0 q0) × 100 = (231.5/165) × 100 = 140.3 %',exampleId=E410)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(173,k) for k in ks])
s['flow']=[P('sol410','a1'),dict(type='table',index=0),P('a2'),dict(type='equation',index=0)]
s['sourceNote']='Printed page 163. The q0 entry of the total row is empty. The printed ratios (for example 1.333, 7.998) and totals 231.5 and 231.488 are kept. Dark pixelation at the top-right corner is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 174 (printed 164) ----------
s=page(174,U,'164','Example 4.10 (household budget method) · Example 4.11 (question)','مثال 4.10 (گھریلو بجٹ کا طریقہ) · مثال 4.11 (سوال)','بېلګه 4.10 (د کورنۍ د بودیجې طریقه) · بېلګه 4.11 (پوښتنه)','index-cpi-4')
Flow(s)
add(s,'a1','(ii) CPI for 1940 by household budget method is','(ii) 1940 کا CPI گھریلو بجٹ کے طریقے سے ہے','(ii) د 1940 CPI د کورنۍ د بودیجې په طریقه دی',role='solution',exampleId=E410)
add(s,'a2','Hence results of both methods are same and indicate that the composite prices in 1940 have been increased by 40.3%.','لہٰذا دونوں طریقوں کے نتائج ایک ہی ہیں اور ظاہر کرتے ہیں کہ 1940 میں مرکب قیمتوں میں 40.3 فیصد اضافہ ہوا ہے۔','نو د دواړو طریقو پایلې یو شان دي او ښيي چې په 1940 کې مرکب بیې په 40.3 سلنه زیاتې شوې دي.',role='solution',exampleId=E410)
head(s,'ex411','Example: 4.11','مثال: 4.11','بېلګه: 4.11',exampleId=E411)
add(s,'q411','Compute consumer price index number for 1958 on the basis of 1948 using (1) Aggregative expenditure method (ii) Household budget method from the following data of eight commodities:','1948 کی بنیاد پر 1958 کے لیے صارف قیمتی اشاریہ عدد حساب کریں (1) مجموعی اخراجات کے طریقے (ii) گھریلو بجٹ کے طریقے سے آٹھ اجناس کے درج ذیل اعداد و شمار سے:','د 1948 پر بنسټ د 1958 لپاره د مصرف کوونکي د بیې شاخص شمېره محاسبه کړئ د (1) مجموعي لګښت طریقې (ii) د کورنۍ د بودیجې طریقې په واسطه له اتو توکو لاندې معلوماتو څخه:',role='question',exampleId=E411)
head(s,'sol411','Solution:','حل:','حل:',exampleId=E411)
add(s,'a3','Since unit of price is different from the unit of quantities consumed therefore we first convert unit of quantities to unit of price so that both may have same unit. Further calculations required for both methods are given in the same table as follows. Note that one maund has 40 seers.','چونکہ قیمت کی اکائی استعمال شدہ مقداروں کی اکائی سے مختلف ہے اس لیے ہم پہلے مقداروں کی اکائی کو قیمت کی اکائی میں تبدیل کرتے ہیں تاکہ دونوں کی اکائی ایک ہی ہو۔ دونوں طریقوں کے لیے مطلوبہ مزید حسابات اسی جدول میں اس طرح دیے گئے ہیں۔ نوٹ کریں کہ ایک من میں 40 سیر ہوتے ہیں۔','ځکه چې د بیې واحد د مصرف شویو مقدارونو له واحد څخه توپیر لري نو موږ لومړی د مقدارونو واحد د بیې واحد ته بدلوو ترڅو دواړه یو شان واحد ولري. د دواړو طریقو لپاره اړین نورې محاسبې په همدې جدول کې داسې ورکړل شوې دي. پام وکړئ چې یو من 40 سیره لري.',role='solution',exampleId=E411,sourceGap=dict(note='The calculation table continues on the next page.'))
rows=[('Wheat','20 seer','Rs. per maund','12','15'),('Rice','8 seer','Rs. per maund','40','45'),('Sugar','2 seer','Rs. per maund','40','50'),('Ghee','1 seer','Rs. per maund','110','120'),('Milk','25 seer','Rs. per seer','0.50','0.75'),('Vegetables','16 seer','Rs. per seer','0.25','0.50'),('Mutton','5 seer','Rs. per seer','3','4'),('Fuel','4 maund','Rs. per maund','2.5','3')]
s['tables']=[table('Example 4.11: quantities consumed (1948) and prices','مثال 4.11: استعمال شدہ مقداریں (1948) اور قیمتیں','بېلګه 4.11: مصرف شوي مقدارونه (1948) او بیې',[c('Commodities','اجناس','توکي'),c('Quantity consumed (1948)','استعمال شدہ مقدار (1948)','مصرف شوی مقدار (1948)'),c('Unit of price','قیمت کی اکائی','د بیې واحد'),c('Price: 1948','قیمت: 1948','بیه: 1948'),c('Price: 1958','قیمت: 1958','بیه: 1958')],[[c(v) for v in r] for r in rows],exampleId=E411)]
s['equations']+=[eqn(174,'e',r'P_{0n}=\dfrac{\sum\left(\dfrac{p_n}{p_0}\right)p_0q_0}{\sum p_0q_0}\times 100=\dfrac{231.488}{165}\times 100=140.3\%','P0n = Σ(pn/p0) p0 q0 / Σ p0 q0 × 100 = (231.488/165) × 100 = 140.3%',exampleId=E410)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(174,k) for k in ks])
s['flow']=[P('a1'),dict(type='equation',index=0),P('a2','ex411','q411'),dict(type='table',index=0),P('sol411','a3')]
s['sourceNote']='Printed page 164. The two-level header "Price / 1948 / 1958" is flattened. Printed text kept: "using (1) Aggregative expenditure method (ii) …" in the question. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
