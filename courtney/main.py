# grete.courtney.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
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
        geografia().sul.vai()except:
            from libby.main import secretary
            secretary().sul.vai()
        
    def _go_school_house():
        school_house_.sul.meio.vai = _gone_school_house
        _vai = Cena(TIRINHA_DO_CLAUDEMILSON)
        def redir():
            _vai.vai = _gone_gimnasiun
        historia = Cena(TIRINHA_DO_CLAUDEMILSON, _vai, _vai, _vai)
        texto = """ One day, there was a manifestation against Claudemilson, and she didnÂ´t like it. She made the people of the manifestation hear Funk Carioca during 10 hours.. """ 
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
    school_house = _sala = Sala(school_house_n,school_house_l,school_house_s,school_house_o, "trig")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    napkin_holder_ = Elemento(napkin_holder, tit = "vase", drag=True,
        x = 310, y = 450, w = 70, h = 60, drop="napkin_holder",
        cena=_sala.norte, texto="please, help me, fix my name")
    microwave_ = Elemento(microwave, tit = "napkin_holder", drag=True,
        x = 430, y = 100, w = 200, h = 150, drop="microwave",
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
        x = 330, y = 325, w = 30, h = 40,drop="dispenser",
        cena=_sala.leste, texto="please, help me, fix my name")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()