"""Pak Studies XII PDF1: front cover."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
b = Builder()
b.h('Pakistan Studies — for Class Twelve', 'مطالعہ پاکستان — بارھویں جماعت کے لیے', 'د پاکستان مطالعه — د دولسم ټولګي لپاره')
b.p('Khyber Pakhtunkhwa Textbook Board, Peshawar.', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.')
b.p('Free From Government — NOT FOR SALE', 'Free From Government — NOT FOR SALE', 'Free From Government — NOT FOR SALE')
b.paras[-1]['untranslatedByDesign'] = True
UT = ('Front matter', 'ابتدائیہ', 'سریزه')
rec = BOOK.record(b, 'pak12-fm-cover', 'Front cover', 'سرورق', 'پښتۍ', 1, [None], unit_title=UT)
rec['sourceCoverIllustrationReview'] = 'Cover photograph (pine forest, snow-capped mountains and river) and the Board logo are decorative; not reproduced.'

if __name__ == '__main__':
    BOOK.save(1, [('FM', rec)])
