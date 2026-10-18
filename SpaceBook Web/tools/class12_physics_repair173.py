"""PDF173 exact learning outcomes, nuclear composition and isotope definition."""
from class12_source_review import upsert,section,shared_class_data_lock,sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text,arrow,isotope,svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
def ref(n):return {'pdfPage':173,'printedPage':n,'sourcePdf':SOURCE}
add('heading','LEARNING OUTCOMES','حاصلاتِ تعلم','د زده کړې پایلې')
add('paragraph','identify the spontaneous and random nature of nuclear decay.','نیوکلیائی زوال کی خودبخود اور بے ترتیب نوعیت کی شناخت کریں۔','د هستوي زوال خپل سرې او تصادفي ځانګړنه وپېژني.')
add('paragraph',r'describe the term half life and solve problems using the equation \(\lambda=0.693/T_{1/2}\).',r'نصف عمر کی اصطلاح بیان کریں اور مساوات \(\lambda=0.693/T_{1/2}\) استعمال کر کے مسائل حل کریں۔',r'د نیم ژوند اصطلاح بیان کړي او د \(\lambda=0.693/T_{1/2}\) معادلې په کارولو مسئلې حل کړي.')
add('paragraph','determine the release of energy from different nuclear reactions.','مختلف نیوکلیائی تعاملات سے خارج ہونے والی توانائی معلوم کریں۔','له بېلابېلو هستوي تعاملونو څخه د انرژۍ خوشې کېدل معلوم کړي.')
add('paragraph','explain that atomic number and mass number conserve in nuclear reactions.','سمجھائیں کہ نیوکلیائی تعاملات میں ایٹمی عدد اور کمیتی عدد محفوظ رہتے ہیں۔','تشریح کړي چې په هستوي تعاملونو کې اټومي عدد او کتلیز عدد ساتل کېږي.')
add('paragraph','describe energy and mass conservation in simple reactions and in radioactive decay.','سادہ تعاملات اور تابکار زوال میں توانائی اور کمیت کی بقا بیان کریں۔','په ساده تعاملونو او راډیواکټیف زوال کې د انرژۍ او کتلې بقا بیان کړي.')
add('paragraph','describe the phenomena of nuclear fission and fusion.','نیوکلیائی انشقاق اور امتزاج کے مظاہر بیان کریں۔','د هستوي انشقاق او امتزاج پدیدې بیان کړي.')
add('paragraph','describe the fission chain reaction.','انشقاقی زنجیری تعامل بیان کریں۔','د انشقاق ځنځیري تعامل بیان کړي.')
add('paragraph','describe the function of various components of a nuclear reactor.','نیوکلیائی ری ایکٹر کے مختلف حصوں کے کام بیان کریں۔','د هستوي ریکټر د بېلابېلو برخو دندې بیان کړي.')
add('paragraph','describe the interaction of nuclear radiation with matter.','مادے کے ساتھ نیوکلیائی تابکاری کا تعامل بیان کریں۔','له مادې سره د هستوي وړانګو تعامل بیان کړي.')
add('paragraph','describe the use of Geiger Muller counter and solid state detectors to detect the radiations.','تابکاری کا کھوج لگانے کے لیے گائگر مولر شمارندے اور ٹھوس حالت کے کھوجیوں کا استعمال بیان کریں۔','د وړانګو د کشف لپاره د ګایګر مولر شمېرونکي او د جامد حالت کشفوونکو کارول بیان کړي.')
add('paragraph','describe the basic forces of nature.','فطرت کی بنیادی قوتیں بیان کریں۔','د طبیعت بنسټیزې قوې بیان کړي.')
add('paragraph','describe the key features and components of the standard model of matter including hadrons, leptons and quarks.','ہیڈرون، لیپٹون اور کوارک سمیت مادے کے معیاری نمونے کی اہم خصوصیات اور اجزا بیان کریں۔','د هاډرونونو، لیپټونونو او کوارکونو په ګډون د مادې د معیاري ماډل مهمې ځانګړنې او برخې بیان کړي.')
rout={'id':'phys20-learning-outcomes-nuclear-decay-reactions-detectors-standard-model-334','title':'Unit20 learning outcomes: decay, reactions, detectors and matter','kind':'lesson','pdfPage':173,'printedPage':334,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
sout=section(rout,T,L,('یونٹ20 حاصلاتِ تعلم: زوال، تعاملات، کھوجی اور مادہ','د20 واحد د زده کړې پایلې: زوال، تعاملونه، کشفوونکي او ماده'))
sout.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(334)],sourceBlocks=[])
T=[];L=[]
add('paragraph',r'An atom has a nucleus. The nucleus is positively charged. The overall dimensions of a nucleus are much smaller than those of an atom. The radius of a nucleus is \(10^{4}\) times smaller than the radius of an atom. This means the volume of a nucleus is about \(10^{12}\) times the smaller than volume of the atom. For an analogy, if an atom is enlarged to the size of a classroom, the nucleus would just be about the size of pinhead. In other words, an atom is almost empty, as (more than 99.9%) of the mass of an atom is concentrated at the nucleus.',
 r'ایٹم کا ایک نیوکلئیس ہوتا ہے۔ نیوکلئیس مثبت بار رکھتا ہے۔ نیوکلئیس کے مجموعی ابعاد ایٹم کے ابعاد سے بہت چھوٹے ہوتے ہیں۔ نیوکلئیس کا رداس ایٹم کے رداس سے \(10^{4}\) گنا چھوٹا ہے۔ اس کا مطلب ہے کہ نیوکلئیس کا حجم ایٹم کے حجم سے تقریباً \(10^{12}\) گنا چھوٹا ہے۔ مثال کے طور پر، اگر ایٹم کو بڑھا کر جماعت کے کمرے جتنا کر دیا جائے تو نیوکلئیس تقریباً سوئی کے سرے جتنا ہوگا۔ دوسرے لفظوں میں ایٹم تقریباً خالی ہے، کیونکہ ایٹم کی کمیت کا (99.9% سے زیادہ) حصہ نیوکلئیس میں مرتکز ہوتا ہے۔',
 r'یو اټوم هسته لري. هسته مثبت چارج لري. د هستې ټولیز ابعاد د اټوم تر ابعادو ډېر کوچني دي. د هستې شعاع د اټوم تر شعاع \(10^{4}\) ځله کوچنۍ ده. دا معنا لري چې د هستې حجم د اټوم تر حجم شاوخوا \(10^{12}\) ځله کوچنی دی. د تشبیه لپاره، که اټوم د یوه ټولګي د خونې په اندازه لوی شي، هسته به یې یوازې د سنجاق د سر هومره وي. په بل عبارت، اټوم نږدې تش دی، ځکه د اټوم د کتلې (له99.9% څخه زیاته) برخه په هسته کې راټوله ده.')
