"""PDF1: front cover — A Textbook of English, Grade 12, Khyber Pakhtunkhwa Textbook Board, Peshawar."""
from class12_book_common import Book, Builder

BOOK = Book('english')
FM = ('Front matter', 'ابتدائی صفحات', 'لومړنۍ پاڼې')
b = Builder()
b.h('A Textbook of English — Grade 12', 'انگریزی کی درسی کتاب — جماعت 12', 'د انګلیسي درسي کتاب — ټولګی 12')
b.p('Khyber Pakhtunkhwa Textbook Board, Peshawar.', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.')
b.p('Free From Government — NOT FOR SALE', 'حکومت کی طرف سے مفت — برائے فروخت نہیں', 'له حکومت څخه وړیا — د پلور لپاره نه')
rec = BOOK.record(b, 'eng12-cover', 'Front cover', 'سرورق', 'مخکینی پوښ', 1, [], unit_title=FM)
rec['sourceCoverIllustrationReview'] = 'Cover artwork (library shelves, phonetic symbols, open book, board logo) is decorative and not reproduced; the third-party download watermark/footer is excluded.'

if __name__ == '__main__':
    BOOK.save(1, [('FM', rec)])
