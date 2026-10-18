"""PDF176 complete binding-energy derivation, force box, table and nucleon panels."""
from class12_source_review import upsert,section,shared_class_data_lock,sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text,svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];ROWS={}
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
def m(s):return r'\('+s+r'\)'
def eq(s):s=m(s);add('equation',s,s,s)
add('heading','FIGURE 20.5','شکل20.5','شکل20.5')
L.append({'type':'visual','blockId':'phys20-176-mass-defect'})
add('paragraph','Nucleus has lower energy than its constituent nuclei','نیوکلئیس کی توانائی اس کے تشکیل دینے والے نیوکلئیسوں سے کم ہوتی ہے','هسته د خپلو جوړوونکو هستو په پرتله کمه انرژي لري')
add('definition','The amount by which the mass of an atomic nucleus is less than the sum of the masses of its constituent particles is called mass deficit or mass defect.',
 'وہ مقدار جس سے ایٹمی نیوکلئیس کی کمیت اس کے تشکیل دینے والے ذرات کی کمیتوں کے مجموعے سے کم ہو، کمیتی کمی یا کمیتی نقص کہلاتی ہے۔',
 'هغه اندازه چې د اټومي هستې کتله د هغې د جوړوونکو ذرو د کتلو تر مجموعې کمه وي، د کتلې کمښت یا د کتلې کسر بلل کېږي.')
add('definition','The energy that holds a nucleus together is called binding Energy, this amount of energy will be required to break the nucleus into separate parts.',
 'وہ توانائی جو نیوکلئیس کو یکجا رکھتی ہے بندشی توانائی کہلاتی ہے، نیوکلئیس کو الگ حصوں میں توڑنے کے لیے اتنی ہی توانائی درکار ہوگی۔',
 'هغه انرژي چې هسته یوځای ساتي د تړون انرژي بلل کېږي؛ د هستې په جلا برخو د ماتولو لپاره به همدومره انرژي اړینه وي.')
add('paragraph','The binding energy is equal to the mass defect of the nucleus. Since the nucleus is a bound system, its total energy is less than the energy of Z protons and N neutrons that are far apart and at rest.',
 'بندشی توانائی نیوکلئیس کے کمیتی نقص کے برابر ہے۔ چونکہ نیوکلئیس ایک بندھا ہوا نظام ہے، اس کی کل توانائی دور دور اور سکون میں موجود Z پروٹونوں اور N نیوٹرونوں کی توانائی سے کم ہے۔',
 'د تړون انرژي د هستې د کتلې له کسر سره برابره ده. ځکه چې هسته یو تړلی سیستم دی، ټوله انرژي یې د هغو Z پروتونونو او N نیوټرونونو تر انرژۍ کمه ده چې له یو بل څخه لرې او په سکون کې وي.')
add('equation',m(r'E_B=(\text{total energy of Z protons and N neutrons})-(\text{total energy of nucleus})'),m(r'E_B=(\text{Z پروٹونوں اور N نیوٹرونوں کی کل توانائی})-(\text{نیوکلئیس کی کل توانائی})'),m(r'E_B=(\text{د Z پروتونونو او N نیوټرونونو ټوله انرژي})-(\text{د هستې ټوله انرژي})'))
add('paragraph',r'If M is the mass of the nucleus, \(M_{\mathrm{p}}\) is the mass of proton and \(M_{\mathrm{N}}\) is the mass of Neutron, the Binding energy of the nucleus will be:',
 r'اگر M نیوکلئیس کی کمیت، \(M_{\mathrm{p}}\) پروٹون کی کمیت اور \(M_{\mathrm{N}}\) نیوٹرون کی کمیت ہو، تو نیوکلئیس کی بندشی توانائی ہوگی:',
 r'که M د هستې کتله، \(M_{\mathrm{p}}\) د پروتون کتله او \(M_{\mathrm{N}}\) د نیوټرون کتله وي، د هستې د تړون انرژي به وي:')
eq(r'E_B=(ZM_{\mathrm{p}}+NM_{\mathrm{N}}-M)c^2\qquad(20.5)')
add('paragraph',r'Where Z is the number of protons and N is the number of neutron in the nucleus. The mass defect or mass deficit (\(\Delta m\)) is given by the relation',
 r'جہاں Z پروٹونوں کی تعداد اور N نیوکلئیس میں نیوٹرونوں کی تعداد ہے۔ کمیتی نقص یا کمیتی کمی (\(\Delta m\)) اس تعلق سے دی جاتی ہے',
 r'چې Z د پروتونونو شمېر او N په هسته کې د نیوټرونونو شمېر دی. د کتلې کسر یا کمښت (\(\Delta m\)) په دې اړیکه ورکول کېږي')
