from class12_source_review import upsert, section, checkpoint, sync_companions
from class12_physics_page013 import SOURCE, svg

CURRENT=[
 ('2. Those substances which have a larger number of free electrons permit current to flow easily. Such substances are called conductors; examples include copper, zinc, silver and aluminium.', '2۔ وہ مادے جن میں آزاد الیکٹران زیادہ ہوں، ان میں رو آسانی سے بہتی ہے۔ ایسے مادوں کو موصل کہتے ہیں؛ مثلاً تانبا، زنک، چاندی اور ایلومینیم۔', '2. هغه مواد چې ازاد الکترونونه پکې ډېر وي، جریان په اسانۍ پرې بهېږي. دغسې مواد هادیان بلل کېږي؛ لکه مس، جست، سپین زر او المونیم.'),
 ('In different current-carrying materials, the moving particles may carry positive or negative charge. In metals the moving charges are always electrons (negative charges), while in gases the moving charges are negative and positive ions. We define the current through cross-sectional area A as the net charge flowing through the area per unit time. Thus if a net charge Q flows through an area in time t, the current I is', 'مختلف رو بردار مادوں میں متحرک ذرات مثبت یا منفی بار لے جا سکتے ہیں۔ دھاتوں میں متحرک بار ہمیشہ الیکٹران (منفی بار) ہوتے ہیں، جبکہ گیسوں میں متحرک بار منفی اور مثبت آئن ہوتے ہیں۔ رقبۂ مقطع A سے گزرنے والی رو کو فی اکائی وقت اس رقبے سے گزرنے والے خالص بار سے متعین کرتے ہیں۔ چنانچہ اگر وقت t میں خالص بار Q گزرے تو رو I ہوگی:', 'په بېلابېلو جریان‌وړونکو موادو کې خوځنده ذرات مثبت یا منفي چارج لرلای شي. په فلزاتو کې خوځنده چارجونه تل الکترونونه (منفي چارجونه) وي، خو په ګازونو کې منفي او مثبت ایونونه خوځېږي. د A مقطع له لارې جریان د هر واحد وخت په ترڅ کې د تېرېدونکي خالص چارج په توګه تعریفوو. نو که په t وخت کې خالص چارج Q تېر شي، جریان I دا دی:'),
 (r'\(I=\frac{Q}{t}\) ...(12.1)',)*3,
 ('Charge Q is measured in coulombs and time t in seconds. Therefore the unit of electric current is coulomb per second, or ampere (A). One ampere is the current when one coulomb of charge flows across any cross-section of a conductor in one second. The submultiples of ampere are:', 'بار Q کولومب اور وقت t سیکنڈ میں ناپا جاتا ہے۔ اس لیے برقی رو کی اکائی کولومب فی سیکنڈ یا ایمپیئر (A) ہے۔ ایک ایمپیئر وہ رو ہے جس میں ایک سیکنڈ میں موصل کے کسی بھی مقطع سے ایک کولومب بار گزرے۔ ایمپیئر کی ذیلی اکائیاں یہ ہیں:', 'چارج Q په کولمب او وخت t په ثانیو اندازه کېږي. نو د برېښنايي جریان واحد کولمب پر ثانیه، یا امپیر (A) دی. یو امپیر هغه جریان دی چې په یوه ثانیه کې د هادي له هرې مقطع څخه یو کولمب چارج تېر شي. د امپیر فرعي واحدونه دا دي:'),
 (r'\(1\,\mathrm{mA}=1\times10^{-3}\,\mathrm A\)',)*3,
 (r'\(1\,\mu\mathrm A=1\times10^{-6}\,\mathrm A\)',)*3,
 ('TIP', 'اشارہ', 'اشاره'),
 ('Current is a scalar quantity because it does not follow the vector law of addition.', 'رو ایک غیر سمتی مقدار ہے کیونکہ یہ سمتی جمع کے قانون کی پیروی نہیں کرتی۔', 'جریان سکالر مقدار دی، ځکه د ویکټوري جمع له قانون سره سمون نه خوري.'),
 ('DO YOU KNOW?', 'کیا آپ جانتے ہیں؟', 'ایا پوهېږئ؟'),
 ('If electrons drift so slowly, why does room light turn on quickly when a switch is closed? The answer is that propagation of the electric field takes place at the speed of light.', 'اگر الیکٹران آہستہ سرکتے ہیں تو سوئچ بند کرنے پر کمرے کی روشنی فوراً کیوں جلتی ہے؟ اس کی وجہ یہ ہے کہ برقی میدان روشنی کی رفتار سے پھیلتا ہے۔', 'که الکترونونه ورو خوځېږي، نو د سویچ په تړلو سره د خونې څراغ ولې ژر بلېږي؟ ځواب دا دی چې برېښنايي میدان د رڼا په سرعت خپرېږي.'),
]

