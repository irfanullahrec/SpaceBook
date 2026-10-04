// Lightweight SVG teaching figures based on the visual models in the KPTBB
// Class 1 and Class 2 mathematics workbooks. No workbook scans are bundled.
var PRIMARY_MATH_VISUALS = {
  cls1: {
    '1.1':'count','1.2':'blocks2','1.3':'line','1.4':'compare2','1.5':'ordinal',
    '2.1':'join','2.2':'tenframe','2.3':'addColumns','2.4':'takeaway','2.5':'missing',
    '3.1':'length','3.2':'length','3.3':'height','3.4':'balance',
    '4.1':'money','4.2':'moneyCount','4.3':'moneyWays','4.4':'change',
    '5.1':'clock','5.2':'clockDigital','5.3':'dayNight','5.4':'week','5.5':'months',
    '6.1':'flatShapes','6.2':'shapeObjects','6.3':'pattern','6.4':'position','6.5':'path'
  },
  cls2: {
    '1.1':'ordinal20','1.2':'count100','1.3':'blocks3','1.4':'compare3','1.5':'skipCount',
    '2.1':'addColumns3','2.2':'subtract3','2.3':'multiply','2.4':'division',
    '3.1':'fractionLabels','3.2':'fractionParts','3.3':'fractionPictures',
    '4.1':'rulerMeasure','4.2':'mass','4.3':'capacity','4.4':'measureAdd',
    '5.1':'clock','5.2':'clockTimes','5.3':'dayNight','5.4':'calendarPair',
    '6.1':'solidGallery3','6.2':'sidesCircle','6.3':'lineTypes','6.4':'gridPattern','6.5':'roman'
  }
};

