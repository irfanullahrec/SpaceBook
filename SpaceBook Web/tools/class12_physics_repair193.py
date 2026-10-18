"""PDF193: full force table and every value in the elementary-particle chart."""
from class12_source_review import upsert, section, shared_class_data_lock
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];ROWS={}
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
add('heading','D. GRAVITATIONAL FORCE','D. کششِ ثقل کی قوت','D. د جاذبې ځواک')
add('paragraph',r'Gravity is long range force and is the weakest of the four fundamental forces having relative strength of \(10^{-43}\), yet it is the dominant force in the universe for shaping the large scale structure of galaxies, stars, etc. Viewed as an exchange force, the massless exchange particle is called the graviton (however it is not confirmed yet).',
 r'کششِ ثقل دور رس قوت ہے اور چار بنیادی قوتوں میں سب سے کمزور ہے، جس کی نسبتی شدت \(10^{-43}\) ہے، پھر بھی کائنات میں کہکشاؤں، ستاروں وغیرہ کی بڑے پیمانے کی ساخت تشکیل دینے میں یہی غالب قوت ہے۔ اسے تبادلے کی قوت کے طور پر دیکھا جائے تو کمیت سے خالی تبادلہ کرنے والے ذرے کو گریویٹون کہتے ہیں (تاہم ابھی اس کی تصدیق نہیں ہوئی)۔',
 r'جاذبه اوږد واټن لرونکی ځواک دی او د څلورو بنسټیزو ځواکونو تر ټولو کمزوری ځواک دی، چې نسبي شدت یې \(10^{-43}\) دی. خو بیا هم په کایناتو کې د کهکشانونو، ستورو او نورو د لویې کچې جوړښت په ټاکلو کې غالب ځواک دی. که د تبادلې ځواک وګڼل شي، بې کتلې تبادله کېدونکې ذره یې ګرېویټون بلل کېږي (خو تر اوسه نه ده تایید شوې).')
add('heading','Table 20.5 PARTICLE INTERACTIONS','جدول 20.5 ذرات کے تعاملات','جدول 20.5 د ذرو تعاملونه')
rows=[
 (['Force','Particle acted on by force','Relative strength','Typical Lifetimes for decay via given interaction (s)','Force carrying exchange particle'],['قوت','وہ ذرہ جس پر قوت عمل کرتی ہے','نسبتی شدت','دیے گئے تعامل سے زوال کی عام مدتِ حیات (s)','قوت لے جانے والا تبادلہ ذرہ'],['ځواک','هغه ذره چې ځواک پرې عمل کوي','نسبي شدت','د ورکړل شوي تعامل له لارې د زوال معمول عمرونه (s)','د ځواک لېږدوونکې تبادله کېدونکې ذره']),
 (['Strong','Quarks, hadrons','1',r'\(10^{-20}\)','gluons'],['قوی','کوارکس، ہیڈرانز','1',r'\(10^{-20}\)','گلوآنز'],['قوي','کوارکونه، هاډرونونه','1',r'\(10^{-20}\)','ګلوونونه']),
 (['Electromagnetic','Charge particles',r'\(10^{-2}\)',r'\(10^{-16}\)','photons'],['برق مقناطیسی','بار دار ذرات',r'\(10^{-2}\)',r'\(10^{-16}\)','فوٹونز'],['برېښنا مقناطیسي','چارج لرونکې ذرې',r'\(10^{-2}\)',r'\(10^{-16}\)','فوټونونه']),
 (['Weak','Quarks, Leptons',r'\(10^{-7}\)',r'\(10^{-10}\)',r'\(\mathrm{W}^{\pm}\) and \(\mathrm{Z}^{0}\) bosons'],['کمزور','کوارکس، لیپٹونز',r'\(10^{-7}\)',r'\(10^{-10}\)',r'\(\mathrm{W}^{\pm}\) اور \(\mathrm{Z}^{0}\) بوزونز'],['کمزوری','کوارکونه، لېپټونونه',r'\(10^{-7}\)',r'\(10^{-10}\)',r'\(\mathrm{W}^{\pm}\) او \(\mathrm{Z}^{0}\) بوزونونه']),
 (['Gravitational','All particles',r'\(10^{-43}\)','?','gravitons'],['کششِ ثقل','تمام ذرات',r'\(10^{-43}\)','?','گریویٹونز'],['جاذبه','ټولې ذرې',r'\(10^{-43}\)','?','ګرېویټونونه'])]
