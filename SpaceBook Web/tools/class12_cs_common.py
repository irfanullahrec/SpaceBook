"""Class 12 Computer Science helpers on top of class12_book_common (English source)."""
from class12_book_common import Book, Builder  # noqa: F401

BOOK = Book('cs')


def code(b, src):
    """Append a program listing as a 'code' block: the whole listing is one paragraph (newlines kept),
    identical in all languages; app.js renders 'code' blocks in a monospaced <pre>."""
    s = src.strip('\n')
    b.paras.append({'text': s, 'urdu': s, 'pashto': s, 'untranslatedByDesign': True})
    b.layout.append({'type': 'code', 'indices': [len(b.paras) - 1]})
    return b
