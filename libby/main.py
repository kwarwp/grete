# grete.libby.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
CAMPO = "https://image.freepik.com/fotos-gratis/paisagem-de-campo-de-golfe_1388-96.jpg"
CASAL = "https://images.vexels.com/media/users/3/129903/isolated/preview/c996f5193090b3a642ffc069bc81da0c-silhueta-do-casal-andando-12-by-vexels.png

def boyfriendsatthecamp():
    campo = Cena (img = CAMPO)
    casal = Elemento(img = CASAL, tit = "casal", style = dict(left = 150, top = 60, height = 200))
    txtcasal = Texto(casal,"let's eat something!")
    casal.entra(campo)
    casal.vai = txtcasal.vai
    campo.vai()
    
    
loversatthecamp()

#OFFICE1 = "https://imgur.com/gallery/88uA2AT?s=wa"
# "https://i.imgur.com/9Vg7DzJ.jpg"
# "https://i.imgur.com/haPQ4rZ.jpg"
# "https://i.imgur.com/Ax1XDBU.jpg"
#OBJECTS
# tomada = "https://i.imgur.com/l6INRuQ.jpg"
# interruptor = "https://i.imgur.com/olpkjL0.jpg"
# interfone = "https://i.imgur.com/4s1Pbpv.jpg"
# extintor = "https://i.imgur.com/AJzKYaE.jpg"
# garrafa térmica = "https://i.imgur.com/M9oUgH6.jpg"
# bebedouro = "https://i.imgur.com/GDRYgs3.jpg"