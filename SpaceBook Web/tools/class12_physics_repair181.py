"""PDF181 complete half-life derivation, graph and activity definition."""
from class12_source_review import upsert,section,shared_class_data_lock,sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text,arrow,svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps));return len(T)-1
def eq(s,num=None):
    v=r'\('+s+(r'\qquad('+str(num)+')' if num else '')+r'\)';return add('equation',v,v,v)
add('heading','20.8 HALF LIFE AND RATE OF DECAY','20.8 نصف عمر اور شرح زوال','20.8 نیم ژوند او د زوال کچه')
add('definition','The time it takes for half of the radioactive nuclei in a sample to decay is called half life.',
 'کسی نمونے کے نصف تابکار نیوکلئیسوں کے زوال میں لگنے والا وقت نصف عمر کہلاتا ہے۔',
 'هغه وخت چې د یوې نمونې نیمایي راډیواکټیفې هستې پکې زوال کوي، نیم ژوند بلل کېږي.')
add('paragraph','Individual disintegrations are random, however, the probability of decay for nuclei in a sample has fixed value, which is characteristic of that material.',
 'انفرادی ٹوٹ پھوٹ بے ترتیب ہوتی ہے، تاہم کسی نمونے میں نیوکلئیسوں کے زوال کے احتمال کی ایک مقررہ قدر ہوتی ہے، جو اس مادے کی خاصیت ہے۔',
 'انفرادي تجزیې تصادفي دي، خو په یوه نمونه کې د هستو د زوال احتمال ټاکلی ارزښت لري، چې د هماغه مادې ځانګړنه ده.')
add('paragraph',r'Thus the amount of radioactive isotope in the sample decrease with time as shown in the figure 20.12 for Half life curve. The number of nuclei present at time t = 0s is \(N=N_0\), and the number present at \(t=T_{1/2}\) is \(N=N_0/2\). The number present at \(t=2\ T_{1/2}\) is \(N=N_0/4\), and so on. For example, \({}^{14}\mathrm{C}\) has a half-life of 15730 years, because it takes this amount of time for one-half of a given quantity of this isotope to disintegrate. In another 15730-years, one-half of the remaining \({}^{14}\mathrm{C}\) atoms will have disintegrated, leaving only one-fourth of the original number intact.',
 r'اس طرح نمونے میں تابکار آئسوٹوپ کی مقدار وقت کے ساتھ کم ہوتی ہے، جیسا کہ شکل20.12 میں نصف عمر کے منحنی میں دکھایا گیا ہے۔ وقت t = 0s پر موجود نیوکلئیسوں کی تعداد \(N=N_0\)، اور \(t=T_{1/2}\) پر \(N=N_0/2\) ہے۔ \(t=2\ T_{1/2}\) پر تعداد \(N=N_0/4\) ہے، اور اسی طرح آگے۔ مثلاً \({}^{14}\mathrm{C}\) کی نصف عمر15730 سال ہے، کیونکہ اس آئسوٹوپ کی دی گئی مقدار کے نصف حصے کے ٹوٹنے میں اتنا وقت لگتا ہے۔ مزید15730 سال میں باقی \({}^{14}\mathrm{C}\) ایٹموں کا نصف ٹوٹ چکا ہوگا، اور اصل تعداد کا صرف ایک چوتھائی حصہ برقرار رہے گا۔',
 r'نو په نمونه کې د راډیواکټیف ایزوټوپ اندازه د وخت په تېرېدو کمېږي، لکه چې په20.12 شکل کې د نیم ژوند په منحني کې ښودل شوې ده. په t = 0s وخت کې د شته هستو شمېر \(N=N_0\)، او په \(t=T_{1/2}\) کې \(N=N_0/2\) دی. په \(t=2\ T_{1/2}\) کې شمېر \(N=N_0/4\) دی، او همداسې نور. د بېلګې په توګه، \({}^{14}\mathrm{C}\) د15730 کلونو نیم ژوند لري، ځکه د دې ایزوټوپ د ورکړل شوې اندازې د نیمایي تجزیه دومره وخت نیسي. په نورو15730 کلونو کې به د پاتې \({}^{14}\mathrm{C}\) اټومونو نیمایي تجزیه شوې وي او د اصلي شمېر یوازې څلورمه برخه به پاتې وي.')
