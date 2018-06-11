# grete.amanda.main.py
from _spy.vitollino.main import STYLE, INVENTARIO, Sala
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
TRIG = None
def trigonometria():
    global TRIG
    if TRIG:
        return TRIG
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    '''
    # INVENTARIO.inicia()
    n_trig = Cena(trig_n)
    e_trig = Cena(trig_e, esquerda=n_trig)
    s_trig = Cena(trig_s, esquerda=e_trig, meio=Cena(vai=vai_geo))
    o_trig = Cena(trig_o, esquerda=s_trig, direita=n_trig)
    n_trig.esquerda, n_trig.direita = o_trig, e_trig
    s_trig.direita, e_trig.direita = o_trig, s_trig
    '''
    TRIG = _sala = Sala(trig_n,trig_e,trig_s,trig_o, "trig")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    vdgball = Elemento(ball, tit = "microscope", drag=True,
        x = 610, y = 140, w = 80, h = 90, drop="glow ball",
        cena=_sala.oeste, texto="please, help me, fix my name")
    eglobe = Elemento(globe, tit = "volcano", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="earth globe",
        cena=_sala.leste, texto="please, help me, fix my name")
    volc = Elemento(volcano, tit = "glow ball", drop="volcano",
        x = 30, y = 500, w = 100, h = 120,
        cena=_sala.leste, texto="please, help me, fix my name")
    # txtchildren = Texto(n_trig,"please, help me")
    
    #n_trig.vai()
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()