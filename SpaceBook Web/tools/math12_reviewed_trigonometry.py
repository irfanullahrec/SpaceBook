"""Printed 83–88, visually read against JPG and full PDF spreads 46–48."""
from math12_reviewed_unit1 import heading, paragraph, page, figure
from math12_reviewed_unit1 import command

def eq(text, number=None):
    return command(None, '\\(' + text + '\\)', number)

def note(text):
    return {'type':'clarification','text':text}

PAGES = []
PAGES.append(page('046_page_1.jpg',83,[
 heading('Derivative of sin x — continued'),
 eq(r'\Delta y=2\cos(x+\frac{\Delta x}2)\sin(\frac{\Delta x}2)'),
 paragraph('Now, divide equation by the Δx.'),
 eq(r'\frac{\Delta y}{\Delta x}=\frac{2\cos(x+\frac{\Delta x}2)\sin(\frac{\Delta x}2)}{\Delta x}'),
 paragraph('Now, apply the limit as Δx → 0 on both sides of equation.'),
 eq(r'\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\left[\cos(x+\frac{\Delta x}2)\frac{\sin(\frac{\Delta x}2)}{\frac{\Delta x}2}\right]'),
 eq(r'=\lim_{\Delta x\to0}\cos(x+\frac{\Delta x}2)\lim_{\Delta x\to0}\frac{\sin(\frac{\Delta x}2)}{\frac{\Delta x}2}=\cos(x+0)\cdot1=\cos x'),
 eq(r'\lim_{\Delta x\to0}\frac{\sin(\frac{\Delta x}2)}{\frac{\Delta x}2}=1,\quad\frac{\Delta x}2\to0\text{ as }\Delta x\to0'),
 paragraph('Hence,'), eq(r'\frac{dy}{dx}=\cos x'),
 heading('ii. Derivative of cos x'),paragraph(r'If y = cos x, then the derivative of y = cos x is \(\frac{dy}{dx}=-\sin x\).'),
 heading('Proof'),paragraph('By the rule of first principle. Let'),eq(r'y=\cos x'),eq(r'y+\Delta y=\cos(x+\Delta x),\quad y=f(x)'),
 paragraph('Subtracting equation from equation.'),eq(r'y+\Delta y-y=\cos(x+\Delta x)-\cos x'),eq(r'\Delta y=\cos(x+\Delta x)-\cos x'),
 eq(r'\Delta y=-2\sin(\frac{x+\Delta x+x}2)\sin(\frac{x+\Delta x-x}2)'),
 eq(r'\Delta y=-2\sin(x+\frac{\Delta x}2)\sin(\frac{\Delta x}2)'),
 eq(r'\cos\alpha-\cos\beta=-2\sin(\frac{\alpha+\beta}2)\sin(\frac{\alpha-\beta}2)'),
 paragraph('Now, divide equation by the Δx.'),
 eq(r'\frac{\Delta y}{\Delta x}=-2\sin(x+\frac{\Delta x}2)\frac{\sin(\frac{\Delta x}2)}{\Delta x}'),
 eq(r'\frac{\Delta y}{\Delta x}=-\sin(x+\frac{\Delta x}2)\frac{\sin(\frac{\Delta x}2)}{\frac{\Delta x}2}')
]))
PAGES.append(page('046_page_2.jpg',84,[
 heading('Derivative of cos x — continued'),paragraph('Now, apply the limit as Δx → 0 on both sides of equation.'),
 eq(r'\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=-\lim_{\Delta x\to0}\sin(x+\frac{\Delta x}2)\lim_{\Delta x\to0}\frac{\sin(\frac{\Delta x}2)}{\frac{\Delta x}2}'),
 eq(r'\lim_{\Delta x\to0}\frac{\sin(\Delta x)}{\Delta x}=1'),eq(r'=-\sin(x+0)\cdot1=-\sin x'),paragraph('Hence,'),eq(r'\frac{dy}{dx}=-\sin x'),
 heading('Do You Know?'),paragraph('The traffic police officers uses radar guns to take the advantage of the easy use of derivatives. When a radar gun is pointed and fired at a car on the motorway. The gun is able to determine the time and distance at which the radar was able to hit a certain section of the car with the use of derivative it is able to calculate the speed at which the car was going and also report the distance that the car was from the radar gun.'),
 dict(figure('radar-gun-source','Radar gun','Original radar-gun illustration from the page 84 information box'),displayWidth=150),
 note('This is the textbook explanation. A Doppler radar estimates radial speed from the frequency shift of the reflected signal; the rate-of-change idea relates displacement to velocity. The illustration belongs specifically to this information box.'),
 heading('iii. Derivative of tan x'),paragraph(r'If y = tan x, then the derivative of y = tan x is \(\frac{dy}{dx}=\sec^2x\).'),heading('Proof'),paragraph('By the rule of first principle. Let'),
 eq(r'y=\tan x'),eq(r'y+\Delta y=\tan(x+\Delta x)'),paragraph('Subtracting equation from equation.'),
 eq(r'y+\Delta y-y=\tan(x+\Delta x)-\tan x'),eq(r'\Delta y=\frac{\sin(x+\Delta x)}{\cos(x+\Delta x)}-\frac{\sin x}{\cos x}'),
 paragraph('Divide equation (iii) by Δx.'),eq(r'\frac{\Delta y}{\Delta x}=\frac1{\Delta x}\left[\frac{\sin(x+\Delta x)}{\cos(x+\Delta x)}-\frac{\sin x}{\cos x}\right]'),
 paragraph('Now, apply the limit as Δx → 0 on both sides of equation.'),
 eq(r'\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{\sin(x+\Delta x)\cos x-\sin x\cos(x+\Delta x)}{\Delta x\cos x\cos(x+\Delta x)}'),
 eq(r'=\lim_{\Delta x\to0}\frac{\sin(x+\Delta x-x)}{\Delta x\cos x\cos(x+\Delta x)}=\lim_{\Delta x\to0}\left[\frac1{\cos x\cos(x+\Delta x)}\frac{\sin\Delta x}{\Delta x}\right]'),
 eq(r'=\frac1{\cos x}\frac1{\cos x}\cdot1=\frac1{\cos^2x}=\sec^2x'),paragraph('Hence,'),eq(r'\frac{dy}{dx}=\sec^2x'),
 heading('iv. Derivative of sec x'),paragraph(r'If y = sec x, then the derivative of y = sec x is \(\frac{dy}{dx}=\sec x\tan x\).'),heading('Proof'),paragraph('By the rule of first principle. Let'),eq(r'y=\sec x'),eq(r'y+\Delta y=\sec(x+\Delta x)'),
 paragraph('Subtracting equation from equation.'),eq(r'y+\Delta y-y=\sec(x+\Delta x)-\sec x'),eq(r'\Delta y=\sec(x+\Delta x)-\sec x'),
 paragraph('Now, divide equation by the Δx.'),eq(r'\frac{\Delta y}{\Delta x}=\frac{\sec(x+\Delta x)-\sec x}{\Delta x}'),
 note('Angles are in radians throughout. The tan and sec formulas require cos x ≠ 0; continuity keeps the nearby denominators nonzero. The sec proof continues on page 85.')
]))
PAGES.append(page('047_page_1.jpg',85,[
 heading('Derivative of sec x — continued'),paragraph('Now, apply the limit as Δx → 0 on both sides of equation (iv).'),
 eq(r'\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{\frac1{\cos(x+\Delta x)}-\frac1{\cos x}}{\Delta x}=\lim_{\Delta x\to0}\frac{\cos x-\cos(x+\Delta x)}{\Delta x\cos x\cos(x+\Delta x)}'),
 eq(r'=\lim_{\Delta x\to0}\frac{-2\sin(\frac{x+x+\Delta x}2)\sin(\frac{x-x-\Delta x}2)}{\Delta x\cos x\cos(x+\Delta x)}'),
 eq(r'=\lim_{\Delta x\to0}\frac{-2\sin(\frac{2x+\Delta x}2)\sin(-\frac{\Delta x}2)}{\Delta x\cos x\cos(x+\Delta x)}=\lim_{\Delta x\to0}\frac{2\sin(x+\frac{\Delta x}2)\sin(\frac{\Delta x}2)}{\Delta x\cos x\cos(x+\Delta x)}'),
 eq(r'=\lim_{\Delta x\to0}\sin(x+\frac{\Delta x}2)\lim_{\Delta x\to0}\frac1{\cos x\cos(x+\Delta x)}\lim_{\Delta x\to0}\frac{\sin(\frac{\Delta x}2)}{\frac{\Delta x}2}'),
 eq(r'=\sin(x+0)\frac1{\cos x\cos x}\cdot1=\frac{\sin x}{\cos x}\frac1{\cos x}=\sec x\tan x'),paragraph('Hence,'),eq(r'\frac{dy}{dx}=\sec x\tan x'),
 heading('v. Derivative of cosec x'),paragraph(r'If y = cosec x, then the derivative of y = cosec x is \(\frac{dy}{dx}=-\cot x\,\text{cosec }x\).'),heading('Proof'),paragraph('By the rule of first principle. Let'),
 eq(r'y=\text{cosec }x','i'),eq(r'y+\Delta y=\text{cosec }(x+\Delta x)','ii'),paragraph('Subtracting equation (i) from equation (ii).'),eq(r'y+\Delta y-y=\text{cosec }(x+\Delta x)-\text{cosec }x'),eq(r'\Delta y=\text{cosec }(x+\Delta x)-\text{cosec }x','iii'),
 paragraph('Now, divide equation (iii) by the Δx.'),eq(r'\frac{\Delta y}{\Delta x}=\frac{\text{cosec }(x+\Delta x)-\text{cosec }x}{\Delta x}','iv'),paragraph('Now, apply the limit as Δx → 0 on both sides of equation (iv).'),
 eq(r'\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{\frac1{\sin(x+\Delta x)}-\frac1{\sin x}}{\Delta x}=\lim_{\Delta x\to0}\frac{\sin x-\sin(x+\Delta x)}{\Delta x\sin x\sin(x+\Delta x)}'),
 eq(r'=\lim_{\Delta x\to0}\frac{2\cos(\frac{x+x+\Delta x}2)\sin(\frac{x-x-\Delta x}2)}{\Delta x\sin x\sin(x+\Delta x)}=\lim_{\Delta x\to0}\frac{2\cos(x+\frac{\Delta x}2)\sin(-\frac{\Delta x}2)}{\Delta x\sin x\sin(x+\Delta x)}'),
 eq(r'=-\lim_{\Delta x\to0}\cos(x+\frac{\Delta x}2)\lim_{\Delta x\to0}\frac1{\sin(x+\Delta x)\sin x}\lim_{\Delta x\to0}\frac{\sin(\frac{\Delta x}2)}{\frac{\Delta x}2}'),
 eq(r'=-\cos(x+0)\frac1{\sin x\sin x}\cdot1=-\frac{\cos x}{\sin x}\frac1{\sin x}=-\cot x\,\text{cosec }x'),paragraph('Hence,'),eq(r'\frac{dy}{dx}=-\cot x\,\text{cosec }x'),
 heading('vi. Derivative of cot x'),paragraph(r'If y = cot x, then the derivative of y = cot x is \(\frac{dy}{dx}=-\text{cosec}^2x\).'),note('The cosec and cot derivatives require sin x ≠ 0. The cot proof continues on page 86.')
]))
PAGES.append(page('047_page_2.jpg',86,[
 heading('Derivative of cot x — continued'),heading('Proof'),paragraph('By the rule of first principle. Let'),eq(r'y=\cot x','i'),eq(r'y+\Delta y=\cot(x+\Delta x)','ii'),paragraph('Subtracting equation (i) from equation (ii).'),eq(r'y+\Delta y-y=\cot(x+\Delta x)-\cot x'),eq(r'\Delta y=\cot(x+\Delta x)-\cot x','iii'),paragraph('Now, divide equation (iii) by the Δx.'),eq(r'\frac{\Delta y}{\Delta x}=\frac{\cot(x+\Delta x)-\cot x}{\Delta x}','iv'),paragraph('Now, apply the limit as Δx → 0 on both sides of equation (iv).'),
 eq(r'\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{\frac{\cos(x+\Delta x)}{\sin(x+\Delta x)}-\frac{\cos x}{\sin x}}{\Delta x}=\lim_{\Delta x\to0}\frac{\sin x\cos(x+\Delta x)-\cos x\sin(x+\Delta x)}{\Delta x\sin x\sin(x+\Delta x)}'),
 eq(r'=\lim_{\Delta x\to0}\frac{\sin(x-x-\Delta x)}{\Delta x\sin x\sin(x+\Delta x)}=\lim_{\Delta x\to0}\frac1{\sin(x+\Delta x)\sin x}\frac{-\sin\Delta x}{\Delta x},\quad\sin(-\Delta x)=-\sin\Delta x'),
 eq(r'=-\frac1{\sin x\sin x}\cdot1=-\frac1{\sin^2x}=-\text{cosec}^2x'),
 heading('The trigonometric formulae are listed below.'),
 {'type':'list','items':[r'i. \(\frac{d}{dx}(\sin x)=\cos x\)',r'ii. \(\frac{d}{dx}(\cos x)=-\sin x\)',r'iii. \(\frac{d}{dx}(\tan x)=\sec^2x\)',r'iv. \(\frac{d}{dx}(\text{cosec }x)=-\cot x\,\text{cosec }x\)',r'v. \(\frac{d}{dx}(\sec x)=\tan x\sec x\)',r'vi. \(\frac{d}{dx}(\cot x)=-\text{cosec}^2x\)']},
 paragraph('The chain rule can be used to derive the generalization of the power rule and the rules for differentiating the trigonometric functions, as summarized in the box:'),
 {'type':'list','items':[r'i. \(\frac{d}{dx}(\sin u)=\cos u\frac{du}{dx}\)',r'ii. \(\frac{d}{dx}(\cos u)=-\sin u\frac{du}{dx}\)',r'iii. \(\frac{d}{dx}(\tan u)=\sec^2u\frac{du}{dx}\)',r'iv. \(\frac{d}{dx}(\text{cosec }u)=-\cot u\,\text{cosec }u\frac{du}{dx}\)',r'v. \(\frac{d}{dx}(\sec u)=\tan u\sec u\frac{du}{dx}\)',r'vi. \(\frac{d}{dx}(\cot u)=-\text{cosec}^2u\frac{du}{dx}\)']},
 heading('Example 16'),paragraph(r'Differentiate the following trigonometric functions: (a) \(p(t)=(t^2+t)\sin t\); (b) \(f(x)=\frac{1+\sin x}{2-\cos x}\).'),heading('Solution'),
 paragraph(r'a. If the given function is \(p(t)=(t^2+t)\sin t\), then the product rule of differentiation w.r.t. t is used to obtain:'),
 eq(r'\frac{dp}{dt}=(t^2+t)\frac{d}{dt}(\sin t)+(\sin t)\frac{d}{dt}(t^2+t)=(t^2+t)\cos t+\sin t(2t+1)'),
 paragraph(r'b. If the given function is \(f(x)=\frac{1+\sin x}{2-\cos x}\), then the quotient rule of differentiation w.r.t. x is used to obtain:'),
 eq(r'\frac{df}{dx}=\frac{(2-\cos x)\frac{d}{dx}(1+\sin x)-(1+\sin x)\frac{d}{dx}(2-\cos x)}{(2-\cos x)^2}=\frac{(\cos x)(2-\cos x)-(\sin x)(1+\sin x)}{(2-\cos x)^2}'),
 note('Example 16(b) continues on page 87. Its denominator 2 − cos x is at least 1 for every real x, so the function and derivative exist everywhere.')
]))

