import re
exec(open('D:/SpaceBook/SpaceBook Web/tmp/c8eng_fill.py',encoding='utf8').read().split("ins('020'")[0])
def M(a,why): return f"sol {a} ## {why}"
t=open('p078.txt',encoding='utf8').read()
for w,s in [('defense','-less (defenseless)'),('final','-ly (finally)'),('swift','-ly (swiftly)'),('anxious','-ly (anxiously)'),('blind','-ness (blindness)'),('instantaneous','-ly (instantaneously)'),('quick','-ly (quickly)'),('ill','-ness (illness)'),('joyful','-ly (joyfully)')]:
    suf,new=s.split(' (')
    t,n=re.subn(r'(tr \| [a-i] '+w+r' \|)[ ]*\|[ ]*(\n|$)',lambda m:m.group(1)+' '+suf+' | '+new[:-1]+m.group(2),t,count=1,flags=re.M); assert n==1,w
open('p078.txt','w',encoding='utf8',newline='\n').write(t)
ins('091','q 1 | Fill the statements',{'a':M('humanoid','a robot that closely resembles a human is a humanoid'),'b':M('therapeutic','gardening that relaxes and calms is therapeutic'),'c':M('automation','automation = using machines in industries')})
ins('057','q - | Find out the meaning',{'a':M('Distraught','distraught = very upset; the farmer was distraught after the neighbour refused him water'),
 'b':M('cunning','cunning = clever in a deceitful way'),'c':M('emperor ... courtiers','"The emperor called on Birbal, one of his nine, and wisest courtiers"'),'d':M('scheme','scheme = a secret plan; the neighbour\'s scheme failed')})
ins('065','q - | Fill in the blanks with the appropriate',{'1':M('gilded ... thin','"He was gilded all over with thin leaves of fine gold" (gilded is not in the bank)'),
 '2':M('Sans-Souci ... sorrow','"the Palace of Sans-Souci, where sorrow is not allowed to enter"'),
 '3':M('plucked ... ruby','the swallow plucked out the great ruby from the Prince\'s sword'),
 '4':M('match girl ... jewel','He swooped past the match girl and slipped the jewel into her hand'),
 '5':M('melt','"This broken lead heart will not melt in the furnace"')})
