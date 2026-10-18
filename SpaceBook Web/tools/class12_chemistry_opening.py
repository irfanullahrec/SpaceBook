"""Source-aligned Chemistry XII opening repair; preserves unreviewed later content."""
from pathlib import Path
import json, os, html
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/source-verification/class-12'
SOURCE = 'D:/SpaceBook/Books/12th/12th Chemistry/PDF/Chemistry Book for 12 class KPTBB.pdf'

def pair(en, ur, ps):
    return {'text': en, 'urdu': ur, 'pashto': ps}

def diagram(language):
    labels = {
        'en': ['Main-group elements','s-block','p-block','Transition elements','d-block','Inner-transition elements f-block'],
        'ur': ['مرکزی گروپ کے عناصر','s بلاک','p بلاک','عبوری عناصر','d بلاک','اندرونی عبوری عناصر، f بلاک'],
        'ps': ['د اصلي ګروپ عناصر','s بلاک','p بلاک','انتقالي عناصر','d بلاک','داخلي انتقالي عناصر، f بلاک'],
    }[language]
    w, h, left, top = 26, 27, 42, 92
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 570 380" role="img" aria-label="{html.escape(labels[0])}: s, p, d, f">',
             '<rect width="570" height="380" fill="white"/>']
    def text(x,y,value,size=12):
        parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="#111827">{html.escape(value)}</text>')
    def line(x1,y1,x2,y2,color='#1f2937'):
        parts.append(f'<path d="M{x1} {y1}H{x2}" fill="none" stroke="{color}"/>' if y1==y2 else f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}"/>')
    def arrow(x1,y,x2):
        line(x1,y,x2,y,'#c02664')
        direction=1 if x2>x1 else -1
        parts.append(f'<path d="M{x2-direction*4} {y-3}L{x2} {y}L{x2-direction*4} {y+3}" fill="none" stroke="#c02664"/>')
    text(276,19,labels[0],14)
    parts.append('<path d="M42 64V31H510V64 M42 72V64H94V72 M354 72V64H510V72" fill="none" stroke="#111827"/>')
    text(68,59,labels[1]); text(432,59,labels[2])
    text(224,110,labels[3]); text(224,126,labels[4])
    groups=['IA','IIA','IIIB','IVB','VB','VIB','VIIB','','VIIIB','','IB','IIB','IIIA','IVA','VA','VIA','VIIA','VIIIA']
    parts.append(f'<path d="M{left+7*w} {top+3*h-7}V{top+3*h-13}H{left+10*w}V{top+3*h-7}" fill="none" stroke="#111827"/>')
    for c,g in enumerate(groups):
        first=0 if c in (0,17) else 1 if c==1 or c>=12 else 3
        text(left+c*w+w/2,top+first*h-5,g,10)
        for r in range(first,6 if c>=12 else 7):
            fill='#fce7f3' if c>=12 else '#f8fafc'
            parts.append(f'<rect x="{left+c*w}" y="{top+r*h}" width="{w}" height="{h}" fill="{fill}" stroke="#334155"/>')
    for r in range(7):
        text(24,top+r*h+18,str(r+1))
        y=top+r*h+14
        arrow(left+2,y,left+2*w-2 if r else left+w-2)
        arrow(left+2*w-2 if r else left+w-2,y,left+2)
        text(left+w/2,y-3,f'{r+1}s',10)
        if 0<r<6:
            arrow(left+12*w+2,y,left+18*w-2)
            arrow(left+18*w-2,y,left+12*w+2)
            text(left+15*w,y-3,f'{r+1}p',10)
        if r>=3:
            arrow(left+2*w+2,y,left+12*w-2)
            arrow(left+12*w-2,y,left+2*w+2)
            text(left+7*w,y-3,f'{r}d',10)
    text(left+17*w+w/2,top+12,'1s',10)
    arrow(left+17*w+2,top+14,left+18*w-2)
    arrow(left+18*w-2,top+14,left+17*w+2)
    for r in range(2):
        y=310+r*h
        for c in range(14):
            parts.append(f'<rect x="{146+c*w}" y="{y}" width="{w}" height="{h}" fill="#fef9c3" stroke="#334155"/>')
        arrow(148,y+14,508); arrow(508,y+14,148)
        text(328,y+11,f'{r+4}f',11)
    for row, label in enumerate({'en':['Inner-transition','elements f-block'], 'ur':['اندرونی عبوری عناصر','f بلاک'], 'ps':['داخلي انتقالي عناصر','f بلاک']}[language]):
        text(78,321+row*13,label,10)
    parts.append('<path d="M137 307H132V366H137" fill="none" stroke="#111827"/>')
    parts.append('</svg>')
    return ''.join(parts)

