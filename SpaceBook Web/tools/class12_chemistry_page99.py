"""PDF99 printed190–191: Unit 17 exercise — MCQs, short questions, Q3 1."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':'lines','indices':list(range(s0,len(paras)))})
add('Exercise','مشق','تمرین','heading')
add('Q I. Choose the correct one from the given options.','سوال I. دیے گئے اختیارات میں سے درست کا انتخاب کریں۔','پوښتنه I. له ورکړل شویو انتخابونو څخه سم یې وټاکئ.','heading')
M=[
 ('1. The reaction of CH₃MgI with acetone followed by hydrolysis gives','1. CH₃MgI کا ایسیٹون سے تعامل اور پھر ہائیڈرولائسز دیتا ہے','1. له اسیتون سره د CH₃MgI تعامل او ورپسې هایدرولیز ورکوي',
  'a. tert-butyl alcohol.   b. sec-butyl alcohol.   c. n-butyl alcohol.   d. none of these.','a. ٹرشری بیوٹائل الکوحل۔   b. سیکنڈری بیوٹائل الکوحل۔   c. n-بیوٹائل الکوحل۔   d. ان میں سے کوئی نہیں۔','a. ټرشري بیوټیل الکول.   b. سېکنډري بیوټیل الکول.   c. n-بیوټیل الکول.   d. هېڅ یو نه.'),
 ('2. Which one of the following halide is most reactive towards nucleophilic substitution reaction?','2. درج ذیل میں سے کون سا ہیلائیڈ نیوکلیوفائلی تبادلے کے تعامل کے لیے سب سے زیادہ تعامل پذیر ہے؟','2. له لاندې هالایډونو څخه کوم یو د نیوکلیوفایلي بدلون تعامل ته تر ټولو ډېر تعامل کوونکی دی؟',
  'a. C₂H₅Br   b. C₂H₅I   c. C₂H₅F   d. C₂H₅Cl','a. C₂H₅Br   b. C₂H₅I   c. C₂H₅F   d. C₂H₅Cl','a. C₂H₅Br   b. C₂H₅I   c. C₂H₅F   d. C₂H₅Cl'),
 ('3. An electron deficient specie is','3. الیکٹرانوں کی کمی والی نوع ہے','3. د الکترون کمښت لرونکی ډول دی',
  'a. electrophile   b. nucleophile   c. Lewis base   d. none','a. الیکٹروفائل   b. نیوکلیوفائل   c. لیوس اساس   d. کوئی نہیں','a. الکتروفایل   b. نیوکلیوفایل   c. لیوس قلوي   d. هېڅ یو'),
 ('4. R–CH₂–X is an example of','4. R–CH₂–X مثال ہے','4. R–CH₂–X بېلګه ده د',
  'a. primary alkyl halide.   b. secondary alkyl halide.   c. tertiary alkyl halide.   d. both (a) and (b).','a. ابتدائی الکائل ہیلائیڈ کی۔   b. ثانوی الکائل ہیلائیڈ کی۔   c. ثالثی الکائل ہیلائیڈ کی۔   d. (a) اور (b) دونوں کی۔','a. لومړني الکایل هالایډ.   b. دویمي الکایل هالایډ.   c. درېیمي الکایل هالایډ.   d. (a) او (b) دواړو.'),
 ('5. The carbon atom carrying positive charge and attached to three other atoms or groups is called','5. مثبت چارج والا اور تین دوسرے ایٹموں یا گروپوں سے جڑا کاربن ایٹم کہلاتا ہے','5. هغه کاربني اټوم چې مثبت چارج لري او له دریو نورو اټومونو یا ګروپونو سره تړلی وي، بلل کېږي',
  'a. Carbocation   b. Carbanion   c. Oxonium ion   d. Carbene','a. کاربوکیٹائن   b. کاربینائن   c. آکسونیم آئن   d. کاربین','a. کاربوکاټیون   b. کاربانیون   c. اکسونیم ایون   d. کاربین'),
 ('6. Grignard reagent can be represented by general formula','6. گرینیارڈ عامل کو عمومی فارمولے سے ظاہر کیا جا سکتا ہے','6. ګرینیارډ عامل د عمومي فورمول په واسطه ښودل کېدای شي',
  'a. R–Mg–NH₂   b. R–Mg–OR   c. R–Mg–OH   d. R–Mg–X','a. R–Mg–NH₂   b. R–Mg–OR   c. R–Mg–OH   d. R–Mg–X','a. R–Mg–NH₂   b. R–Mg–OR   c. R–Mg–OH   d. R–Mg–X'),
 ('7. The end product of reaction of a Grignard reagent with ethyl acetate is','7. ایتھائل ایسیٹیٹ سے گرینیارڈ عامل کے تعامل کی آخری پیداوار ہے','7. له ایتیل اسیټېټ سره د ګرینیارډ عامل د تعامل وروستی محصول دی',
  'a. primary alcohol.   b. secondary alcohol.   c. tertiary alcohol.   d. methyl alcohol.','a. ابتدائی الکوحل۔   b. ثانوی الکوحل۔   c. ثالثی الکوحل۔   d. میتھائل الکوحل۔','a. لومړنی الکول.   b. دویمی الکول.   c. درېیمی الکول.   d. میتایل الکول.'),
 ('8. An electron-pair donor is','8. الیکٹرانی جوڑا دینے والا ہے','8. د الکتروني جوړې ورکوونکی دی',
  'a. Lewis acid   b. Electrophile   b. Nucleophile   d. Free radical','a. لیوس تیزاب   b. الیکٹروفائل   b. نیوکلیوفائل   d. آزاد ریڈیکل','a. لیوس اسید   b. الکتروفایل   b. نیوکلیوفایل   d. ازاد رادیکال'),
 ('9. In secondary alkyl halides the carbon atom to which the halo group is attached is in turn bonded directly to','9. ثانوی الکائل ہیلائیڈز میں جس کاربن ایٹم سے ہیلو گروپ جڑا ہو وہ آگے براہِ راست جڑا ہوتا ہے','9. په دویمیو الکایل هالایډونو کې هغه کاربني اټوم چې هالو ګروپ ورسره تړلی، په خپل وار مستقیم تړلی دی له',
  'a. one other carbon.   b. two other carbons.   c. three other carbons.   d. four other carbons.','a. ایک دوسرے کاربن سے۔   b. دو دوسرے کاربنوں سے۔   c. تین دوسرے کاربنوں سے۔   d. چار دوسرے کاربنوں سے۔','a. یوه بل کاربن.   b. دوو نورو کاربنونو.   c. دریو نورو کاربنونو.   d. څلورو نورو کاربنونو.'),
 ('10. Characteristics of SN1 reaction is','10. SN1 تعامل کی خصوصیت ہے','10. د SN1 تعامل ځانګړنه ده',
  'a. 100% inversion   b. 100% retention   c. partial racemization   d. none of these','a. 100% الٹ   b. 100% برقراری   c. جزوی ریسیمائزیشن   d. ان میں سے کوئی نہیں','a. 100% اوښتون   b. 100% ساتنه   c. نیمګړی ریسیمایزېشن   d. هېڅ یو نه'),
 ('11. Which of the following solvent is aprotic?','11. درج ذیل میں سے کون سا محلل اپروٹک ہے؟','11. له لاندې محللونو څخه کوم یو اپروټیک دی؟',
  'a. Acetone   b. Ethyl alcohol   c. Water   d. Formic acid','a. ایسیٹون   b. ایتھائل الکوحل   c. پانی   d. فارمک ایسڈ','a. اسیتون   b. ایتیل الکول   c. اوبه   d. فورمیک اسید'),
 ('12. Which of the following will not affect the SN1 mechanism?','12. درج ذیل میں سے کون سا SN1 طریق کار پر اثر نہیں ڈالے گا؟','12. له لاندې څخه کوم یو د SN1 پر میکانیزم اغېز نه کوي؟',
  'a. Nature of solvent.   b. Carbocation stability.   c. Nature of nucleophile.   d. None of these.','a. محلل کی نوعیت۔   b. کاربوکیٹائن کی پائیداری۔   c. نیوکلیوفائل کی نوعیت۔   d. ان میں سے کوئی نہیں۔','a. د محلل طبیعت.   b. د کاربوکاټیون ثبات.   c. د نیوکلیوفایل طبیعت.   d. هېڅ یو نه.'),
 ('13. Ethylmagnesium bromide on treatement with CO₂ and further hydrolysis gives','13. ایتھائل میگنیشیم برومائیڈ CO₂ سے عمل اور پھر ہائیڈرولائسز پر دیتا ہے','13. ایتیل مګنیزیم برومایډ له CO₂ سره د تعامل او ورپسې هایدرولیز پر مهال ورکوي',
  'a. acetic acid.   b. propanoic acid.   c. butanoic acid.   d. benzoic acid.','a. ایسیٹک ایسڈ۔   b. پروپانوئک ایسڈ۔   c. بیوٹانوئک ایسڈ۔   d. بینزوئک ایسڈ۔','a. اسیټیک اسید.   b. پروپانویک اسید.   c. بیوټانویک اسید.   d. بنزویک اسید.'),
 ('14. Geometry of methyl chloride is','14. میتھائل کلورائیڈ کی جیومیٹری ہے','14. د میتایل کلوراید جیومټري ده',
  'a. trigonal planar.   b. octahedral.   c. square planar.   d. tetrahedral.','a. تکونی مستوی۔   b. ہشت سطحی۔   c. مربع مستوی۔   d. چہار سطحی۔','a. درې ګوټی سطحي.   b. اته مخی.   c. مربع سطحي.   d. څلورمخی.'),
 ('15. The crowding around alpha carbon in alkyl halides favour','15. الکائل ہیلائیڈز میں الفا کاربن کے گرد ہجوم حق میں ہے','15. په الکایل هالایډونو کې د الفا کاربن شاوخوا ګڼه ګوڼه ملاتړ کوي',
  'a. elimination reaction.   b. substitution reaction.   c. addition reaction.   d. all of these.','a. اخراجی تعامل کے۔   b. تبادلے کے تعامل کے۔   c. اضافی تعامل کے۔   d. ان سب کے۔','a. د ایستلو تعامل.   b. د بدلون تعامل.   c. اضافي تعامل.   d. دا ټول.')]
for q in M:lines([q[:3],q[3:]])
add('Q2. Write short answers of the following questions.','سوال2. درج ذیل سوالات کے مختصر جواب لکھیں۔','پوښتنه2. د لاندې پوښتنو لنډ ځوابونه ولیکئ.','heading')
lines([
 ('i. Compare nucleophilic substitution reaction and electrophilic substitution reaction.','i. نیوکلیوفائلی تبادلے اور الیکٹروفائلی تبادلے کے تعامل کا موازنہ کریں۔','i. د نیوکلیوفایلي بدلون او الکتروفایلي بدلون تعامل پرتله کړئ.'),
 ('ii. Why alkyl halides undergo nucleophilic substitution while benzene undergo electrophilic substitution reactions?','ii. الکائل ہیلائیڈز نیوکلیوفائلی تبادلہ جبکہ بینزین الیکٹروفائلی تبادلے کے تعاملات کیوں کرتی ہے؟','ii. ولې الکایل هالایډونه نیوکلیوفایلي بدلون او بنزین الکتروفایلي بدلون تعاملونه کوي؟'),
 ('iii. Why tertiary carbocation is more stable?','iii. ثالثی کاربوکیٹائن زیادہ پائیدار کیوں ہے؟','iii. ولې درېیمی کاربوکاټیون ډېر ثابت دی؟'),
 ('iv. In a polar protic solvent, the SN1 and E1 reaction for the same tertiary alkyl halide, have equal rates. Explain.','iv. قطبی پروٹک محلل میں ایک ہی ثالثی الکائل ہیلائیڈ کے لیے SN1 اور E1 تعامل کی شرحیں برابر ہیں۔ وضاحت کریں۔','iv. په قطبي پروټیک محلل کې د ورته درېیمي الکایل هالایډ لپاره د SN1 او E1 تعامل سرعتونه برابر دي. روښانه یې کړئ.'),
 ('v. Fluoride ion is weak nucleophile in polar protic solvent and strong nucleophile in polar aprotic solvent. Explain.','v. فلورائیڈ آئن قطبی پروٹک محلل میں کمزور اور قطبی اپروٹک محلل میں طاقتور نیوکلیوفائل ہے۔ وضاحت کریں۔','v. فلوراید ایون په قطبي پروټیک محلل کې کمزوری او په قطبي اپروټیک محلل کې قوي نیوکلیوفایل دی. روښانه یې کړئ.'),
 ('vi. Why in SN2 the nucleophile attack on opposite side of leaving group?','vi. SN2 میں نیوکلیوفائل خارج ہونے والے گروپ کی مخالف جانب سے کیوں حملہ کرتا ہے؟','vi. ولې په SN2 کې نیوکلیوفایل د وتونکي ګروپ له مخالفې خوا برید کوي؟'),
 ('vii. Alkyl fluorides are least reactive while alkyl iodides are more reactive towards nucleophilic substitution. Why?','vii. نیوکلیوفائلی تبادلے کے لیے الکائل فلورائیڈز سب سے کم جبکہ الکائل آئیوڈائیڈز زیادہ تعامل پذیر ہیں۔ کیوں؟','vii. د نیوکلیوفایلي بدلون په وړاندې الکایل فلورایډونه تر ټولو لږ او الکایل ایوډایډونه ډېر تعامل کوونکي دي. ولې؟'),
 ('viii. Why secondary amines are more basic than tertiary in aqueous solution?','viii. آبی محلول میں ثانوی امائنز ثالثی سے زیادہ اساسی کیوں ہیں؟','viii. ولې په اوبلن محلول کې دویمي امینونه له درېیمیو ډېر قلوي دي؟'),
 ('ix. The structure of methyl carbocation is trigonal planar but not pyramidal. Why?','ix. میتھائل کاربوکیٹائن کی ساخت تکونی مستوی ہے ہرمی نہیں۔ کیوں؟','ix. د میتایل کاربوکاټیون جوړښت درې ګوټی سطحي دی نه هرمي. ولې؟'),
 ('x. Explain briefly the differernce between nuceophile and base.','x. نیوکلیوفائل اور اساس کا فرق مختصراً واضح کریں۔','x. د نیوکلیوفایل او قلوي توپیر په لنډه توګه روښانه کړئ.')])
add('Q3. Write detail answers of the following questions.','سوال3. درج ذیل سوالات کے تفصیلی جواب لکھیں۔','پوښتنه3. د لاندې پوښتنو تفصیلي ځوابونه ولیکئ.','heading')
lines([('1. (a) Discuss various methods of preparation of alkyl halides.','1. (a) الکائل ہیلائیڈز کی تیاری کے مختلف طریقوں پر بحث کریں۔','1. (a) د الکایل هالایډونو د چمتو کولو پر بېلابېلو طریقو بحث وکړئ.'),
 ('(b) Explain elimination reaction in alkyl halides.','(b) الکائل ہیلائیڈز میں اخراجی تعامل واضح کریں۔','(b) په الکایل هالایډونو کې د ایستلو تعامل روښانه کړئ.')])
record=section('17.15','Unit 17 exercise: MCQs and short questions','یونٹ 17 مشق: کثیر انتخابی اور مختصر سوالات','د 17 واحد تمرین: څو انتخابي او لنډې پوښتنې',paras,layout,blocks,'190–191')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':99,'printedPages':[190,191]}]
record['sourceContinuesOnPdfPage']=100
issues=[{'id':'chem12-p190-mcq-printing','printedPage':190,'description':'MCQ 8 options printed a, b, b, d (duplicate "b"); Q2 x printed "differernce … nuceophile"; MCQ 13 "treatement" — retained as printed.'}]
if __name__=='__main__':save(99,[record],issues=issues,chapter_number=17)
