from physics_agent1_sequential import save, render
table=dict(id='table1.1',sourceNumber='TABLE 1.1',title='TABLE 1.1 BRANCHES OF PHYSICS',sourcePdfPage=11,sourcePrintedPage=6,
 headers=['Area within physics','Description','Examples'],rows=[
 ['Mechanics','Motion of objects and how it relates to forces','falling objects, friction, weight, spinning objects'],
 ['Heat and Thermodynamics','Heat and temperature and their relation to energy.','melting and freezing processes, engines, refrigerators'],
 ['Oscillations and Waves','To and fro motion','Springs, Water waves, Sound.'],
 ['Optics','Light and the instrument created to use or detect it','Mirrors, Lenses, telescopes, Eye'],
 ['Electricity and Magnetism','Static as well as moving charges and associated physical phenomena','electrical charge, circuitry, magnets, electromagnets'],
 ['Atomic and Nuclear Physics','Structure and properties of individual atoms and nuclei of an atom.','X-rays, LASERS, Nuclear Reactor, MRI, CT Scan, PET Scan'],
 ['Relativity','Moving Objects (including very high speed) and gravitation','Particle accelerators, Nuclear Energy'],
 ['Quantum Physics','Discrete, indivisible units of energy called quanta','The atom and its parts'],
 ['Particle Physics','Nature of the particles that constitute matter and radiation','Quarks, Leptons, Photons, Bosons'],
 ['Cosmology and astrophysics','The origin, evolution, and eventual fate of the universe','Stars, galaxies and black holes'],
 ['Biophysics and Medical Physics','Physical interactions of biological processes and Application of physics health processes such as prevention, diagnosis, and treatment.','MRI, CT Scan, Radiotracers and conduction in living cells.']])
save(dict(pdfPage=11,printedPage=6,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',
 title='BRANCHES OF PHYSICS',tables=[table],sections=[dict(code='1.1',heading='1.1 Introduction to Physics',
 paras=['BRANCHES OF PHYSICS','Due to vast scope and research in physics it is usually divided into a number of branches some of them given below.'],
 blocks=[dict(type='dataTable',**table)])],comparison='Existing branch table had shortened examples and changed headers; all eleven rows rebuilt verbatim and reused in lesson and reference-table views'))
render(12)
