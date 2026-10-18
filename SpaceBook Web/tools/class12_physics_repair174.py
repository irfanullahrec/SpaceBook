"""PDF174 isotope panels, complete spectrograph and derivation."""
from class12_source_review import upsert,section,shared_class_data_lock,sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text,arrow,svg
from class12_physics_repair186 import cluster
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
def m(s):return r'\('+s+r'\)'
add('paragraph','The term isotope comes from the Greek isos-topos, which means same place, because isotopes of the same element have the same atomic number and therefore occupy the same place in the periodic table. Therefore isotopes of the same element have identical chemical properties. Isotopes cannot be separated by chemical methods, but only by methods that are based on their mass differences, such as mass spectrometry. As illustrated in figure 20.3',
 'آئسوٹوپ کی اصطلاح یونانی isos-topos سے نکلی ہے، جس کا مطلب ایک ہی جگہ ہے، کیونکہ ایک عنصر کے آئسوٹوپس کا ایٹمی عدد یکساں ہوتا ہے اور اس لیے وہ دوری جدول میں ایک ہی جگہ رکھتے ہیں۔ چنانچہ ایک عنصر کے آئسوٹوپس کی کیمیائی خصوصیات یکساں ہوتی ہیں۔ آئسوٹوپس کو کیمیائی طریقوں سے الگ نہیں کیا جا سکتا، بلکہ صرف ان کی کمیتوں کے فرق پر مبنی طریقوں، مثلاً ماس اسپیکٹرومیٹری، سے الگ کیا جا سکتا ہے۔ جیسا کہ شکل20.3 میں دکھایا گیا ہے',
 'د ایزوټوپ اصطلاح له یوناني isos-topos څخه اخیستل شوې چې د یوې ځای معنا لري، ځکه د یوه عنصر ایزوټوپونه یو شان اټومي عدد لري او له همدې امله په دوراني جدول کې یو ځای نیسي. نو د یوه عنصر ایزوټوپونه یو شان کیمیاوي ځانګړنې لري. ایزوټوپونه په کیمیاوي لارو نه شي بېلېدای، بلکې یوازې د کتلې پر توپیر ولاړو لارو، لکه کتلي سپکټرومیټري، بېلېدای شي. لکه په20.3 شکل کې چې ښودل شوي دي')
add('heading','FIGURE 20.3','شکل20.3','شکل20.3')
L.append({'type':'visual','blockId':'phys20-174-chlorine'})
add('paragraph','(a) Three natural isotopes of chlorine, choline 36 is unstable and is found in trace amounts','(a) کلورین کے تین قدرتی آئسوٹوپس، کولین36 غیر مستحکم ہے اور نہایت کم مقدار میں پایا جاتا ہے','(a) د کلورین درې طبیعي ایزوټوپونه، کولین36 ناپایدار دی او په ډېره لږه اندازه موندل کېږي')
add('paragraph','(b) The most stable artificial isotope of chlorine','(b) کلورین کا سب سے مستحکم مصنوعی آئسوٹوپ','(b) د کلورین تر ټولو پایدار مصنوعي ایزوټوپ')
add('paragraph','Over 3,000 isotopes either exist in nature or have been made artificially in particle accelerators, out of which only 257 are stable. The remaining isotopes are unstable and are termed as radioisotopes.',
 '3,000 سے زیادہ آئسوٹوپس یا تو قدرت میں موجود ہیں یا ذرہ سرعت کاروں میں مصنوعی طور پر بنائے گئے ہیں، جن میں سے صرف257 مستحکم ہیں۔ باقی آئسوٹوپس غیر مستحکم ہیں اور تابکار آئسوٹوپس کہلاتے ہیں۔',
 'له3,000 څخه زیات ایزوټوپونه یا په طبیعت کې شته او یا د ذرو په چټکوونکو کې په مصنوعي ډول جوړ شوي دي، چې یوازې257 یې پایدار دي. پاتې ایزوټوپونه ناپایدار دي او راډیواکټیف ایزوټوپونه بلل کېږي.')
add('heading','20.3 MASS SPECTROGRAPH','20.3 ماس اسپیکٹروگراف','20.3 کتلي طیف ثبتوونکی')
add('definition','A device which is used to determine the mass of charged particles is called mass spectrograph. This device can also be used to separate isotopes of chemical element and to determine their relative abundance.',
 'باردار ذرات کی کمیت معلوم کرنے کے لیے استعمال ہونے والا آلہ ماس اسپیکٹروگراف کہلاتا ہے۔ اس آلے کو کیمیائی عنصر کے آئسوٹوپس الگ کرنے اور ان کی نسبتی فراوانی معلوم کرنے کے لیے بھی استعمال کیا جا سکتا ہے۔',
 'هغه وسیله چې د چارج لرونکو ذرو د کتلې د معلومولو لپاره کارول کېږي، کتلي طیف ثبتوونکی بلل کېږي. دا وسیله د کیمیاوي عنصر د ایزوټوپونو د بېلولو او د هغوی د نسبي کثرت د معلومولو لپاره هم کارېدلی شي.')