eq(r'\Delta m=ZM_{\mathrm{p}}+NM_{\mathrm{N}}-M\qquad(20.6)')
add('paragraph','The binding energy per nucleon of a nucleus is called packing fraction. If ‘A = N + Z’ is the mass number (number of nucleons), then the packing fraction ‘f’ is',
 'نیوکلئیس کی فی نیوکلیون بندشی توانائی کو پیکنگ کسر کہتے ہیں۔ اگر ‘A = N + Z’ کمیتی عدد (نیوکلیونوں کی تعداد) ہو، تو پیکنگ کسر ‘f’ ہے',
 'د هستې د هر نیوکلیون د تړون انرژي د بسته بندۍ کسر بلل کېږي. که ‘A = N + Z’ کتلیز عدد (د نیوکلیونونو شمېر) وي، نو د بسته بندۍ کسر ‘f’ دی')
eq(r'f=\frac{E_B}{A}=\frac{(ZM_{\mathrm{p}}+NM_{\mathrm{N}}-M)c^2}{A}\qquad(20.7)')
add('paragraph','The packing fraction (binding fraction) is the measure of stability of a nucleus. The greater the binding energy per nucleon, the more stable the nucleus is.',
 'پیکنگ کسر (بندشی کسر) نیوکلئیس کے استحکام کا پیمانہ ہے۔ فی نیوکلیون بندشی توانائی جتنی زیادہ ہو، نیوکلئیس اتنا ہی زیادہ مستحکم ہوتا ہے۔',
 'د بسته بندۍ کسر (د تړون کسر) د هستې د پایدارۍ اندازه ده. د هر نیوکلیون د تړون انرژي چې څومره زیاته وي، هسته همغومره پایدار وي.')
add('heading','For your information','آپ کی معلومات کے لیے','ستاسو د معلوماتو لپاره')
add('heading','STRONG NUCLEAR FORCE','مضبوط نیوکلیائی قوت','پیاوړې هستوي قوه')
add('paragraph','Since very large repulsive Coulomb forces exists between the close-packed protons in a nucleus, and this force should cause the nucleus to fly apart. Because that does not happen, there must be a counteracting attractive force, this force is called strong nuclear force. The strong nuclear force is a very short range (about 2 fm) attractive force that acts between all nuclear particles. The protons attract each other by means of the nuclear force, and, at the same time, they repel each other through the Coulomb force. The nuclear force also acts between pairs of neutrons and between neutrons and protons. The nuclear force dominates the Coulomb repulsive force within the nucleus (at short ranges), so stable nuclei can exist.',
 'چونکہ نیوکلئیس میں قریب قریب موجود پروٹونوں کے درمیان بہت بڑی کولمبی دافع قوتیں ہوتی ہیں، اس لیے اس قوت کو نیوکلئیس کو بکھیر دینا چاہیے۔ چونکہ ایسا نہیں ہوتا، اس کے مقابل ایک جاذب قوت ہونی چاہیے، جسے مضبوط نیوکلیائی قوت کہتے ہیں۔ مضبوط نیوکلیائی قوت بہت کم فاصلے (تقریباً2 fm) تک عمل کرنے والی جاذب قوت ہے، جو تمام نیوکلیائی ذرات کے درمیان کام کرتی ہے۔ پروٹون نیوکلیائی قوت سے ایک دوسرے کو کھینچتے ہیں اور اسی وقت کولمبی قوت سے ایک دوسرے کو دھکیلتے ہیں۔ نیوکلیائی قوت نیوٹرونوں کے جوڑوں اور نیوٹرونوں و پروٹونوں کے درمیان بھی کام کرتی ہے۔ نیوکلئیس میں (کم فاصلوں پر) نیوکلیائی قوت کولمبی دافع قوت پر غالب آتی ہے، اس لیے مستحکم نیوکلئیس موجود رہ سکتے ہیں۔',
 'ځکه چې په هسته کې د نږدې پروتونونو ترمنځ ډېرې لویې کولمبي دفع کوونکې قوې شته، دا قوه باید هسته سره جلا کړي. ځکه چې داسې نه کېږي، باید یوه مقابله جذبوونکې قوه وي چې پیاوړې هستوي قوه بلل کېږي. پیاوړې هستوي قوه د ډېرې لنډې فاصلې (نږدې2 fm) جذبوونکې قوه ده چې د ټولو هستوي ذرو ترمنځ عمل کوي. پروتونونه د هستوي قوې په وسیله یو بل جذبوي او په عین وخت کې د کولمبي قوې له لارې یو بل دفع کوي. هستوي قوه د نیوټرونونو د جوړو او د نیوټرونونو او پروتونونو ترمنځ هم عمل کوي. په هسته کې (په لنډو واټنونو کې) هستوي قوه پر کولمبي دفع کوونکې قوې غالبه وي، نو پایدارې هستې موجودېدای شي.')
