# grete.stacy.main.py
# grete.sara.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
BEACH = "http://casadeluxoemcamboinhas.com.br/wp-content/uploads/2015/01/28506.jpg"
FUNNYDOG = "http://www.instatube.com.br/wp-content/uploads/2015/08/pugs-mais-engracados-do-mundo-vi-480x293.jpg"

def dogatthebeach():
    beach = Cena ("http://casadeluxoemcamboinhas.com.br/wp-content/uploads/2015/01/28506.jpg")
    funnydog = Elemento("http://www.instatube.com.br/wp-content/uploads/2015/08/pugs-mais-engracados-do-mundo-vi-480x293.jpg", tit = "FUNNYDOG",  style = dict(left = 150, top = 60, widht = 60, height = 200))
    txtfunnydog = Texto(beach,"Do you need dolly?")
    funnydog.entra(beach)
    funnydog.vai = txtfunnydog.vai
    beach.vai()
    
    
dogatthebeach()