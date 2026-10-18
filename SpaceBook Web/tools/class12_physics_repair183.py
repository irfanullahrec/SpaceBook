"""Full PDF183 radiation interactions and Geiger–Muller apparatus."""
from class12_source_review import upsert, section, shared_class_data_lock
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, arrow, svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
add('heading','20.9 INTERACTION OF RADIATION WITH MATTER','20.9 مادے کے ساتھ تابکاری کا تعامل','20.9 له مادې سره د وړانګو تعامل')
add('paragraph','Interaction of ionizing radiation with matter is divided into three groups.','مادے کے ساتھ آئن ساز تابکاری کے تعامل کو تین گروہوں میں تقسیم کیا جاتا ہے۔','له مادې سره د آیون جوړوونکو وړانګو تعامل په دریو ډلو وېشل کېږي.')
add('heading','A. INTERACTION OF CHARGED PARTICLES','A. باردار ذرات کا تعامل','A. د چارج لرونکو ذرو تعامل')
add('paragraph',r'Charged particles (electrons (e-), positrons (e+), protons (P), deuterons (d), alphas (\(\alpha\)), heavy ions (A > 4)) traveling through matter lose energy in the following ways:',
 r'مادے میں سفر کرنے والے باردار ذرات (الیکٹران (e-)، پوزیٹران (e+)، پروٹون (P)، ڈیوٹران (d)، الفا (\(\alpha\))، بھاری آئن (A > 4)) درج ذیل طریقوں سے توانائی کھوتے ہیں:',
 r'په ماده کې تېرېدونکې چارج لرونکې ذرې (الکترونونه (e-)، پوزیترونونه (e+)، پروتونونه (P)، ډیوټرونونه (d)، الفا (\(\alpha\))، درانه آیونونه (A > 4)) په لاندې لارو انرژي له لاسه ورکوي:')
add('paragraph','1. In Coulomb interactions with electrons and nuclei','1. الیکٹرانوں اور نیوکلئیسوں کے ساتھ کولمبی تعاملات میں','1. له الکترونونو او هستو سره په کولمبي تعاملونو کې')
add('paragraph','2. By emission of- electromagnetic radiation (bremsstrahlung)','2. برقی مقناطیسی تابکاری (بریمز شٹراہلنگ) کے اخراج سے','2. د برېښنا مقناطیسي وړانګو (برېمس شټرالونګ) په خپرېدو سره')
add('paragraph','3. In nuclear interactions','3. نیوکلیائی تعاملات میں','3. په هستوي تعاملونو کې')
add('heading','B. INTERACTION OF PHOTONS','B. فوٹونوں کا تعامل','B. د فوټونونو تعامل')
add('paragraph',r'There is a long list of possible interactions of photons (gammas (\(\gamma\)) or X-rays), but only the three most important ones are:',
 r'فوٹونوں (گاما (\(\gamma\)) یا ایکس ریز) کے ممکنہ تعاملات کی ایک طویل فہرست ہے، لیکن ان میں صرف تین سب سے اہم یہ ہیں:',
 r'د فوټونونو (ګاما (\(\gamma\)) یا اېکس وړانګو) د ممکنه تعاملونو اوږد لېست شته، خو درې تر ټولو مهم یې دا دي:')
add('paragraph','1. The photoelectric effect','1. ضیائی برقی اثر','1. فوتوالکتریک اغېز')
add('paragraph','2. Compton scattering, and','2. کامپٹن بکھراؤ، اور','2. کامپټن خپرېدنه، او')
add('paragraph','3. Pair production.','3. جوڑے کی پیدائش۔','3. د جوړې تولید.')
add('heading','C. INTERACTION OF NEUTRONS','C. نیوٹرونوں کا تعامل','C. د نیوټرونونو تعامل')
add('paragraph','Since a neutron (n) has no charge, it interacts with nuclei only through nuclear forces. When it approaches a nucleus, it does not have to go through a Coulomb barrier. As a result, the probability (cross section) for nuclear interactions is higher for neutrons than for charged particles. The interactions of neutrons with nuclei are divided into two categories:',
 'چونکہ نیوٹرون (n) پر کوئی بار نہیں ہوتا، اس لیے وہ نیوکلئیسوں کے ساتھ صرف نیوکلیائی قوتوں کے ذریعے تعامل کرتا ہے۔ نیوکلئیس کے قریب آنے پر اسے کولمبی رکاوٹ سے نہیں گزرنا پڑتا۔ نتیجتاً نیوکلیائی تعاملات کا احتمال (عرضی رقبہ) نیوٹرونوں کے لیے باردار ذرات سے زیادہ ہوتا ہے۔ نیوکلئیسوں کے ساتھ نیوٹرونوں کے تعاملات کو دو اقسام میں تقسیم کیا جاتا ہے:',
 'ځکه چې نیوټرون (n) چارج نه لري، له هستو سره یوازې د هستوي قوې له لارې تعامل کوي. کله چې هستې ته نږدې شي، له کولمبي خنډ څخه تېرېدو ته اړتیا نه لري. په پایله کې د هستوي تعاملونو احتمال (عرضي مقطع) د نیوټرونونو لپاره تر چارج لرونکو ذرو زیات دی. له هستو سره د نیوټرونونو تعاملونه په دوو ډولونو وېشل کېږي:')