add('paragraph','A mass spectrograph is based upon the principle that a beam of ions moving through electric and magnetic fields is deflected, and this deflection depends upon the charge and mass of ions.',
 'ماس اسپیکٹروگراف اس اصول پر مبنی ہے کہ برقی اور مقناطیسی میدانوں میں حرکت کرنے والی آئنوں کی شعاع مڑ جاتی ہے، اور یہ انحراف آئنوں کے بار اور کمیت پر منحصر ہوتا ہے۔',
 'کتلي طیف ثبتوونکی پر دې اصل ولاړ دی چې په برېښنايي او مقناطیسي میدانونو کې خوځېدونکی د آیونونو بیم کږېږي، او دا کږېدل د آیونونو په چارج او کتله پورې تړاو لري.')
add('paragraph','A mass spectrometer can be used to separate a mixture of ions having different masses. A schematic view of mass spectrograph is shown in the figure 20.4. The atoms or molecules understudy in vapor form are pushed into ionization chamber. Where an electron is removed from them leaving them with a net positive charge.',
 'مختلف کمیتوں والے آئنوں کے آمیزے کو الگ کرنے کے لیے ماس اسپیکٹرومیٹر استعمال کیا جا سکتا ہے۔ ماس اسپیکٹروگراف کا خاکہ شکل20.4 میں دکھایا گیا ہے۔ زیر مطالعہ ایٹموں یا سالموں کو بخارات کی صورت میں آئن سازی کے خانے میں دھکیلا جاتا ہے۔ وہاں ان سے ایک الیکٹران نکالا جاتا ہے، جس سے ان پر خالص مثبت بار رہ جاتا ہے۔',
 'د بېلابېلو کتلو لرونکو آیونونو د مخلوط د بېلولو لپاره کتلي سپکټرومیټر کارېدلی شي. د کتلي طیف ثبتوونکي طرحه په20.4 شکل کې ښودل شوې ده. تر مطالعې لاندې اټومونه یا مالیکولونه د بخار په بڼه د آیون جوړولو خونې ته ننباسل کېږي. هلته ترې یو الکترون ایستل کېږي او خالص مثبت چارج پرې پاتې کېږي.')
add('paragraph','The charged particles are accelerated through acceleration plates through potential difference ‘V’ applied.',
 'باردار ذرات کو سرعت دینے والی پلیٹوں میں لگائے گئے پوٹینشل فرق ‘V’ کے ذریعے تیز کیا جاتا ہے۔',
 'چارج لرونکې ذرې د چټکوونکو تختو له لارې د لګول شوي پوتنسیال توپیر ‘V’ په وسیله چټکېږي.')
add('heading','FIGURE 20.4','شکل20.4','شکل20.4')
L.append({'type':'visual','blockId':'phys20-174-spectrograph'})
add('paragraph','The beam is then passed through a velocity selector which leaves only the same velocity particles. Thus by leaving the velocity selector the kinetic energy of single charge ion will be given by the equation',
 'پھر شعاع کو رفتار منتخب کرنے والے سے گزارا جاتا ہے، جو صرف یکساں رفتار کے ذرات کو چھوڑتا ہے۔ یوں رفتار منتخب کرنے والے سے نکلنے پر یک باردار آئن کی حرکی توانائی درج ذیل مساوات سے دی جائے گی',
 'بیا بیم د سرعت له ټاکونکي تېرېږي چې یوازې د یو شان سرعت ذرې پرېږدي. نو د سرعت له ټاکونکي تر وتلو وروسته د یوه چارج لرونکي آیون حرکي انرژي په لاندې معادله ورکول کېږي')
