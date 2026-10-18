"""PDF35 printed 61–62: Example 2.18 solution, 2.4.7 variance of sum/difference of independent r.v.s, Example 2.19."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('By definition', 'تعریف کے مطابق', 'د تعریف له مخې')
b.mlines([r'E(X)=\Sigma x\,p(x)=2\times 0.40+4\times 0.60=0.80+2.40=3.2', r'E(Y)=\Sigma y\,p(y)=1\times 0.25+3\times 0.50+5\times 0.25', r'=0.25+1.50+1.25=3'])
b.p('Now by property', 'اب خاصیت کے مطابق', 'اوس د ځانګړنې له مخې')
b.mlines([r'E(X+Y)=E(X)+E(Y)=3.2+3=6.8', r'E(2X-3Y)=E(2X)-E(3Y)', r'=2E(X)-3E(Y)', r'=2(3.2)-3(3)=6.4-9=-2.6'])
b.p('Since X and Y are independent, therefore,', 'چونکہ X اور Y آزاد ہیں، اس لیے', 'څرنګه چې X او Y خپلواک دي، نو')
b.eq(r'E(XY)=E(X)\,E(Y)=(3.2)(3)=9.6')
b.h('2.4.7 Variance of the sum or difference of two independent random variables', '2.4.7 دو آزاد تصادفی متغیرات کے مجموعے یا فرق کا تغیر', '2.4.7 د دوو خپلواکو تصادفي متغیرونو د مجموعې یا توپیر واریانس')
b.p('If X and Y are two independent random variables, then variance of their sum is given by the formula:', 'اگر X اور Y دو آزاد تصادفی متغیرات ہوں تو ان کے مجموعے کا تغیر اس فارمولا سے ملتا ہے:', 'که X او Y دوه خپلواک تصادفي متغیرونه وي، نو د هغو د مجموعې واریانس له دې فورمول څخه لاسته راځي:')
b.mlines([r'V(X+Y)=E[X+Y-E(X+Y)]^2', r'=E[X+Y-E(X)-E(Y)]^2', r'=E[\{X-E(X)\}+\{Y-E(Y)\}]^2', r'=E[\{X-E(X)\}^2+\{Y-E(Y)\}^2+2\{X-E(X)\}\{Y-E(Y)\}]',
          r'=E[X-E(X)]^2+E[Y-E(Y)]^2+2E\{X-E(X)\}\{Y-E(Y)\}', r'=V(X)+V(Y)+2\,\mathrm{cov}(X,Y)'])
b.p('When X and Y are independent then $\\mathrm{cov}(X,Y)=0$', 'جب X اور Y آزاد ہوں تو $\\mathrm{cov}(X,Y)=0$', 'کله چې X او Y خپلواک وي، نو $\\mathrm{cov}(X,Y)=0$')
b.p('$\\therefore\\ V(X+Y)=V(X)+V(Y)$, Similarly', '$\\therefore\\ V(X+Y)=V(X)+V(Y)$، اسی طرح', '$\\therefore\\ V(X+Y)=V(X)+V(Y)$، همداراز')
b.eq(r'V(X-Y)=V(X)+V(Y)')
b.h('Example 2.19', 'مثال 2.19', 'بېلګه 2.19')
b.p('Consider the following joint probability distribution of two independent random variables X and Y.', 'دو آزاد تصادفی متغیرات X اور Y کی درج ذیل مشترکہ احتمالی تقسیم پر غور کریں۔', 'د دوو خپلواکو تصادفي متغیرونو X او Y لاندې ګډ احتمالي وېش په پام کې ونیسئ.')
b.grid('stat12-t-ex2-19', ['$X\\backslash Y$', '0', '1', '2'], [['0', '0.10', '.20', '.10'], ['1', '0.15', '.30', '.15']])
b.p('Find: (i) V(X), (ii) V(Y), (iii) V(X+Y), (iv) V(X−Y)', 'معلوم کریں: (i) V(X)، (ii) V(Y)، (iii) V(X+Y)، (iv) V(X−Y)', 'پیدا کړئ: (i) V(X)، (ii) V(Y)، (iii) V(X+Y)، (iv) V(X−Y)')
b.h(*SOL)
b.grid('stat12-t-ex2-19-marg', ['$X\\backslash Y$', '0', '1', '2', '$p(x)$'], [['0', '0.10', '.20', '.10', '.40'], ['1', '0.15', '.30', '.15', '.60'], ['$p(y)$', '0.25', '.50', '.25', '1']])
b.mlines([r'(i)\quad V(X)=E(X)^2-[E(X)]^2', r'E(X)=\Sigma x\,p(x)=0(.40)+1(.60)=0+.60=0.60', r'E(X^2)=\Sigma x^2p(x)=0^2(.40)+1^2(.60)=0+.60=0.60', r'\therefore V(X)=0.60-(0.60)^2=0.60-0.36=0.24',
          r'(ii)\quad V(Y)=E(Y^2)-[E(Y)]^2', r'E(Y)=\Sigma y\,p(y)=0(.25)+1(.50)+2(.25)=0+0.50+0.5=1', r'E(Y^2)=\Sigma y^2p(y)=0^2(.25)+1^2(.50)+2^2(.25)=0+.50+1=1.50', r'\therefore V(Y)=1.50-(1)^2=1.50-1=0.50'])
b.p('Since X and Y are independent, therefore,', 'چونکہ X اور Y آزاد ہیں، اس لیے', 'څرنګه چې X او Y خپلواک دي، نو')
b.mlines([r'(iii)\quad V(X+Y)=V(X)+V(Y)=0.24+0.50=0.74', r'(iv)\quad V(X-Y)=V(X)+V(Y)=0.24+0.50=0.74'])
rec = b.build('stat12-p035-variance-sum', 'Example 2.18 solution; 2.4.7 variance of sum/difference — Example 2.19', 'مثال 2.18 کا حل؛ 2.4.7 مجموعے/فرق کا تغیر — مثال 2.19', 'د بېلګې 2.18 حل؛ 2.4.7 د مجموعې/توپیر واریانس — بېلګه 2.19', 35, [61, 62])
issues = [{'id': 'stat12-p62-vx-notation', 'unit': 2, 'printedPage': 62, 'description': 'Example 2.19(i) prints V(X) = E(X)² − [E(X)]²; the intended first term is E(X²) (as used in the next line). Printed form retained.'}]

if __name__ == '__main__':
    save(35, [(2, rec)], issues=issues)
