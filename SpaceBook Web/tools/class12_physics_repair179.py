"""PDF179 complete alpha/beta text, equations and three source diagrams."""
from class12_source_review import upsert,section,shared_class_data_lock,sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text,arrow,isotope,svg
from class12_physics_repair186 import cluster
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
def eq(s):s=r'\('+s+r'\)';add('equation',s,s,s)
add('heading',r'A. ALPHA (\(\alpha\)) EMISSION',r'A. الفا (\(\alpha\)) اخراج',r'A. د الفا (\(\alpha\)) خپرېدل')
add('paragraph',r'Alpha particles are helium nuclei (i.e two protons and two neutrons bound together) emitted from the nucleus. When the ratio of neutrons to protons in the nucleus is too low, certain atoms restore the balance by emitting alpha particles. In alpha decay, the original (parent) nuclide is converted to a ‘daughter’ by the emission of an \(\alpha\) particle. Balancing the reaction shows that the daughter nuclide has a nucleon number reduced by four and a charge reduced by two.',
 r'الفا ذرات ہیلیم کے نیوکلئیس (یعنی دو پروٹون اور دو نیوٹرون جو ایک ساتھ بندھے ہوں) ہیں، جو نیوکلئیس سے خارج ہوتے ہیں۔ جب نیوکلئیس میں نیوٹرونوں اور پروٹونوں کا تناسب بہت کم ہو تو بعض ایٹم الفا ذرات خارج کر کے توازن بحال کرتے ہیں۔ الفا زوال میں اصل (والد) نیوکلائیڈ ایک \(\alpha\) ذرہ خارج کر کے ’’دختر‘‘ میں تبدیل ہوتا ہے۔ تعامل کو متوازن کرنے سے ظاہر ہوتا ہے کہ دختر نیوکلائیڈ کا نیوکلیون عدد چار اور بار دو کم ہو جاتا ہے۔',
 r'الفا ذرې د هیلیم هستې دي (یعنې دوه پروتونونه او دوه نیوټرونونه چې یوځای تړلي وي) او له هستې خپرېږي. کله چې په هسته کې د نیوټرونونو او پروتونونو نسبت ډېر ټیټ وي، ځینې اټومونه د الفا ذرو په خپرولو توازن بېرته جوړوي. په الفا زوال کې اصلي (مور) نوکلایډ د یوې \(\alpha\) ذرې په خپرولو «لور» نوکلایډ ته بدلېږي. د تعامل توازن ښيي چې د لور نوکلایډ د نیوکلیونونو شمېر څلور او چارج دوه کمېږي.')
eq(r'{}^{A}_{Z}\mathrm{X}={}^{A-4}_{Z-2}\mathrm{Y}+\alpha+Q')
eq(r'{}^{263}_{106}\mathrm{Sg}={}^{259}_{104}\mathrm{Rf}+{}^{4}_{2}\mathrm{He}\ (\alpha)+Q')
add('paragraph',r'The spontaneous emission of an \(\alpha\)-particle by some (heavy) nuclei is related to the compactness of the He nucleus whose binding energy is = 7 MeV/nucleon. Many Nuclei with Z > 83 are radioactive in this mode. It is manifestation of quantum tunneling through potential barrier.',
 r'بعض (بھاری) نیوکلئیسوں سے \(\alpha\) ذرے کا خودبخود اخراج ہیلیم کے نیوکلئیس کی مضبوط بندش سے متعلق ہے، جس کی بندشی توانائی = 7 MeV/نیوکلیون ہے۔ Z > 83 والے بہت سے نیوکلئیس اس انداز میں تابکار ہوتے ہیں۔ یہ پوٹینشل رکاوٹ سے کوانٹمی سرنگ زنی کا مظہر ہے۔',
 r'د ځینو (درنو) هستو له خوا د \(\alpha\) ذرې خپل سری خپرېدل د He هستې له ټینګوالي سره تړاو لري، چې د تړون انرژي یې = 7 MeV/نیوکلیون ده. د Z > 83 لرونکې ډېرې هستې په دې ډول راډیواکټیفې دي. دا د پوتنسیال له خنډ څخه د کوانټمي تونل وهلو څرګندونه ده.')
