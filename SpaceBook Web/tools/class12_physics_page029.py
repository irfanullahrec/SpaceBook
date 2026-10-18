import json
from pathlib import Path
from class12_source_review import upsert, section, checkpoint, sync_companions, OUT
from class12_physics_page013 import SOURCE, svg

MCQ = [
 (r'4.00\,\mathrm{N/C}. If an ion of charge \(+2e\) is released at rest at the left-hand plate, what is its kinetic energy when it reaches the right-hand plate?\nA. \(4\,\mathrm{eV}\)\nB. \(64\,\mathrm{eV}\)\nC. \(32\,\mathrm{eV}\)\nD. \(16\,\mathrm{eV}\)', r'\(4.00\,\mathrm{N/C}\)۔ اگر \(+2e\) بار کا آئن بائیں پلیٹ پر سکون سے چھوڑا جائے تو دائیں پلیٹ تک پہنچنے پر اس کی حرکی توانائی کیا ہوگی؟\nA. \(4\,\mathrm{eV}\)\nB. \(64\,\mathrm{eV}\)\nC. \(32\,\mathrm{eV}\)\nD. \(16\,\mathrm{eV}\)', r'\(4.00\,\mathrm{N/C}\). که د \(+2e\) چارج ایون په چپه تخته کې له سکون څخه خوشې شي، ښي تختې ته د رسېدو پر مهال حرکي انرژي به یې څومره وي؟\nA. \(4\,\mathrm{eV}\)\nB. \(64\,\mathrm{eV}\)\nC. \(32\,\mathrm{eV}\)\nD. \(16\,\mathrm{eV}\)'),
 (r'The electric potential between two points A and B is \(\Delta V\). The work \(W\) done by the field in moving a charge \(q\) from A to B is:', r'دو نقاط A اور B کے درمیان برقی پوٹینشل \(\Delta V\) ہے۔ بار \(q\) کو A سے B تک لے جانے میں میدان کا کیا ہوا کام \(W\) ہے؟', r'د A او B نقطو ترمنځ برېښنايي پوتنشیال \(\Delta V\) دی. د q چارج له A څخه B ته د لېږدولو پر مهال د میدان ترسره شوی کار \(W\) دی:'),
]
MCQ=[tuple(part.replace('\\n','\n') for part in row) for row in MCQ]
Q13OPTIONS=[r'A. \(W=-q\Delta V\)',r'B. \(W=q\Delta V\)',r'C. \(W=-q/\Delta V\)',r'D. \(W=\Delta V/q\)']
Q13UR=[r'A. \(W=-q\Delta V\)',r'B. \(W=q\Delta V\)',r'C. \(W=-q/\Delta V\)',r'D. \(W=\Delta V/q\)']
Q13PS=Q13UR
MCQ[1]=(MCQ[1][0]+'\n'+'\n'.join(Q13OPTIONS),MCQ[1][1]+'\n'+'\n'.join(Q13UR),MCQ[1][2]+'\n'+'\n'.join(Q13PS))

