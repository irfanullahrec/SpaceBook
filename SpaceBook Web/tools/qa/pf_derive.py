"""Partial fractions for Class 10 Maths Ex 4.1 / 4.2 parts that the printed key does not give (sympy, verified by recombining)."""
import sympy as sp
x = sp.symbols('x')
E41 = {1: (3*x-2)/(2*x**2-x), 4: x/(x**2+4*x-5), 6: (x**2+5*x+3)/((x**2-1)*(x+1)), 8: (2*x-1)/(x*(x-3)**2), 10: x**2/((x-1)**2*(x+1))}
E42 = {1: 1/(x*(x**2+1)), 3: (2*x+1)/((x**2+1)*(x-1)), 5: (3*x-2)/((x+4)*(3*x**2+1)), 7: (5*x**2-4*x+8)/((x**2+1)**2*(x-2)),
       9: 8*x**2/((x**2+1)*(1-x**4)), 10: (2*x**2+4)/((x**2+1)**2*(x-1))}
for name, d in (('4.1', E41), ('4.2', E42)):
    out = []
    for k, f in d.items():
        a = sp.apart(f, x)
        assert sp.simplify(a - f) == 0
        out.append(f'({k}) ${sp.latex(a)}$')
    print(name, '; '.join(out))
