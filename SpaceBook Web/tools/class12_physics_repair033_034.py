"""Re-upsert corrected math-delimited records for already checkpointed pages 33–34."""
from class12_source_review import upsert, sync_companions
import class12_physics_page033 as p33
import class12_physics_page034 as p34

law_layout = [
    {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
    {'type': 'paragraph', 'indices': [2]}, {'type': 'heading', 'indices': [3]},
    {'type': 'visual'}, {'type': 'paragraph', 'indices': [4]}, {'type': 'heading', 'indices': [5]},
    {'type': 'equation', 'indices': [6]}, {'type': 'equation', 'indices': [7]},
    {'type': 'paragraph', 'indices': [8]}, {'type': 'equation', 'indices': [9]},
    {'type': 'paragraph', 'indices': [10]}, {'type': 'visual'},
]
law_visuals = {
    'diagramSvg': p33.ohm_portrait('en') + p33.ohm_graphs('en'),
    'diagramSvgUrdu': p33.ohm_portrait('ur') + p33.ohm_graphs('ur'),
    'diagramSvgPashto': p33.ohm_portrait('ps') + p33.ohm_graphs('ps'),
}
law = p33.create('phys12-unit12-ohms-law56-57', '12.2 Ohm’s law', 56, p33.OHM,
                 law_layout, ('12.2 اوم کا قانون', '12.2 د اوم قانون'), law_visuals, [56, 57])

example_layout = [
    {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
    {'type': 'heading', 'indices': [2]}, {'type': 'equation', 'indices': [3]},
    {'type': 'heading', 'indices': [4]}, {'type': 'equation', 'indices': [5]},
    {'type': 'heading', 'indices': [6]}, {'type': 'equation', 'indices': [7]},
    {'type': 'equation', 'indices': [8]}, {'type': 'equation', 'indices': [9]},
]
example = p34.make_record(
    'phys12-unit12-example12258', 'Example 12.2 — TV receiver load resistance', 58,
    p34.EXAMPLE, example_layout,
    ('مثال 12.2 — ٹی وی ریسیور کی لوڈ مزاحمت', 'بېلګه 12.2 — د ټلویزیون د ریسېور د بار مقاومت'))
resistance_layout = [
    {'type': 'heading', 'indices': [0]}, {'type': 'paragraph', 'indices': [1]},
    {'type': 'paragraph', 'indices': [2]}, {'type': 'equation', 'indices': [3]},
    {'type': 'heading', 'indices': [4]}, {'type': 'paragraph', 'indices': [5]},
    {'type': 'orderedList', 'indices': [6, 7, 8, 9]}, {'type': 'paragraph', 'indices': [10]},
    {'type': 'equation', 'indices': [11]},
]
resistance = p34.make_record(
    'phys12-unit12-resistance-factors59', '12.3 Electrical resistance and its factors', 59,
    p34.RESISTANCE, resistance_layout,
    ('12.3 برقی مزاحمت اور اس کے عوامل', '12.3 برېښنايي مقاومت او اغېزمن عوامل'))
upsert([law[0], example[0], resistance[0]], [law[1], example[1], resistance[1]], chapter_index=1)

example122 = {
    'id': 'textbook-example-12-2', 'num': '12.2', 'title': 'Example 12.2',
    'problem': p34.EXAMPLE[1][0], 'given': [p34.EXAMPLE[3][0]], 'required': [p34.EXAMPLE[5][0]],
    'steps': [p34.EXAMPLE[7][0], p34.EXAMPLE[8][0], p34.EXAMPLE[9][0]],
    'answer': r'113.3\times10^6\,\Omega', 'solutionOrigin': 'textbook',
    'sourceReferences': [{'pdfPage': 34, 'printedPage': 58, 'sourcePdf': p34.SOURCE}],
}
sync_companions(chapter_index=1, formulas=[
    {'id': 'phys12-unit12-eq-12.2', 'name': 'Ohm’s law', 'number': '12.2',
     'formula': p33.OHM[6][0] + ' ' + p33.OHM[7][0], 'latex': r'V=IR',
     'sourceReferences': [{'pdfPage': 33, 'printedPage': 57, 'sourcePdf': p33.SOURCE}]},
    {'id': 'phys12-unit12-ohmic-slope', 'name': 'Slope of an ohmic conductor’s I–V graph',
     'formula': p33.OHM[9][0], 'latex': r'\tan\theta=\frac{I}{V}=\frac{1}{R}',
     'sourceReferences': [{'pdfPage': 33, 'printedPage': 57, 'sourcePdf': p33.SOURCE}]},
    {'id': 'phys12-unit12-ohm-definition', 'name': 'Definition of one ohm',
     'formula': p34.RESISTANCE[3][0], 'latex': r'1\,\Omega=\frac{1\,\mathrm V}{1\,\mathrm A}',
     'sourceReferences': [{'pdfPage': 34, 'printedPage': 59, 'sourcePdf': p34.SOURCE}]},
], definitions=[
    {'term': 'Ohm’s law', 'definition': p33.OHM[1][0] + ' ' + p33.OHM[2][0],
     'definitionUrdu': p33.OHM[1][1] + ' ' + p33.OHM[2][1],
     'definitionPashto': p33.OHM[1][2] + ' ' + p33.OHM[2][2],
     'sourceReferences': [{'pdfPage': 33, 'printedPage': 56, 'sourcePdf': p33.SOURCE}]},
    {'term': 'Resistance', 'definition': p34.RESISTANCE[1][0] + ' ' + p34.RESISTANCE[2][0],
     'definitionUrdu': p34.RESISTANCE[1][1] + ' ' + p34.RESISTANCE[2][1],
     'definitionPashto': p34.RESISTANCE[1][2] + ' ' + p34.RESISTANCE[2][2],
     'sourceReferences': [{'pdfPage': 34, 'printedPage': 59, 'sourcePdf': p34.SOURCE}]},
], worked_examples=[example122])
