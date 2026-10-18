"""Repair PDF 6 (printed 4–5), preserving the source continuation on PDF 7."""
from class12_chemistry_opening import pair, section, ROOT, OUT, SOURCE
import json, os, html
from datetime import datetime, timezone

paras=[]; layout=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]}); paras.append(pair(en,ur,ps))
def heading(en,ur,ps): add(en,ur,ps,'heading')

heading('1. Covalent Radius','1. اشتراکی رداس','1. کووالنټ شعاع')
add('It is defined as “one-half of the distance between the nuclei of two identical atoms bonded together by a single covalent bond.” X-ray diffraction or spectroscopic measurements are used to determine the distance between the nuclei of any two bonded atoms. For example, the inter-nuclear distance in Cl₂ molecule is 198 pm. This means covalent radius of Cl atom is 99 pm.',
    'اس کی تعریف ہے: ”ایک واحد اشتراکی بند سے جڑے ہوئے دو یکساں ایٹموں کے مرکزوں کے درمیان فاصلے کا نصف۔“ بند سے جڑے کسی بھی دو ایٹموں کے مرکزوں کے درمیان فاصلہ معلوم کرنے کے لیے ایکس رے انعراج یا طیف بینی کی پیمائشیں استعمال کی جاتی ہیں۔ مثلاً Cl₂ سالمے میں مرکزوں کے درمیان فاصلہ 198 pm ہے۔ اس کا مطلب ہے کہ Cl ایٹم کا اشتراکی رداس 99 pm ہے۔',
    'دا داسې تعریفېږي: «د یوه واحد کووالنټ تړون په وسیله د دوو یو شان تړلو اټومونو د هستو ترمنځ د واټن نیمایي.» د هر ډول دوو تړلو اټومونو د هستو ترمنځ د واټن معلومولو لپاره د ایکس وړانګو انعراج یا طیف کتنې اندازه ګیرۍ کارول کېږي. د بېلګې په توګه، په Cl₂ مالیکول کې د هستو ترمنځ واټن 198 pm دی. دا مانا لري چې د Cl اټوم کووالنټ شعاع 99 pm ده.')
heading('2. Van der Waal’s Radius','2. وان ڈر والز رداس','2. د وان در والس شعاع')
add('It is defined as “one-half of the distance between the nuclei of two non-bonded and identical neighbouring atoms of two adjacent molecules in the solid state.” Since this radius corresponds to Van der Waal’s forces of attraction between the molecules, its magnitude is always greater than that of covalent radius; e.g. Van der Waal’s radius of hydrogen atom is 120 pm while its covalent radius is 37 pm.',
    'اس کی تعریف ہے: ”ٹھوس حالت میں دو ملحقہ سالموں کے دو غیر بند یافتہ، یکساں اور پڑوسی ایٹموں کے مرکزوں کے درمیان فاصلے کا نصف۔“ چونکہ یہ رداس سالموں کے درمیان وان ڈر والز کششی قوتوں سے متعلق ہے، اس لیے اس کی مقدار ہمیشہ اشتراکی رداس سے زیادہ ہوتی ہے؛ مثلاً ہائیڈروجن ایٹم کا وان ڈر والز رداس 120 pm، جبکہ اس کا اشتراکی رداس 37 pm ہے۔',
    'دا داسې تعریفېږي: «په جامد حالت کې د دوو څنګ په څنګ مالیکولونو د دوو ناتړلو، یو شان او ګاونډیو اټومونو د هستو ترمنځ د واټن نیمایي.» دا شعاع د مالیکولونو ترمنځ د وان در والس کششي قوې سره تړاو لري، نو اندازه یې تل له کووالنټ شعاع څخه لویه وي؛ د بېلګې په توګه، د هایدروجن اټوم د وان در والس شعاع 120 pm ده، خو کووالنټ شعاع یې 37 pm ده.')
