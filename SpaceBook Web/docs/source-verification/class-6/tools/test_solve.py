import sys
sys.path.insert(0, 'tools')
import solve
cases = [('expand', r'$3 \times 5^2 \times 11^4$'), ('index', r'$1 \times 2 \times 2 \times 7 \times 7 \times 7$'),
         ('hcfpf', '366, 145, 780'), ('hcfdiv', '100, 350, 480'), ('lcmpf', '120, 150,145'), ('lcmdiv', '280, 250, 290'),
         ('opposite', '–5'), ('opposite', '0'), ('opposite', '+14'), ('between', '–4 and +6'), ('between', '–8 and –18'),
         ('between', '+6 and +8'), ('six', '< +5'), ('six', '> –16'), ('square', '77')]
for k, t in cases:
    r = solve.generate(k, t)
    print(k, t, '->', r['answer'][:90], '| steps', len(r['steps']))
