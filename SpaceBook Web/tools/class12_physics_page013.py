from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_field_figures import arrow
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
FLUX=[
 ('Consequently maximum electric lines will pass through the surface.','نتیجتاً سطح سے زیادہ سے زیادہ برقی خطوط گزریں گے۔','په پایله کې به له سطحې څخه تر ټولو زیاتې برېښنايي کرښې تېرې شي.'),
 (r'The electric flux is \(\Phi_E=EA\cos0=EA\)',r'برقی بہاؤ \(\Phi_E=EA\cos0=EA\) ہے۔',r'برېښنايي فلکس \(\Phi_E=EA\cos0=EA\) دی.'),
 ('Therefore large number of lines passes through the area.','اس لیے رقبے سے بڑی تعداد میں خطوط گزرتے ہیں۔','له همدې امله د مساحت له لارې ډېرې کرښې تېرېږي.'),
 ('ZERO FLUX:','صفر بہاؤ:','صفر فلکس:'),
 (r'if the surface is placed parallel to the electric field such that surface area \(\vec A\) is normal to electric field \(\vec E\) then no electric lines of force will pass through the surface as shown in Figure 11.11d. Consequently no electric flux will pass through the surface.',r'اگر سطح کو برقی میدان کے متوازی رکھا جائے، اس طرح کہ سطح کے رقبے کا سمتیہ \(\vec A\)، برقی میدان \(\vec E\) کے عمود پر ہو، تو سطح سے کوئی برقی خطِ قوت نہیں گزرے گا، جیسا کہ شکل 11.11d میں ہے۔ نتیجتاً سطح سے کوئی برقی بہاؤ نہیں گزرے گا۔',r'که سطحه د برېښنايي میدان سره موازي داسې کېښودل شي چې د سطحې د مساحت ویکټور \(\vec A\) د برېښنايي میدان \(\vec E\) په عمود کې وي، نو له سطحې څخه به د برېښنايي قوې هېڅ کرښه تېره نه شي، لکه په شکل 11.11d کې. په پایله کې به له سطحې څخه هېڅ برېښنايي فلکس تېر نه شي.'),
 (r'Then flux is \(\Phi_E=EA\cos90=0\)',r'تب بہاؤ \(\Phi_E=EA\cos90=0\) ہے۔',r'بیا فلکس \(\Phi_E=EA\cos90=0\) دی.'),
 ('ELECTRIC FLUX THROUGH CLOSE SURFACE','بند سطح سے برقی بہاؤ','د تړلې سطحې له لارې برېښنايي فلکس'),
 (r'If the case is such that either field is non-uniform or the surface is curved, then we divide the surfaces into very small patches of area \(\Delta A\) called differential area and assume that these are approximately flat and they are so small that electric field \(\vec E\) is almost uniform over it. For one of these small patches of area as shown in Fig.11.12 . The electric flux is defined by the relation. (Differential form),',r'اگر میدان غیر یکساں ہو یا سطح خمیدہ ہو، تو ہم سطحوں کو رقبے \(\Delta A\) کے بہت چھوٹے حصوں میں تقسیم کرتے ہیں جنہیں تفاضلی رقبہ کہتے ہیں۔ فرض کرتے ہیں کہ یہ تقریباً ہموار ہیں اور اتنے چھوٹے ہیں کہ ان پر برقی میدان \(\vec E\) تقریباً یکساں ہے۔ شکل 11.12 میں دکھائے گئے ایسے چھوٹے حصے کے لیے برقی بہاؤ اس تعلق سے بیان کیا جاتا ہے (تفاضلی صورت):',r'که میدان نایوشان وي یا سطحه کږه وي، نو سطحې د \(\Delta A\) مساحت په ډېرو کوچنیو ټوټو وېشو چې تفاضلي مساحت بلل کېږي. فرض کوو چې دا تقریباً هوارې او دومره کوچنۍ دي چې برېښنايي میدان \(\vec E\) پرې نږدې یوشان دی. په شکل 11.12 کې ښودل شوې یوې داسې کوچنۍ ټوټې لپاره برېښنايي فلکس په دې اړیکه تعریفېږي (تفاضلي بڼه):'),
 (r'\(\Phi_E=\vec E\cdot\Delta\vec A\)',)*3,
 ('To calculate total flux through the whole surface we add flux from each patch such that','پوری سطح سے کل بہاؤ معلوم کرنے کے لیے ہر حصے کے بہاؤ کو جمع کرتے ہیں، اس طرح کہ','د ټولې سطحې له لارې د ټول فلکس د محاسبې لپاره د هرې ټوټې فلکس جمع کوو، داسې چې'),
 (r'\(\Phi_E=\sum\vec E\cdot\Delta\vec A\)',)*3,
]
NOTE=[
 ('DO YOU KNOW?','کیا آپ جانتے ہیں؟','ایا پوهېږئ؟'),
 ('In case of closed surface the electric flux may be positive negative or zero depending upon the number of lines entering or leaving the surface:','بند سطح کی صورت میں برقی بہاؤ مثبت، منفی یا صفر ہو سکتا ہے، جس کا انحصار سطح میں داخل ہونے والے یا اس سے نکلنے والے خطوط کی تعداد پر ہے:','د تړلې سطحې په حالت کې برېښنايي فلکس مثبت، منفي یا صفر کېدای شي؛ دا د هغو کرښو په شمېر پورې اړه لري چې سطحې ته ننوځي یا ترې وځي:'),
 ('(i) The electric flux is zero if numbers of field lines entering are equal to field line leaving the surface or no field line intercepting the surface as shown in fig (a).','(i) برقی بہاؤ صفر ہے اگر داخل ہونے والے خطوطِ میدان کی تعداد سطح سے نکلنے والے خطوط کے برابر ہو، یا کوئی خطِ میدان سطح کو قطع نہ کرے، جیسا کہ شکل (a) میں ہے۔','(i) برېښنايي فلکس صفر دی که د ننوتونکو میدان کرښو شمېر له سطحې څخه د وتونکو کرښو سره برابر وي، یا هېڅ د میدان کرښه سطحه پرې نه کړي، لکه په شکل (a) کې.'),
 ('(ii) The electric flux is negative if net numbers of electric field lines are entering the closed surface or more field lines are entering than leaving the surface as shown in fig (b).','(ii) برقی بہاؤ منفی ہے اگر برقی خطوطِ میدان کی خالص تعداد بند سطح میں داخل ہو رہی ہو، یا نکلنے والے خطوط سے زیادہ خطوط داخل ہو رہے ہوں، جیسا کہ شکل (b) میں ہے۔','(ii) برېښنايي فلکس منفي دی که د برېښنايي میدان د کرښو خالص شمېر تړلې سطحې ته ننوځي، یا د وتونکو کرښو په پرتله ډېرې کرښې ننوځي، لکه په شکل (b) کې.'),
 ('(iii) The electric flux is positive if net numbers of electric field lines are leaving the surface as shown in fig (c).','(iii) برقی بہاؤ مثبت ہے اگر برقی خطوطِ میدان کی خالص تعداد سطح سے نکل رہی ہو، جیسا کہ شکل (c) میں ہے۔','(iii) برېښنايي فلکس مثبت دی که د برېښنايي میدان د کرښو خالص شمېر له سطحې څخه وځي، لکه په شکل (c) کې.'),
]
GAUSS=[
 ("The electric field of a given charge distribution can be calculated using Coulomb's law. But sometimes the actual calculations can become quite complicated.",'بار کی دی گئی تقسیم کا برقی میدان کولومب کے قانون سے معلوم کیا جا سکتا ہے۔ لیکن کبھی اصل حسابات کافی پیچیدہ ہو سکتے ہیں۔','د چارج د ټاکلي وېش برېښنايي میدان د کولمب د قانون په کارولو محاسبه کېدای شي. خو کله ناکله اصلي محاسبې ډېرې پېچلې کېدای شي.'),
 ("An alternative method to calculate the electric field of a given charge distribution relies on a theorem called Gauss' law. Gauss’ law provides a",'بار کی دی گئی تقسیم کا برقی میدان معلوم کرنے کا ایک متبادل طریقہ گاؤس کے قانون نامی قضیے پر مبنی ہے۔ گاؤس کا قانون ایک','د چارج د ټاکلي وېش د برېښنايي میدان د محاسبې یو بدیل میتود د ګاوس قانون په نوم پر یوې قضیې ولاړ دی. د ګاوس قانون یو'),
]