add('paragraph','1. scattering and','1. بکھراؤ اور','1. خپرېدنه او')
add('paragraph','2. absorption','2. جذب','2. جذب')
add('heading','20.10 RADIATION DETECTORS','20.10 تابکاری کے کھوجی','20.10 د وړانګو کشفوونکي')
add('paragraph','Nuclear radiations are measured with the effect they produce when interacting with matter. The function of the detector is to produce a signal for every particle or photon entering into it. Every detector works by using some interaction of particles with matter. There are many types of radiation detectors, however we would study only two in detail.',
 'نیوکلیائی تابکاری کی پیمائش اس اثر سے کی جاتی ہے جو وہ مادے کے ساتھ تعامل کے دوران پیدا کرتی ہے۔ کھوجی کا کام اس میں داخل ہونے والے ہر ذرے یا فوٹون کے لیے ایک اشارہ پیدا کرنا ہے۔ ہر کھوجی مادے کے ساتھ ذرات کے کسی تعامل کو استعمال کر کے کام کرتا ہے۔ تابکاری کے کھوجیوں کی بہت سی اقسام ہیں، تاہم ہم صرف دو کا تفصیلی مطالعہ کریں گے۔',
 'هستوي وړانګې د هغه اغېز له مخې اندازه کېږي چې له مادې سره د تعامل پر مهال یې پیدا کوي. د کشفوونکي دنده دا ده چې د هرې ورننوتونکې ذرې یا فوټون لپاره یوه اشاره تولید کړي. هر کشفوونکی له مادې سره د ذرو له یوه تعامل څخه په ګټه اخیستو کار کوي. د وړانګو د کشفوونکو ډېر ډولونه شته، خو موږ به یوازې دوه په تفصیل وڅېړو.')
add('paragraph','1. Geiger-Muller counters','1. گائگر مولر شمارندے','1. ګایګر مولر شمېرونکي')
add('paragraph','2. Semiconductor detectors','2. نیم موصل کھوجی','2. نیمه هادي کشفوونکي')
add('heading','A. GEIGER-MULLER COUNTERS','A. گائگر مولر شمارندے','A. ګایګر مولر شمېرونکي')
add('paragraph','It is the most widely used device to detect radiation. It consist of cylindrical metal tube filled with gas at low temperature and long wire along the axis of the tube. The wire is maintained at high positive potential with respect to tube. The metal tube is attached with detection system such as counter and audio device as shown in the figure.',
 'تابکاری کا کھوج لگانے کے لیے یہ سب سے زیادہ استعمال ہونے والا آلہ ہے۔ یہ کم درجۂ حرارت پر گیس سے بھری ہوئی بیلن نما دھاتی نلی اور نلی کے محور کے ساتھ ایک لمبی تار پر مشتمل ہوتا ہے۔ تار کو نلی کی نسبت بلند مثبت پوٹینشل پر رکھا جاتا ہے۔ دھاتی نلی کو شمارندے اور صوتی آلے جیسے کھوجی نظام سے جوڑا جاتا ہے، جیسا کہ شکل میں دکھایا گیا ہے۔',
 'دا د وړانګو د کشف لپاره تر ټولو ډېر کارېدونکی وسیله ده. دا له یوه سلنډري فلزي نل څخه جوړ دی چې په ټیټه تودوخه کې له ګاز څخه ډک دی، او یوه اوږده سیم یې د محور په اوږدو کې پرته ده. سیم د نل په نسبت په لوړ مثبت پوتنسیال کې ساتل کېږي. فلزي نل د شمېرونکي او غږیزې وسیلې په څېر د کشف له سیستم سره نښلول شوی وي، لکه په شکل کې چې ښودل شوي دي.')