CONCEPTUAL=[
 ('The electric potential is constant through a given region of space. Is the electric field zero or non-zero in this region?', 'کسی خطۂ فضا میں برقی پوٹینشل مستقل ہے۔ کیا اس خطے میں برقی میدان صفر ہے یا غیر صفر؟', 'په یوه ورکړل شوې فضايي سیمه کې برېښنايي پوتنشیال ثابت دی. په دې سیمه کې برېښنايي میدان صفر دی که غیرصفر؟'),
 ('If a point charge q of mass m is released in a non-uniform electric field with field lines pointing in the same direction, will it make a rectilinear motion?', 'اگر کمیت m کا نقطوی بار q، غیر یکساں برقی میدان میں چھوڑا جائے اور میدان کی لکیریں ایک ہی سمت میں ہوں، تو کیا اس کی حرکت مستقیم ہوگی؟', 'که د m کتلې نقطوي چارج q په غیر یوشان برېښنايي میدان کې خوشې شي او د میدان کرښې په یوه لوري وي، ایا حرکت به یې مستقیم‌الخط وي؟'),
 ('What is the relationship between potential difference and electric potential energy?', 'فرقِ پوٹینشل اور برقی وضعی توانائی میں کیا تعلق ہے؟', 'د پوتنشیالي توپیر او برېښنايي وضعي انرژۍ ترمنځ څه اړیکه ده؟'),
 ('How are the units of volts and electron volts related? How do they differ?', 'وولٹ اور الیکٹران وولٹ کی اکائیوں میں کیا تعلق ہے؟ یہ ایک دوسرے سے کیسے مختلف ہیں؟', 'د ولټ او الکترون ولټ واحدونه څه اړیکه لري؟ دوی په څه توپیر لري؟'),
 ('How can electric potential be high when the electric potential energy is relatively low?', 'جب برقی وضعی توانائی نسبتاً کم ہو تو برقی پوٹینشل زیادہ کیسے ہو سکتا ہے؟', 'کله چې برېښنايي وضعي انرژي نسبتاً لږه وي، برېښنايي پوتنشیال څنګه لوړ کېدای شي؟'),
 ('Can the potential of a non-uniformly charged sphere be the same as that of a point charge?', 'کیا غیر یکساں طور پر باردار کرہ کا پوٹینشل نقطوی بار کے پوٹینشل جیسا ہو سکتا ہے؟', 'ایا د غیر یوشان چارج لرونکې کرې پوتنشیال د نقطوي چارج له پوتنشیال سره یو شان کېدای شي؟'),
 ('Will the energy stored in three capacitors be greater when they are connected in series or in parallel?', 'تین کیپیسٹر سلسلہ وار یا متوازی جوڑنے پر ذخیرہ توانائی زیادہ ہوگی؟', 'په درېیو کپاسیټرونو کې زېرمه شوې انرژي هغه وخت ډېره وي چې په لړۍ کې ونښلول شي که په موازي؟'),
 ('Can different equipotential lines cross each other?', 'کیا مختلف مساوی پوٹینشل لکیریں ایک دوسرے کو کاٹ سکتی ہیں؟', 'ایا د مساوي پوتنشیال بېلابېلې کرښې یو بل پرېکولی شي؟'),
 ('Water has a large dielectric constant, but it is rarely used in capacitors. Why?', 'پانی کا ڈائی الیکٹرک مستقل بڑا ہے، پھر بھی اسے کیپیسٹروں میں شاذ ہی کیوں استعمال کیا جاتا ہے؟', 'اوبه د ډای‌الکټریک لوی ثابت لري، خو په کپاسیټرونو کې ډېرې لږې کارول کېږي. ولې؟'),
 ('How can you increase the capacitance of a capacitor?', 'کیپیسٹر کی گنجائش کیسے بڑھائی جا سکتی ہے؟', 'د کپاسیټر ظرفیت څنګه زیاتولای شو؟'),
]

