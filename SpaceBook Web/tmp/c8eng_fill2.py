import re,sys
sys.path.insert(0,'tmp')
exec(open('D:/SpaceBook/SpaceBook Web/tmp/c8eng_fill.py',encoding='utf8').read().split('ins(\'020\'')[0])
def S(a,why): return f"sol {a} ## {why} || درست جواب: {a} || سم ځواب: {a}"
ins('024',"q - | Write 'every'",{
 'a':S('Each','"Each of the" + plural noun: Each of the pupils lost their books.'),
 'b':S('every','"every" with a time expression gives a repeated point in a series: every 30 minutes.'),
 'c':S('each','"one of each" picks one from every bottle type; "each" with of/pronoun.'),
 'd':S('every','"every minute" sees the whole trip as a series of minutes.'),
 'e':S('Each','"Each student" means every student seen individually.'),
 'f':S('Every','"Every time" is a fixed expression.'),
 'g':S('each','"cost ... each" means the price of one bag.'),
 'h':S('every','"every day except Friday" speaks about the whole series of days.'),
 'i':S('Each','"Each of them" takes "of" with a plural pronoun.'),
 'j':S('Every','"Every evening" is a repeated time expression.')})
ins('028','q 1 | Underline',{
 'a':S('kind, selfish, ulterior','kind, selfish and ulterior all describe nouns or the subject: descriptive adjectives.'),
 'b':S('successful, some, false, some, true','successful, false and true are descriptive; "some" is a numeral adjective of quantity.'),
 'c':S('honest, frank','honest and frank are descriptive adjectives.'),
 'd':S('none','"years" is a noun and "overnight" is an adverb; the line has no adjective.')})
ins('028','q 2 | Complete',{
 'a':S('Her (possessive adjective)','Her character is ideal. Other suitable answers: This (demonstrative), A noble (descriptive).'),
 'b':S('Which (interrogative adjective)','Which method is easier? It asks a question and is followed by a noun.'),
 'c':S('ten (numeral adjective)','"ten people" tells the number of people.'),
 'd':S('one (numeral adjective)','"We are one nation": it gives the number. A descriptive answer such as "a united" also fits.'),
 'e':S('talented (descriptive adjective)','He is a talented singer: it describes the noun.'),
 'f':S('her (possessive adjective)','She came with her mission: it shows ownership.'),
 'g':S('one (numeral adjective)','only one fits me: it gives the quantity. (Used as a pronoun here.)')})
ins('029','@printed',{
 'h':S('This (demonstrative adjective)','"This time" points to a particular time.'),
 'i':S('Which (interrogative adjective)','Which books are you reading? It asks a question.'),
 'j':S('your (possessive adjective)','I could not understand your intention: it shows ownership. Other suitable answers: his, her, their.')})
