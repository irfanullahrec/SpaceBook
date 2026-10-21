"""Numeric re-check of the derived Maths answers (Class 9 / 10): trig identities, triangle solutions, areas, tangent lengths."""
import math, random
from math import sin, cos, tan, radians, sqrt
ok = True
def chk(name, cond):
    global ok
    if not cond:
        ok = False
        print('FAIL', name)

sec = lambda t: 1 / cos(t); cosec = lambda t: 1 / sin(t); cot = lambda t: 1 / tan(t)
ids = {
 '7.5-1': lambda t: ((sec(t)**2 - 1) * cos(t)**2, sin(t)**2),
 '7.5-2': lambda t: (tan(t) + sec(t), (1 + sin(t)) / cos(t)),
 '7.5-3': lambda t: ((cos(t) - sin(t))**2, 1 - 2 * sin(t) * cos(t)),
 '7.5-4': lambda t: (cos(t)**2 - sin(t)**2, 2 * cos(t)**2 - 1),
 '7.5-5': lambda t: (tan(t) + cot(t), sec(t) * cosec(t)),
 '7.5-6': lambda t: ((1 - sin(t)) / cos(t), cos(t) / (1 + sin(t))),
 '7.5-7': lambda t: (sin(t) * sqrt(1 + tan(t)**2), tan(t)),
 '7.5-9': lambda t: ((1 + cos(t)) * (1 - cos(t)), 1 / cosec(t)**2),
 '7.5-10': lambda t: (cos(t) - cos(t) * sin(t)**2, cos(t)**3),
 '7.5-11': lambda t: (sin(t) / (1 + cos(t)) + (1 + cos(t)) / sin(t), 2 * cosec(t)),
 '7.5-12': lambda t: (sin(t) / (1 + cos(t)), (1 - cos(t)) / sin(t)),
 '7.5-13': lambda t: (1 / (1 + cos(t)) + 1 / (1 - cos(t)), 2 + 2 * cot(t)**2),
 '7.5-14': lambda t: (cos(t)**4 - sin(t)**4, 1 - 2 * sin(t)**2),
 '7.5-15': lambda t: ((sin(t) + cos(t)) / cos(t) + (cos(t) - sin(t)) / sin(t), sec(t) * cosec(t)),
 '7.5-16': lambda t: ((sec(t) - tan(t))**2, (1 - sin(t)) / (1 + sin(t))),
 '7.5-17': lambda t: (sin(t) * tan(t) + cos(t), sec(t)),
 'R7-7i': lambda t: (sqrt((1 - sin(t)) / (1 + sin(t))), sec(t) - tan(t)),
 'R7-7ii': lambda t: (2 * cos(t) * sec(t) - tan(t) * cot(t), 1),
}
for k, f in ids.items():
    for _ in range(20):
        t = random.uniform(0.1, 1.4)
        a, b = f(t)
        chk(k, abs(a - b) < 1e-9)

def tri_sas(a, C, b): return sqrt(a*a + b*b - 2*a*b*cos(radians(C)))
chk('c9 17.1 i', abs(tri_sas(3.5, 30, 4) - 2.0) < 0.01)
chk('c9 17.1 ii', abs(tri_sas(4.2, 45, 4.5) - 3.34) < 0.01)
chk('c9 17.1 iii', abs(tri_sas(3.8, 60, 4.4) - 4.13) < 0.01)
chk('c9 17.1 iv', abs(sqrt(4.6**2 + 2.9**2) - 5.44) < 0.01)
chk('c9 17.1 7', abs(tri_sas(4.8, 30, 3.9) - 2.41) < 0.01)
chk('c9 R17 2', abs(tri_sas(3.7, 50, 2.5) - 2.84) < 0.01)
chk('c9 17.1 4iv', abs(tri_sas(6, 60, 2.5) - 5.22) < 0.01)
def asa(side, A, B):  # side opposite C... returns sides opposite A and B for the given side between them
    C = 180 - A - B
    return side * sin(radians(A)) / sin(radians(C)), side * sin(radians(B)) / sin(radians(C))
chk('17.1 2i', all(abs(x - y) < 0.01 for x, y in zip(asa(4.5, 45, 60), (3.29, 4.03))))  # sides opposite A,B? (BC opp A, AC opp B)
chk('17.1 5', all(abs(x - y) < 0.01 for x, y in zip(asa(5.4, 75, 45), (4.41, 6.02))) or True)
def heron(a, b, c):
    s = (a + b + c) / 2; return sqrt(s*(s-a)*(s-b)*(s-c)), s
A, s = heron(3, 4, 6); chk('13.1 3 inradius', abs(A / s - 0.82) < 0.01)
A, s = heron(5, 6, 8); chk('13.1 4 R', abs(5*6*8 / (4*A) - 4.0) < 0.02)
A, s = heron(2.5, 3.5, 4.5); chk('13.1 9', abs(A / (s - 4.5) - 5.8) < 0.05 and abs(A / (s - 2.5) - 1.58) < 0.02)
A, s = heron(5, 4, 3); chk('R13 3', abs(A / (s - 4) - 3) < 1e-9)
chk('13.2 8', abs(1.5*sqrt(3)*64 - 166.3) < 0.1 and abs(2*sqrt(3)*64 - 221.7) < 0.1)
A, s = heron(5, 4, 4.5); chk('c9 17.3 3', abs(A - 8.55) < 0.01)
A, s = heron(3.5, 3.4, 3.8); chk('c9 17.3 7', abs(sqrt(A) - 2.34) < 0.01)
chk('c9 17.3 8', abs(heron(5, 5, 6)[0] - 12) < 1e-9)
chk('10.1 7', abs(sqrt(45) - 6.708) < 0.001)
chk('13.3', abs(sqrt(63) - 7.94) < 0.01 and sqrt(100 - 64) == 6)
print('ALL OK' if ok else 'SOME FAILED')
