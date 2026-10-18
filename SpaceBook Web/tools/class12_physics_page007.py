import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions
from physics_agent2_translations import TRANSLATIONS, TITLES

def formula(identity, latex, page, name, legacy=None, number=None):
    entry = {'id': identity, 'name': name, 'formula': r'\('+latex+r'\)',
             'latex': latex, 'note': 'Textbook source equation',
             'sourceReferences': [{'pdfPage': page, 'printedPage': 2 if page == 6 else [4,5]}]}
    if legacy:
        entry['legacyFormula'] = legacy
    if number:
        entry['number'] = number
    return entry

if __name__ == '__main__':
    old = json.loads((ROOT / 'docs/source-verification/physics-agent2-pages.json').read_text(encoding='utf-8'))
    scalar = next(item for item in old if item['id'] == 'phys12-front-coulomb-equations')
    media = next(item for item in old if item['id'] == 'phys12-front-permittivity')
    scalar['printedPage'] = [4,5]
    scalar['paragraphs'][3] = r'\(F\propto\frac{q_1q_2}{r^2}\) ...(11.1)'
    scalar['paragraphs'][1] = r'\(F\propto q_1q_2\) ...(A)'
    scalar['paragraphs'][2] = r'\(F\propto\frac{1}{r^2}\) ...(B)'
    scalar['paragraphs'][10] = scalar['paragraphs'][10].replace('). So', ') So')
    for index in (7,9,11):
        scalar['paragraphs'][index] = scalar['paragraphs'][index].replace(' … (', ' ...(')
    continuation = media['paragraphs'][0].replace('The force', 'The force', 1).replace('Fig 11.2. This', 'Fig 11.2 (o) This')
    # The first printed-page paragraph continues across the spread gutter.
    scalar['paragraphs'][12] = scalar['paragraphs'][12].replace('conventionally', 'conventionaly')+' '+continuation
    scalar['paragraphs'].append('combiningEq(A) & Eq(B)')
    scalar['sourceDefects'] = ["Printed reference Fig 11.2 (o) has no matching panel (o). Retained literally. Printed spelling conventionaly retained."]
    pairs = [(p, *pair) for p, pair in zip(scalar['paragraphs'][:13], TRANSLATIONS[scalar['id']])]
    pairs[3] = (scalar['paragraphs'][3], scalar['paragraphs'][3], scalar['paragraphs'][3])
    pairs[12] = (scalar['paragraphs'][12], pairs[12][1]+' '+TRANSLATIONS[media['id']][0][0], pairs[12][2]+' '+TRANSLATIONS[media['id']][0][1])
    pairs.append((scalar['paragraphs'][13], 'مساوات (A) اور مساوات (B) کو ملا کر', 'د (A) او (B) معادلو په یوځای کولو سره'))
    scalar_layout = [{'type': 'paragraph', 'indices':[0]}, {'type':'equation','indices':[1]},
                     {'type':'equation','indices':[2]}, {'type':'paragraph','indices':[13]},
                     {'type':'equation','indices':[3]}, {'type':'equation','indices':[4]},
                     {'type':'paragraph','indices':[5]}, {'type':'paragraph','indices':[6]},
                     {'type':'equation','indices':[7]}, {'type':'paragraph','indices':[8]},
                     {'type':'equation','indices':[9]}, {'type':'paragraph','indices':[10]},
                     {'type':'equation','indices':[11]}, {'type':'paragraph','indices':[12]}]
    revised_scalar = section(scalar, pairs, scalar_layout, TITLES[scalar['id']])
    revised_scalar['kind'] = 'lesson'
    media['paragraphs'] = media['paragraphs'][1:]
    media['paragraphs'][0] = media['paragraphs'][0].replace(r'\(\varepsilon_0\), i.e.,', r'\(\varepsilon_0\) i.e.,').rstrip('.')
    media['paragraphs'][1] = media['paragraphs'][1].rstrip('.')
    media['paragraphs'][2] = media['paragraphs'][2].replace('So ', 'so ', 1).rstrip('.')
    media['paragraphs'][5] = 'The coulomb’s force can now be written as'
    media_pairs = [(p, *pair) for p, pair in zip(media['paragraphs'], TRANSLATIONS[media['id']][1:])]
    revised_media = section(media, media_pairs,
                            [{'type':'equation' if i in (1,2,6,8) else 'heading' if i==3 else 'paragraph','indices':[i]} for i in range(9)], TITLES[media['id']])
    revised_media['kind'] = 'lesson'
    upsert([scalar, media], [revised_scalar, revised_media])
    formulas = [
      formula('phys12-slo-potential', 'V=W/q', 6, 'Potential', 'solve problems by using the expression V=W/q.'),
      formula('phys12-slo-field-gradient', 'E=V/d', 6, 'Electric field', 'solve problems by using the expression E = V/d.'),
      formula('phys12-slo-point-potential', r'V=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}', 6, 'Point-charge potential', 'calculate the potential in the field of a point charge using the equation V=1/4лE, q/r.'),
      formula('phys12-slo-capacitance', 'C=Q/V', 6, 'Capacitance', 'define capacitance and the farad and solve problems by using C=Q/V.'),
      formula('phys12-slo-energy', r'W=\frac12 QV=\frac12 CV^2', 6, 'Stored energy', 'demonstrate charging and discharging of a capacitor through a resistance. prove that energy stored in a capacitor is W=1/2 QV and hence W=1/2 Cv.'),
      formula('phys12-eq-coulomb', r'F=k\frac{q_1q_2}{r^2}', 7, 'Coulomb force', 'F = K9192'),
      formula('phys12-eq-11.2', r'\vec F_{21}=k\frac{q_1q_2}{r^2}\hat r_{12}', 7, 'Force on q₂', 'F21 = k 9192', '11.2'),
      formula('phys12-eq-11.3', r'\vec F_{12}=k\frac{q_1q_2}{r^2}\hat r_{21}', 7, 'Force on q₁', 'F12 = k9192721 Fiz', '11.3'),
      formula('phys12-eq-charge-quantization', 'q=ne', 6, 'Charge quantization'),
      formula('phys12-eq-11.1', r'F\propto\frac{q_1q_2}{r^2}', 7, 'Coulomb proportionality', number='11.1'),
      formula('phys12-eq-11.4', r'\vec F_{21}=-\vec F_{12}', 7, 'Equal and opposite forces', number='11.4'),
      formula('phys12-eq-k', r'k=\frac{1}{4\pi\varepsilon_0}=9.0\times10^9\;\mathrm{N\,m^2\,C^{-2}}', 7, 'Coulomb constant'),
      formula('phys12-eq-epsilon-zero', r'\varepsilon_0=8.85\times10^{-12}\;\mathrm{C^2\,N^{-1}\,m^{-2}}', 7, 'Free-space permittivity'),
      formula('phys12-eq-11.5', r'F_{\mathrm{med}}=\frac{1}{4\pi\varepsilon}\frac{q_1q_2}{r^2}', 7, 'Force in a medium', number='11.5'),
      formula('phys12-eq-11.6', r'\varepsilon_r=\frac{\varepsilon}{\varepsilon_0}', 7, 'Relative permittivity', number='11.6'),
    ]
    formulas[8]['sourceReferences'][0]['printedPage'] = 3
    sync_companions(formulas, [
      {'term':'Permittivity','def':'Permittivity is the property of a medium which affects the magnitude of force between two point charges.', 'sourceReferences':[{'pdfPage':7,'printedPage':5}]},
      {'term':'Relative permittivity','def':'For a particular insulator the permittivity of a material medium compared with the permittivity of vacuum is called relative permittivity or dielectric constant.', 'sourceReferences':[{'pdfPage':7,'printedPage':5}]},
    ])
    checkpoint(7, 'corrected_verified', [scalar['id'], media['id']],
               'Full spread at 3x plus 5x text crops compared with every equation, constant, unit and paragraph. Equations A/B and 11.1–11.6 retained with source numbering. Removed invented colon/periods, restored printed conventionaly and Fig 11.2 (o); source-reference defect disclosed. Joined the paragraph that crosses printed pages 4–5. Eight corrupt legacy formula cards corrected in place and additional source equations upserted by stable ID. Permittivity definition cards synchronized with printed text.', printed_pages=[4,5])
