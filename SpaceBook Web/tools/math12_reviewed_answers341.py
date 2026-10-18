"""Printed 341: circle keys, omissions and parabola key opening."""
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import eq,note
from math12_reviewed_answers333 import groups
EX81=[*groups([
 (2,[('a',r'x^2+y^2=25'),('b',r'x^2+y^2=36'),('c',r'x^2+y^2-12x+12y=0'),('d',r'x^2+y^2+18x+12y+117=317'),('e',r'(x+5)^2+(y-4)^2=16'),('f',r'(x-5)^2+(y-3)^2=25')]),
 (3,[('a',r'c=(4,3),\;r=4'),('b',r'c=(-2,\frac32),\;r=2\sqrt2'),('c',r'c=(-2,3),\;r=0'),('d',r'c=(\frac12,4),\;r=\sqrt{-\frac74}')]),
 (4,[('a',r'x^2+y^2-2x-21=0'),('b',r'x^2+y^2+4x+6y-72=0'),('c',r'x^2+y^2-22x-4y+25=0')]),
 (5,[('a',r'x^2+y^2-2x+2y-48=0'),('b',r'x^2+y^2-6x-8y+15=0')]),
 (6,[('a',r'5x^2+5y^2+12x-15y=0'),('b',r'x^2+y^2-3x+y=0')]),
 (7,[('a',r'16x^2+16y^2+128x-56y+49=0'),('b',r'x^2+y^2-8x-4=0'),('c',r'x^2+y^2+6x-10y+9=0')]),
 (8,[('a',r'x^2+y^2=25'),('b',r'x^2+y^2=20')])]),note('SpaceBook clarification: a zero radius in 3(c) is a point locus, and the negative radius square in 3(d) gives no real circle. Original key forms are retained; the learning solutions distinguish these degenerate cases.')]
EX82=[heading('Exercise 8.2'),heading('1.'),paragraph('(a) equation of tangent: x + 2y = 5; equation of normal: 2x − y = 0.'),paragraph('(b) equation of tangent: 3x + 2y + 13 = 0; equation of normal: 2x + 3y = 0.'),paragraph('(c) equation of tangent: x + y − 5 = 0; equation of normal: y − x = −3.'),heading('2.'),eq(r'(a)\;\text{tangent: }18x+18\sqrt3y=13'),eq(r'\text{normal: }18\sqrt3x+18y=0'),eq(r'(b)\;\text{tangent: }x+y-2\sqrt2=0\quad\text{normal: }x-y=0'),eq(r'(c)\;\text{tangent: }\sqrt3x+y-2=0\quad\text{normal: }x-\sqrt3y=0'),*groups([
 (3,[('a',r'n=\pm a\sqrt{m^2+l^2}'),('b',r'n=\pm3\sqrt2'),('c',r'n=\pm18\sqrt2')]),
 (4,[('a',r'c=\pm a\sqrt{1+m^2}'),('b',r'c=\pm3\sqrt2'),('c',r'c=\pm9a\sqrt2')]),
 (5,[('a',r'g^2m^2+f^2l^2-2lng-2gflm-n^2+2fnm-m^2c-cl^2=0')]),
 (6,[('a',r'n=7,-43'),('b',r'n=4.52;-13.52')]),
 (10,[('a',r'y=-\frac12x\pm\sqrt5'),('b',r'3x+4y=25')]),
 (12,[('a',r'y=x\pm2'),('b',r'y=\frac{x}{\sqrt3}\pm\frac23'),('c',r'y=\sqrt3x\pm\frac{\sqrt{13}}2')])])]
i=next(i for i,b in enumerate(EX82) if b.get('text')=='10.')
EX82[i:i]=[paragraph('6. (c) Does not touch the circle'),eq(r'C=\frac{-152\pm\sqrt{14721}}{32}'),note('Source-layout note: this additional capital-C expression is printed at the far right beside the Question 6 area without an explicit part label. It is preserved as an unassigned key formula rather than attached to an inferred question.')]
EX82.extend([note('SpaceBook clarification: 1(b) has the wrong sign in its normal. Part 2(a) gives an off-circle point and therefore has no at-point tangent/normal for the printed circle. The key also contains discrepancies in its symbolic tangent condition, 4(c), 6(c), 10(b) and 12(c); the checked exercise solutions preserve the source givens and use valid tangent-distance conditions. The key omits Questions 7–9 and 11.')])
REVIEW8=[heading('Review Exercise 8'),heading('1.'),paragraph('(i) d; (ii) d; (iii) c; (iv) a; (v) a; (vi) d; (vii) b; (viii) d; (ix) c; (x) b.'),note('SpaceBook clarification: items (ii) and (iii) do not offer generally correct center/radius expressions as printed. The selected key letters are retained independently from the checked learning explanations.')]
EX91=[heading('Unit-9'),heading('Exercise 9.1'),heading('1. (a)'),paragraph('Vertex (0,0), focus (0, 1/2), ends of latus rectum A(−1, 1/2), B(1, 1/2), axis of symmetry: x = 0 (y-axis).')]
PAGES=[page('175_page_1.jpg',341,[heading('Answers'),*EX81,*EX82,*REVIEW8,*EX91])]
PAGES[0].update(title='Answers — Circle keys and parabola opening',visualStatus='Every available equation and source statement represented natively; unassigned formula and omitted questions disclosed',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':175,'side':'left'})
