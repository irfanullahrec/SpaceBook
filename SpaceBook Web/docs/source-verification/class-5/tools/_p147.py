out = ['@printed 140', '@deco Cartoon book mascot on "Exercise 4".', 'exercise 4',
       'q 1 | Circle the figures which have reflective symmetry. Also draw their line of symmetry. || ان اشکال پر دائرہ لگائیں جن میں انعکاسی تشاکل ہے۔ ان کا خطِ تشاکل بھی کھینچیں۔ || هغه شکلونه په کړۍ کې ونیسئ چې انعکاسي تناظر لري. د تناظر کرښه یې هم رسم کړئ.']
q1 = [('a', 'isotrap', 'v', 'Yes — 1 line of symmetry (vertical)', 'The two slanting sides lean out equally, so the left half folds onto the right half.', 'ہاں — 1 خطِ تشاکل (عمودی)؛ دونوں ترچھے اضلاع برابر باہر کو جھکے ہیں۔', 'هو — 1 د تناظر کرښه (عمودي)؛ دواړه اریبې ضلعې په برابره اندازه بهر ته کږې دي.'),
      ('b', 'pentagon', 'v', 'Yes — a regular pentagon has 5 lines of symmetry (one through each corner)', 'Each line runs from a corner to the middle of the opposite side; the vertical one is drawn.', 'ہاں — منتظم مخمس کے 5 خطِ تشاکل ہیں (ہر کونے سے مقابل ضلع کے وسط تک)؛ عمودی خط دکھایا گیا ہے۔', 'هو — منظم پنځه ضلعي 5 د تناظر کرښې لري (له هر کونج څخه د مخامخ ضلعې منځ ته)؛ عمودي کرښه ښودل شوې.'),
      ('c', 'irrpent', 'none', 'No reflective symmetry', 'All sides and corners are different, so no fold makes the two halves match.', 'کوئی انعکاسی تشاکل نہیں — تمام اضلاع اور کونے مختلف ہیں۔', 'انعکاسي تناظر نه لري — ټولې ضلعې او کونجونه بېل دي.'),
      ('d', 'arch', 'v', 'Yes — 1 line of symmetry (vertical)', 'The arch is a half circle; the vertical line through its top divides it into two equal halves.', 'ہاں — 1 خطِ تشاکل (عمودی)؛ نیم دائرے کو اوپر سے گزرنے والی عمودی لکیر دو برابر حصوں میں تقسیم کرتی ہے۔', 'هو — 1 د تناظر کرښه (عمودي)؛ نیمه دایره د سر څخه تېره عمودي کرښه په دوو برابرو برخو وېشي.'),
      ('e', 'isotri', 'v', 'Yes — 1 line of symmetry (vertical)', 'It is an isosceles triangle; the line from the top corner to the middle of the base is a line of symmetry.', 'ہاں — 1 خطِ تشاکل؛ یہ مساوی الساقین مثلث ہے۔', 'هو — 1 د تناظر کرښه؛ دا متساوي الساقین مثلث دی.'),
      ('f', 'H', 'both', 'Yes — 2 lines of symmetry (vertical and horizontal)', 'The letter H matches itself when folded left–right and top–bottom.', 'ہاں — 2 خطِ تشاکل (عمودی اور افقی)۔', 'هو — 2 د تناظر کرښې (عمودي او افقي).'),
      ('g', 'umbrella', 'v', 'Canopy: 1 vertical line of symmetry (the hooked handle is not symmetric)', 'The canopy and shaft are symmetric about the shaft; only the curved end of the handle breaks the symmetry.', 'چھتری کا اوپری حصہ ڈنڈی کے لحاظ سے متشاکل ہے؛ صرف دستے کا مڑا ہوا سرا تشاکل توڑتا ہے۔', 'د چترۍ پورتنۍ برخه د لښتې په اړه متناظره ده؛ یوازې د لاستي کږ سر تناظر ماتوي.'),
      ('h', 'A', 'v', 'Yes — 1 line of symmetry (vertical)', 'The letter A folds onto itself along the vertical line through its top.', 'ہاں — 1 خطِ تشاکل (عمودی)۔', 'هو — 1 د تناظر کرښه (عمودي).')]
