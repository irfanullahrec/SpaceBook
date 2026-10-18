"""PDF196: all remaining MCQs, conceptual/comprehensive questions and numericals1–3."""
from class12_source_review import upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import stage_reference
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];QUESTIONS=[];GROUPS=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
def m(s):return r'\('+s+r'\)'
def mcq(n,en,ur,ps,opts):
    qi=add('numberedList',f'{n}. '+en,f'{n}. '+ur,f'{n}. '+ps);indices=[]
    for letter,value in zip('ABCD',opts):
        if isinstance(value,str):value=(value,value,value)
        indices.append(add('lines',*(letter+'. '+part for part in value)))
    QUESTIONS.append({'category':'mcq','number':n,'questionIndex':qi,'optionIndices':indices,'answerOrigin':'No answer key is supplied on this source page.'})
mcq(12,'In Liquid Metal Fast Breeder Reactor (LMFBR), the type of uranium used is','مائع دھات کے تیز افزائش کار ری ایکٹر (LMFBR) میں استعمال ہونے والے یورینیم کی قسم ہے','په مایع فلزي چټک روزونکي ریکټر (LMFBR) کې د کارېدونکي یورانیم ډول دی',[m(r'{}^{234}\mathrm{U}'),m(r'{}^{235}\mathrm{U}'),m(r'{}^{238}\mathrm{U}'),m(r'{}^{239}\mathrm{U}')])
mcq(13,'Nuclear force exist between','نیوکلیائی قوت موجود ہوتی ہے','هستوي ځواک د چا ترمنځ موجود دی',[
 ('Proton - proton','پروٹون - پروٹون','پروتون - پروتون'),('Proton - Neutron','پروٹون - نیوٹرون','پروتون - نیوټرون'),('Neutron-Neutron','نیوٹرون-نیوٹرون','نیوټرون-نیوټرون'),('All of these','یہ سب','دا ټول')])
mcq(14,'Which of the following is a boson','درج ذیل میں سے کون سا بوزون ہے','له لاندې څخه کوم یو بوزون دی',[
 ('proton','پروٹون','پروتون'),('neutrino','نیوٹرینو','نیوټرینو'),('photon','فوٹون','فوټون'),('pion','پائیون','پایون')])
mcq(15,'The hadrons formed by combination of quark and anti-quark pair are called','کوارک اور ضد کوارک کے جوڑے کے امتزاج سے بننے والے ہیڈران کہلاتے ہیں','هغه هاډرونونه چې د کوارک او ضد کوارک د جوړې له یوځای کېدو جوړېږي، بلل کېږي',[
 ('baryons','بیریونز','باریونونه'),('mesons','میزونز','مېزونونه'),('meuons','میوآنز','میوونونه'),('neutrinos','نیوٹرینوز','نیوټرینوګانې')])
mcq(16,'All free particles have a color charge of','تمام آزاد ذرات کا رنگی بار ہوتا ہے','د ټولو آزادو ذرو رنګیز چارج دی',['0','2 /3','1/3','1'])
GROUPS.append(('mcqs-12-16','Multiple-choice questions12–16',list(range(len(T)))))
def group(kind,title,ur,ps,rows):
    start=len(T);add('heading',title,ur,ps)
    for n,row in enumerate(rows,1):
        qi=add('numberedList',*(f'{n}. '+part for part in row))
        QUESTIONS.append({'category':kind,'number':n,'questionIndex':qi,'answerOrigin':'No source answer is printed for this question.'})
    GROUPS.append((kind,title,list(range(start,len(T)))))
