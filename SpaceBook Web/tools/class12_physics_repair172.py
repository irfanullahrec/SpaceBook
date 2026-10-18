"""PDF172 chapter boundary: full Unit19 questions and Unit20 opener."""
from class12_source_review import upsert,section,shared_class_data_lock,sync_companions
from class12_fidelity_repair import stage_reference
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];QUESTIONS=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
def question(n,en,ur,ps):
    i=add('paragraph',f'{n}. '+en,f'{n}. '+ur,f'{n}. '+ps);QUESTIONS.append({'number':n,'index':i});return i
def ans(en,ur=None,ps=None):
    i=add('paragraph','(Answer: '+en+')','(جواب: '+(ur or en)+')','(ځواب: '+(ps or en)+')');QUESTIONS[-1]['answerIndex']=i
add('heading','COMPREHENSIVE QUESTIONS','تفصیلی سوالات','تفصیلي پوښتنې')
question(1,'Describe the spectrum of hydrogen atom in detail.','ہائیڈروجن کے ایٹم کا طیف تفصیل سے بیان کریں۔','د هایدروجن د اټوم طیف په تفصیل بیان کړئ.')
question(2,"What are Bohr’s postulates about hydrogen atom? Hence derive expression for the (a) radii of electron orbit (b) energy of the electron.",'ہائیڈروجن کے ایٹم کے بارے میں بوہر کے مفروضات کیا ہیں؟ ان سے (a) الیکٹران کے مدار کے رداسوں (b) الیکٹران کی توانائی کے لیے ریاضیاتی اظہار اخذ کریں۔','د هایدروجن د اټوم په اړه د بوهر فرضیې څه دي؟ له هغو څخه د (a) د الکترون د مدار شعاعوو (b) د الکترون د انرژۍ لپاره ریاضي څرګندونې راوباسئ.')
question(3,'Explain the terms Ground state, Excited state, Excitation energy, Ionization energy.','بنیادی حالت، برانگیختہ حالت، برانگیختگی کی توانائی اور آئن سازی کی توانائی کی اصطلاحات سمجھائیں۔','د بنسټیز حالت، تحریک شوي حالت، د تحریک انرژۍ او د آیون جوړولو انرژۍ اصطلاحات تشریح کړئ.')
question(4,'What are X-rays? How these rays are produced? Differentiate between Characteristic and Continuous X-rays.','ایکس ریز کیا ہیں؟ یہ شعاعیں کیسے پیدا ہوتی ہیں؟ خصوصیتی اور مسلسل ایکس ریز کے درمیان فرق کریں۔','اېکس وړانګې څه دي؟ دا وړانګې څنګه تولیدېږي؟ د ځانګړو او پرله پسې اېکس وړانګو ترمنځ توپیر وکړئ.')
question(5,'What is a laser? Explain the principle and operation of a laser.','لیزر کیا ہے؟ لیزر کا اصول اور کام کرنے کا طریقہ سمجھائیں۔','لېزر څه دی؟ د لېزر اصل او د کار کولو بهیر تشریح کړئ.')
comp_end=len(T);comp_questions=QUESTIONS[:];QUESTIONS=[]
add('heading','NUMERICAL PROBLEMS','عددی مسائل','عددي مسئلې')
question(1,'Calculate the shortest and longest wavelength of radiation for the Paschen Series.','پاشن سلسلے کی تابکاری کے سب سے چھوٹے اور سب سے بڑے طولِ موج حساب کریں۔','د پاشن لړۍ د وړانګو تر ټولو لنډ او اوږد څپې اوږدوالی محاسبه کړئ.')
ans('1875 nm, 820 nm')
question(2,'In the fifth energy level determine the radius and energy of electron for hydrogen atom?','ہائیڈروجن کے ایٹم میں پانچویں توانائی سطح پر الیکٹران کا رداس اور توانائی معلوم کریں؟','د هایدروجن د اټوم په پنځمه انرژۍ کچه کې د الکترون شعاع او انرژي معلومه کړئ؟')
ans(r'1.323 nm, \(-8.72\times10^{-20}\ \mathrm{J}\) or -0.545 eV',r'1.323 nm، \(-8.72\times10^{-20}\ \mathrm{J}\) یا -0.545 eV',r'1.323 nm، \(-8.72\times10^{-20}\ \mathrm{J}\) یا -0.545 eV')
question(3,'An electron drops from the second energy level to the first energy level within an excited hydrogen atom (a) determine the energy of the photon emitted (b) calculate the frequency of the photon emitted (c) calculate the wavelength of the photon emitted.',
 'برانگیختہ ہائیڈروجن ایٹم میں ایک الیکٹران دوسری توانائی سطح سے پہلی توانائی سطح پر آتا ہے (a) خارج ہونے والے فوٹون کی توانائی معلوم کریں (b) خارج ہونے والے فوٹون کی تعدد حساب کریں (c) خارج ہونے والے فوٹون کا طولِ موج حساب کریں۔',
 'په یوه تحریک شوي هایدروجن اټوم کې الکترون له دویمې انرژۍ کچې لومړۍ انرژۍ کچې ته راکوزېږي (a) د خپاره شوي فوټون انرژي معلومه کړئ (b) د خپاره شوي فوټون فریکونسي محاسبه کړئ (c) د خپاره شوي فوټون څپې اوږدوالی محاسبه کړئ.')
