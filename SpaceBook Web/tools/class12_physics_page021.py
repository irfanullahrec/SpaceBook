from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
from class12_physics_field_figures import arrow
POTENTIAL=[
 ('The electric potential at a point in an electric field may be defined as the amount of work done in moving a unit positive charge from infinity to that point with uniform velocity.','برقی میدان میں کسی نقطے پر برقی پوٹینشل کی تعریف اس کام کی مقدار کے طور پر کی جا سکتی ہے جو اکائی مثبت بار کو یکساں رفتار سے لامحدود فاصلے سے اس نقطے تک منتقل کرنے میں کیا جائے۔','په برېښنايي میدان کې په یوه نقطه کې برېښنايي پوتانشیل د هغه کار د مقدار په توګه تعریفېدای شي چې یو واحد مثبت چارج له نامحدود واټن څخه هغې نقطې ته په یوشان سرعت لېږدول کېږي.'),
 ('The electric potential at distance r from Q is','Q سے فاصلے r پر برقی پوٹینشل یہ ہے','له Q څخه په r واټن کې برېښنايي پوتانشیل دا دی'),
 (r'\(V=\frac Wq=\frac1{4\pi\varepsilon_o}\frac Qr\) ...(11.28)',)*3,
]
EXAMPLE=[
 (r'A point charge of 3μC is placed at point O between M and N, 3cm apart. Point M is 2cm from the charge and N is 1cm from the charge. What is the potential difference \(V_M-V_N\)?',r'3 مائیکروکولومب کا نقطہ بار، M اور N کے درمیان نقطہ O پر رکھا ہے، جبکہ M اور N کا فاصلہ 3 سینٹی میٹر ہے۔ نقطہ M بار سے 2 سینٹی میٹر اور N بار سے 1 سینٹی میٹر دور ہے۔ فرقِ برق \(V_M-V_N\) کیا ہے؟',r'د 3 مایکروکولم نقطوي چارج د M او N ترمنځ په O نقطه کې ایښودل شوی، چې د M او N واټن 3 سانتي متره دی. M نقطه له چارج څخه 2 سانتي متره او N له چارج څخه 1 سانتي متره لرې ده. د پوتانشیل توپیر \(V_M-V_N\) څومره دی؟'),
 ('GIVEN','دی گئی معلومات','ورکړل شوي معلومات'),
 (r'charge \(q=3\mu\mathrm C\), distance \(r_1=2\mathrm{cm}\), distance \(r_2=1\mathrm{cm}\)',r'بار \(q=3\mu\mathrm C\)، فاصلہ \(r_1=2\mathrm{cm}\)، فاصلہ \(r_2=1\mathrm{cm}\)',r'چارج \(q=3\mu\mathrm C\)، واټن \(r_1=2\mathrm{cm}\)، واټن \(r_2=1\mathrm{cm}\)'),
 ('REQUIRED','مطلوب','غوښتل شوي'),
 (r'the potential difference \(V_M-V_N=?\)',r'فرقِ برق \(V_M-V_N=?\)',r'د پوتانشیل توپیر \(V_M-V_N=?\)'),
 ('SOLUTION','حل','حل'),
 ('Potential at M due to the charge is','بار کی وجہ سے M پر پوٹینشل یہ ہے','د چارج له امله په M کې پوتانشیل دا دی'),
 (r'\(V_M=k\frac q{r_1}\)',)*3,
 (r'\(V_M=9\times10^9\times\frac{3\times10^{-6}}{2\times10^{-2}}=13.5\times10^5\mathrm V\)',)*3,
 ('Potential at N due to the charge is','بار کی وجہ سے N پر پوٹینشل یہ ہے','د چارج له امله په N کې پوتانشیل دا دی'),
 (r'\(V_N=k\frac q{r_2}=9\times10^9\times\frac{3\times10^{-6}}{1\times10^{-2}}=27\times10^5\mathrm V\)',)*3,
 (r'\(\therefore V_M-V_N=13.5\times10^5-27\times10^5=-13.5\times10^5\mathrm V\)',)*3,
]
ASSIGNMENT=[
 (r'Two charges \(5\times10^{-8}\mathrm C\) and \(-3\times10^{-8}\mathrm C\) are located 16 cm apart. At what point(s) on the line joining the two charges is the electric potential zero? Take the potential at infinity to be zero.',r'دو بار \(5\times10^{-8}\mathrm C\) اور \(-3\times10^{-8}\mathrm C\)، 16 سینٹی میٹر فاصلے پر ہیں۔ دونوں باروں کو ملانے والی لکیر کے کس نقطے یا نقاط پر برقی پوٹینشل صفر ہے؟ لامحدود فاصلے پر پوٹینشل صفر لیں۔',r'دوه چارجونه \(5\times10^{-8}\mathrm C\) او \(-3\times10^{-8}\mathrm C\) په 16 سانتي متره واټن کې دي. د دواړو چارجونو د نښلوونکې کرښې په کومه نقطه یا نقطو کې برېښنايي پوتانشیل صفر دی؟ په نامحدود واټن کې پوتانشیل صفر ونیسئ.'),
 ('Ans(10 cm)','جواب (10 سینٹی میٹر)','ځواب (10 سانتي متره)'),
]
EV=[
 ('The electron-volt is a unit of energy or work which is defined as the amount of energy acquired or lost by an electron when it is displaced across two points between which potential difference is one volt.','الیکٹران وولٹ، توانائی یا کام کی اکائی ہے، جس کی تعریف اس توانائی کی مقدار کے طور پر ہے جو الیکٹران کو دو ایسے نقاط کے درمیان منتقل کرنے پر حاصل ہوتی ہے یا ضائع ہوتی ہے جن کے درمیان فرقِ برق ایک وولٹ ہو۔','الکترون ولټ د انرژۍ یا کار واحد دی چې د هغې انرژۍ د مقدار په توګه تعریفېږي چې یو الکترون یې د دوو نقطو ترمنځ په لېږدولو کې ترلاسه کوي یا له لاسه ورکوي، چې ترمنځ یې د پوتانشیل توپیر یو ولټ وي.'),
 (r'Since the magnitude of the charge of an electron is about \(1.602\times10^{-19}\mathrm C\), it follows that an electron-volt is about \(1.602\times10^{-19}\mathrm J\).',r'چونکہ الیکٹران کے بار کی مقدار تقریباً \(1.602\times10^{-19}\mathrm C\) ہے، اس لیے ایک الیکٹران وولٹ تقریباً \(1.602\times10^{-19}\mathrm J\) ہے۔',r'څرنګه چې د الکترون د چارج مقدار نږدې \(1.602\times10^{-19}\mathrm C\) دی، نو یو الکترون ولټ نږدې \(1.602\times10^{-19}\mathrm J\) دی.'),
 ('By definition','تعریف سے','د تعریف له مخې'),
 (r'\(\Delta(\mathrm{KE})=1\mathrm{eV}\), when \(q=e=1.602\times10^{-19}\mathrm C\) and \(\Delta V=1\mathrm V\).',r'\(\Delta(\mathrm{KE})=1\mathrm{eV}\)، جب \(q=e=1.602\times10^{-19}\mathrm C\) اور \(\Delta V=1\mathrm V\) ہوں۔',r'\(\Delta(\mathrm{KE})=1\mathrm{eV}\)، کله چې \(q=e=1.602\times10^{-19}\mathrm C\) او \(\Delta V=1\mathrm V\) وي.'),
 ('thus','پس','نو'),
 (r'\(1\mathrm{eV}=1.602\times10^{-19}\mathrm C\times1\mathrm V\)',)*3,
 (r'\(=1.602\times10^{-19}\mathrm J\)',)*3,
 ('This is the smaller unit of energy. Its bigger units are multiples of 1 eV that are in frequent use are given below.','یہ توانائی کی چھوٹی اکائی ہے۔ اس کی بڑی اکائیاں 1 eV کے مضارب ہیں جو کثرت سے استعمال ہوتی ہیں اور نیچے دی گئی ہیں۔','دا د انرژۍ کوچنی واحد دی. لوی واحدونه یې د 1 eV مضربونه دي چې ډېر کارول کېږي او لاندې ورکړل شوي دي.'),
 (r'1 Million electron volt \(=1\mathrm{MeV}=10^6\mathrm{eV}\)',r'1 ملین الیکٹران وولٹ \(=1\mathrm{MeV}=10^6\mathrm{eV}\)',r'1 میلیون الکترون ولټ \(=1\mathrm{MeV}=10^6\mathrm{eV}\)'),
 (r'1 Giga electron volt \(=1\mathrm{GeV}=10^9\mathrm{eV}\)',r'1 گیگا الیکٹران وولٹ \(=1\mathrm{GeV}=10^9\mathrm{eV}\)',r'1 ګیګا الکترون ولټ \(=1\mathrm{GeV}=10^9\mathrm{eV}\)'),
]
PARTICLE=[
 ('A particle carrying a charge (3e) falls through a potential difference of 5V. Calculate the energy acquired by the particle.','(3e) بار رکھنے والا ذرہ 5 وولٹ کے فرقِ برق سے گزرتا ہے۔ ذرے کی حاصل کردہ توانائی معلوم کریں۔','یو ذره چې (3e) چارج لري، د 5 ولټه پوتانشیل توپیر له لارې تېرېږي. د ذرې ترلاسه شوې انرژي محاسبه کړئ.'),
 ('GIVEN','دی گئی معلومات','ورکړل شوي معلومات'),
 (r'Charge \(=q=3e\), potential difference \(\Delta V=5\mathrm V\)',r'بار \(=q=3e\)، فرقِ برق \(\Delta V=5\mathrm V\)',r'چارج \(=q=3e\)، د پوتانشیل توپیر \(\Delta V=5\mathrm V\)'),
 ('REQUIRED','مطلوب','غوښتل شوي'),
 ('Energy: K.E=?','توانائی: K.E=?','انرژي: K.E=?'),
 ('SOLUTION','حل','حل'),
 ('The energy acquired by the charged particle is','بار دار ذرے کی حاصل کردہ توانائی یہ ہے','د چارج لرونکې ذرې ترلاسه شوې انرژي دا ده'),
 (r'\(\Delta(\mathrm{KE})=q\Delta V=(3e)(5\mathrm V)=15\mathrm{eV}\)',)*3,
 (r'\(=15\times1.602\times10^{-19}\mathrm J=2.4\times10^{-18}\mathrm J\)',)*3,
 ('[Editorial clarification: the source prints Example 11.6 for both the point-charge problem on printed page 32 and this particle-energy problem on page 33. Both printed numbers are retained with separate record identities.]','[ادارتی وضاحت: کتاب صفحہ 32 کے نقطہ بار کے سوال اور صفحہ 33 کے اس ذرے کی توانائی کے سوال دونوں پر مثال 11.6 چھاپتی ہے۔ دونوں اصل نمبر الگ شناخت والے ریکارڈوں کے ساتھ محفوظ ہیں۔]','[د سمونوال وضاحت: کتاب د 32 مخ د نقطوي چارج پوښتنې او د 33 مخ د دې ذرې د انرژۍ پوښتنې دواړو لپاره بېلګه 11.6 چاپوي. دواړه چاپ شوي شمېرې د جلا پېژندنو لرونکو ریکارډونو سره ساتل شوې دي.]'),
]

