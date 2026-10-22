"""gen_constr_more.py - construction method steps (EN | UR | PS) for the remaining Class 7 (Review 12) and Class 8 (10.4 c-e, 10.5 Q7-9,
10.6, 10.7, Review 10) construction questions. Reuses the step builders of gen_constr8.py. Every line is marked not verified (^^).
    python gen_constr_more.py
"""
import math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_constr8 as G
from gen_constr8 import R, g

HERE = Path(__file__).resolve().parents[2]


def line(key, rows, ans):
    if isinstance(rows, tuple):
        rows, ans = rows
    return f'{key} ~ @text ' + ' ;; '.join(rows) + f' => {ans} ^^'


def bisectors_tri():
    return [R('Bisect each angle: with the vertex as centre draw an arc cutting both arms, then from those two points draw equal arcs that cross; join the vertex to the crossing point.',
              'ہر زاویے کی تنصیف کریں: راس کو مرکز بنا کر دونوں بازوؤں کو کاٹنے والا قوس لگائیں، پھر ان دو نقطوں سے برابر رداس کے قوس لگائیں جو ایک دوسرے کو کاٹیں؛ راس کو کٹاؤ کے نقطے سے ملائیں۔',
              'هره زاویه نیمایي کړئ: رأس د مرکز په توګه واخلئ، یو قوس رسم کړئ چې دواړه بازوګانې پرې کړي، بیا له دغو دوو ټکو څخه مساوي قوسونه رسم کړئ چې یو بل پرې کړي؛ رأس له تقاطع ټکي سره ونښلوئ.'),
            R('Bisect each side: with the compass opened more than half the side, draw arcs from both ends above and below the side; join the two crossing points (the perpendicular bisector).',
              'ہر ضلع کی تنصیف کریں: پرکار کو ضلع کے نصف سے زیادہ کھول کر دونوں سروں سے ضلع کے اوپر اور نیچے قوس لگائیں؛ دونوں کٹاؤ کے نقطوں کو ملائیں (عمود ثنائی)۔',
              'هر ضلع نیمایي کړئ: پرکار د ضلع له نیمایي ډېر پرانیزئ، له دواړو سرونو څخه د ضلع پورته او ښکته قوسونه رسم کړئ؛ دواړه تقاطع ټکي سره ونښلوئ (عمودي نیمګړی).')], 'Angle and side bisectors drawn'


def parallelogram_diag(d1, d2, ang):
    return [R(f'The diagonals of a parallelogram bisect each other. Draw EG = {g(d1)} cm and mark its midpoint O.', f'متوازی الاضلاع کے وتر ایک دوسرے کی تنصیف کرتے ہیں۔ EG = {g(d1)} سینٹی میٹر کھینچیں اور اس کا وسطی نقطہ O لگائیں۔', f'د موازي الاضلاع قطرونه یو بل نیمایي کوي. EG = {g(d1)} سانتي متره رسم کړئ او منځنی ټکی O یې په نښه کړئ.'),
            R(f'At O make an angle of {g(ang)}° with EG and draw the line FH through O so that OF = OH = {g(d2 / 2)} cm.', f'O پر EG کے ساتھ {g(ang)}° کا زاویہ بنائیں اور O سے گزرتی لکیر FH کھینچیں تاکہ OF = OH = {g(d2 / 2)} سینٹی میٹر ہو۔', f'په O کې د EG سره {g(ang)}° زاویه جوړه کړئ او د O څخه تیره کرښه FH رسم کړئ چې OF = OH = {g(d2 / 2)} سانتي متره وي.'),
            R('Join EF, FG, GH and HE: EFGH is the parallelogram.', 'EF، FG، GH اور HE ملائیں: EFGH متوازی الاضلاع ہے۔', 'EF، FG، GH او HE ونښلوئ: EFGH موازي الاضلاع دی.')], 'Parallelogram constructed'


def square_diff(k, plus):
    s = k / (math.sqrt(2) + 1) if plus else k / (math.sqrt(2) - 1)
    word = 'sum' if plus else 'difference'
    return [R(f'Let the side be s. The diagonal is s√2, so the {word} is s(√2 {"+" if plus else "−"} 1) = {g(k)} cm, which gives s ≈ {s:.2f} cm.', f'ضلع s لیں۔ وتر s√2 ہے، اس لیے {"مجموعہ" if plus else "فرق"} s(√2 {"+" if plus else "−"} 1) = {g(k)} سینٹی میٹر ہے، جس سے s ≈ {s:.2f} سینٹی میٹر ملتا ہے۔', f'ضلع s واخلئ. قطر s√2 دی، نو {"مجموعه" if plus else "توپیر"} s(√2 {"+" if plus else "−"} 1) = {g(k)} سانتي متره دی، چې s ≈ {s:.2f} سانتي متره ورکوي.'),
            R(f'Draw AB = {s:.2f} cm, make a perpendicular at B with BC = {s:.2f} cm, and with centres A and C and radius {s:.2f} cm draw arcs meeting at D.', f'AB = {s:.2f} سینٹی میٹر کھینچیں، B پر عمود بنا کر BC = {s:.2f} سینٹی میٹر لیں، پھر مراکز A اور C اور رداس {s:.2f} سینٹی میٹر سے قوس لگائیں جو D پر ملیں۔', f'AB = {s:.2f} سانتي متره رسم کړئ، په B کې عمود جوړ کړئ او BC = {s:.2f} سانتي متره واخلئ، بیا د A او C مرکزونو او {s:.2f} سانتي متره شعاع سره قوسونه رسم کړئ چې په D کې سره ووځي.'),
            R(f'Join AD and CD. Check: AC ≈ {s * math.sqrt(2):.2f} cm and AC {"+" if plus else "−"} AB = {g(k)} cm.', f'AD اور CD ملائیں۔ جانچ: AC ≈ {s * math.sqrt(2):.2f} سینٹی میٹر اور AC {"+" if plus else "−"} AB = {g(k)} سینٹی میٹر۔', f'AD او CD ونښلوئ. ازموینه: AC ≈ {s * math.sqrt(2):.2f} سانتي متره او AC {"+" if plus else "−"} AB = {g(k)} سانتي متره.')], 'Square constructed'


