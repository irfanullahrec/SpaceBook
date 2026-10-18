import math
from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
from class12_physics_field_figures import arrow
SERIES=[
 ('combination. A battery of voltage V is connected between points A and B. In this type of combination the equivalent capacitance is given by','اتصال۔ وولٹیج V کی بیٹری نقاط A اور B کے درمیان جوڑی جاتی ہے۔ اس قسم کے اتصال کی مساوی گنجائش یہ ہے','نښلون. د V ولټاژ بېټرۍ د A او B نقطو ترمنځ نښلول کېږي. په دې ډول نښلون کې معادل ظرفیت دا دی'),
 (r'\(\frac1{C_e}=\frac1{C_1}+\frac1{C_2}+\frac1{C_3}\) ...(11.34)',)*3,
]
PARALLEL=[
 ('PARALLEL COMBINATION OF CAPACITORS','کیپیسٹروں کا متوازی اتصال','د کپاسیټرونو موازي نښلون'),
 ('When the battery is connected to the parallel plates of a capacitor as shown in Figure 11.25. The equivalent capacitance Ce of this combination is given by','جب بیٹری کو کیپیسٹر کی متوازی پلیٹوں سے جوڑا جائے، جیسا کہ شکل 11.25 میں ہے، تو اس مجموعے کی مساوی گنجائش Ce یہ ہے','کله چې بېټرۍ د کپاسیټر له موازي تختو سره ونښلول شي، لکه په شکل 11.25 کې، د دې ترکیب معادل ظرفیت Ce داسې ورکول کېږي'),
 (r'\(C_e=C_1+C_2+C_3\) ...(11.35)',)*3,
 ('[Editorial clarification: the source caption under Figure 11.25 reads “Series combination of capacitors,” although the diagram and heading show a parallel combination. The printed caption is preserved.]','[ادارتی وضاحت: شکل 11.25 کے نیچے اصل عنوان ”کیپیسٹروں کا سلسلہ وار اتصال“ ہے، اگرچہ شکل اور عنوان متوازی اتصال دکھاتے ہیں۔ چھپا ہوا عنوان محفوظ ہے۔]','[د سمونوال وضاحت: د شکل 11.25 لاندې چاپ شوی سرلیک «د کپاسیټرونو لړۍ‌يي نښلون» دی، که څه هم شکل او سرلیک موازي نښلون ښيي. چاپ شوی سرلیک ساتل شوی دی.]'),
]
POLARIZATION=[
 ('In the previous section we explored the dependence of charge storing capacity of a capacitor on the dielectric material. A dielectric is an electrical insulator that can be polarized by an applied electric field.','پچھلے حصے میں ہم نے کیپیسٹر کی بار ذخیرہ کرنے کی صلاحیت کا ڈائی الیکٹرک مادے پر انحصار دیکھا۔ ڈائی الیکٹرک ایک برقی غیر موصل ہے جسے لگایا گیا برقی میدان قطبی بنا سکتا ہے۔','په مخکینۍ برخه کې مو د کپاسیټر د چارج زېرمه کولو وړتیا پر ډای الکټریک مادې پورې تړاو وڅېړه. ډای الکټریک برېښنايي عایق دی چې د لګېدلي برېښنايي میدان په وسیله قطبي کېدای شي.'),
 ('When a dielectric substance is placed between two parallel plates with an applied electric field. The electric field distorts the negatively charged particles towards the positive plate and the positive charge particles towards the negative plate as shown in figure 11.26. The slight separation of charge makes one side of the atom somewhat positive and the opposite side somewhat negative. This phenomenon is known as electric polarization.','جب برقی میدان کے ساتھ ڈائی الیکٹرک مادہ دو متوازی پلیٹوں کے درمیان رکھا جائے، تو برقی میدان منفی بار والے ذرات کو مثبت پلیٹ اور مثبت بار والے ذرات کو منفی پلیٹ کی طرف کھینچ کر ان کی ترتیب بگاڑتا ہے، جیسا کہ شکل 11.26 میں ہے۔ بار کی معمولی علیحدگی ایٹم کے ایک طرف کو کچھ مثبت اور دوسری طرف کو کچھ منفی بناتی ہے۔ اس مظہر کو برقی قطبیت کہتے ہیں۔','کله چې ډای الکټریک ماده د لګېدلي برېښنايي میدان په شتون کې د دوو موازي تختو ترمنځ کېښودل شي، برېښنايي میدان منفي چارج لرونکي ذرات د مثبتې تختې او مثبت ذرات د منفي تختې پر لور بې‌ځایه کوي، لکه په شکل 11.26 کې. د چارج لږه بېلتون د اتوم یوه خوا لږه مثبته او مقابل خوا لږه منفي کوي. دې پدیدې ته برېښنايي قطبي کېدل ویل کېږي.'),
]
DIPOLE=[
 ('ELECTRIC DIPOLE','برقی ثنائیہ','برېښنايي ډایپول'),
 ('We know that dielectric materials are made up of the two types of molecules; polar and non polar molecules. A polar molecule like water behaves as a permanent dipole; although electrically neutral as a whole.','ہم جانتے ہیں کہ ڈائی الیکٹرک مواد دو قسم کے سالمات، قطبی اور غیر قطبی سالمات، پر مشتمل ہیں۔ پانی جیسا قطبی سالمہ مستقل ثنائیے کی طرح برتاؤ کرتا ہے، اگرچہ مجموعی طور پر برقی طور پر غیر جانب دار ہوتا ہے۔','پوهېږو چې ډای الکټریک مواد له دوو ډولو مالیکولونو، قطبي او غیرقطبي، جوړ دي. د اوبو په څېر قطبي مالیکول دایمي ډایپول ته ورته چلند کوي، که څه هم په ټولیز ډول برېښنايي بې‌طرفه دی.'),
 ('On the other hand, a non-polar molecule like nitrogen has no electric dipole moment in the absence of an external field. In the presence of electric field negative charges in non-polar substance displaces to the opposite of electric field E as shown in Fig11.26. Dipole moments occur when there is a separation of charge. Under the action of external field the centres of negative and positive charges shift and form dipoles. The dipole moment is a measure of the polarity of the molecule.','دوسری طرف، نائٹروجن جیسا غیر قطبی سالمہ بیرونی میدان نہ ہونے پر برقی ثنائیہ مومنٹ نہیں رکھتا۔ برقی میدان موجود ہونے پر غیر قطبی مادے کے منفی بار، برقی میدان E کی مخالف سمت میں سرکتے ہیں، جیسا کہ شکل 11.26 میں ہے۔ بار کی علیحدگی سے ثنائیہ مومنٹ پیدا ہوتا ہے۔ بیرونی میدان کے عمل سے مثبت اور منفی باروں کے مراکز سرکتے ہیں اور ثنائیے بناتے ہیں۔ ثنائیہ مومنٹ سالمے کی قطبیت کا پیمانہ ہے۔','له بلې خوا، د نایتروجن په څېر غیرقطبي مالیکول د بهرني میدان په نشتون کې برېښنايي ډایپولي مومنټ نه لري. د برېښنايي میدان په شتون کې په غیرقطبي ماده کې منفي چارجونه د برېښنايي میدان E مخالف لوري ته بې‌ځایه کېږي، لکه په شکل 11.26 کې. د چارجونو د بېلتون پر مهال ډایپولي مومنټ رامنځته کېږي. د بهرني میدان تر اغېز لاندې د مثبت او منفي چارجونو مرکزونه خوځېږي او ډایپولونه جوړوي. ډایپولي مومنټ د مالیکول د قطبیت کچه ده.'),
 ('The system in which two charges of equal magnitude but of opposite sign separated by the distance d, are present is termed as a dipole. Electric dipole moment is represented by P, which is equal to the product of the charge Q present in the dipole and the distance d between the two charges of the dipole.','ایسا نظام جس میں برابر مقدار مگر مخالف علامت کے دو بار، فاصلے d سے جدا ہوں، ثنائیہ کہلاتا ہے۔ برقی ثنائیہ مومنٹ کو P سے ظاہر کرتے ہیں، جو ثنائیے کے بار Q اور دونوں باروں کے درمیان فاصلے d کے حاصل ضرب کے برابر ہے۔','هغه سیستم چې دوه برابر مقدار خو مخالفې نښې لرونکي چارجونه د d واټن په اندازه سره بېل ولري، ډایپول بلل کېږي. د برېښنايي ډایپولي مومنټ نښه P ده، چې د ډایپول د چارج Q او د دواړو چارجونو ترمنځ د d واټن حاصل ضرب دی.'),
 (r'\(P=|Qd|\) ...(11.36)',)*3,
 ('Where P is a vector quantity.','جہاں P سمتی مقدار ہے۔','دلته P ویکټوري مقدار دی.'),
]
EXAMPLE=[('Figure shows a different combination of capacitors, if the total charge is 600μC. Then determine the values of V1, and C2.','شکل کیپیسٹروں کا ایک مختلف اتصال دکھاتی ہے۔ اگر کل بار 600 مائیکروکولومب ہو، تو V1 اور C2 معلوم کریں۔','شکل د کپاسیټرونو یو بل ترکیب ښيي. که ټول چارج 600 مایکروکولم وي، د V1 او C2 ارزښتونه معلوم کړئ.')]

