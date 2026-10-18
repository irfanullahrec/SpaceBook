"""Replace Unit20 paraphrase cards with source-paired glossary and formula cards."""
from class12_source_review import sync_companions,shared_class_data_lock
from class12_physics_repair195 import G
SRC='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
TERMS={
'Nucleons':'نیوکلونز','Isotopes':'آئسوٹوپس','Atomic mass unit (u)':'ایٹمی کمیت کی اکائی (u)','Binding energy':'بندشی توانائی','Radioactivity':'تابکاری','Activity':'سرگرمی','Random process':'بے ترتیب عمل','Spontaneous process':'خودبخود عمل','becquerel (Bq)':'بیکرل (Bq)','Decay constant':'زوال کا مستقل','Half life':'نصف عمر','Nuclear Reaction':'نیوکلیائی تعامل','Nuclear reaction energy':'نیوکلیائی تعامل کی توانائی','Radiation detector':'تابکاری کا سراغ رساں آلہ','Nuclear fission':'نیوکلیائی انشقاق','Critical mass':'بحرانی کمیت','Nuclear fusion':'نیوکلیائی امتزاج','Quark':'کوارک'}
TERMS_PS={'Nucleons':'نوکلیونونه','Isotopes':'ایزوټوپونه','Atomic mass unit (u)':'د اټومي کتلې واحد (u)','Binding energy':'د تړون انرژي','Radioactivity':'راډیواکټیویټي','Activity':'فعالیت','Random process':'تصادفي بهیر','Spontaneous process':'خپل سری بهیر','becquerel (Bq)':'بېکرېل (Bq)','Decay constant':'د زوال ثابت','Half life':'نیم ژوند','Nuclear Reaction':'هستوي تعامل','Nuclear reaction energy':'د هستوي تعامل انرژي','Radiation detector':'د وړانګو کشفوونکی','Nuclear fission':'هستوي انشقاق','Critical mass':'بحراني کتله','Nuclear fusion':'هستوي امتزاج','Quark':'کوارک'}
definitions=[]
for en,ur,ps in G:
    term,definition=en.split(': ',1);term_ur,definition_ur=ur.split(': ',1);term_ps,definition_ps=ps.split(': ',1)
    definitions.append({'term':term,'definition':definition,'termUrdu':term_ur,'termPashto':term_ps,
        'urdu':definition_ur,'pashto':definition_ps,'sourceClass12Physics':True,
        'sourceReferences':[{'pdfPage':195,'printedPage':378,'sourcePdf':SRC}],
        'interactiveId':'phys20-glossary-'+str(len(definitions)+1)})
