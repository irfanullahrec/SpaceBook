"""Class 2 picture scenes (English and other books): coded SVG redrawings of textbook illustrations.

scene spec:  'W H BG ; item ; item ...'
  BG     meadow | park | road | zebra | room | class | river | snow | field | plain | sky
  item   NAME[.colour][:pose]@x,y[,scale][,f]     f = mirror left-right
         NAME is a person (boy girl man woman grandpa teacher), one of the extra icons below,
         or any Class 1 icon (class-1/tools/figs1.py _icon; reused read-only).
         person poses: stand wave point run dig sit cheer hold
  also   text x y WORDS (use _ for spaces)  |  bubble x y WORDS (speech bubble)  |  sign x y WORDS (board)
"""
import importlib.util
from html import escape
from pathlib import Path

K = '#334155'
SKIN = '#f2c094'
_p = Path(__file__).resolve().parents[2] / 'class-1' / 'tools' / 'figs1.py'
_s = importlib.util.spec_from_file_location('figs1_for_cls2_scene', _p)
F1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(F1)
COL = dict(F1.C)


def col(c, d):
    return COL.get(c, c) if c else d


# ------------------------------------------------------------------ people (feet at y=40, head at y=-38)
def person(kind, pose='stand', c=None):
    hair = {'boy': '#3f2a1d', 'girl': '#3f2a1d', 'man': '#1f2937', 'woman': '#3f2a1d', 'grandpa': '#e5e7eb', 'teacher': '#3f2a1d'}[kind]
    shirt = col(c, {'boy': '#2563eb', 'girl': '#ec4899', 'man': '#0f766e', 'woman': '#7c3aed', 'grandpa': '#f5f5f4', 'teacher': '#0891b2'}[kind])
    big = kind in ('man', 'woman', 'grandpa', 'teacher')
    k = 1.15 if big else 1.0
    o = []
    # legs
    if pose == 'run':
        o.append(f'<path d="M-3 18 L-14 38 M3 18 L12 30 L8 40" stroke="{K}" stroke-width="5" stroke-linecap="round" fill="none"/>')
    elif pose == 'sit':
        o.append(f'<path d="M-4 18 H14 V38 M4 18 H20 V38" stroke="{K}" stroke-width="5" stroke-linecap="round" fill="none"/>')
    else:
        o.append(f'<path d="M-5 18 V40 M5 18 V40" stroke="{K}" stroke-width="5" stroke-linecap="round"/>')
    # body
    if kind in ('girl', 'woman', 'teacher'):
        o.append(f'<path d="M-9 -24 H9 L15 22 H-15 Z" fill="{shirt}" stroke="{K}" stroke-width="1.5"/>')
    else:
        o.append(f'<rect x="-11" y="-24" width="22" height="44" rx="5" fill="{shirt}" stroke="{K}" stroke-width="1.5"/>')
    # arms
    arms = {'stand': 'M-11 -18 L-17 6 M11 -18 L17 6', 'wave': 'M-11 -18 L-17 6 M11 -18 L24 -40',
            'point': 'M-11 -18 L-17 6 M11 -18 L34 -26', 'run': 'M-11 -18 L-22 -2 M11 -18 L22 -30',
            'dig': 'M-11 -18 L8 4 M11 -18 L14 6', 'sit': 'M-11 -18 L-4 4 M11 -18 L18 2',
            'cheer': 'M-11 -18 L-24 -42 M11 -18 L24 -42', 'hold': 'M-11 -18 L4 -6 M11 -18 L12 -6'}[pose]
    o.append(f'<path d="{arms}" stroke="{SKIN}" stroke-width="5" stroke-linecap="round" fill="none"/>')
    # head
    o.append(f'<circle cy="-36" r="12" fill="{SKIN}" stroke="{K}" stroke-width="1.3"/>')
    if kind in ('girl', 'woman', 'teacher'):
        o.append(f'<path d="M-13 -36 Q-14 -52 0 -51 Q14 -52 13 -36 Q12 -46 0 -45 Q-12 -46 -13 -36 Z M-13 -36 Q-15 -22 -9 -18 L-11 -34 Z M13 -36 Q15 -22 9 -18 L11 -34 Z" fill="{hair}"/>')
        if kind in ('woman', 'teacher'):
            o.append(f'<path d="M-14 -38 Q0 -58 14 -38 L16 -14 Q0 -22 -16 -14 Z" fill="{col(None, "#f9a8d4" if kind == "woman" else "#fef3c7")}" fill-opacity=".85" stroke="{K}" stroke-width="1"/>')
    elif kind == 'grandpa':
        o.append(f'<path d="M-12 -40 Q0 -54 12 -40 Z" fill="#fff" stroke="{K}"/><path d="M-8 -30 Q0 -14 8 -30 Z" fill="#e5e7eb" stroke="{K}" stroke-width="1"/>')
    else:
        o.append(f'<path d="M-12 -38 Q-12 -50 0 -50 Q12 -50 12 -38 Q6 -44 0 -43 Q-6 -44 -12 -38 Z" fill="{hair}"/>')
        if kind == 'man':
            o.append(f'<path d="M-6 -29 Q0 -26 6 -29" stroke="{hair}" stroke-width="2.5" fill="none"/>')
    o.append(f'<circle cx="-4" cy="-37" r="1.6" fill="#111"/><circle cx="4" cy="-37" r="1.6" fill="#111"/><path d="M-4 -31 Q0 -28 4 -31" stroke="#9a3412" stroke-width="1.4" fill="none"/>')
    return f'<g transform="scale({k})">' + ''.join(o) + '</g>'


