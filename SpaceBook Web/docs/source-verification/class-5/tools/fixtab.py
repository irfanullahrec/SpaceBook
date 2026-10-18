"""Repair LaTeX commands whose backslash became a control character (\t -> TAB) in page files."""
import sys
for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read()
    t = s.replace('\textcolor', '\\textcolor').replace('\times', '\\times').replace('\text{', '\\text{')
    if t != s:
        open(f, 'w', encoding='utf-8').write(t)
        print('fixed', f)