def square_side(a):
    return [R(f'Draw AB = {g(a)} cm.', f'AB = {g(a)} سینٹی میٹر کھینچیں۔', f'AB = {g(a)} سانتي متره رسم کړئ.'),
            R(f'At A and at B make 90° angles and mark AD = BC = {g(a)} cm on the same side.', f'A اور B پر 90° کے زاویے بنا کر ایک ہی طرف AD = BC = {g(a)} سینٹی میٹر لیں۔', f'په A او B کې 90° زاویې جوړې کړئ او په یوه خوا AD = BC = {g(a)} سانتي متره واخلئ.'),
            R('Join DC: ABCD is the square.', 'DC ملائیں: ABCD مربع ہے۔', 'DC ونښلوئ: ABCD مربع دی.')], 'Square constructed'


def parallelogram_sides(a, b, ang):
    return [R(f'Draw PQ = {g(a)} cm.', f'PQ = {g(a)} سینٹی میٹر کھینچیں۔', f'PQ = {g(a)} سانتي متره رسم کړئ.'),
            R(f'At P make an angle of {g(ang)}° and mark S with PS = {g(b)} cm.', f'P پر {g(ang)}° کا زاویہ بنا کر S اس طرح لگائیں کہ PS = {g(b)} سینٹی میٹر ہو۔', f'په P کې {g(ang)}° زاویه جوړه کړئ او S داسې په نښه کړئ چې PS = {g(b)} سانتي متره وي.'),
            R(f'With centre Q and radius {g(b)} cm and centre S and radius {g(a)} cm draw arcs meeting at R.', f'مرکز Q اور رداس {g(b)} سینٹی میٹر اور مرکز S اور رداس {g(a)} سینٹی میٹر سے قوس لگائیں جو R پر ملیں۔', f'د Q مرکز او {g(b)} سانتي متره شعاع او د S مرکز او {g(a)} سانتي متره شعاع سره قوسونه رسم کړئ چې په R کې سره ووځي.'),
            R('Join QR and SR: PQRS is the parallelogram.', 'QR اور SR ملائیں: PQRS متوازی الاضلاع ہے۔', 'QR او SR ونښلوئ: PQRS موازي الاضلاع دی.')], 'Parallelogram constructed'


def trapezium_sas(par_a, par_b, leg, ang):
    return [R(f'Draw the longer parallel side of {g(par_a)} cm. At one end make the angle {g(ang)}° and mark the leg of {g(leg)} cm on the ray.', f'{g(par_a)} سینٹی میٹر کا لمبا متوازی ضلع کھینچیں۔ ایک سرے پر {g(ang)}° کا زاویہ بنا کر شعاع پر {g(leg)} سینٹی میٹر کا بازو لیں۔', f'{g(par_a)} سانتي متره اوږد موازي ضلع رسم کړئ. په یوه سر کې {g(ang)}° زاویه جوړه کړئ او په وړانګه {g(leg)} سانتي متره ضلع واخلئ.'),
            R(f'Through the end of the leg draw a line parallel to the base (copy equal angles) and mark the shorter parallel side {g(par_b)} cm along it.', f'بازو کے سرے سے قاعدے کے متوازی لکیر کھینچیں (برابر زاویے نقل کریں) اور اس پر چھوٹا متوازی ضلع {g(par_b)} سینٹی میٹر لیں۔', f'د ضلع له سر څخه د قاعدې سره موازي کرښه رسم کړئ (مساوي زاویې کاپي کړئ) او په هغې کې لنډ موازي ضلع {g(par_b)} سانتي متره واخلئ.'),
            R('Join the free ends to complete the trapezium.', 'آزاد سروں کو ملا کر ذوزنقہ مکمل کریں۔', 'آزاد سرونه سره ونښلوئ چې ذوزنقه بشپړ شي.')], 'Trapezium constructed'


