"""Sequential source correction for PDF page 172 of Class 12 Physics, Unit 19 close and Unit 20 opener."""
import json
from html import escape
from class12_source_review import ROOT,upsert,section,checkpoint,sync_companions,shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def ref(n): return {"pdfPage":172,"printedPage":n,"sourcePdf":SOURCE}
def svg(lang):
 L={"en":["nucleus","proton","neutron","electron","fusion","fission","binding energy per nucleon","mass number A"],"ur":["نیوکلئیس","پروٹون","نیوٹرون","الیکٹران","فیوژن","فشن","فی نیوکلیون بندشی توانائی","کمیتی عدد A"],"ps":["هسته","پروټون","نیوټرون","الکترون","فیوژن","فیشن","پر نیوکلیون تړون انرژي","کتلي عدد A"]}[lang]
 b='<circle cx="190" cy="190" r="50" fill="#fde68a" stroke="#a16207" stroke-width="3"/><circle cx="180" cy="180" r="11" fill="#dc2626"/><circle cx="200" cy="190" r="11" fill="#2563eb"/><circle cx="180" cy="205" r="11" fill="#2563eb"/><ellipse cx="190" cy="190" rx="120" ry="65" fill="none" stroke="#16a34a" stroke-width="3"/><circle cx="305" cy="190" r="8" fill="#111827"/><path d="M410 80V300M410 300H620" stroke="#111827" stroke-width="2"/><path d="M430 275Q485 235 520 170T600 110" fill="none" stroke="#7c3aed" stroke-width="4"/><path d="M450 330H600" stroke="#dc2626" stroke-width="4"/>'
 coords=[(145,150),(30,250),(210,245),(315,175),(35,390),(150,390),(350,345),(420,325)]
 for (x,y),t in zip(coords,L): b+=f'<text x="{x}" y="{y}">{escape(t)}</text>'
 return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 430" role="img" aria-label="Simple nucleus model with protons, neutrons and electron, and a binding-energy-per-nucleon trend sketch for nuclear physics" style="width:100%;max-width:660px;height:auto"><rect width="100%" height="100%" fill="#fff"/>'+b+'</svg>'
