"""PDF182 complete source table and every worked-example step."""
from class12_source_review import upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import stage_reference
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];ROWS={}
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
def m(s):return r'\('+s+r'\)'
def eq(s):s=m(s);return add('equation',s,s,s)
add('heading','Table 20.4 DECAY TYPES AND HALF LIVES OF SOME RADIOISOTOPES','جدول20.4 بعض تابکار آئسوٹوپس کے زوال کی اقسام اور نصف عمریں','جدول20.4 د ځینو راډیواکټیف ایزوټوپونو د زوال ډولونه او نیم ژوندونه')
rows=[(['Radioisotope','Decay type','Half Life'],['تابکار آئسوٹوپ','زوال کی قسم','نصف عمر'],['راډیواکټیف ایزوټوپ','د زوال ډول','نیم ژوند'])]
for names,decay,value,units in [
 (['beryllium - 8','بیریلیم - 8','بېریلیم - 8'],r'\alpha',r'2.0\times10^{-10}',['seconds','سیکنڈ','ثانیې']),
 (['carbon-14','کاربن-14','کاربن-14'],r'\beta^{-}',r'5.73\times10^{3}',['years','سال','کاله']),
 (['oxygen - 15','آکسیجن - 15','اکسیجن - 15'],r'\beta^{+}','122.24',['seconds','سیکنڈ','ثانیې']),
 (['cobalt - 60','کوبالٹ - 60','کوبالټ - 60'],r'\beta^{-}','5.3',['years','سال','کاله']),
 (['iodine-131','آیوڈین-131','ایوډین-131'],r'\beta^{-},\gamma','8.04',['days','دن','ورځې']),
 (['Lead - 212','سیسہ - 212','سرب - 212'],r'\beta^{-},\gamma','10.6',['hours','گھنٹے','ساعتونه']),
 (['polonium - 214','پولونیم - 214','پولونیم - 214'],r'\alpha,\gamma','0.1643',['seconds','سیکنڈ','ثانیې']),
 (['radium-226','ریڈیم-226','رادیم-226'],r'\alpha,\gamma',r'1.62\times10^{3}',['years','سال','کاله']),
 (['einsteinium-254','آئن اسٹائنیم-254','آینسټاینیم-254'],r'\alpha,\beta^{-},\gamma','275.7',['days','دن','ورځې'])]:
    rows.append(tuple([names[i],m(decay),m(value)+' '+units[i]] for i in range(3)))
indices=[]
for row in rows:
    index=len(T);indices.append(index);ROWS[index]=row[0];T.append(tuple(' — '.join(cells) for cells in row))
L.append({'type':'table','indices':indices})
add('paragraph',r'The activity ‘A’ is number of disintegrations per unit time (\(\Delta N/\Delta t\)) from equation 4 equals the decay constant times the number of radioactive nuclei in the sample as',
 r'سرگرمی ‘A’ فی اکائی وقت ٹوٹ پھوٹ کی تعداد (\(\Delta N/\Delta t\)) ہے، جو مساوات4 کے مطابق زوال کے مستقل اور نمونے میں تابکار نیوکلئیسوں کی تعداد کے حاصل ضرب کے برابر ہے، یوں',
 r'فعالیت ‘A’ د وخت په یوه واحد کې د تجزیو شمېر (\(\Delta N/\Delta t\)) دی، چې د4 معادلې له مخې د زوال د ثابت او په نمونه کې د راډیواکټیف هستو د شمېر له حاصل ضرب سره برابر دی، داسې')
