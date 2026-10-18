from math_agent1_sequential import save, render
def p(text): return dict(type='paragraph',text=text)
def m(rows,prefix='',suffix=''): return dict(type='matrixProduct',prefix=prefix,matrices=[rows],suffix=suffix)
blocks=[p('a) Row-matrix'),p('A matrix which has just one and only row in it is called a Row-matrix.'),
 p('For example, the matrices'),dict(type='matrixProduct',matrices=[[['a','b']],[[1,3,4]],[[2,4,6,8]]],operators=[',',','],suffix='are all row-matrices.'),
 p('b) Column-matrix'),p('A matrix which has just one and only one column in it is called a column-matrix.'),p('For example,'),
 dict(type='matrixProduct',matrices=[[['a'],['b']],[[1],[3],[5]],[[2],[4],[6],[8]]],operators=[',','and'],suffix='are all column matrices.'),
 p('c) Square-matrix'),p('A matrix in which number of rows and columns are equal is called a square matrix. For example the matrix'),
 m([['l','m'],['n','p']],suffix='has two rows and two columns, so it is a square matrix. The order of the matrix'),
 m([['l','m'],['n','p']],suffix='is 2-by-2 but for brevity we write the above matrix as a square matrix of order 2 or 2-square matrix. Similarly'),
 m([[1,2,3],[7,8,9],[-1,-4,2]],'the matrix',suffix='is a square matrix of order 3 or 3-square matrix. As a special case the matrix consisting of a single element say [3] is also a square matrix of order 1 or a 1-square matrix.'),
 p('Remember'),m([[1,3,4]],suffix='Row matrix.'),m([[1],[3],[4]],suffix='Column matrix.'),m([[1,3,4],[3,1,4],[4,1,3]],suffix='Square matrix.')]
save(dict(pdfPage=11,printedPage=7,page=7,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='1.2 TYPES OF MATRICES',sections=[dict(id='1.2',title='1.2 Types of Matrices',blocks=blocks)],
 visualStatus='All sample matrices and Remember box rebuilt as structured matrices; cartoon is decorative'))
render(12)
