from physics_agent1_sequential import save, render, crop
objectives=[
 'Describe the crucial role of Physics in Science, Technology and Society.',
 'Explain with examples that Science is based on physical quantities which consist of numerical magnitude and a unit.',
 'Differentiate between base and derived physical quantities.',
 'List the seven units of System International (SI) along with their symbols and physical quantities.',
 'Interconvert the prefixes and their symbols to indicate multiples and sub-multiples for both base and derived units.',
 'Write the answer in scientific notation in measurements and calculations.',
 'Describe the working of vernier callipers and screw gauge for measuring length.',
 'Identify and explain the limitation of measuring instruments such as metre rule, vernier callipers and screw gauge.',
 'Describe the need for using significant figures for recording and stating results in the laboratory.'
]
src=crop(6,'printed001-dashboard.png',(.187,.135,.79,.49))
save(dict(pdfPage=6,printedPage=1,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',
 title='PHYSICAL QUANTITIES AND MEASUREMENT',objectives=objectives,
 sections=[dict(code='source-u1-opening',heading='Unit 1: Physical Quantities and Measurement',
 paras=['We need Measurement for safe driving a car','After studying this unit you should be able to:',*objectives],
 figures=[dict(src=src,alt='Car dashboard instruments illustrating the need for measurement in safe driving.',caption='We need Measurement for safe driving a car')])],
 comparison='Existing nine SLO summaries differed from original wording; replaced with exact checklist; opening dashboard image retained'))
render(7)
