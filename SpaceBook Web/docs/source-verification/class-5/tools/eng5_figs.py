"""Coded figures for Class 5 English pages: python eng5_figs.py calendar2018 | pie122 -> SVG on stdout."""
import sys, calendar, math
from html import escape


def calendar_svg(year=2018):
    cols, w, h = 6, 150, 132
    colors = ['#3b82f6', '#0891b2', '#16a34a', '#22c55e', '#84cc16', '#ea580c', '#dc2626', '#e11d48', '#be185d', '#7e22ce', '#6d28d9', '#1e3a8a']
    out = [f'<svg viewBox="0 0 {cols * w + 10} {2 * h + 10}" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">']
    cal = calendar.Calendar(firstweekday=6)  # Sunday first, as printed
    for m in range(1, 13):
        x = 5 + ((m - 1) % cols) * w
        y = 5 + ((m - 1) // cols) * h
        out.append(f'<rect x="{x + 3}" y="{y + 3}" width="{w - 8}" height="{h - 8}" rx="8" fill="#fff" stroke="#94a3b8"/>')
        out.append(f'<rect x="{x + 3}" y="{y + 3}" width="{w - 8}" height="34" rx="8" fill="{colors[m - 1]}"/>')
        out.append(f'<text x="{x + w / 2 - 1}" y="{y + 21}" text-anchor="middle" font-size="13" font-weight="bold" fill="#fff">{calendar.month_name[m].upper()}</text>')
        for i, d in enumerate(['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']):
            out.append(f'<text x="{x + 15 + i * 19}" y="{y + 33}" text-anchor="middle" font-size="8" fill="#fff">{d}</text>')
        for r, week in enumerate(cal.monthdayscalendar(year, m)):
            for i, d in enumerate(week):
                if d:
                    fill = '#dc2626' if i == 0 else '#111827'
                    out.append(f'<text x="{x + 15 + i * 19}" y="{y + 52 + r * 14}" text-anchor="middle" font-size="10" fill="{fill}">{d}</text>')
    out.append('</svg>')
    return '\n'.join(out)


def pie_svg():
    # (label, value or None for unnumbered, fill, plant?)
    slices = [('Fish', 145, '#cfe8d4'), ('Clams, snails', 109, '#d9eedc'), ('Birds', 92, '#cfe8d4'), ('Mammals', 84, '#d9eedc'),
              ('Reptiles', 36, '#cfe8d4'), ('Amphibians', 25, '#d9eedc'), ('Other animals', None, '#cfe8d4'),
              ('Other plants', None, '#2f6b2f'), ('Flowers', 760, '#3f7d3a')]
    est = {'Other animals': 115, 'Other plants': 20}   # unnumbered in print; sized from the picture
    vals = [v if v is not None else est[l] for l, v, _ in slices]
    total = sum(vals)
    cx, cy, r = 300, 190, 120
    out = ['<svg viewBox="0 0 640 380" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="13">',
           '<text x="300" y="28" text-anchor="middle" font-weight="bold" font-size="16">Endangered Species</text>']
    a = -math.pi / 2
    for (label, v, fill), val in zip(slices, vals):
        b = a + 2 * math.pi * val / total
        x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
        x2, y2 = cx + r * math.cos(b), cy + r * math.sin(b)
        large = 1 if b - a > math.pi else 0
        out.append(f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 1 {x2:.1f},{y2:.1f} z" fill="{fill}" stroke="#fff" stroke-width="2"/>')
        mid = (a + b) / 2
        lx, ly = cx + (r + 14) * math.cos(mid), cy + (r + 14) * math.sin(mid)
        tx = cx + (r + 70) * math.cos(mid)
        ty = cy + (r + 40) * math.sin(mid)
        anchor = 'start' if math.cos(mid) >= 0 else 'end'
        out.append(f'<line x1="{lx:.1f}" y1="{ly:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="#334155"/>')
        txt = escape(label) + (f' {v}' if v is not None else '')
        out.append(f'<text x="{tx + (4 if anchor == "start" else -4):.1f}" y="{ty + 4:.1f}" text-anchor="{anchor}">{txt}</text>')
        a = b
    out.append('<rect x="20" y="60" width="14" height="12" fill="#3f7d3a"/><text x="40" y="71">Plants</text>')
    out.append('<rect x="20" y="80" width="14" height="12" fill="#cfe8d4" stroke="#94a3b8"/><text x="40" y="91">Animals</text>')
    out.append('</svg>')
    return '\n'.join(out)


if __name__ == '__main__':
    print(calendar_svg() if sys.argv[1] == 'calendar2018' else pie_svg())