eq(r'A=-\frac{\Delta N}{\Delta t}=\lambda N\qquad(20.9)')
add('heading','(ii) Units of Activity:','(ii) سرگرمی کی اکائیاں:','(ii) د فعالیت واحدونه:')
add('paragraph',r'A common unit of activity is the curie, abbreviated Ci, which is defined to be \(3.70\times10^{10}\) decays per second. This is approximately equal to the activity of one gram of radium. The SI unit of activity is the becquerel, abbreviated Bq. One becquerel is one decay per second.',
 r'سرگرمی کی ایک عام اکائی کیوری ہے، جس کا مخفف Ci ہے، اور اس کی تعریف فی سیکنڈ \(3.70\times10^{10}\) زوال ہے۔ یہ تقریباً ایک گرام ریڈیم کی سرگرمی کے برابر ہے۔ سرگرمی کی SI اکائی بیکرل ہے، جس کا مخفف Bq ہے۔ ایک بیکرل فی سیکنڈ ایک زوال ہے۔',
 r'د فعالیت یو عام واحد کیوري دی، چې لنډه نښه یې Ci ده او په هره ثانیه کې \(3.70\times10^{10}\) زوالونه تعریف شوی دی. دا د یوه ګرام رادیم له فعالیت سره نږدې برابر دی. د فعالیت SI واحد بېکرېل دی چې لنډه نښه یې Bq ده. یو بېکرېل په هره ثانیه کې یو زوال دی.')
eq(r'1\ \mathrm{Ci}=3.70\times10^{10}\ \mathrm{Bq}=3.70\times10^{10}\ \mathrm{decays/s}')
example_start=len(T)
add('heading','EXAMPLE 20.2','مثال20.2','بېلګه20.2')
add('heading','RADIUM','ریڈیم','رادیم')
problem_index=add('paragraph',r'The half-life of the radioactive radium (\({}^{226}\mathrm{Ra}\)) nucleus is \(5.0\times10^{10}\ \mathrm{s}\). A sample contains \(3.0\times10^{16}\) nuclei. (a) What is the decay constant for this decay? (b) How many radium nuclei will decay per second?',
 r'تابکار ریڈیم (\({}^{226}\mathrm{Ra}\)) کے نیوکلئیس کی نصف عمر \(5.0\times10^{10}\ \mathrm{s}\) ہے۔ ایک نمونے میں \(3.0\times10^{16}\) نیوکلئیس ہیں۔ (a) اس زوال کا مستقل کیا ہے؟ (b) فی سیکنڈ ریڈیم کے کتنے نیوکلئیس زوال پذیر ہوں گے؟',
 r'د راډیواکټیف رادیم (\({}^{226}\mathrm{Ra}\)) هستې نیم ژوند \(5.0\times10^{10}\ \mathrm{s}\) دی. په یوه نمونه کې \(3.0\times10^{16}\) هستې شته. (a) د دې زوال ثابت څه دی؟ (b) په هره ثانیه کې به د رادیم څو هستې زوال وکړي؟')