for l, k, line, en, why, ur, ps in q1:
    out.append(f'shape {k} | line={line} || {l}) || {l}) || {l})')
    out.append(f'qp {l} | Figure {l}) || شکل {l}) || شکل {l})')
    out.append(f'sol {en} ## {why} || {ur} || {ps}')
out.append('@issue Ex 4 Q1 g) (umbrella): the canopy is symmetric but the J-shaped handle is not; the book\'s answer key should be checked for the intended answer.')
out.append('q 2 | Circle the figures having rotational symmetry. Also write the order of their rotation and mark their center of rotation. || گردشی تشاکل والی اشکال پر دائرہ لگائیں۔ ان کی گردش کا درجہ بھی لکھیں اور مرکزِ گردش پر نشان لگائیں۔ || د څرخیز تناظر لرونکي شکلونه په کړۍ کې ونیسئ. د څرخ درجه یې هم ولیکئ او د څرخ مرکز په نښه کړئ.')
q2 = [('a', 'I', 'Yes — order 2', 'Turned through 180° the letter I looks the same; it looks the same twice in a full turn.', 'ہاں — درجہ 2؛ 180° گھمانے پر حرف I ویسا ہی لگتا ہے۔', 'هو — درجه 2؛ په 180° څرخولو د I توری هماغسې ښکاري.'),
      ('b', 'pentagon', 'Yes — order 5', 'A regular pentagon looks the same after every turn of 72°, five times in a full turn.', 'ہاں — درجہ 5؛ منتظم مخمس ہر 72° پر ویسا ہی لگتا ہے۔', 'هو — درجه 5؛ منظم پنځه ضلعي په هره 72° څرخه هماغسې ښکاري.'),
      ('c', 'arrowR', 'No rotational symmetry', 'The arrow points a different way after any turn less than 360°.', 'کوئی گردشی تشاکل نہیں؛ 360° سے کم ہر گردش پر تیر کی سمت بدل جاتی ہے۔', 'څرخیز تناظر نه لري؛ له 360° کم په هره څرخه د غشي لوری بدلېږي.'),
      ('d', 'diamond', 'Yes — order 4', 'It is a square standing on a corner; it looks the same after every 90° turn.', 'ہاں — درجہ 4؛ یہ کونے پر کھڑا مربع ہے جو ہر 90° پر ویسا ہی لگتا ہے۔', 'هو — درجه 4؛ دا پر کونج ولاړ مربع دی چې په هره 90° څرخه هماغسې ښکاري.'),
      ('e', 'cross4', 'Yes — order 4', 'The four arrows are alike; every 90° turn gives the same picture.', 'ہاں — درجہ 4؛ چاروں تیر ایک جیسے ہیں۔', 'هو — درجه 4؛ څلور واړه غشي یو شان دي.'),
      ('f', 'trap', 'No rotational symmetry', 'The top side is shorter than the bottom, so it is upside down after a 180° turn.', 'کوئی گردشی تشاکل نہیں؛ اوپر والا ضلع نیچے والے سے چھوٹا ہے۔', 'څرخیز تناظر نه لري؛ پورتنۍ ضلع له لاندنۍ لنډه ده.'),
      ('g', 'star4', 'Yes — order 4', 'The four points are equal; it looks the same after every 90° turn.', 'ہاں — درجہ 4؛ چاروں نوکیں برابر ہیں۔', 'هو — درجه 4؛ څلور واړه څوکې برابرې دي.'),
      ('h', 'zshape', 'Yes — order 2', 'Like the letter Z, it looks the same after a half turn (180°).', 'ہاں — درجہ 2؛ حرف Z کی طرح آدھے چکر (180°) پر ویسا ہی لگتا ہے۔', 'هو — درجه 2؛ د Z توري په څېر په نیمه څرخه (180°) هماغسې ښکاري.')]
for l, k, en, why, ur, ps in q2:
    extra = ' | centre' if en.startswith('Yes') else ''
    out.append(f'shape {k}{extra} || {l}) || {l}) || {l})')
    out.append(f'qp {l} | Figure {l}) || شکل {l}) || شکل {l})')
    out.append(f'sol {en} ## {why} The red dot marks the centre of rotation. || {ur} || {ps}' if extra else f'sol {en} ## {why} || {ur} || {ps}')
out.append('endexercise')
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p147.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
