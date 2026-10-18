"""PDF156 printed306–307: Unit 21 Key Points (end), Exercise Q1 MCQs 1–15, Q2 short answers, Q3 detailed 1–2."""
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
lines([('The substances, which decrease the activity of an enzyme, known as enzyme inhibitor and this process is known as enzyme inhibition.','وہ مادے جو خامرے کی سرگرمی کم کرتے ہیں خامروں کو روکنے والے کہلاتے ہیں اور اس عمل کو خامروں کی روک تھام کہتے ہیں۔','هغه مواد چې د انزایم فعالیت کموي، د انزایم مخنیوونکي بلل کېږي او دې عملیې ته د انزایم مخنیوی وايي.'),
 ('Lipids have three major subclasses: simple lipids, compound lipids and derived lipids.','لپڈز کی تین بڑی ذیلی جماعتیں ہیں: سادہ لپڈز، مرکب لپڈز اور ماخوذ لپڈز۔','لیپیډونه درې لویې فرعي ډلې لري: ساده لیپیډونه، مرکب لیپیډونه او مشتق لیپیډونه.'),
 ('The monomer that makes up a nucleic acid is called a nucleotide.','نیوکلک ایسڈ بنانے والے مونومر کو نیوکلیوٹائیڈ کہتے ہیں۔','هغه مونومر چې نیوکلیک اسید جوړوي نیوکلیوټایډ بلل کېږي.'),
 ('Nucleotide has three parts: an inorganic phosphate group, a five-carbon monosaccharide sugar, and a nitrogen containing structure known as a nitrogenous base.','نیوکلیوٹائیڈ کے تین حصے ہیں: ایک غیر نامیاتی فاسفیٹ گروپ، ایک پانچ کاربن والی مونوسیکرائیڈ شکر، اور نائٹروجن رکھنے والی ساخت جسے نائٹروجنی اساس کہتے ہیں۔','نیوکلیوټایډ درې برخې لري: یو غیر عضوي فاسفېټ ګروپ، یوه پنځه کاربنه مونوساکاریډ بوره، او یو نایټروجن لرونکی جوړښت چې نایټروجني قلوي بلل کېږي.'),
 ('DNA contains genetic information in the form of codes.','DNA میں جینیاتی معلومات کوڈز کی صورت میں ہوتی ہیں۔','DNA جنیټیکي معلومات د کوډونو په بڼه لري.'),
 ('Minerals essential for life are the inorganic nutrients.','زندگی کے لیے ضروری معدنیات غیر نامیاتی غذائی اجزا ہیں۔','د ژوند لپاره اړین منرالونه غیر عضوي غذايي مواد دي.'),
 ('Iron is a part of haemoglobin, a carrier of oxygen in the body.','لوہا ہیموگلوبن کا حصہ ہے جو جسم میں آکسیجن کا حامل ہے۔','اوسپنه د هیموګلوبین برخه ده چې په بدن کې د اکسیجن وړونکی دی.'),
 ('Calcium is the main constituent of bones and teeth.','کیلشیم ہڈیوں اور دانتوں کا بنیادی جزو ہے۔','کلسیم د هډوکو او غاښونو اصلي برخه ده.'),
 ('Living organism cannot synthesized the essential minerals.','جاندار ضروری معدنیات خود تیار نہیں کر سکتے۔','ژوندي موجودات اړین منرالونه پخپله نه شي جوړولی.')],'list')
