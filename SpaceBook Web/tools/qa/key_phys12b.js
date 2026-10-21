// second batch of hand-derived keys for Class 12 Physics MCQs (Unit 12 copies) that print no answer
const fs=require('fs');const f='js/phys_12_data.js';let s=fs.readFileSync(f,'utf8');
const K=[['A wire of uniform cross-section, area A, length L and resistance R is cut into two equal parts. The resistivity of each part will be','C'],
['How much voltage is required to make 2 A flow through a resistance of 8 Ω?','C'],
['In a Wheatstone bridge method, the bridge is said to be balanced, when the current through the galvanometer is','B'],
['In order to achieve high accuracy, the slide wire of a potentiometer should be','A'],
['Resistance of a wire is r ohms. The wire is stretched to double its length, then its resistance in ohms is','B'],
['The powers of two electric bulbs are 100 W and 200 W. Which are connected to power supply of 220 V? The ratio of resistance of their filament will be','B'],
['Thermocouple is an arrangement of two different metals','A'],
['Three resistors of resistance R each are combined in various ways. Which of the following cannot be obtained?','B'],
['Two bulbs marked 200 watt–250 volts and 100 watt–250 volts are joined in series to a 250 volts supply. Power consumed in circuit is','B'],
['When a wire is stretched and its radius becomes r/2, then its resistance will be','A'],
['When n resistances each of value r are connected in parallel, the resultant resistance is x. When these n resistances are connected in series, total resistance is','D'],
['\\(10^6\\) electrons are moving through a wire per second. The current developed is','C'],
['The resistivity of two wires is \\(\\rho_1\\) and \\(\\rho_2\\), which are connected in series. If their dimensions are same, then the equivalent resistivity of the combination will be','C'],
['When a potentiometer is used for measurement of voltage of an unknown source, the power consumed in the circuit of the unknown source under null condition is','C']];
const note='Derived (the textbook prints no key); worked out and checked by hand.';let n=0;
for(const [q,a] of K){const needle='"question": '+JSON.stringify(q);let from=0,hit=0;
 for(;;){const i=s.indexOf(needle,from);if(i<0)break;from=i+needle.length;
  const nextQ=s.indexOf('"question": ',from);const seg=s.slice(i,nextQ<0?s.length:nextQ);
  const seg2=seg;if(/"(answer|correct)": ("[A-Da-d]"|[0-9])/.test(seg2)||!/"choices"/.test(seg2)){continue;}
  const j=s.indexOf('"choices"',i);const indent=s.slice(s.lastIndexOf('\n',j)+1,j);
  s=s.slice(0,j)+'"answer": "'+a+'",\n'+indent+'"answerOrigin": "'+note+'",\n'+indent+s.slice(j);n++;hit++;from=j+200;}
 if(!hit)console.log('no hit',q.slice(0,50));}
fs.writeFileSync(f,s);console.log('keyed',n);