PAGES.append(page('048_page_1.jpg',87,[
 heading('Example 16 (b) — continued'),
 eq(r'=\frac{2\cos x-\cos^2x-\sin x-\sin^2x}{(2-\cos x)^2}=\frac{2\cos x-\sin x-(\cos^2x+\sin^2x)}{(2-\cos x)^2}=\frac{2\cos x-\sin x-1}{(2-\cos x)^2},\quad\sin^2x+\cos^2x=1'),
 heading('17'),paragraph(r'Differentiate the following trigonometric functions: (a) \(f(x)=\sec x\tan x\); (b) \(f(x)=\frac{x^2+\tan x}{3x+2\tan x}\).'),heading('Solution'),
 paragraph(r'a. If the given function is \(f(x)=\sec x\tan x\), then the product rule of differentiation w.r.t. x is used to obtain:'),
 eq(r'\frac{df}{dx}=\sec x\frac{d}{dx}(\tan x)+(\tan x)\frac{d}{dx}(\sec x)=\sec x(\sec^2x)+\tan x(\sec x\tan x)=\sec^3x+\sec x\tan^2x'),
 paragraph(r'b. If the given function is \(f(x)=\frac{x^2+\tan x}{3x+2\tan x}\), then the quotient rule of differentiation w.r.t. x is used to obtain:'),
 eq(r'\frac{df}{dx}=\frac{(3x+2\tan x)\frac{d}{dx}(x^2+\tan x)-(x^2+\tan x)\frac{d}{dx}(3x+2\tan x)}{(3x+2\tan x)^2}'),
 eq(r'=\frac{(2x+\sec^2x)(3x+2\tan x)-(3+2\sec^2x)(x^2+\tan x)}{(3x+2\tan x)^2}=\frac{3x^2+(4x-3)\tan x+x(3-2x)\sec^2x}{(3x+2\tan x)^2}'),
 heading('3.5.2 Differentiation of inverse trigonometric functions'),
 heading('i. Derivative of sin⁻¹ x'),paragraph('If y = sin⁻¹ x, then x = sin y.'),paragraph('The differentiation of x = sin y w.r.t. y is:'),eq(r'\frac{dx}{dy}=\cos y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac1{\cos y}=\frac{\pm1}{\sqrt{1-\sin^2y}}=\frac{\pm1}{\sqrt{1-x^2}},\quad\sin^2y+\cos^2y=1,\ \sin y=x'),
 paragraph('Here, the sign of the radical is the same as that of cos y. By definition of sin⁻¹ x:'),eq(r'-\frac{\pi}{2}\le\sin^{-1}x\le\frac{\pi}{2}\quad\text{or}\quad-\frac{\pi}{2}\le y\le\frac{\pi}{2}'),
 paragraph('Hence, cos y is positive:'),eq(r'\frac{d}{dx}(\sin^{-1}x)=\frac1{\sqrt{1-x^2}}'),
 heading('ii. Derivative of cos⁻¹ x'),paragraph('If y = cos⁻¹ x, then x = cos y.'),paragraph('The differentiation of x = cos y w.r.t. y is:'),eq(r'\frac{dx}{dy}=-\sin y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac{-1}{\sin y}=\frac{\pm(-1)}{\sqrt{1-\cos^2y}}=\frac{-1}{\sqrt{1-x^2}},\quad\sin^2y+\cos^2y=1,\ \cos y=x'),
 paragraph('Here, the sign of the radical is the same as that of sin y. By definition of cos⁻¹ x:'),eq(r'0\le\cos^{-1}x\le\pi\quad\text{or}\quad0\le y\le\pi'),paragraph(r'Also, if y lies between 0 and π, then sin y is necessarily positive. Hence \(\frac{d}{dx}(\cos^{-1}x)=\frac{-1}{\sqrt{1-x^2}}\).'),
 note('The inverse notation denotes a principal inverse function, not a reciprocal. For finite derivatives of arcsin and arccos, −1 < x < 1; their endpoint values exist but their derivatives are unbounded. Thus the proof uses the interiors of the printed y-ranges. For Example 17, require cos x ≠ 0, and in part (b) also 3x + 2 tan x ≠ 0.')
]))
PAGES.append(page('048_page_2.jpg',88,[
 heading('iii. Derivative of tan⁻¹ x'),paragraph('If y = tan⁻¹ x, then x = tan y.'),paragraph('The differentiation of x = tan y w.r.t. y is:'),eq(r'\frac{dx}{dy}=\sec^2y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac1{\sec^2y}=\frac1{1+\tan^2y}=\frac1{1+x^2},\quad\sec^2y=1+\tan^2y,\ \tan y=x'),
 heading('iv. Derivative of sec⁻¹ x'),paragraph('If y = sec⁻¹ x, then x = sec y.'),paragraph('The differentiation of x = sec y w.r.t. y is:'),eq(r'\frac{dx}{dy}=\sec y\tan y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac1{\sec y\tan y}=\frac{\pm1}{\sec y\sqrt{\sec^2y-1}}=\frac{\pm1}{x\sqrt{x^2-1}},\quad1+\tan^2y=\sec^2y,\ \sec y=x'),paragraph('We take the + sign before the radical sign to obtain:'),eq(r'\frac{d}{dx}(\sec^{-1}x)=\frac1{x\sqrt{x^2-1}}'),
 heading('v. Derivative of cosec⁻¹ x'),paragraph('If y = cosec⁻¹ x, then x = cosec y.'),paragraph('The differentiation of x = cosec y w.r.t. y is:'),eq(r'\frac{dx}{dy}=-\text{cosec }y\cot y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac{-1}{\text{cosec }y\cot y}=\frac{-1}{\text{cosec }y\sqrt{\text{cosec}^2y-1}},\quad1+\cot^2y=\text{cosec}^2y,\ \text{cosec }y=x'),eq(r'\frac{dy}{dx}=\frac{\pm(-1)}{x\sqrt{x^2-1}}'),paragraph('We take the + sign before the radical sign to obtain:'),eq(r'\frac{d}{dx}(\text{cosec}^{-1}x)=\frac{-1}{x\sqrt{x^2-1}}'),
 heading('vi. Derivative of cot⁻¹ x'),paragraph('If y = cot⁻¹ x, then x = cot y.'),paragraph('The differentiation of x = cot y w.r.t. y is:'),eq(r'\frac{dx}{dy}=-\text{cosec}^2y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=-\frac1{\text{cosec}^2y}=-\frac1{1+\cot^2y}=\frac{-1}{1+x^2},\quad\text{cosec}^2y=1+\cot^2y,\ \cot y=x'),
 heading('The inverse trigonometric formulas are listed in the box:'),
 {'type':'list','items':[r'i. \(\frac{d}{dx}(\sin^{-1}x)=\frac1{\sqrt{1-x^2}}\)',r'ii. \(\frac{d}{dx}(\cos^{-1}x)=\frac{-1}{\sqrt{1-x^2}}\)',r'iii. \(\frac{d}{dx}(\tan^{-1}x)=\frac1{1+x^2}\)',r'iv. \(\frac{d}{dx}(\text{cosec}^{-1}x)=\frac{-1}{x\sqrt{x^2-1}}\)',r'v. \(\frac{d}{dx}(\sec^{-1}x)=\frac1{x\sqrt{x^2-1}}\)',r'vi. \(\frac{d}{dx}(\cot^{-1}x)=\frac{-1}{1+x^2}\)']},
 paragraph('The chain rule can be used to derive the generalization of the power rule and the rules for differentiating the inverse trigonometric functions, as summarized in the box:'),
 {'type':'list','items':[r'i. \(\frac{d}{dx}(\sin^{-1}u)=\frac1{\sqrt{1-u^2}}\frac{du}{dx}\)',r'ii. \(\frac{d}{dx}(\cos^{-1}u)=\frac{-1}{\sqrt{1-u^2}}\frac{du}{dx}\)',r'iii. \(\frac{d}{dx}(\tan^{-1}u)=\frac1{1+u^2}\frac{du}{dx}\)',r'iv. \(\frac{d}{dx}(\text{cosec}^{-1}u)=\frac{-1}{u\sqrt{u^2-1}}\frac{du}{dx}\)',r'v. \(\frac{d}{dx}(\sec^{-1}u)=\frac1{u\sqrt{u^2-1}}\frac{du}{dx}\)',r'vi. \(\frac{d}{dx}(\cot^{-1}u)=\frac{-1}{1+u^2}\frac{du}{dx}\)']},
 note(r'The source does not specify branches for inverse secant and cosecant and selects a positive radical. Its formulas are valid on x > 1 under the standard branches. On the conventional arcsec range [0,π] excluding π/2 and arccsc range [−π/2,π/2] excluding 0, the formulas on both real intervals |x| > 1 are \(\frac{d}{dx}\operatorname{arcsec}x=\frac1{|x|\sqrt{x^2-1}}\) and \(\frac{d}{dx}\operatorname{arccsc}x=\frac{-1}{|x|\sqrt{x^2-1}}\). Their chain rules likewise use |u|. Neither has a finite derivative at |x| = 1. The arctan derivative holds for all real x; the decreasing arccot branch (0,π) gives −1/(1+x²) for all real x.')
]))

