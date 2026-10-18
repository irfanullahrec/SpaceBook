"""PDF191 source prose, radiation pie chart and coded source-photo schematics."""
from html import escape
import math
from class12_source_review import upsert, section, shared_class_data_lock
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
add('heading','C. TERRESTRIAL RADIATION','C. ارضی تابکاری','C. ځمکنۍ وړانګې')
add('paragraph','Radioactive material is also found throughout nature. It is in the soil, water, and vegetation. The dose from terrestrial sources also varies in different parts of the world.',
 'تابکار مادہ پوری فطرت میں بھی پایا جاتا ہے۔ یہ مٹی، پانی اور نباتات میں موجود ہوتا ہے۔ ارضی ذرائع سے حاصل ہونے والی تابکاری کی خوراک بھی دنیا کے مختلف حصوں میں مختلف ہوتی ہے۔',
 'راډیواکټیف مواد په ټول طبیعت کې هم موندل کېږي. دا په خاوره، اوبو او بوټو کې شته. له ځمکنیو سرچینو څخه د وړانګو دوز هم د نړۍ په بېلابېلو برخو کې توپیر لري.')
add('paragraph','The major isotopes of concern for terrestrial radiation are uranium and the decay products of uranium, such as thorium, radium, and especially radon. We cannot see it, smell it, or taste it, but radon is the leading source of natural radiation exposure. Building materials and ground always emit these radiations.',
 'ارضی تابکاری کے حوالے سے اہم آئسوٹوپس یورینیم اور اس کے زوال سے بننے والے مادے ہیں، مثلاً تھوریم، ریڈیم اور خصوصاً ریڈون۔ ہم اسے دیکھ، سونگھ یا چکھ نہیں سکتے، لیکن ریڈون قدرتی تابکاری کے سامنا ہونے کا سب سے بڑا ذریعہ ہے۔ تعمیراتی مواد اور زمین ہمیشہ یہ تابکاری خارج کرتے ہیں۔',
 'د ځمکنیو وړانګو په تړاو مهم ایزوټوپونه یورانیم او د هغه د زوال محصولات دي، لکه توریم، رادیم او په ځانګړي ډول راډون. موږ یې نه شو لیدلی، بویولی یا څکلی، خو راډون د طبیعي وړانګو د اغېز تر ټولو لویه سرچینه ده. ساختماني مواد او ځمکه تل دا وړانګې خپروي.')
add('paragraph','Radiation exposure may result from artificial sources (source produced by men), the most significant source of man-made radiation exposure to the public is from medical procedures, such as diagnostic X-rays, nuclear medicine, and radiation therapy, as shown in figure 20.22.',
 'د تابکاری سامنا مصنوعی ذرائع (انسان کے پیدا کردہ ذرائع) سے بھی ہو سکتا ہے۔ عام لوگوں کے لیے انسانی ساختہ تابکاری کا سب سے اہم ذریعہ طبی طریقے ہیں، مثلاً تشخیصی ایکس رے، نیوکلیائی طب اور تابکاری سے علاج، جیسا کہ شکل 20.22 میں دکھایا گیا ہے۔'.replace('د تابکاری','تابکاری'),
 'له مصنوعي سرچینو (د انسان له خوا جوړو شوو سرچینو) څخه هم د وړانګو اغېز رامنځته کېدای شي. پر عامو خلکو د انسان جوړو شوو وړانګو د اغېز تر ټولو مهمه سرچینه طبي کړنلارې دي، لکه تشخیصي ایکس وړانګې، هستوي طب او د وړانګو درملنه، لکه په 20.22 شکل کې چې ښودل شوي دي.')
add('heading','FIGURE 20.22','شکل 20.22','شکل 20.22')
add('paragraph','Sources of radiation','تابکاری کے ذرائع','د وړانګو سرچینې')
L.append({'type':'visual','blockId':'phys20-191-radiation-sources'})
add('paragraph','All biological damage effects begin with the consequence of radiation interactions with the atoms forming the cells. The cell damage may lead to two effects.',
 'تمام حیاتیاتی نقصان کے اثرات ان تعاملات کے نتیجے سے شروع ہوتے ہیں جو تابکاری اور خلیوں کو بنانے والے ایٹموں کے درمیان ہوتے ہیں۔ خلیے کا نقصان دو اثرات کا باعث بن سکتا ہے۔',
 'د ټولو بیولوژیکي زیانونو اغېزې د وړانګو او د حجرو د جوړوونکو اټومونو د تعاملونو له پایلو پیلېږي. د حجرې زیان د دوو اغېزو لامل کېدای شي.')
