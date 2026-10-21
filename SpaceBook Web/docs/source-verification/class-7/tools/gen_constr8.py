"""gen_constr8.py - construction method steps (EN | UR | PS) for Class 8 Unit 10 (10.4, 10.5), with feasibility checks.
    python gen_constr8.py     -> class-8/math/dsl/constructions.txt   (every line marked not verified, ^^)
"""
import re, json, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import msol_run

HERE = Path(__file__).resolve().parents[2]
APP = HERE.parent.parent


def R(en, ur, ps):
    return f'{en}|{ur}|{ps}'


def nums(t):
    return [float(x) for x in re.findall(r'\d+\.?\d*', t.replace('∠', ' '))]


def g(v):
    return f'{v:g}'


def sss(a, b, c, names):
    s = sorted([a, b, c])
    ok = s[0] + s[1] > s[2]
    n1, n2, n3 = names
    if not ok:
        return [R(f'Check the triangle inequality: the two shorter sides {g(s[0])} + {g(s[1])} = {g(s[0] + s[1])} cm are not greater than the longest side {g(s[2])} cm.',
                  f'مثلث کی عدم مساوات دیکھیں: دو چھوٹے اضلاع {g(s[0])} + {g(s[1])} = {g(s[0] + s[1])} سینٹی میٹر سب سے بڑے ضلع {g(s[2])} سینٹی میٹر سے بڑے نہیں ہیں۔',
                  f'د درې ګوني نابرابري وګورئ: دوه لنډ ضلعې {g(s[0])} + {g(s[1])} = {g(s[0] + s[1])} سانتي متره له تر ټولو اوږد ضلع {g(s[2])} سانتي متره نه لويې دي.'),
                R('So the two arcs do not meet and the triangle cannot be drawn.', 'لہٰذا دونوں قوس نہیں ملتے اور مثلث نہیں بن سکتا۔', 'نو دواړه قوسونه نه سره رسېږي او درې ګوني نشي جوړېدلی.')], 'Not possible: sum of two sides is not greater than the third'
    base = max(a, b, c)
    return [R(f'Draw the longest side {g(base)} cm as the base.', f'سب سے لمبا ضلع {g(base)} سینٹی میٹر قاعدے کے طور پر کھینچیں۔', f'تر ټولو اوږد ضلع {g(base)} سانتي متره د قاعدې په توګه رسم کړئ.'),
            R(f'From one end draw an arc of radius {g(s[1])} cm and from the other end an arc of radius {g(s[0])} cm above the base.', f'ایک سرے سے {g(s[1])} سینٹی میٹر رداس کا اور دوسرے سرے سے {g(s[0])} سینٹی میٹر رداس کا قوس قاعدے کے اوپر لگائیں۔', f'له یوه سر څخه {g(s[1])} سانتي متره شعاع او له بل سر څخه {g(s[0])} سانتي متره شعاع قوس د قاعدې پورته وکاږئ.'),
            R('The arcs meet at the third vertex; join it to both ends.', 'قوس تیسرے راس پر ملتے ہیں؛ اسے دونوں سروں سے ملائیں۔', 'قوسونه په درېیم رأس کې سره رسېږي؛ هغه له دواړو سرونو سره ونښلوئ.')], 'Triangle constructed (SSS)'


def sas(a, ang, b):
    return [R(f'Draw one side of {g(a)} cm.', f'{g(a)} سینٹی میٹر کا ایک ضلع کھینچیں۔', f'{g(a)} سانتي متره یو ضلع رسم کړئ.'),
            R(f'At one end make an angle of {g(ang)}° with a protractor and draw a ray.', f'ایک سرے پر چاند سے {g(ang)}° کا زاویہ بنا کر شعاع کھینچیں۔', f'په یو سر کې د ګردې په مرسته {g(ang)}° زاویه جوړه کړئ او وړانګه وکاږئ.'),
            R(f'On the ray mark a point {g(b)} cm from the vertex.', f'شعاع پر راس سے {g(b)} سینٹی میٹر پر نشان لگائیں۔', f'پر وړانګه له رأس څخه {g(b)} سانتي متره نښه کېږدئ.'),
            R('Join the two free ends to complete the triangle.', 'دونوں آزاد سروں کو ملا کر مثلث مکمل کریں۔', 'دواړه آزاد سرونه سره ونښلوئ چې درې ګوني بشپړ شي.')], 'Triangle constructed (SAS)'