add('paragraph','Therefore, the rest energy of the bound system (the nucleus) is less than the combined rest energy of the separated nucleons. To separate the protons and neutron from a nucleus work would need to be done to overcome nuclear force, called binding energy. Binding energy is also equal to the energy liberated when a nucleus is created from other nucleons or nuclei. This nuclear binding energy is derived from the nuclear force and is the energy required to disassemble a nucleus into the same number of free, unbound neutrons and protons it is composed.',
 'لہٰذا بندھے ہوئے نظام (نیوکلئیس) کی سکونی توانائی الگ الگ نیوکلیونوں کی مجموعی سکونی توانائی سے کم ہوتی ہے۔ نیوکلئیس سے پروٹونوں اور نیوٹرون کو الگ کرنے کے لیے نیوکلیائی قوت پر قابو پانے کا کام کرنا ہوگا، جسے بندشی توانائی کہتے ہیں۔ بندشی توانائی اس توانائی کے برابر بھی ہے جو دوسرے نیوکلیونوں یا نیوکلئیسوں سے نیوکلئیس بننے پر خارج ہوتی ہے۔ یہ نیوکلیائی بندشی توانائی نیوکلیائی قوت سے آتی ہے اور نیوکلئیس کو اتنے ہی آزاد، غیر بندھے نیوٹرونوں اور پروٹونوں میں الگ کرنے کے لیے درکار توانائی ہے جن سے وہ بنا ہے۔',
 'نو د تړلي سیستم (هستې) د سکون انرژي د جلا نیوکلیونونو د سکون د انرژۍ تر مجموعې کمه ده. له هستې څخه د پروتونونو او نیوټرون د بېلولو لپاره باید پر هستوي قوې د برلاسۍ کار وشي، چې د تړون انرژي بلل کېږي. د تړون انرژي له هغې انرژۍ سره هم برابره ده چې له نورو نیوکلیونونو یا هستو څخه د یوې هستې د جوړېدو پر مهال خوشې کېږي. دا هستوي تړون انرژي له هستوي قوې سرچینه اخلي او هغه انرژي ده چې هسته د هماغه شمېر ازادو، ناتړلو نیوټرونونو او پروتونونو په بڼه بېله کړي چې ترې جوړه شوې ده.')
