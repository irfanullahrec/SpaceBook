"""Render coded source figures for local visual comparison without a browser."""
import json,sys
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[3]
for n in map(int,sys.argv[1:]):
    record=json.loads((ROOT/f'docs/source-verification/class-11/chemistry-page-{n}.json').read_text(encoding='utf-8'))
    for i,figure in enumerate(record.get('figures',[])):
        with pymupdf.open(stream=figure['svg'].encode(),filetype='svg') as svg:
            with pymupdf.open(stream=svg.convert_to_pdf(),filetype='pdf') as pdf:
                output=ROOT/f'tmp/class-11/chemistry-p{n}-fig{i+1}-qa.png'
                pdf[0].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(str(output))
                print(output)
