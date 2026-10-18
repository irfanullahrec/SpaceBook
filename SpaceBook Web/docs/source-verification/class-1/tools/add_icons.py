"""Insert icon entries (lines of "'name': f'...'," at 8-space indent) from a text file into figs1._icon before 'tick'."""
import sys
add = open(sys.argv[1], encoding='utf-8').read()
s = open('figs1.py', encoding='utf-8').read()
anchor = "        'tick':"
assert anchor in s
s = s.replace(anchor, add.rstrip('\n') + '\n' + anchor, 1)
open('figs1.py', 'w', encoding='utf-8').write(s)
print('ok')
