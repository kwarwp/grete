# grete.courtney.main.py
#RESOLVIDO -PRONTO
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
TIRINHA_DO_CLAUDEMILSON = "https://i.imgur.com/yX187fL.jpg"

School_House = None
def school_house_():
    global School_House
    if School_House:
        return School_House
        
    def _gone_school_house_():
        try:
            gimnasium().leste.vai()
        except:
            from anastasia.main import gimnasium
            gimnasium().leste.vai()
    def _go_room23():
        try:
            room23().norte.vai()
        except:
            from lisa.main import room23 
            room23().norte.vai()
        
    def _go_school_house_():
        School_House.sul.meio = Cena(vai=_gone_school_house_)
        _vai = Cena()
        def redir():
            _vai.vai = _gone_school_house_
        historia = Cena(TIRINHA_DO_CLAUDEMILSON, _vai, _vai, _vai)
        texto = """ One day, there was a manifestation against Claudemilson,
        and she did not like it at all. So she made the demonstrators hear 'Funk Carioca' during 10 hours... """ 
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
    def go_school_house():
        _go_school_house_()
    School_House = _sala = Sala(school_house_n,school_house_l,school_house_s,school_house_o, "trig")
    from naomi.main import Elemento
    _sala.sul.meio = Cena(vai=go_school_house)
    _sala.norte.meio = Cena(vai=_go_room23)
    napkin_holder_ = Elemento(napkin_holder, tit = "vase", drag=True,
        x = 310, y = 450, w = 70, h = 60, drop="napkin holder",
        cena=_sala.norte, texto="Please help me, fix my name.")
    microwave_ = Elemento(microwave, tit = "napkin holder", drag=True,
        x = 430, y = 100, w = 200, h = 150, drop="microwave",
        cena=_sala.oeste, texto="Please help me, fix my name.")
    spray_ = Elemento(spray, tit = "dispenser",
        x = 360, y = 70, w = 80, h = 70, drop="spray",
        cena=_sala.leste, texto="Please help me, fix my name.")
    vase_ = Elemento(vase, tit = "spray", drag=True,
        x = 300, y = 275, w = 100, h = 140, drop="vase",
        cena=_sala.norte, texto="Please help me, fix my name.")
    ligth_fixture_ = Elemento(ligth_fixture, tit = "microwave", drag=True,
        x = 50, y = 40, w = 100, h = 100, drop="light fixture",
        cena=_sala.sul, texto="Please help me, fix my name.")
    dispenser_ = Elemento(dispenser, tit = "light fixture",
        x = 330, y = 325, w = 30, h = 40,drop="dispenser",
        cena=_sala.leste, texto="Please help me, fix my name.")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    school_house_().norte.vai()