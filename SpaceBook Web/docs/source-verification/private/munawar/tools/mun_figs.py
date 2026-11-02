"""SpaceBook's own coded (SVG) drawings of the objects a Munawar (Kanz) book page shows.

The Government books show their pictures as drawings made from code, not as scans; a Munawar page can show the same
way. These are NOT copies of the publisher's art: each object is drawn fresh from its name (a monitor, a mouse, a
sewing machine ...), so the page can show "what the picture is" in a form that scales, recolours and is searchable.
Every drawing carries a small "SpaceBook drawing" tag, so nobody takes it for the publisher's own picture; the
publisher's exact pages are in the separate "Original pages" view.

Page line (written in a page file like any other line; build_munawar.py turns it into an svg block):

  pic row  Bicycle=bicycle | Sewing machine=sewing | =tower           labelled objects in a row (empty name = no label)
           add [] after an item for an empty tick box under it:      Monitor=monitor[] | Mouse=mouse[]
           item options after a dot:  tower.black  monitor.win  (colour or screen)   scale: s=1.2 at the end
  pic kb   hl=ctrl,shift  lab=Control Keys@ctrl|Shift keys@shift     keyboard with key groups in pink and labels
           groups: letters numbers function arrows enter ctrl shift esc caps space   (no hl = plain keyboard)
  pic mouse  parts                                                    mouse with Left Button / Right Button / Scroll Wheel
             hl=left | hl=right | hl=wheel                            one button coloured
  pic desk                                                            monitor, system unit, keyboard and mouse together
"""
from html import escape
from pathlib import Path
import importlib.util
import re

K = '#334155'      # outline, same as the Government icons
PINK = '#db2777'   # names under pictures
HL = '#f472b6'     # a coloured key / button


