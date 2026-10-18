"""Add verified textbook exercise solutions to the Class 12 data file."""
from pathlib import Path
import json
import re

ROOT = Path(r"D:\SpaceBook\SpaceBook Web")
DATA = ROOT / "js" / "math_12_data.js"
text = DATA.read_text(encoding="utf-8")
start = text.index("const MATH_12_DATA = [") + len("const MATH_12_DATA = ")
end = text.index("\n];\nif (typeof DATA", start) + 2
units = json.loads(text[start:end])

def q(id_, no, question, solution, diagram=None):
    return {"id": id_, "qNo": str(no), "question": question,
            "solution": solution, "diagram": diagram}

u2 = units[1]
ex21 = next(e for e in u2["exercises"] if e["id"] == "ex-2-1")
ex21["problems"] = [
    q("ex-2-1-q1", 1,
      "Read each of the six graphs in the book and state its function, domain, and range.",
      "From the plotted curves and the answer section: (a) domain ℝ; range (−∞, 5]. (b) domain ℝ; range ℝ. (c) domain ℝ\\{−2}; range ℝ\\{0}. (d) domain ℝ; range ℝ. (e) domain ℝ; range [0, ∞). (f) domain ℝ; range [0, ∞). For each graph, the function is identified by its plotted curve: (a) downward-opening parabola, (b) increasing straight line, (c) reciprocal-type hyperbola with asymptotes x = −2 and y = 0, (d) straight line, and (e)–(f) upward/nonnegative curves. The scan does not print an algebraic formula for these six plotted functions.",
      None),
    q("ex-2-1-q2", 2,
      "Sketch each graph and give its domain and range: (a) y = 2|x − 3|, (b) y = 4|x − 3| + 3, (c) y = 5|3x + 7| − 2, (d) y = 2|4x + 3| + 1.",
      "Each absolute-value graph is V-shaped and has domain ℝ. (a) The vertex is (3, 0), so the range is [0, ∞). (b) The vertex is (3, 3), so the range is [3, ∞). (c) Since 3x + 7 = 0 at x = −7/3, the vertex is (−7/3, −2), so the range is [−2, ∞). (d) Since 4x + 3 = 0 at x = −3/4, the vertex is (−3/4, 1), so the range is [1, ∞). The positive coefficients outside the absolute values make all four graphs open upward.",
      {"type": "absolute-value-set", "title":"Exercise 2.1, Question 2", "functions":[
          {"a":2,"b":1,"c":-3,"d":0,"label":"(a)"},
          {"a":4,"b":1,"c":-3,"d":3,"label":"(b)"},
          {"a":5,"b":3,"c":7,"d":-2,"label":"(c)"},
          {"a":2,"b":4,"c":3,"d":1,"label":"(d)"}
      ]}),
    q("ex-2-1-q3", 3,
      "Find f(g(x)) and g(f(x)): (a) f(x) = x² + 1, g(x) = 2x; (b) f(x) = sin x, g(x) = 1 − x²; (c) f(x) = (x − 1)/(x + 1), g(x) = (x + 1)/(1 − x); (d) f(x) = sin x, g(x) = 2x + 3.",
      "(a) f(g(x)) = (2x)² + 1 = 4x² + 1; g(f(x)) = 2(x² + 1) = 2x² + 2.\n(b) f(g(x)) = sin(1 − x²); g(f(x)) = 1 − sin²x = cos²x.\n(c) f(g(x)) = x and g(f(x)) = x, where the expressions are defined.\n(d) f(g(x)) = sin(2x + 3); g(f(x)) = 2 sin x + 3."),
    q("ex-2-1-q4", 4,
      "For each pair, find f(g(x)) and g(f(x)), then determine the inverse of each composite: (a) f(x) = x + 5, g(x) = x − 4; (b) f(x) = 2x + 7, g(x) = 2x; (c) f(x) = 2(x − 4), g(x) = (x + 5)/2; (d) f(x) = (x + 4)/2, g(x) = 2x − 4.",
      "(a) Both composites are x + 1. Set y = x + 1 and solve for x: the inverse is y − 1, so each inverse is x − 1.\n(b) f(g(x)) = 4x + 7, whose inverse is (x − 7)/4. g(f(x)) = 4x + 14, whose inverse is (x − 14)/4.\n(c) f(g(x)) = x − 3, whose inverse is x + 3. g(f(x)) = x − 3/2, whose inverse is x + 3/2.\n(d) Both composites simplify to x, so each is self-inverse and its inverse is x."),
    q("ex-2-1-q5", "Project", "Observe the two printed graphs and identify the domain and range of each.",
      "For each picture, trace the graph from its leftmost to rightmost plotted x-coordinate to obtain the domain, then from its lowest to highest y-coordinate to obtain the range. The exact endpoints must be read from the printed graphs on page 31.",
      None)
]

ex22 = next(e for e in u2["exercises"] if e["id"] == "ex-2-2")
ex22["problems"] = [
    q("ex-2-2-q1", 1, "Classify: (a) y=sin²x+x; (b) y=7x⁴+3x²−4x+5; (c) y=arctan x−7; (d) y=log₂16+7log₂x; (e) x²+y²=36; (f) y=(e^{3x}+e^{−3x})/(e^{3x}−e^{−3x}); (g) y=√(x−8).",
      "(a) Trigonometric; (b) polynomial; (c) inverse trigonometric; (d) logarithmic; (e) implicit relation (a circle); (f) hyperbolic; (g) radical/algebraic. These classifications follow from the defining form of each expression."),
    q("ex-2-2-q2", 2, "A sealed container has radium amount Q(t) = 100e^{−0.00043t} grams, where t is measured in years. Find Q(0), Q(800), Q(1600), and Q(5000), and describe the result.",
      "Substitute each time into Q(t). Q(0)=100e^0=100 g. Q(800)=100e^{−0.344}≈70.9 g. Q(1600)=100e^{−0.688}≈50.2 g. Q(5000)=100e^{−2.15}≈11.6 g. The amount decreases as time passes because the exponent is a negative multiple of t."),
    q("ex-2-2-q3", 3, "Use point-by-point plotting for (a) h(x)=2^x, −5≤x≤0; (b) m(x)=3^{−x}, 0≤x≤3; (c) N=e^x, 0≤x≤5; (d) N=e^{−x}, 0≤x≤5.",
      "Evaluate each function at the endpoints and intermediate integer x-values, then plot the ordered pairs. (a) 2^x increases from 1/32 to 1. (b) 3^{−x} decreases from 1 to 1/27. (c) e^x increases from 1 to e^5. (d) e^{−x} decreases from 1 to e^{−5}. All four curves remain positive and have horizontal asymptote y=0."),
    q("ex-2-2-q4", 4, "Use point-by-point plotting for the logarithmic functions shown in Exercise 2.2, Question 4 (a–f).",
      "The six functions are logarithmic transformations. Their vertical asymptotes and domains are: (a) y=ln x: x=0, domain (0,∞); (b) u=−ln x: x=0, domain (0,∞); (c) y=2ln(x+2): x=−2, domain (−2,∞); (d) y=4ln(x−3): x=3, domain (3,∞); (e) y=4ln x−2: x=0, domain (0,∞); (f) y=4ln(x−2): x=2, domain (2,∞). Plot by evaluating valid x-values on each side of the asymptote, never at the asymptote."),
    q("ex-2-2-q5", 5, "Sketch the parametric curves: (a) x=3−t², y=2t, t∈ℝ; (b) x=4cos t, y=−3sin t.",
      "(a) Eliminate t: t=y/2, so x=3−y²/4. This is a left-opening parabola with vertex (3,0). (b) Divide x=4cos t by 4 and y=−3sin t by −3; adding the squares gives x²/16+y²/9=1, an ellipse centered at the origin with horizontal semiaxis 4 and vertical semiaxis 3.",
      None),
    q("ex-2-2-q6", 6, "Sketch the graphs: (a) e^{−2x}; (b) (2/3)e^{2x}; (c) 4^x; (d) 4^{−x}; (e) log₂(x+5); (f) log₂(x²); (g) log₂(2x−5).",
      "Each exponential has domain ℝ and horizontal asymptote y=0. (a),(d) decrease; (b),(c) increase. For the logarithms, identify the positive argument: (e) domain x>−5 and vertical asymptote x=−5; (f) domain x≠0 with vertical asymptote x=0 on both sides; (g) domain x>5/2 and vertical asymptote x=5/2. Use the standard logarithm graph and apply the stated shifts/scales."),
    q("ex-2-2-q7", 7, "Sketch: (a) x²+y²=4; (b) x²+y²=16; (c) x²/25+y²/9=1; (d) x²/36+y²/9=−1.",
      "(a) Circle centered at (0,0), radius 2. (b) Circle centered at (0,0), radius 4. (c) Ellipse centered at the origin with semiaxes 5 (horizontal) and 3 (vertical); vertices are (±5,0), co-vertices (0,±3). (d) There are no real points because a sum of nonnegative terms cannot equal −1; its real graph is empty."),
    q("ex-2-2-q8", 8, "Use Maple commands to plot the graphs of the functions in Question 1.",
      "For each expression, enter the function in Maple and use plot(function, x=a..b) with a suitable interval. For implicit relations such as x²+y²=36, use an implicit plot with both x and y ranges. The plot is checked by comparing its shape and domain with the classifications in Question 1.")
]

ex24 = next(e for e in u2["exercises"] if e["id"] == "ex-2-4")
ex24["problems"] = [
    q("ex-2-4-q1", 1, "Use continuity properties to test: (a) f(x)=2x−3; (b) h(x)=2/(x−5); (c) g(x)=(x−5)/((x−3)(x+2)).",
      "(a) A polynomial is continuous for every real x. (b) A rational function is continuous wherever its denominator is nonzero, so h is continuous on (−∞,5) and (5,∞), and discontinuous at x=5. (c) The denominator is zero at x=3 and x=−2; g is continuous on each interval that excludes these points and discontinuous at both."),
    q("ex-2-4-q2", 2, "Show that f(x)=sin x/x for x≠0 and f(0)=1 is continuous at x=0.",
      "By definition, continuity at 0 requires lim_{x→0} f(x)=f(0). The standard trigonometric limit gives lim_{x→0}(sin x)/x=1, and f(0)=1. Therefore the limit equals the function value, so f is continuous at 0."),
    q("ex-2-4-q3", 3, "Use the graph of g(x) to answer the continuity and one-sided continuity questions at x=−1 and x=2 in parts (a–d).",
      "Read the plotted point and the approaching curve at each marked x-value. The answer key states: g is continuous on (−1,2); it is continuous from the right at x=−1; it is continuous from the left at x=2; and it is continuous on [−1,2]. Check the endpoint equalities using the one-sided limits shown by the graph.",
      None),
    q("ex-2-4-q4", 4, "Use the graph of f(x) to answer the continuity and one-sided continuity questions on [0,3].",
      "From the graph and answer key: f is continuous on (0,3), continuous from the right at x=0, continuous from the left at x=3, and continuous on the closed interval [0,3]. Continuity on the closed interval uses the right-hand limit at the left endpoint and the left-hand limit at the right endpoint.",
      None),
    q("ex-2-4-q5", 5, "Graph each piecewise function and locate all points of discontinuity: (a) f(x)=1+x for x<1; 5−x for x≥1. (b) f(x)=−x for x<0; 1 for x=0; x for x>0.",
      "(a) At x=1, the left-hand limit is 2, while f(1)=4; therefore there is a jump discontinuity at x=1. Each branch is linear and continuous elsewhere. (b) Both one-sided limits at 0 equal 0, but f(0)=1; hence there is a removable discontinuity at x=0. Elsewhere each branch is continuous.",
      None),
    q("ex-2-4-q6", 6, "A salesperson earns a $1,000 monthly base salary and 5% commission on sales over $10,000; at sales of $20,000 or more an additional $500 bonus is paid. Define E(s), graph it, and answer the limit/value and continuity questions in parts (a–d).",
      "A piecewise model is E(s)=1000 for 0≤s≤10000; E(s)=1000+0.05(s−10000) for 10000<s<20000; E(s)=1500+0.05(s−10000) for s≥20000. At s=10000, E=1000 and both adjoining values approach 1000, so it is continuous there. At s=20000, the value jumps from the left-hand limit 1500 to E(20000)=2000; the two-sided limit does not exist, so it is discontinuous there. The graph consists of the base segment, a rising commission segment, then an upward $500 jump followed by the same slope."),
    q("ex-2-4-q7", 7, "Use Maple’s iscont command to test whether f(x)=(x²+1)/(x²+2.7) is continuous on [−5,5].",
      "The denominator x²+2.7 is positive for every real x, so the rational function has no singularity on [−5,5] and is continuous throughout that interval. Maple’s iscont command therefore returns true.")
]