add('heading','FIGURE 20.8','شکل20.8','شکل20.8')
L.append({'type':'visual','blockId':'phys20-179-alpha'})
eq(r'{}^{238}_{92}\mathrm{U}={}^{234}_{90}\mathrm{Th}+{}^{4}_{2}\mathrm{He}\ (\alpha)+Q')
add('paragraph','The emission of an alpha particle by uranium-238 results in the formation of thorium-234','یورینیم-238 سے الفا ذرے کے اخراج کے نتیجے میں تھوریم-234 بنتا ہے','د یورانیم-238 له خوا د الفا ذرې خپرېدل د توریوم-234 د جوړېدو لامل کېږي')
add('heading','B. BETA EMISSION','B. بیٹا اخراج','B. د بېټا خپرېدل')
add('paragraph','Beta particle emission occurs when the ratio of neutrons to protons in the nucleus is too high. In this case, an excess neutron transforms into a proton and an electron. The proton stays in the nucleus and the electron is ejected energetically. A neutron by itself is unstable; and on average in 890 s will decay into a proton and an electron.',
 'بیٹا ذرے کا اخراج اس وقت ہوتا ہے جب نیوکلئیس میں نیوٹرونوں اور پروٹونوں کا تناسب بہت زیادہ ہو۔ اس صورت میں ایک اضافی نیوٹرون پروٹون اور الیکٹران میں بدلتا ہے۔ پروٹون نیوکلئیس میں رہتا ہے اور الیکٹران توانائی کے ساتھ خارج ہوتا ہے۔ نیوٹرون اکیلا غیر مستحکم ہوتا ہے؛ اور اوسطاً890 s میں پروٹون اور الیکٹران میں زوال پذیر ہو جاتا ہے۔',
 'د بېټا ذرې خپرېدل هغه وخت کېږي چې په هسته کې د نیوټرونونو او پروتونونو نسبت ډېر لوړ وي. په دې حالت کې یو اضافي نیوټرون په یوه پروتون او یوه الکترون بدلېږي. پروتون په هسته کې پاتې کېږي او الکترون په انرژۍ سره ایستل کېږي. نیوټرون په یوازې ځان ناپایدار دی؛ او په اوسط ډول په890 s کې په پروتون او الکترون زوال کوي.')
add('paragraph',r'Unlike \(\alpha\)-decay, \(\beta\)-decay of a radionuclide does not change the number of nucleons. In essence, \(\beta\)-decay changes a neutron into a proton.',
 r'\(\alpha\) زوال کے برعکس، کسی تابکار نیوکلائیڈ کا \(\beta\) زوال نیوکلیونوں کی تعداد نہیں بدلتا۔ بنیادی طور پر \(\beta\) زوال نیوٹرون کو پروٹون میں بدلتا ہے۔',
 r'د \(\alpha\) زوال برعکس، د راډیواکټیف نوکلایډ \(\beta\) زوال د نیوکلیونونو شمېر نه بدلوي. په اصل کې \(\beta\) زوال نیوټرون په پروتون بدلوي.')
eq(r'{}^{A}_{Z}\mathrm{X}={}^{A}_{Z+1}\mathrm{Y}+\beta^{-}+\bar\nu+Q')
eq(r'{}^{14}_{6}\mathrm{C}={}^{14}_{7}\mathrm{N}+\beta^{-}+\bar\nu+Q')
add('heading','FIGURE 20.9','شکل20.9','شکل20.9')
L.append({'type':'visual','blockId':'phys20-179-beta-minus'})
eq(r'{}^{234}_{90}\mathrm{Th}={}^{234}_{91}\mathrm{Pa}+\beta^{-}+\bar\nu+Q')
add('paragraph','The emission of a beta particle by thorium-234 results in the formation of protactinium-234','تھوریم-234 سے بیٹا ذرے کے اخراج کے نتیجے میں پروٹیکٹینیم-234 بنتا ہے','د توریوم-234 له خوا د بېټا ذرې خپرېدل د پروټاکټینیم-234 د جوړېدو لامل کېږي')
add('heading','Positron Beta emission:','پوزیٹران بیٹا اخراج:','د پوزیترون بېټا خپرېدل:')
add('paragraph',r'Like beta decay \(\beta^{-}\), positron emission \(\beta^{+}\) does not change the number of nucleons. In essence, \(\beta^{+}\) decay changes a proton into a neutron.',
 r'بیٹا زوال \(\beta^{-}\) کی طرح پوزیٹران اخراج \(\beta^{+}\) نیوکلیونوں کی تعداد نہیں بدلتا۔ بنیادی طور پر \(\beta^{+}\) زوال پروٹون کو نیوٹرون میں بدلتا ہے۔',
 r'د \(\beta^{-}\) بېټا زوال په څېر، د \(\beta^{+}\) پوزیترون خپرېدل د نیوکلیونونو شمېر نه بدلوي. په اصل کې \(\beta^{+}\) زوال پروتون په نیوټرون بدلوي.')
