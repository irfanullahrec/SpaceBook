"""Printed 333, including Exercise 3.4 continuation onto next page."""
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import eq,note

def groups(items):
 out=[]
 for n,parts in items:
  out.append(heading(str(n)+'.'))
  for label,value in parts:out.append(eq('('+label+r')\;'+value))
 return out
EX33=[heading('Exercise 3.3'),*groups([
 (1,[('a',r'20(x^3-4x+2)^4(3x^2-4)'),('b',r'\frac{11}{5}(4x-x^3)^{10}(4-3x^2)'),('c',r'-2t(1-3t^2)^{-2/3}'),('d',r'\frac{-21}{(3t+1)^8}')]),
 (2,[('a',r'f′(x)=(2x-5)^2(40x-67)'),('b',r'f′(x)=\frac{x^2-2x-8}{(x-1)^2}'),('c',r'f′(x)=\frac{-12(2x-5)^3}{(x-4)^5}'),('d',r'f′(x)=\frac{4x^2+11}{(2x^2+11)^{1/2}}')]),
 (3,[('a',r'y′=\frac{3}{2}t+2'),('b',r'y′=\frac{12}{a}t^2'),('c',r'y′=\frac{b(t^2-1)}{2at}'),('d',r'y′=\frac{2t-t^4}{1-2t^3}')]),
 (5,[('a',r'-\frac{x}{y}'),('b',r'-\frac{3y^2+4xy}{2x^2+6xy}'),('c',r'-\frac{(x+y)^2}{(x+y)^2+1}'),('d',r'-\frac{y^2}{x^2}')]),
 (6,[('a',r'-\frac{2}{3}x(x^2+1)^{-4/3}'),('b',r'\frac{x^2+4x}{(x+2)^2}'),('c',r'\frac{1}{(5-x)^2}'),('d',r'\frac{-3}{(x-1)^2}')]),
 (7,[('a',r'\frac{du}{dv}=-a^2v/b^2u'),('b',r'\frac{dv}{du}=-b^2u/a^2v')])])]
# Restore printed numerical order around the text-only answer.
q5=next(i for i,b in enumerate(EX33) if b.get('text')=='5.')
EX33[q5:q5]=[heading('4.'),paragraph('4222.8 dollars/hour')]
EX33.extend([heading('8.'),paragraph('slope = 9/7'),heading('9.'),paragraph('25 miles per hour.'),note('SpaceBook clarification: the printed 3(b) gives 12t²/a, while differentiation of the exercise’s parametric equations gives 4t²/a. The checked learning solution follows the exercise.')])
EX34=[heading('Exercise 3.4'),*groups([
 (1,[('a',r'2\cos(2x)'),('b',r'-3\csc^2(3x)'),('c',r'3[\sec^2(3x)-\sin(3x)]'),('d',r'-2\cot(x)\csc^2(x)'),('e',r'\frac{1}{2\sqrt{x}}\sec^2\sqrt{x}'),('f',r'3\sin^2(x)\cos(x)')]),
 (2,[('a',r'-3x^2\csc^2(3x)+2x\cot(3x)'),('b',r'2(\sin2x+\cot3x)(2\cos2x-3\csc^2 3x)'),('c',r'-8\csc2x\cot2x'),('d',r'4(x+3)\sec^2(x+3)^2'),('e',r'\frac{\sqrt{x}\cos\sqrt{x}\sec^2x+\tan x\sin\sqrt{x}}{2\sqrt{\tan x}\cos^2\sqrt{x}}'),('f',r'\frac{2\sec^2 2x+3\cot3x(1+\tan2x)}{\csc3x}')]),
 (3,[('a',r'\frac{dy}{dx}=\frac{-1}{\sqrt{a^2-x^2}}'),('b',r'\frac{dy}{dx}=\frac{p}{p^2+x^2}'),('c',r'\frac{dy}{dx}=\frac{a}{x^2+a^2}'),('d',r'\frac{dy}{dx}=\frac{-1}{1+x^2}'),('e',r'\frac{dy}{dt}=\frac{-1}{(t+3)\sqrt{t^2+6t+8}}'),('f',r'\frac{dy}{dx}=\frac{-1}{x(x^2+1)}+\frac{1}{x^2}\tan^{-1}(\frac{x+1}{x-1})')]),
 (4,[('a',r'P′(t)=\frac{5\pi}{26}\sin(\frac{\pi}{26}t)')])]),paragraph('4. (b) P′(8) = 50 dollars/week; P′(26) = 0 dollars/week; P′(50) = −14 dollars/week.'),note('SpaceBook clarification: the key prints a plus sign between the two terms of 3(f). The checked derivative requires a minus sign on the inverse-tangent term. Exercise 3.4 Question 5 continues on printed page 334.')]
PAGES=[page('171_page_1.jpg',333,[heading('Answers'),*EX33,*EX34])]
PAGES[0].update(title='Answers — Exercises 3.3 and 3.4',visualStatus='All source formulas and rates represented digitally; source derivative discrepancies retained and explained',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':171,'side':'left'})
