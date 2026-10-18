"""Class 1 figure generators (counting pictures, place-value bundles, number cards, money, shapes).

Every generator returns a self-contained inline <svg>. Counting pictures draw EXACTLY the number of objects
asked for, so quantities in the textbook pictures are preserved.

  cnt SPEC            tokens separated by spaces:
                        NAME:N         N objects (NAME may carry a colour: triangle.red:3)
                        NAME:NxK       N objects, the last K crossed out (taking away)
                        NAME:N/W       N objects wrapped W per row inside the group
                        + - = > < ? ×  operator / symbol between groups
                        "TEXT"         short text (use _ for spaces), e.g. "5" or "equals"
                        []             empty answer box     [7] box holding 7
                        |              start a new row
                      options (anywhere): frame (ring each group), s=0.8 (scale)
  tens T O [sticks]   T tens rods (or bundles of 10 sticks) and O ones cubes (or single sticks)
  cards 3,1,_,2       number cards in a row ('_' = blank card to fill)
  train 3,_,5         number cards as coaches behind an engine
  tframe N [colour]   ten frame with N counters
  hand N              a hand showing N fingers (0-5)
  shapes SPEC         same as cnt, shapes only, bigger cells
"""
from html import escape

C = {'red': '#ef4444', 'blue': '#3b82f6', 'green': '#22c55e', 'yellow': '#facc15', 'orange': '#f97316',
     'purple': '#a855f7', 'pink': '#ec4899', 'brown': '#92400e', 'black': '#1f2937', 'grey': '#9ca3af',
     'white': '#ffffff', 'sky': '#38bdf8', 'navy': '#1e3a8a', 'dkgreen': '#15803d', 'gold': '#eab308'}
K = '#334155'   # outline


def _col(c, default):
    return C.get(c, c) if c else default


