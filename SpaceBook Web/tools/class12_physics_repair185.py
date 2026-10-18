"""PDF185 full printed calculations, exercise and fission introduction."""
from class12_source_review import upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import stage_reference
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];ROWS={}
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
def m(s):return r'\('+s+r'\)'
def eq(s):s=m(s);return add('equation',s,s,s)
def masses(left,right):
    start=len(T);rows=[(['LHS','RHS'],['بائیں طرف','دائیں طرف'],['کیڼ اړخ','ښی اړخ'])]
    rows.extend(tuple([m(a),m(b)] for _ in range(3)) for a,b in zip(left,right))
    for row in rows:
        ROWS[len(T)]=row[0];T.append(tuple(' — '.join(cells) for cells in row))
    L.append({'type':'table','indices':list(range(start,len(T)))})
add('heading','B. CONSERVATION OF MASS ENERGY','B. کمیت و توانائی کی بقا','B. د کتلې او انرژۍ بقا')
add('paragraph','Since the mass number differ from atomic masses and difference provides binding energy to nucleons in the nucleus therefore energy conservation should also hold apart from conservation of nucleon number. This also include energy difference due to change in mass from Einstein mass energy relation.',
 'چونکہ کمیتی عدد ایٹمی کمیتوں سے مختلف ہوتا ہے اور یہ فرق نیوکلئیس میں نیوکلیونوں کو بندشی توانائی فراہم کرتا ہے، اس لیے نیوکلیونوں کی تعداد کی بقا کے علاوہ توانائی کی بقا بھی برقرار رہنی چاہیے۔ اس میں آئن اسٹائن کے کمیت و توانائی کے تعلق کے مطابق کمیت کی تبدیلی سے پیدا ہونے والا توانائی کا فرق بھی شامل ہے۔',
 'ځکه چې کتلیز عدد له اټومي کتلو توپیر لري او دا توپیر په هسته کې نیوکلیونونو ته د تړون انرژي برابروي، نو د نیوکلیونونو د شمېر د بقا ترڅنګ باید د انرژۍ بقا هم مراعات شي. په دې کې د آینسټاین د کتلې او انرژۍ د اړیکې له مخې د کتلې له بدلون څخه د انرژۍ توپیر هم شامل دی.')
add('paragraph','For example in the reaction','مثلاً تعامل میں','د بېلګې په توګه په تعامل کې')
eq(r'{}^{4}_{2}\mathrm{He}+{}^{14}_{7}\mathrm{N}\rightarrow{}^{17}_{8}\mathrm{O}+{}^{1}_{1}\mathrm{H}+Q')
add('paragraph','nuclear reaction energy Q can be calculated as','نیوکلیائی تعامل کی توانائی Q یوں حساب کی جا سکتی ہے','د هستوي تعامل انرژي Q داسې محاسبه کېدای شي')
masses([r'{}^{4}_{2}\mathrm{He}=4.00263\ \mathrm{u}',r'{}^{14}_{7}\mathrm{N}=14.00307\ \mathrm{u}',r'=18.005677\ \mathrm{u}'],[r'{}^{1}_{1}\mathrm{H}=1.007825\ \mathrm{u}',r'{}^{17}_{8}\mathrm{O}=16.999133\ \mathrm{u}',r'=18.006958\ \mathrm{u}'])
add('paragraph',r'Since Q is the rest mass difference, therefore Q = 18.005677 u - 18.006958 u','چونکہ Q سکونی کمیت کا فرق ہے، اس لیے Q = 18.005677 u - 18.006958 u','ځکه چې Q د سکون کتلې توپیر دی، نو Q = 18.005677 u - 18.006958 u')
eq(r'Q=-0.001281\ \mathrm{u}=-1.192\ \mathrm{MeV}')
add('paragraph',r'As Q is negative therefore \(\alpha\)-particle having kinetic energy 1.192 MeV can induce such a reaction.',r'چونکہ Q منفی ہے، اس لیے1.192 MeV حرکی توانائی والا \(\alpha\) ذرہ ایسا تعامل پیدا کر سکتا ہے۔',r'ځکه چې Q منفي دی، نو د1.192 MeV حرکي انرژۍ لرونکې \(\alpha\) ذره داسې تعامل رامنځته کولی شي.')
example_start=len(T)
add('heading','EXAMPLE 20.3','مثال20.3','بېلګه20.3')
add('heading','NUCLEAR REACTION','نیوکلیائی تعامل','هستوي تعامل')
problem=add('paragraph','What is the least energy does the proton have to make the following nuclear reaction possible?','درج ذیل نیوکلیائی تعامل کو ممکن بنانے کے لیے پروٹون کی کم سے کم توانائی کتنی ہونی چاہیے؟','د لاندې هستوي تعامل د ممکن کولو لپاره پروتون باید لږ تر لږه څومره انرژي ولري؟')
eq(r'{}^{1}_{1}\mathrm{H}+{}^{13}_{6}\mathrm{C}\rightarrow{}^{14}_{7}\mathrm{N}+{}^{1}_{0}\mathrm{n}')
add('paragraph',r'The mass of hydrogen \({}^{1}\mathrm{H}\) is 1.007825 u, carbon \({}^{13}\mathrm{C}\) is 13.003355 u, neutron \({}^{1}\mathrm{n}\) is 1.008665 u and nitrogen \({}^{13}\mathrm{N}\) is 13.005739 u.',
 r'ہائیڈروجن \({}^{1}\mathrm{H}\) کی کمیت1.007825 u، کاربن \({}^{13}\mathrm{C}\) کی13.003355 u، نیوٹرون \({}^{1}\mathrm{n}\) کی1.008665 u اور نائٹروجن \({}^{13}\mathrm{N}\) کی13.005739 u ہے۔',
 r'د هایدروجن \({}^{1}\mathrm{H}\) کتله1.007825 u، د کاربن \({}^{13}\mathrm{C}\)13.003355 u، د نیوټرون \({}^{1}\mathrm{n}\)1.008665 u او د نایتروجن \({}^{13}\mathrm{N}\)13.005739 u ده.')
