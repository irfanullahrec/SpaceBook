"""Append a [Check] note to printed Class 9 Maths answers that disagree with the working of the question as printed.
The key was typed exactly as printed (verified on the scans of pp314, 319, 324); in these places the printed key belongs to a slightly different question.
    python -X utf8 tools/qa/annotate_key_mismatches.py
"""
import re, time
from pathlib import Path
D = Path(__file__).resolve().parents[2] / 'docs' / 'source-verification' / 'class-9' / 'math' / 'pages'
NOTES = {
 ('1.6', '5'): r"[Check] For the question as printed (3 bags + 4 pens = 257, 4 bags + 3 pens = 324) a bag costs Rs 75 and a pen Rs 8, so a bag and 10 pens cost Rs 155; the printed key belongs to another problem.",
 ('R1', '4'): r"[Check] For $A=\begin{bmatrix}6&-3\\5&-2\end{bmatrix}$: $|A|=3$ and $A^{-1}=\begin{bmatrix}-\frac23&1\\-\frac53&2\end{bmatrix}$; the printed key shows another matrix.",
 ('3.6', '1'): r"[Check] Part (v) evaluated directly is about $4003400.79$; the printed value does not match the printed expression.",
 ('4.3', '1'): r"[Check] Part (iv) for $x+y=7,\ x-y=4$: $x^2+y^2=\dfrac{65}{2}$, $xy=\dfrac{33}{4}$ (the printed key gives $\frac{63}{2},\frac{35}{4}$).",
 ('4.5', '5'): r"[Check] For $3a+\frac1a=4$: $27a^3+\frac1{a^3}=4^3-3(3)(4)=28$ (the printed key gives 52).",
 ('4.5', '6'): r"[Check] For $x-\frac1{2x}=6$: $x^3-\frac1{8x^3}=6^3+3\cdot\frac12\cdot6=225$ (the printed key gives 236).",
 ('4.7', '2'): r"[Check] Part (iii): $\sqrt{240}=4\sqrt{15}$ (the printed key shows $4\sqrt3,\sqrt5$).",
 ('7.1', '1'): r"[Check] For the equations as printed: (ii) $\frac35x-\frac23=2$ gives $x=\frac{40}{9}$; (iii) $6x-5=2x+9$ gives $x=\frac72$; (v) $\frac1{7x+13}=\frac29$ gives $x=-\frac{17}{14}$ (printed key values differ in these three parts).",
 ('7.1', '5'): r"[Check] For the question as printed (father 41, son 9, three times as old): $41+x=3(9+x)$ gives $x=7$ years (the printed key's 95 belongs to Q6).",
 ('7.1', '6'): r"[Check] For the question as printed: $t=u+4$ and $t=2u-1$ give $u=5,\ t=9$, so the number is 95 (the printed key gives 46).",
 ('3.5', '3'): r"[Check] Part (ii): $\log_{\sqrt3}a=\log_{\sqrt3}5+\log_{\sqrt3}8-\log_{\sqrt3}2$ gives $a=rac{5\cdot8}{2}=20$ (the printed key gives 30).",
 ('16.1', '4'): r"[Check] $18\times30$ ft $=540$ ft$^2=77760$ in$^2$; one tile is $64$ in$^2$, so $1215$ tiles are needed (the printed key gives 6720).",
}
done = 0
for f in sorted(D.glob('p3[0-3][0-9].txt')):
    raw = f.read_bytes(); crlf = b'\r\n' in raw
    L = raw.decode('utf-8').replace('\r\n', '\n').split('\n'); ch = False
    for i, l in enumerate(L):
        m = re.match(r'ans (\S+) \| (\d+) \| (.*)$', l)
        if m and (m.group(1), m.group(2)) in NOTES and '[Check]' not in l and '[Derived]' not in l:
            L[i] = l + ' ' + NOTES[(m.group(1), m.group(2))]; ch = True; done += 1
    if ch:
        data = ('\r\n' if crlf else '\n').join(L).encode('utf-8')
        for _ in range(8):
            try:
                f.write_bytes(data); break
            except OSError:
                time.sleep(0.6)
print('annotated', done)
