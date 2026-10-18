"""PDF190 full transcription; source's inconsistent nuclides intentionally retained."""
from class12_source_review import upsert, section, sync_companions, shared_class_data_lock
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, arrow, nucleon, burst, wave, svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];ROWS={}
def add(kind,en,ur,ps):
    L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
def eq(value):
    value=r'\('+value+r'\)';add('equation',value,value,value)
def table(rows):
    indices=[]
    for en,ur,ps in rows:
        index=len(T);indices.append(index);ROWS[index]=en
        T.append(tuple(' — '.join(row) for row in [en,ur,ps]))
    L.append({'type':'table','indices':indices})
def table_row(label,formula,energy,twice=False,twice_energy=False):
    f=r'\('+formula+r'\)' if formula else ''
    if label.startswith('step '):
        n=label.split()[1];labels=[label,'مرحلہ '+n,'پړاو '+n]
    else: labels=[label,'کل' if label else '', 'ټول' if label else '']
    suffix=['(twice)','(دو بار)','(دوه ځله)']
    return tuple([labels[i], f+(' '+suffix[i] if twice else ''),energy+(' '+suffix[i] if twice_energy else '')] for i in range(3))

add('paragraph','A deuteron produced in the above reaction may combine with other proton as',
 'مندرجہ بالا تعامل میں پیدا ہونے والا ڈیوٹیرون دوسرے پروٹون کے ساتھ اس طرح مل سکتا ہے',
 'په پورتني تعامل کې تولید شوی ډیوټرون له بل پروتون سره داسې یوځای کېدای شي')
eq(r'{}^{1}_{1}\mathrm{H}+{}^{2}_{1}\mathrm{H}\rightarrow{}^{3}_{2}\mathrm{He}+\gamma')
add('paragraph','Finally, two such reactions can combine to form helium-4 with the release of two protons as',
 'آخر میں، ایسے دو تعاملات مل کر دو پروٹون خارج کرتے ہوئے ہیلیم-4 بنا سکتے ہیں، اس طرح',
 'په پای کې، دوه داسې تعاملونه سره یوځای کېدای شي او د دوو پروتونونو په خوشې کولو سره هیلیم-4 داسې جوړ کړي')
eq(r'{}^{3}_{2}\mathrm{He}+{}^{3}_{2}\mathrm{He}\rightarrow{}^{4}_{2}\mathrm{He}+{}^{1}_{1}\mathrm{H}+{}^{1}_{1}\mathrm{H}+\gamma')
add('paragraph','The total energy released in this process is 24.7 MeV which is the difference between the masses of 4 protons and mass of alpha particle plus two positrons.',
 'اس عمل میں خارج ہونے والی کل توانائی 24.7 MeV ہے، جو 4 پروٹونوں کی کمیتوں اور ایک الفا ذرے اور دو پوزیٹرونوں کی مجموعی کمیت کے درمیان فرق ہے۔',
 'په دې بهیر کې خوشې شوې ټوله انرژي 24.7 MeV ده، چې د 4 پروتونونو د کتلو او د الفا ذرې او دوو پوزیترونونو د ټولې کتلې ترمنځ توپیر دی.')
header=(['','Reaction','Energy released'],['','تعامل','خارج ہونے والی توانائی'],['','تعامل','خوشې شوې انرژي'])
table([header,
 table_row('step 1',r'{}^{1}_{1}\mathrm{H}+{}^{1}_{1}\mathrm{H}\rightarrow{}^{2}_{1}\mathrm{H}+\beta^{+}+\nu','0.42 MeV',True,True),
 table_row('step 2',r'{}^{1}_{1}\mathrm{He}+{}^{2}_{1}\mathrm{He}\rightarrow{}^{3}_{2}\mathrm{He}+\gamma','5.49 MeV',True,True),
 table_row('step 3',r'{}^{3}_{2}\mathrm{He}+{}^{3}_{2}\mathrm{He}\rightarrow{}^{4}_{2}\mathrm{He}+{}^{1}_{1}\mathrm{H}+{}^{1}_{1}\mathrm{H}+\gamma','12.85 MeV'),
 table_row('step 4',r'{}^{0}_{1}\beta+{}^{0}_{-1}\beta\rightarrow2\gamma','1.02 MeV',True,True),
 table_row('Total',r'4\,{}^{1}_{1}\mathrm{H}\rightarrow{}^{4}_{2}\mathrm{He}+2\,{}^{0}_{1}\beta+2\nu+7\gamma','26.71 MeV')])
