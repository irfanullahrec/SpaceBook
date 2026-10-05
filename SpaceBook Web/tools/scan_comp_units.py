import sys, re
sys.path.append('tools')
from scan_comp12 import all_paras

u_matches = []
for i, p in enumerate(all_paras):
    m = re.match(r'^UNIT[\s\-]*(\d+)\s*(.*)', p, re.IGNORECASE)
    if m:
        u_matches.append((int(m.group(1)), i, p))

for u in u_matches:
    print(f"Unit {u[0]} at para {u[1]}: '{u[2]}'")
