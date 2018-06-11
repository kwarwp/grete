# grete.sarah.main.py
from _spy.vitollino.main import STYLE, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
QUADRA_n = "https://i.imgur.com/befIyyM.jpg"
QUADRA_l = "https://i.imgur.com/kdnYpkh.jpg"
QUADRA_o = "https://i.imgur.com/RVIqCjp.jpg"
QUADRA_s = "https://i.imgur.com/5SnGZmp.jpg"
TRAVE = "https://i.imgur.com/SAjYpW5.jpg"
GRADE = "https://i.imgur.com/4g9dJdv.jpg"
ARQUIBANCADA = "https://i.imgur.com/6PYwS0s.jpg"
POSTE = "https://i.imgur.com/Jk68bvK.jpg"
HOLOFOTE = "https://i.imgur.com/U41sbtV.jpg"
BOLA = "https://i.imgur.com/RVIqCjp.jpg"
TRIG = None
def trigonometria():
    global TRIG
    if TRIG:
        return TRIG
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    TRIG = _sala = Sala(QUADRA_n,QUADRA_l,QUADRA_o,QUADRA_s, "quadra")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    '''
    vdgball = Elemento(ball, tit = "microscope", drag=True,
        x = 610, y = 140, w = 80, h = 90, drop="glow ball",
        cena=_sala.oeste, texto="please, help me, fix my name")
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
