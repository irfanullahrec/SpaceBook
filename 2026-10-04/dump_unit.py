import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

start_p = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end_p = int(sys.argv[2]) if len(sys.argv) > 2 else 60

with open(r'd:\SpaceBook\2026-10-04\english_8_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pno = p['page_num']
    if start_p <= pno <= end_p:
        print(f"=== PAGE {pno} ===")
        print(p['text'])
