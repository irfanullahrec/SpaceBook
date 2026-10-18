"""PDF177 complete binding-energy graph and first part of Example20.1."""
from class12_source_review import upsert,section,shared_class_data_lock,sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text,arrow,isotope,svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
def m(s):return r'\('+s+r'\)'
def equation_intro(words,s):return add('equation',words[0]+'     '+m(s),words[1]+'     '+m(s),words[2]+'     '+m(s))
add('heading','FIGURE 20.6','شکل20.6','شکل20.6')
L.append({'type':'visual','blockId':'phys20-177-binding-curve'})
add('paragraph','The graph of binding energy per nucleon in MeV to the nucleon number is shown in the figure 20.6.','MeV میں فی نیوکلیون بندشی توانائی اور نیوکلیون عدد کا گراف شکل20.6 میں دکھایا گیا ہے۔','په MeV کې د هر نیوکلیون د تړون انرژۍ او د نیوکلیون د شمېر ګراف په20.6 شکل کې ښودل شوی دی.')
add('heading','i. Intermediate Nuclei:','i. درمیانے نیوکلئیس:','i. منځنۍ هستې:')
add('paragraph',r'The most stable nuclei lie in the region of greater stability and about A = 50 to 60 this is where binding energy per nucleon is greatest almost of 8.7 MeV called intermediate size nuclei. (e. g \({}^{62}_{28}\mathrm{Ni}\) and \({}^{58}_{26}\mathrm{Fe}\))',
 r'سب سے زیادہ مستحکم نیوکلئیس زیادہ استحکام کے خطے میں تقریباً A = 50 سے60 کے درمیان ہوتے ہیں، جہاں فی نیوکلیون بندشی توانائی سب سے زیادہ، تقریباً8.7 MeV ہوتی ہے؛ انہیں درمیانی جسامت کے نیوکلئیس کہتے ہیں۔ (مثلاً \({}^{62}_{28}\mathrm{Ni}\) اور \({}^{58}_{26}\mathrm{Fe}\))',
 r'تر ټولو پایدارې هستې د ډېرې پایدارۍ په سیمه کې، شاوخوا A = 50 تر60 پورې، وي؛ دلته د هر نیوکلیون د تړون انرژي تر ټولو زیاته، نږدې8.7 MeV، ده او منځنۍ کچې هستې بلل کېږي. (لکه \({}^{62}_{28}\mathrm{Ni}\) او \({}^{58}_{26}\mathrm{Fe}\))')
add('heading','ii. Small Nuclei:','ii. چھوٹے نیوکلئیس:','ii. کوچنۍ هستې:')
add('paragraph',r'The decrease in Packing fraction ‘f’ for small ‘A’ is due to surface effect. The particles at or near the surface are less strongly bond than the nucleons at the interior. The smaller the nucleus the larger the percentage of constituents at the nuclear surface. (e. g \({}^{4}_{2}\mathrm{He}\) and \({}^{16}_{8}\mathrm{O}\))',
 r'چھوٹے ‘A’ کے لیے پیکنگ کسر ‘f’ میں کمی سطحی اثر کی وجہ سے ہے۔ سطح پر یا اس کے قریب ذرات اندرونی نیوکلیونوں سے کم مضبوطی سے بندھے ہوتے ہیں۔ نیوکلئیس جتنا چھوٹا ہو، نیوکلیائی سطح پر اجزا کا تناسب اتنا زیادہ ہوتا ہے۔ (مثلاً \({}^{4}_{2}\mathrm{He}\) اور \({}^{16}_{8}\mathrm{O}\))',
 r'د کوچني ‘A’ لپاره د بسته بندۍ کسر ‘f’ کمېدل د سطحې د اغېز له امله دي. پر سطحه یا هغې ته نږدې ذرې د دننه نیوکلیونونو په پرتله په لږ ځواک تړلې دي. هسته چې څومره کوچنۍ وي، پر هستوي سطحه د اجزاوو سلنه همغومره زیاته وي. (لکه \({}^{4}_{2}\mathrm{He}\) او \({}^{16}_{8}\mathrm{O}\))')
