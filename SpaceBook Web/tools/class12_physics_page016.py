from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
from class12_physics_field_figures import arrow
SHEET=[
 (r'Consider an infinite plane sheet of charge with surface charge density \(\sigma\). Let \(S_1\) be the point at a distance \(r\) from the sheet and \(E\) be the electric field at this point. Gaussian surface is in the form of a cylinder of cross-sectional area \(A\) perpendicular to the sheet of charge as shown in Fig11.16. By symmetry, the electric field is at right angles to the end caps and away from the plane. Its magnitude is the same at points \(S_1\) and \(S_2\).',r'سطحی بار کی کثافت \(\sigma\) والی ایک لامحدود ہموار بار دار چادر پر غور کریں۔ \(S_1\) چادر سے \(r\) فاصلے پر ایک نقطہ اور \(E\) اس نقطے پر برقی میدان ہو۔ گاؤسی سطح، عرضی رقبے \(A\) کے بیلن کی صورت میں ہے جو بار دار چادر کے عمود پر ہے، جیسا کہ شکل 11.16 میں ہے۔ تقارن کی بنا پر برقی میدان سروں کی سطحوں کے عمود پر اور چادر سے باہر کی طرف ہے۔ اس کی مقدار نقاط \(S_1\) اور \(S_2\) پر یکساں ہے۔',r'د \(\sigma\) سطحي چارج کثافت لرونکې نامحدودې هوارې چارج شوې پاڼې ته پام وکړئ. \(S_1\) دې له پاڼې څخه په \(r\) واټن کې نقطه او \(E\) دې په هغې نقطه کې برېښنايي میدان وي. ګاوسي سطحه د \(A\) عرضي مساحت لرونکي سلنډر په بڼه ده چې د چارج شوې پاڼې په عمود کې دی، لکه په شکل 11.16 کې. د تقارن له مخې برېښنايي میدان د سلنډر د پای سطحو په عمود کې او له پاڼې څخه بهر خوا ته دی. مقدار یې په \(S_1\) او \(S_2\) نقطو کې برابر دی.'),
 (r'The charge enclosed by the surface will be \(\sigma A\). Since we know by Gauss’s law',r'سطح کے اندر محصور بار \(\sigma A\) ہو گا۔ چونکہ گاؤس کے قانون سے ہم جانتے ہیں',r'په سطحه کې محصور چارج به \(\sigma A\) وي. څرنګه چې د ګاوس له قانون څخه پوهېږو'),
 (r'Total electric flux \(=\frac1{\varepsilon_0}\times(Q)\)',r'کل برقی بہاؤ \(=\frac1{\varepsilon_0}\times(Q)\)',r'ټول برېښنايي فلکس \(=\frac1{\varepsilon_0}\times(Q)\)'),
 (r'\(Q=\) charge enclosed by the surface',r'\(Q=\) سطح کے اندر محصور بار',r'\(Q=\) په سطحه کې محصور چارج'),
 (r'\(\Phi_E=\frac1{\varepsilon_0}\times(Q)\)',)*3,
 (r'Since \(\delta=Q/A\) or, \(\delta A=Q\)',r'چونکہ \(\delta=Q/A\) یا، \(\delta A=Q\)',r'ځکه چې \(\delta=Q/A\) یا، \(\delta A=Q\)'),
 (r'\(\Phi_E=\frac{\delta A}{\varepsilon_0}\) ...(11.14)',)*3,
 ('The direction of E is perpendicular to face containing A and parallel to the curved surface.','E کی سمت، A والی سطح کے عمود پر اور خمیدہ سطح کے متوازی ہے۔','د E لوری د A لرونکې سطحې په عمود کې او له کږې سطحې سره موازي دی.'),
 ('The electric flux through the end faces is EΔA, while flux through the curved surface is zero. Thus','سروں کی سطحوں سے برقی بہاؤ EΔA ہے، جبکہ خمیدہ سطح سے بہاؤ صفر ہے۔ پس','د پای سطحو له لارې برېښنايي فلکس EΔA دی، خو د کږې سطحې له لارې فلکس صفر دی. نو'),
 (r'\(\Phi_E=\vec E\cdot\Delta\vec A+\vec E\cdot\Delta\vec A+0\)',)*3,
 (r'Hence, \(2EA=\frac{\delta A}{\varepsilon_0}\)',r'لہٰذا، \(2EA=\frac{\delta A}{\varepsilon_0}\)',r'له همدې امله، \(2EA=\frac{\delta A}{\varepsilon_0}\)'),
 (r'or \(E=\frac\delta{2\varepsilon_0}\) ...(11.15)',r'یا \(E=\frac\delta{2\varepsilon_0}\) ...(11.15)',r'یا \(E=\frac\delta{2\varepsilon_0}\) ...(11.15)'),
 (r'and \(\vec E=\frac\delta{2\varepsilon_0}\hat r\) ...(11.16)',r'اور \(\vec E=\frac\delta{2\varepsilon_0}\hat r\) ...(11.16)',r'او \(\vec E=\frac\delta{2\varepsilon_0}\hat r\) ...(11.16)'),
 (r'Where \(\hat r\) is the unit vector normal to the sheet and directed away from it.',r'جہاں \(\hat r\)، چادر کے عمود پر اور اس سے باہر کی طرف اکائی سمتیہ ہے۔',r'دلته \(\hat r\) د پاڼې په عمود کې او له هغې څخه بهر لوري ته واحد ویکټور دی.'),
 (r'[Editorial clarification: the source first uses \(\sigma\) for surface charge density, then prints \(\delta\) in the subsequent equations. Both source symbols are retained.]',r'[ادارتی وضاحت: کتاب پہلے سطحی بار کی کثافت کے لیے \(\sigma\) اور بعد کی مساوات میں \(\delta\) چھاپتی ہے۔ دونوں اصل علامتیں محفوظ ہیں۔]',r'[د سمونوال وضاحت: کتاب لومړی د سطحي چارج کثافت لپاره \(\sigma\) کاروي، بیا په ورپسې معادلو کې \(\delta\) چاپوي. دواړه اصلي نښې ساتل شوي دي.]'),
]
INFO=[
 ('FOR YOUR INFORMATION','آپ کی معلومات کے لیے','ستاسو د معلوماتو لپاره'),
 ('Airlines Airbus A380 flew through a storm when 500 peoples were on the board but none of them were injured. As there is no electric field, no potential difference inside a metal shell, so one of the safest way to be inside a metal shell during thunderstorm.','ایئرلائنز کا ایئربس A380 ایک طوفان سے گزرا جب اس میں 500 افراد سوار تھے، لیکن ان میں سے کوئی زخمی نہیں ہوا۔ چونکہ دھاتی خول کے اندر نہ برقی میدان ہوتا ہے اور نہ فرقِ برق، اس لیے گرج چمک کے طوفان میں دھاتی خول کے اندر ہونا محفوظ ترین طریقوں میں سے ایک ہے۔','د هوايي شرکتونو ایربس A380 له یوه توپان څخه تېر شو چې 500 کسان پکې سپاره وو، خو هېڅ یو ټپي نه شو. څرنګه چې د فلزي پوښ په دننه کې نه برېښنايي میدان او نه د پوتانشیل توپیر شته، نو د تندر او برېښنا په توپان کې د فلزي پوښ په دننه کې پاتې کېدل له تر ټولو خوندي لارو څخه دي.'),
]
PLATES=[
 (r'Consider two oppositely charged parallel metal plates. The charge densities of these metal plates are \(+\sigma\) and \(-\sigma\).',r'دو مخالف بار والی متوازی دھاتی پلیٹوں پر غور کریں۔ ان کی بار کی کثافتیں \(+\sigma\) اور \(-\sigma\) ہیں۔',r'دوو مخالف چارج لرونکو موازي فلزي تختو ته پام وکړئ. د دې فلزي تختو د چارج کثافتونه \(+\sigma\) او \(-\sigma\) دي.'),
 (r'These plates are assumed to be of infinite length in order to avoid fringing field at end. Under these conditions, the field intensity will be uniform and normal to the plates. In order to find the electric field intensity \(E\), at point P between the plates consider a Gaussian surface in the form of a box of cross sectional area A with its upper surface lies within the plate as shown in figure (11.17).',r'کناروں پر میدان کے پھیلاؤ سے بچنے کے لیے ان پلیٹوں کی لمبائی لامحدود فرض کی جاتی ہے۔ ان حالات میں میدان کی شدت یکساں اور پلیٹوں کے عمود پر ہو گی۔ پلیٹوں کے درمیان نقطہ P پر برقی میدان کی شدت \(E\) معلوم کرنے کے لیے عرضی رقبے A کے ڈبے کی صورت میں گاؤسی سطح پر غور کریں، جس کی اوپری سطح پلیٹ کے اندر واقع ہو، جیسا کہ شکل (11.17) میں ہے۔',r'په پای کې د میدان د څنډیز خپرېدو د مخنیوي لپاره د دې تختو اوږدوالی نامحدود فرض کېږي. په دې شرایطو کې به د میدان شدت یوشان او د تختو په عمود کې وي. د تختو ترمنځ په P نقطه کې د برېښنايي میدان د شدت \(E\) د موندلو لپاره د A عرضي مساحت لرونکي بکس په بڼه ګاوسي سطحې ته پام وکړئ چې پورتنۍ سطحه یې د تختې دننه پرته ده، لکه په شکل (11.17) کې.'),
 ('[Editorial clarification: the source numbers both this section and the preceding infinite-sheet section 11.5.1.3. The repeated printed numbering is retained.]','[ادارتی وضاحت: کتاب اس حصے اور پچھلے لامحدود چادر والے حصے دونوں کو 11.5.1.3 نمبر دیتی ہے۔ اصل دہرایا گیا نمبر محفوظ ہے۔]','[د سمونوال وضاحت: کتاب دې برخې او مخکینۍ نامحدودې پاڼې برخې دواړو ته 11.5.1.3 شمېره ورکوي. تکرار شوې چاپي شمېره ساتل شوې ده.]'),
]

