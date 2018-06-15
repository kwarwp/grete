# grete.courtney.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
children = "https://i.imgur.com/4fTrn8X.jpg"
school_house_n = "https://i.imgur.com/F8vDljG.jpg"
school_house_o = "https://i.imgur.com/Cy3pV4j.jpg"
school_house_s = "https://i.imgur.com/A0CmC45.jpg"
school_house_l = "https://i.imgur.com/wu3DN2C.jpg"
microwave = "https://i.imgur.com/Zp8ke2j.jpg"
spray = "https://i.imgur.com/UHXzvdz.jpg"
vase = "https://i.imgur.com/yBMisN8.jpg"
ligth_fixture = "https://i.imgur.com/1yslKV5.jpg"
dispenser = "https://i.imgur.com/o9raZp8.jpg"
napkin_holder = "https://i.imgur.com/czetnka.jpg"
school_house = None
def school_houser():
    global school_house
    if school_house:
        return school_house
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    school_house = _sala = Sala(school_house_n,school_house_l,school_house_s,school_house_o, "trig")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    napkin_holder_ = Elemento(napkin_holder, tit = "vase", drag=True,
        x = 310, y = 450, w = 70, h = 60, drop="napkin_holder",
        cena=_sala.norte, texto="please, help me, fix my name")
    microwave_ = Elemento(microwave, tit = "napkin_holder", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="microwave",
        cena=_sala.oeste, texto="please, help me, fix my name")
    spray_ = Elemento(spray, tit = "dispenser",
        x = 30, y = 500, w = 1000, h = 50, drop="spray",
        cena=_sala.leste, texto="please, help me, fix my name")
    vase_ = Elemento(vase, tit = "spray", drag=True,
        x = 300, y = 275, w = 100, h = 140, drop="vase",
        cena=_sala.norte, texto="please, help me, fix my name")
    ligth_fixture_ = Elemento(ligth_fixture, tit = "microwave", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="ligth_fixture",
        cena=_sala.sul, texto="please, help me, fix my name")
    dispenser_ = Elemento(dispenser, tit = "ligth_fixture",
        x = 30, y = 500, w = 100, h = 120,drop="dispenser",
        cena=_sala.leste, texto="please, help me, fix my name")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    school_houser().norte.vai()