add('definition','The rate of decay or activity of radioactive sample is defined as the number of disintegrations that occur per second.',
 'تابکار نمونے کی شرح زوال یا سرگرمی کی تعریف فی سیکنڈ ہونے والی ٹوٹ پھوٹ کی تعداد ہے۔',
 'د راډیواکټیفې نمونې د زوال کچه یا فعالیت په هره ثانیه کې د پېښېدونکو تجزیو شمېر تعریفېږي.')
add('paragraph',r'If ‘\(\Delta N\)’ is the number of radioactive nuclei that disintegrate in time ‘\(\Delta t\)’, then',
 r'اگر ‘\(\Delta N\)’ وقت ‘\(\Delta t\)’ میں ٹوٹنے والے تابکار نیوکلئیسوں کی تعداد ہو، تو',
 r'که ‘\(\Delta N\)’ په ‘\(\Delta t\)’ وخت کې د تجزیه کېدونکو راډیواکټیفو هستو شمېر وي، نو')
eq(r'\Delta N\propto-N',1)
add('equation',r'and     \(\Delta N\propto\Delta t\qquad(2)\)',r'اور     \(\Delta N\propto\Delta t\qquad(2)\)',r'او     \(\Delta N\propto\Delta t\qquad(2)\)')
add('paragraph','Combining equation 1 and equation 2, we get','مساوات1 اور مساوات2 کو ملانے سے حاصل ہوتا ہے','د1 او2 معادلو په یوځای کولو ترلاسه کوو')
eq(r'\Delta N\propto-N\Delta t')
add('equation',r'and     \(\Delta N=-\lambda N\Delta t\qquad(3)\)',r'اور     \(\Delta N=-\lambda N\Delta t\qquad(3)\)',r'او     \(\Delta N=-\lambda N\Delta t\qquad(3)\)')
add('paragraph',r'Where ‘\(\lambda\)’ is the proportionality constant called decay constant. The negative sign shows that N decreases with time, the above equation can also be written as',
 r'یہاں ‘\(\lambda\)’ تناسب کا مستقل ہے جسے زوال کا مستقل کہتے ہیں۔ منفی علامت ظاہر کرتی ہے کہ N وقت کے ساتھ کم ہوتا ہے؛ مذکورہ مساوات یوں بھی لکھی جا سکتی ہے',
 r'دلته ‘\(\lambda\)’ د تناسب ثابت دی چې د زوال ثابت بلل کېږي. منفي نښه ښيي چې N د وخت په تېرېدو کمېږي؛ پورتنۍ معادله داسې هم لیکل کېدای شي')
eq(r'\frac{\Delta N}{\Delta t}=-\lambda N',4)
add('heading','FIGURE 20.12','شکل20.12','شکل20.12')
L.append({'type':'visual','blockId':'phys20-181-half-life'})
add('paragraph','Half life curve','نصف عمر کا منحنی','د نیم ژوند منحني')
add('paragraph','We can show from equation 4 that the number of nuclei present varies with time according to the expression',
 'ہم مساوات4 سے دکھا سکتے ہیں کہ موجود نیوکلئیسوں کی تعداد وقت کے ساتھ اس اظہار کے مطابق بدلتی ہے',
 'موږ له4 معادلې ښودلی شو چې د شته هستو شمېر د وخت په تېرېدو له دې عبارت سره سم بدلېږي')
