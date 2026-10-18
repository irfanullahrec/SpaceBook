from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
from class12_physics_field_figures import arrow
FIELD=[
 ('Therefore by Gauss’s Law electric flux is','لہٰذا گاؤس کے قانون سے برقی بہاؤ یہ ہے','له همدې امله د ګاوس له قانون څخه برېښنايي فلکس دا دی'),
 (r'\(\sum\vec E\cdot\Delta\vec A=\frac Q{\varepsilon_0}\)',)*3,
 ('As the box sides are parallel to electric field E so the flux through sides will be zero, while the electric field intensity E is normal to the lower surface of Gaussian box.','چونکہ ڈبے کے اطراف برقی میدان E کے متوازی ہیں، اس لیے اطراف سے بہاؤ صفر ہو گا، جبکہ برقی میدان کی شدت E، گاؤسی ڈبے کی نچلی سطح کے عمود پر ہے۔','څرنګه چې د بکس اړخونه له برېښنايي میدان E سره موازي دي، نو د اړخونو له لارې فلکس صفر دی، خو د برېښنايي میدان شدت E د ګاوسي بکس د لاندې سطحې په عمود کې دی.'),
 (r'Net electric flux \(=\Phi_E\)',r'خالص برقی بہاؤ \(=\Phi_E\)',r'خالص برېښنايي فلکس \(=\Phi_E\)'),
 (r'Electric flux through the side B + electric flux through the side C + electric flux through the lower surface \(=\delta A/\varepsilon_0\)',r'طرف B سے برقی بہاؤ + طرف C سے برقی بہاؤ + نچلی سطح سے برقی بہاؤ \(=\delta A/\varepsilon_0\)',r'د B اړخ له لارې برېښنايي فلکس + د C اړخ له لارې برېښنايي فلکس + د لاندې سطحې له لارې برېښنايي فلکس \(=\delta A/\varepsilon_0\)'),
 (r'\(\vec E\cdot\Delta\vec A+\vec E\cdot\Delta\vec A+\vec E\cdot\Delta\vec A=\frac{\sigma A}{\varepsilon_0}\)',)*3,
 (r'\(0+0+\vec E\vec A=\frac{\sigma A}{\varepsilon_0}\)',)*3,
 (r'\(E=\frac\sigma{\varepsilon_0}\) ...(11.17)',)*3,
 (r'and in vector form \(\vec E=\frac\sigma{\varepsilon_0}\hat r\)',r'اور سمتی صورت میں \(\vec E=\frac\sigma{\varepsilon_0}\hat r\)',r'او په ویکټوري بڼه \(\vec E=\frac\sigma{\varepsilon_0}\hat r\)'),
 ('This gives the electric field between oppositely charged parallel plates. We see that the resulting electric field between the plates is uniform, perpendicular to the plates, and independent of the distance from the plates.','یہ مخالف بار والی متوازی پلیٹوں کے درمیان برقی میدان دیتا ہے۔ ہم دیکھتے ہیں کہ پلیٹوں کے درمیان حاصل ہونے والا برقی میدان یکساں، پلیٹوں کے عمود پر اور پلیٹوں سے فاصلے سے آزاد ہے۔','دا د مخالف چارج لرونکو موازي تختو ترمنځ برېښنايي میدان ورکوي. وینو چې د تختو ترمنځ پایله شوی برېښنايي میدان یوشان، د تختو په عمود کې او له تختو څخه له واټن څخه خپلواک دی.'),
 (r'[Editorial clarification: this page prints \(\delta A\) in the prose flux sum and \(\sigma A\) in the following equations. The line \(0+0+\vec E\vec A\) has no printed dot between the vectors. These source forms are retained.]',r'[ادارتی وضاحت: اس صفحے کی نثری بہاؤ کی جمع میں \(\delta A\) اور اگلی مساوات میں \(\sigma A\) چھپا ہے۔ \(0+0+\vec E\vec A\) کی سطر میں سمتیوں کے درمیان نقطہ نہیں چھپا۔ اصل صورتیں محفوظ ہیں۔]',r'[د سمونوال وضاحت: دې پاڼې د فلکس په نثري جمع کې \(\delta A\) او په ورپسې معادلو کې \(\sigma A\) چاپ کړي دي. په \(0+0+\vec E\vec A\) کرښه کې د ویکټورونو ترمنځ ټکی نه دی چاپ شوی. اصلي بڼې ساتل شوې دي.]'),
]
TIP=[
 ('TIP','اشارہ','لارښوونه'),
 ('The electric flux through arbitrary Gaussian surface can be calculated as','کسی بھی گاؤسی سطح سے برقی بہاؤ اس طرح معلوم کیا جا سکتا ہے','د هرې ګاوسي سطحې له لارې برېښنايي فلکس داسې محاسبه کېدای شي'),
 (r'\(\Phi_E=\frac{-4\mu\mathrm C+2\mu\mathrm C+5\mu\mathrm C}{\varepsilon_0}=\frac{3\times10^{-6}\,\mathrm C}{8.85\times10^{-12}\,\mathrm{C^2\,N^{-1}\,m^{-2}}}\)',)*3,
 (r'\(=3.4\times10^5\,\mathrm{N\,m^2\,C^{-1}}\)',)*3,
]
PROJECT=[
 ('Calculate the electric flux through each Gaussian surface shown in Figure','شکل میں دکھائی گئی ہر گاؤسی سطح سے برقی بہاؤ معلوم کریں','په شکل کې د ښودل شوې هرې ګاوسي سطحې له لارې برېښنايي فلکس محاسبه کړئ'),
 ('[Editorial clarification: in the project diagram some charge-marker signs disagree with their adjacent signed labels: the +6 μC labels beside minus markers and the −2 μC label beside a plus marker. Both the markers and printed labels are retained; no answer is supplied in this source box.]','[ادارتی وضاحت: منصوبے کی شکل میں بعض بار کے نشانات اپنی ساتھ لکھی ہوئی علامت دار مقداروں سے مختلف ہیں: منفی نشانوں کے ساتھ +6 μC اور مثبت نشان کے ساتھ −2 μC لکھا ہے۔ نشان اور اصل مقداریں دونوں محفوظ ہیں؛ اس اصل خانے میں جواب نہیں دیا گیا۔]','[د سمونوال وضاحت: د پروژې په شکل کې د ځینو چارج نښو علامتونه له څنګ ته لیکل شوو علامت لرونکو مقدارونو سره توپیر لري: د منفي نښو ترڅنګ +6 μC او د مثبتې نښې ترڅنګ −2 μC لیکل شوي دي. نښې او چاپ شوي مقدارونه دواړه ساتل شوي؛ په دې اصلي چوکاټ کې ځواب نه دی ورکړل شوی.]'),
]
POTENTIAL=[
 (r'Previously we studied the electric field due to two parallel plates with a space between them. To explain electric potential consider two oppositely charged parallel plates as shown in Fig (11.18 a). If a positive charge \(+q_0\) is placed in between these plates and allowed to move freely in an electric field it will move towards the negative plate, pulled by the electric force and will gain an equivalent amount of kinetic energy.',r'پہلے ہم نے دو متوازی پلیٹوں کی وجہ سے برقی میدان پڑھا، جن کے درمیان فاصلہ ہے۔ برقی پوٹینشل کی وضاحت کے لیے دو مخالف بار والی متوازی پلیٹوں پر غور کریں، جیسا کہ شکل (11.18 a) میں ہے۔ اگر مثبت بار \(+q_0\) ان پلیٹوں کے درمیان رکھا جائے اور اسے برقی میدان میں آزادانہ حرکت کرنے دی جائے، تو برقی قوت اسے کھینچ کر منفی پلیٹ کی طرف لے جائے گی اور اسے مساوی مقدار میں حرکی توانائی حاصل ہو گی۔',r'مخکې مو د دوو موازي تختو له امله برېښنايي میدان ولوست چې ترمنځ یې تشه ده. د برېښنايي پوتانشیل د تشریح لپاره دوو مخالف چارج لرونکو موازي تختو ته پام وکړئ، لکه په شکل (11.18 a) کې. که مثبت چارج \(+q_0\) د دې تختو ترمنځ کېښودل شي او په برېښنايي میدان کې ازاد حرکت ته پرېښودل شي، نو برېښنايي قوه به یې منفي تختې ته کش کړي او د هغې په اندازه به حرکي انرژي ترلاسه کړي.'),
]

