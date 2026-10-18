import json
from class12_source_review import ROOT, upsert, section, checkpoint
from physics_agent2_translations import TRANSLATIONS, TITLES

COPIER = '''<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" role="img" aria-labelledby="phys12-opening-copier-title" style="width:100%;max-width:680px;height:auto"><title id="phys12-opening-copier-title">Photocopier with its document cover raised and a hand placing a page on the glass</title><g stroke="#334155" stroke-width="2" stroke-linejoin="round"><path d="M80 88L342 61 411 112 143 145Z" fill="#dce5e9"/><path d="M143 145L411 112V278L143 294Z" fill="#f8fafc"/><path d="M80 88L143 145V294L80 245Z" fill="#64748b"/><path d="M158 174L393 148V201L158 219ZM158 223L393 203V258L158 277Z" fill="#e2e8f0"/><path d="M176 187V198M176 239V250" stroke-width="5"/><path d="M89 100L138 143 138 207 96 170Z" fill="#0f172a"/><path d="M103 132L125 151V169L103 152Z" fill="#7dd3fc"/><path d="M87 79L348 53 358 17 104 37Z" fill="#475569"/><path d="M104 37L358 17 348 46 98 69Z" fill="#111827"/><path d="M115 85L329 67 374 109 160 128Z" fill="#b8d8de"/><path d="M175 90L299 79 334 108 207 119Z" fill="white"/><path d="M424 62L642 39 653 79 444 113Z" fill="#4b8061" stroke="none"/><path d="M440 90C424 80 407 87 396 91L350 107C338 112 336 122 349 123L382 116 359 137C352 146 359 153 368 148L397 130 380 151C374 160 383 166 391 158L412 141 400 160C396 169 406 173 413 166L440 139C453 128 455 105 440 90Z" fill="#d7ab87"/><path d="M418 111L396 125M405 105L380 116" stroke="#a87c5a"/><path d="M456 174L590 159 643 197 509 218Z" fill="#e2e8f0"/><path d="M509 218L643 197V283L509 299Z" fill="#f1f5f9"/><path d="M456 174L509 218V299L456 260Z" fill="#94a3b8"/><path d="M482 164L599 150 610 127 494 137Z" fill="#334155"/><path d="M527 239L624 224M527 271L624 256"/><path d="M540 244V254M540 276V286" stroke-width="4"/></g></svg></figure>'''

if __name__ == '__main__':
    old = json.loads((ROOT / 'docs/source-verification/physics-agent2-pages.json').read_text(encoding='utf-8'))
    contents = next(item for item in old if item['id'] == 'phys12-front-contents')
    outcomes = next(item for item in old if item['id'] == 'phys12-front-outcomes1')
    outcomes['paragraphs'][3] = outcomes['paragraphs'][3].replace('distance r from a point charge q.', "distance 'r' from a point charge 'q'.")
    outcomes['objectives'] = outcomes['paragraphs'][2:]
    outcomes['diagramHtml'] = COPIER
    pairs = [(text, *pair) for text, pair in zip(outcomes['paragraphs'], TRANSLATIONS[outcomes['id']])]
    revised = section(outcomes, pairs,
                      [{'type': 'heading', 'indices': [0]}, {'type': 'visual'},
                       {'type': 'paragraph', 'indices': [1]}, {'type': 'list', 'indices': list(range(2,10))}],
                      TITLES[outcomes['id']])
    revised['kind'] = 'learning_outcomes'
    revised['diagramSvg'] = COPIER
    revised['content'] += COPIER
    upsert([outcomes], [revised])
    checkpoint(5, 'corrected_verified', [contents['id'], outcomes['id']],
               'Complete spread rendered at 3x and inspected. Table title, column labels, all eleven content rows and page numbers compared against existing semantic table: unchanged. All eight outcomes and heading compared; source quotation marks around r and q restored. Photocopier opening illustration reconstructed in native inline SVG, no source raster. Existing local KaTeX equation engine now formats formulas in Physics12 sourceLayout English/Urdu/Pashto output without changing other subject defaults. Header/footer distribution notice and printed page reference accounted for; background watermark excluded.',
               printed_pages=[1])
