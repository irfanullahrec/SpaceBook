"""Chemistry PDF60, printed112–113. Build-only import; root saves in order."""
import html
from class12_chemistry_opening import pair,section,SOURCE


class Mechanism:
    def __init__(self, identity, width, height, title):
        self.identity=identity
        self.items=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title,quote=True)}"><rect width="100%" height="100%" fill="white"/>']
    def text(self,x,y,s,size=23):
        self.items.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-family="Arial, sans-serif" fill="#111827">{html.escape(s)}</text>')
    def dot(self,x,y):
        self.items.append(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#111827"/>')
    def pair(self,x,y,vertical=False):
        for k in [-3.5,3.5]:self.dot(x if vertical else x+k,y+k if vertical else y)
    def cl(self,x,y,lone_sides=('left','top','bottom'),radical=None):
        self.text(x,y+7,'Cl')
        for side in lone_sides:
            if side=='left':self.pair(x-20,y,True)
            elif side=='right':self.pair(x+20,y,True)
            elif side=='top':self.pair(x,y-18)
            elif side=='bottom':self.pair(x,y+19)
        if radical=='right':self.dot(x+21,y)
        elif radical=='left':self.dot(x-21,y)
    def arrow(self,x1,y,x2):
        self.items.append(f'<path d="M{x1},{y} H{x2} m-9,-5 l9,5 -9,5" fill="none" stroke="#9f1239" stroke-width="1.8"/>')
    def hook(self,d,barb,color='#475569'):
        # Single barbs indicate the motion of one electron, as in the source.
        self.items.append(f'<path d="{d} {barb}" fill="none" stroke="{color}" stroke-width="1.8"/>')
    def done(self):return ''.join(self.items)+'</svg>'


L={
 'en': {'uv':'U.V. light','chlorine atom':'chlorine atom','methane':'methane','hydrogen chloride':'hydrogen chloride','methyl radical':'methyl radical','chlorine molecule':'chlorine molecule','chloromethane':'chloromethane'},
 'ur': {'uv':'بالائے بنفشی روشنی','chlorine atom':'کلورین ایٹم','methane':'میتھین','hydrogen chloride':'ہائیڈروجن کلورائیڈ','methyl radical':'میتھائل ریڈیکل','chlorine molecule':'کلورین سالمہ','chloromethane':'کلورومیتھین'},
 'ps': {'uv':'ماورای بنفش رڼا','chlorine atom':'د کلورین اټوم','methane':'میتان','hydrogen chloride':'هایدروجن کلوراید','methyl radical':'میتایل رادیکال','chlorine molecule':'د کلورین مالیکول','chloromethane':'کلورومیتان'}
}

def initiation(lang):
    d=Mechanism('initiation',650,155,'Initiation: homolytic cleavage of chlorine with single-electron arrows')
    d.cl(115,82);d.cl(215,82,('right','top','bottom'));d.pair(165,82,True)
    d.hook('M165,78 C165,20 211,20 215,52','M215,52 L208,44','#65a30d')
    d.hook('M165,86 C165,142 119,142 115,112','M115,112 L121,122')
    d.text(328,59,L[lang]['uv'],17);d.arrow(276,83,380)
    d.text(452,90,'2 [');d.cl(491,82,radical='right');d.text(532,90,']')
    return d.done()

def propagation_a(lang):
    l=L[lang];d=Mechanism('propagation-a',1050,190,'Propagation: chlorine radical abstracts hydrogen from methane')
    d.cl(75,102,radical='right');d.text(155,110,'+')
    d.text(225,110,'H');d.pair(258,102,True);d.text(297,110,'CH₃')
    d.hook('M99,93 Q140,21 187,45','M187,45 L176,47','#65a30d')
    d.hook('M258,98 Q227,29 190,45','M190,45 L197,53')
    d.hook('M258,108 C258,161 284,150 281,128','M281,128 L274,137')
    d.arrow(385,102,495)
    d.cl(573,102);d.pair(601,102,True);d.text(629,110,'H')
    d.text(761,110,'+');d.dot(884,94);d.text(915,110,'CH₃')
    for x,key in [(75,'chlorine atom'),(260,'methane'),(600,'hydrogen chloride'),(915,'methyl radical')]:d.text(x,174,l[key],17)
    return d.done()

def propagation_b(lang):
    l=L[lang];d=Mechanism('propagation-b',1050,190,'Propagation: methyl radical reacts with chlorine molecule')
    d.cl(70,102);d.cl(170,102,('right','top','bottom'));d.pair(120,102,True)
    d.text(266,110,'+');d.dot(335,102);d.text(369,110,'CH₃')
    d.hook('M120,98 Q205,12 290,43','M290,43 L278,46','#65a30d')
    d.hook('M335,98 Q335,25 296,44','M296,44 L305,48')
    d.hook('M120,108 C119,159 77,151 70,132','M70,132 L69,143')
    d.arrow(445,102,550)
    d.cl(630,102,radical='right');d.text(740,110,'+')
    d.cl(869,102);d.pair(897,102,True);d.text(936,110,'CH₃')
    for x,key in [(120,'chlorine molecule'),(370,'methyl radical'),(630,'chlorine atom'),(910,'chloromethane')]:d.text(x,174,l[key],17)
    return d.done()


paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def equation(e,u=None,p=None):add(e,u or e,p or e,'equation')
def visual(identity,fn):
    blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')})
    layout.append({'type':'visual','blockId':identity})

add('16.2.4 Relative Stability and Reactivity','16.2.4 نسبتی استحکام اور تعامل پذیری','16.2.4 نسبي ثبات او تعامل وړتیا','heading')
add('(a) Alkanes','(a) الکینز','(a) الکانونه','heading')
add('Alkanes are quite inert and unreactive towards most of the reagents under ordinary conditions. That is why they are also called paraffins. The word paraffin is derived from Latin words parum affinis (little affinity or little reactivity) and testifies to the low reactivity of alkanes. The little reactivity of alkanes is attributed to saturated nature and presence of non-polar C–C and C–H sigma bonds. Consequently polar reagents do not react with alkanes under normal conditions. Furthermore, the C–H and C–C bonds are strong bonds and hence alkanes are relatively stable to common reagents such as acids, alkalies, reducing and oxidizing agents etc. at ordinary conditions. However, they can react with several reagents, if the right conditions are used. The characteristic reactions of alkanes are free-radical substitution reactions.',
 'الکینز عام حالات میں زیادہ تر عاملوں کے لیے خاصے بے عمل اور غیر تعامل پذیر ہوتے ہیں۔ اسی لیے انہیں پیرافنز بھی کہا جاتا ہے۔ لفظ پیرافن لاطینی الفاظ parum affinis (کم میلان یا کم تعامل پذیری) سے نکلا ہے اور الکینز کی کم تعامل پذیری کی نشاندہی کرتا ہے۔ الکینز کی کم تعامل پذیری ان کی سیر شدہ نوعیت اور غیر قطبی C–C اور C–H سگما بندوں کی موجودگی سے منسوب ہے۔ نتیجتاً قطبی عامل عام حالات میں الکینز کے ساتھ تعامل نہیں کرتے۔ مزید یہ کہ C–H اور C–C مضبوط بند ہیں، اس لیے الکینز عام حالات میں تیزابوں، الکلیوں، تخفیفی اور تکسیدی عاملوں وغیرہ جیسے عام عاملوں کے مقابلے میں نسبتاً مستحکم ہوتے ہیں۔ تاہم درست حالات اختیار کیے جائیں تو یہ کئی عاملوں سے تعامل کر سکتے ہیں۔ الکینز کے مخصوص تعاملات آزاد ریڈیکل تبادلے کے تعاملات ہیں۔',
 'الکانونه په عادي شرایطو کې د ډېرو عاملونو پر وړاندې خورا غیر فعال او نه تعامل کوونکي دي. له همدې امله پیرافینونه هم بلل کېږي. د پیرافین کلمه له لاتیني parum affinis (لږ میلان یا لږ تعامل وړتیا) څخه اخیستل شوې او د الکانونو د کمې تعامل وړتیا څرګندونه کوي. د الکانونو کمه تعامل وړتیا د هغوی مشبوع طبیعت او د غیر قطبي C–C او C–H سیګما تړونونو شتون ته منسوبېږي. له همدې امله قطبي عاملونه په عادي شرایطو کې له الکانونو سره تعامل نه کوي. سربېره پر دې، C–H او C–C تړونونه پیاوړي دي، نو الکانونه په عادي شرایطو کې د اسیدونو، القلي‌ګانو، ارجاع کوونکو او اکسیدوونکو عاملونو او نورو عامو عاملونو پر وړاندې نسبتاً ثابت دي. خو د مناسبو شرایطو په کارولو سره له ګڼو عاملونو سره تعامل کولای شي. د الکانونو ځانګړي تعاملونه د ازادو رادیکالونو د بدلولو تعاملونه دي.')
add('(b) Cycloalkanes','(b) سائیکلوالکینز','(b) سایکلوالکانونه','heading')
add('Cycloalkanes resemble alkanes in their chemical behaviour except for cyclopropane and cyclobutane. The strength of bond and hence the stability, depends on the extent of overlap of orbitals. In the case of cyclopropane and cyclobutane, the extent of overlap of orbitals is not maximum due to greater angle strains and are unstable (Section 16.2.3.2). Cyclopropane undergoes ring opening reactions with several reagents to give open chain addition product. Cyclobutane, having less angle strain than that of cyclopropane, is more stable and hence it undergoes ring opening reaction only under severe conditions. For example, hydrogenation of cyclopropane and cyclobutane to corresponding open chain alkanes in the presence of nickel catalyst, occurs at 80°C and 200°C respectively. Higher members are even more stable and do not undergo ring opening reactions. Instead, they resemble open chain alkanes in reactivity and undergo only radical substitution reactions.',
 'سائیکلوپروپین اور سائیکلوبیوٹین کے سوا، سائیکلوالکینز اپنے کیمیائی رویے میں الکینز سے مشابہ ہیں۔ بند کی مضبوطی اور اس کے نتیجے میں استحکام، آربیٹلوں کے تداخل کی مقدار پر منحصر ہے۔ سائیکلوپروپین اور سائیکلوبیوٹین میں زیادہ زاویائی تناؤ کی وجہ سے آربیٹلوں کا تداخل زیادہ سے زیادہ نہیں ہوتا اور یہ غیر مستحکم ہوتے ہیں (حصہ 16.2.3.2)۔ سائیکلوپروپین کئی عاملوں کے ساتھ حلقہ کھلنے کے تعاملات سے کھلی زنجیر والی اضافی پیداوار دیتا ہے۔ سائیکلوبیوٹین میں سائیکلوپروپین کی نسبت زاویائی تناؤ کم ہوتا ہے، اس لیے یہ زیادہ مستحکم ہے اور صرف سخت حالات میں حلقہ کھلنے کا تعامل کرتا ہے۔ مثلاً نکل عمل انگیز کی موجودگی میں سائیکلوپروپین اور سائیکلوبیوٹین کی ہائیڈروجنیشن سے متعلقہ کھلی زنجیر والے الکینز بالترتیب 80°C اور 200°C پر بنتے ہیں۔ اعلیٰ ارکان مزید مستحکم ہوتے ہیں اور حلقہ کھلنے کے تعاملات نہیں کرتے۔ اس کے بجائے وہ تعامل پذیری میں کھلی زنجیر والے الکینز سے مشابہ ہوتے ہیں اور صرف ریڈیکل تبادلے کے تعاملات کرتے ہیں۔',
 'سایکلوالکانونه له سایکلوپروپان او سایکلوبیوتان پرته، په کیمیاوي چلند کې له الکانونو سره ورته دي. د تړون پیاوړتیا او له دې امله ثبات د اوربیټالونو د یو پر بل پوښښ په کچې پورې تړاو لري. په سایکلوپروپان او سایکلوبیوتان کې د زیات زاویوي فشار له امله د اوربیټالونو یو پر بل پوښښ تر ټولو زیات نه وي او دا بې‌ثباته دي (برخه 16.2.3.2). سایکلوپروپان له ګڼو عاملونو سره د کړۍ پرانیستلو تعاملونه کوي او د پرانیستي ځنځیر د اضافې محصول ورکوي. سایکلوبیوتان د سایکلوپروپان په پرتله لږ زاویوي فشار لري، نو ډېر ثابت دی او یوازې په سختو شرایطو کې د کړۍ پرانیستلو تعامل کوي. د بېلګې په توګه، د نکل کتلست په شتون کې د سایکلوپروپان او سایکلوبیوتان هایدروجنېشن اړوندو پرانیستو ځنځیري الکانونو ته په ترتیب په 80°C او 200°C کې کېږي. لوړ غړي لا ډېر ثابت دي او د کړۍ پرانیستلو تعاملونه نه کوي. پر ځای یې په تعامل وړتیا کې پرانیستو ځنځیري الکانونو ته ورته دي او یوازې د رادیکال بدلولو تعاملونه کوي.')
add('16.3 Radical Substitution Reactions','16.3 ریڈیکل تبادلے کے تعاملات','16.3 د رادیکال بدلولو تعاملونه','heading')
add('16.3.1 Overview','16.3.1 عمومی جائزہ','16.3.1 عمومي کتنه','heading')
add('Substitution reactions are those reactions in which an atom or group of atoms, attached to the carbon in a molecule is replaced by another atom or group of atoms. A substitution reaction may be initiated by free radical, nucleophile or electrophile. Substitution reactions which involve free radical intermediates are called radical substitution reactions. One of the examples of free radical substitution reaction is the chlorination of methane in the presence of ultraviolet light, shown below.',
 'تبادلے کے تعاملات وہ ہیں جن میں کسی سالمے کے کاربن سے جڑے ایٹم یا ایٹموں کے گروپ کی جگہ دوسرا ایٹم یا ایٹموں کا گروپ آ جاتا ہے۔ تبادلے کا تعامل آزاد ریڈیکل، نیوکلیوفائل یا الیکٹروفائل سے شروع ہو سکتا ہے۔ جن تبادلے کے تعاملات میں درمیانی آزاد ریڈیکل شامل ہوں انہیں ریڈیکل تبادلے کے تعاملات کہتے ہیں۔ آزاد ریڈیکل تبادلے کے تعامل کی ایک مثال بالائے بنفشی روشنی میں میتھین کی کلورینیشن ہے، جو نیچے دکھائی گئی ہے۔',
 'د بدلولو تعاملونه هغه تعاملونه دي چې په یوه مالیکول کې له کاربن سره د نښتي اټوم یا اټومونو د ګروپ پر ځای بل اټوم یا د اټومونو ګروپ راشي. د بدلولو تعامل د ازاد رادیکال، نیوکلیوفایل یا الکتروفایل له خوا پیلېدای شي. هغه د بدلولو تعاملونه چې منځګړي ازاد رادیکالونه پکې شامل وي، د رادیکال بدلولو تعاملونه بلل کېږي. د ازاد رادیکال بدلولو د تعامل یوه بېلګه د ماورای بنفش رڼا په شتون کې د میتان کلورینېشن دی چې لاندې ښودل شوی دی.')
equation('CH₄ (methane) + Cl₂ —U.V. light→ CH₃Cl (methyl chloride) + HCl',
 'CH₄ (میتھین) + Cl₂ —بالائے بنفشی روشنی→ CH₃Cl (میتھائل کلورائیڈ) + HCl',
 'CH₄ (میتان) + Cl₂ —ماورای بنفش رڼا→ CH₃Cl (میتایل کلوراید) + HCl')
add('In above reaction, hydrogen atom of the methane molecule is replaced by a chlorine atom (a free radical).',
 'مندرجہ بالا تعامل میں میتھین کے سالمے کے ہائیڈروجن ایٹم کی جگہ کلورین ایٹم (ایک آزاد ریڈیکل) آ جاتا ہے۔',
 'په پورتني تعامل کې د میتان مالیکول د هایدروجن اټوم پر ځای د کلورین اټوم (یو ازاد رادیکال) راځي.')
add('16.3.2 Mechanism of Free Radical Substitution Reactions','16.3.2 آزاد ریڈیکل تبادلے کے تعاملات کا طریق کار','16.3.2 د ازادو رادیکالونو د بدلولو تعاملونو میکانیزم','heading')
add('We will discuss the mechanism of chlorination of methane to methyl chloride. The mechanism involve the following steps:',
 'ہم میتھین کی کلورینیشن سے میتھائل کلورائیڈ بننے کے طریق کار پر بحث کریں گے۔ اس طریق کار میں درج ذیل مراحل شامل ہیں:',
 'موږ به د میتان د کلورینېشن له لارې د میتایل کلوراید د جوړېدو پر میکانیزم بحث وکړو. په میکانیزم کې لاندې پړاوونه شامل دي:')
add('Step-1: Initiation: A chlorine molecule undergoes homolytic fission in the presence of ultraviolet light to give chlorine free radicals.',
 'مرحلہ 1: آغاز: بالائے بنفشی روشنی کی موجودگی میں کلورین کا سالمہ ہومولائٹک تقسیم سے کلورین کے آزاد ریڈیکل دیتا ہے۔',
 'لومړی پړاو: پیل: د ماورای بنفش رڼا په شتون کې د کلورین مالیکول هومولیتیک وېش کوي او د کلورین ازاد رادیکالونه ورکوي.')
equation('Cl₂ —U.V. light→ 2Cl•','Cl₂ —بالائے بنفشی روشنی→ 2Cl•','Cl₂ —ماورای بنفش رڼا→ 2Cl•')
visual('chem12-pdf60-initiation',initiation)
add('Step-2: Propagation: (a) A chlorine free radical attacks the methane molecule to give methyl free radical and HCl.',
 'مرحلہ 2: پھیلاؤ: (a) کلورین کا ایک آزاد ریڈیکل میتھین کے سالمے پر حملہ کر کے میتھائل آزاد ریڈیکل اور HCl دیتا ہے۔',
 'دویم پړاو: خپرېدل: (a) د کلورین یو ازاد رادیکال د میتان پر مالیکول برید کوي او میتایل ازاد رادیکال او HCl ورکوي.')
equation('Cl• + H–CH₃ → HCl + •CH₃')
visual('chem12-pdf60-propagation-a',propagation_a)
add('(b) The methyl free radical, thus produced attacks a chlorine molecule to form methyl chloride and chlorine free radical.',
 '(b) اس طرح پیدا ہونے والا میتھائل آزاد ریڈیکل کلورین کے سالمے پر حملہ کر کے میتھائل کلورائیڈ اور کلورین آزاد ریڈیکل بناتا ہے۔',
 '(b) په دې ډول جوړ شوی میتایل ازاد رادیکال د کلورین پر مالیکول برید کوي او میتایل کلوراید او د کلورین ازاد رادیکال جوړوي.')
equation('Cl₂ + •CH₃ → Cl• + CH₃Cl')
visual('chem12-pdf60-propagation-b',propagation_b)
add('These propagation steps are repeated again and again.',
 'پھیلاؤ کے یہ مراحل بار بار دہرائے جاتے ہیں۔',
 'د خپرېدو دا پړاوونه بیا بیا تکرارېږي.')
add('Step-3: Termination: The above chain reaction comes to an end, when any two free radicals combine to form stable products.',
 'مرحلہ 3: اختتام: جب کوئی دو آزاد ریڈیکل مل کر مستحکم پیداوار بناتے ہیں تو مذکورہ زنجیری تعامل ختم ہو جاتا ہے۔',
 'درېیم پړاو: پای: پورتنی ځنځیري تعامل هغه وخت پای ته رسېږي چې هر دوه ازاد رادیکالونه سره یوځای شي او ثابت محصولات جوړ کړي.')
equation('Cl• + Cl• → Cl–Cl')
equation('•CH₃ + Cl• → CH₃–Cl')
equation('•CH₃ + •CH₃ → CH₃–CH₃')
add('In actual practice the above reaction does not stop at methyl chloride stage. The remaining three hydrogen atoms of methyl chloride can be successively replaced by chlorine atoms.',
 'عملی طور پر مذکورہ تعامل میتھائل کلورائیڈ کے مرحلے پر نہیں رکتا۔ میتھائل کلورائیڈ کے باقی تین ہائیڈروجن ایٹموں کی جگہ یکے بعد دیگرے کلورین ایٹم آ سکتے ہیں۔',
 'په عملي توګه پورتنی تعامل د میتایل کلوراید په پړاو کې نه درېږي. د میتایل کلوراید پاتې درې هایدروجن اټومونه په پرله‌پسې ډول د کلورین په اټومونو بدلېدای شي.')
equation('CH₃–Cl + Cl₂ → CH₂Cl₂ + HCl')
add('methylene chloride (dichloromethane)','میتھیلین کلورائیڈ (ڈائی کلورومیتھین)','میتیلین کلوراید (ډای کلورومیتان)')

record=section('16.7','Relative stability and radical substitution','نسبتی استحکام اور ریڈیکل تبادلہ','نسبي ثبات او د رادیکال بدلول',paras,layout,blocks,'112–113')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':60,'printedPages':[112,113]}]
record['sourceContinuesOnPdfPage']=61
carry=[{'from':'16.7','to':'16.8','startsAt':'CH2 Cl2+ Cl2'}]
issues=[{'id':'chem12-p112-cycloalkane-generality','printedPage':112,'description':'The source states that higher cycloalkanes do not undergo ring-opening reactions and undergo only radical substitution reactions. This textbook generalization is retained verbatim; it has not been broadened or scientifically rewritten.'}]

if __name__=='__main__':
    from class12_chemistry_sync import save
    save(60,[record],carry=carry,issues=issues,chapter_number=16)