add('Exercise','مشق','تمرین','heading')
add('Q I. Choose the correct one from the given options.','سوال I. دیے گئے اختیارات میں سے درست کا انتخاب کریں۔','پوښتنه I. له ورکړل شویو انتخابونو څخه سم یې وټاکئ.','heading')
M=[('1. The optimum pH of pepsin is around','1. پیپسن کا موزوں ترین pH تقریباً ہے','1. د پېپسین غوره pH نږدې دی','a. 3.0   b. 3.5   c. 2.0   d. 2.5','a. 3.0   b. 3.5   c. 2.0   d. 2.5','a. 3.0   b. 3.5   c. 2.0   d. 2.5'),
 ('2. The most abundant carbohydrate found in nature is','2. فطرت میں سب سے زیادہ پایا جانے والا کاربوہائیڈریٹ ہے','2. په طبیعت کې تر ټولو ډېر موندل کېدونکی کاربوهایدرېټ دی','a. cellulose   b. glycogen   c. pectin   d. chitin','a. سیلولوز   b. گلائیکوجن   c. پیکٹن   d. کائٹن','a. سلولوز   b. ګلایکوجن   c. پکټین   d. کایټین'),
 ('3. The glycosidic linkage is present between the molecules of','3. گلائیکوسائیڈک ربط کس کے سالمات کے درمیان ہوتا ہے','3. ګلایکوسایډیک اړیکه د کومو مالیکولونو ترمنځ شته','a. glucose   b. glycine   c. fatty acid   d. none of these','a. گلوکوز   b. گلائسین   c. فیٹی ایسڈ   d. ان میں سے کوئی نہیں','a. ګلوکوز   b. ګلایسین   c. غوړ اسید   d. له دې هېڅ یو'),
 ('4. Steroid belong to family of','4. سٹیرائیڈ کس خاندان سے تعلق رکھتا ہے','4. سټېرایډ د کومې کورنۍ دی','a. carbohydrates   b. proteins   c. lipids   d. enzymes','a. کاربوہائیڈریٹس   b. پروٹینز   c. لپڈز   d. خامرے','a. کاربوهایدرېټونه   b. پروټینونه   c. لیپیډونه   d. انزایمونه'),
 ('5. Protein present in haemoglobin has the structure known as','5. ہیموگلوبن میں موجود پروٹین کی ساخت کہلاتی ہے','5. په هیموګلوبین کې شته پروټین جوړښت لري چې بلل کېږي','a. primary structure.   b. secondary structure.   c. tertiary structure.   d. quaternary structure.','a. ابتدائی ساخت۔   b. ثانوی ساخت۔   c. ثالثی ساخت۔   d. چہارمی ساخت۔','a. لومړنی جوړښت.   b. دویم جوړښت.   c. درېیم جوړښت.   d. څلورم جوړښت.'),
 ('6. Which carbohydrate does not conform the general formula Cₙ(H₂O)ₙ?','6. کون سا کاربوہائیڈریٹ عمومی فارمولے Cₙ(H₂O)ₙ کے مطابق نہیں؟','6. کوم کاربوهایدرېټ له عمومي فورمول Cₙ(H₂O)ₙ سره سم نه دی؟','a. Deoxyribose   b. Ribose   c. Glucose   d. Fructose','a. ڈی آکسی رائبوز   b. رائبوز   c. گلوکوز   d. فرکٹوز','a. ډی اکسي رایبوز   b. رایبوز   c. ګلوکوز   d. فرکټوز'),
 ('7. Ethanol is produced from starch by the process of','7. نشاستے سے ایتھانول کس عمل سے بنتا ہے','7. له نشایستې ایتانول د کومې عملیې په واسطه تولیدېږي','a. hydrolysis   b. hydrogenation   c. decomposition   d. fermentation','a. ہائیڈرولائسز   b. ہائیڈروجنیشن   c. تحلیل   d. تخمیر','a. هایدرولایسس   b. هایدروجنېشن   c. تجزیه   d. تخمیر'),
 ('8. Human are unable to digest','8. انسان ہضم نہیں کر سکتے','8. انسانان یې نه شي هضمولی','a. glucose   b. cellulose   c. starch   d. denatured protein','a. گلوکوز   b. سیلولوز   c. نشاستہ   d. ڈی نیچرڈ پروٹین','a. ګلوکوز   b. سلولوز   c. نشایسته   d. ډینېچر شوی پروټین'),
 ('9. Which one of the following term is not related to term aldohexose?','9. درج ذیل میں سے کون سی اصطلاح الڈوہیکسوز سے متعلق نہیں؟','9. له لاندې اصطلاحاتو څخه کومه یوه له الدوهېکسوز سره تړاو نه لري؟','a. Aldehyde   b. Ketone   c. Six   d. Sugar','a. الڈیہائیڈ   b. کیٹون   c. چھ   d. شکر','a. الدیهاید   b. کیټون   c. شپږ   d. بوره'),
 ('10. Slow healing of wounds is due the deficiency of','10. زخموں کا آہستہ بھرنا کس کی کمی کی وجہ سے ہے','10. د ټپونو ورو جوړېدل د کوم یو د کمښت له امله دي','a. Ca   b. P   c. Zn   d. Fe','a. Ca   b. P   c. Zn   d. Fe','a. Ca   b. P   c. Zn   d. Fe'),
 ('11. RNA is primarily seen in','11. RNA بنیادی طور پر کہاں دیکھا جاتا ہے','11. RNA په اصل کې چېرته لیدل کېږي','a. nucleus   b. cytoplasm   c. cell wall   d. cell membrane','a. مرکزہ   b. سائٹوپلازم   c. خلوی دیوار   d. خلوی جھلی','a. هسته   b. سایټوپلازم   c. حجروي دېوال   d. حجروي غشا'),
 ('12. In which of following disaccharides both the basic structural units are the same?','12. درج ذیل میں سے کس ڈائی سیکرائیڈ میں دونوں بنیادی ساختی اکائیاں یکساں ہیں؟','12. په لاندې کوم ډای ساکاریډ کې دواړه بنسټیز جوړښتي واحدونه ورته دي؟','a. Maltose   b. Lactose   c. Sucrose   d. All of these','a. مالٹوز   b. لیکٹوز   c. سکروز   d. یہ سب','a. مالټوز   b. لاکټوز   c. سوکروز   d. دا ټول'),
 ('13. In competitive inhibition, the inhibitor','13. مسابقتی روک تھام میں روکنے والا','13. په سیالي لرونکي مخنیوي کې، مخنیوونکی','a. competes with enzyme.   b. irreversibly binds with the enzyme.   c. binds with substrate.   d. competes with substrate.','a. خامرے سے مقابلہ کرتا ہے۔   b. خامرے سے ناقابلِ واپسی طور پر جڑتا ہے۔   c. سبسٹریٹ سے جڑتا ہے۔   d. سبسٹریٹ سے مقابلہ کرتا ہے۔','a. له انزایم سره سیالي کوي.   b. له انزایم سره نه بېرته ګرځېدونکی نښلي.   c. له سبسټرېټ سره نښلي.   d. له سبسټرېټ سره سیالي کوي.'),
 ('14. In DNA, adenine forms a complementary pair with which other nitrogen base?','14. DNA میں ایڈینین کس دوسری نائٹروجنی اساس کے ساتھ تکمیلی جوڑا بناتا ہے؟','14. په DNA کې اډینین له کومې بلې نایټروجني قلوي سره بشپړوونکې جوړه جوړوي؟','a. Uracil   b. Cytosine   c. Thymine   d. Guanine','a. یوراسل   b. سائٹوسین   c. تھائمین   d. گوانین','a. یوراسیل   b. سایټوسین   c. تایمین   d. ګوانین'),
 ('15. Proteins are polymers of','15. پروٹینز کس کے پولیمر ہیں','15. پروټینونه د څه پولیمرونه دي','a. glucose   b. disulphide bridges   c. amino acids   d. peptide bonds','a. گلوکوز   b. ڈائی سلفائیڈ پل   c. امائنو ایسڈز   d. پیپٹائیڈ بند','a. ګلوکوز   b. ډای سلفایډ پلونه   c. امینو اسیدونه   d. پېپټایډ تړونونه')]