def sheet(lang):
    body='<path d="M35 153H137V207H35Z" fill="#e11d48"/><ellipse cx="35" cy="180" rx="10" ry="27" fill="#e11d48"/><path d="M125 52L273 12V305L125 345Z" fill="#fff" stroke="#334155"/>'
    for x in range(141,270,25):
        for y in range(64,300,35):body+=f'<text x="{x}" y="{y-(x-141)*.25}">+</text>'
    body+='<path d="M195 153H288V207H195Z" fill="#f43f5e" stroke="#be123c"/><ellipse cx="195" cy="180" rx="10" ry="27" fill="#fb7185"/><ellipse cx="288" cy="180" rx="10" ry="27" fill="#fb7185"/><path d="M35 180H5M44 147V105M261 75H314" stroke="#334155" stroke-width="2"/>'+arrow(5,180,-1,0,'#334155')+arrow(44,105,0,-1,'#334155')+arrow(314,75,1,0,'#334155')+'<text x="4" y="164">n̂</text><text x="44" y="98">n̂</text><text x="16" y="138">A</text><text x="305" y="63">E⃗</text><text x="294" y="212">S₁</text><text x="20" y="230">S₂</text>'
    cap={'en':'FIGURE 11.16: Gaussian surface in the form of a cylinder perpendicular to the sheet of charge.','ur':'شکل 11.16: بار دار چادر کے عمود پر بیلن کی صورت میں گاؤسی سطح۔','ps':'شکل 11.16: د چارج شوې پاڼې په عمود کې د سلنډر په بڼه ګاوسي سطحه.'}[lang]
    return '<figure>'+svg(body,340,360,'Positively charged sheet crossed by Gaussian cylinder, end caps S1 and S2, outward normal and field')+'<figcaption>'+cap+'</figcaption></figure>'

