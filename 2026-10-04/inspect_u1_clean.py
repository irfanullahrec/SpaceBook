# -*- coding: utf-8 -*-
import json
import re

with open(r'D:\SpaceBook\SpaceBook Web\js\english_8_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove comment and JS variable assignment
clean = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
clean = re.sub(r'const\s+ENGLISH_8_DATA\s*=\s*', '', clean).strip()
clean = clean.rstrip(';\n ')

data = json.loads(clean)
u1 = data[0]
print("Unit 1 keys:", list(u1.keys()))
if 'exercise' in u1:
    print("Exercise keys:", list(u1['exercise'].keys()))
if 'vocabulary' in u1:
    print("Vocabulary count:", len(u1['vocabulary']))
    print("Vocabulary item 0:", u1['vocabulary'][0])