add('equation',m(r'\frac12 mv^2=qV')+'     or     '+m(r'v=\sqrt{\frac{2qV}{m}}\qquad(1)'),m(r'\frac12 mv^2=qV')+'     یا     '+m(r'v=\sqrt{\frac{2qV}{m}}\qquad(1)'),m(r'\frac12 mv^2=qV')+'     یا     '+m(r'v=\sqrt{\frac{2qV}{m}}\qquad(1)'))
add('paragraph','These ions are then subjected to perpendicular and uniform magnetic field ‘B’, in the vacuum chamber, where they are deflected in semicircular path towards the detector. The centripetal force is provided by the magnetic force',
 'پھر ان آئنوں کو خلا کے خانے میں عموداً یکساں مقناطیسی میدان ‘B’ میں رکھا جاتا ہے، جہاں وہ نیم دائرہ راستے میں کھوجی کی طرف مڑتے ہیں۔ مرکز مائل قوت مقناطیسی قوت فراہم کرتی ہے',
 'بیا دا آیونونه په تشه خونه کې له عمودي او یوشان مقناطیسي میدان ‘B’ سره مخ کېږي، چې هلته د کشفوونکي پر لور په نیمه دایروي لاره کږېږي. مرکزته قوې ته مقناطیسي قوه برابروي')
add('equation',m(r'\frac{mv^2}{r}=qvB')+'     or     '+m(r'v=\frac{qB}{m}\times r\qquad(2)'),m(r'\frac{mv^2}{r}=qvB')+'     یا     '+m(r'v=\frac{qB}{m}\times r\qquad(2)'),m(r'\frac{mv^2}{r}=qvB')+'     یا     '+m(r'v=\frac{qB}{m}\times r\qquad(2)'))
add('paragraph','Comparing equation 1 and equation 2','مساوات1 اور مساوات2 کا موازنہ کرنے سے','د1 او2 معادلو په پرتله کولو سره')
e=m(r'\frac{qB}{m}\times r=\sqrt{\frac{2qV}{m}}');add('equation',e,e,e)
add('paragraph','Squaring both sides','دونوں طرف مربع لینے سے','د دواړو خواوو په مربع کولو سره')
e=m(r'\frac{q^2B^2r^2}{m^2}\times=\frac{2qV}{m}');add('equation',e,e,e)
add('paragraph','Solving for m we get','m کے لیے حل کرنے سے ملتا ہے','د m لپاره په حل کولو ترلاسه کوو')
e=m(r'm=\frac{r^2B^2q}{2V}');add('equation',e,e,e)
add('paragraph','So we can obtain the mass if r, B, q and V are known. By rearranging the above equation we can also write',
 'لہٰذا اگر r، B، q اور V معلوم ہوں تو ہم کمیت حاصل کر سکتے ہیں۔ اوپر کی مساوات کی ترتیب بدل کر ہم یہ بھی لکھ سکتے ہیں',
 'نو که r، B، q او V معلوم وي، کتله ترلاسه کولی شو. د پورتنۍ معادلې په بیا ترتیبولو داسې هم لیکلی شو')
ISOTOPES=[{'mass':35,'protons':17,'neutrons':18,'electrons':17},{'mass':36,'protons':17,'neutrons':19,'electrons':17},{'mass':37,'protons':17,'neutrons':20,'electrons':17},{'mass':39,'protons':17,'neutrons':22,'electrons':17}]
def chlorine(lang):
    names={'en':['Chlorine','Protons','Neutrons','Electrons'],'ur':['کلورین','پروٹون','نیوٹرون','الیکٹران'],'ps':['کلورین','پروتونونه','نیوټرونونه','الکترونونه']}[lang];b=''
    for i,item in enumerate(ISOTOPES):
        x=120+i*231;b+=cluster(x,68,39)+text(x,134,names[0]+('. ' if i==2 and lang=='en' else ' ')+str(item['mass']),21)
        for k,key in enumerate(('protons','neutrons','electrons')):b+=text(x,169+29*k,str(item[key])+' '+names[k+1],20)
    b+='<path d="M696 15V286" stroke="#334155" stroke-width="2"/>'+text(347,277,'(a)',22)+text(813,277,'(b)',22)
    return svg(b,930,307,{'en':'Figure20.3: chlorine35/36/37/39, all17 protons and17 electrons, respective neutron counts18/19/20/22; first three grouped as natural, fourth artificial as printed.','ur':'شکل20.3: کلورین35/36/37/39، سب میں17 پروٹون اور17 الیکٹران، بالترتیب18/19/20/22 نیوٹرون؛ اصل کے مطابق پہلے تین قدرتی اور چوتھا مصنوعی گروہ ہے۔','ps':'شکل20.3: کلورین35/36/37/39، په ټولو کې17 پروتونونه او17 الکترونونه، په ترتیب18/19/20/22 نیوټرونونه؛ د اصل له مخې لومړي درې طبیعي او څلورم مصنوعي دی.'}[lang])