ex23 = next(e for e in u2["exercises"] if e["id"] == "ex-2-3")
ex23["problems"] = [
    q("ex-2-3-q1", 1, "Evaluate: (a) lim_{x→4}(3/x+1/(x−5)); (b) lim_{x→1}((x²+3x+2)/(x²+x+2))²; (c) lim_{x→1}(√x−1)/(x−1); (d) lim_{x→1}(1/x−1)/(x−1); (e) lim_{x→0}(1−sin x)/cos²x; (f) lim_{x→0}tan x/x; (g) lim_{x→0}(sec x−1)/(x sec x); (h) lim_{x→0}sin²(7x)/(7x).",
      "(a) 3/4+1/(−1)=−1/4. (b) ((1+3+2)/(1+1+2))²=(6/4)²=9/4. (c) Rationalize: 1/(√x+1)→1/2. (d) (1−x)/(x(x−1))=−1/x→−1. (e) Direct substitution gives 1. (f) The standard limit is 1. (g) Since (sec x−1)/(x sec x)=(1−cos x)/x→0. (h) sin²(7x)/(7x)→0."),
    q("ex-2-3-q2", 2, "Use algebra and limit laws: (a) lim_{x→4}−6/(x−4)²; (b) lim_{x→0}([1/(x+3)]−1/3)/x; (c) lim_{x→5}(√x−√5)/(x−5).",
      "(a) The denominator approaches 0 through positive values, so the expression tends to −∞. (b) Combine the numerator: [1/(x+3)−1/3]/x = [−x/(3(x+3))]/x = −1/[3(x+3)]→−1/9. (c) Rationalize to 1/(√x+√5)→1/(2√5)."),
    q("ex-2-3-q3", 3, "Find the limits of the sequences: (a) {5n/(n+7)}; (b) {(4−7n)/(8+n)}; (c) {(-1)^n/n²}.",
      "Divide numerator and denominator by n in the first two: (a) 5/(1+7/n)→5; (b) (4/n−7)/(8/n+1)→−7. For (c), |(−1)^n/n²|=1/n²→0, so the sequence tends to 0."),
    q("ex-2-3-q4", 4, "Weekly sales are S(x)=5000+3600/(x+2) rupees, x weeks after an advertising campaign. Find (a) S(5), (b) lim_{x→5}S(x), and (c) lim_{x→∞}S(x).",
      "(a) S(5)=5000+3600/7=5514.2857… rupees. (b) S is continuous at 5, so the limit is S(5)=5514.2857… rupees. (c) As x→∞, 3600/(x+2)→0, hence the limit is 5000 rupees."),
    q("ex-2-3-q5", 5, "Use Maple’s limit command to evaluate every limit from Question 1.",
      "Enter each expression using the syntax limit(expression, x=a), replacing x and a with the variable and limiting value shown in Question 1. The outputs are (a) −1/4, (b) 9/4, (c) 1/2, (d) −1, (e) 1, (f) 1, (g) 0, and (h) 0."),
    q("ex-2-3-q6", 6, "Evaluate the limits in parts (a–g) using algebraic techniques and standard limits.",
      "(a) Rationalize the difference of square roots before letting h→0. (b) Factor the difference of powers and cancel the common factor before substitution. (c) Use 1−cos u=2sin²(u/2), giving p²/q². (d) Rewrite tan θ−sin θ=sin θ(1−cos θ); dividing by sin³θ gives (1−cos θ)/sin²θ→1/2. (e) (1−1/n)^n→e^{−1}. (f) Apply (1+u)^{1/u}→e after matching the exponent. (g) Compare the base with a constant less than 1; the limit is 0."),
    q("ex-2-3-project", "Project", "Identify the types of functions represented by the two curves shown in the book.",
      "Identify each curve from its shape and defining equation printed beside it: the first is a real-world plotted curve; the second is the displayed algebraic function. Read the curve’s equation and classify it by its functional form.")
]

review2 = next(e for e in u2["exercises"] if e["id"] == "ex-2-5")
review2["problems"] = [
    q("ex-2-review-q1", "i", "In y=(x²+4x−3)/(x+3), identify the independent variable.", "The input variable is x; y depends on x. Answer: x."),
    q("ex-2-review-q2", "ii", "For f(x)=(3x²−2)/(3x+9), find f(−3).", "At x=−3 the denominator 3x+9 is 0, while the numerator is nonzero. Thus f(−3) is undefined."),
    q("ex-2-review-q3", "iii", "Find the domain of f(x)=(3x²−2)/(3x+9).", "A rational function is undefined when its denominator is zero: 3x+9=0 gives x=−3. Domain: ℝ\\{−3}."),
    q("ex-2-review-q4", "iv", "Find the domain of f(x)=(3x−2)/(3x²+9).", "Since 3x²+9=3(x²+3)>0 for all real x, there is no excluded real input. Domain: ℝ."),
    q("ex-2-review-q5", "v", "If f(x)=2x+3, find f^{−1}(5).", "Set y=2x+3 and solve for x: x=(y−3)/2. Thus f^{−1}(y)=(y−3)/2, and f^{−1}(5)=(5−3)/2=1."),
    q("ex-2-review-q6", "vi", "A function written as y=f(x) is called what kind of function?", "The dependent variable y is explicitly given in terms of x. It is an explicit function."),
    q("ex-2-review-q7", "vii", "If f(x)=3x²+2x−1 and g(x)=x+1, find f(g(x)).", "f(g(x))=3(x+1)²+2(x+1)−1=3x²+6x+3+2x+2−1=3x²+8x+4."),
    q("ex-2-review-q8", "viii", "Choose the listed approximation for e.", "e=2.7182818…; to two decimal places, e≈2.72. The closest listed option is 2.71."),
    q("ex-2-review-q9", "ix", "If 5^x=7, express x using natural logarithms.", "Take ln of both sides: x ln 5=ln 7, so x=ln 7/ln 5."),
    q("ex-2-review-q10", "x", "Write coth x in exponential form.", "Using cosh x=(e^x+e^{−x})/2 and sinh x=(e^x−e^{−x})/2, coth x=cosh x/sinh x=(e^x+e^{−x})/(e^x−e^{−x})."),
    q("ex-2-review-q11", "xi", "Simplify ln(m²)−ln(n²).", "By the quotient law of logarithms, ln(m²)−ln(n²)=ln(m²/n²), for m,n≠0."),
    q("ex-2-review-q12", "xii", "For f(x)=2/(x²−9), find its discontinuity points.", "The denominator factors as (x−3)(x+3) and vanishes at x=3 and x=−3. These are the discontinuity points."),
    q("ex-2-review-q13", "xiii", "Evaluate lim_{θ→0} sin(7θ)/(7θ).", "Let u=7θ. As θ→0, u→0, and sin u/u→1. The limit is 1."),
    q("ex-2-review-q14", "xiv", "If f(θ)=θ sec θ, find f(0).", "f(0)=0·sec 0=0·1=0."),
    q("ex-2-review-q15", "xv", "Find the inverse of f(x)=(e^x−e^{−x})/(e^x+e^{−x}).", "Let y=(e^x−e^{−x})/(e^x+e^{−x})=tanh x. Then x=artanh y=(1/2)ln((1+y)/(1−y)), for −1<y<1. Therefore f^{−1}(x)=(1/2)ln((1+x)/(1−x)).")
]

u3 = units[2]
ex31 = next(e for e in u3["exercises"] if e["id"] == "ex-3-1")
ex31["problems"] = [
    q("ex-3-1-q1", 1, "Find the average rate of change: (a) y=x²+4, x=2 to 3; (b) y=x²+1/x, x=−2 to −3; (c) s=2t²−5t+7, t=1 to 3; (d) h=√(2t+4), t=8 to 8.5.",
      "Use [f(b)−f(a)]/(b−a). (a) (13−8)/(3−2)=5. (b) f(−2)=7/2 and f(−3)=26/3, so [(26/3)−(7/2)]/(−1)=−31/6. (c) [10−4]/2=3. (d) [√21−√20]/0.5=2(√21−2√5)."),
    q("ex-3-1-q2", 2, "Use the definition of rate of change: (a) s=2t−3, t=2 to 5; (b) y=x²−6x+8, x=3 to 3.1; (c) A=πr², r=2 to 2.1; (d) h=√(t−9), t=9 to 16.",
      "The average rate is the change in the dependent variable divided by the change in the independent variable. (a) 2. (b) [f(3.1)−f(3)]/0.1=[−0.99−(−1)]/0.1=0.1. (c) π(2.1²−2²)/0.1=4.1π. (d) (√7−0)/(16−9)=1/√7."),
    q("ex-3-1-q3", 3, "A ball’s height is h(t)=−16t²+80t feet. Find its average velocity from t=2 to 2.1 and from t=2 to 2.01.",
      "h(2)=96. h(2.1)=97.44, so the first average velocity is (97.44−96)/0.1=14.4 ft/s. h(2.01)=96.1584, so the second is (96.1584−96)/0.01=15.84 ft/s."),
    q("ex-3-1-q4", 4, "Inflation is modeled by p(t)=3t²+t+1. Find the average rate of change of price from t=3 to t=5 and explain its meaning.",
      "p(5)=81 and p(3)=31. The average rate is (81−31)/(5−3)=25 rupees per year. Over those two years, the modeled price increased by an average of 25 rupees each year."),
    q("ex-3-1-q5", 5, "Profit is f(x)=1800x−9x². Find the average rate of change when planted area changes from 20 to 50 acres and explain.",
      "f(50)=67,500 and f(20)=32,400. Thus [f(50)−f(20)]/(50−20)=35,100/30=1,170. The profit increases by an average of 1,170 currency units per additional acre over this interval."),
    q("ex-3-1-q6", 6, "Use the first-principle rule to differentiate: (a) 3x; (b) √(5x+6); (c) x²+1; (d) 12−x²; (e) 16x²−7x; (f) 7/x.",
      "Apply f'(x)=lim_{h→0}[f(x+h)−f(x)]/h and simplify. (a) 3. (b) 5/[2√(5x+6)]. (c) 2x. (d) −2x. (e) 32x−7. (f) −7/x²."),
    q("ex-3-1-q7", 7, "For f(x)=x²−7x+6: (a) find the derivative at P(5,−4); (b) find the tangent line at P(5,−4); (c) find the tangent slope at P(6,0).",
      "f'(x)=2x−7. (a) f'(5)=3. (b) Point-slope form gives y+4=3(x−5), hence y=3x−19. (c) f'(6)=5.",
      {"type":"tangent-line","a":1,"b":-7,"c":6,"x0":5,"xMin":0,"xMax":8,"title":"Curve and tangent at P(5, −4)"}),
    q("ex-3-1-q8", 8, "Use the derivative definition to find each tangent slope and tangent line: (a) f=x²+7x at x=3; (b) f=6x²−11x−10 at x=1; (c) f=3x²−6x−10 at x=0; (d) f=2x³+3x−4 at x=1.",
      "Differentiate using first principles, then use y−f(a)=f'(a)(x−a). (a) f'(x)=2x+7; at x=3 the point is (3,30), slope 13, line y=13x−9. (b) f'=12x−11; point (1,−15), slope 1, line y=x−16. (c) f'=6x−6; point (0,−10), slope −6, line y=−6x−10. (d) f'=6x²+3; point (1,1), slope 9, line y=9x−8.")
]