def asa(a, p, q):
    if p + q >= 180:
        return [R(f'The two angles {g(p)}° + {g(q)}° = {g(p + q)}° are not less than 180°.', f'دونوں زاویے {g(p)}° + {g(q)}° = {g(p + q)}° ہیں جو 180° سے کم نہیں۔', f'دواړه زاویې {g(p)}° + {g(q)}° = {g(p + q)}° دي چې له 180° کمې نه دي.'), R('So the rays never meet and the triangle cannot be drawn.', 'لہٰذا شعاعیں کبھی نہیں ملتیں اور مثلث نہیں بن سکتا۔', 'نو وړانګې هېڅکله نه سره رسېږي او درې ګوني نشي جوړېدلی.')], 'Not possible'
    return [R(f'Draw the given side of {g(a)} cm.', f'دیا گیا {g(a)} سینٹی میٹر کا ضلع کھینچیں۔', f'ورکړل شوی {g(a)} سانتي متره ضلع رسم کړئ.'),
            R(f'At one end make an angle of {g(p)}° and at the other end an angle of {g(q)}°, on the same side, drawing a ray for each.', f'ایک سرے پر {g(p)}° اور دوسرے سرے پر {g(q)}° کا زاویہ ایک ہی طرف بنا کر ہر ایک کی شعاع کھینچیں۔', f'په یو سر کې {g(p)}° او په بل سر کې {g(q)}° زاویه په یوه لور جوړه کړئ او د هرې وړانګه وکاږئ.'),
            R(f'The rays meet at the third vertex; the third angle is 180° − {g(p)}° − {g(q)}° = {g(180 - p - q)}°.', f'شعاعیں تیسرے راس پر ملتی ہیں؛ تیسرا زاویہ 180° − {g(p)}° − {g(q)}° = {g(180 - p - q)}° ہے۔', f'وړانګې په درېیم رأس کې سره رسېږي؛ درېیمه زاویه 180° − {g(p)}° − {g(q)}° = {g(180 - p - q)}° ده.')], 'Triangle constructed (ASA / AAS)'


def rhs(side, hyp):
    if side >= hyp:
        return [R(f'The hypotenuse {g(hyp)} cm must be longer than the other side {g(side)} cm.', f'وتر {g(hyp)} سینٹی میٹر دوسرے ضلع {g(side)} سینٹی میٹر سے لمبا ہونا چاہیے۔', f'وتر {g(hyp)} سانتي متره باید له نورې ضلع {g(side)} سانتي متره اوږد وي.'), R('So this triangle cannot be drawn.', 'لہٰذا یہ مثلث نہیں بن سکتا۔', 'نو دا درې ګوني نشي جوړېدلی.')], 'Not possible'
    o = math.sqrt(hyp * hyp - side * side)
    return [R(f'Draw the side of {g(side)} cm.', f'{g(side)} سینٹی میٹر کا ضلع کھینچیں۔', f'{g(side)} سانتي متره ضلع رسم کړئ.'),
            R('At one end draw a perpendicular (90°) line.', 'ایک سرے پر عمود (90°) کھینچیں۔', 'په یو سر کې عمود (90°) کرښه وکاږئ.'),
            R(f'With the compass opened to {g(hyp)} cm and centre at the other end, draw an arc that cuts the perpendicular.', f'پرکار {g(hyp)} سینٹی میٹر کھول کر دوسرے سرے کو مرکز بنا کر قوس لگائیں جو عمود کو کاٹے۔', f'د پرکار خوله {g(hyp)} سانتي متره کړئ او له بل سر څخه قوس وکاږئ چې عمود پرې کړي.'),
            R(f'Join to complete the triangle. The third side is √({g(hyp)}² − {g(side)}²) ≈ {o:.2f} cm.', f'ملا کر مثلث مکمل کریں۔ تیسرا ضلع √({g(hyp)}² − {g(side)}²) ≈ {o:.2f} سینٹی میٹر ہے۔', f'ونښلوئ چې درې ګوني بشپړ شي. درېیم ضلع √({g(hyp)}² − {g(side)}²) ≈ {o:.2f} سانتي متره دی.')], 'Right-angled triangle constructed'