indices=[]
for row in rows:
    index=len(T);indices.append(index);ROWS[index]=row[0];T.append(tuple(' — '.join(cells) for cells in row))
L.append({'type':'table','indices':indices})
add('heading','20.19 BUILDING BLOCKS OF MATTER','20.19 مادے کے بنیادی اجزا','20.19 د مادې بنسټیزې برخې')
add('paragraph',r'Beginning in about 1945, many new particles were discovered in experiments involving high-energy collisions between known particles. Such particles are highly unstable and have very short half-lives, ranging between \(10^{6}\) and \(10^{23}\ \mathrm{s}\). So far, more than 400 of these unstable, temporary particles have been catalogued.',
 r'تقریباً 1945 سے شروع ہونے والے ایسے تجربات میں بہت سے نئے ذرات دریافت ہوئے جن میں معلوم ذرات کے درمیان زیادہ توانائی والے تصادم کیے گئے۔ ایسے ذرات نہایت غیر مستحکم ہوتے ہیں اور ان کی نصف عمریں بہت مختصر، \(10^{6}\) سے \(10^{23}\ \mathrm{s}\) کے درمیان ہوتی ہیں۔ اب تک ان غیر مستحکم، عارضی ذرات میں سے 400 سے زیادہ کی فہرست بنائی جا چکی ہے۔',
 r'شاوخوا له 1945 څخه په هغو تجربو کې ډېرې نوې ذرې وموندل شوې چې د پېژندل شوو ذرو ترمنځ د لوړې انرژۍ ټکرونه پکې کېدل. دا ذرې ډېرې بې ثباته دي او ډېر لنډ نیم ژوندونه لري، چې د \(10^{6}\) او \(10^{23}\ \mathrm{s}\) ترمنځ دي. تر اوسه له دغو بې ثباته، لنډمهالو ذرو څخه له 400 ډېرې په لېست کې ثبت شوې دي.')
add('paragraph','It is useful to group the known particles into three families—the bosons, the leptons, and the hadrons.',
 'معلوم ذرات کو تین خاندانوں، یعنی بوزونز، لیپٹونز اور ہیڈرانز، میں تقسیم کرنا مفید ہے۔',
 'ګټوره ده چې پېژندل شوې ذرې په دریو کورنیو ووېشل شي: بوزونونه، لېپټونونه او هاډرونونه.')
add('heading','A. BOSONS','A. بوزونز','A. بوزونونه')
add('paragraph',r'The boson family is composed of particles that play central roles in nature’s fundamental forces. The photon is associated with the electromagnetic force. The \(\mathrm{W}^{-}\), \(\mathrm{W}^{+}\), and \(\mathrm{Z}^{0}\) particles are associated with the weak nuclear force. The gluons are associated with the strong nuclear force, whereas the graviton is thought to be associated with the gravitational force.',
 r'بوزون خاندان ان ذرات پر مشتمل ہے جو فطرت کی بنیادی قوتوں میں مرکزی کردار ادا کرتے ہیں۔ فوٹون برق مقناطیسی قوت سے متعلق ہے۔ \(\mathrm{W}^{-}\)، \(\mathrm{W}^{+}\) اور \(\mathrm{Z}^{0}\) ذرات کمزور نیوکلیائی قوت سے متعلق ہیں۔ گلوآنز قوی نیوکلیائی قوت سے متعلق ہیں، جبکہ گریویٹون کو کششِ ثقل کی قوت سے متعلق سمجھا جاتا ہے۔',
 r'د بوزون کورنۍ له هغو ذرو جوړه ده چې د طبیعت په بنسټیزو ځواکونو کې مرکزي رولونه لري. فوټون له برېښنا مقناطیسي ځواک سره تړاو لري. \(\mathrm{W}^{-}\)، \(\mathrm{W}^{+}\) او \(\mathrm{Z}^{0}\) ذرې له کمزوري هستوي ځواک سره تړاو لري. ګلوونونه له قوي هستوي ځواک سره تړاو لري، خو ګرېویټون له جاذبې ځواک سره تړلی ګڼل کېږي.')
