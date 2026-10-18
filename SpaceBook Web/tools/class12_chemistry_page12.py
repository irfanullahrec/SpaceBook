"""PDF12, printed16–17: hydroxides, coded acid structures and GroupIA opening."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
import html
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
eq('PCl₃(l) + 3H₂O(l) → H₃PO₃(aq) + 3HCl(g)')
eq('PCl₅(s) + 4H₂O(l) → H₃PO₄(aq) + 5HCl(g)')
head('13.1.6 Hydroxides of the Period 3ʳᵈ Elements','13.1.6 تیسرے دور کے عناصر کے ہائیڈرو آکسائیڈز','13.1.6 د درېیمې دورې د عناصرو هایدروکسایډونه')
add('The word “hydroxide” refers to a compound which contains either a OH⁻ ion or an –OH group covalently bonded to the atom of an element. The sodium and magnesium hydroxides are simple basic hydroxides due to the presence of hydroxide ions. These hydroxide ions react with hydrogen ions of acid to form water.',
    'لفظ ”ہائیڈرو آکسائیڈ“ ایسے مرکب کو کہتے ہیں جس میں OH⁻ آئن یا کسی عنصر کے ایٹم سے اشتراکی بند کے ذریعے جڑا –OH گروپ ہو۔ سوڈیم اور میگنیشیم کے ہائیڈرو آکسائیڈز، ہائیڈرو آکسائیڈ آئنوں کی موجودگی کی وجہ سے سادہ اساسی ہائیڈرو آکسائیڈز ہیں۔ یہ آئن تیزاب کے ہائیڈروجن آئنوں سے تعامل کر کے پانی بناتے ہیں۔',
    'د «هایدروکسایډ» کلمه هغه مرکب ته ویل کېږي چې OH⁻ ایون یا د یوه عنصر له اټوم سره په کووالنټ تړون تړلی –OH ګروپ ولري. د سوډیم او مګنیزیم هایدروکسایډونه د هایدروکسایډ ایونونو د شتون له امله ساده قلوي هایدروکسایډونه دي. دا ایونونه د تېزاب له هایدروجن ایونونو سره تعامل کوي او اوبه جوړوي.')
add('Aluminium hydroxide, Al(OH)₃, like aluminium oxide, Al₂O₃, is amphoteric, it reacts with both acids and bases.',
    'ایلومینیم ہائیڈرو آکسائیڈ، Al(OH)₃، ایلومینیم آکسائیڈ، Al₂O₃، کی طرح دو خصوصیتی ہے اور تیزابوں اور اساسوں دونوں کے ساتھ تعامل کرتا ہے۔',
    'المونیم هایدروکسایډ، Al(OH)₃، د المونیم اکسایډ، Al₂O₃، په څېر امفوتېریک دی او له تېزابونو او اساسونو دواړو سره تعامل کوي.')
add('All the other elements e.g. Si, P, S and Cl, which have –OH groups covalently bonded to the atom of period 3 are acidic. They range from very weakly acidic silicic acid to the very strong sulphuric acid or perchloric acid.',
    'باقی عناصر، مثلاً Si، P، S اور Cl، جن کے تیسرے دور کے ایٹم سے –OH گروپ اشتراکی بند کے ذریعے جڑے ہوں، تیزابی ہیں۔ ان کی تیزابیت بہت کمزور سیلیسک ایسڈ سے بہت مضبوط سلفیورک یا پرکلورک ایسڈ تک ہوتی ہے۔',
    'نور ټول عناصر، لکه Si، P، S او Cl، چې –OH ګروپونه یې د درېیمې دورې له اټوم سره په کووالنټ تړون تړلي وي، تېزابي دي. دا له ډېر کمزوري سیلیسیک اسید څخه تر ډېر پیاوړي سلفوریک یا پرکلوریک اسید پورې دي.')

def acid_svg(language):
    captions={'en':['ortho salicic acid','phosphoric acid','sulphuric acid','perchloric acid'],
              'ur':['آرتھو سالیسِک ایسڈ','فاسفورک ایسڈ','سلفیورک ایسڈ','پرکلورک ایسڈ'],
              'ps':['اورتو سالیسیک اسید','فاسفوریک اسید','سلفوریک اسید','پرکلوریک اسید']}[language]
    svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 380" role="img" aria-label="Si P S Cl acid structural formulae"><rect width="600" height="380" fill="white"/>']
    def text(x,y,value,size=17):svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="#881337">{html.escape(value)}</text>')
    for i,(atom,ends) in enumerate([('Si',[('OH',1),('OH',1),('OH',1),('HO',1)]),('P',[('O',2),('OH',1),('OH',1),('HO',1)]),('S',[('OH',1),('O',2),('O',2),('HO',1)]),('Cl',[('OH',1),('O',2),('O',2),('O',2)])]):
        x=150+(i%2)*300;y=85+(i//2)*180
        text(x,y+6,atom)
        for direction,(label,bond) in enumerate(ends):
            dx,dy=[(0,-1),(1,0),(0,1),(-1,0)][direction]
            for offset in ([0] if bond==1 else [-2,2]):
                x1=x+dx*15+(offset if dx==0 else 0);x2=x+dx*43+(offset if dx==0 else 0)
                y1=y+dy*15+(offset if dy==0 else 0);y2=y+dy*43+(offset if dy==0 else 0)
                svg.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#111827" fill="none"/>')
            text(x+dx*62,y+dy*62+6,label)
        text(x,y+92,captions[i],14)
    svg.append('</svg>');return ''.join(svg)
fig={'id':'chem12-p16-acid-structures','svg':acid_svg('en'),'svgUrdu':acid_svg('ur'),'svgPashto':acid_svg('ps')}
blocks.append(fig);layout.append({'type':'visual','blockId':fig['id']})
head('13.1.6.1 Sodium and Magnesium Hydroxides','13.1.6.1 سوڈیم اور میگنیشیم کے ہائیڈرو آکسائیڈز','13.1.6.1 د سوډیم او مګنیزیم هایدروکسایډونه')
add('Sodium hydroxide (NaOH) is a white solids having soapy touch. Skin contact with concentrated caustic soda can cause serious chemical burns. This is highly hygroscopic. Sodium hydroxide is only slightly soluble in alcohols. It is one of the most soluble substances in water evolving a considerable amount of heat.',
    'سوڈیم ہائیڈرو آکسائیڈ (NaOH) سفید ٹھوس مادہ ہے، جس کا لمس صابن جیسا ہے۔ مرتکز کاسٹک سوڈا کا جلد سے رابطہ شدید کیمیائی جلن پیدا کر سکتا ہے۔ یہ بہت زیادہ نمی جذب کرتا ہے۔ سوڈیم ہائیڈرو آکسائیڈ الکوحلوں میں معمولی حل ہوتا ہے۔ یہ پانی میں سب سے زیادہ حل پذیر مادوں میں سے ہے اور حل ہونے پر خاصی حرارت خارج کرتا ہے۔',
    'سوډیم هایدروکسایډ (NaOH) سپین جامد دی چې لمس یې د صابون په څېر دی. له غلیظ کاسټیک سوډا سره د پوستکي تماس شدید کیمیاوي سوځېدنې رامنځته کولای شي. دا ډېر رطوبت جذبوي. سوډیم هایدروکسایډ په الکولونو کې لږ حل کېږي. دا په اوبو کې له تر ټولو ډېر حل کېدونکو موادو څخه دی او د حل کېدو پر مهال د پام وړ تودوخه خوشې کوي.')
add('Magnesium hydroxide, unlike sodium hydroxide, it is classified as a weak base, so it has no exothermic reaction with water. Magnesium hydroxide is obtained as a white precipitate when caustic potash (KOH) solution is added to a soluble magnesium salt. Both hydroxides react with acids to form salts. For example, with dilute hydrochloric acid, colourless solutions of sodium chloride or magnesium chloride are obtained.',
    'سوڈیم ہائیڈرو آکسائیڈ کے برخلاف میگنیشیم ہائیڈرو آکسائیڈ کمزور اساس شمار ہوتا ہے، اس لیے پانی کے ساتھ حرارت خارج کرنے والا تعامل نہیں کرتا۔ حل پذیر میگنیشیم نمک میں کاسٹک پوٹاش (KOH) کا محلول ملانے سے میگنیشیم ہائیڈرو آکسائیڈ سفید رسوب کی صورت میں ملتا ہے۔ دونوں ہائیڈرو آکسائیڈز تیزابوں سے تعامل کر کے نمک بناتے ہیں۔ مثلاً رقیق ہائیڈروکلورک ایسڈ کے ساتھ سوڈیم کلورائیڈ یا میگنیشیم کلورائیڈ کے بے رنگ محلول ملتے ہیں۔',
    'د سوډیم هایدروکسایډ پر خلاف، مګنیزیم هایدروکسایډ کمزوری اساس ګڼل کېږي، نو له اوبو سره تودوخه خوشې کوونکی تعامل نه کوي. کله چې د کاسټیک پوټاش (KOH) محلول په حل کېدونکې مګنیزیم مالګه کې واچول شي، مګنیزیم هایدروکسایډ د سپین رسوب په بڼه ترلاسه کېږي. دواړه هایدروکسایډونه له تېزابونو سره تعامل کوي او مالګې جوړوي. د بېلګې په توګه، له رقیق هایدروکلوریک اسید سره د سوډیم کلورایډ یا مګنیزیم کلورایډ بې رنګه محلولونه ترلاسه کېږي.')
eq('NaOH(aq) + HCl(aq) → NaCl(aq) + H₂O(l)')
eq('Mg(OH)₂(aq) + 2HCl(aq) → MgCl₂(aq) + 2H₂O(l)')
head('13.1.6.2 Aluminium Hydroxide','13.1.6.2 ایلومینیم ہائیڈرو آکسائیڈ','13.1.6.2 المونیم هایدروکسایډ')
add('Aluminium hydroxide is amphoteric in nature. Like sodium or magnesium hydroxides, Al(OH)₃ reacts with acids which shows its basic nature. The Al(OH)₃ reacts with dilute hydrochloric acid and forms a colourless solution of aluminium chloride.',
    'ایلومینیم ہائیڈرو آکسائیڈ کی نوعیت دو خصوصیتی ہے۔ سوڈیم یا میگنیشیم ہائیڈرو آکسائیڈ کی طرح Al(OH)₃ تیزابوں سے تعامل کرتا ہے، جو اس کی اساسی نوعیت ظاہر کرتا ہے۔ یہ رقیق ہائیڈروکلورک ایسڈ سے تعامل کر کے ایلومینیم کلورائیڈ کا بے رنگ محلول بناتا ہے۔',
    'المونیم هایدروکسایډ امفوتېریک ماهیت لري. د سوډیم یا مګنیزیم هایدروکسایډ په څېر Al(OH)₃ له تېزابونو سره تعامل کوي، چې قلوي ماهیت یې ښيي. دا له رقیق هایدروکلوریک اسید سره تعامل کوي او د المونیم کلورایډ بې رنګه محلول جوړوي.')
eq('Al(OH)₃(aq) + 3HCl(aq) → AlCl₃(aq) + 3H₂O(l)')
add('Aluminium hydroxide also shows acidic properties. It reacts with sodium hydroxide solution and forms a colourless solution of sodium tetrahydroxoaluminate (III).',
    'ایلومینیم ہائیڈرو آکسائیڈ تیزابی خصوصیات بھی ظاہر کرتا ہے۔ یہ سوڈیم ہائیڈرو آکسائیڈ کے محلول سے تعامل کر کے سوڈیم ٹیٹرا ہائیڈروکسو ایلومینیٹ (III) کا بے رنگ محلول بناتا ہے۔',
    'المونیم هایدروکسایډ تېزابي ځانګړنې هم ښيي. د سوډیم هایدروکسایډ له محلول سره تعامل کوي او د سوډیم ټېټرا هایدروکسو الومینېټ (III) بې رنګه محلول جوړوي.')
eq('Al(OH)₃(aq) + NaOH(aq) → NaAl(OH)₄(aq)')
add('Sodium tetrahydroxoaluminate (III).','سوڈیم ٹیٹرا ہائیڈروکسو ایلومینیٹ (III)۔','سوډیم ټېټرا هایدروکسو الومینېټ (III).')
head('13.1.6.3 Other Hydroxides','13.1.6.3 دوسرے ہائیڈرو آکسائیڈز','13.1.6.3 نور هایدروکسایډونه')
add('Other elements do not contain hydroxide ions but –OH group is covalently bonded to the atoms of period 3 elements. These compounds are acidic in nature because they can loss H⁺ from –OH group.',
    'دوسرے عناصر میں ہائیڈرو آکسائیڈ آئن نہیں ہوتے، بلکہ –OH گروپ تیسرے دور کے عناصر کے ایٹموں سے اشتراکی بند کے ذریعے جڑا ہوتا ہے۔ یہ مرکبات تیزابی نوعیت رکھتے ہیں، کیونکہ –OH گروپ سے H⁺ کھو سکتے ہیں۔',
    'نور عناصر هایدروکسایډ ایونونه نه لري، خو –OH ګروپ د درېیمې دورې د عناصرو له اټومونو سره په کووالنټ تړون تړلی وي. دا مرکبات تېزابي ماهیت لري، ځکه له –OH ګروپ څخه H⁺ له لاسه ورکولای شي.')
add('Orthosilicic acid is very weak acid. Phosphoric acid is a weak acid but stronger than acetic acid. Sulphuric acid (H₂SO₄) and perchloric acids are very strong acids.',
    'آرتھو سیلیسک ایسڈ بہت کمزور تیزاب ہے۔ فاسفورک ایسڈ کمزور تیزاب ہے، مگر ایسیٹک ایسڈ سے زیادہ مضبوط ہے۔ سلفیورک ایسڈ (H₂SO₄) اور پرکلورک ایسڈ بہت مضبوط تیزاب ہیں۔',
    'اورتو سیلیسیک اسید ډېر کمزوری تېزاب دی. فاسفوریک اسید کمزوری تېزاب دی، خو له اسیتیک اسید څخه پیاوړی دی. سلفوریک اسید (H₂SO₄) او پرکلوریک اسیدونه ډېر پیاوړي تېزابونه دي.')
add('The strength of an acid depends on the stability of it’s anion. Higher the stability of an anion, higher will be the acidic strength of compound.',
    'تیزاب کی طاقت اس کے منفی آئن کے استحکام پر منحصر ہے۔ منفی آئن کا استحکام جتنا زیادہ ہو، مرکب کی تیزابی طاقت اتنی زیادہ ہوگی۔',
    'د تېزاب پیاوړتیا د هغه د منفي ایون په ثبات پورې اړه لري. د منفي ایون ثبات چې هر څومره لوړ وي، د مرکب تېزابي پیاوړتیا به هم هغومره لوړه وي.')
head('13.2 Group – IA Elements','13.2 گروپ IA کے عناصر','13.2 د IA ګروپ عناصر')
add('The elements lithium (Li), sodium (Na), potassium (K), rubidium (Rb), caesium (Cs), and francium (Fr) constitute group – IA of the periodic table. These are known as alkali metals since they form oxide and hydroxides which combine with water to produce alkaline solution. Only the first three of these are safe to keep in the school laboratory. The rest are violently reactive.',
    'لیتھیم (Li)، سوڈیم (Na)، پوٹاشیم (K)، روبیڈیم (Rb)، سیزیم (Cs) اور فرانسیم (Fr) دوری جدول کا گروپ IA بناتے ہیں۔ انہیں الکلی دھاتیں کہتے ہیں، کیونکہ ان کے آکسائیڈز اور ہائیڈرو آکسائیڈز پانی سے مل کر الکلائن محلول بناتے ہیں۔ ان میں صرف پہلی تین دھاتیں اسکول کی تجربہ گاہ میں رکھنا محفوظ ہے؛ باقی نہایت شدت سے تعامل کرتی ہیں۔',
    'لیتیم (Li)، سوډیم (Na)، پوټاشیم (K)، روبیډیم (Rb)، سیزیم (Cs) او فرانسیم (Fr) د دوراني جدول IA ګروپ جوړوي. دا القلي فلزونه بلل کېږي، ځکه اکسایډونه او هایدروکسایډونه یې له اوبو سره یوځای کېږي او قلوي محلول جوړوي. یوازې لومړني درې یې د ښوونځي په لابراتوار کې ساتل خوندي دي؛ پاتې په ډېر شدت تعامل کوي.')
add('The characteristic feature of the sub-group – IA is the ns¹ arrangement in the outermost shell. The elements symbol and their electronic configuration are given in Table 13.11.',
    'ذیلی گروپ IA کی امتیازی خصوصیت سب سے بیرونی خول میں ns¹ ترتیب ہے۔ عناصر کی علامتیں اور ان کی الیکٹرانی ترتیب جدول 13.11 میں دی گئی ہیں۔',
    'د IA فرعي ګروپ ځانګړې نښه په تر ټولو بهرني پوښ کې ns¹ ترتیب دی. د عناصرو سمبولونه او الکتروني ترتیبونه په جدول 13.11 کې ورکړل شوي دي.')
add('Table 13.11 Elements Symbol with Atomic No and their Electronic Configuration','جدول 13.11 ایٹمی نمبر کے ساتھ عناصر کی علامتیں اور ان کی الیکٹرانی ترتیب','جدول 13.11 د عناصرو سمبولونه له اټومي شمېرو او الکتروني ترتیبونو سره')
rows=[['₃Li','1s², 2s¹','[He]2s¹'],['₁₁Na','1s², 2s², 2p⁶, 3s¹','[Ne]3s¹'],['₁₉K','1s², 2s², 2p⁶, 3s², 3p⁶, 4s¹','[Ar]4s¹']]
t={'id':'chem12-table-13-11-opening','headers':['Element symbol with atomic No.','Electronic configuration',''],'headerRows':[[{'title':'Element symbol with atomic No.'},{'title':'Electronic configuration','colspan':2}]],'rows':rows,
   'translations':[{'language':'اردو','headers':['ایٹمی نمبر کے ساتھ عنصر کی علامت','الیکٹرانی ترتیب',''],'headerRows':[[{'title':'ایٹمی نمبر کے ساتھ عنصر کی علامت'},{'title':'الیکٹرانی ترتیب','colspan':2}]],'rows':rows},
                   {'language':'پښتو','headers':['د عنصر سمبول له اټومي شمېر سره','الکتروني ترتیب',''],'headerRows':[[{'title':'د عنصر سمبول له اټومي شمېر سره'},{'title':'الکتروني ترتیب','colspan':2}]],'rows':rows}]}
blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
record=section('13.8','Hydroxides and Group IA elements','ہائیڈرو آکسائیڈز اور گروپ IA کے عناصر','هایدروکسایډونه او د IA ګروپ عناصر',paras,layout,blocks,'16–17')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':12,'printedPages':[16,17]}]
issues=[{'id':'chem12-p16-salicic-caption','printedPage':16,'description':'The Si(OH)4 structural figure is captioned ortho salicic acid, while printed17 prose calls it orthosilicic acid. Printed caption retained; structure preserves all four OH groups.'}]
if __name__=='__main__':save(12,[record],issues=issues,carry=[{'from':'13.8','to':'13.9','startsAt':'37Rb\n'}])
