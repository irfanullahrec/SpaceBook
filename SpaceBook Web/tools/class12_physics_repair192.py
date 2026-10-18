"""PDF192: complete medical applications and three fundamental forces."""
from class12_source_review import upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
add('heading','B. MEDICAL USES','B. طبی استعمال','B. طبي استعمالونه')
add('paragraph','One of the most important applications of nuclear physics has been in medicine, for both diagnostic and therapeutic purposes.',
 'نیوکلیائی طبیعیات کے نہایت اہم استعمالات میں طب میں تشخیص اور علاج، دونوں مقاصد کے لیے اس کا استعمال شامل ہے۔',
 'د هستوي فزیک له تر ټولو مهمو استعمالونو څخه یو یې په طب کې د تشخیص او درملنې دواړو موخو لپاره کارول دي.')
add('heading','i. Medical diagnostics:','i. طبی تشخیص:','i. طبي تشخیص:')
add('paragraph',r'Radioactive isotopes are used in medical diagnosis as tracers. Radioactive isotopes are introduced in the body in chemical forms that have an affinity for certain organs, such as bone or the thyroid gland. For medical diagnosis, the radionuclide commonly used today is \({}^{99\mathrm{m}}\mathrm{Tc}\) long-lived excited state of technetium-99 (the “m” in the symbol stands for ‘metastable’ state).',
 r'طبی تشخیص میں تابکار آئسوٹوپس ٹریسر کے طور پر استعمال کیے جاتے ہیں۔ تابکار آئسوٹوپس ایسی کیمیائی صورتوں میں جسم کے اندر داخل کیے جاتے ہیں جو مخصوص اعضا، مثلاً ہڈی یا تھائیرائڈ غدود، سے رغبت رکھتی ہیں۔ طبی تشخیص کے لیے آج عام طور پر استعمال ہونے والا ریڈیونیوکلائیڈ \({}^{99\mathrm{m}}\mathrm{Tc}\) ہے، جو ٹیکنیٹیم-99 کی طویل عمر والی برانگیختہ حالت ہے (علامت میں “m” سے مراد نیم مستحکم حالت ہے)۔',
 r'راډیواکټیف ایزوټوپونه په طبي تشخیص کې د نښه کوونکو په توګه کارول کېږي. راډیواکټیف ایزوټوپونه په هغو کیمیاوي بڼو بدن ته داخلېږي چې له ځانګړو غړو، لکه هډوکو یا تایرایډ غدې، سره میلان لري. د طبي تشخیص لپاره نن په عام ډول کارېدونکی راډیونوکلایډ \({}^{99\mathrm{m}}\mathrm{Tc}\) دی، چې د ټکنېشیم-99 اوږد عمر لرونکی پارېدلی حالت دی (په نښه کې “m” د نیمه ثابت حالت استازیتوب کوي).')
add('paragraph','A sensitive detector (called a “gamma-ray camera”) can observe the radiations from the isotopes that are concentrated in the organ and can produce an image that shows how the activity is distributed in the patient. These detectors are capable of determining where each gamma-ray photon originates in the patient as shown in figure 20.24.',
 'ایک حساس سراغ رساں آلہ (جسے ”گاما رے کیمرا“ کہتے ہیں) عضو میں جمع ہونے والے آئسوٹوپس کی تابکاری کو دیکھ سکتا ہے اور ایسی تصویر بنا سکتا ہے جو دکھاتی ہے کہ مریض میں تابکار سرگرمی کس طرح تقسیم ہے۔ یہ آلات یہ تعین کر سکتے ہیں کہ مریض کے اندر ہر گاما شعاع کا فوٹون کہاں سے پیدا ہوتا ہے، جیسا کہ شکل 20.24 میں دکھایا گیا ہے۔',
 'یو حساس کشفوونکی (چې «د ګاما وړانګو کامره» بلل کېږي) په غړي کې راټول شوو ایزوټوپونو وړانګې لیدلی شي او داسې انځور جوړولی شي چې په ناروغ کې د فعالیت وېش وښيي. دا کشفوونکي معلومولی شي چې په ناروغ کې د ګاما وړانګې هر فوټون له کوم ځایه راپیدا کېږي، لکه په 20.24 شکل کې چې ښودل شوي دي.')
