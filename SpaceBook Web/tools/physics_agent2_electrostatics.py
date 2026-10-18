from physics_agent2_sequential import save_page

OUTCOMES1 = [
    'How electrostatics important to us?',
    'After studying this unit the students will be able to',
    "state Coulomb's law and explain that force between two point charges is reduced in a medium other than free space using Coulomb's law.",
    r'derive the expression \(E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\) for the magnitude of the electric field at a distance r from a point charge q.',
    'describe the concept of an electric field as an example of a field of force.',
    'define electric field strength as force per unit positive charge.',
    r'solve problems and analyse information using \(E=F/q\).',
    r'solve problems involving the use of the expression \(E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\).',
    'calculate the magnitude and direction of the electric field at a point due to two charges with the same or opposite signs.',
    'sketch the electric field lines for two point charges of equal magnitude with same or opposite signs.',
]

if __name__ == '__main__':
    save_page(5,[{'id':'phys12-front-contents','printedPage':None,'title':'Table of contents','paragraphs':[],
                 'rows':[['Units','Pages'],['11 Electrostatics',1],['12 Current electricity',52],['13 Electromagnetism',88],['14 Electromagnetic induction',126],['15 Alternating current',156],['16 Physics of solids',202],['17 Electronics',230],['18 Dawn of the modern physics',254],['19 Atomic Spectra',297],['20 Nuclear physics',333],['Glossary',383]]},
                {'id':'phys12-front-outcomes1','printedPage':1,'title':'Unit 11: Electrostatics — Learning outcomes (1)','paragraphs':OUTCOMES1,'kind':'learning_outcomes',
                 'objectives':OUTCOMES1[2:]}])
