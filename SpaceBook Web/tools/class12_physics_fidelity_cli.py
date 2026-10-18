"""stdin JSON: {"fix":[[chapterIndex, sectionId, [[old,new,lang],...]],...], "rec":[[pdf,status,evidence,[issues]],...]}"""
import json, sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class12_physics_fidelity_patch import replace_text, record_page
job = json.loads(sys.stdin.buffer.read().decode('utf-8'))
for ci, sid, ch in job.get('fix', []): replace_text(ci, sid, [tuple(c) for c in ch])
for r in job.get('rec', []): record_page(r[0], r[1], r[2], r[3] if len(r) > 3 else None)