add('heading','FIGURE 20.24','شکل 20.24','شکل 20.24')
L.append({'type':'visual','blockId':'phys20-192-gamma-camera'})
add('paragraph','Gamma Camera','گاما کیمرا','ګاما کامره')
add('heading','For your information','آپ کی معلومات کے لیے','ستاسو د معلوماتو لپاره')
add('heading','POSITRON EMISSION TOMOGRAPHY (PET)','پوزیٹرون کے اخراج کی ٹوموگرافی (PET)','د پوزیترون د خپرېدو ټوموګرافي (PET)')
add('paragraph',r'Another technique that reveals information inside the body is positron emission tomography (PET), in which the patient is injected with a positron-emitting isotope that is readily absorbed by the body. Examples of isotopes used are \({}^{15}\mathrm{O}\) (\(t_{1/2}=2\ \mathrm{min}\)), \({}^{13}\mathrm{N}\) (\(t_{1/2}=10\ \mathrm{min}\)), \({}^{11}\mathrm{C}\) (\(t_{1/2}=20\ \mathrm{min}\)), and \({}^{18}\mathrm{F}\) (\(t_{1/2}=110\ \mathrm{min}\)). These isotopes are produced with a cyclotron. By surrounding the patient with a ring of detectors, it is possible to determine exactly where the decay occurred, and from a large number of such events, an image is produced that reconstructs the distribution of the radioisotope in the patient.',
 r'جسم کے اندر کی معلومات ظاہر کرنے والی ایک اور تکنیک پوزیٹرون کے اخراج کی ٹوموگرافی (PET) ہے۔ اس میں مریض کو پوزیٹرون خارج کرنے والے ایسے آئسوٹوپ کا انجکشن لگایا جاتا ہے جسے جسم آسانی سے جذب کر لیتا ہے۔ استعمال ہونے والے آئسوٹوپس کی مثالیں \({}^{15}\mathrm{O}\) (\(t_{1/2}=2\ \mathrm{min}\))، \({}^{13}\mathrm{N}\) (\(t_{1/2}=10\ \mathrm{min}\))، \({}^{11}\mathrm{C}\) (\(t_{1/2}=20\ \mathrm{min}\)) اور \({}^{18}\mathrm{F}\) (\(t_{1/2}=110\ \mathrm{min}\)) ہیں۔ یہ آئسوٹوپس سائیکلوٹرون سے پیدا کیے جاتے ہیں۔ مریض کے گرد سراغ رساں آلات کا حلقہ بنا کر یہ درست طور پر معلوم کیا جا سکتا ہے کہ زوال کہاں ہوا۔ ایسے بہت سے واقعات سے ایک تصویر بنائی جاتی ہے جو مریض میں تابکار آئسوٹوپ کی تقسیم دوبارہ تشکیل دیتی ہے۔',
 r'بله تخنیکي لاره چې د بدن دننه معلومات څرګندوي، د پوزیترون د خپرېدو ټوموګرافي (PET) ده. په دې کې ناروغ ته د داسې پوزیترون خپروونکي ایزوټوپ پېچکاري ورکول کېږي چې بدن یې په اسانۍ جذبوي. د کارېدونکو ایزوټوپونو بېلګې \({}^{15}\mathrm{O}\) (\(t_{1/2}=2\ \mathrm{min}\))، \({}^{13}\mathrm{N}\) (\(t_{1/2}=10\ \mathrm{min}\))، \({}^{11}\mathrm{C}\) (\(t_{1/2}=20\ \mathrm{min}\)) او \({}^{18}\mathrm{F}\) (\(t_{1/2}=110\ \mathrm{min}\)) دي. دا ایزوټوپونه په سایکلوټرون کې تولیدېږي. د ناروغ چاپېر د کشفوونکو په کړۍ سره په دقیق ډول معلومېدای شي چې زوال چېرې رامنځته شوی دی. له ډېرو داسې پېښو څخه یو انځور جوړېږي چې په ناروغ کې د راډیواکټیف ایزوټوپ وېش بیا رغوي.')
