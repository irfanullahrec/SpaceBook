from class12_source_review import upsert, section, checkpoint, sync_companions
from class12_physics_field_figures import arrow

SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
EXAMPLE=[
 ('A metallic sphere of diameter 40 cm carries a charge of 600 μ C. Find the electric field intensity (a) at a distance of 60cm from the centre of the sphere and (b) at the surface of sphere.', '40 سینٹی میٹر قطر کا دھاتی کرہ 600 مائیکروکولوم بار رکھتا ہے۔ برقی میدان کی شدت معلوم کریں: (a) کرہ کے مرکز سے 60 سینٹی میٹر فاصلے پر، اور (b) کرہ کی سطح پر۔', 'یو فلزي کره چې قطر یې 40 سانتي متره دی، 600 مایکروکولم چارج لري. د برېښنايي میدان شدت معلوم کړئ: (a) د کرې له مرکز څخه په 60 سانتي متره واټن کې، او (b) د کرې پر سطحه.'),
 ('GIVEN','دی گئی معلومات','ورکړل شوي معلومات'),
 (r'Distance of a charge from the sphere \(r=OB=60\,\mathrm{cm}=60\times10^{-2}\,\mathrm m\);',r'کرہ سے بار کا فاصلہ \(r=OB=60\,\mathrm{cm}=60\times10^{-2}\,\mathrm m\)؛',r'له کرې څخه د چارج واټن \(r=OB=60\,\mathrm{cm}=60\times10^{-2}\,\mathrm m\)؛'),
 (r'Charge on sphere \(q=600\,\mu\mathrm C=600\times10^{-6}\,\mathrm C\)',r'کرہ پر بار \(q=600\,\mu\mathrm C=600\times10^{-6}\,\mathrm C\)',r'پر کره چارج \(q=600\,\mu\mathrm C=600\times10^{-6}\,\mathrm C\)'),
 (r'Distance \(r=\frac d2=\frac{OA}{2}=\frac{40\,\mathrm{cm}}2=0.2\,\mathrm m\)',r'فاصلہ \(r=\frac d2=\frac{OA}{2}=\frac{40\,\mathrm{cm}}2=0.2\,\mathrm m\)',r'واټن \(r=\frac d2=\frac{OA}{2}=\frac{40\,\mathrm{cm}}2=0.2\,\mathrm m\)'),
 ('REQUIRED','مطلوب','غوښتل شوي'),
 (r'electric field intensity \(=E=?\)',r'برقی میدان کی شدت \(=E=?\)',r'د برېښنايي میدان شدت \(=E=?\)'),
 ('SOLUTION','حل','حل'),
 ('The electric field due to a charged sphere has spherical symmetry. Therefore, a charged sphere behaves for external points as if the whole charge is placed at its centre.', 'بار دار کرہ کی وجہ سے برقی میدان کروی تقارن رکھتا ہے۔ اس لیے بیرونی نقاط کے لیے بار دار کرہ ایسا برتاؤ کرتا ہے جیسے اس کا پورا بار مرکز پر رکھا گیا ہو۔', 'د چارج لرونکې کرې برېښنايي میدان کروي تقارن لري. له همدې امله د بهرنیو نقطو لپاره چارج لرونکې کره داسې چلند کوي لکه ټول چارج یې په مرکز کې ایښودل شوی وي.'),
 (r'(a) Electric field intensity from the centre of the sphere \(E=k\frac q{r^2}\)',r'(a) کرہ کے مرکز سے برقی میدان کی شدت \(E=k\frac q{r^2}\)',r'(a) د کرې له مرکز څخه د برېښنايي میدان شدت \(E=k\frac q{r^2}\)'),
 (r'\(=9\times10^9\times\frac{600\times10^{-6}}{(60\times10^{-2})^2}=1.5\times10^9\,\mathrm{N/C}\)',)*3,
 (r'(b) electric field intensity from the surface of a sphere \(E=k\frac q{r^2}\)',r'(b) کرہ کی سطح سے برقی میدان کی شدت \(E=k\frac q{r^2}\)',r'(b) د کرې له سطحې څخه د برېښنايي میدان شدت \(E=k\frac q{r^2}\)'),
 (r'\(=9\times10^9\times\frac{600\times10^{-6}}{(0.2)^2}\)',)*3,
 (r'\(=13.5\times10^7\,\mathrm{N/C}\)',)*3,
 (r'[Editorial clarification: the source prints \(OA/2\) in the radius calculation although OA is the radius in its diagram. Part (a) prints \(1.5\times10^9\,\mathrm{N/C}\); the displayed substitution evaluates to \(1.5\times10^7\,\mathrm{N/C}\). Both printed statements are retained.]',r'[ادارتی وضاحت: کتاب نصف قطر کی سطر میں \(OA/2\) چھاپتی ہے، حالانکہ شکل میں OA نصف قطر ہے۔ حصہ (a) میں \(1.5\times10^9\,\mathrm{N/C}\) چھپا ہے؛ دی گئی قیمتوں سے \(1.5\times10^7\,\mathrm{N/C}\) حاصل ہوتا ہے۔ دونوں اصل چھپی ہوئی عبارتیں محفوظ ہیں۔]',r'[د سمونوال وضاحت: کتاب د شعاع په محاسبه کې \(OA/2\) چاپوي، خو په شکل کې OA شعاع ده. په (a) برخه کې \(1.5\times10^9\,\mathrm{N/C}\) چاپ شوی؛ ښودل شوي ارزښتونه \(1.5\times10^7\,\mathrm{N/C}\) ورکوي. دواړه چاپ شوي بیانونه ساتل شوي دي.]'),
]
FLUX=[
 (r'The concept of flux describes how much of something goes through a given area. You may conceptualize the flux of an electric field as a measure of the number of electric field lines passing through an area. For discussing the flux of a vector field, it is helpful to introduce an area vector \(\vec A\). The area vector of a flat surface has magnitude equal to area (A) and its direction is along the normal to the surface \((\hat n)\) as shown in figure 11.11.',r'بہاؤ کا تصور بیان کرتا ہے کہ کسی دیے ہوئے رقبے سے کوئی چیز کتنی مقدار میں گزرتی ہے۔ برقی میدان کے بہاؤ کو رقبے سے گزرنے والے خطوطِ میدان کی تعداد کی پیمائش سمجھا جا سکتا ہے۔ سمتی میدان کے بہاؤ پر گفتگو کے لیے رقبے کا سمتیہ \(\vec A\) متعارف کرانا مفید ہے۔ ہموار سطح کے رقبے کے سمتیے کی مقدار رقبے (A) کے برابر ہوتی ہے اور اس کی سمت سطح کے عمود \((\hat n)\) کے ساتھ ہوتی ہے، جیسا کہ شکل 11.11 میں ہے۔',r'د فلکس مفهوم بیانوي چې د یوې ټاکلې مساحت له لارې یو شی څومره تېرېږي. د برېښنايي میدان فلکس د مساحت له لارې د تېرېدونکو میدان کرښو د شمېر پیمانه ګڼلای شئ. د ویکټوري میدان د فلکس د بحث لپاره د مساحت ویکټور \(\vec A\) معرفي کول ګټور دي. د هوارې سطحې د مساحت د ویکټور مقدار له مساحت (A) سره برابر دی او لوری یې د سطحې له عمود \((\hat n)\) سره وي، لکه په شکل 11.11 کې.'),
 (r'The electric flux is denoted by \(\Phi_E\). For uniform field \(\vec E\) and area \(\vec A\) electric flux is defined as the measure of number of lines of force that pass through the area placed in the electric field. Flux \(\Phi_E\) is the scalar product of the electric field E and plane surface area A.',r'برقی بہاؤ کو \(\Phi_E\) سے ظاہر کرتے ہیں۔ یکساں میدان \(\vec E\) اور رقبے \(\vec A\) کے لیے برقی بہاؤ، برقی میدان میں رکھی ہوئی سطح سے گزرنے والے خطوطِ قوت کی تعداد کی پیمائش ہے۔ بہاؤ \(\Phi_E\)، برقی میدان E اور ہموار سطح کے رقبے A کا عددی حاصل ضرب ہے۔',r'برېښنايي فلکس په \(\Phi_E\) ښودل کېږي. د یوشان میدان \(\vec E\) او مساحت \(\vec A\) لپاره برېښنايي فلکس د برېښنايي میدان په منځ کې ایښودل شوې سطحې د تېرېدونکو قوې کرښو د شمېر پیمانه ده. فلکس \(\Phi_E\) د برېښنايي میدان E او د هوارې سطحې د مساحت A سکالر حاصل ضرب دی.'),
 (r'\(\Phi_E=\vec E\cdot\vec A\)',)*3,
 (r'\(=EA\cos\theta\) ...(11.11)',)*3,
 (r'The electric flux \(\Phi_E\) depends upon:',r'برقی بہاؤ \(\Phi_E\) ان چیزوں پر منحصر ہے:',r'برېښنايي فلکس \(\Phi_E\) په دې پورې اړه لري:'),
 ('i. surface area','i. سطح کا رقبہ','i. د سطحې مساحت'),
 ('ii. electric field intensity','ii. برقی میدان کی شدت','ii. د برېښنايي میدان شدت'),
 ('iii. the orientation of surface area A with respect to the field lines E.','iii. خطوطِ میدان E کے لحاظ سے سطح کے رقبے A کی سمت۔','iii. د میدان کرښو E په نسبت د سطحې د مساحت A جهت.'),
 ('FLUX AT ANY ANGLE (θ) :','کسی بھی زاویے (θ) پر بہاؤ:','په هرې زاویې (θ) کې فلکس:'),
 (r'if the area \(\vec A\) is tilted such that it is making an angle θ with the electric field lines as shown in figure(11.11 b) in this case the electric flux is',r'اگر رقبے \(\vec A\) کو اس طرح جھکایا جائے کہ وہ خطوطِ میدان کے ساتھ زاویہ θ بنائے، جیسا کہ شکل (11.11 b) میں ہے، تو اس صورت میں برقی بہاؤ یہ ہے',r'که مساحت \(\vec A\) داسې کږه شي چې د میدان له کرښو سره زاویه θ جوړه کړي، لکه په شکل (11.11 b) کې، نو په دې حالت کې برېښنايي فلکس دا دی'),
 (r'\(\Phi_E=\vec E\cdot\vec A=EA\cos\theta\)',)*3,
 ('The number of lines passing through the area will be E (A cosθ) depending upon angle θ.','رقبے سے گزرنے والے خطوط کی تعداد، زاویہ θ کے لحاظ سے، E (A cosθ) ہو گی۔','د مساحت له لارې د تېرېدونکو کرښو شمېر به د زاویې θ په پام کې نیولو سره E (A cosθ) وي.'),
 ('MAXIMUM FLUX:','زیادہ سے زیادہ بہاؤ:','تر ټولو زیات فلکس:'),
 (r'if the surface is placed perpendicular to the electric field such that surface area \(\vec A\) is parallel to electric field \(\vec E\) then maximum electric lines of force will pass through the surface as shown in figure 11.11c.',r'اگر سطح کو برقی میدان کے عمود پر رکھا جائے تاکہ سطح کے رقبے کا سمتیہ \(\vec A\)، برقی میدان \(\vec E\) کے متوازی ہو، تو سطح سے زیادہ سے زیادہ برقی خطوطِ قوت گزریں گے، جیسا کہ شکل 11.11c میں ہے۔',r'که سطحه د برېښنايي میدان په عمود کې داسې کېښودل شي چې د سطحې د مساحت ویکټور \(\vec A\) د برېښنايي میدان \(\vec E\) سره موازي وي، نو د سطحې له لارې به تر ټولو زیاتې برېښنايي قوې کرښې تېرې شي، لکه په شکل 11.11c کې.'),
]

