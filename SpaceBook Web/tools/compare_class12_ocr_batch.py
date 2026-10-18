"""Compare recognized source words with Class 12 Physics records as a review aid."""
from pathlib import Path
import argparse
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'docs/source-verification/class-12'
EXTRACT = ROOT / 'tmp/class12-review'
STOP = {'about','after','again','also','among','and','are','because','been','being','both','can','called',
        'does','each','for','from','have','into','its','may','more','most','not','only','other','over',
        'such','than','that','the','their','then','there','these','they','this','those','through','upon',
        'very','was','were','which','while','with','within','would'}


def words(value):
    value = html.unescape(value or '')
    value = re.sub(r'<[^>]*>', ' ', value)
    value = re.sub(r'\\[A-Za-z]+', ' ', value)
    return {word for word in re.findall(r'[A-Za-z]{4,}', value.lower()) if word not in STOP}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--end', type=int, required=True)
    args = parser.parse_args()
    extract_path = EXTRACT / f'extract-{args.start:03}-{args.end:03}.txt'
    ocr_text = extract_path.read_text(encoding='utf-8', errors='replace')
    page_text = {}
    for part in ocr_text.split('===== PDF PAGE '):
        match = re.match(r'(\d+) \([^)]*\) =====\n(.*)', part, re.S)
        if match:
            page_text[int(match.group(1))] = match.group(2)
    records = json.loads((AUDIT / 'physics-corrections-unit12.json').read_text(encoding='utf-8'))
    sections = json.loads((AUDIT / 'physics-sections-unit12.json').read_text(encoding='utf-8'))
    results = []
    for number in range(args.start, args.end + 1):
        coded = ' '.join(' '.join(record.get('paragraphs', [])) for record in records
                         if record.get('pdfPage') == number)
        coded += ' ' + ' '.join(section.get('diagramSvg', '') for section in sections
                                 if any(ref.get('pdfPage') == number for ref in section.get('sourceReferences', [])))
        recognized = words(page_text.get(number, ''))
        implemented = words(coded)
        overlap = recognized & implemented
        results.append({
            'pdfPage': number,
            'recognizedDistinctWords': len(recognized),
            'codedDistinctWords': len(implemented),
            'codedWordOverlapPercent': round(100 * len(overlap) / max(1, len(implemented)), 1),
            'codedWordsNotRecognized': sorted(implemented - recognized),
            'ocrWordsNotInCodedText': sorted(recognized - implemented),
            'interpretation': 'OCR comparison aid only; OCR omissions and column-order errors require visual judgment.'
        })
    out = EXTRACT / f'comparison-{args.start:03}-{args.end:03}.json'
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps([{'pdfPage': item['pdfPage'], 'overlapPercent': item['codedWordOverlapPercent'],
                       'codedWordsNotRecognized': item['codedWordsNotRecognized'][:12],
                       'ocrWordsNotInCodedText': item['ocrWordsNotInCodedText'][:12]} for item in results],
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