add('heading','ii. Radiation therapy:','ii. تابکاری سے علاج:','ii. د وړانګو درملنه:')
add('paragraph','Radiation therapy is the use of high-energy radiation to damage cancer cells’ DNA and destroy their ability to divide and grow.',
 'تابکاری سے علاج میں زیادہ توانائی والی تابکاری استعمال کر کے سرطان کے خلیوں کے DNA کو نقصان پہنچایا جاتا ہے اور ان کی تقسیم ہونے اور بڑھنے کی صلاحیت ختم کی جاتی ہے۔',
 'د وړانګو درملنه د لوړې انرژۍ وړانګو کارول دي، څو د سرطاني حجرو DNA زیانمن کړي او د وېش او ودې وړتیا یې له منځه یوسي.')
add('paragraph','The radioactive source such as cobalt 60 which emit beta particles and high energy gamma rays can also be used to treat various cancers as shown in figure 20.25.',
 'کوبالٹ 60 جیسے تابکار ذرائع، جو بیٹا ذرات اور زیادہ توانائی والی گاما شعاعیں خارج کرتے ہیں، مختلف سرطانوں کے علاج کے لیے بھی استعمال کیے جا سکتے ہیں، جیسا کہ شکل 20.25 میں دکھایا گیا ہے۔',
 'راډیواکټیف سرچینې، لکه کوبالټ 60 چې بېټا ذرې او د لوړې انرژۍ ګاما وړانګې خپروي، د بېلابېلو سرطانونو د درملنې لپاره هم کارېدلی شي، لکه په 20.25 شکل کې چې ښودل شوي دي.')
add('paragraph','Some radioisotopes are made to absorb by selected organ and radiation is concentrated on the infected tissue. For example cancerous thyroid can be treated with iodine-131.',
 'بعض تابکار آئسوٹوپس کو منتخب عضو میں جذب کرایا جاتا ہے اور تابکاری متاثرہ بافت پر مرکوز کی جاتی ہے۔ مثلاً سرطان زدہ تھائیرائڈ کا علاج آیوڈین-131 سے کیا جا سکتا ہے۔',
 'ځینې راډیواکټیف ایزوټوپونه داسې برابرېږي چې ټاکلی غړی یې جذب کړي او وړانګې په ناروغ نسج متمرکزې شي. د بېلګې په توګه، سرطاني تایرایډ په ایوډین-131 درمل کېدای شي.')
add('heading','FIGURE 20.25','شکل 20.25','شکل 20.25')
L.append({'type':'visual','blockId':'phys20-192-radiotherapy'})
add('heading','20.18 BASIC FORCES OF NATURE (Fundamental Interactions)','20.18 فطرت کی بنیادی قوتیں (بنیادی تعاملات)','20.18 د طبیعت بنسټیز ځواکونه (بنسټیز تعاملونه)')
add('paragraph','All particles in nature are subjected to four fundamental forces, strong force, weak force, electromagnetic force and gravitational force.',
 'فطرت کے تمام ذرات چار بنیادی قوتوں کے زیر اثر ہوتے ہیں: قوی قوت، کمزور قوت، برق مقناطیسی قوت اور کششِ ثقل کی قوت۔',
 'په طبیعت کې ټولې ذرې د څلورو بنسټیزو ځواکونو تر اغېز لاندې دي: قوي ځواک، کمزوری ځواک، برېښنا مقناطیسي ځواک او د جاذبې ځواک.')
add('heading','A. STRONG FORCE','A. قوی قوت','A. قوي ځواک')
add('paragraph',r'The strong force is very short range about \(10^{-14}\ \mathrm{m}\) and is responsible for binding of nucleons in the nucleus. It can be considered as an exchange force in which the exchange particles are gluon. It is the strongest of all the forces and have been assigned as relative strength 1.',
 r'قوی قوت کی رسائی بہت مختصر، تقریباً \(10^{-14}\ \mathrm{m}\)، ہوتی ہے اور یہ نیوکلئیس میں نیوکلیونوں کو باندھنے کی ذمہ دار ہے۔ اسے تبادلے کی قوت سمجھا جا سکتا ہے جس میں تبادلہ ہونے والے ذرات گلوآن ہیں۔ یہ تمام قوتوں سے زیادہ قوی ہے اور اس کی نسبتی شدت 1 مقرر کی گئی ہے۔',
 r'قوي ځواک ډېر لنډ واټن، شاوخوا \(10^{-14}\ \mathrm{m}\)، لري او په هسته کې د نوکلیونونو د تړلو مسؤول دی. دا د تبادلې ځواک ګڼل کېدای شي چې پکې تبادله کېدونکې ذرې ګلوونونه دي. دا تر ټولو پیاوړی ځواک دی او نسبي شدت یې 1 ټاکل شوی دی.')