ex33 = next(e for e in u3["exercises"] if e["id"] == "ex-3-2")
ex33["problems"] = [
    q("ex-3-3-q1", 1, "Differentiate: (a) w=4(x³−4x+2)^5; (b) y=(4x−x²)^11/5; (c) u=∛(1−3r²); (d) s=1/(3t+1)^7.",
      "Apply the chain rule. (a) dw/dx=20(x³−4x+2)^4(3x²−4). (b) dy/dx=(11/5)(4x−x²)^10(4−2x). (c) du/dr=−2r/(1−3r²)^{2/3}. (d) Writing s=(3t+1)^{−7}, ds/dt=−21/(3t+1)^8."),
    q("ex-3-3-q2", 2, "Find f'(x): (a) f=(2x−5)^3(5x−7); (b) f=(x+2)^2/(x−1); (c) f=[(2x−5)/(x−4)]^4; (d) f=x√(2x²+11).",
      "(a) Product and chain rules give f'=(2x−5)^2(40x−67). (b) Quotient rule gives f'=(x+2)(x−4)/(x−1)^2. (c) Chain and quotient rules give f'=−12(2x−5)^3/(x−4)^5. (d) Product rule gives f'=√(2x²+11)+2x²/√(2x²+11)=(4x²+11)/√(2x²+11)."),
    q("ex-3-3-q3", 3, "Find dy/dx for each parametric curve: (a) x=1+t², y=t³+2t²+1; (b) x=3at²+2, y=6t⁴+9; (c) x=a(1−t²)/(1+t²), y=2bt/(1+t²); (d) x=3at/(1+t³), y=3at²/(1+t³).",
      "Use dy/dx=(dy/dt)/(dx/dt). (a) (3t²+4t)/(2t)=(3t+4)/2. (b) 24t³/(6at)=4t²/a. (c) [2b(1−t²)/(1+t²)²]/[−4at/(1+t²)²]=−b(1−t²)/(2at). (d) [3at(2−t³)/(1+t³)²]/[3a(1−2t³)/(1+t³)²]=t(2−t³)/(1−2t³).")
]
ex34 = next(e for e in u3["exercises"] if e["id"] == "ex-3-3")
ex34["problems"] = [
    q("ex-3-4-q1", 1, "Using first principles, differentiate: (a) sin(2x); (b) cot(3x); (c) cos(3x)+tan(3x); (d) cot²x; (e) tan√x; (f) sin²x.",
      "Apply f'(x)=lim_{h→0}[f(x+h)−f(x)]/h and the standard trigonometric limits. (a) 2cos(2x). (b) −3csc²(3x). (c) −3sin(3x)+3sec²(3x). (d) −2cot x csc²x. (e) sec²(√x)/(2√x). (f) 2sin x cos x."),
    q("ex-3-4-q2", 2, "Differentiate: (a) x²cot(3x); (b) y=(sin2x+cot3x)²; (c) y=4cosec(2x); (d) y=2tan((x+3)²); (e) y=√(tan x)/cos√x; (f) y=(1+tan2x)/cosec3x.",
      "Use product, quotient, and chain rules. (a) 2x cot(3x)−3x²csc²(3x). (b) 2(sin2x+cot3x)(2cos2x−3csc²3x). (c) −8csc(2x)cot(2x). (d) 4(x+3)sec²((x+3)²). For (e), write y=√(tan x)sec√x; then y'=sec²x·sec√x/[2√(tan x)]+√(tan x)sec√x tan√x/(2√x). (f) Rewrite y=(1+tan2x)sin3x; y'=2sec²(2x)sin3x+3(1+tan2x)cos3x."),
    q("ex-3-4-q3", 3, "Differentiate: (a) cos^{−1}(x/a); (b) tan^{−1}(x/p); (c) cot^{−1}(a/x); (d) cosec^{−1}√(1+x²); (e) cosec^{−1}(t+3); (f) x tan^{−1}((x+1)/(x−1)).",
      "(a) −1/√(a²−x²). (b) p/(p²+x²). (c) a/(a²+x²). (d) −1/(1+x²) for x>0; use the absolute-value form at x<0. (e) −1/(|t+3|√((t+3)²−1)). (f) By the product and chain rules, tan^{−1}((x+1)/(x−1))−2x/((x−1)²+(x+1)²)."),
    q("ex-3-4-q4", 4, "Profit is P(t)=5−5cos(πt/10) hundred dollars, where t is weeks after January 1. Find the rate of change at t=8, 26, and 50 weeks.",
      "P'(t)=(π/2)sin(πt/10), in hundreds of dollars per week. Thus P'(8)=(π/2)sin(4π/5)≈0.9233; P'(26)=(π/2)sin(13π/5)≈1.4939; P'(50)=(π/2)sin(5π)=0."),
    q("ex-3-4-q5", 5, "The air volume is V(t)=0.45−0.35cos(πt/2) litres for 0≤t≤8 seconds. Find the rate of flow at t=3, 4, and 5 seconds.",
      "Differentiate: V'(t)=0.175π sin(πt/2) litres per second. Therefore V'(3)=−0.175π≈−0.5498 L/s, V'(4)=0, and V'(5)=0.175π≈0.5498 L/s.")
]
ex35 = next(e for e in u3["exercises"] if e["id"] == "ex-3-4")
ex35["problems"] = [
    q("ex-3-5-q1", 1, "Use first principles to differentiate: (a) e^{2x}; (b) (1/3)e^{3x}; (c) (5/8)e^{x²}+1; (d) 2^x; (e) 4^{x+4}; (f) log(x+1); (g) log_a(x²); (h) sinh(2x).",
      "The first-principle limit gives the standard exponential and logarithmic derivatives. (a) 2e^{2x}. (b) e^{3x}. (c) (5/4)xe^{x²}. (d) 2^x ln2. (e) 4^{x+4}ln4. (f) 1/[(x+1)ln10] if log is base 10. (g) 2/(x ln a). (h) 2cosh(2x)."),
    q("ex-3-5-q2", 2, "Find f'(x) if f(x) is: (a) 11^{(x²−4x)}; (b) e^{√(x−3)}; (c) x³e^{1/x}; (d) e^{2x}/(e^{−2x}+1); (e) ln(e^{mx}−e^{−mx}); (f) (e^{mx}−e^{−mx})/(e^{mx}+e^{−mx}).",
      "Use the chain rule, and the quotient rule where needed. (a) f'=11^{x²−4x}(2x−4)ln11. (b) f'=e^{√(x−3)}/[2√(x−3)]. (c) f'=e^{1/x}(3x²−x). (d) Let u=e^{2x}; then f=u²/(u+1), so f'=2e^{2x}(e^{2x}+2)/(e^{2x}+1)². (e) f'=m(e^{mx}+e^{−mx})/(e^{mx}−e^{−mx}). (f) f'=4m/(e^{mx}+e^{−mx})²."),
    q("ex-3-5-q3", 3, "Differentiate: (a) y=x³ ln√x; (b) y=x²√(ln x); (c) y=ln√((x²+1)/(x²−1)); (d) y=ln(x−√(x²+1)); (e) y=e^{−2x}cos(2x); (f) y=x²e^{sin x}.",
      "(a) ln√x=(1/2)ln x, so y'=x²[(3/2)ln x+1/2]. (b) y'=2x√(ln x)+x/[2√(ln x)]. (c) y'=−2x/[(x²+1)(x²−1)]. (d) Formal differentiation gives y'=−1/√(x²+1); note the printed logarithm has no real domain because x−√(x²+1)<0. (e) y'=−2e^{−2x}[cos(2x)+sin(2x)]. (f) y'=e^{sin x}(2x+x²cos x)."),
    q("ex-3-5-q4", 4, "Differentiate: (a) y=log((x+2)³); (b) y=cosh(3x); (c) y=sinh^{−1}(cos x); (d) y=tanh^{−1}(x/2); (e) y=ln(coth x); (f) y=x cosh^{−1}(x)−√(x²−1).",
      "(a) y'=3/[(x+2)ln10] for common logarithm. (b) y'=3sinh(3x). (c) y'=−sin x/√(1+cos²x). (d) Using d/dx artanh(u)=u'/(1−u²), y'=2/(4−x²). (e) y'=−1/(sinh x cosh x). (f) Product rule gives cosh^{−1}(x)+x/√(x²−1)−x/√(x²−1)=cosh^{−1}(x).")
]

