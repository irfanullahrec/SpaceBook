# -*- coding: utf-8 -*-
import sys, json, io, datetime; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T
N = {181: 'SLOs page 1.', 182: 'SLOs page 2.', 183: 'Intro, Point to remember, 9.1, absorption of water and salts.',
 184: 'Root hair osmosis, Analysing box, cortex/endodermis/pericycle; Figure 9.1 coded.', 185: '9.2 transpiration, two boxes, Figure 9.2 coded.',
 186: '9.2.1 stomatal control, two boxes, Figure 9.3 coded, 9.2.2 light.', 187: 'Factors ii-vi, 9.2.3, STS box.',
 188: 'Necessary evil, evapotranspiration box, 9.3, Figure 9.4 coded.', 189: 'Water column tension, Analysing box, 9.4, Point to remember, steps i-ii, Figure 9.5 coded ("Germen" kept).',
 190: 'Steps iii-iv, Activities, 9.5, lymph box, 9.5.1.', 191: 'Plasma, Figure 9.6 coded (values checked at high zoom), plasma functions, two boxes.',
 192: 'RBCs, Figure 9.7 coded (duplicate caption noted), info box, WBCs and box.', 193: 'WBC types, info box, platelets, Figure 9.8 coded ("vessls" kept).',
 194: '9.5.2 leukaemia, thalassaemia + box, 9.5.3, ABO list.', 195: 'Antigens/antibodies, Table 9.1 (coded cell row + semantic table, "Anit-A" noted), 9.5.4, Point to remember.',
 196: 'Transfusion, Rh system ("Rh-ve donors" noted), antiserum box, Table 9.2, Analysing box.', 197: '9.6 heart structure, valves, circulation, info box.',
 198: 'Left side circulation, Figure 9.9 coded (faint caption read, "oxygentaed" kept), pulmonary/systemic circulation.', 199: 'Cardiac cycle, Figure 9.10 coded, pulse.',
 200: 'Analysing box, blood vessels, arteries, box, Figure 9.11 coded.', 201: 'Capillaries, veins ("vana cava" kept), box, general plan, arterial system.',
 202: 'Arterial branches, venous system ("Venus" kept), Figure 9.12 coded.', 203: 'Discovery: Ibn-al-Nafees, Harvey (portraits as labelled stand-ins), 9.7, atherosclerosis.',
 204: 'Arteriosclerosis, MI, silent MI box, prevention, STS box.', 205: 'Treatment (clipped "arte" noted), Figure 9.15 coded, World Heart Day box.',
 206: 'Key points page 1 (19).', 207: 'Key points page 2 (20).', 208: 'Exercise MCQs i-x.', 209: 'MCQs xi-xii, short and detailed questions with labelled SpaceBook answers.'}
T.record_pages([(p, 'corrected', n) for p, n in N.items()], next_page=210, current_chapter='Glossary')
cp = r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-9\checkpoint.json'
c = json.load(io.open(cp, encoding='utf-8'))
c.update(currentSubject='Biology', lastFullyVerifiedPdfPage=209, nextPdfPage=210, currentChapter='Glossary',
         lastUpdated=datetime.datetime.now().isoformat(timespec='seconds'),
         nextAction='Biology back matter PDF 210-225 (glossary/index): OCR+view, add glossary to BIO_DATA, record pages; then next subject Physics.')
json.dump(c, io.open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(T.load_progress()['counts'])
