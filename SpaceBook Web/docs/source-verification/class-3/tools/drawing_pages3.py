"""Class 3 Drawing: write drawing/pages/pNNN.txt.
Artwork = the source-matched coded SVG fragments kept from the legacy reader (drawing/legacy_art.json, viewBox 0 0 600 380);
each 'join the dots' page shows the coloured model and a dotted copy to trace. Titles and teacher instructions are read
from the scans (scan NNN = printed page NNN; scan 001 is an inserted advertisement)."""
import json
import re
from pathlib import Path

H = Path(__file__).resolve().parents[1] / 'drawing'
ART = json.load(open(H / 'legacy_art.json', encoding='utf-8'))
SIG = 'p Teacher Signature: ________ || استاد کے دستخط: ________ || د ښوونکي لاسلیک: ________'


def dotted(frag):
    f = re.sub(r'fill="(?!none)[^"]*"', 'fill="none"', frag)
    f = re.sub(r'stroke-dasharray="[^"]*"', '', f)
    return f'<g stroke-dasharray="2 9" stroke-linecap="round" opacity=".8">{f}</g>'


def svgblock(cap, frag, label, dots=True):
    s = (f'<svg viewBox="0 0 600 380" width="300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">'
         f'<g font-family="sans-serif">{frag}</g></svg>')
    out = [f'svg {cap}', s, 'endsvg']
    if dots:
        d = (f'<svg viewBox="0 0 600 380" width="300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}: dotted outline to join and colour">'
             f'<g font-family="sans-serif">{dotted(frag)}</g></svg>')
        out += ['svg Join the dots, then colour || نقطے ملائیں، پھر رنگ بھریں || ټکي سره ونښلوئ، بیا رنګ کړئ', d, 'endsvg']
    return out