COMPREHENSIVE=[
 ('State and explain Coulomb’s law. Include the case when the charges are placed in dielectrics. Discuss how the unit of charge coulomb is defined.', 'کولمب کا قانون بیان کریں اور اس کی وضاحت کریں۔ اس صورت کو بھی شامل کریں جب بار ڈائی الیکٹرک میں رکھے ہوں۔ بحث کریں کہ بار کی اکائی کولومب کی تعریف کیسے کی جاتی ہے۔', 'د کولمب قانون بیان او تشریح کړئ. هغه حالت هم شامل کړئ چې چارجونه په ډای‌الکټریک کې وي. وڅېړئ چې د چارج واحد کولمب څنګه تعریف شوی دی.'),
 ('Explain the concept of electric field and hence define electric field intensity. Discuss the direction as well as the unit of E.', 'برقی میدان کا تصور واضح کریں اور اس سے برقی میدان کی شدت کی تعریف کریں۔ E کی سمت اور اکائی پر بھی بحث کریں۔', 'د برېښنايي میدان مفهوم تشریح او له مخې یې د برېښنايي میدان شدت تعریف کړئ. د E لوری او واحد هم وڅېړئ.'),
 ('Explain the concept of electric flux. Using mathematical expressions for electric flux, show how electric flux is maximum and minimum.', 'برقی فلوکس کا تصور واضح کریں۔ برقی فلوکس کی ریاضیاتی مساوات استعمال کر کے دکھائیں کہ یہ کب زیادہ سے زیادہ اور کب کم سے کم ہوتا ہے۔', 'د برېښنايي فلوکس مفهوم تشریح کړئ. د فلوکس د ریاضيکي څرګندونو په کارولو وښيئ چې فلوکس کله اعظمي او کله لږ تر لږه وي.'),
 ('State and prove Gauss’s law for electrostatics. Also discuss its applications with daily-life examples.', 'برق ساکنات کے لیے گاؤس کا قانون بیان اور ثابت کریں۔ روزمرہ زندگی کی مثالوں کے ساتھ اس کے استعمالات بھی بیان کریں۔', 'د الکتروستاتیک لپاره د ګاوس قانون بیان او ثابت کړئ. د ورځني ژوند له بېلګو سره یې کارونې هم وڅېړئ.'),
 ('Explain the concept of electric potential. Derive an expression for electric potential at a field point due to a source charge.', 'برقی پوٹینشل کا تصور واضح کریں۔ منبع بار کے باعث میدان کے کسی نقطے پر برقی پوٹینشل کی مساوات اخذ کریں۔', 'د برېښنايي پوتنشیال مفهوم تشریح کړئ. د سرچینې چارج له امله په یوه ساحوي نقطه کې د پوتنشیال لپاره رابطه مشتقه کړئ.'),
 ('Describe the construction of a capacitor and derive an expression for the energy stored in a capacitor.', 'کیپیسٹر کی ساخت بیان کریں اور اس میں ذخیرہ توانائی کی مساوات اخذ کریں۔', 'د کپاسیټر جوړښت بیان او پکې د زېرمه شوې انرژۍ رابطه مشتقه کړئ.'),
 ('Describe the concept of equipotential surfaces and derive an expression for electric field as the negative of the potential gradient.', 'مساوی پوٹینشل سطحوں کا تصور بیان کریں اور برقی میدان کو پوٹینشل کے میلان کے منفی کے طور پر ظاہر کرنے کی مساوات اخذ کریں۔', 'د مساوي پوتنشیال سطحو مفهوم بیان او د برېښنايي میدان د پوتنشیال د منفي تدریجي په توګه رابطه مشتقه کړئ.'),
 ('Explain the phenomenon of electric polarization. Discuss how polarization accounts for the increase in capacitance when a dielectric is inserted between the plates of a capacitor.', 'برقی قطبیت کا مظہر واضح کریں۔ بیان کریں کہ کیپیسٹر کی پلیٹوں کے درمیان ڈائی الیکٹرک ڈالنے پر قطبیت گنجائش میں اضافے کی کیسے وضاحت کرتی ہے۔', 'د برېښنايي قطبي کېدو پدیده تشریح کړئ. وڅېړئ چې د کپاسیټر د تختو ترمنځ د ډای‌الکټریک اېښودل او قطبي کېدل د ظرفیت زیاتوالی څنګه تشریح کوي.'),
 ('Derive an expression for the capacitance of a parallel-plate capacitor when a dielectric is inserted between its plates.', 'متوازی پلیٹوں والے کیپیسٹر کی پلیٹوں کے درمیان ڈائی الیکٹرک ڈالنے پر اس کی گنجائش کی مساوات اخذ کریں۔', 'د موازي‌تختو کپاسیټر د ظرفیت رابطه هغه وخت مشتقه کړئ چې د تختو ترمنځ ډای‌الکټریک واچول شي.'),
 ('Describe the process of charging and discharging a capacitor. Give diagrams and mathematical expressions for the growth and decay of charge on the capacitor.', 'کیپیسٹر کو چارج اور ڈسچارج کرنے کا عمل بیان کریں۔ کیپیسٹر پر بار کے بڑھنے اور گھٹنے کے لیے خاکے اور ریاضیاتی مساوات دیں۔', 'د کپاسیټر د چارج او ډسچارج بهیر بیان کړئ. پر کپاسیټر د چارج د زیاتېدو او کمېدو لپاره شکلونه او ریاضيکي څرګندونې ورکړئ.'),
 ('Explain why capacitors are of little use for storing energy for normal domestic purposes such as lighting and heating.', 'وضاحت کریں کہ روشنی اور حرارت جیسے عام گھریلو مقاصد کے لیے توانائی ذخیرہ کرنے میں کیپیسٹر زیادہ کارآمد کیوں نہیں ہوتے۔', 'تشریح کړئ چې د روښانتیا او تودوخې په څېر د عادي کورنیو موخو لپاره د انرژۍ زېرمه کولو کې کپاسیټرونه ولې لږ ګټور دي.'),
]