def charge(x,y,label,sign):
    return f'<circle cx="{x}" cy="{y}" r="9" fill="'+('#0284c7' if sign=='+' else '#e11d48')+f'"/><text x="{x-5}" y="{y+5}" fill="#fff">{sign}</text><text x="{x+14}" y="{y+5}">{label} μC</text>'

def tip(lang):
    body='<path d="M100 40Q178 2 219 54T194 161L157 237Q115 242 86 183T100 40Z" fill="#fef08a"/>'
    for x,y,q,sign in [(126,69,'−4','−'),(171,115,'+2','+'),(126,170,'+5','+'),(253,40,'+3','+'),(40,218,'−4','−')]:body+=charge(x,y,q,sign)
    return '<figure>'+svg(body,335,260,'Gaussian surface encloses minus4 plus2 plus5 microcoulombs; plus3 and minus4 outside excluded')+'</figure>'

def project(lang):
    body='<path d="M15 40H170V160H15Z M15 40L25 24H160L170 40" fill="#6ee7b7" stroke="#334155"/><circle cx="252" cy="102" r="62" fill="#6ee7b7" stroke="#334155"/><ellipse cx="388" cy="112" rx="56" ry="84" transform="rotate(30 388 112)" fill="#fef08a"/><ellipse cx="558" cy="119" rx="63" ry="35" transform="rotate(-38 558 119)" fill="#e11d48"/>'
    points=[(37,64,'+4','+'),(92,86,'−2','−'),(50,133,'−2','−'),(70,197,'+2',None),(235,78,'+3','+'),(245,134,'−3','−'),(250,13,'+6','−'),(229,188,'+2','+'),(397,19,'+4','+'),(381,64,'−3','−'),(353,115,'+2','+'),(333,149,'−5','−'),(317,195,'−4','−'),(550,103,'−1','−'),(514,143,'+4','+'),(570,54,'−2','+'),(545,185,'+6','−')]
    for x,y,q,sign in points:body+=charge(x,y,q,sign) if sign else f'<text x="{x}" y="{y}">{q} μC</text>'
    return '<figure>'+svg(body,650,220,'Four project Gaussian surfaces with original signed labels and charge markers; outside charges distinguished')+'</figure>'