def svg(body,w,h,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" style="width:100%;max-width:{w}px">{body}</svg>'

def zero(lang):
    body='<path d="M45 115L105 50H320L260 115Z" fill="#e879a8" stroke="#334155"/>'
    for y in [66,81,96,111]:
        body+=f'<path d="M40 {y}H350" stroke="#0284c7" stroke-width="2"/>'+arrow(350,y,1,0,'#0284c7')
    body+='<path d="M190 83V16" stroke="#b91c1c" stroke-width="3"/>'+arrow(190,16,0,-1,'#b91c1c',9)+'<path d="M190 68H204V83" fill="none" stroke="#334155"/><text x="161" y="28">A⃗</text><text x="331" y="132">E⃗</text>'
    caption={'en':'FIGURE 11.11 (d): Electric flux(zero flux)','ur':'شکل 11.11 (d): برقی بہاؤ (صفر بہاؤ)','ps':'شکل 11.11 (d): برېښنايي فلکس (صفر فلکس)'}[lang]
    return '<figure>'+svg(body,390,145,'Surface parallel to field, normal area vector perpendicular to field')+'<figcaption>'+caption+'</figcaption></figure>'

def closed(lang):
    body='<ellipse cx="125" cy="120" rx="78" ry="96" fill="#facc15" stroke="#334155" stroke-width="2"/>'
    for offset in [15,35,55]:
        body+=f'<ellipse cx="125" cy="120" rx="{offset}" ry="96" fill="none" stroke="#334155"/>'
    for y,rx,ry in [(44,48,12),(70,68,19),(101,77,22),(136,77,22),(170,66,18),(194,45,10)]:
        body+=f'<ellipse cx="125" cy="{y}" rx="{rx}" ry="{ry}" fill="none" stroke="#334155"/>'
    body+='<path d="M178 83L189 105 185 120 173 98Z" fill="#fb7185" stroke="#334155"/><path d="M179 86L256 47M184 119L279 124" stroke="#334155" stroke-dasharray="3 3"/><path d="M257 47L291 110 247 127 219 66Z" fill="#38bdf8" stroke="#334155"/><path d="M256 88L320 62" stroke="#334155" stroke-width="2"/>'+arrow(320,62,64,-26,'#334155')+'<text x="253" y="37">ΔA</text><text x="317" y="87">E⃗</text>'
    caption={'en':'FIGURE 11.12: Electric flux through a close surface','ur':'شکل 11.12: بند سطح سے برقی بہاؤ','ps':'شکل 11.12: د تړلې سطحې له لارې برېښنايي فلکس'}[lang]
    return '<figure>'+svg(body,350,230,'Curved closed surface divided into small patches and enlarged differential area')+'<figcaption>'+caption+'</figcaption></figure>'

def signs(lang):
    body=''
    for i in range(3):
        x=100+i*205
        body+=f'<circle cx="{x}" cy="100" r="72" fill="#7dd3fc" stroke="#0284c7"/><text x="{x-10}" y="197">({chr(97+i)})</text>'
        for y in [62,100,138]:
            if i<2:
                body+=f'<path d="M{x-95} {y}H{x-38}" stroke="#334155"/>'+arrow(x-38,y,1,0,'#334155')
            if i!=1:
                body+=f'<path d="M{x+38} {y}H{x+95}" stroke="#334155"/>'+arrow(x+95,y,1,0,'#334155')+f'<text x="{x+89}" y="{y-7}" font-size="11">E</text>'
        if i==1:
            body+=f'<path d="M{x+95} 100H{x+38}" stroke="#334155"/>'+arrow(x+38,100,-1,0,'#334155')
    caption={'en':'Positive, negative and zero flux through a close surface','ur':'بند سطح سے مثبت، منفی اور صفر بہاؤ','ps':'د تړلې سطحې له لارې مثبت، منفي او صفر فلکس'}[lang]
    return '<figure>'+svg(body,620,215,'Equal entering and leaving lines (a), net entering lines (b), net leaving lines (c)')+'<figcaption>'+caption+'</figcaption></figure>'

if __name__=='__main__':
    specs=[
      ('phys12-front-flux16','Electric flux (continued)',16,FLUX,[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'heading','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'visual','blockId':'zero'},{'type':'equation','indices':[5]},{'type':'heading','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'visual','blockId':'closed'},{'type':'equation','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'equation','indices':[10]}],('برقی بہاؤ (جاری)','برېښنايي فلکس (دوام)'),{'zero':zero,'closed':closed}),
      ('phys12-front-flux-signs17','DO YOU KNOW? — Closed-surface flux',17,NOTE,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual','blockId':'signs'},{'type':'orderedList','indices':[2,3,4]}],('کیا آپ جانتے ہیں؟ — بند سطح کا بہاؤ','ایا پوهېږئ؟ — د تړلې سطحې فلکس'),{'signs':signs}),
      ('phys12-front-gauss17','11.5 GAUSS’S LAW',17,GAUSS,[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]}],('11.5 گاؤس کا قانون','11.5 د ګاوس قانون'),{}),
    ]
    records=[];sections=[]
    for identity,title,page,pairs,layout,titles,visuals in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':13,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        revised['sourceBlocks']=[{'id':key,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')} for key,fn in visuals.items()]
        revised['content']+=''.join(fn('en') for fn in visuals.values())
        records.append(record);sections.append(revised)
    upsert(records,sections)
    sync_companions(trim_sections=[{'id':'11.6','startsAt':'relationship between the net electrical flux','title':'Gauss’s law (continued; source review starts at PDF page 14)'}])
    checkpoint(13,'corrected_verified',[r['id'] for r in records],
      'Original spread inspected visually at 2.5x. Maximum and zero-flux continuation, differential and summed surface flux, all closed-surface sign conditions, and Gauss-law introduction transcribed and paired in Urdu/Pashto. Close surface wording preserved. Final Gauss-law sentence stops at the source page break after a and will continue on PDF14. Figures 11.11d and 11.12 and sign-of-flux illustration replaced with native SVG. Covered legacy11.6 prefix trimmed while retaining unaudited PDF14 onward.',printed_pages=[16,17])
