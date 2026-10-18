"""PDF195 glossary and MCQs1–11; unreadable MCQ10 remains expressly unresolved."""
from class12_source_review import upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import stage_reference
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];QUESTIONS=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
G=[
 ('Nucleons: The protons and neutrons present in the nucleus','نیوکلیونز: نیوکلئیس میں موجود پروٹون اور نیوٹرون','نوکلیونونه: په هسته کې موجود پروتونونه او نیوټرونونه'),
 ('Isotopes: Nuclei of an element that have the same charge number Z, but have different mass number A.','آئسوٹوپس: کسی عنصر کے وہ نیوکلئیس جن کا باری عدد Z یکساں، لیکن کمیتی عدد A مختلف ہوتا ہے۔','ایزوټوپونه: د یوه عنصر هغه هستې چې د چارج عدد Z یې یو شان، خو د کتلې عدد A یې بېل وي.'),
 ('Atomic mass unit (u): the mass of 12ᵗʰ part of the mass of carbon -12 atom.','ایٹمی کمیت کی اکائی (u): کاربن -12 کے ایٹم کی کمیت کے بارہویں حصے کی کمیت۔','د اټومي کتلې واحد (u): د کاربن -12 اټوم د کتلې د دولسمې برخې کتله.'),
 ('Binding energy: the energy needed to separate nucleus into individual protons and neutrons. Binding energy per nucleon gives the stability of the nucleus, larger the value more stable the nucleus.','بندشی توانائی: نیوکلئیس کو الگ الگ پروٹونوں اور نیوٹرونوں میں جدا کرنے کے لیے درکار توانائی۔ فی نیوکلیون بندشی توانائی نیوکلئیس کا استحکام بتاتی ہے؛ قدر جتنی زیادہ ہو، نیوکلئیس اتنا ہی زیادہ مستحکم ہوتا ہے۔','د تړاو انرژي: هغه انرژي چې د هستې په جلا جلا پروتونونو او نیوټرونونو د بېلولو لپاره اړینه وي. د هر نوکلیون د تړاو انرژي د هستې ثبات ښيي؛ څومره چې ارزښت لوی وي، هسته هغومره ثابته وي.'),
 ('Radioactivity: the emission of rays from the nuclei of atoms','تابکاری: ایٹموں کے نیوکلئیسوں سے شعاعوں کا اخراج','راډیواکټیویټي: د اټومونو له هستو څخه د وړانګو خپرېدل'),
 ('Activity: the number of disintegrations per unit time','سرگرمی: فی اکائی وقت ٹوٹ پھوٹ کی تعداد','فعالیت: د وخت په یوه واحد کې د تجزیو شمېر'),
 ('Random process: A process without defined pattern, rule or method','بے ترتیب عمل: ایسا عمل جس کا کوئی متعین نمونہ، قاعدہ یا طریقہ نہ ہو','تصادفي بهیر: داسې بهیر چې ټاکلې بڼه، قاعده یا طریقه ونه لري'),
 ('Spontaneous process: A process occurring without apparent external cause','خودبخود عمل: ایسا عمل جو کسی ظاہری بیرونی سبب کے بغیر ہو','خپل سری بهیر: هغه بهیر چې له څرګند بهرني لامل پرته رامنځته کېږي'),
 ('becquerel (Bq): SI unit for rate of decay of a radioactive material','بیکرل (Bq): تابکار مادے کے زوال کی شرح کی SI اکائی','بېکرېل (Bq): د راډیواکټیف مادې د زوال د کچې SI واحد'),
 ('Decay constant: quantity that is inversely proportional to the half-life and that is used in equation for number of nuclei as a function of time','زوال کا مستقل: وہ مقدار جو نصف عمر کے معکوس متناسب ہوتی ہے اور وقت کے تابع نیوکلئیسوں کی تعداد کی مساوات میں استعمال ہوتی ہے','د زوال ثابت: هغه کمیت چې له نیم ژوند سره معکوس تناسب لري او د وخت د تابع په توګه د هستو د شمېر په معادله کې کارېږي'),
 ('Half life: The time in which there is a 50% chance that a nucleus will decay','نصف عمر: وہ وقت جس میں کسی نیوکلئیس کے زوال پذیر ہونے کا امکان 50% ہو','نیم ژوند: هغه وخت چې پکې د یوې هستې د زوال احتمال 50% وي'),
 ('Nuclear Reaction: an incident nucleus, particle, or photon causes a change to occur in a target nucleus.','نیوکلیائی تعامل: آنے والا نیوکلئیس، ذرہ یا فوٹون ہدف نیوکلئیس میں تبدیلی پیدا کرتا ہے۔','هستوي تعامل: لګېدونکې هسته، ذره یا فوټون په هدف هسته کې د بدلون لامل کېږي.'),
 ('Nuclear reaction energy: the energy created in a nuclear reaction','نیوکلیائی تعامل کی توانائی: نیوکلیائی تعامل میں پیدا ہونے والی توانائی','د هستوي تعامل انرژي: هغه انرژي چې په هستوي تعامل کې پیدا کېږي'),
 ('Radiation detector: a device that is used to detect and track the radiation from a radioactive reaction','تابکاری کا سراغ رساں آلہ: وہ آلہ جو تابکار تعامل کی تابکاری دریافت کرنے اور اس کا راستہ معلوم کرنے کے لیے استعمال ہوتا ہے','د وړانګو کشفوونکی: هغه وسیله چې د راډیواکټیف تعامل د وړانګو د موندلو او څارلو لپاره کارول کېږي'),
 ('Nuclear fission: nuclear reaction in which a nucleus splits','نیوکلیائی انشقاق: ایسا نیوکلیائی تعامل جس میں ایک نیوکلئیس تقسیم ہوتا ہے','هستوي انشقاق: هغه هستوي تعامل چې پکې یوه هسته وېشل کېږي'),
 ('Critical mass: minimum amount necessary for self-sustained fission of a given nuclide','بحرانی کمیت: کسی معین نیوکلائیڈ کے خود برقرار رہنے والے انشقاق کے لیے درکار کم از کم مقدار','بحراني کتله: د یوه ټاکلي نوکلایډ د په خپله دوام کوونکي انشقاق لپاره اړین لږ تر لږه مقدار'),
 ('Nuclear fusion: a reaction in which two nuclei are combined, or fused, to form a larger nucleus','نیوکلیائی امتزاج: ایسا تعامل جس میں دو نیوکلئیس مل کر، یا ضم ہو کر، بڑا نیوکلئیس بناتے ہیں','هستوي امتزاج: هغه تعامل چې پکې دوه هستې سره یوځای یا مدغمېږي او یوه لویه هسته جوړوي'),
 ('Quark: an elementary particle and a fundamental constituent of matter','کوارک: ایک بنیادی ذرہ اور مادے کا بنیادی جزو','کوارک: یوه بنسټیزه ذره او د مادې بنسټیزه برخه')]
