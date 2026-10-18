"""PDF180 printed354–355: Unit 23 Key Points; Exercise MCQs 1–10."""
from class12_chemistry_opening import pair,section,SOURCE,ROOT
from class12_chemistry_sync import save
def builder():
 P=[];L=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def lines(rows,kind='lines'):
  s0=len(P)
  for r in rows:P.append(pair(*r))
  L.append({'type':kind,'indices':list(range(s0,len(P)))})
 return P,L,add,lines
P,L,add,lines=builder()
add('Key Points','اہم نکات','مهم ټکي','heading')
lines([('Environmental chemistry is the branch of chemistry which deals with the presence of harmful and hazardous chemical and bio-chemicals in nature.','ماحولیاتی کیمیا کیمیا کی وہ شاخ ہے جو فطرت میں نقصان دہ اور خطرناک کیمیائی اور حیاتی کیمیائی مادوں کی موجودگی سے متعلق ہے۔','چاپېریالي کیمیا د کیمیا هغه څانګه ده چې په طبیعت کې د زیانمنو او خطرناکو کیمیاوي او ژوندکیمیاوي موادو له شتون سره سروکار لري.'),
 ('Pollutant is any substance which contaminate our environment.','آلودگی ہر وہ مادہ ہے جو ہمارے ماحول کو آلودہ کرے۔','ککړوونکی هره هغه ماده ده چې زموږ چاپېریال ککړ کړي.'),
 ('Atmosphere is a big blanket of gases, surrounding the Earth’s surface.','فضا گیسوں کا ایک بڑا کمبل ہے جو زمین کی سطح کو گھیرے ہوئے ہے۔','اتموسفیر د ګازونو یو لوی پوښ دی چې د ځمکې سطحه یې را ګرځولې.'),
 ('The term acid rain is referred to all precipitation (rain, snow or dew) having pH less than 5.6.','تیزابی بارش کی اصطلاح 5.6 سے کم pH والی ہر ترسیب (بارش، برف یا شبنم) کے لیے ہے۔','د تېزابي باران اصطلاح هر هغه ورښت (باران، واوره یا شبنم) ته ویل کېږي چې pH یې له 5.6 کم وي.'),
 ('Smog is the combination of smoke and fog.','سموگ دھوئیں اور دھند کا مجموعہ ہے۔','سموګ د لوګي او لړې ترکیب دی.'),
 ('Water is an important natural resource on this planet.','پانی اس سیارے پر ایک اہم قدرتی وسیلہ ہے۔','اوبه په دې سیاره کې یوه مهمه طبیعي سرچینه ده.'),
 ('An important aspect of water quality is the amount of dissolved oxygen in it.','پانی کے معیار کا ایک اہم پہلو اس میں حل شدہ آکسیجن کی مقدار ہے۔','د اوبو د کیفیت یو مهم اړخ په هغو کې د حل شوي اکسیجن اندازه ده.'),
 ('The term green chemistry is defined as the invention, design and application of chemical products and processes to reduce or to eliminate the use and generation of hazardous substances.','سبز کیمیا کی تعریف خطرناک مادوں کے استعمال اور پیداوار کو کم یا ختم کرنے کے لیے کیمیائی مصنوعات اور عمل کی ایجاد، ڈیزائن اور استعمال کے طور پر کی جاتی ہے۔','شنه کیمیا د خطرناکو موادو د کارونې او تولید د کمولو یا له منځه وړلو لپاره د کیمیاوي محصولاتو او عملیو د اختراع، ډیزاین او کارونې په توګه تعریفېږي.'),
 ('There are two major types of smog: ‘industrial smog’ and ‘photochemical smog’.','سموگ کی دو بڑی اقسام ہیں: ’صنعتی سموگ‘ اور ’فوٹو کیمیکل سموگ‘۔','د سموګ دوه لوی ډولونه شته: ’صنعتي سموګ‘ او ’فوټوکیمیکل سموګ‘.'),
 ('Increased concentration of CO₂ increases the Earth’s temperature, by greenhouse effect. This in turn results in climate changes and global warming.','CO₂ کا بڑھا ہوا ارتکاز گرین ہاؤس اثر سے زمین کا درجہ حرارت بڑھاتا ہے۔ اس کے نتیجے میں موسمیاتی تبدیلیاں اور عالمی حدت ہوتی ہیں۔','د CO₂ زیات شوی غلظت د شنه خونې اغېز په واسطه د ځمکې تودوخه زیاتوي. دا په خپل وار د اقلیم بدلونونو او نړیوالې تودوخې لامل کېږي.')],'list')
