import json, subprocess
from math_agent1_sequential import save, render, ROOT
# Read the existing seven questions, then verify/update against this one source page.
code="const fs=require('fs'),vm=require('vm');let c={};vm.createContext(c);vm.runInContext(fs.readFileSync(process.argv[1],'utf8'),c);console.log(JSON.stringify(c.MATH_DATA[0].exercises.find(e=>e.exercise==='1.1')));"
exercise=json.loads(subprocess.check_output(['node','-e',code,str(ROOT/'js/math_data.js')],text=True,encoding='utf-8'))
exercise.update(title='Exercise 1.1 (Printed page 6)',sourcePdfPages=[10],sourcePrintedPages=[6])
assert len(exercise['problems'])==7
matrices=[
 [('i','A',[[2,3],[0,5]]),('ii','B',[[6,3,-1],[1,5,2]]),('iii','C',[[1,0,0],[0,2,0],[0,0,1]]),('iv','B',[[-5]]),('v','E',[[-3,4]]),('vi','E',[[-1],[7]])],
 [('i','A',[[1,2,-1],[3,4,2]]),('ii','B',[[-4]]),('iii','C',[[2,3,-1],[1,2,5]]),('iv','F',[[2,1],[3,2],[4,-1]]),('v','E',[[3,2]]),('vi','D',[[1,2,3],[6,5,9],[0,0,0]])]
]
for i,problem in enumerate(exercise['problems'],1):
    problem.update(id=f'u1-ex1.1-q{i}',number=i,sourcePdfPage=10,sourcePrintedPage=6,solutionOrigin='SpaceBook supplementary solution; not printed on this source page',answerOrigin='SpaceBook supplementary answer; original answer key not yet reviewed')
    problem['solution']='SpaceBook supplementary solution (not printed on this exercise page):\n'+problem['solution']
    if i<=2: problem['subquestions']=[dict(number=n,label=label,matrix=rows) for n,label,rows in matrices[i-1]]
    if i==3:
        problem['givenMatrix']=[[3,2,-4],[-2,5,0],[2,1,5],[-3,4,6]]
        problem['subquestions']=[dict(number=n,element=value) for n,value in zip(['i','ii','iii','iv','v','vi'],['a_12','a_23','a_32','a_43','a_13','a_33'])]
        problem['answer']='(i) 2, (ii) 0, (iii) 1, (iv) 6, (v) -4, (vi) 5.'
    if i==4: problem['question']=problem['question'].replace('are equal?','are equal.')
    if i==5: problem['question']='Let A = [[2, -3], [u, 0]] and B = [[v, -3], [5, w]], for what values of v, u and w are A and B equal.'
    if i==7: problem['question']='Solve the following equation for a, b, c, d.\n[[a+b, b+2c], [2c+d, 2a-d]] = [[-1, 4], [8, 0]]'
save(dict(pdfPage=10,printedPage=6,page=6,chapter='Unit 1: Matrices',status='completed-educational-content',
 title='Exercise 1.1',exercises=[exercise],visualStatus='All seven questions and matrix entries verified against source; original numbering and repeated matrix labels preserved',
 solutionStatus='No solutions printed on this page; existing mathematically checked supplementary solutions explicitly labelled'))
render(11)
