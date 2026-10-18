from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: example11.5 and assignment11.2 views');os.close(fd)
try:
    path=ROOT/'js/app.js';text=path.read_bytes().decode('utf-8')
    for function in ['renderClass12PhysicsWorkedExamples','renderClass12PhysicsSourceExercises']:
        start=text.index('function '+function+'(');end=text.index('\nfunction ',start+1);segment=text[start:end]
        if function.endswith('WorkedExamples'):
            old="'textbook-example-3': ['phys12-front-example113']"
            new=old+",\n    'textbook-example-5': ['phys12-front-example115']"
            if '\r\n' in text:new=new.replace('\n','\r\n')
        else:
            old="['assignment-11-1','quiz-printers-11','project-gaussian-11']"
            new="['assignment-11-1','quiz-printers-11','project-gaussian-11','assignment-11-2']"
            segment=segment.replace("'project-gaussian-11':'phys12-front-project25'","'project-gaussian-11':'phys12-front-project25','assignment-11-2':'phys12-front-assignment112'",1)
        assert segment.count(old)==1
        segment=segment.replace(old,new)
        text=text[:start]+segment+text[end:]
    path.write_bytes(text.encode('utf-8'))
finally:
    lock.unlink()