PEOPLE = {'boy', 'girl', 'man', 'woman', 'grandpa', 'teacher'}

# ------------------------------------------------------------------ extra icons (centred, ~36-40 px)
X = {
    'deer': '<ellipse cx="0" cy="2" rx="15" ry="8" fill="{c:#b45309}" stroke="K"/><path d="M-10 8 v12 M-4 8 v12 M6 8 v12 M11 8 v12" stroke="K" stroke-width="2.5"/><path d="M12 -2 L16 -14 L22 -12 L18 -2 Z" fill="{c:#b45309}" stroke="K"/><path d="M16 -14 l-3 -8 M16 -14 l2 -9 M18 -20 l4 -3" stroke="#78350f" stroke-width="1.6" fill="none"/><g fill="#fff"><circle cx="-6" cy="0" r="1.4"/><circle cx="2" cy="-2" r="1.4"/></g>',
    'monkey': '<circle cy="2" r="10" fill="{c:#92400e}" stroke="K"/><circle cy="-12" r="8" fill="{c:#92400e}" stroke="K"/><ellipse cy="-10" rx="5" ry="4" fill="#fcd9b6"/><circle cx="-9" cy="-13" r="3" fill="#fcd9b6" stroke="K"/><circle cx="9" cy="-13" r="3" fill="#fcd9b6" stroke="K"/><path d="M10 6 q12 4 8 -10" stroke="#92400e" stroke-width="2.5" fill="none"/><path d="M-6 10 v8 M6 10 v8" stroke="#92400e" stroke-width="3"/>',
    'hive': '<path d="M-14 16 Q-18 -2 -8 -14 Q0 -20 8 -14 Q18 -2 14 16 Z" fill="{c:#f59e0b}" stroke="K"/><path d="M-15 4 H15 M-13 -6 H13 M-14 12 H14" stroke="#b45309"/><ellipse cy="8" rx="4" ry="3" fill="#78350f"/>',
    'earth': '<circle r="17" fill="{c:#38bdf8}" stroke="K"/><path d="M-12 -8 q6 -6 10 0 q-2 6 4 8 q-4 8 -12 4 q-6 -4 -2 -12 Z M4 -14 q8 2 10 8 q-6 2 -10 -2 Z M2 8 q8 -2 10 4 q-4 6 -10 2 Z" fill="#22c55e" stroke="K" stroke-width="1"/>',
    'spade': '<path d="M0 -20 V8" stroke="#92400e" stroke-width="3"/><path d="M-6 -20 H6" stroke="#92400e" stroke-width="3"/><path d="M-7 8 H7 L5 20 Q0 24 -5 20 Z" fill="{c:#94a3b8}" stroke="K"/>',
    'sapling': '<path d="M0 18 V-4" stroke="#15803d" stroke-width="2.5"/><path d="M0 -4 q-12 -4 -12 -14 q10 0 12 10 Z M0 2 q12 -4 12 -14 q-10 0 -12 10 Z" fill="{c:#22c55e}" stroke="K"/><path d="M-10 18 H10" stroke="#92400e" stroke-width="3"/>',
    'minar': '<path d="M-14 22 H14 L10 10 H-10 Z" fill="#e5e7eb" stroke="K"/><path d="M-8 10 L-5 -18 H5 L8 10 Z" fill="{c:#f8fafc}" stroke="K"/><path d="M-7 0 H7 M-6 -10 H6" stroke="K"/><path d="M-5 -18 Q0 -30 5 -18 Z" fill="#e5e7eb" stroke="K"/><path d="M0 -28 V-34" stroke="K"/>',
    'crutch': '<path d="M-4 -18 H4 M0 -18 V18 M-3 -2 H3" stroke="{c:#64748b}" stroke-width="3" stroke-linecap="round"/>',
    'stop': '<path d="M0 6 V22" stroke="#64748b" stroke-width="3"/><polygon points="-7,-17 7,-17 17,-7 17,7 7,17 -7,17 -17,7 -17,-7" transform="translate(0 -10) scale(.8)" fill="#dc2626" stroke="K"/><text y="-7" text-anchor="middle" font-size="7" font-weight="700" fill="#fff">STOP</text>',
    'nosign': '<path d="M0 6 V22" stroke="#64748b" stroke-width="3"/><circle cy="-8" r="13" fill="#fff" stroke="#dc2626" stroke-width="3.5"/><path d="M-9 1 L9 -17" stroke="#dc2626" stroke-width="3"/><text y="-5" text-anchor="middle" font-size="8" font-weight="700" fill="#1e3a8a">{t:P}</text>',
    'trafficlight': '<path d="M0 10 V24" stroke="#475569" stroke-width="3"/><rect x="-7" y="-22" width="14" height="32" rx="3" fill="#1f2937"/><circle cy="-15" r="4" fill="#dc2626"/><circle cy="-6" r="4" fill="#facc15" fill-opacity=".4"/><circle cy="3" r="4" fill="#22c55e" fill-opacity=".4"/>',
    'dove': '<ellipse rx="13" ry="7" fill="{c:#f8fafc}" stroke="K"/><circle cx="11" cy="-5" r="5" fill="{c:#f8fafc}" stroke="K"/><path d="M15 -5 l5 1 l-5 2 Z" fill="#f59e0b"/><circle cx="12" cy="-6" r="1" fill="#111"/><path d="M-4 -4 q-6 -14 6 -12 q2 6 -6 12 Z" fill="#e2e8f0" stroke="K"/><path d="M-13 0 l-8 -4 v8 Z" fill="#e2e8f0" stroke="K"/>',
    'pigeon': '<ellipse rx="13" ry="8" fill="{c:#94a3b8}" stroke="K"/><circle cx="11" cy="-6" r="5.5" fill="#64748b" stroke="K"/><path d="M16 -6 l4 1 l-4 2 Z" fill="#1f2937"/><circle cx="12" cy="-7" r="1" fill="#f97316"/><path d="M-13 0 l-7 -3 v7 Z" fill="#64748b"/><path d="M-4 8 v6 M4 8 v6" stroke="#ef4444" stroke-width="2"/>',
    'parrot': '<ellipse cx="0" cy="2" rx="8" ry="13" fill="{c:#22c55e}" stroke="K"/><circle cy="-12" r="7" fill="{c:#22c55e}" stroke="K"/><path d="M5 -13 q7 0 4 7 q-2 -3 -5 -2 Z" fill="#dc2626" stroke="K"/><circle cx="2" cy="-14" r="1.3" fill="#111"/><path d="M0 14 l-4 12 M3 14 l2 12" stroke="#15803d" stroke-width="3"/>',
    'partridge': '<ellipse rx="14" ry="10" fill="{c:#a8a29e}" stroke="K"/><circle cx="12" cy="-8" r="6" fill="#a8a29e" stroke="K"/><path d="M17 -8 l4 1 l-4 2 Z" fill="#dc2626"/><path d="M8 -9 h8" stroke="#111" stroke-width="1.5"/><path d="M-8 -2 q4 4 0 8 M-2 -4 q4 4 0 8 M4 -2 q4 4 0 8" stroke="#57534e" fill="none"/><path d="M-3 10 v7 M3 10 v7" stroke="#dc2626" stroke-width="2"/>',
    'bustard': '<ellipse cy="2" rx="14" ry="9" fill="{c:#d6b98c}" stroke="K"/><path d="M10 -2 Q12 -18 14 -22" stroke="#e7e5e4" stroke-width="5" fill="none"/><circle cx="14" cy="-22" r="4" fill="#e7e5e4" stroke="K"/><path d="M18 -22 l4 1 l-4 1.5 Z" fill="#78716c"/><path d="M-6 -2 q4 4 0 8 M0 -4 q4 4 0 8" stroke="#78350f" fill="none"/><path d="M-3 11 v10 M3 11 v10" stroke="#78716c" stroke-width="2"/>',
    'snowman': '<circle cy="8" r="12" fill="#fff" stroke="K"/><circle cy="-10" r="8" fill="#fff" stroke="K"/><path d="M-1 -10 l7 2 l-7 1 Z" fill="#f97316"/><circle cx="-3" cy="-13" r="1.3" fill="#111"/><circle cx="3" cy="-13" r="1.3" fill="#111"/><rect x="-7" y="-24" width="14" height="6" fill="{c:#1f2937}"/><path d="M-10 -18 H10" stroke="{c:#1f2937}" stroke-width="2"/>',
    'cottage': '<rect x="-18" y="-4" width="36" height="22" fill="{c:#fde68a}" stroke="K"/><path d="M-22 -4 L0 -22 L22 -4 Z" fill="#b91c1c" stroke="K"/><rect x="-4" y="6" width="8" height="12" fill="#92400e"/><rect x="-14" y="2" width="7" height="7" fill="#bfdbfe" stroke="K"/><rect x="8" y="2" width="7" height="7" fill="#bfdbfe" stroke="K"/><rect x="8" y="-22" width="5" height="10" fill="#78350f"/>',
    'swing': '<path d="M-18 20 L-12 -20 H12 L18 20" stroke="#dc2626" stroke-width="3" fill="none"/><path d="M-5 -20 V8 M5 -20 V8" stroke="#64748b"/><rect x="-8" y="8" width="16" height="4" fill="{c:#f59e0b}" stroke="K"/>',
    'seesaw': '<path d="M-20 4 L20 -6" stroke="{c:#f59e0b}" stroke-width="5" stroke-linecap="round"/><path d="M-5 16 L0 0 L5 16 Z" fill="#dc2626" stroke="K"/>',
    'bin': '<path d="M-11 -10 H11 L8 18 H-8 Z" fill="{c:#16a34a}" stroke="K"/><rect x="-13" y="-15" width="26" height="5" fill="#15803d" stroke="K"/><text y="6" text-anchor="middle" font-size="5.5" font-weight="700" fill="#fff">USE ME</text>',
    'mouse': '<ellipse cy="4" rx="12" ry="7" fill="{c:#9ca3af}" stroke="K"/><circle cx="-6" cy="-4" r="4" fill="#f9a8d4" stroke="K"/><circle cx="2" cy="-4" r="4" fill="#f9a8d4" stroke="K"/><circle cx="10" cy="3" r="1.2" fill="#111"/><path d="M-12 6 q-10 2 -8 -8" stroke="#9ca3af" stroke-width="1.6" fill="none"/>',
    'fox': '<ellipse cy="4" rx="13" ry="7" fill="{c:#ea580c}" stroke="K"/><path d="M9 -2 L20 2 L9 8 Z" fill="#ea580c" stroke="K"/><path d="M10 -2 l2 -8 l4 6 Z" fill="#ea580c" stroke="K"/><path d="M-13 2 q-10 -10 -4 -14 q2 8 6 10 Z" fill="#ea580c" stroke="K"/><path d="M-8 10 v8 M8 10 v8" stroke="K" stroke-width="2"/>',
    'panda': '<circle cy="6" r="12" fill="#fff" stroke="K"/><circle cy="-10" r="9" fill="#fff" stroke="K"/><circle cx="-8" cy="-17" r="3.5" fill="#111"/><circle cx="8" cy="-17" r="3.5" fill="#111"/><ellipse cx="-3.5" cy="-10" rx="2.5" ry="3" fill="#111"/><ellipse cx="3.5" cy="-10" rx="2.5" ry="3" fill="#111"/><path d="M-12 4 h6 M6 4 h6" stroke="#111" stroke-width="4"/>',
    'kangaroo': '<ellipse cx="0" cy="4" rx="9" ry="13" fill="{c:#c2410c}" stroke="K"/><circle cx="3" cy="-13" r="6" fill="#c2410c" stroke="K"/><path d="M3 -18 l-1 -6 M6 -18 l2 -6" stroke="#c2410c" stroke-width="2.5"/><path d="M-6 14 q-14 6 -16 -4" stroke="#c2410c" stroke-width="3" fill="none"/><path d="M-2 16 h12" stroke="K" stroke-width="2.5"/>',
    'globe': '<circle cy="-4" r="13" fill="{c:#38bdf8}" stroke="K"/><path d="M-8 -10 q6 -4 8 2 q4 4 -2 8 Z M4 -12 q6 2 6 8" fill="#22c55e" stroke="K" stroke-width="1"/><path d="M0 9 V16 M-8 18 H8" stroke="K" stroke-width="2.5"/>',
    'desk': '<rect x="-18" y="-6" width="36" height="5" fill="{c:#b45309}" stroke="K"/><path d="M-15 -1 V16 M15 -1 V16" stroke="#78350f" stroke-width="3"/>',
    'rope': '<path d="M-14 -12 Q0 30 14 -12" stroke="{c:#dc2626}" stroke-width="2.5" fill="none"/><rect x="-17" y="-20" width="6" height="10" rx="2" fill="#facc15" stroke="K"/><rect x="11" y="-20" width="6" height="10" rx="2" fill="#facc15" stroke="K"/>',
    'compass': '<path d="M0 -16 L-10 16 M0 -16 L10 16" stroke="#64748b" stroke-width="2.5"/><circle cy="-16" r="3" fill="{c:#2563eb}" stroke="K"/><path d="M8 10 l4 -2 l2 6 Z" fill="#facc15" stroke="K"/>',
    'axe': '<path d="M-10 18 L8 -14" stroke="#92400e" stroke-width="3.5"/><path d="M2 -18 q14 -2 14 12 q-8 -2 -12 0 Z" fill="{c:#94a3b8}" stroke="K"/>',
    'hockey': '<path d="M6 -18 L-4 12 q-2 6 -10 4" stroke="{c:#92400e}" stroke-width="3.5" fill="none" stroke-linecap="round"/><circle cx="10" cy="14" r="3.5" fill="#fff" stroke="K"/>',
    'wicket': '<path d="M-6 -16 V16 M0 -16 V16 M6 -16 V16" stroke="{c:#f5d0a9}" stroke-width="3"/><path d="M-7 -17 H7" stroke="#b45309" stroke-width="2"/>',
    'goal': '<path d="M-20 16 V-12 H20 V16" stroke="#fff" stroke-width="3" fill="none"/><path d="M-16 -8 H16 M-16 0 H16 M-16 8 H16 M-12 -12 V16 M-4 -12 V16 M4 -12 V16 M12 -12 V16" stroke="#e5e7eb" stroke-width=".8"/>',
    'cricketbug': '<ellipse rx="12" ry="5" fill="{c:#1f2937}" stroke="K"/><circle cx="12" cy="-1" r="4" fill="#1f2937"/><path d="M14 -4 q8 -10 16 -8 M14 -3 q6 -12 12 -14" stroke="#1f2937" fill="none"/><path d="M-4 4 L-12 14 M2 4 L-2 14 M-8 -2 L-20 -10 L-16 12" stroke="#1f2937" stroke-width="1.8" fill="none"/>',
    'highlighter': '<g transform="rotate(-30)"><rect x="-4" y="-16" width="8" height="26" rx="2" fill="{c:#facc15}" stroke="K"/><path d="M-4 10 L0 18 L4 10 Z" fill="#fef08a" stroke="K"/></g>',
    'mug': '<rect x="-10" y="-12" width="18" height="24" rx="2" fill="{c:#1f2937}" stroke="K"/><path d="M8 -6 q8 0 8 6 q0 6 -8 6" stroke="{c:#1f2937}" stroke-width="3" fill="none"/>',
    'rose': '<path d="M0 0 V20" stroke="#15803d" stroke-width="2"/><path d="M0 12 q-8 -4 -10 2 q6 2 10 -2 Z" fill="#22c55e"/><circle cy="-6" r="9" fill="{c:#ec4899}" stroke="K"/><path d="M-4 -8 q4 -6 8 0 q-4 4 -8 0 M-6 -4 q6 4 12 0" stroke="#9d174d" fill="none"/>',
    'dome': '<rect x="-18" y="0" width="36" height="18" fill="{c:#d6d3d1}" stroke="K"/><path d="M-12 0 Q-12 -22 0 -22 Q12 -22 12 0 Z" fill="#e7e5e4" stroke="K"/><path d="M0 -22 V-30" stroke="K"/><path d="M-6 18 V8 Q0 2 6 8 V18" fill="#78716c"/>',
    'sack': '<path d="M-10 -14 Q-14 10 -10 18 H10 Q14 10 10 -14 Q0 -10 -10 -14 Z" fill="{c:#d6b98c}" stroke="K"/><path d="M-10 -14 q10 6 20 0" stroke="#92400e" fill="none"/>',
    'notebook': '<rect x="-14" y="-17" width="28" height="34" rx="2" fill="{c:#fff}" stroke="K"/><path d="M-9 -9 H10 M-9 -3 H10 M-9 3 H10 M-9 9 H10" stroke="#93c5fd"/><path d="M-14 -17 V17" stroke="#ef4444" stroke-width="2"/>',
    'card': '<rect x="-14" y="-18" width="28" height="36" rx="2" fill="{c:#fde68a}" stroke="K"/><path d="M0 -2 q-8 -8 -8 -2 q0 6 8 12 q8 -6 8 -12 q0 -6 -8 2 Z" fill="#ef4444"/>',
    'shelf': '<rect x="-16" y="-18" width="32" height="36" fill="{c:#b45309}" stroke="K"/><path d="M-16 -6 H16 M-16 6 H16" stroke="#78350f" stroke-width="2"/><rect x="-12" y="-16" width="5" height="9" fill="#3b82f6"/><rect x="-6" y="-15" width="5" height="8" fill="#ef4444"/><circle cx="8" cy="1" r="4" fill="#facc15"/>',
    'leafg': '<path d="M-14 10 Q-14 -14 14 -14 Q14 10 -14 10 Z" fill="{c:#22c55e}" stroke="K"/><path d="M-14 10 L10 -10" stroke="#15803d"/>',
    'buntingflag': '<path d="M-6 -6 H6 L0 6 Z" fill="{c:#f97316}" stroke="K"/>',
    'bubbleicon': '<rect x="-16" y="-12" width="32" height="20" rx="8" fill="#fff" stroke="K"/><path d="M-6 8 l-4 8 l10 -8" fill="#fff" stroke="K"/>',
    'pointhand': '<path d="M-14 -4 H8 q4 0 4 4 q0 4 -4 4 H-2 v6 H-14 Z" fill="#fcd9b6" stroke="K"/>',
    'clock': '<circle r="15" fill="{c:#fff}" stroke="K" stroke-width="2"/><path d="M0 0 V-10 M0 0 L7 3" stroke="K" stroke-width="2" stroke-linecap="round"/><g fill="K"><circle cy="-12" r="1"/><circle cx="12" r="1"/><circle cy="12" r="1"/><circle cx="-12" r="1"/></g>',
    'blackboard': '<rect x="-24" y="-15" width="48" height="30" fill="{c:#14532d}" stroke="#78350f" stroke-width="3"/><path d="M-16 -6 H6 M-16 2 H12" stroke="#f8fafc" stroke-width="1.4"/>',
    'pkflag': '<path d="M-16 22 V-20" stroke="#64748b" stroke-width="2.5"/><rect x="-16" y="-20" width="8" height="22" fill="#fff" stroke="K" stroke-width=".8"/><rect x="-8" y="-20" width="26" height="22" fill="#01411C" stroke="K" stroke-width=".8"/><circle cx="5" cy="-9" r="6" fill="#fff"/><circle cx="7.5" cy="-11" r="5" fill="#01411C"/><circle cx="10" cy="-13" r="1.6" fill="#fff"/>',
    'redhouse': '<rect x="-20" y="-6" width="40" height="26" fill="{c:#dc2626}" stroke="K"/><path d="M-24 -6 L0 -26 L24 -6 Z" fill="#7f1d1d" stroke="K"/><rect x="-5" y="6" width="10" height="14" fill="#fde68a"/><rect x="-16" y="0" width="8" height="8" fill="#bfdbfe" stroke="K"/><rect x="8" y="0" width="8" height="8" fill="#bfdbfe" stroke="K"/>',
    'hive2': '<path d="M-14 -20 H14" stroke="#78350f" stroke-width="3"/><path d="M0 -20 V-16" stroke="#78350f" stroke-width="2"/><path d="M-12 14 Q-16 -2 -8 -14 Q0 -18 8 -14 Q16 -2 12 14 Z" fill="{c:#f59e0b}" stroke="K"/><path d="M-13 2 H13 M-11 -7 H11" stroke="#b45309"/><ellipse cy="8" rx="4" ry="3" fill="#78350f"/>',
    'brokentree': '<path d="M-3 20 L-2 -4 L-10 -16 M-2 -4 L8 -18 M-1 4 L10 -4" stroke="{c:#57534e}" stroke-width="3" fill="none" stroke-linecap="round"/>',
    'smoke': '<path d="M-6 16 q-8 -8 0 -14 q-6 -10 4 -14 q-2 -8 8 -8" stroke="{c:#64748b}" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/>',
    'net': '<path d="M-14 18 L6 -6" stroke="#92400e" stroke-width="2.5"/><circle cx="10" cy="-10" r="10" fill="none" stroke="#475569" stroke-width="2"/><path d="M2 -16 L18 -4 M4 -2 L16 -18 M0 -10 H20" stroke="#94a3b8"/>',
    'doll2': '<circle cy="-10" r="7" fill="#fcd9b6" stroke="K"/><path d="M-7 -12 q7 -10 14 0" fill="#facc15"/><path d="M-9 16 L-4 -3 H4 L9 16 Z" fill="{c:#ec4899}" stroke="K"/>',
    'chartbox': '<rect x="-18" y="-14" width="36" height="28" rx="3" fill="{c:#fef9c3}" stroke="K"/><path d="M-12 -6 H12 M-12 0 H8 M-12 6 H10" stroke="#64748b"/>',
}