add('heading','i. Somatic Effect:','i. جسمانی اثر:','i. جسمي اغېز:')
add('paragraph','The effects which appears soon after irradiation. Such as skin burns, loss of hair and induction of cancer.',
 'وہ اثرات جو شعاع ریزی کے فوراً بعد ظاہر ہوتے ہیں۔ مثلاً جلد کا جلنا، بالوں کا جھڑنا اور سرطان پیدا ہونا۔',
 'هغه اغېزې چې د وړانګو تر لګېدو لږ وروسته څرګندېږي. لکه د پوستکي سوځېدل، د وېښتانو تویېدل او د سرطان پیدا کېدل.')
add('heading','ii. Genetic effects:','ii. جینیاتی اثرات:','ii. ارثي اغېزې:')
add('paragraph','These effects may not appear in the individual life but damage genes and chromosomes that affect future generations.',
 'یہ اثرات فرد کی زندگی میں ظاہر نہ بھی ہوں، لیکن جینز اور کروموسومز کو نقصان پہنچاتے ہیں جو آئندہ نسلوں پر اثر انداز ہوتا ہے۔',
 'دا اغېزې ښايي د یوه فرد په ژوند کې څرګندې نه شي، خو جینونو او کروموزومونو ته زیان رسوي چې راتلونکې نسلونه اغېزمنوي.')
add('heading','20.17 BIOLOGICAL AND MEDICAL USES OF RADIATION','20.17 تابکاری کے حیاتیاتی اور طبی استعمال','20.17 د وړانګو بیولوژیکي او طبي استعمالونه')
add('paragraph','Although scientists have only known about radiation since the 1890s, they have developed a wide variety of uses for this natural force. Today, radiation is used in medicine, academics, and industry.',
 'اگرچہ سائنس دان 1890 کی دہائی ہی سے تابکاری کے بارے میں جانتے ہیں، لیکن انہوں نے اس قدرتی قوت کے بہت سے مختلف استعمال وضع کیے ہیں۔ آج تابکاری طب، تعلیم اور صنعت میں استعمال ہوتی ہے۔',
 'که څه هم ساینسپوهان یوازې د 1890مو کلونو راهیسې د وړانګو په اړه پوهېږي، خو د دې طبیعي ځواک لپاره یې ډېر بېلابېل استعمالونه رامنځته کړي دي. نن وړانګې په طب، زده کړو او صنعت کې کارول کېږي.')
add('heading','A. BIOLOGICAL USES','A. حیاتیاتی استعمال','A. بیولوژیکي استعمالونه')
add('paragraph','Nuclear techniques are used in farming and agricultural communities to combat disease and provide other benefits.',
 'کاشت کاری اور زرعی معاشروں میں بیماریوں کا مقابلہ کرنے اور دیگر فوائد حاصل کرنے کے لیے نیوکلیائی تکنیکیں استعمال کی جاتی ہیں۔',
 'په کرنه او کرنیزو ټولنو کې د ناروغیو د مخنیوي او د نورو ګټو د ترلاسه کولو لپاره هستوي تخنیکونه کارول کېږي.')
add('heading','i. Food Preservation:','i. خوراک کا تحفظ:','i. د خوړو ساتنه:')
add('paragraph','Gamma rays can be used to kill bacteria, mould and insects in food.',
 'خوراک میں بیکٹیریا، پھپھوندی اور کیڑے مارنے کے لیے گاما شعاعیں استعمال کی جا سکتی ہیں۔',
 'په خوړو کې د بکتریاوو، چڼاسکو او حشراتو د وژلو لپاره ګاما وړانګې کارول کېدای شي.')