u4 = units[3]
ex42 = next(e for e in u4["exercises"] if e["id"] == "ex-4-1")
ex42["problems"] = [
    q("ex-4-2-q1", 1, "Find the tangent line at the stated x-value: (a) y=√(x+1), x=3; (b) y=sin(2x+π), x=0; (c) y=x²e^x, x=1; (d) y=x/(x²+1), x=1.",
      "Use y−f(a)=f'(a)(x−a). (a) f(3)=2 and f'(3)=1/4, so y−2=(x−3)/4. (b) f(0)=0 and f'(0)=2cosπ=−2, so y=−2x. (c) f(1)=e and f'(x)=e^x(x²+2x), hence f'(1)=3e; tangent: y−e=3e(x−1). (d) f(1)=1/2 and f'(x)=(1−x²)/(x²+1)², so f'(1)=0; tangent y=1/2."),
    q("ex-4-2-q2", 2, "Find the normal line at the stated x-value: (a) y=xe^x, x=1; (b) y=(2x+1)^4, x=0; (c) y=cos(x−π), x=π/2.",
      "The normal slope is the negative reciprocal of the tangent slope. (a) f(1)=e, f'(1)=2e, so the normal slope is −1/(2e): y−e=−(x−1)/(2e). (b) f(0)=1, f'(0)=8, so y−1=−x/8. (c) f(π/2)=0 and f'(x)=−sin(x−π), giving f'(π/2)=1; the normal slope is −1, so y=−(x−π/2)."),
    q("ex-4-2-q3", 3, "Find the indicated tangent or normal equations: (a) tangent to x²+y²=13 at (−2,3); (b) tangent to sin(x−y)=xy at (0,π); (c) normal to x²+2xy=y³ at (1,−1).",
      "(a) Implicit differentiation gives 2x+2y y'=0, so y'=−x/y. At (−2,3), slope=2/3, hence y−3=(2/3)(x+2). (b) Differentiate: cos(x−y)(1−y')=y+xy'. At (0,π), cos(−π)=−1, so −1+y'=π; hence y'=π+1 and the tangent is y−π=(π+1)x. (c) Differentiate 2x+2(y+xy')=3y²y'; solving at (1,−1) gives y'=0, so the tangent is horizontal and the normal is x=1."),
    q("ex-4-2-q4", 4, "Write the first four nonzero Taylor terms: (a) cos x about x=π/4; (b) √x about x=4; (c) x+e^x about x=1.",
      "Use f(a)+f'(a)(x−a)+f''(a)(x−a)²/2!+f'''(a)(x−a)³/3!. (a) cos(π/4)−sin(π/4)(x−π/4)−cos(π/4)(x−π/4)²/2!+sin(π/4)(x−π/4)³/3! = (√2/2)[1−(x−π/4)−(x−π/4)²/2+(x−π/4)³/6]. (b) 2+(x−4)/4−(x−4)²/64+(x−4)³/512. (c) 1+e + (1+e)(x−1)+e(x−1)²/2!+e(x−1)³/3! + …; the constant term is f(1)=1+e."),
    q("ex-4-2-q5", 5, "Find the Maclaurin expansions: (a) 1/(1+x); (b) sin²x; (c) cosh x; (d) ln(1−4x).",
      "Use standard power series. (a) 1−x+x²−x³+x⁴−… for |x|<1. (b) (1−cos 2x)/2=x²−x⁴/3+2x⁶/45−…. (c) 1+x²/2!+x⁴/4!+x⁶/6!+…. (d) −∑_{n=1}∞(4x)^n/n=−4x−8x²−(64/3)x³−64x⁴−… for |x|<1/4."),
    q("ex-4-2-q6", 6, "Use the series for e^x to show e=1+1+1/2!+1/3!+… and approximate e to four decimal places.",
      "The Maclaurin series e^x=∑_{n=0}∞x^n/n!. Setting x=1 gives e=∑_{n=0}∞1/n!. Summing terms through n=9 gives 2.7182815…, and the remaining positive tail is less than 0.000003, so e≈2.7183 to four decimal places."),
    q("ex-4-2-q7", 7, "Find the intersection angle of the curve pairs shown in the printed exercise.",
      "At an intersection, find both tangent slopes by implicit differentiation. If the slopes are m₁ and m₂, the angle θ between the curves satisfies tan θ=|(m₂−m₁)/(1+m₁m₂)|. Substitute the intersection coordinates for each pair and take the acute angle. The scan’s second pair equation is not legible enough here to state a verified numerical angle."),
    q("ex-4-2-q8", 8, "Find the point(s) on y=5x³−4x² where the tangent is parallel to y=5x−3.",
      "The given line has slope 5. Differentiate the curve: y'=15x²−8x. Set 15x²−8x=5, so 15x²−8x−5=0. Thus x=(4±√91)/15. Substitute each x into y=5x³−4x² to obtain the corresponding points.")
]
ex41 = next(e for e in u4["exercises"] if e["id"] == "ex-4-4")
ex41["problems"] = [
    q("ex-4-1-q1", 1, "Find the second derivative: (a) y=x³−4x²+5x+2; (b) y=x²+3x−1; (c) y=sin x; (d) y=e^x.",
      "Differentiate twice. (a) y'=3x²−8x+5, y''=6x−8. (b) y'=2x+3, y''=2. (c) y'=cos x, y''=−sin x. (d) y'=e^x, y''=e^x."),
    q("ex-4-1-q2", 2, "Find d²y/dx² for the parametric curve x=1+t², y=t³+2t²+1.",
      "dx/dt=2t, dy/dt=3t²+4t, so dy/dx=(3t+4)/2. Then d²y/dx²=[d/dt((3t+4)/2)]/(dx/dt)=3/(4t)."),
    q("ex-4-1-q3", 3, "Find y'' for: (a) y=tan^{−1}x; (b) y=ln(x²+1).",
      "(a) y'=1/(1+x²), hence y''=−2x/(1+x²)². (b) y'=2x/(x²+1), hence y''=2(1−x²)/(x²+1)²."),
    q("ex-4-1-q4", 4, "Show that y=1/x satisfies xy'+y=0, then verify the relation by differentiation.",
      "For y=x^{−1}, y'=−x^{−2}. Therefore xy'+y=x(−x^{−2})+x^{−1}=−x^{−1}+x^{−1}=0, for x≠0.")
]

ex43 = next(e for e in u4["exercises"] if e["id"] == "ex-4-2")
ex43["problems"] = [
    q("ex-4-3-q1", 1, "Find critical values and intervals of increase/decrease: (a) f(x)=x³+3x²+1; (b) f(x)=x⁴+35x²−125x−9.375.",
      "(a) f'=3x²+6x=3x(x+2). Critical numbers: −2,0. The derivative is positive on (−∞,−2) and (0,∞), negative on (−2,0); hence f increases on the first and third intervals and decreases on the middle interval. (b) f'=4x³+70x−125. Since f''=12x²+70>0, f' is strictly increasing and has one real zero, approximately x≈1.566. Thus f decreases before this critical number and increases after it."),
    q("ex-4-3-q2", 2, "Find the critical values: (a) f(x)=2x³−3x²−72x+15; (b) f(x)=x³/3−x²−15x+6.",
      "(a) f'=6x²−6x−72=6(x−4)(x+3); critical numbers are x=−3 and x=4. (b) f'=x²−2x−15=(x−5)(x+3); critical numbers are x=−3 and x=5."),
    q("ex-4-3-q9", 9, "The concentration model is K(x)=4x/(3x²+27), for x>0 hours. Find where it increases/decreases and when its maximum occurs.",
      "K'(x)=4(27−3x²)/(3x²+27)²=12(9−x²)/(3x²+27)². For x>0 the denominator is positive; K'>0 on (0,3), K'<0 on (3,∞). Therefore the concentration reaches its maximum at x=3 hours, with K(3)=12/54=2/9."),
    q("ex-4-3-q10", 10, "A generator uses fuel at G(x)=1/48(300/x+2x) gallons per hour after x kilowatt-hours. Fuel costs $2.25 per gallon. Find x that minimizes fuel cost for 32 operating hours and the minimum cost.",
      "Total fuel cost is C(x)=32·2.25·G(x)=450/x+3x, x>0. Then C'(x)=−450/x²+3. Set C'=0: x²=150, so x=√150≈12.247 (positive domain). Since C''(x)=900/x³>0, this is a minimum. C_min=450/√150+3√150=6√150≈$73.48.")
]

