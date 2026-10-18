"""Hard-link each Class 7 book's JPG scans as D:/SpaceBook/_cls7_jpg/<subj>/NNN.jpg (0-based, in page order).

Page order = the last integer in the file name ("..._page_007.jpg" -> 7, "000 (12).jpg" -> 12).
Prints any book whose numbering has gaps or duplicates so it can be checked by eye.
"""
import os, re
from pathlib import Path

BOOKS = Path('D:/SpaceBook/Books/7th')
OUT = Path('D:/SpaceBook/_cls7_jpg')
FOLDERS = {'eng': '7th English', 'sci': '7th General Science', 'urdu': '7th Urdu', 'comp': '7th CS',
           'geo': '7th Geography', 'hist': '7th History', 'isl': '7th Islamiat', 'quran': '7th M Q',
           'arabic': '7th Arabi', 'drawing': '7th Drawing', 'hpe': '7th HPE'}

for subj, folder in FOLDERS.items():
    src = BOOKS / folder / 'JPG'
    files = [f for f in src.iterdir() if f.suffix.lower() in ('.jpg', '.jpeg')]
    keyed = sorted((int(re.findall(r'\d+', f.stem)[-1]), f.name, f) for f in files)
    nums = [k for k, _, _ in keyed]
    gaps = sorted(set(range(nums[0], nums[-1] + 1)) - set(nums))
    dups = sorted({n for n in nums if nums.count(n) > 1})
    dest = OUT / subj
    dest.mkdir(parents=True, exist_ok=True)
    for i, (_, _, f) in enumerate(keyed):
        target = dest / f'{i:03}.jpg'
        if not target.exists():
            os.link(f, target)
    note = (f' gaps={gaps}' if gaps else '') + (f' dups={dups}' if dups else '')
    print(f'{subj:8} {len(keyed):4} pages (file numbers {nums[0]}..{nums[-1]}){note}')
