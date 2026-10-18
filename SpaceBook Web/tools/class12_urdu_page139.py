"""Urdu XII PDF139 (spread): last scan — printed p.268 and the back cover, captured as mirror-image show-through (illegible)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
b = Builder()
b.h('Back matter (illegible scan)', 'آخری صفحات (ناقابلِ مطالعہ اسکین)', 'وروستۍ پاڼې (نه لوستل کېدونکی سکن)')
b.p('The final scan of the source PDF shows printed page 268 and the inside back cover only as a mirror-image show-through (the pages were photographed from the reverse side). Two framed quotations with references (apparently Qur’anic verses) and a short paragraph under a blue heading are visible but cannot be read reliably, even after horizontal flipping. No text is reproduced; consult the printed textbook.',
    'ماخذ PDF کا آخری اسکین صفحہ ۲۶۸ اور اندرونی پشتی سرورق کو صرف اُلٹی (آئینہ نما) جھلک کی صورت میں دکھاتا ہے (صفحات کی تصویر پشت کی طرف سے لی گئی ہے)۔ حوالوں کے ساتھ دو چوکھٹے دار اقتباسات (بظاہر قرآنی آیات) اور نیلے عنوان کے تحت ایک مختصر پیراگراف نظر آتا ہے، لیکن اُلٹا کرنے کے بعد بھی انھیں قابلِ اعتماد طور پر پڑھا نہیں جا سکتا۔ کوئی متن نقل نہیں کیا گیا؛ مطبوعہ درسی کتاب سے رجوع کریں۔',
    'د سرچینې PDF وروستی سکن چاپي ۲۶۸ مخ او د شا پوښ دننه برخه یوازې د هنداري‌ډوله اوښتي انځور په بڼه ښيي (پاڼې له شا خوا انځور شوې). د حوالو سره دوه چوکاټ‌لرونکي اقتباسونه (ښکاري قرآني ایتونه) او د شین سرلیک لاندې یو لنډ پراګراف ښکاري، خو حتی له اړولو وروسته هم په باوري ډول نه لوستل کېږي. هېڅ متن نه دی راوړل شوی؛ چاپي درسي کتاب ته مراجعه وکړئ.')
rec = BOOK.record(b, 'urdu12-backmatter', 'Back matter (illegible scan)', 'آخری صفحات', 'وروستۍ پاڼې', 139, [268])
rec['sourceGap'] = 'PDF139 is a mirror-image show-through of p.268 and the back cover; illegible — not transcribed.'
issues = [{'id': 'urdu12-pdf139', 'unit': 34, 'printedPage': 268, 'description': 'Final scan (PDF139) is mirrored show-through of printed p.268 and the back cover (framed verses with references, website watermark). Not legible; no text reproduced. Glossary (unit 34) ends on p.267.'}]

if __name__ == '__main__':
    BOOK.save(139, [(34, rec)], issues=issues, complete_units=[34])