WORDS={
 'en':[['Ionization','chamber'],['Heater'],['Acceleration','Plates'],['Velocity','selector'],['B out of page'],['Vacuum','Pump'],['Detection','Chamber'],['Detector'],['Amplifier'],['Chart recorder']],
 'ur':[['آئن سازی کا','خانہ'],['ہیٹر'],['سرعت دینے والی','پلیٹیں'],['رفتار منتخب','کرنے والا'],['B صفحے سے باہر'],['خلا کا','پمپ'],['کھوج کا','خانہ'],['کھوجی'],['تقویت کار'],['چارٹ ریکارڈر']],
 'ps':[['د آیون جوړولو','خونه'],['تودوونکی'],['چټکوونکې','تختې'],['د سرعت','ټاکونکی'],['B له پاڼې بهر'],['د تشې','پمپ'],['د کشف','خونه'],['کشفوونکی'],['پیاوړوونکی'],['چارټ ثبتوونکی']]}
def lines(x,y,labels):return ''.join(text(x,y+23*i,v,17) for i,v in enumerate(labels))
def spectrograph(lang):
    b='<path d="M25 164H73V118H640A170 170 0 0 1 640 458V374A86 86 0 0 0 640 202H73V188H25" fill="#f0fdfa" stroke="#172033" stroke-width="3"/>'
    b+='<path d="M96 131Q139 157 181 131M102 184q4 -19 8 0t8 0t8 0t8 0t8 0t8 0" fill="none" stroke="#7c2d12" stroke-width="3"/><path d="M103 188V259H128M141 259H163V188M128 247V271M141 252V266" fill="none" stroke="#172033" stroke-width="2"/>'
    for x in (227,272):b+=f'<ellipse cx="{x}" cy="163" rx="9" ry="42" fill="#94a3b8" stroke="#172033"/>'
    b+='<path d="M440 137H620M440 188H620" stroke="#65a30d" stroke-width="7"/><path d="M121 163H640A129 129 0 0 1 640 421M640 163A146 146 0 0 1 640 455" fill="none" stroke="#172033" stroke-width="2.5" stroke-dasharray="5 7"/>'
    for x in (150,187,312,372,424,493,565,628):b+=f'<circle cx="{x}" cy="163" r="4" fill="#7dd3fc" stroke="#172033"/>'
    for x,y in [(685,174),(730,201),(767,270),(769,328),(729,389),(683,414),(707,180),(763,227),(785,290),(778,359),(741,412),(690,447)]:b+=f'<circle cx="{x}" cy="{y}" r="4" fill="#7dd3fc" stroke="#172033"/>'
    for x,y in [(640,135),(670,141),(702,150),(736,163),(766,187),(789,220),(802,260),(805,301),(799,343),(783,388),(754,421),(717,448)]:b+=f'<circle cx="{x}" cy="{y}" r="2" fill="#172033"/>'
    b+='<rect x="802" y="272" width="63" height="42" fill="#94a3b8" stroke="#172033"/><path d="M865 278H881V307H865" fill="#e2e8f0" stroke="#172033"/>'
    b+='<rect x="621" y="414" width="19" height="13" fill="#ef4444"/><rect x="621" y="448" width="19" height="13" fill="#ef4444"/><path d="M621 421H535M621 455H535M406 421H350M406 455H350" fill="none" stroke="#172033" stroke-width="2"/>'
    b+='<rect x="406" y="394" width="130" height="91" fill="#bef264" stroke="#172033" stroke-width="3"/><path d="M421 412H436V423H421ZM458 412H475V423H458ZM496 412H518V423H496Z" fill="#fef9c3" stroke="#172033"/><circle cx="429" cy="451" r="9" fill="#334155"/><path d="M468 462A22 21 0 0 1 512 462Z" fill="#f8fafc" stroke="#172033"/><path d="M490 459L503 443" stroke="#172033" stroke-width="2"/>'
    b+='<rect x="218" y="389" width="130" height="100" fill="#e2e8f0" stroke="#172033" stroke-width="3"/><rect x="224" y="395" width="118" height="59" fill="#7dd3fc"/><path d="M227 442l6 -2 4 -22 4 25 4 -33 4 33 4 -34 4 33 4 -35 4 34 4 -36 4 36 4 -34 4 34 4 -32 4 33 4 -34 4 30 4 -29 4 29" fill="none" stroke="#7c2d12" stroke-width="1.5"/><path d="M225 466H339M225 478H339" stroke="#65a30d" stroke-width="5"/>'
    b+=text(659,410,'m₁',18)+text(660,480,'m₂',18)
    b+='<g fill="none" stroke="#334155" stroke-width="1.5"><path d="M136 88V138M533 88V133M355 253L273 204M357 253L231 202M604 366L628 414M849 244V273M844 384L797 392"/></g>'
    positions=[(139,40),(134,291),(350,280),(535,42),(740,90),(841,221),(847,409),(596,344),(472,371),(282,364)]
    for (x,y),labels in zip(positions,WORDS[lang]):b+=lines(x,y,labels)
    return svg(b,950,510,{'en':'Figure20.4: ionization chamber/heater, acceleration plates, straight beam through velocity selector, outward magnetic field in evacuated semicircular detection chamber, two mass-dependent paths m1/m2 ending at detectors connected to amplifier and chart recorder; vacuum pump connected to chamber.','ur':'شکل20.4: آئن سازی کا خانہ/ہیٹر، سرعت کی پلیٹیں، رفتار منتخب کرنے والے سے سیدھی شعاع، خلا والے نیم دائرہ کھوجی خانے میں صفحے سے باہر مقناطیسی میدان، کمیت پر منحصر دو راستے m1/m2 کھوجیوں پر ختم ہوتے ہیں جو تقویت کار اور چارٹ ریکارڈر سے جڑے ہیں؛ خلا پمپ خانے سے جڑا ہے۔','ps':'شکل20.4: د آیون جوړولو خونه/تودوونکی، چټکوونکې تختې، د سرعت له ټاکونکي مستقیم بیم، په نیمه دایروي تشه کشفي خونه کې له پاڼې بهر مقناطیسي میدان، د کتلې دوه لارې m1/m2 په کشفوونکو پای ته رسېږي چې له پیاوړوونکي او چارټ ثبتوونکي سره نښتي دي؛ د تشې پمپ له خونې سره نښتی دی.'}[lang])