PAGES.append(page('049_page_1.jpg',89,[
 heading('Example 18'),paragraph(r'Differentiate the following inverse trigonometric functions: (a) \(y=\tan^{-1}\sqrt{x}\); (b) \(y=\cos^{-1}\left(\frac{x-x^{-1}}{x+x^{-1}}\right)\).'),heading('Solution'),
 paragraph(r'a. \(y=\tan^{-1}\sqrt{x}\)'),eq(r'y=f(x)=\tan^{-1}\sqrt{x}','i'),paragraph('Let'),eq(r'u=\sqrt{x}\quad\Rightarrow\quad\frac{du}{dx}=\frac1{2\sqrt{x}}','ii'),paragraph('Now,'),eq(r'y=\tan^{-1}u\quad\Rightarrow\quad\frac{dy}{du}=\frac1{1+u^2}','iii'),paragraph('By using chain rule'),eq(r'\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}'),paragraph('From equation (ii) and equation (iii)'),eq(r'\frac{dy}{dx}=\frac1{1+u^2}\frac1{2\sqrt{x}}\quad\Rightarrow\quad\frac{dy}{dx}=\frac1{2\sqrt{x}(1+x)}'),
 paragraph(r'b. Given \(y=\cos^{-1}\left(\frac{x-x^{-1}}{x+x^{-1}}\right)\). Let'),eq(r'u=\frac{x-x^{-1}}{x+x^{-1}}=\frac{x^2-1}{x^2+1}'),
 eq(r'\frac{du}{dx}=\frac{d}{dx}\left[\frac{x^2-1}{x^2+1}\right]=\frac{(x^2+1)\frac{d}{dx}(x^2-1)-(x^2-1)\frac{d}{dx}(x^2+1)}{(x^2+1)^2}'),
 eq(r'=\frac{(x^2+1)(2x)-(x^2-1)(2x)}{(x^2+1)^2}=\frac{2x^3+2x-2x^3+2x}{(x^2+1)^2}=\frac{4x}{(x^2+1)^2}'),
 paragraph(r'Now, \(y=\cos^{-1}u\), where \(u=\frac{x-x^{-1}}{x+x^{-1}}=\frac{x^2-1}{x^2+1}\).'),eq(r'\frac{dy}{du}=\frac{d}{du}\cos^{-1}u=\frac{-1}{\sqrt{1-u^2}}'),paragraph('By chain rule'),
 eq(r'\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}=\frac{-1}{\sqrt{1-u^2}}\frac{4x}{(x^2+1)^2}=\frac{-1}{\sqrt{1-(\frac{x^2-1}{x^2+1})^2}}\frac{4x}{(x^2+1)^2}'),
 note('The original quotient in part (b) excludes x = 0. Its principal-arccos simplification continues on page 90; the square root of x² is |x|, which is needed to handle negative x correctly.')
]))
PAGES.append(page('049_page_2.jpg',90,[
 heading('Example 18 (b) — continued'),
 eq(r'\frac{dy}{dx}=\frac{-4x}{\sqrt{\frac{(x^2+1)^2-(x^2-1)^2}{(x^2+1)^2}}(x^2+1)^2}=\frac{-4x}{\sqrt{\frac{4x^2}{(x^2+1)^2}}(x^2+1)^2}=\frac{-4x}{2x(x^2+1)}'),eq(r'\frac{dy}{dx}=\frac{-2}{x^2+1}'),
 note(r'The printed cancellation uses √(4x²) = 2x, valid only for x > 0. In general √(4x²) = 2|x|, so the original principal-arccos function has derivative \(\frac{-2x}{|x|(x^2+1)}\) for x ≠ 0: −2/(x²+1) on x > 0 and +2/(x²+1) on x < 0.'),
 heading('Exercise 3.4'),
 paragraph(r'1. Use of first principle rules to differentiate the following functions. (a) \(y=\sin(2x)^1\); (b) \(y=\cot(3x)\); (c) \(y=\cos(3x)+\tan(3x)\); (d) \(y=\cot^2x\); (e) \(y=\tan\sqrt{x}\); (f) \(y=\sin^3x\).'),
 paragraph(r'2. Differentiate the following trigonometric functions by using any suitable rule. (a) \(x^2\cot(3x)\); (b) \(y=(\sin2x+\cot3x)^2\); (c) \(y=4\,\text{cosec }2x\); (d) \(y=2\tan(x+3)^2\); (e) \(y=\frac{\sqrt{\tan x}}{\cos\sqrt{x}}\); (f) \(y=\frac{1+\tan2x}{\text{cosec }3x}\).'),
 paragraph(r'3. Use any suitable rule of differentiation to perform dy/dx for the following functions. (a) \(y=\cos^{-1}(\frac{x}{a})\); (b) \(y=\tan^{-1}(\frac{x}{p})\); (c) \(y=\cot^{-1}(\frac{a}{x})\); (d) \(y=\text{cosec}^{-1}\sqrt{1+x^2}\); (e) \(y=\text{cosec}^{-1}(t+3)\); (f) \(y=\frac1x\tan^{-1}(\frac{x+1}{x-1})\).'),
 paragraph(r'4. Suppose profits on the sale of swimming suits in a departmental store are given approximately by \(P(t)=5-5\cos\frac{\pi t}{26},\quad0\le t\le104\), where P(t) is profit (in hundreds of dollars) for a week of sales t weeks after January first. (a) What is the rate of change of profit t weeks after the first of the year? (b) What is the rate of change of profit 8 weeks after the first of the year? 26 weeks after the first of the year? 50 weeks after the first of the year?'),
 paragraph(r'5. A normal seated adult breathes in and exhales about 0.8 liter of air every 4 seconds. The volume of air V(t) in the lungs t seconds after exhaling is given approximately by \(V(t)=0.45-0.35\cos\frac{\pi t}{2},\quad0\le t\le8\). (a) What is the rate of flow of air t seconds after exhaling? (b) What is the rate of flow of air 3 seconds after exhaling? 4 seconds after exhaling? 5 seconds after exhaling?'),
 heading('3.6 Differentiation of Exponential and Logarithmic Functions'),paragraph('The goal of this section is to develop the differential calculus of logarithmic and exponential functions. We shall begin by deriving differentiation formulas for ln x and eˣ. The derived formulas will be applied to a number of differentiation problems and applications.')
]))