add('heading','GIVEN','دی گئی معلومات','ورکړل شوي معلومات')
for words,symbol,value in [(['hydrogen','ہائیڈروجن','هایدروجن'],r'{}^{1}\mathrm{H}','1.007825'),(['carbon','کاربن','کاربن'],r'{}^{13}\mathrm{C}','13.003355'),(['neutron','نیوٹرون','نیوټرون'],r'{}^{1}\mathrm{n}','1.008665'),(['nitrogen','نائٹروجن','نایتروجن'],r'{}^{13}\mathrm{N}','13.005739')]:
    formula='‘'+m(symbol)+'’ = '+value+' u'
    add('paragraph','Mass of '+words[0]+' '+formula,words[1]+' کی کمیت '+formula,'د '+words[2]+' کتله '+formula)
add('heading','REQUIRED','مطلوب','غوښتل شوي')
add('paragraph','Proton energy Q = ?','پروٹون کی توانائی Q = ?','د پروتون انرژي Q = ?')
add('heading','SOLUTION','حل','حل')
add('paragraph','nuclear reaction energy Q can be calculated as','نیوکلیائی تعامل کی توانائی Q یوں حساب کی جا سکتی ہے','د هستوي تعامل انرژي Q داسې محاسبه کېدای شي')
masses([r'{}^{1}_{1}\mathrm{H}=1.007825\ \mathrm{u}',r'{}^{13}_{6}\mathrm{C}=13.003355\ \mathrm{u}',r'=14.011180\ \mathrm{u}'],[r'{}^{13}_{7}\mathrm{N}=13.005739\ \mathrm{u}',r'{}^{1}_{0}\mathrm{n}=1.008665\ \mathrm{u}',r'=14.014404\ \mathrm{u}'])
add('paragraph','Since Q is the rest mass difference, therefore Q = 14.011180 u - 14.014404 u, this means that Q = - 0.003224 u, therefore',
 'چونکہ Q سکونی کمیت کا فرق ہے، اس لیے Q = 14.011180 u - 14.014404 u، اس کا مطلب ہے کہ Q = - 0.003224 u، لہٰذا',
 'ځکه چې Q د سکون کتلې توپیر دی، نو Q = 14.011180 u - 14.014404 u، دا معنا لري چې Q = - 0.003224 u، نو')
