"""PDF83 printed158–159: Unit 16 exercise — MCQs, short questions, start of detailed questions."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows):
 start=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':'lines','indices':list(range(start,len(paras)))})
add('Exercise','مشق','تمرین','heading')
add('Q I. Choose the correct one from the given options.','سوال I. دیے گئے اختیارات میں سے درست کا انتخاب کریں۔','پوښتنه I. له ورکړل شویو انتخابونو څخه سم یې وټاکئ.','heading')
mcq=[
 (('1. The number of possible isomers for an alkane having the molecular formula C₅H₁₂ is','1. سالماتی فارمولا C₅H₁₂ والے الکین (اکیلے بند والے) کے ممکنہ آئسومروں کی تعداد ہے','1. د C₅H₁₂ مالیکولي فورمول لرونکي الکان د ممکنه ایزومرونو شمېر دی'),
  ('a. 2   b. 3   c. 4   d. 5','a. 2   b. 3   c. 4   d. 5','a. 2   b. 3   c. 4   d. 5')),
 (('2. 2,2,3,3-terabromobutane when heated with zinc dust, yields','2. 2،2،3،3-ٹیٹرا برومو بیوٹین کو زنک کے سفوف کے ساتھ گرم کرنے پر حاصل ہوتا ہے','2. 2،2،3،3-ټیټرا بروموبیوټان چې د جستو له دوړو سره تود شي، ورکوي'),
  ('a. but–1–yne   b. but–2–yne   c. isobutylene   d. pent–1–yne','a. بیوٹ–1–ائن   b. بیوٹ–2–ائن   c. آئسوبیوٹیلین   d. پینٹ–1–ائن','a. بیوټ–1–این   b. بیوټ–2–این   c. ایزوبیوټیلین   d. پېنټ–1–این')),
 (('3. But–2–yne can be converted into cis–but–2–ene by using','3. بیوٹ–2–ائن کو cis–بیوٹ–2–این میں تبدیل کیا جا سکتا ہے استعمال کر کے','3. بیوټ–2–این په cis–بیوټ–2–ین بدلېدای شي د دې په کارولو'),
  ('a. H₂/Ni   b. Lindlar’s catalyst   c. Na/liq. NH₃   d. Zn/HCl','a. H₂/Ni   b. لنڈلار کا عمل انگیز   c. Na/مائع NH₃   d. Zn/HCl','a. H₂/Ni   b. د لینډلار کتلست   c. Na/مایع NH₃   d. Zn/HCl')),
 (('4. When excess of HCl is added to acetylene, the product is','4. جب ایسیٹیلین میں HCl کی زیادتی شامل کی جائے تو پیداوار ہے','4. کله چې اسیتیلین ته ډېر HCl ورزیات شي، محصول دی'),
  ('a. vinyl chloride.   b. ethyl chloride.   c. 1,2-dichloroethane.   d. 1,1–dichloroethane.','a. وائنائل کلورائیڈ۔   b. ایتھائل کلورائیڈ۔   c. 1،2-ڈائی کلورو ایتھین۔   d. 1،1–ڈائی کلورو ایتھین۔','a. وینایل کلوراید.   b. ایتیل کلوراید.   c. 1،2-ډای کلوروایتان.   d. 1،1–ډای کلوروایتان.')),
 (('5. The homolytic fission of C-H bond in an alkane results in','5. الکین (اکیلے بند والے) میں C-H بند کی ہومولائٹک تقسیم سے بنتا ہے','5. په الکان کې د C-H تړون هومولیتیک وېش پایله یې ده'),
  ('a. carbanion.   b. carbocation.   c. alkyl free radical.   d. all of these.','a. کاربینائن۔   b. کاربوکیٹائن۔   c. الکائل آزاد ریڈیکل۔   d. یہ سب۔','a. کاربانیون.   b. کاربوکاټیون.   c. الکایل ازاد رادیکال.   d. دا ټول.')),
 (('6. The groups that deactivate benzene ring and is o/p-directing','6. وہ گروپ جو بینزین حلقے کو غیر فعال کرے اور o/p-سمت دینے والا ہو','6. هغه ګروپ چې د بنزین کړۍ غیر فعالوي او o/p-لارښوونکی دی'),
  ('a. –NH₂   b. – OH   c. – OCH₃   d. – Cl','a. –NH₂   b. – OH   c. – OCH₃   d. – Cl','a. –NH₂   b. – OH   c. – OCH₃   d. – Cl')),
 (('7. Alkene that can be expected to exhibit geometrical isomerism','7. وہ الکین (دوہرے بند والا) جس سے جیومیٹریکل آئسومرزم کی توقع کی جا سکتی ہے','7. هغه الکین چې تمه کېږي جیومټریکي ایزومېریزم وښيي'),
  ('a. but–1–ene   b. 2–methylbut–2–ene   c. 2–methylpropene   d. none of these','a. بیوٹ–1–این   b. 2–میتھائل بیوٹ–2–این   c. 2–میتھائل پروپین   d. ان میں سے کوئی نہیں','a. بیوټ–1–ین   b. 2–میتایل بیوټ–2–ین   c. 2–میتایل پروپین   d. هېڅ یو نه')),
 (('8. How many isomers are possible for C₂H₆O?','8. C₂H₆O کے کتنے آئسومر ممکن ہیں؟','8. د C₂H₆O لپاره څو ایزومرونه ممکن دي؟'),
  ('a. 2   b. 4   c. 8   d. 5','a. 2   b. 4   c. 8   d. 5','a. 2   b. 4   c. 8   d. 5')),
 (('9. Addition of HBr to isobutylene mainly gives','9. آئسوبیوٹیلین میں HBr کا اضافہ زیادہ تر دیتا ہے','9. ایزوبیوټیلین ته د HBr زیاتول ډېری ورکوي'),
  ('a. n–butyl bromide.   b. isobutyl bromide.   c. sec–butyl bromide.   d. tert–butyl bromide.','a. n–بیوٹائل برومائیڈ۔   b. آئسوبیوٹائل برومائیڈ۔   c. sec–بیوٹائل برومائیڈ۔   d. tert–بیوٹائل برومائیڈ۔','a. n–بیوټیل برومایډ.   b. ایزوبیوټیل برومایډ.   c. sec–بیوټیل برومایډ.   d. tert–بیوټیل برومایډ.')),
 (('10. An alkene upon ozonolysis yield a mixture of acetone and acetaldehyde. The alkene is','10. ایک الکین (دوہرے بند والا) اوزونولائسز پر ایسیٹون اور ایسیٹ الڈیہائیڈ کا آمیزہ دیتا ہے۔ وہ الکین ہے','10. یو الکین د اوزونولایسس پر مهال د اسیتون او اسیټالدیهاید ګډوله ورکوي. هغه الکین دی'),
  ('a. isobutylene   b. but–2–ene   c. 2–methylbut–2–ene   d. pent–2–ene','a. آئسوبیوٹیلین   b. بیوٹ–2–این   c. 2–میتھائل بیوٹ–2–این   d. پینٹ–2–این','a. ایزوبیوټیلین   b. بیوټ–2–ین   c. 2–میتایل بیوټ–2–ین   d. پېنټ–2–ین')),
 (('11. Dehydrohalogenation of alkylhalide is carried out in presence of','11. الکائل ہیلائیڈ کی ڈی ہائیڈروہیلوجینیشن کس کی موجودگی میں کی جاتی ہے','11. د الکایل هالایډ ډی هایدروهالوجینېشن د څه په شتون کې ترسره کېږي'),
  ('a. Zn dust.   b. conc. H₂SO₄.   c. alcoholic KOH.   d. aqueous KOH.','a. زنک کا سفوف۔   b. مرتکز H₂SO₄۔   c. الکوحلی KOH۔   d. آبی KOH۔','a. د جستو دوړې.   b. غلیظ H₂SO₄.   c. الکولي KOH.   d. اوبلن KOH.')),
 (('12. Which of the following molecules contain chiral center?','12. درج ذیل میں سے کس سالمے میں کائرل مرکز ہے؟','12. له لاندې مالیکولونو څخه کوم یو کایرل مرکز لري؟'),
  ('a. n–butyl bromide   b. isobutyl bromide   c. sec–butyl bromide   d. tert–butyl bromide','a. n–بیوٹائل برومائیڈ   b. آئسوبیوٹائل برومائیڈ   c. sec–بیوٹائل برومائیڈ   d. tert–بیوٹائل برومائیڈ','a. n–بیوټیل برومایډ   b. ایزوبیوټیل برومایډ   c. sec–بیوټیل برومایډ   d. tert–بیوټیل برومایډ')),
 (('13. In the following reaction C₆H₅CH₃ + Cl₂ —U.V. light→ C₆H₅CH₂Cl + HCl, what type of reaction has taken?','13. درج ذیل تعامل C₆H₅CH₃ + Cl₂ —U.V. light→ C₆H₅CH₂Cl + HCl میں کس قسم کا تعامل ہوا ہے؟','13. په لاندې تعامل C₆H₅CH₃ + Cl₂ —U.V. light→ C₆H₅CH₂Cl + HCl کې کوم ډول تعامل شوی؟'),
  ('a. Electrophilic substitution   b. Electrophilic addition   c. Free radical substitution   d. Free radical addition','a. الیکٹروفائلی تبادلہ   b. الیکٹروفائلی اضافہ   c. آزاد ریڈیکل تبادلہ   d. آزاد ریڈیکل اضافہ','a. الکتروفایلي بدلون   b. الکتروفایلي اضافه   c. د ازاد رادیکال بدلون   d. د ازاد رادیکال اضافه')),
 (('14. A compound when treated with sodium amide yields a salt. The compound is','14. ایک مرکب سوڈیم امائیڈ سے عمل کرانے پر نمک دیتا ہے۔ وہ مرکب ہے','14. یو مرکب چې له سوډیم اماید سره تعامل وکړي مالګه ورکوي. هغه مرکب دی'),
  ('a. C₂H₄   b. C₃H₄   c. C₆H₆   d. C₆H₁₂','a. C₂H₄   b. C₃H₄   c. C₆H₆   d. C₆H₁₂','a. C₂H₄   b. C₃H₄   c. C₆H₆   d. C₆H₁₂')),
 (('15. Nitrobenzene reacts with chlorine in presence of AlCl₃. The major product obtained is','15. نائٹرو بینزین AlCl₃ کی موجودگی میں کلورین سے تعامل کرتی ہے۔ حاصل ہونے والی بڑی پیداوار ہے','15. نایټروبنزین د AlCl₃ په شتون کې له کلورین سره تعامل کوي. ترلاسه شوی عمده محصول دی'),
  ('a. o–chloronitrobenzene.   b. m–chloronitrobenzene.   c. p–chloronitrobenzene.   d. no reaction occurs at all.','a. o–کلورو نائٹرو بینزین۔   b. m–کلورو نائٹرو بینزین۔   c. p–کلورو نائٹرو بینزین۔   d. کوئی تعامل نہیں ہوتا۔','a. o–کلورونایټروبنزین.   b. m–کلورونایټروبنزین.   c. p–کلورونایټروبنزین.   d. هېڅ تعامل نه کېږي.'))]
for q,o in mcq:lines([q,o])
add('Q2. Write short answers of the following questions.','سوال2. درج ذیل سوالات کے مختصر جواب لکھیں۔','پوښتنه2. د لاندې پوښتنو لنډ ځوابونه ولیکئ.','heading')
lines([
 ('i. What is the difference between aliphatic and aromatic hydrocarbons?','i. ایلیفیٹک اور ارومیٹک ہائیڈروکاربنوں میں کیا فرق ہے؟','i. د الیفاتیکو او اروماتیکو هایدروکاربنونو ترمنځ څه توپیر دی؟'),
 ('ii. What is plane polarized mono chromatic light?','ii. مستوی پولرائزڈ یک رنگی روشنی کیا ہے؟','ii. سطحي پولرایز شوې یو رنګه رڼا څه ده؟'),
 ('iii. How do you detect the unsaturation in alkenes?','iii. آپ الکینز (دوہرے بند والے) میں عدم سیرابیت کیسے معلوم کرتے ہیں؟','iii. په الکینونو کې نامشبوعیت څنګه معلوموئ؟'),
 ('iv. Why benzene is less reactive than ethene but more reactive than ethane?','iv. بینزین ایتھین (دوہرے بند) سے کم مگر ایتھین (اکیلے بند) سے زیادہ تعامل پذیر کیوں ہے؟','iv. ولې بنزین له ایتین لږ خو له ایتان ډېر تعامل کوونکی دی؟'),
 ('v. Why halogens are deactivating groups although they are ortho/para directing?','v. ہیلوجنز اورتھو/پیرا سمت دینے والے ہونے کے باوجود غیر فعال کرنے والے گروپ کیوں ہیں؟','v. ولې هالوجنونه سره له دې چې اورتو/پارا لارښوونکي دي، غیر فعالوونکي ګروپونه دي؟'),
 ('vi. What is the basic difference between a chiral carbon and chirality?','vi. کائرل کاربن اور کائرلٹی میں بنیادی فرق کیا ہے؟','vi. د کایرل کاربن او کایرالیټي ترمنځ بنسټیز توپیر څه دی؟'),
 ('vii. Why there are no geometrical isomers of but-1-ene?','vii. بیوٹ-1-این کے جیومیٹریکل آئسومر کیوں نہیں ہوتے؟','vii. ولې د بیوټ-1-ین جیومټریکي ایزومرونه نشته؟'),
 ('viii. Why cyclopropane is more reactive than propane?','viii. سائیکلوپروپین، پروپین (اکیلے بند والی) سے زیادہ تعامل پذیر کیوں ہے؟','viii. ولې سایکلوپروپان له پروپان ډېر تعامل کوونکی دی؟'),
 ('ix. How can you distinguish 1-alkyne from other non-terminal alkynes?','ix. آپ 1-الکائن کو دوسرے غیر ٹرمینل الکائنز سے کیسے ممتاز کر سکتے ہیں؟','ix. 1-الکاین له نورو غیر ټرمینل الکاینونو څخه څنګه بېلولی شئ؟'),
 ('x. What is the main difference between tautomerism and resonance?','x. ٹاٹومرزم اور ریزونینس میں بنیادی فرق کیا ہے؟','x. د ټاټومېریزم او ریزونانس ترمنځ اصلي توپیر څه دی؟')])
add('Q3. Write detail answers of the following questions.','سوال3. درج ذیل سوالات کے تفصیلی جواب لکھیں۔','پوښتنه3. د لاندې پوښتنو تفصیلي ځوابونه ولیکئ.','heading')
lines([
 ('1. (a) Describe the mechanism of chlorination of methane in detail.','1. (a) میتھین کی کلورینیشن کا طریق کار تفصیل سے بیان کریں۔','1. (a) د میتان د کلورینېشن میکانیزم په تفصیل بیان کړئ.'),
 ('(b) Explain the structure and reactivity of cycloalkanes.','(b) سائیکلوالکینز کی ساخت اور تعامل پذیری واضح کریں۔','(b) د سایکلوالکانونو جوړښت او تعامل وړتیا روښانه کړئ.'),
 ('(c) Write down the physical properties of alkanes and cycloalkane.','(c) الکینز (اکیلے بند والے) اور سائیکلوالکین کی طبعی خصوصیات لکھیں۔','(c) د الکانونو او سایکلوالکان فزیکي ځانګړنې ولیکئ.'),
 ('2. (a) What are hydrocarbons? Explain the different classes of hydrocarbons.','2. (a) ہائیڈروکاربن کیا ہیں؟ ہائیڈروکاربنوں کی مختلف جماعتیں واضح کریں۔','2. (a) هایدروکاربنونه څه دي؟ د هایدروکاربنونو بېلابېل ټولګي روښانه کړئ.'),
 ('(b) Give methods for preparation of ethene from; (i) ethyl alcohol (ii) ethyl bromide','(b) ایتھین کی تیاری کے طریقے دیں؛ (i) ایتھائل الکوحل سے (ii) ایتھائل برومائیڈ سے','(b) د ایتین د چمتو کولو طریقې ورکړئ؛ (i) له ایتیل الکول (ii) له ایتیل برومایډ'),
 ('(c) Explain the relative stabilities of different alkenes.','(c) مختلف الکینز (دوہرے بند والے) کی اضافی پائیداری واضح کریں۔','(c) د بېلابېلو الکینونو نسبي ثبات روښانه کړئ.'),
 ('3. (a) Describe any two methods for preparation of alkynes.','3. (a) الکائنز کی تیاری کے کوئی دو طریقے بیان کریں۔','3. (a) د الکاینونو د چمتو کولو هر دوه طریقې بیان کړئ.'),
 ('(b) Discuss the acidity of terminal alkynes. How terminal alkynes can be distinguished from non-terminal alkynes?','(b) ٹرمینل الکائنز کی تیزابیت پر بحث کریں۔ ٹرمینل الکائنز کو غیر ٹرمینل الکائنز سے کیسے ممتاز کیا جا سکتا ہے؟','(b) د ټرمینل الکاینونو پر تېزابیت بحث وکړئ. ټرمینل الکاینونه له غیر ټرمینل الکاینونو څخه څنګه بېلېدای شي؟')])
record=section('16.30','Unit 16 exercise: MCQs, short and detailed questions','یونٹ 16 مشق: کثیر انتخابی، مختصر اور تفصیلی سوالات','د 16 واحد تمرین: څو انتخابي، لنډې او تفصیلي پوښتنې',paras,layout,blocks,'158–159')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':83,'printedPages':[158,159]}]
record['sourceContinuesOnPdfPage']=84
issues=[{'id':'chem12-p158-terabromobutane','printedPage':158,'description':'MCQ 2 printed "terabromobutane" retained in English.'}]
if __name__=='__main__':save(83,[record],issues=issues,chapter_number=16)