ans(r'(a) 10.2 eV (b) \(2.5\times10^{15}\ \mathrm{Hz}\) (c) 120 nm')
question(4,'Find the wavelength associated with an electron in the state n=4 of hydrogen.','ہائیڈروجن کی حالت n=4 میں الیکٹران سے وابستہ طولِ موج معلوم کریں۔','د هایدروجن په n=4 حالت کې له الکترون سره تړلی څپې اوږدوالی پیدا کړئ.')
ans('1.33 nm')
question(5,'An electron is in the first Bohr orbit of hydrogen atom. (a) Find the speed of electron, and (b) the time required for electron to circle the nucleus.',
 'ایک الیکٹران ہائیڈروجن ایٹم کے پہلے بوہر مدار میں ہے۔ (a) الیکٹران کی رفتار اور (b) نیوکلئیس کے گرد ایک چکر لگانے کے لیے الیکٹران کو درکار وقت معلوم کریں۔',
 'یو الکترون د هایدروجن د اټوم په لومړي بوهر مدار کې دی. (a) د الکترون سرعت او (b) د هستې چاپېره د الکترون د یوه چکر لپاره اړین وخت پیدا کړئ.')
ans(r'(a) \(2.19\times10^{6}\ \mathrm{m/s}\) (b) \(1.52\times10^{-16}\ \mathrm{s}\)')
question(6,'If the shortest wavelength produced by an X-ray tube is 0.46 nm, what is the voltage applied to the tube?','اگر ایک ایکس رے ٹیوب سے پیدا ہونے والا سب سے چھوٹا طولِ موج0.46 nm ہو تو ٹیوب پر لگایا گیا وولٹیج کیا ہے؟','که د یوې اېکس وړانګو نل له خوا تولید شوی تر ټولو لنډ څپې اوږدوالی0.46 nm وي، پر نل لګول شوی ولتاژ څومره دی؟')
ans('2.7 kV')
num_questions=QUESTIONS[:]
def ref(n):return {'pdfPage':172,'printedPage':n,'sourcePdf':SOURCE}
r19={'id':'phys19-comprehensive-numerical-exercises-332','title':'Unit19 comprehensive questions and numerical problems','kind':'exercise','pdfPage':172,'printedPage':332,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
s19=section(r19,T,L,('یونٹ19 کے تفصیلی سوالات اور عددی مسائل','د19 واحد تفصیلي پوښتنې او عددي مسئلې'))
issues=['Numerical problem1 asks for shortest and longest Paschen wavelengths in that order, while its printed answer lists1875nm,820nm in descending order. Values and order retained.']
s19.update(kind='exercise',sourceClass12Physics=True,sourceReferences=[ref(332)],sourceBlocks=[],sourceIssues=issues,sourceQuestions=comp_questions+num_questions)
groups=[]
for key,title,qs,indices in [('comprehensive','COMPREHENSIVE QUESTIONS',comp_questions,list(range(comp_end))),('numericals','NUMERICAL PROBLEMS',num_questions,list(range(comp_end,len(T))))]:
    problems=[]
    for q in qs:
        i=q['index'];item={'id':f"textbook-exercise-19-{'numerical' if key=='numericals' else key}-q{q['number']}",'qNo':str(q['number']),'question':T[i][0].split('. ',1)[1],'questionUrdu':T[i][1].split('. ',1)[1],'questionPashto':T[i][2].split('. ',1)[1],'options':[],'sourceReferences':[ref(332)],'solutionOrigin':'printed_answer_only' if 'answerIndex' in q else 'not_provided_in_textbook'}
        if 'answerIndex' in q:item['answer']=T[q['answerIndex']][0]
        problems.append(item)
    groups.append({'id':'textbook-exercise-19-'+key,'exercise':'Exercise19','title':title,'problems':problems,'sourceSectionId':r19['id'],'sourceIndices':indices,'sourceReferences':[ref(332)]})
T=[];L=[]
add('heading','UNIT 20','یونٹ20','واحد20')
add('heading','NUCLEAR PHYSICS','نیوکلیائی طبیعیات','هستوي فزیک')
add('paragraph','How Sun produces large amount of energy?','سورج بڑی مقدار میں توانائی کیسے پیدا کرتا ہے؟','لمر څنګه زیاته انرژي تولیدوي؟')
add('heading','LEARNING OUTCOMES','حاصلاتِ تعلم','د زده کړې پایلې')
add('paragraph','After studying this unit the students will be able to','اس یونٹ کے مطالعے کے بعد طلبہ اس قابل ہوں گے کہ','د دې واحد له لوستلو وروسته به زده کوونکي وکولی شي چې')
add('paragraph','describe a simple model for the atom to include protons, neutrons and electrons.','پروٹون، نیوٹرون اور الیکٹران پر مشتمل ایٹم کا سادہ نمونہ بیان کریں۔','د اټوم یو ساده ماډل بیان کړي چې پروتونونه، نیوټرونونه او الکترونونه پکې شامل وي.')
add('paragraph',r'Determine the number of protons, neutrons and nucleons it contains for the specification of a nucleus in the form \({}^{A}_{Z}\mathrm{X}\).',r'کسی نیوکلئیس کی \({}^{A}_{Z}\mathrm{X}\) صورت میں دی گئی علامت سے اس میں موجود پروٹونوں، نیوٹرونوں اور نیوکلیونوں کی تعداد معلوم کریں۔',r'د یوې هستې د \({}^{A}_{Z}\mathrm{X}\) په بڼه له ورکړل شوې نښې څخه په هغې کې د پروتونونو، نیوټرونونو او نیوکلیونونو شمېر معلوم کړي.')
add('paragraph','explain that an element can exist in various isotopic forms each with a different number of neutrons.','سمجھائیں کہ ایک عنصر مختلف آئسوٹوپی صورتوں میں موجود ہو سکتا ہے، جن میں سے ہر ایک میں نیوٹرونوں کی تعداد مختلف ہوتی ہے۔','تشریح کړي چې یو عنصر په بېلابېلو ایزوټوپي بڼو کې موجودېدای شي او هره بڼه د نیوټرونونو بېل شمېر لري.')
add('paragraph','explain the use of mass spectrograph to demonstrate the existence of isotopes and to measure their relative abundance.','آئسوٹوپس کا وجود ظاہر کرنے اور ان کی نسبتی فراوانی ناپنے کے لیے ماس اسپیکٹروگراف کا استعمال سمجھائیں۔','د ایزوټوپونو د شتون د ښودلو او د هغوی د نسبي کثرت د اندازه کولو لپاره د کتلي طیف ثبتوونکي کارول تشریح کړي.')
add('paragraph','define the terms unified mass scale, mass defect and calculate binding energy using Einstein’s equation.','متحدہ کمیتی پیمانے اور کمیتی نقص کی اصطلاحات کی تعریف کریں اور آئن اسٹائن کی مساوات سے بندشی توانائی حساب کریں۔','د متحد کتلیز مقیاس او د کتلې د کسر اصطلاحات تعریف کړي او د آینسټاین له معادلې څخه د تړون انرژي محاسبه کړي.')
add('paragraph','illustrate graphically the variation of binding energy per nucleon with the mass number.','کمیتی عدد کے ساتھ فی نیوکلیون بندشی توانائی کی تبدیلی گراف سے ظاہر کریں۔','له کتلیز عدد سره د هر نیوکلیون د تړون انرژۍ بدلون په ګراف کې وښيي.')
add('paragraph','explain the relevance of binding energy per nucleon to nuclear fusion and to nuclear fission.','فی نیوکلیون بندشی توانائی کا نیوکلیائی امتزاج اور نیوکلیائی انشقاق سے تعلق سمجھائیں۔','د هر نیوکلیون د تړون انرژۍ تړاو له هستوي امتزاج او هستوي انشقاق سره تشریح کړي.')
add('paragraph','identify that some nuclei are unstable, give out radiation to get rid of excess energy and are said to be radioactive.','شناخت کریں کہ کچھ نیوکلئیس غیر مستحکم ہوتے ہیں، اضافی توانائی نکالنے کے لیے تابکاری خارج کرتے ہیں اور تابکار کہلاتے ہیں۔','وپېژني چې ځینې هستې ناپایدارې دي، د اضافي انرژۍ د لرې کولو لپاره وړانګې خپروي او راډیواکټیف بلل کېږي.')
add('paragraph','describe that an element may change into another element when radioactivity occurs.','بیان کریں کہ تابکاری کے دوران ایک عنصر دوسرے عنصر میں بدل سکتا ہے۔','بیان کړي چې د راډیواکټیفیت د پېښېدو پر مهال یو عنصر په بل عنصر بدلېدای شي.')
r20={'id':'phys20-nuclear-physics-outcomes-opener-333','title':'Unit20 Nuclear Physics — learning outcomes','kind':'lesson','pdfPage':172,'printedPage':333,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
s20=section(r20,T,L,('یونٹ20 نیوکلیائی طبیعیات — حاصلاتِ تعلم','واحد20 هستوي فزیک — د زده کړې پایلې'))
s20.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(333)],sourceBlocks=[],sourceExcludedVisuals=[{'description':'Sun background on Unit20 opener','reason':'Decorative chapter background, without instructional labels; original title and Sun-energy question retained.'}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([r19],[s19],chapter_index=8)
        sync_companions(chapter_index=8,exercises=groups)
        upsert([r20],[s20],chapter_index=9)
    stage_reference(172,r19,'Reinspected both PDF172 halves, printed332–333. Retained all five comprehensive questions, six numerical questions and separate printed answer lines, restored numbering/headings/punctuation and complete translations. Existing exercise groups reuse exact source paragraphs and keep source answers only. Unit20 opener now includes full titles, Sun-energy question, learning-outcome lead-in and all nine original outcomes/case. Decorative solar background excluded. Both chapter records included in the saved source comparison.',issues,additional_records=[r20])
    print('PDF172 both chapter halves staged; source answer ordering flagged.')