def plates(lang):
    body='<rect x="20" y="35" width="400" height="22" fill="#fff" stroke="#334155"/><rect x="20" y="204" width="400" height="22" fill="#fff" stroke="#334155"/>'
    for x in range(45,414,28):
        body+=f'<text x="{x}" y="53">+</text><text x="{x}" y="220">−</text><path d="M{x} 57V204" stroke="#991b1b" stroke-width="2"/>'+arrow(x,145,0,1,'#991b1b')
    body+='<path d="M171 49H223V105H171Z M171 49L195 18H247L223 49 M223 105L247 75V18 M171 105H223" fill="#38bdf8" fill-opacity=".3" stroke="#334155"/><path d="M171 49V105M195 18V75L171 105M195 75H247" fill="none" stroke="#334155"/><text x="149" y="84">C</text><text x="252" y="83">B</text><text x="206" y="127">P</text>'
    cap={'en':'FIGURE 11.17: Gaussian surface in the form of a cubical box between the plates','ur':'شکل 11.17: پلیٹوں کے درمیان مکعب ڈبے کی صورت میں گاؤسی سطح','ps':'شکل 11.17: د تختو ترمنځ د مکعبي بکس په بڼه ګاوسي سطحه'}[lang]
    return '<figure>'+svg(body,450,245,'Oppositely charged parallel plates, downward uniform field, Gaussian box faces B and C, point P')+'<figcaption>'+cap+'</figcaption></figure>'