function renderPrimaryMathDiagram(classId, chapterNumber, sectionId, subject) {
  const map = PRIMARY_MATH_VISUALS[classId];
  const key = map && map[sectionId];
  if (!key) return '';
  const esc = value => String(value || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const colors = ['#fda4af','#fcd34d','#86efac','#93c5fd','#c4b5fd','#fdba74'];
  const txt = (x,y,s,size=18,anchor='middle',fill='#26364a') => `<text x="${x}" y="${y}" text-anchor="${anchor}" font-size="${size}" font-weight="700" fill="${fill}">${esc(s)}</text>`;
  const rect = (x,y,w,h,fill='#eaf4ff',rx=8,stroke='#58718a') => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${stroke}" stroke-width="2"/>`;
  const line = (x1,y1,x2,y2,color='#42566b',width=3) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${width}" stroke-linecap="round"/>`;
  const dot = (cx,cy,r=10,fill='#fda4af') => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="#526579" stroke-width="1.5"/>`;
  const frame = (title, inner) => `<figure class="math-diagram primary-math-visual"><figcaption>📘 Workbook visual · ${esc(title)}</figcaption><svg viewBox="0 0 800 280" role="img" aria-label="${esc(title)}"><style>text{font-family:Arial,'Segoe UI',sans-serif}.pm-muted{fill:#64748b;font-size:14px;font-weight:600}.pm-grid{stroke:#cbd5e1;stroke-width:1}</style>${inner}</svg></figure>`;
  const board = (labels, values) => {
    let s=''; const x0=90, y0=68, w=620, cw=w/labels.length;
    labels.forEach((v,i)=>{s+=rect(x0+i*cw,y0,cw,54,i===0?'#dbeafe':i===1?'#fef3c7':'#dcfce7',5);s+=txt(x0+(i+.5)*cw,y0+22,v,15);s+=txt(x0+(i+.5)*cw,y0+46,values[i],18);});
    return s;
  };
  const numberLine = (start,end,highlight,step=1) => {
    let s=line(70,150,730,150,'#526579',4)+`<path d="M730 150l-13-8v16z" fill="#526579"/>`;
    const count=(end-start)/step;
    for(let i=0;i<=count;i++){const x=80+i*(640/count),v=start+i*step;s+=line(x,142,x,160,'#526579',2)+txt(x,188,String(v),14,'middle',v===highlight?'#dc2626':'#334155');}
    if(highlight!==undefined){const x=80+(highlight-start)/step*(640/count);s+=dot(x,150,8,'#fb7185');}
    return s;
  };
  const clock = (cx,cy,hour,minute,label) => {
    let s=`<circle cx="${cx}" cy="${cy}" r="78" fill="#fffdf4" stroke="#53677d" stroke-width="4"/>`;
    for(let i=0;i<12;i++){const a=i*Math.PI/6-Math.PI/2,x=cx+62*Math.cos(a),y=cy+62*Math.sin(a);s+=txt(x,y+5,String(i||12),13);}
    const ma=minute*Math.PI/30-Math.PI/2,ha=(hour%12+minute/60)*Math.PI/6-Math.PI/2;
    s+=line(cx,cy,cx+47*Math.cos(ha),cy+47*Math.sin(ha),'#e35d6a',5)+line(cx,cy,cx+64*Math.cos(ma),cy+64*Math.sin(ma),'#2767a1',3)+dot(cx,cy,5,'#34495e');
    s+=txt(cx,cy+108,label,15);return s;
  };
  const shape = (type,x,y,size,fill) => {
    if(type==='circle')return `<circle cx="${x}" cy="${y}" r="${size/2}" fill="${fill}" stroke="#526579" stroke-width="2"/>`;
    if(type==='triangle')return `<polygon points="${x},${y-size/2} ${x-size/2},${y+size/2} ${x+size/2},${y+size/2}" fill="${fill}" stroke="#526579" stroke-width="2"/>`;
    if(type==='rectangle')return `<rect x="${x-size*.65}" y="${y-size*.38}" width="${size*1.3}" height="${size*.76}" rx="3" fill="${fill}" stroke="#526579" stroke-width="2"/>`;
    if(type==='diamond')return `<polygon points="${x},${y-size/2} ${x+size/2},${y} ${x},${y+size/2} ${x-size/2},${y}" fill="${fill}" stroke="#526579" stroke-width="2"/>`;
    return `<rect x="${x-size/2}" y="${y-size/2}" width="${size}" height="${size}" rx="3" fill="${fill}" stroke="#526579" stroke-width="2"/>`;
  };
  let s=''; let title='';
  switch(key){
    case 'count': case 'count100': {
      title=key==='count'?'Count each object once':'Hundreds chart and counting groups';
      const n=key==='count'?12:40, cols=key==='count'?6:10, r=key==='count'?2:4, w=key==='count'?68:60, x0=400-(cols*w)/2;
      for(let i=0;i<n;i++){const x=x0+(i%cols)*w+30,y=70+Math.floor(i/cols)*42;s+=dot(x,y,12,colors[i%colors.length])+txt(x,y+5,String(i+1),11);}
      s+=txt(400,250,key==='count'?'Point, count, then write the number':'Ten objects in each row · count by tens',16,'middle','#50657a');break;
    }
    case 'blocks2': case 'blocks3': {
      title=key==='blocks2'?'Tens and ones: 34 = 30 + 4':'Hundreds, tens and ones: 426 = 400 + 20 + 6';
      const h=key==='blocks2'?3:4,t=key==='blocks2'?3:2,o=key==='blocks2'?4:6;
      s+=txt(170,40,'Base-ten blocks',18);for(let i=0;i<h;i++)s+=rect(80+i*58,62,44,150,'#b8d7f3',4,'#46739e')+Array.from({length:9},(_,j)=>line(80+i*58,62+j*18.7,124+i*58,62+j*18.7,'#6f9bc1',1)).join('');
      for(let i=0;i<t;i++)s+=rect(305+i*35,62,27,150,'#ffe6a1',3,'#a37821')+Array.from({length:9},(_,j)=>line(305+i*35,62+j*18.7,332+i*35,62+j*18.7,'#d0a74d',1)).join('');
      for(let i=0;i<o;i++)s+=rect(470+(i%3)*38,68+Math.floor(i/3)*38,30,30,'#9ee6b1',3,'#44865a');
      s+=board(key==='blocks2'?['Tens','Ones']:['Hundreds','Tens','Ones'],key==='blocks2'?['3 tens','4 ones']:['4 hundreds','2 tens','6 ones']);break;
    }
    case 'line': title='Numbers in order on a number line';s+=numberLine(0,10,5);s+=txt(400,65,'Before ←             → After',18,'middle','#334155');break;
    case 'compare2':case 'compare3':
      title=key==='compare2'?'Compare tens, then ones':'Compare hundreds, tens, then ones';
      s+=board(key==='compare2'?['Tens','Ones']:['Hundreds','Tens','Ones'],key==='compare2'?['5 vs 2','2 vs 5']:['3 vs 3','6 vs 5','8 vs 2']);
      s+=rect(150,160,180,62,'#eff6ff')+txt(240,202,key==='compare2'?'52':'368',25);
      s+=txt(400,205,key==='compare2'?'>':'<',38,'middle','#dc2626');
      s+=rect(470,160,180,62,'#fff7ed')+txt(560,202,key==='compare2'?'25':'382',25);break;
    case 'ordinal': case 'ordinal20':
      title=key==='ordinal'?'Position and repeating patterns':'Ordinal places in a line';
      for(let i=0;i<5;i++){let x=105+i*145;s+=rect(x,82,112,88,colors[i],12)+txt(x+56,116,['1st','2nd','3rd','4th','5th'][i],22)+shape(['circle','square','triangle','circle','square'][i],x+56,150,26,'#ffffff');}
      s+=txt(400,232,key==='ordinal'?'Find the position · circle, square, circle, square…':'First, second, third … twentieth',17);break;
    case 'join':case 'tenframe':case 'takeaway':case 'missing':case 'addColumns':case 'addColumns3':case 'subtract3':case 'skipCount': {
      const cfg={join:['Join two groups','8 + 4 = 12'],tenframe:['Make a ten','7 + 5 = 12'],takeaway:['Take away and count what remains','9 − 4 = 5'],missing:['Find the missing part','7 + □ = 12'],addColumns:['Add tens and ones','27 + 18 = 45'],addColumns3:['Add three-digit numbers','268 + 157 = 425'],subtract3:['Subtract by regrouping','352 − 178 = 174'],skipCount:['Count in tens and hundreds','10, 20, 30 … 100']}[key];
      title=cfg[0];
      if(key==='addColumns'||key==='addColumns3'||key==='subtract3'){
        s+=board(key==='addColumns'?['Tens','Ones']:['Hundreds','Tens','Ones'],key==='addColumns'?['2 + 1','7 + 8']:key==='addColumns3'?['2 + 1 + 1','6 + 5 + 1','8 + 7']:['3 − 1','5 → 14','2 → 12']);
        s+=txt(400,180,cfg[1],30,'middle','#1e5b84');s+=txt(400,228,'Line up each place · regroup when needed',16,'middle','#53677d');
      } else if(key==='skipCount') {s+=numberLine(0,100,50,10);s+=txt(400,60,'Add 10 each step · 10 hundreds make 1,000',18);}
      else {
        const groups=key==='join'?[8,4]:key==='takeaway'?[9,0]:key==='missing'?[7,0]:[7,5];
        const a=groups[0],b=groups[1];
        for(let i=0;i<a;i++)s+=dot(120+(i%5)*38,95+Math.floor(i/5)*42,13,colors[0]);
        s+=txt(310,137,key==='takeaway'?'−':key==='missing'?'+ □':'+',36,'middle','#34495e');
        for(let i=0;i<b;i++)s+=dot(390+(i%5)*38,95+Math.floor(i/5)*42,13,colors[2]);
        s+=txt(400,225,cfg[1],23,'middle','#1e5b84');
      }break;
    }
    case 'length':case 'height':case 'rulerMeasure':
      title=key==='height'?'Compare heights from the same base':key==='rulerMeasure'?'Read centimetres on a ruler':'Compare lengths from the same starting point';
      s+=line(90,210,710,210,'#475569',4);
      for(let i=0;i<=20;i++){const x=100+i*30;s+=line(x,210,x,210-(i%5===0?27:13),'#53677d',2);if(i%5===0)s+=txt(x,238,String(i),12);}
      s+=rect(145,125,key==='rulerMeasure'?290:175,28,'#f8a66b',4)+rect(145,170,key==='rulerMeasure'?440:315,28,'#73c5d8',4);
      s+=txt(545,145,key==='height'?'same ground':'cm',17);s+=txt(545,190,key==='height'?'compare top edge':'0 cm →',17);break;
    case 'balance':case 'mass': {
      title=key==='mass'?'Compare mass on a balance scale':'Heavier and lighter objects';
      s+=line(400,72,400,205,'#7c5a3b',7)+line(315,205,485,205,'#7c5a3b',6)+line(250,116,550,116,'#50657a',5);
      s+=line(280,116,248,180,'#50657a',3)+line(280,116,312,180,'#50657a',3)+line(520,116,488,180,'#50657a',3)+line(520,116,552,180,'#50657a',3);
      s+=`<path d="M220 180q60 35 120 0M460 180q60 35 120 0" fill="#fff0c9" stroke="#805d2b" stroke-width="3"/>`;
      s+=dot(280,145,19,'#ffcd69')+dot(520,145,12,'#a8d8f0')+txt(280,170,'1 kg',15)+txt(520,170,'500 g',15);break;
    }
    case 'money':case 'moneyCount':case 'moneyWays':case 'change': {
      title=key==='money'?'Pakistani rupee coins and notes':'Count, compare and make the same amount';
      const coin=(x,y,r,label,col)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${col}" stroke="#86672d" stroke-width="3"/><circle cx="${x}" cy="${y}" r="${r-6}" fill="none" stroke="#d7b766" stroke-width="2"/>${txt(x,y+5,label,14)}`;
      if(key==='money'||key==='moneyCount'){
        [5,10,20].forEach((v,i)=>s+=coin(155+i*155,120,43,`Rs ${v}`,['#f1d58c','#d5dce3','#efc978'][i]));
        s+=rect(100,190,135,48,'#a7d6b5')+txt(168,220,'Rs 50 note',16)+rect(330,190,135,48,'#f2c3b8')+txt(398,220,'Rs 100',16)+txt(635,215,'Read each value',16);
      } else if(key==='moneyWays') {s+=coin(200,130,42,'10','#efd58c');s+=txt(400,143,'=',30);s+=coin(535,105,32,'5','#cfd8df')+coin(605,155,32,'5','#cfd8df');s+=txt(400,226,'Rs 10 = one Rs 10 coin = two Rs 5 coins',17);}
      else {s+=rect(100,65,250,90,'#e8f1fc')+txt(225,102,'Toy  Rs 35',20)+rect(450,65,250,90,'#fff1d3')+txt(575,102,'Paid  Rs 50',20)+txt(400,200,'Change = 50 − 35 = Rs 15',23,'middle','#167453');}
      break;
    }
    case 'clock':case 'clockDigital':case 'clockTimes':
      title='Read the short hour hand and long minute hand';
      if(key==='clock')s+=clock(400,120,3,0,'3:00 · exact hour');
      else if(key==='clockDigital'){s+=clock(260,118,7,0,'Analogue');s+=rect(440,78,220,85,'#e8f7ec',12,'#4a8060')+txt(550,132,'7:00',38,'middle','#167453')+txt(550,190,'Digital',16);}
      else {s+=clock(180,115,2,15,'2:15');s+=clock(400,115,4,30,'4:30');s+=clock(620,115,7,45,'7:45');}break;
    case 'dayNight':
      title='Parts of a day and a.m. / p.m.';
      s+=`<circle cx="220" cy="115" r="48" fill="#ffd36c" stroke="#e0a23d" stroke-width="3"/><path d="M490 150a48 48 0 1 1 46-68 38 38 0 1 0 -46 68" fill="#c5d1ef" stroke="#536783" stroke-width="3"/>`;
      s+=txt(220,205,'Morning · a.m.',19)+txt(530,205,'Evening · p.m.',19)+txt(400,255,'Sunrise → noon → sunset → night',16);break;
    case 'week':case 'months':case 'calendarPair':
      title=key==='week'?'Seven days in a repeating week':'Solar and lunar calendars';
      if(key==='week'){['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].forEach((d,i)=>{s+=rect(60+i*98,102,88,54,colors[i%colors.length],6)+txt(104+i*98,136,d,16);});s+=txt(400,208,'After Sunday, Monday begins again',18);}
      else {['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'].forEach((d,i)=>{const x=86+(i%6)*128,y=50+Math.floor(i/6)*86;s+=rect(x,y,112,66,colors[i%colors.length],6)+txt(x+56,y+25,d,15)+txt(x+56,y+49,'1  8  15  22',11);});s+=txt(400,238,'Solar year: 12 months · Lunar calendar follows the Moon',16);}
      break;
    case 'flatShapes':case 'shapeObjects':case 'solidGallery3':case 'sidesCircle':
      title=key==='solidGallery3'?'Flat 2-D shapes and solid 3-D objects':'Shapes, sides, corners and circles';
      if(key==='sidesCircle'){
        s+=shape('triangle',160,116,82,'#ffd36c')+shape('square',345,116,76,'#8ed8af')+shape('circle',535,116,78,'#9bc8ef')+shape('rectangle',680,116,72,'#f6a9ad');
        s+=txt(160,218,'3 sides · 3 vertices',14)+txt(345,218,'4 sides · 4 vertices',14)+txt(535,218,'0 corners',14)+txt(680,218,'4 sides · 4 vertices',14);
      } else if(key==='solidGallery3'){
        s+=rect(65,78,140,116,'#8ec5ed',10)+txt(135,225,'Cube',18);
        s+=`<ellipse cx="325" cy="125" rx="54" ry="66" fill="#ffbd82" stroke="#526579" stroke-width="3"/>`+txt(325,225,'Sphere',18);
        s+=`<path d="M435 184L490 75l56 109z" fill="#b8dfa0" stroke="#526579" stroke-width="3"/>`+txt(490,225,'Cone',18);
        s+=`<path d="M600 80h100v110q-50 25-100 0z" fill="#d0b8ed" stroke="#526579" stroke-width="3"/><ellipse cx="650" cy="80" rx="50" ry="15" fill="#eee5fa" stroke="#526579" stroke-width="3"/>`+txt(650,225,'Cylinder',18);
      } else {
        s+=shape('circle',130,125,72,'#9bc8ef')+shape('triangle',310,125,80,'#ffd36c')+shape('square',500,125,75,'#8ed8af')+shape('rectangle',680,125,70,'#f6a9ad');
        s+=txt(130,220,'Circle',16)+txt(310,220,'Triangle',16)+txt(500,220,'Square',16)+txt(680,220,'Rectangle',16);
      }break;
    case 'pattern':case 'gridPattern':
      title='Continue the repeating shape and colour pattern';
      if(key==='pattern'){for(let i=0;i<8;i++)s+=shape(['triangle','circle','square','triangle','circle','square','triangle','circle'][i],105+i*85,125,42,colors[i%3]);s+=txt(400,215,'What comes next?',18);}
      else {for(let r=0;r<4;r++)for(let c=0;c<8;c++){const x=95+c*78,y=55+r*48;s+=rect(x,y,60,38,'#fff',2,'#aab8c6');if((r+c)%3===0)s+=shape('triangle',x+30,y+19,24,colors[r%colors.length]);else if((r+c)%3===1)s+=dot(x+30,y+19,12,colors[(c+1)%colors.length]);else s+=rect(x+20,y+9,20,20,colors[(r+c)%colors.length],1,'#65758b');}s+=txt(400,270,'Rows and columns keep each repeating group aligned',14);}
      break;
    case 'position':case 'path':
      title=key==='position'?'Inside, outside, above and below':'Near, far, over, under, before and after';
      s+=rect(285,60,230,165,'#f6f8fb',6,'#75879a')+rect(330,145,140,54,'#b9d4eb',4,'#536d87')+`<path d="M360 145v-45l35-28 35 28v45z" fill="#ffdb9b" stroke="#526579" stroke-width="3"/>`;
      s+=dot(395,85,8,'#fb7185')+dot(245,110,9,'#7cbd8c')+txt(400,252,'A bird above · a ball inside · a tree outside',15);break;
    case 'fractionLabels':case 'fractionParts':case 'fractionPictures':
      title='Equal parts show fractions';
      if(key==='fractionLabels'){
        s+=rect(100,80,600,86,'#e6eef8',8)+rect(100,80,150,86,'#f5a4a9',8)+line(250,80,250,166,'#ffffff',4)+line(400,80,400,166,'#ffffff',4)+line(550,80,550,166,'#ffffff',4);
        s+=txt(400,214,'1 coloured part out of 4 equal parts = 1/4',21);
      } else {
        [0,1,2].forEach(i=>{
          const cx=180+i*220, parts=i+2, r=62; s+=`<circle cx="${cx}" cy="125" r="${r}" fill="#fff" stroke="#51677c" stroke-width="3"/>`;
          for(let k=0;k<parts;k++){const a1=-Math.PI/2+k*2*Math.PI/parts,a2=-Math.PI/2+(k+1)*2*Math.PI/parts;const x1=cx+r*Math.cos(a1),y1=125+r*Math.sin(a1),x2=cx+r*Math.cos(a2),y2=125+r*Math.sin(a2);s+=`<path d="M${cx} 125 L${x1} ${y1} A${r} ${r} 0 0 1 ${x2} ${y2} Z" fill="${k===0?colors[i]:'#fff'}" stroke="#51677c" stroke-width="2"/>`;}
          s+=txt(cx,220,['1/2','1/3','1/4'][i],18);
        });
      }break;
    case 'multiply':
      title='Multiplication as equal groups and arrays';
      for(let r=0;r<4;r++)for(let c=0;c<3;c++)s+=dot(290+c*54,66+r*40,13,colors[r%colors.length]);
      s+=txt(600,112,'4 groups of 3',19)+txt(600,151,'3 + 3 + 3 + 3',17)+txt(600,195,'4 × 3 = 12',24,'middle','#167453');
      s+=txt(372,250,'Rows × columns make an array',15);break;
    case 'division':
      title='Division shares objects equally';
      for(let i=0;i<12;i++){const group=Math.floor(i/4),item=i%4;s+=dot(190+group*210+(item%2)*35,88+Math.floor(item/2)*42,13,colors[group]);}
      [190,400,610].forEach((x,i)=>{s+=rect(x-65,55,130,105,'none',12,'#8ba0b5');s+=txt(x,192,`Group ${i+1}`,15);});
      s+=txt(400,245,'12 ÷ 3 = 4 in each equal group',22,'middle','#167453');break;
    case 'ruler':
      title='Read centimetres on a ruler';s+=line(70,135,730,135,'#6b5136',6);for(let i=0;i<=20;i++){let x=80+i*32;s+=line(x,135,x,135-(i%5===0?52:25),'#705d46',2);if(i%5===0)s+=txt(x,174,String(i),14);}s+=rect(176,77,190,28,'#ffb967',5)+txt(270,98,'pencil · 9 cm',15);break;
    case 'mass': title='Compare grams and kilograms with a balance';s+=line(400,58,400,207,'#70563c',7)+line(300,205,500,205,'#70563c',7)+line(230,105,570,105,'#526579',5)+line(250,105,220,177)+line(250,105,280,177)+line(550,105,520,177)+line(550,105,580,177)+`<path d="M190 177q60 38 120 0M490 177q60 38 120 0" fill="#e7f4ff" stroke="#526579" stroke-width="3"/>`+txt(250,155,'1 kg',16)+txt(550,155,'500 g',16);break;
    case 'capacity':
      title='Compare how much liquid containers hold';
      [[135,150,74,'#bfe8ff','1 L'],[300,120,82,'#9ed6f4','2 L'],[485,155,76,'#c7e9f7','500 mL'],[665,100,88,'#b4e2f3','3 L']].forEach(([x,h,w,c,label])=>{s+=`<path d="M${x-w/2} ${208-h}h${w}l-8 ${h}q-30 20 -${w-16} 0z" fill="${c}" stroke="#526579" stroke-width="3"/>`;s+=line(x-w/2,208-h/2,x+w/2,208-h/2,'#4499c1',2)+txt(x,236,label,15);});break;
    case 'measureAdd':
      title='Add measurements in matching units';s+=board(['Length','Mass','Capacity'],['cm + cm','g + g','mL + mL']);s+=rect(100,160,600,56,'#f1f8ed',8,'#628560')+txt(400,195,'Change to the same unit before adding',18);break;
    case 'clockTimes':
      title='Read times from the clock face';s+=clock(180,118,2,15,'2:15');s+=clock(400,118,4,30,'4:30');s+=clock(620,118,7,45,'7:45');break;
    case 'calendarPair':
      title='Calendar months and days';
      for(let m=0;m<2;m++){const x=105+m*330;s+=rect(x,48,280,170,'#fff',5,'#b1bdc9');s+=rect(x,48,280,32,m?'#c9dbff':'#bde8ce',5);s+=txt(x+140,70,m?'LUNAR MONTH':'SOLAR MONTH',14);['S','M','T','W','T','F','S'].forEach((d,i)=>s+=txt(x+22+i*39,102,d,12));for(let i=0;i<28;i++){const xx=x+22+(i%7)*39,yy=126+Math.floor(i/7)*21;s+=txt(xx,yy,String(i+1),11);}}
      s+=txt(400,255,'Use the column headings to find each date’s day',15);break;
    case 'lineTypes':
      title='Straight lines and curved lines';
      s+=line(105,95,345,95,'#2f7197',8)+txt(225,137,'Straight',18);s+=`<path d="M455 115q70-85 130 0t110 0" fill="none" stroke="#d77b57" stroke-width="8" stroke-linecap="round"/>`+txt(595,165,'Curved',18);break;
    case 'roman':
      title='Roman numeral reference chart';
      [['I','1'],['II','2'],['III','3'],['IV','4'],['V','5'],['VI','6'],['VII','7'],['VIII','8'],['IX','9'],['X','10']].forEach((a,i)=>{const x=105+(i%5)*120,y=58+Math.floor(i/5)*86;s+=rect(x,y,100,60,colors[i%colors.length],5)+txt(x+50,y+24,a[0],20)+txt(x+50,y+48,a[1],15);});break;
    default: return '';
  }
  return frame(title, s);
}