add('heading','FIGURE 20.26','شکل 20.26','شکل 20.26')
L.append({'type':'visual','blockId':'phys20-193-standard-model'})
add('paragraph','Standard Model of Elementary Particles','بنیادی ذرات کا معیاری ماڈل','د بنسټیزو ذرو معیاري ماډل')
add('heading','B. LEPTONS','B. لیپٹونز','B. لېپټونونه')
add('paragraph',r'The lepton family consists of particles that interact by means of the weak nuclear force. Leptons can also exert gravitational and (if the leptons are charged) electromagnetic forces on other particles. The four better-known leptons are the electron, the muon, the electron neutrino \(\nu_{e}\), and the muon neutrino \(\nu_{\mu}\). Two other leptons have also been discovered, the tau particle \(\tau\) and its neutrino \(\nu_{\tau}\), bringing the number of particles in the lepton family to six. No internal structure for leptons is observed so far, therefore they are considered to be elementary.',
 r'لیپٹون خاندان ان ذرات پر مشتمل ہے جو کمزور نیوکلیائی قوت کے ذریعے تعامل کرتے ہیں۔ لیپٹون دوسرے ذرات پر کششِ ثقل اور، اگر لیپٹون بار دار ہوں تو، برق مقناطیسی قوتیں بھی لگا سکتے ہیں۔ زیادہ معروف چار لیپٹون الیکٹران، میوآن، الیکٹران نیوٹرینو \(\nu_{e}\) اور میوآن نیوٹرینو \(\nu_{\mu}\) ہیں۔ دو دیگر لیپٹون، ٹاؤ ذرہ \(\tau\) اور اس کا نیوٹرینو \(\nu_{\tau}\)، بھی دریافت ہوئے ہیں، جس سے لیپٹون خاندان کے ذرات کی تعداد چھ ہو جاتی ہے۔ اب تک لیپٹونوں کی کوئی اندرونی ساخت مشاہدے میں نہیں آئی، اس لیے انہیں بنیادی ذرات سمجھا جاتا ہے۔',
 r'د لېپټون کورنۍ له هغو ذرو جوړه ده چې د کمزوري هستوي ځواک له لارې تعامل کوي. لېپټونونه پر نورو ذرو د جاذبې او، که چارج ولري، د برېښنا مقناطیسي ځواک اغېز هم کولی شي. څلور ډېر پېژندل شوي لېپټونونه الکټرون، میوون، د الکټرون نیوټرینو \(\nu_{e}\) او د میوون نیوټرینو \(\nu_{\mu}\) دي. دوه نور لېپټونونه، د ټاو ذره \(\tau\) او د هغې نیوټرینو \(\nu_{\tau}\)، هم موندل شوي دي، چې د لېپټون کورنۍ د ذرو شمېر شپږو ته رسوي. تر اوسه د لېپټونونو هېڅ داخلي جوړښت نه دی لیدل شوی، نو بنسټیزې ذرې ګڼل کېږي.')
add('heading','C. HADRONS','C. ہیڈرانز','C. هاډرونونه')
add('paragraph','The hadron family contains the particles that interact by means of both the strong nuclear force and the weak nuclear force. Hadrons can also interact by gravitational and electromagnetic forces, but at short distances the strong nuclear force dominates. Among the hadrons are the proton, the neutron, and the pions. The hadrons are subdivided into two groups, the mesons and the baryons.',
 'ہیڈران خاندان میں وہ ذرات شامل ہیں جو قوی نیوکلیائی قوت اور کمزور نیوکلیائی قوت، دونوں کے ذریعے تعامل کرتے ہیں۔ ہیڈران کششِ ثقل اور برق مقناطیسی قوتوں کے ذریعے بھی تعامل کر سکتے ہیں، لیکن کم فاصلے پر قوی نیوکلیائی قوت غالب ہوتی ہے۔ پروٹون، نیوٹرون اور پائیون ہیڈرانوں میں شامل ہیں۔ ہیڈرانوں کو مزید دو گروہوں، میزونز اور بیریونز، میں تقسیم کیا جاتا ہے۔',
 'د هاډرون کورنۍ هغه ذرې رانغاړي چې د قوي هستوي ځواک او کمزوري هستوي ځواک دواړو له لارې تعامل کوي. هاډرونونه د جاذبې او برېښنا مقناطیسي ځواکونو له لارې هم تعامل کولی شي، خو په لنډو واټنونو کې قوي هستوي ځواک غالب وي. پروتون، نیوټرون او پایونونه په هاډرونونو کې شامل دي. هاډرونونه بیا په دوو ډلو، مېزونونو او باریونونو، وېشل کېږي.')

