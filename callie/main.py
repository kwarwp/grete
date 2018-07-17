# grete.callie.main.py
#TEXTO E TIRINHA
from _spy.vitollino.main import Cena,Elemento,Texto
kit_n = "https://i.imgur.com/98JoHe0.jpg"
kit_s = "http://i.imgur.com/0Ix7Dd3.jpg"
kit_l = "https://i.imgur.com/0Zztrs5.jpg"
kit_o = "https://i.imgur.com/S12NoXf.jpg"

#Objects:
grao_de_bico = "https://i.imgur.com/JdP7kbV.jpg"
coifa = "https://i.imgur.com/6pbktzm.jpg"
sweetpotato = "https://i.imgur.com/OkdQ390.jpg"
oliveoil = "https://i.imgur.com/IgdYch1.jpg"
sweetner = "https://i.imgur.com/8oYmzyp.jpg"
door_lock = "https://i.imgur.com/BmXgyxl.png"
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
    PRR = _sala = Sala(kit_n,kit_o,kit_l,kit_s, "principal")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    grao = Elemento(grao_de_bico, tit = "suction hood", drag=True,
        x = 670, y = 390, w = 100, h = 100, drop="chick peas",
       cena=_sala.leste, texto="Please help me, fix my name.")
    coif = Elemento(coifa, tit = "chick peas", drag=True,
        x = 0, y = 0, w = 700, h = 100, drop="suction hood",
        cena=_sala.sul, texto="Please help me, fix my name.")

    sweet_potato = Elemento(sweetpotato, tit = "olive oil", drop="sweet potato",
        x = 740, y = 500, w = 60, h = 60,
        cena=_sala.norte, texto="Please help me, fix my name.")
    olive_oil = Elemento(oliveoil, tit = "sweet potato", drag=True,
        x = 210, y = 510, w = 100, h = 90, drop="olive oil",
       cena=_sala.norte, texto="Please help me, fix my name.")
    doorl = Elemento(door_lock, tit = "stove", drag=True,
        x = 440, y = 420, w = 80, h = 100, drop="door lock",
        cena=_sala.leste, texto="Please help me, fix my name.")
    adocante = Elemento(sweetner, tit = "door lock", drop="sweetner",
        x = 350, y = 530, w = 100, h = 70,
        cena=_sala.norte, texto="Please help me, fix my name.")
    cokie = Elemento(fogao, tit = "sweetner", drop="stove",
        x = 500, y = 500, w = 100, h = 120,
        cena=_sala.sul, texto="Please help me, fix my name.")

    return _sala

if __name__ == "__main__": 
    INVENTARIO.inicia()
    kitchen().norte.vai()