def section(identity,title,urtitle,pstitle,paragraphs,layout,blocks,printed):
    return {'id':identity,'title':title,'headingUrdu':urtitle,'headingPashto':pstitle,
            'paras':paragraphs,'theory':'\n\n'.join(p['text'] for p in paragraphs),
            'urdu':'\n\n'.join(p['urdu'] for p in paragraphs),'pashto':'\n\n'.join(p['pashto'] for p in paragraphs),
            'theoryUrdu':'\n\n'.join(p['urdu'] for p in paragraphs),'theoryPashto':'\n\n'.join(p['pashto'] for p in paragraphs),
            'content':''.join('<p>'+html.escape(p['text'])+'</p>' for p in paragraphs),
            'translationStatus':'authored_aligned_paragraphs','sourceClass12Chemistry':True,'sourceLayout':layout,'sourceBlocks':blocks,
            'sourceReferences':[{'sourcePdf':SOURCE,'pdfPage':5,'printedPage':printed}],
            'sourceReviewStatus':'implemented_pending_final_comparison','rules':[],'sciNote':''}

intro = [
 pair('To easily understand the properties of the elements in the period table, the elements are placed in vertical columns and horizontal rows. The vertical columns are called groups or families and the horizontal rows are called the periods. The elements in the periodic table are divided into s, p, d and f blocks. Those elements in which last electrons occupy ‘s’ subshell (orbital) are called s-block elements. The s-block elements are at the extreme left of the periodic table and placed in Group IA (alkali metals) and Group IIA (alkaline earth metals) elements. Those elements in which last electrons occupy p subshell are called p-block elements. The p-block elements are placed in Groups IIIA, IVA, VA, VIA, VIIA and VIIIA.',
 'دوری جدول کے عناصر کی خصوصیات آسانی سے سمجھنے کے لیے عناصر کو عمودی کالموں اور افقی قطاروں میں رکھا جاتا ہے۔ عمودی کالم گروپ یا خاندان اور افقی قطاریں دور کہلاتی ہیں۔ دوری جدول کے عناصر کو s، p، d اور f بلاکوں میں تقسیم کیا جاتا ہے۔ جن عناصر کے آخری الیکٹران s ذیلی خول (آربیٹل) میں داخل ہوتے ہیں، انہیں s بلاک کے عناصر کہتے ہیں۔ یہ دوری جدول کے انتہائی بائیں جانب گروپ IA (الکلی دھاتوں) اور گروپ IIA (الکلائن ارتھ دھاتوں) میں ہوتے ہیں۔ جن عناصر کے آخری الیکٹران p ذیلی خول میں داخل ہوتے ہیں، انہیں p بلاک کے عناصر کہتے ہیں۔ یہ گروپ IIIA، IVA، VA، VIA، VIIA اور VIIIA میں ہوتے ہیں۔',
 'د دوراني جدول د عناصرو د ځانګړنو د اسانه پوهېدو لپاره عناصر په عمودي ستونونو او افقي کتارونو کې ځای پر ځای کېږي. عمودي ستونونه ګروپونه یا کورنۍ او افقي کتارونه دورې بلل کېږي. د دوراني جدول عناصر په s، p، d او f بلاکونو وېشل کېږي. هغه عناصر چې وروستي الکترونونه یې s فرعي پوښ (اوربیټال) ته ننوځي، د s بلاک عناصر بلل کېږي. دا د دوراني جدول په تر ټولو کیڼ اړخ کې په IA ګروپ (القلي فلزونو) او IIA ګروپ (القلي ځمکنیو فلزونو) کې دي. هغه عناصر چې وروستي الکترونونه یې p فرعي پوښ ته ننوځي، د p بلاک عناصر بلل کېږي. دا په IIIA، IVA، VA، VIA، VIIA او VIIIA ګروپونو کې دي.'),
 pair('Both s-block and p-block elements are normal elements. s-block elements consist of only metals but p-block elements include both metals and non-metals.',
 's بلاک اور p بلاک، دونوں کے عناصر عام عناصر ہیں۔ s بلاک کے عناصر صرف دھاتوں پر مشتمل ہیں، جبکہ p بلاک کے عناصر میں دھاتیں اور غیر دھاتیں دونوں شامل ہیں۔',
 'د s بلاک او p بلاک دواړو عناصر عادي عناصر دي. د s بلاک عناصر یوازې فلزونه دي، خو د p بلاک په عناصرو کې فلزونه او نافلزونه دواړه شامل دي.'),
 pair('Figure 13.1 Demarcation of the Periodic Table.','شکل 13.1 دوری جدول کی حد بندی۔','شکل 13.1 د دوراني جدول د برخو بېلول.'),
 pair('In previous grades, you have learnt about the periodic classification of elements in groups and periods. You have also learnt the basics about the 1ˢᵗ, 2ⁿᵈ period elements. In this unit, you will study more detail about the periodic trends and some properties of period 3ʳᵈ (Na to Ar), Groups IA, IIA, IVA and VIIA elements.',
 'پچھلی جماعتوں میں آپ عناصر کی گروپوں اور ادوار میں دوری درجہ بندی پڑھ چکے ہیں۔ آپ پہلے اور دوسرے دور کے عناصر کی بنیادی باتیں بھی پڑھ چکے ہیں۔ اس یونٹ میں آپ تیسرے دور (Na سے Ar تک) اور گروپ IA، IIA، IVA اور VIIA کے عناصر کے دوری رجحانات اور بعض خصوصیات مزید تفصیل سے پڑھیں گے۔',
 'په تېرو ټولګیو کې مو په ګروپونو او دورو کې د عناصرو دوراني ډلبندي زده کړې ده. د لومړۍ او دویمې دورې د عناصرو بنسټیز معلومات مو هم زده کړي دي. په دې واحد کې به د درېیمې دورې (له Na څخه تر Ar پورې) او د IA، IIA، IVA او VIIA ګروپونو د عناصرو دوراني تمایلات او ځینې ځانګړنې په لا ډېر تفصیل ولولئ.'),
]