eq(r'{}^{A}_{Z}\mathrm{X}={}^{A}_{Z-1}\mathrm{Y}+\beta^{+}+\nu+Q')
eq(r'{}^{18}_{9}\mathrm{F}={}^{18}_{8}\mathrm{O}+\beta^{+}+\nu+Q')
add('heading','FIGURE 20.10','شکل20.10','شکل20.10')
L.append({'type':'visual','blockId':'phys20-179-positron'})
eq(r'{}^{23}_{12}\mathrm{Th}={}^{23}_{11}\mathrm{Na}+\beta^{+}+\nu+Q')
add('paragraph',r'The positron emission (\(\beta^{+}\) decay) is shown with magnesium-23 decaying into sodium-23',
 r'پوزیٹران اخراج (\(\beta^{+}\) زوال) کو میگنیشیم-23 کے سوڈیم-23 میں زوال سے دکھایا گیا ہے',
 r'د پوزیترون خپرېدل (\(\beta^{+}\) زوال) د مګنیزیم-23 په سوډیم-23 د زوال په وسیله ښودل شوي دي')
def bubble(x,y,a,z,s,r=37,color='#ccfbf1'):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="#172033" stroke-width="2.5"/>'+isotope(x+6,y+2,a,z,s)
def alpha(lang):
    b=bubble(255,60,'A','Z','X',38,'#fef9c3')+bubble(123,177,'A−4','Z−2','Y')+bubble(391,177,4,2,'α')
    b+=arrow(227,87,154,151,'#1e3a8a')+arrow(282,87,361,151,'#1e3a8a')
    b+=cluster(255,329,40)+isotope(179,319,238,92,'U')+cluster(123,458,37)+isotope(122,524,234,90,'Th')
    for x,y,c in [(385,452,'#67e8f9'),(397,452,'#fbcfe8'),(385,464,'#fbcfe8'),(397,464,'#67e8f9')]:b+=f'<circle cx="{x}" cy="{y}" r="6" fill="{c}" stroke="#94a3b8"/>'
    b+=isotope(432,476,4,2,'He')
    b+=arrow(224,359,152,427,'#1e3a8a')+arrow(284,359,377,441,'#1e3a8a')
    return svg(b,520,552,{'en':'Figure20.8: generic alpha emission AXZ to daughter Y with A−4,Z−2 and alpha4,2; uranium238,92 splits into thorium234,90 and helium4,2.','ur':'شکل20.8: عمومی الفا اخراج میں A,Z والا X، A−4,Z−2 والے Y اور الفا4,2 میں بدلتا ہے؛ یورینیم238,92 سے تھوریم234,90 اور ہیلیم4,2 بنتے ہیں۔','ps':'شکل20.8: په عمومي الفا خپرېدو کې د A,Z لرونکی X د A−4,Z−2 لرونکي Y او الفا4,2 ته بدلېږي؛ له یورانیم238,92 څخه توریوم234,90 او هیلیم4,2 جوړېږي.'}[lang])
def beta(lang):
    b=bubble(254,63,'A','Z','X',38,'#fef9c3')+bubble(97,184,'A','Z+1','Y')+bubble(254,214,0,-1,'β',30)+bubble(411,184,0,0,'ν̄',30)
    b+=arrow(225,90,123,161,'#1e3a8a')+arrow(254,106,254,181,'#1e3a8a')+arrow(282,90,390,161,'#1e3a8a')
    b+=cluster(254,342,38)+isotope(179,323,234,90,'Th')+cluster(97,464,34)+isotope(93,529,234,91,'Pa')+isotope(256,516,0,-1,'β')+isotope(425,484,0,0,'ν̄')
    b+=arrow(225,371,121,439,'#1e3a8a')+arrow(254,384,254,485,'#1e3a8a')+arrow(282,371,396,453,'#1e3a8a')
    return svg(b,520,558,{'en':'Figure20.9: generic beta-minus emission increases atomic number by1 and emits beta0,−1 plus antineutrino0,0; thorium234,90 becomes protactinium234,91 with the same emitted particles.','ur':'شکل20.9: عمومی منفی بیٹا اخراج میں ایٹمی عدد1 بڑھتا ہے اور بیٹا0,−1 اور ضد نیوٹرینو0,0 خارج ہوتے ہیں؛ تھوریم234,90 انہی ذرات کے اخراج سے پروٹیکٹینیم234,91 بنتا ہے۔','ps':'شکل20.9: عمومي منفي بېټا خپرېدل اټومي عدد1 زیاتوي او بېټا0,−1 او انټي نیوټرینو0,0 خپروي؛ توریوم234,90 د همدې ذرو په خپرولو پروټاکټینیم234,91 ته بدلېږي.'}[lang])