for row in G:add('definition',*row)
exercise_start=len(T)
add('heading','Exercise','مشق','تمرین')
add('heading','MULTIPLE CHOICE QUESTIONS','کثیر الانتخابی سوالات','څو ځوابه پوښتنې')
add('paragraph','Choose the best possible answer','بہترین ممکن جواب منتخب کریں','تر ټولو غوره ممکن ځواب وټاکئ')
def q(number,en,ur,ps,options):
    questionIndex=add('numberedList',f'{number}. '+en,f'{number}. '+ur,f'{number}. '+ps)
    optionIndices=[]
    for letter,value in zip('ABCD',options):
        if isinstance(value,str):value=(value,value,value)
        optionIndices.append(add('lines',*(letter+'. '+part for part in value)))
    QUESTIONS.append({'number':number,'questionIndex':questionIndex,'optionIndices':optionIndices,'answerOrigin':'No answer key is supplied on this source page.'})
def m(s):return r'\('+s+r'\)'
q(1,'One unified mass scale (1u) is equal to:','ایک متحدہ کمیتی پیمانہ (1u) برابر ہے:','د کتلې د یوه متحد مقیاس واحد (1u) له څه سره برابر دی:',[
 m(r'1.660\times10^{-27}\ \mathrm{kg}'),m(r'1.4924\times10^{-10}\ \mathrm{J}'),'931.5 MeV',('All of these','یہ سب','دا ټول')])
q(2,r'The number of neutrons in \({}^{7}\mathrm{Li}\) are',r'\({}^{7}\mathrm{Li}\) میں نیوٹرونوں کی تعداد ہے',r'په \({}^{7}\mathrm{Li}\) کې د نیوټرونونو شمېر دی',['7','4','3','2'])
q(3,'Sum of the masses of constituent nucleons as compared to the mass of the resultant nucleus is','بننے والے نیوکلئیس کی کمیت کے مقابلے میں اس کے اجزائی نیوکلیونوں کی کمیتوں کا مجموعہ ہوتا ہے','د جوړې شوې هستې د کتلې په پرتله د جوړوونکو نوکلیونونو د کتلو مجموعه ده',[
 ('smaller','کم','کمه'),('greater','زیادہ','زیاته'),('same','یکساں','یو شان'),('infinite','لامحدود','بې پایه')])
q(4,'Which one of the following nuclear radiation is similar to electrons','درج ذیل میں سے کون سی نیوکلیائی تابکاری الیکٹرانوں کے مماثل ہے','له لاندې هستوي وړانګو څخه کومې له الکټرونونو سره ورته دي',[m(r'\alpha'),m(r'\beta^{+}'),m(r'\beta^{-}'),m(r'\gamma')])
q(5,'One curie is equal to','ایک کیوری برابر ہے','یو کیوري برابر دی',[m(r'3.70\times10^{-10}\ \mathrm{Bq}'),'1 MBq',m(r'1\times10^{10}\ \mathrm{Bq}'),m(r'3.70\times10^{10}\ \mathrm{Bq}')])
q(6,r'Half-life of the iodine-131 (\({}^{131}\mathrm{I}\)) is 8.02 days and its weight is 20 mg. After 4 half-lives, the amount left un-decayed will be:',
 r'آیوڈین-131 (\({}^{131}\mathrm{I}\)) کی نصف عمر 8.02 دن اور اس کا وزن 20 mg ہے۔ 4 نصف عمروں کے بعد زوال سے بچی ہوئی مقدار ہوگی:',
 r'د ایوډین-131 (\({}^{131}\mathrm{I}\)) نیم ژوند 8.02 ورځې او وزن یې20 mg دی. له4 نیم ژوندونو وروسته به بې زواله پاتې مقدار وي:',['5 mg','2.5 mg','1.25 mg','0.625 mg'])