EXAMPLE=[
 (r'Each second \(10^{18}\) electrons flow from right to left across a cross-section of a wire attached to the two terminals of a battery. (a) Calculate the current in the wire. (b) In which direction is the current flowing?',r'بیٹری کے دونوں ٹرمینلوں سے جڑی تار کے مقطع سے ہر سیکنڈ \(10^{18}\) الیکٹران دائیں سے بائیں گزرتے ہیں۔ (a) تار میں رو معلوم کریں۔ (b) رو کس سمت میں بہتی ہے؟',r'په هره ثانیه کې د بېټرۍ له دواړو ټرمینلونو سره د نښتي تار له مقطع څخه \(10^{18}\) الکترونونه له ښي څخه چپ لوري ته تېرېږي. (a) په تار کې جریان ومومئ. (b) جریان په کوم لوري بهېږي؟'),
 ('GIVEN','معلوم ہے','ورکړل شوي'),
 (r'\(n=10^{18}\); charge on one electron \(e=1.6\times10^{-19}\,\mathrm C\); \(t=1\,\mathrm s\)',r'\(n=10^{18}\)؛ ایک الیکٹران کا بار \(e=1.6\times10^{-19}\,\mathrm C\)؛ \(t=1\,\mathrm s\)',r'\(n=10^{18}\)؛ د یوه الکترون چارج \(e=1.6\times10^{-19}\,\mathrm C\)؛ \(t=1\,\mathrm s\)'),
 ('REQUIRED','مطلوب','غوښتل شوي'),
 (r'(a) Electric current \(I=?\); (b) direction of current flow = ?',r'(a) برقی رو \(I=?\)؛ (b) رو کے بہاؤ کی سمت؟',r'(a) برېښنايي جریان \(I=?\)؛ (b) د جریان لوری؟'),
 ('SOLUTION','حل','حل'),
 (r'\(I=\frac Qt=\frac{ne}{t}\)',)*3,
 (r'\(I=\frac{10^{18}\times1.6\times10^{-19}}{1}=1.6\times10^{-1}\,\mathrm A=160\,\mathrm{mA}\)',)*3,
 ('The current flows from left to right, that is, in the opposite direction to the electron flow.', 'رو بائیں سے دائیں بہتی ہے، یعنی الیکٹرانوں کے بہاؤ کی مخالف سمت میں۔', 'جریان له چپ څخه ښي لوري ته بهېږي، یعنې د الکترونونو د بهیر مخالف لوري ته.'),
]