# All18 source cards retain mass, charge, spin, symbol and group placement.
P=[]
def particle(col,row,symbol,names,mass,charge,spin,group):
    P.append(dict(column=col,row=row,symbol=symbol,names=dict(zip(['en','ur','ps'],names)),mass=mass,charge=charge,spin=spin,group=group))
particle(0,0,'u',('up','اَپ','اپ'),'≈2.2 MeV/c²','⅔','½','quark')
particle(1,0,'c',('charm','چارم','چارم'),'≈1.28 GeV/c²','⅔','½','quark')
particle(2,0,'t',('top','ٹاپ','ټاپ'),'≈173.1 GeV/c²','⅔','½','quark')
particle(0,1,'d',('down','ڈاؤن','ډاون'),'≈4.7 MeV/c²','−⅓','½','quark')
particle(1,1,'s',('strange','سٹرینج','سټرېنج'),'≈96 MeV/c²','−⅓','½','quark')
particle(2,1,'b',('bottom','باٹم','باټم'),'≈4.18 GeV/c²','−⅓','½','quark')
particle(0,2,'e',('electron','الیکٹران','الکټرون'),'≈0.511 MeV/c²','−1','½','lepton')
particle(1,2,'μ',('muon','میوآن','میوون'),'≈105.66 MeV/c²','−1','½','lepton')
particle(2,2,'τ',('tau','ٹاؤ','ټاو'),'≈1.7768 GeV/c²','−1','½','lepton')
particle(0,3,'νₑ',('electron\nneutrino','الیکٹران\nنیوٹرینو','د الکټرون\nنیوټرینو'),'<1.0 eV/c²','0','½','lepton')
particle(1,3,'νμ',('muon\nneutrino','میوآن\nنیوٹرینو','د میوون\nنیوټرینو'),'<0.17 MeV/c²','0','½','lepton')
particle(2,3,'ντ',('tau\nneutrino','ٹاؤ\nنیوٹرینو','د ټاو\nنیوټرینو'),'<18.2 MeV/c²','0','½','lepton')
particle(3,0,'g',('gluon','گلوآن','ګلوون'),'0','0','1','gauge')
particle(3,1,'γ',('photon','فوٹون','فوټون'),'0','0','1','gauge')
particle(3,2,'Z',('Z boson','Z بوزون','Z بوزون'),'≈91.19 GeV/c²','0','1','gauge')
particle(3,3,'W',('W boson','W بوزون','W بوزون'),'≈80.39 GeV/c²','±1','1','gauge')
particle(4,0,'H',('higgs','ہگز','هیګز'),'≈124.97 GeV/c²','0','0','scalar')
particle(5,0,'G',('graviton','گریویٹون','ګرېویټون'),'0','0','2','hypothetical')
LABELS={
 'en':{'matter':['three generations of matter','(fermions)'],'forces':['interactions / force carriers','(bosons)'],'quarks':['QUARKS'],'leptons':['LEPTONS'],'gauge':['GAUGE BOSONS','VECTOR BOSONS'],'scalar':['SCALAR BOSONS'],'hypothetical':['HYPOTHETICAL','TENSOR BOSONS'],'values':['mass','charge','spin']},
 'ur':{'matter':['مادے کی تین نسلیں','(فرمیونز)'],'forces':['تعاملات / قوت کے حامل ذرات','(بوزونز)'],'quarks':['کوارکس'],'leptons':['لیپٹونز'],'gauge':['گیج بوزونز','سمتی بوزونز'],'scalar':['عددی بوزونز'],'hypothetical':['مفروضہ','ٹینسر بوزونز'],'values':['کمیت','بار','اسپن']},
 'ps':{'matter':['د مادې درې نسلونه','(فرمیونونه)'],'forces':['تعاملونه / د ځواک لېږدوونکي','(بوزونونه)'],'quarks':['کوارکونه'],'leptons':['لېپټونونه'],'gauge':['ګېج بوزونونه','ویکټوري بوزونونه'],'scalar':['سکالري بوزونونه'],'hypothetical':['فرض شوي','ټینسوري بوزونونه'],'values':['کتله','چارج','سپین']}}