def xicon(name, c=None, t=''):
    s = X[name]
    import re
    s = re.sub(r'\{c:([^}]*)\}', lambda m: col(c, m.group(1)), s)
    s = re.sub(r'\{t:([^}]*)\}', lambda m: escape(t or m.group(1)), s)
    return s.replace('stroke="K"', f'stroke="{K}"').replace('fill="K"', f'fill="{K}"')


# ------------------------------------------------------------------ backgrounds
def background(bg, W, H):
    g = H * 0.62
    sky = f'<rect width="{W}" height="{H}" fill="#dbeafe"/>'
    grass = f'<rect y="{g:.0f}" width="{W}" height="{H - g:.0f}" fill="#86efac"/>'
    if bg in ('meadow', 'park', 'field'):
        out = sky + grass
        if bg == 'park':
            out += f'<path d="M{W * 0.35:.0f} {H} Q{W * 0.5:.0f} {g + 20:.0f} {W * 0.7:.0f} {g:.0f}" stroke="#e7d7b5" stroke-width="14" fill="none"/>'
        if bg == 'field':
            out = f'<rect width="{W}" height="{H}" fill="#4ade80"/><path d="M0 {H * 0.3:.0f} H{W} M{W / 2:.0f} 0 V{H}" stroke="#f0fdf4" stroke-width="2"/><circle cx="{W / 2:.0f}" cy="{H * 0.3:.0f}" r="26" fill="none" stroke="#f0fdf4" stroke-width="2"/>'
        return out
    if bg in ('road', 'zebra'):
        r0 = H * 0.66
        out = sky + f'<rect y="{g - 10:.0f}" width="{W}" height="{H - g + 10:.0f}" fill="#86efac"/><rect y="{r0:.0f}" width="{W}" height="{H * 0.24:.0f}" fill="#6b7280"/>'
        out += f'<path d="M0 {r0 + H * 0.12:.0f} H{W}" stroke="#f8fafc" stroke-width="2" stroke-dasharray="14 10"/>'
        if bg == 'zebra':
            x0 = W * 0.42
            out += ''.join(f'<rect x="{x0 + i * 13:.0f}" y="{r0:.0f}" width="7" height="{H * 0.24:.0f}" fill="#f8fafc"/>' for i in range(6))
        return out
    if bg in ('room', 'class'):
        out = f'<rect width="{W}" height="{H}" fill="{"#fef3c7" if bg == "room" else "#e0f2fe"}"/><rect y="{H * 0.7:.0f}" width="{W}" height="{H * 0.3:.0f}" fill="#d6b98c"/>'
        return out
    if bg == 'river':
        return sky + grass + f'<path d="M0 {H * 0.72:.0f} Q{W * 0.3:.0f} {H * 0.66:.0f} {W * 0.6:.0f} {H * 0.74:.0f} T{W} {H * 0.7:.0f} V{H * 0.92:.0f} Q{W * 0.6:.0f} {H * 0.98:.0f} {W * 0.3:.0f} {H * 0.9:.0f} T0 {H * 0.94:.0f} Z" fill="#60a5fa"/>'
    if bg == 'snow':
        return f'<rect width="{W}" height="{H}" fill="#e0f2fe"/><path d="M0 {g:.0f} Q{W / 2:.0f} {g - 20:.0f} {W} {g:.0f} V{H} H0 Z" fill="#f8fafc" stroke="#cbd5e1"/>'
    if bg == 'sky':
        return sky
    return f'<rect width="{W}" height="{H}" rx="8" fill="#fffdf7"/>'


