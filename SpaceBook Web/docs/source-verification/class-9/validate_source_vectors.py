import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET
OUT=Path(__file__).resolve().parent
count=0
for file in sorted(OUT.glob('physics-page-*.json')):
    page=json.loads(file.read_text(encoding='utf-8'))
    for section in page.get('sections',[]):
        for block in section.get('blocks',[]):
            for field in ['svg','svgUrdu','svgPashto']:
                if not block.get(field):continue
                roots=[]
                depth=0
                for token in re.finditer(r'<svg\b[^>]*>|</svg>',block[field]):
                    if token.group().startswith('</'):
                        depth-=1
                        assert depth>=0
                        if depth==0:roots.append(block[field][start:token.end()])
                    else:
                        if depth==0:start=token.start()
                        depth+=1
                assert depth==0, 'Unbalanced SVG tags'
                for svg in roots:
                    try:ET.fromstring(svg)
                    except ET.ParseError as error:raise ValueError(f'{file.name} {block.get("id")} {field}: {error}') from error
                assert '<image' not in block[field] and '<img' not in block[field]
                count+=1
print(f'PASS: {count} coded visual variants are valid XML/HTML fragments with no raster embedding.')