add('heading','iii. Large Nuclei:','iii. بڑے نیوکلئیس:','iii. لویې هستې:')
add('paragraph',r'The decrease in ‘f’ for large nuclei is because of large number of protons. The coulomb repulsion between the protons opposes the binding effect of nuclear force. Therefore nuclei with large ‘A’ are unstable. (e. g \({}^{222}_{86}\mathrm{Rn}\) and \({}^{238}_{92}\mathrm{U}\)). The instability shows why a nuclear fission results in large nuclei such as \({}^{235}_{92}\mathrm{U}\). The fission fragments of the nuclei undergoing fission lie in the region of greater stability. The binding energy increases from 7.5 MeV to nearly 8.5 MeV. This difference is the energy liberated in a nuclear fission process.',
 r'بڑے نیوکلئیسوں میں ‘f’ کی کمی پروٹونوں کی بڑی تعداد کی وجہ سے ہوتی ہے۔ پروٹونوں کے درمیان کولمبی دفع نیوکلیائی قوت کے بندشی اثر کی مخالفت کرتی ہے۔ اس لیے بڑے ‘A’ والے نیوکلئیس غیر مستحکم ہوتے ہیں۔ (مثلاً \({}^{222}_{86}\mathrm{Rn}\) اور \({}^{238}_{92}\mathrm{U}\))۔ یہ عدم استحکام ظاہر کرتا ہے کہ \({}^{235}_{92}\mathrm{U}\) جیسے بڑے نیوکلئیسوں میں نیوکلیائی انشقاق کیوں ہوتا ہے۔ انشقاق پذیر نیوکلئیسوں کے انشقاقی ٹکڑے زیادہ استحکام کے خطے میں ہوتے ہیں۔ بندشی توانائی7.5 MeV سے بڑھ کر تقریباً8.5 MeV ہو جاتی ہے۔ یہ فرق نیوکلیائی انشقاق میں خارج ہونے والی توانائی ہے۔',
 r'په لویو هستو کې د ‘f’ کمېدل د پروتونونو د ډېر شمېر له امله دي. د پروتونونو ترمنځ کولمبي دفع د هستوي قوې د تړون له اغېز سره مخالفت کوي. نو د لوی ‘A’ لرونکې هستې ناپایدارې دي. (لکه \({}^{222}_{86}\mathrm{Rn}\) او \({}^{238}_{92}\mathrm{U}\)). دا ناپایداري ښيي چې ولې د \({}^{235}_{92}\mathrm{U}\) په څېر لویو هستو کې هستوي انشقاق پېښېږي. د انشقاق کوونکو هستو ټوټې د ډېرې پایدارۍ په سیمه کې واقع وي. د تړون انرژي له7.5 MeV څخه نږدې8.5 MeV ته زیاتېږي. دا توپیر په هستوي انشقاق کې خوشې شوې انرژي ده.')
example_start=len(T)
add('heading','EXAMPLE 20.1','مثال20.1','بېلګه20.1')
add('heading','SODIUM NUCLEUS','سوڈیم کا نیوکلئیس','د سوډیم هسته')
problem=add('paragraph',r'Sodium \({}^{23}\mathrm{Na}\) has an atomic mass of 22.989,769 u. Find the (a) mass defect (b) binding energy and (c) binding energy per nucleon for this nucleus.',
 r'سوڈیم \({}^{23}\mathrm{Na}\) کی ایٹمی کمیت22.989,769 u ہے۔ اس نیوکلئیس کے لیے (a) کمیتی نقص (b) بندشی توانائی اور (c) فی نیوکلیون بندشی توانائی معلوم کریں۔',
 r'سوډیم \({}^{23}\mathrm{Na}\) د22.989,769 u اټومي کتله لري. د دې هستې لپاره (a) د کتلې کسر (b) د تړون انرژي او (c) د هر نیوکلیون د تړون انرژي پیدا کړئ.')
