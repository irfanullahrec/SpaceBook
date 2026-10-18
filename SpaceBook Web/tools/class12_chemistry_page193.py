"""PDF193 printed380–381: Unit 24 Exercise Q1 MCQs 1–15, Q2 i–viii."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow193');t=F.t;line=F.line
P=[];L=[];B=[]
def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
def lines(rows,kind='lines'):
 s0=len(P)
 for r in rows:P.append(pair(*r))
 L.append({'type':kind,'indices':list(range(s0,len(P)))})
def visual(identity,fn):B.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});L.append({'type':'visual','blockId':identity})
K=lambda lang,*v:v[{'en':0,'ur':1,'ps':2}[lang]]
def ms(lang):
 X=lambda m:120+(m-10)/40*600;Y=lambda a:220-a*1.8
 s=F.start(260)+line(X(10),Y(0),X(50),Y(0),1.5)+line(X(10),Y(0),X(10),Y(100),1.5)
 for m in (10,20,30,40,50):s+=t(X(m),Y(0)+18,str(m),11)
 for a in (0,20,40,60,80,100):s+=t(X(10)-18,Y(a)+4,str(a),10)
 for m,a in ((12,8),(16,10),(28,10),(44,100)):s+=line(X(m),Y(0),X(m),Y(a),2.5,'#c62828')
 s+=t(X(30),Y(0)+36,'m/z',12)+f'<text x="70" y="{Y(50)}" transform="rotate(-90 70 {Y(50)})" text-anchor="middle" font-family="Arial" font-size="11">{K(lang,"Rel. Abundance","نسبتی کثرت","نسبي کثرت")}</text>'
 return s+'</svg>'
add('Exercise','مشق','تمرین','heading')
add('Q 1. Choose the correct one from the given options.','سوال 1. دیے گئے اختیارات میں سے درست کا انتخاب کریں۔','پوښتنه 1. له ورکړل شویو انتخابونو څخه سم یې وټاکئ.','heading')
M=[('1. Which one of the following is quantitative chemical analysis?','1. درج ذیل میں سے کون سا مقداری کیمیائی تجزیہ ہے؟','1. له لاندې څخه کوم یو کمي کیمیاوي تحلیل دی؟','a. Salt analysis   b. Titration   c. Flame test   d. Bromine-water test','a. نمک کا تجزیہ   b. ٹائٹریشن   c. شعلہ ٹیسٹ   d. برومین پانی ٹیسٹ','a. د مالګې تحلیل   b. ټایټرېشن   c. د لمبې ازموینه   d. د بروماین اوبو ازموینه'),
 ('2. C₂H₆O is the molecular formula of (i) ethanol (ii) methanol (iii) dimethyl ether (iv) diethyl ether','2. C₂H₆O کس کا سالماتی فارمولا ہے (i) ایتھانول (ii) میتھانول (iii) ڈائی میتھائل ایتھر (iv) ڈائی ایتھائل ایتھر','2. C₂H₆O د کوم مالیکولي فورمول دی (i) ایتانول (ii) میتانول (iii) ډای میتایل ایتر (iv) ډای ایتیل ایتر','a. (i) and (ii)   b. (ii) and (iii)   c. (i) and (iii)   d. (ii) and (v)','a. (i) اور (ii)   b. (ii) اور (iii)   c. (i) اور (iii)   d. (ii) اور (v)','a. (i) او (ii)   b. (ii) او (iii)   c. (i) او (iii)   d. (ii) او (v)'),
 ('3. Which one of the following techniques is mainly used for determination of functional group in a compound?','3. درج ذیل میں سے کون سی تکنیک بنیادی طور پر مرکب میں فعلی گروپ کے تعین کے لیے استعمال ہوتی ہے؟','3. له لاندې تخنیکونو څخه کوم یو اساساً په مرکب کې د فعال ګروپ د ټاکلو لپاره کارېږي؟','a. IR Spectroscopy   b. NMR   c. UV/ Visible spectroscopy   d. Mass spectroscopy','a. IR سپیکٹروسکوپی   b. NMR   c. UV/مرئی سپیکٹروسکوپی   d. ماس سپیکٹروسکوپی','a. IR سپکټروسکوپي   b. NMR   c. UV/لیدونکې سپکټروسکوپي   d. ماس سپکټروسکوپي'),
 ('4. Two different compounds will always give different absorption peak in ______ region of IR.','4. دو مختلف مرکبات IR کے ______ خطے میں ہمیشہ مختلف جذبی چوٹی دیں گے۔','4. دوه بېلابېل مرکبات به تل د IR په ______ سیمه کې بېلابېلې جذب څوکې ورکوي.','a. 1500–625 cm⁻¹   b. 4000–1500 cm⁻¹   c. 3000–2500 cm⁻¹   d. 3500–1500 cm⁻¹','a. 1500–625 cm⁻¹   b. 4000–1500 cm⁻¹   c. 3000–2500 cm⁻¹   d. 3500–1500 cm⁻¹','a. 1500–625 cm⁻¹   b. 4000–1500 cm⁻¹   c. 3000–2500 cm⁻¹   d. 3500–1500 cm⁻¹'),
 ('5. Which one of the following methods, relatively gives more information about the structure of an organic compound?','5. درج ذیل میں سے کون سا طریقہ نامیاتی مرکب کی ساخت کے بارے میں نسبتاً زیادہ معلومات دیتا ہے؟','5. له لاندې طریقو څخه کومه یوه نسبتاً د عضوي مرکب د جوړښت په اړه ډېر معلومات ورکوي؟','a. Mass Spectroscopy   b. NMR Spectroscopy   c. IR Spectroscopy   d. UV-Visible Spectroscopy','a. ماس سپیکٹروسکوپی   b. NMR سپیکٹروسکوپی   c. IR سپیکٹروسکوپی   d. UV-مرئی سپیکٹروسکوپی','a. ماس سپکټروسکوپي   b. NMR سپکټروسکوپي   c. IR سپکټروسکوپي   d. UV-لیدونکې سپکټروسکوپي')]
for q in M:lines([q[:3],q[3:]])
add('6. A mass spectrum is shown below.','6. نیچے ایک ماس طیف دکھایا گیا ہے۔','6. لاندې یو ماس طیف ښودل شوی.')
visual('chem12-p193-mcq6-spectrum',ms)
lines([('Which one of the following compound gives complete mass spectrum illustrated?','درج ذیل میں سے کون سا مرکب دکھایا گیا مکمل ماس طیف دیتا ہے؟','له لاندې مرکباتو څخه کوم یو ښودل شوی بشپړ ماس طیف ورکوي؟'),('a. CO₂   b. N₂   c. C₃H₈   d. Mixture of CH₄ and N₂','a. CO₂   b. N₂   c. C₃H₈   d. CH₄ اور N₂ کا آمیزہ','a. CO₂   b. N₂   c. C₃H₈   d. د CH₄ او N₂ ګډوله')])
M=[('7. The wavelength range of UV region is from','7. UV خطے کی طولِ موج کی حد ہے','7. د UV سیمې د موج اوږدوالي پوله ده','a. 400–800 nm.   b. 800–1200 nm.   c. 1200–1600 nm.   d. 10–400 nm.','a. 400–800 nm۔   b. 800–1200 nm۔   c. 1200–1600 nm۔   d. 10–400 nm۔','a. 400–800 nm.   b. 800–1200 nm.   c. 1200–1600 nm.   d. 10–400 nm.'),
 ('8. Which one of the following hydrocarbon produces a proton NMR spectrum with more than one peak?','8. درج ذیل میں سے کون سا ہائیڈروکاربن ایک سے زیادہ چوٹی والا پروٹون NMR طیف دیتا ہے؟','8. له لاندې هایدروکاربنونو څخه کوم یو له یوې ډېرو څوکو سره پروټون NMR طیف تولیدوي؟','a. Methane   b. Ethane   c. Butane   d. Cyclobutane','a. میتھین   b. ایتھین   c. بیوٹین   d. سائیکلو بیوٹین','a. میتان   b. ایتان   c. بیوټان   d. سایکلوبیوټان'),
 ('9. How many signals/peaks would you expect in the proton NMR spectrum of 1,1-dicholorethane?','9. 1،1-ڈائی کلورو ایتھین کے پروٹون NMR طیف میں آپ کتنے سگنل/چوٹیوں کی توقع کریں گے؟','9. د 1،1-ډای کلورو ایتان په پروټون NMR طیف کې تاسو د څو سیګنالونو/څوکو تمه لرئ؟','a. 2   b. 4   c. 6   d. 8','a. 2   b. 4   c. 6   d. 8','a. 2   b. 4   c. 6   d. 8'),
 ('10. How many types of protons are there in butanoic acid?','10. بیوٹانوئک ایسڈ میں کتنی قسم کے پروٹون ہیں؟','10. په بیوټانویک اسید کې څو ډوله پروټونونه شته؟','a. 8   b. 2   c. 6   d. 4','a. 8   b. 2   c. 6   d. 4','a. 8   b. 2   c. 6   d. 4'),
 ('11. In combustion analysis water is absorbed by','11. احتراقی تجزیے میں پانی کس میں جذب ہوتا ہے','11. د سوځېدنې په تحلیل کې اوبه د څه په واسطه جذبېږي','a. Mg(ClO₄)₂   b. NaOH   c. CuO   d. CuSO₄','a. Mg(ClO₄)₂   b. NaOH   c. CuO   d. CuSO₄','a. Mg(ClO₄)₂   b. NaOH   c. CuO   d. CuSO₄'),
 ('12. Modern methods of analysis are superior to classical one because','12. تجزیے کے جدید طریقے روایتی طریقوں سے بہتر ہیں کیونکہ','12. د تحلیل عصري طریقې له کلاسیکو غوره دي ځکه','a. they give more accurate results.   b. small amounts of chemicals are used.   c. less time consuming.   d. all of the above.','a. یہ زیادہ درست نتائج دیتے ہیں۔   b. کیمیکلز کی تھوڑی مقدار استعمال ہوتی ہے۔   c. کم وقت لیتے ہیں۔   d. یہ سب۔','a. ډېرې دقیقې پایلې ورکوي.   b. د کیمیکلونو لږ مقدار کارېږي.   c. لږ وخت نیسي.   d. پورته ټول.'),
 ('13. Which one is an in-plane bending vibration?','13. ان میں سے کون سا مستوی کے اندر جھکاؤ والا ارتعاش ہے؟','13. کوم یو د سطحې دننه کږېدونکی اهتزاز دی؟','a. Wagging   b. Scissoring   c. Twisting   d. None of these','a. ہلنا   b. قینچی نما   c. بل کھانا   d. ان میں سے کوئی نہیں','a. ښورېدل   b. قیچي   c. تاوېدل   d. له دې هېڅ یو'),
 ('14. Pi to pi star transition occurs in','14. پائی سے پائی سٹار منتقلی کس میں ہوتی ہے','14. له پای څخه پای ستوري ته انتقال په کوم کې کېږي','a. ethane.   b. ethene.   c. ethyl alcohol.   d. methyl chloride.','a. ایتھین۔   b. ایتھین (ایتھیلین)۔   c. ایتھائل الکوحل۔   d. میتھائل کلورائیڈ۔','a. ایتان.   b. ایتین.   c. ایتیل الکول.   d. میتایل کلوراید.'),
 ('15. Which one is NMR inactive nucleus?','15. کون سا مرکزہ NMR غیر فعال ہے؟','15. کومه هسته NMR غیر فعاله ده؟','a. ³¹C   b. ¹H   c. ¹⁵N   d. ¹⁶O','a. ³¹C   b. ¹H   c. ¹⁵N   d. ¹⁶O','a. ³¹C   b. ¹H   c. ¹⁵N   d. ¹⁶O')]
for q in M:lines([q[:3],q[3:]])
add('Q2. Write short answers of the following questions.','سوال 2. درج ذیل سوالات کے مختصر جوابات لکھیں۔','پوښتنه 2. د لاندې پوښتنو لنډ ځوابونه ولیکئ.','heading')
lines([('i. What is meant by stretching and bending vibrations?','i. کھنچاؤ اور جھکاؤ والے ارتعاشات سے کیا مراد ہے؟','i. له کشېدونکو او کږېدونکو اهتزازاتو څخه مطلب څه دی؟'),
 ('ii. If a compound shows 100% transmittance, what do we infer from it?','ii. اگر کوئی مرکب 100% ترسیل دکھائے تو ہم اس سے کیا نتیجہ نکالتے ہیں؟','ii. که یو مرکب 100% تېرېدنه وښيي، موږ ترې څه پایله اخلو؟'),
 ('iii. What does λmax mean to you?','iii. λmax سے آپ کیا سمجھتے ہیں؟','iii. له λmax څخه تاسو څه پوهېږئ؟'),
 ('iv. Define and explain Bear-Lambert’s Law.','iv. بیئر–لیمبرٹ قانون کی تعریف اور وضاحت کریں۔','iv. د بیر–لمبرټ قانون تعریف او تشریح کړئ.'),
 ('v. Why tetramethyl silane is used as a standard in NMR spectroscopy?','v. NMR سپیکٹروسکوپی میں ٹیٹرا میتھائل سائلین کو معیار کے طور پر کیوں استعمال کیا جاتا ہے؟','v. په NMR سپکټروسکوپي کې ټېټرا میتایل سایلین ولې د معیار په توګه کارېږي؟'),
 ('vi. Explain the use of ionization chamber in mass spectrometer.','vi. ماس سپیکٹرومیٹر میں آئنائزیشن چیمبر کے استعمال کی وضاحت کریں۔','vi. په ماس سپکټرومیټر کې د ایونایزېشن خونې کارونه تشریح کړئ.'),
 ('vii. Why magnesium perchlorate is used as H₂O absorber?','vii. میگنیشیم پرکلوریٹ کو H₂O جاذب کے طور پر کیوں استعمال کیا جاتا ہے؟','vii. مګنیزیم پرکلورېټ ولې د H₂O جذبوونکي په توګه کارېږي؟'),
 ('viii. Why modern method of analysis is superior over classical method of analysis?','viii. تجزیے کا جدید طریقہ روایتی طریقے سے کیوں بہتر ہے؟','viii. د تحلیل عصري طریقه له کلاسیکې طریقې ولې غوره ده؟')])
r=section('24.12','Unit 24 exercise: MCQs 1–15 and short questions i–viii','یونٹ 24 مشق: کثیر انتخابی 1–15 اور مختصر سوالات i–viii','د 24 واحد تمرین: څو انتخابي 1–15 او لنډې پوښتنې i–viii',P,L,B,'380–381')
r['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':193,'printedPages':[380,381]}];r['sourceContinuesOnPdfPage']=194
issues=[{'id':'chem12-p380-381-printing','printedPage':380,'description':'MCQ 2 option d refers to "(v)" though only (i)–(iv) are listed; MCQ 9 "1,1-dicholorethane"; MCQ 15 option "³¹C" — all retained as printed.'}]
carry=[{'from':'24.12','to':'24.13','startsAt':'Mass spectrum of on element'}]
if __name__=='__main__':save(193,[r],carry=carry,issues=issues,chapter_number=24)
