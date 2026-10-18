import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\SpaceBook\2026-10-04\english_8_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    if pno in [19, 22, 24, 26, 29, 30, 31, 35, 39, 40, 42, 45, 46, 49, 51, 52, 54, 56]:
        print(f"=== PAGE {pno} ===")
        print(p['text'][:500])
