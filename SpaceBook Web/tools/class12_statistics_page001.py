"""PDF1: front cover (single page)."""
from class12_statistics_common import Builder, save


def cover_svg(title, sub, board):
    bars = [(60, 120, '#e11d48'), (110, 170, '#f59e0b'), (160, 95, '#a855f7'), (210, 205, '#f97316'),
            (260, 140, '#0ea5e9'), (310, 230, '#94a3b8'), (360, 180, '#22c55e')]
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 600" role="img" aria-label="Statistics Grade XII cover">',
         '<rect width="440" height="600" fill="#fffbea"/>',
         f'<rect x="20" y="20" width="200" height="40" fill="#fde047"/><text x="34" y="48" font-family="Arial" font-size="20" fill="#111">{title[0]}</text>',
         f'<text x="220" y="125" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="58" fill="#e11d48">{title[1]}</text>',
         f'<text x="400" y="165" text-anchor="end" font-family="Arial" font-size="20" fill="#1e3a8a">{sub}</text>']
    for x, h, c in bars:
        s.append(f'<rect x="{x}" y="{470 - h}" width="38" height="{h}" fill="{c}" opacity=".9"/><path d="M{x+38} {470-h}l10 -8v{h}l-10 8z" fill="{c}" opacity=".6"/>')
    s.append('<path d="M40 470H420" stroke="#334155" stroke-width="2"/>')
    s.append('<path d="M50 440L110 380L160 420L210 330L260 390L310 300L360 350L410 280" fill="none" stroke="#0f766e" stroke-width="3"/>')
    s.append('<path d="M70 450a50 50 0 1 1 1 0z" fill="none"/><circle cx="95" cy="250" r="45" fill="#22c55e"/><path d="M95 250V205A45 45 0 0 1 138 262Z" fill="#f97316"/><path d="M95 250L138 262A45 45 0 0 1 70 288Z" fill="#a855f7"/>')
    s.append(f'<rect x="0" y="500" width="440" height="100" fill="#bef264"/><text x="230" y="545" text-anchor="middle" font-family="Arial" font-weight="700" font-size="19" fill="#1e3a8a">{board[0]}</text>'
             f'<text x="230" y="572" text-anchor="middle" font-family="Arial" font-weight="700" font-size="19" fill="#1e3a8a">{board[1]}</text>'
             '<path d="M30 550l25 -22l25 22l-25 22z" fill="#fff" stroke="#1e3a8a"/></svg>')
    return ''.join(s)


b = Builder()
b.visual('stat12-cover-art',
         cover_svg(('A Textbook of', 'Statistics'), 'For Grade XII', ('Khyber Pakhtunkhwa Textbook Board', 'Peshawar')),
         cover_svg(('A Textbook of', 'Statistics'), 'For Grade XII', ('Khyber Pakhtunkhwa Textbook Board', 'Peshawar')),
         cover_svg(('A Textbook of', 'Statistics'), 'For Grade XII', ('Khyber Pakhtunkhwa Textbook Board', 'Peshawar')), ratio=.55)
b.h('A Textbook of Statistics', 'شماریات کی درسی کتاب', 'د احصایې درسي کتاب')
b.p('For Grade XII', 'برائے جماعت دوازدہم (بارہویں)', 'د دولسم ټولګي لپاره')
b.p('FREE FROM GOVT — NOT FOR SALE', 'حکومت کی طرف سے مفت — برائے فروخت نہیں', 'د حکومت له خوا وړیا — د پلور لپاره نه ده')
b.p('Khyber Pakhtunkhwa Textbook Board Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
rec = b.build('stat12-cover', 'Front cover', 'سرورق', 'د کتاب پوښ', 1, ['cover'])
rec['translationNote'] = 'Cover artwork (3-D bar/pie charts and line graph) is redrawn as a coded SVG; the printed watermark of the scan supplier is not reproduced.'

if __name__ == '__main__':
    save(1, [(1, rec)])