def potential(lang):
    body=''
    for i in range(2):
        x=30+i*230
        body+=f'<rect x="{x}" y="20" width="18" height="205" fill="#fef08a" stroke="#334155"/><rect x="{x+130}" y="20" width="18" height="205" fill="#fb7185" stroke="#334155"/>'
        for y in range(32,226,28):body+=f'<text x="{x+2}" y="{y}">+</text><text x="{x+134}" y="{y}">−</text><path d="M{x+20} {y-7}H{x+130}" stroke="#991b1b"/>'+arrow(x+75,y-7,1,0,'#334155')
        body+=f'<circle cx="{x+34}" cy="177" r="3"/><circle cx="{x+114}" cy="177" r="3"/><path d="M{x+34} 170H{x+114}" stroke="#334155" stroke-dasharray="2 3"/>'+arrow(x+114,170,1,0,'#334155')+f'<text x="{x+20}" y="196">A</text><text x="{x+111}" y="196">B</text><text x="{x+62}" y="163">'+('q₀' if i==0 else 'q')+f'</text><text x="{x+68}" y="252">{chr(97+i)}</text>'
    cap={'en':'FIGURE 11.18: Potential difference between point A &amp; B in electric field.','ur':'شکل 11.18: برقی میدان میں نقاط A اور B کے درمیان فرقِ برق۔','ps':'شکل 11.18: په برېښنايي میدان کې د A او B نقطو ترمنځ د پوتانشیل توپیر.'}[lang]
    return '<figure>'+svg(body,455,270,'Two oppositely charged plate panels a and b; field rightward, points A and B and charges q0 and q')+'<figcaption>'+cap+'</figcaption></figure>'

