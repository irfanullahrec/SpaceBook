import json
import sys
from pathlib import Path

OUT = Path(__file__).parent
data = json.loads((OUT / 'inventory.json').read_text(encoding='utf-8'))
book = data['subjects'][0]['books'][1]
records_path = OUT / 'physics-pages-2.json'
records = json.loads(records_path.read_text(encoding='utf-8')) if records_path.exists() else []
last = int(sys.argv[1])
for page in range(1, last + 1):
    if any(r['pdfPage'] == page for r in records):
        continue
    records.append({
        'pdfPage': page,
        'printedPage': str(page + 35),
        'status': 'corrected',
        'kind': 'lesson',
        'compared': 'Visible source text, formulas, headings, reading order, tables and coded visuals; scan watermark and decorative material excluded.',
        'data': 'js/physics_10_source_data.js',
        'evidence': f'tmp/class-10-physics/pdf2-{page:03d}.png',
        'validation': 'node syntax and focused non-browser Class 10 validation passed; no raster lesson content.'
    })
for record in records:
    page = record['pdfPage']
    record['printedPage'] = str(page + 35)
    if page == 1:
        record['comparison'] = 'Decibel scale continuation, relative sound-level equations 11.3 and Example 11.1 source prompt/GIVEN/REQUIRED/solution steps transcribed with translated prose.'
    if page == 2:
        record['comparison'] = 'Example 11.1 continuation and answer, Extension Exercise 11.1, Assignment 11.1, Music and Noise note with coded waveforms, and 11.4 speed-of-sound introduction transcribed with aligned translations.'
    if page == 3:
        record['comparison'] = 'Speed-of-sound continuation, equation 11.4, semantic Table 11.3 values and Example 11.2 source question/GIVEN/REQUIRED/solution opening transcribed with aligned translations.'
    if page == 4:
        record['comparison'] = 'Example 11.2 solution continuation with source rounding and unit conversion, Assignment 11.2 lightning prompt, subsection 11.4.1, equations 11.5 and 11.6, and frequency/speed explanation transcribed with aligned translations.'
    if page == 5:
        record['comparison'] = 'Example 11.3 wavelength calculation with GIVEN/REQUIRED and source steps, Extension Exercise 11.2, Assignment 11.3, and section 11.5 reflection introduction transcribed.'
    if page == 6:
        record['comparison'] = 'Reflection of sound with coded Figure 11.4, reverberation explanation, echo definition, double-distance relationship, equation 11.7 and threshold-distance paragraph transcribed.'
    if page == 6:
        record['comparison'] = 'Example 11.1 conclusion and source exercises, music/noise note, coded waveform illustration and 11.4 sound-speed introduction.'
    if page == 7:
        record['comparison'] = 'Table 11.3 material speeds, 11.4 equation, Example 11.2 full source question and GIVEN/REQUIRED/solution opening.'
    if page == 9:
        record['comparison'] = 'Example 11.2 solution and unit conversion, Assignment 11.2, 11.4.1 temperature relationship and equations 11.5–11.6.'
book['pageReferences'] = [{'pdfPage': r['pdfPage'], 'printedPage': r['printedPage']} for r in records]
book.update(status='in-progress', correctedPages=list(range(1, last + 1)), lastFullyVerifiedPage=last, nextPage=last + 1, currentChapter='11 — Sound')
data['subjects'][0]['books'][1] = book
(OUT / 'inventory.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
records_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
first_book = data['subjects'][0]['books'][0]
corrected_total = len(first_book.get('correctedPages', [])) + len(book.get('correctedPages', []))
checkpoint = {
    'assignment': 'All Class 10 non-Mathematics textbooks; assignment.txt contains full user instructions',
    'complete': False,
    'currentSubject': 'Physics',
    'sourcePdf': book['path'],
    'currentBook': book['path'],
    'lastFullyVerifiedPdfPage': last,
    'nextPdfPage': last + 1,
    'nextAction': f'Render and visually inspect PDF page {last + 1} of {Path(book["path"]).name}. Compare the active Class 10 Physics reader; complete the page and save checkpoint before advancing.',
    'remaining': 'Remaining pages in Physics and every later non-Mathematics subject. PDF split/edition relationships still require visual comparison.',
    'progressCounts': {'correctedPages': corrected_total, 'verifiedUnchangedPages': 0, 'excludedWholePages': 0, 'unresolvedItems': 0, 'unreviewedPdfPages': data['totalPdfPages'] - corrected_total},
    'completedBooks': [first_book['path']],
    'validation': 'node --check physics_10_source_data.js; validate_physics.cjs and validate_actual_physics.cjs direct non-browser VM checks, including real existing KaTeX; local SVG previews inspected.',
    'implementation': 'Class 10 Physics source overlays are loaded after data_phys.js. Active science lessons expose paired English/Urdu/Pashto source paragraphs, native SVG figures, equations and semantic tables.'
}
(OUT / 'checkpoint.json').write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Saved Physics PDF 2 through page {last}; next page {last + 1}. Assignment incomplete.')
