def change_text(id,text):
  Element(id).write(text)
  
def change_innerhtml(id,html):
  Element(id).innerHtml=html

def change_innerhtmlandtext(id,html,text):
  change_innerhtml(id,html)
  change_text(id,text)

def adolf(id,targetid,text):
  global fundysymbol
  change_text(targetid,text)
  change_innerhtml(id,fundysymbol)
fundysymbol='<a href=\"https://www.youtube.com/watch?v=CEUPIET-r78\" target=\"_blank\" id=\"aadolf\">'