add('paragraph','Does the nucleus have a structure, just like atoms? Yes there are many similarities between atomic structure and nuclear structure, which makes our study of the properties of the nucleus easier.',
 'کیا ایٹموں کی طرح نیوکلئیس کی بھی ساخت ہوتی ہے؟ جی ہاں، ایٹمی اور نیوکلیائی ساخت میں بہت سی مماثلتیں ہیں، جن سے نیوکلئیس کی خصوصیات کا ہمارا مطالعہ آسان ہو جاتا ہے۔',
 'آیا هسته هم د اټومونو په څېر جوړښت لري؟ هو، د اټومي او هستوي جوړښت ترمنځ ډېر ورته والي شته چې د هستې د ځانګړنو مطالعه راته اسانه کوي.')
add('heading','20.1 COMPOSITION OF ATOMIC NUCLEI','20.1 ایٹمی نیوکلئیسوں کی ترکیب','20.1 د اټومي هستو ترکیب')
add('paragraph',r'In an atom the atomic nucleus is several thousand times more massive than the electrons and occupies only a tiny fraction of the atom’s volume (about 1 part in \(10^{12}\) or less). The nucleus is a bound collection of protons and neutrons. Together, protons and neutrons are referred to as nucleons (particles found inside the nucleus).',
 r'ایٹم میں ایٹمی نیوکلئیس الیکٹرانوں سے کئی ہزار گنا زیادہ کمیت رکھتا ہے اور ایٹم کے حجم کے صرف بہت چھوٹے حصے (تقریباً \(10^{12}\) میں1 حصہ یا اس سے کم) کو گھیرتا ہے۔ نیوکلئیس پروٹونوں اور نیوٹرونوں کا بندھا ہوا مجموعہ ہے۔ پروٹون اور نیوٹرون کو مجموعی طور پر نیوکلیون (نیوکلئیس کے اندر پائے جانے والے ذرات) کہا جاتا ہے۔',
 r'په اټوم کې اټومي هسته تر الکترونونو څو زره ځله زیاته کتله لري او د اټوم د حجم یوازې یوه ډېره کوچنۍ برخه نیسي (په \(10^{12}\) کې شاوخوا1 برخه یا کمه). هسته د پروتونونو او نیوټرونونو تړلې مجموعه ده. پروتونونه او نیوټرونونه په ګډه نیوکلیونونه (په هسته کې موندل کېدونکې ذرې) بلل کېږي.')