def _figs1():
    p = Path(__file__).resolve().parents[3] / 'class-1' / 'tools' / 'figs1.py'
    spec = importlib.util.spec_from_file_location('mun_figs1', p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


F1 = _figs1()


def _svg(w, h, body, label, scale=1.0):
    if w < 100:   # keep room for the "SpaceBook drawing" tag under a narrow picture
        body = f'<g transform="translate({(100 - w) / 2:.1f} 0)">{body}</g>'
        w = 100
    h += 11
    return (f'<svg viewBox="0 0 {w:.0f} {h:.0f}" width="{w * scale:.0f}" role="img" aria-label="{escape(label)}" '
            f'font-family="Segoe UI, Arial, sans-serif" data-no-translate="1">{body}'
            f'<text x="{w - 4:.0f}" y="{h - 3:.0f}" text-anchor="end" font-size="8" fill="#94a3b8">SpaceBook drawing</text></svg>')


# ---- objects: each returns (width, height, svg body) in its own box, origin top left ----------------------------

def monitor(c=None, screen='blue'):
    bez = c or '#1f2937'
    scr = {'blue': '#93c5fd', 'dark': '#0f172a', 'win': '#38bdf8', 'fun': '#bbf7d0'}.get(screen, '#93c5fd')
    s = (f'<rect x="8" y="4" width="104" height="62" rx="5" fill="{bez}" stroke="{K}"/>'
         f'<rect x="14" y="10" width="92" height="50" rx="2" fill="{scr}"/>')
    if screen == 'win':
        s += '<g fill="#fff" opacity=".92"><rect x="46" y="20" width="13" height="13"/><rect x="61" y="20" width="13" height="13"/><rect x="46" y="35" width="13" height="13"/><rect x="61" y="35" width="13" height="13"/></g>'
    elif screen == 'fun':
        s += '<circle cx="90" cy="22" r="7" fill="#fde047"/><path d="M14 60 Q40 34 70 52 Q86 44 106 54 V60z" fill="#4ade80"/><rect x="32" y="30" width="3" height="18" fill="#92400e"/><circle cx="33" cy="28" r="9" fill="#16a34a"/>'
    elif screen == 'blue':
        s += '<path d="M14 10 L56 10 L14 46z" fill="#fff" opacity=".28"/>'
    s += (f'<path d="M52 66 h16 l3 12 h-22z" fill="#9ca3af" stroke="{K}"/>'
          f'<rect x="34" y="78" width="52" height="7" rx="3.5" fill="#6b7280" stroke="{K}"/>')
    return 120, 90, s


def tower(c=None):
    b = c or '#cbd5e1'
    return 60, 100, (f'<rect x="10" y="3" width="40" height="92" rx="4" fill="{b}" stroke="{K}"/>'
                     '<rect x="16" y="10" width="28" height="6" rx="1.5" fill="#475569"/>'
                     '<rect x="16" y="20" width="28" height="6" rx="1.5" fill="#475569"/>'
                     '<circle cx="22" cy="46" r="1.8" fill="#22c55e"/><circle cx="28" cy="46" r="1.8" fill="#f59e0b"/>'
                     f'<circle cx="30" cy="62" r="6" fill="#fff" stroke="{K}"/><path d="M30 57 v5" stroke="{K}" stroke-width="1.6"/>'
                     '<g stroke="#64748b" stroke-width="1.5"><path d="M17 76 h26 M17 80 h26 M17 84 h26"/></g>')


def mouse(c=None, hl=None, wire=True):
    b = c or '#1f2937'
    lc = HL if hl == 'left' else '#475569'
    rc = HL if hl == 'right' else '#475569'
    wc = HL if hl == 'wheel' else '#cbd5e1'
    s = ''
    if wire:
        s += f'<path d="M30 10 C30 2 36 -2 44 -2" stroke="{K}" stroke-width="2" fill="none"/>'
    s += (f'<path d="M30 8 C48 8 57 28 57 52 C57 74 46 88 30 88 C14 88 3 74 3 52 C3 28 12 8 30 8z" fill="{b}" stroke="{K}"/>'
          f'<path d="M30 9 C14 9 6 26 4 44 L30 44z" fill="{lc}"/><path d="M30 9 C46 9 54 26 56 44 L30 44z" fill="{rc}"/>'
          f'<path d="M4 44 H56 M30 9 V44" stroke="{K}" stroke-width="1.2" fill="none"/>'
          f'<rect x="26.5" y="16" width="7" height="17" rx="3.5" fill="{wc}" stroke="{K}"/>')
    return 60, 92, s


def laptop(c=None):
    b = c or '#1f2937'
    return 120, 80, (f'<rect x="18" y="6" width="84" height="52" rx="4" fill="{b}" stroke="{K}"/>'
                     '<rect x="23" y="11" width="74" height="42" rx="1.5" fill="#93c5fd"/>'
                     '<path d="M23 11 L58 11 L23 40z" fill="#fff" opacity=".28"/>'
                     f'<path d="M8 62 H112 L106 72 Q105 74 102 74 H18 Q15 74 14 72z" fill="#9ca3af" stroke="{K}"/>'
                     '<rect x="50" y="64" width="20" height="3" rx="1.5" fill="#6b7280"/>')


def printer(c=None):
    b = c or '#ef4444'
    return 110, 80, (f'<rect x="28" y="4" width="54" height="26" fill="#fff" stroke="{K}"/><path d="M34 12 h42 M34 18 h42 M34 24 h30" stroke="#cbd5e1" stroke-width="1.5"/>'
                     f'<rect x="6" y="28" width="98" height="34" rx="5" fill="{b}" stroke="{K}"/>'
                     f'<rect x="14" y="36" width="42" height="5" rx="2" fill="#1f2937"/><circle cx="88" cy="38" r="3" fill="#bbf7d0" stroke="{K}"/>'
                     f'<rect x="26" y="56" width="58" height="18" fill="#fff" stroke="{K}"/><path d="M32 63 h46 M32 68 h30" stroke="#cbd5e1" stroke-width="1.5"/>')


def speakers(c=None):
    b = c or '#1f2937'
    one = (f'<rect x="{{x}}" y="6" width="42" height="64" rx="5" fill="{b}" stroke="{K}"/>'
           f'<circle cx="{{cx}}" cy="26" r="7" fill="#e5e7eb" stroke="{K}"/><circle cx="{{cx}}" cy="52" r="12" fill="#e5e7eb" stroke="{K}"/>'
           f'<circle cx="{{cx}}" cy="52" r="5" fill="#475569"/>')
    return 110, 76, one.format(x=6, cx=27) + one.format(x=62, cx=83)


def cpu_chip():
    pins = ''.join(f'<path d="M{x} 6 v8 M{x} 56 v8" stroke="#94a3b8" stroke-width="2"/>' for x in range(18, 54, 7))
    pins += ''.join(f'<path d="M6 {y} h8 M56 {y} h8" stroke="#94a3b8" stroke-width="2"/>' for y in range(18, 54, 7))
    return 70, 70, (pins + f'<rect x="12" y="12" width="46" height="46" rx="4" fill="#d1d5db" stroke="{K}"/>'
                    f'<rect x="21" y="21" width="28" height="28" rx="2" fill="#94a3b8" stroke="{K}"/>'
                    '<text x="35" y="39" text-anchor="middle" font-size="10" font-weight="700" fill="#1f2937">CPU</text>')


def motherboard():
    chips = ''.join(f'<rect x="{x}" y="64" width="9" height="9" fill="#1f2937"/>' for x in (66, 80, 94))
    caps = ''.join(f'<circle cx="{x}" cy="14" r="3.2" fill="#38bdf8" stroke="{K}"/>' for x in (14, 24, 34, 44))
    slots = ''.join(f'<rect x="{x}" y="22" width="5" height="34" fill="#1f2937"/>' for x in (96, 104, 112))
    return 124, 92, (f'<rect x="3" y="3" width="118" height="86" rx="3" fill="#15803d" stroke="{K}"/>'
                     f'<rect x="20" y="30" width="30" height="30" fill="#e5e7eb" stroke="{K}"/><rect x="26" y="36" width="18" height="18" fill="#94a3b8"/>'
                     f'<rect x="14" y="68" width="40" height="7" fill="#fde047" stroke="{K}"/>' + chips + caps + slots +
                     '<rect x="8" y="22" width="9" height="30" fill="#cbd5e1" stroke="#334155"/>')


def power_supply():
    return 104, 74, (f'<rect x="4" y="6" width="80" height="62" rx="4" fill="#9ca3af" stroke="{K}"/>'
                     f'<circle cx="44" cy="37" r="22" fill="#e5e7eb" stroke="{K}"/><circle cx="44" cy="37" r="5" fill="#475569"/>'
                     f'<g stroke="#475569" stroke-width="3"><path d="M44 18 v38 M25 37 h38 M31 24 l26 26 M57 24 l-26 26"/></g>'
                     f'<path d="M84 22 H98 M84 36 H100 M84 50 H96" stroke="#dc2626" stroke-width="3"/>'
                     f'<path d="M84 29 H98 M84 43 H100" stroke="#1f2937" stroke-width="3"/>')


def ram_stick():
    chips = ''.join(f'<rect x="{x}" y="9" width="14" height="22" fill="#1f2937"/>' for x in (12, 30, 48, 66, 84))
    pins = ''.join(f'<rect x="{x}" y="38" width="3.4" height="6" fill="#eab308"/>' for x in range(8, 112, 5))
    return 120, 50, (f'<rect x="3" y="4" width="114" height="36" rx="2" fill="#16a34a" stroke="{K}"/>' + chips + pins)


def hard_disc():
    return 84, 92, (f'<rect x="4" y="4" width="76" height="84" rx="5" fill="#cbd5e1" stroke="{K}"/>'
                    f'<circle cx="40" cy="42" r="28" fill="#94a3b8" stroke="{K}"/><circle cx="40" cy="42" r="9" fill="#e5e7eb" stroke="{K}"/>'
                    f'<path d="M68 12 L46 38" stroke="#1f2937" stroke-width="3.5" stroke-linecap="round"/>'
                    f'<rect x="14" y="76" width="56" height="7" rx="2" fill="#eab308"/>')


def graphic_card():
    return 120, 66, (f'<rect x="3" y="8" width="112" height="44" rx="4" fill="#1f2937" stroke="{K}"/>'
                     f'<circle cx="34" cy="30" r="17" fill="#374151" stroke="#9ca3af"/><circle cx="34" cy="30" r="4" fill="#9ca3af"/>'
                     f'<g stroke="#9ca3af" stroke-width="3"><path d="M34 15 v30 M19 30 h30 M23 19 l22 22 M45 19 l-22 22"/></g>'
                     f'<circle cx="82" cy="30" r="17" fill="#374151" stroke="#9ca3af"/><circle cx="82" cy="30" r="4" fill="#9ca3af"/>'
                     f'<g stroke="#9ca3af" stroke-width="3"><path d="M82 15 v30 M67 30 h30 M71 19 l22 22 M93 19 l-22 22"/></g>'
                     f'<rect x="8" y="52" width="72" height="8" fill="#eab308"/><rect x="104" y="4" width="10" height="48" fill="#cbd5e1" stroke="{K}"/>')


def dvd_drive():
    return 124, 46, (f'<rect x="3" y="6" width="118" height="34" rx="3" fill="#e5e7eb" stroke="{K}"/>'
                     f'<rect x="12" y="14" width="76" height="8" rx="2" fill="#475569"/><rect x="96" y="14" width="16" height="6" rx="2" fill="#94a3b8" stroke="{K}"/>'
                     f'<circle cx="104" cy="30" r="2.5" fill="#22c55e"/><text x="14" y="34" font-size="6" fill="#475569">DVD</text>')


def dvd_disc():
    return 76, 76, (f'<circle cx="38" cy="38" r="34" fill="#e5e7eb" stroke="{K}"/><circle cx="38" cy="38" r="24" fill="#c4b5fd" opacity=".7"/>'
                    f'<path d="M38 4 A34 34 0 0 1 72 38 L38 38z" fill="#fde68a" opacity=".6"/><circle cx="38" cy="38" r="9" fill="#fff" stroke="{K}"/>'
                    f'<circle cx="38" cy="38" r="3" fill="#94a3b8"/>')


def keyboard_pic(c=None):
    """The small plain keyboard used inside a row."""
    body, w, h, _ = _kb(set(), c)
    return w, h, body


def sewing():
    return 124, 92, (f'<rect x="4" y="72" width="116" height="13" rx="3" fill="#94a3b8" stroke="{K}"/>'
                     f'<path d="M12 72 V30 Q12 14 30 14 H92 Q108 14 108 30 V42 H94 V72z" fill="#f9a8d4" stroke="{K}"/>'
                     f'<circle cx="26" cy="40" r="12" fill="#e5e7eb" stroke="{K}"/><circle cx="26" cy="40" r="3.5" fill="#94a3b8"/>'
                     f'<rect x="44" y="4" width="14" height="10" rx="2" fill="#fff" stroke="{K}"/><path d="M44 8 h14 M44 11 h14" stroke="#db2777" stroke-width="2"/>'
                     f'<rect x="94" y="42" width="6" height="22" fill="#cbd5e1" stroke="{K}"/><path d="M97 64 v8" stroke="{K}" stroke-width="1.6"/>'
                     f'<rect x="90" y="64" width="16" height="5" fill="#64748b"/><path d="M46 72 h36" stroke="#fff" stroke-width="2" stroke-dasharray="3 3"/>')


def washing_machine():
    return 90, 100, (f'<rect x="6" y="4" width="78" height="92" rx="6" fill="#f1f5f9" stroke="{K}"/>'
                     f'<path d="M6 24 H84" stroke="{K}"/><circle cx="20" cy="14" r="5" fill="#cbd5e1" stroke="{K}"/><circle cx="36" cy="14" r="5" fill="#cbd5e1" stroke="{K}"/>'
                     f'<rect x="56" y="10" width="20" height="8" rx="2" fill="#38bdf8" stroke="{K}"/>'
                     f'<circle cx="45" cy="60" r="28" fill="#cbd5e1" stroke="{K}"/><circle cx="45" cy="60" r="21" fill="#7dd3fc" stroke="{K}"/>'
                     f'<path d="M30 52 Q45 40 60 52" stroke="#fff" stroke-width="3" fill="none" opacity=".8"/><path d="M33 70 Q45 80 57 70" stroke="#0ea5e9" stroke-width="3" fill="none"/>')


def refrigerator():
    return 70, 112, (f'<rect x="8" y="4" width="54" height="104" rx="5" fill="#e2e8f0" stroke="{K}"/>'
                     f'<path d="M8 38 H62" stroke="{K}" stroke-width="1.6"/><rect x="14" y="16" width="3.5" height="14" rx="1.5" fill="#64748b"/>'
                     f'<rect x="14" y="48" width="3.5" height="30" rx="1.5" fill="#64748b"/><circle cx="46" cy="22" r="2" fill="#38bdf8"/>')


def juicer():
    return 84, 100, (f'<path d="M14 66 H70 L66 94 H18z" fill="#f97316" stroke="{K}"/><circle cx="42" cy="80" r="5" fill="#fde68a" stroke="{K}"/>'
                     f'<path d="M20 20 H64 L60 66 H24z" fill="#e0f2fe" stroke="{K}"/><path d="M22 36 H62 L60 66 H24z" fill="#fb923c" opacity=".9"/>'
                     f'<rect x="16" y="12" width="52" height="8" rx="3" fill="#475569" stroke="{K}"/><path d="M68 18 q10 -2 10 6" stroke="{K}" stroke-width="2.5" fill="none"/>'
                     f'<circle cx="52" cy="48" r="7" fill="#fdba74"/>')


def bicycle(c=None):
    f = c or '#dc2626'
    return 124, 84, (f'<circle cx="24" cy="60" r="19" fill="none" stroke="{K}" stroke-width="3"/><circle cx="100" cy="60" r="19" fill="none" stroke="{K}" stroke-width="3"/>'
                     f'<path d="M24 60 L52 60 L44 30 Z M52 60 L88 30 L44 30 M88 30 L100 60" stroke="{f}" stroke-width="3.5" fill="none" stroke-linejoin="round"/>'
                     f'<path d="M88 30 L84 18 M78 18 H92" stroke="{K}" stroke-width="3.5" stroke-linecap="round"/><path d="M38 24 H52" stroke="{K}" stroke-width="5" stroke-linecap="round"/>'
                     f'<path d="M44 30 L42 24" stroke="{f}" stroke-width="3.5"/><circle cx="52" cy="60" r="4" fill="{K}"/><path d="M46 66 H58" stroke="{K}" stroke-width="3.5"/>'
                     f'<circle cx="24" cy="60" r="3" fill="{K}"/><circle cx="100" cy="60" r="3" fill="{K}"/>')


def scooter(c=None):
    f = c or '#dc2626'
    return 120, 90, (f'<circle cx="22" cy="72" r="11" fill="#475569" stroke="{K}" stroke-width="2"/><circle cx="98" cy="72" r="11" fill="#475569" stroke="{K}" stroke-width="2"/>'
                     f'<circle cx="22" cy="72" r="3.5" fill="#cbd5e1"/><circle cx="98" cy="72" r="3.5" fill="#cbd5e1"/>'
                     f'<rect x="22" y="62" width="64" height="7" rx="3" fill="{f}" stroke="{K}"/><path d="M86 66 L96 14 M84 14 H108" stroke="{K}" stroke-width="4" stroke-linecap="round"/>'
                     f'<path d="M98 72 L90 62" stroke="{f}" stroke-width="4"/>')


def lever():
    return 124, 80, (f'<path d="M62 44 L46 72 H78z" fill="#fbbf24" stroke="{K}"/>'
                     f'<path d="M10 56 L112 28" stroke="#92400e" stroke-width="7" stroke-linecap="round"/>'
                     f'<rect x="14" y="30" width="22" height="22" fill="#22c55e" stroke="{K}" transform="rotate(-15 25 41)"/>'
                     f'<path d="M104 10 L106 24" stroke="#dc2626" stroke-width="3"/><path d="M98 14 L106 24 L112 12" stroke="#dc2626" stroke-width="3" fill="none"/>')


def wedge():
    return 100, 70, (f'<path d="M8 60 L92 60 L92 24 Z" fill="#9ca3af" stroke="{K}"/><path d="M8 60 L92 60" stroke="{K}" stroke-width="2"/>'
                     f'<path d="M24 56 L82 34" stroke="#e5e7eb" stroke-width="2"/>')


def screw():
    return 60, 100, (f'<rect x="6" y="4" width="48" height="10" rx="3" fill="#9ca3af" stroke="{K}"/><path d="M30 6 v6" stroke="{K}" stroke-width="2"/>'
                     f'<path d="M22 14 H38 V76 L30 94 L22 76z" fill="#cbd5e1" stroke="{K}"/>'
                     + ''.join(f'<path d="M22 {y} L38 {y + 5}" stroke="{K}" stroke-width="2"/>' for y in range(22, 76, 9)))


def pulley():
    return 80, 110, (f'<path d="M40 2 V16" stroke="{K}" stroke-width="4"/><circle cx="40" cy="32" r="18" fill="#cbd5e1" stroke="{K}" stroke-width="2"/><circle cx="40" cy="32" r="5" fill="{K}"/>'
                     f'<path d="M22 32 V74 M58 32 V62" stroke="#92400e" stroke-width="3"/>'
                     f'<path d="M58 62 q4 0 4 6 q0 4 -4 4" stroke="{K}" stroke-width="3" fill="none"/><path d="M22 74 q0 8 -4 8" stroke="{K}" stroke-width="3" fill="none"/>'
                     f'<rect x="10" y="84" width="24" height="20" rx="2" fill="#f59e0b" stroke="{K}"/>')


def phone_card():
    return 54, 100, (f'<rect x="6" y="4" width="42" height="92" rx="8" fill="#1f2937" stroke="{K}"/><rect x="10" y="14" width="34" height="68" rx="2" fill="#fde68a"/>'
                     f'<circle cx="27" cy="89" r="3" fill="#9ca3af"/>')


# ---- keyboard ----------------------------------------------------------------------------------------------

U = 10

# one colour per finger (left pinky, ring, middle, index, right index, middle, ring, pinky) and the finger of each letter key
FINGER = ['#f9a8d4', '#fdba74', '#fde047', '#86efac', '#67e8f9', '#93c5fd', '#c4b5fd', '#f87171']
FNUM = [0, 0, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]
FTOP = [0, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]
FHOME = [0, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7]
FBOT = [0, 1, 2, 3, 3, 4, 4, 5, 6, 7]


def _kb(hl, c=None, blank=False, overlay=False, np=False, fingers=False):
    """-> (svg body, width, height, {group: [key centres]}); np = with the numeric keypad on the right"""
    body_c = c or '#1f2937'
    keys, groups = [], {}

    def key(x, y, w, grp, text='', h=1, col=None):
        keys.append((x, y, w, grp, text, h, col if fingers else None))
        groups.setdefault(grp, []).append((x * U + w * U / 2, y * U + U * 0.45 * h))

    y0 = 0.4
    key(0, y0, 1, 'esc', 'Esc')
    for i in range(12):
        key(2 + i + (i // 4) * 0.0, y0, 1, 'function', f'F{i + 1}')
    key(14, y0, 1, 'plain', 'Del')
    r = 1.6
    for i in range(13):
        key(i, r, 1, 'punct' if i in (0, 11, 12) else 'numbers', '`1234567890-='[i], col=FINGER[FNUM[i]])
    key(13, r, 2, 'plain', 'Back')
    r = 2.6
    key(0, r, 1.5, 'plain', 'Tab')
    for i, ch in enumerate('QWERTYUIOP[]'):
        key(1.5 + i, r, 1, 'letters' if i < 10 else 'punct', ch, col=FINGER[FTOP[i]])
    key(13.5, r, 1.5, 'punct', '\\')
    r = 3.6
    key(0, r, 1.75, 'caps', 'Caps')
    for i, ch in enumerate("ASDFGHJKL;'"):
        key(1.75 + i, r, 1, 'home' if i in (0, 1, 2, 3, 6, 7, 8, 9) else ('letters' if i < 9 else 'punct'), ch, col=FINGER[FHOME[i]])
    key(12.75, r, 2.25, 'enter', 'Enter')
    r = 4.6
    key(0, r, 2.25, 'shift', 'Shift')
    for i, ch in enumerate('ZXCVBNM,./'):
        key(2.25 + i, r, 1, 'letters' if i < 7 else 'punct', ch, col=FINGER[FBOT[i]])
    key(12.25, r, 2.75, 'shift', 'Shift')
    r = 5.6
    key(0, r, 1.25, 'ctrl', 'Ctrl')
    key(1.25, r, 1.25, 'plain', 'Win')
    key(2.5, r, 1.25, 'plain', 'Alt')
    key(3.75, r, 6.25, 'space', 'Space')
    key(10, r, 1.25, 'plain', 'Alt')
    key(11.25, r, 1.25, 'plain', 'Win')
    key(12.5, r, 1.25, 'plain', 'Menu')
    key(13.75, r, 1.25, 'ctrl', 'Ctrl')
    key(16.5, 4.6, 1, 'arrows', '▲')
    for i, ch in enumerate('◀▼▶'):
        key(15.5 + i, 5.6, 1, 'arrows', ch)
    if np:   # numeric keypad: Num / * -, 7 8 9 +, 4 5 6, 1 2 3 Enter, 0 .
        x0 = 19.4
        for i, ch in enumerate(['Num', '/', '*', '-']):
            key(x0 + i, 1.6, 1, 'numeric', ch)
        for i, ch in enumerate('789'):
            key(x0 + i, 2.6, 1, 'numeric', ch)
        key(x0 + 3, 2.6, 1, 'numeric', '+', 2)
        for i, ch in enumerate('456'):
            key(x0 + i, 3.6, 1, 'numeric', ch)
        for i, ch in enumerate('123'):
            key(x0 + i, 4.6, 1, 'numeric', ch)
        key(x0 + 3, 4.6, 1, 'numeric', 'Ent', 2)
        key(x0, 5.6, 2, 'numeric', '0')
        key(x0 + 2, 5.6, 1, 'numeric', '.')
    if 'special' in hl:
        hl = set(hl) | {'esc', 'caps', 'shift', 'ctrl', 'enter'}
    if 'letters' in hl:
        hl = set(hl) | {'home'}
    groups['letters'] = groups.get('letters', []) + groups.get('home', [])
    groups['special'] = [p for g in ('esc', 'caps', 'shift', 'ctrl', 'enter') for p in groups.get(g, [])]
    W, H = (23.6 if np else 18.6) * U + 8, 6.9 * U + 4
    s = '' if overlay else f'<rect x="1" y="1" width="{W - 2:.0f}" height="{H - 2:.0f}" rx="7" fill="{body_c}" stroke="{K}" stroke-width="1.5"/>'
    rects, texts = '', ''
    for x, y, w, grp, text, kh, kc in keys:
        on = grp in hl
        if overlay and not on:
            continue
        fill = HL if on else (kc or '#f1f5f9')
        px, py = 4 + x * U, 2 + y * U
        rects += f'<rect x="{px:.1f}" y="{py:.1f}" width="{w * U - 1.4:.1f}" height="{kh * U - 1.4:.1f}" rx="1.6" fill="{fill}"/>'
        if text and not blank and (w > 1.1 or text in ('Del',) or not on or grp in ('letters', 'numbers', 'home', 'punct')):
            texts += (f'<text x="{px + (w * U - 1.4) / 2:.1f}" y="{py + (kh * U - 1.4) / 2 + 1.8:.1f}" text-anchor="middle" font-size="{3.6 if len(text) > 1 else 4.4}" fill="#334155">{escape(text)}</text>')
    s += f'<g stroke="#94a3b8" stroke-width=".5">{rects}</g>' + (f'<g>{texts}</g>' if texts else '')
    s_groups = {g: [(4 + cx, 2 + cy) for cx, cy in pts] for g, pts in groups.items()}
    return s, W, H, s_groups


def _tag_w(text):
    return 6.0 * len(text) + 16


def _label_tag(text, x, y):
    """A pink name tag centred on x, top at y (20 high)."""
    wd = _tag_w(text)
    return (f'<rect x="{x - wd / 2:.1f}" y="{y:.1f}" width="{wd:.1f}" height="19" rx="9.5" fill="#fce7f3" stroke="{PINK}"/>'
            f'<text x="{x:.1f}" y="{y + 13.5:.1f}" text-anchor="middle" font-size="10.5" font-weight="700" fill="{PINK}">{escape(text)}</text>')


def _spread(xs, widths, lo, hi, gap=8):
    """Move tag centres apart (keeping their order) so they do not overlap and stay inside lo..hi."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    pos = list(xs)
    for a, b in zip(order, order[1:]):
        need = (widths[a] + widths[b]) / 2 + gap
        if pos[b] - pos[a] < need:
            pos[b] = pos[a] + need
    over = pos[order[-1]] + widths[order[-1]] / 2 - hi
    if over > 0:
        for i in order:
            pos[i] -= over
    for i in order:
        pos[i] = max(pos[i], lo + widths[i] / 2)
    return pos


def kb_scene(opts):
    hl = set(filter(None, (opts.get('hl') or '').split(',')))
    scale = float(opts.get('s', 2.0))
    body, W, H, groups = _kb(hl, blank='blank' in opts, np='np' in opts, fingers='fingers' in opts)
    labels = [x.strip() for x in (opts.get('lab') or '').split('|') if x.strip()]
    top = [l for l in labels if l.rpartition('@')[2] in ('esc', 'function')]
    low = [l for l in labels if l not in top]
    pad_t = 30 if top else 0
    pad_b = 36 if low else 0
    out = f'<g transform="translate(0 {pad_t})">{body}</g>'
    for group, ty, anchor_y in ((top, 2, pad_t - 1), (low, pad_t + H + 14, pad_t + H - 2)):
        if not group:
            continue
        parts = [l.partition('@') for l in group]
        cx = []
        for text, _, grp in parts:
            pts = groups.get(grp) or [(W / 2, 0)]
            cx.append(sum(p[0] for p in pts) / len(pts))
        pos = _spread(cx, [_tag_w(t) for t, _, _ in parts], 0, W)
        for (text, _, grp), lx in zip(parts, pos):
            for px, py in (groups.get(grp) or [])[:3]:
                y1 = ty + 19 if ty < pad_t else ty
                out += (f'<path d="M{lx:.1f} {y1:.1f} L{px:.1f} {py + pad_t:.1f}" stroke="#dc2626" stroke-width="1.3" fill="none"/>'
                        f'<circle cx="{px:.1f}" cy="{py + pad_t:.1f}" r="2" fill="#dc2626"/>')
            out += _label_tag(text, lx, ty)
    return _svg(W, H + pad_t + pad_b, out, 'keyboard' + (' with ' + ', '.join(labels) if labels else ''), scale)


def mouse_scene(opts):
    scale = float(opts.get('s', 2.0))
    hl = opts.get('hl')
    w, h, body = mouse(hl=hl if hl in ('left', 'right', 'wheel') else None, wire=False)
    if 'parts' not in opts:
        return _svg(w, h, body, 'mouse', scale)
    out = f'<g transform="translate(105 26)">{body}</g>'
    dot = lambda x, y: f'<circle cx="{x}" cy="{y}" r="2" fill="#dc2626"/>'
    out += ('<path d="M92 54 H122" stroke="#dc2626" stroke-width="1.3"/>' + dot(122, 54) +
            '<path d="M178 54 H148" stroke="#dc2626" stroke-width="1.3"/>' + dot(148, 54) +
            '<path d="M135 20 V48" stroke="#dc2626" stroke-width="1.3"/>' + dot(135, 48))
    names = ('', '', '') if 'blank' in opts else ('Left Button', 'Right Button', 'Scroll Wheel')
    tag = _label_tag if names[0] else (lambda t, x, y: f'<rect x="{x - 42:.0f}" y="{y:.0f}" width="84" height="19" rx="9.5" fill="#fff" stroke="{PINK}" stroke-dasharray="3 2"/>')
    out += tag(names[0] or '', 52, 44) + tag(names[1] or '', 222, 44) + tag(names[2] or '', 135, 1)
    return _svg(274, 122, out, 'mouse with its left button, right button and scroll wheel', scale)



def wireless_mouse(c=None):
    w, h, body = mouse(c or '#dc2626', wire=False)
    return w, h, body + f'<rect x="22" y="80" width="16" height="6" rx="2" fill="#94a3b8" stroke="{K}"/>'


def pointer_arrow(c=None):
    return 60, 64, f'<path d="M14 4 L14 52 L26 41 L34 60 L43 56 L35 38 L51 37 Z" fill="{c or "#1f2937"}" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>'


def tick_mark(c=None):
    return 60, 60, f'<path d="M8 32 L24 48 L54 10" stroke="{c or "#16a34a"}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'


def cross_mark(c=None):
    return 60, 60, f'<path d="M10 10 L50 50 M50 10 L10 50" stroke="{c or "#dc2626"}" stroke-width="9" fill="none" stroke-linecap="round"/>'


def desktop_small(c=None):
    mw, mh, mb = monitor()
    tw, th, tb = tower()
    kb, kw, kh, _ = _kb(set())
    return 130, 114, (f'<g transform="translate(2 2) scale(.8)">{mb}</g><g transform="translate(92 4) scale(.62)">{tb}</g>'
                      f'<g transform="translate(20 74) scale(.5)">{kb}</g>')


def kbs_scene(opts):
    """Several small keyboards, each with its own key group in pink (a Match-the-columns picture column)."""
    items = [x.strip() for x in (opts.get('hl') or '').split('|') if x.strip()]
    scale = float(opts.get('s', 1.0))
    cols = 2 if len(items) <= 4 else 3
    sc = 0.72
    base, W, H, _ = _kb(set(), blank=True, np='np' in opts)
    cw, ch = W * sc + 14, H * sc + 12
    out = f'<defs><g id="mkb-base">{base}</g></defs>'   # one plain keyboard, reused; only the coloured keys are drawn again
    for i, it in enumerate(items):
        over, _, _, _ = _kb(set(it.split(',')), blank=True, overlay=True, np='np' in opts)
        out += f'<g transform="translate({(i % cols) * cw + 4:.1f} {(i // cols) * ch + 4:.1f}) scale({sc})"><use href="#mkb-base"/>{over}</g>'
    rows = (len(items) + cols - 1) // cols
    return _svg(cols * cw + 4, rows * ch + 4, out, 'keyboards with different keys coloured', scale)



def palmtop():
    keys = ''.join(f'<rect x="{14 + i * 13}" y="{66 + j * 10}" width="10" height="7" rx="2" fill="#e2e8f0"/>' for j in range(2) for i in range(4))
    return 80, 106, (f'<rect x="8" y="4" width="64" height="98" rx="9" fill="#475569" stroke="{K}"/>'
                     '<rect x="14" y="12" width="52" height="46" rx="3" fill="#bae6fd"/><path d="M14 12 L40 12 L14 40z" fill="#fff" opacity=".3"/>' + keys)


def smartphone():
    cols = [['#ef4444', '#22c55e', '#3b82f6'], ['#f59e0b', '#a855f7', '#14b8a6'], ['#ec4899', '#84cc16', '#0ea5e9']]
    apps = ''.join(f'<rect x="{13 + i * 12}" y="{17 + j * 13}" width="10" height="10" rx="2.5" fill="{c}"/>' for j, r_ in enumerate(cols) for i, c in enumerate(r_))
    return 56, 108, (f'<rect x="4" y="3" width="48" height="102" rx="9" fill="#1f2937" stroke="{K}"/><rect x="9" y="12" width="38" height="74" rx="2" fill="#dbeafe"/>'
                     + apps + '<circle cx="28" cy="95" r="4" fill="#475569"/><rect x="22" y="6" width="12" height="2.5" rx="1.2" fill="#475569"/>')


def hand_scanner():
    return 96, 76, (f'<rect x="6" y="12" width="62" height="26" rx="7" fill="#1f2937" stroke="{K}"/><rect x="62" y="17" width="7" height="16" fill="#ef4444"/>'
                    f'<path d="M24 38 L18 72 H38 L43 38z" fill="#475569" stroke="{K}"/><path d="M69 25 L92 17 M69 25 L94 25 M69 25 L92 33" stroke="#ef4444" stroke-width="1.6"/>'
                    '<rect x="18" y="18" width="30" height="5" rx="2" fill="#94a3b8"/>')


def scanner():
    return 124, 78, (f'<rect x="4" y="36" width="116" height="34" rx="4" fill="#94a3b8" stroke="{K}"/>'
                     f'<path d="M10 36 L22 10 H102 L114 36z" fill="#e5e7eb" stroke="{K}"/><rect x="24" y="42" width="76" height="20" rx="2" fill="#7dd3fc" stroke="{K}"/>'
                     '<path d="M24 42 L50 42 L36 62 L24 62z" fill="#fff" opacity=".3"/><circle cx="110" cy="52" r="3" fill="#22c55e"/>')


def webcam():
    return 64, 86, (f'<path d="M20 52 L44 52 L38 66 H26z" fill="#475569" stroke="{K}"/><rect x="10" y="66" width="44" height="9" rx="3" fill="#94a3b8" stroke="{K}"/>'
                    f'<circle cx="32" cy="30" r="22" fill="#1f2937" stroke="{K}"/><circle cx="32" cy="30" r="14" fill="#0f172a" stroke="#9ca3af" stroke-width="2"/>'
                    '<circle cx="27" cy="25" r="4" fill="#fff" opacity=".7"/><circle cx="52" cy="14" r="2.5" fill="#22c55e"/>')


def router():
    leds = ''.join(f'<circle cx="{x}" cy="42" r="3" fill="{c}"/>' for x, c in ((22, '#22c55e'), (36, '#22c55e'), (50, '#f59e0b'), (64, '#22c55e')))
    return 124, 66, ('<rect x="20" y="4" width="5" height="26" rx="2" fill="#475569"/><rect x="60" y="2" width="5" height="28" rx="2" fill="#475569"/><rect x="100" y="4" width="5" height="26" rx="2" fill="#475569"/>'
                     f'<rect x="6" y="28" width="112" height="30" rx="5" fill="#1f2937" stroke="{K}"/>' + leds +
                     '<rect x="84" y="38" width="8" height="8" fill="#94a3b8"/><rect x="96" y="38" width="8" height="8" fill="#94a3b8"/>')


def joystick():
    return 88, 106, (f'<path d="M6 98 H82 V86 Q82 78 74 78 H14 Q6 78 6 86z" fill="#1f2937" stroke="{K}"/><rect x="40" y="28" width="8" height="52" fill="#94a3b8" stroke="{K}"/>'
                     f'<circle cx="44" cy="20" r="15" fill="#ef4444" stroke="{K}"/><circle cx="39" cy="15" r="4" fill="#fff" opacity=".5"/>'
                     '<circle cx="20" cy="89" r="4" fill="#ef4444"/><circle cx="68" cy="89" r="4" fill="#f59e0b"/>')


def usb_drive():
    return 50, 112, (f'<rect x="12" y="4" width="26" height="28" fill="#cbd5e1" stroke="{K}"/><rect x="17" y="10" width="5" height="6" fill="#334155"/><rect x="28" y="10" width="5" height="6" fill="#334155"/>'
                     f'<rect x="8" y="32" width="34" height="72" rx="7" fill="#ef4444" stroke="{K}"/><rect x="12" y="38" width="26" height="6" rx="3" fill="#fecaca"/>'
                     '<circle cx="25" cy="92" r="4.5" fill="#fff" stroke="#334155"/>')


def memory_card():
    pins = ''.join(f'<rect x="{13 + i * 6}" y="14" width="3.4" height="10" fill="#eab308"/>' for i in range(6))
    return 62, 86, (f'<path d="M8 8 H40 L54 22 V76 Q54 80 50 80 H12 Q8 80 8 76z" fill="#1d4ed8" stroke="{K}"/>' + pins +
                    '<rect x="16" y="44" width="30" height="20" rx="2" fill="#fff"/><text x="31" y="58" text-anchor="middle" font-size="10" font-weight="700" fill="#1d4ed8">SD</text>')


def external_disk():
    return 108, 66, (f'<rect x="4" y="8" width="84" height="48" rx="9" fill="#334155" stroke="{K}"/><rect x="10" y="14" width="72" height="8" rx="4" fill="#64748b"/>'
                     '<circle cx="18" cy="44" r="3.5" fill="#38bdf8"/><path d="M88 36 H98 Q104 36 104 30" stroke="#1f2937" stroke-width="3" fill="none"/>')


def cd_disc():
    return 76, 76, (f'<circle cx="38" cy="38" r="34" fill="#f1f5f9" stroke="{K}"/><circle cx="38" cy="38" r="25" fill="#cbd5e1" opacity=".8"/>'
                    f'<path d="M38 5 A33 33 0 0 1 71 38 L38 38z" fill="#e0e7ff" opacity=".8"/><circle cx="38" cy="38" r="9" fill="#fff" stroke="{K}"/><circle cx="38" cy="38" r="3" fill="#94a3b8"/>')


def robot():
    return 84, 110, (f'<path d="M42 4 V16" stroke="{K}" stroke-width="2.5"/><circle cx="42" cy="5" r="4" fill="#ef4444" stroke="{K}"/>'
                     f'<rect x="16" y="16" width="52" height="36" rx="9" fill="#cbd5e1" stroke="{K}"/>'
                     f'<circle cx="31" cy="33" r="7" fill="#38bdf8" stroke="{K}"/><circle cx="53" cy="33" r="7" fill="#38bdf8" stroke="{K}"/><circle cx="31" cy="33" r="2.5" fill="#0f172a"/><circle cx="53" cy="33" r="2.5" fill="#0f172a"/>'
                     '<rect x="30" y="43" width="24" height="4" rx="2" fill="#475569"/><rect x="38" y="52" width="8" height="5" fill="#94a3b8"/>'
                     f'<rect x="20" y="57" width="44" height="34" rx="7" fill="#38bdf8" stroke="{K}"/><circle cx="42" cy="74" r="7" fill="#fde047" stroke="{K}"/>'
                     f'<rect x="6" y="59" width="11" height="28" rx="5" fill="#94a3b8" stroke="{K}"/><rect x="67" y="59" width="11" height="28" rx="5" fill="#94a3b8" stroke="{K}"/>'
                     f'<rect x="26" y="91" width="11" height="16" rx="3" fill="#94a3b8" stroke="{K}"/><rect x="47" y="91" width="11" height="16" rx="3" fill="#94a3b8" stroke="{K}"/>')



def headphones():
    return 84, 82, (f'<path d="M14 46 Q14 8 42 8 Q70 8 70 46" fill="none" stroke="{K}" stroke-width="6"/><path d="M14 46 Q14 8 42 8 Q70 8 70 46" fill="none" stroke="#ef4444" stroke-width="3"/>'
                    f'<rect x="6" y="42" width="18" height="32" rx="7" fill="#1f2937" stroke="{K}"/><rect x="60" y="42" width="18" height="32" rx="7" fill="#1f2937" stroke="{K}"/>'
                    '<rect x="10" y="48" width="8" height="20" rx="4" fill="#64748b"/><rect x="66" y="48" width="8" height="20" rx="4" fill="#64748b"/>')


def microphone():
    grid = ''.join(f'<path d="M{x} 12 V36" stroke="#94a3b8" stroke-width="1"/>' for x in range(14, 38, 5)) + ''.join(f'<path d="M10 {y} H40" stroke="#94a3b8" stroke-width="1"/>' for y in range(16, 36, 5))
    return 50, 104, (f'<path d="M20 42 H30 L33 92 H17z" fill="#475569" stroke="{K}"/><rect x="12" y="92" width="26" height="8" rx="3" fill="#1f2937"/>'
                     f'<circle cx="25" cy="24" r="16" fill="#334155" stroke="{K}"/>' + grid + '<rect x="17" y="38" width="16" height="6" rx="2" fill="#94a3b8" stroke="#334155"/>')


def plotter():
    return 132, 76, (f'<rect x="6" y="14" width="120" height="30" rx="5" fill="#cbd5e1" stroke="{K}"/><rect x="14" y="22" width="80" height="6" rx="3" fill="#475569"/>'
                     '<circle cx="108" cy="30" r="3" fill="#22c55e"/>'
                     f'<path d="M20 44 L112 44 L112 58 Q112 66 100 66 L32 66 Q20 66 20 58z" fill="#fff" stroke="{K}"/><path d="M30 52 H100 M30 58 H80" stroke="#60a5fa" stroke-width="2"/>'
                     f'<path d="M28 44 V72 M104 44 V72" stroke="{K}" stroke-width="3"/>')



def tablet():
    return 120, 88, (f'<rect x="4" y="6" width="112" height="76" rx="9" fill="#1f2937" stroke="{K}"/><rect x="12" y="13" width="96" height="62" rx="3" fill="#bfdbfe"/>'
                     '<path d="M12 13 L60 13 L12 52z" fill="#fff" opacity=".3"/><circle cx="8" cy="44" r="2" fill="#475569"/>'
                     '<rect x="48" y="26" width="24" height="24" rx="5" fill="#f59e0b"/><rect x="78" y="26" width="24" height="24" rx="5" fill="#22c55e"/>')


def game_console():
    return 124, 72, (f'<rect x="4" y="8" width="116" height="56" rx="14" fill="#3b82f6" stroke="{K}"/><rect x="34" y="14" width="56" height="42" rx="3" fill="#0f172a"/>'
                     '<rect x="40" y="20" width="44" height="30" fill="#4ade80"/><path d="M18 30 H34 M26 22 V38" stroke="#1f2937" stroke-width="5" stroke-linecap="round"/>'
                     '<circle cx="100" cy="26" r="5" fill="#ef4444"/><circle cx="108" cy="38" r="5" fill="#fde047"/><circle cx="96" cy="42" r="5" fill="#a855f7"/>')



SKIN = '#fcd9b6'


def _small(body):
    return 40, 40, body


SMALL = {
    'teeth': lambda: _small(f'<path d="M4 16 Q20 4 36 16 Q36 34 20 34 Q4 34 4 16z" fill="#f87171" stroke="{K}"/><path d="M8 16 Q20 8 32 16 L32 24 H8z" fill="#fff" stroke="{K}" stroke-width="1"/>'
                           f'<path d="M14 15 V24 M20 13 V24 M26 15 V24" stroke="{K}" stroke-width="1"/>'),
    'ear': lambda: _small(f'<path d="M14 6 C28 2 34 12 30 22 C28 30 24 32 22 38 C16 38 16 30 20 26 C10 26 6 14 14 6z" fill="{SKIN}" stroke="{K}"/><path d="M16 12 C24 10 26 18 22 22" fill="none" stroke="#d97706" stroke-width="1.6"/>'),
    'hand': lambda: _small(f'<path d="M10 38 V24 L6 16 Q4 12 8 12 Q10 12 12 16 V6 Q12 3 15 3 Q18 3 18 6 V14 V4 Q18 1 21 1 Q24 1 24 4 V14 V6 Q24 3 27 3 Q30 3 30 6 V18 Q34 14 36 18 Q36 22 30 30 V38z" fill="{SKIN}" stroke="{K}" stroke-linejoin="round"/>'),
    'foot': lambda: _small(f'<path d="M14 4 Q22 2 24 12 Q26 22 28 28 Q30 38 20 38 Q10 38 10 28 Q10 18 14 4z" fill="{SKIN}" stroke="{K}"/>'
                           + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}" stroke="{K}"/>' for x, y, r in ((14, 4, 2.6), (20, 3, 2.2), (25, 5, 2), (28, 8, 1.8), (30, 12, 1.6)))),
    'chalk': lambda: _small(f'<g transform="rotate(-35 20 20)"><rect x="4" y="15" width="30" height="9" rx="2" fill="#fff" stroke="{K}"/><rect x="26" y="15" width="8" height="9" fill="#e5e7eb" stroke="{K}"/></g>'
                            f'<rect x="6" y="30" width="26" height="7" rx="1.5" fill="#fde68a" stroke="{K}"/>'),
    'bench': lambda: _small(f'<rect x="3" y="14" width="34" height="6" rx="1.5" fill="#d97706" stroke="{K}"/><rect x="3" y="22" width="34" height="5" rx="1.5" fill="#b45309" stroke="{K}"/>'
                            f'<path d="M7 27 V37 M33 27 V37 M7 6 V14 M33 6 V14" stroke="{K}" stroke-width="3"/><rect x="5" y="6" width="30" height="5" rx="1.5" fill="#d97706" stroke="{K}"/>'),
    'whistle': lambda: _small(f'<path d="M6 16 H26 L34 22 V30 H12 Q6 30 6 24z" fill="#9ca3af" stroke="{K}"/><circle cx="14" cy="23" r="3.5" fill="#fff" stroke="{K}"/>'
                              f'<rect x="26" y="12" width="6" height="5" fill="#9ca3af" stroke="{K}"/><path d="M34 26 q4 0 4 5" fill="none" stroke="{K}" stroke-width="1.5"/>'),
    'wheat': lambda: _small(f'<path d="M20 38 V12" stroke="#a16207" stroke-width="2"/>' + ''.join(
        f'<ellipse cx="{20 + dx}" cy="{y}" rx="3" ry="5" fill="#eab308" stroke="#a16207" stroke-width=".8" transform="rotate({a} {20 + dx} {y})"/>' for dx, y, a in ((-5, 22, -30), (5, 22, 30), (-5, 14, -30), (5, 14, 30), (0, 6, 0)))),
    'brick': lambda: _small(f'<rect x="4" y="9" width="32" height="22" fill="#dc2626" stroke="{K}"/><path d="M4 20 H36 M20 9 V20 M12 20 V31 M28 20 V31" stroke="#fecaca" stroke-width="1.6"/>'),
    'whale': lambda: _small(f'<path d="M3 26 Q6 12 22 12 Q36 12 37 24 Q30 34 14 33 Q5 33 3 26z" fill="#3b82f6" stroke="{K}"/><path d="M37 24 Q40 16 37 12 M37 24 Q40 26 39 30" fill="none" stroke="{K}"/>'
                            f'<circle cx="12" cy="22" r="1.6" fill="#fff"/><path d="M20 12 q-2 -6 -6 -7 M20 12 q2 -6 6 -7" fill="none" stroke="#60a5fa" stroke-width="1.6"/><path d="M8 29 Q18 32 28 28" fill="none" stroke="#bfdbfe"/>'),
    'shop': lambda: _small(f'<rect x="5" y="16" width="30" height="20" fill="#fde68a" stroke="{K}"/><path d="M3 16 L6 6 H34 L37 16z" fill="#ef4444" stroke="{K}"/><path d="M12 6 L11 16 M20 6 V16 M28 6 L29 16" stroke="#fff" stroke-width="2"/>'
                           f'<rect x="9" y="21" width="12" height="10" fill="#bae6fd" stroke="{K}"/><rect x="25" y="21" width="7" height="15" fill="#92400e" stroke="{K}"/>'),
    'crab': lambda: _small(f'<ellipse cx="20" cy="24" rx="12" ry="8" fill="#ef4444" stroke="{K}"/><path d="M8 20 Q2 14 6 8 Q10 10 10 16 M32 20 Q38 14 34 8 Q30 10 30 16" fill="#ef4444" stroke="{K}"/>'
                           f'<path d="M10 28 L4 34 M13 31 L9 37 M30 28 L36 34 M27 31 L31 37" stroke="{K}" stroke-width="1.8"/><circle cx="15" cy="17" r="2.2" fill="#fff" stroke="{K}"/><circle cx="25" cy="17" r="2.2" fill="#fff" stroke="{K}"/>'),
    'rat': lambda: _small(f'<ellipse cx="20" cy="24" rx="13" ry="8" fill="#9ca3af" stroke="{K}"/><path d="M8 26 Q2 26 3 34 Q6 38 14 33" fill="none" stroke="#f9a8d4" stroke-width="2"/>'
                          f'<circle cx="31" cy="16" r="4" fill="#9ca3af" stroke="{K}"/><circle cx="30" cy="12" r="3" fill="#f9a8d4" stroke="{K}"/><path d="M33 23 L40 22" stroke="{K}"/><circle cx="35" cy="22" r="1.4" fill="{K}"/>'),
    'potato': lambda: _small(f'<path d="M6 22 Q4 12 16 10 Q30 8 34 18 Q36 30 22 32 Q8 34 6 22z" fill="#c2884d" stroke="{K}"/><circle cx="14" cy="18" r="1.2" fill="#92400e"/><circle cx="24" cy="24" r="1.2" fill="#92400e"/><circle cx="28" cy="16" r="1.2" fill="#92400e"/>'),
    'garlic': lambda: _small(f'<path d="M20 4 Q22 10 24 12 Q34 16 32 28 Q30 36 20 36 Q10 36 8 28 Q6 16 16 12 Q18 10 20 4z" fill="#f8fafc" stroke="{K}"/><path d="M20 12 Q14 24 20 36 M20 12 Q26 24 20 36" fill="none" stroke="#cbd5e1"/>'),
    'three': lambda: _small(''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#f59e0b" stroke="{K}"/>' for x, y in ((12, 24), (28, 24), (20, 11)))),
    'thick': lambda: _small(f'<rect x="6" y="6" width="28" height="28" rx="3" fill="#3b82f6" stroke="{K}"/><rect x="10" y="6" width="3" height="28" fill="#1d4ed8"/><path d="M16 14 H30 M16 20 H30" stroke="#fff" stroke-width="2"/>'),
    'thin': lambda: _small(f'<rect x="12" y="6" width="16" height="28" rx="1.5" fill="#3b82f6" stroke="{K}"/><rect x="14" y="6" width="1.5" height="28" fill="#1d4ed8"/><path d="M18 14 H25" stroke="#fff" stroke-width="1.6"/>'),
}


def _outline(svg):
    """A line drawing to colour in: every shape white, outlines kept."""
    return re.sub(r'(<(?:rect|path|circle|ellipse|polygon)' + chr(92) + r'b[^>]*?) fill="#[0-9a-fA-F]{3,6}"', chr(92) + r'1 fill="#ffffff"', svg)


# ---- registry and rows --------------------------------------------------------------------------------------

def _from_fig1(name):
    def make(c=None):
        return 40, 40, f'<g transform="translate(20 20)">{F1._icon(name, c)}</g>'
    return make


OBJECTS = {
    'monitor': monitor, 'tower': tower, 'mouse': mouse, 'laptop': laptop, 'printer': printer, 'speakers': speakers,
    'cpu': lambda c=None: cpu_chip(), 'motherboard': lambda c=None: motherboard(), 'psu': lambda c=None: power_supply(),
    'ram': lambda c=None: ram_stick(), 'harddisc': lambda c=None: hard_disc(), 'graphiccard': lambda c=None: graphic_card(),
    'dvddrive': lambda c=None: dvd_drive(), 'dvd': lambda c=None: dvd_disc(), 'keyboard': keyboard_pic,
    'sewing': lambda c=None: sewing(), 'washing': lambda c=None: washing_machine(), 'fridge': lambda c=None: refrigerator(),
    'juicer': lambda c=None: juicer(), 'bicycle': bicycle, 'scooter': scooter, 'lever': lambda c=None: lever(),
    'wedge': lambda c=None: wedge(), 'screw': lambda c=None: screw(), 'pulley': lambda c=None: pulley(),
    'phonecard': lambda c=None: phone_card(), 'wirelessmouse': wireless_mouse, 'pointer': pointer_arrow, 'tickmark': tick_mark,
    'crossmark': cross_mark, 'desktop': desktop_small,
    'palmtop': lambda c=None: palmtop(), 'smartphone': lambda c=None: smartphone(), 'handscanner': lambda c=None: hand_scanner(),
    'scanner': lambda c=None: scanner(), 'webcam': lambda c=None: webcam(), 'router': lambda c=None: router(),
    'joystick': lambda c=None: joystick(), 'usb': lambda c=None: usb_drive(), 'memcard': lambda c=None: memory_card(),
    'headphones': lambda c=None: headphones(), 'microphone': lambda c=None: microphone(), 'plotter': lambda c=None: plotter(),
    'tablet': lambda c=None: tablet(), 'gameconsole': lambda c=None: game_console(),
    'extdisk': lambda c=None: external_disk(), 'cd': lambda c=None: cd_disc(), 'robot': lambda c=None: robot(),
}
for _n in ('tree', 'plane', 'umbrella', 'phone', 'apple', 'fan', 'bread', 'car', 'tv', 'iron', 'lamp', 'clockicon', 'book',
          'bag', 'ball', 'cup', 'chair', 'table', 'bed', 'house', 'sun', 'moon', 'star', 'flower', 'fish', 'bird', 'cat', 'dog'):
    if _n not in OBJECTS:
        OBJECTS[_n] = _from_fig1(_n)
OBJECTS['bread'] = _from_fig1('loaf')
for _n, _f in SMALL.items():
    OBJECTS[_n] = (lambda f: (lambda c=None: f()))(_f)
# every other Government icon (255 of them) is available by its name too
_src = (Path(__file__).resolve().parents[3] / 'class-1' / 'tools' / 'figs1.py').read_text(encoding='utf-8')
_m = re.search(r"def _icon\(.*?\n    s = \{(.*?)\n    \}", _src, re.S)
for _n in re.findall(r"^        '([a-z0-9_]+)':", _m.group(1), re.M):
    OBJECTS.setdefault(_n, _from_fig1(_n))

SMALL.update({
    'arrow': lambda: _small('<path d="M4 20 H28 M20 10 L32 20 L20 30" fill="none" stroke="#dc2626" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'),
    'jellyfish': lambda: _small(f'<path d="M6 20 Q6 4 20 4 Q34 4 34 20z" fill="#f9a8d4" stroke="{K}"/><path d="M10 20 Q8 30 12 36 M16 20 Q14 30 17 38 M22 20 Q24 30 21 38 M28 20 Q30 30 27 36" fill="none" stroke="#ec4899" stroke-width="2" stroke-linecap="round"/>'),
    'monkey': lambda: _small(f'<circle cx="7" cy="20" r="4.5" fill="#92400e" stroke="{K}"/><circle cx="33" cy="20" r="4.5" fill="#92400e" stroke="{K}"/><circle cx="20" cy="20" r="13" fill="#92400e" stroke="{K}"/>'
                             f'<ellipse cx="20" cy="24" rx="9" ry="8" fill="#fcd9b6"/><circle cx="16" cy="19" r="2" fill="{K}"/><circle cx="24" cy="19" r="2" fill="{K}"/><ellipse cx="20" cy="26" rx="4" ry="2.4" fill="#d97706"/>'),
})
for _n in ('arrow', 'jellyfish', 'monkey'):
    OBJECTS[_n] = (lambda f: (lambda c=None: f()))(SMALL[_n])

SMALL.update({
    'hippo': lambda: _small(f'<ellipse cx="22" cy="26" rx="15" ry="9" fill="#a78bfa" stroke="{K}"/><path d="M4 18 Q4 10 12 10 H20 Q30 10 30 18 V24 H6z" fill="#a78bfa" stroke="{K}"/><rect x="2" y="16" width="14" height="10" rx="4" fill="#c4b5fd" stroke="{K}"/>'
                            f'<circle cx="7" cy="20" r="1.2" fill="{K}"/><circle cx="12" cy="20" r="1.2" fill="{K}"/><circle cx="18" cy="10" r="2" fill="#a78bfa" stroke="{K}"/><circle cx="24" cy="10" r="2" fill="#a78bfa" stroke="{K}"/>'
                            f'<rect x="12" y="32" width="5" height="5" fill="#8b5cf6" stroke="{K}"/><rect x="28" y="32" width="5" height="5" fill="#8b5cf6" stroke="{K}"/>'),
    'kangaroo': lambda: _small(f'<path d="M14 6 Q18 2 20 8 L22 14 Q30 18 28 28 L34 36 H20 L16 30 Q10 28 12 20 Q12 12 14 6z" fill="#d97706" stroke="{K}"/><path d="M28 28 Q36 30 38 38" fill="none" stroke="{K}" stroke-width="3"/>'
                               f'<path d="M14 6 L12 1 M18 5 L18 0" stroke="{K}" stroke-width="2"/><circle cx="16" cy="9" r="1.2" fill="{K}"/><path d="M18 22 Q22 26 18 28" fill="#fcd9b6" stroke="{K}"/>'),
    'deer': lambda: _small(f'<ellipse cx="20" cy="26" rx="11" ry="7" fill="#b45309" stroke="{K}"/><path d="M28 22 L32 10 Q34 6 37 8 Q38 12 34 14 L31 22z" fill="#b45309" stroke="{K}"/>'
                           f'<path d="M32 8 L30 2 M33 6 L37 2 M31 5 L28 4" stroke="{K}" stroke-width="1.6"/><path d="M12 31 V38 M17 32 V38 M24 32 V38 M29 31 V38" stroke="{K}" stroke-width="2.4"/><circle cx="35" cy="9" r="1" fill="{K}"/><circle cx="14" cy="24" r="1.4" fill="#fde68a"/><circle cx="20" cy="27" r="1.4" fill="#fde68a"/>'),
    'fox': lambda: _small(f'<path d="M4 34 Q2 22 12 24 L14 30z" fill="#ea580c" stroke="{K}"/><path d="M4 34 Q6 36 10 34" fill="#fff" stroke="{K}"/><ellipse cx="20" cy="27" rx="10" ry="7" fill="#ea580c" stroke="{K}"/>'
                          f'<path d="M26 20 L30 8 L34 14 L36 8 L38 20 L36 28 L28 28z" fill="#ea580c" stroke="{K}"/><path d="M30 24 L36 24 L33 28z" fill="#fff"/><circle cx="33" cy="20" r="1.2" fill="{K}"/><circle cx="36" cy="25" r="1.2" fill="{K}"/><path d="M14 33 V38 M22 33 V38" stroke="{K}" stroke-width="2.4"/>'),
    'squirrel': lambda: _small(f'<path d="M8 36 Q0 20 8 10 Q18 4 18 16 Q14 22 14 30z" fill="#b45309" stroke="{K}"/><ellipse cx="22" cy="28" rx="8" ry="9" fill="#d97706" stroke="{K}"/><circle cx="26" cy="16" r="5.5" fill="#d97706" stroke="{K}"/>'
                               f'<path d="M23 12 L22 7 L26 10M29 12 L31 7 L30 11" fill="#d97706" stroke="{K}"/><circle cx="28" cy="15" r="1" fill="{K}"/><path d="M26 34 H34" stroke="{K}" stroke-width="2.4"/>'),
    'stork': lambda: _small(f'<ellipse cx="18" cy="20" rx="11" ry="8" fill="#f8fafc" stroke="{K}"/><path d="M26 16 L28 8 Q31 4 33 8 L31 14z" fill="#f8fafc" stroke="{K}"/><path d="M32 7 L40 10 L32 11z" fill="#ef4444" stroke="{K}"/>'
                            f'<path d="M14 27 V38 M20 27 V38" stroke="#ef4444" stroke-width="2"/><path d="M8 20 H22" stroke="{K}" stroke-width="1.4"/><circle cx="31" cy="8" r="1" fill="{K}"/>'),
    'swan': lambda: _small(f'<path d="M6 28 Q4 36 16 36 H30 Q36 36 36 28 Q28 30 22 26 Q14 28 6 28z" fill="#f8fafc" stroke="{K}"/><path d="M26 26 Q34 22 30 14 Q28 6 34 6 Q38 6 36 10" fill="none" stroke="{K}" stroke-width="5" stroke-linecap="round"/>'
                           f'<path d="M26 26 Q34 22 30 14 Q28 6 34 6 Q38 6 36 10" fill="none" stroke="#f8fafc" stroke-width="3" stroke-linecap="round"/><path d="M37 9 L40 10 L37 12z" fill="#f97316" stroke="{K}" stroke-width=".8"/>'),
    'screwdriver': lambda: _small(f'<rect x="4" y="16" width="14" height="9" rx="4" fill="#ef4444" stroke="{K}"/><rect x="17" y="19" width="19" height="3.4" fill="#9ca3af" stroke="{K}"/><path d="M36 19 L39 18 V24 L36 22.4z" fill="#6b7280" stroke="{K}" stroke-width=".8"/>'),
    'straw': lambda: _small(f'<rect x="3" y="26" width="34" height="7" rx="3" fill="#f8fafc" stroke="{K}"/><path d="M8 26 L14 33 M16 26 L22 33 M24 26 L30 33" stroke="#ef4444" stroke-width="2.2"/><path d="M30 26 L36 12" stroke="{K}" stroke-width="6" stroke-linecap="round"/><path d="M30 26 L36 12" stroke="#f8fafc" stroke-width="3.4" stroke-linecap="round"/>'),
    'inkpot': lambda: _small(f'<path d="M10 16 H30 L34 36 H6z" fill="#1e3a8a" stroke="{K}"/><rect x="14" y="10" width="12" height="6" fill="#e5e7eb" stroke="{K}"/><path d="M12 24 H28" stroke="#93c5fd" stroke-width="2"/><path d="M26 10 L36 2" stroke="{K}" stroke-width="2"/>'),
    'nail': lambda: _small(f'<rect x="8" y="5" width="24" height="4" rx="1.5" fill="#9ca3af" stroke="{K}"/><path d="M18 9 H22 L21 36 L20 38 L19 36z" fill="#cbd5e1" stroke="{K}"/>'),
    'thorn': lambda: _small(f'<path d="M6 34 Q8 22 18 12 Q26 4 36 6 Q34 16 28 22 Q18 30 6 34z" fill="#16a34a" stroke="{K}"/><path d="M12 24 L8 22 M18 18 L14 14 M24 12 L24 7" stroke="{K}" stroke-width="1.8"/>'),
    'yellow': lambda: _small(f'<circle cx="20" cy="20" r="14" fill="#facc15" stroke="{K}"/><circle cx="15" cy="14" r="4" fill="#fef08a"/>'),
})
for _n in ('hippo', 'kangaroo', 'deer', 'fox', 'squirrel', 'stork', 'swan', 'screwdriver', 'straw', 'inkpot', 'nail', 'thorn', 'yellow'):
    OBJECTS[_n] = (lambda f: (lambda c=None: f()))(SMALL[_n])

SMALL.update({
    'bell': lambda: _small(f'<path d="M8 30 Q10 8 20 8 Q30 8 32 30z" fill="#facc15" stroke="{K}"/><rect x="5" y="30" width="30" height="4" rx="2" fill="#eab308" stroke="{K}"/><circle cx="20" cy="37" r="3" fill="#a16207" stroke="{K}"/><circle cx="20" cy="6" r="2.4" fill="#eab308" stroke="{K}"/>'),
    'glue': lambda: _small(f'<rect x="11" y="14" width="18" height="22" rx="4" fill="#f8fafc" stroke="{K}"/><rect x="14" y="5" width="12" height="9" rx="2" fill="#f97316" stroke="{K}"/><rect x="13" y="20" width="14" height="8" rx="1.5" fill="#60a5fa"/>'),
    'tube': lambda: _small(f'<path d="M6 12 H28 L34 20 L28 28 H6z" fill="#38bdf8" stroke="{K}"/><rect x="2" y="10" width="6" height="20" rx="2" fill="#0ea5e9" stroke="{K}"/><rect x="33" y="17" width="5" height="6" fill="#f8fafc" stroke="{K}"/><path d="M12 20 H26" stroke="#fff" stroke-width="2.4"/>'),
    'meat': lambda: _small(f'<path d="M8 14 Q8 4 20 6 Q34 8 30 22 Q28 30 18 28 Q8 26 8 14z" fill="#b91c1c" stroke="{K}"/><circle cx="19" cy="15" r="4" fill="#fecaca"/><path d="M26 28 L35 36" stroke="#e5e7eb" stroke-width="4" stroke-linecap="round"/><circle cx="36" cy="36" r="2.4" fill="#e5e7eb" stroke="{K}"/>'),
    'eight': lambda: _small(f'<rect x="5" y="3" width="30" height="34" rx="6" fill="#ede9fe" stroke="{K}"/><text x="20" y="31" text-anchor="middle" font-size="28" font-weight="700" fill="#7c3aed">8</text>'),
})
for _n in ('bell', 'glue', 'tube', 'meat', 'eight'):
    OBJECTS[_n] = (lambda f: (lambda c=None: f()))(SMALL[_n])

OBJECTS['fan'] = _from_fig1('fan')


def _icon(spec):
    """'tower.black' -> (w, h, body)"""
    name, _, opt = spec.partition('.')
    if name not in OBJECTS:
        raise SystemExit(f'pic: unknown object "{name}" (known: {", ".join(sorted(OBJECTS))})')
    fn = OBJECTS[name]
    if name == 'monitor':
        return fn(screen=opt) if opt in ('blue', 'dark', 'win', 'fun') else fn(opt or None)
    return fn(F1.C.get(opt, opt) if opt else None)


def row(opts, rest):
    scale = float(opts.get('s', 1.0))
    items = [x.strip() for x in rest.split('|') if x.strip()]
    cellw, boxh = 150, 96
    parts, labels = [], []
    for i, it in enumerate(items):
        tick = it.endswith('[]')
        it = it[:-2].strip() if tick else it
        label, _, spec = it.rpartition('=')
        w, h, body = _icon(spec.strip())
        fit = min(boxh / h, (cellw - 20) / w, 2.4 if w <= 40 else 1.0)
        ox = i * cellw + (cellw - w * fit) / 2
        oy = 6 + (boxh - h * fit) / 2
        parts.append(f'<g transform="translate({ox:.1f} {oy:.1f}) scale({fit:.3f})">{body}</g>')
        ty = boxh + 22
        if label.strip():
            parts.append(f'<text x="{i * cellw + cellw / 2:.0f}" y="{ty}" text-anchor="middle" font-size="14" font-weight="700" fill="{PINK}">{escape(label.strip())}</text>')
            labels.append(label.strip())
        if tick:
            parts.append(f'<rect x="{i * cellw + cellw / 2 - 11:.0f}" y="{ty + (8 if label.strip() else -14)}" width="22" height="22" rx="4" fill="#fff" stroke="#60a5fa" stroke-width="2"/>')
    W = max(len(items), 1) * cellw
    H = boxh + 6 + (30 if any(('=' in x and x.rpartition('=')[0].strip()) for x in items) else 6) + (30 if any(x.endswith('[]') for x in items) else 0)
    return _svg(W, H, ''.join(parts), ', '.join(labels) or 'pictures', scale)


def desk(opts):
    scale = float(opts.get('s', 1.0))
    mw, mh, mb = monitor()
    tw, th, tb = tower()
    kb, kw, kh, _ = _kb(set())
    ow, oh, ob = mouse(wire=False)
    W, H = 580, 290
    dot = lambda x, y: f'<circle cx="{x}" cy="{y}" r="2.2" fill="#dc2626"/>'
    s = ('<path d="M22 170 H418 L440 250 H0z" fill="#e8c28f" stroke="#334155"/><path d="M0 250 H440 V258 H0z" fill="#b45309" stroke="#334155"/>'
         '<path d="M14 258 V286 M426 258 V286" stroke="#b45309" stroke-width="8"/>'
         f'<g transform="translate(96 26) scale(1.5)">{mb}</g>'
         f'<g transform="translate(78 186) scale(.95)">{kb}</g>'
         f'<g transform="translate(318 176) scale(.7)">{ob}</g>'
         f'<g transform="translate(468 176) scale(1.15)">{tb}</g>')
    s += ('<path d="M92 20 L150 70" stroke="#dc2626" stroke-width="1.3"/>' + dot(150, 70) +
          '<path d="M512 112 L498 192" stroke="#dc2626" stroke-width="1.3"/>' + dot(498, 192) +
          '<path d="M40 232 L90 216" stroke="#dc2626" stroke-width="1.3"/>' + dot(90, 216) +
          '<path d="M372 168 L346 196" stroke="#dc2626" stroke-width="1.3"/>' + dot(346, 196))
    s += (_label_tag('Monitor', 62, 2) + _label_tag('System Unit', 512, 93) + _label_tag('Keyboard', 40, 232) + _label_tag('Mouse', 384, 150))
    return _svg(W, H, s, 'a desktop computer: monitor, system unit, keyboard and mouse', scale)


def make(line):
    """line: text after 'pic ' -> svg string"""
    kind, _, rest = line.strip().partition(' ')
    opts = {}
    # options: key=value tokens at the end, plus bare flags; for 'row' the items may contain '=' so only s= is read
    if kind == 'row':
        out_ = rest.endswith(' outline')
        if out_:
            rest = rest[:-len(' outline')]
        if ' s=' in rest:
            rest, _, sv = rest.rpartition(' s=')
            opts['s'] = sv.strip()
        return _outline(row(opts, rest)) if out_ else row(opts, rest)
    toks = []
    cur = rest
    # split on two or more spaces or on a recognised key=
    import re
    for m in re.finditer(r'(hl|lab|s)=(.*?)(?=\s+(?:hl|lab|s)=|$)', rest):
        opts[m.group(1)] = m.group(2).strip()
    flags = rest.split()
    for f in ('parts', 'blank', 'outline', 'np', 'fingers'):
        if f in flags:
            opts[f] = '1'
    if kind == 'kb':
        svg = kb_scene(opts)
    elif kind == 'kbs':
        svg = kbs_scene(opts)
    elif kind == 'mouse':
        svg = mouse_scene(opts)
    elif kind == 'desk':
        svg = desk(opts)
    else:
        raise SystemExit(f'pic: unknown picture kind "{kind}"')
    if 'outline' in opts:
        svg = _outline(svg)
    return svg
