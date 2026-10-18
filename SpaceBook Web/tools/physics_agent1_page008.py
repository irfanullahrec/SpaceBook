from physics_agent1_sequential import save, render, crop
paras=[
 'Physics and Science:',
 'Physics is at the root of every field of science. Most of the major developments in Chemistry, Biology, Geology, Agricultural, Environmental science, Astronomy, Engineering and even in medicine have been made by physicists.',
 'Physics, Technology and its Impact on our Society:',
 'Physics and technology are closely related however they are also different from each other. Physics is concerned with gathering knowledge and organizing it. Technology lets humans use that knowledge for practical purposes. Physical phenomenon is there behind every technology and therefore physics has a key role in the progress of humankind and in the improvement of quality of living.',
 'Recall GENERAL SCIENCE for GRADE 7. CHAPTER 11, CIRCUITS AND ELECTRIC CURRENT:',
 'You have already used mathematics in physics when you defined electric current ‘I’, as time rate of flow of electric charge ‘Q’ through a given cross-section of a conductor as',
 'I = Q/t, where I = current, Q = charge, t = time.',
 'Physics provide basic understanding for developing new instrumentation for medical applications such as Computed Tomography (CT Scan), Magnetic Resonance Imaging (MRI), and laser surgeries. The image shown an advance medical imaging device called Positron Emission Tomography (PET).',
 'The use of physics in information technology has improved the standard of communication. Mobile cell phones are commonly used even by illiterates. Hologram technology is a three-dimensional image, created with photographic projection. The hologram technology is also incorporated in cell phones.',
 'QURAAN AND PHYSICS',
 'It is generally accepted that there are more than 700 Ayah in the Quran dealing with the natural phenomena. Many Ayah of Quran ask mankind to study nature, few are described.'
]
figures=[dict(src=crop(8,'printed003-pet.png',(.576,.485,.793,.623)),alt='Positron Emission Tomography medical scanner.',caption='PET'),
 dict(src=crop(8,'printed003-hologram.png',(.579,.637,.8,.769)),alt='Illustration of a three-dimensional hologram projected from a cell phone.',caption='HOLOGRAM')]
save(dict(pdfPage=8,printedPage=3,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',
 title='Physics and Science / Physics, Technology and Society',sections=[dict(code='1.1',heading='1.1 Introduction to Physics',paras=paras,figures=figures,
 blocks=[dict(type='formula',latex='I=\\frac{Q}{t}',symbols=dict(I='current',Q='charge',t='time'))])],
 comparison='Separated interleaved recall and technology text, restored missing electric-current formula and symbols, retained both source figures'))
render(9)
