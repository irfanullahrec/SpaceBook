exec(open('D:/SpaceBook/SpaceBook Web/tmp/c8eng_fill.py',encoding='utf8').read().split("ins('020'")[0])
def M(a,why): return f"sol {a} ## {why}"
ins('026','q B | Match',{
 'a':M('Be honest and frank anyway.','The poem answers "people may cheat you" with "Be honest and frank anyway."'),
 'b':M('Build anyway.','The poem answers "someone could destroy it overnight" with "Build anyway."')})
ins('027','@printed',{
 'c':M('If you are successful, you will win some false friends and some true enemies.','"Succeed anyway" answers the warning about false friends and true enemies.'),
 'd':M('If you find serenity and happiness, they may be jealous.','"Be happy anyway" answers the warning that others may be jealous.'),
 'e':M('Be kind anyway.','"Be kind anyway" answers the accusation of selfish ulterior motives.')})
ins('026','q A | Answer',{
 '1':M('Model answer: The poem teaches us to do good, be honest, kind and generous even when people are ungrateful, unfair or forget our kindness, because in the end our actions are between us and God.','Message: do right regardless of how others react; one possible answer.'),
 '2':M('Model answer: Many readers find it hardest to keep being kind or to keep building when others criticise, accuse or destroy our work, because it needs patience and a strong heart.','Personal opinion; one possible answer.'),
 '3':M('Model answer: Being honest, giving our best and being happy are easier for me, because they depend on my own choices and not on what other people do.','Personal opinion with a reason; one possible answer.'),
 '4':M('Model answer: (a) Even if our best effort is not appreciated, we should still give it, because effort has value in itself. (b) Do good without expecting thanks, since people forget kindness quickly. (c) Our final judgement is with God, so we should act sincerely instead of worrying about people.','Interpretation of each phrase; one possible answer.')})