u7 = units[6]
ex71 = next(e for e in u7["exercises"] if e["id"] == "ex-7-1")
ex71["problems"] = [
    q("ex-7-1-q1", 1, "For A(−1,3), B(2,1), and C(5,−1), show that |AB|+|BC|=|AC|.",
      "Using the distance formula: |AB|=√((2+1)²+(1−3)²)=√13; |BC|=√((5−2)²+(−1−1)²)=√13; |AC|=√((5+1)²+(−1−3)²)=√52=2√13. Therefore |AB|+|BC|=2√13=|AC|."),
    q("ex-7-1-q2", 2, "Find the midpoint of each segment: (a) P(10,20), Q(−12,−8); (b) P(a,−b), Q(−a,b); (c) P(1/2,−1/4), Q(3/4,4/7).",
      "Apply M=((x₁+x₂)/2,(y₁+y₂)/2). (a) M=(−1,6). (b) M=(0,0). (c) M=(5/8,9/56)."),
    q("ex-7-1-q3", 3, "Find R(x,y) dividing PQ in the stated ratios: (a) P(1,2), Q(3,4), ratio 5:7; (b) P(3,4), Q(−6,2), ratio 3:−2; (c) P(−6,7), Q(5,−4), ratio 2/7:1.",
      "Use the section formula R=((n x₁+m x₂)/(m+n),(n y₁+m y₂)/(m+n)) for ratio m:n. (a) R=(11/6,17/6). (b) With signed ratio 3:−2, R=(−24,−2). (c) Rewrite 2/7:1 as 2:7; R=(−32/9,41/9)."),
    q("ex-7-1-q4", 4, "Determine the ratio in which R divides PQ for the two coordinate sets shown in the textbook.",
      "For each set, use the x-coordinate section equation x_R=(n x_P+m x_Q)/(m+n) to solve for m:n, then verify the result with the y-coordinate. The second coordinate of the second printed R point is not legible in the scan, so that ratio cannot be stated reliably from the available page image."),
    q("ex-7-1-q5", 5, "Find each triangle’s centroid: (a) A(4,−2), B(−2,4), C(5,5); (b) A(3,5), B(4,6), C(3,−1); (c) A(1,1), B(−2,−2), C(4,5).",
      "The centroid is the coordinate-wise mean of the vertices. (a) G=(7/3,7/3). (b) G=(10/3,10/3). (c) G=(1,4/3).")
]
u5 = units[4]
ex51 = next(e for e in u5["exercises"] if e["id"] == "ex-5-3")
ex51["problems"] = [
    q("ex-5-1-q1", 1, "Find the domain: (a) F(t)=2t i−3t j+t²k; (b) F(t)=(1−t)i+√t j−(t−2)²k; (c) F(t)=sin t i+cos t j+tan t k; (d) F(t)=cos t i−cot t j+csc t k.", "The domain is the intersection of the component domains. (a) All real t. (b) t≥0 because of √t. (c) t≠π/2+nπ, n∈ℤ, because tan t is undefined there. (d) t≠nπ, n∈ℤ, because cot t and csc t are undefined there."),
    q("ex-5-1-q2", 2, "For F(t)=2t i−5j+t²k, G(t)=(1−t)i+(1/t)k, and H(t)=sin t i+e^t j, find: (a) 2F−3G; (b) 3F+4G; (c) G·H; (d) F×H.", "Operate componentwise. (a) (7t−3)i−10j+(2t²−3/t)k. (b) (2t+4)i−15j+(3t²+4/t)k. (c) (1−t)sin t. (d) −t²e^t i+t²sin t j+(2te^t+5sin t)k."),
    q("ex-5-1-q3", 3, "Evaluate: (a) lim_{t→0}[3t i+e^{2t}j+sin(πt)k]; (b) lim_{t→1}[(t²−1)/(t−1)i+(t²−3t+2)/(t²+t−2)j+(t²+1)e^{−t²}k]; (c) lim_{t→0}[sin t/t i+(1−cos t)/t² j+e^{−t²}k]; (d) lim_{t→0}[sin(2t)/(2t)i+ln(4+t)j].", "Evaluate each component limit. (a) j. (b) The components are t+1→2, (t−2)/(t+2)→−1/3, and (t²+1)e^{−t²}→2/e; result 2i−(1/3)j+(2/e)k. (c) i+(1/2)j+k, using the standard trigonometric limits. (d) i+ln4 j."),
    q("ex-5-1-q4", 4, "Test continuity for all real t: (a) F(t)=t i+3j−(1−t)k; (b) G(t)=t i−t^{−1}k; (c) F(t)=e^t(ti+t²j+3k); (d) G(t)=(t i+√t j)/(√t+t).", "A vector function is continuous where all components are defined and continuous. (a) Continuous for every real t. (b) Not defined at t=0; continuous for t≠0. (c) Continuous for every real t. (d) Defined for t>0 and continuous there; at t=0 the displayed expression is 0/0 and is undefined, although its right-hand limit exists and equals j, so it is not continuous at 0 as written.")
]
ex52 = next(e for e in u5["exercises"] if e["id"] == "ex-5-1")
ex52["problems"] = [
    q("ex-5-2-q1", 1, "Find the vector derivative: (a) F(t)=t i+t² j+(t³+t)k; (b) F(s)=(sin s+s²)i+(2s²−s)j+3k; (c) F(θ)=cosθ[i+tanθ j+3k].",
      "Differentiate components. (a) F'(t)=i+2t j+3t²k. (b) F'(s)=(cos s+2s)i+(4s−1)j. (c) Expand components: cosθ i+sinθ j+3cosθ k, hence F'(θ)=−sinθ i+cosθ j−3sinθ k."),
    q("ex-5-2-q2", 2, "Find the second vector derivatives: (a) F(t)=t²i+3t³j−8t²k; (b) F(s)=(3+s²)i−(s+1)²j+3s⁴k; (c) F(x)=ln x i−x²k; (d) F(θ)=sin²θ i−cos²θ j.",
      "Differentiate twice componentwise. (a) F''(t)=2i+18t j−16k. (b) F''(s)=2i−2j+36s²k. (c) F''(x)=−x^{−2}i−2k. (d) F'(θ)=sin(2θ)i+sin(2θ)j; F''(θ)=2cos(2θ)i+2cos(2θ)j."),
    q("ex-5-2-q3", 3, "Differentiate the scalar functions: (a) f(x)=[x i+(x+1)j]·[2x i−3x²j]; (b) g(x)=sin x i−2x j+cos x k.",
      "(a) The dot product is 2x²−3x²(x+1)=−3x³−x²+2x, so f'(x)=−9x²−2x+2. (b) Differentiate components: g'(x)=cos x i−2j−sin x k."),
    q("ex-5-2-q4", 4, "For each position vector r(t), find velocity, acceleration, speed, and direction of motion at the stated time: (a) r(t)=t i+t²j+2t k at t=1; (b) r(t)=cos t i+sin t j+3t k at t=π/4; (c) r(t)=e^t i+e^{−t}j+e^{2t}k at t=ln2.",
      "Use v=r', a=r'', speed=|v|, direction v/|v|. (a) v(1)=i+2j+2k; a=2j; speed=3; direction=(i+2j+2k)/3. (b) v=−sin t i+cos t j+3k, a=−cos t i−sin t j; at π/4 speed=√10 and direction=(−i+j+3√2 k)/(2√5). (c) At t=ln2, v=2i+1/2 j+4k; a=2i+1/4 j+8k; speed=√(81/4)=9/2; direction=(4/9)i+(1/9)j+(8/9)k."),
    q("ex-5-2-q5", 5, "If F(t) is differentiable and F(t)≠0, show d|F|/dt = [F·F']/|F|.",
      "Since |F|=(F·F)^{1/2}, differentiate by the chain rule: d|F|/dt=(1/2)(F·F)^{−1/2}·d(F·F)/dt. By the product rule for dot products, d(F·F)/dt=F'·F+F·F'=2F·F'. Therefore d|F|/dt=(F·F')/|F|.")
]
u6 = units[5]
ex62 = next(e for e in u6["exercises"] if e["id"] == "ex-6-3")
ex62["problems"] = [
    q("ex-6-2-q1", 1, "Evaluate by substitution: (a) ∫sin⁴x cos x dx; (b) ∫√(sin²x) cos x dx; (c) ∫sin x ln(cos x)/cos x dx; (d) ∫e^x sin(e^x) dx; (e) ∫cot√x/√x dx; (f) ∫(sin x−cos x)/(sin x+cos x) dx.",
      "(a) Let u=sin x: u⁵/5+C. (b) Let u=sin x: ∫|u|du; on intervals where sin x≥0 this is (sin²x)/2+C. (c) Let u=cos x; du=−sin x dx, giving −∫ln u/u du=−(1/2)(ln(cos x))²+C. (d) Let u=e^x: −cos(e^x)+C. (e) Let u=√x; dx=2u du, giving 2∫cot u du=2ln|sin√x|+C. (f) Let u=sin x+cos x; du=(cos x−sin x)dx, so the integral is −ln|sin x+cos x|+C."),
    q("ex-6-2-q2", 2, "Evaluate using suitable substitutions: (a) ∫dx/(x²+16); (b) ∫sin x/(cos²x+1) dx; (c) ∫dx/√(e^{2x}−4); (d) ∫(2x+5)/(x²+4x+5) dx; (e) ∫(2+x)/√(4−2x−x²) dx.",
      "(a) (1/4)tan^{−1}(x/4)+C. (b) Let u=cos x: −tan^{−1}u+C. (c) Put u=e^x; then ∫du/[u√(u²−4)]=(1/2)sec^{−1}(e^x/2)+C, on e^x>2. (d) Write numerator as (2x+4)+1; result ln(x²+4x+5)+(1/√1)tan^{−1}(x+2)+C. (e) Complete square: 4−2x−x²=5−(x+1)² and numerator=(x+1)+1; result −√(5−(x+1)²)+sin^{−1}((x+1)/√5)+C."),
    q("ex-6-2-q3", 3, "Evaluate by integration by parts: (a) ∫x²e^x dx; (b) ∫x cos x dx; (c) ∫e^x sin x dx.",
      "(a) Repeated integration by parts gives e^x(x²−2x+2)+C. (b) x sin x+cos x+C. (c) Let I=∫e^x sin x dx; integrating by parts twice gives I=e^x sin x−e^x cos x−I, hence I=(e^x/2)(sin x−cos x)+C.")
]
ex63 = next(e for e in u6["exercises"] if e["id"] == "ex-6-4")
ex63["problems"] = [
    q("ex-6-3-q1", 1, "Integrate by partial fractions: (a) ∫dx/[x(x−3)]; (b) ∫(3x²+2x−1)/[x(x+1)]; (c) ∫(4x³+4x²+x−1)/[x²(x+1)²]; (d) ∫dx/(x³−1); (e) ∫(x⁴−x²+2)/[x²(x−1)]; (f) ∫dx/(x²−1); (g) ∫(−x−3)/(2x²−x−1)dx; (h) ∫(x²−1)/(x²−2x−15)dx; (i) ∫x/[(x+1)(x²+1)]dx; (j) ∫(x²+2)/(x²+1)² dx.",
      "(a) (1/3)ln|(x−3)/x|+C. (b) Divide first: 3x²+2x−1 over x²+x =3−1/x−? Decompose and integrate after polynomial division. (c) Decompose into A/x+B/x²+C/(x+1)+D/(x+1)², then integrate each term. (d) 1/(x³−1)=1/[3(x−1)]−(x+2)/[3(x²+x+1)]; integrate the logarithmic and arctangent terms. (e) Polynomial division plus partial fractions. (f) (1/2)ln|(x−1)/(x+1)|+C. (g) Factor denominator (2x+1)(x−1), decompose and integrate. (h) Divide and factor (x−5)(x+3), then integrate. (i) Decompose A/(x+1)+(Bx+C)/(x²+1), then integrate. (j) Write (x²+2)/(x²+1)²=1/(x²+1)+1/(x²+1)²; result=(1/2)tan^{−1}x+x/[2(x²+1)]+(1/2)tan^{−1}x+C=x/(2(x²+1))+tan^{−1}x+C."),
    q("ex-6-3-q2", 2, "The drug elimination rate is R'(t)=60t/((t+1)²(t+2)) milligrams per hour, with R(0)=0. Find how much is eliminated in the first hour and after four hours.",
      "Decompose: 60t/((t+1)²(t+2))=120/(t+1)−60/(t+1)²−120/(t+2). Integrating from 0 to T gives R(T)=120ln(2(T+1)/(T+2))+60/(T+1)−60. Thus R(1)=120ln(4/3)−30≈4.52 mg, and R(4)=120ln(5/3)−48≈13.32 mg."),
    q("ex-6-3-q3", 3, "The voting population rate is dN/dt=100t/(1+t²)² thousand people per year. If N(0) is current, how much will population increase over three years?",
      "Integrate from 0 to 3: ΔN=∫₀³100t/(1+t²)²dt. Let u=1+t², du=2t dt; ΔN=50[−1/u]₁^{10}=45 thousand people."),
    q("ex-6-3-q4", 4, "An oil slick radius grows at dr/dt=100/√(r²+9) feet per minute. If r=0 at t=0, find the radius after four minutes.",
      "Separate and integrate: √(r²+9)dr=100dt. Since ∫√(r²+9)dr=(1/2)[r√(r²+9)+9ln(r+√(r²+9))], set this equal to 100t and evaluate at t=4. Solve r√(r²+9)+9ln((r+√(r²+9))/3)=800 numerically; r≈25.9 ft.")
]
review6 = next(e for e in u6["exercises"] if e["id"] == "ex-6-2")
review6["problems"] = [
    q("ex-6-review-q1", "i", "The process of finding an antiderivative is called what?", "Integration. An antiderivative reverses differentiation."),
    q("ex-6-review-q2", "ii", "Evaluate ∫tan θ dθ.", "tanθ=sinθ/cosθ. Let u=cosθ, du=−sinθdθ, so the integral is −ln|cosθ|+C."),
    q("ex-6-review-q3", "iii", "Evaluate ∫dx/√(a²−x²).", "This is the standard inverse-sine integral: sin^{−1}(x/a)+C, for a>0 and |x|<a."),
    q("ex-6-review-q4", "iv", "Evaluate ∫dx/√(x²−36).", "The standard formula gives ln|x+√(x²−36)|+C."),
    q("ex-6-review-q5", "v", "Evaluate ∫(x²−4)dx.", "x³/3−4x+C."),
    q("ex-6-review-q6", "vi", "If d/dx[f(x)g(x)] is expanded, what is the corresponding antiderivative product relation?", "Product rule: (fg)'=f'g+fg'. Therefore ∫f(x)g'(x)dx=f(x)g(x)−∫f'(x)g(x)dx+C."),
    q("ex-6-review-q7", "vii", "Evaluate ∫tan²x dx.", "Use tan²x=sec²x−1. Thus ∫tan²x dx=tan x−x+C."),
    q("ex-6-review-q8", "viii", "Evaluate ∫(x+8)/(x²−64) dx.", "Factor denominator (x−8)(x+8); cancel x+8 to get ∫dx/(x−8)=ln|x−8|+C."),
    q("ex-6-review-q9", "ix", "Evaluate ∫₀¹e^{2x}dx.", "[e^{2x}/2]₀¹=(e²−1)/2."),
    q("ex-6-review-q10", "x", "Evaluate ∫₁²x dx.", "[x²/2]₁²=(4−1)/2=3/2.")
]
ex72 = next(e for e in u7["exercises"] if e["id"] == "ex-7-2")
ex72["problems"] = [
    q("ex-7-2-q1", 1, "Find the distance between P(3,−2) and Q(−1,−5).", "d=√[(-1−3)²+(−5+2)²]=√(16+9)=5."),
    q("ex-7-2-q2", 2, "Find the point dividing the segment from P(2,−3) to Q(8,9) internally in the ratio 1:2.", "Section formula: R=((2x_P+x_Q)/3,(2y_P+y_Q)/3)=((4+8)/3,(-6+9)/3)=(4,1)."),
    q("ex-7-2-q3", 3, "Find the midpoint of P(−4,6) and Q(8,−2).", "M=((−4+8)/2,(6−2)/2)=(2,2)."),
    q("ex-7-2-q4", 4, "Find the centroid of the triangle with vertices (1,2), (4,−1), and (−2,5).", "G=((1+4−2)/3,(2−1+5)/3)=(1,2)."),
    q("ex-7-2-q5", 5, "Find the equation of the line through (2,3) and (−1,−3).", "Slope m=(−3−3)/(−1−2)=2. Point-slope form gives y−3=2(x−2), so y=2x−1."),
    q("ex-7-2-q6", 6, "Find the slope of the line through (−2,5) and (4,−1), and state whether it is parallel or perpendicular to a line of slope 1.", "m=(−1−5)/(4+2)=−1. Since the product of slopes −1·1=−1, the lines are perpendicular."),
    q("ex-7-2-q7", 7, "Find the distance of (3,−2) from the line 4x−3y+5=0.", "d=|4(3)−3(−2)+5|/√(4²+(−3)²)=23/5."),
    q("ex-7-2-q8", 8, "Find the angle between two lines with slopes 2 and −1/3.", "tan θ=|(m₂−m₁)/(1+m₁m₂)|=|(-1/3−2)/(1−2/3)|=7. Therefore θ=tan^{−1}(7)≈81.87°."),
    q("ex-7-2-q9", 9, "Find the area of the triangle with vertices (0,0), (4,0), and (1,3).", "Using base 4 and height 3, area=(1/2)(4)(3)=6 square units.")
]
ex74 = next(e for e in u7["exercises"] if e["id"] == "ex-7-6")
ex74["problems"] = [
    q("ex-7-4-q1", 1, "Find the intersection of each pair: (a) 2x+4y−10=0 and 5x−3y+1=0; (b) 2x+y−8=0 and 3x+2y−2=0.",
      "(a) Solve x+2y=5 and 5x−3y=−1: x=1, y=2. (b) From 2x+y=8 and 3x+2y=2, solve to obtain x=14, y=−20."),
    q("ex-7-4-q4", 4, "Find triangle areas: (a) P(0,0), P(2,4), P(−2,2); (b) P(−1,−2), P(2,5), P(5,2).",
      "Use one-half the absolute determinant of two side vectors. (a) Area=|2·2−4(−2)|/2=6. (b) The determinant from A is 3·4−7·6=−30, so area=15 square units."),
    q("ex-7-4-q5", 5, "Find the areas bounded by the vertices: (a) A(−3,6), B(3,2), C(6,0); (b) A(−2,4), B(3,−6), C(1,−2). Determine whether the vertices are collinear.",
      "Use the determinant area formula. (a) The slopes AB and BC both equal −2/3, so area=0 and the points are collinear. (b) The determinant is zero as well, so the area is 0 and the points are collinear.")
]
u8 = units[7]
ex82 = next(e for e in u8["exercises"] if e["id"] == "ex-8-2")
ex82["problems"] = [
    q("ex-8-2-q1", 1, "Find tangent and normal equations: (a) at (1,2) to x²+y²=5; (b) at (−3,−2) to x²+y²=13; (c) at (4,1) to x²+y²−4x+2y−3=0.",
      "For x²+y²=r², tangent at (x₁,y₁) is xx₁+yy₁=r²; the normal passes through the center and point. (a) Tangent x+2y=5; normal y=2x. (b) Tangent −3x−2y=13; normal 2x−3y=0. (c) Complete squares: (x−2)²+(y+1)²=8. At (4,1), radius vector from center (2,−1) is (2,2), so tangent slope −1: x+y=5; normal slope 1: y=x−3."),
    q("ex-8-2-q2", 2, "For the circle x²+y²=13, find tangent and normal equations at (6cos60°,6sin60°); also find the tangent at (2cos45°,2sin45°) to x²+y²=4.",
      "(a) The stated point has radius 6 and therefore is not on x²+y²=13; no tangent to this circle exists at that point as printed. (b) Point=(√2,√2), circle radius²=4. Tangent: √2x+√2y=4, or x+y=2√2. Normal: y=x."),
    q("ex-8-2-q3", 3, "Find n so the line x+y+n=0 is tangent to x²+y²=9.",
      "The distance from the center (0,0) to the line must equal radius 3: |n|/√2=3. Thus n=±3√2."),
    q("ex-8-2-q4", 4, "Find n so y=mx+c is tangent to x²+y²=a².",
      "The distance from the origin to mx−y+c=0 is |c|/√(m²+1). Set this equal to a; hence c=±a√(m²+1)."),
    q("ex-8-2-q10", 10, "Find tangents to x²+y²=4 parallel to x+2y+3=0, and to x²+y²=25 parallel to 3x+4y+3=0.",
      "Parallel lines have the same x,y coefficients. For x²+y²=r², a tangent x+2y+c=0 has |c|=r√5. (a) c=±2√5. (b) A tangent 3x+4y+c=0 has |c|=5√(3²+4²)=25, so c=±25.")
]
ex81 = next(e for e in u8["exercises"] if e["id"] == "ex-8-1")
ex81["problems"] = [
    q("ex-8-1-q1", 1, "Find circle equations: (a) center (0,0), r=4; (b) center (3,2), r=1; (c) center (−4,−3), r=4; (d) center (−a,−b), r=a+b.",
      "Use (x−h)²+(y−k)²=r². (a) x²+y²=16. (b) (x−3)²+(y−2)²=1. (c) (x+4)²+(y+3)²=16. (d) (x+a)²+(y+b)²=(a+b)²."),
    q("ex-8-1-q2", 2, "Find the circle equations: (a) center (0,0), tangent to x=−5; (b) center (0,0), tangent to y=6; (c) center (6,−6), passing through origin; (d) center (−9,−6), passing through (−20,8); (e) center (−5,4), tangent to x-axis; (f) center (5,3), tangent to y-axis.",
      "The radius is the perpendicular distance to the tangent or to the given point. (a) r=5: x²+y²=25. (b) r=6: x²+y²=36. (c) r²=6²+(−6)²=72: (x−6)²+(y+6)²=72. (d) r²=(−11)²+14²=317: (x+9)²+(y+6)²=317. (e) r=4: (x+5)²+(y−4)²=16. (f) r=5: (x−5)²+(y−3)²=25."),
    q("ex-8-1-q3", 3, "Find center and radius: (a) x²+y²−8x−6y+9=0; (b) 4x²+4y²+16x−12y−7=0; (c) x²+y²+4x−6y+13=0; (d) x²+y²−x−8y+18=0.",
      "Complete squares. (a) (x−4)²+(y−3)²=16; center (4,3), r=4. (b) Divide by 4: (x+2)²+(y−3/2)²=35/4; center (−2,3/2), r=√35/2. (c) (x+2)²+(y−3)²=0; point circle centered (−2,3), radius 0. (d) (x−1/2)²+(y−4)²=−1/4; no real circle."),
    q("ex-8-1-q4", 4, "Find the circle through: (a) (−3,0),(5,4),(6,−3); (b) (7,−1),(5,3),(−4,6); (c) (1,2),(3,−4),(5,−6).",
      "Substitute the three points into x²+y²+2gx+2fy+c=0 and solve for g,f,c. (a) x²+y²−4x−21=0. (b) x²+y²+4x+6y−72=0. (c) x²+y²−22x−4y+25=0."),
    q("ex-8-1-q5", 5, "Find circle equations through the indicated point(s) with center on the stated line: (a) through (2,6),(6,4), center on 3x+2y−1=0; (b) through (4,1),(6,5), center on 4x+y−16=0.",
      "Let center (h,k) lie on the given line and equate squared distances from the center to the two points. (a) 2h−k=3 and 3h+2k=1 give center (1,−1), r²=50; equation (x−1)²+(y+1)²=50. (b) h+2k=11 and 4h+k=16 give center (3,4), r²=8; equation (x−3)²+(y−4)²=8."),
    q("ex-8-1-q6", 6, "Find a circle through: (a) (0,0),(0,3), with 4x−5y=0 tangent at (0,0); (b) (0,−1),(3,0), with 3x+y+9=0 tangent at (3,0).",
      "(a) The center is both on the line through (0,0) normal to the tangent (direction (4,−5)) and on the perpendicular bisector y=3/2 of the chord from (0,0) to (0,3). This gives center (−6/5,3/2), so x²+y²+(12/5)x−3y=0. (b) As printed, the line 3x+y+9=0 does not pass through (3,0), so it cannot be tangent there; the statement contains a typo."),
    q("ex-8-1-q7", 7, "Find a concentric circle tangent to the given line: (a) x²+y²+16x−7y=0, tangent to y-axis; (b) x²+y²−8x+4=0, tangent to x+2y+6=0; (c) x²+y²+6x−10y+33=0, tangent to x-axis.",
      "Keep the center fixed and set radius equal to distance from the center to the tangent line. (a) Center (−8,7/2), distance to y-axis 8, so (x+8)²+(y−7/2)²=64. (b) Center (4,0); distance to line x+2y+6=0 is 10/√5=2√5, so (x−4)²+y²=20. (c) Center (−3,5), tangent distance 5, so (x+3)²+(y−5)²=25."),
    q("ex-8-1-q8", 8, "Find a circle through the origin whose axis intercepts are (a) 3 and 4; (b) 2 and 4.",
      "A circle through the origin has form x²+y²+Dx+Ey=0. If its nonzero axis intercepts are a and b, then D=−a and E=−b. (a) x²+y²−3x−4y=0. (b) x²+y²−2x−4y=0.")
]
u9 = units[8]
ex91 = next(e for e in u9["exercises"] if e["id"] == "ex-9-1")
ex91["problems"] = [
    q("ex-9-1-q1", 1, "For each parabola, sketch it and state vertex, focus, latus rectum endpoints, and axis: (a) x²=2y; (b) y²=−3(x+1); (c) (y−3)²=x.",
      "Use (x−h)²=4p(y−k) or (y−k)²=4p(x−h). (a) h=k=0, 4p=2 so p=1/2; vertex (0,0), focus (0,1/2), latus rectum endpoints (±1,1/2), axis x=0. (b) 4p=−3; vertex (−1,0), focus (−7/4,0), endpoints (−7/4,±3/2), axis y=0. (c) 4p=1; vertex (0,3), focus (1/4,3), endpoints (1/4,1), (1/4,5), axis y=3."),
    q("ex-9-1-q2", 2, "Find the equations of the parabolas shown in the textbook graphs (a) and (b).",
      "Read each vertex and focus/directrix from the graph, then substitute into standard form. (a) The marked vertex is (2,−1), focus (6,1), so axis has direction (4,2); because this is not axis-aligned, use rotated-coordinate form from the plotted focus/directrix. (b) The graph shows vertex (0,0), vertical axis x=−2 as directrix and focal points at (6,±12) inconsistent with a single standard parabola; verify the plotted labels before transcribing an equation."),
    q("ex-9-1-q3", 3, "Write each parabola equation: (a) focus (0,3), directrix y=−3; (b) focus (4,0), directrix x=−4; (c) vertex (0,0), axis of symmetry x-axis, through (3,6); (d) vertex (0,0), y-axis symmetry, through (−12,−3); (e) vertical axis through (−3,4), vertex (5,1); (f) horizontal axis through (7,9), vertex (3,−7).",
      "(a) Equidistance from focus and directrix gives x²=12y. (b) y²=16x. (c) x²=4py; 9=24p gives p=3/8, so x²=3y/2. (d) y²=4px; 9=−48p gives p=−3/16, so y²=−3x/4. (e) Vertical axis x=−3 and vertex (5,1) are inconsistent; an axis of a parabola must pass through the vertex. (f) Horizontal axis y=9 and vertex (3,−7) are inconsistent for the same reason; check the book statement."),
    q("ex-9-1-q4", 4, "Find the locus of points equidistant from focus (4,3) and directrix x=−2.",
      "Set distance to focus equal to distance to directrix: √((x−4)²+(y−3)²)=|x+2|. Squaring and simplifying gives (y−3)²=12(x−1), a parabola with vertex (1,3)."),
    q("ex-9-1-q5", 5, "Find a parabola with focal chord length 6, focus (4,−2), and directrix parallel to the y-axis.",
      "A directrix parallel to the y-axis makes the axis horizontal. The latus rectum length is |4p|=6, so |p|=3/2. The vertex lies 3/2 units horizontally from the focus and the directrix is another 3/2 units beyond it. The directrix position/orientation sign is not specified; the two possible parabolas are (y+2)²=±6(x−(4∓3/2))."),
    q("ex-9-1-q6", 6, "Find intersections: (a) y²+3x=−8 with x−y+2=0; (b) x²=2y with x−y−2=0.",
      "(a) From the line x=y−2. Substitute: y²+3y−6=0, so y=(−3±√33)/2 and x=y−2. (b) y=x−2; substitute x²=2x−4 gives x²−2x+4=0, whose discriminant is negative; there are no real intersections."),
    q("ex-9-1-q7", 7, "Find c for tangency: (a) x−y+c=0 to y²=9x; (b) x−y+c=0 to x²=(2/3)y.",
      "(a) Put x=y−c into y²=9x: y²−9y+9c=0. Tangency requires discriminant 81−36c=0, so c=9/4. (b) Put y=x+c into x²=(2/3)y: 3x²−2x−2c=0. Tangency requires discriminant 4+24c=0, so c=−1/6."),
    q("ex-9-1-q8", 8, "Find tangent and normal equations: (a) at (3,6) to y²=12x; (b) at (1/2,−2/3) to x²=−3y.",
      "(a) For y²=4px, tangent yy₁=2p(x+x₁); here 4p=12, so 6y=6(x+3), or y=x+3. Normal slope is −y₁/(2p)=−1, so y−6=−(x−3). (b) For x²=4py, 4p=−3; tangent xx₁=2p(y+y₁), giving x/2=−3/2(y−2/3), hence x+3y−2=0. Normal slope=−x₁/(2p)=1/3, so y+2/3=(x−1/2)/3.")
]