period = [
 pair('13.1 Period 3 (Na To Ar)','13.1 تیسرا دور (Na سے Ar تک)','13.1 درېیمه دوره (له Na څخه تر Ar پورې)'),
 pair('Period 3 elements consists of sodium (Na), magnesium (Mg), aluminium (Al), silicon (Si), phosphorus (P), sulphur (S), chlorine (Cl) and argon (Ar). Sodium and magnesium are metals and belong to s-block. Aluminum (metal), silicon (metalloid), phosphorus, sulphur, chlorine and argon are non-metals and belong to p-block.',
 'تیسرے دور کے عناصر سوڈیم (Na)، میگنیشیم (Mg)، ایلومینیم (Al)، سلیکان (Si)، فاسفورس (P)، سلفر (S)، کلورین (Cl) اور آرگن (Ar) ہیں۔ سوڈیم اور میگنیشیم دھاتیں ہیں اور s بلاک سے تعلق رکھتے ہیں۔ ایلومینیم (دھات)، سلیکان (نیم دھات)، فاسفورس، سلفر، کلورین اور آرگن غیر دھاتیں ہیں اور p بلاک سے تعلق رکھتے ہیں۔',
 'د درېیمې دورې عناصر سوډیم (Na)، مګنیزیم (Mg)، المونیم (Al)، سیلیکان (Si)، فاسفورس (P)، سلفر (S)، کلورین (Cl) او ارګون (Ar) دي. سوډیم او مګنیزیم فلزونه دي او په s بلاک پورې اړه لري. المونیم (فلز)، سیلیکان (نیمه فلز)، فاسفورس، سلفر، کلورین او ارګون نافلزونه دي او په p بلاک پورې اړه لري.'),
 pair('13.1.1 Physical and Atomic Properties of the Elements','13.1.1 عناصر کی طبعی اور ایٹمی خصوصیات','13.1.1 د عناصرو فزیکي او اټومي ځانګړنې'),
 pair('The properties of the atoms of the elements are called atomic properties. On moving from left to right, in a period and from top to bottom, in a group of the periodic table, atomic properties show a regular variations. Hence, these properties, are also called periodic properties. Certain important periodic and physical properties of period 3 elements have been discussed in this unit.',
 'عناصر کے ایٹموں کی خصوصیات ایٹمی خصوصیات کہلاتی ہیں۔ دوری جدول کے کسی دور میں بائیں سے دائیں اور کسی گروپ میں اوپر سے نیچے جانے پر ایٹمی خصوصیات میں باقاعدہ تبدیلیاں ظاہر ہوتی ہیں۔ اس لیے یہ دوری خصوصیات بھی کہلاتی ہیں۔ اس یونٹ میں تیسرے دور کے عناصر کی بعض اہم دوری اور طبعی خصوصیات بیان کی گئی ہیں۔',
 'د عناصرو د اټومونو ځانګړنې اټومي ځانګړنې بلل کېږي. د دوراني جدول په یوه دوره کې له کیڼ څخه ښي لوري ته او په یوه ګروپ کې له پاس څخه ښکته تګ سره، اټومي ځانګړنې منظم بدلونونه ښيي. له همدې امله دا دوراني ځانګړنې هم بلل کېږي. په دې واحد کې د درېیمې دورې د عناصرو ځینې مهمې دوراني او فزیکي ځانګړنې بیان شوې دي.'),
 pair('13.1.1.1 Electronic Structure','13.1.1.1 الیکٹرانی ساخت','13.1.1.1 الکتروني جوړښت'),
 pair('In third period of the periodic table electrons are successively filled in 3s and 3p orbital of atoms of elements (Na to Ar). The electronic configurations of these elements are given below where [Ne] represents the electronic configuration of neon.',
 'دوری جدول کے تیسرے دور میں عناصر (Na سے Ar تک) کے ایٹموں کے 3s اور 3p آربیٹل میں الیکٹران یکے بعد دیگرے بھرتے ہیں۔ ان عناصر کی الیکٹرانی ترتیب نیچے دی گئی ہے، جہاں [Ne] نیون کی الیکٹرانی ترتیب ظاہر کرتا ہے۔',
 'د دوراني جدول په درېیمه دوره کې د عناصرو (له Na څخه تر Ar پورې) د اټومونو 3s او 3p اوربیټالونه په پرله پسې ډول له الکترونونو ډکېږي. د دې عناصرو الکتروني ترتیبونه لاندې ورکړل شوي دي؛ [Ne] د نیون الکتروني ترتیب ښيي.'),
 pair('Table 13.1 Elements, their Symbols and electronic configurations','جدول 13.1 عناصر، ان کی علامتیں اور الیکٹرانی ترتیبیں','جدول 13.1 عناصر، د هغوی سمبولونه او الکتروني ترتیبونه'),
 pair('13.1.1.2 Trend in Atomic Radius','13.1.1.2 ایٹمی رداس کا رجحان','13.1.1.2 د اټومي شعاع تمایل'),
 pair('The distance between the nucleus and the outermost shell of electrons of an atom or an ion is generally named as the atomic radius or ionic radius respectively. The exact position occupied by an electron cannot be defined with certainty. So the radius of an atom cannot be determined precisely. Thus, we deal with the radii of atoms linked together by some type of chemical bond.',
 'کسی ایٹم یا آئن کے مرکزے اور الیکٹرانوں کے سب سے بیرونی خول کے درمیان فاصلے کو عموماً بالترتیب ایٹمی رداس یا آئنک رداس کہتے ہیں۔ کسی الیکٹران کی درست جگہ یقینی طور پر متعین نہیں کی جا سکتی۔ اس لیے ایٹم کا رداس بالکل درست طور پر معلوم نہیں کیا جا سکتا۔ چنانچہ ہم ان ایٹموں کے رداس استعمال کرتے ہیں جو کسی قسم کے کیمیائی بند کے ذریعے ایک دوسرے سے جڑے ہوں۔',
 'د یوه اټوم یا ایون د هستې او د الکترونونو د تر ټولو بهرني پوښ ترمنځ واټن په عمومي ډول، په ترتیب سره، اټومي شعاع یا ایوني شعاع بلل کېږي. د الکترون دقیق موقعیت په یقین سره نه شي ټاکل کېدای. نو د اټوم شعاع په بشپړ دقت نه شي معلومېدای. له همدې امله د هغو اټومونو شعاعوې څېړو چې د یوه ډول کیمیاوي تړون په وسیله سره تړلي وي.'),
]
names = ['Sodium','Magnesium','Aluminium','Silicon','Phosphorus','Sulphur','Chlorine','Argon']
ur_names = ['سوڈیم','میگنیشیم','ایلومینیم','سلیکان','فاسفورس','سلفر','کلورین','آرگن']
ps_names = ['سوډیم','مګنیزیم','المونیم','سیلیکان','فاسفورس','سلفر','کلورین','ارګون']
symbols = ['₁₁Na','₁₂Mg','₁₃Al','₁₄Si','₁₅P','₁₆S','₁₇Cl','₁₈Ar']
configs = ['[Ne] 3s¹','[Ne]3s²','[Ne]3s²,3p¹','[Ne]3s²,3p²','[Ne]3s²,3p³','[Ne]3s²,3p⁴','[Ne]3s²,3p⁵','[Ne]3s²,3p⁶']
table = {'id':'chem12-table-13-1','headers':['Name of element','Symbol with atomic number','Electronic configuration'],
         'rows':[[n,s,c] for n,s,c in zip(names,symbols,configs)],
         'translations':[{'language':'اردو','headers':['عنصر کا نام','ایٹمی نمبر کے ساتھ علامت','الیکٹرانی ترتیب'],'rows':[[n,s,c] for n,s,c in zip(ur_names,symbols,configs)]},
                         {'language':'پښتو','headers':['د عنصر نوم','له اټومي شمېر سره سمبول','الکتروني ترتیب'],'rows':[[n,s,c] for n,s,c in zip(ps_names,symbols,configs)]}]}
