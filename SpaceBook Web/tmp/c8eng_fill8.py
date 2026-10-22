import re
exec(open('D:/SpaceBook/SpaceBook Web/tmp/c8eng_fill5.py',encoding='utf8').read().split("addq('039'")[0])
exec(open('D:/SpaceBook/SpaceBook Web/tmp/c8eng_fill.py',encoding='utf8').read().split("ins('020'")[0])
def M(a,why='One possible answer.'): return f"sol {a} ## {why}"
def fill(page,pairs):
    f=f'p{page}.txt'; t=open(f,encoding='utf8').read()
    for old,new in pairs:
        pat=re.compile(re.escape(old)+r'[ ]*\|?[ ]*(\n|$)',re.M)
        assert pat.search(t),old
        t=pat.sub(lambda m:new+m.group(1),t,count=1)
    open(f,'w',encoding='utf8',newline='\n').write(t)
S=lambda t:M(t)
sp={'1':S("Model answer: They speak politely and listen to each other, share their ideas, say thank you and sorry, and respect each other's feelings and differences."),
 '2':S('Model answer: Low-maintenance relationships need little effort because the people understand each other easily. For harder relationships I try to listen carefully, stay patient and talk calmly about problems.'),
 '3':S('Model answer: An argument can end well if both sides listen, accept that each may be partly right, and find a middle way. Then nobody loses and the friendship stays strong.')}
ins('002','@status',sp)
ins('016','@printed',sp)
ins('023','@printed',{
 'A':S('Model answer: Yes, a classmate was teased about his appearance and nobody helped him; I remember how sad and alone he felt.'),
 'B':S('Model answer: They can tell a teacher or parent, stay with friends, stay calm and not fight back, and report the bullying so that it can be stopped.'),
 'C':S('Model answer: Some bystanders are afraid the bully will turn on them, some think it is not their problem, and some do not know what to do. We can help by speaking up safely, supporting the victim and telling an adult.')})
ins('023','q - | Answer the questions',{
 'A':S('Model answer: The purpose of the poem is to show how hurtful bullying is and to encourage kindness and respect.'),
 'B':S('Model answer: Bullying makes people feel sad, afraid, lonely and worthless.')})
ins('024','@printed',{
 'C':S('Model answer: I can be kind to everyone, refuse to join in teasing, stand by the person being bullied and tell a teacher.'),
 'D':S('Model answer: The poem tells us that bullying hurts people deeply and that we should treat others with kindness and respect.')})
addq('056','q 1 | In groups','sol Model answer: genre - adventure; plot-line - three friends find an old map, follow clues, face a problem on a river and solve it by working together; characters - Ali (brave), Sana (clever), Hamza (careful) and a guide; setting - the forests and rivers of northern Pakistan. Each character speaks some dialogue, e.g. "Let us check the map again," said Sana. ## Group activity; one possible plan.')
addq('056','q 2 | In pairs','sol Model answer: Retell the chosen story in your own words with a clear beginning, middle and end, vary your voice, use pauses and gestures, and look at the audience. ## Speaking activity; no written answer is fixed.')
addq('060','q 1 | Create your own story','sol Model table: title - The Honest Woodcutter; characters - a woodcutter, a river spirit; setting - a forest by a river; problem - his axe falls into the river; solution - the spirit offers gold and silver axes but he asks only for his own; moral - honesty is rewarded. ## One possible plan.')
addq('074','q 1 | Do you think','sol Model answer: Yes, in some places girls still have fewer chances for education and jobs. We can reduce this by sending all children to school, speaking up against unfair treatment, and giving girls and boys equal respect at home. ## Opinion; one possible answer.')
addq('074','q 2 | Discuss in pairs','sol Model answer: With gender equality everywhere, more girls would be educated, families would have more income, and countries would grow faster. People of both genders would share work and decisions. ## Discussion; one possible answer.')
addq('078','q 2 | Write the suffix','sol defenseless - The lost kitten was defenseless. finally - Finally, we reached home. swiftly - The horse ran swiftly. anxiously - She waited anxiously. blindness - Blindness did not stop him from learning. instantaneously - The light went on instantaneously. quickly - Walk quickly. illness - His illness lasted a week. joyfully - The children played joyfully. ## One sentence for each word with its suffix.')