answer=add('equation',r'\(Q=-0.003224\ \mathrm{u}\times931.5\ \mathrm{MeV/u}=3.003156\ \mathrm{MeV}=3.00\ \mathrm{MeV}\)     Answer',r'\(Q=-0.003224\ \mathrm{u}\times931.5\ \mathrm{MeV/u}=3.003156\ \mathrm{MeV}=3.00\ \mathrm{MeV}\)     جواب',r'\(Q=-0.003224\ \mathrm{u}\times931.5\ \mathrm{MeV/u}=3.003156\ \mathrm{MeV}=3.00\ \mathrm{MeV}\)     ځواب')
add('paragraph','The negative sign shows that the reaction is endothermic, and proton would require more than 3.00 MeV energy to give excess energy to neutron and nitrogen after formation.',
 'منفی علامت ظاہر کرتی ہے کہ تعامل حرارت گیر ہے، اور بننے کے بعد نیوٹرون اور نائٹروجن کو اضافی توانائی دینے کے لیے پروٹون کو3.00 MeV سے زیادہ توانائی درکار ہوگی۔',
 'منفي نښه څرګندوي چې تعامل تودوخه جذبوونکی دی، او پروتون به له3.00 MeV څخه ډېرې انرژۍ ته اړتیا ولري څو نیوټرون او نایتروجن ته له جوړېدو وروسته اضافي انرژي ورکړي.')
example_end=len(T);assignment_start=len(T)
add('heading','ASSIGNMENT 20.3','مشق20.3','دنده20.3')
add('heading','NUCLEAR REACTION','نیوکلیائی تعامل','هستوي تعامل')
assignment=add('paragraph','The following reaction requires an input of energy equal to 2.438 MeV.','درج ذیل تعامل میں2.438 MeV کے برابر توانائی کی فراہمی درکار ہے۔','لاندې تعامل ته د2.438 MeV په اندازه انرژي ورکول اړین دي.')
eq(r'{}^{1}_{1}\mathrm{H}+{}^{18}_{8}\mathrm{O}\rightarrow{}^{18}_{9}\mathrm{F}+{}^{1}_{0}\mathrm{n}')
add('paragraph',r'The mass of hydrogen \({}^{1}\mathrm{H}\) is 1.007825 u, oxygen \({}^{18}\mathrm{O}\) is 17.999160 u and neutron \({}^{1}\mathrm{n}\) is 1.008665 u.',
 r'ہائیڈروجن \({}^{1}\mathrm{H}\) کی کمیت1.007825 u، آکسیجن \({}^{18}\mathrm{O}\) کی17.999160 u اور نیوٹرون \({}^{1}\mathrm{n}\) کی1.008665 u ہے۔',
 r'د هایدروجن \({}^{1}\mathrm{H}\) کتله1.007825 u، د اکسیجن \({}^{18}\mathrm{O}\)17.999160 u او د نیوټرون \({}^{1}\mathrm{n}\)1.008665 u ده.')
assignment_answer=add('paragraph','[Answer: 18.000937 u]','[جواب:18.000937 u]','[ځواب:18.000937 u]')
assignment_end=len(T)
add('heading','20.12 NUCLEAR FISSION','20.12 نیوکلیائی انشقاق','20.12 هستوي انشقاق')
add('definition','The process of splitting of nuclei into intermediate size nuclei is called nuclear fission. The fission process often produces free neutrons and photons (in the form of gamma rays), and releases a very large amount of energy.',
 'نیوکلئیسوں کے درمیانے جسامت والے نیوکلئیسوں میں ٹوٹنے کے عمل کو نیوکلیائی انشقاق کہتے ہیں۔ انشقاق کا عمل اکثر آزاد نیوٹرون اور فوٹون (گاما شعاعوں کی صورت میں) پیدا کرتا ہے اور بہت بڑی مقدار میں توانائی خارج کرتا ہے۔',
 'د هستو په منځنۍ کچې هستو د وېشل کېدو بهیر هستوي انشقاق بلل کېږي. د انشقاق بهیر ډېری وخت ازاد نیوټرونونه او فوټونونه (د ګاما وړانګو په بڼه) تولیدوي او ډېره زیاته انرژي خوشې کوي.')
