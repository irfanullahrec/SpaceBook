"""pdfpg.py SUBJ N [N...] [--dpi 150] : render 0-based page N of a single-page-per-page Class 8 PDF to _render/<SUBJ>N.png.
SUBJ keys: sci urdu comp geo hist isl quran arabic drawing hpe pashto (PDF located by glob in Books/8th/<folder>/PDF, largest file)."""
import sys
from pathlib import Path
import pymupdf
FOLDERS = {'sci': '8th General Science', 'urdu': 'Urdu', 'comp': '8th CS', 'geo': '8th Geography', 'hist': '8th History',
           'isl': '8th Islamiat', 'quran': '8th M Q', 'arabic': '8th Arabi', 'drawing': '8th Drawing', 'hpe': '8th HPE', 'pashto': '8th PAshto'}
OUT = Path(__file__).resolve().parents[1] / '_render'
args = sys.argv[1:]
dpi = 150
if '--dpi' in args:
    i = args.index('--dpi'); dpi = int(args[i + 1]); del args[i:i + 2]
subj = args[0]
pdfs = sorted(Path('D:/SpaceBook/Books/8th', FOLDERS[subj], 'PDF').glob('*.pdf'), key=lambda p: -p.stat().st_size)
doc = pymupdf.open(pdfs[0])
for a in args[1:]:
    n = int(a)
    doc[n].get_pixmap(dpi=dpi).save(OUT / f'{subj}{n}.png')
    print(subj, n, 'of', len(doc))
