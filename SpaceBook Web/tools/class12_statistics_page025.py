"""PDF25 printed 41–42: Example 2.7 (2X+4), 2.2.4 mathematical expectation, 2.2.5 definition of E(X), Examples 2.8–2.9."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('The probability distribution of the random variable $2X+4$ is', 'تصادفی متغیر $2X+4$ کی احتمالی تقسیم یہ ہے', 'د تصادفي متغیر $2X+4$ احتمالي وېش دا دی')
b.dist('stat12-t-ex2-7-lin', ['0', '8', '6'], ['$\\frac{1}{3}$', '$\\frac{1}{2}$', '$\\frac{1}{6}$'], xlabel='$H(X)=2X+4$', vertical=True)
b.h('2.2.4 Mathematical expectation of a random variable', '2.2.4 تصادفی متغیر کی ریاضیاتی توقع', '2.2.4 د تصادفي متغیر ریاضي تمه')
b.p('Hope you have understood random variable and its presentation methods like probability distribution and probability function. Now we want to study its properties like mean, variance and standard deviation etc.',
    'امید ہے آپ تصادفی متغیر اور اس کی پیشکش کے طریقے جیسے احتمالی تقسیم اور احتمالی تفاعل سمجھ چکے ہیں۔ اب ہم اس کی خصوصیات جیسے اوسط، تغیر اور معیاری انحراف وغیرہ کا مطالعہ کرنا چاہتے ہیں۔',
    'هیله ده چې تصادفي متغیر او د وړاندې کولو طریقې یې لکه احتمالي وېش او احتمالي تابع مو پوهېدلي وي. اوس غواړو د هغه ځانګړنې لکه منځنی، واریانس او معیاري انحراف او نور وڅېړو.')
b.h('2.2.5 Definition of mathematical expectation or expected value of a random variable', '2.2.5 تصادفی متغیر کی ریاضیاتی توقع یا متوقع قیمت کی تعریف', '2.2.5 د تصادفي متغیر د ریاضي تمې یا تمه شوي قیمت تعریف')
b.p('Mathematical expectation or expected value of a random variable is defined as “the mean of a random variable over a very large number of trails”. If X is a discrete random variable having the following probability distribution',
    'تصادفی متغیر کی ریاضیاتی توقع یا متوقع قیمت کی تعریف یوں ہے: “بہت بڑی تعداد میں آزمائشوں پر تصادفی متغیر کا اوسط”۔ اگر X ایک منفصل تصادفی متغیر ہو جس کی احتمالی تقسیم درج ذیل ہو',
    'د تصادفي متغیر ریاضي تمه یا تمه شوی قیمت داسې تعریف کېږي: “د ډېرو زیاتو ازمېښتونو په اوږدو کې د تصادفي متغیر منځنی”. که X یو منفصل تصادفي متغیر وي چې لاندې احتمالي وېش ولري')
b.grid('stat12-t-expectation-general', ['$X$', '$p(x)$', '$X\\,p(x)$'],
       [['$x_1$', '$p(x_1)$', '$x_1\\,p(x_1)$'], ['$x_2$', '$p(x_2)$', '$x_2\\,p(x_2)$'], ['$\\vdots$', '$\\vdots$', '$\\vdots$'], ['$x_n$', '$p(x_n)$', '$x_n\\,p(x_n)$'], ['Total', '1', '$\\sum_{i=1}^{n}x_i\\,p(x_i)$']])
b.p('The expected value of X is denoted by E(X) and its formula is given by $E(X)=\\sum_{i=1}^{n}x_i\\,p(x_i)$, provided it exists.',
    'X کی متوقع قیمت کو E(X) سے ظاہر کرتے ہیں اور اس کا فارمولا $E(X)=\\sum_{i=1}^{n}x_i\\,p(x_i)$ ہے، بشرطیکہ یہ موجود ہو۔',
    'د X تمه شوی قیمت په E(X) ښودل کېږي او فورمول یې $E(X)=\\sum_{i=1}^{n}x_i\\,p(x_i)$ دی، په دې شرط چې شتون ولري.')
b.h('Example 2.8', 'مثال 2.8', 'بېلګه 2.8')
b.p('A random variable X has the following probability distribution', 'ایک تصادفی متغیر X کی احتمالی تقسیم درج ذیل ہے', 'یو تصادفي متغیر X لاندې احتمالي وېش لري')
b.dist('stat12-t-ex2-8', ['0', '1', '2', '3'], ['1/7', '3/7', '2/7', '1/7'], total=None)
b.p('Find the mean or expected value of X, i.e. E(X).', 'X کا اوسط یا متوقع قیمت یعنی E(X) معلوم کریں۔', 'د X منځنی یا تمه شوی قیمت یعنې E(X) پیدا کړئ.')
b.h(*SOL)
b.grid('stat12-t-ex2-8-sol', ['$X$', '$p(x)$', '$X\\,p(x)$'],
       [['0', '1/7', '0'], ['1', '3/7', '3/7'], ['2', '2/7', '4/7'], ['3', '1/7', '3/7'], ['Total', '1', '10/7']])
b.eq(r'\text{Mean}=E(X)=\sum_{x=0}^{3}x_i\,p(x_i)=\frac{10}{7}=1.43')
b.h('Example 2.9', 'مثال 2.9', 'بېلګه 2.9')
b.p('A discrete random variable can have the values $x_1=3$, $x_2=8$, and $x_3=10$ and the respective probabilities are 0.2, 0.7 and 0.1. Determine the mean.',
    'ایک منفصل تصادفی متغیر کی قیمتیں $x_1=3$، $x_2=8$ اور $x_3=10$ ہو سکتی ہیں اور متعلقہ احتمالات 0.2، 0.7 اور 0.1 ہیں۔ اوسط معلوم کریں۔',
    'یو منفصل تصادفي متغیر کولای شي قیمتونه $x_1=3$، $x_2=8$ او $x_3=10$ ولري او اړوند احتمالونه یې 0.2، 0.7 او 0.1 دي. منځنی یې وټاکئ.')
b.h(*SOL)
b.mlines([r'\text{By definition } E(X)=\sum_{i=1}^{n}x_i\,p(x_i)', r'\phantom{\text{By definition } E(X)}=x_1p(x_1)+x_2p(x_2)+x_3p(x_3)'])
rec = b.build('stat12-p025-expectation', '2.2.4–2.2.5 Mathematical expectation — Examples 2.7–2.9', '2.2.4–2.2.5 ریاضیاتی توقع — مثالیں 2.7–2.9', '2.2.4–2.2.5 ریاضي تمه — بېلګې 2.7–2.9', 25, [41, 42])

if __name__ == '__main__':
    save(25, [(2, rec)])