def chart(lang):
    words=LABELS[lang];out=''
    for x,key in [(315,'matter'),(843,'forces')]:
        for i,value in enumerate(words[key]):out+=text(x,28+i*22,value,18)
    for i,value in enumerate(words['values']):out+=text(91,104+i*21,value,15,'end')
    colors={'quark':('#fef08a','#e9d5ff'),'lepton':('#f7fee7','#bef264'),'gauge':('#fff7ed','#fb923c'),'scalar':('#fffbeb','#facc15'),'hypothetical':('#eff6ff','#7dd3fc')}
    for p in P:
        x=100+p['column']*172;y=75+p['row']*162
        if p['column']>3:x+=25
        fill,circle=colors[p['group']]
        out+=f'<rect x="{x}" y="{y}" width="161" height="151" rx="12" fill="{fill}" stroke="#334155" stroke-width="2"/>'
        out+=text(x+9,y+21,p['mass'],13,'start')+text(x+9,y+44,p['charge'],15,'start')+text(x+9,y+66,p['spin'],15,'start')
        out+=f'<circle cx="{x+86}" cy="{y+66}" r="29" fill="{circle}"/>'
        if p['symbol'] in ['νμ','ντ']:
            out+=f'<text x="{x+86}" y="{y+78}" font-size="33" font-family="Arial,sans-serif" text-anchor="middle">ν<tspan baseline-shift="sub" font-size="18">{p["symbol"][1]}</tspan></text>'
        else:out+=text(x+86,y+77,p['symbol'],36)
        for i,value in enumerate(p['names'][lang].split('\n')):out+=text(x+81,y+117+i*23,value,18)
    # Group labels retain the source's three-generation and force-carrier structure.
    for x,y,key in [(40,324,'quarks'),(40,650,'leptons'),(808,689,'gauge'),(966,420,'scalar'),(1138,475,'hypothetical')]:
        vals=words[key]
        for i,value in enumerate(vals):out+=f'<g transform="translate({x+i*22} {y}) rotate(-90)">'+text(0,0,value,18,'start')+'</g>'
    return svg(out,1175,737,{'en':'Complete source Figure20.26:18 elementary-particle cards with mass, charge and spin; three fermion generations, gauge/vector bosons, scalar bosons and hypothetical tensor bosons','ur':'اصل شکل20.26 کے تمام18 ذرات: کمیت، بار اور اسپن؛ فرمیونز کی تین نسلیں، گیج/سمتی بوزونز، عددی بوزونز اور مفروضہ ٹینسر بوزونز','ps':'د اصلي20.26 شکل ټول18 ذرات: کتله، چارج او سپین؛ د فرمیونونو درې نسلونه، ګېج/ویکټوري بوزونونه، سکالري بوزونونه او فرض شوي ټینسوري بوزونونه'}[lang])
def ref(n):return {'pdfPage':193,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-gravity-particle-interactions-and-building-blocks-374-375','title':'Gravitation, particle interactions and building blocks of matter','kind':'lesson','pdfPage':193,'printedPage':374,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
sec=section(record,T,L,('کششِ ثقل، ذرات کے تعاملات اور مادے کے بنیادی اجزا','جاذبه، د ذرو تعاملونه او د مادې بنسټیزې برخې'))
issues=['Printed374 gives the unstable-particle half-life range as10⁶ to10²³s with positive exponents, despite calling these very short; both positive signs retained as printed.', 'Table20.5 gives weak-force relative strength10⁻⁷; the preceding page373 paragraph gives10⁻⁶. Both values retained.']
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(374),ref(375)],sourceTableRows=ROWS,sourceIssues=issues,sourceBlocks=[{'id':'phys20-193-standard-model','type':'figure','sourceFigure':'20.26','particles':P,'svg':chart('en'),'svgUrdu':chart('ur'),'svgPashto':chart('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():upsert([record],[sec],chapter_index=9)
    stage_reference(193,record,'Full PDF193 inspected;240dpi crops confirmed the positive printed lifetime exponents and all18 particle cards. Restored gravitational paragraph, all five columns/four data rows of Table20.5, matter/boson/lepton/hadron paragraphs, headings and figure caption. Figure20.26 now retains every source mass, charge, spin, particle symbol/name and family placement with reusable values. Full Urdu/Pashto paragraph and chart-label translations aligned. Both printed inconsistencies recorded rather than silently corrected.',issues)
    print('PDF193 source-fidelity correction staged; two printed inconsistencies remain.')
