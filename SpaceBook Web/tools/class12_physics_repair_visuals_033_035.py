"""Refresh coded source labels identified during OCR-to-code cross-check."""
from class12_source_review import upsert
import class12_physics_page033 as p33
import class12_physics_page035 as p35

law_layout = [
    {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
    {'type': 'paragraph', 'indices': [2]}, {'type': 'heading', 'indices': [3]},
    {'type': 'visual'}, {'type': 'paragraph', 'indices': [4]}, {'type': 'heading', 'indices': [5]},
    {'type': 'equation', 'indices': [6]}, {'type': 'equation', 'indices': [7]},
    {'type': 'paragraph', 'indices': [8]}, {'type': 'equation', 'indices': [9]},
    {'type': 'paragraph', 'indices': [10]}, {'type': 'visual'},
]
law = p33.create(
    'phys12-unit12-ohms-law56-57', '12.2 Ohm’s law', 56, p33.OHM, law_layout,
    ('12.2 اوم کا قانون', '12.2 د اوم قانون'),
    {'diagramSvg': p33.ohm_portrait('en') + p33.ohm_graphs('en'),
     'diagramSvgUrdu': p33.ohm_portrait('ur') + p33.ohm_graphs('ur'),
     'diagramSvgPashto': p33.ohm_portrait('ps') + p33.ohm_graphs('ps')},
    [56, 57])

resistivity = p35.make_record(
    'phys12-unit12-resistivity60', 'Resistivity and specific resistance', 60,
    p35.RESISTIVITY,
    [{'type': 'equation', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
     {'type': 'paragraph', 'indices': [2]}, {'type': 'visual'}],
    ('مزاحمت النوعی اور مخصوص مزاحمت', 'مخصوص مقاومت او resistivity'), [60],
    {'diagramSvg': p35.material_wire('en'), 'diagramSvgUrdu': p35.material_wire('ur'),
     'diagramSvgPashto': p35.material_wire('ps')})

upsert([law[0], resistivity[0]], [law[1], resistivity[1]], chapter_index=1)
