"""Printed 344: all hyperbola key diagrams and formulas retained."""
import math
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import eq,note
from math12_reviewed_answers333 import groups
from math12_reviewed_answers343 import hyperbola
GC=hyperbola('c',3,4,h=2,k=3,point_labels=[(-1,3,'V₁(−1,3)'),(5,3,'V₂(5,3)'),(-3,3,'F₂(−3,3)'),(7,3,'F₁(7,3)')],asym_labels=[(330,68,'y=(3/2)x'),(330,440,'y=−(3/2)x')])
GD=hyperbola('d',4,5,vertical=True,h=-3,k=-1,point_labels=[(-3,3,'V₂(−3,3)'),(-3,-5,'V₁(−3,−5)'),(-3,-1+math.sqrt(41),'F₁(−3,−1+√41)'),(-3,-1-math.sqrt(41),'F₁(−3,−1−√41)')])
G6A=hyperbola('6a',1,1,h=-1,k=2,point_labels=[(-2,2,'V₁(−2,2)'),(0,2,'V₂(0,2)')],caption='Printed answer 9.3, Q6 (a)')
G6A['diagram']['labels'][0]['text']='C(−1,−2)'
G6B=hyperbola('6b',2,2,h=3,k=-1,point_labels=[(1,-1,'V₁(1,−1)'),(5,-1,'V₂(5,−1)')],caption='Printed answer 9.3, Q6 (b)')
EX93=[heading('1. (c)'),GC,paragraph('Centre C(2,3); Vertices V₁(−1,3), V₂(5,3); Foci F₁(−3,3), F₂(7,3).'),eq(r'\text{Asymptotes: }y-3=\pm\frac43(x-2)'),heading('1. (d)'),GD,paragraph('Centre C(−3,−1); Vertices V₁(−3,−5), V₂(−3,3); Foci F₁(−3,−1−√41), F₂(−3,−1+√41).'),eq(r'\text{Asymptotes: }y+1=\pm\frac45(x+3)'),note('Source-diagram note: graph (c) copies unshifted y=±(3/2)x labels although its accompanying text gives the shifted ±4/3 asymptotes. Its F₁/F₂ names are also reversed relative to the text. Graph (d) calls both foci F₁. The native graphs retain these printed names and labels, while their curves follow the matching exercise equations.'),*groups([
 (2,[('a',r'\frac{x^2}{16}-\frac{y^2}{4}=1'),('b',r'\frac{y^2}{25}-\frac{x^2}{16}=1'),('c',r'\frac{(x-4)^2}{9}-\frac{4(y-2)^2}{9}=1'),('d',r'\frac{(y+2)^2}{9}-\frac{(x+5)^2}{16}=1')]),
 (3,[('a',r'\frac{y^2}{4}-\frac{x^2}{5}=1'),('b',r'\frac{x^2}{25}-\frac{y^2}{24}=1'),('c',r'9x^2-y^2=9'),('d',r'16x^2-9y^2=144'),('e',r'\frac{(x-1)^2}{4}-\frac29(y+1)^2=1')]),
 (4,[('a',r'\frac{x^2}{16}-\frac{y^2}{9}=1'),('b',r'\frac{y^2}{25}-\frac{x^2}{144}=1')]),
 (5,[('a',r'\frac{(x+1)^2}{9}-\frac{(x+2)^2}{3}=1'),('b',r'\frac{(y-1)^2}{81}-\frac{(x+1)^2}{16}=1')])]),heading('6. (a)'),G6A,paragraph('Vertices V₁(−2,27), V₂(0,2); Foci F₁(−√2−1,2), F₂(√2−1,2).'),eq(r'\text{Asymptotes: }y-2=\pm1(x+1)'),heading('6. (b)'),G6B,paragraph('Vertices V₁(1,−1), V₂(5,−1); Foci F₁(−√2+3,−1), F₂(√2+3,−1).'),eq(r'\text{Asymptotes: }y+1=\pm(x-3)'),*groups([
 (7,[('a',r'P_1(4,1),\;P_2(-1,-4)'),('b',r'P_1(0,1),\;P_2(-\frac83,\frac53)')]),
 (8,[('a',r'c=\pm2\sqrt3'),('b',r'c=\pm\sqrt7')]),
 (9,[('a',r'\text{tangent: }\sqrt{13}x+2y+4=0'),('a normal',r'4x-2\sqrt{13}y+13\sqrt{13}=0'),('b',r'\text{tangent: }y=\frac{3x}{5}+\frac95'),('b normal',r'y=\frac{5x}{3}+\frac{125}{9}')])]),note('SpaceBook clarification: 5(a) repeats x where its conic needs a y term. In 6(a), the graph’s center sign and text vertex “27” conflict with the actual center (−1,2) and vertex (−2,2). In 6(b), the matching equal-axis hyperbola has foci (3±2√2,−1), not (3±√2,−1). Question 9(b) specifies an off-curve contact, so its at-point tangent/normal is undefined; the key’s claimed lines are preserved separately. Exercise 9.3 continues on page 345.')]
PAGES=[page('176_page_2.jpg',344,[heading('Answers'),*EX93])]
PAGES[0].update(title='Answers — Hyperbolas continued',visualStatus='Four labelled native hyperbola diagrams and all key formulas; contradictory labels, vertices and conic variables preserved with clarification',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':176,'side':'right'})