add('heading','GIVEN','دی گئی معلومات','ورکړل شوي معلومات')
add('paragraph',r'Half life ‘\(T_{1/2}\)’ = \(5.0\times10^{10}\ \mathrm{s}\)',r'نصف عمر ‘\(T_{1/2}\)’ = \(5.0\times10^{10}\ \mathrm{s}\)',r'نیم ژوند ‘\(T_{1/2}\)’ = \(5.0\times10^{10}\ \mathrm{s}\)')
add('paragraph',r'Number of nuclei ‘N’ = \(3.0\times10^{16}\)',r'نیوکلئیسوں کی تعداد ‘N’ = \(3.0\times10^{16}\)',r'د هستو شمېر ‘N’ = \(3.0\times10^{16}\)')
add('heading','REQUIRED','مطلوب','غوښتل شوي')
add('paragraph',r'(a) decay constant ‘\(\lambda\)’ = ?',r'(a) زوال کا مستقل ‘\(\lambda\)’ = ?',r'(a) د زوال ثابت ‘\(\lambda\)’ = ?')
add('paragraph','(b) Activity ‘A’ = ?','(b) سرگرمی ‘A’ = ?','(b) فعالیت ‘A’ = ?')
add('heading','SOLUTION','حل','حل')
add('paragraph',r'(a) The relation between decay constant \(\lambda\) and half life \(T_{1/2}\) is',r'(a) زوال کے مستقل \(\lambda\) اور نصف عمر \(T_{1/2}\) کے درمیان تعلق ہے',r'(a) د زوال د ثابت \(\lambda\) او نیم ژوند \(T_{1/2}\) ترمنځ اړیکه ده')
eq(r'T_{1/2}=\frac{0.693}{\lambda}')
add('paragraph',r'Rearranging     \(\lambda=\frac{0.693}{T_{1/2}}\)',r'ترتیب بدلنے سے     \(\lambda=\frac{0.693}{T_{1/2}}\)',r'په بیا ترتیبولو سره     \(\lambda=\frac{0.693}{T_{1/2}}\)')
add('paragraph',r'Putting values     \(\lambda=\frac{0.693}{5\times10^{10}\ \mathrm{s}}\)',r'قدریں رکھنے سے     \(\lambda=\frac{0.693}{5\times10^{10}\ \mathrm{s}}\)',r'د ارزښتونو په اېښودلو سره     \(\lambda=\frac{0.693}{5\times10^{10}\ \mathrm{s}}\)')
add('paragraph',r'therefore     \(\lambda=1.4\times10^{-11}\ \mathrm{s}^{-1}\)     Answer',r'لہٰذا     \(\lambda=1.4\times10^{-11}\ \mathrm{s}^{-1}\)     جواب',r'نو     \(\lambda=1.4\times10^{-11}\ \mathrm{s}^{-1}\)     ځواب')
add('paragraph',r'(b) The activity is     \(A=\lambda N\)',r'(b) سرگرمی ہے     \(A=\lambda N\)',r'(b) فعالیت دی     \(A=\lambda N\)')
add('paragraph',r'Putting values     \(A=1.4\times10^{-11}\ \mathrm{s}^{-1}\times3\times10^{16}\)',r'قدریں رکھنے سے     \(A=1.4\times10^{-11}\ \mathrm{s}^{-1}\times3\times10^{16}\)',r'د ارزښتونو په اېښودلو سره     \(A=1.4\times10^{-11}\ \mathrm{s}^{-1}\times3\times10^{16}\)')
eq(r'A=4.2\times10^{5}\ \frac{\mathrm{decays}}{\mathrm{s}}=4.2\times10^{5}\ \mathrm{Bq}')
add('paragraph',r'therefore     \(A=4.2\times10^{5}\ \mathrm{Bq}=0.42\ \mathrm{MBq}\)     Answer',r'لہٰذا     \(A=4.2\times10^{5}\ \mathrm{Bq}=0.42\ \mathrm{MBq}\)     جواب',r'نو     \(A=4.2\times10^{5}\ \mathrm{Bq}=0.42\ \mathrm{MBq}\)     ځواب')
add('paragraph','In curies this activity can also be written as','کیوری میں اس سرگرمی کو یوں بھی لکھا جا سکتا ہے','په کیوري کې دا فعالیت داسې هم لیکل کېدای شي')
eq(r'1\ \mathrm{Bq}=\frac{1}{3.70\times10^{10}}\ \mathrm{Ci}')
add('paragraph',r'Multiplying both sides by \(4.2\times10^{5}\) we get',r'دونوں طرف \(4.2\times10^{5}\) سے ضرب دینے سے ہمیں ملتا ہے',r'د دواړو خواوو په \(4.2\times10^{5}\) ضربولو سره ترلاسه کوو')
eq(r'4.2\times10^{5}\ \mathrm{Bq}=\frac{4.2\times10^{5}}{3.70\times10^{10}}\ \mathrm{Ci}')
eq(r'4.2\times10^{5}\ \mathrm{Bq}=1.135\times10^{-5}\ \mathrm{Ci}=0.11\ \mu\mathrm{Ci}')
example_end=len(T);assignment_start=len(T)
add('heading','ASSIGNMENT 20.2','مشق20.2','دنده20.2')
add('heading','CARBON','کاربن','کاربن')
assignment_index=add('paragraph',r'The radioisotope of carbon \({}^{14}\mathrm{C}\) has a half-life of 5730 yr. If a sample contains \(1.00\times10^{22}\) carbon-14 nuclei, what is the activity of the sample?',
 r'کاربن کے تابکار آئسوٹوپ \({}^{14}\mathrm{C}\) کی نصف عمر5730 سال ہے۔ اگر ایک نمونے میں کاربن-14 کے \(1.00\times10^{22}\) نیوکلئیس ہوں تو نمونے کی سرگرمی کیا ہے؟',
 r'د کاربن د راډیواکټیف ایزوټوپ \({}^{14}\mathrm{C}\) نیم ژوند5730 کاله دی. که په یوه نمونه کې د کاربن-14 \(1.00\times10^{22}\) هستې وي، د نمونې فعالیت څه دی؟')
