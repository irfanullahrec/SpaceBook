# -*- coding: utf-8 -*-
import sys, json, io, datetime; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T
N = {
 150: 'SLOs page 1 inspected; transcribed with Urdu/Pashto pairs.',
 151: 'SLOs page 2; printed typo "absorportion" kept.',
 152: 'Intro + 8.1 text + Point to remember verified against image.',
 153: 'Table 8.1 coded as a semantic table (17 nutrient rows, trilingual).',
 154: '8.1.1, 8.1.2, chlorosis box; Figure 8.1 coded as SVG porphyrin rings (Fe/Mg).',
 155: '8.2, 8.2.1, 8.2.2; image confirms only two 8.2.2 bullets.',
 156: '8.2.3 hazards (book "NO⁻³" noted as NO₃⁻), eutrophication box, start of 8.3 carbohydrates.',
 157: 'Proteins, fats, info boxes.',
 158: 'Fat sources, Figure 8.2 (labelled stand-in grid, printed "Carbohydratees" kept), vitamins, vitamin A, Figure 8.3.',
 159: 'Vitamin C ("scury" kept with source note), vitamin D, Figure 8.4.',
 160: 'Minerals, calcium, iron, callouts.',
 161: 'Analysing box, Activities 8.1, dietary fibre, water a, Point to Ponder.',
 162: 'Water b-g; Table 8.2 coded (bread fat 52% printing error noted, kept as printed).',
 163: 'Energy-requirement sub-headings (faded heading words restored, noted); Table 8.3 coded.',
 164: 'Table 8.4 coded (13 rows verified at high zoom); 8.5 intro.',
 165: 'PEM, marasmus, kwashiorkor; Figures 8.5/8.6 photographs as labelled stand-ins; Activity 8.2.',
 166: 'Anaemia (left margin clipped, restored and noted), osteoporosis, goiter, OIN, causes; Figure 8.7 coded ("Thyorlod" kept with note).',
 167: 'Famine, Analysing box, 8.6 introduction.',
 168: 'Figure 8.8 digestive system coded SVG with all 21 labels; alimentary canal parts.',
 169: 'Oral cavity, Figure 8.9 coded, salivary glands, info box.',
 170: 'Pharynx, swallowing, oesophagus, peristalsis; Figure 8.10 coded; three info boxes.',
 171: 'Stomach text and Figure 8.11 coded with gastric gland inset.',
 172: 'Stomach continued, two info boxes, small intestine, duodenum, liver ("gall bladdar" kept).',
 173: 'Pancreas, Figure 8.12 coded, jejunum, ileum, absorption.',
 174: 'Villus text, Figure 8.13 coded, large intestine, caecum, appendix box.',
 175: 'Figure 8.14 coded, colon, rectum, bacteria box, liver roles intro.',
 176: 'Liver roles i-viii, Analysing box, 8.7 constipation and laxative box.',
 177: 'Diarrhoea, ulcers, Figure 8.15 coded; faded letters in last line noted.',
 178: 'Key points (22) transcribed.',
 179: 'Exercise MCQs i-vii; SpaceBook answers labelled.',
 180: 'MCQs viii-x, short and detailed questions with labelled SpaceBook answers.',
}
T.record_pages([(p, 'corrected', n) for p, n in N.items()], next_page=181, current_chapter='Unit 9: Transport')
cp = r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-9\checkpoint.json'
c = json.load(io.open(cp, encoding='utf-8'))
c.update(currentSubject='Biology', lastFullyVerifiedPdfPage=180, nextPdfPage=181, currentChapter='Unit 9: Transport',
         lastUpdated=datetime.datetime.now().isoformat(timespec='seconds'),
         nextAction='Biology Unit 9 Transport: OCR+view PDF 181 onward, write unit9 modules, build_unit9.py, render_check 9, record pages.')
json.dump(c, io.open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(T.load_progress()['counts'])
