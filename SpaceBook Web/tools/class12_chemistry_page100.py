"""PDF100 printed192–193: Unit 17 exercise continuation (Q3 2–5) and Project (Hinsberg's test)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,chain
F=Fig('arrow100');t=F.t;line=F.line
def builder():
 P=[];L=[];B=[]
 def add(e,u,p,kind='paragraph'):L.append({'type':kind,'indices':[len(P)]});P.append(pair(e,u,p))
 def lines(rows):
  s0=len(P)
  for r in rows:P.append(pair(*r))
  L.append({'type':'lines','indices':list(range(s0,len(P)))})
 def visual(identity,fn):B.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});L.append({'type':'visual','blockId':identity})
 return P,L,B,add,lines,visual
def structures(lang):
 s=F.start(400)
 s+=t(30,40,'i.',15)+chain(F,0,80,['H₃C','—','CH₂','—','CH','—','C','—','CH₂','—','CH₃'],15,None,{4:'I',6:'CH₃'},{6:'C₂H₅'},center=220)
 s+=t(450,40,'ii.',15)+chain(F,0,80,['H₃C','—','CH','—','CH','—','C','—','CH₂','—','CH₃'],15,None,{2:'Cl',4:'CH₃',6:'Br'},{6:'C₂H₅'},center=650)
 s+=t(30,190,'iii.',15)+chain(F,0,230,['H₃C','—','CH','—','CH','—','C','—','CH₂','—','CH=CH₂'],15,None,{2:'Br',4:'CH₃',6:'Br'},{6:'F'},center=230)
 s+=t(450,190,'iv.',15)+chain(F,0,230,['H₃C','—','CH','—','CH','—','C','—','CH₂','—','CH₃'],15,None,{2:'C₂H₅',4:'CH₃',6:'Br'},{6:'CH₃'},center=650)
 s+=t(30,320,'v.',15)+chain(F,0,350,['H₃C','—','CH₂','—','CH','—','CH','—','CH₂','—','CH₃'],15,None,{4:'NH₂'},{6:'CH₃'},center=220)
 return s+'</svg>'
P,L,B,add,lines,visual=builder()
lines([
 ('2. (a) Discuss the mechanism of SN1 and SN2 reactions.','2. (a) SN1 اور SN2 تعاملات کے طریق کار پر بحث کریں۔','2. (a) د SN1 او SN2 تعاملونو پر میکانیزم بحث وکړئ.'),
 ('(b) Define the following terms. (i) substrate (ii) leaving group (iii) carbocation','(b) درج ذیل اصطلاحات کی تعریف کریں۔ (i) سبسٹریٹ (ii) خارج ہونے والا گروپ (iii) کاربوکیٹائن','(b) لاندې اصطلاحګانې تعریف کړئ. (i) سبسټرېټ (ii) وتونکی ګروپ (iii) کاربوکاټیون'),
 ('3. (a) How can you prepare Grignard reagent?','3. (a) آپ گرینیارڈ عامل کیسے تیار کر سکتے ہیں؟','3. (a) ګرینیارډ عامل څنګه جوړولی شئ؟'),
 ('(b) Discuss the reaction of Grignard reagent with. (i) aldehydes (ii) ketones (iii) esters (iv) carbon dioxide','(b) گرینیارڈ عامل کے تعامل پر بحث کریں ان کے ساتھ: (i) الڈیہائیڈز (ii) کیٹونز (iii) ایسٹرز (iv) کاربن ڈائی آکسائیڈ','(b) د ګرینیارډ عامل پر تعامل بحث وکړئ له: (i) الدیهایډونو (ii) کیټونونو (iii) ایسټرونو (iv) کاربن ډای اکساید'),
 ('4. (a) How amines are prepared? Discuss its structure and basicity.','4. (a) امائنز کیسے تیار کیے جاتے ہیں؟ ان کی ساخت اور اساسیت پر بحث کریں۔','4. (a) امینونه څنګه چمتو کېږي؟ پر جوړښت او قلویت یې بحث وکړئ.'),
 ('(b) Write down different reactions of amines.','(b) امائنز کے مختلف تعاملات لکھیں۔','(b) د امینونو بېلابېل تعاملونه ولیکئ.'),
 ('5. (a) What are carbocations? Write any two methods for formation of carbocations?','5. (a) کاربوکیٹائنز کیا ہیں؟ کاربوکیٹائنز بننے کے کوئی دو طریقے لکھیں؟','5. (a) کاربوکاټیونونه څه دي؟ د کاربوکاټیونونو د جوړېدو هر دوه طریقې ولیکئ؟'),
 ('(b) Explain the stability order of different types of carbocations.','(b) مختلف اقسام کے کاربوکیٹائنز کی پائیداری کی ترتیب واضح کریں۔','(b) د بېلابېلو ډولونو کاربوکاټیونونو د ثبات ترتیب روښانه کړئ.'),
 ('(c) Write the systematic names for the following organic compounds;','(c) درج ذیل نامیاتی مرکبات کے نظامی نام لکھیں؛','(c) د لاندې عضوي مرکباتو سیستماتیک نومونه ولیکئ؛')])
visual('chem12-p100-naming-structures',structures)
lines([('(d) Draw the structural formula of the following organic compounds;','(d) درج ذیل نامیاتی مرکبات کے ساختی فارمولے بنائیں؛','(d) د لاندې عضوي مرکباتو جوړښتي فورمولونه رسم کړئ؛'),
 ('i. 3-methylpentane-2,3-diamine','i. 3-میتھائل پینٹین-2،3-ڈائی امائن','i. 3-میتایل پېنټان-2،3-ډای امین'),
 ('ii. 2,3-dimethylhexane-2,3-diamine','ii. 2،3-ڈائی میتھائل ہیکسین-2،3-ڈائی امائن','ii. 2،3-ډای میتایل هېکسان-2،3-ډای امین')])
rec16=section('17.16','Unit 17 exercise: detailed questions','یونٹ 17 مشق: تفصیلی سوالات','د 17 واحد تمرین: تفصیلي پوښتنې',P,L,B,'192')
rec16['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':100,'printedPages':[192]}]
P,L,B,add,lines,visual=builder()
lines([('iii. 2-bromo-3-fluoro-2,3-dimethylpentane','iii. 2-برومو-3-فلورو-2،3-ڈائی میتھائل پینٹین','iii. 2-برومو-3-فلورو-2،3-ډای میتایل پېنټان'),
 ('iv. 4-bromo-4-chloro-3-fluoro-2,3-dimethylhexane','iv. 4-برومو-4-کلورو-3-فلورو-2،3-ڈائی میتھائل ہیکسین','iv. 4-برومو-4-کلورو-3-فلورو-2،3-ډای میتایل هېکسان'),
 ('v. 2-chloro-3,3-dimethylpentan-2-amine','v. 2-کلورو-3،3-ڈائی میتھائل پینٹین-2-امائن','v. 2-کلورو-3،3-ډای میتایل پېنټان-2-امین')])
add('Project','منصوبہ','پروژه','heading')
add('Hinsberg’s test is used to distinguish primary, secondary and tertiary amines. The Hinsberg’s reagent is a solution of aqueous sodium hydroxide and benzene sulfonyl chloride. In the Hinsberg’s test, an amine is reacted with benzene sulfonyl chloride. If a product forms, the amine is either a primary or secondary amine because tertiary amines can not form sulfonamides. If the sulfonamide that forms dissolves in aqueous sodium hydroxide solution, it is a primary amine. If the sulfonamide is insoluble in aqueous sodium hydroxide, it is a secondary amine. The sulfonamide of a primary amine is soluble in an aqueous base because it still possesses an acidic hydrogen on the nitrogen, which can be lost to form a sodium salt.',
 'ہنزبرگ ٹیسٹ ابتدائی، ثانوی اور ثالثی امائنز میں امتیاز کے لیے استعمال ہوتا ہے۔ ہنزبرگ عامل آبی سوڈیم ہائیڈروآکسائیڈ اور بینزین سلفونائل کلورائیڈ کا محلول ہے۔ ہنزبرگ ٹیسٹ میں امائن کو بینزین سلفونائل کلورائیڈ سے عمل کرایا جاتا ہے۔ اگر پیداوار بنے تو امائن یا ابتدائی ہے یا ثانوی، کیونکہ ثالثی امائنز سلفونامائیڈز نہیں بنا سکتے۔ اگر بننے والا سلفونامائیڈ آبی سوڈیم ہائیڈروآکسائیڈ محلول میں حل ہو جائے تو یہ ابتدائی امائن ہے۔ اگر سلفونامائیڈ آبی سوڈیم ہائیڈروآکسائیڈ میں حل نہ ہو تو یہ ثانوی امائن ہے۔ ابتدائی امائن کا سلفونامائیڈ آبی اساس میں حل ہوتا ہے کیونکہ اس کے نائٹروجن پر اب بھی ایک تیزابی ہائیڈروجن ہوتا ہے، جو نکل کر سوڈیم نمک بنا سکتا ہے۔',
 'د هنزبرګ ازموینه د لومړنیو، دویمیو او درېیمیو امینونو د توپیر لپاره کارېږي. د هنزبرګ عامل د اوبلن سوډیم هایدروکساید او بنزین سلفونیل کلوراید محلول دی. د هنزبرګ په ازموینه کې امین له بنزین سلفونیل کلوراید سره تعامل کوي. که محصول جوړ شي، امین یا لومړنی یا دویمی دی ځکه درېیمي امینونه سلفونامایډونه نه شي جوړولی. که جوړ شوی سلفونامایډ په اوبلن سوډیم هایدروکساید محلول کې حل شي، لومړنی امین دی. که سلفونامایډ په اوبلن سوډیم هایدروکساید کې حل نه شي، دویمی امین دی. د لومړني امین سلفونامایډ په اوبلن قلوي کې حلېږي ځکه لا هم پر نایتروجن یو اسیدي هایدروجن لري، چې له لاسه ورکول کېدای شي او سوډیم مالګه جوړوي.')
add('Procedure','طریقۂ کار','کړنلاره','heading')
add('Add 4-5 mL of an amine to a large test tube. Add 5 mL of benzene sulfonyl chloride and 10 mL of 10% NaOH and shake vigorously to mix. Check for the presence of a single layer (primary amine) or a double layer (secondary amine) in the solution. If there is a double layer, draw off the lower aqueous layer with a separating funnel and check if the organic layer is soluble in 5% HCl. If yes, it is tertiary but if it is insoluble, then secondary amine is present.',
 'ایک بڑی ٹیسٹ ٹیوب میں 4-5 mL امائن ڈالیں۔ 5 mL بینزین سلفونائل کلورائیڈ اور 10% NaOH کے 10 mL ڈال کر ملانے کے لیے زور سے ہلائیں۔ محلول میں ایک تہہ (ابتدائی امائن) یا دو تہوں (ثانوی امائن) کی موجودگی دیکھیں۔ اگر دو تہیں ہوں تو علیحدگی قیف سے نچلی آبی تہہ نکال لیں اور دیکھیں کہ نامیاتی تہہ 5% HCl میں حل ہوتی ہے یا نہیں۔ اگر ہاں تو یہ ثالثی ہے، لیکن اگر حل نہ ہو تو ثانوی امائن موجود ہے۔',
 'په یوه لوی ټیسټ ټیوب کې 4-5 mL امین واچوئ. 5 mL بنزین سلفونیل کلوراید او د 10% NaOH 10 mL ورزیات کړئ او د ګډولو لپاره په زوره وښوروئ. په محلول کې د یوې طبقې (لومړنی امین) یا دوو طبقو (دویمی امین) شتون وګورئ. که دوه طبقې وي، لاندینۍ اوبلنه طبقه د جلا کوونکي قیف په واسطه وباسئ او وګورئ چې عضوي طبقه په 5% HCl کې حلېږي که نه. که هو، درېیمی دی، خو که نه حلېږي، دویمی امین شته.')
rec17=section('17.17','Unit 17 exercise end and Project (Hinsberg’s test)','یونٹ 17 مشق کا اختتام اور منصوبہ (ہنزبرگ ٹیسٹ)','د 17 واحد تمرین پای او پروژه (د هنزبرګ ازموینه)',P,L,B,'193')
rec17['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':100,'printedPages':[193]}]
issues=[{'id':'chem12-p193-hinsberg-procedure','printedPage':193,'description':'Printed procedure says single layer = primary, double layer = secondary, then tests organic layer in HCl to separate tertiary; retained verbatim.'}]
if __name__=='__main__':save(100,[rec16,rec17],issues=issues,chapter_number=17)