for q in M:lines([q[:3],q[3:]])
r19=section('21.19','Unit 21 Key Points (end) and exercise MCQs 1–15','یونٹ 21 اہم نکات (اختتام) اور کثیر انتخابی 1–15','د 21 واحد مهم ټکي (پای) او څو انتخابي 1–15',P,L,[],'306–307')
r19['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':156,'printedPages':[306,307]}]
P,L,add,lines=builder()
add('Q2. Write short answers of the following questions.','سوال 2. درج ذیل سوالات کے مختصر جوابات لکھیں۔','پوښتنه 2. د لاندې پوښتنو لنډ ځوابونه ولیکئ.','heading')
lines([('i. Why vegetable oil is sensitive to rancidity?','i. نباتاتی تیل ترشیدگی کے لیے حساس کیوں ہے؟','i. نباتي تېل ولې ترخېدو ته حساس دي؟'),
 ('ii. Why melting point of saturated fatty acid is higher than unsaturated fatty acid?','ii. سیر شدہ فیٹی ایسڈ کا نقطۂ پگھلاؤ غیر سیر شدہ فیٹی ایسڈ سے زیادہ کیوں ہے؟','ii. د مشبوع غوړ اسید د ویلې کېدو ټکی له نامشبوع غوړ اسید ولې لوړ دی؟'),
 ('iii. Make at least one point difference in each compound in the given pairs. Differentiate between the following compounds. a. Glucose and fructose   b. Sucrose and maltose   c. Cellulose and starch','iii. دیے گئے جوڑوں میں ہر مرکب میں کم از کم ایک نکتے کا فرق بیان کریں۔ درج ذیل مرکبات میں فرق کریں۔ a. گلوکوز اور فرکٹوز   b. سکروز اور مالٹوز   c. سیلولوز اور نشاستہ','iii. په ورکړل شویو جوړو کې د هر مرکب لږترلږه یو ټکی توپیر ولیکئ. د لاندې مرکباتو ترمنځ توپیر وکړئ. a. ګلوکوز او فرکټوز   b. سوکروز او مالټوز   c. سلولوز او نشایسته'),
 ('iv. Write down at least three important functions of nucleic acids.','iv. نیوکلک ایسڈز کے کم از کم تین اہم افعال لکھیں۔','iv. د نیوکلیک اسیدونو لږترلږه درې مهمې دندې ولیکئ.'),
 ('v. Write down the products of hydrolysis of sucrose with reaction.','v. سکروز کی ہائیڈرولائسز کی پیداوار تعامل کے ساتھ لکھیں۔','v. د سوکروز د هایدرولایسس محصولات له تعامل سره ولیکئ.'),
 ('vi. What happens when protein is denatured?','vi. جب پروٹین ڈی نیچر ہوتا ہے تو کیا ہوتا ہے؟','vi. کله چې پروټین ډینېچر شي څه کېږي؟'),
 ('vii. What are chemical components that compose the nucleic acid?','vii. وہ کیمیائی اجزا کون سے ہیں جن سے نیوکلک ایسڈ بنتا ہے؟','vii. هغه کیمیاوي برخې کومې دي چې نیوکلیک اسید جوړوي؟'),
 ('viii. Describe briefly the primary, secondary, tertiary and quaternary structure of protein.','viii. پروٹین کی ابتدائی، ثانوی، ثالثی اور چہارمی ساخت مختصراً بیان کریں۔','viii. د پروټین لومړنی، دویم، درېیم او څلورم جوړښت په لنډه توګه بیان کړئ.'),
 ('ix. Differentiate between non-competitive and uncompetitive inhibitions.','ix. غیر مسابقتی اور نامسابقتی روک تھام میں فرق کریں۔','ix. د بې سیالۍ او نا سیالي مخنیویو ترمنځ توپیر وکړئ.'),
 ('x. Write down the physical and chemical properties of lipids.','x. لپڈز کی طبعی اور کیمیائی خصوصیات لکھیں۔','x. د لیپیډونو فزیکي او کیمیاوي ځانګړنې ولیکئ.')])