add('paragraph','Nuclear fission of heavy elements was discovered on December 17, 1938 by Otto Hahn and his assistant Fritz Strassmann, and explained theoretically in January 1939 by Lise Meitner and her nephew Otto Robert Frisch. Frisch named the process by analogy with biological fission of living cells.',
 'بھاری عناصر کا نیوکلیائی انشقاق17 دسمبر1938 کو اوٹو ہان اور ان کے معاون فرٹز اسٹراسمن نے دریافت کیا، اور جنوری1939 میں لیزے مائٹنر اور ان کے بھانجے اوٹو رابرٹ فرش نے اس کی نظریاتی وضاحت کی۔ فرش نے زندہ خلیوں کے حیاتیاتی انشقاق سے مماثلت کی بنیاد پر اس عمل کا نام رکھا۔',
 'د درنو عناصرو هستوي انشقاق د1938 د دسمبر په17 اوټو هان او د هغه مرستیال فرېټز شټراسمن کشف کړ، او د1939 په جنوري کې لیزه مایټنر او د هغې خوریي اوټو رابرټ فریش په نظري ډول تشریح کړ. فریش د ژوندیو حجرو له بیولوژیکي انشقاق سره د ورته والي له مخې دې بهیر ته نوم ورکړ.')
add('paragraph','They found that a uranium nucleus, after absorbing a neutron, splits into two fragments, of intermediate size. The general nuclear reaction of splitting of a massive nucleus into two less massive fragments is given below.',
 'انہوں نے پایا کہ یورینیم کا نیوکلئیس ایک نیوٹرون جذب کرنے کے بعد درمیانی جسامت کے دو ٹکڑوں میں تقسیم ہو جاتا ہے۔ ایک بھاری نیوکلئیس کے دو کم کمیت والے ٹکڑوں میں تقسیم ہونے کا عمومی نیوکلیائی تعامل ذیل میں دیا گیا ہے۔',
 'دوی وموندله چې د یورانیم هسته د یوه نیوټرون له جذب وروسته په دوو منځنۍ کچې ټوټو وېشل کېږي. د یوې درنې هستې په دوو لږه کتله لرونکو ټوټو د وېش عمومي هستوي تعامل لاندې ورکړل شوی دی.')
e=m(r'{}^{1}_{0}\mathrm{n}+{}^{235}_{92}\mathrm{U}\rightarrow({}^{235}_{92}\mathrm{U})^{*}\rightarrow X+Y+')
add('equation',e+' neutrons',e+' نیوٹرون',e+' نیوټرونونه')
def ref(n):return {'pdfPage':185,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-mass-energy-example-assignment-and-fission-358-359','title':'Mass-energy, nuclear reaction example and fission','kind':'lesson','pdfPage':185,'printedPage':358,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
issues=[
 'Printed He-4 mass4.00263u and N-14 mass14.00307u do not sum to the printed18.005677u. All masses, sum and Q retained.',
 'Example20.3 reaction shows nitrogen-14, while its prose, GIVEN and solution use nitrogen-13 and13.005739u. Both printed isotopes retained.',
 'Example20.3 prints Q=−0.003224u×931.5MeV/u=+3.003156MeV=3.00MeV. The sign inconsistency remains; the following negative-sign/endothermic explanation is preserved.',
 'The fission equation prints excited uranium-235 after neutron capture by uranium-235; the displayed mass number does not conserve nucleon number. Printed235* retained.']
sec=section(record,T,L,('کمیت و توانائی، نیوکلیائی تعامل کی مثال اور انشقاق','کتله او انرژي، د هستوي تعامل بېلګه او انشقاق'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(358),ref(359)],sourceBlocks=[],sourceTableRows=ROWS,sourceIssues=issues)
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_worked_examples=['textbook-example-3'],worked_examples=[{'id':'phys20-example-20-3','title':'EXAMPLE20.3 — NUCLEAR REACTION','problem':T[problem][0],'sourceSectionId':record['id'],'sourceIndices':list(range(example_start,example_end)),'answer':T[answer][0],'sourceReferences':[ref(358),ref(359)]}],exercises=[{'id':'phys20-assignment-20-3','title':'ASSIGNMENT20.3 — NUCLEAR REACTION','problem':T[assignment][0],'answer':T[assignment_answer][0],'sourceSectionId':record['id'],'sourceIndices':list(range(assignment_start,assignment_end)),'sourceReferences':[ref(359)]}])
    stage_reference(185,record,'Reinspected PDF185 printed358–359. Restored full mass-energy prose, both side-by-side mass calculations as semantic tables, all Example20.3 question/given/required/solution steps, Assignment20.3 and complete fission definition/history/introduction/equation. Canonical worked example and exercise reuse complete source paragraphs. Urdu/Pashto aligned translations. Original mass sums, isotope and sign defects retained with explicit source flags.',issues)
    print('PDF185 complete printed calculation steps staged; defects retained.')