NUMERICAL=[
 (r'What is the magnitude of the force of attraction between an iron nucleus bearing charge \(q=26e\) and its innermost electron, if the distance between them is \(1\times10^{-12}\,\mathrm m\)? (Answer: \(6\times10^{-3}\,\mathrm N\))', r'\(q=26e\) بار رکھنے والے لوہے کے مرکزے اور اس کے سب سے اندرونی الیکٹران کے درمیان کشش کی قوت کا مقدار معلوم کریں، اگر دونوں کے درمیان فاصلہ \(1\times10^{-12}\,\mathrm m\) ہو۔ (جواب: \(6\times10^{-3}\,\mathrm N\))', r'د \(q=26e\) چارج لرونکي د اوسپنې هستې او د هغې د تر ټولو دنني الکترون ترمنځ د جذب قوې اندازه ومومئ، که د دوی ترمنځ واټن \(1\times10^{-12}\,\mathrm m\) وي. (ځواب: \(6\times10^{-3}\,\mathrm N\))'),
]

def divider_svg(lang):
    caption={'en':'Question 12 — positive ion moving between parallel plates','ur':'سوال 12 — متوازی پلیٹوں کے درمیان مثبت آئن','ps':'12مه پوښتنه — د موازي تختو ترمنځ مثبت ایون'}[lang]
    body='<path d="M95 35V235M305 35V235" stroke="#334155" stroke-width="8"/><circle cx="180" cy="130" r="20" fill="#e0f2fe" stroke="#0369a1" stroke-width="3"/><text x="173" y="137" font-size="22">+</text><path d="M207 130H273" stroke="#0284c7" stroke-width="4" marker-end="url(#a)"/><text x="162" y="85">+2e</text><text x="160" y="273">left plate</text><text x="275" y="273">right plate</text>'
    return '<figure>'+svg(body,400,300,'Positive ion of charge plus 2e released at rest and moving rightward between two plates')+'<figcaption>'+caption+'</figcaption></figure>'

def make_record(identity,title,printed,rows,headings,visual=False):
    record={'id':identity,'title':title,'kind':'exercise','pdfPage':29,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[r[0] for r in rows]}
    layout=[{'type':'paragraph','indices':[i]} for i in range(len(rows))]
    if visual: layout.insert(1,{'type':'visual'})
    item=section(record,rows,layout,headings);item['kind']='exercise'
    if visual:
        item.update(diagramSvg=divider_svg('en'),diagramSvgUrdu=divider_svg('ur'),diagramSvgPashto=divider_svg('ps'));item['content']+=item['diagramSvg']
    return record,item

def problem(identity,qno,entry,pdf,printed,answer=None,origin='not_provided_in_textbook'):
    out={'id':identity,'qNo':str(qno),'question':entry[0],'questionUrdu':entry[1],'questionPashto':entry[2],'sourceReferences':[{'pdfPage':pdf,'printedPage':printed}],'solutionOrigin':origin}
    if answer is not None: out['answer']=answer;out['answerOrigin']='textbook'
    return out