heading('3. Metallic Radius','3. دھاتی رداس','3. فلزي شعاع')
add('This term is used for radius of metallic atoms e.g. Na, Mg, and Al. It is half of the total distance between nuclei of two adjacent atoms in the metallic cluster. The metallic radii are smaller than Van der Waal’s radii because metallic bonds are stronger than the Van der Waal’s forces.',
    'یہ اصطلاح دھاتی ایٹموں، مثلاً Na، Mg اور Al، کے رداس کے لیے استعمال ہوتی ہے۔ یہ دھاتی مجموعے میں دو ملحقہ ایٹموں کے مرکزوں کے درمیان کل فاصلے کا نصف ہے۔ دھاتی رداس وان ڈر والز رداس سے چھوٹے ہوتے ہیں، کیونکہ دھاتی بند وان ڈر والز قوتوں سے زیادہ مضبوط ہوتے ہیں۔',
    'دا اصطلاح د فلزي اټومونو، لکه Na، Mg او Al، د شعاع لپاره کارول کېږي. دا په فلزي مجموعه کې د دوو ګاونډیو اټومونو د هستو ترمنځ د ټول واټن نیمایي ده. فلزي شعاعوې د وان در والس له شعاعوو کوچنۍ دي، ځکه فلزي تړونونه د وان در والس له قوو پیاوړي دي.')
heading('Periodic Trends','دوری رجحانات','دوراني تمایلات')
add('In general, atomic radii shows an increase in magnitude on moving from top to bottom in any group and decrease in magnitude on moving from left to right in any given period.',
    'عموماً کسی گروپ میں اوپر سے نیچے جانے پر ایٹمی رداس کی مقدار بڑھتی ہے اور کسی دور میں بائیں سے دائیں جانے پر کم ہوتی ہے۔',
    'په عمومي ډول، په هر ګروپ کې له پاس څخه ښکته تګ سره اټومي شعاعوې لویېږي، او په هره دوره کې له کیڼ څخه ښي لوري ته تګ سره کوچنۍ کېږي.')
heading('(a) Variation in a Group','(a) گروپ میں تبدیلی','(a) په یوه ګروپ کې بدلون')
add('As we move in a group from top to bottom, the number of shells and the effective nuclear charge increases but the effect of addition of new shell dominates over the effect of effective nuclear charge and hence the atomic size increases from top to bottom in a group. For example, see Table 13.2',
    'کسی گروپ میں اوپر سے نیچے جانے پر خولوں کی تعداد اور مؤثر مرکزی بار بڑھتا ہے، مگر نئے خول کے اضافے کا اثر مؤثر مرکزی بار کے اثر پر غالب ہوتا ہے۔ اس لیے گروپ میں اوپر سے نیچے ایٹمی جسامت بڑھتی ہے۔ مثال کے لیے جدول 13.2 دیکھیں۔',
    'په یوه ګروپ کې له پاس څخه ښکته تګ سره د پوښونو شمېر او اغېزمن هستوي چارج زیاتېږي، خو د نوي پوښ د زیاتېدو اغېز د اغېزمن هستوي چارج پر اغېز غالب وي؛ نو په ګروپ کې له پاس څخه ښکته اټومي اندازه زیاتېږي. د بېلګې لپاره جدول 13.2 وګورئ.')
add('Table 13.2 Trend in Atomic Radius of group IA','جدول 13.2 گروپ IA میں ایٹمی رداس کا رجحان','جدول 13.2 په IA ګروپ کې د اټومي شعاع تمایل')
t2={'id':'chem12-table-13-2','headers':['Elements of Group IA','Li','Na','K','Rb','Cs'],
    'rows':[['Outer-shell electronic configuration','[He]2s¹','[Ne]3s¹','[Ar]4s¹','[Kr]5s¹','[Xe]6s¹'],['Atomic radius (pm)','152','186','227','248','265']],
    'translations':[{'language':'اردو','headers':['گروپ IA کے عناصر','Li','Na','K','Rb','Cs'],'rows':[['بیرونی خول کی الیکٹرانی ترتیب','[He]2s¹','[Ne]3s¹','[Ar]4s¹','[Kr]5s¹','[Xe]6s¹'],['ایٹمی رداس (pm)','152','186','227','248','265']]},
                    {'language':'پښتو','headers':['د IA ګروپ عناصر','Li','Na','K','Rb','Cs'],'rows':[['د بهرني پوښ الکتروني ترتیب','[He]2s¹','[Ne]3s¹','[Ar]4s¹','[Kr]5s¹','[Xe]6s¹'],['اټومي شعاع (pm)','152','186','227','248','265']]}]}
