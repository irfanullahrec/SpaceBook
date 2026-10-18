from physics_agent1_sequential import save, render, crop
paras=[
 'All the quantities we deal in physics require measurements. This chapter is built on Unit 8: Measurement of physical quantities of general science for grade 8.',
 'Measurement is not only a key concern in physics; in our daily life we are always making measurements. For example when we go to a tailor shop before sewing our cloths he takes the required measurements.',
 '1.1 INTRODUCTION TO PHYSICS',
 'Man has always been curious to know the ‘how’ and ‘why’ behind the working and function of things. He asks the fundamental questions like how did the universe begin? How does it change? What rules govern its behaviour? Why do things fall to the ground? Why does the moon seem to change shape during the month? What goes inside the sun to make it hot? Physics is all about trying to answer questions like these. All of these phenomena in the universe involve the study of matter and energy.',
 'TELESCOPE: The telescope in the foreground is Gemini North, one of a pair of twin 8.1-m telescopes located on Mauna Kea in Hawaii. Together, these two telescopes are used to see the visible universe.',
 '‘Physics is the branch of science that involves the study of physical universe: energy, matter, and how they are related’.',
 'The study of physics is to understand the world around us, the world inside us and the world beyond us. Physics covers a wide range of phenomena, from the smallest sub-atomic particles to the largest galaxies and universe.',
 'Physicists investigate the motions of electrons and rockets, the energy in sound waves and electric circuits, the structure of the proton and of the universe.',
 'Mathematics-The Language of Physics: Physics and human conditions improved when mathematics was incorporated in physics some 400 years ago. When the ideas of physics are expressed in mathematical terms, they are clearer. They don’t have multiple meanings that so often confuse the discussion of ideas expressed in common language.',
 'MILKY WAY GALAXY: Our solar system is located in a large spiral-shaped galaxy called the Milky Way and the Sun is just one of at least 100 billion stars in this galaxy.',
 'The equations of physics provide compact expressions of relationships between concepts. Also when findings in nature are expressed mathematically, they are easier to verify or to disprove by experiment.'
]
figures=[dict(src=crop(7,'printed002-telescope.png',(.573,.226,.794,.345)),alt='Gemini North telescope on Mauna Kea in Hawaii.',caption='TELESCOPE'),
 dict(src=crop(7,'printed002-milky-way.png',(.574,.595,.795,.715)),alt='Spiral-shaped Milky Way galaxy.',caption='MILKY WAY GALAXY')]
save(dict(pdfPage=7,printedPage=2,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',
 title='1.1 Introduction to Physics',sections=[dict(code='1.1',heading='1.1 Introduction to Physics',paras=paras,figures=figures)],
 comparison='Restored missing opening paragraphs, repaired split telescope caption and proton sentence, removed stray footer, preserved both photographs'))
render(8)
