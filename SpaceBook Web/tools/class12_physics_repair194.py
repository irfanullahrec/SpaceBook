"""PDF194: source quark table, baryon/meson diagram and all color equations."""
from class12_source_review import upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, svg, arrow
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];ROWS={}
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
def eq(s):s=r'\('+s+r'\)';add('equation',s,s,s)
add('paragraph','As more and more hadrons were discovered, it became clear that they were not all elementary particles. The suggestion was made that the hadrons are made up of smaller, more elementary particles called quarks. In-1963, a quark theory was initiated independently by M. Gell-Mann (1929- ) and G. Zweig (1937- ).',
 'جیسے جیسے مزید ہیڈران دریافت ہوئے، یہ واضح ہو گیا کہ یہ سب بنیادی ذرات نہیں تھے۔ یہ تجویز پیش کی گئی کہ ہیڈران چھوٹے، زیادہ بنیادی ذرات سے بنے ہیں جنہیں کوارکس کہتے ہیں۔ 1963 میں ایم گیل مان (1929- ) اور جی زوائگ (1937- ) نے آزادانہ طور پر کوارک نظریے کی ابتدا کی۔',
 'کله چې نور او نور هاډرونونه وموندل شول، څرګنده شوه چې دا ټول بنسټیزې ذرې نه وې. دا وړاندیز وشو چې هاډرونونه له کوچنیو او لا بنسټیزو ذرو جوړ دي چې کوارکونه بلل کېږي. په1963 کې اېم ګېل مان (1929- ) او جي زوایګ (1937- ) په خپلواک ډول د کوارک نظریه پیل کړه.')
add('paragraph','Quark Model is based on the following assumptions:',
 'کوارک ماڈل درج ذیل مفروضات پر مبنی ہے:',
 'د کوارک ماډل پر لاندې فرضیو ولاړ دی:')
add('numberedList','1. There are six types of quark up (u), down (d), strange (s), charm (c), top (t) and bottom (b).',
 '1. کوارک کی چھ اقسام ہیں: اَپ (u)، ڈاؤن (d)، سٹرینج (s)، چارم (c)، ٹاپ (t) اور باٹم (b)۔',
 '1. کوارک شپږ ډولونه لري: اپ (u)، ډاون (d)، سټرېنج (s)، چارم (c)، ټاپ (t) او باټم (b).')
add('numberedList','2. Every quark has corresponding antiquark denoted by the same letter with a bar over it.',
 '2. ہر کوارک کا ایک متناظر ضد کوارک ہوتا ہے، جسے اسی حرف کے اوپر ایک لکیر لگا کر ظاہر کیا جاتا ہے۔',
 '2. هر کوارک یو اړوند ضد کوارک لري، چې د هماغه توري پر سر د یوې کرښې په اېښودلو ښودل کېږي.')
add('heading','Table 20.6 QUARKS','جدول 20.6 کوارکس','جدول 20.6 کوارکونه')
rows=[(['Name',r'Mass (\(\mathrm{GeV}/c^{2}\))','Symbol','Charge'],['نام',r'کمیت (\(\mathrm{GeV}/c^{2}\))','علامت','بار'],['نوم',r'کتله (\(\mathrm{GeV}/c^{2}\))','نښه','چارج'])]
for names,mass,symbol,charge in [
 (['up','اَپ','اپ'],'0.004','u','+ 2/3'),(['down','ڈاؤن','ډاون'],'0.008','d','- 1/3'),(['strange','سٹرینج','سټرېنج'],'0.15','s','- 1/3'),(['charm','چارم','چارم'],'1.5','c','+ 2/3'),(['bottom','باٹم','باټم'],'4.7','b','- 1/3'),(['top','ٹاپ','ټاپ'],'176','t','+ 2/3')]:
    rows.append(tuple([names[i],mass,symbol,charge] for i in range(3)))
indices=[]
for row in rows:
    index=len(T);indices.append(index);ROWS[index]=row[0];T.append(tuple(' — '.join(cells) for cells in row))