u10 = units[9]
ex101 = next(e for e in u10["exercises"] if e["id"] == "ex-10-1")
ex101["problems"] = [
    q("ex-10-1-q1", 1, "Find the order and degree of each ordinary differential equation in parts (a–d) on the textbook page.",
      "The order is the highest derivative present; the degree is its power after the equation is polynomial in derivatives. (a) First order, degree 1. (b) Second order, degree 1. (c) Third order, degree 1. (d) Second order, degree 1."),
    q("ex-10-1-q4", 4, "Solve the initial-value problems: (a) y'=cos x, y(0)=1; (b) y'=x², y(0)=1; (c) y'=1/x, y(2)=0; (d) y'=2xy², y(3)=−1.",
      "Integrate and use the initial condition. (a) y=sin x+C, and y(0)=1 gives y=sin x+1. (b) y=x³/3+C, so y=x³/3+1. (c) y=ln|x|+C; y(2)=0 gives y=ln(x/2) on x>0. (d) Separate: y^{−2}dy=2x dx, so −1/y=x²+C. The condition gives C=−8; therefore y=−1/(x²−8), on the interval containing x=3 where the solution is defined.")
]
ex102 = next(e for e in u10["exercises"] if e["id"] == "ex-10-2")
ex102["problems"] = [
    q("ex-10-2-q1", "1a", "Find the general solution of (dy/dx)²=1−y².",
      "Separate variables: dy/√(1−y²)=±dx. Integrating gives sin^{−1}y=±x+C, equivalently y=sin(±x+C), on intervals where the separation is valid."),
    q("ex-10-2-q1b", "1b", "Find the general solution of e^x(dy/dx)+y=0.",
      "Rewrite y'/y=−e^{−x}. Integrate: ln|y|=e^{−x}+C. Thus y=C e^{e^{−x}}."),
    q("ex-10-2-q1c", "1c", "Solve √(1−x²)dy=√(1−y²)dx.",
      "Separate: dy/√(1−y²)=dx/√(1−x²). Integrating both sides gives sin^{−1}y=sin^{−1}x+C."),
    q("ex-10-2-q5", 5, "A curve has slope dy/dx=1/(1−x) and passes through (4,−3). Determine its equation.",
      "Integrate: y=−ln|1−x|+C. Substitute (4,−3): −3=−ln3+C, so C=−3+ln3. Since the curve passes through x=4>1, y=−3+ln(3/(x−1))."),
    q("ex-10-2-q9", 9, "Oil consumption is dW/dt=1.2e^{0.04t} billion barrels per year. Find the total used over eight years, t=0 to 8.",
      "Integrate the rate: W(8)−W(0)=∫₀⁸1.2e^{0.04t}dt=(1.2/0.04)(e^{0.32}−1)=30(e^{0.32}−1)≈11.32 billion barrels."),
    q("ex-10-2-q10", 10, "The infection rate is dI/dt=100t/(t²+1) people per month. Find the total number infected during the first four months.",
      "Integrate from 0 to 4: I(4)−I(0)=∫₀⁴ 100t/(t²+1)dt=50[ln(t²+1)]₀⁴=50ln17≈141.67 people. The total is about 142 people if rounded to a whole person.")
]
review10 = next(e for e in u10["exercises"] if e["id"] == "ex-10-3")
review10["problems"] = [
    q("ex-10-review-q1", "i", "Find the order of 3(dy/dx)+2y=5.", "The highest derivative is the first derivative. Order = 1."),
    q("ex-10-review-q2", "ii", "Find the degree of (d²y/dx²)²−dy/dx+y=0.", "The highest-order derivative is y''. Its power is 2, so the degree is 2."),
    q("ex-10-review-q3", "iii", "What is a solution containing an arbitrary constant called?", "It is a general solution."),
    q("ex-10-review-q4", "iv", "Solve dy/dx=sin x with y(0)=1.", "Integrate: y=−cos x+C. Since y(0)=1, C=2. Thus y=2−cos x."),
    q("ex-10-review-q5", "v", "Solve y(dy/dx)=cos x with y(0)=−1.", "Multiply by 2: d(y²)/dx=2cos x. Integrate: y²=2sin x+C. The initial condition gives C=1, so y=−√(2sin x+1) on the branch consistent with y(0)=−1."),
    q("ex-10-review-q6", "vi", "Find the differential equation of the orthogonal trajectories of x²+y²=c.", "Differentiate: 2x+2y y'=0, so the family slope is −x/y. The orthogonal slope is y/x, giving dy/dx=y/x. Integrating dy/y=dx/x gives y=Cx, the straight lines through the origin."),
    q("ex-10-review-q7", "vii", "Find the orthogonal trajectories of y²=4ax.", "Differentiate y²=4ax: 2y y'=4a. Since a=y²/(4x), the slope is y'=y/(2x). Orthogonal slope is −2x/y. Solve dy/dx=−2x/y: y dy=−2x dx, hence x²+y²=C.")
]

