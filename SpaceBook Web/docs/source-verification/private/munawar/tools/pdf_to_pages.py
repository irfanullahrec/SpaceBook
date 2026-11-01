"""Turn a publisher-supplied PDF into vector pages for the SpaceBook page reader.

    python -P pdf_to_pages.py <book.pdf> <out_dir> [--report-only]

For every page it writes
    <out_dir>/pNNN.svg     the page as vector (text kept as text, drawings as paths, pictures embedded)
    <out_dir>/pNNN.json    {"w","h" in points, "words": [[x0,y0,x1,y1,"word",block,line,n], ...]}  (the text layer)
and <out_dir>/pages.json   {"pages": N, "w", "h", "report": {...}}.

--report-only prints the check below and writes nothing: it says whether a PDF is "clean" (live text, vector drawings, pictures
at print resolution) or "flat" (every page one picture, as the 437 x 547 sample PDFs are), because only a clean PDF gives
exact pages with vector artwork and a text layer.

The tool never changes what is on a page: no recolouring, no re-typing, no re-drawing. The credit line and the SpaceBook tools are
added by the reader around the page, not inside it.
"""
import json, os, sys
import pymupdf


def page_report(page):
    imgs = page.get_images(full=True)
    big = 0
    for im in imgs:
        # the placed size of the picture on the page, in points, against its pixel size
        for r in page.get_image_rects(im[0]):
            if r.width > 0 and im[2] / (r.width / 72.0) >= 150:   # >= 150 dpi
                big += 1
                break
    return {
        'images': len(imgs), 'images_150dpi': big,
        'drawings': len(page.get_drawings()),
        'text_chars': len(page.get_text().strip()),
        'full_page_picture': any(r.width >= page.rect.width * 0.95 and r.height >= page.rect.height * 0.95
                                 for im in imgs for r in page.get_image_rects(im[0])),
    }


def classify(reports):
    n = max(1, len(reports))
    text = sum(1 for r in reports if r['text_chars'] > 20) / n
    vec = sum(1 for r in reports if r['drawings'] > 0) / n
    flat = sum(1 for r in reports if r['full_page_picture'] and r['text_chars'] == 0 and r['drawings'] == 0) / n
    kind = 'flat' if flat > 0.8 else ('clean' if (text > 0.5 or vec > 0.5) else 'mixed')
    return {'kind': kind, 'pages_with_text': round(text, 2), 'pages_with_vector': round(vec, 2), 'pages_flat': round(flat, 2)}


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    src = argv[0]
    out = argv[1] if len(argv) > 1 and not argv[1].startswith('--') else None
    report_only = '--report-only' in argv
    doc = pymupdf.open(src)
    reports = [page_report(p) for p in doc]
    summary = classify(reports)
    summary['pages'] = len(doc)
    print(os.path.basename(src), json.dumps(summary))
    if report_only or not out:
        return 0
    os.makedirs(out, exist_ok=True)
    for i, page in enumerate(doc):
        name = 'p%03d' % i
        svg = page.get_svg_image(matrix=pymupdf.Identity, text_as_path=False)
        with open(os.path.join(out, name + '.svg'), 'w', encoding='utf-8') as f:
            f.write(svg)
        words = [[round(w[0], 2), round(w[1], 2), round(w[2], 2), round(w[3], 2), w[4], w[5], w[6], w[7]] for w in page.get_text('words')]
        with open(os.path.join(out, name + '.json'), 'w', encoding='utf-8') as f:
            json.dump({'w': round(page.rect.width, 2), 'h': round(page.rect.height, 2), 'words': words}, f, ensure_ascii=False)
    first = doc[0].rect
    with open(os.path.join(out, 'pages.json'), 'w', encoding='utf-8') as f:
        json.dump({'pages': len(doc), 'w': round(first.width, 2), 'h': round(first.height, 2), 'report': summary}, f)
    print('wrote', len(doc), 'pages to', out)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
