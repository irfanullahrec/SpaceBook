const fs = require('fs');
const vm = require('vm');
const path = require('path');
const { execFileSync } = require('child_process');
const file = path.join(__dirname, '..', 'js', 'math_10_data.js');
const context = {};
vm.createContext(context);
vm.runInContext(fs.readFileSync(file, 'utf8'), context);
const unit = context.MATH_10_DATA.find(x => x.number === 7);
const baseline = {};
vm.createContext(baseline);
vm.runInContext(execFileSync('git', ['show', 'HEAD:SpaceBook Web/js/math_10_data.js'], { encoding:'utf8' }), baseline);
const originalSLOs = baseline.MATH_10_DATA.find(x => x.number === 7).slos;

unit.status = 'ready';
unit.badge = 'Rebuilt in textbook order from pages 162–192';
unit.pageRange = 'Pages 162–192';
unit.description = 'The lessons follow sections 7.1–7.5, Examples 1–22, Exercises 7.1–7.6 and Review Exercise 7 in the printed order. Angle, circle, unit-circle, triangle and elevation figures are included with the matching material.';
unit.sections = [
  { id:'7.1', title:'7.1 Measurement of Angles', page:164, theory:'The unit opens with angle measure and the sexagesimal system. A full turn is 360°, a straight angle is 180°, and a right angle is 90°. The initial side and terminal side show the direction and size of a rotation.', rules:['One complete rotation = 360° = 2π radians.','An angle is positive when measured anticlockwise and negative when measured clockwise.'] },
  { id:'7.1.1', title:'7.1.1 Sexagesimal System (Degree, Minute and Second)', page:164, theory:'The sexagesimal system uses base 60. A degree is divided into 60 minutes and each minute into 60 seconds. Angles are written in D°M′S″ form.', rules:['1° = 60′; 1′ = 60″; 1° = 3600″.','To convert D°M′S″ to decimal degrees, use D + M/60 + S/3600.'] },
  { id:'7.1.2', title:'7.1.2 Conversion of D°M′S″ Form into Decimal Form and Vice Versa', page:165, theory:'Convert minutes and seconds to fractions of a degree for decimal form. For the reverse conversion, take the whole degree part first, multiply the remaining decimal by 60 to get minutes, then multiply the remaining fraction by 60 to get seconds.', rules:['Decimal degrees = D + M/60 + S/3600.','For decimal-to-DMS conversion, retain the whole degree, then convert the fractional parts successively by 60.'] },
  { id:'7.1.3', title:'7.1.3 Circular System (Radians)', page:165, theory:'A radian is the angle subtended at the centre of a circle by an arc whose length equals the radius. If an arc has length ℓ in a circle of radius r, its radian measure is θ = ℓ/r.', rules:['θ = ℓ/r radians.','One complete rotation measures 2π radians.'] },
  { id:'7.1.4', title:'7.1.4 Relation Between Radians and Degrees', page:166, theory:'A complete circumference has length 2πr and subtends 360°. Therefore 2π radians = 360°, giving the conversion between degree and radian measure.', rules:['π radians = 180°.','Degrees to radians: multiply by π/180. Radians to degrees: multiply by 180/π.','1 radian ≈ 57.296°; 1° ≈ 0.01745 radian.'] },
  { id:'7.2.1', title:'7.2.1 Length of an Arc of a Circle', page:168, theory:'For a circle of radius r and central angle θ measured in radians, the arc length is proportional to the radius and angle.', rules:['ℓ = rθ, with θ in radians.','For n complete revolutions, distance travelled on the circle is 2πrn.'] },
  { id:'7.2.2', title:'7.2.2 Area of a Sector', page:170, theory:'A sector is the region enclosed by two radii and the intercepted arc. Its area is the fraction θ/(2π) of the circle’s area when θ is measured in radians.', rules:['A = ½r²θ, with θ in radians.','If θ is given in degrees, first convert it to radians.'] },
  { id:'7.3.1', title:'7.3.1 General Angles (Coterminal Angles)', page:172, theory:'Angles with the same initial and terminal sides are coterminal. Their measures differ by an integer multiple of one complete turn.', rules:['In degrees, coterminal angles differ by 360°k.','In radians, coterminal angles differ by 2πk.'] },
  { id:'7.3.2', title:'7.3.2 Angles in Standard Position, Quadrants and Quadrantal Angles', page:173, theory:'An angle is in standard position when its vertex is at the origin and its initial side lies on the positive x-axis. Its quadrant is determined by the terminal side. Quadrantal angles have terminal sides on an axis.', rules:['Quadrant I: x>0,y>0; II: x<0,y>0; III: x<0,y<0; IV: x>0,y<0.','Quadrantal angles include 0°, 90°, 180°, 270° and 360°.'] },
  { id:'7.3.3', title:'7.3.3 Trigonometric Ratios', page:174, theory:'For an acute angle in a right triangle, sine, cosine and tangent are ratios of side lengths. Their reciprocals are cosecant, secant and cotangent. The unit-circle definition extends these ratios to general angles.', rules:['sinθ = opposite/hypotenuse; cosθ = adjacent/hypotenuse; tanθ = opposite/adjacent.','cosecθ = 1/sinθ; secθ = 1/cosθ; cotθ = 1/tanθ.','On the unit circle, a point P(x,y) at angle θ gives cosθ=x and sinθ=y.'] },
  { id:'7.3.4', title:'7.3.4 Values of Trigonometric Ratios for 30°, 45° and 60°', page:176, theory:'The special-angle values are obtained from 30°–60°–90° and 45°–45°–90° triangles. The reciprocal ratios follow by taking reciprocals.', rules:['sin30°=½, sin45°=1/√2, sin60°=√3/2.','cos30°=√3/2, cos45°=1/√2, cos60°=½.','tan30°=1/√3, tan45°=1, tan60°=√3.'] },
  { id:'7.3.5', title:'7.3.5 Signs of Trigonometric Ratios in the Quadrants', page:176, theory:'The signs of the six trigonometric ratios depend on the signs of x and y on the terminal side. The book summarizes the pattern by quadrant.', rules:['Quadrant I: all six ratios are positive.','Quadrant II: sine and cosecant are positive.','Quadrant III: tangent and cotangent are positive.','Quadrant IV: cosine and secant are positive.'] },
  { id:'7.3.6', title:'7.3.6 Finding the Remaining Trigonometric Ratios When One Is Given', page:178, theory:'Represent a terminal point by coordinates (x,y), use the given ratio to determine a side relationship, and apply x²+y²=r². The quadrant fixes the signs of x and y.', rules:['Use r²=x²+y².','Apply the sign of each coordinate from the stated quadrant before writing the six ratios.'] },
  { id:'7.3.7', title:'7.3.7 Trigonometric Ratios of 0°, 90°, 180°, 270° and 360°', page:180, theory:'The unit circle gives the trigonometric ratios at quadrantal angles. Ratios with zero denominator are undefined.', rules:['Use sinθ=y and cosθ=x on the unit circle.','tanθ is undefined when cosθ=0; cotθ is undefined when sinθ=0.'] },
  { id:'7.4', title:'7.4 Trigonometric Identities', page:184, theory:'The fundamental identities follow by dividing the Pythagorean relation for a right triangle by its hypotenuse, base or perpendicular squared. The examples use these identities to transform one side of an equation into the other.', rules:['cos²θ + sin²θ = 1.','1 + tan²θ = sec²θ.','1 + cot²θ = cosec²θ.'] },
  { id:'7.5', title:'7.5 Angle of Elevation and Depression', page:187, theory:'The angle of elevation is measured upward from a horizontal line of sight; the angle of depression is measured downward from a horizontal line of sight. Parallel horizontal lines make these angles equal to the corresponding alternate interior angles in the right-triangle model.', rules:['Draw a horizontal reference and a right triangle before choosing a ratio.','tanθ = opposite/adjacent; sinθ = opposite/hypotenuse; cosθ = adjacent/hypotenuse.'] }
];
const lessonDiagrams = {
  '7.1.1':{type:'quadrants',title:'Initial side and terminal side of an angle'},
  '7.1.3':{type:'sector',title:'Radian measure is arc length divided by radius',radius:'r',angle:'1 rad'},
  '7.2.1':{type:'sector',title:'Arc length ℓ=rθ',radius:'r',angle:'θ'},
  '7.2.2':{type:'sector',title:'Area of a sector A=½r²θ',radius:'r',angle:'θ'},
  '7.3.1':{type:'quadrants',title:'Coterminal angles share a terminal side'},
  '7.3.2':{type:'quadrants',title:'Quadrants and signs of coordinates'},
  '7.3.3':{type:'unit-circle',title:'Trigonometric ratios from a unit-circle point',angle:45},
  '7.3.4':{type:'right-triangle',title:'Special-angle right triangles',angle:'30°, 45°, 60°'},
  '7.4':{type:'right-triangle',title:'Pythagorean relation gives the fundamental identities'},
  '7.5':{type:'elevation',title:'Horizontal line of sight and elevation/depression angles',height:'object',distance:'ground'}
};
unit.sections.forEach(section => { if(lessonDiagrams[section.id]) section.diagram=lessonDiagrams[section.id]; });

