"""Computer Science XII PDF149–156: Glossary (pp.286–300) built from class12_cs_glossary*.G (PDF156 also carries the Index start, see class12_cs_page156.py).
Run: python class12_cs_page149.py N (149–155)."""
import sys
from class12_cs_common import BOOK, Builder
from class12_cs_glossary import G
from class12_cs_glossary2 import G2
from class12_cs_glossary3 import G3
G.update(G2)
G.update(G3)

PAGES = {149: [286, 287], 150: [288, 289], 151: [290, 291], 152: [292, 293], 153: [294, 295], 154: [296, 297], 155: [298, 299], 156: [300]}
ISSUES = {
    149: 'Glossary: “Analyst is a profession al”, “function declator”. Retained as printed.',
    150: 'Glossary: “Constructor” is defined twice (pp.288 and 289); “get values form the users”, “more than one constructors”. Retained as printed.',
    151: 'Glossary: “an operating that is used”, “builds ocuments configures the hardware software”, “Distributed operating” (heading lacks “system”). Retained as printed.',
    152: 'Glossary: “-existing classes”, “These are special function”, the logical operators listed as (!, &&, !!) and “A float type of data” for long double. Retained as printed. The start of the Integer type definition is obscured on p.293 and is read as “It is a group of data type”.',
    153: 'Glossary: “One dimentional array”, “more than one immediate base classes”, “multiple tasks simultaneous”. Retained as printed. The Non parameterized constructor definition is partly obscured on p.295 and is completed from its legible ending.',
    154: 'Glossary: “Parameter” is defined twice; “in which it may be is called process state”; the relational-operator list “(==,=, >, >=, <, <=” is unbalanced. Retained as printed.',
    155: 'Glossary: “System support” is defined as “maintenance”; the ternary operator is printed “? :)”; “A sequence of character is called string”. Retained as printed.',
    156: 'Glossary: “Two dimensional array” is defined as “multidimensional array”; “the process either waiting”. Retained as printed.',
}


def build(n):
    b = Builder()
    if n == 149:
        b.h('Glossary', 'فرہنگ', 'وییپانګه')
    items = []

    def flush():
        if items:
            b.group('lines', items[:])
            items.clear()
    for e in G[n]:
        if isinstance(e, str):
            flush()
            b.h(e, e, e)
            continue
        term, en, ur, ps = e
        items.append((f'{term}: {en}', f'{term}: {ur}', f'{term}: {ps}'))
    flush()
    k = n - 148
    r = BOOK.record(b, f'cs12-bm-glossary-{k}', f'Glossary ({k})', f'فرہنگ ({k})', f'وییپانګه ({k})', n, PAGES[n])
    r['sourceNote'] = 'Glossary terms are kept in English (as C++/computing terms) at the head of each entry; the definitions are translated. Alphabet divider badges are reproduced as letter headings.'
    issues = [{'id': f'cs12-pdf{n:03d}', 'unit': 'BM', 'printedPage': PAGES[n][0], 'description': ISSUES[n]}] if n in ISSUES else []
    return r, issues


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 149
    r, iss = build(n)
    BOOK.save(n, [('BM', r)], issues=iss)