eq(r'N=N_0e^{-\lambda t}',5)
add('heading','For your information','آپ کی معلومات کے لیے','ستاسو د معلوماتو لپاره')
add('heading','CALCULUS FOR HALF LIFE CALCULATION','نصف عمر کے حساب کے لیے کیلکولس','د نیم ژوند د محاسبې لپاره کالکولس')
add('equation',r'For small change     \(\frac{\Delta N}{\Delta t}=\frac{dN}{dt}\)     so     \(\frac{dN}{dt}=-\lambda N\)     or     \(\frac{dN}{N}=-\lambda dt\)',
 r'چھوٹی تبدیلی کے لیے     \(\frac{\Delta N}{\Delta t}=\frac{dN}{dt}\)     لہٰذا     \(\frac{dN}{dt}=-\lambda N\)     یا     \(\frac{dN}{N}=-\lambda dt\)',
 r'د کوچني بدلون لپاره     \(\frac{\Delta N}{\Delta t}=\frac{dN}{dt}\)     نو     \(\frac{dN}{dt}=-\lambda N\)     یا     \(\frac{dN}{N}=-\lambda dt\)')
add('equation',r'Integrating both sides     \(\int\frac{dN}{N}=-\int\lambda\,dt\)     or     \(\ln N=-\lambda t+\text{constant}\)',
 r'دونوں طرف تکمل لینے سے     \(\int\frac{dN}{N}=-\int\lambda\,dt\)     یا     \(\ln N=-\lambda t+\text{مستقل}\)',
 r'د دواړو خواوو په انتګرال کولو     \(\int\frac{dN}{N}=-\int\lambda\,dt\)     یا     \(\ln N=-\lambda t+\text{ثابت}\)')
add('paragraph',r'Apply initial conditions, At t = 0, \(N=N_0\)',r'ابتدائی شرائط لگائیں، t = 0 پر، \(N=N_0\)',r'لومړني شرطونه وکاروئ، په t = 0 کې، \(N=N_0\)')
add('equation',r'\(\ln N_0=-\lambda(0)+\text{constant}\)',r'\(\ln N_0=-\lambda(0)+\text{مستقل}\)',r'\(\ln N_0=-\lambda(0)+\text{ثابت}\)')
add('equation',r'\(\text{constant}=\ln N_0\)',r'\(\text{مستقل}=\ln N_0\)',r'\(\text{ثابت}=\ln N_0\)')
add('equation',r'therefore     \(\ln N=-\lambda t+\ln N_0\)     or     \(\ln N=\ln e^{-\lambda t}+\ln N_0\)     or     \(\ln N=\ln N_0e^{-\lambda t}\)',
 r'لہٰذا     \(\ln N=-\lambda t+\ln N_0\)     یا     \(\ln N=\ln e^{-\lambda t}+\ln N_0\)     یا     \(\ln N=\ln N_0e^{-\lambda t}\)',
 r'نو     \(\ln N=-\lambda t+\ln N_0\)     یا     \(\ln N=\ln e^{-\lambda t}+\ln N_0\)     یا     \(\ln N=\ln N_0e^{-\lambda t}\)')
add('equation',r'Taking anti natural log on both sides     \(N=N_0e^{-\lambda t}\)',
 r'دونوں طرف طبیعی لاگ کا معکوس لینے سے     \(N=N_0e^{-\lambda t}\)',
 r'د دواړو خواوو د طبیعي لوګاریتم د معکوس په اخیستلو     \(N=N_0e^{-\lambda t}\)')
add('equation',r'For half life, At \(t=T_{1/2},\ N=N_0/2\)     \(\frac{N_0}{2}=N_0e^{-\lambda T_{1/2}}\)     or     \(\frac12=e^{-\lambda T_{1/2}}\)',
 r'نصف عمر کے لیے، \(t=T_{1/2},\ N=N_0/2\) پر     \(\frac{N_0}{2}=N_0e^{-\lambda T_{1/2}}\)     یا     \(\frac12=e^{-\lambda T_{1/2}}\)',
 r'د نیم ژوند لپاره، په \(t=T_{1/2},\ N=N_0/2\) کې     \(\frac{N_0}{2}=N_0e^{-\lambda T_{1/2}}\)     یا     \(\frac12=e^{-\lambda T_{1/2}}\)')