J = ('Join the dots and colour the {e}', 'نقطے ملائیں اور {u} میں رنگ بھریں', 'ټکي سره ونښلوئ او {p} رنګ کړئ')
PAGES = [
    (0, 'book-cup', ('book and cup', 'کتاب اور کپ', 'کتاب او پیاله'), 'A blue mug with a yellow star standing on a green book (model) and a smiling apple on a stack of books.'),
    (2, 'bag', ('bag', 'بستے', 'بستې'), 'A red school bag with a smiling face and yellow and green pockets, and a cartoon blue-and-pink bag holding a pencil and ruler.'),
    (3, 'fruit', ('apple and pear', 'سیب اور ناشپاتی', 'مڼه او ناک'), 'A red apple and a green pear (model), and smiling cartoon pear and apple characters.'),
    (4, 'aquarium', ('aquarium', 'مچھلی گھر', 'د کبانو لوښي'), 'A fish bowl with three fish and a water plant, a round glass bowl with pebbles, and an undersea strip of fish and coral.'),
    (5, 'ceiling-fan', ('ceiling fan', 'چھت کے پنکھے', 'د چت پکې'), 'A three-blade ceiling fan with pink blades and a green body, and a photo of a five-blade multicoloured fan.'),
    (6, 'clock', ('clock', 'گھڑی', 'ساعت'), 'A yellow alarm clock with a blue rim showing four o\'clock, and a cartoon ringing alarm clock holding a hammer. The dotted copy has the numbers 1 to 12 printed in red.'),
    (7, 'racket-ball', ('racket and ball', 'ریکٹ اور گیند', 'ریکټ او توپ'), 'A tennis racket with a green ball, and a cartoon boy playing tennis.'),
    (8, 'sofa', ('sofa', 'صوفے', 'صوفه'), 'A pink smiling sofa, a photo of a wooden sofa set, and a cartoon bird holding balloons.'),
    (9, 'peacock', ('peacock', 'مور', 'تاوس'), 'A cartoon peacock with a fanned green tail, and a drawing of a real peacock.'),
    (10, 'scenery', ('scenery', 'منظر', 'منظره'), 'A park scene with a tree, sun, clouds, a fence, flowers and a rabbit; a second picture of a white bunny painting an egg in a garden.'),
    (11, 'shark', ('shark', 'شارک', 'شارک'), 'A grinning purple-and-blue cartoon shark, and an undersea picture of a shark with coral.'),
    (12, 'spinning-top', ('top', 'لٹو', 'لټو'), 'A red, pink and green spinning top with coloured rings, and a second colourful top.'),
    (13, 'eagle', ('eagle', 'عقاب', 'باز'), 'A photo of a bald eagle soaring, and a brown cartoon eagle landing.'),
    (14, 'pot', ('hot pot', 'دیگچی (ہاٹ پاٹ)', 'دېګ (هاټ پاټ)'), 'A blue cooking pot with a red lid, and a cartoon purple pot holding a ladle of soup.'),
    (15, 'rat', ('rat', 'چوہے', 'موږک'), 'A grey rat with a long tail, and a cartoon mouse with a pink tail.'),
    (16, 'cloud-sun', ('clouds, sun and droplets', 'بادلوں، سورج اور بوندوں', 'ورېځې، لمر او څاڅکي'), 'Blue clouds with rain drops in front of a yellow sun, and three children in the rain beside a house and a tree.'),
    (17, 'dinosaur', ('dinosaur', 'ڈائنوسار', 'ډایناسور'), 'A yellow cartoon T. rex with red stripes, and a picture of a T. rex facing a triceratops.'),
    (18, 'sandals', ('sandal', 'چپل', 'څپلۍ'), 'A pair of purple sandals with green straps and red flowers, a pair of colourful flip-flops, and coloured footprints.'),
    (19, 'flamingo', ('flamingo', 'فلیمنگو', 'فلامینګو'), 'A brown-and-orange cartoon flamingo standing on one leg, and a photo of pink flamingos walking.'),
    (20, 'jug-glass', ('jug and glass', 'جگ اور گلاس', 'جګ او ګیلاس'), 'A jug and a glass of red juice, and a cartoon glass of milk with a smiling face.'),
    (21, 'clown', ('clown', 'مسخرے', 'مسخره'), 'A clown face under a jester\'s hat with stars and bells, and a cartoon clown holding balloons.'),
    (22, 'flower-bee', ('flower and bee', 'پھول اور مکھی', 'ګل او مچۍ'), 'A pink flower with green leaves and a bee, a cartoon butterfly holding a flower, and a smiling blue flower.'),
    (23, 'bus', ('bus', 'بس', 'بس'), 'An orange-and-green "School Bus" with big eyes on a road, and a cartoon bus with passengers.'),
    (24, 'house-picture', ('picture', 'تصویر', 'انځور'), 'A red house with trees, a path and a green lawn (model).'),
    (25, 'tomato', ('tomato', 'ٹماٹر', 'رومي'), 'A red tomato with a green star-shaped top, and a photo of tomatoes on the vine.'),
]
LOOK = [
    (26, 'ship', ('ship', 'جہاز', 'بېړۍ'), 'Four outline steps (hull; hull and cabin; cabin and chimney; porthole and deck box) and a coloured red, green and pink ship, with an empty drawing box.'),
    (27, 'bird', ('bird', 'پرندہ', 'مرغۍ'), 'Four outline steps (body and head; eye and wing; beak; legs) and a coloured red bird with a green head, with an empty drawing box.'),
    (28, 'house-steps', ('house', 'گھر', 'کور'), 'Four outline steps (roof; walls; chimney; door and two windows) and a coloured yellow house with a brown roof, with an empty drawing box.'),
    (29, 'car-steps', ('car', 'گاڑی', 'موټر'), 'Four outline steps (wheels and top line; body; wheel hubs; steering wheel) and a coloured red car, with an empty drawing box. The title prints "Car" with a capital C.'),
    (30, 'fish-steps', ('fish', 'مچھلی', 'کب'), 'Four outline steps (body with open mouth; eye and gill line; fins; tail) and a coloured orange, pink and green fish, with an empty drawing box.'),
]
LOOK_T = ('Ask the students to draw the complete picture in the given space and colour it. || طلبہ سے کہیں کہ دی گئی جگہ میں مکمل تصویر بنائیں اور اس میں رنگ بھریں۔ '
          '|| زده کوونکو ته ووایاست چې په ورکړل شوي ځای کې بشپړ انځور جوړ کړي او رنګ یې کړي.')