const ex = (number,page,sectionId,problem,given,method,steps,answer,diagram) => ({id:'eg'+number,number,page,sectionId,title:`Example ${number} (p. ${page})`,problem,given,method,steps,answer,...(diagram?{diagram}:{})});
unit.workedExamples = [
  ex(1,165,'7.1.2','Convert 15°30′25″ to decimal form.','15°30′25″','D + M/60 + S/3600',['30′ = 30/60 = 0.5°; 25″ = 25/3600 ≈ 0.00694°.','15°30′25″ = 15 + 0.5 + 0.00694 = 15.50694°.'],'15.50694°'),
  ex(2,165,'7.1.2','Convert 38.39° to D°M′S″ form.','38.39°','Repeated multiplication of the fractional part by 60',['The whole-degree part is 38°.','0.39×60 = 23.4′, so the minutes are 23′.','0.4×60 = 24″.'],'38°23′24″'),
  ex(3,167,'7.1.4','Convert 4π/7 radians to degrees.','4π/7 radians','Multiply by 180°/π',['(4π/7)×(180°/π) = 720°/7 = 102.85714°.','Convert the decimal fraction to minutes and seconds.'],'102°51′26″'),
  ex(4,167,'7.1.4','Convert 31°45′ to radians.','31°45′ = 31.75°','Multiply by π/180',['31.75×π/180 ≈ 0.5541 radians.'],'0.5541 radians'),
  ex(5,168,'7.2.1','Find the length of an arc of a circle of radius 5 cm which subtends an angle 3π/4 radians at the centre.','r=5 cm, θ=3π/4','Arc length ℓ=rθ',['ℓ=5×3π/4=15π/4 cm.','15π/4≈11.78 cm.'],'15π/4 cm ≈ 11.78 cm', {type:'sector',title:'Arc with radius 5 cm and central angle 3π/4',radius:'5 cm',angle:'3π/4'}),
  ex(6,168,'7.2.1','Find the distance travelled by a cyclist moving on a circle of radius 15 m, if he makes 3.5 revolutions.','r=15 m; n=3.5','One revolution is 2π radians; use ℓ=rθ',['θ=3.5×2π=7π radians.','Distance=15×7π=105π m.'],'105π m ≈ 329.87 m', {type:'sector',title:'Distance for 3.5 revolutions',radius:'15 m',angle:'7π'}),
  ex(7,169,'7.2.1','An arc of length 2.5 cm in a circle of diameter 6 cm subtends angle θ at the centre. Find θ.','ℓ=2.5 cm; r=3 cm','θ=ℓ/r',['θ=2.5/3=5/6 radians.'],'5/6 radians ≈ 0.833 radians', {type:'sector',title:'Arc length 2.5 cm in a circle of radius 3 cm',radius:'3 cm',angle:'5/6'}),
  ex(8,169,'7.2.1','An arc of length 5 cm subtends an angle of 60° at the centre. Find the radius.','ℓ=5 cm; θ=60°','Convert to radians, then use r=ℓ/θ',['θ=60×π/180=π/3≈1.047 radians.','r=5/(π/3)=15/π≈4.78 cm.'],'15/π cm ≈ 4.78 cm'),
  ex(9,170,'7.2.2','Find the area of a sector with central angle 60° in a circular region of radius 5 cm.','r=5 cm; θ=60°','A=½r²θ, with θ in radians',['θ=60×π/180=π/3≈1.047.','A=½×25×π/3=25π/6 cm².'],'25π/6 cm² ≈ 13.09 cm²', {type:'sector',title:'Sector of radius 5 cm and central angle 60°',radius:'5 cm',angle:'60°'}),
  ex(10,173,'7.3.1','Find coterminal angles of 60° and −60°.','Angles 60° and −60°','Add and subtract 360°',['60°+360°=420° and 60°−360°=−300°.','−60°+360°=300° and −60°−360°=−420°.'],'420°, −300°; and 300°, −420°', {type:'quadrants',title:'Coterminal angles on coordinate axes',angle:60}),
  ex(11,177,'7.3.5','Find the signs of the following ratios and state their quadrants: (i) sin105°, (ii) tan(−5π/6), (iii) sec1030°, (iv) cot710°.','Four angles','Reduce each angle to its quadrant and apply the quadrant sign pattern',['105° is in quadrant II: sin105° is positive.','−5π/6 is coterminal with 7π/6 in quadrant III: tangent is positive.','1030° is coterminal with 310° in quadrant IV: secant is positive.','710° is coterminal with 350° in quadrant IV: cotangent is negative.'],'(i) +, II; (ii) +, III; (iii) +, IV; (iv) −, IV', {type:'quadrants',title:'Terminal sides in quadrants II, III and IV'}),
  ex(12,177,'7.3.5','If tanθ<0 and cosθ>0, name the quadrant containing θ.','tanθ<0; cosθ>0','Intersect the possible quadrants',['tanθ<0 in quadrants II or IV.','cosθ>0 in quadrants I or IV.','The common quadrant is IV.'],'Quadrant IV', {type:'quadrants',title:'Sign conditions select quadrant IV',quadrant:4}),
  ex(13,178,'7.3.6','If tanθ=1 and θ is in quadrant I, find the other trigonometric ratios.','tanθ=y/x=1; x=y=1','Use r²=x²+y², then form each ratio',['r=√(1²+1²)=√2.','sinθ=1/√2; cosθ=1/√2; cotθ=1.','cosecθ=√2; secθ=√2.'],'sinθ=cosθ=1/√2; cotθ=1; cosecθ=secθ=√2', {type:'unit-circle',title:'Point (1,1) in quadrant I',angle:45}),
  ex(14,178,'7.3.6','Given tanθ=−2/3 and θ in quadrant II, find the other trigonometric ratios.','tanθ=y/x=−2/3; x=−3,y=2','Use r²=x²+y² and the quadrant signs',['r=√(9+4)=√13.','sinθ=2/√13; cosθ=−3/√13; cotθ=−3/2.','cosecθ=√13/2; secθ=−√13/3.'],'sinθ=2/√13; cosθ=−3/√13; tanθ=−2/3; cotθ=−3/2; secθ=−√13/3; cosecθ=√13/2', {type:'unit-circle',title:'Point (−3,2) in quadrant II',x:-3,y:2}),
  ex(15,179,'7.3.6','If cosθ=4/5 and θ is in quadrant IV, find the other trigonometric ratios.','x/r=4/5; quadrant IV','Use r²=x²+y² and choose y<0',['Let x=4 and r=5. Then y²=25−16=9, so y=−3.','sinθ=−3/5; tanθ=−3/4; cotθ=−4/3.','secθ=5/4; cosecθ=−5/3.'],'sinθ=−3/5; tanθ=−3/4; cotθ=−4/3; secθ=5/4; cosecθ=−5/3', {type:'unit-circle',title:'Point (4,−3) in quadrant IV',x:4,y:-3}),
  ex(16,185,'7.4','Show that (sinθ+cosθ)² = 1+2sinθcosθ.','Identity to prove','Expand and use sin²θ+cos²θ=1',['(sinθ+cosθ)²=sin²θ+2sinθcosθ+cos²θ.','Replace sin²θ+cos²θ by 1.'],'(sinθ+cosθ)²=1+2sinθcosθ'),
  ex(17,185,'7.4','Prove that sinθ=√(1−cos²θ).','Fundamental identity','Rearrange cos²θ+sin²θ=1',['sin²θ=1−cos²θ.','Taking the nonnegative square root for the acute angle gives sinθ=√(1−cos²θ).'],'sinθ=√(1−cos²θ)'),
  ex(18,185,'7.4','Prove that √(1−sin²θ)/sinθ = cotθ.','Fundamental identity','Replace 1−sin²θ by cos²θ',['√(1−sin²θ)/sinθ=√(cos²θ)/sinθ.','For the acute-angle setting, √(cos²θ)=cosθ, so the expression is cosθ/sinθ=cotθ.'],'√(1−sin²θ)/sinθ=cotθ'),
  ex(19,186,'7.4','Prove that sec²θ+tan²θ=(1+sin²θ)/(1−sin²θ).','Fundamental identity','Write over cos²θ and use cos²θ=1−sin²θ',['sec²θ+tan²θ=1/cos²θ+sin²θ/cos²θ=(1+sin²θ)/cos²θ.','Since cos²θ=1−sin²θ, the required expression follows.'],'sec²θ+tan²θ=(1+sin²θ)/(1−sin²θ)'),
  ex(20,187,'7.5','An aerial photographer is 475 ft above the ground and 850 ft from a farmhouse. Find the angle of depression from the plane to the house.','Opposite side=475 ft; hypotenuse=850 ft','sinθ=opposite/hypotenuse',['sinθ=475/850≈0.5588.','θ=sin⁻¹(0.5588)≈34°.'],'About 34°', {type:'elevation',title:'Plane, farmhouse and angle of depression',height:'475 ft',distance:'850 ft',angle:'34°'}),
  ex(21,187,'7.5','A vertical beam of light reaches a cloud. From a point 135 ft from the light source, the angle of elevation to the spot is 67.35°. Find the cloud height.','Horizontal distance=135 ft; θ=67.35°','tanθ=opposite/adjacent',['tan67.35°=h/135.','h=135tan67.35°≈324 ft.'],'About 324 ft', {type:'elevation',title:'Cloud height from a ground observation point',height:'h',distance:'135 ft',angle:'67.35°'}),
  ex(22,188,'7.5','A lighthouse is 300 m above sea level. The angles of depression of two boats on the same side are 30° and 45°. Find the distance between the boats.','Height=300 m; depression angles=30°,45°','Use tanθ=height/horizontal distance',['The nearer boat is at distance 300/tan45°=300 m from the foot.','The farther boat is at distance 300/tan30°=300√3 m.','Their separation is 300(√3−1)≈219.6 m.'],'300(√3−1) m ≈ 219.6 m', {type:'elevation',title:'Lighthouse and two boats on the same side',height:'300 m',angle:'30° and 45°'})
];

