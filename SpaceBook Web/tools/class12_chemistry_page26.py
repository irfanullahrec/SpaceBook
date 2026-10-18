"""PDF26 printed44–45: exact questions/options, no inferred answer key."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def head(e,u,p):add(e,u,p,'heading')
head('Exercise','مشق','تمرین')
head('Q1. Choose the correct one from the given options.','سوال 1۔ دیے گئے اختیارات میں سے درست انتخاب کریں۔','پوښتنه 1. له ورکړل شوو انتخابونو څخه سم انتخاب کړئ.')
mcqs=[
('Electronegativity of Be is approximately equal to that of','Be کی برقی منفیت تقریباً کس کے برابر ہے؟','د Be برېښنا منفي توب نږدې د کوم یوه سره برابر دی؟',['Al','Mg','B','Na']),
('The elements which are most abundant in earth crust are:','زمین کی پرت میں سب سے زیادہ پائے جانے والے عناصر ہیں:','د ځمکې په پوټکي کې تر ټولو ډېر عناصر دا دي:',['Si and Al','Ca and Mg','B and Ar','B and Al']),
('Carbonates of Li are not stable like that of sodium due to','Li کے کاربونیٹس سوڈیم کے کاربونیٹ جیسے مستحکم نہیں، جس کی وجہ ہے:','د Li کاربونېټونه د سوډیم د کاربونېټ په څېر ثابت نه دي، لامل یې دا دی:',['low electronegativity.','low electropositivity.','high charge density of Li⁺.','low charge density of Li⁺.']),
('Which one of the following metal sulphates is not soluble in water','درج ذیل دھاتی سلفیٹس میں سے کون سا پانی میں حل پذیر نہیں؟','له لاندې فلزي سلفېټونو څخه کوم یو په اوبو کې نه حل کېږي؟',['Na₂SO₄','K₂SO₄','BaSO₄','ZnSO₄']),
('Which of the following alkali metal forms only normal oxide with O₂?','درج ذیل القلی دھاتوں میں سے کون سی O₂ کے ساتھ صرف عام آکسائیڈ بناتی ہے؟','له لاندې القلي فلزونو څخه کوم یو له O₂ سره یوازې عادي اکسایډ جوړوي؟',['Li','K','Na','Rb']),
('Strongest oxidizing agent among the halogens is','ہیلوجنز میں سب سے طاقت ور تکسیدی عامل ہے:','په هالوجنونو کې تر ټولو پیاوړی اکسیدوونکی عامل دا دی:',['Cl₂','F₂','Br₂','I₂']),
('Which of the following has the lowest electron affinity?','درج ذیل میں سے کس کی الیکٹرون الفت سب سے کم ہے؟','له لاندې څخه کوم یو د الکترون تر ټولو کم میلان لري؟',['F','I','Cl','Br']),
('Which of the following halide has the highest melting point?','درج ذیل ہیلائیڈز میں سے کس کا نقطۂ پگھلاؤ سب سے بلند ہے؟','له لاندې هالایډونو څخه کوم یو د وېلې کېدو تر ټولو لوړ ټکی لري؟',['NaCl','NaBr','NaF','NaI']),
('The highest boiling point of HF amongst the hydrogen halides is due to','ہائیڈروجن ہیلائیڈز میں HF کے سب سے بلند نقطۂ ابال کی وجہ ہے:','په هایدروجن هالایډونو کې د HF د اېشېدو د تر ټولو لوړ ټکي لامل دا دی:',['lowest electronegativity of F.','highest electronegativity of F.','lowest atomic weight of F.','lowest atomic radius of F.']),
('Which of the following is acidic in nature?','درج ذیل میں سے کون سا تیزابی نوعیت رکھتا ہے؟','له لاندې څخه کوم یو تېزابي ماهیت لري؟',['Al₂O₃','CO₂','SnO₂','CaO']),
('Third period element that initially reacts rapidly with oxygen to form a protective oxide coating that prevents further reactions is','تیسرے دور کا وہ عنصر جو ابتدا میں آکسیجن سے تیزی سے تعامل کر کے حفاظتی آکسائیڈ تہہ بناتا ہے، جو مزید تعاملات روکتی ہے:','د درېیمې دورې هغه عنصر چې په پیل کې له اکسیجن سره ژر تعامل کوي او د اکسایډ ساتونکې طبقه جوړوي چې د نورو تعاملونو مخه نیسي، دا دی:',['Na','Al','Si','Mg']),
('Which of the following has a greater affinity for oxygen?','درج ذیل میں سے کس کی آکسیجن کے لیے الفت زیادہ ہے؟','له لاندې څخه کوم یو د اکسیجن لپاره ډېر میلان لري؟',['B','Na','K','Mg']),
('Which of the following is the strongest base','درج ذیل میں سے کون سا سب سے مضبوط اساس ہے؟','له لاندې څخه کوم یو تر ټولو پیاوړی اساس دی؟',['Si(OH)₄','Be(OH)₂','Mg(OH)₂','Al(OH)₃']),
('The inert pair effect dominates in','غیر فعال جوڑے کا اثر کس میں غالب ہے؟','د غیر فعالې جوړې اغېز په کوم یوه کې غالب دی؟',['Pb','Sn','C','Si']),
('The elements of Group–IVA which have no tendency to form a dichloride are','گروپ IVA کے وہ عناصر جن میں ڈائی کلورائیڈ بنانے کا رجحان نہیں ہے:','د IVA ګروپ هغه عناصر چې د ډای کلورایډ د جوړولو تمایل نه لري، دا دي:',['C and Si','P and Sn','Ga and C','Sn and Si']),
]
translated={'Si and Al':('Si اور Al','Si او Al'),'Ca and Mg':('Ca اور Mg','Ca او Mg'),'B and Ar':('B اور Ar','B او Ar'),'B and Al':('B اور Al','B او Al'),
 'C and Si':('C اور Si','C او Si'),'P and Sn':('P اور Sn','P او Sn'),'Ga and C':('Ga اور C','Ga او C'),'Sn and Si':('Sn اور Si','Sn او Si'),
 'low electronegativity.':('کم برقی منفیت۔','ټیټ برېښنا منفي توب.'),'low electropositivity.':('کم برقی مثبتیت۔','ټیټ برېښنا مثبت توب.'),
 'high charge density of Li⁺.':('Li⁺ کی زیادہ بار کثافت۔','د Li⁺ د چارج لوړ کثافت.'),'low charge density of Li⁺.':('Li⁺ کی کم بار کثافت۔','د Li⁺ د چارج ټیټ کثافت.'),
 'lowest electronegativity of F.':('F کی سب سے کم برقی منفیت۔','د F تر ټولو ټیټ برېښنا منفي توب.'),'highest electronegativity of F.':('F کی سب سے زیادہ برقی منفیت۔','د F تر ټولو لوړ برېښنا منفي توب.'),
 'lowest atomic weight of F.':('F کا سب سے کم ایٹمی وزن۔','د F تر ټولو لږ اټومي وزن.'),'lowest atomic radius of F.':('F کا سب سے کم ایٹمی رداس۔','د F تر ټولو کوچنۍ اټومي شعاع.')}
for i,(e,u,p,options) in enumerate(mcqs,1):
 add(f'{i}. '+e,f'{i}. '+u,f'{i}. '+p)
 for tag,v in zip('abcd',options):
  ur,ps=translated.get(v,(v,v));add(f'{tag}. '+v,f'{tag}. '+ur,f'{tag}. '+ps,'list')
head('Q2. Write short answers of the following questions.','سوال 2۔ درج ذیل سوالات کے مختصر جواب لکھیں۔','پوښتنه 2. د لاندې پوښتنو لنډ ځوابونه ولیکئ.')
short=[
('Give the reason that the nitrates and carbonates of Group –IIA elements are thermally stable.','وجہ بتائیں کہ گروپ IIA کے عناصر کے نائٹریٹس اور کاربونیٹس حرارتی طور پر مستحکم کیوں ہیں۔','لامل ووایئ چې د IIA ګروپ د عناصرو نایټرېټونه او کاربونېټونه ولې له حرارتي پلوه ثابت دي.'),
('Write down at least four characteristics of Group-IIA elements.','گروپ IIA کے عناصر کی کم از کم چار خصوصیات لکھیں۔','د IIA ګروپ د عناصرو لږ تر لږه څلور ځانګړنې ولیکئ.'),
('Give reason(s) that why carbonates of Group – IA elements are more thermally stable than those of Group – IIA.','وجوہ بیان کریں کہ گروپ IA کے عناصر کے کاربونیٹس گروپ IIA سے زیادہ حرارتی طور پر مستحکم کیوں ہیں۔','لاملونه ووایئ چې د IA ګروپ د عناصرو کاربونېټونه ولې د IIA ګروپ له کاربونېټونو څخه ډېر حرارتي ثبات لري.'),
('Justify that beryllium chloride is different from the chlorides of its group.','واضح کریں کہ بیریلیم کلورائیڈ اپنے گروپ کے کلورائیڈز سے مختلف ہے۔','ثابته کړئ چې بېریلیم کلورایډ د خپل ګروپ له کلورایډونو څخه توپیر لري.'),
('Explain the structure and stability of chlorides of Group – IVA elements.','گروپ IVA کے عناصر کے کلورائیڈز کی ساخت اور استحکام سمجھائیں۔','د IVA ګروپ د عناصرو د کلورایډونو جوړښت او ثبات تشریح کړئ.'),
('Why fluorine is stronger oxidizing agent than chlorine?','فلورین کلورین سے زیادہ مضبوط تکسیدی عامل کیوں ہے؟','فلورین ولې له کلورین څخه پیاوړی اکسیدوونکی عامل دی؟'),
('How would you test and confirm the amphoteric nature of Be(OH)₂.','Be(OH)₂ کی دو خصوصیتی نوعیت کو کیسے جانچیں اور ثابت کریں گے؟','د Be(OH)₂ امفوتېریک ماهیت به څنګه وازمویئ او تایید کړئ؟'),
('Why the atomic radius of argon is larger than all the member of third period?','آرگن کا ایٹمی رداس تیسرے دور کے تمام ارکان سے بڑا کیوں ہے؟','د ارګون اټومي شعاع ولې د درېیمې دورې له ټولو غړو لویه ده؟'),
('Why there is a fall in ionization energy at Al and Si in same period?','اسی دور میں Al اور Si پر آئنائزیشن توانائی میں کمی کیوں ہوتی ہے؟','په همدې دوره کې په Al او Si کې د ایون کېدو انرژي ولې کمېږي؟'),
('Give the reason(s) that the compounds of Sn⁴⁺ are covalent in nature while those of Sn²⁺ are ionic.','وجوہ بیان کریں کہ Sn⁴⁺ کے مرکبات اشتراکی، جبکہ Sn²⁺ کے آئنک کیوں ہیں۔','لاملونه ووایئ چې د Sn⁴⁺ مرکبات ولې کووالنټ دي، خو د Sn²⁺ مرکبات ایوني دي.'),
]
for tag,(e,u,p) in zip(['i','ii','iii','iv','v','vi','vii','viii','ix','x'],short):add(tag+'. '+e,tag+'. '+u,tag+'. '+p)
head('Q3. Write detail answers of the following questions.','سوال 3۔ درج ذیل سوالات کے تفصیلی جواب لکھیں۔','پوښتنه 3. د لاندې پوښتنو تفصیلي ځوابونه ولیکئ.')
long=[
('Explain halide ions as reducing agents and discuss their trends in reducing strength.','ہیلائیڈ آئنوں کو تخفیفی عوامل کے طور پر سمجھائیں اور ان کی تخفیفی طاقت کے رجحانات پر بحث کریں۔','هالایډ ایونونه د ارجاع کوونکو عواملو په توګه تشریح کړئ او د هغوی د ارجاع ځواک پر تمایلاتو بحث وکړئ.'),
('Why the bond enthalpy is important in the thermal stability of hydrogen halides?','ہائیڈروجن ہیلائیڈز کے حرارتی استحکام میں بند کی اینتھالپی کیوں اہم ہے؟','د هایدروجن هالایډونو په حرارتي ثبات کې د تړون انتالپي ولې مهمه ده؟'),
('Give the reason(s) that why simple oxides, peroxides and superoxide of Group – II A elements are formed?','وجوہ بتائیں کہ گروپ IIA کے عناصر کے سادہ آکسائیڈز، پرآکسائیڈز اور سپرآکسائیڈ کیوں بنتے ہیں؟','لاملونه ووایئ چې د IIA ګروپ د عناصرو ساده اکسایډونه، پراکسایډونه او سوپراکسایډ ولې جوړېږي؟'),
('What is meant by inert pair effect? Explain inert pair effects in formation of ionic and covalent bond.','غیر فعال جوڑے کے اثر سے کیا مراد ہے؟ آئنک اور اشتراکی بند کی تشکیل میں اس اثر کو سمجھائیں۔','د غیر فعالې جوړې اغېز څه مانا لري؟ د ایوني او کووالنټ تړون په جوړولو کې دا اغېز تشریح کړئ.'),
('Discuss the effect of heat on nitrates, carbonates and hydrogen carbonates of Group–II A elements?','گروپ IIA کے عناصر کے نائٹریٹس، کاربونیٹس اور ہائیڈروجن کاربونیٹس پر حرارت کے اثر پر بحث کریں۔','د IIA ګروپ د عناصرو پر نایټرېټونو، کاربونېټونو او هایدروجن کاربونېټونو د تودوخې پر اغېز بحث وکړئ.'),
('Discuss in detail acid base behaviour of Group – IVA oxides.','گروپ IVA کے آکسائیڈز کے تیزابی اور اساسی رویے پر تفصیلی بحث کریں۔','د IVA ګروپ د اکسایډونو پر تېزابي او اساسي چلند تفصیلي بحث وکړئ.'),
('Explain acid-base behaviour of oxides of third period elements.','تیسرے دور کے عناصر کے آکسائیڈز کا تیزابی اور اساسی رویہ سمجھائیں۔','د درېیمې دورې د عناصرو د اکسایډونو تېزابي او اساسي چلند تشریح کړئ.'),
('Enlist the properties of hydroxides of third period elements.','تیسرے دور کے عناصر کے ہائیڈرو آکسائیڈز کی خصوصیات کی فہرست بنائیں۔','د درېیمې دورې د عناصرو د هایدروکسایډونو ځانګړنې په لست کې ولیکئ.'),
('Explain the bond enthalpies in halogens and bond enthalpies in hydrogen halides.','ہیلوجنز اور ہائیڈروجن ہیلائیڈز میں بندوں کی اینتھالپیاں سمجھائیں۔','په هالوجنونو او هایدروجن هالایډونو کې د تړونونو انتالپۍ تشریح کړئ.'),
('Analyse the halide ions as reducing agents and trends in reducing strength of halides ions.','ہیلائیڈ آئنوں کو تخفیفی عوامل کے طور پر اور ان کی تخفیفی طاقت کے رجحانات کا تجزیہ کریں۔','هالایډ ایونونه د ارجاع کوونکو عواملو په توګه او د هغوی د ارجاع ځواک تمایلات تحلیل کړئ.'),
]
for i,(e,u,p) in enumerate(long):
 prefix=f'{i//2+1}. ({"a" if i%2==0 else "b"}). ';add(prefix+e,prefix+u,prefix+p)
head('Project','پروجیکٹ','پروژه')
add('Perform an experiment that will enable you to differentiate and identify the elements present in salt using flame test. Record your observation in the table form.',
    'ایسا تجربہ کریں جس سے شعلے کے امتحان کے ذریعے نمک میں موجود عناصر میں فرق اور ان کی شناخت کر سکیں۔ اپنے مشاہدات جدول کی صورت میں درج کریں۔',
    'داسې تجربه ترسره کړئ چې د لمبې د ازموینې په وسیله په مالګه کې شته عناصر سره بېل او وپېژنئ. خپل مشاهدات د جدول په بڼه ثبت کړئ.')
rows=[[v,'','','',''] for v in ['Colour of the salt','Colour of the flame','Element identified']]
blocks.append({'id':'chem12-project-flame-observations','headers':['Salt name','','','',''],'rows':rows,'translations':[{'language':'اردو','headers':['نمک کا نام','','','',''],'rows':[[v,'','','',''] for v in ['نمک کا رنگ','شعلے کا رنگ','شناخت شدہ عنصر']]},{'language':'پښتو','headers':['د مالګې نوم','','','',''],'rows':[[v,'','','',''] for v in ['د مالګې رنګ','د لمبې رنګ','پېژندل شوی عنصر']]}]});layout.append({'type':'sourceDataTable','tableId':blocks[-1]['id']})
record=section('13.21','Unit13 exercises and flame-test project','یونٹ 13 کی مشقیں اور شعلے کے امتحان کا پروجیکٹ','د 13 واحد تمرینونه او د لمبې د ازموینې پروژه',paras,layout,blocks,'44–45');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':26,'printedPages':[44,45]}];record['sourceExerciseAnswerStatus']='No printed answer key; handwritten ticks excluded.'
issues=[{'id':'chem12-p45-ionization-question','printedPage':45,'description':'Short questionix asks about a fall in ionization energy at Al and Si; the earlier source table has the second anomaly at S. Exact printed question retained.'}]
if __name__=='__main__':save(26,[record],issues=issues)
