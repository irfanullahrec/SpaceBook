from math_agent1_sequential import save, render
rows = [
 [1,'Matrices',1], [2,'Real And Complex Numbers',50], [3,'Logarithm',75],
 [4,'Algebraic Expressions And Algebraic Formulas',97], [5,'Factorization',126],
 [6,'Algebraic Manipulation',149], [7,'Linear Equations and Inequalities',173],
 [8,'Linear Graphs And Their Applications',192], [9,'Introduction To Coordinate Geometry',210],
 [10,'Congruent Triangles',233], [11,'Parallelograms And Triangles',242],
 [12,'Line Bisectors And Angle Bisectors',256], [13,'Sides And Angles Of A Triangle',267],
 [14,'Ratio And Proportion',275], [15,"Pythagoras' Theorem",285],
 [16,'Theorems Related With Area',291], [17,'Practical Geometry Triangles',298],
 [None,'Answers',313]
]
save(dict(pdfPage=4,printedPage=None,page='contents',status='completed-front-matter',title='Contents',
 tables=[dict(headers=['Unit No.','Topic','Page No'],rows=rows)],visualStatus='Contents table faithfully transcribed'))
render(5)