def series(lang):
    body='<path d="M25 75H305V165H25Z M25 75L38 60H292L305 75" fill="none" stroke="#334155"/><path d="M25 165V75M305 75V165" stroke="#334155"/>'
    for x,label in [(85,'C₁'),(165,'C₂'),(245,'C₃')]:
        body+=f'<rect x="{x-8}" y="87" width="8" height="50" fill="#fef3c7" stroke="#334155"/><rect x="{x+8}" y="87" width="8" height="50" fill="#fef3c7" stroke="#334155"/><text x="{x-12}" y="80">{label}</text><text x="{x-18}" y="107">+</text><text x="{x+19}" y="107">−</text>'
    body+='<path d="M143 165V205M163 177V193" stroke="#334155" stroke-width="3"/><text x="176" y="202">V</text><text x="12" y="70">A</text><text x="309" y="70">B</text>'
    cap={'en':'FIGURE 11.24: Series combination of capacitors','ur':'شکل 11.24: کیپیسٹروں کا سلسلہ وار اتصال','ps':'شکل 11.24: د کپاسیټرونو لړۍ‌يي نښلون'}[lang]
    return '<figure>'+svg(body,330,225,'Three capacitors connected in series between A and B across a battery V')+'<figcaption>'+cap+'</figcaption></figure>'