add('heading','B. ELECTROMAGNETIC FORCE','B. برق مقناطیسی قوت','B. برېښنا مقناطیسي ځواک')
add('paragraph',r'Fundamentally, both magnetic and electric forces are manifestations of an exchange force involving the exchange of photons. The electromagnetic force holds atoms and molecules together. It has infinite range and relative strength is \(10^{-2}\).',
 r'بنیادی طور پر مقناطیسی اور برقی، دونوں قوتیں ایک تبادلے کی قوت کے مظاہر ہیں جس میں فوٹونوں کا تبادلہ ہوتا ہے۔ برق مقناطیسی قوت ایٹموں اور سالموں کو اکٹھا رکھتی ہے۔ اس کی رسائی لامحدود ہے اور نسبتی شدت \(10^{-2}\) ہے۔',
 r'په بنسټیز ډول مقناطیسي او برېښنايي دواړه ځواکونه د داسې تبادلې ځواک څرګندونې دي چې د فوټونونو تبادله پکې کېږي. برېښنا مقناطیسي ځواک اټومونه او مالیکولونه سره یوځای ساتي. واټن یې بې پایه دی او نسبي شدت یې \(10^{-2}\) دی.')
add('heading','C. WEAK FORCE','C. کمزور قوت','C. کمزوری ځواک')
add('paragraph',r'Weak interaction involves the exchange of the intermediate vector bosons, the W and the Z. The weak interaction changes one flavor of quark into another. It is very short range about 0.1% of diameter of proton i.e \(10^{-18}\ \mathrm{m}\). It have relative strength of about \(10^{-6}\).',
 r'کمزور تعامل میں واسطہ بردار سمتی بوزونوں، W اور Z، کا تبادلہ ہوتا ہے۔ کمزور تعامل کوارک کی ایک نوع کو دوسری میں بدل دیتا ہے۔ اس کی رسائی بہت مختصر، پروٹون کے قطر کا تقریباً 0.1%، یعنی \(10^{-18}\ \mathrm{m}\)، ہے۔ اس کی نسبتی شدت تقریباً \(10^{-6}\) ہے۔',
 r'په کمزوري تعامل کې منځګړي ویکټوري بوزونونه، W او Z، تبادله کېږي. کمزوری تعامل د کوارک یوه نوعه په بله بدلوي. واټن یې ډېر لنډ دی، د پروتون د قطر شاوخوا 0.1%، یعنې \(10^{-18}\ \mathrm{m}\). نسبي شدت یې شاوخوا \(10^{-6}\) دی.')

def patient(x,y):
    return f'<rect x="{x-130}" y="{y+25}" width="290" height="20" rx="6" fill="#cbd5e1" stroke="#64748b"/><path d="M{x-110} {y+22}Q{x-100} {y-20} {x-35} {y-11}L{x+90} {y+4}L{x+116} {y+24}Z" fill="#a78bfa" stroke="#475569"/><ellipse cx="{x+130}" cy="{y+8}" rx="22" ry="18" fill="#e9b797" stroke="#475569"/><rect x="{x-75}" y="{y+45}" width="25" height="53" fill="#94a3b8"/><rect x="{x+92}" y="{y+45}" width="25" height="53" fill="#94a3b8"/>'
