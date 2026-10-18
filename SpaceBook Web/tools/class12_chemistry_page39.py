"""PDF39 printed70–71, manganese oxidation and iron catalysis."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def eq(e):add(e,e,e,'equation')
eq('5CH₂=CH₂ + 2H₂O + 2MnO₄⁻ + 6H⁺ → 5HO—CH₂—CH₂—OH + 2Mn²⁺')
add('Under alkaline condition, the manganate (VII) ions (MnO₄⁻) are first reduced to green manganate (VI) ions.','اساسی شرط میں مینگنیٹ(VII) آئن (MnO₄⁻) پہلے سبز مینگنیٹ(VI) آئنوں میں تخفیف پاتے ہیں۔','په قلوي حالت کې منګنېټ(VII) ایونونه (MnO₄⁻) لومړی شنو منګنېټ(VI) ایونونو ته احیا کېږي.')
eq('CH₂=CH₂ + 2MnO₄⁻ + 2OH⁻ → HO—CH₂—CH₂—OH + 2MnO₄²⁻')
add('Dark green solution','گہرا سبز محلول','سخت شین محلول')
add('Then dark brown solid manganese (IV) oxide MnO₂ (manganese dioxide) is formed as a result of further reduction of MnO₄²⁻.','MnO₄²⁻ کی مزید تخفیف سے گہرا بھورا ٹھوس مینگنیز(IV) آکسائیڈ MnO₂ (مینگنیز ڈائی آکسائیڈ) بنتا ہے۔','د MnO₄²⁻ په نوره احیا سخت نسواري جامد منګنیز(IV) اکسایډ MnO₂ (منګنیز ډای اکسایډ) جوړېږي.','list')
eq('2CH₂=CH₂ + 2MnO₄²⁻ + 4H₂O → 2HO—CH₂—CH₂—OH + 2MnO₂ + 4OH⁻')
add('Dark brown precipitate','گہرا بھورا رسوب','سخت نسواري رسوب')
add('The net reaction is given as,','خالص تعامل یوں ہے،','خالص تعامل داسې دی،')
eq('3CH₂=CH₂ + 2MnO₄⁻ + 4H₂O → 3HO—CH₂—CH₂—OH + 2MnO₂ + 2OH⁻')
add('Dark brown precipitate','گہرا بھورا رسوب','سخت نسواري رسوب')
add('ii. In the Oxidation of Aromatic Side Chains','ii. ارومیٹک جانبی زنجیروں کی تکسید میں','ii. د اروماتیکو اړخیزو ځنځیرونو په اکسیدېشن کې','heading')
add('Alkaline potassium manganate (VII) solution oxidizes any hydrocarbon side chain attached to a benzene ring back to a single –COOH group. Prolonged heating is necessary. For example: as shown in the figure.',
 'اساسی پوٹاشیم مینگنیٹ(VII) محلول بینزین حلقے سے جڑی کسی بھی ہائیڈروکاربن جانبی زنجیر کو ایک –COOH گروپ میں تکسید کرتا ہے۔ طویل گرم کرنا ضروری ہے۔ مثال شکل میں ہے۔',
 'قلوي پوتاشیم منګنېټ(VII) محلول د بنزین کړۍ پورې تړلی هر هایدروکاربني اړخیز ځنځیر یوه –COOH ګروپ ته اکسیدوي. اوږده تودوخه اړینه ده. بېلګه په شکل کې ده.')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" role="img"><g font-family="Arial" font-size="22" fill="#222">'
for x,y,label in [(100,80,'CH₃'),(100,240,'CH₂CH₃'),(600,160,'COOH')]:
 svg+=f'<path d="M{x} {y-32}L{x+28} {y-16}V{y+16}L{x} {y+32}L{x-28} {y+16}V{y-16}Z" fill="none" stroke="#222" stroke-width="2"/><circle cx="{x}" cy="{y}" r="20" fill="none" stroke="#222"/><path d="M{x} {y-32}V{y-50}" stroke="#222"/><text x="{x-30}" y="{y-56}">{label}</text>'
svg+='<path d="M150 80L300 160L150 240M300 160H535" stroke="#222" stroke-width="2" fill="none"/><path d="M535 160L520 152V168Z"/><text x="340" y="130">Alkaline MnO₄⁻</text><text x="390" y="192">Heat</text><text x="540" y="225">Benzoic acid</text></g></svg>'
blocks.append({'id':'chem12-p70-aromatic-oxidation','svg':svg,'svgUrdu':svg.replace('Alkaline','اساسی').replace('Heat','حرارت').replace('Benzoic acid','بینزوئک تیزاب'),'svgPashto':svg.replace('Alkaline','قلوي').replace('Heat','تودوخه').replace('Benzoic acid','بنزویک اسید')});layout.append({'type':'visual','blockId':blocks[-1]['id']})
add('In case of the ethyl side chain, carbon dioxide is also produced but in each case, the main product is benzoic acid.','ایتھائل جانبی زنجیر کی صورت میں کاربن ڈائی آکسائیڈ بھی بنتی ہے، لیکن ہر صورت میں بنیادی حاصل بینزوئک تیزاب ہے۔','د ایتیل اړخیز ځنځیر په حالت کې کاربن ډای اکسایډ هم جوړېږي، خو په هر حالت کې اصلي محصول بنزویک اسید دی.')
add('14.3.3.3 Potassium Manganate (VII) as an Oxidizing Agent in Titrations','14.3.3.3 ٹائٹریشن میں پوٹاشیم مینگنیٹ(VII) بطور تکسیدی عامل','14.3.3.3 په تیتریشن کې پوتاشیم منګنېټ(VII) د اکسیدوونکي په توګه','heading')
add('KMnO₄ is a strong oxidizing agent with intense dark purple colour. During reduction, the purple permanganate ion changes into colourless Mn²⁺ ion.','KMnO₄ گہرے جامنی رنگ کا مضبوط تکسیدی عامل ہے۔ تخفیف کے دوران جامنی پرمینگنیٹ آئن بے رنگ Mn²⁺ آئن میں بدلتا ہے۔','KMnO₄ په سخت ارغواني رنګ پیاوړی اکسیدوونکی دی. د احیا پر مهال ارغواني پرمنګنېټ ایون په بې رنګه Mn²⁺ ایون بدلېږي.')
add('Potassium manganate (VII) solution is used to find the concentration of all sorts of reducing agents. It is always used in acidic solution.','پوٹاشیم مینگنیٹ(VII) محلول ہر قسم کے تخفیفی عاملوں کا ارتکاز معلوم کرنے کے لیے استعمال ہوتا ہے۔ ہمیشہ تیزابی محلول میں استعمال کرتے ہیں۔','پوتاشیم منګنېټ(VII) محلول د هر ډول احیاکوونکو د غلظت معلومولو لپاره کارېږي. تل په اسیدي محلول کې کارېږي.')
add('For example, it oxidizes','مثلاً یہ تکسید کرتا ہے','لکه دا اکسیدوي')
add('Iron(II) ions to iron(III) ions','آئرن(II) آئنوں کو آئرن(III) آئنوں میں','اوسپنې(II) ایونونه د اوسپنې(III) ایونونو ته','list')
eq('Fe²⁺ → Fe³⁺ + e⁻ (acidic)')
add('Hydrogen peroxide solution to oxygen','ہائیڈروجن پرآکسائیڈ محلول کو آکسیجن میں','هایدروجن پراکسایډ محلول اکسیجن ته','list')
eq('H₂O₂ → O₂ + 2H⁺ + 2e⁻')
add('Sulphite ions (IV) to sulphate ions (VI) ions','سلفائٹ(IV) آئنوں کو سلفیٹ(VI) آئنوں میں','سلفایټ(IV) ایونونه سلفېټ(VI) ایونونو ته','list')
eq('SO₃²⁻ + H₂O → SO₄²⁻ + 2H⁺ + 2e⁻')
add('In each case, the half-equation for the manganate (VII) ions in acidic solution is:','ہر صورت میں تیزابی محلول میں مینگنیٹ(VII) آئنوں کی نصف مساوات ہے:','په هر حالت کې په اسیدي محلول کې د منګنېټ(VII) ایونونو نیمه معادله دا ده:')
eq('MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O')
add('14.3.4 Iron','14.3.4 لوہا','14.3.4 اوسپنه','heading')
add('Iron is the second most abundant metal in the Earth’s crust. Concentrated deposits of iron ore are found in many localities, thus making it easy to mine. Iron is a transition metal with a symbol “Fe” and atomic number 26 and its atomic mass is 55.845 a.m.u.',
 'لوہا زمین کی پرت میں دوسری سب سے وافر دھات ہے۔ لوہے کی خام دھات کے مرتکز ذخائر بہت سے علاقوں میں ہیں، اس لیے کان کنی آسان ہے۔ لوہا عبوری دھات ہے، نشان Fe، جوہری عدد 26 اور جوہری کمیت 55.845 a.m.u. ہے۔',
 'اوسپنه د ځمکې په قشر کې دویم ډېر موندل کېدونکی فلز دی. د اوسپنې د خامې مادې متمرکزې زېرمې په ډېرو ځایونو کې دي، نو کان کیندنه یې اسانه ده. اوسپنه انتقالي فلز دی، نښه یې Fe، اټومي شمېره 26 او اټومي کتله 55.845 a.m.u. ده.')
add('14.3.4.1 Oxidation States','14.3.4.1 تکسیدی حالتیں','14.3.4.1 د اکسیدېشن حالتونه','heading')
add('Most common oxidation states of iron are +2 and +3 but it can also exists in the form of Fe⁴⁺, Fe⁵⁺ and Fe⁶⁺. The +6 oxidation state of Fe is very rare. The Fe²⁺ and Fe³⁺ oxidation states are stable states.',
 'لوہے کی عام ترین تکسیدی حالتیں +2 اور +3 ہیں، لیکن Fe⁴⁺، Fe⁵⁺ اور Fe⁶⁺ بھی ہو سکتا ہے۔ Fe کی +6 حالت بہت نایاب ہے۔ Fe²⁺ اور Fe³⁺ مستحکم حالتیں ہیں۔',
 'د اوسپنې تر ټولو عام اکسیدېشن حالتونه +2 او +3 دي، خو د Fe⁴⁺، Fe⁵⁺ او Fe⁶⁺ په بڼه هم شته. د Fe د +6 حالت ډېر نادر دی. Fe²⁺ او Fe³⁺ ثابت حالتونه دي.')
add('Iron in the +2 oxidation state is known as the ferrous ion. This ion is pale green in colour and is very easily oxidized to ferric ion. Even traces of dissolved oxygen in solution will complete this oxidation. Solution of ferrous ion is sometimes used as reducing agent.',
 'لوہے کی +2 حالت فیرس آئن ہے۔ یہ ہلکا سبز ہے اور بہت آسانی سے فیرک آئن میں تکسید پاتا ہے۔ محلول میں حل شدہ آکسیجن کی معمولی مقدار بھی یہ تکسید مکمل کرتی ہے۔ فیرس آئن کا محلول کبھی تخفیفی عامل ہے۔',
 'د اوسپنې د +2 حالت فېرس ایون بلل کېږي. دا سپک شین دی او په ډېرې اسانۍ فېرېک ایون ته اکسیدېږي. په محلول کې د حل شوي اکسیجن لږې نښې هم دا اکسیدېشن بشپړوي. د فېرس ایون محلول کله ناکله احیاکوونکی کارېږي.','list')
add('Most solutions containing ferric ions are usually yellow or yellow–brown due to formation of [Fe(H₂O)₅(OH)]²⁺. Fe³⁺(aq) yields a dark blue precipitate called Prussian blue, Fe₄[Fe(CN)₆]₃ is formed, when treated with potassium ferrocyanide, K₄[Fe(CN)₆](aq).',
 'فیرک آئنوں والے اکثر محلول [Fe(H₂O)₅(OH)]²⁺ بننے کی وجہ سے پیلے یا زرد بھورے ہیں۔ Fe³⁺(aq) کو پوٹاشیم فیروسائنائیڈ K₄[Fe(CN)₆](aq) سے عمل کرائیں تو گہرا نیلا رسوب پرشین بلیو Fe₄[Fe(CN)₆]₃ بنتا ہے۔',
 'د فېرېک ایونونو ډېری محلولونه د [Fe(H₂O)₅(OH)]²⁺ د جوړېدو له امله ژېړ یا ژېړ نسواري دي. Fe³⁺(aq) چې له پوتاشیم فېروسیانایډ K₄[Fe(CN)₆](aq) سره تعامل وکړي، سخت نیلي رسوب پروشین بلو Fe₄[Fe(CN)₆]₃ جوړېږي.','list')
add('14.3.4.2 Iron as Catalyst in Haber’s Process','14.3.4.2 ہیبر عمل میں لوہا بطور عمل انگیز','14.3.4.2 د هابر په بهیر کې اوسپنه د کتلست په توګه','heading')
add('In the Haber process, hydrogen reacts with nitrogen to produce ammonia. Without catalyst, the process would proceed too slowly to be economically viable. The reaction takes place according to the following steps:',
 'ہیبر عمل میں ہائیڈروجن نائٹروجن سے تعامل کرکے امونیا بناتی ہے۔ عمل انگیز کے بغیر عمل اتنا آہستہ ہوگا کہ اقتصادی طور پر قابل عمل نہیں۔ تعامل ان مراحل سے ہوتا ہے:',
 'د هابر په بهیر کې هایدروجن له نایتروجن سره تعامل کوي او امونیا جوړوي. له کتلست پرته به بهیر دومره ورو وي چې اقتصادي عملي نه وي. تعامل په دې پړاوونو کېږي:')
eq('N₂ + H₂ → N₂H₂');eq('N₂H₂ + H₂ → N₂H₄')
record=section('14.14','Manganate oxidation and iron','مینگنیٹ تکسید اور لوہا','منګنېټ اکسیدېشن او اوسپنه',paras,layout,blocks,'70–71');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':39,'printedPages':[70,71]}];record['sourceContinuesOnPdfPage']=40
if __name__=='__main__':save(39,[record],carry=[{'from':'14.14','to':'14.15','startsAt':'2NH,\nN2H, + H2'}],issues=[{'id':'chem12-p70-acidic-ethene-balance','printedPage':70,'description':'First printed acidic ethene equation contains 2H2O rather than balanced4H2O; retained.'}],chapter_number=14)