def parallel(lang):
    body='<path d="M35 60H330M35 190H330M35 60V190M330 60V190" fill="none" stroke="#334155" stroke-width="2"/><path d="M164 195V230M184 207V219" stroke="#334155" stroke-width="3"/><text x="192" y="230">V</text>'
    for x,label in [(95,'C₁'),(185,'C₂'),(275,'C₃')]:
        body+=f'<path d="M{x-8} 60V100M{x+8} 60V100M{x-8} 150V190M{x+8} 150V190" stroke="#334155" stroke-width="2"/><path d="M{x-10} 100H{x+10}V150H{x-10}Z" fill="#fef3c7" stroke="#334155"/><path d="M{x} 65V96M{x} 154V186" stroke="#b91c1c"/>'+arrow(x,96,0,1,'#b91c1c')+arrow(x,154,0,1,'#b91c1c')+f'<text x="{x-13}" y="126">{label}</text>'
    body+='<text x="22" y="52">A</text><text x="332" y="52">B</text>'
    cap={'en':'FIGURE 11.25: Series combination of capacitors (source caption)','ur':'شکل 11.25: کیپیسٹروں کا سلسلہ وار اتصال (اصل عنوان)','ps':'شکل 11.25: د کپاسیټرونو لړۍ‌يي نښلون (چاپ شوی سرلیک)'}[lang]
    return '<figure>'+svg(body,360,255,'Three capacitors connected in parallel between A and B across battery V; source caption says series')+'<figcaption>'+cap+'</figcaption></figure>'

def molecules(lang):
    body='<rect x="25" y="25" width="28" height="295" fill="#ec4899"/><rect x="346" y="25" width="28" height="295" fill="#38bdf8"/>'
    for y in range(40,310,18):body+=f'<text x="31" y="{y}">+</text><text x="352" y="{y}">−</text>'
    for y in range(50,300,34):
        for x in [95,155,215,275]:
            body+=f'<ellipse cx="{x}" cy="{y}" rx="22" ry="10" fill="#f9a8d4" stroke="#334155"/><text x="{x-15}" y="{y+5}">−</text><text x="{x+6}" y="{y+5}">+</text>'
    body+='<text x="90" y="345">Dielectric</text><path d="M67 174H324" stroke="#334155" stroke-dasharray="4 5"/>'+arrow(324,174,1,0,'#334155')+'<text x="179" y="165">E⃗</text>'
    cap={'en':'FIGURE 11.26: Polarization of a dielectric in an electric field','ur':'شکل 11.26: برقی میدان میں ڈائی الیکٹرک کی قطبیت','ps':'شکل 11.26: په برېښنايي میدان کې د ډای الکټریک قطبي کېدل'}[lang]
    return '<figure>'+svg(body,400,370,'Dielectric molecules polarized between positive and negative plates, bound charges at surfaces')+'<figcaption>'+cap+'</figcaption></figure>'

