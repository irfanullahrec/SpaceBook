import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from gm import *
pages={}
def P(en,ur,ps):return f'p {en} || {ur} || {ps}\n'
def EX(n,en,ur,ps):return f'example {n} | {en} || {ur} || {ps}\n'
S=lambda:P('**Solution:**','**حل:**','**حل:**')
pages[299]=r'''@printed 299
@deco Unit-running header, folio and decorative footer band excluded
m $\cos\dfrac\theta2=\pm\sqrt{\dfrac{1+\cos\left(2\cdot\frac\theta2\right)}2}$
m $\cos\dfrac\theta2=\pm\sqrt{\dfrac{1+\cos\theta}2}\qquad(10)$
'''+P(r'From (9) and (10), we have $\tan\dfrac\theta2=\dfrac{\sin\frac\theta2}{\cos\frac\theta2}=\pm\sqrt{\dfrac{1-\cos\theta}{1+\cos\theta}}$.',r'(9) اور (10) سے ہمیں $\tan\dfrac\theta2=\dfrac{\sin\frac\theta2}{\cos\frac\theta2}=\pm\sqrt{\dfrac{1-\cos\theta}{1+\cos\theta}}$ ملتا ہے۔',r'د (9) او (10) نه موږ لرو $\tan\dfrac\theta2=\dfrac{\sin\frac\theta2}{\cos\frac\theta2}=\pm\sqrt{\dfrac{1-\cos\theta}{1+\cos\theta}}$.')+r'''m $\tan\dfrac\theta2=\pm\sqrt{\dfrac{1-\cos\theta}{1+\cos\theta}}\qquad(11)$
'''+EX(9,r'Find $\tan(\pi/8)$ exactly.',r'$\tan(\pi/8)$ کی صحیح قیمت معلوم کریں۔',r'د $\tan(\pi/8)$ دقیق ارزښت پیدا کړئ.')+S()+r'''m $\tan\dfrac\pi8=\tan\left(\dfrac{\frac\pi4}2\right)=\sqrt{\dfrac{1-\cos\frac\pi4}{1+\cos\frac\pi4}}=\sqrt{\dfrac{1-\frac1{\sqrt2}}{1+\frac1{\sqrt2}}}=\sqrt{\dfrac{\sqrt2-1}{\sqrt2+1}}=\sqrt{\dfrac{\sqrt2(\sqrt2-1)}{\sqrt2(\sqrt2+1)}}=\sqrt{\dfrac{2-\sqrt2}{2+\sqrt2}}$
m $=\sqrt{\dfrac{2-\sqrt2}{2+\sqrt2}\cdot\dfrac{2-\sqrt2}{2-\sqrt2}}=\sqrt{\dfrac{4-2\sqrt2-2\sqrt2+2}{4-2}}=\sqrt{\dfrac{6-4\sqrt2}2}=\sqrt{3-2\sqrt2}$
endexample
'''+P('The identities that we have developed are also useful for simplifying trigonometric expressions.','ہماری اخذ کی ہوئی مماثلتیں مثلثیاتی اظہارات کو سادہ بنانے کے لیے بھی مفید ہیں۔','هغه هویتونه چې موږ پیدا کړي دي د مثلثاتي عبارتونو د ساده کولو لپاره هم ګټور دي.')+EX(10,r'Simplify each of the following. a) $\dfrac{\sin x\cos x}{\frac12\cos2x}$ b) $2\sin^2\dfrac x2+\cos x$',r'ہر ایک کو سادہ کریں۔ a) $\dfrac{\sin x\cos x}{\frac12\cos2x}$ b) $2\sin^2\dfrac x2+\cos x$',r'هر یو ساده کړئ. a) $\dfrac{\sin x\cos x}{\frac12\cos2x}$ b) $2\sin^2\dfrac x2+\cos x$')+S()+r'''m $\text{a) }\dfrac{\sin x\cos x}{\frac12\cos2x}=\dfrac22\cdot\dfrac{\sin x\cos x}{\frac12\cos2x}=\dfrac{2\sin x\cos x}{\cos2x}=\dfrac{\sin2x}{\cos2x}=\tan2x\quad(\text{using }\sin2x=2\sin x\cos x)$
m $\text{b) }2\sin^2\dfrac x2+\cos x=2\left(\dfrac{1-\cos x}2\right)+\cos x=1-\cos x+\cos x=1\quad\left(\text{using }\sin^2\dfrac x2=\dfrac{1-\cos x}2\right)$
endexample
'''
pages[300]=r'''@printed 300
@sec 10.3.3 | Triple Angle Identities || تہرے زاویے کی مماثلتیں || د درې چنده زاویې هویتونه
@deco Unit-running header, folio and decorative footer band excluded
### 10.3.3. Triple Angle Identities || 10.3.3۔ تہرے زاویے کی مماثلتیں || 10.3.3. د درې چنده زاویې هویتونه
'''+P(r'We have $\sin3\alpha=\sin(2\alpha+\alpha)=\sin2\alpha\cos\alpha+\cos2\alpha\sin\alpha$',r'ہمارے پاس ہے $\sin3\alpha=\sin(2\alpha+\alpha)=\sin2\alpha\cos\alpha+\cos2\alpha\sin\alpha$',r'موږ لرو $\sin3\alpha=\sin(2\alpha+\alpha)=\sin2\alpha\cos\alpha+\cos2\alpha\sin\alpha$')+r'''m $=2\sin\alpha\cos\alpha\cos\alpha+(1-2\sin^2\alpha)\sin\alpha\qquad(\text{By (3) and (5)})$
m $=2\sin\alpha\cos^2\alpha+\sin\alpha-2\sin^3\alpha$
m $=2\sin\alpha(1-\sin^2\alpha)+\sin\alpha-2\sin^3\alpha\qquad(\because\sin^2\alpha+\cos^2\alpha=1)$
m $=2\sin\alpha-2\sin^3\alpha+\sin\alpha-2\sin^3\alpha=3\sin\alpha-4\sin^3\alpha$
m $\therefore\ \sin3\alpha=3\sin\alpha-4\sin^3\alpha\qquad(12)$
m $\cos3\alpha=\cos(2\alpha+\alpha)=\cos2\alpha\cos\alpha-\sin2\alpha\sin\alpha=(2\cos^2\alpha-1)\cos\alpha-2\sin\alpha\cos\alpha\sin\alpha\qquad(\text{by (3) and (6)})$
m $=2\cos^3\alpha-\cos\alpha-2\sin^2\alpha\cos\alpha=2\cos^3\alpha-\cos\alpha-2(1-\cos^2\alpha)\cos\alpha\qquad(\because\sin^2\alpha+\cos^2\alpha=1)$
m $=2\cos^3\alpha-\cos\alpha-2\cos\alpha+2\cos^3\alpha=4\cos^3\alpha-3\cos\alpha$
m $\therefore\ \cos3\alpha=4\cos^3\alpha-3\cos\alpha\qquad(13)$
m $\tan3\alpha=\tan(2\alpha+\alpha)=\dfrac{\tan2\alpha+\tan\alpha}{1-\tan2\alpha\tan\alpha}=\dfrac{\frac{2\tan\alpha}{1-\tan^2\alpha}+\tan\alpha}{1-\frac{2\tan\alpha}{1-\tan^2\alpha}\cdot\tan\alpha}\qquad(\text{By (7)})$
m $=\dfrac{\frac{2\tan\alpha+\tan\alpha(1-\tan^2\alpha)}{1-\tan^2\alpha}}{\frac{1-\tan^2\alpha-2\tan^2\alpha}{1-\tan^2\alpha}}=\dfrac{3\tan\alpha-\tan^3\alpha}{1-3\tan^2\alpha}$
m $\therefore\ \tan3\alpha=\dfrac{3\tan\alpha-\tan^3\alpha}{1-3\tan^2\alpha}\qquad(14)$
'''+EX(11,r'Prove the identity $\dfrac{\sin2x}{\sin x}-\dfrac{\cos2x}{\cos x}=\sec x$.',r'مماثلت ثابت کریں $\dfrac{\sin2x}{\sin x}-\dfrac{\cos2x}{\cos x}=\sec x$۔',r'هویت ثابت کړئ $\dfrac{\sin2x}{\sin x}-\dfrac{\cos2x}{\cos x}=\sec x$.')+S()+r'''m $\dfrac{\sin2x}{\sin x}-\dfrac{\cos2x}{\cos x}=\dfrac{2\sin x\cos x}{\sin x}-\dfrac{\cos^2x-\sin^2x}{\cos x}\qquad(\text{using double-angle identities})$
'''
pages[301]=r'''@printed 301
@deco Unit-running header, folio and decorative footer band excluded
m $=2\cos x-\dfrac{\cos^2x-\sin^2x}{\cos x}\qquad(\text{simplifying})$
m $=\dfrac{2\cos^2x-\cos^2x+\sin^2x}{\cos x}\qquad(\text{taking LCM and simplifying})$
m $=\dfrac{\cos^2x+\sin^2x}{\cos x}=\dfrac1{\cos x}=\sec x$
'''+P('We started with the left side and obtained the right side, so the proof is complete.','ہم نے بائیں طرف سے آغاز کیا اور دائیں طرف حاصل کی، اس لیے ثبوت مکمل ہے۔','موږ له کیڼې خوا پیل وکړ او ښي خوا مو ترلاسه کړه، نو ثبوت بشپړ دی.')+'endexample\n'+EX(12,r'Prove the identity $\sin^2x\tan^2x=\tan^2x-\sin^2x$.',r'مماثلت ثابت کریں $\sin^2x\tan^2x=\tan^2x-\sin^2x$۔',r'هویت ثابت کړئ $\sin^2x\tan^2x=\tan^2x-\sin^2x$.')+P('**Solution:** For this proof, we are going to work with each side separately. We try to obtain the same expression on each side.','**حل:** اس ثبوت کے لیے ہم ہر طرف پر الگ الگ کام کریں گے۔ ہم ہر طرف سے ایک ہی اظہار حاصل کرنے کی کوشش کرتے ہیں۔','**حل:** د دې ثبوت لپاره موږ پر هرې خوا جلا کار کوو. موږ هڅه کوو چې له هرې خوا یو شان عبارت ترلاسه کړو.')+r'''m $\sin^2x\tan^2x=\sin^2x\left(\dfrac{\sin^2x}{\cos^2x}\right)=\dfrac{\sin^4x}{\cos^2x}\qquad\cdots(1)$
m $\tan^2x-\sin^2x=\dfrac{\sin^2x}{\cos^2x}-\sin^2x\qquad\left(\because\tan x=\dfrac{\sin x}{\cos x}\right)$
m $=\dfrac{\sin^2x-\sin^2x\cos^2x}{\cos^2x}\qquad(\text{Taking LCM})$
m $=\dfrac{\sin^2x(1-\cos^2x)}{\cos^2x}\qquad(\text{Factoring})$
m $=\dfrac{\sin^2x\sin^2x}{\cos^2x}\qquad(\text{Recalling the identity }1-\cos^2x=\sin^2x)$
m $=\dfrac{\sin^4x}{\cos^2x}\qquad\cdots(2)$
'''+P('We have obtained the same expression from each side, so the proof is complete.','ہم نے ہر طرف سے ایک ہی اظہار حاصل کیا ہے، اس لیے ثبوت مکمل ہے۔','موږ له هرې خوا یو شان عبارت ترلاسه کړ، نو ثبوت بشپړ دی.')+'endexample\n'+EX(13,r'Find the exact value of $\cos105^\circ$.',r'$\cos105^\circ$ کی صحیح قیمت معلوم کریں۔',r'د $\cos105^\circ$ دقیق ارزښت پیدا کړئ.')+P(r'**Solution:** Because $105^\circ=\dfrac12(210^\circ)$ we can find $\cos105^\circ$ by using the half-angle identity for $\cos\alpha/2$ with $\alpha=210^\circ$. The angle $\alpha/2=105^\circ$ lies in Quadrant II, and the cosine function is negative in Quadrant II. Thus $\cos105^\circ<0$, and we must select',r'**حل:** چونکہ $105^\circ=\dfrac12(210^\circ)$ ہے ہم $\alpha=210^\circ$ کے ساتھ $\cos\alpha/2$ کی نصف زاویے کی مماثلت سے $\cos105^\circ$ معلوم کر سکتے ہیں۔ زاویہ $\alpha/2=105^\circ$ دوسرے ربع میں واقع ہے اور کوسائن تفاعل دوسرے ربع میں منفی ہے۔ یوں $\cos105^\circ<0$ ہے اور ہمیں منتخب کرنا ہوگا',r'**حل:** ځکه چې $105^\circ=\dfrac12(210^\circ)$ دی موږ کولای شو د $\alpha=210^\circ$ سره د $\cos\alpha/2$ د نیمایي زاویې هویت په کارولو سره $\cos105^\circ$ پیدا کړو. زاویه $\alpha/2=105^\circ$ په دویم ربع کې ده او کوساین تابع په دویم ربع کې منفي دی. په دې توګه $\cos105^\circ<0$ دی او موږ باید وټاکو')
pages[302]=r'''@printed 302
@issue This page is a low-quality (blurred) photograph; Example 15 (ii) is read as the standard identity sin4θ = 4 sinθ cos³θ − 4 sin³θ cosθ.
@deco Unit-running header, folio and decorative footer band excluded
'''+P(r'the minus sign that precedes the radical in $\cos\alpha=\pm\sqrt{\dfrac{1+\cos\alpha}2}$ to produce the correct result.',r'وہ منفی علامت جو $\cos\alpha=\pm\sqrt{\dfrac{1+\cos\alpha}2}$ میں جذر سے پہلے آتی ہے تاکہ درست نتیجہ حاصل ہو۔',r'هغه منفي نښه چې په $\cos\alpha=\pm\sqrt{\dfrac{1+\cos\alpha}2}$ کې له جذر مخکې راځي ترڅو سمه پایله ترلاسه شي.')+r'''m $\cos105^\circ=-\sqrt{\dfrac{1+\cos210^\circ}2}=-\sqrt{\dfrac{1+\left(-\frac{\sqrt3}2\right)}2}=-\sqrt{\dfrac{\frac{2-\sqrt3}2}2}=-\sqrt{\dfrac{2-\sqrt3}4}$
endexample
'''+EX(14,r'Show that $\sin^4\theta=\dfrac38-\dfrac12\cos2\theta+\dfrac18\cos4\theta$',r'دکھائیں کہ $\sin^4\theta=\dfrac38-\dfrac12\cos2\theta+\dfrac18\cos4\theta$',r'وښایاست چې $\sin^4\theta=\dfrac38-\dfrac12\cos2\theta+\dfrac18\cos4\theta$')+r'''p **Solution:** L.H.S $=\sin^4\theta=(\sin^2\theta)^2$ || **حل:** بایاں طرف $=\sin^4\theta=(\sin^2\theta)^2$ || **حل:** کیڼه خوا $=\sin^4\theta=(\sin^2\theta)^2$
m $=\left(\dfrac{1-\cos2\theta}2\right)^2\qquad\left(\because\sin^2\theta=\dfrac{1-\cos2\theta}2\right)$
m $=\dfrac{1-2\cos2\theta+\cos^22\theta}4=\dfrac14[1-2\cos2\theta+\cos^22\theta]$
m $=\dfrac14\left[1-2\cos2\theta+\dfrac{1+\cos4\theta}2\right]\qquad\left(\because\cos^22\theta=\dfrac{1+\cos4\theta}2\right)$
m $=\dfrac14\left[\dfrac{2-4\cos2\theta+1+\cos4\theta}2\right]=\dfrac18[3-4\cos2\theta+\cos4\theta]$
m $=\dfrac38-\dfrac48\cos2\theta+\dfrac18\cos4\theta=\dfrac38-\dfrac12\cos2\theta+\dfrac18\cos4\theta=\text{R.H.S.}$
endexample
'''+EX(15,r'Prove the following identities. (i) $\sin2\theta=\dfrac{2\tan\theta}{1+\tan^2\theta}$ (ii) $\sin4\theta=4\sin\theta\cos^3\theta-4\sin^3\theta\cos\theta$',r'درج ذیل مماثلتیں ثابت کریں۔ (i) $\sin2\theta=\dfrac{2\tan\theta}{1+\tan^2\theta}$ (ii) $\sin4\theta=4\sin\theta\cos^3\theta-4\sin^3\theta\cos\theta$',r'لاندې هویتونه ثابت کړئ. (i) $\sin2\theta=\dfrac{2\tan\theta}{1+\tan^2\theta}$ (ii) $\sin4\theta=4\sin\theta\cos^3\theta-4\sin^3\theta\cos\theta$')+P(r'**Solution:** (i) R.H.S $=\dfrac{2\tan\theta}{1+\tan^2\theta}=2\dfrac{\tan\theta}{\sec^2\theta}\ \ (\because\tan^2\theta+1=\sec^2\theta)$ $=2\tan\theta\cos^2\theta\ \ \left(\because\cos\theta=\dfrac1{\sec\theta}\right)$',r'**حل:** (i) دایاں طرف $=\dfrac{2\tan\theta}{1+\tan^2\theta}=2\dfrac{\tan\theta}{\sec^2\theta}\ \ (\because\tan^2\theta+1=\sec^2\theta)$ $=2\tan\theta\cos^2\theta\ \ \left(\because\cos\theta=\dfrac1{\sec\theta}\right)$',r'**حل:** (i) ښي خوا $=\dfrac{2\tan\theta}{1+\tan^2\theta}=2\dfrac{\tan\theta}{\sec^2\theta}\ \ (\because\tan^2\theta+1=\sec^2\theta)$ $=2\tan\theta\cos^2\theta\ \ \left(\because\cos\theta=\dfrac1{\sec\theta}\right)$')
for n,t in pages.items():
    open(f'{OUT}\\p{n}.txt','w',encoding='utf8').write(t)
print('ok')