answer_index=add('paragraph',r'(Answer: \(3.83\times10^{10}\ \mathrm{Bq}\))',r'(جواب: \(3.83\times10^{10}\ \mathrm{Bq}\))',r'(ځواب: \(3.83\times10^{10}\ \mathrm{Bq}\))')
def ref(n):return {'pdfPage':182,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-activity-units-example-and-assignment-352-353','title':'Radioisotope half-lives, activity, Example20.2 and Assignment20.2','kind':'lesson','pdfPage':182,'printedPage':352,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
issues=['Example20.2 prints1.135×10⁻⁵Ci =0.11μCi. The microcurie conversion is inconsistent; both printed values retained.']
sec=section(record,T,L,('تابکار آئسوٹوپس کی نصف عمریں، سرگرمی، مثال20.2 اور مشق20.2','د راډیواکټیف ایزوټوپونو نیم ژوندونه، فعالیت، بېلګه20.2 او دنده20.2'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(352),ref(353)],sourceBlocks=[],sourceTableRows=ROWS,sourceIssues=issues)
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,
          formulas=[{'id':'phys20-activity-equation','name':'Activity','number':'20.9','formula':'A = −ΔN/Δt = λN','latex':r'A=-\frac{\Delta N}{\Delta t}=\lambda N','sourceClass12Physics':True,'sourceReferences':[ref(352)]}],
          retire_worked_examples=['textbook-example-2'],
          worked_examples=[{'id':'phys20-example-20-2','title':'EXAMPLE20.2 — RADIUM','problem':T[problem_index][0],'sourceSectionId':record['id'],'sourceIndices':list(range(example_start,example_end)),'answer':r'\(\lambda=1.4\times10^{-11}\ \mathrm{s}^{-1}\); \(A=4.2\times10^{5}\ \mathrm{Bq}=0.42\ \mathrm{MBq}\); printed \(1.135\times10^{-5}\ \mathrm{Ci}=0.11\ \mu\mathrm{Ci}\) (source conversion inconsistent).','sourceReferences':[ref(353)]}],
          exercises=[{'id':'phys20-assignment-20-2','title':'ASSIGNMENT20.2 — CARBON','problem':T[assignment_index][0],'answer':T[answer_index][0],'sourceSectionId':record['id'],'sourceIndices':list(range(assignment_start,len(T))),'sourceReferences':[ref(353)]}])
    stage_reference(182,record,'Reinspected PDF182 printed352–353. Replaced the compressed summary with all nine isotope/decay/half-life table rows, exact activity prose/equation20.9/unit paragraph, complete radium Example20.2 question/given/required and every printed solution line, and Assignment20.2 question/answer. Full aligned Urdu/Pashto prose and table values. Canonical worked example and assignment point to this source section; duplicate legacy example2 removed. The printed0.11μCi conversion is retained and flagged.',issues)
    print('PDF182 full table and worked steps staged; printed conversion retained.')
