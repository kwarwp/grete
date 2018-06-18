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
sl = "https://i.imgur.com/Ax1XDBU.jpg"
ss = "https://i.imgur.com/9Vg7DzJ.jpg"
so = "https://i.imgur.com/haPQ4rZ.jpg"
#OBJECTS
tomada = "https://i.imgur.com/l6INRuQ.jpg"
interruptor = "https://i.imgur.com/olpkjL0.jpg"
interfone = "https://i.imgur.com/4s1Pbpv.jpg"
extintor = "https://i.imgur.com/AJzKYaE.jpg"
garrafa_termica = "https://i.imgur.com/M9oUgH6.jpg"
bebedouro = "https://i.imgur.com/GDRYgs3.jpg"
        
# grete.amanda.main.py
from _spy.vitollino.main import STYLE, INVENTARIO, Sala, Texto, Cena
STYLE["width"] = 800
STYLE["height"] = "600px"
children = "https://i.imgur.com/4fTrn8X.jpg"
toy = "https://i.imgur.com/57cOaZ9.jpg"
sckoolhouse = "https://i.imgur.com/oXsdN2c.jpg"
leyden  = "https://i.imgur.com/abeXKwL.jpg"
volcano  = "https://i.imgur.com/4Y5aie8.jpg"
globe  = "https://i.imgur.com/EQtHzod.jpg"
ball  = "https://i.imgur.com/rBbRsFU.jpg"
TIRINHA_DO_CLAUDEMILSON = "https://i.imgur.com/yX187fL.jpg"
TRIG = None
def trigonometria():
    global TRIG
    if TRIG:
        return TRIG
        
    def _foi_geo():
        try:
            geografia().sul.vai()
        except:
            from stacy.main import trigonometria as tg
            tg().sul.vai()
        
    def _vai_geo():
        TRIG.sul.meio.vai = _foi_geo
        _vai = Cena(TIRINHA_DO_CLAUDEMILSON)
        def redir():
            _vai.vai = _foi_geo
        historia = Cena(TIRINHA_DO_CLAUDEMILSON, _vai, _vai, _vai)
        texto = """Then when he stay house, he sit on the sofa,and turn on the TV and saw the following head line:
  - Manifestation on the street Dr. poop my pants.
 The manifestation is happening behind her house, and have peoples whif plates, turning down bus and screaming:
   - Became Robervald, became Claudemilson, became Robervald Claudemilson!!!!!!!!!!!!!!!
  He tired of all Claudemilson's and decide go sleep.
  Then he wake up at morning, and cout to her daddy and his mother of the crazy nightmare he has, and sit to turn on the TV and saw:
  - has a manifestation here the peoples are screaming: BECAME CLAUDEMILSON!!!!!!!!!!!!!!"""
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
        
    def vai_geo():
        _vai_geo()
    TRIG = _sala = Sala(sn,sl,ss,so, "trig")
    from naomi.main import Elemento
    _sala.sul.meio = Cena(TIRINHA_DO_CLAUDEMILSON, vai = vai_geo)
    vdgball = Elemento(tomada, tit = "microscope", drag=True,
        x = 610, y = 140, w = 80, h = 90, drop="power outlet",
        cena=_sala.oeste, texto="please, help me, fix my name")
    eglobe = Elemento(bebedouro, tit = "volcano", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="drink fountain",
        cena=_sala.leste, texto="please, help me, fix my name")
    volc = Elemento(extintor, tit = "glow ball", drop="fire extinguisher",
        x = 30, y = 500, w = 100, h = 120,
        cena=_sala.leste, texto="please, help me, fix my name")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()
