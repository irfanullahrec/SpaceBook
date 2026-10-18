out = ['@printed 124', '@deco Cartoon book mascot on "Exercise 1"; yellow answer boxes under each angle figure.',
       'exercise 1',
       'q 1 | Draw a right angle using cardboard and compare it with the given angles to accurately indicate the types of angles. || گتے سے ایک قائمہ زاویہ بنائیں اور اسے دیے گئے زاویوں سے ملا کر زاویوں کی اقسام درست طور پر بتائیں۔ || له کارتن څخه یوه قایمه زاویه جوړه کړئ او له ورکړل شوو زاويو سره یې پرتله کړئ څو د زاويو ډولونه په سمه توګه وښیئ.']
figs = [('a', 'rays=0,90 | right=0:90 | len=80', 'Right angle (90°)', 'قائمہ زاویہ (90°)', 'قایمه زاویه (90°)', 'The arms meet exactly like the corner of the cardboard right angle.', 'بازو گتے کے قائمہ زاویے کے کونے کی طرح بالکل ملتے ہیں۔', 'بازوګان د کارتن د قایمې زاویې د کونج په څېر سم سره یو ځای کېږي.'),
        ('b', 'rays=0,240 | arc=0:240:18: | len=80', 'Reflex angle (more than 180°)', 'منعکس زاویہ (180° سے زیادہ)', 'انعکاسي زاویه (له 180° څخه زیاته)', 'The marked turn goes past a straight line, so it is greater than 180°.', 'نشان زدہ گھماؤ سیدھی لکیر سے آگے جاتا ہے، اس لیے یہ 180° سے بڑا ہے۔', 'په نښه شوې څرخه له مستقیمې کرښې تېرېږي، نو له 180° څخه لویه ده.'),
        ('c', 'rays=0,180 | arc=0:180:16: | len=80', 'Straight angle (180°)', 'سیدھا زاویہ (180°)', 'مستقیمه زاویه (180°)', 'The two arms lie on one straight line; it equals two right angles.', 'دونوں بازو ایک سیدھی لکیر پر ہیں؛ یہ دو قائمہ زاویوں کے برابر ہے۔', 'دواړه بازوګان پر یوه مستقیمه کرښه دي؛ دا له دوو قایمو زاويو سره برابره ده.'),
        ('d', 'rays=0,63 | arc=0:63:18: | len=80', 'Acute angle (less than 90°)', 'حادہ زاویہ (90° سے کم)', 'حاده زاویه (له 90° څخه کمه)', 'The opening is smaller than the cardboard right angle.', 'کھلاؤ گتے کے قائمہ زاویے سے چھوٹا ہے۔', 'پرانیستوالی د کارتن له قایمې زاویې څخه کوچنی دی.'),
        ('e', 'rays=0,125 | arc=0:125:18: | len=80', 'Obtuse angle (between 90° and 180°)', 'منفرجہ زاویہ (90° اور 180° کے درمیان)', 'منفرجه زاویه (د 90° او 180° ترمنځ)', 'The opening is wider than a right angle but less than a straight line.', 'کھلاؤ قائمہ زاویے سے زیادہ لیکن سیدھی لکیر سے کم ہے۔', 'پرانیستوالی له قایمې زاویې څخه پراخ خو له مستقیمې کرښې کم دی.')]
for l, spec, en, ur, ps, why, wur, wps in figs:
    out.append(f'angle {spec} || Angle {l}) || زاویہ {l}) || زاویه {l})')
    out.append(f'qp {l} | Figure {l}) || شکل {l}) || شکل {l})')
    out.append(f'sol {en} ## {why} || {ur}: {wur} || {ps}: {wps}')