def camera(lang):
    out='<rect x="15" y="15" width="710" height="310" fill="#f8fafc" stroke="#94a3b8"/><path d="M250 250V121Q250 40 340 40H461Q505 40 505 102V221H449V113Q449 92 429 92H333Q303 92 303 127V250Z" fill="#e2e8f0" stroke="#64748b" stroke-width="3"/><rect x="302" y="118" width="177" height="35" rx="7" fill="#cbd5e1" stroke="#334155"/><rect x="275" y="162" width="40" height="94" rx="7" fill="#cbd5e1" stroke="#334155"/>'
    out+=patient(375,214)
    # Two attendants and the patient preserve the source photograph's setup.
    out+='<circle cx="146" cy="123" r="23" fill="#e9b797" stroke="#475569"/><path d="M125 148L103 255L165 278L197 195L165 150Z" fill="#fff" stroke="#64748b"/><path d="M170 183L229 212L219 224L159 202" fill="#fff" stroke="#64748b"/><path d="M143 90Q111 89 121 132L139 118L166 115Q171 90 143 90" fill="#475569"/><circle cx="600" cy="116" r="22" fill="#e9b797" stroke="#475569"/><path d="M580 139L553 218L626 245L649 182L620 141Z" fill="#fff" stroke="#64748b"/><path d="M579 170L523 208L534 221L591 192" fill="#fff" stroke="#64748b"/>'
    return svg(out,740,340,{'en':'Coded schematic of the source gamma camera photograph: patient on a bed beneath detector equipment, with two attendants','ur':'اصل گاما کیمرا تصویر کا کوڈ شدہ خاکہ: سراغ رساں آلات کے نیچے بستر پر مریض اور دو طبی اہلکار','ps':'د اصلي ګاما کامرې انځور کوډ شوې طرحه: د کشفوونکو لاندې پر بستر ناروغ او دوه طبي کارکوونکي'}[lang])
def therapy(lang):
    out='<rect x="15" y="15" width="710" height="310" fill="#f8fafc" stroke="#94a3b8"/><path d="M200 36H378L452 82L423 128L321 112L272 175L211 161L169 85Z" fill="#cbd5e1" stroke="#475569" stroke-width="3"/><path d="M272 110L347 137L328 197L253 173Z" fill="#64748b" stroke="#334155"/><rect x="263" y="174" width="61" height="22" fill="#172033"/>'
    out+=patient(280,215)
    out+='<circle cx="586" cy="124" r="22" fill="#d5a080" stroke="#475569"/><path d="M566 145L530 240L607 272L646 209L609 148Z" fill="#fff" stroke="#64748b"/><path d="M560 181L459 215L466 232L575 204" fill="#fff" stroke="#64748b"/><path d="M568 117Q562 90 587 94Q612 96 609 117" fill="#334155"/>'
    return svg(out,740,340,{'en':'Coded schematic of the source radiotherapy photograph: treatment head above a reclining patient and an attendant','ur':'اصل تابکاری علاج کی تصویر کا کوڈ شدہ خاکہ: لیٹے مریض کے اوپر علاج کا آلہ اور طبی اہلکار','ps':'د وړانګو د درملنې د اصلي انځور کوډ شوې طرحه: د پروت ناروغ پر سر د درملنې وسیله او طبي کارکوونکی'}[lang])
def ref(n):return {'pdfPage':192,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-medical-radiation-and-fundamental-forces-372-373','title':'Medical uses of radiation and basic forces of nature','kind':'lesson','pdfPage':192,'printedPage':372,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
sec=section(record,T,L,('تابکاری کے طبی استعمال اور فطرت کی بنیادی قوتیں','د وړانګو طبي استعمالونه او د طبیعت بنسټیز ځواکونه'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(372),ref(373)],sourceBlocks=[
 {'id':'phys20-192-gamma-camera','type':'figure','sourceFigure':'20.24','representation':'Coded source-photo schematic','svg':camera('en'),'svgUrdu':camera('ur'),'svgPashto':camera('ps')},
 {'id':'phys20-192-radiotherapy','type':'figure','sourceFigure':'20.25','representation':'Coded source-photo schematic','svg':therapy('en'),'svgUrdu':therapy('ur'),'svgPashto':therapy('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,definitions=[{'term':'Radiation therapy','definition':T[11][0],'sourceReferences':[ref(372)]}])
    stage_reference(192,record,'Inspected full PDF192 (printed372–373), using cached OCR only as an aid. Restored exact medical-diagnostic paragraphs, Tc-99m metastable notation, complete PET box with four isotope/half-life pairs, radiation-therapy paragraphs, all force headings, prose and source range/strength exponents. Figures20.24/20.25 preserve the source apparatus/patient arrangement as coded schematics. All source paragraphs, headings and caption have aligned Urdu/Pashto translations; source notation rendered with KaTeX.')
    print('PDF192 source-fidelity correction staged.')