add('heading','ii. Sterilizing:','ii. جراثیم سے پاک کرنا:','ii. تعقیمول:')
add('paragraph','Gamma rays are also used to sterilize hospital equipment, especially plastic syringes that would be damaged if heated.',
 'ہسپتال کے آلات، خصوصاً پلاسٹک کی سرنجوں، کو جراثیم سے پاک کرنے کے لیے بھی گاما شعاعیں استعمال کی جاتی ہیں؛ ان سرنجوں کو گرم کرنے سے نقصان پہنچ سکتا ہے۔',
 'ګاما وړانګې د روغتون د وسایلو د تعقیمولو لپاره هم کارول کېږي، په ځانګړي ډول د پلاستیکي پېچکاریو لپاره چې په تودولو سره زیانمنېږي.')
add('heading','FIGURE 20.23','شکل 20.23','شکل 20.23')
L.append({'type':'visual','blockId':'phys20-191-preservation'})
add('paragraph','Preserving food and sterilization of medical equipment','خوراک کو محفوظ کرنا اور طبی آلات کو جراثیم سے پاک کرنا','د خوړو ساتنه او د طبي وسایلو تعقیمول')
add('heading','iii. Insect Control:','iii. کیڑوں کا تدارک:','iii. د حشراتو کنټرول:')
add('paragraph','Controlling insects with chemicals can create environmental problems and result in toxic residues in food. The major way of controlling insects without the use of chemicals is the Sterile Insect Technique.',
 'کیمیائی مادوں سے کیڑوں کا تدارک ماحولیاتی مسائل پیدا کر سکتا ہے اور خوراک میں زہریلی باقیات کا باعث بن سکتا ہے۔ کیمیائی مادے استعمال کیے بغیر کیڑوں پر قابو پانے کا اہم طریقہ بانجھ کیڑوں کی تکنیک ہے۔',
 'په کیمیاوي موادو د حشراتو کنټرول چاپېریالي ستونزې او په خوړو کې زهرجنې پاتې شونې رامنځته کولی شي. د کیمیاوي موادو له کارولو پرته د حشراتو د کنټرول اصلي لاره د شنډو حشراتو تخنیک دی.')
add('heading','iv. Chemical Study:','iv. کیمیائی مطالعہ:','iv. کیمیاوي مطالعه:')
add('paragraph',r'The chemical changes in living organism can be studied through tracer method. For example the process of photosynthesis and incorporation of carbon atoms in \(\mathrm{CO}_{2}\) into giant protein or Carbohydrate molecules have been investigated by tracer technique.',
 r'جاندار میں کیمیائی تبدیلیوں کا مطالعہ ٹریسر طریقے سے کیا جا سکتا ہے۔ مثلاً ضیائی تالیف کے عمل اور \(\mathrm{CO}_{2}\) کے کاربن ایٹموں کے بڑے پروٹین یا کاربوہائیڈریٹ سالموں میں شامل ہونے کی تحقیق ٹریسر تکنیک سے کی گئی ہے۔',
 r'په ژوندي موجود کې کیمیاوي بدلونونه د نښه کوونکي په طریقه څېړل کېدای شي. د بېلګې په توګه، د ضیایي ترکیب بهیر او له \(\mathrm{CO}_{2}\) څخه د کاربن اټومونو په لویو پروټیني یا کاربوهایډرېټي مالیکولونو کې شاملېدل د نښه کوونکي تخنیک په وسیله څېړل شوي دي.')