L.append({'type':'table','indices':indices})
add('heading','FIGURE 20.27','شکل 20.27','شکل 20.27')
L.append({'type':'visual','blockId':'phys20-194-quark-combinations'})
add('paragraph','According to the original quark model of hadrons, all mesons consist of a quark and an antiquark, whereas baryons contain three quarks.',
 'ہیڈرانوں کے اصل کوارک ماڈل کے مطابق تمام میزونز ایک کوارک اور ایک ضد کوارک پر مشتمل ہوتے ہیں، جبکہ بیریونز میں تین کوارکس ہوتے ہیں۔',
 'د هاډرونونو د اصلي کوارک ماډل له مخې ټول مېزونونه له یوه کوارک او یوه ضد کوارک څخه جوړ دي، خو باریونونه درې کوارکونه لري.')
add('numberedList','3. Quarks combine in three to form baryons (proton, neutron, sigma e.t.c.) and antiquarks combine in three to form anti-baryons (anti-proton, anti-neutron, anti-sigma e.t.c.) as shown in figure 20.27.',
 '3. تین کوارکس مل کر بیریونز (پروٹون، نیوٹرون، سگما وغیرہ) بناتے ہیں اور تین ضد کوارکس مل کر ضد بیریونز (ضد پروٹون، ضد نیوٹرون، ضد سگما وغیرہ) بناتے ہیں، جیسا کہ شکل 20.27 میں دکھایا گیا ہے۔',
 '3. درې کوارکونه سره یوځای کېږي او باریونونه (پروتون، نیوټرون، سیګما او نور) جوړوي. درې ضد کوارکونه سره یوځای کېږي او ضد باریونونه (ضد پروتون، ضد نیوټرون، ضد سیګما او نور) جوړوي، لکه په20.27 شکل کې چې ښودل شوي دي.')
add('numberedList','4. Quarks combine with antiquarks in twos to form mesons.',
 '4. کوارکس ضد کوارکس کے ساتھ دو دو کے جوڑوں میں مل کر میزونز بناتے ہیں۔',
 '4. کوارکونه له ضد کوارکونو سره په دوو کې یوځای کېږي او مېزونونه جوړوي.')
add('heading','D. COLOR CHARGE','D. رنگی بار','D. رنګیز چارج')
add('paragraph','Electric charge comes in only one kind (positive) and its opposite (negative), but strong charge comes in three kinds (called red, blue, and green), each of which has an opposite (called antired, antiblue, and antigreen). Color charge has nothing to do with the colors of light that we perceive visually. They are based on an analogy: just as the red, blue, and green dots produced by different phosphors on a TV screen combine to make white, a red quark, blue quark, and green quark combine to form a colorless (white) combination.',
 'برقی بار صرف ایک قسم (مثبت) اور اس کی مخالف (منفی) صورت میں ہوتا ہے، لیکن قوی بار کی تین اقسام ہیں (جنہیں سرخ، نیلا اور سبز کہتے ہیں)۔ ان میں سے ہر ایک کی مخالف قسم بھی ہے (جسے ضد سرخ، ضد نیلا اور ضد سبز کہتے ہیں)۔ رنگی بار کا روشنی کے ان رنگوں سے کوئی تعلق نہیں جو ہم آنکھوں سے دیکھتے ہیں۔ یہ ایک تشبیہ پر مبنی ہیں: جیسے ٹی وی کی سکرین پر مختلف فاسفروں سے پیدا ہونے والے سرخ، نیلے اور سبز نقطے مل کر سفید بناتے ہیں، ویسے ہی ایک سرخ کوارک، ایک نیلا کوارک اور ایک سبز کوارک مل کر بے رنگ (سفید) مجموعہ بناتے ہیں۔',
 'برېښنايي چارج یوازې یو ډول (مثبت) او د هغه مخالف (منفي) لري، خو قوي چارج درې ډولونه لري (سور، شین آبي او زرغون بلل کېږي)، چې هر یو یې مخالف هم لري (ضد سور، ضد شین آبي او ضد زرغون بلل کېږي). رنګیز چارج د رڼا له هغو رنګونو سره هېڅ تړاو نه لري چې موږ یې په سترګو وینو. دا پر یوې تشبیه ولاړ دي: لکه چې د تلویزیون پر پرده د بېلابېلو فاسفورونو سور، شین آبي او زرغون ټکي سره یوځای شي او سپین رنګ جوړ کړي، همداسې یو سور، یو شین آبي او یو زرغون کوارک سره یوځای کېږي او بې رنګه (سپین) ترکیب جوړوي.')