def _icon(name, col=None):
    """SVG for one object centred on (0,0), about 36x36."""
    f = lambda d: _col(col, d)
    s = {
        'apple': f'<circle cx="-5" cy="3" r="12" fill="{f("#dc2626")}" stroke="{K}"/><circle cx="5" cy="3" r="12" fill="{f("#dc2626")}" stroke="{K}"/><path d="M0 -8 q1 -7 5 -9" stroke="#78350f" stroke-width="2" fill="none"/><path d="M2 -12 q6 -6 11 -2 q-6 4 -11 2z" fill="#16a34a"/>',
        'mango': f'<path d="M-12 4 C-14 -10 4 -16 12 -6 C18 4 8 16 -4 14 C-9 13 -11 9 -12 4z" fill="{f("#f59e0b")}" stroke="{K}"/><path d="M8 -8 q4 -6 8 -5" stroke="#15803d" stroke-width="2" fill="none"/>',
        'banana': f'<path d="M-15 -8 C-12 10 8 16 16 2 C10 8 -6 6 -10 -9z" fill="{f("#facc15")}" stroke="{K}"/><path d="M-15 -8 l-2 -3" stroke="#78350f" stroke-width="3"/>',
        'orange': f'<circle r="14" fill="{f("#f97316")}" stroke="{K}"/><circle cx="-3" cy="-11" r="2" fill="#15803d"/>',
        'strawberry': f'<path d="M0 15 C-14 6 -15 -6 -10 -9 C-5 -12 5 -12 10 -9 C15 -6 14 6 0 15z" fill="{f("#e11d48")}" stroke="{K}"/><path d="M-9 -10 l4 -5 l5 3 l5 -3 l4 5z" fill="#16a34a"/><g fill="#fde68a"><circle cx="-4" cy="-2" r="1"/><circle cx="4" cy="-1" r="1"/><circle cx="0" cy="5" r="1"/></g>',
        'grapes': f'<g fill="{f("#7c3aed")}" stroke="{K}"><circle cx="-6" cy="-6" r="5"/><circle cx="4" cy="-6" r="5"/><circle cx="-1" cy="2" r="5"/><circle cx="9" cy="2" r="5"/><circle cx="-10" cy="2" r="5"/><circle cx="-5" cy="10" r="5"/><circle cx="5" cy="10" r="5"/></g><path d="M0 -11 v-6" stroke="#78350f" stroke-width="2"/>',
        'cherry': f'<circle cx="-7" cy="8" r="7" fill="{f("#b91c1c")}" stroke="{K}"/><circle cx="8" cy="8" r="7" fill="{f("#b91c1c")}" stroke="{K}"/><path d="M-7 1 Q0 -14 4 -16 M8 1 Q6 -10 4 -16" stroke="#15803d" stroke-width="2" fill="none"/>',
        'pear': f'<path d="M0 -14 C6 -14 6 -4 9 2 C14 10 8 16 0 16 C-8 16 -14 10 -9 2 C-6 -4 -6 -14 0 -14z" fill="{f("#a3e635")}" stroke="{K}"/><path d="M0 -14 v-4" stroke="#78350f" stroke-width="2"/>',
        'watermelon': f'<path d="M-16 -4 A16 16 0 0 0 16 -4z" fill="#16a34a"/><path d="M-13 -4 A13 13 0 0 0 13 -4z" fill="{f("#ef4444")}"/><g fill="#111"><circle cx="-5" cy="2" r="1.3"/><circle cx="4" cy="3" r="1.3"/><circle cx="0" cy="-1" r="1.3"/></g>',
        'pineapple': f'<ellipse cy="5" rx="10" ry="12" fill="{f("#f59e0b")}" stroke="{K}"/><path d="M-6 0 l12 10 M6 0 l-12 10" stroke="#92400e"/><path d="M0 -7 l-6 -10 l4 3 l2 -6 l2 6 l4 -3z" fill="#16a34a"/>',
        'carrot': f'<path d="M-4 -8 L4 -8 L0 16z" fill="{f("#f97316")}" stroke="{K}"/><path d="M0 -8 l-5 -8 M0 -8 l0 -9 M0 -8 l5 -8" stroke="#16a34a" stroke-width="2"/>',
        'tomato': f'<circle cy="2" r="13" fill="{f("#ef4444")}" stroke="{K}"/><path d="M-6 -10 l6 3 l6 -3 l-3 5 l-6 0z" fill="#16a34a"/>',
        'egg': f'<ellipse rx="10" ry="14" fill="{f("#fef3c7")}" stroke="{K}"/>',
        'candy': f'<ellipse rx="9" ry="7" fill="{f("#ec4899")}" stroke="{K}"/><path d="M-9 0 l-8 -6 v12z M9 0 l8 -6 v12z" fill="{f("#ec4899")}" stroke="{K}"/>',
        'lollipop': f'<circle cy="-6" r="10" fill="{f("#ec4899")}" stroke="{K}"/><path d="M-6 -6 a6 6 0 0 1 12 0" stroke="#fff" fill="none"/><path d="M0 4 v14" stroke="#78350f" stroke-width="2"/>',
        'candle': f'<rect x="-5" y="-8" width="10" height="24" fill="{f("#f472b6")}" stroke="{K}"/><path d="M0 -10 q-5 -5 0 -10 q5 5 0 10z" fill="#f59e0b"/>',
        'cake': f'<rect x="-14" y="-4" width="28" height="18" fill="{f("#f9a8d4")}" stroke="{K}"/><path d="M-14 -4 q7 6 14 0 q7 6 14 0" fill="#fff" stroke="{K}"/><circle cy="-8" r="3" fill="#dc2626"/>',
        'cupcake': f'<path d="M-10 2 L-7 16 L7 16 L10 2z" fill="#f59e0b" stroke="{K}"/><path d="M-12 2 q0 -14 12 -14 q12 0 12 14z" fill="{f("#f9a8d4")}" stroke="{K}"/><circle cy="-13" r="3" fill="#dc2626"/>',
        'icecream': f'<path d="M-8 0 L0 18 L8 0z" fill="#d97706" stroke="{K}"/><circle cy="-5" r="9" fill="{f("#fbcfe8")}" stroke="{K}"/>',
        'donut': f'<circle r="14" fill="{f("#d97706")}" stroke="{K}"/><circle r="12" fill="{f("#f472b6")}"/><circle r="5" fill="#fff" stroke="{K}"/>',
        'biscuit': f'<circle r="13" fill="{f("#d6a35c")}" stroke="{K}"/><g fill="#78350f"><circle cx="-5" cy="-4" r="1.6"/><circle cx="5" cy="-2" r="1.6"/><circle cx="-1" cy="5" r="1.6"/><circle cx="6" cy="6" r="1.6"/></g>',
        'pencil': f'<g transform="rotate(-45)"><rect x="-4" y="-16" width="8" height="26" fill="{f("#facc15")}" stroke="{K}"/><path d="M-4 10 L0 19 L4 10z" fill="#fde68a" stroke="{K}"/><rect x="-4" y="-20" width="8" height="4" fill="#f472b6" stroke="{K}"/></g>',
        'crayon': f'<g transform="rotate(-45)"><rect x="-5" y="-14" width="10" height="24" fill="{f("#3b82f6")}" stroke="{K}"/><path d="M-5 -14 L0 -22 L5 -14z" fill="{f("#3b82f6")}" stroke="{K}"/></g>',
        'book': f'<rect x="-12" y="-15" width="24" height="30" rx="2" fill="{f("#2563eb")}" stroke="{K}"/><line x1="-8" y1="-15" x2="-8" y2="15" stroke="{K}"/>',
        'bag': f'<rect x="-13" y="-8" width="26" height="22" rx="4" fill="{f("#dc2626")}" stroke="{K}"/><path d="M-6 -8 v-6 h12 v6" stroke="{K}" fill="none" stroke-width="2"/>',
        'ball': f'<circle r="13" fill="{f("#f97316")}" stroke="{K}"/><path d="M-13 0 H13 M0 -13 V13" stroke="{K}" fill="none"/>',
        'football': f'<circle r="13" fill="#fff" stroke="{K}"/><path d="M0 -5 l5 3 l-2 6 h-6 l-2 -6z" fill="#111"/>',
        'balloon': f'<ellipse cy="-4" rx="10" ry="13" fill="{f("#ef4444")}" stroke="{K}"/><path d="M0 9 q-3 5 0 9" stroke="{K}" fill="none"/>',
        'kite': f'<path d="M0 -16 L11 0 L0 16 L-11 0z" fill="{f("#f59e0b")}" stroke="{K}"/><path d="M0 -16 V16 M-11 0 H11" stroke="{K}"/>',
        'car': f'<path d="M-17 4 v-6 l6 -1 l5 -7 h12 l5 7 l6 1 v6z" fill="{f("#3b82f6")}" stroke="{K}"/><circle cx="-9" cy="6" r="4" fill="#111"/><circle cx="9" cy="6" r="4" fill="#111"/>',
        'bus': f'<rect x="-18" y="-11" width="36" height="18" rx="3" fill="{f("#facc15")}" stroke="{K}"/><g fill="#bae6fd"><rect x="-15" y="-8" width="7" height="6"/><rect x="-6" y="-8" width="7" height="6"/><rect x="3" y="-8" width="7" height="6"/></g><circle cx="-10" cy="8" r="4" fill="#111"/><circle cx="10" cy="8" r="4" fill="#111"/>',
        'truck': f'<rect x="-18" y="-10" width="22" height="16" fill="{f("#16a34a")}" stroke="{K}"/><path d="M4 -4 h8 l6 6 v4 h-14z" fill="#fde047" stroke="{K}"/><circle cx="-10" cy="8" r="4" fill="#111"/><circle cx="10" cy="8" r="4" fill="#111"/>',
        'bike': f'<circle cx="-10" cy="6" r="7" fill="none" stroke="{K}" stroke-width="2"/><circle cx="10" cy="6" r="7" fill="none" stroke="{K}" stroke-width="2"/><path d="M-10 6 L-2 -6 L8 -6 L10 6 M-2 -6 L0 6" stroke="{f("#dc2626")}" stroke-width="2.5" fill="none"/>',
        'plane': f'<path d="M-18 0 Q-14 -4 14 -3 Q19 0 14 3 Q-14 4 -18 0z" fill="{f("#e5e7eb")}" stroke="{K}"/><path d="M-2 -2 L-10 -14 L-5 -14 L6 -2z M-2 2 L-10 14 L-5 14 L6 2z" fill="{f("#3b82f6")}" stroke="{K}"/>',
        'helicopter': f'<ellipse cx="-2" cy="2" rx="12" ry="8" fill="{f("#ef4444")}" stroke="{K}"/><path d="M10 0 H20" stroke="{K}" stroke-width="3"/><path d="M-18 -9 H14 M-2 -9 V-6" stroke="{K}" stroke-width="2"/>',
        'boat': f'<path d="M-16 4 H16 L10 12 H-10z" fill="{f("#92400e")}" stroke="{K}"/><path d="M0 4 V-16 L12 2z" fill="#fff" stroke="{K}"/>',
        'train': f'<rect x="-17" y="-10" width="34" height="18" rx="2" fill="{f("#dc2626")}" stroke="{K}"/><circle cx="-9" cy="10" r="4" fill="#111"/><circle cx="9" cy="10" r="4" fill="#111"/>',
        'flower': f'<g fill="{f("#ec4899")}" stroke="{K}"><circle cy="-8" r="6"/><circle cx="8" r="6"/><circle cy="8" r="6"/><circle cx="-8" r="6"/></g><circle r="5" fill="#facc15" stroke="{K}"/>',
        'leaf': f'<path d="M-12 12 C-14 -6 2 -14 14 -14 C14 0 4 14 -12 12z" fill="{f("#22c55e")}" stroke="{K}"/><path d="M-12 12 L10 -10" stroke="#14532d"/>',
        'tree': f'<rect x="-3" y="4" width="6" height="14" fill="#92400e"/><circle cy="-4" r="13" fill="{f("#16a34a")}" stroke="{K}"/>',
        'star': f'<path d="M0 -15 L4.4 -5 L15 -4.6 L7 2.5 L9.3 13 L0 7.4 L-9.3 13 L-7 2.5 L-15 -4.6 L-4.4 -5z" fill="{f("#facc15")}" stroke="{K}"/>',
        'sun': f'<circle r="9" fill="{f("#facc15")}" stroke="{K}"/><g stroke="#f59e0b" stroke-width="2"><path d="M0 -12 V-17 M0 12 V17 M-12 0 H-17 M12 0 H17 M8.5 8.5 L12 12 M-8.5 -8.5 L-12 -12 M8.5 -8.5 L12 -12 M-8.5 8.5 L-12 12"/></g>',
        'moon': f'<path d="M6 -13 A14 14 0 1 0 6 13 A10 10 0 0 1 6 -13z" fill="{f("#fde047")}" stroke="{K}"/>',
        'cloud': f'<path d="M-14 8 a7 7 0 0 1 2 -13 a9 9 0 0 1 17 -2 a7 7 0 0 1 9 8 a6 6 0 0 1 -3 7z" fill="{f("#e0f2fe")}" stroke="{K}"/>',
        'heart': f'<path d="M0 13 C-18 0 -12 -14 0 -6 C12 -14 18 0 0 13z" fill="{f("#ef4444")}" stroke="{K}"/>',
        'umbrella': f'<path d="M-16 0 A16 14 0 0 1 16 0 q-4 -3 -8 0 q-4 -3 -8 0 q-4 -3 -8 0 q-4 -3 -8 0z" fill="{f("#a855f7")}" stroke="{K}"/><path d="M0 0 V12 q0 4 -4 4" stroke="{K}" stroke-width="2" fill="none"/>',
        'fish': f'<path d="M-12 0 C-6 -10 8 -10 12 0 C8 10 -6 10 -12 0z" fill="{f("#38bdf8")}" stroke="{K}"/><path d="M12 0 L19 -7 V7z" fill="{f("#38bdf8")}" stroke="{K}"/><circle cx="-6" cy="-2" r="1.5" fill="#111"/>',
        'bird': f'<ellipse cx="-2" cy="2" rx="11" ry="8" fill="{f("#38bdf8")}" stroke="{K}"/><circle cx="8" cy="-5" r="6" fill="{f("#38bdf8")}" stroke="{K}"/><path d="M13 -5 l5 1 l-5 2z" fill="#f59e0b"/><circle cx="9" cy="-6" r="1.2" fill="#111"/><path d="M-6 0 q4 -8 8 0" stroke="{K}" fill="none"/>',
        'butterfly': f'<g fill="{f("#f97316")}" stroke="{K}"><path d="M0 0 C-6 -16 -18 -12 -14 -2 C-18 8 -6 12 0 0z"/><path d="M0 0 C6 -16 18 -12 14 -2 C18 8 6 12 0 0z"/></g><rect x="-1.5" y="-9" width="3" height="18" rx="1.5" fill="#111"/>',
        'bee': f'<ellipse rx="11" ry="8" fill="{f("#facc15")}" stroke="{K}"/><path d="M-3 -8 v16 M3 -8 v16" stroke="#111" stroke-width="2.5"/><ellipse cx="-3" cy="-11" rx="5" ry="4" fill="#e0f2fe" stroke="{K}"/><ellipse cx="4" cy="-11" rx="5" ry="4" fill="#e0f2fe" stroke="{K}"/>',
        'ladybird': f'<circle cy="2" r="12" fill="{f("#dc2626")}" stroke="{K}"/><path d="M0 -10 V14" stroke="#111"/><circle cy="-11" r="5" fill="#111"/><g fill="#111"><circle cx="-6" cy="0" r="2"/><circle cx="6" cy="0" r="2"/><circle cx="-5" cy="8" r="2"/><circle cx="5" cy="8" r="2"/></g>',
        'duck': f'<ellipse cx="-2" cy="5" rx="13" ry="8" fill="{f("#facc15")}" stroke="{K}"/><circle cx="8" cy="-6" r="6" fill="{f("#facc15")}" stroke="{K}"/><path d="M13 -6 l6 2 l-6 2z" fill="#f97316"/><circle cx="9" cy="-7" r="1.2" fill="#111"/>',
        'hen': f'<ellipse cx="-2" cy="4" rx="12" ry="10" fill="{f("#f5f5f4")}" stroke="{K}"/><circle cx="8" cy="-7" r="6" fill="{f("#f5f5f4")}" stroke="{K}"/><path d="M5 -13 l2 -4 l2 3 l2 -3 l1 4z" fill="#dc2626"/><path d="M13 -7 l5 1 l-5 2z" fill="#f59e0b"/>',
        'chick': f'<circle cy="4" r="10" fill="{f("#fde047")}" stroke="{K}"/><circle cx="5" cy="-8" r="6" fill="{f("#fde047")}" stroke="{K}"/><path d="M10 -8 l4 1 l-4 2z" fill="#f97316"/>',
        'cat': f'<circle cy="2" r="12" fill="{f("#f59e0b")}" stroke="{K}"/><path d="M-11 -4 L-9 -16 L-2 -10z M11 -4 L9 -16 L2 -10z" fill="{f("#f59e0b")}" stroke="{K}"/><circle cx="-4" cy="0" r="1.5" fill="#111"/><circle cx="4" cy="0" r="1.5" fill="#111"/>',
        'dog': f'<circle cy="2" r="12" fill="{f("#d6a35c")}" stroke="{K}"/><ellipse cx="-12" cy="0" rx="4" ry="9" fill="#78350f"/><ellipse cx="12" cy="0" rx="4" ry="9" fill="#78350f"/><circle cx="0" cy="6" r="2.5" fill="#111"/>',
        'rabbit': f'<ellipse cx="-5" cy="-12" rx="3" ry="9" fill="{f("#f5f5f4")}" stroke="{K}"/><ellipse cx="5" cy="-12" rx="3" ry="9" fill="{f("#f5f5f4")}" stroke="{K}"/><circle cy="5" r="11" fill="{f("#f5f5f4")}" stroke="{K}"/>',
        'sheep': f'<ellipse cy="2" rx="14" ry="10" fill="{f("#f5f5f4")}" stroke="{K}"/><circle cx="12" cy="-4" r="5" fill="#374151"/><path d="M-8 10 v6 M6 10 v6" stroke="#374151" stroke-width="2"/>',
        'cow': f'<rect x="-14" y="-6" width="26" height="14" rx="5" fill="{f("#f5f5f4")}" stroke="{K}"/><circle cx="-4" cy="0" r="3" fill="#111"/><circle cx="14" cy="-6" r="5" fill="{f("#f5f5f4")}" stroke="{K}"/><path d="M-10 8 v8 M8 8 v8" stroke="{K}" stroke-width="2"/>',
        'teddy': f'<circle cx="-9" cy="-11" r="4" fill="{f("#b45309")}"/><circle cx="9" cy="-11" r="4" fill="{f("#b45309")}"/><circle cy="-4" r="9" fill="{f("#b45309")}"/><ellipse cy="10" rx="10" ry="8" fill="{f("#b45309")}"/><circle cx="-3" cy="-5" r="1.2" fill="#111"/><circle cx="3" cy="-5" r="1.2" fill="#111"/>',
        'doll': f'<circle cy="-9" r="7" fill="#fcd34d" stroke="{K}"/><path d="M-10 16 L0 -2 L10 16z" fill="{f("#ec4899")}" stroke="{K}"/>',
        'cap': f'<path d="M-14 4 A14 14 0 0 1 14 4z" fill="{f("#2563eb")}" stroke="{K}"/><path d="M8 4 h12" stroke="{K}" stroke-width="3"/>',
        'hat': f'<path d="M-10 6 L0 -16 L10 6z" fill="{f("#a855f7")}" stroke="{K}"/><ellipse cy="6" rx="12" ry="3" fill="{f("#a855f7")}" stroke="{K}"/><circle cy="-16" r="3" fill="#facc15"/>',
        'shirt': f'<path d="M-6 -14 L-16 -8 L-12 0 L-8 -3 V14 H8 V-3 L12 0 L16 -8 L6 -14 Q0 -9 -6 -14z" fill="{f("#3b82f6")}" stroke="{K}"/>',
        'shoe': f'<path d="M-16 8 V-6 h8 q2 8 10 8 l8 2 q4 2 4 4z" fill="{f("#92400e")}" stroke="{K}"/>',
        'cup': f'<path d="M-10 -10 h18 l-2 22 h-14z" fill="{f("#38bdf8")}" stroke="{K}"/><path d="M8 -6 q8 0 6 8 q-1 4 -6 4" stroke="{K}" fill="none" stroke-width="2"/>',
        'glass': f'<path d="M-9 -14 h18 l-3 28 h-12z" fill="{f("#bae6fd")}" stroke="{K}"/>',
        'bottle': f'<path d="M-4 -16 h8 v6 q6 2 6 8 v18 h-20 v-18 q0 -6 6 -8z" fill="{f("#22c55e")}" stroke="{K}"/>',
        'house': f'<path d="M-15 0 L0 -14 L15 0z" fill="{f("#dc2626")}" stroke="{K}"/><rect x="-11" y="0" width="22" height="15" fill="#fde68a" stroke="{K}"/><rect x="-3" y="5" width="6" height="10" fill="#92400e"/>',
        'chair': f'<path d="M-8 -14 V12 M-8 2 H8 V12" stroke="{f("#92400e")}" stroke-width="4" fill="none"/>',
        'clockicon': f'<circle r="14" fill="#fff" stroke="{K}" stroke-width="2"/><path d="M0 0 V-9 M0 0 H7" stroke="{K}" stroke-width="2"/>',
        'button': f'<circle r="11" fill="{f("#3b82f6")}" stroke="{K}"/><g fill="#fff"><circle cx="-3" cy="-3" r="1.6"/><circle cx="3" cy="-3" r="1.6"/><circle cx="-3" cy="3" r="1.6"/><circle cx="3" cy="3" r="1.6"/></g>',
        'marble': f'<circle r="10" fill="{f("#38bdf8")}" stroke="{K}"/><path d="M-5 -4 q3 -4 7 -3" stroke="#fff" stroke-width="2" fill="none"/>',
        'block': f'<rect x="-11" y="-11" width="22" height="22" fill="{f("#22c55e")}" stroke="{K}"/><path d="M-11 -11 l5 -5 h22 l-5 5 M11 11 l5 -5 v-22" fill="none" stroke="{K}"/>',
        'cube': f'<rect x="-8" y="-8" width="16" height="16" fill="{f("#f59e0b")}" stroke="{K}"/>',
        'stick': f'<rect x="-2" y="-16" width="4" height="32" rx="1.5" fill="{f("#d97706")}" stroke="{K}" stroke-width="0.8"/>',
        'dot': f'<circle r="8" fill="{f("#1f2937")}"/>',
        'counter': f'<circle r="11" fill="{f("#ef4444")}" stroke="{K}"/>',
        'circle': f'<circle r="15" fill="{f("#3b82f6")}" stroke="{K}"/>',
        'square': f'<rect x="-14" y="-14" width="28" height="28" fill="{f("#22c55e")}" stroke="{K}"/>',
        'rect': f'<rect x="-17" y="-10" width="34" height="20" fill="{f("#f97316")}" stroke="{K}"/>',
        'triangle': f'<path d="M0 -15 L16 13 L-16 13z" fill="{f("#facc15")}" stroke="{K}"/>',
        'oval': f'<ellipse rx="17" ry="11" fill="{f("#a855f7")}" stroke="{K}"/>',
        'rattle': f'<circle cy="-7" r="10" fill="{f("#c026d3")}" stroke="{K}"/><path d="M-4 -7 a4 4 0 0 1 6 -4" stroke="#fff" fill="none" stroke-width="2"/><ellipse cy="10" rx="5" ry="8" fill="none" stroke="#22c55e" stroke-width="3"/>',
        'tumbler': f'<circle cy="6" r="11" fill="{f("#f59e0b")}" stroke="{K}"/><circle cy="-9" r="7" fill="#fde68a" stroke="{K}"/><path d="M-4 -15 l4 -5 l4 5z" fill="#16a34a"/><circle cx="-2" cy="-9" r="1" fill="#111"/><circle cx="2" cy="-9" r="1" fill="#111"/>',
        'rings': f'<path d="M-15 14 h30" stroke="#7c3aed" stroke-width="6"/><path d="M-12 8 h24" stroke="#3b82f6" stroke-width="6"/><path d="M-9 2 h18" stroke="#22c55e" stroke-width="6"/><path d="M-6 -4 h12" stroke="#facc15" stroke-width="6"/><path d="M-4 -10 h8" stroke="#f97316" stroke-width="6"/><circle cy="-15" r="3.5" fill="#ef4444"/>',
        'jelly': f'<path d="M-12 14 L-9 -10 Q0 -15 9 -10 L12 14z" fill="{f("#b91c1c")}" stroke="{K}"/><path d="M-5 -11 L-6 13 M2 -12 L2 14 M8 -10 L9 13" stroke="#7f1d1d"/>',
        'tart': f'<path d="M-14 0 L-11 12 H11 L14 0z" fill="#d6a35c" stroke="{K}"/><ellipse rx="14" ry="5" fill="{f("#fb923c")}" stroke="{K}"/><circle cy="-4" r="3" fill="#dc2626"/>',
        'pumpkin': f'<ellipse cx="-6" cy="3" rx="8" ry="11" fill="{f("#ea580c")}" stroke="{K}"/><ellipse cx="6" cy="3" rx="8" ry="11" fill="{f("#ea580c")}" stroke="{K}"/><ellipse cy="3" rx="6" ry="12" fill="{f("#f97316")}" stroke="{K}"/><path d="M0 -9 l2 -6" stroke="#15803d" stroke-width="3"/>',
        'date': f'<ellipse rx="14" ry="8" fill="{f("#451a03")}" stroke="{K}" transform="rotate(-15)"/><path d="M-8 -2 q8 -5 16 0" stroke="#92400e" fill="none" stroke-width="2"/>',
        'gift': f'<rect x="-12" y="-6" width="24" height="20" fill="{f("#fef3c7")}" stroke="{K}"/><rect x="-14" y="-11" width="28" height="6" fill="{f("#fef3c7")}" stroke="{K}"/><path d="M0 -11 V14" stroke="#dc2626" stroke-width="4"/><path d="M0 -11 q-8 -9 -10 -2 q4 3 10 2 q8 -9 10 -2 q-4 3 -10 2" fill="#dc2626"/>',
        'beachball': f'<circle r="13" fill="#fff" stroke="{K}"/><path d="M0 -13 A13 13 0 0 1 13 0 L0 0z" fill="#ef4444"/><path d="M0 13 A13 13 0 0 1 -13 0 L0 0z" fill="#facc15"/><path d="M-13 0 A13 13 0 0 1 0 -13 L0 0z" fill="#22c55e"/><circle r="13" fill="none" stroke="{K}"/>',
        'snail': f'<path d="M-16 12 H14 q4 0 4 -6 l-3 -8" stroke="#65a30d" stroke-width="5" fill="none"/><circle cx="-2" cy="0" r="11" fill="{f("#b45309")}" stroke="{K}"/><path d="M-8 0 a6 6 0 1 0 6 -6 a3 3 0 1 0 3 3" stroke="#fde68a" fill="none" stroke-width="2"/><path d="M15 -2 l-2 -8 M18 -2 l2 -8" stroke="#65a30d" stroke-width="2"/>',
        'eraser': f'<g transform="rotate(-20)"><rect x="-14" y="-7" width="28" height="14" rx="3" fill="{f("#f9a8d4")}" stroke="{K}"/><rect x="2" y="-7" width="12" height="14" rx="3" fill="#a78bfa" stroke="{K}"/></g>',
        'basket': f'<path d="M-15 -2 H15 L11 14 H-11z" fill="{f("#d97706")}" stroke="{K}"/><path d="M-12 -2 Q0 -22 12 -2" stroke="{K}" stroke-width="2" fill="none"/><path d="M-13 4 H13 M-12 9 H12" stroke="#92400e"/>',
        'nest': f'<ellipse cy="6" rx="17" ry="8" fill="{f("#a16207")}" stroke="{K}"/><path d="M-15 4 q15 8 30 0" stroke="#713f12" fill="none"/>',
        'pen': f'<g transform="rotate(-45)"><rect x="-3.5" y="-17" width="7" height="28" rx="2" fill="{f("#1d4ed8")}" stroke="{K}"/><path d="M-3.5 11 L0 19 L3.5 11z" fill="#94a3b8" stroke="{K}"/></g>',
        'sharpener': f'<rect x="-11" y="-8" width="22" height="16" rx="2" fill="{f("#ef4444")}" stroke="{K}"/><circle cx="-3" cy="0" r="4" fill="#fff" stroke="{K}"/>',
        'scale': f'<rect x="-17" y="-5" width="34" height="10" fill="{f("#fde047")}" stroke="{K}"/><path d="M-13 -5 v4 M-9 -5 v3 M-5 -5 v4 M-1 -5 v3 M3 -5 v4 M7 -5 v3 M11 -5 v4" stroke="{K}"/>',
        'horse': f'<path d="M-15 12 Q0 20 15 12" stroke="#dc2626" stroke-width="3" fill="none"/><path d="M-11 12 V4 M9 12 V4" stroke="{K}" stroke-width="2.5"/><ellipse cy="1" rx="12" ry="6" fill="{f("#fdba74")}" stroke="{K}"/><path d="M8 -2 L13 -14 L18 -11 L14 -1z" fill="{f("#fdba74")}" stroke="{K}"/><path d="M-6 -4 h8 v5 h-8z" fill="#22c55e"/>',
        'tulip': f'<path d="M0 0 V16" stroke="#15803d" stroke-width="2.5"/><path d="M0 8 q-8 -2 -9 -8 q7 1 9 8" fill="#22c55e"/><path d="M-8 -14 L-4 -8 L0 -15 L4 -8 L8 -14 Q9 0 0 0 Q-9 0 -8 -14z" fill="{f("#ef4444")}" stroke="{K}"/>',
        'pencilv': f'<rect x="-3.5" y="-12" width="7" height="28" fill="{f("#ef4444")}" stroke="{K}" stroke-width="0.8"/><path d="M-3.5 -12 L0 -19 L3.5 -12z" fill="#fde68a" stroke="{K}" stroke-width="0.8"/><path d="M-1 -17 L0 -19 L1 -17z" fill="{f("#ef4444")}"/>',
        'bundle': ''.join(f'<rect x="{-14 + i * 2.9:.1f}" y="-16" width="2.6" height="32" rx="1" fill="{["#ef4444","#3b82f6","#22c55e","#f59e0b","#a855f7"][i % 5]}" stroke="{K}" stroke-width="0.4"/>' for i in range(10)) + '<rect x="-16" y="-3" width="32" height="6" rx="2" fill="#dc2626" stroke="#7f1d1d"/>',
        'beadring': ''.join(f'<circle cx="{12 * __import__("math").cos(i * 0.6283):.1f}" cy="{12 * __import__("math").sin(i * 0.6283):.1f}" r="4" fill="{["#16a34a","#3b82f6","#f97316","#dc2626","#7c3aed"][i % 5]}" stroke="{K}" stroke-width="0.5"/>' for i in range(10)),
        'bead': f'<circle r="5" fill="{f("#16a34a")}" stroke="{K}" stroke-width="0.5"/>',
        'runner': f'<circle cy="-11" r="6" fill="#f2c094" stroke="{K}"/><path d="M-6 -15 q6 -6 12 0" fill="#3f2a1d"/><rect x="-5" y="-5" width="10" height="11" rx="2" fill="{f("#3b82f6")}" stroke="{K}"/><path d="M-3 6 l-5 10 M3 6 l6 9 M-5 -2 l-7 5 M5 -2 l7 -4" stroke="{K}" stroke-width="2.4" stroke-linecap="round"/>',
        'frog': f'<ellipse cy="4" rx="12" ry="9" fill="{f("#4ade80")}" stroke="{K}"/><circle cx="-6" cy="-6" r="5" fill="#fff" stroke="{K}"/><circle cx="6" cy="-6" r="5" fill="#fff" stroke="{K}"/><circle cx="-6" cy="-6" r="2" fill="#111"/><circle cx="6" cy="-6" r="2" fill="#111"/><path d="M-5 4 q5 4 10 0" stroke="#7f1d1d" fill="none"/><ellipse cy="15" rx="15" ry="3" fill="#15803d" opacity=".7"/>',
        'owl': f'<ellipse cy="3" rx="12" ry="14" fill="{f("#4a2c2a")}" stroke="{K}"/><ellipse cy="7" rx="7" ry="8" fill="#f9a8d4"/><circle cx="-5" cy="-5" r="5" fill="#fff" stroke="{K}"/><circle cx="5" cy="-5" r="5" fill="#fff" stroke="{K}"/><circle cx="-5" cy="-5" r="2" fill="#111"/><circle cx="5" cy="-5" r="2" fill="#111"/><path d="M-11 -10 l3 -6 l3 4 M11 -10 l-3 -6 l-3 4" fill="{f("#4a2c2a")}" stroke="{K}"/><path d="M-2 0 l2 3 l2 -3z" fill="#f59e0b"/>',
        'donut2': f'<circle r="13" fill="{f("#7c2d12")}" stroke="{K}"/><circle r="5" fill="#fef3c7" stroke="{K}"/>',
        'lock': f'<path d="M-7 -4 V-10 a7 7 0 0 1 14 0 V-4" stroke="#78716c" stroke-width="3" fill="none"/><rect x="-11" y="-4" width="22" height="18" rx="3" fill="{f("#d4a24c")}" stroke="{K}"/><circle cy="3" r="2.5" fill="#3f2a1d"/><path d="M0 4 v5" stroke="#3f2a1d" stroke-width="2"/>',
        'key': f'<circle cx="-11" r="5" fill="{f("#d4a24c")}" stroke="{K}"/><circle cx="-11" r="1.8" fill="#fff"/><path d="M-6 0 H15 M10 0 v5 M14 0 v4" stroke="{K}" stroke-width="3"/>',
        'cupg': f'<path d="M-12 -8 h22 l-3 18 h-16z" fill="{f("#16a34a")}" stroke="{K}"/><path d="M10 -4 q8 0 6 7 q-2 4 -7 4" stroke="{K}" fill="none" stroke-width="2"/>',
        'plate': f'<ellipse rx="17" ry="6" fill="{f("#16a34a")}" stroke="{K}"/><ellipse rx="10" ry="3" fill="none" stroke="#14532d"/>',
        'chickfront': f'<ellipse cy="5" rx="9" ry="11" fill="{f("#facc15")}" stroke="{K}"/><circle cy="-9" r="7" fill="{f("#facc15")}" stroke="{K}"/><path d="M-2 -8 l2 3 l2 -3z" fill="#f97316"/><circle cx="-3" cy="-11" r="1.2" fill="#111"/><circle cx="3" cy="-11" r="1.2" fill="#111"/>',
        'ant': f'<g fill="{f("#b91c1c")}" stroke="{K}" stroke-width="0.6"><circle cx="-10" r="4.5"/><ellipse cx="-1" rx="4" ry="3.5"/><ellipse cx="10" rx="6.5" ry="5"/></g><path d="M-3 2 l-4 8 M0 2 l0 9 M3 2 l4 8 M-3 -2 l-4 -7 M0 -2 l0 -8 M3 -2 l4 -7 M-12 -4 l-4 -7" stroke="{K}" fill="none"/>',
        'spider': f'<path d="M-4 0 l-12 -8 M-4 2 l-13 2 M-4 4 l-11 9 M4 0 l12 -8 M4 2 l13 2 M4 4 l11 9 M-3 -2 l-8 -12 M3 -2 l8 -12" stroke="{K}" stroke-width="1.6" fill="none"/><ellipse cy="3" rx="8" ry="8" fill="{f("#1f2937")}"/><circle cy="-6" r="4.5" fill="{f("#1f2937")}"/><circle cx="-1.5" cy="-7" r="1" fill="#f87171"/><circle cx="1.5" cy="-7" r="1" fill="#f87171"/>',
        'dragonfly': f'<g fill="#bae6fd" stroke="#0369a1" stroke-width="0.6" opacity=".9"><ellipse cx="-9" cy="-4" rx="9" ry="3" transform="rotate(-15 -9 -4)"/><ellipse cx="9" cy="-4" rx="9" ry="3" transform="rotate(15 9 -4)"/><ellipse cx="-8" cy="2" rx="8" ry="2.6" transform="rotate(15 -8 2)"/><ellipse cx="8" cy="2" rx="8" ry="2.6" transform="rotate(-15 8 2)"/></g><rect x="-1.5" y="-8" width="3" height="24" rx="1.5" fill="{f("#0ea5e9")}"/><circle cy="-9" r="3" fill="{f("#0ea5e9")}"/>',
        'caterpillar': ''.join(f'<circle cx="{-14 + i * 6}" cy="{2 - (2 if i % 2 else 0)}" r="5" fill="{f("#65a30d")}" stroke="{K}" stroke-width="0.6"/>' for i in range(5)) + f'<circle cx="16" cy="-2" r="6" fill="{f("#65a30d")}" stroke="{K}"/><circle cx="18" cy="-4" r="1.3" fill="#111"/>',
        'grasshopper': f'<ellipse cx="-2" cy="2" rx="12" ry="5" fill="{f("#84cc16")}" stroke="{K}"/><circle cx="11" cy="-1" r="4.5" fill="{f("#84cc16")}" stroke="{K}"/><path d="M-6 0 L4 -10 L10 8 M-12 4 l-3 6 M12 -5 q6 -8 10 -7" stroke="{K}" fill="none" stroke-width="1.4"/>',
        'firefly': f'<ellipse cx="-6" cy="-8" rx="7" ry="5" fill="#e0f2fe" stroke="{K}" stroke-width="0.6"/><ellipse cx="6" cy="-8" rx="7" ry="5" fill="#e0f2fe" stroke="{K}" stroke-width="0.6"/><ellipse cy="4" rx="7" ry="10" fill="{f("#facc15")}" stroke="{K}"/><circle cy="-6" r="5" fill="#78350f"/><circle cx="-2" cy="-7" r="1.3" fill="#fff"/><circle cx="2" cy="-7" r="1.3" fill="#fff"/>',
        'turtle': f'<path d="M-14 6 Q0 -18 14 6z" fill="{f("#5b3a1e")}" stroke="{K}"/><path d="M-8 -2 l6 6 l6 -6" stroke="#a16207" fill="none"/><ellipse cy="7" rx="17" ry="4" fill="#4ade80" stroke="{K}"/><circle cx="17" cy="2" r="4.5" fill="#4ade80" stroke="{K}"/>',
        'tent': f'<path d="M0 -17 L13 14 H-13z" fill="{f("#3b82f6")}" stroke="{K}"/><path d="M0 -17 L-5 14 M0 -17 L5 14" stroke="#1e3a8a"/><path d="M0 -17 l-4 -4 M0 -17 l4 -4" stroke="#78350f" stroke-width="2"/><path d="M-13 14 H13" stroke="#be123c" stroke-width="3"/>',
        'racket': f'<g transform="rotate(35)"><ellipse cy="-6" rx="9" ry="12" fill="#e5e7eb" stroke="{K}" stroke-width="2"/><path d="M-6 -12 H6 M-8 -6 H8 M-6 0 H6 M-3 -16 V4 M3 -16 V4" stroke="#94a3b8" stroke-width="0.7"/><rect x="-1.8" y="6" width="3.6" height="14" fill="{f("#1f2937")}"/></g>',
        'colorbox': f'<rect x="-11" y="-12" width="22" height="28" rx="2" fill="{f("#f59e0b")}" stroke="{K}"/><g stroke="{K}" stroke-width="0.5"><rect x="-9" y="-17" width="4" height="7" fill="#ef4444"/><rect x="-4" y="-17" width="4" height="7" fill="#22c55e"/><rect x="1" y="-17" width="4" height="7" fill="#3b82f6"/><rect x="6" y="-17" width="3" height="7" fill="#a855f7"/></g><text y="4" text-anchor="middle" font-size="6" font-weight="700" fill="#7f1d1d">COLORS</text>',
        'brinjal': f'<ellipse cx="2" cy="3" rx="13" ry="9" fill="{f("#4c1d95")}" stroke="{K}" transform="rotate(15)"/><path d="M-12 -6 q4 -6 10 -2 l-2 4z" fill="#15803d"/><path d="M-12 -6 l-5 -4" stroke="#15803d" stroke-width="2"/>',
        'chilli': f'<path d="M-12 6 Q4 6 12 -6 Q8 4 -10 9z" fill="{f("#dc2626")}" stroke="{K}"/><path d="M12 -6 l3 -4" stroke="#15803d" stroke-width="2"/>',
        'shark': f'<path d="M-18 2 Q-4 -10 16 0 Q-4 8 -18 2z" fill="{f("#475569")}" stroke="{K}"/><path d="M-2 -5 l3 -9 l5 7z M-18 2 l-5 -7 l1 9z" fill="{f("#475569")}" stroke="{K}"/><path d="M-14 4 Q0 8 14 1" stroke="#e2e8f0" fill="none" stroke-width="2"/>',
        'elephant': f'<ellipse cx="2" cy="0" rx="13" ry="10" fill="{f("#6b7280")}" stroke="{K}"/><circle cx="-12" cy="-4" r="7" fill="{f("#6b7280")}" stroke="{K}"/><path d="M-17 -1 q-4 8 -1 15" stroke="{f("#6b7280")}" stroke-width="4" fill="none"/><path d="M-6 8 v8 M0 8 v8 M7 8 v8 M12 6 v10" stroke="{f("#6b7280")}" stroke-width="4"/><ellipse cx="-8" cy="-5" rx="5" ry="7" fill="#9ca3af" stroke="{K}"/>',
        'giraffe': f'<ellipse cy="4" rx="10" ry="6" fill="{f("#f59e0b")}" stroke="{K}"/><path d="M6 2 L10 -16" stroke="{f("#f59e0b")}" stroke-width="5"/><ellipse cx="12" cy="-17" rx="5" ry="3" fill="{f("#f59e0b")}" stroke="{K}"/><path d="M-7 9 v9 M-2 9 v9 M4 9 v9 M8 9 v9" stroke="{f("#f59e0b")}" stroke-width="2.5"/><g fill="#92400e"><circle cx="-3" cy="3" r="1.6"/><circle cx="3" cy="5" r="1.6"/><circle cx="8" cy="-6" r="1.3"/></g>',
        'snake': f'<path d="M-18 8 Q-10 -2 -2 8 T14 4" stroke="{f("#a16207")}" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="15" cy="2" r="4.5" fill="{f("#a16207")}" stroke="{K}"/><path d="M19 2 l4 1" stroke="#dc2626"/>',
        'bush': f'<circle cx="-7" cy="2" r="9" fill="{f("#15803d")}" stroke="{K}"/><circle cx="7" cy="2" r="9" fill="{f("#15803d")}" stroke="{K}"/><circle cy="-7" r="10" fill="{f("#16a34a")}" stroke="{K}"/><rect x="-2" y="10" width="4" height="7" fill="#78350f"/>',
        'pine': f'<path d="M0 -18 L10 -4 H5 L13 8 H-13 L-5 -4 H-10z" fill="{f("#166534")}" stroke="{K}"/><rect x="-2" y="8" width="4" height="10" fill="#78350f"/>',
        'candlev': f'<rect x="-4" y="-8" width="8" height="26" fill="{f("#60a5fa")}" stroke="{K}"/><path d="M0 -10 q-4 -5 0 -9 q4 4 0 9z" fill="#f59e0b"/>',
        'plant': f'<path d="M0 14 C-2 0 -12 -6 -14 -14 C-6 -10 -2 -4 0 4 C2 -6 4 -14 10 -17 C8 -8 4 0 2 14z" fill="{f("#15803d")}" stroke="{K}" stroke-width="0.8"/><ellipse cy="15" rx="10" ry="3" fill="#3f2a1d"/>',
        'flag': f'<path d="M-12 -18 V18" stroke="#334155" stroke-width="1.6"/><rect x="-12" y="-18" width="26" height="17" fill="{f("#166534")}"/><rect x="-12" y="-18" width="7" height="17" fill="#fff"/><circle cx="4" cy="-9.5" r="4.5" fill="#fff"/><circle cx="5.5" cy="-10.5" r="4" fill="{f("#166534")}"/><circle cx="8.5" cy="-13" r="1.2" fill="#fff"/>',
        'building': f'<rect x="-10" y="-18" width="20" height="36" fill="{f("#e2e8f0")}" stroke="{K}"/>' + ''.join(f'<rect x="{-7 + (i % 3) * 5}" y="{-15 + (i // 3) * 5}" width="3" height="3" fill="#94a3b8"/>' for i in range(18)) + f'<rect x="-3" y="12" width="6" height="6" fill="#64748b"/>',
        'hospital': f'<rect x="-15" y="-10" width="30" height="26" fill="{f("#5eead4")}" stroke="{K}"/><path d="M-17 -10 L0 -19 L17 -10z" fill="#1e293b"/><rect x="-11" y="-6" width="22" height="5" fill="#fef9c3"/><text y="-2" text-anchor="middle" font-size="4" font-weight="700" fill="#7f1d1d">Hospital</text><rect x="-4" y="6" width="8" height="10" fill="#0e7490"/><rect x="-12" y="3" width="6" height="5" fill="#bae6fd"/><rect x="6" y="3" width="6" height="5" fill="#bae6fd"/>',
        'school': f'<rect x="-15" y="-6" width="30" height="20" fill="{f("#b91c1c")}" stroke="{K}"/><path d="M-17 -6 L0 -15 L17 -6z" fill="#1e293b"/><rect x="-4" y="4" width="8" height="10" fill="#bae6fd"/><rect x="-12" y="0" width="6" height="5" fill="#bae6fd"/><rect x="6" y="0" width="6" height="5" fill="#bae6fd"/>',
        'mountain': f'<path d="M-18 14 L-6 -8 L0 -2 L5 -16 L18 14z" fill="{f("#92400e")}" stroke="{K}"/><path d="M5 -16 L1 -6 L5 -4 L8 -9z" fill="#b45309"/>',
        'lamp': f'<path d="M0 -8 V16" stroke="{f("#1f2937")}" stroke-width="2.5"/><path d="M-4 16 h8 l-1 -3 h-6z" fill="{f("#1f2937")}"/><path d="M-4 -16 h8 v8 h-8z" fill="#fde68a" stroke="{f("#1f2937")}" stroke-width="1.5"/><path d="M-5 -16 L0 -20 L5 -16z M-4 -8 h8" stroke="{f("#1f2937")}" stroke-width="1.5" fill="{f("#1f2937")}"/>',
        'melon': f'<ellipse rx="16" ry="12" fill="{f("#fde047")}" stroke="{K}"/><path d="M-8 -10 Q-12 0 -8 10 M0 -12 V12 M8 -10 Q12 0 8 10" stroke="#ca8a04" fill="none"/>',
        'cabbage': f'<circle r="14" fill="{f("#4d7c0f")}" stroke="{K}"/><path d="M-10 -4 Q0 -14 10 -4 M-12 4 Q0 -6 12 4 M0 -14 V14" stroke="#a3e635" fill="none"/>',
        'peas': f'<path d="M-17 2 Q0 -8 17 -2 Q0 8 -17 2z" fill="{f("#4d7c0f")}" stroke="{K}"/><g fill="#84cc16"><circle cx="-8" cy="1" r="3"/><circle cx="0" cy="0" r="3"/><circle cx="8" cy="-1" r="3"/></g>',
        'goat': f'<ellipse cx="-2" cy="0" rx="12" ry="7" fill="{f("#3f2a1d")}" stroke="{K}"/><path d="M8 -3 L14 -12 L18 -9 L14 -1z" fill="{f("#3f2a1d")}" stroke="{K}"/><path d="M14 -12 q-4 -6 -8 -5" stroke="#78716c" stroke-width="2" fill="none"/><path d="M-10 6 v10 M-5 6 v10 M4 6 v10 M8 6 v10" stroke="{f("#3f2a1d")}" stroke-width="2.5"/>',
        'brush': f'<g transform="rotate(30)"><rect x="-2" y="-18" width="4" height="22" fill="{f("#7c2d12")}"/><rect x="-2.5" y="4" width="5" height="5" fill="#9ca3af"/><path d="M-3 9 Q0 20 3 9z" fill="#78350f"/></g>',
        'pencilbox': f'<rect x="-17" y="-8" width="34" height="16" rx="5" fill="{f("#4ade80")}" stroke="{K}"/><path d="M-15 -6 L0 4 L15 -6" stroke="#0e7490" fill="#67e8f9"/>',
        'feather': f'<path d="M-16 14 Q0 0 16 -14" stroke="#1e3a8a" stroke-width="1.4" fill="none"/><path d="M-10 9 Q-6 -6 12 -12 Q8 4 -10 9z" fill="{f("#16a34a")}" opacity=".85"/><circle cx="8" cy="-8" r="3" fill="#1e40af"/>',
        'bat': f'<g transform="rotate(-45)"><rect x="-5" y="-6" width="10" height="26" rx="3" fill="{f("#a8a29e")}" stroke="{K}"/><rect x="-2" y="-20" width="4" height="14" fill="#1f2937"/></g>',
        'cycle': f'<circle cx="-10" cy="6" r="7" fill="none" stroke="{K}" stroke-width="2"/><circle cx="10" cy="6" r="7" fill="none" stroke="{K}" stroke-width="2"/><path d="M-10 6 L-2 -6 L8 -6 L10 6 M-2 -6 L0 6 M8 -6 l2 -5 M-4 -8 h6" stroke="{f("#0d9488")}" stroke-width="2.5" fill="none"/>',
        'pot': f'<path d="M-14 -8 h28 l-4 22 h-20z" fill="{f("#ffffff")}" stroke="{K}" stroke-width="1.4"/><ellipse cy="-8" rx="14" ry="3.5" fill="#e7e5e4" stroke="{K}"/>',
        'cupboard': f'<rect x="-13" y="-18" width="26" height="36" fill="{f("#3f2a1d")}" stroke="{K}"/><path d="M0 -16 V8 M-12 8 H12" stroke="#78716c"/><circle cx="-2" cy="-4" r="1" fill="#d6d3d1"/><circle cx="2" cy="-4" r="1" fill="#d6d3d1"/>',
        'cabinet': f'<rect x="-11" y="-14" width="22" height="28" fill="{f("#5b3a1e")}" stroke="{K}"/><path d="M-11 -4 H11 M-11 4 H0 M0 -4 V14" stroke="#a16207"/>',
        'schoolbag': f'<path d="M-6 -14 q6 -8 12 0" stroke="{K}" stroke-width="2" fill="none"/><rect x="-12" y="-14" width="24" height="30" rx="6" fill="{f("#ffffff")}" stroke="{K}" stroke-width="1.4"/><rect x="-9" y="2" width="18" height="10" rx="2" fill="none" stroke="{K}"/>',
        'clipboard': f'<rect x="-11" y="-15" width="22" height="30" rx="1" fill="{f("#ffffff")}" stroke="{K}" stroke-width="1.4"/><rect x="-5" y="-18" width="10" height="5" rx="1" fill="#9ca3af" stroke="{K}"/>',
        'tennis': f'<circle r="12" fill="{f("#a3e635")}" stroke="{K}"/><path d="M-11 -4 Q0 2 -4 11 M11 4 Q0 -2 4 -11" stroke="#fff" stroke-width="1.6" fill="none"/>',
        'juice': f'<rect x="-11" y="-15" width="22" height="30" fill="{f("#dc2626")}" stroke="{K}"/><circle cy="-2" r="7" fill="#f97316" stroke="#fff"/><text y="11" text-anchor="middle" font-size="5" font-weight="700" fill="#fff">JUICE</text>',
        'burger': f'<path d="M-15 -2 Q0 -18 15 -2z" fill="{f("#d97706")}" stroke="{K}"/><rect x="-16" y="-2" width="32" height="4" fill="#16a34a"/><rect x="-15" y="2" width="30" height="5" fill="#7c2d12"/><path d="M-15 7 h30 q0 7 -6 7 h-18 q-6 0 -6 -7z" fill="{f("#d97706")}" stroke="{K}"/>',
        'crisps': f'<path d="M-11 -15 L11 -15 L13 15 L-13 15z" fill="{f("#f97316")}" stroke="{K}"/><path d="M-11 -15 l3 -3 h16 l3 3" fill="#fbbf24" stroke="{K}"/><ellipse cy="2" rx="6" ry="4" fill="#fde047"/>',
        'palette': f'<path d="M0 -14 C14 -14 18 0 10 6 C6 9 8 14 0 14 C-12 14 -16 4 -16 -2 C-16 -9 -8 -14 0 -14z" fill="{f("#d97706")}" stroke="{K}"/><g stroke="{K}" stroke-width="0.5"><circle cx="-8" cy="-4" r="3" fill="#ef4444"/><circle cx="-2" cy="-9" r="3" fill="#facc15"/><circle cx="6" cy="-7" r="3" fill="#3b82f6"/><circle cx="-8" cy="5" r="3" fill="#22c55e"/></g><circle cx="3" cy="3" r="3" fill="#fff"/>',
        'wheel': f'<circle r="15" fill="none" stroke="{f("#334155")}" stroke-width="3"/><circle r="3" fill="#334155"/>' + ''.join(f'<path d="M0 0 L{15 * __import__("math").cos(i * 0.5236):.1f} {15 * __import__("math").sin(i * 0.5236):.1f}" stroke="#334155"/>' for i in range(12)),
        'carrom': f'<rect x="-15" y="-15" width="30" height="30" fill="{f("#f5d0a9")}" stroke="#1f2937" stroke-width="3"/><circle r="5" fill="none" stroke="#7c2d12"/><g fill="#1f2937"><circle cx="-11" cy="-11" r="2"/><circle cx="11" cy="-11" r="2"/><circle cx="-11" cy="11" r="2"/><circle cx="11" cy="11" r="2"/></g>',
        'rectv': f'<rect x="-9" y="-16" width="18" height="32" fill="{f("#ec4899")}" stroke="{K}"/>',
        'door': f'<rect x="-9" y="-16" width="18" height="32" fill="{f("#44403c")}" stroke="{K}"/><circle cx="5" cy="2" r="1.5" fill="#fde68a"/>',
        'tv': f'<rect x="-18" y="-12" width="36" height="22" rx="1" fill="#1f2937"/><rect x="-16" y="-10" width="32" height="18" fill="{f("#93c5fd")}"/><path d="M-4 10 L-6 15 H6 L4 10z" fill="#1f2937"/>',
        'dice': f'<rect x="-14" y="-14" width="28" height="28" rx="4" fill="{f("#6d28d9")}" stroke="{K}"/><g fill="#fff"><circle cx="-6" cy="-6" r="3"/><circle cx="6" cy="-6" r="3"/><circle cx="-6" cy="6" r="3"/><circle cx="6" cy="6" r="3"/></g>',
        'ludo': f'<rect x="-15" y="-15" width="30" height="30" fill="#fef9c3" stroke="{K}"/><rect x="-15" y="-15" width="11" height="11" fill="#fde047"/><rect x="4" y="-15" width="11" height="11" fill="#86efac"/><rect x="-15" y="4" width="11" height="11" fill="#fca5a5"/><rect x="4" y="4" width="11" height="11" fill="#c4b5fd"/>',
        'pizza': f'<circle r="15" fill="#b45309" stroke="{K}"/><circle r="12" fill="#fde047"/><path d="M0 -12 V12 M-12 0 H12 M-8.5 -8.5 L8.5 8.5 M8.5 -8.5 L-8.5 8.5" stroke="#b45309"/><g fill="#7f1d1d"><circle cx="-5" cy="-7" r="1.6"/><circle cx="6" cy="3" r="1.6"/><circle cx="-4" cy="6" r="1.6"/></g>',
        'warning': f'<path d="M0 -15 L15 12 H-15z" fill="#fff" stroke="{f("#dc2626")}" stroke-width="3"/><path d="M0 -6 V3" stroke="#111" stroke-width="3"/><circle cy="7" r="1.6" fill="#111"/><path d="M0 12 V18" stroke="#6b7280" stroke-width="3"/>',
        'hanger': f'<path d="M0 -8 q0 -4 3 -6 q3 -2 3 -5" stroke="#9ca3af" stroke-width="1.5" fill="none"/><path d="M0 -8 L17 8 H-17z" fill="none" stroke="{f("#f97316")}" stroke-width="3"/>',
        'girl': f'<circle cy="-8" r="7" fill="#f2c094" stroke="{K}"/><path d="M-8 -9 q8 -12 16 0 l1 6 l-3 -5 q-5 -4 -11 0 l-3 5z" fill="#f59e0b"/><path d="M-9 16 L-5 0 H5 L9 16z" fill="{f("#ec4899")}" stroke="{K}"/>',
        'boy': f'<circle cy="-8" r="7" fill="#f2c094" stroke="{K}"/><path d="M-7 -11 q7 -8 14 0z" fill="#7c2d12"/><rect x="-6" y="-1" width="12" height="10" rx="2" fill="{f("#4d7c0f")}" stroke="{K}"/><path d="M-3 9 v8 M3 9 v8" stroke="{K}" stroke-width="2.5"/>',
        'fire': f'<path d="M-12 12 L12 6 M-12 6 L12 12" stroke="#7c2d12" stroke-width="3"/><path d="M0 6 C-10 0 -6 -8 -2 -14 C0 -8 4 -10 4 -16 C10 -8 10 2 0 6z" fill="{f("#f97316")}"/>',
        'coop': f'<path d="M-18 -4 L0 -18 L18 -4z" fill="#57534e" stroke="{K}"/><rect x="-15" y="-4" width="30" height="20" fill="{f("#78716c")}" stroke="{K}"/><rect x="-4" y="2" width="9" height="14" fill="#1c1917"/><rect x="-13" y="0" width="7" height="6" fill="#a8a29e"/>',
        'jar': f'<rect x="-11" y="-17" width="22" height="6" rx="2" fill="#e5e7eb" stroke="{K}"/><path d="M-12 -11 h24 q3 0 3 6 v18 q0 6 -6 6 h-18 q-6 0 -6 -6 v-18 q0 -6 3 -6z" fill="{f("#ffffff")}" stroke="{K}" stroke-width="1.4"/>',
        'cloud2': f'<path d="M-14 8 a7 7 0 0 1 2 -13 a9 9 0 0 1 17 -2 a7 7 0 0 1 9 8 a6 6 0 0 1 -3 7z" fill="#ffffff" stroke="#94a3b8"/>',
        'sofa': f'<rect x="-18" y="-8" width="36" height="12" rx="3" fill="{f("#2f6f5e")}" stroke="{K}"/><rect x="-20" y="0" width="40" height="9" rx="3" fill="{f("#2f6f5e")}" stroke="{K}"/><path d="M-15 9 v5 M15 9 v5" stroke="#1f2937" stroke-width="2.5"/>',
        'frame': f'<rect x="-12" y="-11" width="24" height="22" fill="#bae6fd" stroke="#92400e" stroke-width="3"/><path d="M-10 9 L-3 -2 L2 4 L6 -3 L10 9z" fill="#475569"/><path d="M-6 -11 L0 -17 L6 -11" stroke="#475569" fill="none"/>',
        'seahorse': f'<path d="M2 -14 q8 0 6 8 q-3 6 -6 6 q4 6 0 12 q-4 4 -6 0 q2 -2 4 -4 q-6 -4 -2 -12 q-6 -2 -4 -8 q2 -4 8 -2z" fill="{f("#fde68a")}" stroke="{K}"/>',
        'board': f'<rect x="-18" y="-11" width="36" height="22" fill="{f("#14532d")}" stroke="#92400e" stroke-width="3"/>',
        'crocodile': f'<path d="M-18 4 Q-6 -4 14 0 L20 2 L14 5 Q-6 9 -18 4z" fill="{f("#15803d")}" stroke="{K}"/><circle cx="8" cy="-1" r="1.5" fill="#111"/><path d="M-8 2 l2 -3 l2 3 l2 -3 l2 3" stroke="#14532d" fill="none"/>',
        'kitten': f'<circle cy="2" r="9" fill="{f("#fb923c")}" stroke="{K}"/><path d="M-8 -3 L-7 -12 L-2 -7z M8 -3 L7 -12 L2 -7z" fill="{f("#fb923c")}" stroke="{K}"/><circle cx="-3" cy="1" r="1.2" fill="#111"/><circle cx="3" cy="1" r="1.2" fill="#111"/>',
        'table': f'<rect x="-18" y="-6" width="36" height="5" fill="{f("#92400e")}" stroke="{K}"/><path d="M-15 -1 V14 M15 -1 V14" stroke="{f("#92400e")}" stroke-width="3"/>',
        'bed': f'<rect x="-18" y="-2" width="36" height="9" fill="{f("#60a5fa")}" stroke="{K}"/><rect x="-18" y="-10" width="5" height="22" fill="#92400e"/><rect x="13" y="-6" width="5" height="18" fill="#92400e"/><ellipse cx="-9" cy="-4" rx="5" ry="3" fill="#fff" stroke="{K}"/>',
        'umbrella2': f'<path d="M-16 0 A16 14 0 0 1 16 0z" fill="{f("#ef4444")}" stroke="{K}"/><path d="M0 0 V14 q0 4 -4 4" stroke="{K}" stroke-width="2" fill="none"/>',
        'rain': '<g stroke="#38bdf8" stroke-width="1.5"><path d="M-12 -6 l-2 6 M-4 -10 l-2 6 M6 -6 l-2 6 M14 -10 l-2 6 M-8 4 l-2 6 M10 4 l-2 6"/></g>',
        'slide': f'<path d="M-16 -12 L0 -20 L16 -12z" fill="#f97316" stroke="{K}"/><path d="M-13 -12 V16 M13 -12 V16 M-4 -12 V16" stroke="#1f2937" stroke-width="2.5"/><path d="M-13 -2 H13" stroke="#3b82f6" stroke-width="2"/><path d="M-2 -2 L18 14 L14 16 L-6 0z" fill="{f("#fb923c")}" stroke="{K}"/>',
        'fence': f'<path d="M-10 16 V-14 M10 16 V-14" stroke="#fff" stroke-width="3"/><path d="M-10 -4 H10 M-10 4 H10" stroke="{f("#ef4444")}" stroke-width="2.5"/><path d="M-14 16 H-6 M6 16 H14" stroke="#fff" stroke-width="3"/>',
        'barn': f'<path d="M-18 -4 Q0 -20 18 -4z" fill="#7f1d1d" stroke="{K}"/><rect x="-16" y="-4" width="32" height="20" fill="{f("#92400e")}" stroke="{K}"/><rect x="-7" y="2" width="14" height="14" fill="#fde68a" stroke="{K}"/><path d="M-7 2 L7 16 M7 2 L-7 16" stroke="{K}"/>',
        'pond': f'<ellipse rx="18" ry="7" fill="{f("#38bdf8")}" stroke="#0369a1"/><circle cx="-6" cy="-1" r="2.5" fill="#f472b6"/>',
        'jeep': f'<path d="M-17 6 V-4 h6 l2 -8 h14 v8 h12 v10z" fill="{f("#ea580c")}" stroke="{K}"/><circle cx="-9" cy="8" r="5" fill="#111"/><circle cx="10" cy="8" r="5" fill="#111"/>',
        'rickshaw': f'<path d="M-14 8 V-6 Q-14 -14 -4 -14 H8 Q14 -14 16 -2 L18 8z" fill="{f("#65a30d")}" stroke="{K}"/><path d="M-4 -12 V6" stroke="{K}"/><circle cx="-8" cy="9" r="4" fill="#111"/><circle cx="14" cy="9" r="4" fill="#111"/>',
        'bear': f'<ellipse cx="-2" cy="2" rx="15" ry="9" fill="{f("#f8fafc")}" stroke="{K}"/><circle cx="13" cy="-3" r="6" fill="{f("#f8fafc")}" stroke="{K}"/><circle cx="11" cy="-8" r="2" fill="{f("#f8fafc")}" stroke="{K}"/><path d="M-12 9 v8 M-6 9 v8 M4 9 v8 M9 8 v9" stroke="{K}" stroke-width="2.5"/>',
        'camel': f'<path d="M-14 4 Q-14 -6 -8 -10 Q-4 -4 0 -10 Q4 -4 8 -4 L12 -14 L17 -14 L17 -11 L14 -10 L11 4z" fill="{f("#f8fafc")}" stroke="{K}"/><path d="M-12 4 v13 M-6 4 v13 M4 4 v13 M9 4 v13" stroke="{K}" stroke-width="2"/>',
        'lion': f'<ellipse cx="-3" cy="3" rx="12" ry="7" fill="{f("#f8fafc")}" stroke="{K}"/><circle cx="12" cy="-3" r="8" fill="{f("#f8fafc")}" stroke="{K}" stroke-dasharray="2 1"/><circle cx="13" cy="-3" r="4.5" fill="{f("#f8fafc")}" stroke="{K}"/><path d="M-12 9 v8 M-7 9 v8 M3 9 v8 M7 9 v8 M-15 2 q-6 -2 -5 -8" stroke="{K}" stroke-width="2" fill="none"/>',
        'pizzaslice': f'<path d="M-16 -8 L16 0 L-16 8z" fill="{f("#fbbf24")}" stroke="#b45309" stroke-width="2"/><g fill="#7f1d1d"><circle cx="-8" cy="-1" r="1.8"/><circle cx="2" cy="1" r="1.5"/></g>',
        'cakeslice': f'<path d="M-16 10 L16 10 L16 -6 L-16 2z" fill="{f("#78350f")}" stroke="{K}"/><path d="M-16 2 L16 -6" stroke="#fef3c7" stroke-width="2"/><circle cx="8" cy="-8" r="3" fill="#dc2626"/>',
        'phone': f'<rect x="-8" y="-15" width="16" height="30" rx="3" fill="#111827"/><rect x="-6" y="-11" width="12" height="20" fill="{f("#60a5fa")}"/>',
        'waffle': f'<rect x="-14" y="-14" width="28" height="28" fill="{f("#d97706")}" stroke="#92400e"/><path d="M-7 -14 V14 M0 -14 V14 M7 -14 V14 M-14 -7 H14 M-14 0 H14 M-14 7 H14" stroke="#92400e"/>',
        'clocksq': f'<rect x="-15" y="-15" width="30" height="30" fill="{f("#fde047")}" stroke="{K}"/><circle r="11" fill="#fff" stroke="{K}"/><path d="M0 0 V-8 M0 0 H6" stroke="{K}" stroke-width="2"/>',
        'tyre': f'<circle r="15" fill="#111827"/><circle r="8" fill="#d1d5db"/><circle r="2" fill="#6b7280"/>',
        'envelope': f'<rect x="-16" y="-10" width="32" height="20" fill="{f("#38bdf8")}" stroke="{K}"/><path d="M-16 -10 L0 3 L16 -10" stroke="{K}" fill="none"/>',
        'button2': f'<circle r="12" fill="{f("#7c2d12")}" stroke="{K}"/><g fill="#fde68a"><circle cx="-3" cy="-3" r="1.5"/><circle cx="3" cy="-3" r="1.5"/><circle cx="-3" cy="3" r="1.5"/><circle cx="3" cy="3" r="1.5"/></g>',
        'tunnel': f'<ellipse cx="-14" rx="5" ry="12" fill="#7f1d1d" stroke="{K}"/><rect x="-14" y="-12" width="28" height="24" fill="{f("#dc2626")}" stroke="{K}"/><ellipse cx="14" rx="5" ry="12" fill="#111" stroke="{K}"/>',
        'net': f'<path d="M-14 16 L2 0" stroke="#1f2937" stroke-width="3"/><ellipse cx="8" cy="-7" rx="9" ry="11" fill="none" stroke="#1f2937" stroke-width="2" transform="rotate(40 8 -7)"/><path d="M2 -14 L14 0 M-2 -8 L10 4 M6 -16 L16 -4" stroke="#7c3aed" stroke-width="0.8"/>',
        'top': f'<path d="M-15 -2 Q0 -12 15 -2 L0 14z" fill="{f("#22c55e")}" stroke="{K}"/><ellipse cy="-3" rx="15" ry="5" fill="#fde047" stroke="{K}"/><path d="M0 -8 V-16" stroke="#dc2626" stroke-width="3"/>',
        'soap': f'<path d="M-16 4 h32 l-4 8 h-24z" fill="#1d4ed8" stroke="{K}"/><rect x="-11" y="-6" width="22" height="11" rx="4" fill="{f("#fcd34d")}" stroke="{K}"/><g fill="#bfdbfe"><circle cx="-8" cy="-9" r="2.5"/><circle cx="2" cy="-11" r="3"/><circle cx="9" cy="-8" r="2"/></g>',
        'van': f'<path d="M-18 8 V-6 Q-18 -12 -12 -12 H8 L18 -2 V8z" fill="{f("#1e3a8a")}" stroke="{K}"/><path d="M8 -10 L16 -2 H8z" fill="#bae6fd"/><rect x="-14" y="-9" width="18" height="6" fill="#bae6fd"/><circle cx="-10" cy="9" r="4" fill="#111"/><circle cx="10" cy="9" r="4" fill="#111"/>',
        'jug': f'<path d="M-10 -12 h16 l-2 4 q8 6 0 22 h-12 q-8 -16 -2 -22z" fill="{f("#f59e0b")}" stroke="{K}" opacity="0.9"/><path d="M6 -6 q10 0 8 10 q-2 4 -6 4" stroke="{K}" fill="none" stroke-width="2"/>',
        'fan': f'<path d="M0 4 V15 M-8 16 H8" stroke="#475569" stroke-width="2.5"/><circle cy="-6" r="10" fill="none" stroke="{f("#0ea5e9")}" stroke-width="2"/><path d="M0 -6 l-6 -6 M0 -6 l8 -2 M0 -6 l-2 8" stroke="{f("#0ea5e9")}" stroke-width="4" stroke-linecap="round"/>',
        'pin': f'<path d="M-4 0 H16" stroke="#6b7280" stroke-width="2"/><circle cx="-8" r="6" fill="{f("#dc2626")}" stroke="{K}"/>',
        'box': f'<path d="M-12 -6 L0 -12 L12 -6 V10 L0 16 L-12 10z" fill="{f("#92400e")}" stroke="{K}"/><path d="M-12 -6 L0 0 L12 -6 M0 0 V16" stroke="{K}" fill="none"/>',
        'hoop': f'<ellipse cy="-8" rx="13" ry="4" fill="none" stroke="#f97316" stroke-width="2.5"/><path d="M-12 -7 L-8 12 M-4 -4 L-3 12 M4 -4 L3 12 M12 -7 L8 12 M-10 2 H10" stroke="#9ca3af"/>',
        'lemon': f'<ellipse rx="11" ry="8" fill="{f("#facc15")}" stroke="{K}"/><path d="M-11 0 l-3 0 M11 0 l3 0" stroke="#ca8a04" stroke-width="2"/>',
        'bread': f'<ellipse cy="8" rx="17" ry="5" fill="#b91c1c"/><path d="M-12 6 V-4 Q-12 -12 -2 -12 H6 Q14 -12 14 -4 V6z" fill="{f("#f5d0a9")}" stroke="#92400e"/><path d="M-4 -12 V6 M4 -12 V6" stroke="#92400e"/>',
        'drum': f'<ellipse cy="-6" rx="15" ry="5" fill="#fde68a" stroke="{K}"/><path d="M-15 -6 V10 Q0 16 15 10 V-6" fill="{f("#dc2626")}" stroke="{K}"/><path d="M-15 4 L-8 -2 L0 6 L8 -2 L15 4" stroke="#1d4ed8" stroke-width="2" fill="none"/><path d="M-4 -10 L6 -20 M4 -10 L14 -18" stroke="#78350f" stroke-width="2"/>',
        'legoblock': f'<rect x="-14" y="-6" width="28" height="18" fill="{f("#15803d")}" stroke="{K}"/><g fill="{f("#15803d")}" stroke="{K}"><rect x="-11" y="-11" width="6" height="5"/><rect x="-3" y="-11" width="6" height="5"/><rect x="5" y="-11" width="6" height="5"/></g>',
        'crown': f'<path d="M-14 8 L-14 -8 L-7 0 L0 -12 L7 0 L14 -8 L14 8z" fill="{f("#facc15")}" stroke="{K}"/><circle cy="2" r="2.5" fill="#dc2626"/>',
        'zebra': f'<ellipse cx="-2" cy="0" rx="12" ry="7" fill="#fff" stroke="{K}"/><path d="M-8 -6 v12 M-3 -7 v14 M2 -7 v14 M7 -6 v12" stroke="#111" stroke-width="1.6"/><path d="M8 -3 L14 -14 L18 -12 L14 0z" fill="#fff" stroke="{K}"/><path d="M-10 6 v10 M-5 6 v10 M3 6 v10 M8 6 v10" stroke="{K}" stroke-width="2"/>',
        'shoe': f'<path d="M-16 8 V-4 h8 q2 6 8 6 l10 2 q6 2 6 6 v2 h-32z" fill="{f("#dc2626")}" stroke="{K}"/><path d="M-10 -2 l8 2 M-9 1 l8 2" stroke="#fff"/>',
        'jar2': f'<rect x="-8" y="-12" width="16" height="4" rx="1" fill="#9ca3af"/><rect x="-9" y="-8" width="18" height="22" rx="3" fill="{f("#f8fafc")}" stroke="{K}"/>',
        'guava': f'<circle cy="2" r="12" fill="{f("#84cc16")}" stroke="{K}"/><path d="M0 -10 l-2 -5" stroke="#78350f" stroke-width="2"/><path d="M2 -12 q8 -6 12 0 q-6 4 -12 0z" fill="#15803d"/>',
        'happy': f'<circle r="15" fill="{f("#f59e0b")}" stroke="{K}"/><circle cx="-5" cy="-4" r="2" fill="#111"/><circle cx="5" cy="-4" r="2" fill="#111"/><path d="M-8 3 q8 10 16 0" stroke="#7f1d1d" stroke-width="2" fill="#fff"/>',
        'sad': f'<circle r="15" fill="{f("#f59e0b")}" stroke="{K}"/><circle cx="-5" cy="-4" r="2" fill="#111"/><circle cx="5" cy="-4" r="2" fill="#111"/><path d="M-7 9 q7 -7 14 0" stroke="#7f1d1d" stroke-width="2" fill="none"/>',
        'angry': f'<circle r="15" fill="{f("#ea580c")}" stroke="{K}"/><path d="M-9 -8 l7 3 M9 -8 l-7 3" stroke="#111" stroke-width="2"/><circle cx="-5" cy="-2" r="1.8" fill="#111"/><circle cx="5" cy="-2" r="1.8" fill="#111"/><rect x="-7" y="5" width="14" height="5" fill="#fff" stroke="#7f1d1d"/>',
        'blankface': f'<circle r="15" fill="{f("#fcd9b6")}" stroke="{K}"/>',
        'apricot': f'<circle cx="-4" r="10" fill="{f("#fb923c")}" stroke="{K}"/><circle cx="7" cy="3" r="8" fill="#fdba74" stroke="{K}"/><circle cx="7" cy="3" r="3" fill="#92400e"/><path d="M-6 -10 q-6 -6 -12 -2 q6 4 12 2" fill="#16a34a"/>',
        'turnip': f'<circle cy="3" r="11" fill="#f5f3ff" stroke="{K}"/><path d="M-11 0 a11 11 0 0 1 22 0z" fill="{f("#7c3aed")}"/><path d="M0 14 v5 M0 -8 l-6 -10 M0 -8 l6 -10" stroke="#16a34a" stroke-width="2.5"/>',
        'cucumber': f'<ellipse rx="17" ry="7" fill="{f("#4d7c0f")}" stroke="{K}"/><g fill="#a3e635"><circle cx="-8" cy="-2" r="1"/><circle cx="0" cy="2" r="1"/><circle cx="8" cy="-1" r="1"/></g>',
        'okra': f'<path d="M-16 -2 L14 -4 L18 0 L14 4 L-16 2z" fill="{f("#65a30d")}" stroke="{K}"/><path d="M-12 0 H14" stroke="#3f6212"/>',
        'onion': f'<path d="M0 -16 q2 6 10 12 q6 8 0 14 h-20 q-6 -6 0 -14 q8 -6 10 -12z" fill="{f("#9f1239")}" stroke="{K}"/><path d="M0 -10 V10 M-5 -4 q-2 8 0 14 M5 -4 q2 8 0 14" stroke="#fda4af" fill="none" stroke-width="0.8"/>',
        'milk': f'<path d="M-9 -10 L0 -16 L9 -10 V16 H-9z" fill="#f8fafc" stroke="{K}"/><rect x="-9" y="-6" width="18" height="8" fill="{f("#3b82f6")}"/><text y="0" text-anchor="middle" font-size="5" font-weight="700" fill="#fff">Milk</text>',
        'ketchup': f'<rect x="-3" y="-17" width="6" height="6" fill="#111"/><path d="M-3 -11 q-6 4 -6 12 v14 h18 v-14 q0 -8 -6 -12z" fill="{f("#dc2626")}" stroke="{K}"/><rect x="-6" y="0" width="12" height="7" fill="#fde68a"/>',
        'loaf': f'<rect x="-10" y="-12" width="20" height="26" rx="3" fill="{f("#b45309")}" stroke="{K}"/><path d="M-10 -12 q10 -8 20 0" fill="#bae6fd" opacity=".6"/><text y="4" text-anchor="middle" font-size="5" font-weight="700" fill="#fff">Bread</text>',
        'iron': f'<path d="M-15 8 Q-12 -10 6 -10 H12 V8z" fill="{f("#bae6fd")}" stroke="{K}"/><path d="M-4 -10 Q0 -18 10 -16 V-10" stroke="{K}" fill="none" stroke-width="2"/><rect x="-16" y="8" width="30" height="4" fill="#9ca3af"/>',
        'leftsign': f'<rect x="-11" y="-11" width="22" height="22" transform="rotate(45)" fill="{f("#facc15")}" stroke="{K}" stroke-width="2"/><path d="M4 8 V0 Q4 -4 0 -4 H-6 M-3 -8 L-7 -4 L-3 0" stroke="#111" stroke-width="2.5" fill="none"/>',
        'rightsign': f'<rect x="-11" y="-11" width="22" height="22" transform="rotate(45)" fill="{f("#facc15")}" stroke="{K}" stroke-width="2"/><path d="M-4 8 V0 Q-4 -4 0 -4 H6 M3 -8 L7 -4 L3 0" stroke="#111" stroke-width="2.5" fill="none"/>',
        'sweater': f'<path d="M-8 -14 L-16 -6 L-13 6 L-9 4 V16 H9 V4 L13 6 L16 -6 L8 -14 Q0 -8 -8 -14z" fill="{f("#92400e")}" stroke="{K}"/><path d="M-9 10 H9" stroke="#fbbf24" stroke-width="2"/>',
        'suit': f'<path d="M-9 -14 L-15 -8 V16 H15 V-8 L9 -14 L0 0z" fill="{f("#475569")}" stroke="{K}"/><path d="M-3 -14 L0 0 L3 -14" fill="#fff"/><path d="M0 0 V16" stroke="#1f2937"/>',
        'kurta': f'<path d="M-7 -14 L-15 -8 L-12 0 L-9 -2 V17 H9 V-2 L12 0 L15 -8 L7 -14 L0 -10z" fill="{f("#65a30d")}" stroke="{K}"/><path d="M0 -10 V2" stroke="{K}"/>',
        'gloves': f'<g fill="{f("#1d4ed8")}" stroke="{K}"><path d="M-14 14 V0 l-2 -6 l3 0 l2 4 v-10 h3 v8 v-10 h3 v10 v-8 h3 v10 l0 16z"/><path d="M4 14 V0 l-2 -6 l3 0 l2 4 v-10 h3 v8 v-10 h3 v10 v-8 h3 v10 l0 16z" transform="translate(0 2)"/></g>',
        'cheese': f'<path d="M-15 8 L12 -10 L15 8z" fill="{f("#fbbf24")}" stroke="{K}"/><g fill="#d97706"><circle cx="2" cy="2" r="2"/><circle cx="9" cy="-1" r="1.5"/></g>',
        'butter': f'<rect x="-14" y="-6" width="28" height="14" rx="2" fill="{f("#fef08a")}" stroke="{K}"/><path d="M-14 -6 l4 -5 h28 l-4 5" fill="#fef9c3" stroke="{K}"/>',
        'sandwich': f'<path d="M-15 8 L0 -12 L15 8z" fill="{f("#f5d0a9")}" stroke="{K}"/><path d="M-12 4 L0 -10 L12 4" stroke="#16a34a" stroke-width="2" fill="none"/>',
        'palm': f'<path d="M-9 16 V0 l-4 -6 l3 -2 l3 4 V-14 h3 v10 V-16 h3 v12 V-14 h3 v10 V-10 h3 v14 q0 12 -10 12z" fill="{f("#f2c094")}" stroke="{K}"/>',
        'knee': f'<path d="M-6 -16 L-8 0 Q-8 8 0 10 L10 16 L14 10 L4 4 Q6 -4 4 -16z" fill="{f("#fda4af")}" stroke="{K}"/>',
        'eye': f'<path d="M-16 0 Q0 -14 16 0 Q0 14 -16 0z" fill="#fff" stroke="{K}"/><circle r="6" fill="{f("#3b82f6")}"/><circle r="2.5" fill="#111"/><path d="M-14 -9 Q0 -18 14 -9" stroke="#111" stroke-width="2" fill="none"/>',
        'arm': f'<path d="M-16 -6 L4 -4 L14 10 L10 13 L0 2 L-16 2z" fill="{f("#f9a8d4")}" stroke="{K}"/><path d="M-16 -6 l-3 -3 l1 7z" fill="#f2c094" stroke="{K}"/>',
        'nose': f'<path d="M0 -16 Q-2 4 -9 8 Q-10 14 -4 14 Q0 11 4 14 Q10 14 9 8 Q2 4 0 -16z" fill="{f("#e8b48a")}" stroke="{K}"/>',
        'neck': f'<path d="M-6 -12 h12 v14 h-12z" fill="{f("#f97316")}" stroke="{K}"/><ellipse cy="-12" rx="12" ry="4" fill="#fb923c" stroke="{K}"/><path d="M-14 4 Q0 10 14 4 L16 16 H-16z" fill="#1e3a8a"/>',
        'tiger': f'<ellipse cx="-2" cy="2" rx="13" ry="7" fill="{f("#f97316")}" stroke="{K}"/><circle cx="12" cy="-3" r="6" fill="{f("#f97316")}" stroke="{K}"/><path d="M-8 -4 v10 M-3 -5 v12 M2 -5 v12 M7 -4 v10" stroke="#111" stroke-width="1.6"/><path d="M-10 8 v8 M-5 8 v8 M4 8 v8 M8 8 v8" stroke="{K}" stroke-width="2.5"/>',
        'bear': f'<ellipse cx="-2" cy="2" rx="14" ry="9" fill="{f("#78350f")}" stroke="{K}"/><circle cx="13" cy="-3" r="6" fill="{f("#78350f")}" stroke="{K}"/><circle cx="11" cy="-9" r="2" fill="{f("#78350f")}" stroke="{K}"/><path d="M-10 9 v7 M-4 9 v7 M4 9 v7 M9 9 v7" stroke="{f("#78350f")}" stroke-width="3.5"/>',
        'victory': f'<path d="M-8 16 V2 q0 -4 4 -4 h10 q4 0 4 4 v14z" fill="{f("#fdba74")}" stroke="{K}"/><path d="M-6 -2 L-10 -18 l4 -1 l4 16 M2 -2 L4 -19 l4 1 l-2 16" fill="{f("#fdba74")}" stroke="{K}"/>',
        'thumbup': f'<rect x="-10" y="-2" width="18" height="18" rx="4" fill="{f("#fdba74")}" stroke="{K}"/><path d="M-6 -2 L-4 -16 q4 -2 6 2 L0 -2" fill="{f("#fdba74")}" stroke="{K}"/>',
        'okhand': f'<circle cx="-4" cy="-6" r="6" fill="none" stroke="{f("#fdba74")}" stroke-width="4"/><path d="M-2 0 h12 v14 h-14 z M4 0 V-16 M8 0 V-14 M12 2 V-12" stroke="{f("#fdba74")}" stroke-width="4" fill="{f("#fdba74")}"/>',
        'tick':'<path d="M-10 0 L-3 8 L11 -9" stroke="#16a34a" stroke-width="4" fill="none"/>',
    }
    if name in s:
        return s[name]
    if name.startswith('bug') and name[3:].isdigit():
        n = int(name[3:])
        pos = [(0, 0), (-5, -4), (5, 4), (-5, 4), (5, -4), (0, -7), (0, 7), (-7, 0), (7, 0)][:n] if n <= 9 else []
        dots = ''.join(f'<circle cx="{x}" cy="{y + 3}" r="1.9" fill="#111"/>' for x, y in pos)
        return (f'<path d="M-6 -12 q-4 -6 -8 -6 M6 -12 q4 -6 8 -6" stroke="#111" stroke-width="1.6" fill="none"/>'
                f'<circle cy="3" r="13" fill="{f("#7c2d12")}" stroke="{K}"/>{dots}<path d="M-3 16 l3 -4 l3 4z" fill="#111"/>')
    if name.startswith('nest') and name[4:].isdigit():
        n = int(name[4:])
        eggs = ''.join(f'<ellipse cx="{(i - (n - 1) / 2) * 8:.1f}" cy="{-1 - (i % 2) * 3}" rx="5" ry="6" fill="#fb923c" stroke="{K}" stroke-width="0.6"/>' for i in range(n))
        return (f'<ellipse cy="2" rx="18" ry="7" fill="#fef3c7" stroke="#78350f"/>{eggs}'
                f'<path d="M-18 2 q18 14 36 0 l-2 6 q-16 10 -32 0z" fill="#d6a35c" stroke="#78350f"/><path d="M-14 5 l6 3 M-4 7 l5 2 M6 6 l5 3" stroke="#78350f"/>')
    if name == 'coin':
        return (f'<circle r="15" fill="#d4d4d8" stroke="{K}" stroke-width="1.5"/><circle r="11.5" fill="none" stroke="#71717a"/>'
                f'<path d="M-6 6 h12 M-5 6 v-7 h10 v7 M-2 -1 a2 2 0 0 1 4 0 M0 -9 v-2" stroke="#52525b" fill="none"/>')
    if name.startswith('coin'):
        v = name[4:]
        return (f'<circle r="15" fill="#d4d4d8" stroke="{K}" stroke-width="1.5"/><circle r="11.5" fill="none" stroke="#71717a"/>'
                f'<text y="5" text-anchor="middle" font-size="13" font-weight="700" fill="#1f2937">{v}</text>')
    if name.startswith('note'):
        v = name[4:]
        nc = {'10': '#a7f3d0', '20': '#fdba74', '50': '#d8b4fe', '100': '#fca5a5', '500': '#86efac', '1000': '#93c5fd', '5000': '#fde68a'}.get(v, '#e5e7eb')
        return (f'<rect x="-19" y="-11" width="38" height="22" rx="2" fill="{nc}" stroke="{K}"/><rect x="-16" y="-8" width="32" height="16" fill="none" stroke="#64748b" stroke-dasharray="2 1"/>'
                f'<text y="5" text-anchor="middle" font-size="{10 if len(v) < 4 else 8.5}" font-weight="700" fill="#1f2937">Rs {v}</text>')
    if name.startswith('hand'):
        return hand_g(int(name[4:]))
    raise ValueError('unknown icon ' + name)


