"""PDF3: Qur'anic verse page (Al-Hujurat 10, Urdu rendering) and inner title page."""
from class12_statistics_common import Builder, save

b = Builder()
b.add('quotation', 'مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحم کیا جائے۔',
      'مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحم کیا جائے۔',
      'مومنان خو یو د بل وروڼه دي. نو د خپلو دوو وروڼو ترمنځ روغه وکړئ او له الله څخه ووېرېږئ چې پر تاسو رحم وشي.')
b.paras[-1].update({'sourceLanguage': 'ur', 'english': 'The believers are but brothers, so make peace between your two brothers and fear Allah so that you may receive mercy.'})
b.add('lines', '(سورۃ الحجرات: ۱۰)', '(سورۃ الحجرات: ۱۰)', '(سورة الحجرات: ۱۰)')
b.paras[-1].update({'sourceLanguage': 'ur', 'english': '(Surah Al-Hujurat: 10)'})
b.h('Statistics for Grade XII', 'شماریات برائے جماعت دوازدہم', 'احصایه د دولسم ټولګي لپاره')
b.p('Khyber Pakhtunkhwa Textbook Board Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
b.p('NOT FOR SALE', 'برائے فروخت نہیں', 'د پلور لپاره نه ده')
rec = b.build('stat12-title-page', 'Verse and title page', 'آیت اور سرورقِ داخلی', 'آیت او داخلي سرلیک پاڼه', 3, ['i', 'ii'])
rec['translationNote'] = 'The verse is printed in Urdu; it is kept as printed, with an English rendering for the reader and a Pashto rendering. The board emblem is not reproduced.'

if __name__ == '__main__':
    save(3, [(1, rec)])