add('heading','FIGURE 20.1','شکل20.1','شکل20.1')
L.append({'type':'visual','blockId':'phys20-173-composition'})
add('paragraph','Composition of atomic nucleus','ایٹمی نیوکلئیس کی ترکیب','د اټومي هستې ترکیب')
add('paragraph','In describing the atomic nucleus, we use the following quantities','ایٹمی نیوکلئیس کو بیان کرنے کے لیے ہم درج ذیل مقداریں استعمال کرتے ہیں','د اټومي هستې په بیانولو کې موږ لاندې کمیتونه کاروو')
add('paragraph','• The atomic number ‘Z’ (sometimes called the charge number), which is the number of protons in the nucleus.','• ایٹمی عدد ‘Z’ (جسے کبھی بار کا عدد کہتے ہیں)، جو نیوکلئیس میں پروٹونوں کی تعداد ہے۔','• اټومي عدد ‘Z’ (چې کله ناکله د چارج عدد بلل کېږي)، په هسته کې د پروتونونو شمېر دی.')
add('paragraph','• The neutron number ‘N’ which is the number of neutrons in the nucleus.','• نیوٹرون عدد ‘N’، جو نیوکلئیس میں نیوٹرونوں کی تعداد ہے۔','• د نیوټرون عدد ‘N’، په هسته کې د نیوټرونونو شمېر دی.')
add('paragraph','• The mass number ‘A’ which is the number of nucleons in the nucleus (A = Z + N).','• کمیتی عدد ‘A’، جو نیوکلئیس میں نیوکلیونوں کی تعداد ہے (A = Z + N)۔','• کتلیز عدد ‘A’، په هسته کې د نیوکلیونونو شمېر دی (A = Z + N).')
add('paragraph',r'In representing nuclei, it is convenient to have a system of symbols to show how many protons and neutrons are present. The symbol used is \({}^{A}_{Z}\mathrm{X}\), where X represents the chemical symbol for the element, Z represents the number of protons and A represents the number of nucleons (i.e number of protons and neutrons) as shown in figure 20.2.',
 r'نیوکلئیسوں کی نمائندگی میں علامات کا ایسا نظام سہولت دیتا ہے جو موجود پروٹونوں اور نیوٹرونوں کی تعداد ظاہر کرے۔ استعمال ہونے والی علامت \({}^{A}_{Z}\mathrm{X}\) ہے، جہاں X عنصر کی کیمیائی علامت، Z پروٹونوں کی تعداد اور A نیوکلیونوں کی تعداد (یعنی پروٹونوں اور نیوٹرونوں کی تعداد) ظاہر کرتا ہے، جیسا کہ شکل20.2 میں دکھایا گیا ہے۔',
 r'د هستو د ښودلو لپاره د نښو داسې سیستم ګټور دی چې د موجودو پروتونونو او نیوټرونونو شمېر وښيي. کارېدونکې نښه \({}^{A}_{Z}\mathrm{X}\) ده؛ X د عنصر کیمیاوي نښه، Z د پروتونونو شمېر او A د نیوکلیونونو شمېر (یعنې د پروتونونو او نیوټرونونو شمېر) ښيي، لکه په20.2 شکل کې چې ښودل شوي دي.')
