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
SECRETARY = None
def secretary():
    global SECRETARY
    if SECRETARY:
        return SECRETARY
        
    def _gone_secretary():
        try:
            gimnasium().sul.vai()
        except:
            from anastasia.main import gimnasium
            gimnasium().sul.vai()
        
    def _go_secretary():
        SECRETARY.oeste.meio.vai = _gone_secretary
        _vai = Cena()
        def redir():
            _vai.vai = _gone_secretary
        historia = Cena(TIRINHA_DO_CLAUDEMILSON, _vai, _vai, _vai)
        texto = """Cleison enter the school excitedly and sees the three excited secretaries boring, totally boring, that you would even want to die of so boring that they were. 
He went to talk  to them, and getting closer, he saw  on their  shirts ,the following phrase : 
‘ Become Claudemilson”.He said”hello” and they just said : “ Become Claudemillson  where’s your shirt?”
He said:
-I’m a former student, I just come to visit the school, then excuse me .                            book                                           leaving.
He got away, and the there of them looking at him leaving, just turning their heads, without booking away.
"""
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
        
    def go_secretary():
        _go_secretary()
    SECRETARY = _sala = Sala(sn,sl,ss,so, "trig")
    from naomi.main import Elemento
    _sala.oeste.meio = Cena(TIRINHA_DO_CLAUDEMILSON, vai = go_secretary)
    bebedouro_ = Elemento(bebedouro, tit = "switch", drag=True,
        x = 460, y = 192, w = 80, h = 90, drop="drinking fountain",
        cena=_sala.sul, texto="Please help me, fix my name.")
    tomada_ = Elemento(tomada, tit = "thermal bottle", drag=True,
        x = 185, y = 30, w = 80, h = 100, drop="socket",
        cena=_sala.leste, texto="Please help me, fix my name.")
    extintor_ = Elemento(extintor, tit = "socket", drag=True,
        x = 30, y = 500, w = 100, h = 120,drop="fire extinguisher",
        cena=_sala.leste, texto="Please help me, fix my name.")
    garrafa_termica_ = Elemento(garrafa_termica, tit = "fire extinguisher", drag=True,
        x = 520, y = 220, w = 90, h = 60, drop="thermal bottle",
        cena=_sala.sul, texto="Please help me, fix my name.")
    interfone_ = Elemento(interfone, tit = "drinking fountain", drag=True,
        x = 700, y = 220, w = 90, h = 60, drop="communicator",
        cena=_sala.sul, texto="Please help me, fix my name.")
    interruptor_ = Elemento(interruptor, tit = "communicator", drag=True,
        x = 100, y = 220, w = 90, h = 60, drop="switch",
        cena=_sala.oeste, texto="Please help me, fix my name.")
    return _sala

if __name__ == "__main__": 
    INVENTARIO.inicia()
    secretary().norte.vai()