sections = [
 section('chem12-u13-introduction','Introduction','تعارف','سریزه',intro,
         [{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual','blockId':'chem12-figure-13-1'},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]}],
         [{'id':'chem12-figure-13-1','svg':diagram('en'),'svgUrdu':diagram('ur'),'svgPashto':diagram('ps')}],2),
 section('chem12-u13-period3','13.1 Period 3 (Na To Ar)','13.1 تیسرا دور','13.1 درېیمه دوره',period,
         [{'type':'heading' if i in (0,2,4,7) else 'paragraph','indices':[i]} for i in range(7)]+[{'type':'sourceDataTable','tableId':table['id']},{'type':'heading','indices':[7]},{'type':'paragraph','indices':[8]}], [table],3),
]

outcomes = [
 pair('Recognize the demarcation of the periodic table into s – block, p – block, d – block and f–block.(Understanding)', 'دوری جدول کی s، p، d اور f بلاکوں میں حد بندی پہچانیں۔ (فہم)', 'په s، p، d او f بلاکونو کې د دوراني جدول وېش وپېژنئ. (پوهېدنه)'),
 pair('Describe how physical properties like atomic radius, ionization energy, electronegativity, electrical conductivity and melting and boiling points of elements change within a group and within a period in the Periodic Table. (Analysing)', 'بیان کریں کہ دوری جدول کے کسی گروپ اور دور میں عناصر کی طبعی خصوصیات، مثلاً ایٹمی رداس، آئنائزیشن توانائی، برقی منفیت، برقی موصلیت اور پگھلنے اور ابلنے کے درجے کیسے بدلتے ہیں۔ (تجزیہ)', 'بیان کړئ چې د دوراني جدول په یوه ګروپ او دوره کې د عناصرو فزیکي ځانګړنې، لکه اټومي شعاع، د ایون کېدو انرژي، برېښنا منفي توب، برېښنا لېږدونه او د وېلې کېدو او اېشېدو ټکي، څنګه بدلېږي. (شننه)'),
 pair('Describe reactions of period 3 elements with water, oxygen and chlorine. (Applying)', 'تیسرے دور کے عناصر کے پانی، آکسیجن اور کلورین کے ساتھ تعاملات بیان کریں۔ (اطلاق)', 'له اوبو، اکسیجن او کلورین سره د درېیمې دورې د عناصرو تعاملونه بیان کړئ. (کارونه)'),
 pair('Describe physical properties and acid – base behaviour of oxides, chlorides and hydroxides of period 3 elements. (Applying)', 'تیسرے دور کے عناصر کے آکسائیڈز، کلورائیڈز اور ہائیڈرو آکسائیڈز کی طبعی خصوصیات اور تیزابی و اساسی رویہ بیان کریں۔ (اطلاق)', 'د درېیمې دورې د عناصرو د اکسایډونو، کلورایډونو او هایدروکسایډونو فزیکي ځانګړنې او تېزابي او قلوي چلند بیان کړئ. (کارونه)'),
 pair('Describe reactions of oxides and chlorides of Period 3 elements with water. (Applying)', 'تیسرے دور کے عناصر کے آکسائیڈز اور کلورائیڈز کے پانی کے ساتھ تعاملات بیان کریں۔ (اطلاق)', 'له اوبو سره د درېیمې دورې د عناصرو د اکسایډونو او کلورایډونو تعاملونه بیان کړئ. (کارونه)'),
 pair('Explain the trends in physical properties and oxidation states in Groups I, II, IV and VII of the periodic table. (Analysing)', 'دوری جدول کے گروپ I، II، IV اور VII میں طبعی خصوصیات اور تکسیدی حالتوں کے رجحانات کی وضاحت کریں۔ (تجزیہ)', 'د دوراني جدول په I، II، IV او VII ګروپونو کې د فزیکي ځانګړنو او اکسیدېشن حالتونو تمایلات تشریح کړئ. (شننه)'),
 pair('Describe reactions of group I elements with water, oxygen and chlorine. (Applying)', 'گروپ I کے عناصر کے پانی، آکسیجن اور کلورین کے ساتھ تعاملات بیان کریں۔ (اطلاق)', 'له اوبو، اکسیجن او کلورین سره د I ګروپ د عناصرو تعاملونه بیان کړئ. (کارونه)'),
 pair('Explain effect of heat on nitrates, carbonates and hydrogen carbonates of Group I elements. (Applying)', 'گروپ I کے عناصر کے نائٹریٹس، کاربونیٹس اور ہائیڈروجن کاربونیٹس پر حرارت کے اثر کی وضاحت کریں۔ (اطلاق)', 'د I ګروپ د عناصرو پر نایټرېټونو، کاربونېټونو او هایدروجن کاربونېټونو د تودوخې اغېز تشریح کړئ. (کارونه)'),
 pair('Describe reactions of Group II elements with water, oxygen and nitrogen. (Applying)', 'گروپ II کے عناصر کے پانی، آکسیجن اور نائٹروجن کے ساتھ تعاملات بیان کریں۔ (اطلاق)', 'له اوبو، اکسیجن او نایتروجن سره د II ګروپ د عناصرو تعاملونه بیان کړئ. (کارونه)'),
 pair('Discuss the trend in solubility of the hydroxides, sulphates and carbonates of Group II elements. (Analysing)', 'گروپ II کے عناصر کے ہائیڈرو آکسائیڈز، سلفیٹس اور کاربونیٹس کی حل پذیری کے رجحان پر بحث کریں۔ (تجزیہ)', 'د II ګروپ د عناصرو د هایدروکسایډونو، سلفېټونو او کاربونېټونو د حل کېدو د وړتیا تمایل وڅېړئ. (شننه)'),
 pair('Discuss the trends in thermal stability of the nitrates and carbonates of Group II elements. (Analysing)', 'گروپ II کے عناصر کے نائٹریٹس اور کاربونیٹس کے حرارتی استحکام کے رجحانات پر بحث کریں۔ (تجزیہ)', 'د II ګروپ د عناصرو د نایټرېټونو او کاربونېټونو د حرارتي ثبات تمایلات وڅېړئ. (شننه)'),
 pair('Differentiate beryllium from other members of its group. (Analysing)', 'بیریلیم اور اس کے گروپ کے دوسرے ارکان میں فرق واضح کریں۔ (تجزیہ)', 'بېریلیم د خپل ګروپ له نورو غړو څخه توپیر کړئ. (شننه)'),
 pair('Describe reactions of Group IV elements with water. (Applying)', 'گروپ IV کے عناصر کے پانی کے ساتھ تعاملات بیان کریں۔ (اطلاق)', 'له اوبو سره د IV ګروپ د عناصرو تعاملونه بیان کړئ. (کارونه)'),
 pair('Discuss the chlorides and oxides of Group IV elements. (Applying)', 'گروپ IV کے عناصر کے کلورائیڈز اور آکسائیڈز پر بحث کریں۔ (اطلاق)', 'د IV ګروپ د عناصرو کلورایډونه او اکسایډونه وڅېړئ. (کارونه)'),
 pair('Explain the relative behaviour of halogens as oxidizing agents and reducing agents.(Applying)', 'تکسیدی اور اختزالی عوامل کے طور پر ہیلوجنوں کے نسبتی رویے کی وضاحت کریں۔ (اطلاق)', 'د اکسیدوونکو او ارجاع کوونکو عواملو په توګه د هالوجنونو نسبي چلند تشریح کړئ. (کارونه)'),
 pair('Compare the acidity of hydrogen halides. (Analysing)', 'ہائیڈروجن ہیلائیڈز کی تیزابیت کا موازنہ کریں۔ (تجزیہ)', 'د هایدروجن هالایډونو تېزابیت پرتله کړئ. (شننه)'),
 pair('Distinguish between an oxide and a peroxide. (Understanding)', 'آکسائیڈ اور پرآکسائیڈ میں فرق کریں۔ (فہم)', 'د اکسایډ او پراکسایډ ترمنځ توپیر وکړئ. (پوهېدنه)'),
 pair('Write representative equations for the formation of oxides and sulphides. (Applying)', 'آکسائیڈز اور سلفائیڈز کی تشکیل کی نمائندہ مساوات لکھیں۔ (اطلاق)', 'د اکسایډونو او سلفایډونو د جوړېدو استازې معادلې ولیکئ. (کارونه)'),
 pair('Compare the outermost s and p orbital system of an element with its chemical properties. (Analysing)', 'کسی عنصر کے سب سے بیرونی s اور p آربیٹل نظام کا اس کی کیمیائی خصوصیات سے موازنہ کریں۔ (تجزیہ)', 'د یوه عنصر د تر ټولو بهرنیو s او p اوربیټالونو سیستم د هغه له کیمیاوي ځانګړنو سره پرتله کړئ. (شننه)'),
]
opening_paras = [pair('Unit 13','یونٹ 13','واحد 13'),pair('s and p - Block Elements','s اور p بلاک کے عناصر','د s او p بلاک عناصر'),
                 pair('After studying this unit, students will be able to:', 'اس یونٹ کو پڑھنے کے بعد طلبہ اس قابل ہوں گے کہ:', 'د دې واحد تر لوستلو وروسته به زده کوونکي وکولای شي چې:')] + outcomes
opening_table={'id':'chem12-u13-teaching','headers':['Teaching','Assessment','Weightage %'],'rows':[['25','3','22']],
               'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['25','3','22']]},
                               {'language':'پښتو','headers':['تدریس','ارزونه','ونډه %'],'rows':[['25','3','22']]}]}
opening_section = section('13.1','Learning outcomes','حاصلاتِ تعلم','د زده کړې پایلې',opening_paras,
                          [{'type':'heading','indices':[0]},{'type':'heading','indices':[1]},{'type':'sourceDataTable','tableId':opening_table['id']},{'type':'paragraph','indices':[2]},{'type':'list','indices':list(range(3,len(opening_paras)))}], [opening_table],1)
opening_section['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':4,'printedPage':1}]
sections.insert(0,opening_section)

