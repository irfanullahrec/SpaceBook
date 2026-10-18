from math_agent1_sequential import save, render
blocks = [
 dict(type='paragraph',text='The word ‘matrices’ is plural of the word ‘matrix’. The term matrix was first introduced by the mathematician Arthur Cayley in 1860. The knowledge of matrices is necessary in the various areas of Mathematics. It has widely been used in the fields of pure mathematics, statistics, engineering and physical and social sciences. Thus, matrix theory finds an important place in modern age and has become an integral part of mathematics.'),
 dict(type='paragraph',text='Matrices make presentation of numbers clearer and make calculations easier. The following table presents the information about a series of hockey matches played between Pakistan and India.'),
 dict(type='dataTable',headers=['','Played','Won','Drawn','Lost'],rows=[['Pakistan',8,4,1,3],['India',8,3,1,4]]),
 dict(type='paragraph',text='The information is readily available when presented in this way. For example, if we want to know how many matches India lost against Pakistan, we go along the row ‘India’ and column ‘Lost’ and find that it is 4. Similarly, if we want to know how many matches Pakistan drew with India, we go along the row ‘Pakistan’ and column ‘Drawn’ and find that it is 1. As long as we remember what each number represents, we could remove the row and column headings and write just the numbers, enclosing them in square brackets or parenthesis such as'),
 dict(type='matrixProduct',matrices=[[[8,4,1,3],[8,3,1,4]]]),
 dict(type='paragraph',text='Let us denote this by A.'),
 dict(type='matrixProduct',prefix='Thus A =',matrices=[[[8,4,1,3],[8,3,1,4]]],suffix='is a matrix.')
]
save(dict(pdfPage=6,printedPage=2,page=2,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='1.1 INTRODUCTION TO MATRICES',sections=[dict(id='1.1',title='1.1 Introduction to Matrices',blocks=blocks)],
 visualStatus='Hockey table and both matrix displays rebuilt as structured data'))
render(7)