def ssa(adj, opp, ang):
    """known: side adjacent to the angle (adj), side opposite the angle (opp), angle at the shared vertex of adj"""
    h = adj * math.sin(math.radians(ang))
    if opp < h - 1e-9:
        return [R(f'The side opposite the angle is {g(opp)} cm but the height needed is {g(adj)} × sin {g(ang)}° ≈ {h:.2f} cm, which is more.', f'زاویے کے سامنے ضلع {g(opp)} سینٹی میٹر ہے مگر درکار اونچائی {g(adj)} × sin {g(ang)}° ≈ {h:.2f} سینٹی میٹر ہے جو زیادہ ہے۔', f'د زاویې مخامخ ضلع {g(opp)} سانتي متره دی خو اړینه لوړوالی {g(adj)} × sin {g(ang)}° ≈ {h:.2f} سانتي متره دی چې ډېر دی.'), R('So the arc does not reach the ray: no triangle.', 'لہٰذا قوس شعاع تک نہیں پہنچتا: مثلث نہیں بنتا۔', 'نو قوس وړانګې ته نه رسېږي: درې ګوني نه جوړېږي.')], 'Not possible'
    note = 'two triangles are possible' if (opp < adj and ang < 90 and opp > h + 1e-9) else 'one triangle'
    return [R(f'Draw the side of {g(adj)} cm and at one end make the angle {g(ang)}°; draw the ray.', f'{g(adj)} سینٹی میٹر کا ضلع کھینچ کر ایک سرے پر {g(ang)}° کا زاویہ بنائیں اور شعاع کھینچیں۔', f'{g(adj)} سانتي متره ضلع رسم کړئ، په یو سر کې {g(ang)}° زاویه جوړه کړئ او وړانګه وکاږئ.'),
            R(f'With centre at the other end of the side and radius {g(opp)} cm, draw an arc that cuts the ray.', f'ضلع کے دوسرے سرے کو مرکز بنا کر {g(opp)} سینٹی میٹر رداس کا قوس لگائیں جو شعاع کو کاٹے۔', f'د ضلع له بل سر څخه د {g(opp)} سانتي متره شعاع قوس وکاږئ چې وړانګه پرې کړي.'),
            R(f'Join the cut point to the other end of the side ({note}).', f'کٹنے کے نقطے کو ضلع کے دوسرے سرے سے ملائیں ({note})۔', f'د پرې کېدو ټکی له ضلع بل سر سره ونښلوئ ({note}).')], 'Triangle constructed (SSA)'


