"""Printed 323: full quadrature exercise, interval convention and source history."""
from math12_reviewed_unit1 import heading,paragraph,page,figure
from math12_reviewed_higher_derivatives import note
FIGURE_PDF_CROPS=[(166,'numerical323-simpson',(594,809,737,948))]
QUESTIONS=[
'Use trapezoidal rule, round to nearest hundredth and compare with exact values: (a) ∫₁³x² dx, n=4; (b) ∫₀¹(x²/2+1) dx, n=4; (c) ∫₁³ dx/x, n=6; (d) ∫₀²√(1+x²) dx, n=6.',
'Use Simpson’s rule, round to nearest hundredth and compare with exact values: (a) ∫₂⁴x² dx, n=3; (b) ∫₂³(x²/3−1) dx, n=4; (c) ∫₂³ dx/x, n=3; (d) ∫₀¹e^(2x) dx, n=4.',
'A radius-one quarter circle is y=√(1−x²), 0≤x≤1. Thus ∫₀¹√(1−x²) dx=π/4, n=4. Approximate the left integral by trapezoidal rule; the source says it equals the right side when π=3.1.',
'For the same quarter-circle integral and n=4, approximate by Simpson’s rule; the source says it equals the right side when π=3.1.',
'Use MAPLE commands to find approximate area on [0,2] by (a) trapezoidal rule and (b) Simpson’s rule. [No integrand is supplied on this source question.]'
]
STEPS=[
 ['For n=N subintervals use h=(b−a)/N and T_N=(h/2)[f₀+2Σ interior fᵢ+f_N]. Compare each result with its own exact integral.','(a) h=1/2, nodes 1,1.5,2,2.5,3 and values 1,2.25,4,6.25,9. T₄=8.75; exact [x³/3]₁³=26/3≈8.66666667→8.67.','(b) h=1/4 and nodes 0,1/4,1/2,3/4,1. T₄=1.171875→1.17; exact [x³/6+x]₀¹=7/6≈1.16666667→1.17.','(c) h=1/3, nodes 1,4/3,5/3,2,7/3,8/3,3. Values are 1,3/4,3/5,1/2,3/7,3/8,1/3. T₆≈1.10674603→1.11; exact ln3≈1.09861229→1.10.','(d) h=1/3, nodes 0,1/3,2/3,1,4/3,5/3,2. Summing √(1+xᵢ²) with trapezoid weights gives T₆≈2.96616928→2.97.','The exact value in (d) is [x√(1+x²)+asinh x]/2 from 0 to 2, namely √5+(1/2)ln(2+√5)≈2.95788572→2.96.','The signed errors exact minus approximate are approximately −0.08333333,−0.00520833,−0.00813374,−0.00828356. Matching rounded values in (b) does not imply zero actual error.'],
 ['The chapter’s Simpson convention uses n two-interval panels, so N=2n subintervals and h=(b−a)/(2n). This permits the printed odd panel counts n=3. Under a convention where n counts subintervals, those odd counts would be invalid.','Use S_N=(h/3)[f₀+4Σ odd fᵢ+2Σ interior even fᵢ+f_N].','(a) n=3 means N=6,h=1/3. For x² Simpson is exact: S₆=56/3≈18.66666667→18.67, equal to [x³/3]₂⁴.','(b) n=4 means N=8,h=1/8. The quadratic x²/3−1 is also integrated exactly: S₈=10/9≈1.11111111→1.11.','(c) n=3 means N=6,h=1/6. The weighted sum for 1/x gives S₆≈0.40546637→0.41. Exact ln(3/2)≈0.40546511→0.41; actual error is about −0.00000127, despite equal rounding.','(d) n=4 means N=8,h=1/8. The weighted exponential sum gives S₈≈3.19459686→3.19. Exact (e²−1)/2≈3.19452805→3.19, with signed error about −0.00006881.','Keep the panel/subinterval interpretation explicit rather than applying Simpson to an odd number of subintervals or silently changing the printed n.'],
 ['Use four trapezoidal subintervals, h=1/4, over [0,1].','At x=0,1/4,1/2,3/4,1 the heights are 1,√15/4,√3/2,√7/4,0.','Thus T₄=(1/8)[1+2(√15/4+√3/2+√7/4)]≈0.7489272670.','The exact quarter-circle area is π/4≈0.7853981634, so the trapezoid underestimates it.','If π is estimated as 4T₄, the result is approximately 2.9957090681, rounding to 3.0 at one decimal place.','Therefore the source claim π=3.1 does not follow from these four trapezoids. Using a different count, such as eight subintervals, gives a different estimate; it must not silently replace the source n=4.'],
 ['The chapter uses n for Simpson panels; n=4 then gives N=8 subintervals, h=1/8.','Evaluate √(1−xᵢ²) at xᵢ=i/8 and apply Simpson weights 1,4,2,…,4,1.','The resulting S₈≈0.7802972924 gives π≈4S₈≈3.1211891698, rounding to 3.1 at one decimal place.','If instead the printed n=4 means four subintervals under the other convention, S₄≈0.7708987887 and 4S₄≈3.0835951549 also rounds to 3.1.','Neither quadrature area is exactly 3.1/4=0.775; the equality in the source should be read as a coarse rounded π estimate, not exact numerical equality.','The exact area is π/4≈0.7853981634. The integrand’s derivative becomes unbounded at x=1, so usual bounded-smooth-derivative error formulas do not apply without that qualification.'],
 ['The source supplies only the interval [0,2], not f(x), so there is no uniquely determined area or numerical result.','To demonstrate the requested workflow, choose the explicitly supplemental sample f(x)=e^(−x), nonnegative on [0,2]. This is a learning example, not recovered missing source content.','Source-style sample commands are ApproximateInt(exp(-x),x=0..2,method=trapezoid,output=plot); and ApproximateInt(exp(-x),x=0..2,method=simpson,output=plot); after with(Student[Calculus1]):. No software execution or default partition count is claimed.','Independently choose N=10 equal subintervals, h=0.2. The trapezoid sum is T₁₀≈0.8675450128.','The corresponding Simpson sum with N=10 is S₁₀≈0.8646723662. Exact integration gives 1−e^(−2)≈0.8646647168.','A different chosen f or partition gives different answers. The original problem remains under-specified; the sample merely shows how to carry out a specified quadrature task.']
]
ANSWERS=['T approximations: (a) 8.75; (b) 1.17; (c) 1.11; (d) 2.97. Exact rounded: 8.67,1.17,1.10,2.96.','Using n panels/N=2n: (a) 18.67; (b) 1.11; (c) 0.41; (d) 3.19, with exact comparisons above.','T₄≈0.7489272670; inferred π≈2.9957090681≈3.0, contradicting the printed 3.1.','n=4 panels: S₈≈0.7802972924, inferred π≈3.1211891698≈3.1; four-subinterval alternative also shown.','No unique source answer: integrand missing. Supplemental e^(−x), N=10: T₁₀≈0.8675450128, S₁₀≈0.8646723662.']
HISTORY=[heading('History'),figure('numerical323-simpson','Thomas Simpson (1710–1761)','Source portrait of Thomas Simpson.'),paragraph('Thomas Simpson was a British mathematician and creator of Simpson’s rule for approximate definite integrals. This rule was known and used earlier by Bonventura Cavalieri in 1639 and later by James Gregory. The long popularity of Simpson’s textbook invites this association with his name therefore many readers would have learnt it from them. A challenge proposed by ‘Pierre de Fermat’ to find a point ‘D’ such that the sum of the distances to the three given points A,B and C is least. This challenge was popularized in Italy Sampson treats this challenge in this first part of Doctrine and application of Fluxions (1750) by the description of circular arc at which the edges of the triangle ABC subtend an angle of π/3. In second part of the book he extends this geometrical method. Sampson’s several textbooks contains most of the optimization problems treated by simple techniques.'),note('This history passage is preserved as printed source wording; historical attributions and spellings are not independently verified here.')]
PAGES=[page('166_page_1.jpg',323,[heading('Exercise 12.2')]+[paragraph(str(i)+'. '+q) for i,q in enumerate(QUESTIONS,1)]+[note('The source Simpson n convention is panel-based in its worked example, and Question 5 omits its integrand. These ambiguities remain visible; a supplemental sample is distinguished from a textbook answer.')]+HISTORY)]
PAGES[0].update(title='INTRODUCTION TO NUMERICAL METHODS',visualStatus='All five native quadrature groups, quarter-circle identity and source history portrait',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':166,'side':'left','reason':'All bounds, panel counts, quarter-circle wording and missing-integrand question visually checked; sums independently calculated'})

import math
from math12_native_geometry import geometry,path
def quarter_graph(simpson=False):
 n=8 if simpson else 4
 def pt(x,y):return(80+330*x,275-220*y)
 f=lambda x:math.sqrt(max(0,1-x*x))
 paths=[]
 for i in range(0,n,2 if simpson else 1):
  if simpson:
   y0,y1,y2=[f((i+j)/n) for j in range(3)]
   arc=[]
   for k in range(41):
    t=k/20;y=y0*(t-1)*(t-2)/2-y1*t*(t-2)+y2*t*(t-1)/2;arc.append(pt((i+t)/n,y))
  else:arc=[pt(i/n,f(i/n)),pt((i+1)/n,f((i+1)/n))]
  end=(i+(2 if simpson else 1))/n
  paths.append(path([pt(i/n,0)]+arc+[pt(end,0),pt(i/n,0)],fill='#ffedd5',stroke='#ea580c'))
 paths.extend([path([pt(i/160,f(i/160)) for i in range(161)],stroke='#0369a1'),path([pt(-.08,0),pt(1.12,0)]),path([pt(0,-.06),pt(0,1.13)])])
 labels=[(453,281,'x'),(74,22,'y'),(268,39,'y=√(1−x²)')]
 for v in [0,.25,.5,.75,1]:
  xx,yy=pt(v,0);labels.append((xx-8,yy+24,str(v)))
  if v:xx,yy=pt(0,v);labels.append((xx-39,yy+5,str(v)))
 return geometry('SpaceBook learning diagram — quarter-circle '+('Simpson, 8 subintervals' if simpson else 'trapezoid, 4 subintervals'),'Quarter-circle exact curve overlaid with '+('four quadratic Simpson panels' if simpson else 'four trapezoids'),paths,labels,size=(505,325))
SOLUTION_GRAPHS={3:[quarter_graph()],4:[quarter_graph(True)]}