add('heading','FIGURE 20.13','شکل20.13','شکل20.13')
L.append({'type':'visual','blockId':'phys20-183-geiger-counter'})
add('paragraph','When high energy particle or photon enters the tube trough the thin window at one end some of the atoms of the gas ionizes as shown in figure 20.13. Since the wire is at positive potential the electrons removed from atoms are attracted towards the wire.',
 'جب زیادہ توانائی کا ذرہ یا فوٹون ایک سرے پر موجود باریک کھڑکی سے نلی میں داخل ہوتا ہے تو گیس کے کچھ ایٹم آئن بن جاتے ہیں، جیسا کہ شکل20.13 میں دکھایا گیا ہے۔ چونکہ تار مثبت پوٹینشل پر ہے، اس لیے ایٹموں سے نکلے ہوئے الیکٹران تار کی طرف کھنچتے ہیں۔',
 'کله چې د لوړې انرژۍ ذره یا فوټون د یوه سر له نرۍ کړکۍ څخه نل ته ننوځي، د ګاز ځینې اټومونه آیون کېږي، لکه په20.13 شکل کې چې ښودل شوي دي. ځکه چې سیم مثبت پوتنسیال لري، له اټومونو ایستل شوي الکترونونه سیم ته راکاږل کېږي.')
L.append({'type':'visual','blockId':'phys20-183-portable-counter'})
WORDS={
 'en':[['Gas molecules are','ionized by radiation'],['Electrode positively','charged'],['Metal tube','negatively charged'],['Non-ionized gas','molecules'],['Ionizing','radiation'],['Window'],['Counter and','audio device']],
 'ur':[['تابکاری سے گیس کے','سالمے آئن بنتے ہیں'],['مثبت بار والا','الیکٹروڈ'],['منفی بار والی','دھاتی نلی'],['گیس کے غیر آئن شدہ','سالمے'],['آئن ساز','تابکاری'],['کھڑکی'],['شمارندہ اور','صوتی آلہ']],
 'ps':[['وړانګې د ګاز','مالیکولونه آیون کوي'],['مثبت چارج لرونکی','الکترود'],['منفي چارج لرونکی','فلزي نل'],['د ګاز ناآیون شوي','مالیکولونه'],['آیون جوړوونکې','وړانګې'],['کړکۍ'],['شمېرونکی او','غږیزه وسیله']]}
def lines(x,y,values):return ''.join(text(x,y+23*i,v,17) for i,v in enumerate(values))
def counter(lang):
    w=WORDS[lang];b='<path d="M190 170H590Q630 245 590 320H190Z" fill="#a5f3fc" stroke="#0369a1" stroke-width="4"/><ellipse cx="190" cy="245" rx="25" ry="75" fill="#e2e8f0" stroke="#475569" stroke-width="3"/>'
    for y in range(185,310,10):b+=f'<path d="M170 {y}H210" stroke="#64748b" stroke-width="1"/>'
    b+='<path d="M225 245H640Q690 245 685 325Q670 393 729 363L781 331" fill="none" stroke="#1e293b" stroke-width="6"/><path d="M237 245H591" stroke="#b45309" stroke-width="7"/>'
    for x,y in [(290,194),(350,300),(408,182),(445,309),(519,188),(551,299),(582,214)]:
        b+=f'<circle cx="{x}" cy="{y}" r="7" fill="#fb7185" stroke="#9f1239"/><circle cx="{x+7}" cy="{y-4}" r="3" fill="#38bdf8"/>'
    for x,y in [(257,221),(316,281),(386,205)]:
        b+=f'<circle cx="{x}" cy="{y}" r="8" fill="#fb7185" stroke="#9f1239"/>'+text(x,y+5,'+',14)
        b+=f'<circle cx="{x+20}" cy="{y-12}" r="5" fill="#38bdf8"/>'+arrow(x+23,y-10,x+37,244,'#0369a1')
    b+='<path d="M60 299Q70 320 80 294T100 288T120 282T140 272L188 245" stroke="#15803d" fill="none" stroke-width="3"/>'
    b+='<rect x="745" y="171" width="158" height="188" rx="9" fill="#0284c7" stroke="#0f172a" stroke-width="4"/><path d="M764 236A61 52 0 0 1 882 236Z" fill="#f8fafc" stroke="#334155" stroke-width="3"/><path d="M823 235L854 207" stroke="#0f172a" stroke-width="4"/><circle cx="822" cy="301" r="35" fill="#0f172a"/><path d="M785 302H860M792 286H852M792 318H852" stroke="#475569" stroke-width="3"/>'
    b+='<g fill="none" stroke="#475569" stroke-width="1.5"><path d="M216 83L260 213M216 83L315 276M470 77L480 245M87 163L171 187M481 383L519 188M481 383L551 299M94 373L129 279M218 386L192 294M825 116V171"/></g>'
    for pos,i in [((186,37),0),((487,35),1),((91,117),2),((490,411),3),((83,413),4),((223,415),5),((819,78),6)]:b+=lines(*pos,w[i])
    return svg(b,930,478,{'en':'Figure20.13: radiation enters the window of the negative metal tube, ionizes gas, and releases electrons attracted to the positive axial electrode; cable leads to the counter and audio device.','ur':'شکل20.13: تابکاری منفی دھاتی نلی کی کھڑکی سے داخل ہو کر گیس کو آئن بناتی ہے؛ آزاد الیکٹران مثبت محوری الیکٹروڈ کی طرف جاتے ہیں۔ تار شمارندے اور صوتی آلے سے جڑی ہے۔','ps':'شکل20.13: وړانګې د منفي فلزي نل له کړکۍ ننوځي او ګاز آیون کوي؛ ازاد الکترونونه مثبت محوري الکترود ته ځي. کېبل له شمېرونکي او غږیزې وسیلې سره نښتی دی.'}[lang])