def sphere(lang):
    caption={'en':'Field intensity due to a charged sphere','ur':'بار دار کرہ کی وجہ سے میدان کی شدت','ps':'د چارج لرونکې کرې له امله د میدان شدت'}[lang]
    return '<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 160" role="img" aria-label="O at sphere centre, A on surface, B at 60 cm from O" style="width:100%;max-width:500px"><circle cx="100" cy="65" r="40" fill="#facc15" stroke="#334155"/><path d="M100 65H220" stroke="#7f1d1d" stroke-width="2" stroke-dasharray="2 2"/><circle cx="100" cy="65" r="2"/><circle cx="140" cy="65" r="2"/><circle cx="220" cy="65" r="2"/><text x="93" y="55">O</text><text x="139" y="55">A</text><text x="216" y="55">B</text><path d="M100 113V133M220 113V133M100 123H220" stroke="#334155"/>'+arrow(100,123,-1,0,'#334155')+arrow(220,123,1,0,'#334155')+'<rect x="144" y="113" width="45" height="18" fill="#fff"/><text x="146" y="127">60 cm</text></svg><figcaption>'+caption+'</figcaption></figure>'

def area(lang):
    names={'en':['(a) Unit vectors','(b) Electric flux at any angle θ','(c) Electric flux(maximum flux)'], 'ur':['(a) اکائی سمتیے','(b) کسی بھی زاویے θ پر برقی بہاؤ','(c) برقی بہاؤ (زیادہ سے زیادہ بہاؤ)'], 'ps':['(a) واحد ویکټورونه','(b) په هرې زاویې θ کې برېښنايي فلکس','(c) برېښنايي فلکس (تر ټولو زیات فلکس)']}[lang]
    body='<path d="M85 105L270 105 295 137H110Z M85 183L270 183 295 215H110Z" fill="#67c5d2"/>'
    for y,sign in [(115,-1),(195,1)]:
        body+=f'<path d="M180 {y}V{y+sign*75}M201 {y}V{y+sign*55}" stroke="#111827" stroke-width="4"/>'+arrow(180,y+sign*75,0,sign,'#111827',10)+arrow(201,y+sign*55,0,sign,'#111827',10)
        body+=f'<text x="152" y="{y}">A</text><text x="151" y="{y+sign*45}">A⃗</text><text x="210" y="{y+sign*34}">n̂</text>'
    body+=f'<text x="70" y="284">{names[0]}</text><path d="M137 317L183 317 256 449 210 449Z" fill="#be123c" stroke="#881337"/>'
    for y in range(332,446,18):
        body+=f'<path d="M82 {y}H330" stroke="#334155"/>'+arrow(330,y,1,0,'#334155')
    body+='<path d="M188 365L270 323" stroke="#b91c1c" stroke-width="3"/>'+arrow(270,323,82,-42,'#b91c1c',10)+'<path d="M213 365A25 25 0 0 0 210 353" fill="none" stroke="#334155"/><text x="218" y="361">θ</text><text x="270" y="312">A⃗</text><text x="306" y="470">E⃗</text>'
    body+=f'<text x="35" y="504">{names[1]}</text><path d="M168 576L222 530V675L168 716Z" fill="#be123c" stroke="#881337"/>'
    for y in range(578,691,19):
        body+=f'<path d="M82 {y}H330" stroke="#334155"/>'+arrow(330,y,1,0,'#334155')
    body+='<path d="M222 562H298" stroke="#b91c1c" stroke-width="4"/>'+arrow(298,562,1,0,'#b91c1c',10)+'<text x="295" y="550">A⃗</text><text x="57" y="603">E⃗</text>'
    body+=f'<text x="24" y="752">{names[2]}</text>'
    return '<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 430 780" role="img" aria-label="Figure 11.11: area normals, tilted surface and maximum flux" style="width:100%;max-width:430px">'+body+'</svg><figcaption>'+('FIGURE' if lang=='en' else 'شکل')+' 11.11</figcaption></figure>'

