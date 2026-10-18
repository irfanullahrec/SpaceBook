"""Native labelled geometry descriptors; positions are schematic unless stated."""
def geometry(caption,title,paths,labels,points=(),size=(500,320)):
 return {'type':'diagram','caption':caption,'diagram':{'type':'source-labelled-geometry','title':title,'width':size[0],'height':size[1],'paths':paths,'labels':[{'x':x,'y':y,'text':text} for x,y,text in labels],'points':points}}
def path(points,fill='none',stroke='#334155',dash=False):
 return {'points':points,'fill':fill,'stroke':stroke,'dash':dash}
AXES=[path([(80,285),(80,30)]),path([(40,240),(450,240)])]
AXIS_LABELS=[(78,22,'y'),(455,246,'x'),(57,265,'O')]