add('heading','TABLE 20.2 SOME BINDING ENERGIES','جدول20.2 بعض بندشی توانائیاں','جدول20.2 د تړون ځینې انرژۍ')
rows=[(['Nucleus','Total binding energy (MeV)','Binding energy per nucleon (MeV / nucleon)'],['نیوکلئیس','کل بندشی توانائی (MeV)','فی نیوکلیون بندشی توانائی (MeV / نیوکلیون)'],['هسته','د تړون ټوله انرژي (MeV)','د هر نیوکلیون د تړون انرژي (MeV / نیوکلیون)'])]
for symbol,energy,per in [(r'{}^{2}\mathrm{H}','2.23','1.1'),(r'{}^{4}\mathrm{He}','28.3','7.1'),(r'{}^{12}\mathrm{C}','92.1','7.7'),(r'{}^{16}\mathrm{O}','127.5','8.0'),(r'{}^{56}\mathrm{Fe}','492.3','8.8'),(r'{}^{63}\mathrm{Cu}','552.1','8.8'),(r'{}^{238}\mathrm{U}','1803','7.6')]:rows.append(tuple([m(symbol),energy,per] for _ in range(3)))
start=len(T)
for row in rows:ROWS[len(T)]=row[0];T.append(tuple(' — '.join(cells) for cells in row))
L.append({'type':'table','indices':list(range(start,len(T)))})
def bead(x,y,p):return f'<circle cx="{x}" cy="{y}" r="13" fill="'+('#86efac' if p else '#a5b4fc')+'" stroke="#64748b" stroke-width="1.2"/>'
def mass_defect(lang):
    labels={'en':[['Nucleus','(smaller mass)'],['Separated Nucleons','(greater mass)']],'ur':[['نیوکلئیس','(کم کمیت)'],['الگ نیوکلیون','(زیادہ کمیت)']],'ps':[['هسته','(کمه کتله)'],['جلا نیوکلیونونه','(زیاته کتله)']]}[lang]
    b='<circle cx="108" cy="82" r="56" fill="#fce7f3"/><circle cx="566" cy="82" r="41" fill="#fce7f3"/>'
    carbon=[(x,y) for y in (-28,-3,22,47) for x in (-25,0,25)]
    # Twelve distinct nucleons in carbon and four in helium, with matched separated counts.
    for i,(dx,dy) in enumerate(carbon):b+=bead(108+dx,71+dy,i%2==0)
    for i in range(12):b+=bead(258+(i%4)*43,33+(i//4)*45,i%2==0)
    for i,(dx,dy) in enumerate([(-11,-12),(13,-12),(-11,12),(13,12)]):b+=bead(566+dx,82+dy,i%2==0)
    for i,(dx,dy) in enumerate([(0,0),(47,0),(0,47),(47,47)]):b+=bead(715+dx,57+dy,i%2==0)
    b+=text(109,167,'¹²C',24)+text(566,167,'⁴He',24)
    for x,kind in [(108,0),(327,1),(566,0),(740,1)]:
        for i,label in enumerate(labels[kind]):b+=text(x,204+i*25,label,19)
    return svg(b,870,262,{'en':'Figure20.5: carbon12 and helium4 bound nuclei have smaller mass; corresponding12 and4 separated nucleons have greater mass. Coded particles preserve the source comparison.','ur':'شکل20.5: کاربن12 اور ہیلیم4 کے بندھے نیوکلئیس کم کمیت رکھتے ہیں؛ متعلقہ12 اور4 الگ نیوکلیون زیادہ کمیت رکھتے ہیں۔','ps':'شکل20.5: د کاربن12 او هیلیم4 تړلې هستې کمه کتله لري؛ اړوند12 او4 جلا نیوکلیونونه زیاته کتله لري.'}[lang])
def ref(n):return {'pdfPage':176,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-mass-defect-binding-energy-strong-force-table-340-341','title':'Mass defect, binding energy, nuclear force and binding-energy table','kind':'lesson','pdfPage':176,'printedPage':340,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
issues=['Figure20.5 caption says “constituent nuclei”, while its panels compare each nucleus with separated nucleons. Original caption retained.']
sec=section(record,T,L,('کمیتی نقص، بندشی توانائی، نیوکلیائی قوت اور جدول','د کتلې کسر، د تړون انرژي، هستوي قوه او جدول'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(340),ref(341)],sourceTableRows=ROWS,sourceIssues=issues,sourceBlocks=[{'id':'phys20-176-mass-defect','type':'figure','sourceFigure':'20.5','svg':mass_defect('en'),'svgUrdu':mass_defect('ur'),'svgPashto':mass_defect('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.3'],formulas=[{'id':identity,'name':name,'number':number,'formula':plain,'latex':latex,'sourceClass12Physics':True,'sourceReferences':[ref(page)]} for identity,name,number,plain,latex,page in [('phys20-binding-energy-nucleus','Nuclear binding energy','20.5','EB=(ZMp+NMN−M)c²',r'E_B=(ZM_{\mathrm{p}}+NM_{\mathrm{N}}-M)c^2',340),('phys20-nuclear-mass-defect','Nuclear mass defect','20.6','Δm=ZMp+NMN−M',r'\Delta m=ZM_{\mathrm{p}}+NM_{\mathrm{N}}-M',340),('phys20-packing-fraction-binding-energy-per-nucleon','Packing fraction (binding energy per nucleon)','20.7','f=EB/A=(ZMp+NMN−M)c²/A',r'f=\frac{E_B}{A}=\frac{(ZM_{\mathrm{p}}+NM_{\mathrm{N}}-M)c^2}{A}',341)]])
    stage_reference(176,record,'Reinspected PDF176 printed340–341. Restored full mass-defect/binding-energy definitions, total-energy expression, equations20.5–20.7, packing-fraction paragraph, entire strong-force information box, full dissociation paragraph and all seven rows/three columns of Table20.2. Figure20.5 has both bound-versus-separated comparisons with12 carbon and4 helium nucleons and every label. Full Urdu/Pashto translations. Original constituent-nuclei caption retained; covered legacy20.3 retired.',issues)
    print('PDF176 complete definitions, strong-force box, figure and table staged.')
