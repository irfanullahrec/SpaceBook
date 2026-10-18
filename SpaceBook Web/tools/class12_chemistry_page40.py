"""PDF40 printed72–73: surface catalysis and iron aqua-ion reactions."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def eq(e):add(e,e,e,'equation')
eq('N₂H₄ + H₂ → 2NH₃')
add('However, breaking the nitrogen triple bond to form N₂H₂ is very difficult and resulting compound is highly unstable and is likely to dissociate as soon as it is formed. The formation of N₂H₂ is highly endothermic. So the above reactions do not proceed easily without the use of catalyst.',
 'تاہم N₂H₂ بنانے کے لیے نائٹروجن کا سہرا بند توڑنا بہت مشکل ہے اور حاصل شدہ مرکب انتہائی غیر مستحکم ہے، اس لیے بنتے ہی تفریق پانے کا امکان ہے۔ N₂H₂ بننا بہت حرارت گیر ہے۔ اس لیے مذکورہ تعاملات عمل انگیز کے بغیر آسانی سے نہیں ہوتے۔',
 'خو د N₂H₂ د جوړولو لپاره د نایتروجن درې ګونی تړون ماتول ډېر ستونزمن دي او جوړ شوی مرکب ډېر ناثابت دی، نو ښایي له جوړېدو سره سم تجزیه شي. د N₂H₂ جوړېدل ډېر تودوخه جذبوونکي دي. نو پورته تعاملونه له کتلست پرته په اسانۍ نه کېږي.')
add('The hydrogen and nitrogen are adsorbed on metallic iron surface.','ہائیڈروجن اور نائٹروجن دھاتی لوہے کی سطح پر جذب سطحی ہوتے ہیں۔','هایدروجن او نایتروجن د فلزي اوسپنې پر سطح جذبېږي.')
eq('N₂(g) ⇌ N₂(ad)')
add('The hydrogen almost immediately splits into its component atoms by sharing or exchange of electrons with the catalyst surface.','ہائیڈروجن عمل انگیز کی سطح سے الیکٹرانوں کی شراکت یا تبادلے سے تقریباً فوراً اپنے جزوی ایٹموں میں تقسیم ہوتی ہے۔','هایدروجن د کتلست له سطحې سره د الکترونونو په شریکولو یا تبادلې نږدې سمدستي په خپلو جزوي اټومونو وېشل کېږي.')
eq('H₂(g) ⇌ 2H(ad)')
add('The nitrogen molecules split into their component atoms and they lock into the surface of the iron catalyst. This is the slowest step and so limits the rate of the entire process.',
 'نائٹروجن سالمے اپنے جزوی ایٹموں میں تقسیم ہوتے ہیں اور لوہے کے عمل انگیز کی سطح سے جڑ جاتے ہیں۔ یہ سب سے سست مرحلہ ہے، اس لیے پورے عمل کی رفتار محدود کرتا ہے۔',
 'د نایتروجن مالیکولونه په خپلو جزوي اټومونو وېشل کېږي او د اوسپنې د کتلست په سطحه نښلي. دا تر ټولو ورو پړاو دی، نو د ټول بهیر سرعت محدودوي.')
eq('N₂(ad) ⇌ 2N(ad)')
add('The hydrogen atoms migrate across the surface of the catalyst and react with nitrogen and produce ammonia molecules that are still bound to the surface.','ہائیڈروجن ایٹم عمل انگیز کی سطح پر حرکت کرتے، نائٹروجن سے تعامل کرتے اور امونیا سالمے بناتے ہیں جو اب بھی سطح سے بندھے ہیں۔','د هایدروجن اټومونه د کتلست پر سطح خوځېږي، له نایتروجن سره تعامل کوي او د امونیا مالیکولونه جوړوي چې لا هم له سطحې سره تړلي دي.')
eq('N(ad) + H(ad) → NH(ad)');eq('NH(ad) + H(ad) → NH₂(ad)');eq('NH₂(ad) + H(ad) → NH₃(ad)')
add('The assembled ammonia molecules are desorbed from surface in the form of gas','جوڑے گئے امونیا سالمے گیس کی صورت میں سطح سے خارج ہوتے ہیں','جوړ شوي امونیا مالیکولونه د ګاز په بڼه له سطحې خوشې کېږي')
eq('NH₃(ad) ⇌ NH₃(g)')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 430" role="img"><path d="M70 130Q320 330 650 130" fill="none" stroke="#bdc9c8" stroke-width="30"/><path d="M650 130L600 136L628 172Z" fill="#bdc9c8"/>'
for row in range(4):
 for col in range(15):svg+=f'<circle cx="{35+col*45+(row%2)*15}" cy="{285+row*35}" r="22" fill="#6f8584" stroke="#344c4b"/><circle cx="{29+col*45+(row%2)*15}" cy="{278+row*35}" r="7" fill="#d8e5e4" opacity=".8"/>'
for x,y in [(80,95),(120,180),(260,230),(420,240),(580,150),(620,70)]:
 svg+=f'<circle cx="{x}" cy="{y}" r="9" fill="#202020"/><circle cx="{x+14}" cy="{y+9}" r="6" fill="#e5e5e5" stroke="#555"/>'
for dx,dy in [(-14,8),(3,-14)]:svg+=f'<circle cx="{620+dx}" cy="{70+dy}" r="6" fill="#eee" stroke="#555"/>'
svg+='<path d="M10 97H42V86L66 105L42 124V113H10Z" fill="#222"/><path d="M655 87H683V76L707 95L683 114V103H655Z" fill="#222"/></svg>'
blocks.append({'id':'chem12-figure14-8','svg':svg,'svgUrdu':svg,'svgPashto':svg});layout.append({'type':'visual','blockId':blocks[-1]['id']})
add('Figure 14.8 Catalytic action of iron surface in Haber process.','شکل 14.8 ہیبر عمل میں لوہے کی سطح کا عمل انگیزی عمل۔','شکل 14.8 د هابر په بهیر کې د اوسپنې د سطحې کتلیتي عمل.')
add('14.3.4.3 Iron as Catalyst in Reaction between Persulphate and Iodide Ions','14.3.4.3 پرسلفیٹ اور آئیوڈائیڈ آئنوں کے تعامل میں لوہا بطور عمل انگیز','14.3.4.3 د پرسلفېټ او ایوډایډ ایونونو په تعامل کې اوسپنه د کتلست په توګه','heading')
add('The reaction between persulphate ions (peroxodisulphate ions), S₂O₈²⁻, and iodide ions in solution can be catalysed using either iron (II) or iron (III) ions. The overall equation for the reaction is,',
 'محلول میں پرسلفیٹ آئنوں (پیروآکسوڈائی سلفیٹ آئنوں) S₂O₈²⁻ اور آئیوڈائیڈ آئنوں کا تعامل آئرن(II) یا آئرن(III) آئنوں سے عمل انگیزی پا سکتا ہے۔ مجموعی مساوات ہے،',
 'په محلول کې د پرسلفېټ ایونونو (پراکسوډای سلفېټ ایونونو) S₂O₈²⁻ او ایوډایډ ایونونو تعامل د اوسپنې(II) یا اوسپنې(III) ایونونو په کارولو کتلیز کېدای شي. عمومي معادله دا ده،')
eq('S₂O₈²⁻ + 2I⁻ → 2SO₄²⁻ + I₂')
add('The catalyst used in this reaction is iron (II) ions. This reaction occurs in two steps.','اس تعامل کا عمل انگیز آئرن(II) آئن ہیں۔ تعامل دو مراحل میں ہے۔','په دې تعامل کې کتلست د اوسپنې(II) ایونونه دي. تعامل په دوو پړاوونو کېږي.')
eq('S₂O₈²⁻ + 2Fe²⁺ → 2SO₄²⁻ + 2Fe³⁺');eq('2Fe³⁺ + 2I⁻ → 2Fe²⁺ + I₂')
add('If you use iron (III) ions, the second of these reactions happens first.','آئرن(III) آئن استعمال کریں تو ان تعاملات میں دوسرا پہلے ہوتا ہے۔','که د اوسپنې(III) ایونونه وکاروئ، له دې تعاملونو دویم لومړی کېږي.')
add('14.3.4.4 Reactions of Hexaaquairon (II) and Hexaaquairon(III) with Water and Ammonia','14.3.4.4 پانی اور امونیا سے ہیکسا ایکوا آئرن(II) اور (III) کے تعاملات','14.3.4.4 له اوبو او امونیا سره د هېکسا اکوا اوسپنې(II) او (III) تعاملونه','heading')
add('Reactions of Hexaaquairon (II) with Water','پانی سے ہیکسا ایکوا آئرن(II) کے تعاملات','له اوبو سره د هېکسا اکوا اوسپنې(II) تعاملونه','heading')
add('Many hexaaqua complex ions can undergo acid base reactions with water to produce a solution of pH less than seven. These are not redox reactions because during the reaction no change in the oxidation state of central metal occurs e.g.',
 'بہت سے ہیکسا ایکوا کمپلیکس آئن پانی سے تیزاب–اساس تعامل کرکے سات سے کم pH والا محلول بناتے ہیں۔ یہ ریڈوکس تعاملات نہیں کیونکہ مرکزی دھات کی تکسیدی حالت نہیں بدلتی، مثلاً',
 'ډېر هېکسا اکوا کمپلېکس ایونونه له اوبو سره اسید–قلوي تعاملونه کوي او له اوو ټیټ pH لرونکی محلول جوړوي. دا ریډوکس تعاملونه نه دي ځکه د مرکزي فلز د اکسیدېشن حالت نه بدلېږي، لکه')
eq('[Fe(H₂O)₆]²⁺(aq) + H₂O(l) ⇌ [Fe(H₂O)₅(OH)]⁺ + H₃O⁺')
add('Reactions of Hexaaquairon (II) with Ammonia','امونیا سے ہیکسا ایکوا آئرن(II) کے تعاملات','له امونیا سره د هېکسا اکوا اوسپنې(II) تعاملونه','heading')
add('Ammonia can act as both a base and a ligand. In these cases, it simply acts as a base – removing hydrogen ions from the aqua complex.','امونیا اساس اور لیگنڈ دونوں ہو سکتا ہے۔ ان صورتوں میں صرف اساس ہے، ایکوا کمپلیکس سے ہائیڈروجن آئن نکالتا ہے۔','امونیا هم قلوي او هم لېګنډ کېدای شي. په دې حالتونو کې یوازې قلوي دی او له اکوا کمپلېکس څخه د هایدروجن ایونونه لرې کوي.')
eq('[Fe(H₂O)₆]²⁺ + 2NH₃ → [Fe(H₂O)₄(OH)₂] + 2NH₄⁺')
add('Reactions of Hexaaquairon (III) with Water','پانی سے ہیکسا ایکوا آئرن(III) کے تعاملات','له اوبو سره د هېکسا اکوا اوسپنې(III) تعاملونه','heading')
add('In iron (III) case,','آئرن(III) کی صورت میں،','د اوسپنې(III) په حالت کې،')
eq('[Fe(H₂O)₆]³⁺ + H₂O(l) ⇌ [Fe(H₂O)₅(OH)]²⁺ + H₃O⁺')
add('Fe³⁺ (ferric) gives more acidic solution than Fe²⁺ (ferrous) ions.','Fe³⁺ (فیرک)، Fe²⁺ (فیرس) آئنوں سے زیادہ تیزابی محلول دیتا ہے۔','Fe³⁺ (فېرېک) د Fe²⁺ (فېرس) ایونونو په پرتله ډېر اسیدي محلول ورکوي.')
add('Reactions of Hexaaquairon (III) with Ammonia','امونیا سے ہیکسا ایکوا آئرن(III) کے تعاملات','له امونیا سره د هېکسا اکوا اوسپنې(III) تعاملونه','heading')
add('In Fe(III) case','Fe(III) کی صورت میں','د Fe(III) په حالت کې')
eq('[Fe(H₂O)₆]³⁺ + 3NH₃ → [Fe(H₂O)₃(OH)₃] + 3NH₄⁺')
add('14.3.4.5 Reactions of Iron (II) and (III) Ions with Carbonate and Thiocyanate Ions','14.3.4.5 کاربونیٹ اور تھیوسائنائیٹ آئنوں سے آئرن(II) اور (III) آئنوں کے تعاملات','14.3.4.5 له کاربونېټ او تیوسیانېټ ایونونو سره د اوسپنې(II) او (III) ایونونو تعاملونه','heading')
add('There is an important difference between the behaviour of iron (II) and iron (III) ions.','آئرن(II) اور آئرن(III) آئنوں کے رویے میں اہم فرق ہے۔','د اوسپنې(II) او اوسپنې(III) ایونونو په چلند کې مهم توپیر شته.')
record=section('14.15','Iron catalysis and hexaaqua-ion reactions','لوہے کی عمل انگیزی اور ہیکسا ایکوا آئنوں کے تعاملات','د اوسپنې کتلیز او د هېکسا اکوا ایونونو تعاملونه',paras,layout,blocks,'72–73');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':40,'printedPages':[72,73]}];record['sourceContinuesOnPdfPage']=41
if __name__=='__main__':save(40,[record],carry=[{'from':'14.15','to':'14.16','startsAt':'Iron (II) Ions and Carbonate Tons'}],chapter_number=14)