TEACH = {
    3: ('The teacher should make model of apple and pear from clay plaster of paris and also colour. Assigned the students to do the same exercise at their homes. '
        '|| استاد مٹی یا پلاسٹر آف پیرس سے سیب اور ناشپاتی کا ماڈل بنائے اور اس میں رنگ بھرے۔ طلبہ کو گھر پر یہی مشق کرنے کا کام دیں۔ '
        '|| ښوونکی دې له خټې یا پلاستر اف پېرس د مڼې او ناک ماډل جوړ کړي او رنګ یې کړي. زده کوونکو ته دې همدا تمرین په کور کې ورکړي.'),
    25: ('The teacher should make model of Tomato from clay or plaster of paris and colour it. Encourage the students to do the same exercise at their own. '
         '|| استاد مٹی یا پلاسٹر آف پیرس سے ٹماٹر کا ماڈل بنائے اور اس میں رنگ بھرے۔ طلبہ کو خود یہی مشق کرنے کی ترغیب دیں۔ '
         '|| ښوونکی دې له خټې یا پلاستر اف پېرس د رومي ماډل جوړ کړي او رنګ یې کړي. زده کوونکي دې همدا تمرین پخپله کولو ته وهڅوي.'),
}
ISSUE = {3: 'The teacher note prints "clay plaster of paris" (meaning clay or plaster of Paris) and "Assigned" for "Assign". Kept as printed.',
         18: 'This page is scanned upside down; the content is given the right way up.',
         22: 'This page is scanned upside down; the content is given the right way up.',
         31: 'The title calls the folded bird both a duck and a pelican, as printed.'}
UNITS = {0: (1, 'Join the Dots and Colour (1)', 'نقطے ملائیں اور رنگ بھریں (1)', 'ټکي سره ونښلوئ او رنګ کړئ (1)'),
         13: (2, 'Join the Dots and Colour (2)', 'نقطے ملائیں اور رنگ بھریں (2)', 'ټکي سره ونښلوئ او رنګ کړئ (2)'),
         26: (3, 'Look and Draw', 'دیکھیں اور بنائیں', 'وګورئ او رسم یې کړئ'),
         31: (4, 'Paper Folding', 'کاغذ موڑنا', 'د کاغذ قاتول')}


def head(scan):
    L = [f'@printed {scan if scan else 1}', '@status lesson']
    if scan in UNITS:
        n, e, u, p = UNITS[scan]
        L += [f'@unit {n} | {e} || {u} || {p}', '@sec activities | Activities || سرگرمیاں || فعالیتونه']
    if scan in ISSUE:
        L.append('@issue ' + ISSUE[scan])
    return L


def write(scan, L):
    (H / 'pages' / f'p{scan:03}.txt').write_text('\n'.join(L) + '\n', encoding='utf-8')