r10=section('23.10','Unit 23 Key Points','یونٹ 23 اہم نکات','د 23 واحد مهم ټکي',P,L,[],'354')
r10['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':180,'printedPages':[354]}]
P,L,add,lines=builder()
add('Exercise','مشق','تمرین','heading')
add('Q I. Choose the correct one from the given options.','سوال I. دیے گئے اختیارات میں سے درست کا انتخاب کریں۔','پوښتنه I. له ورکړل شویو انتخابونو څخه سم یې وټاکئ.','heading')
M=[('1. Which one of the following is not a secondary pollutant?','1. درج ذیل میں سے کون سا ثانوی آلودگی نہیں؟','1. له لاندې څخه کوم یو دویمي ککړوونکی نه دی؟','a. O₃   b. H₂CO₃   c. H₂SO₄   d. CO₂','a. O₃   b. H₂CO₃   c. H₂SO₄   d. CO₂','a. O₃   b. H₂CO₃   c. H₂SO₄   d. CO₂'),
 ('2. The coldest region of atmosphere is','2. فضا کا سب سے ٹھنڈا خطہ ہے','2. د اتموسفیر تر ټولو سړه سیمه ده','a. troposphere.   b. thermosphere.   c. stratosphere.   d. mesosphere.','a. ٹروپوسفیئر۔   b. تھرموسفیئر۔   c. سٹریٹوسفیئر۔   d. میسوسفیئر۔','a. ټروپوسفیر.   b. ترموسفیر.   c. سټراټوسفیر.   d. مېزوسفیر.'),
 ('3. Ozone layer in upper atmosphere is being destroyed by','3. بالائی فضا میں اوزون تہہ کس سے تباہ ہو رہی ہے','3. په پورتني اتموسفیر کې د اوزون طبقه د څه په واسطه ویجاړېږي','a. chlorofluorocarbons.   b. SO₂.   c. smog.   d. photochemical oxidant.','a. کلورو فلورو کاربنز۔   b. SO₂۔   c. سموگ۔   d. فوٹو کیمیکل تکسیدی۔','a. کلورو فلورو کاربنونه.   b. SO₂.   c. سموګ.   d. فوټوکیمیکل اکسیډانټ.'),
 ('4. Drained sewage has BOD.','4. نکاسی شدہ سیوریج کا BOD ہوتا ہے۔','4. ایستل شوې فاضله اوبه BOD لري.','a. more than that of water.   b. less than that of water.   c. equal to that of water.   d. none of above.','a. پانی سے زیادہ۔   b. پانی سے کم۔   c. پانی کے برابر۔   d. ان میں سے کوئی نہیں۔','a. له اوبو ډېر.   b. له اوبو لږ.   c. له اوبو سره برابر.   d. له پورته هېڅ یو.'),
 ('5. Photochemical smog is primarily caused by','5. فوٹو کیمیکل سموگ بنیادی طور پر کس سے ہوتا ہے','5. فوټوکیمیکل سموګ اساساً د څه له امله رامنځته کېږي','a. CO.   b. CO₂.   c. O₃.   d. NO₂','a. CO۔   b. CO₂۔   c. O₃۔   d. NO₂','a. CO.   b. CO₂.   c. O₃.   d. NO₂'),
 ('6. Result of ozone hole is','6. اوزون سوراخ کا نتیجہ ہے','6. د اوزون سوري پایله ده','a. acid rain.   b. global warming.   c. increased amount of CO₂.   d. greater exposure of Earth to U.V.','a. تیزابی بارش۔   b. عالمی حدت۔   c. CO₂ کی بڑھی ہوئی مقدار۔   d. زمین کا U.V. کے سامنے زیادہ آنا۔','a. تېزابي باران.   b. نړیواله تودوخه.   c. د CO₂ زیاته اندازه.   d. U.V. ته د ځمکې ډېر مخ کېدل.'),
 ('7. Which one of the following substances is not present in acid rain?','7. درج ذیل میں سے کون سا مادہ تیزابی بارش میں موجود نہیں؟','7. له لاندې موادو څخه کوم یو په تېزابي باران کې نشته؟','a. H₂SO₄   b. HNO₃   c. H₂SO₃   d. CH₃COOH','a. H₂SO₄   b. HNO₃   c. H₂SO₃   d. CH₃COOH','a. H₂SO₄   b. HNO₃   c. H₂SO₃   d. CH₃COOH'),
 ('8. Photochemical oxidant PAN is formed by','8. فوٹو کیمیکل تکسیدی PAN کس سے بنتا ہے','8. فوټوکیمیکل اکسیډانټ PAN د څه په واسطه جوړېږي','a. the action of oxide of nitrogen on hydrocarbons in presence of sunlight.   b. action of carbon dioxide on hydrocarbon in presence of sunlight.   c. action of hydrogen sulphide on hydrocarbon in presence of sunlight.   d. action of SO₂ and hydrocarbons.','a. دھوپ کی موجودگی میں ہائیڈروکاربنز پر نائٹروجن آکسائیڈ کے عمل سے۔   b. دھوپ کی موجودگی میں ہائیڈروکاربن پر کاربن ڈائی آکسائیڈ کے عمل سے۔   c. دھوپ کی موجودگی میں ہائیڈروکاربن پر ہائیڈروجن سلفائیڈ کے عمل سے۔   d. SO₂ اور ہائیڈروکاربنز کے عمل سے۔','a. د لمر رڼا په شتون کې پر هایدروکاربنونو د نایټروجن اکساید عمل.   b. د لمر رڼا په شتون کې پر هایدروکاربن د کاربن ډای اکساید عمل.   c. د لمر رڼا په شتون کې پر هایدروکاربن د هایدروجن سلفاید عمل.   d. د SO₂ او هایدروکاربنونو عمل.'),
 ('9. Which two main gases are produced when you burn a piece of wood?','9. لکڑی کا ٹکڑا جلانے پر کون سی دو بڑی گیسیں بنتی ہیں؟','9. کله چې د لرګي یوه ټوټه وسوځوئ کوم دوه اصلي ګازونه تولیدېږي؟','a. Oxygen and nitrogen   b. Carbon dioxide and oxygen   c. Carbon dioxide and steam   d. Carbon dioxide and nitrogen','a. آکسیجن اور نائٹروجن   b. کاربن ڈائی آکسائیڈ اور آکسیجن   c. کاربن ڈائی آکسائیڈ اور بھاپ   d. کاربن ڈائی آکسائیڈ اور نائٹروجن','a. اکسیجن او نایټروجن   b. کاربن ډای اکساید او اکسیجن   c. کاربن ډای اکساید او بخار   d. کاربن ډای اکساید او نایټروجن'),
 ('10. The temperature range of troposphere is','10. ٹروپوسفیئر کے درجہ حرارت کی حد ہے','10. د ټروپوسفیر د تودوخې پوله ده','a. 15 to –56.   b. 56 to –2.   c. –2 to –92.   d. –92 to 1200.','a. 15 سے –56۔   b. 56 سے –2۔   c. –2 سے –92۔   d. –92 سے 1200۔','a. 15 تر –56.   b. 56 تر –2.   c. –2 تر –92.   d. –92 تر 1200.')]
for q in M:lines([q[:3],q[3:]])
r11=section('23.11','Unit 23 exercise: MCQs 1–10','یونٹ 23 مشق: کثیر انتخابی 1–10','د 23 واحد تمرین: څو انتخابي 1–10',P,L,[],'355')
r11['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':180,'printedPages':[355]}];r11['insertBefore']='23.exercise.solved';r11['sourceContinuesOnPdfPage']=181
tail=(ROOT/'docs/source-verification/class-12/legacy/chem23-tail-from-printed352.txt').read_text(encoding='utf-8')
rest=tail[tail.index('11. In which of the following layer'):]
holder={'id':'23.12','title':'Textbook lesson extract (printed 356–357, pending source authoring)','theory':rest,'content':rest.replace('\n','<br>'),'sciNote':'','insertBefore':'23.exercise.solved','sourcePendingAuthoring':True}
if __name__=='__main__':save(180,[r10,r11,holder],chapter_number=23)