COMP=[
("Describe the spectrum of hydrogen atom in detail.","ہائیڈروجن ایٹم کے طیف کو تفصیل سے بیان کریں۔","د هایدروجن اتوم طیف په تفصیل بیان کړئ."),
("What are Bohr’s postulates about hydrogen atom? Hence derive expression for the (a) radii of electron orbit (b) energy of the electron.","ہائیڈروجن ایٹم کے بارے میں بوہر کے اصول کیا ہیں؟ ان سے (الف) الیکٹران مدار کے رداس (ب) الیکٹران کی توانائی کا اظہار اخذ کریں۔","د هایدروجن اتوم په اړه د بوهر اصلونه کوم دي؟ له هغو څخه د (الف) د الکترون مدار د شعاع او (ب) د الکترون د انرژۍ فورمولونه راوباسئ."),
("Explain the terms Ground state, Excited state, Excitation energy, Ionization energy.","بنیادی حالت، مثار حالت، تحریک توانائی اور آئنائزیشن توانائی کی اصطلاحات سمجھائیں۔","بنسټیز حالت، مثار حالت، د تحریک انرژي او د ایونایزېشن انرژي تشریح کړئ."),
("What are X-rays? How are these rays produced? Differentiate between Characteristic and Continuous X-rays.","ایکس ریز کیا ہیں؟ یہ کیسے پیدا ہوتی ہیں؟ خصوصیتی اور مسلسل ایکس ریز میں فرق کریں۔","ایکس وړانګې څه دي؟ څنګه تولیدېږي؟ د ځانګړو او پرله‌پسې ایکس وړانګو ترمنځ توپیر وکړئ."),
("What is a laser? Explain the principle and operation of a laser.","لیزر کیا ہے؟ لیزر کا اصول اور عمل سمجھائیں۔","لېزر څه شی دی؟ د لېزر اصل او کار تشریح کړئ."),
]
NUM=[
("Calculate the shortest and longest wavelength of radiation for the Paschen Series.","پاشن سلسلے کی تابکاری کے کم ترین اور طویل ترین طولِ موج حساب کریں۔","د پاشن لړۍ د وړانګو تر ټولو لنډ او اوږد څپې‌اوږدوالی محاسبه کړئ.","1875 nm; 820 nm"),
("In the fifth energy level determine the radius and energy of electron for hydrogen atom?","پانچویں توانائی سطح پر ہائیڈروجن ایٹم کے الیکٹران کا رداس اور توانائی معلوم کریں۔","د هایدروجن اتوم په پنځمه انرژۍ کچه کې د الکترون شعاع او انرژي پیدا کړئ.","1.323 nm; −8.72×10⁻²⁰ J or −0.545 eV"),
("An electron drops from the second energy level to the first energy level within an excited hydrogen atom. (a) determine the energy of the photon emitted (b) calculate the frequency of the photon emitted (c) calculate the wavelength of the photon emitted.","مثار ہائیڈروجن ایٹم میں الیکٹران دوسری سطح سے پہلی سطح پر آتا ہے۔ (الف) خارج فوٹون کی توانائی (ب) تعدد (ج) طولِ موج معلوم کریں۔","په مثار هایدروجن اتوم کې الکترون له دویمې انرژۍ کچې لومړۍ ته راکوزېږي. (الف) د خپاره شوي فوټون انرژي (ب) فریکونسي (ج) څپې‌اوږدوالی محاسبه کړئ.","(a) 10.2 eV; (b) 2.5×10¹⁵ Hz; (c) 120 nm"),
("Find the wavelength associated with an electron in the state n=4 of hydrogen.","ہائیڈروجن میں n=4 حالت کے الیکٹران سے وابستہ طولِ موج معلوم کریں۔","په هایدروجن کې د n=4 حالت له الکترون سره تړلی څپې‌اوږدوالی پیدا کړئ.","1.33 nm"),
("An electron is in the first Bohr orbit of hydrogen atom. (a) Find the speed of electron, and (b) the time required for electron to circle the nucleus.","ہائیڈروجن ایٹم کے پہلے بوہر مدار میں الیکٹران ہے۔ (الف) رفتار اور (ب) نیوکلئیس کے گرد ایک چکر کا وقت معلوم کریں۔","الکترون د هایدروجن اتوم په لومړي بوهر مدار کې دی. (الف) سرعت او (ب) د هستې چاپېره د یوه چکر وخت پیدا کړئ.","(a) 2.19×10⁶ m/s; (b) 1.52×10⁻¹⁶ s"),
("If the shortest wavelength produced by an X-ray tube is 0.46 nm, what is the voltage applied to the tube?","اگر ایکس رے ٹیوب سے پیدا کم ترین طولِ موج 0.46 nm ہو تو لگایا گیا وولٹیج کیا ہے؟","که د ایکس ټیوب تولید شوی تر ټولو لنډ څپې‌اوږدوالی 0.46 nm وي، پلي شوی ولتاژ څومره دی؟","2.7 kV"),
]
OUTCOMES=[
("Describe a simple model for the atom to include protons, neutrons and electrons.","ایٹم کا ایسا سادہ ماڈل بیان کریں جس میں پروٹون، نیوٹرون اور الیکٹران شامل ہوں۔","د اتوم ساده ماډل بیان کړئ چې پروټونونه، نیوټرونونه او الکترونونه پکې وي."),
("Determine the number of protons, neutrons and nucleons it contains for the specification of a nucleus in the form ᴬ_ZX.","ᴬ_ZX صورت میں نیوکلئیس کی تخصیص سے پروٹون، نیوٹرون اور نیوکلیونوں کی تعداد معلوم کریں۔","د ᴬ_ZX په بڼه د هستې له نښان څخه د پروټونونو، نیوټرونونو او نیوکلیونونو شمېر پیدا کړئ."),
("Explain that an element can exist in various isotopic forms each with a different number of neutrons.","سمجھائیں کہ ایک عنصر کے مختلف ہم جا روپ ہو سکتے ہیں جن میں نیوٹرونوں کی تعداد مختلف ہوتی ہے۔","تشریح کړئ چې یو عنصر بېلابېل ایزوټوپونه لرلای شي او د نیوټرونونو شمېر یې توپیر لري."),
("Explain the use of mass spectrograph to demonstrate the existence of isotopes and to measure their relative abundance.","ہم جا روپوں کے وجود اور نسبتی فراوانی کی پیمائش دکھانے کے لیے کمیتی طیف نگار کا استعمال سمجھائیں۔","د ایزوټوپونو د شتون د ښودلو او نسبي کثرت د اندازه کولو لپاره د کتلي طیف‌لیک کارونه تشریح کړئ."),
("Define the terms unified mass scale, mass defect and calculate binding energy using Einstein’s equation.","متحدہ کمیتی پیمانہ اور کمیتی نقص کی تعریف کریں اور آئن سٹائن کی مساوات سے بندشی توانائی حساب کریں۔","متحده کتلي پیمانه او کتلي نیمګړتیا تعریف کړئ او د انشتاین د معادلې په کارولو تړون انرژي محاسبه کړئ."),
("Illustrate graphically the variation of binding energy per nucleon with the mass number.","کمیتی عدد کے ساتھ فی نیوکلیون بندشی توانائی کی تبدیلی گراف کی صورت دکھائیں۔","د کتلي عدد له بدلون سره پر نیوکلیون د تړون انرژۍ بدلون په ګراف کې وښایئ."),
("Explain the relevance of binding energy per nucleon to nuclear fusion and to nuclear fission.","نیوکلیائی فیوژن اور فشن سے فی نیوکلیون بندشی توانائی کا تعلق سمجھائیں۔","د هستوي فیوژن او فیشن لپاره د پر نیوکلیون تړون انرژۍ اهمیت تشریح کړئ."),
("Identify that some nuclei are unstable, give out radiation to get rid of excess energy and are said to be radioactive.","بتائیں کہ کچھ نیوکلئیس غیر مستحکم ہوتے ہیں، زائد توانائی خارج کرنے کے لیے تابکاری دیتے اور ریڈیو ایکٹو کہلاتے ہیں۔","وپېژنئ چې ځینې هستې ناثابتې دي، د اضافي انرژۍ د لرې کولو لپاره وړانګې خپروي او راډیو اکټیف بلل کېږي."),
("Describe that an element may change into another element when radioactivity occurs.","بیان کریں کہ تابکاری کے دوران ایک عنصر دوسرے عنصر میں بدل سکتا ہے۔","تشریح کړئ چې د راډیو اکټیو بهیر پر مهال یو عنصر په بل عنصر بدلېدای شي."),
]
if __name__=="__main__":
 en19=[x[0] for x in COMP]+[x[0]+" Answer: "+x[3] for x in NUM]
 ur19=[x[1] for x in COMP]+[x[1]+" جواب: "+x[3] for x in NUM]
 ps19=[x[2] for x in COMP]+[x[2]+" ځواب: "+x[3] for x in NUM]
 trans19=list(zip(en19,ur19,ps19))
 rec19={"id":"phys19-comprehensive-numerical-exercises-332","title":"Unit 19 comprehensive questions and numerical problems","kind":"exercise","pdfPage":172,"printedPage":332,"sourcePdf":SOURCE,"paragraphs":en19}
 sec19=section(rec19,trans19,[{"type":"comprehensive-question","indices":list(range(5))},{"type":"numerical-problem","indices":list(range(5,11))}],("د 19م یونټ جامع پوښتنې او عددي مسئلې","Unit 19 comprehensive questions and numerical problems"));sec19["kind"]="exercise";sec19["sourceReferences"]=[ref(332)]
 rec20={"id":"phys20-nuclear-physics-outcomes-opener-333","title":"Unit 20 Nuclear Physics — learning outcomes","kind":"lesson","pdfPage":172,"printedPage":333,"sourcePdf":SOURCE,"paragraphs":[x[0] for x in OUTCOMES]}
 trans20=[(x[0],x[1],x[2]) for x in OUTCOMES]
 sec20=section(rec20,trans20,[{"type":"learning-outcome","indices":list(range(9))}],("فزکس هسته‌اي — د زده‌کړې موخې","Nuclear Physics — learning outcomes"));sec20["kind"]="lesson";sec20["sourceReferences"]=[ref(333)];sec20.update({"diagramSvg":svg("en"),"diagramSvgUrdu":svg("ur"),"diagramSvgPashto":svg("ps")})
 mcq=[{"id":f"textbook-exercise-19-comprehensive-q{i}","qNo":str(i),"question":x[0],"questionUrdu":x[1],"questionPashto":x[2],"options":[],"sourceReferences":[ref(332)],"solutionOrigin":"not_provided_in_textbook"} for i,x in enumerate(COMP,1)]
 nums=[{"id":f"textbook-exercise-19-numerical-q{i}","qNo":str(i),"question":x[0],"questionUrdu":x[1],"questionPashto":x[2],"answer":x[3],"sourceReferences":[ref(332)],"solutionOrigin":"printed_answer_only"} for i,x in enumerate(NUM,1)]
 ex1={"id":"textbook-exercise-19-comprehensive","exercise":"Exercise 19","title":"Comprehensive questions","problems":mcq,"sourceReferences":[ref(332)]}
 ex2={"id":"textbook-exercise-19-numericals","exercise":"Exercise 19","title":"Numerical problems","problems":nums,"sourceReferences":[ref(332)]}
 with shared_class_data_lock():
  upsert([rec19],[sec19],chapter_index=8)
  upsert([rec20],[sec20],chapter_index=9)
  sync_companions(chapter_index=8,exercises=[ex1,ex2])
  progress=json.loads((ROOT/"docs/source-verification/class-12/progress.json").read_text(encoding="utf-8"))
  if progress["nextPage"]==172: checkpoint(172,"corrected_verified",[rec19["id"],rec20["id"]],"Rendered and inspected PDF page 172, printed pages 332–333. Transcribed five Unit 19 comprehensive prompts and six numerical problems with all printed answers; translations aligned, no solutions invented. Split the facing Unit 20 Nuclear Physics opener into chapter index 9 and recorded all nine learning outcomes (atomic model, nuclide notation, isotopes, mass spectrograph, mass defect/binding energy, binding-energy graph, fusion/fission, radioactivity and transmutation) with a coded SVG. Unit 19 records stayed in chapter index 8. Continued Unit 20 at page 173.",printed_pages=[332,333],chapter_number=20)