def main():
    # The printed statement labels aluminium/silicon and then calls the list non-metals.
    # Preserve it in every language; report the inconsistency outside source prose.
    audit={'sourcePdf':SOURCE,'pdfPages':[4,5],'printedPages':[1,2,3],'sections':sections,
           'issues':[{'id':'chem12-p3-element-classification','printedPage':3,'description':'The source labels aluminium a metal and silicon a metalloid, then calls the full p-block list non-metals. Printed wording is preserved; this is a source inconsistency.'}],
           'status':'implemented_pending_final_comparison'}
    marker='// BEGIN CLASS12 CHEMISTRY OPENING SOURCE REPAIR'
    end='// END CLASS12 CHEMISTRY OPENING SOURCE REPAIR'
    block=marker+'\n{ const correction = '+json.dumps(audit,ensure_ascii=False,indent=2)+''';
const chapter = CHEM_12_DATA.find(item => item.number === 13);
const continuation = chapter.sections.find(item => item.id === '13.2');
if (continuation && !continuation.sourceOpeningBoundaryRepaired) {
  const boundary = continuation.theory.indexOf('1. Covalent Radius');
  if (boundary < 0) throw new Error('Missing Chemistry XII covalent-radius boundary');
  continuation.theory = continuation.theory.slice(boundary);
  continuation.content = continuation.theory.replace(/\\n/g,'<br>');
  continuation.sciNote = ''; continuation.sourceOpeningBoundaryRepaired = true;
}
chapter.sections = chapter.sections.filter(item => !correction.sections.some(section => section.id === item.id));
chapter.sections.unshift(...correction.sections);
chapter.topics = chapter.sections.map(section => ({...(chapter.topics || []).find(item => item.id === section.id), ...section}));
chapter.sourceIssues = [...(chapter.sourceIssues || []).filter(issue => !correction.issues.some(item => item.id === issue.id)), ...correction.issues];
}
'''+end+'\n'
    lock=ROOT/'tmp/class-content-shared.lock'
    fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    try:
        os.write(fd,f'class12-chemistry pid={os.getpid()}\n'.encode()); os.close(fd); fd=None
        target=ROOT/'js/chem_12_data.js'
        text=target.read_text(encoding='utf-8')
        if marker in text:
            start=text.index(marker); stop=text.index(end,start)+len(end)
            text=text[:start]+block+text[stop:]
        else: text=text.rstrip()+'\n\n'+block
        temp=target.with_name(target.name+'.chem12.tmp'); temp.write_text(text,encoding='utf-8'); os.replace(temp,target)
        app=ROOT/'js/app.js'; renderer=app.read_text(encoding='utf-8')
        old="subjKey === 'phys' && (t.sourceClass12Physics === true || t.id?.startsWith('phys12-')) && t.sourceLayout ? renderScienceSourceLayout"
        new="((subjKey === 'phys' && (t.sourceClass12Physics === true || t.id?.startsWith('phys12-'))) || (subjKey === 'chem' && t.sourceClass12Chemistry === true)) && t.sourceLayout ? renderScienceSourceLayout"
        if old in renderer:
            assert renderer.count(old)==1
            temp=app.with_name(app.name+'.chem12.tmp'); temp.write_text(renderer.replace(old,new),encoding='utf-8'); os.replace(temp,app)
        else: assert new in renderer
    finally:
        if fd is not None: os.close(fd)
        lock.unlink()
    (OUT/'chemistry-opening-repair.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    path=OUT/'chemistry-progress.json'; progress=json.loads(path.read_text(encoding='utf-8-sig'))
    progress.pop('userDirectedSwitchUtc',None)
    progress['userDirectedSwitchDate']='2026-10-11'
    progress['sourceInspectedThroughPdfPage']=80
    progress['nextSourceInspectionPdfPage']=81
    progress['nextImplementationPdfPage']=progress.get('nextSequentialImplementationPdfPage',4)
    progress['verifiedUnchangedPdfPages']=[n for n in progress.get('verifiedUnchangedPdfPages',[]) if n not in (1,4)]
    progress['lastContiguousResolvedPdfPage']=0
    progress['unresolvedPdfPages']=sorted(set(progress['unresolvedPdfPages']+[1,4]))
    progress['nextPdfPageMeaning']='Next source inspection; implementation and verification tracked separately.'
    for page in progress['pages']:
        number=page.get('pdfPage',page.get('page'))
        if number in (1,3,4) and number not in progress.get('implementationSavedPdfPages',[]): page['status']='inspected_unresolved'
        if number==4: page['evidence']='Unit 13 starts printed page 1. Unit heading, teaching/assessment/weightage table and all 19 learning outcomes are implemented with aligned translations. Contents are implemented separately; final whole-spread comparison pending.'
        if number==5:
            page['status']='implemented_pending_final_comparison'
            page['evidence']='Printed pages 2–3 replaced with aligned English/Urdu/Pashto paragraphs, coded Figure 13.1 and complete Table 13.1. Legacy duplicate fragments removed at source boundaries. Final source/code comparison pending.'
        if number==27: page['evidence']='Unit 14 cover begins printed page 46; introduction is printed page 47. Inspected; implementation and translations pending.'
    progress['pendingTasks']=[f"Continue sequential Chemistry implementation at PDF page {progress.get('nextSequentialImplementationPdfPage',6)}.",'Complete final source/code comparison of saved repairs; keep source inconsistencies flagged.','PDF pages 81–85 are rendered/OCR cached but uninspected; next source inspection is 81.']
    progress['lastSavedUtc']=datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Chemistry PDF page 5 source repair saved; verification remains pending.')

if __name__=='__main__': main()
