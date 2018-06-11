# grete.libby.main.py
from _spy.vitollino.main import Cena,Elemento,Texto, Sala, INVENTARIO
#CAMPO = "https://image.freepik.com/fotos-gratis/paisagem-de-campo-de-golfe_1388-96.jpg"
#CASAL = "https://images.vexels.com/media/users/3/129903/isolated/preview/c996f5193090b3a642ffc069bc81da0c-silhueta-do-casal-andando-12-by-vexels.png
'''
def boyfriendsatthecamp():
    campo = Cena (img = CAMPO)
    casal = Elemento(img = CASAL, tit = "casal", style = dict(left = 150, top = 60, height = 200))
    txtcasal = Texto(casal,"let's eat something!")
    casal.entra(campo)
    casal.vai = txtcasal.vai
    campo.vai()
    
    
loversatthecamp()
'''
sn = "https://i.imgur.com/evlSZig.jpg"
sl = "https://i.imgur.com/9Vg7DzJ.jpg"
ss = "https://i.imgur.com/haPQ4rZ.jpg"
so = "https://i.imgur.com/Ax1XDBU.jpg"
#OBJECTS
# tomada = "https://i.imgur.com/l6INRuQ.jpg"
# interruptor = "https://i.imgur.com/olpkjL0.jpg"
# interfone = "https://i.imgur.com/4s1Pbpv.jpg"
# extintor = "https://i.imgur.com/AJzKYaE.jpg"
# garrafa térmica = "https://i.imgur.com/M9oUgH6.jpg"
bebedouro = "https://i.imgur.com/GDRYgs3.jpg"
SEC = None
def trigonometria():
    global SEC
    if SEC:
        return SEC
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    SEC = _sala = Sala(sn,sl,ss,so, "sec")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    bebed = Elemento(bebedouro, tit = "microscope", drag=True,
        x = 210, y = 140, w = 80, h = 90, drop="glow ball",
        cena=_sala.oeste, texto="please, help me, fix my name")
    '''
    eglobe = Elemento(globe, tit = "volcano", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="earth globe",
        cena=_sala.leste, texto="please, help me, fix my name")
    volc = Elemento(volcano, tit = "glow ball", drop="volcano",
        x = 30, y = 500, w = 100, h = 120,
        cena=_sala.leste, texto="please, help me, fix my name")
'''
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()