CHART=[{'key':'radon','percent':40},{'key':'building','percent':15},{'key':'artificial','percent':18},{'key':'cosmic','percent':12},{'key':'body','percent':15}]
WORDS={
 'en':{'radon':['Radon gas','from ground'],'building':['Building and','ground'],'body':['Human Body','and food'],'cosmic':['Cosmic','rays'],'artificial':['Artificial','Sources'],'natural':['Natural Sources'],'medical':['Medical'],'other':['Nuclear power,','weapons test and others'],'artificialTitle':['Artificial Sources']},
 'ur':{'radon':['زمین سے','ریڈون گیس'],'building':['عمارت اور','زمین'],'body':['انسانی جسم','اور خوراک'],'cosmic':['کائناتی','شعاعیں'],'artificial':['مصنوعی','ذرائع'],'natural':['قدرتی ذرائع'],'medical':['طبی'],'other':['نیوکلیائی بجلی،','ہتھیاروں کے تجربات اور دیگر'],'artificialTitle':['مصنوعی ذرائع']},
 'ps':{'radon':['له ځمکې څخه','راډون ګاز'],'building':['ودانۍ او','ځمکه'],'body':['د انسان بدن','او خواړه'],'cosmic':['کایناتي','وړانګې'],'artificial':['مصنوعي','سرچینې'],'natural':['طبیعي سرچینې'],'medical':['طبي'],'other':['هستوي برېښنا،','د وسلو ازموینې او نور'],'artificialTitle':['مصنوعي سرچینې']}}
def lines(x,y,values,size=17):return ''.join(text(x,y+i*22,value,size) for i,value in enumerate(values))
def pie(lang):
    words=WORDS[lang];cx=280;cy=230;r=140;angle=120;out=''
    colors=['#67e8f9','#bef264','#fda4af','#e879f9','#a78bfa']
    # Main sectors are generated from the five source percentages, totaling100.
    for item,color in zip(CHART,colors):
        start=math.radians(angle);end=math.radians(angle+item['percent']*3.6)
        x1=cx+r*math.cos(start);y1=cy+r*math.sin(start);x2=cx+r*math.cos(end);y2=cy+r*math.sin(end)
        out+=f'<path d="M{cx} {cy}L{x1:.2f} {y1:.2f}A{r} {r} 0 0 1 {x2:.2f} {y2:.2f}Z" fill="{color}" stroke="#fff" stroke-width="2"/>'
        angle+=item['percent']*3.6
    # Leader positions refer to their correctly sized sectors.
    out+='<g fill="none" stroke="#334155" stroke-width="1.5"><path d="M206 174L113 99"/><path d="M290 140L382 84"/><path d="M370 233L475 223"/><path d="M330 313L395 377"/><path d="M236 323L222 393"/></g>'
    out+=lines(94,52,words['radon']+['40%'])+lines(395,41,words['building']+['15 %'])+lines(498,221,words['artificial']+['18 %'])+lines(402,398,words['cosmic']+['12 %'])+lines(215,419,words['body']+['15 %'])
    out+=lines(283,502,words['natural'])
    # The source gives no numerical split inside the artificial category.
    out+='<path d="M419 210L607 137L607 366L419 255Z" fill="#fed7aa" opacity=".35"/>'
    out+='<circle cx="720" cy="253" r="116" fill="#fda4af" stroke="#64748b"/><path d="M720 253L704 138A116 116 0 0 1 736 138Z" fill="#c084fc" stroke="#fff"/>'
    out+='<path d="M720 151V88M747 290L773 389" stroke="#334155" fill="none"/>'
    out+=lines(725,44,words['other'])+lines(777,418,words['medical'])+lines(720,502,words['artificialTitle'])
    return svg(out,950,535,{'en':'Sources of radiation: radon40%, building15%, body and food15%, cosmic12%, artificial18%; artificial sources shown as medical and other without a numerical sub-split','ur':'تابکاری کے ذرائع: ریڈون40%، عمارت15%، جسم و خوراک15%، کائناتی12%، مصنوعی18%؛ مصنوعی ذرائع میں طبی اور دیگر کی الگ عددی شرح نہیں دی گئی','ps':'د وړانګو سرچینې: راډون40%، ودانۍ15%، بدن او خواړه15%، کایناتي12%، مصنوعي18%؛ د مصنوعي سرچینو د طبي او نورو برخو جلا سلنې نه دي ورکړل شوې'}[lang])