add('equation',r'Taking inverse     \(2=e^{\lambda T_{1/2}}\)     or     \(\ln2=\lambda T_{1/2}\)     or     \(T_{1/2}=\frac{\ln2}{\lambda}\)',
 r'معکوس لینے سے     \(2=e^{\lambda T_{1/2}}\)     یا     \(\ln2=\lambda T_{1/2}\)     یا     \(T_{1/2}=\frac{\ln2}{\lambda}\)',
 r'د معکوس په اخیستلو     \(2=e^{\lambda T_{1/2}}\)     یا     \(\ln2=\lambda T_{1/2}\)     یا     \(T_{1/2}=\frac{\ln2}{\lambda}\)')
add('paragraph','The numeric value of ln 2 = 0.693, therefore','ln 2 کی عددی قدر0.693 ہے، لہٰذا','د ln 2 عددي ارزښت0.693 دی، نو')
eq(r'T_{1/2}=\frac{0.693}{\lambda}','20.8')
add('paragraph',r'This is the relation between decay constant \(\lambda\) and half life \(T_{1/2}\). The value of half-life is constant for each radioactive element and it is possible to characterize the element by using its half-life value. The half-life is a measurement of stability of radioactive elements. The rate of radioactive decay is directly proportional to the stability of the isotope.',
 r'یہ زوال کے مستقل \(\lambda\) اور نصف عمر \(T_{1/2}\) کے درمیان تعلق ہے۔ ہر تابکار عنصر کے لیے نصف عمر کی قدر مستقل ہوتی ہے اور نصف عمر کی قدر استعمال کر کے عنصر کی شناخت ممکن ہے۔ نصف عمر تابکار عناصر کے استحکام کی پیمائش ہے۔ تابکار زوال کی شرح آئسوٹوپ کے استحکام کے براہ راست متناسب ہے۔',
 r'دا د زوال د ثابت \(\lambda\) او نیم ژوند \(T_{1/2}\) ترمنځ اړیکه ده. د هر راډیواکټیف عنصر د نیم ژوند ارزښت ثابت دی او د نیم ژوند په ارزښت سره د عنصر پېژندل ممکن دي. نیم ژوند د راډیواکټیفو عناصرو د پایدارۍ اندازه ده. د راډیواکټیف زوال کچه د ایزوټوپ له پایدارۍ سره مستقیم تناسب لري.')
add('heading','(i) ACTIVITY','(i) سرگرمی','(i) فعالیت')
add('definition','Activity, in radioactive-decay processes,is the number of disintegrations per unit time, or the number of unstable atomic nuclei that decay per unit time in a given sample. (i)',
 'تابکار زوال کے عمل میں سرگرمی فی اکائی وقت ٹوٹ پھوٹ کی تعداد، یا کسی دیے گئے نمونے میں فی اکائی وقت زوال کرنے والے غیر مستحکم ایٹمی نیوکلئیسوں کی تعداد ہے۔ (i)',
 'په راډیواکټیف زوال کې فعالیت د وخت په واحد کې د تجزیو شمېر، یا په یوې ورکړل شوې نمونه کې د وخت په واحد کې د زوال کوونکو ناپایدارو اټومي هستو شمېر دی. (i)')
