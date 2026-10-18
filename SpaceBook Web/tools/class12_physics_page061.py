"""Sequential source correction for PDF page 61 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions, shared_class_data_lock

SOURCE = r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"

def pair(en, ur, ps): return en, ur, ps
def ref(page): return {"pdfPage": 61, "printedPage": page, "sourcePdf": SOURCE}
def svg(body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 380" role="img" aria-label="{escape(label, quote=True)}" style="width:100%;max-width:680px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

DERIVATION = [
    pair("If we view the loop from side 3 and sight along sides 2 and 4, we see the view shown in Figure 13.23. The two magnetic forces F₂ and F₄ point in opposite directions such that they form a couple. If the loop is pivoted so that it can rotate about point O, these two forces produce a torque that rotates the loop (in this case clockwise). The magnitude of this torque is", "اگر ہم حلقے کو سمت 3 سے اطراف 2 اور 4 کی سمت دیکھیں تو شکل 13.23 کا منظر نظر آتا ہے۔ دونوں مقناطیسی قوتیں F₂ اور F₄ مخالف سمتوں میں لگتی ہیں اور قوتوں کا جوڑا بناتی ہیں۔ اگر حلقہ نقطہ O کے گرد گھومنے کے لیے محور پر ہو تو یہ قوتیں ٹارک پیدا کرتی ہیں جو حلقے کو گھماتا ہے (اس صورت میں گھڑی وار)۔ اس ٹارک کی مقدار", "که کړۍ له 3 اړخ څخه د 2 او 4 اړخونو په لور وګورو، د 13.23 شکل لید وینو. دواړه مقناطیسي قوې F₂ او F₄ مخالف لوري لري او د قوې جوړه جوړوي. که کړۍ د O نقطې شاوخوا د څرخېدو لپاره پر محور وي، دا قوې تورک جوړوي چې کړۍ تاووي (دلته د ساعت د ستنې په لوري). د دې تورک اندازه"),
    pair("τ = F₂(b/2) + F₄(b/2) ...(3)", "τ = F₂(b/2) + F₄(b/2) ...(3)", "τ = F₂(b/2) + F₄(b/2) ...(3)"),
    pair("Putting values of F₂ and F₄ from equation 2 in equation 3, we get τ = IBa(b/2) + IBa(b/2), or τ = 2IBa(b/2). Therefore τ = IBab ...(4)", "مساوات 2 سے F₂ اور F₄ کی قدریں مساوات 3 میں رکھنے سے τ = IBa(b/2) + IBa(b/2)، یا τ = 2IBa(b/2)۔ لہٰذا τ = IBab ...(4)", "د 2 معادلې F₂ او F₄ ارزښتونه په 3 معادله کې په ایښودلو، τ = IBa(b/2) + IBa(b/2)، یا τ = 2IBa(b/2) ترلاسه کوو. نو τ = IBab ...(4)"),
    pair("Since a is the length and b is the width of the coil, therefore ab = A ...(5)", "چونکہ a کوائل کی لمبائی اور b چوڑائی ہے، اس لیے ab = A ...(5)", "ځکه a د کویل اوږدوالی او b یې پلنوالی دی، نو ab = A ...(5)"),
    pair("Putting equation 5 in equation 4, we get τ = IBA ...(13.11)", "مساوات 5 کو مساوات 4 میں رکھنے سے τ = IBA ...(13.11)", "د 5 معادلې په 4 معادله کې په ایښودلو τ = IBA ...(13.11) ترلاسه کوو"),
    pair("Equation 13.11 represents the maximum condition for torque on a current-carrying loop of wire.", "مساوات 13.11 تار کے کرنٹ بردار حلقے پر ٹارک کی زیادہ سے زیادہ حالت ظاہر کرتی ہے۔", "13.11 معادله د جریان‌لرونکي سیم پر کړۍ د تورک تر ټولو زیاته حالت ښيي."),
    pair("Now suppose the uniform magnetic field B makes an angle θ < 90° with a line perpendicular to the plane of the loop, as in Figure 13.24.", "اب فرض کریں کہ یکساں مقناطیسی میدان B حلقے کے مستوی پر عمود خط کے ساتھ θ < 90° زاویہ بناتا ہے، جیسا کہ شکل 13.24 میں ہے۔", "اوس فرض کړئ چې یوشان مقناطیسي ساحه B د کړۍ د مستوي پر عمودي کرښې سره θ < 90° زاویه جوړوي، لکه په 13.24 شکل کې."),
    pair("The torque is given by the relation τ = IBA sin θ ...(13.12)", "ٹارک کا تعلق τ = IBA sin θ ...(13.12) ہے۔", "د تورک اړیکه τ = IBA sin θ ...(13.12) ده."),
]

EXAMPLE = [
    pair("EXAMPLE 13.5 — TORQUE ON A LOOP", "مثال 13.5 — حلقے پر ٹارک", "بېلګه 13.5 — پر کړۍ تورک"),
    pair("A square loop of wire of side 4.0 cm carries 3.0 A of current. A uniform magnetic field of magnitude 0.67 T makes an angle of 30° with the plane of the loop. (a) What is the magnitude of the torque on the loop? (b) What is the net magnetic force on the loop?", "4.0 cm ضلع والا تار کا مربع حلقہ 3.0 A رو لے جاتا ہے۔ 0.67 T مقدار کا یکساں مقناطیسی میدان حلقے کے مستوی سے 30° زاویہ بناتا ہے۔ (الف) حلقے پر ٹارک کی مقدار کیا ہے؟ (ب) حلقے پر خالص مقناطیسی قوت کیا ہے؟", "د 4.0 cm ضلع لرونکې مربع سیم کړۍ د 3.0 A جریان لري. د 0.67 T اندازه لرونکې یوشان مقناطیسي ساحه د کړۍ له مستوي سره 30° زاویه جوړوي. (الف) پر کړۍ د تورک اندازه څومره ده؟ (ب) پر کړۍ خالصه مقناطیسي قوه څومره ده؟"),
    pair("GIVEN — For a single square loop, number of turns N = 1; magnetic field B = 0.6 T; area A = ab = 4.0 cm × 4.0 cm = 0.0016 m; current I = 3.0 A; angle with plane of loop φ = 30°.", "معلوم — ایک مربع حلقے کے لیے چکروں کی تعداد N = 1؛ مقناطیسی میدان B = 0.6 T؛ رقبہ A = ab = 4.0 cm × 4.0 cm = 0.0016 m؛ رو I = 3.0 A؛ حلقے کے مستوی سے زاویہ φ = 30°۔", "ورکړل شوي — د یوې مربع کړۍ لپاره د تاوونو شمېر N = 1؛ مقناطیسي ساحه B = 0.6 T؛ مساحت A = ab = 4.0 cm × 4.0 cm = 0.0016 m؛ جریان I = 3.0 A؛ د کړۍ له مستوي سره زاویه φ = 30°."),
    pair("REQUIRED — Torque τ = ?; magnetic force F_net = ?", "مطلوب — ٹارک τ = ؟؛ مقناطیسی قوت F_net = ؟", "غوښتل شوي — تورک τ = ؟؛ مقناطیسي قوه F_net = ؟"),
    pair("SOLUTION — The angle θ between the area vector A and magnetic field B is θ = 90° − φ = 90° − 30° = 60°.", "حل — رقبے کے سمتیہ A اور مقناطیسی میدان B کے درمیان زاویہ θ = 90° − φ = 90° − 30° = 60° ہے۔", "حل — د ساحوي ویکتور A او مقناطیسي ساحې B ترمنځ زاویه θ = 90° − φ = 90° − 30° = 60° ده."),
    pair("(a) The torque on the current-carrying coil is τ = NIAB sin θ. Putting values: τ = 1 × (3.00 A) × 0.0016 m × 0.6 T sin 60°. Hence τ = 2.5 × 10⁻³ Nm. Answer.", "(الف) کرنٹ بردار کوائل پر ٹارک τ = NIAB sin θ ہے۔ قدریں رکھنے سے: τ = 1 × (3.00 A) × 0.0016 m × 0.6 T sin 60°۔ لہٰذا τ = 2.5 × 10⁻³ Nm۔ جواب۔", "(الف) پر جریان‌لرونکي کویل تورک τ = NIAB sin θ دی. ارزښتونه په ځای کوو: τ = 1 × (3.00 A) × 0.0016 m × 0.6 T sin 60°. نو τ = 2.5 × 10⁻³ Nm. ځواب."),
    pair("(b) B sin θ is the same at opposite sides of the loop and opposite sides have equal and opposite forces. The net force is zero: F⃗_net = F⃗_top + F⃗_bottom + F⃗_right + F⃗_left = F⃗_top − F⃗_top + F⃗_right − F⃗_right. Hence F⃗_net = 0 N. Answer.", "(ب) حلقے کے مخالف اطراف پر B sin θ یکساں ہے اور قوتیں برابر مگر مخالف ہیں۔ خالص قوت صفر ہے: F⃗_net = F⃗_top + F⃗_bottom + F⃗_right + F⃗_left = F⃗_top − F⃗_top + F⃗_right − F⃗_right۔ لہٰذا F⃗_net = 0 N۔ جواب۔", "(ب) د کړۍ پر مخالف اړخونو کې B sin θ یو شان دی او قوې برابرې خو مخالفې دي. خالصه قوه صفر ده: F⃗_net = F⃗_top + F⃗_bottom + F⃗_right + F⃗_left = F⃗_top − F⃗_top + F⃗_right − F⃗_right. نو F⃗_net = 0 N. ځواب."),
]

def figure(lang, angled=False):
    lab = {"en": ("Uniform B field", "Force F₂", "Force F₄", "Torque at angle θ < 90°" if angled else "Side view of a coil in a magnetic field"),
           "ur": ("یکساں B میدان", "قوت F₂", "قوت F₄", "θ < 90° زاویے پر ٹارک" if angled else "مقناطیسی میدان میں کوائل کا پہلوئی منظر"),
           "ps": ("یوشان B ساحه", "قوه F₂", "قوه F₄", "په θ < 90° زاویه تورک" if angled else "په مقناطیسي ساحه کې د کویل اړخیز لید")}[lang]
    if not angled:
        b = '<path d="M70 130H610M70 240H610" stroke="#2563eb" stroke-width="4"/><path d="M590 120l20 10-20 10M590 230l20 10-20 10" fill="#2563eb"/><path d="M200 180H490" stroke="#334155" stroke-width="5"/><circle cx="220" cy="180" r="18" fill="#fff" stroke="#334155" stroke-width="3"/><circle cx="470" cy="180" r="18" fill="#fff" stroke="#334155" stroke-width="3"/><circle cx="220" cy="180" r="7" fill="#334155"/><path d="M470 170l20 20m0-20l-20 20" stroke="#334155" stroke-width="4"/><circle cx="345" cy="180" r="7" fill="#111827"/><path d="M220 170V75M470 190V285" stroke="#dc2626" stroke-width="4"/><path d="M210 90l10-18 10 18M460 270l10 18 10-18" fill="#dc2626"/><text x="205" y="55" font-size="17">F₂</text><text x="457" y="320" font-size="17">F₄</text><text x="330" y="210" font-size="17">O</text><text x="170" y="205">2</text><text x="492" y="205">4</text><text x="370" y="168" font-size="17">b</text><text x="505" y="115">'+lab[0]+'</text>'
    else:
        b = '<path d="M65 130H610M65 260H610" stroke="#2563eb" stroke-width="4"/><path d="M590 120l20 10-20 10M590 250l20 10-20 10" fill="#2563eb"/><path d="M220 230L455 155" stroke="#334155" stroke-width="5"/><circle cx="230" cy="226" r="18" fill="#fff" stroke="#334155" stroke-width="3"/><circle cx="445" cy="159" r="18" fill="#fff" stroke="#334155" stroke-width="3"/><circle cx="230" cy="226" r="7" fill="#334155"/><path d="M445 149l20 20m0-20l-20 20" stroke="#334155" stroke-width="4"/><circle cx="337" cy="192" r="7" fill="#111827"/><path d="M230 214V100M445 171V295" stroke="#dc2626" stroke-width="4"/><path d="M220 115l10-18 10 18M435 280l10 18 10-18" fill="#dc2626"/><path d="M338 192L405 120" stroke="#7c3aed" stroke-width="4"/><path d="M338 192H438" stroke="#16a34a" stroke-width="2" stroke-dasharray="6 5"/><path d="M378 192A40 40 0 0 0 367 164" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="242" y="115">F₂</text><text x="450" y="318">F₄</text><text x="413" y="119">A</text><text x="376" y="184">θ</text><text x="368" y="209">b/2 sin θ</text><text x="490" y="112">'+lab[0]+'</text>'
    b += '<text x="60" y="360" font-size="15">'+lab[3]+'</text>'
    return svg(b, 'Figure 13.23/13.24: opposite side forces form a couple and produce coil torque.')

def make(identity, title, printed, pairs, layout, titles, refs, diagram=None):
    record={"id":identity,"title":title,"kind":"lesson","pdfPage":61,"printedPage":printed,"sourcePdf":SOURCE,"paragraphs":[p[0] for p in pairs]}
    sec=section(record,pairs,layout,titles);sec["kind"]="lesson";sec["sourceReferences"]=[ref(p) for p in refs]
    if diagram: sec.update(diagram);sec["content"]+=diagram["diagramSvg"]
    return record,sec

if __name__=="__main__":
    deriv=make("phys13-torque-coil-derivation-eq1311-1312-110","Torque on a current-carrying coil — couple and angle",110,DERIVATION,[
        {"type":"paragraph","indices":[0]},{"type":"equation","indices":[1]},{"type":"equation","indices":[2]},
        {"type":"paragraph","indices":[3]},{"type":"equation","indices":[4]},{"type":"paragraph","indices":[5]},
        {"type":"paragraph","indices":[6]},{"type":"equation","indices":[7]},{"type":"visual"},{"type":"visual"}],
        ("پر کرنٹ بردار کوائل ٹارک — قوتوں کا جوڑا اور زاویہ","پر جریان‌لرونکي کویل تورک — د قوې جوړه او زاویه"),[110],{
            "diagramSvg":figure("en"),"diagramSvgUrdu":figure("ur"),"diagramSvgPashto":figure("ps"),
            "diagramSvg2":figure("en",True),"diagramSvgUrdu2":figure("ur",True),"diagramSvgPashto2":figure("ps",True)})
    example=make("phys13-example135-torque-square-loop-111","Example 13.5 — torque and net force on a square loop",111,EXAMPLE,[
        {"type":"heading","indices":[0]},{"type":"paragraph","indices":[1]},{"type":"paragraph","indices":[2]},
        {"type":"paragraph","indices":[3]},{"type":"paragraph","indices":[4]},{"type":"paragraph","indices":[5]},
        {"type":"paragraph","indices":[6]}],("مثال 13.5 — مربع حلقے پر ٹارک اور خالص قوت","بېلګه 13.5 — پر مربع کړۍ تورک او خالصه قوه"),[111])
    records=[deriv[0],example[0]];sections=[deriv[1],example[1]]
    formulas=[
        {"id":"phys13-torque-coil-maximum-13-11","name":"Maximum torque on a current-carrying loop","number":"13.11","formula":DERIVATION[4][0],"latex":"τ=IBA","sourceReferences":[ref(110)]},
        {"id":"phys13-torque-coil-angle-13-12","name":"Torque on a current-carrying loop at angle","number":"13.12","formula":DERIVATION[7][0],"latex":"τ=IBA sin θ","sourceReferences":[ref(110)]}]
    examples=[{"id":"phys13-example135-torque-square-loop","title":"Example 13.5 — torque on a square loop","question":EXAMPLE[1][0],"solution":" ".join(p[0] for p in EXAMPLE[2:]),"answer":"τ = 2.5 × 10⁻³ Nm; F⃗_net = 0 N","sourceReferences":[ref(111)]}]
    with shared_class_data_lock():
        upsert(records,sections,chapter_index=2)
        sync_companions(chapter_index=2,formulas=formulas,worked_examples=examples,trim_sections=[{"id":"13.10","startsAt":"13.8 GALVANOMETER","title":"Moving-coil galvanometer — first unchecked text on printed page 112"}])
    progress=json.loads((ROOT/"docs/source-verification/class-12/progress.json").read_text(encoding="utf-8"))
    if progress["nextPage"]==61:
        checkpoint(61,"corrected_verified",[r["id"] for r in records],
            "Rendered and inspected PDF page 61, printed pages 110–111. Compared the opposing-force couple, torque derivation equations (3)–(5), Eqs. 13.11–13.12, Figures 13.23–13.24 and all of Example 13.5 including the printed givens, substitution, answer and zero-net-force result. Rebuilt both torque diagrams as coded English/Urdu/Pashto SVGs and synchronized formulas and worked example. The next-page boundary is the printed heading “13.8 GALVANOMETER” on PDF page 62; it remains in the unchecked legacy continuation.",
            printed_pages=[110,111],chapter_number=13)