def square_diag(d):
    s = d / math.sqrt(2)
    return [R(f'Draw the diagonal AC = {g(d)} cm and its perpendicular bisector (it passes through the midpoint O).', f'وتر AC = {g(d)} سینٹی میٹر کھینچ کر اس کا عمود ثنائی بنائیں (یہ وسطی نقطہ O سے گزرتا ہے)۔', f'وتر AC = {g(d)} سانتي متره رسم کړئ او د هغه عمود نیمګړی وکاږئ (دا له منځنۍ ټکي O تېرېږي).'),
            R(f'On the bisector mark B and D at {g(d / 2)} cm on each side of O (the diagonals of a square are equal and bisect at 90°).', f'عمود ثنائی پر O کے دونوں طرف {g(d / 2)} سینٹی میٹر پر B اور D لگائیں (مربع کے وتر برابر ہوتے ہیں اور 90° پر ایک دوسرے کو نصف کرتے ہیں)۔', f'پر عمود نیمګړي د O په دواړو خواوو {g(d / 2)} سانتي متره B او D کېږدئ (د مربع وترونه مساوي دي او په 90° سره یو بل نیمایي کوي).'),
            R(f'Join AB, BC, CD, DA. Check: each side ≈ {s:.2f} cm.', f'AB، BC، CD، DA ملائیں۔ جانچ: ہر ضلع ≈ {s:.2f} سینٹی میٹر۔', f'AB، BC، CD، DA ونښلوئ. ازموینه: هر ضلع ≈ {s:.2f} سانتي متره.')], f'Square with side ≈ {s:.2f} cm constructed'


def rect_ab_bc(a, b):
    return [R(f'Draw AB = {g(a)} cm.', f'AB = {g(a)} سینٹی میٹر کھینچیں۔', f'AB = {g(a)} سانتي متره رسم کړئ.'),
            R(f'At B draw a perpendicular and mark C with BC = {g(b)} cm.', f'B پر عمود کھینچ کر C اس طرح لگائیں کہ BC = {g(b)} سینٹی میٹر ہو۔', f'په B کې عمود وکاږئ او C داسې کېږدئ چې BC = {g(b)} سانتي متره وي.'),
            R(f'With centre A and radius {g(b)} cm and with centre C and radius {g(a)} cm draw arcs that meet at D.', f'مرکز A اور رداس {g(b)} سینٹی میٹر، اور مرکز C اور رداس {g(a)} سینٹی میٹر سے قوس لگائیں جو D پر ملیں۔', f'له A مرکز او {g(b)} سانتي متره شعاع، او له C مرکز او {g(a)} سانتي متره شعاع قوسونه وکاږئ چې په D کې سره ورسېږي.'),
            R('Join AD and CD: ABCD is the rectangle.', 'AD اور CD ملائیں: ABCD مستطیل ہے۔', 'AD او CD ونښلوئ: ABCD مستطیل دی.')], 'Rectangle constructed'


def rect_ab_diag(a, d):
    if d <= a:
        return [R(f'The diagonal {g(d)} cm must be longer than the side {g(a)} cm.', f'وتر {g(d)} سینٹی میٹر ضلع {g(a)} سینٹی میٹر سے لمبا ہونا چاہیے۔', f'وتر {g(d)} سانتي متره باید له ضلع {g(a)} سانتي متره اوږد وي.'), R('So this rectangle cannot be constructed.', 'لہٰذا یہ مستطیل نہیں بن سکتا۔', 'نو دا مستطیل نشي جوړېدلی.')], 'Not possible'
    b = math.sqrt(d * d - a * a)
    return [R(f'Draw AB = {g(a)} cm and a perpendicular at B.', f'AB = {g(a)} سینٹی میٹر اور B پر عمود کھینچیں۔', f'AB = {g(a)} سانتي متره او په B کې عمود وکاږئ.'),
            R(f'With centre A and radius {g(d)} cm (the diagonal) draw an arc cutting the perpendicular at C; BC ≈ {b:.2f} cm.', f'مرکز A اور رداس {g(d)} سینٹی میٹر (وتر) سے قوس لگائیں جو عمود کو C پر کاٹے؛ BC ≈ {b:.2f} سینٹی میٹر۔', f'له A مرکز او {g(d)} سانتي متره (وتر) شعاع قوس وکاږئ چې عمود په C کې پرې کړي؛ BC ≈ {b:.2f} سانتي متره.'),
            R(f'Complete the rectangle: arcs from A (radius {b:.2f}) and from C (radius {g(a)}) meet at D; join AD and CD.', f'مستطیل مکمل کریں: A سے ({b:.2f} رداس) اور C سے ({g(a)} رداس) قوس D پر ملتے ہیں؛ AD اور CD ملائیں۔', f'مستطیل بشپړ کړئ: له A ({b:.2f} شعاع) او له C ({g(a)} شعاع) قوسونه په D کې سره رسېږي؛ AD او CD ونښلوئ.')], 'Rectangle constructed'