add('heading','GIVEN','دی گئی معلومات','ورکړل شوي معلومات')
add('paragraph','Number of protons ‘Z’ = 11','پروٹونوں کی تعداد ‘Z’ = 11','د پروتونونو شمېر ‘Z’ = 11')
add('paragraph',r'Mass of proton ‘\(M_{\mathrm{p}}\)’ = 1.007276 u',r'پروٹون کی کمیت ‘\(M_{\mathrm{p}}\)’ = 1.007276 u',r'د پروتون کتله ‘\(M_{\mathrm{p}}\)’ = 1.007276 u')
add('paragraph','Number of neutrons ‘N’ = 12','نیوٹرونوں کی تعداد ‘N’ = 12','د نیوټرونونو شمېر ‘N’ = 12')
add('paragraph',r'Mass of neutron ‘\(M_{\mathrm{n}}\)’ = 1.008665 u',r'نیوٹرون کی کمیت ‘\(M_{\mathrm{n}}\)’ = 1.008665 u',r'د نیوټرون کتله ‘\(M_{\mathrm{n}}\)’ = 1.008665 u')
add('paragraph','Mass of Sodium nucleus M = 22.989769 u','سوڈیم کے نیوکلئیس کی کمیت M = 22.989769 u','د سوډیم د هستې کتله M = 22.989769 u')
add('heading','REQUIRED','مطلوب','غوښتل شوي')
add('paragraph',r'Mass defect ‘\(\Delta m\)’ = ?',r'کمیتی نقص ‘\(\Delta m\)’ = ?',r'د کتلې کسر ‘\(\Delta m\)’ = ?')
add('paragraph',r'Binding Energy ‘\(E_{\mathrm{B}}\)’ = ?',r'بندشی توانائی ‘\(E_{\mathrm{B}}\)’ = ?',r'د تړون انرژي ‘\(E_{\mathrm{B}}\)’ = ?')
add('paragraph','Binding energy per nucleon ‘f’ = ?','فی نیوکلیون بندشی توانائی ‘f’ = ?','د هر نیوکلیون د تړون انرژي ‘f’ = ?')
add('heading','SOLUTION','حل','حل')
equation_intro(['(a) The mass defect is given by','(a) کمیتی نقص اس طرح دیا جاتا ہے','(a) د کتلې کسر داسې ورکول کېږي'],r'\Delta m=ZM_{\mathrm{p}}+NM_{\mathrm{N}}-M')
equation_intro(['Putting values','قدریں رکھنے سے','د ارزښتونو په اېښودلو'],r'\Delta m=11(1.007825\ \mathrm{u})+12(1.008665\ \mathrm{u})-22.989769\ \mathrm{u}')
equation_intro(['or','یا','یا'],r'\Delta m=11.086075\ \mathrm{u}+12.10398\ \mathrm{u}-22.989769\ \mathrm{u}')
answer_a=equation_intro(['therefore','لہٰذا','نو'],r'\Delta m=0.200286\ \mathrm{u}\quad\text{Answer}')
equation_intro(['(b) The Binding energy is given by','(b) بندشی توانائی اس طرح دی جاتی ہے','(b) د تړون انرژي داسې ورکول کېږي'],r'E_B=\Delta m\times c^2=\Delta m\times931.5\ \mathrm{MeV}')
equation_intro(['Putting values','قدریں رکھنے سے','د ارزښتونو په اېښودلو'],r'E_B=0.200286\times931.5\ \mathrm{MeV}')
answer_b=equation_intro(['therefore','لہٰذا','نو'],r'E_B=186.566\ \mathrm{MeV}\quad\text{Answer}')
# Translate the answer label separately from the shared mathematical notation.
for i in (answer_a,answer_b):T[i]=(T[i][0],T[i][1].replace(r'\text{Answer}',r'\text{جواب}'),T[i][2].replace(r'\text{Answer}',r'\text{ځواب}'))
TRACE=[(0,0),(2,1.1),(3,2.7),(7,5.4),(12,6.5),(20,7.6),(30,8.35),(40,8.65),(50,8.8),(62,8.9),(80,8.93),(100,8.9),(133,8.7),(160,8.5),(208,8.2),(222,8.13),(238,8.05)]
def binding_curve(lang):
    x=lambda a:98+a*2.85;y=lambda e:587-e*55
    b='<rect x="212" y="87" width="114" height="500" fill="#16a34a" opacity=".82"/>'
    for a in range(40,81,10):b+=f'<path d="M{x(a)} 87V587" stroke="#bef264" stroke-width="1"/>'
    for e in range(10):b+=f'<path d="M212 {y(e)}H326" stroke="#bef264" stroke-width="1"/>'
    b+=arrow(98,587,815,587,'#172033')+arrow(98,587,98,43,'#172033')
    for a in (0,50,100,150,200):b+=text(x(a),615,str(a),19)
    for e in range(1,10):b+=text(81,y(e)+6,str(e),19)
    b+='<path d="'+' '.join(('M' if i==0 else 'L')+f'{x(a):.2f} {y(e):.2f}' for i,(a,e) in enumerate(TRACE))+'" stroke="#b91c1c" stroke-width="3" fill="none"/>'
    for a,e in TRACE[1:]:b+=f'<circle cx="{x(a)}" cy="{y(e)}" r="3.3" fill="#111827"/>'
    # Labelled source points and leaders are retained, including its oxygen8/6 typo.
    points=[(2,1.1,(2,1,'H'),135,526),(3,2.7,(3,2,'He'),143,433),(4,7.1,(4,2,'He'),143,158),(16,7.7,(8,6,'O'),184,121),(58,8.86,(58,26,'Fe'),277,151),(62,8.9,(62,28,'Ni'),291,57),(133,8.7,(133,55,'Cs'),487,147),(208,8.2,(208,82,'Pb'),675,95),(222,8.13,(222,86,'Rn'),719,209),(238,8.05,(238,92,'U'),785,110)]
    for a,e,label,lx,ly in points:
        b+=f'<circle cx="{x(a)}" cy="{y(e)}" r="3" fill="#111827"/>'+isotope(lx,ly,*label)
        if a<20 or a==62:b+=f'<path d="M{lx-5} {ly+14}L{x(a)} {y(e)}" fill="none" stroke="#334155"/>'
    labels={'en':['Nucleon Number','Binding energy per nucleon (MeV)',['Region of','greater','stability']],'ur':['نیوکلیون عدد','فی نیوکلیون بندشی توانائی (MeV)',['زیادہ','استحکام کا','خطہ']],'ps':['د نیوکلیونونو شمېر','د هر نیوکلیون د تړون انرژي (MeV)',['د ډېرې','پایدارۍ','سیمه']]}[lang]
    b+=text(449,658,labels[0],23)+f'<g transform="translate(34 326) rotate(-90)">{text(0,0,labels[1],20)}</g>'
    for i,v in enumerate(labels[2]):b+=text(269,345+i*26,v,20)
    return svg(b,860,683,{'en':'Figure20.6: source-traced binding-energy curve with nucleon-number and MeV axes, green greater-stability region, and all ten nuclide labels. Curve coordinates are approximate geometric tracing of the printed graph, not a new numerical dataset.','ur':'شکل20.6: اصل سے اخذ کردہ بندشی توانائی کا منحنی، نیوکلیون عدد اور MeV کے محور، زیادہ استحکام کا سبز خطہ اور دس نیوکلائیڈ لیبل۔ منحنی کی نقاط اصل گراف کی تقریبی ہندسی نقل ہیں، نیا عددی ڈیٹا نہیں۔','ps':'شکل20.6: له اصل څخه رسم شوی د تړون انرژۍ منحني، د نیوکلیونونو او MeV محورونه، د ډېرې پایدارۍ شنه سیمه او د لسو نوکلایډونو نښې. مختصات د چاپ شوي ګراف تقریبي هندسي نقل دی، نوی عددي معلومات نه دي.'}[lang])
