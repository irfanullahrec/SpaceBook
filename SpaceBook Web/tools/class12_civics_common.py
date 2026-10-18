"""Shared Class 12 Civics (شہریت, KPTBB) helpers: Urdu-original book; records carry (en, ur, ps) with Urdu as the source text."""
from class12_book_common import Book, Builder  # noqa: F401

BOOK = Book('civics')

UNITS = {
    1: ('The System of Government of Pakistan', 'پاکستان کا نظامِ حکومت', 'د پاکستان د حکومت نظام'),
    2: ('Rights of Children and Women', 'بچوں اور خواتین کے حقوق', 'د ماشومانو او ښځو حقونه'),
    3: ('Political Economy', 'سیاسی اقتصادیات', 'سیاسي اقتصاد'),
    4: ('International Conflicts and their Resolution', 'بین الاقوامی تنازعات اور حل', 'نړیوالې شخړې او د هغو حل'),
    5: ('Intellectual Skills', 'علمی مہارتیں', 'علمي مهارتونه'),
    6: ('Political Parties and Social Movements', 'سیاسی جماعتیں اور سماجی تحاریک', 'سیاسي ګوندونه او ټولنیز خوځښتونه'),
    7: ('Peace and Diversity', 'امن اور تنوع', 'سوله او تنوع'),
    8: ('Active and Responsible Citizenship', 'فعال اور ذمہ دار شہریت', 'فعاله او مسؤله تابعیت'),
}


def rec(b, unit, n, pdf, pages, note=None, first=False):
    r = BOOK.record(b, f'civ12-ch{unit}-text-{n}', f'Chapter {unit} text ({n})', f'باب {unit} — متن ({n})', f'{unit} څپرکی — متن ({n})', pdf, pages,
                    unit_title=UNITS[unit] if first else None)
    if note:
        r['sourceNote'] = note
    return r


def P(b, items):
    for x in items:
        b.p(*x)


def org_tree(root, kids, cap):
    """Simple hierarchy: root box with arrows down to child boxes (RTL order for Urdu handled by caller)."""
    n = len(kids)
    W, H = 160 * n + 40, 170
    t = lambda x, y, s, sz=15, w='normal': f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{sz}" font-weight="{w}" fill="#1e293b" font-family="sans-serif">{s}</text>'
    b = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{cap}"><defs><marker id="ca" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1e293b"/></marker></defs>',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>', f'<rect x="{W / 2 - 70}" y="8" width="140" height="34" rx="6" fill="#eef6ff" stroke="#1e3a8a" stroke-width="1.5"/>', t(W / 2, 31, root, 16, 'bold'),
         f'<line x1="{W / 2}" y1="42" x2="{W / 2}" y2="62" stroke="#1e293b" stroke-width="2"/>']
    xs = [40 + 160 * i + 80 for i in range(n)]
    b.append(f'<line x1="{xs[0]}" y1="62" x2="{xs[-1]}" y2="62" stroke="#1e293b" stroke-width="2"/>')
    for x, k in zip(xs, kids):
        b.append(f'<line x1="{x}" y1="62" x2="{x}" y2="96" stroke="#1e293b" stroke-width="2" marker-end="url(#ca)"/>')
        b.append(f'<rect x="{x - 72}" y="98" width="144" height="34" rx="6" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.5"/>' + t(x, 121, k))
    b.append(t(W / 2, H - 10, cap, 12) + '</svg>')
    return ''.join(b), W / H


def hier(nodes, edges, cap, W=560, H=360):
    """General hierarchy chart. nodes: {key: (x, y, label, sub)}; edges: [(parent, child)] drawn as elbow connectors."""
    t = lambda x, y, s, sz=14, w='normal': f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{sz}" font-weight="{w}" fill="#1e293b" font-family="sans-serif">{s}</text>'
    b = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{cap}"><rect width="{W}" height="{H}" fill="#ffffff"/>']
    for p, c in edges:
        px, py = nodes[p][0], nodes[p][1]
        cx, cy = nodes[c][0], nodes[c][1]
        mid = (py + 14 + cy - 18) / 2
        b.append(f'<polyline points="{px},{py + 14} {px},{mid} {cx},{mid} {cx},{cy - 18}" fill="none" stroke="#1e293b" stroke-width="1.6"/>')
    for x, y, lab, sub in nodes.values():
        w = max(110, 9 * len(lab) + 24)
        b.append(f'<rect x="{x - w / 2}" y="{y - 18}" width="{w}" height="{32 if not sub else 46}" rx="6" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.3"/>')
        b.append(t(x, y + 3, lab, 14, 'bold'))
        if sub:
            b.append(t(x, y + 20, sub, 11))
    b.append(t(W / 2, H - 8, cap, 12) + '</svg>')
    return ''.join(b), W / H
