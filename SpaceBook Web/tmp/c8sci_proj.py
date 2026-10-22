import re
D='D:/SpaceBook/SpaceBook Web/docs/source-verification/class-8/sci/pages/'
def put(pg,pat,text,after_qp=None):
    f=D+f'p{pg}.txt'; L=open(f,encoding='utf8').read().split('\n')
    i=next(k for k,l in enumerate(L) if re.match(pat,l))
    if after_qp:
        i=next(k for k in range(i,len(L)) if L[k].startswith(f'qp {after_qp} '))
        j=i+1
    else:
        j=next((k for k in range(i,len(L)) if L[k].startswith('endexercise') or L[k].startswith('endbox') or (k>i and L[k].startswith('q '))),len(L))
    if j<len(L) and L[j].startswith('sol'): return
    if j-1>=0 and L[j-1].startswith('sol'): return
    L.insert(j,'sol '+text)
    open(f,'w',encoding='utf8',newline='\n').write('\n'.join(L))
T=' ## Project work; one possible plan (Not verified: depends on your own materials and observations).'
put('035',r'q E \| Project','Model plan: use play dough in different colours: a large grey-pink lump for the brain (cerebrum, cerebellum and brain stem), a long thin rope for the spinal cord running down from the brain stem, and thin threads branching out from the brain (cranial nerves) and from the spinal cord (spinal nerves) to the body. Label each part on a card.'+T)
put('049',r'q E \| Project','Model plan: use two long wires of different colours as the two sugar-phosphate backbones, twist them into a spiral (double helix), join them with short wire rungs carrying coloured beads for the base pairs (adenine with thymine, cytosine with guanine), and label the backbone and the bases.'+T)
put('061',r'q E \| Project','Model plan: stick pictures or drawings of colourful biodegradable objects (fruit and vegetable peels, paper, leaves, cotton cloth, wood) on a chart with the title "Save the Environment" and a short message such as "Compost it, do not burn it".'+T)
put('077',r'q E \| Project','Model plan: draw the periodic table outline with its groups and periods; colour some metals brown (sodium, magnesium, iron, copper), the halogens yellow (fluorine, chlorine, bromine, iodine), the noble gases red (helium, neon, argon, krypton, xenon) and some non-metals blue (hydrogen, carbon, nitrogen, oxygen). Commercial uses: noble gases - helium in balloons, neon in signs, argon in light bulbs; alkali metals - sodium in street lamps and salt, potassium in fertilisers, lithium in batteries.'+T,after_qp=None)
put('097',r'q E \| Project','Expected observation: the baking soda and lemon juice (citric acid) fizz because an acid reacts with a base and carbon dioxide gas is released; the mild abrasive and acid remove stains and the basin looks cleaner and shinier after rinsing. Report: aim, materials, steps, observation (fizzing, stains removed), conclusion (citric acid and baking soda react and clean).'+T)
put('111',r'q E \| Project','Model report: jams and jellies contain citric acid (and pectin); tomato ketchup contains acetic acid (vinegar) and citric acid; pickles are preserved in acetic acid (vinegar) or citric acid; toilet cleaners contain strong hydrochloric acid (or sulphuric/oxalic acid), which must be handled carefully. Uses: flavour, preservation and cleaning.'+T)
put('127',r'q E \| Project','Expected result: a flat piece or a ball of foil sinks, but when it is shaped as a wide boat with high sides it floats because it displaces more water, so the upward buoyant force equals its weight and its average density is lower than water; a steel aircraft carrier floats for the same reason (hollow shape displaces water equal to its weight), while a solid rock has a high density and displaces too little water. Adding coins shows how much load the boat can carry before it sinks.'+T)
put('155',r'q E \| Project','Model poster: two columns. Reflection: light bounces back from a surface, angle of incidence = angle of reflection (mirror, still water, shiny spoon). Refraction: light bends when it passes from one medium to another because its speed changes (a straw looks bent in water, a pool looks shallower, lens and spectacles, a rainbow).'+T)
put('173',r'q E \| Project','Model poster: do not touch switches with wet hands; do not overload sockets; use insulated wires and plugs with earth pins; keep children away from sockets; switch off appliances before repair; never touch fallen wires; use circuit breakers and fuses; keep water away from electrical devices.'+T)
put('189',r'q D','Expected result: milk and vinegar (acid) react to form casein, a polymer curd; this is squeezed, coloured red and blue and moulded into shapes which harden into plastic after two days. The idea is that a natural polymer from milk can be made into plastic. Report: materials, steps, observation and uses.'+T)
put('203',r'q E \| Project','Model plan: Group I chooses a planet (for example Mars, probe named "Red Explorer") and lists its weather (dust storms, very low temperature, thin carbon dioxide atmosphere); Group II draws a lander with three instruments (thermometer for temperature, anemometer for wind speed, barometer for pressure) and labels the parts; Group III writes the mission report and presents how the probe collects and sends data back to Earth.'+T)