u12 = units[11]
ex121 = next(e for e in u12["exercises"] if e["id"] == "ex-12-3")
ex121["problems"] = [
    q("ex-12-1-q1", 1, "Find an interval [a,b] on which f(a) and f(b) have opposite signs: (a) e^x−2−x; (b) cos x+1−x; (c) ln x−5+x; (d) x³−10x+23.",
      "Check endpoint values. (a) f(1)=e−3<0 and f(2)=e²−4>0, so [1,2] works. (b) f(0)=2>0 and f(2)=cos2−1<0, so [0,2] works. (c) f(3)=ln3−2<0 and f(4)=ln4−1>0, so [3,4] works. (d) f(−4)=−1<0 and f(−3)=26>0, so [−4,−3] works."),
    q("ex-12-1-q2", 2, "Compute four bisection iterates for the functions and intervals: (a) e^x−2−x on [1,1.8]; (b) cos x+1−x on [0.8,1.6]; (c) ln x−5+x on [3.2,4]; (d) x²−10x+23 on [3.2,4].",
      "At each step take the midpoint and keep the half interval where endpoint signs differ. The first four midpoints are: (a) 1.4, 1.2, 1.1, 1.15; (b) 1.2, 1.4, 1.3, 1.25; (c) 3.6, 3.8, 3.7, 3.65; (d) 3.6, 3.4, 3.5, 3.55."),
    q("ex-12-1-q3", 3, "Compute four Regula Falsi iterates for: (a) f(x)=e^x−x on [−2.4,−1.6]; (b) f(x)=cos x+1−x on [0.8,1.6]; (c) f(x)=x²−10x+23 on [−2.4,−1.6].",
      "The displayed scan appears to have sign or interval inconsistencies in parts (a) and (c): the stated endpoint values do not have opposite signs, so Regula Falsi cannot be started as printed. For (b), apply x_n=(a f(b)−b f(a))/(f(b)−f(a)), retaining the sign-changing subinterval. The four approximations are x₁≈1.270124, x₂≈1.283233, x₃≈1.283426, x₄≈1.283429."),
    q("ex-12-1-q4", 4, "What happens if bisection is applied to f(x)=1/(x−2) on (a) [3,7] and (b) [1,7]?",
      "(a) f(3)>0 and f(7)>0, so the endpoint signs are not opposite and the bisection method cannot start. (b) The endpoint signs are opposite, but f is discontinuous at x=2 and has no zero. Bisection’s continuity requirement fails; repeated midpoints can approach the vertical asymptote rather than a root."),
    q("ex-12-1-q5", 5, "Find the third Newton–Raphson iterate x₃ for: (a) f(x)=x³−3, x₀=1; (b) f(x)=sin x, x₀=1; (c) f(x)=x³+2x−1, x₀=0; (d) f(x)=sin x, x₀=−2.",
      "Use x_{n+1}=x_n−f(x_n)/f'(x_n). (a) x₁=1.666667, x₂≈1.471111, x₃≈1.442812. (b) x₁≈−0.557408, x₂≈0.065936, x₃≈−0.000096. (c) x₁=0.5, x₂≈0.454545, x₃≈0.453398. (d) x₁≈−4.185040, x₂≈−2.467894, x₃≈−3.266186."),
    q("ex-12-1-q6", 6, "Use Newton–Raphson to approximate the roots, continuing until consecutive iterates agree to three decimal places: (a) x³+3x−1=0 on (0,1); (b) x³+2x²−x+1=0 on (−3,−2); (c) ∛(x−3)=x+1 on [−3,−2].",
      "For each equation set F(x)=0 and iterate x_{n+1}=x_n−F(x_n)/F'(x_n), starting within the stated interval. (a) The root is approximately 0.322. (b) The root of x³+2x²−x+1=0 in (−3,−2) is approximately −2.547. (c) Cubing both sides gives (x+1)³=x−3, or F(x)=x³+3x²+2x+4; the root in [−3,−2] is approximately −2.796. Continue the iteration until successive values round to the same three decimals."),
    q("ex-12-1-q7", 7, "Use Maple’s fsolve command to solve 3x²+4x−3=0 with initial guess x₀=0.5.",
      "The quadratic formula gives x=(−2±√13)/3. The root near the initial guess 0.5 is x=(−2+√13)/3≈0.53518. Maple fsolve with x₀=0.5 converges to this root.")
]
review12 = next(e for e in u12["exercises"] if e["id"] == "ex-12-2")
review12["problems"] = [
    q("ex-12-review-q1", "i", "Find the roots of 6x²+5x−6=0.", "Factor: (3x−2)(2x+3)=0. Thus x=2/3 or x=−3/2."),
    q("ex-12-review-q2", "ii", "Approximate the root of f(x)=x²+6x−5=0 as shown among the choices.", "The quadratic formula gives x=−3±√14, approximately 0.742 and −6.742. Neither matches the values visible in the printed options, so the question or choices appear misprinted; verify the polynomial and options against the original page."),
    q("ex-12-review-q3", "iii", "The Newton–Raphson method is also called which method?", "It is the tangent method: each next estimate is where the tangent at the current point meets the x-axis."),
    q("ex-12-review-q4", "iv", "State the Newton–Raphson iterative formula for x₃.", "Set x_{n+1}=x_n−f(x_n)/f'(x_n). In particular, x₃=x₂−f(x₂)/f'(x₂)."),
    q("ex-12-review-q5", "v", "If f(a) and f(c) have opposite signs, where does the root lie?", "For a continuous function, the Intermediate Value Theorem guarantees at least one root in the interval (a,c)."),
    q("ex-12-review-q6", "vi", "At which points does the Newton–Raphson method fail?", "It fails when f'(x_n)=0, which occurs at a stationary point, because the iteration would require division by zero."),
    q("ex-12-review-q7", "vii", "Approximate the positive root of 3t−cos t−1=0 to three decimal places using Regula Falsi.", "Let f(t)=3t−cos t−1. Since f(0)=−2 and f(1)=2−cos1>0, the root is bracketed in [0,1]. Applying Regula Falsi gives t≈0.607 (to three decimal places)."),
    q("ex-12-review-q8", "viii", "Which Maple command solves x²−5x+3=0?", "Use fsolve(x²−5x+3=0, x). It returns the numerical roots (5−√13)/2≈0.697 and (5+√13)/2≈4.303."),
    q("ex-12-review-q9", "ix", "Use bisection on x−sin x−1/2=0 in 1<x<2 to select the listed root approximation.", "Let f(x)=x−sin x−1/2. It is increasing since f'(x)=1−cos x≥0. Numerical bisection gives x≈1.498, so select the closest listed value."),
    q("ex-12-review-q10", "x", "What is another name for the bisection method?", "It is also called the binary chopping method, because each iteration halves the bracketing interval."),
    q("ex-12-review-project", "Project", "Create a quadratic, find its roots with Newton–Raphson, and plot it in Maple; then approximate an integral from −1 to 2 with the trapezoidal rule.", "For example, choose f(x)=x²−1. Its roots are −1 and 1; Newton’s iteration is x_{n+1}=x_n−(x_n²−1)/(2x_n), which converges from a suitable nonzero starting value. Plot f with Maple’s plot command. For the integration part choose g(x)=x², n=6, h=0.5. The trapezoidal estimate is T=0.5[1/2+0.25+0+0.25+1+2.25+4/2]=3.125, compared with exact ∫_{−1}^{2}x²dx=3."),
]
ex122 = next(e for e in u12["exercises"] if e["id"] == "ex-12-4")
ex122["problems"] = [
    q("ex-12-2-q1", 1, "Apply the trapezoidal rule with the stated n and compare with the exact integral: (a) ∫₁³ x² dx, n=4; (b) ∫₀²(x²/2+1)dx, n=4; (c) ∫₁³ dx/x, n=6; (d) ∫₀¹√(1+x²)dx, n=6.",
      "Use h=(b−a)/n and T=h[f(x₀)/2+f(x₁)+…+f(x_{n−1})+f(x_n)/2]. (a) T=8.75; exact=26/3≈8.6667. (b) T=3.375; exact=10/3≈3.3333. (c) T≈1.10675; exact=ln3≈1.09861. (d) T≈1.14943; exact=[x√(1+x²)+ln(x+√(1+x²))]₀¹/2≈1.14779."),
    q("ex-12-2-q2", 2, "Apply composite Simpson’s rule and compare with the exact integral: (a) ∫₂⁴x²dx, n=3; (b) ∫₂³(x²/3−1)dx, n=4; (c) ∫₁³dx/x, n=3; (d) ∫₀¹e^{2x}dx, n=4.",
      "Use Simpson’s 3/8 rule when n=3, and Simpson’s 1/3 rule when n=4. (a) S=56/3≈18.6667, exact for a quadratic. (b) S=10/9≈1.1111, exact for a quadratic. (c) S≈1.10476; exact=ln3≈1.09861. (d) S≈3.19561; exact=(e²−1)/2≈3.19453."),
    q("ex-12-2-q3", 3, "For y=√(1−x²), 0≤x≤1, use the trapezoidal rule with n=4 to approximate ∫₀¹√(1−x²)dx and compare with π/4 using π=3.1.",
      "With h=1/4, the ordinates at x=0,1/4,1/2,3/4,1 are 1, √15/4, √3/2, √7/4, 0. Thus T=(1/4)[1/2+√15/4+√3/2+√7/4]≈0.74893. The exact quarter-circle area using π=3.1 is π/4=0.775, so the trapezoidal estimate is about 0.02607 lower.",
      {"type":"quarter-circle","radius":1,"rule":"trapezoidal","n":4,"title":"Quarter circle y=√(1−x²)"}),
    q("ex-12-2-q4", 4, "Use Simpson’s rule with n=4 for the quarter-circle integral ∫₀¹√(1−x²)dx and compare with π/4 using π=3.1.",
      "Composite Simpson’s rule gives S=(h/3)[f₀+f₄+4(f₁+f₃)+2f₂], h=1/4. Substituting 1, √15/4, √3/2, √7/4, 0 gives S≈0.77090. The comparison value π/4=0.775, so the approximation is about 0.00410 lower.",
      {"type":"quarter-circle","radius":1,"rule":"simpson","n":4,"title":"Quarter circle and Simpson estimate"}),
    q("ex-12-2-q5", 5, "Use Maple commands to approximate the area over [0,2] by (a) the trapezoidal rule and (b) Simpson’s rule.",
      "Set the desired integrand f(x), interval [0,2], and number of subintervals n in Maple’s numerical-integration command, then request the trapezoidal and Simpson approximations. The printed question does not specify an integrand or n, so numerical values cannot be determined from this prompt alone.")
]