def figure(lang):
    body='<path d="M45 42H345" stroke="#334155" stroke-dasharray="2 3"/>'
    for label,x in [('M',45),('O',245),('N',345)]:body+=f'<circle cx="{x}" cy="42" r="3"/><text x="{x-5}" y="28">{label}</text><path d="M{x} 87V109" stroke="#334155"/>'
    for x1,x2,text in [(45,245,'2cm'),(245,345,'1cm')]:body+=f'<path d="M{x1} 98H{x2}" stroke="#334155" stroke-width="2"/>'+arrow(x1,98,-1,0,'#334155')+arrow(x2,98,1,0,'#334155')+f'<text x="{(x1+x2)/2-14}" y="84">{text}</text>'
    cap={'en':'Potential due to a point charge','ur':'نقطہ بار کی وجہ سے پوٹینشل','ps':'د نقطوي چارج له امله پوتانشیل'}[lang]
    return '<figure>'+svg(body,400,125,'M O N collinear; positive charge at O, distance MO2cm and ON1cm')+'<figcaption>'+cap+'</figcaption></figure>'

if __name__=='__main__':
    records=[];sections=[]
    specs=[('phys12-front-potential32','Point-charge electric potential',32,POTENTIAL,('نقطہ بار کا برقی پوٹینشل','د نقطوي چارج برېښنايي پوتانشیل'),None),('phys12-front-example116','EXAMPLE 11.6',32,EXAMPLE,('مثال 11.6','بېلګه 11.6'),figure),('phys12-front-assignment113','ASSIGNMENT 11.3',33,ASSIGNMENT,('مشق 11.3','دنده 11.3'),None),('phys12-front-electronvolt33','THE ELECTRON VOLT (eV)',33,EV,('الیکٹران وولٹ (eV)','الکترون ولټ (eV)'),None),('phys12-front-example116-ev','EXAMPLE 11.6',33,PARTICLE,('مثال 11.6','بېلګه 11.6'),None)]
    for identity,title,page,pairs,titles,visual in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':21,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        layout=[{'type':'heading' if p[0] in ['GIVEN','REQUIRED','SOLUTION'] else 'equation' if p[0].startswith(r'\(') else 'paragraph','indices':[i]} for i,p in enumerate(pairs)]
        if visual:layout.insert(1,{'type':'visual'})
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        if visual:
            revised.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'));revised['content']+=visual('en')
        for para in revised['paras']:
            if para['text'].startswith('[Editorial'):para.update(isEditorial=True,originalText=None)
        records.append(record);sections.append(revised)
    upsert(records,sections)
    examples=[]
    for identity,pairs,page,title in [('textbook-example-6',EXAMPLE,32,'Example 11.6 — point-charge potential'),('textbook-example-6-electronvolt',PARTICLE,33,'Example 11.6 — particle energy')]:
        examples.append({'id':identity,'num':'11.6','title':title,'problem':pairs[0][0],'given':[pairs[2][0]],'required':[pairs[4][0]],'steps':[p[0] for p in pairs[6:] if not p[0].startswith('[Editorial')],'answer':pairs[-1 if page==32 else -2][0],'solutionOrigin':'textbook','sourceReferences':[{'pdfPage':21,'printedPage':page}]})
    sync_companions(retire_sections=['11.11'],trim_sections=[{'id':'11.12','startsAt':'11.10 CAPACITOR','title':'Capacitor (source review starts at PDF page 22)','clearSciNote':True}],formulas=[{'id':'phys12-eq-11.28','name':'Point-charge potential','number':'11.28','formula':POTENTIAL[2][0],'latex':r'V=\frac Wq=\frac1{4\pi\varepsilon_o}\frac Qr','note':'Textbook source equation','sourceReferences':[{'pdfPage':21,'printedPage':32}]},{'id':'phys12-electronvolt-joule','name':'Electron-volt in joules','formula':EV[6][0],'latex':r'1\mathrm{eV}=1.602\times10^{-19}\mathrm J','note':'Textbook conversion','sourceReferences':[{'pdfPage':21,'printedPage':33}]}],definitions=[{'term':'Electron-volt','def':EV[0][0],'sourceReferences':[{'pdfPage':21,'printedPage':33}]}],worked_examples=examples,exercises=[{'id':'assignment-11-3','title':'Assignment 11.3','problems':[{'id':'assignment-11-3-q1','question':ASSIGNMENT[0][0],'answer':ASSIGNMENT[1][0],'solutionOrigin':'textbook answer','sourceReferences':[{'pdfPage':21,'printedPage':33}]}]}])
    checkpoint(21,'corrected_verified',[r['id'] for r in records],
      'Original spread inspected at2.5x. Uniform-velocity potential definition and Eq11.28 preserved. Point-charge Example11.6 complete solution and M/O/N2cm/1cm SVG, Assignment11.3/source10cm answer, electron-volt definition/conversion/multiples, and second printed Example11.6 particle-energy full solution transcribed with aligned translations. Duplicate source example numbering preserved with editorial clarification and distinct IDs. Legacy11.11 retired and11.12 trimmed to capacitor PDF22.',printed_pages=[32,33])
