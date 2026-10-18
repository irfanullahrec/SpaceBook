from pathlib import Path
p = Path('tools/solve.py')
s = p.read_text(encoding='utf-8')
i = s.index("    sub_tex = re.sub(r'(?<![\\a-zA-Z])")
j = s.index('\n', i)
new = ("    sub_tex = re.sub(r'(\\[a-zA-Z]+)|([a-zA-Z])', lambda m: m.group(1) if m.group(1) else "
       "(f'({vals[m.group(2)]})' if m.group(2) in vals else m.group(2)), tex)")
s = s[:i] + new + s[j:]
p.write_text(s, encoding='utf-8')
print(new)
