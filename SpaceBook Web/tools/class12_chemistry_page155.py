"""PDF155 printed304–305: phosphorus (cont.), zinc; Unit 21 Key Points (first part)."""
from class12_chemistry_opening import pair,section,SOURCE,ROOT
from class12_chemistry_sync import save
def builder():
 P=[];L=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def lines(rows,kind='list'):
  s0=len(P)
  for r in rows:P.append(pair(*r))
  L.append({'type':kind,'indices':list(range(s0,len(P)))})
 return P,L,add,lines
P,L,add,lines=builder()
lines([('Foods that are rich in protein are also excellent sources of phosphorus. These include meat and poultry, fish, eggs, milk and other dairy products.','پروٹین سے بھرپور خوراکیں فاسفورس کے بھی بہترین ذرائع ہیں۔ ان میں گوشت اور مرغی، مچھلی، انڈے، دودھ اور دوسری ڈیری مصنوعات شامل ہیں۔','پروټین لرونکي خواړه د فاسفورس هم غوره سرچینې دي. په دې کې غوښه او چرګ، کب، هګۍ، شیدې او نور لبنیات شامل دي.'),
 ('Some non-protein food sources also contain phosphorus. For example, whole grains, potatoes, garlic, dry fruits and carbonated drinks.','بعض غیر پروٹینی خوراکی ذرائع میں بھی فاسفورس ہوتا ہے۔ مثلاً سالم اناج، آلو، لہسن، خشک میوہ جات اور کاربونیٹڈ مشروبات۔','ځینې غیر پروټیني خوراکي سرچینې هم فاسفورس لري. د بېلګې په توګه بشپړې غلې، کچالو، هوږه، وچه مېوه او کاربونېټډ څښاکونه.')])
add('Deficiency of Phosphorous','فاسفورس کی کمی','د فاسفورس کمښت','heading')
lines([('Deficiency of phosphorous in the body leads to various problems such as, joint or bone pain, loss of appetite, irritability or anxiety, fatigue and poor bone development in children.','جسم میں فاسفورس کی کمی مختلف مسائل کا باعث بنتی ہے جیسے جوڑوں یا ہڈیوں کا درد، بھوک کا ختم ہونا، چڑچڑاپن یا بے چینی، تھکاوٹ اور بچوں میں ہڈیوں کی کمزور نشوونما۔','په بدن کې د فاسفورس کمښت بېلابېلو ستونزو ته لار هواروي لکه د بندونو یا هډوکو درد، د اشتها له منځه تلل، تریخوالی یا اندېښنه، ستړیا او په ماشومانو کې د هډوکو کمزورې ودې.'),
 ('Deficiency of phosphorous in children leads to renal rickets.','بچوں میں فاسفورس کی کمی گردوی رکٹس کا باعث بنتی ہے۔','په ماشومانو کې د فاسفورس کمښت د پښتورګو رکټس ته لار هواروي.')])
add('Excess of Phosphorous','فاسفورس کی زیادتی','د فاسفورس زیاتوالی','heading')
add('Too much phosphate can be toxic.','بہت زیادہ فاسفیٹ زہریلا ہو سکتا ہے۔','ډېر فاسفېټ زهرجن کېدای شي.')
lines([('An excess can cause diarrhoea, as well as a hardening of organs and soft tissues.','اس کی زیادتی سے اسہال کے ساتھ ساتھ اعضا اور نرم بافتوں کی سختی ہو سکتی ہے۔','د هغه زیاتوالی د اسهال او همدارنګه د غړو او نرمو نسجونو د کلکېدو لامل کېدای شي.'),
 ('An increase in the plasma phosphate level due to decrease in its excretion leads to kidney dysfunction.','اخراج میں کمی کی وجہ سے پلازما میں فاسفیٹ کی سطح میں اضافہ گردے کی خرابی کا باعث بنتا ہے۔','د اطراح د کمښت له امله په پلازما کې د فاسفېټ د کچې زیاتوالی د پښتورګو بې دندې کېدو ته لار هواروي.')])