for p in PAGES:
    p['title']='DIFFERENTIATION'
    p['visualStatus']='All first-principles equations and source text rendered digitally; page 84 radar artwork retained as a dedicated source crop'
    p['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':(p['page']+9)//2,'side':'left' if p['page']%2 else 'right','reason':'Visually checked trigonometric signs, identities, all difference quotients and source context against full PDF and JPG.'}

FIGURE_PDF_CROPS=[(46,'radar-gun-source',(1248,381,1406,520))]
EXAMPLES=[
 {'id':'we-3-source-16','num':'16','title':'Example 16','problem':r'Differentiate (a) \(p(t)=(t^2+t)\sin t\); (b) \(f(x)=\frac{1+\sin x}{2-\cos x}\).','given':'A polynomial–sine product and a trigonometric quotient. Angles are in radians.','method':'Use product and quotient rules, then simplify with sin²x + cos²x = 1.','steps':[r'(a) Set u = t² + t and v = sin t. Then u′ = 2t + 1 and v′ = cos t.',r'Apply (uv)′ = u′v + uv′: p′(t) = (2t + 1)sin t + (t² + t)cos t.',r'Both factors are differentiable for every real t, so this formula has no real exclusions.',r'(b) Set N = 1 + sin x and D = 2 − cos x. Then N′ = cos x and D′ = sin x.',r'Apply the quotient rule: f′ = [D cos x − N sin x]/D².',r'Expand the numerator to 2cos x − cos²x − sin x − sin²x. Since cos²x + sin²x = 1, it is 2cos x − sin x − 1.',r'D = 2 − cos x ≥ 1 for all real x. Thus the simplified derivative applies for every real x. At x = 0 it equals 1, which also follows directly from N = D = N′ = 1 and D′ = 0.'],'answer':r'(a) \((2t+1)\sin t+(t^2+t)\cos t\). (b) \(\frac{2\cos x-\sin x-1}{(2-\cos x)^2}\). Both are defined for all real inputs.','progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'pageStart':86,'pageEnd':87,'verification':'complete question and source solution visually compared with JPG and full PDF'}]},
 {'id':'we-3-source-17','num':'17','title':'Example 17','problem':r'Differentiate (a) \(f(x)=\sec x\tan x\); (b) \(f(x)=\frac{x^2+\tan x}{3x+2\tan x}\).','given':'A secant–tangent product and a quotient involving tan x; radians.','method':'Apply product and quotient rules and collect terms.','steps':[r'(a) The derivative of sec x is sec x tan x, and the derivative of tan x is sec²x.',r'Apply the product rule: f′ = (sec x tan x)tan x + sec x(sec²x) = sec x tan²x + sec³x. Require cos x ≠ 0.',r'(b) Let N = x² + tan x and D = 3x + 2tan x. Then N′ = 2x + sec²x and D′ = 3 + 2sec²x.',r'The quotient derivative is [D(2x + sec²x) − N(3 + 2sec²x)]/D².',r'Expand: 6x² + 4x tan x + 3x sec²x + 2tan x sec²x − 3x² − 3tan x − 2x²sec²x − 2tan x sec²x.',r'Cancel the opposite 2tan x sec²x terms and collect the rest to obtain [3x² + (4x − 3)tan x + x(3 − 2x)sec²x]/(3x + 2tan x)².',r'For part (b), require both cos x ≠ 0 and 3x + 2tan x ≠ 0. In particular x = 0 is excluded even though the numerator also vanishes there; cancellation or a limiting extension would define a different function.'],'answer':r'(a) \(\sec^3x+\sec x\tan^2x\), cos x ≠ 0. (b) \(\frac{3x^2+(4x-3)\tan x+x(3-2x)\sec^2x}{(3x+2\tan x)^2}\), cos x ≠ 0 and 3x + 2tan x ≠ 0.','progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':87,'jpg':'048_page_1.jpg','verification':'complete question and source solution visually compared with JPG and full PDF'}]}
]
EXAMPLES.append({'id':'we-3-source-18','num':'18','title':'Example 18','problem':r'Differentiate (a) \(y=\tan^{-1}\sqrt{x}\); (b) \(y=\cos^{-1}\left(\frac{x-x^{-1}}{x+x^{-1}}\right)\).','given':'Principal inverse trigonometric functions; part (a) x ≥ 0, part (b) x ≠ 0.','method':'Chain rule, quotient rule and principal square-root sign.','steps':[r'(a) Let u = √x. For x > 0, u′ = 1/(2√x) and d(arctan u)/du = 1/(1 + u²).',r'Multiply to obtain y′ = 1/[2√x(1 + x)]. At x = 0 the function exists, but its right-hand derivative is unbounded.',r'(b) Multiply the inner numerator and denominator by x, allowed since x ≠ 0: u = (x² − 1)/(x² + 1).',r'Quotient rule gives u′ = [(x² + 1)2x − (x² − 1)2x]/(x² + 1)² = 4x/(x² + 1)².',r'For x ≠ 0, −1 < u < 1 and 1 − u² = 4x²/(x² + 1)². Thus √(1 − u²) = 2|x|/(x² + 1).',r'Apply the arccos chain rule: y′ = −u′/√(1 − u²) = −2x/[|x|(x² + 1)].',r'Therefore y′ = −2/(x² + 1) when x > 0 and +2/(x² + 1) when x < 0. The printed negative-only answer assumes x > 0. The original expression is undefined at x = 0.',r'Independent branch check: the function equals 2 arctan(1/|x|) for x ≠ 0. Differentiating separately on positive and negative x reproduces the two slopes.'],'answer':r'(a) \(\frac1{2\sqrt{x}(1+x)}\), x > 0. (b) \(\frac{-2x}{|x|(x^2+1)}\), x ≠ 0.','sourceClarification':'The source replaces √(4x²) with 2x. Its final answer is correct only for positive x; negative x requires the opposite sign.','progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'pageStart':89,'pageEnd':90,'verification':'complete question and source solution visually compared with JPG and full PDF'}]})