q(7,r'The unit of decay constant ‘\(\lambda\)’ is',r'زوال کے مستقل ‘\(\lambda\)’ کی اکائی ہے',r'د زوال د ثابت ‘\(\lambda\)’ واحد دی',['m',m(r'\mathrm{m}^{-1}'),'s',m(r'\mathrm{s}^{-1}')])
q(8,r'In fission of \({}^{235}\mathrm{U}\), neutrons used have energies of about',r'\({}^{235}\mathrm{U}\) کے انشقاق میں استعمال ہونے والے نیوٹرونوں کی توانائی تقریباً ہوتی ہے',r'د \({}^{235}\mathrm{U}\) په انشقاق کې د کارېدونکو نیوټرونونو انرژي شاوخوا ده',['5 MeV','0.6 keV','8.6 eV','0.04 eV'])
reaction=m(r'{}^{1}_{0}\mathrm{n}+{}^{16}_{8}\mathrm{O}\rightarrow?+{}^{2}_{1}\mathrm{H}')
q(9,'The nucleus that results from the reaction '+reaction+' is','تعامل '+reaction+' کے نتیجے میں بننے والا نیوکلئیس ہے','له '+reaction+' تعامل څخه رامنځته شوې هسته ده',[m(r'{}^{15}_{7}\mathrm{N}'),m(r'{}^{17}_{8}\mathrm{O}'),m(r'{}^{14}_{8}\mathrm{O}'),m(r'{}^{14}_{7}\mathrm{N}')])
q(10,r'The resulting nucleus in the reaction \(\gamma+?\rightarrow\) [unreadable product nuclide in source] \(+\mathrm{n}\) is',
 r'تعامل \(\gamma+?\rightarrow\) [ماخذ میں پیدا ہونے والے نیوکلائیڈ کی علامت ناقابلِ مطالعہ ہے] \(+\mathrm{n}\) میں بننے والا نیوکلئیس ہے',
 r'په \(\gamma+?\rightarrow\) [په سرچینه کې د محصول نوکلایډ نښه نه لوستل کېږي] \(+\mathrm{n}\) تعامل کې رامنځته شوې هسته ده',[
 m(r'{}^{138}_{56}\mathrm{Ba}'),m(r'{}^{138}_{55}\mathrm{Cs}'),m(r'{}^{138}_{57}\mathrm{La}'),m(r'{}^{136}_{56}\mathrm{Ba}')])
q(11,r'The quantity of \({}^{235}\mathrm{U}\) in naturally occurring uranium is about',r'قدرتی طور پر پائے جانے والے یورینیم میں \({}^{235}\mathrm{U}\) کی مقدار تقریباً ہے',r'په طبیعي یورانیم کې د \({}^{235}\mathrm{U}\) مقدار شاوخوا دی',['0.7%','30%','70%','99.3%'])
def ref(n):return {'pdfPage':195,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-glossary-and-exercise-mcq-378-379','title':'Nuclear physics glossary and multiple-choice questions1–11','kind':'lesson','pdfPage':195,'printedPage':378,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
sec=section(record,T,L,('نیوکلیائی طبیعیات کی اصطلاحات اور کثیر الانتخابی سوالات1–11','د هستوي فزیک اصطلاحات او څو ځوابه پوښتنې1–11'))
issues=['MCQ10 printed product nuclide is garbled/overlapped in the primary spread and the alternate split scan. Legible reaction fragments/options retained with an explicit unreadable-source marker; no isotope or answer inferred.']
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(378),ref(379)],sourceBlocks=[],sourceQuestions=QUESTIONS,sourceIssues=issues)
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.18','20.19'],exercises=[{'id':'phys20-source-mcqs-1-11','title':'Exercise: multiple-choice questions1–11','sourceSectionId':record['id'],'sourceIndices':list(range(exercise_start,len(T))),'sourceQuestions':QUESTIONS,'sourceReferences':[ref(379)]}])
    stage_reference(195,record,'Inspected full high-resolution PDF195 and alternate printed379 crop. Restored all18 glossary entries and exact MCQ1–11 stems/options without answers. Corrected prior transcription errors in MCQ9 (deuterium product and oxygen-17 option). Kept the source’s MCQ5 negative-exponent distractor. MCQ10 remains explicitly unreadable at the product nuclide rather than inferred. Every definition, stem and option has an aligned Urdu/Pashto pair. Superseded glossary/exercise OCR sections20.18–20.19 retired after complete replacement.',issues)
    print('PDF195 glossary and source MCQs staged; MCQ10 remains unresolved.')
