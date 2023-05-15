def change_text(id,text):
  Element(id).write(text)
  
def change_innerhtml(id,html):
  Element(id).innerHtml=html
