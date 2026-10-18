"""Generate a simple linear (top-to-bottom) flowchart SVG for page files.

    python -X utf8 tools/flowsvg.py "S:START" "IO:INPUT B, H" "P:A=(B*H)/2" "IO:OUTPUT A" "S:STOP"

Kinds: S = start/stop oval, IO = input/output parallelogram, P = process rectangle (use '|' for extra lines).
Prints the <svg> block (no caption line, no endsvg) to paste between `svg caption` and `endsvg`.
"""
import sys, html

ROW = 56


def main(steps):
    w = 320
    parts, y = [], 12
    centres = []
    for kind, _, text in (s.partition(':') for s in steps):
        lines = text.split('|')
        h = 36 if len(lines) == 1 else 22 * len(lines) + 12
        cx = w / 2
        if kind == 'S':
            parts.append(f'<ellipse cx="{cx}" cy="{y + h / 2}" rx="56" ry="{h / 2}" fill="#fff" stroke="#111827"/>')
        elif kind == 'IO':
            parts.append(f'<polygon points="{cx - 130},{y + h} {cx - 100},{y} {cx + 130},{y} {cx + 100},{y + h}" fill="#e0f2fe" stroke="#111827"/>')
        else:
            parts.append(f'<rect x="{cx - 100}" y="{y}" width="200" height="{h}" fill="#fff" stroke="#111827"/>')
        for i, ln in enumerate(lines):
            ty = y + h / 2 + 5 + (i - (len(lines) - 1) / 2) * 20
            parts.append(f'<text x="{cx}" y="{ty}">{html.escape(ln)}</text>')
        centres.append((y, y + h))
        y += h + 26
    arrows = [f'<line x1="{w / 2}" y1="{a[1]}" x2="{w / 2}" y2="{b[0] - 2}"/>' for a, b in zip(centres, centres[1:])]
    label = '; '.join(s.partition(':')[2].replace('|', ', ') for s in steps)
    out = [f'<svg viewBox="0 0 {w} {y - 14}" width="{w}" role="img" aria-label="Flowchart: {html.escape(label)}" '
           'font-family="Times New Roman, serif" font-size="14" text-anchor="middle" stroke-width="1.5">',
           '<defs><marker id="arFS" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#111827"/></marker></defs>',
           '<g stroke="#111827" marker-end="url(#arFS)">' + ''.join(arrows) + '</g>'] + parts + ['</svg>']
    print('\n'.join(out))


if __name__ == '__main__':
    main(sys.argv[1:])