add('heading','B. CARBON CYCLE','B. کاربن چکر','B. د کاربن دوره')
add('paragraph','The carbon cycle proceeds as shown in figure 20.21.',
 'کاربن چکر اسی طرح آگے بڑھتا ہے جیسے شکل 20.21 میں دکھایا گیا ہے۔',
 'د کاربن دوره په هغه ډول پر مخ ځي چې په 20.21 شکل کې ښودل شوې ده.')
add('heading','FIGURE 20.21','شکل 20.21','شکل 20.21')
L.append({'type':'visual','blockId':'phys20-190-carbon-chain'})
add('paragraph','The carbon-nitrogen chain','کاربن-نائٹروجن سلسلہ','د کاربن-نایتروجن ځنځیر')
add('paragraph','Since proton-proton cycle is more efficient at low temperature so stars cooler as compared to sun may fuel their energy from proton-proton cycle. Whereas carbon cycle is more efficient at high temperature therefore bright stars at high temperature will favor carbon cycle.',
 'چونکہ پروٹون-پروٹون چکر کم درجہ حرارت پر زیادہ مؤثر ہوتا ہے، اس لیے سورج کے مقابلے میں ٹھنڈے ستارے اپنی توانائی پروٹون-پروٹون چکر سے حاصل کر سکتے ہیں۔ جبکہ کاربن چکر بلند درجہ حرارت پر زیادہ مؤثر ہوتا ہے، اس لیے بلند درجہ حرارت والے روشن ستاروں میں کاربن چکر کو ترجیح حاصل ہوگی۔',
 'څرنګه چې د پروتون-پروتون دوره په ټیټه تودوخه کې ډېره اغېزمنه ده، نو د لمر په پرتله ساړه ستوري خپله انرژي د پروتون-پروتون له دورې څخه ترلاسه کولی شي. خو د کاربن دوره په لوړه تودوخه کې ډېره اغېزمنه ده؛ نو په لوړه تودوخه کې روښانه ستوري به د کاربن دورې ته لومړیتوب ورکړي.')
table([header,
 table_row('step 1',r'{}^{1}_{1}\mathrm{H}+{}^{12}_{6}\mathrm{C}\rightarrow{}^{12}_{7}\mathrm{N}^{*}','1.95 MeV'),
 table_row('step 2',r'{}^{12}_{7}\mathrm{N}\rightarrow{}^{13}_{6}\mathrm{C}+\beta^{+}+\nu','1.20 MeV'),
 table_row('step 3',r'{}^{1}_{1}\mathrm{H}+{}^{13}_{6}\mathrm{C}\rightarrow{}^{14}_{7}\mathrm{N}+\gamma','7.54 MeV'),
 table_row('step 4',r'{}^{1}_{1}\mathrm{H}+{}^{14}_{7}\mathrm{N}\rightarrow{}^{15}_{8}\mathrm{O}^{*}+\gamma','7.35 MeV'),
 table_row('step 5',r'{}^{15}_{8}\mathrm{O}\rightarrow{}^{15}_{7}\mathrm{N}+\beta^{+}+\nu','1.73 MeV'),
 table_row('step 6',r'{}^{1}_{1}\mathrm{H}+{}^{15}_{7}\mathrm{N}\rightarrow{}^{12}_{6}\mathrm{C}+{}^{4}_{2}\mathrm{He}','4.96 MeV'),
 table_row('step 7',r'{}^{0}_{1}\beta+{}^{0}_{-1}\beta\rightarrow2\gamma','1.02 MeV',True,True),
 table_row('Total','','26.73 MeV')])