DRIFT=[
 ('DRIFT VELOCITY IN CONDUCTOR','موصل میں بہاؤ کی رفتار','په هادي کې د ډرفټ سرعت'),
 ('Every conductor is made up of atoms, which in turn are composed of electrons. These electrons move in random directions within an atom. Due to their random motion, the net velocity of negatively charged electrons in a conductor is zero.', 'ہر موصل ایٹموں سے بنا ہے، اور ایٹم الیکٹرانوں پر مشتمل ہوتے ہیں۔ یہ الیکٹران ایٹم میں بے ترتیب سمتوں میں حرکت کرتے ہیں۔ اس بے ترتیب حرکت کے باعث موصل میں منفی بار والے الیکٹرانوں کی خالص رفتار صفر ہوتی ہے۔', 'هر هادي له اتومونو جوړ دی او اتومونه له الکترونونو جوړ دي. دا الکترونونه د اتوم دننه په تصادفي لورو خوځېږي. د دې تصادفي حرکت له امله په هادي کې د منفي چارج لرونکو الکترونونو خالص سرعت صفر وي.'),
 ('When a potential difference is applied to the ends of a conductor, an electric field E is set up at every point within the wire. As a result of this force, the electrons in the conductor acquire a certain amount of velocity, which causes a net flow in one direction. This velocity that causes electrons to move in a certain direction is known as drift velocity.', 'جب موصل کے سروں پر فرقِ پوٹینشل لگایا جاتا ہے تو تار کے ہر نقطے پر برقی میدان E قائم ہوتا ہے۔ اس قوت کے نتیجے میں موصل کے الیکٹران کچھ رفتار حاصل کرتے ہیں اور ایک سمت میں خالص بہاؤ پیدا ہوتا ہے۔ الیکٹرانوں کو کسی سمت میں حرکت دینے والی اس رفتار کو ڈرفٹ رفتار کہتے ہیں۔', 'کله چې د هادي پر پایونو پوتنشیالي توپیر ولګېږي، د سیم په هره نقطه کې برېښنايي میدان E جوړېږي. د دې قوې له امله د هادي الکترونونه یو ټاکلی سرعت اخلي او په یوه لوري کې خالص بهیر رامنځته کوي. هغه سرعت چې الکترونونه په یوه ټاکلي لوري خوځوي، د ډرفټ سرعت بلل کېږي.'),
 (r'The net velocity with which free electrons drift in a conductor under the influence of an electric field is called drift velocity \(\vec v_d\).',r'برقی میدان کے زیر اثر موصل میں آزاد الیکٹران جس خالص رفتار سے سرکتے ہیں اسے ڈرفٹ رفتار \(\vec v_d\) کہتے ہیں۔',r'د برېښنايي میدان تر اغېز لاندې په هادي کې د ازادو الکترونونو خالص خوځنده سرعت د ډرفټ سرعت \(\vec v_d\) بلل کېږي.'),
]

def drift_figure(lang):
    labels={'en':('Free electron','Atom','Drift of free electrons'), 'ur':('آزاد الیکٹران','ایٹم','آزاد الیکٹرانوں کا بہاؤ'), 'ps':('ازاد الکترون','اتوم','د ازادو الکترونونو ډرفټ')}[lang]
    body='<rect x="15" y="40" width="210" height="100" rx="45" fill="#fff7ed" stroke="#334155" stroke-width="3"/><circle cx="118" cy="90" r="25" fill="#fde047" stroke="#a16207" stroke-width="3"/>'
    for x,y,dx,dy in [(42,70,12,-7),(70,112,-10,6),(98,57,8,7),(150,65,-8,-8),(184,108,10,-5),(201,75,-8,6)]:body+=f'<path d="M{x} {y}l{dx} {dy}" stroke="#0284c7" stroke-width="2" marker-end="url(#a)"/>'
    body+='<text x="24" y="30">'+labels[0]+'</text><text x="95" y="95">'+labels[1]+'</text><text x="15" y="158">(a)</text>'
    body+='<rect x="270" y="50" width="195" height="52" rx="26" fill="#fff7ed" stroke="#334155" stroke-width="3"/><circle cx="365" cy="76" r="22" fill="#fde047" stroke="#a16207" stroke-width="3"/>'
    for x in (300,330,395,425):body+=f'<path d="M{x} 76H{x+20}" stroke="#0284c7" stroke-width="3" marker-end="url(#a)"/>'
    body+='<path d="M270 102V205H465V102M270 160H465" fill="none" stroke="#334155" stroke-width="3"/><path d="M315 205V188M300 188H330M306 178H324M337 205V188M322 188H352M328 178H346" stroke="#334155" stroke-width="2"/><path d="M430 166H335" stroke="#c026d3" stroke-width="3" marker-end="url(#a)"/><text x="380" y="155">E</text><text x="256" y="54">−</text><text x="468" y="54">+</text><text x="268" y="226">(b)</text><text x="290" y="250">'+labels[2]+'</text>'
    return '<figure>'+svg(body,485,275,'Random electron motion around atoms and directed drift under an electric field in a conductor')+'<figcaption>FIGURE 12.2</figcaption></figure>'

