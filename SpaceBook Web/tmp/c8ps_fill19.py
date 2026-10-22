exec(open('D:/SpaceBook/SpaceBook Web/tmp/c8ps_fill18.py',encoding='utf8').read().split("S=' (Derived")[0])
def H(page,key,what):
    addc(page,key,
     'دا ځواب د نظم په اشعارو پورې اړه لري چې په دې کتاب ډېټا کښې نه دي ورکړې شوي؛ د کتاب د نظم له متن نه ځواب جوړ کړئ۔ (Not verified)',
     'This answer depends on the verses of the poem, which are not reproduced in this book data; '+what+' from the printed poem text. (Not verified)',
     'یہ جواب نظم کے اشعار پر منحصر ہے جو یہاں موجود نہیں؛ کتاب میں چھپے متن سے جواب تیار کریں۔ (Not verified)')
H('007','د لاندې ورکړې شوي','')if False else None
for pg,key,w in [('017','مصرعې د نثري جملو','rewrite each given line as a prose sentence'),('079','مصرعې په نثر کښې','rewrite the lines in prose')]:
    try: H(pg,key,w)
    except StopIteration: print('miss',pg,key)
