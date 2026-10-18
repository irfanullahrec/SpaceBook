"""Source block boundaries, distinct from scan/OCR line wrapping."""
LAYOUT = {
 'phys12-front-cover': [{'type':'lines','indices':[0,1,2,3]}],
 'phys12-front-quotation':[{'type':'paragraph','indices':[0,1]},{'type':'paragraph','indices':[2]},{'type':'heading','indices':[3]}],
 'phys12-front-title':[{'type':'lines','indices':[0,1]}],
 'phys12-front-publication':[
   {'type':'paragraph','indices':[0]}, {'type':'paragraph','indices':[1,2]},
   {'type':'heading','indices':[3]}, {'type':'lines','indices':list(range(4,11))},
   {'type':'paragraph','indices':[11]}, {'type':'paragraph','indices':[12]},
   {'type':'heading','indices':[13]}, {'type':'paragraph','indices':[14]},
   {'type':'lines','indices':[15,16,17]}, {'type':'paragraph','indices':[18]},
   {'type':'paragraph','indices':[19]}, {'type':'lines','indices':[20,21,22,23]}, {'type':'visual'},
 ],
 'phys12-front-preface':[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1,2]},{'type':'paragraph','indices':[3]}],
 'phys12-front-contents':[{'type':'table','indices':list(range(12))}],
 'phys12-front-outcomes1':[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'list','indices':list(range(2,10))}],
 'phys12-front-outcomes2':[{'type':'list','indices':list(range(21))},{'type':'paragraph','indices':[21]}],
 'phys12-front-coulomb-introduction':[
   {'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1,2]},
   {'type':'heading','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},
   {'type':'visual'},{'type':'paragraph','indices':[6]},
 ],
 'phys12-front-coulomb-equations':[
   {'type':'paragraph','indices':[0]}, {'type':'equation','indices':[1]}, {'type':'equation','indices':[2]},
   {'type':'equation','indices':[3]}, {'type':'equation','indices':[4]}, {'type':'paragraph','indices':[5]},
   {'type':'paragraph','indices':[6]}, {'type':'equation','indices':[7]}, {'type':'paragraph','indices':[8]},
   {'type':'equation','indices':[9]}, {'type':'paragraph','indices':[10]}, {'type':'equation','indices':[11]},
   {'type':'paragraph','indices':[12]},
 ],
 'phys12-front-permittivity':[
   {'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]}, {'type':'equation','indices':[2]},
   {'type':'equation','indices':[3]},{'type':'heading','indices':[4]},{'type':'paragraph','indices':[5]},
   {'type':'paragraph','indices':[6]},{'type':'equation','indices':[7]},{'type':'paragraph','indices':[8]},
   {'type':'equation','indices':[9]},
 ],
}