add('paragraph','All free particles have a color charge of zero. A baryon always contains one quark of each color, an antibaryon always contains one antiquark of each anticolor, and a meson always contains a quark of one color and an antiquark of the corresponding anticolor, such as a red quark and an antired antiquark. In each case, the strong force holds quarks together in colorless combinations, similar to the way the electromagnetic force holds negative and positive charges together to form a neutral atom with zero net electric charge.',
 'تمام آزاد ذرات کا رنگی بار صفر ہوتا ہے۔ ایک بیریون میں ہمیشہ ہر رنگ کا ایک کوارک ہوتا ہے، ایک ضد بیریون میں ہمیشہ ہر ضد رنگ کا ایک ضد کوارک ہوتا ہے، اور ایک میزون میں ہمیشہ ایک رنگ کا کوارک اور اس کے متناظر ضد رنگ کا ضد کوارک ہوتا ہے، مثلاً سرخ کوارک اور ضد سرخ ضد کوارک۔ ہر صورت میں قوی قوت کوارکس کو بے رنگ مجموعوں میں اکٹھا رکھتی ہے، اسی طرح جیسے برق مقناطیسی قوت منفی اور مثبت باروں کو اکٹھا رکھ کر صفر خالص برقی بار والا غیر بار دار ایٹم بناتی ہے۔',
 'د ټولو آزادو ذرو رنګیز چارج صفر دی. یو باریون تل د هر رنګ یو کوارک لري، یو ضد باریون تل د هر ضد رنګ یو ضد کوارک لري، او یو مېزون تل د یوه رنګ کوارک او د هغه د اړوند ضد رنګ ضد کوارک لري، لکه سور کوارک او ضد سور ضد کوارک. په هر حالت کې قوي ځواک کوارکونه په بې رنګه ترکیبونو کې سره یوځای ساتي، لکه برېښنا مقناطیسي ځواک چې منفي او مثبت چارجونه سره یوځای ساتي او د صفر خالص برېښنايي چارج لرونکی خنثی اټوم جوړوي.')
add('equation','Red + green + blue = white','سرخ + سبز + نیلا = سفید','سور + زرغون + شین آبي = سپین')
eq(r'r+g+b=0')
add('equation','Anti-Red (cyan) + Anti-green (magenta) + Anti-blue (yellow) = white',
 'ضد سرخ (فیروزی) + ضد سبز (ارغوانی) + ضد نیلا (پیلا) = سفید',
 'ضد سور (فیروزه يي) + ضد زرغون (ارغواني) + ضد شین آبي (ژېړ) = سپین')
eq(r'\bar{r}+\bar{g}+\bar{b}=0')
add('equation','red + anti-red = white, green + anti-green = white, blue + anti-blue = white',
 'سرخ + ضد سرخ = سفید، سبز + ضد سبز = سفید، نیلا + ضد نیلا = سفید',
 'سور + ضد سور = سپین، زرغون + ضد زرغون = سپین، شین آبي + ضد شین آبي = سپین')
eq(r'r+\bar{r}=g+\bar{g}=b+\bar{b}=0')

Q=[{'particle':'proton','quarks':[('d','- 1/3 e'),('u','+ 2/3 e'),('u','+ 2/3 e')]},
   {'particle':'neutron','quarks':[('d','- 1/3 e'),('d','- 1/3 e'),('u','+ 2/3 e')]},
   {'particle':'pi-','quarks':[('d','- 1/3 e'),('ū','- 2/3 e')]},
   {'particle':'pi+','quarks':[('d̄','+ 1/3 e'),('u','+ 2/3 e')]}]
