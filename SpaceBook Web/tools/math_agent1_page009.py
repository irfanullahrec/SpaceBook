from math_agent1_sequential import save, render, crop
def p(text): return dict(type='paragraph',text=text)
def m(rows,prefix='',suffix=''): return dict(type='matrixProduct',prefix=prefix,matrices=[rows],suffix=suffix)
src=crop(9,'printed005-equality-equity.png',(0.443,0.472,0.835,0.675))
example=dict(id='ex1',number=1,title='Example 1 (Printed page 5)',sourcePdfPage=9,sourcePrintedPage=5,
 problem='Write the number of rows and column of the following matrices and hence mention their orders:\n(i) A = [[p, q], [r, s]]\n(ii) B = [[3, 4, 7], [5, 6, 8]]',
 given='',method='',steps=[
 '(i) Given A = [[p, q], [r, s]], we see that:\nA has two rows and two columns, so order of A is 2-by-2, sometimes we will prefer to write the order of A is 2 by 2. Thus A is 2 by 2 matrix.',
 '(ii) Given B = [[3, 4, 7], [5, 6, 8]]\nB has two rows and three columns. The order of B is 2-by-3, or 2 by 3 i.e. B is a 2 by 3 matrix.'],
 answer='',solutionOrigin='textbook',subquestions=[dict(number='i',matrix=[['p','q'],['r','s']]),dict(number='ii',matrix=[[3,4,7],[5,6,8]])])
blocks=[p('Example 1'),p(example['problem']),p('Solution:'),*[p(step) for step in example['steps']],
 m([[2,-5,10],[-4,19,4]],suffix='Illustrative matrix beside Example 1.'),
 p('1.1.4 Equality of two Matrices'),p('Two given matrices A and B are said to be equal if:'),
 p('(i) Both the matrices are of the same order i.e. they respectively have the same number of rows and columns.'),
 p('(ii) The elements in the corresponding positions in A and B are equal.'),
 dict(type='figure',src=src,alt='Two panels showing equal-height supports and different-height supports beneath people reaching trees.',caption='Equality doesn’t mean Equity'),
 p('For example, the matrices'),
 dict(type='matrixProduct',matrices=[[[1,2,3],[6,5,4]],[['1','1+1','12/4'],['4+2','10/2','8/2']]],operators=['and'],suffix='are equal whereas the matrices'),
 dict(type='matrixProduct',matrices=[[[1,2],[3,4],[5,6]],[[1,2,3],[6,5,4]]],operators=['and'],suffix='are not equal.')]
save(dict(pdfPage=9,printedPage=5,page=5,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='Example 1 / 1.1.4 Equality of two Matrices',workedExamples=[example],sections=[dict(id='1.1',title='1.1 Introduction to Matrices',blocks=blocks)],
 visualStatus='Equality/equity illustration retained as source crop; matrices structured separately; original example and solution stored separately'))
render(10)