add('paragraph','The energy liberated in fusion of light nuclei into heavier nuclei is called thermonuclear energy, especially when it is achieved at earth. However this energy cannot be used in controlled manner in self sustaining cycle. Worldwide effort is underway to harness energy from fusion in laboratory, after the test of first successful Thermonuclear Bomb (hydrogen bomb).',
 'ہلکے نیوکلئیسوں کے امتزاج سے بھاری نیوکلئیس بنتے وقت خارج ہونے والی توانائی کو حرارتی نیوکلیائی توانائی کہتے ہیں، خصوصاً جب یہ زمین پر حاصل کی جائے۔ تاہم اس توانائی کو خود برقرار رہنے والے چکر میں قابو شدہ انداز سے استعمال نہیں کیا جا سکتا۔ پہلے کامیاب حرارتی نیوکلیائی بم (ہائیڈروجن بم) کے تجربے کے بعد، تجربہ گاہ میں امتزاج سے توانائی حاصل کرنے کی دنیا بھر میں کوشش جاری ہے۔',
 'د سپکو هستو له امتزاج څخه د درنو هستو د جوړېدو پر مهال خوشې شوې انرژي حرارتي هستوي انرژي بلل کېږي، په ځانګړي ډول کله چې پر ځمکه ترلاسه شي. خو دا انرژي په خپله دوام کوونکې دوره کې په کنټرول شوې بڼه نه شي کارېدای. د لومړي بریالي حرارتي هستوي بم (هایدروجن بم) تر ازموینې وروسته، په لابراتوار کې له امتزاج څخه د انرژۍ د ترلاسه کولو لپاره په ټوله نړۍ کې هڅې روانې دي.')
add('heading','20.15 RADIATION EXPOSURE','20.15 تابکاری کا سامنا','20.15 وړانګو ته مخامخ کېدل')
add('paragraph','All living creatures, from the beginning of time, have been, and are still being, exposed to radiation. when a radiation detector is used it will record these radiations called natural background radiation, it comes from three sources',
 'وقت کے آغاز سے تمام جاندار تابکاری کا سامنا کرتے آئے ہیں اور اب بھی کر رہے ہیں۔ جب تابکاری کا سراغ رساں آلہ استعمال کیا جاتا ہے تو وہ اس تابکاری کو ریکارڈ کرتا ہے، جسے قدرتی پس منظر کی تابکاری کہتے ہیں؛ یہ تین ذرائع سے آتی ہے',
 'د وخت له پیل راهیسې ټول ژوندي موجودات له وړانګو سره مخامخ شوي او اوس هم ورسره مخامخ کېږي. کله چې د وړانګو کشفوونکی وکارول شي، هغه دا وړانګې ثبتوي چې د طبیعي شالید وړانګې بلل کېږي؛ دا له دریو سرچینو راځي')
add('heading','A. COSMIC RADIATION','A. کائناتی تابکاری','A. کایناتي وړانګې')
add('paragraph','The earth, and all living things on it, are constantly bombarded by radiation from space, The dose from cosmic radiation varies in different parts of the world due to differences in elevation and to the effects of the earth’s magnetic field.',
 'زمین اور اس پر موجود تمام جاندار مسلسل خلا سے آنے والی تابکاری کی زد میں رہتے ہیں۔ بلندی کے فرق اور زمین کے مقناطیسی میدان کے اثرات کے باعث دنیا کے مختلف حصوں میں کائناتی تابکاری کی خوراک مختلف ہوتی ہے۔',
 'ځمکه او ټول ژوندي موجودات چې پرې اوسېږي، په پرله پسې ډول له فضا څخه د وړانګو تر بمبار لاندې دي. د لوړوالي د توپیرونو او د ځمکې د مقناطیسي ډګر د اغېزو له امله د نړۍ په بېلابېلو برخو کې د کایناتي وړانګو دوز توپیر لري.')
add('heading','B. INTERNAL RADIATION','B. اندرونی تابکاری','B. داخلي وړانګې')
add('paragraph','All people also have radioactive potassium-40, carbon-14, lead-210, and other isotopes inside their bodies from birth.',
 'تمام لوگوں کے جسموں میں پیدائش ہی سے تابکار پوٹاشیم-40، کاربن-14، سیسہ-210 اور دیگر آئسوٹوپس بھی موجود ہوتے ہیں۔',
 'ټول خلک له زېږون راهیسې په خپلو بدنونو کې راډیواکټیف پوتاشیم-40، کاربن-14، سرب-210 او نور ایزوټوپونه هم لري.')