layout.append({'type':'sourceDataTable','tableId':t2['id']})
heading('(b) Variation in a Period','(b) دور میں تبدیلی','(b) په یوه دوره کې بدلون')
add('As we move in a period from left to right, the number of shells remains the same as the electrons are added in the same shell. However, the effective nuclear charge increases and pulls the electron cloud closer to the nucleus. As a result, the atomic size decreases from sodium (Na) to chlorine (Cl) in period third.',
    'کسی دور میں بائیں سے دائیں جانے پر خولوں کی تعداد یکساں رہتی ہے، کیونکہ الیکٹران اسی خول میں شامل ہوتے ہیں۔ تاہم مؤثر مرکزی بار بڑھتا ہے اور الیکٹرانی بادل کو مرکزے کے قریب کھینچتا ہے۔ نتیجتاً تیسرے دور میں سوڈیم (Na) سے کلورین (Cl) تک ایٹمی جسامت کم ہوتی ہے۔',
    'په یوه دوره کې له کیڼ څخه ښي لوري ته تګ سره د پوښونو شمېر یو شان پاتې کېږي، ځکه الکترونونه په هماغه پوښ کې زیاتېږي. خو اغېزمن هستوي چارج زیاتېږي او الکتروني ورېځ هستې ته نږدې راکاږي. په پایله کې په درېیمه دوره کې له سوډیم (Na) څخه تر کلورین (Cl) پورې اټومي اندازه کمېږي.')
add('The atomic size of noble gas (Argon) is greater than the prior elements in the respective period (3rd period). This is due to the reason that in noble gases, Van der Waal’s radius is determined, whose magnitude is larger than the covalent radius.',
    'نجیب گیس (آرگن) کی ایٹمی جسامت متعلقہ دور (تیسرے دور) کے اس سے پہلے آنے والے عناصر سے زیادہ ہے۔ اس کی وجہ یہ ہے کہ نجیب گیسوں میں وان ڈر والز رداس معلوم کیا جاتا ہے، جس کی مقدار اشتراکی رداس سے زیادہ ہوتی ہے۔',
    'د نجیب ګاز (ارګون) اټومي اندازه په اړونده دوره (درېیمه دوره) کې تر مخکینیو عناصرو لویه ده. لامل یې دا دی چې په نجیبو ګازونو کې د وان در والس شعاع ټاکل کېږي، چې اندازه یې له کووالنټ شعاع څخه لویه ده.')
add('Table 13.3 Trend in Atomic Radius of 3ʳᵈ Period Elements Na to Ar.','جدول 13.3 تیسرے دور کے عناصر Na سے Ar تک کے ایٹمی رداس کا رجحان۔','جدول 13.3 له Na څخه تر Ar پورې د درېیمې دورې د عناصرو د اټومي شعاع تمایل.')
symbols=['₁₁Na','₁₂Mg','₁₃Al','₁₄Si','₁₅P','₁₆S','₁₇Cl','₁₈Ar']
radii=['186','160','143','118','114','104','99','188']
t3={'id':'chem12-table-13-3','headers':['Symbol with atomic number']+symbols,'rows':[['Atomic radius (pm)']+radii],
    'translations':[{'language':'اردو','headers':['ایٹمی نمبر کے ساتھ علامت']+symbols,'rows':[['ایٹمی رداس (pm)']+radii]},
                    {'language':'پښتو','headers':['له اټومي شمېر سره سمبول']+symbols,'rows':[['اټومي شعاع (pm)']+radii]}]}
layout.append({'type':'sourceDataTable','tableId':t3['id']})
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 630 85" role="img" aria-label="Na to Ar atomic radius">'
for i,(name,r) in enumerate(zip(['Na','Mg','Al','Si','P','S','Cl','Ar'],radii)):
    radius=int(r)*.16; x=40+i*78
    svg+=f'<circle cx="{x}" cy="40" r="{radius}" fill="#6ee7b7" stroke="#0f172a"/><text x="{x}" y="45" text-anchor="middle" font-size="16">{name}</text>'