WIDE = {'bus': 42, 'truck': 42, 'car': 40, 'plane': 42, 'train': 40, 'rect': 40, 'cow': 40, 'helicopter': 42}


def _cell(name):
    if name.startswith('note'):
        return 44
    return WIDE.get(name, 38)


def hand_g(n):
    """Hand with n raised fingers (thumb counts as the fifth)."""
    out = [f'<path d="M-11 0 v12 q0 6 6 6 h10 q6 0 6 -6 v-12z" fill="#fcd9b6" stroke="{K}"/>']
    xs = [-9, -4, 1, 6]
    for i, x in enumerate(xs):
        h = 16 if i < min(n, 4) else 4
        out.append(f'<rect x="{x - 2.4}" y="{-h}" width="4.8" height="{h + 2}" rx="2.4" fill="#fcd9b6" stroke="{K}"/>')
    if n >= 5:
        out.append(f'<rect x="10" y="-6" width="4.8" height="12" rx="2.4" fill="#fcd9b6" stroke="{K}" transform="rotate(35 12 4)"/>')
    return '<g transform="translate(0 -2)">' + ''.join(out) + '</g>'


def _svg(w, h, body, label):
    return (f'<svg viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" role="img" aria-label="{escape(label)}" '
            f'font-family="Segoe UI, Arial, sans-serif">' + ''.join(body) + '</svg>')