def ref(n):return {'pdfPage':174,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-isotopes-mass-spectrograph-principle-and-mass-derivation-336-337','title':'Isotopes and the mass spectrograph','kind':'lesson','pdfPage':174,'printedPage':336,'sourcePdf':SOURCE,'paragraphs':[v[0] for v in T]}
issues=['The printed squaring step shows an extra multiplication sign immediately before the equals sign; retained in the source equation.','Figure20.3 caption prints “choline36”; this spelling and the chlorine39 panel description are retained as source wording.']
sec=section(record,T,L,('آئسوٹوپس اور ماس اسپیکٹروگراف','ایزوټوپونه او کتلي طیف ثبتوونکی'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(336),ref(337)],sourceIssues=issues,sourceBlocks=[{'id':'phys20-174-chlorine','type':'figure','sourceFigure':'20.3','isotopeData':ISOTOPES,'svg':chlorine('en'),'svgUrdu':chlorine('ur'),'svgPashto':chlorine('ps')},{'id':'phys20-174-spectrograph','type':'figure','sourceFigure':'20.4','svg':spectrograph('en'),'svgUrdu':spectrograph('ur'),'svgPashto':spectrograph('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.1'],formulas=[{'id':'phys20-ion-acceleration-energy','name':'Ion kinetic energy after acceleration','number':'1','formula':'½mv²=qV; v=√(2qV/m)','latex':r'\frac12mv^2=qV;\quad v=\sqrt{\frac{2qV}{m}}','sourceClass12Physics':True,'sourceReferences':[ref(337)]},{'id':'phys20-ion-magnetic-deflection','name':'Magnetic deflection in mass spectrograph','number':'2','formula':'mv²/r=qvB; v=(qB/m)×r','latex':r'\frac{mv^2}{r}=qvB;\quad v=\frac{qB}{m}\times r','sourceClass12Physics':True,'sourceReferences':[ref(337)]},{'id':'phys20-mass-spectrograph-mass','name':'Mass from a spectrograph circular path','formula':'m=r²B²q/(2V)','latex':r'm=\frac{r^2B^2q}{2V}','sourceClass12Physics':True,'sourceReferences':[ref(337)]}])
    stage_reference(174,record,'Reinspected PDF174 printed336–337 and close equation crop. Full isotope etymology/properties, four chlorine isotope panels/counts/captions, complete mass-spectrograph definition/principle/operation and all derivation steps restored with Urdu/Pashto. Figure20.4 includes connected instrument stages, vacuum pump, field direction, two isotope arcs/detectors and amplifier/chart recorder. Printed stray multiplication sign and caption spelling retained. Legacy20.1 retired only after its full334–336 material was covered.',issues)
    print('PDF174 full isotope panels, apparatus and derivation staged.')
