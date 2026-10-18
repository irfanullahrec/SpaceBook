"""PDF15, printed22–23: thermal decomposition and coded carbonate polarization."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
import html
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
eq('2Na(s) + Cl₂(g) → 2NaCl(s)')
eq('2K(s) + Cl₂(g) → 2KCl(s)')
add('Reactivity of alkali metals with particular halogens increases from Li to Cs.',
    'مخصوص ہیلوجنوں کے ساتھ الکلی دھاتوں کی تعامل پذیری Li سے Cs تک بڑھتی ہے۔',
    'له ځانګړو هالوجنونو سره د القلي فلزونو د تعامل وړتیا له Li څخه Cs ته زیاتېږي.')
head('13.2.5 Effect of Heat on Nitrates, Carbonates and Hydrogen-Carbonates explaining the Trend in Terms of the Polarizing Ability of the Positive Ion',
     '13.2.5 نائٹریٹس، کاربونیٹس اور ہائیڈروجن کاربونیٹس پر حرارت کا اثر؛ مثبت آئن کی قطبی بنانے کی صلاحیت کے لحاظ سے رجحان کی وضاحت',
     '13.2.5 پر نایټرېټونو، کاربونېټونو او هایدروجن کاربونېټونو د تودوخې اغېز؛ د مثبت ایون د قطبي کولو د وړتیا له مخې د تمایل تشریح')
add('Compounds of Group – IA elements are more stable to heat than the corresponding compounds of Group – IIA elements with the exception of lithium compounds.',
    'لیتھیم کے مرکبات کے استثنا کے ساتھ، گروپ IA کے عناصر کے مرکبات گروپ IIA کے متعلقہ مرکبات سے زیادہ حرارتی استحکام رکھتے ہیں۔',
    'د لیتیم له مرکباتو پرته، د IA ګروپ د عناصرو مرکبات د IIA ګروپ له اړوندو مرکباتو څخه د تودوخې پر وړاندې ډېر ثابت دي.')
head('Effect of Heat on Nitrates','نائٹریٹس پر حرارت کا اثر','پر نایټرېټونو د تودوخې اغېز')
add('In Group – IA the lithium nitrates decomposes on the same way as the nitrates of Group – IIA. Group – IIA nitrates tend to decompose on heating to produce metal oxide, nitrogen dioxide (brown fumes) and oxygen.',
    'گروپ IA میں لیتھیم نائٹریٹ گروپ IIA کے نائٹریٹس کی طرح تحلیل ہوتا ہے۔ گروپ IIA کے نائٹریٹس گرم کرنے پر دھاتی آکسائیڈ، نائٹروجن ڈائی آکسائیڈ (بھورے دھوئیں) اور آکسیجن بنانے کا رجحان رکھتے ہیں۔',
    'په IA ګروپ کې لیتیم نایټرېټ د IIA ګروپ د نایټرېټونو په څېر تجزیه کېږي. د IIA ګروپ نایټرېټونه د تودولو پر مهال د فلزي اکسایډ، نایټروجن ډای اکسایډ (نسواري لوګیو) او اکسیجن د جوړولو تمایل لري.')
head('Tidbit','مختصر معلومات','لنډ معلومات')
add('The ability of a cation to distort an anion is known as its polarization power and the tendency of the anion to become polarized by the cation is known as its polarizability.',
    'کسی مثبت آئن کی منفی آئن کو بگاڑنے کی صلاحیت اس کی قطبی بنانے کی طاقت کہلاتی ہے، جبکہ مثبت آئن کے ذریعے قطبی بننے کا منفی آئن کا رجحان اس کی قطب پذیری کہلاتا ہے۔',
    'د مثبت ایون هغه وړتیا چې منفي ایون کږوي، د هغه د قطبي کولو ځواک بلل کېږي؛ او د مثبت ایون له خوا د منفي ایون د قطبي کېدو تمایل د هغه قطبي کېدونکې وړتیا بلل کېږي.')
add('Lithium nitrate on decomposition produces lithium oxide, nitrogen dioxide and oxygen.',
    'لیتھیم نائٹریٹ تحلیل ہو کر لیتھیم آکسائیڈ، نائٹروجن ڈائی آکسائیڈ اور آکسیجن بناتا ہے۔',
    'لیتیم نایټرېټ په تجزیه کې لیتیم اکسایډ، نایټروجن ډای اکسایډ او اکسیجن جوړوي.')
eq('4LiNO₃(s) —Δ→ 2Li₂O(s) + 4NO₂(g) + O₂(g)')
add('The rest of nitrates from sodium to caesium, however, do not decompose completely at low temperatures. At high temperature, the nitrates of these elements produce the respective metal nitrite (MNO₂) and oxygen, but no nitrogen dioxide. (Where M = Na, K, Rb and Cs)',
    'تاہم سوڈیم سے سیزیم تک باقی نائٹریٹس کم درجۂ حرارت پر مکمل تحلیل نہیں ہوتے۔ بلند درجۂ حرارت پر ان کے نائٹریٹس متعلقہ دھاتی نائٹرائٹ (MNO₂) اور آکسیجن بناتے ہیں، مگر نائٹروجن ڈائی آکسائیڈ نہیں بناتے۔ (جہاں M = Na، K، Rb اور Cs)',
    'خو له سوډیم څخه سیزیم پورې پاتې نایټرېټونه په ټیټه تودوخه کې بشپړ نه تجزیه کېږي. په لوړه تودوخه کې د دې عناصرو نایټرېټونه اړوند فلزي نایټرایټ (MNO₂) او اکسیجن جوړوي، خو نایټروجن ډای اکسایډ نه جوړوي. (چې M = Na، K، Rb او Cs دی)')
eq('2MNO₃(s) —Δ→ 2MNO₂(s) + O₂(g)')
add('As we go down the group, the decomposition of these metal nitrates becomes more difficult and higher temperature is required.',
    'گروپ میں نیچے جانے پر ان دھاتی نائٹریٹس کی تحلیل مشکل ہوتی جاتی ہے اور زیادہ درجۂ حرارت درکار ہوتا ہے۔',
    'په ګروپ کې ښکته تګ سره د دې فلزي نایټرېټونو تجزیه ستونزمنېږي او لوړه تودوخه اړینه وي.')
head('Effect of Heat on Carbonates','کاربونیٹس پر حرارت کا اثر','پر کاربونېټونو د تودوخې اغېز')
add('In Group – IA the lithium carbonate decomposes on the same way as the carbonates of Group – IIA. Group – IIA carbonates tend to decompose on heating to produce metal oxide and carbon dioxide.',
    'گروپ IA میں لیتھیم کاربونیٹ گروپ IIA کے کاربونیٹس کی طرح تحلیل ہوتا ہے۔ گروپ IIA کے کاربونیٹس گرم کرنے پر دھاتی آکسائیڈ اور کاربن ڈائی آکسائیڈ بنانے کا رجحان رکھتے ہیں۔',
    'په IA ګروپ کې لیتیم کاربونېټ د IIA ګروپ د کاربونېټونو په څېر تجزیه کېږي. د IIA ګروپ کاربونېټونه په تودولو سره د فلزي اکسایډ او کاربن ډای اکسایډ د جوړولو تمایل لري.')
add('In Group – IA, lithium carbonate behaves in the same way, producing lithium oxide and carbon dioxide',
    'گروپ IA میں لیتھیم کاربونیٹ اسی طرح برتاؤ کر کے لیتھیم آکسائیڈ اور کاربن ڈائی آکسائیڈ بناتا ہے۔',
    'په IA ګروپ کې لیتیم کاربونېټ په همدې ډول چلند کوي او لیتیم اکسایډ او کاربن ډای اکسایډ جوړوي.')
eq('Li₂CO₃(s) → Li₂O(s) + CO₂(g)')
add('The rest of the Group – IA carbonates do not decompose at low temperature, although at higher temperature this becomes possible. The decomposition temperatures again increase down the group.',
    'گروپ IA کے باقی کاربونیٹس کم درجۂ حرارت پر تحلیل نہیں ہوتے، اگرچہ بلند درجۂ حرارت پر یہ ممکن ہو جاتا ہے۔ گروپ میں نیچے جانے پر تحلیل کے درجۂ حرارت پھر بڑھتے ہیں۔',
    'د IA ګروپ پاتې کاربونېټونه په ټیټه تودوخه کې نه تجزیه کېږي، خو په لوړه تودوخه کې دا ممکنه کېږي. په ګروپ کې ښکته تګ سره د تجزیې تودوخې بیا لوړېږي.')
head('Effect of Heat on Hydrogen Carbonates','ہائیڈروجن کاربونیٹس پر حرارت کا اثر','پر هایدروجن کاربونېټونو د تودوخې اغېز')
add('The hydrogen carbonates of Group – IA are stable enough to exist as solid, although they do decompose easily on heating. For example,',
    'گروپ IA کے ہائیڈروجن کاربونیٹس اتنے مستحکم ہیں کہ ٹھوس حالت میں موجود رہ سکتے ہیں، اگرچہ گرم کرنے پر آسانی سے تحلیل ہو جاتے ہیں۔ مثلاً:',
    'د IA ګروپ هایدروجن کاربونېټونه دومره ثابت دي چې په جامد حالت کې موجودېدای شي، خو په تودولو سره په اسانه تجزیه کېږي. د بېلګې په توګه:')
eq('2NaHCO₃(s) → Na₂CO₃(s) + CO₂(g) + H₂O(g)')
head('Explaining the Trend in Terms of the Polarizing ability of the Positive Ion','مثبت آئن کی قطبی بنانے کی صلاحیت کے لحاظ سے رجحان کی وضاحت','د مثبت ایون د قطبي کولو د وړتیا له مخې د تمایل تشریح')
add('A small positive ion has a large amount of charge packed into a small volume of space. An ion with a high charge density has a clear distorting effect on any nearby negative ions. A larger positive ion has the same charge spread over a larger volume of space. Its charge density is therefore lower and it causes less distortion to nearby negative ions.',
    'ایک چھوٹے مثبت آئن میں کم حجم کے اندر زیادہ بار جمع ہوتا ہے۔ زیادہ بار کثافت والا آئن قریب کے منفی آئنوں کو واضح طور پر بگاڑتا ہے۔ بڑے مثبت آئن کا وہی بار زیادہ حجم میں پھیلا ہوتا ہے، اس لیے اس کی بار کثافت کم اور قریبی منفی آئنوں پر بگاڑ کا اثر کم ہوتا ہے۔',
    'په یوه کوچني مثبت ایون کې په لږ حجم کې ډېر چارج راټول وي. د لوړ چارج کثافت لرونکی ایون پر نږدې منفي ایونونو څرګند کږوونکی اغېز لري. لوی مثبت ایون هماغه چارج په لوی حجم کې خپور لري؛ نو د چارج کثافت یې ټیټ او پر نږدې منفي ایونونو د کږولو اغېز یې لږ وي.')
head('Polarizing the Carbonate ion','کاربونیٹ آئن کو قطبی بنانا','د کاربونېټ ایون قطبي کول')
add('The molecular structure of carbonate is given below:', 'کاربونیٹ کی سالماتی ساخت نیچے دی گئی ہے:','د کاربونېټ مالیکولي جوړښت لاندې ورکړل شوی دی:')
add('This figure shows two carbon-oxygen single bonds and one double bond, with two oxygen atoms each carrying a negative charge.',
    'یہ شکل کاربن اور آکسیجن کے دو یک بند اور ایک دوہرا بند دکھاتی ہے؛ دو آکسیجن ایٹموں میں سے ہر ایک پر منفی بار ہے۔',
    'دا شکل د کاربن او اکسیجن دوه واحد تړونونه او یو دوه ګونی تړون ښيي؛ د اکسیجن دوه اټومونه هر یو منفي چارج لري.')
structure='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 130" role="img" aria-label="carbonate two single bonds and one double bond"><g fill="#111827" font-size="19" text-anchor="middle"><text x="78" y="70">C</text><text x="24" y="70">O</text><text x="132" y="28">O⁻</text><text x="132" y="112">O⁻</text></g><path d="M37 61H65 M37 67H65 M87 55L118 30 M87 73L118 101" stroke="#111827" fill="none"/></svg>'
def visual(identity,svg,ur=None,ps=None,width=None):
    b={'id':identity,'svg':svg,'svgUrdu':ur or svg,'svgPashto':ps or svg}
    if width:b['sourceWidthRatio']=width
    blocks.append(b);layout.append({'type':'visual','blockId':identity})
visual('chem12-p23-carbonate-bonds',structure,width=.35)
add('In carbonate, bonds are identical and the charges are delocalized.',
    'کاربونیٹ میں بند یکساں ہوتے ہیں اور بار غیر مقامی ہوتا ہے۔',
    'په کاربونېټ کې تړونونه یو شان دي او چارجونه غیرموضعي دي.')
delocalized='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 150" role="img" aria-label="carbonate delocalized charge 2 minus"><path d="M36 63C26 38 51 40 67 55C73 43 78 12 99 21C128 24 105 53 81 66C104 77 127 104 103 116C78 126 75 95 67 78C41 97 25 88 36 63Z" fill="#fff" stroke="#111827"/><ellipse cx="49" cy="68" rx="19" ry="13" fill="#f9a8d4"/><path d="M50 68H70 M75 62L92 37 M75 74L94 99" stroke="#111827"/><g text-anchor="middle" font-size="16"><text x="47" y="73">O</text><text x="75" y="73">C</text><text x="96" y="38">O</text><text x="97" y="107">O</text></g><path d="M23 18Q5 70 23 126 M123 18Q141 70 123 126" fill="none" stroke="#111827"/><text x="142" y="23" font-size="18">2⁻</text></svg>'
visual('chem12-p23-delocalized-carbonate',delocalized,width=.35)
add('The positive ion attracts the delocalized electrons in the carbonate ion towards itself. The carbonate ion becomes polarized.',
    'مثبت آئن کاربونیٹ آئن کے غیر مقامی الیکٹرانوں کو اپنی طرف کھینچتا ہے، جس سے کاربونیٹ آئن قطبی بن جاتا ہے۔',
    'مثبت ایون په کاربونېټ ایون کې غیرموضعي الکترونونه ځان ته راکاږي او کاربونېټ ایون قطبي کېږي.')
def polarized(language):
    labels={'en':[['The delocalize','electrons are pulled','towards the positive ion'],['This end of the ion is on its','way to break away and','become carbon dioxide'],['This oxygen atom is well on the way to become an oxide ion']],
            'ur':[['غیر مقامی الیکٹران','مثبت آئن کی طرف','کھینچے جاتے ہیں'],['آئن کا یہ سرا الگ ہو کر','کاربن ڈائی آکسائیڈ','بننے والا ہے'],['یہ آکسیجن ایٹم آکسائیڈ آئن بننے کے راستے پر ہے']],
            'ps':[['غیرموضعي الکترونونه','د مثبت ایون پر لور','راکاږل کېږي'],['د ایون دا سر د جلا کېدو','او کاربن ډای اکسایډ','د جوړېدو په لاره کې دی'],['دا اکسیجن اټوم د اکسایډ ایون د جوړېدو په لاره کې دی']]}[language]
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 205" role="img" aria-label="carbonate polarization by positive ion">',
         '<circle cx="58" cy="110" r="15" fill="white" stroke="#111827"/><text x="58" y="116" text-anchor="middle" font-size="16">2+</text>',
         '<path d="M92 106C77 81 104 76 123 96C135 75 140 56 159 69C181 82 146 100 136 112C159 124 184 144 161 155C142 169 132 137 122 127C94 144 79 128 92 106Z" fill="white" stroke="#111827"/>',
         '<ellipse cx="105" cy="111" rx="23" ry="15" fill="#f472b6"/><path d="M106 111H131 M138 103L154 81 M138 120L155 145" stroke="#111827"/>',
         '<g text-anchor="middle" font-size="16"><text x="101" y="116">O</text><text x="133" y="117">C</text><text x="159" y="82">O</text><text x="162" y="151">O</text><text x="108" y="90">2⁻</text></g>',
         '<path d="M75 56L96 91 M91 86L96 91L97 84 M194 113H147 M154 109L147 113L154 117 M97 169L103 132 M98 137L103 132L106 140" stroke="#111827" fill="none"/>']
    for labelgroup,x,y,size in [(labels[0],73,16,11),(labels[1],205,104,10),(labels[2],220,190,11)]:
        for i,text in enumerate(labelgroup):
            out.append(f'<text x="{x}" y="{y+i*13}" font-size="{size}" text-anchor="{"middle" if x!=205 else "start"}">{html.escape(text)}</text>')
    out.append('</svg>');return ''.join(out)
visual('chem12-p23-polarized-carbonate',polarized('en'),polarized('ur'),polarized('ps'),.8)
add('Figure 13.2 Molecular structure of carbonate.','شکل 13.2 کاربونیٹ کی سالماتی ساخت۔','شکل 13.2 د کاربونېټ مالیکولي جوړښت.')
add('When it is heated, the carbon dioxide gets free, leaving a metal oxide. The amount of heat required depends on the polarization of the ion. If the positive ion has only one positive charge, the polarizing effect is reduced. This is why the Group – IA compounds are more thermally stable than those in Group – IIA.',
    'گرم کرنے پر کاربن ڈائی آکسائیڈ آزاد ہو جاتی ہے اور دھاتی آکسائیڈ باقی رہتا ہے۔ درکار حرارت کی مقدار آئن کی قطبیت پر منحصر ہے۔ اگر مثبت آئن پر صرف ایک مثبت بار ہو، تو قطبی بنانے کا اثر کم ہوتا ہے۔ اسی لیے گروپ IA کے مرکبات گروپ IIA کے مرکبات سے زیادہ حرارتی استحکام رکھتے ہیں۔',
    'په تودولو سره کاربن ډای اکسایډ ازادېږي او فلزي اکسایډ پاتې کېږي. د اړینې تودوخې مقدار د ایون په قطبي کېدو پورې اړه لري. که مثبت ایون یوازې یو مثبت چارج ولري، د قطبي کولو اغېز کمېږي. له همدې امله د IA ګروپ مرکبات د IIA ګروپ له مرکباتو ډېر حرارتي ثبات لري.')
record=section('13.11','13.2.5 Thermal decomposition and polarization','13.2.5 حرارتی تحلیل اور قطبیت','13.2.5 حرارتي تجزیه او قطبي کېدل',paras,layout,blocks,'22–23')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':15,'printedPages':[22,23]}]
if __name__=='__main__':save(15,[record],carry=[{'from':'13.11','to':'13.12','startsAt':'The smaller the positive ion'}])