REF=lambda page,printed:{'pdfPage':page,'printedPage':printed,'sourcePdf':SRC}
rows=[
('phys20-mass-number-sum','Nuclear mass-number relation','A=Z+N',173,335),
('phys20-nuclide-symbol','Nuclide notation',r'{}^{A}_{Z}\mathrm{X}',173,335),
('phys20-ion-acceleration-energy','Ion acceleration and kinetic energy',r'\frac12mv^2=qV;\quad v=\sqrt{\frac{2qV}{m}}',174,337),
('phys20-ion-magnetic-deflection','Ion magnetic deflection',r'\frac{mv^2}{r}=qvB;\quad v=\frac{qBr}{m}',174,337),
('phys20-mass-spectrograph-mass','Mass from a spectrograph path',r'm=\frac{r^2B^2q}{2V}',174,337),
('phys20-unified-mass-unit-kilogram','Unified atomic mass unit in kilograms',r'1\,\mathrm{u}=1.660\times10^{-27}\,\mathrm{kg}',175,338),
('phys20-unified-mass-unit-joules','Unified atomic mass unit in joules',r'1\,\mathrm{u}=1.4924\times10^{-10}\,\mathrm{J}',175,338),
('phys20-unified-mass-unit-electronvolts','Unified atomic mass unit in electron volts',r'1\,\mathrm{u}=931.5\,\mathrm{MeV}',175,339),
('phys20-mass-spectrograph-isotope-radius','Mass-spectrograph orbit radius',r'r=\sqrt{\frac{2Vm}{B^2q}}',175,338),
('phys20-binding-energy-nucleus','Nuclear binding energy',r'E_B=(ZM_{\mathrm p}+NM_{\mathrm N}-M)c^2',176,340),
('phys20-nuclear-mass-defect','Nuclear mass defect',r'\Delta m=ZM_{\mathrm p}+NM_{\mathrm N}-M',176,340),
('phys20-packing-fraction-binding-energy-per-nucleon','Binding energy per nucleon (called packing fraction in this text)',r'f=\frac{E_B}{A}',176,341),
('phys20-binding-energy-per-nucleon-packing-fraction','Binding energy per nucleon',r'f=\frac{E_B}{A}',177,342),
('phys20-sodium23-mass-defect-example','Sodium-23 mass defect, as printed',r'\Delta m=0.200286\,\mathrm u',177,343),
('phys20-sodium23-binding-energy-example','Sodium-23 binding energy, as printed',r'E_B=0.200286\times931.5=186.566\,\mathrm{MeV}',177,343),
('phys20-sodium23-packing-fraction-result','Sodium-23 binding energy per nucleon, as printed',r'f=\frac{186.566}{23}=8.11\,\mathrm{MeV}',178,344),
('phys20-carbon12-mass-defect-assignment','Carbon-12 mass defect (printed answer)',r'0.098940\,\mathrm u=1.6429\times10^{28}\,\mathrm{kg}',178,344),
('phys20-carbon12-binding-energy-assignment','Carbon-12 binding energy (printed answer)',r'92.16\,\mathrm{MeV}',178,344),
('phys20-alpha-decay-general','General alpha-decay equation',r'{}^{A}_{Z}\mathrm X\rightarrow{}^{A-4}_{Z-2}\mathrm Y+{}^{4}_{2}\mathrm{He}+Q',179,346),
('phys20-beta-minus-decay-general','General beta-minus decay equation',r'{}^{A}_{Z}\mathrm X\rightarrow{}^{A}_{Z+1}\mathrm Y+{}^{0}_{-1}\beta+\bar\nu+Q',179,347),
('phys20-positron-decay-general','General positron-decay equation',r'{}^{A}_{Z}\mathrm X\rightarrow{}^{A}_{Z-1}\mathrm Y+{}^{0}_{+1}\beta+\nu+Q',179,347),
('phys20-gamma-decay-general','General gamma-emission equation',r'({}^{A}_{Z}\mathrm X)^*={}^{A}_{Z}\mathrm X+\gamma',180,349),
('phys20-cobalt60-gamma-example','Cobalt-60 gamma-emission example',r'({}^{60}_{27}\mathrm{Co})^*={}^{60}_{27}\mathrm{Co}+\gamma',180,349),
('phys20-radium226-gamma-example','Radium-226 gamma-emission example',r'({}^{226}_{88}\mathrm{Ra})^*={}^{226}_{88}\mathrm{Ra}+\gamma',180,349),
('phys20-radioactive-decay-differential-law','Radioactive decay differential equation',r'\frac{\Delta N}{\Delta t}=-\lambda N',181,350),
('phys20-radioactive-decay-exponential-law','Radioactive decay law',r'N=N_0e^{-\lambda t}',181,351),
('phys20-half-life-decay-constant','Half-life and decay constant',r'T_{1/2}=\frac{\ln2}{\lambda}=\frac{0.693}{\lambda}',181,351),
('phys20-half-life','Half-life',r'T_{1/2}=\frac{0.693}{\lambda}',181,351),
('phys20-activity-equation','Activity',r'A=-\frac{\Delta N}{\Delta t}=\lambda N',182,352)]
NAMES_UR=['نیوکلیائی عددِ کمیت کا تعلق','نیوکلائیڈ کی علامت','آئن کی تعجیل اور حرکی توانائی','مقناطیسی انحراف','سپیکٹوگراف سے کمیت','ایٹمی کمیت کی اکائی کلوگرام میں','ایٹمی کمیت کی اکائی جول میں','ایٹمی کمیت کی اکائی الیکٹران وولٹ میں','کمیت پر منحصر مدار کا نصف قطر','نیوکلیائی بندشی توانائی','نیوکلیائی کمیتی نقص','فی نیوکلیون بندشی توانائی','فی نیوکلیون بندشی توانائی','سوڈیم23 کا کمیتی نقص، مطبوعہ صورت میں','سوڈیم23 کی بندشی توانائی، مطبوعہ صورت میں','سوڈیم23 کی فی نیوکلیون بندشی توانائی، مطبوعہ صورت میں','کاربن12 کا کمیتی نقص (مطبوعہ جواب)','کاربن12 کی بندشی توانائی (مطبوعہ جواب)','الفا زوال کی عمومی مساوات','بیٹا منفی زوال کی عمومی مساوات','پوزیٹرون زوال کی عمومی مساوات','گاما اخراج کی عمومی مساوات','کوبالٹ60 کے گاما اخراج کی مثال','ریڈیم226 کے گاما اخراج کی مثال','تابکار زوال کی تفاضلی مساوات','تابکار زوال کا قانون','نصف عمر اور زوال کا مستقل','نصف عمر','سرگرمی']
NAMES_PS=['د هستوي کتلې د شمېر اړیکه','د نوکلایډ نښه','د ایون تعجیل او حرکي انرژي','مقناطیسي انحراف','له سپېکټوګرافه کتله','د اټومي کتلې واحد په کیلوګرامونو کې','د اټومي کتلې واحد په جولونو کې','د اټومي کتلې واحد په الکترون ولټونو کې','د کتلې له مخې د مدار شعاع','هستوي د تړون انرژي','هستوي د کتلې کسر','د هر نوکلیون د تړون انرژي','د هر نوکلیون د تړون انرژي','د سوډیم23 د کتلې کسر، چاپ شوې بڼه','د سوډیم23 د تړون انرژي، چاپ شوې بڼه','د سوډیم23 د هر نوکلیون د تړون انرژي','د کاربن12 د کتلې کسر (چاپ شوی ځواب)','د کاربن12 د تړون انرژي (چاپ شوی ځواب)','د الفا زوال عمومي معادله','د بېټا منفي زوال عمومي معادله','د پوزیټرون زوال عمومي معادله','د ګاما خپرېدو عمومي معادله','د کوبالټ60 د ګاما خپرېدو بېلګه','د رادیم226 د ګاما خپرېدو بېلګه','د راډیواکټیف زوال تفاضلي معادله','د راډیواکټیف زوال قانون','د نیم ژوند او زوال ثابت','نیم ژوند','فعالیت']
formulas=[]
for i,(identity,name,latex,page,printed) in enumerate(rows):
    expression={'phys20-radioactive-decay-differential-law':r'\Delta N/\Delta t=-\lambda N','phys20-radioactive-decay-exponential-law':'N=N₀e⁻λᵗ'}.get(identity,latex)
    formulas.append({'id':identity,'name':name,'urduName':NAMES_UR[i],'pashtoName':NAMES_PS[i],
       'formula':expression,'latex':latex,'sourceClass12Physics':True,'sourceReferences':[REF(page,printed)]})
if __name__=='__main__':
    with shared_class_data_lock():
        sync_companions(chapter_index=9,definitions=definitions,replace_definitions=True,
            formulas=formulas,retire_formulas=['Textbook equation','phys20-binding-energy-per-nucleon-packing-fraction','phys20-half-life-decay-constant'],
            retire_exercises=['Exercise'],update_section_metadata=[{'id':'20.exercise.solved','values':{'title':'Supplemental authored solutions (not printed textbook answers)','authorship':'authored_supplement_not_printed'}}])
    print(f'Reconciled Unit20 to {len(definitions)} bilingual source glossary entries and {len(formulas)} rendered source equations; duplicate OCR exercise lists retired.')
