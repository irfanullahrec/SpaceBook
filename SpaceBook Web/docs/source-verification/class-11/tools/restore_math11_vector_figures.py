"""Restore the four instructional figures incorrectly marked as decoration."""
from pathlib import Path
from math11_vector_figures import source_figures,construction
import pymupdf
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
file=root/'math/pages/p084.txt'
before=file.read_text(encoding='utf-8')
figures=source_figures()
if '@deco figures beside the questions:' in before:
    lines=[]
    for line in before.splitlines():
        if line.startswith('@deco figures beside the questions:'):continue
        lines.append(line)
        if line.startswith('q '):
            no=int(line.split()[1])
            if no in figures:
                lines.extend([f'svg Exercise 3.1 — question {no} || مشق 3.1 — سوال {no} || تمرین 3.1 — پوښتنه {no}',figures[no],'endsvg'])
    assert file.read_text(encoding='utf-8')==before
    file.write_text('\n'.join(lines)+'\n',encoding='utf-8')
else:
    assert all(svg in before for svg in figures.values()),'Source page changed; inspect before repair'
out=root.parents[2]/'tmp/class-11/math'
for name,svg in list((f'source-q{n}',s) for n,s in figures.items())+[('answer-q2',construction())]:
    ET.fromstring(svg)
    assert '<image' not in svg and '<script' not in svg and '<foreignObject' not in svg
    doc=pymupdf.open(stream=svg.encode(),filetype='svg')
    pdf=pymupdf.open(stream=doc.convert_to_pdf(),filetype='pdf')
    pdf[0].get_pixmap(matrix=pymupdf.Matrix(2,2)).save(str(out/f'{name}.png'))
print('Four coded source figures restored; five SVG previews rendered for inspection.')