def aircraft(lang):
    body='<rect width="440" height="240" fill="#334155"/><path d="M15 25L135 40 182 94 230 20 319 31 352 90M230 20L216 60 254 100 239 150M352 90L325 114 358 175" fill="none" stroke="#fef08a" stroke-width="3"/><g transform="rotate(-12 220 150)"><path d="M50 149Q108 126 331 140L383 151Q365 165 86 166Z" fill="#f1f5f9" stroke="#111827"/><path d="M195 144L257 86H285L249 149M182 158L266 205H302L237 159M93 146L69 106H95L134 146" fill="#cbd5e1" stroke="#111827"/><path d="M120 142H319M120 151H319" stroke="#64748b" stroke-dasharray="3 4"/><circle cx="232" cy="179" r="10" fill="#94a3b8" stroke="#111827"/><circle cx="262" cy="129" r="10" fill="#94a3b8" stroke="#111827"/></g>'
    return '<figure>'+svg(body,440,240,'Coded schematic airliner in a lightning storm illustrating the source metal-shell discussion')+'</figure>'

if __name__=='__main__':
    specs=[
      ('phys12-front-sheet22','11.5.1.3 ELECTRIC FIELD INTENSITY DUE TO AN INFINITE SHEET OF CHARGE',22,SHEET[:8],[{'type':'paragraph' if i in [0,1,3,7] else 'equation','indices':[i]} for i in range(8)]+[{'type':'visual','blockId':'sheet'}],('11.5.1.3 لامحدود بار دار چادر کی وجہ سے برقی میدان کی شدت','11.5.1.3 د نامحدودې چارج شوې پاڼې له امله د برېښنايي میدان شدت'),{'sheet':sheet}),
      ('phys12-front-aircraft22','FOR YOUR INFORMATION',22,INFO,[{'type':'heading','indices':[0]},{'type':'visual','blockId':'aircraft'},{'type':'paragraph','indices':[1]}],('آپ کی معلومات کے لیے','ستاسو د معلوماتو لپاره'),{'aircraft':aircraft}),
      ('phys12-front-sheet23','Infinite sheet — field derivation (continued)',23,SHEET[8:],[{'type':'paragraph' if i in [0,5,6] else 'equation','indices':[i]} for i in range(7)],('لامحدود چادر — میدان کا اخذ (جاری)','نامحدوده پاڼه — د میدان استنتاج (دوام)'),{}),
      ('phys12-front-plates23','11.5.1.3 ELECTRIC FIELD INTENSITY BETWEEN TWO OPPOSITELY CHARGED PARALLEL PLATES.',23,PLATES,[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual','blockId':'plates'},{'type':'paragraph','indices':[2]}],('11.5.1.3 دو مخالف بار والی متوازی پلیٹوں کے درمیان برقی میدان کی شدت۔','11.5.1.3 د دوو مخالف چارج لرونکو موازي تختو ترمنځ د برېښنايي میدان شدت.'),{'plates':plates}),
    ]
    records=[];sections=[]
    for identity,title,page,pairs,layout,titles,visuals in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':16,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        revised['sourceBlocks']=[{'id':key,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')} for key,fn in visuals.items()]
        revised['content']+=''.join(fn('en') for fn in visuals.values())
        for para in revised['paras']:
            if para['text'].startswith('[Editorial'):para.update(isEditorial=True,originalText=None)
        records.append(record);sections.append(revised)
    upsert(records,sections)
    formulas=[]
    for num,index,latex in [('11.14',6,r'\Phi_E=\frac{\delta A}{\varepsilon_0}'),('11.15',11,r'E=\frac\delta{2\varepsilon_0}'),('11.16',12,r'\vec E=\frac\delta{2\varepsilon_0}\hat r')]:
        formulas.append({'id':'phys12-eq-'+num,'name':'Infinite sheet of charge','number':num,'formula':SHEET[index][0],'latex':latex,'note':'Textbook uses delta here; preceding definition uses sigma.','sourceReferences':[{'pdfPage':16,'printedPage':22 if num=='11.14' else 23}]})
    sync_companions(formulas=formulas,retire_sections=['11.7'],trim_sections=[{'id':'11.8','startsAt':'Therefore by Gauss','title':'Parallel plates (continued; source review starts at PDF page 17)','clearSciNote':True}])
    checkpoint(16,'corrected_verified',[r['id'] for r in records],
      'Original spread inspected at2.5x. Infinite-sheet setup, full Eq11.14–11.16 derivation, Airbus metal-shell information box and full parallel-plate introduction preserved with source grammar and paragraph boundaries and aligned translations. Delta versus sigma inconsistency and repeated11.5.1.3 numbering retained and editorial notes separately paired. Native SVG recreates cylinder/sheet Fig11.16, Gaussian box/plates Fig11.17 and storm/airliner schematic. Covered legacy11.7 retired and11.8 prefix trimmed to PDF17 continuation; duplicate sciNote cleared.',printed_pages=[22,23])
