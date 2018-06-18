# grete.anastasia.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
children = "https://i.imgur.com/SAjYpW5.jpg"
bars = "https://i.imgur.com/4g9dJdv.jpg”
grandstand = "https://i.imgur.com/6PYwS0s.jpg”
reflector = "https://i.imgur.com/U41sbtV.jpg”
light_post = "https://i.imgur.com/Jk68bvK.jpg”
ball = "https://i.imgur.com/bMUHNdH.jpg”
gimnasium_e = "https://i.imgur.com/RVIqCjp.jpg”
gimnasium_l = "https://i.imgur.com/kdnYpkh.jpg”
gimnasium_n = "https://i.imgur.com/befIyyM.jpg”
gimnasium_s = "https://i.imgur.com/5SnGZmp.jpg”

def gimnasium():
    global gimnasium
    if gimnasium:
        return gimnasium
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    school_house = _sala = Sala(gimnasium_n,gimnasium_l,gimnasium_s,gimnasium_o, "trig")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    children_ = Elemento(napkin_holder, tit = "vase", drag=True,
        x = 310, y = 450, w = 70, h = 60, drop="napkin_holder",
        cena=_sala.norte, texto="please, help me, fix my name")
    microwave_ = Elemento(microwave, tit = "napkin_holder", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="microwave",
        cena=_sala.oeste, texto="please, help me, fix my name")
    spray_ = Elemento(spray, tit = "dispenser",
        x = 360, y = 70, w = 80, h = 70, drop="spray",
        cena=_sala.leste, texto="please, help me, fix my name")
    vase_ = Elemento(vase, tit = "spray", drag=True,
        x = 300, y = 275, w = 100, h = 140, drop="vase",
        cena=_sala.norte, texto="please, help me, fix my name")
    ligth_fixture_ = Elemento(ligth_fixture, tit = "microwave", drag=True,
        x = 50, y = 40, w = 100, h = 100, drop="ligth_fixture",
        cena=_sala.sul, texto="please, help me, fix my name")
    dispenser_ = Elemento(dispenser, tit = "ligth_fixture",
        x = 30, y = 500, w = 100, h = 120,drop="dispenser",
        cena=_sala.leste, texto="please, help me, fix my name")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    gimnasium().norte.vai()