add('iv. Zinc','iv. زنک','iv. جست','heading')
add('Zinc is antioxidant and important for the maintenance of a healthy immune system. Zinc is an important element for the normal growth, reproduction and longevity of animals.','زنک اینٹی آکسیڈنٹ ہے اور صحت مند مدافعتی نظام برقرار رکھنے کے لیے اہم ہے۔ زنک جانوروں کی معمول کی نشوونما، تولید اور لمبی عمر کے لیے اہم عنصر ہے۔','جست انټي اکسیډانټ دی او د روغ معافیتي سیستم د ساتلو لپاره مهم دی. جست د ژویو د عادي ودې، تکثر او اوږد عمر لپاره مهم عنصر دی.')
add('Daily requirement','روزانہ ضرورت','ورځنۍ اړتیا','heading')
lines([('The recommended daily amount of zinc for an adult is 10 mg.','بالغ کے لیے زنک کی تجویز کردہ روزانہ مقدار 10 mg ہے۔','د لوی سړي لپاره د جستو سپارښتل شوې ورځنۍ اندازه 10 mg ده.'),
 ('It is a constituent of several types of enzymes such as alkaline phosphatase, carbonic anhydrase etc.','یہ کئی اقسام کے خامروں جیسے الکلائن فاسفیٹیز، کاربونک این ہائیڈریز وغیرہ کا جزو ہے۔','دا د ډېرو ډولونو انزایمونو لکه الکلاین فاسفاټېز، کاربونیک انهایدرېز او نورو برخه ده.'),
 ('It also forms a complex with insulin and helps in its storage and release according to the needs of the body. It is also required for maintaining the plasma concentration of vitamin A.','یہ انسولین کے ساتھ کمپلیکس بھی بناتا ہے اور جسم کی ضرورت کے مطابق اس کے ذخیرے اور اخراج میں مدد دیتا ہے۔ یہ وٹامن A کے پلازما ارتکاز کو برقرار رکھنے کے لیے بھی درکار ہے۔','دا له انسولین سره کمپلېکس هم جوړوي او د بدن د اړتیا سره سم یې په زېرمه کولو او خوشې کولو کې مرسته کوي. د ویټامین A د پلازما غلظت د ساتلو لپاره هم اړین دی.')])
