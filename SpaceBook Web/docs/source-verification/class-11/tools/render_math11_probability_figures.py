from pathlib import Path
import re,sys,xml.etree.ElementTree as ET,pymupdf
ROOT=Path(__file__).resolve().parents[1]
APP=ROOT.parents[2]
# Draw both intersection boundaries above the shading so neither is hidden.
p=ROOT/'math/pages/p195.txt';before=p.read_text(encoding='utf-8')
extra='<g fill="none" stroke="#075985" stroke-width="2"><circle cx="340" cy="115" r="55"/><circle cx="400" cy="115" r="30"/></g>'
if extra not in before:
    needle='<g font-family="Arial,sans-serif" font-size="18"'
    assert before.count(needle)==1
    assert p.read_text(encoding='utf-8')==before
    p.write_text(before.replace(needle,extra+needle),encoding='utf-8')
for n in list(map(int,sys.argv[1:])) or [193,195,196]:
    source=(ROOT/f'math/pages/p{n}.txt').read_text(encoding='utf-8')
    figures=re.findall(r'<svg\b[\s\S]+?</svg>',source)
    assert len(figures)==1
    svg=figures[0];ET.fromstring(svg)
    doc=pymupdf.open(stream=svg.encode(),filetype='svg')
    pdf=pymupdf.open(stream=doc.convert_to_pdf(),filetype='pdf')
    pdf[0].get_pixmap(matrix=pymupdf.Matrix(1.6,1.6)).save(str(APP/f'tmp/class-11/math/probability-{n}.png'))
print('Three coded probability figures checked and rendered.')
