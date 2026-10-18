# -*- coding: utf-8 -*-
"""Flag stored Urdu sentences (per lesson) whose letters are not found in the Word OCR text.  python urdu_diff.py [lesson]"""
import json, re, sys, subprocess, difflib
sys.stdout.reconfigure(encoding='utf-8')
JS = r'D:\SpaceBook\SpaceBook Web\js\urdu_data.js'
U = json.loads(subprocess.check_output(['node', '-e', f"const fs=require('fs'),vm=require('vm');const c={{window:{{}}}};vm.createContext(c);vm.runInContext(fs.readFileSync({json.dumps(JS)},'utf8'),c);process.stdout.write(JSON.stringify(c.URDU_DATA))"]).decode('utf-8'))
def norm(t):
    t = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED]', '', t)          # harakat
    t = t.replace('ي', 'ی').replace('ك', 'ک').replace('ة', 'ہ').replace('ۃ', 'ہ').replace('ھ', 'ھ').replace('ۂ', 'ہ').replace('ئ', 'ی').replace('ے', 'ی')
    return ''.join(ch for ch in t if '\u0600' <= ch <= '\u06FF' and not '\u06F0' <= ch <= '\u06F9' and ch not in '۔،؟؛')
SRC = norm(open('word_text.txt', encoding='utf-8').read())
only = None if __name__ != "__main__" else (int(sys.argv[1]) if len(sys.argv) > 1 else None)
if __name__ == "__main__":
    for u in U:
        if only and u['number'] != only: continue
        bad = tot = 0
        for si, s in enumerate(u.get('sections', [])):
            for sent in re.split(r'(?<=[۔؟!])\s+|\n+', s.get('urdu', '')):
                n = norm(sent)
                if len(n) < 15: continue
                tot += 1
                m = difflib.SequenceMatcher(None, SRC, n, autojunk=False).find_longest_match(0, len(SRC), 0, len(n))
                lo = max(0, m.a - m.b - 30); hi = min(len(SRC), m.a + len(n) - m.b + 30)
                cov = sum(b.size for b in difflib.SequenceMatcher(None, SRC[lo:hi], n, autojunk=False).get_matching_blocks() if b.size >= 3) / len(n)
                if cov < 0.85:
                    bad += 1
                    if only: print(f'  [{si}] cov={cov:.2f}: {sent[:140]}')
        print(f"lesson {u['number']} {u['title'][:30]}: sentences {tot}, flagged {bad}")
    