out.append('@issue The exact sizes of the printed angles in Q1 are not given; d) and e) are drawn at about 63° and 125° to match the picture.')
out.append('q 2 | Use the protractor to draw the given angles. || زاویہ پیما کی مدد سے دیے گئے زاویے بنائیں۔ || د زاویه پیما په مرسته ورکړل شوې زاويې رسم کړئ.')
for l, d in zip('abcdefgh', [35, 45, 240, 180, 90, 60, 300, 155]):
    out.append(f'qp {l} | {d}°')
    if d > 180:
        rest = 360 - d
        out.append(f'angle rays=0,{d} | arc=0:{d}:22:{d}° | len=90')
        out.append(f'sol Construction (reflex angle) ## {d}° is a reflex angle: draw 360° − {d}° = {rest}° below the ray with the protractor turned upside down; the outside angle is {d}°. || {d}° منعکس زاویہ ہے: الٹے زاویہ پیما سے شعاع کے نیچے 360° − {d}° = {rest}° بنائیں؛ باہر والا زاویہ {d}° ہے۔ || {d}° انعکاسي زاویه ده: د سرچپه زاویه پیما په مرسته د وړانګې لاندې 360° − {d}° = {rest}° رسم کړئ؛ بهرنۍ زاویه {d}° ده.')
    else:
        out.append(f'angle rays=0,{d} | arc=0:{d}:22:{d}° | len=90')
        out.append(f'sol Construction ## Put the protractor centre on the vertex with the baseline on the ray, mark {d}° and join it to the vertex. || زاویہ پیما کا مرکز راس پر اور بنیادی لکیر شعاع پر رکھیں، {d}° پر نشان لگائیں اور اسے راس سے ملائیں۔ || د زاویه پیما مرکز پر راس او اساسي کرښه پر وړانګه کېږدئ، په {d}° کې نښه کېږدئ او له راس سره یې ونښلوئ.')
out += [
    'q 3 | Identify adjacent angles from the given angles. || دیے گئے زاویوں میں سے متصل زاویے پہچانیں۔ || له ورکړل شوو زاويو څخه نږدې زاويې وپېژنئ.',
    'angle rays=45,135,225,315 | pts= | len=90 || Two crossing lines forming angles 1 (top), 2 (right), 3 (bottom) and 4 (left) || دو کٹتی لکیریں جو زاویے 1 (اوپر)، 2 (دائیں)، 3 (نیچے) اور 4 (بائیں) بناتی ہیں || دوه سره پرې کېدونکې کرښې چې زاويې 1 (پورته)، 2 (ښي)، 3 (ښکته) او 4 (کیڼ) جوړوي',
    'sol ∠1 and ∠2, ∠2 and ∠3, ∠3 and ∠4, ∠4 and ∠1 ## Neighbouring angles share an arm and the vertex; ∠1 and ∠3 (or ∠2 and ∠4) are opposite, not adjacent. || پڑوسی زاویوں کا ایک بازو اور راس مشترک ہے؛ ∠1 اور ∠3 (یا ∠2 اور ∠4) آمنے سامنے ہیں، متصل نہیں۔ || ګاونډۍ زاويې یو بازو او راس ګډ لري؛ ∠1 او ∠3 (یا ∠2 او ∠4) مخامخ دي، نږدې نه دي.',
    'q 4 | Find the supplement of the following. || درج ذیل کا مکمل زاویہ معلوم کریں۔ || د لاندې زاويو مکمله زاویه معلومه کړئ.']
for l, d in zip('abcdefg', [98, 180, 115, 3, 78, 135, 90]):
    out.append(f'qp {l} | {d}°')
    out.append(f'sol {180 - d}° ## 180° − {d}° = {180 - d}°. || 180° − {d}° = {180 - d}°۔ || 180° − {d}° = {180 - d}°.')
out.append('q 5 | Find the complement of the following. || درج ذیل کا متمم زاویہ معلوم کریں۔ || د لاندې زاويو متممه زاویه معلومه کړئ.')
for l, d in zip('abcdefg', [12, 88, 90, 10, 62, 40, 70]):
    out.append(f'qp {l} | {d}°')
    out.append(f'sol {90 - d}° ## 90° − {d}° = {90 - d}°. || 90° − {d}° = {90 - d}°۔ || 90° − {d}° = {90 - d}°.')
out.append('@issue Q4 b) asks for the supplement of 180° (answer 0°) and Q5 c) for the complement of 90° (answer 0°); answered by the definition.')
out.append('endexercise')
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p131.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