if __name__=='__main__':
    specs=[
      ('phys12-unit12-current54','12.1 Steady current — definition and units',54,CURRENT,('12.1 مستقل برقی رو — تعریف اور اکائیاں','12.1 ثابت برېښنايي جریان — تعریف او واحدونه'),[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'equation','indices':[4]},{'type':'equation','indices':[5]},{'type':'heading','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'heading','indices':[8]},{'type':'paragraph','indices':[9]}],None),
      ('phys12-unit12-example12154-55','Example 12.1 — current and direction',54,EXAMPLE,('مثال 12.1 — رو اور سمت','بېلګه 12.1 — جریان او لوری'),[{'type':'paragraph','indices':[0]},{'type':'heading','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'heading','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'heading','indices':[5]},{'type':'equation','indices':[6]},{'type':'equation','indices':[7]},{'type':'paragraph','indices':[8]}],None),
      ('phys12-unit12-drift55','Drift velocity in a conductor',55,DRIFT,('موصل میں ڈرفٹ رفتار','په هادي کې د ډرفټ سرعت'),[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'visual'}],drift_figure),
    ]
    records=[];sections=[]
    for identity,title,printed,pairs,headings,layout,visual in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':32,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        item=section(record,pairs,layout,headings);item['kind']='lesson'
        if visual:item.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'));item['content']+=item['diagramSvg']
        if identity.endswith('example12154-55'):
            item['sourceReferences']=[{'pdfPage':32,'printedPage':54,'sourcePdf':SOURCE},{'pdfPage':32,'printedPage':55,'sourcePdf':SOURCE}]
        records.append(record);sections.append(item)
    upsert(records,sections,chapter_index=1)
    sync_companions(chapter_index=1,formulas=[
      {'id':'phys12-unit12-eq-12.1','name':'Electric current','number':'12.1','formula':CURRENT[2][0],'latex':r'I=\frac{Q}{t}','sourceReferences':[{'pdfPage':32,'printedPage':54}]},
      {'id':'phys12-unit12-eq-electron-count-current','name':'Current from number of electrons','formula':EXAMPLE[6][0],'latex':r'I=\frac{ne}{t}','sourceReferences':[{'pdfPage':32,'printedPage':55}]},
    ],definitions=[
      {'term':'Electric current','definition':CURRENT[1][0]+' '+CURRENT[2][0],'definitionUrdu':CURRENT[1][1]+' '+CURRENT[2][1],'definitionPashto':CURRENT[1][2]+' '+CURRENT[2][2],'sourceReferences':[{'pdfPage':32,'printedPage':54}]},
      {'term':'Ampere','definition':CURRENT[3][0],'definitionUrdu':CURRENT[3][1],'definitionPashto':CURRENT[3][2],'sourceReferences':[{'pdfPage':32,'printedPage':54}]},
      {'term':'Drift velocity','definition':DRIFT[3][0],'definitionUrdu':DRIFT[3][1],'definitionPashto':DRIFT[3][2],'sourceReferences':[{'pdfPage':32,'printedPage':55}]},
    ],worked_examples=[
      {'id':'textbook-example-12-1','num':'12.1','title':'Example 12.1','problem':EXAMPLE[0][0],'given':[EXAMPLE[2][0]],'required':[EXAMPLE[4][0]],'steps':[EXAMPLE[6][0],EXAMPLE[7][0]],'answer':'160 mA; current flows left to right, opposite to electron flow','solutionOrigin':'textbook','sourceReferences':[{'pdfPage':32,'printedPage':54},{'pdfPage':32,'printedPage':55}]}
    ],trim_sections=[{'id':'12.1','startsAt':'12.2 OHM&#x27;S LAW','title':'Steady current — source review through PDF page 32'}])
    checkpoint(32,'corrected_verified',[r['id'] for r in records],
      'Original spread rendered at 2.5x and inspected. Current definition, equation 12.1, ampere and submultiples, scalar note, propagation-of-field tip, Example 12.1 solution, drift-velocity definition and Figure 12.2 compared. Example result/direction are textbook answers. Figure 12.2 rebuilt as native SVG. Legacy Unit 12 topic trimmed at the next section boundary.',printed_pages=[54,55],chapter_number=12)
