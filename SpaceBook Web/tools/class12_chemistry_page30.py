"""PDF30 printed52–53: oxidation states, catalysts, magnetism and alloys."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def head(e,u,p):add(e,u,p,'heading')
add('The lowest oxidation states of these elements are +1 or +2 which is due to their 4s electrons.',
    'ان عناصر کی کم ترین تکسیدی حالتیں +1 یا +2 ہیں، جو ان کے 4s الیکٹرونوں کی وجہ سے ہیں۔',
    'د دې عناصرو تر ټولو ټیټ د اکسیدېشن حالتونه +1 یا +2 دي، چې د هغوی د 4s الکترونونو له امله دي.')
add('As the number of unpaired electrons in 3d orbital increases the number of oxidation state also increases form Sc³⁺ to Mn⁷⁺.',
    '3d آربیٹل میں غیر جوڑا الیکٹرونوں کی تعداد بڑھنے پر تکسیدی حالتوں کی تعداد بھی Sc³⁺ سے Mn⁷⁺ تک بڑھتی ہے۔',
    'په 3d اوربیټل کې د بې جوړې الکترونونو د شمېر په زیاتېدو د اکسیدېشن حالتونو شمېر هم له Sc³⁺ څخه Mn⁷⁺ ته زیاتېږي.')
add('After Mn, the number of oxidation states decreases as the electrons starts pairing in 3d orbital and hence fewer unpaired electrons are available for bond formation, so oxidation states decreases from Fe to Zn. From iron to zinc only the weakly held electrons of “4s” subshell are involved in oxidation state.',
    'Mn کے بعد تکسیدی حالتوں کی تعداد کم ہوتی ہے، کیونکہ 3d آربیٹل میں الیکٹرون جوڑے بنانے لگتے ہیں اور بند بنانے کے لیے کم غیر جوڑا الیکٹرون دستیاب ہوتے ہیں؛ اس لیے Fe سے Zn تک تکسیدی حالتیں کم ہوتی ہیں۔ لوہے سے زنک تک صرف 4s ذیلی خول کے کمزور بندھے الیکٹرون تکسیدی حالت میں حصہ لیتے ہیں۔',
    'له Mn وروسته د اکسیدېشن حالتونو شمېر کمېږي، ځکه په 3d اوربیټل کې الکترونونه جوړې جوړوي او د تړون جوړولو لپاره لږ بې جوړې الکترونونه موجود وي؛ نو له Fe څخه Zn ته د اکسیدېشن حالتونه کمېږي. له اوسپنې څخه زنک ته یوازې د 4s فرعي پوښ کمزوري تړل شوي الکترونونه د اکسیدېشن په حالت کې برخه اخلي.')
add('Table 14.3 Commonly Occurring Oxidation States of the 1ˢᵗ Transition Series','جدول 14.3 پہلے عبوری سلسلے کی عام تکسیدی حالتیں','جدول 14.3 د لومړۍ انتقالي لړۍ عام د اکسیدېشن حالتونه')
names=['Scandium(Sc)','Titanium(Ti)','Vanadium(V)','Chromium(Cr)','Manganese(Mn)','Iron(Fe)','Cobalt(Co)','Nickel(Ni)','Copper(Cu)','Zinc(Zn)']
ur=['اسکینڈیم(Sc)','ٹائٹینیم(Ti)','وینیڈیم(V)','کرومیم(Cr)','مینگنیز(Mn)','لوہا(Fe)','کوبالٹ(Co)','نکل(Ni)','تانبا(Cu)','زنک(Zn)'];ps=['سکانډیم(Sc)','ټایټانیم(Ti)','وانادیم(V)','کرومیم(Cr)','منګنیز(Mn)','اوسپنه(Fe)','کوبالټ(Co)','نیکل(Ni)','مس(Cu)','زنک(Zn)']
d=[1,2,3,5,5,6,7,8,10,10];s=[2,2,2,1,2,2,2,2,1,2];states=['2 3','2 3 4','2 3 4 5','2 3 4 5 6','1 2 3 4 5 6 7','1 2 3 4 5 6','2 3 4 5','2 3 4','1 2 3','2'];sup=str.maketrans('0123456789','⁰¹²³⁴⁵⁶⁷⁸⁹')
rows=[[names[i],str(21+i),f'[Ar]4s{str(s[i]).translate(sup)}, 3d{str(d[i]).translate(sup)}',states[i]] for i in range(10)]
blocks.append({'id':'chem12-table-14-3','headers':['Element name','Atomic number','Electronic configuration','Oxidation states'],'rows':rows,'translations':[{'language':'اردو','headers':['عنصر کا نام','ایٹمی نمبر','الیکٹرونی ترتیب','تکسیدی حالتیں'],'rows':[[ur[i]]+r[1:] for i,r in enumerate(rows)]},{'language':'پښتو','headers':['د عنصر نوم','اټومي شمېره','الکتروني ترتیب','د اکسیدېشن حالتونه'],'rows':[[ps[i]]+r[1:] for i,r in enumerate(rows)]}]});layout.append({'type':'sourceDataTable','tableId':blocks[-1]['id']})
head('14.1.5 Catalytic Activity','14.1.5 عمل انگیزی','14.1.5 کتلیستي فعالیت')
add('Many transition metals and their compounds are used as catalysts, which influence the rate of chemical reaction.',
    'کئی عبوری دھاتیں اور ان کے مرکبات عمل انگیز کے طور پر استعمال ہوتے ہیں، جو کیمیائی تعامل کی رفتار پر اثر ڈالتے ہیں۔',
    'ډېر انتقالي فلزونه او د هغوی مرکبات د کتلیستونو په توګه کارېږي، چې د کیمیاوي تعامل پر چټکتیا اغېز لري.')
add('Some common examples are platinum (Pt), nickel (Ni), iron (Fe), chromium (Cr) and vanadium pentoxide (V₂O₅) etc. They are used as catalyst either because of their ability to change oxidation state or in the case of metals adsorbs other substance on their surface and activate them in the process.',
    'عام مثالیں پلاٹینم (Pt)، نکل (Ni)، لوہا (Fe)، کرومیم (Cr) اور وینیڈیم پینٹاآکسائیڈ (V₂O₅) وغیرہ ہیں۔ انہیں تکسیدی حالت بدلنے کی صلاحیت، یا دھاتوں کی صورت میں دوسرے مادے کو سطح پر جذب کر کے فعال کرنے کی وجہ سے عمل انگیز کے طور پر استعمال کرتے ہیں۔',
    'ځینې عامې بېلګې پلاټینم (Pt)، نیکل (Ni)، اوسپنه (Fe)، کرومیم (Cr) او وانادیم پېنټاکسایډ (V₂O₅) او نور دي. هغوی د اکسیدېشن حالت د بدلولو د وړتیا له امله، یا د فلزونو په حالت کې پر سطحه د بلې مادې د جذب او فعالولو له امله، د کتلیست په توګه کارېږي.')
add('Transition metals have variable oxidation states and hence are capable of forming intermediate compounds, which help in the formation of desired product. For example, finely divided iron is used as a catalyst in Haber’s process for the synthesis of ammonia, while V₂O₅ is used in the conversion of SO₂ to SO₃ for the manufacture of H₂SO₄ by contact process. TiCl₄ is used in the polymerization of ethene to polythene polymer.',
    'عبوری دھاتیں متغیر تکسیدی حالتیں رکھتی ہیں، اس لیے درمیانی مرکبات بنا سکتی ہیں، جو مطلوبہ پیداوار کی تشکیل میں مدد دیتے ہیں۔ مثلاً باریک تقسیم شدہ لوہا امونیا بنانے کے ہیبر عمل میں عمل انگیز ہے، جبکہ V₂O₅ رابطہ عمل سے H₂SO₄ بنانے میں SO₂ کو SO₃ میں بدلنے کے لیے استعمال ہوتا ہے۔ TiCl₄ ایتھین سے پولی تھین پولیمر بنانے میں استعمال ہوتا ہے۔',
    'انتقالي فلزونه بدلېدونکي د اکسیدېشن حالتونه لري، نو منځګړي مرکبات جوړولای شي چې د مطلوب محصول په جوړولو کې مرسته کوي. د بېلګې په توګه نرۍ وېشل شوې اوسپنه د امونیا د جوړولو په هابر بهیر کې کتلیست دی، خو V₂O₅ د تماس په بهیر کې د H₂SO₄ د جوړولو لپاره د SO₂ په SO₃ په بدلولو کې کارېږي. TiCl₄ د اېتین په پولیمرایزېشن کې د پولیتین پولیمر د جوړولو لپاره کارېږي.')
add('The application of nickel (Ni), palladium (Pd) or platinum (Pt) in the catalytic hydrogenation of unsaturated hydrocarbons and the use of copper (Cu) in the oxidation of ethanol to acetaldehyde are example of catalytic properties of transition elements.',
    'غیر سیر شدہ ہائیڈروکاربنز کی عمل انگیزی ہائیڈروجنیشن میں نکل (Ni)، پیلیڈیم (Pd) یا پلاٹینم (Pt)، اور ایتھانول کی ایسیٹیلڈیہائیڈ میں تکسید میں تانبے (Cu) کا استعمال عبوری عناصر کی عمل انگیزی خصوصیات کی مثالیں ہیں۔',
    'د ناپوره هایدروکاربنونو په کتلیستي هایدروجنېشن کې د نیکل (Ni)، پالادیم (Pd) یا پلاټینم (Pt) کارول او د اېتانول په اسېټالډیهایډ په اکسیدولو کې د مسو (Cu) کارول د انتقالي عناصرو د کتلیستي ځانګړنو بېلګې دي.')
head('14.1.6 Magnetic Behaviour','14.1.6 مقناطیسی رویہ','14.1.6 مقناطیسي چلند')
add('Substances show two different types of behaviours when subjected to an external magnetic field. If a substance is weakly attracted by a strong magnetic field, it is called paramagnetic substance, whereas a substance weakly repelled by magnetic field is called diamagnetic substance.',
    'بیرونی مقناطیسی میدان میں مادے دو مختلف قسم کے رویے دکھاتے ہیں۔ اگر مضبوط مقناطیسی میدان کسی مادے کو کمزور کشش سے کھینچے تو وہ پیرا مقناطیسی مادہ ہے، جبکہ میدان سے کمزور طور پر دور دھکیلا جانے والا مادہ ڈائی مقناطیسی کہلاتا ہے۔',
    'په بهرني مقناطیسي میدان کې مواد دوه ډوله چلند ښيي. که یو پیاوړی مقناطیسي میدان یوه ماده په کمزوري ډول راکاږي، پارامقناطیسي ماده بلل کېږي؛ خو هغه ماده چې میدان یې په کمزوري ډول دفع کوي، ډایامقناطیسي ماده بلل کېږي.')
add('Paramagnetic behaviour of a substance is due to interaction of magnetic field produced by spinning of one or more unpaired electrons in an atom, ion or molecule with external magnetic field.',
    'پیرا مقناطیسی رویہ ایٹم، آئن یا سالمے میں ایک یا زیادہ غیر جوڑا الیکٹرونوں کی گردش سے پیدا میدان اور بیرونی مقناطیسی میدان کے تعامل کی وجہ سے ہے۔',
    'د مادې پارامقناطیسي چلند په اټوم، ایون یا مالیکول کې د یوه یا ډېرو بې جوړې الکترونونو له سپین څخه د جوړ شوي مقناطیسي میدان او بهرني میدان د تعامل له امله دی.')
add('In diamagnetic substances the electrons are paired up due to which magnetic field of oppositely spinning electrons cancel each other.',
    'ڈائی مقناطیسی مادوں میں الیکٹرون جوڑوں میں ہیں، اس لیے مخالف گردش والے الیکٹرونوں کے مقناطیسی میدان ایک دوسرے کو منسوخ کرتے ہیں۔',
    'په ډایامقناطیسي موادو کې الکترونونه جوړې وي، نو د مخالف سپین لرونکو الکترونونو مقناطیسي میدانونه یو بل خنثی کوي.')
add('Metals like Fe, Co and Ni possess very high paramagnetic nature and attain permanent magnetic moment hence, they are ferromagnetic as shown by Fe³⁺ and Mn²⁺ ions which have five unpaired electrons each.',
    'Fe، Co اور Ni جیسی دھاتیں بہت زیادہ پیرا مقناطیسی نوعیت رکھتی ہیں اور مستقل مقناطیسی مومنٹ حاصل کرتی ہیں؛ اس لیے فیرومقناطیسی ہیں، جیسا کہ Fe³⁺ اور Mn²⁺ آئن دکھاتے ہیں، جن میں ہر ایک کے پانچ غیر جوڑا الیکٹرون ہیں۔',
    'د Fe، Co او Ni غوندې فلزونه ډېر لوړ پارامقناطیسي ماهیت لري او دایمي مقناطیسي مومنټ ترلاسه کوي؛ نو فېرومقناطیسي دي، لکه Fe³⁺ او Mn²⁺ ایونونه چې هر یو پنځه بې جوړې الکترونونه لري.')
head('14.1.7 Alloy Formation','14.1.7 مخلوط دھاتوں کی تشکیل','14.1.7 د الیاژ جوړېدل')
add('An alloy is a mixture of a metal with another element, either metal or non-metal. Transition metals have another great characteristic that they easily mix with each other. This is because all the d-block metals have similarity in their atomic sizes. Some transition metal atoms allow to replace easily in crystal lattice.',
    'مخلوط دھات ایک دھات اور دوسرے عنصر، دھات یا غیر دھات، کا آمیزہ ہے۔ عبوری دھاتوں کی ایک اور اہم خصوصیت یہ ہے کہ آسانی سے ایک دوسرے میں ملتی ہیں، کیونکہ d بلاک کی سب دھاتوں کی ایٹمی جسامتیں ملتی جلتی ہیں۔ بعض عبوری دھاتی ایٹم قلمی جالی میں آسانی سے بدل سکتے ہیں۔',
    'الیاژ له بل عنصر، فلز یا نافلز، سره د یوه فلز مخلوط دی. انتقالي فلزونه بله مهمه ځانګړنه لري چې په اسانه له یو بل سره ګډېږي، ځکه د d بلاک د ټولو فلزونو اټومي اندازې ورته دي. ځینې انتقالي فلزي اټومونه په بلوري جالۍ کې په اسانه بدلېدای شي.')
add('An alloy in which one of the components is mercury is known as amalgam. In alloys the chemical properties of the component elements are retained but certain physical properties are improved. Alloys are more shiny, stronger and harder than the pure metal. They are rigid, light weight, durable, thermally more stable, less reactive and corrosion resistant as compared to its component elements.',
    'وہ مخلوط دھات جس کا ایک جز پارہ ہو، املگم کہلاتی ہے۔ مخلوط دھاتوں میں اجزا کی کیمیائی خصوصیات برقرار رہتی ہیں، مگر بعض طبعی خصوصیات بہتر ہوتی ہیں۔ یہ خالص دھات سے زیادہ چمک دار، مضبوط اور سخت ہیں۔ اپنے اجزا کے مقابلے میں یہ مضبوط ساخت، ہلکا وزن، پائیداری، زیادہ حرارتی استحکام، کم تعامل پذیری اور خوردگی کے خلاف مزاحمت رکھتی ہیں۔',
    'هغه الیاژ چې یو جز یې سیماب وي، املګم بلل کېږي. په الیاژونو کې د جوړوونکو عناصرو کیمیاوي ځانګړنې ساتل کېږي، خو ځینې فزیکي ځانګړنې ښه کېږي. الیاژونه له خالص فلز څخه ډېر ځلېدونکي، پیاوړي او کلک دي. د خپلو جوړوونکو عناصرو په پرتله ټینګ، سپک، دوامدار، له حرارتي پلوه ډېر ثابت، لږ تعامل کوونکي او د زنګ پر وړاندې مقاوم دي.')
record=section('14.5','Oxidation states, catalysis, magnetism and alloys','تکسیدی حالتیں، عمل انگیزی، مقناطیسیت اور مخلوط دھاتیں','د اکسیدېشن حالتونه، کتلیستي فعالیت، مقناطیسیت او الیاژونه',paras,layout,blocks,'52–53');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':30,'printedPages':[52,53]}]
issues=[{'id':'chem12-p53-ferromagnetic-ions','printedPage':53,'description':'Printed text associates ferromagnetism of Fe/Co/Ni with isolated Fe3+/Mn2+ ions having five unpaired electrons. Assertion preserved; scientific review pending.'}]
if __name__=='__main__':save(30,[record],trim=[{'id':'14.6','startsAt':'Table 14.4 Important Alloys'}],issues=issues,chapter_number=14)