const q = (qNo,question,solution,answer,diagram,category) => ({qNo,question,solution,answer,...(diagram?{diagram}:{}),...(category?{category}:{})});
const exset = (exercise,page,problems,title=`Exercise ${exercise}`) => ({exercise,title,page,problems});
unit.exercises = [
  exset('7.1',167,[
    q('1','Convert to decimal degrees: (i) 8°15′35″; (ii) 39°48′55″; (iii) 84°19′10″; (iv) 18°6′21″.','For each angle compute D+M/60+S/3600.','(i) 8.2597°; (ii) 39.8152°; (iii) 84.3194°; (iv) 18.1058°'),
    q('2','Convert to D°M′S″: (i) 42.25°; (ii) 57.325°; (iii) 12.9956°; (iv) 32.625°.','Separate the whole degree part, multiply the decimal part by 60 for minutes, then multiply the remaining part by 60 for seconds.','(i) 42°15′; (ii) 57°19′30″; (iii) 12°59′44″; (iv) 32°37′30″'),
    q('3','Convert to degrees: (i) 2 radians; (ii) 5π/3 radians; (iii) π/6 radians; (iv) −3π/4 radians.','Multiply each radian measure by 180°/π.','(i) ≈114.6°; (ii) 300°; (iii) 30°; (iv) −135°'),
    q('4','Convert to radians: (i) 45°; (ii) 120°; (iii) −210°; (iv) 60°35′48″.','Multiply the degree measure by π/180; convert DMS to decimal degrees first when needed.','(i) π/4; (ii) 2π/3; (iii) −7π/6; (iv) ≈1.0576 radians')
  ]),
  exset('7.2',171,[
    q('1','Find arc length ℓ when: (i) θ=π/6 rad, r=2 cm; (ii) θ=30°, r=6 cm; (iii) θ=4π/6 rad, r=6 cm.','Use ℓ=rθ, converting degrees to radians.','(i) π/3 cm; (ii) π cm; (iii) 4π cm', {type:'sector',title:'Arc length, ℓ=rθ'}),
    q('2','Find θ when: (i) ℓ=5 cm,r=2 cm; (ii) ℓ=30 cm,r=6 cm; (iii) ℓ=6 cm,r=2.87 cm.','Use θ=ℓ/r.','(i) 2.5 rad; (ii) 5 rad; (iii) ≈2.09 rad'),
    q('3','Find r when: (i) θ=π/6 rad,ℓ=2 cm; (ii) θ=3½ rad,ℓ=4/7 m; (iii) θ=3π/4 rad,ℓ=15 cm.','Use r=ℓ/θ.','(i) 12/π cm ≈3.82 cm; (ii) 8/49 m ≈0.1632 m; (iii) 20/π cm ≈6.366 cm'),
    q('4','Find the area of a sector of radius 4 m with central angle 12 radians.','A=½r²θ=½×16×12.','96 m²',{type:'sector',title:'Sector of radius 4 m and angle 12 rad',radius:'4 m',angle:'12 rad'}),
    q('5','A circle has radius 5 cm and a central angle of 30°. Find (i) the arc length and (ii) the area of the sector.','Convert 30° to π/6 radians; use ℓ=rθ and A=½r²θ.','(i) 5π/6 cm ≈2.62 cm; (ii) 25π/12 cm² ≈6.54 cm²',{type:'sector',title:'30° sector of a circle with radius 5 cm',radius:'5 cm',angle:'30°'}),
    q('6','An arc subtends 2 radians at the centre. If the sector area is 64 cm², find the circle’s radius.','64=½r²×2, so r²=64.','8 cm'),
    q('7','A point moves on a circle of radius 10 m through 3.5 revolutions. Find the distance travelled.','3.5 revolutions=7π radians; ℓ=rθ.','70π m'),
    q('8','What is the circular measure of the angle between the hands of a watch at 3 o’clock?','A quarter-turn is 90°; convert to radians.','π/2 radians'),
    q('9','In the diagram, radius OB=8 cm and ∠AOB=90°. Find the length of the minor arc APB.','ℓ=rθ with θ=π/2.','4π cm',{type:'sector',title:'Quarter-circle arc APB, radius 8 cm',radius:'8 cm',angle:'90°'}),
    q('10','Find the area of sector OPR when r=6 cm and ∠POR=60°.','A=½r²θ, with θ=π/3.','6π cm²',{type:'sector',title:'Sector OPR, radius 6 cm and angle 60°',radius:'6 cm',angle:'60°'})
  ]),
  exset('7.3',176,[
    q('1','Find one positive and one negative coterminal angle for: (i) 55°; (ii) −45°; (iii) π/6; (iv) −3π/4.','Add and subtract one full turn: 360° or 2π.','(i) 415°,−305°; (ii) 315°,−405°; (iii) 13π/6,−11π/6; (iv) 5π/4,−11π/4', {type:'quadrants',title:'Coterminal angles share a terminal side'}),
    q('2','State the quadrant for: (i) 8π/5; (ii) 75°; (iii) −818°; (iv) −5π/4; (v) 103°.','Reduce each angle to an equivalent angle between 0° and 360° (or 0 and 2π).','(i) IV; (ii) I; (iii) III; (iv) II; (v) II', {type:'quadrants',title:'Terminal sides in the four quadrants'})
  ]),
  exset('7.4',183,[
    q('1','Find the sign and quadrant: (i) sin98°; (ii) sin160°; (iii) tan200°; (iv) sec120°; (v) cosec198°; (vi) sin460°.','Reduce each angle to its quadrant and use the sign table.','(i) +,II; (ii) +,II; (iii) +,III; (iv) −,II; (v) −,III; (vi) +,I', {type:'quadrants',title:'Signs by quadrant'}),
    q('2','Find all six trigonometric ratios of: (i) −180°; (ii) −270°; (iii) 720°; (iv) 1470°.','Use coterminal quadrantal angles and the unit-circle coordinates; mark zero-denominator ratios undefined.','(i) sin=0, cos=−1, tan=0, cosec undefined, sec=−1, cot undefined; (ii) sin=1, cos=0, tan undefined, cosec=1, sec undefined, cot=0; (iii) sin=0, cos=1, tan=0, cosec undefined, sec=1, cot undefined; (iv) same as 30°.'),
    q('3','If secθ=2 and θ lies in quadrant IV, find the other trigonometric ratios.','cosθ=1/2; use a 30° reference triangle and quadrant signs.','sinθ=−√3/2; tanθ=−√3; cotθ=−1/√3; cosecθ=−2/√3; secθ=2'),
    q('4','If sinθ=4/5 and π/2<θ<π, find the other trigonometric ratios.','Use r=5,y=4 and x<0 in quadrant II; x²=25−16.','cosθ=−3/5; tanθ=−4/3; cotθ=−3/4; secθ=−5/3; cosecθ=5/4'),
    q('5','Evaluate: (i) 2sin45°cos45°; (ii) (tan60°−tan30°)/(1+tan60°tan30°); (iii) cos45°/(sin45°+tan45°); (iv) tan30°tan60°+tan45°; (v) cos(π/3)cos(π/6)−sin(π/3)sin(π/6).','Substitute the special-angle values and simplify.','(i) 1; (ii) 1/√3; (iii) 1/(1+√2); (iv) 2; (v) 0'),
    q('6','In which quadrant does θ lie? (i) sinθ>0,tanθ>0; (ii) sinθ<0,cotθ>0; (iii) sinθ>0,cosθ<0; (iv) cosθ>0,cosecθ<0; (v) tanθ<0,secθ>0; (vi) cosθ<0,tanθ<0.','Combine the sign conditions for each ratio.','(i) I; (ii) III; (iii) II; (iv) IV; (v) IV; (vi) III', {type:'quadrants',title:'Determine a quadrant from ratio signs'}),
    q('7','For each right triangle, find the missing side lengths to two decimal places: (i) hypotenuse 32, angle 53°; (ii) hypotenuse 73, angle 21°; (iii) base 12, angle 33°.','Use sine, cosine or tangent according to the labelled sides in the printed diagrams.','(i) adjacent≈19.25, opposite≈25.57; (ii) opposite≈26.16, adjacent≈68.15; (iii) opposite≈7.79, hypotenuse≈14.31', {type:'right-triangle',title:'Three right-triangle exercises',angle:'53°'}),
    q('8','A surveyor measures a 750 yd baseline and a 24° angle to a point across a lake, as shown. Find the distance a across the lake.','The right triangle has baseline 750 yd adjacent to 24° and lake width a opposite; use tan24°=a/750.','a=750tan24°≈334 yd',{type:'right-triangle',title:'Surveying the width of a lake',angle:'24°',adjacent:'750 yd',opposite:'a'})
  ]),
  exset('7.5',186,[
    q('1','Prove (sec²θ−1)cos²θ=sin²θ.','sec²θ−1=tan²θ; tan²θ cos²θ=sin²θ.','Proved.'),
    q('2','Prove tanθ+secθ=(1+sinθ)/cosθ.','Write tanθ=sinθ/cosθ and secθ=1/cosθ.','Proved.'),
    q('3','Prove (cosθ−sinθ)²=1−2sinθcosθ.','Expand the square and use cos²θ+sin²θ=1.','Proved.'),
    q('4','Prove cos²θ−sin²θ=2cos²θ−1.','Replace sin²θ by 1−cos²θ.','Proved.'),
    q('5','Prove tanθ+cotθ=secθ cosecθ.','Combine sinθ/cosθ+cosθ/sinθ over sinθcosθ.','Proved.'),
    q('6','Prove (1−sinθ)/cosθ=cosθ/(1+sinθ).','Rationalize the left side using 1−sin²θ=cos²θ.','Proved.'),
    q('7','Prove sinθ√(1+tan²θ)=tanθ.','Use 1+tan²θ=sec²θ and the acute-angle setting.','Proved.'),
    q('8','Prove cosθ=√(1−sin²θ).','Use cos²θ+sin²θ=1 and the acute-angle setting.','Proved.'),
    q('9','Prove (1+cosθ)(1−cosθ)=1/cosec²θ.','The left side is 1−cos²θ=sin²θ; the right side is sin²θ.','Proved.'),
    q('10','Prove cosx−cosx sin²x=cos³x.','Factor cosx and use 1−sin²x=cos²x.','Proved.'),
    q('11','Prove sinx/(1+cosx)+(1+cosx)/sinx=2cosecx.','Use the common denominator sinx(1+cosx) and simplify with sin²x=1−cos²x.','Proved.'),
    q('12','Prove sinx/(1+cosx)=(1−cosx)/sinx.','Cross-multiply; both sides reduce to sin²x=1−cos²x.','Proved.'),
    q('13','Prove 1/(1+cosa)+1/(1−cosa)=2+2cot²a.','Combine the fractions to get 2/sin²a=2cosec²a=2+2cot²a.','Proved.'),
    q('14','Prove cos⁴b−sin⁴b=1−2sin²b.','Factor as (cos²b−sin²b)(cos²b+sin²b)=cos²b−sin²b.','Proved.'),
    q('15','Prove (siny+cosy)/siny+(cosy−siny)/cosy=secy cosecy.','Combine the two fractions over siny cosy and use sin²y+cos²y=1.','Proved.'),
    q('16','Prove (secx−tanx)²=(1−sinx)/(1+sinx).','Write secx−tanx=(1−sinx)/cosx and square; use cos²x=(1−sinx)(1+sinx).','Proved.'),
    q('17','Prove sinx tanx+cosx=secx.','sinx tanx+cosx=sin²x/cosx+cosx=(sin²x+cos²x)/cosx.','Proved.')
  ]),
  exset('7.6',189,[
    q('1','A building 21 m tall casts a shadow 25 m long. Find the sun’s angle of elevation to the nearest degree.','tanθ=21/25.','θ≈40°',{type:'elevation',title:'Building and shadow',height:'21 m',distance:'25 m'}),
    q('2','A lighthouse is 150 m above sea level. The angle of depression of a boat is 60°. Find the horizontal distance from the boat to the lighthouse.','tan60°=150/d.','d=150/√3=50√3 m≈86.6 m',{type:'elevation',title:'Lighthouse and boat',height:'150 m',angle:'60°'}),
    q('3','A 50 m tree is observed from a point on the ground 100 m from its foot. Find the angle of elevation of its top.','tanθ=50/100.','θ≈26.6°',{type:'elevation',title:'Tree and observation point',height:'50 m',distance:'100 m'}),
    q('4','From the top of a 240 m hill, the angles of depression of the top and bottom of a minaret are 30° and 60°. Find the minaret’s height.','Horizontal distance to the minaret is 240/tan60°=80√3 m. The rise from the hilltop to the minaret top is 80√3tan30°=80 m.','Height=240−80=160 m',{type:'elevation',title:'Hill and minaret',height:'240 m',angle:'30° and 60°'}),
    q('5','A police helicopter flies 800 ft above the ground. A car is sighted at an angle of depression of 72°. Find the horizontal distance from the car to the point directly below the helicopter, to the nearest foot.','tan72°=800/d.','d=800/tan72°≈260 ft',{type:'elevation',title:'Helicopter and car',height:'800 ft',angle:'72°'}),
    q('6','A lighthouse is 300 m above sea level. Two boats lie on opposite sides of its foot, with depression angles 30° and 45°. Find the distance between the boats.','Their horizontal distances from the foot are 300/tan30°=300√3 m and 300/tan45°=300 m; opposite sides mean add.','300(√3+1) m≈819.6 m',{type:'elevation',title:'Two boats on opposite sides of a lighthouse',height:'300 m',angle:'30° and 45°'}),
    q('7','The angle of elevation of the top of a cliff is 30°. After walking 210 m toward it, the angle is 45°. Find the cliff’s height.','Let the nearer horizontal distance be x. Then h=x and h/(x+210)=tan30°=1/√3.','x=h=105(√3+1) m≈286.9 m',{type:'elevation',title:'Two observation points at a cliff',distance:'210 m',angle:'30° and 45°'})
  ]),
  exset('Review Exercise 7',190,[
    q('(i)','If an object is above the observer, the angle formed by the horizontal and the observer’s line of sight is called _____.','An upward line of sight makes an angle of elevation.','Angle of elevation','', 'MCQ'),
    q('(ii)','cotθ = _____.','cotθ is adjacent/opposite=cosθ/sinθ.','cosθ/sinθ','', 'MCQ'),
    q('(iii)','1+tan²θ = _____.','Use the fundamental identity.','sec²θ','', 'MCQ'),
    q('(iv)','If tanθ=1 and θ is in quadrant III, then sinθ=_____.','The reference angle is 45° and sine is negative in quadrant III.','−1/√2','', 'MCQ'),
    q('(v)','sin(−350°) lies in which quadrant?','−350° is coterminal with 10°.','Quadrant I','', 'MCQ'),
    q('(vi)','45° equals how many radians?','45×π/180=π/4.','π/4','', 'MCQ'),
    q('(vii)','A right triangle has hypotenuse 5 ft and ∠B=58°. Find the leg adjacent to ∠B.','Adjacent=5cos58°.','≈2.6496 ft','', 'MCQ'),
    q('(viii)','In the printed right triangle, MN=8 cm, NP=21 cm and ∠P=20°. Find tanP to the nearest tenth.','tanP=opposite/adjacent=MN/NP=8/21.','0.4','', 'MCQ'),
    q('(ix)','In right triangle RQS, RT is perpendicular to QS, QT=2, RQ=4, and RT=TS. Find RS.','RT²=RQ²−QT²=16−4=12, so RT=TS=2√3. Then RS=√(RT²+TS²).','2√6','', 'MCQ'),
    q('(x)','In the same diagram, RT is perpendicular to QS and RT=TS. Find ∠S.','Triangle RTS is an isosceles right triangle.','45°','', 'MCQ'),
    q('2','Convert 45°35′30″ to decimal form.','45+35/60+30/3600.','45.5917°'),
    q('3','Convert 216.67° to D°M′S″ form.','Take the fractional degree, multiply by 60 for minutes, then by 60 for seconds.','216°40′12″'),
    q('4','Through how many radians does a minute hand turn in (i) 45 minutes; (ii) one hour?','The minute hand turns 2π radians in 60 minutes.','(i) 3π/2; (ii) 2π'),
    q('5','Find coterminal angles for 190° and −250°.','Add and subtract 360°.','190°: 550°,−170°; −250°: 110°,−610°'),
    q('6','Find the six trigonometric ratios of (i) 390°; (ii) −240°.','Reduce to 30° and 120°, then use special-angle values and quadrant signs.','(i) sin=1/2, cos=√3/2, tan=1/√3, cosec=2, sec=2/√3, cot=√3; (ii) sin=√3/2, cos=−1/2, tan=−√3, cosec=2/√3, sec=−2, cot=−1/√3'),
    q('7','Prove: (i) √((1−sinθ)/(1+sinθ))=secθ−tanθ; (ii) 2cosθ secθ−tanθ cotθ=1.','(i) Rationalize the radicand to obtain (1−sinθ)²/cos²θ. (ii) Use cosθsecθ=1 and tanθcotθ=1.','Both identities hold.'),
    q('8','If secθ=2 and θ is not in quadrant I, find the remaining trigonometric ratios.','cosθ=1/2; the possible quadrants with positive cosine are I and IV, so θ is in IV. Use a 30° reference triangle.','sin=−√3/2; tan=−√3; cot=−1/√3; sec=2; cosec=−2/√3'),
    q('9','From a point 85 m from a building, the angle of elevation to its top is 26.5°. The observer’s eye is 1.6 m above the ground. Find the building’s height.','Height above eye level=85tan26.5°; add 1.6 m.','≈44.0 m',{type:'elevation',title:'Building height from a 26.5° sight line',height:'h−1.6 m',distance:'85 m',angle:'26.5°'}),
    q('10','From level ground 125 ft from a tower, the angle of elevation is 57.2°. Approximate the tower’s height to the nearest foot.','tan57.2°=h/125.','h≈194 ft',{type:'elevation',title:'Tower height from a 57.2° angle',height:'h',distance:'125 ft',angle:'57.2°'})
  ],'Review Exercise 7')
];