def _parse_item(tok):
    name, _, num = tok.partition(':')
    col = None
    if '.' in name:
        name, col = name.split('.', 1)
    wrap, cross = None, 0
    if '/' in num:
        num, w = num.split('/')
        wrap = int(w)
    if 'x' in num:
        num, k = num.split('x')
        cross = int(k)
    return name, col, int(num), wrap, cross


def cnt(spec, big=False):
    toks = spec.split()
    scale, framed = 1.0, False
    rows, cur = [], []
    for t in toks:
        if t.startswith('s='):
            scale = float(t[2:])
        elif t == 'frame':
            framed = True
        elif t == '|':
            rows.append(cur)
            cur = []
        else:
            cur.append(t)
    rows.append(cur)
    body, labels, defs = [], [], {}
    y, maxw = 8, 0
    for row in rows:
        x = 8
        row_h = 44
        parts = []
        for t in row:
            if ':' in t and not t.startswith('"'):
                name, col, n, wrap, cross = _parse_item(t)
                cw = _cell(name) * (1.3 if big else 1)
                per = wrap or n
                nrows = (n + per - 1) // per if n else 1
                gw = max(per, 1) * cw
                gh = nrows * (44 * (1.3 if big else 1))
                g = []
                for i in range(n):
                    cx = x + (i % per) * cw + cw / 2
                    cy = y + (i // per) * (44 * (1.3 if big else 1)) + 22 * (1.3 if big else 1)
                    sc = 1.3 if big else 1
                    iid = f'c1i-{name}-{(col or "d").lstrip("#")}'
                    if iid not in defs:
                        defs[iid] = f'<g id="{iid}">{_icon(name, col)}</g>'
                    g.append(f'<use href="#{iid}" transform="translate({cx:.1f} {cy:.1f}) scale({sc})"/>')
                    if cross and i >= n - cross:
                        g.append(f'<path d="M{cx - 14:.1f} {cy - 14:.1f} L{cx + 14:.1f} {cy + 14:.1f} M{cx + 14:.1f} {cy - 14:.1f} L{cx - 14:.1f} {cy + 14:.1f}" stroke="#dc2626" stroke-width="3"/>')
                if framed:
                    g.insert(0, f'<rect x="{x - 3}" y="{y - 2}" width="{gw + 6}" height="{gh + 4}" rx="8" fill="#fff7ed" stroke="#fb923c"/>')
                parts.extend(g)
                labels.append(f'{n} {name}' + (f' ({cross} crossed out)' if cross else ''))
                x += gw + 10
                row_h = max(row_h, gh)
            elif t.startswith('[') and t.endswith(']'):
                v = t[1:-1].replace('_', ' ')
                parts.append(f'<rect x="{x}" y="{y + 6}" width="34" height="32" rx="4" fill="#fff" stroke="#2563eb" stroke-width="1.5"/>')
                if v:
                    parts.append(f'<text x="{x + 17}" y="{y + 29}" text-anchor="middle" font-size="18" font-weight="700" fill="#1e3a8a">{escape(v)}</text>')
                labels.append(f'box {v}' if v else 'empty box')
                x += 42
            else:
                v = t.strip('"').replace('_', ' ')
                w = max(22, 11 * len(v) + 8)
                parts.append(f'<text x="{x + w / 2}" y="{y + 29}" text-anchor="middle" font-size="20" font-weight="700" fill="#0f172a">{escape(v)}</text>')
                labels.append(v)
                x += w + 4
        for p in parts:
            body.append(p)
        maxw = max(maxw, x)
        y += row_h + 10
    w, h = maxw + 4, y
    inner = ('<defs>' + ''.join(defs.values()) + '</defs>' if defs else '') + ''.join(body)
    return (f'<svg viewBox="0 0 {w:.0f} {h:.0f}" width="{w * scale:.0f}" role="img" aria-label="{escape(", ".join(labels))}" '
            f'font-family="Segoe UI, Arial, sans-serif">{inner}</svg>')


def shapes(spec):
    return cnt(spec, big=True)


def tens(spec):
    """'T O [sticks]' -> T tens and O ones."""
    a = spec.split()
    t, o = int(a[0]), int(a[1])
    sticks = 'sticks' in a[2:]
    xt, xo = 0, 0
    for tok in a[2:]:
        if tok.startswith('x'):
            xt, xo = (int(v) for v in tok[1:].split(','))
    body, x = [], 10
    cross = lambda x0, y0, x1, y1: body.append(f'<path d="M{x0} {y1} L{x1} {y0}" stroke="#111" stroke-width="2"/>')
    for k_ in range(t):
        if k_ < xt and not sticks:
            cross(x - 3, 6, x + 15, 80)
        if sticks:
            for k in range(10):
                body.append(f'<rect x="{x + k * 4}" y="10" width="3.2" height="60" rx="1.2" fill="#d97706" stroke="{K}" stroke-width="0.5"/>')
            body.append(f'<rect x="{x - 2}" y="36" width="44" height="7" fill="#dc2626"/>')
            x += 52
        else:
            for k in range(10):
                body.append(f'<rect x="{x}" y="{8 + k * 7}" width="12" height="7" fill="#3b82f6" stroke="{K}" stroke-width="0.6"/>')
            x += 20
    if t and o:
        x += 10
    for k in range(o):
        if sticks:
            body.append(f'<rect x="{x}" y="10" width="3.6" height="60" rx="1.2" fill="#d97706" stroke="{K}" stroke-width="0.5"/>')
            x += 10
        else:
            body.append(f'<rect x="{x}" y="64" width="12" height="12" fill="#f59e0b" stroke="{K}" stroke-width="0.6"/>')
            if k >= o - xo:
                cross(x - 3, 60, x + 15, 80)
            x += 16
    lab = f'{t} ten{"s" if t != 1 else ""} and {o} one{"s" if o != 1 else ""}' + (' (bundles of sticks)' if sticks else ' (blocks)') + (f'; {xt} tens and {xo} ones crossed out' if xt or xo else '')
    return _svg(x + 8, 84, body, lab)


def _card(x, y, v, w=40, h=44, fill='#fff'):
    v = '' if v == '_' else v
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="#2563eb" stroke-width="1.5"/>'
    if v:
        out += f'<text x="{x + w / 2}" y="{y + h / 2 + 8}" text-anchor="middle" font-size="22" font-weight="700" fill="#1e3a8a">{escape(v)}</text>'
    return out


def cards(spec):
    vals = [v.strip() for v in spec.split(',')]
    body = [_card(8 + i * 48, 6, v) for i, v in enumerate(vals)]
    return _svg(16 + 48 * len(vals), 58, body, 'Number cards: ' + ', '.join(v if v != '_' else 'blank' for v in vals))


def train(spec):
    vals = [v.strip() for v in spec.split(',')]
    body = [f'<path d="M8 20 h34 v-12 h10 v12 h6 v34 h-50z" fill="#ef4444" stroke="{K}"/><rect x="14" y="26" width="16" height="14" fill="#bae6fd" stroke="{K}"/>',
            '<circle cx="20" cy="58" r="6" fill="#111"/><circle cx="46" cy="58" r="6" fill="#111"/>']
    x = 66
    cols = ['#f59e0b', '#22c55e', '#3b82f6', '#a855f7', '#ec4899']
    for i, v in enumerate(vals):
        body.append(f'<rect x="{x}" y="14" width="52" height="40" rx="4" fill="{cols[i % 5]}" stroke="{K}"/>')
        body.append(_card(x + 8, 18, v, 36, 32))
        body.append(f'<circle cx="{x + 12}" cy="58" r="6" fill="#111"/><circle cx="{x + 40}" cy="58" r="6" fill="#111"/>')
        body.append(f'<path d="M{x - 6} 40 h6" stroke="{K}" stroke-width="3"/>')
        x += 60
    return _svg(x + 4, 70, body, 'Number train: ' + ', '.join(v if v != '_' else 'blank' for v in vals))


def tframe(spec):
    a = spec.split()
    n = int(a[0])
    col = _col(a[1] if len(a) > 1 else None, '#ef4444')
    body = []
    for i in range(10):
        x, y = 8 + (i % 5) * 36, 8 + (i // 5) * 36
        body.append(f'<rect x="{x}" y="{y}" width="36" height="36" fill="#fff" stroke="{K}"/>')
        if i < n:
            body.append(f'<circle cx="{x + 18}" cy="{y + 18}" r="12" fill="{col}" stroke="{K}"/>')
    return _svg(196, 88, body, f'Ten frame with {n} counters')


def hand(spec):
    n = int(spec.split()[0])
    return _svg(60, 52, [f'<g transform="translate(30 30) scale(1.2)">{hand_g(n)}</g>'], f'Hand showing {n} fingers')


OPS = {'cnt', 'shapes', 'tens', 'cards', 'train', 'tframe', 'hand'}


def stairs(spec):
    """'0-9 | Ascending order | Descending order' -> numbers climbing a staircase up (left) and down (right)."""
    parts = [p.strip() for p in spec.split('|')]
    a, b = (int(x) for x in parts[0].split('-'))
    up = parts[1] if len(parts) > 1 else 'Ascending order'
    down = parts[2] if len(parts) > 2 else 'Descending order'
    n = b - a + 1
    sw, sh = 26, 22
    W = 2 * n * sw + 40
    H = n * sh + 70
    base = H - 30
    body = [f'<path d="M10 {base} H{W - 10}" stroke="#ec4899" stroke-width="2"/>']
    d = f'M20 {base}'
    for i in range(n):
        x, y = 20 + i * sw, base - (i + 1) * sh
        d += f' V{y} H{x + sw}'
        body.append(f'<text x="{x + sw / 2}" y="{y + sh - 5}" text-anchor="middle" font-size="15" font-weight="600">{a + i}</text>')
    mid = 20 + n * sw
    for i in range(n):
        x, y = mid + i * sw, base - (n - i) * sh
        d += f' H{x + sw} V{y + sh}' if i else f' H{x + sw} V{y + sh}'
        body.append(f'<text x="{x + sw / 2}" y="{y + sh - 5}" text-anchor="middle" font-size="15" font-weight="600">{b - i}</text>')
    body.insert(0, f'<path d="{d}" fill="none" stroke="#ec4899" stroke-width="2"/>')
    body.append(f'<path d="M{mid} {base} V{base - n * sh}" stroke="#ec4899"/>')
    body.append(f'<path d="M40 {base - 10} L{mid - 30} {base - n * sh + 20}" stroke="#dc2626" stroke-width="1.5" marker-end="url(#c1ar)"/>')
    body.append(f'<path d="M{mid + 20} {base - n * sh + 20} L{W - 40} {base - 10}" stroke="#dc2626" stroke-width="1.5" marker-end="url(#c1ar)"/>')
    body.append(f'<text x="{mid / 2 + 10}" y="{H - 8}" text-anchor="middle" font-size="14" fill="#1e3a8a">{escape(up)}</text>')
    body.append(f'<text x="{mid + (W - mid) / 2}" y="{H - 8}" text-anchor="middle" font-size="14" fill="#1e3a8a">{escape(down)}</text>')
    defs = '<defs><marker id="c1ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#dc2626"/></marker></defs>'
    return _svg(W, H, [defs] + body, f'Staircase: {up} {a} to {b}; {down} {b} to {a}')


OPS.add('stairs')


def tenrows(spec):
    """'11-20' -> one row per number: bundles of ten pencils, loose pencils, then Tens | Ones | Number columns."""
    a, b = (int(x) for x in spec.split()[0].split('-'))
    defs = {'b': f'<g id="c1i-bundle-d">{_icon("bundle")}</g>', 'p': f'<g id="c1i-pencilv-sky">{_icon("pencilv", "sky")}</g>'}
    rows = list(range(a, b + 1))
    maxt = max(n // 10 for n in rows)
    pic_w = 20 + maxt * 40 + 9 * 18 + 20
    W, rh = pic_w + 3 * 70 + 10, 46
    body = [f'<rect x="4" y="4" width="{W - 8}" height="{rh * (len(rows) + 1)}" fill="#fff" stroke="#fb923c"/>']
    for k, lab in enumerate(['Tens', 'Ones', 'Number']):
        body.append(f'<text x="{pic_w + 35 + k * 70}" y="32" text-anchor="middle" font-size="15" font-weight="700">{lab}</text>')
    for i, n in enumerate(rows):
        y = 4 + rh * (i + 1)
        body.append(f'<path d="M4 {y} H{W - 4}" stroke="#fb923c"/>')
        x = 26
        for _ in range(n // 10):
            body.append(f'<use href="#c1i-bundle-d" transform="translate({x} {y + rh / 2})"/>')
            x += 40
        x += 6
        for _ in range(n % 10):
            body.append(f'<use href="#c1i-pencilv-sky" transform="translate({x} {y + rh / 2 + 2}) scale(0.8)"/>')
            x += 18
        for k, v in enumerate([n // 10, n % 10, n]):
            body.append(f'<text x="{pic_w + 35 + k * 70}" y="{y + 30}" text-anchor="middle" font-size="18">{v}</text>')
    for k in range(3):
        body.append(f'<path d="M{pic_w + k * 70} 4 V{4 + rh * (len(rows) + 1)}" stroke="#fb923c"/>')
    return _svg(W, rh * (len(rows) + 1) + 8, ['<defs>' + ''.join(defs.values()) + '</defs>'] + body,
                f'Numbers {a} to {b} shown with bundles of ten pencils and loose pencils, with tens, ones and the number')


OPS.add('tenrows')


def boxgrid(spec):
    """'6 | 0,_,_,3,...' -> number boxes in rows of 6 ('_' = blank box to fill); a short last row is centred."""
    c, vals = spec.split('|', 1)
    c = int(c)
    vals = [v.strip() for v in vals.split(',')]
    rows = [vals[i:i + c] for i in range(0, len(vals), c)]
    W = 16 + 48 * c
    body = []
    for r, row in enumerate(rows):
        off = (c - len(row)) * 24
        for k, v in enumerate(row):
            body.append(_card(8 + off + k * 48, 6 + r * 50, v))
    return _svg(W, 12 + 50 * len(rows), body, 'Number boxes: ' + ', '.join(v if v != '_' else 'blank' for v in vals))


OPS.add('boxgrid')


def dots(spec):
    """Dot-to-dot picture. 'W H | x,y x,y ... | extra svg-path d (optional, drawn faintly)' -> numbered dots 1..n."""
    parts = [p.strip() for p in spec.split('|')]
    W, H = (float(v) for v in parts[0].split())
    pts = [tuple(float(v) for v in p.split(',')) for p in parts[1].split()]
    body = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="#fff" stroke="#ec4899"/>']
    if len(parts) > 2 and parts[2]:
        body.append(f'<path d="{parts[2]}" fill="none" stroke="#334155" stroke-width="2"/>')
    for i, (x, y) in enumerate(pts, 1):
        body.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#111"/><text x="{x + 5}" y="{y - 5}" font-size="10" fill="#334155">{i}</text>')
    return _svg(W, H, body, f'Dot-to-dot picture with dots numbered 1 to {len(pts)}')


OPS.add('dots')


ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']


def ordsuf(n):
    return f'{n}' + ('st' if n == 1 else 'nd' if n == 2 else 'rd' if n == 3 else 'th')


def ordrow(spec):
    """'ICON N [rtl] [| label,label,...]' -> N objects in a line, each with a label ('_' = blank bubble to fill).
    Default labels: '1st first', '2nd second', ... counted from the left (or from the right with rtl)."""
    head, _, labs = spec.partition('|')
    a = head.split()
    name, n = a[0], int(a[1])
    rtl = 'rtl' in a[2:]
    labels = [x.strip() for x in labs.split(',')] if labs.strip() else None
    step = 74
    W = 20 + n * step
    body, defs = [], f'<defs><g id="c1i-{name}-d">{_icon(name)}</g></defs>'
    for i in range(n):
        x = 10 + i * step + step / 2
        k = (n - i) if rtl else (i + 1)
        lab = labels[i] if labels else f'{ordsuf(k)} {ORD[k - 1]}'
        body.append(f'<use href="#c1i-{name}-d" transform="translate({x} 40) scale(1.25)"/>')
        body.append(f'<rect x="{x - 33}" y="72" width="66" height="34" rx="14" fill="#fff" stroke="#ec4899"/>')
        if lab != '_':
            t1, _, t2 = lab.partition(' ')
            if t1 != '_':
                body.append(f'<text x="{x}" y="{88 if t2 else 94}" text-anchor="middle" font-size="13" font-weight="700" fill="#1e3a8a">{escape(t1)}</text>')
            if t2:
                body.append(f'<text x="{x}" y="102" text-anchor="middle" font-size="11" fill="#334155">{escape(t2)}</text>')
    if rtl:
        body.append(f'<path d="M{W - 20} 118 H{W - 120}" stroke="#ec4899" stroke-width="2" marker-end="url(#c1ar2)"/>'
                    '<defs><marker id="c1ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#ec4899"/></marker></defs>')
    return _svg(W, 126, [defs] + body, f'{n} {name}s in a row with ordinal positions' + (' counted from the right' if rtl else ''))


OPS.add('ordrow')


def hops(spec):
    """'13,14,_,16 | 1' -> number boxes joined by curved hops below, each hop labelled in a circle
    ('_' term = empty box; step '_' = empty circle; step may start with - for backward hops)."""
    terms, _, step = spec.partition('|')
    terms = [t.strip() for t in terms.split(',')]
    step = step.strip() or '1'
    gap = 74
    W = 20 + gap * len(terms)
    body = ['<defs><marker id="c1hp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#e11d48"/></marker></defs>']
    back = step.startswith('-')
    lab = step.lstrip('-+')
    for i, t in enumerate(terms):
        x = 10 + i * gap + gap / 2
        body.append(f'<rect x="{x - 24}" y="8" width="48" height="30" rx="4" fill="{"#fde68a" if t != "_" else "#fff"}" stroke="#f59e0b"/>')
        if t != '_':
            body.append(f'<text x="{x}" y="29" text-anchor="middle" font-size="17" font-weight="600">{escape(t)}</text>')
        if i:
            px = x - gap
            a, b = (x - 6, px + 6) if back else (px + 6, x - 6)
            body.append(f'<path d="M{a} 42 Q{(px + x) / 2} 88 {b} 42" fill="none" stroke="#e11d48" stroke-width="1.6" marker-end="url(#c1hp)"/>')
            body.append(f'<circle cx="{(px + x) / 2}" cy="66" r="12" fill="#fbcfe8" stroke="#e11d48" stroke-width="0.8"/>')
            if lab != '_':
                body.append(f'<text x="{(px + x) / 2}" y="71" text-anchor="middle" font-size="14">{escape(lab)}</text>')
    return _svg(W, 84, body, ('Backward' if back else 'Forward') + ' hops: ' + ', '.join(t if t != '_' else 'blank' for t in terms))


OPS.add('hops')


def _longobj(kind, L, col, y):
    """Horizontal object of length L starting at x=10, centred on y."""
    c = _col(col, {'crayon': '#2563eb', 'pencil': '#f59e0b', 'ruler': '#f472b6', 'rope': '#a16207', 'ribbon': '#ec4899',
                   'stick': '#d97706', 'snake': '#a16207', 'train': '#ef4444', 'worm': '#65a30d'}.get(kind, '#64748b'))
    x0 = 10
    if kind == 'crayon':
        return (f'<rect x="{x0}" y="{y - 8}" width="{L - 16}" height="16" rx="4" fill="{c}" stroke="{K}"/>'
                f'<path d="M{x0 + L - 16} {y - 8} L{x0 + L} {y} L{x0 + L - 16} {y + 8}z" fill="{c}" stroke="{K}"/>'
                f'<rect x="{x0 + 14}" y="{y - 3}" width="{(L - 16) * 0.5:.0f}" height="6" fill="#bfdbfe"/>')
    if kind == 'pencil':
        return (f'<rect x="{x0}" y="{y - 6}" width="10" height="12" fill="#f472b6" stroke="{K}"/>'
                f'<rect x="{x0 + 10}" y="{y - 6}" width="{L - 30}" height="12" fill="{c}" stroke="{K}"/>'
                f'<path d="M{x0 + L - 20} {y - 6} L{x0 + L} {y} L{x0 + L - 20} {y + 6}z" fill="#fde68a" stroke="{K}"/>'
                f'<path d="M{x0 + L - 5} {y - 1.5} L{x0 + L} {y} L{x0 + L - 5} {y + 1.5}z" fill="#111"/>')
    if kind == 'ruler':
        ticks = ''.join(f'<path d="M{x0 + 6 + i * 6} {y - 13} v{6 if i % 5 else 10}" stroke="{K}" stroke-width="0.8"/>' for i in range(int((L - 12) / 6) + 1))
        return f'<rect x="{x0}" y="{y - 13}" width="{L}" height="26" rx="2" fill="{c}" stroke="{K}"/>' + ticks
    # generic band (rope, ribbon, stick, snake, worm, train)
    return f'<rect x="{x0}" y="{y - 7}" width="{L}" height="14" rx="7" fill="{c}" stroke="{K}"/>'


def lengths(spec):
    """Stacked horizontal objects to compare lengths. 'crayon:150 | pencil:270:#f59e0b | ruler:360 ;; Long,Longer,Longest'
    (rows separated by '|'; optional labels after ';;'); left ends are lined up."""
    rows_s, _, labs = spec.partition(';;')
    rows = [r.strip().split(':') for r in rows_s.split('|')]
    labels = [l.strip() for l in labs.split(',')] if labs.strip() else []
    W = max(int(r[1]) for r in rows) + 140
    body, y = [], 24
    for i, r in enumerate(rows):
        kind, L = r[0], int(r[1])
        col = r[2] if len(r) > 2 else None
        body.append(_longobj(kind, L, col, y))
        if i < len(labels) and labels[i]:
            body.append(f'<text x="{L + 24}" y="{y + 5}" font-size="16">{escape(labels[i])}</text>')
        y += 40
    body.insert(0, f'<path d="M10 4 V{y - 16}" stroke="#94a3b8" stroke-dasharray="3 3"/>')
    return _svg(W, y - 8, body, 'Objects lined up at the left to compare lengths: ' + ', '.join(f'{r[0]} {labels[i] if i < len(labels) else ""}'.strip() for i, r in enumerate(rows)))


def sizes(spec):
    """Objects of different sizes standing on one base line. 'tree:0.8 tree:1.6 tree:2.4 ;; Tall,Taller,Tallest'
    (NAME[.colour]:scale; optional labels after ';;')."""
    items_s, _, labs = spec.partition(';;')
    items = items_s.split()
    labels = [l.strip() for l in labs.split(',')] if labs.strip() else []
    scales = [float(t.split(':')[1]) for t in items]
    H = 40 * max(scales) + 50
    base = H - 30
    body, x, defs = [], 10, {}
    for i, t in enumerate(items):
        nm, sc = t.split(':')
        sc = float(sc)
        name, _, col = nm.partition('.')
        w = 44 * sc
        cx = x + max(w, 80) / 2
        iid = f'c1i-{name}-{(col or "d").lstrip("#")}'
        defs.setdefault(iid, f'<g id="{iid}">{_icon(name, col or None)}</g>')
        body.append(f'<use href="#{iid}" transform="translate({cx:.1f} {base - 19 * sc:.1f}) scale({sc})"/>')
        if i < len(labels):
            body.append(f'<text x="{cx:.1f}" y="{H - 8}" text-anchor="middle" font-size="15">{escape(labels[i])}</text>')
        x += max(w, 80) + 20
    body.insert(0, f'<path d="M4 {base} H{x}" stroke="#94a3b8"/>')
    return _svg(x + 4, H, ['<defs>' + ''.join(defs.values()) + '</defs>'] + body,
                'Objects of different sizes: ' + ', '.join(f'{t.split(":")[0]} {labels[i] if i < len(labels) else ""}'.strip() for i, t in enumerate(items)))


OPS.update({'lengths', 'sizes'})


def pattern(spec):
    """Row of shapes. Tokens 'SHAPE[.colour][@size]' with SHAPE in tri, sq, circ, rect, rectv, '_' (blank line to fill);
    colour 'none' = outline only; size 0.6-1.6 (default 1). Example: 'tri.orange@1.3 sq.orange tri.orange _ _'."""
    toks = spec.split()
    body, x = [], 8
    H = 90
    base = 70
    labels = []
    for t in toks:
        if t == '_':
            body.append(f'<path d="M{x + 6} {base} H{x + 50}" stroke="#334155" stroke-width="2"/>')
            x += 60
            labels.append('blank')
            continue
        name, _, sz = t.partition('@')
        name, _, col = name.partition('.')
        s = float(sz) if sz else 1.0
        fill = 'none' if col == 'none' else _col(col or None, '#f59e0b')
        w = 40 * s
        stroke = f'stroke="#334155" stroke-width="{1.6 if fill == "none" else 0.6}"'
        if name == 'tri':
            body.append(f'<path d="M{x + w / 2:.1f} {base - w:.1f} L{x + w:.1f} {base} L{x} {base}z" fill="{fill}" {stroke}/>')
        elif name == 'trir':
            body.append(f'<path d="M{x} {base - w:.1f} L{x + w:.1f} {base - w / 2:.1f} L{x} {base}z" fill="{fill}" {stroke}/>')
        elif name == 'sq':
            body.append(f'<rect x="{x}" y="{base - w:.1f}" width="{w:.1f}" height="{w:.1f}" fill="{fill}" {stroke}/>')
        elif name == 'circ':
            body.append(f'<circle cx="{x + w / 2:.1f}" cy="{base - w / 2:.1f}" r="{w / 2:.1f}" fill="{fill}" {stroke}/>')
        elif name == 'rectv':
            body.append(f'<rect x="{x}" y="{base - w * 1.6:.1f}" width="{w * 0.7:.1f}" height="{w * 1.6:.1f}" fill="{fill}" {stroke}/>')
            w = w * 0.7
        else:
            raise ValueError('pattern shape ' + name)
        labels.append(f'{"outline " if fill == "none" else (col + " " if col else "")}{ {"tri": "triangle", "trir": "triangle", "sq": "square", "circ": "circle", "rectv": "rectangle"}[name] }' + (' (big)' if s > 1.15 else ' (small)' if s < 0.85 else ''))
        x += w + 10
    return _svg(x + 6, H, body, 'Pattern: ' + ', '.join(labels))


OPS.add('pattern')


def scene(spec):
    """Free picture from parts. 'W H ; item ; item ...' items:
       ICON[.colour]@x,y[,scale]   icon centred at x,y
       box x y w h [fill] [stroke]  rectangle (fill 'none' allowed)
       open x y w h [fill]          open box (no top), e.g. a carton or jar
       line x1 y1 x2 y2 [colour] [width]
       text x y TEXT                 label (use _ for spaces)
       label "TEXT" x y             same as text
    """
    parts = [p.strip() for p in spec.split(';') if p.strip()]
    W, H = (float(v) for v in parts[0].split())
    body, defs, labels = [], {}, []
    for it in parts[1:]:
        a = it.split()
        op = a[0]
        if op == 'box':
            x, y, w, h = a[1:5]
            fill = a[5] if len(a) > 5 else 'none'
            st = a[6] if len(a) > 6 else K
            body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{_col(fill, fill)}" stroke="{_col(st, st)}" stroke-width="2"/>')
        elif op == 'open':
            x, y, w, h = (float(v) for v in a[1:5])
            fill = _col(a[5], a[5]) if len(a) > 5 else '#d6b98c'
            body.append(f'<path d="M{x} {y} V{y + h} H{x + w} V{y}" fill="{fill}" stroke="{K}" stroke-width="2"/>')
        elif op == 'line':
            x1, y1, x2, y2 = a[1:5]
            c = _col(a[5], a[5]) if len(a) > 5 else K
            wd = a[6] if len(a) > 6 else '2'
            body.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{c}" stroke-width="{wd}" fill="none"/>')
        elif op in ('text', 'label'):
            x, y = a[1], a[2]
            t = ' '.join(a[3:]).replace('_', ' ').strip('"')
            body.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="14" fill="#1e3a8a">{escape(t)}</text>')
            labels.append(t)
        else:
            nm, _, pos = op.partition('@')
            name, _, col = nm.partition('.')
            v = [float(z) for z in pos.split(',')]
            sc = v[2] if len(v) > 2 else 1
            iid = f'c1i-{name}-{(col or "d").lstrip("#")}'
            defs.setdefault(iid, f'<g id="{iid}">{_icon(name, col or None)}</g>')
            body.append(f'<use href="#{iid}" transform="translate({v[0]} {v[1]}) scale({sc})"/>')
            labels.append(name)
    return _svg(W, H, ['<defs>' + ''.join(defs.values()) + '</defs>'] + body, 'Picture: ' + ', '.join(labels))


OPS.add('scene')


def _guides(W, y0, h=44):
    """Four-line handwriting guide starting at y0."""
    ys = [y0, y0 + h / 3, y0 + 2 * h / 3, y0 + h]
    return ''.join(f'<path d="M6 {y:.1f} H{W - 6}" stroke="{"#f87171" if i == 2 else "#94a3b8"}" stroke-width="{1 if i == 2 else 0.8}"/>' for i, y in enumerate(ys))


def trace(spec):
    """Tracing rows on handwriting guides. Rows separated by '|', each 'KIND N' with KIND in
    hline, hline2, vline, back (down-right), fwd (down-left), zigzag, u, circle, wave, n (hump). Dashed strokes, red start dot."""
    rows = [r.split() for r in spec.split('|')]
    W, rh = 560, 64
    body = [f'<rect x="0" y="0" width="{W}" height="{rh * len(rows) + 8}" rx="8" fill="#fefce8"/>']
    dash = 'stroke="#334155" stroke-width="2" stroke-dasharray="4 4" fill="none" stroke-linecap="round"'
    for r, row in enumerate(rows):
        kind, n = row[0], int(row[1])
        y0 = 10 + r * rh
        body.append(_guides(W, y0))
        top, bot = y0, y0 + 44
        step = (W - 40) / n
        for i in range(n):
            x = 22 + i * step
            dot = None
            if kind == 'hline':
                d, dot = f'M{x} {y0 + 22} h{step * 0.6:.1f}', (x, y0 + 22)
            elif kind == 'vline':
                d, dot = f'M{x + 10} {top} V{bot}', (x + 10, top)
            elif kind == 'back':
                d, dot = f'M{x} {top} L{x + 22} {bot}', (x, top)
            elif kind == 'fwd':
                d, dot = f'M{x + 22} {top} L{x} {bot}', (x + 22, top)
            elif kind == 'zigzag':
                d = f'M{x} {top} L{x + step / 2:.1f} {bot} L{x + step:.1f} {top}'
                dot = (x, top) if i == 0 else None
            elif kind == 'u':
                d, dot = f'M{x} {top} V{bot - 12} a11 11 0 0 0 22 0 V{top}', (x, top)
            elif kind == 'n':
                d, dot = f'M{x} {bot} V{top + 12} a11 11 0 0 1 22 0 V{bot}', (x, bot)
            elif kind == 'circle':
                d, dot = f'M{x} {y0 + 22} a20 20 0 1 0 40 0 a20 20 0 1 0 -40 0', (x, y0 + 22)
            elif kind == 'wave':
                d = f'M{x} {y0 + 22} q{step / 4:.1f} -22 {step / 2:.1f} 0 t{step / 2:.1f} 0'
                dot = (x, y0 + 22) if i == 0 else None
            elif kind == 'hline2':
                d, dot = f'M{x} {y0 + 14} h{step * 0.6:.1f} M{x} {y0 + 30} h{step * 0.6:.1f}', (x, y0 + 14)
            else:
                raise ValueError('trace kind ' + kind)
            body.append(f'<path d="{d}" {dash}/>')
            if dot:
                body.append(f'<circle cx="{dot[0]:.1f}" cy="{dot[1]:.1f}" r="4" fill="#dc2626"/>')
    return _svg(W, rh * len(rows) + 8, body, 'Tracing practice: ' + ', '.join(f'{r[1]} {r[0]}' for r in rows))


def tletters(spec):
    """Dotted letters/words to trace on handwriting guides, rows separated by '|': 'Aa Bb Cc | Dd Ee'.
    A token ending in '!' is drawn solid (model), others dotted; '_' = empty space to write."""
    rows = [r.split() for r in spec.split('|')]
    W, rh = 560, 70
    body = [f'<rect x="0" y="0" width="{W}" height="{rh * len(rows) + 8}" rx="8" fill="#fefce8"/>']
    for r, row in enumerate(rows):
        y0 = 14 + r * rh
        body.append(_guides(W, y0))
        step = (W - 20) / max(len(row), 1)
        for i, t in enumerate(row):
            x = 10 + i * step + step / 2
            if t == '_':
                continue
            solid = t.endswith('!')
            t = t.rstrip('!')
            style = 'fill="#1e3a8a"' if solid else 'fill="none" stroke="#475569" stroke-width="1.3" stroke-dasharray="2.5 2.5"'
            body.append(f'<text x="{x:.1f}" y="{y0 + 44}" text-anchor="middle" font-size="44" font-family="Comic Sans MS, Segoe Print, Segoe UI, sans-serif" {style}>{escape(t)}</text>')
    return _svg(W, rh * len(rows) + 8, body, 'Letters to trace: ' + ' '.join(t.rstrip('!') for row in rows for t in row if t != '_'))


OPS.update({'trace', 'tletters'})


def tline(spec):
    """Sentences to trace, one per guide line, separated by '|'. A line starting with '!' is solid (model)."""
    lines = [l.strip() for l in spec.split('|')]
    W, rh = 560, 62
    body = [f'<rect x="0" y="0" width="{W}" height="{rh * len(lines) + 8}" rx="8" fill="#fefce8"/>']
    for r, t in enumerate(lines):
        y0 = 12 + r * rh
        body.append(_guides(W, y0, 40))
        solid = t.startswith('!')
        t = t.lstrip('!')
        style = 'fill="#1e3a8a"' if solid else 'fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="2 2"'
        body.append(f'<text x="14" y="{y0 + 30}" font-size="34" font-family="Comic Sans MS, Segoe Print, Segoe UI, sans-serif" {style}>{escape(t)}</text>')
    return _svg(W, rh * len(lines) + 8, body, 'Sentences to trace: ' + ' / '.join(l.lstrip('!') for l in lines))


OPS.add('tline')


AR_FONT = "'Amiri','Scheherazade New','Noto Naskh Arabic','Traditional Arabic','Segoe UI',serif"


NONJOIN = set('اأإآدذرزوؤءة')


def _broken(word):
    """Split an Arabic word into its separate letters with joining tatweels: 'خَلَقَ' -> 'خَـ_ـلَـ_ـقَ'."""
    groups = []
    for ch in word:
        if groups and ('ً' <= ch <= 'ٟ' or ch in 'ٰـ'):
            groups[-1] += ch
        else:
            groups.append(ch)
    out = []
    for i, g in enumerate(groups):
        pre = 'ـ' if i and groups[i - 1][0] not in NONJOIN else ''
        post = 'ـ' if i < len(groups) - 1 and g[0] not in NONJOIN else ''
        out.append(pre + g + post)
    return '_'.join(out)


def arl(spec):
    """Arabic letter/word grid, right to left: 'COLS [c] [s=56] [w=1.6] | b~با t~تا ; d ; ...'.
    Rows split by ';', cells by spaces. Cell 'X~name' adds a small name under X ('_' = space, in X too);
    'X^Y^Z' stacks bubbles (full form over short forms); '!X' shades a cell; '.' leaves a gap;
    '*WORD' shows WORD broken into letters above it; 'c' centres short rows (default: right-aligned like the book). 'w=' widens cells for words."""
    head, _, rest = spec.partition('|')
    opts = head.split()
    cols = int(opts[0])
    centre = 'c' in opts
    size = next((int(o[2:]) for o in opts if o.startswith('s=')), 56)
    wf = next((float(o[2:]) for o in opts if o.startswith('w=')), 1.0)
    rows = [r.split() for r in rest.split(';')]
    cw, gap = size * wf, 10
    W = cols * (cw + gap) + gap
    body, y, seen = [], gap, []
    for row in rows:
        cells = [c for c in row]
        rh = 0
        off = (cols - len(cells)) * (cw + gap) / 2 if centre else 0
        for i, tok in enumerate(cells):
            if tok == '.':
                continue
            x = W - gap - (i + 1) * (cw + gap) + gap - off
            shade = tok.startswith('!')
            tok = tok.lstrip('!')
            main, _, name = tok.partition('~')
            if main.startswith('*'):
                main = main[1:]
                main = _broken(main) + '^' + main
            parts = main.split('^')
            bh = size * 0.92
            for k, p in enumerate(parts):
                by = y + k * (bh + 4)
                fill = '#fde2ea' if shade else '#fff'
                body.append(f'<rect x="{x:.1f}" y="{by:.1f}" width="{cw:.1f}" height="{bh:.1f}" rx="{size * 0.3:.1f}" fill="{fill}" stroke="#e11d74" stroke-width="2"/>')
                body.append(f'<text x="{x + cw / 2:.1f}" y="{by + bh * 0.68:.1f}" text-anchor="middle" direction="rtl" font-size="{size * 0.52:.1f}" font-family="{AR_FONT}" fill="{'#be185d' if k == 0 and len(parts) == 2 and wf > 1.2 else '#111'}">{escape(p.replace("_", " "))}</text>')
                seen.append(p.replace("_", " "))
            h = len(parts) * (bh + 4)
            if name:
                body.append(f'<text x="{x + cw / 2:.1f}" y="{y + h + 14:.1f}" text-anchor="middle" direction="rtl" font-size="{max(12, size * 0.26):.1f}" font-family="{AR_FONT}" fill="#9d174d">{escape(name.replace("_", " "))}</text>')
                h += 20
            rh = max(rh, h)
        y += rh + gap
    return _svg(W, y, body, 'Arabic letters: ' + ' '.join(seen))


OPS.add('arl')
