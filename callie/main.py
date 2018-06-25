# grete.callie.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
kit_n = "https://i.imgur.com/98JoHe0.jpg"
kit_o = "http://i.imgur.com/0Ix7Dd3.jpg"
kit_s = "https://i.imgur.com/0Zztrs5.jpg"
kit_l = "https://i.imgur.com/S12NoXf.jpg"

#Objects:
grao_de_bico = "https://i.imgur.com/JdP7kbV.jpg"
coifa = "https://i.imgur.com/6pbktzm.jpg"
batata_doce = "https://i.imgur.com/OkdQ390.jpg"
azeite = "https://i.imgur.com/IgdYch1.jpg"
adocante = "https://i.imgur.com/8oYmzyp.jpg"
fogao = "https://i.imgur.com/fV5Xo6F.jpg"
from _spy.vitollino.main import STYLE, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
PRR = None
def kitchen():
    global PRR
    if PRR:
        return PRR
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    PRR = _sala = Sala(Principals_room_n,Principals_room_o,Principals_room_l,Principals_room_s, "principal")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    grao = Elemento(grao_de_bico, tit = "coif", drag=True,
        x = 480, y = 140, w = 180, h = 290, drop="grao",
       cena=_sala.norte, texto="please, help me, fix my name")
    coif = Elemento(coifa, tit = "chick peas", drag=True,
        x = 260, y = 410, w = 80, h = 100, drop="coifa",
        cena=_sala.leste, texto="please, help me, fix my name")

    sweet_potato = Elemento(sweetpotato, tit = "olive oil", drop="batata",
        x = 500, y = 5, w = 100, h = 120,
        cena=_sala.norte, texto="please, help me, fix my name")
    olive_oil = Elemento(oliveoil, tit = "sweet potato", drag=True,
        x = 510, y = 360, w = 100, h = 90, drop="glow ball",
       cena=_sala.leste, texto="please, help me, fix my name")
    doorl = Elemento(door_lock, tit = "keyboard", drag=True,
        x = 440, y = 380, w = 80, h = 100, 
        cena=_sala.sul, texto="please, help me, fix my name")
    adocante = Elemento(sweetner, tit = "cokie", drop="keyboard",
        x = 300, y = 300, w = 100, h = 70,
        cena=_sala.leste, texto="please, help me, fix my name")
    cokie = Elemento(fogao, tit = "sweetner", drop="cano",
        x = 500, y = 5, w = 100, h = 120,
        cena=_sala.norte, texto="please, help me, fix my name")

    return _sala

if __name__ == "__main__": 
    INVENTARIO.inicia()
    kitchen().norte.vai()