if __name__=='__main__':
    specs=[('phys12-front-plates24','Parallel plates — field derivation',24,FIELD,[{'type':'equation' if i in [1,3,5,6,7,8] else 'paragraph','indices':[i]} for i in range(len(FIELD))],('متوازی پلیٹیں — میدان کا اخذ','موازي تختې — د میدان استنتاج'),{}),('phys12-front-flux-tip24','TIP — Gaussian-surface flux',24,TIP,[{'type':'heading','indices':[0]},{'type':'visual','blockId':'tip'},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'equation','indices':[3]}],('اشارہ — گاؤسی سطح کا بہاؤ','لارښوونه — د ګاوسي سطحې فلکس'),{'tip':tip}),('phys12-front-project25','Project',25,PROJECT,[{'type':'paragraph','indices':[0]},{'type':'visual','blockId':'project'},{'type':'paragraph','indices':[1]}],('منصوبہ','پروژه'),{'project':project}),('phys12-front-potential25','11.6 ELECTRIC POTENTIAL',25,POTENTIAL,[{'type':'paragraph','indices':[0]},{'type':'visual','blockId':'potential'}],('11.6 برقی پوٹینشل','11.6 برېښنايي پوتانشیل'),{'potential':potential})]
    records=[];sections=[]
    for identity,title,page,pairs,layout,titles,visuals in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':17,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        revised['sourceBlocks']=[{'id':key,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')} for key,fn in visuals.items()]
        revised['content']+=''.join(fn('en') for fn in visuals.values())
        for para in revised['paras']:
            if para['text'].startswith('[Editorial'):para.update(isEditorial=True,originalText=None)
        records.append(record);sections.append(revised)
    upsert(records,sections)
    sync_companions(retire_sections=['11.8'],trim_sections=[{'id':'11.9','startsAt':'The energy is required to move the charge','title':'Electric potential (continued; source review starts at PDF page 18)'}],formulas=[{'id':'phys12-eq-11.17','name':'Parallel-plate electric field','number':'11.17','formula':FIELD[7][0],'latex':r'E=\frac\sigma{\varepsilon_0}','note':'Textbook source equation','sourceReferences':[{'pdfPage':17,'printedPage':24}]}],exercises=[{'id':'project-gaussian-11','title':'Project — Gaussian-surface flux','problems':[{'id':'project-gaussian-11-q1','question':PROJECT[0][0],'diagramSvg':project('en'),'solutionOrigin':'not_provided_in_textbook','sourceReferences':[{'pdfPage':17,'printedPage':25}]}]}])
    checkpoint(17,'corrected_verified',[r['id'] for r in records],
      'Original spread inspected at2.5x. Full parallel-plate continuation, Eq11.17, source dot omission and delta/sigma symbols retained with editorial note. TIP retains enclosed/external charge positions and source numerical solution. Project retains four surfaces, every inside/outside charge, signed labels and inconsistent marker signs with editorial note, no invented answer. Potential introduction and Fig11.18a/b coded with A/B, q0/q and directional arrows. All source prose and relevant captions paired in Urdu/Pashto. Legacy11.8 retired and11.9 covered prefix trimmed to PDF18.',printed_pages=[24,25])
