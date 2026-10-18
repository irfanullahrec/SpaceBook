from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: reviewed project exercise');os.close(fd)
try:
    path=ROOT/'js/app.js';text=path.read_bytes().decode('utf-8')
    start=text.index('function renderClass12PhysicsSourceExercises(')
    end=text.index('\nfunction ',start+1)
    segment=text[start:end]
    segment=segment.replace("['assignment-11-1','quiz-printers-11']","['assignment-11-1','quiz-printers-11','project-gaussian-11']",1)
    old="item.id === 'assignment-11-1' ? 'phys12-front-assignment111' : 'phys12-front-inkjet13'"
    new="({'assignment-11-1':'phys12-front-assignment111','quiz-printers-11':'phys12-front-inkjet13','project-gaussian-11':'phys12-front-project25'})[item.id]"
    assert segment.count(old)==1
    segment=segment.replace(old,new)
    segment=segment.replace("const source = item.id === 'assignment-11-1' ? section :", "const source = item.id !== 'quiz-printers-11' ? section :",1)
    path.write_bytes((text[:start]+segment+text[end:]).encode('utf-8'))
finally:
    lock.unlink()