def kite_from(a, b, d):
    r, _ = G.sss(a, b, d, 'XYZ')
    ok = (a + b > d) and (a + d > b) and (b + d > a)
    if not ok:
        return r, 'Cannot be constructed'
    return r + [R(f'Reflect the triangle in the diagonal of {g(d)} cm: with the same radii ({g(a)} cm and {g(b)} cm) draw arcs on the other side of the diagonal; they meet at the fourth vertex.', f'مثلث کو {g(d)} سینٹی میٹر کے وتر میں منعکس کریں: انہی رداس ({g(a)} اور {g(b)} سینٹی میٹر) سے وتر کی دوسری طرف قوس لگائیں؛ وہ چوتھے راس پر ملتے ہیں۔', f'درې ګونی د {g(d)} سانتي متره قطر په اړه منعکس کړئ: همدغو شعاعګانو ({g(a)} او {g(b)} سانتي متره) سره د قطر په بله خوا قوسونه رسم کړئ؛ دا په څلورم رأس کې سره ووځي.'),
                R('Join the vertices: the two pairs of adjacent equal sides make the kite.', 'راس ملائیں: برابر ملحقہ اضلاع کے دو جوڑے پتنگ (کائٹ) بناتے ہیں۔', 'رأسونه سره ونښلوئ: د مساوي څنګ ضلعو دوه جوړې کایټ جوړوي.')], 'Kite constructed'


def trapezium_wzx(par_long, par_short, leg, ang_between_leg_and_long):
    pass


def main():
    c8 = []
    c7 = []
    add7 = lambda k, r, a: c7.append(line(k, r, a))
    add8 = lambda k, r, a: c8.append(line(k, r, a))
    # Class 7 Review 12
    r, a = G.sss(7, 7, 7, 'PQR'); add7('R12|12|', r, 'Equilateral triangle constructed (SSS)')
    r, a = G.sss(4, 6, 6, 'ABC'); add7('R12|13|', r, 'Isosceles triangle constructed (SSS)')
    r, a = G.sas(6.3, 90, 4.5); add7('R12|14|', r, 'Right-angled triangle constructed (SAS)')
    r, a = G.asa(7, 20, 40); add7('R12|15|', r, 'Triangle constructed (ASA)')
    r, a = G.sas(6, 70, 5); add7('R12|16|', r, 'Acute-angled triangle constructed (SAS)')
    r, a = G.sas(5, 140, 3); add7('R12|17|', r, 'Obtuse-angled triangle constructed (SAS)')
    # Class 8 10.4 c-e
    r, a = G.sas(8, 30, 8); add8('10.4|2|c', r, 'Triangle constructed (SAS)')
    r, a = G.sas(9, 105, 7); add8('10.4|2|d', r, 'Triangle constructed (SAS)')
    r, a = G.ssa(3, 4, 15); add8('10.4|2|e', r, 'Triangle constructed (SSA, one triangle)')
    # 10.5
    add8('10.5|7|', parallelogram_diag(4.8, 6, 30), 'Parallelogram constructed')
    add8('10.5|8|', square_diff(4, False), 'Square constructed')
    add8('10.5|9|', square_diff(6, True), 'Square constructed')
    # 10.7 kites
    r, a = kite_from(3, 5, 7); add8('10.7|1|', r, a)
    r, a = kite_from(2.5, 4.5, 5.5); add8('10.7|2|', r, a)
    r, a = kite_from(5, 6.2, 4); add8('10.7|3|', r, a)
    # Review 10
    RE = 'Review Exercise 10|'
    r, a = G.asa(6, 45, 60); add8(RE + '5|', r, 'Triangle constructed (ASA, with the side taken as AB)')
    r, a = G.sas(4, 45, 3.8); add8(RE + '6|', r, 'Triangle constructed (SAS, with the sides taken next to the angle L)')
    r, a = G.sss(5, 6.9, 4, 'GHI'); add8(RE + '7|', r, 'Triangle constructed (SSS)')
    r, a = G.rhs(5.7, 7.1); add8(RE + '8|', r + bisectors_tri()[0], 'Right triangle constructed, with angle and side bisectors')
    add8(RE + '9|', square_side(4.5), 'Square constructed')
    add8(RE + '10|', parallelogram_sides(5, 2, 75), 'Parallelogram constructed')
    r, a = G.rhombus_angle(6, 60); add8(RE + '11|', r, a)
    add8(RE + '12|', trapezium_sas(7, 4, 3, 70), 'Trapezium constructed')
    r, a = kite_from(7, 8, 6); add8(RE + '13|', r, a)
    add8(RE + '14|', bisectors_tri()[0], 'Angle and side bisectors of an equilateral triangle drawn')
    add8(RE + '15|', bisectors_tri()[0], 'Angle and side bisectors of a parallelogram drawn')
    (HERE / 'class-7' / 'math' / 'dsl' / 'constr_r12.txt').write_text('\n'.join(c7) + '\n', encoding='utf-8')
    (HERE / 'class-8' / 'math' / 'dsl' / 'constr_more.txt').write_text('\n'.join(c8) + '\n', encoding='utf-8')
    print(len(c7), len(c8))


if __name__ == '__main__':
    main()
