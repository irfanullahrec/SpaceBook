# -*- coding: utf-8 -*-
import sys
import re

with open(r'D:\SpaceBook\SpaceBook Web\js\english_8_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# find keys of unit 1
m = re.search(r'const ENGLISH_8_DATA\s*=\s*\[\s*\{', text)
if m:
    print("Found ENGLISH_8_DATA")

# Let's inspect unit 1 keys
import json
content = text.replace("const ENGLISH_8_DATA = ", "").rstrip(";\n ")
try:
    data = json.loads(content)
    print("Num units:", len(data))
    for i, u in enumerate(data):
        print(f"Unit {u.get('number')}: {u.get('title')} | keys: {list(u.keys())}")
        if 'exercise' in u:
            print(f"  exercise keys: {list(u['exercise'].keys())}")
except Exception as e:
    print("JSON load error:", e)
