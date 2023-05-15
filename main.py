def change_text(id,text):
  Element(id).write(text)
  
def change_innerhtml(id,html):
  Element(id).innerHtml=html

def change_innerhtmlandtext(id,html,text):
  change_innerhtml(id,html)
  change_text(id,text)

def adolf(id,targetid,html,text):
  change_text(targetid,text)
  change_innerhtml(id,html)