add('paragraph',r'Because the atomic number can also be obtained through the element symbol, therefore we state only the mass number in the superscript and leave out the atomic number subscript, for example \({}^{12}\mathrm{C}\), \({}^{24}\mathrm{Mg}\) and \({}^{35}\mathrm{Cl}\).',
 r'چونکہ عنصر کی علامت سے ایٹمی عدد بھی حاصل کیا جا سکتا ہے، اس لیے ہم صرف کمیتی عدد کو اوپری اشاریے میں لکھتے ہیں اور ایٹمی عدد کا زیریں اشاریہ چھوڑ دیتے ہیں، مثلاً \({}^{12}\mathrm{C}\)، \({}^{24}\mathrm{Mg}\) اور \({}^{35}\mathrm{Cl}\)۔',
 r'ځکه چې د عنصر له نښې څخه اټومي عدد هم ترلاسه کېدای شي، نو موږ یوازې کتلیز عدد د پاسني شاخص په توګه لیکو او د اټومي عدد لاندې شاخص پرېږدو؛ د بېلګې په توګه \({}^{12}\mathrm{C}\)، \({}^{24}\mathrm{Mg}\) او \({}^{35}\mathrm{Cl}\).')
add('heading','FIGURE 20.2','شکل20.2','شکل20.2')
L.append({'type':'visual','blockId':'phys20-173-notation'})
add('paragraph','Symbolic representation of magnesium','میگنیشیم کی علامتی نمائندگی','د مګنیزیم سمبولیک ښودنه')
add('heading','20.2 ISOTOPES','20.2 آئسوٹوپس','20.2 ایزوټوپونه')
add('definition','The atoms of an element having the same number of protons, or the same atomic number, but having different numbers of neutrons, or different atomic weights is called an isotope.',
 'کسی عنصر کے وہ ایٹم جن میں پروٹونوں کی تعداد یا ایٹمی عدد یکساں ہو، لیکن نیوٹرونوں کی تعداد یا ایٹمی اوزان مختلف ہوں، آئسوٹوپ کہلاتے ہیں۔',
 'د یوه عنصر هغه اټومونه چې د پروتونونو شمېر یا اټومي عدد یې یو شان وي، خو د نیوټرونونو شمېر یا اټومي وزنونه یې بېل وي، ایزوټوپ بلل کېږي.')
def composition(lang):
    labels={'en':['Volume occupied by electron(s)','Nucleus','proton','neutron','Approximately'],'ur':['الیکٹرانوں کا گھیرا ہوا حجم','نیوکلئیس','پروٹون','نیوٹرون','تقریباً'],'ps':['د الکترونونو نیول شوی حجم','هسته','پروتون','نیوټرون','نږدې']}[lang]
    b='<defs><radialGradient id="p173-atom-'+lang+'"><stop stop-color="#f9a8d4"/><stop offset="1" stop-color="#fdf2f8"/></radialGradient></defs>'
    b+=f'<circle cx="125" cy="147" r="72" fill="url(#p173-atom-{lang})"/><circle cx="125" cy="147" r="8" fill="#64748b" stroke="#172033"/><circle cx="448" cy="152" r="82" fill="#312e81"/>'
    for x,y,color in [(429,125,'#a5f3fc'),(466,128,'#cbd5e1'),(412,160,'#cbd5e1'),(454,155,'#94a3b8'),(482,164,'#a5f3fc'),(451,193,'#a5f3fc')]:b+=f'<circle cx="{x}" cy="{y}" r="22" fill="{color}" stroke="#e2e8f0" stroke-width="2"/>'
    b+='<circle cx="735" cy="159" r="60" fill="#7dd3fc" stroke="#0284c7"/>'
    b+='<path d="M133 162Q264 292 384 208M512 171Q610 227 677 181" fill="none" stroke="#172033" stroke-width="3"/>'+arrow(360,218,384,208,'#172033')+arrow(651,191,677,181,'#172033')
    b+='<g stroke="#334155" fill="none"><path d="M121 68V92M80 196L117 153M292 97L425 123M297 160L397 162"/></g>'
    b+=text(152,42,labels[0],17)+text(69,220,labels[1],17)+text(285,84,labels[2],18)+text(293,151,labels[3],18)+text(735,165,labels[2],19)
    for x1,x2,y,exp in [(55,196,258,'⁻¹⁰'),(368,528,272,'⁻¹⁴'),(676,797,282,'⁻¹⁵')]:
        b+=arrow((x1+x2)/2,y,x1,y,'#172033')+arrow((x1+x2)/2,y,x2,y,'#172033')+text((x1+x2)/2,y+35,labels[4]+' 10'+exp+' m',17)
    return svg(b,860,337,{'en':'Figure20.1: electron-occupied atom volume approximately10^-10m, magnified nucleus approximately10^-14m with proton/neutron labels, and magnified proton approximately10^-15m.','ur':'شکل20.1: الیکٹرانوں والا ایٹمی حجم تقریباً10⁻¹⁰m، بڑا دکھایا ہوا نیوکلئیس تقریباً10⁻¹⁴m جس پر پروٹون اور نیوٹرون کے لیبل ہیں، اور بڑا دکھایا ہوا پروٹون تقریباً10⁻¹⁵m۔','ps':'شکل20.1: د الکترونونو نیول شوی اټومي حجم نږدې10⁻¹⁰m، لویه ښودل شوې هسته نږدې10⁻¹⁴m د پروتون او نیوټرون له نښو سره، او لوی ښودل شوی پروتون نږدې10⁻¹⁵m.'}[lang])