def carbon(lang):
    proton={'en':'Proton','ur':'پروٹون','ps':'پروتون'}[lang]
    out=''
    nodes=[(70,100,12,'C','#c084fc'),(230,135,13,'N','#fdba74'),(230,245,13,'C','#c084fc'),(420,290,14,'N','#fdba74'),(600,350,15,'O','#f9a8d4'),(600,470,15,'N','#f9a8d4'),(805,510,12,'C','#c084fc')]
    for x,y,m,s,c in nodes:
        out+=f'<circle cx="{x}" cy="{y}" r="18" fill="{c}" stroke="#172033" stroke-width="1.6"/>'
        lx,ly=(x-48,y+5) if (m,s) in [(13,'C'),(15,'N')] else (x,y-28)
        if (x,y)==(805,510):lx,ly=x+48,y+5
        out+=f'<text x="{lx}" y="{ly}" font-family="Arial,sans-serif" font-size="18" text-anchor="middle"><tspan baseline-shift="super" font-size="12">{m}</tspan>{s}</text>'
    for px,py,bx,by,target in [(75,190,145,135,(210,135)),(240,350,328,288,(399,290)),(424,407,512,347,(579,350)),(603,565,715,510,(784,510))]:
        out+=nucleon(px,py)+text(px,py+30,proton,16)+text(px,py-21,'¹H',18)
        out+=arrow(px+12,py-9,bx-17,by+10)+burst(bx,by)+wave(bx+7,by-18,bx+80,by-76)+arrow(bx+23,by,target[0],target[1])
    for a,b in [((87,109),(126,128)),((245,258),(307,282)),((438,300),(490,342)),((619,482),(694,505))]:out+=arrow(*a,*b)
    for x,y,end in [(230,156,224),(600,371,449)]:
        out+=arrow(x,y,x,end)+arrow(x+15,(y+end)/2,x+65,(y+end)/2)
        out+=f'<circle cx="{x+79}" cy="{(y+end)/2}" r="5" fill="#e11d48"/>'+text(x+80,(y+end)/2-14,'β⁺',18)
    out+='<path d="M805 488 C802 50 300 8 91 90" fill="none" stroke="#7f1d1d" stroke-width="2"/>'+arrow(107,83,89,91)
    return svg(out,900,615,{'en':'The carbon-nitrogen chain as printed, with carbon-12 return and all proton, beta and gamma labels','ur':'چھپا ہوا کاربن-نائٹروجن سلسلہ، کاربن-12 کی واپسی اور تمام پروٹون، بیٹا اور گاما لیبل','ps':'چاپ شوی کاربن-نایتروجن ځنځیر، د کاربن-12 راستنېدل او د ټولو پروتونونو، بېټا او ګاما نښې'}[lang])

def ref(n):return {'pdfPage':190,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-proton-and-carbon-fusion-cycles-radiation-exposure-368-369','title':'Fusion cycles, energy and radiation exposure','kind':'lesson','pdfPage':190,'printedPage':368,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
sec=section(record,T,L,('امتزاج کے چکر، توانائی اور تابکاری کا سامنا','د امتزاج دورې، انرژي او وړانګو ته مخامخ کېدل'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceTableRows=ROWS,sourceReferences=[ref(368),ref(369)],sourceBlocks=[{'id':'phys20-190-carbon-chain','type':'figure','sourceFigure':'20.21','svg':carbon('en'),'svgUrdu':carbon('ur'),'svgPashto':carbon('ps')}])
issues=[
 'Proton-cycle text gives 24.7 MeV but its table gives 26.71 MeV; both retained.',
 'Printed368 proton-cycle table step2 writes ¹₁He + ²₁He, while the preceding prose equation writes ¹₁H + ²₁H. Both source forms retained.',
 'Printed369 carbon table uses ¹²₇N* in step1 and ¹²₇N in step2, while Figure20.21 labels nitrogen-13. Printed starred nuclides, charges, reaction totals and both source variants retained.',
 'Figure20.21 prints gamma emission at the final carbon-12 return and omits the helium-4 output that appears in carbon-table step6. Figure and table retained separately as printed.'
]
sec['sourceIssues']=issues
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,definitions=[{'term':'Thermonuclear energy','definition':'The energy liberated in fusion of light nuclei into heavier nuclei is called thermonuclear energy, especially when it is achieved at earth.','sourceReferences':[ref(369)]}])
    stage_reference(190,record,'Reinspected PDF190 in full and both energy tables at240dpi. Restored all prose paragraphs, equations, numbered table rows, energy entries, headings and caption. Kept the source’s proton-table He symbols, carbon-table N-12/starred nuclides, beta signs, 24.7/26.71 discrepancy and gamma/helium difference. Recreated the complete Figure20.21 chain and carbon return with all source labels. All prose and table cells have aligned Urdu/Pashto translations; source defects remain unresolved.',issues)
    print('PDF190 source correction staged with printed inconsistencies retained.')