def _hid(spec):
    import hashlib
    return hashlib.md5(spec.encode()).hexdigest()[:8]


def scene(spec):
    parts = [p.strip() for p in spec.split(';') if p.strip()]
    head = parts[0].split()
    W, H = float(head[0]), float(head[1])
    bg = head[2] if len(head) > 2 else 'plain'
    body = [background(bg, W, H)]
    labels = []
    for it in parts[1:]:
        a = it.split()
        op = a[0]
        if op in ('text', 'bubble', 'sign'):
            x, y = float(a[1]), float(a[2])
            t = ' '.join(a[3:]).replace('_', ' ')
            labels.append(t)
            if op == 'text':
                body.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="13" font-weight="600" fill="#1e3a8a">{escape(t)}</text>')
            else:
                w = 9 + 7.2 * len(t)
                fill, stroke = ('#fff', K) if op == 'bubble' else ('#1e3a8a', '#1e3a8a')
                body.append(f'<rect x="{x - w / 2:.0f}" y="{y - 13}" width="{w:.0f}" height="20" rx="{9 if op == "bubble" else 3}" fill="{fill}" stroke="{stroke}"/>'
                            + (f'<path d="M{x - 6} {y + 7} l-5 9 l12 -9" fill="#fff" stroke="{K}"/>' if op == 'bubble' else '')
                            + f'<text x="{x}" y="{y + 2}" text-anchor="middle" font-size="12" fill="{"#0f172a" if op == "bubble" else "#fff"}">{escape(t)}</text>')
            continue
        nm, _, pos = op.partition('@')
        nm, _, pose = nm.partition(':')
        name, _, c = nm.partition('.')
        v = pos.split(',')
        x, y = float(v[0]), float(v[1])
        sc = float(v[2]) if len(v) > 2 and v[2] not in ('f',) else 1.0
        flip = 'f' in v[2:]
        if name in PEOPLE:
            g = person(name, pose or 'stand', c or None)
            sc *= 0.65
        elif name in X:
            g = xicon(name, c or None, pose.replace('_', ' '))
        else:
            g = F1._icon(name, c or None)
        tr = f'translate({x} {y}) scale({-sc if flip else sc} {sc})'
        body.append(f'<g transform="{tr}">{g}</g>')
        labels.append(name)
    lab = ', '.join(dict.fromkeys(labels))
    return (f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" role="img" aria-label="Picture: {escape(lab)}" '
            f'font-family="Segoe UI, Arial, sans-serif"><clipPath id="sc{_hid(spec)}"><rect width="{W}" height="{H}" rx="10"/></clipPath>'
            f'<g clip-path="url(#sc{_hid(spec)})">' + ''.join(body) + '</g></svg>')
