from physics_agent1_sequential import save, render, crop
paras=[
 'Ibnal Haitham (965 - 1039) A.D',
 'He was born in Busra, Iraq. He was great scholar of his time. His greatest work is the book on optics named KITAB UL MANAZIR. He is also considered as the inventor of the pin-hole camera.',
 'Al Beruni (973-1048) A.D',
 'He is afghan scholar and wrote about 150 books on physics, cosmology, geography; culture, archeology and medicine. Al Beruni discussed the shape of earth, the movement of sun, moon and phases of moon.',
 'FAMOUS PAKISTANI PHYSICISTS',
 'Dr. Ishfaq Ahmad (1930-2018)',
 'Dr. Ishfaq Ahmad an eminent nuclear physicist, contributed enormously for Pakistan. He has served as Chairman of Pakistan Atomic Energy Commission from 1991 to 2001. He was the proud recipient of three highest civil awards in Pakistan: Sitara-i-Imtiaz, Hilal-i-Imtiaz and Nishan-i-Imtiaz, for his contributions towards science, especially in the fields of nuclear, particle, and quantum electrodynamics. His tireless efforts led to the creation of Global Change Impact Studies Centre in Islamabad where research on climatic change is being undertaken in Pakistan, an initiative of its own kind.',
 'Abdul Qadeer Khan (1936 - 2021)',
 'Abdul Qadeer Khan known as A. Q. Khan (born on 27 April 1936) was a Pakistani nuclear physicist and a metallurgical engineer, who founded the Uranium enrichment program for Pakistan’s atomic bomb project. He founded and established Kahuta Research Laboratories (KRL) in 1976, and served as both its Senior Scientist and Director-General until he retired in 2001.'
]
figures=[
 dict(src=crop(10,'printed005-ibnal-haitham.png',(.568,.12,.8,.268)),alt='Textbook portrait of Ibnal Haitham.',caption='IBNAL HAITHAM'),
 dict(src=crop(10,'printed005-al-beruni.png',(.568,.269,.802,.414)),alt='Textbook portrait of Al Beruni.',caption='AL BERUNI'),
 dict(src=crop(10,'printed005-ishfaq-ahmad.png',(.609,.462,.8,.634)),alt='Textbook portrait of Ishfaq Ahmad.',caption='Ishfaq Ahmad'),
 dict(src=crop(10,'printed005-abdul-qadeer.png',(.608,.638,.802,.841)),alt='Textbook portrait of Abdul Qadeer Khan.',caption='Abdul Qadeer Khan')]
save(dict(pdfPage=10,printedPage=5,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',
 title='Contributions by scientists / Famous Pakistani Physicists',sections=[dict(code='1.1',heading='1.1 Introduction to Physics',paras=paras,figures=figures)],
 comparison='Verified biography paragraphs against source, joined broken sentences, retained all four portraits and original headings'))
render(11)
