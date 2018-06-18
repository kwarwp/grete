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
trig_n  = "https://i.imgur.com/9ZcjTjb.jpg"
trig_e  = "https://i.imgur.com/SyHdvjw.jpg"
trig_s  = "https://i.imgur.com/ChRcEvB.jpg"
trig_o  = "https://i.imgur.com/JD6oGRg.jpg"
hq = "https://imgur.com/hib4z1f.jpg"
TRIG = None
def trigonometria():
    global TRIG
    if TRIG:
        return TRIG
        
    def _foi_geo():
        from naomi.main import geografia
        geografia().sul.vai()
        
    def _vai_geo():
        _vai_geo = _foi_geo
        _vai = Cena(hq)
        def redir():
            _vai.vai = _foi_geo
        historia = Cena(hq, _vai, _vai, _vai)
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
    TRIG = _sala = Sala(trig_n,trig_e,trig_s,trig_o, "trig")
    from naomi.main import Elemento
    _sala.sul.meio = Cena(hq, vai = vai_geo)
    vdgball = Elemento(ball, tit = "microscope", drag=True,
        x = 610, y = 140, w = 80, h = 90, drop="glow ball",
        cena=_sala.oeste, texto="please, help me, fix my name")
    eglobe = Elemento(globe, tit = "volcano", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="earth globe",
        cena=_sala.leste, texto="please, help me, fix my name")
    volc = Elemento(volcano, tit = "glow ball", drop="volcano",
        x = 30, y = 500, w = 100, h = 120,
        cena=_sala.leste, texto="please, help me, fix my name")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()