def notation(lang):
    w={'en':['Number of nucleons','Symbol for','element','Number of protons or electrons'],'ur':['نیوکلیونوں کی تعداد','عنصر کی','علامت','پروٹونوں یا الیکٹرانوں کی تعداد'],'ps':['د نیوکلیونونو شمېر','د عنصر','نښه','د پروتونونو یا الکترونونو شمېر']}[lang]
    b=text(181,48,w[0],20)+text(134,113,'A',24)+text(159,144,'X',40)+text(134,169,'Z',24)+text(267,125,w[1],19)+text(267,153,w[2],19)+text(223,220,w[3],19)+isotope(504,143,24,12,'Mg')
    return svg(b,610,248,{'en':'Figure20.2: A is number of nucleons, X element symbol, Z number of protons or electrons; example magnesium24 with atomic number12.','ur':'شکل20.2: A نیوکلیونوں کی تعداد، X عنصر کی علامت، Z پروٹونوں یا الیکٹرانوں کی تعداد؛ مثال میگنیشیم24 جس کا ایٹمی عدد12 ہے۔','ps':'شکل20.2: A د نیوکلیونونو شمېر، X د عنصر نښه، Z د پروتونونو یا الکترونونو شمېر؛ بېلګه مګنیزیم24 چې اټومي عدد یې12 دی.'}[lang])
record={'id':'phys20-nuclear-composition-nuclide-notation-isotopes-334-335','title':'Nuclear size, composition, nuclide notation and isotopes','kind':'lesson','pdfPage':173,'printedPage':334,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
sec=section(record,T,L,('نیوکلیائی جسامت، ترکیب، علامت اور آئسوٹوپس','د هستې اندازه، ترکیب، هستوي نښې او ایزوټوپونه'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(334),ref(335)],sourceBlocks=[{'id':'phys20-173-composition','type':'figure','sourceFigure':'20.1','svg':composition('en'),'svgUrdu':composition('ur'),'svgPashto':composition('ps')},{'id':'phys20-173-notation','type':'figure','sourceFigure':'20.2','svg':notation('en'),'svgUrdu':notation('ur'),'svgPashto':notation('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([rout,record],[sout,sec],chapter_index=9)
        sync_companions(chapter_index=9,formulas=[{'id':'phys20-mass-number-sum','name':'Nuclear mass-number relation','formula':'A = Z + N','latex':'A=Z+N','sourceClass12Physics':True,'sourceReferences':[ref(335)]},{'id':'phys20-nuclide-symbol','name':'Nuclide notation','formula':'ᴬZX','latex':r'{}^{A}_{Z}\mathrm{X}','sourceClass12Physics':True,'sourceReferences':[ref(335)]}])
    stage_reference(173,record,'Reinspected PDF173 printed334–335. Full12 learning outcomes preserved in their stable separate record; full nucleus-size analogy, atomic structure comparison, composition, three definitions, two notation paragraphs and isotope definition restored. Figures20.1/20.2 retain all labels, size scales, magnification relationships and magnesium example; full Urdu/Pashto translations. Both records included in saved source comparison.',additional_records=[rout])
    print('PDF173 full outcomes, prose and two figures staged.')
