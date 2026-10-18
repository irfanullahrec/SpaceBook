from physics_agent2_sequential import save_page

CREDITS = [
    'All rights reserved with the Leading Books Publishers, Peshawar.',
    'Reviewed and Approved by: Directorate of Curriculum and Teachers Education, Abbottabad vide NOC No: 2678-80/Physics-XII//F.01/Vol-1/NC-2006 Dated: 06.05.2021',
    'According to National Curriculum 2006',
    'Authors:',
    'Prof. Shaukat Ali Taran — Government Post Graduate College Timergara',
    'Shadah Gul, Assistant Prof. — Government Post Graduate College, Lakki Marwat',
    'Dr. Naeem Khalid — Dean of Sciences, Islamia College, Peshawer',
    'Prof. Abdul Baseer — Edwardes College, Peshawer',
    'Abdul Rehman, Lecturer — Akram Khan Durrani College Bannu',
    'Aamir Ullah Khan — Director, Pakistan Virtual College, Hayatabad Peshawar',
    'Hafiz Mehar Elahi — Peshawar Model Degree College, Peshawer',
    'Review Supervision: Gohar Ali Khan, Director, Curriculum and Teachers Education, Abbottabad.',
    'Focal Person: Zulfiqar Khan, Additional Director (Curriculum and Textbook Review) DCTE, Abbottabad.',
    'Re-reviewers:',
    'Two faint reviewer names are preserved in the source crop below; their spelling remains unresolved. Affiliations: Associate Prof. G.P.G College Mandian, Abbottabad; (Subject Specialist) GHSS Bandi Dhundan, Abbottabad.',
    'Muhammad Arshid — (Subject Specialist) GHSS Lassan Thakral, Mansehra',
    'Shafqat Hussain — (Subject Specialist) Desk Officer, DCTE, Abbottabad',
    'Nasir Kamal — (Assistant Subject Specialist) Khyber Pakhtunkhwa Textbook Board, Peshawar',
    'Editor: Nasir Kamal, Assistant Subject Specialist (Physics), Khyber Pakhtunkhwa Textbook Board, Peshawar.',
    'Printing Supervision: Rashid khan Paindakhel (Chairman); Saeedur Rehman (Member E&P), Khyber Pakhtunkhwa Textbook Board, Peshawar',
    'Academic Year 2021-22', 'Email: membertbb@yahoo.com', 'Website: www.kptbb.gov.pk', 'Phone: 091-9217159-60',
]

PREFACE = [
    'This book is based on national curriculum 2006. In this edition some topics, diagrams, numerical questions, have been improved, and some brainstorming questions, assignments, projects are added to enhance the learning capacity of students.',
    'Throughout the book an attempt has been made to present the mathematical symbols in italic for its easy understanding.',
    'In case of any errors we request the readers to point out these errors so that they are eliminated in the next edition. I hope that the teachers, students, and experts will keep us informed about the textbook, so that we may be able to improve the textbook, because there is always room for improvement. For feedback and comment mail us at: nasirkamal2@yahoo.com',
    'Editor',
]

if __name__ == '__main__':
    from pathlib import Path
    import pymupdf
    assets=Path(__file__).resolve().parents[1]/'assets/physics12'
    assets.mkdir(parents=True,exist_ok=True)
    source=Path(__file__).resolve().parents[2]/'Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
    pdf=pymupdf.open(source)
    pdf[3].get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(68,311,290,369)).save(assets/'faint-reviewer-names.png')
    save_page(4,[{'id':'phys12-front-publication','printedPage':None,'title':'Publication information','paragraphs':CREDITS,
                 'figures':[{'src':'assets/physics12/faint-reviewer-names.png','alt':'Original two faint reviewer names and their affiliations','caption':'Unresolved spelling of two reviewer names; original source retained.'}],
                 'sourceDefects':['Two pale reviewer names remain unreadable with confidence in both full PDF and original JPG. Narrow source crop retained; no spelling invented.']},
                {'id':'phys12-front-preface','printedPage':None,'title':'Preface','paragraphs':PREFACE}])