def dipole(lang):
    body='<rect x="20" y="25" width="28" height="250" fill="#ec4899"/><rect x="326" y="25" width="28" height="250" fill="#38bdf8"/>'
    for y in range(40,270,20):body+=f'<text x="26" y="{y}">+</text><text x="332" y="{y}">−</text>'
    for y in range(55,260,28):
        for x in [110,185,260]:body+=f'<ellipse cx="{x}" cy="{y}" rx="22" ry="10" fill="#f9a8d4" stroke="#334155"/><text x="{x-13}" y="{y+5}">+</text><text x="{x+6}" y="{y+5}">−</text>'
    body+='<path d="M203 47V243" stroke="#334155" stroke-dasharray="3 4"/>'+arrow(203,243,0,1,'#334155')+'<text x="210" y="147">d</text><text x="373" y="82">FIGURE 11.26</text>'
    return '<figure>'+svg(body,430,300,'Permanent and induced dipole molecules between charged plates, separation d')+'<figcaption>FIGURE 11.26</figcaption></figure>'

if __name__=='__main__':
    specs=[('phys12-front-series38','Series combination of capacitors',38,SERIES,('کیپیسٹروں کا سلسلہ وار اتصال','د کپاسیټرونو لړۍ‌يي نښلون'),series,[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'visual'}]),('phys12-front-parallel38','PARALLEL COMBINATION OF CAPACITORS',38,PARALLEL,('کیپیسٹروں کا متوازی اتصال','د کپاسیټرونو موازي نښلون'),parallel,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'visual'},{'type':'paragraph','indices':[3]}]),('phys12-front-polarization38','11.11 ELECTRIC POLARIZATION',38,POLARIZATION,('11.11 برقی قطبیت','11.11 برېښنايي قطبي کېدل'),molecules,[{'type':'paragraph','indices':[0,1]},{'type':'visual'}]),('phys12-front-dipole39','ELECTRIC DIPOLE',39,DIPOLE,('برقی ثنائیہ','برېښنايي ډایپول'),dipole,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1,2]},{'type':'visual'},{'type':'paragraph','indices':[3]},{'type':'equation','indices':[4]},{'type':'paragraph','indices':[5]}]),('phys12-front-example11739','EXAMPLE 11.7',39,EXAMPLE,('مثال 11.7','بېلګه 11.7'),None,[{'type':'paragraph','indices':[0]}])]
    records=[];sections=[]
    for identity,title,page,pairs,titles,visual,layout in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':24,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        if visual:revised.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'));revised['content']+=visual('en')
        for para in revised['paras']:
            if para['text'].startswith('[Editorial'):para.update(isEditorial=True,originalText=None)
        records.append(record);sections.append(revised)
    upsert(records,sections)
    sync_companions(retire_sections=['11.14'],formulas=[{'id':'phys12-eq-11.34','name':'Series capacitance','number':'11.34','formula':SERIES[1][0],'latex':r'\frac1{C_e}=\frac1{C_1}+\frac1{C_2}+\frac1{C_3}','sourceReferences':[{'pdfPage':24,'printedPage':38}]},{'id':'phys12-eq-11.35','name':'Parallel capacitance','number':'11.35','formula':PARALLEL[2][0],'latex':r'C_e=C_1+C_2+C_3','sourceReferences':[{'pdfPage':24,'printedPage':38}]},{'id':'phys12-eq-11.36','name':'Electric dipole moment','number':'11.36','formula':DIPOLE[4][0],'latex':r'P=|Qd|','sourceReferences':[{'pdfPage':24,'printedPage':39}]}],definitions=[{'term':'Dielectric','def':POLARIZATION[0][0],'sourceReferences':[{'pdfPage':24,'printedPage':38}]},{'term':'Electric dipole','def':DIPOLE[3][0],'sourceReferences':[{'pdfPage':24,'printedPage':39}]}])
    checkpoint(24,'corrected_verified',[r['id'] for r in records],'Original spread inspected at2.5x. Series and parallel capacitor connection paragraphs and Eqs11.34–11.35 preserved. Fig11.25 visibly captions a parallel diagram as series; source caption retained and editorially identified. Electric polarization, dipole, Eq11.36 and start of Example11.7 transcribed and translated. Figures11.24–11.26 replaced by coded series, parallel, and polarized-molecule diagrams. Covered legacy capacitor combination section retired; Example11.7 continuation on PDF25 remains to audit.',printed_pages=[38,39])
