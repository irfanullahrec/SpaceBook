from physics_agent2_sequential import save_page

PAGE4 = [
    r'The magnitude of the force \(\vec F\) between two electric charges \(q_1\) and \(q_2\) separated by distance r can be expressed as',
    r'\(F\propto q_1q_2\) … (A)', r'\(F\propto\frac{1}{r^2}\) … (B)',
    r'combining Eq(A) & Eq(B): \(F\propto\frac{q_1q_2}{r^2}\) … (11.1)',
    r'\(F=k\frac{q_1q_2}{r^2}\)',
    'Where, k is a constant of proportionality and its value depends upon the system of the units used and the medium between the charges. The electric charges q₁ and q₂ are assumed to be point or localized charges, provided that the size of the bodies carrying the charges is very small as compared to the distance between them.',
    r'In order to show the direction of the force we use unit vector along the line joining the two charges as shown in Fig:11.1.(a). If \(\hat r_{12}\) is unit vector, pointing from the charge \(q_1\) towards the charge \(q_2\), then the force exerted by the charge \(q_1\) on \(q_2\) in vector form is:',
    r'\(\vec F_{21}=k\frac{q_1q_2}{r^2}\hat r_{12}\) … (11.2)',
    r'Similarly if \(\hat r_{21}\) is unit vector, pointing from the charge \(q_2\) towards the charge \(q_1\), then the force exerted by the charge \(q_2\) on \(q_1\) in vector form is:',
    r'\(\vec F_{12}=k\frac{q_1q_2}{r^2}\hat r_{21}\) … (11.3)',
    r'Since \(\hat r_{12}=-\hat r_{21}\). So from Eq: (11.2) and 11.3 we can write',
    r'\(\vec F_{21}=-\vec F_{12}\) … (11.4)',
    r'The force exerted by the charge \(q_1\) on \(q_2\) is conventionally denoted by \(\vec F_{21}\) and the force exerted by the charge \(q_2\) on \(q_1\) is conventionally denoted by \(\vec F_{12}\).',
]
PAGE5 = [
    r'The force \(\vec F_{12}\) exerted by \(q_2\) on \(q_1\) is equal in magnitude to the force \(\vec F_{21}\) exerted by \(q_1\) on \(q_2\) and in the opposite direction as illustrated in Fig 11.2. This proves that Coulomb’s law fits into Newton’s third law.',
    r'The constant k can be generally expressed in terms of permittivity of the free space \(\varepsilon_0\), i.e., \(k=\frac{1}{4\pi\varepsilon_0}\).',
    r'Experimentally measured value of \(\varepsilon_0=8.85\times10^{-12}\;\mathrm{C^2\,N^{-1}\,m^{-2}}\).',
    r'So \(k=\frac{1}{4\pi\varepsilon_0}=9.0\times10^9\;\mathrm{N\,m^2\,C^{-2}}\).',
    'COULOMB’S LAW IN MATERIAL MEDIA',
    'Eq:(11.2) gives the force between two charges when there is air or vacuum between them. But it is experimentally observed that when an insulator is placed between the electric charges, it reduces the force. Permittivity is the property of a medium which affects the magnitude of force between two point charges.',
    'The Coulomb’s force can now be written as',
    r'\(F_{\mathrm{med}}=\frac{1}{4\pi\varepsilon}\frac{q_1q_2}{r^2}\) … (11.5)',
    r'The quantity \(\varepsilon\) is called the permittivity of the medium. For a particular insulator the permittivity of a material medium compared with the permittivity of vacuum is called relative permittivity or dielectric constant \(\varepsilon_r\). Its ratio is given by',
    r'\(\varepsilon_r=\frac{\varepsilon}{\varepsilon_0}\) … (11.6)',
]

if __name__ == '__main__':
    save_page(7,[{'id':'phys12-front-coulomb-equations','printedPage':4,'title':'11.1 Coulomb’s law — Scalar and vector forms','kind':'lesson','paragraphs':PAGE4,
                 'formulas':[{'number':'11.1','latex':r'F\propto q_1q_2/r^2'},{'number':'11.2','latex':r'\vec F_{21}=k(q_1q_2/r^2)\hat r_{12}'},{'number':'11.3','latex':r'\vec F_{12}=k(q_1q_2/r^2)\hat r_{21}'},{'number':'11.4','latex':r'\vec F_{21}=-\vec F_{12}'}]},
                {'id':'phys12-front-permittivity','printedPage':5,'title':'Coulomb’s law in material media','kind':'lesson','paragraphs':PAGE5,
                 'formulas':[{'number':'11.5','latex':r'F_{\mathrm{med}}=\frac{q_1q_2}{4\pi\varepsilon r^2}'},{'number':'11.6','latex':r'\varepsilon_r=\varepsilon/\varepsilon_0'}],
                 'definitions':[{'term':'Permittivity','text':'Property of a medium which affects the magnitude of force between two point charges.'},{'term':'Relative permittivity','text':'Ratio of permittivity of the material medium to permittivity of vacuum.'}]}])