group('conceptual','CONCEPTUAL QUESTIONS','تصوری سوالات','مفهومي پوښتنې',[
 ('Why do heavier nuclei have more neutrons than protons?','بھاری نیوکلئیسوں میں پروٹونوں سے زیادہ نیوٹرون کیوں ہوتے ہیں؟','درنې هستې ولې تر پروتونونو ډېر نیوټرونونه لري؟'),
 ('Radium has a half -life of about 1600 years. If the universe was formed five billion or more years ago, why is there any radium left now?','ریڈیم کی نصف عمر تقریباً1600 سال ہے۔ اگر کائنات پانچ ارب یا اس سے زیادہ سال پہلے بنی تھی، تو اب بھی کچھ ریڈیم کیوں باقی ہے؟','د رادیم نیم ژوند شاوخوا1600 کاله دی. که کاینات پنځه میلیارده یا تر دې ډېر کاله پخوا جوړ شوي وي، نو اوس ولې لا هم رادیم پاتې دی؟'),
 ('If we focus our attention on a specific nucleus in a radioactive sample, can we know exactly how long that nucleus will live before it decays?','اگر ہم تابکار نمونے میں کسی مخصوص نیوکلئیس پر توجہ مرکوز کریں، تو کیا ہم درست طور پر جان سکتے ہیں کہ زوال سے پہلے وہ نیوکلئیس کتنی دیر زندہ رہے گا؟','که په یوه راډیواکټیف نمونه کې یوې ځانګړې هستې ته پام وکړو، آیا په دقیق ډول پوهېدلی شو چې دا هسته به تر زوال مخکې څومره وخت ژوندۍ وي؟'),
 ('Why are neutrons such good projectiles for producing nuclear reactions?','نیوکلیائی تعاملات پیدا کرنے کے لیے نیوٹرون اتنے اچھے پرتابی ذرات کیوں ہیں؟','نیوټرونونه ولې د هستوي تعاملونو د رامنځته کولو لپاره دومره ښه توغول کېدونکې ذرې دي؟'),
 (r'Why neutron activated nuclides tend to decay by \(\beta^{-}\) rather than \(\beta^{+}\)?',r'نیوٹرون سے فعال ہونے والے نیوکلائیڈز میں \(\beta^{+}\) کے بجائے \(\beta^{-}\) زوال کا رجحان کیوں ہوتا ہے؟',r'د نیوټرون له خوا فعال شوي نوکلایډونه ولې د \(\beta^{+}\) پر ځای د \(\beta^{-}\) له لارې زوال ته میلان لري؟'),
 ('Why are small and large nuclei unstable?','چھوٹے اور بڑے نیوکلئیس غیر مستحکم کیوں ہوتے ہیں؟','کوچنۍ او لویې هستې ولې بې ثباته دي؟'),
 ('Why is a conventional fission nuclear reactor not able to explode as a bomb?','ایک روایتی انشقاقی نیوکلیائی ری ایکٹر بم کی طرح پھٹنے کے قابل کیوں نہیں ہوتا؟','یو دودیز انشقاقي هستوي ریکټر ولې د بم په څېر د چاودېدو وړتیا نه لري؟'),
 ('Why does the fusion of light nuclei into heavier nuclei release energy?','ہلکے نیوکلئیسوں کے امتزاج سے بھاری نیوکلئیس بننے پر توانائی کیوں خارج ہوتی ہے؟','د سپکو هستو په درنو هستو د امتزاج پر مهال ولې انرژي خوشې کېږي؟'),
 ('What factors make a fusion reaction difficult to achieve?','کن عوامل کی وجہ سے امتزاجی تعامل حاصل کرنا مشکل ہوتا ہے؟','کوم عوامل د امتزاجي تعامل ترلاسه کول ستونزمن کوي؟')])
group('comprehensive','COMPREHENSIVE QUESTIONS','جامع سوالات','جامع پوښتنې',[
 ('What is meant by natural radioactivity? How are the natural radioactive radiations classified into three types?','قدرتی تابکاری سے کیا مراد ہے؟ قدرتی تابکار شعاعوں کو تین اقسام میں کس طرح تقسیم کیا جاتا ہے؟','طبیعي راډیواکټیویټي څه معنا لري؟ طبیعي راډیواکټیف وړانګې څنګه په دریو ډولونو وېشل کېږي؟'),
 ('Explain the principle, construction, working and necessary mathematical theory of a mass spectrometer.','کمیتی طیف پیما کا اصول، بناوٹ، کام کرنے کا طریقہ اور ضروری ریاضیاتی نظریہ بیان کریں۔','د کتلې سپکټرومیټر اصل، جوړښت، د کار طریقه او اړینه ریاضيکي نظریه تشریح کړئ.'),
 ('What are isotopes? Explain with examples.','آئسوٹوپس کیا ہیں؟ مثالوں سے وضاحت کریں۔','ایزوټوپونه څه دي؟ له بېلګو سره یې تشریح کړئ.'),
 ('Explain the term mass defect and binding energy related to a nucleus.','نیوکلئیس سے متعلق کمیت کے نقص اور بندشی توانائی کی اصطلاحات کی وضاحت کریں۔','د هستې اړوند د کتلې د نقص او د تړاو د انرژۍ اصطلاحات تشریح کړئ.'),
 ('Define and explain the half -life of a radioactive element?','تابکار عنصر کی نصف عمر کی تعریف اور وضاحت کریں؟','د راډیواکټیف عنصر نیم ژوند تعریف او تشریح کړئ؟'),
 ('Define and explain nuclear reactions.','نیوکلیائی تعاملات کی تعریف اور وضاحت کریں۔','هستوي تعاملونه تعریف او تشریح کړئ.'),
 ('Write a comprehensive note on nuclear fission.','نیوکلیائی انشقاق پر جامع نوٹ لکھیں۔','د هستوي انشقاق په اړه جامع یادښت ولیکئ.'),
 ('What is a nuclear reactor? Give the principle, construction, working and uses of a typical nuclear reactor.','نیوکلیائی ری ایکٹر کیا ہے؟ ایک عام نیوکلیائی ری ایکٹر کا اصول، بناوٹ، کام کرنے کا طریقہ اور استعمال بیان کریں۔','هستوي ریکټر څه دی؟ د یوه عادي هستوي ریکټر اصل، جوړښت، د کار طریقه او استعمالونه بیان کړئ.'),
 ('What is meant by nuclear fusion? Discuss how can energy be released in the fusion process? Illustrate with examples.','نیوکلیائی امتزاج سے کیا مراد ہے؟ وضاحت کریں کہ امتزاج کے عمل میں توانائی کس طرح خارج ہو سکتی ہے؟ مثالوں سے واضح کریں۔','هستوي امتزاج څه معنا لري؟ وڅېړئ چې د امتزاج په بهیر کې انرژي څنګه خوشې کېدای شي؟ په بېلګو یې روښانه کړئ.'),
 ('What is a radiation detector? Explain the principle and working of GM counter and solid state detector.','تابکاری کا سراغ رساں آلہ کیا ہے؟ GM کاؤنٹر اور ٹھوس حالت کے سراغ رساں آلے کا اصول اور کام کرنے کا طریقہ بیان کریں۔','د وړانګو کشفوونکی څه دی؟ د GM شمېرونکي او جامد حالت کشفوونکي اصل او د کار طریقه تشریح کړئ.'),
 ('Discuss the biological and medical uses of radio isotopes.','تابکار آئسوٹوپس کے حیاتیاتی اور طبی استعمالات پر بحث کریں۔','د راډیواکټیف ایزوټوپونو بیولوژیکي او طبي استعمالونه وڅېړئ.'),
 ('Write a comprehensive note on hadrons, leptons and quarks.','ہیڈرانز، لیپٹونز اور کوارکس پر جامع نوٹ لکھیں۔','د هاډرونونو، لېپټونونو او کوارکونو په اړه جامع یادښت ولیکئ.')])