def half_life(lang):
    x=lambda n:110+n*111;y=lambda v:515-v*4.35
    b=arrow(110,515,722,515,'#172033')+arrow(110,515,110,40,'#172033')
    for v in (0,6.25,12.5,25,50,100):b+=text(93,y(v)+5,str(v),17,'end')+f'<path d="M103 {y(v)}h14" stroke="#172033"/>'
    for n in range(1,6):
        xx=x(n);yy=y(100/2**n)
        b+=f'<path d="M110 {yy}H{xx}V515" fill="none" stroke="#475569" stroke-dasharray="4 7"/>'
        b+=text(xx,545,f'{n} T½',17)+f'<circle cx="{xx}" cy="{yy}" r="4" fill="white" stroke="#172033"/>'
    b+='<path d="'+' '.join(('M' if i==0 else 'L')+f'{x(i/30):.2f} {y(100/2**(i/30)):.2f}' for i in range(166))+'" fill="none" stroke="#b91c1c" stroke-width="3"/>'
    # Five equal samples encode the remaining fractions without a raster.
    for n in range(5):
        xx=x(n)+17;yy=y(100/2**n)-56;h=44/2**n
        b+=f'<rect x="{xx}" y="{yy}" width="41" height="44" fill="#e2f2bc"/><rect x="{xx}" y="{yy+44-h}" width="41" height="{h}" fill="#0f9f8f"/>'+text(xx+64,yy+24,'N₀' if n==0 else f'N₀/{2**n}',17)
    labels={'en':['Half Lives','Percentage of Sample'],'ur':['نصف عمریں','نمونے کا فی صد'],'ps':['نیم ژوندونه','د نمونې سلنه']}[lang]
    b+=text(416,590,labels[0],22)+f'<g transform="translate(31 295) rotate(-90)">{text(0,0,labels[1],21)}</g>'
    return svg(b,750,616,{'en':'Figure20.12 half-life curve: remaining sample100%,50%,25%,12.5%,6.25% at0,1,2,3,4 half-lives; decreasing exponential extends beyond5 half-lives. Five sample blocks mark N0,N0/2,N0/4,N0/8,N0/16.','ur':'شکل20.12 نصف عمر کا منحنی: صفر،1،2،3،4 نصف عمروں پر باقی نمونہ100،50،25،12.5،6.25 فی صد؛ گھٹتا ہوا قوت نما منحنی5 نصف عمروں سے آگے جاتا ہے۔ پانچ نمونے N0،N0/2،N0/4،N0/8،N0/16 دکھاتے ہیں۔','ps':'شکل20.12 د نیم ژوند منحني: په صفر،1،2،3،4 نیم ژوندونو کې پاتې نمونه100،50،25،12.5،6.25 سلنه ده؛ کمېدونکې نمایي منحني له5 نیم ژوندونو اوړي. پنځه نمونې N0،N0/2،N0/4،N0/8،N0/16 ښيي.'}[lang])
def ref(n):return {'pdfPage':181,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-half-life-decay-law-and-activity-350-351','title':'Half-life, complete decay derivation and activity','kind':'lesson','pdfPage':181,'printedPage':350,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
issues=['Printed350 gives carbon14 half-life15730 years twice, conflicting with5730 yr in the following Table20.4 and Assignment20.2. Both original values retained.','Printed351 says decay rate is directly proportional to isotope stability. Retained as source wording; it conflicts with the preceding half-life/decay-constant relation (longer half-life gives a lower decay constant).']
sec=section(record,T,L,('نصف عمر، زوال کا مکمل اخذ اور سرگرمی','نیم ژوند، د زوال بشپړ استنتاج او فعالیت'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceIssues=issues,sourceReferences=[ref(350),ref(351)],sourceBlocks=[{'id':'phys20-181-half-life','type':'figure','sourceFigure':'20.12','values':[{'halfLives':n,'remainingPercent':100/2**n} for n in range(6)],'svg':half_life('en'),'svgUrdu':half_life('ur'),'svgPashto':half_life('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.7','20.8'],formulas=[{'id':'phys20-half-life','name':'Half-life','number':'20.8','formula':'T½ = 0.693/λ','latex':r'T_{1/2}=\frac{0.693}{\lambda}','sourceClass12Physics':True,'sourceReferences':[ref(351)]}])
    stage_reference(181,record,'Reinspected complete PDF181 printed350–351. Restored every half-life/activity paragraph, both15730-year statements, local equations1–5, all calculus integration/initial-condition/logarithm steps, derivation of20.8, information-box headings and complete final activity definition. Figure20.12 recreated with structured exponential values, source axes/fractions/sample blocks and Urdu/Pashto labels. Covered legacy20.7/20.8 retired only after180–181 source restoration. Printed source conflicts retained and flagged.',issues)
    print('PDF181 full half-life source and coded graph staged.')
