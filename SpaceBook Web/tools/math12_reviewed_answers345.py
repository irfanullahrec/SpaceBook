"""Printed 345: transformed conics and differential-equation keys."""
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import eq,note
from math12_reviewed_answers333 import groups
EX94=[heading('Exercise 9.4'),*groups([
 (1,[('a',r'2X-Y=0'),('b',r'X^2+Y^2=4'),('c',r'X^2+2Y^2=16'),('d',r'X^2+Y-3XY+1=0')]),
 (2,[('a',r'2XY+a^2=0'),('b',r'X^2=-4pY'),('c',r'3X^2-Y^2-1=0'),('d',r'XY+6X+4Y-1=0')]),
 (3,[('a',r'3X^2+2Y^2=5'),('b',r'-X^2+4Y^2=1'),('c',r'6X^2-19Y^2=25')]),
 (4,[('a',r'\theta=36.87°'),('b',r'\theta=-30°')])])]
EX101=[heading('Unit-10'),heading('Exercise 10.1'),heading('1.'),paragraph('(a) order = degree = 1; (b) order = 2, degree = 1; (c) order = 3, degree = 1; (d) order = 2, degree = 1.'),heading('2.'),paragraph('(a) y is a solution, since the substitution of y and its derivative y′ reduce the differential equation into an identity.'),paragraph('(b) y is a solution; (c) y is a solution.'),paragraph('(d) y is not a solution, since the substitution of y and its derivative y′ does not reduce the differential equation into an identity.'),*groups([
 (3,[('a',r'xy=2'),('b',r'y=x-x\ln x+1'),('c',r'\sin(xy)=0.7071'),('d',r'\frac{y^2}{x}=\frac{x^2}{2}+\frac12')]),
 (4,[('a',r'y=\sin x+1'),('b',r'f=\frac13x^3+1'),('c',r'y=-\frac1x+\frac12'),('d',r'y=\frac1{8-x^2}')])]),heading('5.'),paragraph('276 students'),note('Source-legibility note: the affirmative key for 2(c) does not resolve the smudged exponent in the exercise’s differential equation. Its exact source fragment remains marked partial; conditional verification is labelled separately. Question 3(c) uses a rounded sine value, whereas the checked initial-condition solution retains the exact value and branch.')]
EX102=[heading('Exercise 10.2'),*groups([
 (1,[('a',r'y=\pm\sin(x+c)'),('b',r'y=\frac{-1}{e^{-x}+c}'),('c',r'y=\sin(\sin^{-1}x+c)'),('d',r'y=\sin^{-1}[\frac{\sin2x}{4}-\frac{x}{2}+c]')]),
 (2,[('a',r'y=\tan(x+c)-x'),('b',r'y=\sin^{-1}(e^xc_1)-x'),('c',r'y=\frac{-x}{\ln x+c}'),('d',r'y=x(\frac{3x^2}{2}+c_2)^{1/3}')]),
 (3,[('a',r'\tan^{-1}(\frac yx)-\frac12\ln(1+\frac{y^2}{x^2})=\ln(x)+c'),('b',r'y=\frac{x}{\ln(x)+c}'),('c',r'y=\pm x\sqrt{-1+cx}'),('d',r'-\frac{x^2}{2y^2}-\frac xy+\ln(y)=c')]),
 (4,[('a',r'y=\frac14x^2-1'),('b',r'\frac{x^2\ln(x)}{1+\ln(x)}')]),
 (5,[('',r'y=\frac{x-13}{x-1}')]),
 (6,[('',r'(\frac{2y^2}{x^2}+1)^{1/4}=9^{1/4}x')]),
 (7,[('',r'\ln x+e^{-y/x}=1')])]),note('SpaceBook clarification: the key omits equilibrium solutions and branch/domain restrictions from several families. In 2(d), the checked family is y=x∛(3ln|x|+C), rather than the printed x² expression. Entry 4(b) is y² for the geometrical branches; its initial y=0 does not permit a classical finite-derivative solution of the printed equation. In 6, the negative-x initial interval requires |x| in the root relation. The key continues on page 346.')]
PAGES=[page('177_page_1.jpg',345,[heading('Answers'),*EX94,*EX101,*EX102])]
PAGES[0].update(title='Answers — Rotated conics and differential equations',visualStatus='All original key formulas transcribed natively, with unresolved exercise fragment, branches and key-family errors distinguished',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':177,'side':'left'})
