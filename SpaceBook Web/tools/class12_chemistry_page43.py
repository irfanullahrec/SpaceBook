"""PDF43 printed78–79: all15MCQs,10short questions and first4long questions."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
add('Exercise','مشق','تمرین','heading')
add('Q1. Choose the correct option from the given options.','سوال1. دیے گئے اختیارات سے صحیح اختیار منتخب کریں۔','پوښتنه1. له ورکړل شوو اختیارونو سم اختیار غوره کړئ.','heading')
questions=[
('The diamagnetic ion is','ڈائی میگنیٹک آئن ہے','ډایمقناطیسي ایون دی',['Ni²⁺','Cr³⁺','Mn²⁺','Cu⁺'],None,None),
('Potassium ferrocyanide is a','پوٹاشیم فیروسائنائیڈ ہے','پوتاشیم فېروسیانایډ دی',['normal salt.','mixed salt.','double salt.','complex salt.'],['عام نمک۔','مخلوط نمک۔','دوہرا نمک۔','کمپلیکس نمک۔'],['عادي مالګه.','ګډه مالګه.','دوه ګونې مالګه.','کمپلېکس مالګه.']),
('The co-ordination compound [CuCl₄]²⁻ exists in the shape of','تناسقی مرکب [CuCl₄]²⁻ کی شکل ہے','د کواردینېشن مرکب [CuCl₄]²⁻ شکل دی',['tetrahedral.','octahedral.','square planner.','rhombic.'],['ٹیٹراہیڈرل۔','آکٹاہیڈرل۔','مربع مستوی۔','معینی۔'],['ټېټراهېډرل.','اوکتاهېډرل.','مربع مستوي.','معیني.']),
('The oxidation state of chromium in CrO₂Cl₂ is','CrO₂Cl₂ میں کرومیم کی تکسیدی حالت ہے','په CrO₂Cl₂ کې د کرومیم د اکسیدېشن حالت دی',['+2','+3','+4','+6'],None,None),
('[BeF₄]²⁻ is an example of','[BeF₄]²⁻ مثال ہے','[BeF₄]²⁻ بېلګه ده',['square planar','tetrahedral complex','bent structure','octahedral complex'],['مربع مستوی','ٹیٹراہیڈرل کمپلیکس','خمیدہ ساخت','آکٹاہیڈرل کمپلیکس'],['مربع مستوي','ټېټراهېډرل کمپلېکس','کږه جوړښت','اوکتاهېډرل کمپلېکس']),
('Which of the following is a typical transition element','مندرجہ ذیل میں کون سا حقیقی عبوری عنصر ہے','له لاندې کوم یو ځانګړی انتقالي عنصر دی',['Zn','Cd','Ra','Co'],None,None),
('The paramagnetic nature of a substance depends on','مادے کی پیرا میگنیٹک نوعیت منحصر ہے','د مادې پارامقناطیسي طبیعت تړلی دی',['the number of electron in the outer most orbit.','the number of electron that are easily ejected.','the number of un-paired electrons.','the number of lone pair of electrons.'],['بیرونی ترین مدار کے الیکٹرانوں کی تعداد پر۔','آسانی سے خارج ہونے والے الیکٹرانوں کی تعداد پر۔','غیر جوڑی دار الیکٹرانوں کی تعداد پر۔','تنہا الیکٹرانی جوڑوں کی تعداد پر۔'],['په بهرني مدار کې د الکترونونو په شمېر.','د په اسانۍ خارجېدونکو الکترونونو په شمېر.','د بې جوړې الکترونونو په شمېر.','د یوازینیو الکتروني جوړو په شمېر.']),
('Ligands are','لیگنڈز ہیں','لېګنډونه دي',['electron pair donors.','electron pair acceptors.','neutral.','donor and then acceptor.'],['الیکٹرانی جوڑے دینے والے۔','الیکٹرانی جوڑے قبول کرنے والے۔','بے بار۔','دینے والے اور پھر قبول کرنے والے۔'],['د الکتروني جوړې ورکوونکي.','د الکتروني جوړې منونکي.','خنثی.','ورکوونکي او بیا منونکي.']),
('Which one is not ferromagnetic?','کون سا فیرو میگنیٹک نہیں؟','کوم یو فېرومقناطیسي نه دی؟',['Fe','Co','Sb','Ni'],None,None),
('The co-ordination number of iron in [Fe(CN)₆]⁴⁻ is','[Fe(CN)₆]⁴⁻ میں لوہے کا تناسقی عدد ہے','په [Fe(CN)₆]⁴⁻ کې د اوسپنې کواردینېشن شمېره ده',['9','3','4','6'],None,None),
('Select ligand which is bidentate?','دو دندانی لیگنڈ منتخب کریں؟','دوه غاښیز لېګنډ غوره کړئ؟',['H₂O','NH₃','CO','C₂O₄²⁻'],None,None),
('Cu²⁺ salt solution is blue in colour due to transition of electron from','Cu²⁺ نمک کا محلول الیکٹران کی اس منتقلی کی وجہ سے نیلا ہے','د Cu²⁺ مالګې محلول د الکترون د دې انتقال له امله نیلي دی',['s to p orbital.','d to d orbital.','p to d orbital.','p to p orbital.'],['s سے p آربیٹل۔','d سے d آربیٹل۔','p سے d آربیٹل۔','p سے p آربیٹل۔'],['له s څخه p اوربیټال ته.','له d څخه d اوربیټال ته.','له p څخه d اوربیټال ته.','له p څخه p اوربیټال ته.']),
('Potassium dichromate acts as a strong','پوٹاشیم ڈائی کرومیٹ مضبوط ہوتا ہے','پوتاشیم ډای کرومېټ پیاوړی دی',['oxidizing agent.','reducing agent.','bleaching agent.','dehydrating agent.'],['تکسیدی عامل۔','تخفیفی عامل۔','رنگ اڑانے کا عامل۔','پانی نکالنے کا عامل۔'],['اکسیدوونکی.','احیاکوونکی.','رنګ سپینوونکی.','اوبه ایستونکی.']),
('One of the constituent of German silver is','جرمن سلور کا ایک جز ہے','د جرمن سلور یو جز دی',['Ag','Au','Cu','Al'],None,None),
('The names which remains unchanged in naming co-ordination compounds are','تناسقی مرکبات کی نام گذاری میں وہ نام جو نہیں بدلتے ہیں','د کواردینېشن مرکباتو په نومولو کې نه بدلېدونکي نومونه دي',['anionic ligands.','cationic ligands.','neutral ligands.','none of these.'],['منفی آئن والے لیگنڈز۔','مثبت آئن والے لیگنڈز۔','بے بار لیگنڈز۔','ان میں سے کوئی نہیں۔'],['منفي ایوني لېګنډونه.','مثبت ایوني لېګنډونه.','خنثی لېګنډونه.','له دې هېڅ یو.'])]
for n,(e,u,p,options,ur,ps) in enumerate(questions,1):
 add(f'{n}. {e}',f'{n}. {u}',f'{n}. {p}')
 for letter,e,u,p in zip('abcd',options,ur or options,ps or options):add(f'{letter}. {e}',f'{letter}. {u}',f'{letter}. {p}','list')
add('Q2. Write short answers of the following questions.','سوال2. درج ذیل سوالات کے مختصر جواب لکھیں۔','پوښتنه2. د لاندې پوښتنو لنډ ځوابونه ولیکئ.','heading')
short=[
('Give the reason that why Cu⁺ is diamagnetic but Cu²⁺ is paramagnetic.','وجہ بتائیں کہ Cu⁺ ڈائی میگنیٹک لیکن Cu²⁺ پیرا میگنیٹک کیوں ہے۔','دلیل ورکړئ چې ولې Cu⁺ ډایمقناطیسي خو Cu²⁺ پارامقناطیسي دی.'),
('Write down the electronic configuration of the first transition series.','پہلے عبوری سلسلے کی الیکٹرانی ترتیب لکھیں۔','د لومړي انتقالي لړۍ الکتروني ترتیب ولیکئ.'),
('Why the transition elements show the catalytic behaviour?','عبوری عناصر عمل انگیزی رویہ کیوں دکھاتے ہیں؟','انتقالي عناصر ولې کتلیتي چلند ښيي؟'),
('Give the reason that transition elements form the co-ordination compounds.','عبوری عناصر کے تناسقی مرکبات بنانے کی وجہ بتائیں۔','د انتقالي عناصرو د کواردینېشن مرکباتو د جوړولو دلیل ورکړئ.'),
('Explain why transition metals have variable oxidation states.','وضاحت کریں کہ عبوری دھاتوں کی تکسیدی حالتیں متغیر کیوں ہیں۔','روښانه کړئ چې ولې انتقالي فلزونه متغیر اکسیدېشن حالتونه لري.'),
('Justify the statement that “Scandium forms colourless and diamagnetic compounds”.','اس بیان کا جواز دیں کہ اسکینڈیم بے رنگ اور ڈائی میگنیٹک مرکبات بناتا ہے۔','دا بیان توجیه کړئ چې سکانډیم بې رنګه او ډایمقناطیسي مرکبات جوړوي.'),
('How do transition elements differ from s and p-block elements?','عبوری عناصر s اور p بلاک کے عناصر سے کیسے مختلف ہیں؟','انتقالي عناصر د s او p بلاک له عناصرو څنګه توپیر لري؟'),
('What is the oxidation state of chromium in [Cr(H₂O)₆]³⁺?','[Cr(H₂O)₆]³⁺ میں کرومیم کی تکسیدی حالت کیا ہے؟','په [Cr(H₂O)₆]³⁺ کې د کرومیم د اکسیدېشن حالت څه دی؟'),
('Give the reason that Fe is a catalyst in Haber process but not in the preparation of sulphuric acid.','وجہ بتائیں کہ Fe ہیبر عمل میں عمل انگیز لیکن سلفیورک تیزاب کی تیاری میں نہیں ہے۔','دلیل ورکړئ چې Fe د هابر په بهیر کې کتلست دی خو د سلفوریک اسید په جوړولو کې نه دی.'),
('Zn²⁺ salts are white while Cu²⁺ salts are coloured. Why?','Zn²⁺ نمکیات سفید جبکہ Cu²⁺ نمکیات رنگین ہیں۔ کیوں؟','د Zn²⁺ مالګې سپینې خو د Cu²⁺ مالګې رنګینې دي. ولې؟')]
for n,row in zip(['i','ii','iii','iv','v','vi','vii','viii','ix','x'],short):add(*[f'{n}. {t}' for t in row])
add('Q3. Write detail answers of the following questions.','سوال3. درج ذیل سوالات کے تفصیلی جواب لکھیں۔','پوښتنه3. د لاندې پوښتنو تفصیلي ځوابونه ولیکئ.','heading')
long=[
('1. (a). Write down the electronic structure of 3d elements.','1. (a). 3d عناصر کی الیکٹرانی ساخت لکھیں۔','1. (a). د 3d عناصرو الکتروني جوړښت ولیکئ.'),
('(b). Explain why the electronic configuration for chromium and copper differ from those assigned using the Aufbau principle.','(b). واضح کریں کہ کرومیم اور تانبے کی الیکٹرانی ترتیب آؤف باؤ اصول سے مقرر کردہ ترتیب سے کیوں مختلف ہے۔','(b). روښانه کړئ چې د کرومیم او مسو الکتروني ترتیبونه د اوفباو اصل له ټاکلو ترتیبونو ولې توپیر لري.'),
('2. (a). Explain the origin of colour in coordination compounds','2. (a). تناسقی مرکبات میں رنگ کی ابتدا واضح کریں۔','2. (a). په کواردینېشن مرکباتو کې د رنګ سرچینه روښانه کړئ.'),
('(b). What are the general characteristics of transition elements?','(b). عبوری عناصر کی عمومی خصوصیات کیا ہیں؟','(b). د انتقالي عناصرو عمومي ځانګړنې څه دي؟'),
('(c). Assess the catalytic nature of vanadium and iron.','(c). وینیڈیم اور لوہے کی عمل انگیزی نوعیت کا جائزہ لیں۔','(c). د وناډیم او اوسپنې کتلیتي طبیعت وارزوئ.'),
('3. Discuss in detail the nomenclature of co-ordination compounds with suitable examples.','3. مناسب مثالوں سے تناسقی مرکبات کی نام گذاری پر تفصیلی بحث کریں۔','3. د مناسبو بېلګو په مرسته د کواردینېشن مرکباتو پر نومولو تفصیلي بحث وکړئ.'),
('4. (a). Explain and write the reactions of Potassium Manganate (VII) as an oxidizing agent in organic chemistry.','4. (a). نامیاتی کیمیا میں پوٹاشیم مینگنیٹ(VII) بطور تکسیدی عامل کے تعاملات لکھیں اور واضح کریں۔','4. (a). په عضوي کیمیا کې د پوتاشیم منګنېټ(VII) د اکسیدوونکي په توګه تعاملونه ولیکئ او روښانه کړئ.'),
('(b). What are alloys? Describe some properties of an alloy that are different from the metals that compose it.','(b). آمیزے کیا ہیں؟ آمیزے کی کچھ ایسی خصوصیات بیان کریں جو اس کی جزوی دھاتوں سے مختلف ہیں۔','(b). الیاژونه څه دي؟ د الیاژ ځینې ځانګړنې بیان کړئ چې له جوړوونکو فلزونو یې توپیر لري.')]
for row in long:add(*row)
record=section('chem12-u14-exercise','Unit14 source exercise','یونٹ14 کی اصل مشق','د واحد14 اصلي تمرین',paras,layout,[],'78–79');record['insertBefore']='14.18';record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':43,'printedPages':[78,79]}];record['sourceContinuesOnPdfPage']=44
if __name__=='__main__':save(43,[record],trim=[{'id':'14.18','startsAt':'(b). Write down some important reactions'}],chapter_number=14)