def main():
    mcq_full=MCQ[0]
    mcq_full=(mcq_full[0],mcq_full[1],mcq_full[2])
    q13=MCQ[1]
    # Page 28 already records questions 1–12; this spread supplies q12 choices and q13.
    q13_full=(q13[0],q13[1],q13[2])
    r1,s1=make_record('phys12-front-exercise11-mcq-cont48','Exercise 11 — multiple-choice questions (continued)',48,[mcq_full,q13_full],('یونٹ 11 کی مشق — کثیر الانتخابی سوالات','د ۱۱م څپرکي تمرین — څو-غوراوي پوښتنې'),visual=True)
    r2,s2=make_record('phys12-front-conceptual48','Exercise 11 — Conceptual Questions',48,CONCEPTUAL,('تصوری سوالات','مفهومي پوښتنې'))
    r3,s3=make_record('phys12-front-comprehensive49','Exercise 11 — Comprehensive Questions',49,COMPREHENSIVE,('جامع سوالات','هر اړخیزې پوښتنې'))
    r4,s4=make_record('phys12-front-numerical49','Exercise 11 — Numerical Questions',49,NUMERICAL,('عددی سوالات','عددي پوښتنې'))
    upsert([r1,r2,r3,r4],[s1,s2,s3,s4])
    # Complete the MCQ companion group from its existing source-backed page-28 entries.
    companion=json.loads((OUT/'physics-companions.json').read_text(encoding='utf-8'))
    mcq=next(x for x in companion['exercises'] if x['id']=='textbook-exercise-11-mcq')
    q12=next(x for x in mcq['problems'] if x['qNo']=='12')
    q12['question']=MCQ[0][0].splitlines()[0];q12['questionUrdu']=MCQ[0][1].splitlines()[0];q12['questionPashto']=MCQ[0][2].splitlines()[0]
    q12['options']=MCQ[0][0].splitlines()[1:]
    q12['optionsUrdu']=MCQ[0][1].splitlines()[1:];q12['optionsPashto']=MCQ[0][2].splitlines()[1:]
    q12['diagramSvg']=divider_svg('en');q12['diagramSvgUrdu']=divider_svg('ur');q12['diagramSvgPashto']=divider_svg('ps')
    q12['sourceReferences'].append({'pdfPage':29,'printedPage':48})
    q13_stem=tuple(part.splitlines()[0] for part in q13_full)
    q13_problem=problem('textbook-exercise-11-q13','13',q13_stem,29,48)
    q13_problem['options']=q13_full[0].splitlines()[1:];q13_problem['optionsUrdu']=q13_full[1].splitlines()[1:];q13_problem['optionsPashto']=q13_full[2].splitlines()[1:]
    mcq['problems'].append(q13_problem)
    comp=[
      {'id':'textbook-exercise-11-conceptual','exercise':'Exercise 11','title':'Conceptual Questions','problems':[problem(f'textbook-exercise-11-conceptual-q{i}',i,x,29,48) for i,x in enumerate(CONCEPTUAL,1)]},
      {'id':'textbook-exercise-11-comprehensive','exercise':'Exercise 11','title':'Comprehensive Questions','problems':[problem(f'textbook-exercise-11-comprehensive-q{i}',i,x,29,49) for i,x in enumerate(COMPREHENSIVE,1)]},
      {'id':'textbook-exercise-11-numerical','exercise':'Exercise 11','title':'Numerical Questions','problems':[problem('textbook-exercise-11-numerical-q1',1,NUMERICAL[0],29,49,r'\(6\times10^{-3}\,\mathrm N\)','textbook answer')]},
    ]
    sync_companions(exercises=[mcq]+comp)
    checkpoint(29,'corrected_verified',[r1['id'],r2['id'],r3['id'],r4['id']],
      'Original spread rendered at 2.5x and inspected. MCQ 12 continuation and MCQ 13 transcribed with choices; its plate/ion figure rebuilt natively. Ten conceptual questions, eleven comprehensive questions and numerical question 1 transcribed in order. Only the printed numerical answer is retained; no other answers added.',printed_pages=[48,49])

if __name__=='__main__':
    main()
