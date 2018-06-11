# grete.morgan.main.py
Principals_room_n = "https://i.imgur.com/U9ixbT0.jpg"
Principals_room_o = "https://i.imgur.com/gxOcDsS.jpg"
Principals_room_l = "https://i.imgur.com/SV1Ko1N.jpg"
Principals_room_s = "https://i.imgur.com/V85pfUS.jpg"
# objects
clips = "https://i.imgur.com/Z25C40V.jpg"
fechadura = "https://i.imgur.com/q1tJiqJ.jpg"
teclado = "https://i.imgur.com/EM4mZq2.jpg"
tomada_telefonica ="https://i.imgur.com/4eX2x0y.jpg"
fiacao_eletrica = "https://i.imgur.com/IWX6ah1.jpg"
caixa_mae = "https://i.imgur.com/THLu9uv.jpg"
from _spy.vitollino.main import STYLE, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
PRR = None
def trigonometria():
    global PRR
    if PRR:
        return PRR
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    PRR = _sala = Sala(Principals_room_n,Principals_room_o,Principals_room_l,Principals_room_s, "principal")
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