u11 = units[10]
ex111 = next(e for e in u11["exercises"] if e["id"] == "ex-11-1")
ex111["problems"] = [
    q("ex-11-1-q1", 1, "If f(x,y)=x²y+xy² and t is real, find: (a) f(0,0); (b) f(−1,0); (c) f(0,−1); (d) f(t,0); (e) f(t,t²); (f) f(1−t,t).", "Use f(x,y)=xy(x+y). (a) 0. (b) 0. (c) 0. (d) 0. (e) t·t²·(t+t²)=t⁴+t⁵. (f) with x=1−t,y=t, x+y=1, so f=t(1−t)."),
    q("ex-11-1-q2", 2, "For f(x,y,z)=x²ye^{2z}+(x+y−z)², find: (a) f(0,0,0); (b) f(1,−1,1); (c) f(−1,1,−1); (d) ∂f/∂x at (x,x,x); (e) ∂f/∂y at (1,y,1); (f) ∂f/∂z at (1,1,z²).", "(a) 0. (b) 1−e². (c) 1+e^{−2}. The partial derivatives are f_x=2xye^{2z}+2(x+y−z), f_y=x²e^{2z}+2(x+y−z), and f_z=2x²ye^{2z}−2(x+y−z). (d) Substitution gives 2x²e^{2x}+2x. (e) e²+2y. (f) 2e^{2z²}+2z²−4."),
    q("ex-11-1-q3", 3, "Find f_x and f_y: (a) f=sin(x²)cos y; (b) f=√(3x²+y⁴); (c) f=xy²tan^{−1}y; (d) f=x³+x²y+xy²+y³; (e) f=sin^{−1}(xy); (f) f=x²e^{x+y}cos y.", "Treat the other variable as constant. (a) f_x=2x cos(x²)cos y; f_y=−sin(x²)sin y. (b) f_x=3x/√(3x²+y⁴); f_y=2y³/√(3x²+y⁴). (c) f_x=y²tan^{−1}y; f_y=2xy tan^{−1}y+xy²/(1+y²). (d) f_x=3x²+2xy+y²; f_y=x²+2xy+3y². (e) f_x=y/√(1−x²y²); f_y=x/√(1−x²y²). (f) f_x=e^{x+y}(2x+x²)cos y; f_y=x²e^{x+y}(cos y−sin y)."),
    q("ex-11-1-q4", 4, "A production function is z=f(x,y)=x^{0.7}y^{0.3}, where x is labor and y is capital. Find the marginal productivity of labor and capital.",
      "Hold y constant when differentiating with respect to x: ∂z/∂x=0.7x^{−0.3}y^{0.3}. Hold x constant when differentiating with respect to y: ∂z/∂y=0.3x^{0.7}y^{−0.7}."),
    q("ex-11-1-q5", 5, "For the Canadian production function z=f(x,y)=x^{0.4}y^{0.6}, find marginal productivity of labor and capital.",
      "Treat the other input as a constant in each partial derivative: ∂z/∂x=0.4x^{−0.6}y^{0.6}; ∂z/∂y=0.6x^{0.4}y^{−0.4}."),
    q("ex-11-1-q6", 6, "For f(x,y)=x³y+xy³, find f_x and f_y by the definition of partial derivatives.",
      "By definition, f_x=lim_{h→0}[f(x+h,y)−f(x,y)]/h. Expanding and cancelling gives f_x=3x²y+y³. Similarly, f_y=lim_{k→0}[f(x,y+k)−f(x,y)]/k=x³+3xy².")
]
ex112 = next(e for e in u11["exercises"] if e["id"] == "ex-11-2")
ex112["problems"] = [
    q("ex-11-2-q1", 1, "Determine whether the functions in parts (a–d) are homogeneous, as asked in Exercise 11.2.", "Test each expression by replacing x,y with tx,ty and checking whether the result is t^n times the original expression for a fixed n. From the scan, part (d), (x²+3y²)^{1/3}, is homogeneous of degree 2/3. The low-resolution scan obscures symbols in parts (a–c); their exact formulas need a clearer page image for a reliable classification."),
    q("ex-11-2-q2", 2, "Verify Euler’s theorem for: (a) z=ax²+2hxy+by²; (b) z=(x²+xy+y²)^{−1}.", "(a) z is homogeneous of degree 2. Its partials are z_x=2ax+2hy and z_y=2hx+2by. Then xz_x+yz_y=2ax²+4hxy+2by²=2z. (b) Let Q=x²+xy+y² and z=Q^{−1}. Then xz_x+yz_y=−Q^{−2}[x(2x+y)+y(x+2y)]=−2Q/Q²=−2z, agreeing with degree −2."),
    q("ex-11-2-q3", 3, "If u=f(y/x), show that x(∂u/∂x)+y(∂u/∂y)=0.", "Let v=y/x. Then u_x=f'(v)(−y/x²) and u_y=f'(v)/x. Hence xu_x+yu_y=−(y/x)f'(v)+(y/x)f'(v)=0."),
    q("ex-11-2-q4", 4, "If z=xy f(x/y), show that x(∂z/∂x)+y(∂z/∂y)=2z.", "The factor xy has degree 2 and x/y is unchanged when (x,y) is scaled by the same factor. Thus z(tx,ty)=t²z(x,y), so z is homogeneous of degree 2. Euler’s theorem gives xz_x+yz_y=2z."),
    q("ex-11-2-q5", 5, "If u=tan^{−1}((x²+y²)/(x+y)), show that xu_x+yu_y=sin(u)cos(u).", "Set v=(x²+y²)/(x+y)=tan u. The numerator has degree 2 and denominator degree 1, so v is homogeneous of degree 1. Euler’s theorem gives xv_x+yv_y=v. Since u=tan^{−1}v, u_x=v_x/(1+v²) and u_y=v_y/(1+v²). Therefore xu_x+yu_y=v/(1+v²)=tan u/(1+tan²u)=sin u cos u.")
]
review11 = next(e for e in u11["exercises"] if e["id"] == "ex-11-3")
review11["problems"] = [
    q("ex-11-review-q1", "i", "In z=f(x,y), x and y are called what?", "They are independent variables; z is the dependent variable."),
    q("ex-11-review-q2", "ii", "If f(x,y)=√(x²+y²−1), find f(1,5).", "f(1,5)=√(1+25−1)=√25=5."),
    q("ex-11-review-q3", "iii", "If f(x,y)=x²+y², find ∂f/∂x.", "Treat y as constant: f_x=2x."),
    q("ex-11-review-q4", "iv", "Find ∂/∂x [1/(x+y)].", "Treat y as constant: −1/(x+y)²."),
    q("ex-11-review-q5", "v", "State Euler’s theorem for a homogeneous function z=f(x,y) of degree n.", "Euler’s theorem states x f_x+y f_y=nf(x,y)."),
    q("ex-11-review-q6", "vi", "A function of more than one independent variable is called what?", "A multivariable function."),
    q("ex-11-review-q7", "vii", "If f(x,y)=√(x³+y²), find f(1,0).", "f(1,0)=√(1+0)=1."),
    q("ex-11-review-q8", "viii", "If f(x,y)=cos y·e^x, find f_y.", "Treat e^x as constant: f_y=−e^x sin y."),
    q("ex-11-review-q9", "ix", "If f(x,y)=3xy²+x²y², find f_x.", "Treat y as constant: f_x=3y²+2xy².")
]

for unit in units:
    for exercise in unit.get("exercises", []):
        exercise.setdefault("problems", [])

json_text = json.dumps(units, ensure_ascii=False, indent=2)
result = text[:start] + json_text + text[end:]
DATA.write_text(result, encoding="utf-8")