add('Q3. Write detail answers of the following questions.','سوال 3. درج ذیل سوالات کے تفصیلی جوابات لکھیں۔','پوښتنه 3. د لاندې پوښتنو مفصل ځوابونه ولیکئ.','heading')
lines([('1. (a). What are carbohydrates? Explain the basis of classification of carbohydrate.','1. (a). کاربوہائیڈریٹس کیا ہیں؟ کاربوہائیڈریٹ کی درجہ بندی کی بنیاد کی وضاحت کریں۔','1. (a). کاربوهایدرېټونه څه دي؟ د کاربوهایدرېټ د ډلبندۍ اساس تشریح کړئ.'),
 ('(b). How would you evaluate the role of various carbohydrates in health and diseases?','(b). آپ صحت اور بیماریوں میں مختلف کاربوہائیڈریٹس کے کردار کا جائزہ کیسے لیں گے؟','(b). تاسو په روغتیا او ناروغیو کې د بېلابېلو کاربوهایدرېټونو رول څنګه ارزوئ؟'),
 ('2. (a). Describe various classes of protein along with examples.','2. (a). پروٹین کی مختلف جماعتیں مثالوں کے ساتھ بیان کریں۔','2. (a). د پروټین بېلابېلې ډلې له بېلګو سره بیان کړئ.'),
 ('(b). Enlist the properties of protein.','(b). پروٹین کی خصوصیات کی فہرست بنائیں۔','(b). د پروټین ځانګړنې لیست کړئ.')])
r20=section('21.20','Unit 21 exercise: short and detailed questions (printed 307)','یونٹ 21 مشق: مختصر اور تفصیلی سوالات (صفحہ 307)','د 21 واحد تمرین: لنډې او مفصلې پوښتنې (مخ 307)',P,L,[],'307')
r20['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':156,'printedPages':[307]}];r20['insertBefore']='21.exercise.solved';r20['sourceContinuesOnPdfPage']=157
tail=(ROOT/'docs/source-verification/class-12/legacy/chem21-tail-from-printed303.txt').read_text(encoding='utf-8')
rest=tail[tail.index('3. (a). What are lipids?'):]
holder={'id':'21.21','title':'Textbook lesson extract (printed 308, pending source authoring)','theory':rest,'content':rest.replace('\n','<br>'),'sciNote':'','insertBefore':'21.exercise.solved','sourcePendingAuthoring':True}
if __name__=='__main__':save(156,[r19,r20,holder],chapter_number=21)