def portable(lang):
    b='<path d="M140 68L329 42L363 239L172 270Z" fill="#1e293b" stroke="#0f172a" stroke-width="4"/><path d="M173 95L296 76L309 134L185 153Z" fill="#e2e8f0" stroke="#64748b"/><path d="M218 132L239 94" stroke="#0f172a" stroke-width="3"/><circle cx="244" cy="200" r="33" fill="#0f172a"/><path d="M219 167L250 81Q250 27 278 25Q308 22 320 61" fill="none" stroke="#111827" stroke-width="12"/><path d="M180 261C60 332 32 196 93 167" fill="none" stroke="#0f172a" stroke-width="5"/><path d="M57 90L113 99L100 227L44 218Z" fill="#94a3b8" stroke="#334155" stroke-width="4"/><ellipse cx="73" cy="220" rx="28" ry="10" fill="#cbd5e1" stroke="#334155"/><path d="M48 30L49 111Q57 128 67 119L74 98Q85 136 99 118L114 95L110 43Z" fill="#d6a38a" stroke="#854d3c" stroke-width="2"/>'
    return svg(b,410,315,{'en':'Coded schematic of the uncaptioned source photograph: hand-held cylindrical probe connected by a cable to a portable radiation counter with carrying handle.','ur':'بغیر عنوان اصل تصویر کا کوڈ شدہ خاکہ: ہاتھ میں پکڑا ہوا بیلن نما پروب کیبل سے دستے والے قابلِ حمل تابکاری شمارندے سے جڑا ہے۔','ps':'د بې سرلیک اصلي انځور کوډ شوې طرحه: په لاس کې نیول شوی سلنډري پروب د کېبل په وسیله له لاستي لرونکي ګرځنده وړانګو شمېرونکي سره نښتی دی.'}[lang])
record={'id':'phys20-radiation-interactions-and-geiger-counter-354-355','title':'Radiation interactions and Geiger-Muller counters','kind':'lesson','pdfPage':183,'printedPage':354,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
sec=section(record,T,L,('تابکاری کے تعاملات اور گائگر مولر شمارندے','د وړانګو تعاملونه او ګایګر مولر شمېرونکي'))
issues=['The source describes gas in a Geiger-Muller tube as being at “low temperature”. This wording is retained; the earlier silent substitution “low pressure” has been removed.']
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[{'pdfPage':183,'printedPage':n,'sourcePdf':SOURCE} for n in (354,355)],sourceIssues=issues,sourceBlocks=[{'id':'phys20-183-geiger-counter','type':'figure','sourceFigure':'20.13','svg':counter('en'),'svgUrdu':counter('ur'),'svgPashto':counter('ps')},{'id':'phys20-183-portable-counter','type':'figure','representation':'Code schematic of uncaptioned source photograph','svg':portable('en'),'svgUrdu':portable('ur'),'svgPashto':portable('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():upsert([record],[sec],chapter_index=9)
    stage_reference(183,record,'Visually reinspected PDF183 printed354–355. Full three interaction subsections, all lists, detector introduction and Geiger-Muller prose preserved, including low temperature and trough source wording. Figure20.13 includes all seven labels, negative metal tube/window, positive axial wire, ionized/non-ionized gas, electron collection and connected counter/audio device. Uncaptioned portable detector photograph recreated as a coded schematic. Urdu/Pashto aligned translations and all figure labels provided.',issues)
    print('PDF183 full source and figures staged.')