def rhombus_angle(a, ang):
    return [R(f'Draw AB = {g(a)} cm.', f'AB = {g(a)} سینٹی میٹر کھینچیں۔', f'AB = {g(a)} سانتي متره رسم کړئ.'),
            R(f'At the vertex make the angle {g(ang)}° and mark the next vertex {g(a)} cm along the ray (all four sides of a rhombus are equal).', f'راس پر {g(ang)}° کا زاویہ بنا کر شعاع پر {g(a)} سینٹی میٹر پر اگلا راس لگائیں (معین کے چاروں اضلاع برابر ہوتے ہیں)۔', f'په رأس کې {g(ang)}° زاویه جوړه کړئ او پر وړانګه {g(a)} سانتي متره لرې بل رأس کېږدئ (د معین څلور ضلعې مساوي دي).'),
            R(f'From the two free ends draw arcs of radius {g(a)} cm; they meet at the fourth vertex.', f'دونوں آزاد سروں سے {g(a)} سینٹی میٹر رداس کے قوس لگائیں؛ وہ چوتھے راس پر ملتے ہیں۔', f'له دواړو آزادو سرونو {g(a)} سانتي متره شعاع قوسونه وکاږئ؛ دا په څلورم رأس کې سره رسېږي.'),
            R('Join to complete the rhombus.', 'ملا کر معین مکمل کریں۔', 'ونښلوئ چې معین بشپړ شي.')], 'Rhombus constructed'


def rhombus_diag(a, d):
    if d >= 2 * a:
        return [R(f'A diagonal of {g(d)} cm must be shorter than twice the side ({g(2 * a)} cm).', f'وتر {g(d)} سینٹی میٹر ضلع کے دگنے ({g(2 * a)} سینٹی میٹر) سے چھوٹا ہونا چاہیے۔', f'وتر {g(d)} سانتي متره باید د ضلع له دوه چنده ({g(2 * a)} سانتي متره) کم وي.'), R('So this rhombus cannot be constructed.', 'لہٰذا یہ معین نہیں بن سکتا۔', 'نو دا معین نشي جوړېدلی.')], 'Not possible'
    return [R(f'Draw the diagonal of {g(d)} cm.', f'{g(d)} سینٹی میٹر کا وتر کھینچیں۔', f'{g(d)} سانتي متره وتر رسم کړئ.'),
            R(f'With radius {g(a)} cm (the side) and each end of the diagonal as centre, draw arcs above and below the diagonal.', f'{g(a)} سینٹی میٹر (ضلع) رداس سے وتر کے ہر سرے کو مرکز بنا کر وتر کے اوپر اور نیچے قوس لگائیں۔', f'د {g(a)} سانتي متره (ضلع) شعاع سره د وتر هر سر مرکز کړئ او د وتر پورته او ښکته قوسونه وکاږئ.'),
            R('The arcs meet at the other two vertices; join all four vertices.', 'قوس باقی دو راسوں پر ملتے ہیں؛ چاروں راس ملائیں۔', 'قوسونه په نورو دوو رأسونو کې سره رسېږي؛ ټول څلور رأسونه سره ونښلوئ.')], 'Rhombus constructed'