svg+='</svg>'
fig={'id':'chem12-figure-13-1-radii','svg':svg,'svgUrdu':svg.replace('Na to Ar atomic radius','Na سے Ar تک ایٹمی رداس'),'svgPashto':svg.replace('Na to Ar atomic radius','له Na څخه تر Ar پورې اټومي شعاع')}
layout.append({'type':'visual','blockId':fig['id']})
add('Figure 13.1 Atomic radius changes across third period elements.','شکل 13.1 تیسرے دور کے عناصر میں ایٹمی رداس کی تبدیلیاں۔','شکل 13.1 د درېیمې دورې په عناصرو کې د اټومي شعاع بدلونونه.')
heading('13.1.1.3 Trend in First Ionization Energy','13.1.1.3 پہلی آئنائزیشن توانائی کا رجحان','13.1.1.3 د لومړۍ ایون کېدو انرژۍ تمایل')
heading('Ionization Energy (IE)','آئنائزیشن توانائی (IE)','د ایون کېدو انرژي (IE)')
add('Ionization energy of an element is the minimum amount of energy (in kJ/mol) required to remove the outermost electron of an isolated gaseous atom to form an ion, the result is the formation of the gaseous cation, i.e.',
    'کسی عنصر کی آئنائزیشن توانائی، توانائی کی وہ کم سے کم مقدار (kJ/mol میں) ہے جو ایک الگ تھلگ گیس ایٹم کا سب سے بیرونی الیکٹران نکال کر آئن بنانے کے لیے درکار ہوتی ہے۔ اس کے نتیجے میں گیس حالت کا مثبت آئن بنتا ہے، یعنی:',
    'د یوه عنصر د ایون کېدو انرژي د انرژۍ هغه لږ تر لږه مقدار (په kJ/mol) دی چې د یوه جلا ګازي اټوم د تر ټولو بهرني الکترون د ایستلو او ایون جوړولو لپاره اړین وي. په پایله کې ګازي مثبت ایون جوړېږي، یعنې:')
add('Mg₍g₎ → Mg⁺₍g₎ + e⁻     ΔH = 737 kJ.mol⁻¹','Mg₍g₎ → Mg⁺₍g₎ + e⁻     ΔH = 737 kJ.mol⁻¹','Mg₍g₎ → Mg⁺₍g₎ + e⁻     ΔH = 737 kJ.mol⁻¹','equation')
add('Ionization energy for removal of first electron from the outermost shell of an atom is called 1ˢᵗ I.E. Similarly, the ionization energy for the removal of an electron from M⁺₍g₎ called 2ⁿᵈ I.E.',
    'کسی ایٹم کے سب سے بیرونی خول سے پہلا الیکٹران نکالنے کی آئنائزیشن توانائی پہلی I.E. کہلاتی ہے۔ اسی طرح M⁺₍g₎ سے ایک الیکٹران نکالنے کی آئنائزیشن توانائی دوسری I.E. کہلاتی ہے۔',
    'د یوه اټوم له تر ټولو بهرني پوښ څخه د لومړي الکترون د ایستلو د ایون کېدو انرژي لومړۍ I.E. بلل کېږي. په همدې ډول له M⁺₍g₎ څخه د یوه الکترون د ایستلو د ایون کېدو انرژي دویمه I.E. بلل کېږي.')
add('Mg⁺₍g₎ → Mg²⁺₍g₎ + e⁻     ΔH = 1476 kJ.mol⁻¹','Mg⁺₍g₎ → Mg²⁺₍g₎ + e⁻     ΔH = 1476 kJ.mol⁻¹','Mg⁺₍g₎ → Mg²⁺₍g₎ + e⁻     ΔH = 1476 kJ.mol⁻¹','equation')
heading('Periodic Trends','دوری رجحانات','دوراني تمایلات')
add('In general, the ionization energy decreases in moving from top to bottom in a group and increases from left to right in a period.',
    'عموماً کسی گروپ میں اوپر سے نیچے جانے پر آئنائزیشن توانائی کم ہوتی ہے اور کسی دور میں بائیں سے دائیں جانے پر بڑھتی ہے۔',
    'په عمومي ډول، په یوه ګروپ کې له پاس څخه ښکته تګ سره د ایون کېدو انرژي کمېږي او په یوه دوره کې له کیڼ څخه ښي لوري ته تګ سره زیاتېږي.')
heading('(a) Variation in a Group','(a) گروپ میں تبدیلی','(a) په یوه ګروپ کې بدلون')
add('As we move in a group from top to bottom, there is an increase in the atomic size, nuclear charge and shielding effect. However, the combined effect of increase in atomic size and shielding effect dominates over the effect of increase in the nuclear charge. Hence, ionization energy decreases from top to bottom in a group with some exceptions.',
    'کسی گروپ میں اوپر سے نیچے جانے پر ایٹمی جسامت، مرکزی بار اور حائلی اثر بڑھتے ہیں۔ تاہم ایٹمی جسامت اور حائلی اثر میں اضافے کا مشترکہ اثر مرکزی بار میں اضافے کے اثر پر غالب ہوتا ہے۔ اس لیے بعض استثناؤں کے ساتھ گروپ میں اوپر سے نیچے آئنائزیشن توانائی کم ہوتی ہے۔',
    'په یوه ګروپ کې له پاس څخه ښکته تګ سره اټومي اندازه، هستوي چارج او د پردې اغېز زیاتېږي. خو د اټومي اندازې او د پردې اغېز د زیاتېدو ګډ اغېز د هستوي چارج د زیاتېدو پر اغېز غالب وي. له همدې امله، له ځینو استثناوو سره، په ګروپ کې له پاس څخه ښکته د ایون کېدو انرژي کمېږي.')
