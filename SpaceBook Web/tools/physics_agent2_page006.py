from physics_agent2_sequential import save_page
from pathlib import Path
import pymupdf

OUTCOMES = [
    'describe the concept of electric dipole.', 'define and explain electric flux.',
    'describe electric flux through a surface enclosing a charge.', "state and explain Gauss's law.",
    'describe and draw the electric field due to an infinite size conducting plate of positive or negative charge.',
    'sketch the electric field produced by a hollow spherical charged conductor.',
    'sketch the electric field between and near the edges of two infinite size oppositely charged parallel plates.',
    'define electric potential at a point in terms of the work done in bringing unit positive charge from infinity to that point.',
    'define the unit of potential.', r'solve problems by using the expression \(V=W/q\).',
    'describe that the electric field at a point is given by the negative of potential gradient at that point.',
    r'solve problems by using the expression \(E=V/d\).',
    'derive an expression for electric potential at a point due to a point charge.',
    r'calculate the potential in the field of a point charge using the equation \(V=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}\).',
    'define and become familiar with the use of electron volt.',
    r'define capacitance and the farad and solve problems by using \(C=Q/V\).',
    'describe the functions of capacitors in simple circuits.',
    'solve problems using formula for capacitors in series and in parallel.',
    'explain polarization of dielectric of a capacitor.',
    'demonstrate charging and discharging of a capacitor through a resistance.',
    r'prove that energy stored in a capacitor is \(W=\frac12 QV\) and hence \(W=\frac12 CV^2\).',
]

TEXT = [
    'Electrostatics is the studies of electric charges which are at rest or static. The electric force between static charged particles is known as the electrostatic force.',
    "The electrostatic force is attractive or repulsive force between particles that are caused due to their electric charges. It is also referred to as Coulomb's force. In SI units, charge is measured in coulombs (symbol C). The charge q is quantized and it is an integral multiple of elementary charge e, i.e., "+r'\(q=ne\).',
    'Another quantity being discussed that plays an important role in electrical circuits is capacitance and its dependence on the dielectrics.',
    "11.1 COULOMB'S LAW",
    "The quantitative measurement of the force between two electric charges was first made by Coulomb. He carried out series of experiments to measure the force between electric charges using an apparatus known as torsion balance. Coulomb expresses his experimental data in the form of a statement which is known as Coulomb's law.",
    'It states “the magnitude of the force between two point charges, is directly proportional to the product of the magnitudes of the charges and inversely proportional to the square of the distance between them.”',
    "Charles-Augustin de Coulomb (1736–1805) was an eminent French physicist who formulated the law known Coulomb's law.",
]

def charges(ident, opposite=False):
    rows=[(70,'opposite')] if opposite else [(70,'right'),(180,'left')]
    svg=f'<figure><svg viewBox="0 0 430 {150 if opposite else 260}" role="img" aria-label="Coulomb force between {"opposite" if opposite else "similar"} charges" style="width:100%;max-width:550px"><defs><marker id="{ident}-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#111827"/></marker></defs>'
    for y,direction in rows:
        svg+=f'<line x1="100" y1="{y}" x2="320" y2="{y}" stroke="#64748b"/><circle cx="100" cy="{y}" r="12" fill="#f9a8d4"/><circle cx="320" cy="{y}" r="12" fill="{"#67e8f9" if opposite else "#f9a8d4"}"/><text x="94" y="{y+6}">+</text><text x="314" y="{y+6}">{"−" if opposite else "+"}</text><text x="90" y="{y-27}">q₁</text><text x="310" y="{y-27}">q₂</text><text x="210" y="{y+35}">r</text>'
        arrows=[(115,185,'F₂₁'),(305,235,'F₁₂')] if opposite else ([(332,397,'F₂₁'),(120,270,'r̂₁₂')] if direction=='right' else [(88,23,'F₁₂'),(300,150,'r̂₂₁')])
        for x1,x2,label in arrows:
            svg+=f'<line x1="{x1}" y1="{y-16}" x2="{x2}" y2="{y-16}" stroke="#111827" marker-end="url(#{ident}-arrow)"/><text x="{min(x1,x2)+10}" y="{y-25}">{label}</text>'
    return svg+f'</svg><figcaption>Figure {"11.2: Coulomb force between opposite charges." if opposite else "11.1 (a), (b): Coulomb force between similar charges."}</figcaption></figure>'

if __name__ == '__main__':
    root=Path(__file__).resolve().parents[1]
    pdf=pymupdf.open(root.parent/'Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf')
    (root/'assets/physics12').mkdir(exist_ok=True)
    pdf[5].get_pixmap(matrix=pymupdf.Matrix(3,3),clip=pymupdf.Rect(670,320,790,449)).save(root/'assets/physics12/coulomb-portrait.png')
    save_page(6,[{'id':'phys12-front-outcomes2','printedPage':2,'title':'Unit 11: Electrostatics — Learning outcomes (2)',
                 'kind':'learning_outcomes','objectives':OUTCOMES,'paragraphs':OUTCOMES+["In this unit two fundamental processes of electrostatics are introduced: Coulomb's law for force between stationary charges and the principle of superposition for electric field configurations."]},
                {'id':'phys12-front-coulomb-introduction','printedPage':3,'title':"11.1 Coulomb's law — Introduction",'kind':'lesson','paragraphs':TEXT,
                 'definitions':[{'term':'Electrostatics','text':TEXT[0]},{'term':"Coulomb's law",'text':TEXT[5]}],
                 'formulas':[{'latex':'q=ne','meaning':'Charge is quantized in integral multiples of elementary charge.'}],
                 'diagrams':[{'figure':'11.1','type':'two-point-charges','charges':['positive','positive'],'force':'repulsive','labels':['q1','q2','F21','F12','r','rhat12','rhat21']},{'figure':'11.2','type':'two-point-charges','charges':['positive','negative'],'force':'attractive','labels':['q1','q2','F21','F12','r']}],
                 'diagramHtml':charges('phys12-f111')+charges('phys12-f112',True),
                 'figures':[{'src':'assets/physics12/coulomb-portrait.png','alt':'Portrait of Charles-Augustin de Coulomb','caption':'Charles-Augustin de Coulomb (1736–1805)'}]}])