const reviewMcqOptions = [
  ['Angle of depression','Obtuse angle','Angle of elevation','None of the above'],
  ['sinθ/cosθ','1/cosθ','cosθ/sinθ','1/sinθ'],
  ['sin²θ','cos²θ','cosec²θ','sec²θ'],
  ['1/2','−1/2','−1/√2','1/√2'],
  ['1st quadrant','2nd quadrant','3rd quadrant','4th quadrant'],
  ['π/3','π/4','π/6','π/2'],
  ['4.2402 ft','8.0017 ft','0.10060 ft','2.6496 ft'],
  ['2.6','0.5','0.4','0.1'],
  ['2√6','2√3','4√3','2√2'],
  ['25°','30°','45°','60°']
];
unit.exercises[6].problems.slice(0,10).forEach((problem,i) => { problem.options = reviewMcqOptions[i]; });

unit.formulaSheet = [
  {name:'DMS and decimal degrees',formula:'D°M′S″ = D + M/60 + S/3600 degrees'},
  {name:'Degree-radian conversion',formula:'π radians = 180°; θ(rad)=θ(deg)×π/180'},
  {name:'Arc length',formula:'ℓ=rθ (θ in radians)'},
  {name:'Sector area',formula:'A=½r²θ (θ in radians)'},
  {name:'Right-triangle ratios',formula:'sinθ=opp/hyp; cosθ=adj/hyp; tanθ=opp/adj'},
  {name:'Reciprocal ratios',formula:'cosecθ=1/sinθ; secθ=1/cosθ; cotθ=1/tanθ'},
  {name:'Fundamental identities',formula:'sin²θ+cos²θ=1; 1+tan²θ=sec²θ; 1+cot²θ=cosec²θ'},
  {name:'Elevation and depression',formula:'Use the right-triangle ratios with a horizontal reference line'}
];
unit.slos = originalSLOs;
fs.writeFileSync(file, '// KPK Grade 10 Mathematics - textbook sequence reconstruction in progress\n// Source: Khyber Pakhtunkhwa Textbook Board Peshawar (Class 10)\nvar MATH_10_DATA = ' + JSON.stringify(context.MATH_10_DATA, null, 2) + ';\n');