heading('Variation in a Period','دور میں تبدیلی','په یوه دوره کې بدلون')
add('As we move in a period from left to right, the number of shells remain the same but atomic size decreases as the electrons are added in the same shell, hence pulling the electrons closer towards the nucleus.',
    'کسی دور میں بائیں سے دائیں جانے پر خولوں کی تعداد یکساں رہتی ہے، مگر اسی خول میں الیکٹرانوں کے اضافے سے ایٹمی جسامت کم ہوتی ہے؛ یوں الیکٹران مرکزے کے مزید قریب کھنچتے ہیں۔',
    'په یوه دوره کې له کیڼ څخه ښي لوري ته تګ سره د پوښونو شمېر یو شان پاتې کېږي، خو په هماغه پوښ کې د الکترونونو د زیاتېدو له امله اټومي اندازه کمېږي، نو الکترونونه هستې ته لا نږدې راکاږل کېږي.')

record=section('13.2','Atomic radius and first ionization energy','ایٹمی رداس اور پہلی آئنائزیشن توانائی','اټومي شعاع او د لومړۍ ایون کېدو انرژي',paras,layout,[t2,t3,fig],'4–5')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':6,'printedPages':[4,5]}]
record['sourceIssues']=[{'id':'chem12-repeated-figure-13-1','description':'The printed figure number 13.1 is reused for the atomic-radius circles. Preserve both printed captions; stable coded IDs distinguish them.'}]

def main():
    marker='// BEGIN CLASS12 CHEMISTRY PDF6 SOURCE REPAIR'; end='// END CLASS12 CHEMISTRY PDF6 SOURCE REPAIR'
    block=marker+'\n{ const replacement = '+json.dumps(record,ensure_ascii=False,indent=2)+''';
const chapter=CHEM_12_DATA.find(item=>item.number===13);
const index=chapter.sections.findIndex(item=>item.id===replacement.id);
if(index<0)throw new Error('Missing Chemistry XII radius section');
chapter.sections[index]=replacement;
const continuation=chapter.sections.find(item=>item.id==='13.3');
if(continuation&&!continuation.sourcePdf6BoundaryRepaired){
 const start=continuation.theory.indexOf('Thus, more energy is required');
 if(start<0)throw new Error('Missing Chemistry XII PDF7 continuation');
 continuation.theory=continuation.theory.slice(start);continuation.content=continuation.theory.replace(/\\n/g,'<br>');
 continuation.sciNote='';continuation.sourcePdf6BoundaryRepaired=true;
}
chapter.topics=chapter.sections.map(section=>({...((chapter.topics||[]).find(item=>item.id===section.id)||{}),...section}));
}
'''+end+'\n'
    lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    try:
        os.write(fd,f'class12-chemistry pid={os.getpid()}\n'.encode());os.close(fd);fd=None
        path=ROOT/'js/chem_12_data.js';text=path.read_text(encoding='utf-8')
        if marker in text:
            start=text.index(marker);stop=text.index(end,start)+len(end);text=text[:start]+block+text[stop:]
        else:text=text.rstrip()+'\n\n'+block
        temp=path.with_name(path.name+'.chem12.tmp');temp.write_text(text,encoding='utf-8');os.replace(temp,path)
    finally:
        if fd is not None:os.close(fd)
        lock.unlink()
    (OUT/'chemistry-pdf6-repair.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    path=OUT/'chemistry-progress.json';p=json.loads(path.read_text(encoding='utf-8'))
    for entry in p['pages']:
        if entry['pdfPage']==6:
            entry['status']='implemented_pending_final_comparison';entry['evidence']='Printed 4–5 repaired with aligned translations, Tables 13.2/13.3, proportional atomic-radius SVG and both complete magnesium ionization equations. Duplicate legacy fragments trimmed; final comparison pending.'
    p['lastSavedUtc']=datetime.now(timezone.utc).isoformat();p['nextSequentialImplementationPdfPage']=7
    path.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Chemistry PDF6 implementation saved; final source comparison pending.')
if __name__=='__main__':main()