add('Sources of Zinc','زنک کے ذرائع','د جستو سرچینې','heading')
add('The different sources of zinc include meat, liver, eggs, fish, milk and cereals.','زنک کے مختلف ذرائع میں گوشت، کلیجی، انڈے، مچھلی، دودھ اور اناج شامل ہیں۔','د جستو بېلابېلې سرچینې غوښه، ځیګر، هګۍ، کب، شیدې او غلې دي.')
add('Deficiency of Zinc','زنک کی کمی','د جستو کمښت','heading')
add('Deficiency of zinc results in slow healing of wounds, impairment of acuity of taste and skin problems.','زنک کی کمی سے زخموں کا آہستہ بھرنا، ذائقے کی حس کی کمزوری اور جلد کے مسائل پیدا ہوتے ہیں۔','د جستو کمښت د ټپونو د ورو جوړېدو، د خوند د حس د کمزورتیا او د پوستکي ستونزو لامل کېږي.')
add('Excess of Zinc','زنک کی زیادتی','د جستو زیاتوالی','heading')
add('Excess intake of zinc can cause gastrointestinal discomfort and when chronic, may disrupt the balance of other chemicals in the body, including copper and iron.','زنک کا زیادہ استعمال معدے اور آنتوں کی تکلیف کا باعث بن سکتا ہے اور دائمی ہونے کی صورت میں جسم میں تانبے اور لوہے سمیت دوسرے کیمیائی مادوں کا توازن بگاڑ سکتا ہے۔','د جستو زیات مصرف د معدې او کولمو ناآرامۍ لامل کېدای شي او کله چې اوږدمهاله وي، په بدن کې د مسو او اوسپنې په ګډون د نورو کیمیاوي موادو توازن ګډوډولی شي.')
r17=section('21.17','Phosphorus (cont.) and zinc','فاسفورس (جاری) اور زنک','فاسفورس (دوام) او جست',P,L,[],'304')
r17['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':155,'printedPages':[304]}]
P,L,add,lines=builder()
add('Key Points','اہم نکات','مهم ټکي','heading')
lines([('Biochemistry studies the chemistry of life.','حیاتی کیمیا زندگی کی کیمیا کا مطالعہ کرتی ہے۔','ژوندکیمیا د ژوند کیمیا مطالعه کوي.'),
 ('Carbohydrates, proteins, lipids, nucleic acid are called biomolecules.','کاربوہائیڈریٹس، پروٹینز، لپڈز اور نیوکلک ایسڈ حیاتی سالمات کہلاتے ہیں۔','کاربوهایدرېټونه، پروټینونه، لیپیډونه او نیوکلیک اسید ژوندي مالیکولونه بلل کېږي.'),
 ('Carbohydrates are polyhydroxy aldehydes (aldoses) and polyhydroxy ketones (ketoses) or compounds formed by linking aldoses and ketoses.','کاربوہائیڈریٹس پولی ہائیڈروآکسی الڈیہائیڈز (الڈوزز) اور پولی ہائیڈروآکسی کیٹونز (کیٹوزز) یا الڈوزز اور کیٹوزز کے جڑنے سے بننے والے مرکبات ہیں۔','کاربوهایدرېټونه پولي هایدروکسي الدیهایډونه (الدوزونه) او پولي هایدروکسي کیټونونه (کیټوزونه) یا د الدوزونو او کیټوزونو د نښلېدو په واسطه جوړ شوي مرکبات دي.'),
 ('Glucose is known as “aldose” and has an aldehyde structure at carbon atom number one.','گلوکوز کو ”الڈوز“ کہتے ہیں اور اس کے کاربن ایٹم نمبر ایک پر الڈیہائیڈ ساخت ہے۔','ګلوکوز ته ”الدوز“ وايي او د یو نمبر کاربني اټوم پر الدیهاید جوړښت لري.'),
 ('Fructose is known as “ketose” and has a keto structure at carbon atom number two.','فرکٹوز کو ”کیٹوز“ کہتے ہیں اور اس کے کاربن ایٹم نمبر دو پر کیٹو ساخت ہے۔','فرکټوز ته ”کیټوز“ وايي او د دوه نمبر کاربني اټوم پر کیټو جوړښت لري.'),
 ('The main classes of carbohydrates are monosaccharide, oligosaccharide and polysaccharide.','کاربوہائیڈریٹس کی بڑی جماعتیں مونوسیکرائیڈ، اولیگوسیکرائیڈ اور پولی سیکرائیڈ ہیں۔','د کاربوهایدرېټونو اصلي ډلې مونوساکاریډ، اولیګوساکاریډ او پولي ساکاریډ دي.'),
 ('Monosaccharides and oligosaccharides are collectively called sugars. Polysaccharides are non-sugars.','مونوسیکرائیڈز اور اولیگوسیکرائیڈز کو مجموعی طور پر شکر کہتے ہیں۔ پولی سیکرائیڈز غیر شکر ہیں۔','مونوساکاریډونه او اولیګوساکاریډونه په ټولیز ډول بورې بلل کېږي. پولي ساکاریډونه غیر بورې دي.'),
 ('When two monosaccharide units combine together by an oxygen atom with elimination of one water molecule, this type of linkage is called glycosidic linkage or glycosidic bond.','جب دو مونوسیکرائیڈ اکائیاں پانی کے ایک سالمے کے اخراج کے ساتھ ایک آکسیجن ایٹم کے ذریعے آپس میں جڑتی ہیں تو اس قسم کے ربط کو گلائیکوسائیڈک ربط یا گلائیکوسائیڈک بند کہتے ہیں۔','کله چې دوه مونوساکاریډ واحدونه د اوبو د یوه مالیکول په ایستلو سره د یوه اکسیجني اټوم په واسطه یو ځای شي، دې ډول اړیکې ته ګلایکوسایډیک اړیکه یا ګلایکوسایډیک تړون وايي.'),
 ('Amino acids are monomers of proteins and they are connected by peptide bond in proteins.','امائنو ایسڈز پروٹینز کے مونومر ہیں اور پروٹینز میں پیپٹائیڈ بند سے جڑے ہوتے ہیں۔','امینو اسیدونه د پروټینونو مونومرونه دي او په پروټینونو کې د پېپټایډ تړون په واسطه نښتي دي.'),
 ('The structure of protein is considered at four levels, primary, secondary, tertiary and quaternary.','پروٹین کی ساخت کو چار سطحوں پر دیکھا جاتا ہے: ابتدائی، ثانوی، ثالثی اور چہارمی۔','د پروټین جوړښت په څلورو کچو کې ګڼل کېږي: لومړنی، دویم، درېیم او څلورم.'),
 ('Lipids are heterogeneous class of organic compounds. They may be saponifiable or non-saponifiable.','لپڈز نامیاتی مرکبات کی متنوع جماعت ہیں۔ یہ قابلِ صابن سازی یا ناقابلِ صابن سازی ہو سکتے ہیں۔','لیپیډونه د عضوي مرکباتو ناهمجنسه ډله ده. کېدای شي د صابون جوړونې وړ یا نه وړ وي.'),
 ('The oils, which contain more unsaturation, are hydrogenated to produce solid ghee.','زیادہ غیر سیر شدگی والے تیلوں کو ہائیڈروجنیٹ کر کے ٹھوس گھی بنایا جاتا ہے۔','هغه تېل چې ډېر نامشبوعیت لري هایدروجنېټ کېږي او جامد غوړي جوړوي.'),
 ('DNA and RNA are two examples of nucleic acid and their function is replication and protein synthesis.','DNA اور RNA نیوکلک ایسڈ کی دو مثالیں ہیں اور ان کا فعل نقل اور پروٹین کی تالیف ہے۔','DNA او RNA د نیوکلیک اسید دوه بېلګې دي او دنده یې کاپي کېدل او د پروټین جوړول دي.'),
 ('The building blocks of nucleic acids are nucleotides.','نیوکلک ایسڈز کی بنیادی اکائیاں نیوکلیوٹائیڈز ہیں۔','د نیوکلیک اسیدونو جوړونکي واحدونه نیوکلیوټایډونه دي.'),
 ('The three components of a deoxyribonucleotide are a five-carbon sugar called deoxyribose, a phosphate group and a nitrogenous base.','ڈی آکسی رائبونیوکلیوٹائیڈ کے تین اجزا ڈی آکسی رائبوز نامی پانچ کاربن والی شکر، ایک فاسفیٹ گروپ اور ایک نائٹروجنی اساس ہیں۔','د ډی اکسي رایبونیوکلیوټایډ درې برخې د ډی اکسي رایبوز په نوم پنځه کاربنه بوره، یو فاسفېټ ګروپ او یوه نایټروجني قلوي دي.'),
 ('Enzymes are protein in nature, which can speed up a chemical reaction.','خامرے فطرتاً پروٹین ہیں جو کیمیائی تعامل کو تیز کر سکتے ہیں۔','انزایمونه په طبیعت کې پروټین دي چې کیمیاوي تعامل چټکولی شي.'),
 ('Enzyme inhibition may be irreversible or reversible.','خامروں کی روک تھام ناقابلِ واپسی یا قابلِ واپسی ہو سکتی ہے۔','د انزایم مخنیوی کېدای شي نه بېرته ګرځېدونکی یا بېرته ګرځېدونکی وي.'),
 ('Most animal enzyme’s optimum temperature is body temperature (37°C).','زیادہ تر حیوانی خامروں کا موزوں ترین درجہ حرارت جسم کا درجہ حرارت (37°C) ہے۔','د ډېری حیواني انزایمونو غوره تودوخه د بدن تودوخه (37°C) ده.'),
 ('A pH, at which an enzyme shows the maximum activity, is called optimum pH.','وہ pH جس پر خامرہ زیادہ سے زیادہ سرگرمی دکھاتا ہے، موزوں ترین pH کہلاتا ہے۔','هغه pH چې پکې انزایم اعظمي فعالیت ښيي، غوره pH بلل کېږي.')],'list')
r18=section('21.18','Unit 21 Key Points (printed 305)','یونٹ 21 اہم نکات (صفحہ 305)','د 21 واحد مهم ټکي (مخ 305)',P,L,[],'305')
r18['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':155,'printedPages':[305]}];r18['insertBefore']='21.exercise.solved';r18['sourceContinuesOnPdfPage']=156
tail=(ROOT/'docs/source-verification/class-12/legacy/chem21-tail-from-printed303.txt').read_text(encoding='utf-8')
rest=tail[tail.index('The substances, which decrease the activity'):]
holder={'id':'21.19','title':'Textbook lesson extract (printed 306–308, pending source authoring)','theory':rest,'content':rest.replace('\n','<br>'),'sciNote':'','insertBefore':'21.exercise.solved','sourcePendingAuthoring':True}
if __name__=='__main__':save(155,[r17,r18,holder],chapter_number=21)