start=len(T);add('heading','NUMERICAL PROBLEMS','عددی مسائل','عددي مسئلې')
def numerical(n,en,ur,ps,answer):
    qi=add('numberedList',*(f'{n}. '+part for part in [en,ur,ps]));ai=add('paragraph','(Answer: '+answer+')','(جواب: '+answer+')','(ځواب: '+answer+')')
    QUESTIONS.append({'category':'numerical','number':n,'questionIndex':qi,'answerIndex':ai,'answerOrigin':'Printed textbook answer; no worked solution supplied.'})
numerical(1,'Find the mass defect and binding energy for helium nucleus?','ہیلیم کے نیوکلئیس کے لیے کمیت کا نقص اور بندشی توانائی معلوم کریں؟','د هیلیم د هستې لپاره د کتلې نقص او د تړاو انرژي پیدا کړئ؟','0.03038 u, 28.3 MeV')
numerical(2,r'The mass of \({}^{14}\mathrm{N}\) nucleus is 13.999234 u, calculate the binding energy.',r'\({}^{14}\mathrm{N}\) کے نیوکلئیس کی کمیت13.999234 u ہے، بندشی توانائی کا حساب لگائیں۔',r'د \({}^{14}\mathrm{N}\) هستې کتله13.999234 u ده؛ د تړاو انرژي حساب کړئ.','104.66 MeV')
numerical(3,r'The half life of radioactive nucleus \({}^{226}_{86}\mathrm{Ra}\) is \(1.6\times10^{3}\) years. Determine the decay constant.',r'تابکار نیوکلئیس \({}^{226}_{86}\mathrm{Ra}\) کی نصف عمر \(1.6\times10^{3}\) سال ہے۔ زوال کا مستقل معلوم کریں۔',r'د راډیواکټیف هستې \({}^{226}_{86}\mathrm{Ra}\) نیم ژوند \(1.6\times10^{3}\) کاله دی. د زوال ثابت وټاکئ.',m(r'1.4\times10^{-11}\ \mathrm{s}^{-1}'))
GROUPS.append(('numericals-1-3','Numerical problems1–3',list(range(start,len(T)))))
def ref(n):return {'pdfPage':196,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-exercise-mcqs-12-16-conceptual-comprehensive-numericals-380-381','title':'MCQs12–16, conceptual and comprehensive questions, numerical problems1–3','kind':'lesson','pdfPage':196,'printedPage':380,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
issues=['Printed381 numerical3 labels radium-226 with atomic-number subscript86 (²²⁶₈₆Ra). Preserved86 rather than silently replacing it with88.']
sec=section(record,T,L,('کثیر الانتخابی، تصوری، جامع اور عددی سوالات','څو ځوابه، مفهومي، جامع او عددي پوښتنې'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(380),ref(381)],sourceBlocks=[],sourceQuestions=QUESTIONS,sourceIssues=issues)
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,exercises=[{'id':'phys20-source-'+key,'title':title,'sourceSectionId':record['id'],'sourceIndices':indices,'sourceReferences':[ref(380 if key.startswith('mcq') or key=='conceptual' else 381)]} for key,title,indices in GROUPS])
    stage_reference(196,record,'Visually inspected both printed380–381 pages, with OCR as aid. Restored MCQs12–16 and every option (including printed “meuons”), all9 conceptual and12 comprehensive questions, and numerical problems1–3 with exactly the supplied answers. Every question/option/answer has aligned Urdu/Pashto; source references connect each group to the exercise view. Source Ra subscript86 retained and flagged; no worked answers invented.',issues)
    print('PDF196 complete questions staged; source Ra notation flagged.')