def positron(lang):
    b=bubble(128,163,'A','Z','X',40,'#fef9c3')+bubble(295,58,0,0,'ν',30)+bubble(333,162,'A','Z−1','Y')+bubble(295,275,0,-1,'β',30)
    b+=arrow(158,137,270,75,'#1e3a8a')+arrow(172,163,292,163,'#1e3a8a')+arrow(158,191,273,254,'#1e3a8a')
    b+=cluster(590,162,29)+isotope(553,111,23,12,'Mg')+cluster(798,162,26)+isotope(857,175,23,11,'Na')+isotope(802,54,0,0,'ν')+isotope(802,285,0,'+1','β')
    b+=arrow(617,137,770,69,'#1e3a8a')+arrow(624,162,766,162,'#1e3a8a')+arrow(615,185,773,262,'#1e3a8a')
    return svg(b,930,328,{'en':'Figure20.10: source generic positron panel changes Z to Z−1 but prints beta atomic number−1; actual panel labels magnesium23,12 to sodium23,11, neutrino0,0 and beta0,+1. Source generic sign retained and flagged.','ur':'شکل20.10: اصل عمومی پوزیٹران خاکے میں Z سے Z−1 ہوتا ہے مگر بیٹا کا ایٹمی عدد−1 چھپا ہے؛ مخصوص خاکے میں میگنیشیم23,12 سے سوڈیم23,11، نیوٹرینو0,0 اور بیٹا0,+1 بنتے ہیں۔ اصل عمومی منفی علامت محفوظ اور نشان زد ہے۔','ps':'شکل20.10: د اصل عمومي پوزیترون طرحه Z په Z−1 بدلوي خو د بېټا اټومي عدد−1 چاپوي؛ ځانګړې طرحه مګنیزیم23,12 په سوډیم23,11، نیوټرینو0,0 او بېټا0,+1 بدلوي. اصلي عمومي منفي نښه ساتل شوې او نښه شوې ده.'}[lang])
record={'id':'phys20-alpha-beta-minus-positron-decay-examples-346-347','title':'Alpha, beta-minus and positron decay','kind':'lesson','pdfPage':179,'printedPage':346,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
issues=['Figure20.10 generic positron particle is labelled0/−1β, while its magnesium-specific panel labels0/+1β; both printed signs retained.','Figure20.10 equation prints23/12Th as the parent, while its diagram/caption identify magnesium23. OriginalTh symbol retained rather than silently changed toMg.']
sec=section(record,T,L,('الفا، منفی بیٹا اور پوزیٹران زوال','الفا، منفي بېټا او پوزیترون زوال'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[{'pdfPage':179,'printedPage':p,'sourcePdf':SOURCE} for p in (346,347)],sourceIssues=issues,sourceBlocks=[{'id':'phys20-179-'+name,'type':'figure','sourceFigure':number,'svg':func('en'),'svgUrdu':func('ur'),'svgPashto':func('ps')} for name,number,func in [('alpha','20.8',alpha),('beta-minus','20.9',beta),('positron','20.10',positron)]])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.6'])
    stage_reference(179,record,'Reinspected PDF179 printed346–347. Restored all alpha, beta-minus and positron paragraphs/equations, including full quantum-tunnelling and free-neutron lifetime statements. Figures20.8–20.10 include both generic and specific isotope diagrams, particle charges, neutrinos/antineutrinos and full source captions/equations. Full aligned Urdu/Pashto. Source positron−1 label andTh instead ofMg retained/flagged. Covered legacy20.6 retired.',issues)
    print('PDF179 full decay text/equations and three figures staged.')