def main():
    leaves = json.load(open(APP / 'tmp' / 'm8_leaves.json', encoding='utf8'))
    out = []

    def emit(q, no, rows, ans):
        out.append(f"{msol_run.exk(q)}|{q['q']}|{no} ~ @text " + ' ;; '.join(rows) + f' => {ans} ^^')

    for q in leaves:
        if q['ex'] not in ('10.4', '10.5'):
            continue
        n = q['q']
        for no, pt in (q['parts'] or [['', None]]):
            t = (pt or '') + ' ' + (q['en'] or '')
            v = nums(pt or q['en'] or '')
            try:
                if q['ex'] == '10.4' and n == '1' and len(v) >= 3:
                    r, a = sss(v[0], v[1], v[2], 'ABC')
                elif q['ex'] == '10.4' and n == '2' and len(v) >= 3:
                    if re.match(r'.*∠[A-Z]\s*=\s*[\d.]+°\s*,', pt) or re.search(r'∠[A-Z]\s*=\s*[\d.]+°$', pt) is None and False:
                        raise ValueError
                    angfirst = pt.strip().startswith('∠')
                    angs = re.findall(r'∠[A-Z]\s*=\s*([\d.]+)', pt); sides = re.findall(r'\{[A-Z]{2}\}\$?\s*=\s*([\d.]+)', pt)
                    if len(angs) == 1 and len(sides) == 2:
                        ang = float(angs[0]); s1, s2 = float(sides[0]), float(sides[1])
                        vert = re.search(r'∠([A-Z])', pt).group(1)
                        names = re.findall(r'overline\{([A-Z]{2})\}', pt)
                        inc = [nm for nm in names if vert in nm]
                        if len(inc) == 2:
                            r, a = sas(s1, ang, s2)
                        else:
                            adj = float(sides[names.index(inc[0])]); opp = float(sides[1 - names.index(inc[0])])
                            r, a = ssa(adj, opp, ang)
                    else:
                        continue
                elif q['ex'] == '10.4' and n == '3':
                    angs = [float(x) for x in re.findall(r'∠[A-Z]\s*=\s*([\d.]+)', pt)]; sides = [float(x) for x in re.findall(r'\{[A-Z]{2}\}\$?\s*=\s*([\d.]+)', pt)]
                    if len(angs) == 2 and len(sides) == 1:
                        r, a = asa(sides[0], angs[0], angs[1])
                    else:
                        continue
                elif q['ex'] == '10.4' and n == '4':
                    sides = [float(x) for x in re.findall(r'\}\$?\s*(?:\(Hypotenuse\))?\s*=\s*([\d.]+)', pt)]
                    if len(sides) == 2:
                        r, a = rhs(sides[0], sides[1])
                    else:
                        continue
                elif q['ex'] == '10.5' and n in ('1', '3'):
                    d = v[0] if n == '1' else nums(q['en'])[-1] if False else float(re.findall(r'=\s*([\d.]+)\s*cm', q['en'])[0]) if n == '3' else v[0]
                    r, a = square_diag(d)
                elif q['ex'] == '10.5' and n == '2':
                    vv = [float(x) for x in re.findall(r'=\s*([\d.]+)\s*cm', q['en'])]
                    r, a = rect_ab_bc(vv[0], vv[1])
                elif q['ex'] == '10.5' and n == '4':
                    vv = [float(x) for x in re.findall(r'=\s*([\d.]+)\s*cm', pt)]
                    r, a = rect_ab_diag(vv[0], vv[1])
                elif q['ex'] == '10.5' and n == '5':
                    vv = [float(x) for x in re.findall(r'=\s*([\d.]+)', pt)]
                    r, a = rhombus_angle(vv[0], vv[1])
                elif q['ex'] == '10.5' and n == '6':
                    vv = [float(x) for x in re.findall(r'=\s*([\d.]+)', pt)]
                    r, a = rhombus_diag(vv[0], vv[1])
                else:
                    continue
            except Exception:
                continue
            emit(q, no, r, a)
    (HERE / 'class-8' / 'math' / 'dsl' / 'constructions.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(len(out), 'construction items')


if __name__ == '__main__':
    main()
