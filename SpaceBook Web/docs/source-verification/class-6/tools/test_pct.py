import sys
sys.path.insert(0, 'tools')
import solve
for t in ['x - 5 = 4', '3x + x = 48', '2x + 3 = 43', r'\frac{x}{2} = 16', '5a + 2 = 32', '7 + x = 4 + 2x', '6x - 79 = x', '123 + x = 4x + 75', r'\frac{(4 + x)}{10} = 3',
          '2.2x + 5.7 = 22.5', r'\frac{3}{4}y - 2 = 7', '3(x + 8) = 14', '8 - x = 1']:
    r = solve.generate('lineq', t)
    print(t, '->', r['answer'], '|', ' / '.join(s.get('m', '') for s in r['steps']))
