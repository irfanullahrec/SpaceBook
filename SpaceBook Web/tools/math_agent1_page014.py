from math_agent1_sequential import save, render
def p(text): return dict(type='paragraph',text=text)
def m(rows,prefix='',suffix=''): return dict(type='matrixProduct',prefix=prefix,matrices=[rows],suffix=suffix)
blocks=[p('Note: Every scalar matrix is a diagonal matrix but every diagonal matrix is not necessarily a scalar matrix. For example,'),
 m([[4,0,0],[0,3,0],[0,0,-1]],suffix='is a diagonal matrix,'),
 p('because all elements of the matrix are zero except the elements of the main diagonal but the above matrix is not a scalar matrix because elements lying on the main diagonal are not all equal.'),
 p('h) Identity matrix'),
 p('The identity matrix (sometimes called the unit matrix) is a square matrix and is denoted by I. It is characterized by the fact that all elements on its main diagonal are 1’s whereas all other elements are zero. Sometime it is useful to write the order of the identity matrix as a subscript of I. thus'),
 m([[1,0],[0,1]],'I₂ =','is the identity matrix of order 2.'),
 m([[1,0,0],[0,1,0],[0,0,1]],'I₃ =','is the identity matrix of order 3.'),
 p('When there is no danger of ambiguity the identity matrices I₂ & I₃ are simply denoted by I.'),
 p('i) Transpose of a matrix'),
 p('Suppose we have a matrix A of any given order. The matrix obtained by interchanging mutually the rows and columns in A is called the transpose of A and is denoted by Aᵗ. For example'),
 m([[1,2],[3,4]],'If A ='),m([[1,3],[2,4]],'then Aᵗ =')]
save(dict(pdfPage=14,printedPage=10,page=10,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='Scalar matrix note / Identity matrix / Transpose of a matrix',sections=[dict(id='1.2',title='1.2 Types of Matrices',blocks=blocks)],
 visualStatus='All matrices and callout text structured; identity cartoon decorative'))
render(15)
