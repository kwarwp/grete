# grete.anastasia.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
children = "https://i.imgur.com/SAjYpW5.jpg"
bars = "https://i.imgur.com/4g9dJdv.jpg"
grandstand = "https://i.imgur.com/6PYwS0s.jpg"
reflector = "https://i.imgur.com/U41sbtV.jpg"
light_post = "https://i.imgur.com/Jk68bvK.jpg"
ball = "https://i.imgur.com/bMUHNdH.jpg"
gimnasium_e = "https://i.imgur.com/RVIqCjp.jpg"
gimnasium_l = "https://i.imgur.com/kdnYpkh.jpg"
gimnasium_n = "https://i.imgur.com/befIyyM.jpg"
gimnasium_s = "https://i.imgur.com/5SnGZmp.jpg"
gimnasium = None
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
    children_ = Elemento(napkin_holder, tit = "reflector", drag=True,
        x = 310, y = 450, w = 70, h = 60, drop="children",
        cena=_sala.norte, texto="please, help me, fix my name")
    bars_ = Elemento(microwave, tit = "grandstand", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="bars",
        cena=_sala.oeste, texto="please, help me, fix my name")
    grandstand_ = Elemento(spray, tit = "bars",
        x = 360, y = 70, w = 80, h = 70, drop="grandstand",
        cena=_sala.leste, texto="please, help me, fix my name")
    reflector_ = Elemento(vase, tit = "ball", drag=True,
        x = 300, y = 275, w = 100, h = 140, drop="reflector",
        cena=_sala.norte, texto="please, help me, fix my name")
    light_post_ = Elemento(ligth_fixture, tit = "children", drag=True,
        x = 50, y = 40, w = 100, h = 100, drop="light_post",
        cena=_sala.sul, texto="please, help me, fix my name")
    ball_ = Elemento(dispenser, tit = "ligthpost",
        x = 30, y = 500, w = 100, h = 120,drop="ball",
        cena=_sala.leste, texto="please, help me, fix my name")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    gimnasium().norte.vai()