def main():
    (H / 'pages').mkdir(exist_ok=True)
    for scan, key, (e, u, p), deco in PAGES:
        L = head(scan) + ['@deco ' + deco]
        L.append(f'## {J[0].format(e=e)} || {J[1].format(u=u)} || {J[2].format(p=p)}')
        L += svgblock(f'Model: {e} || نمونہ: {u} || نمونه: {p}', ART[key], f'Coloured model: {e}')
        L.append('p Trace over the dotted lines with a pencil, then colour the picture like the model. || نقطوں والی لکیروں پر پنسل پھیریں، پھر نمونے کی طرح تصویر میں رنگ بھریں۔ || پر ټکو لړو کرښو پنسل راتېر کړئ، بیا انځور د نمونې په څېر رنګ کړئ.')
        if scan == 24:
            L += ['box check | Activity || سرگرمی || فعالیت', 'p Draw a tree in the picture. || تصویر میں ایک درخت بنائیں۔ || په انځور کې یوه ونه رسم کړئ.', 'endbox']
        if scan in TEACH:
            L += ['box teach | Instructions for Teachers || اساتذہ کے لیے ہدایات || ښوونکو ته لارښوونې', 'p ' + TEACH[scan], 'endbox']
        write(scan, L + [SIG])
    for scan, key, (e, u, p), deco in LOOK:
        L = head(scan) + ['@deco ' + deco, f'## Look and draw the {e} || دیکھیں اور {u} بنائیں || وګورئ او {p} رسم کړئ']
        L += svgblock(f'Steps to draw the {e} || {u} بنانے کے مراحل || د {p} د رسم پړاوونه', ART[key], f'Steps to draw the {e}', dots=False)
        L += ['p Draw the complete picture in the box and colour it. || خانے میں مکمل تصویر بنائیں اور رنگ بھریں۔ || په خانه کې بشپړ انځور رسم کړئ او رنګ یې کړئ.',
              'box teach | Instructions for Teachers || اساتذہ کے لیے ہدایات || ښوونکو ته لارښوونې', 'p ' + LOOK_T, 'endbox', SIG]
        write(scan, L)
    fold = [(31, 'paper-duck', ('Art of making duck (pelican)', 'بطخ (پیلیکن) بنانے کا فن', 'د هیلۍ (پېلیکان) جوړولو هنر'),
             'Eight numbered folding diagrams in light blue (a square folded into a kite, narrowed, turned over, folded up and shaped) and the finished paper pelican.',
             'The teacher should demonstrate making of duck (pelican) from the paper and encourage the students to do the same exercise at their own. || استاد کاغذ سے بطخ (پیلیکن) بنانے کا عملی مظاہرہ کرے اور طلبہ کو خود یہی مشق کرنے کی ترغیب دے۔ || ښوونکی دې له کاغذ د هیلۍ (پېلیکان) جوړول وښيي او زده کوونکي دې همدا تمرین پخپله کولو ته وهڅوي.'),
            (32, 'paper-hat', ('Art of making hat', 'ٹوپی بنانے کا فن', 'د خولۍ جوړولو هنر'),
             'Eight numbered folding diagrams in grey-green (a sheet folded in half twice, corners folded down, brims folded up) and a child wearing the finished paper hat.',
             'The teacher should demonstrate making of hat from the paper and encourage the students to do the same exercise at their own. || استاد کاغذ سے ٹوپی بنانے کا عملی مظاہرہ کرے اور طلبہ کو خود یہی مشق کرنے کی ترغیب دے۔ || ښوونکی دې له کاغذ د خولۍ جوړول وښيي او زده کوونکي دې همدا تمرین پخپله کولو ته وهڅوي.')]
    for scan, key, (e, u, p), deco, tch in fold:
        L = head(scan) + ['@deco ' + deco, f'## {e} || {u} || {p}']
        L += svgblock('Folding steps || موڑنے کے مراحل || د قاتولو پړاوونه', ART[key], f'{e}: folding steps', dots=False)
        L += ['p Fold a sheet of paper step by step as shown. || دکھائے گئے طریقے سے کاغذ کو مرحلہ وار موڑیں۔ || کاغذ لکه څنګه چې ښودل شوی پړاو په پړاو قات کړئ.',
              'box teach | Instructions for Teachers || اساتذہ کے لیے ہدایات || ښوونکو ته لارښوونې', 'p ' + tch, 'endbox', SIG]
        write(scan, L)
    write(1, ['@status blank', '@deco A third-party website advertisement (awazeinqilab.com) inserted into the scanned PDF. It is not part of the textbook and is not reproduced.'])
    print('done')


if __name__ == '__main__':
    main()
