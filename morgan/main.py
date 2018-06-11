# grete.morgan.main.py
Principals_room_n = "https://i.imgur.com/U9ixbT0.jpg"
Principals_room_o = "https://i.imgur.com/gxOcDsS.jpg"
Principals_room_l = "https://i.imgur.com/SV1Ko1N.jpg"
Principals_room_s = "https://i.imgur.com/V85pfUS.jpg"
# objects
clips = "https://i.imgur.com/Z25C40V.jpg"
door_lock = "https://i.imgur.com/q1tJiqJ.jpg"
keyboard = "https://i.imgur.com/EM4mZq2.jpg"
power_plug ="https://i.imgur.com/4eX2x0y.jpg"
pipe = "https://i.imgur.com/IWX6ah1.jpg"
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
    caixa = Elemento(caixa_mae, tit = "pipe", drag=True,
        x = 480, y = 140, w = 180, h = 290, drop="glow ball",
       cena=_sala.norte, texto="please, help me, fix my name")
    clip  = Elemento(clips, tit = "power plug", drag=True,
        x = 260, y = 410, w = 80, h = 100, drop="clips",
        cena=_sala.leste, texto="please, help me, fix my name")

    pipes = Elemento(pipe, tit = "motherboard", drop="cano",
        x = 500, y = 5, w = 100, h = 120,
        cena=_sala.norte, texto="please, help me, fix my name")
    power = Elemento(power_plug, tit = "pipe", drag=True,
        x = 510, y = 360, w = 100, h = 90, drop="glow ball",
       cena=_sala.leste, texto="please, help me, fix my name")
    doorl = Elemento(door_lock, tit = "keyboard", drag=True,
        x = 440, y = 380, w = 80, h = 100, 
        cena=_sala.sul, texto="please, help me, fix my name")
    keyboard_ = Elemento(keyboard, tit = "clip", drop="keyboard",
        x = 300, y = 300, w = 100, h = 70,
        cena=_sala.leste, texto="please, help me, fix my name")

    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()