def ref(n):return {'pdfPage':177,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-binding-energy-curve-fission-and-sodium-example-342-343','title':'Binding-energy curve and sodium-23 mass-defect example','kind':'lesson','pdfPage':177,'printedPage':342,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
issues=['Figure20.6 oxygen label visibly prints mass8/atomic6, while the small-nuclei prose uses16O8. Both retained after close crop inspection.','Example20.1 gives proton mass1.007276u but substitutes1.007825u; all printed steps and results0.200286u/186.566MeV retained.']
issues.append('Figure20.6 includes densely overlapping, unlabelled points without numerical values. The labelled nuclides, axes and stability band are preserved; the curve is an approximate geometric trace. Individual unlabelled points have not been numerically recovered or certified.')
sec=section(record,T,L,('بندشی توانائی کا منحنی اور سوڈیم23 کے کمیتی نقص کی مثال','د تړون انرژۍ منحني او د سوډیم23 د کتلې د کسر بېلګه'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(342),ref(343)],sourceIssues=issues,sourceBlocks=[{'id':'phys20-177-binding-curve','type':'figure','sourceFigure':'20.6','traceGeometry':TRACE,'traceProvenance':'Approximate geometric reconstruction of source curve; source labels/axis ticks authoritative.','svg':binding_curve('en'),'svgUrdu':binding_curve('ur'),'svgPashto':binding_curve('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.4'],worked_examples=[{'id':'textbook-example-1','title':'EXAMPLE20.1 — SODIUM NUCLEUS','problem':T[problem][0],'sourceParts':[{'sectionId':record['id'],'indices':list(range(example_start,len(T)))}],'sourceReferences':[ref(343)],'sourceContinuationPending':178}])
    stage_reference(177,record,'Reinspected PDF177 printed342–343 and enlarged graph crop. Restored all intermediate/small/large-nucleus source paragraphs, full Example20.1 question/given/required and every solution step(a/b). Figure20.6 recreates source axes, scale, stability band, curve and all ten labels; original oxygen8/6 preserved. Proton-mass discrepancy retained. Worked example references full source steps and awaits part(c) on next PDF178; covered legacy20.4 retired.',issues)
    print('PDF177 graph/full example parts(a,b) staged; continue part(c) at178.')
