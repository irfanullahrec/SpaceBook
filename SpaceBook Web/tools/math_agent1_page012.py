from math_agent1_sequential import save, render
def p(text): return dict(type='paragraph',text=text)
def m(rows,prefix='',suffix=''): return dict(type='matrixProduct',prefix=prefix,matrices=[rows],suffix=suffix)
blocks=[p('d) Rectangular-matrix'),p('A matrix whose number of rows and number of columns are not equal is called rectangular matrix. Thus the matrix'),
 m([['a','b','c'],['d','e','f']],suffix='is a rectangular matrix because its number of rows = 2 = m and its number of Columns = 3 = n obviously 2 ≠ 3. Similarly the matrix'),
 m([[1,4],[3,2],[5,-3]],suffix='is also a rectangular matrix with its order 3-by-2 i.e. number of rows and number of columns are not equal.'),
 p('e) Zero matrix or Null matrix'),
 p('Any matrix (weather it is rectangular or square) of which all the elements (entries) are equal to zero is said to be a Zero matrix or a Null matrix. Thus'),
 dict(type='matrixProduct',matrices=[[[0,0],[0,0]],[[0,0,0],[0,0,0]],[[0],[0],[0]],[[0,0,0],[0,0,0],[0,0,0]]],operators=[',',',','and'],suffix='are some examples of zero matrices or null matrices.'),
 p('The following points are very important to remember.'),p('i) A zero or null matrix is not necessarily a square matrix.'),
 p('ii) A null matrix is generally donated by O.'),p('iii) Sometimes we prefer to put the order of a null matrix as a proper subscript with the general symbol O.'),p('Thus,'),
 m([[0,0],[0,0]],'O₂ₓ₂ =','is a null-matrix of order 2.'),m([[0,0,0],[0,0,0]],'O₂ₓ₃ =','is a null-matrix of order 2-by-3.'),
 p('The role of the Zero matrix in matrix manipulation is very similar to that of Zero in ordinary algebra. Provided that they are compatible for multiplication (compatibility of multiplication in matrices will be discussed later on in this chapter), the product of any matrix and the Zero matrix is a zero matrix. When working with matrices involving zero matrices, we choose a zero matrix of such an order which is suitable for solving the problem in hand.')]
save(dict(pdfPage=12,printedPage=8,page=8,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='Rectangular-matrix / Zero matrix or Null matrix',sections=[dict(id='1.2',title='1.2 Types of Matrices',blocks=blocks)],
 visualStatus='Matrices and callout text fully structured; calculator cartoon decorative',
 sourceErrata=[dict(kind='printed wording',text='“weather” and “donated” retained from the source wording.')]))
render(13)
