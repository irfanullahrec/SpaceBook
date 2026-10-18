"""Sequential source correction for PDF page 60 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions, shared_class_data_lock

SOURCE = r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"

def pair(en, ur, ps):
    return en, ur, ps

def ref(page):
    return {"pdfPage": 60, "printedPage": page, "sourcePdf": SOURCE}

def svg(body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 400" role="img" aria-label="{escape(label, quote=True)}" style="width:100%;max-width:720px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

VELOCITY = [
    pair("If the electric and magnetic fields are applied perpendicular to each other and adjusted such that the magnitude of electric force is equal but direction is opposite to the magnetic force as shown in Figure 13.21, then", "اگر برقی اور مقناطیسی میدان ایک دوسرے کے عمود لگائے جائیں اور اس طرح ترتیب دیے جائیں کہ برقی قوت کی مقدار مقناطیسی قوت کے برابر مگر سمت مخالف ہو، جیسا کہ شکل 13.21 میں دکھایا گیا ہے، تو", "که برېښنايي او مقناطیسي ساحې یو بل ته عمودي وکارول شي او داسې برابرې شي چې د برېښنايي قوې اندازه د مقناطیسي قوې سره برابره خو لوری یې مخالف وي، لکه په 13.21 شکل کې، نو"),
    pair("Since F_electric = qE and F_magnetic = qvB,", "چونکہ F_electric = qE اور F_magnetic = qvB،", "ځکه F_electric = qE او F_magnetic = qvB،"),
    pair("Therefore qE = qvB", "لہٰذا qE = qvB۔", "نو qE = qvB"),
    pair("v = E/B ...(13.10)", "v = E/B ...(13.10)", "v = E/B ...(13.10)"),
    pair("If the beam of charged particles moving with different velocities passes through a velocity selector, only those particles will pass straight through the device which have velocities equal to the ratio of electric to the magnetic field. Particles moving slower than this speed will be deflected in the direction of electric force, and those having greater speeds will be deflected in the direction of magnetic force.", "اگر مختلف رفتاروں سے حرکت کرتے بار دار ذرات کی شعاع رفتار منتخب کرنے والے آلے سے گزرے تو صرف وہ ذرات سیدھے گزریں گے جن کی رفتار برقی میدان اور مقناطیسی میدان کے تناسب کے برابر ہو۔ اس رفتار سے کم رفتار والے ذرات برقی قوت کی سمت میں اور زیادہ رفتار والے ذرات مقناطیسی قوت کی سمت میں مڑ جائیں گے۔", "که د بېلابېلو سرعتونو چارج لرونکو ذرو وړانګه د سرعت له ټاکونکي څخه تېره شي، یوازې هغه ذرات به نېغ تېر شي چې سرعتونه یې د برېښنايي او مقناطیسي ساحو د نسبت سره برابر وي. له دې سرعت څخه ورو ذرات به د برېښنايي قوې لوري ته او چټک ذرات به د مقناطیسي قوې لوري ته واوړي."),
]

EXAMPLE = [
    pair("EXAMPLE 13.4 — TIME PERIOD FOR ELECTRON IN MAGNETIC FIELD", "مثال 13.4 — مقناطیسی میدان میں الیکٹران کا دورانیہ", "بېلګه 13.4 — په مقناطیسي ساحه کې د الکترون د دورې موده"),
    pair("The path of an electron in a uniform magnetic field of flux density 1.0 × 10⁻² T in a vacuum is a circle of radius 1 cm. Calculate the period of its orbit.", "خلا میں 1.0 × 10⁻² T مقناطیسی فلوکس کثافت کے یکساں میدان میں الیکٹران کا راستہ 1 cm رداس کا دائرہ ہے۔ اس کے مدار کا دورانیہ معلوم کریں۔", "په تشه کې د 1.0 × 10⁻² T فلوکس کثافت په یوشان مقناطیسي ساحه کې د الکترون لاره د 1 cm شعاع دایره ده. د مدار دوره یې محاسبه کړئ."),
    pair("GIVEN", "معلوم", "ورکړل شوي"),
    pair("Radius r = 1 cm = 1 × 10⁻² m; magnetic field B = 1.0 × 10⁻² T; electron charge q_e = 1.6 × 10⁻¹⁹ C; electron mass m_e = 9.11 × 10⁻³¹ kg.", "رداس r = 1 cm = 1 × 10⁻² m؛ مقناطیسی میدان B = 1.0 × 10⁻² T؛ الیکٹران کا بار q_e = 1.6 × 10⁻¹⁹ C؛ الیکٹران کی کمیت m_e = 9.11 × 10⁻³¹ kg۔", "شعاع r = 1 cm = 1 × 10⁻² m؛ مقناطیسي ساحه B = 1.0 × 10⁻² T؛ د الکترون چارج q_e = 1.6 × 10⁻¹⁹ C؛ د الکترون کتله m_e = 9.11 × 10⁻³¹ kg."),
    pair("REQUIRED — Time period T = ?", "مطلوب — دورانیہ T = ؟", "غوښتل شوی — د دورې موده T = ؟"),
    pair("SOLUTION", "حل", "حل"),
    pair("From the circular trajectory of a charged particle, the time period is", "بار دار ذرے کے دائروی راستے سے دورانیہ یہ ہے:", "د چارج لرونکې ذرې له دایروي مسیر څخه د دورې موده داسې ده:"),
    pair("T = 2πm/(qB)", "T = 2πm/(qB)", "T = 2πm/(qB)"),
    pair("Putting in the given values,", "دی گئی قدریں رکھنے سے،", "ورکړل شوي ارزښتونه په ځای کولو سره،"),
    pair("T = (2 × 3.14 × 9.11 × 10⁻³¹ kg)/(1.6 × 10⁻¹⁹ C × 1.0 × 10⁻² T)", "T = (2 × 3.14 × 9.11 × 10⁻³¹ kg)/(1.6 × 10⁻¹⁹ C × 1.0 × 10⁻² T)", "T = (2 × 3.14 × 9.11 × 10⁻³¹ kg)/(1.6 × 10⁻¹⁹ C × 1.0 × 10⁻² T)"),
    pair("T = 3.57 × 10⁻⁹ s = 3.57 ns", "T = 3.57 × 10⁻⁹ s = 3.57 ns", "T = 3.57 × 10⁻⁹ s = 3.57 ns"),
]

ASSIGNMENT = [
    pair("ASSIGNMENT 13.3", "مشق 13.3", "کورنی دنده 13.3"),
    pair("A velocity selector in a mass spectrometer uses a 0.100 T magnetic field. What electric field strength is needed to select a speed of 4.00 × 10⁶ m/s? (Answer: 4.00 × 10⁵ N/C)", "په کتلي طیف پېژندونکي کې د رفتار منتخبولو آله 0.100 T مقناطیسي میدان کاروي۔ د 4.00 × 10⁶ m/s رفتار د ټاکلو لپاره د برقي میدان شدت څومره پکار دی؟ (ځواب: 4.00 × 10⁵ N/C)", "د کتلې په طیف‌پېژندونکي کې د سرعت ټاکونکی 0.100 T مقناطیسي ساحه کاروي. د 4.00 × 10⁶ m/s سرعت د ټاکلو لپاره د برېښنايي ساحې کوم شدت پکار دی؟ (ځواب: 4.00 × 10⁵ N/C)"),
]

COIL = [
    pair("13.7 TORQUE ON A CURRENT CARRYING COIL", "13.7 پرکرنٹ بردار کوائل پر ٹارک", "13.7 پر جریان‌لرونکي کویل تورک"),
    pair("When a current-carrying coil or loop is placed in a uniform magnetic field, it experiences a force; this force can exert torque on the coil or loop of wire.", "جب کرنٹ بردار کوائل یا حلقہ یکساں مقناطیسی میدان میں رکھا جاتا ہے تو اس پر قوت لگتی ہے؛ یہ قوت کوائل یا تار کے حلقے پر ٹارک پیدا کر سکتی ہے۔", "کله چې جریان‌لرونکی کویل یا کړۍ په یوشان مقناطیسي ساحه کې کېښودل شي، قوه تجربه کوي؛ دا قوه پر کویل یا د سیم پر کړۍ تورک واردولی شي."),
    pair("Let us consider a rectangular coil carrying a current I in the presence of a uniform magnetic field B directed parallel to the plane of the loop, as shown in Figure 13.22.", "شکل 13.22 میں دکھائے گئے مطابق، ایک مستطیل کوائل لیں جس میں رو I ہو اور یکساں مقناطیسی میدان B حلقے کے مستوی کے متوازی ہو۔", "د 13.22 شکل په څېر یو مستطیل کویل په پام کې ونیسئ چې جریان I لري او یوشان مقناطیسي ساحه B یې د کړۍ له مستوي سره موازي وي."),
    pair("No magnetic forces act on sides 1 and 3 because these wires are parallel to the field (θ = 0°); the length of sides 1 and 3 is b. Therefore the magnetic force is", "اطراف 1 اور 3 پر مقناطیسی قوت نہیں لگتی کیونکہ یہ تار میدان کے متوازی ہیں (θ = 0°)؛ اطراف 1 اور 3 کی لمبائی b ہے۔ لہٰذا مقناطیسی قوت", "پر 1 او 3 اړخونو مقناطیسي قوې نه لګېږي، ځکه دا تارونه له ساحې سره موازي دي (θ = 0°)؛ د 1 او 3 اړخونو اوږدوالی b دی. نو مقناطیسي قوه"),
    pair("F₁ = F₃ = BIb sin 0°", "F₁ = F₃ = BIb sin 0°", "F₁ = F₃ = BIb sin 0°"),
    pair("Since sin 0° = 0,", "چونکہ sin 0° = 0،", "ځکه sin 0° = 0،"),
    pair("Therefore F₁ = F₃ = 0 ...(1)", "لہٰذا F₁ = F₃ = 0 ...(1)", "نو F₁ = F₃ = 0 ...(1)"),
    pair("FIGURE 13.22 — A coil in a magnetic field.", "شکل 13.22 — مقناطیسی میدان میں ایک کوائل۔", "13.22 شکل — په مقناطیسي ساحه کې کویل."),
    pair("However maximum magnetic forces act on sides 2 and 4, because these sides are perpendicular to the field (θ = 90°); the length of sides 2 and 4 is a. Therefore the magnetic force is", "تاہم اطراف 2 اور 4 پر زیادہ سے زیادہ مقناطیسی قوتیں لگتی ہیں کیونکہ یہ اطراف میدان کے عمود ہیں (θ = 90°)؛ اطراف 2 اور 4 کی لمبائی a ہے۔ لہٰذا مقناطیسی قوت", "خو پر 2 او 4 اړخونو تر ټولو زیاتې مقناطیسي قوې لګېږي، ځکه دا اړخونه له ساحې سره عمودي دي (θ = 90°)؛ د 2 او 4 اړخونو اوږدوالی a دی. نو مقناطیسي قوه"),
    pair("F₂ = F₄ = BIL sin 90°", "F₂ = F₄ = BIL sin 90°", "F₂ = F₄ = BIL sin 90°"),
    pair("Since sin 90° = 1,", "چونکہ sin 90° = 1،", "ځکه sin 90° = 1،"),
    pair("Therefore F₂ = F₄ = BIa ...(2)", "لہٰذا F₂ = F₄ = BIa ...(2)", "نو F₂ = F₄ = BIa ...(2)"),
    pair("By applying Right hand rule II or Fleming’s left hand rule, it can be seen that the forces on sides 2 and 4 (F₂ and F₄) produce a net torque.", "د دائیں ہاتھ کے قاعدے II یا فلیمنگ کے بائیں ہاتھ کے قاعدے سے معلوم ہوتا ہے کہ اطراف 2 اور 4 پر قوتیں (F₂ اور F₄) خالص ٹارک پیدا کرتی ہیں۔", "د ښي لاس د دویمې قاعدې یا د فلېمینګ د چپ لاس د قاعدې له مخې، پر 2 او 4 اړخونو قوې (F₂ او F₄) خالص تورک جوړوي."),
]

def coil_svg(lang):
    labels = {
        "en": ("Uniform magnetic field B", "I", "a", "b", "F₂", "F₄", "Coil in a magnetic field"),
        "ur": ("یکساں مقناطیسی میدان B", "I", "a", "b", "F₂", "F₄", "مقناطیسی میدان میں کوائل"),
        "ps": ("یوشان مقناطیسي ساحه B", "I", "a", "b", "F₂", "F₄", "په مقناطیسي ساحه کې کویل"),
    }[lang]
    b = '<g fill="#334155" font-size="18">'
    for x in range(55, 680, 75):
        b += f'<text x="{x}" y="56">→</text><text x="{x}" y="344">→</text>'
    b += '</g><path d="M270 115H480V285H270Z" fill="#eff6ff" stroke="#7c3aed" stroke-width="5"/><path d="M270 145V255M480 145V255" stroke="#d4a72c" stroke-width="8"/><path d="M315 115V78M435 285V322" stroke="#dc2626" stroke-width="4"/><path d="M307 88l8-14 8 14M427 312l8 14 8-14" fill="#dc2626"/><path d="M243 168V232M507 232V168" stroke="#16a34a" stroke-width="4"/><path d="M235 178l8-14 8 14M499 222l8 14 8-14" fill="#16a34a"/><text x="350" y="207" font-size="18">I</text><text x="380" y="108" font-size="16">b</text><text x="488" y="207" font-size="16">a</text><text x="210" y="194" font-size="16">F₂</text><text x="516" y="194" font-size="16">F₄</text><text x="250" y="385" font-size="14">'+labels[0]+' · '+labels[6]+'</text>'
    return svg(b, "Figure 13.22: rectangular current-carrying coil in a uniform magnetic field; opposing side forces form a couple.")

def make(identity, title, printed, pairs, layout, titles, refs, diagram=None):
    record = {"id": identity, "title": title, "kind": "lesson", "pdfPage": 60, "printedPage": printed, "sourcePdf": SOURCE, "paragraphs": [p[0] for p in pairs]}
    sec = section(record, pairs, layout, titles)
    sec["kind"] = "lesson"
    sec["sourceReferences"] = [ref(p) for p in refs]
    if diagram:
        sec.update(diagram)
        sec["content"] += diagram["diagramSvg"]
    return record, sec

if __name__ == "__main__":
    velocity = make("phys13-velocity-selector-force-balance-and-eq1310108", "Velocity selector force balance and selected speed", 108, VELOCITY, [
        {"type": "paragraph", "indices": [0]}, {"type": "paragraph", "indices": [1]},
        {"type": "equation", "indices": [2]}, {"type": "equation", "indices": [3]},
        {"type": "paragraph", "indices": [4]},
    ], ("رفتار منتخب کرنے والے آلے میں قوتوں کا توازن اور منتخب رفتار", "د سرعت ټاکونکي د قوې توازن او ټاکل شوی سرعت"), [108])
    example = make("phys13-example134-electron-period108", "Example 13.4 — electron orbital period", 108, EXAMPLE, [
        {"type": "heading", "indices": [0]}, {"type": "paragraph", "indices": [1]},
        {"type": "heading", "indices": [2]}, {"type": "paragraph", "indices": [3]},
        {"type": "paragraph", "indices": [4]}, {"type": "heading", "indices": [5]},
        {"type": "paragraph", "indices": [6]}, {"type": "equation", "indices": [7]},
        {"type": "paragraph", "indices": [8]}, {"type": "equation", "indices": [9]},
        {"type": "equation", "indices": [10]},
    ], ("مثال 13.4 — مقناطیسي میدان کې د الکترون د مدار دوره", "بېلګه 13.4 — په مقناطیسي ساحه کې د الکترون د مدار موده"), [108])
    assignment = make("phys13-assignment133-velocity-selector108", "Assignment 13.3 — velocity selector", 108, ASSIGNMENT, [
        {"type": "heading", "indices": [0]}, {"type": "paragraph", "indices": [1]},
    ], ("مشق 13.3 — رفتار منتخب کرنے والا آلہ", "کورنی دنده 13.3 — د سرعت ټاکونکی"), [108])
    coil = make("phys13-torque-current-carrying-coil-intro-figure1322109", "Torque on a current-carrying coil — introduction and forces", 109, COIL, [
        {"type": "heading", "indices": [0]}, {"type": "paragraph", "indices": [1]},
        {"type": "paragraph", "indices": [2]}, {"type": "paragraph", "indices": [3]},
        {"type": "equation", "indices": [4]}, {"type": "paragraph", "indices": [5]},
        {"type": "equation", "indices": [6]}, {"type": "visual", "indices": [7]},
        {"type": "paragraph", "indices": [8]}, {"type": "equation", "indices": [9]},
        {"type": "paragraph", "indices": [10]}, {"type": "equation", "indices": [11]},
        {"type": "paragraph", "indices": [12]},
    ], ("پر کرنٹ بردار کوائل پر ٹارک — تعارف اور قوتیں", "پر جریان‌لرونکي کویل تورک — پېژندنه او قوې"), [109], {
        "diagramSvg": coil_svg("en"), "diagramSvgUrdu": coil_svg("ur"), "diagramSvgPashto": coil_svg("ps")
    })
    records = [velocity[0], example[0], assignment[0], coil[0]]
    sections = [velocity[1], example[1], assignment[1], coil[1]]
    formulas = [{"id": "phys13-velocity-selector-speed-13-10", "name": "Selected speed in a velocity selector", "number": "13.10", "formula": VELOCITY[3][0], "latex": "v=E/B", "sourceReferences": [ref(108)]}]
    definitions = []
    with shared_class_data_lock():
        upsert(records, sections, chapter_index=2)
        sync_companions(chapter_index=2, retire_sections=[], trim_sections=[{"id": "13.9", "startsAt": "If we view the loop from side 3 and sight along sides 2 and 4", "title": "Torque derivation continuation — first unchecked text on printed page 110"}], formulas=formulas, definitions=definitions)
    progress = json.loads((ROOT / "docs/source-verification/class-12/progress.json").read_text(encoding="utf-8"))
    if progress["nextPage"] == 60:
        checkpoint(60, "corrected_verified", [r["id"] for r in records],
            "Rendered and inspected PDF page 60, printed pages 108–109. Compared velocity-selector force balance and selected-speed Eq. 13.10, the slower/faster particle directions, complete Example 13.4 data/substitution/result, Assignment 13.3 and its printed answer, and the opening current-coil torque derivation through side forces and equations (1)–(2). Rebuilt Figure 13.22 as coded SVG with English, Urdu and Pashto variants. Preserved the next source sentence, beginning “If we view the loop from side 3 and sight along sides 2 and 4,” as unchecked continuation on printed page 110.",
            printed_pages=[108, 109], chapter_number=13)