def preservation(lang):
    sticker={'en':['IRRADIATED TO','PROTECT THE','ENVIRONMENT'],'ur':['ماحول کی حفاظت','کے لیے شعاع ریزی','کی گئی ہے'],'ps':['د چاپېریال د','ساتنې لپاره پرې','وړانګې اچول شوې']}[lang]
    out='<rect x="8" y="15" width="382" height="280" fill="#f8fafc" stroke="#64748b"/><ellipse cx="200" cy="174" rx="170" ry="110" fill="#ea8b55" stroke="#9a3412" stroke-width="2"/>'
    # A code schematic of the source fruit label, not a raster or substitute text.
    out+='<path d="M182 73Q208 48 230 80" fill="#4d7c0f"/><rect x="151" y="104" width="210" height="102" rx="3" fill="#fff" stroke="#94a3b8"/>'
    out+='<circle cx="175" cy="137" r="14" fill="none" stroke="#166534"/><path d="M162 141Q175 160 188 141M175 142V123M175 137Q160 120 161 135M175 137Q190 119 190 135" fill="#86efac" stroke="#166534"/>'
    out+=lines(264,132,sticker,15)
    # Open chamber, shelves, tray and operator's gloved hand from the source photo.
    out+='<rect x="453" y="57" width="312" height="199" rx="7" fill="#cbd5e1" stroke="#334155" stroke-width="3"/><rect x="667" y="77" width="71" height="31" fill="#172033"/><circle cx="700" cy="137" r="9" fill="#64748b"/><ellipse cx="545" cy="157" rx="74" ry="87" fill="#172033" stroke="#94a3b8" stroke-width="8"/><path d="M495 123H595M481 159H610M495 195H595" stroke="#e2e8f0" stroke-width="5"/><ellipse cx="437" cy="167" rx="24" ry="91" fill="#94a3b8" stroke="#334155" stroke-width="4"/><path d="M498 218L680 200L715 231L527 248Z" fill="#e2e8f0" stroke="#64748b" stroke-width="3"/><path d="M555 222L640 212M562 230L650 219" stroke="#64748b" stroke-width="3"/><path d="M790 189L685 205L651 217Q641 221 650 229L682 224L672 237Q674 245 684 237L707 223L790 214Z" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>'
    return svg(out,805,315,{'en':'Coded schematic of the source photographs: irradiation label on fruit and open medical equipment sterilization chamber with tray','ur':'اصل تصاویر کا کوڈ شدہ خاکہ: پھل پر شعاع ریزی کا لیبل اور ٹرے کے ساتھ طبی آلات کی جراثیم کشی کا کھلا خانہ','ps':'د اصلي انځورونو کوډ شوې طرحه: پر مېوه د وړانګو نښه او له پتنوس سره د طبي وسایلو د تعقیم پرانیستی خونه'}[lang])
def ref(n):return {'pdfPage':191,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-terrestrial-radiation-effects-and-biomedical-uses-370-371','title':'Terrestrial radiation, effects and biological uses','kind':'lesson','pdfPage':191,'printedPage':370,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
sec=section(record,T,L,('ارضی تابکاری، اثرات اور حیاتیاتی استعمال','ځمکنۍ وړانګې، اغېزې او بیولوژیکي استعمالونه'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(370),ref(371)],sourceBlocks=[
 {'id':'phys20-191-radiation-sources','type':'figure','sourceFigure':'20.22','chartData':CHART,'unnumberedSubcategories':['Medical','Nuclear power, weapons test and others'],'svg':pie('en'),'svgUrdu':pie('ur'),'svgPashto':pie('ps')},
 {'id':'phys20-191-preservation','type':'figure','sourceFigure':'20.23','representation':'Coded schematic of source photographs; instructional objects and label retained.','svg':preservation('en'),'svgUrdu':preservation('ur'),'svgPashto':preservation('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():upsert([record],[sec],chapter_index=9)
    stage_reference(191,record,'Visually compared full PDF191 (printed370–371) with cached OCR as an aid. Restored all terrestrial/artificial radiation paragraphs, two effects, biological-use introduction and four applications with original paragraph boundaries. Figure20.22 is generated from40/15/18/12/15 source percentages; both artificial subcategory labels retained without inventing numerical shares. Figure20.23 fruit/irradiation label and open equipment chamber recreated as coded schematics. All headings, prose, captions and visual text have Urdu/Pashto translations.')
    print('PDF191 source-fidelity correction staged.')
