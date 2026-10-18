"""PDF47 printed86–87: coal conversion and seven organic characteristics."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
add('15.2 Coal as a Source of Organic Compounds','15.2 کوئلہ بطور نامیاتی مرکبات کا ماخذ','15.2 سکاره د عضوي مرکباتو د سرچینې په توګه','heading')
add('Coal is a rich source of organic compounds. It can be converted into many organic compounds by the following ways.','کوئلہ نامیاتی مرکبات کا بھرپور ماخذ ہے۔ درج ذیل طریقوں سے بہت سے نامیاتی مرکبات میں بدل سکتا ہے۔','سکاره د عضوي مرکباتو بډایه سرچینه ده. په لاندې لارو په ډېرو عضوي مرکباتو بدلېدای شي.')
add('15.2.1 Destructive Distillation of Coal','15.2.1 کوئلے کی تخریبی کشید','15.2.1 د سکرو تخریبي تقطیر','heading')
add('When coal is heated in the absence of air, it does not burn but produces many by-products. This process of heating coal in the absence of air is called destructive distillation of coal. The main products obtained by the destructive distillation of coal are:',
 'ہوا کے بغیر کوئلہ گرم کریں تو جلتا نہیں بلکہ بہت سے ضمنی حاصل بناتا ہے۔ یہ عمل کوئلے کی تخریبی کشید ہے۔ اس سے حاصل بنیادی مصنوعات ہیں:',
 'چې سکاره له هوا پرته توده شي، نه سوځي خو ډېر فرعي محصولات جوړوي. له هوا پرته د سکرو تودولو دا بهیر تخریبي تقطیر دی. اصلي ترلاسه شوي محصولات دا دي:')
for row in [('i. Coke','i. کوک','i. کوک'),('ii. Coal Tar','ii. کول تار','ii. د سکرو قیر'),('iii. Ammoniacal Liquor','iii. امونیائی محلول','iii. امونیایي محلول'),('iv. Coal gas','iv. کول گیس','iv. د سکرو ګاز')]:add(*row,'list')
add('i. Coke','i. کوک','i. کوک','heading')
add('Coke is a fuel which is used in homes and factories but it is mainly used in industries as reducing agent for the extraction of metals from their ores.',
 'کوک گھروں اور کارخانوں کا ایندھن ہے، لیکن بنیادی طور پر صنعتوں میں خام دھاتوں سے دھاتیں نکالنے کے لیے تخفیفی عامل ہے۔',
 'کوک په کورونو او فابریکو کې سون دی، خو په عمده توګه په صنعتونو کې له خامو مادو د فلزونو د ایستلو لپاره احیاکوونکی دی.')
add('ii. Coal Tar','ii. کول تار','ii. د سکرو قیر','heading')
add('One of the products of coal is coal tar, which is a mixture of organic compounds. These can be separated by fractional distillation. The compounds, so obtained can be used for making soap, fats, dyes, plastics, perfume, drugs, pesticides, explosives. On fractional distillation, coal tar gives important organic compounds like benzene, toluene, xylene, phenol, cresol, naphthalene, anthracene etc.',
 'کوئلے کا ایک حاصل کول تار ہے، جو نامیاتی مرکبات کا آمیزہ ہے۔ جزوی کشید سے الگ کر سکتے ہیں۔ حاصل مرکبات صابن، چکنائی، رنگ، پلاسٹک، خوشبو، ادویات، حشرات کش اور دھماکہ خیز مواد بنانے میں ہیں۔ جزوی کشید سے بینزین، ٹولیوئن، زائلین، فینول، کریسول، نیفتھلین اور اینتھراسین وغیرہ ملتے ہیں۔',
 'د سکرو یو محصول قیر دی چې د عضوي مرکباتو مخلوط دی. په جزوي تقطیر جلا کېدای شي. ترلاسه شوي مرکبات د صابون، غوړو، رنګونو، پلاستیک، عطرونو، درملو، افت وژونکو او چاودېدونکو موادو په جوړولو کارېږي. په جزوي تقطیر بنزین، تولوین، زایلین، فینول، کریسول، نفتالین او انتراسین ترلاسه کېږي.')
add('iii. Ammoniacal liquor','iii. امونیائی محلول','iii. امونیایي محلول','heading')
add('The other by product is ammonia solution called ammoniacal liquor which is used for making fertilizers like ammonium sulphate, ammonium superphosphate etc.',
 'دوسرا ضمنی حاصل امونیا محلول، امونیائی محلول، ہے جو امونیم سلفیٹ اور امونیم سپرفاسفیٹ جیسے کھادوں کے لیے ہے۔',
 'بل فرعي محصول د امونیا محلول، امونیایي محلول، دی چې د امونیم سلفېټ او امونیم سوپرفاسفېټ په څېر سرې جوړوي.')
add('iv. Coal gas','iv. کول گیس','iv. د سکرو ګاز','heading')
add('The coal gas is a mixture of hydrogen and carbon monoxide, which is combustible, making the coal gas an excellent fuel.','کول گیس ہائیڈروجن اور کاربن مونو آکسائیڈ کا قابل احتراق آمیزہ ہے، جو اسے بہترین ایندھن بناتا ہے۔','د سکرو ګاز د هایدروجن او کاربن مونو اکسایډ د سوځېدو وړ مخلوط دی چې غوره سون یې ګرځوي.')
add('15.2.2 Conversion of Coal to Petroleum','15.2.2 کوئلے کو پٹرولیم میں تبدیل کرنا','15.2.2 د سکرو په پټرولیم بدلول','heading')
add('Coal gas, obtained from the destructive distillation of coal can be converted into petroleum by a process known as Fischer–Tropsch (FT) process. The Fischer – Tropsch process is a set of chemical reactions that convert a mixture of carbon monoxide and hydrogen into liquid hydrocarbons mainly alkanes.',
 'تخریبی کشید کی کول گیس فشر–ٹروپش (FT) عمل سے پٹرولیم میں بدل سکتی ہے۔ یہ کیمیائی تعاملات کا مجموعہ ہے جو کاربن مونو آکسائیڈ اور ہائیڈروجن کو مائع ہائیڈروکاربنوں، بنیادی طور پر الکینز، میں بدلتا ہے۔',
 'د تخریبي تقطیر د سکرو ګاز د فېشر–ټروپش (FT) په بهیر پټرولیم ته بدلېدای شي. دا د کیمیاوي تعاملونو ټولګه ده چې د کاربن مونو اکسایډ او هایدروجن مخلوط په مایع هایدروکاربنونو، په عمده توګه الکانونو، بدلوي.')
add('(2n + 1)H₂ + nCO → CₙH₂ₙ₊₂ + nH₂O','(2n + 1)H₂ + nCO → CₙH₂ₙ₊₂ + nH₂O','(2n + 1)H₂ + nCO → CₙH₂ₙ₊₂ + nH₂O','equation')
add('The conversion of CO to alkanes in presence of hydrogen involves hydrogenolysis of C–O bond and the formation of C–C bond. This process takes place in presence of transition metal catalysts (cobalt, iron, ruthenium or nickel etc.) at a temperature range 150–300°C.',
 'ہائیڈروجن کی موجودگی میں CO سے الکینز بننے میں C–O بند کی ہائیڈروجینولائسز اور C–C بند بننا شامل ہے۔ عمل عبوری دھاتی عمل انگیزوں (کوبالٹ، لوہا، روتھینیم یا نکل وغیرہ) کی موجودگی میں 150–300°C پر ہے۔',
 'د هایدروجن په شتون کې د CO په الکانونو بدلول د C–O تړون هایدروجینولایسس او د C–C تړون جوړېدل رانغاړي. بهیر د انتقالي فلزي کتلستونو (کوبالټ، اوسپنه، روتینیم یا نیکل) په شتون کې په 150–300°C کېږي.')
add('15.3 Characteristics of Organic Compounds','15.3 نامیاتی مرکبات کی خصوصیات','15.3 د عضوي مرکباتو ځانګړنې','heading')
add('The Following are some of the important characteristic features of organic compounds.','نامیاتی مرکبات کی بعض اہم امتیازی خصوصیات درج ذیل ہیں۔','د عضوي مرکباتو ځینې مهمې ځانګړنې لاندې دي.')
add('1. Unique Properties of Carbon','1. کاربن کی منفرد خصوصیات','1. د کاربن ځانګړې ځانګړنې','heading')
add('Carbon has the property of self linkage. It can link with hundreds and thousands of other carbon atoms to form long C – C chains or rings. This self–linkage of carbon atoms to form chains and ring compounds is called catenation.',
 'کاربن میں خود پیوندی کی خاصیت ہے۔ سینکڑوں اور ہزاروں دوسرے کاربن ایٹموں سے جڑ کر طویل C–C زنجیریں یا حلقے بنا سکتا ہے۔ زنجیر اور حلقوی مرکبات بنانے کی خود پیوندی کیٹینیشن ہے۔',
 'کاربن د ځان تړلو ځانګړنه لري. له سلګونو او زرګونو نورو کاربني اټومونو سره اوږده C–C ځنځیرونه یا کړۍ جوړوي. د ځنځیرونو او کړیزو مرکباتو جوړولو دا ځان تړل کټینېشن دی.')
add('Carbon can also form stable single and multiple bonds with each other and other atoms like hydrogen, oxygen, nitrogen, halogens, sulphur etc. As a result carbon forms a large number of organic compounds.',
 'کاربن ایک دوسرے اور ہائیڈروجن، آکسیجن، نائٹروجن، ہیلوجنز اور سلفر جیسے ایٹموں سے مستحکم یک اور کثیر بند بھی بناتا ہے۔ اس لیے بہت سے نامیاتی مرکبات بناتا ہے۔',
 'کاربن له یو بل او نورو اټومونو لکه هایدروجن، اکسیجن، نایتروجن، هالوجنونو او سلفر سره ثابت یوګوني او څوګوني تړونونه هم جوړوي. نو ډېر عضوي مرکبات جوړوي.')
add('2. Isomerism','2. آئسومرزم','2. ایزومېریزم','heading')
add('When two or more organic compounds have the same molecular formula but different structures, these are called isomers and this phenomenon is called isomerism.','دو یا زیادہ نامیاتی مرکبات کا سالماتی فارمولا یکساں مگر ساختیں مختلف ہوں تو آئسومرز اور مظہر آئسومرزم ہیں۔','چې دوه یا ډېر عضوي مرکبات یو شان مالیکولي فورمول خو بېلابېل جوړښتونه ولري، ایزومرونه او پدیده ایزومېریزم بلل کېږي.')
add('3. Non–Ionic Character','3. غیر آئنک نوعیت','3. غیر ایوني طبیعت','heading')
add('Majority of organic compounds mainly involve covalent bond between C–C and C–H, therefore, they are generally non–polar and have non–ionic characters.','بیشتر نامیاتی مرکبات میں بنیادی طور پر C–C اور C–H اشتراکی بند ہیں، اس لیے عموماً غیر قطبی اور غیر آئنک ہیں۔','ډېری عضوي مرکبات په عمده توګه C–C او C–H اشتراکي تړونونه لري، نو عموماً غیر قطبي او غیر ایوني دي.')
add('4. Solubility','4. حل پذیری','4. حل کېدنه','heading')
add('Solubility depends upon the forces of attraction between the solute and solvent molecules. A general principle of solubility is, “like dissolve like” i.e. polar solute dissolves in polar solvent and non-polar solute dissolves in non-polar solvent. Since the organic compound are formed by covalent bonds and are mostly non-ionic and almost non-polar, so most of the organic compounds are insoluble in water, while some are partially soluble but they are readily soluble in non–polar solvents like ether, benzene, carbon tetrachloride etc.',
 'حل پذیری حل شونده اور محلل کے سالموں کی کشش پر منحصر ہے۔ عمومی اصول مماثل مماثل کو حل کرتا ہے، یعنی قطبی حل شونده قطبی محلل اور غیر قطبی غیر قطبی محلل میں حل ہوتا ہے۔ نامیاتی مرکبات اشتراکی بندوں سے، بیشتر غیر آئنک اور تقریباً غیر قطبی ہیں، اس لیے بیشتر پانی میں ناقابل حل، بعض جزوی حل پذیر، مگر ایتھر، بینزین اور کاربن ٹیٹراکلورائیڈ جیسے غیر قطبی محللوں میں آسانی سے حل ہیں۔',
 'حل کېدنه د حل کېدونکي او محلل د مالیکولونو ترمنځ د جذب پر قوو پورې تړلې ده. عمومي اصل ورته ورته حلوي دی، یعنې قطبي حل کېدونکی په قطبي او غیر قطبي په غیر قطبي محلل کې حلېږي. عضوي مرکبات اشتراکي تړونونه لري، ډېری غیر ایوني او نږدې غیر قطبي دي، نو ډېری په اوبو کې نه حل کېږي، ځینې لږ حلېږي، خو په غیر قطبي محللونو لکه ایتر، بنزین او کاربن ټېټراکلورایډ کې په اسانۍ حلېږي.')
add('5. Rates of Organic Reactions','5. نامیاتی تعاملات کی رفتاریں','5. د عضوي تعاملونو سرعتونه','heading')
add('Bonds between atoms in organic molecules are formed by mutual sharing of electrons and for a chemical reaction to occur the existing bonds must be broken and new bonds are formed. Therefore, the organic reactions are slow.',
 'نامیاتی سالموں کے ایٹموں کے بند الیکٹرانوں کی باہمی شراکت سے ہیں؛ کیمیائی تعامل کے لیے موجود بند توڑنے اور نئے بنانے ہوتے ہیں۔ اس لیے نامیاتی تعاملات سست ہیں۔',
 'په عضوي مالیکولونو کې د اټومونو تړونونه د الکترونونو په متقابل شریکولو جوړېږي؛ د کیمیاوي تعامل لپاره شته تړونونه ماتېږي او نوي جوړېږي. نو عضوي تعاملونه ورو دي.')
add('6. Similar Structural features and behaviour (Homologous Series)','6. مماثل ساختی خصوصیات اور رویہ (ہم سلسلہ خاندان)','6. ورته جوړښتي ځانګړنې او چلند (همولوګ لړۍ)','heading')
add('Mostly organic compounds have similar structural features called functional group and similar physical and chemical properties. Therefore, they show similar behaviour to various chemical reactions. This similarity in behaviour has reduced the study of millions of organic compounds to a few classes of organic compounds or homologous series.',
 'بیشتر نامیاتی مرکبات کی مماثل ساختی خصوصیات، فعلی گروپ، اور مماثل طبیعی و کیمیائی خصوصیات ہیں۔ اس لیے مختلف تعاملات میں مماثل رویہ دکھاتے ہیں۔ اس مماثلت نے لاکھوں مرکبات کے مطالعے کو چند اقسام یا ہم سلسلہ خاندانوں تک محدود کیا ہے۔',
 'ډېری عضوي مرکبات ورته جوړښتي ځانګړنې، فعالي ګروپ، او ورته فزیکي او کیمیاوي ځانګړنې لري. نو په بېلابېلو تعاملونو کې ورته چلند ښيي. دې ورته والي د میلیونونو مرکباتو مطالعه څو ډلو یا همولوګ لړیو ته راکمه کړې ده.')
add('7. Polymerization','7. پولیمرائزیشن','7. پولیمریزېشن','heading')
add('Some organic compounds exhibit the phenomena of polymerization. For example, ethylene polymerizes to polyethylene.','بعض نامیاتی مرکبات پولیمرائزیشن دکھاتے ہیں۔ مثلاً ایتھیلین پولیمرائز ہوکر پولی ایتھیلین بنتا ہے۔','ځینې عضوي مرکبات پولیمریزېشن ښيي. لکه ایتیلین په پولیمریزېشن پولي ایتیلین جوړوي.')
record=section('15.2','Coal conversion and organic characteristics','کوئلے کی تبدیلی اور نامیاتی خصوصیات','د سکرو بدلون او عضوي ځانګړنې',paras,layout,[],'86–87');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':47,'printedPages':[86,87]}]
if __name__=='__main__':save(47,[record],carry=[{'from':'15.2','to':'15.3','startsAt':'15.4 Uses of Organic Compounds'}],chapter_number=15)