def combinations(lang):
    words={'en':['Proton','Neutron','π⁻','π⁺','Baryons','Mesons'],'ur':['پروٹون','نیوٹرون','π⁻','π⁺','بیریونز','میزونز'],'ps':['پروتون','نیوټرون','π⁻','π⁺','باریونونه','مېزونونه']}[lang]
    out=''
    colors=['#fef08a','#e9d5ff','#fce7f3','#fef3c7']
    for i,group in enumerate(Q):
        x=112+i*225;y=125
        out+=f'<ellipse cx="{x}" cy="{y}" rx="102" ry="104" fill="{colors[i]}" stroke="#334155" stroke-width="2"/>'
        positions=[(-35,-40),(42,0),(-30,49)] if i==0 else [(14,-44),(-46,12),(39,44)] if i==1 else [(-45,0),(44,0)]
        for j,((symbol,charge),(dx,dy)) in enumerate(zip(group['quarks'],positions)):
            xx=x+dx;yy=y+dy
            out+=f'<circle cx="{xx}" cy="{yy}" r="43" fill="{["#fde68a","#bef264","#c4b5fd"][j]}" stroke="#334155"/>'
            if symbol=='d̄':out+=text(xx,yy-8,'d',25)+f'<path d="M{xx-7} {yy-34}H{xx+7}" stroke="#172033" stroke-width="2"/>'
            else:out+=text(xx,yy-8,symbol,25)
            out+=text(xx,yy+18,charge,17)
        out+=text(x,255,words[i],21)
    for left,right,label in [(15,435,words[4]),(466,885,words[5])]:
        out+=arrow(left+10,281,right,281,'#334155')+arrow(right-10,281,left,281,'#334155')+text((left+right)/2,308,label,21)
    return svg(out,900,335,{'en':'Figure20.27: proton uud and neutron udd baryons; pion-minus d anti-u and pion-plus anti-d u mesons, with every printed fractional charge','ur':'شکل20.27: پروٹون uud اور نیوٹرون udd بیریونز؛ منفی پائیون d ضد-u اور مثبت پائیون ضد-d u میزونز، تمام چھپے کسری باروں کے ساتھ','ps':'شکل20.27: پروتون uud او نیوټرون udd باریونونه؛ منفي پایون d ضد-u او مثبت پایون ضد-d u مېزونونه، له ټولو چاپ شوو کسري چارجونو سره'}[lang])
def ref(n):return {'pdfPage':194,'printedPage':n,'sourcePdf':SOURCE}
record={'id':'phys20-quark-model-masses-and-color-charge-376-377','title':'Quark model, quark table and color charge','kind':'lesson','pdfPage':194,'printedPage':376,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
issues=['Table20.6 quark masses differ from Figure20.26 on printed375 (up, down, strange, charm, bottom and top); the values in each source location are retained separately.']
sec=section(record,T,L,('کوارک ماڈل، کوارکس کا جدول اور رنگی بار','د کوارک ماډل، د کوارکونو جدول او رنګیز چارج'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(376),ref(377)],sourceTableRows=ROWS,sourceIssues=issues,sourceBlocks=[{'id':'phys20-194-quark-combinations','type':'figure','sourceFigure':'20.27','groups':Q,'svg':combinations('en'),'svgUrdu':combinations('ur'),'svgPashto':combinations('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.14','20.15','20.16','20.17'],trim_sections=[{'id':'20.18','startsAt':'Nucleons: The protons and neutrons present in the nucleus','title':'Nuclear physics glossary — pending source-fidelity review','clearSciNote':True}])
    stage_reference(194,record,'Inspected full PDF194 (printed376–377). Restored quark-model introduction, all four assumptions, full Table20.6, all four particle groups/fractional charges in Figure20.27, caption, two distinct color-charge paragraphs and all six word/symbol color equations. Accurate aligned Urdu/Pashto text and figure labels. Retired fully superseded OCR sections20.14–20.17 and kept only the untouched glossary continuation from20.18. Source mass differences remain flagged.',issues)
    print('PDF194 source correction staged; superseded OCR duplicates retired.')
