"""Urdu XII PDF1: front cover (title, Board)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
b = Builder()
b.h('Urdu (Compulsory) — for Class Twelve', 'اُردو (لازمی) — بارھویں جماعت کے لیے', 'اردو (لازمي) — د دولسم ټولګي لپاره')
b.p('Khyber Pakhtunkhwa Textbook Board Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ پېښور')
b.p('Free From Government — NOT FOR SALE', 'Free From Government — NOT FOR SALE', 'Free From Government — NOT FOR SALE')
b.paras[-1]['untranslatedByDesign'] = True
UT = ('Front matter', 'ابتدائیہ', 'سریزه')
rec = BOOK.record(b, 'urdu12-fm-cover', 'Front cover', 'سرورق', 'پښتۍ', 1, [None], unit_title=UT)
rec['sourceCoverIllustrationReview'] = 'Cover painting (Minar-e-Pakistan, mountains, lake and a portrait of Allama Iqbal) and the Board logo are decorative; not reproduced.'

if __name__ == '__main__':
    BOOK.save(1, [('FM', rec)])