if __name__=='__main__':
    records=[]; sections=[]
    for identity,title,page,pairs,layout,titles,visual in [
      ('phys12-front-example113','Example 11.3',14,EXAMPLE,
       [{'type':'paragraph','indices':[0]},{'type':'heading','indices':[1]},{'type':'lines','indices':[2,3,4]},{'type':'heading','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'heading','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'visual'}]+[{'type':'paragraph' if i in (9,11,14) else 'equation','indices':[i]} for i in range(9,15)],
       ('مثال 11.3','بېلګه 11.3'),sphere),
      ('phys12-front-flux15','11.4 ELECTRIC FLUX',15,FLUX,
       [{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'equation','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'orderedList','indices':[5,6,7]},{'type':'visual'},{'type':'heading','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'equation','indices':[10]},{'type':'paragraph','indices':[11]},{'type':'heading','indices':[12]},{'type':'paragraph','indices':[13]}],
       ('11.4 برقی بہاؤ','11.4 برېښنايي فلکس'),area),
    ]:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':12,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs],'diagramHtml':visual('en')}
        revised=section(record,pairs,layout,titles); revised['kind']='lesson'
        revised['diagramSvg']=visual('en'); revised['diagramSvgUrdu']=visual('ur'); revised['diagramSvgPashto']=visual('ps'); revised['content']+=visual('en')
        if page==14:
            revised['paras'][14]['isEditorial']=True; revised['paras'][14]['originalText']=None
            record['sourceDefects']=[EXAMPLE[14][0]]
        records.append(record); sections.append(revised)
    example={'id':'textbook-example-3','num':'11.3','title':'Example 11.3','problem':EXAMPLE[0][0],
             'given':[p[0] for p in EXAMPLE[2:5]],'required':[EXAMPLE[6][0]],'steps':[p[0] for p in EXAMPLE[8:14]],
             'answer':r'(a) \(1.5\times10^9\,\mathrm{N/C}\), (b) \(13.5\times10^7\,\mathrm{N/C}\)',
             'solutionOrigin':'textbook','sourceClarifications':[EXAMPLE[14][0]],'diagramSvg':sphere('en'),
             'sourceReferences':[{'pdfPage':12,'printedPage':14,'sourcePdf':SOURCE}]}
    upsert(records,sections)
    sync_companions(formulas=[{'id':'phys12-eq-11.11','name':'Electric flux','number':'11.11','formula':r'\(\Phi_E=\vec E\cdot\vec A=EA\cos\theta\)','latex':r'\Phi_E=\vec E\cdot\vec A=EA\cos\theta','note':'Textbook source equation','sourceReferences':[{'pdfPage':12,'printedPage':15}]}],
                    definitions=[{'term':'Electric flux','def':FLUX[1][0],'sourceReferences':[{'pdfPage':12,'printedPage':15}]}],
                    worked_examples=[example], retire_sections=['11.5'],
                    trim_sections=[{'id':'11.6','startsAt':'Consequently maximum electric lines','title':'Electric flux (continued; source review starts at PDF page 13)'}])
    checkpoint(12,'corrected_verified',[r['id'] for r in records],
               'Full original spread inspected at 3x. Example 11.3 statement, given conversions, required quantity, spherical-symmetry explanation, both substitutions and printed numerical answers transcribed; printed OA/2 and 1.5×10^9 preserved and editorial discrepancy separately translated. New native sphere SVG retains O/A/B and 60 cm separation with correct radius/separation ratio. Flux definition, area normal, scalar product Eq 11.11, roman-numbered dependencies, tilted-area and maximum-flux paragraphs implemented with aligned Urdu/Pashto pairs. Figure 11.11 rebuilt as normal-up/normal-down, angle theta and parallel E/A maximum-flux panels. Existing OCR card 11.5 retired and covered prefix of 11.6 trimmed in place; no duplicate source material. Worked-example, definition and formula cards upserted.',printed_pages=[14,15])
